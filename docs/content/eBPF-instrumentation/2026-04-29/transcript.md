SIG: eBPF instrumentation
Date: 2026-04-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Stephen Lang 00:00:56 Hmm.
Tyler 00:01:33 Hey!
Nikola Grcevski @ Grafana / OpenTelemetry 00:01:33 wood.
Tyler 00:01:35 How y'all doing?
Nikola Grcevski @ Grafana / OpenTelemetry 00:01:37 Very good.
Tyler 00:01:40 Oof.
Nikola Grcevski @ Grafana / OpenTelemetry 00:01:43 early morning for you, Tyler.
Tyler 00:01:45 Yeah, feeling it this morning, I don't know why.
Well, I know why, it's because I haven't got the coffee yet, so… yeah.
What's the… you're 2 hours ahead, right? So you're 10, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:01:56 Yeah, no, it's 11, 3 hours in that, Eastern.
Tyler 00:01:59 Oh, we're Eastern, okay, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:00 Weird.
Tyler 00:02:02 Yeah, that's the… actually, I think 10's kind of, like, the sweet spot for… for getting a meeting, like… Yeah. Actually, it's not, because that's actually, like, when you're, like, peak output, like, doing stuff, so maybe not, yeah.
Maybe it's… maybe it's early to get it out of the way, but… yeah.
What's the… How's the spring looking over there, Nicola?
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:26 Not bad. I mean, it's a useful spring for me.
I don't… Wet and green. Not too warm, not too cold.
Tyler 00:02:37 Not a… not like Barcelona.
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:39 No.
No, it's more like the weather you get in Portland, I guess.
Tyler 00:02:45 Oh, really? Oh, okay. I kind of wonder, I think we're probably… About the same… Same, same spot, actually, so, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:02:53 You know, similar now.
All in the weekend.
Tyler 00:03:01 Well, cool, yeah, we can… probably jump in here in just a second. If you haven't yet, please go ahead and add your name to the attendees list. If you have agenda items you wanted to talk about.
Go ahead and add them there as well, and yeah, we can… we can jump in here in just a second.
Cool… I think you can all… yeah, okay, cool.
Awesome. Alright, yeah, let's jump in here. So, first off, Nick and Rod, you wanted to ask about automatic copilot reviews, after CI passes?
nimrodavni 00:04:27 Yeah, I think, Rafael was the one first mentioning it, and, like, we kinda… decided to just ask for a co-pilot review, I guess, every time you want to, but I think it kind of became a… automatic thing, like, at least for me, and I see some other people. Maybe we can, like, automate it, and, like, after CI passes, automatically… yeah, like, ask Copilot for review. The only thing I'm worried, I think Mattia mentioned it, I don't know if it's, like, true, or what happens if it's… count as part of our, GitHub action budget? Is it, like, free? Like, do we have limits on this?
And also, like, if… if multiple, like, you push multiple commits, and every time it does a review, like, if we can, like, minimize the, like, the… have it review only the changes that they made in the commits that it didn't already review, I don't know how Copilot works in this case, so… Just wanted to bring it up if people have any opinions.
Mattia Meleleo 00:05:32 I put a link in the chat, this is what I read the other day. I'm not sure it applies to us, but…
Tyler 00:05:46 Let's see if I can open this horse.
nimrodavni 00:05:50 And sent on June 1st.
Tyler 00:05:54 Oh, interesting.
Yeah, so… so first off, I don't think that it's a… so the co-pilot reviews that you do see currently aren't being run by the OpenTelemetry org, they're being run by individuals who have asked for their reviews, or asked for reviews. So… I know that, like, on mine, yeah, it actually… Copilot kept following me around, and I couldn't figure out why, and it's because I had actually, like, enabled it on, like, my profile, so it just reviews everything that I submit, at least it's supposed to.
I don't know if on the org it can do that, if you can say, like, in the OpenTelemetry org itself, like, we want it to do all these reviews. I think there's definitely some other folks here that have also, like, you can… they can request it, but as far as I know, like, that counts, not against the OpenTelemetry org, like, action budget, or, well, or what will be the action budget, but, like, eventually to the, you know, the co-pilot budget is it's a very different budget. So, I think this is more of a question around, like, maybe, like, the maintainer's channel or the community channel about this. I mean, I'm in favor of it. I don't know how the specifics work.
I know that we actually have, like, a budget for… our actions, and like, we, you know, the CNCF itself pays for this stuff, so… I mean, I think if there's something there, I just don't know the answer. I think it'd have to be something you'd have to elevate to the, to the maintainer's channel, and probably the GC or the TC to ask that question.
nimrodavni 00:07:33 Okay, I can… I'll try to see if anyone asked anything about it, and if not, I'll… I guess I'll open something on Slack or something.
Tyler 00:07:41 Okay.
Yeah, I think that's… that'd be great. I mean, I'd love to see this, so yeah, I'm all about it.
Antonio Jimenez 00:07:49 Do we know, guys, if it is used in other cloud-native products, like OpenTelemetry Collector, or Contrip?
Tyler 00:07:57 It's the same there, so if users have enabled it to do the reviews, then the reviews are happening.
So, I don't think that there is… well, I know there's no, like, universal, like, hotel policy right now on it, But, yeah, I mean, I don't know if another repo has somehow been able to enable it. I think that's kind of what, I think Nimrod's gonna go chase down.
Yeah. But yeah, I'd love to see it. I think it's… they're… they're pretty helpful.
So, yeah, I think that'd be great.
Nikola Grcevski @ Grafana / OpenTelemetry 00:08:32 So if I currently request a profile preview myself, that means it comes up in my budget.
Tyler 00:08:38 Right, correct, yeah.
Which, I think we're still living in a golden age of that, where it's, like, pretty much free, so… Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:08:50 I'll help me.
Tyler 00:08:51 Yeah, I'm all about it, and so we should use it as much as possible while it's free. So, yeah.
Well, cool. If that's it, Nicola, Nimrod, thanks for… taking that action item, and we'll follow up on that one. Nicola, do you want to jump in on reporting back from the maintainer spec sig?
Nikola Grcevski @ Grafana / OpenTelemetry 00:09:08 Yeah, so, A couple weeks ago, when we had a SIG call, Korean mentioned that they wanted to know the update. So I went, to the SIG maintainer spec, call. Yesterday, it was… So, this time as well, and so… I pretty much just, talked about the roadmap, And what our goals for this year are, including and potentially get to a release candidate, and stabilization.
All the cool features they're doing. It was really well to see. People are excited about the project, and Actually, they said, they want to see better SDK integration, so, it shouldn't be as much as OB or SDK should be working together, if possible, and… People are interested if we have any ideas.
On what we need from the SDKs for this to happen. So, they're willing to put code in the existing SDKs to actually support OB Better, and be able to kind of turn on and off things.
the pending one. So that's… that was really great to hear.
And I think we've already started on this path. I believe there's a VR open, or a draft VR open beforehand.
So, using some of this, metadata that can be encoded.
They're asking if we can have any other ideas how we can kind of communicate with the user space better from the OB side, user space instrumentation.
Not if we have any ideas, but… Maybe she'll come up with a proposal and ask for it. So, yeah.
It's very much it.
Yeah, tighter integration with the rest of the SDK ecosystems, is what they want to say.
Which we have as a goal on the roadmap this year.
nimrodavni 00:11:07 I, I commented on Florian's PR, which looks really cool, but… I don't know if it's part of the spec yet, maybe we can suggest it, that… right now, I think it only reports if there's an SDK on the service and, some, like, resource attributes.
But maybe we can also, like, have the SDKs write down which, like, instrumentations, like, or auto instrumentations are applied on the service, and then we can do some kind of detection of, like.
I don't know, there's gRPC and SQL on this service, so we automatically don't instrument that, but we do instrument other stuff.
But we still need to figure out, like, how to share the actual trace context, which I think there's already… there's also something they're working on with, like, the profiler that we might be able to use as well, so… Nikola Grcevski @ Grafana / OpenTelemetry 00:12:02 Yeah, so we should propose a spec if we could come up with a good idea of how we do this.
Consistently, and I absolutely agree with you, right? A patient even, like, considers just metrics. It does it exports maybe HTTP, but there's no… DB metrics, and they're not implemented, and that is the case, so maybe only can supply those.
We are unable to do that at the moment. It's either or, right? So, the application starts sending its own metrics, which is sort of stalled.
And, yeah, some more of that, and I mean, I mentioned also the stuff that, Antonio wanted, so, for example, mixing up, application-level data with networking data, and I mean, we're uniquely positioned to kind of enrich those traces when applications. It's not possible to do across all programming languages efficiently.
So… yeah, keep pushing on that, I guess, to get it more of the enriching the ecosystem more than it's just been a replacement where you cannot instrument, or do not want to spend the time, so it's not… Sort of like a… Pullback, but it's enrich and pullback.
nimrodavni 00:13:19 It's cool.
Tyler 00:13:21 Well, cool. Yeah, we have an issue tracking this, right, Nicola?
Nikola Grcevski @ Grafana / OpenTelemetry 00:13:25 Yeah, yeah.
Tyler 00:13:25 Yep.
Yeah, so if folks wanna… we could probably check in that in a little bit on the roadmap, and yeah, I guess we can keep the conversation going there, too.
Nikola Grcevski @ Grafana / OpenTelemetry 00:13:36 Yep.
Tyler 00:13:39 Okay, Next up, Steven, you had some ideas on reducing total CI minutes instead of, fake APIs. You want to talk about something else? Yep.
Stephen Lang 00:13:50 Yeah, so, I looked into the fake APIs for, you know, Prometheus and Jaeger, but there's… there'd be quite a lot of, Code.
You know, to maintain, even if it's vibe. And also, I wondered… how much of an impact it would actually have versus what we have right now, and I think We're running with, in-memory-only databases for Prometheus and… and Jaeger.
So, I wonder if, you know, if it's the biggest impact that can be made to, the over 3 hours of CI minutes that's actually happening for the integration test suite. I'll be trying to think, what else we could do, like, big impact stuff on the workflow, and there's kind of 3 ideas that I kind of came up with.
One is, let's have a look.
First one.
container restarts, yeah. So, we do a lot of spin-up and tear down of containers on every single test, even though we split up across so many shards. Within each shard, we're constantly creating info and destroying it in terms of containers. But actually, if you think we have in-memory databases for Prometheus.
And Jaeger, actually, all you have to do is just restart the container.
And that should be enough just to wipe out its, in-memory database.
So maybe that's going to be faster than, you know, destroying it, rebuilding it, bracing it. So that's one idea, is to have, sort of, persistent collection containers.
Another is… How we have, like, so many workflows and checks that kick off on every commit domain.
and, obviously, every PR, every commit to every PR, there's loads and loads of checks that kick off.
In the case where There is just, like, a simple static check that fails. Say, for example, you know, a formatting issue, or, you know, even worse, if there's a compilation error, everything still kicks off.
You know, and I've tried to reduce the time to failure, but still, you know, we have the oats, we'll take 7-8 minutes until it fails.
Then we have, you know, all these other tests, ARM tests, VM tests.
They all… each of them take, you know, up to about 10 minutes to fail for a compilation error.
So I wondered if we do something similar, Tyler, to what you did with the release workflow.
Which is that we have some kind of, you know, higher level.
Workflow orchestration, where we put all of the workflows.
To go, kind of, based off a gate. And the gate is going to be, does Lint pass? Does compilation work?
And so we do that first. And also, we generate. So the generate is a big step, it takes, you know, a minute or two, but we're doing it constantly again and again on every shard, on every workflow.
So, maybe we should just do it once.
You know, so we do the lint once, we do the generate checks once, you know, we do the verification.
Once. And then we do the, the sharing of this artifact across all of the workflows. And the idea would be that we don't even kick off boats.
Or, you know, VM tests, if there's a link failure. There's no point.
So this would, like, massively reduce the number of, like, workers that we have at any one point in time, because a lot of the failures are just going to be, you know, around these, these limp failures.
And then also sharing this artifact across all of the workflows means that we're not having to constantly recompile, regenerate. You know, we don't have to run make docker generate on every single job, on every single shard. So.
Overall.
You know, the wall clock time might not be much different, but if you imagine rerunning an individual job, because it's already been generated, every rerun of every job will be at least 2 minutes faster.
So I think it'll be a nicer overall experience.
in combination with just this fast failure, in the case of, you know, you've got, like, a lint error, you'll see that feedback much quicker. And then, you know, we're not, consuming CI minutes and holding up runners, which are possibly causing other contributors to wait on, you know, the runner fleet or whatever.
And then finally, I actually thought, in the case of a lot of our integration tests, where we're just sending data and verifying that it was exported correctly.
Do we actually need this full infrastructure, or could we do something a bit more lightweight?
So the Prometheus, have a library for this called Test Util.
And it effectively just gives you, like, a… it gives you, like, an in-memory Prometheus that will just go straight to the, the Prometheus text exposition format, so you can, you know, effectively tell it to do a collect, at least for the Prometheus side, not for the OTEL side.
But we could effectively just check the exposition format to see if the metrics that are being exported by Obi are in the format with, you know, the correct labels and everything, and we don't need to send them over the wire.
And I think this could potentially be a way for us to just reduce the runtime of the tests, to have them act more like unit tests, rather than integration tests. They don't need necessarily all the infrastructure. This won't work for everything.
Obviously, in the case where you need system processes to be running.
You know, you've still got those dependencies, but in the cases where we're just checking.
you know, are the metrics in the right format? Are the labels there? Maybe we can move some of the tests over.
To be, unit tests instead of integration tests, and therefore just reduce the number of integration tests that we have.
And I figured a combination of these three ideas you know, altogether, should… be a much nicer experience, and just overall reduce the amount of time that we spend in CI.
Give you that feedback quicker.
And, you know, make reruns effectively.
Much more efficient.
So that's kind of what I was thinking, for kind of approaching this.
Tyler 00:19:59 Yeah, this is great.
Mario Macias 00:20:01 Yeah, that's great. Yeah. I think that, for example, this test tool till will be on… On one side, very useful. We currently have some unit tests that export the metrics, and we just verify the metrics.
Using regular expressions in the test, so this will make unique tests way more… solid. And also, at least for the Prometheus exporter, replacing the Prometheus scraper by just the integration test directly scraping OBI, I think it will be also pretty good.
yeah, approach, and we'll simplify… at least for the Prometheus test, for the OpenTelemet export, maybe we will need to find some… some other… Approach, like, container restarting, for example, as you say, instead of redeploying.
Stephen Lang 00:20:59 Yeah. Yeah, so, I mean, the goal here is to try and, like, do the big impact stuff, and then, you know, see where we kind of end up, and if OTEL is still kind of taking up the majority of the time.
We could, you know, approach it.
Mario Macias 00:21:13 Yeah.
Tyler 00:21:13 So for the hotel stuff, though, I don't, like, see why you couldn't do something… exactly like this. Like, we've done this as well in Go.
the GoSig before.
Where you have… Like, we… we will directly validate, like, OTLP, like, you can use, like, PTL utilities to do that, or Pdata Utilities to do that, and then, for, like, the collector, like, we also… we do that as well locally there. We'll just set up these endpoints that just… Directly collect the data and, like, keep it all there, and you can validate it.
They're just… there's local packages, though, but it looks very similar to this. Is there a reason why we want to do Prometheus instead of OTLP?
Stephen Lang 00:21:55 Oh, it's only because I was familiar with this library.
Tyler 00:21:58 Hmm, okay.
Stephen Lang 00:22:00 Likely we would need both, right?
Tyler 00:22:04 Yeah, yeah, I mean, I, I… I'd probably prefer the OTLP, given that's, like, the lingua franca of, like, OpenTelemetry, and we want to make sure that, like, we're exporting that correctly. I guess OB also exports Prometheus data, but I thought that that was just… Internal metrics, right?
Stephen Lang 00:22:26 Well, it can generate, spam metrics, right?
Mario Macias 00:22:30 Yeah, no, it can generate… all the metrics that can be generated with OpenTelemetry can be exported also via Prometheus. We have both exporters, and they clone the functionality.
Tyler 00:22:42 Okay.
Yeah, okay, then I guess that makes sense, we need to test both. But yeah, I would do something, I think, probably similar there for the OTLP stuff, I think you could do… I know you can do the same there.
And, like, I'm a bigger fan of, like, the more we can get into, like, these unit tests, the better, like, of the experiences of just, like, running GoTest.
It's way faster, and you can do it locally, and I think that, like.
That's fantastic, it can cut down on the integration load. I do think it, like… The moment that we can get integration tests faster, though.
the more we're gonna add. You know, like, I think it, like, there's always been this gap of, like, we say we have, like, this support matrix, but we don't actually test that full support matrix.
So, like, And I don't think it's reasonable to do that, because, you know, we're talking about you know, thousands of different combinations of different versions. So, like, I don't know if that's ever going to be realizable. Like, you would have to… You'd have to significantly, you know, 100x reduce the time for our integration tests to actually, like, make that possible.
But I think this is the right approach, like, the right start, at least. I do think that… the container restarts thing is kind of interesting to start with. So, like.
there is a way that we can also look at, like, using the Docker BuildX, like, caching structure.
Stephen Lang 00:24:09 Yeah.
Tyler 00:24:09 because you can… in GitHub integrations, like, you can actually have, like, a local, registry, like, to the actual build setup. So, it may be that, like, yeah, we wanna… I think, maybe reuse our builds, but, the more we can do that in, like, a registry as well, it may just automatically give us that, essentially. So, like, it can use the Docker semantics to understand, like, have I actually, you know.
done this build before, does this image layer exist already? Then I'll just pull it directly, and it pulls it much faster. But that does rely on us, like, restructuring.
Stephen Lang 00:24:46 Yeah.
Tyler 00:24:47 our Docker images, and making sure that we're not running this generate every single time, when we don't need to, but yeah.
Stephen Lang 00:24:53 Yeah, I did look at the layer caching, and it did seem to involve, like, having to rework some of our bugger files, just to take advantage of the layer caching.
But I mean, that's another possibility.
Tyler 00:25:06 I don't think that's a bad idea. I think our Docker files are, really well set up for, I think, what they were intended to do, but I don't think that they were really well thought out for image build, like, caching structure, outside of just, like, grouping commands and stuff. Like, the minimum image layers that we can build, like, the separations that we can build, if we can, like, get reusability, more isolated, I think that that could help a lot in the build times there.
The generate stuff is, is tough, because it, it, like, especially… The… the persistent memory across those, like, the way we use, like, the make targets to actually… tell you what needs to get built and what doesn't need to get built, and what does… you know, like, that doesn't work when you have, like, no timestamps that get copied over, correctly, so… Yeah, there's definitely some optimizations, I think, just looking at the containers themselves, like you're talking about.
The, I am interested in, like, the lint being a gate for all the other things. I think that it would reduce the artifact load, but you also are effectively making a serial lint than other things, instead of.
Stephen Lang 00:26:15 Dude.
Tyler 00:26:15 the…
Stephen Lang 00:26:16 You do, yeah. So, because everything kind of does it in parallel right now. It's the same with the generate step.
That's why I said you wouldn't necessarily see, like, a wall clock benefit from this.
Tyler 00:26:26 Yeah.
Stephen Lang 00:26:26 If anything, it might be 2 minutes slower, because you've serialized it.
Right. So the benefit would be when you're rerunning, because the generate step would be effectively cached, so when you do a rerun, it would be 2 minutes faster.
Tyler 00:26:40 Oh, because you're saying, like, the first lint would be the first generate, and then all the other ones wouldn't have to do the generate, is what you're saying?
Stephen Lang 00:26:46 So both, yeah, so there's kind of two parts to the, the, like, workflow.
It would be the artifact generation, which you would do first, and then you'd do the linked and whatever static checks as well, and then you would kick off the rest of the test suite. So you'd know that the generate step could generate a reusable artifact so that nobody else would need to regenerate. But then, yeah, you would have the lint as a static gate.
Mostly just to say that, is this actually going to compile?
Because you don't want to be testing compilation failures for things that don't directly do that, like an OATS workflow, or, you know, the VM workflow, it's going to be a while before they fail, so why even bother running that workflow if you know it's going to fail, is the idea behind putting the serialized gate.
At the first time.
Tyler 00:27:36 Yeah, yeah.
Yeah, I mean, I… I'm interested in this. I tried to do this in the auto instrumentation, the Go Auto project as well.
it was harder than I had originally anticipated. It sounds like you may have already got a proof of concept or something, but it was like… I remember getting something out and it being, like, 10 minutes slower.
Stephen Lang 00:28:00 Yeah.
Tyler 00:28:01 And, like, it was mostly just because, like, I thought all this caching layer and, like, this reuse stuff would, like, be helpful, but, like, it spent, like, way more time actually pulling artifacts than I thought it would.
Yeah.
Stephen Lang 00:28:13 you need to be careful with how large the artifact is, because then you're, like, network-bound instead of, like, CPU-bound, right? So you need to balance… balance it. Yeah, yeah. I have done the artifact caching already in some of the workflows, in, like, for example, for the Mac lint, it was required.
Because you can't build on a Mac.
So you must generate on Linux first, and then share the artifact to a macOS runner.
And so I know that that artifact is actually not very big at all.
So the… the generation of it… the compute is… takes much longer than just, you know, loading and reloading the actual artifact, which is what does make it faster.
Yeah, okay. But yeah, it does serialize it. It does put that 2 minutes at the head of the queue, and everything has to wait before it kicks off, which is why I haven't done it to date.
But I think when you look at the bigger picture of, like.
reducing the amount of time that we spend in CI. I think this is one of the things that we need, because it's something that is… it's 2 minutes on every single job, on every shard of every workflow, and this is kind of what adds up to, like, the three and something hours.
That we're kind of seeing right now.
Yeah. So it's… it's the cumulative effect of it that you… you benefit from.
Tyler 00:29:32 No, that sounds good. It sounds also, like, have you taken a look at the collector workflow as well?
Maybe it's collector contrib. But they do something very much similar. It's very gated like this, like, you're going through lint before they even touch integration tests or something like that, so… Yeah, I think it… they don't use as much Docker containers in their workflow, though, but I may be mistaken, but it might be just helpful as a reference, just as an aside.
Stephen Lang 00:29:58 Sure, yeah, I can… I'll take a look at that, thank you. And what was it you mentioned around the, the RTOP client libraries? Is that what Robert was talking about last week with,
Tyler 00:30:08 Yeah.
Stephen Lang 00:30:08 What he had done, because he has sent me some links to that.
Tyler 00:30:11 Oh, okay. Yeah, yeah, I would look at that, like, and then we also have, like, complete, like, Oh, that's all gonna be in, like, the Go format. There's PData libraries as well for comparisons, around, like, OTLP as well. So, like, one side is, like, emulating a collector, and the other side is, like.
comparison of that data. Because, like, the collector stuff is really simple, like… like, it's literally just an endpoint you set up with, like, some sort of… gRPC server running, and, then you just store it locally, and then you can build whatever workflows you want on top of that, like, if you want to give it some sort of validation function, if you want it to just give you back the data, if you want it to, like, collate, like.
So I think that, like, you can start building really, like, you know, dynamic testing utilities from whatever you want to do there. It's just about what you want from that, I think is kind of the question.
And so, like, yeah, like, I think that if you wanted to structure what would work best for us, I think that that's kind of, like, the ultimate question, but I… I really prefer having things go, like, I run GoTest locally, and it runs through, you know, data. Data goes through, OB comes back, and then I can see that, like, it was the right form.
Versus having to go find the mate command and then set up all these containers to get that same validation. It definitely helps, like, speed, but as well as, like, just utilities of tools that I'm using, yeah.
Stephen Lang 00:31:39 So it's kind of… I mean, part of this whole thing, the reason that I'm interested in this is speed of iteration, right? Because if we're iterating on the tests, if the tests take… You know, 30, 40 minutes to run, it makes it difficult to iterate on the tests.
If you can speed up the tests, that at least… it's maybe not the end goal, is to have the tests, you know, with this container restarts and shared artifacts, whatever, and the Prometheus side, it helps, but it gets you to a place where you can then maybe iterate faster on the test to get to where you want to be. It's like an end kind of goal.
Yeah, absolutely. So what I'm suggesting is not necessarily, you know.
The end… the end goal right now, but it is just kind of to improve iteration in this area.
Tyler 00:32:21 Yeah, absolutely.
Okay.
Yeah, we'll… I'll keep an eye out for your PRs. I mean, I think, Steven, this sounds great. I'm looking forward to it.
Cool. Do you want to talk next about the flaky test report?
Stephen Lang 00:32:36 So, I wondered if it's… so this has been running every day, I haven't really spent any time looking at it. Each one of these you can kind of click into, and it should be a report based on that day and the previous 5 days' worth of data.
And I wondered if this could be maybe something that we look at in the SIG to try and address, like, the health Of our test suite, because it affects everyone, you know, we're… We're getting all of these flaky tests, and it's difficult as a moving target from week to week. We might have different flaky tests.
I thought maybe if anybody might recognize some of these errors that has really been annoying them, maybe somebody would like to create an issue and pick it up, maybe we could use this to, like, delegate out, you know, the highest impact Errors that people are seeing, or, you know, maybe we could address to see whether the report is actually useful or not.
But for myself, I use this as an area to try and Target, like, which is the… the highest impact change we can make, like, which is the… the flakiest test?
Because if we can resolve that, then, you know, it's… It affects everybody, but all the contributing.
Tyler 00:33:44 Yeah, this connection to Refuse is the one that I've seen a lot. I'm surprised it's only one in this run.
Stephen Lang 00:33:50 So this… well, the report only looks at Maine as well, because I thought if we had the report look at all PRs, then, you know, people are going to be introducing failing tests all the time, and it's kind of difficult to… establish the signal on the noise. Whereas if you know it's on main, then it's something that's been validated, improved, and merged, yet it still flakes.
So, it is a subset of the test failures.
Tyler 00:34:16 Oh, okay.
Yeah, I mean, I… I… I'd love to maybe even… look at, like, a weekly roll-up, but yeah, I mean, I've definitely seen a lot of these.
This Rails one… yeah, I… yeah.
It's all the time.
Stephen Lang 00:34:37 Yeah, a weekly roll-up I thought about as well, because it's… right now, you don't really want to click through each day and try and correlate yourself.
Tyler 00:34:43 Yeah.
Stephen Lang 00:34:44 That might be an idea.
Tyler 00:34:46 That's a good point, I only went through one, too. Oh, yeah, and they're like… very different.
Okay.
This is a low pass, right? How'd we merge anything that day?
Oh, this isn't right. 4…
Stephen Lang 00:35:04 I wouldn't.
Tyler 00:35:05 Okay, alright, alright.
Stephen Lang 00:35:06 I wouldn't trust the numbers.
Tyler 00:35:08 Alright, yeah, you don't trust the numbers. Just look at the hard data, I guess.
What's this Docker error?
Stephen Lang 00:35:19 There should be a legend at the bottom.
And then, yeah, there's examples in the… in the fingerprint table there.
Tyler 00:35:25 Hmm.
Oh, interesting.
Yeah, this looks like… so the thing is, is I thought that we fixed this so it doesn't fail the CI.
Essentially, it's like, it's on teardown that the, that that was happening.
Damon… Image pull… oh, yeah, okay, no, that's… it's also… other errors, I guess, are causing it.
Stephen Lang 00:35:53 So it might be that, you know, the check actually failed for some other reason, and then this thing comes along and scans the logs, and it's picked up on that. It's not necessarily the reason for the failure, it's just one of the error logs that it found.
Tyler 00:36:06 Oh, okay.
Yeah, yeah, because I thought we did a lot of work to make these stop container things not actually fail, so you're probably right, it's probably something else that's maybe failing this. Okay.
Stephen Lang 00:36:18 So with these, if anybody wants to look at the report, there is a link to the failure, like, on the left there. So in the case where you see, like, cannot stop container, if you did actually want to investigate it, you could go ahead and click on the 24924, whatever.
And we do a scan.
Tyler 00:36:34 These are really annoying, these tests. I don't think it's just specifically, like, the red test, but, like, this 3 is not less than or equal to 2, like, there's definitely some, like… There's some flakiness in, like, our… This is, I think, more systemic of, like, how we're writing tests, where we're actually, like, saying.
I don't know, there… this open-endedness, like, when things get, like, jumbled like this, I see a lot of these as well.
Yeah, and it's not… it's a copied pattern, I think is the problem, because I see it, like, in a lot of different tests.
Stephen Lang 00:37:05 Yep.
Tyler 00:37:07 But yeah, I… I… I don't have a right answer to you other than… They're all annoying. They're all past.
Stephen Lang 00:37:16 Yeah, well, I mean, at least it's here, people are aware of it, if anybody wants to take a look.
Cool. I don't know if we need, like, an audit issue for it to say if anybody wants to pick up, you know, certain issues. Anyway, I'll look at doing, like, a weekly roll-up, because I think that could be useful.
Tyler 00:37:36 Yeah, that sounds great, I'd love to see that. Maybe it can get posted in the channel or something like that, the Slack channel.
Stephen Lang 00:37:43 Yeah, I can look at that, yeah. So the daily one's useful, because GitHub only keeps the logs for 5 days, and then they disappear. So if you did want to, say, do a monthly roll-up, you wouldn't be able to do it right now from raw data. You'd have to run over the… these reports, so at least this is, like, maybe raw data collection.
There's a start.
Tyler 00:38:00 Yeah, that makes sense.
Yeah, that sounds great.
Stephen Lang 00:38:05 Alright, thanks.
Tyler 00:38:09 Okay, last up, roadmap check-in. Looks like we've got, 20 minutes.
Well, cool. Nicola, I know you'd just gone over this yesterday in the spec meeting. Anything that stands out that needs to be updated? I can't remember specifically.
Nikola Grcevski @ Grafana / OpenTelemetry 00:38:30 We can kind of go over and see what, I don't think we have anything that we… completed. I believe there's additional protocols, maybe?
Can review that, if any of that's merged, but… I know there's a… NAS was merged?
We delete.
Tyler 00:38:51 Yeah, NASA's merged. Let's check that off. I think that there was more… Nikola Grcevski @ Grafana / OpenTelemetry 00:38:57 AMQP is on its way.
I believe it's a review.
Tyler 00:39:03 Yeah, I saw 1.0 PR for that, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:06 Yeah.
Tyler 00:39:06 Redis PubSub? No… This is pretty close. Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:13 It's getting there, so it's almost there.
Tyler 00:39:15 Yeah.
MongoD… oh, compression, oh, okay.
In version 5 and below? No, okay, yeah.
Damn.
Okay.
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:25 Cloud service SDKs. What's that? They're not Cameron?
Tyler 00:39:29 So, like, AWS CLI and, like, the GCP one, and I guess there's probably an Azure one, yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:38 Yeah.
Tyler 00:39:40 Oh, as well.
Nikola Grcevski @ Grafana / OpenTelemetry 00:39:40 here, I mean, with massive income fee, it's pretty… it's pretty good.
our protocols are piling up, and I mean, obviously, for the, But the Gen AI, we've gone way and beyond. Like, HiBeam, actually implemented so many things, and now, I believe, you know, embedding was merged.
So, it's a lot of fun out there.
Tyler 00:40:07 Yeah, okay.
This looks up-to-date. It looks… so it looks a little weird, because, like, the sub-issues, we only have 3 done. I do wonder, did we have, like, a GenAI issue that was tracking?
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:19 Yeah, I don't know if it's linked here. There's a separate GenAI issue.
Tyler 00:40:23 Yeah, let's see if we can… Nikola Grcevski @ Grafana / OpenTelemetry 00:40:24 I've been creating it.
Tyler 00:40:30 Yeah… Is this it?
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:34 Yeah.
Tyler 00:40:35 Yeah, okay, cool. Relationships work.
Apparent.
Okay, so that's tracking that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:51 Yes.
Tyler 00:40:52 I think this might be done, right?
Nikola Grcevski @ Grafana / OpenTelemetry 00:40:54 No, just scroll to the bottom, I think. There's still some things that…
nimrodavni 00:40:59 and some other stuff.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:02 tools.
And tools are interesting because the specter's changed, I believe.
Tyler 00:41:09 Mmm.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:09 limited tools, but embedding… embedding is actually done now, I just don't know…
Mattia Meleleo 00:41:15 I just merged it, like, one hour ago.
Tyler 00:41:18 Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:19 And so… I'm not sure it's fully done then, but I think it is.
Embedding is… I don't know, rewrite. I don't remember being an engineer render the team.
I don't think it was mentioned there, I don't know, maybe it's related, I don't really know.
So…
Tyler 00:41:40 Yeah, I don't know.
Nikola Grcevski @ Grafana / OpenTelemetry 00:41:41 updated, but… Yeah, a lot of it, it's on its way. It's moving real quickly, so… Yeah.
Tyler 00:41:51 Okay Well, cool, alright. Add that in there, then.
Look at that.
Cool. Alright.
Other than that, maybe we could just go through, like, these top ones, so we… additional protocol support, working on that, still working.
The 1.0 stabilization, still working on that. That's definitely the… the config PR, I think, is one way to take a look at this. We're also working at, security issues right now, and tightening up bugs, so that's another thing that we're working on, but I think other than those two things.
I don't think there's really… Nikola Grcevski @ Grafana / OpenTelemetry 00:42:33 things a lot.
Tyler 00:42:34 Yeah… So, yeah, config stabilization, the shoring up, Yeah, correctness and stability bar, so bugs and that kind of thing, working on that as well.
Telemetry stabilization… Nikola Grcevski @ Grafana / OpenTelemetry 00:42:50 Yeah, so, King Nimrod added… Weaver?
Into one of our… test suites, so maybe expanding on the Weaver support?
Because we do it for Redis, I think, at the moment, right, Linda?
nimrodavni 00:43:07 Yeah, I tried, I think I have something… I need to open a PR that adds it to a couple more stuff.
Maybe, like, the integration tests, I think that's the… I guess that's the main part we want to add it. I don't know if we want to put it in OAT, or… Other places?
And… yeah, I think there's some stuff with… The only thing that I'm not super sure with Weaver and telemetry schemas is that we have a couple of of stuff that we export that is kinda not in the semantic convention, like… Nikola Grcevski @ Grafana / OpenTelemetry 00:43:45 -
nimrodavni 00:43:46 either the custom metrics of, like, Stats Ollie and NetAlli, or even the SPAN metrics and service graph, which are… Like, they're described in the, in the, collector, but they're not… I don't think there's, like, semantic convention for them.
So either we need to create our own telemetry schema for that, and say, like, okay, we export the, like, no, the default, like, semantic conventions, version whatever, 1.38 now, in addition to these stuff.
Tyler 00:44:21 Yeah, we should, we should do that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:44:23 Yeah.
Tyler 00:44:24 That's…
nimrodavni 00:44:24 Excellent.
Tyler 00:44:25 do it. And what we can do is we can publish what our schema is alongside the binaries and things for folks that want to see it.
Nikola Grcevski @ Grafana / OpenTelemetry 00:44:32 Yeah, exactly. Because, I mean, we deviated. I mean, nobody thought that you could instrument SQL databases as servers, but we do it.
And people do it. So, that spec is missing, right? But we… we should start generating the servers, you know what I mean? They're not clients.
server.
nimrodavni 00:44:55 I think there's some issue now that's, like, you can't… Weaver can't run against two registries at the same time. Like, you can't…
Tyler 00:45:03 Yeah, so our registry should definitely import and be based off of the upstream Semantic Convention Registry.
nimrodavni 00:45:10 Can we do that? Can we say, like, our registry is this, plus some other stuff, and then, like, point Weaver to that? I never tried it. I can try.
Tyler 00:45:18 I think you can. I think there's inheritance in there, but if not, then I would… it's worth opening an issue for that, because that… that's… yeah, for exactly the point you just… you just mentioned.
nimrodavni 00:45:28 Okay.
Antonio Jimenez 00:45:28 you can ex… you can extend it. So you… you say that your custom metric extends the semantic conversion from OpenTelemetry. This is what, kind of, we do in ThousandEx.
Tyler 00:45:38 Yeah, yeah.
nimrodavni 00:45:39 So I'll… I can try that and at least try to expand the telemetry, the semantic coverage on our end-to-end integration test.
Tyler 00:45:49 Yeah, even if… even if we just do… like, raw semantic conventions, we didn't go beyond it, we should still probably publish our own schema because of that exact thing where people can then… import it, and they can use Weaver to do dynamic telemetry translations the way they want to, and so we can just be very clear about what we're exporting. Yeah, so that's a great idea. I think it's excellent.
nimrodavni 00:46:14 Okay, I'll work on that.
Tyler 00:46:17 Yeah, awesome. I'm super excited about that. I must have missed the Weaver PR, Or I'm just not awake yet. But yeah, thanks, thanks for doing that, that's awesome.
Okay, cool.
Going back to here, the .NET support, I don't know if I saw Raphael on the call.
Rafael Roquetto 00:46:37 I'm here, yeah. Oh, cool. Very, very next thing on my list. So, getting started.
Tyler 00:46:44 Yeah, until we put some more things on your list, don't worry.
Rafael Roquetto 00:46:47 But, yeah.
Tyler 00:46:48 Okay, cool.
And then, this is the OTEL API SDK integration ticket, so this is a little bit broader than just what we were talking about earlier, but yeah, there's definitely… this is where I think that we could have a lot of the conversation around, that integration we were talking about.
Nikola Grcevski @ Grafana / OpenTelemetry 00:47:04 Yep.
I added some of those comments in there, so…
Tyler 00:47:08 Okay, cool.
Yeah, so what, what mechanism is being proposed to have that communication? Like, what's the, the transport gonna be? Is it… Nikola Grcevski @ Grafana / OpenTelemetry 00:47:21 Yeah, in terms of thread… thread-native storage, I believe.
The two old tabs mentioned do that, sort of let the SDKs write.
And for the thread memory, and then even be able to create that.
No, it's valid.
on.
I don't know.
Tyler 00:47:43 Just, is it gonna be in, like, a specific location that will, like, know how to find it, or will they public… like, how do we find it?
Nikola Grcevski @ Grafana / OpenTelemetry 00:47:51 I think it's going to be in a specific location, so you go on the thread local storage into that region, you pull it out, and then you look at certain offset, the final magic thing.
Tyler 00:48:03 And it's a one-way communication protocol, like, we're not able to communicate back to them?
Nikola Grcevski @ Grafana / OpenTelemetry 00:48:08 No, not envisioned at the moment. None of those two old tabs that was mentioned here do that. I think it's primarily for us to kind of figure out I mean, if we were going to write back, then we need to rely on the BPS ProWrite user.
There's no other way. I mean, the only way you can write is through network stuff, but that means there's network traffic, so… maybe… maybe we can think of the network traffic to the SDK somehow, but then that involves opening ports and… It's kind of ugly.
Tyler 00:48:43 Yeah, I was thinking about network traffic, but even on localhost, like, you can write it over pipes, right? Yeah.
And then… You get the problem of… collating?
Because, I keep going back to, like, Go, right? Like, Go is gonna be a tough one, because Go doesn't actually, like.
as an SDK doesn't, like, pull in all of its instrumentation. Each instrumentation is its own package, right? So how does… How does it, like, register? Is kind of the question? And, I don't know, so maybe there's, like, a shared memory thing where you can… in itself, like, that instrumentation has its own, so you can find it that way, but I don't… I don't know what that registry mechanism's gonna look like.
Nikola Grcevski @ Grafana / OpenTelemetry 00:49:28 Yeah, but maybe Go, we don't actually could do even today. I'm just thinking Go's possibly easier, because we can read the symbols and figure out what's actually imported, and then we know, does it… did it instantiate maybe the network, sorry, the metrics and the tracers?
Or does it do certain kinds of instrumentations?
Tyler 00:49:52 Yeah, I mean… Yeah… Nikola Grcevski @ Grafana / OpenTelemetry 00:49:56 I mean?
Tyler 00:49:57 So kinda, right? Because then there's still a problem of, like, so say, like, gRPC instrumentation, or maybe let's pick a better one.
Nikola Grcevski @ Grafana / OpenTelemetry 00:50:04 Dude.
Tyler 00:50:06 Yeah, say Mongo… MongoDB instrumentation is there, right? And which… which one is there is a problem? Which version of it is a problem? And, like, you would then have to be the one who tracks all of the, like, the schemas for each… each one of those things, right? And then that's just… that's just Mongo, right? And then… Yeah, so, like, I think that it's… it's gonna be, like, extremely hard for us to, like, be the one of, like, the source of truth there. It definitely has to come from the instrumentation.
Nikola Grcevski @ Grafana / OpenTelemetry 00:50:36 It's gonna be tough. Yeah, it's not an easy task. I don't think we're gonna do it this year, to kind of… to be honest. I was more thinking, if you read the sort of description of that proposal here, what we do this year is just sort of try to fit in.
No, not this one, maybe scroll up.
I think this is going to be… take a long time. Probably be… oh, be a little bit more, sorry, in the description of the actual issue.
So, if we see, like, This is talking about other things, such as… like, right now, like, we shouldn't confirm that exemplars do work in metrics with the OTO. It's just doing traces, right? Which is very common, like, that's the case. Oftentimes just enable tracing, but… the previous metrics, and examples should just come out from the hotel trace information, rather than Right. I think this works today, we just need to confirm it, or make sure it works.
Because we should be able to radiate the trace information as it flows through.
done by the SDK, because it's going to be on the incoming request, on the outgoing request, and should be able to produce If we can metric exemplars.
So that would be quite cool. So then… You don't have to worry about… generating metrics for every SDK. As long as traces are there, then exemplars work.
And then, this thing I talked about, like, generating the span events.
to kind of add the accurate timings. I think we can do all those things without having to communicate with the SFK.
consistent.
Tyler 00:52:23 Yeah, this one… this one seems the most… like, reachable? Because, like, I think the answer here is on us, it's just, like, instead of completely turning off, we just turn into a, like.
wrapper mode, or something like that, right? Like, I feel like we should be doing this already right now, like… Nikola Grcevski @ Grafana / OpenTelemetry 00:52:40 Yeah, I know. I know.
Tyler 00:52:44 Yeah, I think that that may be the way we want to look, like, frame that. That, like, seems like a really easy fix, because, like, we're already doing all of this telemetry for them, and, like, it's just about that selection criteria being, like, okay, so turn this off, but don't turn it completely off, like, today. Like, we can do that, because we know no other SDK is doing this right now.
Nikola Grcevski @ Grafana / OpenTelemetry 00:53:02 Yeah.
nimrodavni 00:53:03 We can have the same with other stuff, like, TCP and DNS and stuff that we know there's no, like, instrumentation for. We can, like, we can have, like you said, like a supplement mode where we… Nikola Grcevski @ Grafana / OpenTelemetry 00:53:17 Yeah.
nimrodavni 00:53:17 And they use the same trace context, but we know we export only stuff that aren't for sure not part of the auto-instrumentation.
Nikola Grcevski @ Grafana / OpenTelemetry 00:53:26 Exactly. So, I really like span events for that, to be honest, but I know they're going away, but it's gonna be a while, so me and might as well try it, see how it works, and then figure out an alternative.
Once they go away, we're in the sort of deprecated.
Because I think the events kind of fit in nicely. It's like, you still get your trace, but we also tell you this auxiliary information.
Tyler 00:53:51 But did we want to work on, like, just… Using the event system?
Like, the logging event system?
Nikola Grcevski @ Grafana / OpenTelemetry 00:53:58 Yeah, I mean.
Tyler 00:53:58 Thumb that in.
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:00 Yeah, there's an alternative, kind of, but it rolls vlogs. But it's not bad. I mean, vlogs are great, so… Yeah, or maybe we do both, and… Yeah, I'm gonna start on that soon, if nobody else wants to, but… It's on my list.
Please try that. I'm particularly about the timing, because I think that's a really nice sort of augment the data. Like, we know the actual timing, we should just tell it.
Yeah. It might be SDK to do its tracing.
Tyler 00:54:38 Yeah, that sounds good. And then these other items, Nicola, the… I'm guessing, like, this other stuff, this developed, this hybrid stuff, you're saying is probably gonna get bumped to next year?
Nikola Grcevski @ Grafana / OpenTelemetry 00:54:46 Yeah. Yeah, that… I mean, the… yeah.
I don't know, it's kind of hard to do it, I think, generic, like you said. Every SDK is slightly different, it's going to be a long tail of… SDK changes in relationships between all the teams.
to kind of supplement the CPPF data.
Tyler 00:55:08 Yeah, I… It's like, networking kinda is a little bit easier, Because you can just say, like.
Nikola Grcevski @ Grafana / OpenTelemetry 00:55:18 here.
Tyler 00:55:19 here's, like, go look and see if this endpoint is up, that means Obi's running, and then send it your data.
But then you have networking. I mean, it's not like networking's a big overhead if you're just gonna be doing this once, you know, like, oh, it's up, like, I'm gonna go send it, like, I'm gonna go register, essentially.
But then you have to, like, have… you know, what happens when OB comes up after the instrumentation, right? Like… Yeah, there's all these, I think.
Nikola Grcevski @ Grafana / OpenTelemetry 00:55:46 Yeah, exactly. I was also thinking, man, can we actually extract all of this?
Because we do see the payloads. I think Rimrod floated this idea a while back, if I'm not mistaken, that right now, we just say, oh, there's the metric exports, and we sort of stop there.
Technically, we can look into the OTLP payloads and extract what metrics are being sent, or seeing if we notice Mongo traces being sent, and okay, Mongo is enabled.
And then we can tell, oh, we see are these additional protocols, but they're not actually exported, so there's no instrumentation for this. We can do payload extraction on the OTLP.
Tyler 00:56:34 So is it… is it… maybe a better way to start is not about, like, one-to-one metric mapping, but more about, like, service mapping?
So if you see something, like, instrumenting Mongo, or you see something instrumenting HTTP, like, don't go and say, like, are you implementing these… well, I don't know, that's kind of a problem, it's like… Yeah, what if it's instrumenting a database, but there's no, you know, there's no… specific calls that we can provide that it doesn't provide, I guess.
Nikola Grcevski @ Grafana / OpenTelemetry 00:57:06 Yeah.
So, I mean, we watch all the traffic, so we know what kind of traces are being made. So right now, what we do is we say, okay, so this traces our to an application that's already doing tracing, so we just short-circuit them. But instead.
Tyler 00:57:21 Yeah, but what if… Nikola Grcevski @ Grafana / OpenTelemetry 00:57:22 frozen.
Tyler 00:57:22 What if the semantics are different, slightly, is the point?
Nikola Grcevski @ Grafana / OpenTelemetry 00:57:25 True. I mean, that, that, that is really hard, but I mean, baby steps, but what I'm thinking is that… so we see all these traces, and let's say we see traces from Mongo, Redis, and whatever, and then instead of… We currently discard them all, and instead we start building a sort of, like, internal database about that service, and say, we see all these protocols used by this service, for example, Gen AI.
And then… We then inspect the payloads that the service is making, and… kind of keep track of what they're doing, and after a while, say, okay, they're not exporting this rate as mass, maybe they should, kind of thing, you know, I, or there's no JNAi support here, let's enable the JAI for this service. I think it's doable. It's easier for.
Tyler 00:58:11 Yeah, or… Nikola Grcevski @ Grafana / OpenTelemetry 00:58:11 to be honest.
Harder for Tracy. Yes.
Tyler 00:58:14 That's… yeah, exactly, that's kind of where… I think that's maybe… Yeah, like, if you can do, like, a rolling queue, because, like, even it's kind of, like, right now, we kind of do a… like, just go for it to begin with, and then if you find the service is actually exporting OTLP, then stop. Maybe we can do the same thing, it's just, like, just start reporting all the spans normally, and then if you find… if we find some sort of, like, duplicate, like, heuristic.
then we can turn it, like, turn it down. So maybe there's, like, still a chance you would have some duplicates to start, but, like, we'll, we'll, you know, get to a steady state pretty quick, yeah.
I think that might actually be the way to… yeah. Yeah. That'd be… that'd be pretty slick, And I think you would, like, we'd blow people's minds if we were able to do that.
Nikola Grcevski @ Grafana / OpenTelemetry 00:58:56 Yeah.
Tyler 00:58:57 Which… Yeah, but maybe we also need to, like, embed an AI agent into our server?
Nikola Grcevski @ Grafana / OpenTelemetry 00:59:02 at that point? Yeah, to kind of, like, sniff all the payloads.
Tyler 00:59:07 Yeah.
Nikola Grcevski @ Grafana / OpenTelemetry 00:59:08 all this information. It's a lot of processing, but… Yep, but we can start with metrics, and just, supplement that, and then I'd say… because I think a useful scenario is that maybe the user has used, metrics, but only they're exporting business-level metrics, and now we're turning off all HTTP, DB metrics just because they are.
Tyler 00:59:29 Right.
Nikola Grcevski @ Grafana / OpenTelemetry 00:59:29 supporting their own, right? And… It's not great.
So, I think maybe start with metrics, try sniffing the payloads, because usually the full list of what metrics are exported, and I would pull. So, we'll push them out. Yeah.
nimrodavni 00:59:48 I think for that, we need, like, gRPC, payload extraction, and… Nikola Grcevski @ Grafana / OpenTelemetry 00:59:54 Gotcha.
nimrodavni 00:59:55 schema… I want… I had… I have it on my list as well, like, research how we get the… with, like, gRPC, like, reflection, or maybe pointing to some GitHub repo, or some.
Nikola Grcevski @ Grafana / OpenTelemetry 01:00:10 Okay.
nimrodavni 01:00:10 They comment, I don't know, I want to try to do that, so… it might help.
If I have to… Nikola Grcevski @ Grafana / OpenTelemetry 01:00:14 Okay, yeah, yeah.
Oh, yeah, you're right, yeah, gRPC export, so we need a large buffer support for GRPC, which we don't have, but we can add it.
nimrodavni 01:00:26 And we can have full payloads.
Tyler 01:00:28 We're right at time here, so I want to call it. Yeah, thanks everyone for the discussion. Obviously, a lot more to talk about, so yeah, we'll continue on next week. See you all in that time. Bye.
Nikola Grcevski @ Grafana / OpenTelemetry 01:00:38 Bye.
nimrodavni 01:00:39 Yeah.
