SIG: Prometheus WG
Date: 2025-11-21
Duration: 63 minutes
Zoom Recording URL: https://zoom.us/rec/share/vqGw2G-9RDQPPCRUJlvjTkc01OcpdHnW_Sz_V_ndEM2wZRA_HoQDIS65iT9qSLla.LxvSwjhDQQ9jnRlA
============================================================

## Zoom Recording Transcript

Arthur Silva Sens 00:00:07 Hello.
Owen Williams (he/she) 00:00:10 Hmm.
David Ashpole (dashpole) 00:00:36 Hey, I'm back.
Arthur Silva Sens 00:00:38 Hello, welcome back.
Owen Williams (he/she) 00:00:39 Oh.
David Ashpole (dashpole) 00:00:40 Once again, at the Prometheus SIG.
Feels like it's been months.
But…
Arthur Silva Sens 00:00:46 It has been.
David Ashpole (dashpole) 00:00:48 Huh?
Arthur Silva Sens 00:00:48 Because you miss… I think you'll miss 2 or 3 meetings?
David Ashpole (dashpole) 00:00:53 Yeah.
And thank you, Owen, for all your work on the slides. I actually learned a ton about… it was fun to, like, dig into all the things that have happened in the last 6 months in Prometheus that I wasn't previously aware of, yeah.
Owen Williams (he/she) 00:01:15 Hooray, yeah, I was… I… I apologize, some of the notifications were getting through to me, so you asked some questions, then it would be, like, 6 hours before I'd see it, so I'm glad it… I'm glad that didn't harm things too much.
David Ashpole (dashpole) 00:01:26 I forget, what time zone are you? Are you… Eastern.
Owen Williams (he/she) 00:01:30 Yeah, I'm… yeah, you're… we're wearing.
David Ashpole (dashpole) 00:01:32 So we are in the same time zone. I felt, for some reason, I had in my head that, like, oh man, Owen's in Europe, and he's, like, up at 2AM, looking at my slides.
Owen Williams (he/she) 00:01:41 Yeah, so I was in… yeah, I was in Amsterdam for…
David Ashpole (dashpole) 00:01:44 Okay.
Owen Williams (he/she) 00:01:44 the Grafana thing.
David Ashpole (dashpole) 00:01:46 Yeah, yeah.
Owen Williams (he/she) 00:01:47 This explains why Cryo and I were lonely in the Prometheus Working Group meeting this week, because it had been moved. So, like, I have to copy it to my calendar, and so…
David Ashpole (dashpole) 00:01:59 Yeah.
Oh, no.
Arthur Silva Sens 00:02:03 Why, though?
Like, if you, like… in the community repository, you can join a Google group.
And if you are… if you are in this Google group, once the meeting moves, it moves on your calendar as well.
David Ashpole (dashpole) 00:02:20 Yeah, I do that, but then there's 600 meetings on my calendar.
Owen Williams (he/she) 00:02:25 Exactly. So I copy the ones that I go to, and then I hide the calendar. Exactly. Which doesn't always work.
Arthur Silva Sens 00:02:33 You can join only the Prometheus, there is one group per SIG. You can join the whole OpenTelemetry, and you can join it only for specific SIGs.
Owen Williams (he/she) 00:02:45 I bet there is a way to do that.
Arthur Silva Sens 00:02:49 Anyway…
Owen Williams (he/she) 00:02:52 No, it's good to know. If I… if I have some… yeah, I'll, you know, one day, maybe I'll figure out how to do it.
Arthur Silva Sens 00:02:58 So you think Cryo is not joining today?
Owen Williams (he/she) 00:03:02 He may not know about it, let me ping him.
Arthur Silva Sens 00:03:07 Hmm…
That's probably… Very short heads up.
And I guess we can start.
Yeah. Not sure if you two are aware, Adam and Owen.
David Ashpole (dashpole) 00:03:41 But.
Arthur Silva Sens 00:03:43 The collector SIG is doing a lot of changes to be able to graduate in CNCF.
There's a lot of work going on to declare the collector stable.
And… And that they have, like, a version of Collector That people can use.
And it doesn't break between upgrades.
And this one… this collector that doesn't break is not gonna be contrived.
Because Constrip has a lot of random components, a lot of untrusted code owners, and, like, it's just hard to…
keep control.
So what they're doing is moving a lot of the most used components from the contrib to collector core.
And Prometheus Receiver is the most used component out there between almost all vendors.
Ignoring some, like, I don't know, the batch processor, things that are literally in every collector.
So… they asked us to help them stabilize the Prometus receiver. There's a lot of work to be done.
I created a GitHub project, which is linked in the meeting notes.
And if you open the project, I split it up In a few stars, like.
David Ashpole (dashpole) 00:05:09 Do you want to change?
Arthur Silva Sens 00:05:09 Oh yeah, good idea.
Is this readable?
David Ashpole (dashpole) 00:05:27 Yes.
Arthur Silva Sens 00:05:28 Okay.
Yeah, so I split it up in, like, high level, like a parent issue, and the parent issue has sub-issues, and the sub-issues also have sub-issues.
But I think it's understandable.
I split the… what needs to be done in…
status, like, there's a lot of…
Things that needs to be discussed before we…
We move on to actually implement anything.
Then there are issues that don't have…
Any discussion needed, it's just somebody grab and do it.
that I put it this workable status.
In progress is when somebody picked it up.
And it's working on it, so we just need to be active and review the PR.
But I don't know how we wanna organize this, like…
do we want to discuss everything and then start working, or let's discuss one work, discuss next work? Like, any plans on how to do this?
David Ashpole (dashpole) 00:06:43 I think we can… it would be nice to get a sizable number in the workable queue.
So I think we should prioritize spending our meeting time
If there's anything in progress.
where questions have come up that need to be discussed, we prioritize those. If there's anything that people have tried to start working on, that they have questions about, we can discuss those, and then we can move to the ones that need more discussion.
Does that sound good?
Arthur Silva Sens 00:07:10 Yep.
Like, let's try to keep, like, 5… Is 5 a good number?
David Ashpole (dashpole) 00:07:18 I think it's fine if we have all of them in a workable state, but we should just prioritize, like…
If… if, for example, you have
Things you want to talk about regarding the test coverage?
Stuff that's going on. Like, we should talk about that first.
To make sure we unblock existing work. But, yeah, like, let's try and get through discussion-needed ones, especially anything you think is gonna be…
Quick and easy, so…
Arthur Silva Sens 00:07:46 Hey, I think this PR Cryo has been reviewing.
It's a very AI… made PR, but I guess that's okay.
David Ashpole (dashpole) 00:07:56 Yep.
Arthur Silva Sens 00:07:57 Yeah, like, the author is answering the reviews, Probably.
David Ashpole (dashpole) 00:08:07 Hi, what do you think, Cryo? Like, we need to discuss anything on this PR, or, like, you're… you got this covered?
krajo Krajcsovits 00:08:14 I got discovered. Yeah, it is AI-generated, but it does increase the coverage, and I made them throw away the
glutenant.
Useless.
Arthur Silva Sens 00:08:25 That's cool.
krajo Krajcsovits 00:08:27 Half the size it was, basically.
Arthur Silva Sens 00:08:32 Okay, so… Things that are easy.
I guess this one is easy to discuss.
This went not so easy.
David Ashpole (dashpole) 00:08:48 The observability one was interesting. I don't know if you've seen my comments on some of these.
Arthur Silva Sens 00:08:53 Which one?
David Ashpole (dashpole) 00:08:54 hub.
Yeah, was there another observability tick?
Arthur Silva Sens 00:08:59 Is, processing performance.
David Ashpole (dashpole) 00:09:03 It would be nice, maybe, to discuss all the observability ones together.
Okay.
sequentially.
Arthur Silva Sens 00:09:12 I didn't see this.
Okay, so let's do this one first. Like, a stable component needs to be able to observe data that is going in, data that is going out, and data that is dropped.
A Prometheus receiver has… is using Prometheus codebase for scrapes, so there's some metrics already.
Like, scrapes sampled, script duration, so this is measuring data in.
If we have… if we… configuration option called Report Extra Scrape Metrics.
that toggles a feature flag in Prometheus.
If this is enabled, then there is even extra metrics, like scrape timeout, Yeah, Owen?
Owen Williams (he/she) 00:09:59 Oh, you can finish your thought.
Arthur Silva Sens 00:10:02 There is more metrics, like script time out, body size in bytes.
For data out, we are using,
a helper package from OpenTelemetry Core. It gives us an amount of metrics that goes to the next component in the pipeline.
For data dropped, we don't have any metrics.
But there is some differences, like, if we scrape a classic histogram.
we say that we… I don't know, let's see… 2LALE… labels.
There's two do-term series for the buckets, there is a count, there is a sum, so this is four series, but in the data out, it's only one explicit histogram, so there's a difference.
And this difference, we don't really measure that well. I don't know if we can, anyway.
Owen Williams (he/she) 00:10:59 Yeah, I was gonna say, and then there's issues, you know, more on the Grafana Labs side of, like.
discarding, you know, the difference between discarding because it was bad versus dropping for an adaptive metrics thing versus this consolidation thing, it makes the numbers really hard to compare. But I think…
having as… being able to count all those things. Maybe you need, like, an enum for, like, why it was dropped, like a… like a string label that's, like, dropped
For a reason, and then we can just, you know, people can make up as many strings as they want, hopefully not too many.
David Ashpole (dashpole) 00:11:36 Is this… are you going to… this has already been done?
Owen Williams (he/she) 00:11:40 Yes.
But yeah, I…
Just as much detail as possible, and yeah, to try to make that math add up for people.
Arthur Silva Sens 00:11:53 There is a PR in the collector that adds this dropped metric.
Owen Williams (he/she) 00:11:58 All my greatest ideas other people have already had and started implementing is the rule of software engineering.
Arthur Silva Sens 00:12:08 But, like, I don't know why… I'm not a maintainer of core. I approved the PR, some other person that it's not… also not a maintainer approved the PR, and it's just getting stale.
Yeah. Sorry.
David Ashpole (dashpole) 00:12:21 Can you, can you add dashboll on that? It's not in my queue for some reason. Oh, this is Exporter Helper.
Oh, never mind, I can't approve that.
I thought so.
Owen Williams (he/she) 00:12:30 So wait…
David Ashpole (dashpole) 00:12:31 Prometheus Exporter.
Owen Williams (he/she) 00:12:33 But this is adding metrics with different names.
I don't love that. I would, you know, it'd be… if they were labels, then you could, like.
Do stuff with them.
David Ashpole (dashpole) 00:12:45 Dude.
Owen Williams (he/she) 00:12:47 I don't know if it's too late to have this complaint, I, you know, I'm just… I'm just a guy showing up.
Arthur Silva Sens 00:12:52 But, like, nobody's…
nobody's reviewing this PR. If anybody reviews, better than nothing. So, if you have a different opinion.
Owen Williams (he/she) 00:13:01 Yeah, okay, I'll…
1374.
Arthur Silva Sens 00:13:07 this.
Owen Williams (he/she) 00:13:11 Cool
-Oh, the star is for the metric type, spans, metric points, log records.
David Ashpole (dashpole) 00:13:27 Yeah, that's fine then I do think we should…
Like, we drop metrics, for example, if we get a gauge histogram.
Right? So we… we do definitely drop metrics, and we should definitely…
integrate with OBSReport, or whatever, to record those. I'm not sure if we do today.
Owen Williams (he/she) 00:13:48 And there is a reason string.
Arthur Silva Sens 00:13:51 Yes.
Okay, I mean, when it's obvious that we drop, like, gauge histograms, that's okay, I just don't know how to measure this difference, like, when multiple series becomes one metric, like summaries and classic histograms.
David Ashpole (dashpole) 00:14:11 I agree that that's, like, a…
potential point of confusion for users. Do we… is there an ops report metric for, like, Series in?
Arthur Silva Sens 00:14:23 That we should be populating there.
Owen Williams (he/she) 00:14:30 But there's also the question of how would you do that math if you've… you need to know the multiplier of, like, you've gone from X series to 1 series, and if you don't know what X is, then you can't make those numbers add up.
David Ashpole (dashpole) 00:14:44 I, I see.
Owen Williams (he/she) 00:14:45 Nope.
David Ashpole (dashpole) 00:14:45 the way I would do it is, like.
We do already group by metric family name.
And so we already take, like, a bunch of…
We try and construct complex histograms and stuff, but if we…
If we did that, and then found that we had not received
Something that was required, and had to drop the point in that case.
Then we would know that it was, like.
one… it would have been one hotel series, except that it was dropped.
Right? So, like, we could do that.
But I think it's actually okay, especially for 1.0 for us, to just make sure that we're counting all the things that we're dropping.
In, in some ways.
Owen Williams (he/she) 00:15:29 Yeah, yeah, something's better than nothing, yeah, yeah.
David Ashpole (dashpole) 00:15:32 I think anything that we… so there's two, like, pieces. We have our append path, and then we have our commit path, right, for the receiver.
And append is almost always in terms of samples, like Prometheus samples, and then commit is almost always in terms of, like, all the stuff we do there is already grouped.
So if we drop things during commit, then…
Like, that should… we should be able to count those as, like, hotel series dropped.
But if we drop it during append, I think that actually fails the scrape?
Arthur Silva Sens 00:16:06 Yes, I think it… I think it does, because iScrape is seen as a transaction in Prometus world, so if we… if one metric
It's bad in a whole scrape, then the whole scrape is not committed.
David Ashpole (dashpole) 00:16:21 Yeah, so ideally, we should just never drop anything during append, and we should only drop things during commit, and then we can count the number of
Like, full series.
You know, histograms all combined and stuff that we're dropping.
Owen Williams (he/she) 00:16:36 So, are you saying there's kind of two sets of metrics, one for the append and one for the commit, or are those types on the same metric?
David Ashpole (dashpole) 00:16:43 So, I would say that the Prometheus scrape Metrics
Are the metrics for append behavior?
Owen Williams (he/she) 00:16:51 Okay.
David Ashpole (dashpole) 00:16:51 For example, scrape duration seconds is actually the time to scrape and to append.
For the whole endpoint.
And then, we should only use OBSReport in the commit portion of the receiver.
Right, where we've already done all the appends, and we're now trying to do the big, like.
put it all in an OTLP payload. And if something turns out to be incomplete.
Then I think we can, at that point, consider it essentially, like, one hotel series dropped.
And so we… we would not… we would use OBSReport only for dropped points, and only for…
Export, or, like, sent into the pipeline points, if that makes sense.
Arthur Silva Sens 00:17:38 Can you write this down in the.
David Ashpole (dashpole) 00:17:40 Yeah, sorry.
Arthur Silva Sens 00:17:41 I, I lost you.
Midway.
David Ashpole (dashpole) 00:17:47 Maybe I'm talking too much.
I was listening and writing at the same time, and I failed to do both.
Oops.
Let's see, this is 44196.
Sorry for all the typing noise. We can also move on to…
Arthur Silva Sens 00:19:35 Move on to the next issue, you mean?
David Ashpole (dashpole) 00:19:40 Actually, give me one sec to finish writing, and then if people have comments, they can comment.
Alright, refresh.
Arthur Silva Sens 00:22:31 Okay.
That makes sense to me.
What we don't have is just the number of dropped series, right?
David Ashpole (dashpole) 00:22:44 Well, during the append portion, there's no such thing as… well.
There's sort of no such thing as a dropped series, because we either fail the whole scrape.
If something goes wrong in a pen, or we keep the whole scrape.
But if we fail a point during append, then we're not going to get any of the rest of the points. So it's like… there's no way for us to accurately measure the number of
Stuff we're dropping when we fail a scrape.
And I don't know if we should try. I think that the Prometheus scrape metrics are good enough for that case.
But then if we do drop things specifically during translation, like drop some things, keep others, then…
In that case, we can consider them dropped.
And we can count that.
Arthur Silva Sens 00:23:40 Okay.
I'm gonna move this to… Workable.
Would you consider this a good first issue?
Probably not.
David Ashpole (dashpole) 00:24:14 I think… it's… I think the actual action items might be reasonably good. Like, We need to…
we need to start recording the dropped metric, and I think if we did a little bit of legwork and figured out all the cases where we dropped.
unwrote an issue. I don't think it's a good first issue, yeah. I think it needs a little bit more.
Owen Williams (he/she) 00:24:36 Yeah. Well, all the work is in figuring out where to add these things and what they should be, which is a lot of work, and then…
It's just adding some metrics. But, yeah.
David Ashpole (dashpole) 00:24:47 We could make it actionable for people trying to get involved.
Owen Williams (he/she) 00:24:50 Yeah, that might actually be… yeah, once you do that, even figuring out where to add a line, adding a metric could be enough work for somebody who's never seen the codebase before.
David Ashpole (dashpole) 00:24:59 And unit testing is not trivial for some of these, so…
Arthur Silva Sens 00:25:05 Next one is processing performance. It's how to measure
the whole thing that the receiver is doing, like, doing the scrape, translating to OTLP, and sending to the next consumer.
It is suggested that we have our… our spends.
Somewhere in the codebase, or that we have histogram metrics.
That measures each part.
And David had a comment that I didn't see.
David Ashpole (dashpole) 00:25:37 So, one thing I found while I was digging into the Prometheus server code is that scrape duration seconds includes the…
Append time.
So the only thing it excludes is commit.
And so I think… Scrape duration seconds is already a reasonably good, like, starting point for users.
But I think that the missing piece is that we could instrument,
Commit, which is basically the translation portion.
I'm not sure if that's going to be a meaningful source of latency, even for really large
Payloads, but it could be.
I can imagine.
Arthur Silva Sens 00:26:15 I think there is, like, I think it commits… It's…
It's the one that takes most time, because this is where we translate things, we do the matching of target info, scope info.
It's a lot of work as well.
David Ashpole (dashpole) 00:26:35 Yep, yeah, so I think that…
if we were going to do anything there, I would say we, try and instrument the commit method, basically.
With a histogram.
But I also was wondering, like.
In some ways, I'm surprised that Prometheus doesn't include one.
Because Prometheus does the same thing, right? Like, you have scrape duration seconds, and then Prometheus calls commit. I was wondering, like, is commit just trivial in the TSDB? I don't know if anyone knows.
Okay, so then, like, this could also be just, like, a…
Or the other question was, like.
people have been running Prometheus in production for…
a long time, obviously. Like, is this just not a problem in practice? I…
part of me was, like, wondering if I was missing something, but…
Yeah, we can instrument commit, I think, would be a good… path forward.
Arthur Silva Sens 00:27:32 Are you trying to get that, we could implement this in the Prometheus codebase, and then this will be parted here?
David Ashpole (dashpole) 00:27:41 Right, so we already, provide… Like, we already use…
We already get all the self-observability metrics from the Prometheus server as well, right? So… And…
like, this receiver is very much, like, a drop-in… or it's meant to be, like, a drop-in replacement for the Prometheus server, so if we can… if we can have…
like, this implemented in Prometheus and documented as a thing you should care about.
Then that means that there's less of a diff.
between running a Prometheus server and running a hotel collector with.
receiver, right? So… That was, that was more my thinking, was like, We could benefit both groups.
Potentially.
Arthur Silva Sens 00:28:28 If we had a metric in Prometheus for the commit, would that be… would that leave in the script manager?
Package, or would that be somewhere else?
Because we… we don't impart the whole premise, right? Like, just the script manager.
David Ashpole (dashpole) 00:28:48 Good question. I… so… I haven't done enough digging, so it's not clear to me if
Do you know if commit is…
Per scraper? Or is there one commit after…
I scrape a whole bunch of endpoints.
Arthur Silva Sens 00:29:07 Commit… commit happen… is a… is a function from the storage… storage appender interface.
David Ashpole (dashpole) 00:29:15 Right.
Arthur Silva Sens 00:29:16 And commit happens in scrape, and remote write, and other places for mixes.
David Ashpole (dashpole) 00:29:22 I can think of a few different solutions. One is, if you actually click on that link that I put in there.
So if you scroll up, the next thing you see is commit. So, if we swapped the order of those two defer functions.
Then scrapeDurationSeconds would simply tell you about how long it took you to commit.
So one solution is, don't introduce a new metric, just swap these two, and now we have a complete end-to-end latency
For scraping and committing.
So that's, that's one, like… Cryo, you want to interrupt and jump in?
krajo Krajcsovits 00:30:02 Yeah, so this is per scrape loop.
Which means it's kind of per target, so I don't know if that's what we want, because…
You cannot add them.
Like, I don't know what that would mean for… 4D.
Receiver.
Arthur Silva Sens 00:30:25 Wait, what do you mean about you cannot add them?
krajo Krajcsovits 00:30:29 Because they run in parallel, these are Go routes, so they're not sequential, so adding them up doesn't mean anything.
So, I don't know what we are trying to measure, and, like… Is it…
What are we trying to measure? That's my question, basically.
Arthur Silva Sens 00:30:46 the time… that Prometheus Receiver takes to do his thing.
David Ashpole (dashpole) 00:30:52 Yeah, so the time between when the scrape starts
And when the data has been passed to the next thing in the pipeline.
Like, that would be ideal.
krajo Krajcsovits 00:31:05 Huh.
David Ashpole (dashpole) 00:31:06 So, today… Yep.
krajo Krajcsovits 00:31:09 No, go ahead.
David Ashpole (dashpole) 00:31:11 Today, scrape duration seconds includes the time to make the scrape HTTP request.
And the time to call all of the various append functions.
That are needed.
For that, for the scraped payload that comes back.
It currently excludes the time to call commit.
After… on the transaction, after all the appends.
So the question… I think… and then commit…
Our implementation of commit is what actually sends it to the next thing in the pipeline.
So the question for this group is…
Do we want to separately measure the time it takes to commit?
If so, should that be done in our receiver, or should it be done upstream?
Or should we ask?
That scrape duration seconds.
be updated to include the time required to commit? Or are there issues with that?
Does that make sense?
krajo Krajcsovits 00:32:19 No, I still don't understand what we're trying to measure, but, maybe I'm still… so…
David Ashpole (dashpole) 00:32:26 It is per target, so it… these come with job and instance labels.
krajo Krajcsovits 00:32:31 Okay, and that's… that's fine, then.
David Ashpole (dashpole) 00:32:33 That's fine. You can still, like.
Ignore the job and instance labels when you, like.
query, and just, like, what's my 95th percentile scrape latency? But you could also, like, be like, oh, for this job.
You know, ignoring it, right, yeah.
krajo Krajcsovits 00:32:51 Yeah, that's right.
Adam Bernot 00:32:53 So… The… the commit is happening, like, locally to the, the hotel receiver, right?
Like, that's… is that… like, is that ever going to be significant, relative to, like, an HTTP request? Or…
That's great.
Arthur Silva Sens 00:33:16 I think so, yeah.
Like, it's a very, like, the commit is doing a lot of stuff.
It's not just sending, it is translating, it is matching keys…
Adam Bernot 00:33:30 Okay.
David Ashpole (dashpole) 00:33:30 it's still probably…
it's not going to be on the order of seconds, which some scrape… which scrapes usually are. So it, like…
My gut reaction when I first read the issue was, like, This is…
You know, not… maybe worth it?
But I can also understand that if…
Like, for example, commit is unlikely to ever, like.
cause a timeout for something, right? It might take, if it was really expensive, like, 100 milliseconds.
Arthur Silva Sens 00:34:03 Hi.
I wrote benchmarks for.
David Ashpole (dashpole) 00:34:06 Oh, yeah.
Arthur Silva Sens 00:34:07 the append… the append methods, append histogram, and commit. If I remember correctly, the commit…
David Ashpole (dashpole) 00:34:13 It's lower than the appends.
is slower.
Kyle Eckhart 00:34:20 -Oh.
Arthur Silva Sens 00:34:22 I, I linked the…
Kyle Eckhart 00:34:23 Well, and I linked the Prometheus Scrape Manager,
Which is where it's doing the… it does look like commit's included in the straight duration seconds, just based on… so the first defer is to call rollback or commit, and then the second defer is to record
Scrape duration seconds.
So I would imagine the first defer runs first, and then the second one, reports the time since start.
David Ashpole (dashpole) 00:34:53 I think.
Kyle Eckhart 00:34:54 Or is it backwards?
David Ashpole (dashpole) 00:34:55 Defer is like a stack, so the bottom defer runs first, and then the top defer runs.
Kyle Eckhart 00:35:00 Got it.
David Ashpole (dashpole) 00:35:01 Yeah, great.
Kyle Eckhart 00:35:02 Yeah.
David Ashpole (dashpole) 00:35:03 Check.
Kyle Eckhart 00:35:04 Thank you.
David Ashpole (dashpole) 00:35:05 Had me questioning.
Arthur Silva Sens 00:35:06 To say so.
David Ashpole (dashpole) 00:35:06 Are there, for a second.
Kyle Eckhart 00:35:09 But I guess, so in this case, right, like, the scrape Manager kind of doesn't have any work to do within the commit. It's just… it's the… the appender that it gets is provided to it.
So I kind of see the, you know, in the Prometheus realm, I can kind of see why they don't include it, because it's… well, it's not necessarily part of the actual, like, scrape loop.
Whatever appender is coming in might have its own metric that governs commit. I can't… I don't… I don't remember what all…
is there. Like, I know in Alloy, we have a special one that has a metric governing it.
David Ashpole (dashpole) 00:35:47 It's good to know. So there is some precedence for us just adding a commit metric.
Arthur Silva Sens 00:35:54 And then it's not upstream, like, if we do a commit match, like, if the commit is already covered by the storage appender.
Like, do we… would we have storage Panda matrix in the receiver?
David Ashpole (dashpole) 00:36:08 Sorry, what do you mean by storage? There's no metric specific to the appender interface.
I looked in the TSDB implementation of commit and didn't see any metrics.
Arthur Silva Sens 00:36:19 Okay, okay, okay.
David Ashpole (dashpole) 00:36:19 I might… may have just missed them somehow.
Arthur Silva Sens 00:36:24 Yeah, then ignore what I said.
I'm so confused, like, what can we say here that can just remove the discussion needed?
Just go to it.
David Ashpole (dashpole) 00:36:38 I think… Like, for this group, I think we have two…
My proposal would be, I'd like to open an issue in Prometheus Prometheus and link to this.
Saying, can we make scrape duration seconds include the commit duration.
That way we have end-to-end.
Exactly what we want.
And let's wait till we're told no before we go and accept some other solution.
Arthur Silva Sens 00:37:09 Alright.
David Ashpole (dashpole) 00:37:09 whistle.
Is that okay?
Or… Sounds good.
Arthur Silva Sens 00:37:13 Good to me.
David Ashpole (dashpole) 00:37:14 Okay.
I see some… some head bobs.
krajo Krajcsovits 00:37:25 It seems a little weird to not include comments.
Because we include opens.
So we already include half of it, basically. And also, like…
I don't remember how it goes, but I imagine that it… does…
count into the timeout for the script, maybe. I don't know.
But it seems weird to not include it.
David Ashpole (dashpole) 00:37:55 That might actually be why it's in… Why it's not included.
Arthur Silva Sens 00:38:02 My guess is just people never realized it worked that way, and just forgot about it. Like, there's no, like, smart thinking on why it's left.
Okay, there are 20 minutes left for the meeting, I think…
we could move on to this pack topic, David, and next… next week, we can put more items in the workable state.
David Ashpole (dashpole) 00:38:42 Sounds good.
So I wanted to… I think there's a… when we talk about Prometheus receiver stability, there's, like.
It does implement
the Prometheus to OTLP portion of the spec. In fact, it's, like, the canonical implementation of it. So…
I think it would be good for us.
Because we implement the spec to try and stabilize at least portions of it, so…
If it's okay, let's see, can I share my screen? I can't.
I haven't opened an issue, but I'll do that after this meeting, if that's alright.
And reading through this, I actually don't think Can people see?
Arthur Silva Sens 00:39:37 Yes. I don't think it's that crazy for us to start considering stabilizing some of this, so…
David Ashpole (dashpole) 00:39:43 If we look at just the Prometheus to OTLP portion of the spec.
We don't change the name by default. We do have a, without suffixes configuration documented here.
We do have a… I don't think there's a ton of…
dissent about how we handle Unit today.
Other than… Ideally, we wouldn't break too many people.
Help and type are also not that crazy.
And then most of our other specs, I think maybe we could consider leaving info and state set.
as, experimental, if we wanted, just because…
I don't even know if we get info or state-set metrics in the appender today.
Arthur Silva Sens 00:40:37 Fair enough.
David Ashpole (dashpole) 00:40:40 the only… and then the only other spec that I'm, like, mildly concerned about…
is potentially the native histogram one, but even that, I feel like, has been pretty stable.
We do need to update this.
Arthur Silva Sens 00:41:00 makes me concerned as well is that we have… I think we discussed this in the collector SIG call. There is one spec
that controls all protocols. Remote write, Prometus text, protobuf, open metrics.
And they are all a little bit… different.
And we might want to do different things depending on the format.
David Ashpole (dashpole) 00:41:23 I would love to split this up into different specs.
Okay.
Arthur Silva Sens 00:41:32 and I have…
krajo Krajcsovits 00:41:33 What, what, sorry.
Is that because of the created timestamp, or what do you mean? They are slightly different? Because, at least in Prometus.
We don't differentiate them. We have one parser API, and…
The script code does not know.
What protocol the data comes from.
Arthur Silva Sens 00:41:54 But we transformed them differently, right?
like, for AI, creative timestamp is one of the examples.
And I think… once, OpenMetrix 2.0 comes up.
there's also… there might be differences as well that I cannot remember right now. Maybe…
I'm just too worried without… Anything to back… back up my arguments?
krajo Krajcsovits 00:42:21 Yeah, I think we should discuss this, because I don't believe it's a good idea to make it even more complicated. Like, I'd rather fix issues in the code if we have them.
Then… then make people… you know.
try to figure out which one to apply. Like, I think this single…
definition served us very well, so I don't think we should make it, you know,
Depends on the protocol.
Arthur Silva Sens 00:42:48 I… Info, I would love to keep this experimental. I'm…
I'm planning changes to the info that I…
I still haven't come up with, but
I… I want to change the infometrics.
David Ashpole (dashpole) 00:43:03 Okay.
I think?
What I'd maybe like to do to start is I'll put up a PR,
just to stabilize the portions of this spec that I think are very non-controversial. And we can see how close we can get to that. So if it's, like.
we could stabilize this counter section. It…
I don't know if it needs more detail, but we're not going to not do that, right? Like, so, if we can get it to where we're discussing the, like, two or three sections that are unstable, that we need to stabilize the receiver, I think that would be a better place to be than where we are today, where the whole document is
experimental.
Does that sound reasonable?
Arthur Silva Sens 00:43:46 Yeah, yep.
David Ashpole (dashpole) 00:43:47 Okay.
Arthur Silva Sens 00:43:48 I think there is prior… there are other parts of the spec that is split between stable and experimental, right? Like, you can just.
David Ashpole (dashpole) 00:43:56 This can definitely be status mixed.
Arthur Silva Sens 00:43:58 Correct, correct, correct.
David Ashpole (dashpole) 00:44:00 And that's fine.
Arthur Silva Sens 00:44:04 Okay, sounds good to me.
David Ashpole (dashpole) 00:44:05 Okay, great. I'll have that ready.
Arthur Silva Sens 00:44:07 Chocolate.
David Ashpole (dashpole) 00:44:08 Yep.
Arthur Silva Sens 00:44:09 Talking about the spec, I remembered that I have a PR,
that I went… that went stale and closed without merging about the scope info metrics.
David Ashpole (dashpole) 00:44:22 Okay. Yeah, scope is definitely…
Arthur Silva Sens 00:44:29 Hi.
Are we sure that the… are we sure that the receiver implements the host pack?
Because, like, this copay, we don't.
Yeah.
David Ashpole (dashpole) 00:44:40 Yeah, yeah, so,
You're right, we probably shouldn't stabilize it without an implementation of it. But we… yeah, so we should resurrect your PR.
Let's go here.
Arthur Silva Sens 00:44:55 Hi, this PR gives me nightmares.
But yeah, I can redirect it.
No problems.
David Ashpole (dashpole) 00:45:10 The only other, maybe, discussion topic is… so…
Right now, we have target info on by default.
arthur, when we've discussed this, I think, in the past, you…
Are not comfortable stabilizing target info as part of that.
Arthur Silva Sens 00:45:29 No.
Yeah, not at all.
I…
David Ashpole (dashpole) 00:45:36 I think we'll need to start… we'll need to figure out how we can…
like, it also would kind of stink to turn it off by default and break everyone, because a lot of stuff has been built on it. So, it's like, we're gonna have to figure out how we can go stable, and whether we want to stabilize that in some form, or whether we…
It would be nice as well to, like.
understand your concerns. So I don't know if…
Arthur Silva Sens 00:46:01 I think the target info is a great abstraction of a Prometus target.
David Ashpole (dashpole) 00:46:07 And, like, in a pool model.
Arthur Silva Sens 00:46:10 It doesn't translate well for push, in my opinion.
And, like, But it's complicated to explain, that's why I'm trying… I don't want to discuss much… But I…
Talking with Brian and Bjorn.
they… like, Brian is more… Direct, he says.
This target info, they put in this pack while nobody was looking, and now we're struggling to get a… to remove it, but…
It shouldn't be there.
David Ashpole (dashpole) 00:46:43 You mean in the open metrics spec?
Arthur Silva Sens 00:46:46 Yeah, yeah, the spec that you just showed.
David Ashpole (dashpole) 00:46:49 Oh, the… Well, the target info,
We did that because… originally because it was in the open metrics spec.
Arthur Silva Sens 00:46:59 Oh. Oh, really?
David Ashpole (dashpole) 00:47:00 I didn't.
Arthur Silva Sens 00:47:00 Development metrics, target, info.
David Ashpole (dashpole) 00:47:02 Yeah, yeah, I'll show you.
So we're like, what should we name this metric that's gonna have all the resource attributes? And…
Open metrics…
Arthur Silva Sens 00:47:21 If present, an infometric frame called target for the supporting target metadata in both push-based and pool-based systems section below should be first. Interesting.
David Ashpole (dashpole) 00:47:33 Yeah, so that's… I promise I didn't invent it.
Cryo?
Arthur Silva Sens 00:47:40 Cryo?
krajo Krajcsovits 00:47:42 Yeah, I guess right now it doesn't…
Make a ton of sense, but with entities, you could… Make use of it.
I bet you already thought of that, okay, never mind then.
Arthur Silva Sens 00:47:54 I don't know, I think that I fought it, but I never said that out loud. But, yeah, I agree with you.
I think…
krajo Krajcsovits 00:48:01 Nope.
Arthur Silva Sens 00:48:03 Yeah.
krajo Krajcsovits 00:48:04 So, basically, right now, as David said, we shouldn't break everybody in the world, so it's kind of a status quo.
having it, you know, experimental or whatever in the spec right now makes sense, but yeah, I wouldn't break everybody either.
David Ashpole (dashpole) 00:48:23 Well, like… I guess that's what I'm trying to call out, is…
One of the new rules in…
or that OTEL is trying to push is that if you're a stable component, you don't turn on experimental things by default.
So we can… it's like, choose two. You can be stable, you can have it on by default.
Or you can have the spec be unstable.
So that, yeah, that's all I'm calling out, is, like, this question is coming, and we should, at least think about it, maybe open an issue.
I'm… I'm personally…
I personally feel that Target Info is de facto stable, and that we should find a way to stabilize it in a form that we can live with long-term.
Even if it's… even if we want to… Promote other ways of… Exposing resource attributes.
But, I'd like to understand the… Yeah, I…
if there's technical reasons why we don't like what exists today, then I would love to better understand it. Or, like.
If there's other ideas for how to handle it.
Because promotion… promotion's the only one I've heard, and that…
You know, like, we're even starting to build info, the query thing around it, so…
Yeah, it feels hard to break at this point.
But, go for it, Cryo, and then Arthur.
krajo Krajcsovits 00:49:51 Yeah, I mean, I don't really think it's a technical issue. As you say, people establish usage of it. It's more…
That you cannot really… You know, break this tension that
but we put them into resource attributes that should be identifying, but the stuff coming from IFO is not identifying most of it, so, like…
I don't think it's really technical, so I'm sure we can work something out.
Arthur Silva Sens 00:50:22 Yeah, I… I agree, it's not a technical problem. There's…
I feel like target info doesn't translate the semantics very well.
And there are, for example, if a database is…
is pushing OTLP to Prometheus. A database is not a service.
It doesn't have… service instant ID doesn't have
surface, namespace, I don't know, other service…
Resource attributes, and this… and the way…
Prometheus matches the target info with the… with the metric is with the service instance ID attribute, and then you don't… like, it just doesn't work.
David Ashpole (dashpole) 00:51:10 So I do want to call out that we're only talking about stabilizing the Prometheus to OTLP side of this.
So, that might… It's possible that makes our lives slightly… Easier.
Or…
Arthur Silva Sens 00:51:24 Okay, so we don't… we are not talking about push at all, yeah, makes sense.
David Ashpole (dashpole) 00:51:29 It's still helpful to discuss, maybe, problems with target info in general.
Like, if we could say that we will continue to respect target info metrics that we receive.
That's, like, the stability statement that we would have to.
Arthur Silva Sens 00:51:43 Got it.
David Ashpole (dashpole) 00:51:44 Right?
Arthur Silva Sens 00:51:45 Yep.
Now, another thing that I… makes me want… Makes me worried is that entities is not…
Widely used. It's actually not used at all.
And if we have a stable…
Prometus to OTLP, and then OTLP have entities, but entities is not on this pack.
Does that mean that we'll never translate things to entities?
David Ashpole (dashpole) 00:52:13 I've thought about that a little bit. It's like…
It would, like… I think we could do it in a way that's effectively non-breaking.
So, like, let's say that… I'll throw out a design that
I had in mind once, but that may or may not happen, right? So let's say that we eventually decided that Prometheus exporters were going to take entities and use them to produce an OTEL entity infometric.
Right.
Like, that's… that's the decision we went… like, let's say that's what we decided.
Arthur Silva Sens 00:52:51 Yep.
David Ashpole (dashpole) 00:52:53 It would, in a sense, be breaking if we started producing that metric in exporters.
And then… like, a year later, on the Prometheus receiver, started adding
special handling for the metric, where we drop it and integrate it in entities directly, because then the met… like.
We used to put it as a regular metric, and now we're putting it as the entity itself, right?
But if… if, when we introduce this new concept, we first implement it in the receiver.
and then implemented in our exporters later, I think that reduces the chance of that being, like, a breaking change. Does that make sense?
Arthur Silva Sens 00:53:33 Like, it's almost never-breaking for the receiving part of the thing.
David Ashpole (dashpole) 00:53:37 To implement new handling for a special metric that we just invented, because hopefully nobody was already producing
That special metric name or something. So, I think, like, we could… we can evolve.
It might be… it might be tricky, because someone may also use a really ancient collector version, and then upgrade.
After they have the hotel info… entity info metric, right?
And then break at that point.
I think we can do it.
Arthur Silva Sens 00:54:09 Yeah, we are not, like, entities are an addition to the protocol, it's not changing I…
Today, without entities, we populate the resource attributes. Once entities are out, we will continue populating resource attributes the same way.
There's just an additional object that is the entity ref.
David Ashpole (dashpole) 00:54:30 Yep.
Arthur Silva Sens 00:54:34 Yeah, it makes sense. I think it's not gonna break anything.
Okay, cool.
So I guess it's easier than we thought.
David Ashpole (dashpole) 00:54:47 Whoa.
we have to be careful, but I…
My hope is that there's a path forward.
But we can work through the details one piece at a time.
Alright, 5 minutes left. Anything else people wanted to… Bring up…
krajo Krajcsovits 00:55:10 Yeah, I just wanted to add… that,
This is going to be run by projects for the next quarter.
To help stabilize.
the receiver.
So…
for sure it will get to my, like, reporting or whatever next week, but, I haven't had time to actually start on it, so, hopefully next week, because I have, like, two other projects that
are ongoing as well.
So… Yep.
Arthur Silva Sens 00:55:45 We just had that, yeah, awesome.
krajo Krajcsovits 00:55:48 Yeah, so actually, like, if you have a suggestion of what I should start with, then don't hesitate to DM me or something.
In the… in this list of items.
Arthur Silva Sens 00:56:02 Let's see…
I think, one, that it's gonna be very hard
What that means, if we look at it first, maybe we finish on time? There is no deadline, but yeah. The config coverage?
David made a suggestion that we remove
most of the service discoveries by default, and let people add discovery… service discovery in another way.
I think that would be hard.
David Ashpole (dashpole) 00:56:38 Yeah, this would not affect
the core and contributions. So, let me first say the reason for it. It's been, like, a long time thing I've wanted to do, so if we want to exclude it from stability.
I may have to… I'll be a little sad, but it's okay.
I know that…
GKE tried to use the collector a while ago, and still uses it for a few things, but…
One of the things they ran into is that if you want to run the collector and have like…
A very low default memory footprint, if you're not doing too much.
The Prometheus receiver, because of just the number of things it pulls in in its dependency tree, uses a bunch of memory and makes the binary bigger. Mostly the memory was the concern. So…
They wrote a script.
That copies everything to a vendor directory, and then, like, deletes.
The service discoveries in order to work around this.
But it would…
It's like, I would love if there was a way to build a collector distribution that didn't include, like.
You know, one of the… service discovery implementations that nobody cares about, right?
I remember there being… A wide variety. I don't know. I'm getting some faces.
krajo Krajcsovits 00:58:00 So, you're… I mean… thing that comes to mind is build tags for Go.
Like, it's literally a build problem, so if you have build tags for the…
services queries, would that work? I don't know, maybe, yeah, I can try that.
David Ashpole (dashpole) 00:58:14 Not a bad idea, actually. That was… the only other thing I had thought of was, like, oh, we'll put… because the service discovery is based on an import statement, so you import…
you know, it's like an underscore import, and then the init function registers the service discovery. So, it's like, I was gonna have to make an extension called, like, Prometheus Service Discovery or something, that includes one import statement.
That people can pull in. Because all I want is that the OpenTelemetry Collector Builder, at that point in time, people can, like, decide which ones they want. But a build…
tag might work just as well.
I don't know if OCB… Has an easy way to pass build tags.
krajo Krajcsovits 00:58:58 Yeah, I don't know. But, yeah, we should…
not now, but maybe we should talk about your idea as well, because I'm just speedballing here, like, this is…
David Ashpole (dashpole) 00:59:07 I would hate to have an extension that I maintain that's, like.
krajo Krajcsovits 00:59:10 Okay, okay, never mind that.
David Ashpole (dashpole) 00:59:12 It was like… Me grasping at straws.
So, if there's any other way, other than, like, confusing the heck out of users, and then starting to see extensions, Prometheus service discovery sprinkled everywhere, for good luck, then I'll take that.
Arthur Silva Sens 00:59:29 If you go with build tags, we need to change this upstream as well, right?
krajo Krajcsovits 00:59:34 Yeah, yeah, yeah.
Arthur Silva Sens 00:59:35 We need to put the tags there.
And we need to change all the… all our build pipeline as well for Prometheus.
David Ashpole (dashpole) 00:59:43 I… you can…
it… you will have a default, though, right? Like, the default can still be that if you build with no tags.
then it just builds in all the service discovery, right? So this is just, like, oh, a special way to build without this big import.
Thing, right?
Arthur Silva Sens 00:59:59 suit.
David Ashpole (dashpole) 00:59:59 I don't… I don't know if the… Do you know if…
cryo, if, if you use a build tag, Doesn't import something anymore.
if… That then… hopefully that would then no longer end up in the final binary, right?
krajo Krajcsovits 01:00:16 Yeah, I think so, but again, I have to try. But you're right that you can do default to include everything, and then…
like, use the not… so you can have logic there. Like, basically, I need to try it out, so I'll put it as a first thing to take a look at. Maybe… maybe it turns out to be easy, like, I don't know.
Like, I'm not such a big wizard with Go.
Which is kind of crazy, because I've been doing it for 4 years, but, like.
There must always be more important things than diving into, like, for example, biotanks.
So, yeah, okay, I'll take a look.
David Ashpole (dashpole) 01:00:48 Now you finally have your chance. Alright.
On that note, I'll let everyone go.
Arthur Silva Sens 01:00:53 It was rare.
David Ashpole (dashpole) 01:00:54 But, good to see everyone.
Arthur Silva Sens 01:00:57 Bye-bye.
David Ashpole (dashpole) 01:00:58 Thanks.
