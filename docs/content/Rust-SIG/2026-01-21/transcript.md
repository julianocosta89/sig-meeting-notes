SIG: Rust SIG
Date: 2026-01-21
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/avHB-v5aGVJE5hgUsi24kN3xnrn1AHDkG6Z7p4GX7_Hk5_94MFusHDA55Sur8j3D.OvcomR-8SWhumJDF
============================================================

## Zoom Recording Transcript

**Björn Antonsson** 08:04 Hey there, Franco.
**Franco Posa** 08:07 Hello, hello.
**Björn Antonsson** 08:09 So, looks like it's just you and me. I'm not sure if anybody else is gonna join, I just asked in the… Reviewer's channel, so…
**Franco Posa** 08:22 Hmm.
**Björn Antonsson** 08:23 Yeah, did you have anything in particular?
Wanna discuss, or…
**Franco Posa** 08:30 No, I mean, I just started, joining these. I've been mostly working on the, The tower instrumentation and the contrib repo.
And I talk with CJO a bit about, you know, how to keep moving there. So I've been creating some issues, in terms of tracking towards stabilization there, and reviewing any PR as he shoots my way.
**Björn Antonsson** 08:56 Cool.
Yeah, I haven't looked at that power integration. I looked at the code before, I think, but… I saw the discussion… I'm going to read through the discussion about the path thing in… In Slack.
And, and just look at it quickly and see if there's something that could be sort of, like, pulled out and generalized, even if it's not according to spec, if it's a common pattern for, like, things in Rust.
So, maybe we could… pull something out, like the extractor or something. I mean.
**Franco Posa** 09:45 Yeah, yeah, I think our plan right now is to make a, like, a configurable extractor, And I guess it would first probably be generalized to, like, the tower system for HTTP, but there's a lot of stuff that uses that, so I think it is fairly general.
But yeah, especially since we're not, like, at a 1.0 yet, we can fiddle around with these defaults and these options, without.
**Björn Antonsson** 10:13 Cool.
**Franco Posa** 10:14 Breaking too much.
**Björn Antonsson** 10:29 No issues, or no response in the… In the… in the approver's channel, so I think it's just gonna be you and me.
**Franco Posa** 10:54 Is there anything else you want to get, just, like, in the agenda, or go over?
**Björn Antonsson** 10:59 No, I mean, I think it's, the same… I'm just gonna… there's… there's this PR. I'll… I'll, I'll just, I'll just ping CJ again, because he… last time he said he was gonna look at it.
We went over some PRs, so… It's not from me, it's from an outside contributor, and it actually fixes a bug, or really makes really unwanted behavior, like, crashing into kind of, weird behavior, but documented.
Which is better, I guess. We could maybe discuss if we're gonna make it even more strict, the behavior, but yeah.
So…
**Franco Posa** 11:53 This sounds good. Well, I guess.
**Björn Antonsson** 11:54 No, it's in there. Yeah, absolutely.
Have a great, where are you, by the way?
**Franco Posa** 12:00 Which is in California, so it's, morning.
**Björn Antonsson** 12:02 Oh, frickin', freaking early.
So, I'm in… I'm in Stockholm, so this is the end of… end of my day.
**Franco Posa** 12:12 Okay, okay. Well, enjoy your evening.
**Björn Antonsson** 12:15 Yeah, have a great day.
**Franco Posa** 12:17 Very dangerous, but…
