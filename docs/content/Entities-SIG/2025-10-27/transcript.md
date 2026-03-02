SIG: Entities SIG
Date: 2025-10-27
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:52 Hey, sorry I'm late.
**Dmitrii Anoshin** 01:56 Hi, everyone.
**Josh Suereth** 02:02 Okay.
Just as an FYI, I might not be able to make the next Monday's meeting.
And then… I think after that is KubeCon.
So…
**Dmitrii Anoshin** 02:20 Hi, everyone.
**Josh Suereth** 02:21 I will be at KubeCon, yeah.
**Dmitrii Anoshin** 02:26 Any talks related to entities already? No?
**Josh Suereth** 02:31 I put in to do one at the hotel booth, but I don't think… I don't know if it was accepted or not. I didn't check. I have, like, a thousand emails I have to get through. Apologies.
I'm a bit behind on everything this year.
**Dmitrii Anoshin** 02:46 Yeah.
**Josh Suereth** 02:47 But there's…
Yeah, as far as I know, there's nothing on Observability, Day that I know of on entities. So I do think…
Well, anyway, we do need to talk about our timelines and things. Dimitri, you have a topic, and then, the other topic I wanted to do was,
See if we can go through Daniel's, prototype.
**Daniel Dyla (Dynatrace)** 03:11 No, today is not gonna be a good day for that. I was hoping to get it ready for today.
**Josh Suereth** 03:15 Alright, okay.
Yeah, I think, we need to check our timeline then, too.
**Dmitrii Anoshin** 03:31 I'm not going to this KubeCon, but I really want to go to Europe, and I need something to submit, at least for observability dates, so if you folks want to go, let me know, maybe we can do something for entities.
**Josh Suereth** 03:47 I… I'll check with my management to see if I'm…
how much travel I can have.
Yeah, we're not supposed to go to all of the conferences, and there's a lot in open laundry space. So, usually, I have to pick one. We'll see. Alright, let's go through the issues, though. How about we get started?
**Dmitrii Anoshin** 04:08 Sure, sounds good. Alright, attribute field names inconsistent.
**Josh Suereth** 04:12 Let's see…
**Dmitrii Anoshin** 04:13 Yeah, this was, like, caused by some comments that I'm… on the collector work that I'm doing, so we have, like, inconsistent,
Different, like, let's say…
wording for descriptive and identifying attributes, and I think it's something that we better to resolve early on, rather than keep doing it. So…
**Josh Suereth** 04:40 So, so… Where do we use identity, I guess is the question.
**Dmitrii Anoshin** 04:45 I think we… we don't use it.
anywhere, but… is it actually schema? Latest viewer schema?
**Josh Suereth** 04:54 Coke.
So, Weaver, we got… right now, we have identifying.
And descriptive in Weaver, but we're moving it to be identity and description.
**Dmitrii Anoshin** 05:05 Okay. But we can make it be ID and description, that's fine too.
But, yeah, and identity is fine as well, as long as we are doing description instead of descriptive. Because in our proto, we have description and ID.
And by ID, it would likely mean identity instead of identifying, if we use nouns instead of object.
**Josh Suereth** 05:29 Yeah, so if you look at, if you look,
I guess we'll just look at semantic conventions quick. So, if you look at what we have today, this is just because we adapt to the existing crap that we had in semantic conventions. And I shouldn't say crap, the existing, like, setup.
So, for service, right, we have, under entities, you have a role which is identifying for an attribute.
What the new schema does, though, since we actually call it an entity to begin with, we can just, instead of having attributes with a role, we can just say ID and description, and then have the attributes listed underneath it. And that's totally fine.
**Dmitrii Anoshin** 06:07 That makes sense, but… and still, still we need to define the wording against… when we say attribute of an entity attributes, are they identity attributes or identifying attributes? Are they descriptive attributes or description attributes? And the same for the keys, if we… when we talk about.
**Josh Suereth** 06:26 Yeah, yeah. What I wanted to phrase, and I think this might be in the spec, was you have an identity… an entity has an identity and has a description.
**Dmitrii Anoshin** 06:37 And the identity is a set of attributes, and the description is a set of attributes. So…
**Josh Suereth** 06:42 When we look at…
**Dmitrii Anoshin** 06:43 It will be identity attributes and description attributes in that case.
**Josh Suereth** 06:48 Sure, yeah.
**Dmitrii Anoshin** 06:51 I think it makes sense to me.
**Josh Suereth** 06:54 Yeah, what… the tick model… Well, we call it an ID, attributes that identify the entity.
So we could change that to identity, but I think ID is fine. Again, I don't care.
**Dmitrii Anoshin** 07:05 Yeah, ID is fine. I'm just… like, my issue that's submitted is against whether we use adjective versus nouns. Like, identifying versus identity, or description versus descriptive. Because it's, like, it's inconsistent in everywhere we… it's different things, and when I submit PR against
collector, I've got two people complaining about, hey, why is… why do you say identity and description versus, like, everywhere in the docs we have identified and descriptive?
**Josh Suereth** 07:41 Where do we… where else do we have identified and descriptive?
**Dmitrii Anoshin** 07:45 I believe if you… the…
**Josh Suereth** 07:46 Identifying attributes, yeah, okay, got it, got it.
**Dmitrii Anoshin** 07:50 Yeah, and, like, and all tabs as well. So, if we align… align here that we use identity attributes and description attributes, are we gonna just submit a PR to, like, make it this way everywhere, and we don't have that commence anymore.
Hear… hear this as well.
So it will be identity attribute.
**Josh Suereth** 08:10 I think what we want to say instead, this would be identity.
**Dmitrii Anoshin** 08:15 Yes, that's.
**Josh Suereth** 08:15 Take out attributes, right?
Or,
Or we'd say attributes of identity. So the problem is, this is just English, right? Like, the… calling it identifying attributes are the attributes that compose the identity.
So, like, we don't want… we don't want noun-noun, we want adjective-noun, you know?
**Dmitrii Anoshin** 08:39 I see.
**Josh Suereth** 08:40 Yeah, I agree with you, we should be consistent here.
And I think in code, we should always use nouns, if possible, for these things where they are, right?
So calling it identity makes sense.
**Dmitrii Anoshin** 08:53 So, do you want me to change this wording, or do you want to still keep identifying attributes somewhere?
**Josh Suereth** 09:01 I… I… like, here where we say description is the descriptive attributes of the entity, or the non-identifying, that, I think, is fine for, like, the definition of what description is.
But, like, getting… changing succ… you know, we talk about minimally sufficient identity, we talk about repeatable identity,
you know, getting rid of it here and using consistent terms, I'm fine with, yeah.
**Dmitrii Anoshin** 09:28 Okay, I'll… I understand your point, so I'll try to see when it's, like, when it sounds to change adjectives to noun, when it's not, I just want to leave it as this.
I'll close that, that, issue with the wording that we want to use, nounces.
As much as possible, if there are some concerns about naming.
**Josh Suereth** 09:53 Yeah, well, here we should definitely change it to identity and description.
**Dmitrii Anoshin** 09:57 Hmm, okay.
**Josh Suereth** 09:59 Right.
And we can call it, like, identity attribute keys and Description Attribute Keys. That would work too, right?
Because this isn't actually the identity, this is just the keys which would make up the identity, so…
**Dmitrii Anoshin** 10:12 Okay.
**Josh Suereth** 10:13 Yeah.
**Dmitrii Anoshin** 10:13 Okay, makes sense. I'll…
**Josh Suereth** 10:16 So, yeah, okay, I think it's a good cleanup. Did you already open a PR about that, or.
**Dmitrii Anoshin** 10:20 No, it's just initially, I just wanted to discuss it first, because typically, it's… like, I'm creating Go API, and I use the identity and description terms there, ID and description terms there, and I'm getting, like, comments, wise description and description.
**Josh Suereth** 10:42 Yeah.
description?
Identity… attribute keys… Identifying attributes.
Alright, cool. Next up is this one, right?
**Dmitrii Anoshin** 11:01 You're… yes, this one, yeah.
And, I, I, addressed your comment.
**Josh Suereth** 11:11 Oh, right, failure scenarios. Approval to be added to-do…
Alright, let's take a quick look.
Entity type uniqueness and attribute ownership. So, all entities associated with a resource must have unique types, and two entities within the same resource can share the same entity type.
Fixed identification, yep, this looks good.
Retreat ownership must be owned by at most one entity within a resource.
For… and this is where we can say, for identity.
**Dmitrii Anoshin** 11:43 Yeah.
**Josh Suereth** 11:43 For attributes of identity, ownership is implicitly enforced by a combination of any type uniqueness, and prefix naming convention. For description.
attributes, or attributes of description. Ownership is determined by the placement rules described in the section… following section.
**Dmitrii Anoshin** 11:59 So this is the permitation note I added after your comment.
**Josh Suereth** 12:09 Okay.
Alright, yeah, this looks good to me.
**Dmitrii Anoshin** 12:27 Okay, thank you.
I'll update wording to avoid adjectives here.
Yeah.
**Josh Suereth** 12:44 Cool.
Alright, let's do a quick recap on prototyping efforts, then. I got, a little bit distracted with, Weaver, and doing the Weaver v2 syntax, and then I got distracted with, re-implementing the entire SDK from scratch to use mem-map files to dump things out of process.
That's… that's… that's what I did on the weekend, though, so that's… that's, like, you know, fun time. So I didn't have a chance to actually update my… my prototype, where I think, actually,
I think my prototype is going to delete half of the code that it had, and be totally fine, for the new PR.
Let's actually take a look at the OTEP.
Let's see if anyone has anything they've written to it. Type uniqueness…
**Daniel Dyla (Dynatrace)** 13:43 There are no current, there's no open…
what do they… what do you call them? Threads, comments, whatever it is?
**Josh Suereth** 13:50 Own it, okay.
**Daniel Dyla (Dynatrace)** 13:52 I have been working on a prototype… my… my prototype from the last version was already…
Somewhat close to this?
But I am currently stuck in…
what I would call unrelated problems, to do with
our metrics SDK was never designed to take a meter provider and clone it.
So… I thought it would be as, you know, a simple case of just creating a new meter provider with the same options, but it isn't working out that way.
So… it's requiring more changes to the internals than I thought. Not… Anything to do with,
You know, nothing required by the spec, so it's nothing that would be breaking or external to users or anything like that, it's just…
it's taking me more time than I expected, and…
I didn't have as much time to work on it last week as expected either, so I would say I need another week.
**Josh Suereth** 14:56 Okay.
I'm in a similar boat of, basically, I'm throwing away my previous prototype, because I had all of the listener help.
And I want to get rid of that, so I'm going to reboot the prototype, which is just a lot of copy-paste, or convincing a LLM to copy-paste, and it doesn't know
What is important and what is not, and overdoes it, so…
One of the two. Anyway, okay, so we'll…
We'll keep working on that. I think the…
the implementation of the SDK from the Java side actually isn't going to be quite as terrible. It's more,
I want to make sure two things happen from this prototype and this OTEP.
One is, as soon as this OTEP is merged, I want to start executing entity and resource detection as quickly as possible on the spec.
Because I think that's what will actually unlock entities for all of OpenTelemetry.
And with all the work Dimitri's doing in the collector, we need to get him entities.
So, that's… that is actually…
one of my number one focuses with my prototype is to make sure the SDK-related work is solid. Now, I want to go back to, if we look at the previous OTEP we had.
And the current state of the specification. But if we look at the previous OTEP we had.
around resource and entities, okay? We had data model changes, that we're making, and then,
some approach on improvements. So.
First off, we wanted to make a new set of entity detectors, where we can preserve existing resource detectors, but we created a new thing.
And this needs to interact with,
the resource detection config spec, in my opinion, of, like, what does it mean to say the service detector's on? I want that to be the service entity, right?
we have this notion of a new resource provider component. Question.
I guess it's just you and I, Daniel, from the SDK standpoint. Do we need…
The resource provider component, here.
I like…
**Daniel Dyla (Dynatrace)** 17:11 So…
**Josh Suereth** 17:12 Go ahead.
**Daniel Dyla (Dynatrace)** 17:13 Right now, no. It depends on how we want to implement… right now, resource, and by extension, entity.
is not… an API concept at all. It's an SDK-specific concept.
If we want instrumentations to pass entities to do, like, meter provider for entity or whatever in the instrumentation, we have to extend the entity to be…
an API concept.
And add an API type for that.
Right now, I've done that by just defining
a type. Like, if it could… an object that conforms to the type is an entity, and that's that. I did not make, like, an entity provider, there's no mechanism for interacting with them, or anything like that, and it's working out just fine.
And then because… The resources known at construction time, or at the time that
You, you do the entity for, or, you know, binding, or whatever it is that you're calling it.
Again, there's no need… like, the resource provider would handle…
changes over time, and those are not… I don't have that concept in my current prototype at all. You just construct a new provider if you change something.
Yo.
Right now, I have no need for that.
**Josh Suereth** 18:42 The main thing… the main thing I want to sort out is an entity detector.
And then we have this notion of, like, merging resources and things that we need to write somewhere, and an environment variable entity detector that someone needs to be able to register. So, like.
I want to add those concepts, but I agree with you. Inside of Java, we actually were able to do everything but just modifying resource to support entity.
**Daniel Dyla (Dynatrace)** 19:10 Yeah, and that's exactly what, like, our… our resource detection pipeline, I guess you would call it, is just in, like, the SDK startup process. There's no,
There's no resource provider component that we're interacting with, and certainly there wouldn't be one in the API.
**Josh Suereth** 19:30 there is a resource provider component in the SDK in Java, but I still think we… the whole SDK startup mechanism probably should get specified at some point, but that's a… that's a… that's a different issue. My question would be, if we started to get, things written down, I… I think…
the thing you did with entity is exactly what I'm doing as well. It needs to be an API capability to create an entity.
Because of how we're gonna do things. And the current OTEP has an API capability. But in terms of what we would do here, besides ignoring resource provider, the rest of this, I think we can actually execute on in the spec now. Like, I think we're unblocked on that.
of… there will be entity detectors, there'll be merge logic for resource, that sort of thing. Do you think we have enough that we could write the specification? Like, I can take… the prototype I had for this OTEP still exists.
and is close enough to what we're doing. This is our entity merging logic for resource, right?
I think, can we start moving some… and the environment variable detector, you know, Dimitri already provided the actual details of this, we just need to define that a detector would exist, that you can address in config that does this thing.
Should we start writing specification for this?
**Daniel Dyla (Dynatrace)** 20:50 Yeah, and my SDK batches a lot of this. Like, even the merge logic, when I do, like, meter provider for entity.
under the… under the covers, I'm constructing a resource with nothing…
with no attributes, it just has a single entity, and then merging that into the existing, like, the main resource, using the… this merge algorithm, which are… it's just…
Merging a resource with one entity, which is maybe not, like, the…
whatever. It's not super optimized, but it works just fine, and it's… it is what it is. My prototype matches a lot of this stuff. It just removes the concept of the instrumentation, scope.
Resource thing that we were doing.
**Josh Suereth** 21:39 So… I mean, I'm…
**Daniel Dyla (Dynatrace)** 21:42 I think we're good to start writing, spec.
**Josh Suereth** 21:46 Okay.
Would you want to take a crack at that?
**Daniel Dyla (Dynatrace)** 21:49 Yeah, I can go for it.
**Josh Suereth** 21:51 Okay.
That would be wonderful. I will keep working on the OTEP around this multi thing, but I want to get to the point where we have the spec written and some implementations that people can try out in different languages. So, like, my goal right now
I'm actually… there's two ways I can go about it. Writing a prototype around multi-entity stuff in Java, which I will do.
But there's just as much work taking the original prototype for just entities and resource and the merge logic, and making that something that can be released in the Java SDK.
That you can experiment with. And so, I actually, if I, if I, you know, in my head, the thing I want to focus on is the right-hand side.
Of, of getting that out.
As quickly as possible.
**Daniel Dyla (Dynatrace)** 22:39 Okay.
**Josh Suereth** 22:40 But if, if we need to do,
if we, if we want to finish the current OTEP, which I think we should.
And prototype that, and get that approved before we start merging spec work.
I'm fine with that too, it's just, I, you know, from an implementation standpoint, the one is gonna be a little hacky just to prove it works, and the other one is, like, robust and, you know, what we're gonna do for our end state.
**Daniel Dyla (Dynatrace)** 23:06 Yeah, so I guess…
in order to start working on the SDK, would you want me to make a PR on your OTEP to fill out that to-do SDK section, or would you rather I open a draft PR against the spec itself?
**Josh Suereth** 23:22 I'm fine open to draft PR against the spec itself for the OTEP, which has already been approved.
Right? So, but if… if you need things from the current OTEP, then just… you can just change.
**Daniel Dyla (Dynatrace)** 23:34 anymore.
resource stuff.
**Josh Suereth** 23:37 Yeah, if you need multiple resource stuff, then I can give you access to the current OTEB, because my… the thing is, I think we can implement this in a phased approach of get, you know, part one out, and then part two.
**Daniel Dyla (Dynatrace)** 23:49 Yeah, we could get part one, which is detectors and the, environment variable detector, and defining the entity, like, you know, startup.
**Josh Suereth** 24:05 Yep, exactly.
**Daniel Dyla (Dynatrace)** 24:06 Okay, alright, cool, yeah, I'll work on that.
**Josh Suereth** 24:08 that's what I want to get out in Phase 1, and then we can do the multi-stuff as a follow-on to that.
Like, with the…
**Daniel Dyla (Dynatrace)** 24:15 Okay.
**Josh Suereth** 24:16 Yeah. Cool.
Awesome. That was the major thing I wanted to talk about, actually.
**Daniel Dyla (Dynatrace)** 24:23 As a point of, you know, I guess putting on your PO hat, or PM, or whatever it is, if I only have time to…
prototype your OTEP, or work on the SDK spec, what should I… what would you rather I prioritize my time on?
**Josh Suereth** 24:48 Personally, I think the… spec.
But, hold on, where do I… I shouldn't be clicking on that, hold on. Come on.
**Daniel Dyla (Dynatrace)** 24:59 I hope the spec will be at least more straightforward and time-boxed and… Finished, and then… whatever.
**Josh Suereth** 25:08 That's… that's what I'm hoping as well, but when… when we think of this in terms of what we need.
this Entity Manager OTEP section, I was gonna change this to be… basically, we need to support the browser sake.
Right?
And our current thinking is that that prototype will support the browser SIG.
so, we need enough confidence that that's going to work.
But… I'm fairly confident that we can make it work the way it is,
Or, like, it'll be similar. So, then, what I'm really focused on personally, as a PM,
and my PM hat, is get this done.
get this done, get this done, get this done, right? In order. Like, let's make sure we're making progress on…
attainable chunks. And so, to me, getting resource and entity, just something that is advertised, that entity detection works with, that the resolution rules happen, that the collector can interact with it, like, I think let's just keep making progress on that.
And get that out the door, so people can interact with it, and then unblock browser as we go.
**Daniel Dyla (Dynatrace)** 26:23 Alright, sounds good.
**Josh Suereth** 26:24 That's Phase 2. Yeah. I'm willing to be overridden on that if anyone else has thoughts or concerns, because I do think we…
They're both important, but if we have to pick, it's, let's finish this as much as we can.
Alright, so, with that…
Last up, I want to do timeline.
We don't have to take the whole time, by the way. So, timeline, let's see what we have to do. We're currently listed as at risk, because I think our delivery's end of the year, and I really don't think we're gonna have a stable specification by end of the year at the speed we're going.
not to…
**Daniel Dyla (Dynatrace)** 27:11 I think we could… I think we could have a stable spec, or…
At least a spec that we are happy with submitting for the stabilization process.
**Josh Suereth** 27:21 Yeah.
**Daniel Dyla (Dynatrace)** 27:21 for… the… not multi-resource.
Version of it.
**Josh Suereth** 27:29 That's… yes, agreed. So if we limit our scope to just Phase 1, not Phase 1B,
we can do it. Let's, let's, let's focus on that, then.
Okay, in progress. We have support for new resource entity references, proto-message in the collector. How's this all going, Dimitri?
Anything you want to call out? I mean, I'm seeing more check marks every week.
**Dmitrii Anoshin** 27:53 Yeah, it's going fine. The only challenge is, approvers being… Available, so…
**Josh Suereth** 28:03 Okay.
**Dmitrii Anoshin** 28:04 Hard times getting people to look at the stuff, and, yeah, but I'm not sure what else I can do. I just pinned them.
That's way.
**Daniel Dyla (Dynatrace)** 28:13 We have a few, people working on the Collector, and I can…
Maybe try to reach through some internal channels and get that prioritized.
**Dmitrii Anoshin** 28:22 Yeah, I get, some approvals from people who are not approvers on the collector, unfortunately, so I cannot…
**Josh Suereth** 28:31 We need the actual approvers on this, yeah, and given
focus, it might be hard. Okay.
**Daniel Dyla (Dynatrace)** 28:37 At least Evan is, I know, an official approver. I don't know who…
of Dying the Trace people are official, but I can… I can breach through some internal channels to… to try to bump it up the priority list.
**Dmitrii Anoshin** 28:50 Yeah, Ellen can definitely help.
**Josh Suereth** 28:56 Alright, so the next one is around the Go SDK and prototyping the Go SDK.
I am trying to convince David Ashpole, from our company to, like, take a look at this and help me with the Go SDK. He's been a bit distracted because he actually improved performance of the Go SDK by, like, 80% or something insane recently.
For metrics. So he's trying to do all these performance optimizations. It went from where we were way slower than Prometheus to we're on average or faster, depending on your use case. So, that's fun. But he's landing that first in the Go SDK, and then we're gonna talk about whether he can help.
with this prototyping. Cool. So that's that.
And then, SDK startup specification. This is actually writing the specification for how the SDK starts up.
Which was,
Basically, how are resource detectors provided, and making sure that there's a concept of them that will provide entities instead of resources going forward.
**Daniel Dyla (Dynatrace)** 30:06 This is…
**Josh Suereth** 30:06 Absolutely.
**Daniel Dyla (Dynatrace)** 30:07 if not fully contained in what I just committed to, it's at least, like, there's tons of overlap, so I would say you should just go ahead and assign that to me, and…
**Josh Suereth** 30:16 That's what I was gonna ask, thank you.
**Daniel Dyla (Dynatrace)** 30:18 Yeah.
**Josh Suereth** 30:21 Alright
Then we have prototype and defined startup and resolution system for entity provider and entity for the OTEP. This was,
we… I think we already did these prototypes, and…
I'm gonna mark this as finished.
Or just move it to done. We had a bunch of prototypes for startup. I think we have prototypes for different ways we can do startup. We have the listener approach, if we ever want to pull that out of the bucket and look at it again, we can. But we're going with something simpler to start with, I believe, because we don't need it with the current multi-entity proposal, multi-resource proposal.
Okay.
Then, develop strategy for asynchronous resources and entities. This was, you're talking about this.
**Daniel Dyla (Dynatrace)** 31:13 It's kind of…
**Josh Suereth** 31:14 Good.
**Daniel Dyla (Dynatrace)** 31:16 this is kind of what we're doing. I mean, this is the… the,
like, the SDK startup thing, I think it has a ton of overlap with the one you just assigned me.
The way that I currently have it working is, that the values are just, either a value or a promise to a value. Everything seems to be working just fine.
the only limitation, I guess, is that you…
Have to know which keys are possible in advance.
And by in advance, I don't mean at, like, coding time, I mean synchronously.
**Josh Suereth** 31:56 Yeah. So…
**Daniel Dyla (Dynatrace)** 31:58 It doesn't seem to be a problem.
I guess we should leave this open for now until the current prototypes
are fully resolved, and the startup spec is done, but I think that overall, this is in a decent state.
**Josh Suereth** 32:16 Yeah, if you need language in the spec for this, that's the other thing to call out, but I think that I'll…
from our discussion, that sounds reasonable, and if you need an example where we have to make an HTTP call to do detection, use the GCP ones, because I know we do that.
**Daniel Dyla (Dynatrace)** 32:31 Yeah, those are the… those are the… main…
those were the main drivers of the current design in JS Resource, actually, so,
It's… yeah, I'm well aware of those.
**Josh Suereth** 32:46 Yeah. Well, when we have n variable detection, my hope is to kill all of that for just end variable detection, so you won't have all the promise crap, but until then…
**Daniel Dyla (Dynatrace)** 32:56 Okay. I was gonna say, if we were able to go to the environment variable from that, then maybe we could just remove asynchronous entities entirely, but we…
It's not worth worrying about at the moment.
**Josh Suereth** 33:11 You, I…
**Daniel Dyla (Dynatrace)** 33:12 There will always be a use case for it, I think.
**Josh Suereth** 33:14 Exactly, and I think it's the case where we have to get the end variable thing something people can depend on, then work… places that host workloads will fill out the end variable, then we can remove the asynchronous call generally for people, and it'll be more stable, but we'll always have, like, back compat support, so…
**Daniel Dyla (Dynatrace)** 33:33 Yeah. I don't think it's fine.
**Josh Suereth** 33:35 Yeah.
Okay, entities and schema files. This is, like, transformations and the transformation processor for entity. I think we're getting to a point where we can actually do that and define those.
So…
how to… we'll have to change the existing resource transformations and, like, update that spec, but this is… this is a to-do. There's a lot of… a lot of crap around, schema files to… to figure out over time in SEMConv, because we have new capabilities now.
Okay. Can collector processors differentiate remote versus local?
Dimitri, this is assigned to you, but I know that probably not a lot of progress has happened. This is still something we want to solve before we get ourselves stable, right?
**Dmitrii Anoshin** 34:27 Yeah, this is some money. I'll take it along with other stuff on the collector side.
**Josh Suereth** 34:32 This service and service instance ID is different entities. I'm gonna remove this off our board. We moved this into the service and deployment status, and, currently, just so you know, they are proposing, why? Why did we go over here?
Currently we are proposing that these will be different entities, so I'm actually gonna mark this one as done for us.
So, service, service, namespace, and
Service instance will be different entities.
It's 10XT.
Interesting.
Okay.
Anyway… Let's see… we have…
Browser, session, and entity. This is the client instrumentation SIG.
mechanics, browser-based telemetry ingestion. I think this one we can mark as done. Like, don't we…
know how we want to do this with the multi-entity thing, or do you want me to move it into 1B?
**Daniel Dyla (Dynatrace)** 35:45 I would…
take it down the road. Right now, the browser folks are prototyping what they're calling a session manager.
Which will interact with the entity and…
It's not clear how that mechanism even works at the moment, and how… they're still defining what is a session.
Like, they're too early in the process for us to declare victory on them.
**Josh Suereth** 36:11 Alright, so we have some time. Prototype exporting data shut down, particularly in the browser. This one, I'm gonna move over here to the browser SIG, because that was,
That was around, the entity manager OTEP. Oh, wait, wait, why am I over here?
That would be here.
Yeah, this.
**Daniel Dyla (Dynatrace)** 36:34 Yeah, the shutdown in the browser is always…
**Josh Suereth** 36:37 That's entity, I mean, that…
**Daniel Dyla (Dynatrace)** 36:39 You can always lose everything, unfortunately.
**Josh Suereth** 36:43 Yep.
Okay, so this is the last one to look at. Communicate the breaking change and specification around resource allowing non-mutable attributes. So, this one, this one I can take on as we start making the spec changes, but we wanted to note attributes are no longer considered immutable in the spec.
We need to update our Prometheus compatibility specification. Again, this is one reason I'm trying to get David Ashpole involved as the owner… one of the owners in the Prometheus group. Both he can help us with Go, and he can do Prometheus compatibility.
So that, that is updated. He had a proposal in one of our earlier OTEPs on that. Next, update components of OpusEmmetry that currently interact with resource and need immutable attributes. So this would be the op-amp specification. I think we can change the op-amp specification to say just use identifying attributes.
Or identity of entities, instead of, like… right now, it's kind of crazy, it's like, here's 5 to pick, and pick whichever ones also make sense.
I don't know if you remember that.
And then the routing, exporter, and the collector. We want routing key to be able to leverage, entity.
I'm not aware of anywhere else where we interact with immutable attributes.
I don't know if anyone else has other things, but these were the two we identified.
So… okay.
Anyway, I can take this, and we'll probably split out separate bugs for these.
Dimitri, is this already on your entity list, or not? The routing key?
**Dmitrii Anoshin** 38:18 No, what's that? What's the routing?
**Josh Suereth** 38:22 There's a routing exporter, it might be a connector now, but it's,
It gives you a consistent hash of the resource, so you can fire things to the specific collector if you're doing, like, tail sampling.
Yeah. Or some other kind of, like, you know, span metric calculation kind of crap.
**Dmitrii Anoshin** 38:42 That would be part of, like, support of entities for the routing connector, which is definitely not at the top of the list.
**Josh Suereth** 38:49 Yeah, it's definitely not at the top, this is near the bottom, but this is where we'd have to say, by the way, routing key on resource will be broken when descriptive attributes show up, and so we need to update it to only use the identifying ones, or we need to make a new thing that you use instead. I don't care, but we just need to do something there.
This is… this is just… we have to communicate that this is actually a breaking change.
We don't think it will be breaking in practice, we think it's only conceptually breaking.
**Dmitrii Anoshin** 39:20 But…
**Josh Suereth** 39:21 But we still have to communicate it.
**Dmitrii Anoshin** 39:23 Sounds good.
**Josh Suereth** 39:26 I should say, I don't think it's going to be breaking in practice, because I think people already put non-immutable attributes in resources.
**Daniel Dyla (Dynatrace)** 39:33 I think this was the… the biggest advantage of including the previous version that included resource on the instrumentation scope was that we had a true, immutable, non-breaking resource, and I can't think of a way to preserve that with the multi-resource version without just being…
Pedantic about, like, oh, well, it's a different resource, not a changing resource.
**Josh Suereth** 39:59 I mean, that, yeah, that's kind of what we're doing, is it's a different one.
**Daniel Dyla (Dynatrace)** 40:02 You couldn't do it before, but the other thing I will say, the multi-resource thing.
**Josh Suereth** 40:08 We actually do this today, when we do,
when we do multi-tenancy, you have to instantiate multiple SDKs.
So we actually.
**Daniel Dyla (Dynatrace)** 40:18 Yeah.
**Josh Suereth** 40:19 making a second SDK.
**Daniel Dyla (Dynatrace)** 40:20 It's theoretically possible to already do this, and, like, we know that people are certainly modifying resource…
in the collector, at least. Like, we know that that's happening. So I… I understand that…
The rule was never really followed to begin with.
But it would be… it's still unfortunate to have to, like.
Yeah, in my mind, it's still maybe considered breaking by some people, but we're gonna have to just deal with it, I think. Communicate it and call it a day.
**Josh Suereth** 40:49 I think, I think we considered breaking, and we just communicate it, right? And we communicate why we're okay with it.
**Daniel Dyla (Dynatrace)** 40:54 Yeah.
**Josh Suereth** 40:55 I don't think we ever pretend it's not breaking. We just communicate why we don't think it will break people, even if it's breaking.
Okay, so that one, that one I can take on later, but, cool.
So, are these the last 3 things we have to do before we're done? Or, should I start opening up, like, get an implementation of this language, get an implementation of this language, like, areas of the spec that have to be… I think…
The spec part that you're planning to write, Daniel, that I think is already covered here.
**Daniel Dyla (Dynatrace)** 41:28 Yeah.
**Josh Suereth** 41:28 Yeah, is there anything you can think of opening up?
**Daniel Dyla (Dynatrace)** 41:32 implementation issues is a little premature until we at least have a draft spec for them to look at. I mean…
**Josh Suereth** 41:39 Yeah.
**Daniel Dyla (Dynatrace)** 41:41 Okay.
**Josh Suereth** 41:42 We'll at least get JavaScript and Java, a good PR.
Yeah.
**Daniel Dyla (Dynatrace)** 41:49 And maybe go, if we can wrangle somebody into that.
**Josh Suereth** 41:52 That's… that's the hope. And if we can't wrangle someone,
who knows, maybe I'll write Go when I have more time off again.
**Daniel Dyla (Dynatrace)** 42:00 It's been a while.
Okay.
**Josh Suereth** 42:03 Cool.
Alright, so I think that's it. I'm gonna leave this as at risk, actually.
But I'm gonna add an update. We're gonna say at risk,
We're planning to de-scope the project.
To the original expected scope.
Just… Entity will be, be usable in resource detection.
Resource merge logic will be… Updated to use, entity.
**Daniel Dyla (Dynatrace)** 42:44 Sdks and collector…
**Josh Suereth** 42:47 will transmit… Entity Information.
Is there anything else we're gonna have in our initial scope?
Does that look good?
**Daniel Dyla (Dynatrace)** 43:19 I think so.
**Josh Suereth** 43:23 Alright, cool.
updated, good to go. I'm gonna leave it as at risk, and we can change it as we go.
Alright, that's it for this week. Thanks, everybody.
By the way, I'll probably be out next week.
But there's a chance I'll be on, it depends. So, I'll let you know, on chat.
**Daniel Dyla (Dynatrace)** 43:46 Alright.
**Josh Suereth** 43:47 Okay.
**Dmitrii Anoshin** 43:48 Thank you.
**Josh Suereth** 43:48 Alright, we'll see you.
