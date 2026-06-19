SIG: Swift SIG
Date: 2026-06-18
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**nacho** 02:40 Meaning?
**Billy Zhou** 02:41 In that show.
Ugh, I'm okay. Just, on PTO for a bit, and then… I mean, they're always sleeping ever since.
**nacho** 02:59 Help me… Update the document… Yeah, I think… For the rest of… In the rest of maintainers, Or try, or people in the team are… Not joining today.
So let me share… I will try to… We'll try 2… Oh, sorry.
Sit.
I will try to… Followed.
down there.
It was updating this… Yeah, Ben, I think you… this is your first time?
**Ben Joseph** 03:49 Yes.
**nacho** 03:50 In this Sikh meeting, So I don't know if you… have access to this document, you can add your name here, or I can add it if you want.
Yeah.
Do you want to present yourself or say something about, or just prefer to follow?
**Ben Joseph** 04:10 Little one.
**nacho** 04:11 We talk, as you prefer, I mean, no…
**Ben Joseph** 04:13 Yeah. Yeah, I just want to introduce myself. Yeah, I'm Ben Joseph. I recently joined Grafana And I'm working on some of the auto-related stuff, so that's why I'm here.
I will be, using the Autel SDKs on all platforms, so, like, Android iOS up.
hopefully other, React Native and Flutter also. So I'm here to, you know, learn about, direction, see if I can help with anything, see the evolution of, like, SDK itself, and, like, the direction that we are taking.
**nacho** 04:51 Okay Great.
Yeah, so here, there are, more maintainers, but they are not, Usually Bryce Buchanan, also Aries, DeMarco, and we're not… also help and usually join this meeting, along with Billy.
who have been collaborating also recently a lot in the project. We usually talk about the topics that we have, from one week to the other. People can add new topics, so we cannot talk about them.
And we also try to, follow up with the new issues or PRs that have been updated on the… on the project, with… with everyone who joins, and we try to prioritize or just provide feedback about that.
We have this document that is also linked in the Sikh In the… it's in the bookmarks of the channel, the AutoScript channel in the Slack. You… you are in the Slack, yeah. So this is the… this document is in the bookmarks of the channel.
As for you.
Have any topic, or something that you want to talk now, or in the future, just add Project. This is editable by anyone, so you can also add that topic there if you want that to be talked, or whatever.
So, if you want to join and add your topic, you, you are… You are free for that. Okay.
**Ben Joseph** 06:25 Thank you.
**nacho** 06:27 any… So, yeah, so let's go with the topics we have from last week.
Are you okay, with that, Billy, also?
Okay, so we have, let's follow this, concurrency issue. Still working on this.
This is a PR from, Yeah, this is… this has been, This is… we will switch to Swift 6.
But there were some concurrency things to implement, there is, Willie was working on this PR.
For the concurrency updates?
Right? So what's the state of this PR? Billy?
**Billy Zhou** 07:21 I haven't touched it since before, Yeah, I can spend some time on it today.
**nacho** 07:31 Yeah, my feedback…
**Billy Zhou** 07:33 Yeah.
**nacho** 07:34 Yeah, this is my feedback, that they posted here. It was basically that… I then… I, I don't… think we should… Make protocols for the users to be sendable, if possible.
That's why he was asking.
**Billy Zhou** 07:56 Oh, I see, so, like, the log record processor… Vertical… specifically just verticals?
**nacho** 08:06 Yes, specifically for protocol.
**Billy Zhou** 08:08 the new behavior I didn't intend to do.
Yeah.
**nacho** 08:12 So I don't know if that's… I mean, if that's really needed, for the library, okay.
and it's part of the spec, and we cannot avoid it, that's great. But if not, I think if we can avoid that, because it has some limitations that maybe we can It's possible, right? Because maybe the low record processor, I don't think it will need Right? For example, why would it need to be sendable?
Because it's… Except… I mean, it should be sendable, if it needed itself, so… I don't know if I'll try…
**Billy Zhou** 08:52 to remove the… I didn't realize I added those, annotations.
Or the, the, sendable, extension to, Some of these…
**nacho** 09:03 I mean, for the rest, it looked great. Just evaluate.
In Protocol C, we need to force this kind of things, which limits the possibilities later for the implementers.
But yeah, for the rest, it looked, great for me, but this can be probably, Andrex, so…
**Billy Zhou** 09:22 Okay.
**nacho** 09:23 admit.
**Billy Zhou** 09:24 And then did we, release the, the, all this 6.0 stuff? Oh yeah, we did, so… I know, we merged, on…
**nacho** 09:39 We… we released the… the core one, this is the two-for-one, right?
**Billy Zhou** 09:45 I mean, okay.
**nacho** 09:46 Yeah, and for the non… and this is released, and I think we released also, the… The non… the… the sweep with… with these changes, yes.
And we.
Gummer.
Yeah, taking… yeah, that's the last one.
**Billy Zhou** 10:06 I don't think we released it on Main, did we?
**nacho** 10:10 Create on.
I'm sorry.
**Billy Zhou** 10:14 Open on the main package.
**nacho** 10:16 The main… this is the main package, yeah, this is 2-for-1.
To sweetener.
**Billy Zhou** 10:21 We did the last release on May 11th, but I think the… Migration was merged on, like, May 20-something.
**nacho** 10:30 I… sorry, I didn't… my English is not very good, I couldn't understand that.
**Billy Zhou** 10:36 Like, the, the PR for upgrading to Swiftv6 in, in this repo that you checked out?
**nacho** 10:44 You mean, do you mean…
**Billy Zhou** 10:45 wasted.
**nacho** 10:49 No, not on this one. I mean, alright.
Or, I don't know.
Yes, it was updated. It was March, yeah, on the 20th of May.
I need to work.
**Billy Zhou** 11:04 But I don't think we released it, right?
**nacho** 11:07 I… That we… sorry.
What do you…
**Billy Zhou** 11:13 It wasn't deployed?
**nacho** 11:15 It was the plug, yes.
**Billy Zhou** 11:17 It was, I, I don't see it in the, change notes or the latest tag.
**nacho** 11:25 Oh, it was… This is amazing.
**Billy Zhou** 11:27 May 11th.
Yeah, so…
**nacho** 11:30 Okay, and your commit was?
**Billy Zhou** 11:33 May 21st, right?
**nacho** 11:35 Oh, May 21st, then it's not here, yeah, that's right.
**Billy Zhou** 11:38 Yeah, it's not in the notes either, okay.
**nacho** 11:40 Yeah, sorry, I, I, I missed the dates. Yeah, it was 11th of May, and… And yours was March… yeah, that's right, yeah, on the 20th of May. Yeah, it's not, it's not there. So yeah, I think if we can make that also improve.
with your… with this PR, it will be great if we can release the full thing.
**Billy Zhou** 12:04 Okay, we gotta fix the sendable thing. And then the other thing was, need to review the, the sessions.
contribution.
on… Main rep.
**nacho** 12:16 Yeah. I think… is this… Okay, to be reviewed, who this was?
**Billy Zhou** 12:27 I'll review it right now.
**nacho** 12:30 You mean, here, the session's thing about the.
**Billy Zhou** 12:35 Yeah, someone… Yeah, someone added, max lifetime and restore persisted session configuration.
**nacho** 12:47 Oh, but that… that was him…
**Billy Zhou** 12:50 Yeah, it's, 1107, add configurable Session Lifecycle Rules.
**nacho** 12:56 Okay.
**Billy Zhou** 13:08 Yeah, I'll just finish reviewing this today, I don't know why this is failing, it's kind of weird.
**nacho** 13:15 Yeah, it's weird, and I think… Maybe we can… Granted tickets again? Because it's… Very old, the last commit?
You see, we cannot rerun.
I think that happened also with Ola.
we cannot rerun the test.
Because the commit was so… Because it has, like, updated. It's more than a month after.
the committee… E.
It doesn't allow to rerun their tests.
But, yeah.
**Billy Zhou** 14:03 I see, and you said other, PRs had this issue as well?
**nacho** 14:09 Sorry, sorry.
Sorry for my English, I didn't catch that either.
**Billy Zhou** 14:14 Oh, no, sorry, Did you… so, like, the… you said that these, approval workflows are, like, failing for some weird issue?
**nacho** 14:27 Yes.
**Billy Zhou** 14:27 Did you mention, like, other PRs also see this issue as well?
**nacho** 14:32 We, we have seen some failing, yeah, in other, in other PRs. I don't remember which one, but we tried… I mean.
If you have a… If you have run a check that fails and it has been one month without new commits, in GitHub, by default, it disables running The checks again, if you don't commit.
anything in the year, and that has happened in the past, so I think that's the reason we cannot run this, probably because the commit was one month older.
Yeah, probably this one.
When he added these…
**Billy Zhou** 15:12 Okay, I'll leave a comment then for Robert.
**nacho** 15:15 Yeah, if he can just do the minimal, the most minimal PR, probably we can run the test again.
Yeah, sorry, I lost that.
Well, I'll be… And you had to review this, right?
Millie?
**Billy Zhou** 16:07 Thank you, I just reviewed it.
**nacho** 16:09 You, you already reviewed?
Oh, yeah, that's right.
**Billy Zhou** 16:14 I just did it, yeah, I just tell them to fix the, the approval workflow.
**nacho** 16:23 Okay, yeah. Probably, if you ask him to just commit something… If a change, it will allow to run the test again, and we can… And it's… yeah, and if it's good, we can approve that.
unmet.
So… You, you have approved that? Can you approve Billy, by the way, or you cannot?
**Billy Zhou** 16:46 I don't know if I have… Right, permissions, Oh, I do, I do, I do, I do, I do. At least on the main repo. I don't know if I have it on core.
Let me check.
**nacho** 16:59 Yeah.
DT is the main repo.
**Billy Zhou** 17:03 Yeah, I have approval work. I have, yeah, right permissions on main.
**nacho** 17:07 Okay.
**Billy Zhou** 17:09 And also on the other one, yeah, I have it on both, okay.
**nacho** 17:12 Okay, great, yeah. That's the kind of thing that sometimes are missing.
Issues with API types, hiding extensions in SDK. Review this later, I don't remember what it was about last week.
Oh, yeah, that… I think that's because… Yeah, because on some of the… API things, that are defined in the APIs.
If the extensions are not marked.
as public themselves are not visible, by… because by default, the extensions don't, need to have their own visibility labels there. And, so I think that that's something that Bryce was gonna review last week. Yeah, that was about that. Yeah, we also talked about Cocoa Pulse deprecation plan.
It, it, it, it was, I, I think… Ari, worked on this. It was about… we… Cocoa Pots, you know, is gonna end their life in December.
So we plan to, probably mark September as the last month, where we are gonna release something, Cocoa Pots.
compatible?
And I don't know if you use anything about cocoa pots, Ben.
your company, or you are using SPM. I hope you are already in SPN.
**Ben Joseph** 18:40 No, so, I'm not entirely sure what's the plan there. We do use CocoBots, but, like.
I'm… I wasn't aware about the deprecation plan.
**nacho** 18:52 Okay, yeah. Yeah, our plans here, is that we probably want to release the last version in September.
And have those 2-3 months in case something is broken.
To be able to fix that before CocoPos ends themselves.
So, having the last version in September, that will be CocoaPods compatible with the latest code there.
That's… that's more or less the idea of the depreciation plan.
**Ben Joseph** 19:20 Got it.
**nacho** 19:21 So yeah, the thing is that if we do something in November and we fail, and they end in December, we could have a broken version. That's not what we want. We prefer to have something That works even if it's all, yeah.
This was about co… Nothing new… Then, This was about CodeQL that's always broken, on the analysis.
This is a check that we have, but we are not, following that.
And the other is about… local warning and duplicate instruments registration, that I think had to be also I'm used to buy… Bryce?
Said that? I don't know. Yeah, it has not been reviewed.
But I think we've… oh, this was the original one that had that problem, or not?
Okay, yeah, this is more or less new.
Okay, so these are the things that we have from last week. If there are no new topics, we are gonna review both projects, if there are any new issues or new PRs.
To assign, them.
So on core, issues, new issues… Yeah, this is the… the… when we talk about concurrency, This dependency dashboard, that's about the dependencies, being handled automatically, and about pull requests, We'll have just… updates on… On this week.
Dependencies, which is, noise, always.
You have the warning and duplicate instrument, that's the one I… I just opened, yes.
Okay, final checks, I don't know if we want to… W something here?
If you have any doubt, we can preview them later.
And… any other thing?
Nothing more related here, right?
That's new, or not handled?
So, let's go with the… Maine.
Project.
Any new issue… Okay… Recent version of logs have changed the API.
Sorry.
Okay, this is… so this is a PR that's open?
To handle the new version of the library.
Don't we?
Okay, that's… We will see that then it appears.
And this supported TLP profiling.
Yeah, yeah, we handled this last week, because I'd say in that… We have no AVPX support on iOS.
So, probably doesn't make sense for us. And also, profiling in the phones, I don't think it's our… are you also using, strips of TLP for phones, or… Or, or laptop, or… Not server, right?
Ben, for your use case?
**Ben Joseph** 23:33 No, no, I don't think so.
I… no, no use cases.
**nacho** 23:38 Okay.
Yeah, this is more for core service running, usually, but it's part of the spec, so we are not giving it much.
Hey, Ben, what's priority?
**Billy Zhou** 23:51 What do you work on at Grafana, by the way?
**Ben Joseph** 23:54 I'm starting on the SDK side, for mobile.
My core expertise is in Android, but I'll be working on all the mobile platforms.
**Billy Zhou** 24:08 Very cool.
**Ben Joseph** 24:09 Yeah, I mean, like, we hope to, you know, make use of the OTL SDK, but, like, building on the other side, like, whatever is, required for additional support, or, like, help.
Fill any gaps?
hopefully contributing back to the, the original open source SDKs. So that's the idea.
And that's… yeah. That's what brings me here, yeah.
**nacho** 24:35 We are…
**Billy Zhou** 24:36 So I'm gonna work on this anymore.
**Ben Joseph** 24:38 Sorry?
**Billy Zhou** 24:39 I said I'm jealous, because I don't get to work on SCK anymore at my workplace.
**Ben Joseph** 24:44 Okay, okay.
**nacho** 24:47 Yeah, we are open to any contribution to the project.
Thank you.
**Ben Joseph** 24:52 Yeah, if you work with…
**nacho** 24:54 if we… you work also with Android, you will see that they have much more instrumentation published as public.
Yeah. Yeah, here we have not had, so many contributors to, instrumentation.
So yeah, that's also.
Something that we… you will see a bit different between both.
Okay… So this is our… the issues… also, if you… I mean, for both projects, probably in a presentation, there are more.
If you are interested in some of these topics that are open, some of them are… that's to take… if you are starting with the code, there are some that should be… Labela's good fist… first issue.
for… Some of them, just feel free to take any, or ask, in them about taking them.
So yeah, that gun.
That, that's open, also.
**Ben Joseph** 26:01 Absolutely.
**nacho** 26:01 And… Yeah, and regarding pull requests for the main target?
There is nothing… You know, this is the life cycle, right?
That we have been talking before?
There is also this distribute and tracing bridge.
Yeah, this is the KS crash reporter that Willie worked on the past.
That still needs some… Updates you.
Before merging, this one, the session one, yeah.
The distributed tracing, this was about… M-make… About using this, feed tracing library from Apple, to generate hotel.
open telemetics with, things?
And it's, it's in progress.
Yeah, so it's… it's… it must be… Yeah, Simon Bility is working on it.
And it's advancing, more or less.
Slowly, but yeah, probably we'll have something there.
And this is the other PR we have. So, yeah, those are all the… Piers… Yeah, yeah, there was also this one about You're assessing instrumentation.
But I think it was said that Yeah, Hari was, was… Was, following this.
So, yeah, that's all. Or they… Meeting, if you don't have any other topic to talk about?
Or any other development that you have.
In mine, or any… or any general question about the library, how to use that?
Yeah, yes, we can.
**Ben Joseph** 28:24 I'm sorry, none at this point, I'm just, getting started.
**nacho** 28:28 Okay.
**Ben Joseph** 28:29 Hopefully, by the next time we meet or something, I think I'll have more context.
**nacho** 28:35 Okay, yeah.
**Ben Joseph** 28:36 wanted to get a head start and, like, you know, be here. I'll see how I can help, or where I can get started.
**nacho** 28:44 Great, yeah.
**Ben Joseph** 28:45 Some of that is, clear now.
**nacho** 28:47 Yeah, also you can ask questions in the channel, but, yeah, but… Yeah, all the contributors now, are… Can only work this part-time.
And the maintainers, so we… Tried to keep it working, but we cannot We… none of us have… And that present dedication, or even work on this, on their, companies currently.
So, yeah. So… Sometimes you can expect some delays on review and on things like that, because people is… Most of the, you know, people now on the project.
Are doing this on part-time or on free time only, so that.
**Ben Joseph** 29:38 That's true.
**nacho** 29:38 Please take that into account.
Okay.
So then I think we can end up here.
Yeah, and finish this meeting.
Apparently?
Okay.
**Ben Joseph** 29:55 It was nice meeting you. Thank you.
**nacho** 29:57 Thanks for joining. Usually there is more people, but yeah, I think, All of them had, like, different themes.
Okay.
**Ben Joseph** 30:06 Thanks. Thank you.
**Billy Zhou** 30:08 Thank you, guys. Bye.
