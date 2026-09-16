SIG: K8s Semantic Convention SIG
Date: 2026-09-15
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:06 Alright, Chris.
**Christos Markou (Elasticsearch, Inc.)** 02:57 Hello.
**David Ashpole (Google LLC)** 03:59 Well, hello, sorry for being a little late.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 04:04 Alright.
**David Ashpole (Google LLC)** 04:06 Do we have anything on the agenda for today? If not, I think I have one topic. Is there someone who opened something about creation time?
Put that on there.
Yeah.
**Christos Markou (Elasticsearch, Inc.)** 04:25 Yeah, maybe mine is quite, it's a quick one.
based on… last meetings, conversation, I sent a PR to… Mark the node utilization.
The utilization metrics, that are calculated as a ratio against note… capacity, that we already have them in the cubeless charge receiver. I send the PR to mark them for deprecation.
And, yeah, Tyler had some feedback.
Seems that he approved, so… Yeah.
If you have some time to check this as well.
That would be helpful.
And… Yeah, we'll still have time to keep them, and probably the… Total removal of those metrics will happen once we're ready to transition to stable metrics in general for the component.
**David Ashpole (Google LLC)** 05:34 Cool.
**Christos Markou (Elasticsearch, Inc.)** 05:35 Next one.
**David Ashpole (Google LLC)** 05:37 Yep, let me find it.
So… Sorry, too many tabs.
Alright, so someone had opened an issue asking for object creation time.
And we have some precedence for this, because for pods, we have the pod start time.
As an attribute on… kates.pod entity.
I think there's a lot of questions here, I don't know if anyone has… Like, remembers the history of how… Or why we did start time as an attribute.
But, in general, I think the idea makes sense of having creation time on objects.
Even pod, because… You know, often takes time to schedule or whatnot before the start time is set.
Opt-in seems reasonable to me as well, but I was curious… I know that for CubeState metrics, the start time and the creation time are actually separate gauge metrics, so that people can do Like, math on them.
I know that we've… we're not… We're not trying to be a KSM clone.
But often we do follow in the same… and make some of the same decisions that they've made, so I'm just curious, like… if, if people have thought about this before, if anyone needs this. I can't tell if this is just someone Like, looking for things… To work on, or if there's someone who's…
**Jina Jain** 07:42 So, David, are you suggesting we make it a metric instead of having it as an attribute on the entity?
**David Ashpole (Google LLC)** 07:49 No, I just haven't thought of… I mean, that's the alternative, right?
And it feels like if we… I suppose we could have both eventually.
But I wanted to make sure we… like, I don't have a use for this, so, like, this is me saying, like, oh yeah, that seems reasonable to do the same thing, but I was wondering if any of you had Thought about this, or if you need the creation time, or… Or if you need it as a metric, yeah.
**Jina Jain** 08:21 On the pod node entity, I think I might have… added some of the more, recent Kubernetes object entity attributes, and I have a feeling I did add.
A start time equivalent to some of the objects.
I think I might be following, the existing pattern.
But then on the other hand, like, as part of, like, a descriptive you know, as a descriptive attribute for the object in an entity model, I feel like it makes sense to have it.
Yeah, but… And again, a metric also makes sense, so… I'm not sure. Maybe we can ask them if they have a… specific use case.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 09:06 I can talk to one use case.
So when you're providing a list of pods based off of metrics on a UI, Say, for a node, or a namespace, or whatever.
If you look at a list of pods over time.
It's hard to know when a pod started without the start time, and so if you just look at the list of pods at a point in time, which happens to be now, and you see 100 pods.
How do you know which of those pods?
are older. And if a pod at that point in time happens to be scheduled to be replacing a previous pod, say, for example, for, like, a version rollout or something like that, or a feature flag, whatever change.
How do you know for those two pods which are part of the same workload, for example.
which one would be the newer one. So if you were sorting by age in the UI, or you wanted to somehow show a timeline.
Like a chart where you would see maybe older pods would be sort of coming from one side of the screen, and then the newer pods would be sort of coming.
further on, those things are really hard to do without having a start time, because in order to discover a start time without having it in the metrics, you have to query all the way back to the beginning of when that Odd might have started emitting metrics, which is unknown.
Because you could do, well, is it last one hour, does it lasts 7 days? Does it last one year? Until you start scanning back and find when the That particular pod didn't exist.
then you have no way to discover the age. So, that's kind of the use case that I'm familiar with.
**Jina Jain** 10:53 Interesting. I think I understand what you're trying to say, but now I have a different question. I guess this is not relevant to the topic, but can't we just look at the current instant?
Of the metric, which should be the current age.
I guess, and then figure out the start time for it.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:11 Does it have the age? Does it have the age on it? I thought that was the… the question.
**Jina Jain** 11:15 So, how does a metric which is, like, tracking the age of a thing show up in Prometheus? Is it just… A counter, which keeps incremented by…
**David Ashpole (Google LLC)** 11:30 No, they set it as a gauge.
So you can… I think Prometheus has a time function, so you can just do, like, time minus… The start time, and then you… that gives you, basically, an uptime.
An uptime graph, if that's what you're looking for.
**Jina Jain** 11:53 Okay.
**David Ashpole (Google LLC)** 11:54 But that's if the metric is… is separate and not an attribute. So an attribute, if you, you know, would not be a cube-state metrics replacement. It would be a… this is how open telemetry wants to do it.
And, yeah, you wouldn't be able to, like, consume it that way in PromQL, but I'm sure there are other query languages where you… you could do math on the… on the attribute.
Or display it in the UI in some way.
**Jina Jain** 12:24 Okay. So… So that's… it is… Relatively easy in most backends to… write a query which gets you the exact start time? Is that… from a metric, from a Prometheus-style metric, if we send, like, the creation time or start time in that format.
**David Ashpole (Google LLC)** 12:45 Yeah, if it's as a metric.
I think it has to be… and you're using PromptQL, then certainly it'll work.
**Jina Jain** 12:53 I'm good.
**David Ashpole (Google LLC)** 12:55 Unix timestamp value.
**Jina Jain** 13:02 I mean, to be honest, I think, like, I can see the other argument here also, the… just having that attribute, and if your backend supports showing an entity.
If it's attached to your pod, for example, you have, like.
some sort of data links thing going on, and you can go from a metric, select a pod, and then just show up, you know, the entity shows up with all the descriptive attributes, and you have a start time there. That seems much easier than doing all of this, I guess.
So I can see the argument for both.
For this… for the specific PR, I guess we can ask them if they have a specific use case, and maybe… Suggest, going with metric if they, you know.
Say they want to track up time or something, like, they want to chart it or something, then maybe you can suggest metric for now.
**David Ashpole (Google LLC)** 14:31 Sorry, did you say that we should… Start with the attribute, and then do the metric later?
**Jina Jain** 14:39 Yes, I… like, I'm… I'm not against adding the attribute, to the entity. Someone has requested that and has a use case. That's… that's what I'm trying to say, yeah.
But I'm also, like, I understand having it as a metric is also useful, so… But don't we have an uptime metric? I feel like we have an uptime metric.
dimension.
**David Ashpole (Google LLC)** 15:08 Or pods or for objects? We might have one for pods.
**Jina Jain** 15:13 Yeah, I think it might only be for part and node, not for… But also, like, I don't know, does it make sense to have uptime for objects which are not pod-backed?
**David Ashpole (Google LLC)** 15:25 For a node, maybe?
**Jina Jain** 15:27 Yeah, for a node.
**David Ashpole (Google LLC)** 15:30 Or a volume, maybe?
Is there a PD? I don't know.
**Jina Jain** 15:36 I guess for volume, it'll become then… is it… uptime is only when it is mounted for real, and it's not just in the cloud providers?
So… That can become… Yeah.
**David Ashpole (Google LLC)** 15:50 I think… I think creation time as an optional attribute seems reasonable. I… I think unless anyone's opposed, I'll probably approve the PR.
Assuming it's correct and stuff, I haven't looked that closely.
**Jina Jain** 16:09 Sounds good to me.
**David Ashpole (Google LLC)** 16:15 Alright, anything else people want to discuss?
Anybody have any PRs that are waiting on review?
Cool.
then, I think we can drop early. It's good to see you all.
**Jina Jain** 16:40 Thank you, folks.
