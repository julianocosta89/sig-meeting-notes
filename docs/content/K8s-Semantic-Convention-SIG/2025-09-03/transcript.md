SIG: K8s Semantic Convention SIG
Date: 2025-09-03
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/_s_gbquME_OjYRC3H3jk-l-Zpd2N2CyOHlWWzgC-IjT2bB6jD3yxV_11LfHamNWy.k9vijR0GoFUqBoP1
============================================================

## Zoom Recording Transcript

**Christos Markou** 00:31 Hello.
**Stephen Lang** 00:33 Hey.
I guess we can wait.
A minute.
See if anybody else turns up.
**Christos Markou** 01:28 Yeah, most of those.
**Stephen Lang** 02:35 Alright, I don't think anyone else is gonna turn up here. I don't think anything's changed other than one…
issue I was looking at has moved into blocked status.
Look on the… The triage board.
Okay, it's… Status, reason.
I think that's the only thing that's changed that has, just been moved in there.
That's the one, yeah.
**Christos Markou** 03:08 Yeah, that's correct.
we can talk about this a bit. So, the thing is that we have already introduced similar
Metrics describing status or phases, so on. And… the…
Where is the… yeah, so the question that…
Came up here is about having, if it is allowed to, or what should be the recommended way to…
to model this. And, we didn't have…
like, guidance so far, and Bryden started
Brandon Gaines, started this… PR to add this…
guidance about this, because this also affects the system metrics working group.
And there is this discussion and this concern about, if the name of the metric
Should be, the same.
With the name of the attribute.
And Tyler, also raised some concerns here. I guess that, yeah, this sounds… the concerns make sense, actually.
I was also wondering, because there is a restriction, I remember there was a restriction, or…
Kind of restriction in the past that, didn't allow… didn't allow us to have
the name of an attribute, or the name of the metric to be namespace for something else at the same time. I'm not sure if this has changed. So, yeah.
the…
Long story short here, we need to wait for this one. I think Bridon mentioned he's planning to come back on this.
We'll need to find a way to… or come to a consensus about.
how this should be modeled. And apart from this, we also have other metrics already introduced, and we will need to revisit them, but the good thing is that we don't use them already, apart from one specific
container status, I think, or container region, something like this.
In the collector.
Yeah, I think that's… any thoughts on this, or any preferences, or if you want to take some time to comment on the issue later?
**Stephen Lang** 05:51 Yeah, I'm gonna have a look at the,
the threads on there, I haven't… I haven't seen them yet.
**Jina Jain** 05:56 Yeah, but is… is the… Is this VR, like…
Is it for keeping the attribute name same as the metric?
one? Or is this something… or is it, you know, introducing a different…
**Christos Markou** 06:11 Yeah, so Pryden here suggests that the metric name is, for example, it's, yeah, for instance, example status, and then we have the attribute, called differently, example state.
**Jina Jain** 06:25 Okay.
**Christos Markou** 06:27 the thing is that for Kubernetes, we have things like, phase, and, status reason, we have more… we have extra things. So, I wonder…
If, eventually, having different… Names, will be, like.
Reasonable for us, because, for example, here, In this PR, we're introducing So, we have status phase.
It's this one, status phase, and then the attribute is also status phase.
how it could be modeled, based on what Brydon…
Suggests here, like, phase current and just gauge phase.
Yeah, so…
this one should be phase.current, and this one just phase. I'm not sure if this is allowed. So we add extra, you know, dots and suffixes.
Which might make our metrics, uglier.
Specifically for Kubernetes, because we have this, layering, status, phase, and status reason, so on.
**Jina Jain** 07:47 Yeah, this will… this will be a challenge.
I also forgot, did we decide that we'll send in… like, the…
The reason for a status, you know, explicitly by itself, instead of the reason being an attribute on the status metric itself, on what status we are in.
**Christos Markou** 08:08 I think we have… I might… yeah, I think I've forgotten. Yeah, I don't remember, like, specifically, but I think we are, preferring… we had preferred
having them differently, and I think this is also similar to what Prometheus, CubeState Metrics, does.
**Jina Jain** 08:30 Okay.
**Christos Markou** 08:31 We can… yeah, probably you can…
do this question on the PR end.
Yeah, I will also check what CubeSatMetrix does once more.
**Jina Jain** 08:45 Alright, okay, that sounds good.
Yeah, we'll just have to… I feel like if people are…
I see, like, their concern with the attribute name and the metric name being exactly the same, it gets a little confusing.
We can change it. We just have to be a little creative with the naming there.
**Christos Markou** 09:05 Yeah, I think if this, if this, approach is allowed to have the…
attribute… so, for example, cagephase here, is namespace… is the namespace of this metric. I remember
There was… well, there was a… something… I think it was a restriction or something. I have to draw here in case we can get some help from maintainers. But yeah, probably if this is allowed.
Probably we're fine.
So… But if it is not allowed, then… It will be… Tricky for us, too.
Come up with names.
Yeah, Dimitri, do you maybe… Remember, if…
This thing is allowed to have a metric named…
kh.phase.current, and have an attribute
Which is k.face, which is actually the namespace of the… Of each metric.
**Dmitrii Anoshin** 10:19 I don't remember how specifically applied to attribute names, but it's definitely not allowed across metrics, so you cannot have one metric representing a namespace of another metric.
I would assume that this rule is applicable across all of the…
conventions, but I'm not 100% sure.
Why would we need that?
**Christos Markou** 10:45 So, yeah, there is HPR from Bryden.
**Dmitrii Anoshin** 10:50 That…
**Christos Markou** 10:51 Suggest… that introduces guidance for this status,
**Dmitrii Anoshin** 10:57 type of metrics.
**Christos Markou** 10:59 And, yeah, this also, came up on this PR. Tyler had some concerns about why we're using the same name for the metric and for the attribute itself. And, Tyler shared some, technical, let's say.
Issues, when… when filter… flattened without ETL, for example, and so on.
**Dmitrii Anoshin** 11:26 But we have that already somewhere in the collector. And I don't believe we have any restrictions against that.
in semantic conventions, that attribute cannot be the same as a metric. So, if it's exactly the same, as far as I remember, it's good, but, like, representing a namespace, it's probably likely prohibited.
**Christos Markou** 11:51 Yeah, there is… There is another discussion about
There's that? I think it was from Ludmila, or… The Brydon, actually, file this issue about…
Exactly, these clarifying.
if metrics… Container and attribute sharing the same name, so…
**Dmitrii Anoshin** 12:21 Hmm, okay.
**Christos Markou** 12:22 using this example specifically. Lytmila mentioned that this is fine, and it's actually something like a feature.
That's true.
**Dmitrii Anoshin** 12:30 Okay.
**Christos Markou** 12:31 As a feature, yeah.
**Dmitrii Anoshin** 12:32 So we can reference this issue in the comment from from Tyler.
**Christos Markou** 12:40 Yeah, yeah, we need, some consensus here, and we need to, well, revive this pride, and we'll…
I'll try to push it forward, I asked him. But yeah, anyways,
And, yeah, anything else about this, or we can move to, the next one?
**Stephen Lang** 13:03 It's all good, I was just wanting to highlight the status change.
**Christos Markou** 13:11 Okay, yeah, then on the board, we have, some PRs that are waiting for review. For example, this, container porch one,
I think I already approved this one, or… Okay.
See, Gina, also.
reviewed this one. And, I also started, like, adding some extra ones about, limit and request utilization.
Yeah, if you have the time, please, take a look, and then… .
**Jina Jain** 13:52 So the CPU utilization one, actually, I was looking at it a few minutes ago, and I had a question. A port of, like, the current implementation in…
Because there is a metric which is, like, doing aggregation of
container utilization and forming that caters pod, or something like that in the… Interesting.
**Christos Markou** 14:19 collector.
**Jina Jain** 14:20 Yes. Yes.
**Christos Markou** 14:21 Yeah, yeah, we have the… I referenced the… it is already used in the collector, so I referenced the… probably I can also find the recommendation… the implementation. I think also, Stephen also asked that
Let me see, so…
**Jina Jain** 14:40 So, yeah, I was just… so, the… the latest stable version of Kubernetes.
Allows us to set pod resources now, so you get.
**Christos Markou** 14:53 Yeah.
**Jina Jain** 14:54 So I was wondering if we should hold off on defining the pod.
You know, limit request thingy, until we go see how…
When those fields are actually available, how that metric changes.
Because I don't have the current implementation in kubelet starts receiver holes, like the definition of the metric holes.
When the pod resource level stuff actually gets introduced.
**Christos Markou** 15:27 Will this change, I mean, the definition of the metric?
**Jina Jain** 15:32 Yeah, that… I don't know, because, like, I think right now we just sum it up by container.
**Christos Markou** 15:38 Yep.
**Jina Jain** 15:38 And if container doesn't have a limit or request or something, I think we don't sum that, or we…
Yeah, so I don't know if the new, Kate is, you know, Kate is allowing you to set it at pod itself somehow changes this calculation. Maybe KubeletStats will have another
Will have its own definition of how it counts it, or something? I don't know.
So I was just wondering if we should…
**Christos Markou** 16:06 Yeah, yeah, I see the point, but I wonder if there's actually…
changes the way that we define those. I mean, because now we don't specifically, mention
how this is calculated. We just say that this is the utilization against the limit of… the CPU limit of the pod. If this comes directly from the new limit that we can set on the resource.
then that's fine.
If not, and it comes… it is actually an aggregation of the subcontainers, then that's also fine. Unless we want to, like, include this, but yeah, I'm not sure if we should include this implementation detail in the…
**Stephen Lang** 16:53 The problem is, though, that you could have two different things that you would probably want represented as separate metrics.
Because… I don't know if, Gina, if you know
With the new pod level requests. Can you have both?
Container level and pod level requests? Or if you use pod level, does that mean you can't have container level requests?
**Jina Jain** 17:16 You can have both.
**Stephen Lang** 17:17 So then…
**Jina Jain** 17:19 We'll get to set the container stuff if you want to, and that takes, like, sort of, you know, higher precedence.
**Stephen Lang** 17:26 Oh, okay.
**Jina Jain** 17:27 you have, like, this fallback of setting pod level if you just cannot be bothered to figure out how to distribute your resources amongst your containers. And then, I'll have to look at the actual KAP, and what… because, like, this is, you know, at the end of the day, they'll… they'll still set something to the cgroups.
So Kubernetes probably has its own sort of, like, calculation going on when something is set at pod level, but not at container level, to be… to be sure, like, there's still some sort of fairness between, the different containers.
So, yes, my point was, though, like, what if this changes how we actually… maybe we find that now that Kubernetes has pod-level resources, we don't want to keep the old definition of these metrics around, and…
Actually have something.
direct from, KubeX Plus or something. But I'm okay.
If we feel like the meaning of the metric won't change much.
I, you know, I was going to say, though, like, we could just do a little better with, like, defining what metric
means, because, like, we've had, like, users ask us that looking at the metadata.yaml, it is very difficult to make out, like, what this metric is exactly tracking under the hood.
So maybe…
**Christos Markou** 18:48 Yeah.
Yeah, maybe we can provide additional… Let's say…
Like, description on… how these metrics should be, like, calculated. For example, we can
I guess that from implementation side, we will have something like, okay, if pod-level resource, requested limits are set, then use this directly, and then probably you can use the one that we… the calculation that we have today as a fallback.
something like this, unless we want to completely drop this and say that if there are no research requests and limits set on the pod level, then we don't emit this metric.
**Stephen Lang** 19:42 Yeah, I mean, what you might want is, for example.
The fallback method sounds great in practice.
But I would still want a way to find… say, if I was transitioning a cluster from cluster-level requests and limits to pod-level requests and limits, because it's easier to manage.
How can I tell through the metrics how many of my pods have been migrated over?
If that implementation is abstracted away, I have no way to know from the metrics if I'm using pod level or container level.
So, I'm not saying that that affects the metric design. Maybe you'd need another metric, or another attribute.
On the same metric that kind of indicates, like, where the data source is. Like, is it from container level or pod level? That could be, like, a differentiator.
For example.
**Christos Markou** 20:35 Yeah, yeah.
I see.
Yeah, I think that, we need to talk… yeah, let's think of this a bit more.
If you want to comment here directly with any suggestions or,
Yeah, I don't know, should we just block this, or…
Try to move this forward to a direction, to a specific direction? Do you think…
**Stephen Lang** 21:03 I think Gina made a good point. I think, you know, whether it affects the design or not, I think it's worth just discussing, just to see if we can take the PR as it is, or if,
We maybe need to consider another attribute, or…
Something else as part of the design with the, kind of, upcoming changes.
So, yeah, I can drop a comment on the PR.
**Christos Markou** 21:25 Yeah,
Yeah, I think eventually a metric like this, yeah, it is what it… it is what, it says. I mean…
With this new feature, should be the…
Metric coming directly from the pod.
Then probably the question is.
What about the current implementation, and what about, let's say, use cases where the… container level.
Requestion limits are used.
But yeah, yeah, maybe we need an additional one, I don't know. Okay, let's continue this offline then.
**Jina Jain** 22:10 Do you mind just splitting, like, the kdes.pod one, out from kdes.container one, so that we can at least move on, you know, with the kdes.container one while we discuss the pod?
**Dmitrii Anoshin** 22:20 Yeah, I actually wanted to suggest the same. Why do we need pod CPU request utilization at all? Like, is it really necessary?
Because it's… it's simple sum aggregation over… over container, over… simple aggregation of that metric over a pod attribute.
**Jina Jain** 22:41 Pretty good.
Okay, I think, like.
there was a user request to add it to kubelet starts. You can go take a look at the original issue.
Why they specifically wanted it, because I think we added, you know.
The sort of, like, aggregation for node and pod both.
To make it easier.
And there was, like, an issue open for Kim Blitz stats somewhere, so…
There was, like, a real argument for it.
**Christos Markou** 23:15 Yeah, I cannot really find the PR that implemented that.
But I guess I can, keep them out for now.
Just directly at them, and we can follow up, with an additional discussion about
pod limit utilization. But I guess…
now, since there is this, sort of information directly from the API, I guess we can just have this at some point.
**Dmitrii Anoshin** 23:49 At some point, yeah, once it's clarified and stabilized, maybe we can use this approach a bit.
**Christos Markou** 23:54 Yeah, and probably just drop the aggregation approach and just have the direct one, if exists.
Something like this. Yeah, that's true.
**Dmitrii Anoshin** 24:06 book, Maria.
**Christos Markou** 24:08 Yeah, cool. I will, follow up on the PR, then. Thanks.
Yeah, then…
Yeah, what else? Regarding the meta issue, I… I… I saw that, some PRs were
merged while I was off, so… what is pending here is this phase and status reason that we discussed, but it is blocked. I'm not sure about this OpenShift metrics, probably we can…
Yeah, I don't know. Adam or…
push them for later, I'm not sure. And then we have the memory metrics and the CPU metrics.
CPU, we more or less discussed about this.
We will need, at some point, to discuss the overall utilization thing.
Against the… yeah, something like a hard limb, there was a question that…
came up recently for the collector. But this is another discussion. And… for memory.
Yeah, we have a bunch of them as well.
I guess some of those are more straightforward, because we get them directly from the, stats, the KubeletStats API. Then again, we have utilization
metrics, which, will need similar discussions. Yeah, I will try to…
work on this, at least straightforward metrics for memory, and send the PR.
Unless, somebody else wants to do it earlier.
And, yeah, I think… we're close. I think probably the… the…
the goal for having them completed by November, like, align this with KubeCon, I think is still feasible.
Yeah.
I guess that's all. I don't have anything else.
Any… Any other topics, or…
Comment.
**Dmitrii Anoshin** 26:43 Nope.
Thank you, books.
**Jina Jain** 26:46 Oh.
**Christos Markou** 26:47 Thank you, man. See you in two weeks. Bye-bye. Bye.
