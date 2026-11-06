SIG: Browser SIG
Date: 2026-11-05
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze (Palo Alto Networks)** 01:32 Hey, what's up, everybody?
**Martin Kuba (Raintank, Inc. – Grafana Labs)** 01:35 Hi, Jared.
What's it going?
**Jared Freeze (Palo Alto Networks)** 01:54 Oops, I was gonna take that one.
I guess I have nothing on the list today. I don't know.
Let's see…
**Aditya Reddy** 02:30 I'm not able to access it in the work system, so I'll just mention out what I have. I saw your… I followed your entire thread. Jared, I… was about to say, I'll test it on a real app outside, like, at Northwestern Mutual. I'll… give me, like, a day, I'll come back with what I have… what I find.
**Jared Freeze (Palo Alto Networks)** 02:51 For which, PR?
**Aditya Reddy** 02:53 For, the Browser 1.0, the one you put out, let me see… I need my phone delivered.
Oh, yeah, the first step, the 548.
**Jared Freeze (Palo Alto Networks)** 03:18 And you can.
Oh, yeah, Maxime's here.
**Aditya Reddy** 03:46 Yeah.
You put out 552, right, for this, like…
**Jared Freeze (Palo Alto Networks)** 03:54 That's right, yeah. When I linked it? Yeah, February, too.
Yeah, so this is the… what we had talked about last week, I wasn't sure if people were… Cool with the name, we had talked about API versus… like, calling it instrumentation-based, but it sounded like we probably want it to be broader, so that's what I proposed.
Yeah, and then Jackson's comment, I agree. I put this in so we could talk about it, but just having it be at, at root probably makes more sense, because the package doesn't have anything else in it yet.
So… Yeah, people can take a look. That'll help open up the 3.0 migration, since right now there's… For those that weren't here, you know, there's a dependency where you have to… you know, release… instrumentation and the SDK together in concert, which is annoying. It also pulls in Web Vitals for people that Don't necessarily want instrumentation.
They just want the SDK, so… Or instrumentation-based, for that matter. Building in their own instrumentation, and then… Pulling ours down, but yeah.
It's cool, things are moving forward, which is nice.
**Maxime Quentin** 05:24 Yeah, sorry, I did not have time to review this one, but I'll do it.
**Jared Freeze (Palo Alto Networks)** 05:33 Appreciate that.
Does anybody else have any general topics? If not, maybe we could just look at the pull request dashboard, just see where things are at.
Yeah, I think this one… Yeah, this is a bug. I think it needs… Just a little update.
Yeah.
Yeah, people can check this one out. There is a bug in, The timestamp was not added to, nap timing and resource timing?
Small one, but would improve the quality of that instrumentation a lot.
**Maxime Quentin** 06:47 Boom.
Do you need, like, another reviewer, or should I focus on the instrumentation one first?
**Jared Freeze (Palo Alto Networks)** 06:57 Yeah, definitely the base first, the migration, because that is blocking.
**Maxime Quentin** 07:04 Yeah.
**Jared Freeze (Palo Alto Networks)** 07:04 Yeah, because we…
**Maxime Quentin** 07:05 written.
**Jared Freeze (Palo Alto Networks)** 07:06 don't want to release again until it's pulled out. I think that was the idea. The last release failed, by the way, so it made it a little easier, actually, because then we didn't have to, like, backtrack or deprecate or do anything.
So.
**Maxime Quentin** 07:22 I'll focus on that on my side.
**Jared Freeze (Palo Alto Networks)** 07:25 Okay.
Yeah, let's see, waiting on reviewers. Okay, so I think there's another one here… Yeah, this, Non-errors, I think we had talked. There was definitely some comments, I didn't know my video… See, where was it at? Yeah, I think, Jackson, you looked at this one as well.
Yeah, I think, yeah, we'll just wait on… Re-requests on that one.
**Aditya Reddy** 08:18 Yeah, I was about to say, most of them are tiny in.
the… I think I forgot to re-request. Yeah, I was just waiting on Jackson's review.
**Jackson Weber** 08:36 Oh, sorry, is there a request I should take a second look at? Sorry, I heard re-request. I wasn't sure if that's what you meant.
**Aditya Reddy** 08:45 Yeah, the 494.
**Jackson Weber** 08:48 494? Yeah, here, let me, let me review that, this morning.
**Jared Freeze (Palo Alto Networks)** 09:01 Cool. Yeah, I guess, everyone can just go through.
the list, and yeah, I'll take a peek, let's see, waiting on authors… I think this one got left behind. We may have to… This one, we may need to recreate. I think this one… we'll have to look at, but I think this was a feature we needed.
Yeah, really just looking forward to, Yeah, to… whatever people are tagged in, and then, yeah, we'll just focus on… on Maxime's update, so that way we have the new instrumentation base.
I'd still like to make a integration test, I didn't make an issue for it, that pulls in the old code with new code, so that we have all the combinations. So we'll use instrumentation from… JS Core, so fetch, and then we'll pull in our XHR, run that in the SDK, see what happens, do builds, do VEET, Some other package, maybe.
**Joaquin Diaz** 10:18 There is already an internal test doing that, I think.
Testing both the old one and the new one, and comparing results.
I… I think I did it when we merged the first one, the fetch instrumentation. It's not doing anything with the new SDK, or it was just testing the instrumentations, side by side.
**Jared Freeze (Palo Alto Networks)** 10:42 Okay, cool. So that should start failing for you, then, Maxime.
I wonder if that's already failing.
**Joaquin Diaz** 10:49 Maybe still hooked up to the CI, that's probably why it's still failing, but it's there.
**Jared Freeze (Palo Alto Networks)** 10:55 Oh… That's right.
**Joaquin Diaz** 10:58 I don't remember.
**Jared Freeze (Palo Alto Networks)** 10:59 I think it is, because it uses a real browser, right?
**Joaquin Diaz** 11:03 Easiest pay rate.
**Jared Freeze (Palo Alto Networks)** 11:06 Yeah, yeah.
Okay, that makes… that makes sense.
**Joaquin Diaz** 11:14 I can take a look.
Check if it's not hooked up, I can create a PR.
But yeah, that one… yeah.
That compares both, the new one, the old one.
Yep.
**Jared Freeze (Palo Alto Networks)** 11:30 Got it.
Cool, yeah, so I guess we just need a new file then, which is… importing both.
**Joaquin Diaz** 11:44 You… you want to import both in the same… Like, app, desktop, and run both together.
**Jared Freeze (Palo Alto Networks)** 11:51 Yeah.
Just so…
**Joaquin Diaz** 11:53 Yeah, this is…
**Jared Freeze (Palo Alto Networks)** 11:54 of builds.
**Joaquin Diaz** 11:56 Okay, yeah, this is not doing… this is just… They… it… add them separately to separate apps, and then compress the output, and see if it matches. But it's not running them to a…
**Jared Freeze (Palo Alto Networks)** 12:08 Yeah, this is super useful. Yeah, I think we can just use this as a jumping-off point to have a combined The combined version.
Yeah, cool.
Alright, does anybody else have anything?
**Maxime Quentin** 12:39 I'm good on my side. Thanks.
**Jared Freeze (Palo Alto Networks)** 12:43 Okay.
Cool, we can cut it short today. Appreciate everybody's time.
**Jackson Weber** 12:53 Awesome, thank you all.
**Jared Freeze (Palo Alto Networks)** 12:55 Alright.
**Maxime Quentin** 12:55 by me?
