SIG: K8s Semantic Convention SIG
Date: 2025-12-09
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/H59mEY1eCNmAJLzyfEx7159gbEImKrlp1C77DWDvNwQUtzAQCYTP4a-ba8yi4EU.s8i9lkOzq8koS_0d
============================================================

## Zoom Recording Transcript

**Stephen Lang** 01:39 Just checking through these, links that you put on here. Looks like you've,
Filled out quite a lot of this table on the pay its resource attributes.
Issue.
**Christos Markou** 01:51 Okay.
Yeah, I don't think I have,
A lot to mention there, other than…
there were some… I checked the…
the diff between the implementation and the current state of the registry of Shamad conventions, and it seems that
So, we had few differences.
The major one is around the labels and annotations, because
in the implementation… in the processor, we're following the pattern of, having, for example, k.pod.labels. the name, the key of the label.
And it was decided a while ago, probably 2 years ago or something, that,
this should be plural, should not be plural, should be singular, without the S, so label and annotation.name of the annotation accordingly. So, this is a major, difference, and the other one I could spot is about the container image tags.
Again, it was… Image tag, a single string, but it should be plural.
with an array slice, a list of tags. And other than this, I don't see anything else missing.
So… I want to ask the maintainers.
of SMAT conventions, what should be the process? Right, and there were 3 that were missing, were not defined as remote conventions at all, and it was… I sent a PR last week, and it was merged already.
So, the other thing that I want to check is, I want to ask maintainers, what is the process that we could follow there.
Probably… Yeah.
Moving the attributes, through the stability levels, like marking them as beta or even as release candidates.
And then…
deciding on a time… specific time window, I don't know, like 1, 2, 3 months, whatever. Leave them there, and start using them in the… in the component behind the feature gate, that is the plan.
And the feature gate will be alpha, which means that it can be… can change, with no, like, limitations or whatever, so we are free to do whatever we want there.
And then after a while, we can actually do the transition, if we see no objections, no issues, whatever.
My only question is, If we're… if we should wait on anything, from entities or whatever.
Particularly what Gina mentioned during KubeCon about entities, relationships.
So, yeah, I'm not sure if we're blocked by this, or if we need any… Yeah.
Anything more from, the group, the entities group?
And I have also another PR which, adds
The… the roles for the attributes in the entities, the missing ones.
So if you want to, if you have some time and you can review this.
That would be helpful. There was a question if restart count should be identifying attribute of the KH container.
I think it should not be, after reading again the comment from Josh.
I think it should not be. But, I will wait for feedback from Dimitri.
On this.
And, yeah, I think that's…
More or less the, the updates.
**Stephen Lang** 06:33 Okay, great. So the PR, the review, is it the second link that you have?
**Christos Markou** 06:38 Yes.
**Stephen Lang** 06:39 On the agenda, yeah, okay, I can take a look at that after this.
**Christos Markou** 06:42 Yeah, who will need anyway… in order to, like, stabilize the entities as a whole, let's say CagePod or whatever, as an entity, we need to have
Let's say, roles, specifically, and, define which is the… which are the identifying attributes and which… which are the, descriptive ones.
But at the same time, we have the attributes listed in the…
registry, the very long registry, so… that are not… they are… the registry is the… I think we discussed this another day, it's a flat thing that lists everything.
So each attribute there has a…
stability level as well, so maybe we can start from there. I don't see, for example, things like pod name to change, right?
And then how these are consumed or used in entities is the next step.
Yeah, okay.
**Stephen Lang** 07:39 Okay, yeah, makes sense.
**Christos Markou** 07:41 So, if you have any…
like, feedback or concerns, let us know. And, there is also some progress at the same time on the collector side. I'm also, taking a look there.
Yeah, if you, yeah.
If you want to check the issues there, if you want to,
Look for something, if you have time, feel free.
People are already working on those issues. Oh, okay. Dmitry joined.
**Dmitrii Anoshin** 08:11 I hope.
**Christos Markou** 08:13 Hey, hello.
Yeah, we were just discussing about…
the updates and, the situation, what's the current situation. So, Dimitri.
There is one PR that you can find on the agenda.
There is a question about the cage container, Restart count…
And if should be… that should be identifying or descriptive.
Josh commented there, I changed that to descriptive, because I thought of it again, and I think…
We don't really want to distinguish CH containers differently per restart.
Let's say, sequence or whatever.
But, yeah.
**Dmitrii Anoshin** 09:06 That's actually… I'm not sure about that, to be honest, because we…
we used to… we introduced that restart count to get proper logs from every individual container, run. So, potentially, it can be a different entity. It can be not container, but container.
Container execution, something like that.
**Christos Markou** 09:31 Do we need this, though?
Yes.
**Dmitrii Anoshin** 09:35 We do need this to associate particular logs with container execution, because container logs are stored in most of the container agents under particular…
**Christos Markou** 09:51 log, 1.log, and so on, right?
**Dmitrii Anoshin** 09:53 Yes, and that path includes restart count. So let's say it will be another entity called container execution, in that case.
And, in that… in that case, container restartCount doesn't belong to the container.
**Christos Markou** 10:10 Yeah.
**Dmitrii Anoshin** 10:12 Last terminated reason, however, can be descriptive.
**Christos Markou** 10:17 Because it's relevant to last execution, so essentially.
**Dmitrii Anoshin** 10:23 Kind of here, we… Like… Set some relationship to the latest,
Execution, so… potentially, it's not really needed, but if we want to keep it, we… it can be descriptive, yes.
**Christos Markou** 10:38 Yeah. Do we… I mean…
I'm just thinking, if we actually need this restart count, I see the point of having logs coming from different files based on this restart, numbering.
But then… we have the processor, the KH attributes processor, this cannot container ID, cannot container name.
Probably. I'm not sure… yeah, probably it can… probably it is doable. So, in that case, you have KHContainer, which is, like, a conceptual thing that is the entity, and the actual container from the runtime, it's a different thing with its own ID and stuff, so…
I wonder if we actually need this, you know.
This restart count thing.
how this should be useful. If you have a use case, maybe, can help.
**Dmitrii Anoshin** 11:33 So, the use case for that is,
that file lock receiver doesn't know container ID. File lock receiver only… it can take data from the path, and path doesn't have a container. Yeah, yeah. So it only can have the number, that restart count number.
So, let's say a container, firewall receiver as an observer of an entity, it doesn't have,
ID of the container.
**Christos Markou** 12:08 Yeah, that's true. In that case.
it can… it can have the audio ID and stuff.
But then, can it have container name? Kh container name?
**Dmitrii Anoshin** 12:22 It does have container. So, like, but if we are talking about Kubernetes context, right, the entity is Kubernetes container.
And, we should distinguish, probably, between container definition, And container status, I guess?
Yeah.
**Christos Markou** 12:43 I'm not sure what we get from this, though, because… I mean…
you can have container name, Kubernetes container name, and then
The signal, the log, will go through the container
sorry, Kubernetes Attributes Processor, and if you have pod UID and Kubernetes container name, the processor can extract container ID.
from the runtime, and that's all you need. So you have two entities, container… No?
**Dmitrii Anoshin** 13:15 I believe container ID changes after different executions, between different executions, right?
So, would you…
**Christos Markou** 13:23 get this distinction, right?
**Dmitrii Anoshin** 13:25 What, what, sorry, what?
**Christos Markou** 13:26 So we don't get the distinction based on the different ID?
**Dmitrii Anoshin** 13:31 We don't have the ID provided, right? If you supply… for Kubernetes attribute-based processor, if you supply pod name and… pod UID and container name, you would get a container… container definition, let's say Kubernetes.
Container as a definition, right?
But you will not get an actual container execution that will… from that.
**Christos Markou** 13:58 Okay, I… yeah, I had the impression that we could. If we could get container ID from… as it is coming from the runtime.
**Dmitrii Anoshin** 14:06 Is this enough? We can only have current container, like, if it's currently running. Yeah, yeah, I see, I see. So, you say that if it is…
**Christos Markou** 14:15 Yeah, if it is stopped already and we come afterwards, we cannot get it. Okay, I see.
Okay, then in that case, we need to, clarify this.
That was a… that's what I was missing, so…
**Dmitrii Anoshin** 14:29 So, restart account in that case is important information to get the particular container execution instance.
We can call it container instance, maybe, or container execution instance, something like that.
But for the entity of…
Kubernetes container, we might say that this is Kubernetes definition of a container. In that case, it's not a container execution.
In that case, restartCount can be a descriptive attribute, which would just tell you how many times container restarted.
**Christos Markou** 15:07 Yeah, yeah.
**Dmitrii Anoshin** 15:08 But it'll be a bit different thing, right?
But if we define, later, container execution instance, in that case,
I believe for that particular case.
container ID would be identifying attribute.
But…
in order to get that one from Kubernetes perspective, from, let's say, Kubernetes attribute-based processor, you would need to have restart count.
**Christos Markou** 15:39 Yeah, yeah. So…
For this specific entity, we should be fine, the one that we have already defined, but we need to think
What to do with, running game stamps or whatever, and if we need a new entity.
**Dmitrii Anoshin** 15:55 We need to clarify that this one is specifically about container, like, definition in the Kubernetes.
**Christos Markou** 16:02 Okay, okay. Right.
Okay, cool, sounds good.
**Dmitrii Anoshin** 16:07 I'll also take a look, and I'll review that PR as well.
**Christos Markou** 16:12 Sounds great.
And the other thing is, out of this, I mean, after this, maybe it's not a blocker, but I was reviewing the list of the attributes that we need for the Kubernetes attributes processor, because it is, let's say, the first one that we will be focusing on.
And it seems that we have everything that we need there, is the issue that I linked on the agenda, the first one. So, the question is,
What is missing, or what we should do next.
Should we start, like, considering
Bumping up stability levels for attributes, and then entities as well.
Or we wait for anything from entities? What do you think?
**Dmitrii Anoshin** 17:08 So, I would say we need to… I wouldn't actually bump attributes related to entities, because entities seek in general, is, like, is still…
in development. We don't even have a… let's say… we don't… there's supposed to be another signal when you send data as entity. We have that experimental implementation in the collector, but we haven't defined that in the spec.
So that's, like, the second phrase of the entities, seek. So I would say, let's wait for that. Let's do not…
bump.
entities-related stuff.
Our development, but everything else, whatever we can, whatever we're comfortable with, we can start,
Okay. Making progress. So…
**Christos Markou** 17:58 for Kate's Attributes Processor, specifically.
We now… we call them resource attributes, right?
**Dmitrii Anoshin** 18:06 Yeah.
**Christos Markou** 18:06 everything that we meet. So, for this, we only need
attributes, how they are… whatever is defined in the registry, right? Shaman Convention Registry.
**Dmitrii Anoshin** 18:16 Right, right.
**Christos Markou** 18:17 Okay, so… it seems that nothing blocks us from start, like…
pushing for this, either sending a PR, or start the discussions, get feedback from maintainers? Yeah. Okay, okay.
Alright, cool.
**Dmitrii Anoshin** 18:34 I'll also… I'll also start some work related to entities in the collector, because right now, receivers,
resource detection processor, Kubernetes processor, they all based on the definition of resource attributes, as you said?
And even the configuration that is generated to the users, that's the most important thing based on that. But we need to, like, emit entities, especially in receivers, so the interface would be completely different, I think, and we need to plan for that migration. It's gonna be a big change.
And, I will probably create some issue and start pinning people to… for their opinions, for the feedback, before we can actually stabilize, like, stuff, like, Kubernetes Attributes Processor, oh, sorry,
Kubernetes cluster receiver, or host matrix receiver, etc.
**Christos Markou** 19:30 Do you think that the KH attributes processor
Stability depends on this, because…
**Dmitrii Anoshin** 19:38 I think we need to at least think about it. I haven't looked through the Kubernetes attributes receiver at this point yet, because we, like…
It's currently having the same issue, right? Kubernetes attributes processor only works on the resource attributes. That's the only concept it understands.
it provides some configuration interface… it actually provides two configuration interfaces. One is deprecated when you have a list of attributes, and then you have, like, particular attributes enabled, disabled. So this will likely needs to be changed anyway before we mark it stable.
So, it also goes to that bucket. I guess my… that work that I'm planning is actually pretty critical. So, I'll… I'll…
I'll make a PR, like, issue today. We can discuss, we can, like, under…
We can, agree on the design, and then…
We can stop… stop the product.
**Christos Markou** 20:44 Okay.
**Dmitrii Anoshin** 20:44 You posted this issue from, from Pablo, I guess.
**Christos Markou** 20:49 I think we need to raise awareness there.
**Dmitrii Anoshin** 20:52 Yeah, I'll submit an issue and raise an awareness about that. I guess… yeah, I just, like, I've been delaying that due to other conflicts, but I guess…
That's fine. This time, yeah. So, for example, Prometheus receiver isn't affected, but…
KTS attributes processor is affected, and host metrics are affected, and resource detection is affected.
**Christos Markou** 21:15 File lock isn't affected.
Okay.
Alright, sounds good then. We can, continue offline once we have these issues.
**Dmitrii Anoshin** 21:28 Cool.
**Christos Markou** 21:31 Anything else?
From anyone?
Okay.
Next one is, like.
two weeks from now, quite close to, like, holidays period, so probably I can… I will,
Cancel it, and we can meet again.
Next year, if you agree.
**Stephen Lang** 21:58 Yeah, sounds good.
**Christos Markou** 22:00 So, thank you, everyone, and see you next year, I guess.
**Dmitrii Anoshin** 22:03 Thank you, folks.
**Stephen Lang** 22:04 Thanks, bye.
