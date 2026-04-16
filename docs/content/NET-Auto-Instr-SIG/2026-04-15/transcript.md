SIG: .NET Auto-Instr SIG
Date: 2026-04-15
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 03:59 Oh my gosh.
**Mateusz Łach** 04:07 Hello? Hey, Pietro.
**Alexey Pukhov** 04:09 Bye!
**Piotr Kiełkowicz** 04:13 So, it's a Cisco team, a Cisco meeting again.
**Alexey Pukhov** 04:18 Yep.
Long time no seein'.
**Rajkumar Rangaraj** 08:13 Hello, Peter, thanks for the remainder. I could join.
I don't have anything big, to discuss here, I just want to understand if… even Here, where are we impacted with this?
like, security PRs that's been getting created.
**Piotr Kiełkowicz** 08:34 Yeah, we are impacted, because… I think it is safe to tell it, because PR is public and merged, and not yet released.
**Rajkumar Rangaraj** 08:45 Okay.
**Piotr Kiełkowicz** 08:46 Basically, any OpenTelemetry API package is vulnerable for edmund.
stable OpenTelemetry APA packet is vulnerable.
So, and the auto-instrumentation packet is vulnerable.
We have.
**Rajkumar Rangaraj** 09:06 Probably.
**Piotr Kiełkowicz** 09:07 notes… The vulnerability is 5.3.
We are looking… waiting for validation from the GitHub team to provide CV.
In addition, there is kind of a couple other issues detected. In total, I think we have 4 or 5 CV the GitHub Security Advisor is open in the… SDK repository for NA1 in Contrip, but it is not related to this project.
And… yeah, I think, all major findings will be fixed this week.
So, we probably need to make a release of… SDK and country.
early next week, and before end of next week, also, auto-instrumentation package accessible.
**Rajkumar Rangaraj** 10:09 Got it. Probably, I'll also recommend to, have a, like, I know a few things we cannot disclose in this meeting, public meeting also. I would also recommend, both a combined, or a separate, like, the maintenance connect on this, how we are going to tackle, because this is going to be the story going forward for the next 6 months with what we are… Seeing. Yep.
Yeah, so we need to have a plan, or, like.
security issues means we stop everything and we need to jump on it immediately and see how we can solve it. So I was just… I did not pay attention yesterday, and it looks like there are a lot of PRs created saying codecs scanned and everything in the SDK report. So, but which is good.
**Piotr Kiełkowicz** 10:56 Hello!
**Rajkumar Rangaraj** 10:57 Yeah.
**Piotr Kiełkowicz** 10:58 A lot of them are kind of… Informational findings, kind of tiny back reports, not the security.
**Rajkumar Rangaraj** 11:07 Yeah.
**Piotr Kiełkowicz** 11:07 In fact, in my opinion. Yeah. But part of them, kind of, are pretty important.
**Rajkumar Rangaraj** 11:12 Yeah, so we need to have a way to filter out and see which one to address and who is going to take, like, ownership of what and everything.
So, that's a process I think we need to bring, because like, yesterday in the SIG also, the SDK SIG also, you were discussing a similar pattern, like, I don't know whether you listened to the recording, like, how many patched version are we going to release? Like, yeah.
We cannot wait. We cannot patch and fix and wait. We need to release the immediate patch also.
**Piotr Kiełkowicz** 11:44 I agree, but if we know that we have, kind of, 5 more… Patches to be released.
kind of within one week. I think we should wait one week, because all of them are… More or less the same.
have the same CVSSs.
**Rajkumar Rangaraj** 12:01 Yeah, unless the CV is not disclosed, it's fine, I think.
**Piotr Kiełkowicz** 12:05 Yep.
**Rajkumar Rangaraj** 12:10 Yeah.
I just, like, looked at the number of things, like, I'll be stopping everything and looking at the SDK and the PRs in this repo, whichever is the security thing. I'll be prioritizing that.
**Piotr Kiełkowicz** 12:26 Yeah, especially if you can double-check GitHub Security Advisories, it will be great.
**Rajkumar Rangaraj** 12:31 Yep.
**Piotr Kiełkowicz** 12:33 Zach, you are not here. There is a plan to make SDK releases.
Because we have… CVSS, kind of 5.3 in the baggage propagator.
It touches basically any stable OpenTelemetry API release, ever released.
So… it impacts all… versions here, and based on this, we need to make a stable release, probably next week, of auto-instrumentation.
We need to take a risk and… And ship everything, what we have, within the beta state.
But so far, nobody complains, and it is the second day, so not so bad.
**Zach Montoya** 13:26 How come this, necessitates a GA?
Or a stable release?
**Piotr Kiełkowicz** 13:33 Can you repeat?
**Zach Montoya** 13:35 Oh, it's… you say that, Wait, hold on. Do we… have we already been doing stable releases, or just betas?
**Piotr Kiełkowicz** 13:45 We have had better.
And of course, on Monday, and so we need to make a…
**Zach Montoya** 13:50 Yeah, yeah, okay. Yeah, yeah.
**Piotr Kiełkowicz** 13:52 Whole release… whole state release next week, probably.
**Zach Montoya** 13:55 Okay. Yeah, let's do that.
Does this also affect… I mean, how many… how many lines for the OpenSommetry SDK are updated? Is it just… just one?
**Piotr Kiełkowicz** 14:15 I cannot give you access, unfortunately, on ATC, can give you access to the… security advisories.
I think I can paste… copy-paste something to… to… to… to the closed… Slack channel.
I will share the most important one, in my opinion.
**Chris Ventura** 15:03 So as part of this, do we need to go through… And… mark all previous releases as… Do not use.
**Piotr Kiełkowicz** 15:17 I think so.
**Chris Ventura** 15:24 Going forward, if we use immutable releases, is that something that we can still do?
**Piotr Kiełkowicz** 15:31 Nope.
We can just provide GitHub security advisory for this.
And to be honest, it is… Exactly the same behavior as we have for… For any other NuGet package.
There is no immediate removal from the nougat source, so you can take a risk and still use it, because, kind of.
**Chris Ventura** 16:04 Well, with… Yeah, with Nougat, you can mark specific packages as having a vulnerability, but I wasn't sure how that works with GitHub releases.
**Piotr Kiełkowicz** 16:16 I'm not sure if it is possible at all.
**Chris Ventura** 16:20 Right.
**Piotr Kiełkowicz** 16:21 For sure, we can modify, description.
and put their important notes, or something like this. It is… so, immutable releases means that you cannot modify an artifact attached to such release, but for sure, you can modify the description of it.
**Chris Ventura** 16:45 Okay, that'll be good enough.
Because then we can at least put a warning.
**Piotr Kiełkowicz** 17:07 But it is not so bad.NET also released yesterday, kind of, tons of CVSSs publicly, so… We are not only affected.
As you have joined, I think we can go also from the… our, let's say, regular staff.
It's the soul.
Basically, our CI is failing due to, kind of, some issues related to vulnerable packages. I'm trying to… to fix it.
I… it is almost done. I'm missing one… one more thing for… and service, but so I will try to fix it even today.
And… if we're speaking about requests… There is one ready to reveal.
Not related to boring stuff.
But there is some feedback from Igori and Alexis, so I think… Our contributor will know what to do.
**Igor Kiselev** 18:33 They've already done original… change, so it waits for Ross's second review after the changes.
**Piotr Kiełkowicz** 18:44 Okay, great.
So, I… Thank you, too.
That's all… I'm not gonna show this stuff.
Proflict faults… I think that this one is in progress, I will put it… to the next version, I doubt that we'll have enough time to merge it.
ATC in Pro… I think we cover this case.
**Igor Kiselev** 19:50 Yes, to the next version, we would resolve it up.
We will document everything that needs to be documented and close it after it.
**Piotr Kiełkowicz** 20:00 Great.
So, it is kind of committed.
3 weeks ago, go… I will close us.
Oh, the date.
I do not think that we need to do anything to you.
Do you guys, do you have any other topics to bring up today?
**Igor Kiselev** 21:27 Yes, I opened up, a bug story in .NET repository about assembly loading and redirection and so on. We'll see if it will give us anything or not, but at least, that was pulled from .NET teams that of what we are doing. So we know from day one that, what we are doing is not absolutely safe to, start up Hook Solution. They pointed us for one specific scenario where it will break.
And, assembly would escape all sandbox, and still would be loaded to the default domain. So… It's… Still, I still hope that, most of application would not be affected, and we fixed it for more applications, and we break it, but it means that, importance of, providing scripts, additional executables, all that we talked about, and additional measures to solve, startup books-only solutions.
Are more important than we thought originally, and… We should probably try to do it Soon.
So, not by .NET 11 release, but… as soon as possible, is that.
me, Alex, she probably will work on it.
That's all from me.
Wait.
**Chris Ventura** 23:31 So at this point, we're looking at… Most likely having a release next week.
And removing the beta… Marker from the current re… current release as part of this.
**Piotr Kiełkowicz** 23:45 Unfortunately, yes. To be honest, I would like to give it kind of two more weeks for this, but in current circumstances, yeah, I think we should take the risk.
**Chris Ventura** 23:56 I think that's gonna be a lot easier than having to.
**Piotr Kiełkowicz** 24:01 Project.
**Chris Ventura** 24:01 Portion? Yeah.
**Piotr Kiełkowicz** 24:02 Yup.
And… We could discuss this backporting if we kind of make changes in the .NET supportability set. I think we should, in this case, kind of make some… some changes, but… Without this, it should be fine.
**Igor Kiselev** 24:40 Do you think we also don't, if we release change to… to better support a startup hook-only solution, it would be an additional script, so additional executable that would work the same way on an older version. So, if customers have an issue with, and don't want to update, we could advise them Pick up that script and apply them on all older versions, so it also will work that way.
**Chris Ventura** 25:28 I don't have anything else.
Oh.
See y'all later.
**Piotr Kiełkowicz** 25:33 Bill?
**Zach Montoya** 25:35 Right.
