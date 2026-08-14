SIG: Injector SIG
Date: 2026-08-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Michele Mancioppi (Dash0 Inc.)** 00:19 Hi, Jack.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 00:23 Hey, Michele. Hey, Jacob.
**Michele Mancioppi (Dash0 Inc.)** 00:28 Jack, do you want to work with me on defining in a Notep what it takes for a language to be automatically injectable?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 00:41 I can… I can… I can review it. I'd like… what do you… OTEPs are… OTEPS, as just Jacob knows, can be a… It'd be a big rabbit hole.
**Michele Mancioppi (Dash0 Inc.)** 00:54 That's why I don't want… I don't want to be left alone with that.
And everybody else is playing a game of chicken with me.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:02 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 01:02 I'm there, you know, holding the bag, and I'm like, man…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 01:07 What's up?
I think it's… it's ambiguous, when an OTEP is required.
I only write them when I absolutely have to.
And, you know, you might be able to get away with just an issue in a PR to the spec, which I think, like, eliminates a whole stage of the process, because it's like, even after you land the OTEP, you gotta follow up and open, basically, an equivalent PR to the spec, where people get to debate the whole idea over again.
**Michele Mancioppi (Dash0 Inc.)** 01:38 Excellent.
**jacob** 01:40 Yeah, I… I agree. I think that… were you to do this, I would just PR against the spec, and get some of the, like, language maintainers that you're already you know, have sort of allied on this idea to, you know, give you support on it, and I think that that's, like, a much better path than trying to do the OCEP route. The OCEP route, I think, was useful for You know, Injector and packaging in, like, these larger… initiatives, but I think that, you know, both… I think they're trying to centralize on the requirements for injectable languages, feels like things that are covered within the work that people have already agreed upon. And so I don't know if… I don't know if it's required to, like, go through a larger governance process for that.
**Michele Mancioppi (Dash0 Inc.)** 02:27 Okay.
**jacob** 02:29 And certainly, I would support and review the PR that you would write here.
So… Yeah, that does.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 02:36 That's always a good thing to do, is to, like, go get a group of people that you know are interested in reviewing it before you open it.
And, yeah, so you can quickly get that feedback and iterate on it, and, you know, within a short period of time, get somewhere from, like, 3 to 6 approvals, some combination of green checkboxes and gray checkboxes.
that leaves it in a really good spot, and I think bodes well for its chances of getting merged.
**Michele Mancioppi (Dash0 Inc.)** 03:05 Then, our plan. Thank you.
I don't know when I will do it, but I promised I would, so…
**Bastian Krol** 03:19 Do what? Sorry for being late.
**Michele Mancioppi (Dash0 Inc.)** 03:22 I went in the maintainer, so the, the maintainer, call. There was, there had been talk about, SIGs and projects giving updates.
And, the one last week, like, this week, on Tuesday, nobody was ready with an update, and packaging was on the list, so I went and told packaging, yeah?
And I also mentioned that all the dependencies we need to have on upstream languages and the requirements for what it takes for a language to be automatically injectable.
And, that is something that needs to be codified.
To be explained. So it's not the technical capabilities of the software, but also the software delivery process around it, because if you do what the Python SIG just did, then you break shit, yeah?
Okay.
It's gonna be fun.
So, in this case, it's a PR on the specs, yes.
What would they do? A new document, or… Where would I put it?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 04:36 Yeah, let's… let's go… let's go look at the spec and see if there's any natural place right now, or if it's, like, a new document that's referenced.
So, and just… just to be a bit pedantic, you know, there… there's an issue before the spec PR, and that's technically the process, but…
**Michele Mancioppi (Dash0 Inc.)** 04:58 I am very easily going to create one, like, define the criteria for automatically injectable languages to be used with the Injector operator Anglo.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 05:08 Yeah, right.
There's, library guidelines, that sort of lays out the… A variety of things.
That are sort of adjacent, maybe cousins to this type of requirement.
you know, it talks about how the API must be decoupled from the implementation.
It talks about performance testing, it talks about… you know, how to name your libraries and things like that, so this could be a section or a paragraph in here, at least as a starting point. I think it depends on how complex the requirements get. I think, like, less is more with specification.
You know, you don't want to use overly verbose or… flowery language, just state the requirements plain and simply. And, you know, I guess, what are the requirements in your head?
for… like, if you could sketch them out in, you know, I don't know, 5 bullet points or less, what would they be?
**Michele Mancioppi (Dash0 Inc.)** 06:30 Very simple. The, your language is injectable the moment that you can add instrumentations.
By the virtue of having files in a location where the process that needs to host instrumentation has read access to.
you can activate the SDK and the instrumentation.
Through, environment manipulation.
You can package instrumentations and, and SDKs in a way that this entire process works.
You have a mechanism to gate the activation of the injection, or at least the activation of the SDK and the instrumentation.
On some version compatibility check.
For example, what we do with the site customize, what we do in the Injector by checking the version of .NET.
And,
**Jack Berg (Raintank, Inc. – Grafana Labs)** 07:28 Is that the version of the runtime that the application is running, the version of the instrumentation, or the combination of both?
**Michele Mancioppi (Dash0 Inc.)** 07:35 Could be a combination of both.
Mostly, what we do is, checking the… since the… when you think of the collector and the system packages, the versions of the instrumentations are fixed.
And the variability is in the runtime that needs injection. So, we effectively codifying the configurations of the injector which runtimes it can inject.
If… That doesn't necessarily work, for example, in the operator, when you can pick any version of the instrumentation, then that needs to be configurable, which is why, for example, in the injector now, there is a configuration that you can put in a file with which versions of .NET do you accept to inject.
Yep.
Gabriel?
**Diego Hurtado** 08:20 Okay, so I'm not sure if I understand, but if we are trying to make a list of languages that can be injected, considering the fact that There's a finite amount of… a small, infinite amount of languages? Can we just… just make that list and arbitrarily say this, this, this, and that?
**Michele Mancioppi (Dash0 Inc.)** 08:42 Well, technically, nobody says that SDKs will stay injected.
Yeah, it's very easy for an SDK to break this contract.
**Diego Hurtado** 08:54 Okay, so… What do you make? Yeah, yeah, I see what you mean. You're…
**Michele Mancioppi (Dash0 Inc.)** 08:59 And also the other way around, I mean, Erlang is injectable. In principle, you can do that.
The SDK cannot do it, and the Injector cannot do it. Same is for PHP. Some versions of it.
Technically, most of them that anybody cares about, depending on how you write the instrumentations.
are technically injectable. In reality, the way we write instrumentations in the PHP SIG, only PHP8+, Can be automatically injected.
But, for example, at Instana, we had automatic injection PHP 4 and above.
It was a different technology to build instrumentations, but it was feasible.
**Diego Hurtado** 09:40 How far do we want to go with this as requirements go? For example, Do… do you think, we want to… Actually write down in the spec with a must, like, languages must, Designed this architecture.
When they design, follow this architecture when they design their instrumentation mechanism, so that they can be injected.
**Michele Mancioppi (Dash0 Inc.)** 10:06 I think we need to stick to the… so there are two aspects. One are the technical requirements that I was talking about right now.
And the second one is the software development lifecycle.
And, the way to retire and add new instrumentations, because those come together.
They, they kind of belong together.
**Diego Hurtado** 10:28 Yeah, I'm asking this one.
**Michele Mancioppi (Dash0 Inc.)** 10:29 The ones are not going to be controversial, the sort of development life cycle is, so I would rather keep that part in the, stable by design, initiative.
**Diego Hurtado** 10:43 Right. The… I'm asking this because, as far as I know, there is no… disadvantages in following this design, and there is at least one advantage. The fact that it can be injected, right? So…
**Michele Mancioppi (Dash0 Inc.)** 10:58 there are complications. It is much more complicated for language maintainers to keep in mind what you need to do and what you must not do.
When you automatically inject, as opposed to when you have a package manager resolve conflicts for you.
Which is precisely what happened with Python.
Nope.
**Diego Hurtado** 11:19 Yeah, but who cares about maintainers, right? We care about it.
**Michele Mancioppi (Dash0 Inc.)** 11:24 I care about the users, but Martinas need to have a reference guide, because, like, the amount of people that can explain from the top of their heads of how the LD preload injection works.
Most of them are probably in this Zoom call.
**Diego Hurtado** 11:41 Totally. No, I'm just kidding, you know, I love maintainers, by the way.
**Bastian Krol** 11:46 Yeah, so it sounds like the best we can really require there is to say, if you want to be out-injectable, then you need to follow that, and I don't think we can demand that from every SDK out there. Would be nice, but I think it's probably a bit of an overreach.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 12:05 I mean, totally. I think what we talked about in the spec meeting the other day is, you know, you define these requirements. These requirements reflect what, you know, the injector and packaging and operator groups know about what is, you know, what works, and then you put this as an entry in the spec compliance matrix.
So, you know, not every language will embody these, but, you know, if you want to play nice and want to have better reach, you know, for your instrumentation, this is how you do it.
I added another entry on there that I… maybe you were getting to, Michele, but it's about, like, and I don't know the best way to phrase this, I'm just being simple, but it's like, you know, the instrumentation, the auto instrumentation, needs to go to great lengths to not break the application. So, like, to short-circuit rather than break it.
And this goes, like, this touches on, like, how it structures its dependencies. You know, there's, like, the toxic dependency thing, with, with Protobuff.
But I think there's, like, other strategies to, like, get around that. Like, so in Java, there's this shadowing thing. So, you know, if we have dependencies that conflict with what the application requires, which we have tons of, we shadow those, those.
**Michele Mancioppi (Dash0 Inc.)** 13:18 In reality, you wouldn't even need to, because you have class loading domains in Java. So the extent of the depravities that you need to go to to prevent breaking applications, they go hand in hand with the lack of guardrails in the runtime itself.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:32 Okay, so class loading domains essentially shadows it. That's, like, a different technique to accomplish the same thing, so you can have multiple.
**Michele Mancioppi (Dash0 Inc.)** 13:39 Send me the code.
I think about it, in Node, you can, for example, a node or SDK can import its own version of a dependence, and nobody dies.
If you do that in Python, we know what happens. If you do that in Ruby, you know what happens.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 13:56 Yeah.
**Michele Mancioppi (Dash0 Inc.)** 13:57 So, some languages are much more… Hardened against potential conflict independencies.
than others.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 14:06 Right.
**Michele Mancioppi (Dash0 Inc.)** 14:07 is…
**Diego Hurtado** 14:08 Sorry, Michele, when you say some languages, do you mean, like, only Node? Because as far as I know, Node is the only one that's smart.
**Michele Mancioppi (Dash0 Inc.)** 14:14 Java?
Java, like, you really need to try hard to go and break somebody with a dependency that a Java agent will bring in. Like, you need to work, right?
Node is okay, it's not the best. Java is the best. NET is a close second, because the CLR is a very good runtime from that perspective.
The only problem that this ZRA has at the runtime is that you need to use the profiler interface, which is not production profiling, but that is what it was meant for, and you can have only one of them at a time. So you either have .NET tracing with OpenTelemetry, or Aqua security doing strange shit.
the,
**Diego Hurtado** 14:54 Oh, indeed.
Sorry, Jack, keep me honest here, but… Do you folks in Java, also implemented protobuf by yourselves to avoid a protobuf dependency conflict?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:08 Yeah, but we technically wouldn't have to do that, because in the Java agent.
**Diego Hurtado** 15:13 Nice.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 15:14 the Java agent can structure its dependencies to, for it not to be a problem, but it still is a toxic dependency if you're just using the SDK by itself. And so, you know, the benefits of us hand-rolling it were threefold.
We get rid of the toxic dependency for when you're just using the SDK, no agent. We shrink the agent by about a full megabyte, because the protobuf dependency is huge, and we can be… have much better performance than the protobuf serializer has. So, those are the reasons.
Once we hand-rolled it.
**Bastian Krol** 15:46 The second point is that because then you will get a conflict at build time, but not at runtime, is that what it is?
**Michele Mancioppi (Dash0 Inc.)** 15:55 No, it's because…
**Bastian Krol** 15:56 Is that when you use the SDK directly, but not the agent, is that then a build-time conflict, or…
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:03 Yeah.
Yeah, yeah, exactly. And I don't know what the breakdown is.
**Michele Mancioppi (Dash0 Inc.)** 16:08 Java?
Technically, in Java, it is a runtime conflict, even in that case.
Because you can, depending on how you do your Maven stuff, you can end up with multiple versions of the same jar file, and then it breaks at runtime.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 16:26 There's a lot of different ways it could break, but we just sidestepped the whole issue by not having that dependency. It's a general rule, as you get lower in the stack as a library, you want to have fewer and fewer dependencies, ideally zero, so…
**Michele Mancioppi (Dash0 Inc.)** 16:40 Yeah, that's… Bastian I have a history about this, because I have been saying that forever. It was like, no, no, you don't need to! No, you suppose you are supposed to import packages for… it's even. It's odd.
**Bastian Krol** 16:53 No, no, no.
**Michele Mancioppi (Dash0 Inc.)** 16:54 We go back on that topic, Bastian?
**Bastian Krol** 16:55 Yeah, yeah. I would have phrased it differently, like, writing everything dependency-free in every runtime and every language there is. Yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:04 Yeah.
Well, if we were .NET… if Java were .NET, then it would have good tools for a lot of these things built into the runtime, and we would be able to take even fewer dependencies.
**Michele Mancioppi (Dash0 Inc.)** 17:19 Yeah, for example, if Java had an HTTP client built in worth a goddamn, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:24 And if it was built in from Java 8+, you know, the version that everybody pins to. The version that's any good, or that is at least, you know… passable only comes in Java 11.
**Michele Mancioppi (Dash0 Inc.)** 17:37 I thought that the built-in HTTP client was Java 17.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 17:40 Java 11.
**Bastian Krol** 17:42 But speaking of versions, I think that is a good point. I'm not sure if that is on the list already. Is that, like, a requirement for injectable languages to auto-detect the runtime version and stand down safely, or is that…
**Michele Mancioppi (Dash0 Inc.)** 17:57 We're not too long.
**Bastian Krol** 17:58 Berlin.
**Michele Mancioppi (Dash0 Inc.)** 18:00 You must get a requirement. The reason why I did not add support for PHP in the Injector and the packages is because I've not found a way.
that is reliable to check which version of PHP is running before injecting it.
I mean, we should not… injection is dark magic. You should not break shit. People get very upset. And the loss of trust and the heat, reputation heat, that Operator gets is mess.
So, we better be very, very safe than any little bit of sorry.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 18:38 Here's an optional requirement that we could add, which is, like, you know, this could solve some of the other things that we've been talking about for a while, which is, like.
We could add a requirement that if you want… if you want to say that your language supports injection, then the maintainers of that language are on the hook for, for maintaining smoke tests, or whatever test surface area exists.
In packaging or in the injector that verifies these flows. So you don't get to just shovel the problem over the fence to somebody else.
You know, because the idea is, like, we're creating a row in the spec compliance matrix, and it helps us communicate our requirements, and it acts as an incentive, because whenever there's a checkbox, people want to check it, right? So, like, you know, if you can get more of what you want.
You know, from a maintenance standpoint, in order to have that box checked that it works in your favor.
**Nikola Grcevski** 19:37 I had a question about… you said, Jack, you're gonna work on, or somebody's working on, maybe, not you, on… changing the Java SDK, the one, not the agent.
to not actually be… bringing dependencies in? Are you just gonna… Try to rewrite the… during the Maven build.
To have it all… Namespaced for each… Java dependency? Is that what the plan is? No.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:06 I might be misunderstanding you, but I think I was just talking in general about the… this… a long time ago, the Java SDK had a dependency on Java protobuf.
**Nikola Grcevski** 20:15 Yeah, yeah.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:16 We severed that, so we have no dependency, and as a rule for ourselves, we try to keep all of our components dependency-free. And we only have dependencies in a few narrow cases where it's, like, impractical to hand-roll the thing. Like, we don't have a YAML parser. We have a dependency on a YAML library.
**Nikola Grcevski** 20:36 But in Java, Java, this is easy, like, all you gotta do is just, namespace your… during the Maven build phase, the last part, any dependence you have, you can just… rewrite their names. Right. And actually, they'll never conflict with anything, because they'll be under OpenTelemetry I.O, and… So Java at least has tooling for this. I wish other languages did.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 20:58 Yeah.
And, you know, the trade-off there is, like.
You're, if the dependency is large, then, you know.
**Nikola Grcevski** 21:06 Yeah, you're duplicating code.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:08 you duplicate the code, and you're also on the hook for, I guess more on the hook, I think, for any CBEs that might happen on that dependent library, because it's bundled directly.
**Nikola Grcevski** 21:19 True, yeah.
**Michele Mancioppi (Dash0 Inc.)** 21:21 So, I've been keeping notes in the issue.
activation mechanisms, the, the compatibility with SDK instrumentation runtime, so be able to stand down safely.
Dependencies, decorative config support, and I think there was another one we discussed, right?
**Jack Berg (Raintank, Inc. – Grafana Labs)** 21:42 I mentioned maintenance, if… but that's, like, that's, like, optional.
So, commitment to maintain, any smoke tests that verify that these work as intended.
I think you mentioned early… Something about packaging, so… You were… when I initially asked the question, like, hey, what are these requirements? You started speaking, and you were saying something to the effect of… I was taking notes in the meeting notes document, but something to the effect of, like, you can package the instrumentation in a way that facilitates this injection. Yes. I don't know exactly what you meant by that.
**Michele Mancioppi (Dash0 Inc.)** 22:31 By that I meant, the, When you… it's difficult to put in words, but when you look, for example, at the opportunity of agent, it comes in with a jar file.
That's… you put it anywhere, it works. If you want, to, to put, dependencies for Node that will work.
You technically can go and do strange stuff with the node modules environment variable, but ideally, you put it in a .node modules location on the file system.
And there are similar rules for different languages out there. If you want to do something in Python, you need to package… to put it in a certain way, so the site format.
And then manipulate the Python path variable. So, the way that you get the different binaries that are part of the instrumentation needs to be deliverable in a suitable layout, cross-system layout, I want to say.
And that is not always trivial to understand. For example, when you look at .NET, due to the… dependencies that .NET has on the libc flavor of the host.
You need to put in different locations.
the, one of the DLL libraries for Nulib C, as opposed to, Masso.
So that also needs to be clarified, that, you know, you should have a way, like, if your instrumentation depends on different versions of libc, then have a way to differentiate it, and be able to preferentially load one with respect to the other.
This is roughly what I meant.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:22 Yeah, so I just need to find the words to express that.
**Michele Mancioppi (Dash0 Inc.)** 24:26 Yup.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:27 In normative language.
**Michele Mancioppi (Dash0 Inc.)** 24:29 Exactly, which is going to be pretty difficult.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 24:32 Less is more.
**Bastian Krol** 24:34 Would that… would that what you just discussed, would that also entail, like, I think it would be good to have a requirement, like, the language SIG needs to somehow bundle up the artifacts that we need. So, for example, what we did with the Python distribution.
without that, without the Python distribution, we would have, in the injector or in the packaging, have to list all the instrumentations individually.
And I think that's not a good contract, because that is… I mean, we've discussed that topic a couple of times before, that is something that should come out of the language SIG, not only the SDK, but all the… all the instrumentations, all the artifacts that you actually need to inject, and that should be Ideally, a handful of artifacts at most, or one.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 25:27 Yeah, like, whether it's bundled into some sort of zip directory or something, like, the output for packaging is, like, you know, one file, or maybe one per version of libc, something to that effect. And it's like, what you're trying to express is that the language SIG is responsible for the curation exercise of, like, what gets bundled up into this artifact.
**Bastian Krol** 25:51 I mean, in .NET, we all… yeah, I think that would be a good point. I mean, in .NET, we have a couple of different files, but at least they come from a single artifact, or from, like, two perlibsy, so that's… that's… already good state, and even if you have to break it up and then load from different paths, that is okay, but having, like.
an ever-changing list of files that we need to keep track of, that's not good.
**Michele Mancioppi (Dash0 Inc.)** 26:18 No.
I mean, ideally, the, the old, going to put it in other words.
All the language-specific artifacts should be release artifacts of the upstream language SIG.
**Bastian Krol** 26:35 That doesn't quite cut it, that would still allow the language SIG to release everything individually, like, a lot of tiny bits individually.
That's what I want to avoid.
**Michele Mancioppi (Dash0 Inc.)** 26:47 That wouldn't bother me too much, as long as there are instructions of how to package it.
But, like, if there are glaring gaps, like.
Python does not really have good facilities for site customize, so if you go and injecting Python 2.7, it will blow up in as many readings.
That's a functional gap, huh?
**Bastian Krol** 27:09 Sure, two different things, I think.
**Michele Mancioppi (Dash0 Inc.)** 27:13 Yep.
I'll try to… To write this album, it's gonna take a bit before it gets into decent shape.
Yeah, I'm happy that, But I see there are people that want to collaborate, because I was getting scared of, Of opening that, that kind of worms, but it's, it's necessary.
To make automatic instrumentation, automatic interaction, first-class citizen in Auto.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:40 Yeah, and I…
**Bastian Krol** 27:40 It will be hard to get it right. Sorry, go ahead.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 27:43 people will be pretty accepting of this as a PR instead of an OTEP, if, like, if the scope is narrow enough. Like, if you put a wall of text up there with a thousand words, people are going to be like, open an OTEP.
But if this is, like, a section within a document that has, like, a couple of paragraphs and a couple of bullet points, then it sort of, like, passes the sniff test for what works as a PR, and then your burden as the author goes way down.
**Michele Mancioppi (Dash0 Inc.)** 28:11 Yeah, I cannot promise that it will work, but I'll try. This stuff is not easy. When you go and look at the project document for automatic injection, just to explain the basics of what we wanted to do.
I mean, nobody ever told me that I can write terse content, but it was complex.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 28:28 Yeah, well, you just, like, you just don't have to state everything. You just have to, like, you want to, like, establish, like, a foothold, like, a place in the spec where we can talk about this content, and you want to talk about the basics, and if it's not precise enough, then you can elaborate on it later. But the first step is to, like, have a place where these requirements are discussed.
It's easier to, like, land and expand than it is to, like, you know, start with your initial PR being, like, everything you would ever need to know.
**Michele Mancioppi (Dash0 Inc.)** 28:58 Yeah, that's a good term.
It's a good thing.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:01 Yep.
**Michele Mancioppi (Dash0 Inc.)** 29:06 Did anybody hear from Antoine the new reason why we cannot build an S10TX?
This week?
**Bastian Krol** 29:13 No.
Not closely following that story.
**Michele Mancioppi (Dash0 Inc.)** 29:20 Huh.
**Jack Berg (Raintank, Inc. – Grafana Labs)** 29:23 Alright, well, we're at time. I gotta run to the next Java SIG, so… take care, everyone.
**Michele Mancioppi (Dash0 Inc.)** 29:28 Bye.
**Bastian Krol** 29:28 Bye-bye.
