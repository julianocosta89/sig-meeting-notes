SIG: .NET Auto-Instr SIG
Date: 2026-05-27
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/OjEPPQixmcRdlvWJ_6oPSsx8KL2Uv5Mg2FkGzAMbnVBe9mU8yJQAejL9KonhjuTm.SDxcDB8xisIKTepp
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 02:21 Hello.
**Piotr Kiełkowicz** 02:30 Hey, Matthews.
This has some holidays, rush is not available.
And… that… that should… is active on Slack.
I would wait 2 more minutes.
Hi, guys. Rash is not away on Slack, Chris is marked as, today as a last day of holiday, so I think we can start.
I will share my… share my screen… So, starting from the top, there is a lot of renovate PRs. We are… Trying to clean it up.
One by one, but it takes time.
A lot of them need, kind of, manual assistance, so… It takes even more time than expected.
I see some draft PR from… Erasmus. Matt, were you able to discuss this, or share more information about this?
**Mateusz Łach** 05:33 I'm not sure if not my… if I have, much information about that. I mean, I know that Rasmus is reworking the, like, the plugin… Interoplayer, this is, This is due to… Due to the fact that he wants to improve the support for OpAMP.
And, I think he… as he started working on that, he… he decided to do it consistently, so he's reworking, like, the interface between the auto instrumentation and plugins, so… I haven't had the chance to look into the PR yet, so… and I'm still in draft, so… I think the… We can wait with reviews until this is marked as ready to review.
**Piotr Kiełkowicz** 06:35 Okay, other important stuff, I… I've started working on .NET 11 support.
There were a lot of layers of potential issues, most of them are already handled.
The good part, or bad part, I found regression on the .NET SPNET Core.
One of the… metrics and spanse instrumentations, it is reported and PR is approved already. It should be fixed previous 6, probably.
Other stuff, pinning tools, it is kind of all, grant work, nothing fancy.
CodeQL for C++, it also is waiting for us, and… I think we have… Matt here to discuss… this PR, I suppose.
**Matthew Hensley / Grafana Labs** 07:43 Yep, that's what I'm here today.
So, I can, get it up to date. I've been traveling the last couple of weeks. But in general, we've had some customers notice They have multiple, services in the same application pool, and because… resource?
Attributes were promoted to process-level environment variables. All of the services in one application pool.
Get the same resource attributes, and it's just whichever service gets it first.
Duh.
It's, obviously not the most… Recommended setup to… Run a bunch together, but it's very common, so… This just makes the app settings, keys for service name and the resource attributes, take precedence.
And it doesn't automatically copy them into NVARs anymore, so it just reworks.
Small part of the configuration system.
Do not necessarily rely on those, and then, app settings… Since they're local, take precedence.
**Piotr Kiełkowicz** 09:01 I think we have started discussing this last week, or similar issue.
Like, like this one, in general.
And the… we are pretty sure that we should We should consider it as a braking change, and wait with this kind of stuff for the 2.0 version.
But… for now… There is not so many issues required, major bump, so… There is no good timeline for this.
Am I correct, Zach?
**Zach Montoya** 09:41 For the deprecation, yes. Are you… are we also saying the, the fix as well for the, app pool?
**Piotr Kiełkowicz** 09:53 I'm not sure if it is kind of very different, to be honest, because you are doing… deprecating functionality.
**Igor Kiselev** 10:00 Only for subsidies.
**Piotr Kiełkowicz** 10:02 inverse.
**Igor Kiselev** 10:04 That would not deprecate functionality. I probably was a little bit, it was probably me that I said that it may require 2.0. Right now, I looked into it a little bit more. I don't believe it required 2.0 anymore, as it just scope environment… just scopes the settings to a proper… to a proper application. So, the… it's still a low configuration of, applications through WebConfig.
But it would not promote application configuration from one application to another application. Right now, that promotion feels for me, not as a feature, but more like a bug.
So, despite… it's definitely a backward compatibility change, but it is, Up to a bug level, we never said that we should have the same bug-to-back work on updated versions. So if we consider that promoting as a bug, it's probably not a breaking change.
**Piotr Kiełkowicz** 11:07 So, you are saying that we can configure it on up config level and still read it, or no?
**Igor Kiselev** 11:14 I think we should… we can configure it in that context level, and read it in… only in the prop application, so it would stop promoting to environment variable whose change does, it's probably key to commit it without 2.0.
**Piotr Kiełkowicz** 11:30 Okay, so Igor, can you review this PR and propose something?
**Igor Kiselev** 11:36 I will review, I will… Yeah, so my current belief is, with very high-level reviews that it is… should be a key without 2.0.
**Piotr Kiełkowicz** 11:45 Okay, so I'm assigning it to you if you have, kind of, grant base check for this. We can start with this… with this couple NVARs, but if needed, we can extend this PR, probably.
To the broader section.
Matt, is it working for you?
**Matthew Hensley / Grafana Labs** 12:04 Yeah, been able to run some builds of this in customer environments, and pH as expected.
**Piotr Kiełkowicz** 12:12 Cool.
**Matthew Hensley / Grafana Labs** 12:16 So, any feedback's welcome if we need to gate some of the functionality just to limit the behavioral change, like, if there's not app settings?
present, continue to promote variables, can rework it that way. But I definitely saw it more as a bug, since the docs don't… Cover that one, necessarily, so…
**Piotr Kiełkowicz** 12:36 Okay.
So…
**Igor Kiselev** 12:42 this week. I will review this week, and will share if I think anything else.
Required.
**Piotr Kiełkowicz** 12:50 All other PRs, I think, are marked as a draft, so nothing.
Nothing important to… to look into this, at least for now.
issues, deprecate web config, so this is the only without milestone. I will still keep open it, and we can discuss after the review, the discussed PR.
Hmm… I do not see any new discussions… And all issues are in correct place.
And the last part is to review the project boards.
Nothing.
More for now to drink.
Do you have any other topics to discuss?
Today?
So, see you next week. Thank you.
**Zach Montoya** 14:20 Thanks. See ya.
**Mateusz Łach** 14:22 Thank you.
