SIG: eBPF instrumentation
Date: 2025-11-26
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Mattia Meleleo** 00:42 Hello.
**Rafael Roquetto** 00:47 Hi there.
**Giuseppe Ognibene | Coralogix** 00:51 Everyone.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 00:53 Hey, folks.
**Tyler Yahn** 00:58 Hey.
**Giuseppe Ognibene | Coralogix** 01:02 Are you…
**Tyler Yahn** 01:03 How y'all doin'?
**Rafael Roquetto** 01:06 Good?
Getting started.
**Tyler Yahn** 01:09 Yeah.
**Rafael Roquetto** 01:10 How are you?
**Tyler Yahn** 01:12 Yeah, similar.
**Rafael Roquetto** 01:14 Busy?
**Tyler Yahn** 01:16 Yeah.
Rafael and Nicola, you guys don't have, Thanksgiving up there, right? You guys have to work the whole week?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:30 Yeah, yeah, our Thanksgiving is earlier.
**Rafael Roquetto** 01:32 Stop rubbing that in our faces.
**Tyler Yahn** 01:38 I was like, I thought you guys had a Thanksgiving, but I couldn't remember when it was, but yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:43 I pretty much think that all Canadians are actually on call.
With respect that. It's, like, the worst week to be on call, because…
**Tyler Yahn** 01:53 Yeah, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:54 We're in the same time zone, and there's, like, Black Friday and all this stuff, and…
**Tyler Yahn** 01:58 Oh, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 01:59 They're all off, and so, yeah.
**Tyler Yahn** 02:02 Ugh, Black Friday is… that one's killer, to be on call for, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:06 Yeah.
**Tyler Yahn** 02:09 Well, cool, we can probably jump in here in just a second. Looking, we got a lot of people on the call. If you haven't yet, please go ahead and add your name to the attendees list, and if you have agenda items you want to talk about, go ahead and add those there as well, and yeah, we'll jump in.
Alright, so to start us off, Nikola, you wanted to talk about ideas for HTTP2 gRPC context propagation?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 02:40 Yeah, so I was thinking, that's one of the protocols we currently sort of ignore for, any context propagation, because,
All the internal data structures that we have keys on.
key on exactly just the connection information, so… But gRPC and HTTP2 multiplex, multiple…
Connections through the same,
Multiple requests in the same connection, so…
the idea was to extend that data structure to have a stream ID, or an extra ID that
That would allow us to do this, so we would…
Be able to kind of capture that.
But that's the easiest part. I started thinking more around…
proposed the idea of doing it, but, with a small wrinkle, and I just wanted to hear your opinion of what people think.
essentially, gRPC is a binary protocol, and the way that… I mean, I'm not sure how many people know, but I'll just assume they don't know, and correct me if I'm saying something wrong, but essentially, when the protocol starts.
The client and the server exchange information only about how big the dynamic table.
will be. So that's the only kind of information to exchange, and say, we agree both to use 1,000 settings, thousand entries on the dynamic table for key values, or just keys alone.
So later on, what they do is,
the client sends a value, such as maybe, I don't know, transparent with certain value.
Let's just say, on one side.
And then the receiver sees that value and says, okay, trace parent is a new key. I haven't seen this one yet.
So, I'm gonna add an index for it, and remember it in my dynamic table as index 58, let's just say. Pick a number, whatever the next available index is.
At the same time, the client also does that. When the first time it sends TraceParent, figures out that's a new key, I'm gonna add it as 58.
Because both of them actually, per connection, have the same dynamic table size. They don't have to exchange any more information about future, what this 58 is. Both added synchronously at the client and at the service side.
So technically, what happens is that next time trace parent gets pushed through the wire.
It's just measured as 58.
It's never actually sent as a trace parent.
Text.
A header value.
So the binary protocol optimizes this, so initially they exchange this information, after that it's just numbers.
The value of the trace parent, the 00 dash whatever numbers, that thing is always going to be text, because it's so…
random that… Dynamic table will never actually store that key-value pair, because it doesn't repeat.
So smart that way. So the value will be there.
So now, the question that I have is this.
we could… and the eBPF side decode these packets, and we already do that, and we can extract the trace parents. Let's say,
Java SDK sends a packet with trace parent encoded.
And Obi intercepts the packet, extracts this information, and we're able to kind of achieve context propagation.
The problem is… I do not know the index of the key called trace parent.
That index will be per connection.
One application could have 50A, the other one could have… 78… whatever it is.
So, the only way to kind of extract the header value is to bet that the format of…
W3C, key, the way it looks, the trace variant value is, like, 00 dash, this number of digits, dash.
would mean that's a guarantee to be transparent. So we have to kind of, like, bet on nobody else using this for any other purpose.
In order to, kind of, get the information.
I don't know if I'm explaining it well. Maybe I need a sort of diagram.
**Rafael Roquetto** 07:17 Sorry, go ahead, Tyler.
**Tyler Yahn** 07:21 I was gonna say, I think you're explaining it well,
Like, it's just a hard problem, so there's a lot of thinking.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:27 Yeah.
**Tyler Yahn** 07:29 Yeah, go ahead, Raphael.
**Rafael Roquetto** 07:31 I was gonna ask…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 07:32 Yeah, no way to… no way to know for guarantee if the trace parent wasn't mentioned as a…
head or vouch key. There's no way to know for sure that
This is going to be for the purpose of TracePan, so we might be ingesting something
That people are using for a different purpose, I don't know.
that will look like W3C.
Transparent.
**Rafael Roquetto** 08:01 So, just so I understand, this would be the case where you have a known gRPC service.
Having a server call?
And then the gRPC service puts a client calling needs to encode that trace parent somehow, so that incoming service does not have, like, a stream ID, because it's not gRPC, for instance. Would that make sense?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:29 No, so essentially, the Java service, let's say, it's not instrumented with OB,
And it's just instrumented with a Java SDK, a Java agent, whatever. It uses gRPC, and it's talking to a Go service.
**Rafael Roquetto** 08:41 Okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 08:42 Actually, Go is easy, because Go, we parse the headers. That's fine. So ignore Go.
We… let's say it's talking to a Node.js service that's instrumented with OBI.
Now, with the JavaService 1 code will be some random number, 123, and then the value of the trace parent.
Now, we don't know what 123 is.
Because if we didn't catch the services talking to each other.
before they encoded that 123 on both sides as being the trace parent key.
We have no idea what that 123 is.
Now, we know it's a header key, but we don't know what that header key is. Like, if it's not a…
If Hobby didn't intercept that and cache the dynamic table exchange, Danny will never know.
So the question is, how do we…
parse this in general, and one approach that I thought of was to
So ignore the key value, but just look at the… ignore the key, look at the value, and if the value looks like our transparent in that format, then…
Assume that's the trace path.
We can't know for sure.
And we can be smarter, we can say if there's two values that look the same, they just won't do it, but if there's only one, then…
Let's just do it.
Or something like that.
**Rafael Roquetto** 10:04 We'll see.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:06 there's potential side effects and dangers to that. One potential is that, let's just say they use that value for
Everything and anything, and it's constant.
So what we'll actually end up doing
will end up making all transactions have the same… all transactions have the same transaction ID.
Which is not great.
Like, somebody just encodes in that W3C format something else that just looks in that format.
It's sort of very… that could be… Unexpected side effects.
That's weird.
**Tyler Yahn** 10:40 Yeah, but I mean, like, what's the probability of that? Like, it seems small.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:43 Yeah, it's pretty low. And maybe we can add guardrails against it. Like, we say, oh, this value repeated, or something, since last time, or it's too similar to previous, and we just say, forget it.
**Tyler Yahn** 10:54 Yeah, that means you gotta hold state, though, right? And that starts to be a problem.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 10:58 Yeah, yeah.
But maybe the user space…
could do something along those lines. We're processing.
**Tyler Yahn** 11:05 Oh.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:05 space, we can keep a cache of… and so, oh, trace band keeps repeating.
For different things, and just, like…
Well, we can say, okay, that doesn't look good.
Something like that, I don't know, I'm just making stuff up, but…
**Tyler Yahn** 11:22 The thing is, is though that, like, this project,
it kind of already works on these sort of, like, pattern matching heuristics, right? And it's gotten us pretty far.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 11:32 Oh, absolutely, yeah. It's gotten us really far, actually.
**Tyler Yahn** 11:35 So this seems like… it seems like something to pursue, is my take on this. Like, I think it's… I think it's worth…
Trying this, I think that there may be more complex ways to try to parse this out,
That would be way more involved, I think. But…
If this gets us 90% of the way there, or even 99% of the way there.
And it doesn't really seem like it's worth…
Like, exploring all these other options right off the start, at least.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:08 Yeah, I agree. I mean, it's… we know a couple things. We know it's gRPC, so we know they're exchanging this communication. They're not just making stuff up, you know? We know they started this protocol, we know it looks like the W3C…
Aaron?
I'm not sure, maybe there's a… if Obi can see that service, maybe even though it's instrumented with Java, we can maybe even tell that it's exporting OTEL, and it's OTEL-enabled, and we can… if this becomes a problem, I think there's ways to kind of…
Do more validation.
Bye.
Yeah, that was my gut feel, that there's, like, this edge cases that I'm thinking of will…
be very unlikely, but I just wanted to bring it up before I started working on something like this.
**Tyler Yahn** 12:52 So this, again, is only gonna work on the ingest side, though, right? Like, we still aren't gonna be able to create a trace parent and, like, send it?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 12:59 We would, like, that's the… but the initial step is, like, grabbing it from there. Oh, okay. You know, like, and then, if we can parse it on incoming.
Which is great, that means we can ingest a transparent supply to us from an auto instrumented service.
than…
then I would extend the data structures internally to keep track of the stream ID as well, as the connections, so then kind of split them off for gRPC, so we can track more than one at a time.
And, yeah, the rest of the logic should just work.
**Tyler Yahn** 13:33 And so, when you have the stream ID with them, are you also gonna track this, like, transparent header ID as well, or are you just gonna just assume… Oh, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 13:41 Yeah, everything is just… internally, all the tracking is right now based purely on the connection information, which is not suitable for gRPC or HTTP2.
So… But I will extend that, make the key, have one extra field, which is this stream ID,
Or whatever I'm gonna call it. And this will be zero for any other protocol, so it will be unused, there will never be duplication.
And then…
For gRPC, we'll start populating it, and then we'll be able to discern which gRPC request did what.
And then we can start injecting it, spacing the packets, and we'll be able to do everything.
Because…
We see the full gRPC packet when we are injecting the headers, so we'll do the spacing using the same approach as the way we spaced for HTTP.
**Tyler Yahn** 14:34 Okay. And then the value will be written as text, because that value…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 14:38 GRPC supports it, it's suboptimal, but it does support it. And then…
we would just encode the change in the length of the packet inside the gRPC protocol. It's doable.
This is how it happens to forego.
Confix propagation on unlocked kernels.
Right. This will give us support to do gRPC for both Go and other languages for log kernels.
They'll be pretty cool.
**Tyler Yahn** 15:09 Yeah, I mean, I think it's worth doing. I don't see there's… I don't, like…
The risk versus reward is definitely leaning in the direction of, like, we should try this and add it, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:19 Yeah.
I mean, OB to OB will be fine, but OB2 SDKs is what I'm looking for, to make sure that… that it works. That was the last, sort of…
blocker.
**Tyler Yahn** 15:29 OB to SDK is not…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:30 As the case to OB. As the case for OB.
**Tyler Yahn** 15:32 Oh, okay, yeah, yeah, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 15:33 It's working with the rest of the ecosystem.
Alright, cool. Yeah, that's… that's positive. That was my gut feel, too, that it shouldn't be too big of a…
deal, I mean, I haven't seen anybody else use these headers right of purpose, but…
If they start doing it, we'll cross that bridge, I guess.
**Tyler Yahn** 15:51 Yeah, I mean, like, the only other thing…
that I can think is, like, they're trying to send links inappropriately via some header, which would be, like, extremely rare. Like, well, it'd be wrong, but it'd also be, like, rare, and so…
Yeah, it'd be very odd to me that you would see something that would match the same format, being sent in a header value, or it was just a gRPC-like, field pile, yeah.
Cool. So, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:15 Alright, sounds good.
**Tyler Yahn** 16:17 Cool.
Alright, well, sticking with you, Nicola, you still want to talk about a proposal to extend the OTEL demo with non-instrumented applications that we can use OB hotel operator in the go-out interpretation on?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 16:28 Yeah, I just wanted to bring it to this group as well. When I came up with this idea, I wrote it yesterday on the Go AutoSig, but I'm just bringing it here as well.
I would like us to be able to show off all these technologies that we have in the OTEL demo. So, technically, what we want to do is write some uninstrumented applications, and then
add the operator, OB, GO Auto instrumentation, and perhaps even the OTL injector, as Tyler suggested yesterday, and the GO SIG.
That would use this tunnel.
Autosermentation techniques that are… require zero effort.
So…
This would be on us, or this group, and the group from Go Auto, that we would have to do this work. My understanding is that there's not going to be any help from the hotel demo folks, but I think we're more than capable of writing a couple of services, adding them.
into the hotel demo to do random stuff.
Just sprinkling in various types of instrumentations.
So, people know this is part of the ecosystem, you know? Just to get more exposure.
For all the work we're doing here.
**Nimrod Avni** 17:42 Yeah, I can say we, already did…
We kind of removed the instrumentation from a lot of the existing services, just to, you know, make sure that… so maybe we can also have…
some, like, configuration in the Helm chart of, like, do you want this instrumented or not? And by that, I don't know if you want to, like, change the imports, or the Dockerfile, or whatever. And also we added a couple of, like, connection with different types of technologies, databases…
prepared statements for SQL, stuff like that, so we can show the full demo. Maybe we can…
Maybe we can try to donate some of the stuff we had. It's not like… we're gonna just add it to a bunch of already existing services, there's not real, like, logic of, like, you know, the product card, whatever, we're just adding random stuff to the databases.
I don't know, maybe we can also donate that, or… I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 18:40 Yeah, that would be great, like, especially if you have some head start. We're doing the same thing, we're just ripping out instrumentations from the hotel demo, but I know that… I don't know if that's gonna go well, they're like, you're undoing our work here, we did all this hard work, and…
so on, but I…
I'm sure, like, I can go ask ChatGPT to give a suggestion what other microservices might exist in our…
online, like…
**Nimrod Avni** 19:03 Yeah, we just did it as well, it's like, you know, like, a mindless code that just talks to random technology.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:09 Which is… yeah, I'll just add… stuff, or a truck.
**Nimrod Avni** 19:12 Add Mongo.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:13 I don't know, like, engagement, customer engagement. We can create a call section just by…
Figuring out, doing some analytics, or who knows, something, I don't know.
I'm sure we'll come up with.
parts of, An online catalog.
**Nimrod Avni** 19:31 Yeah, that's cool, and yeah, and also worth including some of the other, technologies that we support, I think it can be…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:38 Yeah, I'm all gone.
**Nimrod Avni** 19:39 Good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:40 Yeah.
I just saw that the hotel demo has added LLM workloads. I think we're not the only ones thinking about this. Apparently, now there's an LLM
block in the picture, so people are showing AI instrumentation
With hotel as well, so…
**Nimrod Avni** 19:55 I think it's not gonna be an unusual request, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 19:59 Zero-code instrumentation efforts.
**Nimrod Avni** 20:05 Sounds good.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 20:07 Awesome. Okay.
Yeah, we decided that we're gonna spearhead that effort and try… try to bring it up forward. I'll… I'll see when the next SIG meeting is, maybe I'll show up and make a proposal, ask them how… how do we get started?
And then I'll bring you back some information on this.
**Tyler Yahn** 20:24 Yeah, that sounds good. I don't know if they meet every week, but yeah, I think it… I think if, yeah, we get something on their books, just to… to talk with them about it, that sounds good.
Okay, moving on, Mattia, you wanted to talk next about, RFC for trace log correlation?
**Mattia Meleleo** 20:41 Yeah, I wanted to… to expose my idea and gather maybe some early feedbacks and stuff like that.
So I will start with a little demo, and then I will explain why I did it like that, and…
Yeah.
I forget that.
Let me share…
Can you see my screen?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 21:09 Yep.
Yeah, that's good.
**Mattia Meleleo** 21:13 Okay, so… okay, let's do the demo first. So, I have a service here.
which, which opens three servers, Python, and does one request from one service to another.
This is the config.
Which… Which is not used at the moment, because everything is hard-coded.
So if I trigger… wait, I need to start mine.
Wait, let me show… let me show you first how it works without the… TraceLog thing.
So here, there is nothing, and… If I start hobby…
I have the Tresady and the Spanish D now here.
And, they are the same as the… Spence over here.
So, how I did this is, by hooking the TTY right.
And, well, don't, don't look at this, this is just hard-coded once I wire up the…
The map for valid pits, this shouldn't be here.
I did some filtering…
So… Here is, where I get the trace… trace ID and span ID.
So I used these two functions.
I don't know if they are correct, but, in the basic, basic case, they should work.
And then I send the… I copied the buffer.
And I send it to user space in,
In an event that I will show you soon.
And then, I…
I write zeros in the kernel buffer, so the target process will not be able to write anything to the terminal. So from here on, the responsibility of writing the log is fully on Hobby.
student… I lost it.
Oh, here's the event. So, in the event, I have the trace, trace information.
the PID, the length of the log, and the…
The parts of the device, where the function is writing to.
And in user space, I have this function here that parses the event.
And, and rise to the…
to the terminal, to the target terminal. Here is hard-coded as JSON.
But…
But I have in mind to… to let the user specify the format of the logs per service, and
In case it's not known, to infer it from the first logline.
So, I have two questions after this. First one is,
Well, do you think it's a good idea? Do you foresee any problems with this approach?
And the other one is,
Yeah, I need the… so, basically, I need to enable this per service, and what I did in the config was to… to have this other field, which is…
A list of the destruct, which contains a globe definition criteria.
So, basically, I need to create a subset of this one and the services in the discovery.
And they're not… I'm not sure what's the cleanest way to do that.
Yeah, this is just a technical question, but the main question is, do you like the idea? Do you see any problems with it?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 25:45 No, this is epic, this is great. I like it.
**Marc** 25:47 Can you show… can you show what is he doing again? Because.
**Mattia Meleleo** 25:52 In… where? In the code, or…
**Marc** 25:54 No, no, the terminal, like, what it's producing.
**Mattia Meleleo** 25:59 Yeah, yeah, yeah. So…
So this is the logs of the target service, of the booked service, without obby running, and it's just printing,
a log line?
And, then… after I start Obi, Obi is injecting the,
The new keys in the… in the log.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 26:22 Yeah, it's great.
I was just gonna say one thing, I, I thought about this as well, and…
I think I've… once I've even thought about writing the code, but I…
I've heard, sort of like,
Somebody discouraged me, but I shouldn't have actually been discouraged. The reason is because somebody told me about the Log4J, how it, like, pushes on buffers, and it will not work for everything. But I think Log4J is sort of, like, special. Most of these simpler programming languages just write straight up.
They don't create this sort of, like, back-end writer thread that… Right, yeah. So,
This is pretty cool, I… I just gotta ask one thing, and
I think we should maybe have a version without the BPF Pro right user, because, you know, that one is, like.
Locked, and it will not be available on many
kernels, especially, like, the cloud vendors with GKE and
Maybe not GK, but Amazon, all new kernels are locked.
So you won't be able to change the contents of the buffer.
However, Maybe that's not the end of the world?
Because… These buffers that you have?
could just simply be an OTLP logs.
And… it's up to the user to not actually scrape logs from TTY, or…
and simply just use OB's built-in functionality to ship logs.
**Mattia Meleleo** 28:00 The problem with that is that,
If we don't zero out the buffer that the process is writing, we will have double output, basically. Because the target process is writing.
And Obi is also writing.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:16 That's what I'm saying, don't have Obi write it. Just have Obi collect this event, and then just use the OTLP logs
Rather than… like we do for traces and metrics, and ship it directly to the auto collector.
**Mattia Meleleo** 28:31 Oh, so basically, I act as a log shipper.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 28:33 Yeah, and then we just tell users not to scrape the logs from the service, because that one doesn't have trace IDs, but just have it all be generated for you, so then…
It's sort of like…
They don't have to parse and collect logs from pods and do all this work, but we're shipping them directly, so…
And that way, you can do what you did, I don't think… but in the case where there's no ProBride user capability.
Then we can take this approach.
**Mattia Meleleo** 29:07 We thought a little bit about this,
But the issue, I think there is an… I think there is an issue with that, and it's that Obi's taking too much responsibility for shipping all the logs.
At this point.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 29:24 Yeah.
Yeah, it would be, like, instead of every service shipping its own logs, you just have OB. Yeah? I mean, it is a… it is gonna be a challenge.
Bye.
**Nimrod Avni** 29:37 We've talked about it a bit, like, either,
especially if you want to not do it on, like, older services, because, I don't know, you have some services that are either already instrumented, or whatever, so you want to, like, you know, take all these specific services.
I thought maybe another solution that was suggested is, like, taking only error logs and duplicating them, and, like, in that case, you can say it's worth enough to have both scrape it and, like, have another log that's enriched.
I don't know, it's just, like, a lot of different strategies, and everyone has, like, every one of them has some pros and cons.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:16 Yeah, exactly, or…
just have the ability to pipe, through a configuration, the OB logs into a different file, and then teach your scraper for logs that you should be picking up from here, if you don't want to ship them through OTLP.
to the collector.
So that people can just pick and choose what they want. It could be a configuration thing, right?
**Mattia Meleleo** 30:41 You know, it's.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 30:43 Yeah, absolutely.
**Mattia Meleleo** 30:44 Because once we have the probe, we can decide via configuration what's the behavior. So for this service, I can get the logs and ship them.
And for this other service, I can, overdrive them.
I don't know what's the benefit of the mixed approach, though, but .
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:04 Yeah, if you have both right user, go ahead and do it, I would say. It could be an.
**Mattia Meleleo** 31:09 Yeah, Tom.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 31:10 Yeah. But if you don't have ProWrite User, and which is gonna be more and more kernels going forward.
But…
**Rafael Roquetto** 31:23 Yeah, I just wanted to say, I thought we were moving away from ProWrite User, altogether.
So, my personal opinion would be if…
I wouldn't go for a mixed approach, because…
You have an approach that… from the user's standpoint.
I mean, maybe probe right user would be a bit better, because you end up with… the user ends up with their original logs just enriched, which is awesome.
But if it breaks most of the time, because the kernel is not gonna load.
then I… I don't know, this is a conjuncture, but I imagine that this can generate a lot of chatter from users, like, okay, it's not working, it's not working. Then you gotta go and tell them, hey, yeah, because your kernel doesn't support it, so you need to use this other approach that we're gonna have to do anyway.
Which is, well, maybe what Nikola or Nimrod were proposing, like a… well, the alternative approach. And then that kind of generates two tiers of approaches for, you know, I'm not sure…
Given that probe right users locked down, and it's pretty much unusable in a lot of kernels.
maybe… I mean, personally, I would argue that we should just go for the alternative approach and not use ProBride User at all, and this is how it's done.
for.
**Mattia Meleleo** 32:47 we…
**Rafael Roquetto** 32:47 documented, yeah?
**Mattia Meleleo** 32:50 Do we know which kernels are actually currently blocking it?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 32:55 I mean, it's up to the, provider of… A service like,
It used to be a very small percentage until AWS started
by default, turning it on for their, managed Kubernetes.
I don't know if Google has done the same thing.
**Mattia Meleleo** 33:15 But, maybe, maybe they are doing this only on both the Rocket and not on Amazon Linux.
Not sure.
**Tyler Yahn** 33:24 Yeah, I think, to everyone else's point, though, like, whether, like, the service providers are doing it or not, most people aren't comfortable running, with, like, the elevator permissions to actually write with VPF Pro for a user. So, like, I think, like, having the solution not use that is probably the ideal…
Approach.
**Rafael Roquetto** 33:46 Ubuntu, for instance, 2204 in Azure. Yeah, there is an issue on OpenTelemetry Go. I gotta, like, to… if you… if you Google for VPF, ProBrite User Lockdown, you're gonna find a lot of, like, posts of people
either replacing or restricting
the ProBrite user, usage. So this is why, for instance, we moved away from it for trace context propagation injection, in the header and used this, soft message program.
which has the downside of cgroups.
Because we run into trouble. So, in the past, we run into trouble with this, and I expect that we're gonna happen the same if we use there. So, yeah.
Just wanna mention it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 34:37 Yeah, I mean, it's okay, like…
In my opinion, maybe from a pragmatic standpoint, it's like, it's okay to have the option to do it, but maybe not make the default, and if you want to use it…
separately, and people say, I don't want this duplication, whatever, and you're on this kernel, then you can just say, yeah, sure, nuke my law.
With my lines with that.
I don't know.
**Mattia Meleleo** 34:59 Another idea I had was to have a LSM hook.
But I don't know if there is the cook for TTY Wright, or for Wright in general.
should look into that, because if there is a hook for the LSM,
We can just, block the syscall, the, yeah, the syscall, and, get the, get the data, block the syscall, and write ourselves to the target, without using VPF probe, right user.
But I need to do some research into that.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:32 Okay, yeah, that's… that's possible. Would you think it will work in any case? Would an application freak out if it wasn't able to write? Like, get an exception on…
**Mattia Meleleo** 35:41 With an application, or what?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 35:44 like, my Python application is not expecting that the call to log will fail, you know, and they get an exception back or something, I don't know.
Like, if we can silently eat it, and just say, yeah, it happened, but didn't…
That would be better, but…
**Mattia Meleleo** 36:01 We have to try, but I think.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:03 Yeah.
**Mattia Meleleo** 36:03 And we will, yeah.
**Nimrod Avni** 36:05 The only thing, I'm also… something I might be afraid of is, like…
If for some reason Obie can't read fast enough, we'll, like, lose customer logs.
But maybe we can, like…
If we have, like, some ring buffer, and we try to push to it, and we, like, we, we're failing because the buffer is full, we can just write the normal log without the context pop… without the trace context, and we'.
**Mattia Meleleo** 36:32 Yeah, yeah, yeah.
**Nimrod Avni** 36:33 Engagement is, like, best effort of, like, how much we can process.
**Mattia Meleleo** 36:37 Yeah, basically, I wrote in the code, there is one line from which the responsibility falls on us, and for every failure, from there, we should write the fallback log, fallback buffer.
Yeah, that's… that's acceptable.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 36:53 Yeah.
**Tyler Yahn** 36:54 So, one of the other questions I had was, like, this is, this is…
intercepting a TTY, right? But, like, most people write to a file Not a TTY.
**Nimrod Avni** 37:09 I think it depends… Right.
I think most of, like, Kubernetes…
customer, like, write to, like, STD out, and then have some, like, you know, the scraper, or, like, the file log, receiver, just reads from Docker logs and ships it to, to the vendor's logs.
Maybe we can also… as for, like, file, writing logs to files, it's kind of harder, because we don't know which file they're writing to.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:37 Yeah.
**Nimrod Avni** 37:38 Maybe we can have some strategy of, like, I don't know, if we see, like, a .log, whatever, file that is being written to, we can assume that it's that, but I don't know.
**Rafael Roquetto** 37:47 What happens if you, on your demo, you redirect the output to a file? Does it still work?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 37:54 Yeah.
**Tyler Yahn** 37:55 Yeah, that should work, yeah.
**Rafael Roquetto** 37:56 Okay.
**Mattia Meleleo** 37:57 Not sure. If you redirected the output of the service.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:01 to a file. Yeah, to a file.
**Tyler Yahn** 38:03 Yeah, because it's still riding through the TTY to a pipe, right? And that pipe is gonna…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 38:08 The pipe is going to fall.
**Mattia Meleleo** 38:09 Yeah. Basically, the TTY… no, no, I mean, the SCD out is, just,
link to a DebPTS file, and I write to this Dep.PTS file directly.
That's the file that is pointed by the file in the kernel.
**Tyler Yahn** 38:29 No, sure, yeah, TTYs are files, it's just that the question is, like, a lot of services that, like, people are gonna be running are just gonna write to files directly, though, and not go through a TTY.
**Nimrod Avni** 38:39 Maybe we can also… Like…
if that's, like, something configurable, we can, like, let them set some, like, regex or something of, like, you know… I know…
this, like, list of matchers, of, like, you know, services and whatever, write to log files that look like, I don't know, star.logs or whatever, and then, like, we can have a hook on, like, FileWrite and match that, and then treat it as logs, I don't know.
That's, like, like another, you know, feature on top of…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 39:10 Yeah, that's gonna be a lot harder, though.
Because by the time you write, you probably just have file descriptor, and then you have to read the threads…
file the script or table list, or whatever, to find the file, and then from there, find the path, and…
It's, like… It's doable, but it requires caching, and sending
We have to be careful where to set the kernel probe, because if you set it on any right, that's just gonna trigger on sockets and everything, and…
It's gonna be massive amounts of…
**Mattia Meleleo** 39:41 It's gonna be very hard to filter on what you want.
**Stephen Lang** 39:46 There's another option.
**Nimrod Avni** 39:48 The logs in Kubernetes are also available through the Kubernetes API server.
**Stephen Lang** 39:53 So you could intercept the network traffic.
When the logs are being shipped to the API server as well.
So there's two ways to gather logs in Kubernetes. Either you can use a host path volume mount and scrape the logs on disk from Docket on the node.
But the other way is to… which is… requires less privilege… privileges.
But it puts more load on the API server, and it increases network traffic.
is to, query the API server. So at some point, presumably.
Those logs have to be shipped to the API server in order for them to be readable in the first place, unless it's, like, an on-demand thing.
But, you know, maybe you could use… that's, you know, that would just be pure network traffic.
In that case, sounds another way to look at it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:43 extender. We can't.
**Rafael Roquetto** 40:45 Yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 40:45 to write it, but then you would have to packet extend in multiple places. Maybe if it's sending in batches, then we would have to go find where to…
It's probably not going to be line by line at that time.
**Stephen Lang** 41:01 But the log files on disk should be predictably named based on the pod and container IDs. So that's.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:08 Hmm.
**Stephen Lang** 41:09 That's the other thing.
But the, the path.
It's…
Could be a few different paths, depending on whether… what your system is, whether it's OpenShift or what distribution of K8s.
**Mattia Meleleo** 41:23 I'll look into this. Very interesting.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 41:26 But it's a good spot.
**Tyler Yahn** 41:27 Mattia, yeah, first off, yeah, great start. Thanks for… thanks for jumping into this. What is, like, the main goal is to try to catch, like, Kubernetes op… like, logs and applications that are running in Kubernetes is kind of the goal here, right?
**Mattia Meleleo** 41:40 Mainly, yes. Ideally, it would work for every kind of log.
**Tyler Yahn** 41:46 Yeah.
**Nimrod Avni** 41:47 Comment is, like, the main,
I know, at least, like, the main,
situation that most of our, like, customers use, so for a lot of users, it's in Kubernetes.
And we can, like, once this feature is live, we can extend it to, like, file loggers and other types of loggers, other types of formats.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:09 So one thing that we need to do is probably figure out how we're gonna do this for Go.
Because Go… We'll all work.
**Nimrod Avni** 42:17 proteins.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 42:18 Yeah, because it has goroutines, so we probably need to add probes into… the go-libraries, like Slog, or…
Whatever else people use, and then try to intercept it there.
**Nimrod Avni** 42:33 But don't we, I think…
I thought, like, if we have some way to correlate, like, something similar we do to… Let's see…
Node.js that we kinda… Save the correlation…
Yeah, we could. You can get it from the PID, we can be based on, like, the…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:02 I see what you're saying. Okay, that will work.
**Nimrod Avni** 43:05 Karen Peed is this goal team, I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:08 Yeah, okay, I like that, I like that. Okay, that's much easier.
That's a good suggestion.
So what we would do is, you're saying the Go instrumentation would populate the current Go routine to thread mapping.
it must be synchronous, because it's just writing to TTY, and then…
At that time, when the ride starts, we kind of reverse…
the thread to go routine, and from Go routine, we pick up the transparency.
**Mattia Meleleo** 43:36 Yep.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 43:37 And then… Slight hurdle there, which we just kind of have to… Mess with,
We just have to mess with, pit filtering, because right now, Go…
processes don't get into the main pit filter, because we don't want them
because they're all done through U-probes, all instrumentations, we don't want them to go through the same PID filter, because then we'll see signals from Go applications going through the K probes, which we don't want.
Because there… all the instrumentation there is done through UPROBS.
But we could have a special pit filter for the logs.
Which you're already alluding to, you're saying you want a separate glob… sorry, glob section, so you can have a separate pit filter that's specially for logging.
And then that one can include Go applications, and we'll do this…
Double reversal, so thread to go routine, go routine to… transparent.
**Nimrod Avni** 44:31 I think it still needs to be a subset of the, like, normal, globe, like, discovery config. So you have, like, a discovery config, and after that you have, like, a log correlation config, but that one will be, like, including Go.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 44:50 That makes sense. Cool. That's a good idea.
**Tyler Yahn** 44:54 I think we also want to maybe talk about, like, the formats that we support. I would be hesitant to try to support, like, a plain text format. I think structured logs are going to kind of be a requirement here.
But, you know, because otherwise we're just going to be adding…
potentially garbage to just, like, plain logs, but, like, I think if they're structured, like, you're dealing with, like, JSON or YAML or something like that, I think it would have a way better chance of actually, like, adding to the logs and not, like, munging things in a way that are, you know…
I think you get into a lot of issues, especially when you have plane logs where you're…
especially if you're passing it through some sort of TTY and you're doing some sort of downstream log parsing that isn't going through, like, OTEL, that you have some complex, like, log parsing operations already to try to, like.
turn those into structured logs, and so if you start adding things, I think, in random places, it might… it might have a lot of complications at that point.
But I think…
**Stephen Lang** 45:48 There's also a tile of redaction and, you know, PII stuff, which, if you've got those kind of processes, this could potentially bypass it.
**Tyler Yahn** 45:56 Right, right, yeah.
Yeah, so I think… I think your approach of starting with JSON might be a good idea here, is what I'm saying, Mattia.
**Mattia Meleleo** 46:06 Okay.
**Tyler Yahn** 46:07 Yeah.
**Nimrod Avni** 46:08 I think also another, consideration of just, adding… being, like, a log shipper, as we said, that instead of using BPA Pro Bright, is a lot of… if you look, like, at the file log receiver, it has a lot of different options of…
Kind of, like, formatting, parsing, like, handing multi-line logs, and…
like, implementing all that in Obi seems a lot, unless we can… maybe we can import the collector, like, I don't know.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 46:36 Okay, I get, I get… I think it's… it's totally fair, yeah, I think you're right.
**Nimrod Avni** 46:40 No, maybe as, like, a first…
you know, like, we need to think maybe of, like, the… as you said, the multi-option stuff that you said. I get the… that, like, doing it with VPF ProBrite, and then saying, if you want to do it the other way, you need to do it, like, you know, with some other config, but that might also have some downsides of, like…
You need to be a real, like, log shipper and log parser instead of, you know, just,
manipulate the output, and then let Autel Collector handle the… the FDD.
**Rafael Roquetto** 47:18 So what's the…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:18 Some customers will, like, will be okay with duplicates, in my opinion. Like, who can't write probe right user, just give them the option that they'll get the duplicate, and…
I am.
And then you can filter anything that doesn't start with a curly brace.
Using the rules.
**Nimrod Avni** 47:33 Maybe we can also let them, yeah, just, like, only errors, I don't know, like, if, like, we know the error field in the JSON.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 47:41 Yeah, yeah.
**Rafael Roquetto** 47:42 So, if we are… sorry, because I don't know a lot about this part of shipping logs, so maybe it's a stupid question.
But… If… if we were, let's say, ingesting the logs, enriching the logs, separately.
And if we use structured logs, like Tyler said.
Why is it a problem to parse these logs, and then enrich them, and…
write them? It's not a rhetorical question, I really don't know.
**Nimrod Avni** 48:13 you mean if we do… because we're getting, like, basically… it is… it is structure logs, like, we're getting JSONs.
I just remember seeing, maybe we need to, like, check exactly, like, the file log receipt, because I think it still does some processing, even unstructured logs, and not just plain text ones, before, like, handing it over to, like, the next parts of, like, processor and exporter and all that stuff.
I can find some examples. I don't know, like, exactly what it does, but…
might need some more research there to see if it's something that's, like, okay, it's easy, or is it, like, something that's really complex to do in Obi?
**Rafael Roquetto** 49:00 Okay.
Thanks.
**Tyler Yahn** 49:07 So, Mattia, maybe just, to kind of wrap this up, like, next steps, is, is, the idea, maybe you wanna…
Submit, like, your code as, like, a draft or something, so people can take a look at it or play with it, or… is it an issue that you can maybe create just to track the work on this?
**Mattia Meleleo** 49:24 I will open a draft PR maybe tomorrow, so we can, we can have some written comments and feedback over there.
One thing I wanted to ask is I have some copy-pasted code from a GPL repository.
Is that, allowed to do? Because I saw that, Obi's, Apache licensed.
But the BPF code is a gray area, it should be GPL licensed, right?
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 49:56 Yeah, if it's BPF, it's fine. If it's not BPF, then I think we…
**Mattia Meleleo** 50:00 It's BPF, yeah.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:01 We have to rewrite the code.
**Mattia Meleleo** 50:04 It's just a function, I could rewrite it.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:07 If it's not that hard to rewrite, just rewrite it. Possibly easiest thing, but I think all BPF code must be double licensed, MIT and
Gpl.
**Mattia Meleleo** 50:18 Educated, okay.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 50:19 So, even our stuff is licensed.
Both.
**Tyler Yahn** 50:23 Yeah, I would say that if you are gonna copy,
I think if you've already looked at the code, I think this ship might have already sailed, to be honest. This is a recorded call at this point. So, I would maybe just say.
**Mattia Meleleo** 50:37 I wrote part of that code, so…
**Tyler Yahn** 50:40 Yeah, that's fine, it's just, like, the GPL license is permissive, or I'm sorry, not permissive, the opposite of permissive, meaning that, like, it's, your mutations on it still need to, like, they can be licensed, but, like, the original code still needs to be licensed as GPL, right?
So I would say, if you could, if you could, put those, in a specific file that's different from…
the other code that you are trying to license as Apache, just to keep it a little bit easier to parse out. Similar to what we do when we copy in the underlying…
**Mattia Meleleo** 51:10 Yeah, sure.
**Tyler Yahn** 51:11 Yeah, yeah.
Bill, I see you have your hand up.
**Bill Zuo** 51:17 Hey, yeah, this is Bill Tua, you know, I'm new to this, you know,
I just have a question, you know, because I have a concrete problem that, you know, that we're currently implementing a more language-specific manner, for example, in, some extension to…
the Java instrumentation automation to capture all the, like, HTTP message bodies in… in addition to just those, like, meta information.
So, we are doing mostly, like, the business layer, data collecting instead of, you know, the infrastructure layer. Seems like, you know, timing or just the mass HTTP core status.
So, recently, I'm, you know, evaluating if we can…
move to the TBBF. You know, what we want is just an, you know, instead of capturing basic, you know, the…
messaging, or, like, a trace. We wanted the actual… HTTP body.
Yeah, so that's… I'm new to eBPF, I just have, like, I know that you guys expect. Could you give me some, like, feedback or hints if this, like,
possible, or, like, what's the pros and cons to implement that into via eBPF, so that we can handle all different text steps, instead of, do that manually for every single language that we are…
Right. Maybe by you.
**Tyler Yahn** 53:00 Yeah, okay.
Bill, it doesn't sound like you're talking about the current topic of conversation. I just want to make sure we actually
put a pin in what we're talking about, existing. Mattia, is this… is this something that you have,
next steps defined for you? Like, are you good going at this one?
**Mattia Meleleo** 53:19 Yes, sure, yeah. I will, open a VR, and then we can continue from there.
**Tyler Yahn** 53:25 Yeah. Okay, that sounds good.
To answer your question, Bill, like, I guess it'd have to depend on how much you've taken a look at the project. I would recommend maybe just running through our examples.
And maybe taking a look from there. You're looking about Java HTTP, I think we have a lot of support.
that Nicola's been working on there. And so, have you done that? Have you taken a look at using just the examples?
**Bill Zuo** 53:49 Yeah, I have done with, like, Java specifically, we extended those, like, Java, automated instrumentation on, you know, absolute connection, as well as, you know, ROS template kind of stuff, these, libraries.
That.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 54:05 I think, to give it a little bit of color, I think I know what you're asking, and these folks right here from CoreLogix here, Mattia and Nimrod, did a lot of work on this, to actually let OB capture large buffers. So, so what happens right now, if you look at our code, a lot of work went into that.
to be able to capture as much you can, and it's configurable, so you can actually say, I want buffers up to 2 kilobytes, or…
8 kilobytes or whatever.
And so all we will collect them for you. So what you need on top of it is… now, what we do with those buffers, we just simply post-process them for various reasons after the fact. So,
folks have been adding processors for Elasticsearch and for, like, SQS and things, protocols like that. But if you want to, do something else with them, then you can just go write an extension on top of OB, probably the easiest way to get started.
**Nimrod Avni** 55:06 I can…
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 55:07 code, for example, where Elasticsearch is handled, you can kind of start from there, and yeah, but let Nimrod, yeah, please, go ahead.
**Nimrod Avni** 55:15 Yeah, I, I…
I think the part where we did with dodge buffers and HTTP initially was for, like, extending for more HTTP-based protocols, but we also had the demand to basically get the full body and response and headers from HTTP requests.
And we thought about a couple of ways
of doing that. I think we also have an issue open there, and we have, like, we're describing
both, like, what we have now of, like, the large buffers in HCP, and also the stuff that we want to implement on top of that, which is, basically header, whitelisting and blacklisting of, like, you don't want to leak out, like, authorization headers and stuff like that. Also, for body, you might want to do some obfuscation of either
all the values, or, like, some Senate-sensitive values, or, like, based on regex, so… Yeah. It's something that, like, it's… I think we… it can be done based on the infrastructure that we have. Now, we just need, like, to design exactly how we want to…
implement this.
And we can, like, continue discussing it. I think it's a really cool and useful feature, and we just need to make sure, like, we know how to configure it so it, like, runs securely and does all the stuff, but it's something that we thought about as well.
**Bill Zuo** 56:37 Yeah, I'm glad that, this, we all… this discussion, I didn't already initiated. I see there is an issue open. Yeah, I'm more than happy to… to look more, deeply, and, you know, do some of the information, and then probably, like, come back to discuss, next time.
**Tyler Yahn** 56:58 Awesome.
**Bill Zuo** 56:58 Shut up, yeah. Laura, thank you, yeah.
**Tyler Yahn** 57:01 Yeah, thanks, thanks for the question.
Cool. Alright, we are coming up on the end of the hour. We had one more topic just to do a PR review, but we do not have enough time for that, so why don't we go ahead and end the meeting here? Yeah, thanks everyone for joining. If there's more topics, please also, continue in Slack, or asynchronously via issues. I think that's a really great place.
But otherwise, I will see you all in a week's time. Thanks all for joining. Bye.
**Nikola Grcevski @ Grafana Beyla / OpenTelemetry** 57:26 Thank you.
Bye.
**Mattia Meleleo** 57:27 Bye.
**Giuseppe Ognibene | Coralogix** 57:28 Thank you. Bye-bye.
