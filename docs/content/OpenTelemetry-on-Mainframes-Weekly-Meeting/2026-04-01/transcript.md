SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-04-01
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 01:36 Hi, John.
**Jim Porell** 01:38 I think it's just you and me.
**Ruediger Schulze (IBM)** 01:40 Okay, and let me at least, give you a very brief update, and I will put it also to the notes.
**Jim Porell** 01:46 Okay.
**Ruediger Schulze (IBM)** 01:47 So, for the TPS PR that we talked on, which is already ongoing for long, and as we discussed on the other call, and you made a comment there as well.
One of the asks on the semantic convention SIG was if we couldn't create a block asking for more contribution from TPS owners, so transaction processing system owners.
And I… I hope I find time to create a draft, and then I would, you know, get this back to the semantic conventions sig, because… I think it's probably good if they look at this before and make their comments.
then, And then let's see what's coming back from this.
The second thing is, and, I need to take this back to… to… to Greg, I think he's working on the, you know, he has, created this PR for the documentation around, mainframe and open telemetry.
I think there will be a couple of more updates on that one. I had this reviewed by somebody from us internally with some suggestions. I still need to see them, but there should be a few updates to that, and I will get this also in.
Okay. And, then… as I said, right, you know, we had this discussion with the semantic conventions.
sick. I think, you know, iteratively, we need to walk through these different topics. Virtualization, obviously, is something that also the community still needs to do some, you know, progress.
I think we, you know, we may, again, you know, pick up what we've done, and also you contributed to this last year, and share this back to them when it… When it comes to this discussion, I think, and also the semantic conventions, they have been recently, you know, there was the KubeCon Europe, I think this, you know, actually, also, they, you know, had some meetings that didn't happen. I wanted to join this Monday, but realized that it was, you know, still because last week the… KubeCon was, it was… didn't take place.
So, and Monday we have… this coming Monday, we have the…
**Jim Porell** 04:24 Monday.
**Ruediger Schulze (IBM)** 04:25 Monday, so I will not join on Easter Monday, probably, then. But, I think there's a few things in flight that we want to finish off, and then finally get to this discussion that, that we want to have, at least for a couple of basic… We realize it's, it's probably no secret, and others may have this as well.
that is really important to… to get, you know, some of these basic attributes on the telemetry, right? Because the backends… Right.
**Jim Porell** 04:54 We want them to implement it, right.
**Ruediger Schulze (IBM)** 04:56 There are certain conclusions on this, or even displaying this, and I think it will be really important to get this right for some of these. Right. So, yeah.
That's all I have, Jim, but as you are here, so I wanted to at least give you an.
**Jim Porell** 05:12 Yeah, no, thanks.
**Ruediger Schulze (IBM)** 05:14 That things are, you know, somewhat in flight, right?
**Jim Porell** 05:19 Is this time going to continue to work for you? Because I know recently you've been hauling But we switched time zones, so…
**Ruediger Schulze (IBM)** 05:26 Yeah, so these time zone switches, this is really, not making it better. Hopefully, you know, the coming weeks, it will work better. It's 6 PM my time. Right. Yeah, let's see, if it doesn't work at all, then we need to kind of, like.
Change time again.
**Jim Porell** 05:47 Yep, okay.
**Ruediger Schulze (IBM)** 05:47 The intention was to put it in for, you know.
For others also to come in.
**Jim Porell** 05:53 Right. Right.
**Ruediger Schulze (IBM)** 05:55 Okay.
**Jim Porell** 05:55 For Antoine, it's a problem for him.
**Ruediger Schulze (IBM)** 05:57 Yeah.
**Jim Porell** 05:58 Triple booked every, you know, each meeting, so…
**Ruediger Schulze (IBM)** 06:01 Yeah, I'm open if you try to look for a new time,
**Jim Porell** 06:06 Okay.
**Ruediger Schulze (IBM)** 06:07 it's, yeah, it's obviously not easy, but I think, you know, we… We want to do it in a way that, you know, we can actually be productive on semantic conventions, at least.
**Jim Porell** 06:20 Right.
**Ruediger Schulze (IBM)** 06:21 Right… I, just as a side comment, it's also of interest here, even if I don't have any specific results yet, for GSE U-Key, my virtual session about no-code instrumentation, OTEL on C got accepted, so I think now I need to do some testing.
Alright, yeah, yeah.
**Jim Porell** 06:44 Any feedback on the… performance problem with the collector on Linux.
**Ruediger Schulze (IBM)** 06:48 I haven't heard… I heard on this, and I believe there was also no updates anymore from the person who created it, but let me check on this. I… I… I know…
**Jim Porell** 06:58 Well, my fear is that this is a problem on x86, too, and it's a volume problem. My first thought is it's a volume problem versus it's truly a performance problem.
**Ruediger Schulze (IBM)** 07:11 Yeah, let me see, I… let me… let me… let me just look at this, but I think there was no update, at least I didn't realize any further updates happening there.
This was this one here. Open issue.
It's open. And the last comment is… More or less from… from my colleague, It was really asking for ways to reproduce this.
And… Yeah, so I think it somehow got stalled.
**Jim Porell** 07:47 Okay.
**Ruediger Schulze (IBM)** 07:49 Maybe, maybe the person figured out a different way, but, there's no, no activity on this.
Okay. Right.
And, Also didn't name… of the person opening it doesn't kind of, like, say anything where… where…
**Jim Porell** 08:09 It was a customer case, wasn't it?
**Ruediger Schulze (IBM)** 08:11 It was kind of like, but.
**Jim Porell** 08:14 Or was it internal?
**Ruediger Schulze (IBM)** 08:16 And so, it's not, you know, you can't see from where this is coming from, and in what kind of… You know, context this, if this is production or testing, or… right?
Obviously, Red Hat 9.6, number of CPU cores, too.
Oh, is this virtual or not? It's not visible, I think.
**Jim Porell** 08:53 Yeah, whether it's a native LPAR or a…
**Ruediger Schulze (IBM)** 08:55 Yeah, would be a very small helper anyway, with two.
**Jim Porell** 08:59 Yeah, right.
**Ruediger Schulze (IBM)** 09:00 But… but anyway.
It's pro… this might be actually a… Let me see, this is written here somewhere. Non-production, okay, this is given.
Yeah, okay, so non-production, but not much.
**Jim Porell** 09:26 Yeah, we're all curious about that one, because again… Yeah. Because the fear… we've had other conversations, I don't think you've been on it, but the fear is… Z has the possibility to flood a collector, given the size, you know, and if it's tests, though, I'm less concerned, but… and that's why the question is, is this a generic collector problem, you know, that all collectors are going to have this issue, or is it unique to Z?
**Ruediger Schulze (IBM)** 09:54 Hmm.
Yeah, I understand what you say, it's just that… Okay, there's the config, and I would have to take a look more closely on this, but supposedly this is… It's not a… Something that we can clearly follow up on.
**Jim Porell** 10:18 Okay.
Has anyone done any benchmarks internally of it, or is that impossible?
**Ruediger Schulze (IBM)** 10:24 So… I've… if you ask about the Open Telemetry Collector, there have been tests done, and actually some recommendations also are published.
with the Obsolvability Connect.
**Jim Porell** 10:37 Okay.
**Ruediger Schulze (IBM)** 10:38 I would have to go to the documentation for this.
**Jim Porell** 10:41 I'll go, look, I'll go.
**Ruediger Schulze (IBM)** 10:42 So, so some testing has been done.
And, that is actually a… it's… Okay, this would be more for the distributed side, but there are quite a number of references out there of what People have been able to… to run with the collector.
**Jim Porell** 11:03 Nope.
**Ruediger Schulze (IBM)** 11:03 Quite, you know, scalable. Obviously, this would have to be transported over or transferred over to the platform to have similar tests done there.
But, yeah.
**Jim Porell** 11:17 Okay, that's it.
**Ruediger Schulze (IBM)** 11:19 Okay, good, Jim, then, I will try to join next week, that should be possible, and, then also at the, at the given time.
**Jim Porell** 11:30 Okay.
**Ruediger Schulze (IBM)** 11:31 Yep, okay.
**Jim Porell** 11:32 See ya.
**Ruediger Schulze (IBM)** 11:33 Thanks for joining, Jim. Yep, bye.
**Jim Porell** 11:35 Bye-bye.
