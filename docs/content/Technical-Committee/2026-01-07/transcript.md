SIG: Technical Committee
Date: 2026-01-07
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Reiley** 00:11 Hey, Tigran.
**Tigran Najaryan** 00:13 Alrighty.
Happy New Year.
How are you?
**Reiley** 00:18 Yeah, doing fine. Just came back, this Monday, still catching up.
How about you?
**Tigran Najaryan** 00:25 Yeah, yeah, I'm good.
Same here, we're off for… 10 days? More than 10 days, I think? Yeah, just like this Monday.
**Reiley** 00:34 Okay, good.
**Tigran Najaryan** 00:37 That was a good tool.
A break, and you come back, and everybody was also on break, so there's nothing to catch up with.
**Reiley** 00:46 It's also a good way to test whether your system is working properly, or you're a bottleneck.
**Tigran Najaryan** 00:55 Yeah, yeah.
**Reiley** 01:00 Hey, Josh, Chad.
**Jack Berg** 01:02 Hey, Riley.
**Josh Suereth** 01:04 Okay.
**Tigran Najaryan** 01:06 Hey, guys.
**Liudmila Molkova** 01:09 Hello.
**Josh Suereth** 01:15 Happy New Year.
**Reiley** 01:18 Happy New Year.
**Tigran Najaryan** 01:18 Dude.
The inboxes are empty.
I'll just check.
**Jack Berg** 01:55 Thank you.
**Tigran Najaryan** 02:27 Josh, you wanna start with your topic? I see you added something to the agenda.
**Josh Suereth** 02:33 Yeah, I'm trying to get the link, apologies.
So… Lydmilla's is related, but a specific task.
Mine could actually go for a long amount of time, so I'm gonna timebox to, like, 10 minutes a description of what I want to talk about, and then maybe we can talk about Lyudmilla's efforts?
Anyway, do you need me to present?
Or are folks okay just opening up the OTEP? I wanted… I wanted to call out In this OTEP, this is the stable by default OTEP for changes in OpenTelemetry. I think a few of us already made a few, a bunch of comments here. I made one comment on the overall OTEP that I want to talk through a little bit on the TC to see where we stand.
Which is basically, kind of a meta comment about the OTEP. I think this OTEP is huge.
I think this OTEP is… should be… Defining a set of work streams that will ripple through OpenTelemetry to accomplish stable by default.
as opposed to one giant OTEP with all the details in it, because I don't think we're going to… figure out all the details quickly. And I think that it'd be best to divide and conquer this work.
So, my suggestion here, and I didn't have time to think through this in detail.
But my suggestion is this OTEP should be, here's the objectives of the overall effort of Stable by default. Here's what we consider, like, success when we're done.
And then here's a set of things that need to get kicked off, and there will be OTEPs and people defining those sets of things.
And that we can divide work in the collector, we can divide work in semantic conventions, we can divide work in SDKs appropriately.
You know, my initial thought was just, you know, experimental features. Cool. We want to be able to enable and disable experimental features quickly, let's just get a group that works on that.
And that could be an independent group, and the group working on semantic conventions, and federating semantic conventions, which is what, Lyudmila's topic is for the next thing, right? I… this was all top of mind, so I didn't really think deeply about what these work streams are, but I wanted to have this discussion to see how we feel, if we should push for… let's… to make this OTEP go through quickly, let's focus on… it defines the requirements, it defines an end state.
And then it defines a set of work streams, and those work streams we find owners for and start driving them quickly.
How do folks feel? Thoughts?
**Tigran Najaryan** 05:12 Josh, before we go there, before we talk about how do we make this happen.
Can we talk a bit about whether this actually solves the problems that are described in the motivation section?
I'm reading it, and I'm not entirely convinced that that's the case.
And the motivation, if you look at the motivation, it says that The problem is experimental features are breaking production deployments.
And so, okay, what do you achieve by… By changing the defaults here, I'm not sure I understand that.
If people do need those instrumentations or components.
**Josh Suereth** 05:51 Changing the defaults.
**Tigran Najaryan** 05:53 Doesn't change the fact that you change the behavior of those components, it's still gonna break the production deployment.
It's only if it's accidental dependencies, right, are going to be prevented here.
how much of these problems are accidental versus deliberate usage of those components, because people need them, right? They use them because they need them, not because they accidentally stumbled upon a component, and not knowing that it's experimental, they started depending on it. How often does that happen?
**Josh Suereth** 06:24 So, I'm a big…
**Tigran Najaryan** 06:25 I'm convinced about all this thing.
**Josh Suereth** 06:27 I think there's two problems here, Tigran. I think there is, people… okay, so… Here's my line of reasoning. One is, we have components in the collector that are still marked experimental, that have been incredibly stable.
And people use them everywhere.
Okay?
What that leads to is now people think all experimental components are at that same quality bar. And so they actually expect experimental to be relatively stable because of that precedent.
And now, when a component really isn't stable and it breaks, people get even more upset because they can't tell the difference between it's experimental, but relatively stable, or it's actually experimental. So, this goes, pretty extreme and just says, cool.
you don't get to turn it on by default until you mark it stable, and this has, I think, a few implications. One is, those components, like the collector components that are used everywhere and relatively stable.
We'll be really encouraging maintainers to mark them as stable so they include them on by default, and users will be pressuring them because they need them. To answer that question, right?
**Tigran Najaryan** 07:39 Okay, so you're trying through this, you're trying to force… A more correct labeling of stability levels for components.
**Josh Suereth** 07:49 I suspect…
**Tigran Najaryan** 07:49 That's what I'm hearing.
**Josh Suereth** 07:51 I suspect that will happen, yes. I am not positive, but I suspect that will happen from this. Yeah.
**Tigran Najaryan** 07:58 Okay.
**Liudmila Molkova** 08:00 I think it's a widespread problem that people install a distro, and it brings 50 or 15 experimental instrumentation libraries.
Authors of this instrumentation libraries don't… consider the implications of breaking changes, because the library is experimental. The distro is not, or it doesn't look like one.
**Tigran Najaryan** 08:27 Okay.
Okay, I'll take that. One other, maybe, objection I have is that this essentially means if you're upgrading to a newer version, that that enjoys this practice of disabling many components that are enabled today, you're essentially going to break a lot of people's existing installations. How does that work?
**Josh Suereth** 08:52 Yeah, I think… I think that needs to get sorted through. I, I, I absolutely agree with that, like… Let me make clear my position here. I think the spirit of this OTEP, I'm behind. I think the details are gonna take a lot of work to figure out, and that's why I want this meta-conversation of We need to divide and conquer. I think there's too much in this effort to put in one OTEP. We're gonna sit here and churn on this for months.
And I don't want to see that happen. What I want us to see is we agree on what the principles are, what the guidance is, and what we think a good end state will be, and then details like what you're asking should actually be in a separate OTEP focused on that.
Like, what… I actually think we need a distribution release management, like, group that gets spun up to figure out what that means and how to do that, and that will be, like, one of the tasks we give them to figure out.
I don't have a good answer. I don't think there's a great answer in the OTEP from my memory, but I could be wrong. So, but that's where… that's where I'm at here, is the spirit of this I agree with, I just… I think there's too much in here for us to ever agree to the details in this OTEP itself.
**Tigran Najaryan** 10:06 Okay.
Okay, yeah, sounds good to me. I think it's a problem that is worth solving.
You're saying the solution is complicated?
it's unlikely to be a single OTAP, I think I completely agree with that.
**Reiley** 10:25 I have a question about the governance. So, my understanding is anyone can announce they have an open telemetry distribution, so how is this going to… govern them.
Like, if they don't follow, we don't have a registration, are we going to have a documented listing, like, we… We disagree with that. This shouldn't be called a distribution, or we're going to send attorneys to them.
**Josh Suereth** 10:52 Yeah, I don't know if that's answered, Riley. I would ask that on the OTEP, possibly, or we can see that, too, yeah.
**Tigran Najaryan** 11:00 We could have some sort of enforcement from our end as well, including technical enforcement. So, for example, if we're talking about the collector, then the collector components, they are… they are enabled or disabled by the, essentially the… the centralized service Business logic, which can… enable the site to not enable a component based on its declared stability level, right? And that same logic is used in distributions as well.
the vendors don't typically change anything in that particular logic. Vendors typically override Maybe the set of components, or other remove stuff.
But the core logic that is responsible for for enabling or disabling a component is the same across all distributions. Or that's what I think it is, maybe. I may be wrong.
**Reiley** 12:03 I see. Thanks.
**Jack Berg** 12:05 What are the set of distributions that we would want governed under this type of OTEP? Obviously, there's the collector, there's the Java agent, there's a JavaScript auto-instrumentation solution, like.
let's get concrete. Like, not every language has a distribution, and so, like, where… who are we actually trying to target with this? Which projects?
**Josh Suereth** 12:29 I do think this is going to target, anyone who has something like auto-instrumentation. So, like, the PHP auto-instrumentation, JavaScript auto-instrumentation, Python auto-instrumentation.NET auto instrumentation, Java instrumentation.
**Jack Berg** 12:47 That's what I thought, and I actually don't think that's quite right, like, is thinking about this in terms of distributions, because, like… like, what about the languages that don't have distributions? These are still guidelines for their… good guidelines for their instrumentation libraries.
And so, like, you know what? Like, all of a sudden, if you bundle these up in a distribution, you have, like, this extremely high bar that you have to cross that, like, you don't if you just publish individual libraries.
That's kind of nonsense.
**Liudmila Molkova** 13:12 Well, I think that this is what the principle is about, right? So that we… But try to ship stable things.
We don't wait for years before things stabilize.
And we try to remove obstacles that don't let us do this. For example, I can ship instrumentation library if semantic conventions are unstable, but if I ever change them, I will need to major version bump.
Or if I'm a Python and I ship log API inside my stable SDK, I probably shouldn't do… sorry, my log… unstable log API in stable… in stable OpenTelemetry API, I shouldn't do this. It's the principle that applies to pretty much anything we ship.
**Jack Berg** 14:00 Yeah, and I think I… I'm with Josh, then, that, you know, details are really important on that principle, because I agree with that principle, but when I'm looking at this, I actually see a lot of additional friction added, not friction reduced, and it's like, it's friction that's preventing us from shipping things stable.
Earlier, you know, I'm looking at this, expanded stability criteria section, and it says, you know, every stable component needs to have complete documentation with a getting started guide and working examples. Like, all configuration options are, you know, documented in a reference, troubleshooting guide.
performance benchmarks published and, you know, running as part of CI. You know, it's thoroughly testing integration points and operational readiness checks, like health checks and graceful degradation, and it's like, yeah, all these things are great, but that's, like, that's raising the bar for stability, not lowering it.
We're a big, sort of, federated community with… that's, like, under-resourced.
And, you know, I think, you know, the policies that we have to have are… need to be really lightweight for them to actually be, to actually… for them to actually be, you know, have any merit, right? Or else they're just going to be ignored. We're just gonna write something down on paper, and then in practice, people aren't going to do the thing.
**Josh Suereth** 15:27 I'm a fan of anytime we have a policy, if we can't automate it, we should rethink whether we have a policy.
So, to that extent, like, if we're able to get, you know, a GitHub action that enforces the policy of stability, or whatever the heck we want, that we can share across projects, cool.
Great, let's do that.
that's one of the things we've been focusing on with, like, Weaver, right? Is getting to the point where it literally, you can have a GitHub action that will enforce compatibility of your telemetry schema, and then you can use it for code gen and all that kind of junk, so that we know that, you know, things are lining up with the policy we want to enforce.
But if we can't do it automatically for you, so it's, like, super lightweight, super easy, it's gonna be hard for us to actually enforce that in practice. Like, it's almost not worth it.
**Tigran Najaryan** 16:21 Josh, things that Jack was talking about, You can have… a GitHub action that, on paper, checks for the existence of those things, that the documentation exists, but in reality.
These are so subjective.
Whether you do have an actual documentation, whether your benchmarks are worth anything, whether your tests are comprehensive or no, they are very, very subjective, so I don't know the automation is going to help in this case, other than surfacing, maybe, the fact that there is some sort of documentation, which is… which isn't a very high bar to clear, and it's not telling me much, that you have a single page with Some random sentences there, right?
**Josh Suereth** 17:09 Right, but it does reduce some friction, right? To some extent. Like, like, again.
when we want performance benchmarking, right? There's a reason why we want performance benchmarking, but configuring that is hard.
Getting that all set up. If we can provide enough automation to get you the basic thing set up.
then you as a maintainer can go in, and the friction of you adding better performance benchmarking is lower. And my expectation is users will ask for more, or possibly we get contributions, because we've reduced the friction so far that it's easier.
For overloaded developers to do this, right?
But I hear what you're saying, like, all of this is subjective.
there's an automation and a qualitative piece. We're meant to be a qualitative bar to hold the standard high, and, like, provide that, but to the extent that we have attention to look at everything.
a little bit crazy, so I, you know, anything we can automate, we should.
anything. Where we could have some sort of… You know, quantitative bar, and then focus the qualitative efforts Piecemeal where we can, you know?
**Tigran Najaryan** 18:26 No, I agree with the spirit of what you're saying, I'm just saying it's going to be hard in practice to get there.
**Josh Suereth** 18:35 That's also why I think this is a multi-OTEB, OTEB. This is not a single effort. This is a… and we probably need a roadmap for when we tackle different pieces of this. The notion that we need benchmarking across OpenTelemetry. Think of how many times we've tried to kick off benchmarking. I think we need to look at this stable by default and say, okay, like, let's get a phased approach of This hits first, this hits second, this hits third.
I, I… Yeah. I look at this OTEP and I see all of OpenTelemetry 100% in on this, or it doesn't succeed, you know what I mean?
**Jack Berg** 19:11 And just to pick on benchmarking for a second, so yeah, like, we've had benchmarking efforts that have, you know, had false starts, and this is… this is so much more ambitious than those previous ones, because this is… this is talking about adding benchmarks as a requirement for stability for every single component, individually. Like.
A performance benchmark for every single instrumentation library. A performance benchmark for, like, every single component in the collector.
like… What kind of resourcing do we have to be able to do all that? To be able to maintain those performance benchmarks over time?
**Tigran Najaryan** 19:47 But is that the bar? Like, every component has to have the benchmark, or is it… I'm not sure that's a reasonable bar, to be honest.
**Jack Berg** 19:56 That's… that's what I'm reading in this right now, because it's talking about the requirements of stability of each of these components, and it's talking about, like, you know, you know, trying to stabil… like, have an individual stability metric or, label for each of your, you know, instrumentation libraries, each of your components in the collector.
And so, you know, if you're gonna have individual stability labels, then you have to have, like, be able to evaluate these things differently. They have to have their own documentation, their own performance benchmarks.
And their own testing.
**Tigran Najaryan** 20:27 Yeah, yeah. I'm not so sure about that. I mean, look at the collector, for example. We do have Benchmarks for certain things that we believe are important there.
But it's not like we have benchmarks for everything, and… Having benchmarks for everything would be an enormous amount of new work there.
I… I don't really know if that's… that's a reasonable ask there.
**Jack Berg** 20:56 And I'm channeling the JavaSig as well, with the Java instrumentation, you know, collection of, I think, 200 different instrumentation libraries.
Hmm.
**Tigran Najaryan** 21:10 Yeah.
**Josh Suereth** 21:11 I absolutely agree. Like, the Java example, I think benchmarking the SDK, you have that. I think maybe benchmarking your HTTP Instrumenter, maybe that makes sense once, but then redoing it for all 200 libraries.
I don't know.
**Tigran Najaryan** 21:26 Yeah, it's the same in the collector, right? We have hundreds of components there.
Rights.
**Jack Berg** 21:32 So it's like, you know, this OTEP… so what are the themes that are emerging in this conversation? It's like the OTEP is too big, too ambitious, and so, like, it's unlikely… you know, past precedent has shown us that OTEPs that are even smaller scoped are tough to get off the ground, and so one that is this big and this broad, you know, like Josh said, it seems like if we don't have all of OpenTelemetry behind this.
It's not going to succeed, and since that's unrealistic, we have to shrink the scope.
Like, that's, like, one sort of theme of this conversation. Another theme of the conversation is, like, that at least is present in my head, is, like, make everything lighter weight.
Right? Like, we need to have an OTEP, that, you know, talks about the principle. I think we can all achieve… get behind the principle of this thing, but, like, meets us in the reality that we're at.
Right? Where we have hundreds and hundreds of components in these distributions, and we, you know, everybody's already stretched thin. So we can't add just, like, a ton more work to, you know, the maintenance requirements of these things. So that's, like, another thing.
What were the parts that you suggested we break it out into, Josh?
**Josh Suereth** 22:48 Again, I didn't… I will caveat that I did not do deep thinking on this. This was literally top of mind. I was writing it while super jet-lagged. So, like, this needs to be rethought. But what I initially called out, these were just the obvious ones to me, and I think there could be more.
Where… where'd my comment go?
Carlos commented right after it. Enabling experimental features.
Federated schema.
a whole distribution and releasing workstream around what does it mean to be a distribution, how do you include pieces, you know, that whole effort, I think, needs an OTEP around what is a distribution and what is a stable release. And if you saw the operational resiliency requirements and stuff, but I was thinking, like.
that would be under some sort of a distribution theme that might even be more than one OTEP, that theme, but it, like, called out to me as, like, a thing to call out. And then lastly, like, a profiling.
around understanding what features need to be profiled, what features don't need to be profiled. This is the performance benchmarking stuff.
You know, as like, oh, Jack, you're muted.
**Jack Berg** 24:02 Okay, profiling here is just a synonym for benchmarking.
For benchmarking, yeah, yeah, yeah.
Alright, I'll… I'll go leave a comment on this that kind of reflects my thoughts.
**Josh Suereth** 24:20 Yeah, again, I don't think this is the right set, this is just the immediate set, so if we… if we… if we sit down and think about this, I think we can all come through and say, okay.
here's the set of work streams we think make sense in OTEL, right? Here's the set of work streams that we think meet the objectives. But if we can refocus this OTEP on, like, what are the objectives we want to accomplish when we're done, what do we consider success?
And then we can really dive deep on specific OTEPs. I'm… we're at 25 minutes, and I think Lyudmila wants to talk about one of those, OTEPs that I think is absolutely critical, and so I want to… seed the floor now, if that's okay? Because I think… I think we… we generally have consensus around some high-level thoughts here, and then the details are gonna take a while. So… Sound good?
Cool, let's… and folks, if we can all comment on this OTEP with thoughts and things, Jack, if you take a crack, beautiful, please do. Alright, let's move on. Ludmila, do you want to… Do you need to present?
**Liudmila Molkova** 25:28 Yeah, I'll present. Thank you.
So I, I… we talked about it in the spec call, but to get everybody, on speed, we are working on the schema, semantic convention schema V2. Josh calls it my effort, it's his effort, and I don't know.
80%, So, what we want to do, and this is… sorry, my lightning is kind of off. Anyway, so what we want to do, we want to be able to… For the consumers of telemetry.
Looking at the telemetry, looking at the schema URL, to know what this telemetry is.
not just the diff, but the definition of it. This helps us with validation tremendously.
It's essentially impossible today with the thousand-plus attributes and a lot of metrics and spans we have in semantic conventions, just in the single semantic conventions.
And… We cannot host every semantic conventions in the world. We want collectors to host their own, we want instrumentation to host their own, we want companies to host their own conventions.
And we want them to be, publishable and discoverable by looking at the schema URL.
So the first thing we're suggesting is that we, instead of publishing the diff.
With major version bump, the schema file format is going to be a manifest.
And it would point to the actual resolved schema. Details are in progress, but we have it implemented, essentially, this schema. We can work with it, in general.
We want to publish two of them. One is for development version, which is everything, let's say, in semantic conventions. One is for the stable only.
And this would be part of the schema URL, so you would get 139… dash dev, if it's a development one. You can read the manifest, but even if… by looking at the version, you can Say if it's stable or not.
I want to talk about diffs in particular, and the major… breaking change we are proposing here. Any questions so far before we get into the diff stuff?
**Tigran Najaryan** 28:05 I love the goals. Fully support.
**Liudmila Molkova** 28:10 Cool, so then let's talk about diffs, and so, first, this document is stable.
It would need some changes.
the schema URL stays the same, but this… This part, the file format, is going to be a major version.
**Reiley** 28:31 break.
**Liudmila Molkova** 28:32 This is in development, so technically we can do this. Still, I wanna love… I would love your opinions. So, one of the important parts, we kinda… we have the schema processor, which works with the schema file format, but it's… It was kinda… it's not included in the… OpenTelemetry Distro, so it was… somewhat implemented recently, it doesn't support everything. We broke this file a lot of the times, in the past, because we didn't have validation, we have it now, but we didn't.
**Reiley** 29:08 And… essentially.
**Liudmila Molkova** 29:11 What we're saying, that given the actual usage of this feature.
We probably don't want to support… first, we want to… we want to pursue breaking change, it will be just file format 200.
Second, we don't actually want to publish DIFs… yet.
is the reasoning that you can produce them on demand. You can say, okay, I'm, I'm going to prefetch the semantic conventions versions that they support, or I can do it lazily, and I can do the div between two arbitrary versions.
using Beaver, and I can cache the diff files if I really want to do this.
**Tigran Najaryan** 29:53 Is diff… is it possible to compute the diff given to version numbers?
**Liudmila Molkova** 29:58 Y-yeah.
So, the Viva supports it, let me show you.
**David Ashpole (dashpole)** 30:05 Are there any diffs that are not not possible. Like, if someone renames a metric, I, like.
**Tigran Najaryan** 30:14 Yeah.
**David Ashpole (dashpole)** 30:14 Will it even know about the diff?
**Liudmila Molkova** 30:17 Yes, so all… all the renames are supported. Nothing but renames is supported.
So, like, if I change the type or unit on the metric, we don't support it now. We could, in theory, but it means some more design, like, for example, Do we use OTTL or some other language inside of, inside semantic conventions to express this transformation?
So, there is a lot of future work there in the space, and this is one of the reasons I kind of want to, have a better design for the whole story before we start publishing the V2.
**Tigran Najaryan** 30:58 So the fact that the metric was renamed, it is recorded in the full schema.
**Liudmila Molkova** 31:04 Somehow. It is. Right?
**Tigran Najaryan** 31:06 Okay.
**David Ashpole (dashpole)** 31:08 Does it have, like, a consistent ID or something, or how does that… End up working.
**Liudmila Molkova** 31:13 So… You see… when we don't remove the metrics, or attributes, or anything that's identifiable.
So when we deprecate, we say it's renamed, and it's renamed to something.
**Reiley** 31:33 And this stays up-to-date, it's validated.
**Liudmila Molkova** 31:36 So, at any moment, if you just look at version N, You… see all the past metrics, even if they are in development. We don't remove them.
And you can… you don't even need a diff, you can just look at the latest version and find things there.
**David Ashpole (dashpole)** 31:57 Interesting.
**Tigran Najaryan** 31:57 Can I ask, why are we not including the diffs if they are easily computable automatically? What's the problem with that?
**Liudmila Molkova** 32:06 So what… what would you include? Do you include the… the… yeah, Josh, go ahead if you want to answer this.
**Josh Suereth** 32:15 I'll just start with, they're not necessarily easily includeable. So, the way the previous schema file worked is you had to diff every single version whatsoever. It was all in the same file. So what we do today is we have this awkward thing where we save the previous file and then add the diff of just the latest version and the previous one next.
The command that we use in Weaver is you give it two schemas, and it will diff the two.
So, you… have to manually understand, like, what version to diff against, and then keep track of that in some way to, like, generate the… so, like, if we were to record a Weaver diff, it would be just the differences between two versions, not all of them.
If we wanted to, like, diff all versions, it's… it's a lot more work, it's a lot more complicated, it's a lot… a lot different feature. So, when we were trying to, like, build out this file and maintain it and have it be automated, that's what actually made this rather awkward.
**Tigran Najaryan** 33:14 Yeah, what if we produce just the diffs for N minus 1 versions?
like the previous version compared to the current one, the latest one that we're releasing. They are aggregatable, right? Do you need to produce all the combinations of this, really?
**Liudmila Molkova** 33:33 I think that all the scenarios that we have today, you don't even need the DF4, because it's already in the schema.
**Tigran Najaryan** 33:45 Okay. Just in a slightly different… just in a slightly different form, essentially. But, the source… The source of truth, essentially, is this schema file, and that it already describes that the rename has happened.
**Liudmila Molkova** 33:59 And it does not cover 100% of the cases, but those we don't support yet anyway. And if we want to support them, this is the time where we would Think about publishing DIFs and transformations.
**Josh Suereth** 34:12 Yeah, for context, the thing that isn't here is what we call an… it's not obsolete, it's a dropped metric. So if somebody drops a metric completely, what we have in semantic conventions is you literally can't submit a PR that does that.
If you try to submit a PR that drops a metric, it fails our validation and our policy.
when we allow, you know, federated semantic conventions, people might do that. And so, that's the thing you lose with diff, is you can't understand that something was dropped between version A and version B.
However, when something is dropped between version A and version B, we can't do any migration whatsoever anyway.
Yeah. Right? It's just that thing is gone. So, like, I agree with Lyudmila that for the purpose of doing transformations and the compatibility we were looking at, just the scheme is sufficient.
we… we… I also believe that we'll be investing in DIF over time, and expanding it, and making it better, and that if you look at the proposal Lydmilla has, we have the capability to add the DIF, in that schema file format. So the file is just a description of where things live. So, if we go back to the… yeah, right there. So where it says future, we can have a diff URL, or an all-in-one URL. Like, we have the ability to expand this, because we're actually moving… the contents to a separate URL, so this is just, like, an index file, if you will.
So I think this gives us the evolution we need to explore diff fully.
to get it working, to add capabilities like, you know, unit changes, unit conversions. If we wanted to figure out how to deal with drops, or mark things as breaking changes officially with diff, I think we can start doing that, right? And I think this gives us that flexibility going forward. But in terms of what we actually do today in telemetry URL, We're not missing anything from the automation that creates telemetry URL, But we are missing some things that we knew… we use policies to prevent users from doing.
**Tigran Najaryan** 36:20 Okay, and we preserve the… the immutability of the schema files, right? Absolutely, yes. So we can… we can prefetch them, cache them, and… There's no problem with splitting into multiple files, there's no performance.
Because of that, because you only need to fetch it once, so no problem with that as well.
**Liudmila Molkova** 36:40 Yeah, and one more thing about diffs, I think they will be useful, not, even between versions, but between schemas, like ECS to OTAL.
where we are trying to figure out how to report RPC metrics along with native gRPC ones, that translation there might also be useful. And these diffs can become, something else in… in… in general.
**Tigran Najaryan** 37:09 Okay.
I think this sounds good to me. One question I have is… Where do we expect, in what piece of software produced by OpenTelemetry, do we expect this schemas.
to be used.
And in the past, the trans… sorry, the schema processor in the collector was supposed to be using the schema files, and it never did become a thing.
**Liudmila Molkova** 37:36 We… yeah.
We already are…
**Tigran Najaryan** 37:40 What is it that… where are we going to use it?
**Liudmila Molkova** 37:43 The main user within OpenTelemetry is Weaver itself, we have a life check there, and it takes the schema, and it validates telemetry you receive against arbitrary schema.
one of the maintainers of this project is using it for their own company's telemetry. It's not even just hotel registries that they care about.
The… thing I'm building, is the validation for instrumentation libraries, in Python currently. It uses Viver LifeCheck, you produce telemetry, you validate the telemetry is valid.
This is actually… would be super useful for the stability effort. It could be the certification, for the library, or it can detect breaking changes in the library, or not compliance.
the… the hope is that once we publish the schema, like, for example, you… like, at Splunk, at Grafina, hopefully we can, read the schema, and we… let's say we can show the tooltips, it's just a trivial thing that vendors would use, but it's… it's beyond open telemetry ecosystem.
**Tigran Najaryan** 38:49 Yeah. So for us, it would be a way to… Prevent breaking changes in the instrumentation, essentially.
**Liudmila Molkova** 38:56 Or not compliance, first, and, breaking changes as well, since you would validate against certain version.
**Josh Suereth** 39:07 I think we can also update a schema processor to use this file, and or create a transformation of the file that gives an optimized thing for the schema processor to do its renames.
Like, I think we can… yeah, I think we can update that thing with this in the future as well, but initially, Weaver would be the primary user.
**Liudmila Molkova** 39:31 Yeah, and we can actually produce, from the existing schemas, we can produce file format 110 if we need to, so it's possible to do this.
**David Ashpole (dashpole)** 39:42 In general.
**Tigran Najaryan** 39:48 This is good.
Thank you.
**David Ashpole (dashpole)** 39:51 My original question, do you think this could be useful for mapping other… ecosystem schemas onto OpenTelemetry.
Like, could I define one of these for Prometheus, and then… Describe how it transforms into some version of the… OTL schema for something.
**Liudmila Molkova** 40:09 Oh, yes, and there are very, quite a few people who are already trying to do this. I think Bartek, create, did a talk on this. There,
**David Ashpole (dashpole)** 40:19 Okay.
**Liudmila Molkova** 40:20 Yes, people are working on it.
**Josh Suereth** 40:22 So, David, Bartek, Ariana, and Arthur San Silva are all in the Weaver, SEMCOM SIG and, like, participate and are doing some crazy stuff. So you should… I think Ariana and Arthur might be the best people to talk to right now, like, some of the stuff they're trying.
Yeah, but abs… that is, that is one of the goals. Now, the caveat I'm gonna add… is… Weaver can only express, you know, within the OpenTelemetry model.
So if you're… if you're trying to map metric A to metric B, and you can describe metrics in the OpenTelemetry model from Prometheus, you can do a diff, you can do that, like, comparison, that's fine.
If you're mapping something that is not in the OpenTelemetry model.
Like, someone has, you know, a thin bar, or like, you know, I'm thinking of a Dr. Seuss term, like, you know, I have marsupials, and I want to treat them as logs. That's where things get weird, right? Like, it has to be an event, it has to be a log, it has to be an entity, it has to be a metric.
Those are the things we can diff.
**David Ashpole (dashpole)** 41:30 Cool, yep.
**Liudmila Molkova** 41:34 Cool, then, thank you. I don't hear major concerns. This is work in progress, there are details to polish, but this is coming. Thanks a lot, everybody. Thanks, huge thanks to Josh for everything you're doing in this space.
**Josh Suereth** 41:53 Thank you for writing all the proposals and, the design, I'm just implementing it.
**Liudmila Molkova** 42:05 Do we have anything else?
**Josh Suereth** 42:10 I think that was our last topic.
I haven't checked in a while. Do we, the TC rotations, has anyone taken a look to see when that runs out?
And if we need to regenerate it.
**Reiley** 42:24 I think till the end of the year.
We're good.
**Josh Suereth** 42:28 Oh, it goes all the way to the end of this year.
**Reiley** 42:31 Yeah.
**Joshua MacDonald** 42:32 Oh, cool. I just keep checking when I'm next, and I have, like, a month to procrastinate on that topic.
**Josh Suereth** 42:40 Well, I don't want to use any more of this meeting, but for the next meeting, please have a think about… the rotations. What's working, what's not working, and how we can improve them.
you know, what can we do better? Do we… are we happy with them now? Do we feel like it's… distributing efforts. I still believe I have never released the specification, I feel guilty about it, but if that's working as intended, cool. And thank you, Carlos, for releasing the specification.
**Liudmila Molkova** 43:09 Do you want to…
**Carlos Alberto Cortez** 43:10 What is specific.
**Liudmila Molkova** 43:10 application today?
Josh?
**Josh Suereth** 43:13 Given that my laptop fried while on vacation, and I'm on a loner Chromebook.
I don't know if I can write code on this yet, so I think releasing the specification is a no-go. But next week, when I have a real laptop again, I'll let you know.
**Liudmila Molkova** 43:32 Sure.
**Reiley** 43:34 Yeah.
releasing spec is probably the only issue I'm seeing, and if you ask, like, what I can see from improving the current rotation, I would say maybe folks are getting used to it, let's switch to a monthly rotation.
Anyways, I'll bring this, like… Later.
**Josh Suereth** 43:55 Yeah, yeah, let's talk about this next week, if everyone's cool, but just, you know.
reflect on it this week as we go through, our daily routines and reviews and things, and I just want to see how we're happy… if we're happy with it, if we need to make any changes.
Awesome. Yep.
Thanks, everybody.
**Reiley** 44:11 Thanks, Mario. Bye.
**Liudmila Molkova** 44:12 Thank you.
**Carlos Alberto Cortez** 44:13 do you…
