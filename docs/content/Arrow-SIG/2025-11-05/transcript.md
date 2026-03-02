SIG: Arrow SIG
Date: 2025-11-05
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/pQC7zIHNF2iTfQI_NR98EEUYdLgRjduN2RgeaKUcaYw_9yMolTXhJRNOTEP6h3cD.Q97XotX9fsLIbNFu
============================================================

## Zoom Recording Transcript

Laurent Querel 00:00:52 Hi, guys!
Chris Hain 00:00:56 Hey, what's up?
Jake Dern 00:01:00 Hey, let's it going?
Laurent Querel 00:01:02 Hi, Jake?
Hey, Jake.
I remember that we had a discussion regarding multivariate metrics, did you…
continue the exploration, after I shared with you the… the…
let's say the specification I wrote, or the draft of the specification I wrote regarding,
multivariate matrix support for Apache Arrow, for Whatapp?
Jake Dern 00:01:49 Unfortunately not, no. We've been, distracted with other things.
Laurent Querel 00:01:55 Okay.
Jake Dern 00:01:56 But, but yeah, I definitely want to get back to it at some point.
I did look over it, and I think I've mentioned to you previously that, like, we have tons of metrics that are, like, already in, like, multivariate form. And actually, most of the exploration I was doing was.
Laurent Querel 00:02:11 How bad it would be to…
Jake Dern 00:02:13 Like, transform them the other way, and make them a single variant, and what the cost was going to be.
Laurent Querel 00:02:19 Yeah, weekend.
Ej, Josh.
Joshua MacDonald 00:02:31 Hi.
Laurent Querel 00:02:31 Are you able to drive the meeting?
Joshua MacDonald 00:02:33 Well, sure.
Let's see, yes, I will pull up the notes, and then the issues, and we'll go from there.
I'm bringing in some people from my team, and they're finding the meeting. While we do, here comes the notes.
Laurent Querel 00:03:19 I'm just creating the section, the new section, into the document to…
Joshua MacDonald 00:03:24 True.
Laurent Querel 00:03:26 I'm not sure who is there today?
So we have Chris, Jake, Albert,
Oh, we have plenty of people, so I will just, let people update the… their name…
Joshua MacDonald 00:03:49 Thank you. Everyone, feel free to add yourself,
you're all welcome to edit this document. So we usually start with the issues, and discuss briefly the new ones since the last time. So the last time is a shorter time.
And we missed all of you.
F5 people last week for your wellness day, so actually we could go back a bit further.
So… I would bring us back at least to,
the, last four of these items… sorry.
For discussion. As we do our issue triage. So here we go,
I had asked about releasing crates, the OTAP data flow crates, the answer was not yet. I'm going to be doing some work on that. You'll see my PR is trying to consolidate and clean up the OTO Arrow Rust code.
So, that's underway.
Albert filed one here, and I will see what I remember about it.
Albert Lockett 00:04:58 Oh, I can talk to… I can speak to it, Josh, if you want me to. This is so… in, 1341, we added the new, filter processor, and internally, this calls a function logFilterNew, which takes these log match properties.
That have an include and exclude. And, then what we do internally is we just
Kind of go through… Those two sets of filters, and then figure out, okay, what are the rows
in the… I guess in this case, it's log, so log record batches. We keep the log, so we want to exclude, and then we intersect those, and so…
first off, this issue that I opened is just trying to say, like, if you're just looking to build a filter that's like, oh, I only want to include this, or I only want to exclude this, then it doesn't make sense for us to, go through and do all that work to figure out,
like, to basically check the filter both ways and then intersect them, we can shortcut one side or the other, depending on if there's no include or exclude filters. And it also…
kind of, you know, so we get that performance benefit, it also kind of maybe fixes a bug where if you do just supply, like, a completely empty one of those log match properties to either side, include or exclude, like, you just get back no results, so…
Joshua MacDonald 00:06:20 Got it.
Albert Lockett 00:06:20 This is trying to… trying to kind of fix the bug and improve performance at the same time. And
Yeah, so Chanley on our team, who worked on the original filter stuff, he's been on PTO for a little bit, but I think that maybe once he's back, we can try to get him to have a look at this one.
Thank you.
Laurent Querel 00:06:41 Additional context to that, so we have this milestone for end of December.
Joshua MacDonald 00:06:48 And, the…
Laurent Querel 00:06:50 Filter processor was there, because we think that we will not be able to deliver
the OPL processor, which is a much
a more advanced capability that will leverage the diffusion, so the filter processor is like a baby version of the filtering capability that OPL will be able to support.
Joshua MacDonald 00:07:13 Gotcha. I…
would move on with the issues, and I just realized it would be sort of, I should… I should stop for a moment and recognize a bunch of new participants. Many of them are from my team, and I don't want to put any of you on the spot, but I just wanted to say hello to Aaron and Andres and Mark.
And Jaime, I know many of you have sort of been here before, but I just wanted to thank you all for joining again.
And if you have something that you would like to speak… to say… to speak about any of the ones I… any of you here, feel free to open the document link and put an agenda item for, you know, 5 or 10 minutes from now, and we will… we will come around and say hello to all of you.
Well, actually, so two of you came off mute video, and I'd like to say hello to Andres and Aaron, who are both here today, since they're showing their faces. Hello, Aaron and Andres.
Thank you. Okay. Well, I didn't actually unshare my screen, so you maybe saw very tiny versions of those people, and
Oh, my video. Oh, my video. Okay.
Coming back to the, issue triage, I… filed an issue here.
Where I, had been studying the batch processing code, and I described this to Laurent already once today. I have not filed a PR. I did work up a design document, but I looked at it again this afternoon, and I thought, it's not quite ready to share. But I did file this issue yesterday morning to kind of capture what I had…
been thinking about the previous week.
In the Go Collector, a batch… the batch processor has sort of a minimum and a maximum size.
And the maximum size is, like, always an option.
you may not have no maximum. And in kind of reality for us, when you have an OTAP records batch, you've got a upper bound, which is some sort of limit on the width of your integer. So, like, if it's U16, it means, like, there's actually really always an upper bound as well as a lower bound for batching purposes.
the… the…
But I like to see that a batch processor is both capable of splitting and combining records in order to find those batch sizes. The existing code, I was not absolutely convinced it was correct, and also there's a bug that was opened a couple weeks ago.
Actually…
I didn't link to that bug here in this issue, but there is another open issue from two weeks ago that's, like, there's an ignored test because there's a bug in the batch processor. So I've been looking at that myself, and I just sort of wanted to file this.
to, sort of, some of the features that I think we should have for a batch processor, I've summarized here.
These are going to be sort of optional features, is the way I see it. So, like, if you'd like to deduplicate your resource or your scope attributes, that should be possible. It's not required, you could just sort of concatenate batches, but you can also concatenate and deduplicate.
And something I'm thinking about, at least for, a batch processor.
Other things that I've seen batch processors do in the past is to sort by trace ID, or by hash of a trace ID. This is in order to sort of get locality in your trace ID set, so that if you have, let's say, 10,000 batches entering, and you want to split it into
2,500 batch outputs, you'd get 4 outputs, and if you've sorted them in some particular way, you're going to get fewer of those in the batch, and that's something that people have
asked me for in a batch processor before.
And that's about it.
this is not to say that the existing code is horribly broken, but if I was being asked to maintain it, I would start making some changes, which started to feel like starting from scratch. So, I just wrote this issue to say so.
Would anyone like to comment on my statements about batch processing?
Laurent Querel 00:11:19 No, only on the maximum, I think,
We obviously need a maximum, just to avoid the out-of-memory, for example.
So that's strange that in the GoCollector, we don't have that, but,
I think we need, I can understand that we don't necessarily have a,
Let's say we could imagine a soft limit and a hard limit.
Something like that.
Joshua MacDonald 00:11:49 That's right. That is actually the way the Go logic works. There's sort of a minimum effective size. If you… if you have less than that, you won't produce a batch. And then there's a maximum. If you have more than that, you'll split. But the maximum's usually optional, and I would say that usually… in our case, the maximum is not necessarily optional. Like, there's always some upper bound.
So my point is to say that I think the code that we have today gave me a lot of inspiration, a lot to work with, but
I couldn't quite figure out how to become the owner of it without restructuring it. So, that's where we are.
Laurent Querel 00:12:25 Okay.
Joshua MacDonald 00:12:25 And I will have a lot more to say on this.
I've already started on this task. This is, like, before we release our crates, we need to clean up some of the, sort of.
separation between the crates. I've just been working on that. By the way, I noticed how our Clippy requirements are much stronger in OTAP Dataflow. So it's working. The OTAP Dataflow being our sort of higher quality set of crates. To move code in there, I'm having to
Fixed stuff, so it's good.
Laurent Querel 00:13:00 Yeah. So just to make sure that we are on the same page, so the goal here will be to merge the Hotel Arrow REST modules into the OTAP data flow.
So we, at the end, we will just have the experiment tall.
and the OTAP data flow, and maybe at some point, the experimental will be merged again.
Into the, hotel barrel, right?
Joshua MacDonald 00:13:29 That's right. I would say we can remove it. I… I don't think it was ever…
Well, it was published on crates.io. I don't know if there's a deprecation process or, like, a stub that we leave in place that refers, and there will be a few issues coming up. For one thing I just noticed, for example, the old code, and this is a good sort of topic right here, the old code had,
procedural macro, attribute macros to allow you to configure features, like, for server-only or client-only, if you wanted to be a…
to only support the server-side gRPC, you would only build that set of dependencies.
that's an example of something that I'm not sure we really want to keep, and so I don't know about maintenance for the old packages, but yes, we want to arrive at the place where all of our crates are underneath OTHAP Dataflow.
Laurent Querel 00:14:24 So… so we have already, some… some crates that are published on crates.io?
Joshua MacDonald 00:14:30 I don't know, actually, maybe I'm wrong about that.
Laurent Querel 00:14:36 Yeah, I don't think we have, but.
Joshua MacDonald 00:14:38 Good. So, there's no real compatibility problem. I don't think we're breaking anybody by moving this stuff.
Does that sound okay?
Laurent Querel 00:14:50 Yep.
Joshua MacDonald 00:14:51 And my high-level idea was to take it sort of step-by-step.
Well, it's kind of hard to do, honestly. The first thing I was doing was to consolidate the generated code, so Pro Syntonic are used twice right now, and I was going to move them. So my idea is basically to move some things up from OTel Arrow Rust into the OTAP DFP data crate.
and then move some stuff down from the OTAP
DF, OTAP create, like, the P data structures, the OTAP
PData objects. They can move down to PData. Everything will arrive in the same place.
And so there'll be a little bit of consult flattening of the nesting structure. So right now, Otel Aero Rust has a…
OTLP, and then it has a PData OTLP. I'm gonna flatten that into one OTLP subdirectory.
Anybody has work in flight there, they want to, like, wave their hands and I can slow down. Like, I don't want to bomb a big PR if you have one, so let me know. I'll slow down. But I would like to clean it all up, and I would take it, sort of.
as much as possible, piece by piece, so that I can understand each piece of code and make sure it looks nice and neat, and there's not duplication.
Laurent Querel 00:16:10 So, Joshua, question for you, because I think,
I asked, basically, Albert to work on the finalization of the metric.
So most likely, he will have some… Could,
Yeah, collision with what you are doing. So, when do you think that, in order to minimize the merge effort.
What is your, your plan.
Joshua MacDonald 00:16:39 Yeah, that's a really good question. So I was sort of hesitating to say, I wish I could just do this piece by piece, but the circularity of it is a little challenging.
I was thinking…
there is a more aggressive way to go here, where we just get the pain behind us. Right now, I have a PR open to move the… as I said, the protocol to consolidate just that stuff.
I think I could do the subsequent move in one step.
Where I would just move all of the rest of the code, I would probably change some of the path structure, and I would have to change a lot of use statements. But it wouldn't be too bad, I think.
If that sounds okay, I might be able to do that, like.
I'll send out a PR right, like, basically right now for the proto names, and then tomorrow.
If that works, But also,
I can… I can work around you, Albert, if… if… I'm sure we can figure this out.
Albert Lockett 00:17:36 I mean, I can work around you, too, and so… Like…
Yeah, I would say just proceed, however.
However makes sense for you, based on… What you, like…
what you think is best, and I can probably figure out, like, where to…
Where to add my changes, because, like, really…
I'm just gonna be adding changes in the, PData OTLP bytes.
like, pack… or module, so that's… it's pretty contained, I'm not gonna be touching a bunch of stuff, and I imagine that you'll probably be moving, like… like, OTLP bytes, traces, no TLP bytes, logs, and common, like, into some directory, so I can just take my metrics module and stick it there, and…
Joshua MacDonald 00:18:31 Sounds about right.
Albert Lockett 00:18:32 theoretically just work, yeah, so it should be pretty… like, there might be conflict, but I think it'll just be, like, scoped to one module, and it should be pretty easy for me to, to fix it.
Joshua MacDonald 00:18:42 Cool.
If there's any dead code or any kind of organizational defects that you're aware of, please let me know, because that's the kind of stuff I'm trying to catch right now. Like, something doesn't make sense, I'd like to fix it.
As we move it, maybe.
So, nothing is too small to consider. As an example, like, I think the convention is to name things ending in macros when they have your macros in them. Like, I had named something derive. It doesn't make sense, like, whatever. Conventions that we want to follow, just let me know if you think of any.
Alright.
Well, thank you for the questions. I will take the feedback as we go forward on that.
Well… okay, so we did our issue triage, except almost not really. I want to now introduce Andres,
who is here for my team. And we are here to talk about, and I'm glad that we have Utkarsh as well on the call. I would like us to spend some time talking about the issue and the PR that were opened. I think this is sort of a good place to start with it.
since Andres and I have already spoken today as well, if I may kind of, like, give my own personal introduction to this topic, those of you who know the OpenTelemetry specification for
SDK is no… it's got a long, like, 5-year, 6-year history now of saying what an SDK is, how it works, how you instrument through the APIs, but how you construct the SDK, and what features the SDK has. The Go Collector
And the Go SDK and OpenTelemetry both Implement this thing called… A configuration model.
standard is, and the SDK has a feature called views that are meant for letting SDKs control their metrics, especially.
When Andres opened the PR, he and I spoke about it. There's a PR and an issue here.
the question was sort of, like, immediately, like, make… from an OpenTelemetry perspective, a question that arises is, why don't we follow the model? The same… we can use exactly the same configuration model that the Go Collector uses for its SDK,
If we follow the model. However, here's my other side of my feedback. I don't love the model much. I don't really love views, even though I've implemented them, because they are really complicated. So, in some sense, I do see where Andres is coming from. I hope that's a good introduction. Andres, would you like to talk about the issue you felt?
Andres Borja 00:21:20 Yeah, thank you.
So…
Yeah, I also worked with the views in the past, and I felt like they were, like, kind of, like.
Working on top of what was implemented before, so… so it was a little hard to…
to differentiate them, why they need to be treated as a separate thing, so…
what I'm proposing is… is trying to
model the internal telemetry just similar to what… how we modeled the other telemetry, right? So… what,
prototyping in my PR is basically adding this,
block, I… the last one, I renamed it, it's not part of the settings, but it's part of the service, so it's kind of similar to the…
to do the telemetry. But, it basically…
users will be able to add processors and exporters, right? The processor will behave in a similar way in Acting sequence.
And the exporters will be, okay.
Like, as a van out, if you have two or more.
In this way, we can, you know, treat the telemetry, the internal telemetry, similar to what we do with other telemetry. It's not the same processors, it's not the same exporters, because they run in a different way, and they have more overhead. These are more like…
Basic processors and…
And it's a set of them. It's not like any processor, right? It's just a set of processors that we might be offering for internal telemetry.
that…
the specific use case that I'm willing to implement after this kind of, like, framework is in place is…
is the different exporters. I'm putting an example there of Prometheus. It's an exporter that we cannot, but some others that I started with the logging, which is basically just logging the metrics to…
You know, to the standard output. And then as processors, We can…
modify the metrics, the specific use case that I'm more interested in actually renaming the… the metrics.
We have today a custom SDK and a custom API, because this is multivariate.
So it's not that we can just reuse, we still need to implement.
some engine for that in terms of telemetry.
Laurent Querel 00:24:05 I haven't… One question, and one,
one comment. So the… the question is, just… just to make sure I understand the…
What we are trying to achieve.
Are we trying to add… to the existing, OTAP engine.
A way to export internal telemetry.
via OTLP, or any kind of exporter supported by the…
the existing ROS Client. ROSE Client SDK?
Andres Borja 00:24:43 Yes, so…
Yes, but it's not the same exporters, you know, because it's an internal telemetry exporters, it's not the same exporters that we offer as part of the
general pipelines.
Laurent Querel 00:24:57 Yeah, the exporters, so you are talking about the, in that case, the exporters.
Supported by the REST client SDK, right?
Joshua MacDonald 00:25:09 I think that… I think this is, the… the big question. Like, we have an exist… we have…
several choices here, and to me, it seems like there's a choice. Well, we could… and Laurent, part of the context here is that you elected to kind of break outside the box already, like, and sort of bypass the OTEL SDK, so now we're on a slippery slope. That's part of what we're talking about here.
And so… Because these metric events arrive somewhat aggregated already in the admin
core, I guess, doing the work of potentially a Prometheus export. There's a temptation now to continue on that slippery slope and bypass
something. So, either we're bypassing the use of the OTel SDK, or we're bypassing use of the OTAP data flow pipeline.
My goal is not to bypass both of those, like.
either would come into the OTAP Dataflow pipeline and use the same OTLP exporter as we have.
Or we'd go into the OTL Rust SDK and use its OTLP exporter. But if we're saying that we need a third OTLP exporter.
the flags are waving for me, and that's kind of the feedback I have.
I do wonder if, Utkarsh, if you have a position or you'd like to speak, because, I mean, this is sort of hotel nerd stuff here, right? But the Metrics SDK has both asynchronous and synchronous instruments, and when we think about transferring metric observations that we already made.
through a bunch of channels that we control ourselves, and then producing them, it's the asynchronous model, where the OTEL SDK is going to be observing our pre-aggregated numbers
some level, the OTEL SDK is just re-aggregating stuff that we've already aggregated once. We don't necessarily need it. Prometheus is really simple.
But I don't want to implement another exporter.
Udkarsh, what do you think?
utpilla 00:27:05 Yeah, I think this, kind of goes back to the question I asked in, I think, the SIG last time, or the one before that.
Because…
like, the easiest thing for us to do is, like, whatever internal metrics SDK implementation Laurent has put in place.
We just take those aggregated metrics, translate them into something that
or model them using what Rust SDK expects. So, like, if you have a multivariate metrics with 5 different metrics.
Maybe we will have 5 async instruments.
based on the Rust client SDK, and then we export it. And the benefit of doing that is that we already have views, all the kind of… all the kinds of processing that you would possibly do on Metrix is already there in the Rust SDK.
It's the easiest and the simplest way to do things, and I'm… I…
I'm, like, I think I'm… I prefer that approach, but unless…
And also, another reason I feel that is okay is because, it's not a puff-heavy scenario. That's not the hard path for us.
So it's okay to have the metrics, the final aggregated metrics, again get collected or aggregated by the metrics SDK.
Yeah, those are my two things. Simplicity and performance not being a major concern. I think for that, I would prefer that we just use Metrix SDK. But yeah, I mean, we could also just
create a parallel SDK if we really wanted to, but…
I think that's more maintenance, and also, it's kind of, like, we could prioritize other work instead of doing that, but…
Yeah.
Laurent Querel 00:28:45 I'd like to propose something,
I think I agree with what you said, Utkarsh.
With one, so… Short term, medium term, I think I totally agree.
Because we, like you said, we also have some other priorities, and we will have a better use of this time to consolidate the OTAP engine and do this, for example, OPL support language.
Which would be a very nice addition.
On the consolidation of the engine itself.
But…
So if there is, and I think there is an easy path to integrate the Client SDK and get, back
telemetry, internal telemetry for metrics, even for event, and potentially for span. I think we should go there. I will not personally spend too much time on the…
the configuration part of this thing. If we can reuse directly what the client SDK is providing, perfect.
Because, in my opinion, long-term, I will…
find very cool and very useful, if we can reuse the OTAP engine at some point.
as a way to accelerate the reporting, because this OTAP engine supports both the TLP and OTAP, which is not the case for the client SDK.
So, once we have a more, mature
And when we have more time to dedicate for a new kind of client SDK, I think we should be able to replace this existing client SDK inside the REST engine, in my opinion, in order to support
both and efficiently OTLP and OTAP.
And potentially, also leverage the,
OPL language on which we, we like to,
to work, because you can imagine that, the OPL, Exclusiveness…
That we will get, from this new processing language will be, excellent even for internal telemetry.
utpilla 00:31:31 And I think, yeah, just one, like, short term, again, if we also want the ability to export it in OTAP, like, through Arrow, then…
So, again, the hacky or, like, a quick fix thing would be to, like, go to the SDK repo, like, the contrib repo, and add a OTAP exporter for the SDK.
So that way, at least, we have the capability to export in both formats.
Andres Borja 00:31:59 So, my kind of, like, rational when I was thinking on function today is two, actually. One is that I just don't feel like…
Like, right to include the…
the existing SDK, like, it's like, we already have an SDK internally, we already have an API that is multi-biant, again.
And then, so… So we are doing all these things in a mudbarity than we are.
Kinda like…
transforming it back to something that is supported by the SDK, so it's like the SDK of the SDK. That sounds…
to me, not completely right. Also, the…
the protocols, you know, in this case, for example, ARO, we don't have any support for that. We can do it natively, right? So it doesn't sound like, right, either, like this.
The collector that is implemented using different protocols is now
Using internal… for its internal telemetry.
something that is not native, you know? It's, that's kind of like…
like, my rationale behind. Adding this extra layer, yes, it's not hot, but… But is it still…
I just feel like we can do better, you know? The implementation of the views, for example, for the particular or specific use case that I'm thinking, it feels more like,
Something that is added after it was designed or implemented, you know?
So…
That's the part that I'm not completely… I mean, I don't… I feel like there are better… there might be better ways to describe transformations in the telemetry.
And that… that is the way…
is expressed in the use cases, right, by adding processors, for example, you know? Adding this extra processor that is not called processor per view doesn't seem like, like.
Like, write to me.
Joshua MacDonald 00:34:12 At some level, this… this becomes a, essentially,
sort of case against the OpenTelemetry metric view SDK Views design.
I… I wouldn't say it was added after, but it was… and I was… but I was there dragging my feet at the beginning, and what I would say is that it was an unproven design that was, like.
hypothetical from the OpenCensus system, was like, we will have a thing called views, and then OpenTelemetry merged with OpenTracing, and therefore we will have a thing called views, and we kept having a thing called views until someone wrote it down.
who happens to be Riley, which is, like, many of our managers, actually wrote this down, and hence we have this thing called views, and it demonstrates a lot of the mechanism that we know and love about metric SDKs. Like, if you're going to remove some attributes, you have to remove them
at the point of contact, or else you have a complicated aggregation problem. And the cool thing about SDKs is they have the simple path. You just…
combine all your observations into one counter if you're dropping attributes. But if you have those metric observations as OTLP data later in the pipeline, it's way harder to do. So…
So basically, Andres, what I'm… what I'm seeing here amounts to, like, OpenTelemetry Metrics Views 2.0.
Or something along those lines, and if… if you hold your ground on that, you can… you can… the point is that people are going to criticize us if we don't have a position, and the position is we don't like OpenTelemetry metric SDK views, and we've designed a new configuration for a new type of view configuration.
One thing you could do to prove that you understand and accept the past while not loving it is to actually take this configuration here, I mean to say.
this… Pipeline-oriented model, where you have
producers, which are the SDK scopes, in my opinion. You have pipelines, which do things like drop and add, you know, extend and drop and so on. And then you have exporters, which we understand.
you could take this, essentially, graph of configuration object, analyze it, and come out with a view configuration. You could then go set up the OTel Rust SDK with a view.
User never sees that config, you had to learn it once to prove that you could, but really you're saying this is Views 2.0, we can compile it down into views, but we don't like those anymore. Something like that.
utpilla 00:36:37 And I have another point, here that I feel like if the metrics SDK spec and everything, even the implementations have been out there for a long time, so…
if I have some custom proprietary backend to send the OpenLeetry metrics to, then…
like, right now, I know that that's the contract that I have to, implement.
So now, if we want to do a parallel internal SDK ourselves, then…
if I want my, then I'm kind of looking at…
I don't know, like, implementing two exporters, one for the regular SDK, and then one for the internal SDK to send data to my proprietary backend, which…
I'm not sure if that's the best user experience, so you…
Also, you already have a lot of exporters available, for the Metrics SDK, so…
You can reuse them. You don't have to, like, ask people to, like, come and implement something for the internal one again.
Joshua MacDonald 00:37:35 And getting back to the slippery slope of this, if I may, it's like, Prometheus is really easy.
Frankly. I mean, it's just a simple protocol.
It's just text. So, if you're just implementing a Prometheus exporter.
you're, like, you've got, I don't know, I'm gonna say 100 lines of code, it's not that little, but it's, like, not a lot.
And you've bypassed this whole SDK, which looks complicated, has this antique thing called views, but…
as soon as you get into the OTLP, now you're starting to replicate things that we already have that are not simple, like calling a gRPC client.
with an OTLP protobuf object.
So…
And what you're saying, Ukarsh, is that, like, we also have, like, this long list of some other bunch of exporters that.
utpilla 00:38:26 EW, yeah.
Joshua MacDonald 00:38:28 Stuff like that, yeah.
Laurent Querel 00:38:30 My concern, josh is the following.
I'm afraid of having, like, so…
Let's imagine that we have two, two,
A short-term version and a long-term version.
And let's see what will be the most logical or the most natural
Or the minimal effort to reach the long-term goal.
So…
on one side, we can consider that we integrate a client SDK that already exists, that we consider maybe not perfect for the concepts that are inside, like the view, like you mentioned.
But that already exists.
And, the other one is to introduce
This configuration that is more pipeline-oriented.
But which is not, in fact, the pipeline system that we use in the collector.
And that's where I have a concern, because then we… it's very, I mean, it's like we have multiple types of pipelines in the same system, which is not great, in my opinion. So if we want to go to the… to the long-term destination.
And if we have to express the internal telemetry pipeline, ideally, this internal telemetry pipeline needs to be similar to the one that we support for
Users of this system.
Andres Borja 00:40:09 For telemetry in general, not the internal ones.
Laurent Querel 00:40:13 So that's why I have some trouble to…
To… to understand the rational behind…
I mean, I definitely like to have a pipeline system to express how to export and transform internal metrics or internal events. That I totally agree, but creating a new type of pipeline, I'm not sure I agree with that.
Andres Borja 00:40:39 So… Two things that you mentioned. So, the first is…
that exists. So, not completely. There's a reason why we implemented an internal SDK, an internal API, actually.
Because it's not completely aligned with the current… with existing Rust SDK. So, it exists, partially, not specifically for the use case. So, if we want to use it, we still need to implement this
bridge between the internal SDK and the…
In the last Autel SDK, right? So…
It doesn't really exist completely, that's one thing.
The… it is confusing, totally agree. It's… it's very similar, that's why I'm not calling it an internal pipeline, I'm calling it actually dispatcher at this point.
is because… I had the same…
and, you know, discussion, and many times, because… because when you say pipeline, you think on the pipeline that we expose with all its robustness, you know, with all the complexities that it has, and synchronization, and message passing, and all those things. This is not that. This is…
Something that processes the internal telemetry that is not the same as the other, because it's a…
As a use case, I would say it's relatively similar. You need to process the data, you need to export it, but as an implementation, it's not the same, because it's more minimalistic. You don't want…
You won, for example.
You don't want the internal processors or the internal components in general, you don't want them to emit telemet, for example, you know?
whether you want in a processor to a metal telemetry, so it can be captured internally. So… so they are not the same.
implementations, right? So…
So I don't even want to call it in pipeline again, because that creates that kind of confusion.
Joshua MacDonald 00:42:43 I can't… I'm sharing my screen, I can't put my hand up. Let me… let me see if I can rephrase that question, though, or…
Andres Borja 00:42:49 Actually, using the hand raised, it doesn't help with that, right?
Joshua MacDonald 00:42:53 Let me, see if I can,
present what Laurent just stated earlier as another question to Andres.
Because I… I…
this… what I… I have this screen up because this looks kind of, at a glance, much like a hotel collector configuration, that we're trying to get the model in our heads of a pipeline. That's helpful to have a sort of common understanding. And… and so this is,
a list of processors and a list of exporters with some sort of, like, connection to a receiver concept, vaguely.
And… And…
we've already kind of slipped on… slippery sloped down to, like, having our own sort of proto-SDK, right?
And…
And I… and what I heard Laurent say, I think I agree with, is, like, creating yet another node structure with an edge structure, or a list of nodes that are connected in series.
or a list of processors that fan out to a list of exporters, that feels like a new configuration problem if you start here. But if you… if I had all the same types of nodes that the
data flow engine is using to configure its own graphs with its name field, and its URN field, and its type field, setting to… settings we have, like processor, export, or receiver, then you would at least be able to reuse the config structs
of the DF engine, so that that future version that Laurent's imagining, where we do start using the core data type of OTAP records, and using the OTLP exporter, then we can, like.
Reframe our telemetry pipeline, internal telemetry pipeline, as having actual nodes that are Some sort of pipeline.
whether it's the real engine, as I think you're saying it shouldn't be, because that's too complicated for a self-telemetry system.
And that you want, maybe, more direct asynchronous… synchronous calls, maybe, or something like that.
And I guess I would counter that, can't we just use the same configuration in a different implementation? There seems to be a debate about whether you could reuse the
OTAPDF engine, with an alternative type, meaning a pipeline data is now, like, the SDK object.
Instead of the OCAP records object. That's one way you could go.
Or you could just read that configuration and construct a completely different graph, bypass the engine, just use it to set up a telemetry pipeline.
There's lots of ways we can go. I don't know…
Andres Borja 00:45:45 There is a reason to complement the idea, there is a reason why there is a collector and there are SDK, right? And they are not the same. It's because the pipeline implementation and needs, the use case in particular use case, is different, right? So…
That's why you don't have internal pipelines.
As part of the collective that are the same, you know?
So… Can you do it using the same…
grammar of the nodes configuration that we defined today? Maybe.
I feel like it's just… confusing, because…
All you… all you want to define is.
list of processors and exporters, you know? So… So…
Laurent Querel 00:46:31 I need to… Sorry to interrupt. I probably need to read the PR, because I'm…
I don't buy the argument of saying that the use case is different, and then we have to implement two
to Pipeline Engine, I don't see why.
Because for me, it's…
I mean, they are processing matrix, even… we could imagine that we derive metrics from span the same way, even for internal metrics.
So I don't see why, it will be different pipelines. So for me, this argument is…
maybe there is a value behind it, but I don't see it, personally. So I probably need to…
to look in more detail to the… to the… to the PR to better understand your approach… the entire approach. I'm not sure I totally follow
So I suggest to, maybe to, to continue the conversation offline.
If you are okay with that.
Joshua MacDonald 00:47:43 Thank you. Also, I've set up an internal meeting for Okarsh, Cijo, and myself with, Andres for… to continue this as well.
Thank you. While the agenda item document looks empty, I wonder if anyone would like to raise a topic.
Laurent Querel 00:48:13 because we have a lot of people that are new, maybe it will be interesting just to share this… we talk about that multiple times, the OPL specification.
So let me retrieve this document.
Joshua MacDonald 00:48:30 Yeah, I wasn't sure that that link was in the public yet. That was one question I had that.
Laurent Querel 00:48:34 Oh…
Joshua MacDonald 00:48:35 I think I have shared it with many of the people here. Maybe not everyone, though.
Laurent Querel 00:48:40 Yeah.
Joshua MacDonald 00:48:40 from…
Laurent Querel 00:48:40 We only share that with, Microsoft people and F5 people yet, yeah, okay, sorry.
Joshua MacDonald 00:48:47 But not everyone has it. Okay, well…
Yeah, it's up to you for what you want to say, but we do have that Data Fusion PR open, and I was speaking about this without you present last Thursday, so not… so people have heard something about this, and I'm…
well, where was I? I'm just gonna… I was… pointing at Albert's…
Albert Lockett 00:49:09 Yeah, if,
If you want, I could speak about this work a little bit, kind of give an update on it.
Joshua MacDonald 00:49:20 to share anything, or can I leave this up?
Albert Lockett 00:49:23 Yeah, yeah, so maybe instead of, like, talking through, like, the PR itself, it might just be more instructive if I just, like, gave a quick demo, would that be okay?
Laurent Querel 00:49:34 It's good.
Albert Lockett 00:49:35 Even better.
Reshare the screen.
So, go to the right… VS Code workspace, this is the wrong one.
Infusion on top of your old…
And I created an example to show
what I've done. So basically, what's in that PR that Josh had opened there?
Is an implementation of, are…
columnar query engine, and what it can do is it can take and parse these, KQL statements, and then internally it turns them into, a, data fusion
plan, and then, we can, run that plan over, our OTAP
arrow records and produce some transformed output. And so…
I wanted to give a few examples of, like, some of the trans… like, the transforms that we currently support, so…
First one is you can do simple filtering by fields on the, like, on the… in this case, it's logs, so, like, log records. So if I run this,
example here… It will ignore the commented code.
But basically what we're doing is we're generating a handful of batches, And, then we…
So we have our… a stream of batches.
And then,
the way the API currently looks, and I'm still kind of fiddling with this, is we take our first batch.
our pipeline expression, and then we, create a new, what I'm calling the executable pipeline, and then we call…
Execute on it, and then,
I haven't figured out a great way to get the result out of it yet, so currently the thing just owns the batch that it transforms, but you can see here that if we look at our input,
We, we had an input of logs, and our filter that we ran was
logs where the severity text is worn, and then if I look at the output, you can see that all I got was worn logs, so that's quite interesting. Let's look at our second example of something that works currently.
Here, we're filtering our logs, by the value of an attribute.
So if I… run that. We're looking for an attribute where it's called k8s.namespace is equal to prod…
And you can see that,
in our input, we had many logs, and they all have different kdes.namespace attributes, but the result is just the filtered ones. Let's look at something more interesting. We can use logical combinations of.
Laurent Querel 00:53:12 Just one thing, Albert, just to make sure that people understand.
Not only you filtered out the attributes, but obviously you also filtered out the logs, which… for the logs that don't have this attributes, or have this, yeah, don't have these attributes, they are just filtered out from the main table.
Albert Lockett 00:53:33 That's right, yeah, so, like, this would be our input. We have a logs table and an attributes table, and then, so we filtered both logs
And the attributes, so it's as if we filtered the logs by them having this attribute value.
That's a good… that's a good call out, Laurent.
So we can,
use a more complicated filter if we want. Here, we're filtering Arcadis namespaces, prod, or staging, and the severity level isn't… is not trace.
And so that's kind of a more interesting filter. What's also supported currently is the ability to set values, so here we're setting the severity text and the severity number on our input.
I run that, it will work.
And then,
There we go, so we should see that the severity is all changed to air. Now, here's something that I think is maybe probably the most interesting example I have to show,
This is, what…
I'm calling the, conditional, operator. So this isn't something that currently exists in, in, in KQL, but, it's this idea that maybe you want to conditionally
run your records through some kind of transform, and so here we can imagine, like, a hypothetical KQL-type syntax, where we have a condition, an if-else statement, where if my severity text is debug, then
set the event name to debug happens. Otherwise, if it's trace, set it to… trace happens. Otherwise, if it's info, set it to…
Something happened, and if it's not one of those
Conditions that match, then set the event name.
to something important happened, and set the severity. So it's kind of a silly example, but… But,
if I… And then, so I extended our, our intermediate representation to have this thing called the conditional
Express… data expression, which…
Has a set of, logical conditions, and then… and then data expressions that… if the logical condition matches the row, then you put it through these data expressions, basically.
So if I go back to my code… And I run this,
So we can see that now we'll have a… an interesting transform happen to our…
to our, logs, and so you can see here that… go back up…
In the input, this is what our input looked like, and then in our output, we see that conditionally, based on, in this case, severity text, we made some modifications to the
To the log records, so,
Yeah, so that's… that's an idea of, like, the kinds of, pipeline… like, KQL pipelines that we currently support through this thing.
And then, the last week or so, I've just been trying to do some performance optimization on it, trying to figure out, okay, how do we… like, once we've planned the data fusion plan that we're going to execute, how do we reuse that, and how do we
do, like…
a more lightweight re-planning if, for example, the arrow schema changes, because sometimes we have that happen with optional fields, or fields that can dynamically be dictionaries and things like that, so… so that's kind of the…
what I've been working on lately to try and improve this. Yeah, so that's, that's my quick demo.
Laurent Querel 00:57:45 Because you couldn't.
utpilla 00:57:47 Hey, yeah, Albert, yeah, thanks, that's a great demo. I had a question around this, mainly because I think you mentioned that
The intermediate language or intermediate expression might have to be modified to accept, like, more kinds of queries, so…
Do you see, like.
Do you think there's, there's this extra step of converting it into intermediate language, or, like, is it serving some purpose? Could we have directly just converted it into, what data fusion requires?
Albert Lockett 00:58:19 Yeah, that's… that's, that's interesting.
I, you know, I think we probably could. You know, the reason I went with the intermediate language just was kind of for the sake of expedience, where we already had a parser, and then, like, that intermediate representation that we had was, like, easier to start with, versus me having to kind of
implement, or, or, I guess.
utpilla 00:58:44 It's like…
Albert Lockett 00:58:45 understand the parser code, but yeah, like, I do think that, like, you know, maybe there is a world where we just say, hey, you know what, we could just… we could just parse this and then take the parsed input and directly build some kind of, like, data fusion plan. I don't think that would be,
I think that would probably… I think that would probably work.
utpilla 00:59:08 Okay.
Albert Lockett 00:59:09 Yeah, I just…
Laurent Querel 00:59:10 I just want to add, to complement that.
the,
in terms of performance, the gain will not be… I mean, for me, the performance aspect is not a driver for that. It could be interesting to have a direct conversion from this,
KQL-ish, language, to… to the logical plan of data fusion.
But, for performance, we don't really care in that case, because what we cache is, directly the data fusion plan.
And because we have configuration in place, so we have streams.
In fact, we have pipelines, and in those pipelines, we have OPL expressions describing what kind of transformation, projection, aggregation we want to apply on a stream of signals.
we don't have to interpret this expression again and again. It's done when we load the pipeline configuration, and then we are done. And that's what Albert did regarding the
The caching mechanism to reuse
the plan as much as possible, even with the complexity of the underlying Apache RO representation that we have.
For OTAP, because as you know, some columns are optional, so the… a batch of matrix does not necessarily look exactly the same, between different batches.
even for the same stream, because we… we support some, some optimization that, but, Albert was able to, to identify ways to, to make the data fusion a little bit more,
let's say, non-sensitive to this kind of modification, which is great. That gives us a lot of ability to reuse the plan and to keep the high performance.
utpilla 01:01:19 Yeah, that… thanks, I didn't know that. I thought maybe we were just, like, doing that conversion on every query, but yeah. So then it doesn't really matter if it's just a one-time cost, or twice.
Albert Lockett 01:01:30 Yeah.
utpilla 01:01:31 Yeah.
Laurent Querel 01:01:32 I think the if statement for people that are interested by this one, you can imagine it as a combination between splits. Let's say you have a stream of something, so in our case, it's a stream of signals.
And, the if is like a split with conditions. You have… you split a stream in multiple substreams.
each of those substreams have a filter, an entry filter. You do something on this, filtered, substreams.
And then there are… there is a union behind that that is implicit. So everything is merged back to the stream, so the if split
Do something with each branches, and then merge back the stream, so that's very powerful, and could be applied to any stream.
Of matrix and logs and so on.
And we also identified, so it's… it's not presented in today's demo, but some of those branches
could be terminal. And by terminal, we mean that they will not participate to the union of the… in the result, they will no longer appear. So, two examples of terminal nodes that could be part of a branch.
Either you want to drop some signals based on some conditions.
So we could imagine that we have a terminal node part of this, branch.
So it's a way to eliminate everything matching a specific condition. The other one is, if you want to
export… In different… to different exporter.
The content of specific branches, then you can do that and,
And if it's an intermediary, How to express that?
For people that are, well, well-versed in the, the…
The pipeline infrastructure that we have for every processor, we have ways to express multiple outputs.
So the… for each branch, we could say, oh, plug this, this branch to this port, plug this branch to this port. So it's also a way to root
The traffic, the telemetry traffic, to different destinations.
So it's a very powerful operator.
utpilla 01:04:17 Nice.
Joshua MacDonald 01:04:19 Thank you. I want to call time. I think some of us might have to go. It's getting dark early these days, if you don't… you might notice outdoors, so, it might be important if you have, say, goats waiting for you, for example.
Thank you all. We'll be here again next Thursday morning at 8 a.m, and if you heard this, and you're still on the call, and you want to see this paper that Laurent referred to, I have a copy that you can see.
And then, you know, if you wanted to speak and didn't get a chance, there's always the next time. Thank you all.
Laurent Querel 01:04:53 Thank you.
Joshua MacDonald 01:04:54 Cheers.
Andres Borja 01:04:55 Thank you.
utpilla 01:04:56 Thank you.
