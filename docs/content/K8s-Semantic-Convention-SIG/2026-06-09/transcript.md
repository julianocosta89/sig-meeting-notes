SIG: K8s Semantic Convention SIG
Date: 2026-06-09
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang** 02:14 Bye.
**Dmitrii Anoshin** 02:18 Of course.
**David Ashpole** 02:18 Okay?
**Stephen Lang** 02:23 So, Chris is out.
Today.
**David Ashpole** 02:25 Oh, Chris, it's out? Okay. Do we have, any topics?
**Stephen Lang** 02:29 The agenda was empty, I just added… One thing, just about a comment on what I mentioned last time.
For workload type and name.
Just to… Kind of notify if anybody wants to… follow-up. David, I know you've commented on this issue before, and you actually said that, Or is it You said you liked the idea of the K8s regarding kind?
Maine?
This is… so this is for… to recap, this is on, K8s.
Pods, for example, where I have all sorts of different workloads currently, which is kind of hard-coded to the five, sort of, standard types, In terms of having… I don't know, custom resources or, you know, other workload types.
It might currently involve, you know, adding… Couple extra attributes every single time.
I'm hoping… my suggestion is that maybe we can add a couple of generic ones. So, I don't know, David, when you said KH.regarding.kind.name, is that a dynamic name, which would be, like, a different Sort of attribute per type and vendor, etc.
**David Ashpole** 03:52 Let's see, so I'm trying to remember what was in my head in.
**Stephen Lang** 03:56 Yeah, I mean, obviously you don't have to answer now, but just to kind of let you know that this is… I finally sort of put my thoughts together, let me share as well.
**David Ashpole** 04:07 I see, so this is for… so this is specifically for Kubernetes events, right? So the question, I think, is… You get a Kubernetes event, all it has is a regarding.kind field.
And it gives you the name and the UID of whatever the resource is. So the question is.
when we get a Kubernetes event for a pod.
What should we set on it?
And I think my response was, I would like to see… the… whatever is parsing that event actually set case.pod.name.
Not just always kids.resource.name.
Yeah. I think there's something to be said for…
**Stephen Lang** 04:55 I'm not tracking the source of where this thing came from.
**David Ashpole** 04:58 I think there's something to be said for having an opt-in set of attributes for workload.
Name and type.
NUID, maybe?
But I would say that that should be in addition to the… existing ones that everyone's joining on, right? I feel like the base… the base ones that everybody actually needs today, and that show up in all the UIs and stuff, are the case. You know.
statefulset.name, or whatever, right?
**Stephen Lang** 05:28 Yeah, yeah, I'm kind of fine with those. It's just, so the use case that I posted was in the case that you want to For example, counts the number of unique workloads by pod.
I mean, this is kind of based around metrics. I don't know if this issue is specifically scoped to events only.
Or if the… if it's the same kind of SEMCOMF that applies to… to both.
**David Ashpole** 05:51 I…
**Stephen Lang** 05:56 Because just in the case of, like, the current metrics, as I see them, if I collect them in Prometheus, I know all the…
**David Ashpole** 06:04 Yeah, I think the current scope of this issue is… What do you do when you have a resource?
a Kubernetes resource.
which is not in our list of official resources in the Semantic Conventions. So that's…
**Stephen Lang** 06:19 Okay.
**David Ashpole** 06:19 I see that the core question is, I got something for a… Like, horizontal pod autoscaler.
what attributes should I put on that? And I think the answer is… You should use the regarding.kind field.
to construct the attribute name, right? So it kind of, like… maybe, hopefully, prevents us from having to actually enumerate every Kubernetes object in existence.
**Stephen Lang** 06:46 Newark.
**David Ashpole** 06:46 interventions, right? I think… I… I do think that separately adding case.workload dot name and workload.uid, or the other thing I could see would be case.
like, top-level controller or something like that. Like, as long as we can define it, where it's like, you go up your owner refs until you can't find an owner ref anymore.
Something like that, then… then I think, as long as we can define it, then I also support adding those probably as opt-in. I'm not sure what you think, but I tend to think that anything that's, like.
duplicative.
People are gonna complain about cost unless it's opt-in.
But I would, I would open a separate issue, and I think you're, your CompQL query.
Is, a good example of why it would be useful, so… I would support that.
**Dmitrii Anoshin** 07:44 No, that's good.
**Stephen Lang** 07:45 Yeah, because I suppose, like.
Just one last thing is, in Prometheus world, you know, we would put this into a recording rule and maybe forget about it.
**David Ashpole** 07:54 Yeah.
**Stephen Lang** 07:55 But I don't know if in the hotel world, just because… you know, we have so many more attributes, and we can be that much more expressive if maybe those generic attributes would just make sense. But I can certainly move this Into a separate issue, if it kind of falls outside of what this original issue was about.
**David Ashpole** 08:13 Yeah, yeah, I… Let me… I'll just post a comment here, just to make sure we capture it.
**Stephen Lang** 08:20 Thanks.
Sorry, Dimitri.
**Dmitrii Anoshin** 08:23 Yeah, Kubernetes Cluster Receiver will already send that kind of, like, let's say, opt-in attribute, it's called gaiters.
workload.kind, and ktest.workload.name, as far as I remember.
But they are not set as a resource attribute, they are sent as additional entity events, which is something, like, still experimental, and we are working towards stabilizing that. But potentially, this can be also emitted as… Obtain resource attribute.
Like, we will make it.
In a, like, configurable in a way that it's always sent as entity events.
But it can be opt-in as a resource attribute.
**Stephen Lang** 09:20 Okay, and is that… so you said about events, is this… would it apply to… Metrics as well, or are you just talking about…
**Dmitrii Anoshin** 09:28 Yeah, I'm talking about… entity events. It's like, it's actually not Kubernetes events. It's, entity events, it's, let's say, additional metadata that we send, or that would be applicable to the metrics, mostly, but to anything else as well.
And, yeah, this is, like, a new thing that is being developed,
**Stephen Lang** 09:51 Okay.
**Dmitrii Anoshin** 09:51 in OpenTelemetry. So, like, end entity, essentially, it's, like, extension of a resource, because currently the problem with the resources, currently, it can have several entities, and you don't know which one is actually associated with the metric. Let's say you can have put that name, put the UID, namespace, that, that name, that UID, or, like, or node as well, so, like.
all of those kind of separate entities, they are combined in one resource, so this is one of the problems that EntitySeq is trying to resolve, but also another problem is how to deliver more, let's say, more metadata associated with particular entities.
That metadata that cannot be sent with the… with the resource attribute, because it's, like, either… it's too, like, low.
Big, like, let's say, Values are big, or whether it's churning too, too frequently, so something like that.
Okay. And one of the… things. One of the good examples of metadata that is being sent with entity events is actually, let's say, pod labels and put annotations. You don't want to put all of the labels to the resource attribute, you don't want to put annotations, of course.
**Stephen Lang** 11:15 Okay.
Nope.
**Dmitrii Anoshin** 11:23 So, yeah, if we want to standardize, and we want to have… we want to introduce a workload, let's say, entity, or, like, semantic conventions and augment telemetry, we should look at what's already been sent by KATS cluster receiver.
**Stephen Lang** 11:41 Okay.
**Dmitrii Anoshin** 11:42 I don't think it's… it's defined in semantic conventions yet.
**Stephen Lang** 12:14 Well, that was the only thing that I had.
And I don't know if anybody else has got anything they'd like to discuss?
**David Ashpole** 12:24 How are we on the migration?
Are either of you involved in that? I know that we were talking about Feature gates a month ago.
**Stephen Lang** 12:34 I haven't been involved.
**David Ashpole** 12:36 Okay.
Okay.
Well, if there's nothing else, then, we can drop. I just posted the comment, so hopefully that…
**Stephen Lang** 12:52 Thank you for that.
**David Ashpole** 12:53 Yep.
**Stephen Lang** 12:54 Appreciate it.
**David Ashpole** 12:56 Alright. Alright, thanks guys.
**Dmitrii Anoshin** 12:58 Thanks, folks.
**David Ashpole** 12:58 In two weeks.
**Stephen Lang** 12:59 Right.
