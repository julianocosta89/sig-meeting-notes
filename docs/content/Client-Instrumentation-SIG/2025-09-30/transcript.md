SIG: Client Instrumentation SIG
Date: 2025-09-30
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:13 Martin, I'm really hoping you can drive, because I'm pretty sick, and I just did the Android call, and I feel terrible.
**Martin Kuba** 01:19 Okay, yeah, sure, no problem.
**Jason Plumb** 01:21 Thank you.
**Martin Kuba** 01:44 Doesn't look like there was a lot to discuss last time.
**Jason Plumb** 01:57 No, it was mostly shutting down the project board, I think.
**Martin Kuba** 02:06 Man.
**Jason Plumb** 02:09 Because there wasn't a lot of long-term traction on that thing.
**Martin Kuba** 02:21 Yeah, I'll just wait one more minute, and… Doesn't seem like… to the observation.
topic soon.
**Jason Plumb** 02:32 Yeah, Hanson was not on the, on the Android call, so he's probably away for whatever reason.
**Martin Kuba** 02:37 Okay.
**VP Valentin Pertuisot** 02:43 Hello!
**Jason Plumb** 02:45 Hello.
**VP Valentin Pertuisot** 02:53 Hello, sorry. Bye.
My headset was still connected to the MacBook.
**Martin Kuba** 03:09 Alright, I think we can probably get started.
Serbi, you have the first topic.
**Surbhi A** 03:20 Hello?
Yeah. So, there are currently, like, the HTTP spans, they provide us the duration of the HTTP request, but they… it does not provide the exact duration of various steps in the network request, like how much DNS resolution took, how much the TLS setup took, how much the connection time was, what the server processing time was.
So, I have proposed adding events to the, HTTP spans.
So, let me share my screen.
Give me a minute.
So yeah, I wanted to gather what the group here thinks about the same.
**Jason Plumb** 04:31 And even though Serbi's coming in kind of from the Android perspective, the Java instrumentation perspective, these are probably attributes that Events that could apply across client instrumentations.
**VP Valentin Pertuisot** 04:46 Yeah, I confirm.
**Surbhi A** 04:49 So, like, this is, can you guys see my screen?
**Martin Kuba** 04:53 Yes.
**Jason Plumb** 04:54 Yup.
**Surbhi A** 04:56 So this is a proposal to the semantic conventions repo.
So proposing these event names, we just need the timestamp when this event happened, and the event name. The attributes are present in the HTTP spans, so that would suffice for drilling down.
So, like, these are the different, event names that… We have proposed. So they help you figure out the DNS duration per request. The currently, the existing metrics that are available.
They provide… they do aggregation at the… agent level.
The server doesn't get per-request correlation.
And the duration per request for each of these, and the exact timestamps.
So… This is what is being proposed, and then, once these events are approved, like the various client instrumentations.
They can… Go ahead and add… these to their instrumentation. So basically, for an example, like, the OKHTTP instrumentation. OKHTTP is a robust library. It sort of provides a listener, a callback for all of these various events.
So, the events like such can be easily added there.
And this should be, like, opt-in, so we don't, produce a lot of events when they are not needed. And sometimes all of these events are not possible, a subset of these are possible. Whatever makes sense for that library can be added.
**Jason Plumb** 06:54 I meant to ask this on the last call, and I forgot. Do you think that you're going to try and take this one on?
To build it.
**Surbhi A** 07:04 I can do that, yes.
**Jason Plumb** 07:06 Okay.
**Surbhi A** 07:06 in the Java instrumentation, yeah, semantic conventions also I can do, yes?
**Jason Plumb** 07:12 Okay, cool, awesome.
**Surbhi A** 07:14 Should I mark it somehow?
Here, for audience, for everybody.
**Jason Plumb** 07:21 I can assign it to you if you want.
**Surbhi A** 07:23 Yeah, but I would need somebody to give me a go-ahead.
**Jason Plumb** 07:29 To start working on it?
**Surbhi A** 07:31 Y'all.
**Jason Plumb** 07:32 No, if I assign it to you, you're good to work on it. You're fine.
We love the help, yeah.
**Surbhi A** 07:38 But first, we should start with this one.
**Jason Plumb** 07:42 I mean, so… there's a little bit of a chicken and an egg thing that happens. If a semantic convention is somewhat, Controversial, or if people have questions about it, they often will ask you to point to an implementation, and if they can see both, then it makes a really strong case, and it also sets a precedent or an example for other implementations to look at.
So I think doing them in lockstep is totally fine.
**Surbhi A** 08:11 That makes sense, yeah.
**Jason Plumb** 08:13 Yeah.
And especially since it's opt-in, like, having these be opt-in, is great, because that doesn't impact… negatively impact or change any existing users, so…
**Surbhi A** 08:25 Yeah.
That would be awesome, yeah. I can then get started on this one.
**Jason Plumb** 08:32 Okay. Lookit, you're assigned.
**Surbhi A** 08:35 Awesome.
Yeah, and then I can take a dig at other libraries, too, slowly.
**Jason Plumb** 08:44 Cool. Yeah, when we talked about it last week in the JavaSig, I think there was… I think everyone's open to it. I didn't hear any pushback or negativity around it, so I think it's good to get started on.
**Surbhi A** 08:54 Awesome.
**Jason Plumb** 08:56 Yeah.
**Martin Kuba** 08:56 I have a couple questions on this, So do you… do you envision these to be, like, span events, or… be… Collect it as individual events, like log events.
**Surbhi A** 09:09 Currently, as span events, Oh… And later on, I do know there is a proposal, to deprecate span events in favor of standalone events.
But right now, directly as events in the span.
**Jason Plumb** 09:28 So you might get feedback or pushback on that if you don't implement it as separate spans, like log-based spans, because that means… that we'll have to change it in the future. If you build in now as spans, then you won't have to make changes in the future. So I would expect someone to bring that up.
Okay, why are you, why are you, why are you using the thing which we know is going away?
Right.
**Surbhi A** 09:54 Currently, can we correlate a… like, span.links is something we would use to relate it to other spans, but how do we relate events to span right now?
**Jason Plumb** 10:08 with span context, so span ID and trace ID.
That's the thing that… that's the thing that already exists.
So, if you're just doing logs, not even events, just any sort of logging, if those logs are happening in the context of a span, they can be correlated.
I can dig up.
convention if you want. Give me a second, I'll try and find it.
Unless someone else can beat me, too.
**Surbhi A** 10:41 I did link the events.md here as well.
**Jason Plumb** 10:49 It's probably not spec'd on events, it's probably spec'd on logs.
**Surbhi A** 10:54 Yum.
That makes sense.
**Martin Kuba** 11:07 Just one thing I would say from the browser perspective, I, like, there's… I think it's fine to have these events. I think in the browser, we will probably not send them individually.
We will probably have a single event.
That will send all these different, metrics, like, in one big event, because that's how the browser provides it.
Through, like, performance.
Observer, resource timing.
But I don't know, if it's… if it sounds like it's different in Android.
Makes sense. If it makes sense there, then…
**Jason Plumb** 11:51 So, the point about that, just to jump in, Servi, and answer for you like an idiot, the point that Serbi made last meeting was that, if you're bundling these together in one event, then you kind of lose the semantics behind the timestamp on the event.
Right? If… like, you're gonna have to have… All of these other, like, name attributes, like, you're gonna have, like.
foo start and foostop, and those all have to have timestamps, and if you're trying to bundle those all into one event, it may not actually be more efficient.
But it's just something to think about, like, data modeling-wise.
every log has a timestamp, and that timestamp only then will mean the time that you're sending it, I guess, or the time you've decided to finally put the stuff together.
So that's something to think about, Martin.
**Martin Kuba** 12:41 Yeah, I mean, like, the way in the browser that we get these, the times that are associated with those.
metrics, it's not like… I don't know, like, what this time would be, like, is it… is it, like, the… But it, like, in browser, like, it's, like, the… The time since the navigation starts, so it's relative to… The start of the session, essentially.
Also, I've seen… I've seen, like, some implementations not send. Not sent, actually.
The timestamps, and instead they just, like.
Calculate the duration from the start and end events, and just send that.
As a metric.
**Surbhi A** 13:32 Sometimes we do need to use Like, different sets of these.
like… I do have some explanation here.
I'm going to refer that. Let me open this one.
So, like, you can use the, like, these two to get total network transfer duration, like, you need the… Header part from the request, and the body and timestamp from the response.
So, exact timestamp for each of these events can be useful. These are not cross-referenced, but the… These sometimes need.
**Martin Kuba** 14:33 request.
**Surbhi A** 14:33 transmission duration.
Makes, makes sense.
Also, I wanted to ask, like, the proposal.
For having separate events, as opposed to span events. Do we think that we have a strong Oh… push towards that, like, Do we think it will materialize?
**Jason Plumb** 15:10 I apologize, Serby, can you repeat that?
**Surbhi A** 15:13 Like, right now we thought that there could be pushback on adding span events and later moving them to separate events, when now only we can create separate events.
And attach it to the span.
But that is in favor of span.events going away. Is this… like, I wanted to know if… We know that we have a strong majority towards this, and this is going to be the case.
**Jason Plumb** 15:47 I haven't been in the log sig too much in the last few months, but my understanding is yes. Martin, how about you?
**Martin Kuba** 15:55 Yeah, same for me, like, I can't say for sure.
I can only say, like, what I've heard that the direction is.
But the direction being that, like, over time, I think we want to move to… Log events, yeah.
**Jason Plumb** 16:11 But, Serbi, it also doesn't… like, I don't want to discourage you and say, don't do it this way, like, do it whatever way you want to, I just would not be surprised if you get that kind of feedback.
**Surbhi A** 16:21 Yeah, I'm just thinking.
**Jason Plumb** 16:23 Anyone… either one's fine, I mean…
**Surbhi A** 16:25 Yo.
Okay. There are no, like, there is no much event body, there is no much event attributes, and then back has to do extra logic of gathering all those spans and events and correlating them using the context.
And they'd be received at different times in the back end, not together.
**Jason Plumb** 16:52 Yeah.
**Surbhi A** 16:53 Like, the adding to the span itself is much… easier. It takes less resources, yeah.
**Jason Plumb** 17:02 And, like, there was talk in Java, at least, about bridging that API anyway, and probably in other languages, so the API, which is span.adEvent, that wouldn't necessarily change.
Or go away, because that's a stable API.
But the implementation of that, through configuration, can be set up, or will eventually be set up.
to allow that to be bridged to the logging API.
Or the, yeah, the logging API which supports events. So when you call span.adEvent, it's not tickling fields on the span model itself, it's creating new log events.
If that makes sense.
**Surbhi A** 17:41 Young.
**Jason Plumb** 17:42 I've linked… in the doc today, I've linked to the trace context fields that are part of the log.
Protobuff, the logged data model?
**Surbhi A** 17:53 Okay.
And there would be backward compatibility, so until the backend is ready, we can keep on using span.events and migrate to the other one via configuration when the backend allows. That makes sense, right? Yeah, I think that's the idea. Okay.
**Jason Plumb** 18:17 Well, you could also join the log sig and give them some grief, I guess.
**Surbhi A** 18:21 Yaw.
I'll try to do that, yes.
**Jason Plumb** 18:25 Cool.
**Surbhi A** 18:27 I did not know that we can today correlate this, this is good to know.
**Jason Plumb** 18:32 Yeah, and those are first-class fields, right? Those are not attributes. Those are, like, first-class fields on the log record.
**Surbhi A** 18:40 Okay.
That makes sense, yeah.
**Jason Plumb** 18:45 Oh yeah, cool.
**Surbhi A** 18:48 Okay, yeah, that's all from my side. Like, if you guys have any, comments, please do mention them in these tickets.
That's all, thank you so much.
I'm going to stop sharing.
Once I find the screen.
**Martin Kuba** 19:14 Grace, you have the next stop.
**Grace Lim** 19:19 Yep.
I can also share my screen.
If I can find the right one, I think there's just… Okay, so I have… A good discussion in the Android.
SIG, but just wanted to run it across to folks at the Client SIG as well. So, basically, I am proposing a couple span definitions for apps.
And specifically, that is, like, a span for AppLunch, and I think that's pretty straightforward. The ones I wanted to discuss were specific toward, like, the screen.
And so, right now, I'm proposing three, like, the first one being time to first appear, which is, like, the time until the, application screen rendered, whether that's, like, time to first draw, in terms of, like, Android, or time to first appear in terms of iOS. And then the two other ones are screen load and, screen visible. So.
for context, like, I did start a discussion in Slack, and kind of the consensus was we want at least one, like, generic, from agnostic span definition for screen loads.
And then we can have, like, these specific, like, screen lifecycle events that are, more defined, catered toward, like, the individual platforms, whether that's Android or iOS. And so this one may not capture all the details for a screen load. So, for example, in iOS, there's, like, you know, view will appear, view did appear, view will disappear. So it doesn't capture all of that, but I wanted to start at least the discussion for, like, what a screen load definition should be for mobile applications, and then go from there. Yeah, so… to start… I think the more interesting one is, like, the screen load definition, and so I wanted to call out that this is, like, different from time to first appear, because just because a UI component may have loaded, it doesn't… or, like, it was drawn, like, the first frame was drawn, doesn't necessarily mean that, you know, as an app developer, I would consider the screen, like, full, loaded.
So, my proposal here is the time from when, you know, the, navigation of the screen started to, like, when the main thread is ready to handle user input.
So yeah, let me pause there for questions.
**Jason Plumb** 22:00 I think it may be true on some platforms that it's hard to get all of these values, and that it's… or to differentiate or discriminate between loaded and visible on some platforms is probably difficult.
**VP Valentin Pertuisot** 22:13 I have one question related to the first happier timing.
Is it… Related to a view, or is it really, like, first frame on the screen that is… Like, display to the customer, to the user.
**Grace Lim** 22:30 So, the second, this one… Yeah. The first one, this is the time to render for the screen. So, mostly it's, like, time to first frame being drawn. And for Apple, like, for iOS applications.
Like, tracking each frame.
is a lot, but they have an API where they kind of expose, like, time to first appear. Like, what is the definition of time to first appear that Apple defined? I'm not quite sure, but given that they do provide that… like, lifecycle event, kind of, I was thinking, like, for iOS applications, at least, we could, like, that value could be used for time to first appear.
Yeah, so first we know, like.
I didn't want to call, like, define this as, like, fully loaded, because technically, you don't know when a screen has, like, fully loaded, right? Whether there's, like, data being loaded asynchronously, or something else going on. So I wanted to… find a middle ground that, you know, for each platform, going off of the assumption that this is technically feasible. Like, you could find when the main thread is able to take user input, and it's no longer busy, like, trying to render and, like, do all the other stuff for a screen, though. So that's kind of where I landed in the middle, because Else it would… it would require… the developer, like, defining the end of a screen node, and at that point, it's a lot of work, and it becomes brittle really quick. So I wanted to create, kind of like.
a proposal. It might not be, like, a perfect definition, but at least to, you know, get the ball rolling on, like, some… like, to define that arbitrary endpoint, at least, For platform… for mobile applications.
I don't… I don't know if the silence means… I have concerns, or, it looks okay for now, let's see how it goes.
**Martin Kuba** 24:45 So I'm not saying anything, because I honestly don't have enough… And I've come, like, experience myself with mobile, So I'm hoping others… others do.
**Grace Lim** 24:58 Well, actually, while you're here, then, I think I heard you mention you're more familiar with, like, the browser telemetry. So, like, even for browsers, though, like, I have yet to look at the semantic conventions for browsers, if it has been defined, but how are, like, page loads being defined? Because… For example, like, single-page applications, after the initial page load, when there's a route change, like, how are we planning on defining, like, when that page load is done?
**Martin Kuba** 25:30 Yeah, I mean, that's… I think we're trying to figure that out right now, actually. So there's… there's a… there's an… we have an existing instrumentation that's been around for a long time that generates a span.
per page load.
But, you know, it's… it's essentially, like, the end of the, of that is when this specific event, like the… Historically, like, page load.
load event, fires, but… but there are a number of different, also… Oh.
Timings that are interesting, like, the paint-paint metrics, for example, or, like, interactivity metrics, and… We're actually capturing them as events rather than spans.
And I'm not sure that, like, it makes sense to continue to rely on the span during low time.
But, like, we've been kind of focusing more on events.
As far as, spa applications, like, we don't really have any instrumentation or semantic conventions right now for that, and it's not even, like, standardized in the industry. Like, there's… So, you know, I think it's… most, most of the, most of the things that I've seen are, like, in, like, instrumenting, Like, framework routers.
But yeah, we don't… to answer your question, like, we currently do not have any semantic connections for that.
**Grace Lim** 27:00 I see.
**Martin Kuba** 27:02 There's a… there are… I mean, there are… I think there are a lot of different opinions on that. I think for You know, there's a one… you know, I think the basic thought would be you could have, like, a page view event, which could be used for both hard page load and soft navigation.
But it's… But it's… the question is… You know, like, what actually does qualify for… for it to be, like, how to actually capture it, like, what's the… Duration for soft navigation.
And, like, what's the duration for even hard navigation? Because… because, like I said, there are, like, a number of different events that happen.
So…
**Grace Lim** 27:42 Gotcha. Yeah, I'm kind of concerned, because, like, for mobile, too, like.
what constitutes the end of a screen load? I think that is also arbitrary.
Okay, like, also, like, for… Single-page applications to kind of a brute.
forced way, I think, that we have done it when we did this way back when, was just to… Like, find the last synchronous network request, and then do some, like, calculation based off that to get that arbitrary endpoint.
Okay, yeah, I'll keep my eye out, then, on kind of how the conversation goes for BrowserSig.
Yeah, but are there any concerns with, like, the screen node definition proposal?
Oh, Valentina, I don't know if you unmuted because you wanted to say something, or…
**VP Valentin Pertuisot** 28:41 Yeah, myself, I unmuted because I had, Question related to the start, client time.
From user initiation, the first point. And I wanted to know… to understand exactly when you… when is it stopping, actually.
Like, because you said the app is ready for interaction, but does it mean it's, like, the first view that is ready for interaction, or is it… Like, is it arbitrary by the… Implementation, or…
**Grace Lim** 29:12 No, that's a really good question. So… to give context, like, I think for Android, we use the… Like, activity life cycles to determine this.
I may be wrong, but, like, this seems pretty already, like, defined in the Otela SDKs.
Sorry, I'm on call this week. But then also for, at least iOS, We were thinking of using the, metrics or, like, telemetry, provided by MetricKit. And so.
I guess my answer to your question is not very clear right now. I was gonna kind of play by ear to see what is provided by the frameworks, but yeah, I can… I can work on the definition for this.
**Martin Kuba** 30:05 So, I just want to also, like, really quickly, like, we're out of time.
We can continue this discussion.
In the next meeting, but also, like, if you wanna… if you need, like, immediate, like, sooner, feedback sooner, we can… I'll have this discussion in Slack as well.
**Grace Lim** 30:22 Yeah, yeah, I can definitely, update the thread I have, and add this PR, and continue there.
**Martin Kuba** 30:28 Great.
**Jason Plumb** 30:30 It's a good start, it's great. Yeah, thank you.
**Grace Lim** 30:33 Alrighty. Take care, everyone.
**Surbhi A** 30:35 Thank you.
**Grace Lim** 30:38 Thank you, bye.
