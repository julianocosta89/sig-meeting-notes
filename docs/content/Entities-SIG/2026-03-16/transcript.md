SIG: Entities SIG
Date: 2026-03-16
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Josh Suereth** 01:33 Hey, everybody.
**Dmitrii Anoshin** 01:38 Hi, everyone.
**Daniel Dyla (Dynatrace)** 01:39 Hello there.
**Josh Suereth** 01:39 What are we.
**Martin Kuba** 01:42 Whoa.
**Josh Suereth** 01:47 Alright, so… Get our agenda going. Welcome, Martin.
**Martin Kuba** 01:55 Thanks, I think Ted's gonna be out next 3 weeks, So I'm kinda here for it in its place.
And also to see, like, if there's anything I can do to… Help with… Browser, being more, you know, having more participation.
**Josh Suereth** 02:13 Yeah, yeah, I think the main thing we need to know is, like, for browser, we still have to solve a bunch of problems that, are kind of implicit to the SDK.
We had a bunch of discussion about that last time, I think. I don't know if you saw.
the, things we were talking about, anyway… Cool. I just saw that.
**Martin Kuba** 02:37 I didn't see that, so… Josh Suereth 02:39 Yeah, we can dive into that again. I don't want to, rant early here, but welcome.
We'll do a quick… Recap of browser.
Okay, Dimitri, do you want to kick off the first discussion here?
**Dmitrii Anoshin** 02:57 Yeah, so I just wanted to start at least, like.
initiate a discussion about this particular pull-up problem. I'm gonna… kind of… we'll be able to drive it, but I need some direction from you folks. So, essentially, the problem is that, as you might know, collector… sometimes.
creates service, entity for… for services that it discovers, but it doesn't have all the data. So, for example, if a service is emitted by the by the instrumentation SDK, it's the owner of that data. It knows, like, service instance ID, service name, and it can be considered as a source of truth. From the collector perspective, it's not the case because there are observers, which discovers some services that are running in the environment, whether it's on the host, or in Kubernetes cluster on a particular node, or in the faster, etc.
And also, if you create a receiver.
You can also, like, some of the receivers can specify services.
And, the logic there is different. Sometimes it's… just, like, using IP address for service instance ID with some port as an identifier. Service name is also… there is some different logics in different receivers to implement that. So, what I'm thinking of is that like, it's specifically for this service, I haven't found any other like, similar issues for other entities. So, for example, if you think about Kubernetes, for Kubernetes, like, UID, always exposed by Kubernetes API, so it's not a problem to use that. It's always available. But for the service, it's com… it's com… Always, this problem can't come… is, like, is always there. So… And, for example, if collector is getting data with the GLP through SDK, right, and if service is instrumented.
And it sends tracing data. And also, the same collector is discovering, like, metrics endpoint, let's say, Prometheus endpoint, or, like, radius styles, whatever, from the same service, essentially.
it would create different… different IDs, different identifying attributes for the same service.
So… I'm thinking of that we should maybe introduce a separate kind of an entity.
Like, let's say, let's call it observed services, and potentially it can have same… same identifying attribute, service ID.
The service name and everything, but also it would need some information about the observer itself.
It'll be, like… I don't know, maybe service observed by. I haven't fleshed out all the details, but I just want to, like, initiate initial discussion. And in that case, if we ever want to combine them and have some logic in the collector, it will be clear, at least, that they are separate.
Separate entities, and we potentially can just emit relationship between them.
And we just delegate that, that, like, association to the backend.
Go ahead, Josh.
**Josh Suereth** 06:32 Yeah, this gets… This is where things are getting kind of fun.
I can't spell observed right, sorry. I do want to put this PR later, because we should talk about it.
Okay.
First of all, you're talking about having observed service.
And this is where relationships and entities get fun.
Would it make more sense to have service have an observer Like, tag to it?
So, so instead of the one way, have it go the other way. So, in service itself, we can say this is observed by something.
**Dmitrii Anoshin** 07:10 Right.
**Josh Suereth** 07:11 So there's an observed by relationship, but the next thing is… does it need to have a different name, or does it only need to have a different name because we can't put them both in OTLP resource?
**Dmitrii Anoshin** 07:22 Right, and not only on TLP resources. TLP resources, like, let's say.
**The limitation that we introduced, but that limit… Josh Suereth** 07:34 Oh, did I lose internet?
You're muted, everyone else.
**Daniel Dyla (Dynatrace)** 07:39 Yeah. No. Okay. Dimitri, Dimitri froze.
**Josh Suereth** 07:44 Okay, we have, crazy windstorms going on, and, like, our school district's out of power, so in case I drop, you know why.
I did not think Pittsburgh would be a hotbed of wind.
**But, you know, there was a tornado on Friday, but… Daniel Dyla (Dynatrace)** 08:01 I think you're… you're getting the same storm that we just got for the last two days that ripped a bunch of shingles off my neighbor's roof and the siding, and some stuff like that.
**Josh Suereth** 08:11 Yeah.
You should keep that stuff on your side of Erie, okay? Don't… don't send it our way. Keep it up there.
**Daniel Dyla (Dynatrace)** 08:21 It looks like he's gone.
**Josh Suereth** 08:24 Alright.
We can keep ranting about the weather. This is a problem.
**Daniel Dyla (Dynatrace)** 08:35 The… the problem… the… the fact that we… we sort of conflate observed and observing service in the same namespace.
**Josh Suereth** 08:46 Yeah, well, no, the fact that we can't have multiple entities of the same type in the same location, because all the attributes start to just glob together in ugly ways, right?
Like, there is such a need, as we do some anti conventions and model these things, there's such a need to have relationships be, like, a special attribute on an entity. So we're doing things like service.owner.
Where owner might actually be a straight-up entity.
that would get reported. There might be, like, a list of, like, service owners that you could report as a… in the NC signal.
But we really want to have a service.owner field, or a service.
Cost center field was one of the ones they added, because people want to do financial reporting.
In the service and deployment SIG, they want to do, Criticality, and anyway, the point being, like, How do we handle two of the same type of a service, where there's a relationship between them. One of them is actually the service that the thing is, you know, talking about, and one has some, you know, extra role to it. Like, it's the observer, or it's the observed.
That makes things a little complicated.
I do think, real quick, I looked through the spec, and I made comments on it before. Let's go through this PR while Dimitri's out, and see if we have anything we want to challenge here. It doesn't have any approval from the entity SIG. It is assigned to me, and I do need to get this through.
And sorry, I've been dropping the ball on this, but this basically changes the description of resource to consistently call it the observed entity.
Everywhere.
So here is one of the big changes. This is in the data model.
Resources are representation of the… or represents the observed entity, as opposed to the entity producing telemetry.
Right.
So it's the observed entity for which telemetry is produced, which just reminds me of Pennsylvania Dutch syntax, where you use as many prepositional phrases as possible.
And I couldn't figure out how to make it Not read that way.
**Daniel Dyla (Dynatrace)** 11:05 to me, this… I mean… Strictly from a spec standpoint, strikes me as a breaking change. Whether it is more representative of real life or not aside, it is the opposite. It's sort of like inverting the definition of resource here.
But the problem is we regularly have used resource to mean both things, right? We have the telemetry SDK attributes right alongside the things that are being, observed, and it's all just kind of bagged together, and that's what resource has always been. It's both.
**Josh Suereth** 11:42 Well… Yeah, that's because we basically optimized our whole specification around SDKs.
And we don't handle any advanced situation, right? So, like, this is the line… this is the only important piece here.
The entity that technically emits telemetry and entities described by a resource are not always the same. In auto instrumentation scenarios, such as eBPF-based agents that observe a running process without code changes, the instrumentation agent produces telemetry on behalf of the observed workload.
That is what we're trying to allow. So this is basically, like, what if the SDK isn't in process? What if it is out of process and still doing work on your behalf? You should still be able to report that way. And I think this somewhat relates to what you need to do, Martin, of, like, you want to report about session.
And the lifetime of session is not the same as the SDK, and we don't have a solution for you.
And we haven't given you a solution. At all.
So this at least changes the definition to be what we want to be. And here's… here's the thing. The data model, this document is still… Where is it? It's still development.
We never stabilized our data model.
**Daniel Dyla (Dynatrace)** 12:57 The resource data model is still development?
**Josh Suereth** 13:00 It never existed before the entity SIG wrote one.
**Daniel Dyla (Dynatrace)** 13:05 Oh, okay, I guess I didn't realize that.
**Josh Suereth** 13:08 Yeah, this document is stable.
This is the resource SDK, which is the only thing that existed prior.
**Daniel Dyla (Dynatrace)** 13:16 Yeah, okay.
**Josh Suereth** 13:17 So, and here it's saying a resource is an immutable representation of the observed entity for which telemetry is being produced, expressed as attributes. So that's the big change of… is an immutable representation of the entity producing telemetry.
I actually think that, in my mind, this is… this is just a better description.
And I think that we should probably allow this. Let's see, the README change also changes to resource represents the observed entity for which telemetry is produced, as opposed to the entity producing telemetry.
And then it also add… like, oh, I already showed that note, right? That was an SDK, because the data model… Yeah, this is the data model, which is listed as development. The README, I don't know if this one lists stable or not. I don't think it does, because again.
I don't think this existed until we wrote it.
Yeah, we… like, we wrote this as part of the entity SIG, because there was no… there was no description of what resource was or what it intended to be. At all.
there was, like, what it was in the SDK spec, which was just shove a bunch of attributes and go.
**Daniel Dyla (Dynatrace)** 14:25 Yeah, I mean, I think all this is fine. I… I know I did just mention that I thought it might be considered breaking, but… you know, if you consider the SDK as a part of the process that's being, monitored most of the time anyways, it's not really… and this is a much more accurate description of the way that it's actually used in practice. Yeah.
I… I'm fine with this change.
**Josh Suereth** 14:51 Alright, I'm going to approve this and merge it then, if no one… does anyone… I'll give one last round for folks to complain about this. Anyone have any concerns with this before we… Okay, cool.
I'm gonna approve it on behalf of the SIG.
And then… because I… I don't know why we didn't talk about this last week, and then… I think that one's good to merge.
Cool.
Right.
Let's come back.
Hopefully, Dimitri can make it back.
If not, because I want to continue the discussion with him, Martin.
You want to do a quick… we can do a quick recap of browser-related things?
**Martin Kuba** 15:45 Sure, yeah.
**Josh Suereth** 15:47 Okay, so… let me just refresh my memory from our discussions.
You had your prototype in progress, and we talked about it. Basically, for entity doesn't look like it's gonna work for you.
**Martin Kuba** 16:00 Right. No.
**Josh Suereth** 16:01 Yep, you still need to be able to mutate things. The main problem we have right now is, We implemented the… thing that Ted had proposed, and for most SDKs, it's gonna be really a pain in the ass, and really breaking for metrics. It's, like, really, really awkward. If you go forward without a metrics API and SDK for browser, it's probably fine.
But we still need to find a solution for that.
Of what do we want to do about metrics?
In the browser, because I don't think we have a solution. But the thing where, when you generate a span, when you generate an event, you just attach to the latest, resource that's in some sort of resource container.
Works really well for spends and logs.
For metrics, huge problem.
**Martin Kuba** 16:54 Yeah, I think we've been, like, in, Pretty much agreement, like, in the browser space, and also, like, with Talked to the mobile folks about it, and… We've been in agreement that, like, we don't need metrics, I mean, there's… at least now, like, from the client, client, you know, client instance SDK perspective.
**Josh Suereth** 17:17 Yeah.
**Martin Kuba** 17:18 But, I mean, there's… it's possible that you could find some, like, edge use cases for that, but if you can say, like, that, like, for… You know, before the first pass, like, we don't… we don't… we just do it without metrics, then we would be fine with it, I think.
**Josh Suereth** 17:34 I think, if you look at our metrics model as, aggregated events.
What we're saying is, you just need an event model, that's it.
Where you can fire spans, you can fire events.
you're good to go. I… I also… I strongly encourage Ted, and he didn't really like this, but, like, to think about our APIs and whether or not you need a, like, mobile edge-focused API that is dedicated for that use case.
He said you were gonna do, like, an end-to-end demo of, like, you know, maybe aggregating events and making metrics in a collector when they come in from the edge, which is awesome. Please do, like, I agree, you need that. But I also would consider, in the long run, of, like, whether or not… our API is actually serving you the way it should.
Right? And, like, are the concerns that we have right for browser? If you have the right set of extensions and hooks you need to make logs and, and, sorry, events and spans the tracer work, great. But if you need to deviate, I… I'm personally comfortable, because I know enough about the mobile space, of having a different API service for the mobile space, like, for browsers and for phones.
That is well-tuned and highly optimized for, like, the environment that you run in there.
just… just from knowing details about it. Like, I think… I… anyway, as you push on it, like, I would ask that question of, like.
are these APIs and things actually serving me, or am I just only working around them?
The other thing you should ask.
and don't hate me, is the OTLP protocol.
Serving me well.
**Martin Kuba** 19:20 Right.
**Josh Suereth** 19:21 And do I need to make optimizations to that to get data out of the client? I think we had talked a while about having multivariate metrics at some point.
It's possible that, like, to get efficient data out of the browser, we need to think about bundle package size and having, like, multiple pieces of data attached to it, and then getting it to a collector that extracts all that out and turns it back into OTLP.
That is something to consider. When you look at what the profiling group did to make their work efficient.
they, I don't know if you saw, they talked in the Spec SIG about how they use dictionaries, and they did all sorts of craziness to… you, you may also want to consider that. Those were things we talked about in the past.
**Martin Kuba** 20:03 Do they… do they have this documented somewhere? Like, do they put it as a part of the specification?
**Josh Suereth** 20:08 Yeah, it's in, it's in, here, Let me close out the Weaver release notes and open up the proto so you can see.
So, this is actually going alpha, relatively soon.
I think this week I need to merge it. But if you look at the profile signal, they talk about how they have a profile dictionary.
And then, they document what the dictionary is, how the dictionary works, how you don't have dupes in the dictionary, and that sort of thing. And then they have, in their table for, like, profile things, all of these Sorry, in profiles, everything has this, like, index value.
It is the underscore something index. It's basically a reference to something in one of these tables.
And they always have 0 mean the empty thing, so that if you don't put an index, you get the right behavior. That's another trick that they do.
But this led to dramatic compression of the protocol for them.
And I do mean, like, dramatic compression. Let me see if I can find you an index here.
Samples… Profile ID… Attribute indices. Here's an example. This, this is an index into the attribute table.
Right.
So that's… that's how they do attribute things. When they have values, they index into the attribute table and the unit table, if they're reporting units.
Units are also optional.
I think… yeah, there's an index into the link table, if you want to have links between profiles, right? So they're not kind of recording everything, they have this, like, decomposed structure. And… Since the structure kind of matches how they record the data initially, it leads to efficiency both in, like, the generation side and the reporting side, and then they deal with this on the back end.
Because again… the way they run, you need to have the least amount… like, it's a very expensive thing to do, profiling, so you want the least amount of overhead in your front end, the most amount in your back end. Some of the things we do, like with metrics or tracing, we might be taking more overhead in the front end to have less in the back end, and it's a bounce.
And I think, you know, some of the environments you want to run in, we really, really, really need to highly optimize, get the data off.
Keep it small, keep it short, keep it efficient.
And we can do a bit more in the backend.
So, just things to think about.
**Martin Kuba** 22:47 Well, this is great, I mean, this is… it's good to see that there's a precedent.
For something like this. Like, we've been talking about Needing to optimize the protocol at some point.
**Just because it's like, yeah, in browsers, like, obviously the payload side is a concern, so… Josh Suereth** 23:04 Yeah.
**Martin Kuba** 23:04 And the same for mobile.
**Josh Suereth** 23:06 One thing I want to do.
**Daniel Dyla (Dynatrace)** 23:07 only.
**Josh Suereth** 23:08 Okay.
**Daniel Dyla (Dynatrace)** 23:09 not only the payload size is a problem, but, like, there's a lot included in the protocol that is not necessarily needed for browsers, and like, the protobuf dependency itself is pretty non-trivial. Like, all of the serialization mechanics, that's all non-trivial, and then if you use JSON to avoid that, you end up with this enormous JSON structure.
for very little data. It's not efficient at all from a size perspective.
Yep. Yeah, I think long-term, there will need to be, like, a mobile events probably something that uses a much lighter weight. You know, if we want to do some binary protocol, you know, maybe Thrift or something is a better choice, but something very lightweight that is serialized very easily.
And doesn't include all of the, like, OTLP machinery.
**Josh Suereth** 24:10 Are you saying you can't issue machine instructions to count the number of zeros in an integer easily in the browser?
Are you implying that Protobuff could be inefficient somewhere?
Is that what you're saying I don't believe you.
**Daniel Dyla (Dynatrace)** 24:24 I mean exactly what I said.
**Josh Suereth** 24:26 Okay, okay. That was sarcasm, for anyone who doesn't… Yeah, yeah, okay. It's meant for other people that are on the call, yeah.
**Daniel Dyla (Dynatrace)** 24:35 There is, somebody from Datadog, And we're way outside the scope of entities now, but somebody from Datadog, wrote a hand-rolled… protobuf serializer in JavaScript. I haven't really looked into it, very… in depth, like, specifically an OTLP protobuf serializer, in order to avoid the protobuf dependency.
You know, you get other advantages, too. There's reasons some other languages have done similar stuff. And I haven't looked into it for, like, completeness and stuff like that, but I believe it's what Datadog is currently using.
**And… Josh Suereth** 25:19 the Java one actually led to a bunch of performance gains because, Protobuf is optimal if you're using, like, the generated code as your data structures, but when you're not.
Doing that translation is actually somewhat expensive, and you can optimize the crap out of it if you do it manually.
**Daniel Dyla (Dynatrace)** 25:37 Yeah, the generated code has to deal with a bunch of generalities that we just know… we know don't exist because we know the domain.
**Josh Suereth** 25:45 Yep.
Yep. It's just then you have to maintain that code. So, one thing I want to add, by the way, is, what I'd love to be able to do at some point, and browser might be able to use this, I want to get to the point where, for attributes.
you don't have to send the big old string at all. Like, if we wanted to have a side channel, like, and use schema URL to say, hey, here's where my attributes are defined, and you just give me a bunch of integer references to the schema URL, and I can look them up in some fashion.
That would make me so much happier in the future, because we could get, like, huge efficiency wins for you.
These are things I want you to think about.
I don't know how we do them. I know that they'll be highly contentious, and we'll have to discuss it, but just don't keep that out of the realm of possibility, right? The key thing we need is, when browser hits the OTLP layer, someone needs to be able to convert it back into pure OTLP that works in any observability vendor.
But for the transport layer, we have a lot of flexibility we could evaluate to just make your domain work well, and I don't want OTLP as designed today to be the reason browser fails, right? That's… that's fundamentally. So, I think… I think we need to start exploring options there.
**Martin Kuba** 27:03 Okay, that sounds great, yeah.
**Josh Suereth** 27:06 Cool.
**Martin Kuba** 27:07 I have a quick question on the prototype that I put together a couple weeks ago.
I don't know if you've got a chance to look at it, but, essentially, I tried to, like.
Think of, like, the easiest way that we could mutate the resource.
You know, so, like, I think the biggest… Thing in that prototype is… that, I added a set entity, A method on the… On the provider, on the providers, like, the log, logger provider.
Does that sound like a good approach to you, or do you have any other suggestions how you could handle this?
**Josh Suereth** 27:48 Yeah, I think the thing… the thing that we didn't do in our OTEP that you would be fine with is you could have this, A, you could have this be multiple entities.
Like, that is… that's just a thing that, for prototyping, we only did one to be lazy.
So if you needed more than one, feel free to do that.
I think the main problem with this is what we ran into. For logging and tracing, this is basically exactly how all the prototypes were. This is what it looked like in Java, for example.
For metrics is where it gets complicated, because, like, metrics is aggregating points against something.
And so you need to figure out what to do with those aggregated points.
And so, what we had was we actually, like, were forking the world.
And, like, remembering the old points and the new points, and reporting them once, and then dropping the old points after a report. And it was not code I think the Java community would ever forgive me for, if I sent it to them.
So, we ended up not progressing with that for metrics.
Because again… Go ahead.
**Daniel Dyla (Dynatrace)** 28:55 That's why the for entity and metrics, at least in the JavaScript prototype, essentially what it's doing is firing up a whole new SDK with a new resource, like, to avoid all of that garbage.
It just flushes and shuts down the old one, and it abstracts the fact that the SDK was changed out from under you in the SDK from the API.
**Josh Suereth** 29:17 Yep.
Yep, so with the… yeah, with meter provider, basically, you'd have to actually track the change of meter provider upstream in the instrumentation you write, for any metric you use.
But for logs and traces, that's exactly what we were doing. You're totally fine.
**Daniel Dyla (Dynatrace)** 29:36 Yeah, and this is why, Josh McDonald has been… I mean, for… More than a year now, possibly 2 years, he's been harping on metric resets and stuff like that for similar problems.
**Josh Suereth** 29:53 Yep.
**Martin Kuba** 29:55 So… so does… do we need to do anything, like, in the spec for this, or can we just have, like, our own… Daniel Dyla (Dynatrace) 30:01 We don't need metrics, and especially if we're gonna go to a, like, browser-optimized API, then maybe not.
or not, maybe, you know, client-optimized API that uses events Because the… both traces and metrics can be thought of as event aggregations. You're… it's a bandwidth optimization that you just don't need when you only have a single user at a time.
Yeah, it's much… you could just scale your collectors and say, you know, we just accept this as… a trade-off.
more work on the back end for less work on the front end, like Josh said.
**Josh Suereth** 30:45 Yep.
**Daniel Dyla (Dynatrace)** 30:46 We could even potentially… have dummy SDKs.
That, you know, you could have a dummy metric SDK that all it does is delegate measurements to an event to the event API.
**Josh Suereth** 31:03 Yeah, yeah, actually, if you want to see crazy shenanigans where I hijack the metrics SDK pretty horribly.
I'll sh… I'll show you something.
This is where I was looking at how do I get everything out of process as quickly as possible.
So the way this thing works is you create a file, you mapmap it between processes, which I know this is foreign words for browsers, sorry.
I'm just being dumb. Anyway, but you… you mem-map it between the two processes, and then you try to get the data off disk as quickly as possible. And so, the way this worked for metrics, you have… you have basically ring buffers that you're throwing stuff onto, and you expect another process to read off of it. By the way, this is fully implemented for Java and for Python.
But, yeah, the way… the way the ring buffer works, you fire… well, this is describing how it works. Oh, wrong thing. I need to show you… in the proto, what I'm doing here… Where is metric event? I think it's measurement? Yeah. A measurement event, I send an integer to a dictionary reference of the metric. I throw the key value attribute to the thing the person wanted recorded, the timestamp, the value, and then the span context. And I'm able to successfully reconstruct an SDK on the other side.
that will, like, create exemplars and metrics and all that kind of junk. But basically, I'm turning metrics, the whole metrics API, into an event stream.
Of these events, and I just fire them down.
This might still be a little expensive for you, like this key value ref. This technically is a dictionary.
You can't tell with the way the protobuf is written, but it's all working successfully. If you wanted an example of, like, some shenanigans I'm doing, or how to, like, write the SDK or whatever, feel free to look at this project. This is a prototype in protocol design and, like, SDK V2 things that I've been looking at.
I think I've shared this a bunch of other places, but… Yeah.
**Martin Kuba** 33:11 Anyway… Josh Suereth 33:12 It's fun. It's written in Rust, so if you hate Rust, apologies. If you like Rust, also apologies.
**Martin Kuba** 33:24 So, so I guess, just, like, just one more time, like.
For my own clarity, like, so do we… like, it sounds like we could just implement this as… as part of, like.
the browser-specific SDK, like, how we handle swapping out the entities, but it doesn't sound like it needs any, like, any changes in the spec, or… Necessarily.
**Josh Suereth** 33:50 I think… I would recommend implementing this and getting experimental prototypes out, and then, working on specification change based on that prototype later. I think you will need, like.
Let's say you're successful with everything we just talked about, I think there will be a specification around your API and how it behaves.
Okay. And that we want it to be consistent between browser, maybe phone.
You know, like, wherever you think this thing needs to live, I think we need to do that. But step one is, like, let's make sure we're actually solving the hard technical problems first, and don't let the current API get in your way, is all I'm saying. Because I think it is, yeah.
**Martin Kuba** 34:33 Yeah, okay, cool.
Yeah, sounds good.
**Josh Suereth** 34:36 Cool.
And if I could give you more help, I would. I'm just, you know, short on time.
Oh, and I'll put the, yeah.
Gosh, it's a dumb experiment.
I guess it's… I shouldn't call it a dumb experiment, it's just… I think I have more fun with it than other people.
are interested, github.com, choose today.
OTLP MAP. The other fun thing about that experiment, by the way, the protocol and stuff, I was able to implement an SDK for Java that takes less memory than the Java SDK, because it's written in Rust.
So if you instantiate Java with its normal SDK, and you instantiate my thing, where I have an SDK writing to this memmap file, and I have Rust reading it, I take less overall RAM, with my combined thing than the Java SDK. I'm not faster, but I get things out of process much faster.
So that's, like, the downside. For Python, though, I think I'm about 10x faster.
than the Python SDK. But that's not hard, because the Python SDK is written in Python, and tries to serialize protocol buffers in Python.
not with, like, native things. So, yay. Fun times.
Okay, cool.
Let's actually talk more about entities, then. What do we say?
I want to do some follow-up on active PRs and active status. I do think we need to talk about this more.
I just don't… like, until Dimitri gets back, I don't know how valuable it'll be to try to have the conversation.
**Daniel Dyla (Dynatrace)** 36:11 Dimitri's here.
**Dmitrii Anoshin** 36:12 I'm back, yeah, my internet is back, sorry.
**Josh Suereth** 36:14 Oh, good, I didn't see you come in.
**Dmitrii Anoshin** 36:16 Yeah.
**Josh Suereth** 36:17 let's… I think this is probably the most important conversation, then. You want to kick us back off with where things were?
**Dmitrii Anoshin** 36:21 Yeah, let's continue. You suggested we have another attribute, observed by, but in that case, if we want to ensure that we are not merging the two entities, observed entities, observed service and the service from the SDK, that absorbed by has to be an identifying attribute.
I'm pretty comfortable with that.
I… I'm not sure, to be honest. What… What do you think? So… It would resolve the problem, but at the same time, it kinda makes it… like, it kind of goes against the definition of the entity, I think.
**Josh Suereth** 37:07 Yeah.
**Dmitrii Anoshin** 37:08 Because we say that entity is identified, but identify an attribute, but observed by is not really an attribute.
**Josh Suereth** 37:20 It'd be descriptive, yeah.
**Dmitrii Anoshin** 37:23 And if it's descriptive, it's not gonna work.
**Josh Suereth** 37:26 Alright, so if I understand this correctly, right, let's show the example. We have, Service A runs on process B.
**Dmitrii Anoshin** 37:37 Yep.
**Josh Suereth** 37:38 Elector… C runs on process C.
But has service… D?
Sounds good.
**Dmitrii Anoshin** 37:51 Sounds like that, yes.
**Josh Suereth** 37:53 Okay.
Elector is observing process the… let me just say process A, too.
Okay. Access A, service A.
Right?
There's a reports telemetry with service.name equal A, right?
**Dmitrii Anoshin** 38:14 Yep.
**Josh Suereth** 38:15 Collector needs to know not to put service.
Dot service entity.
on… telemetry from service A.
But it thinks… It is service D.
Okay, so if we have an example where Service A is reporting telemetry, but isn't in, let's say.
reports telemetry, but forgets to annotate.
service name equals A. Let's, let's say this. This means that the collector's gonna inadvertently put service D on service A's data.
Right.
Is that the problem?
**Dmitrii Anoshin** 39:05 Yeah, I… I'm struggling to… like, really… Josh Suereth 39:13 Follow what I'm saying?
**Dmitrii Anoshin** 39:14 Yeah, like, I guess service name is fine. We can actually make sure that they are kind of synchronized, but service instance is gonna be always different. We will not be able to specify the same instance.
**Unless we… Josh Suereth** 39:31 Oh, oh, oh, this is, this is about observing service instance, right? Alright, so collectors, right. So, service instance… Collector cannot… synthesize a valid sales instance.
**Dmitrii Anoshin** 39:50 Right, right.
**Josh Suereth** 39:50 I think, has to come from the process.
specification.
**Dmitrii Anoshin** 39:57 it has to go… right now, it's coming from the SDK itself. SDK generates that.
what collector doesn't have.
Access to that.
**Josh Suereth** 40:08 What? Doesn't have access. Yeah, have you seen those shenanigans for how to get access to it?
**Dmitrii Anoshin** 40:17 Yeah, I saw some.
**Josh Suereth** 40:19 Yeah, I… So, for context, Let's come back. This was… this was… we talked about this a lot, when we were talking about Prometheus compatibility and, like, service instance name and early on in entities.
**Dmitrii Anoshin** 40:35 Exactly.
**Josh Suereth** 40:36 Yeah.
**Dmitrii Anoshin** 40:37 there is another issue that I can find, if you want to. Like, someone came and said, hey, we need service attributes on everything, service entity on everything, essentially. It's even, like, whenever it's coming from Prometheus, even if it's host metrics, process metrics, and I said, like, it doesn't make any sense if you, like.
**Josh Suereth** 40:59 Yeah.
**Dmitrii Anoshin** 40:59 like, what service you would associate the particular pod you're running in, or some Kubernetes cluster, like, metrics, for example.
**Josh Suereth** 41:10 So, my thinking here, I don't remember if we talked about this out loud. My thinking here is, we should be very careful about what service instance ID means, and what Prometheus IDs we use. So, service instance ID, right?
Let's go look up the definition quick.
Just to ground us all.
So in semantic conventions, the resource… Service… service instance ID is the string ID of the service instance.
Must be unique for every instance of the service. ID helps distinguish. Implements are strongly recommended to generate a random version.
Mediv is particularly recommended for applications running behind an application server. Like Unicorn, we do not recommend using one identifier ID for all processes participating in the application. Instead, it's recommended each division gets its own instance ID, so this is, like, different… even for… within an SDK, It's not recommended for a collector to set service instance ID if it can't unambiguously determine the service instance that is generating the telemetry. For instance, creating a UUID based on pod name will likely be wrong, as the collector might not know from which container within the pod the telemetry originated. However, collector… can set it if they can unambiguously determine the service instance telemetry. This is typically the case for scraping receivers, as they know your target address and your port.
**Dmitrii Anoshin** 42:44 That's… that's what I'm talking about. We… collector can do that, unambiguously determined, but it's gonna be still… it's gonna conflict with whatever SDK is provided.
**Josh Suereth** 42:56 No, unambiguously means that you can determine the service instance unambiguously without conflicting with what the service would be producing.
We should actually change the definition for that.
**Dmitrii Anoshin** 43:09 But there is no way, like, it's… I mean, I remember that we are being submitted to add this, but there is no, like, practical way to achieve that.
That's the problem.
**Josh Suereth** 43:19 Well, did you see the proposal where the SDK is going to be allocating a bit of shared memory, and you just look in it and grab the service ID from there?
**Dmitrii Anoshin** 43:26 Okay, but that should be a, like, safe approach will be available through, like, some kind of an API.
**Josh Suereth** 43:36 Yeah, no, that's what the API is, that's the proposal in the OTEP, is the SDK, it's a little piece of shared memory, and you look at it, and that's how you get your service instance ID.
I'm not saying, that's actually… there's a note tab for it. You can take a look.
**Dmitrii Anoshin** 43:49 application's gonna expose that information through the API.
**Josh Suereth** 43:54 do you mean… do you… by API, you mean, like, an HTTP API?
**Dmitrii Anoshin** 43:59 Any new API. Any API that collector would be able to use.
**Josh Suereth** 44:03 Yeah, the collector will be able to use this, and it's… Dmitrii Anoshin 44:06 Okay, that's… Josh Suereth 44:07 Yeah, and they're planning to use it for, like, OB and for eBPF Profiler.
**Dmitrii Anoshin** 44:12 Okay, cool, that's exactly what I was looking for at this call, actually, if there is something that people.
**Josh Suereth** 44:17 Yeah, where is that?
**Dmitrii Anoshin** 44:19 It's interesting.
**Josh Suereth** 44:21 We need to look at this one later.
Stable by default… I'm surprised that one's not merged yet.
**Dmitrii Anoshin** 44:32 Okay, once we… if we have there, we… I guess it's… it's… it's alright, we can use that API as a… First option, and then we need to figure out, what, like, pullback.
Exactly a fallback resolution process.
For, let's say, If that information isn't available, collector will have to follow particular guidelines, particular logic, to get the ID.
**Josh Suereth** 45:07 Yeah, this, this is the proposal here, if you wanted to see it. This is, for process context.
**Dmitrii Anoshin** 45:17 That's cool. Yeah. Can you please edit it to the… Josh Suereth 45:22 Yep.
**Dmitrii Anoshin** 45:23 to the doc, I should have, looked through the existing… Josh Suereth 45:27 No, that's fine. Honestly, though, I still think… I still think we have a problem after this, Dimitri, where, like, for Prometheus specifically, we need to… we need to basically say, look, when service instance ID exists, use it.
When it doesn't exist, here is how you construct a stable identifier that's exactly like Service instance ID that you can use.
**Dmitrii Anoshin** 45:48 Right.
**Josh Suereth** 45:49 So this is the idea of, like, if service instance ID doesn't exist.
And you need a stable ID to represent the target info. Take all of the identifying attributes of all the entities in the resource, and turn it into a UUID.
**Dmitrii Anoshin** 46:04 Done.
**Josh Suereth** 46:05 Like, I think we need to write that down somewhere, yeah.
**Dmitrii Anoshin** 46:07 Yes, that was my, idea. I think we should have, like, combination of all entity types and their identifiers.
entity type, but we shouldn't always assume that service as an entity must be present on all of the telemetry, that doesn't make sense.
**Josh Suereth** 46:25 Yeah, yeah, I agree, I agree. We're gonna… Dmitrii Anoshin 46:27 I can look into that, and also I'll, look into this app, and I guess once this ATAP is merged, this is pretty cool. We don't need separate entity services.
**Josh Suereth** 46:39 Yeah, I think… I'm kind of surprised. This one has been open for quite a while, and I think it has a lot of approvers from, like… these are all the profiling folks here, right?
But it only has 2 of, like, the TC approving so far, and none of the spec approvers. So, I think it probably still needs a little bit of, attention.
**Dmitrii Anoshin** 47:02 Okay.
**Josh Suereth** 47:03 Yeah.
**Dmitrii Anoshin** 47:04 But once it's done, I guess they follow up for me to completely close the loop, like, if Prometheus is kind of a bit separate, but from the collector perspective, we need to standardize the, like, mechanics behind, like, synthesizing that ID.
Because it's written in the spec that you should do it, but it doesn't prescribe you how you can do it. And we should actually be a bit more opinionated there, I guess.
**Josh Suereth** 47:37 Yeah, service.instead does not exist for me.
You have to use that ability.
Yep.
Cool.
**Dmitrii Anoshin** 47:48 Awesome, thank you.
**Josh Suereth** 47:51 Right, you met… I think you missed… we merged this spec PR that was related to updating, how things are described, so that's good. I want to do a quick follow-up on active PRs. I want to get back to our merge algorithm here. Dimitri, if you have a chance to review this one, I don't remember… So long, discussions are limitations with no complaints, right.
I don't think this has any open comments left, so it'd be good to get one more, approval. Dimitri, if you're willing to do that. I'll ping Tigrin then, and we'll see if we can get this merged. This is holding up the rest of the specification work for us to continue, so I'd like to try to get this through.
**Dmitrii Anoshin** 48:30 Sure. Sounds good. Thank you.
**Josh Suereth** 48:33 Are there any other active PRs? I think, Dimitri, you have… did yours get merged yet?
**Dmitrii Anoshin** 48:43 Actually, yeah, my PR and the collector got merged, so collector now can define entities in the metadata YAML, and entities will be emitted.
**So that's… that's… Josh Suereth** 48:54 That's awesome. Yep. Yeah, yeah.
And then… This is the one I was thinking of.
**Dmitrii Anoshin** 49:03 Oh, okay, not this one. This one is the specification, yeah.
**Josh Suereth** 49:07 Tigger and I both approved this. I just wanted to check and see if there's… if there's any… I didn't see any status updates since this.
Okay.
So, I think this is fine. I just… what I'm looking for is tomorrow in the spec meeting. I think maybe we dump them, both of our PRs, and say, hey, these are approved, these are ready, if anyone has complaints, we'd like to merge them soon.
**Dmitrii Anoshin** 49:28 Okay.
I… from my side about this PR, I've been thinking about, about the relationships between, infrastructure entities and, application entities, specifically service.
Given that they are many-to-many, and I need to probably add an example here, like, which specifically would be the… The owner of the relationships, and how they're gonna be emitted, maybe some, like, exam… practical, kind of.
Idea of how that's gonna be emitted.
**Josh Suereth** 50:06 Yeah, that'd be awesome if you can figure that out. This is where I was a bit nervous, because I think the only place we have that information today, and the only place I thought we planned to, was in resource, just by… fact of them being in the same resource. There's some relationship, we don't know what it is.
But it'd be cool if we could have some kind of explicit understanding of that relationship.
**Dmitrii Anoshin** 50:27 Crap.
**Josh Suereth** 50:28 And you might have to infer it from resource, yeah.
Okay.
I think that's it. Those are the only two PRs we have in the specification. Is there anything else active right now?
Alright, I'm gonna open the project board real quick, then.
Where are we here?
Okay.
we have… You're working on this, and that's making progress, that's making progress… We need to finish… I think next up is the actual SDK specification.
Right? I think that that's… this is the next to-do. Once those… once those two spec PRs are there. So, Yeah, I don't know.
Daniel, are you interested in taking a crack at the SDK specification for entities, or should I just take what we had in the OTEP and start writing that?
**Daniel Dyla (Dynatrace)** 51:41 Either way is fine with me. I'd probably just take what we have in the OTEP as well. You know, it's just… I have time if you don't.
**Josh Suereth** 51:52 I'm a bit swamped right now, and mostly that is… I didn't show it, but the stable by default crap.
**Daniel Dyla (Dynatrace)** 51:59 And this is not including the multi-entity stuff and the binding and all that, right? It's just the initial crack that we have already prototyped, and yeah, I'm happy to take that.
**Josh Suereth** 52:11 Yeah, yeah, this is where I want to start getting resource detectors, including entities, and the merge algorithm, and the ability for SDKs to emit them. Yep.
**Daniel Dyla (Dynatrace)** 52:20 Yep, works for me. Cool. And then I know I already said I would take the SDK startup specification, which I have started working on, but it's… that's part of it as well, so those are kind of… Josh Suereth 52:30 Yeah, that's why I mentioned it, because I think… I think doing both might be easier than doing just one.
**Daniel Dyla (Dynatrace)** 52:36 Yep, and then again, the async resource strategy thing, like, you know, I think we're happy with what we have, But… Josh Suereth 52:44 I would actually almost move this to done. You weren't here the last time we talked about this one. Like, I felt like we could move this to done, but, like, feel free to do that whenever you feel like we're good.
**Daniel Dyla (Dynatrace)** 52:56 Yeah, I would say develop a strategy, probably done, maybe we could document what the actual, strategy is in high level, and I'll close the issue today.
It may change as we get into details of specification, but I think the overall strategy is unlikely to change.
**Josh Suereth** 53:17 Yeah, that's… I'm totally in agreement. I think… I wasn't even looking at these, because A, I think the startup specification, you already had that mostly underway. This one, I feel like we have the strategy, we just need to write it down. This is still active. This one… This is about our Go implementation, and I think we're gonna work on this as we get through the spec. I'm not as worried about this as I was before.
Given some talks with other people, and… Yeah, this was all the collector work you're doing. So, next up is just, a demo of how collector processors differentiate remote versus local. Dimitri has that.
Community Breaking Change. This, I want to do… We've talked about this several times, just a reminder, we're not gonna execute on this until we have… like, an SDK that can actually produce things, and we're ready to start asking people to try it out.
But this is where we expect the, you know, resource to change.
The identity, and how entities will now be part of the identity, and that's technically a breaking change, even though we don't expect it to break people.
Okay.
And then finish that.
So, yeah, I think this might be too big, Daniel, this thing. This is, like, finish all the SDK specification. We can break it up, like, take whatever crack you want, and then when you're ready with that specification, let me know. I can update my Java prototype and turn it into a, ready-to-merge PR against the Java SDK.
Cool.
Alright, I think that's it for this week. Anyone else have any other topic they wanted to mention?
If not, thank you all. We'll see y'all next week.
Or actually, is next week KubeCon?
**Daniel Dyla (Dynatrace)** 55:15 Yeah, I think it is.
**Josh Suereth** 55:18 You can, yeah.
Should… we might cancel next week, then.
**Daniel Dyla (Dynatrace)** 55:22 I'm not going to KubeCon. Is anybody here going to KubeCon?
**Dmitrii Anoshin** 55:25 I'm going… Arve Knudsen 55:27 I'm going… Daniel Dyla (Dynatrace) 55:29 Yeah.
**Josh Suereth** 55:30 I'm not going, but I do need the break.
**Daniel Dyla (Dynatrace)** 55:33 It's, it's good to have a break. Yeah. It's, it's, spring, Christmas.
**Josh Suereth** 55:38 It's… During Christmas, should we get each other presents?
**Daniel Dyla (Dynatrace)** 55:44 Yeah, I'll get you an SDK specification for Spring Christmas.
**Josh Suereth** 55:48 Yeah, how about use the hour and write the specification? I'll use the hour to review it.
**Daniel Dyla (Dynatrace)** 55:52 Yeah, that sounds good.
**Josh Suereth** 55:52 I don't know if… Daniel Dyla (Dynatrace) 55:54 We can use the same hour to both write and review, but… Josh Suereth 55:58 Well… Yeah, we can shop it around. Anyway, I… Daniel Dyla (Dynatrace) 56:01 Happy canceling a week of meetings, that always feels good.
**Josh Suereth** 56:05 Okay, so let's… we'll cancel next week. So we'll see y'all in 2 weeks.
**Daniel Dyla (Dynatrace)** 56:09 Yep.
**Josh Suereth** 56:10 Alright, see ya.
