SIG: Android SIG
Date: 2025-08-19
Duration: 47 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:46 Good morning.
**Leonardo Serrano** 01:53 Good morning.
**Cesar Munoz** 01:56 Hello?
**Jason Plumb** 02:19 Well, I'm just getting… I'm just getting going this morning, but did we unbreak the build?
Hmm… Maybe not Maybe not.
Dang.
Well… I think this one needs to be merged in order to fix this. So, let's get it in… And then we'll see where we go from there.
Alright, so now that our build time's down to, like, 15 minutes or 12 minutes or something cool, we can check back in before the call is over.
… Yeah, this is a weird thing. Thanks for having a look at that. … Cool.
Oh yeah, I think there's also a breakage, maybe?
Yeah.
Oh yeah, this is a cool one. By cool, I mean not cool at all, but we need to come back to it. So, this is the update to the latest instrumentation.
Package.
And then there's also… Is there one more?
No, that's it, okay.
Cool. Alright. Well, let's, go back to the agenda.
And Leo, you're up first.
**Leonardo Serrano** 04:20 Cool, okay, yeah, pretty simple one.
This is more of a, just kind of general, like, thought exercise. I'm not sure if… Such a thing really is possible, but basically, If you go to Jaeger, … And you hook that up to, like, the, … demo application that's in the repo, start clicking around, playing around with things. You will notice that As a result of a single, … I guess, click, or whatever, you'll have a lot of trace IDs, resulting from that.
You'll have all your spans, … Put into their own traces, and… in… In the back-end world, it doesn't make a whole lot of sense to do that. In the back-end world, typically the way you do it is you have a single, like.
Finite operation, you know, the, the dev has control over it with, like, fancy annotations, or manually… Starting and stopping some spans there, … But the point is that, you know, everything that happens as a result of this, like, operation, So the operation itself is the parent span of everything else that happens as a result of that operation.
such a thing isn't… doesn't really have an analog on the front end. This… this goes for, like, you know.
not just, Android, but also you know, iOS and web as well.
I'm just spitballing, thinking out loud, you know.
I might expect there to be some sort of, like.
parent span that gets created. When I click a button.
And I might expect that span to end.
… I guess this is hard to, like, qualify, but I would expect that to end when either the UI stabilizes, or everything that Should happen after the button has been clicked?
Ends.
Be that, like, … you know, some UI rendering thing, or HTTP span resolving.
etc. It's kind of hard to define, you know, when does that parent span end, and I'm not sure there's, like, a great way to automatically do that.
Because you can't really rely on, like, you know, UI stabilizing, because what if… But if your UI never stabilizes, what if there's always things, like, happening in the background?
I don't know.
**Jason Plumb** 07:09 Yeah, it's true, … It's certainly an interesting idea, so I think what you're describing is, like, kind of a… like, using trace as, like, a way to group.
**Leonardo Serrano** 07:19 a certain….
**Jason Plumb** 07:21 … subset of user telemetry.
And the way we've done it historically is just assume that a flattened session ID can be used to group everything, and not creating as much of a hierarchy, you know, with, like, parentage.
Like, the session ID is pretty much flat. It's like a user started using the app, here's all the stuff they did.
And then, at some time later, they stopped using the app, or they got a new session, they logged out, whatever.
**Leonardo Serrano** 07:53 Yeah.
**Jason Plumb** 07:55 And certainly we do create spans. There are… there are places where a span makes sense to be used, and there are still places in the code where a span does not make sense to be used, like these zero duration spans that are still being used as events.
That I'm trying to phase out, that I hope we can get phased out, but it's a little bit slow going.
… So, yeah, I think the real challenge is deciding when to end that thing. So, you can… Right now, with, I think, with manual instrumentation, you could create a new context.
When a user clicks a button.
**Leonardo Serrano** 08:36 And as long as you don't close that context….
**Jason Plumb** 08:40 I think the subsequent telemetry will be… subsequent spans should be parented in that same context.
**Leonardo Serrano** 08:47 Oh, yeah.
**Jason Plumb** 08:48 I haven't tried it, it would be maybe a worthy experiment, but… And then sometime later, if they click the button again, or if they change screens, or whatever the criteria might be, you can then close that context.
**Leonardo Serrano** 09:01 Yeah, yeah, that is my thought, yeah. I also haven't experimented with that, but I don't really see a reason why that wouldn't work.
**Jason Plumb** 09:08 Yeah.
I think this is the first time it's been kind of explicitly asked for, with one exception, that is, at least, I think, historically, I think Embrace used, and correct me if I'm wrong, Jamie, I think Embrace used a session to rep… a long running span to represent the session.
Is that right?
**Jamie Lynch** 09:28 Yeah, that's correct.
**Jason Plumb** 09:29 Okay.
So then you would kind of get parentage, but I'm not sure, like, how hierarchical it would still be. Like, would you create, like, a long-range session around an activity?
**Cesar Munoz** 09:42 Yeah, and would you want to cover that across threads? Because if you create this you know.
context for a click, then you'll have to… Probably will be attached to the main thread only.
It's probably enough, but….
**Jason Plumb** 10:02 That's a good question. Yeah, if there's, like, background work or a multi-threaded situation, you either have to… Manually figure out how to propagate that context to the other threads, or…?
Or not.
Yeah, so is your main… like, the way that you're approaching it is that mostly having so many different trace IDs can cause havoc on backends? Is that kind of where you started from?
**Leonardo Serrano** 10:29 Basically, yeah.
**Jason Plumb** 10:31 Okay.
**Leonardo Serrano** 10:31 I'm also trying to figure out, like, … So… I've been playing around with this and trying to sort of, like, have a unified experience between, front-end tracing and back-end tracing. So, here's the… in my view, this is the ideal experience. So, … A trace ID would be generated when you do some user interaction, and you could follow along that same trace ID all the way from, you know, your UI spans to your backend spans.
That… I think is… is… probably ideal. Otherwise, like.
You know, if you have an end-to-end tracing sort of thing, like a… whatever visualization you're doing for that, you'll end up in a case where you'll just have, like, this dangling span, like, activity lifecycle span or something, or HCCP span, and you won't have any context as to, like, what happened immediately before that dangling span.
So now, in your, like, end-to-end visualization, you just have this single span on your front end.
And then followed by, you know, all your other backend spans, which are easier to group together.
**Jason Plumb** 11:49 Yeah, so I wish our demo app did a better job of demonstrating this, and it's not really mature enough to do this yet, but … I think what you're describing does or should exist in some form, so let me describe the way that I think some products already work. The user opens the app.
And or they log in, and they… we begin a user session, and it starts at the moment they start using the app.
And the user is doing things, they are swiping left, they are clicking buttons, they are, doing activities, and a bunch of those activities are strictly client-side, and we have instrumentation that's, like, reporting about how long things might take.
Or what screen they're on, and we're generating events when they do things. And then let's say that they go to another screen.
And the app needs to… so we're in… we're all in one session, so every piece of telemetry that's been generated has that session ID on it, and they can all be stitched together with session.
Now the user goes to another screen, that screen needs to fetch an image of a cat, and it needs to fetch the cat sound.
And it's implemented very simply. It does an HTTP request to fetch the cat image. Once that is finished, then it does an HTTP request and fetches the cat sound.
When that HTTP client request is created, And assuming it's instrumented.
You will get a trace that's created for that.
And that trace will have a span ID. That span ID and trace ID will be propagated to the server side.
Assuming the server side is instrumented, that context will be propagated into the server, and any downstream requests that the server makes, assuming they're instrumented.
Including all the way to the database, or wherever… whatever… wherever the… these resources or assets are stored. And, so then that… that request completes, and so you should have a chain there from a session tied to a trace, which includes a client request, and then a server and a database call, let's say. And all of those can be stitched together with a trace. And that trace completes on the client side.
And then, depending on how the application's built, let's assume now that it's time to fetch the sound asset, the same process happens. Maybe it's a different server.
But still, a new trace is created.
A client request happens to the server, context is propagated, server continues that trace, does its downstream stuff, and ultimately the trace completes when the asset is finished being fetched.
And so what you… what it looks like on a timeline, or in a RUM view, like, historically, traditionally, is that you have this long-running session.
And at some point, based on an activity, you see a trace, and ideally, that trace could be followed and propagated to the server side, and then shortly after that, you see another trace. Now, if you wanted to group those two traces into, like, some sort of, like.
Defined user behavior, or user activity.
I think we have ways of doing that. I'm not sure that… I think, actually, we didn't… donate these annotations, but we do have, at least on the Splunk side, we have these very… crude annotations that kind of can be used to, like, start an act… I forget what terminology we used it for it, but… essentially like a behavior. And so by starting the trace.
And leaving the trace open, when those two child spans, those two requests are started, they would be parented in the same behavior, or the same grouping structure, but ultimately, you would have the same parent trace for both of those asset fetches, and so I think that's close to what you're describing.
**Leonardo Serrano** 15:29 Yeah, yeah, it is….
**Jason Plumb** 15:30 So that exists today. The main thing that I think Maybe was lacking your description was that the thing that ties it all together is the session.
Right?
**Cesar Munoz** 15:40 Yeah, and also, also the… And I agree, like, we have sessions, and… It's also helpful because sessions also cover log events, not only… not only spans.
**Jason Plumb** 15:53 Totally.
**Cesar Munoz** 15:53 You might have, if you have a dedicated session view, let's call it like a timeline for the session, you can see what are all the steps that a user took, and what are all of the events that happened in between as well. I think some… Vendors call this, … Breadcrumbs, I think that's….
**Jason Plumb** 16:12 One term that I've seen.
Yep.
**Cesar Munoz** 16:14 But essentially it's slog events.
that you, you can… put all together into a single kind of view. The problem… and in this case, I… Yeah, I agree.
It is not… Ideal.
is that… … there, there, there's no… at least not with Jaeger, is it? I understood that's what you're using?
There's no way to… There's no way to see all this.
As far as I'm concerned.
By session, because that's… that's not a… that's not a thing for… for… you know alone. … history on the telemetry, my understanding is, so….
**Jason Plumb** 16:59 Right.
**Cesar Munoz** 17:00 Yeah, I guess it's… it's… It's awkward to see this data right now, unless the UI will actually show it to you.
Yeah.
The way you chose a single… big trace.
That covers a lot of spend.
So, yeah.
**Jason Plumb** 17:25 Yeah, Jae, you're definitely not a RUM… a RUM product, or a RUM… a RUM tool, but it's kind of all you have when you're generating tracing data, open source tracing data, and you want to look at it, like, that's what we have. There's no… there's no open source, like, RUM… tool, utility, product that I'm aware of. If there were, that would make our lives a lot easier, but, I think it just doesn't exist yet. And I think maybe I'm lying, or maybe this is in main… in Android, OpenTelemetry Android, let's see.
**Cesar Munoz** 17:57 Does Jaeger show other signals, like logs?
mentions? We're selling these bands.
**Leonardo Serrano** 18:04 It only spans.
**Jason Plumb** 18:06 It's getting… I think it's getting better, though. I think they're… I think they're trying to incorporate logs.
But it's still, it's not… yeah, I think it's not great. They certainly don't grok session.
Well, maybe I just hallucinated this annotation, but you could build that. We do have the width span annotation in Java instrumentation. We could, or we should maybe think about building something similar. This RUM screen name is just a way to set this kind of global attribute of the… whatever current screen you're on.
because guessing it based on the activity name is not always what people want, I think that falls apart when you're using Compose anyway, so… So we… you could… you could build something to, like, group… the… my whole TLDR is you could build something, or we could build something to group… multiple traces together under one parentage. It doesn't ex… I don't think it exists today.
And if you'd like to open an issue on that, I think that'd be very welcome.
**Leonardo Serrano** 19:09 Yeah, well, dear.
**Cesar Munoz** 19:10 I'm open to them. Oh, that's correct.
**Leonardo Serrano** 19:12 Oh, no, go ahead. I just wanted to say, yes, I will open an issue.
**Jason Plumb** 19:17 Cool.
**Cesar Munoz** 19:17 Thank you. I was just curious if there is some open-related… open telemetry-related UI that we could ask.
kind of RAM support, or something like that, or is it just… Maybe not, probably not, but just asking out of curiosity.
**Jason Plumb** 19:35 Yeah, what's that one thing? Let me look real quick, … What is this thing? Oh, man.
I know for sure I've bookmarked this. The reason I'm laughing is I've bookmarked this and lost it so many times.
Oh, I remember what it's called now. Okay.
Yeah, this thing.
Okay, let me, let me bring it over.
Have you seen this open… oh, this Hotel Tui?
**Cesar Munoz** 20:15 I don't think so.
Oh.
**Jason Plumb** 20:18 it's similar to the OTEL desktop viewer, and this is like, you know, an interactive web app. You can send it all of your telemetry, and you can get kind of a classic, APM view, like, you can view Trace Waterfall just like Jaeger does, but I think they also can support metrics and some other things.
I don't know if this demo gets there or not.
But I think that… I think that they do more than just tracing, so… The 2E is just a command line version of the same thing, or something similar, but yeah, you can do traces and metrics. I think… I think they do logs as well. So that would be an interesting thing to perhaps request of these folks.
Or at least put an issue in, be like, hey… What would it take to make a user session show up in your cool?
Terminal UI, I think is what that stands for.
That's the….
**Cesar Munoz** 21:19 I have a look.
**Jason Plumb** 21:20 I'll put a link to this thing, but that's the best I can come up with right now.
**Cesar Munoz** 21:25 Got it. Thank you.
**Leonardo Serrano** 21:36 We mentioned briefly, there could be a parent span as a session. Basically.
Start a span on session start, end it on session end. … Is that… How reliable is that? I ask because there might be cases where a session… Could spontaneously end before, like, the span has a chance to actually end itself.
**Jason Plumb** 22:07 It's true. … I… I think Hanson has brought up this point a few times.
I have always mentally compartmentalized that as, like, an edge case, and if the session expires, for example, while a session… while a span is in flight.
then, yeah, I think you run the risk of not knowing which side it's associated with. I think… I mean, there's, I think, other… I think it's… I think it's not well handled, I think is the… is the answer. But I do kind of consider an edge case, right?
I think it would be ideal to not end the session while SPAN is in flight, but, you know….
**Cesar Munoz** 22:51 Definitely, yeah.
Also, I think there is a callback.
In case you wanted to… Disclose the span when the session ends.
….
**Jason Plumb** 23:03 There is… Did we call it something obvious, like session listener? That'd be too easy.
**Cesar Munoz** 23:14 Let's go to the session package.
And….
**Jason Plumb** 23:22 Uberals.
**Cesar Munoz** 23:23 come up with… I think that change is already there. You could also come up with your own session logic.
So you decide when it starts and ends.
Maybe, though, cool.
Shield you from this kind of edge use cases.
**Jason Plumb** 23:41 Yeah, I mean, but user code, knowing when a session is ending is maybe… It would still be difficult to handle a case where a session is ending while a span is still running.
Like, if you manually started a long-running span on a button press, and then the session ends, you'd have to keep track of all of that other span state that you might have started, so that you could close it down. I think you could do that.
But if you wanted to sort of con… if you wanted to somehow let that span continue and have two sessions associated with it, that's not… that currently doesn't meet or fit the data model for OpenTelemetry. You would kind of have to end… The one span and start a new one.
If that makes sense.
**Cesar Munoz** 24:30 Yeah, I'm trying to think about the details, because… when I think the session is attached to a span when it starts, so… If it ends… If the session ends before the spam ends, And there are no new… Child spans, you know, to this band, then there shouldn't be a problem, but of course, we cannot guarantee that.
**Jason Plumb** 24:51 So we have that, we have that session span processor, or whatever it's called.
Do you know where that lives?
**Cesar Munoz** 25:00 Ugh.
**Jason Plumb** 25:02 This thing….
**Cesar Munoz** 25:02 So many stuff.
**Jason Plumb** 25:04 So… This does it on start.
So we slapped that session ID on there when the span begins. So if the session ended before the span ended, you would only see the first session.
And not the subsequent or following session.
Does that make sense, Leo?
**Leonardo Serrano** 25:26 Makes sense, yeah, yeah.
**Jason Plumb** 25:34 And really, the reason I consider an edge case is because I think there… I think we do define a maximum time for a session to live, but it's typically considered longer.
Then users use the application.
And as long as the user's clicking on stuff, it shouldn't idle time out their session.
So in the case… in the case where you're using, like, a long-running span to, like, group… Like, screen-level stuff, or, like, activity kind of behavioral… stuff.
then you can encounter that situation, but for… I think for normal usage, we would… I have always considered it an edge case.
Does that make sense?
**Leonardo Serrano** 26:21 Makes sense. I'm only concerned about the case where a device crash might happen.
**Jason Plumb** 26:29 Which we model now as an event, I think, right?
**Cesar Munoz** 26:33 Yes, hello, yeah.
**Jason Plumb** 26:40 So, in that case, if it's a… if a crash is, like, a point-in-time thing.
So, are you concerned about session timeout with respect to that point in time?
**Leonardo Serrano** 26:50 No, no, no, I'm concerned whether or not… I actually don't know what the behavior is. So, when you have a device crash, you… that telemetry doesn't generate, correct me if I'm wrong, you don't actually generate that telemetry until after the next time the app has opened. Is that correct, or does that… Telemetry get generated, like, As the crash event happens.
**Cesar Munoz** 27:14 Right now, it's the latter.
**Leonardo Serrano** 27:16 I see.
I ask because I'm wondering… is it possible… I don't know… I don't really know how this works, … Does, or can, a device crash Close a existing span.
Like, can it close a session span?
**Jason Plumb** 27:41 Did you say session span?
**Leonardo Serrano** 27:42 Yeah, or any span, really.
**Jason Plumb** 27:45 I'm just saying long-running span.
**Leonardo Serrano** 27:47 Yeah, long-running span.
**Jason Plumb** 27:50 I don't think we have any callbacks for that.
It certainly is not the current behavior.
Because the crash handler doesn't keep track or know about what other Spans might be running, right?
**Cesar Munoz** 28:10 Not that I'm aware of. I mean, I guess you could create your own… a crash handler… And then… And do… and do so, yeah, there.
**Jason Plumb** 28:20 Yeah, you definitely….
**Cesar Munoz** 28:20 I don't know how much time you will get, you know, to… To do all this cleanup.
Before the OS kills your app.
**Jason Plumb** 28:30 Actually, with the crash.
**Cesar Munoz** 28:32 We are also kind of, like, the way we're doing it, you know, creating it as the crash happens.
there might be also a risk that it might get lost, maybe, at some point. Not… not so much.
When we started to use disk buffering, because that's all that we're currently waiting for, is for it to get stored in disk, but… I'm not sure… I guess it depends on the OS, and then… flavor… If we… if there might be cases where there might not be enough time to even store stuff in disk when the crash happens, so… It's tricky.
**Jason Plumb** 29:11 Yeah, I mean, I think what you're describing, Cesar, is, like.
One of several problems or challenges that get brought up by using long-running spans for this exact thing.
So I think that's why we've avoided it, is, like, because spans have context, you have to keep track of that context. And in the case of, like, a crash, it's that… everything is going away, … Yeah, it just makes it really hard to clean up all that stuff.
**Cesar Munoz** 29:40 like, you could have your customs context stored somewhere in a static fail or something, but that, you know, that's not something I think we should provide.
For everybody, because we can't guarantee stuff.
**Jason Plumb** 29:56 So I think what Leo's describing, too, is that, like, if you had a long range span, and you were doing stuff kind of parented under that, and then the crash happens, if that parent span is not closed, you lose it, right?
If that span is not ended, if that context isn't closed, then… It won't get exported.
**Cesar Munoz** 30:15 Yeah.
**Jason Plumb** 30:18 Yeah.
And I think this… this has been solved by some vendors. I think Embrace does this. I mean, maybe I'm wrong, Jamie, but I think that there's some, like, on-disk, like, binary crash data that you can parse, and then they stitch it back with the previous session because it was persisted.
**Jamie Lynch** 30:45 Yeah, so… Yeah, I think we saw the crash on disk, and we store the session ID within the crash information, and Ben, you can Go back and, like, get the session span.
… Yeah, I think it was various things.
But… are kind of annoying about that model.
Like, mayo effect that you've just got so much state being held, and….
**Jason Plumb** 31:15 Always.
**Jamie Lynch** 31:16 It gets really complicated really fast.
**Jason Plumb** 31:28 Cool.
Alright.
Well, I only wanted to bring up the release, because instrumentation released over the weekend, and I think that we should try and do a release. I did want to get the build working before even thinking about that, and apparently I failed to do so.
I have no idea what this is.
Generate POM file for Maven publication.
**Cesar Munoz** 32:19 Does this have your changes?
**Jason Plumb** 32:21 It does.
This was the… this was the first build.
After the changes. And so, it looks like… It's still failing during snapshot, but it's failing for a different thing.
Yeah, okay, well, this is gonna require some additional work, because… I don't have a clue what this is about, but there's some indication here… Why did we go to Gradle 9 ever? Oh my gosh.
If anybody has ideas on this, input is welcome, because it's too early for me to think about this right now.
**Cesar Munoz** 33:20 John.
**Jamie Lynch** 33:21 After Gradle 9.
**Jason Plumb** 33:24 Things got much more complicated after Gradle 9, it seems like.
**Cesar Munoz** 33:29 Some deprecations and stuff.
It seems related to cache. I know that your changes disabled it, but I know they disable it, like, globally, or just for coupling.
And I think there's a way to disable compression cache.
Like, generally, Gradle. I don't remember right now.
How it is, but we can have a look.
**Jason Plumb** 33:54 Yeah, so we… Oh… wait, where is this? That's not my… my change has… oh yeah, so this is the thing I added.
I know that when we do a non-snapshot.
I think we include the… the dash dash no cache, or disable cache, or whatever it is. Let's find out.
**Jamie Lynch** 34:14 Yeah, that'd definitely be worth a go.
**Jason Plumb** 34:16 For this snapshot as well.
**Jamie Lynch** 34:19 Is that what you're thinking?
Yeah, yeah.
**Jason Plumb** 34:30 So, we… so I added this one… And I think, yeah, so no build cache is, like, right there on the command line for the normal release.
And I think… That's not new, that's been there for a while, so maybe, yeah, I'll do a quick PR and add this… to the snapshot, and we'll see if that helps as well, I guess?
It's just kind of a spitball.
And if that helps, then that gives us at least a little more confidence in the main… Release workflow succeeding.
That's frustrating, though.
Okay, let's try no build cache.
Okay, then looking at the pull requests, does anybody have some… Things they think ought to be in the… the release this week.
**Cesar Munoz** 35:32 Well, if you want to include the bumping of instrumentation.
**Jason Plumb** 35:37 We gotta fix this, too.
**Cesar Munoz** 35:39 Probably we need to merge the, … the OKHTTP Android resolution one.
Okay.
**Jason Plumb** 35:47 That's true. Okay, so I think.
**Cesar Munoz** 35:49 It's mostly done, I just had a question regarding one of your comments.
**Jason Plumb** 35:53 So I think the fancy way to do this is to create, a release milestone.
So we'd have, like, a 0.14.0 release milestone. How do you think you'd do that?
Agreed.
**Cesar Munoz** 36:07 To be honest, I haven't done so. Right.
**Jason Plumb** 36:09 Let's try it.
**Cesar Munoz** 36:12 Yeah, that's it.
**Jason Plumb** 36:13 Alright, create and assign a new one. Okay, there we go.
Wow.
**Cesar Munoz** 36:17 Okay. That was easy.
**Jason Plumb** 36:18 And then, so the other one, we definitely want this one, right?
**Cesar Munoz** 36:25 Yeah.
**Jason Plumb** 36:33 And….
**Cesar Munoz** 36:39 Hotel Gore? Is that…?
**Jason Plumb** 36:42 This one.
Oh yeah, I think we have to do this, don't we?
**Cesar Munoz** 36:48 Yeah.
**Jason Plumb** 36:49 And are they all… are they still at 5'3"?
They are, okay.
So let's… let's put this one in there, too. Okay, so we need to work on these.
What's up with this one?
**Cesar Munoz** 37:06 Maybe this is the one related to the OKTP stuff.
**Jason Plumb** 37:09 So I'm not sure… if that's the case, I'm not sure what's going on with….
**Cesar Munoz** 37:13 Yeah, yeah, this is related to HTTP. Then I'm not sure what's going on with the instrumentation one, why is it failing?
**Jason Plumb** 37:20 This one. Let's see.
**Cesar Munoz** 37:21 I can have a look.
**Jason Plumb** 37:28 Yeah, same thing.
**Cesar Munoz** 37:29 Same thing, yeah.
**Jason Plumb** 37:30 Okay, so you're… this was… I… what did I say on this one? I said….
**Cesar Munoz** 37:39 It's a bit of a long comment mind, but it's kind of like, yeah, if we go with OKCP Android, then it should be consistent, and also use OKCP Android.
When declaring a dependency.
Within the project, so it's kind of like just to keep consistent. So, if I change it to OKSP Android, then I… what I said there, essentially, is to also change it in the TAML file.
Right.
**Jason Plumb** 38:05 Yeah, I think it's a nitp… this is a nitpick for sure, because we're building on Android, that will… I think this will always resolve to the Android version, or at least it should.
**Cesar Munoz** 38:16 It's true.
**Jason Plumb** 38:17 So, it's… it should be safe to do this.
Is it consistent right now with this everywhere?
**Cesar Munoz** 38:26 So right now, that's what we're declaring in our Tamil file.
**Jason Plumb** 38:29 Okay.
**Cesar Munoz** 38:30 Just, okay, stupid.
**Jason Plumb** 38:31 Then let's just… let's just stick with this, then. I think this is fine. Okay, let's just stick with it for now. If we have a reason later to… to make it explicit, then we can.
**Cesar Munoz** 38:41 Yeah.
**Jason Plumb** 39:09 Okay, so I'm gonna merge this… Yeah, I'm gonna merge this, and then we'll rebase those other two and see if they get fixed.
Does that sound good? Okay.
Then we can look at the milestones, just those two. Okay, is there anything else?
I mean, some low-hanging stuff like this is, like, really good to just get in there too, just because….
**Jamie Lynch** 39:47 I won't have time to do this, unfortunately.
**Jason Plumb** 39:52 I mean, we can just take it as is. I mean, do you think that this is a good… I mean, it sounds like… It's… it's fine, right? But… I don't know, do you want to just wait?
**Jamie Lynch** 40:01 ….
**Jason Plumb** 40:03 You can just wait.
**Jamie Lynch** 40:04 Yeah, I think… maybe just wait, like, I went to try and address a review comment, but I was running into some issues with, like, Roboelectric not finding the new method signature, so I'll take a look probably next week.
**Jason Plumb** 40:20 Okay. If it gets too hairy, just mention that, and we can go with this, and then create an issue to circle back.
**Jamie Lynch** 40:28 True.
**Jason Plumb** 40:29 Okay.
Cool.
Alright, I will point out, since I think our agenda is still pretty light… I will find that milestone.
I think you're supposed to close it also when you're done with the milestone? I don't know, this is the first time I'm using this. I've just seen Traff do it, and… He's such a boss that I just try and follow his every move.
There is this thing that's happening in… semantic conventions around jank.
Which has been out there for quite some time.
And this is even a restart of one that was out there for even longer. … If you remember, we have this, slow rendering instrumentation that reports jank.
There was a lot… apparently, that semantic invention in… over here was, like, fairly contentious, and so this tries to restart it and keep it really simple, it just reports 3 things.
the number of frames, the period over which those frames were observed to be slow, and the threshold that it's above. So that's all that a jank event is reporting in this semantic convention. And it's looking pretty good now. I think we got a lot of discussion handled. … I did… Push that change… And then, Josh is asking, can you add a link to the prototype?
So he's under the assumption that there's a prototype for this, which there kind of is in the form of our slow rendering instrumentation, but it looks very different. It's generating spans, so I'm currently locally working on getting this prototype built. I'm trying to do it in a way that doesn't break the existing instrumentation, so that we can go through a proper one release deprecation cycle, and, like, let people emit both the span and the event at the same time if they so choose, and then the next version will deprecate or get rid of the span, just in favor of the jank event. So, I'm currently working on that.
Hopefully, I can get it out this week.
**Cesar Munoz** 42:47 I am… Super strict with that kind of, the deprecation systems.
**Jason Plumb** 42:54 Okay.
**Cesar Munoz** 42:55 for stable… versions, but since… I'm not sure… I'm not sure it's worth, you know, going through that hassle, but, like, if we want to do it, let's… I'll support it then.
**Jason Plumb** 43:10 Cool.
**Cesar Munoz** 43:11 Broadly, it's not native, but….
**Jason Plumb** 43:13 I agree with you, I think it allows us to do, like, a side-by-side comparison and, like, actually see what the code for the span versus the code for the jank looks like. It might not be that helpful, I don't think it's that much work, though, so I'm planning on doing it, but yeah.
Keep me in check if I get too… too far afield with the… The stability aspect of it.
The goal is to be nice to users, even if we're not stable, it's, like, to give them at least a cycle to know that this stuff is changing.
Before it changes, and… yeah.
Got it. Yeah.
**Cesar Munoz** 43:49 Sounds good. Thank you.
**Jason Plumb** 43:51 Yeah.
Alright, anything else that anybody wants to discuss related to Android today?
I believe this is one of the weeks where we have the client SIG.
And I might be double booked and have to miss it.
Yeah, unfortunately, I am double-booked, so was there anything in the client SIG for me?
I don't think so.
**Cesar Munoz** 44:29 Just one small thing, the app built … build ID, … Yeah.
**Jason Plumb** 44:37 argument.
**Cesar Munoz** 44:37 attribute was merged. I just wanted to mention that in case some people want to use it.
**Jason Plumb** 44:42 Cool. Did, your… did your disc buffering get merged yet?
**Cesar Munoz** 44:49 No, no.
I actually, with this buffering, I think I addressed some of your comments.
So….
**Jason Plumb** 44:59 Probably need to come back.
**Cesar Munoz** 45:00 She'll be better. Yeah.
**Jason Plumb** 45:03 Nice, so this is in there.
**Cesar Munoz** 45:07 Yeah.
**Jason Plumb** 45:08 Cool, cool, cool, okay.
We don't have anything Yeah, do we?
**Cesar Munoz** 45:14 things. So, yeah.
**Jason Plumb** 45:16 Do you have any code that generates that yet?
**Cesar Munoz** 45:21 in Android, in the Android project? Right.
**Jason Plumb** 45:24 Yeah.
**Cesar Munoz** 45:26 No.
Not that I'm aware of.
**Jason Plumb** 45:30 Did they ask you for a prototype?
**Cesar Munoz** 45:33 No, well, it's just a natural gas, so….
**Jason Plumb** 45:42 Okay.
Since we're… since we're talking about it.
That's not it, that's it.
That's it.
Why is this not labeled?
Probably because I didn't label it.
Okay. Cool, so I'll… I'll look… I'll circle back on this one. It seemed like a… it seemed like a good change.
I don't quite fully understand where you're going with it, but I'm nearly there, okay?
**Cesar Munoz** 46:22 Just so you know, I just added the API service, but I didn't actually.
**Jason Plumb** 46:27 There's no.
**Cesar Munoz** 46:28 You know, implemented, yeah.
**Jason Plumb** 46:29 Right.
**Cesar Munoz** 46:30 Did the full work, so….
**Jason Plumb** 46:32 Yeah. Okay.
Cool, I'll circle back on that.
**Cesar Munoz** 46:37 Thank you.
**Jason Plumb** 46:39 Alright, that's probably enough balls in the air for one day.
What you don't see is that just off-screen, there's, like, 34 more.
Fun, fun fun.
**Cesar Munoz** 46:53 Wow.
**Jason Plumb** 46:54 Alright. Well, it's nice seeing everyone, thanks for being here. Appreciate it.
**Cesar Munoz** 46:58 Thank you.
**Jason Plumb** 46:59 Thanks for the help.
**Leonardo Serrano** 47:01 Yeah, thank you.
**Jason Plumb** 47:02 Bye.
