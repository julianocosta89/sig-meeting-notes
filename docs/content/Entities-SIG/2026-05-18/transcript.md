SIG: Entities SIG
Date: 2026-05-18
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**krajo Krajcsovits** 05:22 I agree.
**Ted Young** 05:35 Wow. Can you make that work for Otter, Daniel?
**Daniel Dyla (Dynatrace)** 05:41 I know it works for Fireflies, I… there's a couple of… Otter may have a command also, I don't know it. Oops.
**Ted Young** 05:48 Oh my gosh.
**Daniel Dyla (Dynatrace)** 06:09 I'm not seeing anything from a quick Google search.
I don't… it doesn't matter that much. I don't feel that strongly about it.
**Ted Young** 06:17 Yeah.
It'd be nice if there was a convenient way to do it, though.
Anyways.
**Daniel Dyla (Dynatrace)** 06:26 Are we waiting for Josh?
**Ted Young** 06:28 Yeah, I didn't see a message in Slack saying that he wasn't gonna be here.
But…
**Daniel Dyla (Dynatrace)** 06:45 I also don't see anything on the agenda.
**Ted Young** 06:48 Yeah, I can make an agenda…
**Daniel Dyla (Dynatrace)** 07:26 I can send Josh a quick message if nobody else has.
**Ted Young** 07:29 Yeah, go for it.
**Josh Suereth** 08:53 Hey folks, sorry I'm late.
**Daniel Dyla (Dynatrace)** 08:56 Yeah, no worries.
**Josh Suereth** 08:58 Are we all do it.
**Daniel Dyla (Dynatrace)** 09:00 Good.
**Josh Suereth** 09:09 Okay, so… Topic-wise, Ted, you're writing. If you want to talk, I can finish writing for you.
**Ted Young** 09:18 Sure. Okay. Okay.
Yeah, I was just coming with some feedback from the browser, SIG. You know, Martin's been working on the, the entity provider, spec that got merged, and we ran into just… an issue with it not being particularly relevant to the work we're trying to do in the browser. It's not unique to entities, this is actually… we're looking at for the browser SDK, just having to deviate from the spec entirely, because the… the environment is just so ridiculously hostile. For example, the spec presumes you can have a context object and put it somewhere, anywhere, and the browser's the one environment where there's literally nowhere to put that in a way that wouldn't massively impact, you know, the performance of the browser SDK.
So, you know, we can't use, like, zones or anything like that, to put a context object anywhere, so… In general, We're gonna be taking approach going forward on the browser of, like.
you know, as long as we're collaborating well with the JavaScript SIG and those maintainers to make sure the parts that need to work across Node and the browser work, and as long as at the other end of, you know, like a collector.
processor or something like that, you get, you know, standard OTLP. That looks no different than OTLP you'd get from somewhere else. It's okay for… The stuff in the middle to go its own way, provided that we document it well, you know, what we're up to on the browser since, Since it won't be conforming to the spec anymore.
So that's just the reality that we're having to live with in the browser.
Not, not, not done out of spite, or anything like that.
**Josh Suereth** 11:27 No, I… dude, I… I… I think you've heard me supportive of that several times in this meeting and other meetings. Like, I think that's 100% the right thing to do.
**Ted Young** 11:35 Yeah, we're throwing in the towel. But the one piece of feedback I think that is relevant here was, you know, trying to, you know, Martin did give it a shot with what was in there, and it was just a reminder that the… The stuff related to entities that did get merged into the spec is really focused on metrics, and, like, how do you deal with a metrics pipeline?
But I'm a little concerned that just having that in there, you know, we ended up being confused and trying to apply it everywhere, which ends up making kind of a confusing API for… for, like… traces and logs. Basically, you know, with metrics, you're caring about which entities, right? But in your tracing and logging pipeline, the answer is, like, all of the entities. You're kind of doing something a lot simpler, where, like, if any entity changes, you're just basically segmenting the batch.
And starting a new batch.
And maybe you have some complexity about, like, how many batches go out on a request or something like that, but… It's a simpler problem, but I just wanted to flag that because it might be confusing for other people, just the current state of things, if they go try to implement these.
**Josh Suereth** 12:55 Yeah, I mean, to be fair, that OTEP is not technically in the spec, it's a direction, and when we accepted it, we knew it didn't… like, like we said, this is solving a problem, but it's not the problem browser has. Right.
**Ted Young** 13:08 Right, that… but that was just, like… well, I'm trying to say two things. One, we're going our own way in general, but it was just a reminder, like, for… even though we won't be putting pressure on this SIG anymore, like, coming from the browser side, because we'll just be doing our own thing, And trying to make sure that, again, on the other side of the collector, you would get entities the way you would expect entities to be showing up.
**Josh Suereth** 13:35 Yeah.
**Ted Young** 13:36 But what we actually do in the browser might be a little different.
**Josh Suereth** 13:39 that's the biggest thing I want us to make sure we agree on, is, like, the, like, you know, the foundation of OpenTelemetry is the protocol and the data that makes it on the protocol.
Right? And the data model of that protocol. So, if we can agree on what your signal entity relationship looks like when it's all the way back to OTLP. It can do other shenanigans in the middle, in my mind, that's fine, right? But, like, when we get back to it, as long as we have that right relationship, and if you have trouble modeling that.
or getting to a state that you're happy with, that's when we should really be talking. Because I… I still think, and I… I think this is true. The whole, like, we have a session, and we have, you know, a log or an event tied to the session, like, that's not changing, right? That's still how we're thinking about the world. It's just, we don't have an SDK that makes it easy for us to do that.
**Ted Young** 14:33 Yeah, yeah, I mean, like, the short-term version of probably what we'll do is just, like, the entities might change between… or the resources might change between batches, right? And we'll be using a log, an event, you know, to indicate the start and end of a session, and then As entities settle down, you know, we'll be… Like, switching to that data model.
But, you know, in order to be able to, like, ship something with the data model that we have.
we'll just be doing it that way.
**Josh Suereth** 15:07 But also to confirm, like, the batching that naturally happens with resource should happen. So, like, if I have a bunch of logs attached to session, and it's session 1, I have a bunch of logs attached to session 2, I can treat those as separate batches, and I can aggregate them separately, right?
**Ted Young** 15:24 Exactly, yeah, that's how we'd be doing it.
**Josh Suereth** 15:28 Yeah.
Yeah, like, if we break that, then I'd be, like, scared of any of this, but, like… I think we're fine.
**Ted Young** 15:38 Yeah, no, that would be the idea, is that they would be separate batches, and again, you know, on the connection between, like, the browser and whatever gateway, if there's some… You know, if repeatedly sending resources like that doesn't make sense, like, maybe we're doing something else there as well.
You know what I mean?
Yep.
But… but… The idea that, that, you know, these are just resource… attributes.
and they apply to all the data in this batch is, I think, what we want it to ultimately be.
**Josh Suereth** 16:22 Cool.
Well, you can report on more than one session in a batch or not.
Maybe that… maybe that's more of a… A question we don't have to answer.
That's just my own curiosity.
**Ted Young** 16:37 You mean, can you have more than one active session going at the same time?
**Josh Suereth** 16:41 Or, like, I didn't get my batch of data sent on the previous session, the session has changed, so with the… when I report data, I'm gonna report session one and session 2 at the same time, yeah.
**Ted Young** 16:55 Yeah, yeah, I mean, that's like… I don't know how OTLP, I don't think, is designed to… to have multiple batches be sent in the same message.
**Josh Suereth** 17:07 You can, yeah.
**Ted Young** 17:08 You can? Right.
**Josh Suereth** 17:09 Yeah, so the outer part of OpenTelemetry allows multiple resource batches.
So, like, you can have… you can have multiple resources, and that's what, like, the collector is defined to do. In case you get multiple resources coming in, you can batch them all together into one request if you want. So, yeah, like, you can totally do that.
**Ted Young** 17:28 It's just, like, again, you run into this issue on the browser where, you know, compression, right, like.
GZIP-style compression isn't available, and we have, like, network constraints, so, like, you'd be, like, sending, like… you'd be changing one resource attribute, and it would be a very heavy payload.
Right? So… but then that's… that's more of a question of, like, how to… you know, we'll just go solve that on the browser side of, like, how do we want to…
**Josh Suereth** 17:58 Look at what profiling did. Look at what profiling did. They have the same problem. So they have a dictionary so that you don't have to repeat resources, and they can have hundreds of resources in the same batch if needed. Since profiling is running on, like, big servers, and they're looking at a whole bunch of processes.
Right? That's why we… I mean, it took forever to get this approved through everybody.
But the profiling signal has a dictionary, and the expectation is at some point we might need this for other use cases. I would prefer if we don't, like, invent something brand new after… if that would work for you guys.
The dictionary thing.
**Ted Young** 18:35 I don't know that that solves this particular problem.
Because it's not about having tons of resources in one batch, it's about… you know, basically, like, we don't want to send the same data twice. Yeah. So we want to be sending diffs, or… you know what I mean? I don't know.
**Josh Suereth** 18:56 Depending diffs, or having a pre-agreed-upon dictionary, we say, I'm resource 10.
And then it knows on the other side what you are, yeah.
**Ted Young** 19:05 Yeah, yeah, I… unclear. One problem at a time, but I think the main thing was just to… to kind of announce to the relevant SIGs, it's like, we're just gonna try to… solve things our way just for the browser. The other clients, you know, might care more about this stuff, but I think… we're the only ones who are, like, present in this SIG, so I just wanted to flag that, like, you know, there's interest from the collector and elsewhere around, like, how do you deal with… with entities in relation to metrics? But, in terms of, like, there being… you know, maintainers in this SIG who care about, like, the logging and tracing pipelines, like, just wanted to flag, like, with us not pushing on it, I don't know if you have anybody Caring about that.
So…
**Josh Suereth** 20:02 Yeah, yeah, I mean, I think all of our prototypes started with the login and tracing one, it's just, we ran it, like, we wanted to get all three working at the same time, which is why the design focuses so much on metrics, is because metrics is harder, but yeah.
Yeah, like, We can talk through more, but I hear what you're saying. The high cardinality entity changes, or mutation… mutable resources, we are putting on hold for now, yeah.
Yep.
**Ted Young** 20:33 Cool.
**Josh Suereth** 20:34 Let's, if it's alright, is there anything else you wanted to say there? No?
**Ted Young** 20:40 That's all I wanted to say. I don't know, Martin, if you have anything to add, or… I think I got it right.
**Martin Kuba** 20:49 Yeah, I think you summarized it well.
I mean, I think we still… the one pending thing also is… It's, like, it seems like there are… Different opinions, whether or not we should support metrics, and how in the browser.
But I think… at least for immediate future, I would like to just focus on Logs, events, and traces, because those are, like, the primary Use cases for browser.
And then we can… we can sort out metrics, Once we have… once we have more… more consensus and more information.
**Ted Young** 21:29 People want a metrics API, but we don't want to be handing out a foot gun.
So… You know.
like… It'll probably end up being something funny, like, you have a metrics API, but it emits logs.
**Daniel Dyla (Dynatrace)** 21:46 I mean.
**Josh Suereth** 21:47 Honestly, that…
**Daniel Dyla (Dynatrace)** 21:48 The reason we have a separate API and SDK anyway, is to enable stuff like that.
**Ted Young** 21:53 Exactly.
**Josh Suereth** 21:55 Yeah.
Alright, let's, let's jump into some of our hard topics here. I wanted to start with, ID context, and then get into, SDK startup, if that's cool?
So ID context, I was thinking about this, Dimitri, I haven't had time to actually do… any hard thinking. I was able to tickle all my agents, but I wasn't able to do real work, if that makes sense, because of being slammed with meetings.
What I'm thinking is, for this.
I… I… we asked a lot of hard questions, we had a lot of back and forths here.
Do you have an actual prototype implementation in the collector? Because maybe what would resolve this is if we added some prototypes and SDKs.
**Dmitrii Anoshin** 22:43 Yeah, that's what I want to suggest. I can submit a draft PR for the proto, and then use that proto somewhere in the collector and see how this would work out. And if someone can help me with using that proton in the SDK, That would be good as well.
Does make sense?
**Josh Suereth** 23:00 Yeah, I guess what I want to see is, my concern is that, You have process host container relationships and resource detection processor.
But you're making the code aware of each other, right?
So, like, the host… Does the host detector have to know about the process detector being configured? Does the process detector have to know about the… container?
detector being configured. That's… but that, like, legitimately, that's my main concern, like, is that there's a code dependency between the two.
**Dmitrii Anoshin** 23:33 Yeah, that makes sense, makes sense.
**Josh Suereth** 23:36 Yeah, and so if we have, like, an open ecosystem where people start defining… like, Kate's, right?
Does the Cates container have to be aware of process, or of container? Like, we'll have to figure that out, too.
**Dmitrii Anoshin** 23:50 Yeah, for the resource detector process, it's pretty straightforward. We would, for example, each detector would set its context entity, it's just a type, nothing else. It's just a type, and before sending data downstream, we… it would call some kind of, like, sanitize, or normalize, or something like that. And it would check if the entity doesn't exist.
Let's say host entity doesn't exist, it would just drop that reference from the container entity, for example.
Or from the process entity.
**Josh Suereth** 24:28 Right. Would process, like, say that it could be part of both host and container, and is that hard-coded in the process detector, then?
**Dmitrii Anoshin** 24:37 Container is not part of the resource detection right now, so that entity has to go through SDK, and same goes to process.
So, yeah, that's actually… That invalidates my approach.
So, I see what you're saying. If we have a reverse relationship, it will be always easier when we add something on top, when we have a resource detection that adds it on top.
But at the same time, why, why can't, let's say, host Host detector just mutate process entity.
**Josh Suereth** 25:22 I mean, that's an option, that's why I think we need to prototype this. Like, what I want is, I want us to have a way where, like, I write a process detection algorithm, right? Where I'm gonna make a system call to get, all the processes, or I'm going to actually, like, look in my environment or something to figure out what my PID is, right? Like, I write that code.
What I don't want in that code is I don't want that code to have to understand any possible entity that's been modeled. Like, I don't… it just looks up PID. It doesn't… say, okay, cool, let me check if I'm Docker, let me check if I'm host. We need some way for that logic to exist, but, like, that component of a process detector should just say, what's my PID? And let me say, I found that I am process foo, right?
Similarly, a host detector would say, cool, let me get my host ID in some fashion. I'm gonna look at hostname, I'm gonna look at something else. We have an issue with hosts, right, with, like, the AWS, and the Azure, and the GCP, and the cloud for Alibaba, like, where host ID might be their cloud ID.
So we have that issue, too, where we don't know which detector's really going to provide host. So, if I have the host detector in two places, how do I know that host is going to be you know.
How do I know who owns the process if host is the one with the information? That gets awkward, too.
**Dmitrii Anoshin** 26:54 Yeah, how… Sure. Go ahead, go ahead.
**Josh Suereth** 26:59 Okay, the last thing is kind of this container-host relationship we have, right? Where, like, we have the notion of a host, and we have the notion of a container, and a container kind of belongs to a host, and so a process can either be part of a container or part of a host.
Right. And so we don't know which parent we need to pick.
in that… like, if there is no container, you would have process and host kind of tied together. If there is a container, then you have process, container, host.
**Dmitrii Anoshin** 27:30 Yeah, I think that would be responsibility of the particular detector, and so particular detector would set the additional entity.
With… along with all the attributes. Seriously.
**Josh Suereth** 27:43 You're saying one… one detector… Would do process, host, and container together.
**Dmitrii Anoshin** 27:50 No, I'm not saying that. I'm departing, let's say, the context detector. So, for example, host detector would set host entity, and it would look for other Let's say, entities, and set the relationship there.
Okay. It's gonna be… it's similar to your suggestion, like, reverse relationship, but in terms of, like, the data model would have direct relationship model.
But, we would set… set that in the reverse.
Order, essentially.
**Josh Suereth** 28:26 Okay.
**Dmitrii Anoshin** 28:26 So, the responsibility of the context identity entity would be set its own entity and its child entity, mutated if it's not… if it's alright, you said.
By mutating images, like, setting the reference, essentially.
**Josh Suereth** 28:43 Alright, so if I… if I were to strawman this… Right?
allow other… chapter.
mute change previous entities. So we would define something where we'd have, like, a process detector, a container detector.
And a host detector, right?
**Dmitrii Anoshin** 29:10 Yep.
**Josh Suereth** 29:11 Alright, and so… Oops.
Example order.
And then we'd have something where, like, the host detector Would check for a process entity with no You call it the ID context, what do they call it, or ID scope?
Whose name?
**Dmitrii Anoshin** 29:32 Context… context type… context entity type?
**Josh Suereth** 29:39 tape.
And we eat, and… would add itself.
the process entity. Okay, like, like that, right?
**Dmitrii Anoshin** 29:50 Something like that, yes.
**Josh Suereth** 29:52 So, hosts know that they can have processes, containers know they have good processes. Container would do the same thing if a container is detected. If a container's not detected, it wouldn't, right? So, if I define these three in this order.
and I'm running on a host, I would end up with process, where the context entity type points at host, and end up with host.
**Dmitrii Anoshin** 30:14 Yeah, if container isn't there.
**Josh Suereth** 30:20 Yeah.
I… I want to think through it, but I'm thinking that actually this… this is, this is what I wanted to get to. I'd like to prototype it. Like, I want to do this in the SDK, and then I want to look at what you did in the collector, and then we can, figure out the two things and see… See what we think about that as an algorithm.
**Dmitrii Anoshin** 30:40 Sounds good, yeah, let's… I can put Java prototy and use that in the collector, and we can use this one here.
**Josh Suereth** 30:49 GDP.
Looks at this. Okay.
Does anyone else have thoughts here? I don't want to monopolize the whole conversation.
**krajo Krajcsovits** 31:04 It seems pretty… Simple enough for people to understand what happens if you just have to figure out the order.
And also, It ensures that you get a tree, not a general graph.
Which is good for navigation, so… Seems fine, but, like, I'm the newbie here.
**Yordis Prieto** 31:27 I only have one question, is a container assuming only one container?
**Josh Suereth** 31:34 So, for a detector.
you're detecting, like, your current process, or, like, your current environment, so yeah, there would only be one… like, if I'm… if I'm a running thing, if I'm executing code, there'd be only one thing for me to detect. This is not like a, I'm detecting something remote. This is like I'm detecting myself.
Right?
**Yordis Prieto** 31:57 Yeah, yeah. It's just, like, in between the host and the container, there may be, like, multiple of them, no?
**Josh Suereth** 32:03 Oh, you're saying, like, I could have a container within a container?
**Yordis Prieto** 32:06 Yeah, yeah, yeah, between the host and the containers, like, I don't… I… yeah, I'm just playing devil's advocate of, like, the semantics of what those actually means.
**Josh Suereth** 32:18 Yeah, we… we decided early that we wouldn't actually put that in resource, right? So we would do the inner container and then skip all the way to the host.
But that is a good…
**Yordis Prieto** 32:30 Worth documenting, then, like, that type of semantic is where people get caught up with.
**Josh Suereth** 32:35 Yeah.
It's the exact…
**Dmitrii Anoshin** 32:38 We discussed that, but I don't believe we ever put that in wording. But we have some restrictions in the data model that specifically put restriction.
That entity on the resource cannot have multiple instances of the same type.
Because otherwise… even, like, our current TLP model with backward compatibility with resource cannot work.
**Josh Suereth** 33:08 Yep.
**Dmitrii Anoshin** 33:09 So, if there are some use cases when they're container and container, or, like, VM and VM, those… topologies has to be sent through side channel, through the events.
**Yordis Prieto** 33:25 I'm guessing it's the same for forking the process and things like that?
**Josh Suereth** 33:30 We're forking the pro… you mean, like, when I get a new PID?
**Yordis Prieto** 33:33 Yep.
**Josh Suereth** 33:34 Yeah, right now, that… you're hitting on probably the most awkward part of OpenTelemetry. I don't know if you've seen what Python does. They effectively redo their resource detection every time you fork.
So you end up with a, you end up with a… you're reporting as if you're a different instance of the SDK for every fork.
**Yordis Prieto** 33:57 Okay.
**Josh Suereth** 33:58 Yeah, like, we… I… forking is an Achilles heel, in my mind, of the SDK, and it'd be nice if we come up with some better way to solve it, but yeah. What I, like… If you wanted to have allow forking, but have the same ID, what you would do is actually not include your process in your resource.
So your resource would be, like, your… you'd have a service instance ID, where you'd synthesize an ID when you start up. That's the thing that you'd report all your data against. And then, the process ID would have to be something you'd put somewhere else in your telemetry, similar to, like, the session ID or this mutated thing.
**Yordis Prieto** 34:39 Yeah.
Sorry for asking that.
**Josh Suereth** 34:44 No, no, no, these are good, these are good questions. Again, this gets into… so we've gone back and forth with the browser folks about, like.
this notion of session and how it can change, right? Well, process ID can change every time you fork, effectively.
On the SDK. So for the lifecycle of the SDK, when you fork.
it's still there, but there's now this new instance that has a different PID.
Where do we record the PID? I think is the question.
For, like, a forking process.
like I said, today, the way I know Python works is it actually just recreates the frickin' resource every time you fork. There's, like, a hook for it.
**Yordis Prieto** 35:23 Should it be, like, a list of pids, like, you know, in buck… like… Yeah, should it be any attribute that is actually… you append to it every time you do a forking, and then you propagate that?
**Josh Suereth** 35:36 That… so the problem there is it breaks the identity. We can go into that, but the…
**Yordis Prieto** 35:40 Yeah, yeah, okay.
**Josh Suereth** 35:41 We need resources to have a stable identifier so that you know, like, what you're talking about, and it doesn't change repeatedly.
**Yordis Prieto** 35:47 Right.
**Josh Suereth** 35:47 So, the fact that you're a new PID, changes the identity for anything you report against that process, but not for the overall service. So it depends… it depends on, like, your metric and your use case. If I'm tracking per PID information.
Right? Then… then I do need to mutate, have a new identity to say, here's this PID, and it's separate from this one, but if I'm not actually tracking something by PID, if I don't care, I'm just tracking, like, request count.
I don't care if the request was on PID 1 or PID 2, if, like, my metric is for the request.
But for spans and logs, I probably do. Like, it'd be nice to have that for debugging information.
**Yordis Prieto** 36:27 Got it.
**Josh Suereth** 36:28 Yeah.
**Yordis Prieto** 36:29 My daily work is in airline and Elixir, so that word process is even way more confusing for OpenTelemetry.
**Josh Suereth** 36:38 Yeah, for context, service instance ID in Erlang is, I forget what the hell they call it, but you know how every time you make an actor, you get a random ID?
**Yordis Prieto** 36:47 Yeah, a paid processor.
**Josh Suereth** 36:49 Is it… is it your bid? Okay.
**Yordis Prieto** 36:50 Yeah, it's a pain.
**Josh Suereth** 36:51 That PID that you get in Erlang is your service instance ID. So anytime you are like, communicating in OpenTelemetry, your resource is tied to that thing.
**Yordis Prieto** 37:02 I need to talk to you, because, like, I've been drawing, like, multiple semantic conventions, because…
**Josh Suereth** 37:07 Yeah.
**Yordis Prieto** 37:08 almost everything in airline is like, okay, I understand, but what do you actually mean? Because for me, it's a completely different situation. So I need to talk to you, Josh. I think you may be the one that I was looking for.
**Josh Suereth** 37:20 I can try to help, yeah. The way I phrase it to people, though, is I, I tried Erlang in college, but I never inhaled, so… I can… I can at least speak to some of it. Okay.
Interesting.
To bring this all to a close, though, I think the thing we need to do here is prototype.
And this discussion around forking I'll put an agenda item on for next week to kind of talk through, like, what… how we want to handle forks. I think it's an overall OpenTelemetry issue that we… Just look at the Python docs for how we handle forky, and you'll see that we don't do it well.
it probably deserves a broader discussion, but let me… let me think about that, because I think it's very similar to browser. If other folks want to do writing on, like, how we handle fork and stuff, let me know. And yeah, like, is… is it pronounced Yortis, by the way?
Okay, if you want to sync with me on Slack or something, happy to, like, bring you up to speed on things for… how we deal with Erlang and SEMCOM. Okay.
Tristan might be a better person to talk to, though, overall. Okay.
**Daniel Dyla (Dynatrace)** 38:34 Sounds like a…
**Josh Suereth** 38:35 Wrap for that. Go for it.
**Daniel Dyla (Dynatrace)** 38:37 Before we move on, does this introduce… Like, an implicit dependency on both Like, on one detector, depending on another, both from, like, a… the host detector has to be aware of every type of child that it might have, and also… The configuration has to be done in a specific order, or the process will fail.
**Josh Suereth** 39:04 Yes, it does both of those.
Yep.
So, the difference, though, here is we break the dependency that process doesn't have to know if anything owns it.
But host has to know what it could own.
**Daniel Dyla (Dynatrace)** 39:23 Yeah. I mean, that information has to be encoded somewhere, so… I guess it's fine.
the… ordering, I think, is potentially just confusing, unless we make it very… either very well documented, or… like, the default configuration might just be good enough for 99% of people, and they never have to mess with it. But I think it'd be very easy to misconfigure.
**Josh Suereth** 39:49 Right.
I hear you. Like, the other option is we could actually just invert the order.
So, like, host detector would be configured as high priority, like, first, and then… and then processing container. We just walk them backwards, but I agree with you, the fact the order matters may be surprising to people, but may not. Like… For context today, like in the collector, right?
there's an upsert-insert mechanic, where the order actually does matter, and the prioritization of that order does matter. So, I think we just align to those expectations, and then we'd be okay. But, like, to your point, I'm still… A little bit nervous about this hard-coding, like, implicit dependency from, like, host to process, if you will.
I just don't have a better idea for how to solve it.
**Daniel Dyla (Dynatrace)** 40:38 Well, one thing we could do is enforce it.
you know, at… At startup, we could load the list of detectors.
And… either… either log a warning, or, you know, whatever we want to do, say, like, you… configured the host detector before the container detector. This may cause problems.
Because if host container knows all of its potential children, then it should… you should be able to detect if you did that in the wrong order.
**Josh Suereth** 41:12 Yeah, let'.
**Daniel Dyla (Dynatrace)** 41:13 And we should also do some sort of cycle check on the dependency as well.
**Josh Suereth** 41:18 Yeah, right, like, that's kind of what I'm thinking, yeah.
We could do cycle checks. So, so, we could also even allow it to be configured if it's not explicitly there.
So, if every entity detector says, here are the things that I could own.
If you see this thing, I am its context owner.
And that's also part of the configuration. I could add things that the detector didn't know about when it was written.
**Daniel Dyla (Dynatrace)** 41:48 Could you?
**Josh Suereth** 41:49 I think.
EBITDA.
**Daniel Dyla (Dynatrace)** 41:53 That's if your configuration is, like, a nested, complex configuration object. I'm thinking it's still just, like, a flat list.
**Josh Suereth** 42:00 No, I'm thinking… I'm thinking of something less.
Right? It's a flat list.
And then it has a field called Can Own.
That says, cool, this thing can own processes, right?
And again, names… I'm terrible at names, but, like.
So basically what this would do is this would guarantee, no matter what order I have.
the container detector would have to happen after process, host detector would have to happen after process, and I would have the system figure out What the ownership looks like based on the hierarchy that you see.
**Daniel Dyla (Dynatrace)** 42:41 Yeah, that's… That's more or less what I was saying.
**Josh Suereth** 42:44 Yeah, yeah, yeah, I think…
**Dmitrii Anoshin** 42:47 Sorry, it might be not part of the detector capability, but, like, the overall detection framework, like, this, like, common code between them, after you apply all of the attributes identities, that thing can additionally set all of the relationships between entities.
Does that make sense? So in that case, we don't need to worry… worry about any ordering.
**Josh Suereth** 43:15 Yeah, yeah.
I think that's kind of what… what we're teasing out here. We… you still want to make sure you don't have, like, a… If you allow this kind of relationship to be defined, we'd have to make sure it's configured appropriately and have safeguards and things, but.
**Dmitrii Anoshin** 43:33 Yep.
**Daniel Dyla (Dynatrace)** 43:34 We could run them out of order if we did it in a two-stage process. You could have one stage, a detection stage, and then, like, a relationship resolution stage.
**Yordis Prieto** 43:44 Could you, could you… Could you… to make a point, let's say there's a list of something, and somebody wants to append to it, could you do that between the detectors?
So it's no owning the whole thing, it's more like, you know, like… Modifying it?
**Josh Suereth** 44:06 Say that again?
**Yordis Prieto** 44:08 To imagine there is some value that is naturally a list, for whatever reason?
And the detector, all it's doing is just appending to it.
**Josh Suereth** 44:21 So that's… that's what we have now with the detectors. So there's just a list of entities, and they append, but there's a uniqueness guarantee. So we'll actually look for… we'll see it, Dimitri. There's a uniqueness guarantee where, like, only one of a type can exist, otherwise we have, like, conflicts, problems. So…
**Yordis Prieto** 44:38 the owning is, like, the whole thing is for it, so you cannot do anything after, like, I'm just…
**Josh Suereth** 44:43 Oh, oh.
**Yordis Prieto** 44:44 How bad?
**Josh Suereth** 44:44 Owning is a new proposal, so that's what this… if you want… if you want to read more details, I'd recommend.
**Yordis Prieto** 44:49 Oh, sorry, sorry, okay, okay. Yeah.
**Josh Suereth** 44:52 So, you can read the specification we have right now for our data model, which has, like, our merge algorithm and how detection works, and then this is Dimitri's proposal we're walking through, where there's this notion of ownership.
to handle, like, the fact that… effectively, our process detector, a PID, is not unique, but we kind of want a unique ID, and so we have to do this layering of, like, okay, a PID and a host ID are unique, but the PID by itself isn't. How are we handling that? That's kind of, like, what we're trying to resolve now in the… In the discussions, so… But Daniel, I like this idea. I think maybe… We prototyped this.
**Daniel Dyla (Dynatrace)** 45:39 Yeah, I think it needs prototypes.
I don't think it's all that complex of a mechanism.
**Josh Suereth** 45:48 The only thing I'm worried about is, if we expect users to configure it.
We need to make, like, to your point earlier, we need the default configuration to do the right thing in 99% of the cases, and then allow overrides for people who do special stuff, right?
**Daniel Dyla (Dynatrace)** 46:05 Yeah, well, I think it's not… I think you're not gonna configure… like, a host detector to own different types of entities, because it's, like, more about the… the author of the detector, because it has to modify Like, it's children anyway, so it would have to be… I guess if it's always the same attribute, maybe it doesn't.
Yeah, I think we need prototypes for this, but I don't think it's an overly complex thing.
**Josh Suereth** 46:34 Okay.
Well, let's… let's do that. Dimitri had to drop, so we can, can you talk more?
Can this be merged?
What do we have to find entity scope? Oh, the event… entity event specification.
I'm gonna move on, if that's okay, because I think the next TD is just, the next to-do is just prototyping. So let's work on some prototypes and come back after I get a feel for this. This, I think, we just need someone else from the language sig to approve this, ideally. Like, in my mind, this is approved.
But, yeah, it'd be good if, Someone in this meeting would be willing to… take a look at this and check it over and approve it, just so it's not just two folks from the TC.
**Daniel Dyla (Dynatrace)** 47:30 Can, take a look at it this afternoon.
**Josh Suereth** 47:33 Okay, that'd be awesome, thank you. It's still marked in development, and we're still, you know.
I think there's implementations in the collector here, so we're just trying to catch up, but this is the entity event specification On what relationships look like, how they're going to be modeled, that sort of thing.
Okay.
Cool.
Daniel, when you're done, just ping me, and I'll probably click the merge button then, once we get one more approval in there.
**Daniel Dyla (Dynatrace)** 48:04 Sounds good.
**Josh Suereth** 48:06 Okay, SDK startup, just wanted to check status on this guy. I think we had a bunch of talks, I think you made all the changes already.
Yeah, there'.
**Daniel Dyla (Dynatrace)** 48:17 There's not much other than it's waiting on reviews, and I think you wanted to… I don't know if there's actually any changes you need to make to your prototype to meet this, but I have not changed it To strip out the… like… synchronous requirement.
it wasn't, I think, clear to me at the end of last week whether we decided to strip that requirement or not.
For identifying attributes.
**Josh Suereth** 48:49 Yeah, we were basically saying we want to carve out for… JS.
like, I… again, I… I don't see how… At least for the GCP identifying attributes of today.
I don't know how you're gonna do that synchronously. I don't think you can.
I mean, there's something I want to do that would make it so it's possible, but right now you have to make an HTTP request to get them, so I don't know how you're going to do that synchronously.
**Daniel Dyla (Dynatrace)** 49:19 Yeah.
I… okay, so I'll strip that part out of it. I think the…
**Josh Suereth** 49:25 I think leave it as a should.
Like, I'm fine with that. It's just… it's more… we need a carve out for that scenario, and if you put musts, then, we get into this situation where everyone will tell you no when you have to solve a problem that you can't solve otherwise, right?
**Daniel Dyla (Dynatrace)** 49:46 Right, okay.
Do you think keeping it in as a should is… I mean, if you have to build support in the SDK for asynchronous identity attributes anyways, then… what's the point of keeping that as a should requirement? Is that… because either an attribute is synchronous or it's not.
**Josh Suereth** 50:05 So, so should means, like, only SDKs that cannot do things synchronously would do this. So, like, the idea.
**Daniel Dyla (Dynatrace)** 50:13 Oh, I gotcha.
**Josh Suereth** 50:14 So only, only JavaScript would need to, to solve that problem.
And not all the other SDKs would have to do it synchronously.
**Daniel Dyla (Dynatrace)** 50:23 But I think even in JavaScript, I think we have to do it asynchronously in order to solve the GCP use case, which we do need to solve.
**Josh Suereth** 50:30 Right, well, that's what I'm saying, like, the carve-out is just so JavaScript cannot do it synchronously, but other SDKs can be synchronous, so it's fine today. For them.
**Daniel Dyla (Dynatrace)** 50:39 Yeah, I understand, okay.
**Josh Suereth** 50:41 Yeah, yeah.
**Daniel Dyla (Dynatrace)** 50:41 Yeah.
**Josh Suereth** 50:43 Okay.
Cool. So yeah, I think… I think that's the only… do you want me to make a comment about this?
If you can… Sure, can't.
Allow this to have… These computer requests in.
Entity, identity.
Lookups.
Why don't need this?
Sixers are now broken.
Alright, I'll actually call…
**Daniel Dyla (Dynatrace)** 51:17 The trade-off we discussed last week is the same one. It's like the… like, very specific case of the on-start… processor, which is called synchronously, like, things may not be resolved yet.
And I think that was when we had the discussion about what is actually specified to be accessible.
There, and we had some conversation about that. I think what we found out was that it's not a problem with the spec.
But in JS today, you can't access those things, so we can't just remove them. So it would be a breaking change.
**Josh Suereth** 51:54 No, the spec gives read-only access to all of it.
but it also… the spec doesn't clarify if the read-only access is synchronous or asynchronous.
**Daniel Dyla (Dynatrace)** 52:04 No, the spec of the on start is a writable span, which has access to the API, which you cannot… read, necessarily, from. And then the onEnding is also a writable span, and then the onEnd is a… readables fan, if I remember correctly, and that's where everything needs to be accessible.
**Josh Suereth** 52:29 Yeah.
Yeah, yeah, yeah. You have read access to the resource and the other two, but you don't have read access until here. Until the end. Yep.
Okay.
Cool.
So, I think that's… that's the two things that are in flight. And again, apologies, I had a chance to do some, like.
I got… I didn't have a chance to do anything, like, super useful around entities this past week. I was on call for the TC, so I did mostly security vulnerabilities. Any other status or projects that folks want to talk about?
Cool.
Alright, well, we have, we have some active work here, so, folks, please help us do some prototyping. I think, I'll update the Java prototype to handle this ID context stuff, and make some progress here.
Anyone else who has a prototype, please, you know, help us kind of try to figure and sort this out.
Otherwise, we'll see y'all next week. Thanks!
