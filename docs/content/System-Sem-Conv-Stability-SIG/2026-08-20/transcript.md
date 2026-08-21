SIG: System Sem Conv Stability SIG
Date: 2026-08-20
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:25 Hello…
**Pablo Baeyens** 01:28 Lou.
**Donal O'Sullivan** 01:31 No problem.
How's it going?
**Pablo Baeyens** 01:35 And…
**Donal O'Sullivan** 01:35 Good, thanks for the approval and the peer.
**Pablo Baeyens** 01:39 True.
You said Braden was going to take a look as well?
**Donal O'Sullivan** 01:48 Yeah, he said last week he'd have a look. Rogers approves it as well, so… I think, yeah.
I guess when… if Braden approves, we can merge.
**Pablo Baeyens** 01:58 Cool.
**Donal O'Sullivan** 03:31 I, I don't know if anyone else is gonna join, I know… Christos is out, and Roger's not gonna make this meeting, so… I'm not sure about Braden or Dimitri.
**Pablo Baeyens** 03:46 Yeah, I think Dimitri's back from vacation on… Ray don't as well?
Yep.
Let's keep them one more minute, and ignore.
We can start.
Okay, guess it's us.
I don't know that there's a lot to discuss about, like.
well, I guess if, Igor want to leave a review as well on the… on the PR from Donal, but I don't know if you have the context.
**Igor Peschinskii** 05:32 No, I don't.
**Pablo Baeyens** 05:40 And then I think your topic you wanted to discuss with Dimitri, probably.
**Igor Peschinskii** 05:46 Yeah, maybe I'll DM him.
For… Okay.
**Pablo Baeyens** 05:54 Okay.
Anything that we can do as we?
**Donal O'Sullivan** 06:04 I was gonna look at… I know, Braden had a PR open before for deprecating processes scraper. I know we discussed, myself and Braden, I think, and Dimitri discussed this previously, that… Once… once the process scraper goes release candidate, the next thing we can start doing is deprecating the process scraper and get those metrics into process.
scraper. I think that's… is currently blocked on Braden's work in Collector Core. I think he's made a PR about, Simplifying some way of filtering, I think, isn't it?
**Pablo Baeyens** 06:42 Let me check.
**Donal O'Sullivan** 06:44 Is there anything we can do there, maybe?
**Pablo Baeyens** 06:47 Yeah, maybe I can… maybe you thought,
**Donal O'Sullivan** 06:51 I think there was issues with the CI or something, wasn't there?
**Pablo Baeyens** 06:57 I don't remember, but I'll check.
Kratom…
**Donal O'Sullivan** 07:04 Okay, I linked it in the deprecation of the process scraper issue.
**Pablo Baeyens** 07:10 It's 15653, is that one.
**Donal O'Sullivan** 07:14 Yeah, I think so.
**Pablo Baeyens** 07:21 Oh, okay, yeah. And there's some…
**Donal O'Sullivan** 07:27 Oh, it's still failing on stuff as well.
**Pablo Baeyens** 07:29 Yup.
Yeah.
**Donal O'Sullivan** 07:33 Oh, that's cool, that's fair enough.
**Pablo Baeyens** 07:40 Yeah, I'm happy to merge that one, whenever the tests pass.
**Donal O'Sullivan** 07:44 Yeah, fair, yeah. Once that's merged, can we then work on the… deprecating the process of scraper, because it is the idea… I think it was Dimitri who wanted it, basically, an easy way to, like, disable lots of metrics per scraper, so you can just… for example, you could turn off Sorry, not deprecate, you could turn off all the process metrics on Process Scraper, but only run the processes metrics, was that the idea? Some way of filtering or something like that?
**Pablo Baeyens** 08:14 I think so, yeah, I'm not a co-owner of the host metric receiver, so I haven't been… Oh.
**Donal O'Sullivan** 08:25 Yeah, no, that's fair.
**Pablo Baeyens** 08:26 Super involved, but, you know.
**Donal O'Sullivan** 08:27 Nor is, yeah, no, I think that's the general idea.
Cool.
**Pablo Baeyens** 08:34 Okay, then… I… won't be here next week on Thursday.
So, from my side, see you the week after.
**Donal O'Sullivan** 08:48 Sounds good. See you guys.
**Igor Peschinskii** 08:49 to you.
**Pablo Baeyens** 08:50 Right.
