SIG: JavaScript SIG
Date: 2026-05-20
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/akMlz3zMJvbYNL1IyKoH8DDlaLawNfvXkpvMyHd3v-BJwBKv-dI2cdtRqUAUvzCf.cFuCVSAorY22eVeF
============================================================

## Zoom Recording Transcript

**Raphaël Thériault** 00:31 Later…
**Daniel Dyla (Dynatrace)** 01:49 Yalen!
**Marc Pichler (Dynatrace)** 01:52 Hello?
Alright, let's get started. I'll share my screen.
Oh.
Here we go.
Alright.
Welcome, everybody. The first topic… It is… from Malibia.
It's about, reference application.
A… actually stumbled upon this earlier today, and just a second person, I think, adding the reference application is a good idea, and then also, possibly kicking out some of the older, examples is a good idea, because there's some that are still using 0.25 of the Trace SDK, which is, historical, I guess.
in order.
**Trent Mick** 03:13 OpenTelemetry I.O, there are cases, or you mean in examples? There was another PR in our examples that was updating.
**Marc Pichler (Dynatrace)** 03:20 Yeah, there's, in our examples, so it's… Not sure which one to pick, but probably this one.
**Trent Mick** 03:33 That one is 1.x, the one that…
**Marc Pichler (Dynatrace)** 03:35 How old would exceed that.
**Trent Mick** 03:37 the Open Census shim, I think. I just wanted to delete that one, but…
**Marc Pichler (Dynatrace)** 03:43 Open tracing, maybe?
**Daniel Dyla (Dynatrace)** 03:45 Is that related to… I saw, like, a Dependabot PR…
**Trent Mick** 03:50 Yes, it's.
**Daniel Dyla (Dynatrace)** 03:51 Okay.
**Trent Mick** 03:52 It was updating this one and the gRPC examples.
keeping the example of Virginia… like, yeah, I don't know how people feel about the examples, like, it's a perennial problem, and… no one seems to have the bandwidth to go back and update them. Because you run into a thing like, oh, what should the example be? What should… should we be using SDK Node, and what, Visualizer for traces, or whatever should we be launching and showing? And anyway, that's… a few questions come up, so no one updates the examples.
**Marc Pichler (Dynatrace)** 04:25 Yeah, I think the older ones, like this one for the open tracing shim.
I think that one we can safely delete, nowadays.
**Trent Mick** 04:35 There was a blog post related… Marilla, I don't know if you saw my comment, it was on a… Which one was it?
Mike Goldsmith had a PR for declarative config, which is fair enough to add.
This is just a small PR for part of declarative Config, was to add support for… creating the SDK components for metric producers.
And these are for, like, third-party metric systems, so that you can ingest metrics from those systems into it. The only defined, well-known metric producer is the OpenCensus shim.
And when I was reviewing that thing, I was like, okay, yeah, fine, this is doing things in the declarative config spec. There's a blog post on OpenTelemetry about OpenCensus support being supported for a year after the SHIM packages were created.
That's been over a year. Can we, like… I'm curious, Maria, if you know, like, could we go back to declarative Config and say, hey, like… Do we even need an Open Census support, or can we make that one optional?
**Marylia Gutierrez** 05:41 Yeah, I was gonna… yeah, I was gonna… actually was gonna talk to… to Jack today and bring it up to him, but yeah, I put it on the, like, the comment there, like, I don't know… Right now, I need the extra stuff on top of what the things you share, but it would make sense for us not to add, especially… this is, like, a new function, and we don't want to, like, create something new that is already… like, not supported, but, yeah, I'm gonna…
**Trent Mick** 06:09 It could go either way. Mike's PR was good, it's just doing a conditional require, but… Yeah. Yeah.
Well, I guess, is that… is that thing I put on the agenda? It was.
The next one.
**Marc Pichler (Dynatrace)** 06:21 But that was the next topic, yeah.
**Trent Mick** 06:24 So I'm hijacking the thread then.
**Marc Pichler (Dynatrace)** 06:27 So on the Open Census one, it seems that we have Around 203 weekly downloads for the package, which is not a lot compared to all the other packages that we have.
**Trent Mick** 06:40 Are those 100% CI?
**Daniel Dyla (Dynatrace)** 06:42 I was gonna say the same thing.
**Marc Pichler (Dynatrace)** 06:44 Might… might be. I'm not sure if we actually installed it anywhere. I don't think we installed it in Contrip, And if we use it in the… In the core repo, it's linked locally, so… Must be somewhat abusing it.
maybe… Just installing it out of curiosity or something, but 200 is not much.
Yep.
I wonder if others are seeing similar, Similar usage of the OpenCensus stream.
**Daniel Dyla (Dynatrace)** 07:24 I think even in, like, external use… like, it could be all CI, even if it's not our CI. Like, there are things that mirror NPM, and there's probably old applications that run CI that nobody actually uses and stuff like that, too. 200 weekly downloads for a project our size is… I mean, it rounds to zero, basically.
**Trent Mick** 07:54 So I guess back to Marley's first question, then you assigned it to that guy that asked to take it, or the person who asked to take it.
**Marc Pichler (Dynatrace)** 08:04 Yes, there's also this specification for… the reference… App, so it should be a bit easier to… Review that one, because we actually have the spec to check against.
So once that one comes up, I'll just review, and get that in, and then we can also look into possibly removing some of the older ones.
Or do that in parallel, could also work.
I've looked into… Updating one of the examples a while ago with a bunch of, documentation on, like, which order you're supposed to do stuff in, and, additional info on what each thing does, essentially, like, a primer for somebody who sees an older SDK set up for the first time, but that PR, kind of tight, so, it's probably good to just go with the specified one there.
Right.
Anything else?
**Trent Mick** 09:21 Did you bring up? Mine again, there were a couple.
**Marc Pichler (Dynatrace)** 09:23 Yep.
**Trent Mick** 09:24 Different things.
Okay, so there are… there are HR separator tags in each one, so that first section, who's asking for others' memory and experience. This is a… ER, as I said, adding support for this OpenCensus shim.
And the way Mike has written it, which I think is fine, is it's a conditional Import, so basically that… functionality isn't supported in declarative config unless someone externally Or separately installs the shim, and so we can… Determined from further discussion if we're even gonna add support for this, but… What is the… People's understanding on… Whether we'll have to come back to these, conditional requires.
I'm… drawing a blank on… if we're trying to support ESM for some of these packages, we don't have an ESM build of SDK node right now, but if we did, does having… using require in there cause a problem?
Or, or…
**Marc Pichler (Dynatrace)** 10:30 Definitely.
we shouldn't use require in there. The reason why it works now is because we don't have an ESM build for it, and everything's require anyway, so… Doesn't really cause that much of an issue for the… GRPC exporter, For the others, we have this await input, as you mentioned already, and that one… works also for ESM build, which is why we need it in the resources.
stuff. And that compiles down to require for, for the common JS build.
**Trent Mick** 11:09 That compiles down to require.
**Marc Pichler (Dynatrace)** 11:12 Yes.
**Trent Mick** 11:14 Oh.
**Marc Pichler (Dynatrace)** 11:15 So, it still yields, this will yields to… But is it rafters?
**Trent Mick** 11:24 Is it wrapped in a promise so that it's…
**Marc Pichler (Dynatrace)** 11:26 Yeah.
**Trent Mick** 11:27 Artificially async? Okay.
**Marc Pichler (Dynatrace)** 11:29 I think the last time I checked, this is what was happening.
**Trent Mick** 11:34 Okay, so… Two comments on that.
if… this is the SDK node, so node-specific, so not… the browser compat is out of the story here, but… modern versions of Node, if we start at Node 22, now support require ESM, I think, right? So is… is it necessarily… problematic for an ESM bill to have required… used… used?
**Marc Pichler (Dynatrace)** 12:05 That's a good question.
**Trent Mick** 12:07 Okay, we don't have to answer that right now. Then the second question is on… Using a wait import versus require, the config Declarative config process is currently synchronous.
So… A weighted import would be… Now we have a design question on changing configuration.
**Marc Pichler (Dynatrace)** 12:30 Yeah.
So, I think we should avoid doing these Lazy loading things.
in paths that… We know get executed by default somehow, or, like, people might use in bundles as well.
Right. Because people are running into, like, warnings and build failures and stuff like that, depending on which bundler they use.
Which can be annoying. One thing that I've been thinking about, about, like, how to solve this specific issue was… what we could have if we were to implement the plugin component provider stuff.
Is we could have some way of dynamically loading extra things.
And then… essentially hand that off to some other place, or some other entry point, or something like that, that people can then use to dynamically load these things if they are comfortable with that happening. So if you're using bundlers, you wouldn't touch that code path at all.
And this way, we could maybe work around that bundle situation.
The way that the dynamic loading could work is, intentionally not specified by a draft PR that I, opened earlier today.
**Trent Mick** 14:10 Yeah, I saw it, I haven't had a chance to read it. I'm curious.
**Marc Pichler (Dynatrace)** 14:14 It's just… it's just really a draft of how, like, the internals could look like, using the plugin component provider spec.
And one of the ways we could do it is to have, like, the create function being called by the user.
And then… have some way to dynamically load these components. And there could be a function that just does the well-known components. Let's say the OpenSensus stream is one of these, where we just have a bunch of hard-coded strings that we try to dynamically load.
component providers from.
And then that package could have a component provider in there that just configures that Sync?
And if you're trying to use it, then… you would… Be required to use that path.
If we want to have the convenient way of just installing packages and them being automatically loaded. Or it could also be some other… Mechanism that we come up with.
That just loads these sorts of things. One of the things you would run into here with this dynamic loading is you would probably have, like, an await And… You could have different ones for common.js and for ESM.
And for ESM, you can do top-level L8 anyway, so that should be fine.
**Trent Mick** 15:46 Okay.
I will definitely read that with interest, and obviously we're not going to solve it right now.
**Marc Pichler (Dynatrace)** 15:54 One warning about this, this is very much vibe-coded at this point in time. So it still has some odd choices in there. I need to iron this out.
Before marking that as ready for review, it's still in draft for that reason.
But any sort of, feedback on the overall, approach?
That's very, very common.
**Trent Mick** 16:23 Or we could wait for synchronous import. It's a TC39 proposal.
Which means in 5 years, we can cycle back and come back and make this synchronous config loading.
**Marc Pichler (Dynatrace)** 16:35 Nice.
**Trent Mick** 16:36 Yeah.
Okay, cool, I think my question's been answered.
I don't know.
Where was it?
**Marc Pichler (Dynatrace)** 16:51 So, I guess the follow-up for this PR would be to figure out if we even need, OpenCensus shim support.
At this point in time.
And if we do, then we'll get back to, like, the details on how to do it, right?
**Trent Mick** 17:13 Yeah, I mean, I… I think this is not a super important part of the… declarative config.
thing, so we can sit on this PR for a little while if we need to. And I'm guess… guessing talking about… Yeah, yeah, yeah. I think there's not a huge rush on this one, so we can see.
Yeah, Marilla, if you said you were gonna talk to Jack, that would be great, otherwise I can open…
**Marylia Gutierrez** 17:37 Yeah, I already messaged him when I saw this, but I haven't heard back from him yet, so whenever I get a response, I can update here, or…
**Trent Mick** 17:47 Okay.
Karen?
**Aaron Abbott** 17:50 Hey, It's kind of serendipitous that I just joined this meeting and you're talking about this thing I added.
So, but yeah, I'm curious, so I added this, and I agree, I don't think we need it in the declarative config, but we also have this in, like, a bunch of other languages, so if you do get clarity on, you know, when the shims are no longer needed, if we would deprecate them, I'd be interested to know.
**Marylia Gutierrez** 18:14 Yeah, whenever I get, like, the conclusion of this, my plan is to actually do something on the… so the declaration can feel, like, repo, and that can kind of, like.
Everybody can kind of follow whatever is the decision.
**Trent Mick** 18:26 Yeah, yeah, I assume there would be an issue there, to discuss. If this becomes then optional, or what? It's like… then JS does not support the OpenCensus, well-known producer, yeah.
Okay.
**Aaron Abbott** 18:42 Cool, thank you.
**Trent Mick** 18:43 Okay, cool.
**Marc Pichler (Dynatrace)** 18:52 Okay, so… the example topic, we were done with red.
Okay.
Good. Then I guess we can… move on to the next one if there's nothing, to talk about anymore for the OpenCensus stuff.
**Marylia Gutierrez** 19:16 So yeah, just looking at, like, security stuff, because I… Well, one of the things that I saw, like, the CodeQL, we already run this on our repo, and just a question, like, if that should be a required one, because currently, I don't think it is. I know that a few repos mark as required, it's mostly, like, the Java ones.
Considering that, I don't know, it's always NPM that brings something.
I think if there is, it makes sense for us to be extra cautious. If that is something that we want to do, I can easily open the PRF to do that.
for the Zismor… I can create, like, an action to run this.
But because I'm not a maintainer, I don't see some stuff, so I would need… or I can show the scripture, like, a maintainer and somebody run, just to see if it is running correctly. Like, I can open the PR, but one of you has to verify, because I don't actually see security tabs, and…
**Trent Mick** 20:17 Yeah, I don't think we can… we can either, because it's… you're always gonna run… On… I'll get the names mixed up. It's either on the trigger pull request or pull request target.
And it's gonna run not… against… the DPR that's provided, because otherwise that's basically a security.
If I remember. I don't know, anyway, which is ironic, because that's exactly what Zismor is gonna be about. It's like, don't do this.
Don't… don't allow a PR to change what the GitHub runner actually runs, and then run it, but… So I think that is kind of a hiccup that we just need to get a merge to main to see what the thing's gonna fail on, which is fine if it's not a required check.
So I think we could do that. And then there'll be a number… what Zismor is going to do is suggest a whole bunch of updates to basically all of our workflows to lock down permissions, and to… Breeze… the actions, dependencies that we have to particular GitHaws and stuff like that, so… yeah. I think that… It's probably good, Tad.
**Marc Pichler (Dynatrace)** 21:32 does it work through the security tab? Because… So…
**Trent Mick** 21:38 Well, I don't know, what I've done is run this more locally against our.
**Marc Pichler (Dynatrace)** 21:43 Yeah.
**Trent Mick** 21:43 you can just run it against a directory of workflows, and it just spits out warnings like any linter. So, I haven't looked at this as more action to see what it does.
**Marylia Gutierrez** 21:53 Yeah, so from a… because I have a… one of my teammates is doing that for some of, like, hotel repos, and basically what it does is just open something on the security tab.
**Marc Pichler (Dynatrace)** 22:05 the blue.
**Trent Mick** 22:05 Okay.
**Marc Pichler (Dynatrace)** 22:07 Similar to CodeQL, these things also show up in the security tab, usually.
**Trent Mick** 22:18 Is that the code scanning section?
**Marc Pichler (Dynatrace)** 22:20 I think so, yeah. It usually says where it's from.
**Trent Mick** 22:25 by… yeah, I see that.
**Marc Pichler (Dynatrace)** 22:26 Yeah.
**Trent Mick** 22:26 to scorecard. I've never even looked at these, but… okay.
**Marc Pichler (Dynatrace)** 22:32 Cool.
**Trent Mick** 22:33 We have some work to do.
**Marc Pichler (Dynatrace)** 22:36 It's only visible.
**Trent Mick** 22:37 The maintainers, yeah. Yeah.
**Marc Pichler (Dynatrace)** 22:39 Many of these, that are… that have been there for a while, they are in examples, or… Stuff like that, so…
**Trent Mick** 22:48 Tests, integration tests is one.
**Marc Pichler (Dynatrace)** 22:50 Yeah, it… I usually go through these Every once in a while, and, close the ones out that don't really cause any trouble. But then there's, Sometimes in tests, you need to do some weird stuff to make stuff work, and yeah.
**Marylia Gutierrez** 23:12 Yeah, I can open… I can open the PR for, like, having the action of the CSMR, but then, yeah. And do you want me to make the CodeQL required as well?
**Trent Mick** 23:23 Oh, God, no.
**Marylia Gutierrez** 23:24 No?
**Trent Mick** 23:27 Well, it's gonna be full… full stop work for a week if that… if we do that, I think, right?
**Marc Pichler (Dynatrace)** 23:33 I think it only complains on… I think what you're… what you are saying, Margalia, is that The check should be required, right?
**Marylia Gutierrez** 23:44 Yeah, yeah.
**Marc Pichler (Dynatrace)** 23:45 Yeah, I think that would be reasonable, because the check only fails on newly introduced stuff.
**Marylia Gutierrez** 23:53 Yeah, because, yeah, the check is, like, on the PR itself.
Yeah.
**Marc Pichler (Dynatrace)** 23:57 Yeah, so I think that that definitely makes sense. We can make that required. I've usually been looking at the CodeQL check, anyway as part of, code review, but, we can just make it required, like, unit tests.
are at the moment, so… I think that's… that's very reasonable to do. At least this way, we can… Avoid new stuff being introduced.
And I think there's also usually a pop-up where you can dismiss stuff if it's in tests, or something like that, if we have to. Not sure if approvers also see that, or just maintainers do.
**Trent Mick** 24:44 So, for example, there's a… there's a CodeQL security thing from 2022 in the SDK Metrics package. Does that mean the next time someone does a diff to that particular file in SDK Metrics, they're going to be stuck by?
That, and if it's a security issue only visible to maintainers, how does a user… a non-maintainer submitting a PR to that thing actually see it? That's two separate questions, they're unrelated. I'm curious what the visibility's like for… Making CodeQL.
And required.
required checking. Anyway, we can try it, and if it's a problem, then…
**Marc Pichler (Dynatrace)** 25:21 Yeah, so… Usually it's not the file being modified, but if you… modified.
**Trent Mick** 25:33 A particular line, it's not on…
**Marc Pichler (Dynatrace)** 25:35 Yeah, depends.
down the line, if you modify that, then it, like, detects it as a new issue. Yeah, I got it.
**Trent Mick** 25:42 Makes sense. Yeah.
**Marc Pichler (Dynatrace)** 25:43 But… I actually don't really see that many new ones being introduced. It happens… every once in a while, particularly often with workflows, because I think CodeCore also does workflow scanning.
where CodeQL has been very useful in catching these things early, where it just goes through and checks if something is, User-controlled input.
And then just kind of years at you until you fix the problem.
That, like, gives you the whole chain of stuff.
Aw.
I think we can… we can try enabling CodeCure, and if it… Or making it required, and if it isn't.
Working, then we can still backtrack.
Big sort of stuff, and start again.
Because we need to… do that. Like, we need to go through the stuff that we have in our tests and fix those things at some point anyway.
Because it's very difficult to see what's actually new when the security Counter thingy on the tab goes up all the time.
**Marylia Gutierrez** 27:12 So yeah, because this setting, since it's on the admin repo, that I'm already part of it, so I can actually make the change to make it required.
**Marc Pichler (Dynatrace)** 27:24 Yeah, I think that would be… would be great. And then.
**Marylia Gutierrez** 27:28 So yeah, there's more… I can open the PR with the action of kind of, like, using the same thing that another, like, my teammate showed me, but then once it's merged, one of you will have to just run and tell me if it actually works.
**Trent Mick** 27:48 That's cool, yeah, I mean, I can do that, or any of us.
Maybe not make this as more required one out of the gates.
**Marylia Gutierrez** 27:56 Oh, no, this is not…
**Trent Mick** 27:57 We'll go.
**Marylia Gutierrez** 27:58 So, this is.
**Trent Mick** 27:58 I understand.
**Marylia Gutierrez** 27:59 run on the PR. Oh, yeah, it's gonna run on the PR, but it's… it's not part of, like, the checks of the PR. It's just, like, an action that runs.
on the event of a PR getting merged.
and then create something on the security. That is what I'm understanding, what it does.
But I could be wrong, but…
**Marc Pichler (Dynatrace)** 28:21 I wonder if it does something similar to how CodeQL works.
Fair enough.
Think of a good way to… Has to fit, actually.
detects bad stuff without running into an issue where somebody might accidentally merge bad stuff.
**Marylia Gutierrez** 28:52 So yeah, the thing that you shared turned… yeah, that was pretty much what I was gonna create.
**Trent Mick** 28:58 Yeah.
**Marc Pichler (Dynatrace)** 29:02 I'm just trying to find where my chat window is, but there it is.
**Trent Mick** 29:08 I don't know what GitHub's advanced security is, I haven't read about that.
I would say… Good feature.
**Marc Pichler (Dynatrace)** 29:25 Yeah, I guess we can try it out and just see what happens. If we need to run it, and Modelia, you want to, figure out if something is working, I can… we can just, communicate on… Slack, or an issue, and then go back and forth on that.
**Marylia Gutierrez** 29:44 Cool.
**Marc Pichler (Dynatrace)** 29:49 it would be good to have this as well. I also ran this locally before, and found some Things that could be improved.
And then did a bunch of improvements, I think it was, like, 6 months ago or something, so… Getting that check on the new workflow, is very helpful.
Alright…
**Marylia Gutierrez** 30:27 I do just want to kind of bring awareness, because there was the, stable by default, but it was a little confusing to what I mean, so… Now we have this new one.
And of course, we were bike-shedding a lot on the title of… general availability, I suggest it to be just good to go, but… just, yeah, bringing this, because I think one of the things that would be more affected is mostly, like, instrumentation, how we make sure that it's market stable, so it's definitely going to affect a lot of the SDKs, so just, right now, bring it up, take a look, if there are any concerns and stuff.
Feel free to add the comments there. Or, yeah, talk to me as well.
**Marc Pichler (Dynatrace)** 31:17 Yes, thanks for bringing it up. I… And we'll also have a look at that one.
I think in spirit, it's very similar to what OTEP was about, right?
**Marylia Gutierrez** 31:28 Yeah, yeah.
**Marc Pichler (Dynatrace)** 31:29 Yep.
Alright, sounds good.
Any questions or comments about this?
**Trent Mick** 31:44 For me, I think this'll be… Like, after the dust settles of us doing a 3.0, We'll encourage the focus items to be, one, stabilizing exporters, and two, stabilizing the instrumentation interface.
Which… and the latter, I think, is more… well, I mean… exporters, I defer to Mark on most of that. On the instrumentations, there's a… I think, a discussion to be had on whether we… Do significant rework on the instrumentation base class, given that I think browser is potentially moving away from wanting to have a dependency on that, because it's kind of baking in assumptions about require in the middle kind of stuff, so… like, there's a lot of stuff up in the air. I don't know if… if we go, like, heavily redesigning that, or if we… artificially, or just stamp what we have as 1.0 and start talking about well, I guess it'd be 3.0 at that point, and then talk about any rework being a 4.0 for instrumentation stuff. But anyway, that's down the road discussion.
Are there other sections that are big?
Missing pieces?
**Marc Pichler (Dynatrace)** 32:58 I think the instrumentation that you mentioned is the one that sticks out the most. Also, the thing with the most impact for us, because.
**Marylia Gutierrez** 33:07 Yeah.
**Marc Pichler (Dynatrace)** 33:08 Have so many instrumentation packages.
Yeah.
**Trent Mick** 33:19 Yeah, exporters… Instrumentation… Maybe composite samplers.
**Marc Pichler (Dynatrace)** 33:31 Instrumentation is one of… I think the composite sampler stuff, Should be?
Fairly simple to stabilize.
**Trent Mick** 33:41 No, it's just one package, yeah. I'm just looking at the… This directory… Oh, sorry, the packages center entry, is that… yeah.
So, like, Exporters gets rid of a whole bunch of them, and then instrumentation, and then… There's not a whole lot left.
**Marc Pichler (Dynatrace)** 34:05 We need to… Finish up logs.
Right.
**Trent Mick** 34:12 That's true.
**Marc Pichler (Dynatrace)** 34:12 lift, yeah.
And then that unblocks, essentially, instrumentation, and also the exporters.
Troopy, big chunk of work.
The composite samplers, we could… probably tackle before that. I'm not sure if the spec on that is stable already.
Wow, that's true.
**Trent Mick** 34:35 I'm not sure it is, so fair enough.
**Marylia Gutierrez** 34:39 Which one? Stable and which one?
**Trent Mick** 34:41 Composite sensors.
**Marylia Gutierrez** 34:42 Okay.
**Marc Pichler (Dynatrace)** 34:46 Yeah, and…
**Marylia Gutierrez** 34:49 Yeah, it's not, yeah.
**Trent Mick** 34:51 So, yeah, so no risk there then yet.
**Marc Pichler (Dynatrace)** 34:53 Left out for a bit now, yeah.
And then also, once we have the instrumentation package stable, or… Defined subset, In the instrument… some subset of the instrumentation package that is stable, we can look into also stabilizing the actual instrumentation packages.
Where the main work will probably be just making sure that the API surface is minimal.
And doing any rework that we decide, needs to happen in the instrumentation stabilization.
**Trent Mick** 35:39 And understanding what the intent is for… What stable here means for this amount of conventions coming out of those… Instrumentitations.
**Marc Pichler (Dynatrace)** 35:50 I think some anti-conventions, if I record correctly, I haven't read the whole, thing here yet.
But that was… if I recall correctly, explicitly.
Not a requirement for stabilization of the instrumentation packages, so you could have a stable instrumentation package that would emit unstable semantic conventions, but I'm not sure if I'm just… Talking nonsense here.
It might be better for me to read this before making assumptions.
Yeah.
But, yeah, once we have a stable instrumentation package, then… All the other things should… Kind of fall into, fall into place for us to… Go through all the packages and, Work through them one by one.
Alright.
And I guess we can move on to the next topic, which is… PR on max export batch size. I've started reviewing that earlier, but I didn't finish yet.
I just publish my partial… review for now.
And then I'll get back to that.
**Pranav Sharma** 37:46 Alright, thank you.
**Marc Pichler (Dynatrace)** 37:50 Thanks. We're working on that.
I think the biggest thing about this one is just we need to make sure that the new options we introduce are marked as experimental, so if anything changes in the spec, people are not surprised.
Glova already looks good.
Oh, something right.
**Pranav Sharma** 38:14 Sounds good.
Just one, question on that. This, the, this, this feature… is there, like, in OpenTelemetry JS, a time where you bake the features before marking it stable for OpenTelemetry JS?
Or, like, because I think the spec already agreed to this, right?
**Marc Pichler (Dynatrace)** 38:37 Yeah, so the way we usually do it is, the spec agrees to merge it, and then it's in development. So we mark it as ad experimental, because That is… the TS doc.
trying to think… And once the… there's an issue on the spec that talks about stabilization. This is something that I think everybody can drive.
Then… They were just… check if there's enough implementations of that, and if it meets the criteria, and then there will be a PR on the spec that just moves that to stable, and once that is stable, we also go in and remove the experimental annotation there.
**Pranav Sharma** 39:25 Alright, go ahead.
**Marc Pichler (Dynatrace)** 39:26 So there's a lot of, like, back and forth going on, but it's just to make sure that, if the spec decides to… or if the… If the specification changes, we still have some option of also changing it without having to Pump the major version, on… on the, in this case, SDK metrics package.
Good.
So that's kind of our safeguard there.
**Pranav Sharma** 39:59 Thank you.
**Marc Pichler (Dynatrace)** 40:02 Sure.
Right.
I guess, no.
There's time to move on to… triage session, if anybody has anything you would like to talk about.
Please feel free to interrupt me while we're looking at… I'll treat your bucks.
**Trent Mick** 40:32 Did you do anything special to get NianCat?
your… your persona in the Google Doc right now is NeonCat.
**Marc Pichler (Dynatrace)** 40:41 Let her know what I have anything.
**Trent Mick** 40:43 Okay.
**Marc Pichler (Dynatrace)** 40:45 I always thought that this was, shane told me.
**Trent Mick** 40:51 either. I can't see your…
**Marc Pichler (Dynatrace)** 40:54 But… Maybe… It just gets randomly assigned this.
**Trent Mick** 41:02 Yeah, anyways.
**Marc Pichler (Dynatrace)** 41:03 One of the…
**Trent Mick** 41:05 I wasn't serious, I was just wasting time.
**Marylia Gutierrez** 41:12 Well, I guess just one thing that I can bring up, because, well, it happened last week, but I was not here last week. Well, I'm assuming you all saw graduation happened. The official press release is coming out tomorrow, but yeah, just wanna say for everybody that contributed and was part of it.
Awesome job, and thank you for all the things everybody did here.
**Marc Pichler (Dynatrace)** 41:38 Awesome, thank you, R.
it's good to see it move to the radiation thing. I think we, We've now moved to graduation, but GRPC has not yet, which is… That's something I found out only recently.
**Trent Mick** 41:58 No, as far as I know, the only… the most meaningful outcome of this is that the OpenTelemetry project can now have a mascot.
**Marylia Gutierrez** 42:08 Yeah, that is the most.
**Marc Pichler (Dynatrace)** 42:09 important thing.
**Marylia Gutierrez** 42:09 We don't care about anything else.
**Trent Mick** 42:12 There's a raging bikeside discussion on what the mascot should be, what its background should be, and what its name should be, so…
**Marylia Gutierrez** 42:18 Yeah.
I still vote for the… for the other. They're way too cute.
**Trent Mick** 42:23 Well, the otter's gonna win, isn't it?
**Marylia Gutierrez** 42:25 Yeah.
In case you won't miss it, we now can have a mascot, but we are, like, it has to start with the same letter as the project, so something with an O.
And try to avoid things that already exist in others, like owls already exist, and things like that, so avoiding… Octopuses, stuff like that.
**Marc Pichler (Dynatrace)** 42:51 Nice. Fair.
think about which… which mascot I would prefer.
**Marylia Gutierrez** 42:58 I'm just thinking about the plushie. Which one do you want as a plushie? That is the…
**Marc Pichler (Dynatrace)** 43:07 Right.
Okay, it's… You can… no.
Start with dog triage.
It seems that… It takes quite a time, too.
Load.
**Trent Mick** 43:45 The contributor info, is that where you're at?
Just reload. It worked for me.
**Marc Pichler (Dynatrace)** 43:57 There's, like, no bucks in your 100K button, dude.
**Trent Mick** 44:04 I just deleted the repo.
**Marylia Gutierrez** 44:07 No code, no bugs.
**Marc Pichler (Dynatrace)** 44:09 Yeah, true.
**Trent Mick** 44:18 I… Oh.
Yeah, there's a PR for this one, which I reviewed.
**Marc Pichler (Dynatrace)** 44:28 Oh, P2, probably then.
**Trent Mick** 44:33 Yep.
**Marc Pichler (Dynatrace)** 44:34 Supposed.
**Trent Mick** 44:35 Sure.
**Marc Pichler (Dynatrace)** 44:39 Is that related to.
**Trent Mick** 44:43 You're gonna say there's a PR that was similar?
**Marc Pichler (Dynatrace)** 44:46 I think I saw this PR, I was just skimming over it, and I'm wondering if that is… similar to the issue we had with Express and some other instrumentation, and I don't record which one it was, where… The spans wouldn't be… Nested, but side by side.
**Trent Mick** 45:12 So, yes, kind of related to that is my understanding.
**Marc Pichler (Dynatrace)** 45:14 Thanks.
**Trent Mick** 45:15 So, okay, some confusion, here. So… I think there was a PR, I wasn't following closely, but there's a PR related to Instrumentation Express that deals with basically this same thing about baggage stuff being dropped.
But that was for Express 4, where the routing handling is part of the Express Library. This is for Express 5, where… the routing handling is deferred to a separate router package, so instrumentation router is part of the story, so it's kind of a second fix, one for Express 4 and this one for Express 5. And the reason that… baggage added to the context was dropped is because of the change made that you were talking about, where we didn't want a span for each middleware to be nested a child of the previous middleware, so it's basically a design decision that was made there. And the way that that was done was to… run each middleware explicitly in the parent span context for the route.
what?
happened when you do that, then, is that if anything is added to that context by one middleware, it doesn't get carried over to the next metalware, next middleware, and ending the whole thing, because they are independently being run in the parent context.
So yeah, this… this is just a fix for that. So yes, it is… these… both of these are a side effect of that earlier design change.
I… I haven't merged this yet, because he hasn't signed to CLA.
**Marc Pichler (Dynatrace)** 46:57 I am not sure if… We decided on keeping it like that, or if we decided to Actually make everything nested now.
**Trent Mick** 47:11 Oh, really? I don't recall. I wasn't.
**Marc Pichler (Dynatrace)** 47:14 I always believe it.
**Trent Mick** 47:14 away from that discussion, but…
**Marc Pichler (Dynatrace)** 47:17 Yeah, I also don't record the exact outcome anymore. We might have either done it the way that it's done here, or… The other way around.
We might want to check that, because maybe that's a… That's…
**Trent Mick** 47:35 Yeah, I understand.
**Marc Pichler (Dynatrace)** 47:36 Where we could align everything.
**Trent Mick** 47:46 It was a while ago, though, wasn't it?
**Marc Pichler (Dynatrace)** 47:49 Yes, I think it was… It's, like, at least a year ago.
Yeah, so I think the express instrumentation will be the… The one where we definitely can see what the outcome was from that.
So if we try to run that and see how the spans look like on that, then… That can give us a hint.
But, yeah, seems like the CLA… It needs to be signed here, so I'm hoping that we're over now.
Alright, So this is, documentation.
That's… P4 in that case.
Actually mark this one as up for grabs, in case anybody comes along who wants to work on that.
Looks like, Nobody… back to this one yet, but are just, write the comment to, I assume this is fixed, and if anybody wants to, Anybody wants to open a new issue, then… We can go ahead and triage that.
Alright.
That's it for… contract repo?
And we can go into PR triage mode.
Onto the core repo.
-Oh, Still haven't gotten around to this one yet.
I think I had recommended that we move that to the SDK trace.
Base package… Just ask the person if… They're still working on this.
And then if we see that PR again, we can, Close it if there's no activity on it.
We still need to do that, though, because this is a spec feature.
Not sure if that one actually has an issue somewhere… I wish I could put a note here somehow, too.
Create an issue if… Let me close this, but I'll just have a look at it next.
Time mechanic.
This one I haven't gotten around to yet, this was a performance improvement.
On personal activity, we can still leave it open for a bit.
This was the migration to… to astounded a few other things, I think we discussed at some point that Would be great to have, The testing changes, are also migrated… or the testing changes merged first.
And then… Extra… Migration happen in, What was it? 3.0?
So… Actually, not sure.
Rave Tell us… I seem to remember that this was moving on to some other test runner, but it seems that this current version of the PR isn't.
**Trent Mick** 55:02 There was… moving from Karma to V-Test, and then… David had a comment on the… lower down on PR asking him to extract that, I'm not sure if he did.
**Marc Pichler (Dynatrace)** 55:16 I don't think I've seen the PR yet.
Pardon me.
**Trent Mick** 55:22 Oh, I think just to take it out of this PR, not necessarily having created a PR for the migration yet.
**Marc Pichler (Dynatrace)** 55:35 Right. As we're looking into that later. Once… we start working on 3rd, though, I think this is probably one of the first changes we would want to make, So, at least the… to a common JS ESM export, because that is something that people have asked for quite a bit.
Alright, and this one here… I had looked into that earlier this week, but then had some… Issues with the checks not completing, that seems that has resolved.
So I'm just about scope.
**Trent Mick** 56:28 Just needs a changelog entry.
Do we just need Aleandro to add a changelog entry now?
**Marc Pichler (Dynatrace)** 56:58 Seems like it, yeah.
Sometimes I go in and add changelog entries myself.
**Trent Mick** 57:05 True, yeah.
**Marc Pichler (Dynatrace)** 57:07 But… Sometimes I also, merge main and resolve some conflicts, and then I… Forget to get back to it, so that's what happened there.
Okay.
Assign this to myself.
So, I can get back to this one, and if there's low activity, then I'll just add the changelog entry there.
Alright.
This one here, I have sent myself, but also haven't had a look yet, Potentially, it just… It's the general auctions.
Thing, which should be fine, because… general options are just options, so you don't need to import gRPC for it, which would break the gRPC instrumentation, depending on… How you set it up.
Which order you set up the gRPC instrumentation and the X part are there.
Overall, I think… Looks fine.
Doug is also there.
I still have to… check that locally before approving it, so I'll do that.
Good on.
And it looks like we're out of time for today, anyway.
So, thank you, everybody, for joining.
Have a nice week, and see you next week.
**Daniel Dyla (Dynatrace)** 59:28 Thank you, Mark.
**Trent Mick** 59:30 Yeah, thanks, Mark.
**Hector Hernandez** 59:32 Thank you.
**Marc Pichler (Dynatrace)** 59:32 Thank you, Kelly.
**Trent Mick** 59:33 Bye.
