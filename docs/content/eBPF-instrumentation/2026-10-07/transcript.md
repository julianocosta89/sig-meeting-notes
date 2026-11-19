SIG: eBPF Instrumentation
Date: 2026-10-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Mario Macias** 00:27 Hello, Nikola.
**Tyler Yahn (Splunk)** 00:43 Hey.
**Giuseppe Ognibene (Coralogix)** 00:46 everyone.
**matt** 01:03 Hello.
**Tyler Yahn (Splunk)** 02:02 Cool, so we could probably get started here in just a second. If you haven't yet, go ahead and add your name to the attendees list, and if you, have agenda items you wanted to talk about, please go ahead and add them there as well, and then, yeah.
Let's, let's jump in here a second.
Okay… Awesome. Alright, so, welcome everyone.
Let's jump in here. So, I guess I wanted to bring this up just for everyone's, just aware of the fact that, like, we turned this thing on, which is, like, in the shared workflow that we have in the repo. It allows, Copilot reviews to be run with, like, using the OTEL, Budget? So, like, I don't know exactly… How reliable it is, I've seen a few, runs kicked off with Copilot, but essentially it'll just keep kicking off, Copilot reviews until Like, it has a successful one.
I also see it ran out of, it's budget?
So, like… I think we're on, like, what, the 7th of the month, or 6th of the month is when I saw it, so I'm, like, not exactly sure how useful it is, but, yeah, just a heads up, like, it's there. I don't know if the CNCF is gonna increase the budget, but yeah.
Cool. Alright, so, next up, I wanted to talk about this, The release that went out is the RC we've been talking about, so pretty excited about that.
It was released as a pre-release, so it isn't actually, like, defined as the latest release yet, but yeah, it's the.
It's essentially the thing that's going to be released as the 1.0. Just kind of a heads up, like, the plan is to make that commit the 1.0, so it's also going to be tagged as the V1.0.0.
So, that kind of… I wanted to bring this up at the top of the issue, because that means that things like, changing public Go API here, and, Nimrod, to your question around.
these sort of, like, breaking changes. Like, we're in the 1.0 release candidate phase, meaning that, like, we're already Complying with what the release candidate.
requires.
Meaning that, like, breaking changes are not allowed at this point.
So, Yeah, like, this… this PR, I don't know if this can go forward, or if we need to just go through some sort of, like, rename process that is… is different, so we would add something, and then we would deprecate it, and then that deprecated field would essentially just call… or the deprecated function would call the new thing, if we wanted to do a rename.
Nimrod, I don't know too much about your… changes here…
**Nimrod Avni** 05:14 It's basically just, changing span names, to conform with semantic convention. I have a couple ones per, like, I have a database one, a Gen AI one.
So it is, like, a… it changes the telemetry, and might add, like, kind of… might change some attributes to match what they should be in Semcov. So the question is, like, do we want… I know that we're, like, in a release candidate, so the question is, like.
I don't mind even, like, waiting with these changes until 1.0, but even in 1.0, I don't know if it's a breaking change, you can even relate to it as a fix, because it's something that's not, like, not correct.
So I, I, I don't know if it's like, if, if that's something that.
Like, as long as we could do it even at the 1.0, I think it's fine waiting.
But the question is, is something like this will even be, like, it's fine for us to do these changes after 1.0. That's the main concern.
**Tyler Yahn (Splunk)** 06:25 Yeah, that's a good question.
So… Yeah, I mean, I can see it from both perspectives, like, people are looking for stable telemetry at this point with the 1.0.
But… To your point, also, that, like, this is, like, a bug that isn't, like, it's not correct.
And the semantic conventions, like, in the schema, this kind of change is allowed, right?
**Nimrod Avni** 06:50 Yeah, I think, like, when we release every version that we release, basically, we create this sort of, like, it basically means our schema is evolving, or, like, and you can provide, kind of, like, migrations, like, you can say, okay.
If you wanna, like, take the, you know, use the previous name, you can just do some processing rules to take the… you know, the span name from the not correct one. So it is allowed.
And I would say, like.
Like, it's fine to change telemetry. I think that makes… Sense. It's easy, I mean, it's easier to do before we, declare the, you know, OB stable.
But even after it's stable, we would probably want to… let's say, like, we upgrade the semantic convention between, like, that we rely on from 141 to 144, there might be some breaking changes that we'll need to do, so it makes sense. Right?
So, as long as we provide some… Like, migration path, or like… Say, like, declare it as a breaking change.
To the…
**Tyler Yahn (Splunk)** 08:03 Yeah, in the schema, right, you're talking about, right?
**Nimrod Avni** 08:05 Yeah, totally.
the release notes thing.
**Tyler Yahn (Splunk)** 08:09 Yeah, I mean, I think that's going to have to.
be the case, because we have things that are released that are not stable in semantic conventions, right? So… Like, database is stable, so we should probably get that right.
But yeah.
**Nimrod Avni** 08:24 AW specifically, that's something that's wrong with, like, most of these stuff here is, like, stuff that are wrong with OB and not semantic conventions, but yeah.
**Tyler Yahn (Splunk)** 08:33 Okay.
Yeah, I mean, so… so that makes sense to me.
like I was saying, though, the 1.0 is not going to contain this change, right? Like, the 1.0 is going to be just the original commit for the 1.0 release candidate, and then this, and then… I don't see why, like, a 1.1 doesn't come out pretty quickly after the 1.0, which would contain this change.
Which seems fine to me.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:59 Yeah.
**Tyler Yahn (Splunk)** 09:00 Yeah. Nikola, you also, yeah, go ahead.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:02 Yeah, I agree as well. I mean, we're gonna find bugs.
There's there's just no like, these are bugs, in my opinion.
I think we should, we should just do it.
If customers can actually complain about anything changing on them, we can easily explain, though this was… this was wrong, and it's not according to the spec, we're conforming to the spec.
**Nimrod Avni** 09:24 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:26 Yeah.
**Nimrod Avni** 09:27 Just to, like, you're saying that the 1.0 commit is, like, we're already… It's already like stamped. Like if we merge stuff, they won't go into the 1.0 commit.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:37 Yeah, yeah, but we make 1.1.
**Nimrod Avni** 09:40 So does it make sense to, like, after, like, this gets approved and whatever, to merge it now? Like, we don't need to wait Until release. So, like, we're not blocking any main merges or something like that.
**Tyler Yahn (Splunk)** 09:54 know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 09:54 the.
**Nimrod Avni** 09:55 Okay.
**Tyler Yahn (Splunk)** 09:57 Yeah, the idea is to just add another tag to that, commit that was the 1.0 release candidate. That's just gonna be 1.0.0, and then… Pushing that should kick off the CI to run that as a 1.0 release, yeah.
Yeah.
So yeah, merging this onto main, merging new features onto main.
They'll all be in the 1.1.
So, but yeah, they're ready to go, essentially, yeah.
**Nimrod Avni** 10:25 Okay, so I just want to make sure that we're not, like, blocking… they have, like, some feature freeze with, like, merging stuff.
**Tyler Yahn (Splunk)** 10:32 Implicitly we do, just because I don't think you can redo that commit, but yeah, no, not.
**Nimrod Avni** 10:38 I mean, yeah, but for, like, 1.5…
**Tyler Yahn (Splunk)** 10:39 Usually, yeah.
**Nimrod Avni** 10:40 You know, the next ones are like main silver. Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 10:43 Yep.
**Tyler Yahn (Splunk)** 10:43 I'm being cheeky, but I gotcha, yeah. That being said, I would ask… so, hopefully by next week's meeting, please, like.
Actually, I guess maybe we… Nicola's already got something, but, do come up with something, like, if you have issues with the 1.0, like, commit that we, like, need to actually fix, that's a blocker that we need to do another release candidate, I guess, sooner rather than later, maybe even before next week. Please take a look, I guess is what I'm asking.
Nikola, you wanted to talk about this one, though, the regression in Go?
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:18 Yeah, somebody just opened up this just this morning. I saw it. I don't know if you should block on this. I just wanted to bring it up. It seems like some new probes we added slowed down.
And they had to revert to 0.9.
Wow.
**Tyler Yahn (Splunk)** 11:33 big reversion.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:35 Yeah, I guess they weren't sure. They made a jump from 0.9 to 13, and they saw P99 getting worse.
I mean, I don't know, this analysis here is probably done by an agent, but, looks plausible. They even have, like, PRs that we've added.
It seems like we just made some probes related to GRPC path or HTTP/2 a little bit.
Heavier, because now they're updating the maps for the, For the socket filter. Sona, the question is here, I think is rightfully so. I mean, if… if BPF ProBright user is available.
In which case… that means that we can do goal context propagation without the socket filter, essentially. Do we need to bother? It's a valid question, so… But I don't know if we should block the release or just go on 1.1.
**Tyler Yahn (Splunk)** 12:35 No, I… yeah, I definitely don't think we should block the release on this. Like.
It's a horrible saying, but I like to say fail forward. So yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:44 yeah.
**Tyler Yahn (Splunk)** 12:44 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:45 I mean, they have a way back, I mean, they can revert, so…
**Tyler Yahn (Splunk)** 12:49 Yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:50 Yeah.
**Tyler Yahn (Splunk)** 12:50 I would like to understand, like, it doesn't sound like it's happening all the time, and it is a very specific workload that's causing this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:57 Yeah.
**Tyler Yahn (Splunk)** 12:57 That was… yeah, so… we probably need more information still, but I… yeah, I mean, I definitely think that, like, it's just about trying to figure out a solution for them.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:06 Okay, cool. We're treated as a regular bot, yeah.
**Tyler Yahn (Splunk)** 13:09 Yeah, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:11 Giuseppe?
**Giuseppe Ognibene (Coralogix)** 13:12 Yeah, sorry, I had a question about the previous topic. So I had a PR that was about to renaming, yeah, this one, renaming container store. So what I have to do with this one? I can leave it there, or I can close it and reopen after.
the risk candidate is out. I… I missed this, I mean…
**Tyler Yahn (Splunk)** 13:37 No, this is a 2.0 change at this point.
**Giuseppe Ognibene (Coralogix)** 13:40 Okay, so from… What time to do?
**Tyler Yahn (Splunk)** 13:45 So, I… so this… this… this can't happen in a 1.0, right? Like, this is changing the API, this is in the public package, right?
What you can do is, you can… we can go through a deprecation process of this, so we can create a new function called kubestoreupdateprovider, and then… that's, you know, that's this. But we have to maintain the existing container store update provider, and just say that that function is deprecated. There's a Go syntax for deprecating things, where you can… Put it deprecated.
**Giuseppe Ognibene (Coralogix)** 14:16 is.
**Tyler Yahn (Splunk)** 14:16 Cube sort, yeah, and then it just is gonna sit around until we get to a 2.0, and then we can remove the container store updater provider.
**Giuseppe Ognibene (Coralogix)** 14:24 Okay, I will update it. Thank you.
**Tyler Yahn (Splunk)** 14:26 Yeah.
Yeah, it's kind of a bummer. But, but yeah, I mean, that's… yeah, otherwise, just leave it. I don't know if this is, like, a super important thing that we wanted to change either, but, if it is, that's the way to do it, yeah.
**Mario Macias** 14:40 No.
Yeah, from, this is… this is mainly… this will mainly impact anyone that uses OB as a… as a… as a library. From the Baylor side, for example, is a minimal change. Even if it breaks, it's just replacing it. We are not even… we are not even using it, so maybe that could be in the… could be… place in the… in the private API.
But yeah, anyway, as you… As you feel, Chilby.
**Tyler Yahn (Splunk)** 15:17 Yeah, Matteo, you could also just remove the to-do comment, that's also valid. Yeah, there's nothing… I mean, like, especially at this point, right? Just, yeah, it is what it is.
Yeah, and then, like, maybe Giuseppe, also, if you wanted to think about… if you wanted to create that other function, you could just create the other function internal, if nobody's actually using that function.
But… Yeah, it's… Up.
to be… to be honest, I think Batia's suggestion might be the best, but yeah.
Or…
**Giuseppe Ognibene (Coralogix)** 15:48 usually.
**Tyler Yahn (Splunk)** 15:49 Yeah, yeah.
**Giuseppe Ognibene (Coralogix)** 15:50 I don't have a strong opinion, I just saw what to do, and I… I was doing it,
**Tyler Yahn (Splunk)** 15:58 Oh, okay. Yeah, I guess.
**Giuseppe Ognibene (Coralogix)** 16:00 Gotcha.
**Tyler Yahn (Splunk)** 16:00 I gotcha.
Yeah, well, thanks for… thanks for cleaning it up, just unfortunately. It's also… also, thanks for having a great example of what we, want to talk about for the 1.0. So, yeah, very timely.
Okay.
Cool, alright, then I think with that, let's keep an eye out, like.
Yeah, like, if there are things where you're just like, we cannot live with this in a 1.0, we can't, like, fall forward.
I totally see, like, a 2.0 happening for OB. I don't know if that's going to be in 6 months or in a year, but just, you know, kind of keep that as your timeframe, right? Like… Can we have a deprecated function around for 6 months?
in my mind, sure. So, that's not too big a deal for me. But, if there are other things that are too big a deal, like, this needs to get changed tomorrow, then let's… let's look at our release candidate 2.0, as fast… or release to, as fast as possible, so, yeah.
Okay, moving on, I think, Nimrod, you also wanted to talk about… Sorry, the CASE cache. Yeah, let's talk about this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:12 1.
**Tyler Yahn (Splunk)** 17:13 Well, so, one of the… things that we… I actually saw that you had, like, this issue here.
don't want to step on your feet too much. Just for maybe folks on the call, like, one of the things that, like, we did is we have… OB is shipped as an OpenTelemetry receiver. That OpenTelemetry receiver is very isolated in what it does, that it doesn't essentially reach out, it only does receiving of information from the the kernel space eBPF, that kind of thing. That was one of the things that, like, the OTEL or the collector folks were really kind of big on in trying to get this receiver accepted.
So we split our configuration across these boundaries, and because of that, you are no longer able to communicate with the Kate's cache, because you're not able to set that up. So… one of the things is that that provides, like, a limitation on the richness of what, like, identification can be done, and, so there's… user issue here, pointing out that it's not possible to use that, which is kind of intended. But then there's also, like, still that… question of, like, well, that's great, but, like, can we do better? And, the do better was actually, like, we need to create an issue with OTEL guys, or the collector guys, and see, like, if we can do better, which, Nimrod, you've already done, which is great. I totally forgot that you did this, on July 1st, so…
**Nimrod Avni** 18:38 Yeah.
**Tyler Yahn (Splunk)** 18:38 It's been a while.
**Nimrod Avni** 18:40 So I can say, like, the… just for… I think most people were aware, like, the case cache, and I think Nikola did, like, a more extensive search of it, is mainly for, like.
why we don't use just the local, like, Kubernetes, like, Kubelet or Kubernetes API is because the OB does, like, basically, like, client enrichment, like, we get between, like, pod-to-pod communication.
you want to enrich the client IP, and not only your IP as well. So the client IP might come from a different node, and if you're only reading the local cube blood, you don't have that metadata.
And if each pod reads the entire state of the cluster, then it really kills any like scale, like high scale Kubernetes deployment.
So the K8s cache is just, like, a central component. You, like, deploy, I don't know, like, two, three pods, whatever, and then they just… every… all of them launch, like, share the entire state of Kubernetes between all the OB pods, and they save it in memory.
So.
So, yeah, that's something that, like, Obi does that… and, like, if we… if we… like, it's something Obi always done, but it might not be his responsibility, because we have the Kubernetes attributes processor that should be doing all the Kubernetes enrichment, but… the two main things that are missing are the two that we have, like, the two stuff that I mentioned, like, one is enriching Any client operation, I think, I think, the attribute processor only enriches.
you know, based on an IP, enriches the, like, local pod, and it sets stuff like, you know, the resource attributes of Kubernetes pod name and whatever, whatever, but not the client ones.
And the other stuff is, like, the other issue is that it can't… it can either read from only, like, only the local Kubernetes API, or the, like, go through the Kubernetes API, but you have, like, a fleet, then it's the same issue.
So I suggested, like, it's probably two issues that we can have upstream. It's like, one is allow… have some sort of other component. I suggested, like, a hotel extension, but whatever that… act as the K8s cache, and then have it, like, communicate with the Kubernetes attribute professor, and then have an ability to enrich client stuff, and then we can enrich both, like, peer service, and I think, Nikola, you said for, like, service graph metrics.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:09 Yeah, network metrics, same.
Without that, you just get IPs and not very useful, right?
**Nimrod Avni** 21:17 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:20 It also doesn't, I mean, not reaching out, I don't know where that leaves us with the cloud vendor as well, because we do reach out now to cloud, to get cloud metadata.
So that also would… have to be delegated to the collector at some point in the receiver mode.
**Nimrod Avni** 21:39 Don't be… Nikola Grcevski @ Grafana / OpenTelemetry 21:39 the.
**Nimrod Avni** 21:40 The collector doesn't have any like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:43 They do, yeah.
**Nimrod Avni** 21:44 So we're just doing it in OB because, like, for people that don't deploy it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:49 yeah.
**Nimrod Avni** 21:50 That's.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:50 Yeah.
But I think the main challenge is that without the CADS cash, This… I mean, telling people, yeah, use it with a cluster is just playing with fire.
Yeah, because, I mean, and it's not just us, right? So, I've seen talks where Cilium shows that they have this component because of the same reason.
**Nimrod Avni** 22:16 Yeah, I think I found out, like, other, like, there's, like, Ground Cover and Pixie.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:20 Yeah. Like, a lot of people.
**Nimrod Avni** 22:21 We have this sort of, like, architecture.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:24 Yeah, it's a must because the Kubernetes API, I mean, when we first deployed it in prod, we took it down. Like we took it down prod at Grafana. Yeah.
So the Cube API, even though it has auto scaling or whatever, cannot keep up. Depends how many nodes you have to deploy on.
**Nimrod Avni** 22:45 I think, like, the main… Like there's like two issues of like, what do we do for the future? Like we can suggest this type of, of solutions upstream to OTEL and talk about that. But like the question is, what do we do now? Do we say you can't have this client enrichment, and, and network metrics and stuff like that if you're running OB as a receiver?
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:07 Or.
**Nimrod Avni** 23:07 Or do we tell them like, this is something that's, you know, we know it's kind of a hack, but it must be done now in like scalable deployments.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:19 Yeah, we commit to deprecate it once we have it, because, I mean, a lot of things will fail, like, even if in your traces, when you see peers or any information we put in there, that's just not going to be there if we cannot resolve the name.
**Nimrod Avni** 23:30 Even the, yeah, like, the the host name stuff.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:34 yeah.
**Nimrod Avni** 23:34 You have like, like DNS resolvers, right? Do you have Kate's ones?
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:38 That's right. The case one was just not work. And then.
**Mario Macias** 23:42 yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:42 Everything will be just bare bone IPs, which is not very useful to anyone.
**Mario Macias** 23:47 Yeah, and also take into consideration that the metadata is required also for the service discovery and selection.
**Nimrod Avni** 23:59 Yeah, Nikola Grcevski @ Grafana / OpenTelemetry 24:01 That could be on local network.
**Nimrod Avni** 24:02 I guess that can even come only from the local.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:05 local, because that's only the local that we really care about. You're not going to add a service on a global.
So,
**Nimrod Avni** 24:15 Mhmm. Roy, wanna.
**Roy Reshef (Kubex)** 24:19 Yeah, just, I assume CATES Cache is based on Informers, right?
**Nimrod Avni** 24:25 Yeah.
**Mario Macias** 24:26 Yes.
**Roy Reshef (Kubex)** 24:27 And one thing, again, I do not have experience with this in large clusters.
But one thing you have to be very careful is, and this I'm speaking from experience, from trying to deploy, for example, CubeSake metrics, if you're familiar with it, in massive clusters. I mean, clusters with… Tens of thousands of pods and the like.
Yeah. You run into a few issues. I mean, A, you can take down Kubernetes API as well.
Yeah. Or you just break OOM, and we ran into issues that… so CubeSight Metrics has a notion of sharding. Which you may want to consider here.
Because you cannot have… I mean, you have a limit to how large a pod can be, and how much memory you can allocate to it. I mean, I've seen cases where CubeStack Metrics needed more memory than the node could allocate to it.
If you don't start charting it.
So you, again, I mean, it may be that in our case of Kate's Cash.
you don't need that many informers, because KubeState Metrics really can have informers on pretty much everything that exists in Kubernetes API.
But, still, it's some points to be… if you're really looking at massive clusters. And you're looking at these central components, which are not node-specific.
But try to enrich it based on.
On, you know, cluster metadata, you have to be careful with these kind of things.
**Mario Macias** 26:04 Yeah, that's the reason why we separate the cubes… the cube cache. It was initially shipped inside Vela, but as you say, we took down some big clusters, so that's why it's now deployed as a separate component that is… runs as a… replica… a small replica set, so you only have few… you only have few nodes.
interacting with the… with the informers are… is Bayla. Bayla, instead of connecting directly to the informers, connect to the instances of the cache. This way, we'll resolve these… those issues with the… within.
**Roy Reshef (Kubex)** 26:46 But even if that… if… I mean, the approaches they took in Cubestate metrics, which I had to… I don't like this component, but I had to study it. They literally went into the direction of stateful set.
And… which is something you cannot really have with a bare-bone deployment, because then you can have, like, you know, predictable pod names, and based on pod names, and on some hash function of the UID of the object, it goes to shard 0, or shard 1, or shard 15, or whatever.
**Nimrod Avni** 27:17 In keeping all the Kubernetes objects in memory, like one pod can't keep all of them in memory?
**Roy Reshef (Kubex)** 27:24 Yeah, you just run out of memory very easily. Even if you're limited to only pods and services, and I… I don't know what else Kate's Cash has informers on. I mean.
**Nimrod Avni** 27:34 big-name.
**Roy Reshef (Kubex)** 27:35 really.
**Nimrod Avni** 27:35 Namespaces, services, and pods.
**Roy Reshef (Kubex)** 27:39 Yeah, so… I mean, you may be better off here, because you don't have that many informers, but still.
I mean…
**Nimrod Avni** 27:48 The only, like, the only thing I'm thinking of, if, for example, like, right now, I think this is how it works, like, the CATES cache, basically, each OB pod, talks to, like, one CATES cache component, but it still keeps, like, a full map of all the Kubernetes pods.
**Roy Reshef (Kubex)** 28:04 This can also blow out of proportion.
**Nimrod Avni** 28:06 maybe.
**Roy Reshef (Kubex)** 28:07 If you really have a massive cluster, you will run into issues.
**Nimrod Avni** 28:09 But maybe as an optimization, we can, because.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:13 I.
**Nimrod Avni** 28:13 You don't need the entire, like, all the pods, you just need all the pods of services that, like, you're talking to, so maybe it can be something, like, on demand, like, you know, I'm seeing this IP for the first time, I'll fetch it, and from now, I'll save it, or, like, I'll subscribe only to this, like, service.
But I never ran into it. I know if people in Grafana ran into, like, even with the case cache, that OB memory exploded.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:42 Yeah, it… I mean, on large clusters, people do complain often, sometimes, or… I mean, about, oh, why Zovi needs 1GB of RAM, or whatever, and we know it's… I mean, it's usually environment variables and Kubernetes metadata that's kind of causing that memory bloat, but your idea is great. I think we can… if the Qt Cache case caches deployed, we could definitely just go on demand and cache, or maybe even LRU, and just consult with the cache when we need the data.
**Nimrod Avni** 29:14 I think if I, like, if I'm planning to propose this kind of solution, I can, like, bring it up as, like, we can support this kind of, you know, supporting on-demand fetching instead of the attribute processor storing the full map, because then we'll be on every collector.
Yeah, but that's a really interesting concern I haven't thought about.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:40 That's a good point, yeah. So I guess I want to ask questions for this issue. Do we just — I mean, can we bring back the option and not actually go 1-0 with a collector receiver?
I mean, 1L OV, but not actually… Claim that we have stability on the collector-receiver until we resolve this issue.
Because we want people to use the collector receiver and experiment with it, and they'll tell us stuff that's missing.
And, I mean, especially with OpAmp, it's really nice, you know, having the ability to push remote configs, and you just pick up, and you can change instrumentation on the fly, whatever you like, so… I mean, I think we need to find a solution for 1L for this, but as… Because we committed to 1-0 for OB, but not committed to the OB receiver, so maybe that's… That's an option.
**Tyler Yahn (Splunk)** 30:38 Yeah, the problem is that they're all in the same module.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:43 I know. So, I mean, without this feature, I think the OB receiver is just crippled and might as well not even advertise it. That's what I'm saying.
**Nimrod Avni** 30:52 Yeah, at least on Kubernetes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:54 With Kubernetes, yeah.
Which… Right.
**Nimrod Avni** 30:57 of the world.
Bye.
**Tyler Yahn (Splunk)** 31:04 Yeah, so what's the proposal?
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:08 Proposal to maybe add that option back in. So we have the ability for now and with a commitment that will deprecate it when what Nimrod is proposing is made upstream and a first class citizen in.
**Tyler Yahn (Splunk)** 31:21 Yeah, I don't think we could do that. That… that's… That would mean that we're violating what we told the collector people that we wouldn't do.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:33 Happy to…
**Tyler Yahn (Splunk)** 31:33 Happy to readdress that if like we get sign off from the collector people, we can renegotiate that contract with them.
Like, that… that seems fine.
But just doing it unilaterally, like, that's… Not really.
**Nimrod Avni** 31:47 It makes sense to talk with them and say, like, this is… like, I can write up this kind of issues, I think, both of them upstream on the collector, and then we can say, okay, we have those two issues, upstream until, like, those are stuff that OB already does, kind of, like, its Kubernetes enrichment does.
And without it, like, deploying it on Kubernetes, we must have this.
So, you know, until this is resolved, we probably need to have.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:16 interim solution of some kind.
**Nimrod Avni** 32:20 Does that make sense? Like, I can open those issues and then we can talk to the collector people and point to them?
**Tyler Yahn (Splunk)** 32:29 Okay, that sounds good. But what about for us? Like, are we looking at trying to split out the collector receivers from this 1.0? Because that's going to require… A second release candidate.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:45 Yeah, I mean…
**Tyler Yahn (Splunk)** 32:47 It's probably gonna also require another release to deprecate the existing…
**Nimrod Avni** 32:52 I mean, we can, like, we can treat it as a bug and resolve it in 1.1, I don't know.
**Tyler Yahn (Splunk)** 32:59 Absolutely. We can definitely fix this, like, case caches in 1.1. I definitely see that as an option as well. But to Nicola's point, like, if we don't want this… Receiver to be 1.0, like, we need to fix it.
Today.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:13 Because, I mean, it's unfair to release it, to be honest.
**Tyler Yahn (Splunk)** 33:18 I don't know, I don't see it as, like, too big of a problem. Like, I definitely see it as, like, a… a problem. I definitely see it as, like, something where you're saying, like, it's not that useful to use this collector receiver in Kubernetes, like.
Yeah, I agree.
But, to… to not say that, like, we can't find, like, a solution for it going forward, I guess, like, that's maybe… Like, like, yeah, like a 1.1, 1.2, something like that, we have like, okay, we found out like.
the collector team wants to have the CAITS processor actually handle this, like, is it going to work? They also say, like, okay, maybe that's not the solution. They say, like.
the CATES processor needs to, like, be its own project, and so we just spin that up, and then, like, we're able to talk to it at that point, like.
these are all things that, like, I think we can do in a 1.1, or, like, in a 1.0 world, right? Like, I don't think it requires a 2.0 to, like, get all that feature set in.
It's more just, I think, about, like… what we're comfortable and flexible and, like, what we want to signal in the 1.0 of this receiver, to Nikola's point, right?
**I think that's… Nikola Grcevski @ Grafana / OpenTelemetry** 34:27 I would say this is experimental. The receiver is experimental, and we put the caveat that it will not work well with Kubernetes because we still haven't done the work to merge with the collector Kubernetes data. I mean, it's not a great answer, but…
**Nimrod Avni** 34:40 Yeah, it's like, it'll, like, if we don't propose, like, if we propose to read from the local Kubernetes.
You know, storage, and it will just work, but without any peer enrichment. Like, basically, every… like, every, like, you know, peer name and network metrics won't have a destination.
Like, we can add that as, like, caveats. If you're running…
**Tyler Yahn (Splunk)** 35:06 The thing is…
**Nimrod Avni** 35:07 In general, if you're running OB without a CATES cache, but specifically in the receiver, you have to.
**Tyler Yahn (Splunk)** 35:14 I just want to focus this conversation on like the tangibles of what we can actually control. So, like, if you want to signal that something is like experimental, like we need to we need to do that by splitting the modules.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:24 Mmm.
Okay, okay, so then we just document that there's gonna be… there's a potential here for… It's not… some data may be missing when you're running this Mode.
Cool.
**Tyler Yahn (Splunk)** 35:40 Yeah, I mean, that's… that's… that's definitely an option.
But, like… I guess I'm asking, like.
I can split the modules as well, and so, like, I'm wondering, like.
We need a decision, like, here in this meeting.
**Nimrod Avni** 35:56 I don't think it should.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:57 Yeah.
**Nimrod Avni** 35:58 split, because the… I mean, it's only, like, you can say it's, it's specifically in, like, Kubernetes. So, like, the, the, you run OB receiver on any, like, VM or whatever, then it just works completely.
**Tyler Yahn (Splunk)** 36:13 Yeah.
**Nimrod Avni** 36:14 So, I think it's more of a… like, if we didn't have this feature in OB, like, in normal OB, then it would just be a missing feature. So I think it just, yeah, it's just, you're running it with this set, it's just missing some features, and it's not, like, unusable.
**Tyler Yahn (Splunk)** 36:34 Yeah, I agree.
It is on… it is… less than usable… it's not… it's usable in Kubernetes, it's just not that helpful in Kubernetes, right? Especially for large clusters.
Gosh.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:47 Okay, okay, so honestly, I think nothing… nothing will stop Obi from… from within as a collector component, from grabbing the data from Kubernetes, right? I mean, if you're in a Kubernetes, we'll get it. The thing is that there's no cache.
And so if you deploy this in a large cluster, it's just gonna blow up. So that's the only thing. We don't have our escape hatch because I don't think anything we have in the code stops us from actually talking to Kubernetes API.
**Nimrod Avni** 37:15 I don't think so.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:17 So it will work, it will work, but it will not work on large clusters. That's the thing.
**Tyler Yahn (Splunk)** 37:22 Wait, what about that original issue from the Ozzy Walsh guy?
Oh, he's just saying that he's not able to configure the address, so he… not necessarily that he's not.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:33 Yeah, it's just the option is missing. So if we were to add the option.
I mean… It's not on by default.
So… If the option was there, there would be no issue whatsoever.
That's what I'm saying.
**Nimrod Avni** 37:48 Can they configure, with, like, the OB receiver doesn't work with V1 config?
**Tyler Yahn (Splunk)** 37:56 No, it's so… Nikola Grcevski @ Grafana / OpenTelemetry 37:58 Okay.
**Nimrod Avni** 37:59 I think, yeah, exactly.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:01 Indeed.
**Nimrod Avni** 38:01 Can they do it?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:02 Yes, they can do it. Yeah, he's just saying it's not in V2, and I want to use V2.
**Nimrod Avni** 38:07 Oh.
**Tyler Yahn (Splunk)** 38:07 Yeah.
**Nimrod Avni** 38:08 I think it's even, it's even like a narrower, issue. Like we want to, of course, like migrate people, I guess, to, to V2, but.
**You have this kind of escape hatch, and until… Nikola Grcevski @ Grafana / OpenTelemetry** 38:20 Maybe then it's not a big deal. Then for V2, we eventually gonna solve this with a collector upstream.
produce the cache component, let's push on that, and then for V2, we're just gonna say, well, if you want to use this with V2, then wait until this is done, and… And at that time, Hopefully, we have a full… Gotta… Yes.
Work… we fully work with the case processor, and that's it.
Okay.
**Tyler Yahn (Splunk)** 38:49 Seems like a good plan to me, yeah. Okay.
Okay.
So takeaway then, we're going to keep going.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:57 Yeah.
**Tyler Yahn (Splunk)** 38:58 the.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:59 No blocking, okay, no blocking.
**Tyler Yahn (Splunk)** 39:00 you Nimrod, you're also gonna follow up with the collector folks. I don't know if maybe you can join, like, the collector SIG, meeting. It's at a weird time.
**Nimrod Avni** 39:10 I don't know if they have, if they're like a specific Kubernetes SIG or is it just collector?
**Tyler Yahn (Splunk)** 39:17 No.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:17 Let me go.
**Nimrod Avni** 39:18 Other Kubernetes, Semkov, SIG.
But I don't know if there's a Kubernetes, like, okay, so I'll join the collector when it's in, you know, not 3 AM for me, so…
**Tyler Yahn (Splunk)** 39:30 Yeah, I was gonna say.
It's a weird one, in that sense. But yeah, if you could just get some, like, eyes on it, and then, And maybe also we could just ping like Dimitri and Antoine are two people that I know have looked at this in the past. I'll try to ping them on that issue as well and see what their thoughts on it are. But is that issue up to date?
**Nimrod Avni** 39:48 There's one, like, right after the OB-SIG. Like, I don't know if I have time to, like, I can just, like, talk, but I don't know if you want to come more prepared.
**Tyler Yahn (Splunk)** 40:00 Yeah, oh, I see what you're saying, yeah. Well, as we just said, like, it's not super critical to get done today, so,
**Nimrod Avni** 40:08 We'll do the one next week, I guess. It's the same. It's also, like, at noon for me, so I think it's fine.
**Tyler Yahn (Splunk)** 40:16 Okay.
Great, yeah, then let's… let's plan on that. Let's have you… Pick that up. That sounds like a good plan.
Okay.
Two more things. Last up, I wanted to talk about.
A PR I opened. I just saw Nikola, you reviewed this recently.
It's around our testing shards. So, you know, one of the things that, like, drives me mad is CI, which I don't think anybody on the call is different, but I was noticing that, like, every time that we rerun a test, like, all of the successful portions of the tests are rerun as well, and there's really not a reason it should. Like, the sharding's great, because we can split things up across Like, in theory, the best thing would be, like, every single test that we run is its own job, and, like, each one of those jobs set up time is 0 seconds, right?
This is completely unreasonable, because the setup time is not zero seconds, and, like, we would have thousands of jobs and blow out the CI budget. So, like, we can't do that. So that's why we started to do the sharding. The problem is, is that, like, when you do the sharding, it, like, collects, I don't know, tens, maybe even 100, actual tests that it runs.
And one of those tests, you know, the law of averages of it being flaky and it flaking out on you is pretty high, like, that's why we see a lot of CI churn.
So when you rerun this, you rerun all of the successful tests as well.
So, the idea with this PR is to say, like, okay, like, keep some sort of test recovery record, and, like, any sort of rerun, just run the failed portions of it, not the whole, like, thing. Which… Stephen H. it's still not zero time, like, it's still gonna be a, you know, setup time, plus some of these tests take a little while, but it's definitely, I think, should help reduce the amount of time that we're actually seeing these things run, so… Stephen H. Yeah, I just wanted to pull this up. I see also, Matia, you just commented, I haven't read this.
But yeah, I was looking for some more eyes, looking for things just like this, so I'll take a look at this, but just wanted to bring it to people's attention.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:19 Cool.
Yeah, that would be great. That will reduce the time we're spending CI. The retry.
**Tyler Yahn (Splunk)** 42:24 Open. Yeah.
Right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:27 Still haven't started on my journey to combine tests and whatever.
**Tyler Yahn (Splunk)** 42:31 Yeah, that… that, I think, would also really help. I haven't started on my journey to move all of us to Config V2, so… A lot of work to do.
Okay, and then last up, Mario, you want to say hello to Gregor? Hey, Gregor.
I don't know if Gregor can hear us.
**Mario Macias** 42:50 you.
**Gregor Zeitlinger** 42:51 Yeah, I can hear you. Just had to unmute. I hope you can hear me too. Yep.
Hello.
**Nimrod Avni** 42:57 Hello.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:59 Okay.
Gregor is yeah, join our team.
that's going to work on Obi. He's well known in the Java SIG, I guess. Yeah. Yeah.
**Gregor Zeitlinger** 43:11 That's where I spent most of my time in the last years. Now I'm excited.
To do some hacking here.
**Tyler Yahn (Splunk)** 43:23 Yeah, I'm super excited to see you here, Gregor. But I've got.
reasons for that, and that's mostly because the configuration, the instrumentation configuration, that you wrote a lot for, like, the Java instrumentation, like, we could definitely use some help on that, like, integrating the OB configuration. Right now, we're kind of sitting on the side, but I'd love to see your expertise and drive, try to help, yeah, get that declarative configuration, like.
Us as a better story for that going forward, so yeah, yeah, I'm super excited to see here.
**Gregor Zeitlinger** 43:51 Definitely.
**Tyler Yahn (Splunk)** 43:56 Awesome.
Cool, alright, well, with that, we are at the end of the written agenda. Any other topics folks had?
**You have… Nikola Grcevski @ Grafana / OpenTelemetry** 44:08 I just want to say I'm away next week. Yeah.
**Tyler Yahn (Splunk)** 44:10 Oh, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:11 Sorry, yeah, I added in the notes, I won't be here, I'm on vacation.
**Tyler Yahn (Splunk)** 44:17 Cool, all right, good to know.
Their deadline for the CFP for KubeCon, EU is the 11th, so you have 4 days left, if you have talk ideas, or you wanted to go, come up with talk ideas. So, you should come up with talk ideas.
**More than half of this audience right here is, Nikola Grcevski @ Grafana / OpenTelemetry** 44:38 Can we try the longer arrangement again to get it in?
**Tyler Yahn (Splunk)** 44:42 That'd be a cool one. Yeah, I definitely think so.
**matt** 44:45 I can try, I can just copy-paste the… Nikola Grcevski @ Grafana / OpenTelemetry 44:47 Yeah.
**matt** 44:47 Yeah, I can try.
**Nimrod Avni** 44:49 Now, now you can link the blog post. Blog post, yeah. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:56 I mean, let me know if you want me to look over the proposal. Maybe we can spin it as more of a customer story, how it helps and what it helps. I didn't look at the proposal to see how it was written. Like KubeCon, sometimes there are certain words.
**matt** 45:09 I can try to export it and post it in the… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:15 Yeah, just post it there. Just let me look over, just if I have any suggestions. Let's see if we can get that one in. I think that's important. And I think you submitted it for Japan, right?
**matt** 45:27 Yes, Japan, and then North America.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:29 And it didn't get in there either, okay.
**matt** 45:32 laughs.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:32 Okay, maybe we'll have a chance, maybe we'll have a…
**Tyler Yahn (Splunk)** 45:34 I think you have a better chance getting into EU just as you're an EU citizen.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:39 Yeah.
I.
**Tyler Yahn (Splunk)** 45:40 I've definitely noticed they try to prioritize that, so… Nikola Grcevski @ Grafana / OpenTelemetry 45:43 I see you people. Yeah, for sure. And Japan is so small anyways, so that they've got lots of… proposals, so I think we have a chance to get any.
**matt** 45:55 Let's try. Let's try again.
**Nimrod Avni** 45:58 Do you know if the proposals are only for the main KubeCon? There's also the main… Nikola Grcevski @ Grafana / OpenTelemetry 46:05 You bet.
**Nimrod Avni** 46:05 Amen.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:06 Yeah, so observability day. So there's two. You need to make both, KubeCon main and observability day, which is the co-located event,
**Roy Reshef (Kubex)** 46:15 I think the Kolo is a week after the deadline, the main event.
**Tyler Yahn (Splunk)** 46:18 Oh.
**Roy Reshef (Kubex)** 46:19 Monday, and I think the call was a week later, something like that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:22 Yeah, but usually…
**Tyler Yahn (Splunk)** 46:24 time.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:25 Yeah, you have more time, but make the proposal submitted in both places and It should give you a better chance. You just submit it to.
**Nimrod Avni** 46:34 Do both, you mean?
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:36 Yeah, you submit to both, and I think one of them asks you whether you've submitted already to KubeCon, so then they… the committee will just kind of see, okay, we like it for this, but if it's already there, accepted, then they won't… Accept it either way, or something like that, they check.
Hmm.
**Tyler Yahn (Splunk)** 46:53 Yeah, and it's usually as easy as, like, a drop-down. Like, if you've submitted it to the main track, you can just be like, I'm resubmitting here, and it will just, like, populate all the fields for you, so… yeah, it's really simple.
**matt** 47:03 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:03 And then maintainers track. I'm working with Kamal from Datadog that works on OTLC to submit one joint one for the donation.
But maintenance track is also another one. If we have a topic of, Anything, how we've built the community, the kind of approaches, maybe anything of the struggle.
**Nimrod Avni** 47:26 All the Weaver stuff with, like, the… Nikola Grcevski @ Grafana / OpenTelemetry 47:29 testing.
**Nimrod Avni** 47:30 Schema and stuff, I don't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:32 Yeah, man.
**Nimrod Avni** 47:33 more in like the maintainer summit because it's more for like people building Nikola Grcevski @ Grafana / OpenTelemetry 47:39 Yeah, that would be very useful. I think people want to hear our experience, your experience primarily, on how you did the weaver and what it took and all the things we had to do and how it helped us clean up some of the schema stuff. I think that's a great talk.
Also, any talk from Maintainer's Track about how how to handle AI overloads and the people submitting PRs and That kind of stuff will also go well.
I imagine. But yeah, Viva Rodea for maintenance track, that's cool, man. I would do it. I would be on that talk if you do it.
**Tyler Yahn (Splunk)** 48:17 the.
**Nimrod Avni** 48:17 So… Nikola Grcevski @ Grafana / OpenTelemetry 48:18 Yeah.
**Tyler Yahn (Splunk)** 48:19 The Weaver one could also work really well at Observability Day. I think that's another great one.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:23 talking.
**Tyler Yahn (Splunk)** 48:24 Like, just generalized, like… Nikola Grcevski @ Grafana / OpenTelemetry 48:27 are.
**Tyler Yahn (Splunk)** 48:27 patterns that extends well beyond like even OTEL systems and how to do it using Weaver. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:34 Do it.
**Nimrod Avni** 48:35 Okay, so, like, you have, you have normal KubeCon, you have Observability Day, and you have Maintainer Trial, like, that's, that's three, three.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:42 thanks.
**Nimrod Avni** 48:43 Excellent.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:44 Separate CFEs. I can post the links. I can post the links if you want to if you want to sort them. Yeah, I.
**Nimrod Avni** 48:49 I think I saw the normal KubeCon, but I don't remember Observability Day.
**Nikola Grcevski @ Grafana / OpenTelemetry** 48:54 Okay, I'll post in the channel all this three ones, and you just go submit on all. Like the more you submit, the more chances we get and talk about OB.
**Tyler Yahn (Splunk)** 49:03 And the observability day is pretty key, because you get a pass to both the main track KubeCon, plus the, like, observability day. So, like.
And you have a better chance of getting in, yeah. It's the most valuable, and it's, like, you have a better chance of getting in because you already work, like, your talk is likely to be around observability somehow, so, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:24 Although I have to say attendance is higher on the KubeCon track. So if you, yeah, because a lot of people don't pay this extra for the co-located events. So when they buy a ticket for KubeCon, they just buy them.
Main track.
Now they're co-located, so a lot, like maybe 30%, 40% of people will show up the second day, the day after they're co-located.
**Tyler Yahn (Splunk)** 49:47 Yeah, definitely true.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:48 Yeah, yeah.
**Tyler Yahn (Splunk)** 49:51 Yeah, I think there's a, we already got two more talks, right? The log conversion stuff and the Weaver stuff.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:56 Yeah.
**Tyler Yahn (Splunk)** 49:57 Yeah, great, great talks right there.
Yeah, cool.
Awesome. Anybody else have, ideas or, or, other projects they're working on?
**Nimrod Avni** 50:14 I just wanted to ask about the 1.0 release candidate. Like, what's the expected, like, how much, like, what's actually being, what is the release candidate? Like, what someone is testing it to make sure that it's whatever, and then we release a 1.0? What's the process?
**Tyler Yahn (Splunk)** 50:33 Yeah, it's out there, it's been released. The idea is that folks on this call should be validating it, or they have validated it, and that people can use it in the wilds. And if people submit bugs that are, like, blockers, or things that need to get fixed, then we can iterate. But yeah, this is kind of, like, the time You know, like, at weddings where they say, speak now or forever hold your peace? This is kind of it.
Yeah, so, like, this is just kind of one of those things where it's, like, your last chance to actually give some sort of, like.
feedback from the community. We could try posting something, like, on a blog post we've done in the past as well, but to be honest, it didn't… it was a lot of work for nothing. The people that were gonna evaluate it already had already evaluated, and we didn't get really any other feedback out of that. But, But yeah, so then the idea is just, like, we… like, because if you go, like.
014 to just 1.0, like… you have a chance of having people come to you and go, like, well, I never got the really… you never told me this is the last chance that, like, it's gonna go 1.0, so just doing a release candidate helps signal that we're on the path right now.
But yeah, from the maintainer's perspective, I am kind of asking, like, just go run OB. If you're already running it in your, like, production systems or in your back end, like, that's really all. And then maybe, like, run the release candidate in staging and just seeing if, like, you have any issues.
**Nikola Grcevski @ Grafana / OpenTelemetry** 51:56 Yeah.
No, no, we we they we picked up it in a beta release already when it came out. So we're with it's deployed today in Grafana Prod, and I think tomorrow it goes out to all our customers. So So testing goes well. So it's already in our staging.
Broadbest tomorrow.
or I think it's already pursued prod, we just need to see how it goes.
**Tyler Yahn (Splunk)** 52:22 You guys are also like bleeding edge. You'll already be testing at 1.0 or 1.1 soon. So yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 52:26 Yeah, no, yeah, we publish every week, like, after… if the tests go well, we go every week, so…
**Tyler Yahn (Splunk)** 52:33 Yeah.
**matt** 52:33 And how much time are we giving from the RC to the B1?
**Tyler Yahn (Splunk)** 52:38 Two weeks is what we documented. Yeah, and so.
the idea is, yeah, like, next… next Wednesday was kind of when I was, like, hoping to get a sign-off from all the maintainers to say, like, yeah, this looks good, and then… I guess Nikola won't be here, but, like, the Wednesday after that, then the release candidate should be out, and, like, we… or the 1.0 should be out, and we should be… Talking about blog posts, and talking about next steps before KubeCon, yeah.
**matt** 53:05 Okay.
**Giuseppe Ognibene (Coralogix)** 53:08 I have a question. Do you know if anyone is using OB on REL 8?
Like, some customer, or some of you?
**Tyler Yahn (Splunk)** 53:21 I don't.
Nikola, maybe.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:25 I think we have about eight customers on Bailoff, which is OB.
I don't know, what's the particular… I mean, the kernel they backport the fixes, so usually stuff just works.
**Giuseppe Ognibene (Coralogix)** 53:38 Okay, because for RPR, I was testing on RHEL… I mean, I see that we are testing on RHEL 8.9 in CI.
**Nikola Grcevski @ Grafana / OpenTelemetry** 53:47 within.
**Giuseppe Ognibene (Coralogix)** 53:47 In the doc we say from REL 8.
But the kernel version between 8 and 8.9 There are some changes in the EFN. Not all of them are backported. So I wanted to start to test on REL 8.
But before doing that, I just want to ask if anyone is… Before, like, downloading, 2GB of images.
**Nikola Grcevski @ Grafana / OpenTelemetry** 54:15 No, not in particular. We just want to tell them, like, oh, if it's 418 with all the backboards, you'll get it working. If not, it's… it is… supported.
I think it's very vague what we say. I agree. It's like 418 may work with some backboarded patches by RedHead.
Which ones are those?
**Giuseppe Ognibene (Coralogix)** 54:38 Okay.
Thank you.
**Tyler Yahn (Splunk)** 54:42 But yeah, Debbie, if you do find that, like, we need to clarify that Rel 8 to be 8 point… whatever?
Like, I'm happy, like, to consider that a bug, and like, let's just fix our support docs to be what it is, instead of…
**Giuseppe Ognibene (Coralogix)** 54:58 you.
**Tyler Yahn (Splunk)** 54:58 I'm trying to backport it even further.
**Roy Reshef (Kubex)** 55:01 Well, the main issues you're gonna run into are kernel versions and whatever, and… Maybe eBPF on that one?
**Tyler Yahn (Splunk)** 55:10 Yeah.
**Roy Reshef (Kubex)** 55:11 You may run into, I'm not saying you will, but.
**Tyler Yahn (Splunk)** 55:15 For the Red Hat stuff, like, as Nikola pointed out, like, Red Hat does a good job at, like, backporting, but it's just, like, what they've backported in eBPF and which version of 8. So if it's 8.9, like, it's not like that works, but whether it's 8.
You know, zero, like, that's another question.
But yeah, that sounds good.
I'm trying to look at our compatibility doc somewhere, but… We can look that up later.
Awesome. Well, okay, we could probably end the meeting here.
Thank you all for joining. We'll see y'all next week, or asynchronously. Until then.
Bye.
**Giuseppe Ognibene (Coralogix)** 55:55 mode.
**Roy Reshef (Kubex)** 55:55 Cheers.
**Nimrod Avni** 55:56 Bye.
**Gregor Zeitlinger** 55:58 Bye.
