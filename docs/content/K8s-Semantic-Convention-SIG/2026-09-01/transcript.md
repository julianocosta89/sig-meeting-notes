SIG: K8s Semantic Convention SIG
Date: 2026-09-01
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang (Raintank, Inc. – Grafana Labs)** 00:55 Hi, Chris.
**Christos Markou** 00:59 Nope.
**David Ashpole (Google LLC)** 01:44 8.
**Christos Markou** 01:49 Hello.
Yeah, I guess we can start. I… have added a few… Links there.
There are two PRs that I have sent to promote.
some metrics through a list candidate. One is for the page fault metrics, and the other one is for the… File system metrics.
I… Found an issue very… quite recent one from Tyler, suggesting that Suggesting to rename the file system metrics to align with the system namespace metrics.report.
The respective file system metrics, and… I saw the conversation there, Jina raised the concerns that we should follow the gates.
the Kubernetes API, more specifically, and… stick with the Kubernetes namespaces and container namespaces, so… which is something that I agree. So, yeah, we can wait for Tyler to… Verify this, and otherwise we can… Proceed with the promotion.
of these metrics. And in the last two links that I have added, I was checking what is coming next, and I think… Next thing is the… metrics around… Pod limits, requests, and the utilization metrics that we defined there.
for containers, for containers, Kubernetes containers, we already have their respective metrics. There were some things missing from upstream Kubernetes.
That I think now are covered with the latest release, 137, that happened, that was released this week, or a few days ago.
And, I'm preparing something, I will share it once I have it.
And I also shared some thoughts on CPU metrics in general.
I think… There is a… I think for utilization metrics.
I would be… I think there is no open question there. We can define utilization against… limits and requests, since we already have these metrics in use. I think there is some… There is an open question if we want to actually… keep… The utilization metrics against the node limits.
And… I would lean towards maybe deprecating them in the kubeletScharts receiver directly.
Main reason is that… is one extra thing to maintain.
and also… I think we would struggle to define it, because, it's… it's hard to define… to, like, come up with a limit of the node, because the node reports the capacity and also the allocatable CPU.
So… yeah, in theory, we could have two different metrics, two different utilizations, or we could come up with a specific one that takes the… either the allocatable or the full capacity.
But then, what if someone needs something else? So, it's a bit, like, weird metric. I know that I… asked to introduce it in the past in the receiver, but… yeah.
I… tend to believe that we don't need it anymore, but I would be open for feedback on this, either now or on the issue directly.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:41 Sorry, go ahead, Tony.
**David Ashpole (Google LLC)** 06:43 Okay, sure, I'll go ahead, and then you can go. Like… Would we then have… utilization metrics for, like, some things, but not others. Like, we would have them still for pod, right?
But we just wouldn't have them for Node anymore?
**Christos Markou** 06:57 Yes, for pod, you can define the utilization against the limit or the request. We have this today in the receiver, and it's quite straightforward, more or less. Defining a utilization ratio against and against what the node can provide, is what I'm suggesting to be removed. So, if the node has, like, 8 cores, for example, and the pod consumes 1 core, then we have one 1 as a ratio against 8.
That is the number that… that is the metric, actually, that I'm suggesting to… to be removed, because, Yeah.
It doesn't make a lot of sense.
When it comes to scheduling workloads and stuff like that. And also, node limit is something, like, controversial to define, if you should use allocatable or…
**David Ashpole (Google LLC)** 07:58 You would use capacity. Like, if you're reporting the total… there's two things we should compare against, right? One is the… Usage of everything on the node.
Compared to the node's capacity, right? Including the cubelet, and the kernel, and whatever.
And the second thing we should be comparing against is… Be it usage of pods.
Of the sum of all pods against… The allocatable of the node.
Because that's how the cgroups are structured, right? Inside the allocatable cgroup is where all the pods live.
the allocatable amount is enforced against that C group by the kubelet.
And the qubit also does memory eviction by comparing The total pod memory usage against the allocatable of the node.
So there's… there's actually, like, two different comparisons we could make, but if we're gonna do utilization of the node itself, like, meaning just, like, we took the… CPU number from the root C group or something.
Then we should do it against the capacity.
**Christos Markou** 09:06 Okay, so… Okay, so we can split the discussion, maybe, talk about node utilization and pod utilization.
So… yeah, maybe those are two different topics. I was mainly referring to the pod utilization.
against… Something that the node defines.
**David Ashpole (Google LLC)** 09:31 Yeah, we should only… if we're talking about… right, so if we're talking about the sum of all pods.
Then that should be compared against allocatable as a utilization number.
**Christos Markou** 09:44 Okay.
The question is, do we want this metric per pod, or if we can just…
**David Ashpole (Google LLC)** 09:51 per pond?
I would expect there to be a single metric for the node.
**Christos Markou** 09:57 So the question… we have already the implementation per pod, so we get the usage of the pod, and we divide this, by node, Allocatable, or capacity in the receiver.
**David Ashpole (Google LLC)** 10:13 Yeah, that doesn't make any sense to me.
Okay.
**Christos Markou** 10:20 So…
**David Ashpole (Google LLC)** 10:21 I'm happy to get rid of it, then. Yeah.
**Christos Markou** 10:23 Yeah.
**Jina Jain** 10:24 Okay, why only caters border then? The caters container CPU, you know, utilization, firstly, is just too confusing.
I think even that seems redundant.
this is calculatable, right? Because we expose capacity and allocatable of the node as individuals.
**Christos Markou** 10:43 Okay.
So… Container node utilization, is the name in the receiver. We can suggest this for deprecation, I guess, and pod node utilization is the other metric.
that we discuss. We can also suggest this for deprecation, if we agree. And one open question is if we want to have a metric for node utilization, like, in general.
Yeah, we can discuss this. Actually, we don't have a metric right now like this. We had this metric in the receiver, but it was deprecated, because it was derived by usage, so we did this rename. So, essentially, right now, we have no metric, so it's a new thing. We can, like.
Leave it for… for later, probably.
Okay, in that case.
I could suggest those for deprecation in the receiver directly, and we just get rid of them if we have no objections, after a while.
And then we just need to cover the, utilization metrics against… for pods against the, against the limits and the requests.
Which is quite… more straightforward, at least. Okay.
I guess with those, we close the gap, at least for the Kubelet SATS receiver, and another thing pending is volume, volume-related metrics.
That could be… a bit weird, a bit… tricky, if I remember correctly, because we also relate these metrics to… Persistent volume.
Claims, if those exist.
And… Yeah, maybe… The… the modeling mechanism that we have today will make it tricky.
Anyways, we can discuss it when… We are… when we have something more concrete.
Yeah, other than this, I would suggest, I mean, in… like, if we have these metrics defined, or even promoted in list candidates, we can… I could send the PR in the kubelet SAT receiver and use the feature gates to introduce the the migration. We'll leave them there behind the feature gates, for, like.
we can decide. There is Norras, I guess, and… Yeah, so the Kubelet SAT receiver will be more or less, like, We'll start the migration.
So, yeah, I guess that's a good thing, realizing that we have… covered this gap so far. It's nice.
Yeah, that's all I had, actually, looking into the backlog.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 13:40 Yeah, so before, I was just going to just effectively agree just on the deprecation side, and also I was going to add another dimension which could be confusing on the node utilization side, which is what, if you look at the The sum of all pod usage versus the sum of all pod limits on a node.
Because if I see, like, node utilization, that would be, like, another question that I'd be asking, so I think… If you were going to have a node utilization metric, it shouldn't just be one metric, because it is too… Ambigious as to what it could be, so it sounds like you'd need at least two utilization metrics.
Just to be… You know, absolutely clear as what it is the utilization is measured against, whether it's capacity or allocatable, or it's the sum of hard limits on the node.
The other thing I was wondering is, you mentioned volumes.
Do… what about, like, system disks as well?
**Christos Markou** 14:40 So, the metrics that I was referring are essentially the metrics that we define today, the receiver.
and… Those are actually… In the QBlit stats receiver, those are actually coming directly from the Kubeless Stats API.
The tricky part that I was referring to is that, in the implementation, in the receiver, we check if the volume is Persistent volume, or… something like that, and then we try to fetch the additional details about the names of the persistent volume claim and so on. So, I was a bit worried if we can define this Let's say, relationships today or not.
But I don't remember all the details right now. I roughly checked this a while ago.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:40 Okay, yeah, because there's some edge cases where you have, like, a… You know, local path volume mount against a system disk.
Which… Kind of depends if you're thinking about it in terms of the node.
Or in terms of the persistent volumes.
Like, it depends where the storage pool is coming from.
**Christos Markou** 16:00 Yeah, okay. I think, yeah, I'm not sure if that would be an issue. The metric itself, it would be… if that would be an issue for the metric itself, since we are getting this directly from… Quibleta as human.
This should be fine, but we can double-check this.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:19 Yeah, I think it's a gap in, at least CubeState metrics already, I think.
And possibly…
**Christos Markou** 16:27 Okay, okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:28 the advisor.
I think there's, in some cases, not able to differentiate between The full capacity of the node disk.
And the slice of which you've allocated to a local path volume mount.
But yeah, I mean, if, If an issue comes up, I'm happy to, sort of look into it as well.
Just because what happens is you see, like, the entire disk capacity, say it could be a terabyte, and then you chop it up into several volumes and allocate it to a few pods.
And so you just want to allocate 1GB per pod or something.
But every pod reports that local volume as 1TB, because they all see the local disk.
That's what I've seen in the… some of the Prometheus exporters.
So I wondered if perhaps the same would be occurring.
With the hotel receivers as well.
**Jina Jain** 17:26 Oh, you mean if you look at a mount path, a mount point of a secret or something, it shows up as the actual… You know, the full temporary disk on which the container runs.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:39 Yeah.
**Jina Jain** 17:41 Okay, yep.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:42 Yeah, or if you're mounting some local path from the node.
into a pod. Sometimes it sees the entire disk.
Physical disk capacity instead of… What you've allocated to.
**Christos Markou** 17:58 By the way, these are the metrics that I was talking about.
I'm not sure if we can or if we should handle this.
What you're describing, since we're, like.
deriving these metrics from the Kubelet starts API, if the implementation there is, like, not 100% accurate, or there's something missing, I'm not sure what… if we can do anything about this.
Maybe we could, but… yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:36 So in this case, I think it would affect the local volume type.
But, I mean, that… that could just be… A bug, maybe raised, or…
**Christos Markou** 18:51 Yeah, don't know. David, do you have any… Like… Feed any information?
Around this.
**David Ashpole (Google LLC)** 19:01 Sorry, I was looking at something else.
**Christos Markou** 19:05 the pod volume metrics that, are exposed from the Summary Stats API.
**David Ashpole (Google LLC)** 19:14 They should be… They should be accurate for… I think some of them come from the CNI implementation.
And others come from, the kubelet itself, doing calculations on, like, empty dirs and local stuff.
Are you asking whether we should use them at all?
We definitely… It would be hard to reconstruct volumetrics without going through the qubit, because… Of all the plugin interfaces.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 19:54 I guess I was just wondering if, what I've seen before with the local volumes where the capacity of the volume is shown to be the total capacity of the underlying disk, as opposed to the allocated amount. I just wondered if that same issue would be present.
**David Ashpole (Google LLC)** 20:12 What do you mean?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 20:12 receivers.
**David Ashpole (Google LLC)** 20:13 What do you mean by the allocated amount?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 20:16 So… I can't remember the use case exactly, but this was when you, instead of using a, like, block device that's been allocated from a cloud provider to provision a volume on demand for your PVC. Yep. You could instead provision some part of the node's, you know, boot disk, for example.
**David Ashpole (Google LLC)** 20:38 Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 20:40 And when, when you do that through the metrics for a local volume, it would appear that the capacity of that volume is always the capacity of the underlying disk. So if you…
**David Ashpole (Google LLC)** 20:52 Is the size of that thing actually limited, though? Because… If it's, like, an empty dirt or something, then it… you can keep writing till you fill up the disk, right?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 21:03 So… I don't know if you can… can you bind a PVC against a… a local disk, like that, because then if the PVC only requests, say, 1 gig.
But then you assign it a volume that could potentially be a terabyte.
Than the capacity on that volume, from the pod's perspective.
Even though it's only requested a gig, it's still gonna see the 1TB.
**Jina Jain** 21:31 That is on the volume provisional.
you know.
Kubernetes really doesn't do much, it's the volume provisional, actually.
Making it available.
So if the volume provisioner cannot actually you know, create a volume for 1GB.
And this is actually seen, and I think we have metrics for this also, because it is possible that the volume provisioner is set to provide, like, best effort, so it could give 5GB for a 1GB ask.
But, again, I think this is not a cubelet concern.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 22:11 Okay.
Yeah, I was just wondering how the edge case would be handled, because seeing as we were talking about utilization and, you know, the node perspective of CPU usage before.
I kind of wondered if there was any overlap.
With… You know, on the storage side, because if you think about a volume utilization metric for, you know, a PVC of 1GB, but the underlying disk is 1TB. The utilization numbers, in terms of the amount of space that's been used, could be Unexpected.
**David Ashpole (Google LLC)** 22:45 So, according to… The internet.
the spec.storage… spec.capacity.storage on a local PV is just a metadata label.
That is a hint to the scheduler, not to put too many things that Want a lot of disk space on the same node.
There's no enforcement, so you can… Request nothing and fill up the whole host disk.
With the local PV.
So I… it's like… But I think you're… I do think it's maybe a little bit misleading if… or, like, confusing for someone if they… Say they want 100, you know, megabytes of storage space, and then… use up 100 megabytes of storage space, and they see that they're 0.5% utilized, because the node's capacity is massive.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 23:42 Yeah.
So that's exactly the kind of metric that I was thinking would be, yeah.
probably fall into the same kind of bucket as the node CPU utilization that we were talking about before, if it's not clear what the What the ratio is.
On the utilization side.
you know, is it the total capacity of the disk, or, you know, the total capacity of the number of CPU cores?
Than the percentage that you're presenting.
Just… doesn't make sense unless you fully understand, like, both sides of the… The ratio.
**David Ashpole (Google LLC)** 24:13 Right, I think it makes… the CPU case makes more sense, because it is actually… enforced. I think it's… it's annoying here where we have a… like, this, capacity that isn't a real capacity, right? It's like a… It's more like a request than a limit.
**Jina Jain** 24:34 So, I just looked up the metric in question, we have, like, caters pod, volume available, caters pod, volume, capacity. But the thing is, we are reporting for all types, like, types like, you know, secrets and config map. So your config map can be, whatever, 100KB, but once… actually mounted.
it is going to show up as the empty directory, right, or whatever is the backing file system.
I don't know, is there any value in having things like that?
Because secrets and config maps, etc, they just seem like… even the download API… download API is one of our supported types.
Any means.
**Christos Markou** 25:27 Yeah, I'm also a bit… yeah, it's… It looks a bit weird to me that we report those metrics under, so… what is the entity that is, like, related to these metrics? Do we have a… pod volume entity thing, or we have directly a volume entity.
That we report these metrics against.
And should be pod, should be Kubernetes pod, if we… If we cover everything, like secrets, or every… config maps, whatever. But yeah, maybe it's not that we provide any value with this.
Yeah, if you have any, like… additional thoughts on this, or suggestions, maybe we can continue the discussion offline.
But, yeah.
I'm also confused about these metrics, to be honest.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 26:39 Sure, thanks.
**Christos Markou** 26:45 Okay, anything else?
In general.
**Jina Jain** 26:51 I think it's… It has a… PR Open Gablet stats, and I guess… There was already some discussion around, like, how to name the process metrics, but… I think, like, it's a little… confusing. It was… it was going into, like, first it was using systems.process, but then I think… I'm not sure if, like, all of us have agreed that we should move to the catus.nod namespace.
And if there is, like.
You know, if you should explicitly be calling out process versus a PID counter, explicitly, differently.
But yeah, there seems to be a lot of, like.
previous, discussion with Systems Semantic Convention around These metrics, so… If… if we could take a look at that.
**Christos Markou** 28:05 Okay, cool.
Thanks, Forum.
Raising it again.
Yeah, there is… If you… if we don't have anything else, Gonna wrap it up, and see you in two weeks, then.
Thank you, folks.
**David Ashpole (Google LLC)** 28:26 Bye. Cheez.
**Jina Jain** 28:27 Let's good.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 28:28 What?
