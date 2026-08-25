SIG: C/C++ SIG
Date: 2026-08-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Douglas Barker** 01:25 Hey, Mark, can you hear me?
**Marc Alff [MySQL]** 02:02 Hi Duke, can you hear me?
**Douglas Barker** 02:04 Yep, I can hear you now.
**Marc Alff [MySQL]** 02:06 Okay, better.
Yeah, I'm sorry for my sound. Sometimes it's working, sometimes it's not, and I still need to figure this out, so…
**Douglas Barker** 02:16 I mean, we're.
**Marc Alff [MySQL]** 02:20 So, how have you been?
**Douglas Barker** 02:23 Pretty good, pretty good. How about yourself?
**Marc Alff [MySQL]** 02:26 Buggy with so many things, as usual.
**Douglas Barker** 02:30 Yeah.
**Marc Alff [MySQL]** 02:36 I just, wrote a quick note on the… on the team agenda.
**Douglas Barker** 02:43 Okay.
**Marc Alff [MySQL]** 02:45 Basically, I have only one item, which is, what do we do with all these PRs?
**Douglas Barker** 02:54 Yeah, I just saw it ticked up to 50, so that was a new record, I think, since I've been working on the project.
**Marc Alff [MySQL]** 03:00 Yes, yes.
It is, but I think, well, vous ais open PRs, but I think there is a better record, which is how many PRs we burst in July and August. This is amazing.
**Douglas Barker** 03:20 Yeah, fair.
**Marc Alff [MySQL]** 03:20 Yeah, yeah.
**Douglas Barker** 03:22 Things are moving in the right direction.
**Marc Alff [MySQL]** 03:24 Yes. So… One thing, comparing to what we had earlier, I think we have much more, Contributors, first of all. And also, we have many more contributors which are picking up really fast, like.
New issues, like… Whenever we say, okay, this is a new issue, flag it as, help needed and good first issue. In the past, we would wait for 6 months to have someone actually looking at it.
And last week or two weeks ago, I filed an issue, flagged it as needed help, and so on.
And I was thinking, okay, wow, that was… this one is a bit complicated, maybe it's not that easy.
And I go to PR within 3 hours.
So, it's… that was on the YAML config file.
**Douglas Barker** 04:30 Okay.
**Marc Alff [MySQL]** 04:30 And so… I'm actually quite surprised. We have people, So, first of all, to me, it means that, first of all, we have people paying attention, which is good.
**Douglas Barker** 04:41 True.
**Marc Alff [MySQL]** 04:42 the second thing, we have people who are… not only are paying attention, but are… capable of actually producing a PR, which is even better, because it's not that simple.
And especially for newcomers who don't know the project and don't know the codebase.
So… All in all, we have a good, incoming, rate of PRs, which are… Which are good, I mean, it's, sometimes people don't know everything, but it's, it's overall has a good quality, I think.
And, now the next thing is, the question is how to deal with that and do the reviews, and this is where we are failing today.
**Douglas Barker** 05:28 Yep.
**Marc Alff [MySQL]** 05:31 Well, failing in… well, I would not… should not say failing. I think… We accepted and merged quite a, quite a few of them, so… But the problem is that we… we cannot cope with the income.
**Douglas Barker** 05:48 Yeah, I think it's a challenge that a lot of the other projects are facing as well.
**Marc Alff [MySQL]** 05:53 Yes.
**Douglas Barker** 05:54 Because the barrier to entry is a little bit lower with some of the tools now.
So I wonder what your thoughts are on where to prioritize, because it seems like that's the next step, right? To look at what… What do we, prioritize up?
**Marc Alff [MySQL]** 06:15 Not quite sure. Well… There's only one thing… there's only one thing which is to prioritize whatever we think needs to be in the next release.
So, take, priority with those.
We can also prioritize by area, because, Just on the review side, I find myself it's quite hard to move from, oh, some specific YAML thing, to metrics, to building issues, to whatever.
So it's… at least for the review, it's easier to focus on one area for a short time. Like, okay, do all the YAML things, and then later do all the metrics, and… Later, all the build warnings in syringe ID, or things like that.
It's… at least when reviewing that, I would be more effective, but it's, it's a bit unfair, because, like, if someone raised a valid PR that fixes a valid bug on an area which is not in the high priority, they will wait for… wait for a long time.
Hmm.
**Douglas Barker** 07:33 I found in, you know, I've kind of been testing it out, like, just being a little bit more descriptive in the issues that I write, and then, like you said, new contributors are picking those up within 24 hours, typically.
**Marc Alff [MySQL]** 07:46 Yes.
**Douglas Barker** 07:47 And it feels like, like, and I saw in Slack, some other maintainers were mentioning, like, this is the, you know, kind of the approach that they want to take, is be more specific about the issues that you're filing, and then Contributors will naturally kind of trend towards working on those issues, and not the obscure things that maybe are less important or not the focus of the next release.
So, that's why, you know, from our last meeting, we talked about focusing on the, configuration, side of things, so the YAML and the programmatic configuration, that's where I've kind of been focusing a lot of… a lot of, issues. So I feel like that's… that strategy is going well, because, like, look at the resource detectors, you know, they're… they're pretty…
**Marc Alff [MySQL]** 08:30 Oh, yeah, it's very effective, yeah. It's one thing… we have known for, like, a year that we needed to do that, and nobody got a chance to do it, and now it's there. So, that strategy is effective, yes.
**Douglas Barker** 08:47 So that's my… that's my personal thought, and then just try to do, like, best effort to, like.
drive down the, the queue of the PRs, but put priority on the… The tickets that we're filing to try to get into the next release.
I'm also personally trying to convert my project over to use the YAML, that's why I'm, you know, whenever I find something that I need, I either log an issue or just try to fix it.
**Marc Alff [MySQL]** 09:13 Well, I… I'm exactly in the same spot, I mean, I don't do these things out of the blue. I do this because I have a dependency on it also.
So, yeah, this is, Focusing on the YAML part, I think it's effective. It's also a newer codebase, and both you and I know it well by now.
So I think we are more effective during code reviews and code changes there.
The part where I'm more struggling is, like, things like metrics.
and the different way to aggregate things, I mean, it varies a lot of, Special use case and subsidies about doing aggregation this way or that way, and that requires more thought and more analysis.
And I'm not… I'm not as much familiar in that part of the codebase.
So it's harder for me to do reviews there, for example.
**Douglas Barker** 10:26 Yeah, I think we've got… we've got one that we marked, required for the release.
That is, 4353.
And that's… that's a metrics one on the… exponential histogram.
So I think that…
**Marc Alff [MySQL]** 10:41 That's a pain.
**Douglas Barker** 10:42 This one, we're still waiting on, on, review. I haven't jumped into it yet. I think Lillette was, reviewing it.
**Marc Alff [MySQL]** 10:49 I don't have it in front of my eyes, but is this one from Tom?
**Douglas Barker** 10:55 Yes.
**Marc Alff [MySQL]** 10:56 Oh, okay, yes. Yeah, so it's definitely something which we'd look at.
Yeah, so overall, yes, how to deal with… with PRs. So, I guess the good news is that, We got attention, and we got contribution, which is, better.
So… My concern is how to… To make it so that we don't disappoint, people providing a PR by being too slow, or by being not responsive, and… And… basically… If, if we are too slow, they will, they will, they will… Move to something else and, and, pay less attention, I guess, so… Yeah.
This is the… This is the risk I see so far, which is to keep people engaged.
On another front also, we have this, this contributor, who is banging curl to death. I mean, I don't think there is another word for it.
So, THC something?
I mean, she's… Testing every single corner case of curl and race conditions and whatnot, and… So… from what… from what I've seen, the… all the issues reports are accurate, so, when there is initial reported, it's actually, Something we need to fix.
So it's… it's a good thing to report that many issues, and on the… on the fix, with PRs.
Except for a couple of parts, like, okay, well, this is test code, so it doesn't need to be as robust. But for production code, I mean, she also fixed a lot of issues that we had in the code, which are all valid.
So… I don't know what you're feeling about it, but on one way, on one hand, I'm… Very, glad that we had so many reports, and the code is… It's getting fixed to be more and more robust.
But the other thing is, I'm quite surprised that we have so many issues.
Which means my assumption so far that, well, vSQL has been working for a long time.
And we had no major issues about it, so it must be okay, and in fact, it's not.
So, it's… kind of shattering my confidence on that callbase. I was thinking it was okay, and maybe it's not that good.
So I don't know what to think of it.
**Douglas Barker** 14:01 I think there's… there was a signal there, because there were some contributors that wanted, an extension point so they could inject their own HTTP client, so I think that's…
**Marc Alff [MySQL]** 14:10 this.
**Douglas Barker** 14:11 That kind of gave me some indication, at least, that the community wanted to replace the CURL client.
But I haven't spent much time in the curl client, so I can't really say about the code there.
that contributor, so there was some discussion, I don't know if you saw it, in the discussions tab where Owen brought up, you know, because all of these curl issues I don't… there must be over 20 of them now.
all of the curl issues are kind of picking around different parts of the… that part of the library, and Owen raised the question, should we just redesign it, you know, refactor it, or overhaul it completely? And it sounds like that's what they agreed to, and then there's a PR that's in draft right now, 4458, which I think is…
**Marc Alff [MySQL]** 15:01 Okay.
**Douglas Barker** 15:01 is, like, the… the redesign, so I don't know what that means for the rest of these PRs and all the issues, but maybe… That feels like the right approach to me, is like, rather than fix everything piecemeal, just redesign it if it's got so many real issues.
But I can't say, because I haven't… I haven't dug deep into that… that bar with the code.
**Marc Alff [MySQL]** 15:24 Okay, looks, looks like I missed this discussion, but yeah, I see the… I see the design PR, Right now, so, yeah, I'll take a closer look at that.
So… Historically, Owent is the author of that area, so he knows it quite well.
And, you also… so there are two implementations for GERL, there's the synchronous and asynchronous one.
Things like that, so it's, I mean, there's a lot of things going on, we've… multi-threading, synchronization between threads, and of course, protocol things, so it's… it's not that simple. I mean, it's, It's easy when fixing one thing to break two others, so to get it… to get everything right, it takes some work and analysis.
**Douglas Barker** 16:16 Yeah, that makes sense.
**Marc Alff [MySQL]** 16:25 Another thing, you recall that, ceiling tidy, and the cleanup that we had there.
I don't know why, but somehow it slowed recently, so I'm hoping we can get, oh.
Get more fixes there, soon enough, and… The last time I looked, it was not that far off. Of course, we still have a lot of warnings from ceiling tidy, but… In very few different, categories.
So, each category should be easy to fix, and the last one, the very last one, is, everything related to exception handling, and the way that, If we say it's no except, then we should not raise exception and things like that.
I don't know what are your thoughts on it, but I think we should continue that.
Clean up everything but exception to get to a very clean slate, so when we can finally address the… exception safety, safety parts, because I think we can, we can actually do it.
Based on, the different Proposals and conversation we had, we had before.
**Douglas Barker** 17:43 Yeah, I agree.
And we have to put the warning limit on there accurately, because we left it a little loose, and then more warnings crept in.
So I think the strategy there is the same, we just need to take the current report and log issues.
With the warning categories, and people tend to work on them.
**Marc Alff [MySQL]** 18:07 Yes, yes, sounds good.
**Douglas Barker** 18:11 Okay.
**Marc Alff [MySQL]** 18:14 Another topic I had for discussion was also the team meeting, but since Lalit and Tom are not present. I mean, I think we need to wait for their input. So, you're right that the Wednesday meeting is not… it's not working that great.
It's… first of all, it's very early in the US, so I don't know if people can make it.
And for me, with, school, family issue, family constraint, whatever.
It's actually hard to make it, not to mention also other meetings, which are planned at the same time, once in a while.
So, yeah, the Wednesdays, at least at the time which is allocated for Wednesday, Wednesdays is not working well.
And Mondays are better, also.
if… If everyone agrees with keeping the same time slot for Mondays every week, I think we can do that.
But we should wait on, Tom and Nadit to have some more input, I guess.
**Douglas Barker** 19:28 Yeah, I think that makes sense. You know, my… after joining a bunch of those meetings and being the only one, and I think you experienced that yourself for a while.
**Marc Alff [MySQL]** 19:37 Yes, yes.
**Douglas Barker** 19:38 It's just a matter of, like, how do we make the best use of our time? Because we all want to join the meeting, but we also don't want to sit in the meeting, or set aside the time, and then have there not be a meeting.
**Marc Alff [MySQL]** 19:51 No.
And another thing also, I'm… I'm quite surprised that we don't use it that much, but doing some, discussion on Slack as well.
**Douglas Barker** 20:03 Yeah.
**Marc Alff [MySQL]** 20:04 Because Slack is extremely quiet. I mean, the… so, on one way, it's good to have all the discussion in the open, in issues or PRs, because this is what it is for. But for things which are purely internal, like, okay, meeting coordination, or discussing what we should do next, and things like that.
Those can be done in Slack as well.
Where not everybody, has to be present in the same, same time slot.
But somehow it's, we don't use Slack that much, I don't know why.
**Douglas Barker** 20:42 Yeah, we can use it more, and I think whatever asynchronous communication works for everybody, we should use that.
To the extent that, getting together on Wednesdays is difficult. Like I said.
I could also, you know, as long as we had a reliable, But we're able to make the meeting, you know, even once every other week is fine for me, and then we can do async communication in between.
**Marc Alff [MySQL]** 21:09 Yes.
Well, once… so, as I said, once every other week would be fine with me, but I'm more concerned about missing one.
And sometimes, like, some stupid things, like, okay, it's a holiday in Europe, or it's a holiday in France, or whatever, I mean, in the US, or wherever.
And if for some reason you miss one, then there is a huge gap of 4 weeks between 2 meetings, which I think is too much.
Otherwise, if it's… if we still have weekly meetings, well, if we miss one, it's only two weeks, it's not that bad.
**Douglas Barker** 21:47 Yeah, I think that makes sense.
Well, let's see, let's see what Lilad and, Tom say.
**Marc Alff [MySQL]** 21:54 Yes.
So, I know that Lalit is also buzzed with many other things, namely Rust, and possibly others.
So, because he's also a maintainer of the Rust, Oripple, so it's, it's… is involved in other things in OpenTelemetry as well. I don't know… I don't know about Tom's availability, I don't know if it's, If he's open to Mondays, or if he's… if he has, prior commitments or not.
We… we need to wait for him.
**Douglas Barker** 22:33 Okay.
**Marc Alff [MySQL]** 22:36 But yeah, in general, I think we should… try to… have more communication on Slack, asynchronously, so that we only keep the… the meeting itself for discussion, where we truly need to be online at the same time. It will be more effective.
**Douglas Barker** 22:56 Yeah, I think, I think that makes sense.
**Marc Alff [MySQL]** 22:59 Yep.
**Douglas Barker** 23:04 I'm gonna share my screen, maybe we can go through some of these.
PR, anything else that you wanted to go through?
I had, put these links in from the last one, so we could look at the release, and then the various, tags.
**Marc Alff [MySQL]** 23:18 Yeah, can you zoom in… zoom in a bit, please?
I'm an old guy, so… Yeah, so this is making good progress, I think. On the spin log mutex thing? Yeah. So, I did not comment on it yet, but looking at your PR, So, you change every spin lock to a mutex.
So, so there are parts, like, in the… Whatever it's called in, never vous, storage thing, I don't remember where it's absolutely abuse that we need a mutex, and there is another area which is aggregation.
And in aggregation, it's more, The aggregation code is not doing much, every time it takes a look, so… I think Tom had a comment that, yeah, we could do that, but, The size of a lock for a mutex is much bigger compared to the size of an atomic counter.
So, it will increase the memory footprint, which is… Correct.
And looking at the code as well, a lot of aggregation don't do much on, on the aggregate metadata itself.
So, for those, I think… I think what we should do is, just keep the spin lock for everything which is on the different aggregation.
As is, and only change, things for the, overcooked for metrics.
So… Once this is done, we can later evaluate again whether it makes sense to change for aggregation or not.
But the… I think it's better to decouple the question about aggregation compared to the synchronous and asynchronous metric storage.
**Douglas Barker** 25:30 Yep.
**Marc Alff [MySQL]** 25:31 Because for storage, we know we need to change it anyway, there's no question.
**Douglas Barker** 25:37 Okay. Yeah, I think that makes sense to me, and from looking into it, it looks like those aggregation locks probably aren't contested, if ever. I can't see a use case how they actually get two threads in there, because they're always locking.
Either the, the bound entry lock, or the attribute hash map lock, and then holding that over top, so it's always protected by another lock, so…
**Marc Alff [MySQL]** 26:04 nose.
**Douglas Barker** 26:05 I think the… Question I posed is, do we even need those aggregation locks, or what is the use case where they're actually used?
**Marc Alff [MySQL]** 26:13 So… whether we are actually protected by an overlook, I don't know. It could be the case in which, But the… Mostly, my question is, for those things, to understand what is the code pattern that will put pressure on those logs.
**Douglas Barker** 26:33 Hmm.
**Marc Alff [MySQL]** 26:33 First question being, so… In my app, I'm only using asynchronous metrics, anyway.
So, I'm never using synchronous metrics.
So… There's this part, whether it's for synchronous, asynchronous, or both.
And then, for synchronous metrics, the question is, is the contention happening where there are multiple threads in the application reporting on the same metric and the same instrument?
In which case, we may have, contention, or if it's… if one thread is reporting metric A and another thread is reporting metric B, then in that case, if there is no contention, there's no problem.
So, I would like to understand the… In which use case we have contention first.
To… to see what we… what we need to do about that.
**Douglas Barker** 27:32 Yeah, that sounds reasonable. So I posted some… performance results here, and… You know, please take a look.
high level, the unbound case, even converting everything to Mutex, it doesn't have a major impact in terms of I mean, we're talking about nanoseconds, so maybe you're looking at, like, one additional context switch at times. Okay.
What Benchmark doesn't show is the pathological case where maybe you have a one cycle that takes 15 milliseconds, which is what we can have with the spin lock.
So, that's gonna be hard to see in Benchmark, because it doesn't give you that level of statistics like P95 or anything like that.
So, anyways, yeah, I agree with your approach. I think what we can do for this release is I can scale this back, turn… put all of the aggregation locks back to spin locks, but then keep all the storage locks as mutex.
And maybe that's, that's okay. Less controversial.
**Marc Alff [MySQL]** 28:42 Yeah.
And I think you have a couple of PRs also on benchmarks. We definitely need to merge those.
Because we need the tooling anyway.
**Douglas Barker** 28:53 Yep.
And that… That is interesting, because I'm also gonna… See where it is, huh?
This one has some interesting findings. So, one is that all of the drop aggregations are actually expensive, which you wouldn't expect. So, here's… here's disabled, you know, less than… And it's basically doing no work.
and then drop is doing as much work as recording, so…
**Marc Alff [MySQL]** 29:22 Whoa.
**Douglas Barker** 29:24 So, there's an easy win there. You know, I… I don't think it's gonna be a ton of work to do that, but we just need to… a Boolean that we can check in the storage, and then before we ever lock the hash map, we just… if it's dropped, you just drop it.
**Marc Alff [MySQL]** 29:41 No.
**Douglas Barker** 29:42 So, that's an easy win. The other one that came up was the, performance of the bound instruments. Once we enable that feature, we get a pretty big, performance degradation.
Here's the… ABI V1 versus V2 with bound.
So, turning on the bound instruments, it actually degrades the performance of the unbound.
By about 60% across the board.
So, that's something we can look into, but I'll log two issues based on… on this, but yeah, I'd like to merge this, like you said.
**Marc Alff [MySQL]** 30:16 Yes.
**Douglas Barker** 30:22 And then keeping on the… so I think those two were the… Related to the Mutex Spin Lock.
issue, which is top priority for the release. The other one was on the configuration.
So, one that I found yesterday, which I'd like to… accelerate, if possible, if you have time to review it, is support for environmental variable substitution. I think this is one that kind of blocked me in my own use case, and it seems really important for users as well, so if we can get this one into the release, that would be nice.
**Marc Alff [MySQL]** 30:57 Yes, I actually looked at it, today. Okay. And so, looks like you found… so… the… as… as boolean, as integral, and so on, this is something I missed, but also, it looks like you found something in getString?
What was missing. Right.
So, yeah, it's, I looked at it, and it looks okay to me, so… I will approve that.
**Douglas Barker** 31:28 And then on configuration, so we had another, This one is nice, so this is getting the attribute limits propagated down from the top level.
So, I think this one looks like it's, it's, close now.
Are you familiar with the attribute limits?
**Marc Alff [MySQL]** 31:51 Yes.
So, the tricky part there is that there are some attribute limits defined globally, and then there are some attribute limits for traces and logs.
But the trick is… We somehow need to merge the two limits before applying them.
So, if there is a global limit for something, for A, and then a trace limit for B, the limits to apply will be the… The global limit, for one… one part, and the per trace limit for another part, when applying for two traces.
So there's a bit of, We need to take at both, both nodes and merge them, Before giving… giving that to the SDK, so it's only the tricky part.
**Douglas Barker** 32:50 Yeah, and I… I wrote in this comment, wrote about that, too, and gave this example, because one of the challenging cases is in YAML, it's valid to set a null value, so then we need to Make sure that we merge them, not just by the whole attribute limits versus span limits, it needs to be the individual limit.
**Marc Alff [MySQL]** 33:08 No, yeah.
**Douglas Barker** 33:09 merged in, so I think the contributor got that, did a good job on the fix, so I need to… I got some build issues, but… I think this one is getting close.
So that's one on the YAML, and then we also have… I think there's another one that I've approved, and I was going to merge after this meeting, if you don't have any… Feedback… This one… so this one, it adds some really nice features to the resource detector.
So, it adds the process creation time, process owner, the build hash, and then the process executable. The build hash is a really, really interesting one, so you get a unique ID for the executable.
**Marc Alff [MySQL]** 33:58 Okay.
**Douglas Barker** 33:58 That's… that's deterministic and cross-platform, so… It basically hashes, like, the… The first, 4,000.
Bytes and last 4,000 bytes of the… executable, and gives you an ID.
So, I've gone through several rounds of feedback. I think if you want to take a look, I can leave it open. If not, maybe we just merge it by the end of the day.
**Marc Alff [MySQL]** 34:27 I have to admit, I did not look at it yet, but if you feel confident, just merge it.
Oh.
**Douglas Barker** 34:34 Yeah, I think it's… it's still, you know, the resource detectors are still behind a feature flag, and they're… they're a component that you have to actually compile into your application, either by registering it with the registry for the YAML config, or you have to instantiate it directly, so… I think it's, intestine's good, so I'm okay to merge it, but just, I'll wait till the end of the day, so if you have any feedback or want to look at it, please, please do.
**Marc Alff [MySQL]** 35:02 Okay.
Okay, I will try to take a look, but don't wait forever.
**Douglas Barker** 35:07 Oh, okay.
Then, The other one… so I had two, two up, so the last time you and I spoke.
I was still working on, if you remember this issue, to decouple the SDK builder from the component builders.
So the goal here is to eventually get to a point where you can use the YAML config, or programmatic config, and select the signals that you want, and it'll only link to those libraries.
right now, the SDK Builder is kind of the one-stop shop, and it links, you know, instantiates all of the Trace, metrics, and logs components directly.
Yeah. So… the point of this work is to break out all those interfaces and then just have the SDK builder be relatively lightweight. It just, you know, gets the builders from the registry and doesn't have to link to anything. It's using that abstract interfaces all the way.
So, this, PR, which I like your feedback on.
It really just registers, or creates new interfaces for the actual providers.
So, like, Logger Provider Builder, Tracer, and meter provider,
**Marc Alff [MySQL]** 36:21 Okay.
**Douglas Barker** 36:22 This is the last step, so once these are in.
then I can actually move the… all of those concrete implementations out of SDK Builder. It's going to be a lot of code change, because SDK Builder is, like, already a 2,500 line file, and then its test is probably more.
So…
**Marc Alff [MySQL]** 36:41 Yes.
**Douglas Barker** 36:42 So that… that's the… the rough part, is, like, it's gonna… the PR shows up as a lot of changes, but, you know, it's gonna be moving a lot of stuff.
But the first step is to get these interfaces in, so if you could look at… look at this… That would…
**Marc Alff [MySQL]** 36:55 Okay.
Yeah, I will take a look.
**Douglas Barker** 37:08 Yeah, I think that's most of it, and then we talked about this one. This one I would like… I think is critical for the release, so… Well, that's given a lot of feedback, and they've iterated several times, but no approval yet, so I think we're just waiting for this one to be approved.
**Marc Alff [MySQL]** 37:23 Yeah, the issue for this one is to understand metrics, and it's,
**Douglas Barker** 37:28 It's hard to understand metrics, but the base two exponential histogram is, like, another level.
complexity, too.
**Marc Alff [MySQL]** 37:36 Yeah.
**Douglas Barker** 37:36 So… Yeah.
As far as… Discussions go.
I don't know if you saw the discussion on this one. You had originally logged the issue for the span, or event-to-span bridge.
**Marc Alff [MySQL]** 38:10 Yeah, so the… the event to span is basically a… a fancy way to… so, I don't even recall if it's, like, you… you file… you have a… Sorry, I think you have a log instrumentation, and the side effect of that login instrumentation is to add some properties on a recurrent span. Something like this, I think, or maybe it could be the other way, I don't even remember.
But basically, it's one signal which is collecting some instrumentation, and as a side effect, is manipulating another signal.
So it's a fancy, fancy thing where event and logs, Coupled some way, but only in the implementation for the… For the exporter.
And the issue there is, so this is totally disguised from the application point of view.
Application thinks it's logging things in one place, and creating spans in another, and those are decoupled, but no, they are not.
And in… under… under the hood, so, this bridge is basically… Pretending to create a log record in one place, and acting on it to… It'll change the current span, I think.
And I think… So, the first thing is.
It's highly unusual to have many more… many different exporters on the same signal, so this is creating some overhead.
And on top of that, I think the point of contention there is that, If we want to… Not export things at the end of the day, then why bother allocating memory and creating log records and all that to do nothing about it?
So, maybe there's a way to have something which is more effective?
But it's… There are a lot of constraints, because the… This whole bridge is pretending to be one kind of exporter, when in fact it is a different kind of exporter doing something else.
It's hard to comply with existing interfaces while doing something totally different.
**Douglas Barker** 40:43 Yeah, it… it definitely seems like the processor… For both logs and traces, the processor interface, which takes ownership of the recordable.
Kind of, by definition, means that it's a… it's… And how it's implemented is, like, a fan out, so, like, each…
**Marc Alff [MySQL]** 41:03 Yeah, it is…
**Douglas Barker** 41:04 Each processor gets its own copy, but there's no way to implement something like the, like the specs, you know, has some examples where you can make a filter, and you want to have a log filter that takes the information that the processor gets, and then decides to continue processing the log record or not.
And for our implementation with that fan out, and with the processor taking, you know, creating and taking ownership of the… log record, it makes that, implementing something like that not… it's not really possible, frankly.
**Marc Alff [MySQL]** 41:39 So the thing is, so the multiprocessor implementation, this is a fan-out, so it's the same data which is shipped in many different channels, and all those are independent.
So, we have to expect some duplication there.
And the duplication… the duplication has to be because… Each processor may be using a different buffering, for example, so even if you send the same log record 10 channels.
One channel will have a buffer that, maybe sends the data right away, and another channel will keep the data for a very long time.
Until the buffer is full and the data is exported.
So, that… this is the expected pattern. Now, if the point is to do filtering, I would argue that doing a fan-out is not the proper design. It should be a train instead.
So you have one processor doing some filtering, delegating to another processor doing something else, maybe more filtering, delegating to a third processor, which is finally exporting the data.
So it depends… it all depends on… What is the goal, and what people want to achieve with that?
But as far as the multiprocessor.
allocating more memory because you duplicate things? Well, that's… Kind of basically because of what it is.
Right. I don't think there's a way around it.
**Douglas Barker** 43:18 Yeah, what I propose, and it's what I think, We need for… for both logs in, and traces is the ability to replace the multiprocessor with one that can essentially create a processing pipeline. So that way we can, you know.
And we certainly can, like, the idea that we have to use the OTLP and record directly to Protobuff, it's actually slower than if we just recorded to the, the… the normal, Like, span data and readable… readable read-write log record.
The performance is better if we just use those common objects, recordables. Okay. So… I think, you know, if I look out, like, what I… what I think is the right design, like, you know, 6 months from now, or a couple releases from now, is that we convert those, like, those standard, exporters over to use the common Recordables that have the proper read-write interface, and then we just need a way to swap out the multi-recordable and multi-processor with a processor that can implement these pipelines.
that the… that the YAML, I think, is designed around, because the YAML's not, in my understanding, it's not really representing a fan out until you get to a point where you have Two processors that are exporting.
Is that right? Like, it would make a copy of the log record, like, right before putting it into the batch processor, for example.
But before that, you may have multiple processors, like a filter, sanitizer, the span-to-bridge, you know, event-to-span bridge. You might have these multiple Processors, but they shouldn't make their own copy.
Record, because the whole point is to be able to filter and mutate, right?
**Marc Alff [MySQL]** 45:20 Yeah. Well, if we… If we only… if we want to add filters to that, it's a… it's a different concept that I don't think we have in the space.
So I guess this is why these rules are defined as different processors.
**Douglas Barker** 45:36 Fair.
**Marc Alff [MySQL]** 45:43 But yeah, we need to… We take a look at these. Now, the… The use case of sending to, like, 5 different endpoints at once, I don't see that happening in production.
So this bridge thing, at most, there would be the OTLP processor and the bridge.
So it sees 2 at Marx, but I don't see more things there.
Thinking, like, oh, well, you export both to the output stream in the console, and then to a TLP, and then to Zipkein, and then to Jaeger, like, no, this will never happen.
**Douglas Barker** 46:22 Yep.
Yeah, so I think… You know, looking at some of the other implementations, and then looking at how YAML is laid out, and looking at these, like, advanced processing use cases from the spec.
I think… probably moving towards a, instead of a fan out by default, more of, like, a pipeline processor, and then a common recordable type. I think the opaque recordables where you serialize, you know, directly into whatever format you need, is always there.
But for the common use case that you would configure with YAML for the default, it should have the proper read-write interface that you can access, you know, and I think we can keep the.
**Marc Alff [MySQL]** 47:08 Good.
**Douglas Barker** 47:08 current recordable interface, but you need to have… we need to have that standard interface, which is blocking a lot of these cases, like, specifically the event to span, I think, drove a lot of this.
These requirements.
But it highlights some of the challenges with the current design.
So… Anyways, I've shared my thoughts here on what may be needed. Currently, this PR is waiting on some feedback from Lolette, but I've asked the contributor just to scale it down to only work… only adding the, configuration model, and then that allows us to at least read the element from YAML, and then emit a warning And just say it's not implemented.
Because right now, it's…
**Marc Alff [MySQL]** 47:57 Okay.
**Douglas Barker** 47:57 it's silent. Like, if somebody puts the span… span… event to span bridge in YAML, it will just not say anything, so they won't know if it's.
**Marc Alff [MySQL]** 48:06 Okay.
**Douglas Barker** 48:07 If it's working or not, but at least with this, it will give them a warning, then we have the configuration model implemented. So, I think it's okay to merge as is, and then probably we need some, some, Time to come up with a design.
To actually, actually implement it in the SDK.
**Marc Alff [MySQL]** 48:25 Yeah, so, yeah, so the YAML part, I think, should be straightforward, and for the SDK implementation itself, yes, we need to figure out how to be effective there.
Yep. It's… It will probably take some time, because it's not a simple thing.
**Douglas Barker** 48:43 Agreed.
Okay.
**Marc Alff [MySQL]** 48:55 So, how… how are your thoughts about, releasing? Do you want to… Really soon enough, or, like, in… in 15 days from now, or… What's your own good feeling of…
**Douglas Barker** 49:09 I think we can target by the end of next week, so at the end of, Or maybe the third?
**Marc Alff [MySQL]** 49:17 Okay.
**Douglas Barker** 49:19 3rd or 4th? Does that sound reasonable?
**Marc Alff [MySQL]** 49:23 I would have to check on the dependencies, see if everything is all there, but, why not, yes?
**Douglas Barker** 49:30 Okay.
**Marc Alff [MySQL]** 49:34 Also, something I forgot to mention. So, the huge PR for moment, to change all the CMake options to hotel CPP something.
So, it's finally emerged, so this is some good news.
Yup. And… For many other things, there are some options which are duplicated, and we announced that they will be removed in October.
I'm hoping to… Well, I would like to file a deprecation PR as well, to mention that this renaming of oceans will be also, deprecated… well, it is deprecated, and it will be removed in October as well.
The… the reason being… If we change things in make files, this is, by definition, annoying to people.
**Douglas Barker** 50:31 Sure.
**Marc Alff [MySQL]** 50:32 So, I would rather have all the changes doing… coming up at the same release, so people adjust once.
As opposed to say, oh, in October we remove option A, and in November we remove option B, and in December, you have option Christmas and whatnot, and this gets annoying.
So… if we have to make some changes to make files, just do all of them at once, we have a release node for that anyway, it's the same kind of work, but at least, People will just do it once and don't have to do the testing again and again at every release.
So… For… because of this, I would like to propose to… move the old names from CMake in the same time frame, basically.
**Douglas Barker** 51:26 Yeah, I think… I think that makes sense.
Do you… do you have an idea for how long? I mean, we can just post it here, whatever you come up with?
**Marc Alff [MySQL]** 51:36 Well, I can… I can file a… file an issue and raise a PR just to… toward the, removal date, I mean, that would be… Easy to do.
**Douglas Barker** 51:47 That sounds good. And maybe we need to come… See what other preview options need to be, defaulted to be on, if there are any, available. I think one that we'll want to look at is, like, the resource detectors at some point.
**Marc Alff [MySQL]** 52:05 So, this is another topic which… well, we have plenty of options, but still need to be on by default, which are opt-in today.
And, it will take time to do… to change all of them one by one, so I think it's too late for October.
Because things like, OTLP, virtual preview, and the gRPC, SSL, and things. Those have been done in… maybe in the spring, maybe… If he was… Yeah, sometime in the string.
So we took some… It was announced a very long time ago for people to be aware of that and so on.
Oh.
So I think it's too late to change new things.
But we… we can do another round for those anyway.
It's not like we lack any options.
**Douglas Barker** 53:04 Okay.
Cool, that sounds good. So I'll add a few for the, release issue.
Dude, where was that?
**Marc Alff [MySQL]** 53:24 Yeah, feel free to add anything you need.
**Douglas Barker** 53:26 Do you want me just to edit the top one, or just continue to add to…
**Marc Alff [MySQL]** 53:30 Just… adjusted to the top one.
**Douglas Barker** 53:33 Okay, so I might cross this out so people don't get confused.
**Marc Alff [MySQL]** 53:37 No.
**Douglas Barker** 53:38 Alright.
Sounds good.
I guess the only other thing you probably saw, the Ziz… is this more, security workflows are now enabled on all the… hotel CPP repositories.
**Marc Alff [MySQL]** 53:57 Yeah, I saw something about that, but… Yeah.
I saw something about security, but didn't have time to take a look at it in detail.
**Douglas Barker** 54:06 Yep.
**Marc Alff [MySQL]** 54:07 I think Trask changed some workflows to do some more auditing.
But I don't… I don't know, the full effect of it.
**Douglas Barker** 54:20 Yeah, it should be, well, it's running every PR now, so if anybody edits a workflow file, it will check it, and we'll get some warnings, or no warnings.
**Marc Alff [MySQL]** 54:32 Okay.
**Douglas Barker** 54:33 It's a nice, nice feature to have working now.
**Marc Alff [MySQL]** 54:36 Okay.
**Douglas Barker** 54:41 Cool.
**Marc Alff [MySQL]** 54:45 Okay, that's cool.
Overall, I guess we need to… to try to survive the PR wave.
Let's see how… see how we do.
But it's, I mean, compared to… I've been in OpenTelemetry for a couple of years now, but it's, It's a… it's a good change, compared to… The level of contribution we had in the past.
We definitely have more contribution.
I don't know if this is because people are using LLM today, or if this is because We are more mature, or if this is because we are more advertising easy-to-fix things, or ill-pointed things.
But whatever it is, it is working, so… Which would be… We should be careful to keep that momentum going.
**Douglas Barker** 55:44 Yeah, I think it makes sense.
Cool.
Alright, well, that's all I had. Anything else?
**Marc Alff [MySQL]** 55:55 Not for me. Glad to talk to you.
**Douglas Barker** 55:59 Because I don'.
**Marc Alff [MySQL]** 55:59 I definitely know a feeling of being alone in, in Zoom, so…
**Douglas Barker** 56:06 Yep, well… We'll see if we need to update the schedule.
**Marc Alff [MySQL]** 56:11 Yeah, so, yeah, I'm hoping we can do some, like, every Monday would be… well, I don't know if it will work for everyone, but at least for me, it will be better, so…
**Douglas Barker** 56:21 Okay.
**Marc Alff [MySQL]** 56:21 We'll see.
**Douglas Barker** 56:23 Alright.
Awesome. Thanks, Mark.
**Marc Alff [MySQL]** 56:27 Take care. Cheers.
**Douglas Barker** 56:29 Yeah.
