SIG: Zig SIG
Date: 2026-07-22
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Antoine Gagniere** 03:42 Hello?
**Francesco** 03:46 Hey, Antoine. Good afternoon. Do you hear me okay? Yeah. Yep.
Alright.
So, it's probably just you and me.
I… haven't have… haven't had any feedback from other peers in the SIG or external.
to… with regards to the… to the PR that is now open, you know?
It's a bit of a sad thing that nobody's chiming in, and apparently it's only you and me. Well, I know Gomani just had, birth, so, so Giovanni just came… became father, like, 10 days ago, so I'm expecting he's, distracted with something else.
Yeah, exactly. But I don't remember last time you said you also have kids, or I misunderstood.
**Antoine Gagniere** 04:40 Yes, it's, one, one kid.
**Francesco** 04:44 Oh, okay, congratulations and good luck.
So, yeah, I saw you approved it, thanks a lot for that. I guess, because this is blocking others, others' work, so I, you know, especially the proto and, and everything else, so also the same convo.
I guess if nobody makes a comment on the PR, or writes something in the Slack channel, I will happily merge it, yeah, tomorrow.
Tomorrow morning.
**Antoine Gagniere** 05:18 Nice.
**Francesco** 05:18 Giovanni also approved, by the way, 3 hours ago, okay?
**Antoine Gagniere** 05:22 Sure.
**Francesco** 05:22 So, maybe I could just, you know, squash it immediately, and we take it from there.
What do you say? What do you suggest?
**Antoine Gagniere** 05:33 Yeah, yeah, agreed, yeah, I see you've moved, since I approved you, you moved more code in the build folder, so that's good, so…
**Francesco** 05:45 Yeah, I didn't push more commits, but Yeah, I just, you know, you approved it in the la- it's already the final version, maybe you didn't pull the.
**Antoine Gagniere** 05:55 Yeah, yeah, right, right, correct.
**Francesco** 05:56 It's okay. No, but I think… I think it's a reasonable compromise, you know, that… that… fixes what we are able to do with Zig at the moment, unfortunately.
Right. Okay. You know what? Let's match it. Whatever.
**Antoine Gagniere** 06:17 Yeah.
**Francesco** 06:18 Okay.
Let's see, maybe I should… Picks a bit the… They merge… Omit messenger… Commit message, yes?
And then I will merge it.
Let's do this.
Good place. What is cool is that, is that even, Inventor documentation is still online, which is nice.
actually, I want to see it published, you know? You know, we have, Zig Doc, Autodoc, that's how it's called, Autodoc website already.
**Antoine Gagniere** 07:08 But it's not, Okay, maybe I looked at the wrong place, but the, you know, usually there's a link at the top right?
And here, it just links to the Open Telemetry website.
**Francesco** 07:24 Let me check.
**Antoine Gagniere** 07:26 You are right, the pages are there.
**Francesco** 07:28 Yeah, in the pages, yes. In the pages.
**Antoine Gagniere** 07:31 Yeah, so just… I'm guessing we just have to set the… the link…
**Francesco** 07:37 Zig Docs is completely wrong. Yeah, yeah, yeah, yeah, I see what you mean.
**Antoine Gagniere** 07:41 Yeah, just, yeah, so I just realized the pages are there, just the link was not the one expected, yeah.
**Francesco** 07:48 Yeah, yeah, yeah, yeah, yeah. Also, the image is gone, also, now that I merged.
Yeah, let me fix that.
The image is gone, for some reason.
**Antoine Gagniere** 08:00 Because now… Oh, okay, good.
**Francesco** 08:01 Yeah, yeah.
Images? Let me… also, let me check.
The deployment is this one.
the URL… The URL that I want to put in the Zig docs is… Well, there should be one now.
**Antoine Gagniere** 08:21 Oh, because you… It's interesting, you set it relatively to the repo, probably the image.
**Francesco** 08:27 Okay.
**Antoine Gagniere** 08:28 Ducks.
slash images…
**Francesco** 08:31 Yeah.
**Antoine Gagniere** 08:32 No, it's just images.
**Francesco** 08:34 Yeah, yeah, yeah, that's what's wrong.
I didn't update the…
**Antoine Gagniere** 08:39 Oh, right. Yeah, yeah, yeah, okay, good.
**Francesco** 08:41 It didn't update correctly, they read me, sorry for that.
Let me check… so this one is the URL… Open, Telemetry to get a bio, yes. Copy link? Well, maybe that… maybe it's not wrong.
Oh, it's correct, you know, if I… if I go to… Let me share my screen real quick.
**Antoine Gagniere** 09:03 Yeah.
**Francesco** 09:04 Oh, actually… This one?
**Francesco** 11:25 Hello?
I… I'm back.
I did an attempt of sharing my screen with very few megabytes of memory free.
You know, my computer is 6 years old at this point, I need to upgrade at some point.
But yeah, that's… that was the problem, so I completely froze the Chrome, and I had to reboot… not reboot. I went, you know, I went into the other console, and the other TTY killed Chrome, and stuff.
No, well, I wasn't…
**Antoine Gagniere** 12:04 If you want.
**Francesco** 12:06 Oh, yeah, what I was saying is that the… the README… the image is broken, but if you click to Zig Docs.
**Antoine Gagniere** 12:14 Right, right, yeah.
**Francesco** 12:15 Come on.
**Antoine Gagniere** 12:15 Literally.
**Francesco** 12:16 That one is actually working, so that's correct.
**Antoine Gagniere** 12:19 Correct, yeah, I was thinking about this link here.
**Francesco** 12:23 Okay, let me check.
**Antoine Gagniere** 12:24 Because usually, people put the link… I'm pretty sure, by the way, that the previous report, it was correct. Let me check.
**Francesco** 12:35 Yeah, the previous one, yes, but…
**Antoine Gagniere** 12:36 He was going, yeah, yeah, here, exactly.
I see.
**Francesco** 12:39 What do you mean? Well, we can update it. We can update it, of course.
**Antoine Gagniere** 12:43 Dude.
**Francesco** 12:43 I think so.
**Antoine Gagniere** 12:44 So…
**Francesco** 12:44 Let me check.
Okay, I know, I see what you mean now. Let me see, so… in the settings, about… and I cannot change it, I don't know why.
Because I'm not a maintainer.
I cannot change it.
Probably… probably… Jacob can.
It's a weird thing for… with the permissions, I don't know what's happening, but I cannot change that, unfortunately.
**Antoine Gagniere** 13:13 Okay, okay, no problem.
**Francesco** 13:15 It's fine, okay, whatever. But the Zig Docs link is working.
But the image is not working, so let me fix that.
Yeah.
**Antoine Gagniere** 13:25 Yeah.
**Francesco** 13:26 Stuff like that.
So… that the image will be… yeah, image is zero.
Now, make a new PR… Okay, please approve the PR, Great question, just a second.
45.
**Antoine Gagniere** 14:07 Yeah, 40 players.
**Francesco** 14:09 Yep.
**Antoine Gagniere** 14:11 Mmm… Yeah, right.
And by the way, about the README, I, noticed the other Open Telemetry repos, they have a list of the who is the maintainer, who is the approver, who is triage.
**Francesco** 14:32 Yes, we should change that, yeah. Oh, no, I'm an idiot, I should have merged this other one first, 44.
Bang!
This guy is, is another contributor.
**Antoine Gagniere** 14:48 Right, right, right.
**Francesco** 14:50 Oh, I'm so dumb.
I didn't see that, because I have, I have, I have a cache.
Oh, man!
Okay, well, I'll…
**Antoine Gagniere** 15:01 It's moving the same files.
So there's no conflict, right?
**Francesco** 15:08 No, the problem is that now the files are moved, so his PR… My base automatically?
**Antoine Gagniere** 15:16 IU, of course.
**Francesco** 15:17 he's… Okay, I will need to do some heavy lifting. Oh, yo, yo.
I didn't,
**Antoine Gagniere** 15:25 Yeah, I forgot about this one,
**Francesco** 15:28 Oh, man, can we edit it as maintainer?
**Antoine Gagniere** 15:32 He gets the money would… Where is it written? But normally, Yes, it's written on the right, bottom right, maintainers are allowed to edit this pull request, so you can push on this branch directly.
**Francesco** 15:49 Okay.
**Antoine Gagniere** 15:50 So, I'm sure with a GitMB, or… Hmm…
**Francesco** 16:00 Yeah, JH, check out, and whatever.
**Antoine Gagniere** 16:04 Yeah, yeah.
**Francesco** 16:10 Oh, yeah, yeah.
Nice that we have a new contributor. We have to cherish these things.
**Antoine Gagniere** 16:20 Yeah.
**Francesco** 16:22 We have to charge also, because I… it's something that I wanted to do, if there's an issue, actually, for that. Yeah, fixes 30, nice.
Beautiful.
Oh, man… Mother… Mother of God!
How do I do that? Okay, let me see.
I know I can do that.
Yeah, the repeat peak will not work.
Yeah, we'll find a way to fix it.
Jeez.
Okay.
Anyways, yeah, well, I don't have anything more, actually.
Do you have, something to discuss other than this?
**Antoine Gagniere** 17:13 N-no… Nope.
**Francesco** 17:17 Now that the repo structure is different, are you resuming your gRPC work?
**Antoine Gagniere** 17:22 Yeah, I was quite busy, but yeah, I should…
**Francesco** 17:26 No, you don't have to, I just… I was just asking, because that's… that's the next big thing, I think, to support ZCC. We are not in a rush, of course. Nobody that I know is actually using this project.
**Antoine Gagniere** 17:41 Right now.
**Francesco** 17:42 So, aside, you know, for me, I'm using it, and I'm completely fine with the HTTP Proto, but… but yeah.
gRPC is the next, let's say, big item that we want to support, so again, no rush, you're busy, and I guess… You've been working also on the… no, you said last time, no, you didn't work on the compile-time instrumentation.
**Antoine Gagniere** 18:07 No, no, no.
**Francesco** 18:10 He's okay.
**Antoine Gagniere** 18:11 Oh yeah, I could mention, I saw a message in the upper Telemetry Slack, asking about C… C… Open Telemetry SDK, right? But for the specific use case, we're embedded, so they need… they have a custom compiler, they cannot use… or the compilers, and so I did mention the Zig Open Telemetry by saying that they can transpile Zig to C, And… and compile with their compiler.
But, yeah, I'm… they are not… they did not reply, so maybe not interested, but, yeah, I did…
**Francesco** 18:54 Double thumbs up, I… I… that… you know, having the CAPI is one of the reasons why… why we… why we… why we added it, so thanks for making it, Evident that there is something like that.
**Antoine Gagniere** 19:11 Yep. And I did verify, so… that he… did not fail to transpire to see with the SDK, so I did it, but…
**Francesco** 19:21 Yep.
**Antoine Gagniere** 19:22 I didn't try, so I don't know if you or someone you know already did that.
like, actually used, actually made a binary that depends on the API transfer.
**Francesco** 19:32 I did a toy one, yes, I did a toy one, and basically building the, let's say, a slightly improved variation of our current examples.
But nothing… nothing com… nothing more complex than that, you know, with that.
you know, with adding more dependencies, or system libraries, or link… weird linking stuff, no. But, I have to say, it does… it does produce valid binaries, both with dynamic linking and GCC, and muscle static linking, so… That, that was nice.
**Antoine Gagniere** 20:12 Nice, yeah. Oh, cuckoo.
But, yeah, that's it.
**Francesco** 20:18 Okay, beautiful.
I will add, one… one entry here in the agenda.
And, mentioning that the new contributor is in, Today is 22nd, okay.
So, yeah. Well, we didn't do the meeting on the 15th, so I can just pick this and… Where this, yeah.
Okay, so… Antoine, and we discussed… Nope.
Contributor… Oh, stand up here.
In exporters… Beautiful.
matched… The… multi-module, okay, structure.
And then, yeah, mentions… And… I'll see.
Compatibility?
Or… In… What's it up.
You know, but sometimes I think.
I think some people have been using the C++ SDK for that, and compiling within C projects. I don't remember exactly. I've heard someone doing that, because the C++ is officially supported SDK. But definitely, I would love to see what happens if you have a C project when you… use the… C bindings that we provide with the static library from, from, yeah.
from Open Telemetry Zig, or using the native C++ SDK. I would love to see the difference.
**Antoine Gagniere** 22:15 There.
**Francesco** 22:17 Oh… what else? No, I think that's it.
Oh yeah, no, No, no, nothing, that's it. So… No commitment, I don't… I'm not asking for that, but you are the one that is… that will be trying to port over what's been previously done for gRPC in the repo.
Also, because you are the author of the, let's say, the library that makes the bridge, no, between,
**Antoine Gagniere** 22:50 Yeah.
**Francesco** 22:51 Between the transport that we have to OTLP and the actual GFPC library, so the wrapper that you made is something That you created in your own repo.
**Antoine Gagniere** 23:04 Yeah, yeah. Okay. And, yeah, I had a small question is, did you… is it possible to have a repo where there's a remote that is an old Open Telemetry Z repo, and also another remote that is a new Open Telemetry SDK repo?
Like, to be able to move commits around, can you…
**Francesco** 23:26 So what I… yes, I did that. I did that for, porting over one rep from repo to another.
And I guess the problem with that… no, you should be fine, because the linear history should be preserved. So, you can add both remotes, I think.
And then try to cherry-pick.
**Antoine Gagniere** 23:50 Yeah, exactly, yeah. Okay, yeah.
**Francesco** 23:53 You should try that.
If it's going to speed up for you, the work, of course, yeah.
**Antoine Gagniere** 24:01 Okay, goodness.
**Francesco** 24:06 Beautiful.
**Antoine Gagniere** 24:08 Yep.
**Francesco** 24:09 That's all on my end. I will go and fix Alan's PR. What an idiot. So, going into new standard.io, that's beautiful, actually. Yeah, it's something that I wanted to do. And then cry on my shoulder for a bit, and then, I think we see in two weeks, because next week you're not available, right?
**Antoine Gagniere** 24:31 Yeah, but so next week, I will be even in vacation, so I will not be…
**Francesco** 24:36 See you in 4 weeks, then.
**Antoine Gagniere** 24:39 Yeah, man.
**Francesco** 24:40 Maybe 3?
Well, he went along.
**Antoine Gagniere** 24:43 Yeah, I think, yeah, in 4 weeks, yeah.
**Francesco** 24:47 You're going, you staying in France, or are you going, abroad for,
**Antoine Gagniere** 24:51 Yeah, I'm going one week in the U.S. for… to see a family… yeah, some family.
And, than to… south of France, so near the border with Italy, yeah.
**Francesco** 25:06 Okay, okay. Mentimiglia. Menton.
**Antoine Gagniere** 25:09 Yeah, yeah, close from there, yeah.
**Francesco** 25:14 in Jean Le Pen?
**Antoine Gagniere** 25:16 Oh, yeah, yeah, I used to live in Jonipat, yeah.
**Francesco** 25:18 Oh, really? No.
**Antoine Gagniere** 25:19 Yeah.
**Francesco** 25:20 Oh, incredible!
**Antoine Gagniere** 25:22 Yeah.
**Francesco** 25:23 Incredible. Maybe we met when you were a kid.
**Antoine Gagniere** 25:27 No, no, no, not as a kid, but a few years when working, yeah.
**Francesco** 25:32 Oh, okay.
**Antoine Gagniere** 25:34 Yep.
**Francesco** 25:35 Or I should say, niece.
**Antoine Gagniere** 25:38 Yeah, niece, but I don't like Nice as much.
**Francesco** 25:42 So, yeah, Joan Le Pain is quieter, Nice is a bit more chaotic, but it's still, you know, beautiful city, you know?
**Antoine Gagniere** 25:50 Yeah, yeah, yeah, the old center is beautiful, yeah, but just too… too many people, too many…
**Francesco** 25:56 Cool.
**Antoine Gagniere** 25:57 Too crowd, too much crowd, etc, so…
**Francesco** 25:59 I got it. Okay.
Yeah, enjoy your holidays, then. See you next month!
**Antoine Gagniere** 26:04 See you!
**Francesco** 26:05 By Antoine. Au revoir!
**Antoine Gagniere** 26:07 Cho.
