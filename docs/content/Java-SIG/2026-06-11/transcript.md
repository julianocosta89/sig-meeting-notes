SIG: Java SIG
Date: 2026-06-11
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 02:17 Hello!
**John Watson** 02:24 Howdy.
Hey, Jason and Jack, I ran into Java agent Jason at the dentist yesterday.
Because he only comes down to, big Pink anymore.
To go to the dentist, like me.
**Jack Berg** 02:40 Java Agent Jason? Who's Java Agent Jason?
**Jason Plumb** 02:43 Oh, Jason Keller?
**John Watson** 02:45 Yeah.
**Jack Berg** 02:45 Oh, oh and calories.
**Jason Plumb** 02:50 I was like, who's Jeff Agent Jason? Same thing. I thought that was you, Jason.
**John Watson** 02:55 Yeah, it was very weird. It was very weird we both, like, pulled into Big Think at the same time. It was odd.
**Jason Plumb** 03:00 Funny.
Yeah.
**Gregor Zeitlinger** 03:04 Otherwise, if you think about Java Agent while you're at the dentist, that's slightly disturbing.
**Jack Berg** 03:17 Josh Sarath, I've been reviewing your entities.
VR.
**John Watson** 03:23 Sounds a little personal.
Apologies.
**Josh Suereth** 03:27 It's funny.
**Jack Berg** 03:28 2,400 lines.
**Josh Suereth** 03:31 I… well, yeah, partly, I think I want to split it up, but I wanted to talk through, like, what it is, what it does, and how… anyway, I put it on the agenda, so we can talk about it whenever.
**Jason Plumb** 03:43 You've also been working on policies, right?
**Josh Suereth** 03:46 Yes.
**Jason Plumb** 03:47 Yeah.
**Josh Suereth** 03:49 Now, Jacob Arnoff did most of the really cool policy implementation, I just did a bunch of BS stuff before that.
**Jason Plumb** 04:04 And Shirazi, who's not on this call, is also doing some stuff.
**Josh Suereth** 04:10 I saw some of the stuff in the Java repo, it was pretty awesome.
**Jason Plumb** 04:13 Yeah, yeah.
**Josh Suereth** 04:14 Yeah.
**Jack Berg** 04:20 I didn't hear from Trasp today, So, he normally lets us know if he's not going to be able to attend, but we're 3 minutes over, so I'll start sharing my screen so we can get this meeting going. We got a light agenda. If you have anything else to talk about besides Chef Sareth's topic, please add it. Add yourself to the attendees list as well.
And I'll get set up to share.
Alright, Josh, you want to jump into those?
**Josh Suereth** 05:04 Yeah.
I'm happy to be back, man. I had to cancel, like, 3 meetings to be able to attend, because I'm usually triple booked now.
**Jack Berg** 05:13 Well, thank you for attending.
**Josh Suereth** 05:15 Yeah.
We're trying to get, the entity SDK kind of up and running in the spec, and so I was trying to implement this inside of the Java SDK, so what I did was I killed the previous prototype we had and re-refleshed everything out.
We had made some decisions about 2 years ago that I think we should reconfirm whether they're still the right decisions. When I was here, I don't know, I think it was, like, a year or two ago, I forget when.
But more importantly, I think there's, like, a set of things that are really hard. So the most important thing I want to talk about is the changes I made to resource.
in here.
So, under SDK, what I did was I created a, internal directory where I threw all the stuff around entities in it.
**Jack Berg** 06:06 Let's just, like… let's just open it up in code. I have it checked out right now.
**Josh Suereth** 06:10 Okay, yeah, that'd be much easier, yeah. So, if you look at resource, The big problem with resource right now is it violates how we do things now in Java to be binary compatible. Like, this is an auto value, which is an abstract class which is exposed directly as a public API, instead of as a trait.
So, if you go to add a new field to it, you break the binary compatibility rules.
Even though…
**Jack Berg** 06:44 We've dealt with this before. We have tricks around this.
**Josh Suereth** 06:47 If you have a trick around it, I want to use whatever your trick is. What I did was I added this new collection of entities to it.
That's the thing I need to add.
**Jack Berg** 06:56 Yeah, and that's what we've run into in the past, like, and it's not a breaking change to do this to an auto-value class. I can dig up the details. I think we had to do this with, like, span limits one time, which is, like, you know, exposed similarly, and it's just, like, you know, even though JAPICMP, you know, flags it, it's not a concern, practically, so…
**Josh Suereth** 07:17 Okay.
As long as that's the case and we're comfortable with that, we're good here, because I think the, the, it's, like, a theoretical thing where someone could violate this, but they'd have to also not use standard Java compilation. Like, you'd have to do bytecode writing to, like, make it be incompatible, so… Anyway…
**Jack Berg** 07:38 We do not concern ourselves with that.
**Josh Suereth** 07:41 Cool. So, the one piece of this is actually taking resource and adding, entities into it, implementing the new merge algorithm that pays attention to entities in addition to attributes.
And then updating the OTLP exporter.
to leverage entities so that OTLP has the new, fields in it for entities. So this, this adds the, get entities on resource, the merge.
function here is completely delegated to an internal helper method, because it got a little bit more complicated. So you can look at that if you want to see how that works.
which is effectively, you first merge entities, then you merge attributes, and undo any entities that are problematic based on the merged attributes. And then you figure out what the schema URL needs to be based on the entities, even though, personally, I think we should just deprecate resource schema URL Because it's not gonna be relevant in 99% of cases.
But that… anyway, so that's… that's the TLDR, what that does.
**Jack Berg** 08:49 Just backing up a step, if I can just, like, frame this for other people on the call, because I've been reading the code a little bit, and if you're not, like, in the entity SIG, I think it's kind of surprising, or maybe not entirely intuitive, how they sort of manifest in the data model. And so, like, you know, basically, we have this… we have this resource auto-value today.
And, resources comprised of attributes and a schema URL. And, what… What Entities does, both in the in-memory representation, which is, like, resource, and at the proto level.
is it extends the resource definition to have this, like, optional set of entities which are associated with it. So, resource continues to expose the information it did before, where it's just like, you know, it can be just, like, this raw bag of attributes, but those bag of attributes, you know, can optionally be informed by the entity, and, you know, if you go and look at one of these entities, it's sort of like you know, add structure to these attributes so that, like, you know, every single bag describing a different part of, you know, the telemetry producer has, you know, more structured semantics around it. So, you know, each entity has a type.
a bag of attributes which are identifying, a bag of attributes which are descriptive, and a schema URL.
And so, like, you know, I think what I was positively surprised about is, like, you know, this is just, like, extending resource with this additional, like, you know, immutable sort of data object, which adds structure to the attributes that were already there. And it's just a matter of, you know, when you're building your resource, optionally including these when you're building it up, or before you would just record attributes, and when you're encoding all this and sending it over OTLP, like, now you have a resource that has this optional, like, additional structure to it, and, you know, you need to encode that into Protobuff where appropriate. So it, Yeah, that's, I guess, like, the… like, what's happening here. So all the changes are around, like, you know, you know, being able to include this optional bit of information. So, there's, like, Resource Builder, where now there's new, Methods to add an entity.
**Josh Suereth** 11:06 I don't think they're public yet. Yeah, it's right there, add… And at all.
**Jack Berg** 11:16 Yeah. So yeah, that makes sense to me. What… so, yeah, there's a… like Josh was saying, there's a… the way that resources merged before was always sort of broken, at least with schema URL. So Entities fixes that, and there's a new, you know, merge implementation that, like, fixes that. Basically, nobody used resource schema URL, because if you tried to use it, and then you tried to merge resources, it would be borked, you know.
hopefully, and Josh, correct me if I'm wrong on this, hopefully the resource level schema URL essentially eventually gets deprecated, it's slash always set to null, and it would just be the entity-level schema URL, because entities also have, like, a schema URL, which is… You know, typically not null, in which, like, has, you know, the semantics that we should have had on day one, but that we kind of screwed up along the way.
**Josh Suereth** 12:11 Yeah, exactly right.
Yep.
And if you, if you need to see the protocol changes, they went in about a year ago, and the collector's been kind of leveraging those. But this, this, like, the most important thing we're trying to get to is where we can have a flag in Java, where we can use entities, and where the OTLP Java emits will have the entities in them, so we can start testing collector SDK capabilities, right?
So the… in the exporters, in the OTLP exporter, you can see we have, you know, all the shenanigans to wire that through, but the actual constants have been in your in your builds for some time for entities, it's just the actual implementation didn't write them out. Yeah.
And to be non-breaking, the thing that always confuses people when we first show entities is we don't want to break the ecosystem. So, the data model for resource is actually a bundle of entities and a bundle of raw attributes.
But in OTLP, the way it works is all the attributes are flattened.
And then you have these, like, references that say, hey, these attributes are part of this entity, and here's their schema URL.
**Jack Berg** 13:25 Yeah, and are those in common?
**Josh Suereth** 13:27 They are in common, yeah.
I think so. Or no, in… maybe in resource.
**Jack Berg** 13:33 No, you had it right, entity ref.
**Josh Suereth** 13:35 It was entity ref, yeah, I think I put it in common.
**Jack Berg** 13:39 So, yeah, the entity… at the proto level, the entity's IDs are just, you know, the names of the keys, the attribute keys that are identifying, and those are references back up into the resources, actual attributes key value list.
And same with descriptive attributes, it's just like a repeated list of strings.
**Josh Suereth** 14:02 Right, and then these new refs can be ignored by existing features. So, like.
Adopting entities should 100% be a non-breaking change.
You, like…
**Jack Berg** 14:14 I buy that. Like, that all checks out in my mind.
Yep. So, okay, so practically speaking, let's talk about two things. So, like, what we need to do to actually start producing resources that have this entity information with them is we need to update all of our, our resource detectors, which live over in instrumentation.
to be able to take advantage of these new APIs in Resource Builder, where you can, like, you know, you use this addEntity function within the resource to, you know, have structured information in there.
And we… so that seems straightforward enough. Like, cool, great, let's do that.
You talked about having this be, like, an opt-in flag, so let's talk about that. So…
**Josh Suereth** 15:02 Right.
**Jack Berg** 15:02 you know, assuming we update the resource detectors, and, you know, the resources now have entity information at the in-memory level, you know, that's getting passed down to the OTLP clients, and, you know, you know, I guess, where… where does this flag go? Because, you know, the way that we have flags is everything is… programmatic, and then if there's an environment variable, like, we have the auto-configuration module, which reads the environment variable, interprets it, and calls an equivalent programmatic API. So, like, you know, is this an exporter-level concern on whether it's actually taking this information and going to encode it into the proto?
like.
**Josh Suereth** 15:43 This… so, right now, this has to wire into your resource detection component, which for Java kind of only exists in auto-configure.
**Jack Berg** 15:55 Well, I said… I said we don't make that optional. Like, what's the harm in always having this information on the resource, in the in-memory…
**Josh Suereth** 16:03 Yeah, if you're willing to do that, I'm happy. It's… that's just a risk inversion thing, of, like, giving it a flag initially, so people can opt in and out. But, like, if you're comfortable without having that flag, that makes everything a hell of a lot easier for us.
**Jack Berg** 16:17 I don't think we need a flag there, because to actually access this new entity information from the resource, because these are, you know, package-private APIs, like, you're gonna have to jump through some hoops. So, by jumping through those hoops to access this package private APIs, that's your flag. You've decided that you want to do something with this to use these internal APIs.
**Josh Suereth** 16:37 If we… so then the question would be, are we going to update the actual resource detectors themselves?
to make entities, because if we do… again, so the changes… there's, like, 3 semi-related… maybe 4 semi-related changes. There's updating the core SDK data model to have entities in it. The second change is updating the OTLP exporter to export entities when they exist in the core data model, right?
**Jack Berg** 17:01 Yep.
**Josh Suereth** 17:02 Then the third change is the incubator SDK that lets you interact with everything. And the fourth change is updating detectors.
so that detectors will actually produce entities from the get-go. If we silently upgrade all the entities to have that detection, your OTLP will have the entity refs in them, which again, should be a non-breaking change.
And, like, I just put the flag in there to, like, be safe, right? Of, like, cool, let's do a release where that flag is off by default, and then if we're comfortable, we flip it on by default. It should be non-breaking, but I like to have an escape hatch in case I'm wrong. You know what I mean?
**Jack Berg** 17:44 Yeah, that's true.
**Trask Stalnaker** 17:44 Jack, your question was whether to put the flag on the auto detectors or on the exporting side.
**Jack Berg** 17:54 That's right, exactly. You could have it in two different places. Like, the auto… the detectors are… maybe they are always producing these, in which case you would want the flag on the exporter side so that you can, like, you know, have to opt-in at the exporter level. Or the opposite is, like, the exporters are always gonna encode these if they see them, and the detectors themselves are opt-in.
So it's one of those two paths, if you want an opt-in flag. But I guess, like, I want to entertain for at least a second What it's like to just not have any flags at all.
**Josh Suereth** 18:26 I mean.
**Trask Stalnaker** 18:26 The OTLP is not stable yet, so isn't that problematic for us?
**Jack Berg** 18:32 I don't think we have prior art for this type of thing here, where there's, like, a development portion of OTLP in which we're trying to make a decision on when and why we populate it.
**Trask Stalnaker** 18:45 Have you guys not…
**Josh Suereth** 18:46 interacted with other development pieces of OTLP that we added, like, when we added things to, trace contacts that were new, or when we, like, profiling?
**Jack Berg** 18:57 No, we don't do anything with profiling. Our profile exporter is still completely experimental, it's like a module. And then, like, any of the additional flags, I don't think… We definitely haven't had flags. Either, like, we don't omit anything on OTLP about them, or we didn't have any flags, and we just started emitting them.
**Trask Stalnaker** 19:18 I mean, I think we had, like, event name, you know, we added… I think we added to the proto, but with the idea that you had to have opted in using the incubator And that's where this is different, if we're going to update in place existing.
**Jack Berg** 19:37 detectors.
**Trask Stalnaker** 19:37 detectors.
that that's now gonna start flowing right away. And so, what I'm thinking from, like, you know, Java Agent, or I guess, SDK2 is you… we would start… emitting… these entity… entities over the OTLP, which are not stable.
And then, if we make any changes to that, then now we're… we're breaking a default state. Like, the… to me, it's what happens by default, is… should be stable.
**Jack Berg** 20:13 So just, like, to continue your analogy with event name, so event name you sort of opted into in two ways. You included the API incubator on your class path, and you started calling the API incubator to actually record event name.
I think the analog for that is, like, the equivalent of instrumentation calling, like, the set event name field is resource detectors calling, you know, these new internal APIs to add entity.
And so, if we wanted to, like, mirror that, then the opt-in would be at the detector level, and the OTLP exporters would always encode this information if they see it.
**Trask Stalnaker** 20:55 That makes sense to me.
**John Watson** 20:58 Jason Plum has a question.
**Jason Plumb** 21:00 I didn't want to interrupt the current train of thought, so that seems like a good time to jump in. And this might be more of a question for the entities, SIG, and not this group particularly, but, it seems to me like entities are, like.
marginally helpful on top of the existing attributes, like, especially given that all attributes can be complex now, any values, like… so, that aside.
I think one of the goals originally around entities, or at least what I was aware of in some of the intent behind the design of entities, was to allow the resource to, like.
kind of be mutable. Like, I know the implementation is still immutable, and that's the intention, but to be able to have these entities that change at runtime reflect a new version or a new instance of a resource, and then have other components be aware of those changes. Is that still being discussed, or is there work around that?
**Josh Suereth** 21:53 Yes, the… There's two pieces to resource being mutable, though, that are important. So, for entities, the thing that this would enable, when entities land, and we can depend on them.
You can ignore descriptive attributes for the purpose of identifying identity, like stream identity for metrics.
Allows you to mutate resource successfully without breaking, like, correlation.
Because we're putting a bunch of attributes inside of resource that actually mutate over the lifespan of an SDK, And we don't need to, necessarily. We could actually track them via other means. So that's one of the things entities solve.
The other aspect, though, is, like, recording… like, the resource that you want to record against, the lifespan of that thing does not match the SDK's lifespan.
That's the other use case that we're finding.
**Jason Plumb** 22:48 Yeah, yeah.
**Josh Suereth** 22:49 there's a couple ways to solve that. If you're in the client SIG, that one's even crazier because of how session works.
**Jason Plumb** 22:54 That's where my questioning is totally coming from.
**Josh Suereth** 22:58 Yeah, so one thing we deal with internally in, like, GCP is, like, we're… we'll have, like, one system that's, like, recording data for a couple different clients, and we want to, like.
say, oh, this is the resource that this client sees that we record the data against, and this is the resource that client sees that we record data against, right? As opposed to the SDK having one and only one resource.
So… are we looking at it? Yes, we have a few proposals, but we don't have something that solves all the… constraints all at once. So, we have this notion of a kind of low cardinality way of tracking data across multiple resources. For client browser SIG, as long as you don't try to implement our metrics SDK, it's actually somewhat trivial to have multiple resources be supported.
You can almost treat the resource as a contextual object, and when you start a span, you attach it to the resource at that moment.
And then let it progress, right? And then you can support multiple resources just fine.
For metrics, it's more complicated, because you actually need to allocate memory and have these, you know, like, aggregation Thunks that can, like.
data and allocate them, and so dealing with metrics is a lot more complicated. I have the worst PR I've ever created for Java.
Hidden in a branch, if you want to look at it, that implements that for metrics.
I… I never brought it to this group, because when I wrote it, I'm like, this is so awful, I would never maintain this, I'm not even gonna propose it. And that's when we, like, told the client-side SIG to go figure out another way, and maybe don't implement a metrics SDK.
**Jason Plumb** 24:44 Okay, thanks, thanks for…
**Josh Suereth** 24:45 You've entered them.
**Jason Plumb** 24:47 Yeah, I mean, it's good to, like, kind of know where things are. It doesn't help immediately, but that's really good context for me, so thank you.
**Josh Suereth** 25:01 Cool. Okay, so that answers some questions then.
In terms of… In terms of, resource detection changes, flag to opt-in for entities Belongs here. Real quick, just, In terms of splitting this up for actual contribution.
Would you be comfortable if I created the resource changes and the OTLP exporter as a PR, where we don't make any changes to resource detection whatsoever, so all OTLP will be the same, but the plumbing is in place as, like, the first PR. Does that make sense?
So, it'd be this, like, hidden internal API, you can review it, everything's well tested, but there's no way to produce entities yet.
**Jack Berg** 25:49 Well, there are, because you could manually call those APIs. But, like, yeah, yeah, like… If you're programmatically building up the SDK, then you could totally produce these resources with entities, but let's set that aside. I was initially, like, 2,400 lines is a lot, but I started digging into it, and it doesn't… it doesn't seem that bad. So, like, let me… let me just finish reviewing it, and then I'll see if I can draw a clean line. I'm not entirely sure what the point is right now of, like, you know, there's two entity interfaces, one in like, the… the common section, the common artifact, and one in the incubator. I don't understand why there's both right now, so I think I need to…
**Josh Suereth** 26:35 That was… I did not want to expose an experimental interface Publicly, that people use.
In, in, In that spot. So, like, the idea… this is my assumption from Java. I wanted the entire entity API to be in, Incubator.
And so that's the one that users engage with. The one that's hidden and internal, that's, like, publicly exposed, is just so that I can have an API that I call into against resource that isn't, like, user… User-facing, public must be supported, can't break, that sort of thing.
That's the only reason that there's that disjoint.
**Jack Berg** 27:14 Okay, in the past, when we've had these sort of internal, or, like, experimental APIs that, you know, still need to be part of the core, because if they're not there, they don't function. Like, like, an example was when we extended span processor with this, like, unending new, like, capability, where you could… it was before it ended, but in… well, it was still mutable, and you could still change fields.
The way that we've solved that is we put the stuff in You know, make it package private, put it in internal packages or whatever, and we provide these, like, public utility methods That allow you to still call into it, but, like, you're sort of accepting that this is… you're exposing yourself to breaking changes, because you're… you're calling this public utility method that's in an internal package.
And so, like, I'll… I'll sketch out what that looks like for you in the context of this. I don't know exactly yet, because I need to dig into your code, but I think, like, I don't think we need two copies of this API, one in, like, common and one in the incubator. I think we can get away with just the one in common.
**Josh Suereth** 28:23 If we can get rid of… get away with the one in common, that'd be awesome. What I did is my attempt to do that pattern that you just mentioned.
**Jack Berg** 28:31 Okay.
**Josh Suereth** 28:33 So.
**Jack Berg** 28:33 I'll take that.
**Josh Suereth** 28:34 If there's a better way to do it, like, let me know, yeah, because that was my intention, yeah.
**Jack Berg** 28:37 Okay.
**Josh Suereth** 28:42 Cool, that's all I needed, thanks.
**Jack Berg** 28:47 Sweet, Yeah. So, Josh, actually, I was just going back, because you had this earlier iteration of, like, your entity's PR back from, like, last summer, and I was like.
I remember spending time on this. How did we, like, lose track on this? And, like, so I reviewed your PR, and then you, like, got back to me, and then I went on parental leave, and I was just… that's what happened. That was the order of events on why, like, that got blackholed.
**Josh Suereth** 29:14 That's fine. Actually, the reason it got black holed was because we were working with a client SIG to figure out the mutatable resource. That's when I started working on the second prototype, where you… again, hopefully you never had to look at that code, and I don't want anyone to have to look at it, but it was bad.
But I got it working, it's just, like, what you had to do to the metrics API was very disgusting.
To, to be able to mutate.
**Jack Berg** 29:39 Well, I appreciate you withholding that.
Alright, well, this time, we're gonna, we're gonna make it happen. We're gonna, we're gonna get this landed.
entities in Java.
Okay, next topic, Jason.
You're muted.
Muted.
And I guess I'll share my script.
Just cause I started the meeting.
Nice.
**Trask Stalnaker** 30:13 Sorry I was late.
**Jack Berg** 30:14 Yeah, no worries. Jason, you're still muted, by the way. I don't know if you were talking, but we cannot hear you.
**Trask Stalnaker** 30:20 There we go.
**Jason Plumb** 30:22 Yeah, I just really prefer not to be on mute, but I'm worried that, like, background sounds sometimes sneak in, and whatever. I'm really bad about remembering the mute. I only put this on here because I wanted to make sure that we're on track for releasing this week, just because I have other people asking me about it.
**Trask Stalnaker** 30:40 Instrumentation repo.
**Jason Plumb** 30:42 Yes.
**Trask Stalnaker** 30:44 What do you… what… I'm just curious. It's always interesting to know what people are waiting on.
**Jason Plumb** 30:49 I mean, literally, literally just the release, it's not feature… it's not feature-based, it's not rational.
**Trask Stalnaker** 30:56 Okay, only be… the only reason it, well, in addition to the fact that we slip a lot, the… this time, this is hopefully the last release before 3-0.
**Jason Plumb** 31:09 Got it.
**Trask Stalnaker** 31:10 So we're trying to squeeze… Potentially, we may try to squeeze a few more things in in the next couple of days, so…
**Jason Plumb** 31:18 Okay.
**Trask Stalnaker** 31:19 Set the expectation that, it will probably be Early next week.
**Jason Plumb** 31:26 Okay, that seems reasonable.
Yeah, just thanks for that. There's just a cascade of releases that happen after that over here, so… Okay, that's fine. Thank you.
**Jack Berg** 31:41 Alright, countdown to 3.0.
Picking up our recurring topic.
**Gregor Zeitlinger** 31:50 Yep, I just added it because Trust didn't do it before.
**Jack Berg** 31:56 Maybe I should hand over the driving, to Trask, or Gregor, and the people that are more closely connected to this, if there's specific topics we want to go into, or issues.
**Trask Stalnaker** 32:08 I can drive, yeah.
**Jack Berg** 32:10 Alright.
**Trask Stalnaker** 32:12 And we mostly… Oh, go ahead.
**Gregor Zeitlinger** 32:17 Just wanted to say, the reason I added that link is because my idea was that we have an assignee for all of the topics, so that it's easier to make sure that everything gets done.
**Trask Stalnaker** 32:31 Don't we have a signee here on the issue?
**Gregor Zeitlinger** 32:35 Yeah, yeah, that would be the same, yeah, right.
**Trask Stalnaker** 32:37 Okay.
I don't know why I… I've just never fully adapted to GitHub projects, so if there's an alternative, like the issue milestone list is kind of where I gravitate to.
So, I think… let's see, I've got a couple of… I think this is going well. There's… a couple of… oh, I guess, yeah, let's put assignees on these things.
This one is me.
Let's skip over the invoke dynamics stuff, because there's a bunch of those, and we'll come back at the end.
Stable, Attributes… Agenda.
This is done, why… Okay, I think… I think that's done, but I will confirm.
This one… We decided that this can't be done until just before The release? That's right.
Yep, that's right. Did you… okay.
Okay, and we've got you assigned, perfect.
This is another one that has to be right before… It's a e… I mean, it's… it's easy. I'm not too… I'm not worried about… But… This is an interesting one.
**Gregor Zeitlinger** 34:55 Yeah, I've, I've done some work to categorize them and also take into account, what, Laurie has flagged, which is that we should not force people into declarative configuration, in 3.0 yet, given that it's not as mature as we had, hoped it is, and that is taken into account here.
**Trask Stalnaker** 35:27 Okay.
Cool. I have not looked over, so…
**Gregor Zeitlinger** 35:33 Yeah, I can watch… through it, or you can take a look later. I think, in… If you agree, then I have everything done already.
**Trask Stalnaker** 35:48 Yeah, I agree this for… oh, let's see, you have…
**Gregor Zeitlinger** 35:53 Yeah, one is more intricate, so I created a separate issue, because it would just make this other one too complicated.
**Trask Stalnaker** 36:14 Oh, okay, so just removing the legacy declarative… Config, but not the… yeah, yep.
**Gregor Zeitlinger** 36:25 That's what I figured would be, the right call.
**Trask Stalnaker** 36:31 Makes sense.
**Gregor Zeitlinger** 36:32 And there's yet another split-off, which is the question about, service peer.
Which I also created a separate issue for, because it's… Related to, declarative configuration schema.
And if we decide that, It needs another, Version of declarative configuration, then we also have to do that first.
**Trask Stalnaker** 37:03 Is that one, here, okay.
Yes.
So I should tag this one 3-0.
**Gregor Zeitlinger** 37:14 Yeah, right, I forgot about that, yeah.
**Trask Stalnaker** 37:28 Okay, if you, I think I put in a PR, if you'll notice now, So the semantic convention… Awesome, stability.
**Gregor Zeitlinger** 37:43 Yeah, I saw that you're headed PR.
**Trask Stalnaker** 37:46 Yeah, what I've been doing is, so I don't want… to use the OTEL… the SEMCOM stability opt-in flag.
Going forward, unless… like, this flag should be a stable flag. So, like, we've been kind of abusing it in the past to be, like, the database Stability work is in progress, but not complete.
**Gregor Zeitlinger** 38:18 And so…
**Trask Stalnaker** 38:18 if somebody would use this and opt-in to the DB stable SEMCOM, it's not really stable, it's in progress.
So, what I want to do going forward is have, semconstability Preview instead of opt-in.
And the preview are things that are in progress, and then once they're fully implemented, we can bump that over to The regular opt-in flag.
Got it. So, I think I had flipped… The pier… to use the non-stable, because, it's not going to be stable for 3.0. Code will be stable for 3.0, database will be stable for 3.0.
Rpc won't, messaging won't.
This was ours.
**Gregor Zeitlinger** 39:17 This is different than the question of declarative config schema.
**Trask Stalnaker** 39:24 Yeah, so maybe have a, could you create an issue that just document… we should just remove… All of the… and we could probably do that at any point, removing any old declarative configuration support.
If we have…
**Gregor Zeitlinger** 39:42 It's already part of the PR that I created.
**Trask Stalnaker** 39:46 Okay.
**Gregor Zeitlinger** 39:53 But, what is different about, service peer is that this does not have, that this is not enumerated, in the, configuration repository, like DB is.
And I wasn't sure if that was the right call, since it somehow looks different.
**Jack Berg** 40:15 Didn't we determine that there's a special casing for this? That, like, it's treated as a, as a Java-specific instrumentation library? So it's, like, instrumentationDevelopment.java.something. I thought… I thought J was… investigated that, and found that's how we're handling this today. Because, as you, as you know…
**Jay DeLuca** 40:38 Yeah, it's under Instrumentation, and then Java Common.
service peer mapping.
**Gregor Zeitlinger** 40:46 I mean, this is how it's implemented, but from the Semconf point of view, is that, really Java-specific?
**Jack Berg** 40:53 Oh, oh, is it Java-specific? .
**Trask Stalnaker** 40:57 I think we're the only people who've implemented it.
**Jack Berg** 41:00 Exactly. Like, that, that's…
**Gregor Zeitlinger** 41:02 Hmm, okay.
**Jack Berg** 41:03 We ripped it out of the declarative config schema, and if we… we went back and looked at that, Gregor, that PR, where we ripped it out, and Trask has this comment in there, which is like… like, you know, removing this for the time being, because Java is the only language that has done anything with it.
**Gregor Zeitlinger** 41:20 Okay, now I understand.
**Trask Stalnaker** 41:23 Yeah, I think, most… mostly this service peer mapping stuff is gonna be pipeline stuff. It's kind of, Yeah, I don't… from the discussions we had, I'm not expecting other languages to implement it.
**Jack Berg** 41:46 Should we rip it out?
**Trask Stalnaker** 41:49 We have users using it.
**Jack Berg** 41:52 Okay, okay. As long as you know of a user that's using it.
**Trask Stalnaker** 41:55 Well, all of… so all the light step, all the former light step.
people, I know they were using that heavily, and Michele, has mentioned that the Dash Zero folks who have… they have people coming over from LightStep who are… using that.
**Jack Berg** 42:18 Okay.
**Gregor Zeitlinger** 42:27 So now, back to what you suggested, Jack. A Java-specific lag, or what… what was the idea?
**Jack Berg** 42:35 that it's already a Java-specific, There's already Java-specific support in declarative configuration. Jay found where this code is. It's treated as… there's, like… what's the name of the instrumentation library, Jay, that it's nested under?
**Jay DeLuca** 42:55 The… what do you mean? There's no… are you just looking for an example library?
I'm looking for this…
**Jack Berg** 43:06 I'm looking for the source code that, like, you know, reads the…
**Jay DeLuca** 43:11 Oh, yeah.
**Jack Berg** 43:11 Declarative config schema, and, you know, applies this peer service mapping.
**Jay DeLuca** 43:17 Is it what I just put in the chat?
**Jack Berg** 43:23 Silly.
That looks like it's the one.
Yeah, so it's put under common, instrumentation common.
so I guess it's not… it's not put under a Java-specific place, but It… it's not part of the schema.
**Trask Stalnaker** 43:44 Whoa, whoa, it's not… it's… Are we sure?
It's under the instrumentation config, which is…
**Jack Berg** 43:57 Oh, that's Java-specific, okay.
Then, yeah, we're good.
**Gregor Zeitlinger** 44:04 So, that means the, opt-in flag should also be under this prefix?
**Trask Stalnaker** 44:13 There… oh, I see, for the service peer… I don't… I think it has to be. I think we can abuse that, like, it's a semantic…
**Gregor Zeitlinger** 44:33 Technically, we can, yeah, it's a list of strings.
**Trask Stalnaker** 44:39 Yeah, because I think we're also doing that for code attributes also. Like, I don't think anybody else is… I don't think we've documented the opt-in thing for code.
attribute migration.
I think we are a little bit more aggressive on… providing backwards compatibility for the Java agent users, because we have so many, and… The… we were using code heavily, other languages weren't using code heavily either.
So yeah, I think that's fine. Let's continue abusing that list.
**Gregor Zeitlinger** 45:21 Okay, cool.
**Trask Stalnaker** 45:29 Stable… the JMX target system… So, I think… Jason… Oh, Sylvain provided a list here, potentially.
We have… I guess the question is, Otherwise, we will… Try to recruit somebody else.
**Jason Plumb** 46:20 Is it primarily renaming?
**Trask Stalnaker** 46:25 So, I think that… The proposal was for a bunch of these to just be standard.
**Jason Plumb** 46:36 Yep.
**Trask Stalnaker** 46:37 And then the other ones would, yeah, add the underscore experimental.
**Jason Plumb** 46:42 Okay.
**Trask Stalnaker** 46:43 And, you know, just do a… I would… We need to do a sweep of the other things just to make sure that everything that is doesn't… say experimental is stable in the JMX config.
**Jason Plumb** 47:04 I wish I had time to help with it.
**Trask Stalnaker** 47:11 Rename, okay, this… 1… There's a PR in already… I think Lori and I are just working through the last parts of that, and… Remove deprecated code.
I like removing deprecated code, so I'm going to assign myself.
Alright.
And then all the invoke dynamic stuff, and, like, that… Hmm.
If it slips… you know, it slips. I think that's up to… Sylvain, if that's going to… Happened for 3-0.
Alright, any other questions about, Trio?
**Gregor Zeitlinger** 48:26 Yeah, we have a really old PR about, thread detail configuration that's, like, open for half a year.
Do we want to have that in, or, we want to punt that?
**Trask Stalnaker** 48:43 That's a good… so is that… am I missing that because I'm not looking at…
**Gregor Zeitlinger** 48:50 No, no, you're not missing it. I did not tag it, but I added it to the meeting notes now.
**Trask Stalnaker** 48:57 Okay.
Yes, that one did get lost at the bottom of the PR list, sorry about that.
Do we have… Oh, we have an issue.
Okay, perfect. I'm gonna tag it, for 3O, and I will, I will… check that out. I will revisit that, because I didn't… it's gonna take me several minutes to page that back from Wherever it is in my… Yep.
**Gregor Zeitlinger** 49:41 No worries.
**Trask Stalnaker** 49:41 of my brain.
Yeah, so for 3-0, We're targeting next month for 3-0, still?
We'll see how it goes.
seems… I feel like, at most, we might decide just conservatively to slip a month.
But, depending on how much stuff goes in.
So I think we'll wait, probably should wait and not… Immediately.
Do the breaking things after this release.
Until we kinda… Make sure things are settled.
Jason…
**Jason Plumb** 50:45 Yeah, this one just… no one's looking at this repo, usually, so I just wanted to call it out.
We don't have any of these constants for any of the event names.
So, anybody that's using semantic convention events right now in Java, or… Kotlin.
Has to just hardcode them, or whatever.
**Jack Berg** 51:08 I'm cool, I'm gonna review this. There's another PR out that does the same things for the metric metadata, metric description, metric unit, metric name, and it also hasn't gotten the attention it needs, but I think I'm just inclined to merge that right now, because it does a slightly different strategy than you. It just, for now, it punts on trying to publish stable versions of these. So, you know, if you do that, like, if you basically scope it down to just, like, publishing to the incubating artifact, then, like, I think we can fast track this, and we just… we don't have to… be as conservative. But… yeah.
**Jason Plumb** 51:53 Yeah, so exceptions being the one that is stable, that's the only one that's stable.
**Jack Berg** 51:58 That's right.
**Jason Plumb** 52:00 So you think I should remove them?
**Jack Berg** 52:01 need to… Should I remove that?
**Jason Plumb** 52:04 I don't care about it, but should I remove it?
**Jack Berg** 52:06 It would just be, like, commenting out the section of the code that even, like, generates to the stable semconv artifact altogether. So just be, like, you know, punt on… That is a… is a category.
**Jason Plumb** 52:20 Okay. Until we feel…
**Trask Stalnaker** 52:22 Right, because it's… it already exists over here.
**Jack Berg** 52:25 Right, it already exists over there.
We double produced.
**Jason Plumb** 52:29 Oh, so it's, it's doing both.
**Jack Berg** 52:33 Yeah, the way we have these set up is, like, we don't want to, like, break the incubating or stop including stuff in incubating, just because it got promoted to stable, and so, like… We don't?
We just did. This is something we decided a long time ago. The CodeGen, it will… it'll continue producing to the incubating, and, you know, market is deprecated and linked to the stable equivalent.
**Jason Plumb** 52:56 Yes, okay. And then do we… and then after a cycle of deprecation, then we'd get rid of them, or no?
**Jack Berg** 53:02 No, no, we just keep on.
**Jason Plumb** 53:03 Leave them down.
**Trask Stalnaker** 53:03 Currently.
**Jason Plumb** 53:04 Okay, okay.
**Jack Berg** 53:04 Yeah. Yeah, so the only thing that would actually break you in… And incubating, like, like, let's say you were depending on, like, an incubating attribute or an incubating event name, would be if, like, the type of the attribute changed, maybe from, like, a long to a string.
Or if Semcomp did something strange and, like, deleted the attribute key or the event name, which I don't think they do. I think they keep these around in their data model indefinitely, even… and just mark them as deprecated.
**Jason Plumb** 53:33 Okay.
And so, just to be clear, for this PR, it would be better not to have exception incubating. It's okay to have the stable version, we just don't want the incubating equivalent.
**Jack Berg** 53:46 Other way around.
**Jason Plumb** 53:47 backwards, okay?
**Jack Berg** 53:48 Am I wrong.
**Jason Plumb** 53:48 Okay, that's why I'm asking, because it's confusing. So we want to not just have the stable one at all, even though it's stable.
Correct. Because there's a risk. There's a risk of it.
**Jack Berg** 53:59 we're committed to the generation process, and, like, we're locked into that. And frankly, I'm, like, okay with that, because I think we sort of hashed out all the details that matter for attributes. But, you know, I don't know, just, if you wanted this to be expedient, then, you know, I'll… then just publish to incubating, I'll review and approve it, and I'll merge it.
**Jason Plumb** 54:21 Well, it's too late to be expedient, come on, no, I'm just kidding.
**Jack Berg** 54:24 Yeah, 3 weeks later, yeah.
I know.
**Jason Plumb** 54:26 No, it's fine, okay, I think I have my head around this now, thank you for talking that through.
**Jack Berg** 54:31 Yeah.
**Jason Plumb** 54:32 Bugging on it.
Maybe.
**Jack Berg** 54:34 And I'm gonna merge the metrics one, because… It only publishes to incubating, so…
**Trask Stalnaker** 54:43 Sounds good.
**Jason Plumb** 54:45 Yeah, in full disclosure, I'm probably gonna do something similar for Kotlin, because Kotlin's currently publishing its own semantic conventions within its own repo, and we're now consuming them in Android, so I, you know, I'll probably do the same thing for events, but I might make them fancier, I'm not sure yet.
**Jack Berg** 55:01 You, Kotlin folks, love your sugar.
**Trask Stalnaker** 55:05 In the… in this… in this repo, or you're gonna generate them into your… Yeah.
**Jason Plumb** 55:12 They're already being generated in the Kotlin repo.
**Trask Stalnaker** 55:15 Nice.
What are, what's your semantic conventions?
**Jason Plumb** 55:24 It's all of the existing ones from the main SEMCOM repo. Like, we don't have.
**Trask Stalnaker** 55:29 Oh, okay, the normal. Okay, you're not defining your own…
**Jason Plumb** 55:33 But I'm about to do that for Android, I'm about to do a little Federation action, I think, when I can find time.
**Trask Stalnaker** 55:40 Nice.
**Jason Plumb** 55:41 Yeah.
**Trask Stalnaker** 55:42 It's all their rage these days.
**Jason Plumb** 55:43 I hear that.
**Trask Stalnaker** 55:48 Alright, folks, we are exactly on time.
Any last words?
**Jason Plumb** 55:58 Stay cool this weekend, Portlanders, yeah.
**Jack Berg** 56:01 Yeah.
**Jason Plumb** 56:02 Bye.
**Gregor Zeitlinger** 56:03 Bye.
**Trask Stalnaker** 56:04 Bye.
**Pranav Sharma** 56:04 Thanks, bye-bye.
