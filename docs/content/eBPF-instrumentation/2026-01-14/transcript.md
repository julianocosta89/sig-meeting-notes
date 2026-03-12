SIG: eBPF instrumentation
Date: 2026-01-14
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:43 Hey.
**Florian Lehner** 00:46 Okay.
**Tyler** 00:48 How's it going?
**Florian Lehner** 00:50 Fine, fine, fine, I'm fine, what are you?
**Tyler** 00:52 No.
Hey!
Whoa.
**Giuseppe Ognibene | Coralogix** 00:58 Hi, everyone.
**Tyler** 01:01 Hey.
**Giuseppe Ognibene | Coralogix** 01:03 How about it.
**Tyler** 01:20 Yes, we could probably wait, another minute or two. Doesn't look like we have much of the crew here yet, so we'll do that. But yeah, if you're on the call, if you haven't yet, go ahead and add your name to the attendees list.
And if you have agenda items you wanted to talk about, go ahead and add them there as well, and yeah, we can get started here in just a second.
See, Mario has joined, so yeah, I'm guessing… Guess we got people coming.
Giuseppe, do you know if, Nimrod and, Mattia are able to join today?
**Giuseppe Ognibene | Coralogix** 02:28 Yeah, Mattia just joined.
But I guess it would…
**Tyler** 02:34 Okay.
**Giuseppe Ognibene | Coralogix** 02:35 We'll send a message.
**Tyler** 02:37 Yeah, we can wait a little bit then.
This is Steve Moon.
**Giuseppe Ognibene | Coralogix** 02:43 fear.
**Tyler** 02:48 Oh, there he is. Okay.
Cool. I think the only person I don't see is, Nicola, but I'm guessing he might just be late, so… We could probably jump in here in a second.
So yeah, to those just joining afterwards, welcome. If you haven't yet added your name to the attendees list, please go ahead and do so.
If you have agenda items you want to talk about, also, please go add those, and then, yeah, let me start, sharing my screen, and then we can jump in here.
That's… let's see if we can free that one out again.
One of these days, I'll figure out how to use Zoom.
Okay, cool. You can all see my screen, right? The, agenda doc?
**Stephen Lang** 03:48 Yep.
**Giuseppe Ognibene | Coralogix** 03:49 Yep.
**Tyler** 03:49 Perfect.
Okay, so it starts off, Florian, you wanted to talk or ask a question about, vanity URLs?
**Florian Lehner** 03:57 Yeah, I just saw your, response and the issue. I was not aware there is already a venity URL, registered with UBI.
But, then I will probably, take the task on using this in all the packages, because with the vanity tool, I think at the moment, it's not discoverable at all, and so, the whole project would fit more into the hotel ecosystem.
So, if this is fine by everyone, I will just assign the issue to myself, and we'll probably open a PR in the next couple of days.
**Tyler** 04:37 Yeah, absolutely. If… yeah, I didn't realize there were still issues, with places not using the vanity URL, but they should, so yeah, 100%, please do so, yeah.
**Florian Lehner** 04:49 That's all, I think.
**Tyler** 04:52 Okay, awesome.
Thanks, Warren.
Okay, next up, Nicola is… kind of starting us off here, but, so yeah, this is kind of the main thing I wanted to talk about, and so it looks like a few people are also adding some topics. So, I wanted to talk about our roadmapping ideas and some ideas for… just, topics that we want to tackle in the upcoming year, and I asked last meeting if we could, you know, maybe brainstorm some ideas, on your own, and then come back if you have some ideas.
We'd love to, I think, collaborate on them.
So, I think maybe what I'd really like to do is, nicholas definitely added a lot here, and I've actually added a little bit as well.
So maybe we could just go through this really quick, and I'd love to then ask other people on the call to, you know, if you have things while I'm talking, just go ahead and add them as a topic here as well. But if you also have things that you wanted to talk about.
That, are, motivated by things we talk about here, I think that, like, we want to just get, like, all the ideas, and then calling can come afterwards. So, yeah, I think that's kind of… kind of the goal.
So yeah, Nikola was… I think… let me double check he's not on. Oh, Nicola is on. Okay. So, I can just go through these really quick. I think that I definitely wanted to maybe touch base more on some of these, but yeah, Nikola, just correct me if I'm wrong on some of these, on, like, what you mean, I guess, is what I'm thinking.
So you were talking about stabilization of features and performance, working towards a 1.0 release, so topics, you're being, performance, obviously.
Log correlation works really well. Hotel collector receiver, extended network metric types, based on Nimrod's proposal to make them more useful.
Maybe also work on the hotel profiler.
Update all metrics and traces to make sure it's up to date with the latest semantic conventions, absolutely. Better service metadata when using, when not running in Kubernetes.NET context propagation works, at least for .NET 9+. If we can make it work for 5+, that'd be great as well.
Also, a topic is make OB work really well with OTEL SDKs, so if an OTL SDK has traces enabled, then metric exemplars should also be used, or the OTEL SDK should have that information.
We want to wrap.
Any trace SDKs with Obi, allowing the trace SDK request timing information to be as accurate as if traces were generated by Obi.
Consistent labeling with SDK-generated telemetry.
Also, increased protocol coverage, MQTT, AMQ, AMPQ, NATs, other high-level protocol parsers would be great. Runtime metrics with Obi, so we get a lot of understanding of, like, OBI itself, so GC metrics, NERV threads, Nerv Go routines.
Other items that I added are, specifics for stabilization configuration. I really want to make sure we have a good review of the configuration, because that's something that won't change, once it gets stabilized.
integration with OpenTelemetry declarative configuration. We've already started working on this by supporting, schema formats, around our declarative config… around our configuration.
Another topic is telemetry naming, semantic convention compliance, so kind of similar to what Nichol also added up here.
Nimrod, I've seen you also add, excluding the points above, so gRPC context propagation, Rust Tokyo context propagation, improved support for MongoDB, compressed payloads, so less than the V5 support.
Integration with existing applications, sending telemetry, so allowing combined manual interpretation with OB auto-interpretation.
Reduced overhead by using, tracing programs instead of K-probes.
Experiment with programs, batch, attach APIs, that's interesting, I'd be interested to hear more about that. Http, full payload extraction, full header and payloads on spans with obfuscation and fun stuff.
So, yeah, a lot of great stuff here.
I think maybe I will, just ask if there are folks, maybe they don't have access to the doc for some reason? I don't know why that would be the case, but if you wanted to maybe just, if you have other topics you wanted to add, go ahead and let's pause here and hear you.
Cool. Well then, let's maybe go back through this a little bit. I'd love to get a little bit of clarification, or if people have questions about some of these. So, I definitely wanted to ask Nicola about this .NET stuff. We were talking asynchronously yesterday about it as well.
I did… So, I… I was confused, I think maybe in our conversation, it sounded like we didn't have any .NET support. I ended up upgrading this, like, token application I was running in, like, this distributed context propagation, and it did look like it worked for .NET 10, and I'm guessing maybe 9 as well? So, okay. I'm seeing your… Okay, alright.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 09:53 Yeah, yeah, okay, yeah, so… because they propagate it for us, so we just properly read it, and then we use that, so…
**Tyler** 09:59 Yeah, and I was, I was talking with, Robert Pogg about this, who's my colleague, and he was saying that prior to .NET 9, they were, they were, they were propagating it, it's just it was the wrong format that they were propagating. Like, they weren't truly propagating W3C, like, context propagation and baggage standards.
So, like, there was, like, some weird mismatch there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:19 That's epic. You know what? Then it's gonna make our lives so much easier.
**Tyler** 10:24 Oh, really? Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:25 Okay, so, because this, then, then that will just work, because if you look at that line I wrote, like, we can wrap SDK traces with Obi, so what we're thinking of doing, is something we discussed a few meetings back, I think before the new year, I think, we talked about maybe injecting, on incoming requests. Because right now, we inject an algorithm request, but I mean, the same logic can apply on incoming.
So, which means, with .NET, we can inject One of these bad headers?
And they will propagate it for us, and then on the other side, we'll read it and convert it to proper open telemetry.
Or our metrics, because we…
**Tyler** 11:06 Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:07 I can add the header, have them propagate it, just… Parse it again in this wrong format.
and produce the right telemetry with OTEL.
So, if that is how it works, which is what I think our internal, like, Matt Hensley.
told me, but I didn't quite get it.
Give this on by default, then… That's… That's awake.
**Tyler** 11:34 Yeah.
I think… I think that makes sense. For my experimentation, it seems like that's the case, because one of the other things that I did in .NET 8, I ended up hooking up the, the agent, like, the OpenTelemetry agent with it.
And I think what that does is it, like, takes the wrong format and maybe duplicates it or something like that, but it also propagates, like, a correct W through C trace, like, encoded, trace context, like, header, and things started to match up as well in, like.NET 8. So, like.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:02 Okay.
**Tyler** 12:03 there was.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:03 Yeah.
**Tyler** 12:03 A lot of other weird things going on there as well, but, like, I did see full, complete traces at that point as well, so… I think you might be right. I think there may be just be… some… some mutation that we need there, then. So, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:16 Yeah, I mean, if we write… I mean.
without a header, I think, we won't be able to do anything, because they… there's no incoming header, they will not propagate anything. But if we give them this wrong format header.
My guess is they'll propagate in the wrong format, and all it takes for us is to inject the right format.
And then, write the telemetric, so…
**Tyler** 12:41 Okay.
Yeah, okay, interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:43 Good news, good news, yeah.
**Tyler** 12:44 Yeah I think more investigation, but this is maybe a little bit, yeah, awesome. So… Yeah, that's great. I think also, like, this answer of using a modern, like, the most recent version of .NET is great as well, because I was pretty worried that we were just not supporting this, but I think it, from what I saw, it was working, so, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:01 Yeah, yeah, yeah.NET 9. Yeah, I was just… I needed to test that. I haven't had the time, but after Matt told me that, yeah.NET 9 will propagate it for you, and I was like, oh, really? You know, okay. Then I just need to make sure we read it correctly, and…
**Tyler** 13:15 Yeah, yeah.
So yeah, maybe, this is another one that I was interested in asking a little bit of the details of. So you wanted to wrap the SDK traces with OB, so essentially this is a bi-directional, like, communication protocol, essentially?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:31 So, here's what my view was. I'm not sure, still, like, maybe I'm not seeing all the possible edge cases here, but… So, this is a long-standing thing we've always told people, and it's true. I mean, especially if you have a… A service that's overloaded.
what you're getting from SDK-based instrumentation, let's say you use the Java agent, You're getting the service done.
But, let's say your service can handle 10 requests per second.
Whatever, that's how much… whatever your service is. But you're sending 100.
the… the… what the SDK will give you is gonna be… Completely false information, because it's gonna give you how long each request took, but it will not give you how long each request waited to be served, because maybe you have only 10 threads in the thread pool.
But you want to send hundreds of clients at the same time.
So then they… because this information… this data of waiting in the thread pool, that's on the… whatever… Netty or other threat pools that people use, and that time is not measured in the final time that you're going to get from OTEL to say, this is how long it started a request.
So… but with Obi, we track the request as soon as it comes through the kernel pipe, right? So, as soon as it comes on the network, we start tracking it. So, how long it got stuck in the internal In internals of the… Of the framework that's serving the threads, let's say thread pool of 10.
It's gonna calculate that time, too. And we split it, so in OB, we say queuing time, and then processing time.
So then… if you're building SLOs on top of this information, then with Obi, you're gonna get the right SLO, and you're gonna be like, oh, I'm breached.
But with an SDK, you will likely get… yeah, everything's fine, because it serves… the request correctly.
**Tyler** 15:32 Okay.
Yeah, I was kind of actually wondering about these, like, in-queue and then processing spans I was seeing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:40 That's what it's for, and usually in queue is short, but if you overwhelm a service, enqueue will be dominant. Your processing time will be, like, milliseconds, but then your in queue will be seconds. We had a, like, I think Mario, first time.
talked about this at PyCon.
And we had, like… it's, like… And it's totally normal. Like, at the time that I worked at Microsoft, and we did a bunch of work for LinkedIn, and… There's instances like this, like, clients are reporting one time, but then… The server is reporting completely different time.
**Tyler** 16:14 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:16 The reason is, like, in your logs, you're logging your request times, but it's not the actual… it's not… you're logging the service time, it's not the actual request time that the client sees.
If your client is outside of your organization, let's say you're serving traffic to the internet.
Who's to find out?
What the requests… how long they're actually taking.
So… technically, what I was thinking now is that Right now, they're… like, let's say the implication is instrumental with SDK. We currently, if it's doing SDK instrumentation, we avoid it.
Right? We don't want a duplicate calendar.
we say, Yeah, this service… Exports its own traces, leave it alone.
what I was thinking, instead of doing, is that… We can watch the incoming trace header, transparent header.
And… put that in OB.
then… change it.
for the SDK. So the SDK will not know what the… so, changing in the sense that we keep the same trace ID, but we make the parent the OB trace.
then the OB reports only the… that trace, the queuing time.
And then the SDK reports the rest of it, not knowing that Kind of injected its own parent in between.
**Tyler** 17:45 And this is a… essentially, this processing command would get replaced with what the SDK is reporting?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:50 Yeah.
**Tyler** 17:50 Yeah, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 17:51 So the SDK will report everything, you'll get a super rich, nice trace from the SDK with all the bells and whistles the SDKs produce, which will be really beneficial, but you're also gonna get this queuing time.
The only thing that I'm not sure how to do is that… They'll both appear as server spans, so it'll be like a nested server spam, Not great, but…
**Tyler** 18:16 Yeah, it's not, it's not the end of the world, but yeah. Yeah, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:22 So it will look like, exactly like OB spans, which the in-queue time will be present, and that'll be the time that OB reported until the start of the request, and then Request reports his own timing.
Essentially, we augment the tracing of regular SDKs, which is another value out of Obi, then.
It's not just you run OB when you don't have SDKs, but Hey, this could be even better, that you could run OB together with the SDKs, you get super rich traces, but also accurate timings.
So it doesn't have to be either one or the other.
**Tyler** 18:57 Yeah, okay.
That sounds good. I think there's a lot of great value here. Thanks for explaining that. I definitely… we've talked about this before, so this makes more sense to, like, more of a cohesive, like, way to talk about this, I think, project-wide in OpenTelemetry, not just even in an OB space, like… talking about this at a, you know, like, the added value here, so I think this is great.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:19 I don't want to get too.
**Tyler** 19:20 problem before EBPF, to be honest. Right.
Yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:25 this, but now with eBPF, we can do it, and it would be cool if we can just contribute.
Yeah. Yeah, you're running Java.NET application, yeah, everything's great, but we also give you accurate timings.
**Tyler** 19:36 I do think we need to connect with the semantic convention group on these, but I think that's something… we can dive in that in the solution space, though. I think this is a great goal, though. I love this idea, yeah.
Okay.
So, jumping in here, I wanted to maybe ask, Steven, even working on some of these additional protocols, is there any other thing that you would call out here specifically that maybe we want to try to tackle in the upcoming year?
**Stephen Lang** 20:04 So, well, MQTT and MQP were the two that I was targeting, sort of very soon, short term.
I haven't thought beyond that.
**Tyler** 20:15 Okay.
Nicola, I'm guessing that… yeah, go ahead, sorry.
**Stephen Lang** 20:25 I was just gonna say, like, Nicola, you put me on to these messaging protocols initially. I don't know if there was any… More that you, you had in mind, or, you know, A bigger picture here.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:36 I mean, I've heard from customers, one or two, not too many, talking about NATs, But I think the kind of the work that, like Nimrod, and… Giuseppe, I think, started with adding those additional and I think maybe Mattia as well, protocol detectors on top of HTTP, and maybe we can expand some of those, like, we… I know we have… USSQ, SMS3, maybe there's more we think are important.
**Mario Macias** 21:06 about Google stuff.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:08 If there's anything… of the Google Cloud services that we want to.
**Stephen Lang** 21:19 I spoke a bit about, was it Redis PubSub, maybe?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:24 Yeah?
**Tyler** 21:35 Okay.
Yeah, this is great.
I think also the cloud services stuff, we could… I mean, obviously, all cloud providers would be great here, like, at least the top three. Yeah, I think it'd be great to see that kind of stuff.
Okay, cool.
Running down, again, these metrics. These sound great, I think this is always great, something that eventually everybody wants to know about.
Configuration. We've kind of already talked about this, so review of this stuff, this is still something that Mario's been looking at. I think more people need to take, time to look at as well, so this is, I think.
Pretty self-explanatory.
the collaborative fake also, again, started this to make it to conventions. One of the things I wanted to point out here is that, like, we did start work on trying to upgrade to the latest. I think Alex Bowden had a PR, which is still sitting there.
One of the other things is, I did notice, like, things like, this, where we have NQ spans and processing spans, I think, kind of like what we were just talking about, we want to make sure we're collaborating with the semantic convention group to make sure that, like.
if these sort of things are gonna become canonicalized, like, we have buy-in from the rest of the group, so I think that sounds like, a great task for this, this, this goal, so… Just kind of making sure we're capturing that.
The gRPC context… yeah, go ahead.
**Sven Cowart** 22:54 Jump in here. The two that I have down below, I think they speak to that, and trying to also directly address those, but they're specifically related to the network thing. I've been the guy that's making a lot of noise about networks in Manatee over the last couple days in the Slack channel. So, nice to meet you all.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 23:13 Nice to meet you, Swan, thanks for that.
**Sven Cowart** 23:15 Yeah. So I'm trying to give, two things here. The one is, There's just a lack of network flow attributes in the hotel space, and we need to come to standardization on that, so that different projects can all use the same ones. I don't know if this is necessarily the right audience to decide that. I might… I keep hearing, like, a larger semantic convention group in SIG, so… Maybe we need to take that to them first, and get… sign-off there, and get the spec added for flow-specific attributes, and… And then we can align on that inside of OPI.
**Mario Macias** 23:55 Yes.
**Sven Cowart** 23:56 Totally open to suggestions on how to proceed there.
Yes, stop.
**Mario Macias** 24:01 I, I, I started, working on that, We… I was looking for different people in the hotel community. They told me to start engaging with the hotel system metrics people.
In order to start defining the semantic conventions. I think there is some work we could start. We didn't realize, and thank you for bringing… for bringing it, we didn't realize that the attributes were already… the attribute names were already, standardized, or the semantic convention was already defined.
For… before renaming any… any metric, I think we should first make sure it… it belongs to a proper semantic convention from… from OTEL, and then we can… And then we can implement it. If… if you want, there are, I'm working, or… I have been delaying this topic due to other priorities, but for this quarter, our main goal was to start working on that, so if you want, we can keep working on that together. There is another Grafanista, Lyudmila, that is also a… an hotel contributor that told he… she will work on… on… on this topic. So, yeah, maybe we can… we can start.
**Sven Cowart** 25:31 Yeah, that would be great. Because we have a lot more, so I would say those flow attributes, those are not already defined. Like, the ones that we used in the Merman project, we came up with, based on our experience with NetFlow, and… We need to get those pushed forward. The other issue I created is just an alignment issue with those ones that are already defined, and making sure that OBI is aligned with what's already defined.
But outside of the flow ones, I mean, the… if you look at the issue, the flow issue, you'll see just a handful of them. What we've done in Merman, there's already… there's, like, 50 more of them related to flow-related data, so there's quite a bit to get through there, and so I… We're very motivated to move with you guys, and we're somewhat new to the hotel space, so… any guidance and hub would be appreciated along the way. And outside of Flow, we also have, Rob's on the call, who's also part of Elasta Flow. He has several tens of thousands of vendor-specific fields about MIBs or streaming telemetry that he's trying to standardize into a common schema inside of OTEL right now in the background. So there's more than just flow that we are looking to contribute here.
As far as these semantic conventions for network-specific data goes.
So I'm happy to work with you, Mario. That would be great.
**Mario Macias** 27:01 Yo.
**Sven Cowart** 27:02 I can… is the best thing to just join that, you said the systems?
System Metrics SIG.
**Mario Macias** 27:08 Yeah, let me… let me look for the exact channel, and I can share it with you. Okay. Hotel, hotel system metrics.
**Sven Cowart** 27:17 Okay. It… it would be great if we could maybe… I mean, I know the network SIG itself is completely dead, but it seems like it might make sense to… Restart that up, and… We'd be happy to lead it if that's something that the community is interested in.
**Tyler** 27:35 So, I… I would say a few things, but… Steven, I see you have your hand up. I want to make sure you get your, chance to talk here, just…
**Stephen Lang** 27:46 Oh, that was my cue. I thought you were gonna say something else.
**Tyler** 27:49 No, sorry.
**Stephen Lang** 27:50 Yeah, so this is linked to both this conversation, but also, Tyler, what you were just talking about in terms of stability. And I wanted to raise the fact that if we were to consider renaming metric names or attributes, either now or in the future, at what point should we consider telemetry schemas?
Because this was a sort of fairly new feature, which I'll drop the link in the Zoom chat.
But for consumers of OB metrics.
Who assume that our metrics are named and attribute labels are in a certain format or convention. And then we transition that to a new convention.
we might need to, at some point, use telemetry schemas to communicate that OB version X used this telemetry schema, but version Y actually uses this, and here's the migration for it. So I don't know at which point we would consider that that would be necessary.
**Mario Macias** 28:44 That's a… that's a good point. That's a good point. Yeah.
As long as we currently are not in a 1.0 function, maybe we don't need to create a schema of the current specification, but yeah, that's… that's a good point.
Yeah, yeah.
**Tyler** 29:02 Yeah, I think, Yeah, I mean, I agree with Mario, that's a really good point. I think that it may even be a better, like, I want to say we should do it right now, except you can see, like, the screen is literally full of goals that we have, so obviously prioritization's gonna be a hard one this year.
the reason I would say we'd want to do it right now is because it… we are using non-standard metrics and span names here, right? So it is helpful, because you can take the syllampture schemas and use them in Weaver to do mutations in any way that a downstream user wants to do, as well as validation and a lot of other, like, cool utilities with it.
So, I think at that, there's actually benefit in doing it before it's stable, just for those mutations.
**Mario Macias** 29:46 Okay.
**Tyler** 29:46 after… I agree with Mario, like, it is… I don't… like, it's just super critical, because, like, if we're going to be making sort of… any sort of changes at that point, like, you're gonna break people, and you need a way for them to use the tools and utilities to not have their telemetry broken at that point. So yeah, I agree with Mario then as well, but yeah.
Great, great point, yeah.
Sen, back to you about, like, the… how you'd proceed. I… I think Mario's got great suggestions. Joining that Slack channel, proposing it there.
**Sven Cowart** 30:16 Nope.
**Tyler** 30:16 To be honest, like, getting in contact with Ludmila is probably your best bet. Like, Lyudmila is kind of… one of the main figures in the semantic convention space, let alone, like, this space, if she's interested in it. The problem with semantic conventions is there's just… there's so much space, so it may be that, like, you would then start leading this.
Ludmila has a lot of the standard best practices for OpenTelemetry that she can help communicate to you as well, like, around… naming structure that we already have around, like, how we design, how we think about, metrics, how we think about, like, naming these things, like, what sort of thought process goes into, you know, scoping, as well as, like, extension. So I think that there's a lot of value that she can provide there.
I think… rebooting the network SIG is probably not gonna happen, but I do think saying that you can come here and talk about these sort of things, especially if we're gonna be, like, adopting these sort of things and trying to be working on them, I think this is a great place to have those conversations. So, yeah, I would say just keep coming back here and keep proposing topics here, and the people here, I think, are very interested in this topic.
**Sven Cowart** 31:28 Okay.
Great.
I was surprised.
**Tyler** 31:32 Symetic convention's sake.
**Sven Cowart** 31:33 I'll message her there. She actually answered me, like, a year ago, which I didn't realize that's… that's the person I need to get with anyway, so…
**Tyler** 31:40 Yeah, yeah, absolutely.
Yeah, and like Mario also said, he's also working on this, so if you wanted to keep Mario in the loop, please, yeah.
**Sven Cowart** 31:49 Quote.
**Tyler** 31:50 Please do so, yeah.
**Sven Cowart** 31:50 And by the way, I'm happy to propose, like, a very experienced Go developer here, so I'm happy to actually make the PR for this as well, so when that time comes, that's totally fine with me, and I'll help you guys along there.
**Tyler** 32:07 Yeah, absolutely. Yeah, that sounds good.
**RC Robert Cowart** 32:09 find the raise hand thing here on the Zoom thing, I'm sorry. I'm the counterpart here with Sven working on this. I think the flow stuff makes sense to keep in, like, this group, for example, is a good example, because it is what our flows at the end of the day, it's applications talking to each other. It's the same things in a trace that are just as represented from the network perspective.
although I'm… I think there's still probably a lot that could be done in a separate network around, like, you know, just metrics of network devices. I'm looking here at our normalized set across probably about a dozen vendors for BGP protocol, and it's about 120 values.
And that's where, when Sven said thousands, it is going to be thousands.
of fields across all that different stuff, so there's probably still an opportunity to do both, but I think the flow stuff makes sense here.
By the way, I'm Rob, by the way, like I said, counterpart there with Sven, so…
**Tyler** 33:09 Yeah, yeah, welcome, Rob, as well. Yeah, I think that there's a lot, I think, that can happen here.
I think… like, the scope that you're talking about, I don't know, The problem with the network sick is that I think it was just, like, one person, eventually. I think technically two people, but one person it eventually just turned into, and so that's just… It's not really a healthy sig at that point.
So, I think a lot of these topics, I think there's nothing stopping us from trying to address them, especially if you wanted to define them in semantic conventions. Like, that, I think, once you get these particular flow metrics addressed in semantic conventions, it may be, like, all of these other topics that you're talking about, like, in the BGP, like.
All the other network metric you want to talk about, like.
adding them to semantic conventions first, and then the applicability to other areas, I think that's the way to go. Especially if you wanted to all, like, start leading that group in the semantic conventions, like, it's a subgroup, essentially. Like, I'm sure Ludmilla will talk with you a little about this, like, yeah, that's something that I think they'd be very excited to have help in, so yeah.
Implementation-wise, though, then it's just finding the applications of where you would, implement it, which, again, probably might be here, but yeah. We can definitely talk about that more as the year progresses, and we get some movement on this, but yeah.
But yeah, welcome again.
Okay, so I just want to keep going, keep the… the progress. So, Nimrod has also had a gRPC context propagation, which I'm… I, feel bad it's this low on the list, I forgot, about this one, so this is really important.
I think this is…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:51 Yeah, you should do that. Yeah.
**Nimrod Avni** 34:54 Nikola gave me the idea, so that's why I added it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:59 I completely forgot about that.
**Tyler** 35:01 Yeah, I did too. Yeah, I definitely think this is a pretty high… this is… one of the major protocols that we support, so I think this makes a lot of sense.
The Rust Tokyo I.O. context propagation. I did want to ask you about this, because I, I think we kind of already support this one as well.
Just in the sense that, like, that token example I was talking about with earlier with, like, the .NET stuff, I also have a Rust server in there that's propagating context, but I do remember having to write my Rust server particularly, essentially trying to keep it all in the same thread. So, I'm guessing what you're talking about here is, like, the asynchronous nature, right?
**Nimrod Avni** 35:40 Yeah, like, I didn't test it, I just assumed that for every, like, framework that we don't have any specific support for it, it just does, like, same process or same thread propagation, and not in any async environment. So, maybe, like, implement some custom support like we do for Java, Python, Ruby, that stuff.
**Tyler** 36:02 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:03 Challenge is they strip symbols.
By default, all Rust binaries, when you compile them, by default, the compiler is set to call symbols. Otherwise, we would have done it long ago, I mean… if symbols are there, actually, it's not that hard, and I think Tyler shared a little while back on our, you know, OB Slack.
a presentation from someone that actually explained how to do it, so… It's not that much work, it's just… And… unlike Go, where everything's so standardized.
I'm not sure we can do the same trick, where we could kinda… find the symbol offsets, even though there's no symbols?
Not sure that's doable.
**Nimrod Avni** 36:53 I… Yeah, you might be right, I don't know. I… unfortunately, I didn't do a lot of digging into Specifically this, maybe after we dig in a bit more, we'll see that it's.
**Tyler** 37:05 Yeah.
**Nimrod Avni** 37:06 Too hard to get into.
**Tyler** 37:07 this is… this is what the purpose is, it's a goal session, right? So it's about just saying you want to look at this, that's good enough. So, yeah, absolutely, like, we don't need a full-fledged solution. But yeah, good… I think… I think this is worth looking at. I would definitely like to see this. I think Rust is picking up in popularity as well, so I also would love to get other people that I know working on Rust to come maybe even talk about this, because, Yeah, like, Nicholas said, that presentation I gave, or I shared in Slack, was from a Microsoft employee, and I think that, like, they're, you know, interested enough that they may be, like, we can Get them over here and try to find a solution space, so yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:46 I believe Mario also ran a hackathon, Mario.
related to Rust, and I think you…
**Mario Macias** 37:51 Yes, I was… it was not related with Tokyo. Oh, I… yes, I was doing a hackathon, and it's… impressive, the level of optimization behind an executable, how many symbols are lost, are changed. So it was very, very difficult to… to… to instrument. I don't know if Tokyo, leaves some… Some clues we can follow in the form of… I don't know, core routine ID, or… yeah, we should investigate completely Tokyo, the Tokyo framework to see.
**Tyler** 38:35 Yeah, I agree. I think it… there's a lot, unfortunately, of, like, asynchronous, like, patterns and frameworks, because you get to bring your own runtime.
But this is, I think, one of the more popular ones, so worth prioritizing.
**Mario Macias** 38:45 Yeah. Mostly because many of the lambda functions were aligned.
Then when they were in line, you lose all the track about arguments, or… Many other things.
**Tyler** 38:58 Huh.
**Mario Macias** 38:58 Yeah, maybe Tokyo being a maybe has a runtime being a bit higher level, we can… we can get something to… To… to instrument, or to know where we are.
**Tyler** 39:14 Yeah, okay. Alright, so, keeping it going, one of the other things, so the improved support for MongoDB compressed payloads, this sounds great.
integration with existing applications sending telemetry. So, I am interested in this one, because in theory, like, we have something like this for Go, right? Where if you have, you know, using the standard API, and so I'm guessing what you're saying here is that we want to try to, like.
Integrate also with other languages?
**Nimrod Avni** 39:40 Yeah, other languages, and also, I guess this is for the case of, spans, but in the case of… I think the more interesting is, like, custom metrics, like, having the ability to get custom metrics, and also have Obi, extract metrics from the application.
Because I guess now we have some, like, the… if we detect that the application sends metrics, then we don't send metrics.
But it might be useful to get, like, I don't know, service graph metrics, and my custom, I don't know, my custom reported metrics. And the one for spend, of course, that if you want to have, like, spend on a custom operation, and also have OB Auto Instrumentation.
Yeah.
**Tyler** 40:27 So, you mean, like, if there's no SDK, have those metrics go through Obi, or are you saying, like, there's an SDK already reporting metrics, but you want to, like, add additional metrics?
**Nimrod Avni** 40:37 So, like, either… I think now how the Go thing works is, like, you have the SDK, but you don't actually send telemetry, right? Like, Obi picks up the Go SDK and, like, creates the span, and we send it as Obi.
**Tyler** 40:52 Yeah, so we need to…
**Nimrod Avni** 40:52 I think either, like, either…
**Tyler** 40:55 Typically, though, just to, like, clarify, like, in the parlance of OpenTelemetry, it's just the APIs being used. There isn't any SDK registered, is the difference.
**Nimrod Avni** 41:05 I… I guess so? Like, I guess that might be the end goal. Like, there's a question, do we want the customer to be able to send, like, the application itself to send metrics and traces, and we somehow detect Like, we need to differentiate between, like, complete auto-instrumentation of the app and, like, manual instrumentation of specific things.
Or even, I don't know, ideally.
OB… I think it also relates to something that Nikola said about, like, we can add, in-queue spend, but let the SDK run the processing spend, like, basically complete Like, for example, if we have, like, a client span.
of, like, HTTP, we can have it from the SDK, but, like, stuff that, like, DNS and TCP errors that only OB can do, then we can, like, report it ourselves. So, like, somehow combining all of them… I'm not sure I know exactly how that's, like, kind of a… a goal.
**Tyler** 42:10 So instead of saying, like, it's an all-or-nothing, you're saying more like, I can investigate what the… what is… the SDK is being sent, and I see that it's handling, you know, HTTP server and client, like.
requests, so don't send spans for that, don't do metrics for that, or if it's doing those. But it's not doing any DNS lookups, right? So I can handle those, is what you're saying, right?
**Nimrod Avni** 42:31 Yeah, I think ideally you want, like, you would like what you can get from your, like, instrumentation, like, you know, from the code instrumentation, and the rest we can let, like, OB do. Depends if you're doing any, like, odd instrumentation, or manual instrumentation, or even no instrumentation.
That's, like, the goal. I'm not sure how to completely do it, but…
**Tyler** 42:55 Yeah, I think you would need some sort of way to, like, signal from the SDK what telemetry it is producing, because otherwise you'd have to, like, parse the stream as.
**Nimrod Avni** 43:04 Yeah.
**Tyler** 43:05 out, or something, right? Like… But that, I think, is maybe worth… I mean, like, we're already looking at ways to, like, talk about, like, a resource and an environment variable.
**Nimrod Avni** 43:16 Yeah, so maybe it'd be related, like, some shared context between, like, the SDK and the… I don't know.
**Tyler** 43:23 Exactly, yeah. Yeah, I think that that's a great idea.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:27 Yeah, sorry, did you have something else? Sorry. Yeah, yeah, yeah, I think, I think now what you're getting to, because right now, if you see an application exporting metrics, we just stay away from it, right? We say, don't export metrics, like, they're doing it themselves, right? But you're saying that could be exporting some random internal metrics unrelated to HTTP metrics, or… or GOPC. So we want to get the GOPC with Obi, but we can't, because we see it in exporting metrics, and we're thinking, okay.
it's doing its own thing, so… Don't touch… yeah, don't touch it. Yeah, that would be really cool if we can pull it off.
And I like your idea about the DNS thing, yeah.
Yeah, that's exactly it, why we should do it.
Because some of these, like TCP resets, DNS, and all those things could be really interesting for debugging purposes.
Are not able to be generated from… Yeah, digging in the metrics payloads, I think that's… That's… okay to do if it's HTTP, especially now that you're capturing… that you added… you guys added the support for capturing large requests, so we could potentially kind of scan.
The payload and figure out what… Metrics are exported, and… So on gRPC… I don't know what that looks like.
**Tyler** 44:46 Yeah, and then any TLS, you're kinda…
**Nimrod Avni** 44:49 Yeah.
**Tyler** 44:50 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:52 Yeah.
**Tyler** 44:54 But…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:54 True, yeah.
**Tyler** 44:59 But, I mean, I think it, like, that, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:04 I mean, if it's scraping metrics, maybe that's easier.
**Tyler** 45:09 Oh, yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:11 If the application is set up to use Prometheus, great, then… Maybe that's… We can scrape it.
See what they… they do. No.
**Tyler** 45:24 Yeah, okay. Definitely a good solution space.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:28 Yeah, some idea that people have… I think my… my… One of our colleagues, Fabian, he's quoted the idea that maybe you should look into for a lot of these things to make It will be the proxy for the telemetry, and then we'll actually get it and replay it.
I think that just adds overhead, I don't know.
**Tyler** 45:47 Hmm.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:49 Kinda, like.
**Tyler** 45:52 Essentially acting like a collector agent, almost? Yeah. Yeah, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 45:58 Actually, if we're part of the collector now, would this be possible to do at a collector level?
**Tyler** 46:03 Yeah, that was what I was just thinking, too.
I don't know, because I don't know if the collector ever exposes, like, some sort of… Like, manifest of what it is collecting, or what has been collected, or something like that, but… It may be a better point to try to sync all of these things, at least.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:23 I mean, Collector's written in Go.
So we can self-instrument, go, and do whatever we want.
**Tyler** 46:30 Sure.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:31 So we can self-instrument.
And we can capture this information.
**Tyler** 46:35 Yeah. Yeah, that sounds easy, yeah. You should have that done in a week, right? Yeah.
Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:44 I think we're gonna kind of try really hard to not self-instrument, but for this purpose, I can think, maybe there's… Why not?
Yes.
**Tyler** 47:00 Yeah. Okay.
We'll… we'll keep… digging at this one, I think this is an interesting idea, yeah. Thanks for bringing it up, Imrad. So another one, reduce overhead by using tracing programs instead of K probes. I think this is just an optimization in eBPF, like, programs, right?
Yeah.
This is intra- so, can you expand on this? Experiment with program, batch attach APIs?
**Nimrod Avni** 47:24 I think, maybe Mattia can expand a bit more on that.
**Mattia Meleleo** 47:27 Yeah, this was another optimization, but I don't think it's, like, the first one, I think it has way more impact than this one.
Because I don't think we have any issue right now with attachment times and stuff like that, so this should probably be very low priority.
**Tyler** 47:48 Okay.
**Mattia Meleleo** 47:55 While for the other one, I don't know how many K probes and U probes we use on average.
But if we switch, all the K-propes to tracing programs, I think we… we can notice some improvements there.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 48:12 Yeah, actually, there is an issue open, I'm not sure you guys have seen it, somebody had tried instrumenting Redis.
Redis is famously known for really low response latency times, so… The, so we need to look into that. I don't know which probe is, but some probe is hitting it hard.
I don't know if it's the probe itself, the code, or the fact that we do have too many.
It might be sometime.
Bit of a trace.
I don't know what's the difference between K probe and a trace probe now, I think it's changed over time with kernels, so… But any, any performance improvement we'll get. I think 40 inches is right, but I mean, there might be change in minimum supported kind of version.
**Mattia Meleleo** 48:59 For the… for the K-propes versus tracing ones. I think for AMD64, it's the same. I mean, it's supported on all… on all the kernels that we have.
For ARM64, the BPF trampolines got introduced in kernel 6.3, or 6.2.
So we will need to fall back to KPROMS.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:24 Yeah. So, we can do that.
Install one or the other, depending on the kernel.
Probe it, see if it supports it.
**Mattia Meleleo** 49:33 Yep.
**Tyler** 49:36 Okay.
Alright, so yeah, I think we can include these as goals. Our last one is the HTTP full payload extraction.
I think this is one we need to definitely have… I think we've talked about this before, but we need definitely some configuration, and we definitely need to sync with the semantic conventions on this one, because they have, I think, some thought on this, but… yeah.
**Nimrod Avni** 49:58 I couldn't find any… any… there's, like, semantic conventions on, like, header fields. I don't think there's any semantic conventions for, like, including the full payload. I see… I saw some, like, instrumentation that you can do it, or you can do it, like, independently with, like, hooks.
And I don't know if it's, like, a great idea.
for, like, all spans, or, like, you want to have also that… this kind of sampled, or something, because it's gonna add, like, a… gonna make your… the payload of the spans much bigger. And of course, you need to configure, like, all the large buffer stuff for HTTP for this to actually work.
But it can be, like, a really cool feature, so you can see, you know, headers and the full payload, great for debugging.
Like that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:45 Like, people sometimes want to have their own custom fields, like customer ID, whatever. They're serving some SaaS application, and they're They want to include the customer ID in there.
Traces, right? Yeah, this, this could be… Game-changing, that.
**Tyler** 50:59 Yeah, I think a lot of the semantic convention talk around this, especially in the specification meeting, is, like, yeah, they don't include it because they don't want to promote it by default, because it becomes a footgun for a lot of the reasons you just talked about, as well as the security implications. Like, yeah, the obfuscation is… is hard. I mean, there's entire businesses surrounded around, trying to, like, obfuscate this kind of stuff, and they don't always get it right, even. So… It's really easy for customers to try to, like, Hmm.
Just, you know, have… if it's not by default, to have it be a mistake, but Once they switch it on to also have it.
cause security incidents, and I think that, like, people in the past conversations have talked about these sort of things. But like you guys are saying, like, it's an interesting thing, so I think that, like.
we would want to make sure we were a part of the conversations that, like, have existed around this in OpenTelemetry, and, as Nimrad Alzal pointed out, like, it does exist in other instrumentation, so, like, I think that there are ways to try to accomplish this, it's just… Caution, I guess, is the only thing I would say here, but we don't really have to dive too much into it here, either. So, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 52:07 Yeah, but what if we just have it off by default, and then you have to specifically say which fields you want?
**Tyler** 52:14 Yeah, I think… I think off by default's, like, kind of…
**Nimrod Avni** 52:16 Yeah.
**Tyler** 52:17 Yeah, required. How that turns on, how the sampling is associated with that, but then also, like, this obfuscation, like, do we provide obfuscation, or do we provide a hook for people to provide their own obfuscation, is another thing.
**Nimrod Avni** 52:31 We can open… I think we opened the initial a while back, we can, like, kind of revive it. It's like, we thought about a couple, like, obfuscation rules based on, like, header names and types and JSONs and blah blah blah, but yeah, we can talk about it offline.
**Tyler** 52:45 Yeah.
So, yeah, speaking of that, we're coming up at the end of the hour here, and I think this is great. I think there's a lot of really great topics here. There's definitely more than I think we can get done in a full year, But I'd love for you all to prove me wrong, and so, yeah. Let's do it. Yeah, let's do everything.
One of the things I wanted to do next, though, is I wanted to make sure that we have all of this stuff, I don't want it to get lost, is so… I'd love to get it all tracked in issues, and so I would ask, if you've put something on here, and if you know about an issue, so something like, Sven's already done.
just link to that issue, would be great. And, so, like, Nimrod, like, what you were just doing, the HTTP full payload extraction stuff, you could just link to any issue you know.
would be great. And what, isn't an issue, if you also wanted to, add, an issue, that'd be great. Otherwise, I'm planning on going through this over the next week and finding, you know, making sure each one of these topics has an issue. Maybe even multiple issues for things like this, for protocol coverage, where it makes more sense to have multiple.
And then what we're gonna do, I think, hopefully, next week is look through all of these and say, like, you know.
based on our priorities, like, what are our priorities gonna be? I would love to say, like, stabilization's a priority, but this is a community-driven thing, so, like, you know, what are people planning on working on? And then we'll try to essentially add it to a list. With that list, I think we'll try to then publicize what we've come up with as our, like, you know.
Usually, it's around… 5 goals, but this is a little bit bigger of a developer community, so maybe it's more like 10 goals out of all of these things, and, you know, try to communicate these to the broader, OpenSelemetry community, as well as the user community, so… In a blog post, or, an issue tracking these kinds of things would be cool, so… But yeah, first step is we need to, like, make sure we have it all documented into, like.
These are the things we want to do and what they mean, so we can… we can actually track it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:40 Can we get a project board, and then… Yep. Use it to prioritize and stuff like that?
**Tyler** 54:44 That's exactly, I think, a great way to do it. Yeah, we can take all those issues, put them into project boards, and, yeah, so we can keep it up. That was one of the things that, like, we've definitely gotten responses on at OpenSelemetry, is, like, user space for tracking goals, and so I think this is a great way to do this. I've had a lot of success doing this in past SIGs as well, so, It is annoying doing it sometimes, but man, the community really appreciates it, so, yeah.
Cool, alright, so then… We've got 5 minutes left. Any other questions about these? Any other topics around these goals? Is it okay for those… I guess it's just, Sven's already got his issues, but Nimrod and Nikola, you're okay with opening issues or looking at these as issues?
Yeah. Got a thumbs up.
Okay. And also, if you have other… things that you think of over the next week, create an issue for it, and, maybe add it here, and I will… I will include it in the project board that we go above for next week, in next week's meeting.
I don't think we have enough time to go through all of the open poll requests, definitely not, but maybe I'll just ask if there's somebody on the call who has an open poll request that you wanted some attention on? I see, Maxton, I hope I didn't mess up your name, too. Do you have your hand raised?
**Maksym Iv** 56:04 Oh, yeah, yeah, hey, I just raised that. I want a quick question. What about home deployment? I was… started messing with OBI recently, and a lot of folks asked how to deploy it, so I was wondering if there is any Okay, it's not uncomfortable, thank you.
I mean, it's not in the base repo.
**Tyler** 56:24 It's not, yeah, there's this chart here specifically for the OpenTelemetry EVPF instrumentation. So this is where you want to be.
I don't know of a better way to communicate this. Maybe there's a thing that, you know, if you're asking this question, you're probably not alone, so maybe, we should have this documented in our open…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 56:45 the README or the docs. Maybe now they can include it since it's ready.
**Tyler** 56:49 Yeah, that's… maybe that's why we don't have it, actually. I didn't think about that. But yeah, you're… yeah, that's a great idea.
Adding to the docs here would be… I think here, and maybe OpenTelemetry.io, so yeah, that sounds great.
**Maksym Iv** 57:03 Because on…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:04 We don't mind opening an issue for this, so we don'.
**Maksym Iv** 57:05 Yeah, yeah, I will do, I will do. I just asked before, because I was looking here, and I just sent a link in the chat.
And there were no helm mentioned, so I will create a mission, no worries.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:20 Yes.
We have docs on the… on the original project for this, and it's… and it goes into details on how to use configuration options and all this. I think we should… we should pour those.
**Tyler** 57:33 Yeah, absolutely.
Absolutely. I think that's… that's great. The more we can get use on there, I think that's… that'd be helpful, too, so… Okay, last 3 minutes, any other quick topics from folks?
That was a lot, so I think I'm really excited for some of these goals, so, yeah, I think that there's a lot of really great things here.
If not, then we can end the meeting here. Thanks, everyone, for joining. All the, contributions and thought in this progress, project. We're looking forward to 2026, so I'm pretty excited. So yeah.
I will, I will see you all in a week's time, and, thanks again. Bye.
**Nimrod Avni** 58:19 Bye-bye.
