SIG: Swift SIG
Date: 2026-08-06
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Yasura Dodo** 00:29 Huddle.
**Vishwan aranha** 00:31 Hey there, how are you doing?
**Yasura Dodo** 00:33 Very good. How are you?
**Vishwan aranha** 00:35 Pretty good.
Everybody joins the meeting a little late, like, a few minutes late, so…
**Yasura Dodo** 00:41 Okay, cool.
Usually, how many people are joining the call? It's the first time.
**Vishwan aranha** 00:48 Like, usually, like, at least one or two maintainers, and others.
**Yasura Dodo** 00:51 Okay.
**Vishwan aranha** 00:52 Like, I've seen, like, 3 or 4 people in a call once, and sometimes it was just… 5 or 6, so… there's not many. Okay.
**Yasura Dodo** 01:05 And, we are having the call weekly, right?
**Vishwan aranha** 01:08 Yes, weekly on a Thursday.
**Yasura Dodo** 01:11 Very nice.
**Vishwan aranha** 01:13 Is this your first time joining this call?
**Yasura Dodo** 01:15 Yes, it's awesome.
**Vishwan aranha** 01:26 Where are you dialing from?
**Yasura Dodo** 01:31 Me?
**Vishwan aranha** 01:31 Yeah.
**Yasura Dodo** 01:33 I'm based in Berlin, Germany, but originally from Japan.
**Vishwan aranha** 01:39 Oh, cool I guess, everybody, like, I think some of the maintainers are from Europe as well, so they might be in the same time zone.
**Yasura Dodo** 01:48 Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:51 Have you contributed to Autel before?
**Yasura Dodo** 01:57 Meet?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:57 Yeah, Yasura, sorry.
**Yasura Dodo** 01:59 Oh, yeah.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 02:00 colleagues, so, yeah.
**Yasura Dodo** 02:01 We will…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 02:03 together. Sorry, I forgot to introduce myself. My name is Ben.
me and Vishwan both work at Grafana. We work on the Auto side of things.
So yeah, that's just a bit introduction.
the U.
We also contribute to the Android side of things. Sorry, yeah, go on.
**Yasura Dodo** 02:23 Mmm.
**Vishwan aranha** 02:24 I'm Vishwan. I've been reviewing your… I reviewed your PRs recently, so, I'm not a maintainer, but it's, like, I'd like to go through all the PRs and learn more about the project as well. I don't have any merged PRs yet on this fifth project. I have, like, one with three approvals, that's why I joined asking them if they can merge it in.
**Yasura Dodo** 02:44 I see.
**Vishwan aranha** 02:45 So hopefully…
**Yasura Dodo** 02:46 I see.
**Vishwan aranha** 02:47 Hopefully more, tasks would be lined up, like, based on priority.
And we have been, like, very active in the Android world, so hopefully we can get something in for iOS as well.
**Yasura Dodo** 02:58 Let me see, I got it.
Yeah, as I say, like, my… yeah, maybe, like, I can also introduce myself. I'm Yasura Yasura. I'm from Japan, and I'm working in, a company in Belarin, and, we are… trying to improve our observability system from a mobile perspective, and now, checking, like, what we can do what we can, you know, like, improve our observability and try to persist our data. That's why I created some PRs and also opening our issues.
**Vishwan aranha** 03:40 That sounds good.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:41 Awesome.
Do you also have Android apps? And, like, are you using.
**Yasura Dodo** 03:46 Yes.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 03:47 together.
**Yasura Dodo** 03:48 Yes.
And, yeah, like, also we are looking for a solution in Android.
And my teammate is, working on it. Maybe, like, he will join the next call.
Little, job aside.
**Vishwan aranha** 04:06 Android SIG is more active, and yeah, a lot more people join. And also on Slack, they're responsive, but, Swift has, like.
Low traffic.
**Yasura Dodo** 04:18 Okay. Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:20 Yeah.
**Vishwan aranha** 04:21 I usually wait, like.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:22 cannot… Sorry, guard Rishid.
**Vishwan aranha** 04:24 I usually wait, like, 5 to 10 minutes, and see if anybody joins. Hopefully someone can join, who is a maintainer, so… Go ahead, Ben.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 04:34 No, I was gonna say, like, so there's a CNCF, Slack, channel that you can, join, so it's a Slack org, and, like, it has channels for, each of the CNCF projects, so, like.
Swift, Hotel, Android, and you'll find the maintainers there. For Android, they are active.
And, like, we have discussions there, for swept, I think, like, last… I think last week, they were talking about, like, coming back to, Slack, because, like, they kind of stopped using Slack, but, hopefully, you know, you can try your luck. But yeah, otherwise, like, if you're not able to, get something, you know, on the call, like, you can always, like, comment on the issues, tag maintainers, that's the best way to get their attention if this doesn't work. I mean, like, we are also learning, so just sharing what we found out so far.
**Vishwan aranha** 05:31 I tried commenting on my ticket, like, two to three times. Like, I also brought it up in the last two SIGs, no, so… In Android, within, like, few days, it gets merged in, so… so I would say, yeah, like, be a little patient, and you'll… hopefully something will be merged.
**Yasura Dodo** 05:51 Okay.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 05:53 Yeah, we have less, less people active on the team, and, like, everybody are busy with their… Day jobs as well, so, most of these are independent maintainers, and, Yeah, I think with Android, it's more like… people who are working at different companies, they have their OTL priority as well, so they invest a lot of time on the Android open source project, but… Unfortunately, that just didn't seem to be the case for, Swift.
**Vishwan aranha** 06:21 Yeah, and our ultimate goal is to become maintainers, because we also heavily use the hotel in our project, so… And if we do get that right, then things will move fast for Swift and Androids.
That's the ultimate goal.
**Yasura Dodo** 06:35 Cool.
**Vishwan aranha** 06:42 Usually, they do not join this late, but yeah, I might be wrong. I'll wait for a few more minutes.
Maybe because there was no agenda today on the… Doc?
That's probably why.
See, oh, there is… oh, there… where is this happening?
Because I see people… Today's the 6th. People are actively adding stuff.
Are we on the wrong Zoom call?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:17 Oh, are we on… I am on the new call, is that why?
**Yasura Dodo** 07:22 Oh, yeah, I don't know, like, the link is different between the, the documentation and also on this Slack channel.
**Vishwan aranha** 07:34 Let's try the… One in the dock. Maybe that's… That's a new one.
**Yasura Dodo** 07:41 I just… This is the one of the talk now.
**Vishwan aranha** 07:43 Oh, and…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:47 Are people still on the order?
**Vishwan aranha** 07:49 I'll join in the… I'll try both.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:52 Do you have the older link, Vishan?
**Vishwan aranha** 07:55 Is it on the… I'll check the older,
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 08:00 Calendar invite, maybe.
**Vishwan aranha** 08:02 Let me see, I have so many tabs open.
I'll share it here. I'll share it. It's alright.
**Yasura Dodo** 08:08 This is the… I sent it in a chat.
I think of that.
It's another one.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 08:13 Yeah.
**Vishwan aranha** 08:14 This is the… yeah, yeah, I can try.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 08:16 Let me… I will also jump over to the other one.
**Vishwan aranha** 08:19 See you guys there, yeah.
