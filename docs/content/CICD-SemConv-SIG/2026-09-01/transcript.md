SIG: CI/CD SemConv SIG
Date: 2026-09-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Adriel Perkins** 00:59 Hello, hello!
**Christophe Kamphaus** 01:01 Hello? How are you doing?
**Adriel Perkins** 01:04 I'm okay, how are you?
**Christophe Kamphaus** 01:06 Fine.
And you?
**Adriel Perkins** 01:09 Good.
**Christophe Kamphaus** 01:16 I see it's been some time since I was meeting.
**Adriel Perkins** 01:20 Yes.
That's what it looks like.
**Christophe Kamphaus** 03:00 Will we get started?
**Adriel Perkins** 03:04 Yeah, I don't think we can.
**Dotan Horovits (Amazon Web Services, Inc.)** 03:06 Yep, sounds good.
**Christophe Kamphaus** 03:20 So on our board, I saw there hasn't been much activity.
We still have the VCS burned semantic conventions, pull request sets open.
And I think it's missing the prototypes.
**Adriel Perkins** 03:39 Do we have any ETA on those prototypes?
**Christophe Kamphaus** 03:43 No, I think… He asked about it, we… I gave him some points where he could start, but I'm not sure if he… If he will do it.
Otherwise, I could, take a step at doing it for Jenkins.
Yeah, I think I would, have to do that.
**Dotan Horovits (Amazon Web Services, Inc.)** 04:21 I, I thought you wanted to anyway, get to that, and Jenkins said, I mean, regardless of that, or was that.
**Christophe Kamphaus** 04:27 Yeah, yeah.
**Dotan Horovits (Amazon Web Services, Inc.)** 04:27 My immediate one, right?
**Christophe Kamphaus** 04:29 Yeah, the Jenkins PR, the previous one, has been merged now, so, yeah, I can move on.
What's there.
**Dotan Horovits (Amazon Web Services, Inc.)** 04:38 Then we have, like, a full, end-to-end, example they can show both for the graduation and also for… as a reference for others to implement. I think it's… Could be a really good, hopefully, useful asset to get some more, folks to, to try it out and implement.
Yep.
**Christophe Kamphaus** 05:02 Yeah, that's currently the only thing in progress.
Or do you know about anything else?
**Adriel Perkins** 05:16 It's not on the board, but I have been working on the updating of the infrastructure, so that we can start to do the… direct action instrumentation and have it show up through ENV context propagation. So… But now that the infrastructure is up-to-date, And I have some automations that back it. We can go ahead and search.
found a… found a Python script that's in the Shared Workflows repository for dashboards.
So, intend to, start to add the NV context.
propagation tracing there, so that we can see how that works in advance of the talk that Robert's doing.
**Dotan Horovits (Amazon Web Services, Inc.)** 06:01 Eating your own dog food, huh?
**Adriel Perkins** 06:03 Exactly.
**Dotan Horovits (Amazon Web Services, Inc.)** 06:04 Super cool.
**Christophe Kamphaus** 06:08 You know, so we still have C… implementation in the SDKs for… Context propagation.
And I think Sarah… Some languages are a bit slower.
The Rust one was, auto-closed.
Yo.
So maybe they are waiting for it to be stable, I don't know.
**Dotan Horovits (Amazon Web Services, Inc.)** 06:49 Has it come up with, in any discussion, or, like…
**Christophe Kamphaus** 06:53 Did you try to reach out?
**Dotan Horovits (Amazon Web Services, Inc.)** 06:54 comment? Oh, okay.
**Christophe Kamphaus** 06:55 Now, I tried to reach out to them.
And I saw the rustic, their meetings are relatively rare.
And I didn't get any reply on Slack easily.
**Dotan Horovits (Amazon Web Services, Inc.)** 07:07 So it could be that they're just, no, independently of this specific, feature request that, like.
less active, I guess, or something like that. I'm just wondering if it's something related specifically to this, or is it systemic to that group, because I'm less familiar with the Rust folks, to be honest.
**Christophe Kamphaus** 07:25 I don't know Samisa, so it could be that.
**Dotan Horovits (Amazon Web Services, Inc.)** 07:28 Sugar.
**Christophe Kamphaus** 07:36 And for the long-running traces, I think I saw some activity there. Carlos, how is it going?
**Carlos Alberto Cortez** 07:46 Could you repeat, Dave, which one?
**Christophe Kamphaus** 07:48 I saw some notifications from GitHub, I don't remember which one, but I think it was related to…
**Carlos Alberto Cortez** 07:56 No, not from my side. I haven't received anything myself. Could you open that? Maybe somebody commented on that one. But yeah, there's a long PR that I was working on, but I was… I have been busy with other… Daytime job stuff.
Because, yeah, the plan was to continue working on the spam processor modifications or additions.
So we could be reported… we could… we could get reports, like, when… whenever Span is updated.
But now that we are talking about that, I should talk to my boss, so we get some cycles on that front. At least to grab that up, you know, so we got And actually, the discussion was fine.
the only thing was that I had to… Create a prototy, because there are, well, long story short, how-tos, Make this happen.
I think everybody was on board.
From the specification side, the thing is that there was… there are a pair of ways to… how to implement this, and that was pretty much the thing. So I should take it over. So I will try to work on that this week, if not next week, before, you know, now that Adriel and everybody else is back in town.
**Christophe Kamphaus** 09:18 Yeah, good for you.
Do we have any topics to discuss today?
Also, sends a quick… Updates we now went through.
**Adriel Perkins** 09:43 None from my side.
**Christophe Kamphaus** 09:52 And it was great to see everyone again, and… Let's start again working on stuff.
**Dotan Horovits (Amazon Web Services, Inc.)** 10:01 Thanks, Christophe. Thanks, everyone.
**Carlos Alberto Cortez** 10:03 deal.
**Adriel Perkins** 10:04 Thank you, sir.
**Carlos Alberto Cortez** 10:05 Oh.
**Christophe Kamphaus** 10:05 You too. See you.
**Dotan Horovits (Amazon Web Services, Inc.)** 10:07 Sir.
