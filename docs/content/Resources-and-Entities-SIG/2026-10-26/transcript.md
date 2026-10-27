SIG: Resources and Entities SIG
Date: 2026-10-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 00:47 Hey, folks, how are we all doing?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 00:51 Hello, Joe Doing goods, how are you?
**Josh Suereth (Google LLC)** 00:56 Not bad, not bad. I, I think I forgot to tell this SIG when I took vacation last week. See, we canceled.
Alright.
All right, I think, we might have some folks coming, but let's, let's get through… Oh, let me do this first. Let's do 10 beans… Agenda. Feel free, folks, to add your agenda.
Items, but let's get through some of these open questions.
Yeah, this… do you mind if we do this one first, krajo? Because I think this is the easiest answer.
**krajo (Grafana Labs)** 01:54 Sure, yes.
**Josh Suereth (Google LLC)** 01:56 Okay.
Because I think the other ones might be longer. So basically, TLDR is if you drop an identifying attribute, you can preserve attributes on the resource.
you just drop the entity reference. So, like, all of the other attributes, you can still leave if the user wants them.
You just drop the fact that they're part of an entity. They become raw attributes.
So, like.
We have this notion of an entity, and we have this notion of, like, a resource with extra attributes.
If folks are dropping the identifying attributes of an entity, but they want to keep the other ones, that's fine.
It's just, it's no longer tied to an entity. So, like, you don't have to drop all the attributes, right? That's… that's a… I can show you in the spec where we have that.
**krajo (Grafana Labs)** 02:44 Yeah, I think you might be… Misunderstanding a little bit.
what drop means.
So, yeah, so adoptive diametry is a way to reduce your coordinator.
So what happens is that we drop the attributes and then aggregate those time series into one time series.
So, by taking the sum, or the max, or average, or whatever, of the… Of the time series. So there will not be, like, separate time series anymore, where you can keep those attributes.
**Josh Suereth (Google LLC)** 03:18 See?
**krajo (Grafana Labs)** 03:19 So, I… yeah, sorry.
**Josh Suereth (Google LLC)** 03:21 Yeah, so you're taking, like, max of something, right?
**krajo (Grafana Labs)** 03:23 Yeah, exactly.
But most likely it's a sum, because of cumulative counters, but yeah, that's the…
**Josh Suereth (Google LLC)** 03:30 Yeah, that would imply… yeah, so that's a good use case of, that's one of the things we're hoping entities could help, actually, is, like, when you do aggregation of that fashion.
You could, you're now aggregating at a different level, so you can decide you could have a simple aggregation that just aggregates and says, I want everything aggregated at the cluster level, and you know exactly what attributes to drop.
Yeah.
**krajo (Grafana Labs)** 03:52 Yeah, I thought so too, because right now, you would have to, you know.
Say, all of them, like, specify all of them, and this way you could do it simpler.
Yeah. Nope.
**Josh Suereth (Google LLC)** 04:03 Yeah. Cool.
Anyone have any questions on that?
Let's move on to this next FYI-based discussion here. You want to talk to this one, Kreya?
**krajo (Grafana Labs)** 04:17 Yeah, yeah, I, I… put this as FYI, they are, you know, in the primitives SIG, but I thought you'd want to know our progress.
So, last… Yeah, the last meeting that we had, we talked a lot about, you know, identifying attributes and different levels of them and whatever.
And what we agreed Like, especially on… on that meeting, is that… We shouldn't drop them when we convert.
from, from OTRP to… to Prometus, because right now, there's… The identify attributes are… considered the service name and service instance ID, and they are put into Job and instance, and they are kind of lost, unless you set this configure, parameter.
And then we agreed that, no, no, that's… that's kind of done. We should always have… these identify attributes. Even if it may… takes a little bit of effort to join through the JobN instance to get them, they should be there.
But unfortunately, this is a breaking change.
To enable this, so this is going to go into 4.0 parameters. We'll flip the default.
**Josh Suereth (Google LLC)** 05:33 Great.
**krajo (Grafana Labs)** 05:33 Wow, wait.
**Josh Suereth (Google LLC)** 05:35 Prometheus 4.0 already, you guys are moving fast.
**krajo (Grafana Labs)** 05:39 Yeah, we got kind of, you know, it… People thought that we didn't do anything, because it took such a long time to do 3.0, so now we already announced at PromCon that next year we'll do 4.0.
**Josh Suereth (Google LLC)** 05:52 Okay, I mean, that's awesome. Okay.
**krajo (Grafana Labs)** 05:55 Cool.
**Josh Suereth (Google LLC)** 05:56 Yeah, so this looks like it still needs some more… like, it looks like the Prometheus folks have approved, it just needs some more, spec approvers. So, folks here who have spec green checkboxes, like myself, I'll take a look, I'll leave that open.
Awesome.
And then one more, FYI. Experimental Basic Entry Support in Prometheus, this is cool.
**krajo (Grafana Labs)** 06:20 Yeah, and since Arve is here, I think I'll just hand the microphone to him.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 06:25 Yeah, sure. I'll just, opened this PR to… To add support, to add experimental support for, For deriving… resource identity from entities, if… if entities are contained.
In, then, when interesting OTLP.
So, this… There's one question that remains, which is, Which is whether an entity type should be part of, the, The resource identity hash, because what we do is we make a hash from all the… identifying research attributes, and then there was the question as to whether we should also include entity types. Yeah, do you perhaps have an answer to that, Josh?
**Josh Suereth (Google LLC)** 07:29 Yeah, I think… I think you probably do want them somewhere, So, like, right now, entity type and, like, the prefix of the entity IDs are the same.
So it does feel like duplicate information, but, it depends on whether or not you're going to let people kind of sort on entities or that, because how are you storing? I'd have to look at the details here.
Your instance, job instance to identify, everything goes to the target info, right?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 08:08 If everything goes into the target info.
**Josh Suereth (Google LLC)** 08:11 Yeah, like, the underlying information… I think you will want to know the type of entity, because people want to sort on it, and they'll want to, like, filter by things that are… have entity X, right?
But what I'm not… what I'm not sure of is, like, service… the service entity, for example, right?
Are people going to say, I want things that have a service entity, or are they going to say, I want things where service name is equal to X?
when they make Prometheus queries. That's… that's… I'm trying to turn your question into, how are people going to use it in Prometheus? Like, what are the use cases?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 08:45 Yeah. Well, at the moment, there's… there's no support for actual entities in Prometheus, and so that… I think… I think we're not going to have that until we have, potentially native metadata. So the… so the question now is, is only How, how do we generate the, the resource identity hash?
So that, that hash,
**Josh Suereth (Google LLC)** 09:14 Oh, whoa.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:14 It goes into the instance label.
**Josh Suereth (Google LLC)** 09:18 Yeah.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:18 So the instance label is both put on time series, which are generated for resources, and on target info time series.
**Josh Suereth (Google LLC)** 09:29 Right, and so the question is, do we need the type in the hash?
I don't.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 09:34 Yes.
**Josh Suereth (Google LLC)** 09:35 We do, given the guarantees we put on resource, but I'm actually gonna check with Dmitri on that.
So if we make a unique hash to uniquely identify a resource.
from the entities in it, the identifying attributes. I don't think we need entity type, because we guarantee that when we've merged a resource, that the keys are unique. But what do you think, Dmitriri?
**Dmitrii Anoshin (Splunk Inc.)** 10:00 There is one edge case when we have an entity with the same identifying attribute, but it's… I don't think that's something that we… agreed on, anyway. So, if we assume that every entity Would have its own set of identifying attributes distinct, then we should be good.
Okay. Does that make sense? Because, like, if we say that AWS instance as an entity, would use host ID?
identify an attribute, that… in that case, it's kind of… we lose some information here, right?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 10:38 I, I found an issue by Tigran, and it, it's, it's called, is type part of Entities Identity?
**Josh Suereth (Google LLC)** 10:48 Is that linked here?
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 10:50 I can… yes, it is linked via comment, but I… and I stuck it in the Zoom chat.
Do you see the link?
**Josh Suereth (Google LLC)** 10:59 chat.
Yep, I got it. Let me open it.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 11:06 So So I think Tigran's question in that issue is more abstract, sort of.
So I don't… so I think his answer is actually yes, like, it was determined on… on February 27th, 25.
**Josh Suereth (Google LLC)** 11:24 That's part of the identity. Yeah, we should, we should stick with that then, because… Yeah.
It's accepted.
Type field is not part of identity, then any bug example required that the entity describes the collector. Right.
And I think… I think for the purpose of a lot of the things we're doing, we should we know that there will probably be conflicts, and even if we resolve them in resource, it's probably good to have an independently unique ID, right?
**Dmitrii Anoshin (Splunk Inc.)** 12:08 Yeah.
**Josh Suereth (Google LLC)** 12:11 So let's… let's include it as part of… like, we agreed on this a while ago, let's, I don't know if this is formally written down, I think it is kind of.
Let's… Let's check.
I think when we talk about identifying.
We have type defines the type of the entity, must have changed, for example, host.
Minimally sufficient ID we talk about. Yeah, I don't think we actually call out that… Identified attributes and type… form an ID to… like, an independent hashable ID together.
**Dmitrii Anoshin (Splunk Inc.)** 13:07 If an entity doesn't provide a global set of identifying attributes.
**Josh Suereth (Google LLC)** 13:13 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 13:14 like, the global scope, I think it's important to… Type is part of the cache as well, as well as… like, scope entity if it's not global. Actually, this is part of my thing.
Next topic, we can discuss.
**Josh Suereth (Google LLC)** 13:33 So we… yeah, I assume we'll be talking about it more. I was just trying to see if we have this written down for you anywhere. It's implicit in the spec, right? Because when we talk about identity, minimally sufficient identity, basically type and ID make up the identity together.
And when you look at, like, our merge algorithm, right, you can only merge things that have the same type, which is how we are doing identity.
But we… So, I'll say this, Arve, if you think we need to, like, write in our spec anything for your PR, like, let us know, because we can open a spec thing to make it crystal clear, but I would say, for the purpose of this discussion.
100%, you should include the entity type.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:20 Okay, yes, I thank you for that answer, and I think it should also be made explicit in the spec, because… Because my search for an answer in the spec was actually what led me to find Tigrant's issue.
So I think, I think, Tigrants industry is the only place where it's actually, explicit.
**Josh Suereth (Google LLC)** 14:46 Yep.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 14:47 So, that would be very helpful. Thank you very much.
**Josh Suereth (Google LLC)** 14:50 Okay.
I'm gonna add this to me temporarily, but Dmitrii, you might already be handling this in your VR, so let's, Are there any other open questions here?
Before we move on.
to identity scope.
**Dmitrii Anoshin (Splunk Inc.)** 15:08 We have it at the end of…
**Josh Suereth (Google LLC)** 15:14 Okay.
**Dmitrii Anoshin (Splunk Inc.)** 15:14 Girl, Phil, put you on the mute here.
**Josh Suereth (Google LLC)** 15:15 Alright, Dmitrii, take it away.
**Dmitrii Anoshin (Splunk Inc.)** 15:17 Sure.
**Josh Suereth (Google LLC)** 15:25 Do you want to drive, or do you want me to just poke around while you're talking?
**Dmitrii Anoshin (Splunk Inc.)** 15:27 No, you, you can, you can drive it. So, essentially, this is a revamp of my previous PR, and… I guess the biggest difference here is that Suggesting, like, clear definition of the entity's scope.
So we are not confusing whether entity isn't.
So, there are multiple states of entity scope, whether it's, clearly a global identity. For example, if it's used as your UID, yes, we can assume that it's globally unique, specifically for Kubernetes, when it's called UID, because even if you have cluster on top of that. Cluster unique identity is still based on UUID, which is generated within the same cluster, so it kind of doesn't make sense to make Pod, pod, pod being, unique, saying pod unique within the cluster, because cluster is also… use the same algorithm. So we can assume that both is globally unique, but others might not be, and if they are not… we are not certain that they are globally unique.
We… like, we cannot distinguish whether we don't know the entity, scope entity, or we're just saying that… Yeah, like Teresa's. Anyway, sorry, I'm rambling. I just wanted to clarify that my proposal here is that we say… We introduced the new ID scope.
Attribute being put, filled.
being said on the message of an entity, explicitly saying whether we don't know what's the scope, it's unspecified, or whether it's global, or whether it's local. And if it's local, it has to know which scope entity type it is part of… even if the scope entity isn't part of the same resource. That's how we make this, like… that's how we disjoint them.
That was the, like, one of our H cases and problems that we tried to resolve before. When we say that process, I know that I'm a process.
But I don't know anything about host. I can say I'm a process with a local identity, and the scope being host. And then host as a separate entity will be added later.
And that, like… To the same resource.
So before, I was saying that if it's local entity, and if we have a reference to a scope entity, that scope entity has to be on the resource, and now this PR makes it different. It says that you can have And local identity with the type of scope entity being specified by scope entity isn't necessarily beyond the resource yet.
And if it's… if it's not there at all, if it's not added by any resource detection processor or anything, it means that it's kind of invalid, it's unspecified entity in that case. Does that make sense?
Sorry, like, wasn't very clear.
**Josh Suereth (Google LLC)** 18:54 No, it… I get… I get what… so basically, there's two changes here. One is, you have an ID scope, which is either global or local, or unspecified.
**Dmitrii Anoshin (Splunk Inc.)** 19:03 Yes.
**Josh Suereth (Google LLC)** 19:04 And then you have a scope entity type, which is, like.
I am unique within the scope, and someone has to fill out that scope for me to be unique.
So, here comes the hard question, right? Can you… Cause I… it would be helpful in the PR if it's not already there, because I… sorry if I didn't read through all of it yet.
can you have examples for all of our known OpenTelemetry detectors today, right? Because, what I want to make sure of is if I write a host detector, and I write it in Java.
**Dmitrii Anoshin (Splunk Inc.)** 19:41 Yeah.
**Josh Suereth (Google LLC)** 19:42 what am I putting for my scope?
If I write a process detector in Java, what am I putting for my scope? If I have the same detector in the collector, what am I putting?
I think… I think this might work, but it does mean that, like, the hierarchy You know, when you define process, you have to know about scope.
So that I can… Got fantasy time, right?
**Dmitrii Anoshin (Splunk Inc.)** 20:05 so you don't have to know the scope itself, like an instance of the scope, but you have to know type of the scope which you are in. And I think that's an easier question to answer, rather than… knowing the exact instance of this code. Does that make sense? So this is, like, this is the biggest change, I guess, in this PR, essentially.
**Josh Suereth (Google LLC)** 20:27 And this, this does lock down the hierarchy then. So, like, we would say process is scoped to host.
**Dmitrii Anoshin (Splunk Inc.)** 20:33 Yes.
**Josh Suereth (Google LLC)** 20:33 And it's never scoped to container.
But a container and a host could be the same thing.
**Dmitrii Anoshin (Splunk Inc.)** 20:40 I mean, yes, it… I think, like, technically, it's possible to figure it out, even on the process level, if it's… if you are, like, taking this, like, process namespace, you… you can read that, and you can figure out whether it's container or not. I may be… I may be wrong, but that was my understanding. But you do not necessarily know about anything about the container in that case, so there must be another detector that would pull that data.
So, I get your point, I probably need to be more specific with the examples, because currently, in abstract, it's very hard to reason about.
**Josh Suereth (Google LLC)** 21:21 Right. If you want the hardest example in my head.
that I use as my litmus test for modeling. And again, this isn't the hardest possible example. I think the networking folk have more interesting things, but, let's have a process that's running on a container, that's running on a VM, That's running on a hypervisor that's also a host, right? Like, let's… that's… to me, that's the chain of doom that we… oh, and that hypervisor's part of a cluster.
Yeah. Right? So let's… and, like, there's Kates in there, there's physical things in there, there's virtual things in there, like, that to me is the… if we solve that, and we're happy with what it looks like and all these detectors, I think we can handle, you know, 99% of what OpenTelemetry's gonna throw at us, except networking, it might get a little more exciting.
**Dmitrii Anoshin (Splunk Inc.)** 22:09 Yeah.
I've been trying to… like, separate them as much as possible. So, like, if you have one detector responsible for the host, it doesn't have to mutate all of the other. That was, like, my main goal of this idea. And this is, like, the closest I could get to it.
**Josh Suereth (Google LLC)** 22:32 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 22:32 it might not work still in some particular edge cases, but I'll… yeah, let me try to… go through those usage cases and see how it will play out. But it's… potentially, we might need to say, hey.
Oh, if it's, if we have entities with unspecified host.
Some, like, detector might be responsible to fixing those entities, even if they are not, like.
So, let's say I'm a host detector, I'm responsible for creating host entity, for specifying it, its identity and everything, but I might be also responsible for, let's say, fixing ID scope-only field.
In other entities, like process, or, like, container, or something like that.
**Josh Suereth (Google LLC)** 23:26 So, so this was…
**Dmitrii Anoshin (Splunk Inc.)** 23:27 turns.
**Josh Suereth (Google LLC)** 23:28 Yeah, yeah, my counter… so right now, you have the arrow going out, right? So it's always from the tiny thing to the big thing.
**Dmitrii Anoshin (Splunk Inc.)** 23:37 Yeah.
**Josh Suereth (Google LLC)** 23:38 Which, I think is how we want to do events in general.
Another alternative would be, you could have the arrow go in, where, like, the host would say, I can contain processes.
**Dmitrii Anoshin (Splunk Inc.)** 23:50 Yes.
**Josh Suereth (Google LLC)** 23:51 The problem there is, you know, a host could contain lots of things, and it might have to, like, all of them.
**Dmitrii Anoshin (Splunk Inc.)** 23:56 Exactly. So…
**Josh Suereth (Google LLC)** 23:58 Yeah, so I see what you're going with there. I think what you have might… work, like, across the board. So I just want us to actually do the modeling and, like, draw it all out so people can see it.
That thing you had where, you know, the detector could actually correct things.
what I'd love to see is if we, instead of having the detector do it, if we had some way to make the SDK or the collector components do it, you know, on your behalf, so it's not… so it's easier, you know what I mean? So, like, it's consistent, it's not a… So we have an algorithm that's… that is easy to reason about, is kind of what I'm going after.
I like what you have, where, assuming we can… Assuming we can fill this out everywhere, successfully, this is dead simple now.
Right? It's really easy to figure out that line and that chain and everything. So I do really like that.
I just want to make sure we can fill this out in all the scenarios we have.
**Dmitrii Anoshin (Splunk Inc.)** 25:02 Okay, yeah, if we… if you think we can make it the opposite way, like, host being… host entity would specify all of its children, essentially. It means that we… we would have to stick to particular order of detectors being applied, and I don't know if it's something we want to…
**Josh Suereth (Google LLC)** 25:32 Well…
**Dmitrii Anoshin (Splunk Inc.)** 25:33 Always.
**Josh Suereth (Google LLC)** 25:34 Sorry, krajo has his hand up. Go ahead.
**krajo (Grafana Labs)** 25:37 I mean, don't you already kind of define the order of the detectors in the configuration? That was my impression, that you kind of set that order. So… In my naive view, the SDK puts in… you know, I'm a process… Unspecified scope, and then the chain of… Detectors can update that.
Seems… Well, maybe too simple, but that's… You know, what I've… Would find kind of natural.
**Dmitrii Anoshin (Splunk Inc.)** 26:13 If we go with this approach, yes, we would have to stick to the order anyway, yes, if we need to apply the scope.
If we have… we would have to make host detector being responsible for… for setting the scope of other entities as well.
But I was thinking… for example, in the collector, you can define detectors in any order, and Potentially, we can just… Yeah, we can… we can work around that, I guess. We can make sure that any order you specify, it will be all… Devil owes.
apply.
They are the scope.
I don't even know why would we need this. Oh, we have a different order, because we have other… we have overlapping attributes.
Some of the detectors would write to the same attributes right now, and One of them is host AD, essentially, actually.
**Josh Suereth (Google LLC)** 27:19 Yeah, host ID is still problematic. We still need a plan for host ID.
Yeah, I think if we write some examples down, I think I like this.
Because not a lot changed outside of… You're forcing the scope to be the same?
For merging.
**Dmitrii Anoshin (Splunk Inc.)** 27:46 Right, I think it's necessarily right, because otherwise… They are not mergeable if they have unspecified score.
**Josh Suereth (Google LLC)** 27:56 Oh, if one knows the scope and one doesn't. I don't know, though, is that… is it… That means you can't merge, but would you pick one?
Like, what if, so, the AWS thing that detects a host would actually know That it, like, what its parent might be, but the actual regular vanilla host one might not.
Again, this is where I think we want some examples.
**Dmitrii Anoshin (Splunk Inc.)** 28:30 But this one is for merging the identifying… or not identifying attributes of the same.
**Josh Suereth (Google LLC)** 28:35 encrypted.
**Dmitrii Anoshin (Splunk Inc.)** 28:35 Right? Descriptive attributes, yes. So, in that case, it depends on how… what entity… what identity of the entity we say.
right in that case, like, the type we discussed before, identifying attributes, set. And I think… scope would be part of that as well. If it's global scope, it's like, nope, but if it's local scope, identity of the scope entity would be part of that.
Identity of this entity, that case.
**Josh Suereth (Google LLC)** 29:07 You're right.
We only do this check if it's a local scoped entity.
**Dmitrii Anoshin (Splunk Inc.)** 29:18 Yes, right, right.
**Josh Suereth (Google LLC)** 29:19 Right, and if it's, what did he call it? If it's un… if it's unspecified, we treat it as global.
**Dmitrii Anoshin (Splunk Inc.)** 29:26 That's a good question. I don't know, I think I wrote it here that we don't… they are not mergable in that case.
**Josh Suereth (Google LLC)** 29:34 Yeah, you have unresolved identity.
and a consumer that receives one must treat the identity as unresolved. Unresolved entity is still valid and still describes object and consumer. Meetings correlates signals, must not treat the identities, local identity as global. Okay, that's safe.
That makes sense.
**Dmitrii Anoshin (Splunk Inc.)** 30:00 Should not nourish him.
I mean, should not, but potentially, if you have… if you know that you are working within some kind of isolated environment where You can treat all unspecified entity as global within that environment.
**Josh Suereth (Google LLC)** 30:20 Yeah.
Current reports NC, and different reports enthi that scopes it.
Yeah, it's such a teacher resource, because it locates new spaces, not block user screen.
Service email… Search that knows the cluster completes the chain by adding Kate's cluster. Yeah, this makes sense to me, right? So, like, what we're saying is, if you get Kate's namespace name, you cannot treat it as a global identifier, because it's not, and… and you don't know, like, you don't have the rest of the context to make it be global.
Until the cluster shows up. Okay.
And you can correlate, because you can use the namespace name to correlate between signals and join across them.
Because sometimes, yeah, and then… We should not merge another resource. If someone has a different Cates namespace, we don't know if it's actually the same.
Alright, I'm on board with this now.
I… I… I… yeah, I get your merge changes. I think… I think you're right. This… this ties in with both of those decisions.
**Dmitrii Anoshin (Splunk Inc.)** 31:29 Cool. Yeah, I'll add more examples.
I think through which cases. Cool.
**Josh Suereth (Google LLC)** 31:35 And then everyone here, please do, like, a full review, because we can, Get some comments in, and maybe… I don't know, Dmitrii, do you think this is worth talking about in the spec meeting tomorrow, or do you think it's way too early for that?
**Dmitrii Anoshin (Splunk Inc.)** 31:50 Hmm.
Maybe, let me give examples, I'll see if I can do it by tomorrow.
**Josh Suereth (Google LLC)** 31:57 Yeah.
Oh, here's a question.
Do you think the scope is going to be different?
Even within an entity, or do you think it's always going to be the same for an entity?
**Dmitrii Anoshin (Splunk Inc.)** 32:19 Or entity type, you mean, right? It's… it's…
**Josh Suereth (Google LLC)** 32:21 Oh, sorry, for entity type, yeah. Like, for hosts.
**Dmitrii Anoshin (Splunk Inc.)** 32:23 It's a tricky question for hosts, right? Because the host ID has too many different sources for the ID. I think… Maybe… Like, we need some kind of, way in the spec to specify that the ID scope can… can be different within the identity type.
And, so ideally, if… We can say that this scope essentially should be, like, should or must… applied to those… to some of the fields. And for this one, it should be… host ID should be globally unique.
But under some circumstances, it might not be. And if that's the case, it has to be explicitly specified.
On the wire. Does that make sense?
**Josh Suereth (Google LLC)** 33:14 Yeah, yeah, This does give us some help with the current host problem, where we don't know if things are global or local.
Or how unique they are.
Like, I know in our cloud, you can get globally unique IDs if you want, or you can use relatively unique IDs. I don't remember what OpenTelemetry's doing by default off the top of my head, but yeah.
Interesting.
Container is local within the pod. Service instance is local within the service.
Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 33:55 I don't know what the krajo burned at all.
**Josh Suereth (Google LLC)** 33:57 Yeah, this looks good to me so far. So, like, I want to flesh out, an example that shows that crazy, you know, container running.
container running on a VM, running in a hypervisor, you know, inside of a… the whole thing's a Kubernetes cluster, yeah.
**Dmitrii Anoshin (Splunk Inc.)** 34:15 And probably the whole chain of composition, kind of, approach.
When they, like, said by different detectives, I'll see.
I'll put those as well.
**Josh Suereth (Google LLC)** 34:27 what I do like about this a lot is when we report relationships and things, this… this matches how we want to report relationships, where we report, like.
the thing to its owner, always. And then, if we have that signal of all the, like, relationships of… of…
**Dmitrii Anoshin (Splunk Inc.)** 34:44 So, I'm anxious.
**Josh Suereth (Google LLC)** 34:46 All the relationships between different entity types, we can use this to, like, flesh out if something was unclear.
**Dmitrii Anoshin (Splunk Inc.)** 34:54 To be clear, it's… it's not that… Like, strict correlation with… as before, as in the previous version of this, PR, because now I'm… I… I… I have, like, an option to specify that something is globally unique, even if it has an owner. So, for example, port is globally unique, but it can have an owner, which is with their namespace, or, like, node, or wherever. So, it's kind of… less overlap now with the relationship than before, but I think it's good, to be honest. I don't believe we have to make it.
overlap more.
Does that make sense?
**Josh Suereth (Google LLC)** 35:40 Yeah, yeah.
**Dmitrii Anoshin (Splunk Inc.)** 35:43 So, once we have relationships, They will be, like, superset of, like, the whole knowledge graph, essentially.
**Josh Suereth (Google LLC)** 35:56 Cool.
Anyone else have comments on here they want to raise?
**Dmitrii Anoshin (Splunk Inc.)** 35:59 Yeah, I think that's the… Yeah, I got TBM issue.
**krajo (Grafana Labs)** 36:05 Well, I guess…
**Dmitrii Anoshin (Splunk Inc.)** 36:06 All of us are peeking at you.
**krajo (Grafana Labs)** 36:08 From my perspective, from the use cases that I've seen so far.
You know, for metrics, it would be enough to just know the order of the entities, basically, and… See how the… what Yuszka has put together.
Out of those, you know, Contain each other, because then you can already draw your left-hand navigation, basically. And… You know, if you just had an order, then… potentially… Repeat things, and then do any kind of… containment.
So…
**Dmitrii Anoshin (Splunk Inc.)** 36:52 Beautiful.
**krajo (Grafana Labs)** 36:53 My gut feeling is that This probably works, but there will be so much case where…
**Dmitrii Anoshin (Splunk Inc.)** 36:58 I'm pretty much from somebody.
**krajo (Grafana Labs)** 36:59 I'll try to do something.
**Dmitrii Anoshin (Splunk Inc.)** 37:01 I think so.
**krajo (Grafana Labs)** 37:01 I want two containers in this… in the entities.
**Dmitrii Anoshin (Splunk Inc.)** 37:05 Stop.
**krajo (Grafana Labs)** 37:06 Crazy crap like that.
Anyways, I mean…
**Dmitrii Anoshin (Splunk Inc.)** 37:11 Yeah, all the glass.
**krajo (Grafana Labs)** 37:12 So what I'm saying is that it feels like.
**Dmitrii Anoshin (Splunk Inc.)** 37:14 you know.
**krajo (Grafana Labs)** 37:14 A bit more than we'd.
**Dmitrii Anoshin (Splunk Inc.)** 37:15 Gotcha.
**krajo (Grafana Labs)** 37:16 we need, so I'm happy.
**Dmitrii Anoshin (Splunk Inc.)** 37:17 Yeah, I think the one besides cleaner.
**Josh Suereth (Google LLC)** 37:22 I think one thing we can guarantee is if there's a crazy thing people can do with your data model, they will.
**Dmitrii Anoshin (Splunk Inc.)** 37:29 Busher, for sure.
Thank you.
**Josh Suereth (Google LLC)** 37:36 Let's move on to the last topic of discussion.
So… I'll just put an AI for everyone here.
to review.
And then 8I for neat ring… to… Where examples?
Beautiful.
Yeah.
Supervisor.
Let's true.
Is Jake here?
**Jake Dern** 38:10 I am. Hello.
**Josh Suereth (Google LLC)** 38:12 Yeah, you want to walk us through identifying entities through scope attributes?
**Jake Dern** 38:16 I actually don't, because I'm new to entities, and I think… just sitting in on the topic that was just presented has made me realize that it's kind of nonsense, the question that I was going to ask. I think I'm actually more interested in this idea of, like, entity and identity hierarchy, but maybe I can at least… introduce myself and… and what… why I was, You know, trying to bring this up.
**Josh Suereth (Google LLC)** 38:44 Please do, because actually, scope attributes and Entities, it is something we haven't talked about in various.
**Jake Dern** 38:51 Yes.
**Josh Suereth (Google LLC)** 38:51 Other things. So, yeah, go ahead.
**Jake Dern** 38:53 Sure, yeah, so I work on, so I've been a long-time consumer of OpenTelemetry, but just, recently, like, active participant, in the last year, so I work over on, Hotel Arrow. I work with, Laurent Carell, if you guys are familiar with him, on the F5 side.
And so recently, we've been talking about entities. We have this application over there, the Stataflow engine, and it has a very well-defined entity model, but we don't have anything, you know, baked in there in terms of emitting information about those entities through OpenTelemetry, so we're kind of investigating that.
And the reason why I was asking about scope attributes is something that we do, is we identify a lot of the entities via scope. So… Things internal to the engine, yeah, they're mostly described by a scope, scope attributes, pipelines, and nodes, and other stuff, And so that was one thing that I was going to ask about, and then the other thing, that we've been interested in is… This idea that, you know, the sort of, like, full identity for, like, some entity, you know, may involve inheriting attributes from other entities, basically. So I think this is very similar, or basically the same as this concept you were just describing, where some, like, entity identities are, only unique within the context of another one, and so I was, stopping by to ask questions about that, but I think I need to just read the PR that was just presented there, and absorb that information.
**Josh Suereth (Google LLC)** 40:27 This is an OTEP. There's, so I… this is an aside, but OpenTelemetry has an issue, in my opinion, with, resource and multi-tenancy with SDKs, for example. So, like, let's say I am a process, and I'm running a couple other processes, or I'm doing things on behalf of others, and I want to, like, say, okay, I'm working… this is an old old Javaism, so apologies for those of you who aren't ancient like I am, but, if you remember EJBs and, like, WebJars and WebAssembly and all that stuff with Java, where you would say, here's an application, I publish a WAR, and I have one service serving, like, 20 of them, because Java's expensive to run once.
Or, like, 100 times, but once, it's actually relatively efficient, because you have economy of scale. So, I have one process, which is serving maybe 20 different apps on it, and then I scale that thing.
Well, each of those apps that I'm running should be its own resource, but then our SDK has one resource for the whole SDK. So we made this proposal about, okay, well, what if I, you know, allocate a new entity and say, I want to record data against this entity?
Which is kind of like Entities on Scope.
kind of like Entities on resource, right? It's like, it's like a little bit in the middle, so we made this proposal for that. We had a, We had a few, prototypes of it. Seems to work okay. When you talk about metrics.
all hell can break loose when you do this. When you talk about logs and spans, it's like, whatever, cool, just throw a bunch of extra attributes, slam them down the stream, everything's gravy. With metrics, you have to worry about aggregations, how much memory you're taking internally, all that kind of junk.
So… we put that on hold because high cardinality tendency is more what OpenTelemetry needs right now, which is, say, I want to attach a metric per like, user that's talking to me. So I want to track, like, you know, here's the number of users that are doing X, or the number of users who are doing Y. That's another thing that we don't do very well in OTEL, we push that into a metric label.
And some people want to attach that as, like, an aggregation component, or they want to treat it as, like, a contextual piece of information they put somewhere.
So that's… that's, like, tenancy in OpenTelemetry. That might be relevant. It sounds like you're using Scope to do that within OTEL Arrow, and I know from talking to Lauren a lot, because, like, he and I work on Weaver together, I know… I know that that's kind of how you guys are doing it, and I know some of the earlier discussions, so I don't know where it is now, but, yeah, there's… My long-winded answer is, we don't have a great solution for you at OTEL.
We have a bunch of things we're thinking about.
The other thing that has been on my mind around this is we've had some people ask about having entities in the actual signal side. So, if I'm writing a metric, Or I'm writing a log.
And my log is from this source.
But, I am talking about, like, this source End that destination.
and I'm writing, say, a latency.
metric that says, how expensive is it for A to talk to B, How do I model that?
Right? Because now I have two entities. I have the source, and I have the destination.
What do we do in OTEL? Right now, one of them is fully modeled. You pick which, either the destination or the source, and that goes into resource, and the other one is completely not modeled, it's just loose attributes that someone has to, like, go reverse engineer to figure out what that connection really is.
Which, you know, that's fine. Like, that's phase one. But, like, phase two, we might want to get better with entities of trying to figure out, like, can we not just understand relationships, but report metrics on them?
I might be going way beyond what you wanted to know.
But the, the TLDR is, I don't think we have great answers for you.
They're great questions, so please stay engaged, ask lots of good questions, and tell us what you think and how we can help.
**Jake Dern** 44:50 Yeah, awesome. Yeah, certainly I have not gotten as far as, being concerned about, things like the latency metric and, yeah, you know, sort of attaching that to two different entities.
But yeah, the reason that we're sort of, like, interested in this is, yeah, to more explicitly communicate, you know, to whatever backend it is, what entities we have, and then take the signals that we're emitting and attach them to those entities.
I would imagine that's what everybody wants to do. But, yeah, and the way that we're describing them, using a combination of resource and scope, and also being interested in this sort of idea of inheritance, and how we can best leverage the work that you guys are doing to do that, that's, you know, that's why I'm here.
**Josh Suereth (Google LLC)** 45:35 Awesome.
There's one other thing in OTEL, let me see if I can find it for you. This was a discussion with, the profiling SIG around the actual protocol.
But there was this notion of having a hierarchical set of resources.
So, instead of, instead of your OTLP, Sending, like.
A separate resource bundle of all of the attributes together all at once?
What you do is you actually have a dictionary.
And you can have, like, a resource that has… here's this set of attributes that are different, and then reference this other thing for all of the other attributes that are shared across a thousand. And I believe that is now part of OTLP for profiling. Let me check quick, though.
**Jake Dern** 46:23 Oh, interesting.
**Josh Suereth (Google LLC)** 46:25 Because I don't remember where that landed, and I probably should.
**Jake Dern** 46:42 Yeah, it's interesting you bring that up. Not that I'm familiar with the work, but this is exactly the kind of thing, you know, this hierarchy with dictionaries and that kind of stuff that we were looking at defining. You know, sort of taking our entity-like relationship model, you know, identifying, like, what things are related to what and how via composition and other stuff, and then automatically sort of deriving, like, the full set of attributes that That describe that thing.
It sounds very familiar to what you were just describing with… Dictionaries sort of referencing other ones.
**Josh Suereth (Google LLC)** 47:17 So, it looks like we didn't go with the layered hierarchy of resources. Instead, there's just a dictionary where all the key values live, and then inside of OTLP, only for profiles. But it is part of common, so here, I'll show you this.
the way… the way we're trying to save bytes here, because I know that Arrow is all about that, too, When you have a key value list.
You have this possibility that something is actually an index into a profile.
**Jake Dern** 47:49 Okay.
**Josh Suereth (Google LLC)** 47:49 Into a, into a dictionary.
And there is debate about whether or not we want this across all OTLP to, like… because it is a huge reduction in Payload size, if you're reporting about multiple entities from the same payload.
**Jake Dern** 48:05 Yep, yep.
**Josh Suereth (Google LLC)** 48:06 Pro, you don't care, because everything you do already has that reduction. Yep. But for straight OTLP, right?
**Jake Dern** 48:14 Yeah.
**Josh Suereth (Google LLC)** 48:15 Something…
**Jake Dern** 48:15 Interesting.
**Josh Suereth (Google LLC)** 48:16 you know, something to… if you weren't aware of this, take a look. There's a bunch of open threads about whether or not this should be used across all OTLP. We have no way to do that in a non-breaking way.
So, yeah, but there's always OTLP 2.0. I mean, Prometheus is going 4.0 soon, right? So… We can do OTP20, why not?
**Jake Dern** 48:37 Hey, Arrow's on B60, I think, or 63? B60.
**Josh Suereth (Google LLC)** 48:42 Oh, cool, cool.
**Jake Dern** 48:44 ORS, not us, not us, but…
**Josh Suereth (Google LLC)** 48:46 Oh, gotcha, yeah, yeah, yeah.
**Jake Dern** 48:47 Yeah, yeah, yeah.
**Josh Suereth (Google LLC)** 48:48 Yeah.
Cool. Anyway, if that helps, like, please take a look.
**Jake Dern** 48:54 Yeah, it does, that is really helpful. Yeah, I do not have my, kind of finger on the pulse of everything that's happening in OpenTelemetry, not by a long shot, so… That's, like, 10 times more information than I've already found in my brief searching.
**Josh Suereth (Google LLC)** 49:09 Okay, I don't know if anyone has their finger on the whole pulse, I just… if you… like, for me specifically, I do resources, semantic conventions, and profiling, but I don't do profiling anymore, so everything I told you is about 6 months out of date. Yeah. And if anything changed in 6 months ago.
We'll have to talk to the profiling folks, sorry, yeah.
**Jake Dern** 49:30 Yeah, no, thank you, this is great. I appreciate it.
**Josh Suereth (Google LLC)** 49:32 Cool.
Awesome. So, I think we… we had some really good discussions, lots of good things to get through. I'm gonna… we haven't done… we have, like, 10 minutes left, and we haven't done one thing in a while, which is I want to go through our project board quick.
Because, you know, it's kind of out of date. So… What we have in progress, SDK startup specification. I thought that this went through.
I'll take a look. I think this one might be done, because I think Daniel's PR went through. Strategy for asynchronous Resources Entities, I think this is also done, because I think that PR was merged. I'll check.
This is the collector work that Dmitrii's on that's still in progress. Show demo of how collector process differentiate my own local. This is what Dmitrii's working on now. Resolve resource configuration with data model. What was this one?
Oh, right, right. This is where schema URL was missing for things.
So, this is actually with the configuration SIG. So I think we need to actually talk with the configuration SIG a bit. We're actually… Some of this is resolved, but not all of it, so that's a to-do on me. But in terms of Phase 1 for resource entity mapping.
We have a Java prototype done.
I'm not sure the status of the JavaScript one. I think we need to get a Go prototype going, but, wanted to check in with folks. Do we feel like we're at a state where we're basically waiting for feedback before we… Go in and try to call a, you know, hey, this is ready for everyone to check, or to try out.
Thanks, Jake.
**Dmitrii Anoshin (Splunk Inc.)** 51:38 I'm sorry, Josh, I… We'll start a stop to paying attention.
**Josh Suereth (Google LLC)** 51:45 No, I might not be phrasing that right. I'm basically checking on phase one for resource entity mapping. When do we think we're ready to basically tell people, hey, this is, like, ready to try out, this is feature complete, we can start Working our way towards freezing… freezing the spec and getting the prototypes and demos out.
Another thing I'm… another thing I'm implicitly asking is, Dmitrii, your current PR, do you think that that needs to be part of Phase 1?
I think it does.
**Dmitrii Anoshin (Splunk Inc.)** 52:13 I think it is phase one, Rios, because, like, Phase 2 probably would be Entities of Signal, and Phase 1 is specifically we need to… Clarify what identity is, and that's a pretty important part of the question.
**Josh Suereth (Google LLC)** 52:27 Yeah, so this is currently what you're working on. When this is done, though, like, when you're done with that, is there anything else we're worried about? This is around working with the configuration group to make sure that, resource configuration supports everything we need, but, is there anything else you think we need to do post this? I believe that these two are done from Daniel.
I think all we have left here for Phase 1 is your PR, and then getting all the prototypes updated, and getting enough prototypes.
**Dmitrii Anoshin (Splunk Inc.)** 53:01 Yeah, I think that makes sense. Maybe some… Collector, more merged stuff on the collector's side.
Yeah.
**Josh Suereth (Google LLC)** 53:11 Do you need help with any of this, or…
**Dmitrii Anoshin (Splunk Inc.)** 53:14 I… I don't know, or… Maybe, if you want to take a transform processor, for example.
But we'll do it.
Or someone else can retake it, I don't know.
**Josh Suereth (Google LLC)** 53:28 Is this… this is… so Transform Processor is making sure OTTL supports entities appropriately in all of its stuff?
**Dmitrii Anoshin (Splunk Inc.)** 53:34 Because at least it doesn't break Entities, essentially.
**Josh Suereth (Google LLC)** 53:38 Okay.
Can we do that solely on P data, or do you think we have to actually do it via transform processor functions?
**Dmitrii Anoshin (Splunk Inc.)** 53:48 Transfer repository functions need… would, Like, in terms of making sure that entities aren't broken, we can rely on Pdata API already exposed.
**Josh Suereth (Google LLC)** 54:02 Okay.
**Dmitrii Anoshin (Splunk Inc.)** 54:02 But… Like, if we want to add additional functions specifically to the entities, this is more work, and probably not in the scope of this PR.
**Josh Suereth (Google LLC)** 54:13 Yep. Okay.
Okay, cool.
**Dmitrii Anoshin (Splunk Inc.)** 54:19 like, I… I… it's been a while since I looked into that, so let me… let me… Update all of those.
**Josh Suereth (Google LLC)** 54:28 Yeah, if you… if you make these up-to-date, and they're not assigned to you, I think they're… they're open for others. I've done a bit of work on OTTL in the past, so I might… I might take a look at that.
**Dmitrii Anoshin (Splunk Inc.)** 54:40 Sounds cool.
**Josh Suereth (Google LLC)** 54:41 I don't think I've ever had something successfully merge in a collector, though, outside of, like, BSconfig. So, it'll be the first time I write Go code that's used.
**Dmitrii Anoshin (Splunk Inc.)** 54:52 Yeah.
**Josh Suereth (Google LLC)** 54:53 Alright. Cool.
The other thing is, I'll talk to David Ashpel. I don't remember where the Go SDK prototype stands, but I might revive that as well and get that through.
Cool. And then this is… is figuring out config, so… I'd like to kind of get this shored up and out the door, so that we can basically take a, by the way, before we hit Phase 2, The process generally is… we should take a look at the SIG and make a chartered document for what Phase 2 is, and try to be more strict about what's in and what's out.
what we have to accomplish and who needs to be involved, and then we actually do a renewed project proposal where people sign up to say, yes, I'm going to be involved, and here's what I plan to do.
So, I think it would actually be a good idea for us to do that. So, like, finishing up Phase 1, going back through the project charter process, and having people recommit and say, yes, this is still important to me, I still want to do this, and here's what I'm planning to work on.
Does anyone have concerns with that?
**Dmitrii Anoshin (Splunk Inc.)** 56:01 Sounds good.
**Josh Suereth (Google LLC)** 56:02 Cool. Alright, with that, thanks everybody, and sorry about last week, I should have… I think I… I think I only put in maintainer's chat I was taking a vacation, but not in the Entities chat, so next time I'll warn you.
**Dmitrii Anoshin (Splunk Inc.)** 56:15 It's fine, you… at least you told us before, on the previous call, that's what I remember.
**Josh Suereth (Google LLC)** 56:21 Oh, right, I said it in voice, but not on chat. Okay, alright. Anyway, good to see y'all.
See y'all next week's.
**Dmitrii Anoshin (Splunk Inc.)** 56:28 Bye.
**Arve Knudsen (Raintank, Inc. – Grafana Labs)** 56:30 It's here, behind it.
