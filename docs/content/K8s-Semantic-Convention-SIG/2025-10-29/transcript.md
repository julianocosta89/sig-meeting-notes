SIG: K8s Semantic Convention SIG
Date: 2025-10-29
Duration: 15 minutes
Zoom Recording URL: https://zoom.us/rec/share/CpUTOWvFjoIqqM6cSq6AsrhPI4vWPeJjWFLSpQgU6HvA23Moiylo6w3kRLGRKcOt.xtc9Pr3iYmfPlCnO
============================================================

## Zoom Recording Transcript

**Dmitrii Anoshin** 01:36 Hi, Christus.
Echo, I hear you.
I still can't hear you.
No, they're not here.
**Christos Markou** 02:38 Can you hear me now?
**Dmitrii Anoshin** 02:39 Yeah, I can hear you now.
**Christos Markou** 02:41 That was my… Sorry, my slides.
**Dmitrii Anoshin** 02:44 Sure. So, did you have the meeting half an hour ago?
**Christos Markou** 02:48 No, we haven't changed the time yet.
**Dmitrii Anoshin** 02:52 Okay, because I see the, Slack thread that you want to move it to the server.
**Christos Markou** 03:00 No, no, it was not decided, so, actually it was…
One of the topics I wanted to discuss today.
Since we have it anyways.
**Dmitrii Anoshin** 03:12 We can run Doodle, that's a pretty nice tool to figure out sometimes. That works for most of the people.
Have you tried?
**Christos Markou** 03:21 Yeah, I had, the thing is that the calendar is also a bit packed, every…
like… early morning or late evening time for Europe.
So… It's either, SpecSIG, or it's also Entities SIG.
the TC meeting on Wednesdays.
**Dmitrii Anoshin** 03:50 And it's supposed to be moved to Monday.
**Christos Markou** 03:55 Okay, so probably… These can be used.
**Dmitrii Anoshin** 03:59 Actually, actually, it used to be on Thursday, now it moved to Monday. Anyway, this time works for me, half an hour of this time works for me, and Tuesday, pretty much any time.
Not anytime, but most work for me.
**Christos Markou** 04:15 What about Tuesday? 30 minutes earlier, so same hour as, the system, same config, I guess.
**Dmitrii Anoshin** 04:26 Yeah, that's work for me. Yeah, I am.
**Christos Markou** 04:29 Okay.
I think David, works for David,
**Dmitrii Anoshin** 04:35 Sure, but you know, she might be not that…
Happy for the early meetings, but we'll see.
**Christos Markou** 04:42 Yeah, okay, okay, I can… let's wait and see if we cannot…
Use this time, we can run it to the then.
Okay, so… Yeah, I guess we can keep it short, we can just…
Let me start the recording.
Just in case. It is recorded already. Cool. So… for…
Apart from the meeting time, ideas, I can comment there.
Aww.
There we go.
Okay, I will comment back on the issue, and I'll check.
Taking, you know.
Yeah.
what else? And then, the next one, I will share my screen, just to…
showcase this. I started, created an issue today, I think it's,
proper timing for us to start discussing this.
in order to propose to stabilize the first metric for Kubernetes metrics, I think the most straightforward one is the odd CPU time.
And I list here the…
the items that we need to cover for this to happen. So, if I remember correctly, Josh…
had mentioned, either in vSig or in the other one, SystemSig, that,
For a metric to become stable, also the,
attached entity or the related entity should be stable, so… Yeah.
I filed an issue to stabilize a gates pod entity as well.
**Dmitrii Anoshin** 07:01 Question here. Why do we want to stabilize that metric? I don't think that metric should be enabled by default. Why not container CPU time? Because container CPU time gives you, like, lowest granularity, right?
**Christos Markou** 07:15 And potentially, this metric might be opt-in if we have.
**Dmitrii Anoshin** 07:19 Container CPU time required.
**Christos Markou** 07:23 So… yeah.
Because… okay, because it is kind of included, right?
**Dmitrii Anoshin** 07:30 I mean, look at CPU time is just, just, like…
If you sum up container times, you'll get both spill time.
It's like derivative metric, essentially, from containers period time.
**Christos Markou** 07:47 Yeah, one reason is that, the… this one is…
100% related to a Kubernetes entity, the KHPod.
If we want to stabilize, container CPU time.
**Dmitrii Anoshin** 08:04 Yeah.
**Christos Markou** 08:05 Then we need to stabilize the container in.
**Dmitrii Anoshin** 08:07 I see. I'm okay with stabilizing this one first, but stabilization doesn't mean that metric becomes required. It still should be opt-in, right? And is it opt-in right now?
**Christos Markou** 08:21 I don't think so.
**Dmitrii Anoshin** 08:24 I just wanna ensure that we are not, like, making…
metrics that provide the same data required. That's kind of… that doesn't make a lot of sense to me.
**Christos Markou** 08:38 Yeah, we can… yeah, that's a valid point. We can…
We can check this, hadn't…
**Dmitrii Anoshin** 08:44 Thought of this.
But yeah, if it's opt-in, I don't see why we cannot stabilize it first, it's fine by me.
**Christos Markou** 08:53 Is this the same with, Kate's node CPU time as well?
kind of…
**Dmitrii Anoshin** 09:05 Probably, yes. So, if you… I'm not sure, actually…
If… if it's derivative, because potentially there might be some Kubernetes system-specific CPU
time included there, CPU cycles, like, for, running Kubernetes itself.
If it's included, it means that it's a different metric, you cannot get it from container, but if it's not, if it's just a sum of container metric, in that case, yes, it's pretty much the same thing, so we need to figure that out and see in the description. Clearly, you need to define that in the description as well.
**Christos Markou** 09:49 Yeah, yeah, I see.
Okay, yeah, I will, take this into account.
And, yeah, we can discuss this as part of this issue. For now, it's just filing the, the intention, so no real progress. However, for, the entity itself, there was a discussion already. I had the impression initially that
So, for, identifying attributes,
One is Kubernetes pod UID, and then initially I thought we will need something like Cluster UID, but I had the impression that it's not quite unique.
But I found, also, David, commented there, and I found out that we already in the registry, mentioned that cluster UID is extremely likely to be unique.
**Dmitrii Anoshin** 10:50 So, just to clarify, entity… identity is not supposed to be globally unique.
Entity identity is only, like, at minimum unique within its, within its, environment.
And pod, like, next entity on top of pod as an environment would be Kubernetes cluster. So we only need to ensure that pod is unique within the cluster. So we don't need to bring a Kubernetes cluster here, because it's from a completely different entity, it's unrelated.
**Christos Markou** 11:26 Okay, yeah, I mentioned there that,
Yeah, probably it's already solved, because a pod belongs to a cluster, in a way. Do we have… do we explicitly, mention or link entities to each other? So…
**Dmitrii Anoshin** 11:46 We will be, going forward, yes.
**Christos Markou** 11:49 Okay, okay.
**Dmitrii Anoshin** 11:50 We, like, right now, like, all the, let's say, chain of entities would be added.
So, if you emit… Pod…
pod metrics, you would… you would include pod entity and cluster entity as well, but they will be separate entities.
**Christos Markou** 12:11 okay. This will happen from the… okay, will happen from the implementation.
**Dmitrii Anoshin** 12:17 Yeah, you don't need to specify that here, like, which metric goes to a particular entity. We need to, specify, like, which immediate entity is responsible for the metric, let's say.
So, a cluster is kind of an additional entity.
**Christos Markou** 12:35 All right. So for now, we can move… not…
Move on, not a stabilization, but we can at least…
define their roles here, and have only audio ID as the identifying attribute, and the rest, will be descriptive, right?
**Dmitrii Anoshin** 12:55 Right.
**Christos Markou** 12:56 Okay. Do you think we should wait for this, like, correlation… linking mechanism? Will this mechanism will happen… will be part of the semant conventions, or something else?
**Dmitrii Anoshin** 13:10 No, I think…
For semantic conventions, we need only immediate entity. Define immediate entity for a particular metrics. That's my understanding. We can talk about that with Joe, that's a good question, but I believe that's… that's what we have currently.
**Christos Markou** 13:31 we don't…
**Dmitrii Anoshin** 13:32 In the data model, currently, unfortunately, we don't have a way to specify, like, we have a…
list of entity attached to the resource, but we don't have a way to specify which… Let's say…
which entity is immediate for all the metrics. So we potentially need to solve that on the data model side, but for now, for semantic conventions, we don't need to think about it.
**Christos Markou** 14:02 Okay, alright. Yeah, let's give it some time then, if anybody else wants to comment there. I can send the PR for this change already, I guess.
Cool, sounds good then. I think that's all I had, and
Yeah, that's pretty much it, yeah.
**Dmitrii Anoshin** 14:25 Oh, by the way, I was expecting to see you on the… as nominee for GC.
Have you considered?
**Christos Markou** 14:33 Yeah. No, no.
at least not now, I think I still have to… I still want to, like, do…
**Dmitrii Anoshin** 14:44 technical stuff. Work on… do some engineering, some real work. Yeah, yeah, yeah, yeah, yeah.
**Christos Markou** 14:49 No time for retirement ends. Yeah, going to politics. Makes sense, makes sense.
**Dmitrii Anoshin** 14:55 Yeah, okay.
**Christos Markou** 14:57 Okay, thank you. Thank you, Christy.
Serum, bye-bye.
