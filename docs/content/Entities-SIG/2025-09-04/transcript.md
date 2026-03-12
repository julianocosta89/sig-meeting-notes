SIG: Entities SIG
Date: 2025-09-04
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/OY1yhxOZ8IniAYKeNWS8D9A40ptpTBquuhs7IHSjUyTNAvNUScU1LqwHdv_8-QR9.kIgOVG4iMFiDsURT
============================================================

## Zoom Recording Transcript

**Josh Suereth** 03:14 Hey folks, sorry. We were, the previous SIG ran a little late.
Alright, looks like the agenda needs to get updated, I'll work on that now.
While I do that, does anyone have any topics that they wanted to raise?
**Dmitrii Anoshin** 03:47 I addressed that comments on the PR for the specification, so maybe we can talk about that.
**Josh Suereth** 03:56 Awesome.
Alright, I'll put that as first agenda.
Okay.
Let me start sharing my screen, because it'll take a while before my Chrome to catch up anyway.
Okay.
Do you want to show us what you updated here, Dimitri?
**Dmitrii Anoshin** 04:29 Yeah, just address the comments, essentially. I added another section, for entity.
Detector, which is to be filled.
At the bottom.
**Josh Suereth** 04:41 Oh, at the bottom, yeah.
**Dmitrii Anoshin** 04:43 Yeah.
**Daniel Dyla (Dynatrace)** 04:43 Yeah, and near the top added a line for the SDK should provide an entity detector.
Yeah, it's exactly what I expected.
**Dmitrii Anoshin** 04:52 Yeah, I removed the mast.
**Josh Suereth** 04:55 Beautiful.
Beautiful.
**Daniel Dyla (Dynatrace)** 04:59 I need to remove the must.
Interesting.
**Dmitrii Anoshin** 05:04 Yeah, I… actually, I didn't get your comment completely, Josh, because you said you should leave out must, but you…
**Daniel Dyla (Dynatrace)** 05:16 Yeah, so that came from… since I was the one that made the comment, I guess I'll explain what the issue was. The old specification didn't specify it as an entity detector, it just said the SDK must Like, read this environment variable.
**Dmitrii Anoshin** 05:33 Okay.
**Daniel Dyla (Dynatrace)** 05:34 which was outside of, you know, if we have entity detectors, and then the SDK is separately decoding this variable, then how do you handle collisions and stuff like that?
If it's just an entity… any other… an entity detector like any other, then the user can specify how to handle collisions by specifying priority and that kind of thing.
it could be… the SDK… We can decide whether we want should or must, provide the detector.
And it could be, you know, maybe you have a default list of detectors. You have, like, the SDK detector, which detects the SDK entity, should be obvious enough.
you have the environment detector, and, you know, maybe process and host by default? I don't know. Like, maybe we have some default list, and I think if we do have a default list.
Entity Detector makes sense, or, environment detector makes sense to have in that default list.
But as far as whether should or must provide it… I don't really feel strongly either way, honestly. I think most SDKs will, regardless of what we put there.
The only exception to that being some situations, like browsers, where there is no such thing as an environment, so it doesn't make sense.
**Dmitrii Anoshin** 07:05 Do you want it to be entity detector or environment detector? Because if environment detector, it will handle everything else as well.
**Josh Suereth** 07:17 Well, so I want it to be called the Environment Entity Detector.
Yeah, yeah. So that you know clearly it's detecting entities from the environment variable.
This I wanted to call out, I don't think there's a must at all for these. It's, like, right now in the spec, we reserve names for resource detectors, which is container, host, Process, and service.
And it just says that they're gonna fill things out. Service, it says, uses the hotel service name environment variable. See how this is called out here?
So actually, like, eventually with your PR, I personally think, and I didn't have time to respond to comments fast enough, I think you can drop all the SDK interaction and just describe what the environment variable is and how to read it, and that's it. That's all your PR needs. The rest of this we have to embed into other pieces of the spec.
Right? That's my opinion here, of, like, the easiest way to get this done. My plan, though, is, with what you've done, I think we could merge it as is, and just move the pieces in this component to other parts of the spec later. I'm fine with that, too. Like, we're… we're in… we're… this is not a stable spec, so we shouldn't consider it perfect with one go, and we should be able to have open things we'll resolve later. It's just, I think the specification hasn't been in the state for some time, and we're not used to that how we play in that world. But if you… If you remember the metrics SDK days, or even the tracing SDK days, which we don't want to return to Tracing SDK, that was pure chaos, but if you remember the metrics SDK days, that's kind of how we operated, was we… you just leave open sections, you defer to things that don't exist yet.
So that people understand contextually where it is, and you focus on the core thing you're trying to design, right?
**Dmitrii Anoshin** 09:06 Okay.
**Josh Suereth** 09:08 Yeah.
**Dmitrii Anoshin** 09:09 I also have a section about conflict resolution between different, like, environment variables. I guess I would… I'm gonna remove that section in that case, or, like, keep it to…
**Josh Suereth** 09:23 Again, I… I think it will eventually move. Like, what I want to do with that section, and I put that in a comment, I think you have that… where is it?
environment variable conflict resolution, right? This section, what I want to defer to is when we have an SDK initialization section that talks about the entity provider.
and talks about resource detector. We will talk about how overall entity resource conflict resolution works.
And within that, it'll be implicit with how environment variable detection works. So we can say, like, here's where OTEL resource attributes are resolved.
Here's where the service environment detection happens, and here's where the environment entity detector happens. And so it'll be explicit what conflict resolution looks like in that section. I think this is fine to let people know, like, what it'll actually look like, because there's a lot of uncertainty on that.
So we can leave it in the spec where it is for now, here, but I think as we flesh out the rest of this, like, entity detector, startup initialization, That… that this'll move.
Is that fair?
**Dmitrii Anoshin** 10:40 Yeah, that sounds good. So, like, immediate changes to the PR would be renaming of entity detector to NV Entity Detector. That's pretty much it so far. We can… after that, we can merge it.
**Josh Suereth** 10:53 Yep, yep.
**Dmitrii Anoshin** 10:55 Bill, let me push it right now.
**Josh Suereth** 10:57 I do… I am curious, do you think this should be a must,
**Dmitrii Anoshin** 11:02 Yeah, this is another thing we want to discuss. I think it should be masked, but just… But I don't have strong opinion, because I don't work on SDKs.
**Josh Suereth** 11:12 No, I think it should be a must-do, but… Daniel, what do you think.
**Daniel Dyla (Dynatrace)** 11:18 I… I would have it be a must, except that there are some situations where… where it doesn't make sense. Like, a browser is the one that I think of immediately. There is no environment in a browser, you can't read from an environment, so there's no point.
**Josh Suereth** 11:35 Well, yeah, so we should say it must provide an NVENVT detector where the SDK has access to an environment. Yeah, exactly.
Caveat on it, yeah.
**Daniel Dyla (Dynatrace)** 11:46 It's fairly self-evident where it doesn't make sense. I could imagine, also, in, like, some embedded systems and stuff like that, there wouldn't be an environment, and, you know, it's a you-know-who-you-are type situation.
**Josh Suereth** 12:00 We don't have a Lua SDK yet, do we?
Or what are the other weird embedded languages?
**Daniel Dyla (Dynatrace)** 12:07 I'm not sure how… yeah.
I don't think so.
**Josh Suereth** 12:11 Yeah.
**Daniel Dyla (Dynatrace)** 12:14 I'm sure it's possible, like, for example, you could use the Rust or the CSDK in an embedded context. I'm sure they would make it so you could just compile it without this detector, right?
**Josh Suereth** 12:27 Yep.
Yeah, like, like, so that… say, where you say it should, where it has access to the environment, like, in Rust, that would be, a crate feature of, like, if I'm in a standard environment, can I get access? If I'm not, I don't. C++ would be, you know, compiler flag, that kind of crap, yep.
Makes sense.
Cool. Nice, there, if you make the push and the change, Daniel, if you could, review quick and approve, I will probably merge that later today to make sure that gets through.
Because we have enough approvals, I think the comments are all resolved.
Yep.
**Daniel Dyla (Dynatrace)** 13:09 I've got a meeting immediately after this one, but after that, I'll give this a look, but I already… assuming that none of, like, the format specification changed, I think it's all… I read through all that already, and it all looked fine.
**Dmitrii Anoshin** 13:22 I put out the… what we agreed on is the new PR, as a new commit.
**Josh Suereth** 13:30 Feel free to, ping me in chat when you're done, too.
**Daniel Dyla (Dynatrace)** 13:33 Yeah, will do.
**Josh Suereth** 13:36 Right. The other thing I was working on, because I'm dumb, I was trying to see how hard this specification is to feed through AI and have it generate the parser for you.
Anyway, that was one of my dorky, like, sideisms, just to see what the quality of code was like across different languages. You'd be surprised to know that I thought Java would have good code quality, but it chose the most inefficient parser possible when I naively prompted, so… You know, whatever. Anyway, cool. I had… I had one thing I want to talk about, but first I want to check, does anyone have any major topics to go through? I want to update our, timelines quick, but does anyone have anything else they want to talk about, or dive into the, spec PR?
that we have.
The OTEP, I should say.
**Daniel Dyla (Dynatrace)** 14:31 Did you merge your PR into Ted's PR? Yeah, okay.
**Josh Suereth** 14:35 Yeah, it's all updated now. There's so many comments on that PR, I almost want to close it and reopen it, though. Here, I'll bring it up.
So this is 4316.
**Daniel Dyla (Dynatrace)** 14:48 Comments that are not in threads, I assume you mean?
**Josh Suereth** 14:52 They… Let's see, I think there are a lot of comments, not in threads, too.
No, they're in threads, they're just, like, on stale things, so… Yeah.
**Daniel Dyla (Dynatrace)** 15:03 Let's just go through and resolve them, I guess.
**Josh Suereth** 15:06 Yeah, you wanna do that now?
**Daniel Dyla (Dynatrace)** 15:07 Yeah, when we have time, unless you have something else you want to cover.
**Josh Suereth** 15:12 Just the crazy idea I mentioned last time before we closed it. Alright, so, this is about primary open question, which must be resolved before the sub is accepted. I think this is answered, I'm gonna resolve it.
Yeah, let's see… Naive implementation could lead to a degenerate case on mobile.
This is about oscillating entity churn, and what we do on that, right?
And I think… what Ted was saying was, it's the responsibility of… the instrumentation to not churn, or should the SDK have a general-purpose protection mechanism?
to avoid churning SDK events.
**Daniel Dyla (Dynatrace)** 15:54 I mean, I think the instrumentation should churn. Like, when something changes, it should detect it and send it to the SDK. It's not up to the instrumentation to, you know, if the network is changing all the time, it's not up to the instrumentation to determine what to do with that data. It's just provide it to the SDK, and the SDK should do something reasonable, I think.
**Josh Suereth** 16:18 Yeah, so I do think that this isn't resolved in the proposal.
So, either we need to leave it as an open question in the OTEP, and then solve it in the… as we build out the actual spec, or we need to make a quick proposal here of what we would do to protect in the SDK. I think generally protecting the SDK is, like, one of our… One thing we haven't done early in a lot of our spec work, but we should do here.
**Daniel Dyla (Dynatrace)** 16:44 Yeah, I would lean towards, leave it as open question in the OTEP, and handle it in specification.
It's an implementation detail, almost.
**Josh Suereth** 16:57 Let's move this to be an open question in the LTAP.
Andrew.
Resolve that open question. When do we formalize specification?
of this design.
You start actively… Prototyping… Existing prototypes now. Okay.
Did I spell discussion wrong? No, I did. It's fine. Okay.
What was Tyler saying here? Does this mean there'll be a V2 of the SDK, given this is backwards and compatible?
This one… I don't think we have to break version compatibility, but we have to check this with Go.
I think we can mark this as resolved, like, that it'll be up to maintainers whether or not they need V2.
**Daniel Dyla (Dynatrace)** 17:50 Yep.
**Josh Suereth** 17:51 I don't think it's a big deal to have a V2, personally, but…
**Daniel Dyla (Dynatrace)** 17:55 In general, I think, you know, I know that, some SIGs have been… resistant to things like breaking changes, I think SDKs should start revving V2s anyways, and I think the spec should be written in a way that, you know, we'll just say, this is a breaking change, make it in the next major version of the SDK.
**Josh Suereth** 18:20 Yeah.
Okay.
So, what should I write here, then?
2… Okay, introversion.
Allowed.
First spec… And maintainer… Maintenance… Sorry, it's in no hotel.
Given the success… of, OpenTelemetry.js recently.
I think… Anyway, actually helping.
Let's pump in time for SDK. Alright.
Cool.
Does that sound good?
**Daniel Dyla (Dynatrace)** 19:51 Seems good to me, yeah.
**Josh Suereth** 19:52 Okay.
These are a bunch of things… Yeah. There's, like, 34 conversations to get through here. Some of these we… I don't…
**Daniel Dyla (Dynatrace)** 20:09 They're so specific, like…
**Josh Suereth** 20:11 Yeah.
I can respond to the specific ones there. Why is locking relevant here? Seems current focus topic, but isn't the most important, right? Using the API migration. This is out of date, so I… I can just… declare that base… that, you know, the spec has been updated. I think, I think Tim actually got pulled onto something else and isn't participating with entities right now, so… Yeah. I'm not sure that these will… be resolved.
So I might skip those. Let's see, here's some raw comments.
How do I reconcile this OTEP with the latest assert… with the last assertion?
Trustee provider is created, the association cannot be changed later. Oh, from the stable spec doc.
A resource can be associated with tracer, provider, tracer, provider, the association cannot be changed later. We're changing the entities within resource, but not the resource, is how I…
**Daniel Dyla (Dynatrace)** 21:09 To me, that seems like a, It seems like weaseling out of the problem. I think it is a, a valid concern.
the question, I guess, is how do we handle it? Like… We've… we haven't made any breaking changes in stable spec.
We have, at some times,
**Josh Suereth** 21:36 Yeah.
**Daniel Dyla (Dynatrace)** 21:37 redefined, We've retconned some things in recent history here.
**Josh Suereth** 21:45 Yeah.
**Daniel Dyla (Dynatrace)** 21:45 A, it's not breaking. C, also complex attributes.
I think it's a valid concern.
I don't know how we can handle it, though, without… I mean, without, like, splitting entities out of resource, or providing… a separate… Like, you know.
A separate resource and then entity resource on the proto, or something like that, which we don't want to do.
**Josh Suereth** 22:19 So… I… the complex attribute example, we might be able to leverage that here, but maybe not. So basically.
Here's what I think should be true when we're done.
If you don't make any changes to how you're using an SDK, that invariant holds.
Right? So, if I'm using SDK as of today, and I engage with entities, but I'm not doing any API entity work.
that invariant actually holds. And so, programs that were valid in the original spec, and new programs using that original spec, will still continue to hold that invariant.
only programs that are written that actually produce entities in the future will break this invariant. So, from that standpoint, we have like, if you think about forwards and backwards compatibility, we have backwards compatibility of a program that was written with A will continue to work with A with the same invariance. What we don't have is Something that was written that assumes that invariant for everything, when they see this new data, might break.
Right? So from a SDK API standpoint, we have backwards compatibility, but not forwards compatibility.
And for those of you who aren't familiar with the hells of Java and Maven, and don't care about backwards and forwards compatibility, I can try to find those definitions for you, but it's basically, you know, if I have a system that was compiled against A, and then I replace A, or I replaced dependencies of A with newer dependencies.
does it continue to work? That is backwards compatibility.
Right?
The next thing is, if I have a system that's working with dependencies A and B.
And I recompile it against dependency, you know, where B is a new version. Does my system continue to work? That's forwards compatibility.
So… Yeah.
We have one, but not the other.
**Daniel Dyla (Dynatrace)** 24:33 Yeah I mean… I've never really been… this is one thing, I've never really been happy with the immutable resource from the beginning. I never understood why… That stipulation was even there.
And in practice, nobody treats it like it's there. Like, a receiver, like, from Dynatrace's perspective, we receive… you know, on… if somebody's instrumenting a Lambda instrumentation, for example, the resource could be different on every export, and, like, we don't really care.
And I don't… I'm not aware of any receivers that do care.
And I know that people are using in-production collectors, which modify the resources. I think in practice.
This was never true to begin with.
It was an SDK concern around, like, thread safety, as far as I'm aware.
Like, I don't really know why it's defined as immutable to begin with.
**Josh Suereth** 25:37 Internally, this is how all our systems work, and I think there's part of this came from OpenCensus.
**Daniel Dyla (Dynatrace)** 25:43 There, there's a…
**Josh Suereth** 25:45 Yeah.
By having it be immutable, there's a bunch of performance optimizations you can make.
Effectively, right? So, I'll give you some examples, that I can talk about.
**Daniel Dyla (Dynatrace)** 25:58 Optimizations in the SDK, or optimizations in the analysis backend?
**Josh Suereth** 26:03 Everything.
**Daniel Dyla (Dynatrace)** 26:04 Okay.
**Josh Suereth** 26:05 So, if resource is immutable, what I can do is at startup, I can talk to my backend and say, hey, think OpAmp, actually. OpAmp uses resource, right? So I can talk to OpAmp and say, hey, here's who I am.
What policies do you have in place for me to collect data? I'll say, cool, sample 10% of traces, keep these 5 metrics, report them every 30 seconds, right?
And the reason that works is because the resource is immutable, and I get that information, and then I can report my identity back and say, hey.
what information do you need now? And I can have a control plane that will control my configuration using that resource. OpAmp is designed around this concept as well.
But that's, that's like a thing you can do. The other thing we can do is, if resource is immutable and sufficiently unique.
You can use it to figure out how to do, you can divide your network.
Right? And, do sharding right at the client, instead of necessarily after a load balancer.
So, you could decide within the SDK, communicate with the server and say, cool, here's who I am, what endpoint do you want me to talk to? And you can actually funnel your traffic to different parts of your system based on the resource identity. So you can shard, like, pre-shard work, so you actually put less load on your load balancer.
That kind of stuff. So there's… there's, like, reasons that having resource immutable works, and again, I… that's why I think the end result of this that I want to see is where I need a mutable resource, I can still keep it. It might be asynchronously initialized.
But where I need a mutable resource, like in browsers.
I still need to work in that fashion, right? I still need some capability there.
And, I… browsers is the opposite. You're not gonna have every single browser call back and say, hey, cool, what data do I keep? That's way too expensive. You're just gonna have the browser slam data out and deal with that funnel, you know?
So, architecturally, from a server side, one thing makes sense, and from a browser, different things, and we have to blend both of these worlds together.
**Daniel Dyla (Dynatrace)** 28:15 Yeah.
I almost wonder… so I know that we added entities to resource in order to maintain backwards compatibility with resource receivers. I almost wonder if we would have been better off not doing that, and having a separate field on the proto that's just entities, that's a list of entities, and then maybe having a configuration that's like, I want Here.
or maybe even not a configuration, I don't know, copy all… Like, raw resource attributes would go into resource, obviously, and then all… startup…
**Josh Suereth** 28:58 identifying attributes from entities would be copied into resource, and just deemed…
**Daniel Dyla (Dynatrace)** 29:04 And then, say, the resource never changes. This is… this is still just the resource. How it's initially calculated is slightly different, but mostly the same. And then the list of entities can change over time, but it's a separate field.
**Josh Suereth** 29:20 Yeah.
**Daniel Dyla (Dynatrace)** 29:21 the concept of entity ref.
Like, it's… it's… it would be a wild departure from what we have today.
But…
**Josh Suereth** 29:29 Well… You remember my wild departure, right? I actually want to make it so, you can pass an entity when you grab a meter, or a tracer.
And so, instead of having… instead of, like, the browser sig being like, cool, I'm gonna change the core resource, core resource is static.
Like, there is async initialization, which I still think we want to do for JavaScript. Like, I still think we want this async initialization.
to support what you've done, right? And make that more crystal clear, and have that phase, so you can do async initialization. But, we have a immutable resource after initialization, and then if I want to change the entities that I'm reporting against, if I call Get Tracer and I pass an entity.
I call getMeter, and I pass an entity. And I'm now reporting against resource with this entity as an additional thing that I'm reporting, you know? So, like, the… a way to phrase this would be, the resource might have the host.
Right? Or, the resource might be the browser itself.
And then I would grab a tracer to say, here's my current session, I'm gonna report data against it.
**Daniel Dyla (Dynatrace)** 30:41 But in order to do the optimizations that you just talked about, you still need that, like, core identity resource to be immutable, and you need to report it In a receiver, you need to know this is the core resource versus, like, the extended resource with the entities.
**Josh Suereth** 31:00 Yeah, yeah, yeah, exactly. So, but the difference would be, like, when I send the data, right, the core resource would have a set of entities in it.
And then the, instrumentation scope would have an entity in it.
Oh, I see. Or instead of entities. Yeah.
**Daniel Dyla (Dynatrace)** 31:17 I see, so the top-level resource would be that core resource, and then…
**Josh Suereth** 31:21 Doesn't change.
**Daniel Dyla (Dynatrace)** 31:22 So if you would have another.
**Josh Suereth** 31:24 Exactly.
**Daniel Dyla (Dynatrace)** 31:25 Right now, we don't have, right?
**Josh Suereth** 31:27 We don't have that now. We have attributes in instrumentation scope that 90% of the SDKs don't implement.
**Daniel Dyla (Dynatrace)** 31:34 So instead of having a resource there, why not just entities?
**Josh Suereth** 31:40 Oh, I wasn't saying there'd be a resource in instrumentation Scope, I'm saying just entities.
**Daniel Dyla (Dynatrace)** 31:45 Yeah, okay, yeah. Yeah, yeah.
**Josh Suereth** 31:47 Yeah, exactly. So, so when I get a meter, I would put a set of entities, and that gives me a thing I can talk about that entity on, right?
And since 90% of SDKs haven't implemented attributes on instrumentation scope, Even though it's specified.
We could… we could… we have some opportunity to kind of do some cleanup there, and make it more clear what the hell that means.
**Daniel Dyla (Dynatrace)** 32:12 It… it still doesn't solve the immutable resource thing, though, because if you have an entity that's a part of your, like, core resource, and that entity changes, your core resource isn't changing.
**Josh Suereth** 32:24 Except, except what we're doing, I think it's actually fine, because what we're doing is, in resource, we will know… we'll have a set of identifying attributes and a set of descriptive attributes, right?
And so what we're going to be modeling now is those things that would cause a resource to churn and be unstable, we're effectively pushing in the descriptive part.
And today, in OpenTelemetry, I would say you should not report them in resource. They're not part of your core identity. If you do so, you're actually causing a problem.
So, we're actually kind of resol… like, is it breaking? Yes.
Frankly, it is breaking. But… The end goal would actually be more attuned to what the spirit of the spec was.
Right? Because I'm not going to report… if I have 5 IP addresses and they could churn or change, I'm not going to report that as a stable identity in the future. I'm going to find something else which is my stable identity, and I will report those as descriptive attributes, and if entities exist in resource, I know that I can ignore those attributes because they're not stable.
**Daniel Dyla (Dynatrace)** 33:30 But right now, all the descriptive attributes are still pushed onto the resource as resource attributes.
**Josh Suereth** 33:36 And if you read our spec, that's actually a violation of how you're supposed to use resource. It's just, it's so useful, everyone does it.
**Daniel Dyla (Dynatrace)** 33:45 No, no, no, I mean in the entity spec, like the descriptive entities… Yeah, yeah, yeah, yeah, yeah.
We say, put them on the resource.
**Josh Suereth** 33:54 Yeah, we do, we do. But we also, In the spec, we're also changing it so the resource identity is only the identifying attributes, none of the rest of them.
**Daniel Dyla (Dynatrace)** 34:05 Yeah, but… so it means that you have to… as a receiver, You have to… understand those… you have to update to… to… You know, understand entities in order to maintain that, like, resource Invariance.
**Josh Suereth** 34:28 Yeah, you… by the way, we're about 5 minutes over, I don't know if you need to jump, but…
**Daniel Dyla (Dynatrace)** 34:33 I do need to jump.
**Josh Suereth** 34:34 Well, let's… let's continue the discussion. I think… I think you… this is… this is… this is key. We need to… we need to continue sorting this out, and yeah, we made a bunch of decisions where some things are slightly breaking.
with the assumption that basically, again, my… the way I've been operating, backwards compatibility is preserved.
And forwards, like, you have to migrate everything to the new world to get non-breaking changes. So, if something is using entities in the New World, then everyone starts to need to engage with entities in some fashion. Except, I would argue.
This descriptive attribute breaking thing?
People are using resource with descriptive attributes today. We know that. We've had SEMCOM proposals for it. They're engaging with mutable resources today.
And so, even though the spec says you shouldn't do that, they are doing it. So, we're not making… yes, we're breaking the spec, and we can call that out as this is a breakage.
But I don't think we're breaking users.
**Daniel Dyla (Dynatrace)** 35:36 I think we just have to be very careful about the messaging of the change. I'm not saying that we shouldn't necessarily make the change, I'm just saying we can't… I would not be in favor of… Doing, you know, Greg, I'll… like, mental gymnastics to say this is not breaking, the way that we…
**Josh Suereth** 35:57 No, yeah, yeah, yeah, yeah. I don't like that.
**Daniel Dyla (Dynatrace)** 36:00 I would rather say, yes, this is breaking, we know it's breaking, but here's why we're doing it anyways, because we believe it to be valuable.
**Josh Suereth** 36:09 Well, actually, what I'd like to do, I want to be more clear to users, right? Where I want to say, if you did X, this is non-breaking. If you did Y, you were broken for these various reasons, and this will break, but it's fine, but here's why we're going this direction, right? So, like, but if you were doing this, you're just broken, sorry. But make it clear of, like, what breaks and what doesn't, because I think that nuance is important.
Right?
**Daniel Dyla (Dynatrace)** 36:36 Yep.
Alright, I have to jump.
**Josh Suereth** 36:38 Cool. Alright, I'll see ya.
