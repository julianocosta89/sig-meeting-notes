SIG: Android SIG
Date: 2025-11-04
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/o5wN5tb5ZcfaHSBzOorb4a7owpQqhZigBd7l6bjT53Q0Wr3HoPfiG2-YYsN_DEUt.UYzWFZb-8gXSC-wj
============================================================

## Zoom Recording Transcript

**Hanson Ho** 00:38 Hello!
**Cesar Munoz** 00:39 So… Good morning, afternoon.
**Hanson Ho** 00:47 Very much the morning here, and very much the afternoon for two of you, at least.
**Cesar Munoz** 00:53 Yeah.
**Mustafa Haddara** 00:54 Hello.
**Hanson Ho** 00:56 Hey.
**Cesar Munoz** 00:56 A.
**Hanson Ho** 00:58 At least we're… Oh, go ahead.
**Cesar Munoz** 01:02 No, no, sorry, go ahead. Yeah.
**Hanson Ho** 01:03 I was just gonna say, at least we're done with the confusion of, North America being different than the UK. there was a one-hour offset last week, and it was very confusing, you know, when I was trying to schedule stuff with,
with people, without Google calendars. It's easier with Jamie, because at least the calendar says what? I'll try and tell them, like, what time… because I can't use BST anymore, it's not BST, it's like UK time. It's like, oh, 7, but it's…
Anyway…
**Cesar Munoz** 01:30 It's confusing, and it only lasts a week. So, like, you have to switch twice.
You know, quite short span of time. Yeah.
Luckily, I don't have to deal with that without Google Calendar, because it does help a lot.
So…
**Hanson Ho** 01:49 Spain also switches, in the same time as UK.
**Cesar Munoz** 01:55 Yes. Yeah, I think so. Yeah, it should be.
**Hanson Ho** 01:58 Yeah.
**Cesar Munoz** 01:59 So, Jason, I think he's gonna join a bit late. Oh, he's here.
**JP Jason Plumb** 02:04 Yeah, I made it. I was here. Sorry.
**Cesar Munoz** 02:06 Mmm.
Oh, that's fast.
**JP Jason Plumb** 02:08 Twice it's happened where my laptop just cannot reach zoom.us, like, at all.
**Hanson Ho** 02:13 It's just blocked.
**JP Jason Plumb** 02:15 So, that's pretty cool, and then I reboot, and it works.
Awesome.
**Hanson Ho** 02:21 DNS, DNS!
**JP Jason Plumb** 02:23 Yeah, maybe. I mean, I'm assuming it's some corporate-managed thing, but… Right.
Yeah, sorry for the delay. I was on time, though.
Just couldn't… couldn't show up.
**Cesar Munoz** 02:45 It's fine.
We're 3 minutes in, so it's not like… Losing a lot.
**JP Jason Plumb** 02:52 It's the, alright, so Trask has dropped something on our radar, it looks like.
An invitation to join on the 17th, Monday, okay.
What time is that?
The Manta Conventions Working Group at 8 AM, okay.
So, the confusion between the app namespace and the Kubernetes app namespace.
Alright, what do we got?
**Hanson Ho** 03:49 Kubernetes uses Act on.
**JP Jason Plumb** 03:55 Cool. How's ClientDot sound to everyone?
**Hanson Ho** 03:58 PlantDot sounds fantastic!
**JP Jason Plumb** 04:00 Good luck with that. Okay, well, that seems like a totally reasonable thing that we should probably think about resolving.
Yeah, having… I mean, I guess, you know, it's app.kubernetes, though, like, that's really the prefix. There's a reason that word is in there.
So should it be app.client, app.mobile, app. You know, that'll be the discussion I imagine, that we have.
**Hanson Ho** 04:28 Hot.web…
**JP Jason Plumb** 04:29 Also, we could talk about it at KubeCon next week.
**Hanson Ho** 04:32 Yes.
Who else is gonna be there besides Jason and me?
It's Atlanta, so maybe not a lot of European folks are flying over.
**JP Jason Plumb** 04:43 Yeah.
**Cesar Munoz** 04:47 Yeah, not me, maybe… maybe next year.
**Hanson Ho** 04:51 Amsterdam.
**JP Jason Plumb** 04:54 Yeah, in the spring.
Amsterdam. Okay, well, pretty light,
Pretty light agenda today. Let's take a look at this, issue that Mustafa's bringing up.
**Mustafa Haddara** 05:09 Hey, yeah, this is not…
This is… I remember seeing an issue at some point, or a PR at some point, and I lost track of it, but…
My understanding of It's propagating.
This is… this is the same problem. Yeah, this is what I was gonna talk about. Yeah, yeah, cool. Are we still working on this? I remember seeing someone have, like, a proposal or a proof of concept somewhere.
**JP Jason Plumb** 05:40 There's also this one.
**Mustafa Haddara** 05:42 Yeah, okay, so… Yeah. Yeah, they're related.
**JP Jason Plumb** 05:46 Was there… a PR, I mean…
Manuel brought up this idea, and I haven't looked at this yet, so I'm not familiar with it, but I think this is where it was last updated.
**Hanson Ho** 06:02 So, for the Kotlin API and SDK, this is something that JB has spent a lot of time looking at, so I don't know if, Jamie, y'all want to kind of talk about, you know, like, your thoughts about this, what you looked for, and, you know, how you… where we ended up.
**Jamie Lynch** 06:20 Yeah, I think we started out trying to…
like, implement, like, a Kobe team-based kind of, like, approach for context.
I think the tricky thing is, how do you manage that, where…
there might be an app where someone's using FedLocal in one place, and then there's another place where they want to use coroutine context.
So, I guess the state we've…
Settled on right now in the…
OpenTelemetry Kotlin is just kind of providing the building blocks that allow implicit context.
But not making an explicit choice of opting the user into… Any one of those.
is just really tricky, I think, to get right.
**Hanson Ho** 07:12 Yeah, there's nothing really automatic if you're switching between, you know, thread, like, the main thread and coroutines. And if you're talking about coroutines also, well, what if there's some, you know, other function being run on there? You know, it's gonna share. The whole idea of coroutines is, you know.
non-blocking and all that stuff. So, how do you automatically figure out where you wire things through and what is appropriate to kind of, put in? If there's two things running concurrently?
in the same context. I think there's already a package that allows, I think it contributes, that allows,
context propagation through, a coroutine context, but you kind of have to, like, use it as if you were managing it directly, saying, hey, everything on this coroutine, or this dispatcher, or I forgot what it's attached to, is effectively, like, a thread.
**JP Jason Plumb** 08:08 Do you remember what it's called, Hansen?
**Hanson Ho** 08:10 I think it's just called, like, Kotlin Coroutines or something like that.
**Mustafa Haddara** 08:12 I don't think it's in Contribut, I think it's in…
**Cesar Munoz** 08:15 At the Eastern Core.
**Hanson Ho** 08:17 Core. I think I added…
**Cesar Munoz** 08:19 I think it's an Android.
**JP Jason Plumb** 08:23 Oh, is it… you're saying it's in the Android repo?
**Cesar Munoz** 08:26 Ed.
**Mustafa Haddara** 08:27 I thought so.
**Cesar Munoz** 08:27 the Kotrang stuff? I think it's… no, I think it's Java.
Yeah. Let me see, I have the link somewhere.
**JP Jason Plumb** 08:36 this thing.
**Mustafa Haddara** 08:36 Oh, no, it's, the next block down. Extensions Kotlin, that thing.
**JP Jason Plumb** 08:42 Mmm.
**Hanson Ho** 08:44 This was done, I think, several years ago.
**Mustafa Haddara** 08:47 Yeah, so this works functionally. The drawback with this is that, like, from a developer perspective, the API kind of sucks, because everywhere you start up a coroutine, you've got to pass in the context explicitly.
**Cesar Munoz** 09:00 Yeah.
**Mustafa Haddara** 09:00 And so if you're like, oh, I've got this app with, like, 10,000 files in it, and a million lines of code, and I want to start instrumenting it, and everywhere you make an API call, you're starting up a new coroutine, you're like, oh, I gotta go find all of those places and explicitly pass in the OpenTelemetry context, which is just a pain, and no one wants to do it.
**Cesar Munoz** 09:22 Yeah, that's… that's the reason I created that issue a while ago. So, just… just for context.
quite well used.
**Hanson Ho** 09:32 In this phrase.
**Cesar Munoz** 09:33 The…
**Mustafa Haddara** 09:35 Yeah.
**Cesar Munoz** 09:35 I think about…
**Mustafa Haddara** 09:36 Right?
**Cesar Munoz** 09:37 Yeah. So, okay, so the issue that I was talking about in this Issue was.
That, let's say that you create a…
A span, and you set the context as current.
And then, at some point, you start a coroutine. So the problem is how to pass that context that you had set as current to the coroutine, because the coroutine will run in another thread, and the current context in Java is attached to a thread, so…
So, in order to provide that context into the coroutine, the upstream repo added this extensioned function, which is quite old, as Hanson mentioned.
And it works, but then for it to work, you will have to manually kind of convert.
the, hotel context into the coroutine context that you will pass into the new coroutine.
So, it's… it's annoying. So, I guess we could create an instrumentation that does that,
But we haven't. And I also know that When it comes to coroutines.
the bytecode that Kotlin generates, it's quite,
complicated. So, to be honest, I've been kind of like,
hesitant about creating that instrumentation, because I'm not sure how
stable it could be, but at the same time, I guess Catherine shouldn't change too much.
how they do stuff. So, anyway…
And this is the reason why there's another issue Where somebody mentioned, kotlin compilation, plugins.
where I remember mentioning to them that probably this context propagation
might be a good candidate for a Kotlin compilation plugin.
But I haven't heard from them.
Later, so… I think that's… that's the summary of it.
**Hanson Ho** 11:54 Well…
**JP Jason Plumb** 11:54 I think I… yeah, I think I do remember that issue, I gotta find it, but yeah, I remember this compile time plugin thing, but it was… it was the Kotlin compiler, right?
**Hanson Ho** 12:05 P?
**JP Jason Plumb** 12:06 Yeah.
**Cesar Munoz** 12:08 No, it would be… it would be… intermediate representation…
plugin. It's like an AST…
**JP Jason Plumb** 12:17 Whoa.
**Cesar Munoz** 12:19 So…
**JP Jason Plumb** 12:21 Yeah… Okay.
**Cesar Munoz** 12:26 Let me see… It was… it was tagged… it was tagged onto this one.
**JP Jason Plumb** 12:30 Yes.
**Cesar Munoz** 12:32 Yeah, that one.
**JP Jason Plumb** 12:38 K2 plugins.
Right. That was the context.
That was the… That was the… topic.
Yep, interesting idea. I think, you know, contributions welcome, open to help, and seeing what people might hack together. It's certainly a difficult problem, right, because
The entire… well, maybe not entire…
At least to me as a developer, one of the…
one of the reasons why you might want coroutines, one of the ergonomical concerns, is to be able to shed thread context, right? You're like, I want to not think about what thread I'm running on, and this is, like, purely… or not even thread, like, I don't want… I want to shed context about where I'm running.
And this brings that problem front and center, because it's like, no, we actually need to keep track, because we did something there that we're… it's, like, semi-global, and we need to keep track of it during the whole…
Flow of our execution.
Whereas coroutines are like, yeah, let's get rid of that, like, we're just doing these little bits and stitching them together.
**Hanson Ho** 13:52 We…
we kind of have to figure out first, before we're actually implementing anything, is what do we actually want? What are we talking about when we're talking about auto-propagation? Because proteins are just a black box of, hey, run this shit later. Don't let me worry about any of the details, just make sure it runs, schedule it however you want to.
And… that is…
completely opposite of saying, I want a well-known path, where my execution is modeled, on some construct that I could
tie things to. From which, when new,
executions happen, they are the origin of it, and then tie it back. And the whole tying it back is not a thing, because…
like…
you need a different construct, and… and not something that you can derive from… from execution, basically, which is what auto is about. It's about, if you're executing on this thing, then anything previous to executing on it is the parent. That is not finished. And I think… I think…
I don't know how you determine that when you have this black box. So, I think things could be done where you explicitly, manually, say, this whole dispatcher is effectively one context, and anything that runs within it is effectively
You know, my current.
And then, you know, launch stuff based on it. But you have to also make sure that the things you launch from inside that is running on the same dispatcher, or else…
**JP Jason Plumb** 15:25 Yeah, and to be clear, I mean, the goal here is to have spans that are nested, right? And if you start a span on some kind of user action, and it makes a client request on a different dispatcher.
**Cesar Munoz** 15:37 You know?
**JP Jason Plumb** 15:38 How do you stitch those two things together?
**Cesar Munoz** 15:41 Yeah. But I think, I think the…
the coppering extension that somebody added into the upstream repo.
I think it keeps track of the, context changes
inside an already created coroutine. So, if you…
change the cost… the context later on within the same coroutine, it will…
take care of it automatically. That's what I understand. Now…
**Mustafa Haddara** 16:09 Yeah, I believe that's correct.
**Cesar Munoz** 16:11 when… we need to double-check, but there is actually an issue that I think is quite… nasty about,
Passing that context to a coroutine, which is that
there are some coroutines that are meant to… to never end. So… so, for example.
I know it happens with flows, when you're collecting them. Sometimes, by the time you start collecting a flow, it just, you know, just stays
on that line, and it never ends until, you know, the quarantine ends, or the app ends. So, in those cases, I remember at one time asking myself, you know, what would…
what would happen with the hotel contacts. Essentially, it could probably get leaked.
After the span ends, or something like that, so… that's another issue.
**Hanson Ho** 17:08 would an execution, or rather the starting and stopping of spans, be based on, you know, suspend functions running and stopping?
like, so, like, I think we have to figure out a mental model of what we actually want to achieve here first, before saying, hey, how can we technically do it? I think saying… simply saying auto-propagate on coroutines, it's not specific enough.
**JP Jason Plumb** 17:37 Yeah… Yeah, and when I originally wrote this with span, whatever that one is,
I was not thinking about coroutines at all, I'm just like, someone's built a click handler, or they built, like, a little piece of business logic, and they want that wrapped in a span. And the ergonomics around doing that with the SDK right now are a little bit clunky, like, it's more lines of code than I think a lot of developers expect.
to create a span, give it a name, add some attributes, and then make sure you wrap it in a try, finally, to close it out. Like, that kind of… that…
that kind of block we see everywhere, but not everyone is comfortable with that or wants to litter it in their code, so if you had something as simple as an annotation, compressed at a build time, kind of automatically wrap that for them, is what I was thinking with this, and I did not have coroutines in mind. Coroutines certainly break this.
Or break this idea.
**Manoel** 18:33 Oh, man. Nice,
thread pool internally that may reuse threads as well, so if we try to do something automatically, we could attach spuns to the wrong thread, blah blah blah, so trying to do something automatic here is just wrong. I think the best we can do is to kind of document and provide a manual API
and tell, hey, pass the context here, that's going to work. If you spawn another coroutines inside of coroutine, you won't, unless you pass said context again. So it's like, give control.
The developer, I think, is the best way we can do it.
**Hanson Ho** 19:09 Yeah, manual attaching of child spans is really the only sane way of doing this.
Because execution is also, you know, not, guaranteed on these coroutines.
So, you know, a host of pro… I mean, these are… these are… these are actually problems with mobile anyway, with the fact that, you know, execution isn't just, you know, one process, one way of doing it, there's, like, a bunch of things that…
start. Code genes adds, like, an extra layer of wrinkle that… that exists, I think, previously. Like, previously, you're also assuming that no other thread is using, you know, or…
The main thread, can only do one thing at one time, which…
isn't really true. Well, it is true, but it isn't…
for modeling, like, long, long-running, you know, spans. It's… Not exactly true.
So, is there a resolution for this? Like, should we just, say, come up with a theory, or…
Because I think, I think… There should be an answer for this, whether… even if it's just, hey.
automatic doesn't make sense, because A, B, C, D, E.
And if you have a solution or a suggestion of explicitly what API you want to use. So, something like what Century has, or what the existing Kotlin extension has, but, like, with an improved API that gets stuff
something automatically, I think that's reasonable. If you can say, this is… I can… I completely control, you know, this dispatcher, anything that runs on there is, like, as if it's a thread. Then, you know, you can say.
Anything that runs on this.
Propagate the stuff as if you're running on a thread.
**JP Jason Plumb** 21:05 I think Manuel brings up a good point about just document, like, documentation. We haven't decided yet, but I think seeing an example, and then building documentation around that example would be a good starting point.
**Manoel** 21:18 India.
**JP Jason Plumb** 21:19 At least that's what I would like to see, is, like, someone say, like, look at this coroutine stuff I built, here's what the manual API to propagate context in that scenario looks like.
And then…
leveraging an example to build documentation, because a user coming in today would have no idea how to get started, so…
Yeah, I like that idea about
documenting, like, agreeing, like, we still would need, like, agreement on which technique and which APIs to use, but…
Okay.
**Hanson Ho** 21:52 Can you create an issue that is just about documentation, or transform any existing one?
**JP Jason Plumb** 21:58 Yeah, I mean, I would be happy to close this one.
If we think there is… if we think it's more problematic to try and automate that for someone.
**Hanson Ho** 22:08 No, I think this is good.
**JP Jason Plumb** 22:09 Yeah, this is good. Yeah, so maybe a new issue, or one of these other ones, like… which one?
Like, maybe…
maybe a summary on this one, which is, like, we want to probably do it with manual API.
And document… document it.
**Cesar Munoz** 22:27 By the way, there's an example here.
**JP Jason Plumb** 22:32 Aware.
**Mustafa Haddara** 22:34 This one, though…
**JP Jason Plumb** 22:37 I haven't exist.
**Mustafa Haddara** 22:38 The person looks like they're already using the extension, and they're saying the extension's not working for them.
**JP Jason Plumb** 22:43 Is that what they're saying?
**Hanson Ho** 22:45 Oh.
**Mustafa Haddara** 22:46 Yeah…
**Hanson Ho** 22:47 then it's a bug on the extension.
**Mustafa Haddara** 22:51 bug on the extension maintainer, yeah.
**Hanson Ho** 22:55 Then it shouldn't be on here, because that's not where the repo is.
**Mustafa Haddara** 23:02 more than… who's using… like, why is the Kotlin extension in… OpenTelemetry, Java, Contrib.
**Hanson Ho** 23:11 I think because people are using this for backend stuff.
**Mustafa Haddara** 23:14 Yeah.
**JP Jason Plumb** 23:17 I didn't know this example was here, this is cool.
Okay.
So… Which of these is the extension method? Is it this thing?
**Mustafa Haddara** 23:55 Yeah.
**Cesar Munoz** 23:56 Yeah.
**Mustafa Haddara** 23:56 So, there's, like, context.current is the open telemetry current context, and then as context element turns it into a Kotlin context.
**JP Jason Plumb** 24:05 Yeah, yeah. Confusing…
**Hanson Ho** 24:07 Cogene context.
**Mustafa Haddara** 24:10 I'm sorry.
Well, in coroutine context, yeah.
Oh…
**JP Jason Plumb** 24:17 Okay, so they're doing this, and…
Okay.
Yeah, that does seem like a… that does seem like a bug, then.
**Cesar Munoz** 24:34 I'm not sure if it… we'll have to check. The thing is that… So… They're trying to propagate context
Over to… My understanding, they're trying to propagate hotel context over to OKHTTP…
threads, but the OKHTTP threads are…
are not handled by… by us. It's… it's… it's all managed by OKCTP, so… if…
You know, in order to pass the context.
it's probably that they are creating, you know, an OKHTTP request within a coroutine.
Within a span, and then, you know, the context doesn't…
goes through the… to the coroutine, and that's why they don't get it. That's probably it, but…
**JP Jason Plumb** 25:31 Oh, interesting. So even though they might be bringing over the context from the parent span into their coroutine, the context, the open telemetry context, is still lost by the time it gets to OKHTTP, is what you suspect.
**Cesar Munoz** 25:45 Well, I mean, if they bring it as they say there, yeah, but it's not… it's not a whole picture, so…
**JP Jason Plumb** 25:52 Yeah.
**Cesar Munoz** 25:53 I'll ask, I'll ask a follow-up question.
**JP Jason Plumb** 25:55 I think it's reasonable to ask them to give a more, full example… example.
Like, can we… can we actually see a working…
Repro case, that would be great.
**Hanson Ho** 26:08 I think that's a reasonable thing to ask.
So OKHTP first queues it, and then threads release, and then when it runs, it's picked up by the thread pool, or by default at least, and run on whatever free thread it's on.
there's a disconnect between these two. So even if you have the context in the first thread that's queuing, the context that runs, or rather, the thread that runs, could be
Oh, or is usually from a different thread pool.
So… but yeah, a nice example would… would… would work, would be nice, would be good, because we're talking about, I think.
3 different… potentially 3 different threads and 3 different things that could potentially store context here.
**JP Jason Plumb** 26:56 complicated.
It would be good to know, yeah, if it's specifically coroutines. I mean, I took that at face value, that the coroutines are what is breaking it, and if you're not using coroutines, then the HTTP instrumentation works. It'll hopefully correctly propagates context. I think we've demonstrated that.
So it seems…
**Cesar Munoz** 27:18 Yeah, but we'll need to see the full example.
**JP Jason Plumb** 27:21 Yeah. Are you gonna ask for that, Cesar?
**Cesar Munoz** 27:24 Yeah, I'll follow up there.
**JP Jason Plumb** 27:26 Cool.
**Cesar Munoz** 27:27 You know, Kurt thinks, now that we're talking about it, I think it sounds quite similar to what
In theory, I haven't tried them, virtual threads should do in the newer Java versions.
Kinda looks like it.
Good fight.
**JP Jason Plumb** 27:45 Wait, are they still called fibers?
I forget.
**Cesar Munoz** 27:51 Not that I'm aware of.
But, so I'm curious what the Java state will do.
About those, maybe it's something we can leverage.
**JP Jason Plumb** 28:02 Yeah, I don't know that there's a plan yet, but they…
They do have the luxury of being able to
like, change bytecode in the JVM on the fly, so…
That's probably what they will do.
**Hanson Ho** 28:19 Also, I would assume people know they're working with these virtual threads, right? Like, if they're creating one and using one, they're bound to this virtual thread context, and that should be propagated no matter what the execution thing is. I think here is that there's nothing you can bind it to that is specific enough that you could say nothing will…
nothing will… nothing will disrupt the execution, and, you know, it is persisted as it goes through the workflow.
So… I think, virtual threat. From the brief description that I read, it…
Seems like an implementation detail, but the API is still there, to expose the concept of it, whereas, I think, CodeGene's… not… not quite. It's like… it's like tying a context to a thread pool, which…
Would be silly if you brought that up.
**JP Jason Plumb** 29:18 Yeah, it's not really what the user wants in most cases.
**Cesar Munoz** 29:23 Now, it's still, you know, coroutines aside.
**JP Jason Plumb** 29:26 You know, probably the.
**Cesar Munoz** 29:28 Because this is another topic, the width span annotation.
I mean, does that mean… I mean… Let's say that we…
decide not to add automatic propagation for coroutines. Does that mean that we still… that we also have to, you know, not add the width span stuff, even for the non-corotine?
**JP Jason Plumb** 29:51 I was asking… Yeah, I asked that same question, because I think… I think there's use cases for both. I just think that someone using the withspan… like, if this existed, and we could do this, a naive user might expect that to be compatible with coroutines, and it would not be right now. We'd have to have this other strategy.
And you're kind of mixing modes then, right? You're mixing auto-instrumentation, build time auto-instrumentation.
With probably manual instrumentation to track the coroutine context.
Yeah. Those two things should play nicely.
But the person naively throwing with span on some methods might not understand that, and we would want to help to make that clear somehow.
**Cesar Munoz** 30:35 And we'll definitely get some issues open because of that, so…
**Hanson Ho** 30:39 Yep.
**Cesar Munoz** 30:40 fusion.
**Hanson Ho** 30:40 At the same time, somebody who would start a span before a method call and stop a span after a method call would fall into the… this is… Totally.
**JP Jason Plumb** 30:47 sugar, so… Totally, yeah, we, I mean, yes.
There will be users that make mistakes, yes.
No matter what we do.
**Hanson Ho** 30:57 I think this is individual… I think this is valuable, and I would say separate from… from the coroutine stuff.
So,
you didn't have an implementation, right? This is just the issue, to say, hey, we should do this, right?
**JP Jason Plumb** 31:12 Exactly, yeah, I mean, it's a year and a half old.
**Cesar Munoz** 31:15 It's a PR.
There's that BR for you?
**Hanson Ho** 31:18 Cool!
**JP Jason Plumb** 31:18 Is there?
**Cesar Munoz** 31:20 Yeah.
It's marked as draft.
**JP Jason Plumb** 31:24 Oh, yeah.
**Hanson Ho** 31:25 Okay.
Cool. I mean, we have this, we have this in the Embrace, API. It's a function itself, but it could easily be, you know, an annotation and byteco-instrumented to change to a function, but…
It's nice, you can just put it as a lambda and say, hey, there's a span.
Biggity band.
**Cesar Munoz** 31:46 It's probably… and it's probably worth then… Okay, so it sounds like…
We might want something like this, but then probably should be very clear in the docs, or wherever
That if there's a coroutine being launched within that method, that won't… then it will be kind of ignored, or, you know, it won't be taken into account.
For this bank credit with this, yeah.
**JP Jason Plumb** 32:09 Yeah, and that's kind of… that's kind of a more blanket statement, too, right now, at least, that if…
If it's launched from anything where you have a span context or an open telemetry context.
That it's not automatically propagated yet.
**Cesar Munoz** 32:25 Okay.
**JP Jason Plumb** 32:26 Yeah.
**Cesar Munoz** 32:28 Cool.
**JP Jason Plumb** 32:35 So, originally we had hoped to do, an RC1 in October, and I punted that effort, so let's talk…
more about an RC.
Because we're in November, and also…
Due to KubeCon, we will likely cancel next week's meeting, so…
We should expect to not meet next week.
I hope it will be removed from the OpenTelemetry calendar. I think they will probably cancel almost all SIG meetings for that week.
And then the follow-up following week, looking at the calendar…
Yeah, that'll be fine. So we'll meet on the 18th, okay.
Let's just put… let's put a note up here.
Oh, and it's election day, and I haven't voted. Whoops, I should probably do that.
**Cesar Munoz** 33:52 Sir, just to confirm that… Okay, it's the same wig, so…
So probably we just have to skip just one, okay.
**JP Jason Plumb** 34:02 Yeah, that's what I meant to do, yeah, okay, just so anybody that jumps in here will know, and not be surprised by the empty, empty turnout.
Alright, so back to release candidates. So, initially we said October, hoping to do our first RC. I pulled that back because of this, blog post. Has this landed?
I think it probably has not.
Alright, so it's still being worked on. Only the first 40 comments.
Oh man, okay, look at this, 102…
Alright, so there's a lot of excitement from other groups, not just Android, about this, about this idea, I guess. This is a… wow, I didn't realize it was up to 102.
Well, I'm not gonna read.
**Cesar Munoz** 34:53 That's impressive.
**JP Jason Plumb** 34:54 anyway, but there's a lot of back and forth on this. Cool.
I think I had a takeaway to ask how they were planning on handling this in Java.
And I think the answer I got… let me see if I can pull up Sig Notes so that I'm not making stuff up.
I think the answer is weird.
No, that's not the right thing.
Do any of you use Outlook?
Do you have to use Outlook?
**Cesar Munoz** 35:34 Not right now. I used to be…
**JP Jason Plumb** 35:37 It requires… it requires so many more steps to… to, like, do… to find and do the thing you want.
like…
**Cesar Munoz** 35:43 Hmm.
**JP Jason Plumb** 35:46 This… this is the year where Splunk is adopting Outlook.
Anyway, so I think there was a talk about, last week, about… this…
Right, so some of… some of the discussion, was around…
Experimental features being disabled or enabled by default?
What that would look like in declarative config, because we're thinking a lot about declarative config over there.
And the idea of, in addition to being
Just stable or… or not, stable or alpha, that there could be some threshold levels.
So this is an ongoing discussion that's happening, I think, in this spec call.
So that alphabet, and you could opt into, like, your minimal… minimum threshold level.
But at the end of the day, I think what this… like, assuming that this blog post lands in some way, and assuming that… assuming that the spec gets updated.
I think what that means is that…
if you… if you choose to use the OpenTelemetry Android agent, and we have marked it 1.0 stable, like, non-RC,
Then, you should not be, including… we should not be, or you should not… the user should not have an expectation
That they will be including experimental or alpha components by default.
I know. So that's a lot of code that we currently include that would have to be marked
that would have to be more stable. Or, you exclude it all, and you allow them to opt into it. Meaning…
if you wanted to make it very convenient, then something like the initializer…
Would have a property that says.
Give me everything, and then, like, give me everything would be the opt-in, and we could kind of do what we're doing today.
Which, to me, is a little bit… ridiculous and kind of laughable, because…
You have people that are leery, that don't want to include, or are hesitant to adopt something that's not marked stable.
Yet, when it is stable, there's… they would be comfortable including
unstable components? Like, I don't understand where that line is, and I think that's how you end up in this threshold discussion. So…
There's still some TBDs.
I'm curious what it would be like for us to decide from… Same.
From the initializer…
Which components might be low-hanging fruit for us, if any?
to mark as stable. So…
Of all of the things we include, I don't know, there's, like, a dozen instrumentations.
and disk buffering, and a few other features. Do we think that any of those… Might be low-hanging fruit.
To bring with us as part of a stable release.
**Cesar Munoz** 39:09 I have a question.
**JP Jason Plumb** 39:10 Yeah.
**Cesar Munoz** 39:12 Is there… By not including non-stable Artifacts within a stable artifact.
Does that mean… like… not exposing APIs from those non-stable artifacts, or just not… just not adding them
Because we're not exposing a lot of APIs from non-stable artifacts, and… That's right.
**JP Jason Plumb** 39:45 I… I don't think the wording specifically calls out APIs or interfaces.
I think the blog post wording, which I've lost…
I think the blog… man, it really does take longer to load that with all these comments.
I think the wording on the blog post…
Let's see…
This might have been rewritten a few times as well, so I could be…
behind here. I think this is the one that I was commenting on, so…
Stable components must, and it's not capitalized yet, because this is not spec, this is a blog post, must only enable other stable components by default.
So that doesn't address API… that doesn't differentiate between API, it just says, if you're gonna include something by default, you should only include stuff that's stable.
A new global config shall be introduced that allows adopters to choose a desired minimum stability level. This is kind of the threshold.
With a default value of one of these, stable RC or beta.
So…
I… I mean, I'm a… I'm an anarchist, and I think that software is always unstable, and if you think a SEM conv is actually meaningful, you're deluding yourself, and everything's prone to breaking at all times, forever.
But I also understand that I'm a minority in that thought, and people crave stability in their lives, so it's odd to me that we're creating a situation where I think a lot of users that want functionality are going to just have to opt into
Alpha or beta, like, stability levels by, like, to get stuff to work, to get work done.
But they're okay opting into an alpha, but they wouldn't have adopted if the main artifact or main…
Agent wasn't marked.
stable.
**Cesar Munoz** 42:11 That's weird… that's weird to me. It seems contradictory. Yeah, but I… maybe that's…
**JP Jason Plumb** 42:16 The reality? I don't know.
**Cesar Munoz** 42:18 And I also think that… For Android will be quite…
Because it looks like the, solution that they're proposing to this is to define some sort of flag
Where users can define the levels of stability that they want to include, or enable.
**JP Jason Plumb** 42:36 That's right.
**Cesar Munoz** 42:39 But,
for that to… to be possible at runtime, it means that you will still, at least for Android… at least for Android, you will still have to
I have the library bundled with all of these non-stable artifacts.
Still. I mean, they will be disabled.
Probably by default, but they're still gonna be there, so… Yeah.
you know.
**JP Jason Plumb** 43:08 Yeah, I, you know, I think there's still some TBD on how this lands and what it looks like in the spec.
And with that, I have not…
heard any additional pressure about making Android stable. This idea originally came from some GC pressure, and I'm using that term very liberally, like.
it was purely, like, relaying stuff from the field, and people saying, you know, I've heard customers asking about Android, and they just say it's unstable, like, it's not, you know, it hasn't been marked stable yet, so they're hesitant to use it in production.
And I'm like, cool, we can get there, we can market stable, people are using it in production, what does it take? And so that's when I started on this path. And the timing was just pretty bad around this.
I think that maybe we could use some…
GC or TC guidance around this, probably more GC than TC, because this seems mostly, like, putting names on things, and if there's confusion about metadata or whatever, we can get help, but, like.
I don't know, I…
I'm a little bit lost on this, like, it seems like we have two conflicting goals. One is to create stability, and one is to declare a stability level that people can opt into and out of, and…
If it's just… if it's just declaring stability the initializer.
And allowing people to opt-in like they do today, to get the stuff they need.
to get the job done, then fine, we… I think we can build that.
It seems a little goofy to me.
But I want guidance to make that clear that that's what… that's the direction we should be going, instead of holding back and really making everything robust and stable, or not…
calling it stable at all. I'm cool with all of those options, I just want to know…
from the broader community what they think, and from the GC, like, what the guidance is. I'm curious, what do you all think, too.
I'm very flexible on this, but what I don't want to do is create a bunch of work for ourselves, unnecessarily.
**Cesar Munoz** 45:09 Yeah, well…
**Hanson Ho** 45:10 Well, go ahead.
**Cesar Munoz** 45:13 Well, mine is gonna be quick, it's like, I… I… it would be nice for us to go stable, even if it's only one module, because…
you're right that a lot of people won't use Auto Andre just because it doesn't have
you know, a stable version. So… so that will help, you know, Hotelandry grow quicker, so… Let's see.
Sorry, Hanson.
**Hanson Ho** 45:37 Yeah, I think for me, it's like we're trying to…
Have our cake and eat it too.
It's like, hey, we're stable, wink! And then the people who are naive enough to believe that first statement, didn't see the wink. The one who sees the wink would be like, oh yeah, we can just use, you know.
put the thing to beta, and basically opt into beta components, rendering the previous stable declaration, you know, a bit… a bit…
watered down.
I don't think we're gonna be in the same… I don't think our situation is unique. I hope, at least. I think…
**JP Jason Plumb** 46:15 So, in fact, like, the Java instrumentation, they have 200 instrumentations and none of them are stable.
**Hanson Ho** 46:20 Yeah, so… So, I would almost… I would almost…
see what happens in the bigger wave, and kind of just go along with it, because, like you, I have no preference. I think the stability thing just seems like a reasonable marker, regardless of whatever light pressure the TC and GC may or may not have been putting on. Just because it works, it's functional, it…
you know, It, it, it is, like, you know,
battlefield stable, if nothing else. So we should be at least be able to declare that, and not have to have folks, you know.
work around and run around, but if we have to, like, say, hey, you have to opt into this to get the extra instrumentation, fine. I don't care, whatever.
So yeah, again, similar to you, I have… I want this project to be stable, I don't care about anything else.
Or rather, I would go with what everybody else is going with.
**JP Jason Plumb** 47:21 So we, we now… Sorry, go ahead.
**Mustafa Haddara** 47:24 I was gonna ask, Jason, so first of all, like, what…
what is the Java SIG gonna do? Have they… have they said? And then, second of all, like.
what is preventing us from calling all of our instrumentation, quote-unquote, stable 1.0 as they are today, and then if we decide we need to change the APIs, we just do a 2.0?
**JP Jason Plumb** 47:47 Yep, so those are both good questions. I think the answer about what's the JavaSig gonna do has not been decided yet. It was kind of a bad time to ask, because Trask missed that meeting. So, you know, Trask will have additional say in that, but I think there's a strategy being formed.
I think it will probably be…
to call a small subset of instrumentation stable, like, and mostly the ones that have stable semantic conventions, so, like, HTTP, OKHTTP, and a few others, possibly database.
call a small set of those stable, all of the other ones will remain alpha, and you have to opt in with this… with this flag. I think that's what they're gonna do, don't hold me to that, but I'm… that's what it sounds like.
The second question being, what's preventing us from just marking everything 1-0?
The short answer is nothing. We have agents, we, the Android SIG, we have agency, and we can do that, if we so choose.
Now, this blog post is suggesting that there will be some stricter requirements, and they're… they're expanding
the scope of what it means to be stable, but right now, we could do that. The downside in doing that is that the moment we declare everything on our repo stable, someone's going to want to make a change, and it's gonna be a good, important change. We're gonna have to do 2.0, I think, on pretty short order.
And we will still need to maintain a 1.0 branch for some amount of time.
And I think the convention elsewhere has been, like, 6 months.
But usually not with new features, usually just with, like.
bug fixes and security patches. But that's a non-trivial amount of work to maintain two branches, I think is the downside to doing that.
**Mustafa Haddara** 49:35 Yeah, of course.
**Hanson Ho** 49:38 Also, there are probably features and packages we don't… that we don't feel is comfortable to declare, you know, 1-0 slash stable.
**Mustafa Haddara** 49:47 Sure.
Yeah, no, it's like, the direction I'm thinking in here is, when I read that blog post, I think, okay, they're talking about
bug stability and, like, functional stability, and when we're talking about stability here, we're talking about a lot of the time, not always, but a lot of the time we're talking about API stability and interface stability, which isn't even exposed to the general, like, public, because we're giving them the agent and initialization API.
So it doesn't… almost doesn't matter if those APIs internal… internally change.
**JP Jason Plumb** 50:19 That's an interesting read.
I can tell you, at least on the Java side, from core and instrumentation, they talk about the APIs all the time.
And that's the main thing, like, if you… if you propose an API change right now.
**Mustafa Haddara** 50:32 to core.
**JP Jason Plumb** 50:33 that's breaking, it'll straight up get rejected. Like, it will show up in the API comparison diff.
And they won't approve it, like, it… it wouldn't… it will be under scrutiny instantaneously if you try and…
**Mustafa Haddara** 50:44 Yeah, but that's the core API. I'm talking about, like, an API change to one of our instrumentations, or an API change to how we configure our disk buffering, or whatever, like…
**JP Jason Plumb** 50:56 I'm sorry.
**Mustafa Haddara** 50:56 Ditch.
we call it through our agent, and we expose it through the agent to our users, right? And so if the agent API is stable.
Our users don't actually care what the interface to get to disk buffering, like, internally, is.
**JP Jason Plumb** 51:14 It's true, but the way I read that as well is that if disk buffering is not marked stable yet, then we would be including and using an unstable component. If we use disk buffering by default.
Which we wanted to, right? We think it's a good feature that people benefit from having turned on.
**Cesar Munoz** 51:33 Yeah, but I guess it will be important to then define what is it that they mean by stable, in the sense that stable as in behavior, or stable in API.
If it's stable in behavior, I agree with what you said earlier, that there's really no…
no piece of software that's, you know, perfect, so it's stable in behavior, I don't think it's… not even stuff that's market stable can guarantee that, so…
If… it would be nice to… Have some…
feedback from someone from the… from the GC. I don't know if they can join this… this meeting?
**JP Jason Plumb** 52:15 I think the timing is bad, but I will… I will reach out and try. I'm gonna wait until KubeCon passes, maybe we'll get some clarity there, too, face-to-face about this stuff.
But…
Yeah, I will… I'm willing to ask for some guidance, some additional guidance around this, because it's… it certainly makes things complicated. To your point, Cesar, I bet you several of these 102 comments are also asking for clarity about the definition of stable.
I bet you.
**Cesar Munoz** 52:45 Most likely, yeah.
**JP Jason Plumb** 52:46 We have one, though.
**Cesar Munoz** 52:48 Nope.
**JP Jason Plumb** 52:49 Go ahead.
**Cesar Munoz** 52:51 Well, I just wanted to mention as well that
After the, latest API changes that I added to this buffering, I am fairly confident to market as stable right now, if it's needed.
But, I mean.
Yeah, that's all I wanted to say. But apart from that, I mean, we also have, you know, instrumentations and stuff.
Marked as stable, so… Yeah, it wouldn't be the only issue, but yeah, I just wanted to mention that.
**JP Jason Plumb** 53:22 Yeah, the challenge in contribib, Java Contrib, where disk buffering lives, is that if you… if you… when you need to make a breaking change, we can't…
Do a major version bump for just one module.
**Cesar Munoz** 53:39 And so you have to rev all of Contrib, which is, you know…
**JP Jason Plumb** 53:42 Laughable. And…
I like the irony of, like, looking at versioning a stability document, and it has a clickable link to the word stable. You can click on that and see what it means.
So… Here are all of the defined stability levels in OpenTelemetry.
And stable means it's just available for general availability.
breaking changes including config, and the output, which is… that's pretty vague, but, like, does that include semantic conventions? I think it does.
Are only allowed under special circumstances, wherever possible.
should be given prior notice. So, you know, I don't know if… here's, like, API.
**Cesar Munoz** 54:31 It mostly talks about breaking changes, which to me talks about the API, then, API stability, looks like. This is what it's referring to.
**JP Jason Plumb** 54:41 Yeah.
**Cesar Munoz** 54:41 Which, actually, thanks to Jamie's changes to the initializer with DSL,
It's not even an issue if we wanted to change that DSL in the future.
Right. Because, you know, the compiler won't complain, so…
**JP Jason Plumb** 54:59 Yep.
**Cesar Munoz** 54:59 I would say we're… I mean, if it's about API stability, I think we should… we should go stable as, you know, as… as we planned initially, but, you know.
**JP Jason Plumb** 55:09 And then we make all of the instrumentation and other features opt-in.
Basically, it's every feature is opt-in, then.
Like, you're gonna be passing a flag.
To the initializer in some way that says, enable everything.
**Cesar Munoz** 55:33 I don't like that blog post.
**JP Jason Plumb** 55:35 Yeah. You should comment on it.
**Hanson Ho** 55:38 Yeah, we need a couple more comments on that. It's only got 100, so let's make it 200.
**Cesar Munoz** 55:44 It's kind of silly, because it's just gonna… I mean, I feel like we're just gonna shoot ourselves in the food.
**JP Jason Plumb** 55:52 Well, I appreciate what Austin is doing. I appreciate the desire to get graduated as a CNCF project, and I think that's part of this.
I think as… I mean, they've been very… they've been very transparent about that too, which I appreciate, but it's… it's a… it's a hurdle, like, it's a big road to get to graduation, and they're having to make some…
I don't know, some concessions or some changes that is not gonna work for everyone, so…
It's important. I'm gonna call time, because we're about out, and we could probably talk about this for another hour. So I will take an action item to get some additional clarity and guidance about this. I agree that we want to release an RC or a 1.0 of the initializer.
And we should continue that.
be.
Right.
Alright.
Thanks, everyone.
**Cesar Munoz** 56:54 QCon. Thank you.
**JP Jason Plumb** 56:56 Be in 2 weeks, if I don't see you next week.
**Cesar Munoz** 57:00 Things.
**JP Jason Plumb** 57:00 Bye.
