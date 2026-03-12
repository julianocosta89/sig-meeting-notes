SIG: Prometheus WG
Date: 2025-08-13
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Arthur Silva Sens** 01:54 Hello.
**krajo Krajcsovits** 01:56 Hey, ma'am.
**CE Carrie Edwards** 02:20 Hello.
**Arthur Silva Sens** 02:22 Oof.
**krajo Krajcsovits** 02:26 I know.
**Arthur Silva Sens** 02:58 Looks like we don't have… Much to talk about today.
**krajo Krajcsovits** 03:08 Yeah, I don't have anything to talk about today, I've been supervised with it.
the Othiopian point in parameters, so related, but, like… I just didn't get to.
open 20 stuff. Although I did take a look at that PR that we mentioned, about the upgrade of Prometheus version.
And is it still true that we are postponing that, Arthur? You've been….
**Arthur Silva Sens** 03:32 Yeah, because Prometheus is using a version of a TLP translator that is uncompatible with other parts.
**krajo Krajcsovits** 03:41 No.
**Arthur Silva Sens** 03:42 We cannot upgrade yet.
**krajo Krajcsovits** 03:45 Yeah, the next release is on track, as far as I know. Ayub is working on it. I don't know when it's going to be out, but it's, like, on its way.
**Arthur Silva Sens** 03:55 Yep, sounds good.
**krajo Krajcsovits** 03:56 Okay.
**Arthur Silva Sens** 03:59 Yeah, I… also, I don't have much to talk about, it's just… I noticed that, issues, open issues, open requests are starting to accumulate.
And we are not trashy.
Are you viewing?
If people have the time to review stuff and respond to issues, that's all.
**Juraj Michalek** 04:20 Yeah, sorry, I'll try to find some time this weekend just been dealing with some personal things that are not fun.
Mmm.
**Arthur Silva Sens** 04:27 No need to be sorry, I… Yeah, collective.
I… I don't mean that this is your obligation.
**Juraj Michalek** 04:36 I know, I know.
**Arthur Silva Sens** 04:37 At the time.
**Juraj Michalek** 04:37 It's just I do feel bad for, like, not being as active as I was before.
Still need to finish my stuff, too.
Yeah, there's, like, if you look at the doc, there's Prometheus-related issues in Opal Contriblink. You can look… use that to find, like… Prometheus-related, issues that need the edge. They usually also have that label.
**krajo Krajcsovits** 05:01 Yeah, I feel the same as you, Ryan.
And also, I basically have tomorrow.
to do something, and then I'm off for 2 weeks.
And I'm also on call, so that's not happening either.
**Arthur Silva Sens** 05:17 Yeah.
**Juraj Michalek** 05:18 I hope you're not on call when you're off.
No, not when I'm off, but this week, so, ….
**krajo Krajcsovits** 05:25 part of land time was on-code, and anyway, I'm… Stop looking.
**Juraj Michalek** 05:31 Yeah, anyway, if we don't have any other topics, we can potentially do something, actually.
Unless there's some other topics?
**Arthur Silva Sens** 05:42 I know Owen has an open PR in the Hotel Go SDK.
This one is kind of urgent, actually.
we need to get this done ASAP, so if people have… I don't need, actually, expertise in Go or the SDK, just try things out, and if things make sense, just leave a comment and be out.
**Owen Williams (he/she)** 06:06 Although, if somebody… Let me actually link this thing. If somebody, … has… experience with scope metrics. I cannot figure out how to make them in the SDK. … Basically, the main sticking point right now, other than any notes that somebody might come up with, is the code coverage requirement. There's some error cases that are not covered with tests, and I cannot figure out how to make those lines happen. So if….
**Arthur Silva Sens** 06:38 I… I know how to do scope mat… scope attributes, I'll give you a comment in the PR. Great.
**Owen Williams (he/she)** 06:45 B.
**Arthur Silva Sens** 06:46 landed.
**Owen Williams (he/she)** 06:46 I have a….
**Arthur Silva Sens** 06:48 Code coverage is not a required CI.
**Owen Williams (he/she)** 06:52 Okay, well, … then if people are fine with the coverage as it is, then a stamp is good. Yeah, David Ashpepull was reviewing it, but he's out until September 8th.
He said I could ping him, so I did, but I would, you know, I think it's also better if we let people be on PTO.
**Juraj Michalek** 07:10 there was the person from OTL SDK, right, that was willing to review things.
Forgot his name, but he… there is some questions in the Auto Parameters channel. Maybe you can… maybe you could ping him instead?
**Arthur Silva Sens** 07:23 But who is the person?
**Juraj Michalek** 07:25 God.
Let me trick it down.
**David Ashpole** 07:31 Pete?
**Arthur Silva Sens** 07:34 Oh! Look who it is.
Bye.
We're talking about you, actually.
**David Ashpole** 07:43 I… I have probably about 20 minutes.
**Owen Williams (he/she)** 07:46 So….
**Arthur Silva Sens** 07:48 Yeah. I was just saying… Go ahead.
**Owen Williams (he/she)** 07:50 I was saying we could hopefully… we could… we were hoping to get somebody else to do the review so that you would not have to work on your PTO.
**David Ashpole** 07:58 Yeah, babies….
**Arthur Silva Sens** 07:58 Absolutely.
**David Ashpole** 07:59 I work when baby sleeps, so….
**Arthur Silva Sens** 08:03 So, like, if you're offline, who should we reach out on Go SDK stuff?
**David Ashpole** 08:12 I mean, the maintainers… I would reach out to Robert.
Tyler can also review, but he tends to be very busy, and then, … Damien also occasionally reviews That sort of thing.
Robert reviews a lot.
**Juraj Michalek** 08:35 Yeah, he was….
**David Ashpole** 08:36 That I have.
**Juraj Michalek** 08:37 moment.
**Owen Williams (he/she)** 08:38 Looks like Damien is on vacation right now, but yeah.
**David Ashpole** 08:40 Oh, yeah, yeah.
**Owen Williams (he/she)** 08:41 Okay, I can, I can ping them.
**David Ashpole** 08:43 Oh, Robert is the one that also helped us with this code….
**Arthur Silva Sens** 08:47 Yes. The change on this cycle about COVID rates, right?
Oops, nice.
**Owen Williams (he/she)** 08:57 Sweet.
**Juraj Michalek** 08:59 Arthur, I also saw your PR on the improved logging.
I got, I got pinked in one of the issues, … And when there was a person that had an issue where, like, they removed that exporter would just stop sending data after 15 minutes, they can no longer reproduce it in newer versions, which is good, but they… so I told them, like, you're already adding some extra log lines if they… I told them to look at your PR to add some feedback if they feel like there's a log line, you should be adding to.
And I'll try to review your worst case over the weekend, and the other one too, if it's still open by that point.
**Arthur Silva Sens** 09:33 Yeah, the PR is very simple, it's just literally just adding a logline.
**Juraj Michalek** 09:37 Okay.
And removing some.
But that's fine.
**Arthur Silva Sens** 09:43 Yeah.
**krajo Krajcsovits** 09:44 Also… I finished with the topic?
**Juraj Michalek** 09:50 Yeah, yeah. Okay, so, yeah, there's a… there's an issue that we came across during the Prometus Box Scrum.
**krajo Krajcsovits** 09:56 Actually, this Tuesday.
Where somebody's complaining that, Kubernetes container name that they get from the Prometheus receiver is not consistent, and it seems like it's an issue in Prometheus, so I… I plan to reply to that.
… I'm not sure how easily we can fix that, because… My gut feeling is that when you query Kubernetes, and the init container is running, it will just say that the container is init container, and it will not give you the Like, the container name that you… Expect, which is some application.
So I… I might… I would probably suggest a workaround to base it on a label instead.
For now, … But again, I have to find the time to….
**Juraj Michalek** 10:48 Do you want to drop a link for the issue in the doc or the Zoom chat?
**krajo Krajcsovits** 10:53 Yeah, yeah, let me try to find it, just a sec.
**Juraj Michalek** 10:55 I feel like that could be… if they use Kubernetes Resource Attributes Processor, that could be potentially also coming from that.
**David Ashpole** 11:03 I know there was one long-standing issue there, where basically.
**Juraj Michalek** 11:08 your pipeline could start processing things before the resource attributes processor had, like, the full dataset it needed in memory, and then, like, things would change, basically, because, like, it would first didn't add anything, and later it would add some extra layers.
In the next data point.
**Arthur Silva Sens** 11:35 Anything else to discuss today?
If not, then I guess we can end.
Early.
**Owen Williams (he/she)** 12:13 Sounds good.
**Arthur Silva Sens** 12:14 Right?
Yeah.
**David Ashpole** 12:18 Hi, everyone.
