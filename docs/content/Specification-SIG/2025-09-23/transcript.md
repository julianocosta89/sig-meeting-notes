SIG: Specification SIG
Date: 2025-09-23
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**TELEPHONE_USER** 02:16 The person you're.
**Josh Suereth** 02:16 trying to reach… Hello, can you hear me?
**Liudmila Molkova** 02:28 Yes?
**Bob Strecansky** 02:29 jam.
**Josh Suereth** 02:29 Hello?
**Liudmila Molkova** 02:31 Yep.
**Josh Suereth** 02:32 Okay.
Sorry, my… my computer microphone is completely dead for some reason, but I'm the note-taker for the call, so as long as you can hear me, we'll continue.
Okay, yeah, please add your agenda items.
**Bob Strecansky** 02:53 We can hear him.
**Josh Suereth** 03:02 Alright, I was gonna get started quickly, I don't think we have… Substigs, yeah, okay.
Cool.
I can't see when I'm talking online, so apologies, it's weird.
I'm gonna talk a little bit about an EntitySIG update. So, last time we came here from the entity SIG, we talked about OTEP4316, which was actually adding the ability for resource to be mutated, after initialization.
We had some prototypes around this, we had the ability to attach entities and have entities change states, and the too-long-didn't read is, we ran into a lot of issues with our prototyping. There were a lot of concerns, and it got pretty darn ugly, the implementation.
So we took a step back and started asking, like, what are the fundamental assumptions and fundamental things we need here? And there were some insightful comments on the OTEP. I think the most important one was basically.
There are two kinds of things in resource, and we might be trying to put, changeable, mutatable things into resource when we shouldn't.
So we've created a new OTEP that explores this, which is 4665.
The too-long-didn't read for this OTEP is that we'd like to actually change GitMeter and git logger.
Where you can actually provide an entity when you get a meter or logger. So this would be, I need to record data, for example, about browser session. That was the one big motivating problem.
So I can grab a meter that will record data about a session.
And then I can… all the metrics that I provide on that meter are for that session, and kind of tuned to that session. This is almost like a multi-tenancy capability for the SDK.
So… What this means is that resource remains an immutable, stable identity of the SDK.
We would still use entity to have identifying attributes versus descriptive, and you can read the OTEP to see why we want that.
But Scope would now actually give you an additional identity. So, in the context of scope, you can be recording data about an entity.
sorry, in the context of resource. So this would be, for example, process metrics, right? I might have a resource that is a host, and I might have a scope of a single process, so I can write one thing, an SDK against host, that can report metrics against individual processes.
session events.
would be cool. The resource would be a browser or a device, and scope might be the session itself, so I can pull different sessions. And they might change over the lifetime of the SDK, but the SDK is tied to the browser or device.
Another one that I'm going to call out is the eBPF Profiler. This is a discussion we had in the profiling SIG, where their resource is the host itself, or the, like, the Cates node, and they use eBPF to hook into processes and monitor them. And so, in this case, the scope would actually have the processor executable as the thing that's being monitored.
Those are some examples. If you want to look into details, it's in the OTEP. I believe there's hands. Tigrin, do you want to jump in?
**Tigran Najaryan** 06:28 Yeah. Does this mean that the entity is going to be mutable or immutable?
**Josh Suereth** 06:37 the entity will be immutable on resource. There's an open question of whether we'd allow descriptive attributes to change.
But that would actually be… constitute a breaking change on the spec.
**Tigran Najaryan** 06:51 Okay, so, so you're saying… You, you're solving this problem of Waiting for the resource to settle.
On its mutable attributes by saying you wait until you know what your entity looks like, and then you obtain a meter or a tracer.
And then, when you obtain your meter and tracer, after that point, the entity is immutable. And if it needs to change, for example, a session needs to change in the browser, you have to re-obtain the meter, essentially. Create a new one, if you have a new session.
Is that… am I understanding it correctly?
**Josh Suereth** 07:34 Yeah, so effectively, like, for the session example, I would obtain a meter for my current session, and I would write metrics against it.
And then, when a new session occurs, I would obtain a new meter against the new session and write metrics against it. This, in terms of the prototyping, this solves the biggest problem we had, which was for metrics, which is actually isolating the data by the tenant it's about, by the context, right? So, we already had that capability designed in the spec with scope.
And so, doing this allows us to kind of isolate the metrics for those two sessions, so they're reported independently.
We still have to solve a cleanup issue, you'll see that in the OTEP, but this resolves a lot of issues we were having when we allowed resource to mutate.
**Tigran Najaryan** 08:21 Okay, what happens with the entity refs in the resource? Do we get rid of that?
**Josh Suereth** 08:27 No, we're gonna keep those. So basically, you will have entities in resource and entities in scope. The current proposal says that you cannot have the same entity types in both. They have to be disjoint. So, the idea would be resource has a set of entities, or an entity that it's about, like a host, right?
And then scope would have an entity that further refines. So, you would say that I'm discussing entity X in the context of Y. So, you know, I'm reporting about a process in the context of a host. I'm reporting about a session in the context of a device, or a browser.
**Tigran Najaryan** 09:05 Okay.
**Josh Suereth** 09:06 That's… that's what this is trying to say here.
**Tigran Najaryan** 09:08 Okay.
I guess that second part, I'm not quite sure about.
But the idea of having an entity in the scope, I think I understand. Makes sense to me. I'll need to think a bit more about it, but… Okay.
**Josh Suereth** 09:24 Please do, yeah, we're looking for feedback on the OTEP. The OTEP's still in draft, but, like, that… yes, that is one of the things we absolutely need more thought around.
**Daniel Dyla (Dynatrace)** 09:35 one of the ways that was helpful for me to think about it, because for me, I was approaching it more from the immutability of resource side, it's that the… the resource… the set… the combined set of entities in the top-level resource and the scope resource is, like.
the overall resource that you're reporting against. So rather than mutating the resource when entities change, you create a new scope.
with a new set of entities, and then the resource entities are just the entities that are shared among all scopes, essentially. So all scopes reported by this SDK share these entities, which are in the resource, and then you have the scope entities, which are scoped to specific sets of entities.
**Tigran Najaryan** 10:24 Yeah, and the entities that are associated with a particular signal are essentially a union of the entities on the resource and the entities on the scope that is used for emitting that particular signal.
**Daniel Dyla (Dynatrace)** 10:38 Exactly, yeah. It would be the same list of entities that we previously had, we just had them all on resource, and we would change every now and then. But now, instead of mutating, you essentially create and destroy scopes.
**Tigran Najaryan** 10:54 This, yes, exactly. This gives you an ability to invent new scopes, essentially, which then are associated with brand new entities.
So you're not mutating the scope, you're not mutating the entities, and you're not mutating… nothing is mutated, essentially. You just create new things, new scopes, essentially, and associate the signal that is coming from that moment own with that new scope, essentially, and the entities associated with that scope.
**Daniel Dyla (Dynatrace)** 11:25 It then also makes it, it gives you a better path for reporting against two different instances of the same type of entity. Like, if you're… if you're monitoring Two of the same thing, like two network interfaces or something like that.
That have, you know, the same entity type. It gives you… a sort of, I guess, intro into multi-tenancy. Josh and I have had more discussions about a more holistic multi-tenancy, but… I guess that'll come later, possibly.
**Tigran Najaryan** 11:59 when you say tenant, you mean you're essentially like a… like a… like an instrumentation library, right? That's… that's what you mean by it.
**Daniel Dyla (Dynatrace)** 12:07 No, what I mean is… well, maybe. What I mean is, we have people ask, how can I instantiate two copies of the SDK to report against different resources? So now you could do that with one SDK, and you just have two different scopes.
For if you're monitoring two applications in the same SDK, or two services, or something along those lines.
**Tigran Najaryan** 12:30 Yeah.
**Daniel Dyla (Dynatrace)** 12:31 This doesn't get us all the way there, but it introduces the concepts that we need.
**Tigran Najaryan** 12:39 Okay.
Okay I think I understand the idea, I think about it.
**Josh Suereth** 12:47 Yeah, please do, and look at the open questions. Right now, there's, I think all the open questions that I'm aware of, even the one you raised, should be in open questions, with, like, a proposed path forward for the OTEP.
And I do think as we prototype and explore specification, we'd be diving deeper. The OTEP is a directional OTEP, so I want to get approval for this direction.
with the OTEP, And the current initial thinking for each open question, but I do want to reserve the right, as we explore the specification, to, like, you know, course correct. So, just for context, that don't take what's listed in the answer to the open questions as the only answer it could be.
Okay, that one we spent 10 minutes on, and if folks want to continue discussion, please continue on the OTEP. We will be back here to talk more about the OTEP, and I will take it out of draft after the entity SIG has had a chance to dive in on Thursday on it. So, cool.
All right, let's move on. TRASC, Minimum Severity and Trace Base Logger Configuration Parameters.
**Trask Stalnaker** 13:56 Yeah, we discussed this last week, and, the… Decision was to… ask the configuration SIG to take a look at it, before we merge it. I did post to the config sig Slack, and Tyler did review it and approve. So I think it's ready to be merged.
**Carlos Alberto Cortez** 14:25 Yep. Up to…
**Trask Stalnaker** 14:26 Y'all.
**Carlos Alberto Cortez** 14:27 Yeah, I think we can merge that. I was waiting just in case, Alex Watten or somebody else from the coffee group, Tyler is enough, I think. And we waited enough time. So I think we can go ahead and merge that now.
**Josh Suereth** 14:42 Yeah.
**Trask Stalnaker** 14:42 Cool.
**Josh Suereth** 14:42 Feel free to click the button, Carlos, yeah?
Where I can… do you want me to click it now?
Oh, it's already clicked. I just clicked the button. Okay.
**Carlos Alberto Cortez** 14:51 Yeah, that's what I would say, somebody… Somebody was faster.
**Josh Suereth** 14:57 Alright, so, yes.
Alright, next, this was… oh, this was listed as offline, but let's talk about it in person a little. Robert, extend attribute value set. Suggestions have been there and needs reviews.
Any updates on how you applied the suggestions? Was there anything you want to call out?
**Robert Pająk** 15:17 So, I have, basically, Tigran, thanks for your review. I have, I have replied to all your comments.
and I tried to apply your suggestions. There was one very good, one, very one good comment regarding the attribute count limits, that it needs more clarification.
So, basically, I added more information spec, so it's more, easier to digest, making sure that readers correctly understand that the attribute count is about attributes themselves, not about these things which are in the any value maps.
So I added an additional bullet point, and I also enhanced the description of the PR to call it out, and also the reasons why I propose… why I propose.
Other, other suggestions, I think, were mostly, like, style, style, style-related, so yeah, I… I don't think there are critical blockers, but I'm also… we can follow up on this one. Yeah, like, this is an example of it.
Is there anything, Tigran, that you want to call out?
I didn't have the chance to, unfortunately, look at the last week's recording yet.
**Tigran Najaryan** 16:35 Yeah, I'll take another look, Robert. I didn't have a chance to take a look at after you made the changes, I'll do it.
**Robert Pająk** 16:44 After reviewing the PRT grant, do you think that it's going to the correct direction? Do you think… or, like, overall, what's your feedback about it?
**Tigran Najaryan** 16:53 No, I've… Okay. Yeah.
**Robert Pająk** 16:56 Thank you very much.
**Tigran Najaryan** 16:58 Thank you.
**Josh Suereth** 16:59 Can I ask quick, Robert, was the, entity stuff resolved here that Lyudmila raised?
**Robert Pająk** 17:06 Yes, I think it is. I think I added it here.
I had responded it, I do not remember… Couple right now.
**Liudmila Molkova** 17:21 I think we had a discussion a couple of weeks ago, that… We're… Will not have the distinction in the spec.
Because… We're essentially going all in on supporting complex attributes everywhere.
Am I right, Robert?
**Robert Pająk** 17:44 Yes, that's correct.
**Liudmila Molkova** 17:51 So I think based on those.
**Josh Suereth** 17:52 That means…
**Liudmila Molkova** 17:53 Yeah, go ahead.
**Josh Suereth** 17:54 Yeah, there's, there's, there's a… okay.
There's a, for context, there was a bug in the entities project that I'll have to pull off of the wait for decisions to be made, and add to the… we have to sort out what we're going to do here.
Yeah.
**Robert Pająk** 18:15 Because here, the change… I also had to change it also because of the hyperlink changes, if I remember correctly, but maybe I'm wrong. So, Josh, if you have any suggestions how to tackle this, this particular line, feel free to have the suggestion, but I can also wait on your fix as well.
**Josh Suereth** 18:35 Yeah, this… it could be also something that we tackle in semantic conventions, where we don't allow you to model, complex attributes. Yeah. Okay.
**Robert Pająk** 18:49 Let me, let me think about that, sorry.
**Josh Suereth** 18:52 That was one reason I didn't, approve this yet, was I was looking at it. Okay, cool.
**Robert Pająk** 18:57 distributors.
**Josh Suereth** 18:58 I don't think we have any other topics.
Yeah, yeah, I'll take a look and see what I can say, but what I want to say, if overall in the spec, if we are going towards having, you know, Standard attributes, or attributes be the same everywhere.
I'm fine with that, as long as we're consistent with it, it's just there's a set of implications that we need to sort through, and it could be that we maybe didn't want to use attributes, but we can… we'll talk about that.
Alright, I think that was the 5 minutes. Folks are going to re-review this. Anything else folks want to raise for the spec?
Okay.
Going once, going twice.
**Robert Pająk** 20:04 We'll, we'll call it there.
**Josh Suereth** 20:07 Oh, go for it.
**Robert Pająk** 20:07 One question. We have, KubeCon North America coming in November. Are there any things which are, which needs to be done for preparing? Are there, you know, any… do we have any agendas, or if it's too early yet?
Like, the observatory, etc.
**Josh Suereth** 20:30 That's a great question. Do we have folks here who help plan this?
**Antoine Toulme** 20:35 I will.
**Josh Suereth** 20:37 Come on.
**Antoine Toulme** 20:38 Yeah, we're, So right now, what I'm trying to do at this point is, I'm actually building a list of stakeholders and people from the project who will be at KubeCon. I've asked just to collect a 6 so far, but I will expand that. Based on that, it would be interesting to kind of see what concentration of folks are going to be present in the first place.
For what it's worth, there's just not… I think I shared that internally, but I'll be able to share that with the project.
And it appears that we have quite a few folks who might not be joining us in Atlanta.
So, I want to be upfront about this, is that we might not be having the same discussions we're able to have, maybe, let's say, in London, because we just don't have the critical mass of people who can talk about a specific topic.
So… Okay, thank you, Daniel.
**Josh Suereth** 21:34 You know?
**Antoine Toulme** 21:35 So, I just want you to prepare yourself that if you want to have these type of discussions at CubeCon, let's first make sure people are coming, because that's actually not a given at all at this time. And so, based off that, we will be, probably trying to make plans to engage with people who are there and Not talk about stuff where, you know, some stakeholder's not there.
**Josh Suereth** 21:57 Yep.
**Antoine Toulme** 21:59 And that's all I have.
**Josh Suereth** 22:00 I think that's… Yes.
If there's any announcements we're making at KubeCon, we should, and those of you who are there, I know, I will be there, surprisingly, this time, so I'm happy to talk to anyone and have discussions, but as always with any open source thing, these are conventions for us to get together and say hi, but we should not be exclusive.
To people who are in person at these events, always, and so, like, key work still needs to happen, you know, on pull requests, in issues, and then with support from this meeting, support from, you know, conferences and things like that, so…
**Antoine Toulme** 22:40 jump.
**Josh Suereth** 22:40 Real quick…
**Antoine Toulme** 22:43 Sure.
**Josh Suereth** 22:43 Gmacd added a deprecation plan for, trace-based sampling and things, in chat, so I'm just gonna mention this. Do you want to say anything specific, Josh?
**jmacdonald** 22:54 Not too much. This has been discussed over the months and months. It is just adding, re-stabilizing the trace ID ratio, making the introduction of the probability sampler a little slower, and adding some warning messages. So I think this was, one of the reservations that we heard from users with existing trace ID ratio-based, it's not a big deal, but here it is.
**Josh Suereth** 23:22 Yeah, thank you for this, by the way. I'm super excited for the probability sampler to, become the default. So, it'll be… Yay.
**jmacdonald** 23:30 Yay, thank you.
**Josh Suereth** 23:31 Alright, Cool. And sorry if I, anyway, the, previous discussion, if we want to continue that, let me know. It's just I, Look forward to seeing people who can make it, and I totally understand if you cannot, and why you cannot, and it is, I don't want to dwell on it in this meeting. Any other topics folks have?
Okay Thank you, everybody. We'll see y'all next week. Have a great week.
**Trask Stalnaker** 24:04 Bye.
**Carlos Alberto Cortez** 24:05 See you!
**Liudmila Molkova** 24:07 Bye.
