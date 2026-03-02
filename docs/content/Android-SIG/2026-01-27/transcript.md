SIG: Android SIG
Date: 2026-01-27
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:32 Good morning.
We can give it another few seconds for folks to connect.
**Cesar Munoz** 02:10 Good morning.
And I…
**Jason Plumb** 02:13 Good morning.
Somebody has really done a number on this document, let's see.
**Surbhi A** 02:23 Good morning. I was updating it a little. Went haywire.
**Jason Plumb** 02:29 I was like, somebody did a number on this thing? Yeah, it's fine. It's all good.
Okay.
David Graff, you look like a new name to me, maybe. I'm not sure if you have joined us before, but I'd like to say welcome before we get started.
**DavidGrath** 03:00 Thank you.
**Jason Plumb** 03:03 Cool, yeah, welcome.
**Cesar Munoz** 03:04 telecom.
**Jason Plumb** 03:05 If you have any agenda items or stuff that you'd want to talk about, feel free to either… I mean, the preferred approach is to drop them into this shared document. If you need a link to it, someone can put that in the chat.
Or you can just put it in the chat. Sometimes the meetings get full, it looks like our agenda is fairly light, so we can also just ad hoc bring stuff up. But yeah, if this is your first time joining, yeah, again, welcome.
**Cesar Munoz** 03:28 Welcome. Also, I think it… I just wanted to mention that I think it's pretty cool that we have
Nayankat.
with us today.
That's how it's pronounced. I love when that shows up. I don't know how you make it show up, but it's…
That's pretty cool, so… Wow.
**Hanson Ho** 03:47 What is this, 2013?
**Jason Plumb** 03:49 It is the best one.
I think it's the best one. And it doesn't always show up, yeah.
**Cesar Munoz** 03:57 It's the best one.
**Jason Plumb** 04:01 I don't even know which one I am, let's see.
I can't… I don't think you can tell, can you?
Someone else has to, like, see me typing these, and then determine what color I am?
Or how…
**Cesar Munoz** 04:13 You are a Wolverine.
**Hanson Ho** 04:16 Wolverine, okay, cool.
Anonymous, Wolverine. Not so anonymous.
**Jason Plumb** 04:22 cloth out. Okay.
**Hanson Ho** 04:26 Siri, nice to have you back with us. Let's open your PR.
**Surbhi A** 04:31 Yo.
I wanted to update the group about what's going on on this, so I went forward with implementing the attributes on the original HTTP span itself in the OKHTTP3 manual instrumentation, the OpenTelemetry Java instrumentation repo.
But I came… I hit a roadblock. Basically, in the tracing interceptor there. The span is closed as soon as the response is received. It does not wait for the response body to be read or the call to be finally concluded via
call ended, event callback, right? So those timings couldn't be included in the span. Also, if we were to implement waiting for the span.
It would have affected the current behavior, and there was no conclusive ending of this plan possible, because there are scenarios wherein response can be read, but response body is not closed. So the… it would… the connection would finally leak.
that we would not have any point to end the span, right? And there are other scenarios, right? If the client is not configured correctly, there are no read timeouts, there are no connection timeouts.
we would not have any place to end the span, right? We would need a thread to go and look for any open spans, and keep an account of the open spans, and then end them like how we did for the HTTP URL connection auto-instrumentation, right? So that would have affected the existing behavior. So that wasn't something that would have been an agreed approach.
So instead, I went forward with the next best possible option, which is what browser was recommending earlier as well, which is a standalone log record.
That contains all the timing attributes. So, now we have moved forward to that.
Like, and two, like, backends?
are not, right now, equipped to correlate two different signals, or
span, the HTTP span, and the timing attributes log record.
Because they generate metrics at ingestion time. For example, the Splunk backend generates metrics at ingestion time. So, for such backends to help them, there would be a configurable attribute if you want to copy the original HTTP span attributes to the log record as well.
In the interim, until all backends are ready, right, to relate the two, signals.
So, this.
**Jason Plumb** 07:07 So what other attributes would be helpful there?
**Surbhi A** 07:11 It was, like, right now, because different…
backends can take different approaches. I have gone forward with… like, I have suggested copying all the attributes, not a smaller list of that.
An approach could also be asking for a list of attributes that they want included.
And then including those. But then, there would be a complication of getting the right attribute keys from them, and checking for that in the span, and then adding that. Instead of that, it seemed easier to copy all the original HTTP span attributes.
**Jason Plumb** 07:57 Okay, I think I'm following, so where is that copying… where is that log record being created? It's in the telemetry, right? I mean, it's in the instrumentation.
**Surbhi A** 08:07 It's in the Network Timing Event Listener.
**Jason Plumb** 08:10 Okay.
**Surbhi A** 08:11 That's the new class.
Yeah, so all these attributes are added.
**Jason Plumb** 08:18 Right?
**Surbhi A** 08:20 Right now, did not implement the copying yet, but I will implement it soon, yeah.
**Jason Plumb** 08:26 Okay.
**Surbhi A** 08:28 So, in.
**Hanson Ho** 08:29 Is this?
**Surbhi A** 08:30 Yo.
**Hanson Ho** 08:31 No, no, go ahead, go ahead.
**Surbhi A** 08:32 So, in this… two things that I did in this log record as well is, like, there are… in the log record builder currently, the APIs for adding the top-level trace ID and span ID fields is not there, and you can't do that, right?
**Jason Plumb** 08:46 What do you mean? I thought it is there. I thought you could… I thought Log Record Builder had, trace information on it.
**Surbhi A** 08:53 It, like, in documentation, it does. In APIs, it does not.
**Jason Plumb** 08:58 You gotta be kidding me. Really?
**Surbhi A** 09:00 Yeah.
**Hanson Ho** 09:01 I think it's the current context, maybe?
**Surbhi A** 09:08 Like, if you go to my original issue from my PR, I have linked… oh, yeah, you already came here, right?
**Jason Plumb** 09:17 But yeah, I was gonna try and just look at the… at the actual…
**Surbhi A** 09:21 Yeah, see, it doesn't have anything to add.
**Hanson Ho** 09:24 There's set contexts.
**Jason Plumb** 09:25 Yeah, it's this. It's… yeah.
**Hanson Ho** 09:27 It's… it's that stupid context is not span context, you have to make sure this context contains a span context.
**Jason Plumb** 09:33 It's true.
**Cesar Munoz** 09:34 And it's not Andre.
**Surbhi A** 09:37 Oh, the documentation says we should have trace ID and span ID fields, so I… if I give it the entire context, I'll have the trace ID and span ID fields on.
**Jason Plumb** 09:47 You will…
**Surbhi A** 09:48 part.
**Jason Plumb** 09:48 if the.
**Hanson Ho** 09:49 If the context contains the right…
span context, and all that fun stuff, so… Which it will, right? We're in the middle of an HTTP span, so it should… if you get the current context, it should have trace and span ID.
**Cesar Munoz** 10:03 It's obvious.
**Jason Plumb** 10:04 Same thread. Oh, yeah.
**Cesar Munoz** 10:06 No, because, okay, HTTP changes the thread for these callbacks, doesn't it?
**Surbhi A** 10:11 No, I hooked the span context via the tracing interceptor to this network callback listener, so it would have the correct context to be added.
**Hanson Ho** 10:20 Okay.
**Surbhi A** 10:21 That was the only way to ensure having correct context on this log record, right?
**Jason Plumb** 10:26 Yeah, it's in here. So, yeah, you have it, you're getting it.
**Cesar Munoz** 10:30 Got it.
**Surbhi A** 10:31 Yeah, I store a map of call to context.
And that is fed from the tracing interceptor where the span is created.
**Hanson Ho** 10:43 But do you have the original context?
**Surbhi A** 10:46 Yeah, like here, on line 53 to 56,
We inject the, actual span context, which is created on line 50.
**Hanson Ho** 10:58 So, yeah, so you probably don't need to fish out the specific span and trace IDs, and just slap the whole context in there, and it should show up.
**Surbhi A** 11:07 Yeah, using… I earlier used span.context.current to fetch it, but that was wrong, right? That had a lot of loopholes.
**Hanson Ho** 11:16 Yeah, current context is…
**Jason Plumb** 11:17 Threading, yeah, with the threading challenges, yeah.
**Cesar Munoz** 11:20 And sorry to insist, just to make sure, survey, do you know if this works? Because there's two ways you can
execute an HTTP request.
When it's, you know, async and sync.
**Surbhi A** 11:33 Yeah.
**Cesar Munoz** 11:33 So, in both cases, you get the right context in the interceptor.
**Surbhi A** 11:37 Yo.
Yes.
**Cesar Munoz** 11:39 Okay, awesome. Yeah, I just wanted to make sure.
**Surbhi A** 11:41 I added… I added test cases as well for both the scenarios.
**Cesar Munoz** 11:46 Thank you.
**Surbhi A** 11:47 Because we propagate context correctly in the async scenario, I'm able to get it correctly.
**Cesar Munoz** 11:54 Nice.
**Surbhi A** 11:56 So right now, I used the trace ID and span ID attributes, so I'll correct that to use this setContext API instead.
**Jason Plumb** 12:04 Yeah. Another thing was…
**Surbhi A** 12:06 Like, setting the top-level event name field makes it an event, but this is really not an event in time, but it's a log record containing all the network timing attributes.
So, instead, I used event.name equals to okhttp3.network.timing on line 143. So, if you guys have any suggestion how we can instead use maybe log body to explain that this is the…
This is what log record holds, or I used event name right now. Is there any other suggestion for this?
**Hanson Ho** 12:44 I…
**Jason Plumb** 12:44 Yes. Event names should not even exist anymore.
**Hanson Ho** 12:48 Yeah.
**Jason Plumb** 12:50 So, it's probably been a while for you, Servi, but… so we… we are not setting the event name in an attribute anymore. There is a first class…
There's a first-class element on log record.
It's called Event Name.
Yeah, but that makes it an event.
**Surbhi A** 13:09 So, yeah, that's…
Which is what you're omitting, right? If you're trying to set the event name, then it is an event, right?
**Jason Plumb** 13:16 Oh, you have a comment here, sorry.
Yeah. Because… Yeah, oh…
**Surbhi A** 13:24 Like, the description on that field says if you, set this, it means it's an event in time, but this is a log record, so I want to…
**Jason Plumb** 13:34 Oh, yeah, that distinction is subtle. Why not just make it an event?
**Surbhi A** 13:39 Yeah, that also is okay.
**Jason Plumb** 13:43 I mean, I think that's fine to make it an event.
**Surbhi A** 13:46 Okay.
**Cesar Munoz** 13:48 It works for me as well.
I just… sorry, Serby, I've been out of the loop for this one.
So, I might have some dumb questions, but…
Just to make sure, I'll try to understand it better, to see if I can provide better feedback.
In the future. Essentially, this is a work to add more… to add some sort of metrics to HTTP requests, in a way, but in a way that they're linked
to the trace via its context, which is something that is not possible with metrics right now, so… It's.
**Surbhi A** 14:30 Nothing like that.
**Cesar Munoz** 14:32 Okay.
**Surbhi A** 14:32 Exactly, yes. I do have, like, an issue that I opened in the semantic convention repo that is also linked in the PR.
This PR itself… Yeah, I, mentioned this there, so below, if we go below.
like, I mentioned this in the issue recently, so if you go down, A lot more down.
**Jason Plumb** 14:59 Okay.
**Surbhi A** 15:00 Yeah, here I added this, right?
**Jason Plumb** 15:03 This one.
**Surbhi A** 15:04 The, yes, in the synth, yeah.
No, not this one, the one above this.
**Jason Plumb** 15:10 Sorry.
Still waking up.
**Hanson Ho** 15:13 Thank you.
**Surbhi A** 15:14 No, thank you so much.
**Jason Plumb** 15:16 Okay.
**Surbhi A** 15:17 For helping me out, yeah.
**Jason Plumb** 15:19 Oh, yeah.
**Surbhi A** 15:21 So, like, I have explained… like, the discussion happened there about what it was for, and, like, I have, also updated the new approach here.
So, basically, some of the challenges were, right, we needed per rec… we wanted to show some things at per-request level as well. So, like, the download time, the upload time.
So, also, we needed the metrics to be
possi- it would… it should be possible to filter the metric charts with the HTTP span attributes, right? They become important. Like, if we were to,
draw a histogram for connection times, we should be able to break that via server.port.
server.address, network details, right? So that's why, yeah, we needed correlation between these metrics and the original HTTP span attributes, so that's happening via the context.
**Cesar Munoz** 16:28 Got it.
**Hanson Ho** 16:29 So, are you.
**Cesar Munoz** 16:29 Thanks, I'll have a look.
**Hanson Ho** 16:31 Are you duplicating, information, on the actual, log? So you have these timestamps for these various events. Are you expecting, folks on the server to calculate based on these timestamps, or are you basically putting a duration in there between DNS start and be at DNS end?
**Surbhi A** 16:52 Yeah, yeah, so we are putting timestamps, because using different timestamps, you can gather different durations, so we want to leave it flexible for the backends, that they have all the timestamps, and now whatever they want to calculate, they can calculate, right?
Using of curations from that list.
Right now, I have not implemented the copying of the original span attributes, but I have suggested that as upcoming work in the description, but I will soon implement it, it is also straightforward.
**Hanson Ho** 17:26 Yeah, I think keeping track of this as timestamps makes sense, and the question becomes then, you know,
what's the difference between this and a span? .
**Cesar Munoz** 17:37 Yeah, and I was gonna… yeah, sorry, probably this has been brought up a lot of times before, but it's just that at first glance, it sounds a bit confusing.
Because it seems like we're conflating different types of signals.
Within, signals that are not meant to be used for that kind of…
data, and I know that there are some
limitations to what, OpenTechM3 can do right now. For example, it cannot, like, link metrics to a span context.
As far as I'm aware, so…
So I understand the… but yeah, it's just that it's a lot, and it feels like it's doing…
Things in a way that… are not…
being done in the signal that it should be done. I don't know, it kind of… at first glance, it sounds… it seems a bit… a bit strange, but I understand if there are limitations that…
You know, push us to go this way.
**Hanson Ho** 18:42 I actually quite like this. It kind of just shows, like, some of the underbellies of, like, the primitives that we have, because, you know, I think it makes sense for this to be tracked as one thing, rather than, like, a host of different events.
But then, if you have one event, then you have a log record, and that's point in time, but there's a duration.
So, oh, it's a duration, you should put it in a span, and then how do you have these separate timestamps? Oh, then you have span events. Oh, wait, wait, you don't have span events anymore.
**Jason Plumb** 19:12 Span has a start and end, come on.
**Hanson Ho** 19:14 I know, I know. It does, but you could also have an attribute here that says, basically, you know, end.
as, as, as, as you could. So, you have… you basically have all the information here, that you would have, you know, for the span version of this. And, you know.
I think the difference is that tooling will ingest this a little bit differently, but this has all the data that is necessary to process.
So,
I think initially, I was like, well, why don't you make a different span, just with different attributes, with different life cycle. But then I look at this as like, oh, we can't use span events, at least
you're not supposed to, then how do you represent all these points in time? And this seems like the most reasonable.
**Jason Plumb** 20:03 Am I correct that basically all of these are in pairs, right? There's a start and an end to basically all of these?
Because we're looking at durations. So why not make each of these a child span of the HTTP span?
Like, instead of it being an attribute name, that could be a span name.
And then it has a start time and an end time, and you have.
**Hanson Ho** 20:25 It's a lot of data… it's a lot of data, like, one network request. It would just be HTTP connect…
**Jason Plumb** 20:31 duration, or something, I don't know what you'd call it, we don't have SEMCOMF yet for that. It would be, what is it, like, I don't know, I haven't counted these, but it's like 10 spans, or 8 spans?
**Surbhi A** 20:42 But the thing is, like, span is justified if, like, you have a duration, and then for that duration, you have certain other attributes, right? We just have a duration.
**Jason Plumb** 20:52 Attributes are optional. I mean, spans don't have to have attributes. They can just be a name and a start-end time.
Which is kind of what these are.
**Hanson Ho** 21:02 So, so these could… so these could definitely be, you know, a trace with a bunch of child spans, but the number of… the payload is going to be gigantic because of the span IDs that get generated that don't compress well, and…
everything that kind of comes with, you know, the overhead of a span. So, basically, you're 10x-ing the amount of data usage and overhead of a network request.
**Jason Plumb** 21:29 That's a legit concern, and I don't… I think… I think it's overstating it, but yes, it's definitely going to be more data.
**Cesar Munoz** 21:36 But are the spans, in terms of payload, Are these fans… Children's pants are they sent?
like, within their parent pens, because I thought it was, like, they were sent, like, independently, it's just that the trace ID will connect them later.
In the server.
**Jason Plumb** 21:53 No, there's a parent span ID on Span.
**Cesar Munoz** 21:57 So… So the payload should be the same. In fact, if we turn those logs into spans.
We will reduce the data that's sent from the client by half.
In a way.
**Jason Plumb** 22:11 I'm not following, because you're saying it's gonna reduce it, Hanson's saying it's gonna blow it up.
**Cesar Munoz** 22:16 Because we're… the way it is, we're gonna send two logs per event, like, you know, a log for the start.
**Jason Plumb** 22:23 I think it's just one… right now, the way it's written, I think it's just one.
**Cesar Munoz** 22:28 Oh, and the… okay, the rest are the attributes, I see.
**Hanson Ho** 22:34 the way it is… it basically is the minimum amount of data that would represent all the timestamps that would go back to the server. And it also… the advantage of using this method is that.
**Surbhi A** 22:47 Everyone.
**Hanson Ho** 22:47 everything comes in one object. And if it's a bunch of child spans, depending on how, you know, the network likes to play, you might be missing certain things. Or, you know, have to wait, you know, for all the data to come back. So that's a benefit of basically having, like, a thing represented.
But, you know, in the most, kind of, strictest hotel-ness of it, this ought to be a trace with a bunch of child spans. But, you know.
for… for… for… for mobile and for front-end, there… there becomes a… a practical, set of circumstances that make it, less ideal. So, I think… I think this is… this is a very good,
example of how we break down information that is, you know, part of a single operation in a way that is good for mobile and good for hotel, and I think you have these two choices right now.
**Cesar Munoz** 23:48 Yeah, that's true.
**Surbhi A** 23:50 A lot of signals will… a lot of signals will also then, again, cause problem for the backends, right? They have to relate so many spans to gather the metrics, and then tie them all together for getting all the data that they need, right? That's also a challenge for backends right now.
**Hanson Ho** 24:08 Yeah.
**Jason Plumb** 24:11 Is there any prior art, for these? Like, are there any other instrumentations in OpenTelemetry that gather this network data?
Do we know?
**Hanson Ho** 24:19 I remember looking at a semantic convention for .NET, sorry?
**Surbhi A** 24:27 There is a net… there is a neti instrumentation as well.
**Hanson Ho** 24:31 Yeah, so I don't know about the Netty one, but the .NET one definitely, uses, a trace and child spans. There are fewer, kind of, chunks, but I think there's potentially 4 or 5.
And it's based on the domino?
**Surbhi A** 24:49 But that…
**Hanson Ho** 24:49 life cycle.
**Surbhi A** 24:51 I looked at that, the purpose for that is a bit different, right? The purpose there is, like.
they are capturing the entire TLS phase, so they are capturing all the attributes also that they get, yeah, and the DNS phase they are capturing. Like, their purpose is not for metrics per se, but to capture in detail troubleshooting for those phases, right?
**Hanson Ho** 25:13 Yeah, they want to find out why a particular request is slow, so they're able to do that. Yeah, but…
**Jason Plumb** 25:23 It's not… it's not terribly different from this approach, though, like, knowing how long each of these phases takes…
**Hanson Ho** 25:29 Yeah.
**Jason Plumb** 25:30 You know?
**Hanson Ho** 25:31 it, I mean…
a wide event in a span is, like, 95% the same, except for some couple of structural things. Do we know where in the NetE instrumentation this stuff is?
**Surbhi A** 25:46 I should have a link, let me look through my notes quickly.
**Jason Plumb** 25:50 Okay.
It would be good just to make sure… I'm curious how they're modeling it, first of all, and then I'm curious, if any of the names match up.
**Surbhi A** 26:01 I'm also curious about the modeling.
**Cesar Munoz** 26:03 It's…
Like, I understand the limitations that we have to deal with, but it's just that at some point, I guess we have to draw the line.
somewhere, right? Because it's like, otherwise we can say that everything can be a log, right?
**Hanson Ho** 26:19 Yeah!
**Cesar Munoz** 26:20 Everything can be unlocked, so why bother, you know, with spans and…
**Hanson Ho** 26:24 Yeah!
Yeah, well.
It's different. Metrics has the client-side aggregation bit, but the difference between a hotel login and hotel span is really span links. I mean, there's a bunch of other things, but like, you know.
You can't link logs, you could link spans, and there's the parent-chat relationship, but…
Other than, like, how you relate one to the other, it's…
It's… especially now we have complex attributes, or theoretically, even the body isn't necessarily a distinguishing thing.
I guess there's no event name in Span, but… That's not hard to fix.
**Jason Plumb** 27:11 Yeah, I was trying… so, I matched in the metadata. It looks like they have a flag to turn it on. That touches on my question, which, is it opt-in?
Sorry to switch topics a little bit, but I think, you know, it'd be nice if this were not on by default, and I didn't see that in here.
**Surbhi A** 27:28 So this is manual instrumentation, right? So, there is an API, new call factory. So, I have introduced a newer API, new call factory, with network timing.
And…
**Jason Plumb** 27:41 Where is that?
**Surbhi A** 27:42 that.
It's in OKHTTP telemetry.
**Jason Plumb** 27:46 Okay… Okay.
**Surbhi A** 27:51 So, here only, the Boolean for copying the attributes will go, and right now, if you call this API, you add the network listener.
**Jason Plumb** 28:01 Got it. Okay, so this is, this is opt-in. You get to pick, because you're picking, which one, so we don't have a way to do this with auto instrumentation yet.
**Surbhi A** 28:10 Yeah, with auto-instrumentation, my plan was, in the, configuration that we take, we will take that configuration, Boolean, whether they want network timing, log record as well.
And based on that, the trace… in the… in the bytecode where we change things, we will change the tracing interceptor to be the one that stores the context as well. Like, we can… we'll take a configurable Boolean to be able to…
do this. We can do this via that, and also another configuration for whether they wanted to copy the original HTTP span attributes or not.
**Jason Plumb** 28:47 Okay, and we're gonna do that in a separate PR, though, right?
**Surbhi A** 28:51 Yeah, in the… I'll propose that change so we can look at it and see if that fits our needs, and I will then go ahead and make the change.
**Jason Plumb** 29:02 Okay. And do you mind creating an issue to track that?
**Surbhi A** 29:06 I do have an issue. Perfect.
**Jason Plumb** 29:08 Where is it?
**Surbhi A** 29:10 We did, I did create 3 issues earlier in the semantic repo, Java instrumentation repo, and Android repo, so we did discuss it in brief, where we discussed where… that we don't need to do it for HTTP URL connection instrumentation right now, but we can start with OKHTTP3.
So, I think network timing, something of that sort, if we search.
**Hanson Ho** 29:34 So, here's a… here's a question. Unless you…
**Surbhi A** 29:40 This one.
**Jason Plumb** 29:41 I just mean, yeah, but this doesn't talk about auto-instrumentation, right?
Or does it?
**Surbhi A** 29:46 Oh.
**Jason Plumb** 29:48 I was talking about an issue strictly to circle back, after we're done with this PR, to circle back and make sure that it's working and that there's configuration that supports the auto-instrumentation.
**Surbhi A** 29:59 Yes, yeah. I think that issue meant… was meant for that, but I'll update it. Okay.
**Jason Plumb** 30:05 Okay.
**Surbhi A** 30:06 Yeah, yeah.
**Hanson Ho** 30:07 It might be cleaner just to create a new one if it's already in there.
**Jason Plumb** 30:12 Yep.
**Surbhi A** 30:12 Yes, yeah.
**Hanson Ho** 30:15 Okay.
**Jason Plumb** 30:15 So, yeah, Hanson.
**Hanson Ho** 30:16 So here's a… here's a question. So if you don't already have, like, set up, to… to use the existing network spans.
Based on the data that comes from this log.
Do you… and you don't need to relate the network span with any other data,
Do you need anything more than just this log?
to derive, Metrics and stuff like that.
**Surbhi A** 30:48 We always need the original HTTP span attributes, otherwise you don't… the metrics don't make much sense, right? You need to be able to filter them with various attributes.
And also, like, per request level mapping you need. So, like, in Splunk backend, from each… From the metric charts, you can go to the individual requests where that data is coming from, right? So, and in the…
per… in the request itself, you can show some data, right? What was the download time, upload time, some metrics you can show there as well to show that this request is problematic, right?
**Hanson Ho** 31:32 So, so there is some data in the, in the, in, in the, in the, span itself that, that, that is not in the, in this log.
**Surbhi A** 31:41 Yes, the original span attributes that need… that are needed.
**Hanson Ho** 31:48 Right, but after you copy everything, Okay, cool.
**Surbhi A** 31:52 we don't need. Sorry, I didn't understand your question, maybe.
**Hanson Ho** 31:55 Right, I think right now this was meant to be, like, an addendum to, like, enhance the existing network spans, but I think we're getting to a point where this almost becomes a superset, like, other than the fact that this is not a span, but in terms of, like, the timing information.
everything is in here. And the thing that's missing is…
how this is related to the other telemetry that's out there. So.
**Jason Plumb** 32:24 Yeah, and that copying the attributes I don't love, because it does, at the end of the day, duplicate some data, right? And if you have this log with all the timing information on it, and you have a span ID, because you have the context, you should be able to go look up, in an ideal world.
any of those attributes, but I get that, like, the correlation then is tricky. Logs and spans are set through… sent potentially through different channels and different pipelines, and so, you know, correlating those is potentially way heavier if you don't have immediate access to those same attributes, like route or whatever method, you know.
**Surbhi A** 33:00 Yeah, also this… we should think of it as an interim thing to help backends until they are ready to correlate different signals. Ideally, it shouldn't have, because it's a different signal, right, that should add to the span,
**Jason Plumb** 33:16 Right.
**Surbhi A** 33:16 So… Timing attributes, that's all. But, right, it's an interim thing to help
And also, you don't… like, if you have that set up already, you can set that Boolean to false, and you won't get redundant data.
**Jason Plumb** 33:31 So putting it behind an experimental flag, I think, would be helpful.
**Surbhi A** 33:36 Okay. Like…
**Jason Plumb** 33:37 That copying, you know, it's opt-in, you gotta opt into it, but then you have to do an additional step if you want all of the heavy attributes to be copied over.
**Surbhi A** 33:47 That makes sense, yeah.
**Jason Plumb** 33:49 Yeah. Cool.
**Surbhi A** 33:54 Earlier, Jason, you were looking into OpenTelemetry Java instrumentation repo issues. So the issue is there in the OpenTelemetry Android repo for Android.
**Jason Plumb** 34:05 Oh, it is, okay.
**Surbhi A** 34:06 Yo.
**Jason Plumb** 34:07 What number is it? Do you have it?
**Surbhi A** 34:09 Let's… network, maybe?
Let me look at it.
Maybe we can search for network here?
Yeah, the… Fourth one.
**Jason Plumb** 34:23 This one…
**Surbhi A** 34:24 Y'all.
**Jason Plumb** 34:26 Okay.
**Surbhi A** 34:29 So it's for automatic instrumentations. We propose… I proposed this.
**Jason Plumb** 34:36 Okay, it's a little bit buried, but okay, that's great, okay.
We have.
**Surbhi A** 34:40 Yo.
**Jason Plumb** 34:41 Cool. Yeah.
**Surbhi A** 34:43 I'll, create a proposal, maybe in a new issue, and tag this issue.
**Jason Plumb** 34:48 Okay.
Cool. Well, we've spent half an hour on this, I think we should move on to the next topic. Are we good?
**Surbhi A** 34:57 Yeah, thank you so much. I'm, if you guys have some time, look at it and give your, reviews and suggestions.
**Jason Plumb** 35:05 Great. Thanks, Teremy.
**Surbhi A** 35:07 Thank you.
**Cesar Munoz** 35:07 I'll have a look.
**Surbhi A** 35:08 Thank you.
**Jason Plumb** 35:09 Alright, this topic, Cesar, I have some questions about this, but let's… let's get into it.
**Cesar Munoz** 35:15 Yeah, just for the context. So, well, it's explained in the issue, but essentially,
So, we have an API, Where we based all of our instrumentations from.
And… It's currently… let's say it's not providing…
All the stuff that's needed by all of the instrumentations that are… that extend from it right now.
So, we're kind of doing a workaround.
In some of those instrumentations to make them work.
And I think we shouldn't have to do workarounds.
**Jason Plumb** 35:53 What's the exam… what's an example of that?
**Cesar Munoz** 35:57 If you go to the issue…
**Jason Plumb** 36:00 The one that I added there, it's one.
Oh yeah, this, cast.
**Cesar Munoz** 36:06 So… I'm not sure what's the correct way to address these kind of issues.
But I propose two options.
Probably neither is the correct one. I'm just gonna say that.
you know, up front. But, you know, those are two ideas, okay? And… and if you can have a look… I mean, I know you've already haven't taken… have taken a look, Jason, and…
**Jason Plumb** 36:32 Yeah.
**Cesar Munoz** 36:33 Jamie as well?
Thanks for that. I responded to the comments, but essentially, I think the more people, you know.
say it, the better. You know, all ideas are welcome. Essentially, I just would like
To find a way that we wouldn't have to do any casts and any, you know, stuff to make instrumentations work.
**Jason Plumb** 36:56 Yeah, so we… in the installation, we are given this installation context, that's sort of… that is the basic API for instrumentation right now. That's…
you have to implement this method install, and we will give you a context, and then you do… you can build as many instrumentations as you want, as long as you conform to this very simple API. And in this case of the crash reporter.
He has a collaborator called Crash Reporter, and it takes an instance of some extractors, and then when it's installed, and this is not instrumentation, right? This is a different API. But what it takes on its install is an instance of the OpenTelemetry SDK, presumably, right?
**Cesar Munoz** 37:37 Yes.
**Jason Plumb** 37:38 Alright, so that crash reporter, can we go to that?
Crash Reporter…
And right, so it has an install method. This is just named the same, just for funsies. And it needs the SDK,
Because when it processes a crash, it needs to get what? It needs to probably get, like, a log builder or something, right?
**Cesar Munoz** 38:05 It's to force flush the logs, that's why it needs the SDK.
**Jason Plumb** 38:09 Oh.
**Cesar Munoz** 38:13 Town lines…
**Jason Plumb** 38:14 Well, it's getting a logger builder also, right? Like, it needs this, and then where's the other flush happening? Down here.
**Cesar Munoz** 38:21 The… there's a replacement for the… the SDK logger provider.
So that that's covered by the API. But there is no alternative for the forced flush.
Method.
**Jason Plumb** 38:36 Right, but as it stands today, the implementation of Crash Reporter, like, this is kind of the wrong dependency, right? It doesn't necessarily need…
the SDK. What it needs is, is a logger builder, or a logger provider, rather.
Alright, logger.
**Cesar Munoz** 38:54 later.
**Jason Plumb** 38:54 and logger provider.
**Cesar Munoz** 38:56 ease.
Yes I mean, technically, it also doesn't need to force flush.
It's just that I get it's important, like, in this use case, where, you know, we don't know if it's gonna make it.
**Jason Plumb** 39:09 Right, so I'm just kind of… what I'm trying to do by this, I'm just…
kind of speaking out loud here, but I'm trying to back into a solution by describing the current behavior. So, the current behavior is that we've declared a pretty big hammer here. You're like, pass me the entire SDK, and I'll use what I need, when we really should have implemented this with a much smaller
dependency. All this really needs is the logger provider.
And I think there's an API for Logger Provider. It doesn't even… it probably doesn't even have to be SDK logger provider. But either way…
**Cesar Munoz** 39:42 mentioning earlier, you don't need to use SDK login provider to send logs.
**Jason Plumb** 39:46 logger provider.
**Cesar Munoz** 39:48 Yeah, it's a… they call it logger bridge, I think, in the API.
**Jason Plumb** 39:52 Yeah, okay.
Yeah, there's a lot of history in that. Okay, so if this were then modified, then going back to where the install was happening…
Can we get a logger provider from the context, right? In our installation here, can we say crash reporter install and just pass it the logger provider?
And… The OpenTele… this is OpenTelemetry Rum, is that right?
**Cesar Munoz** 40:18 No, that's… that's Open Sedimentary… upstream API.
**Jason Plumb** 40:23 Oh, oh, and that has a logger provider that you can call git logger provider on that, right?
**Cesar Munoz** 40:29 Yeah, you can just pass the logger provided here.
**Jason Plumb** 40:31 So if we called context OpenTelemetry get logger provider.
Then we wouldn't have to do this cast.
**Cesar Munoz** 40:39 Well, yes, correct, but then you wouldn't have… you wouldn't be able to force flush logs either.
**Jason Plumb** 40:45 Because Force Flush is on some other API.
**Cesar Munoz** 40:48 It's on the SDK, it's not.
**Jason Plumb** 40:49 It is on the SDK.
Okay.
Well then, yeah.
**Cesar Munoz** 40:55 recommended two options.
**Jason Plumb** 40:56 Well… Yeah, so…
**Cesar Munoz** 40:57 Yeah.
**Jason Plumb** 40:58 Look at those options, yes, thank you. Okay, option one, let's talk through it.
**Cesar Munoz** 41:02 Well, both options Past the, openTelemetry wrong.
instance, instead of… the Open Telemetry API.
**Jason Plumb** 41:14 Yeah.
**Cesar Munoz** 41:15 So, the difference between the two options is that, for the first one, Whatever,
functionality we need, it's added right into the OpenTelementary ROM.
API. So, in this case, OpenTelemetry ROM API will have a force flush.
Logs, or something like that.
**Jason Plumb** 41:37 Yep.
**Cesar Munoz** 41:38 Yeah.
The other option doesn't add this to OpenTelemetry ROM, but instead creates a separate file within the API module.
That's called Log Record Flusher.
which an implementation of OpenTelemetry RAM can, you know.
Use, and if it's… and if it… if it's implemented by that implementation.
Then, in the, crash reporter, we will check if that…
capabilities there for that OpenTelemetry ROM instance. Yeah.
So… That's kind of like…
**Jason Plumb** 42:24 I don't love it.
**Cesar Munoz** 42:26 The gist of it.
**Jason Plumb** 42:27 Yeah.
**Jamie Lynch** 42:31 So…
I left a comment on one of the PRs saying this, but it feels like this should be a responsibility of the SDK'd to shut itself down gracefully, and not be instrumentation.
Because you could even have this, like, you could have this instrumentation disabled as a user of the library, and then…
If a log is in flight, and a crash happens, but it gets lost.
**Jason Plumb** 42:59 Yeah.
Yeah, this, this, this feels like such a very specific, weird…
API that is now spreading its tendrils into all of these instrumentations, when it kind of should just be…
an artifact of using the SDK.
The flushing. Do we know the history and, like, why we built that?
That flushing?
**Cesar Munoz** 43:23 Wind flashing?
**Jason Plumb** 43:25 Yeah.
**Hanson Ho** 43:26 I mean, the app is supposedly in the middle of crashing, so the idea is that any telemetry that's kind of, you know, get it out. But, like Jamie said, this would be true for not just the crash that's being logged, it's basically, oh shit, the thing is dying, the entire SDK needs to kind of…
you know, push that forward. So, I think this is… this… in this specific instance, the functionality ought to be provided, by the SDK, so, you know, when we are… the SDK is dying.
Everything that is, you know, in… that's cash ought to be flushed.
So the whole manual flush should not need to be happening at the instrumentation level. Then the problem then becomes the API that needs to be passed down. And I think without the need to do a manual flush,
you already are able to get a logger provider, from there. So that should resolve itself simply by, you know, changing the parameter to either OpenTelemetry itself or, like, a log… logger provider.
So, in this specific case, I think it could be solved simply by, you know, splitting the responsibility.
**Cesar Munoz** 44:40 Yeah, I think that's one of the stuff that Jamie and I discussed on the first option, VR.
You know, having the shutdown handle all this stuff.
I do have a couple… I mean, that's an option, that's fine. I just have a couple of questions on, you know, how we make sure that, you know, shutdown is called.
You know, outside of these, you know, threat, on-card exception handler.
You know, if it gets a chance to get to that, and if it, you know, if we maybe wish flush logs first, just to make sure that, you know, crash events
are saved first, or things like that, but then we'll have to make sure… I mean.
We will introduce, like, More space between the flushing of the events.
And, by the time the crash happens, so I'm not sure if that more time in between will…
increase the probabilities of that event to get lost, right? So, that could be another thing.
Maybe it's not that bad, because it's not like I have any specific numbers.
But I guess we shall…
take a, you know, take that into account, considering that the reason why I believe we're forcing flush
logs right now.
It's because we don't have much time after the crash happened to get… to save this data, so…
you know, I just would like to have that in mind.
**Hanson Ho** 46:12 What's the…
**Jason Plumb** 46:13 Eric.
Go ahead.
**Hanson Ho** 46:15 Oh, what's the mechanism for the SDK to detect that there is a JVM crash coming, and basically, do cleanup?
**Jamie Lynch** 46:24 I've got exception handler.
**Hanson Ho** 46:26 Yeah, so it's the exception handler. Yeah.
**Jamie Lynch** 46:29 Anyways, yeah.
**Hanson Ho** 46:31 So, if the crash handler
lives within that ecosystem. I mean, either there's already a race condition between the two, or it's already handled.
So,
figuring out where to do it, like, to, to, you know, as long as I believe, as long as, your, your, crash handler, is, is active and synchronously handling stuff.
it's not gonna crash unless something dramatic happens. And so, as long as your crash reporter is doing a thing and inserting it into the correct thing, and then, there's no race condition, then your, your, the main SDK
Should handle this already.
In theory, that's, you know… otherwise, there's a bigger problem, if you need to do the manual flush in the instrumentation.
**Cesar Munoz** 47:31 Yeah, I think for that to happen, we will have to make the SDK, well, the… yeah, the ROM…
object to react to the crash as well, right? And to call some sort of shutdown
Internally, when that happens.
Because right now, I don't think that's the case.
we have a shutdown hook.
in our… in our ROM builder, but I think that's to… for other things to attach to the shutdown.
of our ROM instance, but it's not like the ROM instance itself calls that when the app exits.
As far as I'm aware.
**Jason Plumb** 48:14 So I want to take just a small step back and remind everyone that, like, these two options are really with the intent of
figuring out how we can solidify our instrumentation API and mark it stable in a way that is extensible, but that we won't have to make breaking changes, right? And so currently.
I had it open, and I might have closed it, but the, the API is, like, pretty lightweight, right? It's pretty small, it's just that install with context.
And hopefully we all agree that, like, it is rare that
an instrumentation will ever need the SDK directly. Like, having the…
**Cesar Munoz** 48:55 We're doing a lot.
**Jason Plumb** 48:56 every RUM instance should be enough for most instrumentations, in that this specific case is kind of an exception, and allowing one instrumentation to do a cast is, like, not the worst thing in the world.
**Cesar Munoz** 49:08 Definitely. I don't think any instrumentation ever should have to use the SDK.
All the inventory SDK. Only the API, so…
Yeah, that's why this… like, and this is one example.
This is the most,
Critical example, if you will. But there are a couple of others that…
Are not as, as,
clear that I've kind of touched on them in the issue.
Where we might need stuff like, you know, the clock.
that was used, you know, when building the OpenTelemetry instance, or the session provider.
It's used up by a couple of other instrumentations.
The approach that we are going with right now, with all of those, you know.
tools that some instrumentations might need is that we are extending the…
Instrumentation context. Instrumenter Context, I think that's the name.
To add those new parameters.
**Jason Plumb** 50:11 Right, right.
**Cesar Munoz** 50:12 Which, that's… that's good, that's an approach, it's just that some of those parameters
To me, they… it kind of makes sense for them to be part of the ROM.
Abstraction, because they kind of… They're kind of related, so…
**Jason Plumb** 50:28 Yeah, which is what you did.
**Cesar Munoz** 50:29 I think in this.
**Jason Plumb** 50:29 one, yeah, yeah.
**Cesar Munoz** 50:30 Yeah, that's… that's another, like, proposal.
But I'm also, you know, not married to it, but I still wanted to show it.
**Hanson Ho** 50:42 So, we can always add things after we declare stability, right? It's just that we can't take away. So, as long as what we have currently, we're all comfortable with exposing, that could be effectively 1.0. And then, whether or not we add this as 1.1,
We could do that without having to, like, change major versions, so…
**Jason Plumb** 51:05 This feels aggressive to me, though. Like, to put these two all the way up on OpenTelemetry, which is the API that most users are interacting with.
So to bubble these all the way up to account for, kind of, like, one or two weird instrumentation, like, in this case, one instrumentation.
Feels a little…
**Cesar Munoz** 51:25 I said that it's…
Yeah, but in a way, the way… well, the reason why I added it here, because it doesn't have to be a valid reason, but the reason why… the thing I was thinking about was…
You know, these are the stuff that we initialize.
when building the OpenTelemetry instance that are not accessible.
from the OpenTelementary instance, you know, from the.
**Jason Plumb** 51:45 That's true.
**Cesar Munoz** 51:46 SDK.
But still, you know, They might be needed.
for different use cases, and it's something that we have an opinion on, so I was kind of like, well, if we created them and we have these opinions.
Probably we should provide it for people who might need it.
We don't have to leave it here.
One thing that I see of keeping the existing approach of extending the installation context, object.
is that, as Hanson mentioned, we can… we can keep on adding stuff.
And it's fine, it's just that…
installation context, it's not a… it's not an abstraction, so if we add stuff to it, then… well, it's not that bad either. I guess we can just add default values to the constructor, because if we keep on adding stuff in the future, then we'll have to make sure that people can still construct it.
You know, using the same existing parameters that it receives right now.
**Jason Plumb** 52:46 Yeah.
Okay, we've got a few minutes left, I think this is a very good discussion.
Yeah, I mean, clock. I don't know why a user of this would ever want to mess with the clock, or to get the clock, but, you know, we can think about it.
**Hanson Ho** 53:03 What's… what's, well, I mean, I think the clock is useful if you… so, OKHCP uses a different way of obtaining a timestamp that's not, like, the clock open telemetry, and there could be, like, some out-of-sickness.
So it could be useful to basically provide the clock that the OpenTelemetry instance is using. But whether or not it lives in OpenTelemetry ROM or some other object or installation context, that's, I think, you know.
we can debate further, and, you know, frankly, each one of these ones we could probably talk about separately, but… Totally.
not part of the stability, conversation, I think it's an aside.
**Cesar Munoz** 53:37 Yeah. Also, bear in mind, the two stuff that I added there is just because it's already used in some instrumentation, so…
**Jason Plumb** 53:43 Yeah, yeah, I get it.
**Cesar Munoz** 53:45 Yeah. So, yeah, that's it. Please, you know, have a look in your spare time.
Happy to discuss.
And yeah.
**Jason Plumb** 53:53 Cool. I want to make sure that we have a couple of minutes to ask David if he's got anything. I know, maybe first time here, we jumped right into details. We've been going full strength for 53 minutes, so if you have anything that you want to bring to the group, whether it's
your experience with OpenTelemetry Android, or a question you have, anything like that, I just want to give, like, a little bit of room for that.
**DavidGrath** 54:17 Peter, thank you.
I don't really have much to see examples.
**Jason Plumb** 54:22 Sorry, your audio is really muffled, I'm having a hard time hearing you.
**DavidGrath** 54:27 Okay, I'm communicating.
**Jason Plumb** 54:32 Still pretty muffled.
**Hanson Ho** 54:37 No, I can't hear.
**DavidGrath** 54:39 Perfect, can I hang out?
**Jason Plumb** 54:42 It's really muffled.
**Cesar Munoz** 54:42 Bitter?
Has it improved a bit?
**Hanson Ho** 54:45 Slightly better.
**DavidGrath** 54:47 Okay. So I said that I… I don't really have any particular suggestions or things to discuss. My experience so far has only been with pet projects, should I say. So just me actually trying to find out how to integrate it into
my own projects and see how it's, and see how it works. I actually also did that…
SDK… approached in myself, coincidentally. So as I see it's been discussed here, and the future of it.
And yeah, that's pretty much it's…
**Jason Plumb** 55:21 Cool.
Well, that's great. I'm glad you found our project and are at least tinkering with it, so that's awesome. In the last couple of minutes, I want to bring attention to two PRs. One is about TLS stuff.
And maybe it already got merged?
**Cesar Munoz** 55:44 It's, the fourth one?
**Jason Plumb** 55:46 This one, yeah, okay.
So please take a look at this one if you haven't. I think this person hadn't contributed before, and they just jumped on an existing issue without really mentioning it, so it's this issue.
And, yeah, I think it'll be…
Alright, well, maybe, maybe I, maybe I'm confusing two different things. That's probably on me, then. Anyway, please do…
**Cesar Munoz** 56:12 Aren't those two the same thing? It's just different names?
**Jason Plumb** 56:16 Yeah, maybe.
**Cesar Munoz** 56:16 CLS and SSL.
**Jason Plumb** 56:17 Yeah.
I'll have to take another slower look at this. The other one I wanted to bring attention to is in the I.O. repo…
I believe…
This one, yeah. So, please take a look at this one as well. This is the dock site.
And I thought this was awesome because this person also just stepped up to, like, document what we're doing for us, which is awesome. So they, we've had a long-standing issue out here, which says that this placeholder that we currently have should be filled in, right? If you go here today.
It's like, wah, just, like, nothing. Like, no, not helpful at all.
And this person,
Oh, it's slow to render, but yeah, this person came in and dropped a PR on Christmas Eve. So…
Please have a look at this one if you haven't. There's a lot of good information here, and it's gonna really help us to have, this stuff fleshed out. So it kind of… it duplicates what's… some of the README, but then there's, like, awesome, like, code examples on how to, like, use the initializer, what the different configuration options are. I think it's an awesome start. I had some feedback, and it looks like they've incorporated it, so…
If you have other opinions, let's get them out there. Or we can follow it up later with an improvement, so…
Awesome. Any last-minute stuff from folks?
Alright, well, it's nice seeing everyone.
**Cesar Munoz** 58:00 Bane.
Thanks, and talk to you later.
**Jason Plumb** 58:03 Yeah, take care.
**Hanson Ho** 58:05 the next one?
**Cesar Munoz** 58:05 age.
**Hanson Ho** 58:06 Right.
