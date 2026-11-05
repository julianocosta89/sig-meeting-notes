SIG: Collector SIG (EU/ET)
Date: 2026-11-04
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andrzej Stencel (Elasticsearch B.V.)** 01:37 Hello.
**Pablo Baeyens (Datadog)** 01:43 Hey.
**Damien Mathieu (Elastic)** 01:44 Hey.
**Ervin Wallin** 01:45 Hello.
**krajo (Grafana Labs)** 02:29 Hi, Eric.
**Andrzej Stencel (Elasticsearch B.V.)** 02:34 Please add your names to the attendees list on the from the doc and add any topic you have to discuss.
Does anyone have anything for the, priority?
**Pablo Baeyens (Datadog)** 03:31 Yeah. I have one. So On the release happening next week, we will have Config HTTP as a V1 module.
Which means that all of the… Go module dependencies for the OTLP receiver are now V1, so I want to start the process for marking the OTLP receiver as V1 as well.
So part of the process is announcing that at one of the SIG meetings, so here's the announcement.
If you think there is something missing, please comment on the issue.
There was one sub issue about telemetry.
Umm Because of the… the RFC, for the Cortistro B1, I have removed that as a blocker.
Umm.
I… Don't think there's anything else, but… Yeah, please comment if there's something that I'm missing.
**Andrzej Stencel (Elasticsearch B.V.)** 05:11 Awesome. Damien, do you want to continue?
**Damien Mathieu (Elastic)** 05:16 Yes, thank you, Andrzej. I just want to raise awareness on the RFC that suggests introducing a dash dash from config to OCB init. Basically, it would allow folks migrating from, like, a country container collector to their own distribution.
More easily, they take their own Collector, we detect every module that they are using in their configuration, and we build the manifest out of that.
This RFC has been pending in review for almost two months now. It would be nice if we could try to move it forward.
**Pablo Baeyens (Datadog)** 06:04 From my side, it would be nice if we have Arthur and Braden.
At least notified, and if they want to…
**Damien Mathieu (Elastic)** 06:13 Brayden already reviewed. He hasn't approved, but he reviewed left things that have been resolved since. Arthur, I pinged, but since he is not really involved in OCP anymore, I'm not sure he wants to take so much time on that.
The last code owner is Josh McDonald, and he did approve.
**Pablo Baeyens (Datadog)** 06:37 Okay, yeah, if we could get great honest approval, that would be great.
**Damien Mathieu (Elastic)** 06:41 being Brayden.
**Andrzej Stencel (Elasticsearch B.V.)** 07:12 Any other topics?
**Pablo Baeyens (Datadog)** 07:43 Doesn't look like it.
I guess. Thank you, everybody.
**Andrzej Stencel (Elasticsearch B.V.)** 07:55 Thanks, everyone.
**Pablo Baeyens (Datadog)** 07:57 See you.
**Evan Bradley** 07:57 Everybody.
**Ervin Wallin** 07:59 Thank you, goodbye.
