SIG: Sampling SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Sridhar** 01:48 Hi Chris, can you hear me?
**Chris Marchbanks** 01:54 Probably need to unmute myself. Hello!
**Sridhar** 01:57 I was just checking if the audio is working or not. This is the first call that I'm joining, so just checking.
**Chris Marchbanks** 02:03 Yeah, no worries.
I guess I'll put a video on, too. Yeah. I think we're… we generally… Josh is the one running this, so… Waiting for him, but yeah. Sounds good.
Oh.
I don't know if… let me check the Slack channel, I don't know if anyone's showing up.
Josh cannot attend today, so I'm guessing not much will happen. Do you have any topics you want to chat about?
**Sridhar** 05:23 No, I just joined to listen in.
**Chris Marchbanks** 05:25 Okay, cool. Well, I'll try again in a couple weeks, then. Have a good one.
**Sridhar** 05:30 Just a question, Chris, I don't know whether you can answer it or not.
But I was facing an issue with the OTEL Java SDK.
Okay. Where if I use HTTP to send out the traces and metrics to the collector.
And I'm using, SmartDNS, a global traffic manager for failovers.
As to address the high, availability of the collectors. I have my collectors running in multi-region, so if one goes down, then the GTM will update the, IP for the DNS.
**Chris Marchbanks** 06:12 Okay, and go to, like, some… in a different region or something like that.
**Sridhar** 06:15 Yeah, but the problem is, when I use HTTP, until the… until I have to restart my application.
the hotel Java SDK is not able to get the new IP. It is caching in, and there is no way for us to… set the DNS time to leave value also.
**Chris Marchbanks** 06:37 Yeah, I… I'm not super familiar with the Java one, so I can't help you too much, but yeah, definitely… I don't know, I'd suggest maybe just opening… see if you can open an issue in the Java SDK repo?
**Sridhar** 06:49 Okay, okay.
**Chris Marchbanks** 06:50 And see if other people are running into that, if somebody can help you out there. Otherwise, there's also the… there's a Slack… Let me see if there's a…
**Sridhar** 07:01 Yeah, I posted. I posted.
**Chris Marchbanks** 07:03 Airport.
**Sridhar** 07:04 in OTEL or posted in OTEL Java SDK, none of them responded.
**Chris Marchbanks** 07:08 Okay, yeah, I would try an issue in the repo, since, like, if it's being cached in the repo somewhere, like… Hmm.
**Sridhar** 07:14 Okay.
**Chris Marchbanks** 07:15 That would at least direct it somewhat, Good luck. Sorry I can't help you too much on that side.
**Sridhar** 07:22 No problem.
**Chris Marchbanks** 07:23 used Java much recently.
**Sridhar** 07:25 Okay, good.
Yeah, thanks, Chris.
**Chris Marchbanks** 07:28 Yep, have a great day.
**Sridhar** 07:29 Have a good day, take one.
