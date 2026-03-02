SIG: Specification SIG
Date: 2025-12-02
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/1-UMWH92eiuSjYpAXrCg5KLhcPaPL7ETjvZmpkzcxS_ScpyfQtZjrbh_C4N7wPKl.LAz40OUhMAayruBZ
============================================================

## Zoom Recording Transcript

**Jack Berg** 00:17 Hey, Riley.
**Reiley Yang** 00:20 Hey, Jeff.
Hey, Taylor.
Hi, dude.
**David Ashpole (dashpole)** 01:20 Hey, Riley.
**Reiley Yang** 01:23 Morning, Casa.
**Trask Stalnaker** 01:27 Hey.
**Reiley Yang** 02:13 Hey everyone, thanks for joining. We'll get started in a minute.
Okay, let's get started.
The first topic is from Carlos. I don't see Carlos here, but this is more like, FYI, so,
Please take a look at the…
the spec PR for the enabled API for logs, no, for synchronous metrics, and we're going to merge it by default, so if you have any blocking issue, it's a last reminder.
The next one, also from Carlos, the W3C randomness flag.
**Carlos Alberto Cortez** 03:26 Yeah, this is something we discussed last week, about this part that, you know, as you know, it, it's a candidate for the W3C.
And, it's a genetic problem, so we want to move that on your side. It's already in the spec, but it was marked as optional. Now it's, in the matrix, at least. Now it's marked as required. And also, I went and filled manually an issue for every C on, you know, so you don't forget about implementing this one.
If you seek didn't get one issue, let me know, but I think I went through all of them, at least the ones that are in the matrix, you know?
Yeah, that's all. It's an important thing to have
And, it could be great for Sigs to implement this.
Once this is done, we can go back to W3C and tell them, hey, this implemented, just mark this part stable.
Thank you.
**Reiley Yang** 04:23 Yeah, thanks, Carlos.
Okay, the next topic.
the process contacts.
**Ivo Anjo** 04:34 Yes, me, hello.
So, yes, thanks for the feedback, last week. I've kind of applied a bunch of the feedback I got last week, and my question is more of also a meta question, which is, this is my first OTEP, so kind of the question is.
What are the next steps?
In particular, the quick changelog, I would say, is that I changed the process context tootab to use the resource message, as we kind of discussed, as well as removing the documentation about any kind of suggested attributes. We just kind of use whatever's in the resource.
And also did, like, a few text cleanups, so that's kind of it from the feedback I got last week.
**Reiley Yang** 05:27 I wonder if Josh is here.
**Josh Suereth** 05:29 Yeah, sorry, I'm a little late. I was, about 5 minutes late.
Yeah, in terms of next steps, I think it's, OTEPs take a while, I'll just say that, first of all.
But, we need to get approvals. So it's mostly getting people to pay attention, getting people, to approve and things. So, I didn't have a chance to get through to this OTEP in my
daily, like, triage of all the issues that I walk through. So, apologies, I didn't see your response. But I will take a look after this meeting, and yeah, we… the goal now is just get approvals. So, I would look for contention on the OTEP. Coming to this meeting helps get approvals, because you can highlight, hey, there's a contention point, should we discuss it?
And, you know, continue to encourage people to take a look. Once it gets enough approvals, then it gets merged.
**Jack Berg** 06:18 Makes sense. Thank you.
One thing I'll add to that is, so…
All approvals are useful, whether they're green checkboxes or gray checkboxes, and one signal that I look for in particular when there's, you know, an OTEP about a domain that I'm not a subject matter expert in, this is about, you know, shared context correlation between eBPF and SDK, so I'm really familiar with the SDK side of things, not so much about the eBPF side of things.
is, I would look for the other experts in the eBPF world to indicate their support.
And, you know, it's easier for me to give my approval with a green checkbox if I know other people, like, you know, that will be consumers of this, you know, also support it.
**Ivo Anjo** 07:10 Yep, that makes sense. I'll chase up the folks in the profiling SIG to,
Put green checks, or, tell me why they're not putting them.
**Jack Berg** 07:21 Yep.
**Reiley Yang** 07:23 Thanks, Aura.
Okay, any other topics?
**Carlos Alberto Cortez** 07:40 By the way, I don't see many people in the call. I wonder if…
I mean, I know that the last two… well, the two weeks of Christmas season, we will not be having calls, but I'm just wondering, like, thinking loud, I guess, or asking myself out loud whether the next weeks will be quiet.
**Trask Stalnaker** 07:59 Likely.
It's December.
**Carlos Alberto Cortez** 08:03 Yeah.
**Reiley Yang** 08:05 Yes, I remember last year, we… we stopped all the OpenTelemetry community meetings for the last two weeks of December.
**Carlos Alberto Cortez** 08:16 We did that again.
**Trask Stalnaker** 08:19 Yeah.
**Reiley Yang** 08:19 Yeah.
Then that means next week we'll continue this meeting, although we expect, like, less people here.
**Carlos Alberto Cortez** 08:27 Yeah, the next two weeks, at least, yeah.
**Reiley Yang** 08:31 Okay.
So, if that's the case, let me put a note here.
Oh, sorry.
**Carlos Alberto Cortez** 08:46 Well, would you do that, is I have a new point, Josh, about entities PRs?
**Josh Suereth** 08:56 Yeah, so I'm a bit slow, so I'm copying and pasting them as I go.
There's 3 I want to talk through.
There's actually, there's 4 entities slowly, slightly related… 4 PRs related to entities, and one of them is actually the one we just discussed around
propagating the resource attributes. But, this one…
This, these, these three, I kind of want to talk through them in order, if possible.
So the first one is actually just, we're finally ready to commit to the specification, the merge algorithm from the OTEP. There's some discussion on this. Basically, we're trying to take what was defined in the OTEP and,
define a merge algorithm for how resource merging works in the presence of entities. For context, an entity is basically a,
A self-contained thing, like resource, where resource has just a glob of lots of things, an entity has a specific identity, and then a description.
The identity is a set of attributes, the description set of attributes, and so we define an algorithm for how to merge these things together, and that algorithm we would like to start committing to the specification. So, please take a look. There's implementations in Java and JavaScript, and I believe there might be one in Go. I need to take a look at that one.
But we've been doing a bunch of prototyping for the past year, and we're pretty happy with this.
merge algorithm. What we're not happy with is how it's described, which is why we're looking for feedback. So please take a look, read the algorithm. If it's confusing, make comments, because we want to make it clear how it works.
So that's that one.
The second one on the list… is,
Actually, I can pause for feedback if anyone wants to say anything or has anything they want to say.
**Jack Berg** 10:50 Is the first one, linked to some example implementations?
**Josh Suereth** 10:56 It does not, because they are in the OTEP. If you need example implementations, there's an open PR in your repo, Jack, that I proposed with the merge algorithm. I can send you an updated version of it. The… actually, I think the second one.
Which one is the second link I put there? Hold on, let me open it.
The second one, I think, has a link to the example. Now, the third one does.
So the third one has a link to an example that implements it, which has…
yet another implementation of this merge algorithm, if you want to see it in action in Java.
**Jack Berg** 11:38 So it's a different implementation than the one being proposed? I'm just trying to…
**Josh Suereth** 11:42 No, no, there's, I just… I had to copy the implementation in 3 different prototypes.
**Jack Berg** 11:47 Okay.
**Josh Suereth** 11:48 So it's the same implementation, it's just in 3 different PRs.
**Jack Berg** 11:52 Okay.
**Josh Suereth** 11:54 The… that…
That part of the code has not changed, like, the merge algorithm has not changed in any of the prototyping we've done.
**Jack Berg** 12:02 It's just being codified.
**Josh Suereth** 12:04 Yeah.
**Jack Berg** 12:05 Can you… can you link that for our reviewers? Just because we ask, you know, anyone who contributes new ideas to the… to the… to the spec that have links to prototypes, so just kind of…
**Josh Suereth** 12:15 Yep.
Can do.
Let me… Do that now…
Okay.
Are there… is there any other feedback on this before we move on to the next one?
Okay.
Alright, so the next one…
Is, if you don't mind opening that?
This is… this is an interesting…
concern from the collector side. So,
One thing I wanted to have a discussion about here, we talked about this in the entity SIG,
I feel like there's a misunderstanding of entities based on… from the collector side, where when you look at what they look like in OTLP.
So, inside of OTLP,
Because we don't want to break backwards compatibility, we have a very awkward model for using entities.
Where, the resource attributes are still complete and thorough, and denote all the same things that used to be in resource attributes. And there's this new thing called an entity ref, which refers to resource attributes and tells you which attributes are tied to a specific entity.
However, in the data model and in the SDK implementation so far, what we've done is a resource is actually a collection of two things, a set of entities and extra attributes that are raw. That's it. That's what they are. So, inside of the SDK, we can do that in a non-breaking way.
Inside of the protocol, we cannot.
So, we put all of the attributes together to keep existing OTLP folks working, and we have this reference thing. What that's caused is, in the collector, it looks really weird, where you have this notion of an identity ref to an attribute that is somewhere else in the protocol.
To encode entities in it.
Whereas in an SDK, you can actually just have a list of entities, where an entity has an identity, which is a set of attributes, and a description, which is a set of attributes.
This terminology update, I don't know what motivated this in the collector SIG, so that's why I wanted to bring it here to kind of talk through it, but I think it just makes everything more confusing, and I don't understand the motivation at all.
of, like, why can't we use identifying attributes, or identity, which is a set of attributes in entity. So I'm actually looking for more feedback from the folks in the collector, that kind of had concerns about this. I think Josh McDonald's in the call, and you actually raised, some points on this PR, so I was wondering if you could speak to that?
**Joshua MacDonald** 15:19 Hi, I can try. I, I sort of fielded this issue from both camps, knowing the collector SIG and understanding the specification from this group, basically. So I read… I read the PR and understood the confusion, really, but…
I feel like…
the points of confusion are at least half about, sort of, English as a native language types of comprehension, like, points, essentially. I think the way we construct adjective phrases is part of the question here.
You're look… you're looking at me a little quizzically, but, so the… the,
But I… I came down sort of, like, actually supporting your position, Josh. I…
I just… I see the confusion.
I did make a comment on the PR, you could look at it. I can't remember exactly what I wrote.
I think the issue… maybe take a look at the issue.
**Josh Suereth** 16:20 I looked at the issue in the collector, and again, I think this is… I made a comment about this, but basically, in the collector, you're dealing with the ugliness that is how we encoded this in LTLP, but there's not a convenience wrapper that treats entities as wholesale things, where you can actually talk about their attributes individually.
And I think that's what's leading to the confusion. So in the collector, they're like, oh, these are refs, these aren't entities. It's like, well, that's how we encode them, but that's not how to think about them in the data model.
And I never made it past that in the confusion, right? So I think the confusion's actually, like, not understanding entities. If you look at the associated issue, that's what I ran into.
So I kind of wanted to have that discussion to see if that's accurate or not, but I think the update to the spec to change the terminology to fix this particular issue comes from a discussion in the collector, so you have to click on that one.
This particular fix to the spec, I think, actually just doesn't help make things less confusing. I think things are just as confusing as they used to be.
In fact, I think they might be more confusing, because it's just unnatural English going forward.
**Jack Berg** 17:30 If there's a problem stemming from the distinct, like, confusion around how something is modeled in the data model versus encoded in OTLP, we're really going to struggle with this proto-PR that I just linked in the chat.
About, you know, introducing reference-based attributes all over the place.
That's essentially the same thing.
**Joshua MacDonald** 17:53 Could we… could you click into 4700 again? I did post on that issue in the specification repository. I'm just trying to… I'm actually trying to find the middle ground, because I agree that the language that's been proposed is unnatural English.
And I think part of the problem, if you scroll down to my…
**Reiley Yang** 18:17 We lost touch.
**Joshua MacDonald** 18:18 was identity and description. But I don't know if we can change protocol field names.
So…
I… I, I have proposed a more natural English solution to this, which I think addresses half of the concern, at least, which is just to call these description key attributes and identity key attributes. Not identifying attributes, not descriptive attributes, but to use the, like, literal term that's in the protocol field. That's what I was thinking.
But I think I'm hearing, Josh, your concern is bigger. It's about the collector managing this concept, which is going to be the way the collector's P data model today works. It's very literal. It's like the OpenTelemetry protocol manifests as objects. And so you're getting this entity ref and this ID keys field, and it doesn't make any sense. Maybe we need a higher level interface around
protocol data for entities in the collector. I'll stand down, thank you.
**Josh Suereth** 19:13 Yeah, I'll let Danny go, but I did want to call out, that's the… like, specifically identity key attributes and description key attributes I'm very against, because that makes it more confusing. In the… we're talking about the data model here. This is the data model description. In the data model, they're actually attributes. They're not just keys, they're the entire thing, the key-value pair.
So, like, when we talk about the data model, if we were to redo the protocol, we would have a list of entities that contain everything, and there is no ref, and then we would have a list of raw attributes, if we could redo the protocol from scratch, which we cannot do. So, I really don't want to do that, because I think that makes it even more confusing.
to what we're actually building. Go ahead, Daniel, sorry.
**Daniel Dyla (Dynatrace)** 19:55 I saw Josh tried to talk, but was muted.
**Joshua MacDonald** 19:59 Yeah.
**Daniel Dyla (Dynatrace)** 19:59 I was gonna say more or less the same thing. I actually think description key attributes and identity key attributes is almost the opposite of what we would say, descriptive attribute keys and identity attribute keys, but I'm… I'm against…
putting that sort of physical layer into the specification. I would rather deal with the conceptual layer, which is that these are identity and they are description. And how they're encoded is…
in implementation detail. Like, it's handled differently in SDKs than it is in the collector, and the collector decided to interact directly with the, like, OTLP shape of the data.
And this is a consequence of that. But I don't think that we should encode those types of
Physical level details into the specification.
**Joshua MacDonald** 21:07 I see the point that you don't like description key attributes, I get it. So the noun is description key, and the adjective is attribute, except it's an entity that we're describing, not the attribute we're describing. So I'm a little confused now entirely, and I will say no more.
**Josh Suereth** 21:26 Yeah, my objection was the word key. It's not a key, it's a key-value pair, which is what an attribute is.
So that's why, again, the notion of a descriptive attribute and an identifying attribute, I think.
Actually fits pretty well.
calling the thing that contains the attributes a description or an identity, I also think makes sense.
So, what I don't understand is where the confusion comes from from those two terms. Like, that's still… it's like we're over-indexing on OTLP, is what my thinking has happened, of what has happened here. Because we're like, oh, these aren't… they are those things, that's what the data model is, and I really want to avoid
fixing this, I want to actually get us to understand what the concept truly is, so that we actually implement entities correctly everywhere. And so, yeah, if this is like…
you know, we're over-indexing on the actual structure of OTLP, cool. That's kind of what I think is happening, but I do want to confer, right? So, like, Josh, like, I don't want you to give up here, I want to actually finish the conversation. You know.
if I say this is the identity, and it's a set of attributes, and this is the description, it's a set of attributes, and I refer to those as identifying attributes and descriptive attributes, does that sound reasonable? Is that English? Does that match the mental model?
**Joshua MacDonald** 22:53 Yes, I support what you're saying. I'm just trying to arrange the adjectives and nouns in the way that works in my understanding as well. So, there is a…
The…
I guess the way I understand entities may be incorrect. We are talking about the entity ref struct. It has fields named ID keys and description keys. Those are not attributes, those are key lists.
They are entity description keys, and they are entity attribute keys, the way I understand it.
**Josh Suereth** 23:21 Yeah, that's… so this means we don't understand entities. That's exactly what I needed to know. The entity ref struct is a reference to the attributes that constitute the entity in the attributes of the resource protocol buffer.
So in resource, there's an attributes, key-value pairs. The entity actually needs the value from that list, so you get a reference to the key, and you have to look up the value to reconstitute an entity, because the entity actually has all those key-value pairs that make up its identity or its description.
That's the problem here, and that's the thing I want to make sure people understand.
**Joshua MacDonald** 23:56 I think I understand that.
I think that the confusion is simply about the names of the entity ref.
fields, which are ID keys and description keys.
like… .
**Josh Suereth** 24:08 That would be a thing to fix in the proto, then. The data model and the proto are… okay, gotcha. So, so, I think what we should do, based on this discussion is the confusion should be updated in the proto descriptions.
Not in the data model spec of the specification. Is that fair?
**Joshua MacDonald** 24:28 I think that's fair, and I think that we should really bring in some collector people, like Dimitri, to share their perspective, because I think you can change the protocol definition, and it won't change the confusion if there's sort of, like, a…
Well, I'm not sure it will change the confusion.
And I don't have more to say. I think that it might be worth looking at the bigger architectural question of how are we going to deal with entities in the collector.
**Reiley Yang** 25:07 Hey, Josh, I have a suggestion here. Maybe in the spec, when we mention those terms, have a separate section just calling out these terms, and for each one, give a concrete example, so people won't be, like.
the example that you just explained seems to be bringing a lot of clarity. And in the proto, there are places that we can add comments to the proto file, so in that comment, maybe, like, also add example and link to the spec.
So when people try to make changes, they always refer to the same source of truth.
**Josh Suereth** 25:42 Yeah, from my understanding, those are already in the protos. So, but I can add more. I think my… my concern is that I don't think that's being read. I think people are just looking at the name of the term and making assumptions from that.
**Reiley Yang** 25:58 I see.
**Daniel Dyla (Dynatrace)** 25:59 Yeah, I was just about to say the same thing. The proto… the reason the Proto is the way it is, is it's a backwards compatibility hack.
We… we wrote the data model document for, this is how you should think about entities, and then we had to find a way to make
the proto-work-backwards compatible… work backwards compatible with resources, so that if you don't read any entity anything, and you're only reading resource attributes, you still get all the attributes.
And then, I think people are looking at the proto as the source of truth, when it's… it's a layer removed from the source of truth, for the way you should be thinking about entities.
**Reiley Yang** 26:59 Okay, any other, like, ideas?
Comments?
**Josh Suereth** 27:04 It sounds like we should have this discussion again. I'll ping Dimitri. He wasn't able to attend the entity SIG, yesterday.
So I'll ping him again to follow up on this.
I… it does sound like the confusion that I'm hearing is what I expect, we just have to come up with a path forward.
Yep.
Cool.
**Reiley Yang** 27:26 And on a related topic, I… I noticed, like, a couple times in the…
like the docs translation group. I speak a little bit Chinese and Japanese, so I see a lot of debates there when it comes to some very specific English terms.
it's a nightmare for them to translate that to their language, so I… I know it's a hard problem, but my question is, for… for example, like.
the… the terms that we discussed here, is it possible, or would that even, like, help if we get a list of these terms and seek some general feedback for… from the other language docs maintainer, see if, like, the
They feel this is something reasonable for them to translate, or it's just, like, mission impossible before we lock down those terms.
I consider, if we got some English terms, and people here are generally confused, even if they have been involved in open telemetry for years, and then the other language translators, they come and say it's a nightmare, then these terms are bad terms, in my opinion.
**Josh Suereth** 28:37 I agree. We had this discussion with the entity SIG a lot as well. We actually are inconsistent about using the term resource or entity. The specification for resource prior to the entity SIG declared it as the entity being observed.
For example.
Like, it's… we're in this vague notion where I don't think we… in English, it's confusing. So, Riley, I agree with you that we should avoid confusing, like, being confusing.
To some extent, though, we're inventing a model. That's why I think the data model spec is so important, and choosing words is so important, and this PR, defining data model spec in this discussion we're having, is actually really important, which is why I wanted Josh not to give up.
And just… and, like, go through the conversation, because, to some extent, we try to make the words as close to an English word as possible, or as close to a word you might understand, but to some extent, we're inventing new things.
Right?
And the meaning of the thing is actually the meaning we've defined in our data model. And so that's why I really focus on, let's make sure we have the right shared understanding of that data model, and that we're communicating that effectively.
And to the extent that we're able to do that in all languages, I think that's important, and we need to choose terms that, like, do a good job at that, but that's what naming really is. The thing we're talking about is not a real English thing. It's not a word that, like.
we have to find one close enough, and then make sure people, when we say that word, we all understand the same meaning. That's the goal
of the language we use. So, I hear what you're saying, totally agree. I don't know if we have a good option for resource and entity, specifically, because we have trouble with English there as well.
**Reiley Yang** 30:23 Yeah, and sometimes maybe not have an, like, English word, just invent something, and people will just use that.
Right? Like, you see, like, many, many, like, non-SQL databases, they just have a very specific name that's not coming from English. Josh and I had an earlier discussion about the word Q. Q is not even American English. Like, a lot of Americans never heard about this term, but
Imagine if we're using American English, we'll call that a line, and it would be confusing as hell, right? This is why people choose Q as the specific term.
Which is nice, like, it's very clear, so maybe here, not just, like, limit ourselves to some, like, normal English, or, like, American versus British, or whatever, South African English. Just have a specific term for that.
**Josh Suereth** 31:09 Yeah, I hear what you're saying. Unfortunately, we've already committed to the term, like, 6 months ago.
**Reiley Yang** 31:15 That's fine.
**Josh Suereth** 31:15 put it in the photo. So for this one, it's… it's… I… going forward, I'd agree. Yep.
**Reiley Yang** 31:22 Okay, cool.
**Josh Suereth** 31:23 Okay, one last PR, then. Sorry.
**Daniel Dyla (Dynatrace)** 31:28 Josh, I just… As a potential,
I don't even know if I should bring this up, because…
It would set us back, like, 3 months.
what… Are the chances that we would be open to…
Not being backwards compatible with resource.
and just adding a new field called Entities.
where the model… Is directly what we described.
And then a configurable option that also copies those, like, all entity attributes into resource.
as… an opt-in.
flag.
**Josh Suereth** 32:17 I don't think it can be out… I don't…
Ugh. I hear what you're saying.
**Daniel Dyla (Dynatrace)** 32:23 Or opt-out, whatever it is, a configurable behavior.
**Josh Suereth** 32:27 We've talked about this for the past year, like, it's,
The question is, how hard do we want to make it for people to use entities? Do we want the ability for people to, like… we want the SDKs to start being able to leverage entities for detectors quickly.
And so, if we go for that level of breaking change, the answer is they're not gonna land anytime soon, to the point of, like.
You know, what's the value in them?
Right? I don't know if that is viable from that standpoint. I'm not saying no just to say no, because, like, it's different. I'm saying no because I think we thought through this a lot in terms of how to make entities in a way that you can use them and not know you're using them.
And still be successful.
So, if we want SDKs to leverage them to have this new merge algorithm that we think does a better job of schema URL, that does a better job of semantic conventions, we can do all of that today, and the collector never has to support entities, and that's all successful.
And then once the entities are transmitted,
everything still remains successful, and you get extra features in the collector, right? Like, I think that was the whole reason we went with the path we're going today. I don't think any of that has changed.
And the path you're suggesting, I think we could do if the default behavior matched the existing behavior such that we aren't causing high friction.
Like, the difference between entities and other things in OpenTelemetry,
We cannot break users the way other features might be able to. Users have to know they have a problem that they want to fix before they'll engage with it. Entities and resources specifically is one of those things where it either works or it's horribly broken.
And if it's working well enough, people aren't going to make any change, even if we want to improve it, make it better, and solve a whole list of problems we have making it work. So, actually, like, resource is a problem that we have a lot of issues with that we need to work through.
But users kind of don't care, because we solved it enough that they can just get something working and go. And so, I don't think we have that wiggle room we do in other things, where there's, you know, the value of entities when it finally lands is going to be enough to get people to move.
But the amount of infrastructure we have to build in the meantime is really high. So this is one of those things we cannot break users, we need to keep it magical, keep it nice, and we just want to implicitly have all the utilities they use in the collector and in SDKs get better.
I don't think we're gonna be able to convince them to go through a breaking change for entities, in my opinion.
**Daniel Dyla (Dynatrace)** 35:18 Yeah, I guess I didn't mean, I meant, like, double emitting. So, from the user's perspective, it would be… you know, I would probably do it more similar to how we've done some of our semantic convention breaking changes, where you opt into the double emit, and then for some period of time.
And then, you know, the default behavior changes after a year, or two, or whatever, and then it's opt-in to…
Double emitting the opposite direction. And then, eventually.
you know, the default changes. And, you know, maybe… maybe the double emit is always an option for backwards compatibility, because…
Why not? But… It might alleviate some of this confusion.
Both from the implementation perspective, and from a…
Explaining what's going on to users' perspective.
**Josh Suereth** 36:18 Yeah,
That would create a bunch of overhead and resource, but that's not that bad, because generally we don't expect a ton of resources. I…
**Daniel Dyla (Dynatrace)** 36:30 Yes, it would create overhead.
**Josh Suereth** 36:33 Yeah, let's think about that and discuss that. I, I,
My theory is still that there's going to be, eventually, an OTLP V2 in the next 3-4 years, and if that lands, or, like, things like OTLP Arrow, we can just not make that mistake in new protocols.
So that, you know, we don't have to deal with backwards compatibility. But my assumption with the way OTLP has been, if you look at, like, new features in OTLP and such,
there's still gonna be people supporting OTLP 1.x, like 1.7, for example, or 1.5, for a long time. And so…
the… the notion that we'd be able to transition, I just don't… because it involves a protocol change, I don't think we can be as aggressive as we can with instrumentation. Like, this is…
If you think about OpenTelemetry as a spider web of dependencies, we're talking about the core, the bottom.
When we're talking about instrumentation, we're talking about an edge.
And so, making a breaking change on an edge is a lot easier and a lot more clear to see the value. Making a change at the core is… is…
I have a higher bar, personally. But I think it's a good idea that's worth, like, discussing and evaluating pros, cons for.
Maybe don't write down that I said it's likely in the next 2-3 years, I just mean it's something to consider.
**Reiley Yang** 37:55 I put a question mark there.
**Josh Suereth** 37:57 Yeah, I don't really want to pull that trigger at all, if we can help it.
**Reiley Yang** 38:01 Okay.
**Josh Suereth** 38:02 Yeah.
**Jack Berg** 38:03 Well, if you even want a chance of pulling a trigger like that, you have to start collecting the ideas. Like, what are the things that really don't work with OTLP V1 that you'd want to solve with OTLP V2?
**Josh Suereth** 38:16 Yep, and I don't think we're ready to do that right now. Like, let's… we have bigger problems, we have stability things to focus on. The whole idea behind entities is we want to clean up and finish the work that we had started.
and clean up how resource detection works between systems and multi-observer problems. So, let's finish that, let's get that out the door. I do not want to break OTLP, and I think the cost of making break… changes to OTLP is so high.
that I'd prefer not to do anything that would require some sort of breaking flip at any point.
**Reiley Yang** 38:51 Quick question for GMACD. Is this something that people can do better in the OTAP protocol? And then, like, I can imagine we learn some lessons from OTLP, we do a better job in OTAP than when it comes to.
people start to seriously think about OTLP 2.0, they can borrow the idea from OTAP, although the
Column versus row oriented is different, but the… the semantic model is similar.
**Joshua MacDonald** 39:19 Good question. I don't have a good answer, though. We haven't put any entities forward into OTAP at this time, and I'm kind of thinking about it as I'm listening to this conversation, what it ought to be… look like.
So I don't… I don't know, the answer.
we will, of course, have the same type of backwards compatibility issues. Like, we already have a representation for resources in our current protocol, so if we're going to change it, we just… just mean supporting more variations, and all the decoders are going to have to know about it, and so on. So it's… there's potential there. I don't have a better answer.
I do want to interrupt to elucidate a thread that I put in the chat just now. I know it's sort of tangentially relevant, but whenever we talk about OTLP, and everyone knows it's kind of a very verbose protocol, and it's sort of, like, not meant for storage because of its verbosity, and there's this pressure to put dictionaries in.
In the OTel Arrow group, we've had a volunteer approach us, who's doing academic work. We asked them to do a study of this new algorithm, OpenZL, which was published 2 months ago from meta researchers, and I gotta tell you, the results are very promising. Like, when you know the structure of the data and your compressor.
knows that, it's like, we don't have a problem with compression anymore. It's gonna be fast, and it's going to be just as good compression as OTil Arrow, is what we're seeing, or very close. And so I just wanted to put that in the sidebar because, I think we might want to stop worrying about size if these new compression algorithms are just going to solve the problem for us.
I'll try and get those results as published as fast as I can.
**Jack Berg** 41:03 That would be incredible, right? If we can just put this argument to rest and keep using the most simple and dumb representation in the protobuf messages, which is what we have now.
not even worry about these dictionary things and, you know, the promise for increased compression that they have, and just, you know, solve it via off-the-shelf compression. That would be amazing.
**Josh Suereth** 41:24 I want to call out, it's not necessarily about compression.
That is, like, if you think that the reason we're using a dictionary is compression, that's not the way to think about the profiling signal. I'm having this discussion in another thread as well, but the reason that we use the dictionary is actually about sharing these strings and these identities between processes and stuff.
And actually, the in-memory representation of how you store the data is actually way more efficient if you're not keeping these strings, if you just keep IDs and indexes and that sort of thing. So, like, the reason we have a dictionary and profile is more about how the signal is generated than it is about compression, and it's about keeping the overhead of the instrumentation low.
So, I hear what everyone's saying here. I just want to make sure that when we talk about that signal, we are understanding that the instrumentation for that signal is different than what we're used to.
In very interesting ways, and that's where the profiling dictionary comes from.
**Jack Berg** 42:24 But it's trivial, even if that's the most natural way to represent this information in memory from the actual instrumentation itself, it's trivial to, you know, unspool that and have a more verbose
Row-oriented representation on the wire, because…
and then take advantage of this compression. Like, these are two separate things. What's most natural for the instrumentation and how we encode this on the wire? Because the advantage of having everything row-oriented and consistent across all the signals is that the collector and all of its tools built on top of that
orientation of the data, like OTL, can remain consistent.
Like, it's really terrible to imagine the collector having to operate in a split-brained world, where some things are dictionaries and some things are not.
**Josh Suereth** 43:13 I actually… I personally think this is manageable, and I think, continuing to push on row-based approaches is not the right future for us. But we can have a discussion offline. I understand that that's what we have today, but I… I don't see that matching
where we need to go, so… But… anyway.
If, if you look…
I… I'll quiet down now, but, because I've been talking a lot, but I… I hear what you're saying. I… I think there are ways to solve that in the collector. I think there are ways to basically make OTTL work with a dictionary that are totally fine.
N scale.
it's just we have to go build that out, and prove that this exists. So, I don't have time to do it myself, is the problem, but I know that… I'm sure that the team can actually figure that out. So it's fair for us to ask the profiler sig to do this.
Go ahead.
**Ivo Anjo** 44:13 So, hey, I think I can add a bit to the discussion as well, that, about, like, it not just being about, like, the signal in the wire, because, for instance, right now,
the current ProfilingSeq format is kind of based on the old Google Proprof format. And the old Google Proprof format had, like, a bit of,
It's like a… it's kind of a downside that if you want to add attributes to individual profiling samples, then you kind of need to repeat the whole sample again and again and again and again.
And to handle this problem, because we at Datalog, we were using this previous format, we actually have, like, a custom protobuf encoder that kind of
makes that, like, solves that problem by using a combination of compression and, like, a better in-memory representation, so only really the ugly protobuf ends up in the wire compressed, so it's not a problem. But, once it gets to the Datadog backend, it needs to be unpacked back into, like, an in-memory representation, and that's the thing that blows up. And actually, we still have…
We still have kind of quite a high cost of, like, doing this trick of, like, putting a lot of stuff in the protobuf, and the cost is not actually on the producing side, it's not on the wire side, it's actually once we are, we want to parse that protobuf.
And it's kind of annoying to parse the huge part above. That's actually a bad representation for something that's really smaller. So, yeah, a bit of a data point there.
**Reiley Yang** 45:48 Thank you.
Okay, I think we can move to the next topic.
**Josh Suereth** 45:57 Oh, yeah, I had one more PR. Okay, so this one is,
This one, we finally added the prototypes for, we mentioned this before, this is about, actually, the SDK reporting against multiple different resources.
So the TLDR of this OTEP is… this is to help support the browser SIG, where the lifetime of a session does not match the lifetime of an SDK.
We actually implemented a prototype in Java. Jack, the link to that is in the OTEP if you need to see it. But what this adds is, on every provider, there's a four-entity method where you can pass in a new entity. It will use this merge algorithm we were talking about for entities and construct a new
resource that will be kind of like a sub-resource to the SDK, and it will share the actual export pipeline the SDK already has.
And it will export data against both resources now.
The idea behind this sub thing is, you can pass it to instrumentation that you already had that accepts providers. In Java, you can pass it to anything that takes an OpenTelemetry, because you can actually do 4 on OpenTelemetry itself as well, and get nested things for all of the components.
This, we think, helps unblock the browser SIG in terms of when they need to support session. They can actually construct a sub-provider for the session, and then update their instrumentation to use it, and everything's gravy. This continues to preserve the immutability of resource.
And the other thing is, these sessions can… or these, providers can be closed, because we have closed and shutdown methods. If you call shutdown on a provider, it does not kill the underlying export pipeline, it just kills that provider so it can be cleaned up.
the memory or whatever you were using for it. So, please take a look. It's still in draft form. I'm gonna pull it out of draft form. I think,
Daniel just finished the SDK spec, and I think there's just one to-do in the, markdown I have to add for a link to the prototypes.
But, yeah. Anyway, feel free to take a look. This is, I think, before we had this proposed, where it was,
on instrumentation scope, where you'd actually call for a meter that had a session ID, there's a bunch of feedback that actually that's too low. A lot of our instrumentation libraries work against providers, so we moved it up to provider instead. And this is a… yeah, it worked out pretty well.
So, I will caveat this OTEP, we want to record this as future direction. We do not plan to ask SDKs to implement this for some time.
We do not plan to add this to add to the specification until the stability work that is being pushed is done as well. So I'm going to caveat with that. This is a directional OTEP to help unblock the browser.
a SIG when they need sessions, it gives them a thing they can implement and build in the SDK.
**Jack Berg** 49:06 So, I guess,
I'm just trying to think through how this would work in my head. I'm a ma- look, I know this is for browser, but if… if this is gonna eventually come to other languages, then I'm gonna come at this from, like, a Java standpoint, so…
**Josh Suereth** 49:20 Yeah, you can look at the implementation.
**Jack Berg** 49:22 Yeah, right, exactly, and you implemented it in Java. So, you've got, in Java, you've got something like the agent, and the agent is, you know, hundreds of instrumentations that are all over the place, and what we're essentially saying with this is entity detection is a form of instrumentation.
So, you know, it's somewhat different than collecting metrics or traces or logs, but it's instrumentation, right? It needs to conform to semantic conventions and things like that.
I guess what I'm trying to figure out with this model is how the entity instrumentation would communicate its changes to
more than one…
other instrumentation module. This kind of, like, assumes… it seems like it assumes that, you know, the thing that needs to consume the session entity would, like, so there's one instrumentation that is aware of the session entity, and then, you know, obtains a new provider for that session entity, and then continues to emit its instrumentation.
How would… how are you imagining, like.
Entities being attached to all the instrumentations, not just one.
**Josh Suereth** 50:27 So, yeah, the job example we have here is, like, old-school application engines or web servers. So the idea is the web server would own the SDK and create a resource for the web server itself.
When you're hosting a servlet or an application, you would discover… you'd create an entity for that thing, you would construct a meter provider for that thing, and then when you register your filters or whatever the hell you're doing for instrumentation, it would get that meter provider, that tracer provider, that logger provider for that entity for that app.
So that web server would have one resource which represents the web server, and it can have individual
Resources for each application.
And they're all being reported through one SDK with one export pipeline.
That's how we envision it used in Java. That's, like, the Java equivalent.
**Jack Berg** 51:21 So two things, two, I guess, responses to that is it seems relatively niche. That doesn't really happen that often, that you need to have, especially with the way that web servers are going. So, where you need to have, sort of, one application server that has multiple servlets in it, each with their own identity.
And… but I guess what I don't know off the top of my head, and I know Trask is here, is…
Would it actually be, practical, Like, so the way instrumentation
works… like, does it work in this type of flow that you're talking about, where, you know, you spin up a new server with a specific entity, and then you kind of initialize all the instrumentation from there? Or does instrumentation happen sort of globally at one time at application start, and there's not this opportunity to hook into the startup of each one of these individual entities?
Aye.
**Josh Suereth** 52:17 It's… it's a great question. So, this only solves one class of problem regarding, like, multi-tenancy in telemetry, which is where you up front can allocate it. I will say that for internal Google Cloud instrumentation, this pattern is common.
**Jack Berg** 52:37 Okay.
**Josh Suereth** 52:38 And this is what it looks like.
**Trask Stalnaker** 52:40 Yeah, I think the multi-tenancy example is a better example to lean on compared to the web servers, you know, servlet.
Example.
**Josh Suereth** 52:51 Well, web server's just an example of multi-tenancy that's old school.
news.
**Trask Stalnaker** 52:56 Yeah, it's just… we're gonna push back, and if you use that example, and say that, you know, the Java agent has been fine as a global source, and we have pretty much no user complaints about, you know.
Even though, initially, in the early days, I thought we would, that people would want, sort of, more control per web server app.
**Josh Suereth** 53:20 Yeah. I do feel like the days of big web server apps, where you'd have, like, a thousand of them in there that are all from different
Teams and the web server app as, like, your deployment framework, I think those are gone.
and now you're just hiding them in, like, VMs and Kubernetes and that sort of thing. So, I hear you. This is… this is more targeted at multi-tenancy of today. So, like, if I'm… if I want to use the SDK, for example, to report process metrics, not the collector, right? Let's say I want to use the SDK to do that. I actually don't have the capability to do it.
Because I would need a different resource for every process. This actually gives me the ability to do it in an SDK, if I wanted to.
**Jack Berg** 54:02 That's an interesting… nipple.
**Josh Suereth** 54:05 Yeah, so… so there's… there are multi-tenancy examples, and they're out there. I would argue that you're correct, Jack, this is an advanced feature. And that's why I think what we want to do is agree on the direction that we would move, and say this is a good direction to go for that problem. We don't expect to execute on this quickly. I think it needs to be driven by advanced users and the advanced need. So, like, I know from, this is a thing that, like, GCP
does, internally, when we report against multi-tenancy. When we need that.
we might push it in upstream open telemetry. I think if the browser group wants multi-tenancy across session.
they can help drive this OTEP. What we're looking for with this is just, let's agree on this direction for handling multi-tenancy, let's commit to this as an OTEP to say, cool, we know how we're gonna handle it, and then we can figure out when later.
But that win doesn't need to be right now, is the other thing I want people to understand.
**Reiley Yang** 55:00 Hey, Josh, I have a question. When you mention multi-tenancy, what's the magnitude of that problem? Like, are you talking about, like, dozens of tenants, or, like, millions of tenants?
**Josh Suereth** 55:12 This is, this is, like, dozens, this is not millions, yeah.
**Reiley Yang** 55:15 papers.
**Josh Suereth** 55:16 the specific mechanism, I would not recommend it for millions, especially if you look at what it does to metrics.
**Reiley Yang** 55:23 Yeah, exactly. And for folks who haven't been in the tendency discussion before, I want to give you some examples for you to consider. Like, I'll take Microsoft, for example. There's either host machine, where we have, like, many different teams that build a virtual storage, virtual network, and security layer, and…
like, certificate management. So you can imagine on a single machine.
There are about, like, 20, 30 teams, each building their own thing, and they will need to send logs and telemetry. So this is the dozens of tenants scenario, that you want each team to be able to specify their resource, maybe their team name, or who's going to be accountable, things like that.
But then there's the other situation where you can imagine there's a big, like, storage service, for Azure, and when users use, storage block, they'll provision their own subscription account.
And you can imagine, like, a lot of users, maybe, like, thousands of the users, would be sending their requests, and the requests would be hitting the same machine.
And over time, some users would vanish, and new users would come. So if you look at, like, at one day, how many users are in that particular machine, the answer would be, like.
Probably, like, 1 million. And that's a very high…
like, number situation. So here, if you try to model each tenant by having a dedicated in-memory representation, it works if you have dozens. But if you have millions, then that's not going to work at all. You have to, for example, put the tenant information as part of the dimension or a particular key-value pair.
So depending on the number of tenants you have, the solution might be totally different.
And when we talk about multi-tenancy, I want us to be very explicit, because I've seen a lot of past mistakes where people start with multi-tenant design, and they were targeting dozens, and eventually they have, like, hundreds, thousands, and millions, and they just realize, oh, this entire thing is wrong, they have to redesign the thing.
And when the redesigned thing is working for, like, the… maybe, like, dozens of tenants, it sucks, and people don't like it. So, my gut feeling is maybe we don't have one single solution for multi-tenant. It's depending on what magnitude you're dealing with.
**Josh Suereth** 57:34 Absolutely agree, because we use a different solution ourselves for the millions of tenancy problem. Yeah, agreed. Go ahead, Jack.
**Jack Berg** 57:41 And the situation Riley's talking about might be better solved by,
by pushing on our context extraction mechanisms, we're really poor at that, right? We have baggage, we have context, we have terrible tools for pulling information out of context and appending them to spans, logs, and metrics.
Right? So, you know, that is the first thing that came to mind when I was hearing Riley talk, is measurement processor, span processor that was integrated with baggage and context, and a log record processor integrated with baggage and context.
**Josh Suereth** 58:15 You guys, this is wonderful, this is exactly… Anyway, Jack, that's exactly a point I'd love to make. This is not… like, I absolutely agree, we need more than one solution. There's a context problem I think we have, and we need to solve in OpenTelemetry. This is not it. This is… this is a different kind of multi-tenancy. 100% on board with all of that.
**Reiley Yang** 58:37 Okay, Carlos.
**Carlos Alberto Cortez** 58:39 Yeah, there is… sorry, there is another term that Christian Neumuller have, by the way, on context propagation. Maybe it's time to revisit that one.
I think that's… actually, I was curious about working on that one. I'm not sure if you are laughing, because we were trying… we were supposed to actually merge that in the past.
**Trask Stalnaker** 58:55 For so long, it's been my number one OTEP for, like, years.
I guess that means I should.
**Carlos Alberto Cortez** 59:02 Okay.
**Trask Stalnaker** 59:03 about it, but…
**Carlos Alberto Cortez** 59:04 Actually, I was thinking about opening that up myself, since I still have time. But anyway, let's talk offline, but if you think there's value trust, let's talk about that, and we can work on that.
**Reiley Yang** 59:15 Okay, we're… we have 30 seconds left.
Any final thinking about this?
Okay, then I think we kind of finish on time. Great discussion. Thanks, Arah.
**Josh Suereth** 59:29 Thank you.
**Trask Stalnaker** 59:30 I…
