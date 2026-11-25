SIG: K8s Semantic Convention SIG
Date: 2026-11-24
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Christos Markou** 02:21 Hello!
**Tyler Helmuth** 02:25 Hello.
**Christos Markou** 02:42 That's wait.
Couple of minutes, and see if anyone else is joining.
Yeah, so… I don't see anyone else joining, and… The only topic is from my side.
i.e.
I have linked to the agenda the two PRs, that… the remaining PRs that… Try to promote the remaining metrics to release candidate.
And one is for the volume metrics, and the other one is for the utilization metrics.
And… The plan is to complete… to have those merged, hopefully, and then we can consider the whole set completed.
And then, all these metrics will be ported to the KubeletSat receiver behind the feature gates, and, we can give the option to the users to start using them.
And then we will be able to collect feedback. We can wait, we can decide to wait for a long period of time, like a couple of months even more.
Before declaring them stable and smart conventions. So, yeah, if you have some time, please take a look.
And… It's not like, it's not that… End of the world, we can always revisit them, but having them in a list candidate will allow us to… Have, like, an aligned version of V1 potential… targeting V1 metrics in the, the receiver already.
**Tyler Helmuth** 05:47 How close are these metrics to what the collector's already emitting?
**Christos Markou** 05:52 how close. I think for the volume metrics, For these two PRs specifically, the volumetrics are quite close, I think, just… There is a rename there, because in the past we were calling them, KH Volume whatever, now we have added the pod, so it's case, pod, volume thing. I think we also added an extra attribute, the persistent volume name.
And for the utilization ones, The concept is the same, but they change significantly, because.
**Tyler Helmuth** 06:29 Yeah.
**Christos Markou** 06:30 which also introduced the… The new concept of having the limit and the request.
on the pod, and you can have the desired and the actual. So, yeah, it's a bit more… There.
**Tyler Helmuth** 06:46 Do we already have a migration dock for anything, all of these release candidate permissions?
**Christos Markou** 06:53 Wow.
Yeah, we have this long migration… page that is listed on, the OpenTelemetry docs.
**Tyler Helmuth** 07:05 Yeah, and then are these metrics… are the migrations for these metrics and attributes already in there?
**Christos Markou** 07:10 Yeah. Yeah, should be there, or we try to keep this up to date, mostly, but the work is manual, unfortunately.
**Tyler Helmuth** 07:17 Yeah. I'll… when I review these later, I'll… I'll check that they're in there.
**Christos Markou** 07:25 Yeah, during the, like.
migrate… the actual, let's say, migration in the component in the receiver, we will spot any gaps there, I guess, so it's good that we push this forward in parallel. It will give us the chance to spot gaps or misses, I guess.
Which is good.
Okay, that's all I had on my side.
Next one is, by Stu. Welcome, by the way.
**Stuart Buckingham** 07:56 Thank you. I just wanted to ask on the, volume stuff, is there any need to expose what the backing CSI is, or anything about Any more information about the volume?
**Christos Markou** 08:11 We add the… Let me see, actually, those were added.
**Stuart Buckingham** 08:21 Like, maybe it's, like, an optional attribute.
**Christos Markou** 08:25 Yeah, we add the volume…
**Stuart Buckingham** 08:28 Oh, I see volume.type. Maybe that patches, or is that…
**Christos Markou** 08:32 Yeah. or the persistent volume type, and you also can link it to the persistent volume Claim name, and persistent volume name.
So, probably, you can link there, and find this extra info.
We can, like, always shop if it's something.
Useful.
**Stuart Buckingham** 08:58 Thanks.
Yeah, so, there's been a bit of a discussion on this issue that I proposed, which is to gain parity with CubeState metrics.
We're missing the, ability to, show what the controlled resource… or what is controlling the resource. So, like, if you have a pod, replic… you know, it's controlled by a replica set, which is controlled by a deployment, which is controlled by an application, whatever.
There was an ongoing discussion, I think there's an earlier… Issue 3778, which was, proposing a workload.
It's sort of unclear in traversing the controller graph.
a workload would be. I think it's pretty obvious if you've got deployment replica set pod.
But something like, CERT Manager, where is the certificate the workload, or is it the challenge, or is it the request, becomes a little bit blurry.
And I think a lot of the discussion before, sort of.
Got sidetracked into trying to define where that workload definition happens.
And so, I think that rather than trying to follow on for that forever, the… Best… the easiest way is really just to introduce the, controlled-by attribute that… be a type that includes the API version, kind, name, and UID of the controlling resource for any resource. Obviously, not everything has a controller, like, if you start a pod by itself, then there won't be a controller, but I think that, yeah, having the control by or owner As a name is really the only way that we can have something that's declarative and isn't opinionated.
So I wanted to see… this is awaiting triage before I can actually make the make the PR to introduce this semantics, but, wanted to see if that is acceptable.
And yeah, for what… for what it's worth, this is how KSM does it, with their owner.
Metric.
that only returns the label of the owner, which is resolved by the CAITS API getController of. So it's a very, deterministic.
Thing, rather than trying to define what a workload is, and where up the graph we're gonna say that's a workload versus that's just part of the ownership graph.
**David Ashpole (Google LLC)** 12:04 Have you thought about… How this is gonna work with entities?
You know, like… Does it Is that… I think for entities, we're split across, you know, like, there's a pod entity and a… Replicant entity and the deployment entity, like… Would they all have… An owner ref descriptive attribute?
**Stuart Buckingham** 12:30 Optionally, yes.
And then if…
**David Ashpole (Google LLC)** 12:37 If you get a resource… If you get a resource and it has an owner ref.
Is it the ownerf of my pod, or the ownerf of my deployment, or something else?
**Stuart Buckingham** 12:51 So, it'll only go one level up the graph. So if you have a pod that's owned by a replica set, controlled by a replica set, it will be the replica set.
**David Ashpole (Google LLC)** 13:01 Okay, so… For pods, it'll almost always be the replica set.
But you'll… there's no way to get the… Owner of the replica set as an attribute.
**Stuart Buckingham** 13:14 You would have to traverse again and sort of use whatever metric you're targeting.
If it's just, you know, state metrics, then you can go as a two-step process.
**David Ashpole (Google LLC)** 13:28 I, I see, so… But do… we don't have… do we have the same info type metrics?
as Prometheus? Like, do we… I guess we do have rep metrics that are about a replica set, right?
For those state metrics.
**Stuart Buckingham** 13:46 Yeah, so…
**David Ashpole (Google LLC)** 13:47 we could have the owner F.
**Stuart Buckingham** 13:49 Yeah, the driving thing was I do want to expose this in the CAITS object receiver, just… But because there's no semantics for it, there's no way that I can get that PR merged.
**David Ashpole (Google LLC)** 14:05 Yeah, it's hard because there's no… It's kind of nonsensical for all the regular metrics.
Like, if you have a regular resource associated with a…
**Stuart Buckingham** 14:21 So, from what sort of receiver?
**David Ashpole (Google LLC)** 14:24 Just like my application pushed OTLP to the collector, Right.
**Stuart Buckingham** 14:33 Yeah, so that's where, yeah, we do a lot of… I mean, this is internally, we do a lot of enrichment with the CADS attributes processor, and so it could be used for that to enrich whatever your application metrics are to say that, okay, this is coming from this replica set.
And then if you do need to resolve that to a deployment.
You would then have to, like, do a second level of association.
**David Ashpole (Google LLC)** 15:06 Help me understand, like.
this feels a little bit like a means to an end? Like, what's the… I don't know if you can share, like, the actual end… end goal that you're trying to use this for.
Are you trying to… get it so that you can do correlation for objects outside of what the Kubernetes Attributes Processor does today?
**Stuart Buckingham** 15:28 Is it, like…
**David Ashpole (Google LLC)** 15:28 You'd rather do all the joining in a backend where it's more scalable than locally in some collector.
**Stuart Buckingham** 15:35 Yeah, that's where, like, we can only go up one level, just because that's the only deterministic way. Otherwise… I've had a few conversations with people in Slack and in that issue, and it sort of ends up being… like, it works really well when you're just talking about primitives.
But once you start going out into, like, certificate signing requests and other things where, like, the… the… layer at which you want to define it as a workload is a little less… defined.
**David Ashpole (Google LLC)** 16:09 What's the problem with just walking the owner refs until you can't walk it anymore? Is it that you can get to objects that you don't have permissions to look at, or…
**Stuart Buckingham** 16:18 I think that it just becomes a little bit hazy when you think of… when you get to… CRs, you don't know what the workload is, so I guess you could go to the top level.
If you want to… it's just, like, a less… find thing, it's… let… well… I was trying to find an official definition of what a workload is.
Got it.
**David Ashpole (Google LLC)** 16:44 I don't know if I like the idea of a workload, I'll say, but I'm sure there are opinions there.
I've heard proposals before for something like top-level controller or top-level owner.
I think that would be well-defined.
**Stuart Buckingham** 17:02 Okay, yeah, so just walk the graph until you get to the top.
**David Ashpole (Google LLC)** 17:08 I guess the question is, what do you do if you start walking and you find an owner F that you can't go read, right?
**Stuart Buckingham** 17:15 Yeah, that was also part of it, was that, We don't want collectors to have unlimited additions.
**David Ashpole (Google LLC)** 17:25 Yeah.
**Stuart Buckingham** 17:32 And there's a color… I don't know if… like, custom flux customization, if the deployment has a controller that is the actual Customization, or Helm.
Chop.
Whatever the… the HelmCR is.
So it just gets a little bit ambiguous.
**Christos Markou** 18:02 I wonder what is right now the state of, entities?
in OpenTelemetry and SMAT conventions.
I know they introduced, like, a few months ago, support for declaring… entity relationships. I'm not sure if it is landed, that has been landed already in the tooling, and you can all… Do they express these kind of relationships?
But… To me, adding this controlled by, or whatever, Seems like a denormalization of this relationships.
So, I wonder if this can be expressed otherwise by the entities concept.
Because what you're trying to do here is to actually… Link to entities in a specific way that defines that this entity is controlled by this other entity.
And these are of two different kinds.
Don't have an answer for this right now, maybe it's worth exploring.
**Stuart Buckingham** 19:12 The entities, is that part of the SemCom for work?
**Christos Markou** 19:18 I think so, yeah, the main… And the main Semantic Conventions Working Group, which… meets on Mondays, I think.
**Stuart Buckingham** 19:33 And they have those relationships mapped out in that, like, a pod… Belongs to a deployment.
**Christos Markou** 19:42 Yeah, that was the idea. This group owns the Kubernetes entities, but we haven't yet… like, implemented these relationships. I know that this feature, this addition, was landed in the specification recently, a few months ago. I'm not sure if we can already use it, like, when we actually define Semantic Convention or entities.
I can try and find the link, maybe we can… I can post it later, or tomorrow on Slack.
on the, these groups.
Top.
**Stuart Buckingham** 20:22 Okay, yeah, I'm looking at the resource and entities doc right now. I wonder, yeah, if there's no… What other implementations for Kubernetes?
wood.
Benefit from using entities.
Or is this sort of… would this be the first use case for it?
**David Ashpole (Google LLC)** 20:54 I mean, I assume the… You could apply something like this to the resource detection processor.
Because it does… it also does enrichment.
But it… be a little bit funky. I think this would likely be the first.
**Stuart Buckingham** 21:10 Okay, and I'm happy to go ahead and… explore this.
A little bit, I don't know.
What the… what means to the end is here, but yeah, happy to see if I can make a contribution for this.
**David Ashpole (Google LLC)** 21:28 I… I suspect it.
Being the first always means it takes a long time, so I just,
**Stuart Buckingham** 21:35 Exactly.
Yeah, I think it's sort of a blocker in that we want to… we're relying on CubeState Metrics.
this one particular relationship, and so trying to put this into OTLP is… is a tough arse.
Yeah, and being able to do it upstream would be really useful, so… I know that… I mean, there's… there's… other issues that I linked there that, other people have proposed about adding workloads. I think that workload's just too much of an overloaded term, which is why I thought that Just having the… the parent relationships, the… The most deterministic, but yeah, if it can be done with these entities… structure, I'll definitely try and see how we can implement that.
Cool.
Yeah, that's all if… Next person wants to take a look.
**Christos Markou** 23:03 Okay, sounds good.
Yeah, I will try to look for, what I was describing before, I will share it.
on the Slack channel, just for… So, reference.
Cool, okay, it seems that was it for today. Thank you, folks.
Thanks. Byron.
**David Ashpole (Google LLC)** 23:26 My books.
