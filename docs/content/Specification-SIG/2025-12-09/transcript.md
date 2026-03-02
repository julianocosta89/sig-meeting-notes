SIG: Specification SIG
Date: 2025-12-09
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/EtB-TA-nxcRYIM4QmQyRMRUDcH22n8aI1TFN6r_j0SJTmuJnX2lJYE8IU9wVlIt2.KvNwlfvLECaPbmfP
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 01:54 Either everybody's late, or it's gonna be a quiet day today?
**Jack Berg** 02:00 Things are slowing down.
**Tigran Najaryan** 02:02 Yeah.
**Liudmila Molkova** 02:42 Hi, everyone.
**Tigran Najaryan** 02:45 Hello.
**Jack Berg** 02:46 Alright.
**Trask Stalnaker** 02:47 I…
**Tigran Najaryan** 02:58 I think we can start, probably. Let me share my screen.
**Carlos Alberto Cortez** 03:02 Actually, actually, can I share my screen for the first item?
**Tigran Najaryan** 03:07 Sure, go ahead.
**Carlos Alberto Cortez** 03:09 Thank you, give me a second.
So yeah, the first item is, regarding this old OTEP that you may remember.
Besides an OTEP that was created a long time ago, it had enough approvals. Let me share my screen.
There we are. First, let me explain. This hotelb was essentially closed,
Because this was in the old Ripple, and it has
reviews, but there was, you know… we… I think we lacked one or two, you know, reviews, but in the end, it was, like, it had enough approvals, let's say.
You have 4 approvals.
I think 3 of them were official, one of them was symbolic, suddenly we needed one more, I think.
So anyway, let's get into the stuff.
And I'm, of course, presenting this one because we are considering reopening this, but before I do that.
I wanted to get a grasp of, whether people think is something useful or not. So anyway, let's go to,
I will not explain all the other here, I will just, you know, do a general introduction, but imagine this scenario, that you have two logical services in part of a process, like, you know, this web service.
And then you have two different logical instances, my app and App2. And basically, you are getting requests and all that, and you want to see telemetry belonging, you know, to different logical services, or, like, multi-tenancy, similar, you know?
Or multi-tenancy itself, if you want to see it that way.
And basically, it's like, how do you actually mark the telemetry that belongs to one logical service in your process, to one, to that service, or to the other one, right? So, in that regard, we have a pair of options, at least.
The first one is that you get, actually, a tracer meter, meter, logger, or anything, and these kind of attributes that…
Essentially, you can, you know,
say, HTTP app, for example, like, the name of this logical service in your process, it has these attributes, and, you know, they will just be, automatically part of any spans or metrics, or, or, you know, log records that you produce.
The only, situation with that is that you need to either reuse these tracer meter or loggers that you have created with given attributes, or keep those attributes around so that you can, you know, get them from the provider at all times.
So, but that's, I would say, the way it would work today.
The option B is that, actually, you put the attributes that you want to use to identify that logical service in your process in the context.
And then you just propagate the context within your process, of course.
And basically the API would,
sorry, the SDK would… the API would be able to set them, and you can imagine an end user assigning these attributes, you know, using the API,
But the API would have read access, and the SDK has read access, or, you know, the SDK would be messaging and using those attributes, and putting them into all the, propagated spans, or metrics, or log records, you know.
So, how this could look?
basically, it would look like this. This is the way Christian, the original author, wrote this part, which is that you could have an abstract.
call in the, this is, by the way,
Save the code. So you would have in the API some abstract call,
calls, say, context attributes. You set the attributes in a context, you get a new context.
The SDK could be specifically the one, overriding this.
So you can actually,
Read that, you know, because the key, of course, is private, you know, this part, if you remember.
and all those things. So that's how it would look, which is very interesting because,
Currently, I think that at least the context layer we have in different languages, everything happens at the API level. In this case, it wouldn't require some
you know, interaction between the API and the CK.
Now, in case you were wondering how this would happen, how exactly the attributes in the context would be applied.
is that the SDKs will automatically merge them with the span attributes.
So, so basically, when a user is setting the attributes in a context.
Those attributes will appear as part of standard… any normal attributes in spans, or metrics or log records.
So in this way.
The samplers, the processors, the exporters that we already have, or third-party stuff, they will work just fine, you know?
The problem, of course, is that you would have to… the SDK would have to internally, manually.
explicitly go and have and do the merge, you know, which can be expensive, depending on, you know, how many attributes you may have. And, you know, even the merging process can be not cheap.
Alternatively, as Christian mentioned in this OTEP, you could provide an additional parameter that would contain these context scope attributes.
The problem is that, of course, you would have to add more, you know, parameters, then samplers, exporters, processors, etc. would have to become aware of this. So, anyway, that's just one more option.
And the final point, is that
in case people were wondering why not use baggage, because baggage is close enough, is that… the first reason is that baggage supports all strings.
And the second thing is that baggage is actually, you know, it's supposed to be propagated across services. In this case, the idea that we have for these context scope attributes is that you could propagate them only within your process, so that's a no-go for us, you know, be able to propagate them, especially in case you have private information or anything like that.
Also, historically speaking, instrumentation scope wasn't initially, considered for LTEP because it was supposed, or people used to think that it was a compile time.
thing, you know? Now we have changed that so it's possible that we can, you know, tell people, don't use this context attributes approach, just go and use
you know, the attribute that you put in a scope, in, scope, instrumentation scope, sorry.
Finally, as I mentioned before, instrumentation scope should work fine, mostly, but especially for traces, it's fine.
But for metrics and logs, probably not so much, unless you actually are doing correlation at all times.
That's all for my small introduction. For you to see the, go and check the… well, actually, no, even before I open that, I would like to get some… some information. INCT grant. You have your hand raised.
**Tigran Najaryan** 10:12 I think Jack was first. Jack, do you want to go?
**Carlos Alberto Cortez** 10:15 Absolutely, yeah.
**Jack Berg** 10:17 I can go,
So, my comment was about, how these attributes are automatically appended onto telemetry in the SDK.
And I think the proposal was, or one of the proposals, I think there's multiple options, but one of them is to have the SDKs updated to automatically include all of these on logs, traces and metrics, and
I think we have some tools at our disposal that maybe weren't there back in 2022 when this was originally proposed, that open up some additional avenues.
One that comes to mind is, okay, we, the SD… consider if the SDK doesn't automatically append these. Instead, if we have built-in span processors, log record processors, and measurement processors.
which you configure with your SDK, and which have some sort of configuration options themselves about which context attributes are lifted onto metrics, logs, and traces.
Measurement processor in particular was not there back in 2022, so it was not possible to do this type of thing. So, that's unlocked with this. The other thing that's available now that wasn't available in 2022 is declarative configuration. So you can imagine if we have built-in processors which do these, it can be very easy to add these to your, you know, declarative config file, along with the specification of which attribute
should be lifted into your metrics, logs and traces. So, I think the reason I'm suggesting this is, like, maybe people could get cold feet about instrumentation having some global control about, you know, adding, attributes to all telemetry that is emitted by an SDK. That doesn't seem safe in all circumstances, so…
**Tigran Najaryan** 12:14 Okay, I'll go next. So, what is the desirable effect here?
You were showing that the attributes
Will be added to the span, or to the data point, or to the log record.
In the end, but also as an alternate, you were showing that they could be recorded in the instrumentation scope?
If that's the… if that's… I guess, to me, the important question is that, right? What is the… what is the intended effect of having context drop attributes defined? Where do you want them eventually to be recorded in the emitted telemetry? Do you want them to become
a spawn attribute, or do you want them to become a scope attribute? Or… and do we want that to be even user configurable? What's the intended effect here? Is that what.
**Carlos Alberto Cortez** 13:06 Yeah, so…
**Tigran Najaryan** 13:06 It's entirely clear to me.
**Carlos Alberto Cortez** 13:08 Yeah, yeah, sorry for not clarifying that. So, basically, all your…
all these spans would get all these attributes. So in the, in the, for example, in the example I have, we have two,
You have your service, and you have two logical applications. Each, like you say, the first one, HTTP app, which would be my app, then all the attributes that you put there in that context, all the spans, and in theory, all the metrics and all the log records would get… any span that you put that at the root level, they would get extra attributes.
That means the official…
**Tigran Najaryan** 13:40 That is an extra dimension. It's not… they are not describing the scope as it is, but it's an extra dimension.
And they may be served by the same scope, even, right? They are not coming from different scopes.
in the code, but it's a dimension. It's that the application name, it's served by the same code
But we want it to be recorded as an extra attribute on a span or on a data point, essentially.
Okay. Yep. Okay, thanks. Josh?
**Josh Suereth** 14:11 Yeah, so first of all, I think this is awesome. Thank you for starting to work on this. This actually brings us closer in line with OpenCensus now, and one of the, like, key features there. Two things come to mind. One is,
I think, like, the ability for you to control what baggage goes in… like, I like the idea of having an area of context that has a set of attributes that get added to all signals.
And I think the notion that you have explicit control of how, like, whether or not that happens is important.
So, like, to Jack's point, you know, having an explicit processor set that would say, okay, I'm going to be attaching this. We should make that as easy as possible to do. For, like, exemplar sampling, for example, you know, we have the three flags. We can make that config, whatever.
I would also love if we had a thing that would lift baggage into this, or somehow interact with baggage in the same way. Like, I think to make baggage useful, it has to have the same
thing where you say, here are the three fields in baggage I will lift, right? And so, I can see this going one of two ways. One is, we have a processor that basically interacts with context. It will look for local context and remote context, meaning, what, this new thing, and baggage.
and it will have a list of attributes that are safe to pull from baggage, a list of attributes that are safe to pull from local context, and then it adds it. That's option one. Option two is, we do something where we say, cool, every time I pull in baggage, I use baggage to propagate remotely, but I will also lift
particular fields and put them in the local context. And then, instrumentation only deals with local context.
I think you could go either way, I like the first better than the second, but I'd love, like, one thing that I saw as an opportunity missed in the previous OTEP was I think there's an easy interaction with baggage here that opens up distributed and local
attribute, you know, tagging in context that would be really valuable for us to have. So I'd love to see that in the final proposal, whatever you do.
**Tigran Najaryan** 16:21 Robert?
**Pellared** 16:25 So one thing, just to call out, that there's little, like, dependency, the measurement processor, it's not merged there, it's not merged yet.
it was basically stall, the PR has gone stale. Basically, there was also a proposal from Tyler that it can be, instead of creating a new measurement process or component.
It can be basically a new property of the view.
So, basically, we should probably, you know, just backtrack what's going on there, and revive it.
And the second part is, I'm not sure if it was documented in OTEP, maybe not. In Go, and I don't think it's only in Go, we already have this baggage processor, which basically adds this kind of scope attributes from the baggage, from the baggage, which is kind of…
Which means that we have something already.
And yeah, that's all from my side.
**Tigran Najaryan** 17:26 Jackson Lydmila.
**Jack Berg** 17:28 I posted a comment in the chat, and I just want to…
I want to also double down on my support for this. You know, as Josh said, I think this is a really important area to work on, and so my comments here aren't, like.
I want to find a way to make this work. I don't want to, like, dissuade you from doing this in any way, and I'm just kind of exploring options. One other option that comes to mind is, like, for configuration around this is the, the scope config section we have.
Where you can… we have this SDK feature to configure meters and loggers and tracers. And so, you know, we could provide a new option to those that say, hey, for this meter, lift these attributes, these context attributes, up onto measurements for instruments in this meter, for this logger, lift these context attributes. And the advantage of doing it at that level is, like.
hey, like.
We want to have configuration around this. What types of things do we want to be configurable? We definitely want to be able to describe which context attributes are lifted onto the telemetry, and probably we want to be able to dictate that at the scope level.
Maybe not? Like, maybe it's okay to just have it be global, and you just say, hey, you know, the foo attribute is listed onto all telemetry of all scopes.
But I don't know, I feel like people are going to request that, like, certain scopes are excluded for some reason or another, so scope config could be a good option to solve that requirement.
Thanks.
**Liudmila Molkova** 19:03 Yeah, I also wanted to say something about this problem. So, I'm also very supportive. It comes up a lot when people talk about instrumentations and limitations, that we cannot, stamp some context on down, on inner spense.
I think the problem of what to stamp on will come up, and we will need some solution. But I also, there is a priority, right? If you look into, let's say, login scopes,
The thing exists, and all… everything under is expected to get this scope.
And people live with this.
So… I would also be supportive if we just start with the global thing.
As long as we know how to eventually solve the targeted injection problem, or not injection.
**Jack Berg** 19:59 As long as the global thing that we start with has, like, a way to turn it off.
Right? Because if you can't find some way to turn the global thing off, then you're exposing yourself to, like, cardinality issues with metrics in particular, so…
**Liudmila Molkova** 20:11 Yeah, maybe for metrics, the default should be off. For spans and logs, maybe it should be on.
**Jack Berg** 20:18 Something like that, yeah.
**Carlos Alberto Cortez** 20:19 Yeah, fair enough.
Okay, I think we have taken twice the time I had expected for this initial discussion to happen, but I'm listening that there's initial support, so in that case, I will go and actually get the update from Christian updated, and just present that, and let's open an issue, and I will be, discussing with you all for your details.
But that's… that's looking good.
Thank you.
**Tigran Najaryan** 20:48 Okay.
Next we have… Your proposal, Josh? Jay Magdi?
**Joshua MacDonald** 20:58 Yes, hello, thank you. Okay, so first item I put up today…
Is on the screen here.
We have been working on this in Sampling SIG for years at this point. This document, this proposes to stabilize the OpenTelemetry trace state values.
The reason why we think it's a good idea is that it's been stable, in our opinion, for a long time. We've got prototypes, we've got stable implementation, as far as I'm concerned, in the collector.
And so the main document is the first one there, the trace state handling. It defines the syntax of OpenTeometry trace state and the interpretation of two fields there. So it's TH and RV.
this… the syntax document was probably… it's probably 3 years old. The RV and the TH specs are, were revised late last year, but that was after, you know, years of… of iteration. So this stuff is all pretty stable in our opinions, and none of us on the sampling stick have any… any, awareness of any complaints about it, so…
When we stabilize this, what it means is that vendors can commit to recognizing these trace state values in their backends. This means that you can receive a span that was sampled 1 in 10, and count 10 spans, make metrics from it successfully and accurately, and so on. So,
That was the proposal. You know, I think the reason why this is risky or challenging is that there aren't very many SDKs that implement this yet.
And I think that we need to remember that the data model specification here is what we're trying to stabilize, not the SDK specification. We can come and find reasons why the SDK spec is not quite perfect.
change what… how we generate these values. All we're trying to stabilize is the meaning of these values.
So I, that's the issue. I was…
Looking for feedback or any kind of thoughts on this topic.
What we would hold as a sort of, like, blocking or gating,
For this. Bogdan has his hand up, please.
**Bogdan Drutu** 23:09 Should… should we treat this as any semantic convention, and
I don't know if we really need a lot of SDK implementation, since it's more of a semantic.
Or are you worried about the samplers and the logic to be implemented in the SDKs?
**Joshua MacDonald** 23:32 Yeah, you're right about this. It is… it is, roughly speaking, close to a semantic convention, though I would maybe think of it as more like a protocol, you know, this is,
you know, some string… string syntax, and you, you know, you calculate numbers from it. So, I'm not sure it's a semantic convention in the same way that the semantic conventions Repository is concerned with.
But it is not… it is not an SDK spec we're trying to stabilize either. Josh?
**Josh Suereth** 24:02 Yeah, I'm just gonna back that up. I don't… like, these are semantics, but we need to be careful with semantic conventions, that it's not just a hodgepodge of anything… anytime I use the word semantics. Semantic conventions should be, like, this is the shape of telemetry that we're gonna generate. That's the focus of that effort. So, this is… this is different. I see this as, like,
partly a context propagation spec and a definition of protocol, so I… I agree that this is important. And you don't think SDKs are going to be interacting with this?
**Joshua MacDonald** 24:32 Oh, I think they will be, and I'm… in a moment, I'm going to let Yuan Yuan speak as well, but this is, so we do have SDK specs on how to use this, and those are still experimental or in development, and I want that to continue. We have…
seen prototypes in Go and Rust and Python and JavaScript. Some of them are ready to stabilize as well, but those are implementations that produce these values, not the meaning of these values.
This is almost protocol in the sense that I could define you a protobuf that has these field values and, like, write down what they mean, but instead, because it's part of the W3C ecosystem and part of the W3C Trace Context Level 2, it needs to be put into a string field.
**Josh Suereth** 25:18 Yeah, for context, when we have context propagation things that don't fit in W3C, we do keep them in the spec.
like, we have environment variable propagation for trace context, we have environment variable propagation for entities, and I think there's other propagation techniques that we have in the spec. So I would say that this, like, this should fall in that category of thing, and yeah, glad to see it.
**Joshua MacDonald** 25:44 Great, so we do consider this a context. I'll… thank you. I think I've learned what I need. I might send proposals to mark that stable in the specs. Yuan Yuan is also here with us from SamplingSig. Please speak.
**Yuanyuan Zhao** 25:59 Well, it doesn't look like I need to speak much. I was here mostly to second Josh's opinion, and the fact that most of SDKs are in prototypes, and some are even not implemented is not a drawback.
This, actually, have this stabilized is a prerequisite, so that the SDKs have something to build on. So that's…
This is probably…
goes without saying. But thank you. Thanks, Josh, for bringing this up. We, by the way, I'm from Datadog. We very much would like to support this very actively, that's why we, we want, to help,
Motionize… motion, the stabilization of this, and also if they are,
need to implement some of those in SDKs, and they are ways that I think many vendors and companies are willing to support.
Thank you.
**Bogdan Drutu** 27:07 Josh, I have only one question for you.
What… how do you see the sequence of stabilizations? Because if I heard correctly from you, you are planning to stabilize only the definition of the values, or the protocol, and then later you want to stabilize the SDK spec. Is that correct?
**Joshua MacDonald** 27:28 Yeah, I would… I would say we're trying to stabilize this aspect here. The next piece I would stabilize is the recommendation to use W3C Trace Context Level 2, which is, like, the first step, and then…
there were two more pieces of our spec that we added for the SDKs, for traces, and it was… the first was, to fix the trace ID ratio to-do from years ago, and the…
And that would be the next step as well. That's, like, on my, like, must-have list. And then we have a second…
Sorry?
**Bogdan Drutu** 28:00 I would, only one request from me would be, can you document this roadmap or timeline that you are envisioning here, in an issue? And yes, I'm 100% supportive of stabilizing this, but I would like to see the full picture somewhere documented to see, hey, we are here, these are the next steps that we need to do in order to get to the finish line.
**Joshua MacDonald** 28:26 That's fair. I'm gonna look for the PR that… we did spell out the stabilization roadmap at one point in the last 6 months. I'm gonna go find that for you and make sure it's linked to the issue that we were just on.
Because they're…
**Bogdan Drutu** 28:42 Metaissue with that.
**Joshua MacDonald** 28:44 Yeah, there… okay, there may not be a meta issue that's still open. We did make changes in the SDK spec after some of the SDK authors reviewed it and said, well, we need to keep our trace ID ratio the way it is for a while, and so that was… that was discussed. But I will, follow up on that in the issue and ping you as well. Thank you.
**Bogdan Drutu** 29:04 Perfect! But, yeah, and for me, this is a plus one. We should make progress here, and I think the only requirement for me would be just to understand the long-term plan, to see where we are going and where we are in that path.
**Joshua MacDonald** 29:20 Great.
I will… I would follow up on that. I would… I didn't even mention that my old vendor, the one I worked at last, also had an implementation of this, so we've seen… we've seen that it can be done as well.
Okay, I propose to move on from this. Tigran, you're still sharing. Would you, this is the… the… this was the easy one that I wanted to present. The next one…
is a little, trickier, and I knew, Tigran, that you would be here today, so I especially wanted to have you in the room for this conversation. This is very much in a draft form, and I wanted to bring it to this group to sort of,
with… the reasons I wanted to bring it today, or now, essentially, is we've had several conversations recently. One was with Josh about entity ref, how it was sort of bolted on backwards compatibly to the OTLP spec. One's been about this, like, resource conversation with the profiling group about wanting to have more concise ways of representing OTLP. And then there's this ongoing project that I'm involved with, OpenTelemetry Air.
row.
And what I'm searching for here is a solution to our… what I see as a sort of problem.
And it's that we've been using the OTLP model for years now, and it's, like, it's so close to our data model that it's impossible to think about OpenTelemetry at this point without referring in your mind to the OTLP 1.0 or 1.X
series. The data model and the protocol are just extremely tight.
And because of that extreme tightness, we keep using it for our data model, and I think that's good, but it's not a concise protocol.
And, when we started the OTEL Aero project.
we set out with this goal, and it's sort of documented here, which was to be perfectly compatible with OpenTelemetry, and that means something. That's what I'm trying to define here. So, perfect compatibility means that for any OTLP payload that you give me.
I'm gonna turn it into the other protocol, maybe it's more compressed, I'm gonna be able to turn it right back to you and give you the same data. It should be identical for the entire space of data that can be expressed in OpenTeometry, the V1.x.
So that's the first part of this, is that we want to be able to define perfect compatibility in a way that the OpenTelemetry community could accept, such that we could imagine
adding in these protocols as sort of options that would be a sort of feature you could select to say, I'm using OpenTelemetry data, but I want this sort of fancier protocol that gets me better compression. I know my vendor supports it as well, so I'm going to choose the OpenTelemetry Arrow protocol, for example. The reason I wanted to talk about this with Tigrin as well is that he's been working on Steph, which is, I think, a viable alternative that does
you know, even better than Hotel Arrow on compression for metrics.
And…
So, what would be the requirements? These are sort of what I'm proposing as the requirements. These are how we implemented the OTEL Aero 1.0. It's that we are going to be able to provide you a protocol implementation that can share the same port, the same receiver, the same exporter with OTLP.
So that you can have a receiver and an exporter that support OTLP and an option to upgrade to another protocol.
I would phrase this as an extension model. We're saying that we're going to extend the base OTLP exporter and the base OTLP receiver to support alternative plugins, which give you different protocols. And as long as you can do that.
Perfectly compatible, and in the same context, meaning, like, for a gRPC service, you can just register another service.
For an HTTP service, you can just register another path. If you're an OTLP exporter, you can try the alternative, and then you can fall back to OTLP. And this will give us a way to say these are officially supported alternatives that give you a perfect compatibility promise, and give you a better way to compress your data.
I have proposed this as a framework. I'm not saying let's standardize OTel Aero, I'm saying let's have a framework for saying what is perfectly compatible.
So that users can have this as an option. I think this is more feasible than trying to, say, wait for OTLP V2, or try and invent a new protocol and have everyone switch to it. I think what we're gonna… what I'm proposing is we keep our OTLP data model, we keep it as the reference in our heads that we work on, that we talk about, that we specify.
And then let other protocols come in and be more efficient.
Okay, so hands are up. I'd like to hear what you all think.
**Tigran Najaryan** 33:44 Boglin, you wanna go first? I'll go next, then.
**Bogdan Drutu** 33:48 No, go for it.
**Tigran Najaryan** 33:51 Yeah, I did take a quick look, Josh. I think this is great, thanks for opening the discussion. I mostly agree with what you have in the OPEP.
One small comment I had there was the very first requirement
it seems to be a bit limiting to me. If you look at the possibilities there, let's say we're doing gRPC, and we can choose to do streaming as well, if we use gRPC. And then when you do streaming.
There's not necessarily a concept of a request that you want to directly apply there, because you have messages there that are streamed.
So, I would say, in my mind, you're… you're actually… your second requirement, that is, is non-losing representation of
OTLP data model. I think that's the critical requirement in my mind, and the fact that it is recorded in a form of a particular request on the wire is more of an implementation detail, as long as you can make it fit
into the…
into the transport that is currently used by OTLP in an upgradable form, which is your requirement number 3. I think then we're good in that case, right? It doesn't necessarily have to be
Where you have a request here and a request there that are directly mappable, as long as your data that is being communicated is moppable in non-losing way.
and fits the requirements at the transport layer, then we should be good. That's kind of a slightly different way of saying, I think, what you want to say there, so I mostly agree with you. I'll take another, like, more detailed look, I just started looking at it 10 minutes ago, but I think this is a good start. Thank you.
That's all I have to say. Bogdan, you wanna go?
**Bogdan Drutu** 35:41 I… I have a meta question, which is, let's assume… we…
We approve this, or we agree with this.
I would like to understand how… how do we envision
Are we envisioning that we are gonna support 10,000 protocols? Everyone can come up with their own protocol? What… what is the…
what is the end goal of this? Do we want to support
infinite number of protocols, or do we want, as a community, to have, let's say, two other alternatives to OTLP?
I need to better understand, because you are saying here that somebody like OTLP Exporter should support multiple choices, but what are these multiple choices and OTLP Exporter should support?
**Joshua MacDonald** 36:35 Let me try and answer that before we go on. So, I did try to answer this. It's in the text, not on the first page, what we're looking at. But I don't think we should go try to read it now. So I… the answer I tried to give was that, first of all, one of these protocols has to implement both the receiver and the exporter.
support. That's… that's critical. And then the answer was community acceptance. Like, we're not gonna just say anything goes.
What I… the way I would make this requirement on the collector would be to… to expand, and it can be either by extending the current OTLP exporter receiver, or by mod… or by creating new, what we call the OpenTelemetry exporter receiver. These are, like, they support the OTLP as the base, and they let you plug in extensions. So I'm calling them extensions so that we don't… so that we can have them be pluggable, but I don't expect 10,000. I spent one… I expect
one or two. Like, these have to be community agreed upon for them to be fully blessed as 100% compatible. Like.
it's not an easy undertaking. I don't expect many of these to exist, maybe a few. And I wouldn't… and… but I was trying to make them part of the core in the sense that, like, if OpenTelemetry as a group agrees that OTel Arrow has proven itself, it's consistently showing good results, it's promised
compatibility, its multiple implementations are available, and so on. If the community then accepts it, I would say the OpenTelemetry exporter and receiver are part of the core.
And that plugin extension is also available easily, you know, officially supported by OpenTelemetry in some sense. So OpenTelemetry doesn't have enough bandwidth to support very many of these, and…
**Tigran Najaryan** 38:10 Josh… Josh, do you think of this as sort of a…
the only way… a single extension to OTLP, essentially OTLPv2, or do you think of this as…
More than one way to have an extension.
**Joshua MacDonald** 38:25 I actually do think more than one way, and I… and I've listed links below…
**Tigran Najaryan** 38:29 Sophically, those are different approaches, right? It's not just OTLPv2, it's more of an open way to extend OTL.
**Joshua MacDonald** 38:36 Yeah, I'm looking for an open way, and let me give an… just concretely, the OpenTelemetry Arrow components, which are the Phase 1, we finished them a couple years ago, these are Go Exporter and Go Receiver components.
They were forked from the OTLP core. They were… we took the core collector, OTLP exporter, and receiver, and we forked them, and then we added Arrow support, without taking away OTLP support. That was, like, how we did our fallback.
And so those… the structure of the OTL Aero exporter receiver very much resembles the core OTLP exporter and receiver, with the addition of, like, this extra
feature. And that's how I envision this integration working, is that you'd have an extension interface which says, I'm a protocol named X, here's my unMarshall function, here's my Marshall function. If it's a streaming protocol, I think we need a slightly different arrangement, but both of those, the OTLP, the
hotel arrow exporter and Receiver were modeled as the candidates here, because they support fallback, and they support an alternative protocol. They don't have extensions yet, but I would… I would try to invent that.
**Tigran Najaryan** 39:39 Austin.
**Austin Parker** 39:40 Stand up. Yeah, thank you.
I have a couple of questions, but to limit it. I do want to echo what Bogdan just asked in chat, which is, who…
is responsible… Like, where is the implementation for this, Liv? Is this,
Do we expect that there would be changes in both the SDK and the collector?
The second related question is, in terms of upgrading or downgrading or sidegrading.
Is the expectation that the burden of that would be with…
Receiver, like, people that are receiving OTLP data?
So if I'm…
Yeah.
If I'm a vendor, I have an OTLP endpoint, I need to update…
To start receiving this, or can the client renegotiate if it starts sending something that.
**Joshua MacDonald** 40:41 The way this has been framed for us in Otel Arrow would be that both sides do something. So the receiver opens a new protocol path, you know, I'm going to serve more protocol or more service name in gRPC, so that you can try them both, and that both are supported.
And then for the exporter, you know, the way we did it was to recognize the unimplemented code that gRPC sends you, so you try the thing that you like, and it doesn't… comes back unimplemented, you fall back to OTLP at that point.
And the essential part was that we kept the configuration model. Like, we use exactly the same configuration for the endpoint, the gRPC settings, and all the other stuff that…
queue settings, batch retry, timeout, all that stuff is exactly identical, and then we just try two protocols, and if the first one works, we keep it. Otherwise, we fall back. And the reason why I said that OTEL has to provide… like, this has to be provided as a receiver as well as an exporter. Like, we need to be able to say that, hey, vendor.
you know, if you trust OpenTelemetry and you've been using our OTLP receiver, just take our OTL Aero receiver, or the extension that we give you, which is the plugin for the receiver that gives you more protocol support.
And it'll, it'll start working in some sort of, like.
Seamless way is really what we're after.
And I did not make any changes proposed for the SDKs, and this is not an SDK proposal at all. It's entirely about what collectors can do to add protocols. I do think it would be nice if SDKs were starting to experiment with them, but mostly this is about what collectors can do. Josh?
**Josh Suereth** 42:17 Yeah, this is probably in line with what other people were suggesting, but this is… this is an alternative proposal to think about. To get out of, like, the weeds and details of, how the collector works and things.
I would suggest that you have a conformance test for protocol compatibility. So, like, you could say, if I… if I start with an SDK that has instrumentation.
and I go through an alternative protocol to a collector, and that collector exports OTLP. That should match the same as if I go SDK to collector to OTLP, right?
If I am using, like, two collectors in the middle, and OTLP comes in one side, protocol B comes out the other side to another collector, and then I can reconstitute that same OTLP. Like, I would focus on that conformance test.
**Joshua MacDonald** 43:07 Yeah, so we have signed…
**Tigran Najaryan** 43:08 Nothing like that, Josh.
**Josh Suereth** 43:09 That's okay.
**Tigran Najaryan** 43:10 in the collector. We have… we have correctness tests in the collector, which do a round trip through a protocol and verify that the data is represented exactly in the same way as at the source.
We do generate… we generate randomized data, and then verify using that data that the protocol is not losing anything there.
**Joshua MacDonald** 43:34 Can we scroll down a little bit?
**Josh Suereth** 43:36 thing about.
**Joshua MacDonald** 43:36 equivalence testing here, because this is actually a key, is that one of the benefits that we get from OTel Arrow is compression, and the way we get that is by reorganizing the data. So, equivalence testing allowances. We, like, Josh, you're right. One of the first things we have to do to establish this type of thing is to build a conform… like, an equivalence test framework suite, or something like that. And equivalence testing is not obvious or automatic in OTLP.
And so, I've tried to spell out the rules that I'm using to valve
validate equivalents. For the… these were first developed for the Go Hotel Aero implementation.
We've implemented them again in Rust. We need to, like, canonicalize the messages before we compare them, and that's, like, not trivial, but it has to be done. So that would be included in my, what does it mean to be perfectly compatible? Like, passing the conformance test is one obvious, sort of, like, statement we could make.
**Josh Suereth** 44:31 But I guess my suggestion here is I think that should apply to SDK through Collector as well. So, like, I see a need for us with Arrow and other protocols like that, where we're going to want the SDK to produce in that format, because it could optimize the SDK's generation of data.
So, we… I'd want a conformance test that also talks about… from an SDK level. So, if we have an SDK that writes OTLP, and we have… and then we re-instrument it… not re-instrument, sorry, keep the same instrumentation, but also have the same SDK generate,
the new protocol, there should not be a difference in terms of what you experience on the… on the other side on the right, like the data stored. So.
That… I…
I would focus on equivalence testing, personally, and get this specification right, and some of the other things about requests for requests, like the others were saying, I don't think are as important as figuring out this problem.
So, I'm glad to see this here. Sorry, I didn't have a chance to look through the holo test before I talked.
**Joshua MacDonald** 45:34 Okay, I sprung it yesterday. Thank you all. Bugdan.
**Bogdan Drutu** 45:41 Oh, yeah. My last, couple of questions I have here.
And I will… I will play off a role here. Why do you need this versus a completely different exporter and receiver?
What does it bring to you?
**Joshua MacDonald** 45:59 The… the answer I have is a sort of seamless upgrade. Like, can users try to upgrade to this protocol if the backend doesn't support it? How much change is required? And what I'm after is that we use the same settings. So you config… instead of configuring your OTLP exporter with
endpoint and DLS and gRPC stuff. You configure the… any old protocol and exporter, and it will try the ones it's got registered, and it… and I…
and I didn't… I put it out of scope for this document, but, like, HTTP has a lot of work done on content negotiation, whether it's initiated by the server or by the agent, and so on. So, like, this is effectively a solved problem. We know how to use HTTP headers. So we can send a header list saying what… or ask the server for a header saying, like, what content encodings do you accept? You know, you could send an empty request
figure that out if you wanted. Or you could just try what you think is going to work, and there's a couple ways you can do this.
But the goal is that the users don't have to change their configuration, they don't have to change their port, they don't have to change their endpoint. It's equivalent. It's, like, part of the same service. We're trying to avoid that… the user churn that is involved in changing protocols, mainly.
**Bogdan Drutu** 47:14 I understand that, but then should this just be a configuration problem?
**Joshua MacDonald** 47:22 Oh, sweet.
**Bogdan Drutu** 47:23 we have 10.
**Joshua MacDonald** 47:23 I think there's an upgrade problem, a chicken and egg problem of sorts. Like, I need to upgrade my client to use the new protocol. Well, first I have to change the service, so then the service has to add a new port, a new route, a new ingest, like, all that stuff is really hard to get right.
So… so, from my perspective, it's much easier as an operator, much easier as a user to just, like, keep all your configuration and upgrade the protocol.
But I see your point. Like, yes, you could just call it new, and then it's a little harder on the user.
Daniel. No, no, no.
**Bogdan Drutu** 47:58 Sorry, one more follow-up, and then you can jump to another one. So, I understand that, but, for example, if we offer users
again, we keep everything separately, every exporter and every receiver is separately. If we offer users a way from the configuration to configure that once, and say, here are the 10 exporters that you can try, and we offer that, what is the difference of
offering something like that as a framework on top of the exporters we already have, versus changing the core exporters and the OTLP exporter to support this.
**Joshua MacDonald** 48:39 In some level, that sounds very similar to me. I would accept if that's how you thought it should be phrased or framed.
I was imagining, plugins to do that, rather than, like, some sort of meta-exporter or something like that. But I see those as quite similar.
**Bogdan Drutu** 48:57 Okay.
**Joshua MacDonald** 48:59 Daniel.
**Daniel Dyla (Dynatrace)** 49:01 Yeah, I just wanted to raise, as part of the, content negotiation thing that you talked about, one place where in JS,
we see a lot of confusion between the difference between, like, the protobuf, over HTTP and JSON over HTTP.
And we see users misconfigure this all the time, and it's a minor thing to fix, right? You point it out to them, they fix it, they call it a day, whatever, but I would say I've seen this, like.
probably over 100 times. So if there was some form of content negotiation for that as well, like, as long as we're thinking about content negotiation, that would be,
You know, something that… I think would be helpful for us.
**Joshua MacDonald** 49:47 Thank you. I did link… I listed JSON support as, like, almost special case, but kind of the first example of a alternative that we have. It's baked into the same exporter, and in some sense, it's a different encoding of OTLP. It's not… it's like…
you know, and it happens to be that we support it on OTLP because it's, like, a protobuf equivalence level, but what I'm saying is OTL Arrow is equivalent to OTLP, could we just put that in there too?
And it's, it's, you know, it's a different content type.
obviously, completely different parsers are used, so that is the example I used, to say that we already… we already do this in some sense.
Have, have alternatives.
**Daniel Dyla (Dynatrace)** 50:26 Yeah, we have alternatives, but we don't do any sort of content negotiation, and we run into problems because of that.
**Joshua MacDonald** 50:32 Thank you. I think that's a really good observation. I hadn't… I don't know… I haven't focused a lot on that detail, clearly.
**Daniel Dyla (Dynatrace)** 50:39 Yeah, I don't think anyone really has. I… at one point, JavaScript was the only SDK that had a JSON exporter. I don't know if that's still the case, but I know that all languages don't, so it's something that I think not a lot of,
Maintainers think about regularly.
**Tigran Najaryan** 50:59 To comment on Bogdan's question about why this can't be just a…
just a regular exporter and receiver for that particular protocol in the collector. I think it absolutely should, initially, right? You would want to incubate whatever protocol is it that is being proposed as a dedicated exporter and receiver.
in the collector, maybe, like we're doing with Arrow and with Steph right now.
To gain that confidence and usage information.
before you then propose to maybe put it as an extension to existing OTLP. The difference there is, essentially, when you make it part of OTLP is exactly what Josh was saying, right? You gain that ability to essentially, overnight.
upgrade your existing infrastructure to a more efficient, hopefully more efficient protocol without touching anything by simply upgrading to a newer software version, right? And also, I guess, the power of defaults works here as well, right? If it's just
another protocol in the collector, the usage is going to be, like, who's going to use it, right? Who has the very specific acute need for that protocol's benefits? Whereas if it's in OTLP and is used automatically, you suddenly have a lot more people
Actually, having a way to use it, and the vendors also having the interest to support it, so that… because it's now in the collector by default.
So I think, absolutely, we must, first of all, make sure that it is being incubated first, and we feel that… we feel strongly about the benefits of that particular protocol in the collector. But then, I guess a logical step would be that, yes, maybe you make it an upgrade
an automatic upgrade of an OTLP protocol as a step two. But I'm with you, Bogdan, that obviously we can't have 25 different extensions to the OTLP protocol.
Resulting chaos and complexity of implementations.
**Bogdan Drutu** 53:08 So, hear me out, what I'm… what I'm hearing as a… as an external person. What I'm hearing from you is that actually what we need, and correct me if I'm wrong, but what we need is actually a way for… for the OTLP protocol to support,
Format or a protocol negotiation.
And…
**Tigran Najaryan** 53:36 You're breaking up.
We lost you.
What can't hear you boggling?
I guess… Okay, we now hear you, said it again.
**Bogdan Drutu** 53:50 Okay, sorry.
**Tigran Najaryan** 53:53 Oh.
Not good.
**Bogdan Drutu** 53:57 Hold on.
**Tigran Najaryan** 54:00 It's not me, right? It's Pogdan.
Can you guys hear me?
**Ivo Anjo** 54:04 Thank you.
**Tyler** 54:04 Yeah, correct.
**Tigran Najaryan** 54:05 Bogdan, we lost you again.
I guess what you wanted to say, if I were to guess, a protocol negotiation by OTLP receiver and exporter, and a way to hand off, maybe, the control to an alternate implementation, which could be an existing exporter and receiver. We could make that happen, right?
that the connection happens with the OTLP exporter. As a result of negotiation, then the control is handed over to an alternate implementation. Something like that could happen.
in the collector.
**Bogdan Drutu** 54:39 So what I was trying to say, if I'm having now connection, I want to say that I think what the proposal should be is have an ability to negotiate protocols at the OTLP,
protocol. Like, have… no, sorry, have the way to negotiate the encoding of the OTLP protocol.
Is that what… is that…
**Tigran Najaryan** 55:03 Yes.
Then hand over the control for that particular encoding to the implementation of that encoding, right?
**Bogdan Drutu** 55:09 That's for sure, but the whole idea is that we are adding this capability of having a way to negotiate which encodings are you supporting. So, essentially, similar with HTTP, you would send an empty request to the server, server comes back with, here are the 10
content encodings I support, and we should… implement that.
**Tigran Najaryan** 55:33 Yeah.
**Bogdan Drutu** 55:35 Is that… is that what's…
**Tigran Najaryan** 55:36 possibility, I guess. We'll need to think through that. It's a possibility.
**Bogdan Drutu** 55:40 But, okay, it is a possibility, but what I'm hearing, is that what you are trying to achieve, or is something else? Because for me, it's like, do we try to make Prometheus, for example, a way to…
to Prometheus be a way to send data, like Prometheus Remote Ride, for example.
**Joshua MacDonald** 56:05 I don't feel like that that was in scope. I mean, like, I think of Prometheus Remote, right, as not exactly compatible, and that could be up for debate, but I do hear
the feedback from Bogdan saying, essentially, that, that the hard part here is content negotiation. I hear Tigrin saying that, like, of course you're going to want to incubate. Maybe what I'm imagining is sort of like a meta-export or receiver library, which is like, here's the basic
framework of an export or receiver that can fall back to OTLP. OTel Aero, you use that for 2 years now.
See if it's… if it's working out for you. It provides you the fallback mechanism, and if it proves itself after 2 years, you can say, well, take that code and plug it into the OTLP exporter now, because it's proven itself, and the community accepts it, and so on. So I can see a path
Where we build a framework for this upgradeable
thing, and then go to prove out our content negotiation, and then later it gets put into OTLP, like, years out from now.
That's great. I learned what I wanted from this issue.
For sure.
**Josh Suereth** 57:11 Bye.
I wanted to add to that, Tigrin did a lot of writing on content negotiation and OTLP, and it's really well done. I think he, like, Tigrin, maybe share that with Josh, the capabilities thing, because there's a set of challenges there where I… I don't think we can add content negotiation to existing frameworks without it being a breaking change.
when you look at what happens through a load balancer, things get really awkward. I think we can add content negotiation, but we have to, like, do… first of all, I love the idea of adding content negotiation, don't get me wrong with, like, my comments on Tigrin's document, right? I don't think we can do it in a non-breaking way.
And if we do it, this notion that we'd add a new exporter that does content negotiation that people opt into, and then we try to convince our community to move towards that, we should do. Like, and… but let's sort out what content negotiation is, because again, I don't think it can be non-breaking to existing OTLP setups.
But, given what we're trying to build in OTEL, I think it's a direction we should move.
I think there's a lot of power to get there, so I'd love if we can get this sorted out.
And I would recommend reading what Tigrin wrote, because he… I think he captured all the challenges really well in that document.
**Joshua MacDonald** 58:23 Sweet. I'm not familiar with that, and I appreciate it.
I will look for that.
I will try and follow up on this topic. It's interesting to us, especially to help OTEL Aero move forward and so on. Thank you all.
**Tigran Najaryan** 58:42 Okay.
and killed…
**Joshua MacDonald** 58:44 Probably reach the end here.
**Tigran Najaryan** 58:45 Yeah, we don't have much time. Any last comments on this topic?
**Joshua MacDonald** 58:52 Thanks, everyone.
**Tigran Najaryan** 58:54 Right.
Thank you. Bye.
**Carlos Alberto Cortez** 58:56 Cute.
