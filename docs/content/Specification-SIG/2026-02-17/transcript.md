SIG: Specification SIG
Date: 2026-02-17
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:31 Hello, hi everyone.
Israel Blancas 00:01:36 Right?
Josh Suereth 00:02:41 Hey folks, give me a second, I'm getting started up.
Can you see me and hear me?
Carlos Alberto Cortez 00:03:27 Yes, we can.
Josh Suereth 00:03:29 By me, I guess I mean the document.
Carlos Alberto Cortez 00:03:32 Yes.
Josh Suereth 00:03:36 Alright.
Looks like we have a bit light on the agenda today. Apologies I didn't have time to…
get in early and pre-seed things, but we'll give it a little bit for everyone to write their names. Please add your agenda items. We'll get started in about 30 seconds to a minute or so here. Sound good?
Liudmila Molkova 00:03:58 Very precise.
Josh Suereth 00:04:02 Do you want me to be less precise?
Ted Young 00:04:08 Gosh.
How would you feel if we are light on the agenda, going over the state of entities?
Yeah. Because that's something that I think we need more community eyes on, because we want to get at least some of that over the finish line so that mobile and
Client stuff can get unblocked, so it'd be great to know what…
What we could be putting eyes on to help.
Push that forward.
Josh Suereth 00:04:35 Yeah, I'll start getting some links together, too, here.
Carlos Alberto Cortez 00:04:38 Actually, there's a PR that you have, Josh, on multiple resources,
which is, in my opinion, it's great. I reviewed that, your prototype, and there's a JavaScript prototype. There's one even in Go by Debbie Dashboard. It could be great to have more eyes on that one.
Josh Suereth 00:04:56 Yes. Yeah. Wait, do you think it needs more eyes, or does it have enough approvers now? That's the question. I feel like it had a bunch of eyes, but no one approved it.
After they agreed with it.
Carlos Alberto Cortez 00:05:08 Yeah, I think that the problem is that probably people reviewed that a few weeks ago, and then they forgot.
So reminding them would be great, you know?
Josh Suereth 00:05:18 Yeah, it was right before the holidays, and then it's been a crazy January.
Okay.
I will… let me… I'm gonna put some links to those, so folks can see the current…
State of Proposals.
Okay.
This one here.
Okay.
It's been more than 30 seconds, so let's get started. Trask, do you want to walk us through this one?
Trask Stalnaker 00:05:57 Yeah, if you open it, it's a pretty simple one. it was added…
Fairly recently, though, which is the only concern about, I think about marking it stable, but we do have,
Good number of prototypes already.
And so, just looking for… Approvals, feedback, merging.
the basics.
Josh Suereth 00:06:31 Cool.
Is there anything you want to call out? Was there anything of contention?
Trask Stalnaker 00:06:39 No, I don't think so.
Josh Suereth 00:06:43 It's…
Trask Stalnaker 00:06:43 For a bigger picture,
the reason why I'm interested right now is in the, working on the push…
From… to deprecate span events, or to move,
Exceptions over to logs from spans.
And so we have a…
environment variable now in SEMCOM that you can use to opt-in to recording exceptions on logs instead of spans, and I have a prototype in the Java instrumentation, that's probably going to merge, in a bit for that.
Josh Suereth 00:07:29 Gotcha.
Liudmila Molkova 00:07:33 Given it's a direct replacement of record exception and spends, Is there…
Any reason not to… not to merge it? Is there… would anybody, at least on this call, be interested in reviewing, or should we just merge it?
Carlos Alberto Cortez 00:07:58 So, I would suggest just asking more maintainers to at least take a look.
The ones that don't have a prototype.
Just to get an initial feeling, even if they don't have time for a prototype, it would be great for they to come, double-check that this sounds sane to them for their actual implementation.
I could say that would be my only suggestion, you know?
Trask Stalnaker 00:08:22 Cool, I'll post in the maintainer channel.
It's a good idea
And Ludmila, maybe we can merge end of the week, if there's no… Objections.
Liudmila Molkova 00:08:38 Yeah.
Jack Berg 00:08:40 That's a…
Carlos Alberto Cortez 00:08:40 Good?
Jack Berg 00:08:41 That's a good schedule, too, because this has only been open for 6 days, and so I think we, just as a practice, should keep stability PRs open for a little bit longer, just to give people the opportunity to object.
Carlos Alberto Cortez 00:08:56 Yeah, actually, we would be releasing this in the… in the March release, so see, we have some months, so after release… after merging this, by the end of the week, we should, remind in the next call to maintainers that this was merged, you know?
As part of that, yep.
Josh Suereth 00:09:11 Yeah.
Trask Stalnaker 00:09:15 Cool, thank you.
Josh Suereth 00:09:17 Yeah, you should let them know in chat the timeline, too, for merging.
Trask Stalnaker 00:09:21 Will do.
Josh Suereth 00:09:22 review by now, or forever hold you, yeah. Alright, Jack, do you want to talk about declaring
Sorry. Stabilize… declaring stability for declarative configuration. There we go, that's what I was trying to say.
Jack Berg 00:09:35 Sure. I only intend this to be a quick inform, and the reason I'm calling this out in the meeting notes is that this PR is on the second page of PRs in the spec repo, so it might get lost that I reopened this as ready for review. You know, I originally opened this PR back in June of 2025, and then I went out on parental leave, and kind of had to
let it… let it go dormant for a bit, and we reworked a lot of things in declarative Config. Well, we didn't rework, we just… we just improved. We applied additional scrutiny, to the data model schema, and added a bunch more tooling that, allow us to ensure we have a higher quality product. And, yeah, it's… it's time to stabilize it. We've got four languages that are completely up-to-date with the
the latest…
release candidate of this schema, and we've got a fifth language that is, you know, just one version behind, but, you know, they might even be up to date by now. I'm not sure. I'd have to go track that down. So, I think it's in a good spot. If anybody has any specific questions, I can answer those, but otherwise, just take a look.
Josh Suereth 00:10:44 Cool.
It…
Question on this, because this might have already happened. We had talked at one point, I know Tigrin was pushing for this, having, like, the compliance matrix and then, adding issues onto every…
SDK of, like, hey, you know, declarative config compliance tracking issue, and… and, like, the things that they need to do to be compliant with the spec. Is that something that we want to do here, or plan to do with… after this is merged?
Jack Berg 00:11:16 so, maybe you could clarify. I think there's been multiple conversations that have happened. One conversation is,
Should we have general tooling in the specification for when the specification has changes that impact language implementations to go, open issues in those respective repositories and have, like, centralized tracking for them?
And so…
from… for that conversation, you know, declarative config is just one example of the type of spec change that would, you know, impact the language implementations broadly. So, I think those are tangential. I definitely think that that type of automation is important and useful. I haven't been working on it actively myself.
There's another slightly related thing that maybe you could be referring to, which is like, hey, declarative config has this schema with lots of types and properties of its own, and you know, different languages may… their implementations may support
different types and properties at different times. So we sort of need a separate tracking mechanism, so a user writing a YAML config file can understand
which of those types and properties that they leverage are supported by the languages that they're going to leverage it in. And so we have tooling for that already. Basically, like, you know, there's… it's linked to somewhere in here. I can find it if folks are interested, but, you know, we have a…
language support status tracking mechanism specifically for declarative config that is high granularity. It's not in the spec repo, it's over in the declarative configuration repository, or the OpenTelemetry configuration repository.
Num.
Josh Suereth 00:12:59 OpenTelemetry, configuration, got it.
Just… just so folks know, yeah.
There's a tracking thing for the schema here, you mean?
Jack Berg 00:13:10 If you scroll down, so, there's this, no, scroll up to the actual file list. So there's a language support status markdown file.
Yeah, this is… this is generated from these YAML files. Each language implementation has a YAML file that, you know, has build tooling that ensures, you know, common structure and things like that and sanity, and you can kind of go for each lang… this is the markdown representation of it, and it shows
Right? Each language, every type, and every property, what the support status is of those. And so, like, you know, if you're interested in seeing if C++ supports this type and this property, you can go here and see it.
Oh, that's cool.
And there's, like, another view of this as well, so, like, this is sort of like a language-oriented view, so you start with, like, a language, and you say, like, hey, is this property supported? But if you go to schemaDocs.md.
This is sort of a type-oriented view of it, so it lists all of the different types that appear in the schema, and if you scroll down, for each type, there's a table, there's a… scroll up a little bit, language support status.
there's, yeah, this… there's a table here that says the status of each property for that type across each language. So, yeah, you can kind of access this information from a variety of points of view.
Josh Suereth 00:14:33 Yeah, this is cool. Nice.
Jack Berg 00:14:39 And it could be cleaned up and made more user-friendly, but…
Josh Suereth 00:14:43 I think step one is getting the data, and having it be up-to-date, and all that. Anyway, we have hands. Who was first, Robert or Trask?
Jack Berg 00:14:52 Like, rubber.
Trask Stalnaker 00:14:52 Robert?
Pellared 00:14:55 I have a question regarding these metrics, because as far as… as I understand, it's oriented towards the data model, right? So it's basically checking if a language is supporting the stuff in the data model, right? Or am I wrong?
Jack Berg 00:15:11 If a language supports the data model.
Pellared 00:15:14 Yep.
Jack Berg 00:15:16 Yeah, so…
Pellared 00:15:16 It's…
Because the thing which is missing, I'm not sure if it should be separated or not, maybe I'm missing something.
is the features of the SDK. Like, I'm pretty sure that, for instance, some stuff like plugins are not supported in Go, etc, but I think from the user perspective, probably the most important thing is stabilizing the data model and the Amphi first.
Jack Berg 00:15:42 Yeah.
Pellared 00:15:43 feedback, I do not have any, you know, it's not just a blocking comment or anything like that, just…
Jack Berg 00:15:49 Yeah, so that's a good comment. Robert, we've accounted for that in our status tracking mechanism. I'm gonna steal this chair, if you don't mind, for a second, Josh.
Josh Suereth 00:15:59 Yeah, go for it.
Jack Berg 00:16:00 And so, if you, you know.
it's interesting to know if a type in a property is supported, or if it's not supported, like, why it's not supported. Is it not supported just because the language hasn't gotten around to implementing that support yet, or is it not supported because, like, the language doesn't even have programmatic support for that yet? Like, the mechanism just doesn't exist. So, if you go and you actually look at the schema of these tracking documents.
for every type, you record, like, the status, and the status is, like, an enum of different options, and there's options to say, like, hey, like, for what reason is it not supported? There's, like, not implemented, which means that, like, this concept doesn't exist in the SDK.
So, like, you know, we can't support that because we don't… the SDK doesn't even support this thing, so it doesn't even matter that there's a property to specify, there's nothing that we could interpret it. And then there's another status that says, like, I'm not sure if this specific document uses it or not, but
there's another status that says, like, hey, you know, this is supported by the underlying SDK, but the declarative config implementation just doesn't, like, interpret that property yet. Like, we… so, we differentiate between the two. And there's a… there's a fourth status, which is, like, not applicable. Like, it's not applicable to have, like, a Go-specific property.
implemented by Java.
And, you know, an example of that would be the language instrument… or the instrumentation piece of the schema. And so, you know, within the instrumentation block, you can target specific instrumentation libraries by language. And so, like, for example, it doesn't make sense for the Java implementation to have any support for, you know, those Go instrumentation libraries, or vice versa.
Hopefully that makes sense. I'm trying to be… Brief.
Trask?
Trask Stalnaker 00:18:07 Yeah, that actually ties into my, I wanted to make a plug for if whoever's sharing can go to the link I put in chat. The one piece that's not part of this config stabilization is the instrumentation node.
And, we are using that heavily in Java, and would love to see that stabilized.
I did a quick…
search, and… yes, thank you, thank you, Bob. PHP, has implemented it also.
I'm looking for more people to implement this so that I can try to, get it stabilized.
Jack Berg 00:18:57 Yeah, this is a great feature, in my opinion. You know, semantic conventions is relying on configuration options more and more. You know.
you know, the default for the semantic conventions say, collect the data this way, but there's, like, config options to say, like, hey, do you want to collect the database summary, or do you want to collect these HTTP request headers, or these response headers? And so, like, those are really important… being able to configure those things are an increasingly important part of the, the instrumentation user experience, and this… this API that Trask has highlighted here
is what allows that to be standardized across the ecosystem. So, yeah, I second Trask's pitch to support this in other languages.
Josh Suereth 00:19:47 Cool.
Do we have any maintainers who want to sign up right now? No, we'll just… we'll leave that as an open call.
Awesome.
I'm gonna… I'm gonna go back to the agenda. I think that was a really good overview of Convig. Thanks, Jack, and thanks for raising the question. Trask, was that your hand then, too?
Yeah. Yep. Got it.
Okay.
Alright.
If nobody else has any other topics, we'll talk about the state of entities. This might take a little while, and I can exhaust all available time by talking, so I'll try to be… efficient.
We'll start… I'm gonna start by talking about just generally where we are, with entities.
So, if you want to take a first look, for context, we are making a change to resource in OpenTelemetry. This is currently in the specification, and this is the thing we're trying to roll out now. So there is, inside of the resource spec.
Did I link to the wrong thing? There is a new data model, which we never had before, which is still considered development.
And we're actually changing the data model to say that a resource is comprised of a set of entities, and optionally, a set of additional attributes, and we're trying to move more things from here into here.
And so the idea between… the difference between a resource and an entity is an entity has kind of a understood name and meaning.
Where an entity could be, like, a Kate's…
the container, and it could be at Kate's…
deployment. An entity could be a Java process. An entity could be a service instance.
Right? And there's some kind of relationship between these entities that we can talk and discuss and negotiate. But if you haven't seen the specification changes here, we talk about entity, we talk about resource, and we have modified, the README in resource to describe how resource tends to get used in OpenTelemetry and, you know, things about it.
In addition, we're fleshing out the entity section to describe, then, what entities are, their models, and their relationships. This is all in the spec.
So… Next step is now that we have a data model.
There's a few things we need to sort out in the data model.
And there's a few things we need to do to get this into the SDK. So…
I have these in order of probably priority in the ecosystem, as opposed to priority in the entity sake. But first is this notion of multi-resource support.
This is to help with browsers, this is the issue where we want to report against a resource. We want to report telemetry data. And the problem is that, right now, we assume that the SDK has an identity.
And that the thing we're reporting data against is the same identity as the SDK's identity.
That is not necessarily true if the lifetimes don't line up. So, for example, for browsers, I want to report stuff on a per-session basis. Session can change over the lifetime of an SDK.
And so this is a proposal to decouple those. Ted, where this stands, if you see, we have some approvals here. We have a lot of good discussions, and we have a prototype, I think, in JavaScript, we have a prototype in Java, and we have a prototype in Go.
So, we actually have all of the, things here. Unfortunately, Daniel's on vacation right now, so…
One of the prototypers isn't here. David has a prototype. I think this one's ready to go and ready to get approved, but we were waiting for the browser SIG to actually comment on this, and…
tell us whether or not this design is actually going to meet its needs. So that's one of the things we'd like to see. But the TLDR here is, is, think of it like the SDK can start reporting information
about resources that are not necessarily the same as the SDK itself. And so, I can use entities to determine what of my resource
is the same in the thing I'm going to report, and what is different, and construct a new resource and report data. So that's what this one is.
again, just a reminder, folks, I think there was a lot of good discussion here. From my understanding, most of this should be resolved, although some of this is out of date, because this was a big, long discussion. We moved…
I… David Ashball had a bunch of really good suggestions that we moved towards with what we ended up with. The JS prototype is up to date, so I think we're doing pretty good here.
Okay.
Yeah, this is, I think, the only comment left to be addressed in it, but since it's an OTEP, my… my thinking is that we can move forward, and resolve this when we turn this into specification.
For context, this is just a question about, right now, you can only make a new thing against a single entity, but it turns out resources are composed of multiple entities, so the question is, do we need the ability to pass in multiple entities
in this method, and honestly, nothing really changes in the proposal if you allow it or disallow it. So, we could have done it, we just were lazy in our prototypes.
But it's… it's… yeah.
Okay, cool.
Great, so that's the status of that. Are there any questions before I move on?
Alright, next up, we have, kind of what we're working on right now. There's two bits to this. One is the entity resource algorithm. So this is where I can take a list of entities and create a resource. This is how they merge together and rules around them. This does not have…
approvals on it, even though in the SIG, we don't really have anything we've been talking about on this algorithm, because we kind of hash things out, but it does need the formal approvals. Basic just is,
We need a way to take a bunch of entities and turn them back into that attribute list that resource expects.
And so this defines what that is. Now that entities have types, we need to know how we deal with the fact that we might have an entity of a Cates container, an entity of a Cates deployment, and we might need to put those things together into a big ol' resource, and figure out what that looks like for the user.
So this defines that, that specification. I don't think I'm showing it, apparently.
Yeah, so that's what this one does, if we want to see…
There's, two pieces to this. There's the bit, on the…
how to merge entities together, so you can determine if two entities are the same, how their attributes get merged together, and how you can prevent actually merging bad things with… if the entity identity is the same. And then there's a bit here on the resource data model.
which describes, how to compress identities back into a resource that gives you back the flattening, problem. So…
Flattening problem is… Sorry, I'm…
I should have prepped for this, Ted, I'm a bit scatterbrained. But anyway, the flattening problem with entities. We have the notion of an entity of, like, a Kate's pod, a Kate's container, a service instance, that sort of thing.
let's say I have a service instance, and I have a Kate's pod, and I want to create a resource. Well, I get labels of, you know, Kate's pod ID, and service instance ID, and service name. Great, because I collapsed all those entities.
But in practice, because this is open telemetry and people can do whatever the hell they want, they might give a bunch of entities the same attribute.
And so I might have an entity that has an attribute called host.id.
And that would be on an entity called AWS ECC2. And then I might have another entity that was detected from, like, a generic host detector that has a host ID, on an entity called host.
And when I try to collapse these, I now have two attributes that are in conflict across the two entities. And so, we're trying to give you a more holistic view of the world, where basically one will win and one will lose.
And you kind of have choice as a user which one you pick, based on how you've set up your configuration for resource detection.
But you will not get weird, conflicting states where, for example,
I will try to attach, entity information
That doesn't actually belong on that entity.
So, for example, this merge algorithm should work in the SDK and in the collector.
If I'm in the collector, and I'm running as a gateway, and someone is reporting data from one process to another.
and I have a host detector configured as a resource detection processor, I should not attach my local collector host information
To data that comes from a different host than where the collector's running.
And the entity algorithm merge is supposed to basically handle that for you implicitly.
So that's one of the things that this is supposed to do. That's one of the reasons why we're taking a long time kind of getting this sorted out. And that's, led to the next set of problems we're trying to work on to make sure that this is solid.
Right now, if you look at this algorithm, we have a bunch of different implementations of it. It's part of all of our prototypes, and I think it's pretty solid.
The caveat we have is there's a few issues in the collector we're working on next.
Which is where I'm gonna talk about the, entity events and relationship model.
But…
hopefully I did this justice, I'm sort of just word vomiting, apologies. This is better described in the actual PRs and things. Does anyone have questions before I move on?
Ted Young 00:29:49 I think the key element here is it's not just a merge algorithm, like, what splats on top of what.
you know, from, like, a dictionary or a map standpoint. It's about that trickiness of, like, which of these should I be applying to what?
Versus accidentally misapplying information, right? So, there's some…
Like, domain-specific understanding that's going on in there.
Not just a mathematical algorithm.
Josh Suereth 00:30:20 Exactly, exactly, yes. And we're trying to make sure that users have enough control to get the thing that they want done, done, and that we avoid a certain class of issues that we had previously, yep.
Ted Young 00:30:31 But that's the reason why people should have a look at this and review it, right?
Josh Suereth 00:30:34 Yes.
Ted Young 00:30:35 Is that domain-specific?
Application being handled correctly.
Josh Suereth 00:30:40 Yeah, and I think… I don't remember if it's in this PR, when we defined the merge algorithm initially, we had a bunch of, it's in the OTEP, so actually, if you were to look in our OTEPs.
I believe it's in the original OTEP, I might have moved it somewhere else.
Yeah, if you, if you look in here, I think we have a use cases.
This is… this is describing the use cases that Entity is supposed to help resolve, right?
Of, and at the time, we were calling something a resource provider, where we would have different detection, and what we're trying to get
2…
is where OpenTelemetry can have pluggable resource detectors, and they can all work together and not blow each other away, and kind of fight over who owns which, and that you get the data you want from all these different detectors. So there's a set of…
If you want to know the rationale behind the current merge algorithm, this kind of walks through all those different scenarios and what we're trying to achieve, with different detection and, and,
architectures. So this is the collector use case, for example, where the collector's detecting,
a different host than the resource provider here, and we want to make sure that the additional information, like host name, host OS, that kind of crap, doesn't get slammed onto your resource when you go through that collector, but the collector doesn't have to, like.
You don't have to hard-code the collector to say, cool, here's the channel for local things, and here's a separate channel for remote things, and I have two different pipelines. No, you can use the same pipeline, because the resource detection processor's smart enough to do the right thing. That's what we're looking for here.
Okay.
Yeah, so if you're curious about rationale, this was, this was the OTEP from, from, man, about a year ago.
Of why the algorithm is the way it is.
And then, the last bit, which we're running into now, is,
Entity relationships. So this is defining an entity relationship model. This is the latest discussions we've been having. Waiting for GitHub to load.
the,
there's some motivation here. The reality is, as we work through entities, and resources, there's a bunch of questions now. We have this notion of the telescoping resource, where today we just slam attributes on as we need to account for more information, we're gonna have a telescoping set of entities that we can have a resource.
We're starting to have questions where we might need to understand the relationship between them and what that looks like.
And we need enough of a, data model
That we're confident the direction we're moving won't get blocked in the future.
So we're trying to do just enough definition of relationship to kind of unblock the rest of this work and kind of understand what's going on. The open question in our mind is basically, do we need to expand what's available in a resource to include relationships, or can we have them completely as a separate side channel?
That's… that's foundationally what we're trying to answer. So, to start with, we're taking the existing OpenTelemetry Collector, entity reporting
receivers, which, if you're not familiar, there's a Cates Object receiver that will watch Kubernetes.
track CRD update events, and then fire, like, hey, here's the state of this object.
And we're looking at that as kind of one of the foundational pieces of entity relationship reporting, where we can say, cool, if you want to report your telemetry with just, like, the Cates container ID,
or the, sorry, the Cates pod ID, and you want deployment to come from the separate side channel and understanding of relationships, you should be able to use the Cates Object Receiver thing, or Kate… I think it's called…
Kate's Object Receiver. It's… there's a bunch of Kates in there, and I get one of them confused with the other, so apologies. There's a Cates event receiver, but I think it's Kate's Object Receiver.
And you should be able to use, you know, just a vanilla, out-of-the-box OpenTelemetry, SDK.
And you should be able to have an experience where you can still understand what deployment a resource is part of.
if we've gotten this data model right and have defined these things correctly. However.
inside of the collector, if you're using the collector, the Cates annotation processor, this Cates attribute processor, should be able to leverage entities to make smart decisions for attaching data that you need. So if you want to layer in the deployment in the collector, you totally can do so.
If you want to have it a separate channel, totally can do so. This should not break existing users, it should just give you new opportunities and new architectures.
Inside of this, I think the big challenge we just had, which was my major concern here, is now resolved, and I need to go back and comment that as such. I think, Dimitri and I talked about this, and there's a…
Yeah, here's the… here's the change, but, the… the TLDR, this defines a few things. This defines…
Events to describe the state of a system.
That will get sent to an observability backend to reproduce that state. So, if I wanted to understand a graph of what Kubernetes clusters I have.
What deployments are in those Kubernetes clusters?
this is the signal that will tell you that. So if I…
Another way I phrase this for observability, it's the left-hand navigation bar.
Right? I want to have a left-hand bar of what are my clusters, what are the deployments, and then I can click on one and then go view all the signals. Here's the metrics and stuff for that one. I might have an overall dashboard that just tells me what's red, but when I dive in, I can use this for the other kind of correlation, the…
This is your resource context correlation, right?
Okay, so this helps you build that left-hand nav panel, and it needs to send that state, but it's basically a state synchronization algorithm.
So what we're talking about are, there's a when to use it, so when you need to track relationships, and when you want complex descriptive information.
From your objects that you don't want to send
every single time and every single piece of data from, like, every lock. So if I wanted to have something that's expensive to send,
Alright.
The way this works is there's, two types of events. There's a state event and a delete event.
And the state event basically gets emitted to say, here's the current state of an entity.
and a delete event says, oh, by the way, an entity was deleted. We have a bunch of discussions around this, about
Effectively having 3 events, an entity state, an entity update, entity delete,
I'll go into detail of how we resolved it, but I'll just walk through the basic gist.
One of the important things with an entity-state event is you get the entity, you get its description, and this description we expect to be way more verbose than what would be in resource.
For example, you could put in complex types, you could put in whatever the hell you want here. It might be the full CRD from Kubernetes, if you're trying to synchronize that deeply, and you want to do, like, different kube state tracking things.
Great. This, this, this can be… this does not have to be small.
The other bit is entity relationships will be included, and this can be relationships of your entity and how you relate to others. This is the next thing that we're going to be talking through, is…
what does the relationship model look like? Today, this is defined as a string that describes the relationship.
And then a set of entities that you point at.
The question that I think we saw was.
Is just using a string to describe a relationship enough?
What does that relationship mean? We know that there's a few relationships that we want to have here. The first one being, who is my controller? So if I'm a Kubernetes pod.
I'm controlled by, say, a replica set. That replica set is controlled by a deployment. That deployment might be controlled by something else. So this is a way for us to understand the hierarchy of CRD hell in Kubernetes.
For service, if I'm an instance of a service, I know who my parent is. Like, I know that this service instance is controlled by the service, or owned by the service, so there might be an owner relationship.
there is an is-the-same-as relationship. So, if we're reporting process information, that might be in an entity that has no contextual awareness of anything outside of, I'm a process, and here's information about me.
But we can say this process is this… this process ID is the same as this container that's running this process, right?
Or I can say this service instance is the same as this…
pod in Kubernetes. So, you know how OpenTelemetry has service, service.name, service.instanceID? We can actually declare there is a relationship, this service instance is the same thing as this thing, and so when you start drawing your boundaries and doing your left-hand nav, it all works out.
That's what relationships are for.
if I'm very hand-wavy around relationships, it's because that's literally what we're trying to go in and model and define better.
Alright, lastly, in this model, there's a report interval timestamp, so the idea would be you get an update status on entities.
And report interval is one of the ways you can determine if Data has been deleted.
We're trying to make this protocol allow for drops.
And so, if you get a report of an entity.
and that entity is then deleted, but the delete event doesn't make it to you for a various number of reasons. You are responsible, this is a cache, you're keeping a cache of the state of the entity.
For understanding whether or not you need to drop your cash.
Right? And so the report interval is a way for us to tell you, hey, I plan to report this every 10 minutes. So if you don't see something for 20 minutes.
Probably it's not there anymore, you can go clean up.
Let's see, what else was useful here… Event emission future considerations…
Entity Delete has a few questions on it, but I think it's an optimization. You still have to be tracking that, report state. Entity Delete is just to make sure that
If things are flowing smoothly and no data's dropped, you can actually delete entities right when… right when you need to.
Right, and this is more about entity relationship structure I was just talking about. So, yeah, we have scheduled on, contains, depends on, and then there's a definition of standard relationship types we're working out. This, I expect to have a lot more discussion.
Before this gets merged.
Because this is not an OTEP, this is actually for the specification, so whatever's defined here is more binding, so we're… it's taking us a little bit longer to get through this.
I did a lot of talking there. Are there… are there questions or thoughts, or is this still way out of left field for folks?
Liudmila Molkova 00:42:22 I have a stupid question, sorry, Josh.
Josh Suereth 00:42:24 Yeah.
Liudmila Molkova 00:42:25 why, attributes are grouped into a map? Why not
Just have attributes as is on the event.
Josh Suereth 00:42:38 Attributes as is on the events.
Liudmila Molkova 00:42:41 So, like, if you look into attributes or entity ID, entity ID is a single attribute on the event. There's a map of
Attributes, right?
why not just have, I don't know, host ID or whatever attribute is as an attribute?
Josh Suereth 00:43:00 Oh, why not just have one attribute as the ID?
Liudmila Molkova 00:43:04 No, no, no, why… let's say I have an entity with two attributes, foo and bar.
Both are identifying.
In this proposal, the entity ID is a complex attribute, it's a map, with foo and bar as the keys, right? Why? It couldn't be just foo bar in the…
Top squad.
Top level.
Josh Suereth 00:43:30 Yeah, this is… this is confusing the way this is worded. So, the string would be the… the open telemetry attribute. So, entity ID is composed of attributes. This is the data model.
But the… the attribute itself would be, you know, it… let's say… let's talk about process, because process… the… there's the PID, and then a timestamp. And we've decided that we need both to be uniquely identifying.
If I recall correctly. So, in that case, the entity ID would actually be the… a map of string of PID, and and timestamp, created timestamp.
And then the value would be the PID and the creative timestamp.
So it's actually not string string. I can make a comment on this. I think this is just…
Kind of an oversight.
Liudmila Molkova 00:44:14 My question is more like, why not? PID is an attribute?
On the event.
Because you need to separate identity from descriptive, right? That's probably the reason.
Josh Suereth 00:44:28 Oh, oh, oh, I see what you're… why… like, because this is a log event.
Liudmila Molkova 00:44:32 Yeah.
Josh Suereth 00:44:35 Yeah, that's… I'm not even there yet, Lyudmila. At this point in time, I'm thinking about the data model of what the event structure needs to be and contain, and then how we encode it into logs, if we're going to use logs. Great. There was a… there's a potential this would be its own signal type that would have its own protocol.
In which case, we can have those… but I'm not… I'm not… I'm honestly not at that point yet. I'm more at, is this the right data model to get the data from A to B, and to do all the operations we need on it?
Liudmila Molkova 00:45:04 Okay.
Josh Suereth 00:45:05 Yeah.
So, great question, and I would love to dive into it after I've answered the other question of, like, is, you know, is this the right place for the ID, right? Yeah.
Cool.
Any other.
Ted Young 00:45:25 I got a random question for you, Josh. Something that I saw come up recently
was around sharing resources between tools. I think it was specifically profiling, like, the profiler wanting to know some resource information from Obi.
But you could just as well see any one of these things getting loaded up with resources that the other ones want to know about.
And I'm curious whether, as part of putting entities together, if you see, like, a clean way
To resolve that kind of resource sharing.
Josh Suereth 00:46:06 Yeah, that one… so, I think… my hope is that entities can help.
Because you should not have to share quite so much data, and then be able to reconstruct
from this side channel. I'm gonna pull up that, that,
that OTEP, so that folks can see this. That one more specifically, is about, correlating OB traces to profiles.
Did that one already get merged? The, that OTAP?
Oh, here it is.
Okay, so this one, this one is more specifically focused on, like, if you're an SDK,
and there is something outside of your process. This is what I would call cooperative eBPF programming. So, I'm running in the SDK, and something external to me is going to be actually helping me with observability, like profiling, that sort of thing. How do I tell it what resources I detected?
Generically.
Yeah, and so this one is, like, attaching, you know, I allocate blocks of memory that eBBF can read, and I'm gonna put my context in there, and then anyone who wants to interact with this process knows to look at that spot first to see if there's data, and if so, that's, like, the detection part that happened.
So I think what entities could do here is you could actually put less information. You can put just the identifying information you need from, like, an entity, and then you can expect that process to be able to infer
the relation… from relationships, what else to add, right? That would be the theory.
This happens in eBPF space. Yeah, yeah, Florian's exactly right. It happens in eBPF space, is where that.
Ted Young 00:47:54 That sharing kind of needs to go on.
Josh Suereth 00:47:56 So, it's a good question, and it's semi-related. One of the things we pushed for was the,
This sharing is going to use the resource proto. So, whatever we do with entities, resource will be able to use, or this will be able to use for sharing information.
Ted Young 00:48:11 I think part of my curiosity was if you assume all these different things are sending their data to, like, a local collector or something.
does… would you have to do less of this kind of pre-sharing? Because…
the entity, you know, resolver is gonna properly attach all of this stuff when it.
Josh Suereth 00:48:33 Yeah. Oh, that's a good… that's another… yeah, so basically, if… if Obi knows what process it's observing.
Ted Young 00:48:40 And the collector gets information from the SDK about the service-to-process connection.
Josh Suereth 00:48:47 So it knows that this process is the service. The collector could then do the annotation on the OB data to say, cool, I know this process is a service, so I'm going to annotate the data with that. Yeah, that's… that's… again…
That's the kind of use case we want to unlock here, with entities, absolutely, yeah.
Ted Young 00:49:08 I see there's a hand raised.
Josh Suereth 00:49:10 Is that Evo?
Ivo Anjo 00:49:12 Yes, so I actually, I wanted to, to, like, last week, Tigran and, and David also, like, kind of asked, about this, which is,
Where, like, right now, the message that we have there is, we ship the resource.
Where do you see the multiple entities, multiple resources fitting in here? Because right now, we just have, like, one resource that we publish here.
Josh Suereth 00:49:45 So, the entities are in the resource, so I'll show you.
The way we do this, we did this to not break open telemetry. So right now, so much of OpenTelemetry relies on resource, being a flat list of attributes. So what we've done is, we have this layer on top of resource that you can provide.
Which is… there's this notion of an entity ref.
And if you… if you imagine, it's a bit awkward how this works, but basically, you can describe what the entities are, a repeated set of types, and then you def… you just… you have a… it's like a dictionary reference of which attributes in resource are the identifying attributes of that entity type.
So if you need to take entities and layer it into resource, you totally can. And if you are supporting the resource protocol, because we're in there as well.
Once entities land, and we start fleshing this out, you are going to be entity aware.
Great.
Ivo Anjo 00:50:47 Oh, okay, so we kind of get this for free, because we are embedding this exact message, and this message contains the…
Josh Suereth 00:50:54 Yes, and my comments on your OTEP were specifically for this, to make sure that when entities land.
Ivo Anjo 00:50:58 Okay.
Josh Suereth 00:50:59 message, everything, everything should work. Yep.
Ivo Anjo 00:51:02 Okay, okay, that clarifies it, thank you.
Josh Suereth 00:51:05 Yep.
Cool. Let's see… last, I guess I'll just say, we have a… we have a…
We have a project board, and this is covering, all the things happening in the entity space, if you're ever curious. We were… we did want to launch last year with a,
a… what are we calling? I forget… I forget how we changed the stability levels, and I would look it up before we actually officially do this, but we were going to make an announcement to everyone about the resource changes, and we were going to, start on the actual prototypes in the… in languages. So we were going to actually have the…
Declare the specification ready to start prototyping.
for real in SDKs, where we get those… instead of prototypes being PRs, the prototypes would start to be kind of merged into experimental phases with flags to flip it on. That's where we wanted to be at the end of last year.
due to, like, some of the challenges, of getting through things, we delayed that. So, my guess is it'll probably be…
honestly, about June before it actually lands. We need to update this and talk about this in the SIG. If any folks are interested in helping here, you can see
You know, our current phase
is trying to get this resource entity mapping where SDKs and the collector can solve that set of challenges I was… I was talking about. Is this still… this is sharing, yeah.
where we can solve that issue of, like, you know, I have a whole bunch of people talking to Collector, I want to add in a bunch of information, and I want to track those relationships somehow and get them in.
That is kind of what we're currently targeting as our first milestone. When that lands and is successful, we're considering that done.
that requires… SDKs supporting the entity concept in their resource detection.
we want to leverage, actually, the configuration, configuration SIG did us a good service and actually split up resource detection into consumable pieces the way entities wanted them to be anyway. So, we might just hijack your configured resource detectors and have them be entity aware.
For what configuration SIG has, and
Yeah, that's… that's the work that needs to get done in this Phase 1.
So, right now, it's basically getting all the stuff in the spec, and… yeah, that's the metrics here. Getting stuff into the spec, and then getting the SDKs actually producing entities, getting the collector able to understand entities, which it does today, but not in all locations, and do the right thing once it has entities.
Then, we have this Phase 1B, which is, what we call the Entity Manager OTEP, but this is that multi-resource reporting. So this is then expanding SDKs to be able to export data not for the resource in which it is,
which the SDK is, you know, for, like, a different resource, or a resource that doesn't match its lifecycle.
And then, Phase 2 would be where we can actually fire entities completely as a separate signal, and figure out
you know.
details of what that looks like. There's a set of just big challenges there to continue to flush out. We're doing just enough of this to make sure Phase 1 won't run into blocks by the time we get to Phase 2.
Okay.
I did a lot of talking. Any, any other questions?
Ted Young 00:54:43 It was super helpful to get an overview. Thank you so much.
Feels close.
Josh Suereth 00:54:48 Yeah, I feel like we should, probably do this for all of our big SIGs, honestly. What do you think about having, like, a monthly, SIG comes in and does a status update for all of us here on how things are going and what their challenges are?
Ted Young 00:55:03 Sounds great, yeah.
Especially for the spec-related stuff, for sure.
Jack Berg 00:55:07 The spec sub-sigs? Yeah, that's a… that seems like something we should have been doing.
Ted Young 00:55:14 Alright.
Josh Suereth 00:55:15 I'll put a proposal together. Well, I'll just mention it. Ted, would you like to take that, actually, and, like, formalize that?
Yeah.
Ted Young 00:55:24 Sure, just put a schedule together, yeah.
Josh Suereth 00:55:26 Yeah.
That'd be good, and in the future, if I have time to prepare, I promise it'll be less word vomiting.
Ted Young 00:55:34 Yeah.
Josh Suereth 00:55:35 Cool. What would we want to do next, is the question. I think, Jack, you did an informal one for config, which was more awesome than I thought.
Or then I knew, I should say.
Jack Berg 00:55:49 Let me, let me look at the, the list of specs we have real quick.
Ted Young 00:55:54 So the spec sub-sigs are…
Jack Berg 00:55:58 Profiling, Prometheus, Gen AI, oh, that's actually a semantic invention, SIG. Configuration entities… Logs and sampling.
So, which of those do we feel most disconnected with?
Trask Stalnaker 00:56:18 Logs and events would be a good one, good topic.
Ted Young 00:56:23 Yeah.
Josh Suereth 00:56:23 I was gonna go in order of logs than sampling. Sampling, I feel like, is so close. They have such good specification work, and I think it needs to get pushed across the line.
Logs and events, though, How are y'all doing? Let's find out next week.
This is an advertisement.
Liudmila Molkova 00:56:41 Oh, we already destabilize everything!
Jack Berg 00:56:46 Sorry, Ludemil?
Liudmila Molkova 00:56:48 I was joking. We are ready to stabilize everything, but it's not… it's only half-joking. We are… we would like to stabilize all we can by the end of this year.
Ted Young 00:56:58 That would be great. Yeah.
Trask Stalnaker 00:57:01 Definitely some interesting progress and topics to share here.
Jack Berg 00:57:06 So how do we… like, just… just because we have a couple of minutes left, we could either, like, you know, continue to be excited about this, because we… this went well for entities today, and, you know, just jump into this same type of, you know, long-form informed topic for… for next week's specsig, or we could do this, like, monthly or something like that.
Josh Suereth 00:57:26 I think we do it monthly, I was joking about next week. Sorry, that was… that was literally a joke, that was not… Because, because I think, like, yeah, my, my, my, my top three would be, I think, logging, sampling, and then I'm involved with profiling, but I don't know how everyone else is. I know, like, Florian's here, and we're talking about…
that I think getting, profiling has a lot of really cool stuff they're doing with our protocol, a lot of really cool benchmarking and stuff they figured out. I think it'd be good to have a dump from them. So in terms of readiness to
give information to this group, they might be further along with some of the stuff they can say. I don't know, I'm just closer to them, so I, like, I already know that, but I… anyway.
I think this would be useful, let's do it monthly.
Liudmila Molkova 00:58:11 I think it would be useful to have not just the specs on 6, but this is the only cross-project meeting for maintainers we have.
I would love to learn more about OBI, their roadmap, and just any SIG that's interested, we can prioritize and schedule it, especially after we will do it for a few SIGs, and we will run out of super hot topics.
Jack Berg 00:58:38 I'd want to do two things, Ludmilla. I'd want to say, like, SIGs that want to talk about their topics, they can, but spec sub-sigs, we should… I think we should obligate them to have periodic updates.
Like, it shouldn't be optional. Yeah.
Ted Young 00:58:56 Makes a lot of sense.
But yeah, to your point, Lyudmil, I would love to include, you know, it's not technically a spec sub-sig, but all the stuff with the injector and, like, Linux packaging, like, our new approach to trying to package everything up is definitely something.
It would be great to highlight here.
Because that affects everybody in terms of understanding how that's supposed to work.
So, we could throw that one in the mix. I don't know, I almost feel like…
Even more often than monthly.
Or, like, having one of these things queued up and ready to go, but if we have too many topics, maybe it gets bumped.
Maybe we find a way of prioritizing emergency topics versus scheduled topics?
Josh Suereth 00:59:46 I… I… yeah, because it doesn't have to be the whole time, it can be 30 minutes, right?
So… Yeah.
Yeah, why don't we… why don't we get a cue of who we can reach out to, and I think, at a minimum, give them 2 weeks to get ready, because I think not everybody wants to do an off-the-cuff thing, or is comfortable with it, so we should be…
Be reasonable in that sense, yeah. But just say, hey, you know, in two weeks or a month, we'd like to have, you know, here's…
here's your time slot, you get 30 minutes, give us a state of the world and, like, the challenges you have, where you could use help, that kind of stuff, and then we get a queue of those going. I… yeah.
I…
Let's bounce… let's bounce it out. If you wanted to start with 2 weeks, and we degrade down to a month, just because we haven't done these in a while.
That would… that could make sense.
Ted Young 01:00:36 I like that.
Josh Suereth 01:00:37 Yeah.
Cool. I'm gonna call it, though. We're over time. Thanks, everybody. This was a really good discussion, and kind of off the cuff, so awesome. Good suggestion, Ted.
Jack Berg 01:00:46 Thanks, see ya.
Trask Stalnaker 01:00:48 Thanks, bye.
