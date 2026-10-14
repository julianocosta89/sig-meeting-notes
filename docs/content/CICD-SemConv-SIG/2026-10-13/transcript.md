SIG: CI/CD SemConv SIG
Date: 2026-10-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Alan Clucas (Pipekit Inc)** 02:41 Hi, Carlos.
**Carlos Alberto Cortez (Dash0)** 02:46 Hey, hey, how are you doing?
**Alan Clucas (Pipekit Inc)** 02:48 I'm okay.
Surprisingly quiet here.
**Carlos Alberto Cortez (Dash0)** 02:51 Yeah, I think Adriel is busy this week.
But I didn't see anything from Christoph, so… Oh, actually, Christophe cannot make it. Okay.
**Alan Clucas (Pipekit Inc)** 03:06 Shall we leave it till next time, then?
**Carlos Alberto Cortez (Dash0)** 03:08 I think so, yeah, unless… Unless you can provide feedback for me regarding GitHub, but probably you don't.
**Alan Clucas (Pipekit Inc)** 03:18 I don't… yeah, I haven't, I don't have any fatigue… I mean, I wanted to talk about the stuff you were talking about with, like, queuing time and stuff, but it probably would be better done when we're all around.
**Carlos Alberto Cortez (Dash0)** 03:32 Yeah, well, it still could be nice, you know, like, are you talking about the queue time?
**Alan Clucas (Pipekit Inc)** 03:38 That's part of…
**Carlos Alberto Cortez (Dash0)** 03:39 Okay, yeah.
**Alan Clucas (Pipekit Inc)** 03:39 That part is… I mean, I… so I go workflows.
emits pending time.
Which is, like, is it queued? You can't actually tell from the… the span, what it's queued on. It could be queued waiting for another… if it's, like, once a… if it's got a lock it needs to take, if it's just waiting for Kubernetes to schedule a pod, they all appear as pending time, but… Yeah.
**Carlos Alberto Cortez (Dash0)** 04:05 Yeah, yeah, yeah, correct. For me, the tricky thing is also that as you said, like, you don't know what's happening, and based on what I saw, at least from GitHub case.
It's overlap, you know? So basically, the… Let's say the top level task.
Excuse?
And then, so it's subtask ROQs.
And then the queue time is… has, like.
like, a huge, like, not small, like, huge overlap with the top-level task, Q span.
**Alan Clucas (Pipekit Inc)** 04:36 Yeah.
**Carlos Alberto Cortez (Dash0)** 04:37 And I don't know whether there's value in reporting that in that case, you know.
**Alan Clucas (Pipekit Inc)** 04:43 I, I think there is. I think independently.
**Carlos Alberto Cortez (Dash0)** 04:47 Okay.
**Alan Clucas (Pipekit Inc)** 04:49 I don't know. Even if they're… Even if they're different, even if there's a massive overlap and stuff, I still think there's… It's useful, but… yeah.
**Carlos Alberto Cortez (Dash0)** 04:59 Yeah, yeah, yeah, yeah, okay, yeah.
Probably Adrian has an opinion on that one, since he's the maintainer of the Kit Hub.
receiver.
**Alan Clucas (Pipekit Inc)** 05:09 Yeah.
**Carlos Alberto Cortez (Dash0)** 05:10 Ha!
**Alan Clucas (Pipekit Inc)** 05:10 Yeah, Christopher will have some experience with the same sort of thing in Jenkins, so I think it's worth waiting for everybody to be around.
**Carlos Alberto Cortez (Dash0)** 05:17 Yeah, yeah, yeah. Okay, I will ping them, so they don't forget.
I mean, if they're… if they're busy, nothing… nothing to do, but if they are, like, yeah.
Okay, yeah, if you… if there's something in your mind about that later today or the next day, just, yeah, just feel free to comment something there.
**Alan Clucas (Pipekit Inc)** 05:36 Yeah, I think I put some comments on your earlier thread.
**Carlos Alberto Cortez (Dash0)** 05:39 Yeah, correct. Yeah, you did. Yeah.
**Alan Clucas (Pipekit Inc)** 05:41 So, yeah, I don't really have anything to add. I was going to show you what my spans look like.
At the moment, I mean, they're not trying to be SemConf compliant at all.
But at some point they should be.
**Carlos Alberto Cortez (Dash0)** 05:57 Yeah, yeah, actually, it's the same for me. Like, you know, my employer, Dash Zero, you know, we have this, potent CACD action, and we are trying to Implement all the semantic conventions, but there are some things that are… Not present in Semcom.
And so, for now, we understand that We will do it the way we think is the best.
For now, but yeah, the plan, of course, is, like… and that's kind of the stop.
The reason why we also want to provide, you know, some reviews.
So we can actually, if we think there's value in this or that thing, we can try to make it part of hotel.
And then we are aligned, hopefully. But yeah, but for, yeah, but for the time being.
A lot of things, the new things, new changes will not be part of the hotel. So that's, that's part of the trade-offs.
**Alan Clucas (Pipekit Inc)** 06:54 Yeah.
Okay.
**Carlos Alberto Cortez (Dash0)** 07:00 All right. So, yeah. Good to see you. Dr. Joe Heinz. Yes.
**Alan Clucas (Pipekit Inc)** 07:05 In Titan.
**Carlos Alberto Cortez (Dash0)** 07:06 Joe.
