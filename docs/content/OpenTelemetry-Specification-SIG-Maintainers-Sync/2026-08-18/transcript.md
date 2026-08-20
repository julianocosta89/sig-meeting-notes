SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-08-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Joshua MacDonald (Microsoft) 00:03:03 Good morning.
And, wait a few minutes to start this meeting.
Please put your name and any agenda items on the board or on the notes.
And some estimates for time, if you have them. Looks like we have about 20 minutes filled up so far.
All right, we have a few people here. It still says 8.03 on my clock. I'm gonna give us another minute.
Put your names up.
Robert Pająk (Splunk Inc.) 00:04:55 Hello.
Joshua MacDonald (Microsoft) 00:04:58 Hi, Robert.
You are first on the agenda today, and, I said I'd wait, give it 30 more seconds.
Everybody can open up the agenda item Robert's going to tell us about.
Concurrent log export.
All right, we got, like, almost 20 people. Let's, let's get started. Good morning, everybody. It's the 400-somethingth meeting of the OpenTelemetry Spec SIG 448, and we're going to talk first, hear from Robert about, concurrent log export calls.
Robert Pająk (Splunk Inc.) 00:05:43 Okay, hello, everyone.
So, this one is trying to, like, I have a proposal here to a little bit change the specification around concurrency model of the log record exporter, because, we are right now in work of stabilizing logs SDK in Go.
And, the current description of the export interface, it's kind of like Every method needs to be concurrent safe, expect its export method, which cannot be called concurrently with itself, but it has to be concurrently called with other methods, which is extremely, kind of, awkward.
And, in my opinion, it doesn't really help people implementing the interface to, it doesn't really help interface, because they still need to deal with concurrency with other methods, so I think it doesn't really simplify on the implementation side.
And here I am proposing something that Jack proposed, like, I think 2 years ago, that we could offer an opt-in, opt-in, thing that if the exporter, if the exporter If the exporter-export is also concurrent safe.
Then we can simplify, and for instance, the simple processor would not have to serialize, synchronize the calls to the export.
And, yeah, so this is my proposal. In Go, I have a PR where we simply expect everyone to make everything concurrent safe. The reason is that we are also aware that sometimes people are using the exporters even outside of the SDK, so they often want the export calls just to be concurrent safe, like HTTP clients or other Just things that you can often use to make some requests.
So, so even without, Even right now, most of our exporters work concurrency on export.
So, with these guarantees, which we want to add, like, exit optimization Specification, so just allow languages to allow it, I think it can simplify, the… it can just make the user experience for our users a little bit better, and also maybe sometimes simplify our SDKs.
And, I also had… yeah, also there was a proposal that, it can be implemented as a marker interface or other things.
depending on the language, and yeah, I think that's all. I try to express as much as possible the description regarding Baku's capability, why you want to make this change. There's the prototype, and I think that Tristan There's some question here.
Joshua MacDonald (Microsoft) 00:08:40 Yeah, let's hear from Tristan, thank you.
Tristan Sloughter (mydecisive.ai) 00:08:43 Yeah, I guess, first thing is just… So this would make it differ from, like, traces, where the language is right now the same as logs is. Is the logs exporter and processor different enough that that makes sense to be… Like, different in that way, that you're being able to call it concurrently, and not leave concurrency up to the exporter Itself?
Robert Pająk (Splunk Inc.) 00:09:07 So, yes, I think the same language could be in the trace signal as well as the metrics, if that's what you ask me.
I think it will be the same. The fact that I'm changing it here, I just want to make a local change here, so we just do not, you know, change everything, the Specification at the same time, and create prototypes for all the things, because there's the only thing we're working on. That's one reason. And the second reason is that the prototypes, at least in Google, need to be different, because changing, you know, the interface could be like a breaking change for some users. So probably for other signals, when you… at least in Go, when you already stabilize that export does not have to be, you know, concurrent safe, you'll just need to make… make the implementation a little different.
Have I answered your question, or not at all, Tristan?
Tristan Sloughter (mydecisive.ai) 00:10:00 Yeah, so you'd want to carry this over to the other signals versus having it different in each signal.
Then it… then my next question would just be, I… yeah. I liked having it separated that the exporter controls its own concurrency, so it doesn't get called a bunch… it doesn't get called concurrently and say.
it knows how many, you know, connections it has, how much it can be sending concurrently and all that, and that's its responsibility. I always thought it was also just a little weird that the processor was responsible for the batching instead of the exporter, but that's a separate issue, but, I mean, it's kind of similar. But the… so that… that would be my sticking point, that I… it just feels like an exporter responsibility versus the processor responsibility.
Robert Pająk (Splunk Inc.) 00:10:49 It's also, maybe just a little bit history. So, previously, I wanted to add it to the processor, but I got feedback from David Ashbole that, in his opinion, should be also the exporter. Also, I, you know, checked that it was the same proposal from Jack, so… I also thought about doing the processor, whatever, and just saying, oh, exporter does not to be concurrent safe, the processor can handle it, but yeah, what you said, Tristan is also, you know, back from previous feedback that I got, that it should be the exporter's responsibility, so it could be, you know.
that we were used.
And more flexible.
Hey.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:11:27 Robert.
So… and I see Trask is on this call, so Trask, I know this has been, like, a long, standing, issue, or sort of thorn in your side, and so, And I just want to explain what we do in Java and, get your feedback on, like, what we… what we might do if this were to go forward. So, In Java, our exporters return a future. And what the processors do is they take that future and they… they await for it to resolve.
And I think one… I left a comment in your PR about this, but I think exporters still need a way to signal to the processor that they have more capacity for concurrent export.
Because I don't think you want, sort of, them to be… have to handle the burden of, like, you know, sort of unbounded batches being passed to them. And so, in my head.
the, you know, the way that you could signal this, it could vary by language, so… but we return promises today, and What we could do is we could change our promises so that they resolve as soon as the exporter, you know, has, you know, batched it up for, like, an asynchronous export.
And thus, when the exporter is at capacity, and it can't handle any more concurrent batches, it can now return a promise, which is, which, you know, blocks, or, you know, until there's extra capacity.
What do you all do in Go, and I guess, have you thought about this sort of, like, signaling problem?
Robert Pająk (Splunk Inc.) 00:13:17 So first of all, we do not have promises in Go.
we only have, like, little things like channels, and for batch processor, we do everything in one kind of, you know, go routine, one kind of thread. It was just the most efficient way, that we were able to do at this moment. So we could just have, like, a warm, you know, working routine, which is responsible for, for… for exporting all of the stuff. But I think that, Jack, you are correct, that this is very, you know, language, or maybe not even language, but it's runtime-specific, how to do it efficiently.
And I think there's already a language which says something about promises.
that the exporter should deal with, you know, the internal state, and there's something existing. I think near… I think it's even maybe near the… near the section and paragraphs when I was changing things, or maybe it was on the export stuff. So yeah, we can follow up later, Jack, asynchronously, just to make sure that we are online. Jack, anything you want to comment here?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:14:26 Just, just that, I… I agree with this direction, and, you know, I guess I would just want the language to, in this spec, to sort of communicate to… Implementers of this, you know, that there should be some coordination between processors and exporters to signal whether there is extra capacity to do more concurrent exports.
But leave it up to the languages to have language-specific, to make language idiomatic choices on how exactly that's communicated.
Trask Stalnaker (Microsoft Corporation) 00:14:57 Jack, why, it seems simpler to me to have the batch span processor have, like, a max concurrency.
And it to control how much concurrent Things are happening in the batch. How many concurrent calls are happening in the exporter.
Partly also because the promise… If you complete the promise just when it's enqueued.
As opposed to when it's completed, you lose the error signal.
Like, which is, today, the promise completes when it… the whole thing is completed, so you have the completion.
Robert Pająk (Splunk Inc.) 00:15:41 Sorry to interrupt you, but I think that what you're described right now This car is violating the Specification. Right now, the Specification says that you cannot have more than one concurrent export.
Trask Stalnaker (Microsoft Corporation) 00:15:53 And that's what I wanted to change forever.
Robert Pająk (Splunk Inc.) 00:15:56 Yeah, I see.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:15:57 Yeah, so Trask is saying, like, if we're going to change it, why don't we change it a different way? At least the Java implementation of it.
But, like, still, like, I think, you know, within the… what you're trying to describe here in the spec.
Robert Pająk (Splunk Inc.) 00:16:11 I think it's still needed. I think my change is still needed if you want to have concurrent exports, because right now, it's not even allowed, so I think it's a baby step towards what you want to have.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:16:24 Trask, I think that there's, you know, different approaches we could take in Java. Do you think that there's anything, like, that's, like, spec… worthy to talk about, like, you know, you're talking about the error signaling, like, what went wrong at the end of the promise. How is that consumed, and how would, like, one strategy versus the other sort of impact the availability or visibility of that signal?
Trask Stalnaker (Microsoft Corporation) 00:16:50 Well, it's… isn't it consumed on shutdown?
So that we can have, you know, flesh, basically on flesh.
To ensure that everything has been fully exported before we shut down.
Within the given time.
Out.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:17:10 It's very complicated code.
I don't know it off the top of my head.
Joshua MacDonald (Microsoft) 00:17:20 So I've extended the time box on this, we're gonna… Tristan next.
Tristan Sloughter (mydecisive.ai) 00:17:27 Oh yeah, I was just gonna say that, yeah, what Jack described is essentially what, we do in, like, Erlang, in that… the… log… whatever's sending the log, if there's capacity on the other side, it's asynchronous, so it just throws it over the fence, essentially. And if there's not, then it goes into a synchronous and it blocks so that it stops, and then it… that's how you control the concurrency from that side. So there's not multiple concurrent calls to export.
So I don't… that's why Jack sounded to me like it supported the way it's currently written, versus needing to call export multiple times. And then you can signal back, if you needed to, into the span processor to say.
something went wrong through another mechanism, but yeah, I still think the exporter should be in charge of, like, retries, but I know that's out of there, and that's into the spam processors currently, so it's not really an option, but… Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:26 I think the fact that you, you interpreted it that way, Tristan, is, it sort of, speaks to kind of how nuanced and… and maybe, dense this text is. You know, in Java, we have the same thing, you know, we have a future or a promise that we return, and, you know, we read the spec and said, like, hey, because processors can't call exporters concurrently, we need to, you know, synchronously wait for those promises to resolve.
And, you know.
Tristan Sloughter (mydecisive.ai) 00:18:58 Gotcha.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:18:59 I don't know, Erling interpreted it differently, and the way that I think Trask would have liked us to interpret it.
Trask Stalnaker (Microsoft Corporation) 00:19:06 Yeah, yeah, no, I… my interpretation is once we return the promise, we are no longer… we can… we're no longer… Aren't concurrently running that.
Function, but totally get the different interpretation.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:25 So let's fix it.
Joshua MacDonald (Microsoft) 00:19:27 Yeah, for the record, I support Trask's interpretation, and, I mean, I agree with Robert. The… we are being held back by a lack of concurrency in the processors. You cannot export more data without concurrency. There's no way to set our current export processor pairing to get higher throughput than one thread can export.
So… and that's been a problem for a long time. I would like to see us fix it.
Are there any more comments on this issue?
Got a thumbs up.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:19:58 I guess I have one more thought, so, like, you know, I see that Cijo, I think, is writing about max concurrent export. Like.
If there is going to be something that controls the max concurrent export, I think there's some thinking that needs to be done about whether that is a property of the processor or the exporter. Like, who controls the concurrency? And that's kind of what I was getting at at the beginning.
is like, you know, does the processor, you know, keep some sort of state of how many concurrent exports it's handling, and increment and decrement them, or does the exporter signal back to the processor via, you know, promise resolution, if it has extra capacity? So, you know, the way that… the reason that that matters is because when it comes time for users to configure the amount of concurrency that they want.
You know, the property will either be at the batch processor or at the OTLP exporter, so we need to sort of decide that. And, you know, that will manifest in declarative config and things like that.
Tristan Sloughter (mydecisive.ai) 00:20:57 I don't want it in two places.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:20:58 We don't want it in two places.
Correct.
Michele Mancioppi (Dash0 Inc.) 00:21:03 I also think that, if at all possible, we should go with a differ… a similar division of labor.
As in the collector, which has been moving away from the batch processor and into exporter queues.
So moving more of the control, more of the complexity in the exporters.
As a user.
it would be, having in the SDKs more work in the processor and less in the exporter would… Violate the element of least surprise.
Trask Stalnaker (Microsoft Corporation) 00:21:36 I was just gonna mention it, and I think this is what Tristan said that, they're doing already, that the exporter, could, block if it doesn't… I mean, it could… Yeah, that call itself, it could either return a promise right away, basically saying, okay, I'm gonna go deal with it, or it could block and wait, and that would then cascade up to the caller.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:04 Yep, and that would imply that the property's down at the exporter level, not at the processor.
Joshua MacDonald (Microsoft) 00:22:11 So, okay, we're coming up on time for this issue. I will say that Michele raised an important point. The exporter of the collector has subsumed batching and queuing at this point, and you get a choice whether you want to return immediately with success, ignoring the error, or whether you want to wait for the error.
and that's all mixed together with concurrency choices that you have.
As well as batching parameters. Perhaps this would be a good place to present that a future time. I'm involved with the batching migration there, so I could… I could do that. Well, thank you all. We're going to move to the next topic. Michele, it's you.
Michele Mancioppi (Dash0 Inc.) 00:22:52 On…
Joshua MacDonald (Microsoft) 00:22:53 Here we go, please.
Michele Mancioppi (Dash0 Inc.) 00:22:55 So, this is a topic that started yesterday in the semantic convention SIG, where, Roberto from the Python SIG, came up.
discrepancies in the implementation of the service resource detector. We have language in the spec about how the part after unknown underscore service, Double, like, column, should be calculated, and, it brought up, it, it went off tangents.
For which I'm responsible. And, the tangent is that The way we define today the service resource detector in the specifications, and in all the implementations in the SDKs, is very limiting. Effectively, what we do there, we either… we look up the auto service name environment variable, then we look up the auto resource attributes environment variable.
If we do not find an entry for service.name.
We go and calculate the unknown underscore service colon, whatever.
And, most SDK implementations do that with different levels of detail of how the known service works, but when you go and look at the resulting service name from the point of view of automatic injection.
So I come at this with the hat of the OpenTelemetry injector, the system packages, and I also claim that the OpenTelemetry operator With Automot interaction has the same problem. It is left to the user to actually go and configure a respectable service name.
the, interestingly enough, and this is the table that, it's currently on screen, please, Josh, keep scrolling there. Yeah, the pain has been felt by several, automatic instrumentation bundles.
Java has a whole bunch of library and framework-specific ways of coming up with better service names than unknown underscore service. So does .NET, so does, PHP, I know for a fact that a lot of vendor distributions do the same to provide better service names out of the box.
So, my proposal is to, tweak… open up the language for the definition of what the service resource detector can do to allow SDKs to actually perform more refined language-specific logic before falling back to unknown underscore service, because I have never met a user in my life who was happy with unknown underscore service. It's not like we would make the UX worse.
I'll stop here to see if anybody has comments or questions.
Joshua MacDonald (Microsoft) 00:25:57 Tristan.
Tristan Sloughter (mydecisive.ai) 00:25:59 Yeah, I'll just say, again, I completely agree, and we actually already did this in Erlang Elixir, because we have when something is shipped in that, it's called an OTP release, you can find that name when you boot up the system, when it starts. So we find the name, the version, we create the resource with the service name and the service version for the user, which they… we first check, did they set something specifically?
But there's no reason to not use the name of the thing that they're running.
I just assumed others didn't do something like that, because, like, in Java, Spring isn't, you know, core to Java, it's separate, but I'd still agree, putting that in… It's…
Michele Mancioppi (Dash0 Inc.) 00:26:37 It's not in the SDK, but it is in the OpenTalentry Java agent with additional resource detectors.
Florian has a question, how is the service, star information detected and set for instrument applications that don't set it and observe by Demon set solutions? In Kubernetes, it's, more complicated, so the OpenTelemetry operator has additionally on, the operator side, through effectively ingestion, ingestion pipeline, shenanigans. It supports, the resource.opentelementry.io slash And then you put there the attribute key, colon value, annotation. There is a whole bunch of mappings from app.kubernetes.io slash app and other things that are automatically picked up.
And, In those cases.
the OpenTelemetry operator wins over the resource attributes that are sent by the SDK.
So, we would not break the OpenTelemetry operator. What also we would not break is manual setups, where the user has gone and configured, through the initialization of the OpenTelemetry SDK, to patch, so to merge more detailed resources on top of the default one that the SDK will provide.
So I did a bunch of experiments and tests, and I could not find a use case where the only thing that Would be overwritten.
Is not an unknown service scenario.
Which makes me very confident that this change would be a strictly positive one for everybody involved.
There is another additional thing worth mentioning.
Putting it… putting this additional logic in the service detector.
has two additional benefits. One is the element of least surprise, because, you know, service name would come from the service detector, not something like super-duper language-specific service detector, additionally. And we get support for free in declarative configurations, which already Treats, the service resource detector, together with host, container, and process, if memory serves, as the only resource detectors built in out of the box in the specs.
Jason Plumb 00:29:02 I want to offer a little bit of a counterpoint, to the it-benefits-everyone argument, because I think what it might… what we might be at risk of doing is to adding complexity to something that's right now very simple. It's really easy to understand, if you just provide your service name, you get your service name.
We do have custom detectors in our Java distro, and they're quite complex. Like, the ways in which a Java service, depending on how it's constructed, can determine its… or guess… it's really a guess, right? Guess its service name based on 5, 6, or 7 different criteria.
kind of error-prone and fragile, I'll be honest, and I don't know that this… I'm a little concerned that this adds complexity where it's not necessarily needed.
Michele Mancioppi (Dash0 Inc.) 00:29:53 Well, I dis… I disagree on the, there are scenarios in which I disagree on the, not necessarily needed. And those scenarios are the automatic injection ones. Because you either make a better job out of the box, or you undermine the user experience with automatic injection, forcing the user to go and manually go and add to SystemD units, environment variables, In my experience.
Very few people are capable of doing that reliably, going and adding environment variables to your Kubernetes deployments, and peppering, effectively, what should be a smarter default all over the place.
Jason Plumb 00:30:33 Sure, so, yeah, respect, I get that.
I think in those cases, it's perfectly valid to bring in additional components that do the detection, but whether or not it needs to be part of the spec for the default, I guess, is where I'm concerned. The default service detector, right?
Because that's what this proposal is asking about.
Michele Mancioppi (Dash0 Inc.) 00:30:52 Yes, this proposal is asking for that, yes.
Jason Plumb 00:30:54 Yeah.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:30:55 So… The problem is, is the, the, the injector, which is what Michele is talking about, it needs… it needs some sort of standard that it can guide users to reference. So, you know, you're gonna install the injector on your Linux box, and it's going to, you know, have broad brushstrokes and instrument everything that it detects that's a Java processor, a .NET processor, or whatever process.
And there's no practical way to go and individually name those things, to set an hotel service name environment variable. And so, if we want to have a usable experience for that, we need to give some lever that is language agnostic for the users to be able to, like, instruct the injector, or have the injector do by default.
Which triggers these, you know, supplemental service name detectors to activate.
And so whether that's baked into the, you know, the base service detector, or it's, like, an extra name, like an extra service, an extra detector, we can debate that, but I think it does need to be language agnostic, and it does need to exist.
Michele Mancioppi (Dash0 Inc.) 00:32:04 And I feel that having a service detector as a user is the place where I would expect the service to come from.
It's… I, I understand the concern by Jason.
Maybe then the service name was misnamed and should have been, like, an EMV service detector, but if we end up with service detector and service plus plus detector that does language-specific automation, then, That's gonna be confusing.
Joshua MacDonald (Microsoft) 00:32:38 Tristan.
Tristan Sloughter (mydecisive.ai) 00:32:39 I'd say the spec should at least be opened up, and then it's up to each SIG. Like, if the Java one, if people are submitting complicated scenarios for detecting service names, those can be rejected and say, this one's too complicated, it needs to be in a specific injector, or a separate library, or whatever.
But just to open it up in general for those that do have… Core names that are given, and versions given for services already.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:33:09 Yeah, that seems fair, like, because the Erlang case that you stated, where the language has a specific facility to describe what your application is named, to not use that is just silly. So…
Jason Plumb 00:33:24 So, I think we've all felt the pain from users running into unknown service. I've also run into the pain where an application team has had something sitting in their manifest for years and didn't know that they set this value, and then they got these service detectors that found it in their manifest, and they're like, where's this name coming from? We're like.
Well, it's a name you set, like, a decade ago and didn't realize it. So, there can be surprise there, too, but I like this idea overall.
Michele Mancioppi (Dash0 Inc.) 00:33:51 The language that I proposed in the issue, so I went… I did not open a PR yet, because I thought it would need, more discussion, and that's exactly what happened, is to go with May.
implemented it, these additional behaviors. I personally would go as far as to say should.
because of the premium value I put in Smart Defaults.
but, I mean, it's of course up to the… to the group, right?
Joshua MacDonald (Microsoft) 00:34:25 Alright, so we've got an issue filed, we've had a little bit more discussion. It sounds like you could create a PR with feedback you've gotten so far.
Michele Mancioppi (Dash0 Inc.) 00:34:31 Yes.
Joshua MacDonald (Microsoft) 00:34:33 Very good.
All right, and we're a little over time again. I think we can move on, is that all right?
Okay.
Sven, I'm going to, hand it over to you to talk about a new SIG, and I'm gonna give you a little bit of extra time to start.
Sven Cowart (ElastiFlow Inc) 00:34:51 Okay, cool.
Do you want me to share the screen, or you got it?
Joshua MacDonald (Microsoft) 00:34:56 Yeah, let, sure, I would be glad to let you, thank you.
Sven Cowart (ElastiFlow Inc) 00:35:12 All right, hey, I'm Sven. I'm here because Ludnoa, told me to present to you guys that we're reviving and repurposing the old network state, and just wanted to share what the project is and kind of the things that we're going after. A little background about myself on the long-time software engineer and co-founder of a company called Lassiflow. We are focused particularly in the NPM space and solving network observability problems.
I think it's helpful for me to kind of describe some of the pain points we've had, and some problems that have been presented to us by our customers and our user group, and to kind of frame the conversation and why we feel that, going after and creating this project, and reviving the network SIG is a relevant and important thing for the OpenTelemetry community as a whole.
So, we… we started one right around the time that, OpenTelemetry, I think, was in beta, and so it wasn't really… didn't really cross our mind, especially in those early days, that we should be using OpenTelemetry as the way to model the network, particularly because at that time, it was very clear that OpenTelemetry is very… app-centric. I mean, they mostly cater to the ATM space, I would say. And… And, And so, what's happened in, I think, over the last 5 years is, one, OpenTelemetry has Taken the observability space.
like a storm, like everyone knows here, right? I don't think you can talk about observability without talking about OpenTelemetry at this point. And, especially if you go to like, shows like KubeCon or anything where the focus is cloud-based observability, APM type of observability.
But what's happened to us now is, a lot of our… NetOps folks, like most of our users are network engineers, are asking, hey, I want to correlate my data to the stuff that the DevOps team has, and they're sharing platforms, and the ecosystems are colliding on what they're using. And… and so we tried to do that, and then just… Kind of came up against a bunch of walls that felt like lots of hacks to do something like that because of what we think is, a… Under-representation of the… the things that are available and possible to be instrumented and, exposed from an observability standpoint in layers 2 through 4.
And… and so… really where this is coming from is that when we looked at, the Open, OpenTelemetry.
semantic conventions and the ecosystem as a whole is that we just saw that, okay, we're not there yet at servicing the needs of the MPM space, and so let's get there, and so that we can hopefully bring these two worlds of APM and NPM a little bit closer together and empower people to really use the same tools for both needs.
So, for the sake of time, I'm gonna skip over this. I don't want to read a readout to you guys, but, I don't think that's useful here. But, so… What we're focusing on and the way we're going to go about this is that we want to really think about entities and making sure that we create the right network-related entities, and then from there.
Create standard metrics and semantic conventions to deliver on those types of things.
Think of, like, a… a network interface, right? Someone traditionally, a network engineer, if they wanted to see what's going on in their network interface, they would use, typically, flow data and SNMP data and SNMP trap data to, understand, their, their infrastructure. And… And to do that today in OpenTelemetry is rather challenging. The semantic conventions aren't there to do it in a way that would be deemed acceptable by anyone who has spent their career as a network engineer. And then, additionally, just within the collectors.
space, the NetFlow receiver and the S&P and the S&P trap receivers are not… they're in the same state, it's… they're kind of packs put together, so, like, a… somewhat of a best effort at some point or another. That doesn't really, allow someone like a network engineer to really use those three receivers to, To replace the existing collectors or technologies that they would use to do the same thing.
So, the goal then is to, like, for example… yeah, we have a network interface, right? We want to be able to, one.
collect flow data.
for that network interface inside of OpenTelemetry, that can be exposed as two primary ways, which is just as general metrics, and then actually introduced. And there is a proposal here that's coming later in the issue, but actually.
expose the flow records as traces, and we call them flow traces. I did an experimental project called Mermint, where, we do that exactly and specifically within Kubernetes clusters, and that logic is going to be ported over into the, the OBI collector, because it's EDPF-based, and so, And then, if I want to see metrics about the network interface and the hard… the actual physical infrastructure that that network interface is on, right? How do we… being able to map SNMP to actually OpenTelemetry metrics and SNMP traps to, OpenTelemetry logs, and then using that, as well as the entities that we define to be able to properly do that, to come up with the right semantic conventions to then capture the L2 through L4 space and, kind of push everything forward.
For the, OpenTelemetry community.
So, like… I guess high level, again, to just summarize, We want much better and comprehensive, L2 through L4 semantic conventions that are also related to entities. We want better support for those native traditional network Network observability, telemetry methods like NetFlow, S&P, SMMP Trap.
And, and then we also want the ability to instrument, the network layer in areas that can benefit from EBPF-based instrumentation, through OBI, and so, we'll contribute that.
Part of it as well.
Long-term, I don't know how many of you guys know much about SNMP, but SNMP kind of comes with a standard set of four, voids, which voids are… think of them like attributes, more or less, and then there is about 30,000 Vendor-specific things that somehow map to, something that means the same thing as something else, and, right, then it kind of gets really complicated. The long-term goal there is to, we have access to lots of those things, and we've actually Recently tried to make sense of some of that, and so we're going to try to map a lot of the vendor-specific stuff into actual standard insight attributes so that it doesn't become an explosion of attributes.
It probably will eventually, but we're gonna cross that bridge when we get there, and to see what the best way to do that is, but it'll probably be some type of federated approach.
In the long run.
That's kind of it.
Joshua MacDonald (Microsoft) 00:43:46 Thank you, Sven. I learned some things here. I will confess not knowing everything about SMP. It sounds like you're looking for interested participants, experts. What can we do to help?
Sven Cowart (ElastiFlow Inc) 00:44:00 Yeah, so… oh man, did I never share?
Joshua MacDonald (Microsoft) 00:44:04 No, you're sharing, I can see it.
Sven Cowart (ElastiFlow Inc) 00:44:07 Oh, okay. So, yeah, I mean, if you have particular interest in the network space, right, please.
come to our SIG. I think we have a good core group right now, but we need… I think we need more people, and to really get involved. Right now, we're still kind of bootstrapping this thing. I… I did… create the project recently. I'm trying to get rolling there, create the milestone, make this all, run smoothly here pretty soon, over the next couple weeks.
But yeah, if you know someone, either… doesn't have to be a network person, just has to be someone who, like, runs a Kubernetes cluster and has problems seeing what's going on in network space, right? That's also a good person to help us to find what we need to do.
And so, if you know someone, send them to the network SIG and see if there's any way that they can contribute and collaborate. I think we'll benefit a lot from the mindshare that exists within the community.
Joshua MacDonald (Microsoft) 00:45:11 All right, thank you. Any comments here in the room?
Sorry, I see a thumbs up.
Sven Cowart (ElastiFlow Inc) 00:45:22 There will probably be some specification changes that we'll want at some point in the future, just based on the fact that some of this network data is a little different than what you normally expect in the application space. So, but, you know.
We'll be working on it together.
So you'll see me.
Joshua MacDonald (Microsoft) 00:45:42 That's a good teaser.
Okay, thank you, Sven. Unless there are no, I'm gonna suggest we move on. If you wouldn't mind letting me share again, here we go.
The right one, there we go. Okay, thank you very much. Alright, Cijo, you are up, and I'm giving you more than 2 minutes.
Cijo Thomas (Microsoft Corporation) 00:46:06 Hopefully I don't need that much time. This is not a technical discussion, this is more like trying to improve the code ownership for semantic conventions, specifically for things which concerns the SDKs.
So, as of now, it's an independent group, very different from the specification owner, but based on my own observation when I tried to fix some of the semantic convention. It seems most of them require some sort of Either blessing from the spec, or more discussion involving the specification itself.
So that's when I realized, like, there is no common… I don't think there is even a common person between the… spec approvers and the SDK health semantic conventions Approvers. So I was thinking it would be easier, if you, like, add all the spec approvers.
as an additional code owner, for the Sync Convention for SDK Health. As of now, it's a bunch of metrics.
But I expect it to be eventually evolved to add, talks or events.
And also traces in the future. And most of them, like, the semantic convention is not just describing the name of the attribute, it's also trying to describe when you should use this attribute versus something else, and that's where spec gets involved, because the spec has some opinion on what it should and it shouldn't do.
So it feels, like, very closely related, so that we better have, like, a single Like, single, or at least a common, ownership for that one.
If anyone has comments, please raise. Otherwise, I'll ask the semantic conventions group to make the change, like, maybe I'll wait a few more days, but if anyone has comments, we can use this time to discuss.
Joshua MacDonald (Microsoft) 00:47:59 Sounds good. And I see, you linked to, like, the current state of, the SDK metrics… Yeah, yeah, this is just a…
Cijo Thomas (Microsoft Corporation) 00:48:09 Yeah, yeah.
Joshua MacDonald (Microsoft) 00:48:10 examples.
Cijo Thomas (Microsoft Corporation) 00:48:12 Yeah, this is simply, like, a packing of who has implemented what metric.
And we have an interest to make this stable soonish, but I think that's where I try to, like, dig into each metric and realize that, okay, it triggers more discussion, and those discussions always, take me to the spec level, or some discussion in the spec.
Which is why it is important to do it before we do a stabilization, so that everyone from the spec has a say in the semantic conventions as well.
Joshua MacDonald (Microsoft) 00:48:48 All right, well, I support this. Would anyone like to comment?
Cijo Thomas (Microsoft Corporation) 00:48:57 Okay? Assume there is no objection, so I'll talk to some convention people to… Make that happen, maybe giving it another 3-4 days to people, to comment.
Joshua MacDonald (Microsoft) 00:49:08 All right, thank you. By the way, Joe has an OTEP open, we might ask him to talk about it at one of these meetings.
But for now, unless there are more comments, I think we can move on to Trask, and I'm going to give you more time as well.
Trask Stalnaker (Microsoft Corporation) 00:49:25 Thanks. So, Lydmil and I had discussed… brought the conformance testing repo here, previously. Just wanted to give an update that There are PRs up for the, for several languages, for adding initial a single HTTP client and a single HTTP server.
Instrumentation conformance test.
So it's… these PRs introduce the test harness for that specific language. So if you are, knowledgeable in one of these languages, would love for you to review, my AI slop.
And, It's also fine if we, you know, merge it, and you come to the repo later, and you see, like, we're not conforming to good language practices, you know, raise issues, send PRs, that sort of thing.
There will be, once we get the initial, test harnesses in, then, you know, we'll… we can, add more, instrumentations, and there's a bunch more steps, but this is kind of step zero.
Yeah, Cijo.
Cijo Thomas (Microsoft Corporation) 00:50:48 Yeah, thanks, Trust, for driving this. I have one quick question. I didn't see this one until, like, yesterday. There is a central repo. We kind of started the same effort in OpenElementary Rust, and also in .NET.
Where the individual instrumentation libraries are already doing a Weaver type check in their CI. Right. So what's the long-term plan? Like, do we intend to… Maintain those things in individual country repos where the instrumentations leave, or we expect to move everything to the central repo.
Trask Stalnaker (Microsoft Corporation) 00:51:22 So, we'd like to do both. The, it's important to have the, CI in… live alongside the instrumentations, and fail… fail CI, that sort of thing.
We also want to have, sort of cross-language scenarios and tests, that are run on releases and sort of official, like, external-facing.
What, take a look at what Lyudmila has been working on with Python.
So she has… Basically, Done that where, We can reuse, sort of, the harness… reuse pieces… reuse the code, and run it in, kind of, different modes.
for the different repo usages. One for sort of this conformance test where it doesn't fail, it just reports and another for the Python, I think.
I think it's landed in the Python Gen AI repo, but I'm not sure.
Where it uses the same infrastructure that… from the conformance repo to run it in CI.
So I'm not… it'll probably need to be sort of language-specific, again, sort of how we publish things out of the conformance test repo to share.
But that's definitely the long-term goal. If short-term we have duplication, it's totally fine.
Cijo Thomas (Microsoft Corporation) 00:53:09 Okay, yeah. Is it somewhat similar to the W3C, trace context, they have a conformance test where you point a web application at the suit, it'll run… it will fire requests with particular trace ID, malformed, all those things, and it'll observe back what it got on the other side, and confirms that, okay, this… service is compliant with the W3C spec, Tristan spec, or not. Is this the, like, similar idea here? You point an instrumentation, the harness will run against it and observe the telemetry coming out of it using Weaver Live.
And confirms that, okay, this is complaint, or this is not complain, and if it's not, it'll produce a, like, something like a score.
Is that the ideas for… A report. Okay.
Trask Stalnaker (Microsoft Corporation) 00:53:56 Yeah, yeah, if I can share briefly, if everyone, in case it sounds like some folks haven't seen this… Josh, can I share for a minute?
Joshua MacDonald (Microsoft) 00:54:10 Please.
Trask Stalnaker (Microsoft Corporation) 00:54:11 Thank you.
Oops, oh, dash prototy, hi.
So this was the, sort of initial prototype for this, kind of report.
Where, you know, we take different languages, different libraries, and report, kind of, what the conformance, what they produce, what they don't. This was just a very early proof of concept Probably do it differently, Right now, we're just capturing the data.
output from the weaver. We're not actually producing any reports yet.
Cijo Thomas (Microsoft Corporation) 00:54:57 Understood, yeah. I think it feels very similar to what we've been trying to do for the performance benchmarks. Each repo has their own, and we recently started a centralized benchmark report, which runs the equated subset and do a centralized reporting, so, yeah.
Looks cool, like, I was mostly curious on, like, overall direction, because I missed the, like, origin of the report itself.
Trask Stalnaker (Microsoft Corporation) 00:55:24 Yeah, and we kind of struggled with that for a while with this repo, of what the overlap was and where the tests should belong, and I think that's a similar thing we struggled with in benchmarking for a long time. But I… I really like this direction of, you know, of both. Like, we need it in the repos, but it's also very useful to have.
across… Kind of cross-language, and having it all in one repo makes it really easy, once we start defining these scenarios, to apply them, consistently across all the languages, and get some good, public-facing data.
Cijo Thomas (Microsoft Corporation) 00:56:10 Yeah, yeah I also did the similar thing for not just instrumentations, but also SDK's own metrics, because that is also ultimately an instrumentation.
So that PRs are not yet merged, it's in the… I think it's in the Rust repo, and probably in the Arrow repo, where the internal metrics are also tested against the Weaver life check.
So hopefully, like, once we are done, like, we should be able to do this not just to instrumentations, but treat our own SDKs as another instrumentation and move it via.
Anyway, that was just a comment, maybe.
Trask Stalnaker (Microsoft Corporation) 00:56:46 Yeah, I hadn't thought about that, but that… that's a… that would be great, yeah.
Cijo Thomas (Microsoft Corporation) 00:56:52 Yeah, anyway, I'll keep observing this and review things which I can help, and also try to bring the SDK's own thing to this when the time is right.
Trask Stalnaker (Microsoft Corporation) 00:57:04 Digger.
Diego Hurtado 00:57:07 Right, so… Great project, by the way, I really like it.
I was, already… I already opened a couple of draft PRs in the country… in the Python contract repo to add this, testing.
for the… requests, and flask, instrumentations, so that, if they are not compliant with semantic conventions, our CI would fail.
So I just wanted to make sure that that aligns with, the direction this, This project wants to move.
Trask Stalnaker (Microsoft Corporation) 00:57:52 Yeah, are you using… are you following Lyudmila's work and reusing the, the runners and the infrastructure from the conformance repo?
Diego Hurtado 00:58:04 Did you rebuild that?
Trask Stalnaker (Microsoft Corporation) 00:58:05 Sort of as a separate weaver… pipeline.
Diego Hurtado 00:58:11 No, actually, I wasn't, aware of, of, of that, that, that that Lumila created is in the Jennai repo, or… Yeah.
Trask Stalnaker (Microsoft Corporation) 00:58:27 In the GenAI repo.
Diego Hurtado 00:58:31 Oh, okay.
Yeah, I'll take a look at that, make sure that, what I'm doing is consistent with… With that effort, but, yeah, I just wanted to, coordinate with you on that front. Thank you.
Trask Stalnaker (Microsoft Corporation) 00:58:44 Yeah, yeah, and that sharing piece is new. We didn't really prototype that. That's kind of a new direction that, that, we're… We're trying to go into, so, definitely, you know, feedback, and that's very bleeding… bleeding edge for this, repo still.
Cijo Thomas (Microsoft Corporation) 00:59:08 No, trust one comment. Sorry, Gopher, I just had… yeah.
Joshua MacDonald (Microsoft) 00:59:12 Go ahead.
Cijo Thomas (Microsoft Corporation) 00:59:13 I had some notes where I described or shared some links with what I described earlier, but one other observation, which I faced myself, and I tried to include this in many reports, the Weaver tool needs a lot more improvements to really make this easier. I did some small changes to make it easy, because otherwise it's… for example, you have a repo which produces a ton of spans and metrics, and Weaver, like, doesn't know what to really check, because it's given an entire registry, so we don't really have a targeted way of testing it. I have faced the same problem in the demo, which is an OpenPR right now, because it produces, like.
Hundreds, maybe thousands of… conventions, and Weaver doesn't know, like, what to validate.
Because if it tries to validate everything, it's probably going to take forever. So there are, like, some issues opened in the Weaver repo itself to make some improvements to the tooling, so it makes it, easier to do, like, targeted check. Okay, this… this some… this… check… only check the… this particular subsection within the overall semantic section. Where… where you, like.
Fucking any of those things, or did you hit, like, any of those issues yourself, which would be… Fixable by a better weaver or improved weaver.
Trask Stalnaker (Microsoft Corporation) 01:00:31 So, we hit less of them because these are very targeted tests.
Right? We just spin up the SDK, run a single HTTP client instrumentation scenario, as opposed to the demo, where you're running, you know, lots and lots of things.
We did run into it in a couple places. For example, the SDK health metrics themselves violate Weaver, and so, we have a couple of Workarounds slash hacks in the conformance repo for those kinds of things today.
Cijo Thomas (Microsoft Corporation) 01:01:08 Got it. So it's like, you just mentioned that the SDK health matrix itself violated, so that means the Weaver is trying to check against everything, not just the HTTP one which you are after. It's trying to test everything, right? Okay, yeah, that's one of the reasons why I wanted to, like, see if we can tell Weaver, hey, only focus on SDK Health, or HTTP, or database, and ignore everything else, so it can run much… Much more targeted and produce, like, precise results.
Yeah, anyway, like, that's something which I would probably track in the Weaver issue, if it's not already open.
Trask Stalnaker (Microsoft Corporation) 01:01:42 Yeah, sorry, John.
Joshua MacDonald (Microsoft) 01:01:42 You're at time.
Trask Stalnaker (Microsoft Corporation) 01:01:43 jump in.
Yup.
Joshua MacDonald (Microsoft) 01:01:45 And Josh didn't get a chance to talk about Weaver. Failure issues, we'll talk about this again. See you next time.
Cijo Thomas (Microsoft Corporation) 01:01:50 Yeah, yeah, sure.
Trask Stalnaker (Microsoft Corporation) 01:01:51 Bye, y'all.
Cijo Thomas (Microsoft Corporation) 01:01:52 Thank you, bye.
