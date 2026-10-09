SIG: Python SIG
Date: 2026-10-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo  Magliocchetti** 00:36 Hello, Lukas.
**Lukas Hering** 00:40 Hi, Ricardo.
**Riccardo  Magliocchetti** 00:49 How's it going?
**Lukas Hering** 00:52 It's going pretty good.
Are you, sorry, I thought, I thought you were on vacation.
**Riccardo  Magliocchetti** 00:59 No, like, I'm… I'm traveling… Between conferences, like, I've attended one on Monday, and then Friday I am flying again for another one next week.
So…
**Lukas Hering** 01:20 Which conferences?
**Riccardo  Magliocchetti** 01:23 I've been to Observability Summit Europe on Monday and I have PyCon Greece.
Next week.
**Lukas Hering** 01:34 Awesome.
**Aaron Abbott (Google LLC)** 01:40 Hey folks, how's it going?
**Riccardo  Magliocchetti** 01:42 Hey?
**Aaron Abbott (Google LLC)** 01:43 Hey.
I thought you weren't gonna be here, Ricardo.
**Riccardo  Magliocchetti** 01:53 2 I'm not on video, I'm just traveling for conferences.
Okay.
Hey, Tammy.
**Aaron Abbott (Google LLC)** 02:16 Should have done that.
Oops, sorry, I need somebody in the dock.
**Lukas Hering** 03:30 I'm fine with doing the… Triaging, unless someone else wants to.
**Aaron Abbott (Google LLC)** 03:39 Oh, we don't have Tammy today?
**Lukas Hering** 03:41 No, she was just saying she has a sore throat.
**Aaron Abbott (Google LLC)** 03:45 Oh, okay.
Yeah, sure. Please, Lukas.
**Lukas Hering** 03:51 Let me share.
Okay, yeah, maybe we can start with, these two issues… Not sure who put these up, but we can start with these.
Okay.
Oh, these are just the… sorry. These are just the dashboard links.
**Aaron Abbott (Google LLC)** 04:44 Yep.
**Lukas Hering** 04:46 Correct.
Okay, yeah, we can start with, Yeah, the… The main repo first.
So, yeah, let's go… I guess we usually start… Waiting for reviewers, bottom up.
Is that our general convention we're following?
**Emídio Neto** 05:22 Yeah.
**Lukas Hering** 05:23 Okay.
Yep, we can… Start with this one, looks like… Got one from Mike.
Sure. Import agents. Md.
from Cloud Md. So it loads.
I thought we already had this.
Maybe it's on the income trip.
Okay.
**Riccardo  Magliocchetti** 05:43 It is elastic.
like, isn't like recent cloud codes also reading agents.md these days.
**Lukas Hering** 05:55 Is it now? I don't know.
**Riccardo  Magliocchetti** 05:56 I think it was very recent addition, but let me check.
**Aaron Abbott (Google LLC)** 06:07 Yeah, this is a bit of a mess. There's also like the Copilot instructions in a separate directory too.
**Lukas Hering** 06:25 Okay, yeah, we can follow up on this.
Okay.
Okay, Dependabot, you can skip that.
Prevent recursive attribute value crashes.
Attribute values containing self-referential or nested attributes could raise recursion error during cleaning.
Okay, so this looks… it's probably related to… the the.
Extension work that we did for attributes.
So…
**Aaron Abbott (Google LLC)** 07:13 Yeah.
**Lukas Hering** 07:15 Yeah, we can… Maybe, I know Dylan worked on the… that original PR, so maybe Dylan can take a look. I can take a look as well.
**Aaron Abbott (Google LLC)** 07:26 Yeah, it looks like it's limiting the depth.
which Which works. I wonder if there's, like, a… Better way to… Check for recursion.
**Lukas Hering** 07:40 Self-referential. I mean, I don't know if like.
I think, I think this is specifically, like.
Yeah, there's a self-referencing, I don't even know if that, like, we should… I don't know if we should just reject that, like…
**Aaron Abbott (Google LLC)** 07:54 Yeah, I think detecting it is kind of hard. Like, maybe you could do this… It might be expensive to try to detect it instead of just doing this simple depth check.
**Lukas Hering** 08:07 Yeah, okay. Yeah. Yeah.
**Aaron Abbott (Google LLC)** 08:10 But it would be nice to detect it if we could do it efficiently. I think people probably don't want To just recurse until you hit the limit seems not great either.
**Lukas Hering** 08:25 Okay, and then there's a few from me.
This one's just to add, So… the work I did earlier to add a URL through transport for the exporters.
There was a regression last release where This didn't, respect the proxy environment variables, so we switched it back to being requested as the default.
But the JSON exporter is actually still defaulting to URL of 3.
So, yeah, so if anyone has time to take a look, they can take a look.
Do a few more. Okay, so I already brought this up, so maybe we can skip this.
Semantic conventions, stabilization.
This I'll bring up. It's one of the topics.
Maybe we can go to contrib quick.
Oh… Store handlers and formatters on instrument.
Okay… Factory… okay, so it looks like, yeah, probably our cleanup isn't… Doing what it should.
Okay.
Yeah, this is… I would imagine most people need to uninstrument, but we can… We should definitely support it, so… Okay, a few more… Okay, this is a docs change document output.
For the rich console exporter… Okay.
Yeah, I mean.
This does look like it's just caught, but I guess we can add it.
Yeah, I don't have as much familiarity with Bridge Console, so if someone else wants to take a look, they can.
Okay, I think we can probably… Go to the topics now.
**Leighton** 11:48 Thanks Lukas.
**Lukas Hering** 11:53 Okay, yeah, first one from me, Just thought I would bring some attention to this, so… Yeah, so we finished up… All of the issues for… that were, that we identified as being needed for the logs stabilization.
So I've opened up a PR stack here that just does the changes for the the API, the SDK, and then the exporters.
I guess one call out here, that I did do was… I actually kept the old imports, the old module with the underscore prefix.
And, I just added a deprecation. I just deprecated the entire module, so… People will still be able to import it.
But it will, it will just raise the deprecation warning here. So, yeah, just update the SYS modules to point to the new location.
the new public module.
We can probably remove this at some point. I mean, technically, we… We could just remove this right away, but I think we should just try to be nice to our users, because I'm guessing a lot of people are still using this if they're using OpenTelemetry logs.
So yeah, I think we should definitely try to get this out before the next release.
Be nice to close this up.
And yeah, thanks, Lane, for the, Initial approval.
Yeah, Aaron.
**Aaron Abbott (Google LLC)** 13:41 Yeah, I don't know if we have a bug for this already, but… just given some of the, like, concerns I've heard about Python, like, our implementations of OTEL, I was wondering if we should add some benchmarks, especially for the API, like, in the no-op state for the logging SDK, like, I don't. I don't know if there's much better we could do, but like, one concern is if the API shape is… Bad for performance, or, like… I don't know if there's much we could do with Python, but I know there's a lot of effort made in Java and Go to have, like, zero copy for logging calls.
So yeah, maybe just, like, some… benchmarks as we go stable. I think we discussed, like, the possibility of doing SDK 2.0.
If we need to, but if the API is not, like.
conducive to writing a performant SDK.
Maybe we should look into that.
**Lukas Hering** 14:50 Got it, okay. So do you think… I guess we could consider adding that.
Before we do this, or…
**Aaron Abbott (Google LLC)** 15:02 Yeah, I mean, I think it would be more part of, like, a, like, go-no-go kind of decision. I really would… that would really suck to, like, break the API or whatever, but… So so I we have some benchmarks already in some of the yeah, I see there's 1 test benchmark log encoder.
Like, we have this PyTest benchmarking set up, but… It would be good to just, like.
Make a decision based on the.
performs. It also doesn't have to be this PyTest benchmarking thing, like, we could just… make sure the no-op behavior is pretty performant. I think we might have something similar for Spence. If you want, Lukas, I can.
I can follow up, I can, like, file an issue, or I can poke around and see if we already have something like that.
**Lukas Hering** 15:46 Yeah, okay, yeah. I think, yeah, I think, like, most people will probably end up actually just adding the handler to the built-in Python logger.
So there's not too much API… concern there, but yeah, I agree there, so…
**Aaron Abbott (Google LLC)** 16:05 Yeah. Like, so for example, I know we have the non-data class variant to call the API, which I think It could be good for the log handler where you already have the fields and you don't want to, don't need to create a bunch of boxes, just for example.
In the year, yeah.
**Emídio Neto** 16:20 Yeah.
I should say that, we do have some benchmarks already, but… Minimal stuff.
Just cataloger, and, the emit… Method, but nothing, like, extensive.
So maybe we can just improve what we already have.
**Aaron Abbott (Google LLC)** 16:42 Yeah.
**Emídio Neto** 16:44 Okay.
**Aaron Abbott (Google LLC)** 16:45 Cool.
I will file an issue.
**Emídio Neto** 16:50 Yeah, that's true.
**Lukas Hering** 16:53 Yeah, so yeah, it looks like we do have…
**Emídio Neto** 16:56 Yeah.
**Lukas Hering** 16:57 This is the deprecated one, though.
**Emídio Neto** 17:00 Yeah.
**Lukas Hering** 17:01 And then… Yeah, this year, okay.
Anything else?
Emilio?
**Emídio Neto** 17:13 No, thanks for working on this, Lukas.
**Lukas Hering** 17:21 Okay, thanks. Thanks, everyone.
Okay. Carlos.
PRs that are… Ready to be merged.
**Carlos Alberto Cortez (Dash0)** 17:30 Yeah, I was going through some of the PRs and Yeah, actually, there was one more, but it was a good merge regarding TresID radio-based sampler.
Yeah, I just wanted to get the attention from people here. I was doing a symbolic… I was, approving in a symbolic fashion this one.
Please take a look. This… this was kind of a bug, you know, like, basically, when you are getting the unending call, at the spam processor, you should still be able to modify spans, and this… this PR fixes that. We have enough approvals, yeah, I don't know if we need something more, or… There's somebody else that would like to take a final look, otherwise it looks good to go.
**Lukas Hering** 18:18 Yeah, I think I… kind of took a look through this. Yeah, we can probably merge this pretty soon. Thanks for the call.
**Carlos Alberto Cortez (Dash0)** 18:28 Yeah, thank you for that. Yeah, driving, so the second one, yeah.
This one is, I would say, relatively simple, just, like, improving the checks. Basically, it's just, like.
Upon propagation.
the span context was compared against the invalid span context instance, and then, of course, if that's invalid, if it was invalid, you didn't propagate. But what other languages do is that you actually check Not whether this is equal to the internal instance or public instance you have, but whether the actual span context is invalid or not valid, you know, itself.
Just making things a little bit more robust, so to speak.
This is, as I said before, this is what Java and Go do.
And it should be relatively straightforward.
**Lukas Hering** 19:25 Yeah, this seems reasonable. I guess it's… I'm not… I can't remember… What the exact difference is here.
But, yep.
This… yeah, this seems like a reasonable change.
Thank you. So this one got merged.
Or… oh, no, this isn't… this is not…
**Carlos Alberto Cortez (Dash0)** 19:51 Yeah, they're having a few PRs regarding timeout, that's why, yeah. This one is just doing validation.
Probably the important question remaining is that if you could scroll down to the end.
There's a person asking, like, this is not currently used.
Oh, my bad, I was… Pinging the incorrect person there. But basically, yeah, this person is asking, like, do we need to validate this? It's not being used currently.
And I think it… why not, you know? Even if the value is not being used as now in the current implementation, it would be nice to have a valid value and have the user know that this is incorrect.
No strong feeling other than that, yeah.
**Lukas Hering** 20:41 Yeah.
I don't think it hurts to add the validation.
I do notice there's, like, quite a few of these, like, kind of, like, little, almost trivial PRs floating around. I kind of wish they would just submit one, but, yeah, we can probably merge this.
Or get this merged soon.
**Aaron Abbott (Google LLC)** 21:06 I don't think we have Dylan on the call, but he also said something in his comment about Not using this environment variable, is that… something that's feasible.
I would… I would guess, no, this is just, like, the… I assume it's just the batch… the standard environment variables from the spec, is that right?
**Carlos Alberto Cortez (Dash0)** 21:26 Yep.
**Lukas Hering** 21:28 Yeah, and it doesn't look like this touches that at all, so… I feel like… Yeah, I mean, plus, yeah, if we were to remove it, it would be a, like, breaking API change at this point, I don't…
**Carlos Alberto Cortez (Dash0)** 21:44 Yep.
**Lukas Hering** 21:44 Yeah, so…
**Aaron Abbott (Google LLC)** 21:48 Okay. Sounds good. Maybe we could just reach out to Dylan on Slack and, But I don't think it's blocking. It's a really minimal thing.
**Carlos Alberto Cortez (Dash0)** 22:02 Yeah, there was maybe, I saw another PR, but I cannot find it now, and it's… that one is still open, or it was still open earlier today, and it was touching, the environment variables, and I just left a comment saying that.
It's doing the same thing twice, but anyway, I will… Look for that later.
But it was about timeout as well.
Or duration, either one.
**Lukas Hering** 22:32 Okay.
Yeah, see, we have, like, a lot of these similar, VRs here for… Just validation of these timeouts.
Okay.
Yeah, I can, take a look at Some, all these.
**Carlos Alberto Cortez (Dash0)** 23:00 Perfect, thank you.
**Lukas Hering** 23:09 to… abuse.
Oh, yeah.
My expert time… Yeah, it's almost like maybe we just need to have, like, a… Yeah, I think someone… I think this guy said he wanted to pick up one of these issues.
to, I guess, spike on… How we maybe want to.
handle this.
But yeah, it might also make sense to just have, like, a little… internal… Helper function class thing that… Does all this so we don't have to, you know, keep going back to every single one of these And update each one.
**Carlos Alberto Cortez (Dash0)** 24:10 Yeah, if you're comfortable exposing something like that in the SDK common package or something like that, and you're feeling comfortable that it can be called from exporters, I think it could be the best.
**Lukas Hering** 24:21 Yeah, we would… yeah, we would need to make it, public and stable.
But yeah, we yeah, we we should at least determine what we want to do here first.st So Okay, yeah, thanks for this, Tammy.
Okay… Oh.
And… looks like that's it.
Does anyone else have anything?
**Aaron Abbott (Google LLC)** 24:55 Nope.
**Lukas Hering** 24:56 Okay, yeah, I guess we can… Can just end early then, yeah.
Unless there's other other things we want to cover.
**Aaron Abbott (Google LLC)** 25:04 But… Yeah, sounds good. I guess we did the patch release. That's the only other kind of announcement thing I can think of.
**Lukas Hering** 25:16 Yep.
Yeah, looks like we… Yeah, we were able to… Close out.
A few of the bugs that popped up.
**Emídio Neto** 25:24 Yeah.
Okay.
**Lukas Hering** 25:29 Yeah, so…
**Aaron Abbott (Google LLC)** 25:33 Alright, thanks everyone.
**Lukas Hering** 25:35 Mitchell.
**Aaron Abbott (Google LLC)** 25:35 next week.
**Emídio Neto** 25:36 Okay.
Thank you, folks. Bye-bye.
**Carlos Alberto Cortez (Dash0)** 25:39 Thank.
**Leighton** 25:39 you.
