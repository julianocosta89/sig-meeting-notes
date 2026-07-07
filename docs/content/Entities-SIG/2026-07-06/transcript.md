SIG: Entities SIG
Date: 2026-07-06
Duration: 52 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 03:37 Hey! How's it going?
**RC Robert Cowart** 03:42 All right.
**Daniel Dyla (Dynatrace)** 03:43 I'm good. How are you doing?
**Josh Suereth** 03:46 Not bad, not bad. I want to go back on vacation, man.
**Daniel Dyla (Dynatrace)** 03:50 Yeah, same.
I went tubing for the first time in, like, 10 years this weekend. Maybe 15, a long… I don't know, forever. And my body is destroyed. But it was so fun.
**Josh Suereth** 04:06 That is rough. Yeah, yeah, yeah. Did you. Did you do any of the other, like, water sport things or just dubbing.
**Daniel Dyla (Dynatrace)** 04:12 Oh, we, we do everything. We have, we went surfing a little bit. We have, Like, a surfboard with an air… with a waterfoil underneath it.
That stands up out of the water, and we have one of those attached to a chair as well.
**Josh Suereth** 04:28 Oh, that'.
**Daniel Dyla (Dynatrace)** 04:29 Trying… trying to learn how to backflip.
**Josh Suereth** 04:32 Okay.
**Daniel Dyla (Dynatrace)** 04:33 Yeah, I mean, we… our, Well known on our lake for having all kinds of stupid toys.
To pull behind boats.
**Josh Suereth** 04:46 That's fun, man. That's fun.
Okay.
I, yeah, I had… I had a less exciting one, but for, it was… we had that heat advisory.
**Daniel Dyla (Dynatrace)** 05:00 Yes.
**Josh Suereth** 05:01 I now have a pool table that was like a birthday present. That converts into ping pong. We had the whole family over during the heat advisory in our very cold basement, relatively cold, meaning it was 10 degrees cooler than outside.
Yeah, that's what we spent our 4th doing.
**Daniel Dyla (Dynatrace)** 05:22 Nice.
**Josh Suereth** 05:23 Yeah, let's do, I want to talk about SDK changes. So… I don't think I'm presenting yet. We'll get into this. It might be a small one. If you have any topics, please add them to the agenda.
I don't know… you weren't here last week, Daniel, but.
**Daniel Dyla (Dynatrace)** 05:44 I was not here last week, and we skipped a couple before that, so I am probably more out of the loop than… I should be.
**Josh Suereth** 05:55 Right, so we walked through, the Java implementation, and I wanted to just call out a few things, so… Because I want to make some SDK spec changes here based on this Talk. We're actually pretty close to getting approved.
So, it's still reminding me I have to update all my comments. Thank… thank you. Anyway, one thing is… I am doing a thing where if experimental entities enabled environment variables turned on, then resource detectors will produce entities, otherwise they won't.
**Daniel Dyla (Dynatrace)** 06:30 Mmhm.
**Josh Suereth** 06:30 And that's and everything else is invisible to to people, right?
So that's how it's, like, showing up. The other thing is, Right, whether or not entities can have an empty ID, I need to go update to basically make it more restrictive for now until we make a decision.
Where was this one?
**Daniel Dyla (Dynatrace)** 06:51 Did he have an example for an empty ID?
**Josh Suereth** 06:55 No, he doesn't want one with an empty ID. I was the one that gave an example of this host ID problem.
We don't.
**Daniel Dyla (Dynatrace)** 07:03 Yeah, okay.
**Josh Suereth** 07:04 The host collector, detector.
that provides IDs. We think someone else has to provide the ID.
**Daniel Dyla (Dynatrace)** 07:11 Okay.
And then you would just attach to if a host entity already exists.
**Josh Suereth** 07:18 Yeah, so basically, I almost provide descriptive attributes, and then merge them into the thing that provides the ID.
**Daniel Dyla (Dynatrace)** 07:25 Yeah, it's almost more of like entity enrichment than it is entity detection.
**Josh Suereth** 07:31 Yeah, that's… so that's… that's a thing to talk about later. That's not what I really wanted to get into.
**Daniel Dyla (Dynatrace)** 07:38 Yeah, okay.
**Josh Suereth** 07:38 I was, parameter assessed What did I? There was something about the specification. Oh, here.
So, one of the changes, We have in the, in the, in the spec.
I showed the data model where we have attributes and, resource, and in my change, I call something raw attributes.
Because Java already defines an attributes member on resource, and it is everything, not just the loose ones.
**Daniel Dyla (Dynatrace)** 08:12 -H.
**Josh Suereth** 08:12 Not part of entity, and we need a name that refers to the loose ones for all of our algorithms to work.
so that you can directly, you know, address the attributes that are part of entities and the attributes that are by themselves, you know, in the merge algorithm. So, I would like to make a PR, this is the whole point of this discussion, in here.
We talk about SDK-provided resource attributes, resource creation, and the key thing here is Retrieve attributes is a method that is supported on resource in the stable documentation.
So what I want to do is go update this to say it retrieves all attributes regardless of whether or not they're on entities or not. And then I was going to say as a experimental resource operations, there should be retrieve entities.
And possibly retrieve, I don't know if we want to call them loose attributes, if we want to call them raw attributes, like, they need a name to say… Yeah.
**Daniel Dyla (Dynatrace)** 09:16 Unassociated or something.
**Josh Suereth** 09:18 Sure, yeah. But that name is then what Java wants to use. So I'd like to actually make the SDK spec so we can get the Java SDK merge or PR merged, because I still have to go update a few resource detectors in a different repo. But I need to update the Java one first before I update the other one.
you know, all that kind of fun. But the Java one is almost good to go and good to merge, so I think we're actually in really good shape, we just need to update this.
So, the question would be, if I were to go add a couple resource operations here.
Does that conflict with anything that you have going on, Daniel, for specs?
**Daniel Dyla (Dynatrace)** 09:57 No.
**Josh Suereth** 09:59 Okay. Should… so, I can do that as a separate PR?
**Daniel Dyla (Dynatrace)** 10:03 Yeah, it should be totally fine.
**Josh Suereth** 10:04 Cool.
Any concerns with that, or thoughts?
**Daniel Dyla (Dynatrace)** 10:11 Other than the obvious naming bike shed, I think it seems reasonable to me.
**Josh Suereth** 10:18 What name do you want to suggest? I actually do that.
**Daniel Dyla (Dynatrace)** 10:21 I don't know. I think loose and raw are too colloquial of terms.
You know, I think as native English speakers, people, we may know exactly what that means immediately, but somebody else might not. And I prefer something that more explicitly means what it's called.
**Josh Suereth** 10:43 I'll just put unassociated for now.
I think you mentioned that.
**Daniel Dyla (Dynatrace)** 10:48 Yeah, I think unassociated is fine. It's a little bit less, you know, friendly sounding, but it's more technically accurate, I think.
**Dmitrii Anoshin** 10:58 Yeah, it's for attributes that are not associated with any of the entities on the resource, right?
**Daniel Dyla (Dynatrace)** 11:04 Yes.
**Dmitrii Anoshin** 11:04 Okay, sounds good.
**Josh Suereth** 11:07 Yeah, in fact, I think… what do we call them in,
**Dmitrii Anoshin** 11:11 Oracles.
**Josh Suereth** 11:13 Is, shoot, that's in the resource data model.
**Daniel Dyla (Dynatrace)** 11:18 Urge.
**Josh Suereth** 11:18 Yeah, we just, we literally call them additional attributes, as opposed to unassociated.
**Daniel Dyla (Dynatrace)** 11:23 I'd be okay with additional attributes, too.
**Dmitrii Anoshin** 11:29 Maybe.
**Daniel Dyla (Dynatrace)** 11:29 Either is fine.
**Josh Suereth** 11:32 Okay.
**Dmitrii Anoshin** 11:33 What do you think about common attributes? The kind of.
**Daniel Dyla (Dynatrace)** 11:37 I think common… If I didn't know anything about hotel and I was coming in, I might think common means associated to all entities. It's like the opposite.
**Dmitrii Anoshin** 11:47 Kind of.
Why, why is that the opposite?
**Daniel Dyla (Dynatrace)** 11:51 And we want them associated with no entities, right? Like, it doesn't necessarily describe a host, it might describe… I don't know, some network, something.
**Dmitrii Anoshin** 12:01 Yeah, but in that case, network. So we are talking about, like, the gaps in entities here, or we're talking about some generic attributes that are applied to potentially all of the entities on the resource, because they are those kind of 2 separate things in that case, right?
**Daniel Dyla (Dynatrace)** 12:19 We're mostly talking about Backwards compatible, like, you know, there are already resource detectors around that may overlap with some entities and may not.
And… custom attributes that some application author creates that don't… don't, Belong in any existing defined entity.
**Dmitrii Anoshin** 12:46 I'm thinking about examples. And this is so far what comes to my mind that we like would potentially keep long term, even like not considering the gaps, but actually considering something that can be can live without entities. For example, under cloud namespace, right? Cloud. Cloud. You like them, Josh?
Yeah, you're.
**Josh Suereth** 13:13 Like, one of the hardest, or most greatly.
**Dmitrii Anoshin** 13:16 Yes.
Right, exactly.
**Josh Suereth** 13:18 Semconf? Yes. Sure.
**Dmitrii Anoshin** 13:20 like those kind of generic attributes that are not associated with any entities. And if we think about them, they are actually common to all of the Probably entities, they can be applied to all of the entities.
To some extent.
Anyway, I don't think an association cannot even be lost.
**Josh Suereth** 13:45 I was actually… I was planning to make entities for cloud at some point, because I think it kind of makes sense.
But the way that we've designed cloud attributes is problematic because, like, at least for GCP, there are cloud attributes that you… If you fill them out, you get a misinformation about what you're looking at.
Basically, because GCP doesn't do full region isolation the way other clouds do, that cloud region or availability zone is problematic, because if you put cloud availability zone in, it's talking about one of the entities, not all of the entities.
That you're talking to, right? Because I can be on a VM that's managed by something in a different availability zone.
And how do I represent that now, right?
**Dmitrii Anoshin** 14:36 That availability zone is not a common attribute.
**Josh Suereth** 14:41 That availability zone might not be a common attribute or, you know, yeah, so, so, but we have to, we have to define that. It could be that that availability zone becomes a descriptive attribute or even identifying on like other cloud things that we decide, right? So we could, yeah, anyway.
**Dmitrii Anoshin** 14:58 So my question here, like our long-term model, do we even consider that we will still have valid use cases for attributes that are not associated with any entities, or we will ideally want to have all of the attributes associated to any… at least to one entity, or, like, any of the entities. And then… and unassociated will be left for the gaps and backward compatibility.
I think we need to answer that question.
Well.
**Josh Suereth** 15:33 Yeah, I was going with an exploratory phase of, let's assume that everything can be associated with an entity until we have a good use case where it's not, and then we address that use case.
**Daniel Dyla (Dynatrace)** 15:45 I had also… kind of been making that assumption as well. It has been my assumption from the start that we want to get rid of unassociated attributes where possible.
**Dmitrii Anoshin** 16:00 Okay.
So in that case, like, everything under cloud should be… This is broken down somehow and associated with every entity, because that was Yes.
I was.
Say, you're complicated.
**Josh Suereth** 16:20 Yep.
**Dmitrii Anoshin** 16:22 Cool, thank you.
**Josh Suereth** 16:23 Okay.
**Dmitrii Anoshin** 16:24 Okay.
**Josh Suereth** 16:25 No.
Cool. So, that's… Yeah, I… I was just showing… we have… we have Luce in the spec already, so if we don't like the name Luce, I need to fix it everywhere, but I will… I will take the AI to, Create PR spec with changes to get Java.
I would say.
Submitted.
upstream.
Okay.
Cool. Next, Rob, do you want to talk about network entities?
**RC Robert Cowart** 16:59 Yeah, I mean, this is more just, I'll say, introductory more than anything else. You know, I think you may know Josh, but I don't know if others, if the other two guys know that, you know, we are getting this network SIG kicked off.
And, the first thing we want to do, I guess our intuition is right because of the conversation just there about attributes associated with entities. We said, hey, let's first And we'll be discussing this next week. The kind of the first pass is like, let's first identify the network entities that we're going to start with.
Our initial focus is going to be on, we'll call it, enterprise data center WAN stuff, because You know, when you get into network, like you got, for example, the whole carrier side of network, which is then completely different than what the customers of the carriers, the enterprises.
actually see or care about. So, you know, we figure it makes the most sense just to focus initially on enterprise data center WAN, not even campus initially, you know, just to keep the scope a little tighter, gonna focus on what we believe those entities are, and then we'll be coming back here to the group. So, right now, I'm just eavesdropping, learning as much about the entity's effort as I can, and then you know, expect some submissions and things, and in the coming… probably within the next 3 or 4 weeks, I'd say. The first pass of… of stuff. We understand there's already a few things related to network that are, like, under system.
like network interfaces and things like that, you know, we want to try to respect whatever's in places, if, if it makes sense to do so, obviously, but, yeah, so, I guess just kind of introducing to the group to say, this is going to be coming, and any… any tips or anything you want to point me at, or the group at, you know, You know, still eating up and stuff, so, yeah.
**Josh Suereth** 19:03 Yeah, I'll show you two things. So first off, if you haven't seen it, in Semantic Conventions, we have a registry of all entities, but here's what I'll say.
If you look, all of these are in development, like, most of them. So these are in RC.
But most of these are in development. The Kate's ones, I think, are actually pretty close. It's moving into RC, process just moved into RC, right? Service and distro are stable, but if you see things network-related in here.
I am not aware of a path for them to become stable without someone actually taking action on them, and driving them towards stability, and answering all the hard questions. So, like, feel free to take ownership and drive these things to stability when you say, cool, I think we've modeled the problem correctly now, we think we've addressed key use cases, that sort of thing. That's, like, we need that here. That's one of the big things with getting these things to stable.
We need a path to get all the resource attributes, if you will, or entities marked as stable. The other thing is we have this, I think it's under non, it's how to write conventions. We wrote a resources and entities guide for doing semantic conventions about how to think about them, how to model them, different questions. What we'd love is you know.
as you're working on this, read the guide, and then where the guide is not clear, or the English is poor, or whatever, ask tons of questions here, because we'd like to, like, go fix that, and make sure that that is useful for everybody going forward, yeah.
**RC Robert Cowart** 20:42 I think one of the good things already is that, at Elastiflow internally, there's another gentleman in his company in France that also has had a similar effort internally.
And what's here as far as this idea of entities and relationships where it's like is a that kind of like 3 independently, all kind of came to the same conclusion on how to do this. So I think at least we're already thinking in the right path.
from what I've seen so far, but no, this is good, good tips, so, yep.
The other thing that Braden, who's kind of helping us out as we get going, said, you know, that there, and that now it makes sense now that I see how much stuff is still in progress, that he said, like, on the system side, there were a number of enhancements or expanding a little bit some of the scope to be able to create some of the relationships that were necessary. I haven't been through all of that, those yet that are available, but I imagine we might have… for example, we have things, like, tunneled through.
you know, like in Kubernetes, maybe you have, like, a flow of traffic is tunneled through a VXLAN tunnel, is, you know, that type of stuff. So there could be some even relationships that come out, but, you know, we'll try to stay where What makes sense, what's already there, and then see what makes sense beyond that, so…
**Josh Suereth** 22:11 Yeah, regarding relationships, that's Dimitri's the one who wrote the specification around like the first set, but I think they can be relatively flexible. So yeah, that's an example. That's a perfect example of a relationship that, you know, if we if we needed to support, if I recall correctly.
Where are they?
Yeah, the type is a string, and there's this notion of standard relationship types. If there are… You know, you may define.
domain-specific ones, but if there's one that we think are, like, so common that everyone who does network monitoring needs, like, we haven't set up a place to, like, write these down. Yet.
**RC Robert Cowart** 22:52 Okay.
**Josh Suereth** 22:53 So what I don't want to do is force you to go through a frickin' spec PR every time you have to define a new one. So, like, for now, just make sure they're written down somewhere, it would be my recommendation. I don't know what you think, Dimitri, like, where we want to store those, or like, if we have new relationship types, what… Yeah, that's what I.
**Dmitrii Anoshin** 23:11 Sounds good to me, I think that should be… for beer.
specific seek to define.
**Josh Suereth** 23:19 Yes.
But that, that sounds exactly like the whole, you know, what we're trying to go for here, so that's awesome.
**Dmitrii Anoshin** 23:27 And it's still like a pretty experimental.
space, right, for the relationship. It's good to define them, but it doesn't mean that they will stick with the specific names.
**RC Robert Cowart** 23:44 Cool, alright, well, so I guess you'll probably see me around more often here in the coming weeks and months, so, yeah.
**Daniel Dyla (Dynatrace)** 23:53 Always happy to have contributors.
**Josh Suereth** 23:56 Yeah. McKellie, do you want to. You can just jump in.
**Michele Mancioppi** 24:00 Yeah, but it would take the discussion off track, so I can wait until this discussion is exhausted.
**Josh Suereth** 24:06 Okay, okay, cool, cool, cool.
But… Yeah, so yeah, just to end that discussion. If you have any other questions, let us know. And really excited, man. It's good to see more work here.
**RC Robert Cowart** 24:19 Cool.
**Michele Mancioppi** 24:26 Don't be, don't be so dramatic. It's just a small question.
**Daniel Dyla (Dynatrace)** 24:29 Okay.
**Michele Mancioppi** 24:30 I have seen Josh had tabbed into a page that said that there is an entity ID, an entity type.
And I was wondering… Why not the name?
Why not?
**Daniel Dyla (Dynatrace)** 24:46 What?
**Michele Mancioppi** 24:47 a name.
**Josh Suereth** 24:50 So.
**Michele Mancioppi** 24:50 Let me explain the background of this question.
in Derstero, we had entities before this, in fact, we built an entity system before the SIG actually was a thing. And, we started with a Derstero.resource.id.
and then we added a type, and then we added a name to provide effectively a kind of stable identity for the entity itself, that would be human understandable.
And then we see… Is that…
**Daniel Dyla (Dynatrace)** 25:23 Is that replacing the ID, like… something to reference this specific instance of this entity, or is it to replace the type to say, I am specifically referring to this Like, type of entity.
**Michele Mancioppi** 25:39 It's a human readable alias.
With no pretense of uniqueness.
The ID is unique. The ID is the actual identity.
The name, for example, index 0 pod is identified by k.pod.uid.
That is what we use to calculate that there's zero resource ID for pods. And the name is the value of Kate's pod name.
**RC Robert Cowart** 26:05 So, like.
**Michele Mancioppi** 26:06 Because I think there's a catch with pod Yeah, a human readable name, yeah.
**Josh Suereth** 26:11 So, so, yeah, should we have a human-readable name be passed on OTLP all the time? My, my thinking here, McKellie, and I could be completely off, is that, entity type, there should be a easily expressible formula that says, here's how you grab a human-readable name for this type.
For all entities. That'd be awesome. And then it wouldn't have to go down OTLP all the time, you could just look at the type and say, okay, this is a GCE container, here's how I construct a human readable string, and it's off-band, like, not in the OTLP. If we need it to be in the OTLP, that's sent every time, that's a different story. But that was my thinking there. Like, we could even have it in semantic conventions as a thing that we record somewhere, that we say, here's how to compute human-readable names from entities. 100% would be really happy to explore that and do that.
The reason it's not in the document I showed, which I'll show right now, this is, like, the data model for what's going to go… or this is the relationship data model. This is actually describing what goes in OTLP.
So this is what's sent over the wire every single message. So what you're suggesting, 100% agree with, and I think there are other ways for us to solve it, where, I'm happy to put it in SemConf, I'm happy to have it part of the SemConf schema URL you could pull in.
But, you know, does it need to go down OTLP every single time, or is it inferred from what's already there? I was thinking the latter. If… if that's amenable, I think let's… let's explore it. That sounds good.
**Michele Mancioppi** 27:40 I would indeed expect that when we define the entities and the semantic conventions, then we make a non-normative suggestion of what a good entity name is.
**Josh Suereth** 27:50 Exactly. It could even be semi-normative of like a should, not a must.
**Michele Mancioppi** 27:55 Yep.
**Josh Suereth** 27:57 Yeah, go.
**Dmitrii Anoshin** 27:57 That's all. That sounds pretty good. Yeah, sounds reasonable to me. We should do that. And I think we can make it like.
part of Weaver to specify the rules for particular entity types. I think we should also say that whatever attribute is being used to deduct the name should be probably require that review to that case.
**Michele Mancioppi** 28:22 Okay.
**Dmitrii Anoshin** 28:23 Recommended, at least.
**Michele Mancioppi** 28:25 Commander Jeff.
Recommended.
If you're curious, we actually publicly document all of this.
In, here, and, related pages.
We are missing some entities. For example, Dextero doesn't really have an entity for process. We start from the pod.
For technical reasons.
But… There, those you can just take and reuse wholesale.
They… they work.
And there is also one one more thing.
At the moment, you have entity ID and entity type. So in the entity model.
Those things are sent all the time.
I don't think we need to send all the time to type.
it's, it's, enshrined in which attributes are part of the entity ID.
The way we solve that problem is to have a series of rules with precedence executed serially from top to bottom, and the first that matches wins.
**Josh Suereth** 30:32 Yeah, I'm worried about the scalability of that if we end up with an explosive amount of entities or an open ecosystem, right?
**Michele Mancioppi** 30:40 Yeah, I can tell you it's just a little tiny bit like this. We have a processor in there, Sarah.
that does it. It's easy to optimize. It has Early in the morning, so…
**Josh Suereth** 30:52 what I'm suggesting is, okay, Dash Zero, you can write that processor, right? But now, I am, you know, a Joe Smoe company, and I have my own thing that runs code, because I… Built stuff and, you know.
That's how I roll, so I have some sort of hard, weird ecosystem, and I define my own entity for that thing that I built.
And I'm reporting data against it. How do you interact with it? How do you know it exists?
**Michele Mancioppi** 31:20 But then let me turn, let me play a Nuno card, a reverse Nuno card on you. Why are the treating type different than name?
Why is type required and name is not? Why are we happy with a semi-normative name, but the type is required all the time?
**Josh Suereth** 31:36 Good question. I think, So there's two things here. One, type is effectively already encoded in the ID attributes based on how we do namespacing. So I think it's realistic to say that we could drop it if we think that the information's already encoded. But that is actually just a thing we only require OpenTelemetry to do, that's not a thing we're requiring everyone to do.
But it's… it's a decision we could push on.
But you need to know, like, you need to know the type in some fashion. If you can derive it from other information, I think that's fair, if you can consistently derive it. What I'm suggesting is I don't know if you can consistently derive it.
And the other thing is we actually interact with it directly in our merge algorithm.
So, I need access to the type to do merging correctly. Like, the reason why it's in OTLP is because we actually interact with it at that layer. If I didn't need to interact with it at that layer, I could have it be external, I wouldn't put it there at all.
Like, that's… like, in terms of principles here, that's… that's kind of what… what… what my… how my thinking is. If I… if I have to interact with it in OTLP, to be correct, from anyone engaging with this thing.
it should be in OTLP. If I can do it externally, I can move it externally. So the real question is, do we think we could move type to be something external, still have all our behavior work correctly? If that were true, then I'd say we could remove it. Go ahead, Daniel.
**Daniel Dyla (Dynatrace)** 33:02 Yeah, there's two things. One, the aforementioned processor.
it does depend on it being always up-to-date all the time. Like, you… if a new entity type is introduced, then… You would lose, you know, the processor wouldn't know how to deal with it.
it's the same problem as custom entities, but it's just, like, you know, what if I enable some instrumentation that is more up-to-date than the processor that I'm using? What happens with that?
And then I think the, the second part is.
If we say we could derive that from Semantic conventions and create a processor for it.
The the logical extension and conclusion of that is all of entities could be defined as a convention, and we could just go right back to having a bag of attributes on resource.
And call it a day, and we're not doing that.
So I think we've already accepted that some level of structure is.
I… And.
Desirable.
And then it's just a line drawing exercise of saying, yes, this could technically maybe be defined as a convention, but we think it provides value by not.
And I think the ID provides value not just from the merge algorithm, but just purely from an ergonomic standpoint of like, when I look at the data, I can see that it's a logical grouping and it has a name.
Whether it's a name or an ID or both.
I think having something there is important.
**Michele Mancioppi** 34:47 My argument was not about getting rid of entities or making it only semantic conventions.
**Daniel Dyla (Dynatrace)** 34:57 No, I know, but you said that the ID could be fully derived from… which… Identifying attributes are included in the entity.
And that's true.
What?
**Michele Mancioppi** 35:11 What I said is the type.
Could we derive from the attributes in the ID?
**Daniel Dyla (Dynatrace)** 35:17 Yeah, and that's true.
But you could also… Like, that depends on you knowing which attributes are identifying for which entity types in advance, always. And if you know that, then you would also know which ones are descriptive, always. And you could just have a bag of attributes And run a processor on it to derive all of entities from a bag of attributes. And we're not doing that on purpose.
**Michele Mancioppi** 35:48 But… And again, I'm not arguing really against this. I just need to understand.
why some things are done this way.
Is there a concern that somebody may send entity types?
With, an entity ID made of attributes that are not the correct ones.
And then, that would break the merging at the level of the protocol, for example, because now you're Carefully, mixing apples and pears, right?
**Josh Suereth** 36:21 I mean, it is open telemetry, so people can do things like that anytime, and that, you know, if you do something invalid with our data model.
And we… We do our best to prevent you from breaking yourself, but, like, yeah, if you're asking if somebody can make an entity that's ill-formed, they can.
Absolutely. What do we do if it's ill-formed? We do what we say, which is, here's how we interact with type, here's how we do merging, all that kind of stuff. We're trying to make it so it's hard to do the wrong thing, is our goal. We want it to be as easy as possible for you to just naively throw… you know, entities at a system, and it will give you good observability. It's kind of like.
the underlying flow here behind why we spend a lot of time on a merge algorithm, where we don't think people will mess it up. We want to avoid things like, oh, I'm going to throw a bunch of host attributes I discovered at you. And then it turns out the data you're looking at isn't from that host. So we want to drop them and not use them, for example, right? So we're making it hard for you to do dumb things, but it's still possible. Like there's You know, what's the the the phrase like?
you try to make a system idiot-proof, and the universe invents bigger idiots, and I'm generally one of them.
Anyway, So that's kind of how we're thinking about it, but the principle behind what goes in OTLP versus what is not, in my mind, is basically anything where I have to interact with it generically as an algorithm, where I can't leverage the fact that I might have a priority knowledge, right?
we put there. For a complete system, like a platform, like DashO, where you can actually have side channels of information coming in, right?
And we can rely on it, cool. Like that's an alternative that we think is going to be more optimal, but we don't want to bake everything into OTLP because we're just going to explode protocol sizes and make observability too expensive. So we need to be somewhat judicious and we're already kind of bloating OTLP a little bit.
With, with entities, like it's already a little bit much. I think it looks a lot better in OTLP arrow, but in OTLP itself, there's still a lot of, duplication there that I'm not super comfortable with, but I don't see an alternative, you know?
**Daniel Dyla (Dynatrace)** 38:43 I think an example… for, like.
Would be to think about, like, a collector processor, which they're typically stateless.
They need to run quickly, and they need to run on data that, you know, is changing over time and being updated, and you may not Want to keep a map in your collector of all possible entity IDs?
that are all possible entity attributes to map to a specific type. If I wanted to drop Like a user entity, or something like that.
It is much… Easier for me to do that by entity type.
Than it is to say, I need to drop any entities that contain these four attributes, and then… You know, it's… It's easier to configure, and you're less likely to make a mistake.
**Michele Mancioppi** 39:38 Okay, I buy the argument.
Thanks for the explanation.
**Daniel Dyla (Dynatrace)** 39:44 Yeah, it's the same thing that Josh was saying, I guess, about interacting with it at the OTLP layer. Like the collector is a component that operates almost exclusively at the OTLP layer.
**Michele Mancioppi** 40:03 by extension.
The, the collector will also need to be able to introduce New entities.
to the data, right?
So, in fact, if you can do it in OTTL, you're supposed to be able to do it also with entities.
**Josh Suereth** 40:21 Yep. Yes.
**Daniel Dyla (Dynatrace)** 40:21 Absolutely.
**Josh Suereth** 40:23 Dimitri's working on that. There's a big tracking bug, if you want to see how far that is. The resource detectors currently can introduce entities. I don't… I think Dimitri had to step out, because I only see fuzz on his camera now. But I would, I would follow up with Dimitri on, like, the status of where that is in the collector. He's been… Doing some good work. I would like… I have to drop in 10 minutes, unfortunately. I would like, if we're okay, to move on to Pablo's question, because I think this has been haunting us for a while.
And it'd be nice to get at least 10 minutes of progress on it.
We also might want Dimitri back for this, too. Pablo, Dimitri, or at least Pablo, you're here.
**Pablo Baeyens** 41:03 Yeah, I'm here. Yeah, we've been discussing this on the system semantic conventions. And I think you've discussed this for a couple of weeks, but I wasn't able to attend.
I mean, the general problem which you have discussed before is that Defining an identifying attribute for the host entity seems pretty hard.
Especially making it in a way that is, like, works in all environments.
I had one specific question.
about this, but we can discuss the general topic as well. And I guess we can start with a specific question, which is… Well, I guess first a dumb question, which is that I think in order to talk about a host entity, you need to have all the identifying attributes populated. Is that right? Or is there a way to talk about a host entity that cannot be identified?
**Josh Suereth** 42:10 Well, this is actually one of the key discussions we have. In our current model.
There is not a way to talk about a host without the identity.
However, what Dimitri built in the collector, and what I think we need to move into the model, is the ability to say, I have a bunch of attributes about a host. I don't know which host, though.
Like, I'm pretty sure it's the one I'm running Can you do something useful with this algorithm, right? And in the collector, it makes a lot of sense, because you have things that are detecting for the local host ID, and so you can have one person identify a bunch of attributes about the host, and someone else figure out an ID, and then you tie the two together, right? That is what the collector's doing. And what we've been talking about is, how do we formalize that in entities? Because today.
in OTLP, at least, right, on those boundaries. We made it so you have to know the ID.
**Pablo Baeyens** 43:07 Mmh.
**Josh Suereth** 43:08 communicate at OTLP boundary. So originally we were thinking this would be like just within the collector, you could do that. But if we have this problem with host, now let's say I do host detection in SDK.
and I don't have an ID there, and I pass it to the collector, what happens? Do we just drop those attributes? Do we ignore them? Like, how do we want this to interact between an SDK and a collector?
We have the SDK, send this over to OTLP, where we say, hey, we have a bunch of attributes that we think are about my host, but I have no idea what host I am, go figure it out for me, you know? That might be a useful thing for us to do.
**Pablo Baeyens** 43:46 Okay, I'm… oh, I gotta… I'll let Miquela talk first.
**Michele Mancioppi** 43:51 But, wouldn't be… in this case, the fact that SDK does not create an entity, because it doesn't have enough information, but it does, set the resource attributes, and then somebody… and then something… Collector side actually synthesizes the entity.
Since it has all the pieces now.
**Josh Suereth** 44:15 Yeah, that's… we're basically trying to figure out how to design that so it works consistently all the time, like, correctly, right?
So, one of the things there is what attributes go into the host entity. Like, I think OS goes into the host entity as a descriptive attribute, is that correct?
**Dmitrii Anoshin** 44:33 Yes.
**Josh Suereth** 44:35 Yep.
**Pablo Baeyens** 44:35 Yeah, so you have things like the IP or MAC addresses, all of the CPU, are on their host.cpu.
And then thinks about the if it's a VL, there's a bunch of attributes hosted image.
**Josh Suereth** 44:55 So, I guess… yeah, that's exactly what we're kind of asking here, Michele, is, like, if I'm the SDK and I'm detecting attributes about hosts, do I put them in a thing where I say, okay, these are a bunch of things I know are about a host, but I don't know who I am, and we expect someone upstream to figure And, and how do we send that bundle? It could be that we just send them as loose attributes, or what are we calling them? Unassociated attributes. And then the collector can infer from that.
But, the thing that Dimitri built, I kind of liked a little bit, where you can have people create, like, a bundle of attributes that says, here are things about a host, someone needs to go figure out my ID, and if you make it to the end of resource detection, or the end of processing, where I have to send OTLP further, and I haven't figured out what to do with these attributes.
I need to kind of flatten them as, as kind of unassociated attributes, or I might need to drop them, because the data I'm looking at is not relevant. Like, like, it shouldn't be attached, right? And that's, that's the decision we're trying to figure out how to make.
**Michele Mancioppi** 45:58 I can give you a second excellent use case that this problem would solve.
on Kubernetes, No SDK has implemented logic to look up the Kubernetes pod UID.
It is possible, by looking at the C groups, Nobody does it.
But for example, from within the SDK, you would know what the container name is reliably.
**Josh Suereth** 46:28 Yeah, that's a good one.
So, so back to the host question.
We answered one thing for you, Pablo. In order to talk about host entity, do you need identifying attributes populated? And the answer today is yes.
**Pablo Baeyens** 46:52 Okay.
**Josh Suereth** 46:52 I have more questions based on that answer.
**Pablo Baeyens** 46:55 Yeah, I guess… So we can try and find a definition for host ID.
But there may be still cases where we just cannot get a good value for it.
So, for example, Assume you're not on a… Cloud VM, and so you're falling back to the slash CTC slash machine ID, and that file happens to be empty for some reason.
What… is… is that… It's a definition of host ID that is… fallible in that way that can fail to be fetched valid.
**Dmitrii Anoshin** 47:39 We discussed this last time, and I think that's not the problem of the entity.
Model, or entities… It's a problem of us.
The system semantic conventions sick. We need to find a way.
And there are still options, right? There are some like Mac addresses which there are several of them. Right? We can.
just figure out which one to use, or something. There, I… I… yeah.
**Pablo Baeyens** 48:10 Sure. Like, I think the one algorithm we decide to use for hosted ID is the system semantic convention seek problem. But I guess you're implicitly answering my question as like, yes, you always need to have a value for host ID when you're solving for a host.
**Dmitrii Anoshin** 48:26 I think we should stick to that model. Yes, we should stick to that requirement that every identifying attribute should be has to be there.
**Pablo Baeyens** 48:34 Okay.
**Michele Mancioppi** 48:37 It has to be there with any value or an empty string suffices because in OTP we differentiate between missing or empty.
And those two are usually the same on query time, at query time, in most tools I know.
**Josh Suereth** 48:55 It should be there with a real value, not there with a missing value.
I was trying to find out, just for some context, Pablo, I don't remember where this is. I don't see it here. It might be in our OTEP, but one of the problems to think about is the multi-observer problem. Let me pull this up.
So, when you pick an ID, the thing that we want to make sure of is… Let me see if we have this multi… Multiple observers, yeah. We want to make sure that if I'm viewing the entity from two different locations, that I can line the IDs up.
In some fashion. Like, that's critical. So, if you can't discover enough information where you are to know your ID, one of the things we're basically suggesting is, cool, defer that to somebody else who can give that ID. But if you have two people who can observe the same entity and are reporting data, we want to make sure that we're picking the same ID in both of those places, so that the data is actually mergeable and unifiable downstream in the database. So, the only thing I'll say is when you define that algorithm, make sure it's something that works both in the collector or in any other system that would have to infer a host ID for a host.
And that's, to me, that's the hardest part about defining these IDs for entities, is thinking about multiple observers, right? So, if you decide that your ID is something we could never discover inside of an SDK, what that means to me is we never… actually fill out the host ID in an SDK. Maybe we find a way to pass attributes from the SDK to someone else that will discover it, but we never actually say, I know what my host ID is from an SDK. If we can't produce the same ID that will be produced somewhere else. Like, we need to make sure that these things are consistent. Otherwise, again, the whole correlation aspect of hotel breaks.
**Pablo Baeyens** 50:55 Right.
**Josh Suereth** 50:56 Okay. I do need to drop, unfortunately. This is…
**Pablo Baeyens** 51:01 I'm done with my questions. Thank you.
**Josh Suereth** 51:03 No, no, I expect this to be something we churn on. I want to see if we can make some progress offline. I don't know if you want to talk in Slack channels or bug issues or whatever. Obviously, you and Dimitri talk, but the host-related thing is, I think there's still an issue in the entity data model.
we're hinting at here we need to find a way to solve, so I'm happy to continue the discussion. I don't have any good answers yet, though, and I haven't had any insights recently, so, you know, let's keep talking.
**Michele Mancioppi** 51:34 Something that doesn't gel in my head is the requirement of having to put some reputable value, even if you're not sure, with the discussion we were having before about partial entities.
That doesn't fit in my brain, because if you put stuff for the ID, then it better be reliable.
**Josh Suereth** 51:54 Yes. The notion of sending partial information is something we're exploring. That's something you can't do today. So in the NCDA model, you have to put IDs. You can't put partial information.
The hole, I think, is in our data models, the ability to actually put partial information and still have the system work. And how do we do that safely without causing a whole bunch of problems? That's what we have to figure out a design for.
Okay, cool. I'll see y'all later. You can feel free to keep talking without me, but, I gotta drop.
**Dmitrii Anoshin** 52:27 I'll drop as well. Thank you, folks.
**Pablo Baeyens** 52:34 All right, thank you.
**Daniel Dyla (Dynatrace)** 52:35 Yep. If Dimitri's dropping and Josh is gone, I think that's the end of it anyway.
**Michele Mancioppi** 52:41 Bye bye.
**Pablo Baeyens** 52:41 See you, bye.
