SIG: Event WG
Date: 2026-03-17
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/tNfe4TsuV3VaIrMn-DbUFRJnkBE_vVpJLrC0E-HfKK3poMbdVy31r1bNA8kHJPEF.ogW244zxp1XX9UtJ
============================================================

## Zoom Recording Transcript

**Pellared** 01:08 Cliff?
Well, welcome.
**Liudmila Molkova** 01:11 Hello! Hi, Robert.
**Pellared** 01:13 Hello, hello.
**Liudmila Molkova** 01:15 How are you?
**Pellared** 01:18 I thought that… I thought that stress is making the agenda, and probably it was you, right?
**Liudmila Molkova** 01:24 Oh, Trask?
Committed.
**Pellared** 01:28 Excuse me?
**Liudmila Molkova** 01:29 He's coming, at least.
Christ.
**Pellared** 01:34 Okay, so let me add… view here.
**Liudmila Molkova** 01:39 You're coming to KubeCon, right?
**Pellared** 01:41 Yes, I am.
**Liudmila Molkova** 01:43 Awesome. See you next week, then. Are you ready?
**Pellared** 01:48 Like, travel-wise, almost, I'm all… I'm also… the one thing which I also need to do, probably, is to consider, maybe I just should be worth booking a ticket to the Rembrandt's House Museum.
some… I'm going to Van Gogh Museum.
Yeah, not sure if… I would just need to see how much… how many times do I need to have to visit the Rembrandt House Museum. So, yeah, but apart from it, I need to prepare my presentation. Basically, it will be almost a V2. It doesn't make sense to have the same presentation.
Hello, Trask.
**Trask Stalnaker** 02:28 E.
I will miss you all next week.
**Liudmila Molkova** 02:33 You would not. You will be happy quietly doing work with her.
**Pellared** 02:39 Without trying to travel, you know.
For me, it's the same time zone, so it's weird now, you see?
**Liudmila Molkova** 02:49 I miss the quiet time I get when everybody goes to KubeCon.
Yeah.
Whoa.
**Trask Stalnaker** 03:01 Alright.
Let's see, I think I put something on the agenda.
Robert, thank you for making that blog post, that is awesome.
**Pellared** 03:20 Thank you, thanks a lot for your help.
I thought that I will not make it before Kipko, to be honest.
**Liudmila Molkova** 03:34 It didn't get any, any… Angry comments yet, did we?
**Pellared** 03:39 No.
I'm not looking at GitHub notifications because I worked on a presentation, so maybe that's why I missed many comments.
Let me check.
**Trask Stalnaker** 03:54 Let's reorder these… This was… I didn't read this carefully, but I mean, I do think it's an interesting… Kind of area of… in general… Well, so this would be… We're recommending capture it as request, the name as request, and this as a complex Object.
**Liudmila Molkova** 04:35 Yes, I think with caveats.
The first caveat is… if… we… understand, like, if the subject is something arbitrary, like fubor.
we would not… we should not try to serialize it, but if we… we can have… we have a document about mapping. So, like, if it's, some sort of a collection, then we can explore the types in the collection if it's a map. So, map collection primitives, that's what we would map.
**Pellared** 05:10 I was discussing it today with Joskyokovic, who is the maintainer of OpenTremity.net, because they're also… the bridge API even does not exist, or Lox API does not even exist in .NET so far.
So, there are people who want to stabilize it, so it was also one of the things… things which I shared. And I also said I remembered that when we were working on complex attributes, I remembered your prototype for Python, that you add some, you know, kind of log API structures.
To not use reflection, just, you know, like, type checking.
To make it performant. So you would use, for the complex stuff, you would just, you know, use this log API or whatever structures.
So that's what I shared.
**Trask Stalnaker** 05:55 Okay, I think Jack has a prototype, a similar… prototype here… Where, yeah, it doesn't do the whole reflection… thing, it just does specific, like, lists, maps.
primitives, nestings…
**Liudmila Molkova** 06:24 I think the .NET logger already does it, but with some very limited set of things.
And they… there is a… the issuing the runtime to support proper structured login. I'm trying to find it, but see Job.
Leave the guy opened.
**Trask Stalnaker** 06:42 Yeah.
**Liudmila Molkova** 06:43 the issue on the .NET report, they will get help.
**Trask Stalnaker** 06:50 Cool.
Do we want to try to… Resurrect context here… Where did we leave this the last time, Robert? Do you remember? I think you were… Sort of agreeing that maybe we only need… Let's see…
**Pellared** 07:31 I just think we have a summary.
Around the last discussion.
Example, yeah…
**Trask Stalnaker** 07:53 Fantastic notes here.
**Pellared** 07:55 Yes.
**Trask Stalnaker** 08:03 The instrumentation library… Yes.
Log Bridge. Oh, yes, I think I remember the… The thing that we were getting at was… We would… ex… we wouldn't expect the instrumentation… I wasn't, at least, I wasn't expecting the instrumentation library to emit logs using Log4J.
I was expecting the instrumentation library to use the OpenTelemetry Log API.
**Pellared** 08:48 For open telemetry instrumentation, I agree, I think you're right I'm more concerned about Other instrumentation libraries?
What comes to my mind is, for instance.NET, which uses iLogger extensively.
And I'm not sure how the design would… look there.
it's just… I'm just here, like… and the reason, because I think it's an unknown, how it will work, is that I wanted to have this kind of… Safety measure to have it separated.
Also, in the go.
I think also people would rather use the logging API, which we are… which we are creating.
But… there's also S-Log, which is part of the standard library, and we have a very good performance breach for it, so I also see possibilities that it could be used.
But then, if they use the bridge, they have no way So… say what is the instrumentation library attribute, I think, in the scope.
What'd…
**Liudmila Molkova** 09:55 You even know it.
**Pellared** 09:56 At this point.
It is possible, because we have an instrumentation attributes, scope attributes option to add… Like, handcrafted, so people could add it.
On their own.
**Liudmila Molkova** 10:12 Wait, so I'm writing a log breeze, so either I'm somebody is using to make the logs API from up on telemetry.
Or they were using log bridge, and then the log bridge is instrumented.
the log bridge… sorry, the log facet is instrumented by the log bridge. In the log bridge itself.
In the OpenTelemetry part of it.
do you even know which library called into the logger? You don't.
**Pellared** 10:44 No, you don't. Someone would need to explicitly set some configuration that I'm instrumenting this. Somebody would manually need to use it.
**Liudmila Molkova** 10:53 And this is the logar scope, essentially. This is the instrumentation scope name, you were saying.
**Pellared** 11:00 Right.
**Liudmila Molkova** 11:00 comes from.
**Pellared** 11:02 Yes.
Should be.
**Liudmila Molkova** 11:06 should be. If they didn't put it there, it… Do we care?
**Pellared** 11:15 Yes.
I remember there was also discussion, That the instrumentation scope.
It's more granular, the Instrumentation Library name, because there are namespaces inside.
the inside. So, yeah, so the scope could be… More… have more selectivity.
**Liudmila Molkova** 11:44 Yeah, it's encoded, ideally.
**Trask Stalnaker** 12:05 So, are you comfortable, Robert, with Adding these to… attributes… would that… Still give you a… Because I think the reason where you were concerned about adding these two .
**Pellared** 12:26 I can sleep, that's… I can start with either… we can start with these ones as a development, if no one will say that there's a problem after… I don't know.
A year or something? Then it means that, you know… At least we'll minimize the amount of attribute… of attribute names.
**Liudmila Molkova** 12:50 We should have some means to say they are instrumentation scope attributes. We don't have any.
**Trask Stalnaker** 13:03 Other than a note.
**Liudmila Molkova** 13:05 Rather than the note, yeah.
**Pellared** 13:06 that Trask, you want to use instrumentation library name for the bridge name, right? And version. That's your proposal.
In context of locking bridges.
**Trask Stalnaker** 13:18 Yes.
**Pellared** 13:20 Okay.
You're the… I think we can start with it.
What's you guys.
**Trask Stalnaker** 13:32 Cool.
I will send a PR.
**Liudmila Molkova** 13:38 Yay!
**Trask Stalnaker** 13:45 Let's see, following up on Robert's blog post… And I know we were going to present to the spec Sick, probably soonish.
the event stuff.
What do we… I think is the next step.
Or a span event deprecation.
**Liudmila Molkova** 14:24 Robert has a draft, right, in this pack.
**Pellared** 14:31 Yeah, but… the draft… If I remember correctly, To make it deprecated?
We agreed that some parts of the semantic convention will need to be stable, Regarding recording errors?
Maybe I'm wrong.
There was also a discussion about… Adding this set… error… on… Pans, similar to what we have on logs right now.
**Trask Stalnaker** 15:07 So, what was that?
**Pellared** 15:08 So stuffy.
I think during the last discussion, but it was only, like, surfaced, could you scroll down a little?
Yeah, the set exception for… add something like span and with exception to the trace API, but I'll post… I suggest postponing it as late as possible.
**Liudmila Molkova** 15:31 It doesn't seem like a blocker for anything.
**Pellared** 15:34 Yep.
**Trask Stalnaker** 15:35 Yeah, it feels like…
**Pellared** 15:36 Right.
**Trask Stalnaker** 15:37 Convenience.
**Pellared** 15:38 Yup.
I would rather first work on stabilizing recording exceptions, whatever is there.
Thank you so much.
I also remember one concern coming, I think, from CGO.
that we don't… I think we do not have a solution.
for… For… tail-based… sampling for For… for log-based events.
Have I lost, I cannot hear you. Is it on my side?
**Liudmila Molkova** 16:52 No, no, I'm just… I love the tail-based sampling for log-based events.
Sounds good.
**Pellared** 16:58 He was not… it was not a blog He just said… Google wants for us.
**Trask Stalnaker** 17:05 I… I mean, tail-based sampling… Oh, does the collector not include logs in Tailbance sampling? I would have assumed that it… Oh, maybe it doesn't have that option, but it could.
Right.
**Pellared** 17:24 I'm not sure how… It will be performance-wise, because then you'll need to have a cache, you would not… Yeah, you'll just need to wait.
Yeah, you're cold.
Yes, you called.
**Trask Stalnaker** 17:40 cost of, I mean, already tail-based sampling, you're…
**Pellared** 17:44 Yes, same course, you just, you need to wait before you emit the events until the spend, yeah.
So yeah, possible.
You're right.
**Liudmila Molkova** 17:57 I mean, it would be a big change, because it's currently only a span processor.
And it would need to be a log processor, and it would need to be a central component between them.
**Pellared** 18:13 I think there is some… I think which… is cross signals, like this span… span metrics, I don't remember the name of the collector component.
**Liudmila Molkova** 18:23 ESPAN metrics connector.
**Pellared** 18:25 Connector, yeah, I think that's the name.
**Liudmila Molkova** 18:28 it… it kind of, it connects, right? It does… it's not… it only needs spans on input and only metrics on the output.
This would be some state management, but I mean, yeah. I don't think it's a blocker, though, and… Someone could say that since we deprecated span events, we made it harder, that's true.
**Pellared** 18:57 Oh, I'm muted.
**Trask Stalnaker** 19:06 Yeah, I mean, it seems… Seems very possible. It's just, you know.
**Pellared** 19:17 So I guess I would…
**Trask Stalnaker** 19:19 Wait for feedback.
**Pellared** 19:21 Yeah, so my… yes, that's exactly the question. Should we just create an issue or wait for feedback?
Because… If nobody asks, then… It's a war, you've wasted effort.
Maybe we're just guessing that it's an issue.
**Liudmila Molkova** 19:41 Well, there is a condition in it to sample based on span events.
Yeah, let's wait for the feedback.
**Trask Stalnaker** 20:05 I'm good with that.
So, it sounds like the main thing is… Let's see… development… Okay, and this stuff is pretty fresh, still.
Probably… Need to get more people to start implementing and this stuff.
Which, hopefully your blog post will… Start getting people thinking about it, and then also in the spec meeting, we can start pushing Or, Folks to start implementing Using the, the environment variable opt-in.
**Liudmila Molkova** 21:13 Assuming instrumentation libraries.
follow it in a few languages. It would count as… prototypes.
So… If we… Once expedite it, we would focus on the instrumentations.
Java was already using a trait.
inexpensive.
**Trask Stalnaker** 21:44 We have a… We haven't merged it yet, but we do have the prototype PR.
And we are going… we are going to merge it, just haven't yet.
**Liudmila Molkova** 21:58 It would be blocking your stability, would it?
Or would it be there?
**Trask Stalnaker** 22:04 Benefiture Club.
It's behind a feature flag for now, But we were… I was hoping to… Make that the default in 3.0, which is… Hoping for first half of this year.
**Liudmila Molkova** 22:27 So we want to stabilize it regardless.
**Trask Stalnaker** 22:34 Yeah… I mean, as far as what's… Possibly controversial.
The only thing, I think, was maybe the naming pattern?
I was… Like, I feel like the severity… is good and is very, very flexible. Like, there's not a lot of, like… Yeah, it's very flexible, so people… it's still… yeah, I don't feel like that's… controversial.
**Liudmila Molkova** 23:32 Oh, we should probably follow the same principle, then. We have, like, instrumentations don't depend on this guidance.
They depend on specific event names.
And if we stabilize a couple of these event names for HTTP database as RPC, This would de facto mean stabilizing this guidance.
**Trask Stalnaker** 24:06 Yeah, yeah, that's a good… Right.
I see, so you're… you're… the point you're making here is that this Instrumentation really just depends on the… domain-specific semantic conventions, not… doesn't really depend on this. This is more, like.
Guidance for authoring semantic conventions, or people, kind of, Creating their own…
**Liudmila Molkova** 25:47 Yeah.
And technically, we can… Even… Move it away from this dock.
Like, the normative guidance, it should have event came.
Okay, pattern, I think, is necessary.
Should have a severity.
appropriate one.
**Pellared** 26:18 This is just a recommendation, I think it's good for, you know, the instrumentation.
**Liudmila Molkova** 26:32 Sorry, sir.
**Trask Stalnaker** 26:34 Yeah. Yeah, I'm not… where… what are you suggesting to move out?
**Liudmila Molkova** 26:40 So, let's… I think the plan I'm thinking about, maybe we, we start by stabilizing specific events.
Once we do this, we can either stabilize this dock, I think we should try.
If we still have any controversy on the general approach.
We're… can separate the controversial parts. I think we all want it to lend, and it could… we want to provide the flexibility when it makes sense.
So I think we can find beans to stabilize this dog without controversial pieces.
For me, the larger interesting question for this doc would be.
the requirement levels, and I think there is an issue about it.
**Trask Stalnaker** 27:46 Requirement lev… severity levels?
**Liudmila Molkova** 27:50 Requirement levels and attributes, let me find…
**Trask Stalnaker** 27:54 Oh…
**Liudmila Molkova** 28:21 Surety for surety 1… Issues.
Golly, it's either… Type.
Or… message, and I'm… I think it should be both.
Or at least one should be required all the time.
**Trask Stalnaker** 29:04 Is it not already? Is this the proposal, or…
**Liudmila Molkova** 29:09 It's what it looks like now, the proposal.
is… Type and message.
to be required.
**Trask Stalnaker** 29:20 Oh, I see.
**Liudmila Molkova** 29:23 Yeah.
I think it's not the case to… They… because CJR told in the linked comment that Rust only populates the message, but not the type.
So maybe message should be required, type should be conditionally required, it just needs some analysis across SDKs.
**Trask Stalnaker** 29:48 Yeah, I know in… Java, you can have empty exception messages.
**Liudmila Molkova** 29:56 Mmm. Oh, right.
Madame Petty is okay.
**Trask Stalnaker** 30:06 True.
now that we've fixed the… we only, in the last release, fixed the Java SDK bug that, the empty messages were, Empty attributes were dropped over the proto-layer wire.
So there was no difference.
**Liudmila Molkova** 30:30 Creative complex attributes.
**Trask Stalnaker** 30:35 That one actually was… not caught by complex attributes, that was… That was just a bug that somebody… Finally noticed.
**Liudmila Molkova** 30:50 Cool, yeah.
**Trask Stalnaker** 31:07 Alright, well, at least we've got a tracking… issue, but yeah, I like, Yeah, so we need… prototypes…
**Liudmila Molkova** 32:10 checked on GitHub of people using span events on tail-based sampler.
In GitHub.
I found only examples.
And I found one… Repo that actually uses exception message and span event.
Across absolutely all of them on GitHub.
**Trask Stalnaker** 32:34 Oh, it'.
**Liudmila Molkova** 32:34 Sounds promising.
That people don't actually use it enough to justify any complications.
**Trask Stalnaker** 32:44 Yeah, I mean, I could see somebody, though, wanting to tail sample, like, they want to Capture all the traces that have been a… an exception?
But, like, usually that's… have an error, you can just sample on spam status.
**Liudmila Molkova** 33:04 Yep.
**Trask Stalnaker** 33:06 So it'd only be, like, if you wanted to sample on a specific Exception message?
Seems reasonable.
But it also seems… Something that could be… addressed later, like, I don't feel like the spec… Causes any problems for that.
I mean, given that we're going in that direction.
Like, I'm not sure we can do anything about it at the spec level to make that… Better.
**Liudmila Molkova** 33:48 Yeah.
**Pellared** 33:50 Should we also not say that parts of the recording, recording errors should be stabilized?
Because here we are just stabilizing the exception logs attributes, and not how instrumentation should… Yeah, recording errors, I think.
I think in the name.
Recording errors, in general, or somewhere?
**Liudmila Molkova** 34:20 Yeah, here.
So I think we… we can already stabilize everything but recording exceptions in this doc has been, For a while, we implemented it 10 times.
And then the most important section is the last one, yeah.
And then also deprecate exception spends.
**Trask Stalnaker** 35:03 What are exception spans?
**Liudmila Molkova** 35:06 There is a doc next to exceptions logs.
Code exception spans.
**Pellared** 35:21 But this one is actually used, I think.
by the semantic conventions.
And… give me a sec.
What could be errors?
There is this… Because there's error type, not exception type.
I see.
If… Yeah.
Yeah, you're right.
**Trask Stalnaker** 36:15 Oh, yeah, let's add this.
Cool.
Helps.
Need to know what, chip away at when I, emerge from Gen AI land.
**Liudmila Molkova** 36:46 I'm so happy we are there. You can't even imagine.
**Trask Stalnaker** 36:57 Alright, anything else?
To chat about today?
**Liudmila Molkova** 37:05 Nothing from my side, I need to get back to my J&A island.
**Trask Stalnaker** 37:12 Alright, well, have fun in, amsterdam without me.
**Liudmila Molkova** 37:18 Yay! Have fun with here without us, and we are cancelling the next call, right?
**Trask Stalnaker** 37:23 Yes. Yes.
I just blanket assume all OpenTelemetry meetings are canceled the week of KubeCon, unless otherwise stated.
**Liudmila Molkova** 37:38 Yep. Alright. Cool.
Bye. Thank you!
**Pellared** 37:42 Thank you.
