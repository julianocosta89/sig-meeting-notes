SIG: eBPF instrumentation
Date: 2026-07-15
Duration: 53 minutes
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 02:18 Hi, everyone.
**Rafael Roquetto** 02:21 Hi there.
**nimrodavni** 02:22 Hello.
**Roy Reshef** 02:32 Hello.
**Tyler** 03:13 Hey, how y'all doing?
**nimrodavni** 03:15 Hello.
**Giuseppe Ognibene | Coralogix** 03:17 I love it.
**Tyler** 03:19 Hey.
Sorry, going a little slow getting set up here. We'll probably get started in a second. If you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about, go ahead and add them there as well.
Almost, almost set up over here, and then we can jump into the meeting.
Hmm.
Well, we'll see how this goes. Peters.
Running at 100% here. But anyways… Hopefully this all works.
Welcome, everyone. Yeah, good to see you all. Let's, let's jump in here.
I can start sharing my screen.
Maybe?
There we go.
Cool. All right.
Dyson, you can all see my, the meeting notes, right?
**nimrodavni** 04:58 No.
**Tyler** 04:59 Okay, perfect.
Awesome, okay, start us off, Nicholas, you wanted to point out that, Mattia, the patch you made to the kernel, looks like it got accepted I don't know if there's a lot of things going on. Sorry, I'm starting to see the grid. That' Yeah, definitely. Congratulations, Mattia. Thanks for all the help on that one. Definitely, important and helpful in getting us to change things upstream. Also, now you're, like, the go-to point person for, getting all Linux bugs fixed.
**Mattia Meleleo** 05:35 Wouldn't have done it without the powers of cloud.
So, thanks to Anthropic for…
**Tyler** 05:41 For that.
**nimrodavni** 05:43 True, true.
**Rafael Roquetto** 05:43 yours.
**nimrodavni** 05:44 That's a Grammy speech, like, thank you, Anthropic.
Yes.
**Tyler** 05:53 Yeah, no, that's definitely good.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:55 Helped me achieve this. Yeah.
I mean, it's good, like, other people helped, like, obviously, Steven and Mario were working on identifying exactly the commit and all these things, right, and created a small repro and whatever, but at the end of the day, you made a kernel patch, man, and… Provided a workaround, which is epic. Yeah.
**Tyler** 06:22 Yeah, really great. Super exciting. Awesome.
Okay, next, moving on to the, on the agenda. Roy, you wanted to talk about allowing dynamic, attach to optional Java agents on, the JVM runtime?
Thought I saw Roy on here.
**Nikola Grcevski @ Grafana / OpenTelemetry** 06:44 Yeah, you're on m.
**Roy Reshef** 06:45 Yeah. Sorry. I started talking, while being on mute. Apologies. Yeah. That's something that came up, during the discussions that I had with a few of my colleagues. And then I had, a short discussion with, Nicola on, on slack on, I believe it was Friday.
So what we have now, we have a dynamic attach of the OBI Java agent.
And there are a few use cases, and the most compelling one that we are facing with a large organization is We are working there with a platform team or observability team.
And they pretty much want to… they told us, can you help us get JVM metrics for each JVM, applications that is running in our clusters.
A JVM workload.
And… The current approaches that there are, and there are different approaches, I touch a bit about the other approaches to do it in the alternatives.
is to do a Java agent upon launch.
Either you go and you change every container image that you have, which is very labor intensive and makes you dependent on your app teams to actually do the work.
Or there are approaches by all kind of APM vendors or observability vendors to do that using an admission controller.
that adds a Java agent into an empty Dir using init container, and then changes some environment variable of the main container to load it as a Java agent.
But then again, you are dependent on the app team because admission controller, the way they work, they typically select workloads by labels.
And the way you see it with, large organizations is that The platform team or observability team, more often than not, they don't own the labels.
I mean, the labels, again, they are dependent on app teams to do these changes.
And then, I was thinking, hey, maybe… I mean, that's actually, something that Nicola came… maybe we can use Dynamic Attach, and as we already do Dynamic Attach.
To Java agents.
Maybe we can add beyond the OBI Java agent. And the first two I was thinking are either the hotel Java agent.
which, Nicola, made the point that it has some issues with dynamic attach, not all instrumentation works are, or even the good old JMX exporter that supports dynamic attach.
And if we can do that, and I already have in mind more or less on how to do that.
We can also achieve quite a bit of the JVM goals that I believe it's an issue that You, Tyler, opened, and I referred to it, It's called Provide Runtime Metrics with OBI. We can get it almost for free, basically.
Again, not to expose these metrics using eBPF, but To use the language detection or the runtime detection.
and the mechanism of dynamic attach of Java agent, a… to get there.
So that's basically what's behind this idea.
And yeah, Nicola raised the issue of a what if there are vulnerabilities and so on, because I was also taking it a step beyond and thinking of letting you a attach arbitrary Java agents. It's a Wheel of, you know, the cluster owner.
That may be taking it too far.
But I think that at least with those two, with an OTEL Java agent, and with JMX Exporter, we… We can go a long way.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:01 Yeah, I have kind of a few thoughts about this.
So, we do have runtime metrics for JVM now. The OTEL ones, I don't know, maybe they're not sufficient to what we have. I know the original author… wanted extra metrics that are not in the hotel spec.
But now OB does support JVM metrics.
As… I don't think it's in 10 version, but… I mean, I think it didn't make the cut.
I think so.
But this actually poses another kind of interesting question, is that I think what you really need is OB's ability to detect the language, discover the process.
inject, and all these things, right? You don't necessarily may need to even use OB for anything for your purpose, right here?
I mean, you don't need it to instrument with eBPF. You just wanted to discover the process, detect that it's Java, and then able to inject an agent.
Right? Of… Anything you like.
Which is why I thought that maybe I mean this come up like so we had a previous discussion about the survey info, which again, nothing to do with eBPF instrumentation, but the ability to discover a process, detect its language, and all these things are kind of useful to other projects than just our project.
so I… I was thinking, does it make sense for us… a lot… some of these packages that we have are internal, right? We currently don't expose them as external packages. Does it make sense for us to refactor the code in a way that other people can build useful things on top of OB?
Or… I don't know, split these things into reusable components.
That could… other stuff could be built, so you can easily build Like, Damon said that.
Has all these capabilities built in.
That you can give to your customers. Is that an option?
I mean, I understand this is really powerful.
And, I mean, this is why we did it in a way that doesn't require restart, doesn't require injecting control, containers, and works on outside of Kubernetes too, right? It doesn't actually depend on Kubernetes, like, you can inject on any process running on a VM, right?
It's just, I don' If adding… So this Prometheus JMX exporter will likely not be in OTEL spec, and that sort of… raises a question, should it be… does it belong to this project, or… I think your initial proposal was, yeah, let me load any agent.
and I'll choose what to add.
But I'm worried about that from somebody doing something malicious with Adobe, loading something random.
in a process.
and nobody knows right.
**Tyler** 14:05 Well, this also kind of sounds like a like an injector.
Right? Yeah. Like the OpenTelemetry injector Isn't that what they do?
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:15 Yeah, the OpenTelemetry injector, unfortunately, this.
I only… injects the OTEL… Java agent.
**Tyler** 14:31 Right, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:31 They are.
Actually, yeah, actually, yeah, you can use the injector. Maybe. I have to check. I think you can specify the full path, and if you give it another jar, it will load that instead.
So maybe… but that one requires a restart, it does not do dynamic attach.
So it requires that you.
**Tyler** 14:52 Oh, really? Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 14:53 Yeah, it requires that you build What, Roy was saying, you, you build, In its container image that you add to your, you know, some… I don't know, operator controller in Kubernetes that just has a mission webhook, and And on any new pods created, it injects this. Which, you don't need an injector for that. If you know your target services are Java, you can just add something that sets up an environment variable and be done with it. It could just be a busy box with an Something environment said.
I think what Rory likes is our ability to dynamic attach. You just drop this daemon set in the system, discovers the Java process.
Automatically does everything, injects the agent.
Yeah, okay.
**Roy Reshef** 15:40 Yeah, I was looking at the Java injector code, in Obi, and I mean… I don't think it will be rocket science to extend it, to have the capability, because currently it has some hard-coded cons of the jar name and the main agent class name to look for, to know if it's loaded already, yes or no.
And things like this, I mean… Can make it more generic, and… and have the capability to a You know.
to dynamic attach of arbitrary Java agents. Not arbitrary, but, I mean, you will need to, of course, provide them And.
I don't think that's, I mean, too complex to do, in that sense.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:32 So I guess my question is that if we Provided our code in a way that you could build your own, like, small goal, based… payment set that you could deploy yourself, would that be an option? That you can just reuse the OB pipeline for discovery, detection of languages, get events, and then you can use our ability to inject Will you build your own tool, I'm asking, or do you need a tool like OB to be readily available? Would you consider writing on your own?
**Roy Reshef** 17:05 I… I can go down this route, yeah, it's a… it's not too complex. I mean, I was also hoping a bit to avoid having to… I mean, I don't think this should be a… Yeah, if this is something that kind of wraps OB or runs on top of OB, I think that should be fine. I don't want it to be a fork, because then it becomes a bit of a maintenance nightmare to do it, because OB gets updated quite frequently, as we all know. So, but something along these lines, yeah, I think… Yeah, that should be… I think, by the way, it can be… Also, very valuable to… A lot of vendors, I mean, and again, I'm not.
Very familiar with the way that Grafana does it with Java agents.
But, myself and my colleague, we've been taking a look at some of the competitors. I'll just mention them by names. I mean, New Relic, Datadog, Dynatrace, almost all of them go down the route of, admission, an admission controller.
But again, admission controller, when you come to large organizations, and we have a couple of customers like this, it becomes a bit of an organizational challenge.
Yeah. Because admission controller depends on the app team to… to play nice.
And other again.
That may become an issue with certain organizations. Whereas Dynamic Attach, I don't need anyone to play nice.
I mean, I can let… of course, based on configuration and the like, But, You can enforce it on a, let's say, cluster-wide, even, scope.
Without depending on… you only depend on language detection. That's all you depend on.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:05 Yep.
Yeah, I think I understand. This goes really well with what Mike has been working on, right? So…
**Mike Dame** 19:10 I was just gonna say, yeah, I mean, what Nicola was saying, that's, like, building a wrapper or something that instead of having a fork, Obi, that's the whole point Yeah, Gobi is a good off the shelf tool, but also trying to build a platform out of it that like this, what you're talking about sounds like something that we would honestly probably like to use too. So I'd be happy to help and try to build that sort of API out a little bit more into so that right now it's just like selection and some resource attributes, but actually controlling the instrumentation and what, agent is attaching to it. I think that would fit perfectly and, extend, make Opie more extensible.
**Nikola Grcevski @ Grafana / OpenTelemetry** 19:48 Yeah, I think the first step is to make these packages public so they can be reused externally. Right now, some of those are private. I mean, look at what Nimrod did for Node.js in this latest pull request.
This doesn't actually stop at Java. We have similar capability for injecting an agent into Node.js. We detect when we can do it, we send the signal, we load an agent, so you can invariably see in the future somebody wants to build a tool on top of a detect node applications and then send an agent dynamically in an environment Profile something, instrument something.
Close it off when it's done, I think, this… it's proving that, and the whole mention of the survey mode, it's just another reuse of the pipeline, right?
So.
**Roy Reshef** 20:34 Bye.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:35 Yeah, let's refactor the code in a way that it's reusable and composable from Outsiders, other than… eBPF instrumentation, right? There's obviously useful stuff in there that we've built.
That's my take on it Yeah, PR is welcome.
**Roy Reshef** 21:01 Yeah, I can take a crack at it, I can touch.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:04 Be willing to take, build your own… just make OB a dependency and see what it takes to… is it possible to extract the pipeline. I mean, you can look at the Bela code. We actually use the OV pipeline and add process metrics to it. So it should be something like that.
But I think the injector stuff will need to be moved.
Some packages are private.
Yeah, they're in the internal.
So they need to be properly placed into our.
source.
Yeah, if you look at the Baylor source, we have an example essentially of how to Take the OB pipeline and work with it.
Yeah, sure.
**Tyler** 21:46 Okay, yeah, sounds good. All right, well, we'll iterate on that. Sounds like, Roy, you're gonna take a stab at it.
Roy, I think you also have the next, item?
**Roy Reshef** 21:59 Yeah, another one, which is somewhat related.
I was looking at, other… JVM dwellers, other, language running… languages, sorry, running on the JVM and how they are, detected.
And currently, we detect them all as Java.
Because we… We only look at, at the LibJVM SO, or we look at some symbols, but that's the only detection that we do.
So, if you're running, scala, Kotlin, Groovy, Clojure, and the like.
Then, they are all identified as Java. Now, where are the JVM is still there? As a runtime, the language is not Java.
And… this is just a proposal of how to try to fine-tune it and give a more… maybe more valuable… Again, I do not know what things you will want to do different with Scala, for example?
I'm not such an expert on these languages, but I think it may be valuable.
So.
**Tyler** 23:14 Yeah, I think that's my question. It's like, if we do these detections, what happens next?
Do we not… do we not attach it as a Java instrumentation at that point, is what you're saying? And just use, like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:27 No, I do, I just… I guess it's more correct. From a user's endpoint, I know that's a SCAL application, and like, from an OTEL standpoint, I don't.
**Tyler** 23:40 So that I mean, that's that's my question is like.
How does this refined detection get percolated to, like, where does it get seen?
How does it get seen?
**nimrodavni** 23:51 Even if we want to add it under the telemetry SDK language tag, I think the only one from there that is Part of the SEMCOV is Kotl So if we do want to differentiate between them, we need to also probably push… either declare it as something of our own, or… like, I don't know if, I don't think even a Scala, like, Otel of Dec Right? Like, because the Scala Auto SDK just uses Java, I think, and then it won't tell the difference.
It might, it might be useful for, I don't know, it might be useful, but, but even if the AutoAuthDK doesn't support it, then maybe… We need to consider what it gives us.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:34 Yeah, we'll have to come up with our own field.
Telemetry has to go sub-language or something.
**nimrodavni** 24:41 Oh yeah.
**Roy Reshef** 24:41 Or maybe we should distinguish between runtime and language.
Runtime is JVM for all of them. Yeah, no argument about that, but the language is different.
I mean, there are some… I also mentioned caveats, you can have a mixed, A mixed case, when you try to do this detection.
For example, a Java application that is written in Java, but it has some groovy jars for some templating engine. I've seen these examples, too.
a… So… we need to be a bit careful about this, but I just thought it… it may be useful from… Surely from visibility point of view.
**Tyler** 25:25 Well, I mean, I think that that's, like, my question is, like, what is that visibility? And so, like, I agree, I think that'd be great to know, you know, if there's a difference here, but, like.
if we go through, like, all this hard work to do this detection, and then it just falls by the wayside, because, like, we don't actually surface this anywhere, then that's… that's the thing that I'm missing.
So, like, I think we need some sort of… semantic convention or attribute that we're gonna use to surface this, like, and so, yeah, like, this sounds great, just… It's not, like, I need the complete vision of where it's gonna surface, I guess, is the only thing that's.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:02 Does it mean we need a proposal for the SEMCOM to add?
Something to say… Yeah, JVM is technically a platform that you can build other languages to actually have a defined sort of class like languages implemented on top.
**Tyler** 26:23 Yeah, something like that. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:26 That'.
**Tyler** 26:26 I think that… I mean, I… yeah, and I'm fine if we wanted to, like, get something shoehorned in while we're.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:32 Right.
**Tyler** 26:33 But I just, like… Yeah, like, it has to go somewhere, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:40 Yeah, so the television shows again language and television shows decay.
something else.
**Tyler** 26:47 Well, yeah, I mean, it's also, like, you can also talk about just, like, instrumented language and instrumented runtime, Yeah, I mean, these are things that have existed long before.
Hotel.
So yeah, but it's just like that. That sounds good to me. It just needs to get standardized as a part of this issue.
I would not want to, you know, accept all this work to get this parsing done, and then just not do anything with the parsing, I guess, is my concern.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:14 Yeah, right.
So, Roy, would you think you might be able to propose a… Like a spec extension to.
to define sub languages, or whatever they want to call them, or whatever. Pick another word. I don't know what the right word is.
**Roy Reshef** 27:32 I can do that. I need to dive in a bit to see how SENCONs work, because I'm… I have some general knowledge about this, but… Not too much in detail.
But yeah, I can take a crack at this too.
**Nikola Grcevski @ Grafana / OpenTelemetry** 27:46 Okay. Yeah, I… I mean, one interesting example is, like, if you think about it, I mean, I… probably everybody's looking at Maybe not everybody's aware of the whole bun.
being rewritten from Zig to Rust, right, and the whole spat between the Zig community and Anthropic and so on, but if you think about it, that's another instance of this, right? The language itself, it's Zig, it used to be Zig, but the actual thing that's running is JavaScript.
So you might speculate, they say, well, that's kind of similar to what Java is. Java is the base technology, and there's, like, another language on top, like JRuby, right?
So this happens, and now Bun is rewritten in Rust, and so technically the base language is Rust, but what you're running is JavaScript, so… There is a… need for this.
And it's not specific just to the JVM, so it would be nice to… If we can detect it.
**Tyler** 28:51 Yeah, agreed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:52 Yep.
**Tyler** 28:54 Agreed. Okay, well, cool. All right, Roy, it sounds like you're gonna take a little stab at that one as well. Thanks again for bringing this up We're… Sure Worth addressing.
Okay, next, Nimrod, do you want to talk about manual instrumentation support consensus?
**nimrodavni** 29:11 Yeah, I think Nicola mentioned it a bit. I just have some direction I'm going. Specifically, I'm doing it for Node.js now, but I think it could be Useful in the future for other… Language is gonna put it under the, epic of OTEL API SDK integration, because I think it's really… Nikola Grcevski @ Grafana / OpenTelemetry 29:29 Yep.
**nimrodavni** 29:30 I think we received it as, like, a main complaint from a lot of people, like, that OB doesn't do the, like, your business cases, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:39 Yep.
**nimrodavni** 29:40 So there are, like, a couple ways to do it. One of them is something that, Mattia already had, like, an RFC for, I think I'm putting it down there, that's… it's basically kind of doing, manual instrumentation by declarative config.
from, like, you basically… we do, I think, like, a combination of view probes and USDTs on specific functions in the code, and then you have, like, some… some sort of, like, a way to declare, like, I want to create a custom span on this function at this file. I get their, like, attributes and, like, parameters as labels, which is really cool, but I think a lot of… what people already do is they use the Otel API, to kind of wrap parts of their code and do, like, you know, span.start, span.end.
In their, specific languages and, and APIs, and that's the case. So I wanted Obi to support that, like we do in Go right now.
and I think the only way to do it in each language is kind of dive in a bit into the runtime, because I don't think… for example, in Node.js, you can't… you can't do it with, like, Uprobes or USDTs in most production, like, Node, Versions.
So, I have some PR, I think Nicol already reviewed it a bit, that uses the existing Node.js infrastructure to do it.
And, we might do it, like, in Java and other languages. I just wanted to make sure that this is a correct and, like, agreed-upon direction to go, because it kinda… leaves a bit, like, the eBPF-ness of Obi, but… but it does, like, kind of synergizes with all the eBPF stuff we do. Like, we still… we still… everything, the, like, network stuff and… and all that comes from eBPF, and those specific stuff, we kind of… You know, port towards our traces.
So I just want to get, like, make sure that this is, like, a fine direction from you guys, and then, like, I want to continue, like, we want to continue… Working on this in like different runtimes, different languages, improvements to this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:00 I think it's right.
that's… I have already commented and approved the PR, added a bunch of feedback, right? You addressed it, so… I mean, it's pretty cool. As soon as I saw that, I was like, okay, Java should be next.
**nimrodavni** 32:14 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:15 Yeah, we already have an agent, we can easily add support for manual spans in Java, so we have 3 major languages that we have support for.
Go, Node.js, Java.
It's pretty good.
**Tyler** 32:33 Yeah, I mean, I don' yeah.
Yeah, I don't know why there'd be opposition. Yeah, I definitely.
So, like, you're going about it the same way we go and go, Nimrod, where, like, if someone's using just the API there, we're gonna, like, pick up whatever those fans would be, and then just add them to our traces, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 32:53 Yeah, he has OB as a tracer with…
**nimrodavni** 32:57 There are like caveat, like basically if this only works if you don't have any other like trace provider and we have like fallbacks of like if another trace provider tries to register after Obi, we kind of stand down because we want to be like the least intervening that we can.
But yeah, it's just the same API, I think.
**Tyler** 33:23 Okay.
**for Go, I know we had, like, a lot of issues around, like, interface, introspection, right? Like, I don't know if that's the same in, like, JavaScript. Are you going about it the same way, where we're doing a lot of, Uprobes, or are you going about it… Nikola Grcevski @ Grafana / OpenTelemetry** 33:40 You know, you just serialize it to JSON and…
**nimrodavni** 33:43 Basically, it's part of the JS mini agent that we use for context sharing.
I just added another script that basically registers kind of a dummy tracer.
**Tyler** 33:59 Provider.
**nimrodavni** 33:59 Yeah, that's basically a provider. And every time they do like start span, end span, we serialize it to a mini JSON, write it using some syscall to the same way, OBU parses it.
**Tyler** 34:15 Mmhm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:16 Yeah, okay.
**Tyler** 34:17 So, yeah, I mean, that sounds, that's even easier. It's awesome.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:22 Yep.
**Tyler** 34:23 Can we do this for Python as well, then?
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:26 I have to figure out how, but…
**nimrodavni** 34:28 I think so. I think Python might have better, like, debug APIs. I guess Spark probably knows better about that, but… I need to do some more research there, I guess. You're saying Java probably gonna be easy because we have a Java agent, basically?
**Tyler** 34:45 Yep.
**nimrodavni** 34:46 Python…
**Tyler** 34:47 Very similar.
No.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:49 Does Python have a way that you can just say, hey, load this for me after you've started? I don't know. I have to look it up.
**Tyler** 34:57 started thing, I don't know. I mean, it has to.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:59 Yeah, I.
**Tyler** 34:59 interpreted language. It's got it like, I don't like, but at the same time, I'm like, hmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:05 I think it does.
**Tyler** 35:06 Do you know that So… Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:09 I mean, you can attach a debugger after the fact, so… I think it's… we stand a chance.
**nimrodavni** 35:14 I think some newer versions of like 3.12 or something have this kind of the debugger API.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:21 Yeah, yeah, yeah, that thing, yeah.
And if it's 312 and above, I mean, that's just a matter of time before it becomes every version of Python, right?
A year from now, that's it.
**Tyler** 35:32 You guys aren't still running 2.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:34 Nobody is, yeah.
I mean, OTO supports 3.9 and above, right? You can't instru Yeah, yeah.
**Tyler** 35:41 Oh, okay. Alright.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:42 Yeah, hotel is 39 and above.
For us, you use OB, that's how I know.
Sure.
**Tyler** 35:52 Yeah, I mean, I think that that's This is great. The harder questions are, like, Rust and, like, C++. I think.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:58 But that's.
**Tyler** 35:59 It'd actually be easier.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:00 For those, I think we need Matthias PR, his proposal with USDTs, which is tell people how to do this. And maybe we can even have our own small SDK that interjects USDTs.
**Tyler** 36:12 Yeah, that's kind of what I was… I was wondering if we could do something like that, because we did that for Go, where we essentially have our own SDK sitting in the top global, and maybe we do, yeah, something similar, yeah, but yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:22 Yeah.
**Tyler** 36:23 That'd be.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:24 So for the end users, they don't even have to touch the USDT, they just import and rust the crate and they start doing span star, span end and other covers that just puts enough stuff to.
**Tyler** 36:35 I mean, that'd be the ideal, right? Like if something like that, yeah.
But yeah, yeah, Nimrod, I don't… there's definitely not opposition. I think there.
**nimrodavni** 36:46 Cool. Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:49 Crazy idea, but awesome.
Oh, that's great.
**nimrodavni** 36:53 Basic requirements, required.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:55 Crazy requirements, crazy, yeah.
You know, I like actually have.
Customers… asking us… Which is even wilder, that they're seeing, like, oh no, like, we'd like to… with Claude generate Ebpf programs on the fly and have them generate random data for us that doesn't exist in any instrumentation tool. I'm like, okay.
**nimrodavni** 37:19 use like a DPF tool.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:23 Yeah, BPF tool with some random programs, and they say dynamic instrumentation is not enough.
You you want to capture random stuff in your.
Programs and I don't know how you even do that.
converted to? How do you standardize the output in a way that can be consumed by any database?
I mean, I know, Mike, you're… you guys have something in Odegos that you can just define your custom probes in some sort of way and deploy them, right?
**Mike Dame** 37:54 Yeah, I mean, that's something that.
People definitely were really — they think it's pretty cool to get more custom frameworks out of it. It's limited to, I think, what languages we support right now, Java and Go. And I think we have C++.
But… I don't — I'm not sure I understand what you're saying that people are generating random telemetry. This is like people know like, oh, I want this. What we have is I have this function that I want to instrument or I'm not using a common library. But you're saying that people are just kind of buzzing their observability?
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:32 Think of it this way, right? So you ran your application, it's running in production, right? And so now the problem is like.
Like what Nimrod is doing, what we did for Go, is you're allowing people to add your custom spans. But that's sort of like, if you, like, hindsight is 20-20. Did I add the span in the right place to extract this information?
**Mike Dame** 38:51 Sure.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:52 I already have a production problem. Now, how do I actually go and find the insight? I know about the area where I should be inserting some spans and maybe get some extra data. But I simply have no way of actually doing this now post fact. And maybe I'm wrong. Like, what am I going to add a couple of spans and redeploy my app in the middle of an incident?
So, they're like, well, with Claude, it can write the CVPF, we don't even have to know what they were doing, as long as we can inject these things dynamically into a running application. I mean, I… I think it's pretty cool, as a concept.
**nimrodavni** 39:27 I think that.
Quite what Matthias is doing.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:30 Exactly, yeah.
**nimrodavni** 39:31 Like you're doing very custom, like, you know, if, and even if we have something like, What's, like, the hot config, reload with, like, You know, you can very easily, like, do it without restarting Obi, and, you know, just send a command to it, that's like a… Pretty easy way to do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:52 Yeah, yeah. I mean, who knows? Maybe even with your JavaScript thing, you can potentially say, I just want to add in this line in the JS code a probe and then start generating span start end without having to manually declare it. I don't know.
It will be something along those lines, but we can inject the new script dynamically.
There we go. We're talking about Roy's idea, being able to inject anything and everything.
But I could definitely see it like even for Java, like you just say, Hey, I just want to start spanning this method. And right now our stuff is hard coded for specific classes that we know of. But if you supply your own class name, maybe we can just repeat the method, enter method, exit and capture some parameters for you.
into a span.
I don't know, it's, it's a wild idea I think there's a few customers that have asked for this, I just don't know what they're thinking. We need more, sort of.
Pm. Work on that to figure out. Is this real? Or you guys are just fantasizing.
But it's 1 of the advantages of this dynamic attached dynamic and Ebps seems plausible that you can just throw stuff in and take it out once you're done.
Oh.
**Tyler** 41:12 Yeah, I mean, that's definitely… it kind of sounds like a custom probe, but, like, very, very custom.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:18 Very custom, dynamic, inventive.
**Tyler** 41:19 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:20 On the fly.
**Tyler** 41:21 On the spot.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:22 What a spot.
**Mike Dame** 41:23 You know, that's, I mean, that's basically what ours does. But like I said, yeah, there's limitations to it. Like I think in Java, we can get, you can basically say class and method.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:35 Meth.
**Mike Dame** 41:35 And you can get all the arguments and return values from that in Go. I think you guys know from the Go auto instrumentation, it's tough to know where your arguments and return values are. So you can't really do a general approach to that.
But yeah, it is something that is pretty popular that people like.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:57 Nice.
**Mattia Meleleo** 41:59 Actually, in my PR, there is this argument parsing for Go. So they come for free.
But I think the binary needs the PCLN tab or something like that.
Oh, yeah.
Yeah, for other languages, it's harder.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:20 There was a proposal from somebody from New Relic, I believe, on the Go auto instrumentation that they wanted, but they never came and contributed a change. They wanted to add this.
Yeah.
**Mattia Meleleo** 42:32 Oh.
**Mike Dame** 42:32 Remember that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:35 You're right. Yeah, if you had the PC on tab, you can probably guess if it's a pointer or is it an embedded struct and you can kind of say, okay, you need to skip three arguments and go to the next one and grab it from there.
**Mattia Meleleo** 42:48 Yeah, I tried instrumenting some gRPC server.
endpoints, and all the arguments came for free, without even.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:56 Wow.
**Mattia Meleleo** 42:57 find anything.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:58 Wow.
**Mattia Meleleo** 42:59 It was like magic.
But for other languages, for compiled languages, you need the… at least the… Dwarf informations.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:09 Yep.
**Mattia Meleleo** 43:10 And for other languages like Python, JavaScript, I don't think you have this possibility. You only have the USDT probes.
And they are slowly removing it from everywhere. I don't know why.
I think it'.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:26 I don't miss it.
**Mattia Meleleo** 43:27 Or the number.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:27 Yeah, and nobody's using them, yeah.
But for Java, you can do it. I think Java, you can get the signature of the method.
It's… you know exactly where the parameters are, where the return… and there's only one return value, so… Not too bad. You do need to have some reflection and pull out stuff from it, but.
So… Yeah, and Java is doable.
Node.js, Python, I don'.
**Tyler** 43:59 Yeah, okay. Definitely more to look into here. This is definitely a rich area.
Okay. Moving on on the agenda… It looks like I'm up. So the one thing I wanted to ask you all is, there's this open issue in our milestone for the route per service semantics here. This is an issue from a while ago around the V1 stuff, but essentially.
There's two places to do route matching. One's on a per service level, the other's on a global level. And this ignore patterns and unmatch is useful as on a per service as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:39 Mmhm.
**Tyler** 44:40 This was, I think an interesting issue. We did add, directional specific routes for, like, per workflow in the V2 config.
So the HTTP routes incoming and outgoing exist, but the global route map pattern is also directionless, and the ignore pattern and the unmatched routes are still only global.
So, I guess my question is, is, like.
What are people's thoughts on this? Do we want to continue this? We want to change the configuration. I saw Mario had his hand up. We could pause here.
**Mario Macias** 45:18 Yes, what I was about to say is in your comment. Yeah, I think it's interesting, and it was a long-time request, having both… To be honest, I didn't know we supported for service route matching.
I think we should unify both, but of course.
also try, maybe the logic we apply in the global routes matcher regarding to ignore and and match. And how do do we do the? How is the matching? We should port it also to For these persons.
**Tyler** 45:54 Okay.
**Mario Macias** 45:54 Series.
**Tyler** 45:55 Yeah, yeah, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:57 I agree. I think both can, should be directional.
or have the option to use the directional if you want, instead of the common one.
Because a lot of people have, like, this weird services where they just produce a bunch of junk roots, and then they… want to get rid of them, but it's a specific case, so I was like, yeah, in most cases, it's fine what you guys do, but then in this one specific case, I don't want you to… all of those should be… I don't want to be paying for… a cardinality here for this.
**Mario Macias** 46:30 Yes.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:30 here.
**Mario Macias** 46:31 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:33 I think Gautam, I mean, he's with Rufana I know what he's doing. He… he uses this, product redec, or… where he kind of captures websites.
That he finds interesting into, like, his own repo.
He has a home lab, and… but it's an interesting use case, where, he… so he does, like, sort of a save of a website locally, so he can read it after, offline, and whatnot.
And that's just gonna hit all the external routes for… for everything, and it's just random stuff from the internet, and it's like, no, I don't want that in my metrics.
So I want to cut that off, that's why he needed… oh, but the incoming, I want to know what the APS were, but the outgoing, I want to just cut them And so I think it is a real use case.
**Tyler** 47:26 Okay, so if I understand, like, the idea is to take this, like, ignore patterns, and unmatched stuff and move that into the per service, but then also to have, Mmm.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:36 Global directional option, yeah.
**Tyler** 47:39 Global directional. Yeah, that's the thing. Okay, yeah. Okay, cool. Yeah, I think I got that.
Yeah, okay, cool.
I can take that and move on with it. Awesome.
I will take that, under advisement. Okay, next up.
Rafael has updates.
Yeah, so…
**Rafael Roquetto** 48:03 Hi. Yeah, so I just wanted to let everyone know that I'm leaving Rafana at the end of the month.
And, I still don't know… my availability for the project going forward. Like, I… that… that is not a no, it's a… a question mark for now, but I'll try to keep everyone Up to date, and then we can take it from there.
**Tyler** 48:32 Well, that's, yeah, I'm sad to hear that, but hope it's, hope it's for the best for you, and.
Yeah, definitely. Thanks for the heads up on that one.
I guess maybe we'll just keep in touch over the next month until you have a better understanding of what your availability is going forward, and then, yeah.
That make… that make sense for you?
**Rafael Roquetto** 48:52 That makes sense. Yeah, I'll make sure to keep everyone up to date as things unfold because I'm not sure myself how that's going to be. I need to get started first to figure these things out.
So,
**Tyler** 49:05 Jeff.
**Rafael Roquetto** 49:06 I'll keep everyone posted, but yeah, it's been cool.
**Tyler** 49:10 Yeah, well, yeah, just let us know, if we need to adjust, roles, or if you need to just step away. Yeah.
unfortunately, I've been in this long enough to have seen this happen multiple times, not a particularly situation, just people come and go in the project, you know? So, yeah, that's definitely… It's always tough, yeah.
**Rafael Roquetto** 49:28 Yes, sir That's it, right.
**Nikola Grcevski @ Grafana / OpenTelemetry** 49:31 As a project, we have a lot of maintainers, so that's… I mean, losing your file is pretty big, but… I think we'll be okay going forward, but… If you can, you know, still contribute to the project, that would be… That'd be great, but… Yeah, like I spoke with Alfredo, I told him, I got, I mean, you know, you're starting a new job, I mean, you're gonna need to focus and, you know.
May make yourself like a footing there, so we can't expect that. So we're working with something completely unrelated to this job in this spare time, right?
**Tyler** 50:06 Yeah, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:07 They're still EVPF, just not right, not this kind of, not for this purpose, right?
**Tyler** 50:14 Not the cool kind.
**Nikola Grcevski @ Grafana / OpenTelemetry** 50:15 No, no, he's doing cool stuff. It's just not for observability, I guess.
**Tyler** 50:21 Yep.
Okay, well, cool. Yeah, well, yeah, like I said, keep us posted, and we'll… we'll plan accordingly.
**Rafael Roquetto** 50:31 Yeah, we'll do, and I'll be in this meeting next week still.
**Tyler** 50:35 Okay, perfect.
**Rafael Roquetto** 50:36 Bye.
**Tyler** 50:38 Okay, that looks like the end of the written agenda.
Any other updates or topics people have.
Well, cool.
Awesome, sounds like there's a lot of interesting work still to be done, so we can probably end the meeting here.
Thanks everyone for joining. I'll see you all in a week's time, or asynchronously. Till then.
**Rafael Roquetto** 51:05 Thank you. Bye.
**Mattia Meleleo** 51:06 See you. Bye-bye.
