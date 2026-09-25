SIG: Swift SIG
Date: 2026-09-24
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Ben Joseph (Raintank, Inc. – Grafana Labs)** 00:56 I listened.
**Vishwan aranha** 01:02 Hey Ben, how are you doing?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:04 Good.
**Vishwan aranha** 01:05 I'm so distracted with sessions work, like, session replay.
Yeah, I'm looking at Yamaha's docs and saying…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:16 You started… I forgot it's tomorrow. Is it tomorrow?
**Vishwan aranha** 01:19 Yeah, it starts tomorrow, so this is.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:21 stupid.
**Vishwan aranha** 01:21 But it was starting on Monday, so I had to organize everything, so I'm, like, dropping a couple of things, wrapping up all the events.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:28 For some reason, I was thinking it's, like, a week out or something.
**Vishwan aranha** 01:32 in that.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:32 Completely missed the dates. So now I have to figure out, should I participate or skip?
**Vishwan aranha** 01:38 If you want to join our team, we can… I'm doing Android side, but you can help me out if you want. But yeah, it's… the video part is, like, me and Ama both are not good at, so…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 01:50 Haha, let's see.
**Vishwan aranha** 01:54 Excellent.
**Nacho Bonafonte** 05:11 Hello, good afternoon. Sorry for being late.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 05:17 Right, Nacho.
**Nacho Bonafonte** 05:21 Okay, yeah, Let me… Open the… document, I think Bryce is not joining today, he sent me a note.
So yeah, it's… Yeah, these are being… some crazy weeks, I think, for… Many of the people.
At the maintenance, at least, so, Yeah, I have to create a new document.
Let me share that. I just copied… oh… Oh, I think I… oh, I have not my… Okay… Sorry, I didn't have… I am sitting one moment because I cannot share my screen, if not… So, not…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 06:58 Hey, while we wait for Nacho, Billy, I had a question. I saw you were working on KS crash report integration.
Did you run into any issues, I, I saw the work was, like.
done a couple of months ago. Is there any plans to continue on it?
**Billy** 07:17 Yeah, I should be able to clean that up, I was gonna spend… sometime today, just saying the open PRs. I think I only have, like, 3 open PRs.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:32 Okay.
**Billy** 07:33 Yeah, the KS crash, the annoying thing is, I need to test it on a physical device.
I don't think it works very well on, like, the simulator, so that's why I haven't really been updating that VR.
A lot of… I'll message you guys today on, on the Slack,
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 07:58 Sure.
Okay.
**Billy** 08:00 Hair that stuff, yeah.
And, I also wanted to, get the, Sample test in, so that, we can actually, like, you know, centralize where all these, instrumentations go. I also, like, plan to, like, contribute, like.
I heard a bunch of other instrumentations for AWS, I was hoping to, contribute some of those, so, that's also why, like… I created the, Integ Test PR, like, 2 weeks ago.
**Nacho Bonafonte** 08:38 Yeah, okay. Yeah, sorry, I'm back. I had… I don't know if I said that I had to change my laptop because it broke the last one, and I had it approved still.
Zoom to, control the windows here, so… So, yeah, sorry, I was not here last week, because I was on… on a trip, so I couldn't make it.
So, let's review topics from last week, and if you… there is something I don't know, which probably could be, here, Please let me know. So, yeah, approver access for Ben, Joseph, and Vishwan.
Yeah, I have seen them. I have seen them both in core and… and in the main library.
Yeah, Yeah, the idea is, is, is, yeah, it's approving that. I don't know if for core, because I think the idea is releasing now.
2.6, yes.
You know, close it.
Or we don't plan to add more code there, if possible.
Because we want to come back to the… as we said. But yeah, I, I… yeah, we, we… We must take a look at that, but yeah, that, we, we… We talked about it, and yeah, the idea is approving.
So, that's for one theme.
Yeah, the release of, Hotel Swift, there is a PR for that.
I think it was created by, Bryce last week.
I don't know if he told me anything.
Specific, because… She has made some… It wrote something… Yeah. So then I, I think… no, nothing complete. I think we can, we can merge that, because it's needed for another PR, right? On the main repo.
Is that… Is that right?
The… So, the… the PR4 for the release?
I think it's approved already, already.
Let's see… Yeah, that's the only PR.
Yeah, these are the approvers and the release.
Yeah, I've approved it.
So I think we can merge it. Are you okay with releasing this as our last Coco Posubersion, anyone has any issue with it?
Okay, yeah, then I am gonna… What's on that?
Okay, and I think from the other topics… Yeah, the session PR, there are several PRs there, those are in the main library.
So, let's go now with those peers. First of all, See, nice.
Inc.
First of all… Yeah, let's… Check if there is nothing more, right, on this, on the core?
So this would be already the version, and we can update them on the main library.
Enough to eat.
There are… I know there are lots of PRs opens in… main repository. So we have some… some with the… sessions, right? Billy, could you take a look on those that… On those peers?
**Billy** 13:00 yes.
**Nacho Bonafonte** 13:04 the version, I think, are these ones?
**Billy** 13:07 Let me check. Let me check…
**Nacho Bonafonte** 13:11 Yeah, 1184… She wasn't done.
Yeah, this is… Laptop has a small screen, actually.
No, I'm ready, go by.
yeah, the persistence version. I have been checking it.
It looked good to me.
Anything on your site? Bryce, did you have time to take a look to it, or… Or not at all.
**Billy** 14:04 Bryce isn't here.
**Nacho Bonafonte** 14:07 Bryce is… is not… no, Bryce is not here today.
**Billy** 14:12 Yeah.
Maybe I just drop him a message, yeah.
**Nacho Bonafonte** 14:34 For the rest, you put these other two topics here.
Last boink.
Yes.
these ones…
**Billy** 14:47 Alright, sorry, those aren't from Lust League, is there… well, I guess they are from Lust League, There's two small PRs, Red Sanitizer Gate, I guess, and… Yeah.
After…
**Nacho Bonafonte** 15:03 I, yeah… I have taken a look, yeah, and it looks good to me.
Also, and there were also some…
**Billy** 15:13 Fair enough.
**Nacho Bonafonte** 15:14 Yeah, there were some comments, but… Nothing serious.
I feel that.
**Billy** 15:18 I'll clean up that thing by, that Arn suggested, and then, next thing was the, I… like I said, mentioned to Ben earlier today, added some, info for, doing intake tests, particularly for, Like, instrumentations, I… I think there's, like, a couple of things that I want to, change about this in another revision, but, Just wanted to get some folks' feedback on, just, like, the overall architecture.
**Nacho Bonafonte** 16:05 So you…
**Billy** 16:06 for example, like, I might just, for the intake test app, like, maybe I'll just get rid of all the, Live features, so that it's, like, self-contained, I mean, maybe that we don't need to, you know… Kind of a sophisticated app to do all this stuff.
**Vishwan aranha** 16:25 Would this… would this setup, like, support testing session persistence across, like, app restarts, or would that need, like, a separate harness?
**Billy** 16:35 I don't remember what I did for AWS, I don't know if you can, Do the, full persistence, setup.
But you can at least, You can at least, like, close the, You can at least expire sessions, and you'll be able to do, like, you can at least manually trigger the, the UI notifications, like, app is closing and whatever, Yeah, I'm trying to remember… I don't know if you can actually hide… the app and open it again. I can't remember, I need to look at that again. But I did create some, naive, intake tests for the sessions.
in this PR.
**Vishwan aranha** 17:28 Since, like, I meant, like, terminating and relaunching the app, then checking the persisted session state. Would the test runner support that, or…
**Billy** 17:37 I… I'm skeptical about that.
**Vishwan aranha** 17:43 Got it.
**Billy** 17:43 I can look again. Things might have changed in a year. I remember I couldn't think of a career way to do that last year.
I wrote this for AWS.
So the answer is, I don't know. We can try again.
**Vishwan aranha** 17:56 Yeah, we can check the full Apps Reach.case separately, if that works.
**Nacho Bonafonte** 18:06 Okay, yeah, this is about… Yeah, these are the integration tools you were saying, Billy?
Yeah, we're basically, this was handled also last week.
Yeah, it has… Thomas, more feedback?
**Billy** 18:40 Okay.
I would just, like, go through all of this.
But is there any, like, feedback people want to give now in this, in this meeting, or… Okay.
**Nacho Bonafonte** 18:55 Yeah, I, I… Yeah, if there is something… I mean, I would like to advance. I mean… with… as fast as possible, with many of these PRs.
Sometimes I… I mean, I think there are… maybe taking… too many iterations. It's not because It's, it's great reviewing and, and, And I've been many comments, but sometimes maybe If something is not buggy, but works, but could be better, maybe we can land.
And, you know, iterate faster on features, so something… maybe can be added later. There was also a PR out there that was above.
you know, something that is working, but it could be better, but yeah. But if it's already an app.
an improvement We should… and it's not buggy, we should land.
And yes.
**Billy** 19:52 Okay,
**Nacho Bonafonte** 19:52 maybe…
**Billy** 19:53 I'll go with another PR.
**Nacho Bonafonte** 19:55 I think that… that… And another thing that I think we should focus on, especially today.
Because we have to release something for Cocoa Pots, so version 2.6.0 of the library. I would like To take a look, with all of you, and… decide which of these PRs should be made ready, for the version, and try to make that before the… I mean, before the month ends.
For the cocoa pots release, because this is gonna be the last one.
Asset, and probably move.
Just after we release that, moving the… Core version, yeah.
Inside. And it will be… everything will be much faster, So, yeah, and we need to release the last cocoa pot, so… from… from PS… Is there any PR that you… Any of you would really like to have?
Into the 2.6 version, so we can focus on them.
**Billy** 21:17 Yeah, I'm taking a.
**Nacho Bonafonte** 21:18 Any of you… Any who is in the meeting can, and talk. Very true. So we can…
**Vishwan aranha** 21:25 When is the next release planned? I believe 2.
**Nacho Bonafonte** 21:30 it should… B before the end of the month, so maybe, or… Or just next.
probably, I would like to have it next week.
We are… have released the core today, 2.6.0, I think that will be released already, because I merged the PR. I will just check it later and maybe add some.
release notes?
But we should… we should land this, also. If there is some functionality that we are still… we can still put that into main after the release. There is no problem with that. We can release a 2.6.1, or whatever you want.
Or 2.7, or… probably better, because… to keep the functionality with… for CocoPulse in the 2.6 branch, if we need a bug fix, but we can… we can keep main with… with… Then you're 10 years.
**Vishwan aranha** 22:26 I'm working on a session task, so for that, maybe by next release, end of October is perfectly fine for me, so no rush on my PRs.
**Nacho Bonafonte** 22:35 So, I say, before it ends, I mean, this one will land this week.
Okay. Right? In the next week, there will be one release with 2.6.0, which is what's merged.
Or in the next week. And we will probably release another later… As soon as we want, but… this CocoPulse one should land.
As soon as possible.
So, if you have any PR that you really want, the, okay, Millie doesn't have any. If you need anything from this to be in this next release.
Raise your hand.
To prioritize it.
The reviews and the merging.
If not.
If there is no, no, or any of you, I… we can start already the release, as it is, if there is nothing you want to add, or nothing you want to fix.
Or any fix that you want in…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 23:38 Not from me, but I think, Yasura was asking for some items. I think he already brought this up, and then, like, you mentioned that it's… it can be in the pre-release, and then… I don't know if, if there aren't any…
**Nacho Bonafonte** 23:55 Yeah, there was one PR from Yazura that needed the new… 2.6.0 of the library, so, yeah, I… Maybe it was this one?
If I remember correctly.
Yeah, Yasuda had some open. This was approved.
By Bryce, but I think this is… Okay… Oh, there was another one?
Yeah, probably 8 months.
We must ping him.
About this… But this was… this needed… Yeah, this needed the… the… the 2.6.0, this is the… the brand's creation. So we will say theme… Yeah, that's something like that.
So, yeah, so we can try to… Because they have an address.
disappears as soon as possible, that… I think that he wanted them in, and so, yeah, that can… make it… So if you… any of you don't have any other, question or PR that you want to merge?
We… I will… Personally focused on having this release out.
as soon as possible, and yeah, I'm… I'm… Once that's done, I will continue.
That's when I was interviewing many of these peers. I have seen many Yeah, many reviews already in many of them. Some of them also vaccines have conflicts, so… Waiting for those, for, for, for those conflicts for reviewing.
But yeah, I think, yeah.
Thanks a lot for… for the… Time people is taking for reviewing.
for adding PRs and for reviewing other PR.
Because you're having… Approvals of people that say this is great, also helps him.
To the maintenance, to… to… to undo, you know.
A much deeper review, because you know that more people has already… Seen it.
So yeah, that's great.
So apart from that, I don't know if… There are any… new topics… Yeah, about Magic Exporter books, yeah, these are the, yeah, ZRA thing, so… I think those two can be handled.
with that message.
And this, iOS-specific Instrumentation, who wrote that?
**Billy** 28:23 That's true.
**Nacho Bonafonte** 28:23 videos.
Yeah, I think… Have I lost my connection?
**Billy** 28:29 Nope.
**Nacho Bonafonte** 28:35 I don't see you.
Hello? Anyone there?
**Vishwan aranha** 28:51 Yes, I can hear you.
**Nacho Bonafonte** 28:53 Okay, okay, thanks, Jack, I was… I wasn't just going to restart this.
**Vishwan aranha** 28:58 Everyone else is quiet.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 29:00 I'm here, sorry.
**Nacho Bonafonte** 29:02 Okay, thank you. Now, then I will, I will open it again. I was gonna need just to close it, because I thought it was me, but it was Bill who lost it.
So, the AIC specific instrumentation who added that topic?
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 29:18 Yeah, I brought this up with Bryce last week. I was wondering if this is okay to add.
I was, I was interested in adding some view instrumentations, maybe, navigation and, like, screen views.
I didn't really have a plan for it, but, like, I just wanted to make sure that it's okay to add it into the SWIFT project.
**Nacho Bonafonte** 29:42 Absolutely, absolutely. I mean, I think one of the… biggest holes that we have right now in the library is specific instrumentation for iOS things.
Compared to other platforms, specifically Android, I think they have lots of instrumentation there.
We… Yeah.
We, we have, much less instrumentation, and, and… Much of it is… is quite outdated, also.
So yeah, totally open to any instrumentation you want to add. It will be, well accepted, to be sure. And as I said.
Personally, myself, I don't mind if… we can land PRs with functionality not being perfect, especially if it's new functionality, right?
We are adding new features, new instrumentation, but it's not 100% ready. We released that, SIGN is beta.
No problem.
I mean, that's better than nothing. And if other people find it useful, even if it's a bug, maybe they can fix it, and… create a PR and fix that, and make that useful, but yeah, we must… At least my opinion is that we must try to make This project as useful as possible for everyone.
So even if we have, lower quality instrumentation… I don't… I'm not saying that's the case, right? I'm just…
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 31:13 And that, in order.
**Nacho Bonafonte** 31:14 to encourage people to do things. Even if it's not perfect, if it adds value, okay, let's put that in the documentation. What are the limitations? What are the You know, the improvements that it could get.
And maybe another person takes it and improves, or maybe in the future, or maybe it's useful assist.
For some use cases.
So, yeah. I think that… With some pias, maybe we have been taking so long because it was not perfect, But… Having something is better than having nothing, right?
Maybe having a version zero is… You know, maybe it's not production ready, but it opens many, many, many doors, and many, possibilities to many people, so… Yeah, from my point of view.
Totally open to anything, and land it as soon as possible, especially if it's new functionality.
If we are adding to existing, you know, more mature libraries, we must be much more careful.
But not for… Newer stuff that is… Juno.
just, libraries that you can optionally add or not to the… to the… to your project when… when running, with OpenTelemetry.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 32:37 Bye.
Thank you for that.
**Nacho Bonafonte** 32:45 Okay, if there are no more topics… And we found… I'll leave it here today. I think, yeah, I'm not gonna track the PRs to this meeting, or the issues, because I think we must release that 2.6.
Today, Please, if you have any… other PR that you want to follow up, or you want Yeah.
to… to continue, he just… I… I… My idea is just merging all needed here to produce these risks, sorry.
And, I'm continuing as, as… Once that's done, we can continue, just, with… as usual.
Yeah, talking about other features, but yeah, this Cocoa Pots thing is… It's a maintenance program, and we must try to have something Ready.
with… with enough time for users to say that something is wrong before… before the year ends. So, yeah, this, three months is the… the minimum we established… established in the… in the past. So, yeah, that's all.
So, no more topics to talk today?
I think we can… we can leave it here and leave.
Here's how Mark.
Time.
Okay.
**Vishwan aranha** 34:17 See you guys.
**Nacho Bonafonte** 34:19 Thank you. Thank you for coming.
**Ben Joseph (Raintank, Inc. – Grafana Labs)** 34:21 Thank you. Bye.
