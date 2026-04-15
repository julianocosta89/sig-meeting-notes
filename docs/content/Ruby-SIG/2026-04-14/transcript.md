SIG: Ruby SIG
Date: 2026-04-14
Duration: 71 minutes
============================================================

## Zoom Recording Transcript

Kayla Reopelle 00:02:03 Hey, is this honey?
Bart de Water 00:02:09 Hello!
Kayla Reopelle 00:02:11 Hello!
Bart de Water 00:02:13 Long time listener, first time caller.
Kayla Reopelle 00:02:15 And welcome to the party!
I'm gonna put our meeting notes in the chat.
And I guess I can start sharing my screen.
Let's see… Maybe we'll give one more minute?
Before…
Bart de Water 00:03:00 Yeah, is it okay if I add up an item to the contribib section?
Kayla Reopelle 00:03:05 do. Yeah, that's… That's what it's here for.
Bart de Water 00:03:09 Okay, thank you.
Robb Kidd (he/him) 00:03:12 You can… you can add items to this agenda, anytime, really. You can come to the doc and… and it's… it is both the proposed topics and our note-taking tool when… when we actually start talking about it.
Bart de Water 00:03:25 Gotcha. Yeah, like, like I said, like, first time, I mean, relatively new to OTEL, first time actually jumping on this call, so just getting, still getting a sense of the, unwritten rules.
Robb Kidd (he/him) 00:03:38 Sure.
Kayla Reopelle 00:03:39 Yeah, no problem.
Robb Kidd (he/him) 00:03:41 Was the root.
Kayla Reopelle 00:03:41 Excellent.
Robb Kidd (he/him) 00:03:42 It's very friendly.
Kayla Reopelle 00:03:44 We hope so, hold us to it. Let us know if we're not.
Bart de Water 00:03:48 You'll know when I'm back next time, we're not.
Kayla Reopelle 00:03:55 Okay, that's more folks here… I know we don't have Ariel today… Oh, yeah. I think… is everyone ready to go ahead and get started, then?
Cool. Yep.
Alright, so, I went to the specs… the spec thing today, and… There are a lot of things people wanted to talk about, so many things that the agenda for the next meeting is pretty much already set and ready to go. For this particular meeting, one OTEP that I think folks might find interesting is this Policies OTEP. It's a new proposal for how we could kind of configure anything in a more global way. The thing that kind of clicked it together for me is that it sounds like it gives a way to apply metrics views to any other element of OpenTelemetry.
it's, it's a really big proposal, and, it is being actively discussed, But, yeah, it's kind of like something that would exist in parallel with configurations, so that you could have more specific policies. There were some really great examples that people were looking at.
Unfortunately, I don't know where… Where they had them.
That's not quite what we want.
Yeah, but I guess, just at a high level, you know, if you're interested in the future of configuration with OpenTelemetry, I don't think this will replace declarative config, it seems more like another way that you could take care of things.
highly recommend checking this out. If you've also found limitations with the way configuration works right now, and there's more levers you want to be able to pull, I think this would be another great place to… Chime in.
Robb Kidd (he/him) 00:06:20 And we haven't attempted declarative config implementation yet, right?
Kayla Reopelle 00:06:25 Correct, yeah, we have not yet.
Robb Kidd (he/him) 00:06:27 Wishlist.
Kayla Reopelle 00:06:28 Yes, yeah, I think once metrics and logs are a little more stable, we'd probably move on to that next, unless we have a person who's really interested in spearheading it.
Robb Kidd (he/him) 00:06:40 It is of interest to us.
Kayla Reopelle 00:06:43 Okay. But… Cool.
Robb Kidd (he/him) 00:06:45 I don't want to put any carts before horses if, you know, declaring a config for signals that aren't Yeah, landed.
Kayla Reopelle 00:06:52 I mean, you could skip those signals and focus on tracing, like, we could find a way around it, if it's something that you have time to work on. Yeah, for sure.
The other thing that was kind of a spicy-ish topic that, has some relevance to this group is that Ed Young has been working on a lot of different discussions around stabilization in OpenTelemetry as part of the process for trying to migrate us all, or, I'm sorry, graduate the OpenTelemetry project from incubating to stable? Full-fledged? I'm not sure, like, what we're graduating to. But one of those big sticking points is that so much of the code that we have out there is unstable, and there are some users who have hard requirements related to stability. This might also relate to Bart's topic that was added to the agenda, in terms of what people are able to use and not use.
So, it sounds like there's going to be more… effort to reach out to all the SIGs and ask about how things are currently going, and how, you know, the users, what the users of those SIGs actually want in terms of stability, or need in terms of stability. But, the topic is continuing at the SPEC SIG next week, so if anyone has opinions that they really want to discuss live, that would be a good meeting to try to go to.
Oh yeah, I can add those points here after the fact.
Okay, were there any other specs or things that people wanted to look at together right now?
Robb Kidd (he/him) 00:08:43 Is that, add event to span… add event to span event bridge regarding logs? I imagine that that is talk about how we might be dealing with… The span event to log changeover?
Kayla Reopelle 00:08:57 Yep, yep. I… was distracted when this discussion started, so I didn't catch the whole thing, but it sounds like we want the proposal is to add a new log record processor that will convert log events to spam events on the current spam.
So I… that… so I feel like I missed the beginning of the discussion, because I'm pretty sure we're moving away from log events, so I don't understand how… or, I'm sorry, from span events, so I don't really understand why we want this processor. So that's a thing, but I'm gonna listen to the meeting.
Robb Kidd (he/him) 00:09:31 I think that's of mere interest.
Kayla Reopelle 00:09:33 I'm trying to figure it out.
Robb Kidd (he/him) 00:09:33 like, maybe medium.
Interest to us.
So, yeah, I'll go read that too, and…
Kayla Reopelle 00:09:41 Okay.
Robb Kidd (he/him) 00:09:42 Watch the recording, or ask my coworker, who also went, and go.
Must have a lot.
Kayla Reopelle 00:09:47 So, yeah, it was relatively early on in the conversation.
Robb Kidd (he/him) 00:09:56 I can keep notes if you're… if you're…
Kayla Reopelle 00:09:58 Oh, sure, that'd be great.
Robb Kidd (he/him) 00:09:59 Sorry, I haven't been.
Kayla Reopelle 00:10:01 That's okay. Okay, so then for core… so, so Bart, normally what we'll do here is we start with a spec save, then we go into whatever points are listed for core and contrib… burning questions, etc. And then once all of that has been addressed, we'll go into the issues and PRs for each of those sections, and kind of wrap up the time we have with anything that comes up from just looking over what's new or changed.
So yeah, so for these PRs, I don't have a whole lot to say about them, except for maybe this one. So this was in response to… Some concerns with security and the potential to maybe… exploit the ability that we… or the… the behavior that we read the full response body in a lot of our OTLP exporters, and if there is a extremely long response body, like, that could be used to attack, some websites. It's… it's just… it's seen as an… Oh, this is… this is the better way to describe it. Security is a very… and talking about security is very weak for me. But, yeah.
Robb Kidd (he/him) 00:11:23 This would be interesting, because the malicious actor would have to… be who you're sending your telemetry to. But, okay.
Kayla Reopelle 00:11:33 Yeah.
Robb Kidd (he/him) 00:11:35 Okay.
Kayla Reopelle 00:11:35 Yep.
So, this has been an ask for all of the SIGs to update the way that they're doing the response bodies, and make sure that they're limited at some level. Proto and JS, I think, both had the 4MB minimum, so that's kind of… or maximum, so that's why I also… Did that here.
Arielle left a comment that I haven't seen his response to yet, but if, folks have some time to take a look at that.
Robb Kidd (he/him) 00:12:06 This was in my queue to review. I just ran out of.
Kayla Reopelle 00:12:09 time.
Robb Kidd (he/him) 00:12:09 Before the meeting.
So yeah, I'll… I'll add it to my queue.
Kayla Reopelle 00:12:14 Thank you.
Yeah, yeah, this is all still somewhat new stuff to me, too, so if there's more idiomatic ways or other ways that you've seen how to do it that might make more sense, like, please feel free to propose those, too.
This next one is adding event name to logs. It's something that's been in the spec for a while, and something we haven't added yet. There's a few other small features for logs that I'd also like to open up PRs for, I think, like, exception-related attributes, are one of the PRs. There's another one, too, that's escaping me, but I figured we'd start here.
And, The last PR is related to semantic conventions. So, we're in this process of wanting to eventually hand over the act of bumping semantic conventions fully to renovate, but before we do that, we have to close the gap and make sure we release, the versions that are before the most recent version.
So we got out 1.37 last week.
Thank you, Rob. Thank you. I know there are other people, James Thompson-Tomo, he was also really helpful with that.
I'm…
Robb Kidd (he/him) 00:13:31 I'm a huge fan of this idea, I think. I just had a question. My, and I think most of the… Changes here are good.
If I'm remembering right.
Oh!
Okay, so we have the open PRs to do all, like, the interstitial versions, because we're at 37, and it's currently 4.
Kayla Reopelle 00:13:50 based on these.
Robb Kidd (he/him) 00:13:51 or PRs to get us there.
I am pro just moving forward with these. On the Get Renovate to Do It PR.
Kayla Reopelle 00:14:00 Yeah.
Robb Kidd (he/him) 00:14:01 James Thompson had updated it to, open a PR for every patch and miner.
Which… I validated locally that it would attempt to do.
I didn't… I didn't make it happen in CI or anything, or chaos would ensue.
Kayla Reopelle 00:14:18 Okay.
Yeah.
Robb Kidd (he/him) 00:14:20 Our choices are, like, run with the PRs that are already open to do the interstitial bumps.
Kayla Reopelle 00:14:25 Oh, my…
Robb Kidd (he/him) 00:14:25 close those and let Renovate do it, so that.
Kayla Reopelle 00:14:28 We'll see what…
Robb Kidd (he/him) 00:14:29 So that we can say… I don't know that I love it. I don't know which idea. This is me processing a, kind of outlook.
Kayla Reopelle 00:14:35 Thank you for bringing this up. Yeah, I was completely ignoring this draft PR until we did the middle ones and missed the notifications, so…
Robb Kidd (he/him) 00:14:43 So I think, I think, this PR, which, James's suggestions added to it, would result in 3 PRs opened.
And judging by that output from Renovate, each PR going… it would be, like, 37 to 38, 37 to 39, 37 to 40.
Kayla Reopelle 00:15:07 Hmm. Which is cool.
Robb Kidd (he/him) 00:15:08 Weird.
Yeah. And, and then he replied that it's… it's… I don't… he doesn't quite know whether Renovate would auto-re… like, if we… if we merged the 38, whether.
Kayla Reopelle 00:15:18 Renovate room.
Robb Kidd (he/him) 00:15:19 Rebase, 39 and 40.
Kayla Reopelle 00:15:21 Mmm,
Robb Kidd (he/him) 00:15:22 Whether we would go in and say, like, hey, do the thing.
I don't know which one… if we just want to get it out.
Kayla Reopelle 00:15:29 It's just weird.
Robb Kidd (he/him) 00:15:30 to the PRs that are already open.
Kayla Reopelle 00:15:32 Yeah.
Robb Kidd (he/him) 00:15:33 Or we could see what happens if we let Renovate try to help us.
Kayla Reopelle 00:15:37 Okay, yeah, I think we're.
Robb Kidd (he/him) 00:15:40 I'm cool with either these. I don't know which one I like better.
Okay. Just getting it done has a certain appeal.
Kayla Reopelle 00:15:47 there is a level for me of, I would love to just have it done, but, if using Renovate to get it done… is… is helpful. I mean, it feels like a very low lift for me to do it manually, but, the whole point of…
Robb Kidd (he/him) 00:16:05 Sorry.
Kayla Reopelle 00:16:05 Oh, just the whole point of adding Renovate is so that we don't have to do it manually anymore, and think about it.
Robb Kidd (he/him) 00:16:09 I am very pro of that.
Kayla Reopelle 00:16:11 Yeah.
Robb Kidd (he/him) 00:16:12 Is there only, of the PRs that are open, is it only one to take it from 37 to 38?
Kayla Reopelle 00:16:17 Yeah, I think the 38 to 39… I had generated it a while ago. It basically needs to be redone, because it was before we made other changes to SEMConf.
So, it's here, but… You know, it's just a draft and would need to change after we release this one anyway.
Robb Kidd (he/him) 00:16:40 There's a part of me that wants to, Let's go for a renovate. Like, let's get that draft.
Kayla Reopelle 00:16:47 To renovate? Make renovate.
Robb Kidd (he/him) 00:16:48 do it, and see what PRs it would open. Compare that to the one that.
Kayla Reopelle 00:16:52 I like that.
Robb Kidd (he/him) 00:16:52 and…
Kayla Reopelle 00:16:53 Yeah, because we do not have to merge those PRs, we can change our mind.
So…
Robb Kidd (he/him) 00:16:59 Okay with that?
Kayla Reopelle 00:17:01 Yeah, I like that. That sounds good.
Cool. Can you… can you add notes to that effect, Amanda?
Robb Kidd (he/him) 00:17:06 Yes, I should add notes as I.
Kayla Reopelle 00:17:08 Thank you very much.
Anonymous Wolverine.
Okay, Barb, that is you, I think.
Bart de Water 00:17:19 So I haven't met most of y'all. I met Ariel in person a couple of weeks ago at RBQ Conf in Austin.
And for context, I work at a startup, and we're switched, sort of, like, revamping our observability story, switching everything over to OpenTelemetry. In the meantime, trying to figure out where I can maybe contribute upstream with some of the things that, you know, we would love to figure out about our application.
So I just decided to write some code.
And, Ariel commented on this PR, where it's like, hey, these probably should be metrics, according to all the standards. And I remember last year, October, November, Kayla, you and I collaborated a bit on a, pull request that I opened for Puma, where also the feedback was, like, hey, this should have metrics. But in both cases, I'm not quite sure where metrics sort of, like, stands at this time in terms of maturity. There's nothing in the contribo that actually does Has metrics, or at least nothing merged.
I see a bunch of, like, draft pull requests from a couple of people, but I, before I sort of, like, start putting in a lot of time here, or, like, maybe going down a path.
That might not just not be valuable at all. I wanted to… decided to just hop on this call and… Check the temperature, like, what's, what's, you know, what's the direction, what are the plans here? Because I have no insight in that at all. I think I'm also the only person here who doesn't work for an observability vendor.
More of a guy who's on an infrastructure team with too much time on his hands, not really, to be joining these calls.
So, yeah, like, I'd love to help out. In general, I love the concept of OpenTelemetry.
But yeah, before I dive in, I want to make sure that I'm not stepping on anyone's toes or going down to the left when everybody's going down to the right.
Kayla Reopelle 00:19:20 Well, thank you so much for joining, and also thank you for your logs PRs. You, like, you've submitted so many wonderful PRs, and I'm like, oh my god, thank God someone copped it, and, I really appreciate your patience, too, with the review process, as… For most of us, you know, it's not our full-time job, it's just something that we can do as time allows, and so, That… that does kind of segue a little bit into metrics. I think we've been needing to have this discussion again for a while about what we think about metrics and contrib.
The last time… oh, shoot, am I still here?
Mmm… can you guys hear me? Am I back?
Bart de Water 00:19:58 Yes.
Robb Kidd (he/him) 00:19:59 Can hear you.
Kayla Reopelle 00:20:00 Okay. Okay, cool.
Robb Kidd (he/him) 00:20:01 Hannah let me froze, but…
Kayla Reopelle 00:20:03 Oh, okay, interesting.
So, yeah, so I think the last time we had this discussion was probably over a year ago, and there was some hesitance about including metrics in, contrib because they weren't stable, and there was this question of whether we needed to create new packages for every gem that wanted to include metrics, or not. I think we just… we got stuck on the process of how to include unstable metrics with stable traces in a given gem.
I think that we have enough features in the metrics API and SDK now that we should start adding them to Kintrid. We've kind of made one jump with the logger instrumentation actually getting released that we do now have a package for logs that, you know, is dealing with this unstable telemetry.
However, it is isolated from everything else, so it kind of goes back to that earlier question of How do we add metrics into instrumentation?
One of the rules… oh yeah, go ahead.
Robb Kidd (he/him) 00:21:11 I have a question about metrics.
And… spans, but I can wait, because you had more to say.
Kayla Reopelle 00:21:19 Okay, yeah, hold that thought. So the, the last… thing, I think, to add is that where… where I think we could incorporate metrics into instrumentation is by having, Kind of like a… a two… knob approach, or two-switch approach. We need both switches to be on for metrics to be included. We check to make sure that the library is installed, so people need to, like, manually install the metrics API, or SDK, and if that's not present, we're not going to try.
And then they would also need to add some sort of configuration that says that they want to send metrics, and that would default to false, and they could set it to true if they want to send metrics.
To me, that feels safe enough in this time of things being unstable to… be able to allow people to have this telemetry before the API and SDK are stabilized. But I'm… I'm not a… like, a user, I think there's other people who have other perspectives that, you know, might not be as ready to just jump in and add this experimental thing to telemetry that, even though it is still at a zero level, you know, people have been, I think, treating it as stable in a lot of different ways.
So those are my thoughts on… where I think metrics and Contrib could fit together.
But I'm curious to hear what you guys think and, what your preferences are. And also, Rob, if you have your question before we roll into that, we can chat about that too.
Robb Kidd (he/him) 00:23:05 I do have a question, but I can… I can wait for… you had some questions, or a proposal of, Including experimental experiments.
Experimental.
Kayla Reopelle 00:23:17 Having them behind. Yep.
I think the two…
Robb Kidd (he/him) 00:23:20 I…
Kayla Reopelle 00:23:20 flag.
Robb Kidd (he/him) 00:23:21 I think that is in spirit and implementation, how we have done experimental stuff in the past, with this project and in, like, my life and others.
that the default behavior of a contribib instrumentation would be, I'm going to do stable behavior, and you can opt in to experimental stuff. I think that's… legit. I'm interested in Bart's opinion as a consumer.
Bart de Water 00:23:47 Seems reasonable, like, I'm assuming another concern here with not enabling metrics by default is purely that it's new and not fully baked, or is there also, like, a cost aspect to it?
Robb Kidd (he/him) 00:23:59 Yes.
Kayla Reopelle 00:24:00 I think it's… yeah, yeah, yes, folks.
But I think that comes more from, like, the OpenTelemetry guidelines around stability and, like, what adheres to a spec and what doesn't adhere to a spec. So when you say that something is stable, then there's kind of these guidelines that are in the OpenTelemetry specification that you're saying you adhere to.
And the process of making a package staple involves bringing someone in from the technical committee to actually analyze your code and make sure that it is, in fact, doing what you say it is. And so, there's a lot of, like, ceremony around making sure that things are officially True.
Bart de Water 00:24:41 Gotcha.
I think, generally though, if I look at, you know, like, all the other Ruby stuff that I've done over the years, like, usually, you know, new scary features tend to be opt-in and, you know.
usually the changelog or the code itself has, like, a common saying that, like, yes, we try to follow SEMVER, except these things that are marked experimental, they may break, you know, like, any patch release, you know? But in the meantime, you do need to get, like, feedback from the real world, and…
Kayla Reopelle 00:25:09 Yeah.
Bart de Water 00:25:09 I think it makes sense. The other thing that, just comes to mind is that, like, you know, all the gems are called, like, dash instrumentation at some point, but it seems really that right now it just only means, like, dash traces, so I think also.
Kayla Reopelle 00:25:24 Yeah. Makes sense.
Bart de Water 00:25:24 to include metrics in there and not have, like, a separate dash metrics package for that reason.
Robb Kidd (he/him) 00:25:33 One, I would need to go look at other instrumentation packages and see if a particular instrumentation library in a different language for a different Framework.
Does all the signals, and then, which ones you want.
Kayla Reopelle 00:25:46 Yeah.
Robb Kidd (he/him) 00:25:47 is a configuration option. I suspect that's the case.
Did an audit.
Kayla Reopelle 00:25:52 a while ago, and that was the case then, but things could have changed. And so, I think at the beginning of 2025, that was the case that I found when I looked at, I'm pretty sure, Java, Python, and Go.
Robb Kidd (he/him) 00:26:09 So my, so my question that I had held off was, I noticed in this, PR, that… This is recording metrics as attributes on a span, which… Is supportable by the signal.
It's just… Not… I don't even want to say it's… it's kind of off-spec.
that doesn't mean it's wrong.
I happen to work at a vendor who likes metrics coming in on… as attributes.
Bart de Water 00:26:42 I will also add that this has definitely been following the path that Rails itself sets for these, you know, the internal.
Robb Kidd (he/him) 00:26:49 They throw them on events, and whatever you put your event in, whatever backend you put your event in.
Bart de Water 00:26:54 I have these events already, I just need to get them to hotel land, and with some help from my friend Claude, this is what we ended up with.
Robb Kidd (he/him) 00:27:01 Yeah. So, I… As a…
Bart de Water 00:27:06 I'm not against it. I'm not against it, it's just that, like, then we got back to my metrics question, where it's like, okay, you know, like, I got no other example to follow, so, like, I can roll something myself in the meantime for my app, but there's a few things that we're dealing with at work right now, is as we're sort of, like, starting to scale, is that, like.
I got jobs OOMing the worker, and I'm like, which job is that? And just having only logs for that is not a good time to figure that out.
So I started looking into this, and the other thing is, the biggest top of mind thing for me is queue latency. We're running some, like, bigger, heavier jobs, and I want to make sure that higher priority jobs get the treatment that we expect of them.
So that was another thing that I was looking into, contributing a few things, where it's like, these seem useful for everyone, because everybody will have, you know, like, either, probably this shape of problem one way or the other, at least to have some more signal to start digging into.
Robb Kidd (he/him) 00:28:04 So, an idea… to add… Yet another config option. That's a… that's my new phrase for this project. What if we had 3 config options? You gotta… well, not necessarily three that you all… you have to turn on all of them, but if… Like, maybe these… Not… Alright, so we're in the space of, like, where the semantic conventions say, They say, for certain types of activity, you should record these attributes. And then there's, like, shoulds and mays around if you're instrumenting a framework that has interesting data, you should write that, you should record that data.
Good luck! With no real specifications around what names you give it, what shapes those take, because it's kind of very framework-specific, and you can't make a spec.
Meet all needs, despite their attempts.
So I think, as implementers of instrumentation of, let's call it the active job framework, we can… Create an attributes namespace that's specific for this, and… maybe optionally say, like, record metrics as… some option that's in the spirit of record metrics as attributes.
and at a point where we add the actual metric signal.
Maybe we have to think now, or we could defer the thinking until later, because it's all experimental.
what's the interaction of?
when we can emit the metric signal from this library, and maybe it's as simple as the turn these two keys on, and it will emit the metric signal.
that you, the user, Bart, could choose, I would like those metrics as attributes, or as… metric metrics.
Bart de Water 00:29:56 Yeah, or maybe even both.
Robb Kidd (he/him) 00:29:58 Or, yeah.
Kayla Reopelle 00:29:59 Sure.
Robb Kidd (he/him) 00:30:00 I can have a config that's… that's 3.
Or however many, I…
Kayla Reopelle 00:30:05 Yeah.
Robb Kidd (he/him) 00:30:07 I like giving you the data that you need to get your job done, this is valuable stuff, we should record it. We can record it as attributes today.
like, it's… it… it… we are capable of doing that.
Bart de Water 00:30:21 This is sort of like the escape hatch, is that, like, you call this framework specific, you namespace it under, like, messaging active job, and then, you know, you make it your own party.
Robb Kidd (he/him) 00:30:31 Yeah, and I didn't see it go by. These are… these are measures that ActiveJob has already made, is that correct?
Bart de Water 00:30:38 Yeah, like, this is actually for, for every, active support notification event. There's two styles of sort of, like, describing to it. One is the start-finish ones, that's called the evented mechanism, and you also have the event… object mechanism, I believe, and then you get an active support event object after the, sort of, like, the equivalent of a span has already.
Robb Kidd (he/him) 00:31:05 Yeah.
Bart de Water 00:31:05 Yep. And then, on that event object, these, you know, CPU time, idle time, etc. are already there. So, this block of code, the record metrics part, this is basically copied verbatim from Rails itself, because that's not available on the evented API.
Robb Kidd (he/him) 00:31:24 Okay.
Bart de Water 00:31:25 So…
Robb Kidd (he/him) 00:31:26 Well, I'm…
Bart de Water 00:31:26 So yes, it records it, but only if you use the adjacent API, but I wanted… but since then, you don't have control over the span start and the span stop that you need for here. That's why I lifted it out and recreated it.
Robb Kidd (he/him) 00:31:41 Okay.
Then, I have not yet reviewed this implementation, but this is valuable data, and I think we ought to let people opt into it.
Yeah, I agree.
Bart de Water 00:31:53 We can, you know, like, we can recreate this too for, like, requests coming from Rails, that was sort of, like, the other.
Kayla Reopelle 00:32:01 Truck me.
Bart de Water 00:32:01 unit of work where I would be interested in understanding these things, because if you have, like, a runaway bit of code that does an N plus 1 query over an API, I'm totally not speaking from experience here, and you're wondering, like, why are these controllers taking so long?
Robb Kidd (he/him) 00:32:21 some high-level… some high-level concerns is the Sadabi… because this does take some compute time, and there is, Some consumers of these libraries care about compute time, even though they're running Ruby.
So we ought to make these opt-in.
And then the opt-in is… is, like, what format do you want them to take? Span attributes or real metrics?
I don't yet know what the implementation… like, can we do these computations and have the computation done once, and then flow into both attributes and metrics? I don't know what that shape looks like, but yes, I am… Interested in giving you this… behavior, Bart, because this is valuable data, and that's the point. That's the point.
Kayla Reopelle 00:33:10 I agree.
Bart de Water 00:33:13 I think it just.
Robb Kidd (he/him) 00:33:14 Maybe…
Bart de Water 00:33:14 your question? Because if we're finishing the span, would that also be the right moment to emit a metric, just theoretically speaking?
Robb Kidd (he/him) 00:33:22 That, I'm…
Kayla Reopelle 00:33:27 Mmm.
Robb Kidd (he/him) 00:33:28 weak on metrics, but I think yes, because that's the point where you have all of the… you have the end times to do these computes.
Bart de Water 00:33:35 Yeah.
Kayla Reopelle 00:33:36 Yeah. It depends on the metric.
Robb Kidd (he/him) 00:33:38 Are you counting? Are you… I'm recording a duration, or… yeah, it's…
Kayla Reopelle 00:33:45 I remember reading something that, like, metrics and spans are supposed to be able to exist independently of each other, so you shouldn't, like, copy span data onto a metric, and so I don't know if that means that you could record the metric after the span was already completed.
I feel like with exemplars, maybe it gets weird, because you need to have the span ID and a trace ID.
Robb Kidd (he/him) 00:34:12 My default answer is yes, Bart, because I put my metrics on my… in my app.
Bart de Water 00:34:17 Yeah, because it feels like, you know, like, I wanted to measure how long, you know, how much object allocations happened over the execution of this job. As I'm finishing the span, I have that data.
Robb Kidd (he/him) 00:34:29 That's when you, that's when you…
Bart de Water 00:34:29 No.
Kayla Reopelle 00:34:30 Yeah.
Bart de Water 00:34:31 Might as well ignore it as a metric.
Robb Kidd (he/him) 00:34:34 We have done shenanigans with span processors to do, attribute add-ons at the end of things, I don't think that we fully… that the API and the SDK fully implement the official on finishing… Callback, which could… .
Kayla Reopelle 00:34:54 There's a bug in it.
Robb Kidd (he/him) 00:34:56 What's that? How's about?
Kayla Reopelle 00:34:57 It has a big bug, yeah, it's there, but…
Robb Kidd (he/him) 00:34:59 This would be the better way to do… like, there's been hacky ways to, at the end of the span, I would like you to record, you know, difference in memory utilization, or garbage collection, or basically all the metrics you got here.
This is the better way to do that, though. I'm… I should have… shouldn't have even brought up this band processor. This is… you should do it in the instrumentation.
so, alright, I blattered a bit.
I'm pro the spirit of this pull request.
And I… and I'm sort of curious about whether we could run with an initial implementation that is along these lines where we're adding attributes.
Put a guard around it so that we don't do the computation if people don't want these.
Extra metric… extra attributes.
And… I guess we could get together and figure out what… Giving the option of either attributes and or Actual metric signal emitted might look like.
Kayla Reopelle 00:36:06 Yeah, but the high-level idea I have there is maybe instead of making it a Boolean, we pass in a symbol or a string that says, like.
Do you want the metrics on the spans? Do you want them as metrics, or both?
Robb Kidd (he/him) 00:36:18 Yeah.
Yeah.
Bart de Water 00:36:23 Well, I think, yeah, I think if we add an option, maybe just with, like, one permissible value for now, so that we leave the door open to have it for multiple values, like metrics, or both.
And then short-circuit based on the presence of that to whether or not to, like, record these things. I think that could work.
Robb Kidd (he/him) 00:36:43 And I think we're back to the two keys, where, Kayla, you had proposed metrics are enabled, and the, metrics gem is Available.
The metrics enabled could be this Config that has multiple settings.
And…
Kayla Reopelle 00:37:01 Yeah.
Robb Kidd (he/him) 00:37:01 it defaults to off, maybe, initially, and then the other options are as attributes, as metrics, or both. And so, as metrics, or both, would be the, okay, you need the other… metrics that actually have to be around for me to do it.
Kayla Reopelle 00:37:17 Yeah. I think one other thing is this is an experimental library, we're still at 0.
X, and so I think that we can put this in there and have this experiment and see if it gives people value, and if an active job is widely used. So if it… if there are problems with it, we'll most likely hear about it.
Robb Kidd (he/him) 00:37:37 Yeah.
Did you, I'm looking at what the attributes that were put in there, do you have… queue time… like, this is ActiveJob, so it's a job… it's a job runner. Do you have job queue latency in here?
Bart de Water 00:37:58 Not for this PR. I'm experimenting with that in, like, my main applications code. Okay.
I…
Robb Kidd (he/him) 00:38:07 See?
Bart de Water 00:38:08 Yeah, I can add that to… I've seen it, sorry.
Sorry, because there is, like, ActiveJob does report when it's either, like, scheduled or enqueued at, so, like, you know when it's supposed to run a timestamp, and then, of course, you have the current timestamp, so that's something that can be added.
Robb Kidd (he/him) 00:38:26 And I'm having a memory tickle from dealing with Sidekick, that… I think our instrumentation of the job runners emit a span event for NQ time and, runtime?
Yeah. There are… there are tricks that… We have not updated the instrumentation to It's kind of specced to do that, because these are things that happen at a time, and there's no attribute type that is a date time, unless the spec has moved on me since I last looked.
We can't really record times as a time type on… as an attribute on a span, so they show up as span events. There are tricks that you could do in the collector, and I could find a write-up of what I did to compute If you want it on your spans, there's a… you could run it through a collector, and there's some transform rules that you could give your hotel collector that will take the time on the span event, take time on the span, do the math, and then put the latency on the span event… on the span.
The benefit of that is also you're not spending… you're not… that's not even additional compute that you're doing, In your app, because this is, like, on span end, it's kind of blocking, so, like.
You want to get out of that quickly.
Bart de Water 00:39:43 Yeah.
No, like, I can, I can definitely, it's definitely of interest for me to have, Like, queue duration, in there as well to monitor the health of my queues.
Robb Kidd (he/him) 00:39:56 Well, are you in the CNCF Slack?
Bart de Water 00:39:59 I am, yes.
Robb Kidd (he/him) 00:40:00 Okay, I will dig up the write-up of… that I did on how to do that in the collector, so that… You can at least do… you have a workaround today, if you.
Bart de Water 00:40:09 Gotcha. Appreciate it.
Robb Kidd (he/him) 00:40:11 Okay.
Kayla Reopelle 00:40:14 Thanks. Alright, we have more topics on the agenda, so I feel like we should try to move on, but do you have the answers that you need, Bart, to move forward?
Bart de Water 00:40:21 Yep, I'll add some configuration, and then we can sort of, like, hash out the final details.
Kayla Reopelle 00:40:28 Great. Excellent. Thank you.
I… I missed that in the chat, Sean shared also this, ad revenue runtime metrics to OTIL semantic conventions issue, that might be of interest. Do you… do you want to share anything about it, Sean?
Xuan Cao 00:40:47 No, I think it's not related to this, span, metrics. This is more of a one-time metrics.
Kayla Reopelle 00:40:55 Okay.
Sounds good. But yeah, if you haven't seen this one yet, Bart, I don't know if that could also be helpful for you.
Alright, let's move… Into… this one…
Robb Kidd (he/him) 00:41:10 I did notice that some of those semantic conventions are, like, garbage collection things, which might affect what we name things in that.
Kayla Reopelle 00:41:17 After each other.
Robb Kidd (he/him) 00:41:17 of instrumentation?
Kayla Reopelle 00:41:19 Yeah, yeah, that's a good point. I mean, shall always check semantic conventions before we merge.
Xuan Cao 00:41:29 So, yeah, I'll be quick. So… We see a lot of PR for this, test coverage, and then people open PR up. But if you look at each of Amazon, they are really just about… The, the cement, cement commission, the old stable.
Kayla Reopelle 00:41:49 and…
Xuan Cao 00:41:50 Staple, oh, stable, both.
Kayla Reopelle 00:41:54 Yeah, so because.
Xuan Cao 00:41:55 Yeah, because those, make a convention feature that caused the static coverage, drop. And then… so, they have all the fix.
That is a fixed rate to that issue, but the thing said.
they have different approach for each one of them. And since we are moving out of this network connection stability environment, I don't know if we still need to… you know, to, pay more attention to… do we need to, like, actually review this PR, or, you know, just leave it open. So that's just my question. And also, again, they use… they try to solve the same problem, but they use a different approach, which is not really, aligned in the, same approach. So, yeah, that's just my, question, yeah.
Kayla Reopelle 00:42:50 Yeah, that's a great question.
Those are concerns that I've had, too. I'm not sure if anyone else has also had them.
I don't feel like I know the right answer here.
Because on the one hand, I want to encourage these first-time contributors to continue participating, and on the other hand, their work could be pulled out this week, even if we merge it today. We'd have to merge it, release it, and then… take it out as soon as we pull out the environment variable. Hannah, I want to pass it over to you, since you've been kind of leading the environment variable project.
Hannah Ramadan 00:43:26 Yeah, I saw this and also had the same concerns. They're all different approaches, and kind of in line with what you just said, Kayla.
this… It is hard because we did create these tickets, and people jumped on it and spent time contributing solutions.
they all will be pulled out, very soon. So, I don't know if that… what, like, the right answer is. I don't think… from… Yeah, from, like, a technical standpoint, I guess it… It… it doesn't… everything that's added, like, will go away soon, so I don't know if it's worth, like, saying, hey.
we're not going to accept these PRs, because… We'll pull it out in a week, Maybe… it is tough, because then it's requiring all of us to spend time reviewing these.
And that kind of sucks, but… Yeah, I also, like, don't know the right answer here. I kind of… I mean, we could easily, like, thank people for their contributions, but if we aren't going to accept these, I think we need to focus on Like, getting that environment variable removed and just only emitting stable attributes so that we don't have to, like, touch these tests.
Kayla Reopelle 00:44:49 And I don't know if it's still a barrier or not, but one of the things we had discussed in the past was that we wanted to wait to pull out the environment variable until we had schema URLs, so that people would know what the final schema version was that applied to whatever they were using. And so, if we adhere to that, then that will inherently take more time.
And so these could live for a couple of more weeks.
But… this is our… this is kind of laying the groundwork, too, for what we want to do for database conventions and messaging and all of the other conventions that our instrumentations adhere to. This is just the first one, so I think we have to make some… more difficult decisions here than hopefully we will for future.
conventions.
Robb Kidd (he/him) 00:45:39 Are you in favor of the, waiting to remove it until we have schema URL?
Hannah Ramadan 00:45:48 In that case, maybe we do accept these and just live with it for a while.
Robb Kidd (he/him) 00:45:53 And to live with it is that… The implementation of the tests don't… aren't… Don't follow similar patterns?
Hannah Ramadan 00:46:02 Yeah, I think so.
Kayla Reopelle 00:46:04 Yeah, and… So I guess then the only place where it could really get complicated?
This one's interesting. Is if there's new test coverage in… Stable that doesn't adhere?
There's so many PRs, I don't even know which one to open and pick right now.
But yeah, I guess another way we could go about it, too, is… If we set a standard, we could provide that standard as our feedback.
ask.
The people who open the pull request to change their tests to reflect that standard, so that we keep some consistency throughout these.
libraries, which I think is probably fine, as long as we can explain it well and convey it clearly, that it's, like, it's a huge burden to maintain all of these. One thing that makes it easier is having consistency across the libraries. This is what we need.
Robb Kidd (he/him) 00:47:03 So we could use… we could use this… spread.
of implementation shapes, as a…
Hannah Ramadan 00:47:13 Pick a…
Robb Kidd (he/him) 00:47:14 Anytime we would comment, like, don't do it that way, do it this other way, that's… content that we need to go and put into maybe James Thompson's PR to update the contributing or development? I don't remember which.
Kayla Reopelle 00:47:26 Hmm,
Robb Kidd (he/him) 00:47:27 He had, he had some, Updates to… how do you work with this repo?
Yeah, I think that would be good.
And we'd apologize, maybe you're like, sorry, we set these standards as a result of the… Volume?
Kayla Reopelle 00:47:44 Yeah, yeah.
Robb Kidd (he/him) 00:47:45 The volume of different implementations we got had us set the standard, so if you'd like to update your PR based on that… Please do.
And then, if they don't and it goes stale, we close it.
I think this also, that these are all about test coverage. There was another PR, I think, from, James about… Setting the expected minimum test coverage.
was it that one?
Kayla Reopelle 00:48:15 this one.
Robb Kidd (he/him) 00:48:16 A concern I had with this one, and I didn't… I haven't reviewed it deeply, but if we look at files changed.
Kayla Reopelle 00:48:22 There was a.
Robb Kidd (he/him) 00:48:23 A lot of the, A lot of the how of what's being run is in… The actions.
It's in CI, so, like, that bundle exec.
where a minimum coverage is looked up from inputs, and the inputs comes from GitHub CI YAML.
my… it's more than an instinct. My experience is that the how… of testing. I'll call this a test, even though it's, like, test coverage. The how should be in something that's easily runnable in the development environment. So I ought to be able to, like, run rake coverage.
As a develop… if I'm going to iterate on… meeting this coverage minimum. I want to be able to run it in dev and not have to, like, push the… push to GitHub to find out whether I improved things or not.
Kayla Reopelle 00:49:23 Yeah.
Robb Kidd (he/him) 00:49:24 Which is… again, I ran out of time. That's… that is my feedback to this PR, that I would like these, Instead of the GitHub CI YAMLs being where the minimum coverage is set.
Set that somewhere else.
Kayla Reopelle 00:49:43 I think that's great, and I agree with that too.
Robb Kidd (he/him) 00:49:46 And I will… I will give that feedback to this PR.
Kayla Reopelle 00:49:49 Okay.
Robb Kidd (he/him) 00:49:50 When we get out of the meeting.
Kayla Reopelle 00:49:52 I will hold off merging it, but yes, I agree that that would really… I think that would be a better experience for everyone long-term.
Robb Kidd (he/him) 00:50:00 So, I… I can, since I'm… I'm in review mode as much as I can.
Kayla Reopelle 00:50:05 this week.
Robb Kidd (he/him) 00:50:06 as time allows, I will try to, I will comment on that PR from James, and see if I… Like, Joanne, do you have… concrete, like, I wouldn't do it that way on any of these PRs, so that we could… maybe in Slack, maybe we can assemble a list.
Standards that we want to set and document somewhere, so that we could then have that as a reply.
To all of these.
Xuan Cao 00:50:34 I can take a look, but I don't, yeah, I can't take a look to see, but I'm not sure if my, my, answer would be the best, standard for them to follow, yeah.
Robb Kidd (he/him) 00:50:47 Okay, well, it's just if you have opinions about something that one of those contributors did, just drop it up, like, I wouldn't do this one thing, I wouldn't do that way, I think we ought to do it.
Kayla Reopelle 00:50:55 Beautiful.
Robb Kidd (he/him) 00:50:55 And then we can figure out whether we document or implement a linter or something that Checks for that way.
Kayla Reopelle 00:51:04 We can have that conversation in Slack before we put them on all the PR, so that way we have, like, a unified voice, so we can start there.
Robb Kidd (he/him) 00:51:13 Yes, so if, yeah.
Hannah Ramadan 00:51:16 And just one more note, for all, like, these dupe-stable old PRs are just so big and so messy, and they're, like, part of the reason was originally so that we could Keep everything, like, very separate, and then when it's time to remove it, simply go delete, some of these files, and not have to worry about where we might have, like, done extra stuff.
So I reviewed… the first one I happened to review was the HTTP one, and that one's kept with that same pattern of making small edits in every file. Some of the other ones kind of did some, like, very clever, cool things, but might be a little bit more difficult to, like, remember slash rip out later. So I think that's one… It's not as, like… Yeah, cut or clever. That's a great cover.
Robb Kidd (he/him) 00:52:00 marching thing. Make this easy.
move, yeah.
Hannah Ramadan 00:52:03 Yeah, so that is one, like, view as, like, we maybe, like, pick a pattern for these, the pattern.
The existing pattern was that we want to make it easy to rip out.
Kayla Reopelle 00:52:19 Yeah, I think that's a great point.
Okay, Hannah, I believe this is you. I believe you wrote this beautiful thing on database semantic conventions.
Do you feel like we have, like, we have 10 minutes left? Do you want to start the conversation now, or where are you at?
Hannah Ramadan 00:52:39 Yeah, so I have this… Beautifully large.
Kayla Reopelle 00:52:42 Yeah, we do.
Hannah Ramadan 00:52:42 Oh, yeah.
Kayla Reopelle 00:52:43 Sean, are you okay if we move your point here to after Hannah presents this?
Xuan Cao 00:52:50 Yeah, yeah, definitely.
Kayla Reopelle 00:52:51 Okay, thank you. Alright, Hannah, go for it.
Hannah Ramadan 00:52:54 Okay, in short, I have a trilogy PR open that is supposed to set the kind of groundwork for moving for adding that, semantic opt-in stable variable for the rest of the database libraries. A lot of conversation on it, including some conversation that is maybe less related to the just simple attribute name switches and how we want to, like, emit things and name things and such. I have two questions that came up From James on this PR, and I wanted to get some, like, general opinions. I… after writing this, like, sheet and stuff, I think I have a stronger one now, but I wanted to just check with y'all on if we want to… have this PR serve as, like, kind of the… this is where everything… all decisions will get made on, like, when new config values exist, the span names, I think those are kind of the two here, or if we can, like, move that until a later time. This… this first one right here about… is it okay to give users the option to send over raw SQL? It's probably, like, an easier, Question, and really, like, according to, like, spec spec?
People don't… should not be able to do that, but… can we keep allowing people to, like, have that as an option?
And that is, like, that's kind of, like, the first one, where it's like, how much flexibility do we want to give users? First, follow the spec.
So if anyone has an opinion on that, I'm kind of thinking to maybe… Leave that until a later update.
Robb Kidd (he/him) 00:54:40 Leave it configurable, or leave it that we're gonna…
Hannah Ramadan 00:54:44 I would leave it… I kind of think leaving it configurable, but want to get other opinions, and leaving it configurable to send raw sequels out of… technically out of spec.
Kayla Reopelle 00:54:55 And to, like, leave it configurable during this period of time with the environment variable, we can have more of a discussion about it, and then in the future PR, decide to remove it from stable if we don't want to support it.
Hannah Ramadan 00:55:07 Yeah.
Kayla Reopelle 00:55:08 Okay.
Yeah, I think that I'm comfortable with that. I think the database conventions are more complex than the HTTP ones, and so I don't think we should be expected to need to have everything in one release, and that that is what's going to stay stable for the whole time.
I think as long as we have clear changelamp entries about what's happening, then we've communicated enough about what's going on.
Robb Kidd (he/him) 00:55:38 We can update the PR's… we could update the PR's title to, like.
Not just be, it's stable, wicked, but… A step… a step towards stable.
Hannah Ramadan 00:55:47 Yeah, that would be a good call.
Kayla Reopelle 00:55:50 Yeah, right, like, attributes or something, yeah.
Robb Kidd (he/him) 00:55:54 I'm cool with configurable. I think the only thing that would have me lean towards being stricter is to know a little bit more about the details behind why Why did the… why did the people who authored this statement in the spec say it shouldn't… that… that… that should not be extracted from db query text.
What's the reason why it shouldn't be extracted?
And then we can choose whether we… whether we follow the letter of the law or the spirit. I don't know the spirit behind this one.
Hannah Ramadan 00:56:30 I think that's what's difficult with a lot of this kind of, like, spec reading stuff, is it's, like… Kinda hard to tell.
Robb Kidd (he/him) 00:56:37 Yeah.
Kayla Reopelle 00:56:39 And if I remember correctly, there should be a channel that's specifically devoted to the database conventions.
And if not, then the semantic conventions channel could be a good place to just post the question and be like, hey, why is this the case? If you can't find it by looking, you know, in issues or git history or… Whatever.
Robb Kidd (he/him) 00:57:04 Like, I agree.
Kayla Reopelle 00:57:05 really doesn't work. Oh, sorry, go ahead.
Nope. If that really doesn't work, then, we'll… We can look at who was formerly attending the database specsig and just reach out to them individually to try to get some details.
Hannah Ramadan 00:57:20 Okay, how about for this PR, since maybe we focus it more on, like, the attribute names, I will… I will just maybe make a new ticket or document that concern, and then link that and kind of, like, move on and…
Robb Kidd (he/him) 00:57:34 Progress is better, yes.
Kayla Reopelle 00:57:35 Sounds great.
Hannah Ramadan 00:57:36 Yeah.
Kayla Reopelle 00:57:37 Nope.
Hannah Ramadan 00:57:38 Cool. And then for the larger one, the span name, I… we have a unlimited amount of, like, options per spec. I think it's a pretty… unfavorable experience for folks. That's left side of the column strict spec, and the examples of what queries would produce. It's really, you're just getting your database name.
Until we have that.
query summary opt-in environment, or opt-in variable that people can, add, but that's another… potential… can of worms, I think.
performance impact was, like, a concern that was raised. Different agents implementing different versions of this query summary thing. I think, Rob, you brought up that one, and I was like, that's such a fair point. Like, it just… it seems like a lot.
I dug into what Python is doing. They have implemented this environment variable, and they did not change their span name in that go. And they do not yet have the query summary attribute available either.
I… I think after, like, thinking through this more, I think the… The wrong thing to do would be to make changes now that we Done.
to make changes now, and then have to change things again for users.
And I'm not sure that we… I'm no longer confident that we need to change the span name right now. Strix Spec… feels… Like, a loss for users.
And… Keeping things as is, which is the… config options.
none of those config options are wrong, according to, like, the… what we might end up producing for span names. They're all tech… they are in that fallback list of what could be a appropriate span name. So I… I am more so leaning towards just, like, leaving… that alone as is, following Python's lead, and just… not changing anything, and coming up with whatever our new config values could be, what query summary looks like a little bit later. This… it feels like a larger… it doesn't feel worth it to change, but yeah, I love hearing opinions.
Robb Kidd (he/him) 01:00:01 I agree. Vigorous agreement that, we could deliver the improvements in… that are currently in this PR, and have open an issue about the DB summary option for spam names.
While it's… while it's still unresolved about How we implement it.
Is that accurately?
Yeah. Okay.
Hannah Ramadan 01:00:25 That makes sense, yeah.
I… yeah, maybe just… oh, new issue, this is something later on, I think it would be less surprising for users if we, like, change it now and then not change it again.
Robb Kidd (he/him) 01:00:37 There's, like, 4 layers of fallback, right? And we're just not implementing the first one yet.
Is that…
Hannah Ramadan 01:00:44 Yes.
Robb Kidd (he/him) 01:00:44 proposal.
Hannah Ramadan 01:00:46 Yes, there's layers.
Robb Kidd (he/him) 01:00:47 Do parse… do parse operation option, but it's 2, 3, and 4.
Is that the proposal?
Hannah Ramadan 01:00:58 do… my… I… I think my actual proposal is don't make any changes right now.
Robb Kidd (he/him) 01:01:04 Oh, don't mess with the name right now.
Hannah Ramadan 01:01:06 Don't mess with the name right now. I'm worried about changing some configs and fallbacks, and then having to re-change it in the future if we're not, like, really confident in what…
Robb Kidd (he/him) 01:01:14 If we don't know what we're doing, let's not do it yet.
Hannah Ramadan 01:01:18 That is where… yeah.
And there just seems, yeah, too many, like, what-ifs for this, and options that…
Robb Kidd (he/him) 01:01:27 And that's the beauty of changing the title of the PR.
Hannah Ramadan 01:01:30 HPR is no longer…
Robb Kidd (he/him) 01:01:31 It's going stable, it's, steps, baby steps towards stable.
Hannah Ramadan 01:01:36 Statue names, yeah, some other little things.
Fish fan.
Kayla Reopelle 01:01:42 I think…
Robb Kidd (he/him) 01:01:43 Let's improve life.
Hannah Ramadan 01:01:45 Okay, awesome. And maybe as… I would love it if we could just use someone else's query summary, like, if one… somehow that was an option, I don't know, maybe it will be.
But cool. I will document that in a new ticket, link it to that PR comment, and then see if we can just slide this along, keep it going.
Bart de Water 01:02:05 Like, dumb question, like, is this purely on the database adapter level, or is this also happening on, like, an ORM, like, active record?
Kayla Reopelle 01:02:17 So… Yeah, go ahead.
Hannah Ramadan 01:02:20 Yeah, go ahead, I think…
Kayla Reopelle 01:02:25 I think you should answer, Hannah. I think you should answer. Go for it.
Hannah Ramadan 01:02:30 Yeah, I think it's just on the database adapter level. I haven't, like, messed with anything active record, these are just, like, the different instrumentations we have for, the database libraries.
Robb Kidd (he/him) 01:02:46 I'd propose that it's definitely on DB clients.
And then when we figure out how to do it on the DB clients, where it's definitely spec'd.
We could… have a better informed opinion about whether it ought to go on our ORMs.
Kayla Reopelle 01:03:04 the, the Polar.
Robb Kidd (he/him) 01:03:05 A day, long shot, I'd say probably yes, because people sometimes turn off DB client spans, but… That's not set in stone.
Kayla Reopelle 01:03:17 This pull request would only change Trilogy. So, eventually, pull requests would be open for the other DV clients, and also eventually we'd look at Active Record and how it impacts that as well.
Bart de Water 01:03:27 Team Postgres on this side of the screen.
Kayla Reopelle 01:03:31 Then, yeah, you have a little bit of time to wait.
But we will apply the same rules for Trilogy as we will for Postgres, so if you have opinions here, it would be good to voice them now.
Bart de Water 01:03:43 Well, like, my… again, like, as I… just purely on the face of it, option 3 and 4… tell me nothing that I would already know, at least for, like, 99% of the applications that are out there. Like, I know which database I'm connecting to, because it's the only one that I have.
Robb Kidd (he/him) 01:04:02 So the span name would not be meaningful to you.
same along.
Bart de Water 01:04:06 Like, option 2 would at least tell me something, but, yeah, and I don't know what query summary would look like. I do remember…
Robb Kidd (he/him) 01:04:15 We don't either!
Kayla Reopelle 01:04:18 What?
Bart de Water 01:04:19 Remember, This is a bit of an anecdote, if you indulge me for a minute. I used to work at Shopify before joining this startup, and someone on the infrastructure team build a really clever Splunk dashboard that I think hashed the query, but with, you know, like, not the raw query, but with, you know, the… before it was… the values were substituted. So that gave you, like, a query fingerprint, and that was very useful to sort of, like, quickly figure out, like, where your back queries were living. Of course, this was before we had anything like tracing back, this was, like, 5 years ago, and Shopify didn't have tracing at the time, or at least Not on the scale that everyone could use it. But that was a useful thing to have, at least, where it's like, okay, if I know that this controller generates this query here with this hash, then I can use that hash to go and find how it's actually behaving in production.
Robb Kidd (he/him) 01:05:15 the… The hash is an interesting idea, that would definitely be off-spec, so we, like, if a hash could be an interesting thing that we could add as an attribute that's not specced.
DB summary is, like… DB summary is, I'm gonna go and parse your query and try to tell you What operations you were doing on what tables, and…
Bart de Water 01:05:37 Okay.
Robb Kidd (he/him) 01:05:38 it's, I predict, compute-intensive, and… But also, they're, like.
again, the spec is saying you shouldn't compute that from dbQuery text. I'm like, how do…
Hannah Ramadan 01:05:50 What do we do?
Robb Kidd (he/him) 01:05:51 How do you expect us not to?
Which is why we don't quite know… We know what it ought to be, we don't know how to give it to people without doing what the spec says we shouldn't do.
Bart de Water 01:06:03 Well, like, I'm spitballing here. Is there a world in which the database tells you what it did after it's already parsed your query and ran it, and then being like, oh, by the way, like, I did select on the.
Robb Kidd (he/him) 01:06:14 It'd be fantastic to find out that the database would But I don't know that it does today.
Hannah Ramadan 01:06:19 In that, yeah?
Robb Kidd (he/him) 01:06:23 I…
Kayla Reopelle 01:06:23 I'm…
Robb Kidd (he/him) 01:06:24 I wonder, like, what frameworks or database systems are doing this for you, that somebody wrote the spec? You shouldn't do this. You shouldn't have to compute it from the db query text. I'm like, how are you getting it without doing that?
Bart de Water 01:06:36 And then the answer is, like, you go get blaming into the spec to figure out who originally proposed it, and then hope there's a breadcrumb of context in there that…
Robb Kidd (he/him) 01:06:46 is probably… I might park an agent to go, investigate who?
Kayla Reopelle 01:06:50 Where?
Robb Kidd (he/him) 01:06:50 Where does this come from?
It'll go do the spelunking.
Anyway, yes.
Kayla Reopelle 01:06:59 Alright.
Robb Kidd (he/him) 01:06:59 Hannah, huge fan of, punting on the name and keeping it as is. Until we know what we want to do, let's not change it.
Hannah Ramadan 01:07:06 Great. Also, thank you, Bart. It's helpful to hear that, like, two, like.
3 and 4 is useless, and, like, opera… having the operation name and the name would be, like… Pretty neat.
Robb Kidd (he/him) 01:07:17 It doesn't have a name, so something's gonna be there, but…
Hannah Ramadan 01:07:19 Yeah, otherwise it just doesn't make… it just, yeah, not helpful at all.
Cool.
Robb Kidd (he/him) 01:07:29 Cool.
Kayla Reopelle 01:07:30 All right, everybody. Thanks, thanks for staying over. People have one more minute. Shawn, do you want to talk about this this week, or would you rather wait until next week?
Xuan Cao 01:07:42 I would be very shocked. Just, just rant about this, noise label, that every time I open this, township, this huge label, I don't really know what is the person is, it's just, Yeah, and also for the, reviewer, and also it's just a long list of people that is, Oh, I think we, Should, you know, merged to the same, reviewer group.
Yeah, that's pretty much it, pretty much about it, yeah.
Kayla Reopelle 01:08:11 Okay.
I agree with that.
Robb Kidd (he/him) 01:08:15 Oh, I'm sorry, Hanukkah. Kayla, just go ahead.
Kayla Reopelle 01:08:18 I… yeah, I think we're probably on a similar page, just based on what I heard so far. I think that the long… reviewer names, they might be, like, a leftover from, you know, previous ways of working on the repo that I don't know if we're adhering to today. So I think there could be some… space to change that. I don't know why the labels started showing up, so, I would have to dig into that. I'm not sure if that's, like, related to Renovate, or… if there's some requirements there, yeah, I have no idea where those are coming from. Rob?
Robb Kidd (he/him) 01:08:54 If you scroll down to the labels… to the labels getting applied to this.
Kayla Reopelle 01:09:00 This one's simpler, but, like, let's look at this one. This is every instrumentation that is touched in…
Robb Kidd (he/him) 01:09:06 And there's an action where those labels got a… in the, like, history… in the… chronology of this. If we scroll down and look at… at… the actions and stuff, some… we'll see.
Kayla Reopelle 01:09:19 We added…
Robb Kidd (he/him) 01:09:19 paragraph.
Kayla Reopelle 01:09:20 Y…
Robb Kidd (he/him) 01:09:21 Of labels getting applied somewhere in here.
Kayla Reopelle 01:09:23 And here we go.
Robb Kidd (he/him) 01:09:24 GitHub Actions.
There's an action that's configured, I think, to probably look at paths and apply labels based off of path… what was modified in this PR? Was it in these.
Kayla Reopelle 01:09:37 That's the…
Robb Kidd (he/him) 01:09:38 These pads met to these labels.
I suspect that's what's doing it, and we can choose whether we keep that or not.
I agree, it's… A lot.
Kayla Reopelle 01:09:52 Yeah.
Robb Kidd (he/him) 01:09:53 I am pro just using the groups for reviewers. I know Francis was the one who said he wanted to be listed explicitly.
maybe… Maintainers can choose whether they are named.
I'm fine not being named in that list.
Also, Francis and Robert and the Shopify folks are not as active anymore, so maybe… they're… Reserve space in the list.
Isn't as critical now.
Kayla Reopelle 01:10:24 Yeah, I think, I'd be curious.
I'd be curious if we open a PR… oh, Sean's gone.
If, just, like, if people would chime in, if they still had problems with it, then maybe we could have a discussion.
Robb Kidd (he/him) 01:10:37 I think that's the right place to have a conversation. Propose the change, where it's just groups, and tag all of the people, and say.
We're doing this unless you protest.
And if you protest, we'll probably just leave your name in. Remove everybody else.
Kayla Reopelle 01:10:54 Yeah, yeah, that's a very viable solution.
Cool.
Robb Kidd (he/him) 01:11:00 And as far as…
Kayla Reopelle 01:11:01 Everyone?
Robb Kidd (he/him) 01:11:02 As far as labels, I guess, we could find out what's doing it? I think it's a GitHub action that got configured to do it. Who made that?
Kayla Reopelle 01:11:09 I'd get up.
Robb Kidd (he/him) 01:11:10 And then we can ask that person.
What problem is this solving?
Kayla Reopelle 01:11:14 Yeah.
Yeah, I think it's relatively recent, so it shouldn't be too deep of a git history to figure out.
Robb Kidd (he/him) 01:11:21 Cool.
Alright, then.
Hope to see y'all next week.
Kayla Reopelle 01:11:29 Yeah, next.
Have a great week.
Robb Kidd (he/him) 01:11:31 Thanks for coming.
Bart de Water 01:11:33 So far, I don't feel too scared to rejoin later.
Kayla Reopelle 01:11:37 Nice, good.
Wonderful.
Bart de Water 01:11:40 Patience with this newcomer, thank you.
Robb Kidd (he/him) 01:11:42 What?
Kayla Reopelle 01:11:43 Bye!
Bart de Water 01:11:45 Nope.
