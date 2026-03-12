SIG: Client Instrumentation SIG
Date: 2025-08-19
Duration: 11 minutes
Zoom Recording URL: https://zoom.us/rec/share/zVK6M25RDAOWY4GRUQcLEHImIVgRvygmvmjBDVihVc2Ds5T7HZ7GMfS9-dr9lHyk.GVdBwkCxiiNo4uMG
============================================================

## Zoom Recording Transcript

**VP Valentin Pertuisot - Datadog** 01:36 Hello!
**Martin Kuba** 01:44 Hi, Valentin and Christian, I don't think I've met you before. Welcome.
**VP Valentin Pertuisot - Datadog** 01:51 I'm new to this group. I've been once, I think.
**Martin Kuba** 01:58 Yeah, so this, this group has, recently moved to being just twice, twice a month, every other week, and it's… the… the purpose is to discuss anything common, like, across browser and… At mobile, All the browser-specific discussions have moved to the browser seg.
Which is on Thursdays.
But yeah, if you have anything you want to talk about, please put it on the agenda.
**VP Valentin Pertuisot - Datadog** 02:31 Yep, I do.
**Martin Kuba** 03:11 Yeah, I'm gonna say… don't actually have anything… Myself, but… looks like you have something, Valentine.
**VP Valentin Pertuisot - Datadog** 03:21 Yeah, just… so basically, I'm joining this group, because, at Datadog, we are basically working on a RAM product for a long time.
And, we… So we know, for example, there is already RAM SDKs from OpenTelemetry for Swift, Android, for browser, etc. And there is an internal will from Datadoc to contribute to the specification of client-side instrumentation as a whole.
To contribute to the specification, what we already do, what we want to do in the future, to work with you, people, everyone.
To actually align on this, to make sure that Looking forward, what we do also go in your way, and what you do also go in our ways.
To make this specification Even more formalized and better for everyone looking forward.
So, this is just a quick presentation of why I'm joining, and… Probably we'll… you will hear a bit more about people from Datadog on these kind of groups, whether it's on the… on the client-side SIG, or is it directly in the browser SIGs? I see… I know, like, a few of my coworkers are going there.
So we'll… we'll work with everyone to… To make sure that we can contribute to the specification.
As you might understand, on our side, we already have an SDK, I would say, an implementation, so most of our will is to contribute to the specification, to make sure our SDKs are conforming to the specification.
And we know that there is already an existing specification that is currently, I would say, still being built out on the OpenTelemetry side.
And that's why we want to contribute.
**Martin Kuba** 05:23 Okay. Yeah, that sounds great.
Yeah, let me know if you… if you have any questions, specific questions, or you need any help. I think… One thing we're trying to do is, have more, also more conversations in Slack, so there's a… through there….
**VP Valentin Pertuisot - Datadog** 05:38 I mean, I'm in the Slack channel already. Cool.
**Martin Kuba** 05:41 Okay.
… Yeah.
I think there's… there's probably a lot going on in the browser stick right now, as we're trying to, like, you know, make Make progress there.
… I don't know how much there's gonna be to… how many topics are gonna be here, happening here? … Usually, like, it's… usually, like, we have, more folks from the Android seg joining.
Yeah.
Today, they're not here.
But yeah, I… Yeah, let me know if you have any specific questions, so….
**VP Valentin Pertuisot - Datadog** 06:20 Yeah, so, I can reach out directly on Slack. I know I was… … It's, … Dan Gomez that told me that I could also, like, have a chat to… with Hanson Ho, I think?
**Martin Kuba** 06:35 Yeah. Like, involved in this group, too.
**VP Valentin Pertuisot - Datadog** 06:38 to… if I wanted, like, … that is available on Slack, too.
**Martin Kuba** 06:43 Yeah, yeah. Hanson is part of the Androids, I guess.
**VP Valentin Pertuisot - Datadog** 06:46 Yeah.
So, yeah, like, for example, I'm not sure if you know what the RSD case does, but… Basically, we are kind of capturing most of what is already captured by the open telemetry's implementation, but we also capture much… Many other signals.
**Martin Kuba** 07:07 Then we think it's a good idea to….
**VP Valentin Pertuisot - Datadog** 07:10 To be put in the spec, because first, it's likely that people using the OpenTelemetry SDKs would like to capture the same information directly, so if All implementation, basically capture it the same way, or at least… the goal is to report it the same way in the… through the specification, like, that's less work for everyone, I guess.
**Martin Kuba** 07:35 Yeah, absolutely. So, are you focused more on the mobile side, or the web?
**VP Valentin Pertuisot - Datadog** 07:40 I'm more focused on the mobile side, yes.
**Martin Kuba** 07:42 Okay.
Okay, yeah, … Yeah, I would… I guess I would encourage you to, like, to join the Androids, like, I think it actually happens.
on Tuesdays, before this meeting.
**VP Valentin Pertuisot - Datadog** 07:58 Okay.
**Martin Kuba** 07:59 Yeah. So some of the specification discussion also happened in the, I would say, the platform 6?
**VP Valentin Pertuisot - Datadog** 08:06 Oh….
**Martin Kuba** 08:07 But yeah, so I think if it's, like, specific to, you know, like, you would probably first… Discuss it with the group, like, with the, … That's with the focus group, and, like, come to an agreement, and… Then, like, once… Once you have, like, an issue or, like, a PR… You know, ready for review, then you could… you could go to the specifications second.
Or, like, the… yeah.
And get, like, a broader….
**VP Valentin Pertuisot - Datadog** 08:38 Okay.
Okay, thanks for the information.
**Martin Kuba** 08:44 That's true.
**VP Valentin Pertuisot - Datadog** 08:46 I… don't have much to add.
Is there any other topic for today?
**Martin Kuba** 08:53 I don't have anything else, … Does anyone else want to talk about anything?
Doesn't sound like it.
Right.
Okay, well, maybe we can just make a short meeting today.
Sure.
**VP Valentin Pertuisot - Datadog** 09:12 It's nice, nice, nice meeting you. Nice meeting you, too. Have a nice afternoon.
**Martin Kuba** 09:17 Bye.
**VP Valentin Pertuisot - Datadog** 09:18 Right.
