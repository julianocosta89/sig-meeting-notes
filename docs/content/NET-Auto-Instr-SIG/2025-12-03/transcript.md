SIG: .NET Auto-Instr SIG
Date: 2025-12-03
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Yevhenii Solomchenko** 02:50 Hi, guys.
**Zach Montoya** 02:57 Hello!
**Mateusz Łach** 02:59 Hello?
**Rhynier** 03:01 Bye.
**Zach Montoya** 03:04 I've been having trouble with Zoom today, so hopefully I will be able to participate in the call and it won't crash.
We should probably get started at this point, but I'm also wary of, sharing my screen because of my issues with Zoom today. Could anyone else drive?
**Mateusz Łach** 05:07 Yes, I can drive, give me a second.
Hey, sorry, I can… Yeah, I can start.
Let me… And the usual stuff.
Okay, so starting with the… PRs, we have two bumps.
from Dependables, and we have, some ROSIN analysis.
PR from Pyot, then we have, One related to file-based config. Vini, do you want to share some context related to this one?
**Yevhenii Solomchenko** 06:41 Yes, so… And, our distribution, we cannot mark something like, YAML member, and add IDSs to the… properties, so… issue was in the slash for the example instrumentation development. We cannot, use that slash in the properties in .NET, so… I create, some hack.
For that.
interse with development, it will convert to the development of the YAML.
So…
**Mateusz Łach** 07:21 Okay, so you mentioned this being, like, a short-term solution, and what would be our long-term solution?
**Yevhenii Solomchenko** 07:31 I think a long-term solution will be… Create some provider in future.
for, vendor stuff.
It's not preparing the documentation specification for now.
**Mateusz Łach** 07:49 Okay.
Yeah, so I've seen there was some… there's some feedback already, right?
**Yevhenii Solomchenko** 07:58 Yep.
**Mateusz Łach** 08:00 Yeah, so if you could, add what Rasmus, added here, probably, to the PR, so that it's… I'm not sure if you had a chance to already update the description, so that's… Obvious what is, What is being blocked by this not working?
**Yevhenii Solomchenko** 08:24 Okay.
**Mateusz Łach** 08:26 Okay, so that was for the parser, then we have Roslyn and Lesis, we have this one, which is Interrupt, I'm not sure.
What's the current state of it? Seems like there was not much progress recently.
Yeah, so this… I think this, tries to… address the flaky tests.
Which we've been having for some time, so… Yeah, I'll try… try to follow up on this one.
Mmm.
And then we have support for capturing .NET framework call stacks, so FD cart, this is something that you are, like, Currently working on, right?
So it seems like there are a few tests to be addressed, some conflicts to be resolved after other PRs were merged, so… Yeah, so… What would be your, like, estimation when this should be ready to be reviewed?
**efshaikh** 09:37 So I'm going to push all the… test failures, as many as I can enable. There are quite a few flaky tests which I will not enable, but we'll have some fair coverage. So, the plan is to check in today. I'll merge the… whatever conflicts I'll resolve, and I will try to make as many tests, green as I can.
**Mateusz Łach** 09:59 Okay, perfect.
Yeah, so… Zach, if you, if you, if you could take a look in, in, coming, days, that would be very helpful.
**Zach Montoya** 10:15 Yeah, I took a look at the… at the summary, and I… I could review maybe some… native parts, but, I requested… I asked some other colleagues who are doing more profiling work to see if they had time to take a look, so I'll follow up with them, because I think they could probably give a better review than I can.
**Mateusz Łach** 10:35 Okay, thank you.
**efshaikh** 10:36 Thank you.
**Mateusz Łach** 10:39 Then there is Experimental OpAMP client.
Rasmus, anything you'd like to add here?
**Rasmus Kuusmann** 10:48 Yeah, so… this thing got blocked because of the dependency loading issue.
and I wanted to know if… the dependency loading for .NET.
It's intentional, like we have at the moment, so everything is loaded in the default.
Or it was not… Intentional.
**Mateusz Łach** 11:23 Yeah, I've seen you posted a question on Slack, did you get any response to that?
**Rasmus Kuusmann** 11:29 Nope, I think… Yeah, Raj was probably the best person to ask from, but no response at the moment.
**Mateusz Łach** 11:40 Okay.
Okay, so this is in draft, and probably… Aww.
will stay in draft for some time, right? Because my understanding is that the dependency that is coming with OpAM Clang is causing issues if app has the same dependency in different versions, is that correct?
**Rasmus Kuusmann** 12:18 Yep, so… and the protobuf is probably a quite popular library also, so it's a high-risk library.
Doesn't know.
On Flix.
**Mateusz Łach** 12:33 Okay.
Awesome.
Same home.
Then there is… there was some recent progress in this analog bridge.
Slash context injection PR, but I think Piotr took another look at this one, and this… there are still some failing tests, so… I'm not sure.
So, it seems like… All of this failing.
Okay, so this is mostly trace context injection, it seems.
Yeah, so probably… this problem needs to be addressed before… Hmm.
This is being ready to be reviewed.
Okay, so that's all for the PRs.
Then we have issues… There are so… there is, something new, and I think Rasmus already… You already, responded here, right?
So it seems like… or possibly the app has… Reference to different… different version of diagnostic source.
So…
**Rasmus Kuusmann** 14:14 Yeah.
So they mentioned that it is a generic .NET 9 application, it's probably… Somewhere there is a .NET… well, sorry, System Diagnostics, Diagnostic Service version 9 reference.
**Mateusz Łach** 14:30 Hmm.
Okay, so it seems like this one is, Mishandled, so… No-code configuration not working, I think Pete responded to this one.
Okay, so this is waiting for some additional information, it seems, because I think Piotr tried to reproduce it and wasn't able to do… So… So… This one… So this was, created by Steve Gordon.
And Piot responded as well.
Yeah, so this is assigned to Steven, seems it's, He promised to try to work on some simple… repro for this issue, so… Then we have… this one… I'm not sure if this one… was discussed… oh, sorry, Do we want, for the previous issues, do we want to assign some milestones, maybe, or… Any preferences?
I mean… Probably.
Not at this time. Okay, so… This one is missing reproduction, so… We need… probably need some more information in order to be able to help here.
What about this one?
Yeah, so… Well… Okay, so… this one, it seems like we could… assign a milestone to it, right? So… Field merchant needs to be reworked in the near future.
Do we want to assign it to 114 for now?
**Yevhenii Solomchenko** 17:29 Maybe, yes Around 14, I think, but it's okay.
**Mateusz Łach** 17:34 Okay, I need to… That worked as well.
And then we have… Yeah, what about this one, New Guinea? Any…
**Yevhenii Solomchenko** 17:56 Can be the next, I think.
**Mateusz Łach** 17:59 We'll be next.
**Yevhenii Solomchenko** 18:00 No.
**Mateusz Łach** 18:01 Okay.
**Yevhenii Solomchenko** 18:05 Limits are… for limits, we need to update, .NET runtime.
And, I'm laid there.
quantum material.net.
net blocked by .NET runtime.
So, also, it can be the next.
**Mateusz Łach** 18:25 Okay.
**Yevhenii Solomchenko** 18:34 parsing resources, I think, can be also next.
**Mateusz Łach** 18:38 Okay.
Then we have this one, created by Igor, so…
**Igor Kiselev** 18:45 I still intend to fix it, but I have not enough time, and… It's probably not very critical.
**Mateusz Łach** 18:53 Okay, should I add a milestone? Do you, do you… Estimate you might have some time in the near future to work on that?
**Igor Kiselev** 19:03 I… I'm not sure that I will have any time in December, but I intend to fix it in general, for sure.
**Mateusz Łach** 19:10 Okay.
Yeah, so, I'll add V14 for now, and, We might adjust it later.
Right.
**Yevhenii Solomchenko** 19:26 Okay, and then we have parsing resources.
**Mateusz Łach** 19:37 This one is… you were… You had some feedback here, Yukini, sorry if I missed it.
What would be the correct…
**Yevhenii Solomchenko** 19:52 I think that's gonna be the next also.
**Mateusz Łach** 19:55 Okay.
**Yevhenii Solomchenko** 19:56 Whenever you have time, we can do that.
**Mateusz Łach** 20:01 Okay, then we have discussions, but there are no new discussions.
Mmm… Oh, so we closed the milestone, so… Yeah, so this one… This one we wanted to fix for the next release, right?
So I'll assign it to the board.
And that was… And then the project port review.
Okay…
**Yevhenii Solomchenko** 20:57 I think it's also an incorrect version.
**Mateusz Łach** 21:00 Oh, yeah.
Do we need, like, a new view?
Not sure.
**Zach Montoya** 21:37 I think we usually just rename it to the current milestone.
**Mateusz Łach** 21:41 Okay.
**Zach Montoya** 21:42 Yeah.
**Mateusz Łach** 21:49 And then… is this… What else needs to be adjusted?
Hmm… Yeah, sorry, I'm… Not very familiar with… this process, so… Hmm.
**Zach Montoya** 22:26 I don't think… Changed.
For the most part.
**Mateusz Łach** 22:30 Yeah. Do we want to adjust anything else apart from the name on the… of the view?
**Zach Montoya** 22:40 I think, I mean, the other thing we could do is we could move the… The file base, like, the config.
I don't know if there's an overarching issue we could put in progress.
Otherwise, we can just move individual file-based configs to in progress.
**Mateusz Łach** 23:01 Okay…
**Zach Montoya** 23:02 Or… Committed, I guess, the ones that we want to target for 114.
**Mateusz Łach** 23:08 Yeah.
Do we have every platform? Seems like… For file-based config, we don't have that much in… backlog.
At the moment.
**Zach Montoya** 23:29 Okay, yeah, that sounds fine, we don't need to… Move anything, then?
**Mateusz Łach** 23:50 Okay, I'll try to clean up the view after the meeting.
Okay, so that's all for the usual stuff. Anything else you'd like to discuss?
Anyone?
**efshaikh** 24:19 One question. Do we need all the tests to be enabled? Because there are some really flaky tests in the context of .NET network. So I will enable the basic tests, but is the… what is the threshold for acceptance? I see for Mac, most of the tests are disabled.
**Mateusz Łach** 24:42 Oh, sorry, which tests are disabled?
**efshaikh** 24:44 For Mac platform, the selective sampling tests are disabled, so…
**Mateusz Łach** 24:51 Yeah, yeah.
**efshaikh** 24:52 So it's not a hard requirement that all the tests be enabled, because the architecturely .NET Framework has its own quirks.
But we should have basic coverage, and then gradually we can take it from there. I hope it doesn't become a blocker for us to merge.
**Mateusz Łach** 25:14 Yeah, so… How many tests are flaky for you?
Is it, like, big, like, big chunk of the tests, or…
**efshaikh** 25:24 No, not a big chunk.
But the… there are at least 2 to 3 tests.
**Mateusz Łach** 25:31 Okay, yeah, so I think we should, we can start with, like, having them disabled and discuss it in the PR, and You know.
Start with that, and Iterate on it.
**efshaikh** 25:48 Right. So the context propagation works, the basic, the stack sampling and verification of the expected call stack and what is actually reported. These are, like, the bread and butter of the stack.
blink part.
**Mateusz Łach** 26:10 I think, there might be some audio issues.
**efshaikh** 26:14 Fuck.
**Mateusz Łach** 26:18 I heard you, FDCar, when you started talking about that, it seems like we lost you.
-Oh.
**efshaikh** 26:26 those But let's… Can you hear me now?
**Mateusz Łach** 26:40 Yes.
**efshaikh** 26:43 Okay.
So… Which part did you guys miss, Dua?
**Mateusz Łach** 26:51 I've… I've heard you said that, like, the… like, the, The basic tests are working for you, and And then, and then I lost… then I lost you.
**efshaikh** 27:04 Okay.
So, the basic test, meaning if you… the test that verify the expected call stack versus actual reported call stack for that program, that works. Basically.
Covers the loop of actual stack sampling.
And the context propagation, that also works. The tests that wait for a duration and expect X number of samples, basically a range of samples, they want the count of samples to be within certain range. And that is highly unpredictable, and that's a flaky thing.
**Mateusz Łach** 27:41 Okay, yeah.
**efshaikh** 27:42 These are the tests that I would disable, the rest stop.
**Mateusz Łach** 27:47 Yeah, I think we can start with that. This test is known to be flaky, so probably some adjustments or rework, yeah.
**efshaikh** 27:54 Yeah.
**Mateusz Łach** 27:56 Okay.
Okay, thanks, Safdikar.
So, anything else?
Okay, in that case, thanks, everyone, for joining, and see you next week.
**Yevhenii Solomchenko** 28:18 Mine.
**efshaikh** 28:19 Thank you.
