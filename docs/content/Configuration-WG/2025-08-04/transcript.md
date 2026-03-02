SIG: Configuration WG
Date: 2025-08-04
Duration: 8 minutes
Zoom Recording URL: https://zoom.us/rec/share/odjAOHcrNoT1UytKpgY8O2A1r--btGk-HC30CmElbHTTlUUWV_JdH9mSP-tig8Ta.88lbPNn3U7b8SpDz
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:46 Nobody else here.
**Jay DeLuca** 00:49 Yeah, I was looking at the past couple.
I think this has pretty light attendance in general.
It looks like Tyler can't join.
**GZ Gregor Zeitlinger** 01:17 Yeah. Probably probably not much happening. Then.
**Jay DeLuca** 01:26 Yeah. Well, one interesting thing is, if you look down on the July 21st notes, it looks like they're
they're looking for a prototype in Java.
or something.
**GZ Gregor Zeitlinger** 01:43 Controlling context, propagation, boundary.
Oh, this is a very old issue.
**Jay DeLuca** 02:19 Oh, wow, yeah, 2021.
**GZ Gregor Zeitlinger** 02:22 It's ancient.
**Jay DeLuca** 02:27 This is an interesting problem. We had this issue at my last job.
We never solved it, but we were planning on stripping headers at our gateway.
**GZ Gregor Zeitlinger** 02:47 Yeah, I think that was also what I remember.
**Jay DeLuca** 02:54 It's interesting. It looks like they're
talking about, at least in like the last comment they're talking about
having the client be aware of where it's calling and maybe only including the context
on internal calls as opposed to external.
It's an interesting thought.
**GZ Gregor Zeitlinger** 03:21 Why is this coming up in declarative configuration.
**Jay DeLuca** 03:24 I'm just. I was just thinking that, too. I'm I'm curious what they're
what they're looking for in terms of.
**GZ Gregor Zeitlinger** 03:30 I think this is because it requires more elaborate configuration.
That is probably why
what would you want? You would want to define what an internal call is, or something, or what external calls are
what hosts.
**Jay DeLuca** 04:23 Yeah.
**GZ Gregor Zeitlinger** 04:23 So something like the peer service mapping, maybe.
Oh, yeah, here it is in the comment. Baggage
corp, dot tendency. My domain slash, sandbox
tenancy. Is that a name? For in Turner.
**Jay DeLuca** 04:55 See
Or maybe that's the new.
**GZ Gregor Zeitlinger** 05:05 That's what they were using internally. I'm just trying to
see what the word means. Okay, that does not help.
Door is ringing just.
**Jay DeLuca** 05:15 Okay.
**GZ Gregor Zeitlinger** 07:38 All right. Back.
**Jay DeLuca** 07:42 Yeah, yeah. So maybe we
come back and see if Dan wants to explain what they're they're looking for. Maybe in the next meeting, or maybe he'll pop up in the
the Java Channel, or something.
**GZ Gregor Zeitlinger** 07:55 Yeah, yeah, for today, the time is over, I guess.
**Jay DeLuca** 08:03 Yeah.
and actually dance.
**GZ Gregor Zeitlinger** 08:20 All right, then.
See you tomorrow, tomorrow or Wednesday.
**Jay DeLuca** 08:29 Yep, I think. Oh, yeah, I don't know. Do we have meetings tomorrow?
But yeah, I'll see you soon, either way.
**GZ Gregor Zeitlinger** 08:34 Alright! See you.
**Jay DeLuca** 08:36 Have a good one. Bye.
