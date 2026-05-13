SIG: Specification SIG
Date: 2026-05-12
Duration: 58 minutes
============================================================

## Zoom Recording Transcript

**Jack Berg** 05:12 Hello, everyone.
**Trask Stalnaker** 05:18 Hey, hey!
**Reiley** 05:19 Hey, Doug.
Hey, Era.
**Ted Young** 05:24 How's it going, y'all?
**Trask Stalnaker** 05:29 Can we get out the party poppers?
**Ted Young** 05:32 Yeah… .
**Jack Berg** 05:36 Where's the champagne emoji?
**Ted Young** 05:39 Right?
So exciting. Yeah, people on the call, haven't heard.
Opentelemetry, is officially approved for graduation.
What the rest of that timeline looks like, I don't know.
Next KubeCon is KubeCon Japan.
I'll be there.
But, I'm not sure what else is going. In theory, we get a mascot, by the way. That's something we should talk about at some point.
Have to figure that one out.
But, wow.
**Trask Stalnaker** 06:20 sold on, Ollie the Otter.
**Ted Young** 06:23 Yeah.
Ollie the Otter was… the… one of the rules of getting a mascot is it has to start with the same letter as the project, so… Oh, and Otter is pretty close to… to hotel.
So, Ollie the Otter sounds.
**Trask Stalnaker** 06:38 And otters are adorable.
**Ted Young** 06:39 They are. The only… I've been trying to, like, sketch otters, and the only thing is, like, they're, like, an otter holding a telescope, and, like, they have these stubby little arms and these really long bodies, so, like… I think it needs to be, like, floating in space, like… like a little otter astronaut, so it can be floating around a… a telescope, because there's no frickin' way it's gonna be… You make the arms long enough so that it can look through a telescope and doesn't look like an otter anymore.
**Josh Suereth** 07:05 This is… this is crazy, but could we reach out to a zoo that has an otter and, like, officially sponsor it in some way? Like, I would donate for that.
And we could call it the, like, literally the OpenTelemetry Otter.
**Ted Young** 07:16 That would be amazing.
**Josh Suereth** 07:17 we could all go visit it, that'd be amazing, yeah.
**Trask Stalnaker** 07:19 I'm…
**Josh Suereth** 07:20 in.
**Jack Berg** 07:21 Pick one that's young and healthy, has a long life ahead of it.
**Reiley** 07:25 No, they…
**Josh Suereth** 07:26 They can… there can be, like, a lineage, it's fine, yeah.
**Ted Young** 07:29 Yeah.
**Josh Suereth** 07:32 Jack, I also thought about that as it was escaping my mouth, what I said. Okay, cool. Sorry I'm a little late, guys. Yeah, so Ted, you were talking about graduating. Anything else we need to say there? I… I don't… I don't see times on some of these, Agenda items, so I just wanted to kind of, like, start timeboxing. How much more time do you want to talk about graduating, so I can timebox the rest of the discussions?
**Ted Young** 07:57 I think we can move on. There isn't anything actionable from our point, at this moment. It's just awesome that it happened, you know, at the, like, check the box at the GitHub level, merge the PR level.
But we haven't heard back on the GC, we haven't heard back from the CNCF yet about, like, what… What it all means, what are next steps, but we'll definitely keep everyone informed once we know more.
**Josh Suereth** 08:23 Cool Awesome. Okay, so I think in terms of time, we have stable by default. I would like to give you the next 25 minutes for this, it looks pretty big. Does that… is that too much, or is that reasonable?
**Ted Young** 08:37 I think that's reasonable.
**Josh Suereth** 08:39 Okay.
And then, Jacob, do you think 5 minutes for seeking reviews is good?
**jea** 08:45 I probably only need, like, 2 or 3, honestly.
**Josh Suereth** 08:47 2 or 3?
Alright. Then, C. Joe, how much time do you need for this, for your PRs here?
I don't know if Cedra's here.
We'll give this one 5 to 10 minutes.
Lyudmila has 2 minutes for this one. Antoine, how much time do you think you… this is an announcement? I'll give that 2 minutes.
**atoulme** 09:15 Yep, works.
**Josh Suereth** 09:17 And then, Carlos, I think we should have time if we manage the time box, stable by default. So, let's get started with Stable by default. Ted, kick it off.
**Ted Young** 09:25 Great, okay. So, this is just to, to pitch the spec and maintainer community here on a rewrite of this OTEP. So I've been, trying to take over this OTEP called Stable by Default. If you're not familiar with it, this is the grab bag of stuff that we agreed upon with the CNCF, based on a lot of user feedback, on what we need to do to kind of complete V1 of the project for graduation. So we initially set out, you know, to give the world tracing metrics and logs, unified, you know, with OpenTelemetry and the collector, And we're graduating because they agree we've, completed all of that work, contingent upon us working through this set of issues.
The thing about that OTEP was, as it was written, it was, like, a little vague and open-ended, right? So it was kind of hard to get started on this stuff, because some of the work is pretty gnarly, but we… it would be a lot better if it was actually, like, scoped into actionable work streams. So what I've been doing is going around and talking to the various people involved, trying to figure out what is the right size of, like, actionable stuff.
So, what I'd like to go through now is just kind of walk through what I see as a more actionable list, and to just see how… what people feel about that.
So let's kick it off. So, starting at the beginning, we need to stabilize everything. That was, like, a big part of this, is we have a lot of stuff that's de facto stable. And some of these work streams were also in this OTEP about, like.
better definitions of what's production-ready versus not, and I think we'd solve all of those things by getting everything out of the de facto stable zone.
So… we end up in a place, if we do that, where the things that are 0.x are the experimental things that are not production ready. And anything that's 1.0 and above is production ready, and you should use it. So… The two big things there are the collector needs to stabilize. I believe the collector SIG has a roadmap for that.
So I don't know that we need to go into the details there, but that still has to happen.
The bigger bugbear is stable instrumentation. That's kind of what we were talking about last week.
We have all of this instrumentation. This instrumentation needs to work in order for OpenTelemetry to work, but we've had an attitude of, like, the instrumentation is kind of community managed. It's all in Contrib, you know, if people want it to work better, want it to update it, if they care about this piece of instrumentation, they can update it. The SDK maintainers don't have time to maintain all of that stuff.
But that doesn't quite align with, like, how OpenTelemetry works, right? Like, in order for OpenTelemetry to provide, you know, its kind of, like, standardized telemetry, we need a way to have a pipeline from we update the SEMCOMF to the instrumentation gets updated.
We've talked about upstreaming some of that stuff, right? Like, native instrumentation, and the stuff that doesn't get upstreamed needs to have a better management model.
But I think both of those approaches are kind of solved by the same thing, which is we need better tooling for maintaining this instrumentation so that the cost of dealing with it is a lot lower, and it's a lot harder to accidentally make a mistake. Those are kind of the things we see. It's seen as, like, kind of onerous to maintain it, and it's kind of easy to make a mistake because we don't have, like, tooling that wraps it.
But we do have a SEMCOM tooling SIG that has been hard at work on solving those problems.
And, talking to, you know, people from that SIG, like, they're ready for the spotlight. So the first part of this is basically the SEMCOM tooling SIG, still owning that, but, moving that more into.
the spotlight, more into this meeting, more into, like, maintainer discussions, but basically working with that SIG to get a complete story together that we can go pitch everybody with.
But the basic idea is you've got Weaver, that's capable of auto-generating various coding structures for you. If we have more of those coding structures, then we've constrained the problem a lot better. And then if on the other side we have, like, a test harness, that works really well, and, you know, manifest files that kind of, like.
You know, put out the output of, like, what this thing is verified as doing.
That we can hoover up into Ecosystem Explorer and other places. You've now really constrained, you know, the… the instrumentation target. And if all of that's constrained, you know, we're now flooded with all kinds of different AI coding tools.
And we believe that that constraint means we can potentially find a cost-effective way of using, you know, AI to then help you know, write these PRs.
If you add all of that up, the maintenance cost of this stuff looks like it goes down, and it becomes easier also to potentially upstream this stuff, to different, places where it should live.
So that's… that's, like, kind of phase one of this, is, like, work with SemComf Tooling to, like, get a package together to really sell the community on, like, a new way of doing it.
The other part of this that we have to figure out is more of a social one, which is we don't want to say instrumentation is, like, this sort of, like, left-to-the-community thing.
We need to find a way to incentivize people to maintain this stuff, because at least a good, solid subset of that instrumentation is really valuable to us as a community.
But, we don't really have a way of, like, rewarding companies for, you know, putting, a lot of labor into doing that.
So, something we're looking at on the GC, and would love, you know, feedback from people, is, like, what are better incentive models? You know, we currently tell people, don't use dev stats in your marketing, because That makes dev stats useless, because people would start gaming dev stats, but maybe there are ways we can give out badges, rewarded honorarium things that make it clear, like, who's putting the effort in to… to maintain this schlep of stuff.
And same thing goes for, like, libraries and stuff that choose to upstream this. What can we do to kind of give them a certificate or a badge or something like that?
So, that's the stable instrumentation pile of work.
Moving on from that, the other big thing that we need to kind of finish out is the ability to actually install and configure and maintain open telemetry across a large organization from the perspective of someone who's more like an operator, or like, you know, a centralized infrastructure team, or SRE people.
Right now, it's sort of like, you have to touch each application in order to get OpenTelemetry installed, even if you're using, like, our auto-installation tools. And we do have some amount of centrally managed stuff, like the Kubernetes operator, but it's not, like, fully… like, full coverage isn't there yet.
And there's a couple of different, you know.
angles that need to get stabilized as part of that. Like, op-amp needs to go 1.0, like, the Kubernetes operator would need to, you know, say it goes 1.0 once it's completed all of that work. And we just started the system packaging SIG, Which, you know, is a way to basically manage this on Linux if you aren't using Kubernetes, and also a really good getting started experience for people. Someone just wants to kick the tires with OpenTelemetry.
you know, just installing, you know, the OpenTelemetry package in their Linux container, or their little environment, you know, on their dev machine. That's, like, a very common, nice, getting started experience, you know, for open source projects.
So that helps with that as well.
So… That's, like, the thing we'd like to see, and also, maybe as part of doing that, there's, like, various… configuration stuff to solve some of the issues of, like, I want this instrumentation, but not that instrumentation. I want to be pinned on this version, you know, of telemetry. There's, like, various nice things around trying to configure this stuff.
And it would be nice if we did that in a way where it wasn't like… you know, if you're going into the operator, you're using one configuration, system packaging is a different one. If you're directly installing the SDK, it's a different one. It would be nice to make that a little more universal, and we've already been working on that with declarative config.
But there's some harder problems, you know, when you're trying to package this up, versus, you know, having the language dependency manager.
Download the bits for you.
So, a lot of details there, but that's the other big line of work. I've been talking a fair bit about that one, and we'll keep on talking about it, but just to stay on the time box.
for this conversation. The other thing we've been asked to take a look at is security. Oh, Tigran, I see you got your hand up.
**Tigran Najaryan** 19:35 No, go ahead and finish, I thought you were about done. Okay, done.
**Ted Young** 19:39 Yeah, so security, we've been asked, you know, to, as part of, like, graduating and everything.
you know, have, like, a better security story. We do have a security SIG. They have been, you know, working hard, but we could use more participation, again, from organizations on the security side.
We just, at Grafana Labs, have one of our principal security engineers join the SIG, but, turning that into actionable and not just, like, better security somehow.
The things that we're seeing on that front is… we're seeing a lot of, noise, with AI. Basically, people running scanners and AI, you know, vulnerability checkers and various things at scale, and then… Basically, the volume of, like, reports has gone up dramatically, but it's mostly noise.
So it's just, like, more and more, noise and having maintainers having to kind of, like, pay attention to this noise is taking them away from, you know, paying attention to shipping features. So, you know, trying to staff up Even from a triaging perspective around security would be helpful.
The next bit, do you mind scrolling down a little bit, Josh?
or whoever's got the screen. Thanks.
The next bit there is also, like, the security SIG publishes protocols for maintainers to follow. When there is a vulnerability detected, you know, what should you do? What are our protocols?
We can always be improving those, but one question is, like, how do we have oversight To make sure that happens, and if for some reason, say, something happens, maybe, you know, a SIG has, for some reason, gone dark, or the maintainers aren't responding, you know, how do we know that that's occurred, and what would we do if it turned out there was… a serious vulnerability, in one of our repos, and for whatever reason, the maintainers were MIA. Like, what would we do? What is the escalation process there?
So, you know, improving, like, what our responses look like would be helpful.
And then, like, the last thing we're seeing is, like, more and more end users are running their own scanning tools, and they even have some, like, legal requirements around these scanning tools passing, and these scanning tools are more and more kind of, like, showing false positives with OpenTelemetry.
This is related to the noise problem, but the difference is it's end users saying, hey, you know, we're being gated on using OpenTelemetry because it's showing up red on this scanning tool.
And it would be helpful for us to kind of have our own kind of scanning tool, our own way of, like, having a conversation with those end users to say, like, you can ignore that.
That's a better, more official or more quantitative approach than being like, hey, trust me, bro, you don't have to worry about that one.
So, again, we already have a SIG for doing all of this, it's a security SIG.
But, we need more staffing there. And maybe, again, there's a way to incentivize companies being involved there.
If you're willing to, like, staff the security side of this, then, you know, and you go through, like, an trust approval process, then, you know, your organization would get more early warning access to these CVEs.
I don't know how much we want to make that, you know, a carrot, but we do… it does matter, security does matter, so we do need to find a way to get more people involved on the security side.
Just to… to help take the burden off of maintainers on the triaging and the scanning and, like, all of this noise.
Okay.
Last bit, performance and benchmarking was something that got brought up a lot. Like, people do care about performance, they would like to see benchmarks or some kind of reassurance, but, like… Doing all of that in the abstract, you know, we do this for the collector, but we always struggle a little bit with, like, what kind of benchmarking are you gonna do? Why are we doing it?
And my proposal is, like, actually, all of this performance stuff, collectively, is maybe next-gen OpenTelemetry.
Like, people are using our stuff in production today. It could be more performant, but it's mostly fine. And, we can't do everything all at once. So what I'm proposing is we get through this earlier set of issues, because that's much more about, you know, packaging up and securing and finishing the original set of work.
And then on the other side of that.
you know, there's all kinds of different performance things we could look at, but it would be much better to be doing this benchmarking in the context of we're actually trying to improve performance in various places, you know? So we've got some, like, you know, skunk work projects going on around, like, better protocols and things like that that are interesting.
But when it comes to things like, you know, the collector internals, or, like, the SDK, it would be much better to, like, have performance be in the context of, like, what do we want to do to… to change our architecture, or otherwise, like, you know, make changes so that we can improve performance?
But we can't do everything all at the same time, so I'm kind of proposing, like, this is the work we focus on after we've gotten through this earlier set of work that's more focused on packaging and security and installation.
If we collectively do all of that stuff.
Then OpenTelemetry's, like, in kind of a super awesome 2.0 place, where, you know, it's easy for everyone to install and manage at scale everywhere. The instrumentation is all, you know, 1.0 and stable and, like, up-to-date with the latest semantic conventions, which are also stabilizing, and… And, we're in a really, like, cool spot. And then we can start kind of having fun again around, like, how do we, like, what's, like, the next gen look like for telemetry? How can we start improving this stuff?
Okay, that's my pitch.
**Josh Suereth** 26:23 So, yeah, we have… we have a hand, and we have some writing here. So let's… let's do Tigrin, and then, we'll do the writing, but just so everyone knows, we only have about 7 minutes left in the time box. So go ahead, Tigrin.
**Tigran Najaryan** 26:35 Yeah, thanks for presenting, Ted. So, looking at this list, I think it's… it's necessary work, but it's a lot of work that will take time. Luckily for virtually all of these things, we already have SIGs who, in my mind, they are ultimately responsible for doing the work of getting to stable. What I'm… what I'd like to understand is What exactly is the way of executing this project? Are we looking at working with these existing SIGs to define the stability goals and what it means to be stable, and then let the SIGs work towards that goal?
essentially becoming some sort of an overseeing project that helps other Sikhs get to stable.
but not necessarily doing the actual work, and not having the, I guess, the dedicated staffing that works just on the stability of each of the individual area. What's the thinking here? What is the execution model for this project?
**Ted Young** 27:37 Jack, I'm guessing you have comment… thoughts on this?
**Jack Berg** 27:39 Yeah, I think, Tigran, that we… we establish the principles and create mechanisms to go reach out.
to the respective SIGs that we think have work that ought to be done, and just track it. It's like a tracking mechanism, right? So, like, you know, here are the principles, and here… the way that we're going to sort of incentivize getting to the end goal of this is by, like, some sort of public tracking mechanism where we're, like, where we're repeatedly following up with it, so that we're all on the same page What's being done.
**Tigran Najaryan** 28:17 Yeah, so what I'm asking is to be clear about the fact that we're not looking at getting 3 engineers, let's say, in the stability project to go and begin stabilizing the collector. That's not what we're doing, right?
And similarly for all other areas. We're just helping the existing SIGs to achieve the goal of stability. That's what this is going to be about.
**Ted Young** 28:44 Yes, exactly.
**Tigran Najaryan** 28:46 how I'm understanding it, just please correct me if I'm wrong.
**Ted Young** 28:49 if you look at this, like, trying to make it actionable, there's some aspects of it where it's like, we need better tooling, or better, like, stuff in order to make it work, and there's a SIG responsible for that part of it. And then there's a second phase for a lot of these things, which is, like.
you know, all the different SDK maintainers, you know, or, or, you know, all the different contribib rep repositories. We need to find some way to, like, organize our efforts there. And that's just about, kind of, like… just improving the way we do project management, and really just socializing this stuff with the SIGs, and getting their feedback, and, you know, working with them on their roadmap, and if they don't have enough the kind of staffing to do it all, like, we try to, you know, address that directly.
That's kind of, like, how I'm trying to divide it up. There is some aspect of, like, some of these things, like, we don't feel like we currently have the staffing to do it.
Especially, like, instrumentation, for example. Like, we're not saying, like, the SDK maintainers have to go do this, but that means, like, there's a certain amount of, like… like, kind of like what we're doing right here, being… trying to have, like, a better, more open way of, like, managing these roadmaps, and being more public about it, and getting more feedback, and yeah, we would definitely love… Feedback from the community about, like, better models for, like, how we do that.
**Tigran Najaryan** 30:21 Okay, thanks.
**Ted Young** 30:24 Okay.
Josh?
**Josh Suereth** 30:27 I was just gonna echo that, like, I… I like that idea of, like.
having SIGs… I consider this, like, a platform. Like, with semantic convention tooling, we've been building a platform that other SIGs can use to maintain instrumentation.
And we have to think about, like, how do we make all of their lives easier? And that's why we build the tooling, you know?
So, I don't know if that helps, but that's kind of, you know, how I'm thinking about it, of like, there's a group of people who care about tools.
And that's really boring for other people, but we need to think about making it easy for everyone. And I did want to call attention to what they've been doing with the Gen AI stuff. I think that's… that's a template here. Like, please take a look at that. I think Lyud Mila has something later about this, but please take a look at that.
Yeah.
**Ted Young** 31:14 Nope.
**Jack Berg** 31:15 I wrote some stuff, as we were… as you were presenting this, and I just… we only have a couple of minutes, so I'll be… I'll be brief. I think the thing that I want to call out here is that, we need to make these sort of open-ended, hand-wavy goals tangible, and the way that I think that we do that, at least in the case of instrumentation, is by, like.
Defining what we actually mean by this. Stable instrumentation is just, like, too open-ended of a mandate.
And I think the way that we make that tangible is that we call out, like, the specific languages and ecosystems that we want to call attention to soon. And the ones that matter, I think from a user-facing standpoint, are the ones that have auto-instrumentation capabilities, or zero-code instrumentation capabilities. And, you know, we have those listed, Java, Python, JavaScript.NET, and PHP. So if we can have a common set of principles for what it means to have a distribution of one of these zero-code instrumentation solutions, and sort of, from those principles, argue about them at the sort of town square level, the spec level, and then, you know, go and track and create goals for each of these languages to get to the point where they're embodying those principles. That's how I think that we can check this box.
**Ted Young** 32:30 Yeah.
Yeah, totally agree. Like, you know, I think just getting this feedback process going so that we can get more and more granular with each one of these things, there's still… definitely question marks for, like, how we go about doing some of these, and I'm sure when we try to implement some of these changes, we're gonna run into even more questions.
And… Yeah, kind of, like, getting back into that game, almost like how we were in the early days of the project, with a lot more kind of, like, maintainer involvement and feedback, and being a little more coordinated around like, looking at these… these problems.
So, for sure.
I think we're… Cool. With that, yeah.
**Josh Suereth** 33:18 We just hit our time box, that's what I was gonna jump in for. So, thank you. I think if we have time at the end, maybe we can come back to this topic and talk about more stuff as folks have a chance to marinate and think about it, but, let's jump into the rest of the agenda quick. Sound good?
Okay, thanks. Jacob, do you want to take it away?
**jea** 33:39 Yeah, this is just sort of a quick reminder, a quick bump, for people to check out the, Policio tip that, Josh and I have written with another, colleague, Raphael.
It's in a pretty good place, I've answered all the current open questions, so if you haven't checked it out recently, please look again.
Just seeking some reviews on it. It's been open for, I think, a couple of months now, and not a ton of com- well, we got a lot of comments, like, a couple months ago, but, definitely in a good place now for, review, and hoping to get it merged.
Hopefully soon. I'm not gonna use this time to, like, answer any questions, just because there's plenty of other people on the agenda, but if you have any questions or feedback, please put it on the OTEP.
**Josh Suereth** 34:25 Jacob, quick question. Have you done a demo of, like, using this and, like, the, kind of the prototype itself? Because that might be a good thing to schedule for next week.
**jea** 34:34 Yeah, I can schedule that for next week. I have a bunch of stuff for that, so that sounds good.
**Josh Suereth** 34:39 Yeah, that'd be awesome. Or if you already have a recorded SIG that has the demo, we could also pull that in too. Yeah. Awesome.
**jea** 34:45 I think I'll do the demo next week, I'll put it on the agenda.
**Josh Suereth** 34:49 Cool.
Awesome. Let's do, CJO can't make it, so I think I might be… Oh, man, I opened the PR but forgot to share my screen. I'm sorry, guys. Let… yell at me if I don't do that again, anyone who is, here, or take over presenting. Alright, so CJO has two questions, needs a PR review. He said, might not be able to join SIDC call.
This is about having spec-to-semantic invention links. So for context, in the past.
When we pulled semantic conventions out of the specification, we have this… the semantic conventions depend on the spec.
So anything in the specification overrides something in semantic conventions. That's how we have that dependency chain working. So this is basically asking, can we have a dependency from semantic conventions back to the spec? What we did previously was… If the spec would actually call out attributes it owns that need to exist, and semantic convention owns their definition.
So I'm just gonna give that context of, like, that's… when we pulled semantic conventions out, that was a decision. This is, like, a quick 5-minute discussion on some of these, about referencing semantic con… semantic conventions for SDK self-observability.
So, yeah, I don't know if anyone wants to comment. I'm just gonna comment, because I remember pulling semantics conventions out. The idea here would be… if… when we do this, and we say there are self-SDK, self-metric observability, the specification is reserving, like, there will be a set of metrics that exist that folks need to conform to, and then should, like.
Is delegating the responsibility for what those set of metrics are to the semantic convention spec.
That's kind of like the way I visualize this. But the question would be for us, for us folks, how do we feel about that?
You know, what, anyone have concerns?
**Reiley** 36:52 No concern from me.
**Tigran Najaryan** 36:53 going to be just… just linking, right? So the definition of the convention leaves in SEMCOM repository, and the spec simply references the particular semantic convention. As long as we keep it that way, I think it's fine, right? As long as we don't bring the whole definition into the spec repository, we keep it separated, we keep it in the same conv as it is now, where it has the tooling in place.
Referencing it is fine, and we have other places, other repositories referencing semconconf.
That's also fine, so… It's no reason to… these allow, somehow, for spec to reference that. That should be fine.
**Josh Suereth** 37:35 Oh man, I wasn't presenting again. Yeah, okay. For context, here's the specific thing I think he had. No, that's the changelog. This is the specific thing he had of… there's a call-out for self-observability metrics, and then there's actually a link to SemConv.
I am gonna call out, the only thing that I think is pedantically annoying is this is… this is pointing at not OpenTelemetry I.O, And it's pointing at Maine.
So it's not pointing at a specific version of semantics Conventions, and it's not pointing at a specific, like, website.
I… Yeah, I'll make a comment in here that I think we want this to be a link, and we want it to say it depends on SDK semantic conventions.
But I think we need to be flex… like, are we gonna hard code what version of semantic conventions we require in the version of the spec? I think that's… that's BS. That's not needed.
So I want to find a way to divorce that. Go ahead, Lyudmila.
**Ludmila Molkova** 38:32 Yeah, I'm fine with the direction, and I support having up until I would try you here. The thing I was going to bring up that maybe we should… I have a dedicated A document for self… SDK self-observability, it's not just metrics. We have some sections on how to provide troubleshooting with logs, and eventually, maybe we'll have events. It's not a blocker for the SPR, but eventually, I think we should move in the direction of having a dedicated page for self-observability.
**Josh Suereth** 39:06 Okay, absolutely agree. We're out of our time box for this, so… or no, I gave 5 to 10 minutes. Absolutely agree, Libella. Anyone have any other things they want to add there?
Okay, I will update… I'll make some comments on these two PRs and let Cesar know that, this is totally fine, and then some things for us to think about so it's, like, less annoying to maintain. Alright, let's move on. Ludmela, you want to talk about final call for reviews on Schema V2?
**Ludmila Molkova** 39:37 I think there is another PR from Sijo he wanted to bring up about the second one.
Is this…
**Josh Suereth** 39:44 Is this different? I thought this was the same, but .
**Ludmila Molkova** 39:47 It's completely different, and… this is something we've been discussing in the log sig. Not sure if Robert is here, but he was also interested in this, and this aligns with what we wanted to do, To describe log bridge, which is not instrumentation scope name, because instrumentation scope name for logs is a logger name.
But this would be the first example of Really, the instrumentation scope attributes.
And I think CJ wanted to bring it up here, my assumption is to get Some blessing for using them for the first time.
**Jack Berg** 40:34 Ugh.
I've been worried about this.
So… The… when you write a log appender, you have to do something that's kind of unusual.
You know, you have this stream of log records recorded from another API, and you're trying to bridge them into OpenTelemetry. And what do you need to do when you're bridging? Well, the first thing you need to do is you need to map the upstream logger to the OpenTelemetry logger.
name, and so you say, okay, upstream log record, get the logger name, and then open telemetry, look up the logger name. And, so, you know, that's a really important thing, because it doesn't match what we do for traces or metrics. With tracing and metrics, when we establish a tracer, or we establish a meter, it's done, like, statically and infrequently.
With writing a log appender, you're asking for a logger every single time a log record is bridged. And so, I jumped through some hoops in the Java instrumentation to make that logger lookup really fast.
And, I'm not sure I can make it really fast and really performant if there's scope attributes.
And also, we don't support scope attributes in Java. Yet.
**Tigran Najaryan** 42:05 Oh, Jake, this…
**Ludmila Molkova** 42:06 when it comes.
**Tigran Najaryan** 42:06 You only need the name of the logger, though, right? These are not identifying the scope attributes.
They are not identifying. Your lookup doesn't need to look at the scope attributes.
**Josh Suereth** 42:17 They are identifying, aren't they?
In the spec, they're identifying Tigrin.
**Tigran Najaryan** 42:24 what Jack was describing, in terms of the lookup that he's doing.
I don't think he needs to look at these attributes to do that lookup.
I think we had suggested.
**Jack Berg** 42:35 And, I think scope attributes are now identifying.
**Josh Suereth** 42:43 Yeah, scope attributes are absolutely identifying. That was a decision made A little while ago, that really complicates things, yeah.
**Jack Berg** 42:53 It also has allocation implications as well, so, I'm able to, like, short-circuit some allocations of actually, for reasons by only having, like, the logger name, but if there's, like, a logger name and scope attributes, then every single one of these log records that's bridged, I think, has to have an extra allocation.
**Tigran Najaryan** 43:13 Yeah, what I meant is a slightly different thing. Yes, attributes are identifying for the scope. These particular attributes, they are statically defined. They are the name of the bridge.
they don't change. You don't… you know, they… when you have the name of the logger.
it statically maps to the name of the bridge, if I understand correctly. So for the lookup, you don't need to use the attributes.
I'm not sure how exactly your code is organized, but you shouldn't need that.
**Jack Berg** 43:44 The lookup is happening not inside the log appender, the lookup's happening within the log SDK of OpenTelemetry, and so the log SDK doesn't know, you know, this distinction between that, like, these attributes are going to be static. It just sees that, like, hey, I got a logger name and a set of attributes.
**Tigran Najaryan** 44:01 Okay, okay.
Alright, you're saying something.
**Josh Suereth** 44:06 We're at time. Ludmila, you had your hand raised. Jack, I don't know if you… if we want to finish this point. Can, Do we want to put a pin on this and continue discussion in the PR? Like, how do you guys want to proceed?
**Jack Berg** 44:21 I mean, I'll definitely add a comment to the PR, but I do want to hear what Lyud Miller has to say.
And she's up for it.
**Ludmila Molkova** 44:28 Yeah, I think we will keep discussing it. I'll leave a comment on the PR as well.
**Josh Suereth** 44:36 Cool.
Alright.
I think… I think that sounds like a plan. I don't think we're gonna come to a resolution at this meeting, necessarily. That sounds more like one we have to hash out. Cool. Ludmila, you're next, then, with, Schema V2OTEP.
**Ludmila Molkova** 44:50 Yeah, so, there have been a lot of discussions. We've implemented the schema effectively for the GenAI conventions that we split, and we have the approvals from semantic conventions Maintainer from Tigrin, who worked on the first version of schema from Trusk, who implemented the GenAI split, and Effectively, we have all the prototypes, more than prototypes for this OTAP.
And they have the approvals. Less approvals than I hoped for, and I still… I'm still very interested in feedback from people who are interested in other split. For example, Anton is, we will be talking about mainframes, and there are maybe some people from the collector. Also, Anton.
But essentially, I think this is ready. I addressed all the open feedback that there was.
And if people want to take another look, please go ahead, but I would like to merge it sometime.
This week.
Oh, that's all the pitch.
**Josh Suereth** 45:56 Awesome. Super supportive.
cool.
Antoine.
Do you want to jump in with your announcement?
**atoulme** 46:06 Yeah, short plug to let us, to let everybody know, next week, I will take time of this meeting to go over the packaging SIG, which has been newly introduced.
I want to make sure, so there are a couple… couple things to do. One is to go over the SIG goals, and, kind of go over the PR that was merged into the community repository, maybe explain some of the roadmap, some of the big, milestones we're trying to go for, and also explain, how the SIG is going to report. It's a little different from other SIGs, because we have, I'm being dedicated by the TC to report back.
So I just want to make sure we set the processes for that. We have a chance to discuss. I want to do this in advance, to put a notice of this presentation, so that if anyone is interested to participate.
We will be talking about it on the Hotel Packaging channel, and we'll try to have a first discussion soon about that as well, either in the channel or in a Zoom meeting. So, yeah, anyone interested to participate?
**Josh Suereth** 47:13 I'm gonna say one thing real quick, which is that this is not new… so this is a new requirement, but it's not just for the packaging SIG, this is for all SIGs.
Okay? This is across the board. What we want to do is turn this meeting into a place where we can all have open discussion about what we're building, and things that, like, impact all different, like, ecosystems. So this is not like you're… we can… we can talk more about this offline, but it's not like they're targeting the maintenance SIG. This is just a thing we want to make happen, because we find really healthy discussions in this meeting. So, like, I actually am really excited about this. I think this will be really good, because I don't know if you have enough attention on stuff you're building. So, please, like, make these presentations.
**atoulme** 47:52 Yeah, we haven't.
built anything, because we just got set up. But, yeah, yeah, definitely. So, trying to make sure we present that.
Check?
**Jack Berg** 48:00 Just a point of process. On next week's agenda, there's already an item on the, on the agenda for a 20-minute, conversation about the policy OTEP demo. And so, if we're gonna have a talk about packaging, and we're gonna have a talk about policy OTEP, that's you know, 40 minutes, probably, right there. And so, we should either stagger them, or basically commit to having nothing but those two topics, plus little status updates.
**atoulme** 48:30 I can move it in 2 weeks, is that… is that preferable?
I can… You tell me.
**Josh Suereth** 48:38 who's… who's… I think Armin's running it next week, so I think, in terms of, like, the coordinator, I'm just gonna say, like, as coordinator, I… I think that these are important for us to kind of get through. Jacob, maybe we could drop that to 15 minutes, and then have.
**jea** 48:55 under 20 points.
**Josh Suereth** 48:55 20 minutes for the, packaging one.
**jea** 48:58 That's totally fine.
**Josh Suereth** 48:59 Does that sound reasonable? But I hear what you're saying, Jack. I do think that, like.
Packaging is urgent. We do need to talk about it. We're gonna have time to talk about stable by default, but packaging, as you saw, is, like, one of the important pieces there. So I don't really want to delay packaging having time in this meeting myself. Like, I'd love to make sure that we're addressing that. So I think that just means we might get to less of the nitty-gritty things. Does that sound reasonable for everybody?
**jea** 49:27 Yeah, I can go after Antoine. He had his issue in this agenda earlier anyway, so I'm happy to go after him.
For prioritization's sake.
**atoulme** 49:38 Well, thanks, Jacob, but he didn't have to do that.
Shit.
**Josh Suereth** 49:42 One of the things that I do… I'm just gonna go on a little 10-second thing. We should be spending a little more time optimizing our agenda here to make sure… we want to be fair to everybody, but we do need to focus on priorities, and so something that has to, like, launch or is part of, like.
you know, hotel graduation criteria. I do think we want to make sure that those things come first, and it's fine for us to manipulate things a little bit. And so, hopefully, yeah, those of us who are running this meeting can use our judgment to say, you know what, this hasn't gotten enough attention, let's move it higher. So this is more for, like, the TC members here who run the meeting to, like, make sure that we're doing that prioritization ahead of time. Yeah.
Cool. And if… and if you need more time, Antoine, just let us know.
Okay.
Okay.
**atoulme** 50:31 Thanks.
**Josh Suereth** 50:32 Awesome.
Let's move on to… I think Carlos.
**Carlos Alberto Cortez** 50:40 Yeah, that just means a very quick update. We… you may remember the previous discussion, we had last week on the context scope attributes tab. It's almost ready. There were a pair of items to update.
The first one is, well, both things are things that, Tyler, correctly pointed out. The first one is that we need, like, different users may need to set something in the context, like, for example, instrumentation Library.
and then the user. So we… now, instead of having an operation called addContext Attributes, we have a… that it became aft context attributes, which means that we can just merge different stuff. It's very simple, it works in the same way that standard attributes work. The last one wins, very simple.
there are a few different ways how to implement this, but that's the general idea, you know? The second thing is that this is probably a… The more important one is that I actually massage the text to… to… make this specific… add the specific details regarding metrics, so the context attributes are not added at instrument creation time, but rather when the actual measurement happened. And also making clear that the context attributes are added right before, views, or advisories, or coordinarity limits, or any other downstream processing happens. We don't have to discuss that here, I think. I haven't updated that.
So Tyler, Jack, and CEO, and everybody else, if you have any.
Anything to comment, please say so. Are there some comments that somebody added?
In the last couple days, I will go over them. They seem minor.
Just probably the need for their, refinements.
**Josh Suereth** 52:37 Cool.
All right, so that's, a heads up for folks, you're not looking for discussion here. Awesome, thank you. We have, we have 10 minutes left if there's anything we want to revisit, or anything we want to call out. I think, I'd like to give that time back a little bit to the overall stable by default.
or, like, topic-specific in this table by default as well. So, like, that would include packaging, that would include, the, federated SEMConf and, instrumentation stability topics. So, I don't know, I'm gonna open the floor for that, if anyone has any topics they want to… They had time to think about, had time to turn on and want to discuss?
All right, I was too good at timekeeping, so we all get 10 minutes back. Please, all these things that were advertised on the PR, take that 10 minutes, and those PRs that are open, please take that 10 minutes, if you can, and take a look, and make comments, and that sort of thing, and we'll see y'all next week. Looking forward to some presentations, too.
**Jack Berg** 53:51 Thanks, everyone.
**Trask Stalnaker** 53:54 Great. Thank you.
