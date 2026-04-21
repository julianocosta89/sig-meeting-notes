SIG: Semantic Convention SIG
Date: 2026-04-20
Duration: 41 minutes
Zoom Recording URL: https://zoom.us/rec/share/vmWNGe5D2fBKsdo8jDafQOWjh1B9XVqT6VN5-peu7UV_S_pXwuhgT4M_gmfbSkia.WY66vFeGL8Nwx-k5
============================================================

## Zoom Recording Transcript

**Victor Lu** 01:31 Hey, good morning.
**Trask Stalnaker** 01:36 Hi, y'all.
**Victor Lu** 01:38 I want to make sure that, from, last week's meeting with OCSF, what's a follow-up, and you're going to join the co-sign meeting?
**Trask Stalnaker** 01:52 Yeah, so I'm… I'm gonna continue joining the OCSF meetings and see if we can make progress there.
The COSI meeting… Let me… Check if I have that on May.
**Victor Lu** 02:11 Yeah, I put in the Slack.
**Trask Stalnaker** 02:15 Okay, that one is… Directly following the…
**Victor Lu** 02:19 Right before the OCSF meeting.
**Trask Stalnaker** 02:29 Oh, okay, okay. Yeah, I should be able to join that.
**Victor Lu** 02:36 Alright, awesome. Thanks.
**Josh Suereth** 03:35 Hey, how's everybody doing?
I have to drop in, like, 25 minutes. Would someone be willing to run the meeting today?
**Trask Stalnaker** 03:55 I can.
Just give me a minute.
**Josh Suereth** 04:00 Yeah, no worries. Thanks, Travis.
**Trask Stalnaker** 04:28 Ugh.
Alright, I'll let us start with triage.
And let's start with… Ready to be merged.
Alright, this has lots of… Approvals, and we've got merge conflicts.
Let's see how bad… oh, no, I can't do that on the web.
Alright, let's check next one… Alright, we've got required approvals… Got… Open conversations… Owl.
Yeah, I think that is.
not… a blocker… Oops, what am I doing here? Alright, we have got… Approvals… I'm assuming, Josh, I should just resolve this.
Entity question.
**Josh Suereth** 06:53 Yeah, I don't remember how we use ID here. I think you do have, like… in V1 versus V2, I think the ID has to be entity dot.
Or resource. One of the two. Like, if you look at all of our other identities, so… Yeah.
Like, that doesn't… I don't think the idea actually affects the… the real… identity of the entity. It's the name is what is used. So, like, that's like a V1 versus V2 schema thing, and will not actually be a question at all. Hopefully soon.
**Trask Stalnaker** 07:35 Book.
Let's see… What do I got here?
Okay, so… Okay, let me just ping… Braden… I must… Alright, and… last one… Got required approvals… Pink… Oh, okay. They just had not… I may just commit this… Since it's not a generated file… And… it will emerge if it passes.
Okay, it looks like someone just hit merge on this… Guy… Josh, yes.
Stabilized deployment environment. All right.
Did we want to go to RC?
Or straight to stable, feeling good.
**Josh Suereth** 09:41 Yeah, I… I don't, so… This is one of those de facto stable attributes. We did change it to be, deployment name, and you remember how fun that was for everybody?
**Trask Stalnaker** 09:54 Yeah…
**Josh Suereth** 09:56 So that's why I'm, like, I'm comfortable skipping an RC and going straight to stability here, because I think it's actually generally used significantly, and I, like… I would rather have this be the precedence for de facto stable things if we're not going to make any meaningful change to them, of like, cool, let's just mark it stable. Like, people are using it, it's used in production, we don't need an RC because, effectively, it's been an RC for 3 years or something, you know?
But… if you wanted to go through RC, like, I can understand following the process here, it's just I was comfortable going straight to stable.
I don't think there's much more that I would do that with. Like, there's… there's a few that, I think we already did that for service, right? Like, service name, I think, went straight to stable.
I think, what else do we have in there that probably will go… I see a few others that might go straight to stable, but I don't think it's a large list.
**Trask Stalnaker** 10:55 Cool. No, no, no objection, just… Wanted to make sure it was… Intentional.
**Josh Suereth** 11:01 Yeah, well, I don't know if the author was intentional about it, but I.
**Trask Stalnaker** 11:05 Yeah, but you were intentionally, yes.
**Josh Suereth** 11:07 Yeah, yeah, it is something to consider and think about every time we do this, so… yep.
**Trask Stalnaker** 11:15 Alright, we don't have topics. There is one topic I wanted to raise, which is…
**Josh Suereth** 11:27 If we have time, I do want to talk about, the federated SEMCOM proposal.
**Trask Stalnaker** 11:34 Cool, that is very related to my topic, which is splitting the GenAI semantic conventions out of the SEMCOM repo.
**Josh Suereth** 11:45 Oh, cool. So let's start… let's start with that proposal. I have to leave it, At 11.30 my time, which is in, you know.
18 minutes, so let's start with this. Let me… let me open up my, Let me open up the PR.
And then we can talk through it.
Cool.
For context, I was able to get Weaver to work with multiple dependencies right now.
And I was able to get it to, version… resolution. So, if you have two repositories.
that depend on the same schema URL.
You can depend on both of them, and it will pick the most recent version of the shared dependency.
for all the things that it does, whenever it has a conflict. So you can actually, like, create chains of dependencies and stuff with some comp now.
Not… anyway, we have to talk about it in SEMConf, because we have to cut a 1.0.
Because we're not using… semantic version… because we're using semantic versioning, and we're not 1.0 in SEMGONF.
Every release we make is a breaking version.
**Trask Stalnaker** 13:01 We're not 1.0, what do you mean? Like, the SEMCOM tags are…
**Josh Suereth** 13:08 I guess not. Oh, oh, they're 1.x now, aren't they?
**Trask Stalnaker** 13:12 Yeah…
**Josh Suereth** 13:13 Okay, never mind, we're fine, we're fine. Anything that is 0.whatever will be a breaking version every time, which is problematic.
Okay, cool.
**Trask Stalnaker** 13:23 We have a different problem in SEMConf repo, which is that we have the monorepo, mono tag, so we can't do major… we can't major version bump database by itself.
**Josh Suereth** 13:36 Yeah, which we want to do, yep.
**Trask Stalnaker** 13:38 Yeah, yeah.
**Josh Suereth** 13:41 Cool. So, actually, this is probably easier to read this way. What… what we're proposing here, just want to walk through everyone again, is this notion that we're going to change the semantic convention lifecycle. And we're going to kind of, get sub-ecosystems to evolve independently, and then come back to core if and when they want.
That's the basic idea. So, we've had a bit of slow resolution and highly specified domains. For example, JVM metrics might want to do a version bump. If they do so in core semantic convention, it breaks everyone in semantic conventions.
Whereas having it JVM-specific might be better. We have cloud-specific resource provider things that we have found are problematic, and we probably want to do a major version bump there.
By the way, this is the other one where we might want to de facto stable, make an RC for what we have, put it in 1.0, make it 2.0 in a separate thing, right? Okay, anyway.
We have a couple breaking changes, which, Trask was just talking about. If we try to major version bump a domain, like JVM, or like database, it forces all semantic conventions to have a major version bump.
So it looks like a breaking change to everything, even if it only touches one little area.
And we found that we do want to do that.
And that that's problematic the way things are today. So, lastly, we need a way for instrumentation libraries to declare what they generate prior to semantic conventions having a stable standard.
So that's kind of an important, important thing here. This would be, like, we have a lot of instrumentation in the collector, we have a lot of instrumentation in, you know, Java, JavaScript, all that kind of stuff. For those libraries, we want to give them the ability to have their own YAML files that describe what they produce to keep those YAML files stable and give people an expectation of stability from instrumentation.
But where we're still kind of figuring out what the semantic conventions would be.
And it's basically what we've done in practice. So if you think about HTTP and how that rolled out.
we had de facto stable HTTP instrumentation. When we started to change to make the standard, HTTP basically made a 2.0, but they hid it inside of an environment variable of, hey, I'm going to the new standard. They had releases of instrumentation that could do A and B together, and we treated it like a major version bump, from, like, de facto stable A to semantic convention B.
what this proposes is actually we would do that in these little sub-channels, where there'd be an HTTP, you know, convention set, where you could Make a 2.0, work on all the changes you want to make.
And then give people, you know, like, a year timeline or whatever to migrate from their existing conventions to the new 2.0.
And then eventually that 2.0 could be, rolled up into core, if needed.
The roll-up to core is probably the weakest part of this proposal, but we'll talk through that. But that's the idea behind how we work. So, we want an independent lifecycle for each SEM vert. We want instrumentations to be able to pin, so they can declare stability, and then enforce That they are stable?
using the same tools that we have, like Weaver, for example, to make sure that their instrumentation is stable, and I think, Trask, you might be talking more about that.
when you take over, after I'm done ranting. And then we want a promotion path. So basically, we can take some of these federated things and say, okay, this is… What our instrumentation produces now, and then when we say, like, oh, this is, like.
you know, core semconf, like, this won't change dramatically going forward for a very long time. That would be when it comes into core, right? So there's a way to promote and say, I was this independent thing, I was evolving for a bit, but now I'm pretty stable, I'm gonna evolve into core, and once I'm in core.
I have that really long lifetime, I have that really long, you know, no-breaking change expectation. I can't really bump major versions. But while I'm independent, I can actually do major version bumps, but I still have to abide by our major version bump policy for instrumentation in OTEL.
But… like, once I go into core, I'm much more unlikely to be able to do that, because the entire thing has to go through a major version bump, right?
Okay.
**Trask Stalnaker** 18:10 Could you talk a little bit about the, say, I mean, let's take the GenAI concretely. If we… Split it out.
Once we split it out, and we're doing… evolving there.
What is the advantage to… promoting it back into core, ever.
**Josh Suereth** 18:36 So, the main advantage is all semantic conventions are required to depend on core.
And so, what that does is if we start having other like, the big open question in my mind is, as long as these things are disjoint, everything's gravy. When they start to depend on each other, it gets a little awkward.
**Trask Stalnaker** 18:58 Yeah, that makes sense to me. So, I mean, in that concrete case, I mean, I guess we can… debate that, but, like, at least GenAI is less likely to… is more likely to be a standalone something that other things don't depend on, versus… deployment in the service, or deployment. Yes.
Yep. Stuff.
**Josh Suereth** 19:22 Like, deployment and service would have to get promoted eventually, in my opinion.
**Trask Stalnaker** 19:25 Right, right.
**Josh Suereth** 19:26 Whereas an HTTP is another interesting one. There are pieces of HTTP that might be core, and pieces that might be okay to keep on its side, right? Like, the error type that we defined, that one kind of has to be core.
**Trask Stalnaker** 19:43 Yeah, it… I mean, I would consider that core because it's not under HTTP dot.
**Josh Suereth** 19:51 Right, but HTTP is the thing that created and stabilized it initially, and then we expanded it.
**Trask Stalnaker** 19:55 Oh, I see. Yes, yes, if you wanted to, yes, yes, you would need to at least promote the common things that would want to be reused.
**Josh Suereth** 20:04 Yeah, and there's… so I think this is gonna create a thing where we, like, the core group will have to figure out some core abstractions that have to be across different conventions, but we get to kind of focus on that. I'll walk through it quickly, like, the life cycle, which is basically, you get… you get a federated registry.
This is defined by, Lyudmila's OTEP, where you can start to have new schema URLs, like, we can have a schemas for JVM that has its own version number.
In that registry, you'll have a new manifest for your schema, and then you will have a, your own, you know, definition of all the metrics that you use. There's a few requirements that we have, right?
Your separate registry has to declare a dependency on core.
So that's… that's, again, the reason why you want to be in core is because you make sure the whole ecosystem depends on you, things have to be shared between, we still have a place to do that.
A stable, federated registry must not depend on unstable or experimental core conventions. So that's another fun thing, is… if you're depending on it, and you want to be stable, it has to be stable. So, we have to make sure that either you create your own stable copy of it that you depend on.
Or we need to stabilize things in core, and this starts to do that pressure of what is core and what is, you know, federated. We can start to have that discussion of when things overlap and when they don't.
Okay, then… The registry has to use Dependabot or Renovate to keep your dependency up to date, meaning if Semconv rev bumps, the idea would be you would rev bump with Semconv. And you would… you could declare a dependency that says, you know, I'm on 1.x a semconv, and you will rev bump with Semconv every time it releases to make sure that you stay up to date with the latest.
the registry must enforce semantic convention policies that we are defining with GitHub workflow. So one of the things we created was this GitHub, OpenTelemetry Weaver Packages thing, where you… we can enforce naming conventions, stability, and overall naming concerns.
for any distributed repository in… in anything.
And so, the idea would be for open telemetry distributions, you're required to use these checks. These checks are reverse-engineered from the semantic conventions repo to make sure everything abides by the same set of policies. And then we have a central place where we can enforce those policies. So we as SEMCOM maintainers.
Could, go update those policies however we need to make sure that everything is consistent.
If we… if we have naming concerns and changes. If you haven't taken a look at those, please take a look. They have overrides and stuff. I haven't had a chance to update our repository to use them, but that's partly because we're not using V2.
Which, which they require, and partly just, time.
Okay.
Lastly, independent versioning. These things have independent versions, right? So you can release a federated convention registry independently of SEMCOMF, so we could say version 2 of JBM depends on version 145 of SemConf. That's totally fine.
if there's a version 2 of JVM, there should be a version… I don't know what you're at right now with Java instrumentation, but I'm assuming it would be 2 to 3, right? You'd make a major version bump of your instrumentation, too.
So the idea is the major version bumps can pair. If you want to actually pair the version directly to the version of your instrumentation, if you're, like, that hard-coded, I think that's fine. Go is an example. I don't know if you've seen some of the Go changes that are coming in now.
for, like, Go runtime metrics, we might just say, cool, you guys can rip out and just keep that in the Go SDK, repo.
and you can version it with your repo. Like, I think there's no problem there, because then if you do a major version bump, you do a major version bump, this is all… that's kind of one of the ideas, is if you're highly tied to your instrumentation, it's totally fine.
Okay.
So… Yeah, policy enforcement, again, you have to do that. Lastly, around stability and OTLP output, right?
In the future, instrumentation libraries will own the stability of the OTLP they produce. To maintain that, we're going to require that they should version pin to schema URLs.
So the idea would be, like, with, GenAI, for example, if you have a separated GenAI SEMconv.
you know, Python would pin to a specific version, it would use Dependabot or Renovate to update that version as GenAI conventions come out, and that there would be some sort of conformance test that makes sure that you abide by that version, and then we use the policies we have for breaking changes to make sure that that specific version doesn't have breaking changes. The same things we use in semantic conventions. So, in the stable by default policy, we say instrumentation can be marked as stable once its code and OSOP output are production ready, but this would mean your federated definitions are stable.
And… to even make this looser, the federated definition doesn't have to live in a specific semcon sig.
in, like I was saying for the Go example, if you wanted to move Go metrics right into the Go SDK, that's fine. If you wanted to create a federated repo that is, like, the Postgres receiver for the collector.
and that's the thing that you own and have major version bumps and defined there, that is fine too, according to this policy, as long as the major version of the instrumentation and the output of OTLP doesn't break.
you can use Weaver to enforce this, you can use Weaver to enforce compliance, you can use Weaver to make sure that, we are documenting to users what's produced.
And that's how we get that.
Okay.
Right, but you're not necessarily Semcov at that point. You're just, here's the definition of what I produce. If you want an example of that, by the way, take a look. Weaver itself, actually.
is going to be producing its own SEMCOV for metrics that it will produce in LiveCheck and logs that it generates, which is funny. The other one that I think is interesting is the OTAP arrow project. They have a bunch of semantic conventions for, like, the arrow conversion and stuff that they do that is defined internally.
And so, you know, they can actually maintain stability of their versions and releases independently of SemConv. Whether or not we ever adopt that into SEMCOV, I don't know.
Right? But… but there's a… Possibility for them to be stable.
and keep things stable, and use all the tools, but we don't have to necessarily create a semantic convention yet. Like, we can figure out when and how to do that.
Alright, lastly, this went into…
**Trask Stalnaker** 27:16 Yeah. Sorry, I didn't quite understand your distinction between What is and isn't a semantic convention?
**Josh Suereth** 27:27 Okay.
**Trask Stalnaker** 27:29 Like, why isn't just defining the schema a semantic convention?
**Josh Suereth** 27:34 It gets blurred. So, I think the difference would be a semantic invention is where we get a project together, and we have multiple We have multiple things that are trying to create the same set of metrics.
So…
**Trask Stalnaker** 27:49 Okay.
**Josh Suereth** 27:50 like, this is where, in Gen AI.
**Trask Stalnaker** 27:52 So, it's.
**Josh Suereth** 27:52 trying to make…
**Trask Stalnaker** 27:54 So it's just a tele… it's just a telemetry schema.
Yeah. Versus a semantic convention.
**Josh Suereth** 28:01 Yes.
**Trask Stalnaker** 28:02 Terminology difference. Yeah, that's…
**Josh Suereth** 28:04 That's… and if you want to call them all semantic conventions, that's fine, in which case we have to go check… change the stable by default policy.
Or OTEP, because it says you can stabilize without semantic conventions, and it's like, cool, I'm fine with that, but I still think you should have a telemetry schema that you keep stable.
That was, like.
**Trask Stalnaker** 28:24 You know that.
**Josh Suereth** 28:24 Check on that one, yeah.
**Trask Stalnaker** 28:25 Makes sense.
**Josh Suereth** 28:26 Yeah.
Okay, I only have, like, one minute left here, so apologies. The last bit is around the notion of a platform release. Again, I don't know… this is… this is all a bit speculative, and I'm fine dropping this completely from the proposal as we find out what the hell a platform release would be for OpenTelemetry, but the stable by default Had this notion of a platform release.
And so, if we're going to have a platform release, the idea here would be we create a platform release, semantic convention that just depends on all of the things that the instrumentation in that release are using.
And so, someone can depend on that, and they get access to everything that's generated from, like, the OpenTelemetry distribution, or release, or whatever it is. Alright, so that's the key components here.
There's this notion of promotion, I think we already walked through that, about how you can be incubating, maturing, what it means to merge.
And then, lastly, how do we know if we're successful? Like, what does success look like in this proposal?
If we can define instrumentation libraries, and let them overhaul their OTLP with a major version bump.
by adopting the new version of Federated Registry, without requiring open telemetry Semantic Convention's diversion bump.
That's, like, the thing we need, right? This is… Java can update JVM metrics without breaking all semantic conventions. Great.
users that can use components of OpenCellar together without conflicts in signal definitions or unexpected braking changes. That's another big thing we need. And so, this success criteria is pretty loose, but that's one of the goals. And finally, Core semantic convention, we focus on stable.
And, we want to focus on things that can accelerate the ecosystem, we also want to focus on, on, like, core, like, things that should be shared. So that's basically what success looks like if this… proposal works, and apologies, I can't stay for more discussion, but Trask, I'm sure you can take it away from there. Thank you.
**Trask Stalnaker** 30:39 Cool, thanks.
**Josh Suereth** 30:40 Okay.
**Trask Stalnaker** 30:58 So, just a heads up that, The… we are… planning… right now, we're in the planning stages of using this federated SEMCOM to split out GenAI SEMCOMs out of the, core repo.
Specifically so that, for multiple reasons, but one is, we want to be able to move faster in the Gen AI, space, and we want to be able to do major version bumps.
de facto stable, Probably do major version bumps every 6 to 12 months.
And also have, sort of dedicated maintainers, approvers of that, semantic convention.
So keep an eye out for more… info there, or join the GenAI SIG.
For more… details.
**Ruediger Schulze (IBM)** 32:07 Hey, Trask, this is really good from the mainframe. So, just out of interest, so, when you say you split out the GenAI content into the federated approach.
So it sounds like, you know, based on the OTEP that was just presented by Josh.
There is sufficient, kind of like, you know.
material around of how to do that, and if we would, maybe from a mainframe point of view, want to do something similar, we could, for instance, follow the Gen AI approach.
That you are just going through.
**Trask Stalnaker** 32:43 Yeah, yeah, so what I would look at, so, this Weaver Examples… is really useful.
As far as… Sort of an example of… I think… yes. So, like, a basic example of something that has its own semantic invention… Uses the tooling to generate the docs, And there's… the various CI things, sort of, that… Josh was talking about, about setting up and running Weaver, and doing all the… Policy checks.
So if you wanted to start looking at that, otherwise, I would expect the GenAI, breakout Hope… hoping to land that in the next… couple of weeks, so you can definitely kind of see how that goes first, and what problems we run into. This is, there's… Definitely, it's a little… it's… it's bleeding edge, But it's… it's… it's really close.
**Ruediger Schulze (IBM)** 34:18 Sounds good, and this is my interpretation, right, that you would then become an own repository under the Open Telemetry organization.
**Trask Stalnaker** 34:26 Right.
**Ruediger Schulze (IBM)** 34:27 Yeah, okay.
Good. Thanks, Trask.
**Trask Stalnaker** 34:31 Yeah.
Cool, any questions about that, or any other topics that anyone wants to chat about today?
**sanjay(IBM)** 34:49 Hey, Patrick, this is Sanjayl.
**Trask Stalnaker** 34:52 Hey.
**sanjay(IBM)** 34:53 So, I have one question, like, we work upon, Some semantics related to storage domain.
And we created PR, but aware that PR got rejected, saying that This is the new… area storage, which doesn't have any active SIG or project.
Hence, it's got closed, so I'd like to understand what next we need to do.
To work on it, okay?
**Trask Stalnaker** 35:26 Yeah, can you drop a link for me to the PR?
**sanjay(IBM)** 35:30 Sure, let me post it.
Yeah.
I post it in the chat window.
**Trask Stalnaker** 35:51 Quote.
storage, cement to conventions… Yeah, so this is, very reli- on point related to the, federated SEMCON, and what kind of has driven us in this direction of federating semantic conventions, is that, this repo… Just, we cannot… this repo can't be the, one place where all semantic conventions across all industry, like, everything goes.
It's just too hard for us as maintainers to have that, Expertise, maintain all of those, etc.
So… In the past, what our answer has been before Federated SEMCON was, okay, you need to go and get a group of folks together, in the community.
And… start a project.
To… so this… you can see an example, let's… take, mainframe.
Where you write up a project, you get, you know, staffing and sponsorship.
And that allows you to move forward within the semantic convention repo, while we ensure that we have enough people, who are dedicated to that project to make it successful.
Now, with the federated SEMCOM, we have a… another option. So, you… if you want to do it inside of the OpenTelemetry community.
You'll still need to create a project and gather together, you know, staffing and sponsorship.
Even if we do it in OpenTelemetry in a separate repo inside of OpenTelemetry, sort of the way Rudiger was describing for a mainframe, like, they might want to move the mainframe SEMCOM out of the general SEMCOM repo, but still under OpenTelemetry, and still with an OpenTelemetry project SIG, for that.
So… you can do that, still, that's another option. But still, another option is if this is something, you know, very specific to, That, you know, you can… if you just need it for your company or something, you could create it external to OpenTelemetry and publish your schema URL for it, and other people could consume that.
Sometimes there's another standards body, like we're in, chatting with the OCSF, security folks, which is a… another Linux Foundation project.
And, in that case, you know, it may make sense for them to own some of the security semantic conventions.
So there… if… I don't know if you have, you know, if there's sort of a standards body that you're working with already, that's another option.
**sanjay(IBM)** 39:42 Okay So, just, so to make it clear, so one way is go and create projects. So, anybody can create projects, or we need some… Authority to create projects.
**Trask Stalnaker** 39:58 So what you'll do is you'll send a pull request.
To create one of these project files, but you'll need to show, you'll need staffing, is the main thing.
We want to see that there's, you know, Domain expertise across, you know, multiple companies coming together.
And then, And then, you know, getting the… TC and GC support is something that, you know, we can do, once we see that there is, Sufficient staffing.
For the… the project.
**sanjay(IBM)** 40:44 Okay.
And another way, you mentioned that, we can have our own, branch out, and saying that this is what is for the company-specific time being, till it get, went through the Community process, correct?
That also can be… Oak.
**Trask Stalnaker** 41:09 Yeah.
**sanjay(IBM)** 41:11 Okay.
So, let me go through this, and then I will come back with some questions in next session.
**Trask Stalnaker** 41:19 Okay.
**sanjay(IBM)** 41:20 Mike, thank you.
**Trask Stalnaker** 41:29 Alright.
Thank you all, and see you next time.
**Christophe Kamphaus** 41:34 Still…
**Armin (Dynatrace)** 41:39 Okay.
**Ruediger Schulze (IBM)** 41:39 Thank you.
