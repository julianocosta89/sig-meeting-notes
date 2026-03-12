SIG: K8s Semantic Convention SIG
Date: 2026-02-03
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 02:18 Hello?
**Jina** 02:26 Hey, folks.
**Dmitrii Anoshin** 03:04 Hi, everyone.
**Christos Markou** 03:09 Hello?
**Dmitrii Anoshin** 03:32 Joe Stop?
**Christos Markou** 03:35 Yep, let's it, let me share my screen.
Have added, two topics for today. So, one is the… the request for… from Ludmila and the… the semant convention maintainers.
About our suggestion for the roadmap for this group.
And I put here an idea of what we realistically expect to do.
this year. So I think the main focus would be to work on stabilizing the Kubernetes and container attributes in alignment with the work that is happening in the collector, components, respectively, and specifically the KH attributes processor.
And then, if we have time, I suggest that we will… Yeah, so this is the phase one of the plan. This is what we discussed, actually, during KubeCon in November. Gina over there, Stefan, you were there. David was also there. And then, next, we'll be focusing on the metrics. So… Then, if we have time, we can start picking up issues from the metric side.
Any… Concerns, comments on this, or we can consider it as… Like, our final proposal?
From this group.
**Dmitrii Anoshin** 05:08 That may, like, seems reasonable to me.
Thank you.
**Christos Markou** 05:14 Okay, I think it's just, like, an estimation. If we want to change it later, yeah, nobody will complain, I guess.
Cool. And, yeah, another one… this is already approved by multiple people, but just an FYI.
I sent the PR to change the stability from alpha to beta, from specific… Attributes.
Yeah, and there was a question from Josh yesterday, if we should move entities as well, but I remember, Dimitri, we discussed that a while ago, that we can for now keep entities out, because In any case, we're not going to use them in the component like, really soon, right? So, we should not block the work there, based on what is coming on entities, and if there is anything that is blocking there or not, right?
**Dmitrii Anoshin** 06:14 If there's anything blocking there. I'm not really aware of anything, but I would, agree that we can leave it out. It's just, It's just, like, I wouldn't… Make it slowing down the work on the entities, which is… Like, probably mostly on my plate, and… Yeah, yeah. So, if I… yeah, if I… if it's… that's okay, I… I can, I would like to… keep it separate, but… I… would like to get some help on the reviews. I know, like, I'm not the best on the reviews from my side either, but if I can give… have some… If I prepare more PRs towards entity work on the collector in general.
And, I would appreciate reviews on those, so we, like.
So we can continue working on that quickly enough. Not like… my point is that it's okay to leave it aside, but I don't want to.
**Christos Markou** 07:21 Yeah, yeah, sure.
**Dmitrii Anoshin** 07:22 So that it's slow, slow, slowing down.
**Christos Markou** 07:24 Yeah, yeah, yeah, yeah, totally, get this. Also the point is that the Kubernetes Attributes Processor, does not really use entities right now. So… like, technically, to, like, move forward with this.
**Dmitrii Anoshin** 07:40 We only need the SMAT conventions from the registry directly.
**Christos Markou** 07:44 So that's the point.
I agree, if we want to, like, catch up with entities, we can do it, but right now, it doesn't seem to be, like, a requirement for the component to proceed towards stability.
**Dmitrii Anoshin** 07:58 In the following months. I agree.
**Christos Markou** 08:00 Yeah, if you have prayers, yeah, feel free to send them over.
**Dmitrii Anoshin** 08:04 And maybe, like, Kubernetes Attributes Processor, the name itself would be not ideal for the… when it's, like, completely gonna be moved to the entities, right? Potentially, we might consider introducing, like, another one, I don't know, some kind of Kubernetes… I don't know…
**Christos Markou** 08:22 Yeah, naming is hard.
**Dmitrii Anoshin** 08:24 Enrichment or something, I don't know, but yeah.
**Christos Markou** 08:27 Yeah, yeah.
By the way, I think it's not like… totally related to this, like, some unconvention-specific work, but in general, there are, like, there is some progress there in… regarding this component, so… if you are interested, or… yeah, Dimitri, you are also a co-donor, so, yeah, if you can find some time to… have a look into the PRs there, that would be great. Specifically, there is…
**Dmitrii Anoshin** 09:03 this PR, or something else as well.
**Christos Markou** 09:06 No, for example, there are, Yeah, I can send them, or I should send them.
I can send them to you later, but in particular, there is one trying to improve the performance of the metadata that we are caching, and the other one is the feature gates PR that adds the feature gates, and someone from Dynatrace is working on those, and, yeah, it would be nice to have them in.
**Dmitrii Anoshin** 09:36 I'm struggling to keep up with, like, the notifications, but I definitely have time this week, today, and tomorrow, and I'll look into this. If you can send me, that would be perfect.
**Christos Markou** 09:47 Yeah, I will send you these two PRs, which are more important on my mind. The good thing is that this component does not face the same issues that the host metrics receiver face, because we don't use mdatogen to Generate configurations and everything right now, so we can do the feature gate transition easier.
We don't mesh with M. DataGen and stuff.
**Dmitrii Anoshin** 10:14 Okay, and that one is Kubernetes Attributes Processor, I guess.
**Christos Markou** 10:18 The processor, yeah.
**Dmitrii Anoshin** 10:19 Yeah, makes sense.
**Christos Markou** 10:20 So it's mostly trivial. Okay, sounds good. I'll send you the,
**Dmitrii Anoshin** 10:26 Thank you.
**Christos Markou** 10:28 the links later.
Yeah, I don't know, anything else? That's all I had. Anything on the agenda?
**Dmitrii Anoshin** 10:36 Jenna, do you want to bring your PRs?
**Jina** 10:39 What's, Crystals, can you click on those?
One is for… both have, like, new entities overall for Kubernetes, and they also have metrics.
Actually, this conversation about entity brought something to mind. I have been defining… the new attributes I'm adding, which… Can either go in as a resource attribute, or can be a descriptive entity.
attribute to both the registry and entities, cause, like.
I don't know if people would want those to move, to the resource attributes, you know.
thing. But… I don't know. Does it matter? If it matters, I guess. You folks can comment.
**Dmitrii Anoshin** 11:31 Yeah, right now, when we don't have, like, events except for Kubernetes cluster receiver experimental events, we typically don't distinguish descriptive attributes from resource attributes. I mean, they can be both, essentially.
**Jina** 11:48 Okay, because I've been just, like, interchangeably adding them in both places, but for implementation, I sometimes make a call that the label or annotation, for example, goes into metadata, because we don't have a way to disable those string type… template string type thing.
For the service thing, though, I can go over if, like, there are any questions, and… also, like, I do have more follow-up things coming in. Those will be for entities only, which is why, I guess.
I just want to make sure, like, There are no issues with.
Oh.
**Christos Markou** 12:31 See, Sean, yeah, I had a look today, mostly, looks fine. I only had the question about the stability. Do we have experimental in semant conventions?
**Jina** 12:46 So, I think they used to be experimental, but the large majority is, like, development. I'll change this to development.
**Christos Markou** 12:55 Okay.
I think this one should be good to go, mostly. We'll have another look and approve, maybe.
**Jina** 13:03 If anybody has, like, any opinion on the zone thing, because, like, I'm still… Not sure. On the other hand, I was thinking, like.
zone might be something which shows up in other Kubernetes objects later on.
So, the caterers.service, That endpoint might become more specific, and maybe we can do something generic.
**Dmitrii Anoshin** 13:29 But, Gina, will that be… that zone be essentially the same thing, if it ends up…
**Jina** 13:36 It's always the caters. The topology.katers.io slash zone label on the node.
**Dmitrii Anoshin** 13:44 And Kubernetes only populates to that and to all the other objects.
Wow.
**Jina** 13:49 So, yeah, my suggestion was, I think, like, something ks.topology.zone, if you don't want to use cloud.
**Dmitrii Anoshin** 13:57 In that case, we don't need to bring topology as an entity, because the thing is, we should distinguish between descriptive attributes that can be applied to anything.
and and entity descriptive… descriptive attribute of specific entity. If topology… there is no such thing as a topology as an entity, we should… we can… we can bring it as a descriptive attribute. But if there will be topology as an entity itself.
We shouldn't add anything, we can just add the relationship, essentially, to the topology as an entity.
**Jina** 14:33 I mean, we can add topology as an entity then, because, like, region is also technically topology.kls.io slash region, which is also just a label. This is for bare metal clusters, where… a region might be, like, two different data centers or something, and not a cloud provider region, explicitly. So, I don't know. Or we can keep it this way, if it's okay.
**Dmitrii Anoshin** 14:56 But at the same time, in any, like, another lead, like, test for whether it's an entity or not, can we have telemetry associated with an entity? Like, specifically, let's say, telemetry associated with topology. I don't think so. Topology potentially can be just… It can be just, like, some descriptive… set of descriptive attributes in that case.
Does make sense?
**Jina** 15:24 Oh.
Sure. So, hold on, are you, are you for adding KSD Apology as an entity by.
**Dmitrii Anoshin** 15:31 I'm just, like, not… I'm… I'm good with either. I'm just trying to figure out whether the topology itself can be represented as an entity, and if it looks like it cannot.
**Jina** 15:44 There is no… yeah, there is no identifying thing. It's just like the script, I guess.
**Dmitrii Anoshin** 15:50 Right, in that case, it can be descriptive. And it's also fine to keep them separate, like, peer, Even if they potentially can have the same name, like, I mean, if they potentially can be the same between, like, one topology applied to, let's say, port, one topology applied to endpoint.
It's fine to have Separate.
keys.
**Jina** 16:19 Okay.
**Dmitrii Anoshin** 16:19 When we have kits.service.endpoint.zone, it will be no conflicts.
with other entities. But if we say it's topology.zone, potentially it can… it can conflict with something else if there are several entities associated with the same telemetry.
**Jina** 16:39 Hmm.
**Dmitrii Anoshin** 16:40 Yeah, I had a similar question on the persistent volume one, though.
**Jina** 16:44 Got, I… I'm trying to add, The namespace of a different object of the volume claim on metrics coming from persistent volume.
Right? For now, I have described it as caters.namespace.name in that metric attribute, but, like, it is technically not the namespace name of the persistent volume. It's… persistent volume is cluster-scoped.
So it doesn't have a namespace. But then, like, if I don't use this, I'll be putting in another, you know, attribute, like caters.persistentVolume.namespace, just to make that distinction.
So it's getting a little hairy.
**Dmitrii Anoshin** 17:31 Yes, in that case, if there are some potential conflicts, it's better to be precise and, like, add, like, specific descriptive attribute for a specific entity, essentially, so it doesn't conflict with others.
**Christos Markou** 17:44 Would that be, like, answered if we answered this issue, this open question about… how entities are correlated to each other. So, if a metric is about persistent volume that is also related to a pod that belongs to namespace.
the metric is related to a pod entity, but also to a persistent volume entity at the same time. So, you don't need to attach, like, the namespace name to the persistent volume directly, right?
**Jina** 18:20 Yes, but… That relationship does not exist in its current form right now in entities, right?
I don't know if the… like, the data model doesn't really have any real way Any backends actually understand of…
**Dmitrii Anoshin** 18:39 relationships. I know that…
**Jina** 18:42 Put in, like, an association in the semantic conventions, but that doesn't help in the real telemetry.
That's the issue, I think.
**Dmitrii Anoshin** 18:50 So, in the real telemetry, every day, every, Let's say every metric can be associated with several entities.
But there is supposed to be only one which is, like, let's say, the main entity for that particular… telemetry, and this is what we define in the semantic conventions. So, every entity has a set of metrics.
But when you emit those metrics, you can also attach other entities on top of that if needed. So, for example, we have pod, right? We have KATS pod, and we have, let's say, kits.pod.phrase, or, like, which is not an ideal metric example, but anyway, we have that metric.
And we have Kubernetes pod associated with that.
So, it's like, that metric is part of the… associated with the pod entity, but when we emit it, we can attach other entities on top of that, so in that case, we don't need relationships for now. We can attach KTS namespace as an entity, KTS cluster as an entity.
And that's pretty much it, I guess. Those three entities will be essentially a part of the resource. They will get… they will give users all of the attributes from those… from those entities, the resource attributes, for backward compatibility. That… that's how we currently do it.
Does make sense?
**Jina** 20:22 Is that an example? Because right now, if we do it in just what is implemented, just cluster receiver, the only thing I can do is send stuff as a resource attribute or a data point attribute on the metric.
**Dmitrii Anoshin** 20:37 No, Gina, it's, it's, like, you are probably missing that another part when, like, resource association with an entity, it's there already. It's just not implemented yet, in the collector, but the semantic convention is pretty well stabilized for that part.
And, I think… I'm gonna maybe…
**Jina** 21:02 So, like, it's… it's… it's a concept, as a concept, it's well-defined as a specification, it's well-defined.
Which is…
**Dmitrii Anoshin** 21:10 Cool.
**Jina** 21:11 You'll be able to attach, like, these multiple entities into the.
**Dmitrii Anoshin** 21:15 Right, right, right, right.
But we currently do it in, like, let's say, backward-compatible way. We attached them as resource attribute for now, but… they also need to be entities added to those resource attributes that point to existing resource attributes. So every entity with just a reference to existing resource attribute, and the resource would be pretty much the same for backward compatibility, but it'll give a more idea about, let's say, KATS, that name… that namespace, that name would be part of this entity, so it will add more associations with the entity inside the resource itself.
Does that make sense?
**Jina** 22:02 Like, theoretically, it makes sense, I'd have to see the thing, actually.
**Dmitrii Anoshin** 22:08 Yeah, in MDataGen, I have an issue. I'm gonna, probably prioritize the work this week and that, and so it's, like, it's, it's more…
**Jina** 22:21 I go.
**Dmitrii Anoshin** 22:22 It's, it's important to implementation as well, essentially.
**Jina** 22:26 Okay. Yeah, I mean, that would be great, cause, like.
That… that would at least help with the… all the relationships.
**Dmitrii Anoshin** 22:35 Yeah, yeah. So it'll be implicit relationship was set right on the, on the telemetry itself. But later on, we'll get, like, broader relationship defined as, let's say, like… specific types of relationships. Run zone, part zone, contains, and whatever.
**Jina** 22:58 Oh.
Yeah, that's… that's what I had.
**Dmitrii Anoshin** 23:05 And then, by the way, Christos, once we approve the PR for, let's say, service, we already can, merge, I guess, the PR in the… collector, right?
**Christos Markou** 23:20 Yeah, I think we're allowed to, like, do development, additions, so yeah, this would be fun.
**Dmitrii Anoshin** 23:28 And it's just not related to this one, but, like, some other, like, force metrics receiver, for example, we're also gonna stabilize it.
you're more involved into the semantic conventions in general, so the question is that if someone wants to add new metric, the guideline is that they submit a PR against semantic conventions, and at least have it, like, looked at, approved, and only in that case, we can, like, start adding them in the collector, right? Or it can be done without semantic conventions, too.
**Christos Markou** 23:57 That is the suggestion. There is a, like, an added, guideline in Collector.
**Dmitrii Anoshin** 24:06 In contrary band core.
**Christos Markou** 24:08 that co-donors should suggest or prefer this way whenever it is applicable. So, for example, for host metrics receiver.
This should be the suggestion, at least. But it's on the discretion of, it's, like, up to the code donors to decide if they want to approve something without having the semantic conventions.
So, yeah, you can also, like, file something as a draft in Collector, for example, to illustrate the idea, work towards the SMAT conventions, and once code owners feel, you know, confident enough, they can merge So, either both, or one after the other. So it's not a hard guideline, it's, like, mostly a suggestion.
**Dmitrii Anoshin** 24:52 Yeah, that's how I, how I envisioned, I think.
**Christos Markou** 25:00 Alright, seems that's all that we had for today, right?
**Stephen Lang** 25:05 I have a question, I know we've only got a couple of minutes.
As soon as there's nothing else.
**Christos Markou** 25:10 Yeah.
**Stephen Lang** 25:11 So I'm just wondering about, metrics for really large busters. So, you know, many thousands.
of pods.
traditionally on, like, CubeState metrics and things, we've had to use recording rules to reduce the cardinality of the queries, so that the queries can respond in a reasonable timeframe. Because if you imagine you've got so many active series for such a huge number of pods.
So, I'm wondering, what would be the approach in the hotel world for, like, around the semantic conventions, because I'm just looking through, and I don't see anything that rolls up the, for example, the CPU usage across an entire namespace, or, like, across all, replicas of a deployment, or across an entire cluster.
I don't know if this has been approached before, so my question is, is there any prior art for discussing conventions around recording rules?
Or would this be something like.
Maybe a new metric that would be introduced that would roll up the total CPU usage for an entire namespace, for example.
**Dmitrii Anoshin** 26:16 So you want to do the reaggregation on the client side, essentially? That's the question?
**Stephen Lang** 26:21 Well, yeah, so I guess with, with a metric, it would be done on the client, because it would try and calculate and roll up everything, and export it.
But the other side, if it was a recording, will it be done on the server?
**Dmitrii Anoshin** 26:35 In addition to the more granular metrics, or you want to remove them?
**Stephen Lang** 26:38 addition.
**Dmitrii Anoshin** 26:39 Okay.
I don't think we have anything… any semantic conversions like that, and I'm not sure we even need to do that. But you already can do it with the collector, you can, I guess, as far as I remember, metrics… Transfer processor allows you to do that reaggregation, potentially, but I'm not sure. And in that case, you can just name it however you want.
**Jina** 27:05 CPU case, Steven, like, you can do these stuff which come from Kata's cluster receiver in its current form right now, with the transform processor, I suppose, but how would you do it with metrics from kubelets? That's right. They're all on local node.
**Stephen Lang** 27:20 Yep.
**Jina** 27:21 So, you don't even have that entire namespaces metric or anything, like the view.
So… That'll be difficult.
**Stephen Lang** 27:33 So there's nothing that takes into account semantic conventions around recording rules or anything like that, that would be doing, like, server-side processing, so that you could look across many receivers, for example, to aggregate the data.
**Dmitrii Anoshin** 27:47 I don't know.
That's typically, anyway, would be the back-end territory, where you would… If you want to add some additional pre-reaggregation, or let's, like, ingest, ingest that.
Potentially, that… yeah. I don't think… We need to define semantic convention for something that's supposed to be back-end.
**neil yashinsky** 28:11 Okay.
Yeah, I will say, interesting, points. Hello, everyone. My name's Neil. I think this is the first time I've been here, so I really just want to em and fly on the wall mode, or what have you, for the most part, but anytime anyone asks a question that I might be able to help with, honor bound to chime up, even if I sometimes look slowly in the process. But, Steven, I think your question, is… is conceptually very relevant to some of the work that I'm doing on, because it is about aggregating, and underst… you know, basically, extrapolating more context from our metrics to allow better insights into… you know, operational… whatever, quality monitoring, etc. So I… great question. I haven't just back to your original question, I haven't seen any prior art around in any of the other hotel groups that I've been working in.
But, would be happy to chat with you a little bit more if anything that I said sounded at all interesting, because what I'm working on is a concept called business observability, and that is basically a job is to bring more context to the, you know, using custom resource definitions to the Kubernetes you know, workspace. And so, when Gino mentioned that one part, about, like, maybe not having all the inputs needed to do the aggregation properly, that was when my dog ears perked up.
**Stephen Lang** 29:35 Okay, well, I suggest, because we're out of time, I'll create a thread, and Neil, if you're on, on Slack, you know, we can, we can chat there.
**neil yashinsky** 29:43 Oh, that'd be great, yeah, awesome, thanks.
**Christos Markou** 29:45 I just shared another link in case. We had something… somehow similar discussions for the host CPU, introducing opinionated metrics. We also had an approach to do this on the collector, as Dimitri mentioned. Maybe you can have a look there as well. But I think we ended up deciding that As a group, we didn't like to, like.
define conventions about opinionated metrics, about, you know, aggregated stuff, and… because you can go down the path of having lots of arguments why to do this in this way or the other way, so it gets complicated. That was the story there.
**Stephen Lang** 30:26 That's all good. Thank you for the discussion, I just didn't want to do this in isolation.
**Christos Markou** 30:30 Cool.
Smart. See you.
**Dmitrii Anoshin** 30:33 Two weeks in. Thank you, guys. Bye-bye.
