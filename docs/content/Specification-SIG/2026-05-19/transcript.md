SIG: Specification SIG
Date: 2026-05-19
Duration: 80 minutes
============================================================

## Zoom Recording Transcript

Armin (Dynatrace) 00:04:38 Hello, hello?
Jack Berg 00:04:43 Hello.
David Ashpole 00:05:17 Hello?
Hey, Jack.
Jack Berg 00:05:22 Bye.
Armin (Dynatrace) 00:05:27 Right, we have a fairly packed agenda today. Antoine, you will be first. Do you want to share the screen, and are you ready to prepare for it?
atoulme 00:05:43 Yeah, just a second, folks, setting up.
Armin (Dynatrace) 00:05:47 Alright.
atoulme 00:05:48 Excellent.
Two showing up.
So… So, videos… share… Chair.
This… Okay.
Morning, afternoon, evening.
I'm going to talk to you a little bit about the packaging SIG, which is a new SIG that has been approved.
As of something like 2 weeks ago now.
By the TCNGC.
We're going to talk a little bit about, the goal of the SIG. I wanted to start with something maybe a bit more… Tactical, simple.
We have a PR open right now against Community.
You can take a look.
So, post approvals, just so everybody knows where the resources are.
We now have… so there's some simple idiots, like, just making this a bullet point.
At least. We also have, now, a hotel packaging, Slack channel you can reach and join or ask questions there.
We also have, and we're going to go over this today, a project in GitHub for the roadmap.
And we have a repository that has been provisioned under OpenTeometry-packaging.
We, have SIG meetings that have been established to be weekly, Wednesday, 10 a.m. Pacific Time.
This time might change.
It will change, things change.
But right now we, in thanks to TED, we have a dock.
So that we can follow along here.
So… This is just a very simple thing, just if you were looking to understand better, you're interested afterwards, these are a number of tactical items that we have.
Any questions about this PR?
Straightforward.
Okay. So, now we have, the project that we started to work on.
Last week, we started to file some issues.
That might be a bit too technical, so maybe let's re… First and talk about the goal of the project.
So, the system packaging project is gonna have, first and foremost, a Phase 1, Which… is going to establish a number of packages that we want to make, available for the ecosystem to download and install up until M3 packages.
Starting with the injector project.
And joining with other SIGs, such as the OBE SIG, to provide a cohesive experience and a better coverage for the various application runtimes.
Ultimately, we want to make it easy for people to write APT installer pentametry.
It becomes available upstream in your distribution of choice, and that makes it easy for people to install.
Right now, it's kind of difficult to install everything from OpenTeometry.
You have to go download from GitHub, have to pay attention to details about versions that are supposed to work together.
So people who are not experts, you know, would be fine to start also with the transformation, so that they can start to experience open telemetry without having to do the burden of doing the, adoption of the OpenTelemetry libraries in their project.
So, our immediate roadmap is to create infrastructure to publish those packages.
We just want to have an APT repository in an RPM repository.
We will be targeting specifically Debian, Ubuntu.
And, Rail, so Red Hat and CentOS and whatnot, so that we can allow people to install, the injector and the SDKs in a way that makes, makes sense.
And this, this is the focus of what we're going to, support.
We're going to go… Again, the injector, OB is the capacitor respondation.
And we will also copy… so we already have our PMW packages for the collector.
available in the releases today. We will just push them also to that releases, repository.
And make sure that we align with the packaging versioning policies that are used by those distribution.
will make it possible to extend with vendor packages, so if you have a vendor package for Java, you'll be able to swap that in.
And we will, as much as possible.
make declarative configuration a first-class citizen of the system packages, meaning that we'll be looking for those files as part of the configuration of those SDKs.
And about things that are out of scope… We're not looking to do anything but Debian and Unreal.
We don't know yet how to go about that. There might be an APK in the works at some point, but that's, That's down the road, it's not as important.
We're… we're not yet looking to get the profiler in there, it's more complex.
We're not trying to build container images yet.
Tigran Najaryan 00:11:31 Can you… can you clarify something? It says SDKs and auto-instrumentation, so the language FDKs will be also… so you do that install command.
It essentially brings everything OpenTelemetry, like, the… injector, the collector as well, the SDKs, auto-instrumentation, all of it for all languages.
atoulme 00:11:54 Yes. For the injector, if you were to do this, it would install everything. I can show you a bit about the way that we're looking at it, and we have a PR open right now on the packaging repository to start the structure and the dependencies between those packages.
We've taken the liberty to try to make it a bit more… Cute to look at using Figma.
So, this is a view of this, where we have dependencies, so here we're using the notion of virtual package.
This is becoming more of a… like, the way things are being fulfilled in this dependency environments is that you can have concrete packages, and you can have dependencies which are saying that we want a package that fulfills a particular requirement, right, such as the injector. For example, if you wanted to swap it with your own, then you can do that by offering another package that offers the same capacity.
as part of it. So that becomes a meta-architecture Where if you were to install OpenTeometry.
It would depend on virtual packages for Injector, Java, Node.js, and .NET, in that case. The Open Dementry injector.
You would have… the Ubuntu Injector 1, actually providing this, this capacity.
Oh yeah, so the OpenTeemetery injector package provides the OpenTeometry Injector 1 capacity, which fulfills the OpenTeometry requirement.
And so on and so forth.
Allowing you to do this, so that we can have a dependency tree that can be fulfilled through this. Now, the only reason…
Tigran Najaryan 00:13:34 My question specifically, I guess, was more about the SDKs. Do you also bring the SDKs, or just the runtime portions that are necessary for instrumentation?
Is this more for developers, or more for operators, for people who need to…
atoulme 00:13:49 Corporate.
It's a Java agent, it's the Node.js library, but packaged in a way that is ready to be injected into an application. I think, you don't see Python yet in there, because we're actually working with the Python team, so that they package it in a way that is just one blob, one… library, one agent. So there's… there's actually work that has been, taking place in the last week or so, with, the Python seek to start to work on that.
But every other… language here, java.js.net, has a bit of a download where you can download everything packaged, ready to be injected into an application.
Tigran Najaryan 00:14:28 Okay, so if I'm a developer, I… and I want to write custom instrumentation in my code.
This is not what I would be using. I will just go and download the Java SDK, compile against it, or C++ SDK. This is for operators, this is for different persona.
atoulme 00:14:45 That's right, and it's still compatible down the road, so you could, you could say, let's say, you know, I just want to depend on the API, and I'm going to annotate everything I like with my span annotation in my Java code, and then I auto-instrument, and this gets picked up, and it's still being reported through this agent method.
So we're not… we're not forbidding one or the other, it's great, everybody can get something out of this.
Ted Young 00:15:10 I think there's a point of… that should be clarified here, is there is nothing… installing things this way is no different than if you were to install it the regular way.
It's using the same, you know, injection mechanisms, right? Like, the same auto-instrumentation mechanisms. It'll be the same libraries, instrumentation libraries, same API, same SDK.
Which means this is also a good… like, for… for developers, like, not just for operators, but also for people who are trying to, like, kick the tires of OpenTelemetry and just, like, try it for the first time. This is, I think, a very easy way For people to do that as well.
atoulme 00:15:57 Yeah, you could also bake it into your EC2 instances, or… you know, it's becoming easier for people then to have it as a tool that they can deploy.
We… Yeah, so I think where we're going to spend most of our time in this SIG is going to be configuration, and where we place this configuration in a way that is well understood, that is composable, allow people to maybe overlay a configuration file. So, for example, you're very happy with the standard OpenTemmetry Java auto-instementation.
But because you're a vendor, you would like to have an additional file in that folder.
that changes the way the Java agent is behaving, or maybe you want to deploy something additionally to that. This allows you to do that using some composition aspect that will… you know, look into to make it possible. The injector already is thinking about it this way, using a inclusion package. If you're familiar with how, let's say, NGINX works, right, it's all in a conv.d type folder, where you can add additional configuration.
This is also the way we want to make it composable, so that we can layer multiple packages on top of each other without problems.
But I jumped a little bit on the latest here. This is what we're working on right now. This is going to take us quite a while to make sure we got right, and there are really two prongs to this work. One is making sure we have this metadata Correct.
And the other is the practical work.
Of finding where to host all those packages in a way that is cohesive, makes sense for open telemetry, is vendor neutral, allows us to have some sort of continuity, make sure that it doesn't go down in 3 days.
Right? And so there's… there's work there.
So we started to look at this in the initial maintainers of this SIQ, We raised their hand when we were working on the initial documentation.
Started to kind of, meet last week. We were just very early.
With one member here looking at, investigating package hosting options.
And then another here, working on, the validation of that metapackage structure.
And this is going to take us a little bit… this is what we want to make sure we get right.
Once we have this right, we can… we can be composing.
Go ahead.
Jack Berg 00:18:17 So… We're going to do things like what the operator does today, where the operator publishes these, these images, and these images have, directory structures which are sort of implicit conventions on where different resources are located.
And packaging is going to do the same thing. It's going to, like, have these conventions that are formed about, like, where to put the Java agent, where to put config files, where to put other resources that are involved, from auto-instrumentation.
And, one thing that I think we all need to do as a community is come together and, like, share the ownership of this.
And so, when the packaging SIG says, like, hey, it's time for us to start packaging up the Java agent, like, I want the Java agent maintainers to… and the Java core maintainers, like myself, to go be code owners to that part of the packaging repository where that is codified, so that, like, we own the unit tests, we, you know, are consulted.
and, you know, give the thumbs up to topology of these resources. And then I want the same thing to happen for the other languages as well, JavaScript and whatever. And so, you know, I raised my hand and, because… and I see you nodding along, I know you're in agreement with us, but I think that, like the other people from the community that are listening to this should kind of expect this, to happen some point in the future. Expect to hear from the packaging SIG and to, you know, kind of coordinate with them so that we can all You know, get the benefit from this.
atoulme 00:20:00 Yeah. We have some protot work from the Injet or SIG, which we… where we already have The injector right now is packaging inside its own RPM all the SDKs in some bespoke place, and there's an expectation of a configuration file to be inside a certain folder.
We will try to port that over to the packaging SIG, and as we do that.
We will then involve the SDKs to become code owners and make sure we have their inputs, because we want to make sure we get this in a composable, maintainable way moving forward.
Armin (Dynatrace) 00:20:36 Antoine, since we only have 2 more minutes here, and you have a bunch of maintainers in this round, is there anything you'd like the maintainers to know specifically what you'll need from them, and what the expectations there are?
atoulme 00:20:51 Well, first, let's set the expectation that, this SIG will be reporting on a quarterly basis to this crowd here, so I will try to be back in, we're in May… is it? Yeah, August, end of August, September, to do a report, and I will do that on a quarterly basis moving forward. I will try not to take as long, maybe if there's nothing to say.
That's great. We don't mean this, so there is a little bit of a… there's an entry here of, like, how long do we want this packaging sig to be running? The expected timeline right now is a little bit of a to-do. I will fill that up, because right now we're still getting started, but I think we would want to kind of make sure Phase 1 gets executed in this calendar year, and then we will also move on to maybe more of a maintainer, you know, less active role. We'll see exactly.
So with that, yes, I, you know, I would expect that I will be back and asking, questions. I might join also specific SIGs to ask questions.
Please don't let me know if you have any questions. Thank you.
Tigran Najaryan 00:22:00 Anton, I think to follow up on what Armin was asking about, is there anything that you need maintainers to do now for you, or in the observable near future?
That you depend on for this to succeed.
atoulme 00:22:14 Of course, please, if you have not reviewed this proposal before, please do. If you have any comments or questions, please ask, either on Slack or Open Issues. If you have any questions about our existing implementation, please go ahead. We currently have a PR Open… So Okay, I'll share my screen for one more second, and we'll stay inside those 20 minutes, I swear.
So, if I go to… Can I go to my packaging sig here?
Armin (Dynatrace) 00:22:47 You've linked it in the, sync notes as well?
atoulme 00:22:52 I just want to make sure you know about this PR, which is… important, so we have… currently, this critical PR is going to set up how we're going to set the architecture and dependencies between all the injector and SDKs and all that. I went over that earlier with that little Figma trading view.
This is the real job.
So this is the actual real work that's going into this. Please, if you care, please review.
Please, make sure this is not something that you have any qualms with. I don't think you will, and we can change it.
So, you know, this is, this is the first work order we have.
Jack Berg 00:23:33 Can you… can you tag the maintainers of each of the respective, language SIGs that are experts on that?
atoulme 00:23:41 Yeah. Okay. Is that… okay, yeah, sure, I will do that now.
Ted Young 00:23:46 As mentioned before, the one language that we've identified as, you know, we do need to do some work with is Python, but we're already engaging with them.
atoulme 00:23:56 Yeah, and it's… we're not starting with it, as you can see, just to be on the safe side. There's no reason to push.
Quite there yet.
But we're getting there. It's really encouraging.
And thank you, Ted, for putting us in touch with the Python dev.
And that's it.
Armin (Dynatrace) 00:24:17 Thank you. Thanks for the update as well. Looking forward to hearing back from you then. It doesn't really need to be quarterly. If you have intermediary results or anything that you need from the maintainers, feel free to come back earlier.
atoulme 00:24:31 Go meet now.
Armin (Dynatrace) 00:24:31 freak.
Didn't…
atoulme 00:24:33 He'll be here every week.
You would be.
Armin (Dynatrace) 00:24:36 As long as it makes sense, sure.
Alright, then let's move on with Jacob, who has a demo for us for the policy OTEP that he's working on together with Josh.
jea 00:24:48 Yeah, thank you. So today I'm just gonna show some of the stuff that I've been working on. I'm gonna go through the policy spec very briefly, and then give a demo of, specifically the collector processor that I made, and the Go library that I made. I'm gonna show off some of the features of filtering. David, I saw you left a comment about sampling on there, so I'm going to show that as well.
I'm gonna share my screen here.
So… Yeah, over here, on the right, you can see the… This is the telemetry policy spec, the OTEP, I mean, not the spec, and… In here, the goal is to define what I'm… what I think Josh and I are sort of thinking of as a universal configuration, for doing, telemetry processing functionally, right? It's… We want to be able to do, filtering and transforming, not just in the collector, but also in the SDK. We want to make it easier to do remote configuration for these things. It also… The goal is to make it so that we can, you know, implement this in other projects as well. I've been coordinating with some folks from the Prometheus group about getting this natively in Prometheus, and so it's really providing a universal syntax for expressing user intent for this type of thing.
The goal of these is to be typed.
With very clearly specified behavior, implementation agnostic, as I said earlier, with a basis in OTEL, in OTEL's language, as you'll see.
We're also aiming for them to be very standalone. This is not pipelines, we're not trying to replace pipelines at all.
We're just trying to make… make these independent policies function.
I have some more rules in here, but we can talk about that later if anyone's interested. In terms of the ecosystem, as I mentioned, there's a few ways that we're hoping to integrate this into the existing ecosystem. So, around SDKs, we'll be able to embed these libraries and SDKs.
The collector, as I'll show today, op-amp, and this is pretty interesting, the model for this is transport agnostic. So, OpAmp just becomes a transport layer for policies, and op-amp, as far as I can tell, will require no changes, to its existing capabilities.
I have a sort of example schema here for what a policy looks like. Not maybe super interesting to this group who's looked at plenty of produce.
But you can see an example of the matcher, and so… The goal here is to provide a way for a user to specify very targeted what they want to match on in terms of what they're trying to do. So, because this is a log matcher, we have access to log fields. We can also access log attributes, resource attributes, and scope attributes. So, very OZL-focused in its syntax.
This is about design, we don't really need to go into that.
Then there's been conflict resolution.
A bunch of prior art, and then… I have here at the bottom a bunch of prototypes that I've been developing over the past couple of months.
If you're interested in seeing some of them, the Go one I'm going to show today, but I also have one in Rust and in Zig.
I have also a library here for conformance.
Testing, so this is something that would also be… all of these sort would be part of a donation.
And would work on it as part of OTEL, but I have a pretty large suite of test cases to check that each of the language implementations functions as I expect it to, so that we're pretty confident that across languages we'll have Equal, like, usage.
So, before I move on, any questions before I sort of show a demo of this?
Cool.
So, to demo this, I was just gonna show an example of a bunch of policies that I wrote. Make this a little bit bigger. On a large monitor.
It's a little bit bigger. So, very simply, this is sort of, like, one of the core things that you might see, is a drop policy. So, you can see here that… sorry.
My screen is huge. So you can see here that we're matching where the log attribute has an attribute called dbsource, and we're going to match on the regex nginx, and we're saying that we want to keep none of them. All of this proto-syntax, by the way, is definitely subject to change, so don't… judge that, too hard in terms of the OTEP, please. Similarly, you can see here that we're trying to match on if we find a debug and trace in the log body. We might also want to match on, you know, more complex regex, something where we do You know, a dot plus, and this could be, you know, such… this may be optional, or something like that.
Right. So you can do pretty advanced regex matching. The constraint that I have here is, no backtracking on the regex. That's really a performance thing. If you're familiar with, like, regex, syntaxes.
Pcre2 is very not performance, whereas, like, RE2 is pretty solid. So that's sort of a design decision here. If somebody really wants backtracking, we can talk about that later.
But you can see, you know, all of these are relatively straightforward.
Similarly, I have support for doing metric filtering today. Later on, we could add support for metric transforms and things in that realm, but as you get into transforms with metrics, you have to think about, downsampling, aggregation, and that's something that I didn't want to go too… too advanced into right now.
Similarly for traces, I already have support for all of the modes from the probabilistic sampler in the collector, so that's what I sort of inspired the design of this on.
So, that means I have support for, the various modes that the collector supports today. So, whether that's, hash seed, proportional.
Equalizing, and then I… and then just the basic one for percentage-based sampling.
For each of these, you can supply a… I also support these for logs, so you can use the same approach for sampling on logs as well. You just have to supply a sample key for logs, otherwise it won't work. You won't have anything to sample off of.
So, to show what this looks like in practice, I have a collector running here.
Let me make this a bit bigger.
Let me just post that.
And close… that.
So I wrote a bunch of sample payloads. This one, is to verify that we are matching Up here.
For dropping echo logs, so… You can see that… match, logged from NGINX should be dropped. If there's an NGINX prefix, that should also be dropped, because this is a regex match.
And then we want to keep something where it's Python, and if the attribute isn't present, then it should also be cut. And so, just to sort of verify that.
Let me do this… And we can see that, you know, we see the expected behavior here, right? So… We indeed kept the Python one, and because the attribute wasn't present, we kept that as well.
Interestingly, the provider that I wrote also supports, hot reloading by default, so we can, get rid of this. This will reload, and I think I've added support for this in the collector, let's see.
And… Maybe not. I think it's because this is in a Docker container.
But, you get the idea. Anyway, on to metrics… Just the one. Metrics… So, you can see here that we want to match and drop, the system load metric. So, where system load, let me go down here.
So, in this case, we're doing a regex match on the metric name, so let's just say that we think that this metric is terrible, and we just want to throw it out entirely, and anything like it. We just want to toss it.
So, you can see here in the scope metrics payload, we have system load 1M, 5M, but we want to keep the system CPU, because we like that one.
So, when we send it, And I will delete this again.
We can see that we only keep, you know, the system load metric.
And so that's something that I know the Prometheus folks really want, to be able to do this type of dropping, from the client.
And then the last one that'll show is maybe keeping error spans.
So… Traces… So, you can see here that we have an error span, and we would like to keep it, therefore we do. So we're, you know, maybe kind of straightforward, but I think you get the idea.
So, any questions on this? Anything that people want to see in this demo? I can sort of show anything that you're interested in.
Tigran Najaryan 00:34:46 Jacob, about the goals, you said you want this to be added to the collector and to language SDKs.
And the concern I have is that this is… cumulatively, this is going to be a lot of work for language SDKs, right? Whatever you do, times 12, It's going to be… lots of work. Why not just the collector? Why? Because we have lots of other types of processing we do only in the collector.
Alright, and… then that's… seems to be sort of a slippery slope, right? Why don't we bring the entire processing within the collector into the SDKs then?
Why not just the collector, then?
Josh Suereth 00:35:28 I can take this, Jacob. So first of all, you're not guaranteed to have a collector in all environments, right? Like, you could be in AWS Lambda, you could be in Cloud Run, you can't.
Tigran Najaryan 00:35:38 Sure, the same argument applies to everything you do in the collector, right? Why this specific thing needs to be in the SDKs, and not enough to have it in the collector, while many other things we only have in the collector.
Josh Suereth 00:35:50 the idea behind this is you can stop caring about your architecture, and you can define your intent. So, these are meant to be idempotent, which means if I do it in the SDK, I don't have to do it in the collector. If I do it in the collector, I don't have to do it in the SDK.
But the idea would be, since we're gonna use OpAmp to kind of propagate these, we can actually advertise which ones we support.
And so, we can decide to run something in the SDK, or we can decide to run it in the collector. Doing it in the SDK, like dropping a metric, means we could be more efficient, right? Because we could say, you know what, this metric has always dropped, I'm just not going to calculate it.
So there's, like, there is reason to be at the edge. The other important piece of this is it expands beyond the OpenTelemetry ecosystem, where this is a, like, an intent-based thing to control telemetry collection that we can use with the Prometheus ecosystem.
Right? We could use it with other ecosystems as well. It's a specification, a way of distributing out these policies that anyone can enforce in anything. The policies have an expected behavior. So, the idea would be, it spans beyond it, and someone who's writing these doesn't have to care, necessarily, about the architecture.
We just have to make sure that we say, here's my intent, and I'm gonna push it to the thing that can do that intent.
Tigran Najaryan 00:37:06 Well, I get it. That's nice from the user's perspective, but from our perspective, from the perspective of developers of OpenClenchry SDKs.
That's a lot of difference, right, between implementing it once in the collector and doing it many times in all the SDKs. Maybe what we could do is limit the SDKs to only implement the policies where what you said is important, that from a performance perspective, applying it in the SDK makes a lot of difference. Whereas for some other things, it doesn't really matter that much. You can do it later on as well.
Josh Suereth 00:37:43 Yeah, that's a good point, and I think it's in the OTEP, Jacob, of, like, the notion that you can advertise what policies you support.
So that, like, an SDK wouldn't be expected to do all of these.
But there is a subset that we think, like, trace sampling, for example, we probably want that in the SDK.
Tigran Najaryan 00:37:58 Yes, where you drop, you eliminate data, that's where you gain efficiency. Okay, makes sense.
Josh Suereth 00:38:04 Yeah, and if I'm using an old SDK that doesn't support sampling, I might want to control it in the collector, because I can.
Tigran Najaryan 00:38:10 Yeah.
Josh Suereth 00:38:10 Great, great. Yeah. But you're absolutely right, not every policy is available to everybody, and SDKs and languages can choose which ones they want to implement.
Tigran Najaryan 00:38:20 Okay, sounds good. Thank you.
Jack Berg 00:38:25 I think I'm next. So we've… as I think a lot of people on the call are aware of, there's, like, limitations in terms of what types of filtering you can do in the SDKs themselves. Traces are the only thing that has, like, something in the pipeline that is dedicated to filtering in a sampler.
logs… log processors and, you know, and span processors, those are not filtering-type things. Like, the architecture is you call each span processor that's registered, they're not chained, such that one can stop data from flowing to the next. And so, you know, another limitation, even within traces, that has, like, access as the sampler concept, is they don't have access to scope information.
they don't have access to resource information. And so, to really do effective filtering in the SDK, you're looking at some sort of delegating exporter.
Something that wraps another exporter, and can, like, apply a filtering policy, and then call another exporter with, like, you know, your filtered data.
But the problem with doing it at the exporter level is that that can't actually inform, like, it's… we call our exporters asynchronously, and so you can't actually inform the collection of the traces, the collection of the metrics to disable these things based on the policy anymore.
And so, there's, like, there's something missing that would need to be resolved in the SDKs in order to do effective policy enforcement down in the SDKs.
Josh Suereth 00:39:55 I'll jump on this, too, because I did this part of the OTEP. So, the OTEP includes… there'd be a set of SDK components that we'd specify, and include in the SDK to do policy enforcement.
And again, the idea is that we can be incremental, we don't have to bite the whole enchilada at once. So we could start with, in the SDK… the thing that I think is most important in the SDK is sampling.
So we would figure out a component in the SDK that would be like a policy sampler that would interact with the policy ecosystem. And you can read the OTEP for more information about that.
But then SDKs would effectively only support it for, like, sampling decisions, and we would want to make sure that that filter that Jacob was showing.
is, like, SDK appropriate and collector appropriate at the same time. Like, it has to be the subset of the two, not the superset. Although I might have gotten my arrows inverted, I don't… I… sometimes I do that. Anyway… But, but you get the point. So there, like, like, really, like, the first milestone of this for SDK has gotta be, in my opinion, like, like, sampling decisions and controls. Like, like, like a… kind of a replacement for Jaeger Remote Sampler, right?
But we can start expanding further and figure out what those components are, and that… the OTEP is not necessarily, like, exactly what those components are. There's a proposal, and it's a straw man, and we can pick it apart. It is, is this the direction we're gonna go?
around, like, building out this capability, and then we'll figure out the components and follow on work, right? So we can figure out, like… like Jacob said, don't pay attention to the specific details of the policy. The prototype is just to prove that there's a lot of value and merit in this, that there's some scaling that goes on here, and that, like, this has… this… this has legs.
And then we can figure out the details as we go forward.
Jack Berg 00:41:39 My point is just that, it's not just that you need to define new SDK components, like, you have to do a little bit more, you need to define new SDK extension points.
Like…
Josh Suereth 00:41:51 Yeah.
Jack Berg 00:41:51 The points don't exist. The points need to be modified to make this worthwhile to do in the SDKs.
Josh Suereth 00:41:57 there are some assumptions there that we will need to figure out as we flesh out the design of a policy. For example, do you need to know the resource… So, like, the resource policy for a metric, right? Do I actually need to know the resource at metric creation time to apply the policy, or can I use the fact that the SDK knows the resource to filter down policies that are just applicable to myself, and then the policy would only look at information available to the metric at that point?
to determine whether to record, right? There are things we can do here. So, like, as we…
Jack Berg 00:42:33 What's the metric extension point that you're going to provide an instance of that does that and informs the SDK on how to change its behavior?
Josh Suereth 00:42:41 Okay, so metrics is a little bit of a bad example, because I think we do have to build something new.
So you're right that I think right now the extension point would be a metric reader wrapper.
And that is awkward as hell and not ideal, and I think we can do better. But again, like, this is a walk before we run thing. I do think there's a set of things we need to do in the metrics SDK anyway.
But we could implement policies in a not ideal fashion early, and then expand later.
Jack Berg 00:43:11 Right, and that's… yeah, exactly. So the not ideal fashion comes in the form of, like, a metric exporter wrapper that, like, does this filtering, but, you know, it's not ideal in the sense that those policy decisions cannot be propagated into the SDK internals to optimize those.
Like, if it's… yeah, so…
Josh Suereth 00:43:30 That might be… that might be, like, a V1 milestone, where, like, the end state is to figure out how to wrap this all in a nice bow, and we want to prototype that, of course. But yeah, like, I can… I can absolutely see that, yep.
jea 00:43:47 Are we at time, or do we have more? I know Ted also had a question, but…
Armin (Dynatrace) 00:43:51 Not at time, but over time. Oh, sorry.
jea 00:43:56 I can take Ted's question offline, if that's okay.
Ted Young 00:43:59 I can address… I'll address it as part of my little time block, so it's fine.
Armin (Dynatrace) 00:44:05 Like, later on, on a different topic, you mean?
Ted Young 00:44:10 Yeah, yeah.
Armin (Dynatrace) 00:44:12 Okay, alright. Then, let's move on.
This… Pellarette, right? You have two items there.
Free, actually.
Pellared 00:44:22 Can you share? Yeah, can you share? I tried to go very quickly.
Armin (Dynatrace) 00:44:26 Yep. True.
Pellared 00:44:26 Mostly it's asking for… mostly it's asking for reviews and asking for feedback here synchronously, if someone wants to discuss things here with bigger audience.
Jack Berg 00:44:40 My opinion is that these two BRs have been open for a long time. I'm sorry I, you know, didn't review them until recently, Robert. You know, I don't think anybody has voiced dissent on these, have they? Are there any open dissenting comments?
If not, they have the required approvals, and we should proceed with them.
Pellared 00:45:03 Yeah, I think we can give one more day, just if someone has any opinions, just to give one more day.
I also think… I also think there are no blocking or actionable comments right there.
anymore.
Yeah, this was the one, this is one… the one, and Armin, you can also open the second PR.
So this is more like a clarification.
And the second is only about, Using the same pattern for, for encoding a single attribute.
And it also has a bunch of approvals.
Okay, so maybe let's follow up to the next topics to gain some minutes.
Armin (Dynatrace) 00:45:48 Next ones are RCOs.
This one here.
Pellared 00:45:56 Yeah, correct.
So.
Armin (Dynatrace) 00:46:00 its OTLP request size limitation.
Pellared 00:46:03 Yeah, this was quite new, and, Tigran, I, we, together with Felix, we had responded, to your comments. So, the last time we have been discussing it was the question about the size.
Which is requ… which would be good enough for the profiling, and Felic said that in most cases.
32MB will be good enough, but ideal will be 64, because then it will be very unlikely that we will drop anything. And there was also a question whether, we want to have some splitting capability, that the exporter will split the requests into into, you know, two subsequent, requests, but both myself and Felix find that, it… first of all, the efficiency is questionable, because you will need to split the dictionary into two things, you will need to, it will not be a simple task, and I also want to trade that this will kind of also be, then it is kind of against the idea of the initial PR, which is avoiding DDo scenarios when someone wants to, basically, Just push too much data.
And also the limits are all… were already defined, or the configuration of the limit was already in DPR. It was just as May. I proposed to have it as shield. It's already implemented, it will go.
And I think we should… I think the missing part as a follow-up is also added this configuration to the OpenTelemetry configuration, to the OTLP exporter.
However, I'm also not sure… I have not looked there yet, but I'm also not sure how to add it, given its development, and the… I think the OTP corrects, I think the OTLP exporters are stable in the auto configuration, then probably I'll need some help from Jack, or maybe Jess, try to find, find somewhere how to add, development attributes, sorry, field to existing stable components.
Jack Berg 00:48:14 That's… we have… we have facilities for that, Robert, so you can definitely add, you know, a development property to, you know, a type that already exists and is otherwise stable, so that's supported.
Pellared 00:48:25 discovered not checked it, because, yeah.
Jack Berg 00:48:27 One question I have for you is, like, so, like, let's say there is a, like, a size limit that we impose, and, you know, this is a config property that we're passing to, you know, these OTLP clients.
how are these clients going to enforce this? Are they going to be responsible for, like, computing the size and, like, not sending the request if it's over the… over the limit?
Pellared 00:48:54 Yep, that's correct… that's how it's implemented right now. You can check the PR. I think it's… I'm not sure if it's… I think it's already implemented Go in .NET. I'm not sure if it's not even implemented in Java as well.
Jack Berg 00:49:05 I don't think it is. There might be some default limits.
Tigran Najaryan 00:49:08 It's actually a cool place.
Pellared 00:49:09 We don't know.
Tigran Najaryan 00:49:11 There's two places where enforcement happens, right? One is on the client, one is on the receiver side as well, right? The receivers are supposed to reject the request.
And it's, it's, with an error code which says it's not retrial, not to retry anymore.
That's the expectation, that both the client and the receiver are expected to honor the configured limit, and the limit may be configured differently, that's why you need to enforce it in two different places. The client may decide to send, and the server still may decide to reject.
Whoever needs that higher limit, essentially, they need to do the configuration in two places, in all of the clients, and in all of… in the receiver side as well.
I think that's fine.
What we were discussing about splitting is essentially to simplify the user experience, so that you don't need to do that configuration manually.
it's obviously… Significant complication compared to enforcing a limit just by dropping it.
And I agree with, I guess, your assessment, guys, that we should just go for configurability now, and later, if necessary, we can consider adding splitting And also, when we consider it, it likely needs to be done in a way that preserves backward compatibility, or it's a new version of protocol, so it's obviously a significantly more complicated approach if we take that. So, I think I'm fine with that, saying that we're not doing splitting now.
We're aiming for configurability, and there is going to be a significantly high enough default that Most realistic payloads that we can imagine at the moment should fit below that, and if somebody has extraordinary needs, they can just change the configuration.
Jack Berg 00:51:04 And just like… just real quick on the configuration front, so if a… If you pass a payload or an export request that will exceed the client's configuration.
the client shouldn't even attempt to send it over the network, right? It should compute the payload size, you know, as a prerequisite to actually encoding this on the network, and see that it's too large, and just say, like, hey, I'm not going to send this, and just, like, fail the export request.
Okay.
Tigran Najaryan 00:51:36 Can we… is there… is there another option for the client to, instead of dropping the entire thing, try to truncate it to fit within the limit? Do we want that to be an option available to the client, if… if the client is able to do that easily?
Jack Berg 00:51:53 That's part of the complexity, that bites off some of the complexity of this splitting suggestion, because, you know, you'd need to decide where to truncate in order to not have corrupted data, right? So you need to truncate at the record level, at some sort of record boundary, whether it's the metric data point or log record or span, and so you need to have good facilities to be able to compute the size of individual records and choose a logical cutoff point.
Tigran Najaryan 00:52:25 Okay, so it's essentially drop-all, we're not trying to do anything clever there.
Because it's… if you try, you bring all that complexity, almost all of it, that you need for splitting.
Sounds good to me. I just wanted to be explicit that we're not doing it. We're just dropping the entire payload, if it hits the limit.
Okay.
Armin (Dynatrace) 00:52:55 Thank you. Please continue reviewing on the PR, and last one by Robert.
This one here.
Pellared 00:53:03 So… Yeah, this one is just asking for… just for double-checking for reviews. I think, yeah, I think it's… So, it's mostly for stabilizing environmental variable carriers, and it's just, one of the aspects Which was, well, not obvious when I was reviewing other PRs. Also, this is, like, also JAX, and I think Python implementations and other. This is a very thing, easy to miss during implementation, so I decided to call it out explicitly here.
And that's all.
And also, I do not see any other missing points in this document, so if anyone sees some missing parts, then please call… just reach me out.
That's all for me.
Armin (Dynatrace) 00:53:52 Thank you.
Then we'll move on with TED.
Will you be sharing yourself, or should I?
Ted Young 00:53:58 Yeah, let me share the screen real quick.
Okie doke.
So, this is a, new project file, for lack of a better place to put it.
We had a OTEP called Stable by Default that was basically all of the work that we hashed out with the CNCF as part of their due diligence and review of OpenTelemetry for graduation.
Where we identified OpenTelemetry as in a great place, we're graduating, but there's still a set of work, that they would like to see, and we also agreed that we would like to see in order to kind of finish out what we initially started.
The way that document got laid out, it was feeling a little bit difficult to make progress. It felt a little open-ended, just the way the work streams were laid out. We were feeling, like, a little blocked on, like, how do we actually move forward on this stuff?
So, this doc is an attempt to kind of rewrite the intention of that doc into something that's hopefully more actionable in terms of the work streams.
The name stable by default was weirding some people out, so I switched this to being called OpenTelemetry GA, or Generally Available, because that was the term we used way back in the day, when we thought this would just be a quick and easy thing to deliver tracing metrics and logs to everybody, everywhere.
But basically, that's the idea here, is, we want to deliver tracing metrics and logs in the collector, to everybody, everywhere, in a way where, it works, and they can install it, and everything's stable, and everything they're running in production should be at least 1.0.
And we're, like, most of the way there, but there's a bit of work that still needs to be done, kind of across the board.
In order to finish all of that stuff out.
And if we can finish all of that stuff out, our reward is we now have an open roadmap where we can kind of choose our own destiny, because we will have totally finished what we initially set out to do.
So I would love people to review this doc. As I said, it didn't seem to make sense to have this as an OTEP, because almost none of the work in it relates to changing the spec. It's almost all, you know, different project work, and since we're doing that kind of Project management out of the community repo.
I moved it over there. Though, as I noted here, we don't fully have like, high-level workstream… tools or roadmapping tools, we just have project files.
So, that's part of what I think we need to change.
So, I would encourage people to look over this. In particular, what I'm interested in is, like, how much detail we need for each of these work streams in this doc for people to feel comfortable that, like, this is the right scope of work to get things done.
And if once, maintainers have had a look at this and feel like they're comfortable with it, we can merge this stock, and then for each one of these work streams, you know, create… a sort of project file or something that gets into the details about it. I tried to separate everything out in a way that allows a single SIG to be the one driving, driving the work, I think that was one of the main differences between this and the original OTEP.
Just to briefly go over what seems to be the remaining work, There's some work related to stability. We have a lot of components that are de facto stable, right? And we also have some components that are genuinely experimental. But because everything's 0.x, it's hard to tell, as an end user, what I should be running in production.
So what we're proposing here, since we were asked to deliver a mechanism for users to be able to tell what's production-ready or not, is a simple one. If it's 1.0 or higher, it's production-ready.
And if it's 0.x, then it's experimental. We don't have anything that's 1.x or higher that's experimental, so that's convenient. But we have lots of things that are 0.x, that people have been running in production for years.
So, the stability chunks here are those parts. One big one is the collector, needs to go 1.0. That's obviously owned by the collector SIG and their roadmap.
But I would love to get maybe some high-level color in here from the collector maintainers about what they see as, like, at a high level, what's the goal of their 1.0 roadmap.
The other big chunk of work we've identified is instrumentation. We have tons of instrumentation packages, that's the biggest surface area in OpenTelemetry. It's currently owned by the community and contrib repos, but OpenTelemetry doesn't work Unless the instrumentation works. We're trying to stabilize the semantic conventions, but we also need to bump all of these instrumentation packages to 1.0, which means somebody needs to take ownership of them.
And to make that easier and more effective, we want to have better tooling for managing that instrumentation.
The SemCon tooling SIG has been hard at work, in the background, building a set of tools, and we're going to be, test running those tools in the GenAI SIG, trying to use Weaver and tools like that to manage the Gen AI instrumentation that we're writing in Python.
If that… proves successful, then we're going to try to export that model and see if we can use it as a way to encourage people to take over and manage the instrumentation and get it to 1.0. But figuring out some subset of this instrumentation that we figure is, like, critical in every language and getting it over the finish line. This is actually, like, the biggest ball of work in this whole thing, in my opinion.
The other aspect, that… We've identified, in terms of OpenTelemetry being generally available, is that it's installable and manageable at scale. We have ways where you can install every individual piece, but if you try to deploy OpenTelemetry at scale across a giant organization, you discover that while we have some tools that can handle some of this, there's no clear-cut, straightforward way to just deploy and manage manage all the pieces that we consider necessary for OpenTelemetry to work.
you know, as a complete system. We have a Kubernetes operator. It can deploy some things, and it can configure some things.
So getting the operator to a 1.0 where it can, you know, handle everything on Kubernetes, and then for Linux and, you know, figuring out some of the lower-level packaging details, we have the packaging SIG.
The third piece is OpAMP. OpAMP is not 1.0 yet, but if we want to say OpenTelemetry's deployable and manageable at scale, having this control plane… be feature complete as far as what we consider it needs, to do all of those basic operations. That would need to be 1.0 as ever, as well, in order for us to say we've got a stable 1.0 way of deploying and managing everything.
So that's the deployment track.
And, last but not least, we have a couple of, kind of, cross-project things that we need to improve and figure out. One is security. We have a security SIG, it's understaffed, it does have a scope of work it needs to chew through.
And so we need to get more organizations, involved in our security SIG to help us triage, and make sure that we're actually following through on our security protocols when we do have vulnerabilities reported to us.
And last, but certainly not least, we need to kind of revamp how we're doing roadmaps and project management.
As we come to the end of this initial set of work, we need to figure out kind of a better way for maintainers to have sort of more control over the destiny of the project.
I think we've identified this as, like, we've had a GCTC that kind of tried to manage the roadmap, but we want to kind of… We've been making incremental improvements on how we do project management, but we've been feeling a desire to kind of Blow that up, and… and be a little more… open to new ideas about how we could do project management going forwards. Jack Berg's created a bunch of issues in the community repo to kind of, explore different ways we could improve this, so I would encourage the maintainers to have a look at that. But I included it as part of OpenTelemetry generally available, because Figuring that out, you know, for the road ahead is kind of necessary.
If we can complete this big pile of stuff, then there's lots of things we could do in the future. There were some things in that initial scope of work that I put as out of scope, not because it isn't important, but because you technically wouldn't need To deal with these things, in order to… to deliver open telemetry as, like, stable and deployable everywhere.
So, that's the short, short version. Please have a look at this doc, and help me, flush out all of the individual sections here. Make sure there's enough detail here so everyone feels confident we can actually execute this.
That's what I got.
And we're at time.
Armin (Dynatrace) 01:04:24 Thank you. Evo added a PR where he's blocked on. I requested a review from the blocking reviewer there, so hopefully you'll find a follow-up there soon.
And that's it for today. Please take a look at the PRs in the agenda. Ted left a link to his PR there as well. Thanks, everyone. Bye-bye!
Ivo Anjo 01:04:46 Q.
Jack Berg 01:04:47 Yeah, bud, thanks.
