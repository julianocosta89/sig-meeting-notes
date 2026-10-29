SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-10-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz (Splunk Inc.)** 02:48 Hey, guys.
**eftiquar** 02:52 Hey, what's up?
**Piotr Kiełkowicz (Splunk Inc.)** 05:03 Hey Matthew, do you have any specific topics for today? Because… We do not have any kind of external contributors from other companies than Cisco than you.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 05:17 Okay, then. I have, opened up a draft PR For a different attempt at fixing the… service name, and apps that share an app domain. Or, sorry, app pool, an IS.
**Piotr Kiełkowicz (Splunk Inc.)** 05:32 Okay.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 05:33 So, it's, 5599, the CI failures cropped up, I will fix.
But Say, it's a lot… Simpler than the previous approach about, like, merging app settings.
that I'd done before, Yeah, just… whenever someone has some thoughts, we can talk about it now, or offline.
**Piotr Kiełkowicz (Splunk Inc.)** 05:59 To be honest, I did not have time to touch it earlier.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 06:03 No problem.
**Piotr Kiełkowicz (Splunk Inc.)** 06:05 But I think what would be the best, it would be… if you can share the link on the… our Slack channel, I hope it will trigger Oh, Zahi's here, maybe he has some thoughts already.
**Zach Montoya** 06:23 Hi, sorry. What's, what's going on?
**Piotr Kiełkowicz (Splunk Inc.)** 06:27 Matthew would like to discuss this, disappear, this kind of second attempt to… Avoid promoting problematic settings from under the IIS.
And did you have a chance to look into this PR, or not yet?
**Zach Montoya** 06:45 No, I haven't.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 06:49 No problem. We can do it offline. I can drop one in Slack. It's, Just the high-level version is it uses declarative config, And… Wires it up via the app settings, so it looks local.
To the application, letting applications in the same application pool on IIS have their own resource attributes.
There are limitations still, like bytecode Instrumentation applies across the whole pool, of course, so not everything works, but… Went through all the feedback on the previous attempt and the comments, and through some of the existing issues around config changes.
And tried to go for something, fairly narrow and understandable.
Bonus, it gets closer to declarative config being the default.
So it's… It is still a little strange, because it does rely on app settings, and, you know, it's like, what subset of config is respected there.
And so, went with the very narrow, it's like, no, you said you wanted YAML, that's where it lives.
Type thing. Kind of like the environment variables that trigger config loading do. So… Can leave a link in Slack, but it's… It's very little code, which is always nice, and it's… Pretty easy to reason about, but it's mostly, like, are the trade-offs okay, and… Just… need another set of eyes to think through them, of course.
**Piotr Kiełkowicz (Splunk Inc.)** 08:23 I… I cannot promise, but I will try to look into it this, or before the next six.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 08:30 Sure.
**Piotr Kiełkowicz (Splunk Inc.)** 08:36 So…
**Igor Kiselev** 08:36 So, I've done review of a previous version, I will try to repeat reviews this week also.
**Piotr Kiełkowicz (Splunk Inc.)** 08:43 Correct.
**Matthew Hensley (Raintank, Inc. – Grafana Labs)** 08:46 So, open to whatever feedback. It's mostly this has become a more common problem for my end users. I'm hearing this Heard earlier this year, and made an attempt, and found a decent enough workaround for them.
But I have some end users that… they have massive fleets of EMs and could not separate out their application pools. It's just… it's not feasible for them.
Right now.
**Piotr Kiełkowicz (Splunk Inc.)** 09:24 I have another topic, this time from Mateusz, Mateusz, can you share the details, or no?
About the OpAMP client issues.
**Mateusz** 09:36 Yes. Sorry.
Yeah, so basically, we were trying to use the… the… basically use this, in our plugins of the new, new plugin callbacks, that we released, but, we realized, we realized with Fiftheni that.
In country prepository, not all of the messages sent by OpenPlient include agent capabilities, and this is a problem for us.
So, I'll be creating the PRs in contract with the fixes, and then we would like to update OpenCl client version used in Auto Instrumentation, and probably make another release.
If that's okay with everyone.
**Piotr Kiełkowicz (Splunk Inc.)** 10:31 For now, I do not see any blockers. There is nothing strange, immersed.
Right now, into the main after the release, so… if you are a ZAK fan, it should be kind of easy to go.
**Mateusz** 10:52 Okay, thank you.
**Piotr Kiełkowicz (Splunk Inc.)** 10:56 And we can go through the… Puller request, it is the first on top, yes.
PR from Matt, we have already discussed briefly.
Crown trip… two automatic updates, but we cannot merge it in this way, and I do not see a good way to close it, so it stays with us for some time, until I'll find a way to… Closing it.
Runtime async… I'm in progress on, kind of, direct Or targeted, upstream Sync with Datadoc.
I think it will be the better option than… going through… going with this. Unfortunately, one comment from this PR is also applicable to the code I'm trying to Two kinds of graph.
I'm working on the potential fix that I hope we'll share today or tomorrow.
Which is, like, Looking for the opinion sense.
That's all.
And a couple others are pretty… Long not updated.
So, I do not think we need to spend time on this.
Oh, no, sorry, this one.NET 11 passed with .NET RC3, so no blockers so far.
no issues.
This one was detected by… codecs, and during the async Native support implementation, but… it affects broader code, not only the… async Native stuff. If I understand correctly, I understand correctly, and it does not support this kind of signatures.
of the methods, and I think… If you want to support it, we should go with the separate, PR. I do not check if it affects also the upstream.
Zach, do you know?
**Zach Montoya** 13:49 No, I'll have to check on that.
**Piotr Kiełkowicz (Splunk Inc.)** 13:53 Yeah, so if you check, please let me know what to do with this, what are your recommendations?
For sure, no blocker for the .NET 11 release or anything like this, so… It would be great to fix it if needed, but no rush.
Steve Gordon proposed to… You utilize new way to… Mmm… unlock.
everything in… Auto Instrumentation, and… Chris asked to prepare some proof of concepts.
and compare with current behavior, because SDK prepared Music Diagnostics mechanisms.
I will put it into VNEXT for now, but if Steve is fine to prepare something… Earlier, it will be great.
Zach, Alex, any recommendations what to do with this?
**Zach Montoya** 16:12 Yeah, I mean, this one's, like, a small… smaller issue, so, like, a good for grabs one, where we do a couple more checks to determine whether we've loaded the profiler or not.
**Piotr Kiełkowicz (Splunk Inc.)** 16:26 Okay, so it should be a relatively easy fix.
**Alexey Pukhov** 16:30 Yeah, it should be pretty straightforward. I'll… I'll take care of it.
**Piotr Kiełkowicz (Splunk Inc.)** 16:41 I cannot assign you, sorry.
Yeah, also… One of the issues found during the… Upstream thing? Zach, did you have a chance to look into it, and… Check on the recommendations.
**Zach Montoya** 17:22 No, let me… let me… let me check on that. So, I have a couple of things that I, have in my backlog right now.
**Piotr Kiełkowicz (Splunk Inc.)** 17:30 Sure.
I will keep it open as is, for now.
The next one from Upstream Sync, I do not think it is… very problematic, but we are ignoring cases, I think, in the managed code, but we are not ignoring cases in the native code, and the same problem is in the Datadog. I've checked it some time ago.
I will put it into the next release, because it is not so important, but it will be… Nice tool, fixed it.
Zach, I think you have discussed it kind of months ago.
Any recommendations? What to do?
**Zach Montoya** 18:38 No, nothing yet. Yeah, we discussed that this would be, perhaps a preferable way to do it, but I haven't… I haven't tested this yet.
So, we'll have to look into that.
**Piotr Kiełkowicz (Splunk Inc.)** 18:56 VNEXT, or we can… keep it open.
**Zach Montoya** 19:01 Let's do VNEXT.
**Piotr Kiełkowicz (Splunk Inc.)** 19:11 Mateus?
Can I close it?
**Mateusz** 19:18 Sorry. No, not yet. I think there is one more thing I'd like to add, which is support for custom capabilities, and then I will double-check if there is anything else left, and we'll close it after that.
**Piotr Kiełkowicz (Splunk Inc.)** 19:34 So, I'm putting into the next release, hopefully. Okay. Not specifically.
Move it forward.
**Mateusz** 19:42 Okay, thank you.
**Piotr Kiełkowicz (Splunk Inc.)** 19:46 And this one we have PR, but there is… I think it is stale.
Nope.
No progress there.
I put it into VNEX for now.
And I think we are pretty… Well, sweethe.
It's all.
Important stuff.
Discash… That's wrong.
Nothing here.
for all signs, I'm not sure if we need to update here anything.
Nope.
I'm not sure if you are aware about the new Anthropic, possibility. There is a possibility to scan open source projects, and we have did scans, for… SDK, most of the issues are already solved. The next… parts… From… Probably next week we'll go through the contrib trip.
repository.
when it will be cleaned, I'm considering also executing it against auto-instrumentation.
But it is kind of a longer project.
**Zach Montoya** 21:50 So right now it's, running on the… the core, .NET SDK, or Contrib?
**Piotr Kiełkowicz (Splunk Inc.)** 21:57 In general, you are creating a Docker image, and they… and they need to have possibility to build it, and they are executing Probably metal scanners or something like this.
I will share the link to you.
**Chris Ventura (New Relic, Inc.)** 22:31 Feel free to just, reach out to me on Slack if you need me to review something sooner.
That way we can get through some of those things faster.
**Piotr Kiełkowicz (Splunk Inc.)** 22:49 And…
**Zach Montoya** 22:50 What are the most high-priority ones at the moment, then?
**Piotr Kiełkowicz (Splunk Inc.)** 22:56 Do you mean PRs?
**Zach Montoya** 22:59 Yeah.
**Piotr Kiełkowicz (Splunk Inc.)** 23:00 The async native support, but it will be… it will occur tomorrow morning, probably.
I doubt that we'll have enough time to finish it today.
And the next one will be probably .NET 11.
**Zach Montoya** 23:21 Yeah, okay.
**Piotr Kiełkowicz (Splunk Inc.)** 23:23 and the issues without the V-next version.
And other topics?
Thank you. See you next week.
**Zach Montoya** 23:56 Thanks.
**eftiquar** 23:57 Thank you.
**Mateusz** 23:58 True.
