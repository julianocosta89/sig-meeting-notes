SIG: Entities SIG
Date: 2026-02-09
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/F-kn7njRnifMQG0TEXPaAqZ5m9R-8aue7745ZLYwsw54BJ4jR8DzhtivV17Fx-JC.WcjB4BB0R4IBmgyh
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:02 is being recorded.
**Dmitrii Anoshin** 00:59 Hi, everyone.
**Arthur Silva Sens** 01:08 Loaf.
**Josh Suereth** 01:11 Sorry, we had a long semantic convention one, so I'm still getting… Things sorted. I forgot to put agenda ahead of time.
Alright, I'm going to start with our project board, and kind of what we're working towards.
And open PRs… If that's alright… we, Unless someone else has something higher urgency. One of the things that we… we have is, we are currently listed as at risk for a November of last year delivery. I would… I would argue that we haven't finished anything.
by November, that was targeted for last week. I think our goal was to have a default specification that we could implement some of the SDK work on.
And I want to update this date or the milestone we're targeting. One of the two. So that's, like, the big thing I want to talk about. So, to start with, I thought it'd be useful to go through some of our in-progress stuff.
And go through what Phase 1 is, and let's update our definition of done, and then update our target date for the GC tracking. Sound good?
**Dmitrii Anoshin** 02:42 Sounds good.
**Josh Suereth** 02:43 Okay.
Cool.
So… First off, we have, Dimitri working on support for, entity references in the protomessage. I think this is in the collector.
This appears to be making lots of good progress. Anything you want to call out?
**Dmitrii Anoshin** 03:05 Yeah, I… I didn't have, actually, My adult… yeah.
Haven't made a lot of progress on the collector, but I've been focusing a lot on the specification PR for the… For the entity events, because that work is kind of important for me to get, like… I don't have specific blockers on the collector, I still can continue, but, like, getting that one merged is, like, will give me a much cleaner path forward, so I would like to maybe… maybe we can talk about that one?
**Josh Suereth** 03:38 So, we need decisions on that one before we can…
**Dmitrii Anoshin** 03:42 No, not a decision, it's more like… just like my time investment. I spent more time towards specification, because it's, like, more foundational, it's still needed for the collector anyway, rather than on the collector, and I spent much less time working on the collector last week, if that makes sense.
**Josh Suereth** 04:01 Yeah, I guess what I'm… what I want to know is, one of the reasons this is listed here.
**Dmitrii Anoshin** 04:06 Yeah.
**Josh Suereth** 04:07 and we can change the scope of this, is if we have SDKs start to produce entity.
**Dmitrii Anoshin** 04:13 Yep.
**Josh Suereth** 04:14 Are… is the collector gonna be able to handle it?
Like, or are we gonna be broken?
**Dmitrii Anoshin** 04:19 It will handle it, in a way that it's kind of more no-op at this point. It will not… it will pass it through, it will not… you will not be able to do anything with that, but it will not break anything. It will… and it will pass it through, through the collector.
**Josh Suereth** 04:36 Alright, so I think that's probably good enough. Like, what I'd like to do… you have support here, maybe we should split this into two. For res… for Phase 1, there is, like, what do we need to have SDKs provide entity, right? And do the SDK part of the spec. For phase, with resource in it. For phase two.
I think that's where the collector work gets way more interesting, right? And the stuff you're working on.
**Dmitrii Anoshin** 05:03 It is, yes, it is way more interesting, and also, like, for the resource part, I still, want to introduce much more features, like, ability to, actually, like, operate on entities in some meaningful way, so it's ongoing, like, I'm working on that. It's just I haven't spent much time on that, because I would like to…
**Josh Suereth** 05:28 do the spec first, that's fine.
I think it might make sense… I'm thinking with my project manager hat, it might make sense for us to de-scope this, then, the in-progress work. So this bug here is probably too broad, and we probably just want, like, a… thing that makes… like, my thinking is, for in progress and phase one, I'm still trying to get the point where SDKs are producing… or have a way to interact with entities, and so I'd like to get to that state.
**Dmitrii Anoshin** 05:58 Sure.
**Josh Suereth** 05:59 Okay, if that's the wrong first phase, we can… we can talk about that. Let's go through the rest of these quick, and then we can… we can talk about your, your current proposal.
I just want to go through kind of current status. Alright. Entity prototype for SDK specification, this is one of the in-progress things. We have a prototype for Java here.
I don't know why it opened a different… thing. Anyway, we have a prototype for Java. This is just waiting on specification work, so that we can take the prototype and, actually contribute it to the SDK, so the spec PRs are just sort of languishing. And we need to… we need to kind of get those through, or figure out what's going on.
Define entity merge algorithm from the OTEP, this is… This… this… I don't know what we need to finish here.
I think everything's addressed.
But if anyone has any comments or concerns, like, it has no approvals, so that means that either folks haven't reviewed it, or I didn't finish addressing all the comments. So… I believe I've addressed all the comments?
But if not, please take a look and let me know. This is blocking further SDK work for the spec.
**Dmitrii Anoshin** 07:16 Great.
Yeah, I'll take a look. Okay. Thank you.
**Josh Suereth** 07:21 Alright, so then we have, in progress… That was… resource entity merge logic prevents fine-grade detectors. This is having a, a prototype for Go.
I think… David Ashpel actually had a prototype of one of our OTEPS, so I'm going to take a look at what he did there. This is the ability for us to have resource detectors that detect one attribute at a time, and somehow reconstitute entities. That's how Go works today. Yeah, I think that's still something that needs to get worked on.
But that's… We can do that when we start working on Go.
Sdk startup specification.
I talked to Daniel about this. He's gonna be gone for, like, a week or two now, I believe? And then, basically, all of February, he's kind of gone.
Looks for a different place to speak up.
Yeah, interesting, this got put on declarative configuration stability.
I don't remember when that happened.
Tyler put it on there.
Huh.
Anyway, the idea here is we don't really have a SDK startup, definition?
Which means, when do you do resource detection? When you do entity detection, the SDK is still somewhat awkward. This… the reason this is signed to Daniel is because the resources that need to get instantiated asynchronously in JavaScript kind of pose a problem. There's no way to block. We need something in the spec to kind of… make allowances for that. Daniel actually has a, prototype in JavaScript for entities, and so I think that's making some progress, we can work on that from there.
that's related to this strategy for asynchronous resources. So those two, I synced with Daniel on. I think they… they made good progress, but we probably won't do anything until the end of March on those.
In terms of remaining to-dos.
decide how entities are supported by schema files. We are actually changing the definition of schema file.
So, I think I can actually mark this as done. The TLDR… There's a… there's an OTEP where schema files are going to disappear, as they exist today.
So today's schema files are, from version to version, it says A change to B.
Right?
In the future, schema files are gonna be, here's the definition of everything.
Here are all the entities that I could produce from my schema.
for this Euro.
And inside of that, there will be, this old schema is deprecated, we renamed this attribute to be this new thing. So all the renames and stuff that are part of schema, all the renames of NC names, all the renames of metrics, all the renames of attributes, will actually be in the definition schema to begin with.
And we already have that capability for entities in open… in, semantic conventions in Weaver.
So we actually already have this diff cap capability, we just didn't have it in schema files. So, I think what I'm going to do for this is say… I'm gonna edit it… When the new OTAPS for schema files.
Weaver Support.
for entities.
There is no more here.
You know, the works of… Integrated.
Zip code, and… It's not public opinion.
Alright, so I'm gonna do that, and if folks are comfortable, I'd like to mark that as closed. Anyone feel like we're not done there?
Okay.
Alright, can collector processors differentiate between remote and local?
Question for you, Dimitri. Does this… do we need to talk more about the second signal before we talk about this? Is this one that's kind of blocked on the spec?
**Dmitrii Anoshin** 11:42 Not this one in particular, more, like, how we… it's blocking more work on the receiver, which will eventually produce, like, all telemetry signals, including, entity events. And there we have, like.
some… declarative language was being produced, so I need to figure out declarative language in order to figure out declarative language in a good way, I need to find out… know how we're gonna emit entity events going forward. This one is more for processors.
And, like, we have… I need to think about it. I actually, currently, we are trying to… mark one of the processors stable, like a Kubernetes processor, and that is clearly a remote enrichment processor. So… And, like, the configuration interface of that processor is kind of super confusing, and probably we need to adopt some entities concepts in that one, even before.
So, yeah, that's, like, it's gonna be… This particular problem is probably getting more, like.
like, importance from my side as well, so I'm gonna think about it, and maybe reply on here as well.
**Josh Suereth** 13:10 Yeah, to me, this is one of the big wins of… Phase 1.
**Dmitrii Anoshin** 13:16 Yeah.
Like…
**Josh Suereth** 13:18 If we can get this solved in Phase 1, I think we've really succeeded at eliminating some user friction.
That said, if you need more definition on the signal to get this done, I'm fine with that, because, like, my focus is, I want to have a clear phase one, a clear phase two.
**Dmitrii Anoshin** 13:36 This, to me, is…
**Josh Suereth** 13:40 hands down, the biggest win in Phase 1.
Second thing will be, like, cleaning up resource detectors so that we have, We have a clear set of how they work together, and the ecosystem can kind of evolve.
Rapidly, without blowing each other away. Right now, we still have some issues where some resource detectors do not play nicely together.
In practice, so… but people don't turn them on together in practice, so no one really notices until you do, and then it's… oh, hell breaks loose. Anyway…
**Dmitrii Anoshin** 14:13 So, like, if I'm just gonna answer this question right away, there is currently no like, differentiation. It's like, it's implicit.
differentiation, so you need to think about, hey, this processor is taking data from Kubernetes API, this processor is, like, based on the local enrichment. But we… I do think we need to introduce, even if it doesn't affect the logic of the components, we at least need some way to, like, explicitly differentiate that.
I guess.
**Josh Suereth** 14:47 Yeah, I actually… so here's my intuition. I think we're going to have to make one more protocol change.
In addition to what we've already done.
**Dmitrii Anoshin** 14:58 Or what was that one? What was that about? What did you change?
**Josh Suereth** 15:02 This is just purely speculation intuition. The more we dive into things, and the more we look at identity, you know how right now in resource, every single entity participates in the identity of the thing, right?
And there's no relationships.
**Dmitrii Anoshin** 15:18 Yeah.
Yeah, that's…
**Josh Suereth** 15:20 In fact, we might need to put The ability to define whether or not an entity is a or is a relationship of some fashion, right? Like, this is the owner of the previous, that sort of thing.
**Dmitrii Anoshin** 15:34 I've been thinking that it's potentially still can be something uploaded to the entity events completely, so I don't… I haven't found, like, a reason to put that information in the resource, but I've been stumbling… on situations when… where I definitely need to decide some kind of an owner entity between the two, because currently they are all, like, all the same…
**Josh Suereth** 16:01 All the owner, yeah.
**Dmitrii Anoshin** 16:03 owners, right? And it's not the case, especially when we define, like, metadata YAML for the receivers, when we're defining VIVER, it's only one entity being responsible for a particular telemetry type, and others are, like, secondary, which have some kind of relationship to that entity, whether it's parent or, like, Isaiah or something.
So, at least that one, like, is owner, I do think we need to add. But others, potentially, as well.
**Josh Suereth** 16:31 Yeah, this is… that's my intuition, which is why, like.
I think answering this question will help us drive the design we need for that overall issue. So, like, I want to make progress on your PR and the entity model, but primarily the reason I want to is because I think we need to better understand relationships.
**Dmitrii Anoshin** 16:53 Here.
**Josh Suereth** 16:54 because, as soon as we start… as soon as the SDK starts producing entities, and we can't understand enough of the relationships in the collector for them.
we're gonna run into problems, right? And so I… I really want to… I want to make progress on what you're working on, but specifically for this use case, initially. That makes sense.
**Dmitrii Anoshin** 17:15 But even if I have relationships in the resource, like, I… my concern that I raised will not be addressed anyway. Owner won't… will not be clear.
Yeah. In that case, so we probably need to address both, or something.
**Josh Suereth** 17:33 Well, once we know what the relationships look like better, we can figure out the minimum amount of information we put in resource. Okay. I think we agree resource should be very minimal.
**Dmitrii Anoshin** 17:42 Yes, yes.
**Josh Suereth** 17:43 Yeah, okay.
Cool. This one, I think, is just around how we roll out Phase 1, that we can't really do until we're ready.
To communicate the breaking change in resource, that one's fine.
Add entity supports a metadata Guillaml schema. I think that's also… we can do that. I don't… I'm less worried about that task specifically. Generate entity configuration interface for metric scrapers. Okay. What I wanted to focus on, though, was this resource entity mapping phase one, is what does done mean?
And I'll give you my straw man.
Done is where, openTelemetry SDK… we have a specification and implementations in 3 OpenTelemetry SDKs.
Those three allow you to define resource detectors that actually discover entities.
The SDK has an entity merge algorithm that will merge things into resource appropriately, and it's filling out the entity section of OTLP.
when I send that to the collector, the important pieces of the collector, meaning, like, the processors and the resource detection processor, the Cates processor, are able to use entities to, like, layer on information.
**Dmitrii Anoshin** 18:57 Okay.
**Josh Suereth** 18:58 and answer that question. And I think, to me, that is the phase one look.
is, like, we get that working. And then phase two is where we start to do… figure out which, you know, Which relationships and processors and stuff we expose.
**Dmitrii Anoshin** 19:13 Okay. Okay, yeah, that makes sense. I'll… I'll focus more on the reprocessors in that case. I mean… Well…
**Josh Suereth** 19:21 So, to the extent that we… I think you… you started scratching an itch of looking at the event model for how we're going to expose relationships. And I think the event model is important for us to get right.
But the relationship model is a thing I'm more worried about. Does that make sense? First.
**Dmitrii Anoshin** 19:41 Yeah, but it also depends whether we… when… whether we want to put that relationship model in the resource or not. If we don't want, we still… we… I mean… We can keep it… We can model it and agree on the long-term approach, and that would not block us as well. Just like agreement, I guess. That will unblock that work, right?
**Josh Suereth** 20:04 We need just enough information to know that, yeah. So, like we were just talking about, I think this whole… the differentiating local versus remote entities as they come in, and being able to annotate them successfully without breakage. If that needs relationship or owner.
then we add it. If that doesn't, we don't, right? But, like, let's sort that out. The things… the things that I think will matter are, we talk about identity being contextual, so, like, you know, a Kubernetes pod is unique within the cluster, but I might have more than one cluster.
**Dmitrii Anoshin** 20:43 Right? Yeah. So, if I have an entity signal.
**Josh Suereth** 20:46 and I'm sending state information, I want to be consistent about how that identity expands, and what that looks like. So, do I expect to have someone reporting the state of all the Kubernetes things together in a cohesive fashion?
Right? And if so, then when I have two clusters reporting that data, how do I differentiate between the two? Can I make sure the entity signal that's exposing the state relationships is using the same technique as the resource if it has to say, I'm part of a cluster.
**Dmitrii Anoshin** 21:15 Yeah, that's the idea.
**Josh Suereth** 21:18 And that's why I want to get into your PR, because I think, like, the decisions we're making in your PR are super critical.
But there's so many of them, so I want to kind of focus a little bit on, let's get real firm resolution for things that are part of Phase 1, and things that are part of Phase 2. If it takes us longer to resolve, I'm not worried. But I want to make sure, even if your PR isn't approved, that we agree on those important pieces for Phase 1. Make sense?
**Dmitrii Anoshin** 21:44 Sounds good, yeah.
**Josh Suereth** 21:45 Cool. Alright, with that, do you want to present? Because I think the next thing I want to talk about was your PR.
Do you want to present your PR things?
**Dmitrii Anoshin** 21:54 Sure.
**Josh Suereth** 21:59 Good.
**Dmitrii Anoshin** 22:04 So, Your… we discussed your concerns about, like, load, and like… That you mentioned here, it's gonna be pretty un… Hard to manage all of this, like… a lot of data, and you had some discussion with Kigran, but I addressed that in a few ways. So, let me actually pull the… just the diff in that case. The div gonna be here. So, what I've done… is… I addressed the PR in, like, several ways. First of all, I… Clearly separated state changes and periodic reports, so they… we can disting… make a clear distinction between them.
And, Potentially, we can make it optional configuration on the… on the, like, receiving, like, let's say, emitting side. Whether you want only periodic reports, or you potentially want state changes only, but by default, they are both emitted as before.
And differentiation between that is just, entity updated optional field. It's kind of… in order to differentiate between whether it's change or heartbeat, it's gonna be, like, the… it's gonna be treated as a boolean flag, so if updated is present, it means that it's, like, actual update. If it's not, it means that it's heartbeat.
Then, another one is I, like, as I understood your problem, I think you wanted this kind of aggregated reporting. Essentially, what it does.
It only reports events on, like, particular like, periodic basis. It doesn't report anything when it's changed right away. And, re… like, events that are… happened within that window, for example, like, pod is shortening, right? Pod is keep… keep changing its state from running to failed, running to failed, and at the end of the window, we only report the latest state.
That's kind of optional. Optional capability I suggested to… that, like, SDKs or collector can have.
And it comes to the same… the same additional field. If entity… if it's, like, aggregated, or if it's an update event, it will be the time when the event… when event was produced, the latest event, latest change.
Would indicate… would be indicated in this field.
So it potentially can differ for aggregated reports to… it can be different from the, log time stamp, essentially.
Because log timestamp would be… will always be time when event is emitted.
And the last thing, I, like, I heard your concern about the… relationships, but I still, like, I tried to separate them, but at the same time, I found out that it's gonna… it's a lot of repetitive stuff, like, you would… we always need to… We always need to… specify a source and target, and it's, like, separate event per, separate log record per event, and I wasn't sure that it's actually gonna help. So, instead of, like, separating relationships from the entity-state event.
I… like… I put it… I made it very clear, the relationship statement guidelines. I put some relationships placement guidelines, and made it very clear.
Where do you put relationships? Give me a second… Relationship placement, here it is.
So… For example, if you… if there is a relationship between pod to replica set, we would rather put relationship on the pod, because pod is churning the most, right? So we don't want…
**Josh Suereth** 26:42 So, as a question for you, though, isn't… the pod doesn't know about its replica set, the replica set knows about the pod.
**Dmitrii Anoshin** 26:48 No, no, no, from, like, for example, in the collector, it doesn't matter. In the collector, we take everything from the Kubernetes API. So I don't think… Actually… Actually, no. Like, even if you are inside the pod, you have ownership… ownership, object.
**Josh Suereth** 27:09 You, you know who you're… who owns your…
**Dmitrii Anoshin** 27:11 Yeah, it's actually… it's likely you have, replica state inside the port rather than, here.
**Josh Suereth** 27:19 Not inside a replica set. Oh, Replicaset has the… the labels or something, right? I forget how that works.
**Dmitrii Anoshin** 27:25 Yeah, but anyway, for companies, that's not the problem.
**Josh Suereth** 27:27 Nevermind.
**Dmitrii Anoshin** 27:28 For Kubernetes, in the collector, for example, we emit however we want.
It's just like, here I wanted to put guidelines, like, that you put relationship to the most churning entity of the, of the, like, topology. So, because spot is churning the most, this one should have relationship to the replica set, not the otherwise. Because if it was otherwise.
any change to any port would require separate event for the replica set. But now, given that we didn't meet this requirement, go ahead.
**Josh Suereth** 28:04 Yeah, let me, let me ask a bigger question, right?
Deletion might never happen. Deletion event.
**Dmitrii Anoshin** 28:11 Deletion might never happen, yes?
**Josh Suereth** 28:14 But, like, the… so again, it gets lost. I don't get an event that says it's deleted.
How do I know that a pod was gone?
**Dmitrii Anoshin** 28:22 Yeah, and that's why we have the heartbeat events. On the backend, if you don't see heartbeat event from a particular port, you just… you remove it along with all of the entities.
**Josh Suereth** 28:33 With all of its relationships, okay.
**Dmitrii Anoshin** 28:34 lightweight detail, yeah.
**Josh Suereth** 28:36 Okay, so basically the idea here is the relationship always comes from that part, and then the pod itself… If it dies, all of its relationships are implicitly deleted.
**Dmitrii Anoshin** 28:48 Right, exactly.
**Josh Suereth** 28:49 Okay, okay. Just for context, the way I envision this whole system.
We are doing a giant, distributed cache.
Where there's, the state of the world somewhere.
And then there's the state of the world that we're trying to report to, and your system is basically a giant cache coherency problem.
**Dmitrii Anoshin** 29:11 Yep.
**Josh Suereth** 29:12 And so I'm just throwing cash coherency issues at you to see how they line up, especially with relationships.
I think that My, my… I need to think about this, because my question would be, if the thing that churns still has a crap ton of relationships, you're still sending a lot of data. Like, can I send just the relationships of an entity without sending, the configuration state of it?
**Dmitrii Anoshin** 29:43 I don't have it here, in this spec. I think if we're gonna… that's the whole, like.
Issue. When we gonna… Go into this situation when we're gonna split parts of the…
**Josh Suereth** 30:01 Yeah.
**Dmitrii Anoshin** 30:01 state.
That's when things get much more complicated.
**Josh Suereth** 30:06 Right, because… so, from a volume standpoint, if I'm sending the entirety of, what's the etcd over the network.
every minute. That's… that's a lot of data.
**Dmitrii Anoshin** 30:20 But why… like, that's how you… first of all, every minute is probably too aggressive. I think we, for heartbeat, we should have something like… so the interval of heartbeat would… specify the TTL on the backend, essentially. So let's say if you send every minute, you would expect everything to be churned in 2 minutes on the backend, or something like that. That may be not, like, very practical.
So I think we can make… we can send every 15 minutes, or something like that, and on the back end, like, let's say 30 minutes would be the TTL for the data.
Okay. That seems…
**Josh Suereth** 30:59 The other, the other question would be the, If we go back to the… the update event, right? In my update event, if I said update equals true, do I have to fill out every… do I fill out every field?
Or do I just give you the fields that changed?
**Dmitrii Anoshin** 31:13 Exactly, that's the same question. If we're gonna split the events, that's gonna be complicated, we're going to introduce patch events now, and the handling patch is gonna be… pretty complicated, and like… I mean, I think you just haven't figured it before.
**Josh Suereth** 31:32 The thing is, though, I'm not aware of a system that doesn't get there. And so the question is, if we build a system that doesn't have that, are we just screwing ourselves over where we're gonna have to build it later?
**Dmitrii Anoshin** 31:45 What do you mean?
**Josh Suereth** 31:46 So, so, like, I, I, Tigrin was arguing this, of like, oh, it's much simpler if we don't allow patches. Agreed.
But… Can you build a system that does what we're building, and not have the ability to do patch diffs, and limit your network bandwidth in that fashion? Like, is it actually going to scale?
**Dmitrii Anoshin** 32:07 Yeah, bro.
**Josh Suereth** 32:08 The reason I don't think so is because our internal system that does this.
**Dmitrii Anoshin** 32:12 At GCP.
**Josh Suereth** 32:15 can't, like, it has the ability to patch. It has snapshots, and it has patches, right? And so, I keep looking at this and saying, cool, I have not seen a successful system that doesn't get away without having patching capability in this kind of a sync. And… Can we… can… Can we keep it simple?
with a bunch of, like, simple things that maybe aren't that optimal that we can try out, and then prototype with Kubernetes. Because I think Kubernetes is a really great… I mean, they have all the APIs we need to build out what we want, with, like, the watch… watching objects and reporting relationships, great.
**Dmitrii Anoshin** 32:52 Kubernetes doesn't provide patches by itself, so Kubernetes API, if you get… if you watch for API, you would get new objects altogether.
**Josh Suereth** 33:04 You get the whole object.
**Dmitrii Anoshin** 33:05 Oh, we would need to actually keep the cache on the collector, and, like, recreate the patch, figure it out, and send for the event.
**Josh Suereth** 33:16 I see. Gotcha.
So Kubernetes, Kubernetes is actually sending everything, but they're also keeping their objects really small, because that could be the last bit here, is basically We would recommend tiny things.
That we sink. Like, I like what you're doing with the, with the recommendations around how to do relationships to keep it small, and to promote the thing with the most churn. I just want to make sure that we're not, like, dumping a giant amount of state all the frickin' time.
In this ecosystem, right?
**Dmitrii Anoshin** 33:51 Yeah, and for example, you don't have to… like, that's why… what… how I try to address that concern with aggregated reporting. In aggregated reporting, you can disable heartbeats.
disable heartbeats, and enable aggregated reporting. In that case, you will only be receiving state changes, particular entities that got changed during that window.
**Josh Suereth** 34:18 Yeah.
**Dmitrii Anoshin** 34:18 Not the whole state.
If that makes sense.
**Josh Suereth** 34:23 That's where you batch… you batch a few changes for up to n minutes, and then report them all as one, yeah.
**Dmitrii Anoshin** 34:28 Right, right, right.
**Josh Suereth** 34:29 Okay.
**Dmitrii Anoshin** 34:30 But in that case, keeping track of entities that have been removed, that's gonna be complicated, and… We do have delete events, but they potentially can be lost.
**Josh Suereth** 34:45 Yeah, this is where I was kind of thinking around, so your changed entity event is going to be the entire entity, but it's going to be, like, a change flag.
what does the change flag by me versus a state… versus, like, just a report? Like, why… How do I interpret it differently if there's a change flag?
**Dmitrii Anoshin** 35:03 If there is a change flag, it means that it would actually… it was actually changed. That particular event was actually changed from the last time you received an event.
**Josh Suereth** 35:12 So if I don't have a change flag, I can just ignore the event, because there was no change.
**Dmitrii Anoshin** 35:16 You can ignore it, yes, yes. If you don't… if you don't use the heartbeat event, if you don't track them.
**Josh Suereth** 35:21 Yeah, except, like, if I fall out of state with sync, I probably need to diff anyway. You see what I'm saying?
**Dmitrii Anoshin** 35:31 Why do you need to diff if you can just read those events in that case periodically? So, the issue in all these systems is you cannot guarantee delivery of events.
Yeah, right.
**Josh Suereth** 35:43 So, like, a change event might not happen. And so the heartbeat is your backup to basically get the state back in sync.
So you always have to pay attention to it. So, like, you literally… I think you could just remove the changed flag, and your design doesn't change at all.
**Dmitrii Anoshin** 36:00 In that case, we remove aggregated reporting.
**Josh Suereth** 36:03 I think we could remove aggregated reporting as well, but think about it this way, like, the decision to aggregate reporting, the decision to send states and periodic, I love that it's configurable and I think it should be, but does the event itself change in any meaningful way?
And I think the answer that you have here is actually no. You threw a flag, but you don't need the flag to interpret, because you interpret the event the same way no matter what.
**Dmitrii Anoshin** 36:27 Yes, exactly. Because, you know, if you don't need that, you just ignore it. Like, typically, for the… I guess some backends would just, like, ignore that flag, and they… keep, like, using those events as…
**Josh Suereth** 36:41 what I was thinking was, if you send the flag, it's an update event, and so what we would say is, cool, when we send an update event, we will verify the identity is fully complete, every attribute identity is complete, but you might only get partial description attributes. And so, you will only get ones… if you get them, change them, but don't change the definition of anything else.
**Dmitrii Anoshin** 37:03 Until you get a heartbeat event.
Yeah, I understand. So we are… we are going to the territory of the patches. So, but in that case, like…
**Josh Suereth** 37:11 But, like, a very simple definition of a patch, right? I understand.
**Dmitrii Anoshin** 37:15 I understand, but we, like, simple… so we would introduce patch events.
**Josh Suereth** 37:21 Yeah. And we…
**Dmitrii Anoshin** 37:23 like… We would optimize our change events, but if you want to keep periodic events, so if you're saying that they are important…
**Josh Suereth** 37:32 You need both, yeah. I think, like, even if I'm using state change events, I would need some kind of periodic sync anyway.
**Dmitrii Anoshin** 37:40 this is the biggest thing, right? It's the state change events that we are… we are optimizing for with the… with the, Batch events, this is the smallest part. This one is the biggest.
**Josh Suereth** 37:54 periodic report, I can defer. Like, I can make the periodic report send once every hour.
Or once every day. Like, I can really delay my periodic reports.
if I have a healthy state changer thing that's coming quickly enough, and I'm not dropping it, right?
**Dmitrii Anoshin** 38:14 Okay, in that case, wouldn't be practical, keep periodic reports?
**Josh Suereth** 38:21 Oh yeah, I think we always keep periodic reports.
**Dmitrii Anoshin** 38:24 Okay, for, like, let's say once a day, and then we enable aggregated reporting for, let's say, every 15 minutes.
And every 15 minutes, you will get specifically entities that got… that were changed within that window, not everything.
**Josh Suereth** 38:38 But let's say… let's say I need to… so… so what I'm trying to bounce here is data volume and, like, freshness of state versus, like, inconsistency problem. If I… let's say I want to be as fresh as I possibly can, so I actually want those state changes to come out almost immediately.
Because I want the data… I want the data to be as fresh as possible in my cache that I have in my observability system.
Which means I'm gonna get a lot of state changes, and I want them to be as small as possible, because I want the ability to tweak down the window between when I'm out of state as small as possible. And so, yes, I might miss events, state changes, great, that's fine. I will have this periodic sync that comes in.
But I really, really, really want fresh data, so I really want minimal state change events as quickly as I possibly can.
Aggregated reporting, I think, is fine as a thing, but I think what I'm pushing for here is I want, the, periodic reports.
at a frequency that's acceptable for the amount of data I have, whatever that happens to be, every minute, every hour, every day, like, something, right? There's something that I decide, based on the volume of data, how often this big report can come out.
And then the state changes is the thing I put in the middle.
And the state change is basically how fast do… or how fresh do I need the data to be in my sync, and how much am I willing to pay to do it? But at the extreme, let's pretend like every event that comes in leads to me pushing a state change thing.
In Kubernetes, right, isn't any change to an etcd, like.
config object leads to you getting a notification? Is that right?
**Dmitrii Anoshin** 40:24 Yeah, and you'll get the whole state, essentially, of that particular object.
**Josh Suereth** 40:28 You get just a notification that says, hey, something changed, and then you have to build the full stage.
**Dmitrii Anoshin** 40:31 That's how Kubernetes Watcher and Go SDK is built. We would need to… Do it separately for, like, by ourselves in that case, which is gonna be…
**Josh Suereth** 40:44 Well, yeah, we're trying to do a push-based protocol instead of a pool-based protocol. Like, they can pull. So they can have a push-based, hey, there's an event, and then you have to pull to get the state in. So that way, you as a receiver can decide do I do periodic reports where this thing changed, but it just changed 5 minutes ago, so I'm gonna ignore it for now and I'll pull it later? Like, you can make those decisions in the Kubernetes Watch API. We have to make all those decisions ourselves and push everything, right?
**Dmitrii Anoshin** 41:13 That… yeah, I guess that's how it's done currently, anyway. Like, I… I think I'm missing something here. What do you want to…
**Josh Suereth** 41:24 Oh, what I'd like to do? Oh, I… Okay, let me… let me rephrase what I'm saying in terms of, like, what you have here. I like your relationship placement guidance, I think that addresses my relationship array size thing. It gives us clear guidance for where we put relationships, how we do relationships, and it does mean that the, like, big, big things, like a Kubernetes cluster.
probably won't have many relationships reported. It'll just be a resource by itself, right? An entity that just goes no relationships on it. And then someone else will say, yeah, this namespace is part of that cluster.
Right?
**Dmitrii Anoshin** 41:58 Yeah, yeah.
That's right. Okay.
**Josh Suereth** 42:00 I'm… that… that… that, I think, actually works out pretty well, because I think… I think that will keep them limited, the… let's talk about periodic reports and state changes. We always need periodic reports.
**Dmitrii Anoshin** 42:12 Can I add something here? This was, like, I made that guidance because I was thinking how to avoid going into the patch changes, like, capabilities, because if we do have patch changes, that's gonna be not that much relevant, because we can potentially introduce patch changes to the relationships as well, I guess, like…
**Josh Suereth** 42:40 I, I think you, you nailed it. I don't… I'm comfortable right now, but I'd want to prototype this, that we won't need batch changes with that change, yeah.
**Dmitrii Anoshin** 42:50 By the way, sorry to interrupt, if we don't have patch changes, can we defer that problem about the volume to the protocol somehow?
Like, we…
**Josh Suereth** 43:05 Possibly? The state change thing… this goes into how we define our protocol.
I think that the next thing I wanted to say, state change in periodic reports and this update event.
I think the notion of whether we send deltas versus full state change is something we could add later.
As long as we are clear about how the event is interpreted. What you've defined right now, I think you can cut that updated flag. Don't even put it in, because I want… I want to save room in the design where if we wanted to add delta state changes.
we could do so later. Initially, what you're proposing doesn't have a delta state change, but it does have state change, and I think that's totally fine, right? If I get a periodic report of an entity with a relationship, I interpret it the same as I would just a state change event, right?
**Dmitrii Anoshin** 44:04 They're exactly the same, there's no difference.
**Josh Suereth** 44:09 What we still haven't answered is… you have to, as a consumer of this, I have to understand your timing window for periodic reports to know when I can kill an entity, to know when it has been deleted.
**Dmitrii Anoshin** 44:30 Yeah, I do have that field here.
**Josh Suereth** 44:32 Oh, so it's sent… the reporting interval has to be sent with each message. Yes. So for an entity, you know what the heartbeat will be.
**Dmitrii Anoshin** 44:39 Yes.
**Josh Suereth** 44:41 Okay.
**Dmitrii Anoshin** 44:43 And it's also value of 0 indicates that periodic events are disabled. So, actually, there is some… redundancy here. This can provide the same information as this Boolean flag.
Isn't that essential?
**Josh Suereth** 44:59 I see. I think we can get… we can get… well, you don't want Entity Updated to get used as the heartbeat event, is what you were trying to avoid?
**Dmitrii Anoshin** 45:07 Yeah, I mean, that's what they originally paid…
**Josh Suereth** 45:12 Honestly, I think it's… so this is what I would change in the model. I would get rid of entity updated, you don't need it, keep report interval.
**Dmitrii Anoshin** 45:19 But basically say it's okay for entities to be reported more than.
**Josh Suereth** 45:24 this interval.
Like, you might get events more frequently than this interval.
**Dmitrii Anoshin** 45:28 Yeah, that's true, that that's implied. I probably… I need to put it in words, but that's implied if you have update events enabled.
**Josh Suereth** 45:36 Yes, and so the update event thing is not even in the data model, it's a pure configuration capability, right?
So I like that. I think that works. So, so basically with your relationship change, with this update change, the only thing that… okay, so I can use report interval to detect if things die.
What… are we missing anything else here?
**Dmitrii Anoshin** 45:59 So in that case, I'm removing aggregated reporting from here, right?
**Josh Suereth** 46:03 I don't think we need that, yeah.
I don't think we need NC updated, I don't think you need NC reported.
**Dmitrii Anoshin** 46:09 Yeah, I guess that also was coming from Tigran to that thread, so, like, we are more aligned with him in that case.
**Josh Suereth** 46:18 Yeah, and then this notion of whether you send Delta events, I think I would actually put it in the OTEP as potential future work.
**Dmitrii Anoshin** 46:27 Okay.
**Josh Suereth** 46:27 when we launch this, if we run into problems with scalability, I think that what you've defined, we could expand that way in a non-breaking fashion.
**Dmitrii Anoshin** 46:36 I agree, yeah.
**Josh Suereth** 46:37 Yeah.
Cool.
**Dmitrii Anoshin** 46:41 We can call it, like, it's just the name of the event, right? We can, entity state and entity delete. We can…
**Josh Suereth** 46:50 We can do an entity update, yeah, which is… which is a partial… partial delta or something, yeah.
**Dmitrii Anoshin** 46:55 Yeah, something like that.
**Josh Suereth** 46:56 Yep.
Are you still planning to put this in a log push-based protocol? Or do…
**Dmitrii Anoshin** 47:03 And that's the most, like, reasonable way to put it, because we already have, like, we… events as a thing in OpenTelemetry.
So, and this is an event, it's just a different type of an event that we can specify in OpenTelemetry, semantic conventions.
**Josh Suereth** 47:25 So, one thing we did, and I know this is awkward as hell, but one thing we did in Google, we have, like, events that are special, or, like, different. So we have this thing called telemetry type.
Which is… right now, it's a resource attribute, because that's how you make batching different in OpenTelemetry, is you change the resource identity. So we have this thing that you put there, that lets you say, like, cool, I have a batch of data, and it includes, like, entity events, and it includes other events.
And so, I'm actually grouping them separately on purpose, because they might be authenticated separately, they might be rejected separately, they might go different places.
Which is a bit awkward, but that's… that's one thing we're doing.
That's my only fear with entities, right? Is, like, let's say I'm sending entity events through the collector.
And the collector has a memory-limiting processor and a batch processor, and I get flooded with a whole bunch of logs at the same time I'm sending entity events.
**Dmitrii Anoshin** 48:28 Yep.
**Josh Suereth** 48:30 Do I drop the entity events? Do they make it through? Do I have any control over that? I could, like, I have all the capabilities today to fix it, right? I could… But do I want it to be protected by default? Do I want it to be a separate channel by default? I don't know. That's… I'm still… I'm still on the fence here. I think… using the OTLP logs, spec.
to work out all the details here makes sense to me. Like, let's start with OTLP logs, let's just use them for all of our prototyping.
If we run into, like, issues where we can't work around them, or we have friction because logs and entity events are flying through the same channel.
then we can start proposing something more aggressive. Does that sound reasonable?
**Dmitrii Anoshin** 49:16 Sounds reasonable, yeah. We can… or, like, I'm speaking for the future, but if we have those reasons, we are… I think we might have different ways to approach that, not only going to a separate signal. Like, for example, as you said.
Oh, like, completely treating them separately and never batch, that kind of… introducing that on… on a… I don't know, like, not a protocol level, but on subsymmetic conventions level, so everyone… everyone must.
**Josh Suereth** 49:46 Yeah.
**Dmitrii Anoshin** 49:47 Follow that, and the collector as well, something like that.
**Josh Suereth** 49:49 Yeah, just like a collector convention could work too, like, we don't have to be heavyweight, I think.
**Dmitrii Anoshin** 49:53 Right, right, right. Yeah. It's just… I've been trying to avoid introducing a new signal, because it's, like, it's just too much work for… with less returns, I guess. I cannot justify it enough to make… from my perspective, I cannot justify enough to make it a separate signal, at this point, at least.
**Josh Suereth** 50:15 Oh, the other thing I wanted to ask about real quick, we have 10 minutes left, and I think we had a great discussion, and I think we're coming to a close here. And I think this is true. The resource for which an entity event is reported is important.
**Dmitrii Anoshin** 50:29 Yeah, it is.
**Josh Suereth** 50:30 It's the observer, right?
**Dmitrii Anoshin** 50:31 Yeah, yeah.
**Josh Suereth** 50:32 It represents the state from that observer's point of view.
**Dmitrii Anoshin** 50:35 It's, like, not like an observer, but rather, like, over… overarching entity kind of thing. So, for example, if you send from a entity for Kubernetes cluster the resource.
Has to be in the context of the cluster, not, not something more granular.
**Josh Suereth** 50:57 Like, the resource would be the cluster itself, or information about the cluster, right? Yeah, yeah, yeah. Okay, I think that's critical to the data model. I think you called it out, but I want to go double check.
**Dmitrii Anoshin** 51:08 Okay, I'll… I'll ensure it's called out, yeah.
**Josh Suereth** 51:11 Yeah, because I would… I would put a section about multi-observer.
So, like, imagine if, for some reason, we have two… Different observers of entities reporting about the same set of things.
So, let's say I'm getting information about Kubernetes from Kubernetes itself, and let's say I'm getting information about Kubernetes from the cloud provider's record of Kubernetes.
How do we want to resolve that?
I actually don't think… I don't know if you need to put that in your model, I just want to think about it a little bit.
**Dmitrii Anoshin** 51:47 Yep.
**Josh Suereth** 51:47 Like, I don't think anything changes, but I'd want to think about it, make sure that we have an answer, that's all.
**Dmitrii Anoshin** 51:53 Yep.
**Josh Suereth** 51:54 Yeah.
Cool. Hey, great, this is good, man, thank you.
**Dmitrii Anoshin** 51:58 Sure, thank you for discussing this, it's very helpful, and now I'll address your…
**Josh Suereth** 52:05 comments, and I think we are gonna be in line with Stikran as well, because I've seen he's asking about…
**Dmitrii Anoshin** 52:11 some changes and review from your side, and I think you addressed everything.
**Josh Suereth** 52:17 Yeah. Yeah, I mean, my main concern was just, if these relationships are sent from the big end, I think this becomes unwieldy as hell. But we resolved that by forcing it to be from the… yep, cool.
Awesome. Thanks, Ben. We'll see you next week.
**Dmitrii Anoshin** 52:34 See you next week, bye!
