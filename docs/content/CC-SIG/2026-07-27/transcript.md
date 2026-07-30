SIG: C/C++ SIG
Date: 2026-07-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Doug Barker** 00:00 Meeting is being recorded.
Hey, Tom.
**Tom Tan** 02:22 Hi, Doc, good afternoon.
**Doug Barker** 02:24 Good afternoon.
So I saw, Mark sent a note that he's not going to be able to join.
**Tom Tan** 02:37 Okay, I see.
**Doug Barker** 02:43 Do you know if, Lillette is around? Will he join?
**Tom Tan** 02:49 I'm not sure who will join, I think usually he was key for this meeting, because he has some other… Meetings too.
**Doug Barker** 02:57 Okay.
**Tom Tan** 03:08 I'm just opening the meeting agenda.
**Doug Barker** 03:32 Alright.
Can you see my screen?
**Tom Tan** 03:47 Okay, I can see your screen, yeah.
**Doug Barker** 03:49 Okay.
So I think the good news is we've got a lot of PRs.
I think we'll… we'll have to… a few of these have been going on for a while that I'd like to close out. So one is the probability sampler, this one.
It looks like you made some comments. I'll try to make some comments on this one, but I think it's in pretty good shape now.
**Tom Tan** 04:22 Yeah, okay. I think my comments was, addressed, so…
**Doug Barker** 04:27 Okay.
Alright, so I'll try to take a look at that one… at this one this week. Would you be able to do the same?
**Tom Tan** 04:35 Yeah, sure.
**Doug Barker** 04:36 Okay.
**Tom Tan** 04:38 Thanks.
**Doug Barker** 04:39 Yep.
And then… I think there is… Yeah, I don't know if any of these… this one is pretty old, drop stale attributes.
on a retry, I think this one, Owent, has been commenting, so maybe I'll ping Owent on this one to see if he has any more.
Sure. Okay.
**Tom Tan** 05:13 There's some conflicts need to be resolved. I think we can sort the PR by updated date, then maybe we will see.
**Doug Barker** 05:22 Good idea.
Recently updated.
Okay.
Yeah, so I think maybe if we try to get the probability sampler this week… I don't know about that, a 2P parser, or a success, but that would be a good one.
I would like to get some feedback on this one, if you have some time. This one hits the tracing start span implementation. It fixes a few correctness things, but also improves the performance, especially in the sampled case.
**Tom Tan** 06:07 I see.
**Doug Barker** 06:08 So…
**Tom Tan** 06:09 Could you please highlight this, like, by other label?
Please review, like that, yeah.
That would be helpful.
**Doug Barker** 06:29 I think the one that I wanted to discuss, because it does seem important, is the… SpinLock case. Have you looked at that?
**Tom Tan** 06:38 Yeah, yeah, I looked at it, yeah.
Should be updated this, this, yesterday or today, this morning.
That's Yeah, that's a PR.
**Doug Barker** 07:07 So I started to look into this, and one of the things that I'm finding is that we may be using SpinLock in cases where SpinLock isn't really a great fit, so especially, like, in the.
**Tom Tan** 07:18 Yeah.
**Doug Barker** 07:19 you know, where there's… it's, like, locking over a user callback, or it's locking over I.O.
Yeah, I think we should switch to Mutex, and there's cases, too, in the metrics pipeline where I think we should switch.
**Tom Tan** 07:30 Yeah, yeah, I think we should maybe fix the SDK at the first, instead of fix it here.
**Doug Barker** 07:36 Yeah, I agree. So what I was thinking is I can log an issue, at least what I'm, you know, with all the call sites, and then maybe we can discuss and decide where, we should switch to Mutex and where we should keep the spin lock.
**Tom Tan** 07:49 Yes, yeah, I think that would be good.
**Doug Barker** 07:52 Okay.
**Tom Tan** 07:54 The current change is too risky in the current year.
**Doug Barker** 07:58 Yeah, and I didn't know there was a 1 millisecond sleep, that one scares me a little bit, but hopefully we switch to Mutex and that never gets hit.
**Tom Tan** 08:07 Yeah, hope so.
**Doug Barker** 08:09 Alright.
The other one, since you called it out in the issue, I think this one is one to get feedback on, too, so… how you feel about the switch to add the prefix to the CMake options?
**Tom Tan** 08:29 Yeah, I think, okay, let me take a more look on this one. I think the uncommented one, and the… The Moodle oncoming, yeah.
**Doug Barker** 08:42 Yeah, so in my mind, the biggest question here is the impact will be all of those cases that you pointed out, where everybody has the old options in their CI files.
All of a sudden, when they start to take this update, they will get a lot of deprecation messages in their.
**Tom Tan** 09:02 doing well.
**Doug Barker** 09:02 And the question is, is if that's going to be a blocking problem, or if that's acceptable.
**Tom Tan** 09:09 Yeah, we'll be annoyed if… Get all of these issues in a certain, and they need to fix all of the… all of them.
**Doug Barker** 09:16 Yeah. What do you think for the VC package? So, like, if you… if you imagine, like, when you go to update the VC package, would this be a problem, or would you just fix all of the… see make options in that… in that package when you do the update.
**Tom Tan** 09:32 Well, basic package is fine, I think I can fix all of them, all of the options in one PR, but, Should be… But for the user of VC package, I'm not sure how much change do they need, or… yeah, I need to take a look. Yeah, from the package upgrade side, I think it should be good.
**Doug Barker** 09:57 Okay.
Yeah, I don't think… other than the deprecation messages, I don't have a major concern with this, because it will automatically take the old option and then convert it to the new option. The new option will be cached.
**Tom Tan** 10:11 And there's even, I think, one more risk is, besides the official VC package port, I think, I saw some teams, like.
created their own.
with the package port in the repo, because they need to override some… some options, like, which is not… Provided in the official port. So, which means for all the custom Customized port, they will also be broken, need to be updated.
**Doug Barker** 10:43 Okay. Yeah, I don't know if they would be broken, but they would… they would emit the deprecation warning.
**Tom Tan** 10:48 Yeah, yeah, we'll see.
Yeah, I think in the production system, in the deprecation, usually the warning will be treated as error, right, so you don't need to be…
**Doug Barker** 10:59 Yeah, I think that's…
**Tom Tan** 11:00 Dude, yeah.
**Doug Barker** 11:02 That's definitely the risk, is if it's treated as a… as an error, then they'd have to fix it right away.
Okay.
unless, I guess, at least this is getting in good shape. I think we just need to decide what, what, how to release it.
**Tom Tan** 11:20 Yeah.
That's true.
**Doug Barker** 11:23 Okay.
The other one… Was this CI one?
I think what happened is this is, upgraded to GRPC, and then CI started failing on the Functional tests, because of the… the test… Here, cert not found. So we're intentionally sending it a bad, bad, value. I think we can probably be more protective on our side and address this case, possibly without sending that value to GRPC and exposing this bug.
**Tom Tan** 12:02 Okay, So, is this a regression, or…
**Doug Barker** 12:14 Yeah, it seems like something related to the GRPC upgrade.
to this latest version has exposed this issue that has pre-existed on the gRPC side.
**Tom Tan** 12:27 Okay.
**Doug Barker** 12:28 So, I think we can probably address it. We may be able to address it in our code.
**Tom Tan** 12:35 So you mean this is actually an issue in gRPC, but we may need to work around it?
**Doug Barker** 12:40 Yeah, that's what this, this, contributor, found here and documented.
**Tom Tan** 12:45 I see.
**Doug Barker** 12:57 So, I think that's… Something we can… we can.
**Tom Tan** 13:00 And the fakes is test only, right? Test only?
**Doug Barker** 13:03 Yeah, it's periodically failing in the CI pipeline, so the current workaround is just to restart the job, and it typically passes on the second try.
But…
**Tom Tan** 13:14 Okay.
**Doug Barker** 13:15 But it just, I guess is obviously not ideal for those tests to be periodically failing, so I think we can potentially look at fixing it on our side.
**Tom Tan** 13:25 Yeah, yeah.
**Doug Barker** 13:32 So, I think those are the ones that I wanted to cover. Were there any that you wanted to talk about?
**Tom Tan** 13:40 No, no special issue or PR I want to call out, I think. I have about small fakes when I… I created… when I made the VCPAC report, which should be pulled back. I think we missed some… targeting, say, make, so I will do that.
**Doug Barker** 14:00 Okay.
Perfect.
As far as issues go, so this contributor added a lot of new bug reports.
**Tom Tan** 14:10 Yeah, I saw, you know, a lot of issues like this.
**Doug Barker** 14:15 So… I, am not too familiar with this code. Who do you know is, the most familiar with… this is all the, HTTP… Code.
**Tom Tan** 14:27 Yeah, I haven't looked into details. I think that there was PR attached, right?
For orbit.
**Doug Barker** 14:36 Some of them, yeah, some of them you can see have PRs associated.
**Tom Tan** 14:39 Yeah.
**Doug Barker** 14:40 That's gone.
I think maybe we… we can, just accept it based on the PR. I think Owen closed one of them based on the file, not being needed anymore.
**Tom Tan** 14:50 Yeah.
**Doug Barker** 14:54 Okay.
Other than that, there might be some old ones here.
So, hold on… Oh, ETW.
what should we do about… there's a lot of… so there's a lot of issues, but also a lot of PRs that have been around for a while.
**Tom Tan** 15:13 I think that was true, and I think both Lalita and I made some comments, so maybe waiting for the update from the… Oh, no.
**Doug Barker** 15:22 Phase 2.
**Tom Tan** 15:24 Yeah.
**Doug Barker** 15:32 Okay, yeah. Maybe if you could, just ping the contributor and see if they're interested in continuing?
**Tom Tan** 15:39 Okay, yeah, this contributor, I think, is from Microsoft, so he'll campaign him to move forward.
**Doug Barker** 15:47 Perfect.
All right.
Well, I think that's all I had. Is there anything else?
**Tom Tan** 15:56 No, no from my side.
**Doug Barker** 15:58 Okay.
Alright, we can end it there. Thanks, Paul.
**Tom Tan** 16:03 Yeah, talk to you later. Bye.
