SIG: K8s Semantic Convention SIG
Date: 2026-09-29
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:50 Hey, Chris.
**Christos Markou** 01:55 Nope.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 01:56 Absolutely.
Hey, Tom.
**Christos Markou** 03:02 There is only one topic, let's give it a couple of more minutes, and… Then we can… Oh.
Can't start.
Okay, Let's… Let's start, and I only added, One PR on the agenda, which I called for review. It's, It's a PR that promotes the CPU usage metrics to release candidate.
And… I think we spent… A lot of time in the past months to discuss about.
Specifically how this metric is calculated.
And… I think we'll have, enough evidence so far that we're doing it the right way, and we're following what also the system metrics are doing.
and there is on on the implementation side, on on the collector, on the kubelet charge receiver. There is the change… We have introduced a change to implement the metric on the fly, essentially.
Doing the calculation using the… latest metric and the current metric that we are retrieving from the CPU time, instead of using the metric that the kubelet stats provide.
And yeah, we discussed that extensively. The future gate is on beta right now, which means it's a default behavior.
I guess we can promote it to release candidate, and we can leave it there for a while, in any way, and unless someone complains on the implementation side.
when we decide to promote the metrics, the Kubernetes metrics to stable, yeah, we'll have all the information. We will have this validated.
Oh, that's the idea.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:21 Sounds good.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 06:23 No updates needed to the normative doc, right? Because the… this is the SEMCOM that's been in place for a while.
**Christos Markou** 06:32 Sorry, I didn't hear,
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 06:35 a Do we need to update anything in the migration guide for Kubernetes?
**Christos Markou** 06:40 I don't think so, Because, semantically, the… The metrics are not changing.
What changes is that instead of getting the metric directly from Kubelet Stats.
from Kubelet's touch API, we calculate.
It's on our own way.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 07:00 Yeah, and that was that. I remember that change that's in place already and that's an implementation detail, not a migration thing. So I think we're.
**Christos Markou** 07:06 Yes.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 07:06 Right. Okay, cool.
**Christos Markou** 07:15 Okay, next one. It's from you, Steven.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:25 Sorry, muted. So, I was looking at the KXPOD status phase SEMCOM the other day. I know this is different from the actual implementation currently in the collector. This doesn't match up with the metrics that we see, so this is currently unimplemented, and I know that it's been changed fairly recently as well.
But I was actually trying to understand what the metric is supposed to look like.
And if I just share, so that it's… we can… Maybe you can just clarify mine.
understanding as to what these attributes are going to look like. So, there's a metric with an attribute of the same name, which is KXPOD status phase, and the metric is linked to this entity, KXPOD.
And it says that the value of the metric.
If I understand correctly.
is the number of pods that are in a given phase, so I would expect five series, you know, one for running, one for pending, one for succeeded, completed, and failed, I think they are.
but then… What I didn't understand is, does this entity association, does it mean that it's also going to inherit all of the other attributes from that entity, such as the namespace?
As well, and maybe all of the workload details. So what I'm asking is.
Would this be, like, one set of series per cluster? So, for my entire cluster, would I expect only 5 series?
**Christos Markou** 08:53 It's per pod. So, if the possible… the possible phases are, let's say, 5, you will have 5 different states, 5 different lines, let's say, time series, per pod. And the other description is, in a way.
number of pods in this phase will be always one, because we limit this, to the specific pod. So, that is the caveat there. And if you… aggregate all those, you will have all the pods of the cluster, for example, that are in the specific given phase. But here, the assumption is that we scope it within a single pod. We scope it within Yeah, per pod, essentially, that is the idea.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 09:45 So what attributes could I expect if I was to see this metric in implementation?
Other than the CAITS pod status phase.
Absolutely.
**Christos Markou** 09:54 Maybe, yeah, the Entity Association is a Kubernetes pod, so it's like… everything that is related to this pod, I would say.
So it's a pod-specific metric, not for the whole cluster, unless you do an aggregation there.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:15 So.
Okay, so the metric has a value.
Which is the number of pods, which is always 1.
**Christos Markou** 10:25 One or zero, yes.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:26 And it's gonna have K8s namespace name, K8s pod name, deployment name, all of those things.
**Christos Markou** 10:35 Yeah, based on, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:38 eventually.
**Christos Markou** 10:39 How it's implemented, but yes, here it is.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:42 And then this… Attribute of the same name.
Says that it's a string.
So… Is this just… meant to represent the five individual series that I would see for this pod.
So, I would effectively see This K, it's pod status phase equals ending, equals running, once per…
**Christos Markou** 11:06 Yeah, you will have 5 different values there, so… and… For only one of these phases, you will get, the value being… equal to one. So, you will… let's say we have 5 phases, 4 of them will be equal to 0, and one will be equal to 1. So, yeah, that's the idea. And I think it's similar to KSM cube state metrics.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:32 Yeah, it is. Yeah. I think I might just, So, I might, suggest an update to this wording. I might have a… have a think about that, because, when… initially, when I saw this, and it said, describes the number of KAX pods that are currently in the given phase, I thought, well.
Is that for the entire cluster, for the namespace, for the deployment?
And if it's always going to be 1, then maybe we shouldn't say that it's a count of pods. We should just… I mean, maybe should it be a Boolean value instead?
**Christos Markou** 12:08 Yeah, I know it is confusing, and I would be happy to… To see this improved.
I'm not sure if we can have anything, any… I mean.
It's actually like a Boolean value here.
But I'm not sure if we can describe it like this.
I don't… yeah, David, any… do you remember any details around this?
**David Ashpole (Google LLC)** 12:29 Is the disagreement around the unit?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 12:32 So there was just a point of confusion because this isn't actually an implementation yet. I'm just trying to guess at what it would look like eventually. And there's two things that threw me off. One is the wording because it says describes a number of K8s pods.
So I thought, well, is that pods in the entire cluster? So would I expect to see only five series for an entire cluster? And it would be almost like the kubelet running pods and kubelet running containers metric.
So I would just see, you know, there are 68 running pods, 73 failed.
But Chris has clarified that this is a per pod.
series, so that's not true. This would be, for each individual pod, you would have 5 series, and each pod would be one for only one of those series to indicate which phase it was in. So each part would say it was… Failed or succeeded.
So I understand that, but then, The next thing that kind of threw me off is the fact that it's an up-down counter.
And it can only ever be 0 or 1.
And I thought, well, to clarify this behavior.
One is to update the description.
To not even talk about the number of pods, because it can only ever be one or zero.
And secondly, the type, then, if it can only ever be one or 0, should it be a Boolean value?
**David Ashpole (Google LLC)** 13:57 There's no… Juliet Instrument.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 14:01 I'm only thinking of the Boolean value that I've seen in OTLP. Is that different to instrument type?
**David Ashpole (Google LLC)** 14:08 I believe for instruments, they today only take… Float 64 or Int 64.
Like there's no.
There's no instrument type that records only true or false.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 14:23 Okay.
**David Ashpole (Google LLC)** 14:25 our.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:26 the.
**David Ashpole (Google LLC)** 14:26 It would be up, down, counter, gauge, counter, or histogram, which would be even sillier.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 14:31 Okay.
**David Ashpole (Google LLC)** 14:32 Tyler jumped in.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:33 The it this is an aggregatable metric. It it would be meaningful to aggregate this.
metric with other series. Is that accurate?
You could say, give me… the state of all my pods in the cluster that are pending, right?
**David Ashpole (Google LLC)** 14:51 Okay.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 14:51 That's meaningful. So my guess is that it can't… it should definitely be some sort of number to reflect the fact that it's… aggregatable. That's why we went with up-down counter, right? Because it's… it's going from 0 to 1, so it is going up and down, but it's a counter, so it's a sum, so it's aggregatable.
**David Ashpole (Google LLC)** 15:10 Right, yeah, so you wouldn't, for example, want the If you aggregated cluster-wide, you wouldn't want the average.
Which would just be one.
You would probably instead want to sum them. So that's where up, down, counter.
comes in.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:30 Okay, so it all looks correct, I'm just… you're helping with… helping me with my understanding, so thank you for that.
Is there…
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 15:36 I don't… This, this, markdown is generated from the.
from the YAML files, right? Is there a way to add, like, a 2?
That clarifies, like, this… this is going to be 0 or 1. Would that be enough, you think, to clarify, Steven?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:57 Well, I was thinking we could just… Maybe update this description.
So rather than talking about the number of pods.
It could say something else that was to indicate that it would be the active phase or not.
I could think about the wording a bit better.
But, doesn't necessarily need another footnote, but… Maybe just improving this description.
But, I guess I'm still a little bit confused because of the… The attribute and the metric of the same name kind of having a bit of an overlapping meaning.
But independent in terms of types.
**Christos Markou** 16:41 Yeah, I I added 2 links in the agenda. The 1st one is a Like, guidelines around how these metrics are designed.
So… It is documented, and… If we see that this needs any sort of improvements, we should also update this one as well.
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 17:07 I know this particular metric's been hard. We had… I think the way it is in the collector right now is.
It's got dot A's in the name, right? It's like dot pending dot.
running, and I don't think it even has an attribute, so… Well.
Yeah, this, I feel like we've talked about this one a lot. It's a hard one.
**Christos Markou** 17:29 Yeah, I think we use underscore.
We split the metrics by a different name, so we have underscore something, underscore pending, underscore something else.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:43 Because, isn't there a number that represents the current phase?
if I remember correctly, there was, like.
Running is number 2. And then, you know, those 5 integers all have a different meaning, I think, at the moment. And it's all k8s.pod.phase.
**David Ashpole (Google LLC)** 18:02 Is it the value has a different number?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:04 Yeah.
**David Ashpole (Google LLC)** 18:05 Like, if I sum, I just get, like… A very odd number.
**Christos Markou** 18:10 That you need to figure it out.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:11 Is.
**Christos Markou** 18:12 What that means.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:13 Is that right?
**Tyler Helmuth (Raintank, Inc. – Grafana Labs)** 18:14 Summit.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:15 Serena, you've been looking at this.
Serena, can you remember is the value for running? Is it two? Is that how it looks?
**Serena Serena (Raintank, Inc. – Grafana Labs)** 18:24 Yeah, I think 1 is pending, 2 is running, 5 is unknown.
I can't remember what 3 and 4.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:31 Okay.
So if you want to sum, David, you'd have to do, you know, sum of… You know, subquery everything equals 2, or… At the moment.
Sum of group by of everything equals 2.
And.
Okay, yeah, thank you, I can, I'll take a look at it.
Let's take a look at this.
**Christos Markou** 19:04 Cool, anything else?
Okay, so see you in 2 weeks then. Thank you. Bye bye.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 19:16 Excellent.
**Christos Markou** 19:18 Have a good one, bye.
