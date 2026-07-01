SIG: Arrow SIG
Date: 2026-06-30
Duration: 65 minutes
============================================================

## Zoom Recording Transcript

drewrelmas 00:02:48 Hello, everyone. Happy Tuesday.
Is anyone else able to speak up? I haven't heard anything.
Utkarsh 00:03:11 Yep.
drewrelmas 00:03:11 Yep. Oh, there we go. Cool.
jmacdonald 00:03:21 Thought my Zoom was gonna crash.
It's trying to crash. Can you guys hear me?
Yeah, Zoom threatened to crash, we'll put it that way.
Hello.
Hello, team. Hello, friends.
So we missed last week.
I did discover in the end why, but we just hope it won't happen again.
AI note-takers and calendar mistakes combined.
Alright.
I know Laurent's out for another week, so, I guess we're looking forward to his return.
But, we will carry on.
And I'll put up the notes.
I just went through the, issue list myself. There's about 10 or so that are new since 2 weeks ago. Many of them have already been triaged, but I still kind of looked at them. The… we could work in forward order, That might be best. It's Albert Either way, by the way. First and last.
drewrelmas 00:04:37 Well, do we want to… I know in the past we've tried to avoid talking about the accepted ones in…
jmacdonald 00:04:44 Yeah, that is true. I, merely was suggesting that some of the larger ones, although we accept them, are still interesting to discuss. We could put them in the, like, discussion area.
So… Yeah, so back to that list, there are some that need to be discussion… need some discussion, and I'm glad Ukarsh is here. We've got this Geneva Exporter one. So… Who's been doing all the triage? Are people… triaging themselves, very good. Tom has been doing good triage work, so, Looks like Albert has made some progress on… design for the op-amp feature extension work. And I find that uncontroversial. Is there anything we can discuss, Albert?
Albert Lockett 00:05:37 Yeah, hopefully it's not too controversial. All that I'll say is that I started working on this as kind of, a proof of concept, and then it was kind of fortuitous timing that CJO started a thread about it in the Slack channel.
So, the way that I'm planning on doing this is, Laurent added, these things called controller extensions last week.
Which are similar to, how we would implement, like, processors or exporters or whatever. You'd basically just implement a trait, and then you use linkme and give it a URN, and it will… it has this life cycle of, like, accept config, instantiate itself, and then what gets passed into the trait is, like, an instance of a trait called control plane, and then you can use that to get configuration snapshot, and also it has methods on it that you can use to start pipelines and stop pipelines, or receive a full config and then reconcile it.
So, Yeah, so my plan was to go ahead and implement the capability for the Dataflow engine to receive its config, like, from an OpAmp server, either as a WebSocket or HTTP. And I actually started a, design document for this, and I just put up the PR with the design document in it.
But, like, right before this call, so we don't have to spend, like, the whole, like, the time on this call going through it. We can if there's interest, but this would also be something that I'd like to get feedback on async. That's why I created a design document, because I think that, like, you know, it's usually easier to, like.
To review designs, and you can create threads and stuff using… the PR workflow. So, yeah, it's that PR right there. So this design doc is up.
if time permitting on the call, people are interested, I can speak to it. Otherwise, you know, anyone who's interested in this, please review, async and give feedback.
jmacdonald 00:07:45 Well, I'll definitely pass this around. I'm sure some more people are interested on the call, besides the ones that I know who are on the call. Ukarsh, I know, has expressed an interest in this one, and generally, OpenTelemetry, op-amp is a big deal these days.
So cool, I want to read it.
Anything that, like, sticks out as, like, a gotcha or worth discussing off the top of your head?
Albert Lockett 00:08:10 I… so I think, like, what I was basically trying to align on here was how, like.
how we receive the config, and, how we produce the status. I mean, that's kind of, like, the two things that, like, an op-amp server basically does. So my, my… envisioning of this was that there's a field on the server-to-agent message called, remote config, and it has in it a config… it's… it's a… if you go down, down more, Josh, there's a field called, Keep going. Keep, rate go up a little bit.
right there. So there's a field called… so this is, like, the server-to-agent message, there's a field called config map, and then it has a hash map of these agent config files, where the body is… is a content type, and just an opaque, like, like, vec of bytes.
So my thinking here was that this is, like, this is how we should serialize the, like, the engine configuration, and the server should send down, basically, like, the entire config. It should be JSON serialized, in this body, so it's kind of like making the assumption that the server sends the config, like, declaratively, to say, like, here is what the whole engine config should look like.
go, like, go away and reconcile this, basically.
So that's, like, that's the first kind of, like, thing I was trying to get alignment on.
The, the second thing I wanted to get alignment on was, and… and again, like, you know, we can discuss the design either here or in, in async on the document, was how, the ser… how the agent reports its health back to the, back to the server. So, in OpAMP, there are a few, like, health and status, fields, but, like, none of them align, like, really well with, like, our level of… like, the level of granularity that we have for health. So, for example, like, when we think about, like, our health, we have, like.
like, groups, and then pipelines, and instances of pipelines, and each one of those has their own phase, and whether it failed to start, whether it stopped, and blah blah blah, right?
But, like, the agent, the server message kind of expects that all to be, or… it doesn't have, like, the same level of granularity, basically, so what I was trying to, like, like, write out here in the second half of this document was, like, like, here's how we can, like, like, use the existing fields in the, in the server-to-agent message to have, like, to have a rolled-up version of the health, but also, like.
there is a… there is a… there, if you go down a little bit, Josh, so status resolution, health resolution.
here is… here is what I was trying to say, and here's the rules for how we set these statuses based on, like, the phases of each pipeline. I'm… I'm completely open to… to feedback on this as folks are reading through it, if this, like, if what I've described here seems hokey.
And then the agent-to-server messages also has the capability to have, like, a custom message, which can have a body of anything you want. So, like, that can also be the mechanism where we send back to the server, hey, if you're not interested in this, this, this aggregated health, if you actually want the full, like, pipeline, right here. We can… so we can send the full thing, using this, using this custom message. So this was also what I was trying to call out here, so…
jmacdonald 00:11:49 That's it.
Albert Lockett 00:11:50 Yeah, so that, like… basically, like, my… my idea here was, like, implement the op-amp agent, like.
like, faithful to the spec, but the op-amp spec gives you, like, some leeway in terms of, like, what you fill in in the remote server config and the health status and things like that. So, this was trying to, like, fill in those gaps in a way that, like, that fits with the system that we have, basically.
If that makes sense.
jmacdonald 00:12:25 It does. I was gonna, comment that the… there's probably a precedent that's been at least explored in the OpenTelemetry Collector repo. As you were speaking, I remembered, like, echoes of the past. There's this, health check extension that was, like, V1, and then… over the years, like, enough complaints arose that it became clear that, like, there needed to be a component… a per-component or per-node notion of health, and the HealthCheck V2 extension was launched And I wouldn't say I know every single detail about this topic, but But on that topic, I could put in… At least a link to… The… health check extension, which has a connection to the op-amp component in that collector, so, like, it's worth looking at.
Albert Lockett 00:13:20 Okay, yeah, sure, I'll… I'll go through that, and so I guess, like.
yeah, I… I didn't know about that, so I will go through it, because I think there's probably some interest in, you know, design inspiration that we can draw from that, and so, Yeah, I'll.
jmacdonald 00:13:35 I… yeah, I don't actually know the deep, deep details, so maybe there's nothing here, but you should check it out.
Albert Lockett 00:13:41 Okay, sounds good.
jmacdonald 00:13:42 Looks… looks vaguely familiar here. Cool.
Albert Lockett 00:13:47 Question.
Yeah, sure. I see Ukarsh has his hand up, so we'll go to that first, and then we can go to the…
Utkarsh 00:13:56 Yeah, I had a small question around this. So, like, now we would have multiple ways to configure the engine, right? Like, this op-amp would be one, then the HTTP API, and this, then SDK, and I think also Laurent, long ago, had shared some CTL command line thing.
So, do they all go through the same, abstraction or component that finally, configures the engine? Like, is it all going through the controller extension hook?
Albert Lockett 00:14:28 So as far as I know, we haven't, like, refactored away the, the HTTP admin API to become a controller extension.
I, like, I don't… I don't know if that was planned, but it, like, at least at this point, it, like, that's… that's not what we did. And sorry, what was the… what was the third way that you mentioned?
Utkarsh 00:14:51 I remember…
jmacdonald 00:14:53 TLI uses the… the… the HTTP API, is what I heard.
Utkarsh 00:14:59 Okay, that DFCTL, CLI, remember that? Like, that presentation?
Just like kubectl, we had this DFCTL thing, which Laurent showed, and So yeah, I was just wondering, like, now we would have multiple ways to, Maybe configure and potentially apply library configurations later. So… Do they all then go through some same standardized component which applies there on the engine, or do they all have, like, different ways of doing it? I haven't looked into the internals of the implementation.
Albert Lockett 00:15:34 So as far as I know, there is a, An instance of a, of a… of a trait called Control Plane that is able to, like, you know, do all the control operations that we, that we do, right? Like, you know, start pipelines, stop pipelines, things like that. So as far as I know, like, the, the HTTP admin API and any controller extension basically have, like, a, like a… A shared, reference to that, that they… they… Use the same underlying, Object, basically, to, to control the, to control the, the engine configuration.
Utkarsh 00:16:23 Okay, yeah, go ahead.
jmacdonald 00:16:26 That makes sense.
Continuing our triage, I think many of these are sort of, like, relatively minor. I know that the… this one here, back in time, 3310, was, has been… is a needs info.
Oh, no, I hit the wrong button. Let's go back.
Come.
on… people?
See, I'm just having a very slow time right now.
This is… Seems uncontroversial.
Request to use. Request header, key values.
As an input to the query engine.
Albert Lockett 00:17:18 This is, yeah, this is something that I, that I added and then didn't spend a lot of time looking at, but basically, like, I think it would be nice if there was a way to use, like, the OPL and transform processor to modify, like, metadata, that exists on, on OTEP batches, like, headers, being, being an example of that. So, this was, like.
sort of a placeholder for basically adding that capability, which I think is something we want. As Josh said, I think it's something uncontroversial. The needs info here, I added because, off the top of my head, I didn't know what other metadata we had, in, in the… like, on the OTAP batches, so, like, I just wanted to make sure that, like, we didn't, like, like, you know, like, plow ahead with the syntax without thinking about it, like, a little bit more carefully, and so I just added the needs info, Labeled, it kind of blocked it, so just no one picked it up without us thinking more deeply about the syntax.
jmacdonald 00:18:19 Gotcha. I see Kennedy has a hand up.
kennedybushnell 00:18:23 Yeah, so kind of more general than just headers. It feels like there's a bunch of information that may be useful in the OTAP payload period, like, even beyond like, as it flows in the pipeline, you might want to touch these things. Is that all fully accessible today, or should we have, like, a round of looking at What kind of information disappears as soon as we, like, turn it into a payload and maybe inject it into the data in a more grabbable way.
jmacdonald 00:18:58 I have a… response to that topic, which would refer us to one of my open PRs that I just opened in the Arrow repository here. I've had it open on an internal PR for a bit. This is roughly the same document, and it will let me partly answer that one a little bit, Kennedy. At least I want us to talk about that document in response to your, your, your, statement there. So I will say, I just opened this document, talking about multi-tenant design, because I think a lot of the reasons why we talk about this other context question is what else do we know about the request that can help us route it, filter it, or dissect it in any other way? And so this document here, I'm sharing for everybody now.
Is covering at least a proposal for, mechanism, for extracting information from context and making it become Part of a sort of formal tenant descriptor, And the reason I'm using this sort of to answer Albert's, topic, sort of by way of Kennedy's question, is to say that, when I saw this snippet of code in Albert's, like, issue, it's like, you're gonna see the headers, and you're gonna get a key named X or Y or Z, and you're gonna go looking up in that dynamic map.
And if you are actually trying to extract the value, that sounds good, but you also might want to hash by a value and route, or you might want to extract the source IP and use that for routing or filtering or some other query facility. And this mechanism is a mechanism that we… that I'm proposing. I just opened it, so no one's read it yet, at least. But I'm proposing as a way that we can Formally, kind of, declare the not just that there is a map of headers, but there is a set of headers that we've already pre-computed all the things we might want from. So in the case of the query where you're extracting headers, you might… you might have a tenant descriptor that extracts the queryable header that you want.
much further upstream, so that you don't have to recompute it when you're in that processor. So some of the answers might come out of my document.
And I wanted to just refer to that.
And I saw a thumbs up from Kennedy, so, I think we're able to move on, or at least back to, Where we were.
If there's anything more on headers.
Or the topic that Kennedy and I spoke about, please let me know.
kennedybushnell 00:21:35 Yeah, I think that the desire to have access to headers definitely makes sense. Whether or not explicitly having headers be, like, a special thing or not is something we should think about, and whether or not there are other such special things, and maybe Josh's document speaks to some of that.
But, yeah, definitely plus.
jmacdonald 00:21:55 Yeah, for other special things, what I at least found was, that on the sort of connection level, you have, like, source IP address and, you know, MTLS certificate name, or it's, like, stuff on the level of the connection that you can, like, propagate into the request that's not header state.
And then, in the course of thinking this through, I saw something that, might actually connect to, another one of our… Oh, jeez.
open PRs, I'm gonna say.
From… from Akarsh about… Geneva Exporter routing by schema. So, the other features that I'm aware of are you might want to extract a resource key value and split the requests Into… so… so that the… some sort of data field becomes elevated into the… I'm going to say request context, not necessarily header state, but I'm saying I have asserted that this payload has one request resource… one resource associated with it, therefore you may use my attribute as a request-level metadata. And likewise, I'm aware that we need to split data by metric name, or by log event name, or something else. Often.
To, like, shuffle it into a place where there's one metric name per request, so that you can lift that metric name into the metadata, or use it for some other query that's, like, whole request.
Kennedy.
kennedybushnell 00:23:25 Yeah, so one… one, like, kind of important point that I think will help drive the point that I'm trying to make home is that, headers is HTTP, or GRBC, and we are intentionally building a system that speaks many protocols. So, special casing headers kind of is almost problematic in in kind of that context. So, if we had a standardized way to inject, like, metadata that comes from your request, and it happens to be headers in HTTP, or… plus, like, other connection bits of info, like source IP, that's great, but on, you know, some, like, RS485, it's some other thing.
jmacdonald 00:24:10 Yeah, actually, my document has gone through a round of review, and that question, roughly speaking, came up from Lalit, who asked.
Well, I'm thinking about an ETW receiver where there's no concept of HTTP headers, and my answer was sort of, like, I agree, but I was sort of thinking of headers as a generic concept. Like, I didn't mean HTTP headers, I meant just sort of, like, maybe arbitrary key value. Like, in gRPC, it's just called metadata.
So yeah, and if you're in Kafka, you'll have Kafka headers that are not the same as HTTP, and And maybe it's from the connection if you're an RS485.
kennedybushnell 00:24:49 Yeah, totally fine, as long as we… we make it very clear that, like, this is not something that you should assume is an HTTP header, this is what we're calling, like, our metadata thing, and… let it be more open, and not feel like you're shoving data in there, like, kind of sideband, because you don't happen to be HTTP right now.
As long as we do that, I think that we… We win.
jmacdonald 00:25:15 Yeah, that sounds good, at least the concept makes a lot of sense. And I tried to answer that question, I'm not sure I did the greatest job, but yes, thank you.
Utkarsh 00:25:23 And I mean, also, like, if… even if we name it headers, right, like, then… It could be, like, the person who is introducing that processor would know that there is a HTTP or a gRPC-based receiver In front.
And only then would I… like, I'm just saying, like, even if we call them headers, even if we call HTTP headers and gRPC metadata headers, give them that semantic meaning, that keyword.
Then, the, the operator who's setting up the YAML file should know that, like, if I'm using an ETW receiver, I wouldn't want to write a processor that is using headers, because just doesn't exist. Like, we could basically have our own semantic conventions for, like, what, each receiver's metadata, should be named.
jmacdonald 00:26:10 Yeah, and I actually said, roughly speaking, exactly what you just did, that we could have a semantic convention for ETW that says, I know that this app.id field is meaningful, and I want to think of it as a header for the purposes of tenant logic, but it means that when you're in the ETW receiver, you know who you are, so you're not going to go looking for HTTP headers. You've got some other definition.
Now, I would definitely want to scrutinize that little section I wrote about something about that.
This is turning out to be a great meeting. Glad we're here.
Continuing on triage, I think there's maybe one more that I saw that looked like we should talk about it.
So, I was referring to event name mapping just now, So I'm gonna bring that one back. The… when I look at tenancy, I was trying to satisfy, like, a broad list of design requirements were written down before I joined, essentially. And they said multi-tenancy. And I know that multi-tenancy can mean so many things. It can mean something about static assignment of tenants in isolation, or it might mean, like, I have 3 million clients, they're all considered tenants, and I need to do something to balance my load.
So that every user ends up on one core, even though I have so many users, I want to use all my cores. And then, a very common pattern is to say, okay, I'm going to split by something. It might be a tenant ID, and route to diff… to sort of, like, a load balanced destination, like, topic that does a per… like, a per-tenant load balance. But then, you'll… you'll find applications like you might in a Prometheus context, or, like, metrics aggregation.
Or trace tail sampling, where you want to gather all the values by a particular feature of the data at one location in a pipeline. So when I saw this issue, Akarsh, I thought, hmm, I wonder if we want to, like, target, in the future, maybe a more general-purpose way to route and assemble and batch data by… Event name, for example.
Utkarsh 00:28:17 Yeah, so, this issue, this issue in particular is, not… It's confined to a single tenant.
So this one is more like the same tenant has, multiple tables that They would want to send data to, depending on some custom logic.
Either they can, route them by event name or, like, some other attribute of their choice.
But it's still scoped to one tenant.
in Virginia exporter, like, I think so far, the multi-tenancy approach would just be to have dedicated Genuo exporter instances pertinent, and they can have their… each of them can have their own routing logic.
But yeah, like, we… it definitely seems like a common requirement, and I think, Laurent already mentioned the issue that Albert created for this in… in the… in one of the comments.
So, yeah, the very first comment from Laurent, I think.
Maybe, yeah, you scroll up, yeah, the 3273 issue.
So, Albert already had created a… An issue for such a processor, something that partitions data.
And… this is useful for us, and I think, yeah, for… Other exporters as well.
Albert Lockett 00:29:33 Yeah, I can speak to this a little bit. My intention was that, I would create, like, a primitive that could take, like a… like an OPL expression.
That we would evaluate, and then we would partition the OTAP batch based on the… the values of that expression, and then we would, for each… for each batch, we would add to the, to the… to the… what we are maybe calling headers, but the batch metadata, effectively.
jmacdonald 00:30:07 Context.
Albert Lockett 00:30:08 context, yeah, this, this value, and then emit multiple batches, and then so downstream, if, like, if you did have some… some logic that was, like, based on the context value, then that's… that's how it would be computed. And so my intention was that, like.
like, this is something that, like, the transform processor could do, perhaps, based on, like, some OPL program, but I wanted to write it, like, the actual partitioning logic, as a… as a… like a primitive, like a free-floating function that we could embed directly into, a processor, or that, like, perhaps other processors could use if they… if they wanted to.
Internally, right? Just, just like our, we have a, like a, like a batching splitting function.
jmacdonald 00:30:56 I'm thinking a topic exporter-receiver pair as well, but go ahead, Kennedy, or Drew.
kennedybushnell 00:31:02 I think Drew was first. Go ahead.
drewrelmas 00:31:05 Oh, okay. I was just gonna say this, triggered in my mind, some… an offline discussion that I'm having.
About… you know, I've been raising a bunch of PRs and issues about our own internal telemetry. I wonder if we can use this context, dictionary, if that's what we call it.
To also drive independent metric reporting, based on slices of payload.
What I mean by that is, you know, if I have a processor working… it would help use a shared processor in multiple tenants. You wouldn't need to, like.
have a batch processor for one tenant, a batch processor for another tenant. We can do the same work with a single processor and emit Our own telemetry based on… well, that might get complicated, because you might be keeping multiple sets of counters based on the context metadata, so maybe I just disproved myself, but…
jmacdonald 00:32:10 I don't think so. I feel like you're actually confirming what I was trying to type together with the idea that… well, Albert said it, that there's, like, a reusable function here, but what I was trying to say is that there's a reusable function which might split and load balance by feature in the data, but I see the continuum between splitting by the data and splitting by tenant descriptors. And it's very natural, I was saying Prometheus earlier, but if you're going to aggregate metrics, you probably want to get all your tenants and all your metric names in the same place, and that's sort of like a two-dimensional routing, essentially, that's part tenant and part data.
This is great. We have more questions and hands up.
And Kennedy.
kennedybushnell 00:32:54 Yeah, so, before I switch to mine, plus one on, like, that concept, I think that it depends on how we land on what our resource governance and, like, kind of partitioning is of Tenancy.
Because, like, that dictates how you allow for in-memory aggregation and all of these things to happen. If we require that you route between cores, for example, to split tenancy, that's very different than, kind of.
having an implication of your design must be able to kind of part… sub-aggregate, because you know that you're going to be handling multiple tenants in your same memory space. So depending on where we land there, kind of.
leads.
jmacdonald 00:33:42 Yeah.
kennedybushnell 00:33:43 some of this, I think.
jmacdonald 00:33:44 I was… I have a section on routing and batching by tenant descriptor, so I would say you don't have to route to another pipeline thread to get batching by tenant ID. We should have a batching configuration that knows about the tenant descriptor, and just it, like, multiplies its configuration so that you can have one batch per tenant, or something like that. That's what I'm aiming for. I'm not sure if I've been able to succeed at that.
kennedybushnell 00:34:07 Yeah, the fun there is when you pull resource governance in, and you're trying to, like, account for memory and CPU usage.
By tenant, or… or whatever your… tenant descriptor is, I suppose. That gets really fun, maybe.
jmacdonald 00:34:23 Yeah, and to be clear, I've aimed… my scope is that large. It's a big document, so I do talk about resource limiters, and to try to tie it all together. I'll say also that I see we don't have Lauett here, but he's open to PR that actually ties to some of what you said about how we track, you know, memory in the batch processor would have to be tracked independently, and that would be given a tenant descriptor, like, attribute there as well. So at least that's what we're aiming for here, Kennedy. Thank you.
kennedybushnell 00:34:53 Yeah, Gokhan, was your topic related to what Drew was chatting about? If so, I'll let you go before I…
Gokhan Uslu 00:34:58 Yeah.
kennedybushnell 00:34:59 Okay, go ahead.
Gokhan Uslu 00:35:00 So, not entirely related, so I'm not sure if… I just wanted to ask, and to see if this is a related question to tenancy or not, because not entirely… Related to tenancy in my mind. But say there are multiple, The telemetry pipeline configurations.
And there is, And that we want to optimize it. We want to, instead of, say, for example, having Having two pipelines, we want to merge them together, but we still want to extract separate telemetry.
The same data can be running through the same process… one processor.
Okay? And then going to two different endpoints in the exporter.
And what I want to extract from processor is that I want to extract telemetry in a duplicate manner, so that it has attributes… so, say, one attribute dimension is an identifier of one pipeline definition, the other is another pipeline definition identifier. It's the same attribute name, different value.
And a processor would be emitting a metric Once, but at the… Time of… Sending that metric, like, to outside.
I was wondering… If it would… be a good idea to duplicate that metric once per the dimension value, or attribute value.
Does it make sense?
kennedybushnell 00:36:35 I think I understand what you're saying, and that's why I posed the question in chat, so that's why it matters that we have a decision here, because today, processors can literally just count with an atomically set Incrementing value, like the batches that they've touched, or the items that they've touched, and they know that that's going to be correct, because you're not sub-partitioning beyond the processor itself.
But as soon as we implement something like this, they now may need to have a map of such values, and be aware of what the kind of, like, lookup key for that map is, and all of that stuff. So, It… you're…
Gokhan Uslu 00:37:16 Yeah, like, some static, static dimension value that I want to add, sorry, dimension key that I want to add with two different static values, so that the metric is emitted one per that value, kind of thing.
kennedybushnell 00:37:29 Right, like, you're, you're proposing like, subset of what I think this design that's being proposed would ultimately do, where it's, like, much more open to what that that tenant, I can't remember what it was called.
jmacdonald 00:37:47 A tenant descriptor is the word I'm using, and Kennedy, I did, I did encounter… This crossover between how we instrument and the question about whether a request always associates with a single tenant, or whether a request can, like, logically contain a multi-valued tenant.
distribution. Yes, the multiple.
Gokhan Uslu 00:38:09 Yes.
jmacdonald 00:38:10 like a, like I would consider a gauge histogram is the right data structure conceptually here. And I did write this as an open question. I've avoided any complexity going in that direction for… to be res… to be minimal on this, but I've considered your question, and it's not unreasonable, so I agree, it's worth pinning down.
And I left it as an open question down here, multi-value limiter requests. Like, I have a batch… I have a rate limiter, and I don't want to split these requests, and I'm going to use the resource key as the… as the tenant descriptor, and now I have to, like, virtualize the limit request to, like.
pre-compute or, like, iterate over the request resources as I'm limiting, which makes the whole… whole complica… it's a lot more complicated.
kennedybushnell 00:38:57 Yeah, plus you can split and fork.
So, the way that you output that metric becomes different depending on the scenario there as well.
jmacdonald 00:39:08 Right.
Gokhan Uslu 00:39:09 Sorry for… I just wanted to finalize… say final thing. So, I… I anticipate this is something that we will need, just from our side, yeah.
So I'll be happy.
jmacdonald 00:39:21 I want to get more detail, make sure I fully understand it, but we can take that offline. Okay.
Alright, I think we beat that one up. I want to follow up and learn more, Because I think there's a separate question that Drew was really asking, and we steered it a lot into the multi-tenant question, topic area, but it seemed like… Well, anyway, please read my document on multi-tenancy. I actually have a section on multi-tenant observability, where I may have also brushed on this topic.
somewhere near the very end, observability limits. Well, you can see where I am. But there might be something different that you're asking for.
So anyway, that was what I thought of when I saw this issue on Geneva event name mapping, is that we might want to map by all sorts of things.
Kennedy, do you have a different new topic?
kennedybushnell 00:40:25 Yeah, so it was back to what Albert was kind of talking about. So with that idea of, like, the concept of routing on, like, a key, I'm curious if your thought was that That it would… Yeah, this example. So… if I'm routing by service name, or part… partitioning by service.name, that becomes part of, like, some context that flows in, or I could, like, hash, like, those are both great examples. Does… does this allow for, like, collapsing and all of that? Like, let me give an example. So, in Utkarsh's proposal, we have scenarios where, like, you might have Event 1, Event 2, and Event 3, and you can pick what that field is. Let's just say event name to be easy.
You might say that Event 1 goes to a table called Event 1, and Event 2 and Event 3 goes to a table called Errors, or something.
would your… proposal allow for that, or is it more just, like, you… you take the event name, and then I'm going to partition by that, and then something downstream then goes and… Like, batches, or… or something.
Albert Lockett 00:41:49 Yeah, so I think, like, I think that… the… I think you could do both, actually. So, like, I think that what you would… probably, like, what you would be able to do with the transform processor with this proposal would be to… you could write an OPL program that's, like, if the event name is this, this, or this, then set the header about… then… Yeah, it's actually… it's actually easier, because you could do… you could do something, like, if the event name is this, this, this, set the header value to this… to this static thing.
or sorry, the header value, the context value to the static thing. Otherwise, set the context value to this other thing, right? And then downstream, you're just routing on that, that context value.
So, like.
If, if, like, if you didn't, like, if you didn't want to have, like, that, like, if the event name is this, this, this logic, like, built into, like, where you're routing downstream, then you could do it, upstream using, using the transform processor.
kennedybushnell 00:42:58 So it's a standard transform processor.
Albert Lockett 00:43:02 Yeah, I mean, I, I was, I was imagining doing it using the transform processor, just because it's, like, like, of, of the, Of the nodes that we've implemented, it's, like, the… probably the most straightforward way to achieve what you were describing.
jmacdonald 00:43:18 And that's because it has built-in logic for the splitting and the multiple output batches, I think.
Partly what you're saying that for.
Albert Lockett 00:43:26 Yeah, that's, that's, that's right. Like, you can, That's right. Yeah.
jmacdonald 00:43:36 I was going to answer the question slightly differently, not to contradict, but just to add more, like, options to the landscape, is that, I… in my tenant proposal that just got posted, you might have a tenant descriptor that is event name, and that that is an advanced use already, it's, like, not V1, because having event name requires that you logically split every request As it comes in.
and into groups by event name first, and then you have conditions saying if event name is A, go to destination, you know, the pipeline, or… but it sounds like what we're actually doing is schema-specific batching here, and Definitely we should all read the proposal I made. I'm gonna look into this one from… from Albert, but as I mentioned earlier, there's… I'm trying to keep tenancy and sort of routing by descriptors separate from partitioning, because partitioning happens beyond tenants, in addition to because of tenants.
kennedybushnell 00:44:38 Right, so would it… So I'm a… I'm a huge proponent, first of all, to have, like, using… just standard processors, right? Not having routing become, like, a… a special node type, necessarily, but it does kind of sound like routing key and partitioning key may need to be first-class citizens in the system. And we treat those special as we're connecting nodes.
But… But you still use standard transform… like, standard receivers, processors, and exporters to set those keys.
And I think that does simplify a lot of stuff here.
jmacdonald 00:45:22 This is a cool idea, Kennedy. I feel like I want to think about it. But, what you're basically proposing sounds great. Like, the idea is that the pipeline definition has some sort of overlay that tells you that actually, in fact, this is a bunch of routing that's by some… Data and or tenant key that is not… That is sort of implicit in the pipeline definition, is what I'm hearing you suggest.
kennedybushnell 00:45:48 Yes. Yeah, it could default to just, like, pass through to next node, and that would keep default behavior, and now that I think about it a little bit more, I don't think partitioning… partition key necessarily needs to be one, because you would just say… you would, like, as you're processing that, you just make it another batch.
With potentially a new routing key, and that becomes your partition inherently.
So, routing key may get promoted, I think.
jmacdonald 00:46:20 I think it makes sense. I'm also just imagining how there's sort of a… if I want to do batching, let's say, by service name, then I would prefer to just read a batch processor exists with a configuration that says, logically, the pipeline is split into service name.
individual requests, goes through the batch processor with batching by service name, and comes out, so it looks like one pipeline with just a sort of, Splitter and joiner implicitly kind of grafted on for the keys that we're using.
I like it.
Albert Lockett 00:46:54 income, and I think that, like, on this issue that was… I think the wrong had a suggestion, like.
somewhat similar to that, where he had, like, a, I think it's, like, the very last comment on the, on the… on the issue that Karsh had open.
Where, he was trying to call out, like.
You could have this, this partition policy that you set, like, on a particular node.
And then, like, what it does internally is it sticks our partition processor, like.
In front of it as it constructs the pipeline.
kennedybushnell 00:47:39 Yup.
jmacdonald 00:47:40 Super cool. I think we're all on the same page.
Utkarsh 00:47:42 Yeah, I mean, just wanted to say one thing here, like, I agree with Kenny, because I… I read this suggestion by Laurent, and I think it looks good. It gives us a way to… go forward in Geneva Exporter with this feature, and… make it simple when this policy partition thing is supported at the engine. But one thing that wasn't very clear in this example, so if you look at that policies partition configuration section.
Key is geneva.event name, And it's not very clear, like, how that… Key gets resolved to the routing key specified within the event name mapping section of genuine exporter, so… Something has to be, like, a first-class, thing, first-class field within config for any node to specify, and for partition processor to know that this is what I should be looking at, or, like, this is the partitioning key.
Because right now, here, it's not very clear how that gets resolved. I was gonna comment and ask Laurent, like, about it specifically.
Right.
Yeah, Kennedy, do you have a question around this, I'm assuming?
kennedybushnell 00:48:51 No, I mean, I agree with you that that's not super clear. I can make some assumptions based on what he's got there, but I think having him answer that would be better. I had another comment that I just wanted to make, more general comment.
jmacdonald 00:49:07 Let's… let's do it.
kennedybushnell 00:49:08 Yeah, so generally speaking, I'm not a huge fan of implicit configuration for anything other than default values.
So, like, there was just a comment made about, like, maybe we implicitly go and grab the partition info and stick it… stick a node in front of this node. I think it would be better to just Explicitly put that partition node in front if you know you want.
Partitioning, right? And not special case it.
Utkarsh 00:49:40 I think it would still be explicit, right? Like, from what I understand from your suggestion, the… You have to put that policies partition, config section Explicitly.
You just don't have to, create a partition processor separately in the YAML. That would be… Done by the engine.
kennedybushnell 00:50:00 Right, but what… what do we gain with that?
Versus… What do we… making the partition processor sit in front of this and explicitly tying it up. Like, not ex… not just explicitly… I agree, it's explicit in this config, because, like, there's that conversion that you just need to now know happens, but now you need to know that that's what happens, rather than just… Easy partition processor right in front of where you want it.
Utkarsh 00:50:26 Yeah, I think the benefit is mainly that you… your Geneva exporter or the backend related config is confined to just one node, which is Geneva Exporter.
Otherwise, the operator has to fetch some part of the config for a dedicated partition processor, and some for a Geneva exporter. So you have… you're splitting the config information across two nodes, multiple nodes.
Versus in this approach, you… It's confined to just any VAX portal.
So if I were to not use policies partition here and have a different dedicated partition processor in the YAML, I again need to refer to my Geneva config.
The… the backend config, right?
To know what the partition key should be.
kennedybushnell 00:51:19 No, it's the YAML config, right? So, like, as you're translating your proprietary config into the YAML config.
I think it's put there, right? Because otherwise, like, what he's suggesting is a policy concept would not be just for Geneva exporter, right? It'd be for any exporter.
Utkarsh 00:51:38 Yeah.
It would be for any exporter, yeah.
jmacdonald 00:51:44 I could imagine a pipeline configuration or validation that happens at startup that says, okay, I know the Geneva exporter has a routing key, which is event name, and I… and I… therefore, the inputs to Geneva must have event name, and then, like, it could check the whole pipeline and make sure that everybody is routing by the same key.
kennedybushnell 00:52:07 Yeah, that… that makes sense. I… I guess I'm just…
jmacdonald 00:52:11 Against syntactic sugar, is what I'm hearing.
kennedybushnell 00:52:15 No, like, if it's such a common scenario that it makes sense to do, and it simplifies the config, then sure.
But if it… I don't know, I personally think it'd be easier to grok the DAG by seeing that the partition processor is sitting there, because I put it there, and things like that.
Like, typically, those types of things are… Like, compilers overused, but, like, have something like that that compiles it down to your running config.
I don't know.
jmacdonald 00:52:56 One takeaway that I'm getting here is that we may want to partition within a pipeline, and we may want to partition as we distribute across a topic, and that is, like, hopefully we're using similar configuration for both of those. I think I personally need to think about this a bunch more, it's really interesting.
I think we've, come around on that one. Very good.
And here we are, we've used most of the meeting, Doing triage of the most interesting issues.
I should come back to the notes to make sure, but I think that that covers all the, like, really likely, contentious ones.
Tom Tan 00:53:39 A one machine. I'm gonna pass.
jmacdonald 00:53:40 the ones by Tim. Sorry.
Tom Tan 00:53:43 Yeah, I have one issue, I think. I would like to get sick, advice.
33… 3320.
jmacdonald 00:53:52 3320… there it is.
Tom Tan 00:53:54 Yeah.
jmacdonald 00:53:56 Okay.
Tom Tan 00:53:57 And, the follow-up approach.
That's in the last report, that's 3 proposals, and Yeah, the last reply, the little below, yeah.
Scroll down.
jmacdonald 00:54:17 Oh my gosh.
Tom Tan 00:54:18 Yep, yeah.
jmacdonald 00:54:20 Okay, this the three?
Tom Tan 00:54:22 Yep.
The first option, exclude every… every now ask. I think that makes sense, so… I think we will make a decision on allow list or deny list, which may… Which one makes more sense for our… raster source files.
jmacdonald 00:54:49 I have come to think that the restriction on non-ASCII is totally fair, for the record. And I hate the AI with all their dumb Unicode that I could never type myself.
kennedybushnell 00:55:03 Yeah, so…
jmacdonald 00:55:04 For the record.
kennedybushnell 00:55:05 I'm fine with either. I've found non-ASCII to be restrictive, overly restrictive in very few cases, but slightly frustrating, but I've always been able to work around it.
jmacdonald 00:55:17 Right, like, Laurent's name, his last name contains Unicode, and darn it, it's hard to type. Yeah.
Well, personally, I would vote for full ASCII just to be simple, even though I recognize occasionally it becomes an obstacle.
kennedybushnell 00:55:37 As long as there's… as long as there's an escape hatch, like most, like, linters have where you can say, this line's fine, because especially when you're trying to, like, write a unit test for Unicode, and now I can't because this stupid linter won't let me, like, that sucks.
jmacdonald 00:55:54 Yeah, I'd be… I'd definitely be okay with that as well.
I actually think it's harder to read those, like, Unicode symbols than to read, like, an emoji in the source code. Sometimes it's… obfuscating and potentially more of a vulnerability to have, to have ASCII codes. Cool. Well, I'll write that, seems to be consensus… I can't spell… on… a first option.
Oh, ASCII… Especially if there is an escape hatch.
Cool. Very good.
kennedybushnell 00:56:40 Gokon had an agenda item. Did we get both of yours, Drew?
jmacdonald 00:56:46 Oh, yeah.
drewrelmas 00:56:47 So we had 3 items here, and we got 5 minutes left.
kennedybushnell 00:56:52 You didn't get through any of them, great.
drewrelmas 00:56:57 Gokhan, do you want to go first? I can take some of mine offline, but I know you're.
jmacdonald 00:57:03 And I can help, Drew. I have context on this stuff, and I'm not sure that there's… if we can only have 5 minutes, I'd rather hear from Goken. Apologies.
drewrelmas 00:57:10 Sounds good.
And Pratish is here as well, who's the actual author of this PR.
jmacdonald 00:57:16 I'm good.
Oh, good, because… okay, so would somebody like to speak for minutes of time about this topic, about this, new capability?
Gokhan Uslu 00:57:26 Yeah, so I just wanted to ask, in general, this is the first capability, right? So it's going to be part of the engine, and I guess a good review of an understanding of what this means would be helpful to set a direction of how the capabilities maybe should evolve in the codebase. For example.
One of the things that I wanted to bring up, Is then, In this case, what this means is that… in goal case, most of the authentication manipulation is basically based on header, not all of them, but based on header, and roundtripper and HTTP calls, etc.
But there's no, global HTTP client, set up in Rust, so… This approach would mean, in this case, that, for example, any exporter that wants to support multiple authentication methods.
would need to, optionally require… sorry, optionally, depend on a capability, and then have their own implementation of how they use that capability. So, like.
If you use SIGv4, or if you use Bearer token, etc, etc, you can require them optionally, and so you can get them optionally, and then write your own usage of it within the exporter.
Or, maybe, you know, an alternative approach is a much more generic out capability that can do everything. I'm just, you know, talking about Xtreme. So, just to give you an idea about what this capability might mean, For all the, you know, usage areas and cases, and if you want to look into it, and if you want to say, like.
How granular we want to have, at least.
In this case, authentication-based, capabilities, for example.
jmacdonald 00:59:23 Kennedy.
kennedybushnell 00:59:25 Yeah, so I think what I'm hearing is you're… you're trying to decide if we should expose the capability as more of, like, information that you're then required to act upon, or if the capability should be something that, like, you pass a larger object, like your HTTP request to, and then it modifies that?
Is that kind of the… the pivot point you're…
Gokhan Uslu 00:59:52 Yeah, but, for example, choosing that would mean that maybe we would need to stick with, like, request API or something, like, we need to pick a client or something, or… or, like, we need to have some different alternative implementations, so to think and understand What kind of approach, what kind of balance we want to, you know, make.
At least, for example, if we can narrow it down to say that for auth purposes, for… authentication for outgoing requests, for example. And, you know, if this PR is approved, my understanding would be that And each authentic… like, each authentication method would have its own capabilities, but then an exporter that would only depend on one authentication method would be mutually exclusive of all other authentication methods, so would need to be like, okay, you can only choose one capability, error out, and then afterwards.
with the choosing capability, implementing some logic in the exporter, or stuff like that. Just… I'm just trying to share my, share the general idea, give some context for the review of this PR. I'm not trying to make any statement, just a little bit, you know, probe some questions, put some questions out there.
kennedybushnell 01:01:11 Yeah, so… so back to the, like, kind of the… generality that I keep bringing to the table.
Like, let's take, for example, CERT-based auth.
And you may want to use that with a HTTP protocol, and even if we said you always use request in, you know, DF engine. What do… how would I use that capability with my custom protocol that's not HTTP-based.
Like, that's something that we should think about as we kind of make this decision, I think.
Gokhan Uslu 01:01:53 Yeah, I mean, my… what I'm leaning towards is, impersonally, I would think, like, maybe each implementation side should have its own logic, and then the certain… Level of granularity should be supported at capability level, but shouldn't go as, like, very generic.
And, and there's, like, a very vague… concept, but, in my head, saying that a bearer token, or MTLS, or API key, or what, what, whatever, whatever, whatever, what else have you, like.
Seemed like a good level of, granularity to define those capabilities, but again.
it's just my idea, and I think that a general, like, consensus of the community would be a good starting point for us to start adding these capabilities.
jmacdonald 01:02:48 if I'm hearing you right, it sounds like when you start your exporter, you're gonna say, these are all the off methods that I could possibly know of that are applicable to the protocol that I speak.
I have a way to do… to use a bearer token, so I'm gonna try that one first. I also have a way to use a TOS something, so I'm gonna use that as a second alternative. I also know about something something like service tokens from my cloud provider, so that's my third option.
And when my configuration comes in, I will get a sort of meta capability, which is auth.
And within auth, there's the, like, all the iterations that I know about, that I'm going to enumerate to see if we can bind correctly. That's what I heard. I hope that's.
Gokhan Uslu 01:03:34 That would be more like, say, for example, I will give my exporter one capability, and my exporter will be like.
I'm okay with these 5 different capabilities, and you provided me one, then I'm gonna use the one that you provided and ignore all the others. If you provided in the configuration two different capabilities that I can use for same purpose, then I'm gonna say, oops, it's not accepted, you need to pick one.
jmacdonald 01:04:01 It sounds good to me. I'm gonna take a closer look at this tomorrow.
kennedybushnell 01:04:06 Yeah, and then one other option to, like, kind of help with the concern around, like, requests and how it hooks up is… It's a pattern I've seen used elsewhere, is have helpers kind of tied to Maybe the capability itself, where it knows how to attach itself to a request.
request. And then… then you at least know that, it's consistent among the uses of that, so that if I'm not an expert on, off, and I… I know I want to use this thing, I still don' Can look for the common pattern on how I do this right.
Yeah, I saw that correct, right?
jmacdonald 01:04:46 Absolutely.
Goodbye.
It sounds good. I think, Gokan, does that sound good to you?
Gokhan Uslu 01:04:56 Yeah, I will talk with Kennedy to understand the latter part. I didn't fully understand, but we are out of time, but, Yeah.
jmacdonald 01:05:04 We are out of time, and well, I've been speaking with these other two about… with Drew, so Drew, I can try and help in the meantime. I'm sorry that we ran out of time for you.
Thank you all for being here. We'll try again next time.
Bye.
kennedybushnell 01:05:20 Thanks, Al.
drewrelmas 01:05:20 Bye.
