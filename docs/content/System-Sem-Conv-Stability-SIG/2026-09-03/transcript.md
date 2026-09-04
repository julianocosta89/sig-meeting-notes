SIG: System Sem Conv Stability SIG
Date: 2026-09-03
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin (Splunk Inc.)** 04:30 Hi, folks.
**Christos Markou (Elasticsearch, Inc.)** 04:33 Nope.
**Donal O'Sullivan** 04:34 Anyways…
**Christos Markou (Elasticsearch, Inc.)** 05:03 Seems we don't expect… Anybody else, we can start, I added the first one.
Which is about, a comment on, Kubernetes?
related PR that promoted the network.
metrics to… To release candidate.
There was a comment from, thompson?
that, Tom Shantomo, that, the… metric name that… It's like… He's… suffixed with .io.
might not be the best option, because potentially in the future, we would need to have this as a namespace as well. This is linked, though, to the system metrics, because we have a very similar metric in system metrics, and also we have… we have system disk I.O. metric, and we also have the metric System Network I.O.
So… The question is something that we need to Discussion is, What we want to do with these metrics, if we need to change them or not.
I think it was clarified last time that we touched this issue, issue 2062.
It seems… it seems that the limitation was coming mainly from ECS, but Was confirmed that… ECS, it's not an issue anymore.
So, probably, we don't need to do this rename now.
But we need to validate this and come to a conclusion, and… Either close that issue, or, Yeah, figure out what we have to do.
**Dmitrii Anoshin (Splunk Inc.)** 07:02 I'm wondering why it's in the Kubernetes issue. Do we have a similar thing in Kubernetes as well?
**Christos Markou (Elasticsearch, Inc.)** 07:11 So, in Kubernetes, the metric format is similar to system.
**Dmitrii Anoshin (Splunk Inc.)** 07:16 Okay.
**Christos Markou (Elasticsearch, Inc.)** 07:17 So… I see. So…
**Dmitrii Anoshin (Splunk Inc.)** 07:18 datas.pod.netro.io. Okay.
**Christos Markou (Elasticsearch, Inc.)** 07:21 Exactly, and…
**Dmitrii Anoshin (Splunk Inc.)** 07:22 Currently, the I.O. is networked bytes for the port, which is… Cumulative.
Number of bytes being transferred through the network in one direction or another.
Oh my god.
Fair.
**Christos Markou (Elasticsearch, Inc.)** 07:44 I remember we had an extensive discussion A while ago, I think we even discussed it at the KubeCon, a while ago.
To, to come up with this.
This, metric name, the disk I.O. specifically, I think.
So… now… The question is, if we are happy with this, metric modeling, or… If we need to change it. I think… I don't see any reason to change it, actually.
**Dmitrii Anoshin (Splunk Inc.)** 08:20 why not? What about additional… like, if we don't change it now, we need to address the comment, saying… Like, for example, limited utilization can be… named, differently without I.O.
Conflicting with the… are your namespace conflicting with the metric name?
**Christos Markou (Elasticsearch, Inc.)** 08:44 Yes, because I think it's not a limitation anymore, so I think we need to clarify Another for another time, if that is actually a limitation, or it's not a limitation anymore.
**Dmitrii Anoshin (Splunk Inc.)** 08:57 Oh, you're saying that, like, specification that doesn't have that restriction anymore?
**Christos Markou (Elasticsearch, Inc.)** 09:04 I'm not sure if it was part of the specification, I think it was part of some… maybe policies or something in Semat conventions, and that was because of ACS.
But…
**Dmitrii Anoshin (Splunk Inc.)** 09:18 I… no, I don't think it's a CS. I think it's… it's generic. I remember that receipt.
**Christos Markou (Elasticsearch, Inc.)** 09:24 generic.
**Dmitrii Anoshin (Splunk Inc.)** 09:25 It was generic, specifically, done for in OpenTelemetry.
And, yeah, so I… where can maybe quickly find, right, but, yeah.
I think that's a good, like, start. We can go into SpecSeq.
And tell that, hey, we have those metrics that are just about to be stabilized.
And we might have potential other metrics that would use the same, Name, as a namespace instead of, ventricle.
So, we need to have some guidance, whether we break everything now and adapt to the restriction, or we leave the restriction.
**Christos Markou (Elasticsearch, Inc.)** 10:12 I'm pretty sure…
**Dmitrii Anoshin (Splunk Inc.)** 10:13 I'm pretty sure it comes from the form of telemetry and not from ECS.
**Christos Markou (Elasticsearch, Inc.)** 10:18 Okay, okay. Alright, so in that case, I think, yeah, as part of the… system metrics ability, since we have this disk I.O. and network I.O, we need to clarify this before proceeding, so… Okay.
We can do that, I guess.
Cool.
I think… Yeah, that's mostly what I had.
Any other comment about the issue?
I'm sharing thought.
And buddy.
Cool.
And go to the next one, then.
Thanks.
**Donal O'Sullivan** 11:12 Yeah, so I have a pull request to, in semantic conventions to start moving the system metrics to release candidates, so I started with the attributes that Host Metrics for ZRA uses.
So any metric… any system metric that Host Metrics Receiver uses, I marked the attributes used, referenced by those metrics as release candidate, with the idea… idea if we… If we get this merged, we can mark the actual metrics as release candidate, then?
I guess there might be an issue, though, Crystal, as you were talking about the… For example, is a system, disk I.O. and network I.O. might have to be discussed further, but that shouldn't affect the current PR.
So… Yeah, it's just that the pull request is there if you want to have a look.
**Dmitrii Anoshin (Splunk Inc.)** 12:14 Yeah, thank you, Donald, I'll take a look.
I think it makes sense.
**Christos Markou (Elasticsearch, Inc.)** 12:19 Each one is just about the attributes first, right?
**Donal O'Sullivan** 12:22 Yeah, so mark the attributes first, and then… and then we can mark the metrics, but there might be more discussion of that, as you say.
Yeah.
Thanks.
**Christos Markou (Elasticsearch, Inc.)** 12:42 Alright, if there's… Nothing else, we can keep it short today.
Thank you, folks. See you next week.
**Dmitrii Anoshin (Splunk Inc.)** 12:54 Thank you, bye.
