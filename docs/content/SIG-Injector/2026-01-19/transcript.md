SIG: SIG Injector
Date: 2026-01-19
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

PL Pavol Loffay 00:00:44 Hello?
Bastian Krol 00:02:05 Hey, folks!
PL Pavol Loffay 00:02:08 Oh, hi there.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:09 Dang.
Bastian Krol 00:02:10 Hello, Nicola. Hey, Pavel, nice to meet you, new face in the meeting.
PL Pavol Loffay 00:02:17 Nice to meet you as well. I'm from Red Hat, and I'm working on the operator.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:02:23 Nice.
Bastian Krol 00:02:23 On the Open Telepiture operator?
PL Pavol Loffay 00:02:26 Yep.
Bastian Krol 00:02:26 Oh, interesting.
Awesome. Yeah, I think there's a lot of overlap between the operator and the injector, or at least we are discussing operator-adjacent topics a lot here, so that's good.
PL Pavol Loffay 00:02:42 I would like to talk about it today. I'm into this SIC, I don't know… I'm… I'm familiar with the approach, but I have a lot of questions how it works, and I would like to explore how we could use it in the operator, and…
Bastian Krol 00:02:56 That's awesome. I'm not sure, how big our crowd will be… Because I just… Jack just wrote in Slack that there's a… that today is a U.S. public holiday, so I guess a couple of folks will not show up.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:03:12 Alright.
Oh, yeah, it's an okay day, yeah.
Bastian Krol 00:03:16 Yeah, it's Masonle Nattingne, exactly. I wasn't aware of that until 3 minutes ago, so yeah.
That's… yeah.
Hmm.
Sure, yeah, I guess we can get started with your questions, then we can just use that meeting for that. Or, I don't know, Nikola, do you have… do you have topics?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:03:41 I had one, like, a while back, but we can discuss that next time. I was just wondering if we can just… I don't know, we have a bunch of tests from the eBPF instrumentation Project that try all these different languages and stuff, so I was thinking if we can make sense to port some of those to have end-to-end tests and check if the expected output is there and all this stuff.
Bastian Krol 00:04:02 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:03 I don't know.
Bastian Krol 00:04:03 We have… we have a… two integration test-like setups already, so one is just testing the injector binary in a container image with different runtimes, Node.js.NET, JVM, so that's… covers to… to a degree, and then we have the packaging integration tests, which basically install the other Debian or RPM package, and then just look for a line. But, I mean, if there's valuable stuff in these other test suits.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:43 Or we can extend them. Yeah, I was thinking more of, like, making sure the data will make it through the collector, and it's correct, or something, like…
Bastian Krol 00:04:51 Oh, my goodness.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:51 attributes make you through as well, like…
Bastian Krol 00:04:53 Make sure.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:54 Where we don't mess up environment variables in a way that's preventing something from working.
Yeah.
Bastian Krol 00:05:01 Could be worth exploring, yeah.
Absolutely.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:05 Alright.
Bastian Krol 00:05:05 So, but I'm not familiar with the EBPF Center, or…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:10 No, we don't have to use the same framework. I'm not… I don't have to introduce anything new, I can just extend your existing tests and make sure that I throw in a collector and verify some output.
Bastian Krol 00:05:20 Hmm.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:21 in Jaeger or something, I don't know.
Bastian Krol 00:05:24 Yeah. Yeah. Why not? Sounds good.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:05:27 Huh?
Bastian Krol 00:05:28 Cool.
Yeah, I don't… I don't have… topics for today… Pavel, Do you want… do you want to start with… with your questions, or… Yeah. Okay.
PL Pavol Loffay 00:05:45 Secondly, Bish… talk about what we have at the moment in the operator, and what I would like to do, and then I have many questions about the injector, and how it works and configuration.
So right now, and maybe you know it, the operator supports injecting the auto-instrumentation into workloads.
It uses the init container that, copies the… specified auto-instrumentation library into the port file system via a shared volume.
and configures the SDK and instrumentation of our environment variables. There is a lot of issues around it. It needs to watch if variable is used, and a bunch of things, or… there's a bunch of issues related to that. And… One of the good things about this is we only, or the operator only, kind of, initialized the init container only with a specific language instrumentation, so it's kind of small.
And… this has been around for a long time, couple years, probably. I created it originally.
Bastian Krol 00:06:58 Oh, he.
PL Pavol Loffay 00:06:58 the hotel.
And I think it got really good traction, people are using it, it's very easy to get started, the config is simple, and… It mostly works.
Bastian Krol 00:07:11 Yeah.
PL Pavol Loffay 00:07:11 But, we would like to, kind of, kind of move it forward.
And we thought maybe using the injector will, simplify two things, our maintenance in the operator, because right now we have to maintain many instrumentation images, and I don't know how Python exactly works, or .NET… or .NET, or Node.js.
And sometimes we had to maintain, like, small initialization code in the operator, and it was a bit annoying. That's one part. Second part.
The users, they had to spec… they had to use the language-specific annotation.
It's not terrible, but if we could kind of solve this problem by kind of automatically figuring out the language, it would be awesome.
And the last part was the configuration, that if a user is it… if a deployment or pod is using… it's kind of mounting environment variables from a config map. We didn't support that because there was… we couldn't figure out, what was going on in the operator.
So, presently, I know nothing about Injector.
Bastian Krol 00:08:37 And.
PL Pavol Loffay 00:08:39 I would like to understand how this could be used on Kubernetes.
Bastian Krol 00:08:43 Yeah, absolutely. I can totally, talk about that, because we are using the OpenTele Miniature injector currently in the dash zero operator, so our own Kubernetes operator that, that, my, employer offers. It's also open source, but it's different from the OpenTelemetry operator, although it does similar things. Can you first clue me in a little bit more about how the telemetry operator does it, because I've not spent too much time with it. So, you have an init container per runtime, like a JVM init container and a Node.js init container?
PL Pavol Loffay 00:09:29 Essentially.
Bastian Krol 00:09:30 Correct? Okay, and then if a user annotates a workload with inject this, it's a JVM injected with the JVM thing, then how exactly does the operator do that? I guess it sets a Java agent, or Java tool options on the work.
PL Pavol Loffay 00:09:50 load.
Bastian Krol 00:09:51 And it's actually said, init container, and is it…
PL Pavol Loffay 00:09:55 the init container copies the Java agent from the init container to the shared volume.
Bastian Krol 00:10:01 To a shared way. Okay, that's the same that we do in the distributors thing. Okay. Yeah, I can elaborate a little bit on… on… how we are using the indexor in the zero operator. So that's very similar. We also have one instrumentation init container, but it contains, the image contains the agents for all runtimes that we support, so it's not one image per runtime, but a Catch all.
init container image with the JVM agent, Node.js, a node module for auto-instrumentation, and .NET stuff.
Michele Mancioppi 00:10:42 And so to let both libcies.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:10:45 Yeah.
Bastian Krol 00:10:46 yeah, for both, libc variants, so the .NET stuff is different per libc flavor, and of course, in Injector binary, is independent of it, but… works, works with both slip Cs.
So that's all in the init container, and we do the same as you, we copy it over in the init container phase to shared volume, and we said.
LD preload, so we don't set node options, or Java tool options, or any of that, we set on the Kubernetes level, we just set LD preload, Which is a mechanism that been around on Linux for forever that preloads a specific library, so it's just a space-separated list of shared libraries that you basically give to the linker, and whenever a process then starts up, it will inspect the LD preload list, so… and before even the process actually gets control, the… Dynamic Linker will inspect this list and load these libraries first, and that's where the injector sits.
And then the indexor reads the current environment.
and potentially modifies it, so… pretty, pretty sure it will modify it. And then the injector sets node options, and Java tool options, and core CLR profiler, and all that stuff.
And the advantage of doing it at that level is, if you, if you set, like.
Java tool options on the Kubernetes level, of course, you see whether or not it's set on the Kubernetes level, but it could also be set in the Dockerfile, or… Script.
Wow.
PL Pavol Loffay 00:12:49 Yep.
Bastian Krol 00:12:49 or in the config map, as you just said. So, we don't care about any of that, because we see exactly the same environment that the actual process within the container sees, and then we have all the facts, and if there is… for example, if there is already a node options with With stuff in it, that's fine, we just prepend the… Autom instrumentation node module there.
or if Java tool options already set, we can add our stuff to it without overwriting it or getting overwritten by something else. So that's… that's one neat thing. And then, when the injector has read the existing environment, it basically uses setEnf to write back what it thinks the environment should be, so it's called setEnf for Three runtimes, basically.
PL Pavol Loffay 00:13:46 Does it still… use the environment variables to configure the SDK?
Bastian Krol 00:13:53 Yes, yeah.
So the injector basically is just a small piece of software that reads the environment variables that exist prior to injection, and then writes back new environment variable values via setenf. That's basically all it does.
Configured through a configuration file, or whatever, and .
PL Pavol Loffay 00:14:16 And is… is there any… is there any configuration file for the injector? Or, like, some configuration… stable configuration file, or some… spec, or does it use the hotel SDK schema, or anything like that?
Bastian Krol 00:14:30 There's a very simple text-based configuration file format that the injector currently understands. It's, there's an example file somewhere in… I guess you already have had a look at the injector repository?
Probably, yeah, there's in packaging somewhere, packaging, FBM, ETC also, there should be an example of that hotel conf… AutoInjectTalk.conf or something like that.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:58 Yeah, I guess it's simple on purpose, right? Because we want to minimize dependencies in this injector library so that it's easy to be ported.
Bastian Krol 00:15:09 I mean, I think in the last meeting or so, someone brought up that my baby should be more in line with what other components do, like, other existing configuration file formats, but currently it's basically a properties file, so it says Node.js instrumentation equals, and then a pass.
And JVM.
Michele Mancioppi 00:15:30 Yeah, I agree.
the only thing that we need to… for that configuration file to be able to say is, A, should we turn on instrumentation for Java, and B, where do we find it? And then the same for the other languages. It doesn't do anything else.
PL Pavol Loffay 00:15:45 And what… what languages do you support at the moment?
Michele Mancioppi 00:15:49 Java.js.net, Python is something that we know how to do. It's a bit more involved because, Python and some of the dependencies of the Python SDK, which are not safe to auto-inject, specifically protobuf.
I am confident, Ruby is easy to do.
Erlang would be easy to do.
We…
Bastian Krol 00:16:13 I think PHP might also be worth looking into. It apparently supports 0, zero code.
Michele Mancioppi 00:16:22 What's similar.
Bastian Krol 00:16:23 out to instrumentation, that's what I read on.
Michele Mancioppi 00:16:25 Yeah, but the problem with PHP is that the, the SDK, as far as I know, works only in version 7.
And, it doesn't have a mechanism to not activate itself in incompatible versions of the PHP runtime.
Bastian Krol 00:16:38 Okay.
Michele Mancioppi 00:16:39 Yeah, that's not great.
Bastian Krol 00:16:40 about instrumentation, yeah.
Michele Mancioppi 00:16:41 I mean, don't take the… don't quote me on that, but the last time I looked at it, that was the case.
Bastian Krol 00:16:47 Yeah, yeah, no, I'm… That, that sounds fair.
PL Pavol Loffay 00:16:51 So, Java.net node.js.
Bastian Krol 00:16:53 That's the currency.
status quo, I think Python will be, by hook or by crook, we will get support in some time soon, at least that's the plan. So, Python is very much on our shortlist of things to do. Ruby, a little bit less. I think Antoine was looking into Ruby at some point, but also, I personally find the market share of Ruby these days is probably Maybe it makes it less worth it to invest there, but yeah, we could, I guess.
Michele Mancioppi 00:17:24 Let's put it on that. If the Ruby 6 said, oh, we would like support in the injector, and they make sure that just by adding Ruby ops with a particular set of values it works, then we would gladly add support for that.
Bastian Krol 00:17:36 Absolutely. I mean, that's easy.
easy pass, basically. Yeah, so, does the… what does the OpenTelemetry in, operator currently cover?
PL Pavol Loffay 00:17:50 the Java notice… nets… PHP rule. It supports a lot of languages.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:00 Yeah, okay.
Michele Mancioppi 00:18:01 Apache, NGX, if I recall correctly.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:04 Yeah, internet, yes.
Bastian Krol 00:18:05 Okay, yeah, so that's quite a bit more, of course.
I mean, I guess if you want to look into using the injector, you could probably introduce it gradually for, like, just.
Michele Mancioppi 00:18:17 H.
Bastian Krol 00:18:18 Just one language at the start.
Michele Mancioppi 00:18:20 overload.
Bastian Krol 00:18:21 Or something like that. So there's no hard cut, necessarily, I guess.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:26 Oh, well.
Michele Mancioppi 00:18:26 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:27 Can I ask you a question?
In your current setup with the OpenTelemetry operator, do you support, for example, other platforms than Linux, For example, I don't know.
BSL… BSD, or, Windows, there's…
PL Pavol Loffay 00:18:44 offers support.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:45 any of those? No, it's just Linux, right?
PL Pavol Loffay 00:18:48 Yeah, I'm not sure who runs Kubernetes on Windows.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:18:52 You'll be surprised. You'll be surprised. You'll be surprised.
Bastian Krol 00:18:55 I already had… That one zero customer who, asked about that, and they run Windows nodes with Kubernetes. I was also very surprised.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:07 Yeah, I know.
Bastian Krol 00:19:07 But we needed to make an exclusion, for the OS, annotation that is on the node, or something like that, so… But, yeah, realistically, the injector will also, for the very long foreseeable future, only support Linux And we are.
Michele Mancioppi 00:19:25 I mean…
Bastian Krol 00:19:26 supporting ARM and AMD, and that's the two architectures, I'm not sure if the operator…
PL Pavol Loffay 00:19:33 Everything's logged.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:34 Yes, I…
PL Pavol Loffay 00:19:35 I think IBM architectures as well.
Michele Mancioppi 00:19:38 Yeah, but in reality, the support here is… so the injector is built… it's more bound to Lib C than to Linux.
The, so if it's not running… if the process is not running a flavor of libc, dynamically linked, then the injector doesn't inject.
Bastian Krol 00:19:55 That's true, but it's also very much bound to the ELF format. So… it is bound to Linux quite tightly.
Michele Mancioppi 00:20:02 Yes!
Yes. Yes. The ELF on PowerPC is not so different, but yes, that's a yes.
Bastian Krol 00:20:14 Okay. Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:17 I mean, Parker.
Bastian Krol 00:20:17 But also, I mean, this is like… 95% of production workloads is on Kubernetes is Linux with these two architectures.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:28 I mean, you say Linux, also Linux Mayframe? ZOS?
Right.
Michele Mancioppi 00:20:32 Yeah, so don't do that.
I believe, I believe, I believe it would work.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:37 Yeah.
Michele Mancioppi 00:20:37 I got He has ever tried.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:39 Absolutely. No, absolutely, it will work. Yeah, nothing we do is special to x86 or ARM.
Bastian Krol 00:20:48 I guess for other CPU architectures, it's… it's probably mostly a matter of… of, building the… cross-compiling the binary, and… but, yeah, we would… I guess we would need.
Michele Mancioppi 00:21:02 I mean, the moment it kind of looks like Linux, and feels like Linux, and it has a lipc, it should work. We are looking up the location of the program header in ELF, using, the UXV.
they were… it should… if it's Linux, it should work, really. I would be surprised if there was a bug in inside OS or similar stuff. BSD, I'm already far less convinced.
Bastian Krol 00:21:27 Yeah, but I think the other point is more important, so it's really only feasible for things that kind of have a runtime, like a JVM or the Node.js runtime, so it… the technique that we are using here will never work for anything that doesn't have a lipc, like, if you compile Go a certain way, that's… and no matter how you compile Go, basically.
Michele Mancioppi 00:21:51 Exactly.
Bastian Krol 00:21:52 will, will not work, or, or Rust or C++.
Michele Mancioppi 00:21:56 That's…
Bastian Krol 00:21:57 Kind of not, possible with this injection, so…
Michele Mancioppi 00:22:02 Actually, the, what's his face? M2 in, in GitHub?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:10 Mclean.
Yeah, Morgan. Morgan McLean.
Michele Mancioppi 00:22:13 Morgan was asking about what are our thoughts, because I opened the note app for the system packaging to use the injector to create DEB and RPM. He was asking, yeah, but what is the interplay between the injector and Bela?
Which the answer was, I think they cover different languages, so it could also work well together.
Especially at the system package level.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:33 Yeah, that's what we're aiming for, yeah.
PL Pavol Loffay 00:22:36 and…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:38 So cover the cases that they're not covered until we have a way forward that's better.
Michele Mancioppi 00:22:46 Scope for Bela to re-implement all auto-instrumentations in the Java agent, but in eBPF?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:55 No, we'll never do that job. We'd like to use the Java.
Michele Mancioppi 00:22:59 That's cool.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:59 Boys.
Michele Mancioppi 00:23:00 Right, so really your focus is Rust, C++, Go.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:06 Go… I mean, we support the other languages, just in case some people sometimes have library incompatibilities or version incompatibilities. Let's say they're running an old Ruby version.
Michele Mancioppi 00:23:16 human words.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:17 And, the SDK says no.
Michele Mancioppi 00:23:20 I just… version…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:22 Whatever, 5 and above.
And people said, well, I have Ruby 3, what am I supposed to do? And then you're like, well…
Bastian Krol 00:23:28 Update!
Michele Mancioppi 00:23:30 date.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:30 Well, no, some of them will say, yeah, update will take 2 years.
Bastian Krol 00:23:34 Yeah, yeah, no, I know the… I was making a joke, sorry. Go ahead.
Michele Mancioppi 00:23:37 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:39 Update takes 2 years if we stop working on the product features, so… yeah.
Michele Mancioppi 00:23:46 Yeah, our language is, like, go… Pretty much.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:54 That's… that's the… sort of the primary target. We even tell people, like, if you are a Java customer and you can load the agent, you just load the agent, or use the injector, just don't… Don't mess with this. I think .NET is also in a sort of funny situation, because… a little bit, because they only support one agent at a time, so sometimes people want to run some security stuff, but also get this, or that, and…
Michele Mancioppi 00:24:20 Yeah, that was great fun, yes, at Instana, we had the same problem. You get one profiler.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:24:27 it's sort of an escape hatch, right? For us, we see it as, yeah.
So you have nothing, you can easily get to something, and it may not be the best, because it's eBPF, and we can only see at the kernel level, we can't touch the languages, or we don't want to expand, but, But yeah.
It's actually…
Michele Mancioppi 00:24:47 I have a question about this. So, the, One of the things that, for example, Audigos has been doing.
Is to, touch stack frames to add, well, not the stack frames, but the stack, to add, arguments to libraries, to functions that are invoked in the library, to be able to pass the trace context.
Is it something that Bela also does?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:12 Yeah, yeah.
Yeah.
Michele Mancioppi 00:25:14 So you do touch the application, in a sense.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:25:17 We… we do touch… So Go, obviously, we do a lot.
I don't know, Odigos is now proprietary, there's… So I don't know what all kind of libraries they instrument, but OB is part of OpenTelemetry, or formerly Vela.
So we do support a number of libraries for Go.
We do… try to load a tiny Node.js agent, dynamically.
Because Node.js is… if you don't have… our instrumentation with the SDKs, it's… difficult to do context propagation, because… I mean, it was okay until no 20?
They did most of the async parent-child relationship creation in C, but then they rewrote a bunch of stuff in JavaScript, so we can't touch it. So, we have to inject the tiny agent that helps us Figure out a context propagation internally.
Java, we do also now, which is still a work in progress, attach a tiny agent dynamically without restart, because we can't see TLS.
And for the thread pool, But these are all, like, workarounds in case you can't load it, or… People don't want to use… this or that.
What else? Python for async I.O.
We need to… otherwise it's single-threaded, so it's easy to do context propagation, but async I.O, There's a PR that's in progress right now.
And, yeah, the other two we attach to is NGINX and Rails. Rails, specifically Puma, because of their reactor framework. That's very popular.
But those are just, to get us… Small, kind of, like, probing into specific libraries for the purpose of Allowing us to do context propagation. But, at the end of the day, if you add the SDK, you always get better insights than if you use OB or Baylor, because it's just not enough richness of the… what the language can give you. Let's say you're running Java, we don't instrument Hibernate, so if you really want to see the Hibernate sort of specific… Details there, what it did with the query, how much it did work here and there, no. You may see the final sequel, and how long it took.
Michele Mancioppi 00:27:41 And I have another question around… what the OpenTerm Operator does with NGINX and Apache.
the, if I recall correctly, those extensions Need, for the configuration file to be touched up.
Right?
I think you just load a kernel in one of those modules, I think.
Huh.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:06 Bing.
Michele Mancioppi 00:28:07 So, technically, it is something that could be done also in the OpenTalentry injector.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:11 I think you just need to copy a file in a specific place, if I remember correctly, last time I looked them back.
Bastian Krol 00:28:19 Babel, do you know how the operator, works with Apache and Linux?
to instrument?
PL Pavol Loffay 00:28:27 Good.
It touches the config file. I'm not very familiar with that, but it does a bunch of things on the config file. It's not very… It's messy instrumentation.
I would say.
Bastian Krol 00:28:40 Oh. Okay.
Michele Mancioppi 00:28:41 That is also what we ended up doing at Instana way back. We needed to effectively do terrible things to the nginx.conf, so I was wondering, because, of course, I mean, implementing an NGINX.conf parser is something that nobody would like to do in the injector.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:28:59 And also another thing I wanted to mention, since we're talking about the interaction between OV and the injector, we have planned for this year to actually see if we can actually work with Obi as a in the background, and have the SDKs included as well. Because there's one little thing, but it's important to some group of people that.
Michele Mancioppi 00:29:25 Colby, or formerly Bela, does better, which is…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:29 Request time versus service time.
all the SDIC instrumentation will give you just the service time off the… when the request gets picked up by the internal frameworks.
While in EVPF, you can also find the full request time, which is from… because we see the data as it comes on the wire.
So, as soon as the network sees the get, whatever, request, HTTP or gRPC, whatever it is, we start counting.
So…
Michele Mancioppi 00:29:56 I'm laughing, I'm smiling, because, that is… I mean, you're talking about the start time, and have you ever seen Twitch TP instrumentations agree on when the request ends?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:07 Exactly.
So… So because of that, and for us, request ends when the kernel sees the response back, so we know exactly to the client, so…
Michele Mancioppi 00:30:19 Oh, wait a second, is it, first byte, or is it end of file, or…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:23 So we wait, there's a… sort of, like, a logic, because we see the 200, okay, whatever, right? And then we know that, okay, this is a guy that's about to end.
And then we monitor what's happening, so it's sending more bytes, it's sending more bytes, and eventually it stops. So, two things would happen. One is, it will do TCP close, which is… okay, good, right?
Michele Mancioppi 00:30:47 in HTTP3 or Speedy, no?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:30:50 No, with those, no. We don't support those. But, with, if there's a new request. Also, sometimes they don't close the connection, they just, keep alive, so they'll try again on the same software, right? But then we'll see that there's a new request, so it kind of bumps the old one out.
Michele Mancioppi 00:31:12 I kind of expected you implemented the Miami type specification with the chunking.
What? No. Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:21 No?
But that's actually not a bad suggestion.
Michele Mancioppi 00:31:25 Actually, it would be probably simpler than what you're doing now.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:28 Yeah, maybe that's easier, yeah.
But the good news is what we're trying to do, at least this year, is to, on incoming requests that are coming to an SDK, we'll try to modify the incoming header.
To kind of chain the eBPF timing around the SDK timing.
So you'll get, it's kind of rapid, so we can get the.
Michele Mancioppi 00:31:53 The request time.
We write from within the SDK, or what?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:31:58 No, the SDK will be oblivious, it won't know, they'll just pick up the trace parent, but the context part of the trace ID, not the trace ID, but the… Span ID will be different than the one that came on the wire. It will be, kind of, made payment.
Michele Mancioppi 00:32:13 Interesting.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:15 So we're hoping that that way we can actually see the full…
Michele Mancioppi 00:32:20 How are… how are you going to do that without a spam processor?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:25 We don't have spam process here.
Michele Mancioppi 00:32:28 So the way that I understand is that you want to add an HTTP header. Let's say that you put something in trace state, because we feel funny like that.
And, that timestamp is supposed to be used by the SDK somehow, and I'm missing this somehow bit.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:45 No, the SDK will ship its own data, but Obi will ship this additional span that wraps it.
Michele Mancioppi 00:32:50 Oh, dear, okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:52 Yeah.
Michele Mancioppi 00:32:53 Oh, boy.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:55 Yeah, even…
Michele Mancioppi 00:32:56 That is gonna wreak havoc the trace.
Structure, like, there's no tomorrow.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:01 It shouldn't. I don't think… I don't think so. I think it will work.
Because there should be independently, as long as they chain correctly, as long as they make it back to the, To your database or collector, it should work.
Michele Mancioppi 00:33:14 Yeah, but you're going to put, what, two server spans, one after the other?
And one is more server than the other? I mean, that's breaking the trace.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:22 That's the question, yeah. So, we need to work with the hotel community to figure out what we do there, you know.
Michele Mancioppi 00:33:28 That's why I immediately thought, I mean, you want a spam processor, right?
Right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:33 Yeah, then that one, yes, you're right. That's something that was mentioned on the call when we discussed that change, that, We'd like to see if there's a possibility to figure out what we need to do from a motel here, and maybe a change in…
Michele Mancioppi 00:33:49 Yeah, I feel… I feel that the span process is a better way, because if you start adding multiple server spans, you're… screwing up a bunch of traces, and even creating some tempo. They're probably breaking customers at that.
It's, yeah, I don't… it's not very hot.
Bastian Krol 00:34:07 I'd like to circle back, because we… I think we got a little sidetracked, Pavel, did you… you were probably in the middle of your list of questions, or…
PL Pavol Loffay 00:34:18 Yeah, I have one more, Is, like, I'm not sure… if the injector would as well use, like, a Docker image for the unit container, or those libraries would come from somewhere else?
Michele Mancioppi 00:34:35 Use the Docker image, yes.
PL Pavol Loffay 00:34:37 And is it something you're protesting?
Bastian Krol 00:34:38 In the current OpenTelemetry injector project, we don't have any container image, or we don't produce a container image, we just have the injector binary and a Deviant and an RPM package. We are building an init container image over in the 0 operator repository with the OpenTelemetry injector and a set of instrumentation agents, so that That part still lives in… in our… the zero repository, and I've not ported it over yet.
But that is something that we could potentially do, although I'm not sure how much everybody in the world agrees on what should go into that container image, but there's potential for synergy there.
Michele Mancioppi 00:35:26 The problem with, so problem in, in, air quotes.
Is that the more languages we support, the more that image grows, and the more that image grows, the more space we need in the NTDR.
For, copying over the tracers, because we need to copy all of them.
Bastian Krol 00:35:42 Since we do not know which processes we're going to find inside.
Michele Mancioppi 00:35:46 Now, Kubernetes shipped in 1.36, the, image volumes, that is something that I would love for us… Yeah, something like that. I would love for Destro to try, to get some experiences with it, but for older Kubernetes, the more tracers we put in there, the more is effectively in memory.
Bastian Krol 00:36:08 Yeah.
And I think, realistically, that is something that's… at earliest, I'm not sure when customers will start using 135, maybe… later this year, next year, I don't know.
Michele Mancioppi 00:36:21 That's very cute. It's similar to B3, right?
Bastian Krol 00:36:25 Pardon?
Michele Mancioppi 00:36:26 It's going to be like Ruby 3.
Like, you tell them upgrade, and say, yeah, we could do it if we stop doing product for 2 years.
PL Pavol Loffay 00:36:35 Yeah.
Bastian Krol 00:36:35 I don't… I'm not sure. Whatever, but what I'm saying is it will be quite a while until we see a decent percentage of people being on a new enough Kubernetes version for that.
PL Pavol Loffay 00:36:48 Is it something that could maybe contribute to the repo?
And I think that would make it easier for us to start consuming something like this, and start experimenting.
Michele Mancioppi 00:37:00 Actually, I have something that we are going to do. So there is the auto for the system packages, and in there it's mentioned that the Kubernetes operator is out of scope. Bastian and I are traveling to the Auto Unplugged in Belgium.
in a few weeks. And there, the plan is to… pitch how the SDK6 should effectively at least guarantee not to break the basic interfaces that we use in the detector.
And I would love for at least the 6 to actually get, you know, integration tests to make sure that if such an image is built, it's not broken by a new version of the SDK.
Until then, it's, I mean, the more we put in the injector, the more it becomes the injector problem to maintain, and without the sig buy-in, it's a bit dicey.
For example, I do not expect the Java agent to break the minus Java agent flag.
I do expect Python to do something that would break the way we would inject it, yes.
PL Pavol Loffay 00:38:12 Yeah, it happened in the operator as well. We had some issues like that.
Michele Mancioppi 00:38:17 Yeah, exactly.
PL Pavol Loffay 00:38:18 It's a clever idea to put this responsibility on their shoulders.
Michele Mancioppi 00:38:23 I think it's barely… it's absolutely necessary, because if we say in open telemetry we must have an auto-injection story, they do not get to break the basic mechanisms about injection.
Bastian Krol 00:38:38 Yeah, I think that that's a fair point, although, I mean, that is… The difficult or the challenges of enabling auto-instrumentation are very different per runtime.
Michele Mancioppi 00:38:51 Exactly, that's why, per runtime, they don't need to break them.
There are some runtimes that are going to break it.
much easier than others. Python is a terrible example, but for example, Node.js released version 2.0, which requires different flags.
And that's, something where we need to… we need to do a… I don't remember how we solved it in the injector busted.
Bastian Krol 00:39:15 didn't. It's… so, if you are talking about.
Michele Mancioppi 00:39:20 Jessica, too.
Bastian Krol 00:39:20 modules, and… oh, no, SDK, too, is not so hard, I guess, that can be solved. You can just make a… that's mostly about which Node.js version you want to install.
instrument, and we can just do a switch in a distribution, we do that. The real hard problem for Node.js, and I think that's only partially solved, or I've not seen a full solution yet, is, the difference between common JS modules, where you do minus minus require, or node options with minus minus require, and ECMASBIT modules, where you need.
Michele Mancioppi 00:39:56 minus minus 8.
Bastian Krol 00:39:57 Experimental loader, which… and you don't know ahead of time, and that's… yeah, that's… that's an issue.
Michele Mancioppi 00:40:06 Yep.
Bastian Krol 00:40:08 Yeah. Pavel, I, just took the liberty to add you to the Autel Injector channel in the CNCF, Slack workspace, and send you a link there.
Because you said you might take a look at contributing the container image, and basically we already have something that probably would fit that bill in the Dashivo repository, so feel free to admit.
Michele Mancioppi 00:40:37 By the way, there is also an old PR of mine in the operator.
Where, because the, the injector actually started.
in OpenTelemetry as an operator PR back in, I think, 2024.
And then it went a different route in the project. So there is also something, probably, that you can reuse there in the way.
PL Pavol Loffay 00:41:01 the instrumentations are applied in the LD preload.
So our mission, was to introduce new version of the instrumentation CR that would use the SDK config.
Directly in the CR, and then use the injector for injecting, but.
As I'm realizing, the SDK config is only supported by Java, Golang, and C++.
So… I'm not sure if it will be… well, it will be supported by others.
And yeah, Injectors, as well, supported by… Handful of languages, which might not be a problem, because we want to keep those Two different versions separate, and don't kind of offer… feature parity But still, it feels like… if I'm gonna propose this, and it's unclear for me when the support will be kind of wider across languages, then…
Bastian Krol 00:42:06 Sure.
PL Pavol Loffay 00:42:06 It's questionable whether we should go this route. I see the injector will get there, but the SDK config, I'm not sure.
Bastian Krol 00:42:15 And in particular, I think combining these two goals is maybe… I think it's quite separate from each other, and one is not really…
PL Pavol Loffay 00:42:26 Yeah, I, I thought… For some reason, I thought the injectors were using the SDK for config for, like, simplicity and, you know, but… Starts.
Michele Mancioppi 00:42:37 Speaking of which, does Bela plan to use the declarative config?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:42:46 Yes, yes, there's a work item in plan.
We do have our own declarative config in Bela, or OB.
But, it's not.
Always… doesn't look like the new spec.
Long story short, we always started with the config.
environment variables would override, but there was no such standard at the time from OTEL, so we just… Did whatever we thought was best.
Michele Mancioppi 00:43:16 Right, environmental robots do not override in the… in the SDK, in the character config, you need to interpolate them, right?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:23 So, if you have something configured with a declarative config, an environment variable, the environment variable does not take precedence.
Michele Mancioppi 00:43:31 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:31 Hmm?
Michele Mancioppi 00:43:33 It does not, no, you opt into the… This is how I remember it. You opt in with a config file with the hotel underscore experimental underscore config and var.
And.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:43:45 Yeah.
Michele Mancioppi 00:43:45 Yeah, that takes, there was actually huge discussions in the design of the creative config file about that, and if I recall correctly, the, trade-off where we landed was that, you can access environment variables in the configuration file with the usual interpolation.
But if you turn on the declarative SDK, forget environment variable configuration, because that's… so the SDK is going to ignore the built-in environment variable config, and allow you to interpolate whatever variables you want in the declarative config.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:20 Yeah, but sometimes it's so much easier to pass an environment variable just temporarily to fix something, or enable something, or…
Michele Mancioppi 00:44:28 Yeah, but I feel that the discussion went the other direction in the creative SDK, but I may be wrong.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:44:35 I mean, look, I mean, if that's the case, we won't change it in OB, I'll tell you that much. It's just against all, I guess, well-known principles. But, I mean, people can use the config as is, environment variables will likely override always.
I'm just… I'm willing to die on that hill.
Don't tell Jack.
So that's how the injector behaves as well, right?
So you can have your config file, but with environment variables, you override them.
Michele Mancioppi 00:45:09 The injector doesn't care at all.
For the injector, the clarity configuration does not exist.
It's not something the injector cares about.
Bastian Krol 00:45:17 Nobody.
PL Pavol Loffay 00:45:18 debate.
Bastian Krol 00:45:20 Nikola said this is, right, you can have the injector-specific config file and then override it with environment variables.
Michele Mancioppi 00:45:26 Yeah, sure, that is fine, yeah, for…
PL Pavol Loffay 00:45:31 Maybe briefly talk about how the injector handles the configuration.
Michele Mancioppi 00:45:35 It does not handle SDK configurations at all, so the only thing we do is we… I mean, we pass down the… we add to the process environment.
the runtime-specific environment variables we need to activate the SDK, so Java underscore tool underscore options equal minus Java agent jar, whatever, where whatever is the path that we have in this simple text-based configuration file about where to find the Java agent, and we also go and add stuff, to the, auto resource attributes.
environment variable, because there is a bunch of, languages, like Java, Node.
Java, python.net, that, are not using the get temp call to retrieve configuration like I don't know, auto resource attributes, but instead they go and read the location in memory where the process environment is specified. So we have to patch some environment variables at startup.
PL Pavol Loffay 00:46:45 And so… The operator, for instance, it has to specify the exporter endpoint, so this is something that is completely out of scope of the injector.
Michele Mancioppi 00:46:58 That's funny that the SDK picks up.
Bastian Krol 00:47:01 Yeah, but it should be… probably not be set by the injector, because I don't think it makes a lot of sense to, for example, pass that from the operator to the injector, and then the injector sets it. I think that the operator should just set that directly, because the operator also I guess, knows where the collectors are, and…
PL Pavol Loffay 00:47:22 Yeah.
Bastian Krol 00:47:24 Miss…
PL Pavol Loffay 00:47:25 Yeah, we had this issue that if a user sets environment variable in, like, a Dockerfile or config map, it becomes… Impossible for the… Operator to, to find out And this could be implemented in the injector.
Bastian Krol 00:47:40 That's so cute. You could override an auto-exporter endpoint… that is already there from the Docker file, but… Yeah?
Michele Mancioppi 00:47:53 Yeah, but it's a bit dicy to do…
Bastian Krol 00:47:55 It has complicated… can create complicated follow-up issues, I would guess.
Michele Mancioppi 00:48:02 It is, there are also some formats of environment variables are not the same between SDKs.
If I recall correctly, all the resource attributes in Python accept both colon and semicolon separators, because they can.
The, would be very, very dicey to do that, especially if your goal is also to support the declarative configuration file.
Alright.
So, in that case, the operator puts that auto-experimental file.
Whatever, and then the SDK picks it up, the injector doesn't need to get in the way.
PL Pavol Loffay 00:48:37 No, but I think… I'm trying to remember what users complained about in the operation. I think that's the fact that they said something in the…
Michele Mancioppi 00:48:46 That issue.
PL Pavol Loffay 00:48:46 Or config map, and we override it for them.
Michele Mancioppi 00:48:49 And that issue was, that issue was, if I recall the issue correctly, it was the Java tool options that, will, so a modification in the entry point in the Docker image will override what the, operator does.
Hence preventing… that is something where we actually, inside the injectors.
PL Pavol Loffay 00:49:09 This is sole. Yeah.
Michele Mancioppi 00:49:10 That is solved, yes.
PL Pavol Loffay 00:49:12 Yeah.
Bastian Krol 00:49:13 There's also…
PL Pavol Loffay 00:49:15 Similar things with the hotel underscore ones.
Bastian Krol 00:49:19 There's also one more thing in the indexor, so you can specify and… so in the main configuration file, you can specify an addition… pass to an additional configuration file that has… like… settings for the auto-instrumentation agent, and if that file exists and has settings, then you can basically, by that mechanism, apply config settings to all the SDKs. That's a mechanism that is already there in the injector, I'm not sure if it's… if it's used.
A lot, but that… that also… so I guess you could… roll out, also, the exporter endpoint to all the SDKs.
via the indexor. If that's something that you really want to do, it's another question, but the mechanism is there.
Michele Mancioppi 00:50:12 But again, if I'm correct about the way that the Lucrative SDK makes the environment variables be ignored.
That may not help you much.
Bastian Krol 00:50:23 Yeah, in cases where that is an issue, then it doesn't matter where the environment variable comes from, that's for sure. This mechanism can only set more environment variables.
And if they are ignored, by the SDKs, and they are ignored.
I mean, it's conceivable that He lets the injector write a configuration file somewhere.
but… That's, maybe more an integral,
Michele Mancioppi 00:51:01 I feel we very much should not do that, because the…
Bastian Krol 00:51:05 Yeah, no, no. I, I was saying we could, not, not, not heavy, not sure… Sure.
Michele Mancioppi 00:51:12 All the interesting bits in the declarative configuration follow. I mean, one is the exporters, but the interesting bits is which instrumentations you want to turn on and off.
Bastian Krol 00:51:20 And that is entirely language-specific. Yeah.
Michele Mancioppi 00:51:23 Do not see the point of that.
Bastian Krol 00:51:31 Yep.
Michele Mancioppi 00:51:34 In the OTAB that I wrote about system packages, however, I, I, did write up that the, so the auto-instrumentation package is for specific languages.
Should come with built-in, default files for the, declarative configuration format.
Because I understand that as a project, we are going with the character configuration format, despite the SIGs lagging behind in terms of implementation.
So I thought it made sense.
Bastian Krol 00:52:12 What do you mean by that? The SDK should include a file with what, exactly?
Michele Mancioppi 00:52:17 When you read the… when you read the autop, there is… several system packages, and I'm going to talk, Deb and Debian, with my excuses to Paolov, because RPM is not my forte, but there is effectively a meta package called OpenTelemetry, which then requires a system package, so a DBM package for the injector, and DBM packages for the one per language.
Java 1, Ruby 1.NET1.
Bastian Krol 00:52:48 These auto-instrumentation packages should be.
Michele Mancioppi 00:52:53 are, like, scoped to one single language. They suggest, they recommend the injector package.
And the scope is designed so that the vendor could define a system package for their own distro, for Java, for example, and then the user would install that Instead of the community upstream package. And in this Java, for example, let's take the OpenTelemetry-outinstrumentation-java.
That would have inside the, Java agent, the jar file.
And, ideally, sample files.
and a default configuration file for the declarative SDK. And the reason why we should be doing that is that there should be another package in the, In the system of interconnected system packages for the collector.
In case of, you installing, wanting to do APT, you install minus Y openTelemetry.
That should also come, in my eyes, with a collector.
And the SDKs should talk to the local collector.
And these things are actually really viable only if We add the declarative configuration format as part of the system packages.
Bastian Krol 00:54:20 You mean support for reading that to all the SDKs?
Michele Mancioppi 00:54:25 Yeah, I mean, in that case, the injector would go and say, hey, does the instrumentation package have a configuration file?
Yes, use that.
The user, of course, can go and, in their SystemDunit or whatever, set the author underscore experimenter underscore config and point to a different file they have.
Or they can just go and modify in the, slash ATC slash auto whatever, the default configuration that the system package installs.
And that, I think, is very similar in terms of what I understood the OpenTangular operator wants to do, to… by embracing the creative, configuration format.
Bastian Krol 00:55:14 Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:20 Hello. Son?
I want to ask one thing that we probably didn't discuss here, but I guess right now the… Hotel operator uses separate image for every language. Sort of download. You tag your deployment as, I want Java instrumentation, so I'll just pull the Java image.
If, say, the injector in the future, supported many, many languages, and we have to make this combined image to support this. Would that… you see that as a problem? Or… You still see that you want to retain the same approach of people tagging specifically the language, or you were ever considering going full auto-instrumentation, which is… you just label that you want to instrument this namespace, and it just happens.
PL Pavol Loffay 00:56:08 I would go with a simpler approach for the end user.
And if they are not had… yeah, we don't want an image.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:17 So they'll have to be manually tagged, right? Is that what you mean? Or one image?
PL Pavol Loffay 00:56:22 One image, single tag for all images.
What a single label that we want to use a label on the tech.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:29 Yeah, okay, that's good. Okay.
So that's sort of…
PL Pavol Loffay 00:56:31 I… we… like, it will be a new approach, I don't have experience with it, and maybe if you already use it in Dash Zero or Grafana.
Already got some feedback.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:44 Yeah, Grafana, we don't do it right now, but we're thinking of doing something like that, given that the injector project now exists.
Because for us, it's like, obviously we teach people how to use the hotel operator.
Which is great for people that… enough into the hotel ecosystem, they understand it, they know. There's plenty of good documentation there, people love it.
But there's also a lot of customers that… Simply don't have the time, or they're willing to learn.
PL Pavol Loffay 00:57:16 don't know, don't care. They want to use the simplest approach.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:57:19 They just give me one thing that does everything, sort of, like, one agent, instrument, the world kind of approach, and those customers… Sort of…
PL Pavol Loffay 00:57:32 Yeah, especially if Michaela mentioned this, image volumes? I don't know how it works, but maybe it's like a volume that you can have in a cluster that would contain the image.
Michele Mancioppi 00:57:44 It's, in fact, the container image is mounted as a volume.
I do not know where the image is stored, so I expect it's served from the file system of the node, but I never double-checked.
Bastian Krol 00:58:00 But the great thing about it is that it saves us the copy at init.
PL Pavol Loffay 00:58:04 Yeah.
Bastian Krol 00:58:05 container init step, and that can be costly, especially if you have, like… so our init container image is around 200 megabytes right now, and if you give the pod really very low CPU, then actually the copy step takes A considerable time, like a couple of seconds, so that's… that's… something that we would sidestep with the set, I guess.
Michele Mancioppi 00:58:32 Plus, there is a bunch of funny bugs in the CAdvisor about the memory used by NithContainers.
Right, Busty? You remember it?
Bastian Krol 00:58:41 That, that, that as well, yes.
Yep.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:58:47 So even the CP-R is too much memory for certain people?
Bastian Krol 00:58:53 No, it's not… it's weird. CP minus R takes CPU, and if you only give, like, 100M CPU to the pod, then… this copying, takes… and… Yeah, it takes time. The memory, the memory usage is basically, the size of the init container image. So, because everything is… during the copy, everything is in memory once, and then, for some reason, this stays around as in the metrics, as used memory forever for the duration of the But there are very weird.
Things at play there.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:59:32 Oh, okay.
Michele Mancioppi 00:59:33 It's great fun.
I mean, of course, we do not expect CAdvisor To deal well with image volumes.
But it's more like… Let's see what new funny bugs come up.
Bastian Krol 00:59:48 It was…
Michele Mancioppi 00:59:54 So anyhow, who of you gentlemen will be in Belgium?
For the Hotel Unplugged.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:02 I can't make it, unfortunately, this time.
I sort of regret that decision, but…
Michele Mancioppi 01:00:09 Because we need to gang on the SDKs.
Woof.
PL Pavol Loffay 01:00:12 Please do.
Michele Mancioppi 01:00:14 What do you mean? You're not coming, Pavlov?
PL Pavol Loffay 01:00:18 I'm not coming, I can send you some help, but…
Michele Mancioppi 01:00:22 It's ganging of two. One is me, the other is Basil, and what is this?
Bastian Krol 01:00:27 That would not be very impressive, I'm afraid.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:31 I think Jack, Jack is gonna be there?
Bastian Krol 01:00:33 Oh, really?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:00:34 Yeah, Dragon Burke is fine, yeah.
Bastian Krol 01:00:36 Okay.
Michele Mancioppi 01:00:38 I mean, we're gonna give it our best shot, but as an anger mob, it's not gonna be very large.
Bastian Krol 01:00:43 Wow, if he, if you corner each…
Michele Mancioppi 01:00:46 FDK maintainer, 3 to 1 in an isolated… You know how many things we have? Yeah.
Bastian Krol 01:00:59 Okay.
Yeah, we are at time, actually. Unless anyone of you has something very urgent or important.
PL Pavol Loffay 01:01:11 Now, thank you very much for the discussion.
Bastian Krol 01:01:14 Yeah, you're very welcome.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:17 Thanks for coming.
Bastian Krol 01:01:18 Yep, exactly.
Good, okay, see you around, folks!
Michele Mancioppi 01:01:24 Yeah, folks.
PL Pavol Loffay 01:01:25 Bye.
Bastian Krol 01:01:27 Alright.
