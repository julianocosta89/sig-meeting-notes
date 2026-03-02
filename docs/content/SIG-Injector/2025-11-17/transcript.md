SIG: SIG Injector
Date: 2025-11-17
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**atoulme** 00:20 Hello.
**Bastian Krol** 00:21 Low…
**Rafael Roquetto** 00:23 Hey, guys.
**atoulme** 00:23 How are you?
**Bastian Krol** 00:25 Hey, hey.
How was KoopCon?
**atoulme** 00:33 I… I can hear you.
**Bastian Krol** 00:36 You can't hear me, on my side.
**Rafael Roquetto** 00:39 I, I can't, I can't hear you.
**Bastian Krol** 00:41 You can hear me, okay.
**atoulme** 00:42 Amy.
Hang on, my edger must be messed up.
Yeah, mate.
My speaker's my microphone. How's that now?
**Bastian Krol** 00:52 We can't hear you.
**atoulme** 00:53 Yeah. Can you eat yours?
Yes, I can hear you. Okay.
Sorry.
**Bastian Krol** 00:59 As I said, how was KubeCon?
And your talk.
**atoulme** 01:04 Well, it went okay, I think. And Michele actually was…
running the interesting part of it with the BPS stuff, and, sorry, with Zigg and…
**Bastian Krol** 01:13 What? Did you say EVPF?
**atoulme** 01:16 Yeah, I got confused for a sec, with Zig and all the interesting parts around that, so…
**Bastian Krol** 01:22 Hmm.
**atoulme** 01:22 That one, okay, I…
Think people were receptive to the message of the injector being an easy solution to install stuff.
**Bastian Krol** 01:31 It ties well with some of the things that are being discussed right now at the GC level. Again, like, some…
**atoulme** 01:37 some of the interest that we're seeing from, from others, like Ted, who showed up in this, SIG meeting a couple times.
**Bastian Krol** 01:43 So…
**atoulme** 01:45 Yeah, well, good adoption, good discussions,
I… it helped me, because it kind of forced back on me to kind of do some work on the injector, so you've probably seen the… you've seen.
**Bastian Krol** 01:57 Oh yeah, flurry of PRs.
**atoulme** 02:00 Yeah, I think that was very good of me to be able to kind of spend time on that. It really felt liberating in a way, because I haven't had time to do it for a while.
**Bastian Krol** 02:09 but nice.
**atoulme** 02:10 So we had a release out, which is great, and there were some fixes for… was it .NET?
No, it was for Node.js, so we need to do the… the next step is to do yet another release, and maybe we could agree on some, like, even if it's still, like…
Not really serious, we should probably agree on having some release cadence.
even though it's, like, super simple right now, we can automate it more, too, because it's, the first feedback I got, like, from my first release, I opened some issues. It's not… it's not super well done. Like, right now, it's very, like.
Trust me, I'm going to upload some binaries from my laptop.
From what I'm doing.
**Bastian Krol** 02:52 Okay.
Yeah, so you're saying the release process is… has a few rough edges?
to say, yeah, okay, that's fine, that's fair.
**atoulme** 03:03 And I think this is to be expected, right? We're early.
**Bastian Krol** 03:06 Yup.
**atoulme** 03:07 there is an open issue for that. Automate the release step 115.
**Bastian Krol** 03:11 Hmm.
**atoulme** 03:12 like…
So… but overall, like, besides the fact that, so it's interesting, because adding those tests at the very end kind of helps, in a sense, like, make sure certified things work.
So the Node.js things would work all the way, except the final RPMD package was not, like, was missing one install of the actual module, so that shows that having this type of test is still worth the trouble.
The next step would be to add, so, discussing release feedback…
I have an open PR that doesn't pass. I'm bumping my head against the wall, on adding both ARM and AMD64 tests.
That's a good start, and then we should also do Alpine versus Libsy, just because.
But,
right now, I'm having a hard time with it, just because the testing frameworks themselves don't work, or, I'm trying to remember. I think for, our, yeah, for ARM64, the .NET image is slightly different.
And so you end up having to do a lot more work.
on .NET to make it so that you can build it for that, and I think I'm… I'm hitting a wall.
**Bastian Krol** 04:33 Yeah.
**atoulme** 04:34 I'll continue to work on that, or I'll just opt out, I mean, the thing is also, like.NET and ARM is kind of less mature as an ecosystem, people don't do that as much.
Yeah. So start with Java and Node.js first, then.
**Bastian Krol** 04:48 I mean, in the, the Zebra operator, the version of the injector that we have there has full support for .NET by now,
Based on the init container, or the instrumentation image that we built there, and that takes care of downloading the right binaries and putting it in the right
place, so maybe we can… we can also wait with .NET for… for when I get back to…
Getting that latest "-euro-specific codes, Shipments drop, over into the…
Into our repository, and then maybe it gets easier.
But if it's about packaging…
DEP or RPM package, that, of course, is not in there, so I'm not sure how much…
That will actually help.
Because we really only built the container image, for now.
**atoulme** 05:53 But we can see.
Yeah, I mean, I guess it's just discovery for the day… for the… for the…
**Bastian Krol** 06:02 Hmm.
**atoulme** 06:02 For the stake-of-state disc coverage, so it's not… it's not… I… just reviewing with you here quickly, just for you.
There's just a couple things that are, oh, shoot, come on.
This is this… this is this line?
So, maybe this… we could at least fix that one. I can probably make a separate PR just to make it so it's optional, because right now it's set as a constant.
**Bastian Krol** 06:31 Oh, no, that should definitely be, be something that is…
configurable. That is the main make file, and we only ever built… build…
**atoulme** 06:41 Well, I mean, yeah, so this is the type.
**Bastian Krol** 06:43 Interesting.
**atoulme** 06:44 Right? So it's cool.
**Bastian Krol** 06:45 Hell yeah.
**atoulme** 06:45 In a sense.
**Bastian Krol** 06:46 Yeah.
**atoulme** 06:47 And, maybe you could make it so it's a smaller step there. Anything else after that starts to become more nebulous, because it's more about the test files than anything else.
So, maybe I'll just, yeah, and then just debug stuff that I'm pretty desperate to get going. So what I'll do is, I'll just do a PR with just that, because that's super simple. But, after that, I'll stop, I guess, for now. Or keep this in draft, and we can rework it as we go.
**Bastian Krol** 07:15 Yep.
**atoulme** 07:15 So, okay.
**Bastian Krol** 07:18 Clue.
**atoulme** 07:19 Yeah, so, how the event went? It went well. I think we had a good showing. Again, Mikli had a good run. I have the slides up if anyone wants them.
**Bastian Krol** 07:33 Hmm, sure.
**atoulme** 07:34 Show them here.
**Bastian Krol** 07:35 Many people attended the talk, roughly speaking, do you know?
**atoulme** 07:40 So in between… It's… it's… so the room could contain about 300?
I would say about… 50 to 80?
**Bastian Krol** 07:50 Nice. I mean, it's a niche topic, so that's pretty cool.
**atoulme** 07:54 Yeah, it's just before lunch. We had a… we had a really good run. We got really lucky.
So… Right.
Yeah, I'm trying to find… I need to go look at further slides. They're in a different Google account.
Yeah, so…
**Bastian Krol** 08:11 Also, share them later via Slack, or whatever.
But I'm not.
**atoulme** 08:16 Yeah, yeah, any other questions, anything you'd like to know about how that went?
Oh, I'll tell you one thing, so…
for you, it's super important, Bestie, is that for CubeCon EU, there is an event the day before the conference starts called,
The maintainer summit?
Skip a meta event where people can come and kind of have discussions.
About the project, how it's run, like, it's more like, how do you run things, how do you make proposals, how do you… how do you work stuff, right? And so, that was probably… that would be a good use of your time, in my opinion, like, just to also get other maintainers,
And, yeah, I would really want to…
To come to that one, especially in Amsterdam, be easier for you. And .
**Bastian Krol** 09:10 Amsterdam this time, yeah, that might be nice. Yeah, I need to check with my company, because originally the plan was that we all go to Atlanta as well, and then plans changed, and budgets changed, so I need to…
Check on that, but, yeah.
**atoulme** 09:25 Yeah, I would say, like, just… yeah, of course, but, I mean, for what it's worth, the event is free for maintainers.
You just need to show that you're a maintainer. So…
**Bastian Krol** 09:35 Yep.
**atoulme** 09:36 Maybe worth the trouble, the only part is that it's on a Sunday, so it sucks.
**Bastian Krol** 09:43 Yeah.
**Ted Young** 09:46 Also, we'll be throwing,
at Fostum, the Monday after Fostum in February, we'll be throwing Hotel Unplugged, so if… if that's… Brussels isn't too far out of your way, would definitely love
to see some representation there from this SIG.
**atoulme** 10:06 Yes, let me put a link of that.
Attail, unplug.
And that one is also, like, super cheap. It was, like, 30 bucks a day, right?
**Ted Young** 10:15 Yeah, yeah, 30 euro to attend.
Yeah.
**Bastian Krol** 10:21 Yeah, I'll look into that.
**atoulme** 10:24 Yeah.
**Ted Young** 10:25 Kyle, have you gotten to introduce yourself yet?
**Rafael Roquetto** 10:29 Yeah.
Alright, so yeah, I work with Ted at Grafana Labs. I…
I'm one of the developers, behind the beta project, and now OOBI.
But yeah, Teddy told me all about the hotel injector, I got interested, so I thought I would show up and see what's going on. So, for now, I don't have anything to add but watch and learn, I guess.
**Bastian Krol** 10:55 Cool.
Welcome to the party!
**Ted Young** 10:57 Thank you.
**Rafael Roquetto** 10:58 Oh, and yeah, just for the record, I'm in Canada, so central Canada. I don't know which time zone you guys are, but I guess Europe?
**Bastian Krol** 11:09 I'm in Europe.
**atoulme** 11:11 Yeah. I mean, California.
**Rafael Roquetto** 11:13 Okay.
So it's also rarely for you.
**atoulme** 11:16 all over the place.
Actually, yes, that was a very good talk on OBI at KubeCon, so that's a new thing coming out, right? So it's a new BBF Auto-segmentation approach for using new probes through any software, right?
So… That was the first question in that talk, actually. I don't know if you were there for that.
They presented this technology for about 40 minutes. They explained how it's done. It's using, again, like a Java… sorry, an agent approach that is installed at some root level that does perform this type of transformations on your probes to capture the traffic out of
programs.
First question from the audience, how is this different from the injector?
And, I think the answer was, like, well, these are not really the same things, because the injector can install, like, the agents that are Java agent, Node.js agent, Python agent, what have you.
This is… this is running, like, similarly to a Java agent. It would be more competing, let's say, with a Java agent in a sense, even though it's not as fine-grained. Like, the Java agent is exactly what you would like to do, but this is nice because it works across any program.
So… maybe there's a story we need to have here about how we could install Obi
using the injector, and make it… makes that story really easy, right? So that you can… it's just another agent.
For all we care about.
Does that make sense, Rafael?
**Bastian Krol** 12:49 Is it so…
I mean, wouldn't… wouldn't you… I mean, isn't that something that sits between processes and workloads, and what we do with the injector, we inject into the actual JVMs, Node.js, runtimes, etc.
**atoulme** 13:11 Well, I mean, the injector installs a Java agent and makes it available so that any Java JVM can pick it up, right? And that thing is similar in the sense that you install something and then any process can pick it up. There's…
I'm not sure exactly what configuration you can do with Obi at this point, and how much you would like to set environment variables for Obi to pick up stuff.
But that's a discussion for the OB guys. Like, to me, it's like…
**Ted Young** 13:36 The injector is a great way to install host-wide.
**atoulme** 13:39 stuff, at this point, right? Maybe there's a community story where we need to continue having.
But those guys don't really have an installer today, so how do we install OB right now? It's like, we're getting here, do a bunch of stuff.
**Ted Young** 13:53 I mean, Nobi actually can install dynamically, right? So you don't even have to stop your… or restart your applications for that to get…
**atoulme** 14:01 any better.
**Ted Young** 14:02 So…
**atoulme** 14:03 Yes.
**Ted Young** 14:04 the main thing that we don't want to do with Obi is, like, because it's a different…
kind of instrumentation, if you were to start writing instrumentation on top of OB, it would be kind of like recreating this ecosystem that we've already created in code with the libraries that we're installing with the injector. So it's like…
we definitely, like, there is, like, some alternative universe where you just lean heavily on eBPF and, like, just do all your instrumentation that way, but we don't want to have two piles of instrumentation, right? Like, it's hard enough to maintain one pile of instrumentation.
So… but at the same time, Obi… with eBPF, you can get, like, networking information that's really interesting, so I think there is an interesting question for, like.
if you have both of them available, like, what do you do? Like, what is the advantage for when you install both of them? Or, like, how does one detect that the other one wants to be installed? I think there's some trickiness there we'll have to figure out.
**Rafael Roquetto** 15:12 This… I just wanted to add, yeah, I feel like… and again, I'm just…
arriving here, I don't have a lot of context, But…
I feel like they are complementary, like the injector and OBI, because the injector is going to give you, ultimately, the ability of injecting Java agents, or whatever that's a higher level, more fine-grained instrumentation, that eBPF can do. So, there are a lot of things that eBPF can do.
Like, you know, like, network metrics, or, you know.
Metrics are good. In general, service metrics, span metrics, whatever.
But once you start dreading to the…
trace context propagation, correlation, that kind of stuff, it gets trickier in EBPF, so we can do…
it will for Go and for some languages, but it's not a… like you guys said, it's not as fine-grained. Like, we're just discussing how to instrument
Java with SSL, right? You need some sort of…
Asian support there, because EVPF can't see that kind of semantics that are on the library level, and I think that's…
Where the injector becomes really interesting, because it enables people to, you know, for anything that eBPF can catch, or you want to be more fine-grained.
You know, then you have all these higher-level instrumentation that's much more context-aware than for your technology or framework or whatever than eBPF.
**Ted Young** 16:46 Yeah.
You also made the other great point where these things are complementary, is two languages that are important to us that we can't capture with the injector are Go and Rust.
**Bastian Krol** 16:59 Absolutely.
**Ted Young** 17:00 Go, at least, the eBPF story is actually getting really nice. Like, there's actually really nice interplay between manual context propagation and the stuff that OB automatically injects into Go. I know the Go community is very interested in some kind of, like, compile-based
solution, and that would be a more Go-ish way of doing stuff, but eBPF is looking very promising. It's actually… of the thing that's going on over there, that seems to be the most advanced, as far as having something like what we're doing with the injector, but for Go.
Like, like, it seems like, like, it's getting pretty robust. The edge cases are, are getting, like, pushed farther and farther away.
**atoulme** 17:45 Yep, I can see also C, C++ being good targets.
It would be kind of funny if we were able to tell you, hey, you just ran curl, and here's the span for your curl command.
But, yeah, so… my view is the injector is here to inject stuff and make sure that things get instrumented on your host.
However, we can instrument more stuff is great.
So, that sounds like, one more… one more way to do stuff, but,
I think we should be agnostic about how the agents work underneath. Right now, we have support for Java, Node.js Python.
We can add one more. This could be the EBPF, like, OB stuff, and it doesn't matter to us as much.
**Bastian Krol** 18:28 I, I think, I think,
we are not very accurate when we say that, so… maybe I'm… I'm… I don't know enough about OB to really evaluate that, but I mean…
with the current Injector project, it has basically two parts. One is a packaging that includes a Java agent, a Node.js agent, and the other one is the actual
injector Zik codebase that really, so far, only sets environment variables. It does nothing else. And that second part, I think, is kinda… is that something that OB would even need?
I think the part… if you say we could install one more agent, what we really mean is we could include it in our.
**Ted Young** 19:19 Yeah.
**Bastian Krol** 19:19 Debian packages and RPM packages, and set it up, but we wouldn't need to instrument any actual processes for that, then, to capture EVPF.
Stop.
**atoulme** 19:36 Yeah, you put me…
**Bastian Krol** 19:36 Is that understanding correct?
**Rafael Roquetto** 19:38 Yeah, kind of. So, the way…
the way Obia works is basically…
it does two things. First, it does discovery. So, it will see what's running on your machine, or in your cluster, and then it will apply… it was going to look at a set of rules.
whatever, to see, okay, should I instrument this process? Is it because this process is running, let's say, on port 5000, or because it has Kubernetes metadata that matches the service name? Yeah. And then, and then, based on these rules.
it picks up the process to instrument, and it does just that. Then it inserts the eBPF programs and starts.
**Bastian Krol** 20:21 So, I feel like…
**Rafael Roquetto** 20:24 And again, I'm coming from the other end, I have very little context from the injector project.
I feel like the only thing the injector could do, and I don't know if it's the role of the injector, and I'm not being rhetorical here, is…
deploy OB somewhere, like, just bundle it, and then it needs to… it would need to provide Obi with a configuration, and I don't know if that's the place of the injector to do that, because these configurations didn't get complex, and the injector, as far as I know, is… it's just really simple, right? The environment variables, there's this…
library, so… I don't know, for me, there is a… I still don't understand, there's this huge gap that…
how to connect both of them, they… my gut feelings, but again, I have no experience, would be to say they are still talking out to each other, and the injector coming on top with all the instrumentation, it could be OV-aware to the sense, like.
How do we reuse what Obi's producing, or do I… do I tell Obi not to instrument certain
Services or whatever.
**atoulme** 21:25 This is beautiful.
**Rafael Roquetto** 21:26 Because the injector is doing that, that's something.
**Bastian Krol** 21:30 That's right.
**Ted Young** 21:31 They don't need each other, just to clarify, right? Like, OB… like, EBPF doesn't need LD preload.
**Bastian Krol** 21:38 Exactly.
**Ted Young** 21:39 bootstrap itself and vice versa. That's why… that's why they work successfully in different environments, right? Is because they're… they're totally independent.
Linux mechanisms.
The question is just, yeah, like…
One, like, what does double instrumenting look like? Is it even safe? Like, I assume it's safe, it's just a fucking mess. You know? But I… we shouldn't necessarily assume that it's safe. So one is, like, what happens when you accidentally turn both these things on?
**Rafael Roquetto** 22:09 I can tell… I can tell you what happens. If OB… I mean, in theory, right? OB can pick up if a project is instrumented with OTEL SDK, or whatever, because it sees the OTEL traffic, like, metrics, and then it…
It does not double instrument, so it detects that, and then it ignores it.
**Ted Young** 22:30 Yes.
**atoulme** 22:31 Oh, that's great.
**Rafael Roquetto** 22:32 In theory, right? Right.
**Ted Young** 22:34 Depending on the… I would assume the way LD preload works is that detection mechanism would still work, right? Because we would have already…
chosen which headers to apply and everything by the time eBPF is running.
Because EBTF is dynamically attaching after…
**Bastian Krol** 22:51 Yeah, exactly. I mean, the injector really only works at Process Startup with the LWP load hook, and that's quite separate from everything that Obi is doing, but of course, it might be a good move, even if it's not super cohesive, to include Obi
In our packaging.
And if we only reuse that, maybe it's… Still a good move, technically.
**Ted Young** 23:17 Or the other way around, I mean, I know there's the… you know, there's one approach where we're just doing Linux package management, and, you know, the basic, like, Linux package management approach, where this just gets installed, and it's going to aggressively bind…
to just… you know, everything it finds, essentially.
But then there's, like, this other approach, which is the approach we've been taking with Ovi, which is, like, for end users who want to have more of a control plane where they're kind of first figuring out what's running, and then…
deciding…
what to instrument? It's a little bit weirder, it's… that's… it's one of those approaches. With Obi, that's more straightforward, because it can… eBPF can dynamically attach. That story makes a lot more sense than with LD preload, where it's like, cool, so we've decided to attach to these things once something
Triggers them to restart.
you know.
**atoulme** 24:20 Yeah.
**Bastian Krol** 24:21 That's where…
**Ted Young** 24:21 It gets a little, like…
Is that… is that… is… is there much value even in that approach? But… but we at least want it to be coherent.
You know, so… so having these things be coherent. But it could be just… it… it shakes out naturally. And also the, Rafael, the questions we have about, like, what should Obi do?
when the injector is running, might just evolve down to, like, what does Obi do when it detects that the SDK is running?
Right? Because it actually doesn't… shouldn't really matter if the injector stuck it there, or if the human did.
**Bastian Krol** 25:00 There's some situations where it's valuable to be running both.
**Ted Young** 25:04 Either because you don't have library-level instrumentation on, like, some valuable endpoints, for example, so you actually want eBPF-level networking instrumentation and, like, automatic, like.
trace… Kickoff.
Because there isn't a library, you know, instrumentation package giving you what you want. That's, like, a good example. And the other example would be, like…
you don't want double and triple instrumentation, but is there, like, low-level stuff you can get with eBPF to decorate those client spans?
That's hard to get out of the library level.
**Rafael Roquetto** 25:44 I, I, I think this, I mean…
This makes sense to me, and even before the injector project, like, this is something we've been discussing
a lot within the team, in the sense of, okay, there is this SDK, or even manually… well, manually instrumented, library instrumented, processes generating some sort of, open telemetry… telemetry,
what do we do with that? So do we double instrument? We don't, so we detect that, but maybe, like you said, maybe we… for instance, OB is able to inject a transparent and propagate transparent in a few cases, but what if
And this happens
the SDK already injected transparent, so we need to be able to detect that and not re-inject it again or generate a new one. So, I feel like this should fall on OB's side. I mean…
It's just a feeling, don't get me wrong, on… Okay.
these things are coming, like, just what I'm saying is SDK, like, higher level instrumentation takes precedence over Obi. Obi is able to see that, and now it just doesn't double instrument, but it could instead
Like you're saying, enrich that, whatever's being generated, and pass it forward, because, you know, it's seeing everything.
So, I feel that's how they would connect. And I can see a scenario, for instance, I had a meeting with some guy.
two weeks ago, their… part of their system is using Perl. And… and then Obi was really handy for detecting some stuff, because it was, like, a really simple system.
**atoulme** 27:19 We're good.
**Rafael Roquetto** 27:19 I don't know if you have an OTL library for Perl, like, you know, but it's just part of the system. Part of the RSI would be served with the SDK.
So…
**atoulme** 27:29 That's… that's funny.
Yeah, so, absolutely. So, I think, you know what I'm coming out of this discussion with, is that I think we should write something.
That exactly is the discussion we just had.
And it's very clear, because I'm worried that we may actually confuse our community with those different approaches, and we need to be very, like, good about, like, explaining how those two things play together really nicely, and some of the future roadmap items, so we can start to, kind of.
make sure, even if we don't actually have that much in common, or, like, we're orthogonal to some extent, let's make sure we coordinate that very publicly, because that's super nice for people to know how to do this, otherwise I'm fearing that people continue to ask questions like, where Injector will be? Like, what's… what's the… what's going on here?
And Bessie has a good point. Like, we do have, two parts to the injector right now. We are talking a lot about packaging, because making things easy requires good packaging, and then we have the actual mechanism.
And so, while OB would benefit from our packaging efforts, the mechanism in Zig is kind of orthogonal, like, not really applying to OB that much.
**Rafael Roquetto** 28:38 Yeah. So…
**atoulme** 28:39 Yeah, let's play that,
I don't know, we can… I can just open an issue for having a blog post about Obi and Injector, like, how we work together, and we could do that, to not have to come out, like, urgently, but I think it's actually a big, big item for us to do.
**Bastian Krol** 28:58 Yeah, I totally agree. I think from a user's perspective, it can really be confusing, because both this kind of low-level injection, automatic, zero-touch stuff, and if you are not living in that ecosystem, and you maybe don't know what EBPF is doing, whether it's LD preload, all these technical details, you really need some explainer on
What is what, and what are the strong suits, and how it differentiates.
**Ted Young** 29:27 Yeah.
Especially in the long run, you know, for the environments where we can make this work, I want these mechanisms to become the default way that people interact with OpenTelemetry. We always need to have, like, a good story for how you install OpenTelemetry by hand, right? But it's just…
you know, the more I get out there, the more obvious it is that
The application developers writing this code by hand and kind of doing it by hand are in the minority compared to the number of organizations who want someone more like an operator to manage all of this stuff, so…
Like, kind of getting that mindset out there into OpenTelemetry, like, blog posts like this help.
But I'm happy to see that these mechanisms don't really need to interact, right? That as long as OB concentrates on what it does when it detects an SDK being there, regardless of how it gets there, I'm happy to hear that. Because that's one of my worries, is that based on which
which injection or installation mechanism people are choosing, that they get some different menu of options, or… or telemet… you know, I don't like the idea of it becoming a complicated matrix.
**Rafael Roquetto** 30:46 Yeah.
**Ted Young** 30:47 You kind of want people to get the same data no matter which path they chose to install.
this stuff.
**atoulme** 30:55 Alright, well, I opened an issue on our end.
**Ted Young** 30:59 Great.
**atoulme** 31:00 And, yes.
I mean, it continues to be, baffling. We don't have a packaging SIG, so the injector's picking up the tab for packaging for now, and the moment someone else shows up, we're like, oh, how do we make packaging make sense?
So that comes out to be a fun one, but…
We should… we should maybe have one test that tests Obi and, or maybe even part of the OpenTeometry demo, that's another issue we could have, which is we take the injector for a spin with the Java service, and we take Obi for a spin next to it with some Go project, and we show that the traces can flow together nicely.
And I would really show, like, Better Together as a story, too.
Okay, I'll open an issue for that.
**Ted Young** 31:44 Yeah.
**Bastian Krol** 31:44 Sounds great. Yeah, sorry, folks, I need to drop early today.
**atoulme** 31:49 I know it's like…
**Bastian Krol** 31:51 just arrived, and it's getting cold, so… but, good discussion we had, and.
**Ted Young** 31:56 That's fine, I think that's enough for today. Congrats on the success at KubeCon.
Thanks.
**Bastian Krol** 32:03 Yeah, absolutely.
**atoulme** 32:05 Yeah, that's good. We need to build on that, I think, we'll see more.
**Rafael Roquetto** 32:10 Yeah, take me on the issue, and then, tomorrow I got a meeting, like, internal meeting with the OB slash builder team, and I'll bring it up with them as well.
So everyone is aligned.
**Ted Young** 32:22 Yeah.
**atoulme** 32:23 New, give me your GitHub ID real quick.
**Rafael Roquetto** 32:25 Oh, okay, I'll… we'll chat it on… I'll type it on the chat, where is the chat?
**atoulme** 32:31 Add a example… of integration.
Body and injector.
**Rafael Roquetto** 32:39 Here it is.
**atoulme** 32:41 Ventimentary demo.
**Rafael Roquetto** 32:44 That's it.
**atoulme** 32:47 I gotcha. Alright.
**Rafael Roquetto** 32:49 Bye.
**atoulme** 32:50 Well, nice meeting you.
**Ted Young** 32:51 Yep.
**Rafael Roquetto** 32:52 See you guys…
**Ted Young** 32:53 See ya.
**atoulme** 32:54 Cheers. Bye.
**Rafael Roquetto** 32:55 Bye.
