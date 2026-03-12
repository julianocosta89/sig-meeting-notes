SIG: Kubernetes Operator SIG
Date: 2025-08-28
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

**Mikołaj Świątek** 00:26 Hello there?
Can you hear me?
**Vincent Desbois** 00:33 Yes, hello.
Thank you.
**Mikołaj Świątek** 00:38 I wanted to apologize for myself and my fellow maintainers for being a little bit late.
Unfortunately, we have a… the time… we might, we might decide… we might, consider moving this time, I think.
**Vincent Desbois** 00:52 Oh my god.
**Mikołaj Świątek** 00:52 because I feel like it's more difficult and more difficult to actually get everyone here at this time.
Hey, Benny.
Do you know if, Jacob and Pavel are coming?
**Benedikt Bongartz** 01:08 Mmm… Pavel, I think yes. Jacob was… he said he's moving?
Maybe from one house to another? I don't know what exactly, or maybe he is moving, so traveling.
**Mikołaj Świątek** 01:24 Alright.
**Benedikt Bongartz** 01:24 I don't know.
**Mikołaj Świątek** 01:25 Let's give ourselves… let's give ourselves two more minutes, and then we can start.
Unfortunately, I'm… today, I am also, like… … not on top of things. I'm not on top of things ever since I've gotten back from my PTO.
So, I don't know if there's, like, anything… Critical that we need to talk about.
**Benedikt Bongartz** 01:55 I was….
**Vincent Desbois** 01:56 May I also ask you some questions, since I'm… I mean, you don't know me, I will, of course, introduce myself, but is it… I understand it's okay to participate in this way, right? And to bring some topics, or… just let me know, because I wasn't sure about the practicalities.
**Mikołaj Świątek** 02:14 … It's absolutely… this is… you can absolutely participate, this meeting is open.
The way you would normally introduce a topic is we have an agenda document that's linked in the calendar, and you can go… you would normally go in there and add it, but it's not like this is a very formal requirement.
So, you can, for example, you can add it now. I'm gonna link the… I'll link to documents in Zoom chat over here.
**Vincent Desbois** 02:44 Okay.
**Mikołaj Świątek** 02:48 go.
**Vincent Desbois** 02:50 Yeah, okay, okay, I can do that immediately, actually, yeah, thanks.
**Mikołaj Świątek** 02:54 You can also add yourselves to the attendees list.
It's still… it's still summer, so… so these meetings tend to be less staffed than… than you would normally see. That's why it's just… just the three of us.
**Benedikt Bongartz** 03:14 Oh.
**Mikołaj Świątek** 03:15 We have more arrivals.
**Vincent Desbois** 03:17 Right.
**Benedikt Bongartz** 03:42 Oh, there's Jacob.
**Jacob Aronoff** 03:44 Hey, sorry.
Okay, let's get into it.
**Mikołaj Świątek** 03:59 I think we can get started, yeah.
So, what do we have? We have something about… Skipping O132.0.
So what happened this time?
**Jacob Aronoff** 04:13 This time it got put on the… like, the issue got created kind of late.
I think it… Pavel opened it, like, 3 days ago, and I just saw it 2 days ago, and then they did the release for 33 this week, so I think that the… They just, like, missed the, … the issue when they did the 32 release.
**Mikołaj Świątek** 04:37 Okay.
And… and because… because we're all, like, moving between PTOs and so on, we… we actually don't know this.
**Jacob Aronoff** 04:46 Yeah, I also literally moved, like, last week, so I've been… my availability for, like, reviewing has also been nearly zero.
**Mikołaj Świątek** 04:56 Believe it or not, I only, like, now am getting out of my backlog after getting back. This is just… I also have a string of things I need to review in the operator that I haven't… although it looks like there's been a bunch of activity on these PRs, so it's not like anything's waiting for me.
But yeah, I'm fine with skipping.
**Jacob Aronoff** 05:20 Yeah, I don't think that it's the end of the world. There is, as Ben I put in here, it looks like .NET is failing for some reason.
**Benedikt Bongartz** 05:30 I guess it's just the end-to-end test, so we didn't upgrade .NET itself, it's still 1.2.
And the end-to-end test fails and says specific… I didn't look into it too much, but it says some specific values are missing.
And I'm curious why.
Because exactly the same stuff works.
On the main branch.
**Mikołaj Świątek** 05:52 Yeah, why… like, these tests now should be… should be… really much exactly the same. Like, have you bumped .NET in this….
**Benedikt Bongartz** 06:02 Nope.
**Mikołaj Świątek** 06:03 So it's exactly the same thing.
**Benedikt Bongartz** 06:05 It's exactly the same thing.
**Jacob Aronoff** 06:07 Did someone change….
**Benedikt Bongartz** 06:08 The only thing is the collector changed, and that's why I was… as I said, I didn't look into it yet, so I was curious if maybe… There's something… That filters out… description changed or something, I don't know.
**Mikołaj Świątek** 06:27 I love it.
**Benedikt Bongartz** 06:27 Since we search for the specific strings, if you just… Remove a dot at the end of the sentence, or whatever, it should be already starting to fail.
**Mikołaj Świątek** 06:37 But do we… do we search for, like, specific strings from collector logs?
**Benedikt Bongartz** 06:42 Yes.
So, if… I've seen this when I went there to modify all the tests.
There is some script which goes and checks the collector lock if, for example, a specific metric appeared, and the way it's checked is it prints this to console in the Bose mode.
And then we go line by line and check if this is in this line.
**Mikołaj Świątek** 07:09 So… Does that happen necessarily, or does that happen because we wrote it that way before we knew that Chainsaw had a function to decode Prometheus metrics?
**Benedikt Bongartz** 07:24 I guess this was before, but this is also not Primeter's metrics, it's… Yeah, I think the Open Terms Collector just goes and… Prince… Yeah, right, so technically we could use the Prometus exporter And then check it with this.
But yeah, I guess….
**Mikołaj Świątek** 07:41 Huh.
**Benedikt Bongartz** 07:42 Way to go.
**Mikołaj Świątek** 07:43 If we're using Debug Exporter to print that stuff, debug exporter output can change.
And then has, historically changed a bunch of times.
So… Not… not unlikely, I would say.
But this is the case.
**Benedikt Bongartz** 08:03 So if we go here, maybe I can share my… Screen? Somehow?
… Give me 20 seconds to figure out here.
**Mikołaj Świątek** 08:19 There are some changes to Deepad departure in this release.
**Benedikt Bongartz** 08:25 Oh, nice. Yeah, so what you can see here is more or less that we go and use kubectl, I guess, somewhere to generate some load.
And then afterwards… there's this check logs, and then we check, for example, process CPU time.
and then the description, the description, if this is in. So if, for example, the metric name changes, or just the description changes, or the way how it prints, gets printed changes.
This is already… Not working.
But I'm confused that it just happens in .NET.
**Mikołaj Świątek** 09:16 … alright, I'll also have a look later.
But this is most likely, like, not a real problem, right? It's just, ….
**Benedikt Bongartz** 09:33 Nope.
**Mikołaj Świątek** 09:34 discovery.
**Benedikt Bongartz** 09:34 I think so.
**Mikołaj Świątek** 09:35 Problem, problem, art tests.
Right.
Okay, the next topic is supporting range of OpenTelemetry collector versions, so… who's… whose is that?
**Vincent Desbois** 09:55 Yeah, that's the topic that I was, willing to bring up. So first, thanks for the possibility to participate to this meeting. That's the first time I participate. I'm working in, in Ericsson, located in Stockholm. And just to give a context, we are, you know, I'm involved in a project where we are actually, starting to build some products based on, OpenTelemetry Collector and OpenTelemetry Operator, actually, and the goal is to replace, a few, earlier open source projects, such as Promet I use Jager, and, yeah, and a few more things.
And, actually, so, yeah, and I think, you know, actually, I'm not bringing necessarily a problem, but more a fundamental question. I mean, we, when I started to look more into the, you know, some of the documentation around, you know, a recommendation around the operator component, I bumped into this, this principle here that, … I mean, dependency principles, that major and minor version between the… between the operator image and the operand image.
And, you know, I was wondering, actually.
Whether this is actually still, you know, a strict principle being used in the project, and … because we… I mean, we are… from our perspective, you know, we are, I mean, looking at the perspective to be able, actually, to have much more decoupling between, between the operator and the operator, we believe that they need to be able to, you know, we should be able to upgrade them independently.
So either you upgrade the operator without affecting the operand, assuming, of course, that the installation is still compatible, or you have the possibility to maybe modify your CO in the… request the operator to upgrade or downgrade an instance without upgrading the… the operator itself.
And, I mean, at the end of the day, when you try to achieve these type of patterns, and we've been dealing with other Kubernetes operators, it usually boils down to have the… having the operator supporting a range of versions of the operand.
… And of course, yeah, that probably… that pattern can maybe not last forever. I mean, there might be at some stages when you… when, for example, there is some major change, you need to, yeah, you need to accept that, but… But generally speaking, yeah, we're a bit curious about, whether this, this, you know, this, this pattern or this, recommendation is still really a strict recommendation, recommendation.
So far, at least in what we have tested, we did not, and we didn't test many combinations, at least we haven't seen that there was actually, necessarily some, compatibility issue, even if the minor versions were not matching.
But I'm wondering, you know, how you… how you look at this aspect, and also how you have been maybe considering, you know, upgrades, upgrade scenarios, and independent upgrades of these components here. And in the ticket I created, you know, I was bringing up the example of the Prometres operator, which seems to have a… a pattern of, supporting a range of, of different, Prometer use, server versions, actually. And, this is documented, on the… inside the project.
So that's more, yeah, a bit of principle thing. I'm wondering, is this still, really a strict, strict pattern? Where is it coming from? And, yeah, that's maybe… that's the kind of topic I wanted to bring.
**Jacob Aronoff** 13:16 Yeah, so, … I think the reason that we don't… that we recommend keeping them relatively in sync is that the collector is not at a stable version yet, technically, and there are breaking changes that they can push, and so when we're doing things like automatic Configuration for, ports.
or, extensions, you know, things like that. We need to have a guarantee that, their configuration that they read is the one that we're going to write. And so that's sort of the, like… principled currently. I think… That being said, I believe that you could probably get away… with, … running a… Current operator with an older version.
If you are not using those features, that should be okay, and if you're not using the upgrade features.
it might be okay, but you'd probably run into a few of these things where, like, the newer operator version writes config in a way that an older collector version doesn't support. That's really the core of the problem, is that the, … Collector components do change, right?
… And that's why we have upgrade strategies, is so that we can do automatic upgrades as the collector, you know, makes changes internally. But we also do have some support for the external, like, contrib components. And the stability of those is really up in the air, and those can change really rapidly.
kind of on whatever timeline they want at this… for most of them. In which case, if you're using those contribib components, you might run into issues. I think if we really wanted to.
We could probably do this type of thing, where we only said.
You know, we would only support some subset of collector components post… collector 1.0 stability. We then say any components that are 1.0 are compatible with the operator You know, for end versions, and that would be reasonable. I think that we wouldn't be able to say that carte blanche, though, is the problem. We wouldn't be able to say that, like, the operator will always work With every version of the collector, with every component of the collector, and that's where you get into trouble.
Miguel, does that seem reasonable? Take it away?
**Mikołaj Świątek** 15:51 Yeah, so if you want to compare us with Prometheus operator.
Prometheus operator was written at a point where Prometheus itself was a much more mature project already than the OpenTelemetry collector is right now, so it's easier… so it's a bit easier for them. And also, Prometheus has… a pretty defined scope. If you take Prometheus, it's just Prometheus. It's always the same artifact, and the Prometheus does keep, generally, API stability and configuration stability seriously, so you can be reasonably, as a Prometheus operator maintainer.
you can be, like, reasonably assured that, yeah, you know, you can change that version in a pretty decent range, and you're gonna be okay. We're in a difficult… more difficult position, as Jacob suggested, where… … the OpenTelemetry ecosystem in general is just not… not that stable, so we're all working with moving targets over here. If what you want Auto Operator to do for you.
is just, kind of, management tasks, let's call them. You don't want us to automatically create anything for you, or parse your configuration, and open ports, and so on.
then you're… like Jacob said, I think you're going to be okay. Like, this is… this is… I say, I think, because there's not really, like, a boundary anywhere that enforces this. Like, I can't tell you right now with… with full confidence.
that this is gonna be okay, but I think it's gonna be okay. I think it's gonna be okay if you, like, just disable, for example, the features which tries to… the features that tries to parse the configuration and do things like, add, air back.
necessary, because we have features that do things like port opening, we also have features that add air back automatically for components that interact with the Kubernetes API. If you don't want to do all of that, if you're okay with doing all of that on your own.
then you should be fine, because fundamentally, you know, we just spawn the collector. If you supply… you supply your own configuration for that collector, if you're okay managing that yourself.
you know, if you're okay saying, I know which configuration goes for which version, and when in my pla… in your platform, if somebody does a rollback, you're okay knowing alright, we need to do a rollback to this configuration for this to work, then I think… you… and I think you're going to be fine, but also you're going to get significantly less value out of Auto Operator if you work that way. But if that's okay for you, then I think that's fine, and we can think about giving some kind of… Maybe not guarantee to start with, but we can think about giving some guidance that says, basically, if you don't use these features of the operator, then you can expect a wide compatibility for collector versions.
Fundamentally, we're not doing it right now, because we're… we're… we are… we, as many other projects in the hotel space, we are waiting until the collector is going to be stable, and then a lot of things are hopefully going to become easier to manage.
In this respect. So this… and the reason this version coupling was originally envisioned was just to make our life simpler. That is literally the only reason. But it's the same way, I think, with instrumentation images, where we don't really say anything about instrumentation images. We publish the ones we have, and there's not really a specification.
For them, but there are a bunch of people who just repackage them and add things to them, or build their own based on what we do, and this seems to just work alright. If you want to do these things, you are accepting more work, like, you are… the work that we're doing, you're rejecting, and you're saying, I want to do this by myself.
And if you're okay with doing that, I think you should be fine.
sense?
**Vincent Desbois** 20:16 Yeah, no, that makes sense. Maybe also some, maybe, I mean, also to give a bit more about our context, at least, you know, I was… I also saw in this recommendation that, there was, like, the special case that if you are doing an… if you have a non-custom image, which is… which is our case, you know, we are building our own, collector custom image, and then the recommendation from the… the README file, whatever file it was, was, yeah, then in this case, you should be… you should think about the version of the core part of the hotel collector. So I was thinking, okay, maybe the… then the issue doesn't lie so much in all these exporters and so on, but more potentially in the core compatibility with the operator.
I have to admit, I'm not on top of all the features, but at least I know that when I look at least at the different CRVs, I mean, I don't think at this point in time we would use the instrumentation one, and we would not use the, … what is it called? The OPMP, but probably focusing on the… OpenTelemetry collector, CRE, of course, and, yeah, and possibly the target allocator. I don't know if this, by saying this, if this is also potentially you know, removing, risk when it comes to, to, to compatibility, problems, but, I don't know what, what, what you, what you said, but, you know.
**Mikołaj Świątek** 21:37 Mmm… I… Honestly, instrumentations are even more shaky in some ways than the auto-collector. It depends on which ones. Again, there's, like, a wide, wide variety of stuff.
The Java one, for example, is pretty nice, but there are some which are quite new and moving quite fast.
… Oh, yeah, but that's….
**Vincent Desbois** 22:04 The instrumentation is something we don't plan to use, actually, so that's probably removing some risks, then, in terms of compatibility. So, you know, if we were… if I was really going for maybe the minimal, well, minimal scope from a CRD perspective, and if we were just using, essentially, the OpenTelemetry Collector, CRB.
Are we already, kind of, at least, you know.
Removing a few of the hinders for achieving compatibility, or are there still, ….
**Mikołaj Świątek** 22:31 I think the main… I think the main prob… the main thing that might be left there is the fact that we do some… parsing around.
Health checks and exposing metrics?
If you disable those as well, I think you'll be… you'll be in the clear.
because, … Jay… Anyone else, if you remember this better, please, … correct me, but I think we are doing some stuff like that around, like, service… I don't know if it's just when you want to use, like, service monitors and so on, where we, for example, try to get the port of the Prometheus endpoint.
for the collector internal metrics, and do some stuff with that. And that is something that has recently changed upstream.
in the auto collector, to… to some amount of pain for us.
… so… What I can promise you is that we can, in your issue, list the things that you might have trouble with to start with. So, you can list the things that you might have trouble with, and what you might want to avoid using.
Because it might be functionality that might depend on the collector version in some way.
And where right now, we are, again, we are not doing anything like, here's the code path before version X, and here's the code path after version X. We don't want to do it until the collector is stable, because it's just gonna be a lot of… churn, and ultimately, after the collector is stable, like, basically everyone's gonna jump to that version. It's gonna be, like, a clean slate going forward, and we can consider doing those things afterwards.
But I think what I mentioned is going to… Hope you get started.
Yeah. With, like, with what you need. Eventually, I don't think we're gonna give, like, a support statement right now, but we might, we might update the README that you've read to… to give a little bit more detail about how to approach this.
Trouble?
**PL Pavol Loffay** 24:57 I can… I can look in. I… I'm interested, like, why do you want to use the OpenTelemetry operator to deploy the collector?
**Vincent Desbois** 25:10 Why? I think this is… I mean, we see, you know, that we… actually, we have quite a lot of, sitting in an organization who is kind of, you know, serving a lot of applications, having different needs, and I think having the flexibility to to, I mean, to manipulate and to define different kind of configurations and so on. I mean, and also, you know, the goal maybe to align more towards GitOps approach and so on, so I think the declarative approach, I think that's something that fits very well in our, in our, in our, in our strategy, so I think we… we have so many varieties of needs for configuration that, you know, we… I mean, at the end, the operator… I mean, the operator pattern is of interest. We are already using a lot of operators for… For data management services.
So far, when we were using, and I would say, our first generation of open source collectors, such as Prometary Server or Jaeger, I mean, we didn't… other than the operator, so, but yeah, I think this is also a general direction we are taking for in many, many areas.
But it's not a… yeah, I think I see the operator that we have now here of our geometry corrector is very original. I mean, I see, I mean, there is a very… already a large variety of use cases, but as I said, some of them are maybe… never going to adopt, I mean, such as the instrumentation one, I'm not sure we will go for that. But, yeah, we are very interested in the basic lifecycle one, and also the target allocator, which seems to provide some quite good way to Blue-scale parameter scraping, and so on, and with much more flexibilities on what we can do with basic, A basic Prometheus server, basically, and, yeah.
**PL Pavol Loffay** 26:57 I see, like, the reason I'm asking is, maybe if you just need to deploy a collector as a deployment.
Then I would argue that you probably don't need even the operator, you don't need all this additional functionality, like.
the sidecut injection, and the instrumentation, and so on. And that way you can, you know, control, if it were.
**Vincent Desbois** 27:20 No, he wasn't.
**PL Pavol Loffay** 27:20 It very well, and it's… it's fully under your control.
**Vincent Desbois** 27:26 No, no, I get your point. I mean, that's also, that's a valid argument. I mean, that has been also, I mean, one of the earlier alternatives we considered, but then we have also different stakeholders, I mean, you know, also different requirements and expectations, so yeah. But, yeah, I mean, that's, that's, of course, yeah, a possibility, still, yeah.
And then I was maybe thinking, you know, if we look at… I think that would be great to anyway, yeah, if you… if you can give some kind of input, in written form, either in the ticket or in this README file, whatever, I think that's great to… as a guidance.
Then I was thinking, if we are looking forward, you know, in the future, when, you know, based on what you said, all of you, once the collector is more… is more stable, then is there, then, you know, I guess a future where you would definitely, you know, relax more this, this principle, and I was wondering if you have, … If you have even such a milestone already, that, you know, as soon as a collector is reaching, version 1, and then you will start, you know, really opening the door to different principles, and maybe follow a little bit more what some approach… some other approaches with more mature components have adopted as well, or what… is that already… is there such a milestone already, or… Where are you from this perspective, or…?
**Jacob Aronoff** 28:46 I don't think we've talked about it yet, but, I could definitely see… part of it is that we're waiting on the collector to finish their V1, and, you know, the conversations are kind of moot.
Until they do. But I can definitely see us running, in the same way that we want to do for semantic invention, running, like, nightly compatibility tests. We also do this for Kubernetes, where we support, like, a range of versions, and I can see us doing that with some subset of the V1 collector builds, where we say any components that are marked, stable.
for the collector, should always emit, you know, this telemetry given this input, and we should be able to run that nightly and confirm that, like, the operator does support that stable build. I think that that's, like, a pretty reasonable ask. … if you wanted to, … what would be very helpful for us, and for me, would be, if you were to take this context around collector stability and, like, operator compatibility, from this conversation and put it on your issue, I think that this would be a great thing for us to do post-collector V1 stability, and it wouldn't even be that hard. We already have … a lot of testing harnesses that do exactly this, and I don't think… you know, I think it would actually be very… it would be very beneficial to people like yourself, who are sort of seeking that, stability guarantee. I think until the collector has that stability guarantee, we can't, … have one, right? But once they do, I think we should as well. So I think that that's pretty reasonable.
**Vincent Desbois** 30:28 Yep.
Dio?
Okay. No, please.
**PL Pavol Loffay** 30:35 Really, the pattern with operators is that the… the upgrade goes through OLM, the Object Lifecycle Manager, and it updates, or upgrades the operator, and then Once the operator is up, it will upgrade the instances.
In OLM, you can as well… not sure you can, but you should be as well able to configure… configure it to watch specific namespaces.
And that could allow you to run multiple instances with different versions.
But this is not what most people do.
**Vincent Desbois** 31:15 Yeah, yeah, yeah. I mean, we have, I think we have already some customers, I think, that are already using OLM. I mean, we also have some others who don't, so I think we are also still, you know.
some situations where we are actually upgrading an operator using Helm, actually.
So I think we have a variety of patterns to support, but yeah, OLM is obviously the… the direction for many, but, yeah, no, yeah.
No, but, you know, I think, I don't know, I think you gave me… quite some good insight about, you know, the background to this. I was expecting, of course, that it had to do with stability of the collector, especially. I mean… that you didn't just, implement this because it was make… yeah, I mean… Yeah, so I think that's great to get this confirmation, and I think, yeah, if we can get any help on understanding a bit more, at least what are the sensitive areas that can break a compatibility, I think that's… That's also a great input for us, actually.
Do you… from this discussion, and maybe based on what one of you said, do you want me in the ticket to at least, you know.
Maybe possibly list some, you know, some principles that we believe should be applied, and then, and also having this expectation, maybe on having some kind of, milestone where we can start having, you know.
some stability, a goal, or whatever, I mean, is that, is that good input to include then? Yeah, okay.
**Jacob Aronoff** 32:49 Yeah, yeah, I think it would be great to do. Thank you. And then we can also, I'll add a label or something. It probably would be worth doing this for other issues as well, but, like.
I had a label for post, … supposed to be one milestone, I think would be really good to do. Sorry, I'm getting a call, so give me one….
**Mikołaj Świątek** 33:29 All right, Vincent, are we okay to move on for this, for now? Nope, I don't think so.
**Vincent Desbois** 33:33 Hold on a second.
Thanks a lot, Jan. Yeah.
**Mikołaj Świątek** 33:37 Okay.
So the only… Benny, can you actually share your screen? I'm afraid of trying after some stuff that happened earlier today.
So then we have this host PID.
… That's….
**Simon Olander (SAP)** 33:57 Me?
Right, so, … what I want to bring up is simply that I have a situation where I want to be able to set the host PID field in the collector, and I'm not able to do that. So, that's why there are an issue for… there is an issue for it, and also I made a pull request for it as well.
I can share my screen if y'all want to see it, or… what do you feel like?
I guess my input is really just I want to have feedback, if it makes sense to… to have.
What's your opinions about it? I wanted to bring up in the run to see.
**Mikołaj Świątek** 34:34 It's just, I mean, that's just another field that basically gets passed to the pod spec, right?
directly. I don't see any reason to reject it when we added all the other ones. This is an unfortunate aspect of Kubernetes, unfortunately, where whenever there's anything in the pod spec, eventually your CRD has to include all of it, just because there's always someone who wants to set some specific attribute, and Kubernetes Doesn't actually let you… If Kubernetes let you reference the standard CRDs in some way inside your own CRD without having to embed the entirety of it, that would solve all of these problems instantly, but it doesn't.
So, we have to add things manually. From what I can see in your pull request, it looks perfectly fine to me. You have some, like, some conflicts, but….
**Simon Olander (SAP)** 35:35 Okay, still some conflicts? Alright, I guess I have to rebase or something again, but… ….
**Mikołaj Świątek** 35:40 Mmm….
**Simon Olander (SAP)** 35:41 One thing….
**Mikołaj Świątek** 35:41 I will say… I will say that in the contributing, there's, like, a bunch of, make targets that will help you not get these, generally speaking. So, … so you can have a look.
Those help. We have a bunch of code generation and things updating in various places, and it's, like, surprisingly easy to commit something you shouldn't really be committing.
**Simon Olander (SAP)** 36:08 Are you… are you, … which… are you seeing my screen? I'm not sure.
**Mikołaj Świątek** 36:12 Yes.
**Simon Olander (SAP)** 36:12 It's clean.
**Mikołaj Świątek** 36:13 Which is….
**Simon Olander (SAP)** 36:13 minimize the sharing?
What do you think?
**Mikołaj Świątek** 36:15 You're sharing the issue right now.
**Simon Olander (SAP)** 36:17 Okay, sweet. … Okay, yeah, I'm having conflicts here. Yeah, I was battling a little bit with it, that's why. I kept getting, like, an issue when I was… making it. So I was a bit confused, but I will go over it again.
It basically kept complaining about it, and then, you know, one of the make commands worked, and some didn't, so I was a bit confused.
Anyways… ….
**Benedikt Bongartz** 36:44 country.
**PL Pavol Loffay** 36:44 Why do we need a feature gate for it?
**Simon Olander (SAP)** 36:48 I thought that was mainly… to me, like, to me, I guess my… I don't know, like, I guess I'm a bit unsure about it. Like, I… to me, it seemed to be that this change I don't know, I guess my feeling was that this change was not there, like, this field didn't exist for a reason, and adding it… to me, you know, like, I guess some organizations, some people might not want to run the host PID as, like, to use that, and that's why I felt, like.
But then again, like, I'm also on the same page, like, I feel like, you know, if you're able to set the fields, then you probably can have the power to do it as well, right?
**Mikołaj Świątek** 37:27 Yeah, that's….
**PL Pavol Loffay** 37:28 I don't think we have feature guides that allow… or, like, that enable specific parts of the CR config. I think what's in the CR, it's, like, users are able to use it. I don't think we… We had such a case is when we disabled something from the CR with a feature gate.
**Simon Olander (SAP)** 37:47 Yeah, alright. No, but I can remove it, it's all… I was a bit unsure about it, what the kind of procedure would be to add new features like this, basically.
….
**PL Pavol Loffay** 38:00 maybe… I'm not an expert on this domain, but… the… like, does it conflict with any of the configuration that we have in the… on the collector CR?
Like, if they flipped on something else, would the… post-PID break, or vice versa.
**Simon Olander (SAP)** 38:28 You're asking me for my opinion.
**PL Pavol Loffay** 38:30 Yep.
**Simon Olander (SAP)** 38:31 I'm not sure. Like… If I would be honest, because, like.
this would allow you to access host processes, right? So it would be kind of, like, at least ID for it, but you would be able to make changes a bit more authorized and set capabilities for it.
**Mikołaj Świątek** 38:49 So there's, like, sorry.
**Simon Olander (SAP)** 38:52 No, go ahead.
**Mikołaj Świątek** 38:53 Part of the… another problem with the embedding this way is that normally when you create a pod, there's some amount of validation that happens for that pod, or pod, or pod template, whatever. So, for example, if host PID is mutually exclusive with something else, and you try to set both, and you try to create, like, a stateful set or deployment with that, the Kubernetes API server will tell you no.
Whereas for us, you create our CRD, and we don't have this validation, so then the time at which this runs into an error is during reconciliation, when we actually asynchronously try to start creating stuff.
And that's, like, a much less nicer user experience, because you don't get an error when you submit the thing. Instead, the error happens somewhere in the operator logs. Like, your stuff just doesn't work, and you have to go deep out and understand why it doesn't work. So that's something to maybe check.
of this? Like, is this… does this setting conflict with anything, and should we, in that case, reproduce that check?
I don't think so, I wouldn't expect so. Like, this just seems like some… this really just seems like a proxy for some feature of the underlying container runtime.
To be honest. So, it's probably… it's probably, like, not very sophisticated inside Kubernetes itself.
But it'll be nice to check.
**Simon Olander (SAP)** 40:25 Yeah, I can have a look at it and see if I can add it to the issue, maybe, if I find anything.
I guess one thing that I'm a bit… like, because I always felt that this was a little bit of, … how do I say it? Controversial change, because it is adding a bit more… like, the reason why I want to have it is because I want to run it more privileged, right? I want to be able to access more stuff.
So, I know that… in a way, right? But, like, in a way, like… I know that this is sometimes also checked for, you know, in case… like, to prevent… how do you call it, like, I guess… To make sure that pods or whatever deployments are basically not running in this way, like, has this field set in… for the same reason to not be able to run.
**Mikołaj Świątek** 41:08 To access the system you shouldn't be running.
**Simon Olander (SAP)** 41:10 Could that be an issue?
We don't care, this is just, like… Right.
**Mikołaj Świątek** 41:17 As long as we're not forcing it on users by default, you know… Right, right. It's your environment, it's your Kubernetes cluster, if you wanna… if you wanna let the hotel collector have some… You know, elevated privileges, that's up to you.
Sweet. We're not gonna… if Kubernetes lets you do it, then we'll let you do it.
**PL Pavol Loffay** 41:40 I think it can be a security concern for some people.
you know, that there is maybe a system administrator that, you know, manages the operator installation, and now users that are RASP leveraged could potentially have access to something that They shouldn't have access to.
**Mikołaj Świątek** 42:02 Yeah, but if they don't want this to be accessed, then they already should have, like, Kyverno blocking it on the policy level, and if Kyverno's blocking it, then the operator will not create it either, typically, right? It will just run into problems.
I mean, it'll just get rejected the same way everything is rejected, unless I guess, it's running as a more privileged user, but it really shouldn't.
But that's, like, you know, we're not gonna not add features.
**Simon Olander (SAP)** 42:33 Because sometimes.
**Mikołaj Świątek** 42:34 Somebody… somebody might… might want to disable these features.
**Simon Olander (SAP)** 42:42 I don't see… I don't really see any reason, and I don't really….
**Mikołaj Świątek** 42:49 Like… We definitely have not, … we definitely have not rejected anything in the past.
For this reason.
That it can be used, can be used irresponsibly.
**Simon Olander (SAP)** 43:07 Cool, alright.
Cool, cool.
**Mikołaj Świątek** 43:09 Now, if you told me that you wanted to set this automatically in some cases, then that would be a very different conversation, but just adding the option to the CRD is….
**Simon Olander (SAP)** 43:19 It's just an option, yeah.
**PL Pavol Loffay** 43:21 And….
**Mikołaj Świątek** 43:21 dramatic.
**PL Pavol Loffay** 43:22 I'm curious, is this required by any of the collector components?
**Simon Olander (SAP)** 43:27 So, the… that's, I guess, is the whole… shebang around it, right? Like, there is… the reason for why I want to have it is because, we're exploring the idea of, kind of ingesting audit logs.
This was also kind of… by coincidence, opened also in the collector, contrib… repository as an issue. Someone had an idea, like.
Wanted to have it, I guess.
more or less the same time as I was investigating this as well. But one of the key things to basically… they referenced, like, an elastic the RDP situation there, and the sample application there.
a deployment, rather. But in order to run this, you need to be able to have access to the host system.
So that's kind of the idea. So we're exploring the idea of using something like this to basically try to ingest audit logs.
**PL Pavol Loffay** 44:23 So, it's like your custom receiver for audit logs.
**Simon Olander (SAP)** 44:27 For the moment, and then, I guess, at some point, maybe it could be interesting to try to figure out how to make this happen as well, if this would be relevant as well, in terms of….
In the collector.
**PL Pavol Loffay** 44:38 Okay, I'm just thinking from the user experience perspective, like, if there is a component that requires it, maybe we should… you know, Do something to… … to make their life easier. That's… that's the kind of dope that… the point with the operator, we are trying to simplify the… deployment for the end user. There is many configuration options in many components, and, like, people don't know what to configure, what RBAC is needed, what they need to… how they need to deploy the collector, and what they need to enable.
**Simon Olander (SAP)** 45:15 But, like, I guess it's… the scope that I know is that it's more of a custom situation, right? To basically try to explore the situation and be able to set it, because it would not be possible at the moment.
I don't know how it will be for the existing components, like, like, parts of the collector, so I'm not sure how it… if it would increase or improve usability or something for the users, but… … But yeah.
**PL Pavol Loffay** 45:45 And does it make sense to only, kind of, A little bit on the… In the team onset mode.
**Simon Olander (SAP)** 45:58 It feels, in my opinion, that feels a bit strange to me, but I don't know the operator that well. Like… like, to me, it seems like if you would enable it for the component, wouldn't you enable it for all the different types of deployment… deploying that component? It feels strange for a user to maybe be able to do it in DemonSet, but not stable set.
and deployment.
Nope.
Like.
**Benedikt Bongartz** 46:23 The audit logs, we speak about Kubernetes audit logs from the control plane.
**Simon Olander (SAP)** 46:28 Yes.
**Benedikt Bongartz** 46:32 Hmm… would it make sense to have a separate… Custom resource for something like this, which just allows you to collect audit logs.
So technically, you can then have this enabled by default, if it's required, and separate this from the Open Talent Collector CRD in general, which then also allows you with RBAC, to split the permission so that the administrator can configure, for example, the audit log export.
While the user is typically not interested in this.
There was also a discussion for this, … Anthony started this, I guess, somewhere.
To have a separate custom resource, which simplifies the entire… Collector configuration.
So it should set up a bit more and abstract a bit more. And I guess this could be a use case where you have maybe a platform section, platform audit logs, and you can just enable this.
And, that's the only way how your privilege gets enhanced compared to other use cases, so you cannot really abuse this at the end.
**Simon Olander (SAP)** 47:48 But why, why… But… but… Yeah, like, like, I get the… I see what you mean, but would you then call it, like, audit log? Wouldn't it then be more… make sense to make… call it some kind of, like, more privileged collector or something? Like, has more… Or, I don't know.
Like, cause I feel like it's… like, for my use case, it makes sense to have audit logs, right? But I feel like adding more ability for it would make sense from a, maybe.
Other use cases for Lindy, I don't know.
**Benedikt Bongartz** 48:18 Yeah, what I was looking for is… Give me one second… I think to have this more or less managed, there is, … This, if you're here, I put it to the document, and maybe you can open this.
Oh, I need blood.
Make a link out of it.
Or notes.
So there was this discussion to have a managed custom resource, and if this is really for one specific use case, so that you need to access the audit logs on the control plane nodes.
This might be something which can be done in the managed custom resource.
So that you just go, for example, to the log section, or the… I don't know how it's structured at the end. The platform section, and then you go to, and enable audit log export.
And technically, we could also then directly configure something like an audit lock receiver.
if this is generic and works, for example, on OpenShift, AKS, and so on.
So that way, nobody can set a specific ID, override something, abuse it, It's just hidden.
**Simon Olander (SAP)** 49:59 It's, yeah, like, it's, it, it changes… Yeah, like, it just moves, basically, the choice to run its privilege to a different level, right? Instead of having it in… Literally in the field.
**Benedikt Bongartz** 50:12 Everything's privileged, you can only run the audit log specific parts privileged.
In that case. Because you don't have access to the underlying parts.
**Simon Olander (SAP)** 50:23 Okay, Yeah? Like, like, I don't know, like, to me, it sounds like it… I feel like I'm not an authority to make a decision, like, like, make… say something here, I don't know, like, it feels… To me, that it could make sense.
**Benedikt Bongartz** 50:45 It was also just a random thought, so it… it's not that I have their stumb opinion, it was just that I thought that May fits in so that technically have a CRD afterwards, like, … Where you have your config, and inside you have… I don't know.
**Simon Olander (SAP)** 51:04 Boom.
**Benedikt Bongartz** 51:06 And then locks… metrics… Traces, or whatever.
And then you can have specific configurations while… Having then also, … I don't know what to pick here.
applications, and… Instrumentation, and here would then also have locks, and then you can go here for… Audit… enablers.
And then the rest will be done, and the operator will take care of Giving it permission if needed, configuring it depending on the environment where you're in, something like this.
**Simon Olander (SAP)** 51:55 Right, right.
**Benedikt Bongartz** 51:59 And here you have maybe done a selector.
For, maybe space, ABC….
**Simon Olander (SAP)** 52:09 Right, right, yeah.
to me, it sounds like a reasonable idea. I guess the question is, I would have to look into what… I don't know what the idea here is with the management, but… Yeah, like… Because I guess, like, setting the RBAC and setting the permissions for accessing the things are quite… Well, by user experience would be a lot easier to just be able to enable it, and then you have access to it, so….
**Benedikt Bongartz** 52:38 Yeah, I was thinking about, because it's such a really specific case in that sense, so that, yeah.
**Simon Olander (SAP)** 52:44 I guess it is true, if you look at it from that perspective, right? Like, it could be that….
**Benedikt Bongartz** 52:49 the other components?
**Simon Olander (SAP)** 52:51 doesn't necessarily need to have access to, the host PD. And again, any… I'm not super familiar with all of them, but what kind of… components in the collector, for instance, uses, … By the top of her head, like, basically has to access some kind of security context and have some capabilities for accessing stuff.
Are there anything that… Quite obvious, needs to have it.
**Benedikt Bongartz** 53:18 No clue. So I don't know what the host metrics thing, depending on some metrics, I guess? I don't know, but that's just a guess.
**Simon Olander (SAP)** 53:30 Yeah.
Because that is something I also said in the… with the audit situation, right? I have to set some certain capabilities to access it.
So… Yeah.
Okay, I'm not sure what we do for running it off here, getting close to the end, but, … Should we continue that issue to try to figure it out, or what do you feel like?
To try to discuss it. I can try to figure out something and see how it could work as well.
Diar.
**PL Pavol Loffay** 54:04 Yeah, I guess maybe, a workaround, if this is controversial to be added to the CR, could be, like, you could deploy Run a deployment, and then maybe inject the collector as a sidecar.
And the pod already has the host PID enabled.
**Benedikt Bongartz** 54:30 Maybe I misunderstood, but doesn't need to process the ID, too?
**PL Pavol Loffay** 54:42 If that makes sense, I'm not sure.
**Simon Olander (SAP)** 54:45 I'm not sure either, but… I don't know, I don't know.
**PL Pavol Loffay** 54:58 It's set on the pod level, right, not on the container.
**Simon Olander (SAP)** 55:03 Yes.
**PL Pavol Loffay** 55:05 Yeah, so you would have a pod that already has it, and then you would inject the collector as an additional container on that pod. It would inherit the security settings.
**Simon Olander (SAP)** 55:23 I guess that is an option, as well.
I could try it out and see, I guess.
Yeah.
Okay, to put up this….
**Benedikt Bongartz** 55:36 This makes sense.
**Simon Olander (SAP)** 55:38 I can try it out and see how that works, right?
And then add it to the issue, maybe, to see… Let me write it down, maybe, so I have an idea. So… try to do… run it as a deployment, and then sidecar it, inject it as a sidecar.
**PL Pavol Loffay** 55:53 Yep.
**Benedikt Bongartz** 56:07 I guess the proposal would then look like… This, and then just the sidecar annotation on top.
Oop.
try it out. See?
Tim.
**Simon Olander (SAP)** 56:36 Cool, cool, cool.
All right? Well, I'll try it out, and, report back, see what happens.
Other than that, no.
Thanks for the input.
**PL Pavol Loffay** 57:16 Yeah, thank you, Simon. I need to run anyways. Thank you guys, bye.
**Simon Olander (SAP)** 57:20 Bye-bye.
**Benedikt Bongartz** 57:21 Goodbye.
