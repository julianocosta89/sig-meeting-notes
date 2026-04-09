SIG: Semantic Convention Tooling
Date: 2026-04-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Laurent Querel 00:02:26 It would win.
Arthur Silva Sens 00:02:30 Hello, hello.
Josh Suereth 00:04:16 Hey, folks.
Laurent Querel 00:04:20 Understood.
Arthur Silva Sens 00:04:21 Hello.
Josh Suereth 00:04:22 Sorry I'm a little late, it's been quite a while. How y'all doing?
Arthur Silva Sens 00:04:28 Pretty good, how are you?
Laurent Querel 00:04:28 good.
Josh Suereth 00:04:30 Pretty good, pretty good.
Ugh.
We, I'm… got totally bogged down on this Provenance stuff for Weaver, and I'm in, like, a rabbit hole that I want to talk about later.
Yeah.
Folks, fill out your topics.
Arthur Silva Sens 00:04:53 I have the first one, I… This is mostly, like, a temperature check?
about… getting Weaver Life Check, as part of the collector.
Like, we don't know yet how, but we've been discussing, like… Let me, let me start again, like, This idea came up a few times, because Collector wants to validate the telemetry that it produces.
Yeah, so Ariana made a prototype where… She built a library that spins up Weaver with test containers.
And then the collector can validate its metrics, Using a Weaver container.
then Josh… create another prototype on top of Adiana's prototype.
with WASM?
And I'm now thinking, hey, I would love to get this in production, actually, not just as a CI step. I would love to have a component in Collector.
Whereas part of the pipeline, can validate telemetry and emit OTLP locks, into… back into the pipeline, so I get real… real-time alerts when… Talian trees violating any of my policies.
So I… Yeah, so my approach, I would actually rewrite Live check in goal.
So it… In the collector.
Like, how do you all feel about this? Like, does any of those ideas is already, like, a red flag for you, or anything looks exciting?
How do you feel?
Josh Suereth 00:07:03 I'll say one thing quickly, which is, the whole goal of having the YAML Schemas is so that if you wanted to use a different language to do something.
You should be able to.
However.
Then there's the, like, health of the ecosystem, and, like, should we maintain two things that do the same thing? Yeah, so, I'm gonna, like, save maybe 10 minutes of ranting about how I think Go just does not have a good plugin story, and it annoys the crap out of me. They make it as hard as possible for you to use anything with Go, and I think that is just bad.
but… Yeah, it'd be good if we can figure out how to share.
I think would be my take. Like, if we're gonna put, like, priorities on, like, goals, I think having it in the collector is a great goal.
As something that people can opt into using.
Or having it in your collector architecture, whatever that means, right?
I do… if the collector had a plugin ecosystem of some sort that made sense, that was not bundle everything into the binary, I'd prefer that, personally.
I think the current, like, binary bloat is significant.
And it… it is something that kind of… is in the back of my mind all the time. It's actually something we chase a lot of.
Internally. Of, like, trying to optimize these collector images.
Arthur Silva Sens 00:08:42 Yeah, by large size.
Josh Suereth 00:08:44 Yeah. Anyway, there's hands, so I'll stop and let others say things, but, like, in terms of priorities, I think they're good goals, is what I would say. Figuring out the details is gonna be fun.
Laurent Querel 00:09:01 So, this idea of having Weaver into a collector is, definitively, Something, we have in mind, for a long time.
And I… the scenario that… or the use case that you described is, a perfectly valid, in my opinion, valid, scenario.
the reason why I'm not so, I should say, at all active on Weiver currently is because I'm working on a new engine named Dataflow Engine, or OTAP Dataflow Engine, which is part of the Otero project.
And the reason why I'm mentioning that is… It's basically a collection of libraries, both in Rust.
To recreate, a collector.
And, and the idea was to leverage an element of river when we can.
In some aspect of this system.
That's what we are already doing.
Not for the live check, but for the emit.
So we… we use, Weaver and, some, some libraries of Weaver.
And, similar to coin shouldn't to generate traffic.
In a smart way.
Instead of doing just, the Basic Classic, static generation of signal, we just leverage the semantic convention to generate personatically correct.
Traffic of metrics, logs, and spam.
the next step was to integrate LiveCheck. The reason why we didn't, integrates with her yet for that is… We want to make it, very efficient.
And, and not, So, I need to go deeper to explain why it's not efficient in the way that it is.
This OTAP with a OTAP data flow engine is based on… Apache Arrow, so a way to represent, Open telemetry object in a columnar way.
And the reason is to get a better compression rate for the protocol, but more importantly, To get, A better way to process data internally, in memory, online.
If you are familiar with things like Data Fusion, or ClickIOs, or this kind of stuff.
They are all leveraging, columnar-oriented representation to accelerate.
and leverage, with a special instruction set, like CMD instruction set.
To, to accelerate the, the letter processing.
So… With our light check, we'll have to process columnar-oriented data in order to… To leverage this, acceleration.
So we can't use directly, unfortunately, in that case.
the live check into the… this data flow engine.
We were able to do that for EMIT, because for EMIT, it's less critical. It's… so first, it's not necessarily inline, it's more… we create a receiver that will generate autograph object.
That will be automatically converted into Apache R, because we have this capability.
But, in the case of, Weaver Life Check, we will have to covert OTAC to protobuf.
Checking the protobuf and converting back, Or maybe not converting back, but just, we have this, conversion that will, take a significant amount. So that's something we could do, as, just a proof of concept.
That probably will not be good enough to be, in production, especially when it's a very heavy production. If it's, I think even the level of Go… what the GoCollector is able to achieve, that will be okay, because we are 2, 3, sometimes 4 times faster than the GoCollector already.
But, in order to provide something that will be As fast as all the other processors that we support, we will have to work much more.
So sorry for the long answer, but definitively super interesting.
That's something on which we are usually, thinking for a long time, and I just explained why we didn't, but, And by the way, Joshua is part of this project.
Joshua McDonald.
I don't know, I see, GMACD here, so combined.
Arthur Silva Sens 00:14:31 Yeah.
ariannavespri 00:14:32 Can I… can I say something? Can I say something? Sorry for, for, being a bit late, I was in another meeting. So, what I'm reading here in the agenda, we were, like, checking the collector. My… My prototype, which is Braden and my prototype, is not in the collector. We don't… do not leverage, we were, like, checking the collector. I saw your, your reviews, Arthur, but there are some misunderstandings there, and I'm, and I'm, as soon as I can, I'm gonna… you know, I'm gonna reply to them, it's just that there are other people also who are… you know, that also, like, made some reviews, and I have to do things in order, and there are still, like, some things there that are, like, moving, and and also, like, thank you, Jeremy, because we, we adopted your suggestion about, I tagged, I don't know if you had the time to see that, but basically, we switched completely away from the… file, you know, the file, storing approach, so the mounting, the file and everything. Now, you know, we, we, leveraged the stop and point the way that the, the, the latest version of, of Weaver.
you know, actually, enables us to do so. So… in the response, basically, the byte payload in the response. So, thank you very much.
Arthur Silva Sens 00:15:58 Lynn Miller has a… yeah, thanks for clarifying, Adiana.
Ludmila?
Liudmila Molkova 00:16:06 Yeah, I was thinking that you're calling out my cats from on your cat's behalf.
Anyway, so I think this is a very, very cool, approach for the emission, like.
I would imagine that Weaver LifeCheck… that the Viver Life Check runs in CI, But if you want to, like, continuously monitor your telemetry, then it's natural to have something in the collector.
that, I don't know, alerts if, sends something that you can alert on if it discovers broken telemetry old versions, or you can, essentially make it part of your continuous checks.
So… It sounds like, we cannot just take life check as is, because if it translated to collector.
It would mean we need a receiver, a processor, and then export… well, some parts… that forwards to exporter. So there are parts… like, if we do it right, the parts in the collector have intersection.
But it's essentially a set of policies that we also made language agnostic.
and a set of models that we express in JSON… sorry.
It's just Prata model, yeah, yeah, so we… like, everything we have externally is language agnostic, and I think there is a use case in the Go Collector, just because it's so easy for people then to set up continuous Checks, but it's a subset.
And I don't think they are… I can see why both can exist, they just serve two different purposes.
Arthur Silva Sens 00:18:03 Yeah.
I can see that the group is… Generally excited about the idea, just the implementation.
looks… fuzzy right now. We don't know how to proceed. I think this is… Good enough for the discussion for today.
ariannavespri 00:18:23 Actually, I know how to proceed for myself, if you allow me. I mean, this is an issue that has been assigned to me that I've been working on for some months, so… and also, what, you know, what our PR, mine and Braden's kind of, like, targets, is the, it's not, like, whatever service is, like, the components That are, you know, it's the telemetry of the components, which are, of course, written in Go. And so this is, like, a package for tests, and so it's not, like, trying to solve, like, it's not trying to offer, like, a solution that could hold for… whatever service, you know, so it's very specific, it's very… it's very, like, scoped, so, it has its own… it has its own scope, you know what I mean?
Arthur Silva Sens 00:19:13 Yeah, yeah, yeah. What I meant was not about your PR. Like, we are not discussing your PR. Your PR is good, and we should proceed, and the discussions can happen there. Like, we are not.
ariannavespri 00:19:25 Yeah, yeah, okay.
Yes, yes, that's not what I said, it's just that, you know, it's my fault that I came a little bit late, and I'm just, you know, the context that I have is, of course, like, a list here, where everything is a bit conflated together, so I'm just trying to give context and to get context for myself.
And there is a plan there that has been going on for some time. So, I just want to say that on my side, I don't have much uncertainties.
But, of course, you know, I'm, I'm happy to see this conversation going, of course.
Laurent Querel 00:20:03 Yeah. So, I don't know if I understand well, What you are… what you want to achieve, or what you are… on which you are working, is basically the standard way of validating The instrumentation of the collector with Weaver.
ariannavespri 00:20:21 Yeah, exactly. So it's basically really, like, a very, very narrow and internal kind of thing. Then, of course, you know, could be an inspiration for other, for other things, but right now, I mean, the issue was about that, and And so it was very, like, basically, you know, once that PR is done, then we are already, like, discussing, okay, what could be the first adopter? What could be the first component that could actually adopt this package when the… and include it when they taste the things, you know?
And there are… of course, there are infinite candidates who are, like, trying to narrow down, you know, what could be, like, the… the first guinea pigs, I don't know how to explain.
Arthur Silva Sens 00:21:03 But…
ariannavespri 00:21:05 So it's very, it's very widely scoped, and sorry, it's very narrowed scope, and we already have, you know, some conversation going on in that sense. A lot of things are not surfaced in the PR, in the PR description. The PR description is also, like.
It's like, it's the original one of when the PR was the draft?
But what is still valid there is, like, the steps. So the steps… the PR is the first step, and then, of course, the second step is having the package adopted once it's, like, accepted and approved. Of course, I cannot have in the same PR the package and the adoption of the package.
You know, so… That's it.
Laurent Querel 00:21:46 And, you're talking about the Pierre 46 315?
Or a different one.
ariannavespri 00:21:56 Let me check, because I have to open the…
Laurent Querel 00:21:59 Yeah.
ariannavespri 00:21:59 So the PR is 463115, yes.
Laurent Querel 00:22:02 Yeah, so the… Okay, and and you will, at some point, generate, Semantic correction, specifically, for the collector.
ariannavespri 00:22:16 I mean, it's for the… it's for the components, so… it's like… you know, this is something built on top of Braden prototype, we are discussing that, but it's, like, for the different, for the different components.
Laurent Querel 00:22:31 Yeah, but, in the approach, will you, Enable… authorized people to create their own semantic correction for their components, so they can specify the… So we could live check not only the regular attribute and matrix, but also the custom one.
ariannavespri 00:22:53 But also, sorry?
The custom…
Laurent Querel 00:22:55 Son, yes.
ariannavespri 00:22:57 You are catching me unprepared right now, I don't remember.
Laurent Querel 00:23:02 Okay.
Because, so I copy-passed a link into the, The chat.
We, we, I think we, we didn't start. We are also working on something similar on our, on our, on our side, not related to the GoCollector.
But we definitively want to… do exactly what you are saying, checking the instrumentation of this data flow engine, with Weaver, in the CI pipeline.
And for that, we will have to… To create our own registry.
Leveraging the, the recent, ASCIVA V2, and all the stuff that has been done recently by the team.
To, yeah, to properly check And not only the one coming from OpenTelemetry, semantic convention, the standard registry.
ariannavespri 00:24:10 Maybe Jeremy wanted to say something.
Jeremy Blythe 00:24:14 Oh yeah, sorry.
I guess the, I think we had some debate when we were first starting.
live check about, is this a thing that goes in the collector? And then we went, oh no, we'll make it have a collector inside it, kinda.
So that's what we've got.
The thing that worries me now?
is… I just worry about having two lots of code that are doing the same thing. I think this is what you said, Josh.
It's… it's enough work to maintain at once.
maintain it twice, and then have it… have them so they're consistent, they're not diverging from each other, they're not… because you're… you're gonna want… the same expectation.
You're gonna expect the same outcomes if you're… using it within Weaver or in the collector, right? So… I guess, that's my concern.
Anyway.
I like the idea, I just… how do we do it cleanly, I think, is the thing.
Liudmila Molkova 00:25:23 beyond just definitions, model definitions, what else is shared, actually?
The, the, like, the checks for… that are embedded?
Probably yes, but policies can be completely share it.
So I think the only important piece that… that would be… would go out of sync is… is the… embedded checks.
Laurent Querel 00:25:55 Yeah, totally agree. The point of this, of using policy, rego policies in river, and not only for the weaver check, but also for the life check, to some extent.
was exactly that, being able to express, policies, in an independent way, and in a dynamic way. Also, solving the other problem that we have with Go, that mentioned, Josh.
The inability to, so the no-plug-in, aspect of Go, is… In some way, solve with this approach?
Jeremy Blythe 00:26:45 Would I want to write my policy once?
And use the same policy in the collector and in Weaver, without having to change it.
Laurent Querel 00:26:54 Yeah, because.
Jeremy Blythe 00:26:54 The policies are directly linked to the input and output structures, which is… So then, what the policy reads at the moment is the… the data structure of samples, which is an intermediary that's invented in the Weaver codebase. So in terms of things that are the… things that are sticky that would then have to come across, it's not… If you don't mind writing your policies again.
So you have two sets of policies to use it in either place, then, sure. But that seems like a shame.
Liudmila Molkova 00:27:25 Hawaii.
Laurent Querel 00:27:26 I think we can use the simplicity.
Liudmila Molkova 00:27:29 Oh, go ahead, Torin.
Laurent Querel 00:27:30 No, sorry, Brandon.
I was just saying that I think we don't have to change the input-output, and we, We can just reuse the same policies.
Josh Suereth 00:27:42 Yeah.
Laurent Querel 00:27:43 that are externalizing and regulating.
Josh Suereth 00:27:46 Right, so Jeremy, I think right now, technically, the Weaver sample structure is public, because you use it in the REGO policy.
So, what I think we're saying is we would document that schema more, if we haven't already. We'd have it, like, as a JSON schema dump, and then if Go uses the same schema for their sampling technique.
they should be able to reuse the same REGO policies, right? Yeah.
Jeremy Blythe 00:28:13 The go would have to re… rework the sample, like, the OTLP to sample conversion.
Josh Suereth 00:28:20 Yes, they would have to build up.
Jeremy Blythe 00:28:21 I have to stay in step.
Josh Suereth 00:28:23 Right. But, like, that interface, we shouldn't be changing significantly or breaking.
In the long run.
So, one thing we could say, though, is, I want to put a pin on this, by the way, in the next minute, so we can move on. It's been 30 minutes. But we could say, and you can tell me if this is true, Jeremy, if you think that interface is going to be changing Over the next… You know, ear.
Significantly, or in ways that might break, where having two implementations is problematic, then we should say, hold off on re-implementing and go.
Because we're actually going to be changing that interface, and you're gonna… we don't want to go through breaking changes in two places. But if that… if that interface is relatively stable, and we don't expect much change to it, I think it's fine to say, if you have enough bandwidth on your side in open source.
go build against the spec. Like, it's specified, as long as the Rico policies can be reused, and it's clear what that should look like, we shouldn't have a problem. That's the, like, again, that's OpenTelemetry's philosophy. If we have clear interfaces, like OTLP, the protocol, right?
or the specification for APIs and SDKs.
We don't care who implements it, as long as you're up to spec.
Jeremy Blythe 00:29:36 Oh yeah, totally, totally agree. I just think it's… It is not as simple as… It seems at face value as well, that that's…
Josh Suereth 00:29:45 No, I… yeah.
Jeremy Blythe 00:29:46 Warning, this is a little deeper than just, Maybe that's how it seems.
But yeah, totally agree, and I think it would be… it would be awesome to see, but… needs a bit of careful thought. The only thing I can think… sorry, I know we want to move on. The only thing I can think immediately that we need to tackle is, entities. We haven't done entities, right? And there's actually an issue, it's been… Someone submitted an issue about it as well.
I think the guy from Dasho But, yeah, we don't have good… We now have a good story around, live check for entities.
Laurent Querel 00:30:25 what I can offer, and I will not spend more than 2 minutes on that, Josh, but what I can offer is, Helping someone, To do this integration into the, the Rosetta flu?
Because the work will be much smaller.
We could imagine a first version that is not as efficient as what I was thinking initially, so we will introduce this, conversion OTAP to OTLP, and then we will be back to basically what, Weaver is consuming for live check. So the… the integration will be really minimal, and it's full ROS code, so there is no rewrites to do at all.
So, I can either try to do it, or, which is possible, not necessarily in the following days, but in the following, one, two weeks.
Or I can help someone to, to welcome that.
Josh Suereth 00:31:31 Yeah, I… I mean… Going back to Arthur, I think we… you… I'll say this, I don't think we're going to make a ton of actual decisions here. I think we're exploring the space. So, I don't want to sit here until we come up to a decision, because I don't… like, that means we're not going to get time for the other agenda items. So what I'd say is, Arthur, I think you were asking, like, how do we all feel pulse check?
hopefully you have enough information now to follow up, know who to talk to, and know what to do. I think Arthur had to drop.
So, we're no longer, like, even talking to the person who was making the proposals, right? So, I'd like to move on. This is recorded, but yeah, just for context, like, I think Arthur hopefully has enough to move on.
Cool. Let's, let's go on through the agenda. Jeremy, I'm gonna move yours up to the top, actually, because I think this is kind of an important one. We have a PR that got dropped.
And basically, this was, about having auth token.
And there was some open discussion on this.
Sent some feedback.
And then, I think it just closed 3 weeks ago.
so… Jeremy, you need authorization now for your local.
Jeremy Blythe 00:32:59 So… Yeah, so I was, exploring the packaging, publishing.
And I got it to work, because the way Weaver works at the moment is, if you put a URL The… Today, it assumes, if you give it a URL that doesn't end in .zip.
I think. Then it… it takes that as a GitHub.
repo, and then I added that small thing so that you can enable what's it called? The thing so it can use your security helpers. So then you can pull from a private repo. So that gives us a flow of, I can publish… I can publish in a way provided that what I'm publishing is, like, committed.
What I'd like to be do… what I'd like to do is… Have it so that actually it's an artifact of a build.
And so then I'm pulling something that is a zip, but that's not going through GitHub security, right? That's just going, this is a published… this is a published thing, but now it's internal.
So there's kind of… anyway.
So then I'm like, oh, well, maybe I could put this on one of our, One of our servers in the company that provided your, you know.
in the company, you can access this server and have an HTTP server, but now Weaver can't get from there, and how do I do the… how do I do the security? And so the… basically, the publishing… Publishing story is not complete, I think, unless we have something like this.
To allow us to go and fetch what we need to fetch from various hosted places.
Basically.
And I feel like this… PR was heading in the right direction, but… I guess the guy, whoever that was, closed it, because… I don't know.
We took our eye off that one for too long.
Josh Suereth 00:35:00 Yeah, yeah, I think we… we ended up not giving the feedback we wanted. I know we talked about it, and there was discussion about how, like, adding the bear string was problematic in some way, like, just that, but I think we need to… we need to get something here.
Jeremy Blythe 00:35:14 It may not be the… it's not the… It might not be the right PR at all, it might not be the right way to do it at all, but conceptually.
Especially now with the packaging.
Josh Suereth 00:35:24 Yeah.
Jeremy Blythe 00:35:25 We wanted to…
Josh Suereth 00:35:25 Conflict-wise, by the way, we broke the crap out of this with, some of the changes we made, if I remember right.
Jeremy Blythe 00:35:32 No doubt.
Josh Suereth 00:35:33 Yeah.
And the PR author also was like, I'm not sure if this is the right thing to do.
Jeremy Blythe 00:35:46 Again, it's fine that it's closed, it's just… It was that idea. That is still a problem that we need to solve, so I don't know if we want to… Have an issue or something to track it for the project, or… .
Josh Suereth 00:36:02 Yeah, let's open an issue, and let's, I think if you have time to try to solve it, since you're using it in a way that, like, would need a solution, that'd be ideal.
Jeremy Blythe 00:36:15 Yeah, so… We have, like, we have a shed… Company repository… in, GitHub.
It's obviously all private.
Loads of people contribute to that, like the SemConf project.
In OTEL, but it's internal in the company.
And then we have a release, and when we do a release, we want to make an artifact, and the artifact can now be the package.
Which is, like, awesome.
But now no one can really get it, apart from it being a bit awkward. So that… I'm just trying to solve that.
Josh Suereth 00:36:45 Yeah, like, it'd be… it'd be nice if we could have one of these things with a zip in it, and you get that.
Jeremy Blythe 00:36:50 Right, yeah.
Josh Suereth 00:36:52 Yeah.
Okay.
Yeah, yeah, so I think, basically, TLDR is… I don't know if that PR was 100% right, but we should open a bug and try to make progress on it.
And I'll put it into consider for next release if you open the issue.
Jeremy Blythe 00:37:12 Yeah, we'll do.
Josh Suereth 00:37:13 Okay.
Cool. I want to talk about Providence, lineage, and next steps.
Quick thank you, Lyudmila, for reviewing this PR.
But basically, what this does is what we talked about a few weeks ago, before KubeCon. Basically, we now track schema URL, Of attributes and groups.
Or, well, signals, through the whole system.
I did one really ugly thing.
that I… am only okay with because V1 is going to go away, and you shouldn't use V2 and V1 together.
But Lyudmila caught it and, like, made appropriate comments about it being slightly ugly. I'll show you what that is. This only does resolve schema. This doesn't impact Forge yet.
So, with that caveat that you can't actually access schema URL in Forge, and you can't access, kind of, groups and provenance in Forge, what this does is basically add provenance. Let me see… Providence tracking core. The big difference is we add provenance.
Instead of lineage, to attribute.
So this is on, I think, yeah, this is on pub struct attribute. We add provenance, then, to all the signals, attribute group, entity, etc. Provenance in V2, is… Where does it show me… that's… not what we want.
Providence is optionally a dependency ref.
Which is an integer that links to the dependency list.
In the schema?
Or… It is a string that we keep locally to track, like, what groups specific things came from.
Right. So, you know how we tend to track locally, like, this attribute came from this attribute group, that kind of thing?
It is also used there locally for debug messages. Or, sorry, this is… this is… sorry, this is the file path.
We track the file path for debug messages, so if you need to say, hey, this thing defined in this file is bad, you can do it there. If we want to expand this to be, like, a span as well, to say, this file, this line of code, that kind of crap, like, we could do that.
So that's what Providence is in V2.
And this is not serialized, so that, the only thing that is serialized is a dependency thing. If you want to see examples of what this looks like.
Are you… can you… What's this? Oh yeah, here. So here's an example. Providence source is 0.
And then, if we were to look at the expected schema, where's the expand button?
Did I… do I have to look at the whole file? Oh yeah, here. Dependencies, you know, this is the dependency, and so anytime it says source 0, you know it came from the dependency.
It is not serialized when it's not needed.
That's the TLDR. Go ahead, Lauren.
Laurent Querel 00:40:22 Yeah, the, the… the string? Why a string and not, RCSTR, or, a quote, because that will be something that will be so much replicated, and just… Trying to understand why it's a string. It's a… it's a replacement.
Yeah, the pass or something like that, that you have into your script.
Close to the… in the Provenon Street, you have.
Josh Suereth 00:40:53 Oh, when we're tracking the file name.
Laurent Querel 00:40:56 Yes, so why are you straying? That looks like a particular inefficient.
Josh Suereth 00:41:01 Previously. Like, Laurent, we're tracking it as a string today. I just kept what was there today. In V1, it's a string. In V2, it's a string. If you wanted to know… spring, which I think it shouldn't be, that would be great, but it's spring today. Yeah.
Laurent Querel 00:41:14 Oh, I'm surprised. Okay.
Josh Suereth 00:41:16 Yeah.
Laurent Querel 00:41:17 Yeah, that's definitely not, that should not be a string.
I kid.
Josh Suereth 00:41:21 Okay. Yeah, we… and we can… we can change it in the future, again, that's fine. It's just, yeah, I… I… That's… that's why it is like it is now.
Laurent Querel 00:41:33 Okay.
Josh Suereth 00:41:33 Yeah.
So… Because, like, previously, we were tracking path as a string in lineage.
And I'm not keeping path when we, when we go through, but path was a string previously.
Laurent Querel 00:41:49 Okay.
Josh Suereth 00:41:52 Oh yeah, and here's what… if you want to see the ugly thing I did, I know what file it's in, is it in the… where is it gonna… maybe I'll just go to all files.
This is where I'm failing at my AI-ness. Sorry, guys. You'd think I'd be better at AI. Alright, I think it's in here.
To round-trip these things through, to… to round trip it, through V1 schema.
I am making… because attribute lineage, we weren't tracking schema URL through, but what I do is I invent a fake group.
ID called V2 something, and then I shove the schema mural in it, and then extract it later. And Lamela's like, this is really gross, could you actually not do that? Well, I can't unless I break V1 schema and add a bunch of extra crap to it.
So… I'd like to keep that if that's possible, even though it's gross, and I agree, it's gross. What do you think?
Laurent Querel 00:42:57 Bye.
Liudmila Molkova 00:42:58 I'm glad to get away with it.
For now.
Josh Suereth 00:43:02 Okay, okay.
It does show up in tests where you are resolving V2 into V1 schema and outputting it that way, which I'm… again, I'm under the assumption that, like, we're going to have a… you're either wholly in V1, or you're in a V2 world that can resolve V1 schemas.
And so, it will never show up, because your output will be V2.
Alright, cool.
The next step here is actually, whether or not we need anything else that… oh, oh, so, there's two next steps. Next step number one is, what do we need in Weaver Forge?
To represent these? Like, do we just put the, Providence Schema URL in WeaverForge straight up as is?
It turns out V2 didn't have the, source files either, which I think is somewhat important for doing error messages out of, templates, so I think we need to add that in for… so, in WeaverForge, I would actually include source and have it be serialized, where it's not serialized today for Resolve schema.
The second thing to follow up on is then, is there anything else we need for providence tracking?
Outside of just the dependency it came from.
Liudmila Molkova 00:44:28 And we can start with that. I think the only problem I remember is that, yeah, we don't know where the… Something came from in the forge schema.
But we can always add things.
Later.
Josh Suereth 00:44:53 That's… that's actually kind of what… what I'm asking, is like, I… I think it's actually reasonable for us to add things later, in the sense of, if I know the dependency, I can actually infer what group it came from.
I can infer back to the file it came from, but I also don't need to care, because we're actually depending on dependencies, right?
Liudmila Molkova 00:45:19 Oh, if you don't have a dependency definition, if you only have dependency resolved, you have no… Waste to… No, unless we publish.
Forge schema for everything.
Josh Suereth 00:45:33 Unless we publish it, right? Which is why I'm thinking, like, to some extent.
we're basically saying that doesn't matter anymore, because you're depending on a resolved thing, and it doesn't matter what the source file was. And if we needed to, we could actually find the definition and track it that way.
Or open a bug against, you know.
I'm trying to think of where this would actually be used when we have published schemas. Are you going to need to go all the way back?
Liudmila Molkova 00:46:02 I mentioned for the good error messages, we would publish.
Like, like, symbols.
Josh Suereth 00:46:13 Eventually.
Poss… possibly? Possibly? Maybe that would be an external thing? I don't… yeah, okay.
I'm trying to figure out if we have a one-way door.
Liudmila Molkova 00:46:29 I mean, with publishing resolved schema, it's a one-way door, right? Unless we want to double-publish something else, too. But it's a good one door. We want… That one door for the… being optimal.
Josh Suereth 00:46:44 Yeah.
some information here, of course.
Yep, okay.
And then for Weaver Forge, basically, we're gonna add, make sure it's unit URL… Show up. Okay.
Cool. So, once this PR gets, approvals and merged, I'll start working on the WeaverForge stuff next, and then I think we're gonna call… provenance tracking done for V2, enough for, like, launch ready?
Sound good?
Cool.
Alright, this is an FYI, thank you, Ariana, for commenting on the broken build of Weaver pa- apparently Weaver Packages was broken for a while.
ariannavespri 00:47:36 Hmm.
Josh Suereth 00:47:37 when we updated Weaver.
So, the fix is in. Please take a look, review, approve.
ariannavespri 00:47:43 Yes, yes.
Josh Suereth 00:47:47 Yeah, this should fix everything for you, but, I was a little bit aggressive with my, regex.
Because I don't want to have to fix it again.
ariannavespri 00:47:59 Makes sense.
Josh Suereth 00:48:01 Okay.
ariannavespri 00:48:03 I mean, right now, what I… right now, what I'm working on is simply, like, that t-shirt that I… that I posted, so it's, like, building on… on what Lumila used for her… for her demo, and so trying to… to get into Weaver packages, basically the DMD, the Markdown templates.
So I'm, like, trying to do a combination of what Lunmila did and what I had originally done, of course, with the V2 version, like, and I have a question.
It's really, like, a general question. When you, when you, you know, When it comes to testing.
do you think it's a better approach in general to, like, maybe have some inconsistency across the way you test the different things? Like, I don't know, like, metrics, or attributes or entities, for example?
But having less repetition.
Or is it preferable as, like, your guideline in general to have, like, everything really consistent, even though you have more repetition.
I know it's an abstract question.
Josh Suereth 00:49:10 No, no, no, yeah, yeah, yeah. I… I was… this was my fear in making the testing system, was should we have, like, God tests, where we do a whole bunch in one test? Or do we have individual tests with lots of repetition, but they only test one thing?
Yeah. Yeah.
ariannavespri 00:49:28 So because…
Josh Suereth 00:49:29 I would blend it, is what I would recommend. Like, I use your judgment here, but if you look at what I did for some of the policies, I tried to keep them independent when I could get an agent to do the right thing, and I didn't have to type it all myself, where I made the test.
I did slightly larger grouped tests.
ariannavespri 00:49:50 Yeah, so basically what I was trying to do, because, like, the difference between, in content, let's say, between what I had originally added to Weaver in… as, MD templates, and, what Lumila did in her, in her repo is that entities are missing.
So, if I had just everything but entities, I could just have, like.
you know, kind of concentrate everything without repeating the attributes everywhere, let's say.
And that would work no problem, okay? It's just, like, a concentrated kind of thing, like, referencing them just once. But with entities, I… I am not able to explain exactly why, but it doesn't work unless I put, like, a sort of filter, also.
Sorry, yeah, sort of filter. So keeping, like, the, the other four, with, just one, one.
just the attributes for all of them, and and then having, like, this filter that if, if something is missing, then you… you… when… it's, like, try-catch empty, something like that.
Does it ring a bell? So… but then, of course, you would have, like, the entities with two extra files, basically, whereas the others would have, like, just one reference for the attributes.
I've explained it very badly, but I hope you… I hope you understood what the dilemma is.
Josh Suereth 00:51:24 Yeah, yeah, yeah, I don't…
ariannavespri 00:51:30 Of course, it's better if I push the PR, but…
Josh Suereth 00:51:33 Yeah, it would help if you pushed the PR. I have macro advice for you, which is, feel free to fix the test environment.
ariannavespri 00:51:42 Like, they…
Josh Suereth 00:51:43 It's very naive, and when I did the first set of policies, every single PR I was making, I was making an improvement to the test suite to be better. It's a frickin' ugly Ascend bash script.
And it doesn't have the features you need. And it sounds like all the questions you're asking are, we really didn't get the feature set right, which doesn't surprise me at all.
And some of the things you want could be, like, test script features, or, like, you know, if you set up your test environment, you throw, like, a configuration file that tells the script how to run the tests to make it easier for you to get the stuff done. I think that's part of it. The entities thing, I want to see, like, if you could send your PR, because I think it… I think I know what you're running into.
I have a guess.
And I hope… I hope I'm not correct, but if I am, we might have a bug or something to look at there.
ariannavespri 00:52:36 Yeah, okay, I will, I will, because now I was like… first I edited with the first approach that I said, so the inconsistent one, but the less repetitive one, and then I said, but what… how are we actually doing things? How I did actually, how did I do things? Because I don't remember, like, getting into this kind of problem when I added the DMD templates originally in Weaver, and there's, okay, there is, like, an attribute… there is, like, the repetition of this… of this file.
So I kind of did that, so I can, I can revert, and yeah, but… yeah, no problem, no problem.
Josh Suereth 00:53:13 Yeah, yeah, it, like, whatever, again.
use your judgment on what will make a good test and maintain it. Like, if you have to go in and fix these things, what's gonna lead to the best experience maintaining these is what we want. And all I'll say is, like, yeah, that test script is… it works, that's the only thing it has going for it.
Whether it has the full feature set you need and makes it easy to maintain, look, we have room to improve it.
ariannavespri 00:53:39 Fantastic, thank you.
Josh Suereth 00:53:41 Yeah. Cool. Alright.
Let's, Lyudmila, last one. We have, 5 minutes.
Liudmila Molkova 00:53:48 Yeah, maybe we have enough.
So, can I share for a sec?
Josh Suereth 00:53:55 Yeah.
Liudmila Molkova 00:53:57 Cool. So, jack, sorry for my… Ai here?
So Jack left a good comment on the ATAP, and I… I don't know, I didn't have a chance to think it's a roux, so let's… let's do it together. So what we have today is this manifest.
And it points to the resolved schema, right?
And here is the result schema next to it.
It's the branch without, dependencies, I think. Oh, sorry.
It's just all wrong. Okay, so this is the resolved schema. Maybe this branch doesn't have everything we need, but… If you pay attention, this… is part of the resolved schema. This is not.
This is part of the resolved schema.
This is not.
And this is just a pointer to the resolved schema. Why the heck do we need manifest at all? Like, who would download manifest without downloading resolved schema, and why?
Can we just drop the publication manifest and publish resolved schema and all the future extension properties, like link to, I don't know.
symbols can be part of this resolved schema URL. It's big enough to… it's okay to accommodate a few extra metadata properties.
Josh Suereth 00:55:25 Okay, I'm gonna throw on my dependency resolution hat, and basically say.
the reason you want the… we want the manifest to be incredibly small, incredibly cacheable, and we want it to have enough information to make dependency resolution successful, and I expect it to evolve over time. So if you… if you look at, I'm gonna use Java. If you look at the Maven example, where there's, like, a Maven YAML that tells you, like, here's my name, here's my dependencies, and that sort of thing.
It is small, and what I do is I do that to do my dependency resolution set, to actually explore the entire tree of dependencies, look for conflicts, figure out what versions I'm gonna pick, and oust versions I'm not gonna use.
And figure that all out very quickly.
And then I get a list of, okay, here's all the schema URLs to download now, and then I go resolve all the versions I'm really gonna use. So I can actually save, like, when we're in a world with multiple versions, and we're picking, like, a version over another version.
That's when a manifest file is really, really, really critical.
Whether or not we need that sophistication for Weaver, I'm not sure of, but until we know we don't need it.
until we actually build out that dependency resolution system that handles conflicts and all that, I would be nervous to get rid of it, just because I know from working in dependency management systems in the past.
And actually building out the resolution algorithms. Having a form… a file like this, that lets you rapidly expand the space, grab all your dependencies, and understand the tree.
is super valuable. I do not want it to be big. I actually think it's already too big.
Like, if it was more binary or had less information in it, that'd be better, but with what's there, it's kind of okay.
Liudmila Molkova 00:57:18 We have 3 minutes, and probably I wouldn't get to the bottom of it, but help me understand. So we can do dependency res… like, let's say we just downloaded this guy, and it has some dependencies.
Where can… take dependencies from it, the dependencies section only. It would be here.
Josh Suereth 00:57:40 Yeah, I have to download the whole file, right?
You don't need to…
Liudmila Molkova 00:57:45 We… you need, in order to… this is the resolved, schema for the top-level thing you're hitting, right?
Josh Suereth 00:57:53 So when I do dependency resolution, I will be looking at a lot of manifests that I never would do the resolve schema for.
Liudmila Molkova 00:58:00 I don'.
Josh Suereth 00:58:01 Why would you?
Because, so, so, I have dependency A, depends on version 1.1 of B.
Dependency C depends on version 1.1.1, of B.
I don't need 1.1 of B, I need 1.1.1 of B, and so I will resolve the manifest to figure that out, and then I will download only one file instead of two for B.
Liudmila Molkova 00:58:31 You will need to download both A and C for sure, right? And then you…
Josh Suereth 00:58:37 For B, let's say there is 1.1 and 1.1. Sorry, 1.1.0 and 1.1.1. Let's say we have those versions, right?
Liudmila Molkova 00:58:46 Okay.
And then, essentially, you… you cannot just rely on the schema URL, because it's a tree.
or maybe even a graph… it's a graph. And then you first need to know All the nodes before you get all the information.
And the optimization is the similar versions that you don't download, different versions of the same package before you know you need them.
Josh Suereth 00:59:17 Yes, so basically, if I have B… if I depend on B1.1 and B1.2 and B1.3 across my dependency chain.
and I have a resolution algorithm that's gonna say, okay, we'll just pick 1.3, because that's the latest compatible version.
That means I can do the whole expansion of the graph, I can figure out that I have those 3Bs, but I only need to download the Resolve schema for 1.3, because that's the only one I'm using. And so it makes your dependency resolution that much faster.
Which matters when this gets explosively big.
I don't know if… again, I don't know if we're gonna be there. I don't know if we need it yet, but I know, generally, for dependency resolution, this is a thing you want.
Liudmila Molkova 00:59:59 Okay, it makes sense. Jack, I think Jack left a comment that he doesn't like our resolved schema URL inside schema URL. Maybe we can address that as an alternative, but yeah, let's keep manifest for now. It's also, like, you see manifests everywhere, so it makes sense.
Josh Suereth 01:00:15 I can point them at mavenpalm.xml, because that's exactly what they do, with our.
Liudmila Molkova 01:00:20 Yes.
Josh Suereth 01:00:21 Be like, hey, This is what we're doing.
Liudmila Molkova 01:00:23 Yeah, yeah, I… yeah, the analogy makes sense.
Josh Suereth 01:00:27 Okay, gotcha.
Liudmila Molkova 01:00:28 Thank you.
Josh Suereth 01:00:30 Cool. Thanks, everybody. I think that was it for today. I hope everyone has a good week. Good discussions.
Laurent Querel 01:00:37 Thank you.
ariannavespri 01:00:38 Goodbye, bye.
