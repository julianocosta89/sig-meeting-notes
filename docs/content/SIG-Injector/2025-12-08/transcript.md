SIG: SIG Injector
Date: 2025-12-08
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

atoulme 00:01:22 Hello.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:28 Hey, Antoine. How are you?
atoulme 00:01:31 I'm good, how are you?
Alright, so you put your name down, that's great, thanks.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:01:39 Dude.
Bastian Krol 00:01:41 Hello!
atoulme 00:01:43 Hi, Busty.
Bastian Krol 00:01:46 Right?
atoulme 00:01:48 How you doing?
Bastian Krol 00:01:48 I… I'm fine, how are you?
atoulme 00:01:51 I'm cold, it's cold in California.
You believe that?
Bastian Krol 00:01:56 What happened?
atoulme 00:01:59 Well, I need to… I need to run the heater, and… And, you know what I'm gonna do? I'm just gonna go run some 3D prints, that'll help.
So anyway, yeah, not much. I had, looks like we skipped last week, We… the week before, we had a bit of a discussion, I think it's just me and Jack. We talked about some of the stuff that, you know, was important in terms of messaging.
But, yeah, anything we'd like to… Okay, so I see there's one item in the agenda. Let's be good about this. Just, if you have anything you want to talk about, let's put it in the agenda right now.
And then we can start with what Nicola has put up, so… Wanted to see…
Bastian Krol 00:02:50 No.
atoulme 00:02:51 we'd like to consider, so we have a PR app for Nicola, add an option to include or exclude certain programs based on executable path command line arguments.
Sure.
Okay, so this was opened by Jack… She reads you back then.
There's four…
Bastian Krol 00:03:19 I think there are two open PRs right now that we might want to…
atoulme 00:03:24 Okay.
Bastian Krol 00:03:25 Talk over… what was the other one?
Did not put anything in the agenda as of time.
Oh, okay, the other one is just upgrading the ZIG version, so that's nothing that… really… requires a lot of discussion, I guess.
Yeah.
the other one is a new feature that's certainly worth discussing. I mean, the upgrade to… the upgrade of the ZIG version, and anyway, the fact that people are now starting to contribute will make it a bit harder for me to upstream the changes that we did in the Dash Zero, injector, because that was like, half a rewrite, and now people make changes based on… on this code basis, but yeah, that's… I guess that's for me to figure out once I find the time to…
atoulme 00:04:21 Well, if you want us to wait a little bit, and you have some changes that you want to make first, just…
Bastian Krol 00:04:27 Yeah, I think there's no good way here, because people have already made these PRs, and if I now change the whole codebases, then the onus of merging or updating their PRs is on them, and…
atoulme 00:04:41 Yeah.
Bastian Krol 00:04:41 That's also not really fair, so…
atoulme 00:04:44 I guess.
Jack Berg 00:04:45 Somebody's gonna have to rebase.
Bastian Krol 00:04:48 Yeah, it's not just rebating, it's… yeah.
Jack Berg 00:04:51 Rewrite.
Bastian Krol 00:04:52 revised, no, I guess, it will be okay.
atoulme 00:04:57 You do it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:04:58 I don't mind redoing my work, so if… if I'm the blocker here, just… I'm happy to take that answer, like, wait a week or two until I do this work.
Bastian Krol 00:05:07 No, I don't think so. I think that… I think that's fine.
Okay. That should be okay. No, no, no, I… I think… so my stance on this, I think we should… not block any of these PRs, I'll just figure out how to merge the stuff, but I guess I should do that pretty soon.
So, we don't accrue many more changes.
atoulme 00:05:36 That's always the problem, right?
Bastian Krol 00:05:38 Yeah.
But that pretty soon part is also, like, not, like… 2 hours of work, it's a bit more, I guess, and I need to find time for that.
atoulme 00:05:49 No worries, I hear you.
Yep.
Okay, so…
Bastian Krol 00:05:55 Okay.
atoulme 00:05:57 Let's talk about that PR, right? So, we… maybe from the point of the requirements here, before we go into the code.
So, we want to talk about why this is important, and… is this really important that much? Like, so you want to… You want to be able to include and exclude things.
Which one… which one overrides the other? Is it the exclude path is going to override the include path?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:24 I can maybe explain, start from scratch, why did I even want to do this in the first place, right?
atoulme 00:06:29 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:06:30 So… I… I like the concept of having this deployed in ETC preload, so that it just gets automatically picked up for every program, that we don't have to actually go and specify command line arguments to… or environment variables to every application.
But… I was mostly concerned about the case where, there's other programs on the system running that you definitely don't want to instrument. And so, I worked in Elasticsearch before I worked through Grafana, so, I mean, we use Logstash to push logs.
atoulme 00:07:04 Right. And log stash is within Java, so…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:07:08 things like that. I don't want log stash metrics or traces or anything happening, because there'll just be extra volume of stuff that I have to pay for stuff that I may not want, actually.
At all.
So that's one example of things that you just don't want to see, and you're deploying, presumably random applications, using Elastics as a vendor. You never want to have your log stash logs or traces, anything shipped.
The other example that I had in mind is that There's people who write all sorts of security tooling, sometimes those things are written in Java, they love… load random agents.
prevent the OpenTelemetry agent from conflicting with some stuff that we know that doesn't work well with. So we say to people, oh, the Java agent is not supported if there's another agent loaded. It would be nice if we could actually detect that these agents are loaded, and users can write rules about the stuff that they want to exclude with.
So it doesn't pick random programs that are running on the system.
And the other thing is, like.
Some applications, depending how they're set up, may not survive instrumentation.
For example, I'm just thinking of… Like, in simple terms, it's like, a user has fine-tuned that they've picked, like, 4 megabytes of heap or something.
for their application, they, like, have some small utility. Now, imagine if we tried to throw in an agent on top of it, it may go beyond their heap, it silently goes out of memory, they're not sure why their tooling is actually not running on the system, right?
Maybe they have a periodic app that kicks in, does something, doesn't do anything else, you know?
So… We wanted to be able to have people specify some default configs for them that makes sense, say… Exclude these apps, don't… When you see an argument of single-digit M supplied on a command line, don't do it. When you see, you know, Java agent used already, don't do it. Or look for specific agents that I want to instrument that, and so on.
atoulme 00:09:22 Okay.
Bastian Krol 00:09:23 I agree, that's totally a must-have. So, I mean, we are only using the injector with Stashido so far in Kubernetes environments, so it's a little bit different, but I think, in general, this rule very much applies. If so.
if you have, basically, an injector somehow installed in an environment, be it a physical box or a Kubernetes cluster, and it is On by default, you need to have something to opt out of.
this, because there's… you always need an escape hatch, and if you install it on a VM system-wide, there needs to be some mechanism to say, yeah, I basically want to instrument everything that runs here, but there are known cases where I really need to opt out of it. That's, I think, a must-have feature.
So I'm… I'm… And… and doing that either by, by, executable name or by… by argument matching, I think it's a good strategy. And it's… and it's a known strategy in… Other vendors have done that before, other contexts.
It's auto-instrumentation.
Jack Berg 00:10:37 Yeah, I picked this up and ran this on a Linux box of mine, and, you know, I was surprised by, you know, there is some Java processes running that I wasn't aware of.
And, like, you know, there were weird things, right? So I was doing remote development from my machine onto this Linux machine using this IntelliJ tool. That's, like, an IDE, and they have, like, a remote development tool, and it's implemented in Java. And so, like, surprisingly, all of a sudden, my IDE was being instrumented by the Java agent. Like, that was unexpected, and I would like the ability to turn that off.
Bastian Krol 00:11:13 You could even… that's maybe further down the road, you could even think about maybe having a default exclude list, like, never, instrument, IntelliJ, or stuff like that. That's probably something you never want, and…
Jack Berg 00:11:28 defaults from us.
Bastian Krol 00:11:29 same defaults, but also, even if you… I mean, currently we are instrumenting JVMs, Node.js, and .NET, even for… but the injector is a very broad sword. It's not a scalpel, right? It just injects into every process on the system, so… Right now, I think it's… it's pretty safe to do that, but let's say we find some kind of executable where it would crash the executable and wouldn't even have any positive effect if it was… because it's not a JVM on a known Jeth runtime, then also for that, an escape patch.
Would be very good to have.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:08 Yeah, I was also thinking .NET, it's even scarier, because even PowerShell itself is implemented in .NET, right?
Bastian Krol 00:12:14 Oh, good point.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:15 you know on any PowerShell script, we'll actually probably pick it up and…
atoulme 00:12:20 people around. Maybe you want that, that's the…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:12:23 Yeah, maybe you do, yeah.
atoulme 00:12:24 Actually, maybe that's actually a feature of the thing. It's interesting because we're starting to target, like, interesting, maybe, use cases on the side, like security stuff, but… Yeah, so the argument that I think I could have made, months ago would have been that in some cases, you do want to get maybe more than you need because a collector can drop some stuff on the way to the backend.
And so… but I like your approach. I think it's neater anyway. I was going to apply towards what Besti said, is that we should have a default list, and you already, in your example, are giving a good idea of what defaults could look like. So if you would like to do that in subsequent PR… I think that'd be nice.
I'm not the best at Zeek, I can review and make sure it passes my, my, you know…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:13 man, I was just, like, it was hackathon week here at Grafana, so I was just like, let's learn Zig and try to do this, and I was struggling quite a bit, I haven't.
Bastian Krol 00:13:23 Oh, I hear you.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:27 But that's okay. You know.
Bastian Krol 00:13:30 The compiler error messages are quite horrible, and not helpful.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:34 Yeah, that's okay, you know, you make do what we can, and I was happy to actually have the opportunity to use Zigg and try to learn it, so that was quite cool.
Bastian Krol 00:13:43 Yeah, I like it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:13:44 It was a whole experience, so I have to say. So that was great.
atoulme 00:13:49 Awesome.
Bastian Krol 00:13:50 I think it's also very good to have a few more people who have actually touched the zip code, that's just, also, definitely, but, going back to one of Antoine's questions earlier, so there's include and exclude, and there I also would have the question how… what's the semantics, if you define both, or what… how does that work in detail?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:14:13 Yeah, so I opted out for the following things. So, I did two, kind of, design choices, and we can change them if you'd like, but I thought include should be… so I want to maybe include everything that starts in slash app. Let's say people deploy on VMs and preload stuff, and it's always in app.
And then you have the escape patch of exclude, Anything that has agent, and… I don't see a case where people use often both, but I said exclude should be higher priority than include. So you said you included something, but then you said, I definitely don't want to see this. It's more like, these things will hurt me, things that I definitely don't want to see.
So, it tries to match by the include, but then it says, yeah, but I also found an exclude rule about this. So in the debug logs, it would say.
I approved it, but also denied it later, so there's an allow and deny.
Bastian Krol 00:15:10 And if you don't set anything for include, by default, everything is included except for the excludes. Yeah, I think that makes sense. Sounds, sounds… Good, I think.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:22 Yeah, I said, I don't want to change the default, so anybody using the injector right now should not see any behavioral change. Like, whatever, right?
Bastian Krol 00:15:29 I'm not sure if anybody is really already using it, so that argument is, but…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:35 I mean, yeah, you never know, right? I mean, people are using it, and we definitely want to use it.
Bastian Krol 00:15:41 Yeah, yeah, sure.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:15:43 And so… and the other design choice I made was to… if you mention multiple includes, one after another, it's a union of that, because I thought, yeah, I can comma separate them and list them, but if I were to do this with an automated tools, something that people, you know, push, New Line is easier for those kind of tools to implement.
atoulme 00:16:07 So, rather than…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:16:09 figuring out where to put the comma, do I have a trailing comma, do I… did I prepend it? It's just, like, add multiple lines, but if I'm as a human typing it, probably easier for me to add commas and list everything I wanted.
So… you mentioned multiple lines, nothing overrides the previous. You just said, I want to include this, I want to include this, I want to include this, and then I want to exclude my… you know, dash… agent, Java agent, colon.
Bastian Krol 00:16:36 That's maybe one thing to, have in mind here, though, if we ever extend this config file format with various other things, and there are other, we stick to this key-value pair.
Format than this… This semantic might not make sense.
for every, configuration setting. Maybe there's something that you only specify once, and then you either have a different semantic there within the same config file format, or… yeah, I don't know, that's maybe something to think about in advance.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:19 I guess you're saying, like, include paths and then call in, and then you can do, like, in YAML dash something dash something dash something, kind of list them as a list, rather than… discussion.
Bastian Krol 00:17:28 I was not going to… I mean, for this, for includes, having multiple key-value pairs and they all get merged makes sense, but let's say there's down the road some complete.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:39 different.
Bastian Krol 00:17:40 configuration setting, with another key, where this merging makes no sense, and it's a little bit inconsistent how we treat key-value pairs based on the key, which is also okay, I guess.
Just…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:17:57 Yeah.
Bastian Krol 00:17:58 But I don't have a strong opinion about it, I think.
This merging sounds okay. I.
Jack Berg 00:18:06 I posted a link to, you know, another project I'm involved in is declarative configuration, so standardizing the configuration scheme for SDKs, and we have this type of concept that appears in a number of places where we need to do pattern matching to include or exclude something, and so the link that I post to is our data structure that we use to represent that recurring concept.
It's very similar to what Nikola has presented here, with, like, you know, an include, and an exclude that overrides the include, and.
Bastian Krol 00:18:37 You know?
Jack Berg 00:18:37 You know, both of them are lists, and, you know, they're unions, and I think one difference is that in declarative config, we've opted for glob matching, glob pattern matching, where a star matches any characters any number of times.
And a question mark matches any character exactly one time. And so, you know, it's just a little bit easier in the case of declarative config to do glob matching, because, regex is not standardized across languages.
So, you know, GLOB, we can at least have some sort of standard. So, I don't think that applies here, like, so I… did you go with…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:19:14 Yeah. Yeah, because I knew Oto, he likes them, so… Yeah. Forget about regex.
Bastian Krol 00:19:22 post that link?
Jack Berg 00:19:24 in the, the docs, the document, the notes document.
Bastian Krol 00:19:28 That's the one place that didn't… yeah, okay, same.
Oh, okay.
atoulme 00:19:33 He looks… okay, so I think… I'm good with merging this. It's better than before.
We can talk, I think, about the config file, maybe separately from this effort, and…
Jack Berg 00:19:43 Yeah, no, I was just, giving an example of prior art, like, because, you know, when you're discussing this stuff, it's always easy to, you know, question whether you're doing the thing most idiomatic or correct, and so it's good to have prior examples.
atoulme 00:19:57 That confirms it, right? So… We should be good.
okay.
I'll give you an approval on my end.
there's a need for me that, you have one line of change to the contributing MD that could be a separate PR, so just… this is me being a bit of,
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:20:19 Okay, sure. If you want, I can undo that. I saw, because I was reading your contributing guide to see what I should do, you know, and then I noticed that this one line was, like, kind of copy-paste duplicate, so I was like, might as well fix that, but sure.
Bastian Krol 00:20:34 Antoine, I have to say, you are super strict about factoring out these, like, type of fixes. I mean, to be honest, so from my perspective, they can stay all in that PR, maybe that's something that we need to align on at some point, but I find your position on that very strict.
atoulme 00:20:52 It is very strict. Yes, I know. I'm coming also from the point of view of that in larger repositories, like Contrib, I will be stricter about this for a couple reasons, because it's difficult to land an EPR, and there's a lot more conflicts.
And this doesn't matter, right? The other reason I do this in Contrib for Collector is because we tend to revert stuff, and I don't want to revert some…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:16 Mmm.
atoulme 00:21:17 traditional changes.
Bastian Krol 00:21:17 changes, yeah, yeah, that… In theory, that makes change. I don't think it has any practical application here, really, but yeah.
atoulme 00:21:27 Right.
Bastian Krol 00:21:27 Yeah, okay, I see where your philosophy comes from.
atoulme 00:21:30 not the construction of my sentences can be a separate PR, which is this passive-aggressive way of saying that we need to produce.
Bastian Krol 00:21:39 When you say, can, you mean should. That's how I read it.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:21:42 I'll make another PR. As easy as that. I mean, Antoine, no worries. I'll make another PR. I noticed it, I… yeah.
atoulme 00:21:51 to be extremely weird about this, did you know your stats are also coming from the fact that how many NPRs you merge?
Don't…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:00 You know?
I don't care about it, honestly, but, sure, yeah.
atoulme 00:22:06 But it also creates more velocity if you have, like, small PRs that are able to, like, you could… get them in like this, it's easier. Okay. Again, you know, Bestie's giving me the right grief here, which is, like, why are you… why are you standing in the way of a typo, right?
Don't… don't even think about it. Do it if you have the time or the…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:22:26 I will, yeah, sure, I will, yeah, no, it's an easy thing for me to do, honestly, like, yeah.
atoulme 00:22:32 But yeah, that's a discussion that will continue to happen with maintainers, because as we keep moving forward, we'll see more and more of a… like, people tend to be messy, right? And one thing I try to do, again, quite the contrary, because when I'm strict like this, is because I know that if I start to let go.
Then, two weeks after, some guy's going to drop a PR and be like, you know, here's a bunch of changes all over the repo. I'm like, well, I don't like that. But you let that one in. Why are you giving me so much grief when… why do I get double, double standard treatment?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:04 Yeah, yeah, yeah.
atoulme 00:23:05 So, it's my fine.
Anyway.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:23:09 It's all… it's all good, yeah, I'll do it, yeah.
atoulme 00:23:14 Okay, maybe we could move to all the questions from Jack, because he's got some stuff.
But…
Jack Berg 00:23:19 Yeah, so… If we're ready to move on, so, as Nikola mentioned, Grafana is interested in the injector. We're excited about it, we're trying to figure out how it fits in with our recommendations from an instrumentation standpoint. And so, you know.
Nicola has obviously gotten involved. I'm starting to look at this project and, and, you know, figure out what it does great, figure out, like, you know, if there's any areas that need improvement, and just try to help things along where I can. And so, you know, as I was kind of analyzing this, these are some of the questions that I was thinking about, and were, like, kind of rough edges when I was experiencing this. And so.
Bastian Krol 00:24:02 You know, instrumentation management. So, you know, when you install the injector right now, it downloads.
Jack Berg 00:24:08 you know, the latest of the different instrumentations. And so, if you think to the future about the upgrade path, you want to upgrade the injector, because it's installed directly on a VM, well, how do you upgrade the versions of these instrumentations, and how do you sort of, like, manage a collection of different versions of instrumentations, because maybe some apply, to some processes, but, like, others don't, right? Like, the Java agent has breaking changes sometimes.
So you don't necessarily want to, you know, update the version and not retain the ability to go back to a previous version if you liked the behavior back then.
atoulme 00:24:43 Well, okay.
Jack Berg 00:24:44 and… Well, so just, like, just to complete that thought real quick, so, like, part of me thinks, we don't… we shouldn't think about that at all on this project. There's already good, like, you know, package management tools, like, there's this tool called Mize, and, you know, for Java, something called SDK Man, which There are already CLIs for managing, you know, different versions of the Java SDK, or of Maven, a popular, you know, build tool in Java. And, you know, there's NVM for Node. And so what Mize is, is this tool that, you know, one of my colleagues recommended to me, and it's sort of, It's sort of like a… like a… like a… a higher-order version management tool. So, like, you know, it would replace NVM, it would replace Go Version Manager, it would replace Java Version Manager, and maybe we can plug into that ecosystem so that we don't have to manage instrumentation versions within the injector at all.
Bastian Krol 00:25:43 I would give you… like to give you another perspective. So, from my very naive and maybe too simplistic thinking, one injector version is always bundled to a set of instrumentation versions, and that's it. And we update to newer SDKs, and then release a new injector version.
And that way, it's always very clear, if you install Injector XYZ, then it comes bundled with… with… the Java, agent… whatever, and that's… that's that. So that makes it also someone else's problem without recommending any specific approach to managing that.
Jack Berg 00:26:24 I think that's a nice simplifying assumption for the short term.
Bastian Krol 00:26:29 happened.
Jack Berg 00:26:29 But the practical reality is, like, the Java agent is on an annual major version release cycle. And so, each year, we release a new Java agent version, and then we will continue to publish patches to the previous major version for some period of time, so we're double producing for some period of time. And it's, like, a really important decision of, like, whether you're using major version 2 or major version 3. And so, if the injector is always coupled to, for example, the latest major version, then, you know, you'll be stuck in these situations where it's like, you can't upgrade your version of the Java agent.
Yet, and so you're tied to old features of the injector, you know, because of that.
atoulme 00:27:13 Good.
Bastian Krol 00:27:14 you know… Realistically, the injector might not move that fast, and might not be a problem, but it could. I'll give you that.
Jack Berg 00:27:22 If the injector turns out to be extremely stable, then yeah, that's not really an issue.
atoulme 00:27:28 Yeah, you know what? I'm gonna brag, I could take the existing example of the operator here.
The operator, like, he has the bindings to bring all the SDKs, and so the operator right now has a version.txt, I'll put it in the doc.
Actually pointing out to which version of the Java SDK to bundle into itself.
And every time they make an update to these changes, then they make a new release of the operator, so that's going to what Batsy, what he's saying, where everything is kind of tied together, and the best part is, we actually tested everything so that we know it works.
Because we're worried about having basic things not work, like this environment variable is no longer valid for this particular SDK for that reason. So, now nothing works. I think that's the first… I think we should go for that first, because we don't know any better, and we don't have the community support to do more than that. And down the road.
we should make it so that we have a much better packaging system. Mine is… clearly an approach you can use, where we would be able to kind of say, we trusted with not just one version, but all those known supported versions of the Java agent.
As part of a matrix of tests.
It's still at work, right? Just, bear with me.
Bastian Krol 00:28:45 It's complicated, but I mean, it's a problem for later, maybe.
Jack Berg 00:28:48 I think, I think, like, you can probably have the best of both worlds by, you know, bundling in the single latest version that you know works well.
And then, providing an escape hatch where users can, you know, follow their own path and choose whichever version they want that is not the major version, and then just kind of say, like, you know, your experience may vary, right? You're free to use something like Mize or whatever the solution is to choose an alternative version, but, like, it's up to you to understand the idiosyncrasies of how the injector interacts with that version.
Bastian Krol 00:29:21 Yep.
Cool. I have to drop, unfortunately, I have a customer call coming up, but yeah. Oh, that sounds good, Jack. I like that.
See you around!
Jack Berg 00:29:31 Alright, nice to meet you, Bastion, I'll see you around.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:29:34 That's sweet.
atoulme 00:29:34 Chef.
Let's, maybe continue for just a minute, so… there's multiple things going on. I mean, we talked about it a little bit last time, right, where they would want to have all the SDKs kind of also distribute their own SDKs using Debian RPMs, and this way we can do some meta, like, declarative dependencies between… We know this injector SDK, or sorry, this injector Debian package has a dependency, can be a floating dependency on this major release of the Java SDK based on the name of the RPM, so we're going to pick whichever is the latest major release of that particular, like.
We can play that a bit better.
I don't think we're there.
Jack Berg 00:30:18 Yeah, right, there's different ways to solve this, but, like, whether it's Mize or we do the packaging ourself, or something else completely, it's just like, you know, this family of problems. Like, how do we manage versions of instrumentations, how do we provide an upgrade path, and how do we provide, like, control over which version you want to use?
Those are the types of questions we have to, look towards solving. And, you know, they're not that high of a priority right this second, but we should just… I just wanted to, like, socialize this idea.
atoulme 00:30:46 they're gonna crop up. The… maybe also a good question is, if you were an SDK maintainer right now for Java.
wouldn't you like to have some sort of a sense of, like, a commanding approach to how you want your stuff to be used on Linux boxes, right? You would be… Maybe even telling people, mice is the way, we tested it, we know it's certifying, we certify it works, and this is how you do it, and by the way, like it turned out, this is Debian package, this is how you're going to install this stuff. And… yeah, who am I to say that? You know, whatever you want to do.
So, I think that's a collaboration we need to have with different SDK owners as we… as we move forward, but yeah, so in the other… so, the flip side, why is Bestie also saying we should just be very good about saying this works with that, and even package it with us, is because of the community's use case.
I think very quickly, Basti and his team, they're very interested in having us support communities really well with Injector.
That's the next step.
And kind of enlarging the scope of the project from host to Kubernetes is a big deal, because it makes us take over a chunk of what the operator has to do today.
And relieve some of the operator work, actually. So it's too bad that we don't have Jacob, and unless he had to drop, but… those guys from the operator have been looking for a solution to kind of make their life a bit better for a while. And if we can move this portion of the operator and self-contain it into some sort of a well-understood fashion, that we can test outside of the operator, then their maintenance work is much less.
Jack Berg 00:32:24 Right.
atoulme 00:32:25 And…
Jack Berg 00:32:26 We're doing the unit tests, and they just kind of have a sort of end-to-end smoke test type of thing that makes sure that they integrate right.
atoulme 00:32:31 That's exactly it, yes.
And right now, if you look at the operator code, there's a lot of spaghetti code in Go that says, oh, if you're Java, then we're gonna slot in some, you know, environment variable a certain way. But you show Python, oh, we have to look for that environment variable, extract it from your container environment, and prefix it with something, and suffix it with something else.
Jack Berg 00:32:52 Yeah.
atoulme 00:32:53 That's disgusting.
Jack Berg 00:32:54 Yeah, ugly branching.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:32:56 Yeah, yeah. So, I guess what they're thinking is, like, make a much simpler operator by leveraging this, you know… The injector, which natively is able to do all this environment variable checking and all this stuff, rather than have to deal with this complexity at the operator level, which is not really its place to do this.
atoulme 00:33:15 Yeah, and then go back to committee and say, now there's only one way to do, injection of SDKs. That's the blessed way, using ZIG, using this approach, and then doing it this way. And people should just use that, and don't look at doing your own environment variable stuff.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:33:32 Yeah, yeah.
And then the same approach works across, better, your host, Or your Kubernetes.
atoulme 00:33:40 Yeah, Kubernetes, and then you can play with lambdas, and then you can play with, like, you, you know… it becomes some sort of a, like, ready-made type solution. So, I think this is why there is a good reason why the operator should… sorry, the injector should have a strong stance on which SDKs is going to use, and it's almost like two deliverables now, right? Like, one is the… I want to play along with the ecosystem, and I need to be nice about it, and then the other is like, oh, we really need… you just want to get something done here.
So, yeah, that's, and to the point, Jack, of saying is, like, for that, injector library, if it were to be bundled with the SDKs, and I think we care less about versions, and we care less about the comfort of people, because we would forcibly be pushing people off the newest, all the time. And in Kubernetes environments, it's not seen as much of a scene.
as if you're, you know, trying to… I might be wrong about this, and I eat my words, but it seems like in Kubernetes, going fast is much more appreciated. On hosts, you want to be on the same version of the thing until the end of times, right? Because you're like, oh, I don't know. No one's looking at this thing.
That makes sense?
Jack Berg 00:35:03 Yeah, yeah, yeah, definitely. It's like, So, as you're talking, there's sort of a recurring principle that I think I see in a lot of these questions I'm asking, which is, like, we should have, like, a curated paved path, but offer an escape hatch.
That's the thing that happens over and over again, you know, because we need that easy button where the injector just works, you know, for most cases. But then, you know, for the cases where it doesn't, what's the escape hatch? So that's…
atoulme 00:35:34 Well, yeah. And, we didn't really consider yet, but vendors like, Grafana.
or Splunk, we're going to want to swap in our own libraries at some point.
Jack Berg 00:35:44 Exactly. I'm surprised, like, you know, you coming from Splunk, I was surprised that there's not, you know, something to do that already, because Splunk makes heavy use of its own custom distributions.
atoulme 00:35:57 Because, for me, what's most important from the injector's standpoint as a project right now is to gather community.
Jack Berg 00:36:03 Okay, so yeah, it's like secondary priority. I got it.
atoulme 00:36:06 We're not in a hurry to move over to the injector, because we've had the old C code that's been working for us for years. We will eventually do that, because the pain will be worth the gains, right? So, right now, we're also trying, like, this type of features that we're being… seeing added from you folks.
help us make a case internally to say, well, it's time to cut over.
But yeah, we haven't had the need intensely yet to move over, even though we were donating that code and it got rewritten.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:36 But Jack, since they are allowed to override the… what… what is the path to the jar.
Jack Berg 00:36:43 Essentially, or the path to the…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:36:46 each of the SDKs and the environment variables or in the config file, Yep.
Kind of, like, as a vendor such as us, maybe distribute something that we just say, this is our version of the injector, take pretty much the stock.
upstream version and package whatever versions of SDKs that we feel like should be Out there for customers, you know, nothing's… stops the packaging. I think you're… I guess you're thinking of a more of an official hotel community packaging.
Jack Berg 00:37:15 Oh, it's just, like, I guess what I'm thinking of is, like, you know, that is an escape patch, you can modify the path to the, to the agent, but this is going to be a recurring, question for the injector is, like, how do you manage versions of these instrumentations? And it's like, you know, the, you know, the version of a distribution that you use, 2.0, 3.0, whatever, and then also, which distribution are you using? Whether you're using the Grafana or the, you know, the vanilla upstream one, and, you know.
it's great to be able to tell customers, like, hey, modify your config to point to this Grafana agent, but it'd be great if the injector could be opinionated about how we recommend people manage these versions.
atoulme 00:37:59 Yep.
Jack Berg 00:38:01 dumb.
atoulme 00:38:02 We did not document how to do any of that in a way that would be worthy. Like, when we make a release of the injector right now, we have a number of artifacts that we could publish that you would be able to plug into your build, for example.
Right? For example, we could give you the .so file, right, as part of the build, and then you would import that into your Graphana build, where you import it, make it a part of some RPM or Dillion, or even Docker image, right? And then the rest of it is just configuration files. But we did not document how to OEM the injector, in a sense. We did not do that.
Jack Berg 00:38:36 We don't need documentation on it, like, we could just always figure it out ourselves for, you know, people like Grafana that want to provide a distribution of this.
atoulme 00:38:46 Yeah, I'm not… I'm sure it's not… it's not that much of an obstacle, but it is not something that we have, it's not even a path that we are documenting in the sense that we don't know. Maybe we change our minds in two weeks and say, well, actually, we want the dots profile to be named something else, or…
Jack Berg 00:39:02 We break your stuff inadvertently.
atoulme 00:39:05 So we need to just be good about that. There's, we'll play the game at some point of…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:12 I get Grafana and Splunk installed on my box, and I'd like to get the Hotel 1, too, and I now got 3 versions of the injectors fighting for…
atoulme 00:39:20 That's gonna be a fun one.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:39:23 That's gonna be a fun one to do.
Jack Berg 00:39:25 Yeah, so, like, you know, we could take two different approaches. We could have, like, a Splunk injector, a Grafana injector, and an OpenTelemetry injector that are all competing with each other, or we can have an OpenTelemetry injector that has good configuration about indicating which distributions of the instrumentations you want, so that Splunk and Grafana don't feel the need to publish their own injector.
atoulme 00:39:46 That would be best for me, but yeah, we still have some special bits in our Java SDK, which is around profiling for the most part.
Jack Berg 00:39:54 I'm not saying you get rid of those, I'm just saying the injector learns how to point to the Splunk Java agent instead of, you know, the vanilla one.
atoulme 00:40:03 Yeah, yeah, yeah, yeah. Yeah, so maybe we could make our config files additives, for example, or… We'll figure it out. Yeah.
Jack Berg 00:40:13 Yeah.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:14 there's a feature request, somebody also asked for versions for the SDK, so you can kind of say, this path over here, like, I don't include exclude, use this version, this path, this version.
atoulme 00:40:26 Do you imagine? I, I mean…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:40:29 It would be… it might be a little bit difficult to kind of make sense of it all, but .
atoulme 00:40:35 I think this is asking a bit too much of our user base, and the problem of this type of config is that you set them up, and then you forget them, and two years later, someone else is going to be like, but why is this not doing the right thing?
I don't know how to SSH in that box, and, you know, it takes 3 days to get in that box, and I'm like, some… Bob did this, did not tell anybody. Like, that's what I'm worried about, it's more like the grating friction of humans in the middle of that. I might be wrong.
Jack Berg 00:41:05 So, on that note, so that's kind of an extreme case of fine-grain control, but, like, a more practical example of fine-grain control that you would want over configuration would be, like, I want to be able to specify a different set of environment variables for .NET than for Java, because some idiosyncrasy about how the .NET agent works requires different environment variables than Java. And so, like, I don't think that that's actually crazy unreasonable to say, like, hey, use this configuration for this language, use this other configuration for this other language.
atoulme 00:41:42 Should we do a… I wonder if it would be worth having the injector twice, then, with two different config files?
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:41:50 Yeah, should be, and then you use the exclude-include thing to kind of say which ones to affect.
atoulme 00:41:57 this… I mean, I don't… I don't love it, but…
Jack Berg 00:42:04 It's like you want, again, it's like you want a simple approach for the common case, but then you want an escape hatch. And so, like, when you install it, it should be the simple case for everyone, but then it's like, when you want to do something outside of these guardrails, how do you achieve it? And so, it doesn't have to be super pretty how you achieve it for the escape hatch.
atoulme 00:42:25 Yeah, and then for, going towards your… abounding toward your use case, I was thinking maybe if you're an Ansible guy, and you have a playbook that says for .NET of that type of program, I want the injector to just be very specific about what it's going to do.
So I have an Ansible playbook, for example, an Ansible collection, or a, you know, CHEF, or whatever. I'm going to install it on all my hosts, and it needs to be composable, meaning that there might be the injector installed for all of it.
And then on top of that, for that .NET program, I want this to be done differently.
And so the way it needs to be is completely composable in terms of configuration.
Jack Berg 00:43:04 Yep.
atoulme 00:43:04 Okay.
Jack Berg 00:43:08 So we don't need to have answers for these things. Like, my point with this list of things was just to start to socialize some ideas and, you know, get everybody talking about using similar language about the problems that we might encounter sooner or in the medium term.
atoulme 00:43:22 Yeah.
Jack Berg 00:43:24 I guess to move on, like, to one of the other ones, which is, like, something I came across immediately, was we need to find a way to get rid of the reboot requirement to, get environment variables seen by these SDKs. Like, right now, the way that you set them is, you know, at C environment.
And, yeah, like, you pretty much… I know there's a technical way to reload that if you, like, log out and log back in of your user, but, like, practically speaking, you have to restart the VM to have these be seen, and that means that the iteration cycle of getting your environment variable configuration wrong, it's, like, it's really painful.
So, we gotta find a way to… like, the install story gets really good if you can… because you can… you can point LD preload to your .so file, and that all works without a reboot. And the only thing that requires a reboot right now is actually getting the processes to see your environment variables.
atoulme 00:44:23 It's interesting.
Jack Berg 00:44:25 Yeah, so we can… we can avoid a reboot altogether if we solve that.
atoulme 00:44:30 Nature's pretty easy.
Oh, we, okay. So there's something a bit sad here.
I might be wrong.
I believe that this hotel export to OTLP endpoint thing is actually something that we support, but we gave it a different environment variable name.
And I don't know why.
Jack Berg 00:44:55 Well, that's actually a question that I have for you. Like, what's your… what's the project's philosophy around in, loading environment variables, right? So, you know, obviously it's kind of risky for the, the, you know, the program to be able to wholesale rewrite environment variables that a process is loading with, like, you know, whatever is in a, you know, your injector config file. That seems kind of risky, but there's, like, more constrained approaches where maybe you say something like, any environment variable that is prefixed with OTel underscore is a candidate for being loaded from an injector configuration file, and therefore, you know.
It might override what the process would see otherwise.
atoulme 00:45:41 Yeah, the way it's done in Zig is that we have, instead of overriding setenv, which we had done in C, in C, what we do is we look at the current environment variable set on the process, and if it is not set, then we override it with whatever is in the config file according to an allo list of environment variables that we selected.
But we don't want to just allow you to do a bunch of creepy things. But it's important, if it's already set, then we leave it alone, and you might get inconsistent behavior based off that, which, well.
You know, I don't know. But in the case of the Z code, from what I understand, we don't override setenv, we override getEnv. And when you override getEnv, you get a whole bunch of different clarity about what is already set, and then you can make some additional configuration changes. So, for example.
I was going on and on earlier about the Python path environment variable, which has been really problematic. Instead of just honoring that environment variable, you can manipulate it on the way out and, you know… prefix it, subfix it, stuff like that. So you can do more changes. You can change it, but not always. You can… you can do stuff, right? So, I think the approach here is still to honor whatever is set already, but also to… to make it possible to set those on-run variables, and… In the config file, you can see what… you can set which environment variables you want to set for the program, but for some reason… We decided to use a different name for those, and I think… I might be wrong about that, though. I can't remember. I know that I had it in my test where I managed to set environment variables To… something else.
Without restarting, as far as I can tell. I might be wrong.
Jack Berg 00:47:35 Okay, so maybe I just need to look into this further, and I was trying to configure something that was using a slightly different name than what was on the allow list, or something to that effect.
But it's good to hear that your perspective is something like, okay, so we intercept getENV, not set ENV. There's an allow list of, environment variable names, that will, inject.
atoulme 00:48:00 Yeah, correct.
Jack Berg 00:48:01 We'll ignore injector environment variables, if that environment is already set… set in the process.
atoulme 00:48:10 Yeah.
Jack Berg 00:48:14 And that's pretty much it. That's, like, the philosophy. So, you know, if… We just need to keep that allow us up to date, and, you know, that's the principle. Like, you know, if you really want the injector config to always take, to always be the source of truth, you need to make sure that these hotel environment variables aren't being already set for your process.
atoulme 00:48:36 I think so.
I mean, I feel pretty stupid right now, I should know this.
This is… the fate is not well understood, that's a big problem.
So… Yeah, Otherwise, like, we're not just setting the Java agent or Node.js agent. You need to be able to set environment variables. This is extremely critical, right? And if you have to set them in ETC environment, then we did not fix the problem. I agree with that.
So there's a problem here.
I must… I must find where the…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:12 I don't… I don't see that, the setting of the exporter. I couldn't find it.
atoulme 00:49:18 Okay, can't find it.
I think maybe it's in the… Okay, we, we look at… Oh, it's deep down inside here, let me share my screen.
There's some nasty things going on.
So, we do this, right? So… We have some… So this is for resource attributes.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:49:51 Yeah.
atoulme 00:49:54 I wanna say… Terital options, maybe not.
Config.zip, so these are the prefix things, which are…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:03 Can be set instead of that.
atoulme 00:50:06 When we read the configuration, I think we do some other things.
I don't remember. There's, there's, there's a way to do it.
Anyway, so…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:17 to say the exporter?
atoulme 00:50:24 We're, where's the name…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:29 Yeah, the resource attributes is quite cool, because that… that one is, like, half the battle, I think.
atoulme 00:50:36 Yeah, it needs to be a bit better, like… actually, I don't think it needs to be that specific.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:50:43 Yeah.
atoulme 00:50:45 Let me do the dumb thing, which is… There.
No, it's not mentioning code.
Okay.
Yeah.
Jack Berg 00:50:57 So maybe there's a gap right now.
If we have this principle, and we just haven't implemented it yet, then that's fine. We just need to implement it.
atoulme 00:51:06 Well, yeah, absolutely. So, no, the C code used to do that, for what it's worth. Okay.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:51:11 Yeah, I think it was accidentally removed.
Okay. Because I found the resource attributes, so that was… it's pretty cool.
atoulme 00:51:20 remember, but I must be setting this in test.
I thought him.
I can't remember. I must be setting this in test because we tested it in Docker, so we have to override that environment variable. So either we just override it using the standard?
Jack Berg 00:51:36 Maybe you're just getting away with… Yeah, maybe, maybe, yeah, maybe you're able to set the environment variable for the process itself.
You know, before you start the process, and so it's a little bit different than me installing the injector on a Linux box and having to, you know, somehow change the environment variables for processes that, you know, I'm not controlling.
atoulme 00:52:00 No, this is good feedback. We should… we should not have this problem at all.
I'm just struggling with this for some reason.
I don't see us doing anything… oh, okay.
It's because we're doing everything in one Docker image. So, collector…
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:17 the default, right?
atoulme 00:52:18 This happens to be coinciding. So that's a really good feedback. We should… we should make this a bit more painful in the test, and make sure that we can set those environment variables in the test, and see what breaks. And then we'll have a much better time.
Right?
Jack Berg 00:52:34 Yeah, maybe that's an area I can look at, just to, you know, start cutting my teeth on this project and start to get familiar and angry with Zig.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:52:43 No, it's actually quite cool, to be honest. I had a question about the resource attributes, or these environment variables. I guess, any reason why… I mean, design choice was made to kind of, like, prefix them with hotel injector?
Yeah, exactly. That's… that's the thing that caught me.
atoulme 00:53:06 none that I can think of. It's just… It's just, you know, safe.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:53:13 Yeah, true.
Jack Berg 00:53:15 Wait, so safe, like, you know, you avoid a possible conflict with if hotel resource attributes is already set?
atoulme 00:53:21 Yeah.
Jack Berg 00:53:22 Like, maybe… Hmm.
Is there, like, is there a theme there? Do we need to do that for other environment variables?
atoulme 00:53:31 Oh my god.
Jack Berg 00:53:31 injector alternative?
I don't know.
atoulme 00:53:34 I think so. You drive me.
Jack Berg 00:53:38 Or did we just get rid of that?
atoulme 00:53:41 Yeah, I think I… I think I don't know that we care, Well, not that special, right? So… But that's… that's a question that's, I think this is coming also from, from, the… the combination of, like, how this was given over from Dezger. So, we just need to… To think this through.
Yeah, anything of Autel Injector… Prefix seems to have some opinion based on that.
Then, I think we can change our minds about this. This is a good time.
So I don't have a… I don't have a reason one way or another. I really don't care at this point.
Jack Berg 00:54:21 My, my last bullet on here is actually related to the resource attributes thing, which is like, you know, when you're actually running this in practice, there's an increased reliance.
atoulme 00:54:30 On whatever your agent is, having good auto detection for a service name.
Yes.
Jack Berg 00:54:36 Because if you don't, then everything gets, you know, emitted with the same unknown service colon language, unknown service Java, unknownservice.net, whatever it is. And so, you know, that's really bad, because that means that, like, you know, two different processes can end up with the same, like, identity.
atoulme 00:54:54 Yes.
Jack Berg 00:54:56 maybe they have a different service instance ID that differentiates them, but, like, I'm trying to think through, like, what… what can we… like, we can go and improve the agents so that they have better detection mechanisms and have, you know, look in all sorts of nooks and crannies for a good candidate for service name. But I'm wondering if, from the injector standpoint, we should think through some sort of escape hatch.
Like, maybe there's a way to specify in your configuration that if service name, if hotel service name is not already set, you set it based on, like, the pattern, some sort of pattern where you can reference parts of the, like, the process, you know, the arms or the, you know, the process name.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:40 Imputable, or the jar name, or something.
Jack Berg 00:55:42 Exactly, the executable name, whatever it is.
atoulme 00:55:45 As long as it's not too expensive to do so.
Jack Berg 00:55:48 I mean, it's just, you're setting one environment variable.
atoulme 00:55:52 Yeah, but I mean, it starts like this, and then people are like, oh, can you also.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:55:54 Fuck.
atoulme 00:55:55 the WSC2 metadata API, so we can do a little bit of search, and then we can, you know, get the lambda function name based on some correlation, and now you're in hell.
Jack Berg 00:56:05 Okay, so no lookups, just like, you know, the only thing that are candidates to be set in the hotel service name could be, you know, the bits of information we already have accessible locally.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 00:56:15 The command line, yeah.
Jack Berg 00:56:16 On the command line.
atoulme 00:56:18 Oh, okay. I think that's the same default.
And we could also just be… So, on that thing, it's also great not to be perfect, because we can give it hints for the collector later down the pipeline to maybe amend that service name, maybe drop the command line arguments, or do something, or perform its own service name attribution based on some parameters. But I also know that the SDKs, like the Java SDK, is well known to have its own, you know, service name detection, right?
Jack Berg 00:56:47 Yeah, and it does a good job most of the time, probably better than most languages, but there's still exceptions. So, when I ran this, for example, I was getting unknown service Java for a few processes that were on my machine.
atoulme 00:57:00 I mean, okay, you start with service name, but that's a slippery slope, because the next thing people are going to ask is, who's that name, right?
Jack Berg 00:57:09 What? I mean, maybe, maybe we just, maybe we just more generally have a capability to templatize OTEL resource attributes, and, like, service name is just, like.
you know, a thing that you can set in OTEL resource attributes, and we have some known list of properties that you can inject into this template. And it could be, like, you know, we know the host that you're operating on, we know the process name, we know the executable, we know the process command line args.
Things like that.
atoulme 00:57:42 I'm good with that. I think just… And it's… I mean, I'm always in the camp of under-promising and over-delivering on this type of stuff, and I… I don't want to set too much of an expectation that we're going to be able to nail the whole ecosystem problem.
Especially on host, Windows, like, all those things. But if you want to engage in that, I think that's fair. I don't… I won't have any problem with it.
Jack Berg 00:58:08 I just anticipate this being a problem as, you know, people actually pick this up and use this in anger. You know, they're going to ask the question, why do I have unknown service Java? And, you know…
atoulme 00:58:21 Yeah, I was gonna make it the Java SDK problem, frankly. Be like, I don't know, just ask the Java guys.
missing something.
I mean, but then the point that I'm making in my head is, like, maybe you'd like to have the same uniform value between your Ruby process, your Java process, your Python process, and having all those three teams talk to each other and make sure that they get the right service name is a long and lengthy process where, really, what they wanted to do is app.
And they didn't have the, you know, they just want that thing to say app on it. And it's the same app for them, for some reason. Let's say they're running GitLab, and it's, you know, 5 different things in a trench coat, and then they just want app to show up, right? So… I find myself agreeing with you.
Jack Berg 00:59:07 It's really hard to standardize, like, these types of resource detection problems across all the agents. Like, it's gonna be hard to convince .NET to do what Java does to do what Ruby does. And so, like, you know, we're basically… by not solving this problem at the injector level, we're, we're sort of, letting our hotel organization issues be a leaky abstraction and, like, get up to users when, you know, we could provide an escape batch to solve them.
In one place.
atoulme 00:59:37 it's not… it's… we're… it's going to feel like a walk around for the fact that there is an organizational issue, but that's fine. I think we can live with that for 2-3 years. And in three years from now, we'll have a discussion about how we should have a test framework, applies to any SDK, any language, and it returns the exact same value for your… That's… that would be a great point to have, right?
Jack Berg 00:59:59 Yeah.
atoulme 01:00:01 Okay.
Okay, so hopefully I, looks like we covered most of your questions.
Jack Berg 01:00:07 Yeah, we covered all of them. I just… and again, these are just socialization topics, and, you know, I don't think any of them are super pressing right now. I think.
atoulme 01:00:16 Fair enough.
I'll give you my philosophy, which is going to be a guiding principle for me, it's just less is more. We need to make another release of the injector, and continue to bring more people to this project, and make them more amenable, excited about what it can do.
And, all those customizations and additional things, this configuration, all those things, we need to just make sure that we expose people to a user API that is making sense. So, for example, every time we add an option, we need to have send defaults with it, like, include, exclude, cool, but it comes with send defaults so that people are like, I don't really care, this works, right? And then they… they start to get that value for free, and they don't, like, if they really don't like it, they can get into the config file and change, but… yeah. So, for any of those additional things, just let's think about the user impact of that, and be good about it.
Jack Berg 01:01:09 Yeah, and like… you know.
sort of like a Unix philosophy of, like, a really small set of composable tools. Like, what's the smallest surface area we could have for configuration options that when, you know, bundled together in different ways, allows you to sort of have a… end up having with a Swiss Army knife that can solve a lot of different problems?
I don't know what the answer is, but, you know, all these problems are sort of intertwined in some way, they're all sort of like configuration-level problems.
atoulme 01:01:39 Yeah, let's continue to get more feedback from people who try it out as well. I think, we will always be surprised by people.
One way or another, so…
Jack Berg 01:01:48 Yeah.
Okay, we're at time, so let's, try to have a good meeting hygiene and stop now. Thanks, everyone.
Nikola Grcevski @ Grafana Beyla / OpenTelemetry 01:01:55 Good chat.
