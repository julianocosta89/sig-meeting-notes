SIG: Specification SIG
Date: 2026-05-26
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 03:31 Hi, everyone.
**Tigran Najaryan** 03:45 Oh, my mom.
Well, folks from TC, do you guys know if it's my week?
**Reiley** 04:08 because…
**Tigran Najaryan** 04:09 And mine? Yeah? Okay.
Wasn't able to find the schedule. Okay.
I'm gonna share my screen.
**Ted Young** 04:22 Do we have a project that wants to do a report back this week?
**Tigran Najaryan** 04:32 I do not know, I don't see anything in the agenda.
**Pablo Baeyens** 04:38 We could talk about… collector B1, I… Don't know if… Alex is here. Let me ping him. I guess we can get started on how… Let you know in a bit.
Yeah, we can'.
**Tigran Najaryan** 04:54 get started, we have only a few small, I guess, short items here, so maybe there should be enough time remaining you can go at the end.
Alright, the release is out, this is an FYI.
The link doesn't open, so either the ring is wrong, or we haven't.
Hit the publish button.
Who was? Who did the release, guys?
Anyone on this call?
Okay, we'll need to double-check that.
Someone was saying something.
**Josh Suereth** 05:35 Oh, I think it was Carlos, but I don't know if he's here.
**Tigran Najaryan** 05:37 Okay, we'll check with Carlos.
Maybe he didn't… he didn't hit the publish button. Okay.
Alright.
Ready for merging, or no? Is evil here?
**Ivo Anjo** 05:50 Yes, hello. So, thanks, Tigran and Robert, for the feedback, and I… I… I think I have a, kind of, I've, accepted and did a few commits to incorporate all that feedback, so I guess let me know if there's more feedback, or if you can kind of merge this in.
**Tigran Najaryan** 06:17 I think I should be good to go, if anyone else… Is interested in taking a look.
I'll keep it open for today, but otherwise we can merge it. We have enough approvals here already.
We made a decision that it's the right place to have it in this repository, so we should be good to go.
**Ivo Anjo** 06:36 Thank you!
**Tigran Najaryan** 06:41 Alright.
Acceptance for… Is Nimrod here?
**nimrodavni** 06:52 Yes, hi. This is actually very related to what Ivo just showed. It's basically an expansion of the, resource, sharing protocol, just adding, instrumentation information. And this is mainly, like, our use case in OB is to… basically allow, like, see if the SDK is already instrumenting some protocol, and if so, we can, avoid Duplicating the instrumentation for it.
And I have… we have a couple thumbs up here, also from Ivo, a commenter, so I just want to know if it's okay to continue to a PR phase, and, I guess open some, you know, some document for it.
**Tigran Najaryan** 07:39 So it's a proposal to extend the proto files, primarily?
Is that…
**nimrodavni** 07:44 I think it's just one… one field. There are some, like, caveats and things we can consider if we need, do we put the raw name of the instrumentation, or do we try to classify it of, like, what, namespace does it instrument? Because, I know HTTP instrumentation for… I don't know, between different, let's say, libraries or even languages, the name can be different, but that will require additional work in the SDK side, but maybe we can start off with just Just the name of the instrumentation.
And Obi can do, like, the mapping of, like, I don't know, express implementation means that we can skip HTTP, or whatever.
**Tigran Najaryan** 08:33 Yeah. If this makes sense for OB Fultz, I don't see why not. Anybody on this call has an opinion.
**Pellared** 08:40 I support this proposal.
**Ivo Anjo** 08:45 Was one…
**nimrodavni** 08:47 Okay.
**Tigran Najaryan** 08:50 Okay, make a proposal, we'll take a look.
**nimrodavni** 08:53 Cool, thank you.
**Tigran Najaryan** 08:58 Ricardo, looking for more input on trace continuation strategy.
**Riccardo Magliocchetti** 09:05 Yeah, like, we have a discussion open. If… Where, Anurag is proposing to implement something, differently.
At the moment, this proposal, just, Enhance the current propagators.
But this has some limitation, like, like… Does not work for every use case we have.
when we want to handle the continuous strategy of tracing.
And Anurag, again, is proposing to implement something like a sampler, but not a sampler.
And so… was wondering if… Anyone want to take a look at the proposal? And especially in the… we have a thread with a bunch of comments.
And, yeah, like, I'll spend some time drafting a prototype following Unranked suggestion.
But, like, before spending too much time, I prefer to have, like… More inputs to see if there's a consensus.
towards a direction or not. Thanks.
**Tigran Najaryan** 10:30 Anyone from the tracing or trace context, maybe Jay Magdi, Daniel, Diala, do you guys have any thoughts on this?
**Daniel Dyla (Dynatrace)** 10:48 I'm sorry, I was, not paying attention.
**Tigran Najaryan** 10:53 If you get a chance, then maybe you can take a look at this. This may be…
**Josh Suereth** 11:04 Yeah, I want to jump in. Sorry, we've been running into this issue really, really, really problematically inside of Google, for our services that interact with Trace. So, like, thank you, Ricardo, for putting out a proposal, because I think you and I discussed this offline. I really think we need to look at it. I haven't had a chance to look at Honorogs, but I think, the basic gist that I want to call out is there's some kind of an interaction between tracing and authorization.
And understanding if, like, you are working on behalf of something else, and having, like, an internal trace and a public trace, when you're dealing with a SaaS product. And so, the notion that you could say, like, I want to drop the external trace context, I think is, like, a step one.
And I think there is further we can go, and we'll have to decide, I think, to avoid bike shedding too much.
Which I don't want to do to you, Ricardo. We should make sure we're nailing which use case we're going to target initially, and make sure we can evolve into something nice. That would be my main concern, is if you look at this proposal just at face value.
And try to simplify it. You could, but then you might not solve the end problem, which is what we actually need to solve, which is how does, like, someone running software as a service actually provide tracing where people want to trace their call through your service, and you need to trace your own service at the same time?
So, like, the whole, like, drop, keep, you know, make a new thing, totally makes sense, but I don't know if it's enough controls, but I think it's a really good start. And the alternative of, like.
do we want this to be a separately controllable thing in the SDK? Possibly. And I think the question I have… to answer that would be, you know, where do I understand if I'm at a kind of authorization boundary of a SaaS product, right? So where do I know that this instrumentation I'm dealing with is actually, like, for somebody else's trace, and not, like, my own self-trace that I want. So how do I make that decision?
So, it's possible that having a new SDK component makes sense there. I'm still dubious without someone showing an end-to-end example of, like, what that would look like, how it's configured, and how it interacts with all the rest of instrumentation.
**Riccardo Magliocchetti** 13:25 Thanks for the feedback again.
India.
Yeah, I'll try to provide visa.
other implementation inside the SDK, incredible eyes.
But, yeah.
But again, if anyone else wants to take a look, Maybe, share some concern or use cases, we're more than welcome.
Thank you.
**Tigran Najaryan** 14:04 Alright, let's move on.
Robert.
**Pellared** 14:16 This one, I think I'm just asking to be merged later today. I think it got enough approvals.
And, already some languages, at least in Goe, it made a fix.
Maybe you can wait until the evening, I'm sure.
Or you can click no? Yeah, thanks.
**Tigran Najaryan** 14:38 It's been opened for a while now.
**Pellared** 14:40 Yes, indeed.
**Tigran Najaryan** 14:40 True.
**Pellared** 14:44 As a follow-up, I also added limits to the declarative config. I just didn't want to do it to do not have too many work in progress, because I already had too many.
The next one It's a similar thing It's, regarding entrimeter variable, environmental carrier queue normalization.
it has 4 approvals, it doesn't, maybe… I don't know if it feels enough, but these are all people who are, who are involved into implementing those, or specifying those. I mean, CICD, group, or people which are actually implementing, including Jack from this PC.
**Carlos Alberto Cortez** 15:25 Yeah, from the, CACD group, Adria had already reviewed that, so that's a good sign.
**Pellared** 15:34 So, maybe giving one more day and version will be good.
As far as we checked, this seems to be the last part blocking the destabilization, and also it would be good to have more languages implemented this career, but I think, like, already 5 languages implemented, or something like that.
Let's go forward, if you have no questions.
Settlers.
**Tigran Najaryan** 15:58 Yeah, you have the… the number of… formal number of approvals needed.
So, shouldn't be possible to merge.
The next one is yours as well, Robert.
**Pellared** 16:13 Exactly. So, this is a non-UTLP, transfer, non-OTLP, like, representation for attribute collection. This is just a follow-up from the previous PR, which was for single attribute, and this was all… this was also, like.
discovered by, also by Jack, that this part was missing as well.
Just to have it formally.
It is, like, obvious that this is the way we would represent it, but just to have it, have it in the specification.
So, asking for reviews.
And is it the last one? Oh, there's one more?
**Tigran Najaryan** 17:02 Thanks, Silver.
**Pellared** 17:03 Any questions, but I don't think there should be any, because this is… if there will be questions, they will be the same as for previous one, for a single attribute.
I think that's all, and I think it's time to… Pass the voice to Ted.
Thanks.
**Ted Young** 17:18 Sure.
Thanks. Thanks, y'all.
Yeah, we've got OpenTelemetry general availability. If we don't have, any projects that want to present this week, we can dive into this subject. Looks like Collector wants to.
**Tigran Najaryan** 17:35 Do you want to share, or do you want me to continue sharing? What do you want to?
**Ted Young** 17:38 You can continue sharing, I think it's okay.
There aren't, like, specific things in here on the doc that we necessarily need to go through, but if you haven't seen this, just to let you know, what we're trying to do is sort of summarize a roadmap of everything we need in open telemetry to sort of put a bow on the original scope of work for the project. The original scope of work was tracing metrics and logs, integrated everywhere in, a large number of popular languages, and, Along with a telemetry pipeline through the collector to get all of that out.
And we've done a ton of work, we've graduated now, but… and we're moving on to lots of, like, more projects, like profiling, like, you know, browser and mobile clients, and, like, all kinds of other interesting things, you know, even, like.
next-gen protocols, like Arrow and all of that fun stuff, but… We need to… finish what we started, and there's still a lot of things, kind of, like, loose ends that we want to tie up, to get OpenTelemetry, you know, into, like, a fully stable, satisfactory system.
And it's quite a bit of work.
There's a number of different work streams, so I'd encourage people to look through this doc. I'm going to try to flush My plan is to have this in sort of two stages. One is flush out enough in this document around each workstream that people feel like there's agreement, especially the the SIGs that would be taking this work on.
And then from there, figure out a way to kind of manage each work stream on its own, working with the people who own that work stream.
So, have a look at this. In terms of, like, specific things that have come up, based on, you know, Q&A, one is some people want to bike shed about what we call this scope of work. We originally called it stable by default.
found that confusing. General availability is, like, a term we've used a lot. Not everyone likes that. Production readiness was another term thrown around, but that's also confusing because, like, OpenTelemetry's already in production everywhere.
I don't think there's a perfect word, but if you want a bike shed on that, my request is we do that on Slack instead of on the, GitHub issue, and keep the GitHub issue focused on the content. But I do promise, if there's consensus about better words, I'm happy to swap these words out.
That said, in terms of the actual details, a work stream that got brought up that we hadn't included here is OpenTelemetry self-observability. This is a thing we actually saw, you know, through the graduation process. People, pointing out they wanted… Better self-observability, especially around back pressure, for example, when our pipeline is dropping data, not because it's being sampled out or anything like that, but because of back pressure.
better reporting on that. We do have some amount of, like, self-reporting, semantic conventions.
But their rollout is maybe, you know, like, kind of patchy, so I think it's a mix of, like, what still needs to be rolled out everywhere, and what is actually missing from our design that end users would want.
In order to have, like, a fully self-observable open telemetry system. That seemed like an important part of GA, right? Like, if our system's hard, ironically hard to observe when it's, In, you know, in a state.
That feels like something we should fix.
That is a very narrow window. There we go.
So, that's a workstream I'm looking to add. I would love people's feedback. Maybe we… we've got plenty of time in this meeting, so maybe we can stop on that right now. We've got lots of maintainers. Maintainers, what are your feels on self-observability of the SDKs right now?
**Tigran Najaryan** 22:11 And on that specifically. Yeah, sorry, go ahead, Brighton, you had your handle.
**Braydon Kains (Google)** 22:16 Well, the question's about… oh, sorry, can you hear me?
**Ted Young** 22:19 Yep.
**Tigran Najaryan** 22:19 Yeah, we can read you, go ahead.
**Braydon Kains (Google)** 22:22 If the question is about SDKs, then I can't answer. I was just going to say that the Collector 1.0 already, like, nominally includes a ton of self-observability work and changes to the pipeline self-metrics, so I don't know how we rope that into this workstream, but, like, it's a big part of Collector 1.0 stuff already.
**Ted Young** 22:41 Awesome.
Yeah, I think, I think, you know, that's great that it's there. I would keep that in the collector work stream, just because, you know, the collector sigs owning that work stream.
But… but yeah, understanding… being able, as the end goal, to present people, like, a very straightforward doc on our website about, like, here's how you self-observe open telemetry, like… And giving peop- being able to give people, kind of like.
playbooks and things like that around OpenTelemetry would probably be, like, a great addition to our documentation.
But I think we have to understand what the plan is first. So that's great that Collector's working on it.
Okay, Tgrin.
**Tigran Najaryan** 23:24 But on the, yeah, on the self-observability thing, this is a general comment, not about just that thing. I think there's many things that we will continue working on in OpenTelemetry, adding new capabilities over time, and that's fine.
I would be reluctant in maybe bringing more things into this initiative.
Because it seems like it can be a never-ending thing if we try to do that. We don't have to cover everything that OpenTlemetry Possibly can do in this project.
That's… that's just… it's gonna be an extremely large scope, right? I would try to do the opposite, see if there's things that you can remove from this, so that it becomes more manageable and easier to finish.
In my opinion, what we need to do here is, for things that are already part of OpenTelemetry, but they are not of sufficient quality, right, so that we can say that it's 1.0 or GA, whatever is the label we choose, then those should be in scope so that we can complete those things.
but not bring more stuff, more new stuff, so that we can now complete that other new stuff. So this is sort of a meta comment about the scope of the project. In my opinion, self-observability is like that. It's important.
But I don't necessarily see that as… as… Something that we should bring into scope of this project.
**Ted Young** 24:56 I think that's… that's totally fair. One thing, you know, that's… kind of confusing people is, like, the term GA versus 1.0, because we've got plenty of components that are… some of our issues, we have de facto stable things, things that are still less than 1.0, still not marked as stable, and yet have been in production forever, right? Like, the collector, all of our instrumentation.
So, some of it is, like, literally getting these things to 1.0 and marking them as stable, and, like, what's the minimal amount of work we need to do there, versus work… To do in the future.
But some of these are, like, improvements to things that are already multiple major versions up, like the SDKs.
I could see this as going into a second category. I try to put performance in that category for that specific reason, right? Like, there's a desire for performance, and like.
being able to take, like, the benchmarks that some SIGs have done that we're, like, happy with, and maybe try to generalize them, and I feel like that's really important work, but it's definitely not, like… that to me feels like improvements, as opposed to, like.
We literally can't mark this as stable or done because we don't have performance benchmarks.
But I also don't want to discourage people from working on this stuff. So maybe out of scope's the wrong name for this section.
But you're right, maybe these are just to separate out specifically what we need in order to stabilize things, and finish out what we started, versus, like, hey, this is the next step of, like, really important improvements that we see on this set of core technology.
That we're offering people.
Great. Diego?
**Diego Hurtado Pimentel** 26:47 Yeah, regarding these, the scope that the project should have.
and not including things, I just worry a little bit about what could happen in the future, considering that this project was… It started because there were many standards, right, that, we're competing, I… feel like OpenTelemetry is a great place to avoid that from happening again, which is pretty much the reason why the project exists. So, if the industry Needs a new feature that's important.
I think it'll be better to include it.
Instead of just letting it live.
Outside the project, without a standard, and then… Let it… it become competing standards, and then finally deciding to integrate it in a project, right?
**Ted Young** 27:50 Yes.
I think this is an area where we want to clear up our roadmap. Part of it is, like, we really want to keep Like, you know, keep improving the core set of offerings, but there's also, like, the industry is, like, wants to move forwards and actually experiment and come up with things that are fundamentally better.
And we actually have, you know, some Skunkwork projects already on that front, right? We have a couple different SIGs working on new protocols, right? We have cool tools like Weaver and things like that. And one of the things I want to do with, like, our… the way we have our project managed is to maybe… It may get a little more clear what's… what's what, on that front.
But I also think we'll have more room to, like, breathe and think about that stuff once we've gotten through some of this stuff on this list.
I think there's some evergreen things, like performance, but there's some stuff on this list that's sort of like a one-time thing we have to get through, and something I'm trying to do is make sure we actually finish that before we get completely swamped with all the new, interesting things everybody wants to do.
Because that's kind of been the… we tend to be picking projects, because people come in and they're, like, excited to work on something, and like, we're ready, we have our shovels, there's a workforce, we want to do stuff, and we don't want to tell those people no, because they're excited, and we want them to, like, be successful. But we've also been feeling, like.
that work kind of, like, competes with maintainers' attention to, like, finish this stuff, so… But I think if we can get through this round of stuff, we'll have, like, a lot more space to think about, like, what's the cool next-gen stuff we can work on.
Cool. I saw some hands go up and then back down.
Okay.
So that was, again, you know, getting back to self-observability, I like that idea of, like, you know, not calling this out of scope, but having a better name for it. It's like, you know, improvements, as opposed to… you know, core requirements, or something like that, and putting it there. But I did want to say, I thought this was a good workstream for us to think about, because it does… this did pop up, not just as, like, a like to have, like, we did see a lot of, like, community response around Some frustration around, you know, how do you self-observe OpenTelemetry.
The other area I think of is, like, when you first install OpenTelemetry, and it… if it works out of the box, it's great, but if it doesn't work out of the box, that can be a confusing experience, because those people are usually using OpenTelemetry for the first time, so their ability to debug anything is, like, super limited.
I'm not sure exactly what we can do to improve that experience, but that's the other place where you know.
Having, like, better playbooks and better reporting could… could help people, you know, debug their installations when they're kind of failing to bind properly.
Braden?
**Braydon Kains (Google)** 31:09 In my experience, trying to get customers and internal teams onboarded to OTEL and, like, making that out-of-the-box experience work best. It feels like the only way to scope it well enough that we can, like, make sure it works is to target environments. So, like, if we were going to scope that kind of out-of-the-box work, it would be, like.
make it work really well on Kubernetes, or make it work really well on a VM from a cloud provider, and, like, scope it that way, because there's… As soon as you start getting… Into each environment, there's different work you have to do entirely to make it work nice out of the box in those different ways.
So probably if we can…
**Ted Young** 31:48 Absolutely.
**Braydon Kains (Google)** 31:49 Yeah, scope the most popular environments, that sort of thing.
**Ted Young** 31:52 you're playing my favorite song, and just to let people know that part of this work is looking at that. We're looking at two environments to start with, Linux and Kubernetes. On Kubernetes, it's… and on both of them, it's about, the primary thing is having an installer That can install… every language that has some kind of auto-instrumentation hook, you know, can we get that installed in those environments, where the user doesn't need to have any language-specific understanding?
Because we… many languages have some kind of way to bootstrap and auto-install everything, but you have to learn how it works for that language, and also, if you have to touch every single application individually, that's a big barrier for, like, a big organization. So we want to move away from that and to… having some wrapper, the Kubernetes operator or Linux system packages.
**Braydon Kains (Google)** 32:55 Were you.
**Ted Young** 32:55 You have some way as, like, an operator of deploy this stuff globally, and have that work for, like.
**Braydon Kains (Google)** 33:02 So…
**Ted Young** 33:03 Most of what we have available.
Right now in Kubernetes.
through the operator, there's some limited ability to do this, right? Like, it can handle a couple of languages, but there's still also some…
**Braydon Kains (Google)** 33:15 Right?
**Ted Young** 33:16 Kind of, like, deployment-specific annotations and things you need to put in there.
And the System Packaging SIG just kicked off, so if you're interested in that work, definitely join the System Packaging SIG, come into our Slack channel and say hi. If you go to the community repo, you can find all the details there.
The third piece of that is OpAmp.
And the supervisor, that's another way to do this, that we want to be poking around at.
Michelle?
**Michele Mancioppi** 33:49 Public service announcement about system packages and OPAMP. So, we are in the process of, speccing the way the system packages are going to work.
There is APR in the, OpenTelemetry-packaging repo. Please go and have a look at that. It's, it's important to get it right.
And, specifically between system packages and OPAMP.
There is, in the SIG for system packages, we need more expertise with the PAMP, and if some maintainer of the PAMP SIG can join us.
We would love to make sure that what you're cooking for system packages will work very nicely with OPAMP as well, where the experience is you go and make APT, install OpenTelemetry, and then you have an experience where an OPAMP then delivers all the other configurations needed.
We lack some of the expertise to make that on our own, so please come and help.
**Tigran Najaryan** 34:54 I can take a look at it. Can you send me the link, or maybe put it in the agenda doc? We can even open it now.
Or in the chat, whatever you prefer.
**Michele Mancioppi** 35:03 I'll do both.
**Ted Young** 35:06 Yeah.
We can definitely… we've got plenty of time, so we could definitely dig into this, in this meeting.
let me just get through the other places we're looking for help, and then maybe we could circle back into having a discussion about this, because I think it's definitely an important place. We want to have, like, some commonality across declarative config, system packaging, op-amp and the supervisor, and things like the Kubernetes operator, understanding what You know, what's helpful across all of those different things, would be… would be great.
But, just real quick, the other places we're looking for help… is, instrumentation is the biggest bugbear in this whole affair. We have lots of instrumentation that's been left to the community in terms of these contribib packages.
A lot of these packages got donated early on, you know, to OpenTelemetry. For example, there was a big round of donation where Datadog said, hey, you could… you know, steal a bunch of our packages, but we're not gonna, you know, we don't have the resources to port them over, and then LightStep had the resources to port all of that over, and LightStep's been acquired and evaporated, so, like.
And a lot of other packages are probably in a similar state, where they were brought over at some point, they have some amount of nominal maintainership, maybe. But, In general, you know, keeping them up to date with the latest versions of the semantic conventions, responding to, like, any bugs or problems in them.
That's… that's an issue. We would like to get these things marked as 1.0, not meaning 1.0, the semantic conventions have gone stable. We've kind of changed our definition there to match something That more matches what end users expect, but just to say, hey, this package is, is, like, actively maintained, someone's willing to look at it.
That's… and it's safe to run in production.
That's enough to mark it as 1.0, and if the semantic conventions improve at a later date, we can bump it to a 2.0, you know, to indicate that.
But just getting everything out of the 0.X. But the pushback we got was, like, we don't want to just blindly mark these things as 1.0 if there's no one around to, like, actually take care of them.
the SDK maintainers generally feel like they don't wanna… Take on a whole bunch of community… Package management, because they're… they have limited capacities.
We have a couple of languages where, you know, there's a more healthy ecosystem, but this, to me, is like, we need better tooling, we need a better way of managing at least some of these, if not all of them, and we probably need more people to help with this.
So that's a big pile of work with a bunch of open questions. I'm gonna try to figure this stuff out, but I would love help.
brainstorming about how to do this. Even basic things like doing an audit of our whole ecosystem and figuring out what's maintained and what isn't, and stuff of that nature would be super helpful. So, if anybody wants to help me chart the landscape of instrumentation and, you know, figure out a game plan with the community.
Definitely reach out to me.
Because I see that as, like.
The least straightforward of all of the things we need to figure out in this roadmap.
Yeah.
Always get a lot of silence on this one.
But moving on, the last piece that I think is also really important, that's kind of a meta thing, is we want to change how we do roadmapping and project management. You know, we've… been, sort of.
we initially had a setup, we have a governance committee, and we have a technical committee. The technical committee was originally basically the people writing the spec, because that's how small the project was.
Then the project grew and grew, and the technical committee turned into kind of like, you know, the sort of technical architects or managers of the project, and the governance committee kind of turned into the project managers.
And we've been making incremental improvements through, like, project files and, like, at least understanding all of the pieces that need to be in place before a project kicks off to make sure that it has success.
And I think all of these improvements have been helpful, but there's been a feeling like, like, we could do a deeper overhaul of how we do this in a way that gives more agency and inclusivity to the maintainers.
And make it more of, like, a community effort to figure out our roadmap, and to also have, like, a clear and more well-published roadmap.
I think one of the issues when we try to publish a roadmap, you know, if it's just the GC figuring it out and then publishing it, you know, that's just kind of… like, there's just sort of a disconnect, it feels like, between the two levels of… of… of… Management that we have in this organization.
Everyone's trying really hard to make it all work, but it feels like, structurally, we could shake things up, and this is a good opportunity to do that.
So, this is something we've been thinking a lot about on the GC and the TC, but we would love maintainers' thoughts about what you all are looking for, other projects or other things that you've been involved with.
Where you feel like this works well.
I think OpenTelemetry is, like, a little unique in the sense that it's a very federated ecosystem, but also one where, like.
There's a lot of self-similarity between the different pieces, so there's still a lot of need to kind of coordinate our efforts if we want to offer something that's coherent to our users, but at the same time, there's a lot of room for independence.
So… you know, this is something we're generally looking to improve, and that's why it's on this GA roadmap, because I feel it's important at this time to… To have some coordinated effort into figuring out a better way of dividing this work up and managing it.
again, it's a pretty big topic. I feel like it's so big, it's, like, hard for people to kind of get a handle on it and have, like, a good conversation.
But if this is something you're interested in, reach out to me on Slack.
And I'm gonna try to keep the conversation going on Slack as well, in the main OpenTelemetry channel, just to get more community involvement in, and the maintainer's channel.
Rather than just this meeting.
But… Yeah, any big thoughts on that? Big feels?
Okay.
Well… That's, my list, for today. That's… that's your update. I will keep pushing this.
asynchronously.
And we can maybe circle back to the conversation we were having earlier about… about op-amp and system packaging and all of that.
So… Who wants to take the reins?
**Tigran Najaryan** 43:12 Thank you, Ted.
There's nothing else in the agenda, guys. We can talk about what is it, the packaging, go pump, or whatever else.
If anyone has topics.
Or we can give back almost 20 minutes.
If there's nothing to discuss live.
**Michele Mancioppi** 43:41 About the system packaging and, OPAMP.
I, If you want to start now, great. If instead you want to have it in one of the SIG meetings of either of the SIGs.
Wraith as well.
**Tigran Najaryan** 43:57 Yeah, we can talk about it, we have time, but what sort of input specifically are you looking for?
**Michele Mancioppi** 44:02 So, the, the idea for the system packages is that, we want Effectively, we're taking the auto-instrumentation, so think of the Java agent, think of the Node.js out-instrumentation package and all its dependencies, for Python.
Putting them in, language-specific system packages.
Which puts, like, the OpenTelemetry, there's note, there's auto-instrumentation, contains 15, 20, 50, NPM packages for the other instrumentations, plus the SDK, and then activate at runtime, inject the SDK through the open connection injector.
That is, the opportunity jet is also being used in, it's been added to the operator, OpenTech operator, to use the same… the same mechanics.
And the question with OPAMP is the following. So, we are thinking in the system packages to use… to build them based on declarative configuration.
There is the… very much the need with automatically injected instrumentation to be able to turn off instrumentations you don't want.
for example, DNS instrumentation in Node that nobody likes, to make an example.
That, given the fact that, it is… the behavior of the declarative configuration is unspecified, what happens if you ask to turn off an instrumentation that doesn't exist?
We think we cannot share.
The same declarative configuration file between different languages.
Which means that each… each system pack… each language system package, the one for Java, the one for Node, comes with its own decorative configuration file.
Now, if you want to use op-amp, And… use, the, the supervisors in the SDKs, like what we're doing, what Java is building.
Then you would need to configure a PAMP, For each of the languages in the decorative configuration file.
And that is a whole chunk of work that We are not sure it's good for the user to have to do for every language on every Linux host.
So, something that is unclear to me is what is the correct trade-off between, having different the criteria configuration files per language, and make that work well with the OPAM supervisor.
**Tigran Najaryan** 46:39 Are you… are you proposing to also install Collector by default with the… with the system packages on the host?
**Michele Mancioppi** 46:47 Not by default, but something that… the collector is something that we kept on purpose for Phase 2. Phase 1 is having a small set of languages and injector work very well together. In my mind.
the collector, DEB and RPM packages should be… should become part of this family of packages, and have a very cohesive experience, because these things are targeted at Linux hosts. You do want a collector on those.
to collect syslog D and all the rest of the fun.
So, I would love for that to happen.
**Tigran Najaryan** 47:25 But the reason of why I'm asking this is if we could rely on the existence of the collector on every host.
Then all the, all these implementation packages can be pre-configured to point to that locally running collector as the source of an old pump.
information, and the collector then would be essentially a proxy that would then connect to the actual destination managing server. And so that would allow you to point all the instrumentations to the same local O-Pump op-amp accepting collector, and have the same, essentially then having the same configuration. It would solve the particular problem that you were describing. Then the collector would be responsible for figuring out What is the destination to connect to, and if the received configuration needs to be per language, if it needs to be altered, even per language, the collector could do that processing, additional processing of the config, and send back to the connecting instrumentations, if necessary.
**Michele Mancioppi** 48:31 So this assumes that every single SDK we inject knows how to talk op-amp, right?
**Tigran Najaryan** 48:39 Yes. Yes.
**Michele Mancioppi** 48:43 And as far as I know, we have an OpenAmp extension, In Java.
Which is not yet part of the… default Java agent build, I wanna say, but I'm not sure.
**Tigran Najaryan** 48:55 Yes.
**Michele Mancioppi** 48:56 So…
**Tigran Najaryan** 48:57 Yes, sir.
**Michele Mancioppi** 48:57 That's… that's.
**Tigran Najaryan** 48:58 As far as I know, we don't have it implemented in all the languages, at least that's true, yes. It's sort of work in progress, I believe.
**Michele Mancioppi** 49:08 I think Ricardo has had the hand up.
**Riccardo Magliocchetti** 49:11 Yeah, like, I think we have… like, at least we have one for Python, even if Python is not on by default for the injector.
And I think also, maybe Trent, correct me, like, maybe also not as an OPMP… Implementation as well.
**Trent Mick** 49:28 We have one in our client… opam client in our distro, I'm happy to upstream it. There just hasn't been… that desire. Like, it hasn't been a… Higher priority, because… I haven't seen op-amp used.
Externally. But yeah, definitely can upstream what we have.
**Tigran Najaryan** 49:45 So, anyway, what I was describing is one possible architecture where the SDKs or instrumentations actively establish OPAMP connections to a locally running collector. Essentially, they need to be OPAMP client implementations. But you're right, that's not the only way. We could do a completely different architecture where the configuration for the SDKs or for configurations is based on the local config files.
And those config files are managed by the… either the collector or something else that implements OPA.
open protocol, right? It could be the centralized configuration manager for all of the… all of the instrumentation packages you have running locally. That would be a different possible architecture. I think we have a number of options here. Somebody has to think through the implications of those and make a proposal of what do we want to do there.
**Michele Mancioppi** 50:43 What I'm hearing is that No, more than just hearing. So, my extrapolation is, op-amp should be up in.
It's not the default way of managing configurations.
Well, at the moment, we do not have it built in in our SDK, for example. That may happen in that, in that, in that case, we could, we could revisit.
I can imagine…
**Tigran Najaryan** 51:10 I agree with the assertion that Open needs to be an opt-in. Yes, definitely. And you have to opt-in somehow, because you have to specify what's the destination server, right? Without that, it doesn't work.
**Michele Mancioppi** 51:23 So I could imagine a package that effectively delivers the configurations to make The SDKs dock op-amp with the nearby collector.
It's… I don't…
**Tigran Najaryan** 51:38 It's more work, though, right? That's, like I said, that's a possible architecture. I am not sure that's the best architecture.
**Michele Mancioppi** 51:44 Yeah, neither do I.
**Tigran Najaryan** 51:47 Hedge.
**Ted Young** 51:49 Yeah, I think one interesting thing that's kind of glued together but could be teased apart is there's op-amp and there's the supervisor, right?
If we're talking about op-amp, you know, we're talking about a protocol, and like you're saying also, like, how do SDKs… One advantage of something like OpAmp is there's some aspects of configuration that we want to be hot reloading or, like, live updating, things that are more like rule sets, right? Like, sampling is probably the biggest ask there, you know, remote sampling control and things like that. But then there's also, just having a control plane that manages the installation and configuration.
Of all of the things. And if you look at the supervisor, and if you just said the supervisor.
installs the configuration files, and then even potentially downloads the bits, you know, and installs them, then the supervisor is effectively a control plane managed, you know, packaging system at that point.
So, it's sort of like two separate.
**Tigran Najaryan** 52:57 Which I wouldn't do, I would stay away from that, because we already have package management systems on Linux hosts, right? So why replicate that functionality? So maybe we don't do that piece, but the configuration piece is still actual, right? You want to have something like that.
**Michele Mancioppi** 53:13 Exactly. So, the configurations will live in AHTC, ETC, which is supposed to be modifiable by the user, or from additional packages, so that would be perfectly fine.
**Tigran Najaryan** 53:24 Yep.
**Ted Young** 53:25 Yeah.
But this is maybe a thing we can kind of clarify with, like, the SDK portion of OpAmp, is, like, is the goal ultimately for it to be about, like, managing everything, or is the goal to have, like.
you know, file-based config be a way of doing it, and basically teasing out the general, like, how do I get the la- and update the configuration, general configuration for SDKs? Like, how do I push an update out for those?
Versus, like, how am I doing, like, live management of, like, the aspects of the SDKs that… where it's more like rule sets and things.
**Michele Mancioppi** 54:06 Interesting point.
**Ted Young** 54:07 Trying to understand the difference between those two use cases.
**Michele Mancioppi** 54:11 I mean, technically, they're not, they're not orthogonal. The, with op-amp, an extension in Java, you still need a bootstrap configuration that tells the agent to use op-amp.
That is something that should come from system packages, and then opam takes over and overrides stuff.
**Ted Young** 54:28 Right.
Anyways, it would be great to have that whole story.
**Tigran Najaryan** 54:33 We need a design, definitely, yeah, I agree with that, yeah.
**Ted Young** 54:38 And then also the upgrade.
**Tigran Najaryan** 54:39 value in that, right? So, particularly, like you said, for sampling, you want the sampling changes to be possible to do live without restarting the whole thing, right? And OPAMP is a way to do that, essentially, a possible way to do that.
Now, whether that requires an active connection using an actual OPAM protocol from the SDK to whatever is the Controlling destination, or you do it Using a file, and then poultryload as a concept, so that then the SDKs can watch those files and do the adjustments on the fly. That's also an option. Possibly an easier option, I guess, right? Maybe it's easier to do.
I think we need to have these designs maybe side by side, and do some comparisons, cons and pros, and make a decision about which way to go.
**Michele Mancioppi** 55:32 I've heard of organizations doing either, some that really want the files to be distributed, like, for example.
We're talking Linux, it's not like a GitOps workflow, but the usual configuration management systems that they use to deliver configurations and packages, and others that went all-in on Open, and then have it pretty much all dynamic, and the only thing they ship is just a, hey, go and grab stuff from over there.
It's, then it might be that we should allow both, because they kind of cater to different philosophies in adopting organizations. And at scale.
Those opinions tend to be pretty strong at an organization level.
**Ted Young** 56:17 And the third piece that I think we should directly involve in this conversation is the Kubernetes operator. Maybe there are other approaches to managing all of this on Kubernetes, but right now, the operator's the way we want to do it, and it's sort of the same thing, right? Like, if you're using the operator in conjunction with OpAMP, like, what's the… what's the complete story on Kubernetes that we want to be?
Explaining to people about how to… At scale, be able to kind of turn this on and then manage everything.
**Michele Mancioppi** 56:49 I actually spoke with, Jacob Aronov, he's the… one of the people involved in, In revisiting the concept of the instrumentation plus adding the jetter to the operator.
And the way I understand it, is that… The declarative configurations are coming as a config map.
And then they would say, go and do a PAMP, so it's gonna be… it's gonna feel very similar to the console for system packages.
**Ted Young** 57:16 Yeah.
**Michele Mancioppi** 57:17 Unless the plan changed, but for that when it was Jacob.
**Ted Young** 57:22 Cool.
**Tigran Najaryan** 57:23 Yeah, Ted, if you're not aware, there is a basic implementation of an all-pump-controlled operator-supervisor. There is some basics in place. I don't know if it's… How we want it to be in the end, but the basic functionality exists today.
**Ted Young** 57:41 Yeah, I've been aware of these things, but it just seems like, yeah, we've had several SIGs who have all been kind of, like, chipping away at this problem, and it's, like, it feels like a good time to kind of… Have those efforts just get… get more coordinated, and just…
**Tigran Najaryan** 57:58 Yeah, just…
**Ted Young** 57:59 figure out what our roadmap is, and like McKelly was saying, also making sure we've actually gotten the requirements from the different kind of end-user organizations, right? Like, so we aren't… Picking a solution that's… if there's no universal solution that's gonna work for everyone, like, what are the… the options that we give people. It should be based on the way these large organizations Need to… to be able to manage… manage the bits.
Cool.
Well, we're basically at time.
That was a good discussion.
I'll try to help coordinate between these, these three different SIGs, So that we can keep the discussion going.
**Tigran Najaryan** 58:47 All right, any last-minute comments?
Okay, thank you, everyone.
Bye.
