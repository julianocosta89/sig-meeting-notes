SIG: Arrow SIG
Date: 2026-04-07
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

drewrelmas 00:02:57 Hey, everyone. It looks like we're still waiting on maybe Josh to… show up. I believe Laurent's not going to be present today.
Oh, hey, I see we have Albert, at least.
Albert Lockett 00:03:16 Hey, yup, I'm here.
Yeah, I'm not sure if Lauren will be here, I think he had a doctor's appointment.
drewrelmas 00:03:23 There we go, I see Josh has joined the room.
jmacdonald 00:03:35 Alright, hello. Look at all these people.
Hello. I will share the.
Albert Lockett 00:03:39 this.
jmacdonald 00:03:40 the notes, and I will go off video, since all of you are as well.
I know that Laurent said he wouldn't be here today, maybe, so if he does, I'll be good, otherwise… No big deal.
And as you know, I always love when we end a meeting early. So, I've looked over the issues, That we have.
I put my favorite one up first.
Looks like we have about a whole page of them, today.
Considering what's new since last week. So… Can you see my screen? Yes, I see you laughing, so you must be.
drewrelmas 00:04:28 Yes, we can.
jmacdonald 00:04:29 All right, cool. So, we'll start here. I'm gonna remind us that our goal is to, like, remove the triage deciding label, And… I think it goes back to about… here?
I think we discussed Gokan's variation on some of the same issues Laurent had filed last week about shutdown. That's making some progress, and we can review the PRs that are open. I think we'll probably get to talking with Gokan about that work.
As well. So I'll start… I guess, here. Anybody in mind? Are we ready?
So, I think we need to do a little bit of work to print the notices. It's a licensing question. We've accepted this library called The Boost.
Software 1.0, you know, the Boost C++ template library.
And it requires an attribution to be printed through a command, and we can just do it. It's pretty easy. I think it's a good first issue.
Does anybody disagree?
Or perhaps object to the Boost software license. I was saying, if we decide later to remove this, whatever library we depend on, we can do so later.
Alright, I think… maybe I talked about that one last week? Anyway, there's two here from Laurent, which are also duplicates of each other, apparently. And this was related to, I guess one of his open PRs, somewhere we asked for something.
Probably… Laurent filed that in response to the PR review. It was number 2466, if you recall, where he introduced a new Control channel thing.
Okay, flaky test, this is… this is the same as mine. The build is always red, but one of the reasons why is, there's some, flakiness in the validation tests. It's not the only place where there is flakiness, unfortunately.
Any comments?
drewrelmas 00:06:47 Nope, I maybe got one of the cases, earlier.
jmacdonald 00:06:53 Yeah, I saw you merged one, thank you, Drew.
So now we're looking at this one that Andres filed. He's, I had asked him to make a note about the problems we were having with keeping our documentation up to date.
It's always been an ambition to, first of all, generate our own documentation, but second of all, to incorporate Weaver, and that's roughly speaking what Laurent said.
And… I have actually started looking into this one myself. It's, not because I need the documentation, but this is part of our internal telemetry metrics story.
So I'll have more to say on that one. If anyone else does, I'm… I'm… Open to it.
Okay, I think I just jumped correctly back to page 1. More about flakiness. This is one that was filed last week, observing it from someone on my team.
Yeah, I don't know what to say. It's timing out at 20 minute, 20 minutes, right?
Here's an example, let's take a look.
Jake Dern 00:08:06 This one might just be the shutdown? Sorry, go ahead.
drewrelmas 00:08:11 Oh, I was just gonna say, with regard to the pipeline performance test, it'd be great if we had CJO or, counterpart from F5.
jmacdonald 00:08:20 Yeah, Chris…
drewrelmas 00:08:21 Excellent.
jmacdonald 00:08:22 Okay, this… this one, yeah.
I should crash.
drewrelmas 00:08:27 Prestige, okay.
jmacdonald 00:08:28 quit.
drewrelmas 00:08:29 CJO merged some PR that was supposed to let some, like, benchmark… most benchmarks pass and not crash if one of them fails, but I'm not sure if this is before or after.
Jake Dern 00:08:42 Yeah, there's… there's, like, this shutdown endpoint on the collector, and if it doesn't, like, if that times out at, like, 60 seconds, then it returns a gate, like, a 403. And then, yeah, the.
drewrelmas 00:08:54 Oh, there's an open PR that would fix this. Correct.
Jake Dern 00:09:00 I think that's why that one's failing.
kennedybushnell 00:09:02 Yep.
jmacdonald 00:09:02 Okay, and so far, I've done poorly at updating the triaging label. This one has been accepted. What we ideally would see is a PR linked here, but we can fix that later.
Otherwise, it will not get closed.
Okay, so… Lauett opened one about, startup ergonomics. I know this has to do with embedding our library as, part of another agent, or, sorry, I should say collector.
I don't know that there's anything too important. There was already a PR merged.
or it's… it's actually open, and I… one of the problems we're going to discuss is how the build is very red, and so it's hard to get stuff merged right now. So Loud's PR is not actually merged.
We found, in that PR, I asked Lauett to create a new issue that It's actually… sorry, this is in a different PR. There was one open for one of our exporters that added a bunch of new metrics, and my remark was that this was, like, common functionality in the Go codebase, the collector, we call that an exporter helper. You can imagine both receivers and exporters having some sort of Helper to generate the sort of standard metrics for all the things that exporters and receivers do.
So, here we have it.
As far as I know, no one's actually working on that, but you can see… the associated code that Lauett added here, and you can imagine putting that sort of into the pipeline, maybe.
Triage. Well, I accept, since I asked for it.
And what do I… what do I do?
It's accepted.
And then maybe someone will come and work on that, not sure.
Alright, let's go quickly here. Josh.
Flaky tests for co-pilot, I don't… okay.
Good luck with that.
We have been trying to assign things to Copilot. It's not been super successful, also because of the build being red all the time.
Okay.
Well, someone's gonna have to read that. Lowett, since he opened it, can say more. I don't think Lowett's here on the call with us.
Unless I'm wrong about that. Now I can see everybody. Yeah, okay. So, we're not gonna go deeper on that one. Thank you for the AI assists, if they work.
Meter names should not need the word metrics in it. I fully agree. Thank you, CJO.
Yeah, we should try and be, concise and avoid repetition and stutter.
Although I don't remember the specific issue… here it was, Drew. Oh, right, oh, right, oh, right.
drewrelmas 00:12:06 Yeah, it's related to this.
jmacdonald 00:12:08 Okay, so we added some support for the OTEL SDK view configuration.
Also been looking into that.
Okay… and then we were something like, split tests into multiple units. I think this was me saying that our tests are so big that half the time they time out. This has been noticed for the ARM platform as well as the macOS platform.
So it's one of the reasons why our build is always red.
I'd like to.
drewrelmas 00:12:39 I had help wanted on that one, Josh.
jmacdonald 00:12:41 Oh, yes. Help wanted.
drewrelmas 00:12:44 Okay, I got it. Don't worry about it.
jmacdonald 00:12:46 Okay, you did it. Alright, thank you.
Okay, so Aaron has filed one about… something, something, something. It's complicated, and I know that the PR that was open was put back into draft.
You have a few words, Aaron?
Aaron Marten 00:13:07 Yeah, this was… this was something that came out of a attempt that I had made to link OTAP data flow in with an internal C++ application, for Windows specifically, and was hitting all sorts of issues, and this seemed to be the… the simplest solution, was to just go to linking against a platform native TLS backend. But we currently have, requests crate, which requires you to select a crypto provider, of the three listed there. So this was gonna add an additional Ability to… to do that.
excuse me, to use… to use none of the above, but just to use native TLS, right? Part of the problem with that is there's also this, that was discussed in the PR a little bit, is there's also this experimental TLS feature flag we have, which is to enable I think Lalit had a comment further down, which was to enable MTLS, for, like, the admin and server listeners, whereas I was mostly looking at the… the outbound request.
outbound requests. So anyway.
There's some more kind of work and exploration that needs to be done here, and I kind of put this one on pause because I was taking a look at a more, more serious issue.
jmacdonald 00:14:30 Got it.
Aaron Marten 00:14:31 Unreal. True.
drewrelmas 00:14:33 Yeah, I was just gonna make a note that I think long-term, we want to get rid of the experimental TLS feature. It should just be native without an extra feature in the compilation. So, if you're thinking more in those lines, maybe at the same time, we could take out the feature. I think that's the plan while you've had, For a long time.
Aaron Marten 00:14:56 Okay.
Yeah, I can sync up with Molly about what we want to go forward with here, so…
jmacdonald 00:15:01 Does it make sense to support both native TLS and… the… Rust TLS implementation.
Like, it's a… it's like either-or, as opposed to a two-different feature matrix.
That's my question. We could… Take that to another location.
Aaron Marten 00:15:29 Yeah, I don't have a great answer right away. I would defer, probably, to Lala and others that have spent more time in this space.
jmacdonald 00:15:34 I barely know what I'm asking, but I know that, last time we faced this, we tried to switch from the Rust native to the Rust TLS, and there's a lot of changes that are needed for that. It's not as clear and obvious as it… as I would like it to be, but, We can sort that out.
Okay, Let's see, CJ's had some fake generator improvements. I think Tom has also been helping on that front.
Talking about more different point types, especially in metrics. Anybody have comments?
Go read the issue.
Cj has also been making improvements on… Saturation test measurement, benchmark, new benchmark, and so on.
I don't see CJ on the call. Lalit has joined us, Anybody who'd like to comment on previous issues we've rolled through already is welcome to raise their hand.
Gosh, it seems like this page is growing every time I look at it. We're up to durable buffer retry metadata. I think this may be the one that you're looking at, Aaron.
Aaron Marten 00:16:48 No, this is… this is actually a follow-up, on Laurent's PR.
jmacdonald 00:16:57 Oh, correct. He… oh… okay.
the PR, which is, about wake-up handling.
Aaron Marten 00:17:07 Yes.
jmacdonald 00:17:07 Okay, good. Well, we can maybe look at the open PRs.
Aaron Marten 00:17:12 This one…
jmacdonald 00:17:13 124.70.
Aaron Marten 00:17:15 This one we should address, but the title, I think, is scarier than the actual issue.
jmacdonald 00:17:19 Okay.
Aaron Marten 00:17:21 similar details.
jmacdonald 00:17:22 Okay, good. Well, thank you for the detailed note.
Sweet.
Okay, we're almost up to where we can see it on one screen of mine, but not quite. Node processor pros… nodekind processor chain, I know Drew's got a PR open about that. Maybe we should discuss that right now.
drewrelmas 00:17:45 door. It… I mean, it should be linked in the issue. It's still… I moved it back to draft because I wasn't fully… satisfied with the benchmarking. I wasn't sure if it was a true comparison, but the motivation for this is implementing processor chain, which has been in the repo for a long time as a node kind, but was, unimplemented. It would cause an error if you try to use it.
The use case that I'm bringing to it is a customer wanting to… or a user of DF Engine wanting to report, an aggregated metric, for… to represent, for example, the duration of a single logical operation that might involve multiple discrete, processors. So.
I wrote up the issue, took a stab at it in the PR, but… I briefly mentioned it to Laurent offline, I think we're aligned on what it should look like. You can see telemetry output there. Essentially, it would… keep reporting individual metrics from individual processors, but give us the option to… I mean, it also reports a chain metric, which is greater than or equal to the sum of… the internals.
Josh, I know you had mentioned offline, you have a… maybe a question here about wall clock time versus CPU time.
So maybe we can… take that offline. I don't think we need to get into it here.
jmacdonald 00:19:21 Yeah.
I'm aware of… why Laurent wanted this in the first place, it had to do with, I guess the CPU efficiency of fusing together the CPU or the compute work of processing a single request, rather than always going through a channel.
drewrelmas 00:19:42 So yeah, that's exactly it, and the reason this PR is draft right now is if you look at the performance section, my testing, like, when you have some non-trivial work?
They're pretty much equivalent.
Between chain and regular processors with channels, but.
jmacdonald 00:20:03 Right.
drewrelmas 00:20:04 The testing I'm doing shows there's actually overhead if you have, like, a very small amount of simulated work, but I'm still working on the benchmarks. I'm not certain if these are valid numbers yet, so I moved it back to draft.
jmacdonald 00:20:18 Gotcha.
I also imagine there are other ways we could, manipulate metrics or aggregate what you're looking for to aggregate, but that might be a separate topic. I know that this was… when Laurent sort of conceived that idea, it was an optimization.
Cool.
Oh, alright. Well then, heading back, I know we're almost onto the one-page limit, that's good.
Trying to get this done.
allow it has been looking at factoring the library apart so that you can install it in another process, sort of related to what Aaron was saying.
And… We have here… A need to separate configuration, and this has not been done, separate configuration, so that you can configure your main function, essentially, from another process.
I would say, accept, does anybody have a problem with that?
Very good. Okay, thank you. Trying to move quickly… Good job filing new issues, everybody.
We are, arriving now on one that Chanley, has been working on.
And this covers… Sort of a portion of a larger workflow that is about propagating contacts through the engine.
Chanley, would you like to describe any of your current work or this issue?
Chanly Ly 00:22:06 Yeah, so basically what I've been working on was, just adding the infrastructure for… basically, like, when we have receivers, we define, like, a policy to extract headers from, let's say, gRPC or Kafka.
And then we could store those headers into the, context of DLTAFP data.
So this is just an extension of that, so, the exporters can actually take those headers and send them out wherever they need to go.
jmacdonald 00:22:35 And you have an open PR about that, just to kind of tie this all together.
Chanly Ly 00:22:41 Yeah.
2585.
jmacdonald 00:22:46 Sorry, there it is.
And this, I've looked at, pretty, pretty simple little PR, actually. Once you factor them into smaller units, you end up with something like this.
You end up having this metadata map Be propagated, and then there's some logic to take in… sorry, to send out the new, metadata here.
Very good. Thank you, Chen Lee.
Okay, I'm on the wrong page. We're working our way through these issues, Thank you, Albert. Okay, oh, this is going to be fun. We should talk about protocol buffers and the never-ending conversation about whether they are defaulted or present or not.
It's a well-written issue covering, some inconsistency.
And we've been discussing it throughout the day.
Udkarsh, would you like to speak?
Utkarsh 00:23:58 Sure, yeah, so… We have these views, which we… wanted to use as an abstraction, so that the processors don't have to worry about the actual OTAP data type. Now, we have multiple implementations of these views for OTLP protobytes and for arrow records, but there's some inconsistency in how we implement these views, so… Especially for things like severity number, which is… Not optional from a proto… protobuf specification standpoint, but… It was just marked optional in the comments.
We have this discrepancy in whether If a CVT number is missing, should you emit it as… Sum as a zero severity number, or should you emit it as none?
And that's where the discrepancy is, and we have that with, like, flags and time, Unix, nano, and other things as well.
So, semantically, and, like, functionally, it's not too much of a problem, because most of our receivers, I think they do the right… at least the receiver side of, data do the right thing.
But still, I think it's good to be consistent, at least in our… View implementations.
So, we should either just do none if it's missing or not present, or make it sum of zero, and we shouldn't be having a mix of both.
yeah.
jmacdonald 00:25:38 Thank you. I agree. I also remember there were some test helpers that have equivalence checking, and some of those equivalence checkers have a few special cases that are essentially hand-coded to recognize these weird cases, and actually let tests pass, where maybe we could actually fix the underlying problem.
There as well.
Alright.
Good issues. Oh, we should, we should remove the label. There we are.
Thank you.
Accepted. Okay, so many new issues.
I think we're now legitimately onto the one-page mark.
aaron has filed an issue about… UX key in a dictionary.
Aaron Marten 00:26:27 This one is related to the PR from this morning. It's a follow-up item.
Got it. Essentially, we ended up So we're doing this unit… dictionary unification handling.
And what we did is, down at the Quiver layer, we hard-coded the widening to stop at UINT16, because OTAP does not consider anything above that to be valid. Hypothetically, Quiver could handle more than that, but we kind of hard-coded that as a limit, so that's just a follow-up item, too.
Consider handling you know, doing widing beyond Uint 16, and then also, you know, making that limit configurable.
Now, the number of times we would need to widen beyond Uint 16 is probably vanishingly small, but…
jmacdonald 00:27:22 Yeah, I know that, in the past, this has been brought up as a potential, like, compatibility concern. We say, even in my README PR, I say we're 100% compatible with OTLP, but you produce an OTLP message that has more than 16 bits worth of metric data point, you might have an error converting those points.
So I've seen this before, in other sort of aspects. Anybody have comments on this?
Jake Dern 00:27:54 Only that… what you just said, about… potentially not being able to convert from a valid OTLP message, yeah, I've also run into this in a couple places, particularly in the temporal reaggregation processor. We have to just reject the batch, because we can't represent it.
jmacdonald 00:28:12 Hmm Jake, would you support widening OTAP to a U32?
Jake Dern 00:28:20 That sounds like a lot of work.
jmacdonald 00:28:24 Okay.
Jake Dern 00:28:25 I think…
jmacdonald 00:28:27 Possibly, it's better just to let the batch processor put a limit.
If you can.
Like, split the thing before.
Jake Dern 00:28:35 That's something too big.
jmacdonald 00:28:38 It's a legitimate answer, in my opinion.
All right, so that was a good follow-up. Thank you, Erin.
The next 3R.
drewrelmas 00:28:48 related to processor chain, they're, like, follow-up items I don't think we need to get into.
jmacdonald 00:28:54 Right now. Okay, feature requests for the new processor chain thing.
drewrelmas 00:28:58 Yep.
jmacdonald 00:28:59 Albert does a good job recording his work. Opl is coming along, you want to say anything?
Albert Lockett 00:29:07 Yeah, so this one is just, to support some functionality on, strings, so concatenating strings together, concatenating strings delimiter, and replacing, substring… Being able to get the value of a regex capture group as the result of an expression, so that work is, Is in progress. Yeah, I see you, Josh, you've highlighted content.
jmacdonald 00:29:33 WS.
Albert Lockett 00:29:35 I, so that's what the underlying function that we would use to From Data Fusion for string, concat with delimiter. They have a function that implements that, that we're gonna reuse for this called concat underscore WS.
again, when we parse from KQL, we would use the stringcatDLIM function, and for OPL, I decided to make, a function called join, a alias for concat underscore WS. I think that concat w under… WS, might have originally meant concat with white space, although you can use any delimiter, and it is something that I think comes from SQL, effectively.
jmacdonald 00:30:25 Cool.
Alright.
Very cool to see, OPL evolving.
Let's see… Okay, so more on processor chain. Thank you, Drew, for…
drewrelmas 00:30:38 That's me.
jmacdonald 00:30:39 Gives you many small PRs ahead, I'm glad to see it.
This looks exciting. I haven't read it.
And, let's see. So, it looks like we're able to panic something somewhere.
Albert Lockett 00:30:55 I read this one briefly, I think I can speak to it.
jmacdonald 00:30:59 Thank you.
Albert Lockett 00:31:00 I think the idea here is that, if you were to try to, like, use, some of the types from, the OTAP data flow crate, specifically, I think, a node user config.
If you tried to use this, CRD method, which I'm not sure what it does. I think it might produce, like, the OpenAPI spec for, for, like, creating and installing a Kube custom resource definition, it will fail if you have your enums, Structured in some kind of, in some kind of way where, like, some of them have… some of the variants have underlying data and some of them don't.
Anyway, I think, like.
pretty sure that the… well, at least I thought, based on the description, that the… the, all we had to do was add some kind of, annotation to, the field that was causing the issue on node user config. In fact, we have already added that for the config, field, which is a SIRTI value.
But then, it looks like… maybe that's not all there is to do. I see that Chris just opened a PR.
draft PR about, 20 minutes ago that has some other, changes, that, that, that might help with this.
But I haven't read the PR yet, so I can't speak to it.
jmacdonald 00:32:38 Got it.
Albert Lockett 00:32:38 All that effectively.
jmacdonald 00:32:41 I gotta admit, I do not really understand what the JSON schema-derived world does, and I'm afraid to know, almost.
It sounds pretty scary, but, that's… that's the nature of… I mean, SERTA protocol buffers.
Same, same.
Okay, okay, we're almost there now. Chanley, put this, and there's a PR about this right now, so, maybe it should say… I think I updated the PR description, actually, so there.
Here it is. Thank you very much. That's gonna add an arc.
Around, the newly added context for transporting headers from gRPC and HTTP that we were discussing earlier.
I asked for a slight refactoring in one of Laurent's large PRs. He's added a heap inside of a node local scheduler. I love heaps, but I want to see them in their own data file, or own code file.
So, there's my request.
We have a few uses of binary heap in the codebase, which is a standard Rust library. However, it does not give you the indexed feature. If you're a Go programmer, you might be used to that by now, so Go's heap program lets you do indexing.
But it's hard to use, if you're… if you're familiar with that.
I love heaps. Okay, so here's mine. The build is always red. I'm so tired of it. I put the screenshot. I… one of the things I try to do for the project is to review a lot of PRs and merge them as fast as I can reasonably do so. This is just like hitting… these two make it hard to see when you can merge a PR for one thing.
I will say that the pipeline perf, pre-merge is probably, like, important to fix, and the codecove thing is just, like, I don't even understand why it's broken.
If anyone figures that out.
drewrelmas 00:34:48 I left a note, that, I'll take a look at CodeCub again, I was the one that configured it to begin with.
jmacdonald 00:34:54 Yeah, something's not quite right.
And there were some items that we filed… I know, Drew, you know this, but items about the flakiness of coverage in the Go codebase, and maybe we're going to remove some of that.
I don't know.
Cool.
Almost there. Config structs just seems related to, the one down on 2582.
I had to guess, 10 apart.
Okay, we're just gonna run through it here.
Anybody, anybody?
Tom.
Tom Tan 00:35:33 Could we also take a quick look on the issues, which was just marked as stale in the last 7 days? I think there were… there are 8 of them, maybe we can take a look at them quickly and decide whether We should have removed still.
jmacdonald 00:35:49 I see. Thank you, that's a good point.
Tom Tan 00:35:53 I'll send a link, yeah.
jmacdonald 00:35:55 Thank you.
Tom Tan 00:35:56 for our link.
jmacdonald 00:35:58 I will find that link.
drewrelmas 00:36:03 Oh, we have 37 marked as stale.
jmacdonald 00:36:06 Oh my god.
drewrelmas 00:36:11 Oh, okay, these are new.
jmacdonald 00:36:12 It's 8. Okay.
Yeah, that's good, that's good, that's good. As I look at.
drewrelmas 00:36:24 We have a metric set for syslog Ceph, right?
jmacdonald 00:36:27 I know that these first two I'm looking at have… had… have been largely addressed.
I don't know specifically, it'd be worth asking Chris. I think I see… I thought Chris maybe came in and out of the… of the meeting here, but… They're pretty old, and I would be willing to let them go stale, and… Auto Close… Since they're all so old at this point.
I think this one has been done.
I think this one has been done.
And this one has been ongoing, but, here we are.
So, at the very least, I'm… Completed.
Cool.
drewrelmas 00:37:41 Is this just no TLP exporter, which we…
jmacdonald 00:37:43 Yeah, we have this. I mean, like, I don't know if we have… the example.
drewrelmas 00:37:48 Fig, but…
jmacdonald 00:37:49 exact config. I'm gonna say we do it.
kennedybushnell 00:37:51 Yeah, leave that open. I'm gonna have somebody work on the OTLP exporter this… over the next couple months, so I'll probably have.
jmacdonald 00:37:58 Okay.
kennedybushnell 00:37:59 Tackled by them.
jmacdonald 00:38:00 Thank you, Kennedy.
Yeah, there's some features here, you know, in the Go Collector world.
These two, especially, are parts of the… exporter helper, you get those for free. And, we've argued in this project that you can get much of the same functionality from a processor because we have the zero copy properties. So, like, why not use the retry processor as one of the questions that comes up.
And then sending queue is effectively an in-memory queue. We have one of those for each, but… But the Keep Alive stuff, I'd like to know if we have it, if we have all the compression support that we need, and so on. Thank you, Kennedy. Okay.
So, leave that one open. I'm gonna remove the stale, sorry, thank you.
And now we should have 2 left.
Albert Lockett 00:38:56 Yeah, 12.09, you can close, That was, when we were going from OTAP to… or OTLP to OTAP, we were using more CPU than going round-trip OTLP, OTAP, OTLP.
And… we were trying to figure out why, and we have since discovered why. It was the transport-optimized encoding, which we've optimized, and now it's, not weird anymore.
jmacdonald 00:39:24 Got it. And does anyone know about this one here, the OTLP exporter?
I'll say we should leave it open.
Okay, I would like us to, well, returning to our notes…
kennedybushnell 00:39:43 Do we… Do we expect those to be the same?
It seems like they're expecting OTAP and OTLP bytes out to be the same in their different formats.
Wouldn't… isn't it reasonable that they're different?
jmacdonald 00:39:57 Yeah, that's a very good point. I agree. I don't think I expect them to be the same, and since these lines are flat, I don't see a change. You'd expect this type of issue to be about a change.
Albert Lockett 00:40:09 that the, like, we generate basically the same data, and then, like, in one case, it comes in as OTLP, in the other case, it comes as OTAP, but they both go as OTLP, but we have a different volume of data.
jmacdonald 00:40:24 Hmm.
But that's… That can be explained by different, sorting orders and… compression factors, I think.
Possibly.
Oh, this isn't gonna help. I was gonna find… A link to our current results, so we could look at new But I forget the URL every single time.
And this… Apologize, people.
I won't look for that right now. Can we now, come back to our notes?
we have done a fairly good job of the triage labels, and Drew has put together, An agenda item we may have covered already.
drewrelmas 00:41:21 Yeah, I think… I think we largely covered it. I think the PR is still under construction. I don't know if we need to present it, here.
jmacdonald 00:41:30 Thank you. Yeah, I peeked at it, it looked, like the right approach.
drewrelmas 00:41:35 I really want… my big thing is I really want to understand Or why, I see the performance overhead using chain instead of… Individual processors, because theoretically, we're cutting out some middle work.
jmacdonald 00:41:57 Right.
This is a good opportunity to try out the new profiling instructions, which, like everything else, We're having trouble merging, I wouldn't mind saying something about this for a minute. If you have an open PR and you're wondering why it's not merging, but you look at the bottom and it has Stuff like this, especially Clippy.
format, we need you to come back and do something. And a lot of them are in this state right now. Across the board, it's not any one person, so… These are having trouble merging for that reason, and so are a bunch. If you notice, they're… they're all… they're all red. There's nothing green here. Oh, except at the bottom, which… it's a draft, I don't quite know why.
But I love it when we get, a shorter list of PRs, so if you can help Please try to get them green, and we'll take a look at the… Code Cove problem.
I have one agenda item, which I will put up, and I, well… I was looking at who's on the call, And… I, see, Goken, that you're here.
And I wonder if we could use, the rest of the meeting time, or most of it at least, to talk about your two open PRs. I'm looking for more reviewers on these in addition to wanting to talk about them.
So let's see.
We have the two of them, and they are… Here… We have two approvals, thanks to Lalit for going through in depth, here. Looks like Tom has been doing some work as well on it.
This is our second document on extensions. This is sort of the how version. Laurent had done one with the what and why type of requirements. So, Please take a look.
And Gokan, if you would like to say anything, or you're aware of any kind of interesting topics to discuss right now, that'd be a good time… now would be a good time to talk about it.
Gokhan Uslu 00:44:17 Nothing particular, but if there are any questions, or anyone who wants to discuss the… Changes, like, it's slight differences to the original requirements document that… this approaches, I think that would be a good time. Otherwise… everything is pretty much explained in that pupil request, I think.
jmacdonald 00:44:43 Thank you. Yeah, I didn't see any major departures, more of a sort of stylization approach that you've applied, to try and sort of I don't know, make things, you know, at right angles, and so on. So, my position here is that this looks as good as it can get without actually seeing code. We probably have not much more to debate here, and that's why… while I recommend people reviewing that document, I think if there's anything kind of at a deeper level, we're probably going to not notice it until we get to the code, and then it'll be unclear. So I'm okay merging that PR, for myself, and I'd like at least, someone from the F5 side to give it a look.
And then, also just sort of, like, giving us a tour of Gokan's work, here, because it does need more eyeballs. This here is a PR, which is, PR number one, from the design that we just looked at, and, I thought I would kind of show you a little bit of what it looks like. So, this is the capabilities section that Laurent had proposed in his requirements document, which covers configuration. So this would be a basic configuration for an extension.
Where the name of the extension is Sample KVStore, the URN is… Sample shared key value store.
Although I think we might be able to shorten this a little bit. And then, as far as down in the nodes section, where we'd put our ordinary components or nodes, we now have a capabilities listing, which gives you a mapping from key to value. The key is a capability ID, so this is a well-known label.
applied to what it is. So, this is a key value store, that's its capability name. And then you name your node. So, sample KV store refers to sample KVStore.
And this was, roughly speaking, the configuration model that Laurent had proposed.
So… Yeah, that's a pretty small standalone little PR. It doesn't get anywhere near some of the stuff, which I think will be a little bit more intensive for review, about extensions. And if anyone has comments or would like to talk, GoCan especially, please.
Gokhan Uslu 00:47:14 Yeah, and always feel free to reach out on Slack or wherever.
jmacdonald 00:47:19 Yeah, I think this looks good, everybody. So, a few more reviews would be nice.
And thank you.
Well, that didn't take as long as I thought it would.
We just need reviews.
We'll put in the notes.
Please review… also, I think it was 2510.
Yup.
Also, 2510, thank you, thank you, thank you.
All right, well, now that we've arrived at almost the last part of the hour, I thought I'd ask if anybody here has a topic they want to add or bring up right now.
I do have one, but I'd like to let other people talk.
kennedybushnell 00:48:11 I have what's probably just a quick question about… kind of the expectation with pull requests without issues, so… I've done a couple of, like, perf fixes. Do we… is the right way to go about doing that to create an issue first and then link against it, or are those fine without?
jmacdonald 00:48:32 In my opinion, it's fine.
when you're making a change that's really, like, modifying behavior, it's really good to have a kind of trail of issue to discuss, but there's not… I don't think it's reasonable to expect every change. Would anyone else disagree with that?
drewrelmas 00:48:54 I don't. I think it makes sense, especially when we talk about doing things for leaky tests, or keeping the CIA passing.
Performance is another aspect, unless… The performance improvement impacts the capability that… such that a downstream consumer might notice.
I don't think I would expect an issue for everything.
jmacdonald 00:49:24 I guess the answer is use your judgments.
I'm certainly happy to approve many a PR without an issue, but it's nice if you're doing something that might raise questions to put the issue out.
I mentioned I have one. We actually saw it a second ago, and I… Thought I'd, while we're here, mention that it's sort of been… this is, like, not new, in OpenTelemetry. This was… debated for more than a year and merged about a year ago. So, it's sort of 2 years old in OpenTelemetry. It introduces… I'll show you the protocol change, it's really simple. It's part of a type called Entity Ref, it's in the common protocol namespace.
It has four keys, and schema URL, if you're familiar with that field, it's, like, kind of littered across a bunch of different types. It's kind of deprecated in those places where you see it today, but it does live on in this location.
So, entities should have schemas, and a URL lets you find them.
There's a type, name, and then the big idea here is that we're separating the attributes into those that we consider identifying and those that we consider merely descriptive.
The names are sort of… Yeah, they're not ideal. We've debated that as well, but here they are. So, ID keys and description keys are what we're labeling them. So, in your entity definition, you will say.
which… Entities are descriptive, which entity sets, are descriptive or which are not.
And this… sorry, I didn't say that very well. I did link in the issue to, some documents that you can use to make more sense of what I just said. These entity refs go in the resource, and this lets you declare, in a kind of backwards compatible way.
What you are… The identifiable Entities within your telemetry.
The reason I filed that, and this is sort of related, is that I… I've been looking into internal metrics SDKs for ourselves. We have a desire to have an internal metric pipeline that's not derived from the OTEL SDK, and as part of getting there, I've been looking at how to generate OTAP kind of directly from instrumentation.
And what I find currently is that since we don't have multivariate metrics, it's leaning… it's pushing me towards, using scopes as the place where your attributes go. And there has been a discussion in OpenTelemetry about scope entities as well, which would be, potentially a way for us to, store less data.
It's an open question, but for now, the resource model has been accepted, so… Users are gonna ask for this eventually, and we should be ready. It's… I think the longer we wait, the harder it gets.
Does that sound reasonable to anybody?
Albert Lockett 00:52:49 Sounds reasonable.
jmacdonald 00:52:51 Cool. Well, I hope to follow up on that myself as well. I think it was not exactly clear what we get from this, but, It is, definitely forward progress, and follow the issue, or click some of those links, and you can learn more.
All right, well, unless anyone has another thing to say.
lalitb 00:53:13 Hmm.
jmacdonald 00:53:14 Alice Hand, hello.
lalitb 00:53:15 Hey, yeah, I had one issue, probably just wanted to quickly discuss. I just pasted that in the chat.
If you could.
jmacdonald 00:53:25 Alright, let me, pull it back up.
Filing issues as fast as they come.
lalitb 00:53:40 Yeah.
I think I raised that this probably last month, and probably I didn't join the meeting, so it… if it was discussed, I mean, I would not have… probably attended that meeting, but… but yeah, just to summarize right now, I do see some… you know, we have a batch processor, and we have a durable buffer. And I do see some issue, or at least… There is not a clarity how we should be ordering these Processors, if we are going to use them in a pipeline.
In ideal scenario, the durable buffer should be very early in the pipeline, because we don't want data to be lost, so that should be something coming very early, but then… If we have durable buffer as the first entity, So, durable Buffer also has a retry.
It will also have a retry, like.
It also supports retry, but then that means that we have first durable buffer, and then the batch.
But… This, again, means that we are going to do a retry or not… On the exact batch.
every time we are going to retry a different event in a different set of batches, which is not the right approach, again, to do it. So, probably some clarity we need, either in a documentation, or maybe some other way that… If we are going to use a durable buffer and the batch processor, how should we be ordering them… Or… what should be the proper way of doing it?
I, I saw… I was just trying to see how GoCollector does. I see that now GoCollector is… Probably has this similar issue, and they are deprecating the batch processor, and they have a… probably some helper which does persistence, retry, and also the batching. So they kind of get rid of that.
By having a single entity which does all these operations.
So… so just, just, probably just wanted to bring this issue, I mean, if probably some people can go through this and comment, on what do you think what should be the right approach. Not looking for any answers right now.
jmacdonald 00:56:00 Thank you.
This is a topic that I talk about way too much.
And I would invite anyone else who has a comment to speak first.
See a thumbs up.
Oh my god.
Gokhan Uslu 00:56:16 I mean, I would say, I don't… I just… the first thing that came to my mind was that Should that be something as a processor, then? Because it makes a lot of sense.
like, I guess durable buffer can be a processor, but what I'm talking about is, if what we want to have is to accept a request.
And then say to the client, hey, I got the request.
And if the… and by that time, it is already probably persisted if someone switched the button saying that.
I want some persistence.
just think about any kind of persistence. So, like, it would be maybe, like, a receiver-related concern, but not written into the receiver, it's just an, you know, engine solves it based on a switch that you enable. What it ensures is that receivers, instead of saying that, okay, I got the request, or if ACNAC is not enabled, for example, then it could say, okay, I persisted it.
And then I return, you know, okay, something like that.
lalitb 00:57:37 So, Dualbot buffer is already a processor, right, Gokhan?
When you're talking about durable buffer here, it's already a processor.
Gokhan Uslu 00:57:44 No, I was, I was talking about if, like, persistence of, persistence of the receipt messages.
lalitb 00:57:51 Yep.
Gokhan Uslu 00:57:52 Probably would be, like, some… a post-receiver preprocessor concern, kind of, like, in the middle.
lalitb 00:58:00 Okay, go to the deal.
Gokhan Uslu 00:58:01 That engine can, you know, like.
lalitb 00:58:04 Yeah, got it, yeah.
Gokhan Uslu 00:58:05 based on a switch that you provide. It wouldn't be like a drawable buffer, because a drawable buffer maybe can, you know, it can persist whatever you give it to it, but that creates the problem that you're talking about.
I don't know, yeah.
jmacdonald 00:58:24 I, I will say that… that I can add some issues to this that will fill in more that I have… than I can say in the next 2 minutes. You referred to a very complicated topic in the Go Collector, and they've moved a lot of their functionality into this thing called the Exporter Helper, but they've very intentionally put the queue before the batcher.
And so that the batcher is expected to pull from the queue, but then we had to go back and sort of backfill a bunch of functionality on top of that, which… to allow you to wait for a non-durable buffer, so… or a non-durable queue, which is really about passing X and X through a batcher.
So all of it got really complicated, and we've been trying to clean up essentially the mess in the Go Collector for a couple of years now. So I'm part of the problem, or I'm part of the solution, I don't know, both.
There are a bunch of issues that I've created that are saying, we have to decide, we have to decide, and finally I realized that nobody's going to decide except maybe me. So, we have now found an issue about Like, finally deprecating the batch processor, because it… doesn't have, proper error propagation, and you're meant to use the exporter helper, but there's, like, masses of people still using it, and so it's hard to change. We should write a doc… my opinion here, Lalit, thank you, is we should write a document that explains all the options, that they all have reasonable, or that they're all reasonable, and that they all have good outcomes, and that they have different properties. That would be a good document.
So I will definitely accept.
All right, thumbs up, we're at the hour. Thank you all. Next time I'll see you, it'll be, Thursday.
next week.
Thank you all.
lalitb 01:00:25 And goop.
