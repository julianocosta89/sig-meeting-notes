SIG: OpenTelemetry on Mainframes Weekly Sync
Date: 2026-11-11
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Richard Nikula (BMC)** 04:52 This is very weird.
Did you just join?
**Rüdiger Schulze (International Business Machines Corporation)** 04:56 You know, I'm actually.
**Richard Nikula (BMC)** 04:57 We've been on here for a while.
**Rüdiger Schulze (International Business Machines Corporation)** 04:59 Richard.
Thanks for joining.
**Richard Nikula (BMC)** 05:02 But now I can't hear you either.
**Rüdiger Schulze (International Business Machines Corporation)** 05:05 You can't hear me.
Can you see me?
**Richard Nikula (BMC)** 05:08 What is going on?
**Rüdiger Schulze (International Business Machines Corporation)** 05:09 Hey, Richard.
**Richard Nikula (BMC)** 05:11 Hang on.
**Rüdiger Schulze (International Business Machines Corporation)** 05:14 Can see you and I can hear you.
**Richard Nikula (BMC)** 05:17 There. Well, it's weird. I can see you, but it looks like you're sitting in a dark room.
**Rüdiger Schulze (International Business Machines Corporation)** 05:22 Sitting in a car.
**Richard Nikula (BMC)** 05:23 Ha ha ha.
Well, I joined the meeting and no one was here, and then I left, and then I and then I said, Well, I must have the wrong thing, and then I clicked around and eventually you were here, but I could see you taking notes. And I was like, Yeah.
**Rüdiger Schulze (International Business Machines Corporation)** 05:38 Ken, can you hear me now?
**Richard Nikula (BMC)** 05:40 I can.
**Rüdiger Schulze (International Business Machines Corporation)** 05:41 Okay, great. Then at least very briefly talk about what I put in the notes there.
So, I opened a set of PRs, based on this initial BICS PR for virtualization and mainframe HMC, To…
**Richard Nikula (BMC)** 05:59 Okay.
**Rüdiger Schulze (International Business Machines Corporation)** 06:00 To make it better reviewable, and also… Robert Payak, he's from Splunk. He had been doing some, AI-assisted review. I also took this into consideration. Effectively, actually, the split of this big PR is also done with… Something like that.
But I want to go over these PRs during the next week, so until next Wednesday, to just kind of, like, make the sanity checks. Also, there's a couple of things that, are dependencies, but need to be resolved in the meantime, so that makes these PRs also… a simpler structure, because the underlying, you know, tooling has been enhanced, hopefully as well. And, Then, essentially, we may actually go into a cadence where we aim to review each of these… well, one PR at a time.
Once per week, or something like this.
To make progress.
**Richard Nikula (BMC)** 07:02 Okay, yep, we definitely need to do something.
**Rüdiger Schulze (International Business Machines Corporation)** 07:05 Yeah.
So, and actually the findings that Robert was, you know, his tooling was reporting that was quite interesting. So obviously some inconsistencies and some, you know, unit hiccups and so on. So this was actually quite interesting.
**Richard Nikula (BMC)** 07:22 Right.
**Rüdiger Schulze (International Business Machines Corporation)** 07:23 Good stuff.
**Richard Nikula (BMC)** 07:23 It can't hurt to actually try to use it to figure out what's wrong.
**Rüdiger Schulze (International Business Machines Corporation)** 07:26 Yeah, yeah, right. And now that we have this in smaller pieces, I think it will be easier even for, you know, humans and AI to Right. Shot on this, and tell us what is missing.
**Richard Nikula (BMC)** 07:40 Okay.
All right, I will try to get to those.
And review them this week as well.
**Rüdiger Schulze (International Business Machines Corporation)** 07:46 Yeah, sounds good, Richard.
Okay.
**Richard Nikula (BMC)** 07:48 you.
**Rüdiger Schulze (International Business Machines Corporation)** 07:49 Yeah, so see you next week. I suppose also at least, you know, those who work for an observability vendor, they are probably at KubeCon this week. So.
**Richard Nikula (BMC)** 08:01 I know there was some… somebody mentioned that, Ann.
**Rüdiger Schulze (International Business Machines Corporation)** 08:04 Yeah.
Okay.
**Richard Nikula (BMC)** 08:07 Right.
**Rüdiger Schulze (International Business Machines Corporation)** 08:07 Richard, have a good one. Alright.
**Richard Nikula (BMC)** 08:09 How are you, Zane?
