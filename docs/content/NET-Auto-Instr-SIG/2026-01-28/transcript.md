SIG: .NET Auto-Instr SIG
Date: 2026-01-28
Duration: 28 minutes
Zoom Recording URL: https://zoom.us/rec/share/HfYjf4G92T5PSPxSjSoHKBB_prUFkljC45RJdYoZlju4K4j__26R1Pv7qoazZRBe.vtfYPL2vDP-YgqxB
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 00:06 Hello.
**Piotr Kiełkowicz** 00:18 Hello, guys.
**Zach Montoya** 00:23 Hello.
**BhupinderSingh** 01:46 Hello, everyone.
**Alexey Pukhov** 01:51 Aye.
**Yevhenii Solomchenko** 02:14 Yes.
**Piotr Kiełkowicz** 02:46 Do you know… Zach, do you know if Rash or, prius will join us today.
I think we are having a couple minutes of our regular time, so…
I think we can start. Matawsh, can you share the screen and drive?
**Mateusz Łach** 03:32 Yes. Yes, I can do that.
Okay.
Yeah, let's, okay, so let's start as usual with the…
With the open pull requests, so we have something from Martin, release… Release verification documentation…
And this fixes… what issue is that?
Okay, so Robert created an issue that…
That we should document the… how to verify the releases, basically.
Yeah, so… we have a PR, I… I see that Thrasmus already…
Already approved it, not sure what is the… What is the issue?
Probably some flaky test.
Yeah.
Anyway, okay, I see that, you, Pietra, requested a review from Robert. Robert added some,
Some suggestions, so probably once he's, he's able to take another look and approve, we should be good to merge this one, right?
Okay, awesome, so… Then we have, PR from FTCAR, we have, additional details related to…
Profiling support for… .NET Framework…
Yeah, so, FTCAR, anything? Do we have FTCAR on the call?
No.
Okay, so, if you could take a… take a look at this one and,
See if this is, acceptable, I think.
Oh, that'd be very, very helpful.
Okay, so this basically, updates the, sorry, documentation after the recent, changes, which introduced the support for, for profiling on .NET Framework, right?
it has some gotchas, and I think that, This is all,
Clearly documented here, so… yeah, so…
If any other of the approvers or maintainers could take a look, that'd be… that'd be helpful.
Do you hear me, by the way?
That's… okay.
**Alexey Pukhov** 06:48 I didn't hear you.
**Mateusz Łach** 06:50 Okay.
So then we have semantic conventions update for MongoDP.
Pietro, do you happen to know what is the current…
Current state of this one? Are we waiting?
**Piotr Kiełkowicz** 07:07 Wellness.
**Mateusz Łach** 07:08 Seems like… We have some…
**Piotr Kiełkowicz** 07:10 Tons of tests… the tests are not working, or compilation? I do not remember, to be honest.
Okay. I have some doubts how to…
how it should be handled, I mean the semantic conventions, because there is kind of inheritance on the semantic pages.
But with me, let's say Unswert.
On this, and put a lot of good comments here.
**Mateusz Łach** 07:39 Okay.
**Piotr Kiełkowicz** 07:39 So… So…
**Mateusz Łach** 07:41 Okay, so it seems like.
**Piotr Kiełkowicz** 07:43 It'll be pretty obvious how to proceed with this.
**Mateusz Łach** 07:46 Okay, so do you think this is ready to be reviewed, or should we wait for the, for the person working on that to… to fix the issues first? I mean… I think that's okay.
**Piotr Kiełkowicz** 07:57 and ask to verify what's wrong in the CI by the end user.
By the contributor, sir.
**Mateusz Łach** 08:07 Okay, so let me add the… So
Aww.
Would that be okay?
**Piotr Kiełkowicz** 08:28 I think so.
**Mateusz Łach** 08:46 Yeah, and then we have a couple of PRs that are in draft. Any… do we want to discuss any of them? I see that we have people working on them here.
Alexei, anything you'd like to discuss related to your PR?
**Alexey Pukhov** 09:01 Sure, yeah, definitely. So, in short, right now, I'm working on looking at the failures, at the test failures for my PR.
**Mateusz Łach** 09:10 Okay.
**Alexey Pukhov** 09:11 So I finally was able to make sure that the solution works both for Windows and Linux. It compiles on CI pipeline.
But there are some test failures. Some of them are obviously something I just need to adapt to the new things, but there are some suspicious… well, not suspicious, but something that I really want to take a closer look. It's the instrumentation tests.
So just before I move to the startup hook solution, I just want to make sure I didn't break anything that should have worked.
I don't know yet the context of those tests, that's what I'm doing right now.
Basically looking at those tests, figuring out
figuring out if it's related to the profiler change that I did, or Or what… what it is.
But basically, once I figure out if there's anything I need to address right now, in terms of tests.
Then I'll be moving to the startup hook. I have a plan how to do this, so I'll just implement it.
But yeah, you will see the rest.
Tons of tests failing.
**Mateusz Łach** 10:20 Okay.
Okay, so, before you are able to, to investigate the failures with the instrumentation tests, do you feel like, any feedback would be, like.
**Alexey Pukhov** 10:37 Sure.
**Mateusz Łach** 10:38 Are you…
**Alexey Pukhov** 10:39 Please, please, because I think the profiler solution is done.
It's still in a draft because they didn't provide the startup hook solution.
But the Profiler solution is there, so yeah, if you guys have time, please take a look.
**Mateusz Łach** 10:55 Okay, maybe you could, maybe you could add a comment with what you think is, like, ready to be reviewed?
Hello.
Would that be okay?
**Alexey Pukhov** 11:06 Sure. How, what would you expect?
As a comment…
**Mateusz Łach** 11:14 Yeah, I'm just wondering, because you mentioned that you, like, treat one part as more or less, like, completed from your site, right? So, I don't know if,
Like, so that is… it is obvious for reviewers which part you are still, like, working on, and which part you, like, feel is ready to be reviewed.
**Alexey Pukhov** 11:38 Oh yeah, sure, if you can scroll up to the top…
**Mateusz Łach** 11:42 Okay. Let's see if it's kind of…
**Alexey Pukhov** 11:44 If it's obvious that this is under what, and this is the native profiler-based deployment.
So that, the point one, is done.
**Mateusz Łach** 11:54 Okay.
**Alexey Pukhov** 11:55 The added to the NuGet package deployment and the startup hook-only deployment are a…
**Mateusz Łach** 12:00 Okay, I see.
**Alexey Pukhov** 12:00 are not yet done. So, and then there is everything I did for the native profiler-based deployment,
They're, there is an explanation of what I did, and…
**Mateusz Łach** 12:13 Okay.
**Alexey Pukhov** 12:13 really the changes.
**Mateusz Łach** 12:17 Okay.
**Igor Kiselev** 12:18 I believe…
**Mateusz Łach** 12:19 So.
**Alexey Pukhov** 12:20 Or maybe I should put something.
**Igor Kiselev** 12:23 I believe the question was if there is anything in pull request that's not ready to review, and I already have done a first review pass, and as I understand right now, everything that is in PR ready for review.
But PR is not ready in the whole picture, the pieces that… so it couldn't be merged, but it couldn't be merged because there are some pieces that have not been implemented at all yet.
**Alexey Pukhov** 12:50 Okay, I see. Okay, excellent. Yeah, that's a good… that's a good summary. You're gonna see some of the debug traces, which I'll be removing at the end of the PR, but other than that, everything there is…
There's no random code there.
**Mateusz Łach** 13:06 Okay, okay.
Yeah, so, so I think, like, the request would be to… for any of the,
Approvers and maintainers, or anyone in the sync, if someone could,
take a look and share some feedback, that'd be helpful, right? And by the way, thanks for the clarification, Alexei and Igor.
**Alexey Pukhov** 13:28 Oh, thank you for asking.
**Mateusz Łach** 13:30 Okay, yeah, so then we have a PR, from, Igor. Do you want to discuss this one? This is in drafts to you.
**Igor Kiselev** 13:39 No, I still have no time to finalize it, but everything except of end-to-end test required already here, so if anybody would take a look, there would be no more changes, except that I would end some tests.
**Mateusz Łach** 13:57 Okay.
Thank you, Igor. And then we have a native code bump from Piotr.
**Piotr Kiełkowicz** 14:07 It is still blocked by the…
I think you can close this PR for now.
**Mateusz Łach** 14:19 And this is blocked by… okay.
For sure.
**Piotr Kiełkowicz** 14:37 We should be able to handle it, let's say…
Together with .NET 11 release, I think.
**Mateusz Łach** 14:45 Okay.
**Piotr Kiełkowicz** 14:45 I'm not sure if it will be possible.
We'll do it earlier. Wheels.
**Mateusz Łach** 14:53 Okay, and then we have, OpAMP client, and this is waiting for, basically…
Alexei's, PR? Is that correct, Rasmus?
**Piotr Kiełkowicz** 15:10 Erasmus is not with us. Okay, sorry. But yes, it is blocked by this, this PO.
**Mateusz Łach** 15:16 Shh, okay, should I add some… Aww.
Information… Oh, this one.
Okay, so that's all for the PRs,
Let's see what new issues do we have.
So there is a release from your Piotr, right?
**Piotr Kiełkowicz** 16:00 Yes, there is kind of one issue important from the Splank perspective, you know, in scope of SPNET instrumentation.
**Mateusz Łach** 16:11 Right.
The baggage was…
**Piotr Kiełkowicz** 16:16 Yes, it is in queue, and we have agreed to refresh to make a release today the hotfix.
**Mateusz Łach** 16:25 Okay.
**Piotr Kiełkowicz** 16:26 Shortly, it's…
fixes the way when the baggage is propagated from the headers to the boat. Now it is just… it is after the activity is propagated, it should be before.
Just because activity… starting activity should have the… Access to these implicit contexts.
From the… from the baggage.
So, mmm… We need it into our instrumentation, distribution.
So, it would be great if you can make hotfix releases with these three changes. This kind of one is… the most important is the ASPNET Core.
The second one is kind of tiny fix related to resource attributes for the most common architecture. It was reported as 64 instead of AMD.
64, and the last one… last but not least, it's… we could include also stale versions of SQL client, there is no changes.
The behavior, just the version reference, but it is not necessary.
**Mateusz Łach** 17:54 Okay, and the plan would be to basically make a release, after this.
new versions.
Are available, right? So basically… Yes.
**Piotr Kiełkowicz** 18:05 Hopefully tomorrow.
Morning, our time, if you are fine.
**Mateusz Łach** 18:17 Any comments from the Sikh? Is that okay with you? Releasing the new version with these changes?
**Piotr Kiełkowicz** 18:30 So, I will hand it.
Thank you.
**Mateusz Łach** 18:33 Okay, then we have this one…
Okay.
Should I…
Yeah, do we… do we want to, like…
Added to the project, or set a milestone for this one?
Any recommendations?
**Piotr Kiełkowicz** 19:18 They have some doubts if we should attests
every single DLL included into the zip file.
Most of them are external dependencies. I'm not sure what are the best practices in such cases.
I can check with Robert what he thinks about this internally.
**Mateusz Łach** 19:54 Okay.
So, should I leave it as it is for now?
**Piotr Kiełkowicz** 19:59 I think so.
**Mateusz Łach** 20:01 Okay.
Okay, so there's another one… From Robert…
So this is already being handled by Martin, I think?
We have a…
**Piotr Kiełkowicz** 20:20 The PR is in progress, so I think you can put into the next milestone.
**Mateusz Łach** 20:25 Okay.
Hmm…
**Piotr Kiełkowicz** 20:29 Yeah, 115.
**Mateusz Łach** 20:32 Okay.
So, assign you to the board.
Totally.
Okay, and then we have some… something from the… operator… Opentelemetry Operator.
**Piotr Kiełkowicz** 20:50 There are some changes.
**Mateusz Łach** 20:51 Right.
**Piotr Kiełkowicz** 20:52 There are some changes in our release process. For now, we needed to make a PRs to operate a repository.
**Mateusz Łach** 21:00 Okay.
**Piotr Kiełkowicz** 21:02 Now it was automated, and Renovate is handling it for us. They are… Mikawa is requesting us to make the code owners of this file just to click approve before they will automatically merge, if you are fine.
I think, Nico, I will create appropriate PR.
**Mateusz Łach** 21:38 Okay,
Sounds like we are okay with that, right? So…
**Zach Montoya** 21:52 Yeah, makes sense to me.
**Mateusz Łach** 21:59 Piotr, any suggestions what to make?
**Piotr Kiełkowicz** 22:02 Yeah. You can just type that SIG is fine, and we can approve this kind of changes.
**Mateusz Łach** 22:40 Okay, so that's all for the issues.
I don't think there are any discussions.
Yeah, there's an infant here… Issues that should be assigned to the board.
Yeah.
Seems like probably milestone is wrong, right?
We don't have… This milestone yet?
Okay.
We have… These senties are on the board already.
So, the project board…
So this one is in progress, I think, right?
Okay, apart from that, any… any changes to the board?
**Piotr Kiełkowicz** 24:15 We have a request in the… Zoom chat.
To review some.
issue.
**Mateusz Łach** 24:24 Okay…
So this is from…
**BhupinderSingh** 24:32 Yeah, right.
**Mateusz Łach** 24:35 Country repository, right?
**BhupinderSingh** 24:37 Yeah, they said to Prinder.
Am I audible?
**Piotr Kiełkowicz** 24:41 Yeah, we can see rooms.
Yes, I think I actually…
I think it will be better to bring it up on the Tuesday meeting. There is the separate .NET seek
Not related to Delta instrumentation.
**BhupinderSingh** 25:02 Okay.
**Piotr Kiełkowicz** 25:03 I do not…
**BhupinderSingh** 25:03 That's probably quite late for me.
Okay, or I can connect.
On the Slack, right-click them, right?
**Piotr Kiełkowicz** 25:18 Give me a second, I was trying to find Dick's calendar.
**Mateusz Łach** 25:53 Okay, in the meantime, is there anything else, apart from, I mean…
Apart from what we already discussed that you'd like to discuss today? Any other topics?
Okay, I think in that case, thank you all for joining, and see you next week.
**Alexey Pukhov** 26:26 Thank you, bye.
**BhupinderSingh** 26:27 So, sorry.
**Alexey Pukhov** 26:29 Let me push…
**BhupinderSingh** 26:30 This is, like, 12.30 for me, 12.30 in the night, so…
Like, may I know what other way to submit?
Or… or I need to get in touch with… Approver on the Slack.
**Piotr Kiełkowicz** 26:47 Yeah, you can… try to reach, especially Raj.
On the Slack channel.
The Geneva or Geneva Exporter is kind of open-source exporter, but used internally only by the Microsoft team, so…
If you need to make there any changes, the best option is to contact directly with Rush. I will post you the exact name, you.
You can try to reach,
reach him on the Slack channel, or… Shock.
Yeah, and dedicated submitting is, as I mentioned, every… Every Tuesday.
We have kind of splitted it to SDK and contract repositories, and today we are trying to discuss on the auto-instrumentation stuff.
So there's kind of… Note… Let's say not all experts are included today.
**BhupinderSingh** 28:05 Okay, got it. So I will reach out to Raj.
I mean, what?
**Piotr Kiełkowicz** 28:08 Cool.
Thank you all, have a nice day. Thank you for joining.
**BhupinderSingh** 28:11 Thank you, bye.
