SIG: Specification SIG
Date: 2025-07-08
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:56 Hi folks.
Tyler Yahn 00:02:03 Hey!
Josh Suereth 00:02:40 Hey? Everybody sorry. Can folks can folks hear me now?
Austin Parker 00:03:57 Yeah, okay.
Armin (Dynatrace) 00:03:58 Yep.
Josh Suereth 00:03:59 Cool, I think, we're starting a new rotation thing on the Tc, so I think it's my turn to do the Sig meeting today. So apologies for that.
I was having some audio issues with my laptop. So I couldn't actually hear anyone. All right, let's get started. So yeah, Robert, do you want to start.
Robert Pająk 00:04:26 Yes, you can share. I want to make it weak because we have a lot of agenda items. So basically, there are just 3 Prs, that I would like you guys to review 1st is regarding anon values and the case insensitivity. So basically, it's about especially consistency. For example, bullying by using Nvr. That is already case insensitive. And I also check that. For example, in Go. This is the thing of SDK, which, already doing second, is a follow up regarding the primit use compatibility. So this adds, basically the auto scope attributes to non exporters. And the 3rd one is just an just a refinement and basically improving, clarifying the concurrency safety description of on end meet for log record processor.
And I think that's it. If anyone has time, I just I just welcome, and I'm happy to accept any feedback.
I think, Josh, you can follow up here.
Carlos Alberto Cortez 00:05:31 I have a comment. By the way, the 1st item, yeah, if you could open it Josh could be great.
That one is a small clarification, or you can think of it as a clarification. But I would like all maintainers to take a look to make sure that the embar ha! Handling is, you know, aligned with this.
So please take a look. If you're a Maintainer, or even an approver, it would be great. Really, you know. Yeah, I think it's this is a good change. But yeah, we we need just double confirmation. That's all.
Trask Stalnaker 00:06:06 What does declarative? How does declarative config handle this.
Jack Berg 00:06:14 So enumerations in declarative config because we use Json schema. And so when you say that a particular type is an enumeration, you list out the exact set of string values. It's a string type with a allowed set of string values. And so.
you know, then so like it depends. There's like an interaction between Json schema, which is just like, you know, string values which are case sensitive, therefore, and the language specific code generation of the types that correspond to the enum from Json Schema, and so like in Java. We use this gradle tool that you know, interprets the Json schema and spits out all of the the, the classes and enumes corresponding to all those types. And what do we do for like a new values? I think.
Trask Stalnaker 00:07:21 I think you've answered the my question already, which is that the Json schema is going to only allow case sensitive values.
Jack Berg 00:07:32 But it's more complicated than that, because, like, there's, there's other things at play right? So like, ultimately, the thing that's going to parse the Yaml. To those Java. The generated Java bindings is Jackson.
and so Jackson, like I think it's probably configurable whether enums are case sensitive or not.
I'm in favor of this change. Personally.
Trask Stalnaker 00:08:01 Okay, cool. Yeah. I wanted to make sure. It aligned with declarative config, was all.
Carlos Alberto Cortez 00:08:08 Yeah, I guess that the question that I would have and we can discuss that offline for sure is.
what if like, would be, would it be a problem if configuration handling cannot guarantee cases, insuccessitiveness.
or or what do we do here? You know, if they it is one and the configuration. One. They defer what we would. What what do we do? In that case, you know.
Robert Pająk 00:08:29 I just want to call out that it's already a problem for Boolean values.
Carlos Alberto Cortez 00:08:33 Right?
So yeah, I think it's a, it's a yeah. We have to compromise, and that's my opinion. But let's just goes out of line.
Thank you.
Josh Suereth 00:08:46 Cool.
I will say just real quick as we move on. Any kind of case, and sensitivity always makes me nervous.
So I'm I'm glad that we're fully specifying what we do here. I like it, anyway.
this one's going to be 15 min. I just want to check quick to make sure we have time. Yeah, it looks good. Okay for the entity specification. Pr, I mentioned this last time and we got some reviews for context, what we're trying to do is expand resource, detection and resources and open telemetry for you to be able to talk about bundles of things called an entity. Right? So this is like I can report a host that I run on. I can report a browser session that I'm talking about. I can talk about a service right in semantic conventions. We already have these as groups of things that you can report.
We have a specification Pr for what this would look like, and a lot of the feedback led to us to advance some topics of discussion that we had in the Entity Sig a bit sooner than initially planned, which is what we were proposing as an SDK actually makes sense as an Api.
So I'm going to walk you through a little bit of the details. Here I put it in the notes, and then you, there's a bunch of links here. There's a Java prototype of this where it is an extension Api for a resource provider and a way of emitting entities against that resource, and saying, I want to attach this entity and say, this resource is about a host. This resource is about a service.
There's an end to end test which shows how it works end to end as an SDK with programmatic configuration.
I have a to do that. I haven't had time to do to wire this into the configuration based examples.
But that's that's that's more to do in prototyping. Anyway. The background for this we have 2 Oteps, I think, are important, one which is about resource and SDK changes we were planning that is approved and merged.
one that is currently in kind of discussion mode that was looking for prototypes which we now have some of for allowing resource modification to enable the client and browser sync. And thank you, Ted, for putting that one together at a high level. What we're proposing for the specification is a piece of the second Otep.
Okay.
resource detectors would have a change. What happens now is you can still register resource detection at Startup. But what a resource detector does is it grabs the resource from the resource provider.
and it attaches entities to it right? So instead of it, like creating a resource and calling merge across all resources, and that kind of shenanigans that that exist in the spec today.
A resource detector just grabs the resource provider, emits an entity.
a resource provider allows you to attach an entity against the current resource or update the description of entities. So, for example, if the IP address of the host changes. I can actually report that because IP address is considered a descriptive attribute not identifying. And so I can safely update the IP address. I'm reporting another example, and this is the the one of the critical ones, for, like browser or client is, if the session changes.
I can have something that actually watches for session changes and reports it in the SDK, and it will update the resource so that it is describing the appropriate session as session changes throughout the lifetime of that. SDK, okay, if you if you want to see a code example, I can pull that up. But that's that's basically the main things. The other change here is to the signal providers. This is trace, provider, tracer, provider, logger, provider, meter, provider.
Instead of registering a single static resource at Startup, you actually register the SDK resource provider, who then gives access to the resource. And if in this Otep, which is not part of the current, prototypes.
may extend into actually sending events to the other pieces of the SDK, saying, Hey, the resource has changed.
Open questions are right now in the prototype.
I don't know why that's highlighted. But in the current prototype on resource change.
nothing changes to how we are collecting or reporting data. All that happens is when we go to export signals and we look up the current resource to attach. We just ask the resource provider what is the current thing we should report against. So we're not stopping metrics. We're not cutting spans in half. We're not doing any of that. We're just reporting against the current resource which allows us to basically update descriptive attributes. That's what the current specification proposal has. That is an open question. We're going to be exploring more in prototypes as this goes through.
I wanted to open this up for some discussion.
Let's see, I took about 5 min for that.
Want to open this for some discussion, some thoughts, and just get people aware of what's going on with the Spec. Pr, what we're doing, the state of the prototyping I especially want to hear from SDK maintainers.
So with that I'll open the floor.
Go ahead, Jen.
Jack Berg 00:14:06 Okay? So you got a resource provider. And you now have like this, initialization ordering problem resource provider has to be initialized. First, st because it's going to be passed to the other providers, the meter, provider, tracer, provider, logger, provider during instantiation and you know, once all these things are sort of configured. They're provided to instrumentation libraries that go and do things like create spans and meters and instruments and all those things that we know about. And now we're saying that, you know, providing entities is is a new form of instrumentation.
right? So just like, you know, an instrumentation may be responsible for emitting spans, or recording to metrics, or emitting logs and instrumentation. You know its main purpose might be to just, you know, emit entity information.
I think that sort of aligns with this question that we've had in Java for a long time is like, what is the nature of resource? Detectors? They kind of seem like instrumentation in some sense. But you know they don't have Api surface area. You know, they've they've up to this point been only been limited to SDK functionality. So that that seems like a good clarification. What do you think about race conditions?
Right? So you know, you've got the resource provider, meter, provider, tracer, provider, all being initialized and passed to passed to instrumentation, and those instrumentations are sometimes emitting entity information using the the resource provider Api, and that entity information is also ultimately going to get merged and manifest on the Otlp payloads that are being emitted. And so like what happens if a you know a different instrumentation. Library immediately starts emitting spans or metrics or logs before one of the instrumentation libraries that is responsible for emitting entity. Information has an opportunity to emit that entity information.
It seems like mutability is is going to be quite common.
Josh Suereth 00:16:15 Yes, yeah, that is actually one of the concerns, I think, listed in the Pr the current proposal is effectively to solve that the same way we do today, where you have resource detectors that are configured as part of the the SDK startup. So I'm actually planning to rely on the configuration Sig here. So those resource detectors that you create a name.
Would actually be run on the resource provider before you finish instantiating tracer, provider and meter provider.
Right? So yes, and we have a dependency problem here, where we might not have everything kind of up and running. But the idea would be, we in the configuration of the SDK. Try to make it so that resource detection is run 1st before anything else.
The same way we do today by requiring resource to be fully instantiated before an SDK can be created. We've effectively forced resource detection to happen before any of the other things happen in today's world. Right?
So the difference here is We. We rely on that, and we allow it to mutate. And so yes, there's a foot gun. If you don't register resource detectors as resource detectors.
Jack Berg 00:17:28 Right? Okay? So a resource detector, when you implement one of these things, there's kind of 2 things you're implementing. There's you know this.
you know, initialization phase, which is invoked extremely early in the application's lifecycle, and, you know, is provides the set of, you know, attributes and entities that contribute to the the resource and entities in the initialization state of the SDK.
And then there's this sort of secondary thing that you maybe it's optional or something like that. But in a resource detector might also be interested in getting access to this resource Provider Api and using it to update the entity information.
But you know it's it's probably the case that not all resource detectors would be interested in updating their entity information. But it's available.
Josh Suereth 00:18:22 Yeah, I think I'm not muted. Okay, yeah, that's that's so the discussion we're having, like again, we we have to sort this all out and make sure it's written well. But the discussion we had in the ntig is basically resource. Detectors happen at Startup.
and if a resource detector wants to like, watch something and report on change. It would register and control its own lifecycle, and it would have access to the resource provider or the resource to report those entities as it goes on. But we would kind of instantiate resource detectors in that SDK config, so there'd be an SDK thing where you could register a resource detector.
The instrumentation itself is kind of something we can generate as part of our Api generate it the same way we do in weaver and semantic conventions, and that sort of thing. I might be explaining this in confusing way. There's a couple hands, Daniel. You had your hand up first, st and then, Ted, I believe I don't know if you want to jump in here, but feel free.
Daniel Dyla (Dynatrace) 00:19:19 Yeah, I I raised, lowered, and then raised again. I I think what you said addressed my concern mostly, which is why I originally lowered it. But then.
thinking about it a little bit more, I think there's an important distinction between entities which are required at application, startup and entities which are not so. For example, you want to detect, like the host entity before any telemetry is emitted, because.
all telemetry emitted from the host should be attached to that host. But you could have an entity added later, like call it a user session or something like that. I'm not sure which isn't necessarily required at Startup. And right now we don't have any way to distinguish between an entity that the exporter should wait for resolution and an entity that is fine to not be created or resolved before the 1st export.
it. This has been a problem in, in, in resource, at least for Js as well, because we don't have any way to wait synchronously on stuff. So we have to just hold exports for it.
But it may be worth adding that distinction to the to the detection. Api. If we yeah, only if we, if we actually have a use case for it, it may, it may be a a false use case. But what Jack said made me think of that.
Ted Young 00:21:14 Yeah, to to that point. When we last took a pass at this like 2 years ago.
One of the things I had in that proposal at the time was like a validator to to for exactly this point where you could give it, you know an allow list, or like a deny list of keys.
And then, at a certain point, call freeze and saying like, if anyone attempts to update any of these things after freeze. Then, you know, you can choose how you want to deal with it. A warning or whatnot, but some kind of mechanism where the ability to now be flexible about these things is not totally wrecking. The original reason why resources were immutable. In the 1st place, which was basically to avoid handing this foot gun out to people around, you know.
resource, resolution, and all of that stuff that happens around startup. So that was actually part of an earlier design was like a validator specifically to.
to, to help, at least warn you that you had done something like that.
Josh Suereth 00:22:28 I like that. One thing I want to call out in the prototype and in the spec, the way it's written you are allowed to add a resource to or sorry added entity to resource. Resource. Entities have identities and descriptions.
Once in a resource of a particular type like host service, SDK. Browser, client session. Whatever. Once a single one of a type is added that identity is locked, you actually can't replace that identity. You can update the description part of the entity when you emit, but if you try to emit one with a different identity, you are blocked, unless you explicitly call, remove.
and remove is not part of the initial specification.
That was just part of the prototype. So that that's actually how how the spec has worked to kind of alleviate some of those concerns.
It's a different take than than the the like freeze idea. I think we should explore both because I like what you're suggesting there. But yeah, like, I agree, like, we need a way to make sure that these things are somewhat stable, that we get the things in early and that we have some way to know that you have like startup concerns. That's that is the biggest concern. I think, with this proposal that we need to work through and make sure we're comfortable with what we have. I can show you what we have. I recommend looking into it. I want to give about 2 more minutes for discussion before we're out of time box. So with that, is there anything else you want to say, or does it any anyone else. I think Robert had their hand up like feel free.
Ted Young 00:23:58 Yeah, I do. Wanna just flag something here, Josh, which is like it feels like I'm I'm a little nervous around this, going directly into the spec as like a kind of partially worked out thing like we were in the process of making. We had an otep like we're in the process of making a couple of different prototypes against that Otep and usually we want to kind of like prototype and like sort out all of these problems before we hit the spec, so that like maintainers don't don't face a lot of thrash. I definitely don't want to slow down work on this. That's not what I'm proposing, but I'm just maybe gently just raising the point of process. Should we be like continuing to prototype against an Otep?
Here, and kind of like bang through some of these remaining issues in code. Before adding this to the spec, rather than adding this to the spec as a way to force people, to, to.
Josh Suereth 00:25:00 Yeah, I.
Ted Young 00:25:01 Typing on it.
Josh Suereth 00:25:02 This is a draft pr to the spec.
This is not a a like I. I am not planning to ask for reviews to approve this to the spec. What I'm looking for is feedback on the direction. Because I think you you're calling out a good point of our initial prototype called out the use. So our initial Otep called out this use case as a thing that was out of scope for the Otep, and what we would provide, which was the ability to register entities and change description only right?
And so the current way the spec is worded.
It allows changing the description, but it also allows changing entity or adding new entities in the current prototype and the current way the spec is worded. So it did expand on the Otep. So if we want a full Otep on that totally agree, I do think that we need to finish the prototyping before this goes through. The reason I want discussion. Here is, you see how big of a change this is and how impacting. I want people aware of it. I want people to have. Input. And I want us to kind of agree on the direction.
no matter what we do. If you'd like, I think we should revive your Otep we either need to cut some scope from it, because I don't think the current spec Pr will have that much scope, or we just need to fully prototype everything in your Otep which includes like sending change notifications. Right?
And then, yeah, and then go from there. So so I'm fine either way. The most important thing I want, though, is the discussion around the direction and what what we're doing to happen.
Ted Young 00:26:29 Yeah, I'm happy to jump back in. I was kind of waiting for people to get interested in this again. So it sounds like there is. So I think that's great. I think we should maybe do more of it. Just because I found working on that Otep. Some of those like later problems like on change started to influence my Api design decisions. And I'm happy to talk about that in the entities. Sig. But
Josh Suereth 00:26:55 And.
Ted Young 00:26:56 Prs.
Josh Suereth 00:26:58 Absolutely.
Ted Young 00:26:58 Cool.
Josh Suereth 00:26:59 From from the entities, from the entities working group. Basically, we tried to make an SDK only change. And the the big thing we learned here is, we think this should be an Api. What I'm hearing from everyone is. No one disagrees that the Api doesn't make sense. From what I hear like this is a piece of instrumentation, the way like, for from Jack's point.
reporting on entities on a resource, feels like instrumentation, the same way, reporting on spans and reporting metrics feels like instrumentation.
So having an Api makes sense from that standpoint.
Ted Young 00:27:30 Yes.
Josh Suereth 00:27:30 If anyone has concerns with that, that's the most important thing for us to decide today, and then we'll move from there cool.
Ted Young 00:27:39 Yeah, sounds, good.
Josh Suereth 00:27:43 All right. Thank you. Everyone for that discussion. Move on, Adriel. Do you want to talk about the spec being merged? And next suggestions prototypes in the libraries.
Adriel Perkins 00:27:58 Yes, sure. Thank you, Carlos, for merging that this morning.
It was really it was originally, and asked to have emerged. But then you saw it and merged it. So that was fantastic. I appreciate the feedback everyone gave for that. I I guess this question is is twofold one like the last, the 1st iteration of the the spec change we found a a clear, distinct thing that we wanted to add as a next step. So breaking out, you know the the spec changes into small bite. Size chunks.
We've done that. I was wondering if there are anything. If there's anything else that someone can think of, that they might want to see specifically in a spec for a next step or and or what the the next step would be with regards to I think. Well, sorry. Let me rephrase the the second portion of that. I've not had enough coffee this morning. The second portion is, I think, the next step for me is to actually help get some of those changes into the actual libraries. We have a the go prototype that robert opened up. Thank you for that. I think it'd be great to actually get that through the door, and then same with the python prototype, and then hopefully get some additional pro prototypes through the door actually implemented into the various libraries. That's kind of my thinking of what the next steps were, but I wanted to make sure there were no additional spec changes that anyone could think of that that we want to address.
Liudmila Molkova 00:29:34 Hidra. I have a comment
Adriel Perkins 00:29:36 Yes.
Liudmila Molkova 00:29:37 Since since you're asking thanks for asking.
there is a piece in semantic conventions where we have a cli spans. But we didn't describe how context propagation works across processes.
It could be useful to document it there and then. I think python instrumentation for the cli framework they have would also benefit from actual context propagation.
If you are interested in working on this, that would be wonderful.
Adriel Perkins 00:30:12 Yeah, absolutely absolutely. Could you send me the the links to what you're referring to? Specifically.
Liudmila Molkova 00:30:18 Yeah. Will do. Thanks.
Adriel Perkins 00:30:21 Awesome. Thank you.
Josh Suereth 00:30:28 Okay, cool.
If that's all right, we'll move on to the next one blinku measurement processor next steps.
Lukasz Gut 00:30:40 Alright, hey? Everyone So probably most of you are aware at this point of this initiative. And we wanna introduce measurement processor concept. That's kind of the counterpart to spans processor and log record processor.
So last time we chatted about this here, we didn't have any proof of concepts. Now we do. There is one in Python that basically follows the spec. I opened it. It's in a draft state, and there is also one in rust. It doesn't fully follow the spec. I'm not sure if the author was aware of our initiative, but I feel like it could be pretty easily adapted.
I've given it a quick look, and I think Joshua also recently dropped a comment. I think last week that if I'm reading the comment correctly that he believes we should try and move forward with the with the, with the spec change, and actually include the measurement processor. So the base question I have for the group here is, do we need more Pocs? Or should we merge it as is in? I suppose, Alpha, not not sure in what the status I I probably need some help from you.
yeah. And yeah, what? What would be the next? The next step to make it a reality.
Jack Berg 00:32:07 Yeah. So from my perspective, this has meet the met, the, you know the strict requirement from a a Poc standpoint. And you know, even though, that we've kind of gone back and forth in the past about you know what constitutes a Poc. And we said, like, you know, hey? Does it have to be a like a a Pr with that has a corresponding artifact that users can actually consume in their code?
Or, you know is is just the Pr sufficient. And we've said, you know in the past that you know, we've made the case that just the Pr should be sufficient in cases. And so I think this is an acceptable Poc. I'd like to hear from the python Maintainers, and you know, get some confirmation that you know they agree with this approach that it fits in with you know their their model for how the SDK functions the python metrics SDK functions, and then so like setting that aside, then the question is like, Okay, do the other spec maintainers and the other SDK authors in here in this group? Do they?
Does it make sense to them? Is the design right? Does it seem useful? Do they see a way that they could evolve their sdks to incorporate this concept. And so that's like the subjective piece. I think you've you've probably met the objective criteria and you know, if I have some time. I'm a maintainer of the the Java SDK. You know. I don't have time to prototype this right this moment, but you know I'll review it on. You know that sort of subjective criteria.
Carlos Alberto Cortez 00:33:43 Yeah. Also, I would like to ask Robert and the go Maintainers. I know that. You started a prototype, but you didn't have cycles to grab that up. But it would be great that you review that the prototype itself. It would be great, you know.
Robert Pająk 00:33:59 So from my perspective, I actually tried to make a prototype, but I just failed and dropped after, after like a few hours of trying doing it. And I know Luke also tried doing it in go. And basically, it may be connected with the complicated internal go. So from my perspective, I don't think it's a blocker.
but probably it will be good if other autogo maintainers which were involved in basically implementing most of the parts of the metric SDK will double check it.
Carlos Alberto Cortez 00:34:31 Yeah, I don't think you have to implement at this point an extra prototype. But with your experience trying to work on that.
Robert Pająk 00:34:39 Whether you think that the current approach would be a blocker. I just said for yourself, it's not a blocker.
Think it's a booker? Yeah.
Carlos Alberto Cortez 00:34:45 Good.
jmacdonald 00:34:50 I thought I'd add the reason why this maybe reappeared. And the reason why I put a comment on the original Pr. This week was the collector. Sig has been eager to adopt this type of functionality. It's become pretty critical. They want to be able to inject metadata like tenant id or pipeline name, or anything along those lines that comes in on the receiver and is put in the context throughout the pipeline. So I should be able to count, you know. Subdivide my otlp exporters by tenant Id, and get metrics on that. And this is how we want to do that. If we don't move this forward quickly, I think for the collector, Sig, they're gonna just do something that's not very Api or hotel compliant, and that would be a a loss. So let's let's do this. I also. I put a link to the Poc that I did for myself over a year ago. It's not exactly the the current spec, but it gives me some confidence that this can be implemented. It is a question how to get performance out of the go SDK for me, which is what I was facing there, and I I don't know what to do. Exactly, so I'll leave that to the go go if go, Sig.
that's all. Thank you.
Josh Suereth 00:35:58 Yeah, I I just wanna add, I think if you're going to add anything to your Poc, I I do think the Poc is enough to for us to kind of discuss the the spec. Pr. But I before stabilization for sure, and even now it's probably worth doing some benchmarks and showing the benchmarks of like, what's the cost of this feature? And are we able to implement it efficiently?
I'm personally also supportive of this change? I think we need a way to interact with context. The previous proposals we had for interacting with context were different than other signals. So I think this is a good path forward. But let's just make sure we can do that efficiently with the implementations we have.
Jack Berg 00:36:37 Would would the lack of ability to do it efficiently, and I know efficiently, is going to be like a subjective criteria in here. But to me I I've kind of thought about this, and you know, even if you have to pay a little extra performance tax to do this, I still think we need this feature.
Josh Suereth 00:36:56 Oh, I I mean the 0 cost performance task. Like I like I, we should make sure this feature doesn't cause performance regressions.
Jack Berg 00:37:04 Okay.
Josh Suereth 00:37:05 By implementing it.
and then that the cost you pay is relevant to your usage of it. Right? That's all that. That would be my main concern. Yeah.
jmacdonald 00:37:18 I I think you're right. It's subjective. We shouldn't be too strict about it. And when a user comes and says, this is a problem for me with performance. We we often go to this conversation about bound instruments. And I just wanna say it's it's a tricky one, because even with bound instrument. You're gonna want this feature. And the cost is gonna still be important. And you're still gonna have to do something dynamic. That's gonna cost you. So I think the biggest question, Josh, you put it well is that we wanna make sure that when you turn off instrumentation, or you're not using that instrument that the measurement processor somehow is not super expensive. Ideally, it's low cost, and that's what I would look for in the the final sort of stabilizing. You know. Change here.
Josh Suereth 00:38:00 Yep.
yeah. And then the other benefit of having the benchmarks now is, you can show them to people, and you stabilize. So again, I don't think it's a blocker for merging the spec. Pr. I think I think when we stabilize we should make sure we can show people the expense of the feature, that's all. And yeah, like to Jack's point.
I don't actually see this as a blocker, right? I see it as a thing I see having the benchmark as a blocker. I don't think the number is going to matter as much as whether or not we caused a regression to all metrics with this.
Yeah.
Jack Berg 00:38:32 So the the benchmarks are context to, you know, for for users to help decide whether they want to use this. 1. 1 more thing that, Blinky, I think you mentioned that, I think was unaddressed in this conversation is like, Hey, what's what's the status of how we merge this to the spec, you know, assuming that it gets the required approvals and so the the spec has a maturity model that allows different sections of the spec within a single document to be at different levels of maturity. And so like, for example, the metrics SDK document. The maturity is is marked as stable, except where otherwise noted.
And you know so this would be one of these exceptional, or, you know, sections that is, falls in the criteria of, except where otherwise noted. And so we would merge this as maturity level in development. That's the you know, the designation we've been using for this type of thing, and then the process to getting it to stable would be, you know, getting more prototypes in a variety of languages. And then, you know, after we've had a chance to solicit feedback about those prototypes. Then we can consider changing it from in development to stable.
Lukasz Gut 00:39:53 Alright yeah, in the in the Pr. I think it's already marked as status in development that particular section. So if if I'm reading the room correctly, we wanna proceed and merge it. And basically figure out the rest like benchmarks and more prototypes as we go for for stabilization of this of this Api.
Jack Berg 00:40:20 Josh, just a point of clarification. So were you thinking the benchmarks are the existence of benchmarks? Are they a blocker? For you know, merging this this Pr, and it's in development status. Or do you think that that's a blocker for a future stabilization effort.
Josh Suereth 00:40:34 I think that's just a balker for stabilization, not for merging. Pr, yeah.
the cause. I don't think it changes the shape of what you're proposing at all. It's just a can we say that? Hey? Here's what the overhead is, that's all. Yeah.
Jack Berg 00:40:47 Thanks.
Lukasz Gut 00:40:49 Alright. So yeah. And and ask for me is for you to and guys to maybe give it another look. If you feel like there is anything missing. Let me know. If not, maybe we can get that merged
Josh Suereth 00:41:04 Cool.
All right, let's move on. We have 20 min left in 15 min of stated topic, which I think is always a bit expanded. So, Arthur, do you want to talk about Prometheus? Related Prs, do you want to open any of these.
Arthur Silva Sens 00:41:21 I don't think it's necessary, actually, but I'll try to make it quicker than 5 min.
with Tldr we, the permitive sig, came up with 2 spec changes we already discussed. There's a lot of discussion, Api already, and some approvals.
We're just wondering what's next. If we if there's anything that we missed somehow, that we need to add to the Pr.
Before it gets it get merged.
Josh Suereth 00:41:52 I, I think you just need more specification approvers. So yeah, th, this is the right place to basically say, Hey, we're trying to make these changes. Here's what we're doing. Here's the context. And then we just need to get more people to review. So it's good to know that the Sig has reviewed it. And yeah, I think at this point, just those of us who are spec sponsors or spec maintainers should be reviewing this and accepting it cool.
Arthur Silva Sens 00:42:17 Alright, then, I'll wait for you. No pressure at all.
Josh Suereth 00:42:22 No problem I will say, I think the anything that comes out near like mid June.
We move very slowly around holiday times, and and people taking summer vacations. So just that that also is a thing. All right, cool this one. I expect to take more than 10 min with Miller. Complex attributes.
Liudmila Molkova 00:42:44 Yay, so I want to continue. The thing was started last time. Josh, would you mind if I share.
Josh Suereth 00:42:51 Yeah, go for it.
Liudmila Molkova 00:42:53 Yes.
Josh Suereth 00:42:53 Sorry I don't mind. Yes, please share.
It's always the difficult.
Yeah.
Liudmila Molkova 00:43:00 So when I ask my kid if he is sure about something, he always says, no.
which means, yes, but anyway.
okay. So last time we discussed extended attributes on everything. We got some feedback from Dan. Dan, I hope you're still here. I want to continue the the conversation.
So I think there are 2 points you've raised.
Sorry if I forgot something so the 1st one is that we don't have a real use case for anything, for the complex attributes on, let's say, metrics or resources entities instrumentation scope. The second is that it feels wrong to allow something, and then immediately document that is not recommended to be used.
I kind of want to talk about use cases which we don't have in open telemetry instrumentations or semantic conventions.
but I can easily imagine use cases like for end users.
Daniel Dyla (Dynatrace) 00:44:11 Yeah, I As far as the use cases go. I don't.
I don't think that I ever made the statement that there aren't used cases for for metrics. I don't know what they would be and for for entities. I'm much more worried about the entity identity attributes, but that's more to do with efficiency than like than anything else like. Of of course you could think of a way to use them. But is that trade off worth it.
For entity identity. I don't think efficiency is a massive concern.
beyond how it affects metric identity.
Liudmila Molkova 00:44:56 Yeah.
Daniel Dyla (Dynatrace) 00:44:58 Doesn't.
Liudmila Molkova 00:44:58 Metric.
Daniel Dyla (Dynatrace) 00:44:59 Are often in tight loops.
Liudmila Molkova 00:45:02 They are. But it's the question of whether people who implement those metrics care about that. The the performance, like I can imagine. First.st Let's say, address here the Ci CD metrics about pull requests. They are rare. Even the cardinality is not a big deal. So if you can add, if you want to add some standard information about Github pull request.
why wouldn't you add it? Right? You you can. It could be useful to someone, or, let's say, the container manifest right? It can be quite interesting and nasty.
and it's not really flattenable. It's an array, but it's local cardinality. And if you want to measure something about the containers. If performance is not a huge concern, go for it, why not?
It's not even mutable.
Daniel Dyla (Dynatrace) 00:46:14 Yeah, I mean, as I said it, I I don't. I don't contest that there are use cases where it's useful. I would say that there are alternative that I I think you would be able to find alternatives. Although I'm happy to be proven wrong. If that's the case.
I still feel the second argument strongly, which is that adding an Api and immediately telling people not to use it just feels wrong. Okay, there's something about that. My, my brain just can't let that go.
And yeah, I guess I just don't.
I?
I don't have specific reasons to block this, which is for the record. Why, I haven't blocked it.
I just am also not sold on it.
So that's why I haven't approved it.
And I yeah, I I've been trying to change my mind on this, and I just can't.
Liudmila Molkova 00:47:22 Yeah, I I don't want to push it to approve. I wanna discuss things, and maybe hear other people thoughts or just talk through the concerns. So no, no, no pressure.
Daniel Dyla (Dynatrace) 00:47:36 I'm very worried about that. So the fact that there are legitimate use cases, you know, is.
is, you know, fine. I accept that I think it is possible that there are workarounds where they're not required, and then, I think, providing these Apis even telling people not to use them.
I think the the risk is that people who don't understand the implications shoot themselves in the foot constantly.
Austin Parker 00:48:10 Can I add.
Daniel Dyla (Dynatrace) 00:48:11 We already fight cardinality issues. And when you have deeply nested structures, I think you're you're very likely to run into additional cardinality issues.
I?
Yeah, I mean, it's like I said, I, I'm not here to block it. I just don't.
I just yeah. I'm not convinced either.
Austin Parker 00:48:37 Just to throw something out there like I think we have to kind of walk the line between a yes, highly possible that someone will find a use for nested attributes on, or complex attributes on any of these things. Right?
Definitely, if you build it, they will come. On the other hand, I think we risk there's like 3 things we risk right? One is that One is that I think we would like to think that we have a fairly good idea of the capabilities and shapes of databases that people use for telemetry, and the capabilities of those databases and the theoretical capabilities of those databases.
and why? And we should in some we should bias a little bit towards like what is feasible in terms of ingest and query, right?
Like giving people some the ability to do something that everyone turns around says that's cute. But we're not gonna support it because of XY, and Z. Reasons, doesn't feel very useful. So that's you know.
that's 1 problem.
The the second problem is.
I see the counterpoint of like, okay. So if we don't do it. If we don't let people do it, and they need it, then they will come up with something that is worse.
Which people have done right like if we don't. If we there there have been instances where people come up with like hacky workarounds, the things that they don't like and those hacky workarounds usually wind up, being like suboptimal.
And so I think that's a something to consider right like, if we don't let people do it, we need to have a really good reason why so? Which leads me to my 3rd point, which is.
maybe the answer here is like something else, right? Like, maybe I don't know.
Maybe it's we need some sort of canonical pointer type that allows us to say, Hey, the attributes for this are over here.
Maybe it's I don't know. I don't want to like solutionize. But if we're worried that, you know.
if we're worried about this, then maybe the answer is, you know. Then we shouldn't dismiss our worry. But we should think about like, do we need to solve it in this specific way?
Trask.
Trask Stalnaker 00:51:35 Yeah. So what my main motivation for wanting this is very specific to Java, or strongly typed languages where I want to have a single attribute type.
Grouping that we use everywhere.
That's very important to me. Because without that we end up having to do some kind of hacky feeling things, or we expose the complex attributes everywhere. But we drop them from those other signals.
So in I think there's a very strong reason ergonomically, to support this in strongly typed languages.
I'm completely fine with dynamically and coming back.
Daniel Dyla (Dynatrace) 00:52:42 Press here, cutting in and out.
Liudmila Molkova 00:52:46 We've heard you're completely fine, but haven't heard.
Bye find it.
Trask Stalnaker 00:52:49 Sorry my Internet is horrible.
dynamically typed language is not implementing it. For now until we, you know, making it a May, and that's what we tried to do originally in this Pr was to kind of bridge. Those allow that flexibility.
But then we got pushed back from some people who wanted it consistently, so I don't know if I missed last week's discussion. So I'm not sure if that's an option to go back to if that address even addresses your concerns. Daniel.
Daniel Dyla (Dynatrace) 00:53:30 People who wanted it consistently for the sake of consistency, or people who had a particular use case for it that wanted it available everywhere.
Trask Stalnaker 00:53:40 No, I think it was the pushback came originally from tea grin that he wanted it to be the same across all signals when we we tried to split that. And we can, you know, go back to the way it was previously. If that I I'm personally totally fine. With that we can always route make that we can always ha require that of dynamically typed languages in the future. If there's stronger arguments.
jmacdonald 00:54:22 I wanted to go back to what Austin said earlier. I mean, I think feasibility is pretty important, and it's important that hotel has an engine that can work with this type of data. So until we have like way to select and count metrics projecting into these structured objects, I don't think it matters if we do this.
But the weekend.
the other thing I think you meant to sort you were sort of getting at was reasonability like what is reasonable when you have this signal that has a complex attribute type to do. And I think we're all kind of afraid of the idea of encoding that information in a structured way or otherwise. Every single time you write out the metric.
or every single time you write out a span attribute, and I think to myself, reasonably speaking, what I would do if I wanted to instrument a complex system of this nature is, I would do what Austin suggested. I'm going to create a pointer somehow to say I've already instrumented this thing once it was in my past. I put it in a log. Probably maybe it's a special conventional log that says, here I am logging an object that's got structure, and I'm going to refer to it by a pointer type later. And now you can make your attributes have pointer types. And I think this would give us a solution that's both reasonable and feasible. That's all I wanted to say, Thank you.
Josh Suereth 00:55:42 I I was actually, if I can jump in on my hand raised, I think if you look at what the profiling Sig is doing around dictionaries where they're even doing it in the protocol.
To me. The, I'm just getting signals and and vibes, if you will, because we use that term. Now, when we develop that we, we should be thinking about that as a as a possible future evolution for opentelemetry. Apis of like here is a attribute set that I'd like to register and reference.
and that that might even hit the protocol itself.
So I I'm looking at the otop arrow work. I'm looking at the profiling work. I'm looking at how we want to do optimizations. And I'm thinking about how to optimize metrics. Even this context work. We have right with this measurement. Processor. Imagine, if you can reuse the bundle of attributes you had, and and you allocate like a context attribute once and then just share it. By id, right, we can actually do some incredibly efficient things.
They're a little bit wonky when you 1st see them. Possibly. But it's something we can sort through. So I just want to double emphasize. I'm not going to say double click. But I almost did what Josh is saying, because, 1st of all, we're both Josh's. But second of all, I think we need to like see that coming technically with open telemetry, we have a lot of pressure on us around performance and efficiency of attributes. And I think that that is the solution we see people gravitating towards so that might also alleviate some of the friction here with complex attributes, a bit.
Liudmila Molkova 00:57:27 Yeah, I would like to reiterate what the trust said. So for, okay, so to address the the id thing. So somewhere, sometimes you still need to capture the whole attribute the whole complex structure. Let's say the the container image manifest. The entity seems like the right place for it. That's an entity.
is it?
And then, if you are referring to the same object.
then on on later on.
then it's actually up on telemetry. We do the business of the duplication for you, help you do this, or some structure that that hides this object should be able to give you a unique identifier for this.
and it should not really leak into the user Api, at least.
not that they don't want to to know about the details. The second point is that the reason we've done this on metrics is because it's actually ugly to have different types for attributes. We've tried it before we've got feedback. That different types for attributes don't fly. Well.
we forget to make conversion conversion costs. We need to do inheritance of some sorts.
Most importantly, when the case arises, the significant case that would make us change when and if that that would make us change our opinion, let's say in metrics we will need to go through the round of deprecations and we will have some ugly naming, so the the cost of separating and allowing some signals to have extended attributes, and others not have them.
maybe higher than the tastes or kind of like the the taste concerns that we have.
We are almost out of time. I think the next steps I will. I I hope we can discuss it on the log. Seek and let's consider if we can bring the separation back, and how we can solve it in the way that some, some signals don't have extended attributes.
Josh Suereth 00:59:58 Sounds good. I it's a good point. I unfortunately need to leave on time today. So we have 30 seconds left. So I don't know if 30 seconds is a good time for us to get in like one last pithy thing to say, so I think we had a good discussion here, I think what you just said folks need to think about like, even if we do a workaround with a pointer type thing.
there's still the question of. Do we allow complex attributes everywhere? We'd we'd allow an attribute. And I think that's that's the thing we need to to come back to. It should be okay for us as a group to move forward with some disagreement, disagree and commit. You have enough approvals on this Otep to some extent. So for you and Trask, who, I think, are proposing this. Let you know at some point in time. We need to make a choice and move forward.
And if you'd like to discuss this again or discuss it online, let's do that. So that's that's all I'm gonna call out. With that, I do need to end the meeting, at least for myself, so good to see everybody.
Jack Berg 01:00:58 We need to end it for everyone we need to. We need to be good on this, and saying that our meetings end on time and not reward people who stay longer.
Josh Suereth 01:01:05 All right. No one gets rewarded. Thank you all for joining. Please comment on the bug.
Austin Parker 01:01:09 Hi! All!
Liudmila Molkova 01:01:10 Bye.
Jack Berg 01:01:11 They are.
