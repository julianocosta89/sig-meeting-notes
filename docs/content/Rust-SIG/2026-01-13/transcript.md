SIG: Rust SIG
Date: 2026-01-13
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Cijo Thomas** 01:20 Hello?
**Franco Posa** 01:28 Hello?
**BA Björn Antonsson** 01:30 However…
**Cijo Thomas** 01:34 Let's wait a couple of minutes… Yeah, feel free to add your name to attendees list, and any topics to be discussed as well.
I need to take a cube break, so I'll be back in, like, one minute.
Yeah, wonderful.
Hey, sorry, I had to take a quick break. I am back. Let me… Reshare my window, and get started.
Okay, sharing seemed to have worked.
Okay, we can get started. Yeah, nice to see all of you again. I think… This is probably the first time we are meeting in January. Oh, yeah, we had one last week, but only Scott and Franco attended.
Hey, Christian, like, welcome back.
thing we can get started. I have a very small item in the agenda, which is basically going through All the milestones, and updating them to be more realistic, because it was all sometime in the 2025 was the date we planned to achieve few things. We haven't quite reached there, so I put, like, new dates.
The TLDR version is, like, OTLP for all signals, and Tracing API.
is now having a target, 3 months, 2 and a half months from now, tracing SDK, another three months from now, sorry, another 3 months from that date.
Looks quite reasonable now, because we have unblocked most of the… Tokyo Tracing-related discussions, so hopefully it's now, going to be, like, much easier.
Any comments on that one? I don't think we have any… Like, anyone other than probably people in this group committed to work on improving or achieving these goals, but if anyone feels this is aggressive or too late, please feel free to speak up.
Okay?
Yeah, the next one. Yeah, Bjorn, I think someone else also reported the same thing.
I will take a look, because last time I tried to fix it, I didn't have permissions, but I now have permission, so I should be able to fix it, because we had to redo a lot of things to accommodate the change of schedule starting this year.
So most likely, something bad happened while we copied, so I will make sure it is correct before the next meeting.
**BA Björn Antonsson** 07:13 Boop.
**Cijo Thomas** 07:14 Yeah.
Any important topics to cover? Otherwise, I'll just, like, go through a couple of PRs, from the main repo and the contrib repo, since, like, Franco and Christian, you both are here, I'll probably start with the one from… country.
I think, like, one of the main goal is, like, if you want to get tracing API to stable, we really need to validate with at least one instrumentation library. We currently have two.
Actix, and then tower.
Tower is… I think it only had metrics, we are just adding, like, tracing this PR. So this is very important, like, in my view, this is, equally important as the, stable release of the API itself.
I believe I left a comment, like, sometime yesterday.
Yeah, okay. Yeah, I think, Franco, you already replayed, yeah. In my view, like, we, I mean, once the… Readme… merge conflict is resolved, like, I'll go ahead and merge, and then we can take, additional improvements, one by one, because this is already quite big, and we don't want to, like, hold PRs too long. Unfortunately, it took, like, 6 months, but hopefully we can make it faster.
Christian, Franco, like, anything, you want to discuss in this PR? Otherwise, once the conflict is resolved, I'll go ahead and march.
**Franco Posa** 08:48 No, that's fine. I think we just want to do a fast follow with fixing the span name to Matt's semantic conventions, because we don't want to let that hang out until it gets released.
**Cijo Thomas** 08:58 Yeah, so this is only PR from Contrib, like, and from main PR, I think Christian had a PR waiting for too long, let me… Open that one… I think it's this one.
I left some review comments, like, earlier, but I didn't get a chance to revisit since you, sent this, like, last week.
Anything which you want to bring? I only had, like, one comment which was… I believe that command is resolved now, so I'll need to take a quick look. Beyond, like, would you have some time to take a look at this one? I think we discussed this a couple of times in previous meetings. This is basically using, the… improving the appender for tracing to incorporate attributes from span.
**BA Björn Antonsson** 09:53 Yeah, I can absolutely take a look.
**Cijo Thomas** 09:58 Yeah, thank you. Yeah, there were, like, some interesting things, like, we are storing attributes into the span as an extension, and then we have to retrieve it all the way till we get to root, and then we have to add all of them back to logo code. It's somewhat intense. I'm curious to see whether any benchmarks are already happening. Christian, if you have some time, can you add, like, one or two benchmarks? We already have a benchmark for… This happened, huh?
I think it… should exist right here, yeah. There are a few benchmarks, so if we can add, like, one benchmark, or maybe two, like, showing spans from multiple depths, how does it impact the overall timeline? That would be a good thing. It's still under… feature flag, so even if it's slow, it's fine, like, I'm quite curious on how much, how much more CPU it's going to consume, because we have to store a bunch of things.
and retrieve it, and then add it to each and every log. So, it's somewhat involved, so if you can add a benchmark, I think that would help, reviewers also.
**Christian Leghadjeu** 11:12 Alright, alright, let's say, honey.
I'm going to say true to…
**Cijo Thomas** 11:19 I think you can look at the existing benches, like, we have, like, few, so you can just add, like, one extra, with some spines on top.
Yeah, that's the main thing, and there are, like, few open peers. I think, like, folks are still, like, coming back from vacation and, going through the list. I started looking at a few open issues.
Just, last few days, so, hopefully, like, we'll get things picked up. We have a huge number of pull requests open in the main repo, and in here also, like, somewhat high. This is not very good, so I'll… Go through the ones and start cleaning up things.
Okay, any other topics to discuss?
**BA Björn Antonsson** 12:06 So I actually have two PRs that has been outstanding since before Christmas. It's not me, it's, I can give you the numbers instead.
**Cijo Thomas** 12:18 Yeah, I noticed, like, a few of them, yeah, it's very…
**BA Björn Antonsson** 12:21 3262 and 3267.
It's, external.
**Cijo Thomas** 12:28 I think we discussed this in the past also, yeah, it's… Okay. Yeah, I need to just take some time and review this one. Yeah.
**BA Björn Antonsson** 12:36 I mean, because that is… Proper one, proper fix, actually, to make sure that the things don't break inadvertently.
**Cijo Thomas** 12:49 Okay, so this one requires urgent review. It's… yeah, I mean, we have, like, quite a few from before Christmas.
**BA Björn Antonsson** 12:58 Yeah.
**Cijo Thomas** 13:00 And there are a few, which is improving the overall.
**BA Björn Antonsson** 13:04 Ap Surface.
**Cijo Thomas** 13:06 Oh.
Yeah, I also sent, like, few, I think, like, Lilith or some other folks approved a few of them, like, but those were, like, very minor things. I was just, like, warming up with Rust again after I gap.
Yeah, thanks.
I'll take a look at that. I did look at it, like, a few months ago, when you initially asked me to, and then I realized, okay, this requires some focus time to really look at it. I understand the problem very well, I just need to spend a little more time reviewing the solution. It already helps that you already reviewed, so I have your approval, which is already a good thing.
Okay, I'll take a look at that one, and for contribib, I think there are a few… Like, ab… like, renovate, dependable thing, which I have asked Lilith to help, because these are all, like, in a component which he maintains.
Then the… there is another thing which I have started, like, very briefly with, which is to clean up the country repo. And first step was I added, like, owners and status to every… every crate we have.
And I think, like, sometime in the next few days, like, when I get time, I'll modify the repo so that… whenever an issue or PR is created, the listed owners gets tagged automatically. So, there are some scripts which is used by other OpenTelemeter repos. I'll see if I can copy that, so people get notified for those components which they are listed as owners.
And another month from that, we need to do a cleanup, which is to… remove components which does not have owners. I think that should… There aren't that many. Maybe, like, we'll get rid of… One or two. Stackdriver did not have anyone actively looking at it. The Datadog one, I believe, is no longer required because OTLP is good enough.
So that these two, we may be able to get rid.
Similar thing in the main report, I think, like, in the main report, so we have… the blessing from spec to deprecate Zipkin and the Jager Propagator.
So that should reduce the load a little bit. Not significantly, but yeah.
Yeah, I'll create issues. I think I already created issues, but if anyone wants to, like, help with those things, those are, like, relatively easy things, yeah, deprecation of.
Jaeger, and deprecation of Zipkin.
Which we should be able to tackle, towards the next milestone.
Okay, if there are no topics left, let's meet again next week. By that time, hopefully, people are back from vacation and actively reviewing all the open issues.
Thank you, everyone. See you next week. Bye-bye.
**BA Björn Antonsson** 15:59 Myers.
