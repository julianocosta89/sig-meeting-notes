SIG: Rust SIG
Date: 2026-05-05
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/5YmiOnYovVEQSILVNst7tgFac8DSVTMrDhUNPTBQk_gIgc3FLog2jPnRV0PSm4e7.XPLyQWP1Fcpkujwb
============================================================

## Zoom Recording Transcript

**Björn Antonsson** 04:56 Hi there, I don't think any of the maintainers will be joining today, either.
Yeah.
So… Does anybody have any… Issues in particular they want to discuss?
**Davide Melfi** 05:13 Yeah, oh, yeah. But yeah, yeah, I was joining because I raised, a CR.
For, the metrics.
in Rust, so basically what I've noticed is that Basically, metrics have no constructors, no public constructors, so… We… it's… it's basically, difficult to basic… to… to use the exporter, which is public.
Without, without those objects in there.
So, yeah, I wanted to ask about, yeah.
if this is something that is useful, I already created a CR for that.
And that's it.
It's a specific issue.
**Björn Antonsson** 06:04 Yeah, okay. I have… I'm mostly looking at the tracing side of things. I haven't looked at, at that PR.
**Davide Melfi** 06:17 I can give you… I can give you the… The issue…
**Björn Antonsson** 06:23 Yep.
**Davide Melfi** 06:27 This is the issue.
And I created a… PR for that.
Which is this one.
Okay, amazing.
That's it. So, the point is that for all the other, signals.
we have… Public constructors.
For tracing, for example, or for logs, so there is a way to use the exporter.
But, metrics are the only one that do not have this kind of… Of public constructors. So, basically, you can only read from them without… without generating those objects.
So… Yeah.
The point is that I think, I think that… This should be fixed, and should be… should be public, because otherwise there is no point in making the exporter public.
**Björn Antonsson** 07:34 Okay, yeah.
See if we can take a look at that one.
It's a snitch.
**Davide Melfi** 07:44 Thank you so much.
**Björn Antonsson** 08:00 Anybody else have anything they want to discuss?
Okay, I guess, we can end it early then.
Nobody else have any topics?
Oh, man.
Thanks for joining me. See you around.
