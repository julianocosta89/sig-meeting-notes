SIG: Entities SIG
Date: 2025-12-01
Duration: 66 minutes
============================================================

## Zoom Recording Transcript

Josh Suereth 00:00:21 Hey, what's…
Nathan Smith @ Elastic Observability 00:00:24 Hello.
Josh Suereth 00:00:29 Alright, is this working now?
Nathan Smith @ Elastic Observability 00:00:33 Yes, I can see and hear you.
Josh Suereth 00:01:23 Alright, we'll give a few moments for folks to join. We have 3 things to talk about. I don't know if there's anything you wanted to add.
But, wait, why did I do that?
Let's do this.
Okay.
My computer gets, like, really slow whenever I, boot into Chrome.
Because I have so many open tabs, and it does, like, a scan of everything, so… When I first try to join these meetings, it's always a pain in the butt.
Nathan Smith @ Elastic Observability 00:02:10 Yeah, between those and the Slack teams… 30… 36 gig of RAM just doesn't… just doesn't cut it anymore, I guess.
Josh Suereth 00:02:25 I actually, can't install Slack, I have to run it in the browser, so that's partly what is taken up on my Chrome. Sometimes I kill Slack for the meeting.
The number of browser-based apps I have is insane, I guess is what I'm saying.
Nathan Smith @ Elastic Observability 00:02:42 Yeah, yeah. Well, these days, like… all of the native apps you're running are all electronic, too, so it's just, like, all browsers all over the place. Why not?
Josh Suereth 00:02:55 Yeah?
I don't know if Dana Dyla's gonna be here or not, and I don't have the, chat open anymore to check.
So… we can… we can get started a little bit. How's that sound?
Nathan Smith @ Elastic Observability 00:03:14 Good, I think, Dimitri replied?
He's gonna be 30 minutes. You will be 30 minutes late.
Josh Suereth 00:03:21 Yeah.
So we can go through stuff, and then we'll, get to where we need Dimitri.
We'll do some Dimitri things.
Yeah, let's talk about this merge algorithm here.
First I want to talk about the wording clarification when Dimitri's here.
Then we can talk about OTEP next steps.
So what this is, is I tried to add our merge algorithm.
from, from the OTEP, Which, it adds two sections, one in entities, which talks about how to merge entities, and then one in resource, which talks about how to merge entities into resource.
So, the entity merge button is basically… just talks about when you can merge an entity, which is if the type's the same, and the schema URL's the same, and they have the same attributes. And I don't know if this is, like, if I need to… make different pseudocode for this, I don't care. I just was going for expediency over anything else. So, if we want that to be a programming language, whatever, I can do that.
But that's the, the test that we have for whether or not an entity can be merged.
And then when you merge it, basically, it's just… all the descriptive attributes get merged together, which is, if I don't already have a descriptive attribute, I merge in the one from the one side.
The other thing I call out here is there's always a priority entity. How do I want to phrase this?
Yeah, the first entity is the primary entity, which is, like, the latest, if you will.
And so when you merge, since you only add ones that don't exist, the latest always wins.
So that's how I define this, and then however you want to implement this, like, if you want to implement an algorithm where the right-hand side always wins instead of the left-hand side, I don't care. It's about… you just have to pick a primary, and that one has its stuff take over the other one, right?
So that's entity merging.
But that's also from the OTEP, and that's what we've been doing. Then, under resources, I have this note, which is basically, there's already specification that outlines a merge algorithm for resources.
This, updates that algorithm to be compliant with entities in the data model.
But, you should not use it yet. It says this section will replace that section upon stabilization of entities, meaning we're going to define our merge algorithm in the data model, but we're not going to update the SDK spec to use it until we're ready to actually submit SDK spec changes.
So this is not an SDK spec change yet. That would actually follow this immediately after, hopefully.
Or I can do it in this PR if we want. Anyway, then it describes why you merge.
So this is… this is basically, talking about telescoping again, where merging together entities is expanding the context of the entity.
So you're saying I want… a resource in the context of a host, and in the context of a service, in the context of whatever, and I throw all that stuff together. I don't know if this makes sense, but you can take a look at that offline.
And then this is the basically copy-pasted algorithm.
from our OTEP.
The only thing that's different between our OTEP and this Is… we say for each entity, new entity, in priority order, instead of talking about entity detection.
The OTEP only talks about entity detection, and you detect entities and merge them. The second change is we defer… oh my god, I can't spell perform.
I need to do a spell check pass on this, this is a draft. But, anyway.
We perform… perform a, entity merge.
So, in the OTEP, we actually outlined all the steps for what an entity merge means in this algorithm. Here, what I do is I define entity merge separately here, which we already talked about. This can merge, and then what merge looks like.
And then here, we just say, if an entity exists with the same type, we perform a merge if it's applicable. Otherwise, we ignore the new entity.
Man, my spelling was horrible. I gotta… I ran spell check on this, and it didn't do anything. Okay.
Right.
So that's the TLDR of this, and it just defines the merge algorithm.
I want to go fix those spelling mistakes, like, right now. Any thoughts?
Nathan Smith @ Elastic Observability 00:08:13 It seems pretty clear.
I think I followed everything you just said.
And, The, I think it's good to make a distinction between the… the merging of entities and the merging of resource.
So, yeah, and then I have… I… it just came up on my… notifications, so I'll… I'll read through the whole thing, but from what you explained just now.
It makes sense to me, and I don't think I have any questions. I think the… I think… You… I mean, you've pretty much implemented this in Java.
So, obviously, like, For you, like, the whole… the whole thing works. So, I think… Probably, Probably if, like, questions come up, they'll probably come up In the course of implementing it.
Josh Suereth 00:09:18 I hope, yeah, if you, if you have any, yeah.
Nathan Smith @ Elastic Observability 00:09:22 Yeah, so, yeah, I'll give it a read-through, but so far, Looks pretty good.
Josh Suereth 00:09:34 Okay.
G.
I'm gonna add some more caveats there. So, if nothing… We don't have anything to talk about here, that's good. Do you think I should add, like, the actual SDK specification as well here, or just the data model merge?
Nathan Smith @ Elastic Observability 00:10:17 So this is in… This is in the specification.
Josh Suereth 00:10:25 cut up.
Nathan Smith @ Elastic Observability 00:10:29 I… I don't know. I don't really know what's… what's expected.
Josh Suereth 00:10:36 Before we can implement this across everything, we need… We need the specification to be… stable.
Nathan Smith @ Elastic Observability 00:10:45 Alright.
Josh Suereth 00:10:46 Or at least we need to merge an SDK specification. So let me… I'll just walk you through that a little bit, what we have. So right now, the specification… Under Resource, We have an SDK.
This is stable.
So, when we make changes here, they have to be… account for the fact that the SDK's stable, so we need to do it in non-breaking ways. Resource creation, it… Requires two ways for people to create resource, which is Create and Merge.
Create, we're going to extend to have entities.
As a optional parameter.
Because we're not going to be breaking things, so we need to have it be optional.
but it'll be kind of like this, where schema URL is optional since a particular version.
Merge, interface, this has to get updated to actually talk about how to calculate things. The main thing we need to do with merge… Oh, it's so weird that, like, empty resource shows up. Anyway, The main thing we have to do is this.
we have to update how schema URL is modified, like, this kind of gets deleted, and we're gonna put that merge algorithm we had before here.
the updating resources attributes take precedence. So, you have to basically specify an old and a new, and this will get modified to talk about entities, and then we'll defer to the merge algorithm in the data model.
We do need to then eventually talk about detecting resource information from the environment.
Like, this section, I think, needs to get updated.
there's things about it that are true and all that. There's this notion of a resource detector name and resource detectors, and how we have a container, a host, a process, and a service. I want to change these to basically be entity-based.
And then, this thing about specifying resource information environment variable, we'll talk about this one.
Which is a must, but I don't think most people treat it as a must.
And then we can have a, A secondary thing about the entity signal, and how, like, you should prefer using the new one over the old one.
Resource operations, resources are immutable, so you can just retrieve attributes. We might add a retrieve entities operation here.
If anything, right?
So, I do… I do want to make changes to the SDK here.
And I do think we have to propose those things from the OTEP, and I'm happy to do that, but I wanted to split up the PR where we get our merge algorithm merged, and then we make the SDK PR separately, which I can probably do this week.
What do you think?
Nathan Smith @ Elastic Observability 00:13:50 Yeah, I think that sounds good.
There's kind of the… to, like… The… I don't know the best way to make it clear that, kind of, like.
Entities is the new, better way to do stuff, and… the… Like, raw resource, or whatever you want to call it, is, like… A fallback, like, available for fallback.
Backwards compatibility, but… That's not true. That's not really true until we have the SDKs implementing it.
So it's probably, probably tricky to write.
Well, at least in a clear way.
Josh Suereth 00:14:37 It's fine to put them in specification.
As long as we then roll it out everywhere. The main thing we have to do here is, these resource creation methods. We're gonna… we need to do a Go prototype, because I think the existing one doesn't, like, doesn't look the way we want it to look, and I think that's fixable, so… The other thing is, I'm not sure… this is new.
and in development, the resource detector name with these things. I don't think Go has done this, and the reason why is the same problem we have with our entity's prototype.
So Go does fine-grained resource detection where every single detector detects one attribute and only one attribute.
Nathan Smith @ Elastic Observability 00:15:24 Right.
Josh Suereth 00:15:25 So, that is problematic for this. So, we'll have to look at how they're gonna solve that, and I think… Proposing that a similar entity solution should work.
Oh, Daniel, we were just talking about the spec.
Daniel Dyla (Dynatrace) 00:15:39 Hey there.
Sorry I'm late.
Josh Suereth 00:15:42 No problem. I was just walking through with, Nathan, like, what we have to change to the spec.
And I think, the next PR I want to do is the create algorithm here.
we'll have a sense, you know, X.x.x, Entities option?
Daniel Dyla (Dynatrace) 00:16:02 Cash.
Josh Suereth 00:16:03 And then the merge algorithm will get updated completely.
and leverage the data model merge that I described in the.
Daniel Dyla (Dynatrace) 00:16:13 In the OTEP.
Josh Suereth 00:16:15 No, well, I'll show you what… I'll show you what… I have a PR that pulls it from the OTEP, so we'll walk through that.
Daniel Dyla (Dynatrace) 00:16:20 Okay.
Josh Suereth 00:16:21 then, empty resource is fine. Detecting resource information from the environment, this is where we'll actually, This one, this section, can Lee stay, I believe?
Resource detector name, this section can stay.
Except, instead of… we're gonna change this to, say, populate container entities instead of attributes.
This section's still in development, so we can still do that.
And then specifying resource information via environment variable. This one I want to change to encourage to use the new One that we provide, so we'd allow you to use both.
Yep, and we'll have…
Daniel Dyla (Dynatrace) 00:17:02 To merge them somehow, or… override.
Josh Suereth 00:17:07 Yeah, we need to pick which one wins.
Daniel Dyla (Dynatrace) 00:17:09 Yep.
Josh Suereth 00:17:11 My thinking is we define it so that this one happens first, the entities happen second, and then we merge the entities… like, we merge it so the entities one has priority.
Daniel Dyla (Dynatrace) 00:17:23 Okay.
Josh Suereth 00:17:25 But we can, you know, we can figure that out. Lastly, resource operations. So, we have retrieve attributes. I think we should have retrieve entities.
But… Doesn't matter. Like, I don't… I'm… I haven't needed a retrieve entities operation, just like I haven't needed a retrieve resource attributes operation, even though, you and I were talking about this, I think, in a chat on EntitySig, This might need to be available in the API.
Daniel Dyla (Dynatrace) 00:17:58 I didn't even know… oh, so this is SDK, yeah, so…
Josh Suereth 00:18:02 This is the SDK, yeah. The API, there's a need where people want to take service name and throw it on baggage, for example.
Daniel Dyla (Dynatrace) 00:18:10 Okay.
Josh Suereth 00:18:11 And so, there's a need to be able to retrieve attributes, and it's possible we want to be able to retrieve entities as well.
So… That gets into the whole, what… what… how does an instrumentation API engage with resource if needed? And right now, the answer is you don't. And I think there's a problem there at times, so… We'll have to get that sorted.
Daniel Dyla (Dynatrace) 00:18:36 Okay.
Josh Suereth 00:18:37 Yeah.
Okay, so that's… that's the changes I want to make to here, but that is Phase 2. Phase 1 is… if we keep going back… where did I… This is the, this is the, the definition. What I did was I split it into two pieces. There's an entity merge, which basically says entities may be merged if and only if the types are the same, identity attributes are exactly the same, and schema URL is the same.
So, here's just a simple Ken merge, right?
Daniel Dyla (Dynatrace) 00:19:04 Yep.
Josh Suereth 00:19:05 Then, when you merge an entity, this is the algorithm that we had before. Basically, one of them is priority, which is E, the other one is E prime, but I can make it, like, other, or something, if that makes this easier to read. For every attribute in the second… the lower priority's description, if it doesn't exist, you fire it over.
So, E preserves all of its descriptive attributes, the other one kind of inserts ones that aren't already there.
And I'm doing this left to right. In practice, you can imagine, if I am doing an entity detection, I would put the new stuff on the left, and the existing stuff on the right, and then when I merge, I get what I want.
Daniel Dyla (Dynatrace) 00:19:45 Yep, okay.
Josh Suereth 00:19:47 Right? And if I want to make sure I'm doing detection in the collector, and I don't override something that already exists, I would put it on the right, not the left.
Daniel Dyla (Dynatrace) 00:19:56 Yeah.
I think that the merge… that… that… I guess it's not what we're talking about right now, but that merge order is the opposite of the entity merge order that you Right, because…
Josh Suereth 00:20:09 This is… this is actually kind of the same.
It's the same as it was described in the OTEP.
Because the way the OTEP worked was you started with the most important and went to least important.
Daniel Dyla (Dynatrace) 00:20:25 Right, yeah, oh, okay, I must have just misunderstood when… I had the order mixed up in my head for when you were describing it here, I guess. Maybe I misheard you.
Josh Suereth 00:20:35 No, I don't think you did, but the most important one wins, basically.
Daniel Dyla (Dynatrace) 00:20:40 So this…
Josh Suereth 00:20:40 Right now, the least important one is the second one, the most important one's the first one.
Daniel Dyla (Dynatrace) 00:20:46 Right, so in practice, you would take the first entity and merge the second entity into it, then the third entity, then the fourth entity, then the fifth entity, just merging it all back into the base entity.
Josh Suereth 00:20:59 Yeah. In the order of the list.
In the order of the list. And this is only if you're detecting the exact same entity.
Daniel Dyla (Dynatrace) 00:21:06 Right, yeah.
Josh Suereth 00:21:07 Yeah.
Daniel Dyla (Dynatrace) 00:21:07 Which is not supposed to be allowed. So that was why I, said it's the opposite order, because I think that the merge that I was thinking of is the merge into the resource attributes.
Which, I believe… was the opposite, right? Incoming entities… Or incoming attributes. Oh, do not override.
existing. Yeah, yeah, so it's the same. I'm sorry, it's… I haven't been working for a few days, so…
Josh Suereth 00:21:37 It's fun, it's fun.
The other part of it, and this is again from the OTEP, but I changed a few things. So first, there's a bit here about why you merge, what it means in the data model.
So this is the idea that you have… you're adding context to what you're discovering, right? So I can have a host with a service with a whatever.
In that context.
Then we talk about how to merge an entity into a resource. I only talk about merging an entity into a resource for now, like a set of entities into an existing resource.
Daniel Dyla (Dynatrace) 00:22:11 Yeah, so you construct the resource at startup, and then you run all your entity detection… Okay.
Josh Suereth 00:22:19 So, the idea here is you have, we take all the entities in priority order, we construct the set of existing entities E, if… and then we look at the new entities in priority order. If that entity exists in… or if a different entity exists in E, with the same type as new entity, then we perform a merge, if applicable. Otherwise, we ignore it.
And if there is no conflict, we just add it into the set.
Crap.
Daniel Dyla (Dynatrace) 00:22:50 Correct.
Josh Suereth 00:22:51 I've… I converted.
Daniel Dyla (Dynatrace) 00:22:52 That's true.
Josh Suereth 00:22:52 Using D' and E prime and all this kind of crap. I need to just change it to be new entity everywhere.
So anywhere you see D', it should be New Entity. Let me go fix that before I get annoyed with myself.
This is in Resource Data Model.
Should not be D prime, it should be new entity.
Yeah, I was using… I was being too mathy, so I tried to make it less mathy.
So yeah, this should be new entity. Anyway, lastly, we update the resource to use this new set of entities, everything that you've put in the set.
If all entities within E have the same schema URL, you set the schema URL to match. This is the same logic we had before. Otherwise, you set it blank. We had a bunch… Tigrin had a bunch of comments on this, about, like, not violating existing schema URL semantics, but I'm basically saying if you merge an entity in.
and that entity will have schema URL. If they don't match, then…
Daniel Dyla (Dynatrace) 00:23:52 Yeah, the schema URL either has to be 100% correct, or it is worse than useless.
Josh Suereth 00:23:59 Yes, I would argue it's not really used today the way it's intended. Hardly at all.
Daniel Dyla (Dynatrace) 00:24:04 Yeah. Okay.
Do we want…
Josh Suereth 00:24:07 Java until I added it at one point, is surprising. Anyway.
Daniel Dyla (Dynatrace) 00:24:12 So…
Josh Suereth 00:24:14 Oh, this is the last…
Daniel Dyla (Dynatrace) 00:24:15 possible… a possible… I guess it doesn't… I was gonna say we could have… a schema URL per entity, but… Yeah, I don't know.
We may want to… At some point, once we have the schema migrations, Extend this such that you… Like, the merge algorithm… Would upgrade all entities to the latest.
supported by the SDK.
Josh Suereth 00:24:52 Yeah, it could.
Daniel Dyla (Dynatrace) 00:24:53 Yeah, like, you could have, like, an upgrading merger or something like that. Maybe the merge would then have to have… yeah.
We don't need to do it right now, anyways, doesn't matter.
Josh Suereth 00:25:04 You, you would need… you need the ability to actually know what the… how to… how to make that change.
Daniel Dyla (Dynatrace) 00:25:10 Yeah.
Josh Suereth 00:25:10 Version.
Daniel Dyla (Dynatrace) 00:25:11 We need Schema V2 done, anyways.
Josh Suereth 00:25:15 That is… I am… I'm pushing real hard for that. That is what, I'm working on next, is actually the diff algorithm for V2.
I don't know if you saw how far V2 is, but you can already write policies and do Weaver Live Check and, generate schema and stuff for V2, we just don't have the diff. And the diff is what matters for telemetry schema.
So, it'll be fun. Alright, so, following CFE. Okay, otherwise, this is the last one, which is basically, what I'm defining here is if you… only merging entities into resource. I don't talk about if you're also adding raw attributes, which we can cover when we do the SDK merge algorithm. But this just says.
if you have any raw attribute, right, that exists either in description or identity of an entity in that set, you would just remove it at this point. So, the… if you're taking a new set of entities and merging it into a resource.
You have no raw attributes on the thing that's coming in.
So, what happens is any of the new entities that come in override everything you have.
And so, if something new comes in that conflicts with an existing raw attribute you have.
You actually blast it away.
it disappears from raw attributes. You keep what was in the entity.
There's a second bit of this that, when you implement it on resource-to-resource merge that you have to deal with, which is if the other resource also has raw attributes, what do you do with them?
If they conflict with entities from the first one. That is a category in my implementation, but was not in the OTEP, actually. So, that one will have to pull… pull over when we do the SDK spec.
Daniel Dyla (Dynatrace) 00:27:03 Yep, Okay. I guess, like, this kind of just assumes that entities is the way forward. I think you might get some pushback on that, and the… a use case that I could see to turn it the opposite way would be… Using resource attributes to override… Entity description attributes manually.
like, if I, as an operator, I have my set of entity detectors or whatever, if I want to override some attribute, setting it on the resource is, like, an easier way to do that, if that were to win. In this case, it wouldn't. It would just get blown away.
I don't know how else you would necessarily do that, other than inserting a higher priority entity detector in the list that then has the same… identity as the one you're trying to override, and overriding a descriptive attribute, like, it becomes more complex.
Josh Suereth 00:28:15 woman.
Daniel Dyla (Dynatrace) 00:28:15 If somebody overwrites an attribute that is identifying in an entity, then you've screwed everything up.
Josh Suereth 00:28:22 Why don't we… why don't we define that in here, then? Instead of merging entities in resource, I can say merging a resource with entities.
And we can actually handle that. I, I think… What I would like to have happen with raw attributes, what I implement in Java, I don't like, because we blow away entities too quickly.
Anytime there's a raw attribute that has any conflict, you blow away the entity. But what we could do is just say, if you merge an attribute.
That conflicts with the idea of an entity, you blow away the entity.
Daniel Dyla (Dynatrace) 00:28:56 What if we defined resource as… an entity with no identity. With no identifying attributes. And then allow the user to put it wherever in the priority list they feel like.
and then just rely on the entity merging and call it a day. Say, either use entities or just one resource, not both. If you want resource, you have to insert it into your entity list.
Josh Suereth 00:29:35 We do have a rule that entities cannot have the same attributes, like, they can't own the same attributes at all.
It doesn't apply to the a pleasure.
Daniel Dyla (Dynatrace) 00:29:46 Well… I think it does, by the wording we have now, I think… I think the wording just says that they can't conflict, but…
Josh Suereth 00:29:54 Yeah.
Daniel Dyla (Dynatrace) 00:29:55 If there was a descriptive attribute.
Could allow that, and that would be… I mean, the fact that we have a priority order at all implies that that might happen.
Josh Suereth 00:30:08 Yeah…
Daniel Dyla (Dynatrace) 00:30:09 Otherwise, the order wouldn't matter, because if they never had the same attributes, you could do it in any order.
Josh Suereth 00:30:15 The priority order only applies to how you merge them, it doesn't actually apply to the data model of a resource.
Like, to me… Right.
Daniel Dyla (Dynatrace) 00:30:24 Yeah.
Josh Suereth 00:30:25 Yeah.
Cause of how we changed this.
It's interesting, we're… we have implementations we're happy with, Generally.
But describing it, the specification is hard. Okay.
Daniel Dyla (Dynatrace) 00:30:45 Yeah, I mean, the implementations… Do what you're saying in the spec here?
Josh Suereth 00:30:51 I guess maybe in the interest of.
Daniel Dyla (Dynatrace) 00:30:55 of moving forward, we should just keep it, because what I was just describing would be, I think, a more… more break-in for users, like, they have to have a harder break when they move to entities, and your way is probably a little bit softer there.
And then if we… 6 months or a year from now, or, you know, let's be real, 5 years, when everybody's using entities.
Maybe we can redefine, like.
Josh Suereth 00:31:26 Instead of…
Daniel Dyla (Dynatrace) 00:31:27 Calling it resource attributes, we just call it, like, an identity-less entity and call it a day.
Josh Suereth 00:31:34 Yep.
Yep.
I like that. Okay. Okay. So, I can update the algorithm here to deal with attributes, and I do think we should, if you're changing a descriptive attribute, you shouldn't blow away the entity. If you're changing an identifying attribute, we blow away the entity definition.
Daniel Dyla (Dynatrace) 00:31:52 Yes.
Josh Suereth 00:31:53 Yeah.
Daniel Dyla (Dynatrace) 00:31:54 I think that that works.
Josh Suereth 00:31:56 Okay.
So I will add that to a… an algorithm thing here. Like, what we implemented, just… we'll… we'll call it out. So I'll add that to that, we can add a comment for it. And I think that's actually it for… this PR. This PR is supposed to just be the merge algorithm, so that the next PR can actually do more SDK work.
So please, please review, make comments, I'll make cleanups. There's a lot of spelling mistakes that Spellcheck did not get for some reason.
So, I'm, planning to get better spelling checks.
Okay.
Cool.
Let's go to… the next thing. I keep looking at code, and I'm not looking at you guys.
Right.
So that was the merge album. Is… if Dimitri's not here, we're gonna skip to OTEP Next Steps.
Okay.
I'll take some notes quick, too. Well, do you wanna… do you wanna walk us through what you did here, Daniel?
Daniel Dyla (Dynatrace) 00:33:01 Sure, I mean, it's not very much. If you… Go to the… SDK… So I intentionally left this, somewhat… vague.
And I essentially defined it as, like.
you know, the three requirements that we had talked about, before, and I just codified them, a little bit more strictly. But I intentionally left it vague because I'm not entirely sure, What might happen in implementation that, you know, I'd… the OTEP doesn't need to define every little thing, But I think, we should be good to go here.
So, essentially, this is just taking the… the… the… provider, and I called it entity-bound, so when you do, like, provider for entity, or whatever the, the API ends up being called.
It returns an entity-bound provider, which is the same as a normal provider, with the restrictions that it does not shut down its export pipeline.
Because it shares the export pipeline with its parent provider.
And siblings. So, if you flush it.
You must flush at least the data that was, Generated by the bound provider, but you may also flush.
Josh Suereth 00:34:56 You know…
Daniel Dyla (Dynatrace) 00:34:57 data generated by its parents or siblings, just depending on the implementation. They may be kept in, You know, the same place.
Let's see… yeah, oh, configuration is shared. So, I did not, specify that the configuration is… is shared exactly, just that it's… should be the same as its parent, and not directly configurable. So… That…
Josh Suereth 00:35:33 I mean, right?
Daniel Dyla (Dynatrace) 00:35:34 Right now, there's no way to configure Any providers after they're constructed, as far as I'm aware. This is more to head off any sort of… op-amp or after-the-fact, configuration changes. Like, if you want to change the behavior of a child provider, it should be done by configuring its parents.
Josh Suereth 00:35:56 Yes.
Daniel Dyla (Dynatrace) 00:35:56 And then, yes, it may be achieved by directly sharing the object. That's just, The easiest way to do it, probably, if you… In a language where you can.
Josh Suereth 00:36:08 Yep.
Daniel Dyla (Dynatrace) 00:36:10 Let's see, I took the idea of your, The shutdown, like, being treated as a flush, but just ignoring the shutdown part of it in the provider.
I think that's it. It's a relatively simple change, like, there's not very many, differences here.
Josh Suereth 00:36:36 I mean, that matches the implementation, right?
Daniel Dyla (Dynatrace) 00:36:39 Yeah.
Josh Suereth 00:36:40 I mean, the main, the main… craziness, is how to actually physically do it in the metric SDK, but this specification gives you the behavior that we achieved, so… I think it's fun.
Daniel Dyla (Dynatrace) 00:36:54 Yeah, I went for end-user behavior here, because the metrics implementations don't really match each other all that well from language to language, so it needs to be a little bit… I don't know, vague is probably the wrong word, but it leaves a lot up to implementation.
Josh Suereth 00:37:12 Yeah.
I think that's… I like how this is phrased, actually, because it… I think it covers everything we wanted, specifies the outcome.
Yeah, I'm really happy with this.
Daniel Dyla (Dynatrace) 00:37:25 I'm sure we will get much more detailed when we get to the actual specification part of it.
But I wanted to leave it, a little bit open on the OTEP, so that when we're working on the specification, and somebody says, oh, I can't do that in Python for some reason, we don't have to then go back and modify the OTEP. The OTEP just describes the desired end result.
Josh Suereth 00:37:52 Yep.
The only thing that's missing here, if I recall correctly, is just we need to list our prototypes.
And then I think this is good to go. Take out a draft and try to get approvals.
Daniel Dyla (Dynatrace) 00:38:04 Okay.
Josh Suereth 00:38:04 So, I can… I can add the Java prototype, if you want to add the JavaScript one, and then we're…
Daniel Dyla (Dynatrace) 00:38:11 Yep, okay.
Josh Suereth 00:38:12 Okay.
Cool.
Nathan Smith @ Elastic Observability 00:38:15 Yeah, Daniel, do you have a draft PR for the JavaScript one?
Daniel Dyla (Dynatrace) 00:38:21 I do, yes. It's a little bit, unfortunately, out of date, but it, it does not have… I… The bound entity part finished.
I will try to finish that up this week.
Let me find the PR, though.
Nathan Smith @ Elastic Observability 00:38:52 Josh, you said you were… I mean, I know we've been looking for a go… Prototype.
Josh Suereth 00:38:59 If you have a chance to do a Go prototype, that'd be… that'd be amazing to add, yeah.
Nathan Smith @ Elastic Observability 00:39:03 I'd have to learn Go first.
Josh Suereth 00:39:07 Yeah, but…
Nathan Smith @ Elastic Observability 00:39:09 I'd have to learn more Go, I think.
And I've asked around at Elastic to see if there's anybody who can jump on that, but I haven't gotten any takers yet.
Josh Suereth 00:39:21 I mean, it's fine. I think the thing I'm more worried about would go is the merge algorithm for entities and resource detection, so that's actually where, you know, there might be some time spent, so…
Daniel Dyla (Dynatrace) 00:39:35 Yeah, in JS, merging and detection and all of that is done it's the… The bound provider that's not finished, but… It should… not be that big of a deal. That the metrics is… is the hard part, and that's why… that's what blocked it, was not… not that, anything in the metrics made it impossible, but that I… am not familiar enough with the metrics implementation to very quickly wrap my head around it and make those changes, so I've been kind of… Poking my way through it, But, yeah, nothing that makes it impossible, it's just… it's a limitation of me, not of the spec.
Josh Suereth 00:40:25 Well, the… yeah, with Java, there's some optimism… if we're… when we go to actually implement that OTEP for real, I would do a lot of optimization work on the prototype I have, because there's a lot of potential there. Like, it works.
It's not too bad. Mostly, there's, like, ergonomic… code… code health things that I think I could fix. A good bit of those, and then some actual optimizations around collection.
To be fair, with metrics.
Their collection is where you have the most amount of freedom in performance.
So, if you're talking about, like, you know, doing an atomic lookup.
It's not as bad as during writing, if you do 2 versus 1, But if you're allocating, like, thousands of objects, then that does matter. So there's, like, a limit to how much you can get away with on… Collection, but you have a lot more wiggle room there.
So… Anyway, cool.
we're already 40 minutes in. I want to talk about this wording clarification. I don't know if Dimitri's gonna join or not, so let's just talk quickly about this. I approve this, even though… I can show you my comment, is like, I don't care.
But I ca- but I kind of care.
Daniel Dyla (Dynatrace) 00:41:46 I saw this PR, a while ago, oh yeah, October 31st.
Josh Suereth 00:41:51 I think… I think people are confused about, like.
the fact that identity is a set of attributes, and that we have attribute key… they're, like, they're confusing the protocol and the thing, and calling it identifying attributes, and descriptive attributes, and identity and description is confusing people, so I won't.
Daniel Dyla (Dynatrace) 00:42:09 Yeah.
Josh Suereth 00:42:09 with a D… And they're calling it now Attributes of Identity, Okay, cool. I…
Daniel Dyla (Dynatrace) 00:42:17 Yeah, it's attributes of entity identity, rather than attributes that identify the entity. I mean, I don't fully understand, I don't think it changes anything, to be completely honest.
Josh Suereth 00:42:30 I agree. I don't… personally, this just seems very pedantic, but Dimitri was running into confusion in the collector SIG around entities and pushback, and so I do want to figure out why.
But even changing this to be attributes of entity identity instead of identifying attributes, Why isn't this just entity identity, you know?
So, I don't care enough to push back on this if people think this is easier to read, because I'm also not… like, I don't… This does not read, like, English to me, this reads like somebody… not… comfortable with English writing.
But if that makes it more clear to people what's going on, that's fine. I think the main problem is the way the OTLP manifests itself.
The identifying keys and description keys confuses people.
the fact.
Daniel Dyla (Dynatrace) 00:43:30 It's just…
Josh Suereth 00:43:31 Tested thing. I think that's actually the problem.
Daniel Dyla (Dynatrace) 00:43:37 Yeah, I guess maybe it's easier in the SDK land, where you're only really interacting with the logical.
Josh Suereth 00:43:45 Model of it.
Daniel Dyla (Dynatrace) 00:43:47 in the collector, I think they have to interact with, like, the… the real data structure a little bit more, during development. I don't know why people were confused with the old wording.
And because of that, I can't really… have an opinion on the new wording, because I don't know if it solves a problem that I can't recognize. I… I didn't review this.
Not because I… think is a bad change, but because I just didn't, I don't care, one way or the other, about the wording.
Here, I feel like it's a no-op change. I was leaving it to see if other people had an opinion, and I thought maybe the stalebot would just kill it.
I don't know, I did see Josh's comment there, which I.
Josh Suereth 00:44:42 Yeah.
Daniel Dyla (Dynatrace) 00:44:43 even just… more… I don't like to… make things difficult to read with overly technical wording when I can avoid it, and Josh McDonald's comment kind of… it reads as overly, I don't know. It's… it's a very pedantic change.
Josh Suereth 00:45:06 I agree, there's also… yeah.
I'm… if you… if you're looking at what I'm looking at here, this is… or no, hold on, this… this is the motivating issue.
from the SIG, but it's basically, hey.
the proto calls it description keys, and you call it descriptive attributes. What's the difference? And it's like.
the data model, it's an attribute. I think that… I think half of the problem is… I don't know if Josh understands, because I think this is actually driven by Josh McDonald, mostly.
From what I understand now.
Looking at, like, comments and things.
the… if you look in the collector, you only see, like, descriptive keys. And so, I understand that there's a difference between OTLP and how you've named it and all this kind of junk, but I think… I think, literally, they don't understand.
that… The reason it's called descriptive keys in OTLP is to not break backwards compatibility. If we could, it'd just be called description, and it'd be a set of attributes. If we could have broken OTLP, right?
Right. So, I don't want descriptive keys to… Bleed everywhere into our discussion here.
And this whole, like, you know.
I think this is just a misunderstanding of what we've done, and we need to do a better job of describing our data model and how things work, but it's weird, if you look at the data model spec in this issue.
Right? One thing I'd challenge, it says pro definition uses this, semantic conventions uses descriptive attributes, it doesn't talk about the specification itself, where the data model says it's called identity, and it's called description.
Daniel Dyla (Dynatrace) 00:46:42 Yeah, I mean, to me, there's a reason we didn't call it, like, I don't know, Entity Descriptive Key References, which we could have, and would have been very pedantically correct.
Josh Suereth 00:46:54 Yeah.
Daniel Dyla (Dynatrace) 00:46:55 there's a reason we didn't do that. I think it's just a, a matter of some of the people involved here have not been in these meetings, and possibly we have not done a good job communicating.
the difference. When we say descriptive keys versus descriptive attributes, we're kind of referring to the same thing, depending on which context we're talking about. It's just the key of the attribute.
I don't know.
I think they're trying to take the OTLP backwards, backwards compatibility hack that we had to put in there, and push that wording into the specification, which we did intentionally not really do.
Josh Suereth 00:47:46 Yes.
Description, our preferences.
Two keys in.
However, if we… It was purely… This remote keys.
Not… over-index on… collector slash PData.
Shoes here.
Let's see if we can create… Ergonomic API for ecstasy skin.
Such that.
Let's see if the guy matches the… Data model.
That's true.
Don't have foreign institutes.
Daniel Dyla (Dynatrace) 00:48:41 Yeah, if I remember correctly…
Josh Suereth 00:48:44 Dimitri thought that that would be a problem.
Daniel Dyla (Dynatrace) 00:48:47 Not that, like, it would be impossible to do, but so far, as far as I'm aware, nothing in Pdata has, like, any sort of… ergonomic sugar of any kind, right? It's just wrapping the data model almost exactly.
I don't know.
Josh Suereth 00:49:12 Oh, shit.
Why don't.
Withdrawing money.
Approval, for now.
rename things.
But… I think this is an unknown issue, kind of stupid. Okay.
There we go.
Cool.
Let me go remove my approval here.
How do I do that?
Daniel Dyla (Dynatrace) 00:49:50 You just dismiss your review on the…
Josh Suereth 00:49:53 Just missed the… Okay.
Cool.
Yeah, I think we're over-indexing the collector a bit here. And for… what's it called? OLAP, or whatever the hell the, Apache Arrow protocol thing is, they should literally just use our data model, they should not… I mean, they don't exist yet, so…
Daniel Dyla (Dynatrace) 00:50:24 Yeah, if you're constructing something from whole cloth.
Yes. Yes.
Josh Suereth 00:50:33 I'll add this to a D.
So they're using music.
Otap.
And then I'll put a link to the data model so he can see it's in the specification.
So that is under Resource, Data Model… Gear.
Oh, hold on.
Yeah. We call it ID, not identity, in here.
That's…
Daniel Dyla (Dynatrace) 00:51:20 In the data model document.
Josh Suereth 00:51:23 I… and I'm fine calling it ID instead of identity, but.
Daniel Dyla (Dynatrace) 00:51:28 I mean, it's identifying attributes and descriptive. I don't really think that's problematic.
Josh Suereth 00:51:33 Okay, cool.
Oh yeah, one last thing. We only have 8 minutes left. Just wanted to show this.
As part of V2 schema for Weaver, I was implementing Weaver Registry Stats, which is what records statistics across, all the semantic conventions.
And I got a note of the number of entities. So there are 55 defined resource things defined in semantic conventions today, 55 groups of resource attributes.
Of those, 53 are in development, and 2 are stable. This is for entities themselves.
One is deprecated. We got rid of, like, code or some… I forget what it was. Something was in resource that shouldn't have been.
Total with note, you can ignore that. Oh, I have a spacing error, I gotta fix that, alright. Entity identity length distribution, this is interesting. 36 entities have not been updated to have identifying descriptive attributes.
Daniel Dyla (Dynatrace) 00:52:39 I got it. So these are just ones that, like, we took a resource, we moved it over with modifying essentially nothing, and said everything is descriptive.
Josh Suereth 00:52:47 Yes, well, we don't say everything's descriptive, we actually have an other category, which, if you have any attribute in another category, it prevents you from going stable.
Daniel Dyla (Dynatrace) 00:52:55 Undefined. Okay.
Josh Suereth 00:52:57 Yeah, it's like an undefined category.
Daniel Dyla (Dynatrace) 00:52:59 Yes.
Josh Suereth 00:53:00 So you have to… you have to… you have to have at least one identifying attribute to go stable, and you have to have all of your attributes have a defined role before you can stabilize.
Daniel Dyla (Dynatrace) 00:53:11 Yeah, that's a good idea. So, for… in order to take a resource, turn it into an entity, and stabilize it, you have to at least look at every single attribute and say, I am saying this is descriptive specifically, rather than just moving them all over and assuming. Yeah. Okay.
Josh Suereth 00:53:30 Exactly, exactly. So of the ones that are stable, this is interesting, 14 have one and only one ID. That is all the Kubernetes ones.
Daniel Dyla (Dynatrace) 00:53:39 Yeah, that makes sense. They're all pod ID type stuff, UUID type stuff.
Josh Suereth 00:53:43 IDs, yep, which is fun.
Four of them have 2 identifying attributes.
One of them has 3, but that's gonna get removed with one of my latest PRs. Which one has 3? Take a guess.
Nathan Smith @ Elastic Observability 00:53:58 Is it…
Daniel Dyla (Dynatrace) 00:54:02 Is it, like, data center, AWS.
Josh Suereth 00:54:07 Nope.
What's the most used entity today?
Daniel Dyla (Dynatrace) 00:54:13 Nathan said process.
Josh Suereth 00:54:15 Nope, not process. Process, I think, is a 2.
Daniel Dyla (Dynatrace) 00:54:18 host.
Josh Suereth 00:54:20 Nope, not helping.
Daniel Dyla (Dynatrace) 00:54:21 The most used, the most used SD today is the SDK.
Josh Suereth 00:54:27 It's not a service, exactly.
Daniel Dyla (Dynatrace) 00:54:31 Oh, I thought you were gonna say the SDK.
Josh Suereth 00:54:34 The SDK will have 3, it is… it's service, so it's service namespace, service name, and service instance ID are identifying today, but we're actually fragmenting that into 3 entities. I don't know, did you… did I show you this, by the way?
Okay, so first of all, this is, this is really exciting. If you're ever curious about statistics and semantic conventions and how we use things, like, it's so interesting. Most used, attribute type string, of course. All these enums, it's split by cardinality.
We have a.
Daniel Dyla (Dynatrace) 00:55:06 before.
Josh Suereth 00:55:07 Cardinality, anom?
That's right, 54 options on the Anu.
Daniel Dyla (Dynatrace) 00:55:14 That's gotta be, like, the database type or something like that, right?
Josh Suereth 00:55:17 Yep, so that's fun, but you can look at, like, what people use. I want to get Enum to break down differently, but it's just fun. You can see what's stable and what's in development. You can see we still have a lot that are in development, a few release candidates.
Then, the other fun thing is under metrics, I thought this was just fun to look at, instrument breakdown. Up-down counter is… is killing it. Remember when we added up-down counter, everyone's like, this isn't useful? And why do we have this versus a gauge? Now, it's the most used… instrument in semantic conventions.
Daniel Dyla (Dynatrace) 00:55:56 Yeah, I mean…
Josh Suereth 00:55:56 Like, the difference between it and gauge is actually somewhat significant.
Daniel Dyla (Dynatrace) 00:56:02 Yeah, it makes sense to me.
Yeah, I guess I'll leave it at that. We don't have… at Dynatrace, we don't have a difference between an up-down counter and a gauge.
Internally.
Josh Suereth 00:56:15 Yeah.
We… we are… we have been debating how to fix gauge behavior to match what up-down counter behavior should be, because actually, if we could, at query time, handle up-down counter, we could get rid of so many, hey, these metrics are wrong bugs that aren't metric problems, they're query problems.
Daniel Dyla (Dynatrace) 00:56:34 Yeah.
Josh Suereth 00:56:35 I mean, they're merging data the way you expect.
Daniel Dyla (Dynatrace) 00:56:38 We do it at query time, and it's entirely possible to use aggregations that don't make sense, but don't do that.
Josh Suereth 00:56:48 Yep.
Yep. Anyway, I just, I found this interesting, you know, histograms, and then units, right, most things are bytes, and then there's a lot of units that get used once.
Spins, I don't have anything super interesting here besides way more client spends than server spends, which I would expect because it's mostly focused on SDK implementations.
And then a few internal spans.
So… Kind of fun.
Daniel Dyla (Dynatrace) 00:57:19 Yeah, that is cool. I, I feel like, all of these types that get used once, or that the, the… not types, Units that get used once?
They're all likely… counters and up-down counters, right? That are… that are counting some… Some domain-specific thing.
I almost feel like it would be worth aggregating all of those to see, like, how many domain-specific counters do we have.
Josh Suereth 00:57:47 I'm actually playing… so, I was gonna do that, and then with… and Noom's, I was gonna have a Noom's as a roll-up.
And then a breakdown by cardinality from there. So, you would get, under type breakdown, you'd get all the enums in one thing, and then you'd have an enum cardinality breakdown as a separate stat. Anyway, these are all things that… you know, it's real easy to write. I actually had Jim and I do most of this CL.
For calculating the stats for V2, but it's, It just takes a while. The other thing is, when we talk about refinements, that'll blow your mind. Alright, if you didn't see this, by the way, this is, how service is getting modeled in the service and deployment SIG. We had a bunch of discussions on this, and I want to do… Is this the… that's the registry, I don't want the registry, I want this.
We might throw this in the registry. But basically, we're doing a three-tier entity layout.
So the idea is you have service namespace as an entity, which can contain a set of services, and then within those services is instance IDs.
So it's gonna be.
Daniel Dyla (Dynatrace) 00:58:53 That makes sense to me.
Josh Suereth 00:58:54 Three entities, yeah. And you can layer them as you want.
Daniel Dyla (Dynatrace) 00:58:58 Having not read any of this and only looking at this description, is it intentional that the instance IDs are, post-fixes of the service names or not?
Josh Suereth 00:59:10 Right now, it's intentional, because they are… mirroring what happens in Kubernetes, but they do not have to be, right?
It's just a dumb example. We also give them descriptions, right? So… a namespace is a system of components, service is one, logical, distinct components that make up an application. By the way, we're using the word application because when we used Gemini and, what, Claude and all, you know, OpenAI and all these folks to ask, hey, what… What does OpenTelemetry model a service as? It used the word application every time.
So I think it's canonical. There's also, Kubernetes has a notion of an application and how to model it.
In their annotations that we're trying to match.
So, anyway, if you have a chance, please take a look at this. This is in SEMCOV. I'd love to have some of the entity sake approving this as well, to make sure this is in line with entities.
Yeah, this just adds these definitions, and then updates the, well, it updates the rolls.
So, we have the three entities, and then we have their roles. So, service instance ID is identifying for service instance, and service name is identifying for service, service version is descriptive, and for service namespace, the namespace is identifying.
That's it.
I think we did change the definitions of some of these things, yeah.
We just renamed that. Did we change any of the attribute definitions? No, I don't think we needed to.
Nathan Smith @ Elastic Observability 01:00:55 So… so it's not… It's just service.namespace.
But service.namespace is the identifying attribute.
Of the service namespace? I was expecting something. If service…
Josh Suereth 01:01:14 Namespace was going to be an entity I was expecting service.namespace.name.
Daniel Dyla (Dynatrace) 01:01:19 Well, it could potentially have some descriptive… like, I think the service namespace is essentially, like, your, application name, I don't know, like, taking Google as an example, the service namespace would be, like, Google Search, right?
And then you might have a name… I guess… I don't know if the identity would be split from that. I can't… I can't think of a reason why you would have… a name be different than an ID in that case?
Nathan Smith @ Elastic Observability 01:01:52 Yeah.
Josh Suereth 01:01:53 What… what do you mean?
Daniel Dyla (Dynatrace) 01:01:56 Well, it wouldn't… makes sense. You would only have… The ID… separate from a name if you thought you were gonna have two separate namespaces with the same name. So, like, you might have.
Josh Suereth 01:02:12 Oh, like, I don't.
Daniel Dyla (Dynatrace) 01:02:13 Google Search Internal and Google Search External, or something like that, and they're both called Google Search.
Josh Suereth 01:02:21 Yeah, which we kind of don't really want at that level, if possible.
Nathan Smith @ Elastic Observability 01:02:26 And in Kubernetes, I'm… I haven't looked, but I'm guessing people are putting, like, the cage namespace And the service namespace to be the same?
Josh Suereth 01:02:37 Oh, you mean, yeah, so by default, by default, if you use the OpenTelemetry operator, the service namespace is the case namespace.
Nathan Smith @ Elastic Observability 01:02:45 Right, yeah.
Josh Suereth 01:02:45 And then your service name is your, like, workload Thing, so deployment, job, whatever.
Daniel Dyla (Dynatrace) 01:02:55 Yeah, I guess what, Nathan, what you're… what you're getting at is the, like… An entity with only a single attribute that's identifying is kind of odd.
right.
Nathan Smith @ Elastic Observability 01:03:09 Well, yeah, I mean…
Daniel Dyla (Dynatrace) 01:03:10 out.
Nathan Smith @ Elastic Observability 01:03:11 Well, we just went through and changed, like, deployment environment, and… A few other things, like, we added a name.
attribute.
Josh Suereth 01:03:22 Yes.
Do we need to do that for service namespace? Not sure. That's… actually, that's one of the pieces of contention here. Right now, the plan is not to add that to service namespace. This also violates… well, it's a bit awkward.
Because service name and service namespace are so widely used, we don't think we can afford to break them.
Like, if I could… wave back time and start again, I would actually call it application name. I would have service name underneath that, and I would have just gone with that to go forward with. I can show you some bugs where service name and namespace have confused people, and they don't know how to use them.
Nathan Smith @ Elastic Observability 01:04:08 Yeah.
Josh Suereth 01:04:09 Yeah, excellent.
Nathan Smith @ Elastic Observability 01:04:09 I mean, I…
Josh Suereth 01:04:10 Pictures that are weird, you know.
Nathan Smith @ Elastic Observability 01:04:11 I guess the way I understood it from looking at the… from… from reading The pre-existing docs is that like… namespace… Is an identifying attribute of a service, along with service name.
Josh Suereth 01:04:29 That… yes. What we're… what we're saying now is namespace is identifying of a service if You want to report a service in the context of a namespace, but you could report the service independently.
So, for example, if… this is the entity thing overall, right? If I am… running a Prometheus inside of a namespace, and that namespace owns my whole application scope, and I'm just reporting all my data specific to one application.
I don't care about the namespace at that point. It doesn't… because all I have are raw surfaces.
So, great, I don't need it. But when I want… to contextualize things on that namespace, great, then I add it. And so then I have both those entities reported, versus not.
The thing… the thing we… I found, when we look through things, service namespace was being used inconsistently. Some people absolutely require it, some people don't pay attention to it at all.
So… As with all things OTEL, Unless we actually make a hard requirement.
It's kind of, like, de facto chaos.
Daniel Dyla (Dynatrace) 01:05:36 I didn't even know it existed.
Josh Suereth 01:05:38 You didn't know namespace existed? Some people thought it was a hard requirement, and someone were like, no, it's absolutely not, that was surprising.
Daniel Dyla (Dynatrace) 01:05:46 It makes sense that it exists, but I didn't realize that it did.
Josh Suereth 01:05:51 Yeah.
Right?
Nathan Smith @ Elastic Observability 01:05:52 It is there on, OTELD demo data, at least.
That I'm running.
Josh Suereth 01:05:58 Yeah, Hotel Demo is supposed to be the best of hotel, so it would have all the most recent stuff in it.
Daniel Dyla (Dynatrace) 01:06:04 Absolutely, the demo's always kept 100% up to date.
Josh Suereth 01:06:11 Yeah. Anyway, feel free to take a look at that. I'm curious what your thoughts are, if you want to make comments, let us know. It already has, I think, 2 approvals, so we're probably gonna merge that one relatively soon, and then that will help us actually start to… mark more entities as stable, or get service done. The next goal of that SIG is to get deployment marked stable. That one's gonna be exciting.
Because deployment's where you could say there's internal and external, right? Or, I have staging tasks dev.
Okay, we're way over. Thanks, guys.
Daniel Dyla (Dynatrace) 01:06:49 Hola. Yeah, thank you.
Nathan Smith @ Elastic Observability 01:06:52 Thanks.
