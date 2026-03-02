SIG: Entities SIG
Date: 2025-10-06
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/ju78D3F68URyU1HLvnu6b_qtVg5LCIeKUaIjqC-cLG2IamF4XGc5cmO0YizgpF9f.9aBEzNZ0drrFxyyu
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:20 Hey!
**Dmitrii Anoshin** 00:23 Hi, Josh.
**Josh Suereth** 00:25 How's it going?
**Dmitrii Anoshin** 00:27 Doing well, how are you?
**Josh Suereth** 00:29 Busy, busy, trying to get caught up in things.
We, we had a vacation in New York City last weekend, and I always come back just dead tired.
**Dmitrii Anoshin** 00:41 I see. I actually had a vacation in New York City a couple weeks ago as well.
**Josh Suereth** 00:45 Nice, nice, yeah.
When you go to New York City, what do you do? That's the question.
**Dmitrii Anoshin** 00:56 It was a family trip, so we went to, like, just walking around, enjoying, like, Brooklyn Heights, Manhattan, and went to one of the Broadway shows, like, old restaurants, stuff like that.
**Josh Suereth** 01:12 Yeah.
**Dmitrii Anoshin** 01:12 And you?
**Josh Suereth** 01:13 That's what we do. We did… we did a Broadway show, we did a musical.
And we did,
We did a walking food tour that was just way too much food and not enough walking.
I don't know if you've ever dealt with this one, I gotta… I'm logging into,
Logging into GitHub here,
Okay.
Alright, cool. Apparently, my login had died.
Alright, I think we're good.
So I can open everything,
We have an hour today, and going forward. Thank you, everybody, for the time change. Sorry I didn't send it out earlier.
Yeah, and if you need a walking food tour recommendation, I can give you one that was actually pretty decent, just lots of food and not enough walking. So after the walking tour, you're gonna want to, like, walk all the way across Manhattan.
**Dmitrii Anoshin** 02:16 Okay. Yeah, we did a lot of work on this one.
Yeah. The opposite, not enough food. What a lot of food.
**Josh Suereth** 02:23 Yeah. Well, this was, this was supposed to be a walking, like, history and food tour, but it was, like, there was literally a restaurant every 10 minutes.
And so… which, I mean, I'm not gonna complain, it was really good, like, sampling of stuff, but it was, yeah,
Every time I think New York, I think you're walking at least a mile everywhere you go, even if you use the subway, you know?
**Dmitrii Anoshin** 02:49 Right.
**Josh Suereth** 02:50 Yeah, anyway, cool. Let's, let's get started.
We had a bunch of good discussions, just tons of good discussions last week, and there's a lot of open questions on the OTEP.
what I wanted to start with, if it's okay, Daniel, you and I were discussing the prototype in JavaScript. Do you want to raise your questions first?
**Daniel Dyla (Dynatrace)** 03:16 Yeah, let's see how well I can remember Friday. I was wondering why…
The, resource initializer has to…
handle, waiting for initialization and then notifying the rest of the SDK when a resource is initialized.
The way that the resource works in JavaScript right now is,
All of the detectors are synchronous.
**Josh Suereth** 03:49 Right.
**Daniel Dyla (Dynatrace)** 03:50 Individual attributes can be…
**Josh Suereth** 03:54 Promises or values.
**Daniel Dyla (Dynatrace)** 03:58 So it's on the exporter to await the… any unresolved attributes?
And we handle conflicts on a…
**Josh Suereth** 04:12 Hi.
**Daniel Dyla (Dynatrace)** 04:14 Configuration order, and then detection order, basis.
**Josh Suereth** 04:23 So.
**Daniel Dyla (Dynatrace)** 04:24 There's actually no need for something like the meter provider or tracer provider, or anything like that to know whether the resource is fully resolved or not.
Because at no point does it matter until you go to access one of the attributes, which could happen in a processor, or could happen, most likely, in an exporter.
**Josh Suereth** 04:49 So, you're assuming you know… All of the attributes in resource detection, then?
**Daniel Dyla (Dynatrace)** 04:56 What do you mean by that?
**Josh Suereth** 04:58 So, like, on GCP, if you're running in, like, a VM, you have to hit our metadata server, which is an HTTP call.
Which is asynchronous. We don't know what attributes we're gonna fill out until we make that call.
Because we don't actually know if you're running in GKE, if you're running in Cloud Run, if you're running in a VM, right? Until we make that call and check other things, we might not actually know the full set of attributes.
**Daniel Dyla (Dynatrace)** 05:28 Interesting. I… I guess I had not realized that.
**Josh Suereth** 05:33 I think what the team did today is they just give you all of them, even if they're not gonna fill them out.
**Daniel Dyla (Dynatrace)** 05:39 Yeah, so I think probably what we're doing, I would have to look, this is… I'm a little bit guessing… I call this an educated guess. I think what we're doing is using essentially the same promise for all of those values right now.
And we just assume that they'll be there. If they're not, they end up being null on resolution, and it doesn't matter.
**Josh Suereth** 06:02 Right, right.
**Daniel Dyla (Dynatrace)** 06:03 But if an attribute came along that we…
That came from the endpoint that we weren't specifically looking for, we would probably miss it.
**Josh Suereth** 06:13 Yeah.
Right, right, right. And this is where, like, the… when we move to entities, right, we won't know the entity type until that call resolves.
**Daniel Dyla (Dynatrace)** 06:24 Well, yes and no, because if you… you know what entity types are possible, you won't know whether it, you know, it may resolve as nothing.
But you know which entity types are possible. Though, what would not work would be, if…
You wanted to… Have the results of that call,
add arbitrary properties. Like, if you wanted descriptive properties that you weren't aware of in advance or something like that, then I guess that wouldn't work.
**Josh Suereth** 06:59 We do also have a mechanism for that, where you can make the entire resource.
**Daniel Dyla (Dynatrace)** 07:06 Like, the entire result of the resource detector asynchronous?
But that makes it…
It's essentially impossible to do conflict resolution until everything is resolved, which is why we moved away from that.
**Josh Suereth** 07:28 Yeah, that's interesting. So, that's not how the JavaScript prototype, or sorry, the Java prototype works at all.
Because in Java, you know, we can actually have threads and block and await and that sort of thing.
**Daniel Dyla (Dynatrace)** 07:41 Yeah, so this is not only the way the prototype works, this is the way the current production resource works as well. So that was why we did the prototype that way also.
**Josh Suereth** 07:50 Well, yeah, that makes sense, like, the… and again, Java right now…
Forces all resource detection to happen outside.
of, of the main thread, which means you actually block
the SDK starting up and the application start up until that, like, remote call is… it actually happens, which is a little… fun.
**Daniel Dyla (Dynatrace)** 08:14 What happens if you start a span in the meantime there, before that… resolves.
**Josh Suereth** 08:21 it's… it's held. That's also…
The most frequent request we hear from GCP users in OpenTelemetry is, can I get rid of the metadata server spans?
**Daniel Dyla (Dynatrace)** 08:32 Yeah, okay.
**Josh Suereth** 08:34 So, like, the SDK will, like, try to make the span, and I think there's kind of a weird…
There's some weird thing that's happening where it's kind of blocked and kind of successful.
I'd have to look at the details for how that worked, but I remember, like, when we first put our,
when we first created, like, OpenTelemetry resource detection, that was the most common ask, was how do I disable metadata server lookups for resource?
**Daniel Dyla (Dynatrace)** 09:03 Okay .
**Josh Suereth** 09:06 What I did now is we have,
Let me talk about failure scenarios I want to avoid. I don't want every single, you know, implementer to have to think hard about concurrency.
or the possibility of things not being fully resolved. I want it to be absolutely in their face that this is an asynchronous thing, that they interact with that API.
Or, it's completely handled on their behalf before it gets to them.
Right? So, an idea here, like, what you've done with JavaScript is you're returning stubs.
**Daniel Dyla (Dynatrace)** 09:40 So you return a resource stub that, when you interact with it, may or may not unbox into.
**Josh Suereth** 09:46 a concurrent thing.
And then you're making people who deal with the resource stub handle that, so most of the API is safe. When I have to finally unbox the package, it could blow up, it could do whatever. That's… that's fine. That's reasonable.
In Java, what we have is, we have this resource listener thing that we made for the previous one, where effectively, we can communicate resource changes if we need, but the rest of the SDK can start booting up and start accepting data.
And when it goes to first access a resource, when it first needs to actually grab one, there… then it finally hits the timeout block.
And the way that works is there's one central piece of code that will understand I'm going to try.
to grab this resource for n amount of time, but once that time window is gone.
I let resource go through, and I'm in an uninitialized resource state that I can communicate to downstream clients and say, yeah, here's what I know about my resource, but it's not done.
**Daniel Dyla (Dynatrace)** 10:49 Yeah, so we can't really do that in JS, because we can't block on the access. You would have to make that an asynchronous call, which would… and then you would await it, and that can't be done…
Because…
It's specified that the, on start, onEnd, and onEnding are all called synchronously with spans start and end.
So you can't have anything in the SDK that's… you essentially can't have any asynchronous methods along that path.
So everything has to be synchronous for that access. The first thing that you're allowed to decouple is…
The spam processor from the exporter.
Because, obviously, you have batching and stuff like that.
**Josh Suereth** 11:43 Yeah.
**Daniel Dyla (Dynatrace)** 11:45 So because it's all specified to be synchronous, and I think the reason for that is you want to be able to access
Like, the implicit context.
In processors, potentially.
Because it is required to be synchronous,
we have… all those calls to access the resource must be synchronous in JS. So that… this was our workaround to make those calls synchronous.
And it's… the only time that it might be a problem is on the very first
export. If you access resource properties in…
a span processor, they might be missing. So we have this Boolean function to ask, like, is this resolved or not? And then if it returns true, you know you can safely access them, and if it returns false, the processor can then decide what it wants to do. Does it want to await them? Does it want to, whatever,
But the first, like, required… Awake is on the… first export.
And then after that, Accessing it synchronously works as expected.
**Josh Suereth** 12:57 Right. I'm trying to think of, like, to rephrase what you're saying into principles. So, effectively, startup has to be synchronous. We need some way of synchronously starting up.
And, should not block for… Certainly.
Types of, entity lookup, for example, hitting GCP metadata, server, or any remote.
API… Like Keats.
**Daniel Dyla (Dynatrace)** 13:32 It's okay if we have other SDKs that do block, or have a blocking mode or something like that, but we need to be aware of the fact that.
**Josh Suereth** 13:41 Oh.
**Daniel Dyla (Dynatrace)** 13:42 JS will not be alone here, but there are certain places where we just cannot block.
**Josh Suereth** 13:47 Well, that's kind of what I mean. Like, if we're gonna make a specification, it has to work for all languages, so we can't write a specification that doesn't allow JS to work. That's just not an option. Apologies, I'm gonna eat some lunch while we talk.
**Daniel Dyla (Dynatrace)** 13:58 Go forth.
**Josh Suereth** 13:59 So, the next… so I'm just trying to figure out, like, principles from this. So, first of all.
Needs, needs to allow.
Synchronous startup.
Specification.
Cool. The other thing is, we want uninitialized async should not bleed.
across the entire SDK.
We want the first time, we need to understand, async startup.
is… Export?
This is the other weird one, or interaction.
With the resource via,
Samplers are what have access to resources, and processors, or both. It might be both.
**Daniel Dyla (Dynatrace)** 14:50 I think… Both of them?
At least processors do. I don't know if samplers do.
**Josh Suereth** 15:02 Sampler has changed recently, but, yeah, I think they were more highly limited back in the day, but I'm not… I'm not sure what they have access to at this point.
We'll have to take a look again.
Okay, does this, does this principle make sense?
**Daniel Dyla (Dynatrace)** 15:20 Yep.
**Josh Suereth** 15:24 Alright, cool.
I'm gonna leave those two principles as the resolution of this, of like, now we know the design space, right? We need to make sure that these two things are true.
The next comment I wanted to talk through was, resource with entity versus instrumentation scope.
with entity. And I think this is one that, David Ashbel had a proposal.
That I like, and I think that there's concerns that Dimitri had that I think are viable here. So this is basically… the current proposal is instrumentation scope will have entities in it.
And there's some sort of correlation between resource entity and instrumentation scope entity, so…
The proposal, as is, is basically, resource entities are the identity of the SDK, or the thing doing the observing.
And then entities in instrumentation scope are the thing I am… I'm observing something else, or something within the scope of the SDK, right? And that identity can change.
There's concerns here that, basically, the cost of entity and resource in the collector is already somewhat high and awkward.
And adding it in scope will make it even higher and more awkward.
Especially if we have to deal with conflicts. I think the modeling question's the big one. You know, can I have a resource that has the same entity as instrumentation scope? They're different levels, so naturally you could, unless we say this is broken, like, a broken modeling thing.
And there's… there were a bunch of questions about that, like, how do we know whether they would be the same, right? Could it be that one process is monitoring another process, and that'd be fine?
So those are kind of the issues that were raised. Go ahead, Dimitri.
**Dmitrii Anoshin** 17:04 I just want to add something. It's not only modeling, like, usability problem, it's also we're trying to do it to avoid breaking changes, but if we go that approach, we would have to
push a lot of existing attributes from resource to instrumentation… to instrumentation scope otherwise. And that's gonna be maybe even…
bigger break and change for the users, right? Because they, currently, they… Expect…
all of the attributes for entities, whether it's internal or, like, as you said, outside, something that SDK is observing, they…
are expected to be on the resource right now. And, like, instrumentation scope attributes, I believe, as of today, they serve pretty different purpose, right?
And if we're moving entities to…
Instrumentation scope, we would have to move all the attributes as well.
**Josh Suereth** 18:08 Yeah, I hear you in terms of breaking, like, that… it becomes hugely breaking. So, let me, let me show the alternative.
The alternative is, basically, SDK has a core resource.
Right, so if I do meterprovider.get whatever, Uses Core Resource.
Okay?
You can add layer.
additional resource information.
on the SDK. So I could say, meter provider, dot 4, entity.get.
Layers a specific entity.
on resource. Now, the way I've been visualizing this in my head, and this is actually… this almost exactly matches how I was implementing things.
God, I hope if I make a drawing, this doesn't make loading our notes super horrible.
But effectively, we have this thing where, generally for the SDK, We have the main resource.
Right? And then underneath this resource, we have data storage where we're tracking
let's… I… I'm thinking about metrics here, by the way, so I guess we don't really need this for the other ones, because we're using queues, but anyway. We have resource, and we have, you know, metric storage.
And then the idea would be when I grab a new… meter provider.
I basically have a resource diff here, or a resource diff, like, you know.
added ET1, and then I have… I actually construct a new metric storage.
here.
And so, when I'm reporting data.
This is the SDK itself.
Oh, God.
I forgot how annoying all this can be. The SDK itself, right, would be reporting all of the metrics across all the resources that have been constructed.
But, a specific meter provider would be for either the resource or, you know, sub-things underneath it. So if I were to call, you know, meter provi- oh, let's move to back…
let's say I, you know, add a different entity, added entity.
Two, I would literally be constructing new metric storage for this new entity that the SDK is responsible for. This is the primary thing that we need
Out of this, the, like, multi-tenancy aspect of this, right?
is the fact that we can have different metric storage and different entities. But the idea would be this metric storage would take Entity 1 and add it to resource and report the whole thing in a big blob.
So the resource is kind of, like…
You know, expanded with additional scope.
This is defense, or am I doing this poorly?
**Daniel Dyla (Dynatrace)** 21:26 This is not that different to what your draft proposal was, except that instead of putting it on the instrumentation scope, you just merge it with a resource, and you report multiple resources, right?
**Josh Suereth** 21:36 Exactly. That's the only bill.
**Daniel Dyla (Dynatrace)** 21:38 is identical, and I think the SDK implementation is nearly identical, because you need the same… in terms of, like, the metric storage and stuff, you would need to do the same thing anyway.
**Josh Suereth** 21:48 Yep, yep, exactly. And then, if you do this for entity on, say, a tracer provider, because those are already pipelines, the only… we can do this, like, here, we could do…
We could have separate pipelines.
To make it easier. So there'd be a, you know, Expand pipeline?
to make it easier to bundle the data, so you can actually look at the pipeline separately, but I actually don't think that's needed.
I actually think you could have one span pipeline for all the resources you're reporting, and be okay with the way we've defined things, as long as when I call… when I call start span, right.
There is a resource I can grab that's fully constructed.
**Dmitrii Anoshin** 22:46 It sounds reasonable to me.
**Josh Suereth** 22:48 Okay.
If it does, I will work on the prototype for this.
**Dmitrii Anoshin** 22:56 Go ahead. Just to clarify, it doesn't change the data model in any way, right?
**Josh Suereth** 23:00 No, no, we won't have to change the OTLP data model then.
**Dmitrii Anoshin** 23:03 Yeah, and…
**Josh Suereth** 23:04 Every data model's exactly the same.
**Dmitrii Anoshin** 23:05 all of the resources emitted by the SDK will be, like, independent, essentially. They will have all of the attributes and all of the entities.
**Josh Suereth** 23:15 Yeah, yeah, so this would, I can add that here to make sure we would report.
**Dmitrii Anoshin** 23:20 3 resources in every export.
**Josh Suereth** 23:24 Yep.
**Dmitrii Anoshin** 23:25 That's great.
**Josh Suereth** 23:28 Okay, yeah, because I think I actually, like, the more that you guys were raising concerns and things.
There's a part of me that still likes instrumentation scope as being cleaner, but I'd rather have this work and not break people.
**Daniel Dyla (Dynatrace)** 23:43 No, that is my cat. Apologies. Okay, you're making me… I was like, what is happening in here?
**Josh Suereth** 23:49 Yeah, we were gone for the weekend, so she just wants tons of attention, it's kind of crazy.
**Daniel Dyla (Dynatrace)** 23:55 Yeah, no worries.
**Josh Suereth** 23:58 I can mute my microphone when I'm not talking, if it helps not…
Okay, I… but thinking more about it, I actually think this is probably the way to go.
**Daniel Dyla (Dynatrace)** 24:10 I mean, it's no… the proposal is essentially unchanged, it's just where do you put the entities?
**Josh Suereth** 24:17 Yeah, well, it gets rid of all the scope stuff. The main crux of the proposal is unchanged, from an SDK standpoint. We still have a way of tracking entity and grabbing, you know, providers for it.
**Daniel Dyla (Dynatrace)** 24:29 Yeah.
I guess my… Biggest complaint with this is still…
Probably my biggest complaint from before.
Which is that in your current proposal, you have,
Like, you, you… that 4-entity call, must not be one that's on the core resource.
And I don't know if you're writing in instrumentation, how you could…
guarantee that. Like, how do you know, if I'm writing an interpretation for, like, some HTTP library, and I want to represent the API as an entity, when I get a meter provider for that entity, how do I know that it's not already on the core resource? Like, how could I possibly follow that?
Mandates.
**Josh Suereth** 25:20 So actually, with this one, I don't think we need that restriction anymore, because if we keep all the entities in resource, when we flatten out.
the resource, we can actually have conflict resolution at that point in time.
So I'm, like, less concerned about it here. My main concern was, I… I… until I knew better, I wanted to prevent the same entity being in a resource and instrumentation scope at the same time.
**Daniel Dyla (Dynatrace)** 25:44 Okay.
**Josh Suereth** 25:45 But, since we're changing the resource.
it's… it would be a conflict, right? So we would have to remove it from the resource, which I think gives us a clear definition of what to do and how to resolve it.
Okay. So, yeah, I'm actually fine completely lifting that restriction with this… with this shift.
I don't know how other people feel, but yeah. Like, a lot of these open questions are about…
**Daniel Dyla (Dynatrace)** 26:19 The problems that start to show up if you have resource with entity and instrumentation scope with entity, and what that means as a data modeling perspective.
**Josh Suereth** 26:26 If we don't allow that, we already have the answer to most of those, from the work we've done the past year.
**Daniel Dyla (Dynatrace)** 26:35 Are we saying the core resource is immutable?
**Josh Suereth** 26:40 I think we can allow the core resource to remain immutable right now in the SDK, yes?
with this change.
Like, I think this gives us a path forward for that.
So, like, we would recommend for the client side's sake, for example, that, yeah, browser.
Don't put it in the core resource, because you know it's gonna change. Call, you know, get with the new browser session, and then report data against that meter provider.
**Daniel Dyla (Dynatrace)** 27:11 And then, would we…
would… and I guess we're… maybe it's too far down the path. If the… if the session ends or is changed, and they need a new…
entity, would they then just call meter provider git
you know, git meter again with just a different entity, and we'll have to have some lifetime APIs.
**Josh Suereth** 27:35 Yes, I think that's the next open question here, is, Lifetime APIs.
Yeah, that's the theory. That was the theory behind the thing. The original thing as well, with Interpretation scope, we still would need lifetime APIs.
**Daniel Dyla (Dynatrace)** 27:53 Yeah, yeah, we were gonna need it anyway.
**Josh Suereth** 27:55 Yeah, if you look at all of the complaints from, like, Apache Pulsar and folks who are doing kind of this, like, multi-entity reporting shenanigans,
Lifetime for metrics is something we really have to consider, given that, like, spans and traces and things are…
sorry, traces and logs, I should say, are all just queues.
That journal through.
We don't need as much of a lifetime
For those, because you're not storing data in the long run.
**Daniel Dyla (Dynatrace)** 28:25 Yeah.
Right now, Metrics is our only stateful, pipeline.
I guess a spam processor still counts as state, but… .
**Josh Suereth** 28:36 Yeah. In terms of, like, the SDK internal.
**Daniel Dyla (Dynatrace)** 28:38 The… the metrics is the only…
SDK that requires state, and I expect that to remain true for the foreseeable future.
**Josh Suereth** 28:50 Yes. Yeah, I think… well, that's partly the design of metrics. If they didn't do state, they wouldn't be worth it.
**Daniel Dyla (Dynatrace)** 28:57 Right, because you would just have events.
**Josh Suereth** 28:59 Yeah, yeah.
Oh my god, Kat, don't unplug me. Okay.
Sorry.
Okay, I think she left, so you won't hear as much meowing.
**Daniel Dyla (Dynatrace)** 29:08 That's fine, I just thought my cat was trying to get into my office, and when I went to open the door, she wasn't out there.
**Josh Suereth** 29:15 Oh, yeah, if I had my door closed, then she will claw at it, which is… which is dangerous, and, you know, anyway. Okay, lifetime APIs. So, should we go through the OTEP and start looking at some of the more specific concerns? Like, we have a direction forward now with this alternative, which I think everyone's comfortable with.
Yeah, what's that? By the way, remember to add your name to attendees.
Let's start looking through the comments, because I think a bunch came in that I wasn't able to get through previously, and I want to make sure we're kind of addressing everything.
Alright, so…
Yeah, we talked about blocking, In the order provided, refer to the textures list parameter, yeah.
That's a good one. Should we include transform processor? Yeah, I think they understand the context there of what is impacted.
Describe connections between scopes. For instance, the intended scope is a continuous session XYZ. This has to do our pipeline can run task.
Yeah, this is… well, we can address this later, I think. We'll have to move the… what to do with scope as a future thing.
To reobtain… This was just answering the question.
This is answering what we mean by tenant.
This was David's proposal, which we just discussed and we're gonna move towards. Let me make a comment.
I discussed this in… Entity C… 22… destruction.
Thanks for that suggestion.
Okay.
And then…
These were open questions about why do we have to have a data model change? Can we just emit multiple resources? So this was the pros and cons, and Dimitri, you already had this comment, so again, I'll resolve this once we update the spec to match the current thinking.
**Dmitrii Anoshin** 31:26 That's good. Thank you.
**Josh Suereth** 31:27 This one, I think I eventually did fix. Nathan, thanks for raising that.
**Daniel Dyla (Dynatrace)** 31:34 I don't think it's fair.
**Josh Suereth** 31:35 It's not fixed?
**Daniel Dyla (Dynatrace)** 31:37 Oh, it doesn't say outdated, and it just says instrumentation scope lose, that's the whole line.
**Josh Suereth** 31:44 Okay, alright. I think I fixed it locally and maybe didn't push. Apologies, it was,
I was trying to get out the door last week. Alright, let's go…
This, this we talked about, this one won't matter because we're not changing how we model things, so we can cut that one out.
**Daniel Dyla (Dynatrace)** 32:05 I think we still have to answer the question, because people will want to… they'll ask…
when do I add an entity to the core resource, and when do I do it in an instrumentation? And…
We'll have to settle on terminology for, like, how the…
entity… even though they're merged into one resource, for the API documentation, we'll have to settle on terminology for how those are related.
**Josh Suereth** 32:34 Yeah, I do think we want to do a thing where it's basically,
for an entity which, outlit… or, sorry, has a different lifespan than the SDK,
that's when you would use this, and that's the terminology I want to continue to use, right?
**Daniel Dyla (Dynatrace)** 32:51 Yeah, okay.
**Josh Suereth** 32:52 So, the entity has a shorter lifespan than the SDK, and I expect a different identity to show up.
We need… we need someone to turn that into human language.
Okay.
It looks like, I think…
Oh, also, just the notion of what is implied by… what's the implied relationship of entities on a resource in general is something we need an answer to, or we need a way to phrase it.
So, I think your point still holds, but it held, like, prior to the OTEP.
Okay.
**Daniel Dyla (Dynatrace)** 33:31 I think so.
**Josh Suereth** 33:32 Cool. Alright, I think with those two major decisions, that… that gives us an answer to everything except this.
And let me add… The APIs.
Subprovider.
That's good.
To-dos.
Relationship.
Applied… oops.
Lots of entities on a resource.
Okay, cool.
**Daniel Dyla (Dynatrace)** 34:15 We actually potentially already have lifetime APIs.
**Josh Suereth** 34:20 I was thinking about that, don't we have a close on meter provider?
**Daniel Dyla (Dynatrace)** 34:23 It was shut down, yeah. In JS, we called it shutdown, but it essentially flushes the SDK, you know, metrics, and then makes it so you can't
You can't write to it again.
But if you're creating a new meter provider with a new storage, you could shut down a meter… or creating a new meter with a new storage. You could shut down a meter.
And then just create a new one, like, I don't think there's any… problem there.
**Josh Suereth** 35:01 Yeah, absolutely, okay.
Interesting.
**Daniel Dyla (Dynatrace)** 35:04 watches, and then you can't… I guess this is… you're looking at meter providers shutdown?
Yeah.
Which implies that there is a meter shutdown. I don't know if meter shutdown is actually specified anywhere.
If you shut down your meter provider, you shut down all the child meters as well.
**Josh Suereth** 35:24 Well, remember that the proposal for GET entity is on meter provider. So meter provider will have a, like.4Entity, or .git
with an entity to, like, grab a new meter provider that you would then get submeters.
**Daniel Dyla (Dynatrace)** 35:40 provider. Okay, I thought it was, like, git meter4, I thought that was the way we were…
**Josh Suereth** 35:46 No, that's what we were doing with Instrumentation Scope, but if you read David Ashpole's comment, and I think Tyler's here, so he might be able to confirm this, in Go.
They often give a meter provider to instrumentation, not a meter.
And I think that might be true in some Java things, and so giving a meter provider actually gives us way more flexibility in terms of making sure this can be used with existing instrumentation.
**Daniel Dyla (Dynatrace)** 36:09 Okay.
**Josh Suereth** 36:09 Yes.
So…
Okay, and I think, let's take a look, quick look at, like, Trace. I think Trace also has shut down, and…
Because that's the oldest one, yep, trace has shut down, and then I believe logs will have to have shut down if the other two do.
Yep.
So, we will have to change this spec to talk about, sub-providers and what happens on shutdown.
Ed, but I think that's fine.
Cool. Let's move on.
I think…
we have this relationship. Does anyone else have anything else they want to… does anyone else have a topic before we move on?
Okay, let's go to our… Project board, quick.
Alright.
So, we have a… Four things here.
That are in progress, let's just check on them. Environment variables to provide keys, container, and pod name. I think this…
Dimitri, we merged your spec, right? We just need to implement this in SDKs to use it? Is that fair?
**Dmitrii Anoshin** 37:51 I'm not aware of this particular issue, to be honest. We merged the one to provide, like, entities as environmental variable definitions.
Pacific.
**Daniel Dyla (Dynatrace)** 38:03 You…
**Josh Suereth** 38:03 I think… I think this… you…
**Daniel Dyla (Dynatrace)** 38:07 You could provide whatever you want that way, including Kate's container and pod names.
**Josh Suereth** 38:12 Yeah.
**Dmitrii Anoshin** 38:13 It may be that this issue was mentioned in my PR, and that's how it went here.
**Josh Suereth** 38:20 Right, this one I attached to the other one, so that's why it's kind of assigned. So, I think you actually completed most of what we need here. The Cates semantic invention group is making the Cates entities, so then all we need to do is actually be able to parse this environment variable.
**Dmitrii Anoshin** 38:37 Okay.
**Josh Suereth** 38:37 And then I think we're good to go.
**Dmitrii Anoshin** 38:44 I can double-check on this one, because I'm part of the greatest semantic convention.
Group as well, so…
**Josh Suereth** 38:50 Okay. From an entity standpoint, I'm gonna mark this as done, even though, there's still more work to do for it, though, because I think
the work that you did on the end variable is… is all that we needed to finish to be able to close that out. After we get… like, that was… that was the reason we were working on it, but you… you did, like, the key work there.
**Dmitrii Anoshin** 39:13 If you move it to done, it doesn't close the issue, right?
Got it. Cool.
**Josh Suereth** 39:18 No, because it can be on multiple project boards, right? So, like, we're kind of playing pass between SIGs here.
**Dmitrii Anoshin** 39:25 Awesome.
**Josh Suereth** 39:26 Yeah, okay. Add support for new resource entity references proto-Message in the collector. How's that been going?
**Dmitrii Anoshin** 39:34 The protomessage… actually, yeah, this is, like, a bigger issue, like, with everything, all the support, etc. So I… I'll have more time to work on this, this week and next week, so I'll take more progress.
And given that we resolved the issue with resource versus instrumentation scope, that was kind of… I was uncertain about, that's why I didn't take any progress here.
**Josh Suereth** 40:04 Oh, that makes sense, especially if you're changing the transform processor, yeah.
Cool. Alright, so that's still in progress,
Entity contradiction between resource and entity attributes. This is marked to Daniel. What's going on here?
Oh, complex attributes, right?
**Daniel Dyla (Dynatrace)** 40:21 Yeah…
I think that this was essentially resolved. This was a story more about following the complex attribute OTEP,
I think the end result was complex attributes are technically allowed everywhere, but they're discouraged in places where they would affect metric identity.
And I think at this point.
there's no… there's no point in us, like, that will not be a decision that's changed or reversed or anything like that at this point. I think there's no point in us keeping this open.
**Josh Suereth** 40:56 Alright, do you mind making a comment to that effect of, like.
We have to allow complex attributes, and we'll just discourage them for identity.
**Daniel Dyla (Dynatrace)** 41:06 Yeah, yeah.
**Josh Suereth** 41:07 Okay. Alright.
That sounds good.
And then, as you know, the entity prototype for SDK specification is… this is the Java one. That's the one that I've been working on. I think we need to add some more. Alright, so let's move on to…
resource entity mapping to-dos. Decide how entities should be supported by schema files. This is about transformations.
I'm… I'm okay, given that we're kind of reformatting the entire schema file.
In part of some kind of tooling.
to use automatic diffs that are calculated from Weaver, I'm okay kind of continuing to defer to this one.
Alright, resource entity merge logic prevents fine-grained detectors. This was a Go-specific issue.
that I think, Dimitri, you were gonna look at because you had time, but given that I don't think you have time anymore, do you mind if I unassign you from this?
**Dmitrii Anoshin** 42:05 Yeah, pretty pleased.
**Josh Suereth** 42:06 Okay.
This is when Tyler's here, and you probably don't have time.
Tyler, this is… we're trying to figure out how to prototype entities for the Go SDK. We want to have a full Go SDK prototype before we start pushing, like, major spec changes, just because I think it will be somewhat…
exciting, and we don't want to have Go be, like, the last thing here, like has happened in other SIGs. So, is this something you might have time to help us out with?
**Tyler Yahn** 42:38 I mean, I don't have time to do this prototype. I'm happy to review it. Like, in the past, like, Tigran's prototype, I remember helping review that. I can do something on that level, but, no, like, onboarding the whole idea and then trying to build the prototype would be something I'm not able to do.
**Josh Suereth** 42:56 That's fine. One question I have, because I ended up doing this for the Java SDK, was we ended up…
We have two ways forward with the prototype. One is, we could actually start having, entity detection be a completely new path in the SDK, and so if you're doing the programmatic configuration with the old APIs, that's considered deprecated, and you move to the new ones.
What Tigrin wanted to do was completely reuse all of the old instantiation code 100%, so that if you were… if you had, like, you know, programmatic configuration of what resource detectors you wanted, it would work with entities.
**Tyler Yahn** 43:36 Yeah.
And so the idea is that, like, you wouldn't specify an entity when you created a provider?
**Josh Suereth** 43:45 Yeah, like, that's what this is showing right now, is basically, if we wanted to allow the existing Go thing to work, we have to find a way to reconstruct an entity after all the individual attribute detection has happened.
**Tyler Yahn** 43:59 Hmm.
**Josh Suereth** 44:00 Which is a little bit exciting.
**Tyler Yahn** 44:05 Yeah, I'd have to… I'd have to look more into it, to be honest. It's also, like, you have this concept of a detector there. I think that's partially not, like, representative of a resource, though. Like, a detector was the thing that, like.
Eventually determines the resource.
**Josh Suereth** 44:21 Yes.
Yeah, so the config sig actually has those, right? Where there's resource detectors that are by name. We want those to actually be some kind of an interface that people can implement and pass in.
Or, or a, a thunk, or what do you, what do you call them in Go? A function definition? Function type?
**Tyler Yahn** 44:40 Yeah.
**Josh Suereth** 44:41 Whatever it is, it's something that people can, like, create and register.
**Tyler Yahn** 44:47 Yeah, I mean, again, I'd have to, like.
get onboarded on all of this stuff before I was able to even start, so I'm happy to review. Is Tigran not working on this anymore?
**Josh Suereth** 44:57 No, no, he took a step back.
**Tyler Yahn** 45:00 Okay. What's your timeline on this?
**Josh Suereth** 45:05 We want to actually have the specification landed by end of the year.
If you… like, I'm actually happy to make some Go prototypes, if that… if you're amenable to my Go code. I apologize in advance for it.
**Tyler Yahn** 45:21 No, that's… there's nothing… I… yeah.
I mean, like, I… yeah, like, syntax-wise, like, I think that's more important, because it's all about more, I think, just showing compatibility and understanding the deals there, because, like, the resource is kind of a…
A thorn, to try to do.
**Josh Suereth** 45:37 Yeah, and resource today, you guys rely on comparison capabilities of resource, right? Do you explicitly define the comparison operation yet?
**Tyler Yahn** 45:47 We do, but that doesn't actually matter, because it was comparable when it was released to stable, and it needs to remain that way using the default built-in operator of, double equals.
**Josh Suereth** 46:01 I see, and you can't override that if it was comparable.
**Tyler Yahn** 46:04 Correct.
**Josh Suereth** 46:05 Okay.
And it's used everywhere.
**Tyler Yahn** 46:09 I mean, I… that actually isn't… like, I don't know, firsthand what the usage, but for our compatibility guarantees, like, code won't compile if you don't provide it, and that would break our versioning stability guarantees.
**Josh Suereth** 46:24 You have to provide the default out-of-the-box comparison, or I can provide my own, and then it's fine?
**Tyler Yahn** 46:29 No, so the thing is, is like, actually, the comparison can be incorrect. That actually doesn't matter. So that was something I think that Tigran kind of realized, because you can do comparison of, like, pointers, right? Because pointer values are comparable, yet the value itself
Doesn't really mean much, because it doesn't mean it's actually pointing at the same thing or not.
Yeah. It's just that it… that would compile, and that would meet our compatibility guarantees, and, like, we have it documented, you should use the equals method anyways, so that's all good. If you go and you add, like, a map to the resource, that'll stop compiling, and that would break our compatibility guarantees.
Because a map is not a comparable type. And so, like, that's, I think, where we're at a hard no on that one.
**Josh Suereth** 47:12 I see. So, what can we put in resource? We can put in, like, an array?
**Tyler Yahn** 47:17 Yeah, but I doubt you were talking about an array array. Array being a fixed-sized array, sure. An array being a slice, no.
**Josh Suereth** 47:28 Okay.
How are you doing key values in it today?
**Tyler Yahn** 47:32 Like you have there with a set. A set is immutable, though, yeah.
**Josh Suereth** 47:38 We can probably do something similar. Okay, alright, cool. We'll figure out what we can do here, but I'm… if nobody else has the ability to jump on this, I'll take that and kind of work through that. That's a thing we want to do, and I'm going to put that in the in progress, because we need…
we kind of need some of these prototypes for the… we need the Java prototype, JavaScript, and go are kind of the three we really want to target before we get the specifications starting to land in the OTEP thrum.
I… Okay.
**Tyler Yahn** 48:10 So just to clarify, like, I might have more time, like, after KubeCon, but that's.
**Josh Suereth** 48:16 Yeah, that's a…
**Tyler Yahn** 48:17 That's a maybe, and that's a ways away, so I didn't want to, like, hold up on this, so, yeah.
**Josh Suereth** 48:21 No, no, no, yeah. I mean, right now, we just need as many… as much help as we can get, but we'll make progress with what we can.
**Tyler Yahn** 48:27 Okay.
**Josh Suereth** 48:30 Okay.
**Dmitrii Anoshin** 48:32 Here, before we go forward. Like, sometimes, like, SDKs accumulate too many changed things, too many deprecated things that they want to get rid of.
**Josh Suereth** 48:44 And close to releasing a new version, like.
**Dmitrii Anoshin** 48:48 V2 in this example. So I'm curious, is that the case for Go? Because if that's the case, we might…
want to provide, like, more intuitive API for entities?
**Tyler Yahn** 49:02 We don't have any plan to release a V2 SDK.
**Dmitrii Anoshin** 49:06 Just, just checking.
**Tyler Yahn** 49:06 Thank you.
**Josh Suereth** 49:09 You… we… we should probably talk about that, cause there's a… Yeah.
It might be worth it at some point.
**Tyler Yahn** 49:18 To…
**Josh Suereth** 49:19 Remember how hard it is for Go.
**Tyler Yahn** 49:21 A V2 SDK is not impossible.
But… I think there'd have to be some pretty good, compelling reasons for it.
**Josh Suereth** 49:35 Okay.
**Tyler Yahn** 49:36 Yeah. The API is kind of a non-starter there.
**Josh Suereth** 49:39 But…
**Tyler Yahn** 49:40 Yeah.
**Daniel Dyla (Dynatrace)** 49:41 I think as an overall project, 2.0 APIs are still not allowed in anyways. I'm curious…
is the 2.0 SDK…
challenge more of a community challenge, or would it be difficult to make it compatible with the 1.0 SDK? Or API, I mean.
**Tyler Yahn** 50:05 No, the compatibility,
I… that… there's very little doubt that we could do that, like, that just sounds like… I don't even know if there's a challenge, let alone, like, an engineering challenge to something we can solve there. It's more just about, like.
kind of like what Dimitri just said, like, there's sometimes, like, a bunch of cruft. Like, there's no cruft right now. Like, there's nothing that, like, stands out in the SDK design that, like.
we would change in a V2. You know, I think that, like, if this entity thing could be resolved in this manner, then…
yeah, I think we would want to continue doing that. I don't, like, see trying to resolve entities as being the main reason we'd want to go with the V2, if that makes sense.
**Josh Suereth** 50:49 Okay.
I look forward to working with you on that, we'll see how we go. Alright.
Let's move on to the, the next, the next issue in our, in our to-dos. We have clarify requirements to meet before NTREF is added to resource. We actually did add it to resource.
So, we didn't mark it. Well, I mean, we haven't stabilized it, so I was going to use this for stabilizing. Okay. We want to check payload size increase, which I think we haven't done on, like, real data.
We've done it on fake data, but not real data.
If you will.
**Dmitrii Anoshin** 51:24 I don't even know why that would be a problem, because…
What's the increase here? It's pretty insignificant, I think.
**Josh Suereth** 51:33 Yeah, there's this one about the Go prototype and resolving it,
Which I honestly think that we… we have…
I think we have enough options with a path forward here that we'll be fine.
And this notion that entity reps break compatibility, I think we can fix it, you just have to write the Go code we have to write might be exciting.
And I think that's fine.
Names of the fields to be confirmed, I think we did confirm them.
I think I want to mark this as complete.
**Dmitrii Anoshin** 52:05 I believe so, yeah. It was a prerequisite for releasing data modeling video.
**Josh Suereth** 52:27 Check them off. Okay.
Cool.
That one we can close.
Alright, we already talked about that. Collector processors differentiate between remote versus local. Is this one still needed to be done in our current phase here?
**Dmitrii Anoshin** 52:46 Yeah, this is needed to be done. It's not required, but… and I will get back to this once I… once I'll be prototyping and making more changes to the collector, specifically in resource detection processor.
**Josh Suereth** 52:58 Okay. Let me know if you want it to be an issue to track it better.
**Dmitrii Anoshin** 53:01 Let's convert it to the ish.
**Josh Suereth** 53:03 Converted to issue? Okay. What do you want it on? Specification or collector?
**Dmitrii Anoshin** 53:12 I don't know, to be honest, maybe specification?
Because it'll be, like, it's not only a collector, right? Do we want to have the same differentiation in the, in the SDKs in that case, and, like, maybe some, some, like, uniform way to specify the entities?
**Josh Suereth** 53:32 It'd be better if it's generic, yeah. I'll keep it in specification, then.
And we need to put some labels on this, so this is, has sponsor.
Otherwise, it comes to us, and then we want entity…
Why are we not an area?
Huh.
Okay.
Cool.
Alright, so that is now officially an issue to track.
And… I'm gonna leave it there until you, have a chance to start on it. The site of service and services are different entities,
This, I can actually defer to the, the new SIG that is on service. So I'm going to convert this to an issue on semantic conventions.
And then I am going to move this to the, service sig.
And.
**Dmitrii Anoshin** 54:38 Are you sponsoring that SIG as well?
**Josh Suereth** 54:41 I am sponsoring that SIG, yeah.
It's not ready with SIG, locked by entity SIG. We haven't updated all our labels yet, but I am sponsoring it. I'll make sure that that gets triaged to the right spot, and I will probably help, solve it that. Okay.
Last one, communicate breaking change and specification around resource allowing non-immutable attributes. We are still going to be allowing non-immutable attributes with the new design.
So this actually still needs to happen. My thinking is, after the OTEP gets merged with the change, then we'll have to tackle this.
We're figuring out how to communicate it. Is that fair?
**Dmitrii Anoshin** 55:24 Sounds good.
**Josh Suereth** 55:26 Okay.
Cool, so we're back into prototyping, which is good, so we have a bunch of prototyping stuff to do. The entity manager OTEP, I might actually start
dropping some of these or change it, but the SDK startup specification
Right. This one I'm gonna move to active, because this is part of the current OTEP.
strategy around for asynchronous resources and entities. This one, actually…
Daniel, can I assign this to you, since we're working on this with the current OTEP, and
Yeah. Yeah, okay.
Cool. And then I'm gonna move that to active as well.
And we have…
Adding resource attributes post-creation via auto-discovery, that's a to-do. Okay, I think we can almost close out most of this.
This is… this prototype is also in progress.
And exporting data shut down, particularly the browser, that one we still have to do. Okay. Cool. I think we can eventually close Phase 1B, since we're changing around what the OTEP is and what it means, and great. Last thing is, on track.
We have a release date of 25th, or sorry, 2025-12-31, which would be end of the year for getting… landing our spec changes. I actually would like to land more than our spec changes when… for this date, so I'm happy if we push the date back.
How do we feel, though?
The amount of work we just walked through.
**Daniel Dyla (Dynatrace)** 57:08 For the end of the year, I…
I think just to get it specified is maybe reasonable.
**Josh Suereth** 57:17 Okay.
**Daniel Dyla (Dynatrace)** 57:19 I'm between on track and at-risk in my own head.
**Josh Suereth** 57:49 Alright, I'll… I'm gonna be conservative, and we're gonna put at risk.
Okay. Sound good?
**Dmitrii Anoshin** 57:59 Sounds good.
**Josh Suereth** 58:00 I know that people hate doing that, but I think it's totally… I'd rather be right and have people freak out than be wrong and have people expect something that never shows up.
Cool.
Alright.
Thanks, everybody. Hey, this is the first time we had enough time for me to update the status like I want to every week. So…
Winning!
**Daniel Dyla (Dynatrace)** 58:25 I almost said something after our first topic, we were 38 minutes in. I almost said something about not getting cut off halfway through a topic.
**Josh Suereth** 58:33 It was nice to actually make some decisions for once, yeah. Agreed. Agreed. Well, now that we're not trying to conflict with the entire ecosystems
every meeting should be on Thursday decisions. I think… I think we're… we're in better shape, but… I still… not… I kid you not, I used to have 3 meetings I wanted to attend Thursday during the entity sig, right?
I still have 3 meetings I want to attend at that same time slot.
So, you know…
Apparently Thursday's a big meeting day, I don't know. Thank you, everybody, have a great day, and yeah, excited to work on these prototypes.
**Dmitrii Anoshin** 59:09 Perfect.
