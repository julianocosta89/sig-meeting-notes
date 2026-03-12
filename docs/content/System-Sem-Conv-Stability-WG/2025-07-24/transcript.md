SIG: System Sem Conv Stability WG
Date: 2025-07-24
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/uHmkk1mcUUPoOpC_3Gr19gjSijzdMoJa3pZv-FcLkdhAiBc9ZEC1FpN5IcYcOHT0.jH1rMX7eSCU6ApYh
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:55 Hey!
Morning!
**Fraggle Rock (ca-wat-brt3)** 01:50 Only 3.
**Pablo Baeyens** 04:25 To Restart.
**Fraggle Rock (ca-wat-brt3)** 04:27 Yeah, might as well.
I think I am 1st on the agenda.
So this pr, is about nfs metrics been going for a while.
this this Pr and the Pr. For raid conventions have been going at the same time, and the the same person has been, I kind of upset, or at least seems upset to me at both. Really trying to make everything like more generic into the storage and Rpc. Namespaces, at least for the Nfs metrics, and I'm really not convinced the suggestions are useful, but they have been holding back this Pr. For ages. So if if anybody has time to take a look and like.
see if I'm crazy for thinking. These suggestions don't are are like they. They seem dubiously useful to me. Given how complicated. It would be the the metrics that are there make a lot of sense to me. For, like, if I'm just a generic user who wants to get nfs or nfs. Server metrics like the the metrics, work well as they are versus if they were just a bunch of like stuff in storage and Rpc. And they have to be like used a certain way. And then that's how you get your nfs. Metrics that feels weird to me.
So I'm if anybody has time to look, even if you don't really know about Nfs or Rpc. Stuff.
See, this is more in a general like metric design and usability sort of opinion, and see if I'm see if I'm on the right track here.
**Pablo Baeyens** 06:24 Okay, I I see, Josh just commented.
**Fraggle Rock (ca-wat-brt3)** 06:29 Yeah.
**Pablo Baeyens** 06:30 You said.
**Fraggle Rock (ca-wat-brt3)** 06:34 We talked about it offline a little bit, and he he seems he seems to sort of agree with me, and I think he's actually like.
I think he's on on board with merging mostly the way it is.
So we'll see we'll see what happens. These these Prs have been very draining to deal with, because then it starts getting into like interpersonal conflicts of like, I'm not convinced we should do any of this becomes less of a like a technical discussion, and more of a personal opinion discussion. And well, that is a lot less fun for me.
**Pablo Baeyens** 07:13 Yeah, I get that.
**Roger Coll** 07:22 Rpc, but yeah, we'll take a look just in case it aligns with some decisions that we have already made, or something like that.
**Fraggle Rock (ca-wat-brt3)** 07:32 Yeah, it's it's kind of a weird one, because, like, it's not totally strange to imagine some of the metrics might make sense in storage or Rpc because Nfs is a Rpc protocol for storage. But like the the stats are so specific and weird that I'm not sure it's worth unifying. Basically, that's that's that's kind of where my, where my head is at. It doesn't feel worth unifying across. Because, like, if you try and unify all these nfs metrics, and then they're only useful for nfs. Anyway. What was the point of them being moved into the storage and Rpc namespaces.
**Roger Coll** 08:10 Okay.
Let's see.
**Fraggle Rock (ca-wat-brt3)** 08:24 That was all for me.
**Dmitrii Anoshin** 08:36 Folks, I just want to mention that there is work going on on the aggregation, capability and and data gen, that would allow us to make a CPU state optional or not state, but CPU like CPU core optional.
**Fraggle Rock (ca-wat-brt3)** 08:54 The CPU core number, yeah.
**Dmitrii Anoshin** 08:55 Yeah, that would be good, and I'll I'll send the Pr. I'm I'm I'm reviewing it like it's all it's in progress. But if you're interested, please take a look. I'll post it in the doc.
**Fraggle Rock (ca-wat-brt3)** 09:12 Okay.
**Roger Coll** 09:19 A little bit related on that. Also. We have been playing around with Weaver and M. Dot Zoom, and looks like it's feasible to change at least what let's say, the P data SDK generation with Weber because it has a so basically, the problem that we were seeing is that there's some very specific golank or M dating fields like the value type or the future aggregation thing, that it's not on some right.
But in Weber you have an annotations field. And we can leverage that one to just arbitrarily use any, let's say, current failures and data. Gen. In the weaver generated templates, and who have been playing this week with with Damian. And yeah, we have actually converted a few templates already from and for the metrics and resource attributes. But yeah, we will share that.
I'll switch.
**Fraggle Rock (ca-wat-brt3)** 10:24 Cool, looking forward to seeing that.
Alright. If we don't have anything else, then I guess we can end early.
**Roger Coll** 11:08 Sounds good.
**Dmitrii Anoshin** 11:09 Good. Thank you. Folks.
**Fraggle Rock (ca-wat-brt3)** 11:11 Thanks. Everyone.
