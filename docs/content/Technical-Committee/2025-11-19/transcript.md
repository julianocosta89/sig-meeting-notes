SIG: Technical Committee
Date: 2025-11-19
Duration: 67 minutes
Zoom Recording URL: https://zoom.us/rec/share/LQAWUdMvIzAui2KXDtW1GHBHuKsrnByq8Xcysht5EdCJDfH5RJtv-iBrhpDlimDU.MFMYkwstMmHRxp97
============================================================

## Zoom Recording Transcript

Reiley 00:01:01 Hello, Jack, Josh.
You're muted, Jack.
Jack Berg 00:01:09 Hi, Riley. Hi, Josh.
Josh Suereth 00:01:12 How's it going, man? It's been a long time.
Jack Berg 00:01:15 Yeah.
It's good.
You were… you were sick, right?
Josh Suereth 00:01:21 I… I'm still… I still have a head cold, dude. I think… I think I got COVID at KubeCon.
Jack Berg 00:01:27 I was traveling last week, too, and came home sick.
I mean, I'm on the up, but I was… I had a head cold as well.
Josh Suereth 00:01:35 Yeah, I hear ya. It's…
I… there's something since 2020, every time I go on travel, I come home sick.
Jack Berg 00:01:43 Yeah, every time. Every time I travel.
Josh Suereth 00:01:47 Yep.
But it's probably age-related, but I'm gonna blame… Anything else?
Alright.
Because we're waiting for everyone else to show up. If you guys have agenda items, please add them.
I did want to talk about…
Reiley 00:02:14 Dude.
David Ashpole (dashpole) 00:02:18 Hey, bro.
Josh Suereth 00:02:37 Okay…
David Ashpole (dashpole) 00:02:40 So…
Josh Suereth 00:02:42 We'll wait a little bit for Carlos. Did Carlos say he… Couldn't make it.
We'll wait, like, 3 minutes before we start.
Then…
Anything else, new going on? Jack, you changed jobs, didn't you?
Jack Berg 00:03:30 I'm at Grafana now.
Josh Suereth 00:03:31 Nice.
David Ashpole (dashpole) 00:03:33 Congratulations.
Jack Berg 00:03:35 Yeah, I decided to, I decided to take all the change at once, instead of spreading it out.
Josh Suereth 00:03:44 Nice.
David Ashpole (dashpole) 00:03:45 How are you enjoying that?
Jack Berg 00:03:49 New job is great.
That's, I took a couple of months off, and
I don't know, it's not like I was really off, because I had a newborn, and so that keeps you really busy and tired, but still, somehow, I feel, like, refreshed.
Josh Suereth 00:04:11 Coming back to work, and…
Jack Berg 00:04:14 Kind of new energy.
Reiley 00:04:21 Yeah, now you've made me worried. I have an employee who's going to
Take, maternity leave in a week.
And I started to wonder what would happen when he came back.
Jack Berg 00:04:36 Yeah, well… I don't know, I like…
I actually wanted to switch jobs, like, a year ago, but, you know.
it didn't feel right going to a new company and going on parental leave immediately. And so, like, I kind of bundled everything up. I got everything at my old employer in, like, a really nice spot.
David Ashpole (dashpole) 00:04:57 And I was like, okay, this is a perfect time to just, like, you know, sever the relationship.
Jack Berg 00:05:03 Everybody's in a good spot.
Josh Suereth 00:05:06 Yeah.
Carlos Alberto Cortez 00:05:07 I saw, by the way, I saw a developer from New Relic.
According to the specification calls.
I'm hoping the best, that she will stay… she will stay around, I know it's part… she's part of… yeah, correct, yeah.
Jack Berg 00:05:22 She's part of the Ruby side, yeah, she's a maintainer over there.
Carlos Alberto Cortez 00:05:25 Yeah, correct.
Yeah, so let's hope that New Relic keeps her working, you know, for Opel… for Open Telemetry.
Jack Berg 00:05:33 Yep.
Reiley 00:05:34 Now it's you, Jack, Linmella, and Ted.
Jack Berg 00:05:39 Yeah, we're all at the same company, but we're on different teams. Well, I guess I'm on the same team with Ted, so we can coordinate pretty well, but…
Carlos Alberto Cortez 00:05:48 Don't forget that this is a recorded call, by the way.
Jack Berg 00:05:52 Thanks, Carlos.
Josh Suereth 00:05:55 Huh.
I'm curious, but we'll… we can talk more later. Carlos is here, and we're at plus 5, so let's get started on the Kotlin MP donation. Carlos, you wanna take it away?
Carlos Alberto Cortez 00:06:06 Yeah, please, thank you so much. Yeah, basically, you may remember this, review that, I presented in the past.
There were some concerns about regretting instrumentation, about whether this could be something, like.
could be implemented in a different, simpler way, relying on JavaScript and Java implementations.
And basically, I had… they gave me some guidance, and I went and talked to the Android folks and other people, and first of all, Embrace, who is… has been pushing for this donation, they have this idea that
They want to reuse instrumentation as much as possible, instead of regretting that. So that's a good sign, in my opinion.
There will be probably some cases for specific instrumentation that it just makes sense, much more sense to write that.
Under Kotlin. And I'm talking about instrumentation that exists for the Java ecosystem.
That cannot be used in any case.
For, for IUs, for example. So that's a good thing, in my opinion.
The second one is that the Android folks actually do support this, because They think that,
A lot of complexities.
are appearing more and more in the Java SDK, because the Java SDK has to support Android, you know, as Jack mentioned in the past.
So they think that this could help things a lot for everybody, you know? Their main… my impression, and I have to confirm this, but based on what I talked to them, is that
Even though it's a great alternative.
for providing multi-platform support, I think that their initial, at least their initial target is Android, you know, to make life for Android observability so much better.
So that's the stuff, that, that being said,
I have to say my personal opinion, which is I think this donation should be accepted. That's just my personal opinion. And if we were to decide to recommend that to the GC,
I would say that there are two initial things that could be done either prior to accepting the admission, or right after the donation has been, you know, started.
The first one is, validating… you may remember that they have an API.
Duff.
also can play with some interop layer, so it can use the Java SDK behind the scenes.
So, I'm Bogan said that… or somebody that we could, like, actually ask them, you know, to make this stable, you know, or, like, implement everything, so, you know, we are confident on that front.
And the second thing is that, I don't know if it's too obvious or not, given what the Android folks told me, that go and check all the requirements that currently the Java SDK has to, you know, that the Java SDK has to do in order to work on their Android.
And make sure that those things would work smoothly, like, very smoothly under Kotlin. If that… if that can be proved.
Then it makes a lot of sense for the Java SDK included.
So I guess, yeah, I don't know how obvious that is. I guess I would, like, have to ask more, but yeah, basically, that's the point. And of course, like, these two, potential requirements about testing, validating the API and the interrupt layer.
Or validating the PSDK, whether they should be done right after the donation, or they should be requirements.
Prior to accepting the invention itself.
Jack Berg 00:09:50 There's a couple of things in there that I don't fully, I guess, understand.
They say they want to reuse instrumentation.
What does that mean?
the instrumentation is written against the Java API, and the whole point of Kotlin multiplatform is that you have to write it all in Kotlin so that it can compile to the different targets. So…
What am I missing there?
Carlos Alberto Cortez 00:10:18 Yeah, I think that they would be… I forgot to mention, they were… I think an adapter layer would be something
which is kind of a hack, probably, if you think about that. Like, exposing then the API they have, you know?
Jack Berg 00:10:32 So they can write… how would that work? So, like, in Kotlin multiplatform, everything needs to be written in Kotlin, and they want to have… they want to use the Java-based instrumentation.
Like, when they compiled it, the Kotlin multiplatform can only compile Kotlin source code.
So, what, what is…
Carlos Alberto Cortez 00:10:55 As far as I know, there will be some kind of conditional compiling, like, platform-specific, you know?
So that means that, basically, you will have different profiles, like.
when you are doing the general compilation, you have to select an IOS profile, for example, which you may be importing IOS-specific stuff.
And of course, there's the usual thing that you just only do business logic, so you don't have to actually
worry about that. But anyway, I can gather some last additional feedback from them on this point.
Jack Berg 00:11:35 Yeah, I think… I think that actually… there's something missing there, and that's not quite right. They can't actually rely on, on Java-based instrumentation. And so, like, you know, a couple of the other, like, arguments in there, so just… just to pre… pre…
To back up a bit, I do support this donation, but for different reasons.
And that's because, you know, I think Kotlin multiplatform is becoming increasingly a thing, and we can't support it with our current solution. And it's like, so if we want to have a story around Kotlin multiplatform, we have to do something like this. So the question in my head is, like, hey, like, what…
how big is Kotlin multiplatform going to get? And,
And, you know, does that demand justify all the work that's gonna go into this?
You know, I can't answer that question. I don't know how big Kotlin multiplatform is going to get in terms of popularity, and I don't have a firm grasp of how much effort this is going to be to, you know, build out this solution. I think it's a lot, but, you know, if there's enough folks that want to do it, who am I to stop them?
Carlos Alberto Cortez 00:12:45 Yeah, I could say that in the perfect… go ahead.
Josh Suereth 00:12:47 I was just gonna jump in, Jack. The thing about reusing Java instrumentation, like, to your point, if Kotlin multiplatform needs multiplatform code.
they would only want to reuse Java instrumentation when they're compiling in the Java ecosystem. If you're actually compiling for, like, native.
you don't have Java code you're depending on, right? You have something native you're depending on. So that's where you'd want to share instrumentation with that native thing, if you're able to.
We don't have a native shared…
instrumentation story at all between any languages that are native. So that's something that, like, we'll have to investigate, but in terms of, like, the Java thing, I actually have no concerns there of, like, if they're compiling for Java, they reuse Java instrumentation, we make sure it's compatible. If they're compiling native, that's a new exploration space that's wild and crazy and fun.
And, yeah, I still think the build ecosystem in Android and Gradle will be exciting for you. I… that's actually more my concern, is how do we distribute this craziness? Because last I checked.
distributing,
at least if you're using Maven standards, distributing native binaries or, like, built for different distributions is a pain in the butt.
And actually figuring out how to declare, like, this is stable, this is not stable.
Across platforms is also exciting.
for an ecosystem that was not designed for it, right? Like, Java never designed itself around that. So, I don't know where Kotlin Multiplatform stands there. That would be more my concern of…
you know.
what is our story around distributions and these things? Do we just distribute a bunch of Kotlin code and someone else is responsible for making it binary compatible and understanding dependencies? I hope that that's true. I… someone who understands the Kotlin namespace better could tell us.
But from what I've seen so far, I don't have concerns around, like.
what we're doing with this Java compatibility thing, right? So, we say, if you're compiling for Java.
Make sure you're compatible and can reuse Java instrumentation, great. If you're compiling for native, there will be some requirement we have to sort out at some point.
But for now, I think it's Wild West.
Jack Berg 00:15:08 bet.
I won't, like…
I'm not gonna block on that, but Josh, the whole point of Kotlin Multiplatform is that you can, you know, instrument.
something that is all written in Kotlin and compiled to multiple targets. And so, like, there's not a lot of benefit to saying, like, hey, we can have this compatibility layer that says, like.
you know, if you're compiling to Java, you can use the existing Java instrumentation. Like, if we're gonna do that, then what we have currently is just as good. We don't gain anything from this. The whole benefit is about being able to compile the multiple targets, and so…
Josh Suereth 00:15:46 And I'd agree with, yeah, like, if we even said… so, the only…
The only reason I say that we should be able to reuse Java instrumentation is actually the invisible dependencies, right? So, like, the way that, the way this worked in Scala, native.
Was you actually, when you would compile a dependency, the dependency actually was a different block of source code for every platform.
Potentially. It could be pure, like, you know, Kotlin code, if you will, but you can also say, like, this is the block of code for this platform, and this block of code uses this Java library when I'm on the Java ecosystem. That Java library uses native Java instrumentation inherently.
That I want to work.
But when it's like, okay, when I'm running on iOS, and I use this iOS library.
Ideally, if that iOS library is natively instrumented with OTEL in some fashion.
then that should also work with Kotlin Multiplatform, right? To me, it's the transitive dependencies that matter.
I don't expect a user to basically say, hey, I'm gonna use Java instrumentation. What I expect them to say is, I'm using this library in my… in the Java world, and here is the replacement that I use in iOS, here's the replacement I use natively in Android.
And the way, you know, you design a module in Kotlin Multiplatform is you might
you might have that module be written in pure Kotlin, but you might also have a wrapper around 3 different implementations, right? One for Java, one for iOS, one for Android. You know, especially if you're doing dynamic load library kind of shenanigans, right?
So that…
Anyway, that's my point, is that's the use case I'm thinking of, not the… I agree with you 100%.
people will not be writing Java code for Kotlin Multiplatform.
Jack Berg 00:17:40 That's, like, missing the point.
Josh Suereth 00:17:41 Exactly, yeah.
Carlos Alberto Cortez 00:17:46 On top of that, I think that, according to what I could confirm with the Android folks.
you know, there are some, let's say, hacks, or I don't know, and, you know, that Java… the Java SDK has to do to support Android. So, in theory, like, by having these.
At least the SDK part would help a lot of stuff.
Jack Berg 00:18:06 Yeah, so.
Carlos Alberto Cortez 00:18:07 Java is the key, yeah.
Jack Berg 00:18:09 Let me give you some examples. So, like, in Android, there's, you know, they have compatibility with a certain subset of the Java core APIs.
And… but not all of them. And, like, you know, with each successive version of Android, you know, there's… there's more and more support for the Java Core APIs. And you have to, like, basically go to the Android docs and say, like, hey.
I want to use this Java Core API. Is it actually supported?
And there's things within the core of the Java SDK that are not supported in Android. Things like, a double adder, an atomic double adder, or, like, just double adder, let's call it. And it's like this, you know, high concurrency, lock-free way to add numbers together.
And so we use that, and but it's not supported on Android, and so we have to provide some… do some… jump through some hoops to say, like, hey, use this or this based on what's available, at runtime. And so that's an example, but… so, like, in theory, we can get rid of all those hacks to support Kotlin and Android.
If this Kotlin multiplatform thing gets mature. But it's a big in-theory thing, because, like.
there's going to be… it's going to be a long time before this project is suitable for all current users of Kotlin.
that use the OpenTelemetry Java SDK. And so, as long as the OpenTelemetry Java SDK is still, like, superior to this in, like, any dimension.
you know, we're going to have user requests that say, like, hey, no, I don't want to use this immature new product, I want to use the existing OpenTelemetry Java SDK, and therefore, therefore, we'll be stuck with those hacks for a long time.
So, like, I…
Carlos Alberto Cortez 00:19:57 I would be surprised.
Jack Berg 00:19:58 surprised if we could get rid of the Kotlin hacks that we have, you know.
Before 3, 5, 7 years from now. Just…
I don't know, I'm not that optimistic about them being able to replicate all of the things that we do quickly.
Carlos Alberto Cortez 00:20:18 Okay, I will add two notes about those things, about the timeline on the existing,
things you have to do to support Android.
And I will ask about the compatibility regarding existing instrumentation. So, other than that, is there any other concern?
that I can't… Comment, you know, or otherwise you can… you yourselves come and add stuff yourselves there.
But, yeah, other than those two items, anything else that I would like to…
you would like me to go and, you know, talk to Embrace about this?
Jack Berg 00:20:56 So.
Carlos Alberto Cortez 00:20:57 Here's the thing.
Jack Berg 00:20:58 Just one final thought, so, is… It's…
There's a lot to know about… there's a lot to note…
to be successful in publishing an OpenTelemetry API and SDK, there's a lot of opportunities to shoot yourself in the foot if you design it wrong, and, you know, you're forced to have a major version break, or, you know, you don't properly understand how to provide, like, strong backwards compatibility guarantees.
I'm wondering if there's, like, enough people that are working on this project that are from the OpenTelemetry ecosystem. I know there's Jason Plum.
Carlos Alberto Cortez 00:21:40 There's… one of the… at least one of the, developers involved in the…
Kotlin, SDK is already part of OpenTelemetry Android.
Jack Berg 00:21:52 Yeah, but the… I don't think they have any stable components.
Carlos Alberto Cortez 00:22:00 In Android, you mean?
Jack Berg 00:22:02 If they do, it's recently stable.
Josh Suereth 00:22:08 I did talk to Jason about this. If I remember right, the theory behind OpenTelemetry Android is it's just configuration defaults. So, like.
I hear what you're saying, Jack. Like, the concern is an API is different than a configuration file, in terms of keeping it stable and making sure that it
you know, maintains compatibility. So, yeah.
What… what do you want to see there?
Jack Berg 00:22:37 I don't think it's realistic what I want to see. I think what I would like to see is somebody that's already a maintainer of another API or SDK,
Going and working on this and helping to seed this project.
Like, do we have… do we have examples of other APIs or SDKs that are, like, seeded from… from scratch without, like.
from people that, you know, weren't priorly involved with other APIs or SDKs?
Josh Suereth 00:23:08 I mean, do you mean, like, the foundation of the OpenTelemetry project?
Jack Berg 00:23:12 Yeah, yeah, yeah, that one, sure.
That's an example, but, like, we've come a long ways from there.
Josh Suereth 00:23:24 I mean, it depends on language, right? Like, I still think there's languages that we don't support that come in.
You know?
I think there's an OpenTelemetry Haskell, for example. Has anyone looked at that one?
Got it.
Yes.
Carlos Alberto Cortez 00:23:41 This is the closest, you know?
Jack Berg 00:23:44 And Rust was struggling, my understanding is that it was struggling before, you know, some other .NET maintainers got involved.
Reiley 00:23:54 Yep.
Jack Berg 00:23:58 Anyways, that's… this is… this is a concern of mine, but, like, I don't think I want to do anything based on it. I just…
Carlos Alberto Cortez 00:24:05 No, I think it's a good one. I can… go ahead, Josh.
Josh Suereth 00:24:09 Yeah, I was gonna say, we, we…
I think your concern's legit, man. Like, we… we should do a… the API reviews that we did in every other maintainer and language for compliance and, like.
The thing is, though, when it comes to understanding stability, you know.
do we understand what school looks like in Kotlin multiplatform? You know, who can provide that? Like, I hear what you're saying, I think that's key, so I think partly what we need to do is be asking them a lot of questions that they haven't thought about ahead of time.
in this review, and as they onboard. And, like, the expectation should be that they become that expert. So the thing that I would say to your point is not, we don't want, like.
an existing maintainer to drive this, we want to teach them how to care about the things we care about and drive it. And so how do we make that happen? And I think reviews, asking lots of questions, you know, mentorship, that sort of thing, we need to be active in this one.
I think is what you're saying. So I would argue that this probably needs a strong TC sponsorship requirement.
You know?
Jack Berg 00:25:17 That's where my head was going as well, is like, as soon as you started talking, it's like, yeah, you know, so I don't think we can get away with just, what was the sponsorship level? The lowest level, where it's like, maybe it buys, or… no.
Carlos Alberto Cortez 00:25:32 escalating.
Jack Berg 00:25:35 isolating.
Josh Suereth 00:25:35 Yeah, this one, I think, needs at least guiding, yeah.
Carlos Alberto Cortez 00:25:38 Yeah. If I am around, I could be that person. If I am still around, but let's see.
Josh Suereth 00:25:54 Yeah, I do think that, Carlos, that'd be awesome if you… if you can do that. Do… do you have…
We should recommend that this comes in with a guiding sponsorship and make sure we have a TC who can provide guiding level sponsorship.
Absolutely agree. Carlos, is this… is this what you need to continue with the discussion?
Carlos Alberto Cortez 00:26:13 That's correct, yes. And in the meantime… well, the last thing that I want to say is that the previous point that… about initial things to do, validating these two things, if you have any opinion on whether we should
Require any of those?
Prior to the donation, let me know. We can be offline, or here, or right now.
Those things will be things that we'll be recommending to the GC, you know?
I think the GC will have to…
Make, you know, make the call.
But yeah, it would be nice to let them know what we think.
Josh Suereth 00:26:51 Oh, that, that sounds, that sounds reasonable.
Carlos Alberto Cortez 00:26:54 Sweet, so let's do this! Yeah, okay, so I will be, providing some feedback. I'll be talking to the Embrace folks, and coming back. By the way, there's a lot of interest, it seems.
from people in the issue, but I wonder… and that's actually an interesting thing, that either… even though Embrace is happy to put a few engineers, we need to see how much
actual people from outside Embrace could help on this one. But anyway, I will be providing some,
Some news on this one, hopefully this week.
Thank you.
Josh Suereth 00:27:30 Yeah, thanks for driving that, man.
All the fun things. Alright. I wanted to have a discussion around stabilization efforts, but first I want to see if anyone has any other topic. This one will probably be the remaining 30 minutes, if we let it be that, so…
Did anyone have any other topics before I jump in?
Carlos Alberto Cortez 00:27:50 I have a small one that I would like you to think. I would probably open an issue or
Discuss something, but… The CICD was wondering, like, every time the CICD wants to do
They add something, like environment propagators or environment carriers, they would like to see that implemented in all the SIGs.
And they were, they were saying, maybe we can help them, you know, go and write that for them, maybe. But how do we track
whether SIX are working on this or not, and the matrix is the usual thing, right? You have that feature there.
But they were saying whether the metric is…
clear enough or not, you know, or whether there's a better way to do that. Also, in particular, they could be very, they are very interested in having this stuff that they are working on actually implemented.
But, of course, that depends on the, on the maintainer. So if you, if you have…
something in your mind around that, or you think that the matrix is the way to go?
Josh Suereth 00:28:55 I think that might be part of this broader discussion on stabilization efforts that I want to have. It's kind of related. Yeah, what do we want to do with the feature matrix and track things?
Jack Berg 00:29:05 Can I just jump in real quick as another.
Josh Suereth 00:29:07 Sure.
Jack Berg 00:29:08 point before we have this longer discussion. So this is just an informed.
So, the config sig, we are looking to stabilize key portions of the specification and of our data model, which is in the OpenTelemetry Configuration Repository at the end of this year slash early 2026. Your talk about stabilization just jogged my memory. We've been talking about this for a while in our group, and we're all aligned and are ready to make a push.
Carlos Alberto Cortez 00:29:34 Nice, actually, I wanted to ask about, because you have a PR, which has been staling for a little while, so I will… so it's ready to review that, right?
Jack Berg 00:29:41 I should honestly just mark it as a draft. I'll go do that now, and then, you know, I'm gonna re-open it once everybody's on the same page.
Carlos Alberto Cortez 00:29:50 Okay, it makes sense. Yeah, because I did review that, but I was wondering when it could be a good time to review that again.
Good.
Josh Suereth 00:30:03 Yeah. Cool.
So, I think,
I want to talk overall about the stabilization efforts, and this is… this is an example of someone added something, we want to make sure it actually gets implemented across the board.
And so there's an aspect of tracking stabilization, right? First I want to ask overall, with the stabilization, the GC has taken the impetus to kind of, like, drive the narrative and make the blog posts and that sort of thing. Our charter does call out that we own, like, release management for a hotel.
And so, right now, with the way that sits, I am curious how much of this we want to be driving and should be driving. I did some investigation myself around where things are stable and where things aren't stable, and for example, the specification, even the specification on stability is unstable.
So, what, what I'd like to propose, Carlos, this is a great, a great example of what, what I, I think we need. There's, like, two…
Two things I think we want to do. One is process around stability, right? So, what is our process around driving things to stable and tracking unstable things?
for example, we added something to the spec, but it's not implemented across languages. How do we want to track that, and manage that, and understand the shape of where things are?
you know, So… within that, we can talk about, you know, Tigrin's,
Tracking bugs on every… oh my gosh.
on every sick, we can talk about a compliance matrix.
And the last is actually just, prioritization, which I guess you could call process, but,
How do we finish things?
Perfecto.
Stable, but maybe…
I'll give some examples. If we look at the spec, like, if we look at the telemetry stability spec, right?
And you look at this, this is currently considered in development.
We have this notion of unstable and stable instrumentations, and we have to-dos right here.
We have this notion of fixed schema telemetry producers, schema file-driven telemetry producers, and when you think of this spec.
We did a lot of work around schema-file-driven producers, but honestly, a lot of implementations of OpenTelemetry are not even producing schema URL.
In practice. And if you need examples of that, just go instantiate the OpenTelemetry demo and look for schema URL.
Okay? So, I would argue that the work for this has not finished.
If it's not… across all of OpenTelemetry that hasn't been driven, It's not done.
There are… our spec is riddled with stuff like this, when you start looking through it.
So, what I'm proposing for us to do is… actually start taking this as a TC,
and figuring out how we want to accomplish it from a process standpoint. So, I want to categorize
the spec. You know, the compliance matrix is one categorization. There's a whole bunch of other pieces in the spec. Let's look through our spec and figure out all the various components that are not considered stable.
Let's figure out what they're meant to do, where they're meant to be,
And let's start churning off and prioritizing those capabilities as part of the stabilization effort, and understand, like, what does it take for us to bring them to be stable?
This… this particular one, I call out, again, because it's in the blog, about they want to change what it means for instrumentation to be stable.
to not rely on semantic conventions going forward. And we're asking a bunch of questions on what that means in semantic conventions, we're talking about federating SEMConv, etc.
But the whole thing relies on a piece of the specification that's still in development with a bunch of to-dos.
And with a vision that has not finished.
Reiley 00:34:24 Right? So…
Josh Suereth 00:34:26 How do we as TC want to start engaging with these things and driving them forward?
Anyway, this is supposed to be an open discussion.
Joshua MacDonald 00:34:51 I'll share what you made me think and feel as you asked the question, Josh.
I have this sense, and this is sort of not answering your question, but
I feel like rotating maintainers through the SIGs would help us somehow. The idea that the maintainers become essentially entrenched, and like, they know their users, they know
their own codebase, and they're not paying attention much to the spec. And I… and I…
at least I've seen a few times, like, it just seems as though, you know, we as engineers forget that we're here to produce high-quality instrumentation, that I would actually want to use to instrument a real system.
I would love to see the people who are working in these SDKs, like, leave for a bit, try to use it in a real system, in a language that they're working in, and come back and see how the experience was. Is it good? Is it the best it can be?
are we doing our jobs here? Because I feel like we get too narrowly focused on, does it implement the specification, instead of asking, is it good?
Reiley 00:36:09 Yeah, I have some similar thinking with Josh, but I'll come from a different angle.
I want to ask, do we have clear understanding what does stabilization mean? Do we have some alignment? Like, my gut feeling is I probably would only agree with
you about, like, 50% of the definition of stabilization. Like, in my mind, if people come, like, I remember, like Dan mentioned for the JavaScript taxi, customers come.
And they normally don't complain about, hey, we're missing a specific feature. If they miss a feature and there's enough demand, they'll prioritize that. If there's a feature on the spec, compliance metrics, but nobody has ever asked for it, then they wouldn't do it.
That makes sense to me. And then, on the other side, I see a lot of people come and say, I don't want to use your stuff, then on the next day, I just bump the version, and my stuff, like, starts to fall apart, right? So… so people care about the backward compatibility. This is what they call a stabilization.
Like, I…
It's fine if you have a very early stage thing, you're telling them this is beta or something, but they want to know, what does that mean for me? And for different components, it might be different. Like, you might have a preview version of the instrumentation library, and the indication here is by eating that.
We might change the schema in your breaking way, and your entire telemetry would look at, like, Totally differently.
And… and that's scary for many folks, but you could also have a preview version of the ICK. Well, everything is super nice, and you just say, like, I don't have super confidence about the…
like, the performance or something. I just want to let people give a dry run. So, I feel stability here.
ask is more coming from the user, and they have specific need. Well, in our definition, stability means something very different.
And my worry is we focus on some stability, we think, oh, we're super stable, now we're perfect. The user come and say, no, we disagree with you.
Josh Suereth 00:38:09 I'm gonna respond to that right now, if that's okay. Sorry, I'm gonna jump in line, David, but that, like, I…
I agree with you. Here's where I think we fail.
We have a thing that's widely used, that's been in development for 5 years, and doesn't consider itself stable.
However, there are pieces of it that are incredibly stable. I'm talking about the collector, by the way. There are pieces of it that are incredibly stable. People depend on those pieces.
Then, they look at a piece, and they're like, oh, I need XYZ feature. Well, XYZ feature is not marked as stable, but I'm using so many unstable things that it's probably at the same quality as the rest of it. And then it starts breaking, and they're like, why the hell does this break? What, you know, you guys can't keep things stable.
The collector… in my opinion, the Collector should have been 1.0 way long ago, because it's been 5 years in development.
Right? It's been relatively stable for most of those 5 years in certain ways, and it's actually more of a cultural thing, in my opinion, than a technical thing. If we need to make breaking changes to key things, we need to figure out how to rev V2s. Look at Java versus the collector. There's a lot of gunk in Java.
Right? There's a lot of gunk that has come from remaining backwards compatible.
But it has evolved significantly. This is true of a lot of other things as well, like if you look at the SDKs.
What we need with… is to set good expectations with users on stability. So when we say something stable, we know what we mean.
And… That needs to be consistent with user expectations.
So, we've set up an expectation that unstable things in hotel are stable.
That's the problem.
And so we have no distinction between unstable and stable at all, because people treat unstable as stable. That has to be fixed.
So, I agree with you that there's, like, there's a bit of a disjoint here, but I think the disjoint isn't what you're suggesting. It's actually this issue of everything unstable is considered stable.
Because of how long things stay unstable, and the fact that we never mark them to stable. What I want is a process where things can't live in that state for very long.
If something gets to a point where it's widely used in version 0.x.
it needs to hit 1.0. Like, like, basically, if you haven't spent the time to change it, market 1.0. If you need to break it in some way, make a 2.X.
And we move that direction. Yeah, go ahead.
Reiley 00:40:42 But then you're going to have trouble, like, that means we're going to either stabilize permissions powder very soon, or we just go and remove the entire thing. It has been there for many years. Like, if you ask me, do I want to remove permissions powder? Sure.
Like, I don't want anything unstable there for more than a year. I'm more than happy to remove that, but do you think we can?
Josh Suereth 00:41:01 I think, practically, we could have had multiple… well, David, I shouldn't jump in front of you. Practically, we could have 1.0'd it, and then have a 2.0 as a Prometheus exporter, and I think that's probably…
Reiley 00:41:09 It's even worse, in my opinion. You give 1.0, then enterprise starts to make heavy adoption, then you tell them, oh, sorry, now we have 2.0, and 1.0 got the.
Josh Suereth 00:41:18 about to be retired in a year. We're doing that now. We're just not being honest about it.
That's what we're doing.
Reiley 00:41:26 I want to be careful about which product we're talking about. I'll pick OpenTelemetry.net. Like, I don't work on that anymore, so I don't have any attachment, but OpenTelemetry.net, when I was part of that project.
one thing we try to make, like, really clear is we're not going to release a new version that has breaking change. Like.
We're not going to have V2, V3, V4. We're done. V1. Never going to change. Like, we know it's not perfect. We're not trying to deliver a perfect thing, but our promise, it's something that's not so interesting. It's like Linux kernel, like, most people don't care. It's super stable there. And having V2, in my opinion, is a disaster.
And do we agree or not? If your position is, let's just declare V1, next year we'll go V2, then I strongly disagree. My question is, if within the TC, like, we have this strong disagreement, I feel
We're not going to push this to a clear direction.
Like, I'm happy to step back, like, most folks think, like, having a major version every year is great, then I have strong opinion, I disagree. Then I might just decide, okay, I'm not going to get involved in this work, or if you give some, like, very simple thing, I'm happy to help, but I fundamentally disagree with, like, V2, V3 approach.
Josh Suereth 00:42:41 Yeah, Jack, my fair…
Reiley 00:42:42 It's like, we're not talking about this hard problem, we're trying to be nice people here.
Josh Suereth 00:42:47 Yeah, no, no, no, no, no, I agree. Jack, do you want to bring up what you raised? Because I think you raised a really good point in chat.
Jack Berg 00:42:54 Yeah, yeah, so, we can't group everything together. We can't have the same philosophy around 1.0 and 2.0 for all parts of the ecosystem. The APIs, in particular, really benefit from having a 1.0 and never a 2.0.
The SDK is to a lesser extent, but, like, it's still more possible to have a 2.0 of the SDK. I think JavaScript is navigating this, but I think, you know, you should be pretty cautious about it. In Java, we have plans for no, like, 2.0 SDK either. We're just gonna have backwards compatibility for as long as we can foresee. This isn't as true, and it's not as important for us
other types of auto-instrumentation distributions, like the Java agent or the JavaScript thing, or the collector. We've gotten really good in the Java ecosystem of getting into an annual cadence on the Java agent.
And it's really good for managing user expectations. It's like, you know, we have this once-a-year opportunity to say, hey, we're going to switch the default version of instrumentation from producing database, you know, experimental database metrics to the stable database metrics, or whatever else we want to bundle in there. And users are, like, comfortable with this, you know, once-a-year breaking change with detailed notes about what they need to do to accommodate it.
some backwards compatibility, or some support documentation about what we're going to do for the previous major version, and how long we're going to support that, and do patch security releases, and so there's some… there's something for everybody. But, yeah, I don't think that we should get into a one-size-fits-all mindset.
David Ashpole (dashpole) 00:44:40 a very minor point, but I also think that
It's not as important to me how often we release new major versions as that
we support them for a long period of time before removing them. So it's like, even if someone has to jump from 1.0 to 4.0,
like…
Reiley 00:44:57 No, I disagree, so I'll give you one example. I'm a customer, I use 3 components from different people, from different organizations, different companies, and one is telling me I should use 1.0, another one is telling me I should use 2.0, and they're incompatible, they fight with each other. What should I do?
Like, we never spend time to really thought about this and fight about this. We're trying to be nice and not talk about the tough problem, and this is my worry.
Like, you see, like, I fundamentally disagree some of the points. I haven't read them, because I… I think so far, we haven't brought this to the highest attention. Like, what does stabilization really mean? Do we… do we have clarity? And my assertion is, if we don't have clarity there, then we're already there.
Josh Suereth 00:45:44 It sounds like that's something we need to talk about with the GC then, too, given… given this… this blog and this push.
Reiley 00:45:50 Yeah, and I know there's a spectrum, so I'll give you two extreme examples.
In the Windows team of Microsoft, like, they take care of the stabilization and backward compatible seriously. And you see some of the applications developed, like, 40 years ago, they still work on Windows. But if you ask most of the consumers.
Like, they don't like windows. It's, like, like, too bloated, too slow, all the… all the things there, like, not clean and tidy, right? That's because it's very…
very, like, highly organized, and there are a lot of, like, you can see that's view all crazy or something. But they have this, like, governance committee, they have gatekeepers, they have shape room, all these things, to make sure you don't screw up things. But that's super slow.
And I don't think open time should want to be in that extreme, but then there's the other extreme, like, everything is just, like, free form, like, free market. We don't want to be there as well. There's a balance. But that's the hard part, because when it comes to balance.
We all have different personalities, and we learn different things, so I'm probably on the… more on the left side, like, 80 percentile, and you're probably, like, 20th percentile. And that lack of clarity, I figure, is going to be a very risky thing for… for this, like, work stream.
Josh Suereth 00:47:05 David, do you have something else you want to say? Both you and Riley still have your hands up.
David Ashpole (dashpole) 00:47:09 Yeah, yeah,
So, I was trying to think of some, like, practical ways we can help the SIGs that we're involved in. One thing that's been, like.
I'll say minorly helpful in the GoSig was to try and set, like.
delivery goals for different things, and so I think even just going to the SIGs that we work with and trying to figure out, like, what in the next 6 months could we commit to stabilizing, and then
like, as a TC, collecting that somewhere, I think, would be, like.
Reiley 00:47:35 helpful exercise.
Josh Suereth 00:47:38 Yeah.
David Ashpole (dashpole) 00:47:39 Would be a little bit less… like, we can…
go to them and say, here are the important parts of the spec that you're not implementing, like, I think is… that's part of what, Tigrin was suggesting, like.
open issues and track things and try and highlight big gaps. But also, I think the SIGs that I talk to at KubeCon are very interested in, like, getting on the stabilization bandwagon, and they all have good ideas, and so if we can, I think, just help them, like.
Set goals, and, like, make a push when the time comes, I think.
That'll be helpful.
Josh Suereth 00:48:13 Yeah, I think that's all practical things we can do. Agreed. What I…
this… I'm glad we're having this discussion. I think there's two things here in my mind. There is…
what we need to do around OpenTelemetry, and then, honestly, what we have to do around the specification, and the, like, incompleteness, and, like, things that we have left unfinished.
And not driven through. You know, like, I feel like we got into a state of, we got the initial feature done, we got the practical bits done, but we never finish. We never cross our T's, we never dot our I's.
Automation's a good example, Jack, thanks for raising that. How do we automate, like, spec compliance, or understanding if things are there, so that it's less tedious for people to track, less tedious for things? To Riley's point around these features, if we add something to the spec and no one wants it, we probably shouldn't have added it to the spec.
But helping SIGs understand the importance of things, or where they stand in that matrix, making sure that when you read the spec, you're not reading a whole bunch of, like, mixed status documents, or in-development documents, because then you don't know what's actually important and what's not.
I want to clean that up a little bit. So there's a piece of this of open telemetry overall, and there's a piece of this of us, and, like, the ownership of the spec, and things we need to do, and the specifications sake, and kind of, like…
going through a bunch of docs that need to get shored up. We've been doing this in SEMConf of trying to clean up our… the mess, if you will, of things that have been de facto stable for 5 years.
And it's not easy, but I think we need to kick off that effort, too, as well, in the spec.
Go ahead, Riley.
Reiley 00:49:52 Yeah, I, I, I remember, like.
we briefly talked about this idea, like, if you look at, like, CSS or, like, HTML, they kind of have, like, version standard. They have this, like, level 1, level 2, level 3.
And then, independently, if you have an implementation, like you have a web browser or something, you can declare, I'm level 1 compatible, level 2 compatible, and they have the test, like the ICT3 test. They show you
you complete all of them, or you're 90%, and they run this on, like, I think the open telemetry demo can be one thing. My question, there are two things. One is, do we think we want to see the spike
having this layered approach, so we have level 1, level 2, level 3, and we're not going to add some new feature back to level 1, like, that's golden.
And then…
we don't try to force, like, for example, if JavaScript is saying, we don't have customers asking for this feature, then it's fine, but it's still level 1, so you can declare you have a stable component from the backward compatibility, from performance, reliability perspective.
But you have to make it clear that you only pass, like, 97% of the IC forecast, or whatever, passed for level 1. So, having that, like, do you cover all the features for a certain level of the spec, versus what's the backward compat and reliability of spec? So there are two different dimensions, and now try to mix them.
Would that help? Because I know there are, like, web browsers, they're super stable, used by millions of users, and they don't pass any acid level tests, like, 100%. They're, like, 97 or 91, and people are fine with that.
But also, that… that's… so… so, in my opinion, like, backward compat, in the way, are not breaking the user.
is a must-have, then having this feature coverage and meeting 100% of the compliance test is something we should encourage, because the nature of the languages and the ecosystem, they might have very different opinion. Like, if you ask for permissions, it's powered. Maybe the web browser, JavaScript folks will say, that makes no sense for us.
Josh Suereth 00:51:56 Yeah, so I hear what you're saying, Riley. I don't even think that's the problem I'm talking about. The problem I'm talking about is just things aren't implemented at all.
You know, there's things just missing. Like, we added advice to the metrics API. It doesn't exist in half the languages, and when I go to use it, it's not there.
So, like, how…
Jack Berg 00:52:13 How are they getting by with that? How are they getting by without that? That's, like, essential to producing stable HTTP server request duration.
Reiley 00:52:24 But what if they don't deal with HTT Solar? They're a language focused on the client, you know?
Jack Berg 00:52:29 Sure, I get it, but that's not what we're talking about here. Like, we're talking about mainstream languages that are used for servers.
Josh Suereth 00:52:36 So, so this is more… this is more what I wanted to get at. So, so the advice stuff, like, let… like…
we added it, we want it to be stable, we want it to be everywhere, right? That's a thing that we know we need for HTTP. Let's find a way where we can look at this spec, find things that aren't complete, and drive them to completion.
And things like advice, I think, are big, where we know we needed it, we know we deferred it, we know we delayed it, and then we add it, but it's not done.
Right? It's not finished, in some sense. When I went to go use Advice recently, I was unable to find it in certain languages. But again, I only paid attention to, like, the Java bits that Jack was working on. I didn't pay attention across the board.
Right? And that's… that's where I think we all do this. But we need a way, a pro… and I want to do this with process.
Reiley 00:53:29 Because process can help us fix some cultural things, but let's make a process where we can drive these things, let's get automation, like Jack suggested, because we need it.
Josh Suereth 00:53:38 And let's figure out how to make that work. But this starts with, if we can all take a time to do this, and I know that time is the most precious resource, look through the spec.
Look through areas that you own in the spec, and look at what is still marked as unstable. And let's collect all of those in a big document somewhere.
Where we can go through and say, is this important to stabilize, yes or no?
Right? What's blocking the stability?
We should also eventually find a way to look at stable pieces of the spec that are somewhat recent, and kind of ask, is this implemented across the board?
Right? The recent spec discussion on Trace Context V2 is another example of, we need a process around driving this and helping SDK authors know how to drive important things in our ecosystem. Trace Context V2, no one will ask for.
No one will ask for. Yet, it is critical for our ecosystem that we evolve in that direction, and we as TC need to understand that and drive it. There will never be a user demand for it. What they will ask for instead is better sampling.
But we need to turn that into, okay, we have to drive Trace Context V2 support through the SDK, right?
Reiley 00:54:54 I'll give you one extreme example. So if you look at OpenTelemetry Rust, I think I put a couple Microsoft developers on that, and we treat it seriously. But if you look at that, still, the tracing API is beta.
Like, tracing API is the very first thing we added in OpenTelemetry. Like, Josh, in your opinion, it should be declared stable 5 years ago. We're not there yet. And then why do we even talk about, like, the device API? I would say, let's just forget about metrics, just get the tracing part down.
So, my heart is even to that extreme.
Josh Suereth 00:55:29 So it's different, rather. The Rust tracing implementation, first of all, hasn't existed for 5 years.
Reiley 00:55:36 What I was saying is the collector has existed for 5 years and been evolving for 5 years.
Josh Suereth 00:55:41 That's… that's the difference. I see.
Yeah, it hasn't… so Rust is still somewhat new, and the other thing is we were experimenting with Tokyo Tracing for years, where we didn't want an API, so I'd argue that the API implementation has only just begun for Rust. So I view that completely differently, and I don't want to have just a naive view of this.
I see. I understand what you're saying there. You have to look at this… it's… you have to look at things in context.
Okay, anyway, go ahead, Josh and Carlos, I forget who was first.
Joshua MacDonald 00:56:14 I'm glad that we're talking about Rust, because I often pick on the Ghostig, and I don't mean to pick on the Ghostig. I mean, like, tracing in Rust is a good example of something where no one's asking for it, because no one's using it. And that's why I'm getting back to the, like, prior point, like, we're not using our own stuff.
I don't… it doesn't matter to me if it follows a spec. If you don't want to use it, it doesn't matter to me. So, I don't think people use the GoMetrix SDK. That's why there's no, like.
the advice API is not implemented. I don't think any users are there. I mean, like, I'm probably exaggerating, but the ergonomics of that library are not quite right for me, and I'm not writing Go anymore, but I wouldn't… I wouldn't… I wouldn't recommend it to a user exactly.
Jack Berg 00:57:00 I had a similar feeling.
Joshua MacDonald 00:57:02 reasons.
Performance is not good enough.
Jack Berg 00:57:05 I had a similar feeling, Josh. Like, I think we could be thinking about this from a slightly
misguided angles, like, okay, what's in the spec? How do we… how do we get a grip on the spec and delete parts that aren't useful and finish the parts that are useful? But it's like, the instrumentation.
Will necessitate, you know, the implementation of parts of the spec that are useful.
And so, like, you know, focusing this from, like, an instrumentation standpoint, it could be beneficial, because, like, you know, if you want to do, for example, stable HTTP server metrics, you have to have the Advice API. And so that, like, kind of… that, like, teaches you which things you actually need to implement from the spec in order to provide a useful end experience for users.
And, you know, that's another thing. I think this, like, we're talking about stability, Josh, from the spec, but that's not what this blog post is talking about. They're talking about, like, stability for instrumentation. They're, like, talking about user-facing stuff, and so, like.
I think we're on slightly different wavelengths right now, talking about, like, the spec.
Josh Suereth 00:58:10 It's… so, the blog post is focused on instrumentation, it's how do we get stable instrumentation out, but the reason I'm bringing this up is, if that stable instrumentation depends on an unstable feature of the SDK, can you declare it as stable or not? And that's the whole stable by default, is getting
For example, if HTTPSMConv needs advice, advice has to be stable.
Theoretically.
Reiley 00:58:34 In short.
Jack Berg 00:58:35 Frugmentation has two components, right? So, two parts of its contract that you can consider in deciding if it's stable or not. It has the actual API that you use to configure and install it, and then it has the data that it emits.
it doesn't really matter what else happens internally to fulfill that contract… those contracts, specifically the contract of the data that's coming out. Like.
I don't care if advice is stable or unstable, if I'm getting reliable data out the other side, a stable contract of what the schema is for the telemetry data.
Josh Suereth 00:59:08 If that's the case, then we should make our recommendation to instrumentation APIs that, like, you can use experimental features of the SDK and still declare yourself stable.
I think the optics of that look weird, though, if I have an instrumentation library that depends on a alpha library that then depends on a stable library. Do you see what I'm saying?
Jack Berg 00:59:26 I, I do, I do.
Josh Suereth 00:59:27 I agree with you 100%, but this is where I think the rubber meets the road in that, and that's why, from my standpoint, what can I do as a TC? I think there's two things. One is, let's have the broader discussion with the GC around what to do. And then, the things that we own with the TC, right, I want us to define some follow-up steps of, like.
what are we gonna do to take the piece of the spec needed for instrumentation stability and get them stable? The one that I list above here about, literally, telemetry stability, that we should stabilize, of, like, what does stability mean?
So, so, I think there, there's a piece of this we gotta do. Carlos, if you want to jump in, I think we jumped over you. Why don't you, why don't you jump in with your question, because you had your hand up for a while.
Carlos Alberto Cortez 01:00:11 No, I just, like, exactly what you said. I think that we need to take actual action, you know…
you know, into what do we do? I think this is a great conversation, but I am afraid that we'll just forget about this call zone, so we should define specifically what we do. And it sounds to me like talking to the GC is a very important first step we cannot avoid.
Josh Suereth 01:00:35 Yes, I think the definition of stability is probably going to be the biggest thing.
Reiley 01:00:41 Alright, for next steps, I know what I want to do, which is to do a catalog of the spec and what's unstable that we think is needed to be stable for instrumentation stability.
Josh Suereth 01:00:49 Right? To me, the big call-out is the telemetry stability.
specification that is blocking people from marking things as stable without SEMCOM today has to change.
with that OTAP.
But that's one thing I want to do from spec side. From overall TC guidance side, we should probably define what we consider stability.
Like, that has to be defined somewhere. Does anyone want to take a crack at writing that up?
Reiley 01:01:19 I can, and I'll, like, my thinking is, I'll just throw a list of the PM questions. Like, as a user, I want this, I want that in the TC channel, then we can debate, is that something we want to consider as part of the stabilization, and what's the priority?
Because if we want everything, then we won't be able to achieve them, right? So we have to pick the battle.
Jack Berg 01:01:41 And are we scoping this to instability definition for instrumentation?
Josh Suereth 01:01:46 I think we should focus on stability definition for components that you need for a successful telemetry distribution. So this would actually be instrumentation.
SDKs.
The collector and the operator. Those are kind of the distribution components that we have that people depend on.
Jack Berg 01:02:08 Alright, I'll engage with Riley async.
Josh Suereth 01:02:10 It should also include, like, OBI, the new, eBPF instrumentation component, the eBPF profile, like, it'll apply to those, but it's like, if you think of OpenTelemetry as a product that you are consuming, the components that I consume, specification is not that. It is the components I consume.
Cool.
Alright.
We're out of time, thanks everybody. It's a good discussion.
Reiley 01:02:34 See you.
Joshua MacDonald 01:02:35 Thank you.
