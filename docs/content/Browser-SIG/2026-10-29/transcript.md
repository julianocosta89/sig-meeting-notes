SIG: Browser SIG
Date: 2026-10-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:39 Alright, it's here.
**Aditya Reddy** 00:42 Hey, good morning.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:44 How are you?
**Aditya Reddy** 00:46 Good. Oh, you?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 00:49 Not so bad.
attend.
**Ted Young (Raintank, Inc. – Grafana Labs)** 00:56 Hey, how's it going, y'all?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:00 Alright, how are you doing?
**Ted Young (Raintank, Inc. – Grafana Labs)** 01:02 Doing a gate? Yeah.
Morning.
**Joaquin Diaz** 01:29 True.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:30 Hey, Quicken.
Let's just wait one more minute, There's nothing on the agenda at the moment, like, if you have anything you want to bring up… As usual, put it on the agenda.
Well, alright, I can get started.
So there is nothing on the agenda. We could… so, I guess… One update, quick update, we did have a release last week, And I think there's a bunch of things that could also go to… go… be released this week.
Let's see… I'm gonna share my screen.
**Jared Freeze (Palo Alto Networks)** 03:53 Thanks for taking over a minute.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 03:57 Freeze, Okay.
Yeah, so we have, in the release PR, we have, the refactor of the instrumentation base, which is… which is great that it was done. Thanks, Jared, for working on that.
Are we still waiting for some updates based on that, or are all the instrumentations now updated?
**Jared Freeze (Palo Alto Networks)** 04:39 They were all unnecessarily updated. There were a couple of things I found that are on a branch. I think it started getting reviews.
Called Base Fixes. So, I wouldn't release until that comes in, because there was, like, two legit… Stumbling blocks.
Okay.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:06 this one.
**Jared Freeze (Palo Alto Networks)** 05:11 Yup, that's right.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 05:13 Okay.
**Jared Freeze (Palo Alto Networks)** 05:14 Yeah, so a lot of the alerting was, not consistent, and then this one you called out, I need to fix right now. So, I'm talking about locked dependencies. So I changed the name to Resolved, because… I changed that to not necessarily be a lock and a lookup.
I may switch it back, I know that's kind of churny, but, you were right about I… I didn't… I didn't realize that it was important for people to know that it started before that the instrumentation started before the SDK, because I didn't consider people doing that outside of you know, doing, like, new fetch instrumentation, calling .enable, and then calling Start SDK. Like, that just seems so strange, but it is possible, so… So that's fine.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:03 Just educates us, right, so…
**Jared Freeze (Palo Alto Networks)** 06:05 Yeah, for sure. It's an easy, easy guard, so…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 06:08 Okay, cool, so yeah, like, once that's… Once that's merged in, I guess we could do another release, The other thing that I… I guess, just for cross-sharing, with SIGS, we had, in the client side.
Sig we had… we did a first release of the semantic conventions, the client-side semantic conventions, which does include the, our browser… semantic conventions.
So there is, in this repo, I'm gonna… We'll put a link in the notes here.
Yeah, so I think now that that's kind of… off the ground, I would like to get back into that, that work in this… in this repo, and do some… generate… start generating constants from, from the semantic conventions, so I'm gonna… that's kind of the next thing on my plate.
Hmm.
Alright, david. Sessions and propagation.
**David Luna Bistuer** 07:45 Okay, there's no topic, so just… some, Oh, that's something that we kind of commented yesterday, Jared, I already know that in the, in the, in the AIC. So… just to kind of, get ideas, or maybe just to kind of run through something that is okay. So, now we get in sessions. We have… Maybe it's something that it's not mature enough, but we have, at least we have sessions, we have session processes on the front end, but then those spans get the session ID as an attribute, and the spans unlocks, okay?
Right, okay.
So, was thinking that that makes sense to actually propagate this and have this kind of same information on the backend.
Thinking maybe on a use case, so yesterday kind of was… was kind of explaining the situation, but I think it wasn't clear enough.
So, let's say that I have a… I'm having a service.
that gets an error, and I want to know which session, Was affected by that.
So, for that, you need to follow the links to the parent spans, and get finally to the root span from the front-end span, and get the session ID.
what if I don't get that span? There was something lost in translation in the transit, and that span doesn't get there. So, okay, it's an incomplete span. Sorry, it's an incomplete trace.
But, I was wondering if I can propagate somehow the CND downstream?
then I could get, you know, this kind of a link between, okay, there's an error, the error is happening in the service, and this is the session that is being affected.
So, I don't know. Have you thought about that? Ideas, it should be something that is done My, text map propagation, and that's it.
I don't know.
M… Zed commented out that, also.
Propagating back from the back end to the front end is going to be difficult.
I agree with that.
But for now, I'm just thinking on the… this way around, so from the front end to the back end. So, okay, it says NAD, I want to propagate somehow, so the telemetry that I have in the… on the back-end services also are aware of the… of the session.
**Joaquin Diaz** 10:03 So, sorry, I'm trying to reproduce the case in my head. So you have an error request and has some error on the backend.
And you want to know, like, which session was associated with it.
**David Luna Bistuer** 10:14 Let's say the service has an error in the query, the meter.
Okay, so then I got this error in my APM view, but it's APM, it's not… it's not ROM, it's not sessions, you know? I'm in this view, I'm just viewing and analyzing that service, and I want to link somehow that that's this session, which is the session that was affected.
Then if I had the session ID, or if I got some link to the session, I can just drive my user from that specific UI, that actually… that specific analysis from the session, the APM analysis, to the session, and get an overview of the session. So this was the session affected, this was the user, and then from the front end, from the SDK from the Browser SDK will get all the events, all the jury from the user to get to that error.
So, yeah, basically it's how to link the backend service to the session.
What's the original propagation, yeah, yeah.
**Joaquin Diaz** 11:10 this span is created on the backend, not on the UI. Like, this is not a network request from.
**David Luna Bistuer** 11:16 wild thing.
**Joaquin Diaz** 11:16 outward.
**David Luna Bistuer** 11:17 Think about… think about the form submit. So, I create the… or a request, so I click on a button that actually does a request. Submit something, gets… makes some GET request to the server. So, I get the HTTP span.
the fetch span on the front end with access Unity.
Then, transparent gets propagated, so… the span that is created on the backend, on the HTTP span.
Gets linked to the front-end span.
And then, of course, the database span gets linked to that. So, in order to get the session ID, I should, you know, walk up the hierarchy of the spans to get the root span from the front end, but finally resolve the session ID.
So, yeah, that works.
Okay? It works if I have the whole trace complete, if I have the front end, too.
So… Is that good enough?
Or it's… I don't know, maybe it's better to actually… well, I don't know, Drop it.
It's something that is not crazy to actually say, okay, I'm gonna choose to passed down, would propagate the SRID as well.
So, you know, the thermometry I have on the backend service also at least has some link to the session, so some relation to the UI.
**Aditya Reddy** 12:34 Okay, so you're saying…
**David Luna Bistuer** 12:36 Maybe it doesn't make any sense at all, right?
**Joaquin Diaz** 12:38 No, it does, yes.
**Ted Young (Raintank, Inc. – Grafana Labs)** 12:40 I mean, this is a common pattern of using baggage, right? Like, in general, what people do with this kind of thing is we use baggage to send it down, and then, users configure… Like a span processor or something to attach Certain baggage items as attributes.
Onto spans.
And I think… I don't know where it stands, but I… there's been work kicking around to try to make some more official way of… attaching baggage to… as attributes to things, but I'm not sure where that spec work is.
But that's a pattern people have been doing with OpenTelemetry since the beginning.
**Aditya Reddy** 13:25 Yeah, that…
**Joaquin Diaz** 13:25 these days.
**Aditya Reddy** 13:26 dilute.
Sorry, go ahead.
Oh, I was just saying, that's what I thought David was already suggesting, is we just add it to the baggage.
was what I thought the ask was.
And keep it, like, opt-in.
**Joaquin Diaz** 13:44 Yeah, but if I'm understanding correctly, the case is that what happens if the permanent span fails to deliver, so we don't have the baggage on the span that gets propagated, right?
Because, for example, the trace hitter… That goes with the request, so we know it goes to the backend. But if we create a span that is supposed to be the parent of its network request on the backend.
And that fails for some reason, then we lose the connection.
So… what we're… what you're asking is, can we figure out something similar to how we send TraceParents?
like, the trace ID in the header, for example.
what if we send the session ID in the header as well when we do the request? So, we know that I'll listen back and know that there is some session attached to it, and then we can connect them together, even if the parent of that network request is missing. Is that what you're asking?
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:39 Yeah, that's what… that's what baggage is.
**Joaquin Diaz** 14:41 Oh, okay.
**Ted Young (Raintank, Inc. – Grafana Labs)** 14:42 Yeah, baggage is, additional tracing, like, arbitrary, headers, basically, for us to send additional keys.
So…
**Joaquin Diaz** 14:56 Got it. Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 14:57 But as far as I know, this is really intended for, like, custom things that users send. It's not, like… like, the spec doesn't really have anything… documented, like, for… that we have already decided should be done by all SDKs, right?
**Ted Young (Raintank, Inc. – Grafana Labs)** 15:15 We've traditionally seen… we haven't had internally, within OpenTelemetry a lot of use for baggage. We built baggage as actually a way to allow people to build other, The other cross-cutting concerns, right, that need to follow execution context, if you've already installed OpenTelemetry, we've done all that hard work to flow things through, so if you have a security concept or some other concept, right, like baggage is an API for… For modeling your own your own thing on top of our system. But yes, it's true. Internally, we've… we haven't, like… I'm not sure if we've officially used baggage anywhere, and… A more ideal place to put this would be… Yeah, like an official trace session header or something like that.
But… I don't think we have that. And the advantage of the baggage headers is, I think.
Have they… are there… I think they have been standardized.
through the W3C at this point.
But they're, they're known headers.
And less likely to get, like, chopped up.
And I think, unfortunately, a session is, like, too… a session ID is too big to fit into something like TraceState, or one of our other… Existing trace headers.
So… but at any rate, we have baggage, it's already a thing.
So it's certainly a place we could model this for the time being.
**David Luna Bistuer** 17:01 Okay.
**Aditya Reddy** 17:01 You can inject it at, like, same time, right? Add the session ID when the header is written.
**David Luna Bistuer** 17:16 Thank you. Yeah.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:18 So, Tad, do you think, like, this is something, like, that would need to be proposed to the spec? Or is it just something we can document, like, for the SDK? Like, if you want to do this, like, you can just send it through baggage, and…
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:34 Pete, I feel like it's… in general, a good thing to write down our model, right? Like…
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 17:41 Yeah.
**Ted Young (Raintank, Inc. – Grafana Labs)** 17:42 I feel like how we model sessions should be in the spec somewhere. Yeah. And, and if we're gonna pick a header to send this, we should write that down.
You know, it's like an official header and format.
So people know what it is, but… but I think we can prototype it first.
You know, make sure we're satisfied with it.
**Aditya Reddy** 18:06 I was… Yeah, we should probably have clear instructions, because I was like, what if… It's not followed correctly, you end up sending your… session ID is not to your backend, so… They go outwards.
**Ted Young (Raintank, Inc. – Grafana Labs)** 18:24 Yeah, I mean, in general, the whole aspect of, like.
How does security relate to client-side telemetries, like… It's not just… Session IDs, right? It's like everything.
But… I mean, cores and all of that stuff kind of… like, the whole point is to kind of prevent you from accidentally sending crap to… To random places, but… A way to avoid that would be, even though we're using baggage to send it, I don't know that we would necessarily… Like, one place to… one way to build this is, like, when we… whenever we start a span.
Like, whenever we, like, we're, we're, like, adding… whenever we create a context, right, or start a trace, like, we… we add baggage, because baggage is carried through the context.
But I don't know that we need, because this is, like, the entire Browser tab uses this, right? Like, it's a, because this is an entity.
that we're pulling from. I think on the browser side, it could just be in the, like, span exporter.
Or something like that.
Where, where this gets attached.
On the browser side.
So there's no need for us to use the baggage API on the browser, it's just setting it as a baggage header, so that the server side knows where to look for it.
**Aditya Reddy** 20:11 Yeah, that makes sense.
**Ted Young (Raintank, Inc. – Grafana Labs)** 20:14 And actually, that's another great advantage of using baggage, is that, the SDKs are already configured to… deserialize baggage headers when they see them, and… and add them as context, so… all the existing SDKs will… We'll know how to grab that session.
If you do it that way.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 20:41 Makes sense.
**David Luna Bistuer** 20:46 Thank you for your feedback. While we're doing something on Elastic, I'll let you know how it goes.
And then, what are the results, and maybe just, you know, based on the experience, then we just can… we can share something here, and then maybe we can put the things in common and make that documentation, and kind of, starting with additional documentation. Kind of, real scenario. Not of expressed this, because… something new.
But kind of documentation on how could be done, and they may… from that, we can just be above here.
**Ted Young (Raintank, Inc. – Grafana Labs)** 21:19 Yeah.
Oh, by the way, did you all see LinkedIn had a post?
recently about how they use OpenTelemetry, and they… they have modeled a bunch of stuff. They're using OpenTelemetry in the browser, in, like, client-side OpenTelemetry, and kind of built… built their own stuff.
On top of it, like, they didn't call it a session ID, but they called it, like, a page forest ID.
So they actually have modeled some of these concepts on their own.
It might be worthwhile to just… I'll dig that up and post it into our Slack channel.
But I thought it was interesting to see who's out there in the wild, basically building their own version of this on top of a hotel.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 22:14 It would be interesting to know, like, if they're considering… if they're aware of… This… these new instrumentations here, and…
**Ted Young (Raintank, Inc. – Grafana Labs)** 22:24 Yeah.
You're all… I found it. I'll add it to the,
**Jared Freeze (Palo Alto Networks)** 22:44 This is starting to make some sense, because I got a, I got a DM from a large company named in this blog post, which you can find yourself, that says, hey, where's the 3.0 version of the Browser SDK?
What can we do to accelerate?
I was like… Just give us a week or two.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:09 Yeah.
**Jared Freeze (Palo Alto Networks)** 23:10 But this actually makes a lot more sense now, because I was wondering why they were hunting down maintainers.
**Ted Young (Raintank, Inc. – Grafana Labs)** 23:20 But, yeah, looking at this… So, page, Forest… If I just share… Screamy… I'll click… So… they have a trace ID, span ID, and what they were calling a page forest ID, which sounds basically like a session ID.
Right.
**Joaquin Diaz** 23:58 Yeah, I don't know if his session ID sounds more like, they track, like, what page they're on. Like, the example says PF Hub.
As in, they will, well, they want to aggregate based on that date, for example, they want to see all the requests from the home.
Yeah. Not a specific, unique session, maybe.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:20 Yeah.
Yeah.
And maybe this is just… yeah. Yeah, I don't know quite… quite how different a page forest is versus a session. Maybe it's just single page.
But… Right.
**Joaquin Diaz** 24:40 That example, assess site.
PF home, so it makes… it makes me think that that's a way of… for them to know, you know, what's going on in their home for every user.
**Ted Young (Raintank, Inc. – Grafana Labs)** 24:51 Yeah.
So… the paid session, Yeah.
So, anyways, cool example of this already up, being out there in the wild.
**Jared Freeze (Palo Alto Networks)** 25:09 They have the authors list as well, and it says that they're using semantic conventions internally, so I'm gonna email every single one of them and say, come to the client side.
Meeting.
With links to their pages. Make it easy.
**Ted Young (Raintank, Inc. – Grafana Labs)** 25:30 No, that would… it would be fantastic to get some end users like that involved, people who are already… using this… Aggressively. That'd be super cool.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 25:46 Alright, few minutes left, I guess, Any other topics, or does anybody need help with anything?
We've got a bunch of… Pr is open…
**Aditya Reddy** 26:03 Yeah, for 486, can we decide on the client name? I like… on the… Names I cannot open on the Office laptop.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:18 Sir, which one is that, buddy?
**Aditya Reddy** 26:20 486.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:22 Right at 6.
Oh, the INP one, yeah.
**Aditya Reddy** 26:26 Yeah.
So adding, like, 13 fields. I just wanted… Everyone to agree on the names?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 26:38 Yeah.
Okay.
Yeah, I've seen this, and I haven't had a chance to think about it yet, but I'll take a look.
Look at it.
Also, it'll be something worthwhile, bringing to the client side.
SIG, from the semantic convention side perspective.
**Aditya Reddy** 27:00 Okay, I don't think I'm in that group, is… Is there a way to get… Anyone share a link?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 27:12 Yeah, I'll send you, I'll send you a link, yeah.
**Aditya Reddy** 27:14 Okay, thank you.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 27:18 Right, I think we're done then, if there's nothing else.
Cool, thanks everyone.
**Jared Freeze (Palo Alto Networks)** 27:24 Diaz.
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 27:25 dear.
**David Luna Bistuer** 27:25 Thank you. Bye.
