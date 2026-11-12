SIG: Zig SIG
Date: 2026-11-11
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Antoine Gagniere** 02:16 Hey! Hello?
**Francesco Gualazzi (OpenTelemetry)** 02:20 Hello, do you hear me okay?
**Antoine Gagniere** 02:22 Yep.
**Francesco Gualazzi (OpenTelemetry)** 02:25 Exactly.
**Antoine Gagniere** 02:33 Yep.
**Francesco Gualazzi (OpenTelemetry)** 02:34 I don't.
**Antoine Gagniere** 02:35 It's a holiday today.
**Francesco Gualazzi (OpenTelemetry)** 02:38 The holiday in France?
**Antoine Gagniere** 02:40 In France, yes.
**Francesco Gualazzi (OpenTelemetry)** 02:42 Oh, also in Poland and in Serbia, if that concerns you. Only in Italy, it's not.
Hey, beauty!
Oh, for your own understanding, Antoine, you know this is recorded, right? Okay.
**Antoine Gagniere** 02:56 Oh, yeah, yeah, yeah, right.
**Francesco Gualazzi (OpenTelemetry)** 02:59 I mean, just, just… I'm… fairly, I have to say, Convinced that the meetings I call the store securely, but probably they're also ending up on YouTube, I don't know, but… I don't remember. Maybe, maybe they are. No, you know, you shall know.
Okay. You doing okay?
**Antoine Gagniere** 03:26 Yeah, yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 03:28 First of all, congratulations for being, a maintainer. I mean, this was, like, from the get-go. I thought… I immediately raised that, that issue. Which I hope is now closed, no, I guess?
Yee!
Hello, beauty!
Let me check.
It should be closed.
Because now the teams are… A.
Give this name… Issues here… But do what?
**Antoine Gagniere** 04:08 Ours?
**Francesco Gualazzi (OpenTelemetry)** 04:10 Hey, Yeah, it got closed. Pretty good, okay.
Okay.
Let's wait another minute, and then we start. I know Giovanni wanted to… 1 to 2? 1 to 2… Speak about the conformance to the latest,
**Antoine Gagniere** 04:39 Yeah, yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 04:39 Yeah?
**Antoine Gagniere** 04:41 Yeah, he mentioned it to me in the… In the messages.
**Francesco Gualazzi (OpenTelemetry)** 04:46 So, hopefully he joins, otherwise we…
**Antoine Gagniere** 04:49 But we can start reading… Wait, let me, let me… Fitch brief.
**Francesco Gualazzi (OpenTelemetry)** 04:58 Yeah, I can present.
Yeah.
Okay, let me know when you see it, if you see it.
Here you go.
Okay.
**Antoine Gagniere** 05:35 What do you want to say.
**Francesco Gualazzi (OpenTelemetry)** 05:35 Can you see?
**Antoine Gagniere** 05:38 Yeah, good.
**Francesco Gualazzi (OpenTelemetry)** 05:41 Papa. Can you see? Papa?
of Antoine.
Alright.
So that one… I created.
And it's this one.
**Antoine Gagniere** 05:58 Right, yes, it's this one, yes.
**Francesco Gualazzi (OpenTelemetry)** 06:00 So, yeah, when we developed, we were targeting 148, but now… There's been, like… 14, yes, 14, minor versions increase, and If… even if we're gonna release an alpha, it should be, let's say, up-to-date as much as possible.
with that. So, for that, I will add this one to the Alpha release milestone.
Which, let me just, give a quick look at that.
Okay.
Right, so I… again, I think it's completely doable by end of January, hopefully, maybe… But the start, let's say the start of the new year could see the alpha read, right? Because we've already done one-third of the… of the issues, and if I'm looking at this… And this… those are pretty lightweight, you know?
probably Clock Zig and Windows, you know, if we… if we solve Clock Zig, then we immediately Solve the window support, gRPC compression… this one is probably the biggest, huh?
Because this is a simple bug.
think…
**Antoine Gagniere** 07:25 I think… One is, freeze, frozen, and I…
**Francesco Gualazzi (OpenTelemetry)** 07:31 Is it? No, I am moving my mouse. Do you see it?
**Antoine Gagniere** 07:35 Yeah, no, it's still showing the conformance latest.
**Francesco Gualazzi (OpenTelemetry)** 07:39 Oh, okay.
Okay.
**Antoine Gagniere** 07:44 Oh, yeah, no, yeah, it changed now, yeah.
**Francesco Gualazzi (OpenTelemetry)** 07:46 Oh, okay, okay, okay, sorry for that. I… Because it opened in a new tab. Oops, apologies, I didn't notice that. Okay.
**Antoine Gagniere** 07:54 Okay.
**Francesco Gualazzi (OpenTelemetry)** 07:55 So, I was saying, the lighter one, the bug, which I think might already be resolved.
by the PR that emerged, A couple of days ago, but yeah, let's verify that.
**Antoine Gagniere** 08:07 Yeah?
**Francesco Gualazzi (OpenTelemetry)** 08:08 This one needs to be investigated. And I was saying, if we address or even remove Glock Zig and, We are able to support Windows immediately, I think. Then the biggest one is the compression.
the… this… this one, which I put in the milestone, but possibly we can… take it away, I don't know, because it's like an embellishment, right? It's not… It's not something that is functionally… Right, right.
**Antoine Gagniere** 08:41 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 08:42 That doesn't bother the correctness, huh?
**Antoine Gagniere** 08:44 Right, it doesn't need to block the release, right? Exactly.
And also.
**Francesco Gualazzi (OpenTelemetry)** 08:48 George.
**Antoine Gagniere** 08:49 change recently, so… I just need to check if it's still a…
**Francesco Gualazzi (OpenTelemetry)** 08:55 Okay.
So the biggest one is this one, actually, the conformance, right? Where… Giovanni did a great job already in summarizing the stability and the items. Also, adding the version. Hopefully, this is… done not manually, but… oh yeah, with some Agenting help. Okay, that's good.
And then… You know, we also have some… Evidence in the code, which we can immediately turn into sub-issues, if we want.
to tackle that. But again, because these are so many, probably this one is going to be… and again, I don't care about the development, because one of the Dogma that we say we will just support the stable for now.
So the development, I think some of that is… Going to be in, but, we don't need… them for their needs. But the stable… the stable components, yes. So, See?
I think this is done, yeah?
Okay… Right. We can, let's say, we can… we can try to create some issues out of it, I can do that, and then one by one, we… we… C.
We try to tackle.
Right? Because this is… this is definitely the biggest one, okay? The other ones… again, I'm not gonna… Not gonna expect too many… Many time spent on them, but for this one, we really need… First, we have stabilized all the code, for example, that this is in, which I'm reviewing.
And maybe this one from Daisuke, although I haven't heard from him recently on this one. Let's see if he progresses.
And then once we have the code, say, that is stable, we can move.
Easily into tackling One… each one of these individuals.
What do you think?
**Antoine Gagniere** 11:12 Yes, so the Windows one, is it a hard requirement for the release?
**Francesco Gualazzi (OpenTelemetry)** 11:21 Yes.
Yes, because… You would not expect that, but there are a lot of Windows developers also using Zig for cross-compilation benefits. So, they develop on Windows because it's corporate machine, and then they cross-compile to Linux ARM, Linux x66, so… So, if they are unable to compile locally and running the test, It's… It's not. So I'm not confident… I mean, again.
In an ideal world, there is only one operative system, but because development happens at least on three major operative systems, Linux, macOS, and Windows, we have to support all 3. Not to say that they were able to support all runtime behavior on all three equally, but at least they did, you know, it compiled. Yeah.
We should…
**Antoine Gagniere** 12:19 Okay, yeah. Because GRPC… Would be… would require a bit more.
**Francesco Gualazzi (OpenTelemetry)** 12:26 Oh.
Good point.
Wait. gRPC uses Jerva, which uses… a C library, right?
**Antoine Gagniere** 12:40 Right, yes. I guess the Google LibJob PC does support Windows, but my build script does not, like, I need some work, right, to… for Windows.
**Francesco Gualazzi (OpenTelemetry)** 12:56 Mike?
**Antoine Gagniere** 12:58 Maybe not a lot, just I never tried, to be honest, so…
**Francesco Gualazzi (OpenTelemetry)** 13:02 Okay.
I mean, if… Can I do?
**Antoine Gagniere** 13:07 like, I…
**Francesco Gualazzi (OpenTelemetry)** 13:08 That's green.
**Antoine Gagniere** 13:09 Yeah. Ma'am? I create an issue.
**Francesco Gualazzi (OpenTelemetry)** 13:12 Okay.
**Antoine Gagniere** 13:14 I'll create an issue in my report.
**Francesco Gualazzi (OpenTelemetry)** 13:20 Let him, let him say, you know, Zig is good.
Zig… Zig… Zig…
**Antoine Gagniere** 13:27 Zig to this Zig?
**Francesco Gualazzi (OpenTelemetry)** 13:29 Can you say Zig?
**Antoine Gagniere** 13:31 Zig? Zig went there.
Zig. TD Zig.
**Francesco Gualazzi (OpenTelemetry)** 13:35 Almost.
To the Zig.
**Antoine Gagniere** 13:39 Yeah, okay, but… let's… because without gRPC, I'm… you know, you remember someone merged the PR but cloak, last week.
**Francesco Gualazzi (OpenTelemetry)** 13:52 Oh yeah, yeah, yeah, moving to timestamps, standard timestamp would be fast.
**Antoine Gagniere** 13:55 So, maybe we can already… I think he even mentioned in the comment, he said, yes, he built to Windows and it worked.
**Francesco Gualazzi (OpenTelemetry)** 14:03 Oh, is it? I asked the.
**Antoine Gagniere** 14:05 Let me, let me try right now.
**Francesco Gualazzi (OpenTelemetry)** 14:11 I pinged the reporter of the… of the original issue to see… but again, the definitive, the definitive, confirmation we will have when we add the CI, which, again, is trivial. I can start doing that.
Actually, this is meant to me, so I should probably get going.
Adding the Windows machine in the matrix is… Not a problem.
But before that, I would like to see if you know, we can close this, because again, if Clock Zig now… it only contains a handful of functions, then we can… probably just move it into, I don't know, helpers or whatever, right? Because… Clock used to be the fold like that, because it would contain time-related functions that we would use across the board, and it was used by Hendrik when we introduced, the… the context. Context and some OTLP… modification. Honestly, I don't remember the whole thing, but you see, for example, now we have timeout after, time out after, all of that.
I don't think… That we use them… As much as we need.
The only one that we use is this one, called Timeout and the payload all.
Which, by the way, is not public. Trail of Love is just…
**Antoine Gagniere** 15:44 You still… we still use them?
**Francesco Gualazzi (OpenTelemetry)** 15:47 Yeah, yeah, cold timeout, is cold.
Is it called in, oh, great.
**Antoine Gagniere** 15:54 Maybe it's in…
**Francesco Gualazzi (OpenTelemetry)** 15:55 All is not your pain.
**Antoine Gagniere** 15:56 with.
So, and I just tried compiling with target windows, and it worked, so… I see.
So, apparently we are…
**Francesco Gualazzi (OpenTelemetry)** 16:05 Mmm… well, wait, no.
you are compiling on a Mac machine… Right. …with the output… with the output of, of an executable for Windows.
**Antoine Gagniere** 16:20 Right, yes.
**Francesco Gualazzi (OpenTelemetry)** 16:20 What's failing here, for the reporter of the issue, is compiling on a Windows machine.
Which does not have… all the POSIX APIs.
Dev… were used.
**Antoine Gagniere** 16:35 Isn't Zig supposed to be ematic? Like, it ships all the system headers…
**Francesco Gualazzi (OpenTelemetry)** 16:42 Hermetic, yes, but it's not probably what you mean. Platform independent, you mean?
**Antoine Gagniere** 16:49 Shoot?
Yeah.
**Francesco Gualazzi (OpenTelemetry)** 16:52 from Windows.
**Antoine Gagniere** 16:55 For Windows, they ship, you know, Ming W64.
So they ship the headers of Mingwen Sixture.
**Francesco Gualazzi (OpenTelemetry)** 17:05 Yes, okay, but we mean, W, Win, whatever it is, still… a Linux.
Environment.
**Antoine Gagniere** 17:15 Right, but… I mean, it's a libc for Windows, right? It's…
**Francesco Gualazzi (OpenTelemetry)** 17:21 Oh, yes, sort of. But again, the man, probably, the reporter here is trying to do a Zig build with the Zig.x binary of Zig on a Windows machine, which is completely lacking certain APIs which were used here.
**Antoine Gagniere** 17:39 Now they're gone.
**Francesco Gualazzi (OpenTelemetry)** 17:41 Okay, now these APIs are gone, apparently.
Because we are only relying on STD, and STD is cross-platform across the board.
**Antoine Gagniere** 17:51 Yes.
**Francesco Gualazzi (OpenTelemetry)** 17:52 I mean, unless…
**Antoine Gagniere** 17:53 So…
**Francesco Gualazzi (OpenTelemetry)** 17:54 special integrations, but yeah, we do… we do still use clock timeout, but the other ones, I'm not sure. So yeah, both are assigned to me. The Windows one, which is easily solvable by adding, CI runner in the matrix, and this one, understanding if we still use, for example, wait timeout. I'm not sure we do use that.
Oh yeah, index portal.
Okay.
Oh, wait, wait, wait.
No, this is not the same. State done, wait timeout is… Yeah, it's another thing. Self-wake with… I think, I mean, probably this one can go away, but again, I will work on it, this week.
And I will make sure that both are sorted out.
And then we can go back to, you know, doing Actual… Features and bug.
Features incurrence and bug, and bug resolutions for the milestone, which, yeah, here we go.
So… These two, these two consider them done, okay?
And then again, this one is the biggest one.
Which will generate a ton of subissues.
**Antoine Gagniere** 19:12 Right.
**Francesco Gualazzi (OpenTelemetry)** 19:13 This one, we have to decide if we want to keep it in.
This one, I would happily assign it on you. Oh, it's already on you, so… okay.
I also, this one, I think this one is doable, in the sense that, you know, it's a couple of PRs, and we can heavily use LLMs for those.
Focusmentation, that's great.
And a couple of bucks, so… Pretty optimistic about it, honestly.
**Antoine Gagniere** 19:41 Okay, okay, yep, yeah, yeah, I think compression is… is small, and Windows support for gRPC, so you think it's blocking the release as well?
Because gRPC is optional, right? So… But I can, I can look at it, yeah, I can take a look.
It must, yeah, because the lib should support, so yeah, I'm guessing it's not a lot of work.
So, yeah, I can…
**Francesco Gualazzi (OpenTelemetry)** 20:22 One second? Oh, no.
**Antoine Gagniere** 20:27 Do you want to ping Giovanni?
**Francesco Gualazzi (OpenTelemetry)** 20:34 No, he's also… B.
His daughter was born 4 months ago.
**Antoine Gagniere** 20:43 Oh, yeah, yeah, yeah, okay, he's…
**Francesco Gualazzi (OpenTelemetry)** 20:45 He's primarily very busy right now.
**Antoine Gagniere** 20:47 Right, right.
**Francesco Gualazzi (OpenTelemetry)** 20:48 But again, we can still summarize the outcomes.
And you already did most of the job of IE.
populating that table. So, we can just say we briefly discussed the Alpha release milestone, and we do want the… performance to the 1.62 specification in the release, so for that, we will create some issues, and they will be added to.
**Antoine Gagniere** 21:17 Ego.
Yeah, yeah, if you want, I can run a sub-agent on each row, on each stable row.
Yes.
**Francesco Gualazzi (OpenTelemetry)** 21:25 If you can do… if you can spare some tokens to create the submissions, okay.
**Antoine Gagniere** 21:30 Yep.
**Francesco Gualazzi (OpenTelemetry)** 21:31 But, yeah, try to be… to be… also in the… so what I would like to see in the subissues is you know.
The problem is this one, this is the component that is affected, propose that the solution is, you know, something like that.
Or…
**Antoine Gagniere** 21:50 mission of.
**Francesco Gualazzi (OpenTelemetry)** 21:52 Yeah.
**Antoine Gagniere** 21:53 The blessed release, yeah.
Yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 21:57 What else? Yeah, I don't have anything else.
really hyped.
**Antoine Gagniere** 22:05 Yep.
**Francesco Gualazzi (OpenTelemetry)** 22:06 You know what? This week, I have deployed In production, at my company.
the first DIG service with the OpenTelemetry stick.
**Antoine Gagniere** 22:18 Whoa.
**Francesco Gualazzi (OpenTelemetry)** 22:19 that is ingesting metrics and traces into an OpenTelemetry-compatible backend via gRPC.
**Antoine Gagniere** 22:29 Oh, oh, nice, so you did build with gRPC?
**Francesco Gualazzi (OpenTelemetry)** 22:33 Oh, yes, of course, I'm Doc… oh, why, I have to tell you, I have to tell you. It takes 40 minutes to build.
In UWCI, 40 to 45.
It's crazy. You know, even when caching the dependencies, you know, it's bonk.
**Antoine Gagniere** 22:50 Yeah, did you see, I have improved the caching?
**Francesco Gualazzi (OpenTelemetry)** 22:55 Yeah, yeah, no, I did say that.
You're allowed.
**Antoine Gagniere** 22:58 CPU, Bayesian CPU, the new version of Zig, and…
**Francesco Gualazzi (OpenTelemetry)** 23:04 Yeah, but…
**Antoine Gagniere** 23:05 And also, you need to raise the cash limit of… set to Zig? Because it… yeah.
It will not… it will flush its cache every time, because the lib job is too big, so it will flush the cache.
Well, you mean…
**Francesco Gualazzi (OpenTelemetry)** 23:23 We set up a ZIG action.
**Antoine Gagniere** 23:25 Yes.
**Francesco Gualazzi (OpenTelemetry)** 23:26 How did you do that? Wait, this is… this is relevant. What… what's that… what's…
**Antoine Gagniere** 23:30 Yeah, yeah, I can send you the exact… Yeah, please.
**Francesco Gualazzi (OpenTelemetry)** 23:34 I'll share it with the whole group in Slack, because I think this is relevant.
Because again, gRPC, unfortunately, is the default, so, yeah, we need that, we need a bit more.
**Antoine Gagniere** 23:47 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 23:47 With a veto.
**Antoine Gagniere** 23:50 So, here in… Fisher.
So… Yep.
Here, you can see, I set up Zig, I have to raise the cash limit.
Because else… It will flush every time, so you will never restore cache, because it…
**Francesco Gualazzi (OpenTelemetry)** 24:11 Yeah.
**Antoine Gagniere** 24:12 The, the…
**Francesco Gualazzi (OpenTelemetry)** 24:12 Yeah, so…
**Antoine Gagniere** 24:13 It's bigger than the limit, yeah.
**Francesco Gualazzi (OpenTelemetry)** 24:15 What's that? Megabytes?
14.
**Antoine Gagniere** 24:19 Easy enough.
Yep, it's megabytes, right.
**Francesco Gualazzi (OpenTelemetry)** 24:24 Right.
**Antoine Gagniere** 24:25 Yeah, thanks.
**Francesco Gualazzi (OpenTelemetry)** 24:25 I will do that. Thank you.
**Antoine Gagniere** 24:27 Yep, and the baseline is required because each runner may have a different CPU, so in practice, they will not reuse the cache.
So…
**Francesco Gualazzi (OpenTelemetry)** 24:37 A haha!
**Antoine Gagniere** 24:38 you need to force them to all use the same CPU, basically.
**Francesco Gualazzi (OpenTelemetry)** 24:43 So, yeah, we'll take inspiration from the all your codebase, build.
Gitaville. Okay, good, good, thank you.
**Antoine Gagniere** 24:51 And, I used dynamic so that, all the examples and tests, they reused the… the same .SO, and it, has… it links faster, because, yeah, I don't know if you see, but the… When you build statically, then it takes, like.
Several seconds, like, at least 5 seconds to link.
Each time, if you modify, like, one character in your end program, and then it needs 5 seconds.
just to relink the huge .A, but if you use .SO, it's much faster.
So I recommend… I mean… so for local development, at least.
**Francesco Gualazzi (OpenTelemetry)** 25:33 Should we… should… let me ask you this, then. Should we make those decisions?
**Antoine Gagniere** 25:39 Sorry?
**Francesco Gualazzi (OpenTelemetry)** 25:40 Should we make those options the default?
So, instead of opting in…
**Antoine Gagniere** 25:47 It used to be dynamic the default, but, no, it's… There's complications that come with dynamics, so that, for, like, yeah, each layer, each package importing something that depends on gRPC, that needs to be imported by, like, consumed by another package on top, you need to add a line to install the .SO to, like, to pass the .SO through the layers. It's… so… It comes with a bit of complexity cost, so… But…
**Francesco Gualazzi (OpenTelemetry)** 26:28 Huh.
**Antoine Gagniere** 26:29 Yeah, I don't know if you've tried Dynamic, but also for your prod… I would recommend using the system.so, no?
Did you try that?
**Francesco Gualazzi (OpenTelemetry)** 26:43 production service, in the end, ends up in a distro-less image. That's why I built it statically.
**Antoine Gagniere** 26:49 Okay, oh, Distrolets, okay, you don't, okay, okay.
**Francesco Gualazzi (OpenTelemetry)** 26:53 But the CPU baseline for CI should be… it's probably the best optimal. I thought it was already the default when we turned it on when I reviewed the PR, but that probably is not the case, but I will double check.
**Antoine Gagniere** 27:09 Oh, yeah.
**Francesco Gualazzi (OpenTelemetry)** 27:10 I will show you the cache size. The crash size should be…
**Antoine Gagniere** 27:13 Right, but I don't think it's a good idea to set CPU baseline as a default.
**Francesco Gualazzi (OpenTelemetry)** 27:19 No, no, I mean NCI.
**Antoine Gagniere** 27:21 Yeah, in CI, yes.
Oh, okay, oh, sorry, you mean default in CIO. Not sure how to… like, to do it?
To define, like…
**Francesco Gualazzi (OpenTelemetry)** 27:32 No, no, no.
**Antoine Gagniere** 27:33 I was…
**Francesco Gualazzi (OpenTelemetry)** 27:34 I was… I was saying… In my project, I should use those.
**Antoine Gagniere** 27:41 Right.
**Francesco Gualazzi (OpenTelemetry)** 27:41 In the linking, If it's so slow to link statically.
should we make the link, the dynamic linking the default instead of statically? But I remember now, you reminded me, we already had this conversation, I said, no, we should link statically by default, because we also bundle the library, and it should be… Static editing… For distribution?
**Antoine Gagniere** 28:11 Right, yes. Never mind.
**Francesco Gualazzi (OpenTelemetry)** 28:13 Suck.
Right.
Forget one.
**Antoine Gagniere** 28:17 No problem.
Okay, well, good to hear, so someone is using this, yeah. Of course!
Agreed.
**Francesco Gualazzi (OpenTelemetry)** 28:25 I've had great success so far, so… and I'm, you know, dog-fooding. I've also… I've also stumbled on the bug that was fixed by a recent PR by Yash.
mem… no, I want to say… don't want to say memory leak, but memory growth, unbounded memory growth by the fact that all data points are preserved, so… Yes. That was by design, if I have to tell you honestly, but, I… I prefer to get rid of it with… with the ash spear, because, yeah, we cannot… we cannot assume that No, memorisi.
Alright, I see it's bedtime.
**Antoine Gagniere** 29:09 Okay.
**Francesco Gualazzi (OpenTelemetry)** 29:12 Okay, I don't want to steal too much of your time from you and your kids, so… I don't have anything else to discuss. I will leave a note to Giovanni in the Slack till we discuss the… conformance, and if you are willing to spend some tokens on generating the issues, thanks for that. Thank you.
**Antoine Gagniere** 29:32 Yep.
Yep, I can do that.
**Francesco Gualazzi (OpenTelemetry)** 29:34 It is, yeah.
**Antoine Gagniere** 29:36 And so, you… because gRPC doesn't have compression, did you notice it? Like, it… do you notice a difference? Like, with HTTP, it was better, or… Because in your setting.
**Francesco Gualazzi (OpenTelemetry)** 29:48 I don't notice a difference.
**Antoine Gagniere** 29:51 Okay.
**Francesco Gualazzi (OpenTelemetry)** 29:52 But I… I mean, we don't have… in that specific service, which is an internal-only service, it's not a service in production that is accessed by customer. It's an internal-only service, but it's still… in production, and ingesting data in the production backend that collects our internal telemetry, I haven't noticed a difference, so…
**Antoine Gagniere** 30:16 No guaker.
**Francesco Gualazzi (OpenTelemetry)** 30:16 Very good.
All the metrics that have to be injected, and all the traces are there, so… That's what the food is.
**Antoine Gagniere** 30:24 Okay, okay, good, good, good.
**Francesco Gualazzi (OpenTelemetry)** 30:26 Memory, probably, the memory usage, I noticed a little, little increase, but… Absolutely… Minimal stuff, so we're talking, like, 100 to 120 megabytes of access.
**Antoine Gagniere** 30:39 Right, right.
yeah, so maybe I should prioritize the compression still to… if you are using it.
**Francesco Gualazzi (OpenTelemetry)** 30:49 If you want, but again… I don't… I don't think it's super priority, but also, it's the only… let's say, big item in the milestone that requires your attention specifically, because most… because you are the one that is the matter expert in the gRPC… OTP gRPC protocol.
Awesome.
Do you wanna do that first, rather than the… Alignment of providers, that's… Excellent.
**Antoine Gagniere** 31:20 Yep, okay.
**Francesco Gualazzi (OpenTelemetry)** 31:22 I will mostly take care of the windows and clock, and a couple of bugs on top.
**Antoine Gagniere** 31:27 Good, yeah.
**Francesco Gualazzi (OpenTelemetry)** 31:28 And the reviews that, contributors out of Sandy.
**Antoine Gagniere** 31:33 Okay, okay.
**Francesco Gualazzi (OpenTelemetry)** 31:35 So, you're also not going to Kubkon.
**Antoine Gagniere** 31:38 No. Maybe I could, but yeah.
**Francesco Gualazzi (OpenTelemetry)** 31:44 Barcelona next year?
**Antoine Gagniere** 31:46 it's… It's where?
**Francesco Gualazzi (OpenTelemetry)** 31:49 I think it's Barcelona 2020.
**Antoine Gagniere** 31:51 Oh, okay.
Yeah, but is there anything interesting? Like, any talk to, like…
**Francesco Gualazzi (OpenTelemetry)** 31:59 Just meeting the other OpenTelemetry maintainers.
**Antoine Gagniere** 32:03 Right, right, yes.
Yeah, maybe. Like, I know that my company, like.
I can ask for one conference per year, and they will…
**Francesco Gualazzi (OpenTelemetry)** 32:12 Oh, okay.
Yeah, it's gonna be in Barcelona.
15 to 18 March.
**Antoine Gagniere** 32:19 Okay.
**Francesco Gualazzi (OpenTelemetry)** 32:21 I think they already did it in Barcelona, maybe last year or the year before, I don't remember.
Anyways, okay.
**Antoine Gagniere** 32:29 Okay.
Yep, okay.
**Francesco Gualazzi (OpenTelemetry)** 32:31 Good.
Upworks and onworks, is that how they say it?
I only know the Latin word.
**Antoine Gagniere** 32:42 Yeah, maybe in Latin… what do you say it in Latin?
**Francesco Gualazzi (OpenTelemetry)** 32:45 Raspera d'astra.
**Antoine Gagniere** 32:47 yeah, right, very good.
**Francesco Gualazzi (OpenTelemetry)** 32:51 Hey.
**Antoine Gagniere** 32:51 is rusty, is rusty, I forgot that.
**Francesco Gualazzi (OpenTelemetry)** 32:56 I speak the… I speak it every day, so… Enjoy your day, Antoine. Thanks for everything, and see you next time.
**Antoine Gagniere** 33:04 Thank you, see you.
