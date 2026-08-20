SIG: .NET SDK SIG
Date: 2026-08-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Matthew Hensley** 00:47 Hello?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:01 Did I see correctly, it's your birthday today.
**Matthew Hensley** 01:04 It is, in fact.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:06 Happy birthday.
**Matthew Hensley** 01:08 Thank you.
Get some old man now.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:16 Welcome to the club.
**Matthew Hensley** 01:24 Yeah, I think last month or month before was, 20 years of full-time this.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:36 Yeah, I think… It's like in 2 weeks is, like, my 20th anniversary of being in IT.
**Matthew Hensley** 01:46 Yeah, well… Yeah.
Nope.
**Julius Koval** 01:55 Right?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:56 Oh, Julius?
Give it, one more minute, see if… I don't know.
Or how is she gonna join the cup?
And…
**Alan West** 02:31 Hey, y'all.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:55 Hey, Rosh.
**Rajkumar Rangaraj** 02:59 Hello, everyone.
Does anyone have a problem with joining this meeting? It took, like, a few minutes to… Join.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:13 Not that I've noticed.
**Rajkumar Rangaraj** 03:14 Okay, and it happens with auto-instrumentation also, so no idea.
**Alan West** 03:21 No, I haven't had a problem… I mean, there's a different flow now. I joined as a guest.
I don't know.
**Rajkumar Rangaraj** 03:27 Yeah.
**Alan West** 03:28 You see the difference.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:31 Oh, I've not noticed that myself. I just sort of click, and then there's a pop-up for, like, 2 seconds, and then it looks like any other Zoom.
**Rajkumar Rangaraj** 03:59 Let me try and present my screen.
Save it.
Martin, you have a topic.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:17 Yep, so I was just wondering if we thought we were maybe in position to do another minor release? Because there's a bunch of… there's a grab bag of stuff that's been merged recently, and so I created a milestone last week and went through and put everything that's been merged.
since the last release on it, and I've put a few items on there, because I figured these ones, if we were going to do a release, like, imminently.
it would be good to wait to make sure these ones are included, because they include, new API, or seem like something that… Better to have sooner rather than later.
**Rajkumar Rangaraj** 04:57 Sure. So does that mean, after this, we will merge the .NET 11 changes, and it will get the repo ready for the next release?
Floor 19.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:07 I… I guess we probably wouldn't merge until it at least gets to RC1.
**Rajkumar Rangaraj** 05:17 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:17 In a couple of weeks.
**Rajkumar Rangaraj** 05:19 Yeah, I think this time it's there. I don't know, I'm getting confused with this version on the… normally in November, I… I heard it's… they are going to predate it, I don't know whether… I'm confusing with 10 and this one, the conversation.
So…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:34 We had, I think, Preview 7 shipped last week.
**Rajkumar Rangaraj** 05:37 Yeah, yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:39 Yeah, so I think we'll get RC1 on the 8th of September.
**Rajkumar Rangaraj** 05:49 Cool, I think we are good here, then.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:55 Okay, cool. Whenever, these, and if there's anything else anyone thinks should be on the milestone are all merged, then I'll look at, sorting out in the next release.
**Rajkumar Rangaraj** 06:06 Sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:14 That was all from me on that topic.
**Rajkumar Rangaraj** 06:17 Let's take a look at the dashboard for both the contrabandy.
some cursor issue.
Lost my Kaiser.
So, I did not look at the, the metrics PRs, which are in the top. The only reason is, SIG was acting as a get, like, once he provides a… if he shows the green flag, that's when I thought we could jump on it, as he's driving that part.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:03 Yeah, I think with that one, it seemed okay to me, but as CJ had specific feedback on that one, I've just been waiting for him to come back to it.
**Rajkumar Rangaraj** 07:11 Yeah.
I think the next PR, it's pending review, I think.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:20 Yeah, yeah, that… I've rebased that one. That was… that PR and another one that was merged today. Yeah. So, like, parts one and two of the same issue that Piotta opened last week, so… Yeah.
That's just waiting on review.
**Rajkumar Rangaraj** 07:35 Yeah, I don't know whether we need to have this happen. I would say better we create an issue and close this off if… As a PR, just… Parking the pier for these many days may not be good, I believe.
Maybe we need to speak with Pietro and see if we can create an issue. If we are not handling it. At least someone else ORAS bandwidth could go and take a stab on it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:01 Maybe, maybe we could move it to draft until he's back from vacation.
**Rajkumar Rangaraj** 08:06 I think he needs back.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:08 I think he's on a vacation again now, until September.
**Rajkumar Rangaraj** 08:11 Oh, okay, then, yeah, then we will move it to draft and keep it that way.
Yeah, this is another good addition for the repo if this happens.
It would reduce a lot of memory allocations for the metric point, but I think, some minor work is needed, I think. He's also on vacation.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:37 Oh, yes, I remember this one.
**Rajkumar Rangaraj** 08:39 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:41 Oh yeah, he's left a comment, said he'll come back to it.
**Rajkumar Rangaraj** 08:43 Yeah, yeah. Remaining, I think, this also, I don't know whether it's, something on this one also, I believe, I don't recall it. Yeah, remaining, I think, we can, just review and move it. It's like… it's like very few days and all that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:05 Yeah, I think I was just waiting for Steve to do it. I think… I don't think he's addressed all the feedback I've given on the self-diagnostics one, but, it all seems to be going in the right direction to me.
**Rajkumar Rangaraj** 09:17 Yep.
Let's see, like, if the work gets complete, we can include this as well in the release.
It helps.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:26 I think this dashboard is slightly out of date as well.
**Rajkumar Rangaraj** 09:30 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:31 Might be because of the GitHub issue yesterday.
Because the second-to-last one has been merged.
**Rajkumar Rangaraj** 09:40 Yes.
I remember providing, yeah.
Let's move on to the country report, the country… Here's the dashboard for that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:58 Yeah, so the top one, Alan, I replied to the feedback you left on that. I was just waiting that you were happy with it.
**Alan West** 10:07 Oh, okay, sorry about that. Yeah, I'll take a look.
**Rajkumar Rangaraj** 10:20 I think apart from that, most of them are, the… from the maintainers are all new. I'll probably… I'll take a stab at it, Martin, today, to see if I can unblock all of your peers.
Here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:32 Sure, I think out of all of them, the… the Elasticsearch one's probably the biggest, but it's not that big.
The OneCollector 1, I'll just flag that, because whenever I ask Claude or Copilot to see if there's any security issues, it keeps flagging up stuff about Jason not being escaped properly, which is in the OneCollector 1. So, I know you said you were trying to minimize the changes, but…
**Rajkumar Rangaraj** 10:59 Unless there is a customer ask, we don't want to add any feature or tweak anything to this collector, so… either one collector or the Genoa exporter. The reason is, recently, the newer updates As we discussed last week, got several SEB tools within the Microsoft.
So, we want to very be… the retro was done, and we wanted to be very cautious taking updates on this one.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:23 Yeah, sure, I just thought I'd flag it in case you want to check it anyway, because, the agents keep complaining about the issues they're finding, which is what that's trying to address.
**Rajkumar Rangaraj** 11:36 Sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:39 I think all of the other ones from me are… Should be relatively trivial.
the two from Peter. I think one of them… One of them, I think, is the… yeah, I tagged you on that one, Raj, the one about the query string parameters, because that's the thing where…
**Rajkumar Rangaraj** 11:58 I missed that. Yeah, I was too much into the SDK and did not come to the contrib yet. So either today or tomorrow, I'll go and get, like, start reviewing the contributions.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:13 Yeah, and then, I think the other one is some docs, I haven't looked at it yet, and also… There's an issue about implementing a SQL batch size… And Peter has created an issue in the SQL client repo to get them to extend Okay. The instrumentation there to add it, which he said he was… which they've approved, and he said he would implement, so when… at some point, I think he'll come back and do a PR onto Contrips, so that, we can consume that. But that's pending upstream stuff at the moment.
**Rajkumar Rangaraj** 12:49 Okay.
Cool, I think then we pretty much, we have, things under control, here.
I think, Julius is here, I think we had a long pending pair of this. We got that merged as well. So probably that should unblock the box bridge or the things related to that part, I believe.
**Julius Koval** 13:12 Yes. Hi, hi. I wanted to add, attributes and schema URL to, logger, because that's part of the spec.
Yeah. And I noticed, whether the version wasn't serialized, so I did that.
And then, once that's merged, I want to add the attributes and schema URL, like I mentioned.
And there's also the issue… There's this bug that, I reported, I don't know if you read it.
It was related to the issue that you pointed out, about… How all, logs… From loggers with the same name but different versions are reported under the same scope.
**Rajkumar Rangaraj** 14:01 Yeah.
**Julius Koval** 14:02 Yeah, and so that affects all signals, so I… I guess I could fix that if we… because the approach should be similar.
Yeah, I guess that's… Everything.
Right, there's also that one issue from the PR from the key value list that you pointed out.
I don't know if you remember.
It was… I think if there was, tag with a value, which was supposed to… which was supposed to be stringified.
But then the toString method throws an error, then that would not be handled correctly, I think.
**Rajkumar Rangaraj** 14:45 Yep.
**Julius Koval** 14:45 Yeah, so I guess I could create an issue for that as well.
**Rajkumar Rangaraj** 14:50 Thanks, Julius, like, start creating, I know that I left that note, if you want to create an issue and follow up.
and different PR, I'm good as well on that. The current PR which you have is currently good. I don't know whether you made any update after that.
If so, I need to take a look at it.
**Julius Koval** 15:08 Yeah, there's a merge conflict currently, so I should address that.
**Rajkumar Rangaraj** 15:17 Cool, thank you.
Are there any other topics or anything else for discussion?
Yeah, I think if there are no other topics, we can end early. Thanks, everyone.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:35 Thanks, everyone. Bye.
**Julius Koval** 15:36 Thank you. Bye.
