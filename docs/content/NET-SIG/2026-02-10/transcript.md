SIG: .NET SIG
Date: 2026-02-10
Duration: 10 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello** 00:10 8.
**Matthew Hensley / Grafana Labs** 00:14 Hello!
**Martin Costello** 00:18 He caught you off.
**Matthew Hensley / Grafana Labs** 00:18 You will.
Have not… But I do have wonderful weather, so I'll take that.
**Martin Costello** 00:28 Not freezing, then.
**Matthew Hensley / Grafana Labs** 00:30 It is… something like 16, 17 Celsius.
**Martin Costello** 00:37 That's certainly better than we've got here.
**Matthew Hensley / Grafana Labs** 00:40 Now, it's, quite funny, because it snowed so much, but of course it's going to take FOREVER to melt, so it's… I have all the windows open, and fans on, and…
It's… there's 6 inches of snow outside.
**Martin Costello** 00:58 Don't think that ever happens in the UK.
**Matthew Hensley / Grafana Labs** 01:02 Yeah.
**Martin Costello** 01:06 Hey, Zach.
**Zach Montoya** 01:08 Hello!
How's everyone doing?
**Martin Costello** 01:12 I think he…
**Zach Montoya** 01:21 Did you all end up watching Super Bowl? I don't know how… where are you guys located?
**Martin Costello** 01:27 I'm in the UK, so…
I didn't watch the Super Bowl, but even if I wanted to, I'd have to stay up very late.
**Matthew Hensley / Grafana Labs** 01:36 which part of it? I'm in Kentucky, so… My,
Not much into sports myself, but my son is, so…
March about half the game. It was… Yeah, mediocre.
**Zach Montoya** 01:51 Yeah, it was a low-scoring affair.
But I'm in Seattle, so, everyone's pretty happy here.
**Matthew Hensley / Grafana Labs** 01:59 Oh, yeah, that'll… that'll do it.
**Martin Costello** 02:05 I think that was the only fact I took away from the Super Bowl, was that the Seahawks won.
Alan said he's not going to be able to make it today.
But I haven't heard anything from Raj.
So… Maybe give him one minute.
And if he doesn't turn up… On attempt.
To run the meeting.
Right.
We might get rushed any second, because I just saw he left a comment on a PR.
Hey, Raj.
**Rajkumar Rangaraj** 04:45 Sorry, I got just late. Martin, I see you have a topic. Do you want to start?
**Martin Costello** 04:52 Sure,
I noticed that there's a lot of open PRs at the moment that are, like, small fixes, so I wondered if maybe we should do a patch release soon.
That, that was the entirety of the topic.
**Rajkumar Rangaraj** 05:08 I think we can do a patch release, but what I would recommend is, like, in… at least we… it is a time for us, instead of doing all the packages based… all the packages, making it as 0.1, only release the SDK with 1.51, and not impact.
**Martin Costello** 05:26 Oh yeah, that's what I meant, not do everything.
**Rajkumar Rangaraj** 05:29 Yeah.
**Martin Costello** 05:30 That have got changes.
**Rajkumar Rangaraj** 05:32 Yeah, historically, what we have been doing is, even if one package got impacted, for example, if there is a…
We need to release a patch for OTLP export. We used to release all the packages because of our pipeline constraint. Probably, it's a time we need to fix and release the package that has impacted.
**Martin Costello** 05:58 Right, okay. Yeah, it's just… it's just, it seems to be bug-fixing season.
**Rajkumar Rangaraj** 06:04 Yeah.
Is there any other topics from anyone else for discussion?
let me share my desktop. I've not been pretty active in the past week, because,
I was, like, heads down with the other internal,
issues to take a look at it. So this week, I have some cycles to spend here.
Martin, you have been very active over here. If anything needs attention immediately. I just saw this PR as, like, a good addition for us, and just reviewed and, looked good to me. But do you see anything else that we need to prioritize here?
**Martin Costello** 07:21 Based on a Slack conversation a week or two ago, probably the second-to-last one.
If you scroll down.
**Rajkumar Rangaraj** 07:30 Yeah.
**Martin Costello** 07:32 It's my fixed thread safety one.
**Rajkumar Rangaraj** 07:35 Yeah.
I'll prioritize and take a look at it, this one, today.
**Martin Costello** 07:44 I think everything else has either got pending comments, or they're just maintenance rather than bug fixes.
**Rajkumar Rangaraj** 07:53 Okay.
Do you have any timeline in mind when we could do this?
patch release.
Probably we will wait for a week, or even we…
**Martin Costello** 08:11 I was just thinking to, once all of the PRs that are bug fixes are in.
Okay, cool. Either immediately after, or, say, wait a few days in case another one appears.
**Rajkumar Rangaraj** 08:24 Yeah. And then cut a release then, because I think if everything that's a small bug fix…
**Martin Costello** 08:29 that's currently open gets merged, plus there's one that got merged yesterday, and it's like, I don't know, between 5 and 10 bucks.
**Rajkumar Rangaraj** 08:38 Correct. Even it might take a week for us to do the release. The reason is the current pipeline does not allow us to release
Single package as a patched version, so we may need to do the modification to that, and merge that too.
In order to do the patch release.
**Martin Costello** 08:57 I guess it depends which ones have changes by the time everything's merged.
**Rajkumar Rangaraj** 09:02 Yeah, that's correct, but we need to allow our pipelines to release the packages independently.
Right now, it's all bundled together.
**Martin Costello** 09:14 Right.
**Rajkumar Rangaraj** 09:18 So, I think… That's all we have right now, nothing like, Much.
Does anyone have any other topics they want to bring for a discussion here?
Okay, like…
for everyone, like, whenever you get a chance, please, take a look at the PRs, like,
we have a lot of PRs here, only Martin is very actively looking into it. Both myself and, like, Alan, being a maintainer, we just got a bandwidth issue and got slowed down here. Probably I should be back.
To the active mode here from next week on, but, and, help from others also would help here if you, if they go ahead and take a look at, the PRs over here for review.
Okay, I don't have anything else. I think we could end the meeting early then.
Thanks, everyone.
**Martin Costello** 10:31 Any next time.
**Zach Montoya** 10:33 Alright, see ya.
