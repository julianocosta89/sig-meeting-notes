SIG: eBPF Instrumentation
Date: 2026-07-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 00:13 Hey, Mario.
**Mario Macias** 00:15 Hello, Tyler, good morning.
**Tyler Yahn (Splunk)** 00:17 Morning, how you doing?
**Mario Macias** 00:19 I'm doing good, and you?
**Tyler Yahn (Splunk)** 00:21 Yeah, doing well. Going slow. A little… Little, I don't know, I feel tired today.
**Mario Macias** 00:28 Okay, okay.
Are you doing holidays near… near this summer, or…
**Tyler Yahn (Splunk)** 00:36 No. Well, I'm taking Friday off.
**Mario Macias** 00:40 Oh, God.
**Tyler Yahn (Splunk)** 00:40 Yeah, I'm gonna go do some, fishing on a river, so I'm pretty excited about that. But, how about you? Taking some time off, I'm guessing?
**Mario Macias** 00:49 Yes, I'm… I'm in the three, first three weeks of August.
I'll be off, so yeah, we will see each other in 4 weeks.
After this meeting.
**Tyler Yahn (Splunk)** 01:04 Nice. Are you going anywhere fun, or just hanging out, nearby?
**Mario Macias** 01:09 I'm… yes, I'm staying nearby, and we got some… a couple of hotels in New York City.
Yeah, we don't like to travel so much in August, because everything is super crowded.
**Tyler Yahn (Splunk)** 01:24 Yeah.
**Mario Macias** 01:24 It's super expensive.
**Tyler Yahn (Splunk)** 01:27 Yeah, all you Europeans, you love… you love traveling in the summer, boy.
**Mario Macias** 01:30 Yeah, for some reason.
**Tyler Yahn (Splunk)** 01:34 Yeah.
Yeah. I, like… it's always actually nice to have coworkers, In Europe, because they remind you, like, hey, you should take some time off.
Like, yeah.
**Mario Macias** 01:48 That's true.
**Tyler Yahn (Splunk)** 01:49 Yeah.
Looks like, everyone else is joining.
Welcome, everyone.
If you haven't yet, go ahead and add your name to the attendees list. If you have agenda items, you wanted to talk about, please go ahead and add them there as well.
We can give it just a little bit longer, and then we'll probably jump in here in just a second.
Is Nikola able to make it, or is he out?
**Mario Macias** 02:19 I think he's out, yeah, he's on PT on holiday.
**Tyler Yahn (Splunk)** 02:23 Okay, cool, right.
Cool.
Awesome, alright. Well, let's, let's jump in here, 3 minutes in, yep.
Cool, so first up, Mario, you wanted to, talk about Dino support. Hand it over to you.
**Mario Macias** 02:56 Yes, just to… to agree on some parts. I'm extending current JavaScript framework support, runtime support to Deno.
One thing is that, there is no… in… in the OpenTelemetry standard, there is OpenTelemetry… telemetry SDK language equals, Node.js, but there is no one for Deno, no semantic convention. I… the Deno people have their own OpenTelemetry exporter, native… experimental native exporter.
And they use Deno Rust. I don't… I don't know why they should add Rust, but they are… they do it, so… should we maybe keep the same convention as they do? Dino Rust?
**Tyler Yahn (Splunk)** 03:45 Do you not know why they have Dino Rust, instead of, like, Deno Zig?
**Mario Macias** 03:51 I know, because the, the, no, no, Zeke is the, bun, the boon.
the boom runtime is using Seek, and they move to Rust.
**Tyler Yahn (Splunk)** 04:01 Oh, right, that's the one I'm thinking.
**Mario Macias** 04:02 Yeah, Dino, I think, was written in grass from the beginning.
**Tyler Yahn (Splunk)** 04:06 Oh, okay, okay.
**Mario Macias** 04:08 But, you know, Rust programmers love to let people know that the code is written in Rust.
**Tyler Yahn (Splunk)** 04:15 Yeah, just wait. Somebody's gonna come in and ask us to migrate to Rust.
**Nimrod Avni** 04:19 Nairobi to Russia.
**Tyler Yahn (Splunk)** 04:21 Yeah, yeah.
**Mario Macias** 04:23 Oh.
**Tyler Yahn (Splunk)** 04:24 Yeah, I mean, this sounds… this sounds good to me, Mario. I mean, I… I think using this… I don't know why this isn't up in the semantic conventions, but that makes good sense. I also think this… Rename definitely makes sense, if we're… yeah, we're gonna go in that direction, I think that that makes a lot of sense to me. Okay.
**Mario Macias** 04:42 Yeah, the other option would be keep Node.js enabled and DNO enabled, but maybe it gets unnecessarily complex. Even that part of the code is shared, and the process, so maybe we can move it to JS or… Something like that.
**Tyler Yahn (Splunk)** 04:59 Hmm.
Yeah, any other thoughts on this from other folks?
If not, we can keep going.
**Mario Macias** 05:11 Okay.
**Tyler Yahn (Splunk)** 05:11 Cool.
Alright, Mario, next up you want to talk about ARM integration tests.
**Mario Macias** 05:16 Yeah, yeah, I just realized that today while fixing a flaky test in CI, I realized that it failed in my local machine because of a bug in our ARM code.
And it seems because we run ARM tests, but only the multiprocess tests. There are many other tests we don't run, so shall we? Even if that can delay the… or call slow down the CI, maybe shall we run ARM test? At least, for example, when… when we modify the eBPF code.
running… don't trigger it in all… in all the… in all the PRs, but maybe when… when BPF code is modified.
**Tyler Yahn (Splunk)** 06:09 I mean, it sounds good to me. Steven, you have thoughts on this?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:13 Oh, well, I was just wondering, Mario, if you knew the context of why it wasn't enabled everywhere in the first place.
**Mario Macias** 06:20 I don't know, maybe… maybe just to be quicker… Yeah, I don't know. Maybe we have less test runners in ARM test runners, so just to save some time or save resources, I don't know, I don't know, yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:36 Okay.
**Mario Macias** 06:37 Maybe we felt it wasn't necessary.
**Tyler Yahn (Splunk)** 06:39 It might also have been a mistake, though, as well. Yeah.
**Mario Macias** 06:42 Yeah.
**Tyler Yahn (Splunk)** 06:42 Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:43 So, I think before we had ARM runners in GitHub, I think they were all emulated through, QEMU, so… Maybe they used to take forever.
And now we have the native arm runners, maybe it's not an issue anymore.
**Mario Macias** 06:58 Okay, okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:59 I mean, I could take on this, if you like, and just, basically trying.
**Mario Macias** 07:03 trailers.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:04 mirror.
**Mario Macias** 07:04 as you want.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:05 Maybe we don't need separate ARM tests anymore, we can just matrix the existing ones that we have and run them on both platforms.
**Mattia** 07:13 Just one thing, I think we have ARM integration tests somewhere running, but they don't run the whole suite, they run…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:22 That's what… that's what Mario said, yeah, so they… they…
**Mario Macias** 07:25 Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:25 Match on the multiprocess tests.
**Mattia** 07:28 Yeah.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:28 Not all the suites. So I wonder if we could just simplify it and actually just remove all of the separate ARM workflows.
And then, you know, matrix the existing workflows.
**Mattia** 07:39 Yeah, that would… that would be.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:40 the arm runners, so then we're not, like, differentiating them at all. If everyone thinks it's okay that we just run all the arm tests all the time.
**Tyler Yahn (Splunk)** 07:51 Yep.
**Mattia** 07:52 Yep.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:53 Okay. Okay.
**Mario Macias** 07:54 Thank you.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:55 I'll take that as a follow-up, then.
**Mario Macias** 07:57 Great, thank you.
**Tyler Yahn (Splunk)** 07:59 Awesome. Yeah, thanks for bringing that up, Mario. Let's… let's definitely address that.
Okay.
Next up is, me. I'm asking for a review on a PPR, so one of the ones I wanted to get out of the way at first was this, Yeah. This PR to enable the standalone configVT runtime loading?
So, yeah, this is, I think… kind of like the last… well, it's not the last, it's one of the last in the conversion, before we get the release out. So essentially, it just is in our CLI, we're able to parse and, actually support the V2. It's all there, all the tooling.
As you all are painfully aware, there's been a lot of code changes to support that, so this is the last thing that says, like, we could actually use it.
it updates the CLI again, like I said. So, yeah, looking for reviews on this. Actually, I don't know why this isn't in the milestone, but yeah, this is one of the things that we need to do. It's gating our milestone release, so… Yep, asking for a review on this one. I know Nicola has taken a look, but he's out and, I… yeah, I was hoping to get another review from him, but… Not gonna have him.
Okay, cool.
The other one's a lot smaller, these are cleanups, to the config. I'm working on also documenting, this migration path, and in the process of documenting this migration path, I built a PR, and it's… Massive, So, yeah, this is, oh, sorry, no, this isn't actually that. This is a totally different bug that I found. Yeah, sorry, I'm getting confused. I had a bunch of other things. We'll talk about those in just a second.
This is a bug where, just, I was noticing, the route harvesting expansion, for this is not capped. In fact, it's, like, unlimited right now. So, yeah, through some, auditing of, some security issues, this is one that, like, I found it's not really, like, critical, but yes, one I put in just to limit this routing.
This needs review, should be pretty straightforward.
The other ones, though, yeah, now these are the ones that I found where I'm trying to document, and just cleaning up, things. One of the things I've noticed was, yeah, our YAML export mode, is great, but it can be, encoded from a map, so this stabilizes that export form, so it'll always show up in the same form. This is pretty straightforward, it's really small. So, yeah, that one's… just needs eyes on it. Oh, Mario, I didn't see you left a comment, sorry.
**Mario Macias** 10:43 Yeah, for me, it's okay, I will approve it now, but I would suggest just adding some context as a comment, because that sounds to me like something next year I can see and say, why are we doing it this way? Remove it, improve it, so…
**Tyler Yahn (Splunk)** 11:00 Yeah, sorry.
**Mario Macias** 11:01 For the rest is okay.
**Tyler Yahn (Splunk)** 11:02 Yeah, I can definitely add a comment. That sounds like a great suggestion. Thanks. Absolutely.
Okay.
Others is keep language detection, skips with the internals. So, right now, there's, like, a conversion.
Process that we've always tried to skip this, so this is a little bit complex, but… Currently, like, in the V1, there's this Discover Exclude Linux system path.
If this is enabled, that means that, like, our new routing policy actually conflicts with it, so this is actually ignored in the V2. There isn't, like, a conversion for this, so this is something that, like, the routing policies cover this, you can… you can… you know, exclude these paths already, but, like, having this and then trying to, like, convert this into rules doesn't really map, because it's going to be a rule selection, you know, by process, or whatever the rule capture selection is. So, this is just, making sure this is ignored in all of our, like, conversion and migration paths, so… Yeah, this looks like, again, I didn't see these this morning, sorry. Looks like there's some feedback from Copilot, which I'll plan on addressing afterwards, but yeah, also just some reviews. Thanks, Mario, for kicking that off. That's a good idea.
And then the last one… Yeah, this is for the, support for the Auto SDK. So, this is the thing where we're trying to do for, Go API, calls in OTEL. We want to be able to try to support them. I've got a PR to actually activate that. It's something that, like, we've been working on already as well, like, we've got the offsets in for all of the, the functions for the Auto SDK.
We've got, a lot of the probes are already written, it's just that right now we are not actually loading any of those probes.
And so one of the things that, like, I have a PR to do that. It's quite large, it's about 3,000 lines, so I'm trying to break out some other function of it. This is one of the things that kind of stood out that we can break out. Essentially, like, one of the things that I'm doing is if, Let's see if I wrote it down there, but essentially, it's just like… if I go to load the probe, but BPF write user's not there, if the offsets aren't there, if the, you can't find any of the symbols, I don't want to actually load any of the probes.
And so, each one of those things, essentially, I want to group all three probes to be run as one particular, you know, set, and so what this is doing is it allows you to run, you know, a set of probe, You know, additions, and if they fail, it has a clean rollback, is kind of the idea.
It's included in the other PR, but this is actually, I think, a cleaner approach in this PR, where it just, you know, builds the utility instead of doing a one-off thing for those other probes. So, yeah, just looking for a review on this one as well.
Okay, cool.
And then, the last thing that I wanted to bring up, is this sampler decision.
Which has been sitting in the back of my mind for a long time. I've got a… proof of concept started for this, but the issue is that currently right now, as far as I understand it, and correct me if I'm wrong, is our sampling decisions are done during, like, the export phase of telemetry.
So, meaning that, like, we gather every telemetry, there's not really a reason we wouldn't gather telemetry, meaning that, like, you know, if we look at it as something that should be, you know, a span, there's not any sampling decision of whether that span should be made or not. So essentially, we're always a, recording operation for all of our gathering, right? Then, when we go to export, we do some sort of sampling with our samplers. We obviously support, like, the most or all of the hotel samplers, The problem becomes, though, if we're gonna support things like the Go Auto SDK, or I'm expecting the Node.js, manual spans as well, this is something that, like, won't work, given the fact that we need to have a sampling decision when the span is created to actually, like, tell, hey, that span right there that you're creating is not recorded, or it's sampled, or it's not sampled, or something like that. And so… What we've done in the Go Instrumentation project, when we supported the Auto SDK, is essentially that we pushed down all of our sampling decisions into the eBPF space, so as the span is being created, it's actually determining this.
So, there's… I mean, there's some wins there. Obviously, we can support the Gato SDK sampling, meaning that, like, you know, if they have decisions in their codebase, they can use that sampling decision there.
It definitely reduces the telemetry pipeline as it's coming through, but the real downside, obviously, is that it's, like, way more complicated. I don't know if anybody has seen the… the Auto SDK, or the Go, Instrumentation project, but, like, yeah, like, the sampling there is… it's much more complicated, because you obviously have to, like.
you have to encapsulate the sampler, which is not hard for the always-on or the always-off, it's the parent sampler, where you've got, like, what is the root span decision, what happens when it's, like, a parent span, what happens when it's, like, yeah, all of these things need to get, like, pushed down into eBPF configuration.
It also limits the ability for extensibility of our samplers. Like, right now, we support these 3 samplers, but… like, if a user wanted to come along and give us a custom sampler, like, that is, if it's defined in Go, like, that's not possible. Like, there's maybe a possibility of, like, trying to say, like, you need to give us other… functionality, maybe we can incorporate it, but yeah, that's definitely a limitation, but… Yeah, I wanted to bring this issue up, because this is going to be needed for the Go Auto SDK, like, sampling, and I'm guessing Node.js as well, but, yeah. Sorry, I'll stop talking. Go ahead, Mario.
**Mario Macias** 16:47 No, I was thinking, whether, for simplicity.
We can add the sampling, not in the VPF level, but in the very first stage of the pipeline. When the span traverses the ring buffer before we decorate it, we filter, or whatever, we can drop it there.
It… the advantage… the disadvantage is that the ring buffer will still be, active with traces that won't be emitted, but at least the rest of the… Pintering and decoration pipeline will be emptied at the very early stage.
just proposing as an alternative in case we find eBPF is too complex, but otherwise, eBPF looks, for me, okay for me if… If it's possible to do it.
**Tyler Yahn (Splunk)** 17:38 So that… I don't… don't know if I fully understand, but essentially, like, I don't think that would work, because, like, the u-probe for the start operation in the Auto SDK has already returned at that point. So, like, you don't have… I don't… I think you might still be able to… technically right to the span context that you returned, but, like, it's already likely being used, and then you get race conditions as well around that, like, whether, like, the sampling decision, you know, is before or after.
**Mario Macias** 18:06 Yeah, okay, okay, yeah.
Now I understand better, yeah, yeah, yeah. Okay.
**Tyler Yahn (Splunk)** 18:11 Yeah, yeah.
Yeah, so, yeah, that's why, yeah, like, I wish… If you can think of another way, I am looking for another way. Like, because if we can still support, like, Go samplers, that'd be really great for users to be providing extensibility to Opie eventually.
**Mario Macias** 18:26 One day.
**Tyler Yahn (Splunk)** 18:27 But, like, Yeah, I… I think… and I think there's a way you could possibly do this as well, but, like, right now, I couldn't figure this out before in the Auto SDK, or the Auto Instrumentation for Go either, so I was thinking, yeah, eBPF was the way, but, like, yeah, I'm happy to keep thinking if you guys have other options there.
But yeah, it, like, it just needs to be there during the U-Probe, is kind of thing.
**Mario Macias** 18:52 Okay, okay.
**Tyler Yahn (Splunk)** 18:54 Yeah.
And, it's also kind of an awkward one, because, like, all sampling decisions, like, especially, Actually, I don't think any of ours… the trace-based stuff, actually, with the parent stuff, there is, like, an upstream requirement for W3C on, like, looking at the existing trace ID, to make the distinction based on, like, this new correlation.
But technically, it's supposed to get all these span parameters when it actually makes a decision, but I don't think we actually use any of them. Oh, except for the root stuff.
I'm saying this because I was thinking it'd be really nice if we could just make, like, random, you know, numbers and send them down through the pipeline, but, like, they need to be done in context of whether it's a root span or not, is kind of the problem, so, yeah.
But yeah, please take a look at the issue. It's definitely one that I'd like to, you know, I've got some work going on, a proof of concept, but yeah, like, it's, still looking for a review and looking for thoughts, if you have any input.
Okay, cool. Next up, Nimrod, you are also requesting some reviews on the Weaver validation of internal telemetry.
**Nimrod Avni** 20:03 Yeah, there's a couple… This one is kinda smaller in the… scheme of things, just validating, I think, most of our internal telemetry with Weaver. I think you left some comments there, and I think I fixed them since then.
And I think Nicola made it… should merge to main, and the same with the Node.js stuff, there was some more, like… I think there's, like, a lot of stuff still to do in the Node.js to make it perfect, but I want to, like, at least get something there, and I can build it, increment, like, stuff like, getting… making sure we're getting the correct scope, and making sure we're, like, supporting all different, like, JavaScript, like, bundlings, if it's ESM, and what happens if you use stuff like some builders, like ESBuild and stuff like that.
And, so I have some follow-ups I want to do there, but I at least want to get something stable so we can continue building off of it.
**Tyler Yahn (Splunk)** 21:18 Yeah, I agree with you on trying to get something stable. There are… I'm a little hesitant on some of the stuff, where I'm noticing things like this, where it's just, like, there's just… potentially, like, corrupted data is kind of my problem. But, like, yeah, I agree, like, I, like, if we can get something that, like, works, maybe not all the features, like, that's kind of my goal as well, in trying to get something in, but yeah.
**Nimrod Avni** 21:41 Yeah, so I viewed your comment, you were right regarding, really some applications that we were not kind of stepping down, correctly. And, like, I prefer to… as you said, like, try to… like, if it doesn't work on some runtimes right now, it's fine. It's better to not work than to corrupt the user's application.
**Tyler Yahn (Splunk)** 22:04 Right, yeah, 100%.
**Nimrod Avni** 22:05 Yeah, so I'm… that's what I'm going for here.
**Tyler Yahn (Splunk)** 22:08 Cool.
Yeah, I can… I can take another look at this. It's great. I'm, like, super excited about this as well. Don't take my rejections as any indication that I'm not, but, like, yeah, I'm, like, super excited about this, and all the other languages that come from doing things like this. So, yeah, I'm really pumped about this, so… Cool, yeah, it's on my list of things to get done today.
**Nimrod Avni** 22:31 Thank you.
**Tyler Yahn (Splunk)** 22:35 Cool. Alright, well that's the end of the written agenda.
Any other, topics?
folks I'd like to talk about? Maybe other PRs that are sitting there and looking for reviews?
**Nimrod Avni** 22:49 I have something, that I noticed recently, I'm trying to, like, fix it, I'm not sure exactly the root cause of… we have a couple of integration tests of, like, gRPC Relay that keep failing, and I'm trying to dig into why, so if anyone has any lead… I think it's something, from what I'm trying to read in the logs, it's like, some part, like, in the Docker Compose, we're, like, destroying the Compose, but… but sub… like, we don't kill the orphans, like, the sub-processes that were created, and then the ports keep binded. So I'm trying to see… I think that's… at least that's the…
**Mattia** 23:30 I think both me and Mario tried to fix those, so the Compose part that you just said, that one is fixed in my APR, gRPC1.
Also, there was an issue with the resource consumption, I think.
So, there is, something that changes there. Like, there are, the CPUs for QEMO are inherited, or something like that.
That's also in my PR.
And, there was some, health checks, I think, added by Mario.
And, some assertions were made stricter.
I don't remember what else is in there, but I… I don't think it's, flake anymore. I… I hope.
But we should, keep it.
**Mario Macias** 24:25 Yeah, we shall keep.
**Nimrod Avni** 24:28 I'm not sure how, I'm also, like, how close your PR is to merge, because, like, if it probably should be merged, soon.
**Mattia** 24:38 I think it's very close, I just wanted to wait for another review, because… so it happened that there were a couple of reviews from Nikola and Tyler, and then I added an integration test.
which discovered the bug, and the bug led to verifier errors, and I needed to refactor a bunch of stuff, so that's why I need another review.
**Nimrod Avni** 25:02 Okay.
**Tyler Yahn (Splunk)** 25:03 Yeah, I saw your… I saw your comment earlier, by the way. I plan on reviewing that, after the meeting.
**Nimrod Avni** 25:08 Nope.
I'm saying, if maybe, maybe if, oh, I'm hoping it gets merged soon, but maybe if it doesn't, we can just, like, extract the… the… The integration test fixes and merging two mains separately?
**Mario Macias** 25:21 Yes, for what I'm checking, the latest commits into Maine, the CI, It seems the gRPC test that was consistently failing now is passing, at least in the last 2-3 merges in main from the last hour. So, let's hope it's… Already stable enough,
**Nimrod Avni** 25:52 Okay.
**Tyler Yahn (Splunk)** 25:52 Yeah, I'm definitely noticing a bunch of CI failures on PRs I have, but… I haven't dug too deep into their source.
But, yeah, I… Again, I also don't know if they just haven't been rebased, so… maybe it is fixed, like, on main, or… closer to fixed. Mattia's CPR is probably still… Yeah, quite helpful here.
But other than that, Nimrod, yeah, I don't have any input on… the failures there. But thanks for looking into it, because that's definitely something that is, frustrating, is the CI failure, so yeah.
Cool. Alright, any other… Complaints, ideas, investigations?
Well, if not, yeah, we can end the meeting early here.
Yeah, thanks everyone for joining. I will see you all in a week's time.
**Michele Mancioppi (Dash0 Inc.)** 26:54 Wait a minute, I have one last question.
**Tyler Yahn (Splunk)** 26:56 Yeah, sure.
**Michele Mancioppi (Dash0 Inc.)** 26:57 Where are you with the system packages?
**Mario Macias** 27:02 Yes, we haven't, yet started this task. I mean, we are providing… I don't think we are even providing executables.
We will need to… yeah, we will need to integrate the build system with your system packages to get Cignet executables.
But… See, at least personally, since we are focusing on releasing 1.0, I haven't prioritized this.
Excuse me.
**Michele Mancioppi (Dash0 Inc.)** 27:35 So, if you should guess, what timeline can I ask again?
What would that look like?
**Tyler Yahn (Splunk)** 27:42 Well, we have, the 1.0 slated and scheduled For KubeCon. So, I imagine if we're looking at prioritizing things outside of that, it would be after KubeCon.
**Michele Mancioppi (Dash0 Inc.)** 27:54 So we're talking about end of the year, beginning new year?
**Tyler Yahn (Splunk)** 27:57 probably beginning of new year, before we would work on new major projects, but I do also want to say that, like.
Well, we do have executables, Mario, like, we do compile the binary in our releases,
**Mario Macias** 28:09 Okay.
**Tyler Yahn (Splunk)** 28:10 Yeah, I guess, is there an issue around this? That we're tracking it?
**Michele Mancioppi (Dash0 Inc.)** 28:16 I mean, I don't know if there is an issue, and I know we have been talking about this since the unconference in Brussel.
**Mario Macias** 28:23 I think that he's… I think there was an issue, let me look for it.
because I don't remember if it was in this SIG, in the packaging SIG.
**Michele Mancioppi (Dash0 Inc.)** 28:35 And in the packaging-seq, there is, technically, OBI was part of the project scope that… More than one maintainer of this CAIC has agreed upon.
Yeah, I understand that in the scope of WandaToad, it is from the wayside, but… The prototy scope was different.
**Tyler Yahn (Splunk)** 28:59 Just to be clear, though, like, if this is important to you, like, we're happy to accept donations of, like, pull requests.
**Michele Mancioppi (Dash0 Inc.)** 29:06 You're willing to work on it. I would take you up on that if I thought.
Anybody in the packaging SAG would be capable.
Of answering issues that may result from packaging, but alas, that's not the thing.
The, I expect that, for example, those packages will need to do some very interesting checks on the kernel to see if the version is eligible, because there is absolutely nothing that prevents it from installing this from online Xboxes from yesteryear. It will need to depend on BPF tools.
And that is a notorious, notoriously janky… set of packages in, in RPM, Debian, Ubuntu, so, I don't think I would be capable of doing that.
**Mario Macias** 29:52 Yeah, we don't rely on anyBPF tool for installing the executable, no, no.
Yes, they are self… of course, what you need is to… what we will need, is to check that the kernel enables BPF, or the kernel version is bigger than file update, I think is the…
**Michele Mancioppi (Dash0 Inc.)** 30:18 Oh, yeah.
You're in longer support team, 418 and, and above?
**Mario Macias** 30:23 We support 418, but only the version from Red Hat Distributions, because Red Hat ships a 418 version of the kernel that backports theBPF tools that are required.
**Michele Mancioppi (Dash0 Inc.)** 30:45 We'll talk again.
I cannot promise I will, I will go into those packages, but if I have a… some… A couple of spare days, I might.
**Mario Macias** 31:00 Okay, something just to clarify, do you think it's worth Including OB into the hotel packaging, before reaching 1.0.
**Michele Mancioppi (Dash0 Inc.)** 31:15 Yes. I mean, I, I'm not familiar with what you mean in scope 1000, but… Hopefully it works well, and it has been working well since forever.
**Mario Macias** 31:26 Yeah, it works.
**Michele Mancioppi (Dash0 Inc.)** 31:28 Very nicely alongside the injector.
**Mario Macias** 31:30 Yeah, it works.
Works well, but it's subject still to some breaking changes, is the only thing that worries to me.
**Michele Mancioppi (Dash0 Inc.)** 31:38 We are so far away from declaring that the packages are stable. There is absolutely no guarantee of… so the injector We consider it stable. It works really well. All the language SDKs and instrumentations that you inject, it's still something that is best effort without the language SIGs actually supporting that, because they don't support it.
**Mario Macias** 32:02 Okay.
**Michele Mancioppi (Dash0 Inc.)** 32:03 Neither.
**Mario Macias** 32:04 Okay.
**Michele Mancioppi (Dash0 Inc.)** 32:04 Well, honestly, pre-1-0, I would take it.
**Mario Macias** 32:08 Okay, okay, so let me, you know, because precisely today, I'm… this is some internal stuff, but in the goals, in my personal goals for this quarter is releasing packages, or working with Obi and the packages. I'm… next week, I'm going on holidays.
But let's… I'll talk to you in September, and then we can start releasing, or including Ovi, even if it's Ovi not yet stable, but we can…
**Michele Mancioppi (Dash0 Inc.)** 32:40 The, for information, I mean, okay, now, now it's August.
No, not so much, it's gonna happen in August.
We, we published a blog post.
about the packages. I'm talking to the end user, SIG.
this. So, I would love for the first impression of system packages that most people are going to get to have OBI as part of it.
**Mario Macias** 33:06 Okay.
**Tyler Yahn (Splunk)** 33:08 Yeah, I mean, so I don't think anybody on this call thinks otherwise, it's just… there's a limited amount of developer capacity that I don't think is.
**Michele Mancioppi (Dash0 Inc.)** 33:15 I'm getting across here.
**Tyler Yahn (Splunk)** 33:16 Which, like… it's fine, and I'm happy to, like.
have anybody who was willing to come in and help on this project help on the project, but, like.
We are also focused on… Getting a 1.0 out, which requires a lot of, like, developer capacity as well.
**Michele Mancioppi (Dash0 Inc.)** 33:34 Understood.
**Tyler Yahn (Splunk)** 33:36 So yeah, like, I think this is great, and I think it's a great goal, and let's just… let's just make sure that it's prioritized, I think, as we have already prioritized as a group.
**Mario Macias** 33:45 Okay.
**Tyler Yahn (Splunk)** 33:46 I think the first step would be, if we can get it captured… as work that we want to actually accomplish, so an issue, I think, would probably be ideal.
Or some sort of communication that we can turn it into an issue?
Because, like, I haven't seen anything like that.
**Michele Mancioppi (Dash0 Inc.)** 34:02 I'm happy to link you the project proposal that lives in this specification. Give me a second.
**Tyler Yahn (Splunk)** 34:10 Yeah, that'd be great, and then maybe we can take that project proposal and turn it into an issue in this repository to track work for this repository.
**Michele Mancioppi (Dash0 Inc.)** 34:18 Mr. Temperky.
I'll, I'll find it and put it in the, in the channel.
Inc.
**Tyler Yahn (Splunk)** 34:27 That'd be great. Yeah. Perfect.
Okay.
Any other, topics?
Top of mind thoughts on this?
Okay, awesome. Well, if not, we can end the meeting here. Thanks, everyone, for joining. I will see you all, in a week's time, or Mario in a month's time.
Till then.
**Mario Macias** 34:51 Okay.
**Michele Mancioppi (Dash0 Inc.)** 34:52 Aye.
**Giuseppe Ognibene (Coralogix)** 34:54 Everyone.
