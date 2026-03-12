SIG: Client Instrumentation SIG
Date: 2026-03-03
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Santosh** 01:04 Hello.
**Martin Kuba** 01:08 Hey, Santosh.
**Santosh** 01:12 Yeah, I put your item on the top, because I think we didn't get to it last week.
**Hanson** 01:21 Hey, everyone.
**Martin Kuba** 01:24 Bye, Henson.
**Santosh** 01:58 Okay, we can start, I guess.
**Martin Kuba** 02:05 Okay.
Should we get started?
So I have, yeah, there's, My first topic is from last week, but I also have one other thing that I wanted to ask this group, that's probably related, But let's start with the API. So, like, my… I think my question… In the browsers, SIG, we're trying to figure out right now how to structure our SDK and our packages.
And the Android SIG has gone through this, I know, before, so… and I know that you have… you know, structured your package a certain way, and you have a separate API. So, like, I see that you decided, you made a decision to introduce Around the specific API.
My question was, like, what were, like, some of the reasons, or some of the… kind of thinking through this?
the reasoning, how you came to the conclusion that you needed a specific API.
Is it… is that API… and is the API intended… To replace, like, the… kind of more, like, the higher-level APIs, the instrumentations, Talk to?
Or is it more just for, like, the user application to use?
like, why… so, like, for example, I know that you have, like, emit event, right, in that API. Why would some… why is… why do you think you needed that, as opposed to the user application just, like, calling, like, logs, emitLog.
Yeah.
experience, like…
**Jason Plumb** 03:59 Yeah, I mean, first of all, I do want to call out that, half the people on this call are in the Portland area, which is awesome, and if you include Hanson, Pacific Northwest, hell yeah.
And Santosh, are you in Seattle? Where… no, you're on the East Coast.
**Santosh** 04:14 No, I mean, no, no, no, I'm in the… in the Bay Area, San Francisco.
**Jason Plumb** 04:17 The Bay Area, okay, okay. So I think that our reasoning was, I think there's a little bit of history as to why we wanted a RUM API. It was very much a product, kind of, driven decision. It was like we had application developers using our RUM APIs before it was donated, and that was sort of iterative, and we wanted ways to expose things to application developers that they could surface in the UI.
As far as, emit event goes, it's because OpenTelemetry's stubborn and refuse to have a first-class event API, even though they should have.
That's really a workaround. But also, I mean, RUM developers, like, sorry, mobile developers, think in terms of events, right? They're like, a thing happened, I want to admit an event. So, it seems like a natural fit to me. Like, that's… I think it's really that simple.
And we also wanted an extension point for future APIs, you know? Like, I think we also… it's not direct, but we also expose session. Like, we know that people think about and care about the session, and there's certain application space behaviors that might want to cause the session to reset, like logging out of your bank or whatever. Like, there's… there's different reasons why we want to expose RUM-level concerns up to the application. That was the main thing. And it's really application-facing and not instrumentation-facing.
**Martin Kuba** 05:45 Okay.
**Hanson** 05:45 Yeah, there's also… it is not quite there, but there… the fact that there is an API means that there's, I think, 3 large groups of things that we could do. One is, as Jason mentioned, about, Well, actually, no, you didn't directly mention this, but, an easier way to initialize the SDK, so it's almost syntactic sugar for easy configuration. Another is, you know.
a set of, things that… I mean, we say that instrumentation can't depend on it, but, like, things like session, and things that… that basically exposes, the state of the SDK and the platform in an agnostic way.
could potentially also go in this client API, get session ID, reset session, whatever it is. And then the third one, which is, I think, where the event thing comes in, which is almost like a… something around the instrumentation part. So I would say all those three things could be considered Separate.
groups of API that can be exposed, and depend on what you're looking at in the JavaScript space, in terms of, like, which of the three that you want to do.
it may be a fourth thing, like, I don't know. But it's probably better to conceptualize or rather, break down a client API into different categories, because when it's an API, people immediately think instrumentation. And most of this, it's not really instrumentation, it's everything around it, so…
**Martin Kuba** 07:31 That makes sense. Yeah, I think… I think right now, we basically… would not have anything special, or don't have anything special in browser, so, like, the user application would have to talk to the, like, the higher level APIs, plus, like, sessions is, like, a… Extra layer on top of it that… You're right, like, I… we have kind of considered… That that's something that you, That you, initialize, like, in one place in your application, but, like, if you needed to access session in different places in your application, then obviously you would need to pass it around somehow.
But… .
**Hanson** 08:14 basically, instrumentation, it's useful for instrumentation to have access to some shared logic, that is not purely just the hotel, you know, API. And anything that kind of falls under that umbrella could be considered, like, a, you know, client instrumentation, or end-user-facing instrumentation API, or…
**Jason Plumb** 08:34 Yeah, and you can imagine… you can imagine an instrumentation, like, you don't have to be too creative to imagine an instrumentation that, like, would also want to mess with the session. Like, oh, I only emit this event once per session, or, you know, I'm an instrumentation that detects this scenario, and I do it, you know, every one minute while the session's active, or, you know, like, whatever, and then… You can imagine it having RUM-level concerns, too. I linked to the OpenTelemetry Rum API.
**Martin Kuba** 09:02 Yeah, yeah, yeah.
I've seen it, yeah.
Yeah, I guess I… Do wonder, like, if we, if there's something, like, we should… Kind of, align on, or if… Or if it's okay to have our own APIs.
Based on, like, the… environment, but…
**Hanson** 09:25 I think it might just be easier… go ahead.
**Martin Kuba** 09:27 Yeah.
**Jason Plumb** 09:28 I mean, we should do things like getting alignment on the session first, like, and session probably being a first-class.
**Martin Kuba** 09:36 part of this API that we're talking about, and so…
**Jason Plumb** 09:40 It's hard to align on the whole thing if you can't align on the parts first.
**Martin Kuba** 09:44 Sure.
**Jason Plumb** 09:45 I think there's room for it, I just think it's a lot of work, and no one's really spearheading that.
**Hanson** 09:49 if you search Session API in this document, you can probably find, you know, some of us talking about it a year and a half ago. But it's further down. I believe, Martin, you wrote a big doc about that as well, and implementation?
**Martin Kuba** 10:02 Probably, like, 4 years ago.
**Hanson** 10:05 I think… I think for sake of speed, you might just want to do it yourself, and then I think we could see where things align, like, when you're done. Because, you know, right now, if Android or iOS, they don't have capacity to actually go and spec it out and implement it, then it's all theory, and I… don't want to block you based on my theoretical concerns. You might as well go and implement it, you see what it's like, and then, as long as we don't declare it stable, we could… we could have, you know, a chance to change it.
And if it starts off with, you know, unstable APIs, that session, they kind of do the same thing on different platforms, and then we say, hey, we… they're functional, let's merge them somehow. Like, I don't think they're going to be doing two radically different things. It's probably get the API, or get the session, reset, because session is done, or like… Because we already fire events, right? So if, if, if… we have the ability to, like, you know, have a programmatic way of listening, rather than, like, looking around and spying the, the pipeline, which we shouldn't do anyway, then there you go, there's an API.
**Martin Kuba** 11:12 Okay, yeah, I was… That's… that's fine. That sounds good. I… I think I was more just, like, trying to… Can I get a… like… opinion in my head, like, whether we should be introducing API now, or if it's just a convenience that we can always add on later. You know, so I was curious, like, if maybe, like, part of the reasoning was you were kind of thinking ahead of… and… In terms of, like, if… if, like… separation of API and SDK. Like, if, like, you know, the application uses your API, but then you can swap out the SDK behind the scenes, or… what if it's basically just convenience? So… yeah.
**Hanson** 11:51 I want that, because I want a common… I'm talking about a common client API for the Embrace SDK and the OTEL Android agent to do stuff like session management and things like that, but, you know, it's just… If I had 3 of me, it'd be done, but I don't have 3 of me.
**Martin Kuba** 12:12 Okay, cool. The other thing that I wanted to just bring up, it's actually related to the next topic that Santosh has on the agenda.
And that's, that's metrics. And, specifically, like, What we have been talking about Or revisiting again is, Modeling sessions as resource… as resources?
As, like, more like as entities, actually. Modeling sessions as entities.
And part of that, like, we've been… Trying to figure out, you know, how that would affect, things.
In the browser SDK and instrumentations, and there's… I don't know if you've seen, but the entity SIG has had a proposal for, Basically, updating the API to, To get providers that are… bound to a specific entity, so, like, you… you initialize your SDK, with certain resources, but then later on, like, if you… if you have, like, a new entity that shows up, you can… Can I create, like, a child… Child provider, that's bought… that has the additional attributes of that.
entity. That said, like, it doesn't… really work for our use case, because… Because, like, we need the ability to update entities during the life of the SDK, and, like, and have that… and, like, something like session is global, like, that doesn't… you can't just, like, scope it, like.
part of your… part of your, just, like, one instrumentation, for example, like, you want to apply it to… Like, to everything.
So, in… I wasn't part of the discussion yesterday in the NTT SICK, I wasn't there, but… but they were basically… part of the thing they were saying is… is that… We're kind of trying to solve two different things, like we have in our client applications, like, we have this… This use case of, we want to model certain things as entities.
But, like… but, like, and then there's, like, a different problem for the metrics SDK, like, which is, like, if you update the resources, then… then it, like, it has… Like, challenges in the, in the, in the metrics, metrics SDK, because of, You know, additional… Additional attributes, like to, So, the… so the outcome of that was basically that… sounds like in our client applications, like, we should not have metrics SDK, ever.
And I know that, Jason, you brought it up last week, that maybe, like, you were changing your mind on this.
Santos, you have this, topic here that's related to… so I wanted to add that little bit additional context to that, too.
I know I said a lot, sorry, like, if you have questions.
**Jason Plumb** 15:24 People keep asking for it, is, like, where I'm coming from. I hadn't considered… so does, resource… Changes to the resource, like entities that change the resource, does that impact… aggregation.
Because of metric identity?
**Martin Kuba** 15:41 That's my understanding, yeah.
**Jason Plumb** 15:42 Yeah, that's not even a… that's not even something I considered before.
**Martin Kuba** 15:46 Yeah.
**Jason Plumb** 15:46 But yeah, that definitely… Screws things up.
**Hanson** 15:51 I mean, it doesn't screw things up any more than it's already screwed up. It's almost like… it's already not super working, and you add another high cardinality dimension, even higher cardinality, or… no? Same? Anyway, yeah, you're pissing at… I don't know. I'm not gonna use the metaphors with long piss. But, I think, you know, back to the Santoshes topic specifically, if we're talking about recommending, writing something down for metrics for user-facing apps, we should do that, and I think the session stuff, whether it comes in via an… well, I mean, if we wanted to have it come in via an entity, it'll just introduce another wrinkle, to this, which, Yeah, it always doesn't solve it, or doesn't support it well. Adding that it won't solve it either, unless someone's willing to go and change hotel metrics, at the core, so…
**Jason Plumb** 16:55 this is…
**Hanson** 16:56 What I think is weird about this topic is that it's often being pushed by users, it's often being asked for by users.
**Jason Plumb** 17:02 And I'm not hearing any vendors Come and say, oh, we love metrics on mobile, like, we want to really do this, and, like.
I haven't ever heard that happen.
In fact, I think for most vendors, it's kind of a problem.
But users have this expectation, so I don't know. It suggests that maybe there's an opportunity to do some… some bridging, or, you know, put, like, a metrics-like facade in front of another signal, or… I don't know, but… Yeah.
Yeah.
**Santosh** 17:32 Yeah, in fact, I think the conclusion, or rather one of the, you know, suggestions to consider from Martin last week, last time we spoke, was given that there is this panmetrix processor, in the collector.
Is there some convention we could come up with?
When creating these, events for the metrics scenarios. You know, that could, you know, readily, you know, transform into their metrics equivalent, You know, that way we can establish that as a… as a… as some sort of a convention that, hey, yes, you are creating metrics, but, you know, because of all these reasons.
We recommend creating these events in this form, but, you know, they will eventually get converted into, you know, metrics. And therefore, given that it's now part of a client-side Instrumentation standard.
You know, everybody could follow that convention, and then, you know, all of us would get You know, consistent metrics on the back end.
**Hanson** 18:45 So, I posted a link to a discussion in the OTEL Android, I guess, channel, so not everybody's following that, but somebody who's using the Java SDK and not the Android SDK, funny enough.
It's already doing something similar, basically, at the collector side. They take logs and spans and turn those into metrics. And then they're able to basically handle the cardinality, persistence, all that stuff on their own.
So, basically, you do what you do, on mobile or on user-facing apps, and you create logs and spans, and then that gets converted into the metrics. I think I think the confusion really is about you can actually get metrics without using OTL metrics, but OTel Metrics also offers a very nice API to do metrics.
But it's just the constraints that you're… that you have when you use this API. And I think the disconnect is, what if we could use that API and not have to deal with those constraints? And that could be done in a number of ways. You could… I'll probably do it in the SDK to do the conversion and all that fun stuff.
basically, every time you log a measurement, you log an event, or… So, there are, like, different ways of solving this problem, and I think having something that, you know, we talked about two weeks ago, writing it down and say.
this is the perspective of end-user-facing apps, and how we should deal with metrics, and define what metrics actually mean. Hotel metrics with, like, lowercase m metrics, ways of working around to use OTEL metrics and ways of working around to get lowercase metrics with other OTEL signals, and perhaps a future path where those could be merged. So… I think Santosh, one of us, we're gonna look at this. It's maybe probably one of us that has free time first. Yeah.
**Santosh** 20:45 One, I want to ask one additional question, In terms of the requirements, here, is… Is it always the case that the client instrumentation Scenarios always represent one user.
Or is there a scenario where they could represent, you know, multiple users? So, the one in that GitHub issue.
Somebody mentioned a scenario where we're talking about, of, you know, some IoT gateway, let's say.
That is out on the internet at some client-side location.
And that is actually representing multiple clients that are connected to it.
And in that case, it feels like… You know, it is not, like, a single event we're talking about, it is really an aggregate metric.
But aggregate to that.
you know, those bunch of clients. I don't…
**Jason Plumb** 21:50 I don't understand the question. I mean, a session is for one user.
**Hanson** 21:57 But if we forget about sessions right now, and just say there are these metrics-producing things that are running on what we consider end-user-facing apps, whether it makes sense to fully aggregate those, the answer is yes.
**Jason Plumb** 22:12 Okay.
**Hanson** 22:13 The answer is yes, but what data will you get if you basically… disambiguate, or you anonymize the source. Like, if you can guarantee that they all run the same, and they all basically represent each other, then aggregating all that is great.
But if they have variability in terms of, client state, app state, memory, all that stuff, then you're gonna get… you're basically smudging together things that are very different and getting a flat number. So there are…
**Jason Plumb** 22:45 just to support your point, like, I think most users could benefit from having a global crash counter. How many crashes did your app have yesterday? How many crashes did it have today? You may not know that 99% of those crashes come from one crappy type of device.
Right? You might be losing that, but, or, like, 99% of your crashes are coming from, like, Nebraska. Like, you're not getting all of that insight anymore, but it's still valuable, right? Like, that counter, the count of crashes is still useful.
Now, whether that's a hotel metric or you're counting events on the back end, That's where it gets interesting.
**Santosh** 23:26 Yeah, and in that case, can we still… Fit that requirement into this… Proposal that we're talking about, where… Even that, if represented as an event, can be, you know, eventually translated back into metric.
**Hanson** 23:46 I think the… oh, Lad, do you want to say something?
**Ladd Van Tol** 23:49 Yeah, I was a little curious, I haven't tracked this conversation in a few months, but, the… the thing that stuck with me a little bit about pushing towards Trace Demetrix as a recommendation Is, you know, we'll typically have sampling.
And, you know, everybody who looks at this for our use cases is like, well, we need… we need metrics to capture everything as best as we can, and if we're pre-sampling at 1%, Or, you know, requiring a very, chatty signal and sampling 100%, like, all of a sudden we break One of the core requirements of client-side instrumentation, which is not to consume a ton of bandwidth.
So I'm curious, you know, has that been covered by prior discussion, or is that just an open problem at this point?
**Jason Plumb** 24:50 I think we've touched on it. I tend to… I think it's part of why I'm relaxing on this topic a little bit, because I think client instrumentation, if it were to create these high cardinality metrics, they can still be distilled down in a backend pipeline to the minimal set of dimensions that users or teams care about, right? So, if you want to throw out session, for example, as a dimension, and maybe almost everyone wants to do that because it's too stupidly high cardinality, then you do that, but you do it in the back end, right? And you still have actual open telemetry metrics that are being aggregated client-side and emitted, you know, every minute, or however you… however often.
But then… The counting, the aggregation, or whatever is still done in the device, or in the app, and not… Not in the collector and not on the back end.
**Ladd Van Tol** 25:47 But it seems like, then, if we say, use Metrics API or something similar on the client side, then you're still missing a sort of fuzzy time re-aggregation pipeline, right? I haven't seen that, at least in public work, when I've looked for it, there's not really.
**Jason Plumb** 26:06 What do you mean by that?
I'm not following… what do you mean?
**Ladd Van Tol** 26:09 So you have to re-aggregate at some point in the pipeline, right?
**Jason Plumb** 26:14 Yeah.
**Ladd Van Tol** 26:14 bye.
by my reading, you know, all of the metric specs talks about timestamps, right? That… will not precisely match, right? So all of a sudden, you have to do sort of this fuzzy aggregator that says, this is close enough to this one-minute bucket, throw it in there.
Or am I misunderstanding?
**Jason Plumb** 26:38 No, I think… but I think that's fine. I'm not sure that that's as challenging as maybe you're making it seem, because I think you just throw it into buckets.
**Ladd Van Tol** 26:45 Yeah, I don't think it's a hard computer science problem, I just don't think it… I don't think it exists, as, like, a piece of existing open source.
**Jason Plumb** 26:56 I don't think it does.
I mean, like, maybe Prometheus or something can, you know, has that, but, like, whatever.
**Hanson** 27:03 So there's probably, like, two issues here. One is, we've been told that, sending, high cardinality metrics… so on the client, you could… doesn't matter how high the cardinality is.
it's fine. It could send it out no problem. It's the collector's side that something will blow up, is what we've been told, or things will not work correctly, or you do something…
**Jason Plumb** 27:26 Database will have a problem with it.
**Hanson** 27:28 Exactly. So, if there's a way of, like, putting something in front of that and basically kind of, you know, merging stuff together and throwing it in, that would work. Dropping cardinality, that would work.
whatever. That's fine. On the client side, if there were things that are, happening in such high volumes, like frame drops or, data usage, where you have measurements that are coming in, like, multiple times a second, then that API is very, very attractive. Versus, like, if we're talking about crashes or app startup, then… having that as an event not only allows us to produce metrics on the top… on the server side, but also gives you specifically a timestamp of when that happened, which metrics does it really give you, unless you use exemplars, and if everything's exemplar, then it's not an exemplar, I don't think that handles that. So it's almost like there… is a use case for the high velocity metrics.
But how do we get that, back to the… to the server so that they could… process it, and what kind of use cases would there be, where, we wouldn't just use, a span or a log? I think… I've also warmed up to the idea of just supporting it.
go ahead and shoot yourself in the foot, if that's what you want to do, which is why I think the recommendation on… this is probably how you should use it, but if you want to still use it, you can still go ahead and use it, is likely the best route of doing, you know, at least in terms of the project, of the direction that we'll go.
My opinion, at least.
**Martin Kuba** 29:11 Yeah, Hansen, so I think I was gonna, like, I think you answered my question. I was gonna say, like, for things, for certain… it seems to me, like, for most things, like, what is the advantage of sending metrics?
Like, it seems like it would only be… advantageous for, like, the use case, like you were saying, like, for the, like, something that happens very fast, like, in the client, and, like, you want to… you don't want to send as, like, too many events at once, right?
But I… so, like, if we… if you introduce the… if we, like, allow for… metrics to be sent from the client, then, like, it sounds to me like we have to be very… Specific that… that, like.
you have to use some kind of re-aggregation, or… on the backend. Otherwise, like, you end up, you know, in a… in a… situation that, like, we did not, like, we do not recommend, right? So… Yeah. Whoa.
**Hanson** 30:06 Cool.
How does she do that?
**Jason Plumb** 30:09 Yeah, I know.
**Martin Kuba** 30:15 Yeah, okay, well.
**Jason Plumb** 30:17 This meeting goes by fast, we didn't get to all the topics.
**Santosh** 30:20 Yeah. Just to get a… like, a count of, how many folks want versus do not want. Jason, are you the only one who still feel… We should retain, you know, metrics.
Usage on the client side, or are there more folks?
**Hanson** 30:39 I… so I feel like we should allow the usage of it, but in the documentation, very specifically dis-recommend and basically say only use hotel metrics currently under these circumstances, and with these safeguards in place. Because if you use it naively, your backend's gonna complain at you. And… but if you want to just… count things that are small numbers, you don't need to use metrics to do that. You could use it, you could use logs, you could use… sorry, you can use events, you could use spans. So it's… it's… it's… yes, you can do it, but you shouldn't do it.
Then you should do it this other way.
That's…
**Martin Kuba** 31:13 that.
**Hanson** 31:14 We're at.
**Santosh** 31:15 But what is recommendation to the instrumentation authors, though?
Like, in the hotel.
**Hanson** 31:20 stock instrumentations that we are building.
**Santosh** 31:24 I think there should be some… You know…
**Jason Plumb** 31:28 I think we don't have consensus. I don't think we have a consensus yet.
**Santosh** 31:32 Okay, okay, we can… okay, we can continue.
**Hanson** 31:34 We could definitely recommend that to be deployed on an end-user-facing app, be prepared for high cardinality.
**Jason Plumb** 31:39 Yeah.
**Hanson** 31:40 Especially if you enable it, then your backend must handle it. Like, that is… that is a recommendation that… We have to do.
**Martin Kuba** 31:50 Or maybe, like, is there maybe, like, an opportunity for us, like, to… to think about, like, a client-specific API for metrics?
**Santosh** 31:59 Yeah, I think we… let's talk… Let's spend some time on that topic next time, and then see if it leads us anywhere.
I looked at the span metrics processor, I don't think it is… it is a generic processor. The metrics it creates are, like, well known in advance.
But, like, I have seen systems in my prior organization where you could actually define rules based on the incoming spans and logs, how you can create metrics. So I don't think this span processor takes rules.
I could be wrong, I have not looked into it in detail, but… but even going beyond rules, where if you could define conventions, or hey, if you name your event name in such and so… such and… So, convention, and include this additional attribute to indicate that, hey, yes, this needs to be translated into a metric, then this processor automatically creates a metric for you.
Something like that. My…
**Hanson** 32:57 My gut says the solution here is something on the server side that handles, high cardinality OTOMetrics better, and also server-side component that converts logs and, logs and spans into something that is metrics-like, perhaps with some conventions, for us to annotate spans and logs.
**Santosh** 33:17 Yeah, yeah, yeah. Yeah, I think the collector is not… in my knowledge, it's not used in the client environments. The collector processor, we are talking only to… to illustrate the point that, hey, such a thing could be built, and here is a, here is a, like, a proof of concept.
You know, in the collector. But in reality, you know, people need to build equivalent stuff on their server backends.
**Hanson** 33:46 Let's take this up in two weeks.
**Santosh** 33:48 Okay.
**Hanson** 33:48 Or, or we can switch to Slack, which is what I'm gonna do, pointing everybody to the client, or the crash semantic convention. If you want to take a look at the… there's no updates for a couple weeks, so I hope people look at it, so.
**Jason Plumb** 34:05 Cool.
Awesome. I'm outta here.
**Martin Kuba** 34:08 See y'all later.
**Hanson** 34:09 Bye.
