SIG: Kotlin SIG
Date: 2026-06-08
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 01:58 Hello!
**Leonid Stashevskii** 02:00 M.
**Jason Plumb** 02:02 How's it going?
**Leonid Stashevskii** 02:03 Good.
I'm here for the first time, so I don't know the rules yet.
**Jason Plumb** 02:11 Well, we'll see who shows up, and yeah, welcome, I'm glad you're joining for the first time. This is an open meeting, we encourage anyone interested in the project to join and help out, so… wherever you are, it looks lovely.
**Leonid Stashevskii** 02:23 Yeah, I don't analytics.
I'm actually joined as a part of the Kotlin team, from JetBrains to…
**Jason Plumb** 02:31 Awesome.
**Leonid Stashevskii** 02:32 I'll ask you if you have any feedback or requests for the language itself.
Yeah, if you have anything to me to share, if you have from the compiler team or the libraries team, we are on our site already, too.
I mean, in case, I will collaborate.
**Jason Plumb** 02:51 Yeah, that's awesome. Yeah, we, Gosh, I don't have anything specific right now, but we love… that you all are interested and aware of this project, and are able to maybe, you know, provide some resources, some guidance, some help, and maybe there's opportunity to build in, you know, some first-class language-level, runtime-level hooks, you know, for doing telemetry solutions like OpenTelemetry, so… That's awesome.
**Leonid Stashevskii** 03:20 Nice, so if you have any kind of ideas, we can discuss it here, or we can jump in next time, or you can send a doc, whatever format works best.
So, I just noticed that there is a meeting in Guy is discussing clothing, so why not to jump in and ask if we can offer any help for you?
**Jason Plumb** 03:42 No, that's very much appreciated, yeah. I'm just getting set up right now, so we have… the way that this normally works, and it looks like you're out, so it won't really… It won't… it'll be a little challenging for you, but the way that it normally works is that we have this document that I'm now sharing, that…
**Leonid Stashevskii** 03:58 I can see.
**Jason Plumb** 04:00 Okay, cool. So this is our meeting notes, and we encourage everyone to add their name here. I will just go ahead and add that you're on here.
**Leonid Stashevskii** 04:10 Yeah, I cannot judge Brian Scotland for me.
**Jason Plumb** 04:13 Yeah.
And… then, you know, people can front-load agenda items, they can put stuff in here, topics of interest. If there's open issues or open PRs that folks want to discuss, we can do that. We can review the current project plan or milestones if they exist, and our main maintainer, Jamie, is, currently on leave of absence, and so I've been… I'm a co-maintainer, I'm helping to sort of keep things… keep the project momentum moving forward.
But honestly, I've not been giving this the kind of attention that it really deserves, so… let's, There's nothing on the agenda for today, so what I would say we'd probably do is to look at the list of open issues and open PRs, and see if there's anything that's really blocking. I am, like, until Jamie comes back, I'm basically just trying to keep the lights on. I am not… my goal here is not to, like, to really be driving and pushing this as, like, a priority for me. I'm just hoping to keep it on track, so…
**Leonid Stashevskii** 05:18 Nice, thank you for doing this.
**Jason Plumb** 05:21 Cool. And… Hanson's on the call, he's a long-time contributor, he helped with the donation, he knows a lot about this thing. And, yeah, I just wanted to give a chance to say hi there, too.
**Hanson Ho** 05:33 How'd like.
**Leonid Stashevskii** 05:35 Dang!
**Hanson Ho** 05:37 It's, it's Leonid?
I hope I'm pronouncing it correct.
**Leonid Stashevskii** 05:41 Yeah, absolutely correct.
**Hanson Ho** 05:43 All right, cool. Yeah, Jamie's been the force behind most of the effort. I'm also here, hoping to step up a little bit in the next few weeks to kind of, you know, keep things going. Right now, we're focusing on trying to get stability, in the API, and also get the… first implementation out, in a way that you know, folks shouldn't find any issues with to use in mobile without, you know, manual workarounds and things like that, that they might have to do with the Java SDK, vanilla SDK. So, Yeah, right now it's, it's, it's, it's… focusing on the right things, and I think we're trying to figure out what those are.
**Leonid Stashevskii** 06:29 Good, good. So, right now you're focusing on making the Kotlin SDK without Java.
Where is it, like, the Javaish SDK with the Kotlin bridges to mitigate the problems?
**Jason Plumb** 06:44 I think the priority first is to get the API stabilized, so, you know, the way that OpenTelemetry works is there's an API layer that's purely the interface layer that implementations can code to, and then there's an underlying implementation of those interfaces that form the SDK.
And everything that's Java-based right now is based on the OpenTelemetry Java API and OpenTelemetry Java SDK. And so we're gonna work on stabilizing the API layer first, and once we've decided that those interfaces look… correct, or that we don't want to change them for the near future, then we can change priorities and then start working on the KMP implementations.
**Leonid Stashevskii** 07:25 Nice, thank you for the short introduction. I was long time on the KTOR team, and our team contributed to the OpenTelemetry SDK, and… So, we're more or less aware of the details of the instrumentation and how the API layer works.
So, yeah, but it's surprising to know that you're thinking how to make The… how to reduce the amount of workarounds, to apply this to the mobile. That's interesting.
By the way, could you tell me where can I find the link to the document, and maybe read the previous agendas and understand If, our expertise might be helpful.
**Jason Plumb** 08:13 Sure, yeah, so I pasted it in chat, but if that's not convenient, the way to get to it is to go to the OpenTelemetry…
**Leonid Stashevskii** 08:20 That's fine, I can see it.
**Jason Plumb** 08:22 You can go to the… you can go to this OpenTelemetry Community page, and then on the main README, if you just look for Kotlin, there's links to the Google Doc.
And the Slack channel, and the calendar.
**Leonid Stashevskii** 08:36 Good, thank you.
**Jason Plumb** 08:38 I think, Carlos, since you're on the call, is Ella lead a really hard liaison? Is that true?
I guess she is.
**Carlos Alberto Cortez** 08:45 Yeah, she's.
**Jason Plumb** 08:46 Okay.
**Carlos Alberto Cortez** 08:47 Yeah, she's mostly responsible for, in case we need to, To talk to her about something important from the leadership Like, beep.
**Jason Plumb** 08:56 That's right, she was involved in the onboarding of this. Okay, yeah, I had just forgotten. Okay.
Cool, so that, yeah, that's where the dock is.
Sweet, so yeah, I'm trying to think if there's anything else, like, about the history, or if there's any, like, specifics about OpenTelemetry that we might want to share with Leonid, because…
**Leonid Stashevskii** 09:17 No pressure at all, I will just…
**Jason Plumb** 09:18 Yeah.
**Leonid Stashevskii** 09:19 the… in two weeks, I guess, and we can repeat. If you have any questions regarding the compiler API, if you're using… or the KSP layer, or the Tulink layer, wherever it is, just, get… get them there.
**Hanson Ho** 09:38 Cool.
**Jason Plumb** 09:39 That's great. Yeah, go ahead.
**Hanson Ho** 09:41 I think we might have some, but I think we need probably a little bit of time to, like, gather them, because I think we had thought of, you know, that part of it as something that, you know, we're not going to be able to, like, you know, get any answers for, so we're kind of working around it. There are certain issues, especially with making a KMP library only with a…
**Leonid Stashevskii** 10:03 Boom.
**Hanson Ho** 10:03 We were… but that's… that's, like, more, I had to think about what specifically we were asking for first, like, we had some… some things that we wanted to do, at least initially, before the project was donated, you know, for this to be a standalone, without having to, like, you know, Anyway, we'll definitely reach out once we've gathered our thoughts.
So it's more…
**Leonid Stashevskii** 10:27 No problem. Absolutely no rush. Just thank you folks for making this project, and it was really surprising to us to discover that you're doing this, and we just… realize that there is a Kotlin group, an open telemetry reporting specifically on this, yeah, just… We're really happy.
**Hanson Ho** 10:48 Yeah, I submitted a talk for KotlinConf this year to talk about this, but, you know, I guess it wasn't super, exciting, so…
**Leonid Stashevskii** 10:56 No, it was a huge competition. It's not on you. We had more than… like, 10 candidates per slot this year. It was a really huge competition.
**Hanson Ho** 11:07 Oh, sure, no worries. Totally get it.
**Leonid Stashevskii** 11:10 app.
**Jason Plumb** 11:14 Well, we have a lot of open PRs, and you can see by all the blue on here that I have not reviewed many of them, so there's a bunch that I need to… to follow up with. There are a lot, I'm just noticing at a glance, there are… we have a lot of open PRs.
that are opened by automation for things that we may not be ready to upgrade yet, like min-AG… like, I think we talked about this last time, like, min-AGP, and then Kotlin version itself.
And… I'm not touching those presently, just because I know that they're pretty disruptive, and I don't know what our… I don't know that we've codified our policies on when we upgrade. It's so early.
that… slamming to newer versions is probably fine, but we will need a… we'll need to be careful about that going forward, right? Like, especially once we approach stability.
**Hanson Ho** 12:07 slightly newer versions, as long as it doesn't raise our minimum version. So, like, you know, with AGP, that will probably do that.
**Jason Plumb** 12:17 Yeah. Yeah.
**Leonid Stashevskii** 12:18 Yeah, for the Kotlin specifically, you can set the target language version.
And it means that you will be using the new toolchains, the new Kotlin version to compile your stuff, but you will be outputting the binaries that will be compatible with older version of Kotlin, so it's… if you haven't, made this, parameter, I would highly suggest to turn this on.
to always have a target-specific version for Kotlin and upgrade it explicitly, it's important for the library.
**Hanson Ho** 12:53 Yeah, we do. So I think this is going to be fine, because we're using 2.3 right now, and compiling to 2.0 for a minimum requirement, so I think going 2.4, unless that bumps the backwards compatibility to 2.1.
**Leonid Stashevskii** 13:07 Yeah.
No, no, it's not bumping. It should be 2.0 still.
**Hanson Ho** 13:11 Yeah, so, so I think, I think, I think, changing the runtime would be totally fine.
**Jason Plumb** 13:18 Is that in the root of the project?
**Hanson Ho** 13:20 Yeah, it's, it's, it's defined somewhere. That's why we can support… that's why we could use, compile with 2.3 and, and support, 2.0.
**Jason Plumb** 13:30 Great.
I just don't know where that's… I don't know how this… build is wired up very well, so I'm still hunting it.
**Leonid Stashevskii** 13:39 Yeah, there are lots of things. I think it should be, like, target version somewhere in the Gradle configurations.
**Hanson Ho** 13:46 I think there's a plugin where we define… Oh, yes.
**Leonid Stashevskii** 13:51 If it's Clyde.
**Hanson Ho** 13:52 Just to go search for 2.0.
**Jason Plumb** 13:57 30 files.
**Hanson Ho** 13:59 Liver.
**Jason Plumb** 14:00 Because of Apache… because I have an Apache 2.0 license.
**Leonid Stashevskii** 14:04 Oh, yeah.
**Jason Plumb** 14:06 But here it is, yeah, it's in here, I think. These, right?
**Leonid Stashevskii** 14:09 I mean, Sabor East Coast version, yeah.
**Jason Plumb** 14:12 Yeah.
**Leonid Stashevskii** 14:15 Lovely, so you're doing this right, I'm ready.
So, if the CI is green, the immersion Kotlin upgrade will be fine.
Because it's worth…
**Jason Plumb** 14:24 But this is, you know, we gotta kind of see why this broke. I don't know, I haven't looked at… the first time seeing this.
**Hanson Ho** 14:31 I'll take… I'll take a look today. I have some time today, so…
**Jason Plumb** 14:35 Thank you, Hanson.
I mean, some of these, some of these are, yeah.
Okay, that's warnings.
**Hanson Ho** 14:46 We might fail on warnings, but, we'll see. I'll take a look.
**Jason Plumb** 14:51 So, no, here it is. This… it's incompatible.
So it's AGP, though.
**Hanson Ho** 14:55 Oh yeah, well, AGP 8.13 is definitely incompatible, so that one we can close.
**Jason Plumb** 15:00 Yep.
But this bump of Kotlin version says it's incompatible with the AGP that we're using.
**Hanson Ho** 15:08 Mo, though, we should have a look.
**Jason Plumb** 15:10 Yep.
**Leonid Stashevskii** 15:11 By the way, do you enable compiler warnings as errors?
as a…
**Jason Plumb** 15:18 I think so. I think we don't yet, because, like, this warning was up here, and it failed because of an actual failure, I think.
**Hanson Ho** 15:29 There are some places where we do. Well, maybe it's the other repo, actually.
**Jason Plumb** 15:33 Good practice, though.
**Hanson Ho** 15:37 But yeah, I'll take a look at some of this stuff, today.
**Jason Plumb** 15:41 Yep.
So we don't think that was a…
**Hanson Ho** 15:53 No.
**Jason Plumb** 15:54 So, I don't… do any of… like, Hanson, do you have any open PRs?
**Hanson Ho** 15:59 I have one that I haven't submitted to finish the, the, not throwing in a knit time kind of thing, but I have to… I was gonna look at some of these, these reviews,
**Jason Plumb** 16:12 Yeah, Mitchie… Mitchie's been helping, like, add… add some PRs. Do we… do you know them?
**Hanson Ho** 16:18 No.
**Jason Plumb** 16:19 Okay, I think they're just a community contributor, so…
**Hanson Ho** 16:21 Yep.
**Jason Plumb** 16:22 If you notice, like, they've got a bunch that are open already, and it's awesome because these are all… Pretty well scoped, like, they're nice and small.
**Hanson Ho** 16:32 Yeah.
**Jason Plumb** 16:34 Yeah.
So, yeah, they rebased, cool. And then, as a reviewer, what I usually do is, if I gave someone an approval, and they need to rebase, I often just double-check to make sure they didn't completely change the entire… Except, you know… And they didn't in this case.
But that's always an opportunity to sneak something in, and it pains me.
But this one looks good.
Anyway, yeah, that list of PRs is getting pretty big, and this person's, like, helping out a lot, so that's great.
**Hanson Ho** 17:13 Definitely. I was gonna catch up last week, but ended up catching up on other things, so…
**Jason Plumb** 17:22 Looks like David started this a while ago, but it stalled out, probably.
**Hanson Ho** 17:27 Yeah, Dave's on the call, so we can add it to the end of the agenda.
**Jason Plumb** 17:34 A very long agenda.
Alright, are there any of these that we want to talk about specifically?
**Hanson Ho** 17:45 I have to look at it first.
**Jason Plumb** 17:47 I'm just behind.
Okay, well, I won't… I won't force, like, a, you know, a PR review of all of these. We can start going through them, but, I think this one also may have required a…
**Hanson Ho** 18:06 Are there new issues?
I think it's… it was, well, 74, oof.
**Jason Plumb** 18:14 The newest one's 2 weeks ago, so that was from Jamie, and it looks like, no, there are no new.
**Hanson Ho** 18:20 Got it. So, yeah, these are, these are effectively the outstanding, things, probably, that we want to do to stabilize the APIs and stuff, so…
**Jason Plumb** 18:29 Yeah, exactly, and he's done a really good job of making these all kind of, like, very specifically feature-targeted and small in scope, or smaller in scope, and then also labeling them, or actually putting them on milestones, so… the tracing API milestone's 68% complete, here's what's remaining. You know, he's done a really good job of, like, project management with that kind of stuff.
Way, way better than I've ever done on the Android, for sure.
So, I think this one was also rebased, yeah.
Yeah, this one was very targeted.
Yeah.
Don't damage that.
**Hanson Ho** 19:16 I put a topic in there.
I think we had a couple meet… a couple weeks ago, we had a meet… we had some discussion about the, Attributes API, and whether or not, what we have is okay.
I think I posted… did I post in Slack, or here, or something like that, about, the, the… the type being in the set attribute method names. I talked about, I think it's fine having not that… having that not block the initial, you know, stabilization.
Because that is still the most, intentional API we can have.
having the type being inferred or, you know, part of the parameters. There's still, there's still kind of ambiguity, potentially, or easy, room for mistake. And since we have what we have already, I don't feel super compelled to, like, change everything.
to a, type-inferred API.
And if we want to remove it, in version 2, I think it's reasonable to keep these as… as deprecated.
Until then, if we choose to do that, but I don't… I don't see that being a huge issue right now.
**Jason Plumb** 20:34 Yeah, I'm not losing sleep over this. I think it's maybe not as clean as I wish it were, but.
**Hanson Ho** 20:43 Like, adding an inferred one is an additive thing that we could do, and then if that one, you know, proves to be popular enough, and that people don't have issues where the, you know.
they don't want, like, a str… An int, but in a string format, and have that be, like, an issue. Then we can deprecate and remove. But… it's a bit of verbosity, which mirrors the Java API at this point, so…
**Jason Plumb** 21:13 Yeah, we don't have any other open issues on the Attributes API, so I think we're in pretty good shape to call that stable if we're ready to do that.
**Hanson Ho** 21:22 Yeah, that's the one that's, like, blocking everything, almost, because everything that we want to stabilize has attributes on it, so…
**Jason Plumb** 21:28 Do we have any other modules that we've marked stable already?
I've forgotten.
**Hanson Ho** 21:33 I don't think so, because everything is attributes, at least the main APIs, the log event API and the tracing API.
**Jason Plumb** 21:47 Yeah, so the way that we did this in Android, at least, is that we had… I need another cup of coffee.
So… Bleach… Yeah, we put stable equals true, I think, in the Gradle properties for the ones in Android that are stable.
But we probably haven't hit that with any of these yet.
**Hanson Ho** 22:17 No, because I think we wanted to declare logs, as our first one, but then that pulled in attributes.
**Jason Plumb** 22:25 Right.
Okay, so we need to mark that stable, so… I will open an issue to do that work, like, I don't know that the build respects that stable equals true yet, if this is the first time we're doing it.
**Hanson Ho** 22:40 Jamie should have created a bunch of issues, and milestones, so we could probably look at the stability milestone and kind of just walk that tree and see if, See if there's anything that…
**Jason Plumb** 22:51 There's, like, an umbrella one, you're saying?
**Hanson Ho** 22:54 Yeah, I want… yeah, yeah, like… like, logging API, for instance, if you click on that, Hmm, maybe not.
**Jason Plumb** 23:02 But what I was saying, Hanson, is that, like.
I don't know that the… even if we were to put that property, that Gradle build property of, like, stable equals true, I don't know that the build respects that to drop the alpha suffix.
**Hanson Ho** 23:13 Got it.
**Jason Plumb** 23:14 That makes sense.
**Hanson Ho** 23:15 Yeah.
There's no way to declare stable, even if, in theory we can.
**Jason Plumb** 23:25 Right.
**Leonid Stashevskii** 23:31 Yeah, the flagship work for the API file that's generated.
**Jason Plumb** 23:41 Can you say that one more time?
**Leonid Stashevskii** 23:42 The flag should work for the API files. I think you should be using the binary compatibility validator, which dumps the public declarations to the text files, so the build will fail if you change the public API, since it's public, and the flag should be specifically for that.
**Jason Plumb** 24:00 Yep, we use that.
**Carlos Alberto Cortez** 24:04 By the way, I have a cool question. If you were to actually make the API artifact stable, and with only attributes stable, that means that you're still bringing everything that is margin stable, like resources and everything else, it's not crop up.
**Jason Plumb** 24:19 That would be the idea, yeah. So everything else should have alpha in the suffix, except for the things that we've marked as stable.
So we're using that as a stronger indicator than SEMVER, if that makes sense.
We can't… we can't version our components independently. They all.
**Carlos Alberto Cortez** 24:35 Yeah, of course.
**Jason Plumb** 24:36 Yeah.
**Carlos Alberto Cortez** 24:37 Yo.
**Jason Plumb** 24:37 Is that what you were asking, Carlos, though?
doomed.
If I go out here and show you… Heartland… And, like, we don't have… do we have a module for, attributes?
Maybe that's the problem, right? Is, like, I don't know where… attributes is part of the API, right?
**Hanson Ho** 25:00 Yeah, we must be part of the common…
**Jason Plumb** 25:06 In any case, the… Oh, these do not have alpha in them.
So maybe we were just using SEMBER as the stronger indicator.
**Hanson Ho** 25:18 Yeah, I don't know, I don't know if we have, I don't know if we have the same issue as Android in terms of the renaming stuff.
**Jason Plumb** 25:28 But then, I guess the question is, how do you signal that something is stable?
Right? Like, we can… we can write words in a Markdown document, but that's not a strong enough signal. We need… there needs to be some indication that something is stable or not.
**Leonid Stashevskii** 25:48 We use two things internally. We use the stable releases as 1.0, like, after one first version, everything is stable, but in terms of the single bundle.
You can mark, the, experimental APIs instead, with opt-in annotation.
**Jason Plumb** 26:12 Yeah.
**Leonid Stashevskii** 26:12 That will make it, usage opt-in, so people who use an experimental API will have to opt in first.
And be ready to, like, fix stuff when upgrading versions.
**Hanson Ho** 26:29 Yeah, we also use an opt-in annotation, so I think one concrete way of doing this is we can drop that opt-in for APIs that we've declared stable.
**Jason Plumb** 26:46 Yeah, like this, like, is the… yeah, so this thing is what you're.
So to mark… yeah, so to mark this as stable.
we would drop this. I mean, that's a… that's a pretty strong signal.
It would be nice if, through the dependency declaration, you also had some indication.
But until we hit 1.0, which kind of implies everything, right?
Yeah. Which is gonna… it's gonna take us a while to get there. It'd be nice to have something… in the interim, or in the shorter term, that could declare a specific module as stable, and I don't know what that mechanism would be unless we start using alphas.
**Hanson Ho** 27:26 Yeah, well, one thing we don't want to do is change names of the actual artifacts, because we're going to get declared stability one module at a time, so, you know, we're going to have a combination of, like, stable and non-stable, and right now, nothing is stable, so it's a much bigger ask to say, hey, you know.
if you want to use tracing, you have to use B, like, you know, apt into unstable, while some underneath, there's some things that are… that are stable. I think that's why we didn't have, like, the artifact names be… be what they are, like, renaming that.
**Jason Plumb** 27:59 proper.
**Hanson Ho** 28:00 Yeah, with Alpha.
**Jason Plumb** 28:01 Because alpha's only part of the version, like, it's not… it doesn't change the coordinates.
**Hanson Ho** 28:07 Okay.
**Leonid Stashevskii** 28:10 You can also split the experimental annotation.
Like, if you have a separate annotation for the Attributes API, or the Traces API.
Like, you can drop one annotation and keep other.
**Jason Plumb** 28:28 Leonid, are you finding that the use of the experimental API is becoming, like, pretty, canonical? Like, pretty idiomatic for people to understand when something's stable or not?
**Leonid Stashevskii** 28:39 Yeah, I think it's a… it is, and we even not call it, like, the… the experimental API notation is inside your own codebase, so you can name it as you want.
**Jason Plumb** 28:49 Right, yeah, yeah.
**Leonid Stashevskii** 28:50 So, it's, like, you can name it, like, Unstable, or you can name it as, like, as whatever you want, so you can have the experimental attributes, API, experimental, whatever, I want API, you can have multiple of them.
and versions, APIs within the… language itself. We're also going to make some moves to let people have different levels of reporting, like, in the future, you will be able to declare experimental API with warning level.
Leave a message, like, what kind of things you're meaning by this annotation.
But yeah, it's a general idea that you want to hide some API, you use the annotation to do this.
**Jason Plumb** 29:40 Okay.
Yeah, I think I had forgotten that this was ours. It wasn't a language feature.
**Hanson Ho** 29:47 Yeah, we use the require opt-in annotation and declare opt-in level warning.
**Jason Plumb** 29:54 That's right.
Well, I still don't have a good answer. I mean, I don't… I'm not happy with our current answer.
**Hanson Ho** 30:05 I'm pretty sure we discussed this, so let's take a look at some of maybe the old discussion. Okay.
**Leonid Stashevskii** 30:11 Hey folks, thank you for, joining. I will leave it here. We'll join in two weeks, to the next meeting. If you will have any questions, or need any feedback, or whatever.
**Jason Plumb** 30:26 gold.
**Leonid Stashevskii** 30:26 Let me know. Yeah.
**Jason Plumb** 30:27 Yeah, thanks so much for joining, it's nice to meet you and see you in person. If you want to lurk on the repo and leave feedback, comments, or anything about any of the PRs, very much welcome, and we could use a language expert to, like, keep us on track when stuff is not, you know, canonical.
**Leonid Stashevskii** 30:44 Yeah, if you need any help, like, from the compiler experts, or, like, the libraries experts, I can bring you the related folks, because I'm not an expert on everything. We're already with Cage, our team.
contributing to the OpenTelemetry, so, like, kind of… my folks already, like, part of the… the discussions, but yeah, if you need, like, some… deep topics, then I'm maybe not the best guy, but I easily can find one.
**Jason Plumb** 31:15 Awesome.
That's great.
**Leonid Stashevskii** 31:17 The tooling is included, by the way, so the IntelliG plugin, Android Studio, all this stuff is also, like… No, probably not.
**Hanson Ho** 31:26 Excellent. Awesome.
**Leonid Stashevskii** 31:28 It was nice talking to you.
**Jason Plumb** 31:30 Thanks, you too.
**Hanson Ho** 31:30 Thanks, Nice, Elena.
**Leonid Stashevskii** 31:32 Alright.
**Hanson Ho** 31:37 I think having some help on, context propagation would be… would be interesting, like, let's see what they're… especially if they've worked on some KTOR stuff, especially mobile usage, be interested to see what their opinion is about, automatic context propagation, and how they might solve that, or… or not.
**Carlos Alberto Cortez** 31:56 Yeah, it could be… it would be worth preparing some summary of what's… The situation, the plan, and the challenges, of course, instead of trying to just think about that right the moment.
**Hanson Ho** 32:09 Oh yeah, that's why.
**Carlos Alberto Cortez** 32:12 It was wise to not ask him, not today.
**Jason Plumb** 32:21 Yeah, so we did… we did talk about some of this previously, Hanson, I appreciate that.
check, but I don't remember… like, I'm so sleepy right now.
None of this is fresh in my brain.
**Hanson Ho** 32:39 Yeah, let's take… let's take a look.
and make sure we have something that we can declare stable first. Because until we do, you know, we can still kick this down… kick the can down the road.
**Jason Plumb** 32:56 Yeah, but you, I mean, we were talking about the attributes stuff, but that's part of the core… Yeah. API common, anyway.
**Hanson Ho** 33:05 Yeah. And you can't really… I mean, it's not useful to have… I mean, really, what we wanted to clear stable is individually usable APIs, so, like, logging, for instance, or tracing.
So…
**Jason Plumb** 33:19 Yeah, if these were all separate modules, and this wasn't all just the universal API module, then it would maybe be a little easier, but with these being so…
**Hanson Ho** 33:32 But we definitely talked about whether we want to rip this apart just so we can declare stability. I think the decision was.
**Jason Plumb** 33:39 in the mold.
**Hanson Ho** 33:40 No, yeah.
Because we can do… we can move tracing and logging metrics out on their own, but then they still depend on everything here, which is common, unless we want to move each single one out of there. But then, you know, what does that even mean? If attributes are stable and, say, context isn't?
**Jason Plumb** 33:57 Yeah, maybe…
**Hanson Ho** 33:58 mode.
**Jason Plumb** 33:59 Maybe in the short term, we just create a matrix that we can put in here?
To sort of help us understand, like, which components we've declared stable, even if they're… even if it's not reflected, but just so we don't lose track of where we are.
**Hanson Ho** 34:15 Yeah, for sure, just like… just so that we know, conceptually. Yeah.
**Jason Plumb** 34:21 That's where I'm at right now.
**Hanson Ho** 34:23 Yep.
And we should also have… well, yeah, and that matrix should be, like, I guess the rows, Which… which… API services do we consider, to be… to have a stability attachment to it?
**Jason Plumb** 34:47 Yeah, and it's… I think it's okay for us to say, you know, this is… It's gonna… it's… effectively, it's a release candidate until we hit 1.0.
But the matrix can help us to declare that we want to minimize or eliminate changes, and maybe we couple that with removing the experimental API.
And then the.
**Hanson Ho** 35:11 Something like that.
**Jason Plumb** 35:11 Those two things probably get us there, yeah, okay.
**Hanson Ho** 35:14 I like that.
**Carlos Alberto Cortez** 35:15 Yeah, that should work, yeah.
**Jason Plumb** 35:33 And then, remove any… Yeah. And then when we go… Okay, so that, you know, and if something comes up.
you know, if we really decide we do need to change something in that API, we can still do that before we hit 1.0.
But the intent will be to try and minimize that. Okay, I think I can live with that.
**Hanson Ho** 36:14 I think by the time we can put it in even the matrix and remove the API, it would be, like, for the most part, as good as we can make it, with the current information that we have. So, I'm okay with just writing that out.
**Jason Plumb** 36:27 Cool, I'll take that as an action item.
**Hanson Ho** 36:30 Excellent.
**Jason Plumb** 36:39 I have to add it to my ever-growing list of… In another window, the list that just keeps growing and never shrinks? Yeah.
**Hanson Ho** 36:46 Good.
**Jason Plumb** 36:46 Top of it, though, so that's good.
I just have to… I just have to not have more things ahead of it by the end of my, you know, morning meeting block, is what that means.
Okay, we technically have 10 minutes left, how do we want to use that time?
**Hanson Ho** 37:08 I'm good with getting it back.
So I can get 10 more minutes to look at this stuff, so…
**Jason Plumb** 37:14 I'm okay with that, too. David, do you have anything you want to bring up?
Okay, that's cool. Carlos, in case you didn't hear, David is now an approver in OpenTelemetry Android as well, so…
**Carlos Alberto Cortez** 37:33 Nice.
Perfect.
Nice, pretty nice, pretty nice.
**Jason Plumb** 37:38 Yeah, yeah. So, let's call it there. Appreciate you all.
**Hanson Ho** 37:41 Alright?
**Jason Plumb** 37:42 Alright, take it easy.
