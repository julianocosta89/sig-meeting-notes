SIG: .NET SIG
Date: 2026-01-27
Duration: 10 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 01:02 Hello, Matthew.
**Matthew Hensley** 01:05 Hello.
**Rajkumar Rangaraj** 02:08 Let's wait for a few more minutes to see if the others join here.
**Matthew Hensley** 02:14 Alrighty.
**Julius Koval** 03:32 I am.
**Rajkumar Rangaraj** 03:36 E.
I don't see any agenda in the…
like, the documenter. Does anyone have any topic for a discussion today?
**Julius Koval** 03:50 Hi. Yes, actually.
I think, can you hear me?
**Rajkumar Rangaraj** 03:56 Yeah, I can hear you, go ahead.
**Julius Koval** 03:57 Yeah, okay.
So I think sometime in, September, I asked about…
the Logs Rich API, and I think you said that…
At the time, you were busy with .NET 10, but after that was released, you might consider working on it?
**Rajkumar Rangaraj** 04:15 If you have a bandwidth to contribute, I would say you should go and start the process. We would be able to review and move forward.
**Julius Koval** 04:24 Sure. And is there something specific? Because,
Yeah, I don't know if there's…
**Rajkumar Rangaraj** 04:31 There is nothing specific. Already, there is a work done by branch, in one of the branches, so you can just go and visit around that, and, see if you… come back to us if you need any help.
In the next zig.
**Julius Koval** 04:47 Yeah, just… I guess I didn't hear you. You said Blanche was doing work on it?
**Rajkumar Rangaraj** 04:54 Yeah, Blanche has done… it's in… already… the work is in the experimental phase.
And,
All we… mostly you may need to test and flip the switch from the experimental to the stable one and verify everything works. That's what you may need to do with. Probably that's the research you might need to… I'm not familiar myself with that part of the code. So…
**Julius Koval** 05:23 Sure.
**Rajkumar Rangaraj** 05:23 That's right.
**Julius Koval** 05:23 I guess… Yeah, so I guess Blanche would be the person to talk to.
**Rajkumar Rangaraj** 05:29 Blanche is kindly… he is not doing the .NET anymore, but I would say first go ahead and review the code, and whatever we have it, how it is, before reaching anyone out.
probably we will also… the maintenance and approver also will do the same, because if you're planning to get started on it, we also need to go and take a look into it. Or Alan may have a lot of context, because this was done before I become very active in this repo, and I was not much engaged when that experimental feature was added.
So, if not, I would ask you to reach out to Alan, who is another maintainer of the repo, so he would be able to give, like, a head start for you on this one.
**Julius Koval** 06:14 Okay, sure.
Yeah, so I'll, ping him.
Okay, thank you.
**Rajkumar Rangaraj** 06:24 Are there any other topics?
I have one other, topic I thought I'll discuss, like, the…
I had a question about, to Alan and Martin about the SQL instrumentation stable release. We have been in this RC version for nearly two weeks, and the plan is to do the stable release by the end of this week.
I'll follow up with them offline on the Slack to see if we could do that. I just wanted to check, as Jack, Matthew, and Julius, as you are here, like, did you guys get a chance to try out the SQL instrumentation? Are there anything that you heard about that? Any feedback? Do you guys have it?
**Zach Montoya** 07:14 No, I don't have any feedback on it.
**Rajkumar Rangaraj** 07:17 Okay.
**Julius Koval** 07:19 We've been using it for a while, but I don't have any… Specific feedback, either.
**Rajkumar Rangaraj** 07:25 Go ahead. Someone else was saying something?
**Matthew Hensley** 07:30 I was just gonna say, it's been, stable enough.
No concerns?
**Rajkumar Rangaraj** 07:35 Cool. Then I'll… I'll just go and check, like, work on this to see, with Martina and Alan. They were too much engaged in this space to see if we can move that to the, towards the stable from RC.
Huh.
That's all the topic, like, we can take a look at the PRs. There are a few PRs from Martin.
So these are all the new PRs that got, created…
decently, but, I saw in one of the PR, like, whenever…
we are trying to do the reducing the, like, size, getting rid of the regex parsing, but looks like Martin left a comment saying that it's, rather it is increasing the size of the,
package.
So… Probably, I would, wait to see how this is heading. Apart from this, we…
We have one other PR which is pending in the long state, it's the last one. I think at least we have the clarity from the single-threaded environment. We'll go ahead and review this last one. If anyone of you have bandwidth, please take a look at the last PR and provide the review feedback.
The remaining are a very small one, yeah. Anyone has time, please revisit those things, too. So, nothing important over here, which is…
And if I recall correctly, there are not any… there are no new issues also.
And we did the release last week, and,
we should plan to do the, like, if LogBridge API becomes stable, that's something we need to incorporate in the next release.
So apart from that, I don't see any…
Big things that we have to tackle it as of now.
At least there were no issues or something. We can, just revisit and see if there are something we can, tackle it for the next minor version.
Nope.
Yeah, that's all I have it. Are there any other…
Thanks, anyone, for discussion. If not, we could end, oddly.
Cool. Thanks, everyone, for your time.
**Zach Montoya** 10:31 Alright, thanks. See you.
**Julius Koval** 10:33 Yeah, thanks, bye.
