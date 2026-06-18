SIG: Community Demo App SIG
Date: 2026-06-17
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**FELIX GEORGE** 00:19 I don't know.
**Donal O'Sullivan** 00:23 Hey, Felix, how are ya?
**FELIX GEORGE** 00:27 I'm good.
Already?
**Donal O'Sullivan** 00:30 Absolutely.
I'd say, I think your PR is probably still in review, right?
**FELIX GEORGE** 00:38 Yeah.
**Donal O'Sullivan** 00:39 I actually… apologies, I haven't got a chance to look at it. I'm gonna hopefully have a look at it tomorrow.
I'm gonna… Yeah, we were, Busy last week, so, just the way the conference would work, so…
**FELIX GEORGE** 01:00 There were some comments in the PR. I think I was… I answered them properly, I assume.
So, yep.
**Donal O'Sullivan** 01:10 Okay, cool.
**Shenoy Pratik Gurudatt** 02:07 My feelings, I don't know.
**FELIX GEORGE** 02:11 tonight.
**Donal O'Sullivan** 02:37 I guess Giuliano's probably on holiday still, is he?
**Shenoy Pratik Gurudatt** 02:43 Yes, pierre did tell that he might join today, that was the last week, but let's see.
Let me add entry to our… Dog.
Yes.
Yep, Felix, you know, to start on your PR? I didn't get a chance to look at it, but I saw, Others, let's take a look.
**FELIX GEORGE** 04:04 Yes, there were some comments, But I try to address all of them.
So, the first one was Juliano. He tried to run it, but, in between, there was some package update from AIO HTTP, which broke the code, then I fixed it, then he was able to run it, basically. Then, there were some comments from key, like, so… so he asked me to convert the requirements.txtv to requirements.in.
Done that. Yeah, then adding the Docker, you know, SHA, Docker image, SHA tags.
That's also done.
So, and there was a question on why I… I have added YAML ignore to the, to the cache, which are, like, request-response files. So, basically, the length of the, each line is exceeding the YAML limits.
But I added it because I thought, this is a machine-read and read code, it's not for really humans or any editor compliance, right? So that's why I added YAML ignore, and it was much easier without YAML Ignore to, you know, write these files.
**Shenoy Pratik Gurudatt** 05:32 Alright, I feel like the PR is coming together. Not sure if… Noel, do you want to take a look, or I can take a look anyways this week, and we can hopefully get this merge now.
**Donal O'Sullivan** 05:45 Yeah, I… I don't mind, Shania. I was gonna add it to, like, my list of stuff to do tomorrow, so I was hopefully gonna just… I was just gonna basically try and run it locally and see how I get on, but Yeah, I think, I think Giuliano and… Keelig have done some good reviews, so… Yeah.
**FELIX GEORGE** 06:05 So, in the other thread that you can see in the, you know, In the initial part of the PR, you can see all the comments that, was raised by Shinoy, in the old PR, you can see, which is in the close date now.
So you can also see that from there.
**Donal O'Sullivan** 06:25 Yep, that's cool, yeah.
**Shenoy Pratik Gurudatt** 06:26 Yeah, I already requested for a ton of changes. Thanks, Felix.
**FELIX GEORGE** 06:30 They can't.
**Shenoy Pratik Gurudatt** 06:31 role of that.
**FELIX GEORGE** 06:32 around that triangle.
**Shenoy Pratik Gurudatt** 06:35 I have some follow-ups, like, the one that Juliano mentioned.
Probably I was thinking we can split out, one with traceloop instrumentation, the agent, and the MCP probably can do the GenAI manual instrumentation, but that all can be, I believe, as a follow-up after we get this initial part merged in.
**FELIX GEORGE** 06:56 Yeah, and I think the most important follow-up should be the load generator, where…
**Shenoy Pratik Gurudatt** 07:01 That's… that's something that you have been planning to do after we get this merged, right?
**FELIX GEORGE** 07:05 So we have… so I have created a list of queries which kind of, you know, generate this diverse set of graphs.
Because, like, each trace can, like, we see it as a graph, right? I mean, so we can get this diverse set of graphs, and, like, many queries can be decomposed into sub-queries, and there are also queries which kind of make… kind of tries to confuse the LLM.
Bye.
Where you get the error response, or, you know.
So, yeah, that's something that I'd like to add.
**Shenoy Pratik Gurudatt** 07:39 What I was thinking with the load generator is to also have subsequent Grafana dashboard changes, so we can view these telemetry signals on Grafana dashboard.
stores are still the same, OpenSearch Jaeger, and we also have Profiler, I don't know if we can get something for Profiler, but yeah, with the Prometheus and these two, we can add…
**FELIX GEORGE** 08:04 It will be metrics, right? The number of tokens, or those kind of token usage, or…
**Shenoy Pratik Gurudatt** 08:09 So even Jaeger is connected to Grafana, that you can query traces, and OpenSearch is also connected, so if you have logs coming in, that can be also viewed in Grafana.
**FELIX GEORGE** 08:18 Yeah.
**Shenoy Pratik Gurudatt** 08:19 all the three signals. So, if you are emitting some of them, all of them, we can create a parallel dashboard, or we already have a dashboard for all services.
**FELIX GEORGE** 08:29 Yeah, yeah.
**Shenoy Pratik Gurudatt** 08:32 So we can update that.
**FELIX GEORGE** 08:34 I love it.
Alerts also on top of.
**Shenoy Pratik Gurudatt** 08:37 We don't have alerts today in the hotel demo, I believe.
No? Yeah.
**FELIX GEORGE** 08:44 Oh, God.
**Shenoy Pratik Gurudatt** 08:45 As far as I remember, we don't, but you can go ahead and add it. I think Cyril did add something, like a basic thing, initial part of the year.
**FELIX GEORGE** 08:52 a number.
**Shenoy Pratik Gurudatt** 08:52 Yeah, I'm…
**FELIX GEORGE** 08:53 I think number of calls, or, you know, some things I remember seeing in the.
**Shenoy Pratik Gurudatt** 08:59 Yeah, yeah, yeah, I think Cyril did add something. Might have forgotten it.
Let me check.
Anyways, so we can add that in the same PR with load generator, is what I'm saying. We have the internal story, you have the telemetry going through, and then we can also view the telemetry.
**FELIX GEORGE** 09:15 Yeah, that would be nice.
**Shenoy Pratik Gurudatt** 09:20 Good.
Yep, we'll try to get this in by Friday. No, I can take a look tomorrow, I can ping others. And I'll create a follow-up issue for the load gen part.
Yeah. And, for the Gen AI normalizer, I have some ideas, so I'll put that as a follow-up. We can split the work between load gen and the other pieces.
**FELIX GEORGE** 09:41 Yay.
**Shenoy Pratik Gurudatt** 09:42 Cool.
Then, we have a lot of open… beers, I think.
Any of them are merged, or… No, it's still open.
**Donal O'Sullivan** 09:55 Yeah, I think a lot of them are just… are they depend bots, or… What are they?
**Shenoy Pratik Gurudatt** 10:00 Yeah, most of them are Dependables.
Let's see.
Oh, I see you left a comment on the telemetry test update, right?
**Donal O'Sullivan** 10:12 Yeah, so, yeah, like, it looks good to me, to be honest, like, I was happy to approve it, but… so I ran the… I set the environment variables, and then ran the telemetry test minimal, works fine, and then ran telemetry test, just a full one.
And it's great, because, like, it doesn't time out, it just runs through, it doesn't take that long, but, I think it just took a few minutes, but yeah, there is some failing tests in it. I guess maybe that's just my local setup.
**Shenoy Pratik Gurudatt** 10:41 Yep.
**Donal O'Sullivan** 10:42 It's probably just some Docker images that I'm… that I might have to rebuild, or something like that.
**Shenoy Pratik Gurudatt** 10:49 Yeah, let me just take another stab at the response first, before we get the PRN.
I just want to double-check the assertion error that we see here is not a code issue.
**Donal O'Sullivan** 11:04 Okay, yeah.
**Shenoy Pratik Gurudatt** 11:06 So I fixed a couple of things in that pair. One was, you remember, load generator emits out fraud detection and other spans as well, whenever it goes through the API. Those are probabilistic, whereas, like, only 6% of the actual checkouts that happen with load generator go through The fraud detection API that caused a lot of, race conditions where some of the tests pass within 3 minutes, if that fraud detection thing is reached, otherwise it would take forever.
**Donal O'Sullivan** 11:35 Yeah, yeah, just hang waiting for that fraud detection to get triggered. Yeah, yeah.
**Shenoy Pratik Gurudatt** 11:40 Yeah.
**Donal O'Sullivan** 11:41 Yeah.
**Shenoy Pratik Gurudatt** 11:42 And something like that is what I wanted to fix, because I don't want to keep this flaky as the older trace tests that we had.
So… Yep, this looks good, so there is a warm-up prop, which will just run every, run, in addition to what load generator is doing.
So, minor test run of spans and APIs.
Cool. Let me take, one look at your response here, for the failures. Once it is all good, I'll again update the PR.
**Donal O'Sullivan** 12:13 Cool. No, like, it sounds good tonight. Like, I'm wondering… so, it's not running in the… in that PR yet, right? Like, I'd have to approve it for… for that.
**Shenoy Pratik Gurudatt** 12:21 Oh, yeah.
**Donal O'Sullivan** 12:22 Ron, I guess. Yes.
So maybe… maybe I can just approve it, and then we can just see if, like, if it runs into CI… Because I guess it's just, it's building the images from scratch every time, isn't it? So, like, it's taking whatever the current state of the code is.
Yeah.
Yeah, let me… so if… so if you run it locally, it doesn't rebuild all the images, it just takes whatever you have locally and runs them, and then runs the test against them, I guess, is the idea, right?
**Shenoy Pratik Gurudatt** 12:52 Yes.
Also, what I can do is I can update the branch, so it pulls up the latest main as well, and then it runs all together.
**Donal O'Sullivan** 13:00 Hmm, yeah, maybe, yeah, okay.
**Shenoy Pratik Gurudatt** 13:02 I just clicked on update.
So it'll merge from main, and then once you approve, we'll actually see the latest of latest images being built.
**Donal O'Sullivan** 13:11 Yeah, cool. Sure, I can hit approve there, and let's see it run.
Okay. Let's see how it goes. Cool.
Alrighty.
Alright, I'm gonna approve it there.
So that, that will trigger once everything else is set, I guess.
**Shenoy Pratik Gurudatt** 13:30 Yep.
**Donal O'Sullivan** 13:31 Yeah, thanks.
Yeah, it'd be a nice, a nice change to have some decent tests.
**Shenoy Pratik Gurudatt** 13:39 Yeah, I'm getting more confidence for the Dependabot PRs now.
**Donal O'Sullivan** 13:43 Hmm.
Yeah, there… there is quite a lot of them.
Yeah, if we have this, then we can just, like, oh, if it passes, just merge it.
**Shenoy Pratik Gurudatt** 13:56 Yeah.
**Donal O'Sullivan** 13:58 Cool.
**Shenoy Pratik Gurudatt** 14:01 Yeah, I don't have any other item… me today. But, are there any outstanding PRs which are passing on Dependapot, but… not approved. I know Kilik and myself did that… Did some takes on approving some of these.
Not sure who merged them, I think.
I think Juliano or Pierre might have helped to merge them in. Oh, I see. Juliano also merged a lot of these pending PRs from last night.
**Donal O'Sullivan** 14:35 Hmm.
**Shenoy Pratik Gurudatt** 14:36 The only ones pending are minimal approved stuff or actual failing tests.
So once I get my PRN, what I would do is, I'll rerun all the dependabot failing PRs, just to verify those are not failing because of the flakiness of the test, rather some actual issues.
**Donal O'Sullivan** 14:54 Sounds good.
**Shenoy Pratik Gurudatt** 14:58 Cool.
Yep, and there was another PR for the zero instrumentation stuff.
**Donal O'Sullivan** 15:04 Yo.
**Shenoy Pratik Gurudatt** 15:06 Mmm.
This is the one I can put in the chat here.
This one, I took a look, it looked good to me. I did, run it locally. Like, I did run it locally and see the telemetry pop up correctly.
**Donal O'Sullivan** 15:21 Hmm.
**Shenoy Pratik Gurudatt** 15:23 So… This is all good.
From my side.
**Donal O'Sullivan** 15:29 And was it the same telemetry as with the instrument, like, the manual instrumentation, or had it…
**Shenoy Pratik Gurudatt** 15:34 Yeah, it's a bit… it's a bit more, because.
**Donal O'Sullivan** 15:37 Okay.
**Shenoy Pratik Gurudatt** 15:38 For something like resource detection, the auto-instrumentation does everything, whereas previously with the RFJS thing, it was manually specifying it the container resource ID or something like that.
Okay. This is a bit more than what we had already, with auto-instrumentation getting much better now.
**Donal O'Sullivan** 15:56 Yeah, yeah, yeah, it's nice.
Yeah, cool.
**Shenoy Pratik Gurudatt** 16:04 Perfect.
Yep.
I'll have one PR next week, where I'm removing the old race tests.
A lot of spending once this gets stable.
So we don't have to rely on this anymore, the older stuff anymore.
**Donal O'Sullivan** 16:21 Nice.
we have them in our fork, and, like, yeah, they just don't work, so we just have to disable them.
Yeah. So yeah, no, that's good.
Let's get rid of them.
It's always good to be, removing coat.
**Shenoy Pratik Gurudatt** 16:42 Yeah, yeah, yeah, that's usually not the norm. These days, especially when you're adding stuff a lot.
refactoring has taken a step back, so… Yeah.
It's only when humans were doing it, I believe.
**Donal O'Sullivan** 16:56 Yeah, yeah, yeah, yeah, true.
**Shenoy Pratik Gurudatt** 16:59 Yeah, I can navigate through all the dead codes.
**Donal O'Sullivan** 17:02 Yeah, yeah, yeah, that's it, like… Cool. I, I don't have anything for today, anyway. It was just, yeah, I just did some reviews, and… Felix's gonna definitely look at your PR tomorrow.
It's gonna… it's on my list of… my list of items to do, so…
**FELIX GEORGE** 17:22 Thank you.
**Shenoy Pratik Gurudatt** 17:25 I'll update the doc after the meeting as well. You can… Grow up in…
**Donal O'Sullivan** 17:32 Cool.
**Shenoy Pratik Gurudatt** 17:34 Thanks, everyone.
**Donal O'Sullivan** 17:35 See you guys.
