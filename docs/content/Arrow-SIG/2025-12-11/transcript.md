SIG: Arrow SIG
Date: 2025-12-11
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Pablo Baeyens 00:01:20 Hey.
Albert Lockett 00:01:42 He is.
Danny Chin 00:01:48 Hi, Oprah.
Joshua MacDonald 00:03:25 Good morning.
I think we can wait a couple minutes. I am hoping to see Laurent today.
Meanwhile, there are, notes document open…
And if you can find it, please go ahead and, you know, add your name…
I can give you a link to that document.
And thank you for coming.
So… I will keep waiting a little bit.
Glad to see, Trask, thank you. You're a government committee… governance committee sponsor. Appreciate you being here. I had tried to gather, maybe a larger than normal group today, so we'll see if a few more people arrive. I am still expecting a lot.
I'm glad Pablo's here. This was sort of my idea for today, aside from any normal meeting business we feel we must do, was to talk about…
I guess where we are. Been more than 6 months since we kicked off this Phase 2
The way I see it, we've pretty much confirmed and accomplished what we said we would.
And it's time to start thinking ahead, to see if we are, kind of, like, where we are as far as,
The project, and the, the charter that we have.
So… So let's see, I…
I… the way I imagined this meeting, was more like, let's talk, because I have something that I wanna… that I… I feel like would be interesting or valuable for Phase 3, and…
But I'm in a weird position here, because I've been in the middle of this for a long time. So, I want to bring out other voices and start talking about, how OpenTelemetry Arrow fits into OpenTelemetry.
As we move forward.
And… I'm going to start by, at least, I guess.
Well, we're at 5 minutes past the hour, I'm just gonna start.
Can't see the list of attendees very well.
I put up what I think are of our… as the big, big questions. So, one thing is OpenTeometry Arrow has now been, for about 3 years, a sort of alternative working inside of OpenSeometry. I feel like we've incubated this for quite a while, and it's time to start promoting this as a viable alternative protocol.
And whatever that means. So I've, so that's one of my big topics for conversation today, is making OpenTelemetry Arrow more official for OpenTelemetry. This sort of second aspect of that same conversation is separate, but not really, which is, like, we have been skirting around the idea of a collector.
a Rust collector codebase, and I've been pretty good about not calling it a collector. Anytime I use the word collector, it's a capital C, it refers to the Go codebase, but everyone kind of sees that we've built a lot… a lot of similar function into a thing that we
don't call collector. And, at some point, this is becoming a weakness, or a…
a risk to the project, because other projects are out there
growing their user base, for a Rust collector-like thing. And we are prohibiting ourselves from advertising what we have, essentially. So, my second topic, my big topic, is about what we mean when we say collector, and how do we get to where there's
A grander collector.
Project Coalition.
I don't think we can get through that topic, really, without talking about interoperability between Go and Rust. And if I could just say, those are my three big topics. I put all the other ideas below.
that I have, there's sort of, like, interesting ideas. And then the last one, I think maybe that's also connected with the same
big one I just mentioned, which is, like, Go and Rust, collector or not. We have…
We have been out here doing an experiment, we'll say, for the last 6 months on what does it look like if we build a Rust pipeline.
At this point, I'm ready to make some takeaways. We have a very efficient pipeline. We win quite a lot by having an OTLP bytes representation in our pipeline. We are not deserializing OTLP proto-objects.
And I think that that is a substantial winning that we're having. And it shows in the benchmarks that we've got so far, as far as I can see.
That seems like a very good architectural decision, and I think it might be time to visit whether that makes sense in the Go Collector as well. I'm sure it's been thought of, but it's just never been done.
the…
The second idea that's sort of obviously connected with that same idea would be to go as far as, if you're going to talk about having variant representations in your pipeline, you know, right now the Go collector has just the P data, which is protocol message. If we were to move as far as OTLB bytes as an alternative, then I would also think about
the Go Arrow library. We can make a Go P data out of Arrow records as well.
basically have the libraries written to do that. So I'm sort of… sort of skirting around the idea of an enhancement to the Go Collector that would give it variable data types the way we've done here.
And that might also enhance our abilities to interoperate. So that's my… my big introduction here. I do want to make this conversational, and I do want to let others talk. I've given you my three big ideas. I'd like to hear from someone else.
If no one speaks, I will keep talking.
Pablo Baeyens 00:09:35 I took a look at your OTEP very briefly before… To school…
I think it makes sense, and I guess one comment I have… it's not about the…
OTEP itself. It's more about the process. I feel like,
it would be good to try to get the collector SIG,
into the review of this, even if formally is the technical committee and the specifications seek the one that needs to go through this?
Joshua MacDonald 00:10:12 Absolutely.
Pablo Baeyens 00:10:12 Boom.
we have the experience, for example, of the schemas, telemetry schemas, OTEP, where we said a bunch of things should be done on the collector's sake, and then, well, they didn't get done, and I feel like part of it, at least, is,
we didn't try to get enough buying from the collector seg, so…
Joshua MacDonald 00:10:32 I understand. Yeah, I kind of see the same with entities. We also have not implemented entities in Arrow, and it's sort of like, what should a collector be doing here?
So, that's a really fine point. The point is, I shouldn't be talking about planning without bringing in the collector SIG, and I didn't really mean it that way. I put… I intentionally filed this on Tuesday or Monday night, because I knew Tigrin would be in the spec SIG meeting, and I wanted his attention on it, because he's the one who's been most involved in this type of issue. If you go to the Slack.
And of course, because of this meeting this week, I wanted it to be out before I got here. In the Slack for hotel specification, there's a link to Tigrin's document about content negotiation. Apparently, it's 20 pages long, and I haven't read it, but it's not… it's not a new topic, so…
So, so this OTEP, which I sketched together very quickly, is, asking for…
a specification change, which is why I put it on Tuesday morning, but it's really talking about a major architectural improvement in the Go Collector, which would require a ton of buy-in. So, obviously, I didn't mean to make it sound like this is a proposal to force you to do something.
Pablo Baeyens 00:11:47 I mean, it needs to be discussed somewhere, I didn't mean it as, like… And Bogdan gave us…
Joshua MacDonald 00:11:52 basically that type of feedback in the meeting yesterday. You know, like, why is it that you're proposing… just to give us a brief synopsis, I'm… you know, the OTel Aero components, the export and the receiver that we wrote in Phase 1,
Those were copied, forked from the core components, the OTLP exporter and the OTLP receiver. So we took their configuration, we took their structure, and just extended it. It still has that same structure, it still has that same configuration, so that there's a huge amount of compatibility built in. What we decided to do is, like, you know, we're gonna try Arrow, and if it doesn't work, we fall back on the OTLP.
Both sides. We do that on the receiver and on the exporter.
And… and so that's my model of a, like, proof of concept already. Like, we took those core components, and we just sort of, like, add more protocols to them. And if they don't… those new protocols are options, you fall back on the core-based component.
Pablo Baeyens 00:12:43 Bogan's feedback was like, why do you want to modify the OTLP exporter? Why don't you make a new one? And I…
Joshua MacDonald 00:12:48 that's also sort of the proposal. You know, Laurent, in this project, has created something called the Hotel Exporter.
in Rust, which is a new prototype, but it's like, this is, again, the implementation that we would like to have where there's one port with one receiver logic, and it's got all the protocols that are compatible. So, really, this was about specifying what it means to be a viable alternative protocol, not about forcing change on the collector, but I think I appreciate it.
Pablo Baeyens 00:13:13 Hmm.
Joshua MacDonald 00:13:15 Because if… if we go into it, what we're really saying when we talk about alternative is, what's permitted? What can I change without breaking the data model? And I wanted to kind of… and… and so this…
this came out, its equivalence testing is, like, the big deal, is, like, the OpenTelemetry project needs to say what is equivalent, and I think provide testing frameworks to validate that, so…
We've done this once in Go, we've done this once in Rust now, which is to say, OTel Arrow resorts, it deduplicates, it changes the structure of the data quite a bit. You can't do byte equivalents.
You can't do object equivalents, you have to do, like, semantic equivalents.
because of reorderings that happen that just doesn't make sense to preserve. So that's what this is really about here.
And anyway, this is a… this is, like, how I propose
That we could do this, but this is more about making OTel Arrow an official support than about exactly how to do it in the collector.
Pablo Baeyens 00:14:16 Okay, thank you.
Joshua MacDonald 00:14:17 Oh, thank you, Pablo. I should be very careful what I say and do.
And I… so that is one leg of what I'm thinking about right now, is just to, like, let's… we've incubated this now, it's saving us quite a lot of memory, or a lot of CPU, or a lot of network.
And it's a… it's a viable option. What I think I've…
Learned from this past year or two, of studying, kind of, protocol costs in these telemetry pipelines tells me
That…
the best protocol you can choose in your exporter is one that the receiver knows how to work with. So, if I'm sending to a vendor that has, like.
TLP protobufs in their system.
they really want OTLP protobubs, because there's no extra conversion cost for them on the end. If I'm sending to a vendor that has an arrow-based pipeline, they're going to want the OTL Arrow format, because it gives them the data in this zero-copy way that they can do whatever they want with. So, in some sense, I see content negotiation as essential, because
any vendor is going to have an opinion, and we're not going to force all the vendors to update their backends. And this was… I've seen this problem for a long time now. You know, it's like, if you have a protocol that you're using in your backend, you are incentivized to put an exporter in the collector for your protocol.
And that's why we have 25 exporters in the collector that are all doing one vendor protocol. It's because that vendor would pay an enormous amount to convert from OTLP.
we're trying to get to where OTel Arrow is a viable choice for the vendor and for the exporter, so that if they both support it, they can drop into Arrow, save a bunch of bytes, and save a bunch of CPU at the other end.
And…
So, so I don't mean to say OTel Arrow should be the one true protocol in OpenTelemetry. We've seen reasons why, you know, the OTLP 1.0 is, like, very valuable because of its de facto standard.
Guillermo Calderon 00:16:23 And we're seeing other protocols that, frankly, compress better.
Joshua MacDonald 00:16:26 So if you're choosing for compression, you might choose Steph as one that's been pop… becoming, legitimate, essentially, in metrics. And so, if you have a pipeline that can handle Steph efficiently, you want Steph, that's better. But if you don't have Steph, then…
you know, Aero or OTLP are both going to require a conversion, and then it's a which one wins kind of question.
So I think that protocol choice for OpenTelemetry is just about giving vendors the choice to have the most efficient path that they can. And so, another question that came up in the meeting yesterday was, well, Josh, do you expect there to be 25 of these? No, I expect there to be 1 or 2 or 3 of these. They're good alternatives.
That, more than one vendor would support.
Well, that's my position about the OTEL Aero protocol itself.
Danny Chin 00:17:17 So that's the two.
Please. I have a question, sorry.
So what does it really mean by making it official? Like.
Joshua MacDonald 00:17:27 Yeah.
So that was why I brought it to the specifications sake. I was trying to define what it means to be viable, and my requirements essentially included perfect compatibility. So OpenTelemetry has a data model, they have a protocol, and OpenTeometry is in a position to say, yes, we officially say this protocol is one-for-one, it's effectively.
Guillermo Calderon 00:17:49 All right.
Joshua MacDonald 00:17:50 Promises.
Danny Chin 00:17:51 Basically, we recommend, not only OTLP, but also OTAP.
Yeah. To, like, other, like, newcomers, and… .
Joshua MacDonald 00:18:03 Yes, but also, what I'm really aiming for is someone else's words here, but someone called it an overnight upgrade, which is just the idea that, like, we're not going to ask you to change all your SDKs, but you are running a collector.
Overnight, we should be able to change you to use the new protocol between the collector and the backend, assuming the backend already.
Guillermo Calderon 00:18:22 And there's a content.
Joshua MacDonald 00:18:23 negotiate.
Guillermo Calderon 00:18:23 100% topics, really.
Joshua MacDonald 00:18:25 And that was always our idea with the OTel Arrow Go components, was same configuration, same fallback, therefore you can… anywhere you're using OTLP Exporter, you can just drop in OTL Arrow, and then if the vendor supports it, you will then get the benefit. I just want to make that a little bit more…
Formally blessed, essentially, is the proposal.
Danny Chin 00:18:45 I see. Thank you.
Joshua MacDonald 00:18:46 Yeah. Because I think that OpenTelemetry also imagines a V2 of OTLP. It just… it's pretty impractical to imagine it. One of the thoughts I was… I've mentioned to you, Danny, in private, but also we're looking at OTLP, and dictionaries keeps coming up. It's like, I wish I could just have dictionaries on top of OTLP.
That's one potential future that we could, you know.
there's… there's a couple ways of looking at this protocol negotiation. You could be negotiating protocol inversion, you could also have a feature negotiation, which is like, I'm willing to accept this, like, dictionary thing that's optional, or I'm willing to accept exponential histograms, but…
You know, or else I'm… or I'm not. Like, then would you like lossy conversions or not? And that kind of question.
So, it's a… it's a… that's… that's the type of support question, that I'm… that I'm…
contemplating here.
And the overnight upgrade is, again, by making these plugins to official components, if I could just have an extension on the exporter, an extension on the receiver, then, you know, new protocol comes out, we plug them both in, OpenTeometry says they're officially compatible, and the user doesn't need to know that they're dropping into that protocol and saving some money or whatever.
But that's a… that's one level of… of discussion.
Pablo Baeyens 00:20:11 I… Please.
Yeah
So, we talked a bit about this on your collector RFC, on the plugin story, and that. I think that's one of the parts that I'm…
most worried about? Like… People already struggle…
Joshua MacDonald 00:20:33 Yeah.
Pablo Baeyens 00:20:34 building custom distributions, we're going to ask them to have a Rust toolchain, effectively, to build their distribution, if they want to have support for this.
How do we do that in a way that, like, still leads to a… acceptable experience.
When you…
Joshua MacDonald 00:20:51 Yeah, I think this is the biggest risk here. I mean, I shelved it in summer, this last summer, because I effectively felt like it was a negative result. Like, the high level is people like Go because it's so easy to build and release.
people like Rust if you're using cargo commands. I think the, like, the…
revolution in software development in the last 20 years has been to get these, like, out-of-the-box toolchains that just, like, here's a tool, you can compile your code and run it. As long as it's one language, it kind of works. As soon as you start mixing languages and weird toolchains, it becomes hard.
In one sense, we've already heard that users have this pain, and they need it, because they're running NVIDIA drivers, really, or, like, they need the CGO code, and so they're already there in some sense.
But I… I don't want to belittle this, it's such a major, a major aspect of… our…
problem. Also, I mean, and I'm going to just… full disclosure, like, my employer would like plugins in pure Rust, like, we don't… like, even if it was without talking about interoperability in Go, we want
to be able to distribute pre-built code. And that's sort of a… maybe that's a big company thing, but that's what we're after. So, we will be talking about plugins if it's just Rust anyway.
And I don't… and I don't know how to evaluate the, like, I guess, risk-reward for the Go Collector.
it might be better, and that's what I put in my, kind of closing thoughts idea here, it might be better to focus first on
we have an arrow library for OTLP to OTAP already. It's pretty proven.
we could… what I'm… I think is probably more feasible is to… is to go reinvent the PData object in Go. Right now, it's,
hard-coded, self-managed, manually generated, or automatically generated code structs, right? We're not using
go-go anymore, we're not using the Google Protobuf compiler, we're using Bogdan's code.
So, like, go in and alter that, instead of having a… And I, you know, like…
Go is not my favorite language anymore, but I can imagine doing this. Like, right now, the pointer to impol… the P data is a pointer to an implementation object, which is a protocol message. We could change that to more of a, like, a union of, like.
Either it's bytes, or it's protocol buffer object, or it's arrow frames, and now there's 3 ways to represent the data.
It would be closer to what we have.
And you just have to be able to do conversions between them, and… The arrow thing is… is…
I'm not… I'm on the fence about it. It's, like, a very complex…
thing to add to your code. I'm not sure that anyone wants Arrow and Go.
The reason why we want Arrow is really to get into data fusion.
And DataFusion's not in Go, so I don't have a huge motivation.
to, like, add arrow and go. Other than the fact that I could then bolt on the Rust pipeline, cross the process boundary with my arrow, and then not do a lot of copying to get to my Rust pipeline with my same arrow, or something like that. So there's an interop story where you zero copy because of Arrow.
But.
Pablo Baeyens 00:24:20 And you're not sure about RO and Go because the ROGO ecosystem is not…
Joshua MacDonald 00:24:26 It's just not a strong ecosystem. There's not a lot of, like, oh, once I have it in Arrow and go, I can do X and Y and Z.
That's my impression.
I wouldn't be surprised to find a code base that's written in Go that's using Arrow, but…
I know Polar Signals has talked about it, but they think they're switching back and forth between Go and Rust.
And they've got Data Fusion as well, so…
Largely, people end up in Arrow because they want data fusion, I think.
Pablo Baeyens 00:24:57 Right.
Joshua MacDonald 00:24:59 And so then, can we imagine bolting together a collector that has Rust and Go components? Yes. Will it be hard to build? Yes.
Pablo Baeyens 00:25:12 I guess if… If it is acceptable for the default experience to be…
pure Go, and you need to enable explicitly that you want the Rust things, then it's…
Joshua MacDonald 00:25:24 Yeah, I would… I would…
Pablo Baeyens 00:25:25 by me?
Joshua MacDonald 00:25:26 I would start there, for example. Yes, absolutely. Keeps the pure…
We understand that. And to be clear, this is, like, I don't have, like, a concrete plan to start on this or tomorrow or anything. I'm… I was…
The… in some sense, this is stuff that we said we would look at in the Phase 2 proposal.
if we're talking about a Phase 3 proposal, I would…
I would probably just be a little bit more concrete about what we aim to do and try and get done this time. I think it was a negative result last time because we tried.
And… but I… you know, this… this… this document that I put together on Interop was…
Was trying to aim in the direction where you could keep the pure default and turn on options and so on, and…
Get it working.
I think this… this is not in a shape for anyone to read right now. I think it would be, something that…
Needs a little bit more…
another take over it, or another edit pass to, like, get to what you just said, Pablo, about, you know, emphasizing that we're not going to try and change the default, for sure.
And that it's… and that… I would… I would assume that for the most part, we try and keep
like we did in Phase 2, trying to avoid interference with the Go Collector group, like, like, we're not gonna try and shove this into the repo, but maybe we can start adding, you know, this or that to make it possible to build
You know, in other words, trying to keep the complexity out of the repo for as much as possible.
and to do, I guess, more feasibility study by modifying our codebase, see if we can get this building
Because I do know… I do know people building CGo and deploy code that way. We certainly are doing that for the Go Collector.
Pablo Baeyens 00:27:27 Yeah, I don't have a strong opinion on the P data. I think Bogdan and Dimitri are much more knowledgeable about that than I am.
Joshua MacDonald 00:27:37 It would be interesting to… I mean, we can sort of do a roundup of our results. We are seeing quite a, like, stark… like, if all you're doing is passing data through and batching, for example, you don't need to decode protobuf data.
or you… you… there's maybe a reason to, but you can also not, and it's, like, huh… it's gonna save you a lot of performance. So, I actually think we'd get,
you know, unless you… so unless you're doing, like, a transform processor, you don't need to do decoding into protocol buffer objects, and that's kind of the result that we're aiming to show at the end of this, like, we have a transform processor that does column-oriented modification, and it's going to be, like, way faster. So…
We're gonna be looking at the GO… the Rust pipeline does, you know, transform processor in aerospace.
And the Go processor does it by decoding protocol buffers in row space, and the performance is going to be pretty different there. And…
So I'm suggesting partly that if we could build the Go Collector to not unconditionally decode protocol buffers, that would be a huge step towards making an arrow integration, because then we could just have the Go collector
parse into OTLP,
at least having an option to leave unencoded protocol buffers. I know Bogdan has looked at this in the past, I gotta catch up with him. Then you could…
get your unencoded OTLP bytes, pass them to a Rust bridge, go into the Rust, still, like, you haven't copied any data yet, Rust can do efficient things with the bytes, turn them into Arrow, transform them, turn them back into bytes, and then return you to the Go pipeline, maybe, or… if the Go pipeline had a bytes representation.
So maybe that's the avenue of, like, least resistance, or most benefit.
To see what… to see what we think about maybe lazily decoding those protocol messages.
Definitely something.
Pablo Baeyens 00:29:37 Sounds interesting, and yeah, I think Boglan definitely should have thoughts about this.
Joshua MacDonald 00:29:41 He's talked about it in the past, so I'll bring that to him specifically.
Well, I've been talking a lot. We're halfway through the meeting. I don't… I don't want to keep talking about those same topics unless someone else wants to speak.
Oh, true.
Trask Stalnaker 00:30:03 Trying to absorb… .
Joshua MacDonald 00:30:08 Let's… I'm gonna… while you… why don't you speak for a moment, Trask, while I re-sort this list?
Trask Stalnaker 00:30:17 So, the… There's… a bunch of different pieces here, as you called out.
the…
The topic you brought up near the beginning of Rust collect… like, a Rust collector, like, not calling it a Rust collector, of there being other projects that are positioning themselves as Rust collectors.
Can you talk about that a little bit more? And, what in the current Hotel Arrow repo, is it doing…
Like, is it supporting any of the collector, kind of, like, YAML stuff?
Or it's just pure, kind of, programmatic pipelines that you… Pulled together.
Joshua MacDonald 00:31:15 So we, and I… I put a… I tried to be very open about this, but we did create a binary that parses YAML, but it's not in any way configured… compatible with the Go Collector's YAML, and…
That's, like, not just a syntax difference, it's more of a level of abstraction, I would say. The Go Collector has quite a lot of syntactic sugar around its pipeline configuration.
well, maybe it's not syntactic sugar, it's… it's model. It's a model where you have receivers and processors and exporters, and then you build a graph, and the processors are in a line, and the exporters and receivers fan in and fan out. And, like, that's all kind of hidden from you. And when the GoCollector builds the graph, it inserts fan out.
fan out consumers and fan out producers and stuff in ways that are kind of hidden from you. That is not implemented, and we don't intend to implement that. That would be a cross… crossing a line, as far as I know, as far as I feel, given what we said we wouldn't do.
But we could imagine, written in Go or in Rust, we could imagine parsing a YAML that was equivalent, and then forming that graph with the fan-out processor… fan-out consumers and such. We could do that in Go and spit out our own YAML, we could do that in Rust and just…
with another copy of the configuration. I think I'm imagining a…
If I… if I was forced, I mean, I'm not… I'm not being forced, but if you ask me, Josh, we really need to integrate with the Go Collector in the best possible way.
It would be… you know, my RFC here did kind of cover this, but I would… I would lean on the… I would continue using the Go Collector's config. I would have the Go collector parse its own config, because nobody wants to do that again. It's like half of the collector code base is configuration logic.
So, you would load your configuration, you would identify which components were Rust, and then you would spit out the Rust pipeline, its own configuration, which is a much lower level of abstraction. We don't have any kind of fan-out, like, hidden stuff like that.
So, that's how I would approach it. Like, if we're gonna interop, we would… we would convert the Go Collector YAML in the Go Collector into Rust YAML, which is, like, these are the nodes we want you to carry out. This is just exactly what your part in this pipeline.
Right, so we're not trying to be a compatible GoCollector, and honestly, I would prefer to just let the Go Collector do its thing and spit out a configuration for us if we're trying to interoperate.
But I did touch on a real topic, Trask. You know, I probably have heard of this Rotel project.
They are not an OTEL project. They once called themselves an OpenTelemetry collector. They were point… they pointed out to them that they had not the right to say that, so now they call themselves Rust Collection.
Trask Stalnaker 00:34:14 And…
Joshua MacDonald 00:34:15 what I'm trying to say is, I am trying to stay away from saying I'm a Rust collector as much as I can, and these guys are not Rust collector, but they're saying they do Rust and they do OpenTelemetry.
they're taking the market that I would like to take, honestly, is a nice way of saying it. Actually, I don't want to compete with them. If I could say, we have a rust collector project.
come join us. I think they would. I think they would bring their energy into this group, but I have to be able to say we're building a collector somehow, and that's… right now, we don't have that. So that was really the sort of…
Question of…
if we have a charter to build a Rust collector with some restrictions, then I would reach out to these guys again and say, hey, I think, you know.
we're interested in whether there's an opportunity to share or to collaborate. For example, I think their technology has a lot of, like, SDK integration that could be very powerful. You want a faster SDK for your Ruby or your JavaScript? It's Rust running with a local collector that we've
you know, like, in some sense, a collector can do an SDK, and an SDK is… so we can drop in their SDK or whatever. I think that that would make cool integration for us, and maybe that would be a nice project, but I'm not calling what we have a collector yet, and…
That's the… I feel like it's, like, limiting our ability to advertise.
And I think we should sort out the… what we're planning to do with Go Interop, and we have to maintain the branding and the community strength of the collector, period, I would say.
Trask Stalnaker 00:35:57 Who, and that… you're, like, to…
You're specifically talking there about a full REST collector to, sort of, like, that market, or do you think that people would… are going to be… do you think that people will be equally interested in Rust
pipelines inside of the Go Collector.
Joshua MacDonald 00:36:25 I think… that… Both answers are going to happen.
I know…
Okay, so I would… the first answer I have is, yeah, there are… there are users of Go Collector that…
Are probably using,
components that we aren't gonna have in Rust for a very long time, or, you know, there's… there's, like, a long… there's 300 components there. You're using… you're using it for a reason.
But we know that if you… but for… there are some fairly straightforward, like, more vanilla types of pipeline that OTel Arrow can do very well. So if it's pure OTLP passing through.
or if it's passing through data fusion, then there's some portions of that pipeline could be written in Rust, and we can imagine, as ugly as it might be, building a unified piece of software that brings in both. That is very hard as.
Trask Stalnaker 00:37:19 I see.
But I think there's a benefit.
So, with being inside of the… I'm trying to think of, like, the collector, all the components in the collector,
Because, obviously, the… Pipeline transformation stuff, doesn't really…
bridge, then… I mean, it could, but it sort of defeats the purpose.
But there's, like… Hundreds of receivers that you would… be able to benefit from.
Joshua MacDonald 00:37:54 I will never write Prometheus in Rust. It will always be a Go project. That's kind of one, like, permanent example. So if I just wanted Prometheus, but everything else was Rust was… could be done in Rust, then
I would probably come looking for a Go collector that could bolt onto my Rust pipeline. I would… I would pass it from OTLP and Go to Rust, and the rest would be Rust. That's the type of pipeline I imagine.
Trask Stalnaker 00:38:18 Okay, yeah, and then the… I mean, other… I mean, receivers are super popular, Kubernetes, host receiver, all of those things.
Joshua MacDonald 00:38:27 Yeah, we just don't want to duplicate all that stuff, and it's not performance sensitive, really, and, you know…
Okay. But my other answer…
Trask Stalnaker 00:38:35 to me.
Joshua MacDonald 00:38:36 is… is… is partly where this Rotel project came from, which is, like, we… we see that not having garbage collection can save you money. We see that,
That… in our case, we have, like, security requirements that just make Go a little harder. Like, we're not willing to use Go in certain places. Like, we need pure Rust for whatever big company reasons or whatever.
And so…
we are in a position, I would say, of having a hard line of, like, yeah, we understand why people want to run Go and Rust together. We want to give you that, but we also want a mode where you can run this without that.
And because we're not a collector right now, we're not trying to provide a user configuration model that you can, like, here's your Rust distro of a collector, it has YAML that's either the same or very similar, and here's how you run it, here's the Docker image, we're not doing all that.
because… partly because we said we wouldn't, but the user who wants pure open… who wants a pure Rust pipeline
Is either gonna do all those things, like, with a main function of their own, or,
They're going to… You know, they'll do it themselves, and they can, you know, do it through.
Trask Stalnaker 00:39:54 That's still an op…
Joshua MacDonald 00:39:55 Embedded software, basically.
Trask Stalnaker 00:39:58 And that's still an avenue for people who want to do that to leverage the components that were…
Joshua MacDonald 00:40:05 Yeah.
Trask Stalnaker 00:40:06 to the…
Joshua MacDonald 00:40:06 And one of the…
Trask Stalnaker 00:40:07 pipelines.
Joshua MacDonald 00:40:09 Yeah, and then we might say something like,
well, there's something here about, crates.io release. Like, if I want to make embedded software out of this, and just say, you know, it's… it's a toolkit for collector pipelines, we can bolt it into Go, we're working on it, but if you just want to use it, here's the crate that you can…
run. And then… and that way, people who are looking for pure rust can do it themselves, and they have to… they have to fight it a little bit.
But we're not… I definitely just don't want to write the same YAML in Rust and try and make them compatible.
Like, it's a… conf map package.
I hope that helps.
Sort of with.
Trask Stalnaker 00:40:55 Yeah, no, that helps a lot. I think I have a… let me look. From…
From a performance perspective, because I know that was one of the, sort of.
Key outcomes that we were looking for and can help us to justify, you know, moving forward.
Do you have… Official results… is that something that's…
can be put together before sort of closing out Phase 2.
Joshua MacDonald 00:41:30 Yeah, I actually was hoping I would get someone else on the phone, on the call here, to… to walk us through the current results. CJ, do you have… could you… would you be able to put on the… could I put you on the spot and see what we… what we know?
Cijo Thomas (Microsoft) 00:41:43 I don't have the numbers right now, because we never had anything which compared.
the IRO pipeline with Collector. We just merged such APR, like, 2 days, maybe yesterday.
Joshua MacDonald 00:41:56 We're kind of not done. Two things here. One is we're… we've been doing continuous, like, nightly testing of our own code just to track regressions and so on. But it's been my… my wish and desire to see us do
fair comparisons with Go and Rust pipelines. A few examples would be, like, here's the filter processor.
based on OTTL, here's the filter based on data fusion, here's the batch processor, simple batching configuration in both versions.
we should do that, and I… but I… but… but the high-level belief that I have, from what I've seen, is it's, like, several orders of magnitude. Like, we're 3 times faster, or 3 times lower resource usage, or 4 times, or something like that. Like, it, it's binary orders of magnitude, but… but… but… but…
Trask Stalnaker 00:42:43 Yeah, we just need to… yeah.
Joshua MacDonald 00:42:46 And…
Trask Stalnaker 00:42:46 Okay.
Joshua MacDonald 00:42:48 And part of what I said was really about bringing some of that back to the Go Collector. Like, we think it would be way better for some cases just to, like, pass bytes through, because you don't always need to decode the data. That would… that would help a lot.
But we do have current efforts, very active efforts, to get basic benchmarks between the two.
Hoping not to make them look critical, we just wanna, you know, like, if we can show that we're doing 3 times better than a Go Collector, it also suggests a Go Collector can improve.
Trask Stalnaker 00:43:21 As far as the,
P data, byte representation, is that an orthogonal piece, like, just for speeding up the Go pipelines, or is that needed…
For… a… before you can… embed a pure Rust pipeline into the collector.
Joshua MacDonald 00:43:55 Yeah, I would say… I'm… yeah, those are connected for me. If you… If you didn't have a…
PureBytes or an Arrow native kind of data type in the Go Collector.
Well, you're kind of back where we… where we started with the Phase 1 components. Like, we can get compression on the wire, but we can't save you any CPU cost.
In the collector.
Evan Torrie 00:44:21 Especially not listening.
Joshua MacDonald 00:44:22 Hey, Evan, I think you're… you're… you mean to be muted.
Evan Torrie 00:44:25 Christine.
Joshua MacDonald 00:44:26 Can't mute you, there you are.
Trask Stalnaker 00:44:27 Okay.
Joshua MacDonald 00:44:30 So, so yeah, I wouldn't say it's a hard connection, but it seems like a very logical one.
I, I also…
Trask Stalnaker 00:44:39 My worry… my… the… my worry there is, just that that is a very impactful change in the collector side.
Joshua MacDonald 00:44:49 And I think Pablo caught that as well.
Trask Stalnaker 00:44:51 1.0. I definitely don't want to put anything on the collector before 1.0.
Joshua MacDonald 00:44:59 Totally fair. Let me… let me put it this way. In my… in my proposal, the rough collector proposal from this summer, I didn't have that proposal at all.
It was a… we believe that there are… when you look at one collector configuration, that you can… that you can very likely separate it into
Rust components and Go components, and… And…
in the most… for the most part, we think that the ideal outcome is that you never change your data more than once. So if you were in that configuration, like Prometheus receiver with the rest of its OTL Arrow, you would have… expect one conversion from OTLP proto-objects to proto… protobytes, and then you would switch into the rest
data. Of course, there's an alternative. You could call our Go library to turn it into Arrow, and then do… call into Arrow like that.
It's gonna be way easier to just do bytes, since that's built in everywhere.
But then I could… but then, like, at that… at that level, the proposal was there will be some Go logic that looks at your whole configuration, partitions it into Rust stuff and Go stuff, puts in the bridges as needed, and then spits out two binary… or two… two processes that, you know, are collaborating in some way. That would be my first approach.
Trask Stalnaker 00:46:15 Okay, and that, I mean, that's sort of the full interop story. I guess, for an… is there an interim…
Interop story, which is just the… you can either… your pipelines are either… Go or Rust.
Does that help?
Joshua MacDonald 00:46:37 I think that would be…
Trask Stalnaker 00:46:38 Can you still leverage the receivers?
Joshua MacDonald 00:46:40 of my proposal, which would be, like, if you have a Go… a configuration that includes one Prometheus to OTLP export and one OTel Arrow to OTel Arrow pipeline, then the OTel Arrow pipeline is entirely Rust, and the Prometheus pipeline is entirely Go, and you start two processes.
And this is a mess. This is, like… Pablo doesn't really want to hear me say any of this, right? Like, this is totally a mess.
I kinda don't like it, because observability's gonna suffer right away, and that's the…
Like, we can make these pipelines work without making them observable first.
I don't know. I'm… I'm a little… I'm a little bit at a loss of how to do this.
Trask Stalnaker 00:47:23 So with the… so that's why… sorry, I'm not quite drawing the connection yet on the, the bytes.
Joshua MacDonald 00:47:32 I was trying to say, we don't need that. We don't want to disrupt the collector. What we can start with is full partition. If, you know, like, there… you look at the collector configuration, you find that there is an OTL
P to batching to OTLP export.
We could do all that in Rust and more efficiently.
you see that there's a Prometheus to batch to OTLP export. We can't do all that in Rust. Therefore, you will do it in Go.
Trask Stalnaker 00:48:00 So you… you wouldn't… Why can't the… Receivers be bridged?
since those aren't performance sensitive, why can't those pipelines be bridged over to, Rust Aero?
Joshua MacDonald 00:48:20 Oh, okay. I can. I think I was trying to take that step by step. So, the first thing you could do is full partitioning with complete separation, and then the next thing you could do is try to insert, like.
one conversion. You know, I just don't want to do two conversions. Like, I don't want to go back and forth and back and forth, like, that seems… Yeah, yes, yes, I understand. So at some level, I don't want to make every possible configuration work. It's, like, not reasonable.
Trask Stalnaker 00:48:45 Okay.
The thing that you said was a mess that Pablo didn't want, Explain that one more time.
Joshua MacDonald 00:48:55 is that if I'm starting, one collector to do, let's say, the Prometheus pipeline, and I've identified that the… there's a…
a particular path through this pipeline is pure aggress, potentially.
I was imagining that I have, like, a… equivalence map.
for individual components. So there will be well-known components where I know I have an equivalent in Rust. I have an equivalent OTLP receiver in Rust, I have an equivalent batch processor in Rust, I have an equivalent filter processor in Rust, and I have an equivalent exporter OTLP. If I'm… if a pipeline is built entirely of components where I have an equivalent
in Rust, then maybe I can drop into Rust.
And maybe it performs better, but how observable will that be?
Now we've got to bridge together the observability from one pipeline into the other, and like…
I'm just saying this is not going to be easier or, or simple.
Trask Stalnaker 00:49:46 Oh, I see. Okay. Okay. Okay.
Joshua MacDonald 00:49:50 Mostly about observability.
I feel tempted to throw this out for the… this is more of an arrow question for this codebase, the Rust codebase.
I… at one point,
like, OpenTelemetry doesn't have a specification for the collector, it's part of our gray area.
Like, what is a collector? What does it mean to be a collector?
And now we have this concept of P data. Something about what it means to be a collector means having P data, right?
In the Go Collector model, P data consists of a
A very well hidden, but very, very physical protocol buffer message object.
So, underneath the abstraction of PData, you have message object, and that's where all those allocations come from.
But it gives you a simple API, which at some level is the… is, I think, the specification. What is a collector? It has a simple API for mutating data.
GoCollector gives you that in the form of a protocol message object. Here you go. If you want to change it, it's simple. It's an object, you just modify, change its name, whatever.
If that is a requirement, we don't… we do not meet it in Rust, and that is because we do not have a simple protocol message
pipeline object. I can't convert my P data
In a seamless way to protocol message object and mutate it.
The only way I could do that would be to mutate it, or is to serialize it back to bytes when I'm done, and that…
would… make whatever you're doing, I would say, a bit worse.
there's no concept in our pipeline of saying, oh yeah, I dropped down to the simple model because I just wanted, like, to be simple.
And do row-by-row mutations. That's what the collector is able to do. If that's a requirement, we don't need it, and I'm wondering if we should try to meet it.
And I'm sort of having that feeling because I see cases where
where OTLP bytes and arrow records are neither quite suitable for us. And the one that we've discovered this week or two past were… is if you're trying to output compressed JSON,
Neither of those representations is very good for you.
And this… this, well, Pablo knows this story very well, but the Go Collector has shifted… has shifted away from the batch processor, which is…
Pure data type, pure pipeline data, batching, and shifted towards
batching in the output format. So you tie your protocol and your batcher together, and you can do things. You can do clever things, but you can't convert it back to P data at that point. And so…
it… there is a… there's a sense that we're discovering at which, if you're going to batch and you have an alternative format, you cannot go back to the pipeline data model at that point. You are… you are opaque at best, and you maybe are the simple model at best.
And… and so we have struggled to make an OTLP, or a… a non-OTLP JSON exporter for Azure Monitor, essentially. So I'm starting to wonder if we… if we are not…
quite ready to kind of support more than just… like, in other words, we are not good at supporting a non-arrow protocol or a non-OTLP protocol right now.
And so the… that's a… that's an area of…
Curiosity for me, whether we move in the direction of exporter helper and allowing alternative export protocols that can do batching and retry and so on. I don't actually think that this…
Trask Stalnaker 00:53:28 that…
Joshua MacDonald 00:53:29 Go ahead.
Trask Stalnaker 00:53:30 Is that important use case? Going back to what you said of, generally people who want to use, people are going to want to use whatever is their backend
supports…
Joshua MacDonald 00:53:47 That's… that's kind of what I'm trying to do.
Trask Stalnaker 00:53:49 If you're…
Joshua MacDonald 00:53:51 Yeah, like, if you want compressed JSON objects at the end of the pipeline.
Trask Stalnaker 00:53:58 You have two problems.
Arrow, would you use Arrow?
In the middle, then?
Joshua MacDonald 00:54:04 That's what I'm… that's what we're struggling with. Like, suppose that you're running through the transform processor, and we finish it, and it's been very efficient because it's Aero, and so now you're… now you're handed this Arrow payload. We… we… we have a batch processor, we have a retry processor.
But you can't use the batches of Arrow
you have to convert them back into JSON. And if you convert one batch for one batch, you might end up with a JSON batch that's too large. What you actually need is a limited-size compressed JSON blob, and that is very hard to produce.
in an export situation, when you've got one arrow frame handed to you. This is, like, 3 JSON blobs here. Couldn't we have gone back to the batcher and said, hey, batcher, I want 1 megabyte JSON GZIP files from this process. Please give me data that is 1MB of gzip batch.
which is a batch JSON.
Which means…
Trask Stalnaker 00:55:02 I guess what I'm… what I'm trying to… kind of getting at is, can we put a box around the use cases for the Rust Aero pipelines?
at least, you know, in whatever phase we're working on, you know, long-term, yes, I support solving all these problems,
But would it be okay to say, for now, Russ.
Aero pipelines are only for outputting Arrow at the end.
Joshua MacDonald 00:55:38 Yeah.
Trask Stalnaker 00:55:41 Or are there important use cases that are needed?
Joshua MacDonald 00:55:45 Yeah, I don't know.
Trask Stalnaker 00:55:45 year, a term…
Joshua MacDonald 00:55:47 I can take both sides of that one. Like, why are we working on JSON gzip blobs when we have Azure Monitor supporting OTLP already? Question mark.
I don't know the answer to that one either. I suspect it's a compatibility issue.
But your question is valid. Why are we talking about other protocols here? And I think the answer is that we…
are being pragmatic. We understand that back-ends won't always
Want to accept the protocol we have.
And that's why we're… well, but I am kind of repeating myself and affirming what I said earlier. If the backend does not support OTLP, and the backend
does not support OTel Arrow natively. What I mean natively is, like, you're willing to take that data type and, like, let it pass through your system. The first… if the first thing you do is turn it away, like, convert it from OTLP or convert it from OTel Arrow into random vendor protocol struct.
then you have not benefited from OTL Arrow or OTLP as much as potentially you could, and that's why the vendors are always pushing exporters into the collector, is to say, well, if you send me OTLP or OTL Arrow, I just have more conversion costs. I don't want that, so I want you to send me my native format.
What I'm trying to say here is that we are not yet good at sending native format, because we're not good at batching native format, because we're not good at compressing and treating, sort of, like, other forms of prepared telemetry in our pipeline.
And that may be okay, Trask, your question is valid. We are not focused on that very well, and maybe we shouldn't be.
But I put it in this, like.
There's something about how we can't deal with JSON very well.
Basically.
Trask Stalnaker 00:57:32 Cool. Thank you for feeling all of my… Neh.
Joshua MacDonald 00:57:35 And we were at the end,
Cj, I know you had this sort of non-topic about Phase 3, and your hand is up.
Cijo Thomas (Microsoft) 00:57:44 I had a topic at the very end, it's about, like, internal logging. If I can take one minute, I just want to talk about that, yeah.
Joshua MacDonald 00:57:52 Absolutely. I have a strong opinion to share with your… after your one minute.
Cijo Thomas (Microsoft) 00:57:56 Yeah, the main thing is I'm doing benchmarking, and I'm seeing some issues, and there is no way for me to figure out what's going on. There is zero internal logs right now, so I'm just sending tenderland statements throughout my local…
So basically, this is an item to solve that, and it's not perfect, it does not do the, philosophy of thread per core or anything, but at least it gets some logs flowing, and it's going to be disabled by default, so unless you opt into it explicitly, it's not going to enable anything, so it would be, like, zero, like.
truly zero cost. So I want, like, some reviews on that. If things are okay, I'll, like, spend some more time, like, polishing it. But I'm mostly looking for, like, is it
Like, a direction which we are okay to pursue, or do we want to do, like, something else completely?
I also saw that, like, Lauren had some, specific requirements. I put a to-do comment in the PR itself.
Joshua MacDonald 00:58:55 Yeah, he wrote some stuff here. I think we can sort out this type of… this type of concern about the fiber core and the locking and stuff.
I…
I also think that we're… what you're recommending is the right thing for OpenTelemetry Rust, to just follow the plan. I mean.
I, and so if we're off by default, Laurent shouldn't have a very strong complaint. I absolutely agree, we've had major problems debugging our own code, because it's not really,
debuggable.
I don't know. The thing I… the thing I want to share with my personal opinion, and I'll say no more after this, is I hate the syntax. I just hate it. I don't want to see this route equals, I want to see…
curly braces with variable names inside of message format strings, but OpenTelemetry has never done formatted logging, and I don't expect them to do it now.
So, I just feel my own internal reservations of wanting a plain old logging library, which…
Cijo Thomas (Microsoft) 01:00:00 Then we'll comment this.
Joshua MacDonald 01:00:02 strings.
Cijo Thomas (Microsoft) 01:00:02 I think you've.
Joshua MacDonald 01:00:03 Told me we can.
Cijo Thomas (Microsoft) 01:00:04 We can… it's just that, like, we did it this way in Open Elementary Rust, so I'm basically copying it, but the underlying library, they totally support that templated kind of thing.
Joshua MacDonald 01:00:14 Yeah, this is… this is, like, technically more efficient, because you're not doing any formatting, you're just bidding out keys and values, and… and…
technically, I… you're saying it's compatible. If you want to write info with message formats, then you get that, and it will do the formatting if the logging is enabled. So, if I turn it off, it doesn't format, that's good enough for me. I don't have a major complaint here.
Cijo Thomas (Microsoft) 01:00:37 And by the way, this does not… yeah, this does not yet integrate with OpenTelemetry SDK in any way, it's just using tracing and its std out writer.
To begin with, similar to the Go collectors, like, ZAP-based HDOT logging. It's just step one, but I really need to get this in so I can start, because, like, the DF engine is crashing in my machine.
Joshua MacDonald 01:00:59 I'm not gonna… I'm not gonna fight you on this. I will fight OpenTelemetry on this.
Cijo Thomas (Microsoft) 01:01:04 Anyway, thanks all, just, please do review, give me thumbs up, thumbs down on the…
Joshua MacDonald 01:01:08 I think we'll… we'll merge this and let Laurent.
disagree. He wasn't here, so he doesn't get to disagree today.
Cijo Thomas (Microsoft) 01:01:16 Thanks.
Joshua MacDonald 01:01:17 Thanks all. We're out of time. Next Tuesday, we will be here again, for those of you in the Pacific time zone, at least, or something like that. Thank you all. See you next time.
Albert Lockett 01:01:28 Thanks, Josh. Bye, everyone.
