SIG: System Sem Conv Stability SIG
Date: 2026-09-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 01:57 Hello.
**Igor Peschinskii** 02:00 Hello.
**Donal O'Sullivan** 02:55 Is your PR merged Igor?
**Igor Peschinskii** 03:01 My PR, about Jose.
**Donal O'Sullivan** 03:03 Yeah.
**Igor Peschinskii** 03:05 Yeah, it can be merged. Like, yesterday I got final approval.
from Ludmilla.
So, I'm planning to wait for it.
Day or two, and then measure it.
**Donal O'Sullivan** 03:21 Yeah, I think she gave more feedback to you to rename a file, is it?
**Igor Peschinskii** 03:25 Yeah, I'm gonna do it.
**Donal O'Sullivan** 03:27 Yeah, yeah.
Yeah, yeah, because they're the only ones that can merge, like, the maintainers have to merge the PR for you.
**Igor Peschinskii** 03:36 Hmm.
**Donal O'Sullivan** 03:37 Yeah.
It's a slow process.
**Igor Peschinskii** 03:41 Yeah, it took, like, 2 months.
**Donal O'Sullivan** 03:45 Yeah, well.
**Igor Peschinskii** 03:57 Like, I don't know, there will be.
Semantic Convention SIG meeting that Monday.
I'm not sure, should I go to this meeting to, like… Got more approvals for this PR, or… It's fine to merge, since Lumio approved it.
**Donal O'Sullivan** 04:15 Yeah, I mean, like, if… you could… you could just go to it and, like, just bring it as… bring it up to bring attention to it. I assume if you addressed all the feedback that Ludmilla had asked, she'd… and you went to the meeting eric hansen: she'd probably merge it then and there, or just after. It's… it can be nice to kind of, like, help speed up the process a bit, especially when they put, like, a face to the work, I guess, if that makes sense.
And yeah, have you attended the SIG before?
**Igor Peschinskii** 04:50 This sick? No, I didn't.
**Donal O'Sullivan** 04:52 Yeah, it's normally… it's quite casual, so it's normally fine. No.
Hope to.
**Dmitrii Anoshin (Splunk Inc.)** 04:59 Hi, folks.
**Donal O'Sullivan** 05:00 Hey Dmitrii.
**Dmitrii Anoshin (Splunk Inc.)** 05:13 Do we have anything on the agenda today?
**Donal O'Sullivan** 05:17 They just have one thing.
**Dmitrii Anoshin (Splunk Inc.)** 05:20 You discussed that already, or not yet?
**Donal O'Sullivan** 05:23 No, not yet. So it's just regarding the feedback from promoting, system I need to think about this for a second. System attributes to release candidate. Ludmilla had come back. I know a bunch of the… a bunch of you had approved the PR, but Ludmilla came back with a couple of open issues. One of them was the attribute, system.device.
There was an open issue around that, so I think she was looking to either merge that with hardware, metric, or hardware attributes, or either… if not, if we couldn't do that, then namespace system.device, so I have it, like, system device name, just so, like, we could… Give some kind of a… Clear, kind of, name, like, clear understanding as to what System Device is doing. So, I just opened the PR there to rename it to SystemDevice.name.
And I just updated the, you know, updated all the the markdown files and the just updated the description to be a bit more specific to systems, so like OS related kind of.
Interface naming.
So, yeah, I had previously, I think I brought it up.
I brought up that, the other, the system attribute PR up.
Maybe last week or the week before, and I think most people were on board with the change.
Yeah, so just bring that, bring some attention to it.
**Dmitrii Anoshin (Splunk Inc.)** 06:56 And we don't use that currently in In-house metrics receiver anyway, right?
**Donal O'Sullivan** 07:01 No, so we do use device. So we have an attribute device that stands alone. I guess that probably should be system.device, or it should have been. Maybe it was just like a legacy thing.
Because there is no device attribute, I guess, right?
**Dmitrii Anoshin (Splunk Inc.)** 07:17 Exactly. And my point is that we haven't migrated from device to system device yet. So it's good to change this now. So we migrate from device to system device.name.
**Donal O'Sullivan** 07:29 Yeah, yeah, spot on, yeah, exactly. Yeah, yeah, yeah.
So, just a question on that, then. If we… so, if we get… if we get this name change through, and we want to make, System Attributes Release Candidate.
Would we have to make the device change in host metrics to system device name first?
And then down… so just go straight to release candidate and system device name.
**Dmitrii Anoshin (Splunk Inc.)** 07:56 Yeah, of course. Yes, that's that's exactly was my question.
**Donal O'Sullivan** 07:59 Okay, cool.
That makes sense.
**Dmitrii Anoshin (Splunk Inc.)** 08:08 Yeah, that.
Sounds good to me. I approved it. Thank you.
**Donal O'Sullivan** 08:14 Thanks Dmitri, appreciate that.
**Dmitrii Anoshin (Splunk Inc.)** 08:25 Anything else, folks.
**Donal O'Sullivan** 08:29 There is a couple other issues on the system attribute PR.
I think most of them can be closed off, but I, not closed off, but, like, I don't think they affect it.
I think Braden has to get back, but yeah, I left a comment about it in the System SIG Slack, so if you have some time, maybe have a look, but no pressure.
**Dmitrii Anoshin (Splunk Inc.)** 08:55 Okay.
Okay, cool.
**Donal O'Sullivan** 09:04 That's all I have, anyway.
**Dmitrii Anoshin (Splunk Inc.)** 09:08 Okay.
Should we wrap it up earlier, then?
Sounds good.
Thank you, Ron.
**Donal O'Sullivan** 09:20 Yeah, right.
