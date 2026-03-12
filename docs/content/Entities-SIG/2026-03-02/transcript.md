SIG: Entities SIG
Date: 2026-03-02
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

**Ted Young** 00:36 Yellow!
**Dmitrii Anoshin** 00:40 Alright, Dad.
**Ted Young** 00:41 How's it going?
**Dmitrii Anoshin** 00:43 Doing well, how are you?
**Ted Young** 00:45 Pretty good! It's Monday.
Catching up with everything.
**Dmitrii Anoshin** 00:55 You, you live somewhere on the… Pacific Northwest? Or no, no, okay.
Origos.
**Ted Young** 01:01 I live in Portland, Oregon.
**Dmitrii Anoshin** 01:03 Oh, nice, nice.
**Ted Young** 01:04 Yeah. How about you?
**Dmitrii Anoshin** 01:06 I'm in, the Bay Area.
**Ted Young** 01:09 Sorry, where?
**Dmitrii Anoshin** 01:10 Bay Area.
**Ted Young** 01:11 Bay Area, cool. Where in the Bay?
**Dmitrii Anoshin** 01:13 Sans Jose?
**Ted Young** 01:15 Oh, cool. Yeah. I lived in the Mission for many years, in San Francisco and in Bernal.
**Dmitrii Anoshin** 01:39 Are you coming to the, KubeCon EU by chance?
**Ted Young** 01:43 I'm not this year, unfortunately. I wish it was there.
Especially, I was helping to set up like, you know, Prometheus and OpenTelemetry maintainers kind of having a little mini summit.
**Dmitrii Anoshin** 01:59 life.
**Ted Young** 02:00 But… Sadly, I will be on vacation in Japan.
**Dmitrii Anoshin** 02:06 Oh, okay.
**Ted Young** 02:07 Priorities are all messed up.
**Dmitrii Anoshin** 02:10 It's a good thing, yeah.
So, yeah, it's my… it's been a while for me since I traveled from the… North America, like, 7 years, and I'm going… I'm coming this year, finally.
**Ted Young** 02:26 Did I hear you're from Siberia originally?
**Dmitrii Anoshin** 02:28 Yes, I am.
**Ted Young** 02:30 I have a couple of friends from… Novo Sebrisk?
**Dmitrii Anoshin** 02:34 Oh, nice.
**Ted Young** 02:34 How do you pronounce it? Yeah.
**Dmitrii Anoshin** 02:36 Yeah, now we see Birsk. Right, right.
Cool. I've never…
**Ted Young** 02:40 in, but…
**Dmitrii Anoshin** 02:41 That's true.
there are two rival cities, for taking, like, call… to have a… to be called, like, capital of Siberia. Mine, Krasneursk, and now Zibirsk, but they said they are… we say we are, so…
**Ted Young** 02:59 Yeah.
No, I have, like… like many Americans, I feel like I had an image of Siberia that is, like, Siberia in the year 1905.
You know, not really Siberia today. So my friends are like, we're from Siberia. I'm like, oh, wow, out in the country. They're like, no, we're from a humongous city.
**Dmitrii Anoshin** 03:19 Yeah, it's, like, a million-plus people, yeah, usually.
**Ted Young** 03:28 Let me finish.
Signing it.
**Josh Suereth** 03:34 Thanks, everybody.
Sorry I'm a little bit late, some kind of meeting ran long. Talking about fun things.
Alright, so… Let's get started. This is feedback from the browser seg, huh?
Do you wanna…
**Ted Young** 03:49 Yeah!
**Josh Suereth** 03:49 Just Ted, go for it.
**Ted Young** 03:51 Yeah, so unfortunately, Martin couldn't make it, he had a family thing at the last minute, and since I have been in back-to-back meetings since I showed up to work this week, I haven't had a chance to really review, but he did take a shot at, making a prototype for this, so I would encourage people to look at This attempt to start hooking up entities and sessions, and then eventually try to make an end-to-end demo that everyone can play with, so we're all clear about what's going on.
And he had some questions… I think in the new design, it's really focused on the issue of metric instruments, wanting to know about specific entities, right, in order to emit metrics that use those entities as, like, a label set, essentially.
But I think there's some open questions about… What about, like, all the situations where you just generically care entities changed?
like, you're an SDK exporter, for example.
So I think he had some questions about that.
**Josh Suereth** 05:11 So, I'm looking at his prototype. Is there a reason he didn't use Daniel Dila's JavaScript prototype for how the SDK would work?
**Ted Young** 05:19 He started with that, he did.
**Josh Suereth** 05:22 Okay.
**Ted Young** 05:27 So, I copied over some of his questions here, but yeah, unfortunately, I didn't have time to prep for this meeting and actually get up to speed, but, these were his primary questions.
So I don't know if you guys have thoughts on these based on what he wrote.
**Josh Suereth** 05:48 No, this, we, we should, we should go through those. Huh.
somehow this didn't show up in my Things to Pay Attention-to-urgently script. Okay.
Alright.
is the only emitter of telemetry bound to the entity. How does this work for entities that should be applied to all telemetry augmentation user application? Browser sessions fall into this.
I think what he's asking about is if you have default instrumentation, right?
So… the assumption here is that you can call for entity and pass the OpenTelemetry API in all the places you needed where you generate that instrumentation. If I understand this correctly, he's trying to attach browser session without… passing the OpenTelemetry API when the browser session changes, is that correct?
**Ted Young** 06:47 I think it's that the API right now kind of assumes… like… everyone knows what's on either side. So, somebody is putting sessions and other things into entities, and everyone on the other end has to know about what got put in there if they want to access it.
Right, so I have to know that there's something called sessions in there.
to go get access to it through this API. And I think that makes sense if what you're trying to do is be specific about metrics labels on a metric instrument.
But there's, like, lots of other situations where you're like.
I just want to generically be listening for, like.
an entity changed. I don't know anything about this entity, but I know I need to segment my batch, or do this or that. So I think that's… that's… Where I suspect some of his questions are coming from.
**Josh Suereth** 07:43 No, I think this is just what we designed is not going to be useful for you guys.
**Ted Young** 07:48 Okay. You were looking at something specifically to solve a problem in the last design around the metric So, making metric instruments, like, like, you know, more sane?
**Josh Suereth** 08:02 We were… we… so, I mean, the problem is with the… with… if you want to do this, like, notification bit.
It breaks the metrics SDK. It is an intra- like, it is… it is horribly, expensive to… to design, implement, make it work.
with, like, notifying whenever things change in that fashion. Right. I am wondering if maybe session should be treated more, like, if we actually have to solve context attributes for you.
And if session should be something like baggage that gets, like, added contextually everywhere. Because I, you know…
**Ted Young** 08:39 It's… but it's not… that's transactional execution context, and this is more like environment context, like… like resources. But it could be there's just more than one API. It could be that metrics specifically need one API, and everything else needs a different API. It could just be… that situation. Because realistically, there's nowhere else… the other places where we care about it, we care about it more like… like a bag of attributes, not like… not, like, metrics labels, right? Like… Like, logs, tracing, like, all the other data doesn't really care too much about which session… which entities are available, they just want To be associated with everything.
**Josh Suereth** 09:27 Yeah.
**Ted Young** 09:27 So maybe that's… maybe it's just two APIs, maybe it's just metrics need… need something special that's just different from everything else.
**Josh Suereth** 09:34 I got to sleep.
This is actually why… I think, dude, I think we're barking up the wrong tree with client-side and RUM here. I think we want a different API SDK.
And, like, I think fundamentally, the problems that you have there are subtly different. Like, metrics just doesn't make sense in your world.
the way that.
**Ted Young** 09:55 Yeah, we also don't have metrics on the browser, right?
**Josh Suereth** 09:59 Oh, boy.
**Ted Young** 10:00 be done.
**Josh Suereth** 10:01 No, you do, you're pushing them in events, and we want to take those events and turn them back into metrics at some point later, but you don't need that SDK at all where you are, right? Like, there's no… in fact, it's almost detrimental for us to throw it to you, because it doesn't work in any way the way you want it.
**Ted Young** 10:19 That's kind of what I mean, like, in terms of, like, how we would create metrics on the browser, we're just planning on creating events, and having something downstream be the thing that That synthesizes You know, a subset of the labels into a metric.
Yeah.
**Josh Suereth** 10:37 I still think So… My opinion is the current API SDK as specified in OTEL, you might be better off crafting a new thing.
Like, crafting a new API for client-side.
That actually solves your problem.
**Ted Young** 10:55 completely… complete, like, throw everything away new API?
**Josh Suereth** 11:00 Possibly, I don't know, like, the tracer might be okay, but the way… the way resourcing works today, I don't think fits… fits you. Like, it… this is… this is where… Ideally, what you would have is you can just mutate the resource freely at any time, because whenever you report data, you're just going to report against the most up-to-date thing.
And you want session ID and resource, but you're not really modeling, like, a resource the way we're thinking about with metrics. Like, everything you're telling me is basically you're violating all the principles and, like, the way our data model works, and that's fine.
Because I think we need to solve browser, but, like, I… yeah, it… The, the… we can't shove… a lot of what you want to do in the general SDK, because it starts to make… it causes a whole bunch of problems. Like, I can show you that prototype I had, where we were firing events in Java, and how ridiculously hard metrics became, and, like, untractable some of those issues would be to solve.
For logs and things, for logs and trace, it's just… I'm generating a span, and I have a reference to something, and I don't really care what's in that something.
And when I send it downstream, I'm just gonna take whatever that reference is for that resource and send it, and I'm fine, I'm gravy, right? And that's what you want here, but you only need that. You don't need a general SDK print… like, you need to say, our SDK is actually fundamentally different, we don't have metrics.
We're just sending events, and we can… we can mutate logs, right?
you might want to start looking at that. I still think we need the multi-sDK thing, the multi-resource and SDK for metrics specifically, but this… this keeps… you know, this is why we really wanted you guys to take a look at this and get an understanding. I don't know if this is going to work for you if you need to actually Because the answer to this today with our prototype would be, you would need to actually create your own reference to the OpenTelemetry that you're using, and anytime the session changes, you have to go reinstantiate an open telemetry and swap your reference.
that you're using in instrumentation, right? And that's gross as hell. Like, you want the SDK to do that for you.
**Ted Young** 13:17 Right, yeah, we would never do it that way, right? The point on our side is that… like, the instrumentation does not care that these things are changing, right? Like, this is information that's getting stapled to telemetry at the batching.
point in the exporter. That's where we're stapling these things together. And at that stage, something like an event listener makes plenty of sense, and it is efficient.
**Josh Suereth** 13:46 And in our mental model for the SDK and things, the idea is resource is figured out ahead of time, and doesn't change, and if we start to break that, the whole metrics SDK goes to hell, right? So, because we rely on that so heavily there.
So this was a way for us to at least allow you to have multiple different resources where you would explicitly make that change, but it relies on the instrumentation still being able to point at a single OpenTelemetry instance, and you being able to, like, say, cool, now the instrumentation, here's your OpenTelemetry instance that has the right SDK.
And the right thing, so that we can control the memory management crap of the metrics thing easier, like, simpler.
**Ted Young** 14:28 I just wonder if this is not a one versus the other, but a yes and.
**Josh Suereth** 14:34 I think it's a yes and, yeah. I think basically what we proposed won't work for you, and you need something else.
**Ted Young** 14:40 Right, but I don't know if we have to go as far as what you were saying and, like, throw… the whole SDK away, or something like that.
**Josh Suereth** 14:49 I wouldn't.
**Ted Young** 14:49 feels like…
**Josh Suereth** 14:51 I would throw away the Patrick's SDK. Like, I think that.
**Ted Young** 14:55 We're not… we're definitely not using the Metrics SDK in the browser, so that's a non-issue for us, but in terms of, like, I still would be great if this felt like a coherent design.
Like, if we came back a year from now, and it's like, gee whiz, some people really want metrics on the browser, and we have to add it now.
**Josh Suereth** 15:11 And what it'd be like… But again, if we just hide metrics in events and say, cool, there are no metrics in the browser, I think that's wrong too. I think we need to understand their metrics in the browser, but we need to understand that the way we report them and the way we aggregate has to fundamentally be different than what we did in our current API and SDK.
**Ted Young** 15:32 Right.
**Josh Suereth** 15:33 So, I think that you actually need a new metrics API specification for browser.
of, like, what to do, how to do it, why you need it, all that kind of stuff, right? For now, you can say, cool, we're not gonna have a spec, and we're gonna rely on using events, and we're gonna rely on doing aggregations against this data downstream, because that's what happens in practice for RUM.
But that doesn't mean you don't necessarily have metrics, it just means that we're doing, like, because of the complications of client-side stuff.
We like to send events.
with a lot of data in them that are highly compressed, and then we extract the metrics and things downstream of those events. This is why… and again, this is why my intuition is, like, you have… a very similar problem to open telemetry, but with subtle differences we have to address in some fashion, right? Like, this is also why I was suggesting, I think the protocol OTLP is wrong for you.
You know, when I think of browser side, it'd be better if you can get a bundle of data all out at once that has your spans, your metrics, and your events all in the same thing.
**Ted Young** 16:39 Yes, yeah, but one thing at a time.
**Josh Suereth** 16:42 Oh, sure. But for now, let's put it all in an event, fire it out the gate, but you might even be… it might be beneficial for you to just say, cool, let's start figuring out what the client-side API needs to look like, and let's allow ourselves to diverge from the current APIs to solve those problems. You see what I'm saying?
**Ted Young** 17:03 Yeah, tell you what, so how about this as a concrete next step? We will go our own way in terms of figuring out the stuff we need to make our model work, and we will use the protocol, since we're all gonna keep doing OTLP, but we're gonna use, like, entity… like, how resources and entities, like, we're going to try to report it in a way that's commiserate with what everyone else expects.
So, you don't know what we're doing under the hood up here in browser. We'll just try to synchronize on the protocol level for now. And then when we have something where we're like, this solves all of our problems, we can present that to this SIG.
And figure out a way to merge that with maybe other entity-related API Stuff that other people want to do.
**Josh Suereth** 17:55 Sure, yeah, I… I, I also think that maybe the specsig is the right place for you to start presenting some of it. Like, I… the problems that you guys are running into need… needs more attention overall.
And my fear is you're still in a world where I know what you're doing, because you're coming here and telling us.
But when we try to run that through the TC, we might still have one of those kerfuffles where nobody knows the context, nobody knows your problems.
**Ted Young** 18:20 Yeah. I think we've hit a point where we need an end-to-end working demo. We need to actually stand this up so you can click through web pages and see telemetry, and go look at code, and be like, this is what we mean. I think as long as it's not… Like, literally, you can get your hands on it and play with it, everyone's gonna probably keep talking past each other.
**Josh Suereth** 18:45 Yeah, and if it were me, like, if I were leading this, what I would be doing is saying, you know what? We're gonna build our own API for now, and we're gonna use OpenTelemetry Event Protocol.
And that's what we're gonna do for that demo. Like, we're just gonna make the demo work, we're gonna make a good instrumentation for the browser, and we're gonna be willing to diverge for now, and get that demo working of what we want this to be protocol-wise.
**Ted Young** 19:10 Okay.
**Josh Suereth** 19:11 And then we'll walk backwards into, okay, here's the things we had to do that are non-negotiable.
around the API that we have, and then let's start picking the… because what happened before was it was all hypotheticals, right? It was all hypotheticals. So if you give us a prototype and a demo that works, where you're, you know, then we can reverse engineer and say, cool, these were non-negotiable things, here's what we really need. Yeah.
**Ted Young** 19:36 But I think I'm realizing part of this demo has to include how do we synthesize… how are we expecting to synthesize metrics out of these events? We also need to include that.
**Josh Suereth** 19:47 In the demo.
**Ted Young** 19:48 That's…
**Josh Suereth** 19:48 Yeah, yeah. If you… I mean, if you throw it into… and again, I'm fine using the Grafana LGTM, because I think it's… it's relatively representative of capabilities in the ecosystem, but if you're like, hey, we got these into the Prometheus instance, and here's how you view it, visualize these.
And here's how we handle the cardinality hell of, like, a thousand phone devices, or web browsers, or whatever. Like, that would be really powerful.
You know?
**Ted Young** 20:14 Cool. Okay.
**Josh Suereth** 20:15 So, and I don't think you need… again, you might even be hindered by the current API. If you're just firing OTLP log events and synthesizing them straight up, you might be able to get this out the door even quicker.
Initially.
Yeah, I mean, we feel like, I mean, the tracing and logging APIs are fine. I don't think…
**Ted Young** 20:37 We're feeling need to change those at all, but it's more just, like you're saying, it's… for this stuff, it integrates more with how batching and exporting works than it does with anything else, so I think we just need to show you all what we're trying to do with that.
**Josh Suereth** 20:55 Right, so you could reuse the API, but then your SDK might actually fire everything down one event or something, yeah.
**Ted Young** 21:01 Exactly. I really… for our purposes, I think we don't need any API changes at all. I think it's… where the API changes come in is when you start thinking about metrics, making metric instruments, and you're like, for this metric instrument, I want to use, like, this entity, and that entity, and this other entity.
And trying to make a nice, clean metrics API for dealing with all of that stuff, that's its own hairball, and I think that's what you guys are trying to solve.
And that's specifically the one thing we're like, we literally don't care about that hairball. Like, we could… you guys can solve it or not solve it, and… and it will make a difference to us on the browser, because that's the one API we're not including.
**Josh Suereth** 21:45 Yeah, I do think that you probably need an API around metrics in some fashion, but the one we have now is absolutely wrong for you. The one now assumes that you have memory that you can store things in.
**Ted Young** 21:56 I think our…
**Josh Suereth** 21:57 Efficiencies and reduction in size, and that is not true for you.
**Ted Young** 22:01 Right, I think our API for metrics… the way we're thinking about making metrics is literally, like, it's all synthetic and happening in a gateway, like the collector, right? So, our API for that is more like some kind of declarative syntax than anything.
Like, programmatic things.
**Josh Suereth** 22:20 Yeah, we have events with fields in them, and we have, like, a set of declarations or simple conversion from event to metric that you can do generically at these gateways. Right. Yeah, yeah. I love that.
**Ted Young** 22:35 Here's the default set of metrics we think you should be generating out of edit these events. If you're sending…
**Josh Suereth** 22:42 By the way, do you know that's why Census exists, and why OpenCensus exists? That's, like, what it was designed to solve?
**Ted Young** 22:50 Which… sorry, which piece… piece?
**Josh Suereth** 22:52 Census was designed around high cardinality and around actually tagging contextual data, which was so high cardinality that existing systems, like the Prometheus of Google, didn't work, right? And then having a gateway actually reduce that aggregation.
Which is what Open Census views were.
Right. And that's why views and measurements are completely separate things.
**Ted Young** 23:12 Exactly. We're basically saying, like, views on top of events, and shipping people with, like, a default… Set of, like, you know, blueprints that they can throw in.
If they're trying to send client data to a more generic backend instead of some client-specific backend.
**Josh Suereth** 23:30 See, that all makes sense to me, then. So I would just recommend for now, Make your own SDK.
**Ted Young** 23:38 Because for a lot of… if they are sending data to a client-specific backend, here's the thing, you don't even want to synthesize metrics, right? That backend is going to do its thing, whatever that is, and it's just… it's just pure overhead.
For us to be generating that along the way, if no one at the end Cares about it, because it's going to do its own thing with the events.
**Josh Suereth** 24:01 Yeah, yeah, so…
**Ted Young** 24:03 Okay, okay, this is all very helpful. I think we know how to be unblocked from this SIG and move forward with, not just browser, but also Android and Swift.
And we'll just try to coordinate more with each other, and give updates here and at the main specsig.
**Josh Suereth** 24:25 Yeah.
**Dmitrii Anoshin** 24:26 a similar kind of situation of the collector. In the collector, we don't use Go SDK to produce, for example, metrics or events and the receivers themselves. So we, like, we…
**Ted Young** 24:36 Look at the protocol, and…
**Dmitrii Anoshin** 24:38 provide a, like, an easy interface for the end users to define their receivers through the, like, YAMLs, specifically… specific YAMLs, metadata YAMLs, which generate the API, which is not… like, which doesn't depend on Go SDK at all. And, we, like, there are pretty similar problems that we would need to… we need to resolve. Actually, like, one of the questions in that issue, last questions, how we define multiple entities. This is one of the problems that we had to resolve on the collector, and I can, like, later I can show how it's done there. And maybe we can inspire each other. Yeah. So, yes.
**Ted Young** 25:21 Yeah, I mean, I think we'll literally be doing it in the collector, so it's like… Code reuse time.
**Josh Suereth** 25:28 Yeah.
Cool. I, I think… I think we can make a lot more progress now, going forward, so I'm glad we got this feedback. Thank you for taking a look at this and getting some feedback to us. If you need us, I, the, the client-side stig is at such a bad time for me, but if, if you need us to attend at some point, or you want to talk about this in the spec call…
**Ted Young** 25:50 call is the better, better place for it. I think, you know, we can come here, and the spec call, and then just GitHub,
**Josh Suereth** 25:58 Yeah.
**Ted Young** 25:58 So…
**Josh Suereth** 25:59 I would… I would also recommend, you know how we're trying to do the highlights of the spec call, where we highlight different SIGs? I would… I would bring that early. I'm… I'm really nervous. With… with what we're talking about, I get what you need.
We need to make sure the TC is aware of what you're doing, and that all of the questions that we talked about, how long it took us to get to where we are, is written down or somehow accessible in ways that doesn't lead to Other fun, yeah.
**Ted Young** 26:28 I think we need to deliver that, but I think… we… without a working demo, it's still gonna be everyone feeling part of the elephant. So, I think… I think that's what we need. We need to kind of go away, stand up a working demo, and, like, present that with, like, a paper that explains what people should be looking at.
**Josh Suereth** 26:49 Cool. I would also, not, over-index on the quality of the demo being, like, mergable and usable. Good, because that's the other… my other fear is… yeah.
**Ted Young** 26:59 But you can, like, see telem… it's end-to-end, right? You can see… We're like, we mean literally this, nothing more, nothing less.
**Josh Suereth** 27:09 Cool.
Alright, let's move on to, Dimitri's topic, if that's alright, I think we'll call.
**Dmitrii Anoshin** 27:16 I can actually probably proceed with collector updates, because they are kind of… there are some over… there is some potential overlap, and maybe it makes sense, because entity events seek is a completely separate story, right?
So… Maybe I can share my screen?
Cool.
**Josh Suereth** 27:37 Go ahead, my cat really wants attention, so she's in the way of my keyboard and everything now.
**Dmitrii Anoshin** 27:42 Okay, so, we do, like, the receivers and the collector is, like, how you get metrics. There are some push-based receivers, like, when you OTLP, but there are pull-based receivers when you actually… pull data from separate sources. Typically, it's somewhere from the outside, and we have this receiver, Kubernetes cluster, Kubernetes cluster receiver to get, like.
cluster-level metrics from Kubernetes API.
And last time I showed how we defined metadata YAML, for, like, for entities.
And with some, like, And that, that definition of entity will create another, go, like.
Go API to, emit metrics specific to those entities, so I made that.
Let me… It's actually… Share… sorry.
container… usage of that API.
the API is generated, and so, before that, how it used to be, container is pretty complicated, but before that, we would… iterate over available objects in Kubernetes API Response, and we will just build… build the resource first.
Assign, like, particular attribute to that resource, and then we generate metrics.
and then put it in the resource. And that API records particular data points for particular metric. This is generated from metadata YAML, but there is no association between resource there used to be no association between resource and metrics that you can generate, so you can essentially generate any metrics and assign them to any resource with any attributes. Now, what we have instead with the new builder that produces new API with entities in mind, is that we have the new function.
called, let's say, 4KS container. This is also, like, generated with… this is just the usage of that API. And we put an entity there. And entity is being built similarly how resource was built, but a particular entity can only accept specific attributes and specific related entities.
So you cannot put anything else there. And also, you cannot emit any other metrics, from that builder. Now, you can only Emit container-specific metrics.
So, like, this association is fixed now, which is good, like, once this pair is merged, I mean.
That's… that's, one thing, and how it is related to the… To the point that we discussed before, how we associate several entities to one resource, is that we define relationships in the metadata YAML file, and that relationship generates this, function.
Because port, container is a child of a port, and now we can set an additional port entity to this container entity.
And as a result, both of them will be added in the… In the resource that is being emitted, after… After we record all the metrics.
So I think, like, at least to answer that question, we can send something to the browser stick as well. You can either emit metrics from the port entity, or for the container. George, go ahead.
**Josh Suereth** 31:56 Yeah, how are you doing the child… so first of all, the child parent stuff, that's only local to the collector, that you keep Reference of that.
**Dmitrii Anoshin** 32:06 Right.
**Josh Suereth** 32:07 But it does seem so, like, kind of cool and useful. So basically, what you're doing is you're saying, I want to report data against this entity.
And, by the way, this entity is a child of this one.
**Dmitrii Anoshin** 32:20 And then you'll implicitly add the identity of its parent?
No, you would need to… parent entity, you need to, like, pass entity itself as well.
**Josh Suereth** 32:31 So, like, what is an object.
As an object, okay. But how are you using the child relationship, then? Like you said, if I report an object against an entity.
**Dmitrii Anoshin** 32:39 not being used. The type of relationship is not being used at all, because right now, all of the entities in the resource are flat. Until we have any distinction between them, we just ignore the type itself. The type is being used to generate API only.
goipe.
**Josh Suereth** 32:54 I see, I see. No, what I meant was the relationship, so right when I say set child of Kate's pod, right?
That's just for the entity signal. That's not being used, like, in resource.
**Dmitrii Anoshin** 33:09 For the entity. No, this is, like, this is being used in the resource just to add another entity. So, essentially… Right, that's what I'm…
**Josh Suereth** 33:17 Yeah. So if I say this is a child of the other entity, then the other entity gets added to the resource. So I say, like, hey, the resource is going to be about this entity, but if I say this is a child of it, then you're going to add the other resource as well. Is that generic across any relationship that I declare?
**Dmitrii Anoshin** 33:35 We can, potentially define that, if that, like, this relationship needed in the resource or not. For now, I just… I just keep it simple. We can extend it later on, but for now, any relationships being added to the resource, yes.
**Josh Suereth** 33:51 Yeah, I like… I kind of like what you're doing. There's… there's a whole can of questions I have around it. My overall thing, though, is, like, if you… if you think that's useful for how you construct a resource in the collector.
**Dmitrii Anoshin** 34:04 Yeah.
**Josh Suereth** 34:05 I'm worried… I'm worried that we're not planning to send relationships downstream anywhere, you know?
**Dmitrii Anoshin** 34:11 No, in general.
**Josh Suereth** 34:12 Right, so only the collector would know about that relationship and be able to use it.
**Dmitrii Anoshin** 34:17 Yeah.
**Josh Suereth** 34:17 But if that's useful, it might be useful also in the API.
and the SDK.
Of the client. And then, if it's there, and it's in the collector, but we never communicate it.
Are we then going to say, okay, now we want to communicate it? That's kind of what I'm getting at, yeah.
**Dmitrii Anoshin** 34:35 But we need to define that first. Like, there is no, like, it's not defined in the proto, right? Once it's defined in the proto, we can, like, align them, and make them work together, right? So, for now, I just wanted to solve a particular problem. We don't have any association between metrics and entities in the collector. It's all, like, a bit all confusing, and that specifically… that relationship was added to resolve that problem, if that makes.
**Josh Suereth** 35:06 Yeah, I… I… if I understand what this is doing, I really like… The implications of what this can do for you in, like, simplification.
Yeah. Any, any other thoughts from anyone else here?
**Ted Young** 35:27 Nope.
**Dmitrii Anoshin** 35:29 One thing I wanted to discuss as well is that currently.
in the collector, I don't want to change any data except for adding entities layer. Like, the full set of resource attributes that user get, user can disable particular attributes, enable them. I don't want to introduce any breaking changes to the emitted data at this point.
The thing is, is that before oof.
like, not before, currently. What is being emitted is that we have pod UID, we have pod name in the container matrix, for example, but we only had node name, only have node name, and only had namespace name.
So we cannot introduce entities for those.
So, currently, in order to just, like.
keep whatever we have, and do not make any breakage changes. I introduced this thing to the builder, YAML.
Give me more… I introduced this thing called A relationship is here, oops, sorry.
And I'm probably here.
I bet they are.
Don't see this.
Meta, beta.
Damo.
Okay.
Yeah, I had to replace.
a relationship to no namespace, because it will bring you ID, which is gonna be kind of a breaking change for the end user. And I added just, like, another section called, extra attributes. And that extra attribute, let's say, like.
Contextual, like, additional information, which typically comes from related entities, but we don't add those related entities yet, and I'm not sure how to solve it going forward. Do we want to introduce namespace UID by default? We probably still don't want to introduce it by default, but we can make it, like, a configuration interface for that.
So user can enable if they want to, but eventually I want to switch to this one anyway. So that's, like, just… like… kind of… minor, adjustments I had to do to, not break users at this point.
Does that make sense?
**Josh Suereth** 38:04 Yeah, yeah, this gets into… I think we talked about this last time, of, like, if users only want namespace main name, but we decided that UID is the identity, did we make the right choice? But that's a different, yeah.
**Dmitrii Anoshin** 38:22 Anyway, I'll keep it like this, and then later on, I'll figure out how to make it entities in the definition, but potentially keeping the existing Like, data being emitted as is by default.
And if user want to enable namespace UID, they just, like, pass a flag and configuration interface for the collector, and then it creates a new entity added to the resource.
**Josh Suereth** 38:52 This is cool, by the way, like, this is good work here, man.
**Dmitrii Anoshin** 38:56 Cool, thank you. Yeah, I think… so, it's, for me.
**Josh Suereth** 39:00 By the way, there's a piece of me that is currently working on Weaver that looks at your metadata YAML, like, why can't we just be friends?
**Dmitrii Anoshin** 39:09 I have some problems in the collector that needs to be resolved quicker, so, like, yeah.
**Josh Suereth** 39:17 Yeah, yeah, yeah.
No, that's… that's a… that's a longer-term discussion, but it just… it's funny, the stuff that you're doing and the stuff that I'm doing. Like, literally, my PRs are all YAML-based code generation crap right now, and yeah.
**Dmitrii Anoshin** 39:30 Yeah, long-term, we definitely need to, like, converge, and if you see the ref, this is the inspiration from the V2, I guess.
So I'm, like, I'm trying to some extent, like.
**Josh Suereth** 39:43 Yep.
**Dmitrii Anoshin** 39:43 To not break a lot, but there are some cons of that needs to be separate.
For now.
**Josh Suereth** 39:48 So, one fun thing for you, if you haven't tried this yet, when you need to do BS stuff.
like, really annoying code. Lyudmila had success where she wrote the YAML definition.
and then wrote an example, like, Go file that you wanted to generate, and then ask an agent like Claude or Gemini, which I have to mention.
**Dmitrii Anoshin** 40:12 Bye.
**Josh Suereth** 40:13 But ask it to, like, automatically create your template.
**Dmitrii Anoshin** 40:18 Yeah.
**Josh Suereth** 40:18 It's actually good at that, if that helps you accelerate here in any way. Just say, here's what I want, here's what the definition is, go make this work and don't change either. We're having some success there.
**Dmitrii Anoshin** 40:31 Yeah, I'm looking…
**Josh Suereth** 40:32 Telemetry Weaver packages, for example, an example of stuff that we're doing with that, yeah.
**Dmitrii Anoshin** 40:36 Yeah, I heavily use Cloud and, like, prototyping on some, like, generated kind of, doc, and then ask it to reverse engineer it to the template. Yeah, it works perfectly.
**Josh Suereth** 40:53 Cool.
**Dmitrii Anoshin** 40:55 I guess that's pretty much it from my side. Don't need to cover anything else. And also, I've updated the… spec PR for the entity events. Like, last time you asked how can we put relationship information to the resource? I have a few ideas, but I'm not sure if that has to be in that… in that PR, because that PR is specifically about events, so I'll probably maybe create another issue or another PR to the resource, and with my proposal.
Are you on mute?
**Josh Suereth** 41:33 I was looking at… I was looking at a window of your… your PR. The… the resource thing… I have… I should clarify what my blocking comments are, right? So, Will we need the relationship, will we need attributes and relationships as fully blocking? The blocking comment on will we need the relationship information and resource is more a blocking comment for, stabilizing the proto as it is today.
Right? Because in the proto, we don't have relationship in resource. And the question is, we were trying not to put it there.
**Dmitrii Anoshin** 42:07 And I think we want to continue down…
**Josh Suereth** 42:10 This exploration of how we're going without putting it there until we know we need it.
But I don't want to stabilize the proto-changes on resource.
**Dmitrii Anoshin** 42:22 Okay.
**Josh Suereth** 42:22 If we still have that as an open question. So that's only blocking that stability, it's not blocking your PR. The only blocking change on your PR, blocking is just, hey, like, do we need to have attributes in the relationship?
And I think you said, I can propose a problem… I can propose something to resolve this problem separately, given the PR is focused on entity events, should it be included here? That's the resource thing, and yeah, I think you're right, we can push that off.
But the… the attributes on relationships, that's the one I think we should probably figure out in the PR.
**Dmitrii Anoshin** 42:56 So I removed that. I think we discussed that it's fine. It's fine to remove it, and later we add it if needed, because that's gonna be… Set, like, a list of relationships is a descriptive kind of thing, right?
So it can change through the lifetime. And adding another descriptive thing on the real… one of the relationships is not gonna change anything. It's gonna be, like, an additive change, not a problem at all. And given that we don't have any use cases, like, necessary… Necessary right now for the attributes on the relationships.
I would… I think… Are you living it out makes sense.
**Josh Suereth** 43:39 Gotcha. Okay.
You're saying we can add them in a non-breaking way in the future?
**Dmitrii Anoshin** 43:45 Right, exactly.
**Josh Suereth** 43:47 Let me take a quick gander. I'll just re-present this.
Let's see… we're here… we're here… and again, this is… this is not the OTEP, this is in the spec, so we have… Required attributes, optional attributes, relationships is an array of maps.
And the map… the string is the type of the relationship, right?
In the map, where is relationships defined?
Each of those are going to find in this. It's in a map containing… array is a map containing the type and the ID. Okay, so the… this is a really dumb knit, then. It's an array… oh, it's an array of maps, so you're fine. Okay.
Because it's an array.
And then we have type, and… right, I think when I was first complaining, I saw it as a map of string to any, and the string was the type, but you cleaned that up, so we're good.
Cool.
Yeah. Alright, I am… let me re-review it, just to make sure I remember everything in it, and then I'm fine approving that, probably.
I do want to see… I think we still don't have a lot of our stuff ready to merge here. So, like, this one here… Yeah, our entity merge algorithm is still kind of open. I don't know if there were any new concerns raised since our last meeting?
**Dmitrii Anoshin** 45:25 I was just about to, approve it.
Before the call.
**Josh Suereth** 45:31 Yeah, this one, I'm… I am working on this, we'll put a few examples, just because I think people aren't reading the prototypes, and it's fair to have an example for people to see what it does in the data model. That's fine.
I don't think we've done that in any of our other data models, but I'm fine adding it for clarity.
And then… What was the other? We had another one in here.
You have your events, we have merge, and then we have the project, the OTEM. Is this… Oh, here's one for us, I think, if we haven't talked about this, we should talk about it here.
this is trying to clarify that resource describes an observed entity, as opposed to source. This is for eBPF folks, because, like, and we've talked about this in the SIG a lot, about a remote observer.
I think you saw, maybe there was the brief Slack discussion that we had on this. I was about to mark this as approved. I need to go… read some of the verbiage, because I had changed some things, but this is, like, instead of saying you identify what produced the telemetry, we're calling it the observed entity. So this is, like.
It gets complicated with eBPF, because the data might be coming out of the kernel.
And so, if we were to say it's the thing that produced the data, that's kind of true, but kind of not. And so, just to make it crystal clear that, like, if I'm using eBPF to observe a process, my resource should be the process, not the eBPF code. Does that make sense?
Similar to what you're doing with, like, the Prometheus receiver resource, or the, like, the database receiver resources in the collector that are talking about something else, you know?
Okay. So yeah, if you have a chance to review this one, that'd be good. I think this is a good clarification. It changes our, the logs data model, it changes the resource data model, it changes, the resource readme.
The… the… oh yeah, that's right. This is the part that I… might complain about?
This note is a little too specific.
We can talk about that one in more detail, but I'll make my suggestions on the PR. I didn't finish that before this meeting. And then… this one… Yeah, resource must identify an entity that is producing telemetry. It must identify the observancy for which telemetry is being produced.
Yes.
this is where things get awkward in my mind, like… We need to account for eBPF, but conceptually.
This is the conceptual thing, and it's much easier to read than this.
Even though this is more true. So, is, I'm kind of curious what folks think about that. Like, I… I don't want eBPF to get confused, but man, I still… when I read this, with the four witches and the is-being, like, it starts to feel more harder to understand.
But I could just be, like, nitpicking. How do folks feel?
Okay.
**Dmitrii Anoshin** 49:00 I have no comment at this point. I guess, for me, It's just how we… like, how I think about it. So, both old and new version kind of makes sense.
If we think from the perspective of the producing telemetry entity and observed entity.
Yeah.
**Josh Suereth** 49:24 I'm just trying to figure out which one will lead to less confusion in the future.
That's… that's my take. Anyway, cool. If you haven't… I think this is generally a really good cleanup and a really good call-out, and this is probably the most important bit.
of the PR to pay attention to, and so I'll probably have a little bit of nitpicky tweaks here, but generally, I'd like to see us move quickly on this one, particularly to help the eBPF folks know what resource needs to be.
We had, for context, in the profiling sig, they initially didn't understand how resource was supposed to be used, and so they were putting all their resource attributes inside of the profile itself, and the resource was relatively just empty, with nothing in it.
So I want to make sure that it's clear that what we intended to be used, how it's used, and, like, that kind of crap across hotel.
**Dmitrii Anoshin** 50:14 This one, actually, first change is kind of, I think, makes it worse, because source of the lock is pretty much the same. It doesn't matter whether your source is instrumented by itself.
Or if it's observed by some sort… like, by some sort entity.
**Josh Suereth** 50:32 Yep.
**Dmitrii Anoshin** 50:32 pool data.
**Josh Suereth** 50:33 Exactly, so please make that comment. Like, I think, again, I think the clarification here is important for eBPF, and the clarification here is the most critical part of this.
**Dmitrii Anoshin** 50:45 Okay. I'll, I'll, I'll review this. Thank you.
**Josh Suereth** 50:51 Awesome.
I think that's it for… today's agenda. I don't have… outside of that merge algorithm for which I need to generate examples, which is next on my to-do, I don't have anything active, so I might, just check quick on some of our… Project board.
Right.
Ted, given the discussion we just had around entity manager OTEP and, like, some of the things we wanted to do.
I'm thinking of killing this.
**Ted Young** 51:37 Sure.
**Josh Suereth** 51:38 And, like, let's re-figure out what the plan is that we need between SIGs from there.
Is that fair?
**Ted Young** 51:46 Yeah. Okay.
**Josh Suereth** 51:47 Adding resource attributes, post-creation, for example, auto-discovery. This one, I still need to move somewhere, so I'll move that out. Cool.
Under In Progress, I believe we talked about all of these.
Daniel has a proposal for that. SDQ startup specification, yeah.
Cool.
Can collector differentiate between remote versus local? This is one of our things. I think… Dimitri, you're showing some examples of that in collector work.
this… Issue as it's phrased.
Do we want to rename it to be what you're actually doing? Should we change it to be, like, let's put a prototype together around this? Like, what do you want to do with it?
**Dmitrii Anoshin** 52:36 This will be in the scope of the work I'm doing. The work I'm doing is bigger than this, but this one, I'll get to it.
**Josh Suereth** 52:44 Right, I'm thinking of just changing it, to, be, like, Show a demo of how the collector processors differentiate remote versus slow.
**Dmitrii Anoshin** 52:55 Sounds good.
**Josh Suereth** 52:56 That's out.
**Dmitrii Anoshin** 52:57 Yeah, sounds good.
**Josh Suereth** 52:58 Okay. That way, you have a very clear definition of when we can mark it done, because I think the way it was phrased was, Bad. Okay, then we have, oh, we were here.
Communicate breaking change in specification around resource. I don't think we're ready for this, because we actually aren't… we don't have enough in the specification to go out to SDKs yet, so I don't think we're ready for this communication. This is blocked in actually getting SDKs, which is blocked in having the spec PRs merged.
okay.
Generate entity configuration interface for metric scrapers. Do we need to talk… this is… you were just showing this.
**Dmitrii Anoshin** 53:37 Yeah, exactly.
**Josh Suereth** 53:39 Yeah. Should I move this to in progress, then?
**Dmitrii Anoshin** 53:41 It's, yes.
**Josh Suereth** 53:43 Okay.
**Dmitrii Anoshin** 53:46 Thank you.
**Josh Suereth** 53:47 Cool.
I think I'm gonna add an item here of, right.
I'll just make it pretty… a draft, oh.
Oh my gosh.
What the heck happened, man?
Delete.
This is… that's so annoying. So I click add item, I have to type everything first. Okay, finish SDK specification, so we can begin implementing… entities in SDKs, against, you know, beta.
Or experiments.
spec.
Okay, I'm gonna add that as a draft thing. This is… this is, like, the next thing I want to kick off here.
of where we actually have entities in the SDK, so you get it in the collector. I think we're still blocked on this merge algorithm getting merged, and then we need to do other SDK spec things. We can flush that out. Is there anything else under Phase 1 that we think is blocking us?
No.
Okay.
Cool!
All right, if you haven't reviewed or added things into the merger algorithm yet, please do. I will add those examples, and We'll see y'all next week.
Say, everybody.
**Dmitrii Anoshin** 55:21 on.
