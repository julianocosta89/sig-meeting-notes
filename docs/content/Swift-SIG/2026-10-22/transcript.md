SIG: Swift SIG
Date: 2026-10-22
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nacho Bonafonte** 00:42 Hello?
**Marius Ciocanel** 00:43 Hey, everyone.
**Nacho Bonafonte** 00:44 Good morning, radar tenongo.
Whatever.
**Marius Ciocanel** 00:51 Good day.
**Nacho Bonafonte** 00:58 Okay, yeah, someone already updated the document, right?
Thanks.
To whoever did it.
This copying the topics from last week.
Yay.
I don't know if we provide… we get per more of minutes for anyone who joins late. I always join late, these meetings, usually, because I come from another meeting on my company.
So, I am always thinking of someone who also… Enjoy late.
Bye.
Maybe we can start, if you want.
I don't know if there are many topics today. As always, if you have any new topic, please add it.
to the… To the… to the entries… And whatever you want to talk, yes, can be added there.
**Marius Ciocanel** 02:21 I have a question.
**Nacho Bonafonte** 02:23 Yes, sir.
**Marius Ciocanel** 02:24 Just because, I mean, I've recently, like.
started looking… looking at this project, and I'm just kind of trying to figure out what the… governance processes, and I see a bunch of people saying, oh, I can do this PR, I can do, you know, this PR, but they never do, and the contributing document doesn't really say how it works, but I saw you just commented on someone's… you know, there was a… there was an issue with, like, two people saying that they want to work on this, and I think you clarified saying.
you know, just send a PR. Don't worry about saying that you're gonna do it, just do it. Maybe that is worth clarifying in the… in the, I guess, the contributing.md file, just saying, you know, if an issue hasn't been resolved, please submit a PR without asking for permission.
Just… just to give people a bit of… You know, because, like, if people say, I want to do this, And they're waiting for… Someone to give them permission is not gonna…
**Nacho Bonafonte** 03:30 Yeah, I… we… I think that's… Yeah, usually, we don't assign tasks except Here in these meetings, when someone wants to take it.
that's the usual thing, and usually for those peers that are small.
And, for fixes that… you usually just appear. It's enough. Sometimes we have had two peers, and maybe one developer just disappears and never fixes the conflicts or whatever comes with that, so sometimes it's a bit frustrating if you wait just on one.
On one PR for that. I, I don't know. Yeah, could be clarifying that in the document, or maybe we could… assign… but assigning when…
**Marius Ciocanel** 04:18 No, assigning… I don't think assigning is the right thing. It's more… Kind of giving people permission So they can work on the PR without asking for permission, like, for someone to tell.
**Nacho Bonafonte** 04:30 Yeah, yeah, it could be.
Yeah, okay, yeah, I think so. I mean, we have been very open there. Probably we should document that, right? That's what you…
**Marius Ciocanel** 04:39 Yeah.
**Nacho Bonafonte** 04:39 Mentioned. Okay.
**Marius Ciocanel** 04:40 Yeah, I can… I mean, I can open a small issue and kind of update that, and you can… You guys can… Figure out a few.
**Nacho Bonafonte** 04:48 Yeah, that's right. Yes, okay.
**Marius Ciocanel** 04:51 Great.
**Nacho Bonafonte** 04:52 That's the win.
Okay, so, glad to see you, Bryce.
So, do you want to… drive it… Should I… As you prefer.
**Bryce Buchanan** 05:14 Would you mind? I'm trying to get this hot thing published, so,
**Nacho Bonafonte** 05:19 Sure.
**Bryce Buchanan** 05:20 I'll get an update on that before the, new topics get reached.
**Nacho Bonafonte** 05:25 Okay, yeah.
Okay, yeah, so, topics from last week. We have, one issue here… This is about… yeah, the proposal from, yeah.
from, Vladimir, yeah, do you want to…
**Vladimir Kukushkin (Apple)** 05:51 Hi, hi, I think I discussed it last time. Yeah, okay.
**Nacho Bonafonte** 05:56 Okay, yeah, just if you wanted to update something.
**Vladimir Kukushkin (Apple)** 05:59 Someone for community picks it up, it's fine, or we will have, eventually.
Okay. At some point in time to address it.
**Nacho Bonafonte** 06:07 Great, okay.
Okay, yeah, we have a local graphana view for instrumentation, demo, has it been already merged?
I think so, Billy?
**Billy Billy** 06:27 Yeah, he merged it in a few hours ago.
Yeah, thanks, and then, For me, I'm, also still working on the, hang-in, app launch instrumentations, should raise this soon. Didn't have a chance to finish it.
**Nacho Bonafonte** 06:45 Okay, yeah, great. Yeah, regarding that, yeah, this one added some, some review there, thanks for that, you addressed it, so I merch… I mean, it's… it's also not non-production code, so, if anyone has now any comments or improvements, they're just, probably, even on the closed PR, you can comment on, probably, will… Billy will… will address it also. But yeah, it's a great addition. Okay.
**Billy Billy** 07:17 Thanks.
Did anyone get a chance to try it out, by any chance?
**Nacho Bonafonte** 07:22 Sorry, what? I didn't get that, sorry.
**Billy Billy** 07:25 Did anyone get a chance to, try it out by any chance? The, the local view.
It just got merged, so maybe not. Okay.
**Marius Ciocanel** 07:36 I tried the PR after the meeting last week, but maybe, like, I need to figure out how to use Grafana better. It's like, I saw them, like, botting as they… as the app started, like, a bunch of, like, events in… I could see the events at the bottom.
Like, being triggered. But, like, the graph…
**Billy Billy** 07:57 The Ghant view didn't show?
**Marius Ciocanel** 08:00 It shows, but they were all, like… Like, a column of…
**Billy Billy** 08:06 Yeah, that's… yeah, it's kind of hacky. I don't think it's, like, natively supported. I just kind of hacked it together. I can take a look, another look to see how to improve it, and if anyone has any, you know, pre-built Grafana Gantt timeline view, that'd be great to share.
**Nacho Bonafonte** 08:29 Okay, the next topic, from last week is this distributed tracing issue.
Which, it has been closed.
because it was just solved, right, by the dependencies?
**Billy Billy** 08:47 Yeah, it's all good now.
**Nacho Bonafonte** 08:50 Okay, great.
So…
**Billy Billy** 08:52 And the issue is closed, yeah.
**Nacho Bonafonte** 09:09 Okay.
So, for new topics, we have here the Cocoa Pods Publish.
That was you, Bryce.
**Bryce Buchanan** 09:17 Yeah, so there… for the last publish, for 2.6.0, the Swift version in the pod spec file for the main repo, was incorrect, so it wasn't, it did not publish correctly, and, I'm not sure if I… I'm still trying to work this out, but I'm not sure if I have permissions anymore to publish myself.
To CocoaPods, so I might need somebody who has permissions To either add my email or, or publish it themselves.
But I can follow up in, our chat, maybe with, Ari, because I think he's the only one who has permissions on that.
**Nacho Bonafonte** 10:02 Yeah, I think so, yeah. Yeah, this was our last Cocopus available.
Version, so yeah, better if we can, really upload it.
**Bryce Buchanan** 10:11 Yeah.
**Nacho Bonafonte** 10:11 local books. Yeah, okay.
The priority that will be… that will have to happen in the… in the… in that branch, if we need to update something. So we should create a branch from that version, from that path.
**Bryce Buchanan** 10:27 Yeah, that's the other thing.
**Nacho Bonafonte** 10:28 permits.
**Bryce Buchanan** 10:28 Push a, push a separate branch and then run our, run our publish job on that branch. That was…
**Nacho Bonafonte** 10:35 Yeah, because we already moved, core to the main library, I don't know you. Yeah.
**Bryce Buchanan** 10:40 And the butt specs got removed.
**Nacho Bonafonte** 10:43 Yeah, and updated all the dependencies, and all the versions also.
Great.
Okay.
Then the, follow up, on the… Yeah, with, with, with Harry, who's the other maintainer, but he has been out for a long period now.
Let's see if we can address that.
Okay.
So, no more new topics, anyone? So let's review, let's review the… the PRs and, and the issues, so, starting with the issues… Yeah, the last one, is the… the one that, from, Vladimir, that he created, last week. Yeah, it was about the, exporter. The async is typically an export… transport exporter.
And… and that was already handled, and also the… these, new issues that you brought, Vladimir, thanks for doing that.
Because we… we have had several, several users trying to address them, or, so that… that was a really… Really good.
Idea, it moved the project a bit with new people adding Pierre, so thanks for that.
I think it was… it was really great to add those, issues.
So people could… could help. And also, thank you for… reviewing, them when they reach the PRs. So…
**Vladimir Kukushkin (Apple)** 12:30 Yeah, if I can ask, in case I miss any of the PRs you think my review is worth it, please add me to the reviewer's list so I get the notifications.
Thank you.
**Nacho Bonafonte** 12:46 Okay, great. Yeah.
So, for the peers.
We still have here the gRPC version 2, we are still holding on that. We have the, all those URL sessions, PR's, one of them, I think, Tomer… He, addressed the chains, I think.
This one has been.
Yeah, with conflicts, we have several with conflicts still. He addressed one of them.
But, yeah, it still has not… We will continue merging them.
As he continues updating and fixing the merge… merging issues, but he… at least he has given back.
Some, he updated one of them, and addressed the… address the conflict, so he is still helping here. Probably he's now taking more time, because one of them, yes, we're conflicting each other, so yes, yes, better late now.
So, we have also this about the trace… Con… Sorry, yeah, we have… Yeah, I have, sorry.
Report exception types instead of error codes.
This got some comments, that were, I think, addressed.
from, yeah, Vladimir, and aranha, and Vishwan, so Vishwan approved it. I just wanted to wait, for Vladimir, if he thinks his comments were all correctly addressed here. In order to merge, I don't know if you could review or not this one.
Again?
But if you are okay… I mean, he addressed what you said, but…
**Vladimir Kukushkin (Apple)** 14:44 I don't know. It's all good. It's all good. If I haven't pressed the button, I can press the button, yeah.
**Nacho Bonafonte** 14:49 No, I… yeah, I… Yes, yes, I mean, we had the meeting. I have seen it has been approved, yeah, earlier, from this one. I just was waiting for your feedback, if you added, or, but yeah, probably adding the feedback here, well, is enough, just for… That, yeah, great.
Didn't want just to ping for this.
So, yeah, the other… Yeah, we have, change, adding Billy as an approver, so I… I'm not sure if you did all… I mean, I approved this, I was waiting for, Yeah, more, maintenance approvals, so… I pinged them in a… in a channel, I… So, yeah, I… I'm just waiting for that, for… before merging, so it… you know, it really shows that you were approved by many of the maintainers. That's something I think it adds a bit of value to the approval, to be honest. So that's the reason I have still not merged that, because I want it to be approved by more maintainers before doing that.
just as a recognise to the… to the effort, Billy, so it's not, like.
Nothing more than that. But… One thing is that I don't know if you… this is, like, all you must do to be… an approver here, Billy?
I don't know if there is something more that must be added, apart from this, PR.
That's my only concern also, apart from, just adding you here, or does it need to be added to other… Group.
Bryce?
I think also, Yeah, Ben and Vishwan were also added as approvers. I don't know if this was the only…
**Vishwan aranha** 16:45 Yeah. Bye.
**Nacho Bonafonte** 16:45 is to change.
**Vishwan aranha** 16:46 I think we just added one PR, and we got access, so I think they should be, but that's my…
**Ben Joseph** 16:51 I think Bryce added us to a group also.
**Bryce Buchanan** 16:55 Yeah, there's a group, in the OpenTelemetry, like, organization that they need to get added to as well, but I can… I can take…
**Vishwan aranha** 17:05 Do you…
**Nacho Bonafonte** 17:06 Okay, okay, yeah.
**Vishwan aranha** 17:07 Do you have to manually add that, or does it auto-add after merging?
**Bryce Buchanan** 17:11 It appears it needs to be done manually.
**Vishwan aranha** 17:13 Okay.
**Ben Joseph** 17:16 And I think you need to first join the OpenTelemetry community as well.
**Nacho Bonafonte** 17:22 Yeah, yeah, Billy was. He was a tree a year before.
**Ben Joseph** 17:26 Oh, yeah.
**Nacho Bonafonte** 17:27 In the, in the project already, so yeah, he, he was there. Just, yeah, we… Yeah, we… Decided to move to, to, to an approver also.
Because, yeah, of all the previous work.
So that, that thing, I guess, waiting for, that, so that, that will happen.
This week, for sure.
Just to… to explain the delay. And yeah, we have also this one about owner… Include this context in auto lock handler.
It resolves one of the issues there.
It has been approved by Ben, but I think that it's missing the approval… the… the ECLA here.
So I think that's the thing missing here. So he must sign that. I don't know if we should ping him.
About the… About the class?
**Vishwan aranha** 18:34 I wonder if we can comment on the PR thing, you should sign the easy clip.
**Ben Joseph** 18:41 Yeah, I can add a question.
**Nacho Bonafonte** 18:42 Yep.
Okay, great. Yeah, but yeah, he must register for that.
So, yeah. And once he is registered, he then can run, basically.
command.
For that to, to, to be signed.
Yeah, that's… yeah, that's something that we need always.
Probably… I don't know if he just didn't notice it, or… I don't know.
Yeah, if you can ping him, it will be great.
And the last one is, yeah, this one, fixed metrics with same level, but different dimensions being merged. I think the problem is here… Was that… yeah.
I think was that he… Vladimir added some, comments here.
And he applied it directly?
So it's… ECLA is… now needs, Vladimir,
**Vladimir Kukushkin (Apple)** 19:44 Oh, neither does it.
**Nacho Bonafonte** 19:47 So I think that's the reason it's being blocked, because, I think that that's… you added some comments, and probably he approved… I mean, he merged them directly.
I think that's the thing. If… if you don't want to sing that.
I don't know. We, we can try to override that, the PR, or ask him to overwrite that.
We thought, yeah, he probably had your…
**Vladimir Kukushkin (Apple)** 20:13 I'll double-check with our legal people.
That should be fine.
**Nacho Bonafonte** 20:18 Yeah, okay.
Yeah, and also there is a requested change that I don't know. Yeah, this was… but I don't think it… it… As you are not an approver, I don't think that blocks the PR.
but yeah, I think the thing… what is blocking is the… is the ECLA.
The, the, the cloud authorization, yeah.
So yeah, that… that's it. And also, I mean, you have the recorded change. We wouldn't mess without that, but I was just trying to… Surface the… that other, thing.
And I think with this one, I think we have all the peers, for… Well, that…
**Vishwan aranha** 21:04 GitHub is flaky today, it's…
**Nacho Bonafonte** 21:06 Oh, nice, great, yeah.
**Ben Joseph** 21:10 Yeah, there's an insulin going on.
**Nacho Bonafonte** 21:13 Okay, yeah.
So yeah, that's all for this week, on the project side.
If you have any other question, topic that you want to handle, and if not, let's… Yeah, recover some time for other… More productive tasks, maybe?
Thanks.
**Marius Ciocanel** 21:38 I wanted to…
**Nacho Bonafonte** 21:38 Oh.
**Marius Ciocanel** 21:39 I wanted to ask something about, I was looking at CodeRabbit as… because they have free, like, code review functionality for open source projects, and that this definitely Meets that criteria, and I've been playing around with it.
I could show it a little bit, just to see, you know, the kind of stuff that, it adds, because I know that a lot of us use AI to review, but basically you don't have to give it any kind of permissions, it's just read-only, and just reads and gives you feedback on the PRs themselves, kind of like as a first step before anyone kind of Go… goes into the depths of… Of the PR. I don't know if it's,
**Billy Billy** 22:30 How does that pricing work for that?
**Marius Ciocanel** 22:32 I think, well, for open source, it's free. You get 10 free pull request reviews per hour, which is more than enough for, For this project.
And I played around with it on my local like, branch.
My local fork, of OpenTelemetry Swift, and it kind of shows you, like, security blast radius if something changes, Just a bit more signal to… to the PRs.
**Billy Billy** 23:11 Yeah, I'm super down. I definitely would have done this before I quit AWS, because they give you, like, unlimited tokens, but, yeah, if this is free, then I definitely would have done it. Yeah, just go for it, I think.
**Nacho Bonafonte** 23:26 Yeah, we usually use, It… with, with GitHub, there is, what's the name of this?
**Ben Joseph** 23:36 mileage.
**Marius Ciocanel** 23:37 Copilot, co-pilot.
**Ben Joseph** 23:38 Yeah.
**Nacho Bonafonte** 23:39 The quality of the review is not extremely good, I don't know, code dropping, yeah. But, you know, it's something, right? It… at least gives you some sign-as, quickly, so yeah, it can be.
It can be interesting. The only concern I have is… If it touched too much noise.
But yeah, probably it can point some…
**Marius Ciocanel** 24:02 I can…
**Nacho Bonafonte** 24:03 or…
**Marius Ciocanel** 24:05 I can create an issue, so, like, we can keep the discussion, like, I guess, for next week, or…
**Nacho Bonafonte** 24:11 Okay.
**Marius Ciocanel** 24:12 in comment, in, like, in the GitHub issues. I can point to some of the bits. I actually tried it on two PRs that were… I guess we were looking at… And, yeah, it gives you a bunch of stuff.
But I think it can be configured to how strict and, you know, how much information it actually shows you.
It has some nice, nice visualizations as well, with… Kind of, like, flows and what changes, and it even alerted that one of them, I guess one of the PRs was touching, like, the boundary, like, the library-public interface, which obviously is important, information to know, because you can't really tell that based on just the code changes, like, based on a diff, it's hard to figure that out, but it kind of surfaces a bit more information without necessarily having to open Xcode or… You know, and kind of tracing, like, looking at the code, so… I'll, I'll put something, like, a small written piece, like, in an issue, and we can discuss it if… Okay.
Just so people can look at it in their own time.
With, with arguments.
why, you know, if it's useful. I've seen other projects use it as well, because I think that's kind of how I saw it. Like, I was looking at other open source projects, and I saw people actually using it, and I looked into there, I guess, you know, how much free… Usage can we get, and… Yeah.
**Nacho Bonafonte** 25:54 Okay, sounds, sounds good. You can, you can, you, yeah, start a topic with that, yeah, and let's see, because maybe, yeah.
Having good quality on Swift is not easy.
for LLMs, because they don't have, like, a stable language to focus on. So, yeah, sometimes the quality is social.
So yeah, let's… let's see that.
Yep.
**Marius Ciocanel** 26:22 Okay.
**Nacho Bonafonte** 26:26 Any other topic?
**Vishwan aranha** 26:30 Are any of you guys based in Europe?
**Marius Ciocanel** 26:34 Yes.
Awesome.
**Vishwan aranha** 26:37 Oh, next week, there will be Daylight Savings Time for Europe, but not for North America, which will be November 1st, so there will be some… Mess up in the.
**Nacho Bonafonte** 26:46 Meetings.
True, yeah, it uses the American time.
Because I always get late or too early when that happens, because I am in Spain. So, yeah, I, I, I, I will try to remember that. It will be…
**Marius Ciocanel** 27:05 An hour earlier for us.
**Nacho Bonafonte** 27:07 an hour late… no, it will… for you, in the States, it will be the same hour.
So don't, don't, don't… yeah, it's only for Non-American people.
**Vishwan aranha** 27:19 We have some coworkers based in Europe, so all our meetings are, like, conflicting with each other, so yeah. That's why I wanted to conflict.
**Nacho Bonafonte** 27:27 Yeah, we usually miss some people, so… when we sync again.
**Marius Ciocanel** 27:32 I think the best thing to do is just use the notification in the Slack channel, just based off of that. When it says 15 minutes to the meeting, just use that.
Whatever time zone that's configured for.
**Nacho Bonafonte** 27:44 True.
**Marius Ciocanel** 27:47 I don't know.
**Nacho Bonafonte** 27:48 Great.
Have a nice weekend, and sleep one hour more if you can this weekend.
**Vishwan aranha** 27:54 See you guys.
**Marius Ciocanel** 27:56 Take care.
**Vladimir Kukushkin (Apple)** 27:57 Bye.
**Marius Ciocanel** 27:57 Bye-bye.
**Bryce Buchanan** 27:58 Hi, y'all.
**Marius Ciocanel** 27:59 Man.
