SIG: Go SIG
Date: 2026-07-30
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 01:22 Hey, how's it going?
**David Ashpole (Google LLC)** 01:24 Doing well. Pretty…
**Tyler** 01:26 You think we…
**David Ashpole (Google LLC)** 01:27 Okay.
**Tyler** 01:29 Yeah, looks like it. Awesome.
Well, cool.
We could probably jump in here in just a second, then. If you haven't yet, please go ahead and add your name to the attendees list.
If you have agenda items you wanted to talk about, please go ahead and add them there as well, and I will… Start sharing my screen in just a second.
Cool. Okay.
Awesome. Welcome, everybody.
So, I wanted to start us off by talking about the next release. We're… let's just say overdue for it. I think it's all set, actually. There's only two PRs that are still open that are in the, milestone that have been added kind of recently. This one is from Robert that is preventing process calls from, after provider shutdown.
I don't think it's strictly required, but I wanted to ask, David if you wanted to take another look at this before we did the release. It's not, like, super critical.
**David Ashpole (Google LLC)** 02:49 I had one outstanding comment.
**Tyler** 02:51 Oh, okay, cool. So, yeah, if that's the case, then, oh yeah, you're right. Yeah, sorry, I forgot about that. Let's just pull this into the next… Milestone.
This one… It… Needs another review.
I thought I might have saw Sam on the call.
Yeah, Sam's on the call. Sam, if you have time, could you get this reviewed, within the next few hours?
**Sam Xie** 03:22 Sure.
**Tyler** 03:23 Okay. If you approve, I'm not forcing you to say approval or anything, but if you approve, then let's keep this in the, the milestone.
But yeah, other than that, I don't think there's anything, there's nothing contrived, I just merged the last, PR that was there.
So, I think that this should be ready to go. I'll try to get out the, release this afternoon.
for 145.
Unless there's anything else that's missing that people wanted to get in, prior to… release.
Cool. Well, if not, then, let's keep going on the agenda. So, Puneet, you wanted to talk about finalizing GPRC status mapping? Yes.
**Puneet Singh** 04:11 Yeah, so I think this is, this was previously discussed, and it's kind of already in progress, so, because the spec allows for this thing, I just wanted to bring it up for, you know, that what are the options, and… among those, what we already have it going, and I think there's a kind of approval for option 3.
Because I want to also bring it up at the spec level, that this is something that is being introduced at Go. So, just wanted to get a consensus on this. If we are fine with 3, then I'm… I don't have any issues with that, so…
**Tyler** 04:56 Yeah, walk me through this one again, so…
**Puneet Singh** 05:03 Oh, I thought this…
**Tyler** 05:03 What's funny.
**Puneet Singh** 05:04 Yeah, so yeah, I think you've already reviewed this PR, I think David also had a look, but this is about, the user requesting to treat some, methods, inside gRPC with, I'm sorry, not the method, but the error code has non-error codes that, to reclassify some of the error codes. And the spec actually allows that, the spec language itself.
hope is that, you can override the… the… you can classify the error codes at non-error codes, if the… if there is override option available at the SDK level. So the language does open… allows to open that interface, for… for this, gRPC itself, so… So, so yeah, I think, we opened with, first PR, which was… About introducing a callback.
Which was, like, very open, because it allows, execution of a user-provided function on the hot path. This was the first approach.
I think second one was, like, we wanted to go at least in a restricted path, so it was at least, like, some kind of configuration which is more restricted.
But it was, like, I think, the… another user jumped straight to third option, which is, like, very safe and, just allows us a specific set of status to be classified as non… non-error codes, so… so, yeah.
**Tyler** 06:41 Yeah, I'm familiar with this one. I think I forgot about this one. I do remember taking a look at some point.
Yeah, I… Walk me through why one or two would be preferable to this global.
**Puneet Singh** 07:01 So, one is, it allows user to provide a custom mapping function, so… One actually gives a lot of independence to users in terms of what they want to do, in terms of a specific method, and how they want to treat it differently from other methods, but that also means that this method will be executing in the hot path, and this is… Much more unsafe for the instrumentation, so this has received a kind of pushback before, so not considered a good option.
So… the consensus was that, or at least the input was in the previous discussion, that we need to provide something which is more restricted or more configuration-based, actually, which we can know that, you know, that there's a fixed set of functionality that is going on in the SDK, not something that is… we cannot control. So, first was, like, out of question, without any doubt.
Second and third both are kind of that how much restriction you want to put on this configuration, in terms of what is allowed.
Second is, like, more flexible option that it allows for, it allows you to classify what what gRPC response codes you want to classify as non-error codes by method.
So that is, like, highest level of flexibility, but the third is, like, a very restricted form, that you don't have such classification at the method level, but at the entire… for all methods, actually. So, you just classify that, what are the… some of the… GRPC status code you want to classify as the non-status portal response. So… so yeah, third is, like, most restricted form, and I think that is what Currently being in progress.
**Tyler** 08:53 Yeah.
Okay, sounds like… Yeah, thanks, that's helpful.
I definitely agree, I think it, like, having some sort of, like.
Configurable functionality's nice, but, like, the… the overhead of actually, like, doing this, I think, in the hot path is probably going to be restrictive of something along these lines. I do… I'm interested in this. I also see that maybe we could add both, But I think I'd want to understand, like, why you would want a per-method override versus just a global, like, is there… Have you seen a use case like this in the wild?
**Puneet Singh** 09:31 No. I mean, this is more like, you know, like, on-the-fly thought that if you want to customize, you have, methods with different purpose, some are health check, and some are, like, more of a regular business logic-based methods. And you do want to, treat them different… differently in terms of what kind of, you know, like, in… some cases which is more related to the health of the app, the… you want to reclassify the error quotes only for that particular method, but not for the business logic, so that kind of thought process went into, you know, coming up with the second option, so…
**Tyler** 10:08 soon.
**David Ashpole (Google LLC)** 10:10 I was also wondering if, like.
If we do something simple, like stop marking these as errors, In our config, if… users… Can add whatever arbitrary logic they want to fill in the gap, and like… If they want super custom, complicated.
You know, these are errors, and these aren't errors, then that probably belongs, like, in the application layer?
So maybe if we can just disable Like, if we can just disable setting these by errors, then they can do whatever they want.
**Tyler** 10:47 You mean, like, we don't set any of these status codes to errors?
**David Ashpole (Google LLC)** 10:50 No, no meaning, like, if we went with the… third, which is… non-Eric, like… I guess what we're actually doing, if I remember, is, like.
We're… instead of setting those codes to error, we're just setting it to unset, right?
But, like, users can still override those?
Right. We're not setting it.
**Tyler** 11:15 Yeah, I think it's… I think it's putting in… it's taking it out of the list that, like, OTEL provides, like, here's the gRPC error codes that, like, are errors, and it's just saying, like, that's no longer in that list to consider it to be an error. So yeah, I think it would be an unset status at that point.
**David Ashpole (Google LLC)** 11:30 But it's like, I guess, in a sense, like.
If a user can disable that behavior from our end, then, like, They can do whatever.
Custom stuff they want, if they need, like…
**Tyler** 11:42 I see what you're saying.
So yeah, if they wanted to do, like, this method, or… yeah, so, like, if they wanted to do, like… per method routing, they could set, like, hey, don't do note not found here, and then in that method, specifically, they could ask for, like, the span and then reset the error for all the other ones that they don't want, so it's essentially more of a whitelist at that point.
**David Ashpole (Google LLC)** 12:00 Right, it's… we're just turning off behavior inside of our instrumentation.
But users still have, like, the ability to… Set.
You know, within… within there.
**Tyler** 12:11 Can a… can a user get the span in?
Like, during the transaction?
**David Ashpole (Google LLC)** 12:18 That's a good question.
**Tyler** 12:22 Cause I don't…
**David Ashpole (Google LLC)** 12:23 I don't…
**Tyler** 12:24 No.
**David Ashpole (Google LLC)** 12:25 I think they would have to use an interceptor at a…
**Sam Xie** 12:27 I think probably none.
But they can set their own spin to be some kind of arrow, so the entire trace will become an arrow.
**David Ashpole (Google LLC)** 12:37 Mmm.
**Tyler** 12:37 Yeah, just as long as they get context.
That includes the trace, right?
**David Ashpole (Google LLC)** 12:43 Right, so that's… I guess that's different from HTTP, then.
**Tyler** 12:47 Yeah, alright, that's… I like your idea, David. I don't know if we, like, if we can get it so that they can get the span, or just even the context, like Sam's saying.
That'd be helpful.
But even if they can't, I do think that 3 is probably the best way to start, and then when a user comes back and is like.
I want two. We can either look into this or something else, right?
Because I don't think these are mutually exclusive, like, this is a different option, name. It's not a different signature of the same option.
**Puneet Singh** 13:24 So…
**David Ashpole (Google LLC)** 13:25 It's like…
**Puneet Singh** 13:26 Yeah, currently, I mean, I thought of these options as, like, mutually exclusive. I didn't thought that we can layer these, like, two and three.
Like, you know, user can override or provide specific options at method level, but you also have option to override at the all status level. That… that part wasn't part of this proposal, actually, yet.
But I get the idea, you know, that why you want to have both options for the user, that they want to apply some options for all the methods rather than one single method. That also makes sense.
**Tyler** 14:36 Okay.
What is this?
Yeah, I mean, I'm… I'm… I don't know.
I'm open to all of them except probably one. In fact, if we wanted to look at some way to, like, combine these two, where it's… because the other downside I see is, like, if we go with two instead of one.
this kind of stinks if you just want a global, right? Then you have to go find out all of your methods, and for each one of your methods, you have to put in some sort of, like.
list here.
Which is not ideal, either.
So, like, if we wanted to go with this direction, like, I'd want this to also have a global, like.
Option, somehow? Yeah.
So, like, if we wanted to find some way to combine these, I'm not opposed to that either.
But I'm also not opposed to just going to 3 as well. Like, I don't have any strong opinions, On that one. So if somebody would like to take the torch and go try to update 2 to make it more universal, that sounds great, too.
**Puneet Singh** 15:57 So, what we can do is, we can go forward with 3, but we also, you know, prepare up, like.
instead of two, we'll try to develop into that 2. The three is option, actually, to improve the… the options it provides. Currently, it doesn't provide any global option, like you said, so that thing I can work on.
**Tyler** 16:19 Yeah, okay. Yeah, sounds good.
Okay, cool. Alright, next up, you also wanted to talk about… Schema conflict regression test.
**Puneet Singh** 16:59 So, I think this was, regarding one of the feedback you mentioned in the Docker detector, that, it is having an older dependency of SDK, and because of which, there's the same conflict if we try to combine with… So I'm, like, half-convinced regarding the issue that It's, it makes sense, but… I was… I was wondering that, you know, what could be the downside if that test is not included? I mean, I just wanted to understand that… how useful it is for detectors to be at the latest SDK level, because the merge is not, you know, no detectors do merge, actually, it is done in the auto-detect. So, So yeah, I mean, the test still has use, but… What will go wrong if the test is not added?
**Tyler** 17:57 The test isn't added… like, that's… that's not really the problem, it's more the user behavior, right? Like, this is actually a really big problem for users, where they get these conflicts.
**Puneet Singh** 18:08 Agreed.
**Tyler** 18:10 To be clear, it's inevitable that they will get these conflicts if they do, like… any sort of, like, version upgrades that are incompatible, which happens very easily.
The ideal thing, though, is that, like, if… if they do one upgrade, it should work with the others, is kind of the idea. So, meaning, like, if they start using this, and they have, like, a completely up-to-date hotel, you know, dependency, they have a completely hotel, like, up-to-date other dependencies on the auto, on all these other things.
ideally, they should not get a merge conflict, right? Or, I'm sorry, a schema merge conflict, right? Like, so that's… that's, like, pretty key. Like, it always seems to happen that they will do, like, a partial upgrade.
Although I haven't seen this issue in many years, so maybe this doesn't happen as much anymore, but, like, they will do a partial upgrade, and, like, this error will come in anyways.
it's not, like, the end of the world. We document that you should probably just ignore this error. It's an error that's required by the specification, hence why we return it.
But… I do think adding a test here to try to, like, verify that, like, it is being used, I think that that's fine. We kind of already have, like, a linting test that actually shows that, like, you're using the wrong SEMConv.
Which I'm not sure… it's probably not passing because, or it'll… it'll… which means it'll start to fail when I try to go do a release, because it'll actually bump the version of SumConf in the process. So this… this will catch this before that happens, I guess is the thing.
**Puneet Singh** 19:51 Yeah, I was thinking that, you know, that if this change happens in the auto-detect, actually, because auto-detect is the… is the point which, you know, collects all the detectors and applies one by one. But I guess there are cases where if someone is trying to apply it manually, this kind of issues can still occur, so… so we are… I mean.
yeah, it makes sense to upgrade the SDK. I just wanted to, you know, like, follow it up, you know, to see if I'm missing something. But the test makes sense, so… I'll add those. It's still pending, actually. So, yeah.
**Tyler** 20:26 Okay. Yeah, it's, I don't… yeah, the… ideally, the entity stuff should try to fix this, or… I don't… I don't really know what's going on with the schema URL eventually, too much of my life has been wasted trying to handle this error, so I don't know what to tell you other than, like, this is just the way it is. It's just… it's super annoying. Yeah, so I'm just trying to keep it at the latest.
Ideally, we have a package to try to do at the latest. If a test can help in preserving that, I would try to do that. If it's… if you're like, don't worry about the test, it'll be caught somewhere else, like.
that's fine pushback as well. Like, it's just more about, like, I need to make sure that, like, that… It's not gonna have an error once we release it.
Which I will catch when I try to do the release, but it'd be nice to catch it earlier, yeah.
**Puneet Singh** 21:15 Got it.
**Tyler** 21:16 Yeah.
Yeah, welcome to the frustration of that stupid error.
Okay.
Alright, next up, Sam, add partial benchmarks for CI.
**Sam Xie** 21:34 Yeah. So, our current benchmark runs everything, like, all of the benchmark.
at the same time, and this PR will only allow, The package that has been changed.
To run the benchmarks?
Which should be, less than our benchmark, processing time.
And also, after remove the manual benchmark tying, the benchmark seems more stable than before.
Yeah, I just want to… Ask more review on this.
**Tyler** 22:14 Yeah, so this affected modules. Does this do a dependency tree, though?
**Sam Xie** 22:18 No. They… they only do the… the… How should I say? It's more agitative.
if there is a diff on a certain package, then it's just gonna run the benchmark for that specific package. It's not going to find, oh, who depends on that, then run all of them.
**Tyler** 22:42 Let's see… So, what if, like, changes in the benchmarking of one dependency amplifies the benchmarks of another?
**Sam Xie** 22:51 I think that… Could be in the following iteration. So this one, just a very simple block.
**Tyler** 23:02 Yeah, I mean, I'm, like, I'm thinking… Like, you change the benchmark of a function that's very minor, and you, you know, maybe add a few, tens of nanoseconds or something like that, but then it's, like, used in the hot path of, like, the metrics processing pipeline, and all of a sudden you're talking, like, milliseconds.
**Sam Xie** 23:21 Does it…
**Tyler** 23:21 It's run, like, continuously,
**Sam Xie** 23:25 if we want to.
**Tyler** 23:25 I see that, right?
**Sam Xie** 23:27 Yeah, another thing we can do is probably schedule a bi-weekly food.
benchmark.
Run.
So you're against all of the code.
**David Ashpole (Google LLC)** 23:38 I feel like the percentage increase would be higher in the microbenchmark.
Because it's only gonna comprise, like, some percentage of the second… Like… I would hope it would still be caught, if we have good benchmarks. There's, like, the obvious, like, what if we just don't have benchmarks for something, and it would have been caught elsewhere, you know?
But, like, I feel like our attributes package, which is probably the main culprit here, Yeah. I think.
It's gonna be reasonably well covered.
**Tyler** 24:11 Yeah, but I mean, I think that's a good example, right? Because the attributes package… So first off, like, I think… you have to remember that not all of our algorithms scale linearly, right? So… a microbenchmark that has, like, a small percentage is not going to linearly scale to something that has a dependency on it. Like, without, you know.
Caveat there. Obviously, there are some places where it will.
And I think the Ashby package is definitely one where, like, you start to see things like the set, or, like, the hashing algorithm, or something like that, like, you know, a microbenchmark in changing the hashing algorithm seems… you know, like, a minimal overhead, but then all of a sudden you are in the hot path of the SDK, trying to, like, do, you know.
5 hashes per measurement or something like that, like, that's… that's, I think.
Where you start to see, like, this scaling problem show up, and it may be more impactful than, I mean, we're also not gating PRs on any of these benchmarks, but it's more just, like, you wouldn't be able to tell, like.
you know.
on Sundays, we're running, like, the once-a-week benchmark, and you're like, hey, over the past week, like, something really blew up, like, what happened?
And, like, you wouldn't be able to figure that out without… I mean, I guess maybe eventually you could figure that out, but… yeah.
What's the downside of running what we have right now?
**David Ashpole (Google LLC)** 25:31 We're trying to reduce I think is the…
**Sam Xie** 25:34 Yeah, yeah.
**David Ashpole (Google LLC)** 25:35 I think we're using, like, 50% of all of Open Telemetry's runners or something.
**Sam Xie** 25:41 Yeah.
**David Ashpole (Google LLC)** 25:41 So…
**Sam Xie** 25:42 You see the usage of that bare metal, probably 50% on this ripple.
**Tyler** 25:50 Okay, sure.
Sounds good. I'll take a look at this. You're looking for reviews, I'm guessing is what you're saying?
**Sam Xie** 25:57 Yeah.
**Tyler** 25:58 Okay.
Yeah, I could take a look after the meeting, then. That sounds good.
**David Ashpole (Google LLC)** 26:02 I don't know if… do we… like, is there anything else we should think about doing? Like, I don't know if we should… Do an audit of where bench time goes on a single run, and like… Yeah, you know.
**Tyler** 26:15 Yeah.
**David Ashpole (Google LLC)** 26:16 See if we can trim any of them back by just a couple cases without losing too much signal.
**Puneet Singh** 26:24 So, we have to benchmark our benchmarks, I suppose.
**David Ashpole (Google LLC)** 26:29 profile them. We're profiling.
**Tyler** 26:31 Yeah.
**Puneet Singh** 26:32 Still.
**Tyler** 26:33 I mean, I… I think you were… intuitions are completely right, it's somewhere in the attribute package, but yeah, I don't know…
**David Ashpole (Google LLC)** 26:40 I think it's in the metrics SDK.
**Tyler** 26:42 Really? Okay.
**David Ashpole (Google LLC)** 26:43 Probably wrote off both.
**Sam Xie** 26:44 Most often, I would say.
**Tyler** 26:48 Yeah, the… Yeah, that was… yeah.
Actually, you're right. I think it's, like, the metric SDK takes over, like, a half hour to run locally or something like that, so… Yeah.
Yeah, I don't know, but I… I guess this is a first start, we can just turn this down, so… Yeah.
**Puneet Singh** 27:11 Actually, I did try to run benchmark one, so I progressively changed machine from 2 CPU to 4 CPU to 8 CPU, and then, you know, the time.
went down, actually, so yeah, now I remember.
**Tyler** 27:25 Yeah, I've definitely had to reboot my system and just run it without a… a UI, just to try to… Get reasonable results out of this thing, so, yeah.
Yeah, okay, I'll take a look. Anyone else on the call, please take a look as well, and yeah, we can try to get that included in the next release.
Okay, that's the end of the written agenda. Any other topics or things people are working on? Cool projects?
Well, okay, yeah, if not, we can end the meeting early here. Thanks, everyone, for joining, good to see you all. I will see you all in a week's time, or asynchronously. Until then.
**David Ashpole (Google LLC)** 28:14 Yep.
**Puneet Singh** 28:15 Bye.
