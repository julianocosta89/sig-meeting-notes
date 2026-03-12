SIG: K8s Semantic Convention SIG
Date: 2025-11-25
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/KfSGYFhgE1b-sdnTqrTxk-4xdJvP1AEktLlHV5Uv5odIu8T3w4vPC2hu9Bwxi1w0.RgPTZPod6A94A7CQ
============================================================

## Zoom Recording Transcript

**Christos Markou** 00:52 Hey there.
**Stephen Lang** 00:58 Right.
**Christos Markou** 03:10 Let's see if anybody else is joining, and then we can start in a couple of minutes.
**Stephen Lang** 03:18 Sure.
**Christos Markou** 04:53 I guess we can, yeah, start.
it's not something… it's not that we… I have added a few topics, not something really new.
Mostly summarizing what, what we discussed during… the in-person meeting that we have in the hotel observatory.
So, yeah, I filed this issue… To, depict the phases that we discussed.
Having the first one being the, yeah.
The first one is about the… Attributes that are required by… The components that the collector will be stabilizing.
essentially Kubernetes attributes processor, And, a little bit, research detection and file… processor and file receiver.
Wasn't sure about the promises receiver, we'll need to… I know David mentioned that, I will need to ask him explicitly, but I couldn't think of anything that… do you know if Prometheus Receiver has any… specific usage of Kubernetes attributes.
**Stephen Lang** 06:07 Not off the top of my head now, I don't know.
**Christos Markou** 06:10 Okay, cool.
Yeah, and then the two other phases. This is mostly a meta issue, not… Something that can be completed, like… from one day to the other. And… yeah, I think the first… The top priority right now will be, Dishon.
Specifically, the research entity attributes, whatever. So, I took the chance to collect everything from the metadata.
YAML file of the processor, And also the extract metadata configuration, because… Yeah.
You need to explicitly… Add those in the extract metadata configuration setting, so as to have them being exported.
So, yeah, I… created this list here. I still haven't, like, completed the table, so I only added those that are used by the KH attributes and file log receiver. I didn't, I didn't go over issues detection.
But I think there are, just a few of them, probably cluster, cage cluster name, KHClusterUID, these things.
But yeah, anyways… Yeah.
out of this, I think… And this brings us to the two other questions or topics that I had.
The first one is mostly about this issue that was raised.
Yeah.
A little bit ago.
And I would love to have the feedback from this group, so… Yeah, the… The issue describes the situation that, some… Kubernetes resources are covered by the semant conventions.
But we can also have other things, like custom resources, we can have resource open telemetry Collector, for example. So… Yeah, the question was if we should have, some generic rules on how those should be covered. I'm not sure if the suggestion was to just have guidelines, or if we should change the modeling.
So, I just commented a few minutes ago, And, yeah.
I'm not sure if we would like something like this, to change the modeling. I would try to avoid this, to be honest.
To generalize the model in a way that can cover any sort of research type.
then have resource UID and resource name. I think this will be, this will complicate things, maybe will make queries, harder, and also bring significant braking changes for the components, so maybe it's not a good idea.
However, having guidance, within the SMAT Convention, saying that if you want to extend the… you have custom… you want to have custom Kubernetes… research attributes, entity attributes, you can, follow this pattern. So… Yeah. In this, we can, like, tell to the users, follow these guidelines and extend the SMAT convention, or even define your own registries using WIVER or whatever, in a way that works for you. I think that was a suggestion from Tyler. I would wait to, get some feedback, but if you have anything to add, yeah, please.
Also, add your commentary, or if you have anything to share now.
**Stephen Lang** 10:04 Sure, yeah. I'd be interested to know why you think it might make the queries more complicated if you use the generic attributes.
**Christos Markou** 10:14 So, was that the question? I…
**Stephen Lang** 10:17 Yeah, yeah, just, why do you think it would make the queries more complicated with the generic attributes?
**Christos Markou** 10:24 Yeah, because I think it adds an additional… Let's say… abstraction layer, so… we don't… For example, if you want to… like… Aggregate something that is pod-specific.
Right now, we have the… you have the KHPod namespace, so you can directly, look out for those. You can also have pod-specific attributes that are not, yeah, also part of something else. So… If we generalize this, first let… first… first step could be to, first… Part of the query would be.
if K's resource type equals pod.
then, list the names, or list the, I don't know.
CPU resources or whatever. So, I think this adds an extra layer of complexity.
And, since Kubernetes API itself Does not have this abstraction.
First place, Maybe we are… Good to go with what we have today.
**Stephen Lang** 11:37 Yeah, that's a good point. Yeah, I like the point about the… being influenced by the design of the KX API itself.
**Christos Markou** 11:45 Yep.
**Stephen Lang** 11:47 But it does mean you end up with a whole load of potential Well, an unknown number of… Like, custom attributes.
with, with the idea being that They wouldn't all have to be upstream if you were, you know, creating…
**Christos Markou** 12:06 That's the idea. Upstream, we can have the, let's say, vanilla cage, resources.
**Stephen Lang** 12:14 As we need them.
**Christos Markou** 12:15 And then… people, if we want to do, they want to do, like, custom things, they can maintain their own registries, which is, in general, is also the direction. Semantic conventions are not expected to, like, cover every single use case for every, like, random… scenario.
**Stephen Lang** 12:34 So Argo could have a registry, for example.
**Christos Markou** 12:37 yep.
**Stephen Lang** 12:41 Okay, and is, you mentioned Weaver before, I'm not too familiar with, with Weaver. Is that something that would allow you to, you know, reference these other… conventions.
**Christos Markou** 12:55 So, yeah, Weaver is, like, a recent project of OpenTelemetry.
And actually, it can be used as a tool to validate telemetry, and Weaver itself is used by Semat Conventions project as well, I think.
And, for example, it allows you to define your own registry, define rules, validation rules, for example, for your own registry, and you can also import, let's say, cement conventions from an upstream, a remote. So…
**Stephen Lang** 13:29 Okay.
**Christos Markou** 13:31 Potentially, you can define your own registry, and import upstream Cemant conventions, and extend it as you… as you wish.
**Stephen Lang** 13:40 So, for people who wanted to share their registry.
They could, host it somewhere.
**Christos Markou** 13:47 if they… I'm not sure, yeah, I'm not sure how this could be shared or whatever, but I assume that, based on your needs, you can maintain this, so… I'm not sure if there would be, like, a common place where, yeah, if there is something that can be common, then probably this can go to some other conventions, maybe.
**Stephen Lang** 14:09 Okay.
**Christos Markou** 14:10 That's a common place to maintain attributes, or whatever.
And there are also discussions in the collector project about using Weaver.
And there, there is also this argument that, it… it won't be necessary for All the metrics or all the attributes to… Define… to be defined as a math convention. So, let's say you have a random comp… you have a… you have a component like Kafka or whatever, and maybe you don't want to, like, implement the defined metrics that it emits as a MAT conventions. There, you could have a Weaver support.
define the local registry for the component, and potentially also import from upstream cement conventions, and also, define the rules that should, the validation rules for this component, that, for example, stable metrics should not be changed, and so on.
So I think we're heading towards this direction, in general.
**Stephen Lang** 15:20 Okay, cool. Thanks for explaining.
**Christos Markou** 15:23 Yeah, no problem. Yeah, since this is kind of important, I would wait, like, to have, like.
Clear majority and agreement.
Yeah. And then, out of this… yeah, after this, we can also start discussing about Yeah, actually declaring those as… release candidates, or, I don't know, generally available. I don't see anything, like, blocking us, other than the open question about, what What we should do, or if we should do something about entity relationships.
So, for example, we have, a pod that will be belonging to a namespace, and deployment, and so on. How… We should handle these relationships.
I'm not sure if there is support already for this.
But in, yeah, general.
what we care about is, should we wait for this? Should we be blocked for this to be discussed first as part of entities working group?
Or we can just proceed.
**Stephen Lang** 16:34 Okay, makes sense.
**Christos Markou** 16:37 And the good thing is that, most of those are not breaking, so… Oh.
Yeah, Kate Spot name was there before.
Nothing has changed, so, the things are mostly straightforward.
Aww.
Opposite of metrics, where we have changed a bunch of those.
Unfortunately.
So, yeah.
Yeah, I think that's all I had, I… Yeah, can't wait for people to, comment there online, and we can keep the… conversation going, I guess.
**Stephen Lang** 17:18 Yeah, sounds great. Thanks for, Documenting all of that on the GitHub issues.
**Christos Markou** 17:24 Yeah, it's a good timing now, because it helps having this momentum in Otel in general, and… Also in the collector SIG.
about stabilizing, stuff. It's, important for end users, and… Downstream, let's say, users like vendors or whatever.
Would be nice to see this happening soon.
**Stephen Lang** 17:47 Yep.
**Christos Markou** 17:49 Cool. Yeah, anything else from your side?
**Stephen Lang** 17:54 No.
No, that's it for me, yep.
**Christos Markou** 17:56 Okay, sounds good.
**Stephen Lang** 17:58 Alright, thanks.
**Christos Markou** 17:59 See you in a few weeks. Bye-bye.
