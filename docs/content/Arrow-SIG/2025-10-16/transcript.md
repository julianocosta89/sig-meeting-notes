SIG: Arrow SIG
Date: 2025-10-16
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/rNFR9iDee9T-54IzBO6smuAk4TPoqWj0vnPKOq-DNiuKlniLUoxa2Lk8NWumPA.pXFIPcn6IjP1KGBo
============================================================

## Zoom Recording Transcript

Laurent Quérel 00:00:15 Leu.
Pablo Baeyens 00:00:21 Hey!
Laurent Quérel 00:00:22 How are you?
Long time.
Pablo Baeyens 00:00:24 Doing fine. Yeah, long time. I'm going to try and join… this meeting… Dude.
Laurent Quérel 00:00:32 Nice.
Pablo Baeyens 00:00:33 The other one is at an inconvenient hour, but this one I can… I can make it, so you'll see me every other week.
Laurent Quérel 00:00:39 Little kids.
North River, where are you, located?
Pablo Baeyens 00:00:44 I'm in the south of Spain, so…
Laurent Quérel 00:00:47 Oh, yeah, you can… Hmm.
I think Josh will join us soon.
Just in case, I will share the… the link to the Google Doc?
In the chat.
So we can start to… To a date and put some agenda.
JM Joshua MacDonald 00:02:06 Good morning.
Laurent Quérel 00:02:08 Good morning, Josh.
Okay, I just, finished to… to create the… the new entry into the Google Deck.
JM Joshua MacDonald 00:02:35 Well, I see we have Pablo joining us.
Welcome, Pablo.
Pablo Baeyens 00:02:41 Yep.
Oh, thank you. I'll be here every other week.
JM Joshua MacDonald 00:02:46 Yeah.
Pablo Baeyens 00:02:47 to get more involved in… RO stuff.
JM Joshua MacDonald 00:02:51 Thank you. I… I want to say, since you're here, that I've been doing my best and most honest to keep this charter of the Hotel Arrow separate from the collector, and not… not say we're, you know, building a collector, because we… we don't want to do that without more involvement from the community.
So, you know, I, continue to be fair and honest with my collector involvement, is what I'm trying to say.
Pablo Baeyens 00:03:16 Yeah, I appreciate it. I think… I think you're doing a great job in that regard.
JM Joshua MacDonald 00:03:21 Thanks.
I think that at least the agenda I know about… Laura, I want you to lead, if you can, would be to look over the issue… issue review.
you had asked me to look at the milestone for December. I haven't finished fully studying, but I did add a couple of tickets that came top of mind when I had my team review stuff.
So, the two that come to mind are on the top of the list if we're gonna do a new issue review.
And then I have open PRs, which I would love to get some attention, or, like, at least discussion on, So, that could be my agenda.
Laurent Quérel 00:04:07 Okay, this seems good.
So you start and share your screen, or how do you.
JM Joshua MacDonald 00:04:13 Sure, I'll, yeah, let's start with issue triage. I'm gonna share… here we go.
Yeah, here we are.
You can see my screen.
And, I'll just pull that up. So… It's been a week or so since we met, and… Just to keep everyone, especially Pablo, in the loop here, we've put together a milestone summary of the sort of core features that we feel are most important for development over the next couple months.
And, you know, I'm focused on the retry processor right now.
The issue list covers a lot of old stuff, you know, back at 173, you know, but also some new stuff.
And there's a board, there's a project board, I won't click into it. And I think, many of these new issues are ones that we filed after we kind of looked at that list, so maybe that's the set I'd like to review now.
Some of these are just, like, umbrella issues, so, and they might just say very little, This is a strong statement that we should not have unbounded memory when we have back pressure.
I fully agree. In fact, that is one of the ongoing topics in the Collector SIG as well.
test back pressure. I fully agree. In fact, that's the… I would say the reason why I'm feeling kind of urgent about my PRs is that until we… there's no… there's no receiver or exporter that implements back pressure yet, so we're… we're not quite there.
And, so… OTLP export and receiver is what I'm thinking about.
Those are the open PRs.
Laurent, you want to talk about your ideas for semantic convention registry?
Laurent Quérel 00:06:29 Oh, yeah, so, as you know, I'm involved in the… Hotel Weaver Project.
Can you hear me?
JM Joshua MacDonald 00:06:39 Yes.
Laurent Quérel 00:06:40 Okay, so I'm, deeply involved into the Hotel River project, which is the tooling, basically, used by the semantic convention project to To maintain, to process semantic conventions in general.
And, now since… probably more than 6 months. We support what we name custom semantic convention registries.
Which are a way, basically, to express for an application the… Specialized signal that this service device or whatever is producing.
And then we can reuse the same kind of control and code generation and documentation generation that are currently used.
For the standard hotel cemetery convention.
So, I liked the… this new pipeline engine. Follow the same pattern, ideally.
And generate, or having at least a way, either it's maintained manually, or even bitter.
Maintained automatically.
The semantic conventions specifically for this pipeline engine.
So the… And then we can generate documentation, and then we can, use some CI-oriented mechanism part of Hotel River.
to validate, for example, the instrumentation coverage. It's a functionality that is part of Weaver.
Name, live check.
That gives you a weight.
During your integration test, or, for example, the benchmark system that we have.
or the stress test that we could implement at some point. We could, collect all the OTLP metrics.
Events and so on, and detect when there is a gap between what was expected in terms of telemetry and what we observe.
And, and act accordingly.
So that's why. And so right now, we already have, I think, a good foundation.
Because even if we have internally this, multivariate metric implementation, which is not, standard.
There is a way to automatically derive a standard OTLP matrix.
from those internal multivariates. And there is, already an endpoint, I need to retrieve the name of this endpoint.
for the admin, HTTP server that we have internally, that generates automatically the… those semantic conventions.
So, live, we can detect that. So the idea is to put some CI automation in place, having that as a file that we put into the system, so we have a way to maintain it easy.
Should not be a big work. Right now, there is nothing regarding the event, but at least for the metrics, we already have a… A good start.
We call their users.
JM Joshua MacDonald 00:10:04 As you know, I'm, interested in, exploration, I will call it, for a multivariate metrics SDK, for a multivariate metrics data model, for a multivariate metrics API. All those things are, I think, in scope for us, as long as we keep our eye on the main deliverables, and sort of keep it short. I did file, since you're on that topic, this is the one that is going to be a kind of a kicker for us, is that I want to be able to push the metrics out in an OTLP format. I know that what we have today is an admin console, much like a Prometheus receiver.
Laurent Quérel 00:10:42 The Prometheus exporter, so.
JM Joshua MacDonald 00:10:45 That was actually maybe one of the parking lot conversations I wanted to have after the triage here, which is the state of metrics and what we expect from OTAP metrics. I think there's a couple questions.
Cool. Well, so that makes sense now. I get the connection with Weaver, and the ambition to do more semantic encoding. Yeah.
Laurent Quérel 00:11:10 And we're using the… and this exercise is definitely not… fully done.
But we… Because we have this, Export of every metric attribute currently, used for all the metrics inside the system.
We… we will have an exercise of figuring out if there are some attributes that should be, reused from the standard OpenTelemetry semantic convention.
I tried to do my best, but sure, there are some that I missed.
So we need to, To make sure that we are aligned, and so this rationalization exercise at some point will happen.
JM Joshua MacDonald 00:11:56 Okay.
Laurent Quérel 00:11:57 I, I, I, you know, that's it.
JM Joshua MacDonald 00:11:59 Yeah, so for me, what this rep… brings up is, you know, I think nothing happens… like, we can't build something incredibly great all at once, right? And I think, you know, there's many places in our codebase where we've kind of put in a placeholder, you know? Like, this is gonna get us through now.
And metrics instrumentation is an area where I already feel like A little chaos, Because…
Laurent Quérel 00:12:25 I agree.
JM Joshua MacDonald 00:12:26 you know, most of the pipeline metrics are really, like, the same for all the components, and we can't go instrumenting every component like that, so I know that… I think this is gonna be soon, I want all of us to know it's an important one, which is, like.
Right now, we have these channels, and we send messages, and we have these control channels, and we receive acts and acts, and, like, that is the signal for counting the things moving through the pipeline. I would like to have the instrumentation of the pipeline message movement underneath that abstraction layer, somehow. And I don't know exactly the way to do it.
Laurent Quérel 00:13:00 Well, that was the plan, That's the plan, day one, but, like you said, we proceed with, With the instrumentation of the nodes?
Yeah, and we didn't proceed with the implementation of the pipeline. I think it's a mistake, because then we will have some duplicates.
But that's how it is.
JM Joshua MacDonald 00:13:25 more about.
Laurent Quérel 00:13:25 We do some, some garbage collection at some point.
JM Joshua MacDonald 00:13:28 Great, great, that's a good way to put it.
Yeah, I… I… I fundamentally, though, agree with the multivariate instrumentation approach, the use of structs to, like, put your field… your counters, you know.
And… Don't want to get too, too down into the SDKs are hard-to-write details.
Actually.
So, cool. Well, we'll move on from that topic. I skipped us forward to the export OTLP metrics. I'm gonna keep skipping us there. So, for me, I… I was just imagining what pieces are missing right now. I think that we have not implemented all the way the OTAP representation for metrics the same way that we have for logs and spans today, because it's just, you know, four times as many tables.
And that, to me, is… has become a source of concern.
And this is lending me this idea that maybe we should start talking about multivariate metrics as soon as possible. However, I think this is a question more for you, Laurent, is… what we have is, you know, 19 tables of OTAP in Arrow, and that's fine.
honestly don't think anyone's using summaries, honestly don't think anyone's using… or, like, you should use one histogram, not two, etc. But that gets it only down to 12 tables.
I think we've mostly implemented it. I think Michael was working on some of it. My question is for you, and Albert, like, do we have that data path done? And then.
is the missing piece then just, takes those multivariate structs from the instrumentation, turns them into arrow rays that are OTAP records, and then we should be able to push it through a pipeline that looks like an OTAP pipeline, and it should spit out internal metrics.
Laurent Quérel 00:15:22 So I can, so let me organize my license.
Explore that, I think there is multiple topics there. The… We're getting the matrix support for that.
I don't think we can avoid to support all the metric types if we want to be compatible with OTLP, especially because the… the fact that we built an ATAP engine And not an OTLP engine.
And obviously, we want to support the TAP class.
JM Joshua MacDonald 00:15:59 Yeah.
Laurent Quérel 00:16:01 Make us, forced to support every type of metric type.
Because we don't know what we will receive at any point.
That is, an ongoing work.
Hopefully, I was expecting to see the PR done for the end of the week. Unfortunately, Michael was sick.
And, the… A kid sick also at the beginning of the week, so… Hopefully, next week, that will be done.
That's the expectation.
Now, regarding the…
Pablo Baeyens 00:16:37 The support of multivariate metric. I already have…
Laurent Quérel 00:16:41 let's say a plan, with, an extension of the data model.
Never tested, so it's right now more an exercise of data modeling and trying to figure out if the… at the end of the day, this additional extension will make the Like everything we observed before, a better compression rate, and a better data processing speed.
I think so, that is on my experience, but obviously we need some benchmarking tests, and obviously, some additional implementation. Should not be a big work, in fact.
But anyway, it's, it's still, it's still work to do. So I… I think it's a big, big stretch goal if we want to achieve that for end of, mid-December.
I think it's… it's a little bit too big. I wouldn't… You mean… But… Yeah, yeah. Especially because right now, if you look at the benefits.
I think the benefits will be gigantic, long term. And as I'm saying gigantic that, By exaggeration.
I really think that it's a big problem inside OpenTelemetry, but…
JM Joshua MacDonald 00:18:02 Yeah.
Laurent Quérel 00:18:04 without a strong support inside the client SDK, you will not observe the benefits, except for The only thing that will support, MTI matrix, which is this pipeline engine at some point, will be probably the first to support it.
So we will observe benefits for a very, very, very, Small thing.
So… that's why I think it's not necessarily a major urgent task, in my opinion.
But it's definitely an urgent test overall for hotel.
JM Joshua MacDonald 00:18:39 Yeah, I have a thought, but I want to hear Pablo, since his hand is up.
Laurent Quérel 00:18:42 Yeah.
Pablo Baeyens 00:18:43 Yeah, I have a couple of dumb questions, since I haven't really worked on this before, but, what's the current level of support for metrics? Like, what types are supported?
Laurent Quérel 00:18:54 We want to support everything.
So the… the gauge, the… the contour, the updated contour, the histogram, the summary…
Pablo Baeyens 00:19:04 Right now, there's… Right now, we are closed to… it's.
Laurent Quérel 00:19:09 So we have someone in my team that, He's working day-to-day on that.
That's definitely the most complicated… part of the hotel model and implementation, so… yeah, we are close. I will say that we are 90% done.
JM Joshua MacDonald 00:19:27 For the background here, we… the OTel Arrow Phase 1, the Go components and the Go reference implementation do this, you know, supporting all five metric types and so on. And it's just that we haven't done the Rust equivalent for that yet, too.
Okay. Translate the multitude of metric types is just more code.
Pablo Baeyens 00:19:47 Yeah, that makes sense. And then the second question I had was, What… what do we mean with multivariate metrics? Metrics with multiple values per timestamp, or is it something completely different?
Laurent Quérel 00:19:59 Yes, that's.
Pablo Baeyens 00:20:00 Okay.
Laurent Quérel 00:20:01 They are… so… Let's take an example of, very basic example, memory usage.
Or CPU usage.
If you look at any tool on Linux or whatever is in the OS, memory usage, at least memory metrics, they all come with a bunch of maybe something like 10 memory metrics, CPU matrix, something like 10 CPU matrix.
And usually, they are all reported with the same attribute set and the same timestamp.
If you look at what that means for OTLP, it means that you have to duplicate those attributes on the wire, duplicate the timestamp, and so on. It's a vast amount of data that are just duplicated without reason.
Pablo Baeyens 00:20:52 Right, right, okay, yep, thank you.
JM Joshua MacDonald 00:20:55 It also comes…
Pablo Baeyens 00:20:57 Go ahead. Sorry.
You can go ahead.
JM Joshua MacDonald 00:21:01 Well, I was gonna say, There's sort of like a… when you talk to a data engineer or an analyst who is common, you know, works with metric data in the real world, they're very familiar with the idea that you have tables of information. You've got rows, which are your timestamped observations, and you've got columns, which are all the variables that you measured at those timestamps. So it's sort of common outside of the world of, I would say.
Computer metrics that we are so familiar with, that you would take more than one measurement on a line.
So I mentioned in the chat, InfluxDB is a perfect example. They sit outside of OpenTelemetry, they cover open… they cover observability, but they cover the vast world outside of observability as well, and their line format does support multivariate.
Laurent Quérel 00:21:49 Yeah.
JM Joshua MacDonald 00:21:50 when I think.
Laurent Quérel 00:21:51 Exactly.
JM Joshua MacDonald 00:21:51 what we're trying to achieve. Also, it's more like, it's expensive to instrument so many variables, and, like, we don't have instrumentation APIs that could say, here's my attribute set, here are 5 measurements I just took with the same attributes. It should cost you less to instrument as well.
And, so, I think the… the… my… thinking as far as, yeah, no one's doing this yet, so why would we build it, is that we have our own multivariate metrics sort of setup. We have that SDK under development. We are the ones who are going to prove that you can make multivariate out of instrumentation, and then do something with it. I guess the hope I'm having is that, again, I think I've shared this with everybody now, my dream, or, you know, one of the long-term projects I have, ambitions I have for OTEL is to have a metrics engine, which means we're going to be able to take in all that data and, like, manipulate it, erase attributes, but correctly aggregate, and so on.
I don't… I… when I think about doing that, it's, like, kind of a large task, and one thing that would probably simplify it, I'm saying probably, because I haven't done it, would be… To, have one table of metric data.
and learn how to build an engine that's multivariate. And then… and then I can have one engine that's my multivariate metric engine.
I translate all my univariate metrics into it, I do all the stuff I learned to do with multivariate, it's just that they're univariate, and then I spit them back out as univariate, or whatever. The point is, I think it's going to be easier to build an engine once, probably once, for multivariate, rather than once for every univariate signal we know about.
Maybe wrong, just a thought.
Pablo Baeyens 00:23:30 Well, I was going to say for, like, thank you, thank you for answering. If I am derailing the meeting too much by these questions, let me know, and I can…
JM Joshua MacDonald 00:23:37 I don't think you are. I actually… you know, one of my long-standing interests is in OpenTelemetry is instrumentation, and I think metrics is a tricky one. Like, I… everyone is unhappy with the cost of metrics, and I think… the… part of it, I think, is that we're using the wrong interfaces. If I am forced to construct an attribute set, and then make a measurement, and then make another measurement, and then make another measurement through the API, it's already sort of too… too much overhead.
And, there will be debates over the optimization potential, of course.
And… And I think… OpenTeometry itself has a problem with instrumentation cost.
One of the things I know that advanced users do, which they can't really do in OpenTelemetry.
Is to kind of combine the instrumentation… the instrumentation of attributes, the instrumentation of scope, the instrumentation of context, the instrumentation of a request.
Often you're generating logs and metrics and spans, and there's an efficient way to do all those things that doesn't repeat yourself so often, so… maybe when I start my span, I put some attributes into a scope. Then when I metric, I don't recreate those attributes, because they're part of my scope. It's, like, implicit state that I think people do. These are instrumentation APIs that exist outside of OpenTelemetry.
So, when I think about multivariate, I also think I want to make sure that I have new APIs that let me do the minimum of instrumentation that spit out the multivariate metrics as well, so… Maybe it's, like, there won't be a metric update, so you'll have your begin span, and your end span will include a bunch of measurements, and it outputs multivariate metrics. That's two instrumentation points that gives you 5 measurements, or whatever. That's what I'm after.
Is a new and better way to instrument.
Laurent Quérel 00:25:31 I will just, like to add one, one, One last, comment on that.
So multivariate matrix, I think, why they are so important, it's not only because there are a lot of overhead regarding the instrumentation side, but also the true sort, also the storage, also the query, and also the mental model for everyone that is Leveraging this information.
And at any level, in fact, not having a meteorite matrix is a problem.
Which… That's why, in my opinion, it's… that should be one of the top priorities, because, in fact, it's… Yeah, impacting every, every part of an observability stack.
integrating human and using it.
Pablo Baeyens 00:26:23 Makes sense.
Thank you.
JM Joshua MacDonald 00:26:25 Cool. Well, we've all… now we've laid out our dreams, our hopes and dreams, and… and I… and I just wanted to emphasize that we feel we're experimenting with SDKs and instrumentation, not just the OTel Arrow right now, so… I'm back on our issue triage.
We're halfway through the hour, almost.
I see a couple more that are kind of, like, broad issues. I'm already working on, retry, which is not listed here, and, for me.
I'm, you know, I'm kind of focusing on the control flow stuff, the back pressure, the axe and the NX, and the implementation of all that. So for me, these two are both kind of pressing next concerns.
just as a matter of exposing the history here, I spent about 4 months studying rate limiting in the Go Collector world, gathering requirements, and eventually Laurent said, Josh, we need you to do some work here.
And I started working on a… thinking I would prototype rate limiting next in… in this code, just to, like, get more experience. So that is, a correlated effort across the two, and I'm… I'm gonna try and… Do a, like, version zero, proof of rate limit design for… for this, and then bring it back to the collector group.
Laurent Quérel 00:27:41 Yeah, and I will, also on my side, Josh, Also, start to focus on those things with you, Also, with the memory limit system, and The… the emission control in general.
JM Joshua MacDonald 00:27:56 Thank you, yeah.
Laurent Quérel 00:27:57 That's cool.
JM Joshua MacDonald 00:27:57 So, rate limiters are… users want it a lot, but I feel like the memory limits are actually the more important thing, and What I'm hoping to achieve is sort of, like, the minimum viable version of something where a request comes in, let's say a gRPC OTLP request, it has headers.
the configuration of limits is almost always going to say, I want to pull a header and look at it.
Anything beyond a naive configuration. I want to look at the header, it's got a user tenant, or whatever identifier. Next, I want to put that in the context.
Now when I get to my rate limiter, I'm gonna say, I've already done my rate limiter identifier.
it's got the header set by the guy that knows the headers. Now I have my key. Now I need some sort of logic to say, okay, the key is here.
which limit am I using? Is it the default limit or the big limit, maybe, for example? And that's about it, is that you separate the identification and the keying of the context.
Because that happens early in a receiver. And then, somewhere in the pipeline, you add limits.
But I'm afraid of.
Laurent Quérel 00:29:06 So, I think that the next part is the emission control, control message.
That will be generated by the right limiter, for example.
And should be honored by the receivers.
with the same kind of mechanism that we created for the ACNAC Combined with the retry processor.
Which is a nice interaction between the exporters and the values component.
upstream.
Especially the retry and the failover.
But for the direct limiter, I think that's more or less the same kind of control we need to put in place, except that the message is not a hack or NAC, but more… Some kind of, I don't remember the name I gave, to one of the design, but it's related to admission controls, so the… Okay. Resource budget, or something like that.
JM Joshua MacDonald 00:30:03 The reason this got complicated in Go is that we were dealing with gRPC, and the observation is that in many cases, your limit could be applied right there before you begin constructing the request, like.
Laurent Quérel 00:30:16 We need a control message back to the receivers.
Exactly like the exporter versus retry processor.
Except that it's at the beginning of the pipeline.
And, and we can inform So the… I think that's exactly the same logic. We don't want every receiver to implement a complex logic.
for the rate limiting, or for the memory limits, and so on. Right. So we want to focus this complex logic into a dedicated component, like the retry processor.
But we also want to have a control message mechanism that will inform, of what to do.
So they just have to, turn on, off, some connection, or to refuse something that matches a specific condition, like a tenant ID on a specific header.
And, and, And that's it. So, trying to move the complex logic and the dedicated, flow control, flow-oriented, component, and, and implement a very basic logic into the… at the boundary, either export or receivers.
JM Joshua MacDonald 00:31:28 Let me ask you, a sort of sample type of question. Like, in the GO model that we had… that I've studied.
you know, we arranged for this decision to be made sort of deep down in the middleware, like, as soon as you have the data sort of start to arrive, but it's still, like, there's a reference and a mutex and a thread boundary somewhere where you're like, okay, I'm now a receiver, I'm going to contact the rate limiter logic, which is an extension.
and ask it if I can do this or not. So it's like a synchronous call.
Where you're crossing a thread boundary, grabbing a walk, asking to do something. And that is very normal in Go.
I don't think that's very normal in the system we've built here. I think what you're suggesting is some sort of more, maybe ahead-of-time messaging, where you'd say to the receiver, I grant you permission to accept a megabyte of data for the… or something like that.
some decision that… a sort of information that can be used to make decisions in the future, in the near future, until the next set of decisions arise. So it might be, like, In a rate-limiting situation, you allocate some rate, and then you hand it to the person who's gonna use it, and they meter it out, and then they say, I'm out, I need to get some more rate.
Maybe. That's just… I don't want to go.
Laurent Quérel 00:32:49 Yeah, that's the…
JM Joshua MacDonald 00:32:50 Sure.
Laurent Quérel 00:32:51 Yeah, so that's, Yeah, that's more or less the plan I had in mind. Obviously, we need to test to validate this approach.
If we observe any kind of issue with that, At least per pipeline runtime, so one per core.
We… we… even if we want to implement what you mentioned related to the Go implementation, we could do it without Mutex.
Because we are running into a single thread approach in that case. Now, if we have to apply a rate limit globally.
Across golf?
then that's where we will have some, additional, synchronization. Maybe we could have, like, a mixed approach, where we have a no-mix approach internally into the pipeline, and a messaging approach, interpipelines, if we need to have this kind of synchronization. So we will send messages To the other pipelines on a broadcast channel.
To inform that we… we observed some, limit reach for a specific tenant, and the other pipeline will receive that for a specific amount of time, and could apply the corresponding limitation or policy.
Definitely something we need to explore, and .
JM Joshua MacDonald 00:34:20 Yeah.
Laurent Quérel 00:34:21 I will defeat I'd be interested in working on that with you.
JM Joshua MacDonald 00:34:24 Okay, I have a few questions that I won't ask right now, but I think I… I think I don't quite have the full picture in my head about how I could share a reference to something.
Especially when I'm thinking of the gRPC receiver, which uses a shared receiver logic, so I think I can't, but maybe I'm wrong about that.
Anyway, that's a little bit low-level detail for everybody here. I'm gonna… we'll keep talking on that topic.
Failover processor is a lot more straightforward for me, but that's an interesting design space.
it actually connects with this other one that I, wrote out, and I want to talk about that briefly. So, one of the key requirements that was stated to me by an internal member of the team here is, like, look, we have a product built on the Go Collector model, essentially, which has that baked-in model where You… receivers are connected with processor pipelines and are connected with exporters, and every receiver Essentially, logically broadcasts to every pipeline in an isolated fashion, so that, you know, every receiver output is stitched to every pipeline that Connects to it. And there's seamlessly, automatically, isolation.
And it knows about copy on write, so it knows if you're mutating the data that it has to copy before it calls, and so on. That's the isolation mechanism. Moreover, it does it in sequence. There's never parallel exports in this fan-out. It's just part of the design. I would say it's an area where you could call for options, like… Maybe you do want concurrent exports in this fan-out arrangement. The other options that come in are, do you want to fail fast? Do you want to fail, if any, of your fanouts?
Or do you want to fail if they all do? Do you want to wait for them all to fail, or do you want to fail if the first one fails? Do you want to succeed when the first one fails, or do you want to succeeds, or do you want to succeed when they all fail? These are all configuration spaces that… Basically, connect, failover, and fan out in a… they're almost the same at that point.
I'm wondering if there's a kind of common, like, connector that's, like, can do fan-out, can do failover.
configured to do all those things, but what I need is to emulate the Go Collector in this way. So, at the bare minimum to implement that fan-out logic. And I linked to exactly what the Go Collector is doing, and you can see It's not super straightforward, because it's dealing with, like, are there mutables? Do I need to copy? And then it runs the read-onlys first, and then it runs the mutables, I think. Yeah.
Laurent Quérel 00:37:02 That will definitely not be the… yeah, that will not be the way for us, because we are using channels.
broadcast channel for this specific case, for example.
So it's not a sequential approach, it's, like, a parallel approach.
We have different ways to find out, in fact.
JM Joshua MacDonald 00:37:22 That's what I was gonna say. I think… I think we could emulate both… both a parallel fan-out broadcast and a sequential iteration broad… fan-out.
And I really…
Laurent Quérel 00:37:33 Surely it's like the silver, right?
It's like, you try the… is the second shell, semantic, of at least the expected semantic for the second shell?
Is it something very similar to the failover processor that we…
JM Joshua MacDonald 00:37:50 similar. It would be… it would be sort of within a configuration knob of difference to say that you want to fail early, as opposed to, After the first success, you can return. That would be a configuration that makes it look like failover.
What I was… what I was… this little note I wrote here was thinking through the idea, because I… you all have raised the, like, warning flag, okay, the engine only knows about P data, and you're dealing with context.
and you've got a backwards channel, so you're pushing the data back through the pipeline, but we're carrying P data, and that's because the engine and the control messages don't know about context, they only have P data containers.
So… This means that the Notify Act message will inspect the interests now and see if you have return data set. If you have return data set, you'll give it back.
So then you could imagine a fan-out arrangement where it's sequential, and there's never a copy or a clone made. Where… the fanout sends it to the first exporter with return data set, gets an ACK, with its return data back, sends it to the second exporter with its return data set, gets an ACK, keeps doing that. So, there's only one copy of the data live. This requires no one to… that no one's modifying the data, which is something we haven't really built up, so…
Laurent Quérel 00:39:11 No, no, no, no, no, no, we have.
We have that enforced by the compiler directly.
JM Joshua MacDonald 00:39:16 So there is no way to… yeah, there is no way in the system to update the… our records without.
Laurent Quérel 00:39:23 for a system that will compile. So first, because first, the hotel arrow is immutable, so you can't update in place.
JM Joshua MacDonald 00:39:34 But… but I'm saying that for a request in, like, the AC or the NAC, I… like, I'm not holding that data. I put some data into a message queue.
it came back to me, I don't know if it's the same data or not, and the…
Laurent Quérel 00:39:47 No, I mean, it could be totally different.
JM Joshua MacDonald 00:39:49 That's what I'm trying to say, and it could be Meaning it got turned from OTAP records to OTAP bytes, or to OTLP bytes. But, I was just trying to imagine, is it possible to do fan-out without cloning? And the answer is maybe, but why? I don't know if it's useful, but, You could imagine Because in the model of the hotel collector, like, the exporters are not supposed to modify the data, so if we can enforce that somehow, then that'll help.
Exporters or processors modify data, exporters push data. So, you could imagine a fan-out, as long as there are no mutators between the fan-out and the exporter, then the fan-out sends it to exporter 1, exporter 1 hands it back when it's done.
Pin out to Exporter 2, hands it back when it's done.
Export 3, hands it back when it's done. As long as no one modifies the data when they're exporting, then that'll work, and there's no cloning needed. I don't think this is super important, but I'm talking about it because I want to make sure I understand the concepts. I also have to admit.
below the level of the OTAP records, I'm not sure I fully understand the consequences. I know that there are arcs inside of the OTEL… the arrow data structures. I know I can clone them, and that they save references, and that I'm not that there's no danger of mutation. The copies aren't write and so on happen. But I, So that tells me that it shouldn't cost me very much to clone, and I shouldn't have this conversation that I'm having.
Laurent Quérel 00:41:18 Well, that's defensive either.
design decision, we… We, we have, art… On every Apache Arrow Records.
And the second property that we have is that it's impossible to update NRO records in place.
So there is no mutation. You can create a new PDATA with new Apache RO records.
So the… that means that… If you have a reference to a P data, you are sure that it will not change in the future.
If… and if you want to fan out and clone DC data in multiple destinations.
Again, that will be… A very, very lightweight, operation.
JM Joshua MacDonald 00:42:10 It's a… Bytes, we're gonna clone a vector.
albertlockett 00:42:14 Yeah, we should…
Laurent Quérel 00:42:14 I think we should, yes.
albertlockett 00:42:17 I was gonna say we should maybe… maybe we should change the implementation of OTLP bytes to be an ARCVEC.
Instead of just, like, the VEC being contained right inside the, Inside that enum, that would… that would definitely help.
Laurent Quérel 00:42:32 Yeah, I agree.
JM Joshua MacDonald 00:42:35 I think I understand. I was just bringing up the code where here's where, you know, we call notify ACK or Notify NAC, There's nothing preventing me from modifying this data right here.
Like, I could… I can create a new P data and return the different P data, that would be the wrong thing to do.
But it goes back here.
Anyway, I… I'm glad that we had the conversation. I have been wondering about the asymmetry of, like, it's a VEC if it's bytes, and then we're gonna clone it.
And I just spent at least a few minutes telling… talking about a way we could avoid cloning, but I'd rather not, and that sounds like maybe we could think about putting an arc there, so thank you.
Laurent Quérel 00:43:15 Yeah, I definitely agree. Could you, Could you, Evil, if you have to redact it a little bit, put into your, GitHub issue, or getting the fan out.
the example of a GoCollector YAML configuration file that you'd like to support?
Just to make sure that we have a reference on what is the target, what we need to emulate.
Or at least to support semantically, even if it's not exactly done the same way.
Yeah. But, I think the treatment.
JM Joshua MacDonald 00:43:55 I think I can. I realize I don't actually have it. I know… I know the concept, I don't know the specifics, but I believe is that customers are given this feature, like, you can have multiple pipelines, you can have your syslog receiver go in two directions immediately by going to two pipelines, and that's the basic.
Laurent Quérel 00:44:10 Okay.
Okay.
JM Joshua MacDonald 00:44:13 But I can… I can work on, you know, whether we have mutable or not mutable, like, I actually… it's always concerned me that the order is out of control. Like, the… the… There's no way as a configuration in the collector to say which fanout you want to happen first. It's just not possible. It's like a…
Laurent Quérel 00:44:30 Always, always sequential.
JM Joshua MacDonald 00:44:34 It's always sequential, it always does all of them, it always joins the errors, so…
Laurent Quérel 00:44:40 Yeah, you can… we… okay.
You're having a situation where, The first pipeline that is into the second, fail.
And, and impact all the other pipelines, in fact, right?
JM Joshua MacDonald 00:44:57 No, they will see the same data and have their own chance, although the timeout could happen, so time doesn't.
Laurent Quérel 00:45:05 Yeah, but when I say impact, so that you will slow down.
All the other branches, all the other.
JM Joshua MacDonald 00:45:11 Yeah, yeah, yeah, that is the deep trust for me.
Laurent Quérel 00:45:13 The first one is much slower, or not responding properly.
JM Joshua MacDonald 00:45:18 So, I would… what I would like to do would be a more general sort of connector that almost could be the same as failover. It doesn't have to be, but could be almost, where you have a few knobs, which is, like, how much concurrency do you… would you like? Full concurrency, limited concurrency, or one?
And would you like to exit early on success, or would you like to exit early on failure? And those… that covers a large space, I think, of connector. But I don't know… I don't know.
Laurent Quérel 00:45:47 So we have, I think, a much nicer answer for that in the… The configuration, file that we put in place. We have this concept of, HyperEdge.
JM Joshua MacDonald 00:46:00 Yeah, yeah.
Laurent Quérel 00:46:01 So you have the receiver.
By default, let's say you have just an edge, so a channel connecting to the next, downstream component. But if you have multiple downstream components, so you have an hyper edge, and you can specify the semantic of this hyper edge, or this channel.
And the semantic, so right now, we don't support all the semantic, but the configuration file allows that.
JM Joshua MacDonald 00:46:31 There's a round robin in every outport. Yes, yeah, but we have this concept of dispatch.
Laurent Quérel 00:46:36 strategy.
And that's exactly how to express what you are discussing for now.
So this past strategy, you could decide, okay, it's a round robin, or it's, it's like a broadcast, and we could express also the… the guarantees, that, for example, we… we… what… what we do when… when one of the founders would broadcast, Destination.
failure.
And what will be the impact on the other, destinations?
do we want to minimize the impact of one on all the others, or do we want to make sure that everything is synchronized in some way? So that's something that's… is a load in terms of configuration, but not yet fully implemented into the engine. And I think that's, In my opinion, the right way to go.
But we can definitely discuss that. So it's not involving, really, a specialized processor or specialized component. It's more at the connection level between those systems.
And the nice way of… if we follow this way, we can… we can replicate that at any level into the pipeline that will work similarly, which is really nice, in my opinion, because it's not only on the receiver side, it's also on the exporter side. It's also interesting, for example, for the fallouts, for the fallback into the failover processor, and so on.
So, yeah, that's my answer. Not yet implemented.
JM Joshua MacDonald 00:48:12 I see, a little bit… I'm gonna have to study this a bit more, and consult with you before any… any work imagined on the fan-out processor. Sounds like fan-out processor, much like the Go Collector, is almost a hidden component, like, it's part of the HyperEdge implementation, is you can… you can fan out with various policies.
Laurent Quérel 00:48:33 And that will be very explicit for us. That will be directly visible in the configuration.
JM Joshua MacDonald 00:48:38 I'm gonna write that. Cool.
Okay, I don't wanna… Dictate what we do for the next 10 minutes of meeting time.
Does anybody have an urgent feeling?
I see.
Laurent Quérel 00:49:07 I think we can discuss, I think RESTful chat. Everyone is aware of that, so I don't want to, To do that, necessarily. Maybe, we can just talk with, with you.
Regarding the KQL, exploration that we are doing.
JM Joshua MacDonald 00:49:24 Sure. That sounds good. Drew dropped off, none of my team, direct team are here, but I can tell you what I had picked up just from feeling around after you talked to me about it.
This week.
So… So, I'm speaking to an audience mostly of F5, but I see Jake's here, so you're gonna… you can hear what I have to say on this topic of KQL.
We started this effort that you see, that Drew and Blanche have been working on, And Riley kicked it off, so it's his vision that we've been following a bit. And, he, from the beginning, talked about, like, intermediate language, referring to, like, how LLVM created a whole space where it's optimizing generation of code, but it's not choosing your language for you, and there are many languages that target LLVM.
Laurent Quérel 00:50:18 Yeah, we totally align with that.
JM Joshua MacDonald 00:50:20 So the idea of an intermediate representation, logical representation for OpenTelemetry data that we can then apply queries to seems natural, and I'm starting to sense that you guys have even gone even further on this, which is to say that, and I've heard you say a few times, what we need is a view.
A view that logically joins together the attributes, the resource attributes, the scope attributes, and the thing, or the record.
And then, the, the… to me, the intermediate representation is forming up to be data fusion queries over that model, essentially. So, data fusion logical plans is the intermediate representation of… this. I like it, and I just wanted to be very clear, we do not have religion about KQL, except that we… Users like it for logs, and we expect to keep doing that.
Also, KQL is clearly a general-purpose language, it's used for database queries, it's used for all kinds of stuff that's not OpenTeometry, and we recognize that. So it's not always going to be perfect, and I think you've got some thinking about, sort of, more appropriate stuff that's dedicated to OpenTeometry.
For me, I hope we talk about metrics, but go ahead. One day we're going to talk about metrics.
But I'd like.
Laurent Quérel 00:51:35 Albert, do you want to, do you want to talk about what we did together?
albertlockett 00:51:43 Sorry, was there a question for me?
Laurent Quérel 00:51:46 What'd you say, Albert, I didn't hear you well?
albertlockett 00:51:49 I said, who was that question directed at? Was it directed at me?
Laurent Quérel 00:51:53 Yeah, because I was either thinking presenting what we did, or you can present, so I was suggesting, if you want to present, up to you.
albertlockett 00:52:03 Oh, yeah, sure. Let me, let me… I'll pull up the documents. So, what Laurent and I started to put together… Was this document that starts to define, a query language that is inspired by KQL, and sort of takes some inspiration from OTTL. And so we can see that, in general, We have, a KQL-like syntax that starts where you identify, okay, here's the signal I'm going to be processing, and this defines, The signal that you choose defines, like, what are the… what are, like, the valid identifiers that you can use in the query, but also which signal we apply the pipeline to. And then, so we've gone through and listed the valid identifiers for each, type of signal, and these are inspired by the OTTL contexts, And then, what we kind of said was, like, we'll use some of the KQL, operators that we can use to apply to, the signals. So you can see we've got extend for setting values.
Project Away and Project Rename for operating on maps, which we thought would be, very useful for, for, like, modifying attributes and whatnot. And then, we kind of said, you know, maybe for metrics, we'll try to align on, what are the specific, you know, operators that we could use that are, like, that can modify metrics.
And then we tried to list out a bunch of functions that we think You could apply to, one of these, one of these fields to modify them, and these are inspired by, the, the kind of, like, what's available in OTTL, basically.
So if I go down… actually, I'll scroll down to the bottom here, and then we can look at some of, like, the example… queries?
Laurent Quérel 00:54:23 So, just before that, we have those destination examples, I think that's, Yeah, destination output port, so…
albertlockett 00:54:30 Yeah. So, yeah, the other thing that we wanted to do here was to try to figure out, a KQL operator that we could use to, to route data.
route to an output port, so we've got route 2, and then output port here. And then I think one of, like, the more interesting things that Laura and I are trying to figure out is how do you write this pipeline in a way that can, route data conditionally. And so, for example, one of the ideas we've been toying with is this split buy operator that has conditions that match to the data, and then pipelines for each, matching condition.
And then, so you can see that, like, what this is trying to say is, for higher severities, route to this output port. For medium severities, route to this other.
output port would be the motivation behind something like this. Again, we're still trying to figure out the syntax for this. We've been kind of, like, brainstorming. Another example was to have Kind of an if-else sort of statement for that.
But, you know, the motive… like, just to call out here that, like, one of the motivations is to be able to not only transform data, but use it in a way where you could maybe say, at least in the OTAP world, hey, we want to send this down this pipeline or this pipeline, depending on, like, some conditions.
And then, we've also been trying to figure out how we handle nested lists.
So, how do we apply a pipeline to, say, like, a nested list type, like span events, or span links, or, metric data points, for example.
So you can see we've been kind of brainstorming some ideas here about an apply operator that applies to the nested type, or maybe an any operator or an all operator that you could use to filter the parent type by the child type. Again, these aren't set in stone, this is just kind of our brainstorming.
and then we… what I tried to do was to call out, like, what are all the things that you would want to do with… with, like, OTTL generally, and then, like.
rewrite it using this syntax, and so you can see that we've tried to spell out a bunch of different, types of operations. How do you filter by fields using a logical expression? How do you invert those logical expressions? How would you use, say, functions in your expressions to transform the data. For example, if you're working with time, would be, very common.
How do you filter by attributes?
And then as well, trying to figure out how we do transformations. So, how do you set fields using extend?
How do you set fields from… The… a source that might be attributes.
setting an attribute from the source of another attribute, and then, and then how do we transform maps? How do we delete keys? How do we rename keys? And things like that. So, this is, Anyway, we're almost out of time. I'd rather go through this very fast. This is what Laurent and I have been working on the last two days, trying to just get a bunch of ideas down on paper, for this.
For this.
OpenTelemetry transform language that is inspired by KQL, inspired by OTTL, but it's, like, kind of purposely built for, processing hotel data in, in, in streams.
Laurent Quérel 00:58:31 Can you move back to the very beginning of the document?
I think for the conclusion that we'll be… we, we.
albertlockett 00:58:39 We've put a bunch of principled guidelines at the beginning of this document that guide us.
Laurent Quérel 00:58:45 And I think that's very important to have some kind of, agreement between us to make sure that those principles are, acceptable for everyone.
like you said, I think we… KQL is a pipeline-oriented language, easy to understand.
following a form of classic logic for people, as opposed to SQL, where you start with the projection, and then you have the form.
the KQL, you have the source, and then you apply sense transformation. So it's… it's more natural. But, the… I think what is important also is to recognize that the standard KQL comes with some limitation, and we want to make sure that we will optimize the experience for open telemetry users.
First.
And, that's why the data model, reusing the convention used by OTTL, looks interesting.
And we want those identifiers very easy to express. And we don't want to have this, square bracket, between double cut, and then you have, things like, log.sources.attributes, blah blah, because it's super, annoying to do, so just having stripe the logs.
Processors that attribute something.
Oh, look, those are foods, sorry.
So that's one thing. The other very important thing is making sure that we can't create invalid signal with any pipeline.
So, we know that the input of a stream is necessarily a valid signal, open telemetry, and the output should, and we must guarantee that it's a valid… so it's not a general purpose pipeline language. It's a… it's an open telemetry processing language, and with the property of making sure that nothing is invalid for the output.
So we can't generate a JSON document with this thing.
And that's fundamental, because this KQL, or let's say, OPL processor.
will be anywhere into the pipeline, and obviously, because we have an OTAP, engine.
before it's a tap, after it's a tap. That's basically the reason why we have that. The next one is… All the operators that we have into this pipeline language.
they will… Logically or semantically, they will act per row, or… Bill bitch.
But there is nothing in this first iteration of the OPL language, That is across, batches.
Or even across, let's say, a pipeline runtime, or across multiple servers.
That could be extended at some point with a more complicated solution.
But we don't target that in this iteration.
That prevents us, to implement some very nice, operators, for example, on metric.
We could do aggregation, but per batch.
And I have the feeling that there are some aggregation operator into the transform processor, into the GoCollector.
That are most likely, following the same constraint without seeing it.
Because basically, if you… if you have multiple instances of your GoCollector, what happens with some of those operators in terms of result? They… they're not… they don't share anything, so they will end up with some… potential issues.
JM Joshua MacDonald 01:02:33 Yeah.
Laurent Quérel 01:02:34 And.
JM Joshua MacDonald 01:02:35 what I call time, I am aware of a few issues like that, and I… I, also, you know, we need some sort of time alignment.
critically, and then we'll talk about that, I guess, later. I saw that you listed AUXQL and UQL and stuff, and Those will be exciting topics.
I think we… we should respect the time and, call it. I'll see you all next week.
I'm tempted to continue talking about that topic, but we're out of time.
Laurent Quérel 01:03:10 Okay.
albertlockett 01:03:11 Cheers, Colin.
Laurent Quérel 01:03:12 Thank you, Major.
JM Joshua MacDonald 01:03:12 Alright, see you next time. Bye, everybody.
