SIG: Python SIG
Date: 2026-01-15
Duration: 37 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 02:10 Hello, everyone.
**Dylan Russell** 02:15 Blue.
**Riccardo Magliocchetti** 03:04 So, looks like… looks like this will be, like, a quick one.
Don't have any topic yet.
So, if you want to discuss anything, feel free to… To add them to the agenda, please.
And of course, welcome to this week's Python Week Recall.
**Liudmila Molkova** 04:16 Hi, everyone.
It seems the notes has moved to a different location. Would anyone mind if I update the calendar invite to point to the new one?
**Riccardo Magliocchetti** 04:43 Yes, please. Sure.
Where did you find the order?
Location?
**Liudmila Molkova** 05:00 Sorry, if I go to OpenTelemetry Calendar.
There is a meeting notes link there.
**Riccardo Magliocchetti** 05:05 Oh, okay.
Yeah.
Yes, thanks.
Boom.
Welcome again to this week's Wiggly Call.
We're waiting a few more minutes for more people to join.
And… And for some topics to be added, since the agenda's still empty?
Okay, so 5, I think we can start.
So, welcome again to this week Python, Sig, call?
We have the… First topics?
Okay, Redeem asking for reviews.
on a bunch of PRs.
**Ridhima Satam** 07:05 Yeah, so I presented these two PRs. One is the Langchen, instrumentation, using the utils. I spoke about it last, Tuesday, this Tuesday, and the LLMSIG, and then there is workflow PR, so I just, wanting some, eyes on that.
**Riccardo Magliocchetti** 07:32 Thank you.
Any comment?
**Ridhima Satam** 07:38 Right now, there is nothing to discuss. As such, there is no concern yet. We are just asking for reviews.
**Riccardo Magliocchetti** 07:47 Okay, thank you.
Thank you, so I don't Okay, my next topic is from a medium.
**Emídio** 08:02 Hey, This PR is not mine, but I have been reviewing it very closely. Yeah, it's basically to fix a bug when we try to export.
to HTTP endpoint, and let's say, like, the collector is down.
And… we don't, catch into the hit right loop.
GitHub. Yeah.
**Riccardo Magliocchetti** 08:33 Yeah, sorry.
**Emídio** 08:37 I don't know, like… yeah, it's not… it's not loading for me anymore.
I'm gonna have a look.
Oh, wow. Yeah, it seems so…
**Riccardo Magliocchetti** 08:58 Okay, bad timing.
**Emídio** 09:00 Yeah.
But yeah, I already approved the PR, so… If you… anyone can take a look.
Later.
I think it's, it'll be nice to have this fixed.
**Riccardo Magliocchetti** 09:19 Okay, thank you.
I will try to take a look tomorrow, if you have notes.
Alright, thank you.
Okay, now it's loaded.
**Emídio** 09:44 Yeah, it basically is… basically inside in the… That's why… Catch on the… when exporting.
Before, when you retry, it doesn't get into the retry loop.
So now, when… with this PR, we get into the hit right loop, which is… which is pretty much the bug.
**Riccardo Magliocchetti** 10:33 Okay.
So, I'll take a look tomorrow.
And I've seen that also.
We have Aaron already.
Did some reviews?
**Emídio** 10:49 Yeah.
**Riccardo Magliocchetti** 10:56 What's the deal?
**Dylan Russell** 10:57 Yeah.
I looked at it, I thought it looked pretty good.
Like, you can see here, there's… like… If it fails to, like, connect to the… like, I guess the collector in this case, it would throw an exception. We wouldn't catch that.
**Emídio** 11:18 Go.
**Dylan Russell** 11:19 So… This is just catching the exception, and… Retrying it.
**Emídio** 11:27 Correct.
**Dylan Russell** 11:28 Ew.
Yeah, so it seemed good to me.
**Riccardo Magliocchetti** 11:43 Okay.
And… yeah, this was the last topic, and GitHub isn't helping.
Any other topic you want to discuss?
**Liudmila Molkova** 11:57 I maybe wanted to chat with you recording about Weaver. We didn't talk, we didn't have a chance to discuss last time, and I didn't realize that you have messages on Slack. So, if you have time now, maybe we can, we can chat now.
**Riccardo Magliocchetti** 12:10 True?
**Liudmila Molkova** 12:13 Yeah, so… Yeah, go ahead.
**Riccardo Magliocchetti** 12:17 No, no, go ahead, go ahead, go ahead.
**Liudmila Molkova** 12:19 You had your prototype, and you had some ideas about how to scale it to other instrumentations. Maybe you can show it, and you can show the issues you have, if any… Sorry for putting you on the spot.
**Riccardo Magliocchetti** 12:41 Yeah, no problem. Let me see, We have a radio request.
**Liudmila Molkova** 12:58 Did she sort of ball?
**Riccardo Magliocchetti** 13:04 Okay, let me check… So, this is… Like, I worked on this, like, a couple of days last week.
And the idea, was to… End-to-end test the telemetry we send out of our instrumentation.
So, my plan was to recreate a bunch of, simple applications.
I started with the Flask one. Yeah, you have also a fast API one, but I haven't tested that.
And… The idea was to use, Weaver as a OTP gRPC receiver, and leveraging its, what they call, like, the registry life check.
Which is, like, the ability to, check whatever is ingested against, a registry or a… Semantic convention in practice.
And… Yeah, like, the issues… Like, first of all, I tried to leverage, Ludmila, yours, with a container, but I found that, Like, it was, like, not… Again, since you… also, you did, like, a proof of concept.
was, like, not generic enough for me. Like, I kind of assumed that you passed a specific configuration, but, like, that's fine. And so, like, I… just, like, since I didn't have much time, I just moved to… Using Popen to call it, The… and communicate with the… Viewer process.
And… Yeah, like, a fond of… bunch of issues, on Weaver, like.
The tablets are kind of open.
Later, the… We have an issue tracker.
But, yeah, like, what I've done, different from you, it's just… Like here, I'm not unit testing.
Again, I'm just shelling out a process, wrapped by our auto-instrumentation wrapper.
And… yeah. With that, my test is… just a bunch of calls to the… to Flask app, in this case.
One for, 404, one for, 200 response?
And, like, in this example, I'm using the output as, to, like, to write the report about the… The data it received on disk, on a file.
But I, like, I think there is, like, a risk condition when you send both metrics and traces, and the matrix overrides the traces report.
**Liudmila Molkova** 16:16 Oh, seriously? Oh, okay.
**Riccardo Magliocchetti** 16:17 Yeah, at least this is what I see.
And… and yeah, so this is just select.
my proof of concept. The outcome of this is a couple of issues inside our instrumentation, one in Flask.
Where we have, like, when we have the stable somatic convention, we are sending a metric using the unit and description of an older one.
But I think someone already opened up PR.
and my doubt on fixing that is, do we care of keeping the metrics, when not setting the stable HTTP semantic convention.
like… Do we care of the, like, the older schema version of the metric?
Otherwise, like, it should be trivial to fix.
And the other one is, an issue I've found, like, that we've found on… An attribute, what was wrong?
And the fun part of this is that… This was in a system matrix in the Python GC matrix.
And so, like, since I contributed the Python ZC metrics, it's fine for me, like, I missed the additional review.
But, like, we were using, like, the wrong attribute for specifying the generation. Wrong attribute and type of the value.
But I already created IPF for that that was merged.
No.
Let's see if we can open the… Cuiva?
Are you?
**Liudmila Molkova** 18:06 I'm not sure if you're sharing. I see the OpenTelemetry Python contribute your work.
the… Just the root of the repo.
**Riccardo Magliocchetti** 18:18 Oh.
Okay, so maybe it's not working. Let me share again.
Can you see it?
**Liudmila Molkova** 18:35 Yep.
**Riccardo Magliocchetti** 18:36 Okay.
So I filed a bunch of issues. One is the one… I already mentioned.
That is, if I send traces and metrics, I only get metrics only when I use the… the output profile.
I don't know if it's something strange on the stuff I sent, but… Like, if I disable the matrix, I get the traces. If I enable both.
And the matrix, gets sent after the trace. I got totally matrix.
Yep.
**Liudmila Molkova** 19:13 Okay, interesting. I didn't notice it, but okay.
**Riccardo Magliocchetti** 19:18 And the other one is, since I have issue with this output, I was wondering if maybe like, just reading from the standard output of Weaver will be enough.
**Liudmila Molkova** 19:33 Oh, no.
**Riccardo Magliocchetti** 19:35 At the moment, it's sending, like, a JSON, like, pre-printed.
That's true.
Kind of annoying to parse that.
Like, you have to read line by line, and keep into account, like, when the objects are.
But, like, it's… I think, I played a bit with this, earlier today, and it's trivial to create, what is it called, like, new line delimited JSON or JSON line exporter, but is, again, just by, like, providing the templates, what is not pretty printing the JSON is enough.
But I still have to open the PR, but I tested it locally and seems to work fine.
**Liudmila Molkova** 20:20 Yeah, I mean, we should fix the converter, for sure, yeah.
**Riccardo Magliocchetti** 20:24 Yep.
And when other issues are reported, is that, now that I get all the metrics, I noticed that sometimes, like, for some attributes.
We will suggest, like, a random one, replacement. For example, Visuals.
I don't remember which metrics it was… Okay, this was, like, a system network connection metric?
And, and it looks like there is not a state attribute anymore.
And we were suggesting to use, DB Cloud.
**Liudmila Molkova** 21:05 Yeah.
**Riccardo Magliocchetti** 21:08 I think, like, the name is similar, but I don't think it's the same thing.
**Liudmila Molkova** 21:12 It's not, so I think what happened is that we used to have the state attribute, which was used on different metrics and meant different things, and now in semantic conventions, we documented that it's renamed to something.
something… one of those things. So maybe the fix is in the semantic conventions to actually, change the reason to obsolete it and remove the confusing node, because it's… Not clear, yeah. I'll… yeah, let's keep it in view where I'll probably transfer it to semantic conventions.
**Riccardo Magliocchetti** 21:47 Thank you.
**Liudmila Molkova** 21:48 Yeah.
Yeah, go ahead. I have some questions, but go ahead.
**Riccardo Magliocchetti** 21:53 I'm not sure. This is it.
**Liudmila Molkova** 21:57 We're… yeah, I will try to do my best and deliver, and fix the stuff.
I… I'm curious… how do you think about POPEN versus Docker? What do you… care? Like, do you think Docker is necessary by any means?
**Riccardo Magliocchetti** 22:22 I don't think it's… It is necessary.
And… but, yeah, if it's more… like, I think it… like, if it's easier for people to run it with Docker, it's fine for me to move to test containers. Like, it's not an issue.
Like, for me, since, like, I wasn't able to use the output.
And I really needed the standard out.
I guess, probably VPopen is a bit easier to get that done.
**Liudmila Molkova** 22:59 Yeah, it's just less of a… so the only difference I see is that Docker essentially comes with Ubuntu, you don't need to install Weaver to run it, but it's easy to install a tool in the CI check anyway, so… I think it's a good feedback that… that doc… and an extra layer, right? That's the extra thing that can go wrong.
**Riccardo Magliocchetti** 23:24 Yep.
**Liudmila Molkova** 23:24 like, the problem you had was not shutting down Weaver properly, and that you had the same container name, being reused, and the conflict there. It's one of the things.
So, Let's see, and then… okay, let's say we would, USP open. Let's say Weaver reports everything you need in the… I had an issue, and I think you commented on this, that we should… that… that Weaver should report… return the report when you stop it.
And if it, let's say, had some runtime errors and validating some signals, then it should also report it there.
So, you would only need a STD error or STD outlet for the errors if things went wrong, for the, like, completely wrong. You misconfigure it with or couldn't start or something.
**Riccardo Magliocchetti** 24:28 And…
**Liudmila Molkova** 24:29 You would, Get the JSON response and return from HTTP's top API.
It would solve… and if it… if there were no risk conditions, it would pretty much solve Other problems, is it right?
**Riccardo Magliocchetti** 24:53 I don't know about this, like, this will be helpful for us too, but I'm not sure it will solve the matrix versus trace risk condition.
**Liudmila Molkova** 25:04 Yeah, I mean, if it… yeah, if it worked, if the race condition would… would… you wouldn't need, like, JSONL STD output, because…
**Riccardo Magliocchetti** 25:13 Yeah, exactly. Yeah, yeah, like, all the, like, we have different options, like, create another sport, or… fix the output, or provide, I mean, like, to… return the report inside the HTTP response of PCPI. So, like.
**Liudmila Molkova** 25:31 Yeah.
**Riccardo Magliocchetti** 25:32 Whatever works, it's fine for me, like…
**Liudmila Molkova** 25:36 Yeah.
Okay, so then… Imagine these parts worked. You would run this in… the integration test, it would be a Flask, let's say, application doing something else, like HTTP outgoing, gRPC, I don't know, database calls, things like this.
**Riccardo Magliocchetti** 25:57 Isn't the case?
Yeah, well, my plan was to create one test application per instrumentation.
**Liudmila Molkova** 26:05 Yeah,
**Riccardo Magliocchetti** 26:06 So, like, it's easier to find out where the issue is.
And, like, my idea was, like, when people is proposing new instrumentation.
At least we have, like, a check that is more, on point than usually humans on… the stuff, like, respecting the semantic convention. Like.
having, like, an automated check will also be useful, because I think, like, Tammy opened some PR, on implementing the stable HTTP some call for some HTTP server instrumentation.
And, like, I think there was a comment that… from a media thing, but it was saying, like, I don't remember… like, it's been a while since I read the HTTPS spec, so I may be… Like, there was, like, some issue about, like, an attribute also being, yeah, present in the stable, or just another one. And, like, having something like this would, like, solve all the issues.
**Liudmila Molkova** 27:10 Right.
**Riccardo Magliocchetti** 27:10 Like, I know most of the dubs, yeah.
**Liudmila Molkova** 27:13 Most of them, yeah. So… one per, instrumentation, it's still maybe a few calls, I don't know, if it's an HTTP client, that's sync and an async, and maybe… A few variations.
Or is it just one?
Scenario.
**Riccardo Magliocchetti** 27:37 Oh… maybe, I think, one scenario for instrumentation, otherwise this will take, like, quite a bit.
**Liudmila Molkova** 27:50 Yeah, I mean, we can start with one. It's just if there is a sync version of API and async, and the instrumentation is slightly different for them.
**Riccardo Magliocchetti** 28:01 Yeah, yeah, yeah.
**Liudmila Molkova** 28:04 Probably should call both, and…
**Riccardo Magliocchetti** 28:06 Yeah, yeah, but, yeah.
Like, I… I don't know if you have any… Yeah, maybe the database instrumentation, I have a sync, I don't think much, yeah.
**Liudmila Molkova** 28:22 And there might be other variations, right? So, like.
For Gen AI, there were 3 different types of dispens we could emit, like, tool called the… inference and embeddings, and they're multiplied by 2, there are async things, And it becomes a little bit intimidating, but assuming… we… so I think it's, like, the integration desk, there is a few of them, not a lot of them.
And they tend to be bigger, so we would, not limit ourselves to one test, but it's just we keep the amount of them to the minimum, and we would rather maybe combine similar scenarios together. If there are, like, do you need to make a few requests, then you, you, like.
maybe combine them to one test. I think this is precise enough. I kind of… if you agree that this is the direction we're going, I kind of understand. It makes total sense.
**Riccardo Magliocchetti** 29:33 Well, this is just, like, For me, it was like an experiment.
Yeah, like… my… My goal is, like, to… Reduce the doubt of the quality of the stuff we export.
Because at the moment, I have many doubts. But yeah.
**Liudmila Molkova** 29:57 And essentially…
**Riccardo Magliocchetti** 29:59 No, go right, great.
**Liudmila Molkova** 30:01 And essentially, you are currently blocked on the issues you created, and you cannot move forward with it until they are fixed.
**Riccardo Magliocchetti** 30:09 Well, and not blocked, because, like, we have, like, two weeks a year at Elastic, where we can do some experiment and try new stuff.
And this was, like, my… The issue I tackled for mine, that was, like, last week.
**Liudmila Molkova** 30:32 I see.
**Riccardo Magliocchetti** 30:33 So, like… It's not, like… I can spend a lot of time on this.
But yeah, like, as a background task, I would like to move this forward. So, no hurry from my side, like, I'm not blocked at all.
on this.
**Liudmila Molkova** 30:54 You cannot progress this even if you had time. That's what I meant, because the viewer is… Because of the issue.
**Riccardo Magliocchetti** 31:01 Yeah, but, like, luckily, I work around the issue by implementing, a new line delimiter, just on exporter, but… And so, like, I can create and test the other instrumentation, so… like, now that… you know, the next step for me will be to create, like, more examples, and so maybe see if you get other issues. Because, like, anyway, I cannot put this finger on CI until it's, like, the test passes are passing, so…
**Liudmila Molkova** 31:35 Reliably.
**Riccardo Magliocchetti** 31:37 Yeah, so, like, a lot of work would be also on fixing stuff. For example, like, the system metrics.
He's reporting a lot of, metrics, but are not.
In the semantic convention, so… We need to…
**Liudmila Molkova** 31:51 Yeah.
**Riccardo Magliocchetti** 31:52 Osipation, yeah.
**Liudmila Molkova** 31:54 Okay, so then, It's also not, like, the top priority for me, but I think it's quite important to solve it at some point, to give us all more time.
And I will be working on the background on the… Waiver issues and making it more friendly.
And let's see what we'll end up with.
**Riccardo Magliocchetti** 32:20 And that would be great. Thank you, Mila.
**Liudmila Molkova** 32:24 Yeah, thank you, thanks a lot, it's a great feedback.
**Riccardo Magliocchetti** 32:39 Okay, any comment, or… Any topic?
You want to discuss?
Okay.
So Thank you, everyone.
Ceo.
On Slack, or on the next SIG code?
Thank you.
**Liudmila Molkova** 33:02 Thank you. Thank you.
**Ridhima Satam** 33:03 Thank you.
