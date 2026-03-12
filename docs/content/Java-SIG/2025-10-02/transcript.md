SIG: Java SIG
Date: 2025-10-02
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/q9vBQvxHXISiwAMYrUgfvrm8rSOlryvM5fDAwSaLraz7NDFZHW2VzLyfpTWepiJu.gMjxHxdsHeulk6aN
============================================================

## Zoom Recording Transcript

**Trask Stalnaker** 02:25 Yay, folks.
**Jay DeLuca** 02:28 Oh, boom.
**Jason Plumb** 02:30 Hello.
**Trask Stalnaker** 03:12 Let's see, we'll wait on this, case Jonathan shows up.
Oh, and I forgot to… Forgot to read that.
**Jason Plumb** 03:28 There's a lot of words in there.
**Trask Stalnaker** 03:33 Oh, hey, Jonathan.
**Jonathan Halliday (IBM)** 03:38 I am.
Oh, I timed that right then.
**Trask Stalnaker** 03:49 Yes, and… Alright.
Forgot to do the homework.
**Jonathan Halliday (IBM)** 03:55 Don't worry about it, it's fairly verbose. I'm just trying to get my head around what the main use case is for the profiling.
Signal type look like, and what that means for functionality we might want to put into… the SDK.
So there's… there's a use case where we basically don't need anything in the SDK because the profiling's done by eBPF, And… the Java process is being observed, but is not participating in that observation at all, other than as a… you know, passive thing. There's nothing for the SDK to do.
And at the other extreme, we've got something like gaseync Profile or JFR doing the observation, and perhaps we want to drive that through config in the… the SDK, so that, A user can configure all the signal types in the same way, and… Doesn't have to special case the profiling bit.
So, if anyone's got thoughts on… Which of those use cases might be popular, which ones we want to support, which ones we want to rule out and say, if you go that route, you're on your own, sorry.
And what the implications of, those decisions are for… what functionality we put in. So, if we're driving async Profiler, for example, we… Do we want to ship?
native binary for that. What does that look like in terms of the build process? What does it do to the agent startup, and so on?
**Trask Stalnaker** 05:32 So, couple questions. The profiler configuration, this would mean, like, exporter, like, OTLP, Exporter…
**Jonathan Halliday (IBM)** 05:46 Yeah, yeah, certainly the exported part of the pipeline, but in order to have something to export, you have to configure whatever's doing the data collecting.
So that might be that we have a config that gets passed down to JFR, or passed down to async Profiler.
Or it might be that we say, you can figure those bits yourself.
Using some out-band config mechanism.
That isn't… isn't part of OTEL, and we'll just provide you with… Some object you can get a handle on that will accept a JFR file, a stream of JFR events, and export them for you.
So we're defining the scope of what we support as just the export, not the data acquisition part.
**Trask Stalnaker** 06:33 So that would be my initial assumption.
that we would… the SDK would… Have support that would have the exporter configuration support, and then we would have separate… library instrumentations, but it wouldn't be… the async profile at JFR wouldn't be baked into the SDK itself.
It would be, like, a separate library.
Which… would normally our instrumentation libraries depend on the API packages?
And so that's… That's true.
**Jonathan Halliday (IBM)** 07:17 for profiling, because there's something… Yeah. But yes.
So, what would that look like for me as a typical user if I want to bring up, instrumentation in my app for all the signal types?
the existing three I can figure through an hotel, config mechanism.
The other one, I've got to bake some kind of bootstrap into my application that will fire up async Profile or JFR, And I've got to do some manual wiring to then pass the output of that through to something I get from the the hotel code that gives me the export or pipeline. Is that the kind of model you're envisaging?
**Trask Stalnaker** 08:01 I was thinking more like, we have the OpenTelemetry SDK, instance, and we would pass this into the async profiler library.
our async profiling library.
And then the async profiler from the… could read… oh, no, but that… it has to register ahead of time.
**Lauri Tulmin** 08:31 I think, what we need is that, like.
Just having the exporter is… is pretty much useless on its own.
What we need is a library that allows building the data that can be exported.
It doesn't need to, like, be tied to any of the data.
**Jonathan Halliday (IBM)** 08:52 Yeah, like, this is the obtaining spectac.
**Lauri Tulmin** 08:54 Traces from, like, calling, like, thread, like, whatever, like, thread get tall, stack traces… And then, you somehow need to patch those stack traces into a payload, and.
**Jonathan Halliday (IBM)** 09:06 Yeah, so there's… there's two different things there. There's the… there's the capturing the data.
And there's the translating the captured data into a format that the exporters will accept.
And most of the code for doing that translation from JFR, I'm just bundling with the exporter.
But what we're… we're still lacking, then, is the… the code that… actually does the capture, configures JFR, configures Async Profiler.
To get to the point where there is… a JFR file.
that it can hand off to the exporters. The API for the exporter might be, please export this JFR file, here's a… A file object.
Right? We can do that.
I think it's going to be a translation.
**Lauri Tulmin** 09:56 complicated.
in the sense that, like, the JFR file can be, like, very large.
**Jonathan Halliday (IBM)** 10:02 Yes?
**Lauri Tulmin** 10:03 There needs to be some sort of, support for patching the data.
**Jonathan Halliday (IBM)** 10:08 Yes?
**Lauri Tulmin** 10:12 But basically, yeah, you need something that just is able to consume the stack traces.
I packed them into the payload, and somehow sent them.
And if you have that, then you can start working on, I think.
to different data sources, like JFR or Async Profiler.
**Trask Stalnaker** 10:33 How does the profiling SDK… is there a profiling SDK today? Sorry, of… Or is it… there's only a profiling OTLP exporter?
**Jonathan Halliday (IBM)** 10:46 There is only the exporter, currently.
**Trask Stalnaker** 10:49 I see, so…
**Jonathan Halliday (IBM)** 10:51 FilingSync does not plan to define an API, which makes this signal different to every other signal, which is a pain.
**Trask Stalnaker** 10:58 Not even an SDK. I knew that they weren't gonna have an API, like.
**Jonathan Halliday (IBM)** 11:02 There is no language-level API, and the reason is a lot of languages won't do this. Java and Golang I, Well, not unique, but they're the two major languages that kind of have a de facto profile, are defined as part of the language platform.
Right, Go has one baked in, and… Java's JFL.
For every other language, that's not the case. You tend to use an external profiler, and eBPF is becoming the common case for that.
And in those languages, you… don't need an API, because the thing being observed, the application, isn't involved.
the data is flowing directly from the eBPF profiler to the collector.
We could, we could. One of the use cases I've got is that… JFR can still be used, or async profiler can still be used, but what you do is you deploy a sidecar collector.
And it's up to the sidecar to grab the output of the profiler, which is a JFR file.
And deal with it.
And then the Java SDK doesn't do anything.
So that, in that respect, it's the same deployment as using an eBPF profiler. The Java process is being observed, but doesn't participate.
So that, again, then, in those cases, there's no Java API.
**Lauri Tulmin** 12:40 Yeah, but.
**Jonathan Halliday (IBM)** 12:41 only involved if…
**Lauri Tulmin** 12:42 But if you are going to parse the JFR file in another process, you still need to do it somehow.
**Jonathan Halliday (IBM)** 12:50 Yes.
**Lauri Tulmin** 12:52 In some sense, maybe we don't need that.
**Jonathan Halliday (IBM)** 12:55 The collector already is looking at this. The collector's like, okay, what if we want a collector endpoint that can receive JFR? What if we want a collector endpoint that can receive Golang's PPROF format?
And the collector will have a pipeline for translating that and being able to export.
**Lauri Tulmin** 13:14 profile. That there is no JFR parser outside of Java.
**Jason Plumb** 13:22 Oh, that's not true. I think the dog has one, yeah.
**Jonathan Halliday (IBM)** 13:26 The issue is that JFR isn't really a spec in the same way that the hotel stuff is. It's… the Java people consider it an implementation detail of OpenJDK.
And that is open, in the sense that it's open source. You can go and look at how it works, but they don't document it, and they don't guarantee it's stable.
So that's a bit of a pain.
**Jason Plumb** 13:45 Yeah.
**Jonathan Halliday (IBM)** 13:46 Java cheats a bit. The export I've prototyped for… this doesn't have to understand the file format, because Java's got a… an API that reads the file for you and presents you Java objects, so you're just writing a translator at that level.
**Lauri Tulmin** 14:01 The only problem is that, that actually parsing the JFR file It's kind of expensive.
**Jonathan Halliday (IBM)** 14:08 Yes Well, it's not so much the parsing, it's manifesting everything onto the heap just to serialize it again, which is a pain.
So one of the scenarios I have is, if this turns out to be too expensive, do we want to attempt something that… Both formats essentially are lookup table based. They've got a kind of dictionary to save space, so that duplicate elements only appear once in the dictionary and everything else is a pointer.
So it should theoretically be possible to write a kind of direct translator that copies the dictionary from one to the other.
And then, you know, remaps the pointers on the fly.
**Lauri Tulmin** 14:46 Even that might not work too well, because.
**Jonathan Halliday (IBM)** 14:50 Well, it'll churn a lot less heat memory, but yeah, it's still a non-zero cost.
**Lauri Tulmin** 14:54 Like, consider that, like, maybe you're all only, like, interested in some sort of, like, stack traces for, like, CPU, But if somebody has also turned on some sort of memory profiling.
**Jonathan Halliday (IBM)** 15:06 So you want to be able to filter the events in the JFR file? Yeah.
**Lauri Tulmin** 15:10 And then you will have, like, a whole bunch of more events there.
And you might, like, send more data than expected.
**Jonathan Halliday (IBM)** 15:17 Yes.
**Lauri Tulmin** 15:27 Yeah, like, coming back to the SDK, like, like… maybe we don't, like, need a proper SDK, at least from the start, but we definitely need some sort of internal API, at least, that allows building those…
**Jonathan Halliday (IBM)** 15:41 Yes.
**Lauri Tulmin** 15:41 Beautiful.
**Jonathan Halliday (IBM)** 15:42 Yeah, I mean, that pretty much exists. Right now, the API is the data objects that are used by the exporters.
So there's no… split between the public API and The internal one that the exporters used, they're one and the same thing.
And that's probably okay, in that it's not gonna be… anywhere as widely used as the API for the other signal types, because the apps are not going to talk it.
Only the… the handful of things that are exporting.
You know, there's basically going to be one component, probably, that knows how to ingest JFR and export it.
This is not something you'd typically do in application-level code in the way that you do chasers, for example.
**Lauri Tulmin** 16:29 Yeah, definitely correct.
**Jonathan Halliday (IBM)** 16:31 son.
**Lauri Tulmin** 16:31 Anybody can send logs, but, like…
**Jonathan Halliday (IBM)** 16:33 Yeah.
**Lauri Tulmin** 16:34 Nobody wants to build, like, profiling dates on an IP.
**Jonathan Halliday (IBM)** 16:37 AI.
If we have something that… we'll call it an SPI, or an internal API. As long as we're clear that it's, you know, moderately stable and supported, that's probably fine. It's not going to be a… a user-level API that's backed by the spec in the same way the other ones are.
But that has kind of knock-on effects on packaging, because, for example, the global OpenTelemetry object can't have a get profiling method on it, because what does it return? There's no API type for it to return.
**Lauri Tulmin** 17:22 Jack probably has an answer for that. I think, initially, when the events were incubated, we also had, A different class for getting to Global Event Provider, or something like that.
**Trask Stalnaker** 17:35 We now have, an extended open telemetry Internal class that we can put things on.
But it's really supposed to be for things that are incubating at the spec level.
Which this wouldn't be.
So I know that…
**Jonathan Halliday (IBM)** 17:57 I mean, it will be for the next few years, but yes, eventually I'd hope it becomes stable.
But what the scope of that stability is might be… might be different. If there's no API, we've… we've got nothing to say, this API is stable.
**Trask Stalnaker** 18:13 Yeah, I guess what I mean, is there… before… typically, the, in the core repo, the… before adding some incubating feature there, they like to see it, spec In development, or draft, or something.
**Jonathan Halliday (IBM)** 18:33 Well, the wire protocol spec's about to come out of experimental and go into whatever the next phase is, alpha, or whatever the… the next level of stability is. It's basically, we're at the point where the Sigers said, okay, we're done fiddling with this. It's time to get some implementations that are interoperable, and we'll… we'll try not to break things.
**Trask Stalnaker** 18:55 Yeah, and I think that's enough to build…
**Jonathan Halliday (IBM)** 18:57 Yeah, I mean, we've had some of the exporter code for a while, but we've not shipped it. We've had the flag turned off to say, you know, build this, test it, but don't push it to Central.
We really need to go past that point so that people can start kicking the tires on it.
So we have to make some decisions about what it is we're going to ship and ask people to evaluate, or offer them as functionality to try out.
You know, one extremely answer is nothing, just go and use eBPF, And at the other extreme, it's, we'll take care of configuring JFR Async Profiler for you, we'll give you all the binaries for that stuff, and all you do is flip this config flag on.
It'll do everything for you.
I think the reality is somewhere in between, where we… we have a toolkit of the parts, you know, we'll say, here's the exporters, you don't have to write them, here's the thing that'll build the dictionary tables for you, so you don't have to write that.
But you do still need to handwire the bit that will somehow… provide a stream of JFR events to this thing we've given you.
**Trask Stalnaker** 20:04 What, profiling, could exist in the core repo outside of this module?
Is it anything, or is it exclusively…
**Jonathan Halliday (IBM)** 20:15 No, I think it's all in there. There's some utility code, because the way that… attributes are handled a little bit different. Almost all the code for handling attributes assumes you've got set semantics, key value map.
But because we're using dictionaries, it's actually possible to break that in profile, so I had to… to write some new stuff, and I think some of that went into the attributes module instead, but anything that's profiling-specific is basically in the exporters at the moment.
**Trask Stalnaker** 20:48 So, maybe a question to John, from Azar.
Core Maintainer Representative.
Would you… do you see anything living in the core repo?
Outside of the… OTLP exporter.
So the other, there's this piece, there's this kind of intermediary piece, utilities, that… would… Help to build the export?
the OTLP… data… But that's not spec'd.
Could that live… In the profile… profiling exporter itself?
Or…
**Jonathan Halliday (IBM)** 21:47 That's currently my intent. There's an open PR that's got the Dictionary Builder, for example.
Yeah, I looked at that, I looked at that PR. That's just going into the profile for now, we can move it later.
**John Watson** 21:58 Yeah, yeah. So, I think it's fine to put that kind of helper stuff in some internal packages.
I don't… I think it would be a while before we'd want to declare that stuff stable and.
**Jonathan Halliday (IBM)** 22:14 Yeah, absolutely.
**John Watson** 22:15 Look API.
I don't have a problem… this stuff seems reasonable, though. It seems reasonable to have this stuff in internal package, because it's going to be probably generally useful, especially if you need to implement async, and you need to… async profiler, and you need… we need to implement JFR.
**Jonathan Halliday (IBM)** 22:32 Yeah, the JFR bit gets hairy because, the JFR consumer API didn't get backboarded to 8.
Yeah, well, I mean, I think… We're gonna probably have to declare that you gotta be… I think… I think I am 100%, 100% happy saying we are not supporting profiling for Javaid.
**John Watson** 22:51 like… If you want profile… if you want the profiling signal, you gotta… you gotta get yourself…
**Jonathan Halliday (IBM)** 22:56 The problem is, if I put 9 code into exporters, currently the build breaks, because although it's building using 17, something somewhere in Gradle.
Thinks the language level is 8, and goes…
**John Watson** 23:08 Yeah, that… we can… we can… That's fixable. Yeah, we can… we can fix that.
**Jonathan Halliday (IBM)** 23:12 Yeah, okay. So then, yeah, as far as I'm concerned, everything can just live in the exporter for now.
**John Watson** 23:17 I mean, I would say that I would be happy saying you have to be… has it been backported to Java 11?
**Jonathan Halliday (IBM)** 23:23 Yes.
It went into 9, it was mainstream from now onwards.
**John Watson** 23:28 Yeah, I didn't remember exactly when that ended up going in. Yeah, I mean, I think, A, we do not need to support Java 8 for this. I will… I will just… I'll put… I'll put my foot down and say, no, we don't need to support Java 8 for this. It's brand new… brand new stuff, like, you gotta get on something at least quasi-modern.
something that's actual LTS at the moment to be on… to get a profiling signal. And I think putting this kind of helper stuff in what… in our code, initially in internal packages, or if we want to think this as a real public API, they don't have to be internal.
But we wouldn't want to declare this stable until… A couple of.
**Jonathan Halliday (IBM)** 24:08 Great, so I think that covers the exporting. The other major area I just want to touch on is signal correlation.
So there's, there's talk about how do we get information that is either process level, or thread level.
Down to the… the profiler.
So, with eBPF, for example, your communication is basically limited to… Ebpf maps.
So it would be nice if some of the… you know, identifiers for a workload, say, could be exposed to eBPF, so that when eBPF is profiling a system-wide, it's looking into multiple containers, multiple pods.
It would be nice if it had some metadata so that it could attach that metadata to the profiles.
So that a receiver knew what was being profiled.
And then at the thread level, if you've got trace context.
And you take a stack trace of the thread.
You kind of want to be able to attach the, the trace ID as well, so that you can do things like, oh, this trace showed this taking longer than usual, let me look at the stack traces that were captured to see if there's any hints there in what was taking the time.
And that's going to be more invasive, in that it's not going to be just limited to the, you know, the profiling exporter module anymore, it's going to have to touch on the The stuff that does… Tracing as well.
So I don't know what that's going to look like in terms of the APIs we use for that, and the mechanisms we use, but that's… We can pump that down the line a bit, and we haven't got a spec or any real idea of how to do that yet. We're just kicking around ideas, so it's just a… To raise the issue to be aware at this stage.
**Jason Plumb** 26:10 But, Jonathan, the protobufs, do have provisions for trace context, at least.
**Jonathan Halliday (IBM)** 26:15 Yeah, yeah, on the wire, yes, yeah.
**Jason Plumb** 26:16 Yeah, okay, good.
**Jonathan Halliday (IBM)** 26:18 Okay, good. But it's a question of how to get that information to the profiler, because as a profiler, for example.
**Jason Plumb** 26:24 Yeah. He doesn't see it, right? Yeah, totally.
**Jonathan Halliday (IBM)** 26:27 Async Profiler does have an API for you to be able to pass information down to it, but it's async Profiler-specific. So you would have to have something like the… the trace context object would have to be async profiler-aware in some way.
So that whenever you updated the trace context on a thread, it automatically passed that information down to async profiler.
And likewise, there's ways to do custom JFR events.
But that means the, the tracing code, which currently knows Stuff all about profiling would have to magically become profile-aware in some way.
**John Watson** 27:03 Could we do it in the con… could we do it, though, in our context implementation, or in a context, like, an extension to.
**Jonathan Halliday (IBM)** 27:09 Yeah, quite possibly. It might be that there's already extension points we can leverage, so we can… You know, swap in a profiler-aware context object that has this bolt-on functionality.
Cool.
**John Watson** 27:22 That would probably be better than trying to put it into tracing or into metrics or anything.
**Jonathan Halliday (IBM)** 27:26 Yes, yeah, I agree.
**John Watson** 27:28 Put it into the context itself, or put it.
**Jonathan Halliday (IBM)** 27:29 physics.
**John Watson** 27:30 reading.
**Jonathan Halliday (IBM)** 27:30 If there's extension points there we can use, then great. If there aren't…
**John Watson** 27:35 Well, if not, we need to invent them. We might need to invent them.
**Jonathan Halliday (IBM)** 27:38 Yeah.
**Trask Stalnaker** 27:40 There is a context storage hook that is… A couple people I know have used for… specifically for correlating to profiling.
**John Watson** 27:52 Yeah, maybe a couple.
**Jason Plumb** 27:52 Customer.
**John Watson** 27:53 Custom storage, custom storage implementation that would do this work?
**Jason Plumb** 27:57 Yeah. That's what we do.
**Jonathan Halliday (IBM)** 27:59 Okay, so it feels like, for now, I'll keep doing what I'm doing, I'll put utility code just straight into the exporters, We'll try to get to the point where we've got something we can offer users that will Accept.
a stream of JFR events, and… export them. That seems like a good first milestone.
And then we'll… we'll revisit what extra functionality we might want to offer on top of that.
**Trask Stalnaker** 28:26 Nice.
**Jonathan Halliday (IBM)** 28:28 Great, thanks for the time.
**Trask Stalnaker** 28:31 Thank you.
Next topic… So this is a, in contrib, where we have the rule-based sampler, which is… Gaining popularity as we have declarative… as we roll out declarative config, since it solves the health check problem and other problems.
This is… A much more powerful.
Sampler, that allows you to use… Common expression language.
To… Define your conditions for, for sampling.
We had… There are a couple reasons I wanted to bring this… Here… Let's… Let's see… Yes, one was… so we had discussed this a while back.
This was another sort of, not sampling, but it was proposing to, Be able to use… An expression language, which was basically… Java, Jexal, you could do anything you can do in Java.
And this got… blocked by, security concerns, like, at least living direct… living in the Java agent distro. I think people were fine with it being an opt-in feature.
that lived in Contrib that people had to opt in to bringing in. The concern was that if this was always present in the Java agent, it's now a… Another source, a source of, External execution that we have to worry about.
So this is a much smaller surface area of things that can be, executed?
And so… Yeah.
So, I don't know if folks… probably haven't seen it, but wanted to draw attention. So, the reason we are now pulling this module in, the rule-based sampler, we're pulling into the core Java agent distribution now.
Again, because we have the declarative config support now, and that's super useful, and… So this is currently landing in the same module.
So this would be available by default.
Another, I mean, the CEL seemed nice, at least it's a standard, and it doesn't allow arbitrary… Expressions, Java… There's also… we've just… I mean, OTTL is what's used at the collector level.
For defining samplers, span processors, etc.
It would… I mean, this is true, that… Applying… At both the language level and collector The same kind of samplers, processors, would be… nice.
Ottl is something…
**Jason Plumb** 32:45 We would do a Java implementation of OTTL.
**Trask Stalnaker** 32:49 We would.
**Jason Plumb** 32:50 Yeah.
**Trask Stalnaker** 32:51 And I don't know how well it's spec'd.
**Jason Plumb** 32:59 I thought it was pretty good.
**John Watson** 33:05 Yeah, or is there a TCK for it? That would be nice.
**Lauri Tulmin** 33:09 Isn't the OTTL built for something completely different?
Is it the suitable language for this at all?
**Jason Plumb** 33:23 Yeah, because it kind of only knows about or only targets OpenTelemetry concepts, and it doesn't target, like, arbitrary Java classes and methods, right?
To Lori's point.
Whereas both Injectsel and this CEO, I think you can kind of do arbitrary… Or more arbitrary.
**Trask Stalnaker** 33:49 We're not… Do we want arbitrary… And… Aren't most of these things based on I mean, attribute starts with… I mean.
**Jason Plumb** 34:01 Yeah, the business…
**Trask Stalnaker** 34:02 be written in OTTL.
**Jason Plumb** 34:04 Yeah, it depends on the use case. So, for sampling, I think it's fine to stick with something that's, like, domain-specific.
But in the case of no-code, that domain is different, right? Where you're… where you're wanting to declaratively specify instrumentation points, which are typically… Cut points, you know.
class method.
**Lauri Tulmin** 34:26 It really depends on what you want, like… If you only need, like, that you want to have expressions like string starts with.
Or you want to take a method parameter and invoke another method on it.
**Trask Stalnaker** 34:42 But samplers don't have access to arbitrary Java objects anyways.
They only have access to… our… Yeah, specifically.
**Lauri Tulmin** 34:55 I think even with checks, it's probably possible to limit what it can do, like… After all, it has its roots in the JSP expression language.
**Jason Plumb** 35:18 Yeah, I'm starting to just think it's a different use… like, different use cases here.
**Trask Stalnaker** 35:24 For no code.
**Jason Plumb** 35:26 Yeah.
**Trask Stalnaker** 35:27 Certainly, yeah, I agree with this for no-code, it's… like, CEO… Something like this, or Jexal.
**Lauri Tulmin** 35:39 Like, the checks list is probably, like, the syntax should be more familiar for Java folks.
Because it should resemble more the expression languages that they have used before.
Well, the common expression language is probably… I don't know.
It's definitely not Java-based.
**John Watson** 36:00 Yeah, it's one of those things where… who is the audience? Is it Java developers, or is it operators who are also going to know how to, like, understand the collector and how to use it? Because if it's operators who aren't really Java people, it probably makes sense more to have something that works with OTTL, so it's something familiar.
If it's Java developers, obviously having something more Java-friendly would be… Preferable. Or maybe we need both.
**Trask Stalnaker** 36:28 idea… like, the dream would be something that we could have across languages for, at least for, say, samplers, span processors. Let's… let's ignore the no-code For now.
**Lauri Tulmin** 36:43 Then, most likely, the common expression language is a winner, because I think it has implementations in multiple languages.
**Jason Plumb** 36:51 But then also, yeah, I mean, OTTL would also, but it doesn't have implementations yet.
**Lauri Tulmin** 36:56 But the question is, like, is OTTL suitable for this at all? I think that's the first question we should look at.
**Jason Plumb** 37:03 It's a good question.
**Lauri Tulmin** 37:04 Maybe a language that's built for a specific task inside the collector.
That might not apply to this problem that we are trying to solve.
**Trask Stalnaker** 37:14 sampler, but I mean, isn't it… It's the same way behind.
To, yeah, to define samplers in the collector, samplers and processors inside the collector.
**Jason Plumb** 37:28 And to be able to slice and dice, like, pick out specific parts of a span and do stuff with an attribute, or… Map it over, copy it, filter it.
I think it… I think it's the same stuff, but…
**Trask Stalnaker** 37:48 Yeah, John, to your point, I would love if there was a TCK like, you could just send… I mean, I would have a lot more confidence in… Because it could probably send Copilot to build something like that, but I wouldn't have a lot of faith in what it produced.
Without a…
**John Watson** 38:09 Could we have Copilot build a TCK for us?
**Jason Plumb** 38:19 It can do anything you ask it to do, and it will do it happily.
**Trask Stalnaker** 38:22 It can… it can try, it can… yeah.
**Jason Plumb** 38:24 It'll do it happily.
**John Watson** 38:25 It'll do it happily, and…
**Jason Plumb** 38:27 And confidently. Yeah, very confidently.
**Trask Stalnaker** 38:29 Yeah, very confidently, yes, yes.
Okay.
So it sounds to me like, Potentially, we should split the, like, if, Dominic wants to continue pursuing this. We should probably split it out of the existing sampler module so that it doesn't get pulled into the Java agent by default for now.
**Jason Plumb** 39:04 Concerned about that?
**Peter Findeisen** 39:07 So…
**Trask Stalnaker** 39:08 Yeah, go ahead.
**Peter Findeisen** 39:09 I believe we had a policy that we do not put into the Java agent anything that doesn't have approved specification.
**Lauri Tulmin** 39:21 No, that's a policy for the core module.
**Peter Findeisen** 39:24 Nope, not true.
Okay.
**John Watson** 39:27 Yeah, that's just a quote.
**Trask Stalnaker** 39:27 Okay.
**John Watson** 39:28 That's just the core repo, yeah.
API and SDK need to be spec'd, but…
**Peter Findeisen** 39:35 I see.
**John Watson** 39:37 Naughty, naughty stuff.
**Jason Plumb** 39:39 Trask, I would like this pull request to land, but it sounds like you're hesitant.
**Trask Stalnaker** 39:45 Do you want it to land and be included in the Java agent distro?
**Jason Plumb** 39:49 Well, those are two separate things, but I mean, I understand that that module would… so are you suggesting, then, maybe move this over to a new module?
In contrib? Yeah. Okay.
That's cool.
And your concern… your concern about it being in the… in the agent is that somebody could wire this up and do something nefarious with it, using that language?
**Trask Stalnaker** 40:18 Not so much as just, I'd like, like, if we are… I'd like us to decide if… the… in the Java agent.
our… I don't want to have a lot of different solutions.
**Jason Plumb** 40:32 Yeah, it's okay.
**Trask Stalnaker** 40:33 are going to pursue the OTTL, I don't want to have to support both.
**Jason Plumb** 40:40 Okay.
Yeah, I'm all about then putting in a different module. I mean, they may not like that answer. They've been pretty patient, but… It's probably not that much work.
**John Watson** 40:53 Yeah, I would say the other advantage of having it as a separate module is that if there's somebody who's extra paranoid about having CEO in their.
**Jason Plumb** 41:02 Yeah.
**John Watson** 41:02 They can… they cannot have CEL in their distribution.
**Jason Plumb** 41:06 Yeah, I mean, that's bound to be a kind of a twitchy dependency anyway.
**John Watson** 41:11 Yeah.
**Lauri Tulmin** 41:12 But what would be, like, the… The eventual plan somehow merged this with the rule-based sampler.
**Trask Stalnaker** 41:23 merge the… I mean, I… I would love to see… personally, I would love to see OTTL, just, from… for people who don't have a collector to be able to do cool collector-like stuff in the Java agent via declarative config.
Both processors and samplers.
And if we did that, I could see it being merged, potentially, with the rule… with the rule-based sampler, since… It's pretty… Basic.
But I'm not sure. I haven't gotten that far in my dreaming.
Cool, I think we have a plan there, at least short-term. Let's move on… Jay.
**Jay DeLuca** 42:31 Yeah, so I'll be super quick. But yeah, I just wanted to call out that the, the automation is helping us slim down the backlog a bit, so hopefully we'll get to a point where we can have clearer… vision into the priorities and things like that. I think if… just to call out, if you've seen PRs or issues closed that you think shouldn't be closed, feel free to reopen them or comment on them. We're definitely trying to reduce noise, but we don't want to flush out, like, legit things. And then, as I was kind of working through some things, the next item is, do we want to create a project for 3.0. I noticed that there was one for 2.0. I think we have a milestone, but… And maybe this is still too early to even talk about, but I just came across it, so I wanted to raise that.
**Trask Stalnaker** 43:21 I think we should, yeah. Yeah.
I like… I've been getting more… acclimated to projects. I didn't like the projects for a long time, but I guess having to use… using them more… a lot in SEMConv.
Gotten used to it.
**Jay DeLuca** 43:43 Cool. And then I put a couple issues for us to go through if we have time, but we can…
**Trask Stalnaker** 43:48 Circle back to that.
Cool.
**Jason Plumb** 43:52 I didn't bring this up earlier, when we were talking about extended stuff and extended logger, especially in the context of, like, doing profiling, but… We use this in Android, we also have people internally here that are using this, and I'm wondering when we expect this to come out of incubator, and it sounded like the answer I heard earlier was when events are marked stable. Is that true?
**Trask Stalnaker** 44:17 It should be more when… you just want the is enabled flag, or you want…
**Jason Plumb** 44:23 I don't wanna… I don't wanna have to… I don't wanna have to jump through the extended logger casting stuff.
**Trask Stalnaker** 44:31 to init… complex app, sorry.
**Jason Plumb** 44:35 To emit… sorry, just to emit events. Like, to set event name?
That's on extended logger.
Yeah.
**Trask Stalnaker** 44:44 Don't we move event name… Event name is stable now, so we…
**Jason Plumb** 44:51 Oh, maybe we don't need that anymore, then.
Okay.
**Trask Stalnaker** 44:57 I thought… I thought I… let's see…
**Jason Plumb** 44:59 Let me check.
That will be a little bit of good news.
**Trask Stalnaker** 45:06 Yes, I think that… That's already in… Log record builder.
**Jason Plumb** 45:12 It is, okay, great. Okay, that's all I care about, selfishly. Other people might care about extended attributes, I'm sure we will at some point, but right now, that's all I care about, so…
**Trask Stalnaker** 45:21 Yep. Sweet.
**Jason Plumb** 45:24 I need to make a clarification statement to Nikita, then.
Cool, thanks.
**Trask Stalnaker** 45:30 Hey, say hi to Nikita for us.
**Jason Plumb** 45:33 I will.
**Trask Stalnaker** 45:35 Nikita was a, instrumentation maintainer, like, many… Ages ago.
Alright, yeah, yeah, let's… let's do 10 minutes of… Issue triage.
**Jay DeLuca** 45:54 And this one might be a can of worms, but… Just curious if we have consensus on… What we want to do about something like this, and if it makes sense to start incorporating some of it into declarative configuration or anything.
**Trask Stalnaker** 46:13 Yeah, didn't we have another discussion going on an issue about this?
development, I asked… Gregor, what the declarative config was, and he said it was… Instrumentation slash development. Let's find that.
Come on… Really?
Instrumentation slash develop out notes.
Maybe it was not in this repo.
Nope.
I have no idea what I'm thinking of.
But yeah, Sue… in configuration… Look at kitchen sink… So, everything under Instrumentation Development This is how we do it in… declarative config.
That's sad.
General strategy, anything slash development?
Yeah, looks like…
**Jay DeLuca** 48:04 Yeah.
**Trask Stalnaker** 48:07 Okay, so it's not really… I think instrumentation… Is under development… is development currently because they haven't declared this node stable.
But then anything we want, we just append So, I, I would say… Yeah, I would say maybe we don't need to deal with the properties?
And just… Config properties, and just… Apply this going forward, solve this going forwards in declarative config.
**Jay DeLuca** 49:08 Well, so we won't make, any effort to go back and… Change any of the existing ones.
**Trask Stalnaker** 49:18 We could, if we find that it's… if there's some alignment with… Declarative config.
But if there's not… I think it's probably okay to… Yeah.
I guess it depends on what's… If we find alignment.
Okay. Helps.
Alright.
Micrometer Bridge… Yeah… So, I think we could go ahead with this… This change, at least.
For the micrometer bridge, do we have a public API surface that we need to… Review.
Because to Lori's, let's see… Documentation… Yeah, I mean, we want to do it, I mean, we would support doing it, but somebody needs to kind of go through the… Oh, oh, we should… okay. Maybe it needs triage and… Contribution, welcome.
Yeah… Did I… let's see… I should have labeled this one… Oh, maybe we'll put this one on the… On our declarative config… Project.
Oh, dear.
**Jay DeLuca** 52:23 Yeah, wasn't sure if this is something that we… we do want to do, or… I don't know too much about it, to be honest.
**Lauri Tulmin** 52:35 Oh, I figured.
**Trask Stalnaker** 52:36 Lord, dear.
**Lauri Tulmin** 52:37 Pretty nice.
But it's… it's not as easy as… As one might expect.
**Trask Stalnaker** 52:49 Would we accept the… contribution, if somebody…
**Lauri Tulmin** 52:55 Well, I think we should, like, the idea is, like, crude, I think.
The Duke.
You could use the regular Put the white body plugin to run our muzzle.
Generation.
But I think the problem is that, for resource location.
ByteBuddy provides a class file locator.
But our muscle stuff really wants to loot classes.
So there is a bit of a mismatch there.
Cool. So making it work might require working with a byte by the author.
**Trask Stalnaker** 53:55 And… request for… VAPT report.
Vulnerability Assessment and Penetration testing.
So I think the collector… Pass… something…
**Jay DeLuca** 54:17 Yeah, I think you linked to it in a comment below.
**Trask Stalnaker** 54:21 Thanks.
So, I mean, the problem is this requires hiring, like, people to do this, which is what the CNCF did for… this effort… So, I… Don't really know how… We would… address it… Why don't I… Said security… I'll also throw it on the next… Security SIG meeting, which is…
**John Watson** 56:23 Doesn't look like there's a lot of attendees to that.
Riley's on vacation.
**Trask Stalnaker** 56:31 So usually there's 3.
Sadly, though, they're all from Microsoft, so if y'all want the security SIG to not be a Microsoft shop, you should send your security-interested folks.
our way.
All right.
Just in time.
Thanks, all.
**John Watson** 57:06 Thanks for running things, stress.
**Jay DeLuca** 57:07 Later.
**Trask Stalnaker** 57:10 I…
**John Watson** 57:11 See some of you in an hour or so.
