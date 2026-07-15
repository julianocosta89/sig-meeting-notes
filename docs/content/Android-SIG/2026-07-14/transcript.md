SIG: Android SIG
Date: 2026-07-14
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Hanson Ho** 01:04 Hello!
**Jason Plumb** 01:05 Good morning.
**Cesar Munoz** 01:08 Hello?
**Jason Plumb** 01:09 Good evening.
**Cesar Munoz** 01:14 Morning.
**Hanson Ho** 01:16 So a friend of mine said Dinosaur Junior is the most is the daddest band of all dad bands.
**Jason Plumb** 01:23 I think you might be right.
Now.
Yeah, I think, I think of the bands of the kind of the grunge era that are still around, I think they're the ones I've seen the most too.
Anyway, good band. Check them out. They have a new album. They're touring.
**Cesar Munoz** 01:56 Dinosaur?
**Jason Plumb** 01:58 Yeah, okay.
**Cesar Munoz** 02:00 Had a hair print.
Do you know about them?
I'll say no.
**Jason Plumb** 02:05 Well, I'm.
**Cesar Munoz** 02:06 Hello.
**Jason Plumb** 02:13 All right, we have one item on the agenda. I can add one, too.
But let's go ahead and jump in. We've got a good turnout so far.
So it looks like Ben wanted to talk a little bit about, and… Did Ben drop? Right as I was…
**Ben Joseph** 02:32 No, but hey, I'm here, yeah.
**Jason Plumb** 02:34 Okay, okay. Hey, you wanted to talk about Compose Navigation?
Yeah.
You're on mute.
**Ben Joseph** 02:49 Can you hear me? Okay.
**Jason Plumb** 02:50 I can, yeah.
**Ben Joseph** 02:52 Sorry.
Yeah, so I was hoping to add, compose instrumentation, for OTEL.
And I was looking for some guidance on how we need to go about doing this. I understand.
We already have the visible screen tracker.
So, Jason, I see your comment that we would like to see it integrated as part of that.
So, yeah.
How, And I looked at other implementations, I think, from Sentry and Datadog. What they typically do is hook into the navigation.
Pick up whichever composables, like, loaded or, like, displayed.
Use that as the screen name.
Yeah.
this is the manual way of doing it. There is also an auto-instrumentation wherein you are Either by ASM or… IR, you… Automatically instrument this.
like, they have their own advantage and disadvantages, I guess, but, like, I was hoping, like.
As a first step, we could… have an API that people can call, and then probably, as the next step, also have auto instrumentation in place.
So given that, like, what should be the approach, Yeah, should be, Again, looking at some of the previous implementations.
I see they create custom spans using the navigation hook.
Is that what we want, or just we want to update the current visible screen tracking?
Because we already have that implementation.
Any thoughts on that?
**Jason Plumb** 04:51 Yeah, that's a great question. I'm curious what other people think.
**Hanson Ho** 04:56 Bands are wrong for that, I think.
I think these are navigation things, should be events.
Because we could have different types of vets, folks, don't tend to use spans to track non-performance things. And although they're useful for certain things, for view, They tend to be a bit misleading, they screw up waterfalls and Navigation events are right there.
**Jason Plumb** 05:27 Spans are typically for operations that take some duration or that perform, you know, something over a length of time. And if it's just the, if you're trying to time how long it takes to transition from a screen to a screen, then maybe there's some discussion to be had there. But if you're just giving, if you just want to provide a notice.
Or a notification that… The old screen is no longer active, it's a new screen, and that does feel like more of an event.
Just to try and tee apart that distinction.
**Ben Joseph** 05:57 Yes. I think, again, looking at some of the other implementations, they do, you know, the how much time does it take for a compose to a compose object to render or load. So those kind of tracking is also present.
of… For Otter specifically, I think, Our navigation tracking is part of lifecycle spans, I think lifecycle events. That also is currently recorded as a span, if I'm not wrong.
Should we hook into that, or… What would be the other option? Should each of these be an event where we have a previous screen and current screen?
**Hanson Ho** 06:48 So does that.
**Ben Joseph** 06:48 and navigate him.
**Hanson Ho** 06:50 There's actually… A few different types of telemetry that you're kind of roughly describing over there.
First you have effectively the load times of activities or, whatever screen you want to define. That's performance related. There's a reason, you know, it's reasonable to track that with spans. Then you have the actual navigation events when you enter and leave a particular screen.
Those are points in time. They make sense as events. And the third thing you kind of talked a little bit about, is… is transitioning in and out. Basically, if you can think of it as a canonical state of an app, what screen they're on.
That's basically metadata. You're logging an event, you're creating a span, what screen are you on?
So, you have basically… The device, the app producing, well, I guess these hooks that you could do, but from an instrumentation point of view, there are several things that we want to do with that data, and it doesn't have to be a monolithic telemetry that captures all three things. These can be broken down into the constituent parts, to be used and in the shape that, that makes sense. So, you should probably think about what you want to achieve first, and then do that, rather than say, hey, with this navigational information, what can I do? But rather, work backwards and figure out, hey, what problem do I want to solve, and what What shape of telemetry makes sense? I would say the existing instrumentation in the project.
may not necessarily be a model that you want to, like, directly build on top of, if the shapes don't make sense. So I would kind of, like.
it's like a version 2 of, like, navigation, or a view instrumentation.
That would be totally okay. I don't think you have to be beholden to what exists currently.
**Ben Joseph** 08:42 Copy.
**Jason Plumb** 08:42 I think that was very well put. Hanson and I second all of those things. If I can try and summarize, just… just to make sure that I… that we're on the same page, we're talking about 3 different kinds of things, right? We're talking about the time it takes to load a composable or a screen, the… event that you have navigated from one screen to another, and then the metadata of what screen you're currently on while other telemetry is happening. So those are kind of the three things that exist today. And even in the Compose world, I think that also maps over pretty nicely. And that's probably not conveyed well, and this issue is two years old, right? So we still need some sort of Compose navigation, or some sort of Compose instrumentation, because People are using that more and more, and we don't… we just don't have good coverage for it.
Does that make sense so far, Ben?
**Ben Joseph** 09:30 Yes, I understand, like, I…
**Jason Plumb** 09:32 Okay.
**Ben Joseph** 09:33 I wasn't trying to combine all of that. I also wanted to provide future scope. These probably might be of interest to us in the future.
And we consider that into whatever we are building right now. So that's what I'm…
**Jason Plumb** 09:48 Great, okay.
**Hanson Ho** 09:50 Well, if the original, thing is scoped as navigation, then you should really look at, Jetpack Navigation, Nav2 and Nav3, and their different navigation models, and what navigation means. There's loading destinations, basically. And there's a… depending on, you know, what framework you're using, there are different ways to hook into that, and basically capture these destination events, and then fire, hey, a destination is loaded.
So you may want to look into that if you want to just look at the headline and use that as what you're trying to do.
Ravishi.
**Jason Plumb** 10:32 And I'm gonna ask you to comment on that issue and ask to be assigned, and then I'll assign it.
**Ben Joseph** 10:36 Okay.
That's good.
**Jason Plumb** 10:38 The other thing that I don't have a clear mental model of is in the Compose world, right? Compose being… kind of like a web DOM, or, like, React Native, or whatever, like, you have this, like, tree structure, and it's all kind of programmatic, and at any time you can swap out different parts of it, right? You can… and so what some people do is they kind of build their own screen or component infrastructure where you've got some… normally, I think you have some sort of, activity, or, you know, very basic fragment, but then you've got the composables, and you kind of stay within the composables, right? Within one activity. And… Even though the screen might look wildly different and have very different business concerns, you're still on the same activity, and so that information currently, without this instrumentation, is lost.
The thing I don't have a strong sense of is, like, your screen could be one button.
And when you push that one button, you now have a split screen with two things going on. Like, I don't know what screen you're currently on. In that case, right, if you're going from, like… the way that Compose works is the notion of a screen might not be well understood in Compose. So… that's why I wanted to ask this question, is like, which composables do we even care about? You've got a tree of them on screen, which one's important? And I wonder if there's room for something like an annotation, or… I don't know if there's… like, I'm also not a compose expert, so maybe there's something I'm overlooking that's easy…
**Ben Joseph** 12:05 I think more.
**Hanson Ho** 12:06 Oh.
**Ben Joseph** 12:06 Matt, Matt Sorry. Go ahead, Hanson.
**Hanson Ho** 12:10 No, you go ahead.
**Ben Joseph** 12:11 Yeah. I I was gonna say, like, if we have to when we care about it, I think that's when we are doing auto instrumentation.
As an initial step, I think we want to provide an API. But yeah, when we are doing auto instrumentation, either we can do all the composables, which is an oracle, definitely.
Datadog follows the approach of annotation so that only those are tracked. So I think when we get to that auto instrumentation, I think we can Figure out, like, what's the best approach there.
**Jason Plumb** 12:46 Okay, so you're definitely, in this first stage, you're more interested in the API.
**Ben Joseph** 12:51 Yes, I think that should be the first step. That's a seems like a smaller.
You know, a scope that we can, like, definitely achieve.
**Hanson Ho** 13:03 I know it's.
**Jason Plumb** 13:04 I don't have a sense of what that would look like, so I'm looking forward to seeing it.
Go ahead, H.
**Hanson Ho** 13:09 Is an API then just a hotel semantic convention event with some attributes?
**Ben Joseph** 13:17 So, what… What I really… to make it easier, the API would be something that hooks into your, nav… navigation book, like, what the Compose provides for navigation, so you automatically track the destination changes. You can look at the stack, which was the previous item, and what's the next transition.
So a user or a dev doesn't have to create this events manually. So we do some of that. They just add a listener into the navigation.
**Hanson Ho** 14:00 Right.
**Jason Plumb** 14:00 That's.
**Hanson Ho** 14:01 That's on the API then. That's basically, I guess, a composable or some sort of callback hook that will produce the event.
It does require manual instrumentation, but it's on API in the sense that you fire your own event, I guess.
**Ben Joseph** 14:16 Right, yeah, sorry. I probably used the wrong term.
**Jason Plumb** 14:24 So, I… we're throwing design patterns here around like crazy, but I see this as, like, a… it's kind of a wrapper or a facade, then, on the existing stuff that the navigation… APIs already provide? Is that… is that what we're talking about?
**Ben Joseph** 14:40 Yeah, that would be more like it. It's probably, A listener, or a callback that you register?
So that we can track the navigation events.
**Jason Plumb** 14:53 Okay.
**Hanson Ho** 14:56 Yep, getting access to the destination controller for NAV2, and then adding a callback there would basically get you that.
**Jason Plumb** 15:06 Yeah, and that could be good to have that also within the scaffolding of instrumentation. Like, we normally have, like, instrumentation module, and then broken down into, like, library versus… Agent… This might be leading or suggesting that there's library instrumentation that we could build. And then the auto instrumentation would — maybe.
kind of actually be the thing that generates traces and events and spans.
Cool.
Looking forward to seeing what that might look like.
**Hanson Ho** 15:41 Feel free to take a look at the Embrace implementation. I did navigation, Stuff. That's a little while, so… I have two and a half, three support, so…
**Jason Plumb** 15:51 Can you link to it here, Hanson.
**Hanson Ho** 15:53 Yeah, once, like, my computer boots up, it was, it was a stupid, patch application. It just killed everything, which is why I'm on the phone.
**Jason Plumb** 16:02 Or if Jamie knows that code base. But yeah, it looks like you're on a phone.
**Jamie Lynch** 16:05 I can add a link.
**Jason Plumb** 16:07 Thanks, Jam.
**Ben Joseph** 16:10 Yeah, thanks for the input. Thanks.
**Jason Plumb** 16:13 Yep, just put a comment, and then we'll get you assigned and off to the races. That's great. I hadn't thought about Compose in a while, and it's definitely.
**Ben Joseph** 16:21 Yep.
**Jason Plumb** 16:25 Okay, any other agenda items that people want to bring up and or discuss before I jump onto the roadmap PR?
**Ben Joseph** 16:36 I I had one more item, more of a query from, Vishran. I think he already, raised a PR for the, native crash.
Just, I think, Jason, you has tagged in one of the comments, regarding, the label names, I think the Use the approach of having that map.
Yeah.
to, you know, because we were changing label names between minor versions, and we wanted to retain that through an opt-in, right? So, if that is the… Or this approach should be taken care of.
**Jason Plumb** 17:15 Yeah, okay, I haven't looked at this yet, I don't think.
Okay. So I can try and take a look at that.
Yeah, I know what you're referring to, though. It's the.
It's the compat thing, right? This,
**Ben Joseph** 17:30 Nice.
**Jason Plumb** 17:32 Yeah, it's.
**Ben Joseph** 17:33 We don'.
**Jason Plumb** 17:33 I don't love this, but this was a way for us to be able to have semantic conventions that are getting kind of codified or solidified, and then not have breaking changes, or allow people to not have breaking changes. So whatever random-ass semantic convention we might be using today that we don't love.
Once we talk about it and come up with something that we do love, there's a difference there, and some people might be expecting the bad name, right? If they've used.
If you use OpenTelemetry Android in their product or whatever, they could be expecting certain names and then they upgrade and the names change and they get upset.
So this allows them to opt into keeping the old names, and that's all that this was intended to do. And I know that if it's crash-related, you might just see this and go, oh, what should we do?
If it's the same event name.
then yeah, we probably do want to keep this mapping for users. But you could argue that with new instrumentation, it's not necessary, right? Because no one's expecting these events. If they look and are… if they carry the same semantics, then maybe we do.
But if it's a brand new event, then you, I mean, if it has this name, then yes, I think we do want to use that. If it's a new name, I haven't looked at the PR yet, but if it's a new name.
**Ben Joseph** 18:55 Yeah. In this case, I think it's it's a crash, native versus JVM layer. That's the difference, but I think, like, we still are hoping to use the crash here.
Cash label here.
Okay. Or if, if, if you think, if you guys think, like, that should use a different label name?
And that's also something we can consider.
**Hanson Ho** 19:16 it should be the same event name. What should differentiate it is the payload information. So there could be potentially different things that you attach to it, if it's a native crash.
So the event should be the same, so that folks can count crashes, they can just count that event. And then, you know, the details on it, you… there may be, some class — I'm previewing something — classification information or self-describing properties in there that tell you what type of crash it is or what types of payload that crash you can expect. Because for native crashes, you're not going to have the Java stack trace, for instance. Right.
Yeah, it's gonna be all obfuscated, so there's gonna be, like, blo Likely that's what's gonna differentiate it.
**Cesar Munoz** 20:04 It's the same name.
So, the PR, the… That this one, I hope it pronounced it properly. Open.
**Vishwan aranha** 20:12 No, sorry, sorry, I joined a little late, yeah.
**Cesar Munoz** 20:15 Hello.
**Jason Plumb** 20:15 Hey, which one?
**Cesar Munoz** 20:17 It is.
**Vishwan aranha** 20:17 Same.
**Cesar Munoz** 20:17 Right.
Mostly, I like the mapping, but I think what Jason mentioned about probably not needing it for a new event. It's not like any instrumentation, rather.
Because I guess we needed the mapping because we actually added a breaking change. Well.
Kind of, in the sense that we renamed an event that we used to name differently, so… So maybe it makes sense to just go with the new name for a new instrumentation.
I added there… I added you there, Jason.
Also, mostly because I know that you've been working on.
this semantic convention stuff that might help.
not having to manually… if I understand correctly, I think what you did is that we don't… we don't have to manually you know, send the event like this. I think if you define it. then there's some classes created that sends the event or something like that. So I was wondering if there was an easier way.
To do this, but it's only if there is.
**Jason Plumb** 21:27 That's a really good point. Yeah, let's talk about that. So… Okay.
Okay, so let's point out that distinction, because I think it's an important one, and I think we haven't really… Finished that work yet, so… app.crash, or specifically device.crash, is now in the upstream semantic conventions, right? This is the SimConf repo. We have Oh, it's called app.crash now, not device.crash. Okay, so I had the direction the other way around. app.crash is the actual semantic convention.
And this is still in development, but that's probably, like, what we're trending toward, unless somebody has something… revolutionary to throw at this. We'll probably end up with app.crash, which is great. And… Because this is an upstream semantic convention, it does not live in… our… Semantic conventions here are federated local semantic conventions.
Where are they?
I clicked on the wrong thing.
Right, so I'm embarrassed to even open this, but let's, like, let's look at it. So this is, like, this is all of the stuff that's, like, bespoke to this Android repo and doesn't have any definitions in upstream OpenTelemetry. So we have stuff like app.widget.longpress.
We have stuff like… See if I can get out of widget.
What else is there?
like event.websocket.open, right? These are not spec'd in Upstream.
And because of that, because these are defined here locally and we have Weaver running locally against these, we can do things like create event classes for these different events. So I'm just going to pick one, like this WebSocket one. We probably have this WebSocket event.
Let's see… Mmm… Maybe.
WebSocket listener wrapper.
Does that make an event?
There's our logger.
Here, here, see here. So these classes are generated at build time.
And we will end up publishing these. I think we will end up publishing these.
And so that fully encapsulates like what the event is. If there are mandatory required attributes for the event, they show up in the form of constructor arguments. That way you can't create one of these without passing the required attributes. And then you can also have some additional attributes. And it's just a kind of a simple.
Supposed to be, like, really, Like, fluent, the way… like, this encapsulates everything about the event as it's specced.
So it's supposed to be handy, but in the case of crash, or, like, these upstream things, we don't generate events for these, because we don't know which ones we care about. There's probably room for improvement, like, if we wanted to come up with a list of here's the ones that Android cares about, here's the ones that we want to generate events for. We could probably do something like that.
I wouldn't be opposed to it, but I'll show you how it happens right now for crash. I think if I go to Kotlin.
And we look at the semantic conventions.
The Weaver generation over in the Kotlin semantic conventions is currently committing the source code that it generates back into the repo, which is something that, Jamie, while you were away, we chose not to do in Android.
So, instead of having the source code, we're just generating the artifact, like, basically the class files, or whatever the Android equivalent is.
And we're linking and being able to use those, but in Kotlin… so we probably have… do we have this crash event? Oh, it's probably in… Yeah, we might not have that event in here yet.
**Hanson Ho** 25:53 Kotlin is on 1.41, and Crash is 1.43.
**Jason Plumb** 25:57 So that's why we don't have crash in here yet. But if crash… when this gets the new semantic conventions, it'll show up here as app.crash, and that looks like this, right? And we do use app.jank event.
I think.
In fact, let's prove that.
I wonder why.
**Cesar Munoz** 26:22 There's other stuff in your search, so…
**Jason Plumb** 26:25 Oh, was there?
**Cesar Munoz** 26:26 Yes.
**Jason Plumb** 26:27 Let's try again in a different window.
**Cesar Munoz** 26:31 Well.
**Jason Plumb** 26:33 Oh yeah, this thing. Get out of there.
**Cesar Munoz** 26:37 No, but but but I think that's fair enough. So so and I think something that this one was mentioning that It aligns with what you said.
That we only have this code generation for.
Federated events. I think it makes sense. What I like about the generated event code.
is that we have some sort of standard, you know? It's like, it doesn't matter if, probably in the future, we decide to… Well, maybe we don't decide, but we have to do more mappings, you know?
It's like we don't have to… we probably could have everything in a single type, and then we're gonna have to replicate it all over the place.
I kind of like that idea, but definitely will have to be.
Something else.
Not this, because it's only for federated conventions, so probably something for… The future.
**Jason Plumb** 27:38 Yep.
**Hanson Ho** 27:39 The federation stuff is actually super flexible. We could pull in any registry, generate any subset, actually apply special templates to special events, however, what we want. So it's definitely a good way of going forward is to.
heavily lean into this. Anything that we're deriving from semantic convention repos and registries, the code generation is quite powerful.
**Cesar Munoz** 28:11 That's good.
**Jason Plumb** 28:14 Yeah, so it looks like we're not using the upstream event for this yet, and there might actually still be a couple of places where the upstream events are just being done kind of the old way, and there's… there's probably room, I think… I think the last release of Kotlin went out last week, and I think it does include the events, so we should be able to source the… the actual app jank event and wire it up here, we just haven't done that yet.
So I'll take an action item to follow up on that.
Okay, we can keep talking about federated semantic conventions, Hanson.
**Hanson Ho** 29:04 Yeah, that's it.
**Jason Plumb** 29:06 It's a good moment to switch topics.
Do that.
**Hanson Ho** 29:11 So Federated Science Conventions is kind of like the new thing of splitting out your registries and having kind of islands of maintainers maintaining specific domains. Jason did that for Android.
And there are other ones that exist out there for things like GenAI, among other things. I took a stab and started one for, I guess, client-side or end-user-client, events. And I threw up a couple of, PRs. Effectively, the registry itself is… doesn't have code generation. All it does is define, Like the registry, what it extends from and what attributes then it exposes or attributes or events. Android right now derives or only takes from OTEL core. So the basic one or the core one where everything lives. In the PR link there, I modified it to take the sample, Android one, or a sample, a user client one as well.
And then, because we are generating stuff.
in our repo already, we could then also generate the federated events or from other registries and basically have everything kind of local there. So we'll take the, where the PR is right now, we take the core semantic convention constants from OTEL Kotlin.
And then everything else we generate using the pattern that we have, for local consumption. So, With this scheme, we're basically able to take not only the core ones, but additional ones as well. And I think there's a couple of PRs I'll probably add to do renovate updates and things like that based on detecting version changes.
This is just, we want to kind of figure out Because there is no central place that generates constants for platforms for anything other than the core conventions.
I wanna kinda ask.
it doesn't make sense for us to just generate everything, that isn't core, basically. Anything we pull in, that, from a, from a federated registry, we just generate, as, as this PR, does.
**Jason Plumb** 31:43 Cool. I mean, I've been in this world, so I think I have my head around this. I'm curious what other people think or if they have questions.
**Hanson Ho** 31:52 I also moved, the, the, the definition to V2, in the, in the repo. So, you'll see some things that you may not recognize, in the, in the schema.
**Jason Plumb** 32:03 Yeah, like, in here.
**Hanson Ho** 32:09 Oh, here you wouldn't find it, it's, it's in the original, the, the original, so, attribute group IDs, specifying that.
Yeah.
**Jason Plumb** 32:21 Okay.
That's not right. Model.
**Hanson Ho** 32:26 Yep.
**Jason Plumb** 32:28 So V2?
**Hanson Ho** 32:30 Oh, this is a definition of so registry.
So, yeah, attribute groups… So right now, you basically can pull in a group and say, hey, I… I take this in, and that pulls in all the attributes. So, event names you would address by the actual event, but attribute groups, you don't want to pull in individual attributes, as an import, so you can pull in, you know, specific groups. There is public, as well as internal.
So you can have internal attributes that you can't reference outside of your registry, so you can have events in that registry register, or, reference internal attributes, but that you don't export. So, think of it as, like, you know, a module private,
**Jason Plumb** 33:17 Yes.
Cool. Yeah, I hadn't seen that. That's awesome. Int.
**Hanson Ho** 33:26 But you have a look, give some feedback to see, hey, this is how we want to extend it. We're already basically doing it with our own distributed Android registry, but this will give another layer. Well, it's not really a layer. You actually take dependencies to both because it's… Yeah, anyway.
It's all there.
**Jason Plumb** 33:48 Cool.
Thanks for sharing that, Hansen.
If people haven't seen this yet.
It's, I think it's… it's… It becomes very obvious when you look at the registry of attributes that we have in Android.
How funny some of them are.
And it's actually less obvious now that we're not generating the classes, because the class names really showed this. But like, you know, we have Oh, what was, like, a really good one?
Like, heap-free, I think there's an upstream equivalent for this, and we should probably just be using that, and not this at all.
But there was one that was, like, really funny.
**DavidGrath** 34:38 Screen the lasts.
**Hanson Ho** 34:41 Last thoughts.
**Jason Plumb** 34:41 Yeah, this one, oh my god, yeah, last.good call out, David, yeah, last.screen.name, because the namespace is called last, like, what? It's completely broken, like, it should be probably screen… dot last dot name, you know, just Or something better than what it is now, like…
**Hanson Ho** 35:01 To be fair, we never thought of global scopes for, ostensibly, like, local attributes. Like, we always thought the.
**Jason Plumb** 35:09 Totally.
**Hanson Ho** 35:10 And now we're saying, hey, everything's local or it's global and it really matters what that first one top level namespace is. Then it becomes, oh yeah, start.type doesn't make sense anymore because you don't have a qualifier about what it is. So a lot of this I think is just.
It is what it was.
**Jason Plumb** 35:30 Totally, and when this was being, like, hacked up in kind of an isolation, I imagine there was a preference toward brevity, you know? Like, when you're just building this thing for yourself, might as well just keep it simple and short, but… yeah, some of these things are very much wrong, and we need to fix them, so… I'll use that as a good transition to talk about the roadmap PR I put in yesterday.
Which is just a bunch of pros, but if you're interested about this project, and kind of the shape of the direction of it, and where I think we're probably trying to collectively take this thing, please have a look. And semantic conventions are mentioned.
Anyway, I don't… I'm assuming there's been some discussion, some reviews already, but yeah, thanks for having a look, and feedback's welcome. That's kind of all I had, I just wanted to call… attention to it. I will link to it in the doc.
and What other PRs and issues are interesting?
So no new ones for me, nothing in a few days. And yeah, some PRs that need review.
Alright. Anything else from people.
We don't have to use the whole hour.
**DavidGrath** 37:12 Okay, I guess, does anybody even know who this Hugo person is, who does drafts and lifts? I don't know.
**Jason Plumb** 37:20 their name.
**DavidGrath** 37:21 Hugo Levy or something like that. Does anybody know who he is?
**Jason Plumb** 37:25 I don't… I know… I see what you're talking about, though.
This, this one right here.
**DavidGrath** 37:33 Yeah, let me try and get any follow-ups.
**Jason Plumb** 37:40 I'm not sure who that is.
**João Oliveira** 37:43 It's from Datadog. Why are you asking?
**Jason Plumb** 37:48 Oh.
They're from Datad.
**João Oliveira** 37:51 Yep.
**Jason Plumb** 37:53 Cool.
**DavidGrath** 37:56 It's just that he seems to have just dropped it and left. We want to just know if maybe he… Still in drought Yeah, that's true.
**Jason Plumb** 38:07 I think it's okay to just drop a draft, and for… it's only been a week, right? So, if it was months, I might be inclined to do something about I think a week is totally fine and normal.
**DavidGrath** 38:18 All right, then.
**João Oliveira** 38:20 Yeah, I'll reach out to them anyway.
**Jason Plumb** 38:23 Thank you, thank you.
Well, I don't think it's a huge rush. Yeah, I just didn't recognize them. Have they? Do you know if they've joined Sig before.
Him? If he's joined SIG before.
**João Oliveira** 38:35 Not this one.
**Jason Plumb** 38:37 Okay.
But he's around, that's cool Is that the only PR from him?
Looks like it.
Oh yeah, David, what's up with this one? Are you coming back to this one There's a bunch of breakage on…
**DavidGrath** 38:58 Yeah, I haven't had the time, and when… And I have to consider the linting and then the events.
And then this federated semiconductor thing back into it, so that takes some extra work.
**Jason Plumb** 39:12 Yeah.
Yeah, sorry about that. The rug got pulled out from under you there.
**DavidGrath** 39:17 And there is one.
**Jason Plumb** 39:25 Okay, well, thanks for showing up today. I appreciate all of your input and help with this.
Ben, comment on that issue.
**Ben Joseph** 39:34 Adam, thank you.
**Jason Plumb** 39:35 All right. Yeah. See you guys soon. Bye.
