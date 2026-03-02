SIG: Entities SIG
Date: 2025-07-03
Duration: 55 minutes
Zoom Recording URL: https://zoom.us/rec/share/Nyyhq4e7qYFVtiqpR9vlLL0Bf-WaJ_NzI0bNlh2jbVcf_hbXzs2qoZGluLbRD2da.37YO7VjbDfICJANp
============================================================

## Zoom Recording Transcript

**Josh Suereth** 00:29 Hey! Everybody.
**Dmitrii Anoshin** 00:33 Hello!
**Tyler Yahn** 00:36 Hey!
**Daniel Dyla (Dynatrace)** 00:41 Before we get started here. I wanted to quickly mention the 1st meeting of the new browser. Sig
is in half an hour, so I'll drop for that when it comes.
**Josh Suereth** 00:54 Okay, do we need to change our time at all, then to accommodate you in the in the future?
I mean selfishly, ideally. Yes,
**Daniel Dyla (Dynatrace)** 01:06 I understand the difficulty of finding meeting. Time slots that work for everybody.
And if I have to drop a half an hour early or
join the browser sake half an hour late, half the time. That's probably okay.
But yeah, if we could move the meeting, that would be fantastic.
It's just.
I'm not the only concern here.
**Josh Suereth** 01:34 Yeah, I understand.
we can. Also, we'll try to get through everything important in the 1st 30 and then
I'm I'm debating whether we're we're at every other week here.
which I think was all we had like time wise to focus on with folks like we weren't.
We basically were having meetings where we talked about. Oh, we didn't make any progress yet, but every 2 weeks we're constantly making progress and have things to talk through so
The other option we could do is do a 30 min meeting every week.
So we talk about less in a particular week. I don't know. We'll run it by everyone at the end of the meeting. Sound good.
**Daniel Dyla (Dynatrace)** 02:16 Works for me.
**Josh Suereth** 02:20 I have one topic in here. I wanted to talk through. I don't know if other folks have topics. There's a spot here to keep adding things. I think this is probably the thing we should talk through while you're here, Daniel.
just cause. Yeah, it's it's kind of a big decision. I think we should talk through with the Sig. But things that came up in the spec. Pr,
with that I'm gonna put a few links here quick to. Sorry I didn't get everything
set up ahead of time.
Technically, I have off today. But I you know, I love entities. So I'm here, anyway. Cool.
Should we give? It's like 11 0, 3. We can get started. All right. So first, st I want to talk about basically the possibility of having entities be an Api instead of an SDK, only thing.
there's there's a few reasons for this, and there's there's a link to the specification Pr for our SDK, where I think some people raised some concerns.
and we kind of talked about this a bit. There's also the the pr, not the pr, the Otep from Ted for the browser based work
where we wanted to have the ability to kind of add and remove session based entities like live.
So
you know, this is just me brainstorming here for a discussion. But basically, I think there's a couple of benefits. Right now, inside of like weaver and Syman conventions, we do code generation for instrumentation.
That code generation generates code. That depends on the Api. We have not built code generation for resource. We do resource attributes, but we don't like generate entities. Yet. The way we have like generated metric code or or span code right?
There's a certain parallelism here with entity and the other signal types as an instrumentation. Api, where, like me, as a cloud provider, could give you resource, detection, instrumentation that is independent of the SDK, and that you can register and and hook into your system. Similarly, you know, if I have a library that does. Xyz. I can have instrumentation for that library.
I think there's some concerns which is basically, we want to make sure we have as stable a possible resource before we send signals, and if we expose resource, detection as an Api, it means we have effectively for some languages we have to deal with threading concerns.
I believe in Javascript. You actually already have the issue of having to do asynchronous things with resource. Is that correct?
**Daniel Dyla (Dynatrace)** 05:16 Yes, we do.
**Josh Suereth** 05:18 Yeah. So I don't like. For some languages this is a benefit for others. It actually kind of significantly changes some of the design of the language.
However, when I went through a straw man to try to think through this, I'll just give you my rationale if you look at logger provider right? It has a get logger method. If you look at meter provider has a get meter method, tracer provider has a get tracer method. The logger is the way that you
interact with instrumentation around logs, the meters, the way you act interact with instrumentation on meters and and metrics tracer is how you make spans and that sort of thing. There's like methods on it to do stuff. So the question is, what would resource provider have? Well, I think it has a get resource. It's the provider of the resource. Right?
And then what would the Api look like? This is not the SDK. This is the Api.
I think we have 2 kind of things that would exist in this Api going forward, one that exists now, and one that exists. If Ted's Otep gets accepted, which I do kind of anticipate. That would happen.
The 1st one is basically we could register an entity detector on the Api and say, here's an entity detector. There might be options for that. But this is similar to Async metric instrumentation registration. If you're not familiar with that basically for metrics, you can say, Hey, I have a metric. Here's the name of it. Here's some information about it, and here is a callback that I want you to call when you do metric collection.
So I think entity detectors kind of similar. It's, it's basically here's a thing that will detect entities. Here's some information about it.
add it to the resource, the the Api resource, which is not the same as the SDK resource right?
And then in the future, if you, if you read Ted's Otep, there would be add entity, replace, entity, remove entity. I think those were all methods that were submitted to be on
the entity provider
in this case we'd call it resource provider. We'd have those methods on resource which you'd get access to. And then the browser Sig, for example, would call these methods on the Api resource. And the SDK would interact with that in some way. So we're creating kind of a more stable boundary for the instrumentation that has to understand when entities is changed.
I think the the entity detector and entity, like class that is in the current spec. Pr. Would remain unchanged completely.
So this is the only difference would be these move into the Api, and then we have this. Well for the for the initial Pr, we basically just have registered entity detector in the Api and a resource provider that gives you back a resource.
Yeah, go ahead, Daniel. I wanted to open up for discussion and brainstorming.
**Daniel Dyla (Dynatrace)** 08:20 Yep. So I have a couple of angles that I'd like to address here.
The 1st is like the motivation behind. Do we want this? I think, I,
the the entity data is telemetry data. And the Api is how we collect is how users tell us what data telemetry data they want us to aggregate and ship off somewhere.
I think
it could have been argued that resource should have been there all along. I think the main reason we didn't was because we didn't expect it to be changed on an ongoing basis. So just doing it once that's set up was fine. Now that it's expected to change on an ongoing basis. I think that expectation has changed.
and the Api is how you tell opentelemetry. Here's the things to send. The SDK is mainly a configuration in my mind, and the resource or the entities are not a configuration. They're data.
So that's that's from like the motivational side. I think that it makes sense to have it in the Api.
I certainly think, providing entity detectors and and building it into libraries, and such that don't know whether an SDK is registered makes sense from many different standpoints. It might make sense for a platform provider to provide like.
you know, Gcp. Always has the Gcp detector available. Whether you're using open telemetry or not. The data just shows up. Everybody's happy, even like I could see a database driver
being like, I am emitting traces when you contact Redis. But I'm also going to emit an entity that says, like, here's the data. Here's the database you're interacting with.
you know I'm not. That use case, I think, is is a little less clear, but it opens up that path
in terms of the actual Api that you propose here.
I would remove the register entity detector
because I view the entity detector as analogous to an instrumentation in this case, and we don't have in the Api. We don't have like a like in the tracer provider. There's no register like trace, instrumentation, function.
The trace instrumentation calls start span, which in this case add entity is what the the entity detector would call
I think the entity detector is a user of this Api.
It's not a part of it.
In the same way. That instrumentation is not a part of the tracing and metrics and logs Apis, and that a single instrumentation that uses
tracing and metrics may also want to use the entity api.
**Josh Suereth** 11:31 Those. Those are good points. I
just my. My initial response is, I like what you're suggesting. I still think there is a add entity. Async
option.
Where are you?
Yeah.
**Daniel Dyla (Dynatrace)** 11:47 That's that's fine. I just think.
**Josh Suereth** 11:49 For you.
**Daniel Dyla (Dynatrace)** 11:49 Maybe maybe it's a rename of register entity detector.
**Josh Suereth** 11:52 Yeah.
Good about renaming this too awesome.
Similar to Async instruments.
Metrics.
Okay?
Yeah. Awesome.
yeah. So so to me, the important part was. There's a synchronous way to throw entities on, and an asynchronous way.
whether or not it's a detector I actually don't care if we call it entity detector.
cool anyone. Anyone have other thoughts based on what Daniel said or related. I I see Tyler on the call. I know that you
own the go SDK and Api, what's what's your thinking? Here.
**Tyler Yahn** 12:45 Yeah, I'm I don't see too much of a problem.
I'd have to like work through, obviously like the whole thing. But
I mean that all seems reasonable to me, especially with like the Async callback like. Seems fine
sorry. I don't have much more info. Yes, it looks looks good.
**Josh Suereth** 13:06 I I'm just more worried about. If there's practical concerns with the implementation.
but if we're if we're amenable to this direction, I'll update my specification. Pr, so what we'll do is we will get rid of this
and we'll basically create a resource provider Api that has get resource on resource. We'll have add.
I don't know. If, should we do add or add or replace, we can. We can figure that out later, but we'll have something like, add, remove, replace crud operations on entity, right? And we'll have an Async option for that as well
where you can.
Yeah, I yeah.
**Daniel Dyla (Dynatrace)** 13:59 The Async option.
I am not necessarily a hundred percent convinced that it's required.
And maybe we can talk about that a little bit. Again drawing analogies to the other.
Apis taking the trace. Api as an example, start span as a synchronous Api.
It's called by the instrumentation whenever a span starts, which happens asynchronously all the time. But the Api itself is synchronous.
and it's up to the instrumentation to determine when to call it, I think, for entity detectors it could be the same. It's a little bit different with metrics, because in metrics
you want to like pull every second or minute, or whatever to see what the current value is
with entities. You're waiting for the detector itself to tell you when something has changed.
a user has logged in, or your IP address changed, or whatever, and I guess maybe we could.
It could all that every minute.
But I don't think in the normal case, we'll want to.
I think the detector itself could easily have its own timer if something is a polling
versus event based. But also we want to be able to react directly when events happen without waiting for the next polling cycle, which may or may not actually come.
So I would remove the Async. I would try to remove the asynchronous Api from this
and see what roadblocks we run into. I'd I'd rather try to remove it
and see what's possible, and add it later than to add it now
and find out that we don't actually need it. But now we have to maintain it forever.
**Josh Suereth** 16:01 Yeah, that's a good point.
I think I like what you're suggesting. So basically, let's remove Async.
and then let's do some prototyping on. Let's take existing detectors
and and let's build this Api.
And then we can figure out how like
hard that Api is to use, or how good it is for users. I think the main reason I still think Async.
and this could just be a
this, this is probably solvable, is, how do I make sure that the
the detector, if you will, actually runs at Startup.
So I think you're right that we need the ability synchronous gives the ability for the instrumentation to own the lifecycle of how and when that runs, and with metrics with Async, we know that, like the lifecycle, is complicated enough, that giving the lifetime of when to collect to the metric system, but still retaining the memory. Allocation yourself is what Async instruments do.
I don't know if that's needed for for entities as well. So I think we should try without it. It's just that's that's the thing I want to make sure we
don't lose is that this instrumentation that detects these entities has a place to run in our ecosystem like right now we have a I'll show this
to do
right now, if we look at our spec, it's only in the SDK on resource.
We have a notion of detection, right
resource, detector packages must provide a method that returns a resource resource. Detector packages may detect information from multiple sources, and the logic is expected to complete quickly. We talk about this. We talked about these things and how they can have a name and be configured right?
This is still in development. So I guess.
how do we change this in a non-breaking way.
If if I can interpret what you're saying, and I'm just thinking out loud, by the way, so feel free to stop me.
we can register an instrumentation component.
We could. So so this whole thing about resource detection could move out of the SDK specification.
And we can have a component that we can configure, that ensures that the instrumentation runs at Startup, and that you can register these things, and that we have something called container, something called host, something called process, something called service. Right
like this. This, I think, is important not to break for users. I want the ability for resource detectors named container host process and service to continue to exist, to to work with our config structure, if possible, and to do the right thing. I think what we're saying now, and if I'm interpreting what you're saying, Daniel, is this resource detector would would operate by
grabbing the resource from the resource Api, and filling out entities on it.
Is that correct?
**Daniel Dyla (Dynatrace)** 19:28 Is no craft
cause the the Api is right. Only unless I'm misunderstanding what you mean by grab from the Api.
**Josh Suereth** 19:43 Yeah, yeah, no, it would. That's what I'm saying is, it would write. So basically, this resource detector that you register and configure would would use the Api to call resource provider, get resource, and then would say, add container entity, add host, entity, add process, entity, add service, entity, depending on which one.
**Daniel Dyla (Dynatrace)** 19:59 Yes.
**Josh Suereth** 20:00 Yeah.
**Daniel Dyla (Dynatrace)** 20:00 Yes.
**Josh Suereth** 20:01 And that's all they do. So so this specification doesn't isn't necessarily broken. We just actually clarify how it works.
**Daniel Dyla (Dynatrace)** 20:09 Guest.
**Josh Suereth** 20:11 So there's still an a resource detector component. But the way the resource detector component works is it interacts with the Api.
**Daniel Dyla (Dynatrace)** 20:21 Yes.
**Josh Suereth** 20:22 Okay. I think that I'm comfortable. With that. I think that actually works out. Still. Tyler, I know.
**Daniel Dyla (Dynatrace)** 20:31 As far as.
**Josh Suereth** 20:31 Go ahead!
**Daniel Dyla (Dynatrace)** 20:33 I was gonna say, as far as backwards, compatible resource legacy stuff goes. There's another way that it could be viewed, which is
that the resource detectors do run in the SDK like the legacy ones without entities, entity, awareness.
and that that's like a base resource. That, then.
is, you know, the the Api would would add on to that.
No, I think I like your version better.
**Josh Suereth** 21:08 I'm hoping we can do it in a non-breaking way, and and keep these things working because I think, like I was talking to Jack, about this. I think the this is needed. This is powerful. We want this to work like. And and I think we need to find a way to make it work with with what config is done. Honestly given the prototype we're doing. Tyler. The thing I'm most worried about is go, resource, detection. How how is go handling this? These resource detector names. Now, in this development, spec.
**Tyler Yahn** 21:39 Like in the config module that's actually implementing like the configuration. It just is like
manually going in. And and if it's configured to do this, it'll create that detector, and then it will run the detector
within whatever resource.
But it's like a separate module, so like the SDK itself isn't actually doing any of this stuff.
Right now.
**Josh Suereth** 22:01 I see, and your your fine grained resource detectors, where they would detect, like one attribute at a time that module is just like registering a couple of them right.
**Tyler Yahn** 22:12 Yeah.
**Josh Suereth** 22:12 Like this.
**Tyler Yahn** 22:13 Yeah, like, I think, yeah, exactly. I think process is the only one that is a little bit more like involved.
But yeah, like each. Each one of those is just like a single essentially attribute that gets added to the resource. Yeah.
yeah, I mean, I
think there's a little bit of Wiggle room for us here, because, like, we haven't like, we're still working on this. We have like this other thing that's trying to like.
Hmm, generically create these resource detectors. That's in development right now. But
it's it's kind of the same process. It's a totally separate module that is like a user has to set it up as well. So it's not. It's not like baked into the SDK right now.
**Josh Suereth** 22:57 Gotcha.
Okay. So if this is, if this is currently being built out, I think this gives us some flexibility. I mean, I should list this in our in our notes. But one of my goals is, we have motivation for why we propose Api. Let's get rid of this. But I also want to have Cogen
from Weaver be a thing that this can do. So like, you know the your semantic convention. Go, Directory Tyler, that, like generates the metrics Api.
**Tyler Yahn** 23:28 Yeah.
**Josh Suereth** 23:29 I would love if we have something in weaver that can generate the same thing for entities.
Right?
And then these detectors can leverage that. And so.
and the the more the names kind of align between the entity name and the detector name, I think the better we are for users, so I think this has a lot of merit. I will. I'll take an AI now to go update the spec Pr for an Api. If you I want to be wise with. With Daniel's time we only have 5 min left. We can do that here. We can move on to other topics, because I think that
we have a direction. I'll update the specification Pr with the Api we just discussed. So register entity detector will be gone. Add and remove entity will be there. I'll figure out if it's add and replace or add, remove. We'll do that. Offline.
yeah.
this and then and then I might start prototyping some resource detection. How that looks in in the Java SDK that I have, and hopefully we can get the same thing and go, and a few other languages.
Does that sound like a path forward?
Cool?
Alright! Is there anything you want to discuss before you have to head out.
**Daniel Dyla (Dynatrace)** 24:52 Sorry I didn't realize I was muted there. There's nothing that I specifically want to discuss now.
**Josh Suereth** 24:59 Okay.
cool? Well, then, let's spend the rest of the meeting. Let's take a look at the active projects and progress, and see if there's anything blocked or anything we can help with.
Cool am I showing the right screen here or.
**Dmitrii Anoshin** 25:15 We are all sharing.
**Josh Suereth** 25:16 It. It crashed. Okay, wonderful.
Alright. Here we go.
Right? So we have in progress the
entity SDK specification. That one we just talked about that one. I'm on the entity prototype for the SDK specification is the Java prototype resource, entity, merge logic prevents fine grain detectors. Given the discussion. We just had Dimitri, I think. I don't know if you if you worked on this at all. But I kind of feel like
we're gonna go a different direction here.
**Dmitrii Anoshin** 25:57 Okay, yeah, probably move it. I haven't looked into that yet. So I've been focusing on the collector first.st So maybe we can move it to do or.
**Josh Suereth** 26:08 Yeah, that that's fine. I'll I'll move it back into
I'll move it back into this one here. I guess a question for Tyler. Do you expect folks to continue to use programmatic? SDK configuration pro primarily? Or do you think we'll have a mass migration to the config based? SDK setup for go.
**Tyler Yahn** 26:32 I think
programmatic configuration is probably going to persist for quite a while. I don't anticipate the config stuff, at least in the next year. I don't see that happening really fast.
**Josh Suereth** 26:44 Okay.
But that's just obviously like my opinion. I don't know.
No, no, that that's fine. I just that. I mean, all of us are just taking a guess at some of these things. Right? You never actually. But that, yeah, just a good estimate would be fine the
right now all of the detectors in the programmatic config are those like individual things? We need to decide if we are going to
break those and ask people to move to new like entity detectors in the programmatic config
and ask them to move from A to B, or if we're going to try to find a way to make those detectors work with entities.
That's that's basically what this task is. So the assumption in the way it's worded now is that we would keep the existing detectors a hundred percent as is
yeah. Anyway, we have to. We have to discuss this.
**Dmitrii Anoshin** 27:39 If we have the new way like to generate entities, we probably can keep the existing fine-grained logic just to set up resources like old fashioned way. We can make it
kind of deprecated, and don't that as well.
**Josh Suereth** 27:54 Yeah, it's that that is a harder ask for people to migrate in that fashion, but I like, if it's
the way I view any kind of migration like that. If the pros outweigh the cons, so.
**Dmitrii Anoshin** 28:06 Okay.
**Josh Suereth** 28:07 Like, if we think config is a big benefit to users, and entities are benefit to users, the combined weight hopefully will move people to the new way of doing it right? So that that's kind of my thinking. There.
cool. We we do have to like, take some hard guesses. All right. Let's move on to add support for new resource and see references. Proto message in the collector. How's that going? Dimitri.
**Dmitrii Anoshin** 28:32 So, yeah, I created this one issue to summarize all the work needed, and, like the most important parts of the collector to market as supported. And the first, st the 1st issue that was done is actually support that and P data interface P data interface is an access point to the actual data in the collector. And that's not. It wasn't very easy, because I had to
like refactor it a bit to move
accessors, accessory accessors to the entity refs from the resource to a separate in experimental package, because in collector, we have
P data 1.0, and we have pretty strong
Api guarantees. So I had to move it somewhere else until that message Prota message is stabilized.
So that is done. And currently we can access everything related to resource references that we have. And I created those other issues. We I have some volunteer to do the back exporter, which is easy and others I'll probably do myself.
**Josh Suereth** 29:50 Should there be an issue for adding it to Ottl.
**Dmitrii Anoshin** 29:57 Ottl, yes.
ottl, it's a big one. I've been thinking of that as a probably phase 2, because the 1st one is a.
**Josh Suereth** 30:09 So.
**Dmitrii Anoshin** 30:10 What was based on my original
prototypes. It's it involves detection. Processor is the most important. Then Kubernetes, cluster, receiver and host matrix receiver which are generate the entities, and then, probably as a phase 2, we would do Ottl, I believe, because, Octl, it's a bit more complicated.
**Josh Suereth** 30:31 And yeah, yeah, there's a couple of decisions to make there. I I think
you probably know this, but I've rewritten Ottl a few times in a few different languages, and I have some proposals for it. But if you need help modifying Ottl to support entity, ref I'm pretty sure I could get that done relatively quickly. It's just we have to make some hard decisions on what the Api shows up in Ottl.
**Dmitrii Anoshin** 30:58 Right.
**Josh Suereth** 30:59 Like, are we going to treat entities as a 1st class thing where we do the unwrapping in Ottl on your behalf? Or do we want to expose them raw, we can do both honestly, it's actually not hard to to pick one. It's more
the function ecosystem that yeah. I don't want to phrase this. We need to firm up the specification in Ottl, and I'm I'm I have some proposals on that. I haven't had time to get around to really pushing on them hard. But entities might be a good excuse to firm up some of the specs, so that we can do
an advanced entity support. There.
**Dmitrii Anoshin** 31:39 Yeah, I agree. It's like a lot of questions we need to ask and answer before we can proceed, because once the interface is defined, for Ottl is going to be hard to change. I believe we already that component is in Beta, in the collector, and it will be complicated. That's why, I'm even thinking that
I would delay Ottl definition and to the point when we have
this separate entities signal, because once we have a signal, it probably better to align ottl language for both references and the entities in Ottl.
rather than doing Ottl for references first, st before even understanding how we do the separate signal does make sense.
**Josh Suereth** 32:33 Yeah, I think the main thing I'm concerned about is we want to make sure that if you're using Ottl on resource, you're not just blowing away your entities and causing havoc.
**Dmitrii Anoshin** 32:42 Oh, okay, that's like basic support. I I see what you mean.
**Josh Suereth** 32:48 Yes, I mean, there's exposing entity ref directly, so you can manipulate Ottl, and then it's just making sure Ottl doesn't blow away. Entity refs.
**Dmitrii Anoshin** 32:58 Okay? So I would add basic support for Ntrfs as part of this issue and basic support would be if you change an attribute on the resource
or remove. I don't even know like if you if you
I don't even know how to support that, to be honest, if you, let's say, change the value of the resource attribute. It's okay from the entity perspective. But
if you remove an attribute you remove.
if it's an identifying attribute of an entity, you remove the entity from the Refs.
**Josh Suereth** 33:35 So you.
**Dmitrii Anoshin** 33:36 For like this.
**Josh Suereth** 33:37 The thing you have to do, which is, it's a pain in the ass right now at the
the Ottl interface is kind of awkward as hell from a scripting standpoint. But what you can do is you override all the setters, so you need to go into everywhere where someone's creating a setter on resource, and you override the setter to have advanced logic.
So in the getter setter for the resource in the context object, you can go in and say, You know, anytime someone sets an attribute on resource. I will do some advanced entity work and make sure that if they set an attribute on resource. I blow away the entities. Yeah.
**Dmitrii Anoshin** 34:11 Yeah, that's in implementation details. But what's the like logic behind it? That's my question.
**Josh Suereth** 34:19 If so, mate, if someone.
**Dmitrii Anoshin** 34:21 Go ahead.
If someone removes identifying attribute of an entity from the resource.
we would remove an energy reference.
**Josh Suereth** 34:30 Yes, we can leave all of the attributes, but we have to remove the reference.
**Dmitrii Anoshin** 34:36 Have to remove. Okay, yeah, I see, I'll probably create an issue. And we'll put all of those requirements to
like to try to keep entities
valid essentially, that that would be the goal of that, that basic support. Okay.
**Josh Suereth** 34:55 Yeah, I think I think that I might have that logic in my Java
prototype. By the way, because Java currently allows you to kind of add
the way the way the resource detection thing works. You're actually modifying the same resource. So it has the ability to take a resource and throw raw attributes on it. And so my merge algorithm looks for when raw attributes have overridden entity identity and throws them away.
Where? But if it's a descriptive attribute. It doesn't.
**Dmitrii Anoshin** 35:27 Okay, is it immersed? Or it's in draft somewhere.
**Josh Suereth** 35:30 It's in draft. Yeah, it is this one here.
**Dmitrii Anoshin** 35:34 Okay, I can look into that, and we'll try to align the logic.
**Josh Suereth** 35:39 Yeah, it. I mean, we. We need to fully specify that. I think to to make sure it's clear to everybody, because that is something we don't want to behave differently between implementation.
**Dmitrii Anoshin** 35:48 Yes, but I still don't think we should expose additional api for manipulating entities at this point until we have signal.
**Josh Suereth** 35:58 Yeah, yeah, that's fair. And like, if there were a way to have experimental components of ottl like a a feature flag that adds it. That would make sense. But if not, yeah, I agree we should. We should not expose anything yet.
**Dmitrii Anoshin** 36:09 Okay, I'll look into that. Thank you.
**Josh Suereth** 36:11 Okay, cool. Alright. And then this one, I think
the complex attributes bit. I think this has changed significantly, and this might not be an issue again.
Did that Otep merge?
I'm just gonna take a look over here.
It is still open.
Okay?
All right. We'll just keep that in progress. Next steps.
So we have a bunch of stuff to
to continue making progress here.
we'll start with deciding how entities should be supported by schema files. Right now, inside of schema there is reference to resource
which has transformations on it. If you let me actually pull open the specifications so we can see this. So if we come into the specification
schemas.
file format one dot one. If we look here in terms of changes that are allowed, there's this notion of resources where you can have a sequence of transformations to ensure compatibility.
and the resources Section allows you to change, attribute names from A to B,
I actually think that we should.
Kind of deprecate the resource changes one or this should only apply to raw attributes, and we probably need an entity based change
thing. Where we say this entity with this type, change this attribute name
as something that we allow, but that that's what that task is about is is what this should look like going forward for diffs.
for context. We are in semantic conventions planning to release a 2.0 of this file format that gets rid of the problematic transformations that we actually can't enforce or detect programmatically.
But yeah, I'm curious. Does anyone have thoughts here, or want to take this on or look at this.
Nope, okay, we will leave that one stop sharing again. One sec.
We'll leave that one in to do update resource, model inversion and stability specification.
This is somewhat similar right now, if we look at versioning and stability.
this describes what attributes constitute a breaking change.
And so, right now, under resource, the keys, the key key names of a resource are not allowed to change.
That would be considered breaking for telemetry and for semantic conventions. I think we need to add, the only thing we have to do here is add entity type.
Because if we don't change the key or the type, everything's gravy.
Anyone. I I think we might also be able to with trace. Do we allow key changes. I think we do.
No, we don't. Okay.
yeah. So I think it would be attribute keys. And then the entity type.
**Dmitrii Anoshin** 40:09 Oh!
**Josh Suereth** 40:10 Anyone anyone have thoughts there or or is this still kind of
we don't know what this section is talking about?
**Dmitrii Anoshin** 40:18 Do do we need to do? We need to have a separate entities. Entity refs section here or.
**Josh Suereth** 40:27 That's kind of what I'm saying. Yeah. So underneath, underneath resource, we would say, entity ref, and the type would be something that you're not allowed to change the keys, because the reference references attribute keys. I think that this already covers the keys in the entity refs. The only thing that's missing is the entity type.
**Dmitrii Anoshin** 40:45 But do we need to provide guarantees given that that whole Us. Messages to experimental.
**Josh Suereth** 40:58 If I recall correctly, I mean, we we need to eventually. So this is still stable. So once the message stabilizes.
then then we will have to provide it. This task is just to make sure that we know what we're doing.
The other thing is, if you look in some of our documents we have a mixed status where you would call out.
basically a not stable. Call out that, you know, for the purposes of stability of the experiment. This
type should remain stable.
**Dmitrii Anoshin** 41:32 Okay.
**Josh Suereth** 41:33 If that makes any sense sorry. That was kind of convoluted.
**Dmitrii Anoshin** 41:37 Yeah, I'm just not sure if it's like, if it's still experimental, the whole thing. The whole message entity refs is experimental.
Yeah, do we want to introduce crunchies in stable document.
**Josh Suereth** 41:57 Yes.
**Dmitrii Anoshin** 41:58 Okay.
**Josh Suereth** 41:59 This describes this, describes what stability of that convention looks like in semantic conventions, and we already have it in semantic conventions, in kind of.
**Dmitrii Anoshin** 42:08 I see.
**Josh Suereth** 42:08 Semi-stable ways. So I think I think it. It does make sense. Now, I wouldn't add it as stable in this document. I would add it as as experimental right?
So that we have a chance to stabilize and kind of go through and say, Yeah, let's commit now and mark everything stable, but I would add it to this document.
**Dmitrii Anoshin** 42:28 I can. I can take that too.
**Josh Suereth** 42:30 Okay.
**Dmitrii Anoshin** 42:32 Alright!
**Josh Suereth** 42:39 Cool
Should I move that to in progress, or leave it where it is?
**Dmitrii Anoshin** 42:46 I'll move it once I start working on it, probably, but that's.
**Josh Suereth** 42:51 Resource. Semantic conventions need to be marked stable. This was a Meta bug tracking our work here to be able to start stabilizing semantic conventions, and I think we are now able to start marking things as stable. So service and telemetry SDK are stable. I do want to
get the entity ref stabilize before we actually close this.
**Dmitrii Anoshin** 43:15 Josh, you are still sharing the.
**Josh Suereth** 43:18 Oh, got it? Sorry. Yeah. This one here resource. Semantic conventions need to be marked stable. This is a Meta bug we opened over 2 years ago where we realized we weren't comfortable, stabilizing semantic conventions for resource because we lacked all the controls we've been adding around entity.
so specifically, we want Kate's to be able to stabilize, and I think with what we've done so far, we'll be. We'd be comfortable stabilizing what Kate's is and how it works. But I do. I would like to make sure. Entity Ref is
officially stabilized before we mark this closed, and before we start marking more things. Stable. But
yeah, this this one is now true, and we need outline differences for resource. Semantic entry from other standards like Ecs. This one, I don't think has been done.
I'll keep this on my on my task list. I think this is old enough that it was back when we auto assigned Tc members. So I'll keep that on my task list. And that's something I'll work on next.
okay, one more to do here. This is the notion that we have entity detectors that can work with the environment variable.
We wanted to have a way to provide
environment variables for entity detection. And then, in our proposal for resource, we wanted to have an entity detector that basically reads the environment, looks for entity types and attributes and fills out resource based on it
in a safe way. If I pull up otap.
I'll show the
when it loads
environment variable detector where we want an environment variable that looks something like this
right hotel detected entities. You can define an entity type, and then the attributes of the entity or the identity of the entity. We need to sort out the detail. So we have a set of requirements for this right?
Is anyone interested in working on design for that? Or do we need to finish the prototypes and the Api spec before we can do this work?
**Dmitrii Anoshin** 46:10 Yeah, I think we that's some work to do on the prototype. Yours, new phone number clear.
**Josh Suereth** 46:20 I think you could design this environment variable setup, and how we read the environment variable and and meet this set of requirements independently of the Api prototyping work we're doing.
**Dmitrii Anoshin** 46:31 Okay, go ahead.
**Josh Suereth** 46:33 Go ahead!
**Dmitrii Anoshin** 46:34 I actually volunteered for this one, probably some time ago. Just didn't have
time to get to this. Is it fine to me?
**Josh Suereth** 46:45 Do you want it?
**Dmitrii Anoshin** 46:47 I can. I can take that this one.
**Josh Suereth** 46:49 Okay.
**Dmitrii Anoshin** 46:49 Because I already we discussed that before. I believe.
**Josh Suereth** 46:52 Yep.
Okay.
Cool, then can the collector processors differentiate remote versus local?
This was a question.
**Dmitrii Anoshin** 47:06 You are still not sharing that.
**Josh Suereth** 47:08 Oh, sorry!
Let me come back!
**Dmitrii Anoshin** 47:11 Yeah.
this is an interesting this year.
I'm not sure. Why, why would we need that.
**Josh Suereth** 47:35 I think this was before we got more clarity. This was over a year ago. This is before we had more clarity on what like the notion of having multiple entities and the whether you can attach
data to something or not. I think
today, like we're saying, you would have an entity that would have the host IP address in it. And if you get data from something that has a different IP address, you have an Nc. Conflict. So you don't attach the data
so we could be naive about how we do things.
But yeah, the the question is basically in the collector.
how do I know if things I've discovered about my local environment are things I can attach to data coming in
off a you know, a network port.
**Dmitrii Anoshin** 48:34 Okay, yeah, I understand the ask. But I don't understand why this ask is was made.
**Josh Suereth** 48:42 Simple.
**Dmitrii Anoshin** 48:42 I don't understand the reasons. Anyway, we I can maybe take that figure out why it would be needed, and then I'll
create an issue from it. Put a comment, if this needs to be resolved or not, and we can discuss it. Maybe after that.
**Josh Suereth** 48:59 Yeah, yeah, that sounds good.
And feel free. I think if you need to convert it to issue, feel free, you should be able to edit this and and work on it so.
**Dmitrii Anoshin** 49:09 Sounds good.
**Josh Suereth** 49:10 Oh, you wanted me to sign that to you.
**Dmitrii Anoshin** 49:13 Yeah, please.
**Josh Suereth** 49:14 Okay.
**Dmitrii Anoshin** 49:19 Thank you.
**Josh Suereth** 49:21 All right, decide if we need to record nil attributes in the Id. I think we decided no to this. I believe right.
This may be important to indicate the fact attribute was required by the producer, was not able to record the value. This is oh, right! This is from your your prototype, Dimitri. So
if we want to attach
descriptive attributes to an entity, but we couldn't figure out which one it was. We just know how to describe it? Does it make sense for us to produce an entity with nil id.
and then say, attach these descriptors to it.
**Dmitrii Anoshin** 49:54 I believe we decided that it's invalid entity if it live on the, on the wire, on the protocol.
But inside the collector it's okay, to pass it between the between the components.
**Josh Suereth** 50:10 Yeah. And I think if we design an Api, we can actually design an Api where you just instead of registering and saying, Hey, I have an entity, we could say, add a description to an existing entity.
You know what I mean like, hey? Here's an entity type. I have something that describes it. So I can register descriptive attributes without having to know the identity of the entity I'm describing.
**Dmitrii Anoshin** 50:31 Yeah, that that's that was the part of my prototype. And but it doesn't leave the collector. That that's my point. I'm not sure if we need to make it like, if we need need to make it valid entity
that can be sent over the wire. I don't believe so.
**Josh Suereth** 50:51 Yeah.
**Dmitrii Anoshin** 50:52 Anyway, I'll take that as well, and.
**Josh Suereth** 51:08 To scripted attributes to existing entities website if needed for the collector.
We don't think this needs formal specification.
If entities of this type speak to the collector. It's a bug.
Does that.
**Dmitrii Anoshin** 51:37 That sounds good.
Sounds visible. Yes.
**Josh Suereth** 51:39 Alright. So I actually might move this to done. Then I don't know if we need to do anything.
**Dmitrii Anoshin** 51:44 Okay.
**Josh Suereth** 51:45 Yeah.
So that's decide if we'll move that over to done alright, and
we're running out of time. And I think that's totally fine entity, semantic conventions for hosts.
I believe this was something you were working on with the system. Simcop. Is that correct?
**Dmitrii Anoshin** 52:06 That's right. Yes.
**Josh Suereth** 52:08 Okay, so I think we're gonna defer this to the some that some comp completely. Yep.
we'll move on.
And what do we have decide if service and service instance are different entities. I think we can defer this for a bit right now. The way it is inside of semantic conventions is service has service instance Id in it.
It's just it feels a little weird right? Is there a thing with a service that has a name where you have entities that are instances of a service in it.
Yeah, I think we can defer that for a bit. That. That's not urgent.
And then add Kate's pod, Id. Or IP attribute.
What? Why is this one in here?
Please take a look.
Been using this field as a resource attribute for many years and had no issues.
The concept of entities. Oh, this is where they want it to be. A descriptive attribute.
Got it
so we moved it in here.
I think this should just be unblocked right? This is no long. They no longer need us for this. Just mark Kate's pod, IP, and descriptive attribute.
**Dmitrii Anoshin** 53:39 Yep.
**Josh Suereth** 53:40 Okay, yeah.
okay, cool and then I'm gonna move that to done for us.
But it's still a to do for Kate Semkoff. Alright beautiful!
I think that's it for our phase. One work.
Thanks everybody. Is there anything else anyone would discuss before we call it
cool? I will get the Api SDK specification up to date. I will get my prototype to match it, and I will send that out to all of y'all. So thank you so much for the discussion.
See you, in 2 weeks.
**Tyler Yahn** 54:47 Thanks. Josh, bye.
**Josh Suereth** 54:49 See ya.
