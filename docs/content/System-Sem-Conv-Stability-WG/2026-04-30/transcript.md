SIG: System Sem Conv Stability WG
Date: 2026-04-30
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 04:05 And how are they removing bolts?
**Donal O'Sullivan** 04:09 Hey, Pablo.
**Pablo Baeyens** 04:11 8.
Oops.
Christos is joining at some point, if he added a topic, right? Do you know, Donald?
**Donal O'Sullivan** 06:46 Yeah, I would assume so. He's… he says… Earlier today, did he join.
Let me.
**Pablo Baeyens** 06:55 Okay.
**Donal O'Sullivan** 06:56 Let me slack him there.
**Pablo Baeyens** 06:58 Okay.
Should we start?
**Christos Markou** 08:13 Yeah, first one is mine. I… had this question again. I'm pretty sure we have discussed that in the past, but, I couldn't recall any specific answer or place that we have documented this decision or not.
And, it is related to another group that is, similar to this one. It's about Kubernetes SIG.
And there we have, we have promoted the… Attributes themselves.
to release candidates already, and the reason for this is that the KH processor is just using… at the moment, it is using the attributes directly, and adds them as resource attributes.
So that was the decision, and right now, next steps for this group will be to work on metric stability.
And I remember that, there was a requirement about, for a metric to be promoted to stable, or any kind of level, like release candidate, or whatever.
First, the entity, that is attached.
To… that is related to these, metrics should also be, let's take, for example, stable.
So, things like, container CPU time, for example. In order for this to be promoted to stable, should container entity be stable first?
And I think we also hit that here, so… I know we have this PR that promotes process attributes to at least candidates. We haven't yet done anything… we haven't yet promoted metrics.
So, the question is how we're going to do it, and if we have any, specific Guidance around this, and how, in general, we're going to handle it in this group.
Because anything that we discuss here or decide here, I think it will apply in other groups as well. My main concern here is that, for example, to stabilize entities, the thing that I believe we're missing is The entity… entities relationships, mostly.
On the spec level. But yeah, maybe, Dimitri, you can correct me here. So first question is.
for metrics to be promoted to, like, release candidates or stable, do we require, their related entities to be promoted as well? That's the first question, and the second question is, Either it is required or not, where we stand when it comes to entity stability, things like process, entity, or container entity, and this sort of stuff.
So, yeah, that's it, the questions I had.
**Dmitrii Anoshin** 11:20 Do… how would it block, like, having entities defined comparing to the old style? Let's say we don't have entity 1, we have attributes.
How would it be different?
Like, defining attributes as part of resources table, whether, comparing to the entities.
**Christos Markou** 11:45 I don't think it's, it really matters. So, for… for metrics specifically today, we say we have, for example, container CPU time, or system CPU time, whatever.
And then we say, we have this entity's reference, and we say it is, related to, let's say, a container entity, right?
And I remember that some of the maintainers back then had said that for a metric to be promoted to another stability level, their respective entities should also be promoted at the same level. I'm not sure if this is still the case.
But this is something for us that we need to figure out. And if so, What is the situation… what's the case with entities being promoted to release candidates, or even stable .
**Dmitrii Anoshin** 12:40 I don't think we should block… put block on entities. Like, the entities work is still… is going on pretty good, there is some progress, but I don't want… to block… marking metric, or, like, the whole semantic convention, namespace by entities, because we already have other namespaces declared by stable, even… even before entity was, like, introduced, or… So, identity sites, we'll be working with some kind of, let's say, limitations or pre-existing… Requirements?
Yeah, I don't think it should be a big problem. As far as I remember.
What's, what, what's… what has been promoted to stable database, maybe? Or… Sorry, I don't remember.
**Donal O'Sullivan** 13:38 HTTP.
**Dmitrii Anoshin** 13:40 Right, so, like, HTTP, there is no entities.
promoted to stable associated with that, right? Server, I guess HTTP would be connected to the server entity. A server entity is pretty much just a wake concept. I don't think it's… processes much, but in a much better shape.
As well as host, at this point. So I don't think we should blog on that.
Does make sense.
**Christos Markou** 14:11 Yeah, I see the point. I'm still afraid that maybe, like, some unconvention maintainers would raise this again.
And, I… I saw also a comment from Ludmila on the, process, promotion, process namespace promotion to release candid, where she asks about, if entity should also be promoted.
I assume this is… this should be based on… on case… This should be per case, so… Whenever something needs to be promoted, there needs a disc… we need a discussion to happen to decide what we want to do, and yeah, either require entity or not. Do you think that the entity… let's say, for example, container entity, or Kubernetes pod entity, these things, could those things be promoted, to release candidates, for example?
**Dmitrii Anoshin** 15:13 Yeah, I think we should be close. There is one important PR that I raised recently.
bore… For the, the… There are issues here.
No, not the relationships. The, identity score.
If you look at that one, there is… there are some… comments from Josh, I'm gonna address them, but this one is pretty interesting, and it's kind of not blocking, but… It's, something that we need to have defined and merged, for sure, before we even consider any of the entities being stable.
So, yeah, take a look, I will… it's the first PR in the series, but once it's merged.
We'll be in better shape when it… Right, because before… without this PR being merged, and other subsequent I don't feel confident in declaring any entities stable, but after that, it should be… should be in better shape.
**Christos Markou** 16:22 So, from your perspective, your suggestion would be that we can promote metrics, Standalone metrics, without caring about their entities now.
So, system CPU time.
**Dmitrii Anoshin** 16:38 Let's do that.
**Christos Markou** 16:38 hosted.
**Dmitrii Anoshin** 16:39 That's my… that's my position, because I just don't want to block anything by entities. Entities' work go slowly, and then don't want to block, because there are not a lot of people. I, like, have very less time… not a lot of time to work on that, and others as well.
So I don't want to block any… anything by that. But maybe there are some other opinions on the NGTC. Let me bring that in the NGTC call next time. It's gonna be next Monday.
And I'll discuss it with Josh, and We'll see, what is his opinion, and others.
**Christos Markou** 17:19 Okay, it's okay.
**Dmitrii Anoshin** 17:19 Does that sound good?
**Christos Markou** 17:21 Yeah, yeah, perfect. Thank you, thank you very much.
**Braydon Kains (Google)** 17:24 The only thought I have on this is that, like, for process in particular, it's kind of interesting because, like, the design of our metrics really depends on I mean, originally it was just on, like, the resource being formatted the right way with the right attributes. Now it's against, like, being reported against the process entity properly, but if we stabilize stabilize the process attributes, and then for some reason, the identifying attributes of the process entity needed to change, that would technically change, like, the overall time series of those metrics as we expect them to be reported.
**Dmitrii Anoshin** 18:01 I… I… Done. Only if we add some other new attributes, I guess.
So, let's say we… we decide that identifying attributes should be something else completely, that we don't even have in the resource at this point.
Maybe in that case only, right? Because if we just reshuffle and say that, I don't know, not beat, but… I don't know, process name is… is identifying attribute. And in that case, it's already there, it's just… One of them identifying attribute becomes another one.
**Braydon Kains (Google)** 18:40 Hmm.
**Dmitrii Anoshin** 18:41 So, like, from MTS perspective, it doesn't… shouldn't change anything, I guess, unless you're taking… identify an attribute only part of the MGS.
I think…
**Braydon Kains (Google)** 18:55 That's the only thing that can be part of the… metric identity, right? I don't think we want descriptive attributes to be part of it.
**Dmitrii Anoshin** 19:01 Yeah, I see what you mean. But, I mean, in practice, no one currently does that. It's long-term. Right.
**Braydon Kains (Google)** 19:08 Yeah, it's theoretical. Yeah, theoretical.
**Dmitrii Anoshin** 19:11 typical long-term solution, but you're right. I guess, yeah, like… Hmm… I get your point. Let me…
**Braydon Kains (Google)** 19:22 For process… I mean, we feel pretty good about the two identifying attributes we have. The only thing that we have… haven't done yet that I kind of want to do is to add, like, an optional third identifying attribute of the namespace, because… If you're… if you don't specify the namespace, you can have PID and creation time clashes, technically. Like, the identity could clash if you have the same process in two different namespaces. This is, like, an excessively rare scenario, but, like, technically it's possible.
**Dmitrii Anoshin** 19:52 Within the same port, or within the same, host.
**Braydon Kains (Google)** 19:56 Within the same host, yeah, if you're running… I mean, this can happen within… containers. Like, I'm trying to think if… if, theoretically, you started two Docker containers at The exact same time.
And then instrumented them separately to report their PID and creation time within the container namespace.
Like, like, from within the containers, root.
But without considering the namespace that they're in.
Then…
**Dmitrii Anoshin** 20:29 Two.
**Braydon Kains (Google)** 20:30 different PID1 creation time for the init process of the container. This is all getting… this is getting very deep into the weeds of it.
**Dmitrii Anoshin** 20:38 That's actually… potentially, that's something that is being addressed in my PR that I linked. You're saying that namespace associated with a container within a host.
**Braydon Kains (Google)** 20:50 Right, yeah, because, like, the…
**Dmitrii Anoshin** 20:51 Okay.
**Braydon Kains (Google)** 20:52 the init process of the container is PID1 within the container's scope, but not within…
**Dmitrii Anoshin** 20:59 or…
**Braydon Kains (Google)** 21:00 the host. Within the host, there is a different PID one.
**Dmitrii Anoshin** 21:03 So, like, there is one-to-one relationship between the name… what you call namespace and the container within a host. Is that correct understanding?
**Braydon Kains (Google)** 21:11 As far as I know, yeah, I don't think there's… I don't think there's any way for one container to have multiple namespaces. I don't think that's how Docker works.
**Dmitrii Anoshin** 21:21 I think, yeah, that's what's been addressed in the MIPO request. Please take a look.
**Braydon Kains (Google)** 21:27 Okay, yeah, I will.
**Dmitrii Anoshin** 21:28 In the pull request, I say that Identity of the process.
Is local.
against its context identity, its context type. And context type is not something we specify in the semantic convention that is required, but it's something that can be different in some cases, rare cases. So, for the process, typically.
Context type is the host, so its identity of the process, in most cases, is unique within the host.
But…
**Braydon Kains (Google)** 22:06 Inside.
**Dmitrii Anoshin** 22:06 In some situations, it can be processed in a container. Like, let's say, a container with several processes, that would be the case. And in that case, you emit data with Process entity still having pit, pit and start time.
And, the context, Context entity type would be not the host.
But it would be a container. And then you add an additional container entity along with that.
And a combination of them would give you some kind of, like, more global identity. And then if you add host.
to the, let's say, parent or context entity of the container, it'll give you a potential global identity. But please take a look at the APR.
**Braydon Kains (Google)** 23:00 Yeah, yeah, thanks for… thanks for that. I will take a look.
Okay, cool.
I wonder if we should skip ahead to, to the TCP thing, since we have some guests here to discuss it.
**Donal O'Sullivan** 23:17 Yeah, sure, that's, that's one of you.
**Giuseppe Ognibene | Coralogix** 23:22 Hi, everyone.
Can you hear me?
**Braydon Kains (Google)** 23:25 Yep.
**Giuseppe Ognibene | Coralogix** 23:26 Hi, my name is Giuseppa. Nice to meet you.
And, with Nimrod, we… we created an issue about a proposal to introduce system.network.tcp and UDP metrics.
We are working on a project called the Open Telemetry PBF Instrumentation. We had already a prototype about some metrics.
And we saw that there is no semantic conventions for the TCP, FTT, failed connection, and stuff like that.
So, we thought about, introduce something, That can be a standard.
There is the issue in the, document.
We thought that maybe to join the SIG. I hope it's the right SIG, because it's touching also the network one.
So… Hmm, this one.
**Braydon Kains (Google)** 24:26 Yep, I think this is the right sake.
**nimrodavni** 24:34 Yeah, just wanted to bring it up because we have, I think there's some other… product, kind of in the… I think there's the old OpenTelemetry eBPF, now it's called OpenTelemetry Network, I think, that are… also produce similar types of metrics.
And there's some other, like, open source, mainly BPF-type projects that expose, like, this network observability, metrics.
So we wanted to… right now, we, produce them… the project is still not, like, in a stable release, so we'll also… producing all the metrics with, like, an OB prefix, just to, basically say, this is not part of any semantic convention, and this might change, but we wanted, in the meantime, start pushing For, this to be more stable and, agreed upon, so… If you guys are new.
Have any, Like, any review of this document would be great, and also if you have anything, like, from us regarding how to proceed, if you want us to… open a PR after some… someone, like, vouched for it, or whatever.
**Braydon Kains (Google)** 25:46 So, do you actually have, like, an example… Project that is instrumenting these right now?
With just… with the prefix, like you mentioned?
**nimrodavni** 25:56 Yeah, I think, Pino had, we're only producing two of them, I think. It's the RTT and the failed TCP connections.
**Braydon Kains (Google)** 26:04 Okay.
**nimrodavni** 26:05 And like, we're continuing to implement them, and… Basically, working on all of them.
Yeah, this is done via OB, just with some eBPF probes.
**Dmitrii Anoshin** 26:23 That sounds good to me.
Yeah. Go ahead, sorry.
**Braydon Kains (Google)** 26:28 Sorry, I was just gonna say, I… I want the metrics to exist, but I'll need to look more deeply at everything, and I'll also check with Some members of my team who… would probably have opinions here, and I'll try and loop them in.
**nimrodavni** 26:47 Agree.
**Giuseppe Ognibene | Coralogix** 26:48 Thank you.
**Dmitrii Anoshin** 26:50 I want to say it's pretty much the same. Thanks for coming, and thanks for your interest, and… if you can contribute those metrics, that would be perfect. I… I don't have any objections, sounds good to me. But yeah, I would defer to, Braden for further evaluation.
More detail, more details, yeah.
**nimrodavni** 27:13 Great, so I guess we're just, Most of the discussion will be on the issue itself, and we'll just wait for responses from you guys.
**Braydon Kains (Google)** 27:23 Yep, I think, most likely. I'll need to… I'm still sort of… On my own, evaluating we have some sort of… we're experiencing this in CPU right now, where I'm not sure exactly what stuff should go in system.whatever, and what stuff should just go in, like, whatever the thing. So, like, CPU.something, or system.cpu.something, and network is kind of… Intertwined with the same thing.
So that might affect maybe the names, but, like, based on my scan of what metrics you're trying to introduce, like, I think we should have signals for them.
It just may depend on, like, what namespace they end up in.
Probably still System.network, but we… Have to… Think about this a bit more.
But yeah, I'll also bring it up with some members of my team who do… they do, like, eBPF for collecting golden signals stuff, which is a lot of these same types of metrics, so they probably have opinions about how exactly these should look in SAMCOM as well. So, I'll bring them in, too.
**nimrodavni** 28:35 Right.
Thank you very much.
Sounds good.
**Giuseppe Ognibene | Coralogix** 28:38 Thank you.
**Braydon Kains (Google)** 28:39 Thanks.
We have 5 minutes if you want to give your update, Donald.
**Donal O'Sullivan** 28:49 Yeah, so really quickly, I don't know, did you see Roger's reply to the issue for the multiple schema configs? So, he was just wondering about… the new feature in mDataGen where you can, enable configurable attributes for metrics. So, like, say, if your metric has two attributes, and then in the user's runtime config, you can only specify to emit one attribute.
**Braydon Kains (Google)** 29:15 Right.
**Donal O'Sullivan** 29:16 So, the issue there is… if we want to allow that, that means that the user then has to, like, explicitly, add the version metric to their user config, if that makes sense? So you'd have, like.
I suppose you'd… the way… I've replied there to the actual issue, but you'd have to essentially have the metric with, like, your… with the version number in it, because, essentially the version metric is pretty much a separate metric that is, you know, where we generate the code for that.
So, to actually… pick which attribute you want to use. You'll have to explicitly state that for the versioned metric, and not on the The legacy metric, if that makes sense.
It's just… it's fine, it's just that it's a bit annoying because you're then asking the user, do they actually have to add this to their user config?
And the way we kind of saw it was there's kind of two options, so, like… We… we support the user doing that, or we just do not support the, what you call it? The, the configurable attributes for metrics for versioned metrics, if that makes sense.
**Dmitrii Anoshin** 30:29 So what we do instead, if we don't support them, and you can use the configuration?
**Donal O'Sullivan** 30:34 Yeah.
**Dmitrii Anoshin** 30:34 I know. We send them both?
Okay.
Maybe… maybe we can… So… like, for example, it's only problematic for the double publishing. If we… if both feature gates, like, exclusively disabled enabled, it's not a problem. But if both enabled.
Potentially, we can just have a… Like, separate, configuration options with, Let's say, metric… system distributes the time.
slash V0 and slash V1, and we don't even have Configuration option without that suffix.
In that case, it will be explicit, it will not break users, but at the same time, when they enable both feature gates, they're kind of aware of this problem, right?
**Donal O'Sullivan** 31:37 Yeah.
**Dmitrii Anoshin** 31:37 And, I think we need to provide some kind of… maybe not, but I think it would be better to provide some kind of knobs to enable one of them.
**Donal O'Sullivan** 31:51 Yeah, like, just some kind of guidance. Like, so it does work at the minute, so as long as you update your runtime configuration, and you put in the metric, like, the version metric, and then you specify the attribute you want to emit, it works fine. It just means… We're asking, like, if the user wants to use that, they'll have to explicitly You know, add their versioned metric to the user config, so they'll have the legacy and the versioned one.
Yeah.
**Dmitrii Anoshin** 32:19 Right, that was my idea.
**Donal O'Sullivan** 32:21 Yeah, yeah, and that, that, that works as is, that's fine, you know, I hope you have the example, yeah.
**Dmitrii Anoshin** 32:29 But if one or another feature gate is disabled, there is nothing like that. All the user config stays as is, right?
We don't… we don't have any suffixes.
**Donal O'Sullivan** 32:41 Yes, that's correct, yeah, because in the actual… like, for example, in the CPU scraper, we check if the feature gets enabled. If it's not enabled, we don't emit those, the metrics for that version metric, I guess. They could have it in the config, I guess, but it won't. We could probably just emit, like, an error or something if it isn't there and the feature gate is off, or something like that.
**Dmitrii Anoshin** 33:05 Yeah, sounds good.
**Donal O'Sullivan** 33:07 Yep.
**Dmitrii Anoshin** 33:08 So, is it ready for review, that particular CR?
**Donal O'Sullivan** 33:12 No, I'll have to… I haven't opened a PR, I only have one in my own fork, so… but I… yeah, if that's what you guys want, I can open… a PR in Contrib, and then, I have to open a PR in mDataGen as well.
**Dmitrii Anoshin** 33:28 Okay, that sounds perfect.
**Donal O'Sullivan** 33:30 Yeah.
**Dmitrii Anoshin** 33:32 Unless anyone else has any concerns with that approach.
Sounds good.
**Braydon Kains (Google)** 33:37 Good with it.
**Donal O'Sullivan** 33:40 Thanks, guys.
**Braydon Kains (Google)** 33:45 Cool, I think we're at time.
Thanks, everyone.
**Dmitrii Anoshin** 33:49 Thank you, folks.
**Braydon Kains (Google)** 33:50 See you online.
**Christos Markou** 33:50 Facebook.
**Donal O'Sullivan** 33:51 Rose.
**Giuseppe Ognibene | Coralogix** 33:52 Bye-bye.
