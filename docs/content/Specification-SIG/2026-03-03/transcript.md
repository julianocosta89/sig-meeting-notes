SIG: Specification SIG
Date: 2026-03-03
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/w70Fn5sLW7rRirHtsJE1TtLdq9FWCaZy_IxJHT8CaM5XPYhvSHy8Sv-Iu5cQAX3U.HRb4JXG9M22ZRVQS
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:32 Hi, everyone.
**Tigran Najaryan** 00:40 Hello.
**Florian Lehner** 00:45 Hello.
**Jack Berg** 03:04 Hey y'all, sorry I'm late. I am… running this spec meeting today, so I'll pull up the notes, and we'll start in a few minutes. I don't know if… Anyone else has already commented on that?
**Trask Stalnaker** 03:25 Nope, you're good to go.
**Jack Berg** 03:42 So, is Lude Miller here?
**Liudmila Molkova** 03:46 Yes, I am here. I thought that somebody would add some topics before, but… No snow.
Yeah.
**Jack Berg** 03:57 I guess I have a small topic, which is just that we're gonna be, cutting a release of the spec this week.
That's not really a topic, unless anybody has anything that they think ought to be in there.
**Carlos Alberto Cortez** 04:14 It's a topic because you're releasing also, as part of that, the configuration stability, which is great.
**Jack Berg** 04:22 Yep, includes the initial stabilization, of declarative configuration. So we finally reached 1.0 for that, for the schema, and for the spec parts of it, maybe something like 80 or 90% of the spec has been stabilized. So, that's really exciting. If there's any maintainers here that have been Waiting for a particular signal, waiting until the time is right, to implement, now's the time, because the schema won't be changing under your feet anymore, so… All right, any other comments before we jump into Lute Miller's discussion? Just a reminder for folks that, so, last week and the week before.
We had some positive feedback to sort of impromptu discussions that were status updates, kind of deep status updates from the various specification sub-sigs.
Two weeks ago, I talked at length about declarative config, and Josh Shareth talked about the status of the entities SIG.
And, we like those, right? So, we like having these opportunities for these spec subsigs to come back up to the broader spec group.
and tell people what's going on, so everybody's in the loop about these things. I think it'll help things move faster and be less surprised, by, by things that are coming down the pipeline. So, we asked for some volunteers to talk about the other spec sub-sigs.
In upcoming meetings, and where did we land? We landed with… Lydmella volunteering to talk about RPC stability. We talked about TED.
Giving an update about graduation and this overall, like, project priorities of 2026 for OpenTelemetry on behalf of the GC. And then in coming weeks, we… we have some volunteers from, TRAS to talk about logs, from Florian to talk about profiling, from David Ashpel to talk about Prometheus.
So yeah, that's… that's kind of the context behind this.
And I guess while I was talking, Robert, you added an agenda item here, and, you know, the whole point of this was to talk about other topics before we kind of hand over the conversation to Ludmilo. So, yeah, why don't you jump in, Robert?
**Pellared** 06:52 Hello, I just have a quick question, because I thought maybe it would be fast… I basically checked this just before this meeting, and I think that maybe it's worth asking here. So, we are right now, adding not to go, complex attribute support, like bytes, empty, map, and slice.
And I started reviewing the spec and implementation.
And what I, spotted is that in goal, we are not applying limits to the scope attributes, unless I have, I have seen wrongly, because I was not even making tests, I just looked at the code. And I'm not sure if it was not even the original intention, because we are not making… we are not remitting resources, for instance, so I thought maybe the same reasons as for resources are given for the scope after this. I just wanted to double-check what is the current implementation status.
And… yeah, if… and what is the, like, way forward? What do you want to do with this?
You can participate later, of course.
**Jack Berg** 07:59 No, I think it's a good question. I don't have an obvious answer to this. Some… some just, like, kind of thoughts off the top of my head. If I recall correctly, resources were excluded from attributes limits because of their, because they contribute to metric identity.
And so… or at least at one point, it was unclear… maybe it still is, I think it still is unclear which attributes from a resource contribute to metric identity. And so, like, for that reason, attribute limits don't apply to metrics at all.
Right? So, like, you know, there's log attribute limits, there's span attribute limits, there's not metric attribute limits, so they're sort of exceptional.
And, and resource attributes got excluded for that same reason. And so… Yeah, like, scope attributes, where do those fit in? Because they appear in the metrics signal, and you know, they're at least involved in metrics identity, so, you know, arguably that same argument holds for scope attributes for metrics.
But, you know, it's… they're not part of any identity or anything for spans or logs.
**Trask Stalnaker** 09:11 Jack, you said limits don't apply to metric attributes?
**Jack Berg** 09:15 Correct.
**Pellared** 09:18 One thing, Jack, the attributes, I think, are part of the identity.
for the tracers, metrics, and loggers. So, I think it may be a reason to not apply the limits there.
**Jack Berg** 09:33 That's true. So, like, a scope… a scope does have an identity, but it's, like, a different type of identity than, like, a metric series.
so… Metrics… I'm just gonna say the obvious thing, like, metric series, the identity is a crucial concept, because you have to be able to identify points in that series that come in over time and associate with them with the same underlying, ID, or whatever you're calling it, in your metric system, and so, like, while there is an identity for a tracer, for a logger, it's, like, it's a different type of identity. I don't know.
If that makes sense.
**Josh Suereth** 10:17 Is it right? Like…
**Liudmila Molkova** 10:20 Sorry, go ahead.
**Josh Suereth** 10:20 Yeah, I was gonna say, Jack, we, we… okay.
Whether or not you like this, the specification currently states that the resource… all the resource attributes are part of metric identity.
Which Entities is trying to fix by letting you only use some of them, which will be a breaking change, and we'll communicate that when that rolls out, but all of them are part of identity today. But additionally, when we did all the instrumentation scope stuff, we decided that was true for instrumentation as well. The name, the version, and all the attributes are part of metric identity.
And so if you have a metric from one instrumentation scope and another one from a different one, and they have conflicting definitions, that's allowed.
Currently, in our spec.
We will send both of them down.
And there was, there was, like, lengthy discussions on this. Now, whether or not that's, like, we like that.
is a different story. Whether or not people use that in practice, I don't think a lot of people do. I don't think a lot of people are using instrumentation scope in that way in practice, personally.
But that is what we've specified in our data model.
So, yeah, I think there's a lot of good questions that are being raised here. And I do want to call out, we do have cardinality limiting capabilities metrics, right? Like, the thing where we were talking about being able to limit cardinality and redact labels and let you know that that happened.
We might want to think about that for these other cases here, too. Something similar.
**Jack Berg** 11:48 Yeah.
Ludmel, go ahead, you were trying to jump in earlier.
**Liudmila Molkova** 11:53 Yeah, thanks. Is this right? So the count of attributes, well, it's still that the cardinality limit would limit them, but if somebody puts a very large String attribute onto metric.
what are we… why are we trying to protect the metric identity? It's already beyond broken.
**Jack Berg** 12:15 Yeah, you're putting a 2,000 character string in there, you're probably not adhering to, you know, using low cardinality identifiers.
**Liudmila Molkova** 12:26 Even if you do, even if it's a static string, you… You're doing something weird.
**Jack Berg** 12:32 Yeah, and I was gonna make a similar comment, which is, like, so, I was sort of just trying to, off the cuff, re… recall the history for why resource attributes are excluded from attribute limits, and why metrics in general don't have any attribute limits. And so, you know, that metric identity piece was the history behind that. As someone who's written and spent a lot of time thinking about the metrics SDK implementation.
I actually don't understand, like, those arguments. Like, so it would be perfectly fine to truncate attribute strings And if two measurements previously had distinct attribute values, but after truncation they were the same, then you just aggregate those measurements together.
I don't see it as a problem. Like, it's… by the time it gets to the back end, you know, the measurements from the distinct series have been spatially re-aggregated, just the same as we would use views to drop attributes. So, Yeah.
**Josh Suereth** 13:41 I can defend that a little bit, but the concern is actually that when you write a metric query, so unlike a log query, or like a SQL query, or a trace query, generally metrics, when you write a query, you write the metric name, and then it returns all the time series individually.
And so if you go from having individual time series with an alerting threshold, to having, like, an aggregate value with an alerting threshold, your alerts will suddenly fire.
Because your thresholds are now all wrong, because you're expecting them to be at a lower granularity.
My… again, I have personal takes. I can give you my hot take, which is don't do that. The default should be you pick which labels you use in every alert you write with thresholds. It's just in practice, that's not true. People… People will just do more simple queries, or not… not do the aggregation when they… when they do this, and so that's why we consider that a breaking change.
**Jack Berg** 14:39 But why… so… Why is it a breaking change if… at the SDK level, everything that comes out are… Our valid series without any collisions.
**Josh Suereth** 14:54 Cool.
**Jack Berg** 14:54 That's what we… that's what we read.
**Josh Suereth** 14:56 Yes.
**Jack Berg** 14:56 by having attribute limits in the metrics SDK would be, like, you know, you used to have You know, two distinct, series because of some difference in an attribute value, and after truncation, they're now part of the same series.
But from what's emitted on the other side of the SDK, what's exported, you know, it all just looks like those were measurements from the same series, and there's no sort of collisions.
**Josh Suereth** 15:25 You mean if the SDK is already aggregating those things?
**Jack Berg** 15:28 That's how it would have to work. Yeah, they would be aggregating those things if a collision is produced after truncation.
**Josh Suereth** 15:37 Oh, I see what you're saying. Yeah, the… I… I would be a… like, what the behavior you're describing is what I think I argued for.
In that, I think that that makes sense. The problem we have is, if I have one instrumentation scope defines a metric as an integer and another one describes it as a double, someone has to win.
What we decided was we're not gonna solve that problem, we're just gonna send them both downstream, and someone else has to deal with it. Like, like, your assumption is we know how to aggregate, and the problem is we actually don't, in some cases, and we'd have to actually write spec for how to do that.
I…
**Jack Berg** 16:15 From scopes, you're right. We don't do any… we don't do aggregation for metrics across scopes that have collisions. Like, you're totally right. But what I was talking about is, like, the lower level from scopes, like the individual series within an instrument.
And then also higher than scope's resources. Like, so if resource attributes were to be truncated, you would not… that would not produce any metric identity collisions.
**Josh Suereth** 16:38 For that, it would produce potentially a weird oddity if you're relying on the identity being similar between restarts.
That's all Like, like, let's say… let's say for some reason one of the values is larger this time I ran versus previously, because someone has an integer or a timestamp in it or something, I don't know. You know, that… but you're right, like, it's not… I think this is something we should probably look into and try to resolve, I guess is my TLDR. I think we… there's a set of problems that we kind of forced on others, and this is kind of the implications of it, but I think it might be time for us to start trying to tackle those. So I'm supportive of what you're saying, and I can defend the metrics viewpoint that we had.
But I also agree, like, let's… we should start… I don't think this is the meeting for us to just decide a solution. We should decide whether or not we think we should have a solution, right? Like, should we… should we work on that? I think that my answer would be yes.
**Jack Berg** 17:39 Do you agree?
**Tigran Najaryan** 17:41 So, I think We have to have… attribute size limits.
in the… in the scopes, and I think it's a mistake that we don't have in the metrics as well.
Those are… The reason you want to have limits is because when something is unlimited, it's going to cause a lot of problems downstream.
you're going to cause the systems that are receiving this data problems, or the systems are going to apply their own limits anyway, if they are designed well. They have to protect themselves. So, saying that something doesn't have a limit, it just says that we don't know how to apply that limit. We're opting out of solving that problem. Somebody else is going to solve it.
So it's not a solution, it's opting out of a solution here, really.
So, in my mind, we should look into Actually applying limits everywhere, and if applying the limits ends up truncating the identity in a way that Loses that identity and creates a collision with some other metric time series, or whatever it is, a different resource, maybe, even, right?
then so be it, right? Maybe you add mechanisms to detect that.
The loss of identity or the collision as a… as a… something that needs troubleshooting, maybe, in some cases, but it is the reality of the situation.
the fact that we don't do it at OpenTelemetry in the SDK, we emit data… at some unlimited sizes, and then it ends up being truncated somewhere else, because all the systems have limitations anyway. It's not solving the problem. It's just punting it down the road to some other system. That's how it happens.
Having well-defined limits at OpenTelemetry in the spec.
Actually, it's very helpful for all those other downstream systems to know what to expect to, and to design appropriately, to be prepared to receive those sizes.
**Jack Berg** 19:49 Piggrin, what you're saying reminds me of the conversations that we had when we introduced the cardinality limits and metrics, and there were some points being made about, like, hey.
it… We want to have We won't… it would be good if the series that we're emitted… we're emitting to represent this overflow series when cardinality limits are exceeded is, like.
is perfectly clean and, like, you know, perfectly sort of, like, blends in with all of your other series for that instrument. And we couldn't find a way to do it.
And basically, the argument was, like, that we landed on was, when you exceed the limits, you're in a degraded state, and it's better to get a signal out that you're in a degraded state than to try to, like.
retain conceptual purity. Like, emit the.
**Tigran Najaryan** 20:42 I agree.
**Jack Berg** 20:43 Don't just… don't just ignore it.
**Tigran Najaryan** 20:45 Yeah, yeah, it's a fantasy that you can actually have no limits in your system.
That doesn't work, really. You're saying there's no limiting metric attribute sizes.
There is a limit, it's just that that limit is not specified.
And probably, when you try to exceed that, instead of it being a known situation, it becomes an unknown situation. You are going to crush your system, something weird is going to happen, you're going to… To out of memory, anyway, right? But there is a limit, always there is a limit in real systems.
**Jack Berg** 21:31 So it seems like there's sort of, consensus or sentiment that, Scope attributes should be… should be constrained by attribute limits. There's some existing problems with attribute limits and metrics in general. We should probably think About solving these things collectively.
**Tigran Najaryan** 21:54 Yeah, I agree, we should… Robert, maybe you can file an issue, maybe separate issues for scopes and metrics if you want to, but I think it's…
**Pellared** 22:05 I think it's a mistake in the spec that we're saying that the metric attributes have no limit, really.
**Tigran Najaryan** 22:11 But let's think it through. Let's have an issue, we can have a discussion.
**Pellared** 22:15 Jack, you can make an action item for me to add, to create these issues. So we want for resources, as well as scope attributes, or no, just for metrics, but for resources as well.
**Tigran Najaryan** 22:30 My argument is everything should have a.
**Pellared** 22:32 everything.
**Tigran Najaryan** 22:33 everything has a limit, we're just not specifying that limit. That's the current situation.
**Pellared** 22:39 So let's…
**Tigran Najaryan** 22:40 create issues, can be one issue, maybe? Just do one issue, and if necessary, we can branch it out into sub-issues.
**Pellared** 22:48 Okay, I can click create a parent and establishes.
**Tigran Najaryan** 22:53 Thank you.
**Pellared** 22:57 Okay, can you imagine?
**Jack Berg** 23:03 Okay, Lyudmila, do you want to take over?
**Liudmila Molkova** 23:07 Yes.
**Jack Berg** 23:09 Do you want to take the screen share, or do you want me to continue? Your choice.
**Liudmila Molkova** 23:13 I'll share the screen. Thanks.
Okay, so, welcome to my talk about RPC.
We've started this project in May 2025, and that's 2026 beginning, and we reached our CE in February.
It's pretty exciting. It was not a super hard project from my perspective, but you see, it still takes us roughly a year to reach stability on something.
So we initially went through some exercise of scoping this project and saying, okay, what do we do for streaming? Because, you know, in RPC, there are essentially an easy case and a hard case.
An easy case is when you send an unary call. You make a request, you receive a response, and it's a matter of recording a span and just defining the attributes, metrics, names, and so on. We know how to do this, pretty much.
The other case is more interesting, the streaming case, when you have one long call, and you have message exchange between client and server.
But, you don't know if this… on the instrumentation level, or on the library level, you don't know how these messages are related to each other. You cannot make any conclusions that there is a request and response, you cannot propagate context through these messages.
And in the past version of semantic conventions, we recorded them as span events, with some, information, like the idea of the message, the number, the index of it, and the stream. So we decided that this is a strategic goal.
That we are not, going to try to create meaningful instrumentation unless we will find it necessary.
And we're… well… Scope this down to just recording the calls.
itself.
Both streaming and unary.
Then, the other interesting question was, what are the… RPC systems. So, in semantic conventions, we considered AWS SDK as an RPC system before.
And, it's still, an exercise, a subjective exercise, if you look into RPC systems, do they define themselves as RPC?
And essentially.
some of them do. The gRPC, ConnectRPC, JSON RPC, Apache Dabo, there are more, there are Microsoft technologies like WCF, and many others, but essentially.
what we… considered to be RPC is some generic framework that allows you to make calls to the remote service, usually remote, that provides something on top of, like, physical protocol. So HTTP is not an RPC system, but you can think about REST that it might be.
But we… it's the mental model, right? It's not the library. Rest is usually not the library.
So essentially, we talk about the systems, and we are going to… we are stabilizing gRPC and Apache Daba at that time.
We don't have enough expertise or instrumentations for connector PC, And JSON RPC is this weird beast which is more like a… An abstraction and mental model done.
the actual library you would instrument. We don't have essentially JSON RPC instrumentation libraries and open telemetry. So we're not going to stabilize this one.
I have a project board, I'm just listing it for… for consistency, you can take a look. I don't think it's interesting.
I want to walk you through, the migration guide.
But before… I wanna show you… Just a visual how the old conventions and new conventions compare.
They are really similar.
So if we look into the… client's bench.
So this is the new one, this is the old one.
And… we changed the RPC status code, it's now a string, it's similar to what JRPC native instrumentations do.
And it's also helpful because we can record are the same… the status code, the same attribute from different systems. Sometimes it's string, sometimes it's integer. We used to have per-system attributes.
Like, like this one. And we merged them into one generic RPC response status code.
The method is now the full method. We used to record two different Properties, this is also something we… Realized, was not… across our PC systems, and also it was not something that gRPC folks did.
The server address, server port appear here, but not here, only because the old Python, this is Python, did not set them before. They had some other names prior to, like, years ago.
Nothing interesting happens on the server side, it's pretty much the same. It's again the same renames, and… Yeah, we used to have some weird attributes.
And you know how I found it?
Since I have your attention, I need to show you this. So, I… had this test application, and they fed the input of the telemetry to Weaver, and here is the Weaver life check showing some violations about the telemetry I gave it, so it says this is not stable, and this is deprecated, this is from the old one. And again, there are a bunch of… alt, and the perkita attributes. Anyway… This is distraction, but getting back to… this.
So here you just see cosmetic changes, nothing else.
But let's talk about full changes, as some of them are structural.
So, the bunch of renames and cleanups, you've seen it.
So, we realized that we have all these different status codes for JRPC connector PC, there was one for JSON RPC, maybe. Probably, probably not. Then we had the repetitive Metadata properties for different systems.
The… Important thing that Prior, we did not clarify what RPC client spends meant.
You can think about the attempt span and the call span, logical versus more like physical.
The gRPC native instrumentation has both.
And we said that we will limit this convention to just the logical one.
And we will leave physical one to the underlying protocol, which is usually HTTP, or some form of HTTP, or a custom implementation that's not using the existing library.
So, we will leave attempts out of scope, and it will be thinking about Josh's favorite T-shaped API telemetry.
This is the horizontal shape, and GRPC can have their vertical shape however they want it.
Okay, so we are having usual renames for the system name. We now have some guidelines on how to name those things.
And following those guidelines, we, along with attributes renamed, we renamed some values.
we dropped this to France.
Because, they are old, and they should not live in Upon telemetry semantic conventions now, they should live somewhere else federated.
We also didn't have conventions, we just had a constant name for them.
So the duration metric also went through a similar, set of renames, milliseconds to seconds, and so on. It also now tracks the full Duration of the logical call.
Prior, it was not super clear.
So, prior, we recorded Exceptions, span events.
Now, we are replacing it with, still in development.
but log-based events. They're essentially the same as structurally as span events, they are reported with WARN, for clients, And this error for servers.
We'll have a more discussion on it when we talk about logs, but this stays in development for now. We don't… we're not stabilizing it yet.
We had this events per message.
In old conventions, we no longer have them.
Not because they are useless, but because, first we need to change them to log-based events.
And second, we need to make them more useful.
There were a bunch of controversial things there, and a lot of decisions to make, like this… Yeah, go ahead, Tigrin.
**Tigran Najaryan** 34:15 Just a quick question on these messages. Were they… in the old version, were they expected to be sent for… for each message in a streaming RPC? Is that what they were?
**Liudmila Molkova** 34:27 Okay, and you removed them, but you're planning to add something as a replacement for those?
**Tigran Najaryan** 34:32 That's the plan.
**Liudmila Molkova** 34:34 So we deprecated them.
we have not defined the new semantics for them, so it can be done incrementally. We are not… trying to stabilize this part yet. Yeah. And…
**Tigran Najaryan** 34:47 Yeah.
And for now, from what I understand, if I have a streaming RPC, there's going to be a spam at the end of the stream, essentially. So if I have a very long-running stream, it's gonna be delayed, essentially.
**Liudmila Molkova** 35:03 You will get this, yes, the span describing. It was always like that.
Yeah. Right.
**Tigran Najaryan** 35:08 Okay.
Okay, I'd be interested, maybe, in the discussions about the… the per-message events, and what do we want to do with stream RPCs, particularly for the… for the long-running types of streams. The… I guess the particular use case I'm interested in is in the staff protocol, which has very long-run connections, which can go… default is 10 minutes.
And, I think getting one span at the end of a 10-minute period is probably… I mean, it's fine, you get something, but… Preferably, you would want to have something at the beginning, I'm guessing.
Optionally, maybe for the messages, something as well would be useful.
So when… when you guys are discussing this particular topic, I'd be happy to come and see how can I contribute to that.
**Liudmila Molkova** 36:01 Yeah, two points. First one.
it… if we want to instrument something like this, and we have a good example, MCP, We're essentially defining a separate convention for MCP, because there are meaningful operations there within a stream.
And it's the layer above. And there you can instrument, like, individual requests and responses within a stream.
second point, we probably won't target this problem.
I'm happy to share the link with you, but we will… the current group will focus on stabilizing The logical part?
Without messages at all, and this can be added as a separate project later.
**Tigran Najaryan** 36:51 Okay, sounds good. I'll take a look at what you guys have, and if I have some thoughts, maybe I can… Submit some issues, maybe work on it myself.
**Liudmila Molkova** 37:00 Yeah, and would be super interesting, I think we have an issue that tracks it. Yeah, here, here we go. I'll post it here.
**Tigran Najaryan** 37:12 Great, thanks.
**Liudmila Molkova** 37:27 Okay, what else interesting has happened? We deprecated a bunch of metrics.
That, were questionable.
So, we realized that since we're not doing the streaming part, the requests per RPC, it was actually messages per RPC. We need to rename this metrics anyway, and we essentially, well, if… if we want to work on streaming part, we would redesign this metrics from scratch.
Similarly here, this metrics had some questionable scope. It was not clear if they applied to messages, or… requests, and how it would live in the world of logical calls, where retries could happen, like how many times we will track this, what would it mean, would it mean networks throughput, or something else? So, essentially, we deprecated those.
And this is a good segue to talk about gRPC compatibility. Do folks have any… Questions before we move over to that part?
Students know.
Okay.
So, the most interesting part happens now.
Since we declared RPC… oh, sorry, since we declared RC release candidate, immediately after the gRPC folks reached out, we tried to work with them from the beginning, but they were… they didn't have resources for this.
But, they realized we are serious, and they just commented yesterday that they would like to coordinate with us.
We are things to ask for a reply, and we're happy to work with them. And this is the only reason I don't… I'm not ready to say when we're going to stabilize, because we need to first to discuss it with gRPC folks.
But I, I, like, we, I can share how we look at this, directionally, regardless of… their involvement.
Sorry, I'm… Looking for the documents.
So, there is… there are native gRPC instrumentations for metrics and for SPANs. So, metrics are somewhat mature. I'm not sure that they are… you can enable them, they are… just one step away, the spans are more experimental and Almost not documented.
Okay, so… The… this is the… mapping between what gRPC has natively, and this is what we defined.
So these two are equivalent in pretty much everything, structurally the same.
convey pretty much the same information, but you see this has gRPC prefix.
And we really want to define a metric, like the basic metric for… to get all your throughput latency, and error rate that's generic, and you can build a dashboard that somewhat meaningfully represents your typical RPC system. And we just cannot be compatible here.
when it comes to individual, like the T, the vertical part of the T, then it's essentially not something that we want to define consistently across all systems, and this is where we Are effectively fully compatible, but not… by not defining things.
This is the structural part. Essentially, the GRPC metrics has… have these three attributes. Again, we would like to be compatible, but this… this concepts are generic enough that we Want to have common attributes here.
And server address and server port are the fundamental pieces we have for null client spans that are just something we cannot give up on. Then we have error type to clearly say if something was an error or not. You can Just without even knowing it's an RPC metric.
Just… just understand if something is an error or not.
And we set the RPC system name, which is also… and you can write a OTTL transformation from one metric to another. They are structurally the same.
This is probably the most important spends part. The spans are in… very basic in gRPC. They are very experimental, and, they only said method name. They… sorry. They only said method name and spend status.
So… it's… They're not structurally the same as our spans, but also it's probably not as important as metrics.
Okay, so then the next steps for us are we're working on prototypes, Trask has prototype in Java, I have prototype in Python, I think Matthew Hensley has, applied it to WCF.
And… the most important part is figuring out what we will do with… together with gRPC.
Anything you, Trask, want to add?
**Trask Stalnaker** 43:41 No, that was a great, run-through.
**Liudmila Molkova** 43:47 Thank you.
Anyone else has a question, comment, concern?
**Jack Berg** 43:54 Yeah, the gRPC point, I just want to reinforce the importance of the compatibility there. You know, we have this… like you said, they have native instrumentations, and one of the things that's going through my head as you were talking is, like.
with the Java agent, we're trying to figure out what the story is when there's a native instrumentation.
And we want that instrumentation to, be sort of the source of truth, so that we don't have to maintain all the instrumentation ourselves.
And, like, there's going to be this kind of recurring question, I think, that happens more and more as instrumentation goes native, which is like.
What if they don't conform to the semantic conventions? What if using the semantic conventions results in a step back in terms of the consistency that our users have grown to expect?
What do we do about that? So, yeah, really happy to see you, them reaching out and the willingness to work together.
**Liudmila Molkova** 45:06 Thank you, Josh.
**Josh Suereth** 45:08 I just want to say, this is awesome, and yeah, that, summary you have, if you, if you ping me that, I can reach out directly to the gRPC folks again, and I know that they're, they're basically overloaded, so the folks who were handling observability have shuffled.
And so there's a new set of people. So yeah, like, if you… if you send me the bug or, like, whatever you want to communicate with them, I'll make sure that they get it.
**Liudmila Molkova** 45:33 Yeah, thanks.
**Jack Berg** 45:39 I believe it's, it's this document, Josh.
the challenges, gRPC native conventions Alignment.
**Josh Suereth** 45:47 Cool. I'll open that and throw it in. Thank you.
**Trask Stalnaker** 45:51 Yeah, I conveyed to them that, yeah, we'd love to set something up quickly to start discussing, how we can move forward with them, since we would love to… Get to stable, or understand what we need to do to get to stable.
From this point.
**Jack Berg** 46:13 Alright, we got… How many minutes left? Is this 9 minutes?
Do we end at the 55 mark, or can we go all the way to the top of the hour? Either way, Ted, do you want to give an update today, as planned, or do you want to push it till next week? Or maybe a little bit of both?
**Ted Young** 46:34 Either way, I mean, does anyone have, like, a short topic, or anything they wanna… wanna throw in there?
So I'm happy to do this next week.
Otherwise, I can just give, like, a brief overview of this stuff. I think that's… that's helpful.
**Jack Berg** 46:55 Yeah, how about a primer? And then, yeah, we… if… if it's… if it's obvious that we're not getting through even, like, a good portion of it, we can… we can obviously overflow into next week.
**Ted Young** 47:08 Okay, so the… the short, short version, basically, where we're at with OpenTelemetry is we've been working hard on our original goals, and we're… we're closing in on solving them, which are tracing metrics and logs. We've… Added lots of other great things, like profiling and all kinds of other ways to do observability and different locations where we can observe things, but the core was to get Tracing metrics and logs working in all the major languages and out there for everyone to use in a stable way. And since the spec has finally stabilized on that stuff.
It means we can kind of put a bow on that original goal and say that it's done. And that would be a great time to announce graduation for OpenTelemetry in the CNCF.
So, we've been, going back and forth with them about what the graduation requirements would be. We went through an audit. It's been a long process. We've had an audit, security audits, all these different things, back and forth discussion with them.
And, they went out and talked to a bunch of end users, and we settled on a set of things that we think are important to get done as part of Declaring the original mission complete, and OpenTelemetry graduating.
one piece of this that's not… not part of, like, graduation stability, but is, like, relevant to… to making all of this work, and so I'll start with that, even though it's not necessarily listed in the stability OTEP, is, Centralized installation. Something that we have with OpenTelemetry right now is… all of our docs, all of our installation tools for the SDKs are really oriented towards an application developer to be able to do it. We have, like, tools in every language for allowing you to do things like resolve your dependencies and auto-inject things in some level.
But you kind of have to have code-level access, to do it in a lot of languages. Or, at any rate, you have to kind of go, like, service by service through it if you want to add open telemetry.
We've been working on an operator for a while, and that's improved this, for some languages on Kubernetes, but we wanted to have, like, a coherent, holistic way that you could just roll all of OpenTelemetry out everywhere, and manage it all through OpAmp and the collector. So we've been working on that, in a SIG called the Injector, which is the piece you need on Linux to actually install hook all of these SDKs into basically every language but Go and Rust. Those are the two languages we have support for that don't… have any kind of, like, C or standard lib dependency, so the injector can't work for those languages, but we are looking at using eBPF and, like, other tools for things like Go to get the same experience.
So, that's not part of stability, but that is a big change in how we roll OpenTelemetry out for people.
And it's also a place where we can improve some of our configuration story, which is something that is part of our stability initiative. So getting onto that part.
There is an OTEP that covers, basically.
like, the contract that we made with the CNCF around going back and forth and agreeing on, like, what we wanted to cover as part of this graduation effort. That's kind of the point of this OTEP. If you look at it, it doesn't have a lot of details about, like, how we solve the problems. It basically proposes the problems, the stability things that we want to focus on, and it suggests some work streams as a way to tackle it.
But it's a very high-level dock.
something we're struggling with, and we need to figure out, is we don't really know how to do these kind of, like, cross-sig rollouts, right? Like, the way we work in OpenTelemetry is to have a spec, right? So anything we all need to agree on goes in the spec.
But then everyone's allowed to work independently. All the SIGs can kind of work at their own pace, focus on the features they feel are most important for their community. We have a lot of autonomy in that respect. We don't do a lot of, like, hey, get all the language SIGs to row together and, like, like, work on something.
So, that's actually, like, the part that I want the most feedback on, for this, is figuring that part out. Like, if we're gonna have goals in general with OpenTelemetry beyond the original tracing metrics and logs, because I don't think stability is going to be the end of it.
I think it's helpful to find some way to have the SIGs, not everyone doing everything in lockstep, because that's impossible, SIGs are all in different places, but having some way of continuing to have, like, at least a group across different languages be sort of… Working on similar things so that they can collaborate with each other.
So, stability's kind of like the first one of these with graduation, but… once we're done with that stuff, I'm sure we'll have more goals. So this is, like, some… Some… some organizational growing that we have to figure out how to do.
But just to get into the high-level details of what we promised the CNCF we'd try to tackle as part of this graduation effort, let's go into the top-level items. So, I grouped the first three together because they're kind of related to this idea of stability by default.
When people get OpenTelemetry, there's the SDKs, but then there's all the instrumentation plugins and everything else, and we have installers that will install all of this stuff for you. But currently, today, across OpenTelemetry, there is not any consistency around those installers only giving you the stable stuff.
it'll just give you everything. Some of this stuff is stable, some of it's experimental, but, like, de facto stable, and some of it's, like, genuinely experimental, like some brand new thing we just rolled out, and it's genuinely in beta. You probably shouldn't… Be getting that component flowed all the way into production.
So that was one of the things that we identified from our end users, is they want to see everything be stable by default. So when you roll OpenTelemetry out, the stuff you get is all stable and ready for production.
We have a problem with that, which is if you try to do that with OpenTelemetry today, you get very little stuff.
And that's because of how we approach stability for instrumentation, specifically.
We were concerned about marking instrumentation packages as stable if the semantic conventions were not stable.
So, we decided, until semantic conventions go stable, let's hang back on marking the instrumentation as stable.
The feedback we've gotten from end users is that's actually confusing.
People interpret code-level stability like you would see from your package manager, saying, hey, this instrumentation package is in Bable… in beta, or experimental, or something like that. People re… interpret that to mean this thing is not safe to run in production.
Not that my telemetry might break, but this might blow my program up. That's what it means to be experimental, right?
And a lot of organizations have, like, you know, security and stability concerns, and they're starting to get all of that written down, and they have policies, and a lot of organizations have policies that say they can't run beta things in production.
So, this was probably, like, the biggest, sort of.
like, quickest schlep we could accomplish, which is to just change our approach to stability for instrumentation, and say, if the package is stable, if it's okay to run this in production, in the sense that it's safe, it's not gonna blow your system up, then that should be marked as stable.
when the instrumentation data changes, because we've stabilized it, or let's say we stabilized it, and then we did some kind of rev that changes it.
Those would be major version bumps.
So, you're still getting a major version bump to catch you and understand, I should have a look at this, because this might break my telemetry, but we don't want to stay gated and experimental. We want to go to 1.0 and then 2.0 and beyond.
So that was just a big change in how we approached marking stability that'll actually, I think, make a big difference to our end users, that mostly just involves us going through and auditing this stuff.
But when we do that, I think we're gonna discover a lot of this instrumentation is out of date, even relative to semantic conventions that haven't been marked stable.
Just due to how old some of this instrumentation is, and how long it's been since anybody touched it.
So, some way of going through all of our instrumentation, getting it, like, up to date, if it's out of date in terms of the telemetry that it emits, and marking it as a 1.0.
that's… that's kind of like a big across-sig effort we'd like to see as part of this stability thing. So that's a thing we have to figure out how to tackle, because… again, across our SIGs, we don't have, like, a big, consistent, coherent way we deal with, contrib. The SDK maintainers tend to be, like, we have our hands full maintaining the SDK, we don't have a lot of cycles to maintain contribib and instrumentation.
So, figuring out how we do a roll-through of that as an organization is probably one of the biggest schleps that we want to do here.
And we're basically at time, and I see you have a question, so let's, let's kind of end there. Oh, Teller Red?
**Pellared** 57:56 But just a quick question. From my experience, a lot of people who are worried about stability are the users of agents or different auto instrumentation. This is my experience. And the question here goes.
how we make major bumps here, because I think if we just make a major bump in one instrumentation library, I don't think we want to make a bump, a major bump for the whole auto instrumentation.
But maybe this is what the users expect, but then in so, then ours, then our, support guarantees.
Totally, this will not make sense in this scenario. That's all my feedback, or question, or however you want to interpret it.
**Ted Young** 58:37 That's a good question. Trask, I see you got your hand up.
**Jack Berg** 58:40 Grass, take us home. We got one minute left.
**Trask Stalnaker** 58:43 I just wanted to share the Java agent experience, that, that's exactly what we are doing. I mean, and we do have, you know.
100-plus instrumentations, but we do have a single version and a single major version bump, so we kind of hide changes behind flags.
And then, you know, so you can opt into those changes earlier, or… and then at the next major version bump, we flip it on by default.
**Ted Young** 59:14 Yeah.
**Trask Stalnaker** 59:16 But I agree, that's a tension that, a lot of it that needs to be discussed more. I don't want to make… act like it's a simple answer.
**Ted Young** 59:25 Yeah.
Yep, that's the one place where the language-level dependency managers are really helpful right now. And as we go to some, like.
cross-system way of installing things. Well, now we're not leaning on those language-specific dependency managers anymore, so we have to have some other way of describing this stuff.
And that's time, so we'll continue this discussion next week.
**Jack Berg** 59:51 Thanks, everyone!
Talk to you later. Bye.
**Pellared** 59:54 Bye!
**Carlos Alberto Cortez** 59:54 do.
**Riccardo Magliocchetti** 59:55 Bye, thanks.
