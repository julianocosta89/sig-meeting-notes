SIG: K8s Semantic Convention SIG
Date: 2025-10-01
Duration: 30 minutes
Zoom Recording URL: https://zoom.us/rec/share/w7WRAQj-VofyAlpNSbEkEbV-pnnjr0dUSQh3phlVhHz1-Z4gTlxFoG0brOURXFne.XIFc-Bs5WIrxXvOT
============================================================

## Zoom Recording Transcript

**Jina** 00:55 Hey, Dimitri.
**Dmitrii Anoshin** 01:01 Of course.
That's a lot of Splunk people here. Nice.
**Hemant Seth** 01:15 Yes, me and Gaurav, we were invited for this session.
We'll just probably… Listen in, or answer any questions around the… some of the things we are asking in Hotel.
Like, services and labels and annotations, stuff like that.
**Jina** 01:33 I'm sorry, but is this on the agenda for the meeting? Have you already added that on the agenda for the meeting? Because, like, the way this meeting is driven is… You add those items on the doc and start the discussion there.
Or is that I'm starting the discussion?
**Hemant Seth** 01:50 Antoine, do you… did you add, or do you want me to add that in the doc?
**Antoine Toulme** 01:55 You can add the two docs, okay.
I just need to find where the dock is.
Boom.
Sorry.
**Hemant Seth** 02:10 Thanks.
**Antoine Toulme** 02:18 Hmm.
**Jina** 02:21 Okay, so I see, message in there, it seems like…
**Antoine Toulme** 02:30 Where am I?
**Jina** 02:31 Oh, yeah, so Chris and David are just in the Slack. There are no new topics, which is why I was like, if there are… if nothing is seen in the doc, people might not join.
**Antoine Toulme** 02:46 Hey, Kate.
Let's put people's name in there.
**Dmitrii Anoshin** 02:50 Looks like it got canceled, essentially, because there are no, topics.
Added to the agenda.
**Antoine Toulme** 03:06 Do you want to pick up the…
**Gaurav K** 03:07 eating, right?
**Antoine Toulme** 03:08 Stability board, take a look.
While we're at it.
How should we stop?
**Gaurav K** 03:16 This is a weekly meeting, right, Anto?
**Antoine Toulme** 03:20 This meeting's every two weeks, is that what you're asking?
Yep.
Okay.
So, Gina, Dimitri, can you tell us a little bit about that stability board? My understanding is that we're trying to aim to stabilize all the community semantic conventions by KubeCon. Is that still what the goal is?
**Dmitrii Anoshin** 03:47 That was the intention, at least.
**Antoine Toulme** 03:50 Okay.
And so, right now, the stability border is 1, 2, 3, 4, 5, 6, 7, 8, 9 issues.
We can show…
**Christos Markou** 03:59 Hey, folks.
we're discussing about skipping this one, but then I saw that, lots of.
**Antoine Toulme** 04:05 Management.
**Christos Markou** 04:06 So, yeah, I joined.
**Dmitrii Anoshin** 04:08 Hi, Christos.
**Antoine Toulme** 04:09 Yeah, sorry, we did not think this through, but, we're here, so… Hi.
**Christos Markou** 04:14 Sounds good.
**Dmitrii Anoshin** 04:16 The question, Christ, is, was there a goal for… to stabilize Kubernetes, conventions by .conf?
**Christos Markou** 04:25 By… sorted by what?
**Dmitrii Anoshin** 04:27 Buy.com… oh, sorry, by… By Kitcom?
**Christos Markou** 04:32 No, the goal was to, complete the first phase, which is this big meta, which suggested, like, introducing metrics in some metrics that are already existing in the collector.
stability will come, after this, but yeah, I think we're pretty close doing this.
**Dmitrii Anoshin** 04:53 And we're gonna announce that on Kipkon, right?
First place, yeah. Because we… for system semantic conventions, we decided to announce, essentially, I believe.
**Christos Markou** 05:05 Yeah, for… Yeah, Josh is aware, and trask as well, so probably they are going to include this in project updates or something like this.
**Dmitrii Anoshin** 05:17 Sounds great, thank you.
**Jina** 05:24 Hey, Crystal, so while I, have you here, I had a question about one of the PRs I was reviewing, the memory metrics one.
So… I understand the description for those, it's just, like.
you know, copy-paste from the kubelet stats, you know, API.
in upstream Kubernetes, right? And… I think it makes sense, but it also does not make sense when you're, like.
kind of a user, and don't really understand these different concepts. So for, like, you know, caters.node.
memory.available, or something like that. We talk about a limit, but, like.
if I did not know Kubernetes inside out, I wouldn't understand what a memory limit means in the context of a Kubernetes node.
**Christos Markou** 06:17 Yep.
**Jina** 06:18 So, yeah, I was just wondering, like, I can, you know, when I'm reviewing the… this thing, I can maybe suggest some edits to change the description to be more… layman friendly? Does that sound like.
A good way.
**Christos Markou** 06:33 Oh, yeah.
**Jina** 06:34 Ode.
Better, okay.
**Christos Markou** 06:37 Yeah, I… I… but that's… that's not really crucial, right? It's mostly an enhancement to… okay, okay, challenge me then.
**Jina** 06:44 Come back and, like, redo the descriptions after user feedback, if that's also…
**Christos Markou** 06:49 Okay, yeah. Yeah, that would be nice, yeah.
**Antoine Toulme** 06:53 Do you have the… Do you have the… the PR?
**Jina** 06:59 It's…
**Antoine Toulme** 07:03 Vision issues, I think.
**Jina** 07:06 2667.
**Antoine Toulme** 07:08 Is it on… Semantic conventions?
**Jina** 07:12 Yes.
**Antoine Toulme** 07:14 Oh, okay.
**Jina** 07:15 Sorry. Anyways, was there anything in specific, you know, Antoine, Heyman, you folks wanted to discuss in terms of semantic convention?
**Antoine Toulme** 07:24 Yeah, there's a couple stuff that's popping up, but I think this would be great to get directions, some of this, so… I know Hemant and Gaurav, they have… they have needs around having to shore up.
every other object in the Kubernetes cluster, right? Not just… we currently have pod deployment, we have replica, we render a lot of metrics and information. We would like to go further and discuss additional objects on Kubernetes services, a big one.
Anything related to, burst and volumes?
kind of trying to go deeper into the domain set and understand better some of the use cases that, I think Hemant in particular has articulated around, like, what people want to monitor, what they want to operate, and how they can make more sense of some situations so they can go to root cause much, much faster.
Yeah. Yep.
**Hemant Seth** 08:25 Yeah, maybe I can sort of, add to that. So, yeah, like Antoine said, what we are trying to do is we are trying to, expand our… visibility into our Kubernetes, into full-stack Kubernetes. So today, we support most common Kubernetes resources, like deployments, pods, containers, all those things, but we don't have visibility into things like Kubernetes services, or persisted volumes, and the whole network stack that includes the… you know, the access control layer, the rule, the ingress rules, the egress rules, all those things are completely missing today. So those are the areas that we want to sort of bring into our, into our product. And I can sort of answer any questions or provide some use cases why these are essentials, like Kubernetes, like, for example, like, services is a pretty… important aspect of Kubernetes. That's how these services talk to the pods, and we've seen, like, when we are doing root cause analysis, which is the big thing in Kubernetes.
A port may be healthy, may be running fine, but if a port mapping is misconfigured at the service level, we won't be able to root cause that problem, because we don't have any visibility into the services, or what is… how… so… so that's just one use case, but there are several similar use cases, and Gaurav, feel free to add anything from your end.
But, yeah, those are the areas that we wanted to sort of, and we have a whole list of things that we are requesting in, In Hotel.
**Gaurav K** 10:06 Right. So maybe one thing I'll add is, like, in terms of use case, we also want to capture how different Kubernetes objects are related.
And, basically create, something on the lines of a service map, for example.
Which essentially gives a quick overview of how different objects are related. And for that, what we want… we were hoping to initiate a discussion where how we can collect these objects as part of, hotel collection.
**Jina** 10:37 Okay.
I would suggest, like, the way to go about this discussion would be start making issues on semantic conventions with What you're looking for, what data you want.
You know, for the object.
And this would involve, like.
Suggesting, are you looking for metrics data? Are you looking for… Something with entities, or…
**Antoine Toulme** 11:05 Yeah, Janet, do you know of anything currently being filed? Like, is there an existing effort? Where… where are people at? Do you know?
Is this surprised for semantic ventures? Is it, like, out of scope right now?
**Jina** 11:21 I would, like, I don't know, I don't want to say it as out of scope, because, like, if you want to define, you know, all these new attributes, like semantic conventions is the right place.
But we can't have, like, a very high-level discussion like this. I guess we need to start drilling into details about what you're asking, and the best way to do about that is… start making issues. So if you want a Kubernetes service, sort of, like, fully fleshed entity, you know, to start showing up on some metrics or something, start an issue in semantic convention describing what… what would you like to see here, Dimitri?
**Dmitrii Anoshin** 12:01 Yeah, I agree with you. That's the right way. Going a bit more into the specific requirements, if it's just topology, if we only need to show, like, what particular objects are, how services are connected to pods and everything.
that those… that data would be entities. Like, there is no way to… we can… like, there is no reason to introduce, like, any, Like, synthetic metrics, so… Anything like that.
But if you want some measurable data for those additional entities, like, as you mentioned.
PVCs or, like, services or anything. If there is measurable data that needs to be showed in the UI, those can be different… additional metrics. And the metrics are easier to add, so you can just suggest in semantic conventions.
particular matrix that you want to add, and that's the way to go. But for topology, again, it should be entities.
**Hemant Seth** 13:03 So, clarification, so what about… Anton, I'm going back to that question that came up, like, a lot of the data that we are requesting is metadata, some may be metrics, but, some of it may not be metrics or metadata. Things like, ingress rules, like, Those are not metric data, so how do we… I mean, will that be also one of the requests here, or is that…
**Antoine Toulme** 13:30 If it's an object in Kubernetes, I would want us to make sure we understand how to represent that in OpenTeometry specifics and semantics. I think it might be a both an entity, which is a representation of the ingress rule in the cluster.
And I'm asking, actually, like, if anyone here, right, if you have an opinion. And at the same time, that ingress pool would have metrics that are associated to that entity that defines some specific behavior you're trying to track, right? So I think you end up with both, because they have different use cases.
Whereas the entity is going to be very stable over a period of time, and represent something in your cluster that you don't want to repeat on every time you emit the metric.
The metric itself is going to have cumulative counters, or these type of things, to help people understand the behavior of an ingress wall, such as number of bytes coming in, for example, right?
**Dmitrii Anoshin** 14:20 And so you end up with both, because you…
**Antoine Toulme** 14:23 You have those two needs at the same time.
for… Yeah, I… I don't know how, there is currently a set of entities in… for Kubernetes in Syntonic conventions, and service is not there, and ingress rules not there.
is it a… is it a big, like, net new pro… like, should we just open a PR and say, hey, by the way, we forgot one… one paragraph of YAML. Oops. Or do we want to have, like, a… an issue, a bit of a discussion? How was that come… coming together for those entities?
**Dmitrii Anoshin** 14:58 I believe for the entities right now, there is no, like… it's not standardized how we… provide new entity without any telemetry? Because right now, the problem is that entity is something that emits telemetry.
Eventually, we would potentially have something like an entity with no telemetry that can be defined in semantic conversion, but it's not ready yet, so in order to get a use case, we need to have something that emits the data, so we put metric for services, we need to start with that particular metric. Hey, we want to have metric for, like, rental service, for example, and that would be the metric.
**Antoine Toulme** 15:39 Okay.
**Dmitrii Anoshin** 15:39 you haven't mentioned about metadata, like, specific metadata. That potentially can be either resource attributes or entities with… an entity would allow you to provide more, like, richer data structures. For example, with entities, we can even… Like, send data, like, Config maps, for example, with, like, complex data structure, because with attributes, it's not going to be possible.
**Antoine Toulme** 16:12 I see.
**Dmitrii Anoshin** 16:13 Yeah, but that's, like, going forward. For now, you still have a solution. We already have Kubernetes Objects Receiver, which we can use, and Kubernetes Objects Receiver already available, and we can send all of the data, right? It's just, like, raw format of Kubernetes API.
And, it's like, it can be used right now as a replacement, as a, like, instead of entities, until entities are fully fleshed and ready.
**Christos Markou** 16:43 Usually for… for SemConv, it helps if there is a POC or something, trying to illustrate the idea. This will help us. Usually, that helps conventions approvers or maintainers to judge the solution and discuss around it.
So, probably implementing something with a collector or another implementation.
Would be, helpful at the same time.
**Antoine Toulme** 17:09 What's up?
**Jina** 17:10 Is it an issue for… this is just an example for, you know, somebody coming to us with a concept in Kubernetes, and they want to see… Something modeled around this concept.
**Antoine Toulme** 17:21 I see.
**Jina** 17:22 with, like, how would you go about creating that issue and putting those details? Because, like, the discussion we are having about Kubernetes service, it doesn't help us. We need to see it in written form in an issue. So just based on that example issue. In fact, that is a gateway, so your ingress kind of.
**Gaurav K** 17:38 Yeah, thank you, Gina. Thanks for sharing that. Actually, that is… that is very helpful.
**Hemant Seth** 17:42 So, Gina will look at the… and start looking at defining issues, but we have a doc that we have shared with Antoine and the team. I'm assuming, Antoine, I'm assuming you'll… the doc has the requirements in terms of what attributes we want and those things. Is there additional requirements you guys are looking for? I'm trying to understand what level of requirements do you need from us?
**Antoine Toulme** 18:07 I think… I think usually it's a job to be done, who is doing the job, what are they looking for, and maybe a motivation. So, if you look at the issue that Gina was… was pushing here, that… the interesting thing is.
People are going to ask you why.
Right, so you're going to say, I want all this information, and the question is going to be, well.
Why is that? How is this used? What is the leverage of this?
And there's some considerations about being careful about what you expose, and, yeah. So… Yeah, usually it's going to be more of a, I want to understand what a service is doing as part of my cluster architecture, because I want to be able to list everything that is labeled with a particular key-value pair, so my SRE team can see the slice of all the cluster that is being represented. Okay, that's your entity for service. That is what it's going to look like in a model, and we're going to make sure it has all the annotations and all the labels exposed in some way.
So that people can search for this type of data, and they can filter and see the facets of their cluster, so they can identify what resources are attached to what cost center, for example.
Right? That's one use case. Another use case could be, I want to understand what the service health looks like in terms of availability, so I want to understand what pods are matching the selector at a given point in time. So now I have an entity where I'm going to have a service, I'm going to be able to match to existing pods.
So I can understand if we're actually serving any traffic from that service to existing pods, or if it's being dropped on the floor.
Hopefully that helps. Like, this needs to be… this level makes it clear for anyone coming after us. I'm mostly thinking about end users, right? People who are maybe a year from now, like, looking at this and trying to use this service, this entity, this metric. They need to be able to Match that to their own use case, and unfortunately, otherwise, it feels like they're… they might not be able to catch up.
**Hemant Seth** 20:14 Got it. Thanks. Yep.
**Antoine Toulme** 20:16 Did you do a good job, folks? Is that… is that right?
**Dmitrii Anoshin** 20:20 Yeah, but I believe the original equation from Gaurav was that, like, we have a document, what else do you want from us? But the document, I believe, is internal, and we… we need, like, public discussion on OpenTelemetry's side, not on our side, and then doc. And that should be… that doc should be translated in the public GitHub issues, so we can invite people to discuss and, Like, suggest some ideas or accept whatever we propose.
**Gaurav K** 20:51 Thank you, Dimitri.
Thank you, Anton. Maybe… Not to get ahead of myself, but I was trying to understand this process. So, we file an issue, the issue gets discussed by the community, we get inputs, and then, is that usually followed by, semantic conventions, PR, and finally by an implementation?
Christos mentioned, a POC. Is that something… Christos, are you suggesting that as part of, semantic conventions PR, or something that is part of issue, so that we can explain, the issue better? Was that your suggestion?
**Christos Markou** 21:30 Usually, when people file issues or PRs in semantic conventions, semantic conventions, maintainers, approvers.
ask for, an example instrumentation that is already using or is, going to use these, semantic conventions. So… yeah, in your case, assume there is nothing in the collector, for example, right now, but probably if you have a draft VR in the collector showcasing how the telemetry will look like and all this stuff, this will help the discussions.
**Gaurav K** 22:04 Okay, thank you.
**Christos Markou** 22:06 Because it's hard to do conversations in just semantic conventions level without, knowing in a pragmatic way how the telemetry will look like.
**Gaurav K** 22:15 Okay, yeah, okay, thank you, thank you for explaining that. Okay, cool.
**Antoine Toulme** 22:19 Gaurav would say that the order in which you go about this, like, you can open the semantic convention issue at the same time that you have the PR against 70 conventions, at the same time that you have the PR on contrib.
The way it will land is usually in some sort of a well-understood way, so that you land the PR in Contrib once the semantic conventions are settled, but you can make the change in the Semantic Convention's repository.
and showcase that as part of your issue to make your point. So it's becoming more biting, it's more concrete in the same way for the PLC. So you're not blocked on just the issue. You don't have to have some sort of a handoff in the issue that says, oh, we're good, now go implement. No, you…
**Gaurav K** 23:00 Yeah, do it in town.
**Antoine Toulme** 23:00 They start the conversation. Usually, the earlier the conversation starts, the better, because it takes time for people to catch up to your reasoning. The main reason of putting things into an issue is you also put a stake in the ground and say, hey, we're thinking about this. That means that everybody else who's also thinking about this.
We'll align to your vision, will not create their own issue for the same use case, and it creates an aggregation of people and trust.
And that creates a… you know, for maintainers of semantic conventions, that's super important, because not just one person with that need. It's like, oh, that other person's also saying, I need this. So, I think issues are more of a social conveyor of the importance of an issue.
If that makes sense.
**Hemant Seth** 23:45 And…
**Gaurav K** 23:46 That's what it does. Thank you, Atun.
**Hemant Seth** 23:47 One more question from my side. So, each issue is a specific use case, or each case… like, will there be one issue for the entire services, and then we put all the requirements in that? It'll be one issue, or within services, we may have, like, 3 or 4 different use cases, and each use case will be a separate issue.
**Antoine Toulme** 24:10 I don't know, each project's different there. What do you prefer, folks?
**Dmitrii Anoshin** 24:15 I would say if use cases are completely independent, that… they can be separate issues, but if they are kind of related to each other, it's probably… it makes sense to have one issue per series, let's say.
**Hemant Seth** 24:29 Love it.
**Dmitrii Anoshin** 24:32 there are no strict requirements around that. Of course, we shouldn't have, like, just one issue for everything, for everything not related to each other, but it's… yeah.
**Hemant Seth** 24:45 Got it.
**Antoine Toulme** 24:51 Okay.
Crystal, sorry, anything you'd like to bring up? Sorry.
Don't mean to take over the meeting.
**Christos Markou** 25:02 No, no, no. I guess we are good for the day. In any… yeah, in any way, we were, thinking of skipping this one, but since you had topics… Yeah, I think we're discussing. Yeah.
**Antoine Toulme** 25:15 Yes.
And, pRs, services… Ingress came up, ingress rules… And then we discussed entities and metrics.
Adhop to… Work on one or the other.
Or, go ahead.
**Hemant Seth** 25:47 And what's the typical timeline to get this approved? Like, we'll… obviously, we'll put the requirements, we'll put the… create the issues, put the requirements, you guys will discuss it, and then finally, I'm assuming there'll be some approval.
So, what does that timeline look like, typically?
**Christos Markou** 26:08 It depends. It really depends.
**Antoine Toulme** 26:14 Come on, be honest.
**Dmitrii Anoshin** 26:17 Given that there is a big effort to, like, for stabilization of existing things.
This might be not taken, like, higher priority, like… comparing to stabilizing an existing thing, but… I don't know, like, feel free to always Pink people, and like, and comment on the issue. If, like, if there is more… activity on the issue, it gets more traction, typically. So if, like, no one replies, additional comment on the issue will pop it up on people's, notifications list, etc, so…
**Hemant Seth** 26:58 Okay.
**Dmitrii Anoshin** 26:59 Works.
**Christos Markou** 27:00 It also has to do if it is, like, super KH-specific, or if it's going to touch, generic, more generic cement conventions, like, concepts in that case.
Semant conventions, like, let's say, maintainers or approvers would need to jump in and provide direction This complicates things, usually.
**Hemant Seth** 27:25 Got it.
**Dmitrii Anoshin** 27:28 For something straightforward, for example, we know that there is this metric for additional service, it provides some value.
and it's pretty clear what's the purpose of the metric and everything, it can be quickly merged in. If something that is pretty vague and clear, what's the purpose, how to shape it in the data, etc, it will take more time for all the discussions and figuring out what's the best.
Was the best, like, model for that type of data, etc.
**Antoine Toulme** 27:58 I want to understand one thing, is that you want to declare Kubernetes semantic conventions stable, but as… is surmised in the discussion we just had. There's a number of concepts that we can add.
I wonder if we can have this happen in parallel, meaning that we're currently working on a set of well-known, well-understood semantic interventions for Kubernetes that are going to be stable in some short amount of time. At the same time, can we continue to work on more extended semantic conventions for Kubernetes for a later release.
So that we can also work in parallel, and not jeopardize the work that has been done on stabilization.
**Dmitrii Anoshin** 28:45 I think that's been the case for other 6, and… Okay. I don't see any problem, but Christos, you've been involved more than I am, so maybe I would like to hear your opinion on this.
**Christos Markou** 28:58 I think it's doable, yes. In any case, we're going to focus to start, like, targeting specific subscripts for… subgroups for stabilization.
The thing is, all about, the tricky part is the staffing that we have, because we are only a few people that we're going to work on reviewing stabilization PRs.
then, yeah, reviewing additional PRs would require additional time, so that's the only burden that I could see there.
**Antoine Toulme** 29:32 Can approve everything. It's easy.
**Christos Markou** 29:36 Yeah, let AI approve, and… The worst thing. It doesn't work for us, yeah.
**Antoine Toulme** 29:43 Okay, okay, understood. Alright, so it's a matter of putting some work into it, understanding the scope, making sure we're not over-subscribing ourselves, and we don't have to tie everything into one big deadline, is that what I'm trying to go for, right?
**Christos Markou** 30:00 Yeah, yeah, you can start working on this, and feel free to also ping us, and yeah, we can iterate on this.
**Antoine Toulme** 30:10 Okay, cool. Thanks Gonna run.
**Dmitrii Anoshin** 30:14 Thank you very much. See you. Bye-bye. Thanks. Bye.
