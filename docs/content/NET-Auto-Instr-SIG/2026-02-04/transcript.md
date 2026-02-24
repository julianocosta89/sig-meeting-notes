SIG: .NET Auto-Instr SIG
Date: 2026-02-04
Duration: 9 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 00:14 Hello.
**Igor Kiselev** 00:18 Whoa.
**Zach Montoya** 00:25 Looks like we've got a small audience today.
**Igor Kiselev** 00:26 Hmm.
**Zach Montoya** 00:27 Is Hotel Unplugged still going on?
**Chris Ventura** 00:34 I don't know.
**Igor Kiselev** 00:36 I have an internal meeting in the company, so a lot of People. Zah.
**Zach Montoya** 00:42 Huh? Okay.
No, that checks out.
Alright, I guess we could just run through, the agenda with the folks we have here. Let me just…
Boom.
Alright, I'll share screen, and we can…
Just gonna go through… I know we don't have a lot of people here, so maybe I won't be able to make decisions, but at least we can…
Just do a quick… Just a quick sanity check.
Arts… Alright, so we got a bunch of, the dependency updates.
So we can approve those and merge those… Later…
Mongodb traces, so there's some semantic convention updates.
Looks like this interview has a lot of conversations.
I imagine Ludmila is commenting on this.
Okay.
**Chris Ventura** 01:53 Yeah, last I checked… There were problems with the tests…
**Zach Montoya** 01:59 Okay.
**Chris Ventura** 02:02 But I didn't check, this morning.
**Zach Montoya** 02:05 Okay. Yeah, I think we can follow up.
Okay, yeah, it has at least one approval, so it's like it's… On the right track.
And then we have a couple other in drafts. I'm not sure if there's any…
status we should be aware of? I don't know, Igor, if you have anything on your end. If not, we can just,
Skip over it for now.
Alright, so let's see if there's any… New issues? Okay.
Attestations for…
**Igor Kiselev** 02:43 Pull request, for pull request, the dependent, Alexei is not here, but, his pull request on, reviser, on using
up, all the user loading context is nearly ready, so it's passing all tests right now. So, with leftover, it's some discussion about, environment variable naming, if we would rename it, if we need to support old, and so on, and some cleanup. So,
While, some provider-based solution, Have a little bit.
more mature right now, solution without a profile, it's just freshly done and, still may require some minor cleanup. It's a little bit hacky,
But it works. The high key, the main part, hike is that, we have to, instead of allowing application to start up normally, start an application from our startup hook directly.
So we just push control to main method of application form startup hook, and then terminate an application after it exited. Otherwise, we are not able to contain an application in secondary abdomain, and we need to do it to be able to control both assemblies to be loaded. So…
it was original idea that we know from the beginning that we plan to do that, so we need now to review it. If anybody have, concerns, we still have a fallback plan. We could have a, double option, so have, still, dependence, depth, JSON and, store folders for, non,
or non-profile resolution, or we could suggest splitting it into two different ZPAR hives, because it would make sense in that case. Or we could use that hacky option.
**Zach Montoya** 04:52 Gotcha. Okay. Yeah, I think I would probably need to review this in a little more…
To… have a good opinion.
**Chris Ventura** 04:59 Yeah, it may also be time to discuss whether or not we want to support a startup hook-only approach.
Given some of the other things we've been building into this project, so things like, continuous profiling.
Because the profiling signal won't work without the profiler being set up. Similarly, we've got a handful of no-code instrumentations now.
Where you can even do custom instrumentation. And all of that requires the profiler.
So… We may finally have reached enough.
Features to justify a big change, but it may take a while to get there.
**Zach Montoya** 05:58 Yeah, that's a good point.
Okay, yeah, we can certainly discuss that. Oh, we have more people around.
Okay, cool. I can, start taking a look at these changes. I'm sure it'll take a while to go through, but…
Start diving in.
**Igor Kiselev** 06:15 Unfortunately, it's really hard to split the change in a part, because it's a lot of change how we build our application, and at the same time, a lot of change how we use and build artifacts, and you really couldn't split it into parts.
**Zach Montoya** 06:33 Got it.
Okay.
So, let's see, so going back to issues, we had one that Robert opened up…
Looks like there's some discussion about, you know, relating artifacts to releases.
**Chris Ventura** 07:10 Yeah, I'm… I'm not sure how big of a need this is…
**Zach Montoya** 07:19 Yeah, I personally haven't done any of GitHub attestations for any of my repos, so…
Seems more like a nice-to-have, and I guess… It helps customers know that
the artifacts are authentic, but I don't… I mean, this… isn't blocking.
**Chris Ventura** 07:38 Right. I kind of want to hear from people with a need to do at the stations to see just how much we want to invest in it beyond…
What we're able to do, more simply.
But I think we can discuss this, async.
On the ticket.
**Zach Montoya** 08:02 Okay, yeah.
That sounds fine.
Okay, so with that, that's all the open issue, or the new issues. I… see, I doubt we have any discussions… okay. And otherwise, I think, I don't think we have any more…
Issues right now, they need to go onto…
the board, we have the work that's in progress with the MongoDB, And the assembly loading…
So, I don't think there's anything unsettled over here.
So, I think that's… that was a very quick, agenda today.
Was there any other items you guys wanted to discuss while we're here, or,
Maybe we wrap early?
**Chris Ventura** 08:54 No, I think the big one we already talked about…
And the fact that all of the tests are passing is a good sign.
because our previous experiment with the, with the load context.
I… We ran into failing tests.
Huh?
**Zach Montoya** 09:21 Yeah, I guess that's all for today. Cool, well…
Thanks, guys. See ya, see you next time.
I…
