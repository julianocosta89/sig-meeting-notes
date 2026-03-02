SIG: Entities SIG
Date: 2025-08-28
Duration: 52 minutes
Zoom Recording URL: https://zoom.us/rec/share/JUCKPlLPOy3YyuFHxPGMsjr1AmEzw615SJSK373GOMap10rUjFAjwHvNQZK4XqjL.VFW-DDmyPOlggeQf
============================================================

## Zoom Recording Transcript

**Nathan Smith @ Elastic Observability** 02:52 Hello.
**Josh Suereth** 02:54 Hey!
Hey, how's it going?
**Nathan Smith @ Elastic Observability** 02:59 Hmm… Ew.
**Josh Suereth** 03:03 I know Dimitri can't make it today, so it might be a light day.
**Daniel Dyla (Dynatrace)** 03:12 Hello there.
**Josh Suereth** 03:13 8.
Alright.
How we all doing?
**Daniel Dyla (Dynatrace)** 03:21 Okay.
**Josh Suereth** 03:35 Alright. We have two agenda items today, and then, probably the triage.
Just add that. Anyone else have an agenda item?
**Daniel Dyla (Dynatrace)** 03:52 I do not. Dimitri tagged me, said he wanted to talk about a comment from me.
on his PR inspect repo.
**Josh Suereth** 04:04 Let's do….
**Daniel Dyla (Dynatrace)** 04:05 I already forgot what comment I made.
**Josh Suereth** 04:08 Dimitri's PR, and spec, yeah. … let me….
**Daniel Dyla (Dynatrace)** 04:16 I know.
I was asking why… The environment, …
entity detector is not… you know, why is it implemented as an SDK feature and not just, like, an entity detector?
**Josh Suereth** 04:34 … yeah?
**Daniel Dyla (Dynatrace)** 04:38 Because the way the spec is written now, it's like the SDK must read these things.
It makes it a little bit less obvious.
**Josh Suereth** 04:46 That, I think, is the… yeah, here, you know, hold on, let's, ….
**Daniel Dyla (Dynatrace)** 04:52 We can talk about… sorry, we'll go in the order you have the agenda.
**Josh Suereth** 04:55 No, I had a comment to Lyudmila about the same thing. I responded to a comment from her. I think the main problem with this PR is…
it does… it's not the whole entity spec all in one shebang. And so it needs to defer to things that don't exist.
That's fine.
**Daniel Dyla (Dynatrace)** 05:14 I think.
**Josh Suereth** 05:15 We're gonna be asking him to add those things, and then he does, and then it looks super awkward. Yeah.
**Daniel Dyla (Dynatrace)** 05:19 Yeah, I think for something like entities, where it's, like, literally in early development.
deferring to things that actually don't exist is fine. You just link to, like, Entity Detector, and then it links to some heading, and when you click on that, it says to-do, and like.
**Josh Suereth** 05:36 Yeah.
**Daniel Dyla (Dynatrace)** 05:37 Fine.
**Josh Suereth** 05:38 Yeah, so maybe we'll discuss that when we get to the PR, about what to do. Or we can do that now, because let's just… why don't we just go through that?
Alright.
**Daniel Dyla (Dynatrace)** 05:48 Whatever order you want to do is fine. Keep in mind, we only have 25 minutes left.
**Josh Suereth** 05:52 Yeah, it's fine. I don't have anything, like, super… I think mostly we just need to do a lot of reviews. Okay. Okay. So, we had the puzzled statements, so this one with Lyudmila is basically… she had a question about how should conflicts be resolved, right?
And so, Dimitri added how conflicts are resolved.
But the reality is, that should defer
to, like, this is used as an entity detector, and the conflict resolution between entity detectors and resource detectors need to be called out in the spec. And so, I think our suggestion would be here… I'll add this, yeah.
Suggestion from Sid.
We should create a section on Entity Detector.
Which is to-do… Fill out.
And another on… Conflicts between… resource… Detection and Entity Detector.
Which is… To do. Fill out.
in this… Specification here should call out that…
There will be an end entity detector.
Which uses this format to detect.
Entities.
And we can address the problem. Come on.
Gibbling.
What's, ….
**Daniel Dyla (Dynatrace)** 07:27 Yeah, and I think, just to make it clear, that this PR is not expected to actually fill out those to-dos.
**Josh Suereth** 07:34 Yeah, yeah.
**Daniel Dyla (Dynatrace)** 07:35 I think that's clear enough.
**Josh Suereth** 07:37 We always have the problem where perfect is the enemy of good.
**Daniel Dyla (Dynatrace)** 07:40 Yeah, and I think people…
you know, address a comment in a PR doesn't always mean I did the thing that somebody suggested. Sometimes it means, like, I addressed it by saying we're doing it later.
**Josh Suereth** 07:55 Yeah.
And… yep. Cool.
So I think… I think that's, … that's that. That was… that was my… my general thinking here, and that's… that's what we had. I think if that happens, we need, like, another one or two reviewers here before we can merge. I mean, technically we could merge now, but I think we should clean that up.
… And then, … try to get… I think, …
Daniel, you and Lyudmila, I'd appreciate… like, let's try to get both of those concerns addressed before we merge. That sound good?
**Daniel Dyla (Dynatrace)** 08:35 Okay. ….
**Josh Suereth** 08:37 Awesome.
So… action.
Defer to sections that don't exist.
Shadow to-dos. Okay.
Next up, this is a pull request to OpenTelemetry I.O.
This one's a fun one. …
They want to add entity definition here, because entity showed up in the spec. And they pulled the definition we have from our spec.
Which is appropriately generic and useless.
**Daniel Dyla (Dynatrace)** 09:09 Haha, yep.
**Josh Suereth** 09:12 So, what I wanted us to do is, if we were thinking in terms… so, like, in the specification, I think it's okay, because contextually, it's described around resource, it has resource in it, like, the generic description we have is not…
the worst. Like, it's not… I don't think it's actually causing issues, but I think that definition here would be causing issues. So if we go to… where is that… the terminology one?
Is it concepts?
Yeah.
Yeah, glass room.
**Daniel Dyla (Dynatrace)** 09:51 Monitor resources.
**Josh Suereth** 09:53 Oh, it's probably glossary, yeah. Resources and Glossary. Like, if they want to add this term here, right, I think we should look at what resource says.
Which is here.
Captures information about the entity producing telemetry as attributes. Oh gosh, I clicked the wrong thing again, sorry.
I clicked on it. For example, a process-producing telemetry that's running in a container on Kubernetes has a process name, a pod name, a namespace, and possibly a deployment name. All these attributes can be included in resource. So I feel like we can take this and change the description to basically
We could use the description of resource and entity together, right?
**Daniel Dyla (Dynatrace)** 10:36 Yeah, I was gonna say…
One can reference the other. So, we can either redefine resource as a collection of Entities and attributes.
Or, we leave resource as is, and we say an entity is a collection of resource attributes with a name and identifying and descriptive parts.
**Josh Suereth** 11:01 In the type, yeah.
**Daniel Dyla (Dynatrace)** 11:02 I… I actually… One way or the other.
**Josh Suereth** 11:05 Yeah, yeah, I think this is where, if we look at the spec…
… that we changed for resource.
Here we go.
I think… is it the high-level one?
Resources and repetition entity produced at temperature within open source signals associated with the resource, same architectural correlation… ….
**Daniel Dyla (Dynatrace)** 11:34 Yeah, so this… that's actually not true, and it's not true of entities either, because…
the resource attributes are not always describing the entity producing the telemetry. Sometimes the producer is external to the thing. It's more about
The thing described by the telemetry than it is the thing produced by the producing the telemetry.
Actually, resource muddles those concepts more than that.
office.
**Josh Suereth** 12:04 It does… yeah, well, we've allowed it to, basically, and we're trying to fix it.
**Daniel Dyla (Dynatrace)** 12:08 Yeah, but I… so I think as a starting place, it's a decent, definition.
I would say… I, I would say that resource…
I would define resources as a collection of entities and attributes, because I think it's easier to clearly define entities.
**Josh Suereth** 12:32 Yeah, because we, like, when we look at the data model, it explicitly says that, right?
**Daniel Dyla (Dynatrace)** 12:36 Yep, so I would say it is a collection of entities and attributes where an entity is a collection of attributes which describe a physical or logical
… Like, physical or logical object that is either producing or described by telemetry.
**Josh Suereth** 13:02 Well….
**Daniel Dyla (Dynatrace)** 13:03 I can type that out.
**Josh Suereth** 13:06 Because service is not physical, but sure, describes a.
**Daniel Dyla (Dynatrace)** 13:09 I said physical or logical.
**Josh Suereth** 13:11 Physical or logical object that what produces.
**Daniel Dyla (Dynatrace)** 13:16 That produces or is described by telemetry.
**Josh Suereth** 13:25 ….
**Daniel Dyla (Dynatrace)** 13:26 And I would say before entities describes, or in between entities describes, I would say entities is a collection of
attributes, which describes.
**Josh Suereth** 13:39 Well, I'm just gonna let, yeah, of entities, we'll say.
**Daniel Dyla (Dynatrace)** 13:44 Oh, yeah, I gotcha.
**Josh Suereth** 13:45 to concepts, or attributes, right?
**Daniel Dyla (Dynatrace)** 13:48 Yep.
**Josh Suereth** 13:48 Link to concept. Okay.
**Daniel Dyla (Dynatrace)** 13:51 Yep, and then Entities, same thing. Entities is a collection of… attributes.
**Josh Suereth** 13:58 Okay, and then we have entities.
A collection of attributes.
**Daniel Dyla (Dynatrace)** 14:07 Yep, and then… Yeah, that identify and describe.
**Josh Suereth** 14:13 Identify and describe.
**Daniel Dyla (Dynatrace)** 14:16 And then I would take.
**Josh Suereth** 14:17 Physical. Or logical.
**Daniel Dyla (Dynatrace)** 14:20 Yes.
**Josh Suereth** 14:21 objects that produce… telemetry. Actually, we can do this.
Well, you can just link to concept.
Yeah, that's exactly… I would say resource links to entity.
**Daniel Dyla (Dynatrace)** 14:37 Entity probably should not link back to resource, unless just to say related, but you don't want to have a…
A reference loop.
**Josh Suereth** 14:49 produce or is described. Actually, the producer is described isn't necessarily two of entities.
**Daniel Dyla (Dynatrace)** 14:56 is….
**Josh Suereth** 14:58 Because we might need to represent entities that, like, you don't necessarily produce data at, but you would aggregate data to, you know?
**Daniel Dyla (Dynatrace)** 15:08 Yeah, so I'd just say, is related to?
**Josh Suereth** 15:12 is related to… so an entity is… so this is where, I'm… this is where I'm going to phrase entities in resource describe a physical or logic object that produce
or…
that produce or are associated with total.
signals.
Maybe telemetry.
This is… this is where it gets confusing, right? So, we're currently using association in semantic conventions. Like, alright.
Let me, let me clarify my thought first before I talk.
entities
we can have things that you might not produce data about, right? So, an entity could be an organization.
And the organization might have a team, and that team might have a VM, right?
I could look across an organization and say,
how much CPU usage am I using, and I'm aggregating at that entity level.
But the organization isn't the one producing the data, it's just a…
Some… you know, it's… it is somehow related to that.
**Daniel Dyla (Dynatrace)** 16:27 Yeah, that's why I think related to is probably just, you know, that's still a relationship, even if it's not a direct relationship, it's still a relationship. You know, I'm still related to my second cousins.
**Josh Suereth** 16:39 Object, I see, okay, object that… Produces telemetry…
Or one that is related to an object.
That produces telemetry.
**Daniel Dyla (Dynatrace)** 16:57 Yep.
**Josh Suereth** 16:59 Yeah.
That's… a mouthful, but cool.
**Daniel Dyla (Dynatrace)** 17:03 Yeah, I… I would actually… say, if you think that's a mouthful, the second
like, clause there, where you say, OR is related to an object, you could just say, related to…
An entity, yeah, because then you still have to have producers' telemetry.
**Josh Suereth** 17:22 Another entity. There we go, yep.
**Daniel Dyla (Dynatrace)** 17:25 Yeah. Perfect.
**Josh Suereth** 17:31 And then….
**Daniel Dyla (Dynatrace)** 17:33 Technically emit entities without any telemetry?
And it's still… an entity.
It's… I just don't know why you would.
**Josh Suereth** 17:45 I'm gonna do this one, that describe… Object that produces…
or is associated with generated telemetry. How about that?
**Nathan Smith @ Elastic Observability** 18:01 I suppose you could get around that by saying.
Any… anything that we're producing telemetry describing the entity
is producing telemetry. Since we're producing telemetry
Saying what it is, even if we're just saying what it is.
**Daniel Dyla (Dynatrace)** 18:20 Yeah, I think we're running into the same problem. I think I brought this up in, like, the second entity's meeting. We use the same term for the data structure as the thing that it describes.
**Josh Suereth** 18:34 Yep.
**Nathan Smith @ Elastic Observability** 18:35 Yeah, it doesn't help that entity is a synonym for thing. So it's a really hard thing to work with.
**Daniel Dyla (Dynatrace)** 18:43 Right, because now we have to use, like.
verbal gymnastics, like physical or logical object, where it would be.
**Josh Suereth** 18:51 It is Tuesday.
**Daniel Dyla (Dynatrace)** 18:52 entity.
**Josh Suereth** 18:53 Rather than… rather than just use entity and produce an entity, yeah, because entity actually means something, yeah, agreed.
How about this? I think this, this, this I'm feeling more confident with. It's more crisp, but a collection of entities or attributes that identify or describe a physical or logical object that produces telemetry.
**Daniel Dyla (Dynatrace)** 19:13 Yeah, I like that, I think that's fine.
And then, I think… the… definition of entity…
I mean, you don't technically need produces or is related, you don't technically need that part. The only thing that makes it an entity is that it's a collection of attributes that identify and describe
Like, an entity… a CPU entity is still a CPU entity if you're not collecting CPU metrics.
**Josh Suereth** 19:44 Fair, fair, yeah.
**Daniel Dyla (Dynatrace)** 19:47 Because… and then… Yeah, it's just, you would only…
I would say as a separate sentence, entities are typically associated with telemetry data, or, you know, something along those lines.
**Josh Suereth** 20:08 Container… Service.
Yeah, this one we actually have to flesh out.
**Daniel Dyla (Dynatrace)** 20:14 Yeah, like, for example, a CPU entity describes a physical CPU which is monitored by, you know, which produces CPU metrics, or something like that, because just as an example.
**Josh Suereth** 20:34 of, … The logical grouping of processes that compose a, service.
Something like that. So we have a physical and a logical.
**Daniel Dyla (Dynatrace)** 20:51 Yeah.
**Josh Suereth** 21:01 service.
Okay.
Alright, so what I'm gonna do… we'll do this live, because… yay?
… discussed in HTSIG.
This suggests… updating the two concepts.
of resource… and entity… Together with these definitions.
Resource.
Okay… oh, you can't see what I'm typing.
Here we go.
Is this… that's not the right one.
Here's the right one.
… entity.
And… we're comfortable with this, right?
**Daniel Dyla (Dynatrace)** 22:03 Yeah, I think, you know, as a starting place, they may come back and say, that's confusing to me, and that's good feedback.
They may also just copy and paste it without thinking about it.
We never know.
**Josh Suereth** 22:20 Not WordShot, Wordsmith. There we go, more, but this, …
Specific.
Okay.
Cool. We have 8 minutes left, so I want to move on then. That's… that's the majority of what I wanted to get done. The spec update, PR. I don't know if anyone had a chance to read through this, …
I think, Dana, you had comments previously, and I think they were addressed with the, … with the changes we made here? Yeah.
All I want to call out is the major changes that happened in this PR since the last time we talked, because I want to get reviews from everyone here. Effectively, what we have now is we have some internal details about how initialization for SDK is now explicitly kind of part of the spec.
We have an API part of the spec, which defines the entity API that you will use when you are external.
… Or, or, like, to update things over time. And then for the SDK, We define a listener.
we add this resource initialized state, where the SDK actually won't send events until initialization is complete.
And then, we add, an entity provider creation section, where we basically say there are two things that, are given. You no longer give a set of entities to start. You actually give a set of detectors.
And a timeout. That is optional if you don't allow asynchronous startup.
But it's expected that the detectors are run by the entity provider, and when those are complete, then the initialized signal comes out.
… The other thing is, I think I called out two states for the entity provider.
It is either in a resource detection state, in which case It's initializing?
and it's running these resource detectors, and no events are fired, and then it's in an initialized state, where the complete resource is available and fired to everybody. Okay?
… I don't think there's a lot of other changes here besides, changing the actual
like, this is defined in the API instead of in the SDK. … I changed a little bit of the phrasing around concurrency, based on the prototype, and then we added, for update entity.
We added a little bit about the conflict resolution rules that we actually use.
from the conflict resolution before. So this is actually more in-depth.
… I believe I… oh, I have GetResource as an optional thing that can be provided.
as opposed to a required part of the SDK. So…
We can cut that. I'm actually not sold on it one way or another. I made it in the Java prototype, where it's completely, like, I don't need it anymore.
it's how we implemented the Java prototype initially, … I….
**Daniel Dyla (Dynatrace)** 25:26 That's part of the SDK spec, right?
**Josh Suereth** 25:28 That's part of the SDK, yeah.
**Daniel Dyla (Dynatrace)** 25:30 Yeah, I'm not sold on it. I mean, nowhere else.
anywhere. Do we have, like, read APIs in the API or the SDK? We treat memory tree as a sync.
Almost exclusively.
**Josh Suereth** 25:46 Metric Reader is a read API.
**Daniel Dyla (Dynatrace)** 25:50 Yeah, that's true, but I think that was more of an implementation detail.
Because we had poll metrics.
**Josh Suereth** 25:58 No, that's actually… most metric systems, even, like, all the pool-based ones… push-based ones I'm aware of.
You have a piece of metric storage where it's your hot path and everything collects into memory, and then even when you're pushing, you asynchronously decide, okay, I'm gonna read data and push it.
And so Metric Reader was, we have pluggable, you can define your own memory block for storing memory. If you can do it more efficiently than OTEL, go for it. And you can still wire into our exporter pipelines and get data out, right? So… but that's an implementation default for how metrics are designed. Like, that's the point of that, is…
HotPath metrics flow in.
And then something else can collect those metrics and read from that internal storage on its own timeline.
But you're right, like, it's not called GET.
It actually has a specific thing, like, it's a composed deal, so I think we could provide that as well. I'm fine cutting it, if you want to, like, comment on it, please do. In practice, what I did was I…
Right. All other signal providers… this is why I have it. All other signal providers, tracer provider, meter provider, etc, must be updated to use entity provider to obtain resource. This should be done either through list entity list or interface, but it may be done by a git resource operation.
**Daniel Dyla (Dynatrace)** 27:23 Mmm, I gotcha. Okay. Yeah.
**Josh Suereth** 27:26 So, so I just….
**Daniel Dyla (Dynatrace)** 27:27 to get resources better.
**Josh Suereth** 27:30 Yeah, yeah, like, we're basically saying we want this to be a listener-based interface, but
because I'm not sure of how we can implement this everywhere, we might need to allow that.
…
What I also call out is SDKs that do not provide Git resource operation may provide a latest resource component. This is what I built in Java. If you want, I can show you.
But it's just an entity listener that provides the latest resource. In fact, all….
**Daniel Dyla (Dynatrace)** 27:59 I guess the question is, at what point do you, like.
lock the resource. Is it when you obtain a tracer? Is it when you create a span? Is it when you end a span, or is it when you export a span?
**Josh Suereth** 28:13 Yes, that I don't have in the specification now, and I think that one is more complicated. I…
I can tell you my opinions. Hold on. Java… there it is… JSRETS… Open telemetry…
I'll just show you the… I updated the, prototype if you're curious.
Branches… The boot entity prototype… … What do I do?
contribute… I guess we do this, but I think I already have a thing.
Give me a files change.
… Yeah, if you want to see any, any changes here, …
I think they're at the bottom.
Let's do Latest Resource.
Supplier…
Java has the best names for everything. Yeah, so latest resource, what I do, we have an atomic reference to resource, we have an initialization lock.
And then what happens is, when you call GET, right.
If we don't have a resource, Then we actually lock.
We attempt to grab the resource, tracking timestamps, and we do the whole shenanigans of grab resource until the timestamp actually has died.
And once the timestamp is dead, we return the default resource to make sure that the SDK doesn't lock on startup. And I tested this by creating a resource detector that never finishes.
And then make sure that, like, the SDK doesn't block, right?
…
The other thing… the other thing here is there's implicit in resource detection. Java's completable result code, this is equivalent to a promise of a… of a result.
Right
So, it's a promise of a result code. That is how that's implemented, so that you can actually have asynchronous startup, and a resource detector can, like, spawn a thread to do something, or use an execute service, or whatever, right? To do things asynchronously.
So I don't know what the equivalent is in Node.js, but that's how that's implemented, if you wanted to, like, see how this works. Yay, Java concurrency. But anyway, anytime we get a change then, all I'm doing is lazy-setting the resource.
for… if you… if you're a concurrency buff, what that means is I say that I'm going to set the resource, but I don't put a memory pre… like, it's like, …
I'm not flushing memory actively. I'm not flushing the CPU cache. I expect that to happen on read, because when someone calls getResource.
or get, this here, when we call this GET, this will actually flush CPU caches for that particular block of code.
So, I'm basically not doing that when I write, and then doing that when I read.
And we're doing it every time we read. And in Java, where this happens is on export.
So, when I go to export a span, or when I go to export a metric.
That is when I will attach resource.
Kinda.
So… when I looked at the details, there's going to be some concurrency issues where
A span might be attached to a different resource than when it was started. But also.
if I start a spin on resource A and end it with resource B, what do I do, right?
**Daniel Dyla (Dynatrace)** 31:56 Yeah. So, I was just thinking about that, like, what if… It almost seems like…
The instrumentation should decide, because it might be different… the correct answer might be different for different instrumentations.
**Josh Suereth** 32:13 Yeah, yeah, well, my thinking here is twofold, right? Metrics are kind of a global storage thing, and so I think that the inaccuracy we get, we need to do some experimentation with browser, but the inaccuracy we get by doing this, I'm not as worried about.
Because if I'm reporting a metric against a browser session.
and the browser session has changed, right, the instrumentation probably should be clearing my metric before I report the next thing.
In some fashion. And we might need to figure out how to do that physically.
we can actually make the metric SDK clear memory.
**Daniel Dyla (Dynatrace)** 32:53 You need to report both, right? Like, if the session changes, you report your metric with the old session, and then you have a new…
metric, yeah.
**Josh Suereth** 33:03 Yeah, for now, for Java, I'm actually… because I'm not sure what we're going to do overall around this, I just sort of let it all flow through.
We're out of time, by the way, for you, if you have to go to the browser sig, so I don't want to hold you too long.
…
I'm letting everything flow through for two reasons. One, I actually have, … where can I show you this? When you… the entity builder.
You can provide a, … that's Entity Builder. No, I need the Entity Provider Builder.
Of course, it's Java, right? …
That's the entity provider… where's the entity provider builder? Here it is. You can provide a listener executor.
What this does is it actually lets you control the threading model used for startup.
One thing that I did, which you may hate or not, but I have a current thread executor service, okay?
In the current Thread Executor service, this completely blocks startup.
of the entire SDK.
Until the resource detectors are done.
Because none of the events actually fire out on different threads, and the actual waiting for resource detection happens on the local current thread, as opposed to spawning a executor for them to happen asynchronously. So in Java, you can actually fit… you can control and say, cool, I don't want to start up until resource is done.
It will block everything until that happens. Or you can configure to say, yes, I am fine with that, and here's the threading model I want for events firing across the SDK.
**Daniel Dyla (Dynatrace)** 34:44 it's not really an option for Node.js.
Right. Because any… anything you would do to block execution, even if you just said, like, Startup is asynchronous.
…
you… if the user application continues to start up, which it does, you… the load order is too important in Node.js. Like, in order for us to wrap
modules with our auto instrumentation, everything has to be done. So essentially, startup has to be synchronous, and if there's asynchronous resources and entities, it just can't be… they can't be there on startup, and we can't block.
So, what I did is… the entity detector returns
A promise of an entity, or, it could return an entity, a promise to an entity, or null .
And then…
If, basically, a promise to an entity says… is a signal that's like, don't return, or don't export until this resolves.
a synchronous entity is obvious, and null is obvious. It's like, we're… don't wait on anything, this is fine. And then, any changes that are not important for a startup, you call the entity APIs, like the modification APIs, right?
**Josh Suereth** 36:10 I see, yeah. I'm not returning antsy object, I'm actually always calling the synchronous APIs.
I just have two states for that API. For entity detectors, I give them one in the resource detection state, and then I flip to the final state, right?
**Daniel Dyla (Dynatrace)** 36:27 Yeah, in any case, I could do it the same way. I could just return, like, a result code promise, and then say, I will resolve this promise when I'm happy with startup. That would be fine as well.
**Josh Suereth** 36:41 Honestly, what you have works just fine. Like, they both work. I guess the thing I'm saying is, in Java, I can do both. I can have synchronous… synchronous resource initialization if I want, as a configuration parameter, or asynchronous. For JavaScript, you can't. You have to do one.
**Daniel Dyla (Dynatrace)** 36:58 not possible.
**Josh Suereth** 36:59 So, which I think this is… the reason I'm mentioning it is, as a prototype.
it gives us some good experimental capabilities, right? We can look at, in Android, having it be asynchronous, and having, like, entities change after the fact, and for servers, we could have the default just be, you know, synchronous, the same as it's always been. And so there's no real change of behavior.
Because of that.
**Daniel Dyla (Dynatrace)** 37:25 Yep, and then I would argue, it's mostly… not only is it signal-dependent, it may be instrumentation dependent, but the… like, where do you decide to lock the resource and say, this is what I'm using for the export? I would say for metrics.
if you have a change in resource, you should flush with the old one, and then create new metric streams with the new one, right? With traces, I would say most of the time.
I probably want… The resource state from the span start.
Like, when did the operation start? That's most of the time, I think, what I would want.
I could see Span End as a reasonable option.
I think an export is the least reasonable option, because with batching and waiting and stuff, it could be exported much later, and then, like.
you may just have incorrect telemetry. So, for example, I make a web request, and then I…
change my network on my phone, right, because I walked out of my Wi-Fi, and now I'm on cell network, and then it's exported? If it's associated with the cell network, that's just incorrect data.
So I would say you want the start of the span most of the time.
I think you could make the argument all of the time, And then you would have…
end-span attributes as, like, I'm overriding these specifically this time, but… …
I would… I would say span start is my gut feeling for what you want most of the time.
**Josh Suereth** 39:10 I think I'm inclined to agree with you. The thing that gets awkward… I think events and logs, by the way, just always pull current. Those are point-in-time things, right?
**Daniel Dyla (Dynatrace)** 39:20 Yeah, it's just….
**Josh Suereth** 39:21 There would be the mattress.
**Daniel Dyla (Dynatrace)** 39:22 only… yeah.
**Josh Suereth** 39:23 With metrics we should flush and create, we need to sort out… that's probably the next thing to prototype.
**Daniel Dyla (Dynatrace)** 39:28 Yep.
**Josh Suereth** 39:29 This, I think, if we're accepting span end can work, I believe that's what Java's actually doing, but it might be span start. I'll confirm that.
…
Because that was… you know, honestly, the way it works is in, … where is it? SDK Tracer? When it creates a span, it grabs the resource at that time. There's this thing called, shared state.
That is used to create spans, and it just grabs the resource when it creates a span and keeps it there.
…
So, I'm pretty sure, yeah, resource comes in when you start a span. So, in Java, it's actually span start.
So if you change resource after span start.
you get the previous one, the way it's implemented, because of how I was able to fire it through.
So, we're getting kind of what you want. I think that's what I want.
Metrics is on export. I don't have flush and create new. That is something we'll have to sort out, so I'll start looking into that. And events and logs is current, so this sounds like a good plan. Alright, so next step is…
Flush and create new on metrics, let's start debugging what that looks like.
**Daniel Dyla (Dynatrace)** 40:40 And I think that's the correct way to do it, just because, same thing, like, if you have metrics that are batched up and then you export them later, like, doing it on the
Like, the resource from the export time
Like, you always have to imagine a situation, like, what if they're exported tomorrow?
**Josh Suereth** 40:59 So, this gets into another conversation I want to have, which is multi-tenancy.
But…
I might actually just make the metric storage be multi-tenant. So, for example, there would be a metric storage for resource A,
And that's what's used when resource A is active, and then when I make resource B, I make a new storage thing, and then what… I will, like, garbage collect the previous storage.
**Daniel Dyla (Dynatrace)** 41:28 Yeah, they could theoretically run in parallel, although…
They won't, because any new incoming metric data points will go to the new one, but….
**Josh Suereth** 41:36 Except, think about this use case, because I actually have this internally. Think about when I say get meter, or get tracer, right? That I actually say, cool, I need to get a meter that's recording this other subentity right now.
And I… and I do that, and I report metrics against it. And I might call getMeter for different entities, right? So now, instrumentation scope has entity, and I have multi-tenancy.
Because I can say, grab me a new instrumentation scope for this entity, I want to record data about it. I think that's actually a pretty cool way for us to move forward, but way out of scope for what I'm trying to do right now.
**Daniel Dyla (Dynatrace)** 42:18 Yeah, I think the other… …
The other related topic there would be, like.
A server with two network interfaces.
You need to report metrics against both of them, but they have different entity… they have different resource info.
**Josh Suereth** 42:39 Yeah, what we recommend to people who are doing that now internally, is we say, instantiate two SDKs.
**Daniel Dyla (Dynatrace)** 42:46 Yeah.
**Josh Suereth** 42:47 And that seems bad.
**Daniel Dyla (Dynatrace)** 42:49 Yeah.
What we're doing, yeah.
I, I think…
Yeah, it's a recorded call, but at risk of getting in trouble, I would say most of the time what we're doing is telling people to install our proprietary agent in that case.
**Josh Suereth** 43:06 Okay, so, so, true.
**Daniel Dyla (Dynatrace)** 43:08 I think, I think doing it with….
**Josh Suereth** 43:10 How much your agent does, we'll do that, yeah.
**Daniel Dyla (Dynatrace)** 43:13 Yeah, I think the open source solution for us is, handle it in the collector. Because the collector can always do
essentially… Doesn't matter if it's valid or not, you can always… Create things for the collector.
**Josh Suereth** 43:29 Yeah, I'd like to fix that in some fashion, but okay. Alright, cool. I think we have next steps. In terms of project status, I don't see anything that's delaying us still. I think we're making progress, so I'm gonna leave that as still end of the year.
Any concerns?
**Daniel Dyla (Dynatrace)** 43:47 Fine with me.
**Josh Suereth** 43:48 Okay.
**Daniel Dyla (Dynatrace)** 43:48 I think our… we're… what are we right now, end of year at risk? Is that our current….
**Josh Suereth** 43:54 No, we're end of year on track, but I can change it to at risk if we want.
**Daniel Dyla (Dynatrace)** 43:58 I…
If we get to… yeah, I mean, we still got a quarter. I think we're fine to leave it as on track for now.
**Josh Suereth** 44:06 I do want to get this OTEP approved, like, as soon as possible, so….
**Daniel Dyla (Dynatrace)** 44:12 Yeah, so I was gonna say, with this PR specifically into Ted's, branch.
I would say, like, the bar to merge this should be pretty low. It's not very discoverable. I always have a hard time finding it when I'm looking for it. I would say, if Ted is happy with the changes you've made, merge them, and we'll review the details in the PR to.
**Josh Suereth** 44:36 in the main PR. That sounds good.
Alright, I'm gonna get rid of the do not merge on it, then. …
And change it from draft, yeah.
**Daniel Dyla (Dynatrace)** 44:45 Yeah, and I would just say, as long as Ted's happy with the changes, even if there's some details he would change, I would argue…
merge it into his branch, and then make… make detailed changes on the main PR.
**Josh Suereth** 44:58 Yep.
More changes to deploy our SDK interactions.
Fund resource change follow-up, yeah. Okay.
Cool update… Pull out a draft, and then… oh, I can merge it, actually, now.
I'll follow up with Ted and do that.
**Daniel Dyla (Dynatrace)** 45:23 the multi-tenancy question is gonna be stuck in my brain all day, though, because that… the situation that I just pointed out, where there's two network interfaces that use separate, …
that have separate resources, that could… I mean, you could have an instrumentation that has a similar concern. I can't think of one right now.
But, like… I guess if you're reporting…
Do we need the… do we need the…
instrumentation to be able to select which resource it's reporting against, or are we getting too into the weeds on that?
**Josh Suereth** 46:05 That's… that's what I'm saying, right? Like, I feel like that's why my current thinking and what I've been kind of debating, I don't want to derail our… all of our API discussion, but what if,
What if instead of reporting entities, via an API, right?
Only. We actually, when you get a meter, when you get a tracer, when you get a logger.
You actually provide an entity.
And that is the way that you say, cool, this is… all of this data is about this entity versus the default.
Or is that entity an expansion on the default, right? So your resource detector provides default information, and I say, get a meter for this, and that would be basically an override, a creator update on a resource, and now I report data against that resource, and I have multi-tenancy.
**Daniel Dyla (Dynatrace)** 47:00 about it, but you were.
**Josh Suereth** 47:00 That's the thing that's.
**Daniel Dyla (Dynatrace)** 47:01 single entity, not a whole resource. You just report one entity. Like, I am monitoring this network interface.
**Josh Suereth** 47:09 And that's it. Yeah, I mean, we could make it take a collection if we wanted, but the idea would be, when you say get meter, you'd say, cool, I want to get the meter, and I don't provide anything, I get the default resource. But if I say get meter, and here is a new network entity, right?
That means I'm reporting against a different network resource. And so the way you would do the reporting against two network connections is you would get the meter for the specific network connection you're reporting against.
And then write your metrics. So the instrumentation would look exactly the same, because it's an HTTP server, but the meter would be different, and you'd get that meter when you pick which one you're going after.
**Daniel Dyla (Dynatrace)** 47:50 Yeah, and if you get a meter twice with the same entity, you have to probably have the same storage, so there's some hashing that needs to be done there, maybe.
**Josh Suereth** 47:58 Exactly, which I may end up having to implement that anyway to do the shenanigans we're talking about with metrics.
… But, yeah, that's… that's an alternative I've been noodling in my head, and …
that's why I'm a bit nervous about our OTEP and our timeline, because
I kinda like that model better, honestly.
Personally.
**Daniel Dyla (Dynatrace)** 48:26 Yeah, I just don't know… like, in 99% of cases, the default resource is probably fine, right? So….
**Josh Suereth** 48:35 Right, but think about it this way. We don't need an entity provider API now. It's gone.
what we have instead is we have entities in entity detection, the way we were planning to, with SDK only.
And that provides the default resource. And then for these browser use cases, we just say, cool, grab a meter with the session, and report against that.
Right?
And that's how you dynamically do things, because we need, actually, deeper integration with the SDK.
Anyway, think about that for now.
**Daniel Dyla (Dynatrace)** 49:10 Yeah, I will. Okay.
**Josh Suereth** 49:12 That's been the back of my mind thing. I had a, you know those, like, you're doing something else, and you have insight, and you can't stop thinking about it? That's one of mine that I haven't fleshed out enough. I was just like, this seems like it has legs.
**Daniel Dyla (Dynatrace)** 49:27 Yeah, I'm just trying to think of a use case for it.
I'll… I'll give it some thought over the next week.
**Josh Suereth** 49:34 Okay.
I can give you use cases from our side if you're curious, but ….
**Daniel Dyla (Dynatrace)** 49:40 I am curious, just to, like, I'm curious…
Yes, I'll leave it at that, yes.
**Josh Suereth** 49:47 I'll give you one that's dead simple, okay? So, Google Cloud has a bunch of services. Let's say PubSub, right?
Let's say there's a service in PubSub that works on behalf of multiple different projects.
Okay, so that… maybe, like, a load balancer or something that is doing behavior on… on… on…
On account of a couple people.
**Daniel Dyla (Dynatrace)** 50:11 Okay.
**Josh Suereth** 50:11 Right? So what I want to do is I want to say, cool, grab the metric for this particular person's project, and I will record data for them, and I want it to be isolated from
The data for this other person.
**Daniel Dyla (Dynatrace)** 50:26 Okay.
**Josh Suereth** 50:27 But I'm using the same, you know, binary, because architecturally that makes sense, and it's more efficient for everybody.
**Daniel Dyla (Dynatrace)** 50:33 Yeah, I got it. I see what you're saying.
**Josh Suereth** 50:35 Even hypervisor.
**Daniel Dyla (Dynatrace)** 50:37 A similar use case would be…
And this, all the way back from the earliest days of OpenTelemetry, people always said, what if I have two services in the same process, and we always just said, set up a second SDK? Yes. But that was never great, because all of our APIs are set up to be… to have a global SDK. This would…
kind of invert that to say you only ever have one SDK. If you have a second service, you just would report it against a different service entity.
**Josh Suereth** 51:08 Yeah.
**Daniel Dyla (Dynatrace)** 51:10 Yeah, and I think…
And then you just have… that simplifies the overall API SDK model, too, to say you only ever have one.
It's global.
And… I… I think I like that better, too.
I mean, most of the time, that's what people are treating it as anyways.
**Josh Suereth** 51:29 Right, right. And what we're doing is we're divorcing the notion of the thing I'm reporting data against from my data pipeline.
**Daniel Dyla (Dynatrace)** 51:37 Those two services in the same process probably want the same data pipeline.
**Josh Suereth** 51:41 But they were putting data against two different things, right?
**Daniel Dyla (Dynatrace)** 51:44 Yeah.
**Josh Suereth** 51:46 So…
Alright, let's noodle on it. Maybe I'll be crazy and make a whole proposal on it, and just upend everything we're doing.
But I think it does not bend much, right? Because all of the… like, all the hard stuff we already have. We have an SDK, we have a merge algorithm, right? We know what that looks like, we know about this environment variable entity provider, we're gonna fix resource detection, we have that all sorted out. That's not under contention.
Yeah, no, the dynamic thing.
Yeah.
**Daniel Dyla (Dynatrace)** 52:15 Okay.
**Josh Suereth** 52:17 Awesome.
I'll see y'all next week. Thanks, everybody.
