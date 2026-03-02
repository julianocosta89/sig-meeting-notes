SIG: Entities SIG
Date: 2026-01-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:07 Hey!
How's it going?
**Dmitrii Anoshin** 01:11 Hi, Josh. Donald, how are you?
**Josh Suereth** 01:14 You know, I'm snowed in.
**Dmitrii Anoshin** 01:17 So what?
**Josh Suereth** 01:18 snowed in. We had, about…
16 inches of snow, and it's kind of still coming.
**Dmitrii Anoshin** 01:25 Oh.
**Josh Suereth** 01:26 Yeah.
**Dmitrii Anoshin** 01:28 I miss snow. I'm from Siberia, originally.
**Josh Suereth** 01:35 California's a big shift. Big shift.
**Dmitrii Anoshin** 01:38 Exactly. Exactly.
No snow anymore.
**Josh Suereth** 01:42 Yeah.
Well, once you guys get snow, I think that's the sign all hell is broken loose, and it's a problem.
**Dmitrii Anoshin** 01:49 Yeah.
Not gonna ask for that.
**Josh Suereth** 01:55 Alright, sorry I'm a bit, delayed from semantic conventions, cool.
So, let's see, we had…
I think I'm gonna put this back on the agenda, and I want to go through our…
project board, but I'm going to put this… feel free to add topics between this and the project board review. I just want to make sure we're making progress and updating status, because we're behind on a few things. Okay.
**Daniel Dyla (Dynatrace)** 02:26 Yeah, it's not really a topic, but I wanted to mention, you know, this is step one on my apology tour for, not working on the prototype for the last month or so.
**Josh Suereth** 02:39 Yeah, I… you're not the only one who has to apologize. I'm,
I had to make some decisions about what was more important in OpenTelemetry, and so I'm focused on getting, federated SEMCOV out the door as quickly as possible. So, that means I'm spending more time on it to get it done quicker, and then I'll be coming back to entities. So, it'll be… I'm thinking it'll be another month.
Before I actually have a lot of dedicated time for entities, to do prototype work. But, like, reviewing and finishing the spec work from the prototypes I already have.
**Daniel Dyla (Dynatrace)** 03:13 I'd like to keep making progress on that, because that's not a lot of wall clock time.
Your excuse is better than mine. I've just been snowboarding a lot, and I've had some internal job things going on that I have just had less time working on OpenTelemetry.
**Josh Suereth** 03:29 So, the first one, I think your excuse is better than mine.
Alright.
**Daniel Dyla (Dynatrace)** 03:37 In any case, I should have time to work on it, really starting this week, to be honest. I should be good to get back into it in earnest, if we decide that it's still important. If we want to refocus our efforts somewhere else, then I have time to spend on that, too.
The message is, I now have time, we just need to decide where is best to spend it.
**Josh Suereth** 04:00 Yep, let's, let's do that. So, let's end the meeting with a bit of a prioritization thing. I wanted to talk about Dimitri's, pull request. Dimitri, do you want to jump in? I'll take notes, and we can,
Here, where's the Zoom?
I'll take notes, and we can, we can discuss,
I'll present. Do you wanna… do you wanna recap? I just wrote my major concern on this, right before the meeting, which, sorry it took me so long to get to, but I'm trying… for context.
We have an internal team that does, resource reporting and resource management, resource updates, resource resolution, metrics from resources, that kind of crap, right?
I have concerns with the overall model, but this goes back to the original proposal, that I think if we're going to start addressing the entity update model, we need to, like, figure out a solution for here.
And I can… I can comment on those, but I think there's a lot here. Anyway…
You want to go into the comments in the order you want to resolve them?
**Dmitrii Anoshin** 05:06 So, yeah, maybe we can speak about Milos first, I don't think we need to spend a lot of time on it. I guess that makes sense to move it to
bigger part of that to SMCON, but I think it's better to do it after we kind of settle on everything, right?
So.
**Josh Suereth** 05:24 Well, yeah, we don't know if these are gonna be events or if they're gonna be a signal, right?
**Dmitrii Anoshin** 05:30 Yeah, that's another thing we want to discuss. I actually… that's gonna be one of the other topics I want to talk about.
**Ted Young** 05:41 Just an FYI, by the way, there's been a big uptick, not just in interest in browser, but, like, mobile in general. So, like, clients in general in OpenTelemetry, and getting the entity stuff sorted out, at least the bits of it.
That those SIGs care about for session management.
That's definitely a thing where, at this point, we're just gonna roll into production with some temporary measure, but…
It would be good to… to get that part.
You know.
**Daniel Dyla (Dynatrace)** 06:21 If I remember last week's meeting correctly, the temporary measure is emitting events for now, right?
**Ted Young** 06:29 Yes, emitting events for session start and end, and maybe just…
**Daniel Dyla (Dynatrace)** 06:35 Session activity or something.
**Ted Young** 06:36 bookkeeping session ID in… in the…
In the red, as a resource, essentially. Still just modeling it there, maybe.
I'm nervous about having the temporary measure be, like, we model it by putting it as an attribute everywhere that feels like too different.
So I feel like we would be better off modeling it as just a rough version of
Where we expect this to land.
**Dmitrii Anoshin** 07:07 Sounds good.
**Ted Young** 07:08 M.
**Dmitrii Anoshin** 07:10 So… Hmm… Josh, maybe… let's talk about your…
your comment first. I wanted to settle, clear that up. Just for me, I'm gonna follow up on this and update the PR,
After that, but for me, like, I'm still confused, how do you want to… I understand the problem, like, the problem definitely makes sense.
I'm just a bit confused about the means, how you want us to address it. So, you are saying that we have an option for the users to not emit update events whenever something is updated, right away, nothing will be sent.
We… the only thing we will be sending is, like, those heartbeat state events, essentially, and whenever something is updated, it's just state updated, and delayed message will be sent after that, right?
**Josh Suereth** 08:06 Right, so this is about expectations of different messages. I'm actually… right now, we have two.
We have the notion that you send the state of an entity, and we have the notion that you send whether an entity was deleted. In state, state is meant to be everything about state, so if an entity doesn't show up, like in a child relationship thing, it means that entity was deleted.
So, if I change the attribute of an entity, I have to report all the relationships.
**Dmitrii Anoshin** 08:32 Hmm.
**Josh Suereth** 08:33 If I have tens of thousands of objects from, like, a Kubernetes cluster, that means I'm reporting tens of thousands of entities in the same thing for just the name changing.
That seems a bit unwieldy to me.
**Dmitrii Anoshin** 08:45 Okay, so you… You want to at least detach the relationships in that case, to…
**Josh Suereth** 08:50 So, so I think there's a few different directions we can go, and we need to brainstorm them. Like, one is, we can actually detach… we could send entity, like, state information, like, here's my set of attributes and configuration about me, separately from relationships.
Or… or we could have, like, we could have a bunch… like, this is, again, goes back to some things we're talking about. We could have a thing that's like, here's the entity state, here's the relationship separate. If I send you the relationships, they're always complete.
**Dmitrii Anoshin** 09:19 And so, if someone gets added or deleted from that, I send you a complete snapshot of that.
**Josh Suereth** 09:24 And I can do that with less, like, overall network hell, I still need to send snapshot events. Like, in all cases, in all of my proposals, there still needs to be a heartbeat that
tells you what the current state is, every once in a while. Like, you need that to resolve, because you will, you know, data will drop.
**Dmitrii Anoshin** 09:45 eventually.
**Josh Suereth** 09:46 might not make it. You need a way to… we're doing, basically, state synchronization here, so we need a way for that to recover at some point. What I'm trying to do is, I actually think, given the scale that I was looking at in our internal systems and things we had to do.
And just for Kubernetes itself, actually, large-scale clusters, I think the current definition won't last.
to those big things. And so, I wanted something that, like, gives us some flexibility here for dealing with that problem.
**Dmitrii Anoshin** 10:14 Okay. But in that case, let's say some pod gets deleted, right?
And, the relationships, of, let's say.
Like, stateful, stateful set to that plot, they all need to be sent, all of the relationships needs to be sent, as well as the delete event of the pod, right?
**Josh Suereth** 10:36 Or we could say, like, we could define the model that you get a delete event for the pod, and you're expected to delete the relationships on your side.
**Dmitrii Anoshin** 10:44 Okay. Because the pod's gone.
Okay.
**Josh Suereth** 10:47 Right? Like, again, we have flexibility in our data model here, so we have to decide how you, like, the way… almost the way I want the spec to be written is, okay, let's pretend you have a big database of all the entities in your system and their relationships, like a GraphQL kind of thing, right?
And I am getting events in that I need to figure out how to modify my state of what's going on.
what actions can I safely do and not safely do, and what actions do I have to do when I get an event? Like, what does it mean on that model?
I… again, I'm approaching this the way we did metrics, where we had the Prometheus data model, and we were like, okay, if you get this metric event, here's what you do in the data model. If you get these metric events, you need to aggregate them, here's what you do, right? But I'm thinking of it like,
We're responsible for getting the data to you, and you're responsible for keeping a database up to date.
How do you interact with our events to keep that thing up to date? What are the things you can and can't do?
you call out a bunch of that in this, and I'm trying to think about…
Let's start decomposing it so I do less on every event, if possible.
**Dmitrii Anoshin** 11:52 Okay. Like, a snapshot event, obviously.
**Josh Suereth** 11:55 I'm gonna have to do a bunch, but, you know…
The other part of what I'm suggesting is, can we make it so snapshot events don't go out all at once? Maybe I send a snapshot every minute, but I can actually batch it into several different requests, so that I don't overload my network with a ginormous request. It's like, you know, a terabyte… well, okay. Let's pretend like your request is several megabytes in size, right?
**Dmitrii Anoshin** 12:19 Yeah.
**Josh Suereth** 12:19 That actually puts a lot of friction on your network just to get it out the door.
**Dmitrii Anoshin** 12:23 Right, but is that a problem of this specification? Like, for example, in the collector, we have an exporter batch and splitting capabilities, right, when you can split the request however you want, based on payload, even payload size.
**Josh Suereth** 12:38 But that's my problem, is right now, I can't split the event, right? Because the way it's defined, if I split the entities up.
that means it's no longer a complete thing, and so it'll cause deletes of entities when I don't want them. Like, I can't split at an entity level.
See what I mean?
**Dmitrii Anoshin** 12:55 Because the relationship's part of the state.
**Josh Suereth** 12:58 Yep.
**Dmitrii Anoshin** 12:59 Okay, yeah, I guess I understand your concern. I'm gonna… I'm gonna detach a relationship from the state. Another thing is that
unclear to me. We still, like… anyway, the snapshot, the state, even if it's supposed to be sent.
on a regular basis, I guess it would make sense to be able to disable it and send update only, for example, so it's gonna be kind of the separate of what you propose, right? It's gonna be still, like… my point is that they should be configurable and controlled by the user, however they want to send them. It can be either only state, let's say, snapshot events with no updates.
or, like, with relationship detached, or it can be only update and delete events, like actions that took place, right? But the payload…
**Josh Suereth** 13:48 We're all three, actually.
**Dmitrii Anoshin** 13:50 All three, exactly. Yeah, all three probably gonna be default, right? And
But I just wanted to clarify that we are not splitting further in terms of we are not introducing event, let's say, kind of patch events. Hey, this, let's say, this field of the description attribute was the only one that changed, because that is gonna be pretty complicated, and we're gonna…
It's gonna be problematic for…
**Josh Suereth** 14:17 I'm fine with that for now. I think we might want to consider… like, let's… let's…
keep prototyping and see if we need that in the future. Like, right now, again, because our… if…
My comment applies to just Kubernetes, and I think that's fine, if we apply to, like, just Kubernetes. But, like, as we start evolving, let's say we start integrating with older systems, like VMware, or even, like, some of the hipstery systems like HashiCore Nomad, right? Or what's the… what's the… Ted, what was the one you worked on?
Cloud something, or…
**Ted Young** 14:51 Cloud Foundry?
**Josh Suereth** 14:52 Cloud Foundry, yeah, let's pretend like we're integrating with Cloud Foundry, right? Is it possible that, like, they don't provide a watch API like Kubernetes, where we get everything at once, and they literally just tell us about one thing going?
one attribute at a time. You know, if we find that, again, this is what we found with, like, the metrics API. We went for one that could represent
The common ways that these things are expressed, which is actually, a bit broader than maybe what we really, really, really wanted for, like, simple implementation.
So it's possible that we find out, cool, Kubernetes works like X, and we handle Kubernetes just fine, and then we hit one of these other systems that has, like, a registry of entities we need, and we need some additional capabilities.
We can add them to the model later.
But I just want to warn you that, like, that might happen. Like, we might not be able to hold that…
line. I think we can for now, and see how everything goes, but I'd rather not… what I consider a failure scenario, is if we have instrumentation where I can listen to a, a watcher.
on resources from the management API, get those watch events, translate them into OTLP, and fire them on.
That's like… that's like an ideal for me, you know? And I… I don't have to do a ton of state tracking locally.
Maybe I do relationship tracking, because I need to, because the system doesn't do it for me. Cool. But, like, we want that to be relatively minimal.
**Dmitrii Anoshin** 16:23 Because otherwise, the instrumentation gets really hard to write.
Okay, I understand. I'll… that's clear… that's clear to me. I'll… I'll keep that in mind as a potential point for extension, as potential capability that we might want to have.
**Josh Suereth** 16:40 to be clear, I don't think, like, from a Google perspective, I don't know if we need it. I don't think we do. I think what you have is fine. I'm just saying, from an OpenTelemetry standpoint, like, these are things we need to look at the things we're gonna integrate with and where we're gonna get data.
And it's possible we need to add something like that. So, let's not… let's hold the line, but I don't think it's a hard line.
**Dmitrii Anoshin** 17:02 Okay. Yeah, I understand your point. It's like, if, for example, API provides only delta metrics, right? We provide OpenTelemetry a way to emit deltas as well. Otherwise, we would have to keep the state for all of the time series internally.
**Josh Suereth** 17:16 Yep.
**Dmitrii Anoshin** 17:17 Okay.
**Josh Suereth** 17:18 Cool.
**Dmitrii Anoshin** 17:19 Makes sense. Thank you.
**Josh Suereth** 17:22 Yeah, otherwise, I do think this is a great first start, so I,
Yeah, cool. Let's move on, unless other folks… did anyone else have anything they wanted to add?
Okay.
I'm gonna briefly talk about the merge algorithm.
PR. I did… I think I made updates to this. I will apologize, between December
I went… I went out of the country for, like, 3 weeks, and when I got back, my laptop was completely dead. And so I had to reboot my laptop, and it took me a while to get my specification VRs working again. Because for some reason, installing Make and all the stupid things we use is against the security policy in… now.
So I had to get creative and docker everything. So, yay.
Long story short, I think this is updated now. Does anyone have any remaining comments on this merge algorithm here? I'd like… like, we have no approvals on this, so I wanted to see what is left
from the SIG to resolve before we, like, push it in the spec.
I think… I was trying to be cute with, using E prime here.
And trying to keep my algorithms not, in any known language, because everyone complains if my language looks too much like Rust or too much like Java or something.
So I tried to specifically make it not a language at all that people would recognize. I don't know if that was good or terrible, but I got no comments about chosen language on this one.
**Daniel Dyla (Dynatrace)** 19:17 Seems fine to me, I just think it's…
Sometimes, when we go to the larger group, it may be unclear
I mean, it is… it's clear if you read the whole thing, but if you're just skimming it, it might not be clear which one is, like, incoming and which one is out, like, is the pre-existing one.
**Josh Suereth** 19:38 Oh, okay. So I could… honestly, instead of calling it E and E prime, just calling it, like, current and previous.
**Daniel Dyla (Dynatrace)** 19:44 Yeah, I think that might be easier, because, you know, we do get a lot of people that just kind of skim through.
**Josh Suereth** 19:51 Yeah, that's fine, I can do that.
I think this was the other one that had more comments,
This is about how we build resources from entities.
And I think we had to…
Yeah.
They wanted to have a dropped count, for, like, when we drop entities from merge conflicts.
And I'm… I was gonna do that as a follow-up thing, because I think that needs to be in this SDK specification, not the data model specification.
**Daniel Dyla (Dynatrace)** 20:31 Where… is that, does that match, like, the previous dropped attributes count and that kind of stuff?
**Josh Suereth** 20:37 That's… that's supposed to be the idea, yeah, so if…
when you merge entities, you end up dropping data that we would fill out a dropped X count, and then we need to make a proto-update for that, we need to make prototypes for it, yeah. I think it's all reasonable to do, I just wanted to, start actually getting some of these implementations in without it, initially.
Because again, the dropped X counts, I think we added some of them later, and I think we can add them later, so I'd like to kind of get…
get to the point where people are using this, and we get confirmation that we really need that before I add it. Like, is just logging the fact that there was a conflict not enough? You know?
**Daniel Dyla (Dynatrace)** 21:17 Right.
**Josh Suereth** 21:21 Let's see, what else was there? There was resource check… that was the thing there. Oh, and then we talk at the bottom about how we have to do resource flattening issues.
and…
This was the one thing we talked about before. Basically, if there's a conflict where two entities use the same attribute key, but both have the same value, then I'm saying nothing's needed, and I think, Dimitri, you wanted this to be a failure.
**Daniel Dyla (Dynatrace)** 21:50 I think…
**Dmitrii Anoshin** 21:51 Alright, yes.
**Josh Suereth** 21:52 Yeah.
**Daniel Dyla (Dynatrace)** 21:54 Yeah, I… I think it's… it opens up the ca- like, like,
possible problems, where, say, you detect two entities during initial detection, they share an attribute, the value's the same, fine, you move on. And then later on, you update one of them, and it becomes a failure, like, that's potentially super confusing.
**Josh Suereth** 22:19 Yes.
**Dmitrii Anoshin** 22:20 But we should not allow that, and, like, if you want to update and to… and assign one entity and conflicting attribute, that shouldn't be allowed. Because it's gonna be… we discussed that, and the problem is that the ownership of the…
attribute gonna be lost. And in the processing pipeline, dealing with figuring out which entity owner of a particular attribute based on the OTLP model is gonna be just…
**Josh Suereth** 22:51 Okay.
**Dmitrii Anoshin** 22:52 Super complicated, you know, We… we need additional…
Points to the data in that case.
**Josh Suereth** 22:59 Are we okay with just these two things, then? So basically, if there's a conflict of two entities in the same attribute key, if one of them has it on description, you just drop it from the descriptive keys.
Right? Because the other entity, it's its identity. And so we allow that, where you could… if somebody creates an entity where they say, hey, I have a descriptive key, but it's the identity of another entity, we're like, okay, cool. This entity was describing that entity, that's like shenanigans because we don't have a signal about relationship, we can drop the description.
**Daniel Dyla (Dynatrace)** 23:26 So the difference between ID and description overrides the priority set, is what you're saying?
**Josh Suereth** 23:33 Yeah.
In this case, in this case, what we're assuming, like, this failure is assuming, this is why I wrote this, right? Is, like, cool, people might have descriptive attribute sets of, like, they might, add in, you know,
something like process ID might be dis… descriptive on a service.
entity for some reason, because people are following things and just adding descriptive attributes willy-nilly. But if you have both the process and the service entity together, it's identifying for one, scripted for the other.
there's no loss of context if I get rid of the descriptive thing here.
you know, basically by putting them together in resource, I'm describing
the service in some way, or I'm creating that, like, you know.
**Daniel Dyla (Dynatrace)** 24:25 This is… as opposed to just dropping the entity entirely. It's…
**Josh Suereth** 24:31 Otherwise.
**Daniel Dyla (Dynatrace)** 24:32 Preserve as much as possible.
**Josh Suereth** 24:34 Exactly. This is… this is that idea of trying to preserve as much as possible where we can, and deal with the fact that people are doing things with resource, and when we switch to resource detection to be entity-based, I want to try not to have entities never show up because of weird conflicts.
If you want, I could totally, like, I could see, I can see…
Dropping just this rule and being fined.
But I did want to check, do I need to drop this one as well? Because basically, we can just say, if there's ever a conflict where two entities use the same attribute key, and both use the attribute key… well, this is… and both use for attribute identity, I could get rid of that. Then you just remove the lower priority entity from resource. Like, the end. We could say that, and be done.
I would like to keep this, because I think that it gives… like, I don't think it breaks the entity data model, and I think when it happens, it's accidental, not like a… and I don't think we lose, a lot by having this as a rule.
**Daniel Dyla (Dynatrace)** 25:30 Yeah, and I assume… I think you're probably working under the same assumption, that in semantic conventions, we would make this a rule, like, where when you define, you know, ownership must be clear, we wouldn't share keys.
**Josh Suereth** 25:46 No, no, and we can have an actual policy that prevents that, too.
**Daniel Dyla (Dynatrace)** 25:50 So this is just preventing…
Like, users who tack on a bunch of keys because they feel like it might be a good idea.
**Josh Suereth** 25:58 Yes, yes, I imagine that will happen more frequently than, than not.
**Daniel Dyla (Dynatrace)** 26:06 Yeah, we already see it with resource, so I think it's safe to expect it to happen.
**Josh Suereth** 26:11 Yeah, I don't know if you get this from your users as well, but then they're like, hey.
Why is my data so expensive? Because I have all of these resource attributes.
That I… that are costing me money in the size of what I write. And then they're like, hey, why is everything so slow?
When they, yeah, it's… it's been exciting.
But then if you ask to remove any particular attribute, they, yeah, they won't.
No, we need that. Okay, cool.
Do you need it everywhere?
**Daniel Dyla (Dynatrace)** 26:46 Yeah.
Always a balance.
**Josh Suereth** 26:49 Yeah.
So, hopefully we get a better balance. Anyway, random rant. So…
we're okay keeping this. Anyone have concerns keeping this? Like, I… again, I'd be fine removing it
Because I think…
If we're… if we're being very, very cautious, removing this, I think, will be fine, it's just there will be some instances where we could have had entities and we don't.
**Daniel Dyla (Dynatrace)** 27:24 So, wait, when you say removing it, you're saying remove that bullet point from the list here, or you're saying remove the attribute?
**Josh Suereth** 27:31 Oh, no, I'm… remove the bullet point from the list, yeah. I'm planning to remove this… this bullet point from the list.
The question is, do I remove this one or not?
Because I could remove this bullet point and update this one to just be anytime there's a conflict whatsoever.
We just remove the lower priority entity.
Anytime.
And I'm fine with that going forward, if that's the way we want to go.
**Daniel Dyla (Dynatrace)** 27:57 I think while it is removing the lower priority entity.
is in some ways worse, because if something is identifying, then it's, like, a much stronger signal. I think…
It's more confusing if you have something that sometimes overrides the priority order.
I think if you just have… this is the order of the priority, and then, you know, if users are saying, like, why is the fourth item overriding the second item, you know, it may not be immediately clear to them why that's happening.
**Josh Suereth** 28:35 Okay.
**Daniel Dyla (Dynatrace)** 28:36 Hi, so… Yeah. Well, it may technically result in, you know.
a worse data some of the time. I think we're working on edge cases here, and we want to prioritize, like, the debugability. Like, why… why did this happen? Because…
We want to focus on… ideally, they update their configuration and stop it from happening in the future.
So helping them to do that as easily as possible, I think is more important than allowing them to continue to emit, like.
Partially correct data forever.
**Josh Suereth** 29:16 Yeah, this will actually make the implementation easier, less if else checks.
**Ted Young** 29:21 I have to run, but I'll add, we have a database called Knowledge Graph at Grafana Labs that's kind of, like, where I think a lot of this stuff will live. I'll try to get some people from that team to review these two, just to see if they have any feels from their perspective.
**Josh Suereth** 29:39 Please do. When I think knowledge graph, I keep thinking Google search, but it's basically, this is the knowledge graph of, like, your infrastructure. Yeah.
**Ted Young** 29:49 Yeah, very… it's just… it's very similar to what we're doing here, so… Yep. …might have some lived experience.
**Josh Suereth** 29:55 Yes.
**Ted Young** 29:56 Getting folks who work on these systems would be amazing, because again, that's the team we need to interact with the most.
**Josh Suereth** 30:03 in the V2, like, the relationship part of this, so… Right. Yeah, yeah.
**Ted Young** 30:09 Okay.
**Josh Suereth** 30:10 Cool. I gotta run.
**Ted Young** 30:11 Thank you.
**Josh Suereth** 30:13 Alright.
Alright, so… update and push. Cool, I'll update and push that later today, and then I'll ping the chat. I'd like to… I'd like to try to get,
some check marks on that quickly, so we can get that through. I've had to mark it not stale several times.
But then, we, you know…
The next step is getting prototypes of this. Actually, I'm not showing what I'm presenting. Okay.
Let's get back to our project board and see what we can do for next steps.
Because we have… we have a couple things in motion, and we list ourselves as at risk, but we need to do that.
Need to update our timelines and stuff, because we kind of…
didn't meet them, and that's fine. I just want to try to get a better view of what we're doing.
Okay, so let's take a look at in progress, right? We have add support for new resource entity references proto-Message in the collector.
How is this all going, Dimitri?
**Dmitrii Anoshin** 31:17 Are you sharing the screen?
**Josh Suereth** 31:20 Oh.
Did… it just… it crashed.
when I… okay, cool.
Great, thanks.
it… When I clicked share this screen, it just crashed my sharing. Apologies.
Alright, is this working?
**Dmitrii Anoshin** 31:38 Yeah, now I see it.
**Josh Suereth** 31:40 Yeah.
**Dmitrii Anoshin** 31:41 So… And… It's a… it's a collector, yeah, I'm,
I've not made a lot of progress on this one, unfortunately, but I'm gonna… I'll have more time, given that, like, the DVR that we work on for the relationships and entity brings more clarity, and now I'm more unblocked than before, so I can proceed working on this.
**Josh Suereth** 32:08 Awesome.
I just want to make sure if we start sending entity refs to the collector from SDKs, we're not, like…
I think you have the key things we need, like, the debug exporter will show them.
Right? They're NP data.
**Dmitrii Anoshin** 32:23 Yep.
**Josh Suereth** 32:24 So… We'll be able to do, like, a modicum of testing with them.
**Dmitrii Anoshin** 32:29 Right.
Yep. Passing them through is not a problem.
**Josh Suereth** 32:34 Yeah, the transfer… this seems to be the big, hard one here, right?
**Dmitrii Anoshin** 32:39 Beh, yes.
And, I mean, I mean, like…
there are… I see a couple, let's say, interfaces. This maybe we can discuss a little bit. So, I see…
a couple of interfaces that we can provide. First of all is, like, just low-level protobuf definition kind of interface. You can just remove the reference, and you'll get invalid entity. But I don't think that's something that users really need.
So they actually need to interface over entities, like, not entity references, but over entities. Yep. That one will probably… will take precedence over manipulation, over resource attributes, right? So it will be in conflict. And,
like, will it be part of the transform processor? Or will it be maybe some additional processor? And so, like, let's keep it clear. Because transform processor, currently, it's more like low-level interface for all of the other signals. You can mess up with the data however you want.
So, like, let's say… Naturally, it would be…
better to add low-level interface for the entity refs as well.
Because it's, like, it's just over, like, transformational protobuaff, essentially.
But it's gonna be disruptive, right, for the end user. It's gonna be more complicated to change something meaningful, in a meaningful way. So…
I mean, I see two options. We either…
Like, add low level or don't add to transform processor, doesn't matter, and we have another processor to manipulate entities.
Or, we only add an interface to manipulate entities, like higher-level interface to the transform processor.
What's your… I, thinking about it.
**Josh Suereth** 34:39 My thinking so far has been… it's the same thing I want to do for the API and SDK, is we only provide a high level. Okay.
and we hide the fact that we have this reference crap behind it. In the collector, what this would mean, so, for context, we've been doing lots of arguments about P data for profiling SIG.
Profiling SIG is using a dictionary lookup.
for strings, from resources and from attributes, and my… I'll tell you what I recommended to Bogdan, which he did not like, and I kind of understand, maybe it's… this is hard and go, but I would create a new struct.
For entity and resource in PData. So in that struct in PData would have resource B a array of entities.
And then, the raw string key value array.
And, the entity would be, like, resource entity or something. It would have the type, the attributes and stuff in it.
And then, when I serialize that PData resource, I would have a way to erase the entities and turn it all back. Like, that's where I would do my flatten, that's where I would do all that, in the thing that writes the…
protocol buffer code from there, but the P data interface would be the high-level entity interface we want on resource.
**Dmitrii Anoshin** 36:05 I actually added that already. There is high-level interface for entities and P data. There is low level and high level.
I just…
**Josh Suereth** 36:12 Okay.
**Dmitrii Anoshin** 36:13 don't, don't know what to use, going forward. So I was, I, I, I, I'm.
**Josh Suereth** 36:20 I would… I would get rid of the low-level.
**Dmitrii Anoshin** 36:22 Yes, yes.
**Josh Suereth** 36:23 Any code except things that go to… directly to protocol. Yeah.
**Dmitrii Anoshin** 36:26 It doesn't change the data structure under the hood. Under the hood is still entity references, but this high-level interface, I guess it's prefer… I think it's preferable as well, and potentially we can just remove the low level, it's not a problem at all, because it's an experimental API right now, we can remove it if needed. Okay, and that's…
**Josh Suereth** 36:46 I want to check with Bogdan. He was telling me, are you actually using an interface, or are these structures?
Because he was saying that.
**Dmitrii Anoshin** 36:53 Me neither.
**Josh Suereth** 36:53 Trying to avoid all.
**Dmitrii Anoshin** 36:54 Nothing like Go interfaces. By interface, I mean.
**Josh Suereth** 36:57 Oh, oh, gotcha, gotcha. Okay, good, good, good.
**Dmitrii Anoshin** 37:00 actual new structures, but which reuse existing protobuf messages under the hood.
**Josh Suereth** 37:08 Cool.
**Dmitrii Anoshin** 37:09 Okay. Okay, in that case, I think it's clear. Let's remove that. In that case, there is no, like, even…
An option for the components to, like, mess up with entities in any way in that case.
And it answers the question, what interface we provide for the transform processor.
Okay, I'm on board to you. I just… I actually wanted to clarify that for some time, yeah. Thank you.
**Josh Suereth** 37:33 Awesome.
**Dmitrii Anoshin** 37:34 But it doesn't… it doesn't… I don't think it conflicts with your discussion with Bogdan about dictionaries. That one is a bit different, and it's like, whether you put that into Protobuff or not, it's not about PData. PData interface for entities is, like, separate, right?
**Josh Suereth** 37:51 Yeah, but it's… it's a… you did the abstraction that I want Bogdan to do for profiling.
Already, apparently. Like, I want a struct that is, called, like, resource, that has,
Where it will have a dictionary in it, right? Or it'll be able to reference a dictionary.
**Dmitrii Anoshin** 38:12 Yeah, that's it.
**Josh Suereth** 38:13 And everything in OTLP pulls in that struct that is resource-capable, but there are two different protocol buffer messages where that same struct can serialize to both the resource profile and regular resource, or profile resource and regular resource. That's what I wanted.
Right, so in P data, there's one interface, but there's actually two different protocol buffer messages it can serialize into, depending on whether you're in the profound signal or not. Because I think this would… anyway, that's… we can talk about that, that's a different SIG, but yeah.
**Dmitrii Anoshin** 38:46 Yeah, it's, like, there's some common things in that, but it's not, like.
**Josh Suereth** 38:52 No.
**Dmitrii Anoshin** 38:52 Rend onto each other.
**Josh Suereth** 38:54 Yeah, similar, but we have a much easier problem, I hope.
**Dmitrii Anoshin** 38:56 Yeah, okay, but in my interface, it's like, there is a resource struct, and there is experimental function, which takes resource and gives you entity, entities, list, entity slice, or resource entities, whatever. And then, through that interface, you have everything that we discussed.
But at the same time, just another thing to clarify, for users, it's still entity attributes still available, and they can mess up with the entities in that case, like, in some kind of way. So…
like, additionally, I would think maybe, like, I don't know, providing some kind of…
like, some kind of API that would clean up the state, or something. By cleaning up the state, it would check if some, like, let's say, identifying attributes got corrupted, entity gets removed.
**Josh Suereth** 39:51 Yeah, like a sanitized method or something.
**Dmitrii Anoshin** 39:54 sanitize, yeah, sanitize entity to something like that, right? And it would, I don't know, maybe potentially just mutate the resource, and gives you an error if something gets removed, or how would you imagine that to work?
**Josh Suereth** 40:09 So, in the SDKs, I think this is in the merge method, or, like, if you think of resource, where we're gonna have, like, an add entity call.
Right? So if I take an existing resource and I merge in another one, I'm taking the entity sets and merging them, and that's where I should detect errors and issue the problem. That's why we're focused on that merge algorithm, when to have errors. From your standpoint, I can see it, like, cool, I change an entity and I want to add something to it, right?
**Dmitrii Anoshin** 40:37 In an immutable world, that would be cool. I add something to that entity, and I re-merge the resource.
**Josh Suereth** 40:43 So, you almost need to, like, on mutation of entity, revalidate that the merged resource is appropriate.
**Dmitrii Anoshin** 40:50 But it's not even related to the merge. Like, if you, let's say, call this, get, give me entity from the resource.
**Josh Suereth** 40:58 Yeah.
**Dmitrii Anoshin** 40:58 source already can be corrupted by some other processors in the pipeline, which, like, removed or changed the identifying attribute or something, right? So, in that case.
what would be… maybe that API that takes resource from… entities from the resource that mutates the resource, I don't know, like, maybe… I would like to make it explicit. So…
**Josh Suereth** 41:22 So there's an explicit, like, our entity sane method.
**Dmitrii Anoshin** 41:25 Maybe, maybe that API that returns entities, like, high-level entities, struct over the resource, that would error if the… if the…
resource is broken, and then you can have an additional function that would sanitize it. So you would sanitize, and then you do that conversion again, something like that.
**Josh Suereth** 41:49 to me, that makes the most amount of sense, right? Like, if I'm gonna interact with them, I have to make sure they're clean, and if they're not, I can have some sort of way to know that they're not clean.
**Dmitrii Anoshin** 41:58 Okay, cool.
**Josh Suereth** 41:59 I like that.
**Dmitrii Anoshin** 42:00 Thank you.
**Josh Suereth** 42:01 Okay, cool. This was related to the Go…
Go implementation, I don't think there's progress on this.
Sdk startup specification.
Do we still need this? I think this is assigned to Daniel.
**Daniel Dyla (Dynatrace)** 42:20 Yeah, I… I honestly don't know, I…
off the top of my head, how much is already, like, specified and how much is not, but I mean, we're… I don't think we have much SDK specification at all, and we will certainly need to define startup.
I think it should be very straightforward with the merge algorithm and rules that we have, you know, and between that and the configuration, which we will, I assume, go through the declarative config.
I think it should be very straightforward. There shouldn't be any, like, big… Bye.
I don't know, big questions. If there are, I think the other stuff is… is… Not ready.
**Josh Suereth** 43:06 Okay.
Do you, are you prepared to write this specification, or do we need to do more prototyping work, you think?
**Daniel Dyla (Dynatrace)** 43:14 No, I think I'm prepared to do it. I could probably work on that this week.
**Josh Suereth** 43:18 I'll leave it here, because it could be one of these other things is high priority. Develop strategy for asynchronous resources and entities. This is from the JS SIG. Do we have a strategy yet? We had kind of briefly talked about it. Not brief… sorry, we talked about it in depth, but I don't know if we actually wrote anything down of what we were going to do.
**Daniel Dyla (Dynatrace)** 43:37 Yeah, I guess the… the question that we ended on is whether or not it's okay to have asynchronously resolving attributes. I think what we agreed on is, like, ID needs to be synchronous, and description could be asynchronous.
I guess this also would have been related to the discussion we just had about, attributes conflicting with each other, because if you have an asynchronous one, you don't even know if it will be conflicting or not, so that is…
Resolved if we just say priority order wins, also, because then we don't need to know the result of the value in order to do it.
Right.
**Josh Suereth** 44:20 Well, the other thing I think was, it's okay if the ID is asynchronously resolved…
If the key is not…
**Daniel Dyla (Dynatrace)** 44:31 Yeah, all keys have to be known in advance, but I think we said identifying…
attributes must be synchronous. Maybe I don't… maybe, maybe I'm just remembering that.
**Josh Suereth** 44:43 We said that, but I don't know if that's actually true in practice. Like, I think there are…
**Daniel Dyla (Dynatrace)** 44:48 Certainly the keys have to be synchronous.
**Josh Suereth** 44:51 Yeah, he's graphing asynchronous, yeah.
**Daniel Dyla (Dynatrace)** 44:53 Yeah. We have to know the keys in advance, I think even identifying values there's no…
problem to them being asynchronous, because they're always resolved before the first report anyways.
**Josh Suereth** 45:11 Yeah, I think it just makes your implementation awkward, where, like.
You could identify that two entities have the same… are the same type.
and then have, like, a complicated async thing that says, cool, I have two entities of the same type. I'm gonna, like, partially merge them, but if the ID that this one resolves to is different than that one, then I drop all of it. Otherwise, I keep it. Yeah.
**Daniel Dyla (Dynatrace)** 45:33 Yeah.
**Josh Suereth** 45:33 kind of crap.
**Daniel Dyla (Dynatrace)** 45:34 Yeah, so determining whether two entities are the same when they're separately detected.
Yeah, I mean, ideally, I would like the keys to be synchronous,
Since we haven't done really any semantic conventions work, it's hard to say whether that will actually be the case in practice.
**Josh Suereth** 45:54 We… we actually have started a lot of semantic interventions work, so here, let me,
I should say, we've hijacked all the semantic conventions work around entities.
**Daniel Dyla (Dynatrace)** 46:03 Yeah, from resource, yeah.
**Josh Suereth** 46:06 it's giving us good insight. So, if we look at, the registry.
I think this works now.
You can see all the different things, right?
**Daniel Dyla (Dynatrace)** 46:19 F.
I mean, it's gonna be the… it's not gonna be surprising which ones are a problem. It's the same ones that are already a problem with resource, which is, like, the FAS function ID is not available, like, at startup time until you get a first request.
**Josh Suereth** 46:41 This fast instance one, or the FAST name?
**Daniel Dyla (Dynatrace)** 46:44 Yeah, I think it's the FAS instance.
**Josh Suereth** 46:49 Okay, those… those haven't gone through things, but the one… the one I know from GCP, I'm pretty sure this…
Cloud Run might be okay. That… we… oh, we haven't updated these, huh?
Cloud Run might be okay, but I think some of the other ones, if you're in Node.js, would be problematic, because they require a network hit. Like, the Kubernetes stuff from GCP,
If you need any of these, like, what deployment you're a part of, you're screwed.
**Daniel Dyla (Dynatrace)** 47:19 Yeah, but entities… Can be resolved
after startup, so that… I guess it would just be, we only need the IDs to be synchronous on, like, the startup entities.
Because anything that's resolved after startup follows the,
you know, we don't have to resolve the whole entity until the ID is resolved.
**Josh Suereth** 47:48 Right, but the…
What I'm saying is that the ID might still be asynchronous. I know in here it is as well.
This one… did this one get IDs? No, but this, that's the wrong thing.
That's not what we want.
We wanted… where's GCP? GCP GCE. There we go.
Where did GCP GCE go? Did it disappear?
Here it is.
It looks like my links are bad. That should go to this, what's the link for that?
GCP-GCE, that's what it… why didn't it go down? Anyway, whatever. This, this, this right here,
One of these you have to hit the metadata server for.
Perfect, that one's fine, that one's fine. Oh, I know what's… I know what it is, it's, it's frickin' CloudID.
That's what it was. This thing. Cloud account ID, and then Cloud Resource ID.
this dealy deal.
getting the full resource name on GCP, if they are using this, that is always a network hit, or almost always a network hit on GCP. You have to hit our metadata server.
**Daniel Dyla (Dynatrace)** 49:08 Gotcha. Okay.
**Josh Suereth** 49:12 So… and that… that people do grab this in Cloud Run?
**Daniel Dyla (Dynatrace)** 49:19 Yeah, so I think… It's still… not a problem.
For the values to be…
asynchronous, as long as, like, you just don't run the merge algorithm until after everything resolves, which is… you wait to export, you wait for everything to resolve.
And then you run the merge algorithm at resolution time, rather than running it.
**Josh Suereth** 49:53 Yeah.
**Daniel Dyla (Dynatrace)** 49:54 Each time a new entity is added.
It then… Would mean you don't know whether there's an error until… Resolution time, either.
But as long as we're just logging the error, and it's not something that, you know, the user needs to know right away, it's not like a throw-catch situation, then maybe that's fine.
**Josh Suereth** 50:19 That's… that's my thing. That's kind of the approach we took for other failures in the SDK. The other thing is, when we prototyped the crazy-ass resource manager thing in Java, where I was doing asynchronous startup.
That actually worked out pretty well, honestly, where, like, you defer resolving the full resource until the first export, you do the merge algorithm right before it, error messages weren't too bad. There was a bit of shenanigans where, like, you needed to make sure that you didn't get yourself into an inconsistent state that got exported.
But I think that's easier in JavaScript, because you have async concurrency, but not, like, thread hell.
**Daniel Dyla (Dynatrace)** 50:57 Yeah, you don't have to worry about any, like, thread safety, I mean, essentially.
**Josh Suereth** 51:03 Until you yield to the runtime, everything you're doing is… is…
**Daniel Dyla (Dynatrace)** 51:08 basically safe.
**Josh Suereth** 51:10 Yeah.
Yeah, so I think, I think it's a bit easier for you there, but, like, yeah, I, I.
**Daniel Dyla (Dynatrace)** 51:17 The biggest caveat, and we already have it with resource, is that, like,
processors, like span processor, can't, you know, access those values until they're resolved, and then if we haven't even run the merge yet, like, that might be weird on, like, the first span that's emitted, having, like, weird asynchronous data. Yeah.
And also in… Metrics. I mean, we essentially can't have any asynchronous,
Like, anything that affects metric identity can't really be asynchronous.
**Josh Suereth** 51:56 Right, but I think the difference is, and this should be true.
From a metric standpoint, you should refer, like.
I know that I'm referring to a resource. I don't know what that resource is, because I have no control over it, right?
**Daniel Dyla (Dynatrace)** 52:10 Yeah, you just use.
**Josh Suereth** 52:11 Whatever it results to, I'm referring to, and it shouldn't change my identity, because it's that resource's identity. Where this gets interesting is the multi-resource tenancy thing we have, where you can say, with entity.
But again, like, if you just have a, cool, resource 1 is this one, when someone comes with entity, they're now resource 2. Whatever that resolves to is their identity, but you haven't resolved it yet, that's fine.
Right? Because you're attached to that as your identity.
**Daniel Dyla (Dynatrace)** 52:36 Yeah, and that's what we're doing, yeah, that's what we're doing in several places, is we just use the, like, object identity, and then, you know, if it's the same, then great. If it's not, they might end up being the same, but the… that gets resolved further down the line. You just might export it.
During export time, you have two, like, entries in the list that resolve to the same thing, and then you just resolve that on the server as if it was two separate exports, and you call it a day.
**Josh Suereth** 53:07 Yeah.
Yeah.
Okay, so I think when… as you work on the prototype, this should probably get fleshed out more.
Do you… that's the strategy. Do you think,
How do you want this to show up in the spec?
would this show up in the data model, or this shows up in the SDK spec for how to deal with asynchronous stuff?
**Daniel Dyla (Dynatrace)** 53:33 I think it'd be in the SDK spec.
**Josh Suereth** 53:36 Okay.
**Daniel Dyla (Dynatrace)** 53:37 And I…
Yeah, I don't even know how much this will affect other languages. I don't know if there's other languages that have the same type of problem where they can't really…
block. I mean, there's definitely other situations where you don't want to block.
**Josh Suereth** 53:53 Yeah, sure.
**Daniel Dyla (Dynatrace)** 53:54 Maybe it's useful in other languages for that reason.
**Josh Suereth** 53:59 I know PHP is weird, because I learned that when I did the due diligence for their auto instrumentation, but I don't remember the specifics. They might be in a similar place, but maybe not as hard.
And I think they just added a threading model.
**Daniel Dyla (Dynatrace)** 54:15 Okay.
**Josh Suereth** 54:16 Did you know PHP is evolving and releasing new versions? It's pretty impressive.
**Daniel Dyla (Dynatrace)** 54:20 Every 2 or 3 years, somebody tells me that, and it surprises me all over again.
**Josh Suereth** 54:26 It's, I think it's awesome, man. That's longevity in its finest, right? That's, anyway, cool.
So, that was, that was our in-progress things. We have resource entity mapping, entity manager OTEP. Real quick, the entity manager OTEP that, that, for browser and session and things,
I do think that I'd love… we'll have to talk to Tet. I'd love if somehow they could do a bit more heavy lifting on some of that. We do have that OTEP that's out around, multi-tenancy and entity.
Yeah. It's still… I mean, I think we approved it, but I don't think it's approved.
**Daniel Dyla (Dynatrace)** 55:06 Yeah, we didn't really get feedback from them, and since they're the only ones we know right now that absolutely need it, it would be a real bummer to release it and then have them say it doesn't work for them.
**Josh Suereth** 55:19 Yeah, and we, we did prototypes of it, I think… Come on. You can load. Do you see what I'm presenting now, this thing here?
**Daniel Dyla (Dynatrace)** 55:27 Yeah, I see you.
**Josh Suereth** 55:29 Okay, yeah, it has… it does… but it doesn't have approval from this SIG either, so I think we should probably fix that. So folks could take a look at this. As far as I know, this resolves all of our comments and concerns.
I removed Stale 2 weeks ago.
David wrote a Go prototype for it, too, so it has prototypes in two languages now.
And one of them's go, which is…
you know, pretty good. I really don't think there's a lot
in here, and I really like what you did, Daniel, with the,
the way you did the SDK spec.
Short, sweet, to the point, you know.
where was that? Right here? No.
Yeah.
like… Daniel was able to do a, prototyping spec, and…
the… the only thing he had was basically, like, we should move this from the SDK spec to the API provider spec, and then put some sort of close or shutdown on there.
I'm fine doing that, I'd have to prototype that in JavaScript, but we can also do that when we make this a real spec. I mean, I think for a…
For OTEP, this is fine.
**Daniel Dyla (Dynatrace)** 56:54 Yeah, okay.
**Josh Suereth** 56:55 So, if you wouldn't mind, stamping your approval, if you agree with it, we can push on this in the spec sig, and then get the browser folks to actually pay attention to it.
**Daniel Dyla (Dynatrace)** 57:06 Yep, I join the browser meeting every week, so I can… I can toot the horn this Thursday on it also.
**Josh Suereth** 57:14 Please do, because it'd be like, look, at this point, you know, if you want this to move faster, we have a proposal, we have some prototypes, we're happy with what it looks like, we just want to make sure it works for you, like…
**Daniel Dyla (Dynatrace)** 57:23 Yeah. Jesus.
**Josh Suereth** 57:25 prototype, try it out, help us drive this into the spec. Otherwise, I think it's gonna languish.
**Daniel Dyla (Dynatrace)** 57:31 Okay.
**Josh Suereth** 57:32 Cool, but we have… we have all these things here that we gotta sort out for that.
And then we have the things to finish… oh, yeah, define entity merge algorithm for the OTEP. Let me put this in in progress.
Support my schema files. Schema files are changing dramatically, by the way. Did you… I don't know if you saw that there's an OTEP around this. This might become non-work.
With the new OTEP, we're getting rid of schema files the way they exist, where they're just diffs, and going towards definitions only.
And in the definition, there'll be, like, a… this thing is deprecated, here's what it previously was, so all your rename rules will actually be implicit.
**Daniel Dyla (Dynatrace)** 58:14 Not this thing is deprecated, this thing is not deprecated, here's the previous deprecated one.
**Josh Suereth** 58:19 No, it'll be, here's the thing, here's the thing that's deprecated, here's the new one. And so if you encounter something that's one of the previous things, you can move it to the new thing.
**Daniel Dyla (Dynatrace)** 58:28 Got it, okay.
**Josh Suereth** 58:29 Collector process, differentiate remote versus local, that's still TBD.
And then we have to communicate this change to resource. That's the last…
So, I think we need a bunch more tasks around… I really want to start getting the SDK implementations out the door. Like, the spec work and the SDK implementations to get these out. That's, like, one of the things I really want to push on. Like I said, I'm not going to have much time to do it myself until next month, or until probably March, actually, because it's end of January.
**Daniel Dyla (Dynatrace)** 59:01 Okay.
I'm around this week. I am starting… I'm out for, most of the beginning of February.
and then I'm back for 2 weeks, and then I'm out for the beginning of March.
**Josh Suereth** 59:16 Okay.
**Daniel Dyla (Dynatrace)** 59:18 I'm taking 2 separate vacations that are each roughly 10 days long at the beginning of February and March.
**Josh Suereth** 59:24 That… I'm so jealous. That sounds fun, man. Enjoy.
Okay, cool, and then… entity as a signal. This, this stuff here.
If you have a chance, Dimitri, to, like… this is just a task list for things as a signal. All the stuff we were talking about from your OTEP,
should probably be in this. If there are things you want us to work on, or divide up work, please add items here, so we can start figuring that out.
**Dmitrii Anoshin** 59:53 I really did.
**Daniel Dyla (Dynatrace)** 59:54 Yo, I can't stay overtime today.
**Josh Suereth** 59:56 Same.
Thank you, Bill. Thanks. I'll see y'all.
