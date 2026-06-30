SIG: Semantic Convention SIG
Date: 2026-06-29
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:10 Hello! Hi! Everyone!
Surbhi Agarwal 00:04:21 Hello.
Liudmila Molkova 00:05:50 So maybe let's get started. I think several other Maintainers were going to join, so it will start… Was it triage session?
Yeah, okay.
Can you see my screen?
Surbhi Agarwal 00:06:33 Yes, we can.
Liudmila Molkova 00:06:36 Awesome.
Okay, so we have just one topic on the agenda. Please add any topics that you'd like to discuss. Please add your name to the attendees list, and Let's take a look at the PR triage board.
There are a couple that need more approval.
Rudiger, do we… plan to work on this Pure? Should we get it merged, or you'd rather federate?
Ruediger Schulze (IBM) 00:07:09 Actually, now that we have the mainframes semantic conventions, I will move this over. We're just setting up the repo, and that should actually then find its home over there in the mainframe semantic conventions repo.
Liudmila Molkova 00:07:25 Awesome. Did you do the federation already?
Ruediger Schulze (IBM) 00:07:29 I'm just working on it. Getting closer, getting closer.
Okay.
Liudmila Molkova 00:07:36 If you see any rough edges, let us know.
Ruediger Schulze (IBM) 00:07:39 Yeah, definitely. So I played around with the Gen. AI repository. I think I understand the process now, and now need to to repeat it on.
On the one for the mainframe.
Liudmila Molkova 00:07:53 Yeah, maybe you don't.
Need to repeat everything because there are some hugs there that you don't need.
Maybe let's add it to the agenda and let's chat about it.
Ruediger Schulze (IBM) 00:08:05 Okay.
Liudmila Molkova 00:08:14 Okay, so, this one will move over CI to use CISPAL.
Joshua approved… A bunch of… I think there is some link that we have.
Yes, that needs help.
Then it's fixing, but that's unrelated.
It's just a different tool… Oh, okay.
Cool, I'll take a look. There are a couple of things that are blocked.
Okay, this, Serbi, you had a, you have it on the agenda, awesome.
Launch pass to replace executable path.
There's a discussion and I would expect.
A review from… Process seek. There were some blocking reviews in the past.
Do we have anyone with the context on this one?
Okay, then I'm going to… Move it.
to a waiting Coordinator's approval.
And let's take a quick look at dentriaged, some tooling things… This one, we couldn't… it's draft, we couldn't agree on the direction.
Github release for Viva version.
Okay, this is, something for… System seek to review.
And those are a bunch of tooling PRs if anybody is interested.
Okay, so this is switching from.
Docker to… GitHub releases.
Any concerns with this, Josh? I think you added the Docker in the beginning.
Josh Suereth 00:11:03 No, it's well, are we actually publishing to.
Weaver, or sorry. I I do have a concern with this.
it might not be available in Docker when it's available in GitHub releases. Like, we're not publishing Docker there.
Did we move to not use the Docker image at all in our build? Because if we didn't, then we don't do this.
Like, what… the reason we would use GitHub releases is if we actually are publishing to GitHub, right? This is about getting the version number.
Liudmila Molkova 00:11:37 Yeah. Okay.
Josh Suereth 00:11:38 Yeah, so, like, the publishing to Docker and the publishing to GitHub releases are actually independent for Weaver.
Which is an unfortunate reality. It'd be nice if we had them all the same, but we haven't figured out how to resolve our process. So, I would not be a fan of this, because it means we're gonna take… version numbers that might not be available in case the build is borked, which does happen. In fact, yeah, well, anyway, we can get into details of that, but basically, it's not guaranteed that one succeeds when the other does.
Liudmila Molkova 00:12:29 we cool.
So then, moving on to the agenda.
So B, let's talk about the network timing semantic conventions. Do you want to present? Do you want me to present?
Surbhi Agarwal 00:12:42 I can share my screen.
Sharing my screen now, can you guys see my screen?
Liudmila Molkova 00:12:50 Yep.
Surbhi Agarwal 00:12:52 Awesome. So, were you able to… I went through your comment, Ludmila, thank you for putting a comment asynchronously, it was very helpful to understand what was, the Semantic Convention group's idea about it, and I had posted a comment on top of that. Were you able to take a look at that? Basically, it mentions how like, we think that SPAN doesn't work here, and why events work here.
Liudmila Molkova 00:13:24 I'm sorry, I didn't see the comment. Can you walk me through?
Surbhi Agarwal 00:13:27 Yes.
So, basically, the option 1 that you mentioned was putting the timing attributes on the original HTTP span itself.
So… with that, there is a semantic convention conflict. What that is, is that the semantic convention today mentions that HTTP client spans should start sometime before the first request byte is sent.
This may or may not include the connection time. This in particular is important here. HTTP client spans should end sometime after the HTTP response headers are fully read, or when they fail to be read. This may or may not include the reading the response body.
Right? Because reading response bodies asynchronous and there is a probability of a span getting leaked if we were to wait for reading the response body. Here is goes on to further. Yeah, yeah, yeah.
Liudmila Molkova 00:14:28 that… The question to you is, why event wooden brick?
You would have… the only reason this, the thing is there is because it's impossible to collect the span.
And therefore, it's impossible to guarantee the collection of event either. And if we have the same limitations between the span and event.
It's not, like, a reason to have two different things.
Surbhi Agarwal 00:14:56 Event is a separate event that contains the context of the original HTTP span.
And that can… that is a complementary signal, the original spam.
Liudmila Molkova 00:15:08 No, no, no, the question is.
Surbhi Agarwal 00:15:11 I understand, okay.
Liudmila Molkova 00:15:12 But do you know when to emit event? How do you know when to emit event?
Surbhi Agarwal 00:15:17 Yeah, yeah. So, my… my perspective is… Even if the event is lost, that's a new signal that we are adding, and there are ways we can ensure that it eventually gets To the backend, but we shouldn't affect the existing behavior and the existing…
Liudmila Molkova 00:15:37 Wait, the timing will be completely off, so if you're… well, first, you cannot guarantee, because with garbage collection, you don't know if it will ever run, or that it will be, like, the finalizer will be actually called.
So you you cannot guarantee it will be sent, and the timing will be completely off. It does not make sense.
Surbhi Agarwal 00:15:59 is not a problem here, right? If we affect the span, that's a problem, but a new.
Liudmila Molkova 00:16:05 No, I'm saying that the event, the delta you're suggesting to collect.
is unreliable and infeasible to collect. And if it was feasible, we could have collected it on span.
Surbhi Agarwal 00:16:20 The thing is, here we can implement some strategies to send the event and ensure that it is not garbage collected. Here, this is an additional signal that helps backend calculate the metrics, right? It doesn't affect your HTTP monitoring as such.
Liudmila Molkova 00:16:41 You still don't know when the stream ends, because there is… if user didn't close it explicitly.
Surbhi Agarwal 00:16:48 Yeah, sure.
Liudmila Molkova 00:16:49 read to the end, you don't know if it ends. So you cannot guarantee that the end body timing will be correct. It's anything after, right?
Surbhi Agarwal 00:17:00 That is true, but then that's why, this signal, it's the issue only with Android, it's not an issue with… browser and iOS. So, browser and iOS, what happens is, asynchronously, after the HTTP span is done and sent to the backend, right.
After the call is done, they asynchronously have APIs, resource timing API in case of browser and URL session task metrics in case of iOS.
So, they asynchronously get these metrics.
And then they are able to create an event out of it with whatever data is available. So if body read timings are not available, they'd be represented similarly.
So the backend knows that this wasn't available, or body wasn't read, whatever the norm is for these platforms, right? Only in Android, that's a problem.
Right? Wherein, For the event, we do not know, we are not sure how to end it, but then there are ways to ensure that. There are new configurations that we can add for somebody opting in into this event newly. They can configure that timeout that, hey, wait for this much time.
And because when a person would be configuring it, they would know how their HTTP events are happening in their app. They would know whether they are closing the response body correctly or not. Are they leaking it, or are.
Liudmila Molkova 00:18:36 I would not rely on this. If they knew they were leaking it, they would fix it.
Surbhi Agarwal 00:18:42 No, no, it's not about them fixing it. So, similar issue was there with HTTP URL connection as well. There also, we implemented this strategy.
But then, SPAN doesn't fit the, like… all the use cases. So here, this is what the proposal was to deal with the edge cases, where the… we do not know whether call end or call failed will be called.
Which is particularly for Android scenario, where we do not know where the response body will be read. So, here we suggested a periodic timeout, scheduler, similar to what we did in HTTP URL connection, scenario.
wherein the app knows what they are doing with their HTTP requests, they know what they are closing it or not timely, and they are able to set a timeout.
And we are able to ensure that the spans in this case, in case of HTTP instrumentation, are getting to the backend based on what the app chooses as the configuration.
So, I think this… this is…
Liudmila Molkova 00:19:56 So this is the custom code that users would write.
Surbhi Agarwal 00:20:00 Yeah, this is a custom code that the user… they need to configure, timeout. And internally, we have wires to ensure that this gets… this is respected.
Liudmila Molkova 00:20:13 in practice, very few users would do this. They would use auto-instrumentation, and they would not write the code, or they would write it in an incorrect way. The… let's figure out how we can address the delta with the… Best way possible. It seems like the only timing that… is not captured on the HTCP span is the end of stream.
And it will be useful for everybody to capture if it's possible, right? We can say this event is not guaranteed, but other timings are.
And.
Surbhi Agarwal 00:20:51 Other things also, let me touch base on them, right? Keep it at the back of your mind, so, okay, I get what you're saying, but then I mentioned browser and iOS, right? They do not… Have a synchronous callback.
which they are following along with the network request happening. So, they just asynchronously get an event wherein they get these metrics. So, like, if you were to think of them.
We talked about parent-child relationship in case we were to have a separate span.
Right? So, there is an issue with that. So, browser has already sent the exported, the original HTTP span by the time they receive this data. So, retrospectively, they can't parent something. If they were to do that, they would have to create a span beforehand in anticipation of receiving that event later on, and parent this And for whatever reason, if that event did not come, they parented something, and in the backend, now the parent is missing for that original HTTP span.
We end up adding another trace level.
To the hierarchy.
And this is…
Liudmila Molkova 00:22:11 You're saying that the browser and IOS Don't… cannot parent to an HTCP client span, even if it existed.
Surbhi Agarwal 00:22:22 Yeah, they already send it. It is already exported by the time this metrics is received, which we want to put in the event.
The data that we are talking about here in this PR that is received asynchronously after the fact that the HTTP event, HTTP request has already happened and the span out of it has already been exported.
There are other places in browser where there is no span.
And there won't be any span. There is just this event which is being received. So there also, there is no parent-child relationship. There is just… This new… this data that needs to be sent there.
Liudmila Molkova 00:23:04 So it sounds like the browser and AI are some somewhat special.
The Android was okay, HTTP is pretty much as anything else in Java.
And these 2 cases are.
Completely separate in what happens and how it happens.
Surbhi Agarwal 00:23:24 Yeah. And the.
Liudmila Molkova 00:23:25 Unprecedented reminds me of is the browser timing in.
browser, where we said, yes, resource timing, is that we don't attempt to, represent them in OTEL, we represent them as something that's for following the browser signal. We just capture what browser provides almost as it is.
Surbhi Agarwal 00:23:52 We would like to unify these, that's why we had discussion with BrowserSig and MobileSigs to figure this out.
So, this is a effort to unify the semantic conventions and have an hotel semantics around this. I had another thing that I wanted to call out. So, our intention was to have this Semantics for the client-side apps only.
Not for the server-side apps.
So I wanted to ask this question here. Is that okay if server-side apps are discussed separately? Was there a confusion there earlier?
Michele Mancioppi 00:24:32 It's people are going to get very confused by this, yes.
Surbhi Agarwal 00:24:37 Can we put it in the semantics that this is the case, that this convention does not cover the HTTP clients and server-side apps?
Liudmila Molkova 00:24:47 It's difficult because you have attributes like time to for first response byte or something that would be natural candidates for an HTTP client span anywhere.
Right? Or…
Surbhi Agarwal 00:25:02 Okay, thank you.
That's not an attribute, that's a metrics that you can drive out of the attributes.
Liudmila Molkova 00:25:10 Well, this is an attribute. You put it as an attribute on an event, which means somebody can put it as an attribute on span and it would fit naturally there.
And time to first byte is uniform metric across client and server.
Surbhi Agarwal 00:25:25 There is no time to first byte attribute in this PR that's being suggested. That's something that can be derived in the backend using these attributes. We are only mentioning the start and end of the various phases here in this PR.
Liudmila Molkova 00:25:40 I mean, this, whatever attributes there are here, they can be.
on the HTCP client span on the server as well.
Surbhi Agarwal 00:25:48 Yeah, but we haven't done that work of, working with the server side yet, and I'm not, like, the one who can do that, actually. Not… don't have…
Liudmila Molkova 00:26:03 I'm not asking you to do the work. I'm asking to design the thing that can be used across.
Surbhi Agarwal 00:26:10 introduction.
Liudmila Molkova 00:26:10 using this attribute, it can be used on any signal.
Surbhi Agarwal 00:26:14 Yeah, fair enough. So my question is, do you think that this… there is no way we can have these semantic conventions for just the client-side app with the comment right now, while we work on that in development phase, while we work on that?
Or do you think both of… somebody needs to work on that, and then this… and then how do we find that… Someone who takes the ownership for that.
to unify these things across the server side apps and client side apps. These are my like multiple questions here.
Liudmila Molkova 00:26:49 The way I'm curious what other thing, but the way I see it being specialized for clients is that the attributes are not specific.
to clients, and maybe potentially add it, to the server in the future. Well, not to the server, but to the HC^C client on the server.
And the event name itself can be specific, but I then.
We would log the context to say if it's useful to unify resource timing and IOS.
metrics. Yeah, Josh?
Josh Suereth 00:27:28 Yeah, I… Sorry, I'm gonna try to raise the conversation up a level, because I think we still… we're coming around to, if I understand correctly, we want an exception for client-side that looks different than the way HP looks like for server-side. And we keep running around in circles around this and try not to confuse people. Surabhi, I want client-side to be able to instrument, so I guess I'm gonna ask Something first is, are you blocked on defining semantic conventions, or can you make progress with client-side instrumentation without pushing into core Semconf, right? Like, could we do something where you federate, like we're doing with GenAI, where you can actually, like, work independently of Semconf.
on what you think your exception looks like, and we get more clarity on how it works, and we can start asking the really hard questions that I think, McKellie was asking of, like, how are you going to integrate with HTTP in the long run, right? Because I think there's a… there's a reality here with client-side. You're going to be sending data.
That might not go directly to the database, it might be aggregated or transformed.
After it leaves the client, before it actually hits the data store, or maybe in the data store, in some fashion, to unify with other signals.
And from a… from a semcom standpoint, we don't know what the hell that looks like yet. We have no way of dealing with it, we have no way of addressing it. So we're asking you all these really hard questions immediately when you're just trying to get, like, an initial thing done.
Okay? And I think that's the thing I'm seeing here that's kind of problematic, of it… just fundamentally, do you need this in SEMCOMP to make progress, or can we define this, like, specifically for client-side, as an exception somewhere, that you make progress on.
And we can answer the hard questions there. And then once we understand how these hard questions interact, we can come back to this discussion.
Is it? Is that fair?
Surbhi Agarwal 00:29:28 Yeah, we are not blocked. We can go ahead with, whatever event we have come up with, right? And… The thing is, later on, when semantic conventions are defined, first of all, we should ensure that somebody is actively looking into defining them.
Right, that's my… that would be a worry. I would have, like, if I leave it here, right, would there be somebody taking it up from the server side to… Talk with me, and we can discuss such that we can unify it for both server-side and client-side.
That would be my worry. And secondly, yeah, we can do it, but the thing is that, yeah, we'll need to change, adapt to the new semantic conventions whenever they are available, both in the agents and in the respective backends, but that's okay.
But…
Josh Suereth 00:30:24 Well, so I'm actually, Correct me if I'm wrong here, some of this is, I don't anticipate us making significant changes to our existing HTTP SEMCOM, because that would require some kind of major version bump.
What I'm more wondering is, when we think of client-side holistically.
and how this observability cycle will be, right? You have a bunch of data that looks non-traditional from server-side, right?
How is a person who is observing both clients and servers going to interact with the data? That's the fundamental question we need to ask here. And when you want an exception, one of the easiest exceptions could be, you know, no one would ever try to actually put the client side data that we're talking about.
In the same context as service ID.
If that is true, then you have a clear use case for an exception, because you're actually a completely different user journey, completely different set of users, right? And we can say, cool, there's an exception for this, 100%.
I don't know if that's actually true from the discussion we're having and some of the concerns. So the second thing would be, you guys continue working with this event as an exception, but we don't put that event in SEMCONF, we put that event on your side.
Like, you would have, like, a semantic conventions for client-side that would define your event.
And we and we start working on this question together. So you would keep coming and talking to us, but you're not blocked on a PR frustrated, you're making progress, you're moving forward, you have an event defined that you're experimenting with. And we can start figuring out what this looks like in an end to end system where we want to be able to see client side network connection status, service side connection status and look at them.
kind of together. Does that make sense?
Surbhi Agarwal 00:32:07 That makes sense. I have a confusion there. So when you say define it in the bucket of client-side semantics, would that be the individual repositories for iOS, Android, and browser, or would that be someplace here?
In this report.
Josh Suereth 00:32:27 Yeah, so we… we started to… you… you can show this if you want, Ludmilla, I think you're presenting. Like, for GenAI, we gave them their own repository where they can define things specifically for GenAI, so they could move faster than this, the overall thing. There's a few limitations we have when we do this, right? Like, when we spin stuff off, but if you're willing to work Where what you do would not be part of HTTPSemconf, you would literally be an extension, or, like, a, a deviation from it in some fashion.
that's… that's kind of how this works. So, like, you would… you would find a way to eventually interact with HTTP SEMCOV, but you would have, like, a client-side specific namespace that you could use to do all of your experimentation in and define things. Do you want to show the… the GenAI thing, just so we can show people what it looks like?
That's so big.
Liudmila Molkova 00:33:21 We can take over, or…
Surbhi Agarwal 00:33:23 Yeah, go ahead But, this is one thing that we discovered is separate. Like, would a repository be justified for one thing like this?
If we create a repository, you'll need to have maintainers and approvers, and are there more agenda items that can… more items that can live there?
Josh Suereth 00:33:47 Right, this is where my expectation is, and again, I haven't been to the client-side SIG, I just know that a lot of them attend the entity SIG, so we talk there, but my expectation is that there is a large set of events that the client-side SIG will be defining and getting out of browsers and phones, right?
And that you have a lot of events to… to generate and kind of find a way to export.
Basically, what we'd be doing, similar to GenAI, is we'd give you a namespace where you would define those events within, and then your approvers, the way you move forward, there's a set of things that we'd be requiring from SemConf, so you're compatible with SemConf, but Outside of that, you would self-approve the set of events that you're exporting.
in your, like, client-side semantic conventions, if you will. Okay?
Surbhi Agarwal 00:34:37 Hmm?
Josh Suereth 00:34:38 So, it would let you move forward much more quicker. Now, it's not, like… there's a dependency relationship here, where client-side would have to depend on SemConf, so you can't just, like, change the meaning of something SemConf has defined, the core.
but you can define new things within your namespace and kind of explore in a much faster way. So, like, for example, in this… in the CENTCOM GenAI, if… if we look at, any of their docs or their model, inside of GenAI or MCP, right, there's an MCP namespace. Inside of the MCP namespace, there's a whole bunch of attributes defined for modeling MCP.
Right? These might reuse attributes from HTTP. It might reuse things from networking in core, but it defines its own set of new attributes. And they were able to make progress kind of independently of Semconv with the understanding that they're a extension.
They have this, you know, place where they… or a namespace where they can play and make rapid decisions and kind of prototype and get things out relatively quickly. There's an expectation that they keep their users stable.
but you don't have to actually align all… everything against OpenTelemetry all at once straight away. Like, we have a path to success there, in the long run, so it's a bit less friction for your group.
Surbhi Agarwal 00:36:01 I see. There is semantic conventions incubating repo as well.
Which already has some stuff. Would that be a fit for this kind of stuff? Rather than creating a new repo?
Liudmila Molkova 00:36:14 There is no such ripple.
Surbhi Agarwal 00:36:16 Oh.
Earlier was there…
Liudmila Molkova 00:36:20 No, I think you're talking about the quad generation that produces incubating import pass somewhere.
Surbhi Agarwal 00:36:29 Okay, from maybe semantics which are experimental?
Liudmila Molkova 00:36:34 They are still in this repo.
And some of the, even some of the HTTP semantics are, like, you can, like, they are produced for everything.
that you see this status that's not stability, that's not, stable. So every signal has a stability and everything that's not stable goes into incubating usually.
Surbhi Agarwal 00:37:00 Got it.
Liudmila Molkova 00:37:03 I would be cautious, though, because… The defining like, as I mentioned, the attributes you're writing, they are something that's some of them or something that's we've been discussing for HTCP and expressing different phases of HTCP request is pretty generic.
So this is where I would love us to make progress in semantic conventions, but the event definition and any extra stuff can totally be separate.
Josh Suereth 00:37:34 That's fair, Lyudmila. I wanted to check with you, too, to make sure that we're not overdoing this. I'm just trying to find a way for you, like, again.
I expect client-side to look a little bit different than everything else, and I expect this question we're asking you needs to be something that has to be resolved. Like, we have to find a solution to it. I don't expect it to be, you come here, we talk about it for 30 minutes, and we have a solution.
You know, I don't expect that to actually work in the long run, because a lot of the questions that are being asked are really hard, and they're hard commitments and decisions. What I'd like to see, because this works really well in OTEL, is, you know, give you guys a place… a place to play, and get everything working, and show us, right? So you would come back with, here is a system that collects these metrics.
via events, and here is how we're converting them into, storage in some kind of a database that where a user can look at, you know, HTTP metrics and look at client-side HTTP information, and it makes sense, right? That's… But I think that's going to take time to evolve, and, you know, the client-side SIG needs to be able to make decisions there, where they can move quickly and figure stuff out.
This decision, though, like what we're talking about, I think is a rather hard one. I don't think this is a, we can sit down and force it through. I don't think we're gonna force through that PR relatively quickly.
Without answering these tough questions. And to some extent, again, the way that I've seen this work best is demonstration, right? If you can show what it looks like and show how these things don't confuse users.
That would alleviate a lot of the concerns and things we've heard in this meeting.
Surbhi Agarwal 00:39:18 Got it. I understand, yeah.
Would you be able to share a point of contact from the server side who I can exchange thoughts with to see?
How it should look like on the server side.
Liudmila Molkova 00:39:37 So, there is no dedicated HTTP semantic conventions group yet, but me and Trask were the ones who were the authors of the original one, and I think we're still the approvers.
And whenever you have a question of who owns what you can.
Check with.
this… code owner's file.
And there is a group and you can check who who are the people on this group.
Surbhi Agarwal 00:40:03 Sounds good.
Yeah, this is…
Liudmila Molkova 00:40:07 Christoph?
Sorry.
Christophe Kamphaus 00:40:08 Yeah, I wanted to ask, which other conventions do you expect End User SIC to define? Are we talking about real user monitoring?
Surbhi Agarwal 00:40:22 Yah.
like, was that question to me? Yeah, real user monitoring, like, want to define Metrics?
I'll quickly share my screen again.
So… Yeah, this issue has the example… So, yeah, we want to, like, this is not exactly what final PR contains, but it was the initial proposal. So, basically, we want to be able to add the start and end timings of these various network phases.
such that backend can calculate these metrics, what was the DNS resolution duration, TCP duration, TLS duration, which… and, like, TTFB, where it would be header, start and body end, not really header, start and header end. Right? It would be a different set of the 2 attributes that could be required.
So the idea is to have these attributes at the backend, so backend can calculate this. Also, have a context to the original HTTP span, which contains other data, which could be used for filtering and aggregating on these metrics.
like the URL, server address, server port, network carrier, whatever is relevant. We came up with a list of things that would be relevant to these metrics, like this.
So, some backends can't yet correlate. We thought that we would copy these to the event, but then, yeah, we… that is an instrumentation, and that's not a part of the PR.
Christophe Kamphaus 00:42:37 No.
My question was more after defining this, these metrics or events, are you thinking further? Do you have other conventions that you want to define?
For example, for real user monitoring interactions on A mobile app or web site.
Surbhi Agarwal 00:42:58 Oh, yeah, that is missing today. I do not have… an agenda, any plan as such for further defining those. And but you are saying that could be a good Place, like the new report, to define such things.
Christophe Kamphaus 00:43:14 Yes, if you have more plans to define in the future, it would be very good to do it in a federated way, because there you can experiment as much as you want.
Surbhi Agarwal 00:43:26 Got it.
That makes sense. Yeah, there are no semantic conventions around some of the client stuff which could live there.
I'll take it to the client SIG and see, and get more ideas, and see how to go about that.
Would there be a documented process to follow for that, which I can… Oh.
Like, refer to while talking to them.
Liudmila Molkova 00:43:57 Not quite. We're going to talk about this. This is the the other topic we have on the agenda.
Surbhi Agarwal 00:44:03 Okay, okay, yeah, like, whether to get… where to get sponsors and all of that.
Liudmila Molkova 00:44:12 Yeah, that you're… To clarify, you don't need sponsors, because Mobile and ClientSeek are active, and they would, own this work. This is the scope of sponsorship that's needed.
Surbhi Agarwal 00:44:28 Okay, but would… there should be dedicated maintainers, no?
Like, the maintainers on the different client 6, would they each be maintainers on this new repo as well?
Liudmila Molkova 00:44:44 That that's a good question. I don't know. I think the mobile and browser and should decide.
Josh Suereth 00:44:53 Yeah. I would use that as a starting straw man proposal, but yeah, I think effectively it might be a subset of your current maintainers, but it'd be folks who care about the transmission of data.
Surbhi Agarwal 00:45:09 Okay.
Liudmila Molkova 00:45:11 We we have a client approver group, for Semconf. This can de facto become maintainers of the Semconf. Yeah.
Okay, let's talk for duration.
Since we'll end it here.
Er… So… Let me share again.
Okay, so what, Do we have today. So we need a separate repo.
We decided not to do federation within semantic conventions repo, even though we could have done it.
I'm… Then… There are some tricks we do in Gen AI that are.
That should not be.
Necessary in the future.
So, Rudiger, I think you went through some hacks that exist to clone semantic conventions, remove duplicated files, and such.
It's.
Not necessary anymore, because of… This PR?
Let's see.
you can now declare a dependency on semantic conventions, but main branch. Maybe we should just release some kind of because it's helpful.
So what happens here? We have a manifest, That allows to… Errr… Use it as a dependency. Second, we added a special magic connotation to say ignore this from when you resolve this as a dependency.
So that you can mark all your mainframe things that you would rather have in your repo as such.
And then you don't need to do the dance with, Removing stuff, you can just say… We didn't do it in GenAI SM Conf yet, but… We will, once some conf is released, you would say, okay, this is the dependency, the schema URL would be whatever, And here, you would provide the… the URL to semantic conventions, because it's it's not schema. We don't publish the schema here yet.
Oh, we can… but we can put a link to the Samconf repo, to the tag, Here.
and… It will be used. You won't need to clone or do stuff. Okay, so this, like this.
should we release Semconf?
To make it easier, Are we in a good place to release? I think we should be.
Cool.
So let's see.
Josh Suereth 00:48:28 So once we have that, then we think GenAI should be in good shape.
To publish?
Liudmila Molkova 00:48:36 Gen AI, well, a separate topic.
Let's not talk about it yet. Let's get there.
Err… You connect the connection item to the release.
Because I really want it to happen.
Okay, So for Eurodigger, the changes in Semconf would be to deprecate everything?
Ruediger Schulze (IBM) 00:49:23 Great, yeah.
Liudmila Molkova 00:49:25 No.
Ruediger Schulze (IBM) 00:49:25 It would be the mainframe namespace, the CUS namespace.
And potentially some of what we have on the IBM namespace. TPS is not in yet, as we have seen earlier, but there's a few definitions that we have in, and that we would remove them once the other repo is fully populated.
Liudmila Molkova 00:49:46 Do you want to go ahead and send the PR with this annotation so that before the release?
Ruediger Schulze (IBM) 00:49:53 I can do that. I can do this in the next days. Yeah.
Cool. Yeah, let me do that. Yeah, that's… that's possible. Yeah.
Liudmila Molkova 00:50:03 I think it… you don't need to deprecate… Your stuff until you actually publish it in the new repo?
Ruediger Schulze (IBM) 00:50:11 Mmhm.
Liudmila Molkova 00:50:13 So then it would not affect anybody who generates code or uses conventions because nobody uses them as a dependency yet. So you would just do this. Once the new repo is established, you can come back and mark those as deprecated saying, okay, they've been moved around.
Ruediger Schulze (IBM) 00:50:31 Okay.
Liudmila Molkova 00:50:33 Good. Okay.
So then I'll wait for your PR, so that… yeah.
Okay. And then there is the.
More cool stuff, so… Here we use templates.
We duplicated them, and we generalized them a little bit.
I'm… it doesn't have to be this way. So, what I… what we can do better?
is we have this viva packages repo where we can keep yeah.
Generic stuff, common stuff.
I sent a PR, so Josh, maybe you can take a look to have the generalized templates we have here for GenAI in this repo.
There is, a thing that we cannot, we need to work around for now, but it seems inevitable.
Okay, so let me open the README and remind myself what was it.
Sorry, those are tests.
And… There should be a README here… Yeah, so there are a bunch of configurations, that… Exist for these templates.
The Sorry, the example would be easier. I should have an example.
Mmhm.
Weaver, Weaver, Yamo. Wonderful.
So these are the configurations for the links because links are special. So those are easy. This is just the fundamental pieces of guidance. They are still from the Semconf. We use Hotel IO for them because it's the… link that exists to guarantee. Well, it's more reliable than Otel, and doesn't need to change his versions.
These two friends are the most interesting.
When… We… Have a link!
For example, in the document, this is the generated part.
Let's take Colocrat. I don't know this one.
So, this… Attribute is defined in this repo.
So if I click on it, it will go to this repo. This guy is defined in semantic conventions repo, right?
And, the docs generation is kind of tricky, and it uses some heuristic to differentiate, but this heuristic is currently limited to, okay, there is the core repo, my dependency, one dependency, and me.
And this is the link to my dependency.
Only one is supported.
And you probably can just copy over this example because it's the same. In theory, somebody could depend on something else and would use some other.
Links. This is overwritable from the Weaver command with minus minus param, but you can also hard code it in your Weaver YAML.
So, I would propose, like.
Josh, if you have time this week, could you give this PR a review? Maybe we can merge it and ask And I will switch the GenAI to this one.
Josh Suereth 00:55:03 Yeah, sounds great.
Liudmila Molkova 00:55:05 Yeah, I had since You're here, and I had a question.
Related to this, we already have some templates and They kind of make sense. They are easy, right? They are simple profile. And this is more like advanced profile.
So… I'm currently in this PR. I'm replacing the simple ones. Maybe we just keep both.
And people can choose if they want a simple or they want advanced.
Josh Suereth 00:55:40 I'd rather have a strong default myself, like… So… if we think that these are going to be generalizable and usable by everyone, like, let's focus on one set that we all improve, as opposed to having two. The simple ones are simple, but they're also not really usable. I mean, they're usable.
they're hard to read. Like, I think we spent time in SemConf making the stuff we generate readable and succinct and, like, linkable and all that, so I… I think we would end up doing that with the simple version anyway, so I'm a fan of just replacing with this.
Liudmila Molkova 00:56:18 Okay, one… Thing to think about the simple one.
renders everything as registries, metric registry, event registry. They're registries we don't have today, and does not support Markdown, update Markdown at all. This one is somewhat opposite attributes or entities are the registry, and everything else is through Markdown.
It's kind of a different philosophy.
Josh Suereth 00:56:44 I mean, I would… I would want us to actually have a registry for everything at some point, and then if we continue to use Update Markdown, that's fine, but… So you're saying the Update Markdown is in this? I haven't reviewed it fully.
Liudmila Molkova 00:56:57 Yes.
Josh Suereth 00:56:57 Okay.
Liudmila Molkova 00:56:58 Update markdown is in it is in this, and from the GenAI, I don't really want to have a registry of spans and metrics yet, at least.
Josh Suereth 00:57:07 Okay.
Liudmila Molkova 00:57:11 Cool. So then let's get it reviewed. Let's, maybe, if you wanna change, I'm happy to change.
Then.
Rudiger, Sorbi, and other people can reuse.
this template.
Ruediger Schulze (IBM) 00:57:34 It's actually good that you answered this here, or showed this here. I was wondering specifically about the templates, if they should be moved over, or if they should be generic, so thanks.
Liudmila Molkova 00:57:45 Yeah. Awesome. Thank you. And, it's obviously easy to copy things for now. If you, like, if we don't have it merged and then remove them, just it would be unfortunate if they start to deviate across five different federated repos.
Ruediger Schulze (IBM) 00:58:01 Okay.
Liudmila Molkova 00:58:02 Yeah, okay.
And Dan, we didn't do the release… Oh, we probably have a release workflow for this one.
I'm.
It's.
not finalized, we didn't test it yet, I would not recommend reusing it, and we kinda wanted to bake this thing for a little bit longer before we do the first release.
So, Rudiger, if you are looking for a release for a federated repo sometime soon, we can work together and figure it out, but it's the… Greenfield thing.
Ruediger Schulze (IBM) 00:58:37 Yeah, this would have been my next question. I haven't looked at releasing or how the release would work for this type of semantic conventions.
Yeah, hopefully, you know, with a minimal version, we could, you know, have at least a base being released in sometime soon, and happy to collaborate on that, and, you know, understand and help with the process.
Liudmila Molkova 00:59:02 Yeah. And in general, like, there are some mostly manual prerequisites here. The.
That are, we will automate. The key part is this workflow, I'll do… oh, here.
So the key.
Thing here.
Is this make package dev, So this calls Viva registry package.
So once you're ready to release, you have everything, all versions bumped.
Everything looks right. You call with a registered package.
You give it the schema, you write the place where it will be hosted, and it would… The only thing it would do for now is to make it, this published schema available on your GitHub artifacts after your release. There is the piece that's absolutely… Greenfield, kills.
Write it down.
Neighbor registry package.
And then GitHub release artifacts. The part that's completely missing is Otelio publishing.
I didn't even research it yet. It should be a reveal. I was going to maybe ask some AI to figure out what's needed on Atelier and go talk to Atelier people.
Uhm.
We can work on this together if you want, like, when you feel, like, you're close to releasing, we can go figure it out.
Yeah.
Ruediger Schulze (IBM) 01:01:08 Sounds good, yeah. So time-wise, I hope that, you know, I have something for this week's SIG meeting to have the, repo initially populated, and then the PR was, With a sick team being, you know, going through.
And then, you know, we can have some initial… Semantic conventions being… being put to the repo, and… Once we have this being approved.
We can work on an initial release.
So hopefully sometime soon, yeah.
Liudmila Molkova 01:01:42 Awesome.
Cool. So then, I'll wait for the PR from you, we'll merge it, we'll release Semconf, it will make things a little bit easier, and we will figure out the templates, and then… Yeah, we'll work on those. Sounds good.
Great. Thank you all.
Ruediger Schulze (IBM) 01:02:01 Thank you.
Surbhi Agarwal 01:02:01 Can I ask, can I request you to put the guidance that we discussed today for the PR in the PR, like a small comment, so that will help us, like, keep everybody on the same page, as the PR is not going to have some activity for some time?
Liudmila Molkova 01:02:18 Yeah, sounds good. Thank you. I will try my best to do it today. Thanks.
Surbhi Agarwal 01:02:22 Yeah.
Liudmila Molkova 01:02:23 See you later. Bye.
Surbhi Agarwal 01:02:26 Bye-bye.
Armin (Dynatrace) 01:02:26 Bye-bye.
