SIG: Specification SIG
Date: 2025-10-14
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Robert Pająk** 00:41 Hello, how are you?
**Reiley** 00:45 Alright, don't worry.
Hey, I know.
**Daniel Dyla (Dynatrace)** 00:51 Hello!
**Liudmila Molkova** 01:24 Hello! Hi, everyone.
**Reiley** 01:29 At all.
**Liudmila Molkova** 01:34 Yeah, I'm going to drive the meeting today. Give me a sec to prepare, and in the meantime, feel free to add things to the agenda.
While we're waiting, when was the last time we released the spec repo? It was last month?
I'm just checking if it's the time for the new release.
**Reiley** 03:19 I remember seeing a PR yesterday that Carlos is preparing the release.
**Liudmila Molkova** 03:24 Oh, okay.
**Daniel Dyla (Dynatrace)** 03:25 There's already a PR open for version 50.
**Liudmila Molkova** 03:31 Oh, cool.
**Daniel Dyla (Dynatrace)** 03:31 Let's see.
It looks like the most recent was last month, yeah.
**Liudmila Molkova** 03:39 Carlos is very fast.
**Daniel Dyla (Dynatrace)** 03:42 On the 16th.
Oh, sorry, I thought I was muted.
**Liudmila Molkova** 04:00 You didn't say anything bad.
Okay, let's give folks a couple of minutes to join. We have just two items on the agenda. If you want to discuss anything, please go ahead.
Sirbi, do you want to give any time estimate on the issue?
**Surbhi Agarwal** 04:29 I don't have any idea. Maybe to begin with, 15 to 20 minutes?
**Liudmila Molkova** 04:36 Okay.
Cool.
**Robert Pająk** 04:47 Alex also wants to add some… no, it's the release PR, okay.
**Liudmila Molkova** 04:59 Okay, so then let's get started. We talked about the release, let's talk about extended attributes.
Robert, do you want to present? I think there are some discussions. Do you want to go through them, or what do you want to do?
**Robert Pająk** 05:17 So…
I wasn't able to be last week and the week before, so basically, I feel that I addressed all the comments.
So, basically, if there are things are open here, it's because I'm just double-checking, for instance, with Tigrant, if he's fine with this, but I think, I think Interior could even resolve all the conversations.
I do not think that any comment is not addressed. Also, I saw that, Dumi, while you were also reviewing this PR, I'm not sure if you checked the open discussions, or you just checked the actual content.
**Liudmila Molkova** 05:50 I checked the actual content, it looks good to me.
**Robert Pająk** 05:53 Okay, yeah, I think that I addressed all the comments, so yeah, I basically begged for approvals. It's more open more than a month.
And we would love to have it for KubeCon, and also, also to have the blog, the blog post that Little Mio is preparing, also to have it probably released together with the OTLP changes. So, yeah.
Are there any questions? I guess… I remember last time, Tigran, you said that you review it, but I guess you simply did not have a… you didn't have any time, right?
**Tigran Najaryan** 06:28 Sorry, I didn't… I will do that today. Sorry, sorry about that.
**Robert Pająk** 06:31 No, it's fine, it's fine, no problem.
**Carlos Alberto Cortez** 06:36 I left a comment, but for some reason, it hasn't been posted. It appears to me as pending comment.
And these Awesome.
Regarding, like, usually we don't update, we don't go and update existing OTEPs.
So, yeah, and usually, like, tips are just, you know, like, a desire to change something, which may still change when we are applying that specification.
So, for me, it's fine that you went ahead and updated that. Well, I hope we don't make that a tradition.
**Robert Pająk** 07:09 I wanted to do it just to make sure that… to make it clear that it is, you know, different than it was originally proposed in the OTAP, and we also discussed in the SPAC meeting, just, you know, just to make it as clear and cohesive as possible.
I don't know, Carlos, what do you think about this?
**Carlos Alberto Cortez** 07:28 Yeah, I remember somebody complained of, about, for example, and this is when we had to clarify, it's not important, just the historical context, that we approved an OTEP, and it was merged, and then when we were applying that OTEP into the specification, we did change the contents.
And then he was complaining, like, if you compare that with the specification, it was different, and we had to clarify that. But now, like, for example, if somebody were to complain about that, that person may go ahead and check, hey, that's not the type I approve, you know, etc. Something like that.
Anyway, I have no problem with this, I just hope we don't make a tradition of updating a tapes, otherwise we would have to go and update a lot of stuff there. Yeah, that's all my… so it's… I'm fine with this, I just hope we don't make a tradition.
**Tigran Najaryan** 08:18 The alternate approach could be that instead of modifying the OTEP with the new content, you… you just link to the PR that makes the modification to the spec.
which impacts the OTAP, and essentially make a note in the OTAP that what the OTAP says is no longer up-to-date. Go read this part of the specification to know what's the current state of things.
So you keep the original OTEP as it is, but whoever reads it now knows that this is not the complete picture. They need to go read something else in addition.
**Robert Pająk** 08:59 Okay, so you prefer to have an OTAP? Like, the…
**Tigran Najaryan** 09:02 Changes you made…
**Robert Pająk** 09:03 does originate in…
**Tigran Najaryan** 09:05 the changes you make to the spec, they are… they describe the whole story, right? They describe how it changes the entity, data model, all of that is there, right? So, the OTEP can stay as it is for historical, like, reasons. It's how it was when it was proposed and approved.
But somebody who reads it, we don't want them to be misled by the, I guess, outdated content of the OTEP. You just add a link which says, here's more data to go read, because it overrides, essentially, what the OTEP says.
in the relevant section of the… of the OTAP.
for the… for the entities OTEP, that would be the… the data model section, right?
Just an idea how to maybe address this, so that you don't make extensive changes to the LCAP itself. It's just, you add one line and that's it.
**Robert Pająk** 10:03 Okay, so do you think that, you know, we have Git, assuming I have done the work, do you think that it is fine, or do you prefer to revert these changes in OTAP and just add some kind of appendix?
**Tigran Najaryan** 10:18 Yeah, I guess you could keep the… most of what you have in the PR, because it modifies the spec, right? It changes the logs, data model, entities, data model, all of that. That can stay.
The… the changes in the old tabs, you could, yes, you could revert and just add the small link to the P… to this PR, essentially, itself, right? Which says this is… this overrides.
**Robert Pająk** 10:44 I could even… I could even make a short appendix linking DPR and making even two statements how it has changed…
**Tigran Najaryan** 10:52 Yes.
**Robert Pająk** 10:52 changing.
**Tigran Najaryan** 10:53 Yeah, a link and, like, a one sentence or two sentences, how exactly it changes, yes.
**Robert Pająk** 11:00 Okay, I will do it.
**Carlos Alberto Cortez** 11:04 What do you mean?
**Robert Pająk** 11:06 You want to leave a comment, Carlos, or I can do it myself. I'll do it myself.
**Liudmila Molkova** 11:10 I'm taking notes, if you can leave a comment, that would be great.
Okay.
Anything else on this?
Cool, so then please take a look at the PR, and let's move on to the next topic. Serbi, let's talk about HTTP spans for Network Phases Breakdown.
**Surbhi Agarwal** 11:53 Yes.
So there has been some good discussion on this ticket. I was wondering how to go about it, what would be the next steps. So, like, the conclusion from the discussion so far, I think, is…
Like, to figure out the different network phases, break down the timeline around those, so backend can derive various metrics on it.
There are two different proposals. One is, we add… attributes, like, connections, dot.
connection end, DNS start, DNS end, like this to the HTTP span itself.
And then have a configuration, which is like a list of connection-level attributes, and a list of request-level attributes. The request-level attributes would be request header start, request body start, response body start.
So, these lists would be default, Lee empty, and…
It can be customized to indicate what
Do they want to capture, so there is not noise unless needed?
This is useful because we don't add a separate standalone event, so the browser's idea is to add a separate standalone event, which is resource timing event.
But the problem with that is you'd need to replicate all the attributes from your original HTTP span that you require. Otherwise, the backend needs to correlate between the HTTP span and the event somehow. There is a trace context available.
To correlate, but then the backends do metrics processing in a timed batch.
the timing is sometimes as short as a minute or something, right? They need to cache one until they receive the other. What to cache, what will receive first, there is timing mismatch. All those sorts of issues are there. So having everything in one
span as attributes would be very helpful, to not have these issues. So I wanted to understand what people here think, and based on, let's say, that these are the two things between mobile and browser.
How to go about it.
**Austin Parker** 14:37 I mean, I think there's a pretty decent argument for consistency between the two.
And favor… with the idea that we favor pushing that kind of logic down to the client, rather than…
Requiring it on the server.
Right, so… doing the… You know, computing these values at,
Client right, rather than a server right.
I… obviously… There are cases where that is suboptimal.
But… Broadly…
I think… Pre-calculating this stuff, putting it all on one event or on one span as attributes.
And then, sending it in…
Winds up being better in most cases, for most people, most of the time.
**Surbhi Agarwal** 15:58 Yeah, that gives flexibility to the backends to decide what metrics they would like to
have, and whether they have the… and to then configure available
Attributes into their spans, so they are able to do that.
**Austin Parker** 16:20 It also, I mean, I also, like… it… The… the upside to…
Turning these things into attributes and putting them on, like, the…
The logical route of this operation is that if people would like to transform those and turn them into a series, then they can… it gives you more options for how to do that, so you could either do that in the
you know, collector pipeline, you could do that at query time, whereas if you are doing these as individual events and requiring consumers to handle… to handle it, then you've added… I mean.
more or less stateful either way, but it's a different type of sta- like, it's a…
More annoying state the latter way, because you have to, buffer, you know.
a large amount of events, and then, parse them down to what you care about. So, I…
**Surbhi Agarwal** 17:29 Not a large amount, like, the proposal sort of had… it has advanced to, like, Just the relevant attributes.
Based on the configuration that the…
user would have an option to set. First, the, like, the instrumentations provide the users that option, so they can exactly decide what timestamps out of the following they want.
And, like, to add to the aggregation…
headache, like… like, Splunk has its own time series and… Different metrics.
aggregation, logic. So, like, they do want this kind of a raw data, so they can apply their own aggregation logic on top of it in their own backend processes, right?
And not go via the… Jay.
**Austin Parker** 18:25 Yeah, I mean, I…
I don't think you're gonna find… I don't think you're gonna get every single person to agree, because every backend does things slightly… like, there's… there's enough distinctions between these, between different backends, you know?
From a forward-looking perspective, you know…
Column stores are very popular, having the…
You know, and doing these sort of things… as pre-aggregates…
Or pre-aggregated values on a span.
Very easy for column stores to handle that.
I, I mean…
I don't really think we have, I mean, I suppose we could always, you know, one thing we could consider is if…
If it really is, hey, there's two ways to do this, maybe…
We need to provide two ways to do this.
And Should be a… do you want these as individual events, or do you want these as,
You know, roll-ups, basically.
I'm… I'm mostly trying to think of the…
I'm trying to think, what's the eas… if there is one way to do it, what's the easiest way for people… which one is easier for people to transform? Like, downstream?
Is…
**Liudmila Molkova** 19:57 Can we talk about feasibility first?
**Austin Parker** 20:01 Sure.
**Liudmila Molkova** 20:03 So… Some of, like.
if I can, summarize, there are two proposals. The first one is to represent those as events.
Maybe a spence?
**Surbhi Agarwal** 20:14 One event.
Containing all these.
like, the discussion advanced to having one event containing all of these phases. Just wanted to clarify that.
Like, those would be standalone events.
a standalone event which has trace context tracing back to the original HTTP span, and that contains
All these different phases and the timestamps for the start and end.
**Liudmila Molkova** 20:44 And option 2 is attributes on that span.
**Surbhi Agarwal** 20:48 Yeah, which can be limited with the configuration list.
**Liudmila Molkova** 20:55 Yeah, so in this sense, this do not… are not… are somewhat orthogonal to HTTPS pens to start with, right? Because connections are pulled, and
the connection pool can be not even HTTP-specific in theory.
But essentially, these are not… does not belong on HTTP spans.
**Surbhi Agarwal** 21:19 Yeah, we did discuss that.
But there is value in knowing whether this… why did this particular request take a lot of time? So, okay, there was connection handshake for this request. It was the first request to this server, that's why it took time. So, I understand that there is connection-level instrumentation, but that serves another purpose.
when you want to look deeper into the connection, DNS, and security stuff.
But this is… per request level, we want to understand what happened during the request duration, whether there was connection.
And how much duration did each of the phases take?
**Liudmila Molkova** 22:03 So what you're saying, that for this specific feature that you are proposing, if there… there was no connection setup happening, that you would not have those attributes on either event or span?
And this instrumentation would do… would not provide any visibility into connectivity.
**Surbhi Agarwal** 22:25 These attributes of zero can be removed, not added to the span to reduce the amount of data sent over the network, right? And if there are values to these, and it happened for… it was initiated for a request, then these values would be included in the span.
**Liudmila Molkova** 22:46 Yeah, so then if there is a separate instrumentation of those things that are not specific to HTTP span, then
The, theirs would be duplicated.
**Surbhi Agarwal** 22:57 No, that is not needed, right? Like, the… like, in Android, one of the most used
HTTP clients is, like, OKHTTP. That does have a listener, which provides callbacks to all these different stages. You don't, like, you just need to…
Add that listener and gather these attributes to add in the span, if that makes sense.
**Liudmila Molkova** 23:21 Yeah, so my question about is something different. Can we clarify something? Is it specific to client and browser, or is it the generic feature across all different instruments for HTTP?
**Surbhi Agarwal** 23:35 Client and browser, yes.
Oh…
**Liudmila Molkova** 23:40 Others, I'm not sure of.
**Austin Parker** 23:44 I mean, any HTTP client would have all this stuff, right?
**Liudmila Molkova** 23:53 Yeah, yes and no. So, if it's server-specific, that connections are mostly pooled, and this would not be available most of the time.
Also, the… our ability to measure the response body end, is very limited. We actually end the span.
At this point, HTTP span, in most cases.
So, it's up to very specific instrumentation to actually be able to reasonably capture
some of those details. And also, the connectivity server to server is usually much better, so you're probably much less interested in specific
Details.
**Austin Parker** 24:32 No, I, I mean, I agree with you there. I'm…
I do like what Daniel said in the chat, the…
As much as I'm in the… You shouldn't.
Make small spans, like…
If these are true, you know, if these are things that happen that have a duration, then… you know…
That's what a span is.
And if you are trying to metric size these, then it's just as easy to… it's probably easier to metricize a…
a single… named span… Than it is to…
Do a bunch of… of math.
Or do a bunch of, like, state management, and da-da-da-da-da.
**Liudmila Molkova** 25:27 why would we… like, where does the desire to report metrics as difference between attributes come from? Why it's not a metric?
**Austin Parker** 25:35 The next part right there.
**Liudmila Molkova** 25:37 Right, why is it not a metric? We actually have some metrics like this.
**Surbhi Agarwal** 25:41 Yeah, there are different metrics that a backend might need to derive out of it, so we don't want to choose
Like, the best of these, because all of them are…
needed, based on the requirement a particular company has, right? So, like, they… if we provide the raw timestamps, they are able to calculate what they need, and, like.
have their own sort of metric aggregators, processors that work on it, and not tied to any particular calculation, like histograms, in case of
some HTTP metrics, which are defined in hotel, right?
**Liudmila Molkova** 26:26 So if you have spans that represent start and end.
And you already would have the raw data to re-aggregate it however you want.
**Surbhi Agarwal** 26:36 I feel like span is too much, because we don't have any other data, like…
This does has the duration, I understand, but this doesn't have… this is not an entire instrumentation, it doesn't have other data to go along with it.
**Liudmila Molkova** 26:56 It does, though. It has the status, right? If you had an error by writing request body.
you would see it on that span. How would you represent it as an attribute? You would have… you would have to flatten it down to the out…
Through the resulting.
spam status.
**Surbhi Agarwal** 27:15 Span status is there in the original span, right? The response status also.
**Liudmila Molkova** 27:22 Yeah, if somebody opts into those sub-spans, those subspence would have substatuses.
And you would be able to see that, oh, your request has failed because you couldn't write the request body, or you couldn't… the request failed because you couldn't read the response body.
**Austin Parker** 27:41 Right.
Yeah, the more we talk through it, I think the… Question really is, like…
caveat, I don't think, the front-end people would be happy with these being subspans either, but, like.
I also don't… It's hard for me to see a reason why they shouldn't just be subspans, and… with…
With some way to…
With a processor or something that could turn them into attributes, if you wanted to flat… if you wanted a flat…
HTTP span, right?
But they should be represented… In memory as spans.
**Surbhi Agarwal** 28:32 There is another point, like, to the point we were discussing just before, right? We don't really need separate status on each of these. Like, if the, let's say, request body… response body end is missing, we know something went wrong, the header was received.
But the body started… we started receiving the body, but we don't have an end time stamp, so something went wrong there, right?
So, we don't really need… Like, status for each phase.
The overall status is fine, and the missing, let's say, end timestamp, or the missing attributes will tell us that, hey, this phase completed, and after that, something went wrong.
Does that make sense?
**Daniel Dyla (Dynatrace)** 29:20 I think you could make that argument for…
Almost any child span of any kind, you could say an error would bubble up to its parent.
They're like, why not just have a single span that represent the entire operation, and then events for everything? It's because the semantic… you know, the structure gives it semantic meaning.
I… anywhere where I see start and end.
my first thought is that's a span. And to say that the overhead of… Span is too much.
I… I… I'm not sure that I agree.
That there's any meaningful overhead difference between two events versus one span.
**Surbhi Agarwal** 30:06 But between…
**Daniel Dyla (Dynatrace)** 30:07 from, like, a memory allocation perspective, but also, like, a wire size perspective, I think it's… I mean, we're talking about very, very…
**Austin Parker** 30:17 Small differences, and…
**Daniel Dyla (Dynatrace)** 30:20 Allocating two events is likely more impactful than allocating a single span.
**Surbhi Agarwal** 30:29 I wanted to clarify, like, the proposal was one event containing all.
The attributes for all the timestamps.
like, not multiple events. And one more thing is, like, would you… would… do you think that attributes on the original HTTP span and additional spans, would they not have difference?
Well, if they were…
**Daniel Dyla (Dynatrace)** 30:56 So it's one event with a bunch of timestamps on it? I guess I misunderstood.
**Surbhi Agarwal** 31:02 Yeah.
**Daniel Dyla (Dynatrace)** 31:03 Yeah.
I mean, to me, that strikes me as even weirder.
**Austin Parker** 31:09 Yeah, I would say, like, from a pure efficiency standpoint.
A single… having, you know, having all of these be attributes, be computed attributes on the logical root of the operation is the lowest overhead.
Right, because you're still… Because attributes are, you know, cheap.
And you're effectively, you know, in terms of, like.
Duration… timers and all this, you know.
that all comes out in the wash, I feel like, if you're creating, you know, spans per each, or whatever. The second lowest would probably be…
I guess would be the, you know, single… single event with a bag of these attributes on it, because you're, you know, you're allocating one single thing.
But you still have to compute all the… you still have to have… you're still recording all the attributes, so, like, it's not that much of a difference. There's, like, probably a little difference, because you're writing, you know, just… you're not having to do the computation of duration.
But again, like, you're already paying the overhead of OTEL, like, I'm not sure…
How many, you know, microseconds or whatever, you know.
at some point, like, I feel like if you're at the point where you're that performance sensitive, you're probably not using…
In-memory tracing, you know, you're not using in-memory spans anyway, and you're… You're writing out events.
I think the biggest thing is just, like, what feels… like, what is the least surprising thing to end users? I feel like…
To Daniel's point, A additional event that has, sort of, this bag of… bag of extra attributes, which are…
timestamp, name pairs is weird. Like, nothing else does that, as far as I'm aware.
And logically, Like, it becomes really hard to do something with that, other than turn it into… a metric.
Because the data…
unless you flatten that out on ingest and turn it into something, or you flatten it out at query time onto…
parent.
Like, just having a grab bag of attributes doesn't…
Strike me as terribly useful, because you would have to go through…
to do it quickly, at least, you would have to flatten them, I guess.
I guess if you only cared about it in the context of, like, one single thing, it would be quick, because you would have the trace… you'd have the context on there, so you could…
you know, say, get all of these for trace ID, whatever, span ID, whatever, across this period of time.
But…
Turning those into aggregations seems like it'd be really expensive, like, at query time, because the cardinality would be very high, it would be…
the… whatever, you know, whatever the cardinality of, like, your trace and span ID is.
**Surbhi Agarwal** 34:48 Perhaps it's sort of an option, right? If your backend wants it one directly…
confirms to the hotel-derived metrics, which are directly sent from the, let's say, client side. They can go that route, but if they have… there are backends which have use cases to have their own aggregations, right? If that's their use case, they can perhaps have these attributes.
like, adding to what you were saying, right? There are use cases for both, so is it possible to provide both, and… because users can choose based on the need?
**Daniel Dyla (Dynatrace)** 35:33 I agree with that concept in theory. I mean, in general, in OTEL, we try to provide
Primitatives that allow the users to choose the way that they want to…
Represent their data, and that, you know, it should be possible To get the data in… Whatever format,
I guess I'm just… there's… to me…
Or to get the data, not necessarily in whatever format, but to get it at all, to get the source data that metrics are computed from.
To me, these look like spans. But then also.
You said that it would be attributes. I…
see… in the issue here, it says span events.
With proposing event names per naming guidelines. Two things there. One, I think these are spans, not events, but two, span events are being…
deprecated to my knowledge, aren't they? Or did that not…
**Liudmila Molkova** 36:42 Oh, they are.
**Daniel Dyla (Dynatrace)** 36:42 that.
**Liudmila Molkova** 36:43 HR.
**Daniel Dyla (Dynatrace)** 36:43 reversed.
**Surbhi Agarwal** 36:44 Yes, actually, the discussion has progressed. Sorry, this was my first proposal. There has been significant discussion beyond this.
And, like, span events are…
like everybody mentioned, going to go away. So instead, the final propo… the final two proposals that I bring today is one standalone event containing all
and two, like, attributes on the HTTP's plan, and then now we are discussing other ways, yeah.
**Daniel Dyla (Dynatrace)** 37:14 Got it, okay.
**Austin Parker** 37:15 Yeah, I, I think…
**Daniel Dyla (Dynatrace)** 37:17 I, I think, I mean, I…
**Austin Parker** 37:20 My… my gut is that…
To your point, like, the only way, you know, to your…
And I respect that, yes, there are different, you know, connection pooling, da-da-da-da-da, but…
you mostly care about these durations in the context of whatever request it is, right? Like… you're not…
You probably aren't going through and doing a…
query about DNS resolution across the
everything. You… but what you probably do want to know is, okay, I have 10,000 requests here.
And let me look at the P95, and let me see what those things have in common or don't have in common. And then you would see, like, oh, things that were on this node or this pod were having, like, DNS timeouts or failures.
I care about… these… these things, these durations of these various HTTP lifecycle events in the context of
what I am trying to do, which is the actual HTTP request response flow, right? So, from the strictly that perspective, it makes the most sense to me to say, these should all be attributes. And, helpfully, that normalizes, like, the front-end world and the back-end world.
I think, if not that, then, like, okay, we record these things as spans, and then users have the option to do roll-ups, either in their ingest pipeline or at query time, where they convert those spans into attributes, from a query perspective, or
They take those attributes and turn them into…
Time series metrics at, like, a collector.
**Surbhi Agarwal** 39:27 Yeah.
**Austin Parker** 39:27 I mean, but you could also do that with, like, the, you know, attributes on spans approach, too, right? Like, it's a question of which pipeline do you want? I think…
In my opinion, my professional opinion, the path of least surprise here is that these should be attributes, that the durations should be attributes on spans.
And…
I, I am…
**Surbhi Agarwal** 39:57 Yo.
**Daniel Dyla (Dynatrace)** 39:58 Having the durations be attributes on spans, would mean that you cannot… one of the examples given, I think it's, like, network setup time or something like that, it uses timestamp across two of the categories, so if they… if you only had the duration, you wouldn't be able to do that.
**Austin Parker** 40:17 And so for things like that, that would… for things that are out… that aren't part of a logical…
single requests, and those would need to be, like, separate spans, or separate events, or something, right? Like…
Because then it wouldn't be part of the… logical HTTP request, right?
**Surbhi Agarwal** 40:37 It's part of the request, but, like.
the total network connection duration would be when the TLS end timestamp minus the DNS start timestamp. They are all part of the request, but it is using a TLS end and a DNS start, so the proposal was to add timestamps rather than to add
durations. So, any metrics, like network setup duration, can also be calculated, and separately, DNS duration, TLS duration can also be calculated. Does that make sense?
**Austin Parker** 41:11 Yeah, Trask and the Milla have their hands up, so…
**Trask Stalnaker** 41:16 Oh yeah, thanks.
I'd…
I think that I do see a difference here between, you know, client-side and server-side instrumentation, and what's sort of optimal path there. For server-side, where, you know, you have really high… you're talking about really high throughput services.
And capturing all of those span… all of those extra attributes on every single HTTP span.
Is kind of a lot, and not, the more optimal path there is metrics and exemplars for connecting them back to individual, spans.
Whereas on the client side, we've heard this, a lot, that they don't want to really emit metric… metrics don't really make a lot of sense client-side, and they want things
on spans.
Not sure the, I don't have a solution how those things can coexist.
But on the client side, I did want to mention,
From an implementation perspective, the easiest is going to be stamping timestamps directly on the span.
Because we already have the concept of current span that propagates into these different paths, and so it's easy in, you know, when you get the DNS
Start and events to stamp those.
I don't know about duration, if, like, the callbacks give you
Duration, or if you have to, you know, sometimes we have to do weird things of capturing something into the context, and…
Reading it back later.
**Surbhi Agarwal** 43:14 Yeah, modern, like, clients, HTTP clients, should give you the callbacks to
each event, right? The start and end.
**Trask Stalnaker** 43:24 Okay, great. So you could stamp the duration directly on the…
Span, the current span, easily.
**Surbhi Agarwal** 43:32 The timestamp on the span.
The individual timestamp, the start and end both, so different metrics can be calculated.
**Trask Stalnaker** 43:42 Okay, so the callbacks are… there's separate callbacks for start and end.
**Surbhi Agarwal** 43:48 Versus one callback where you could calculate the duration client-side?
Yes, there is separate for start and end.
**Trask Stalnaker** 43:57 Okay.
So, I mean, I… From an implementation perspective, that would be the easiest, then, to… Just in those callbacks.
Get the current span, and stamp the attribute onto the… the timestamp onto there, and not do any,
duration calculation.
**Surbhi Agarwal** 44:19 Yeah, and, like, we can provide configs, like a list of…
connection attributes and a list of other attributes that they want to add, we can figure out a better way, and then based on the selection, only we add… slap those attributes on the HTTP span, otherwise we don't, right?
To reduce the noise, if not needed.
**Liudmila Molkova** 44:41 Sorry, I'd like to call time on this. We have a couple of other topics. I think we had a great discussion.
If I can propose something, maybe we can have a prototype of a specific instrumentation for the client, let's say for a KHTTP, and if it could be an experimental instrumentation.
That we can gather feedback on, that would be wonderful.
**Surbhi Agarwal** 45:06 That sounds great. I do have a ticket in the OKHTTP instrumentation in the OTL Java instrumentation repo. I will try to add it there to showcase an example. We do use that in our proprietary SDK as well.
So, we will gather some data there.
**Austin Parker** 45:27 It would also be good if the… prototypes could…
If it could be prototed up, you could find people that had multiple different backends, or at least different styles of backend.
To benchmark it, or to try it out.
**Surbhi Agarwal** 45:42 Yo.
**Liudmila Molkova** 45:46 Okay, thank you all for the great discussion.
**Surbhi Agarwal** 45:51 Thank you.
**Liudmila Molkova** 45:53 Let's move on to the next… next topic. Time-rated reserver assembling. Who added this? Is it David?
**Carlos Alberto Cortez** 46:00 I put that myself, but yeah, David Ashbold created the PR, it has 3 reviews, by the way, and this is a PR we discussed last week. I have asked David to hold it for a few more days.
so maintainers can be aware of these. So, please, if you're a maintainer and you were not here last week, please take a look.
Otherwise, it looks good.
Probably we should merge it soon, maybe the end of the week.
**David Ashpole (dashpole)** 46:31 Yeah, I'm not in any rush on this one, so happy to wait for reviews.
Appreciate anyone who wants to take a look. Thanks.
**Liudmila Molkova** 46:42 Okay, thank you.
And Anton, do you want to talk about KubeCon?
**Antoine Toulme** 46:48 Hello, everybody.
very short announcement that we are going to have a space at KubeCon where we can meet.
If you would like to use some of that space for some time, please send your interest on this form. You can submit more than one entry, you can have as many entries as you want, and the idea is then we just are going to put that into the spreadsheet so that we have maximum of
People being together.
Please, and please send that to everybody, you know?
**Liudmila Molkova** 47:20 Do you envision it as something like the people meeting on whatever topic?
**Antoine Toulme** 47:25 It's a secret.
**Liudmila Molkova** 47:26 Formally.
**Austin Parker** 47:27 story.
**Antoine Toulme** 47:28 AMA could be, like, I want to talk about one particular topic, I want to just have a discussion about Java.
**Austin Parker** 47:35 It's like… it's like the past few years with the observatory, it's the same… same thing.
**Trask Stalnaker** 47:42 Antoine, I'm looking at the form there, if I click SIG, like, if I want to do a JavaSig.
meet up.
Do I click… other and, say, Java?
**Austin Parker** 47:55 I'm not sure what SIG… how do you know which… how do you know which SIG I… I'm gonna do? I guess you know.
**Antoine Toulme** 48:02 of decisions.
**Austin Parker** 48:03 session.
**Trask Stalnaker** 48:04 Describe the session perfect.
**Antoine Toulme** 48:05 And Traska will do the hard work of making sure I read everything.
I will, I will…
**Trask Stalnaker** 48:10 Fantastic.
**Antoine Toulme** 48:11 What we'll do, actually, is probably we'll just send the answers to some form of some sort. We'll make sure that this is, you know, we'll make it happen.
We'll ask ChatGPT to do it.
Yeah, works.
**Austin Parker** 48:23 Some, some pipe…
**Trask Stalnaker** 48:25 That's why you said I'll do the hard work of actually reading, as opposed to just feeding it to chat GPT.
**Antoine Toulme** 48:32 I like reading stuff.
**Austin Parker** 48:33 If you are on the fence about attending KubeCon this year, we have a very, very cool gift for maintainers.
So…
**Antoine Toulme** 48:46 Well, I wasn't sure before, but no.
Thank you, Austin.
**Austin Parker** 48:51 You should either show up yourself or have a very trusted proxy to, because I think
Unless they are very trusted, your gift might not get to you.
They're very, they're very nice shirts. Baseball shirts.
**Antoine Toulme** 49:09 Wow. Okay, well, I mean, Mehdi, thank you.
**Liudmila Molkova** 49:16 Awesome. Thank you all there at the end of the agenda. Is there anything last minute anybody wants to bring up?
**Austin Parker** 49:23 A gentle reminder that GC elections are happening soonish?
Don't wanna… X suite?
**Daniel Dyla (Dynatrace)** 49:33 The deadline for nominations is, like, the end of this week, right?
**Austin Parker** 49:36 Yeah, that sounds right.
So… yeah, keep an eye on your mailbox for…
The… the election info when that comes out, and…
End of this week, you should… I think everyone's names should be up.
I believe we'll have a blog post,
Announcing, like, when the nominations have closed, so…
**Liudmila Molkova** 50:09 Yay, good luck to all, participants!
**Austin Parker** 50:13 Yeah.
**Liudmila Molkova** 50:15 Thank you all.
Have a great week!
around.
**Trask Stalnaker** 50:20 a…
**Surbhi Agarwal** 50:22 Bye-bye.
**Carlos Alberto Cortez** 50:23 Beautiful.
