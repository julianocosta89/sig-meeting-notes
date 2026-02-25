SIG: Entities SIG
Date: 2026-02-23
Duration: 53 minutes
Zoom Recording URL: https://zoom.us/rec/share/8mrBWTQGX_4-HypDYZKW8Y25BkxCSnnhBHlfld9UdD0jdBZjuBcCgZvBYJQfyBKl.gj9SoSUWshzrxkMk
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:30 Hey folks, sorry we were a bit delayed with SemConf.
Ugh, just getting started here.
If you haven't, add to the agenda.
I have a few things I want to grab in, then.
Stillness of the humans.
Retoplas.
Okay.
Alright.
Ian.
Somehow I hit the debug mode.
Alright, can you all hear me?
**Dmitrii Anoshin** 01:12 Yes.
**Josh Suereth** 01:12 Yep. Good.
Can you see my screen?
Beautiful.
**Dmitrii Anoshin** 01:21 Yes, we can see.
**Josh Suereth** 01:24 Alright, I'm gonna grab the project board…
I don't know if this is the best way to review open PRs, because I don't remember if they all show up here, but we're going to start with this and…
go from there. In progress. Alright.
Resource entity, proto message, that's in there.
Exproductive, press key.
Merge algorithm… We'll start with this one.
Yeah.
So this one still has, no approvals.
Okay.
Four days ago, we have otherwise… oh, yeah, spelling errors. Do you possibly access the last requirement bit?
I think we talked about this in the SIG. So for context, this is the entity merge algorithm we're defining, and I think we had aligned on actually being strict here.
Actually, is Daniel here? Yeah. Because I think that was one of your…
**Daniel Dyla (Dynatrace)** 02:28 I am here. Sorry, I was distracted there for a second. What was the question?
**Josh Suereth** 02:32 No, no worries. So this is… I'm just reviewing, like, current status of things. The entity merge algorithm that we need for the specification, currently still has no approvals, but, Tigran made some comments 3 days ago, where we say entity may be merged if and only if their types are the same and their identity
Attributes are exactly the same, and their schema URL is the same, and otherwise we're not merging. Tigrin's asking if we should be more flexible here.
**Daniel Dyla (Dynatrace)** 02:57 Oh, yeah. I mean, I guess the question he's asking is, should we build in schema support for, like, the transformations, right?
**Josh Suereth** 03:07 Because if you can't…
**Daniel Dyla (Dynatrace)** 03:09 If you can't, then you can't merge.
Incompatible schemas.
**Josh Suereth** 03:15 Yeah.
I'm fine allowing schema transformation to be used when merging entities, but I think that this would be the same. So basically, the idea would be they can only be merged
This still remains true. If their types are the same, the identity attributes are the same, and their schema URL is the same.
If we want to allow merging between schema URLs, basically, you have to know that it's safe to move to that version and then merge.
Like, he's saying, what about if attributes used by entities are unchanged between versions?
We don't know if that's the case. We have no way of knowing.
**Daniel Dyla (Dynatrace)** 03:56 Yeah, without support, we have no way of knowing. We could make the assumption that they're not compatible, and somehow encode
You know, have… if you… if you merge to schema URLs.
to differing schema URLs, you take…
The earlier schema version and add it in, like, some blob.
it, you know, a complex attribute, as a record. You would say, like.
One attribute contains all of the…
Attributes from the previous schema version.
**Josh Suereth** 04:40 No, I… I think… Like, again, we want this to be efficient at runtime and kind of sane.
I understand, like, what you might be able to do there, but that's, like, so much work. My thinking is, if we want to do any schema version shenanigans, you have to do so on the entities, and we could make it so that the merge algorithm requires the URLs to be the same.
But the SDK might have access to schema and be able to change the version of the entity to match the other one. If… you see what I mean?
**Daniel Dyla (Dynatrace)** 05:13 Yeah.
**Josh Suereth** 05:15 So you can't merge until you've made the schema URLs the same.
But you could.
**Daniel Dyla (Dynatrace)** 05:20 Yeah, so you just have to upgrade the other one first.
**Josh Suereth** 05:23 Exactly. And so we could allow… we could allow someone to do that.
In the algorithm, but the actual definition of merging in the data model would not allow it.
Does that make sense?
**Daniel Dyla (Dynatrace)** 05:37 Yeah, that makes sense to me.
Is Tigrin here? No, he's not.
**Josh Suereth** 05:42 No, he's on travel this week, so he's gonna be missing pretty much every meeting.
So that, in that event… Expect the following.
Mr. Give me, there's no way of knowing.
If the schema URL was compatible.
With another, looking…
**Daniel Dyla (Dynatrace)** 06:05 schema?
**Josh Suereth** 06:08 The SDK collector.
We'll have to… Look at the schema.
We do convert the version.
Successfully.
We didn't merge two.
Entities that are at the same convergence.
do what makes it allow us to give me that URL.
Based conversions… merge.
outgruden.
What these can be found anymore.
Much more simply.
We leave room for, conversion, conversion.
to this. Okay.
Cool.
Next thing, this is fairly common, please add a few examples to demonstrate what it's doing. Merge entities into resource. Okay, I can add examples, that's fine. And then Dimitri, yeah, my spelling's horrible. Cool.
**Dmitrii Anoshin** 07:18 Yeah, for me, otherwise, everything was good, essentially. I just didn't want to put a…
approval before we discuss the Tigrant's comments, I guess, but otherwise…
**Josh Suereth** 07:29 It was good.
**Dmitrii Anoshin** 07:30 Thank you.
**Josh Suereth** 07:30 That's fine. Is there any… like, I can add examples, that's fine. Is there anything else here that we're worried about?
**Dmitrii Anoshin** 07:37 No, nothing major from my side, I guess.
**Josh Suereth** 07:45 I think I did address this one from December in the… in the… yeah, it's outdated. I think this is addressed, but I didn't mark it as resolved, because I wanted to check.
I'll ping David Asheville to take a look at it again.
Okay.
Cool. So, if folks could, like, confirm, and let's get this one stamped as approved, if we have no concerns, but if we do have concerns, let's get them on the BR.
Gosh.
**Ted Young** 08:12 Is there anyone we should be reaching out to specifically? Like, groups, or… like, who… who would care about this and find out about it too late?
**Josh Suereth** 08:23 So, at this point, we're in the phase of the SIG itself needs to approve, and then we would do the reach-out, is kind of what I'm thinking.
**Ted Young** 08:30 Oh, okay, cool.
**Josh Suereth** 08:31 Yeah, so, like, I… this is feedback that we got from TC and, like, spec meters as well, of, like, hey, none of the entity SIG has approved this BR, so why would we look at it?
your feedback.
Right?
So if the SIG agrees that this is what we want to do, then we go out and advertise and get people to take a look. And yeah, I plan to advertise this in the spec SIG and make it
I already did that. That's where we got David Ashpole and,
Well, actually, and Carlos took a look when we did that. But, I'll do that again, I just, like, I'm waiting until we have approval, because that was the feedback from the first time we did that.
**Ted Young** 09:10 Yeah, that makes lots of sense. Thanks.
**Josh Suereth** 09:13 Cool. Alright, let's go back to other in-progress things we have…
SDK startup specification, I think… did this turn into a proposal in the OTEP, Daniel? I think it did, right?
**Daniel Dyla (Dynatrace)** 09:32 Yes.
It did.
**Josh Suereth** 09:35 Alright, so let's look at the OTEP and the status of that, then.
Oh!
**Daniel Dyla (Dynatrace)** 09:40 Nevermind, not that OTEP. It's not your OTEP, yeah, your OTEP, not Ted's.
**Josh Suereth** 09:45 Right, right, with the revamped one. This is the…
**Daniel Dyla (Dynatrace)** 09:49 And we're… I think right now it's stuck on getting feedback from the browser folks. We've raised it with them a couple of times.
I've been on vacation for most of February, so I'm not sure if any of them have actually looked at it yet. I don't see any of their names in this list.
**Ted Young** 10:07 I brought it up, I brought it up on Thursday, and Martin Kuba took it as an assignment to, to take everything and put it together as a demo for people to try.
So we should get.
**Daniel Dyla (Dynatrace)** 10:21 Yeah.
**Ted Young** 10:22 browser people soon, but I took that feedback to them that we're waiting on.
On browser feedback.
**Josh Suereth** 10:28 Cool.
**Daniel Dyla (Dynatrace)** 10:28 the feedback that I remember is that reading the text, they don't see anything obviously broken or wrong, but without
using… my prototype in combination with Martin's prototype, which is the, session manager.
They don't actually know if it will cause problems or not until…
They've proven that they can work together.
**Ted Young** 10:52 Exactly, it should… it should be stood up end-to-end at this point, and then approved. Yeah, I think.
**Daniel Dyla (Dynatrace)** 10:59 Both prototypes exist and have been shown to work in isolation, but they haven't been used together yet.
Yeah. And Martin took that, as an item on the 19th, or whatever, whatever Thursday was last week.
**Ted Young** 11:14 Yeah, yeah, so hopefully we'll… we'll get to see that in action soon.
**Josh Suereth** 11:20 Yeah. Now, one thing, I don't know if we put authors in this, I don't think we did. So even though you were, like, everyone here was kind of a co-author, and we all contributed into this, I think it'd still be good if,
people who aren't me, Mark, this is approved, from the SIG.
So I think that's, like, Ted, Dylan, Dimitri. If you want to wait for the browser prototype, that'd be fine. I just, again, this is about signaling that we think this is ready for review from broader ecosystem community. I think the most important folks are the browser folks. But… but…
you know, if we don't see any concerns there, I think we should be marking this as approved or getting things reviewed. And I know, like, Daniel, it's awkward because you helped write it and wrote a whole section of it, so you're approving your own section, but…
You know.
just that the signal is what I'm looking for here, of, like, this SIG has reviewed it, we're on board with it, and we, we're ready for other SIGs to take a look at it.
**Daniel Dyla (Dynatrace)** 12:23 Yeah, honestly, the only reason I haven't approved it is because I haven't thought to approve it yet. I'm very familiar with the whole thing, and I am…
I think I'm comfortable approving it, so I'll just do that now.
**Josh Suereth** 12:34 Okay.
**Daniel Dyla (Dynatrace)** 12:35 Nothing's changed drastically in the last 2 weeks while I've been on vacation, right?
**Josh Suereth** 12:41 No, no, no, I… at least I have not done anything. Oh, you know what? I forgot to put these in here. Let me, in our notes, so I'll just… I'll just take a note. We talked about the merge algorithm.
We talked about the,
multi-resource SDK OTEP. Dimitri, I actually want to talk about yours next, while we're in here. I see… I see you have an agenda item for it, but I think we're just going to open up anyway.
**Dmitrii Anoshin** 13:11 Sure.
**Josh Suereth** 13:14 I added one comment. I don't know if that's what you want to talk about. You have collector work and discussion around not-important identity attributes.
Yeah.
**Dmitrii Anoshin** 13:22 I can wait, we can start with this one.
**Josh Suereth** 13:24 Okay.
Cool, so the… I want to talk about… where's my comment?
That's first? Yeah, okay. So this is about, like, what protocol should we use? Again, That one, we don't…
I think we have others, bigger fish to fry.
Okay.
Yeah, this is it. Okay.
So, my last remaining concern is around relationship type, and this might be a big can of worms here, but effectively.
You know, you have examples of relationship later.
And my big open question in my head is.
we have span links, right? And there was a question, I think, from James Thompson that I want to…
double-click on. Wow, that's a Google thing. Anyway,
Do we need attributes on relationships themselves?
Right? Like, is a relationship basically a type?
the actual link, and then a set of attributes that can help describe that relationship in some fashion going forward. Or…
are we okay with just, you know… right now, it's basically just this type string. Everything else is the connection.
**Dmitrii Anoshin** 14:40 if…
**Josh Suereth** 14:41 Good.
**Dmitrii Anoshin** 14:42 I actually added an attribute to the relationship at the first initial version of this PR.
And then, like, after cleaning it up and addressing all the reviews, I remove that. And I removed that, keeping in mind that potentially we can edit, and the current format, data structure for how we define the relationships allows that to be added later on.
So I think, to keep it simple for now, we can just…
ignore it. Because relationships, definition.
Attached to an entity, means that it's descriptive and can change over time of the lifetime of an entity.
So, if any relationship changes, we update the list of relationships.
And it would imply that attribute of a relationship will be…
Descriptive as well, and can change as well, if we add it later on.
**Josh Suereth** 15:56 Yeah, apologies, I was eating a little bit. So, yeah, I…
I can buy that. I can buy that. That's why I wanted to ask the question.
the…
So then the question would be, what is… what are the identifying set of things on the relationship? And that gets into my second thing. I'm fine adding this as a comment to basically address that. That's… that's… that makes sense to me of, like, cool, we can add these in a non-breaking way. If that's true, we don't have to agonize over that decision, we can move forward. Let's document, like.
or have a note of how you would do that? Like, would that be… you'd have relationship.description? Is that what you're saying? Yes. Okay, and it would be a set of attributes? Okay, beautiful.
I'm good with that. So I'll add this as,
That part, but this one here now is the next thing.
Do we need information about relationships, or what the implicit relationship inside of a resource means?
So, yeah, like, there's gonna be a bunch of these things in a resource, and we try not to have relationship information in there. The more we work on our prototypes, and the more you ask questions, the more I'm wondering if
If that's gonna work out.
Because we're getting into awkward things where that could help so much if we had it.
**Dmitrii Anoshin** 17:16 Are you asking about entities in the resource in terms of the first phrase that we are working on, or you're asking about relationships from here to the resource?
**Josh Suereth** 17:26 No, I'm talking about entities in the first phase. One of the reasons why I think it's valuable for you to be doing this is, as we work on the first phase, if we don't know how relationships will be and be used, some of our prototypes are a little awkward, right? Yep.
I can… I can show you some examples of that. But, like, the question would be, do we need to… to…
I have a few questions, but it's mostly how does relationship and resource work?
We know that if two entities are in a resource, there is some form of relationship between them.
Is there going to be an implicit relationship that we can infer?
because entities are in the same resource, like, there's an implicit thing that we would show. Do we want an explicit thing in resource? Like, like, how do they interact together overall? What are your thoughts?
**Dmitrii Anoshin** 18:18 Yeah, I don't think we… we can implicitly say
like, deduct type of relationship, but I would say that if we have several
Entities in a resource, it means that they are related in some way.
So, like, my idea was that we do not…
Pass that information in the resource to not, like, overcomplicate it.
And just make it that if you want to know about relationships of these particular entities.
use the NTD events signal.
That was my original idea.
But even in the current data structure that we have.
I guess it's pretty feasible to add relationship information in a non-breaking way.
If we want to.
**Josh Suereth** 19:26 Yeah, that's… that's kind of what I'm… I'm trying to think through.
Here. So… We believe we can add
relationship information in a non-breaking way. This would be,
So, an entity always has to explain who its owner is, right?
**Dmitrii Anoshin** 19:47 Yes, that's… that's the… that's the one thing, the most important, and I think maybe that one can be…
It can be added.
**Josh Suereth** 19:57 Yeah, that's actually the one I'm a bit nervous about, because I think you don't know who you own, or who your owner is, in resource detection. Let me turn my camera back on now that I'm not chomping on stuff.
Let, let, let's, here, let me, let me… Let me open a new…
spec thing. So it, like, let's look at some of the examples we had, right?
Where's our… oh, OTEPS is top level, isn't it?
**Dmitrii Anoshin** 20:30 I guess we're just increasing scope of the problems that we are trying to solve with the resource. Initially, it was, like, particular small set of problems, and we achieved that. Now we are getting, like, into the field, and we expand them.
**Josh Suereth** 20:48 I think folks are asking good questions, right? So, like, that's kind of… kinda what we're getting at. So here's… here… like, I just want to go through these use cases. Let's refresh, and basically say, can we do this better with resource, or if we had relationship again, just to confirm.
That's all. You could call it that I'm having cold feet, you know.
So, we have, two resource detectors, right? We have, like, the Google Cloud-specific, we have OpenTelemetry one. The OpenTelemetry generic one, we have, like, a generic host detector, a process detector. We know that, relationship-wise, a process is kind of owned by a host.
**Dmitrii Anoshin** 21:26 Yep.
**Josh Suereth** 21:26 But the process doesn't know about the host ahead of time, right? So the only thing it could really say is I'm a process, and there should be some host type that owns me.
So the only thing you could say in resource detection is, like, There's a host type.
What we would get, though, out of knowing the relationship is inside of the resource, we would know, cool, process is the most specific thing.
**Dmitrii Anoshin** 21:53 Yep.
**Josh Suereth** 21:54 And we could construct an identity of host and process together to get a unique identity versus a global one. That's kind of cool.
Service makes things a little more awkward, though, right? Service, process, and host. Service would be, like…
we have an instance ID, we have a name.
That's a unique thing, but the relationship between these two are… is the same as.
You know, not necessarily, like, Like, the service instance is the same as the process.
In this case. It may not be, it may be there's just a relationship. We don't know what that relationship is.
how are you gonna get that relationship in the collector or downstream? The fact that this process and this service are the same?
**Dmitrii Anoshin** 22:39 Yeah, that's an interesting question. We…
I mean, they are both supposed to be on the resource, right? It's just… Yep.
**Josh Suereth** 22:59 Yeah, the problem we're solving here was the fact that there's a generic host, and then there's the Google-specific host, where the ID is different.
And this lets the user decide… we can have the user decide which one to pick by putting either this resource detector first, or this one first, and entities will implicitly get rid of the other one.
But it does mean that this has to detect the full set of host attributes, not just the GCP-specific things.
For that to work correctly.
**Dmitrii Anoshin** 23:24 Yeah, before we pass… Both of them.
We… we can, right?
**Josh Suereth** 23:31 Or our merge algorithm needs to make sure that it knows how to take the generic labels from here and here, as long as the IDs are not different, yeah.
**Dmitrii Anoshin** 23:41 But we should make them different, I guess that's what we discussed.
**Josh Suereth** 23:44 That's what we discussed, yeah. The IDs will actually be different. I still think that we gotta sort this one out. This is, like, the worst one.
**Dmitrii Anoshin** 23:52 If we go to… if we go to some of the other ones, it's a little easier. This is the one I think is well supported, which is…
**Josh Suereth** 23:57 I have a process and a service that come down. I have hosts and AWS, and I can attach them. That one's… that one's dead simple.
This is the… this is the one I mean. So, if we have a resource provider that texts a host and something that texts a service, when it gets to the collector, the collector can say, oh, I'm on a different host, and it won't attach all the labels… it won't overwrite any labels, right? It'll know that it's different, and the merge algorithm will prevent that.
This is the one that we, like, are really targeting with V1.
really well. This one, I still think the issue here is I don't think GCP should be doing this at all.
With host ID.
And doing host ID shenanigans. I…
I think that we probably need a way for this thing to do its lookup appropriately.
Independently. And that we need to know that this, you know, which one of those to pick.
**Dmitrii Anoshin** 24:57 Yeah, I guess we are… Again, discussing different problems here, like…
**Josh Suereth** 25:02 Yeah, yeah.
**Dmitrii Anoshin** 25:03 I, I'm… So, I'm not sure which…
Like, problem we can help with introducing relationships into the process.
**Josh Suereth** 25:13 Into the resource.
**Dmitrii Anoshin** 25:16 What can we make?
Better.
What can we resolve with adding relationships?
**Josh Suereth** 25:25 Yeah, yeah, yeah, I, I… I'm, I'm thinking, sorry.
I just have some intuition, that's all. So, first off, the fact that service and process are somehow related.
**Dmitrii Anoshin** 25:38 I don't think we have a way to extend that relationship at all.
**Josh Suereth** 25:42 That's only implicit in the resource today, right?
**Dmitrii Anoshin** 25:46 Yep.
**Josh Suereth** 25:47 Maybe that's fine, maybe there's no problem we have to solve there.
**Dmitrii Anoshin** 25:50 We can. It's… that doesn't stop us. Nothing stops us from that. We can add a relationship between process and service.
I guess it's gonna be run zone, service run zone.
**Josh Suereth** 26:03 Yeah, service runs on process, yeah.
**Dmitrii Anoshin** 26:06 Yeah.
And on the backend, it would end up with many-to-many.
**Josh Suereth** 26:12 With that, yeah, this is… I think this… was this the other one? Oh, this is where it was host to, right? Where they can't merge.
What was this one? This is the schema difference, that one's fine, we can handle schema changes… I think that was it. Okay.
So really, the main problem we have is still this frickin', the fact that we have two hosts.
And technically, the identity is different between the two.
**Dmitrii Anoshin** 26:39 Yeah.
**Josh Suereth** 26:42 And you're right, I don't know if,
A relationship would fix this, necessarily.
Right?
**Dmitrii Anoshin** 26:51 But I think… It can be…
Useful to add that information to the resource.
**Josh Suereth** 27:03 Yeah, yeah, let's go back to what you have.
**Dmitrii Anoshin** 27:08 Let me think about it more, and maybe I'll reply with… some… Yeah, I wouldn't…
**Josh Suereth** 27:16 I want to go to your relationships that you have, right? You have runs on, scheduled on, contains, part of, depends, manages, and hosts, right?
We're thinking that, like, the service instance and process would be runs-on relationship?
Right?
**Dmitrii Anoshin** 27:35 Yeah, I guess because it's logical to infrastructure, essentially.
**Josh Suereth** 27:40 Okay.
**Dmitrii Anoshin** 27:43 This one is, like… example is not… it's not very good, because it's infrastructure to infrastructure, essentially.
**Josh Suereth** 27:50 yeah, I think that one could literally be a runs-on dependency, too. Like, that's… that's the…
the two things I wanted to do is basically, I wanted… I want us, if possible, to kind of go through our…
sets of use cases, and make sure that we have the right set of relationship types in this. Because you're… by the way, because you're going directly to a PR and not an OTEP with this.
Much higher standard.
For what we're going through, like…
**Dmitrii Anoshin** 28:18 Should it be OTAP? I can make an OTAP, and in that case, I can expand, I can also, like, bring relationships to resource if needed.
**Josh Suereth** 28:28 I… I think I would have preferred this to be an OTEP initially, because again, with an OTEP, we can agree on the direction. When it's in the specification, all the pieces have to be things that we are committing to and aren't locked down in the future.
So, there's a bit of a higher bar. So, in that case, what I want is… if you want to get this in to the spec, I actually think we're pretty close. So…
if we say that we can add relationships in a non-breaking way in the future, which you're suggesting and I agree with, great, but then that gets down to what's the identifying piece of a relationship.
And I think the identifying piece is this type.
And I would want to actually go through you have some examples?
I want to go through… I wanna go through these and say, like, okay, cool.
Is runs on and scheduled on both needed, or are they basically the same?
Like, could we… could we… somehow…
go down to 1, because when you say logical entity runs on infrastructure, process to host.
I actually think a pod is a logical entity.
And I don't think a process is one.
But I think it's, it's like some sort of workload to infrastructure
thing, right? I have a thing I need to run, and I'm running it on something else. And I think runs on…
Totally makes sense. Contains, I get… You know, when, A pod contains a container.
We… well, the other thing is, if we only have child-to-parent relationships, you wouldn't have contains.
So, you know, anyway, this graph I think we want to go through.
**Dmitrii Anoshin** 30:17 I, I actually, I actually put, like, added this one in an OTAB style, this, like, this…
The standard isn't
this set of relationships here is more like an example for future improvement, but I see what you're saying. This probably should be more well thought through and well-defined as a, like, standard set of types that we can stick to.
**Josh Suereth** 30:43 Yeah, I'm fine. If you want, for the spec PR, make this be a to-do, and in an OTEP, put the proposal for what they would be for us to discuss, that's fine. If you want to just, in this PR, mark it as to-do, and move this into a separate PR that we can just… like, how do I want to phrase? The discussion of what these should be, we need to have, regardless.
**Dmitrii Anoshin** 31:03 Right, right.
**Josh Suereth** 31:03 Yeah, what I don't want to do is hold up the… a lot of the important decisions we've made on entities for the spec because of this discussion.
**Dmitrii Anoshin** 31:11 Okay.
Sounds good.
**Josh Suereth** 31:13 Yeah.
Cool. Do we want to dive into any more of that, or should we move on?
**Dmitrii Anoshin** 31:19 We can move on.
**Josh Suereth** 31:20 Okay, let's see, so if we come back to…
just other… I think there's one more entity PR in here, right?
Oh, that one, that one will be fun. We can talk about that one later. So we have merge algorithm, entity events,
And then we have context sharing, which… this is a PR unrelated to our group, but they're asking questions about this.
I'm gonna defer that discussion for later. I think if you guys haven't read this OTEP, from Obi, and for context process sharing for, the EBPF-based instrumentation, please take a look. I think they're actually kind of in line and understand the problems now.
But they just needed some help understanding entities.
Okay, cool. So that's spec work.
What else did we have? We had developed strategy for asynchronous resources and entities, and Daniel, I think you have that strategy, right?
**Daniel Dyla (Dynatrace)** 32:36 No, I don't think so. Oh, yeah, this was the… yes, yeah, yeah. So…
Yes, in terms of, it's implemented in the prototype. No, in terms of I have not written down
Like, a, proposed specification for it.
**Josh Suereth** 32:57 Okay.
And it was, 2026 to… 23… Implementation.
Oh my god.
JS Prototype.
You just need to bring the specification down.
Cool.
**Daniel Dyla (Dynatrace)** 33:20 The main, the main limitation is the same that we have talked about a couple of times, which is that you need to know the keys.
synchronously.
**Josh Suereth** 33:34 Yeah. In order for the merge algorithm to work.
Yeah, agreed.
Alright, limitation, please.
This must be known.
Synchronously.
Brilliant.
I'm driven.
to work. Okay.
Cool.
Let's,
let's move on. So that's all the in-progress stuff. Let's go, I think, Dimitri, you had a,
You had another discussion topic here?
**Dmitrii Anoshin** 34:11 Yeah, I wanted to quickly just give some update on the collector work and bring some discussion, if you…
Sure, give me that.
**Josh Suereth** 34:23 Do you want to take over presenting?
**Dmitrii Anoshin** 34:25 Yeah, I can do it.
**Josh Suereth** 34:26 Okay.
How do I… there we go, stop sharing.
**Dmitrii Anoshin** 34:31 So, the thing is, is that in the collector.
we, like, always rely on the metadata, and I'm sorry.
And, like, even if… we… my work from the… for the enrichment, right?
of the, like, in the processors, essentially.
It's still, like, most of the things are related to metadata, even
how the documentation, or how configuration is generated, etc. So, this is…
I started with metadata YAML to, like, make some things to be streamlined. Essentially, what we currently have is that we have a set of… we used to have, I already, like, experimented in changing this.
We have a set of resource attributes that can be enabled or disabled, but it generates Go API when you can create a resource, you can add attributes.
And, to those resources, and they can be disabled or, enabled by the users.
it's… the thing is, is that the generated API doesn't provide you a way to specify which particular metrics are attached to
particular resource attributes, and that's super unclear in the,
makes it, like, for example, we have namespace UID, namespace name, we have note UID, note name, etc, and, like, a lot of resource attributes that can be potentially disabled, enabled by the user, but we also have metrics that are not necessarily attached to particular entities.
So, with the entities work, I wanted to resolve that issue as well.
And if we go back… if we go to main… that's why I also needed the relationships here. So I added entities.
For now, I just, like, reference resource attributes that I defined before.
So, for example, for namespace, there is a name UID, namespace UID, namespace name, and from that, I can generate
like, specifically which metrics are associated with particular entities. So, it's, like, it's going pretty well. I'm, like, I'm…
It will be much cleaner, and metadata eventually will represent
Like, particular metrics can be associated with entities, and, like, it'll give users a good idea of what is emitted.
In the resource, what is emitted in the metrics. The thing is, is that even if we have namespace UID defined here, and even if it's enabled by default right now in the metadata YAML, currently in the collector, it's not always set.
Because there is another, like, method that is supposed to set it on the resource. So, essentially, this one is pretty much disabled all the time, but namespace name is added to almost all of the metrics, because it's pretty important.
So that's why… that's the place where my, like, my approach breaks a bit, and I need to resolve it.
So, a way to resolve it, because I'm adding, like, all of these entities with all the relationships, so I'll figure out if I have a relationship to that additional entity will be added to the resource, it'll be done, like, automatically generated.
In Go API, but… The problem is that this one…
For backward compatibility, like, it will be harder to adopt, because
sorry, namespace UID. Namespace UID isn't said, isn't said anywhere. I'm sorry for rumbling, but I think I, like, making some sense out of it. So, essentially.
This is… identifying… attribute of an entity.
of a namespace entity that is potentially supposed to be added to almost all of the metrics, because, like, if you report in pod metrics, you'll get pod and namespace. If you report, like.
some… if you report node metrics, you will not get this, but if you report replica set matrix, you will get it. If you report pod metrics, you will get it, etc. But it's currently disabled. It's currently not being emitted.
So, but namespace name is always emitted. So, I'm like…
I have an option here, whether add namespace UID
aggressively to all of those metrics. In addition, and disallow it, disabling it.
Or, I… like, the option I'm thinking about is that
I allow disabling identifying resource attributes.
And in that case, I keep it, like, backward compatible, and nothing breaks for the end users. So in the resource, it will be, let's say, pod entity with pod UID,
and reference… it will be relationship to namespace entity, but namespace entity will not have UID, will only have descriptive namespace name attribute.
Does it make any sense?
What I'm… what I'm saying?
Do you get the idea here?
**Josh Suereth** 39:59 Oh, I get the problem.
Okay, I'm gonna ask something more fundamental.
Is namespaceName the actual identity users want? And we chose UID instead.
**Dmitrii Anoshin** 40:11 That's a… good question. I…
Like, namespace is unique within a cluster.
I guess we went with UID for more, like, consistency approach, because we're taking UID for all of the other
objects, Kubernetes object, so it's like, why would we go with native to name?
As there is… as an identifying attribute instead?
But potentially, that's another way to solve it, yes. We can make namespace name identifying attribute, and make namespace UID a descriptive attribute, and it'll be the only exception from that, like, approach that we take for other.
**Josh Suereth** 40:57 Are you… yeah, you're not running into this issue with, like, pod name, or node name, or anything like that?
UAD is actually used in those cases as well?
**Dmitrii Anoshin** 41:10 Actually, UID is rarely being used by the users in general.
it's, like, it's mostly to specify uniqueness, global uniqueness, essentially. But within the cluster, even pod UID, I guess, pod name. Actually, I'm not, like, an expert in that field, but I think it's…
it's… Uniqueness, For the port only… uniqueness of port name only guaranteed within the namespace.
So we would need to make the namespace kind of, like, parent entity in that case, or something like that.
**Josh Suereth** 41:52 Right, right. If you… yeah.
My… my…
**Dmitrii Anoshin** 41:57 This could be because I have a Google Cloud lens.
**Josh Suereth** 42:01 But when I've seen people do observability here, they tend to send the triplets.
Namespace, pod, and container. Or, namespace deployment and pod, right? As, like, a triplet.
of identity. And the deployment is kind of like part of that namespace, the pod's part of the namespace, and that's kind of what they use. And so they might look, you know, grouped by deployment, they might group by…
pod,
But they always send, like, the namespace and the thing when they send both, like, when they're using the strings. But we see, more commonly.
Again, this is anecdotal evidence.
Like, name-based identity here.
And theoretically, our model could handle it.
It's more a ques… like, to me, it's more a question of what…
We know that that's what users want.
is, like, they want these strings. That's, like, the most useful. It's that whole notion of what I call the navigational identity when we did that initial proposal, right? They need to navigate, and to navigate, the UIDs are useless.
**Dmitrii Anoshin** 43:08 I don't really know or care what that is as a human. The actual name is what I care about to navigate down to something useful.
So…
**Josh Suereth** 43:20 it makes sense to me that they want the navigatable name and not the ID. And this gets into…
a lot of our early discussion around identity. Yeah. We do have telescoping identity, so we could actually say, you know what?
The identity for namespace should be the name.
and the identity for these other things should be the name, and we're gonna have a telescoping identity there. We could go the other direction and say the ID is required, and what we're gonna do is, for half these Cates users, say, cool, you're not using entities.
the ID's dropped.
**Dmitrii Anoshin** 43:56 What do I mean by that? You notice entities, I…
**Josh Suereth** 43:59 So, you can do resource detection, but effectively, like, what's the value of an entity bundle where we don't have an identity to do any comparison later?
**Dmitrii Anoshin** 44:17 Not sure I followed this question.
**Josh Suereth** 44:21 Okay, so, you know how you're saying, like, you would make identity be an optional thing?
For an entity?
**Dmitrii Anoshin** 44:30 Yeah, that's an interesting approach, yeah. Like, making the identity optional, something like that.
**Josh Suereth** 44:36 Yeah, except it gets… you're not really using entities anymore, right?
**Dmitrii Anoshin** 44:40 Yes.
**Josh Suereth** 44:41 You're just doing raw attributes, so…
**Dmitrii Anoshin** 44:44 But, like, my point here, can we, like, let's say, not… So, we have…
I mean, I don't want to… may… make it…
A human-readable identity be the priority?
Because, I mean, UID is here for, like, providing global identity, right? And if we have it, it's better to have global, even if we are thinking about some particular, like.
particular namespace or anything, because it'll…
I mean, it's just there, it's just UID. I think it makes more sense to use them instead of switching to something else. But, like, making them optional, and let's say, providing a concept of
quote-unquote invalid entity, and how to work with them, that's also something that we can explore.
So, for example… yeah, go ahead.
**Josh Suereth** 45:51 Yeah, would you send that over OTLP? Like, I would argue you could do that internally to the collector, but the outgoing OTLP should not have the entity, it should have raw attributes, right? Because, like, I'm attaching namespace name, but I'm not attaching the namespace entity, because I don't have its… I don't have its identity.
**Dmitrii Anoshin** 46:08 Okay.
**Josh Suereth** 46:09 There's a… there's another… so I'd say, with the model way of the day, that's what you're doing. You're just attaching the raw attribute. So if you want to have configuration in the collector, where you can attach raw attributes from entity detection, instead of the full entity, great. Like, I want to attach the descriptive attributes, but not the identity, cool.
That said.
**Dmitrii Anoshin** 46:29 Just get your partner before the resource.
What? Descriptive attributes for the resource, we're not putting them in all the entities in that case, right? Or picking up…
**Josh Suereth** 46:36 Okay. Exactly. It'd be on the resource. So the resource would have it, I have access to it if I need to do a quick filtering or whatever, but I don't need the full entity there.
The other alternative here, and I'm gonna throw this out there, this is another horrible one.
Is allowing a different identity.
attributes for the identity.
**Dmitrii Anoshin** 47:00 That's what I was thinking as well, but how to make it work, and how to, like…
**Josh Suereth** 47:07 Yeah, that's… that's a can of worms that's, like, a month's of work for us to figure out, right? So I don't want to open that can of worms, I'm just gonna call out, like, maybe…
I think we agree on what we want in the end. We want users who rely on name.
for that navigatable identity. They need it in resource. So, whatever we do, we have to give that to them, or they can skip the ID and just keep the name for now.
Ideally, the value you get from entities over time is so good that they will eventually want the ID in there.
Okay. And that the backend systems could have, like, the strings, right?
**Dmitrii Anoshin** 47:46 We'll see you, Daniel.
**Josh Suereth** 47:47 So, like, if we do our job well with entities, eventually users will want these IDs.
**Dmitrii Anoshin** 47:55 Is another way to think about it.
**Josh Suereth** 47:57 And that they prefer them, and they'd prefer having a minimal set of IDs, and then all the descriptive things kind of get layered in over time.
Yeah. That's… that's… if we've done… if we're successful.
And then, in that design space, like, I think we have a lot of room.
**Dmitrii Anoshin** 48:13 Okay. I think that's the most viable… the best approach here. So, essentially, even in the configuration interface that we generate here in Metadata YAML, we have, like, a section called resource attributes.
With all of them listed in one list, and users can enable, disable each of them.
So I think we can keep that, and if they disable an identity attribute of an entity, we just don't set that entity, it's… but all the resource attributes of that entity, if they are enabled, resource attributes, descriptive attributes of that entity, if they're still enabled, we put them on the resource.
Okay, that makes total sense to me.
Yeah, and I'll… I'll go with that approach here, and then I'll… I'll move towards processing side of things, like, this, like, Kubernetes attributes processor and everything, and I'll model… model that in a way to…
handle those cases as well. So, if we don't have entity, it means that potentially we still can have things on the resource, so looking at the resource at backward compatibility.
it would mean that we will stack with the resource attribute for a while, but I guess once we reach that state, when we are, like, have pretty stable foundation, when we have both of them, we potentially can at least think about moving towards the entity, like, going forward.
From resource attributes, okay.
**Josh Suereth** 49:50 And this is one of those things where we want people to continue to be successful at what they do today.
And the thing we're adding has to be high value.
So that they are encouraged to move to it, as opposed to, like.
We force them to by breaking everything, right? That's not what we want to do.
**Dmitrii Anoshin** 50:08 Okay.
**Josh Suereth** 50:09 Yes.
**Dmitrii Anoshin** 50:09 Okay, makes sense. That… thank you. I guess… and in that case, we don't… we still can have the namespace UID as an identifying attribute, but if the users don't care about that, they can just disable it, and they'll have, let's say, resource attribute for namespace name everywhere else.
**Josh Suereth** 50:27 Cool.
All right, we're… I think that was the last agenda item. I did want to say hi to Fernando, thank you for joining us. I saw that you wanted to just listen, so I didn't…
Say hi earlier, apologies, but just want to say hi, welcome, and if you had any questions or anything, we have 8 minutes left, but otherwise, we'll call it early.
Oh, I can't hear you, I don't know if…
**Fernando Okuma** 50:58 Can you hear me?
**Josh Suereth** 51:00 Now I can.
**Fernando Okuma** 51:02 Oh, good. This is the first time that I participate in Open Telematry Agenda, so I'm just getting familiar to…
How the process works in… Yeah, just watching. So…
I… I hope that I can…
Contributing to, any, any initiatives Well, early soon.
**Josh Suereth** 51:32 Well, welcome, yeah, if you have any questions or anything, like, let us know. We unfortunately don't have…
We're in the middle of a bunch of proposals, as you saw, but we do have a lot of prototyping work, so I'll… for the next time we meet, or I'll try to get a list of, like, low-hanging fruit that we could use help. We have a lot of stuff that you could help with. I don't know if any of it is, like, easy to get started with, though.
**Fernando Okuma** 52:01 Oh, okay, no problem.
**Josh Suereth** 52:02 Yeah, yeah, so, so, yeah, I don't know if you have anything, Dimitri, or if the list of, like, collector work is anything that could be interesting, but if you have any questions, or you're interested in contributing, or looking for areas, happy to, happy to help, and happy to have you.
**Fernando Okuma** 52:17 Good, thank you. I… I use the OpenTelebetween .NET application, so I just try to… to get familiar to contributing any… anything, so…
And I'm from Brazil, and my English is not… not so good, but I… I try to communicate, so… that's it. You need to take, some patience with me, but…
**Josh Suereth** 52:43 No worries. I'm from, you know, the United States, and my English is also not the best, and it's the only language I speak.
So, you're already better than me, yeah.
**Fernando Okuma** 52:53 But, so that's it. Thank you, and… .
**Josh Suereth** 52:59 Alright, yeah, thanks. Thanks for joining, and we'll call it here. Thanks, everybody. See y'all next week.
**Dmitrii Anoshin** 53:04 too, right?
**Fernando Okuma** 53:05 See ya!
