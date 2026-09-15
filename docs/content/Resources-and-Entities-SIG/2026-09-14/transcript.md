SIG: Resources and Entities SIG
Date: 2026-09-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth (Google LLC)** 02:00 Hey, folks.
**Matthieu Noirbusson (Sensor Factory)** 02:06 Hello?
**Josh Suereth (Google LLC)** 02:09 How we all doing?
**Neil Fajardo** 02:17 It's not a bad Monday.
**Josh Suereth (Google LLC)** 02:21 If you have any topics, please add them.
Might wait a little bit. The first topic needs, Dan, so I was gonna wait for him to show up.
Unless we have another topic we can get started.
Let's see… Keep switching between tabs to go from chat to here, so apologies, I have way too much open.
Alright, here we go.
Looks like we don't have any… Any other topics?
**Neil Fajardo** 03:37 I guess something that's more conversational is, if I want to get more involved with the entities and this topic, is there any advice that the group can give?
**Josh Suereth (Google LLC)** 03:46 Yeah, right now, I think the main thing we have going on is we're trying to land Part 1 of Entities.
So, yeah, I think some of these have…
**Neil Fajardo** 03:58 In the spec, you mean? The version?
**Josh Suereth (Google LLC)** 04:00 In the spec, yes. We have, like, there's, like, two PRs in the spec repo, and then there's actually prototyping and implementation in languages. Right now, we have JavaScript and Java.
And I think we have some Go prototypes from, like.
From a while ago, that probably need to get updated.
The thing that we really want to do is make sure we're landing that and getting that through initially. If I show you the project plan… I think, where's this right here?
It obviously opened in a different tab.
So we have, like, a Phase 1 and a Phase 2 going on, and so, with Phase 1, If there's anything that you want to help out with, like… let us know, and there's probably work there that has to get done. A lot of it right now is just getting the specifications sorted, so that we get that approved and through for everyone. There's a lot of nuances with the language and stuff for people.
We'll talk about that a bit more, but if you have a language that you develop in that doesn't have a prototype and you want to make one, that would be actually really big initially.
Regarding collector work, that's where Phase 2… we have… we have a big tracking bug for Collector, which is… add support for new entity resources, this one here. There's, still some open support for entity refs and entities in the collector.
So if you want to, like, sync with Dmitrii and pick up any of these bugs, that would also be super useful.
And then, in Phase 2, we basically need to start really thinking about, entity as a signal and relationships, and do relationship modeling. And so, Dmitrii has been doing a bunch of that work, but got pulled off onto other things at work.
So, it's kind of a little bit on pause. If you wanted to take a look at what he has and start thinking through some of that, that'd be great. You know, from my perspective, obviously, I'm trying to, like, land stuff before we… so we all move together, so I'm really trying to get these things shored up and nailed down and contributed quickly, so we can move on to Phase 2.
is where my head's at. But if any of that sounds interesting, let us know.
**Neil Fajardo** 06:17 It does, that's good info, too. So I'll take a look through the project plan and see where we might be able to help out.
**Josh Suereth (Google LLC)** 06:23 Yeah, and anything at all, just let us know, and yeah.
I think we also have a backlog here of things that we haven't, like.
worked on. If there's any of these that call to you, we might be able to pull those over as well. Cause I think there's some things probably not tracked in here. Okay.
Daniel's here, so… If you have any other questions, let me know. If you want to read through this, let us know. And yeah, look forward to talking to you more. Hopefully.
**Neil Fajardo** 06:56 Mother.
**Josh Suereth (Google LLC)** 06:57 Find something exciting.
**Neil Fajardo** 06:58 Thanks, Josh.
**Josh Suereth (Google LLC)** 07:00 Okay. Cool.
**Daniel Dyla (Dynatrace LLC)** 07:03 Yeah, sorry I'm late, I actually joined the wrong meeting link.
**Josh Suereth (Google LLC)** 07:07 Do we still have the…
**Daniel Dyla (Dynatrace LLC)** 07:07 old one.
**Josh Suereth (Google LLC)** 07:09 Where… where do we have the old one listed anymore?
**Daniel Dyla (Dynatrace LLC)** 07:12 We don't. I have it in my calendar still.
**Josh Suereth (Google LLC)** 07:14 Oh, okay. I tried to go through and delete it everywhere. Just for context, folks, we used to have an old Zoom link, so the new one's here. Alright. Yeah, so Daniel, you went through and modified stuff, so I don't know if this is still relevant. Do you want to give us a status update on the PRs?
**Daniel Dyla (Dynatrace LLC)** 07:33 Yeah, so there still are some, conversations that are, relevant.
Particularly, Jack asked us to add, like, a to-do on, on, Let's see, where is that?
**Josh Suereth (Google LLC)** 07:53 Let me see, where's the conversation button? Or is that only over here?
Isn't there a…
**Daniel Dyla (Dynatrace LLC)** 08:01 I've already made some changes, so I just wanna… let's see, David Ashpole asked to… if… asked us to add the skimmer URL to the entity fields list, which I did.
Jack Berg asked us to leave a to-do, for… On his question, like, how do attributes change over the lifetime of an entity, we said we want to just leave that open, but we're not specifying it for now, he wants us to leave it to do.
Which I have done, but not yet pushed.
Okay. I was working on this pier this morning.
I removed the conditional, like, when entity support is enabled.
Because it should always be enabled.
**Josh Suereth (Google LLC)** 08:46 Yep.
**Daniel Dyla (Dynatrace LLC)** 08:48 I added a clarification about what to do when identifying attributes are detected asynchronously.
There is a question that I had that's probably worth bringing up here.
There's two ways we can go about this.
We can… Attach… Entities to the resource that have unresolved attributes, so that, like, the processors see them, and they just see, like, a promise for the attribute or something along those lines.
But they have access to the rest of it.
or… We could not attach them to the resource until they are fully resolved, and then replace the resource So that any spans created after that time just get the new entity, which would potentially omit them from startup.
Or we could do a sort of combination of those, where we omit them in processors, but, you know, we have the whole thing resolved to a promise, but you can't inspect any of the synchronous attributes.
Right now, the way that I went, like, my first thought was to… Omit them from the resource until they're resolved.
But I'm not sure if you have an opinion on that, or… And because what I don't want is… For the non-resolved attributes, you know, partial identity, which then opens the door to, like, collisions in the future and confusion with processors and that kind of thing.
**Josh Suereth (Google LLC)** 10:44 Yeah.
**Daniel Dyla (Dynatrace LLC)** 10:45 Especially if the resolution eventually fails, then what do we do?
I feel like we shouldn't attach the resource until we're, like… Sure that it is correct.
**Josh Suereth (Google LLC)** 11:03 Yeah, the only use… so, you know that I have… I have, like, a use case that's, like, you know, important to me, which is basically, if you're using Node.js and you're running it in Kubernetes on Google Cloud.
our… if you want to look up your Google ID, it's actually an HTTP call to the metadata server to find out, like, what project you're in and that kind of crap, right? Yeah.
And so… you would end up with a resource where you'd… I think you'd know all about your Kubernetes things, but you wouldn't know… your GCP project at that time.
**Daniel Dyla (Dynatrace LLC)** 11:42 Your GCP project is a separate entity, so all the Kubernetes, like, anything that resolved synchronously would be there.
**Josh Suereth (Google LLC)** 11:50 Right, that's kind of what I'm thinking, is like, all the synchronous stuff would be there. There is a, like, cloud platform that would say that you're in GKE.
But that would be an independent entity.
the cloud, project account region, whatever the hell we have in there, we have, like, a bunch of those things, those would all be in the same. So I think, like, the entity being async is probably not problematic.
like, if you can inspect it, or look at it, or whatever. What I'm wondering is, though, if it gets attached later, is that problematic?
If it gets missed on the first export or whatever.
**Daniel Dyla (Dynatrace LLC)** 12:26 I… I think in order to have it not missed on first export, we could… attach… like, a… a non-inspectable… like, in JS, we would just use a promise. We would say there is an entity here.
Maybe with its type.
And, like, that would be it. Like, the processor would not be able to look at any of the attributes or anything like that.
**Josh Suereth (Google LLC)** 12:54 Yeah.
**Daniel Dyla (Dynatrace LLC)** 12:55 It would resolve at export.
**Josh Suereth (Google LLC)** 12:58 That's kind of what I'm thinking, is, like, we have a way where you can Take in the entities by type, and then you'd have to do conflict resolution across the… like.
If somebody… if there's two that have the same type, would you do conflict resolution generically, you know? Like, have a promise for each one, or do you pick one ahead of time and say, we're only going to allow the first promise that shows up for a particular entity type?
**Daniel Dyla (Dynatrace LLC)** 13:22 Yeah, so that's the ques… that opens a lot of questions about, like.
What is the priority? If it's first wins, is it the first attached, or is it the first resolved?
**Josh Suereth (Google LLC)** 13:34 Yeah, because if one fails, but the other one succeeds, or one succeeds, but returns no entities, actually, saying, yeah, I'm gonna resolve entities, but it turns out I'm not. Because, again, like, I think if you're… if you're being lazy, right, you just put AWS, Google, all of the… all the discoveries together, you just run, you know.
**Daniel Dyla (Dynatrace LLC)** 13:53 Yeah, and it's like, this is maybe an entity, but also maybe nothing.
**Josh Suereth (Google LLC)** 13:59 Exactly. And so, we don't want to reject the legitimate one, because we had to do a lookup and they didn't. And vice versa, if they don't have to do a lookup, they would always win, so we could never be there. Like, I think it's… That's why I feel like there has to be something where we can say there's a piece of this that's unresolved, and you can see the resolved bits, and we'll resolve the rest later.
You know?
**Daniel Dyla (Dynatrace LLC)** 14:21 You… do you want… So, like, I don't think there's a lot of risk in processors seeing partially resolved entities, but… The question is, like, what happens… if the resolution fails, I feel like we have to remove the entire entity from the resource, not just the failed attributes.
**Josh Suereth (Google LLC)** 14:42 Yeah, agreed.
**Daniel Dyla (Dynatrace LLC)** 14:43 We don't export any partial entities.
**Josh Suereth (Google LLC)** 14:46 Yeah, it would be, like, you either get the whole NC or get nothing.
**Daniel Dyla (Dynatrace LLC)** 14:50 Yeah, and then during resolution, which should only happen for, like, the first… export.
you see partial entities in your processor, and… you know, you just have to figure out how to deal with that. Because, like, the built-in processors, that's not a problem. They're not inspecting anything anyways.
**Josh Suereth (Google LLC)** 15:11 Yep.
If you're a custom processor, yeah.
**Daniel Dyla (Dynatrace LLC)** 15:15 we don't expect the, like, custom processors, what are custom processors doing? They're… they're… Adding and removing… they're adding, potentially, like, you know.
team tags and stuff like that. They're removing sensitive data. We don't want them to redact.
Identifying attributes in any way, really, if we can avoid that.
So… I think it's fine…
**Josh Suereth (Google LLC)** 15:43 Yeah, the only thing that I think would be happening in a processor, but we don't allow it today, would be throwing different entities in place because you're mutating based on context. But that's, like, the degen… that's, like, what we're trying to solve with, like, our… other SDK proposals, right? So… I don't really think that's a use case we should optimize for at all.
So yeah, I think most… most of the… We looked at this before, do you actually… I don't think you have mutable access to the resource.
Great.
**Daniel Dyla (Dynatrace LLC)** 16:15 in the process.
**Josh Suereth (Google LLC)** 16:16 a processor, I thought it's read-only.
**Daniel Dyla (Dynatrace LLC)** 16:19 I believe it is… read-only, but I mean… I guess maybe my brain is too mutated by JavaScript, but, like, there's… it's basically impossible to prevent anyone from doing whatever they want to do.
**Josh Suereth (Google LLC)** 16:34 Oh, I see, okay. I'm used to, like, stronger languages where, like.
Read-only and not read-only actually matter.
**Daniel Dyla (Dynatrace LLC)** 16:42 We can disallow stuff, like, in the spec and documentation and all that kind of thing, but at the end of the day, people are gonna do what they want to do. I mean, in the span start, you have more control, because, You can ignore… what… but… in, like, the span end, A processor could just… construct a new span from whole cloth, right? Like, a new span-like object, and send that to the exporter, and we can't stop them from doing that.
**Josh Suereth (Google LLC)** 17:12 Yep.
**Daniel Dyla (Dynatrace LLC)** 17:13 So, like, at the end of the day, they'll be able to do whatever they want to do. But I think it's not… Like, the official mechanisms to mutate resource are not there.
**Josh Suereth (Google LLC)** 17:25 Yeah.
Yeah, okay. Isn't it still the case, though, that span processor's the thing that calls the exporter directly?
**Daniel Dyla (Dynatrace LLC)** 17:33 Yes.
**Josh Suereth (Google LLC)** 17:34 So, like, you can do whatever the hell you want, really.
**Daniel Dyla (Dynatrace LLC)** 17:36 You can do whatever you want. I am not… yeah, I mean, that's, we don't need to…
**Josh Suereth (Google LLC)** 17:42 Yeah, I think… I think from that perspective, though, like, we give… we give read-only access. I think the processors that need to look at the resource, if we just warn them and say there can be, like, async partials here that you have to… You know, adjust for.
And so here's the shape of what it is. I think that can be handled as, like, a JavaScript-specific concern.
**Daniel Dyla (Dynatrace LLC)** 18:03 Yeah.
**Josh Suereth (Google LLC)** 18:03 And then languages that have blocking, we're gonna try to block resource detection, Before we continue.
Like we do today.
So, yeah. I… to me, to me, that works. So, like, I'm fine with that.
**Daniel Dyla (Dynatrace LLC)** 18:20 Okay.
**Josh Suereth (Google LLC)** 18:22 Are there… are there other things here that need to get addressed? We have the… what toggles? We're turning that off, right?
**Daniel Dyla (Dynatrace LLC)** 18:30 Yeah, like the when ST support is enabled, yeah, yeah, we're just saying it's always enabled.
Cool.
**Josh Suereth (Google LLC)** 18:35 And then, from existing resource mart spec…
**Daniel Dyla (Dynatrace LLC)** 18:40 Oh, there was a, there was a question about,
**Josh Suereth (Google LLC)** 18:44 Yeah.
**Daniel Dyla (Dynatrace LLC)** 18:45 the merge priority, and that needs to be resolved. So we had, like, Like, the merge order… let me find the… conversation that I'm thinking about.
**Josh Suereth (Google LLC)** 19:05 I think… yeah, I know exactly what this is, so here's the problem.
We all want an order and a priority.
But some of us put the new thing on the left and the old thing on the right, and some of us put the old thing on the left and the new thing on the right. And then we would just refer to them as left and right, basically.
And that became problematic. But more importantly.
If… are you assuming that the resource has been, like, generated and then a new thing shows up? Or are you assuming that you have everything kind of decomposed and are… doing stuff in priority order. So, like, I think the… the intention of both specs is compatible, the way they read is confusing as hell, because the existing spec basically assumes that you have, a fold, if you will, where the top is the… I think the top is the least important, the bottom's the most important, and then we wanted the opposite.
And so we just have to, like, clarify there's a priority order and you follow the order, but we should not specify whether first is higher priority or last is higher priority, in my opinion, because we need to, like, languages already have that decided in their configuration stack.
**Daniel Dyla (Dynatrace LLC)** 20:18 Yeah, first and last in the list, we don't need to specify, but this… the… it's… it's David Ashpole's comment in the bottom right of your screen.
**Josh Suereth (Google LLC)** 20:27 Yeah, this one… yeah, that's the one I was looking at. I tried to click to go… did it go to it yet? It didn't. I clicked the button.
**Daniel Dyla (Dynatrace LLC)** 20:33 telling them.
**Josh Suereth (Google LLC)** 20:33 jump to.
**Daniel Dyla (Dynatrace LLC)** 20:34 It's not in general.
**Josh Suereth (Google LLC)** 20:36 It's what?
**Daniel Dyla (Dynatrace LLC)** 20:37 We're calling them old and new, which I think is fine, right?
**Josh Suereth (Google LLC)** 20:41 Yeah, yeah.
**Daniel Dyla (Dynatrace LLC)** 20:43 Old and updated, is what we called them.
**Josh Suereth (Google LLC)** 20:46 And this was under the existing one, merge semantics, updating attributes take place over old ones, right?
**Daniel Dyla (Dynatrace LLC)** 20:52 Yeah, so that's, like, in the merge algorithm.
**Josh Suereth (Google LLC)** 20:58 Bro, here it is.
Must occur first, followed by resource estimate merging.
MC merging algorithm follows below, and we say… Sorted priority, where we say highest is first.
And I think that was the issue, is, like, if we had said lowest is first.
And then we had older places, new, it'd be fine.
Because when we say old and new here.
Old actually implies higher priority, because we said highest first instead of lowest first. But the previous algorithm had lowest first, and then old replacing new, or new replacing old was fine.
So literally, I actually think this one is just fixed by either the Like, saying, lowest is first.
Or, we have to change the actual algorithm to say that new, old, old is protected and new, you know, isn't, or whatever. Something stupid like that, but… Our intention was basically to be the same, it's just that I think somewhere we made that change.
**Daniel Dyla (Dynatrace LLC)** 22:03 Is it… would it be okay to just add, like… After the… after the algorithm definition here, just add a paragraph that says, for resource attribute merging, resource detectors must be merged, such that, like, higher priority detectors take precedence.
And just…
**Josh Suereth (Google LLC)** 22:27 I mean, we can say that. I think the thing, though, is where we say highest is first, and we talk about old and new, right? What we're… what we have going on here is, when we talk about old and new.
Old is always the higher priority entity, and new is always the lower priority one, right? And I think that is… this works if we do that, right? Because we drop the new entity.
If the Entities can be merged, we merge, otherwise we drop new, which means the higher priority one wins.
And here we at… yeah, so I think this is fine. Yeah, so we probably just need a paragraph that says, like, you know, previous algorithms, the first resource detector was the lowest priority, and the last one was the highest priority, so… We need to account for that in our merge algorithm.
**Daniel Dyla (Dynatrace LLC)** 23:10 I guess the question is, we run through that merge, and then we do resource attributes.
If there's a conflict, We want the one that was already there from the entity to win, right?
**Josh Suereth (Google LLC)** 23:24 We want the one that… You mean here, this thing?
**Daniel Dyla (Dynatrace LLC)** 23:28 Non-entity resource attributes?
**Josh Suereth (Google LLC)** 23:32 Non… yeah, we… we…
**Daniel Dyla (Dynatrace LLC)** 23:34 Should be always assumed to be the lowest priority.
**Josh Suereth (Google LLC)** 23:40 That's not actually how I did it, because I was trying to make sure we didn't break users that had other expectations. The way… the way… the way the Java one works is we actually… construct a resource each time and call the merge algorithm wholesale on every single instance of it. We don't do it decomposed, right? But we… we kind of do it decomposed. So basically, what's going on with entities is, this is the algorithm we have for entity, and then I think you… did you list the,
**Daniel Dyla (Dynatrace LLC)** 24:14 Oh, I see what you mean.
**Josh Suereth (Google LLC)** 24:15 environment separately?
**Daniel Dyla (Dynatrace LLC)** 24:16 These existing resource merge semantics, he's saying, like, before entities, like, what's in production today?
**Josh Suereth (Google LLC)** 24:23 Yes.
**Daniel Dyla (Dynatrace LLC)** 24:23 Updating attributes take precedence.
**Josh Suereth (Google LLC)** 24:26 Yes. And so, we actually… I actually implemented that, like, that's how the Java one works, because of how we actually do the merging. So, the only way you can provide, Detection is you provide a whole resource object.
So instead of providing, like, raw entities or raw attributes in Java, you provide the whole resource object, and then we merge. And the way we preserve highest order first is we always have, the new one be the thing you're merging into, like, if you will, for entities, so we drop the ones that aren't important.
And then the attributes from the new ones, since they're merged last, they will kind of override what happened from entities. So the idea would be, like, when I construct that resource, my raw attributes are only the ones that are still raw.
And those raw attributes, if they are conflicting with identity, Right?
then I have to drop the entities that use them.
But if they are descriptive attributes, I actually just put them into the entity descriptive.
**Daniel Dyla (Dynatrace LLC)** 25:30 Yeah.
Like, that…
**Josh Suereth (Google LLC)** 25:31 That's how I was doing shenanigans in Java, to try to keep things actually, like, you know, preserving the behavior that we had before.
**Daniel Dyla (Dynatrace LLC)** 25:40 Yeah, I see.
**Josh Suereth (Google LLC)** 25:42 So it's, it's mostly, it's just really confusing to describe.
**Daniel Dyla (Dynatrace LLC)** 25:47 Yeah.
But I think, so… Is that… what we have… Correct.
Construct a set, each entity aware, collect… Sorted by priority.
**Josh Suereth (Google LLC)** 26:14 I think for entities, this is correct. Where it gets confusing is when you have to mix entities with Attributes, and understanding that aspect, right?
So, because what we have here, we have this algorithm where we say, okay, and see, merging happens first, and you do resource merging semantics, and then after that, We have to merge in, raw attributes.
I think the way this is phrased… I think what we have is correct, it's just the way it's phrased is hard. Let's see, where do we have…
**Daniel Dyla (Dynatrace LLC)** 26:49 Yeah, like, I'm trying to think of, like, all the various edge cases, like, if you… if you… configure… 3 detectors… And the second one… Only has resource, and the first and third have entities, and all three of them conflict.
Which one should win?
**Josh Suereth (Google LLC)** 27:17 That's where this is supposed to answer that question, like, this part of the spec. Which is why I didn't want to have it near PR, I wanted to link to it, but everyone complained, so you added it, which is fine, but I would rather, like… we already agreed to all of this when we wrote the data model spec, so I'd rather, like, link to this, because…
**Daniel Dyla (Dynatrace LLC)** 27:36 Can I just strip the algorithm part out of my PR and link to this?
**Josh Suereth (Google LLC)** 27:40 That would be my recommendation, yeah.
And say, like, you need to be semantically compatible with this. You can implement it however you want, as long as the outcome Of your algorithm matches the outcome of this, right?
**Daniel Dyla (Dynatrace LLC)** 27:54 Yeah.
**Josh Suereth (Google LLC)** 27:55 But yeah, this is where… and this would answer it, so… when we solve for resource flattening, right, this is where we have the thing to make sure there's no duplicate attribute keys across entities. If there's a conflict, that use the same key, we remove the lower priority entity from the resource, remove attributes from attributes, which I exist in either description or identity, and… yeah.
This one's actually a little more aggressive. If you put a raw attribute in.
And it conflicts with either the description or the entity. We're actually removing it today in this algorithm.
I think we can… we can actually update that to only remove If it conflicts with the identity and not the description.
**Daniel Dyla (Dynatrace LLC)** 28:39 Then you have to remove the whole entity.
**Josh Suereth (Google LLC)** 28:42 Yeah, if it conflicts with… so right now, the way this is phrased, and the initial implementation we had in Java from, what, like, a year or two ago? That was, if we… if it conflicted with anything with the entity, we'd drop it, just to be safe.
We dropped the entity, not the attribute, sorry.
**Daniel Dyla (Dynatrace LLC)** 28:59 Yeah.
I mean, a part of me likes that, just because it's, like, it's providing, like a… an upgrade carrot, right? Like, a little bit of a… part of me wants to just say, like, if you ever mix and match, you lose all entity information, so… upgrade.
**Josh Suereth (Google LLC)** 29:17 That's basically what we have, yeah, okay. So, let's… let's not change this, but I think this answers all your questions, right? Because this has constructing the entities, having newest first, talking about how to do raw attributes, and then how to merge them into a resource. Like, we… I'd rather us just defer to this than try to rehash it again.
Because yours, this Performant Entity Data Model Merge, yours covers this, but I think it was missing this bit here, which is probably what's confusing everyone.
**Daniel Dyla (Dynatrace LLC)** 29:50 Yeah.
Okay.
Alright, I will point to this implementation, and we'll see… If that is sufficient.
I think that was the last,
**Josh Suereth (Google LLC)** 30:07 Yeah, I believe so. Let's go back, back, come on.
**Daniel Dyla (Dynatrace LLC)** 30:11 Yeah, because there were, like, 3 different places where it was, like, when the Entities are enabled, so those are all changed. Yeah, so those are all the changes that I have on my local, Oh, and then when I added schema URL to the field list, You know, David Ashpole asked us to do that a month ago, Should that also be reflected in the data model document?
**Josh Suereth (Google LLC)** 30:36 It should be. If it's not in the data bottle document, we should make sure it's there.
**Daniel Dyla (Dynatrace LLC)** 30:39 It's not in the table there, so I added a row to that table as well at the same time.
**Josh Suereth (Google LLC)** 30:44 Okay, that sounds good.
**Daniel Dyla (Dynatrace LLC)** 30:46 Okay.
**Josh Suereth (Google LLC)** 30:47 Cool.
**Daniel Dyla (Dynatrace LLC)** 30:48 Then I'll push this today, hopefully. Er…
**Josh Suereth (Google LLC)** 30:51 Awesome.
**Daniel Dyla (Dynatrace LLC)** 30:51 I'll definitely… I'm committing now, I'll push it today.
**Josh Suereth (Google LLC)** 30:56 Awesome. I will review it today, although you already have my approval, but I'll re-approve and make comments. I think the other one, I need to make sure mine's not gonna get closed.
This one… right. This one doesn't have any of our approvals, but it has… DC approval. This is the one that was using the, hotel Entities opt-in feature.
And I think… with your changes.
Let's just make sure we have…
**Daniel Dyla (Dynatrace LLC)** 31:32 I think we removed the opt-in behavior, right?
**Josh Suereth (Google LLC)** 31:35 I didn't remove it from this PR, I'm waiting for yours, because I'm going to merge yours in and then update it all together.
**Daniel Dyla (Dynatrace LLC)** 31:40 Yeah, so… Probably why nobody has… nobody from here has approved this PR, is because it's depending on mine.
**Josh Suereth (Google LLC)** 31:46 Exactly, yeah. So, and that's why I'm not merging it or not pushing to merge it until yours is through. So, I'll remove this, and then I think… what was this? Another thing about Strange, about having a feature flag, okay, because if we remove that, that's fine.
Process populates a single entity, fine.
Service detector name, is that intentional? Yes, it is.
There's a lot of people who are, we should talk about this. A lot of… there's a lot of confusion about the SDK environment variable configuration thing, where people keep treating, like, re… we had this before with OTL Entities, where, the resource that you are is not necessarily configuration. Like, configuration can say what your resource is, but the notion that you are detecting who you are from the environment versus the notion that it's actually configuration.
was running us into trouble, because we put a hiatus on new SDK environment variables for configuring the behavior of the SDK, right?
But we did expand environment variables to, like, send trace IDs, and this is what we're doing here, is we're using environment variables to propagate, you know, who you are, your identity.
Yeah, I mean…
**Daniel Dyla (Dynatrace LLC)** 33:12 The service name is arguably configuration.
Even though it is put into, I think it blurs the line a little bit.
**Josh Suereth (Google LLC)** 33:23 I think it blurs a lot, like, the hotel operator just fills it out for you.
from your Kubernetes deployment name, right?
So is that configuration, or is that propagation of your identity?
**Daniel Dyla (Dynatrace LLC)** 33:36 Right. Yeah. I don't know.
**Josh Suereth (Google LLC)** 33:38 But…
**Michele Mancioppi (Dash0 Inc.)** 33:39 It feels like a very academic discussion. It's a type of configuration that comes from the propagation of your identity, purely technically.
**Josh Suereth (Google LLC)** 33:49 Yeah, well, what we don't want is we don't want to fall afoul of the no new configuration environment variables. And they're all deprecated, don't change them. We want to keep using it, and we still want it to be useful. So that's why I'm trying to make the distinction, but I hear what you're saying.
**Michele Mancioppi (Dash0 Inc.)** 34:04 I would actually… I would very… so, the whole point with the detection resources, you know, it's near and dear to my heart.
the, one route one could take is, in the specs, there is a section that, defines the named service detectors.
**Josh Suereth (Google LLC)** 34:27 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 34:28 Service is one of them.
And, what does not have a moratorium He's introducing a new one.
Something called, for example, the Entities Detector.
So you could define the behavior of an entity's detector as the detector that reads auto underscore entities.
And sets it all up correctly.
**Josh Suereth (Google LLC)** 34:52 That's… that's what we have here.
**Daniel Dyla (Dynatrace LLC)** 34:54 That's what it is, yeah.
**Josh Suereth (Google LLC)** 34:55 That's what this PR is. It doesn't call it the Entities Detector, it calls it the ENV detector, as in, I detect entities from the environment.
**Michele Mancioppi (Dash0 Inc.)** 35:05 Yeah, I don't love that.
**Josh Suereth (Google LLC)** 35:07 If you want… if we want to rename it, I'm fine. Like, the name isn't important to me. It… the fact that, A, you can configure it, and B, it pulls from the environment are the two important things.
**Daniel Dyla (Dynatrace LLC)** 35:17 The names… the name is… is not super important, but I think calling it the Entities detector is a mistake, because Entities can come from all kinds of other places.
**Michele Mancioppi (Dash0 Inc.)** 35:28 Yeah, the name is very important, because we end up exposing this in the declarative configuration, and nobody will guess.
that DM detector sets the entities.
**Daniel Dyla (Dynatrace LLC)** 35:40 Well, it's an EMV entity detector, so they will.
**Josh Suereth (Google LLC)** 35:45 We could… we could just call it ENV underscore Entities, and I'm fine with that, too, as a name, because then it implies both that it comes from the environment and its entities, but…
**Michele Mancioppi (Dash0 Inc.)** 35:54 Nevertheless.
We actually, for example, the service detector, by this logic, should be called EMV underscore service, right?
**Josh Suereth (Google LLC)** 36:02 That's… that's fair, because we only get the values from the environment. Yeah.
**Michele Mancioppi (Dash0 Inc.)** 36:08 I would…
**Josh Suereth (Google LLC)** 36:09 This, by the way, changes that detector where it will be producing service entities.
**Michele Mancioppi (Dash0 Inc.)** 36:17 Come again.
**Josh Suereth (Google LLC)** 36:19 So, it'll still be creating the same attributes that you expect, but it'll be producing entities for service, instead of just the attributes.
**Michele Mancioppi (Dash0 Inc.)** 36:29 Yeah, okay.
It's… I don't think that is… so the… my… my… my concern… is not… As much what it does, but how well a user that is not Weekly taking part in the SIG can guess what it does based on the name.
**Josh Suereth (Google LLC)** 36:46 Yes.
**Michele Mancioppi (Dash0 Inc.)** 36:46 And that is particularly important because of the discarded configuration where this needs to be exposed. If it were just an internal detail of the SDKs, I wouldn't even mention it.
**Josh Suereth (Google LLC)** 36:58 Agreed.
So, I think the thing, though, is if you call it a service detector.
And you have to set environment variables.
maybe calling it end service is easier for people to understand, because you're not saying, I'm detecting service the way, like, Prometheus service detection works, or service discovery. I literally require environment variables, you know? I'm not… there's not, like, an API I'm hitting, you know?
**Michele Mancioppi (Dash0 Inc.)** 37:22 Yeah, but this argument is no longer valid.
entirely since I got my PR merged that allows the surveying languages to implement language-specific… Ways of determining what the service is.
Like, for example, looking up in the… in the meta info, In the meta…
**Josh Suereth (Google LLC)** 37:45 Oh, so it's not environment anyway? Yeah, that's fair, that's fair. So yeah, it's.
**Michele Mancioppi (Dash0 Inc.)** 37:48 a great environment.
**Josh Suereth (Google LLC)** 37:50 I agree with the point, and that's why we're moving towards having a process detector, a container detector, host detector, service detector, right? They're all listed here. This is just making them all entity aware and saying which entities it produces, which then implies what attributes are produced, and this is all non-breaking.
And it adds the env one, which pulls the hotel entities environment attribute. If we want to call it envities attribute, I don't care. I think that this has to be here. I think env is fine, personally. I do think we have to handle Dmitrii's concern here.
which… I'll do a… once Dan's PR is merged, I'll do a write-up here. I do need to drop, unfortunately, so… Because I do have a conflict that I was able to slide, but not get rid of.
Okay.
**Michele Mancioppi (Dash0 Inc.)** 38:44 without any…
**Daniel Dyla (Dynatrace LLC)** 38:44 Any other topics on the agenda?
**Josh Suereth (Google LLC)** 38:46 There was nothing.
Yeah, it was… it was literally just… the other thing I wanted to confirm, is that we are planning not to do an opt-in, and that we don't consider it a breaking change, and I think we'll have to get… roll the prototypes out with that. That's a discussion I want to have at the spec meeting.
a reminder of the spec meeting tomorrow. Like, I'm hoping, Dan, if you get this PR up to snuff, we'll get it merged, we'll talk about the spec meeting, and we'll remind everyone of this, and so that we can actually get, complaints about it early, because I do expect there to be some angst.
**Daniel Dyla (Dynatrace LLC)** 39:20 I'm obviously okay with this, since it was my idea in the first place. I think the spec meeting was where I first brought it up, and we got people that… nobody specifically complained about it, I think we had a lot of people say, I have to think more about that, and that was kind of the…
**Josh Suereth (Google LLC)** 39:36 Yeah.
**Daniel Dyla (Dynatrace LLC)** 39:36 The final.
**Josh Suereth (Google LLC)** 39:38 I think it's FUD at this point. Like, it's 100% FUD, so I think once we… if we actually get PRs that make… that do the changes for the spec, like, where we actually have entity support in the SDK, and it's non-breaking, and all the tests pass with no changes, and then once we have, PRs that add the entities to the resource detectors.
Right? And all tests pass without breaking, that's when I think people will be like, oh, okay, this is cool. But until those actually show up, people don't know, and so they'll block it.
Just out of, you know, emotional reaction, no… over anything else, so… That's why I want to get to the point where we actually have these prototypes landing based on the PR. So let's try to get your PR in.
try to get my PR in, and then we'll update all the prototypes so that it's, like, obvious what's going on.
**Daniel Dyla (Dynatrace LLC)** 40:27 Okay.
**Josh Suereth (Google LLC)** 40:29 Okay, I have to drop. If you guys want to discuss anything else, I saw Dmitri showed up. If you want to talk about collector things, please do. And yeah, look forward to seeing y'all next week, and Dan, Let me know as soon as that's ready to review, because I do want to talk about it tomorrow in the spec meeting.
**Daniel Dyla (Dynatrace LLC)** 40:45 Yep, upping.
**Josh Suereth (Google LLC)** 40:46 Alright.
We'll see y'all.
**Daniel Dyla (Dynatrace LLC)** 40:49 Yeah.
Anyone have topics to bring up, or is that it?
**Dmitrii Anoshin (Splunk Inc.)** 40:56 No, nothing from my side this week.
**Michele Mancioppi (Dash0 Inc.)** 41:01 I have one quick question. Sure. Besides, Dmitri's work on the collector.
Are you folks aware of any, work ongoing in the language SIGS about Entities?
**Daniel Dyla (Dynatrace LLC)** 41:14 There are prototypes in… JavaScript, Java, and Go.
Is there a Python one, Dmitrii? Am I remembering that correctly?
**Dmitrii Anoshin (Splunk Inc.)** 41:27 I haven't heard anything about it.
**Daniel Dyla (Dynatrace LLC)** 41:29 Yeah.
That's the only work.
that I'm aware of, is to the prototypes that we've been doing.
**Michele Mancioppi (Dash0 Inc.)** 41:37 And, did you speak with Jack, for, so I… my expectation is that after this PR that you just discussed.
Then, another PR appears for the declarative configuration.
Because the quality configuration treats.
Some, resource detectors as first-class citizens, and the others don't exist.
And this one feels like the kind of detector that should be treated as a first-class citizen.
**Daniel Dyla (Dynatrace LLC)** 42:13 Yeah, well, the environment detector will be, certainly.
**Michele Mancioppi (Dash0 Inc.)** 42:19 That's what I meant.
**Daniel Dyla (Dynatrace LLC)** 42:20 think that probably will be the only one for now. But we'll see, that's… I, I think that Ed… a first step, I think that'll be the only one.
**Michele Mancioppi (Dash0 Inc.)** 42:35 That would be absolutely fine. Also, the way I understand it.
The plan is that existing named resource detectors Are learning how to send entities, and those are going to be the service, the process, the host.
which is 1 to 1, the list of named service detectors in the clarity configuration, so that bit doesn't need change.
**Daniel Dyla (Dynatrace LLC)** 42:59 Yeah, and I think that they will, yes.
**Michele Mancioppi (Dash0 Inc.)** 43:03 Excellent.
Man, I have no more questions, Your Honor.
**Daniel Dyla (Dynatrace LLC)** 43:09 Okay.
I guess that's it, then.
I'll see everybody probably in the spec meeting tomorrow.
**Dmitrii Anoshin (Splunk Inc.)** 43:17 Oops, bye.
