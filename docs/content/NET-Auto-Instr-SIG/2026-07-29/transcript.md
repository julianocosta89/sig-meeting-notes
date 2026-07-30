SIG: .NET Auto-Instr SIG
Date: 2026-07-29
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**malach** 02:41 Hello?
**Zach Montoya** 08:08 Hello. Have I, missed anything?
**Igor Kiselev** 08:13 Bye.
You'll probably miss… Matthij.
very disconnected.
Let's do here.
**malach** 08:42 Hello.
**Zach Montoya** 08:44 Hi.
Alright.
Let's see… So it looks like we only have… One topic for today, Natuj, the Open Telemetry Resources host.
**malach** 09:05 Yeah, so I was wondering, because this… this is a dependency of our project, and that recently there was, advisory published for it, so I was wondering if we should prioritize, like.
updating it and releasing the advisory is… the scope is… of the… the scope of the issue is only macOS, so I was wondering… However you want to approach that.
**Zach Montoya** 09:33 Oh, that's interesting. Okay.
I… I mean, the first thing I want to do is just check what… if we sort of officially support macOS. I feel like the answer is yes.
**Igor Kiselev** 09:47 Yes, but at the same time, I would mention that previously, when we discussed if we should do a proper, a proper deprecation notice when we switched from macOS, x64 to ARM64. The answer was, yes, we support it, but we believe it is mostly used by dev and test teams, and we never planned to support it at the same level as Windows and Linux. I don't think it's ever documented, but I just remind the discussion that was before.
**Zach Montoya** 10:21 Yeah, yeah, our CI runs on… on macOS, ARM 64, yeah. I'm trying to see… Where do we actually declare the platforms that we support?
**Igor Kiselev** 10:57 Open Telemetry .NET automatic instrumentation should work with all official support operating system and version of .NET in the compatibility section.
And S.NET support macOS, And we see that we run AI test against Mocos.
**Zach Montoya** 11:21 I see, yeah… So, we say R64 is experimental, and… but we still run macOS on that.
Yeah, I guess it's not… it's not very explicit, but it seems like the policy is we officially support, like.
Linux, Windows, x64, and x86, and then any ARM64 distribution, including Mac, is just… Unsupported.
**Igor Kiselev** 12:00 How you figure it out that way?
**Zach Montoya** 12:04 That was me looking at this compatibility section of, like, the supported processors are SIG6, AMD64, ARM64, and then just extrapolating from there.
**Igor Kiselev** 12:14 Yeah, yeah, yep, yep, so it looks like, yep.
Formally, as Mark, we have only ARM64 right now.
As soon as we dropped Mark x64, we, moved Mark to experimental support only.
**Zach Montoya** 12:32 Yeah. F… I mean, if we don't have any issues requesting ARM64 support, then, I mean, I guess that's fine.
So, okay, oh, we have one question, or one issue for the operator, but… okay, that's different.
So, yeah, I guess… This doesn't necessarily impact a production scenario that we officially support, so, we could just take a safe approach and just do a release anyways, just so that there's no issues with, like, questioning, like.
The security of our packages.
But from an officially supported standpoint, yeah, we don't support, we have experimental support for… R64.
So I don't… I think would be guaranteed.
I'm fine with putting together a… A release patch to… to update that dependency.
**malach** 13:36 Yeah, so the thing is that, I think we, like, Aw.
We already merged the PR with the changes to plugin APIs, which is, like, a breaking change. I wonder if we should, like… keep it, should we revert it, or only bump packages to a release, or, like, any recommendations here? I mean, the PR that, so, the PR from Rasmus that we merged just after a previous release, so basically latest release.
do we want to, like, split the changes in a plugin API into two releases, or… Any, like, preferences here, recommendations here?
**Igor Kiselev** 14:25 My prefer… mostly, my preferences would be to wait until we will finish and say that it is, as much as non-production, do not… We never promised production support for macOS.
and issue, and vulnerability is only macro-specific, just wait a little bit, because it's not only macro-specific, it's macOS-specific with very edge condition. So, I would say that, allowing non, trusted application to put, SSHA in the pass.
into high-level path. It's already a pretty bad situation. Yes, we would be one reason of escalation in that cases, but as it is.
Thirst.
It's already a bad situation, and most probably some other application affected by that, already. And we are not, officially supported. I'd suggest to wait a little bit.
**Zach Montoya** 15:28 Yeah, I think that makes sense.
Yeah, we can… I mean, we can, put a PR together to update the dependency, but we don't need to ship it until after the… those other PRs are emerged, there's, we can just document that.
**Igor Kiselev** 15:45 At the same time, the issue already gives a pretty good description of what is an age condition. I would say that it is right now on a User to validate that that edge condition would not affect them.
Because edge condition already a mitigation, so do not allow that edge condition.
Zach, I actually have one more topic to discuss, hence it's great that you are here. So, we looked into, so we, in our internal product, looked into what, asynchron time, would add into .NET 11.
and brass, and, Right now, my belief is that, most probably we don't break anything… or .NET 11 with a synchron time, but, if customers have, configured instrumentation on a method that they define, and one of that method would be compiled with runtime async. A profiler will break that method.
As, right now, for example, task return method would return void, So on. I have not validated yet, if it really breaks, on, hotel or not, but my, I would bet that it will break.
So… The code is, from Datadog Profiler. So, right now, we have two options. First option would be, we could try to fix it ourselves in hotel, and it means that it would be even more diversified from Datadoc realization, or second option would be we could wait for Datadoc realization to fix it, and then try to, to, sync with Datadoc code. As a temporary workaround, would be to apply, some detections that it is a synchron-time method, and do not transform it at all, do not break customer application.
So, so that's why I'd like to hear your guidance as a maintainer of hotel, and at the same time have some insights in Datadoc.
**Zach Montoya** 18:17 Yeah, can you just… oh, sorry, can you reiterate, like, which, what exactly is unsupported at the moment? Is it… is it if you author… or if you want to instrument a method that has…
**Igor Kiselev** 18:32 Then.
**Zach Montoya** 18:32 Authored with, the new async model?
**Igor Kiselev** 18:36 Yes, yes. So if you enabled, if you try to instrument a methods that have been compiled by a compiler that, Async method, compiler with enabled async runtime.
**Zach Montoya** 18:49 I see, okay. And so that would require some, like, modification to the call target instrumentation to correctly handle, like, a target method that's been compiled.
**Igor Kiselev** 18:59 I'm thinking mostly to a profile, I think.
**Zach Montoya** 19:02 Yeah, yeah, and the profiler, yeah, okay.
So I… Don't think that has… been identified or prioritized on the Datadog side. There's a lot of other stuff going on over there.
So I… like, if you're actively investigating this, I think it could be… Good to… like, we could build it out here, and… the Open Telemetry.instrumentation repo, and then… I can bring that back to Datadog as needed, but I don't know that word in that moment, so if we want to try to get ahead on the issue, this is probably the best place to prototype it.
**Igor Kiselev** 19:48 Okay, so in that case, we will try to… we can try to fix that issue in Open Telemetry Repository. I'm not saying that it would be a highest priority, but before .NET 11 released, we should implement at least a blocker that would not instrument what is not supported.
And better to implement a full support of runtime sync, okay?
**Zach Montoya** 20:13 Yeah, that makes sense.
**Igor Kiselev** 20:17 Yes.
**malach** 20:17 So, I… I have one… one more, question. So… We have a lot of renovate PRs open at the moment. I think we need a maintainer, in order to merge it. Zach, do you expect you might have some time to take a look at some of the PRs and merge them? I think, like… at least several of them are already approved, but we just need… we just need someone with the maintainer role to actually merge them. Yeah, I…
**Zach Montoya** 20:50 Yeah, I can… I can look into this today.
**malach** 20:53 Okay, thank you.
**Zach Montoya** 21:08 Cool. Not sure if, you guys want to go through the rest of the, Sort of, pre-planned agenda stuff.
We're not…
**Igor Kiselev** 21:23 there is a new issue about startup oscillations and breaks, customer application. So, we are looking and trade what would be the best way to fix it, our best way to work around it.
At the same time, as we declared for .NET 11, we would need a script.
That would recreate pre-startup Hook behavior on the client, so we collect all assemblies in a folder. That will definitely fix the issue by returning a startup Estatos, es… a code branch that was used before we implemented startup isolation.
So… Now it's the best way I could do it. It would be before .NET 11's release, and probably we will be able to do it even faster.
I will rep… I will reply.
**Zach Montoya** 22:19 Okay, okay.
**Igor Kiselev** 22:20 About it, that we are… at least that we are working on it, and…
**Zach Montoya** 22:26 Okay, yeah.
Okay, looks like… yeah, there's… looks like there's a lot of detail, so hopefully there's enough there to… For us to reproduce on our side.
Cool. Yeah, is there anything else you guys wanted to discuss while we're here?
**malach** 23:05 No, nothing from my side. I think we can, like, skip the rest of the… usual agenda. I mean, I think we discussed the most important topics, but…
**Zach Montoya** 23:19 Yeah. Okay.
Sounds good.
**malach** 23:23 Okay, thank you. Cool.
**Zach Montoya** 23:24 Well, thank you guys for your time.
See you.
**Rhynier** 23:27 Thank you guys, bye.
