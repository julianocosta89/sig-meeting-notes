SIG: Java SIG
Date: 2026-03-26
Duration: 6 minutes
Zoom Recording URL: https://zoom.us/rec/share/1Y3Nhl9XMdjoS5bPwHvMh2CbuB4WfeQUXunMOCs2erOFsoSoP9JZLqPFdaI8Obe1.Xb0VXXaN-6qalZLi
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 01:57 Well, my camera seems to be trying.
**John Watson** 02:03 Well, we can hear you, at least.
**Trask Stalnaker** 02:08 That is the important part.
Cool. Well, it is, a bit of a slow week in OpenTelemetry this week because of KubeCon, but Yeah, let's… Anything anyone wants to talk about today, let's start with… Jonathan.
Profiling…
**Jonathan Halliday (IBM)** 03:09 I'm not ready yet.
**Trask Stalnaker** 03:12 I forgot.
**Jonathan Halliday (IBM)** 03:13 Just want to find the links. Yeah, so, announced at KubeCon, pretty much now, I think, actually. The profiling signal spec is transitioning from development to alpha, so, yay.
And, the next bit is getting some implementations, and getting them to work together, and getting people to use them.
So the… the key piece, is probably the… the profiler itself.
Most people will be using the eBPF profiler.
But some people will be using a Java one. They'll want to use async profiler.
JFR to generate the profiling data. And for those people, it would be nice if we gave them a bit of help by supplying some of the The sort of more boilerplate-y code they're gonna need.
for instance, to grab a JFR file, which both of those profilers can write, and converted into the… a TLP line format, and send it out over the wire. So I have most of the code for that.
It's tucked away in, a module in OpenTelemetry Java that so far, we haven't shipped. It's, the shipping bit is turned off, basically.
So, question, do we want to ship it, and if so, in which release?
We are missing, yeah. Slightly kept by not having, Jack Burke, yeah.
**Trask Stalnaker** 04:48 Yeah…
**Jonathan Halliday (IBM)** 04:49 Yeah, who needs to answer that one, I think.
**Trask Stalnaker** 04:52 Yeah, probably.
It definitely sounds reasonable, now that, to enable that shipping bit, It's just alpha.
It's not marked stable.
I would suggest… just send a PR to turn the… that bid on, and let's get feedback on it.
**Jonathan Halliday (IBM)** 05:23 Sounds good.
What's the release schedule? There's one just after Easter, is that right? Roughly every month, I think, yeah?
**John Watson** 05:32 The end of the first week of the month.
**Jonathan Halliday (IBM)** 05:35 Yeah, okay, so, I don't think… I don't think we'll hit that one, because I'm on vacation next week.
It'll be the tag.
**Trask Stalnaker** 05:43 April 10th.
**Jonathan Halliday (IBM)** 05:46 Yeah, that feels tight. I think… I think we'll aim for the May one.
**Trask Stalnaker** 05:50 Cool.
**Jonathan Halliday (IBM)** 05:53 Great, thanks.
**Trask Stalnaker** 05:55 Yeah.
Anyone else have anything they want to… Raised today, otherwise we can… Call it a shorty.
Cool.
Well… Shortest meeting ever.
**John Watson** 06:24 Yeah, we might be breaking some records.
**Trask Stalnaker** 06:26 See y'all.
