SIG: Go SIG
Date: 2025-09-18
Duration: 23 minutes
Zoom Recording URL: https://zoom.us/rec/share/PmjfwOBE-7jhX8ovbwwue_C-i79LyVK-lHNLpzF0meQ0EDdI0AgpohwaHFvEn0mx.I0hmXhy5vz_MX1mx
============================================================

## Zoom Recording Transcript

**Damien Mathieu** 00:42 Hey!
**Tyler Yahn** 00:43 Hey, Damien, how's it going?
**Damien Mathieu** 00:45 Good, how are you?
**Tyler Yahn** 00:47 Good.
How about yourself?
**Damien Mathieu** 00:53 Yeah, good.
**Tyler Yahn** 00:55 Nice, yeah. Not out and about, hanging out with friends tonight?
**Damien Mathieu** 01:00 No, not… not today, but, I'm… Yeah, I have a, like, meeting in 2 hours, so that's… yeah, fine.
**Tyler Yahn** 01:10 Even worse.
**Damien Mathieu** 01:13 I mean, just enough time after this meeting to just, like, put the kid to bed and then leave.
8pm is perfect.
**Tyler Yahn** 01:22 8PM, boy, that's, it's definitely winding down.
**Damien Mathieu** 01:26 I mean, it's not a work meeting, it's, like.
**Tyler Yahn** 01:30 Oh, oh, okay, okay, okay.
**Damien Mathieu** 01:31 I know it's not work.
**Tyler Yahn** 01:33 Oh, okay.
Yeah, I was like, man, that's… I definitely have some, like, colleagues that'll do that, like, that are in different time zones, but man, I just… I can't…
**Damien Mathieu** 01:42 I…
**Tyler Yahn** 01:43 I'm falling asleep at that point, so…
**Damien Mathieu** 01:45 Yeah, I used to do that, but, yeah, no more.
**Tyler Yahn** 01:52 Yeah, yeah.
**Damien Mathieu** 01:54 Hello, Brian.
**Bryan Boreham** 01:58 Hello? Oh, I had my audio on and video off for… No reason.
**Tyler Yahn** 02:11 Yeah, well, so it looks like this is probably gonna be sparsely populated today. I don't know if David's gonna be able to make it. I know Robert said he wasn't gonna be able to make it, Sam's out, so this might be us for the day.
I didn't have too much to talk over. If you have agenda items you wanted to talk about, please go ahead and add them.
If you want to also please make sure you add your name to the attendees list, and I can start sharing my screen. We can just jump in here in just a second.
Cool. Alright, yeah, I just wanted to check in. Last week we did a little bit of work. I don't, remember, Damian, if you were here last week. Oh, actually, no, you didn'.
**Damien Mathieu** 03:08 No, I was not here last week, it was at the time when it's convenient.
**Tyler Yahn** 03:14 Yeah, right. That makes sense. So, yeah, maybe we could just kind of check in here. We had gone through some open issues and opened, pull requests, just to make sure we have, like, our milestone up to date for this next push, for the next few weeks. So… I think we did a pretty good job, in kind of… finding some things, but maybe we could just kind of go through this. And if you, Damien, have some things you wanted to add, or things that you see in here that shouldn't be, then maybe we could talk about it.
So, essentially, just doing this again. So, This is something that's opened by Robert. He wanted to investigate the cardinality limit performance overheads, Yeah, so I think that was fine. This is something we talked about as well, the exposed temporarily select functions. This didn't make a lot of sense.
Based on, like, adding two different ways to configure this, and it was pointed out that they probably want to add, This, temporality selection, like, type to the, the OTELConf package itself, so that was suggested here.
Looks like, Damien, you also had suggested.
**Damien Mathieu** 04:26 Yes.
**Tyler Yahn** 04:27 Let's look at this. So, yeah, this looks like… I don't know if it's just gonna get closed, but… so this looks like it's getting a little stale at this point, so… Yeah, I mean, I think it's fine to leave it in, but I don't think we're actually gonna take any action on this.
David is working on the optimized locking for metrics aggregation, still in the draft state.
exported from Ethiasmigrate to the new configuration options. This has to do with the, naming, I believe, yes, with the translation strategy.
So, this is, I think just an open one. I don't think… Right, that's right. We have some remaining tasks. We want to change the default to the, Default we want, that's kind of a bad way to say that, but it's essentially we want to change the default, to whatever the new modern way is, and then we wanted to eventually remove the options, but we wanted to change the default, For this next release.
Oh, in the next release.
Okay, David is here, so I actually… I don't know if there's any action items for this… milestone.
I can't remember now.
David, sorry to throw you on the spot, I saw you just joined, but we were talking about this one, this migrating to the new configuration option for the translation strategy. I wrote this down last time, but I'm realizing, like, I'm a little confused. Are there any action items for this release, or are we just waiting? Yes. Okay.
**David Ashpole** 06:00 I just need to switch the default.
**Tyler Yahn** 06:02 Okay, alright, alright, so that's just the default of the thing we're waiting on for this one, okay.
Cool, alright. Then, that sounds good?
Next up is to improve Prometheus error handling. There's an open PR for this, that is… It's in… draft state? I thought it wasn't in draft state.
Yeah, I thought it was…
**David Ashpole** 06:26 Yeah, I thought that looked good.
**Tyler Yahn** 06:30 Oh.
I think it's just cause… Oh, I think maybe they're following up on some things. Okay.
Okay, yeah, it's probably just following up to David's review, so, yeah, I did too, I thought this looked close, so, it looks like they're just working on it.
**David Ashpole** 06:48 Still on… okay, yeah, you switched.
**Tyler Yahn** 06:50 Sorry, go ahead.
**David Ashpole** 06:52 I think you were looking at that one in a different tab or something that we couldn't see.
**Tyler Yahn** 06:57 Oh, okay, sorry, yeah.
**David Ashpole** 06:58 What you're doing now, yeah.
**Tyler Yahn** 06:59 Yeah, internet's maybe going a little slow, too. So, okay.
That looks like it's update, we're just waiting on, Yeah, follow-up from the person who it's assigned to, high mutex contention in the metric sums. This has something to do with the optimized locking for metrics aggregation, right, David? Yeah, okay.
I can't remember, I was, like, trying to remember, did you want review of this? No.
**David Ashpole** 07:23 Please, please don't look at this yet. It's… it's a mess. I… The… there's some interesting… If you have free time, it's interesting to look at.
The new file, atomic.go, has some cool stuff in it, that people might just be interested in generally, but the… The structure of our code isn't very conducive to what we're trying to do here yet, so I have to figure out some way to either refactor the aggregation package in general, or Or we can just accept That it's gonna be harder to read, but… It's replacing a simple locking strategy with a much more complex one, and I don't know if it's a good idea to do that. Well, one, I'm working on, actually, some new concurrent safe tests.
Now that we're introducing, kind of, the possibility for weird race conditions.
But two, just making it more readable so that It doesn't just break all the time in the future.
When people try and make changes.
**Tyler Yahn** 08:33 Yeah, okay.
Alright, yeah, that sounds good. We'll keep posted on that then.
**David Ashpole** 08:37 I did… so actually, one piece of feedback that might be helpful, so if you can just click on it. Yeah, sure.
I'm curious what people's thoughts are on… benchmark improvements.
that come with caveats. So, if you look at the benchmark results.
For sums and last value aggregations, it's just across the board better.
but the implementation for histograms and exponential histograms Comes with big performance improvements for… Parallel benchmarks.
And moderate performance Degradations for single-threaded benchmarks.
And generally, I think the parallel ones are probably more important, but I just… I'm curious if people think that this kind of Degradation for the single threaded benchmarks is something that would block something like this.
**Tyler Yahn** 09:40 Is that just because, like, the added overhead of the locking is causing this? And so you're not seeing the benefits of, like, the concurrency?
**David Ashpole** 09:46 Right, so part… right, it's the added overhead of… two locks instead of one for exponential histograms. But then it uses a lot of atomic types.
For individual pieces. And so, presumably, the atomics are just not as fast as… like, a regular… counter, right? So, you don't get any of the benefits. Maybe I'm wrong. Maybe I've messed something up here.
But that was my assumption.
**Tyler Yahn** 10:18 I don't think you're… that seems… like, we've seen this in other places where we've tried to address I think it actually was in the metrics SDK before, where we tried to look into using atomics in… it actually increased the computation time as well. So, I mean, I'm not opposed to this, But I would also… yeah, I'd have to look at the code, I think, as well, because I'm… I'd be… I'd be interested to find out, like, why, and what's going on there, and…
**Bryan Boreham** 10:49 I… I would offer 30 nanoseconds for a single increment feel… that's… that's the difference, right? That feels like a lot.
But yeah, I… similar, I… I guess… I'd be interested to see a profile.
**David Ashpole** 11:06 Okay.
**Tyler Yahn** 11:10 Yeah, okay. But yeah, like, if you're still working on, like, the code, like, I feel like this may change also, so.
**David Ashpole** 11:17 I'm gonna start with the tests, actually, and then… I'll do the refactor… Next, and then I'll probably just do the counter and, up-down counter stuff, because that seems non-controversial, and it's also much simpler.
And then I think histograms and exponential histograms will take a while.
I had fun watching a talk from Bjorn from… 2019, on… The… they have a lockless histogram.
Which is, pretty cool, but… Yeah, I don't… I don't know if I'm gonna attempt to replicate that.
**Tyler Yahn** 11:59 Just a standard histogram, or an exponential histogram?
**David Ashpole** 12:03 I believe both are. I was looking at their exponential histogram implementation. Their data structure is a little bit different, but, I think they use a sync map for the exponential one.
**Tyler Yahn** 12:17 And then for the, The explicit bucket histogram, like, is it just, like, similarly, a sync map, or are they using…
**David Ashpole** 12:25 No, they have saved something that's a lot different and weirder. I linked the video from this… PR if you're really curious, but… .
**Tyler Yahn** 12:36 Okay, yeah, cool, alright. That's interesting.
**David Ashpole** 12:39 That's interesting. It'll probably take me a while to get to it, if I ever do.
**Tyler Yahn** 12:44 Yeah, I mean, I think it… what you described also is a great idea, is to split it up. I would not try to tackle all that in this. So yeah, that also makes a lot of sense to me. The way that you've just described it as well is, like, testing is going to the… Counters, and then moving on from there.
Yeah, I mean, I think that the other thing is, like, is there a possibility to straddle these two? Like… Or is that just such a bad idea that you wouldn't want to do it?
I mean, I guess it's more about, like.
again, like, there's so many caveats here, but, like, if you did come back to the point where, like, you found that there is, like, a performance difference for these, and it's, like, if we could just use the old locking mechanism here, and use the new locking mechanism here, is that possible, or is that…
**David Ashpole** 13:29 Yeah, that's what I meant by doing things one at a time, is that I can implement the change for counters. It just won't… like, our code won't be consistent, but I think that's fine.
**Tyler Yahn** 13:39 Well, yeah, I mean, like, even in the long-term phase, though, like, if you started up the program and you said, like, oh, actually, hey, I'm running this in a single-threaded environment, Take this code path instead of this code path?
**David Ashpole** 13:53 I… I'm not sure, but I suspect we can actually I suspect with more work, I'll be able to improve it such that it's not such a big deal. I think Brian's probably right that 30 nanoseconds sounds like a lot.
So I must be doing something.
**Tyler Yahn** 14:11 I mean, 30 nanoseconds sounds like an extra lock.
I… I don't know, like… That seems on order, especially for a read-write lock, yeah.
**Bryan Boreham** 14:24 An uncontended lock in single thread?
**Tyler Yahn** 14:28 Yeah.
Like, that computational, like.
processing of just adding another lock is, I mean, 30 to 90 nanoseconds I've seen in operational modes, yeah.
It is not… it's not a cheap operation, So, I… yeah, again, like I said, I'd have to see the code, I think, before.
But, yeah. Okay.
**David Ashpole** 14:52 generics… I'll also say generics have been a pain in my butt.
Because you can make different optimizations for int versus float, but not if they're…
**Tyler Yahn** 15:05 Yeah, not if everything is… Defined over both, yeah. Yeah, fair enough.
Yeah, I know. I've been there before. Okay.
Moving on, in the rest of the… milestone, I've added… we were talking about this last time as well, we wanted to… include the observability issues that have PRs already out for them, so I've done that, through these few here.
I think we're all the way down to… Might be it. Yeah, okay, and then… The last is, this might be ready to merge, Return partial OTLP errors, to the caller. This is something that… While reviewing other code, I found this. Yeah, this is ready to merge. So this is… looks like it's been approved by everyone on the call, so not really much to say here. Okay.
Yeah, I'll… Look at merging that after there's… Okay.
Next up would be the contribib milestone. I don't think there's too much here. Yeah, there's… remove the, Deprecated, inject, and extract from OTEL gRPC.
It's got an assignee.
this looks like it just needs to get, I think, worked on. I think we had to fix the deprecation at first, so I think this is… Yeah, okay, last week I did add this.
Okay, yeah, so I think we're just waiting on some movement from the assignee, and we can probably switch this if we need to at some other point.
Not a big rush on this.
Okay, cool. That is the end of the agenda that I had. I know some more people have joined, so I can pause here. Any other topics people wanted to discuss?
**Damien Mathieu** 16:57 I do have one. We have one remaining issue on the, hotel HTTP SEMConf migration.
I'm not sure it's really related to the migration, but it's… I mean, we would probably need Robert to make a decision there, but I think it would be nice to close that out.
**Tyler Yahn** 17:22 Is… it's an issue, you said?
**Damien Mathieu** 17:24 It's an issue. It's the one about recording errors.
If you look at the project.
Yes.
Cannot trigger the error.
There's a bunch of discussion there, and opinions from Robert.
And it looks like it's not necessarily going anywhere.
**Tyler Yahn** 18:00 Okay.
I'll add it to the milestone so we can prioritize this to get it resolved, though, so…
**Damien Mathieu** 18:06 Yes.
**Tyler Yahn** 18:07 Okay.
Cool, thanks for bringing that one up.
Cool. Any other topics?
If not, I guess we can end the meeting early here. Thank you all for the work. I think, yeah, we're just chugging along. So yeah, we'll keep it going.
I'll see you all in a week's time, or two weeks, depending on, if you're joining next week, and then otherwise, asynchronously. Alright, bye everyone.
