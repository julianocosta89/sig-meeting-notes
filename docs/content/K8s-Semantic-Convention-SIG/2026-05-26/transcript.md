SIG: K8s Semantic Convention SIG
Date: 2026-05-26
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/QfusOzofJYFn8dkvFnJAHucwBjFJ0uQZ_68Wxu1WbNj0cdTyt4mMt2NAPuFLFsHX.ViQGcMrQzyuY9Tnn
============================================================

## Zoom Recording Transcript

**João Marques Correia** 00:29 Yay.
**Stephen Lang** 00:58 Oh, seems like the last one was kind of busy, and there's, just me and you at the moment.
**João Marques Correia** 01:02 Yeah, I'm wondering.
Chris didn't say anything that he wouldn't be joining. I think he's online, so I would expect him.
Okay.
**Stephen Lang** 01:20 Bye.
**João Marques Correia** 01:21 Hey, Christus.
**Christos Markou** 01:24 Hey, hello.
Seems we don't have… Anything specific on… The agenda for today.
So, there is a… there is a PR app, or… The promotion to… of some attributes, that are… used by the cage processor of the collector, and… those have gone through the process of being promoted to Alpha, beta release candidates, and now the PR suggests those to go to stable.
And it is approved by the majority of the group, but if you folks want to approve as well, that would… Help as well, would be good.
And another issue related to the discussions that we had.
Last time is… CPU mode, someone, picked this up.
And, yeah, it's just the attribute CPU mode that is used by some of the metrics.
So, it has some approvals, If you folks want to have a look, that would be helpful as well.
And, yeah, regarding metrics, I'm not sure, we need to discuss… regarding metric stability, we need to discuss this again, because I saw that in another group, in system metrics group.
There was some… Pushback on stabilizing, staff.
And it was shared that it is fine to stabilize To promote attributes without having… Without promoting entities to the next level.
But, for metrics.
It is kind of a requirement to stabilize the entities that are related to these metrics.
So, yeah, would need to clarify, would like to proceed here.
And if we are ready to… Start promoting, for example, entities like pods, nodes, and so on.
Yeah, I don't see anything… Blocking us here.
Other than entity relationships, especially in Kubernetes.
Would need to clarify how this would be.
modeled, because everything is pretty much related to something else in Kubernetes.
So, yeah, I think.
That's an issue for us.
Do you know…
**Stephen Lang** 04:13 I know if, as soon as we've got some time, do you remember a while ago we spoke about, workloads?
And, like, non-standard workloads, because, you know we have replica set, staple set, but what about other things, like Stream Z, pod set, that kind of thing?
So, do you know… I haven't really seen any discussions around this. Do you know if there's been anything like, Talk about a generic… workload name, workload type attribute, because at the moment, it's quite difficult to aggregate when you have all, you know, K8's replica set name, K8's deployment name, K8's crum job name.
When you're just trying to aggregate for all workloads in a namespace. You have to have this huge query with all these OR statements, looking for all these individual different types of attributes.
Because they're all named differently per controller. So there's kind of, like, two… two issues I have with that. One is that it makes the queries very large.
And, the other is that, you know, it locks us into just only the official Workload controllers.
**Christos Markou** 05:19 Yeah, so I… there is… there was… there is an issue, actually, for this. Okay. That was discussed a while ago.
And… Yeah, it's… if I remember correctly, we said that we are fine to proceed with what we have now.
And… We just… in order to cover… so this would not solve the, the issue with the query, how extensive a query should be.
But for custom workloads, the idea is to, provide guidance in order to, Be able to potentially implement additional workload types, implementations or whatever, but following a specific guidance that, Simad Convention could provide, without necessarily having them, maybe, as part of Simad Convention or whatever.
**Stephen Lang** 06:18 And that'd make the queries even longer, right? And for every type that was created.
you'd have to have another, like, OR statement on the query for picking these kinds of unique attributes.
**Christos Markou** 06:30 Yeah.
**Stephen Lang** 06:32 So maybe, maybe, like, additional… Attributes, as well, might help to… for… grouping, or I don't know if this would be anything to do with the Entities in some way, to group, somehow generically, workloads to namespaces, for example.
Other than, you know, just at the lower level via a pod.
But just to have, like, groupings of… pods together.
**Christos Markou** 07:00 Yeah, I guess… Good need to maybe… have a specific… have some specific use cases to, try to see how… Mainly.
**Stephen Lang** 07:12 mainly the querying, right? Just… it's one thing to have all these entities in there, but then the resulting query just becomes, not unmanageable, but it's, It's a lot bigger than it could be.
**Christos Markou** 07:25 Yeah, I remember us, seeing some, like, decent vitalization, like, unifying… So, would… would the suggestion be, the alternative would be to have like, a generic… Representation of the workloads, entities, whatever.
**Stephen Lang** 07:49 So…
**Christos Markou** 07:49 be resource UID, resource name, resource type.
**Stephen Lang** 07:54 Something… something like that, or that could be in addition to, like, the custom vendor-specific controller attributes as well.
**Christos Markou** 08:02 Just…
**Stephen Lang** 08:02 I mean, you could have… you could have both, so that one is… Kind of more geared toward general aggregation, whereas the other is more specific to, like, if they need more attributes on a vendor controller.
workload type than you would for standard workloads. But the analogy that I'm taking is over from Prometheus, where there's recording rules.
Around the K8's odd owner.
And we create two labels, which is, workload.
and workload type, which represent the workload name, and then the type of the workload. And that makes it super easy just to look at, say.
Show me all, like, the maximum number of types in this cluster, or across many clusters. Or just list me all the workloads in my fleet.
Without having to enumerate all the individual pods, which at scale, enumerating pods is very expensive. And enumerating namespaces is not enough detail, so you want to drop down a level and enumerate workloads.
And this is what gets very difficult if you don't have the, The generic attributes, just to capture the name and the type of workloads.
So that's… that's the main use case that I'm trying to… is really listing at scale.
without… Having to invoke all individual pods.
**Christos Markou** 09:22 Yeah, if it can be additive on top of what we have today, that would be easy way, I guess.
To achieve this, because, like, changing what we have now, would be, like, major… shift, major braking change. But if we can achieve this flexibility or convenience with just adding some additional descriptive attributes, for example.
I guess that should be fine, and I think we should be… able to add them later, at some point, if we want. If they are descriptive and optional, I guess we should be allowed to do it.
But yeah, feel free. I think, yeah, writing this down on the issue, would help, so…
**Stephen Lang** 10:11 I can do.
**Christos Markou** 10:11 I'll share something there.
So we can maybe get to it at some point.
**Stephen Lang** 10:18 I'll do that, thanks.
So you're saying that it wouldn't be breaking in terms of if the attributes that we were looking at, or the entities, were stabilized? It's okay to add new ones in future, because it's not breaking. Is that what you're saying?
**Christos Markou** 10:33 That's my assumption. Maybe Dimitri, can correct me here, but if some… if… We want to add additional descriptive attributes in the future, and… Have them also, also as optional.
I guess we should be fine to do it, right?
**Dmitrii Anoshin** 10:49 Yeah, it's not a problem at all.
**Stephen Lang** 10:52 Great, cool. I'll add some detail to the issue, thank you.
**Christos Markou** 11:01 Okay, I see some items, okay, it's mostly what we discussed.
**Stephen Lang** 11:07 I just captured the links from the chat to you.
**Christos Markou** 11:11 Thank you. Okay, cool. Yeah, I don't have anything else to mention, anything… from anybody.
Okay, I guess, we can keep it short today, then.
**Stephen Lang** 11:35 Thank you.
**Christos Markou** 11:36 Thank you, folks. See you.
**João Marques Correia** 11:37 Thank you.
