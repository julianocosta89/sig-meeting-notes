SIG: K8s Semantic Convention SIG
Date: 2026-07-07
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang** 01:29 Right.
**Christos Markou** 01:33 Hello.
**Tyler Helmuth** 03:37 Merry Christmas.
I haven't come to one of these, I think, maybe ever. But I wanted to show up because we marked that KACE Attributes Processor stable. So I wanted to come for the celebration.
I see.
**Christos Markou** 03:48 Don't have a celebration, just boring stuff. But yeah.
**Tyler Helmuth** 03:51 Bum.
**Christos Markou** 03:53 We can do a celebration, though, we can convert a meeting, if you want.
**Tyler Helmuth** 03:56 Okay.
You guys did so much work on it. I just stood there and said, don't change the names ever.
**Christos Markou** 04:05 Yeah, I mean, someone commented right from from Grafana already. Yeah.
**Tyler Helmuth** 04:13 I had same, I had same comment, yep.
**Christos Markou** 04:15 Okay, nice. And Alex also from Honeycomb side. Yeah.
**Tyler Helmuth** 04:19 Mmhm.
**Christos Markou** 04:20 at at this point. It's mostly collecting feedback, and we'll see how how we can proceed.
I guess we can start. Yeah, not sure if anybody else will join. But Let me check the Slack.
Nobody… Shit. Okay.
We have one for kids, right?
Oh, I cannot see it.
There.
Does the Slack thread, the Slack channel still exist?
Anyways, yeah, I'll check it later. So… I have, I can share my screen.
Should be too many times.
You see the agenda, right?
Okay, so, I think last time we discussed about, this fix on the CPU usage calculation, and I took some time to actually try this implementation out.
And, I also, Test this manually to verify that our results look.
sane, and it seems that it, it's what we have been discussing. So the approach that I took is to actually introduce a feature gate for this, just to be sure, and… calculate on the fly the rates for the pod CPU usage node and container CPU usage, and at the same time we leverage the this result, the the CPU usage course to calculate the CPU utilization metrics that we have, so the change is transparent. If you enable the feature gate, both the CPU usage metrics but also the CPU utilization metrics are calculated based on this new approach.
And, yeah, I think it's pretty much it. One note here is that, I found that the CPU stats metrics, from kubelet stats API come, with a timestamp on them, so I… thought that might be better to use this but I'm open if there is any concerns around this or maybe David if you have any if you have more input on this and insights that This might be problematic. We can use maybe the systems time, the collector time, for example, from the environment the collector runs.
But to me looks better, looks more, looks cleaner.
safer, maybe, to use the timestamp that the data come with directly from the API.
Yeah, I guess that's pretty much it about this. Any concerns, questions, otherwise would appreciate reviews.
**David Ashpole** 07:50 I will. I'll take a look.
**Christos Markou** 07:53 Yeah, I added you here, David, even if you're not a code owner, sorry for this, but your review would be really helpful, I guess.
Yeah, I think other than this, now that the attributes are stable, I was checking the list with the metrics that we have.
It seems that most of the metrics that For example, cubelets that receiver emits are introduced are asymmetric conventions. The trickiest part is the CPU utilization, the utilization metrics essentially for both metric for both memory and CPU.
I was thinking to take a look into this in the following weeks, but my question right now is if we should consider about promoting entities to, like, release candidate or something, because we have intentionally promoted that entity.
Kept them out so far.
Maybe that's a question for Dimitri. I pinged both Dimitri and Josh here.
I don't know.
My question always is.
If we need the entity relationships support.
Because for Kubernetes, I think it's critical to have this in.
But, yeah.
**David Ashpole** 09:32 I don't, I don't know the answer to this.
**Christos Markou** 09:35 Yeah, so… Yeah, let's, let's wait then and, I can raise it with the meter again. There was another another… Issue that is, like, easy to tackle, I think.
Oh, is it here?
Yeah, this one from Zhao.
Umm.
So I think as part of the stability efforts on the system side.
there was a discussion about paging.
paging fault type common attribute that is part of the registry and someone mentioned that maybe it's not correct to have metrics on Kubernetes side that both yeah.
Use memory and paging.
for the… inside the name, because paging implies it is about memory, and for example, the common attribute is just system paging. We use this, but on the metric name, we'll have memory, and and I think the on the system side, the the metric does not involve memory at all. It's just system.
Yeah, oh, no, yeah, should be somewhere here. So the proposal is to maybe rename these metrics to remove the metric mention entirely and just keep it like KH pod paging fault, for example.
I think it makes sense. I can open a PR and discuss it there on the reviews. If you have any objections or any input on this, feel free to comment. But, yeah, I think it's a good idea.
I think. But I think, yeah, this is more or less the let's say the the backlog right now. I I will try to push for metrics and have some progress there as well, and hopefully entities.
because I think it's a requirement for metrics to have stay to have the related entities promoted to any stability level along with the metrics. Process entity was promoted along with the process metrics.
Yeah, I don't… I'm not 100% sure if we can proceed on Kate's side.
Yeah.
Anything… Else from anyone.
Nope.
Okay.
Then I guess we can keep it short today.
That's all I had from my side.
Okay, so…
**Stephen Lang** 12:35 Thanks.
**Christos Markou** 12:35 Weeks. Thank you. Bye.
**David Ashpole** 12:37 Bye, everyone.
**Dmitrii Anoshin** 13:35 Hi there. Are you still here? Hi there.
