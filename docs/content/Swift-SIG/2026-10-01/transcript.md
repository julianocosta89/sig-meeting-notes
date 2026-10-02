SIG: Swift SIG
Date: 2026-10-01
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Vishwan aranha** 04:32 Hey, guys.
**Nacho Bonafonte** 04:37 Oh, good afternoon.
Sorry, sorry.
We are probably on today. I know from other maintainers that, yeah, they are.
Basically. Yeah, so I will… Try to handle it again.
Okay.
The… so let me share my screen.
Okay.
Sorry for… I didn't have time for… creating an NC for today, so I will copy this quickly.
Okay, Ali, I think you have not been here in the past. Do you want to… Present yourself for, I mean, it's so if you don't want to to share, that that's also fine. Just just to know you what are why what are your role, what are you doing, what do you want from from the project, and that that will be great while I continue preparing this document.
for… for everyone.
**Ali Ghaznavi** 06:14 Yeah, no worries. Yeah, so I'm Ali. I'm a member of the Firebase Crashlytics team.
And I'm just, you know, like, here to, see what's going on on the OpenTelemetry, like, Swift side of things.
And stay up to date with, you know.
Whatever, whatever the latest updates are.
**Nacho Bonafonte** 06:40 Okay.
Great. Let me.
Yeah, we usually, in this meeting, we usually… Yeah, we reviewed topics from last week.
And we add some other topics.
That anyone… That people can have.
So, yeah, basically… and then we review.
if there are new issues in the project, or if there are new PRs to review.
So, yeah, that… that's usually what we do in this meeting.
usually more people. Today we are a bit short on people, but yeah. Okay, yeah, from last week, approval access request for Ben Joseph and this one.
So, yeah, I have not been able to meet with the other, Approve, sorry, maintainers this week.
Yeah, they, as I said, they are… Yeah, really busy, The other two maintainers.
Changed their, jobs recently.
So I think their time for the project is really reduced to a minimum.
Yeah. So, yeah, sorry for that delay.
**Vishwan aranha** 08:03 That's fine, like, we have a PR up, but yeah, whenever you guys get a chance, you can approve, yeah.
**Nacho Bonafonte** 08:08 Yeah, thanks. Yeah, thanks for that. Yeah, that's the point, right? You also have, probably not seen Ari or Bryce for a long time in this meeting, and that is the reason.
I will try to sync with them.
I will ping them again and see how can we handle it, because, yeah, if they have less time.
Definitely having more approvers is something really useful.
So, yeah.
Okay.
Next version of Hotel Swift with book fixes.
Okay, yeah, release for 260 is already for the main library.
It's still, in, in… In preview mode or draft mode?
So, it's not the latest release. So, yeah, I created this today.
Yeah, because I merged the peers that were missing. I have created this peer release here.
It will be great if we… Can test it for one or two days.
So probably… Yeah, or during the, for, for… Doing it publicly on Monday, I think that that's a good… Timing for this?
It also, uses the… a core version which is This one… Yeah, this is… if you said this one that was released last week.
And now everything is building, the test… passed on the nightly bills also, so yeah, that's them.
That is already introduced.
**Vishwan aranha** 10:14 Makes sense. So they, they're… the code has been freezed. So, frozen, so there's a code freeze, and we are not introducing anything else into that PR.
**Nacho Bonafonte** 10:24 Yes, that's right, yeah. So, yeah, my, my, my… Yeah, talking about this… The thing is, Yeah.
Sorry. As we mentioned last week and the week before.
We are freezing core.
And the next thing we should do is bring in core into main library again.
I can create a PR, or, If you… or any other today. You are the only one here who has experience with the code.
So if… it will be great if we create a PR that just brings everything from core into the Swift library.
As it was before. So before it was, basically.
Yeah, if we have… Both libraries.
Just for comparison.
Yeah, basically, we want The… We… We want to move source.
no, this is for… no, sorry, this is correct, okay. Yeah, In source, we have sources with the API… these… these libraries?
Like, they are, they should… Should be moved.
Fuck.
Into this, into these sources.
That's the thing. They were in the past.
I don't know exactly when, because… Yeah, probably the first comment here.
I don't know if we can navigate there very easily, or… Yeah, because it has many pages, right?
Yeah, that's gonna be Ml.
Oh… Ali? Yeah, you raise your hand.
**Ali Ghaznavi** 12:43 Yeah, sorry, I just had a clarifying question. So, when the core moves into the OpenTelemetry Swift repo, the core will still stay there, right?
I'll continue.
**Nacho Bonafonte** 12:56 I'm, I mean… Yeah, yeah, we are moving the code to the main library.
Right now. So, that's the first thing we might want to do after releasing 2.6.0, so that's gonna happen Soon, very soon, probably in the same… in the next week.
It should be there, and all the development that happens on core should up in… on the… on the main library. That was originally like that. It was only OpenTelemetry Swift with all the libraries there in a… big single package.
There were some companies that wanted that.
separated because they only wanted API and core, and SPM Even several years later, it still downloads all the repositories that are dependencies.
So, people who only wanted API or core.
Wanted to have it separated in a different repository in order to download faster, especially on CIS, which, yeah, I mean, it's fair.
You can also solve that by using… touches and things like that, but okay, but yeah, they asked for that, and we changed. But we have seen that development there has been absolutely.
Slow, and adding lots of problems, and a lot of maintenance burden that we have not enough resources to handle.
So, we are moving back the development into the main library.
But we plan to keep.
source code only copy at core. So at core, there will only be the repository with a simple package.
But no… more commits than just copying what's from the main library. So people can use that with a package, they can link that, and they can use, but the main repository is not gonna use it directly.
**Ali Ghaznavi** 15:07 Okay.
**Vishwan aranha** 15:08 existing Okay.
**Ali Ghaznavi** 15:11 Sorry, please go ahead.
**Nacho Bonafonte** 15:12 Existing users of the core will continue using the core. The existing users of OpenTelemetry Suite We'll continue using OpenTelemetry Suite, but OpenTelemetry Core won't be a dependency anymore.
**Vishwan aranha** 15:25 So the existing pending PRs will need to be updated, the ones that have been approved.
**Nacho Bonafonte** 15:31 In Swift Core, yes.
**Vishwan aranha** 15:32 no.
**Nacho Bonafonte** 15:33 I know.
**Vishwan aranha** 15:34 In the other Swift repository.
**Nacho Bonafonte** 15:36 No, no, in the main library, no, no, no, no, because we are moving core into the main library, right? So everything will be in the same place. The changes that are the PRs that are created in the main library.
**Vishwan aranha** 15:47 Okay.
Because I have one.
**Nacho Bonafonte** 15:50 And they don't have a problem with whatever is in core, right?
**Vishwan aranha** 15:54 Okay.
**Nacho Bonafonte** 15:54 Because they are in the code that's already in that repository. So even if we merge core into main, there should be no problems with existing PRs.
**Vishwan aranha** 16:03 Okay, so as long as there's no issues or conflicts, then we should be fine.
**Nacho Bonafonte** 16:07 Yeah, it shouldn't be any, because code is totally separated. I mean, API and SDK and OTLP, some stuff is there.
But we are moving back.
So, they will be in different folders, so no problems with existing PRs. Only the PRs that exist in SwiftCore, that are… most of them From Renovate Bot, Will… will be discarded.
And they are… yeah, they are… Small things and… or things that have been there.
for a long time, or not updated. So, yeah, that… To them, yeah, Brian.
And also, these approvers here will, you know, it will be discarded, all the PRs here.
We won't accept PRs in this project, except when we copy the code, when we release on the main library. So we will release the main library, we will copy all the code back to this repository, where it will be alive for whoever wants to link with it.
But the main library won't link with this.
And we will avoid any burden with any… we don't have actions, we won't have renovate bots, we won't have anything here.
No maintenance, just maintain… maintaining, one repository.
**Vishwan aranha** 17:30 Makes sense.
**Ali Ghaznavi** 17:31 That makes sense.
**Nacho Bonafonte** 17:32 that's.
**Ali Ghaznavi** 17:33 Thanks for your time.
**Nacho Bonafonte** 17:35 Yeah, yeah, I mean, that's something that, yeah, we decided to do, because… Our resources have been always been very low. We expected That the companies who asked for this.
will help maintain it, but they disappear once they, got this. So… Yeah, you know.
That's life.
So, yeah, that's the thing. So, continuing with this, yeah, that's the thing.
So, new topics… I will, Yeah, I think I will take… that I will. I I added, here we we can handle it later.
Okay… When can we release already in preliminary? Yeah, this is done.
Sessions PR to do… Yeah, now we can start once we have the release.
created, we can continue with the PRs that we were reviewing.
Anything about… this PR fast.
**Vishwan aranha** 19:01 Oh, it's all the approaches needed a merger for maintainers.
**Nacho Bonafonte** 19:05 Okay.
Yeah, I will take a look then. Yeah, I've been focused only on merging what was needed, bringing Yasura, the dog who had some things there to merge, and fixing a… I build, I don't know why they build.
was failing, but we didn't notice when merging appeared in the past, so I had to fix that and wait for approval, so for the maintenance, also for that, so… Yeah, I think the metric is ported back, and this stuff. Done.
And then, yeah, okay.
So… Yeah, this requires time.
I think… This was March also.
This was March.
And session persistence. Yeah, this is approved, right?
**Vishwan aranha** 20:05 Yes.
**Nacho Bonafonte** 20:06 Yeah, proof that… So I am merging now.
I prefer not to have too much description.
Especially if they are just commits.
Okay… So that means… these… So, all these are 100, then?
**Vishwan aranha** 20:37 Yeah, the new topic is gone then. Yeah, it's the same.
**Nacho Bonafonte** 20:41 Okay.
So… oh, yeah, there are still some here.
Oh, this is the app.
From… Okay, yeah, some… Things are still not clear.
Yeah, probably they need some.
Yeah, we try.
okay, so I think we can remove this one.
Oh, so the new topic you added was the one I merged?
**Vishwan aranha** 21:12 The one that I added was, like, just a link to the PR, and it's already merged, so it's all good.
**Nacho Bonafonte** 21:17 Okay.
**Vishwan aranha** 21:18 Aramura.
**Nacho Bonafonte** 21:18 Okay.
So, let me check these three, because I don't think I have clicked them properly to know if I can remove them or not.
Sessions persistence, this has been merged, so that was the third one, right?
Astra Sanitation, that's the second, and it has also been merged already.
And testing, and again, sample app. Okay. Yeah, it has some text failing.
But it's approved.
Yeah, I… yeah, I don't know, I met the branch.
Because it was working, but I don't know why it's failing, so.
I tried… Big scene.
The conflicts.
Yes.
Okay, so the other thing, we have… is the… Hi, Ben, sorry I didn't realize you.
That's connected. Yeah, the other thing is what we have mentioned is moving the Pentalamity Swift core back to main library.
I was planning on doing that.
Yeah, it was in the past, it should be just moving then.
moving this… this code back again. So we have just one.
repository to maintain.
And whenever we are gonna release version 3.0, then, because we will rename to 3.0, okay?
I think it's better for maintenance, so people can know that this has been released.
And yeah.
And moving these, sources, especially this. This will be inside the exporters.
And this will be, the root of source.
And probably this test.
Ruthie, what's this?
Yeah, maybe it should be inside test. But yeah, that's basically… I will move that.
Accordingly to the main app. Again.
And we can… Yeah.
Because that was the last version we will use.
Or, for cocoa pots, and we will move to the question 3.
Okay, so.
Another topic.
And I think it's also something important, that we should take a look.
Or take decisions, probably this, in this forum, or… Asking in the chat.
in the… in the Slack thread… in the Slack channel, also, if… It's about what minimum version do we want to support.
So, the thing is, currently.
If we go to OpenTelemetry Swift.
Package… Yeah, these are our minimum versions.
Wow.
So, Just thinking… What should be the minimum versions to support from now on?
After… 3.0.
What questions do you think are… Would be good enough.
For… for this.
I'm thinking about probably the latest Xcode version, Xcode 26.
What's the minimum SDK that we can target?
Any idea there?
What are your…
**Vishwan aranha** 26:31 people.
**Nacho Bonafonte** 26:31 Funny minimum.
**Vishwan aranha** 26:33 Did people, like, complain about, like, is it gonna be safe? Should we test first?
Check, like, send out a warning, like, we'll… Yeah.
**Nacho Bonafonte** 26:44 That's right, yeah, we need to warn people.
**Vishwan aranha** 26:47 Yeah.
**Nacho Bonafonte** 26:48 They… I mean, the thing is for the future, so it's not… it will be the first 3.0, so they… We'll be able to use 2.6.
So basically, do you have a minimum version of your company, for example, that you are Targeting?
**Vishwan aranha** 27:07 I don't… we don't have, anything yet.
Okay. Ben, Ben, do you happen to know? Do we…
**Ben Joseph** 27:15 No, no. So we just built for iOS, and Yeah, so not sure about what the… but I understand, like, the Xcode 27, it has changed some of these minimum supported SDKs, but yeah, I don't recall what exactly. So I think that would be more of a limitation with the Xcode than, like, anything else.
**Nacho Bonafonte** 27:44 Yeah, maybe we… I mean, I think Xcode 26 is still supported.
At least for App Store.
So maybe targeting the minimum version with Xcode support, Xcode 26 supports.
I don't know, maybe it's iOS 16, iOS… 15? I don't know. Maybe we should target something like that.
Do you think iOS 15 is good enough?
It's…
**Ben Joseph** 28:22 Yeah.
**Nacho Bonafonte** 28:22 5, 6 years, right?
**Vishwan aranha** 28:23 Yeah, I think so, but we should also check with other maintainers as well, just in case, if anybody has any complaints from Apple or any others.
**Nacho Bonafonte** 28:32 Okay, yeah.
So…
**Ben Joseph** 28:35 A lot of the enterprises, they support, like, N-3 versions for iOS, because, like, unlike Android, like, they get… a lot of the devices get updates, so I think… pretty, very, very old devices, only those will be stuck on 13 at this point. Like, Xcode 27 minimum support is 15 right now for iOS.
**Nacho Bonafonte** 28:59 is 15.
**Ben Joseph** 29:00 Yeah, for 27, not 26.
**Nacho Bonafonte** 29:04 Okay.
I'm gonna write in the Swift channel.
**Ben Joseph** 29:28 Yeah, my preference would be to support whatever Xcode 27 supports, because, like, otherwise you are forced to use an older version of tooling, and that covers a pretty broad range.
So I think, like, let's put that for recommendation, and if somebody says that they still want a lower version, then we can consider that. Otherwise, I think we should stick to the floor provided by Xcode.
**Nacho Bonafonte** 29:55 Okay, yeah, that… yeah, that brings something… yeah, iOS 15, I think it's macOS 12.
So we are using macOS 12 already here.
But using iOS 13.
**Ben Joseph** 30:08 Yeah.
**Nacho Bonafonte** 30:09 So maybe… yeah, maybe that makes sense. I don't know why we moved to Mac 12.
To be honest. But no one has really… Say anything about that, but yeah.
Yeah, I think I'm gonna.
I'm gonna ask.
Because we also moved to… Swift Tools version 6.
For structure concurrency, so that… Yeah.
I don't know if that… I'm not sure if that has a minimum version, but yeah.
I think that can.
TVOS 15, Watsos 8.
**Vishwan aranha** 31:16 Yeah, 15 seems like a safe bet, yeah.
**Ben Joseph** 31:19 Yeah.
**Ali Ghaznavi** 31:30 I just shared in the chat, like, Apple's guidance on minimum versions, for the latest Xcode, and this is usually what we like to follow.
**Nacho Bonafonte** 31:43 Yeah, the problem is that sometimes we have had Some users of the library that needed to, address older versions.
Of the platform, because of contracts, basically.
So the… usually… Middleware, Applications or observability platforms that use the library that At the same time, they had users which had contracts, government contracts, usually, which had a minimum version that were lower than this, but… That has been in the past, so… Yeah, Apple, yes. I mean, it will move to use only Xcode 27 probably soon.
And so whatever Xcode 27 supports is… will be the… the minimum that Apple, will provide, so…
**Ali Ghaznavi** 32:43 Makes sense.
**Nacho Bonafonte** 32:46 So yeah, that's another topic. So, for the… So, okay, so no more new topics?
Any other topic?
you want to address, or you want to bring up Ben or Ali.
I think this one has left.
**Ben Joseph** 33:19 I'm good.
**Nacho Bonafonte** 33:20 Okay.
Then do you want to review some of these new issues, if there are any, or any… PR that you are interested?
**Ben Joseph** 33:31 I don't have any pending or, like, anything that's particularly pressing at this point, but I can do general review with you.
**Nacho Bonafonte** 33:40 Okay.
Wow.
**Ben Joseph** 33:44 I think Trask had pointed some… like, in the Slack channel, he had posted some of… some…
**Nacho Bonafonte** 33:51 Okay, yeah, that's… that's something about a secure PPR, right?
**Ben Joseph** 33:56 Yeah.
So, yeah, this one.
**Nacho Bonafonte** 34:24 Yeah, I… There is something… Yeah, okay. It looks good, right?
**Ben Joseph** 34:35 Yeah.
**Nacho Bonafonte** 34:36 It should just pass this test, right?
Is this more of a test?
**Ben Joseph** 34:45 Understanding.
**Nacho Bonafonte** 34:55 Yeah, he tried to appropriate that himself.
Yes.
**Ben Joseph** 35:00 There's one more in SIP core. I posted the link in the channel.
**Nacho Bonafonte** 35:07 Okay.
You're in detail. Sorry, I… you have…
**Ben Joseph** 35:35 No.
**Nacho Bonafonte** 35:35 something.
**Ben Joseph** 35:36 One more PR from Trask. I posted it in the Zoom chat.
It's in SIFT Core.
**Nacho Bonafonte** 35:44 Yeah.
Yeah, I can approve that. As I said, we are not gonna continue.
With this, you know?
Living with the life code in this PIA.
I can merge it so he can be happy, but yeah, the idea is blocking this for…
**Ben Joseph** 36:04 that's.
**Nacho Bonafonte** 36:05 or more PS.
once we… yeah, the idea is moving this to the main repo, and everything needed will be there. And it will help a lot. Testing new code in the main repository, not having to release Oh… Not having to release.
Versions of one library for the other to be.
Life… yeah, it was being… That's our maintenance, rather than that. Yeah.
Do that.
**Ben Joseph** 36:38 We update the README or something to reflect this.
**Nacho Bonafonte** 36:43 Yes, that's right, yeah.
Would you mind doing that, for example?
**Ben Joseph** 36:52 Yeah, I can do that. Sorry, so I missed the initial part of the meeting.
**Nacho Bonafonte** 36:58 Yeah, okay, yeah. Yeah, I think… yeah, we are only now, us both.
Yeah, I think, yeah, what we mentioned, was basically that we are moving all the development To the… to the… to the main library repo?
**Ben Joseph** 37:23 Yeah.
**Nacho Bonafonte** 37:24 So all the development… And and yeah.
Basically, something short and… Maybe you can express it better.
Yeah.
But basically, the idea is we are not continuing development in that repo.
Because it's gonna be only a copy of what's been Store it in the main repository.
**Ben Joseph** 37:51 So is the plan to copy and like maintain two separate libraries, but in one single repo or merge it into a single library?
**Nacho Bonafonte** 37:58 No, the idea is having one simple… one single library.
**Ben Joseph** 38:02 Okay.
**Nacho Bonafonte** 38:03 And sharing that, and it's time we release that code, copying the files into the other repo.
Okay. With the same package.
**Ben Joseph** 38:13 Okay.
**Nacho Bonafonte** 38:14 No PRs, no… Issues… Nothing in that code, except a repository with a Single package, for people who want to just use that.
But no development, no PRs accepted, anything like that. It will be considered just a… proxy repository?
Or I don't know what would be the proper name for that.
But basically, that's the idea.
**Ben Joseph** 38:43 Yeah, I think we can archive the repository. That would, there is an option in GitHub to archive.
So it will maintain a read-only copy. I mean, I don't know if you want to do that already.
Yeah, but…
**Nacho Bonafonte** 38:57 No, but the thing is that we… Some maintenance.
Some maintenance. But we will continue adding versions. So, for example, when we release version 3.0 of the Mine Library.
We will… Copy that code, and we will tag that as 3.0.
**Ben Joseph** 39:17 Okay.
**Nacho Bonafonte** 39:18 But no bills, no nothing.
No actions, no… Cocoa Puffs, no, nothing… Both.
**Ben Joseph** 39:27 I'm curious, why the version?
**Nacho Bonafonte** 39:32 We're keeping the version, because there are still users of that library.
We don't want to… we… they forced us to create that. They promised they will help maintaining it.
Okay. That didn't happen, and that meant that we were doubling the maintenance of our repository.
With all these… you know, updates things on third-party libraries, and with all those security things, with this PR, like, Trask PR that, you know, he created double of it.
And adding extra maintenance that no one wants to handle just for that. So…
**Ben Joseph** 40:11 Oh.
**Nacho Bonafonte** 40:12 We keep a single copy. We also avoid having to release a version.
I mean, if you add something that needs both core and main library, now you have to wait for the core to have that version.
**Ben Joseph** 40:26 Yeah.
**Nacho Bonafonte** 40:26 other to land.
**Ben Joseph** 40:28 Makes sense.
**Nacho Bonafonte** 40:28 That's… that's a mess.
But you cannot really develop like that, right? You cannot.
**Ben Joseph** 40:33 6.
**Nacho Bonafonte** 40:34 Backs easily, you cannot… I mean, that's a burden for everyone.
So… We decided we were feeling that again. And going back to our initial, idea that worked better and had less maintenance and better development cycles.
That's the thing. We were… parts to that?
it took some time to get us there, even. But even… but without… with false promises, promises that Said will help with the maintenance, and that that was not true at all.
So, yeah, we forget about that. And people who use that repository, that will be okay. They can still… the only problem they will have is if the same library is linked by several third-party libraries at Merge.
They will be identified as two different libraries.
Because OpenTelemetry Swift and OpenTelemetry Swift Core.
will be… different bundles, but…
**Ben Joseph** 41:39 Yeah.
**Nacho Bonafonte** 41:40 That's the only… the only…
**Ben Joseph** 41:42 How long do we need to support that? That also, I think, like, we can stop now on one or two versions, or what?
**Nacho Bonafonte** 41:49 I don't… I don't know. If we could do that automatically, with an action or something that just copied.
And through the data, that will be… Good enough, I think.
Okay. We could maintain that for longer, but the thing is that it won't have anything except Cool.
The SWIFT files and the SPM, and the package file. Only that.
If it doesn't build, it's not my, you know, it's not my program.
**Ben Joseph** 42:19 I.
**Nacho Bonafonte** 42:20 To be honest, maybe we only accept a PR for fixing builds with a package.tree file.
But yeah, that's the only thing we are gonna do with that.
**Ben Joseph** 42:33 Got it.
I will, I'll create a PR to update the README. If you think, think any, any change in text is needed, you just come in there and update.
**Nacho Bonafonte** 42:43 Yeah, I mean, yeah, I think clarifying what's the purpose now for that project, maybe the first line.
With a big note, or something like that.
So everyone is aware. You don't need to remove anything from the README, just adding the note at the top, saying this is. Yes.
That repository, yeah, will keep You can say, might get copies of the versions. Might.
Nothing.
Not even be… I mean, we cannot be sure we will be doing that, because it will take some time. Whenever we release 3.0, we will first release on the main library, and later we will think how to copy that cleanly.
So, they don't need to be synchronized.
**Ben Joseph** 43:28 Right.
**Nacho Bonafonte** 43:28 Neither.
Okay, yeah, if you can do that, it will be great. I will try to address it.
Yeah, the PR, bringing all that code back to the main library.
**Ben Joseph** 43:41 Alright.
Alright, then. Okay. Anything else, Nacho?
**Nacho Bonafonte** 43:48 Yeah, no, thanks. Yeah, I think we can.
We can end for today. We are on.
**Ben Joseph** 43:53 Right.
**Nacho Bonafonte** 43:54 You on mute now, so… Yeah, probably we can stop here and see. Yeah, let's see next week. Also, I told this one, you were not here, 2.6.0 is already released.
**Ben Joseph** 44:07 All right, great.
**Nacho Bonafonte** 44:08 It's in pre-release, okay?
**Ben Joseph** 44:10 Okay, yeah, yeah.
**Nacho Bonafonte** 44:11 Both core and main library.
So… If you want… If possible, I, yeah.
Test that that works, as expected, in your… Library…
**Ben Joseph** 44:25 back.
**Nacho Bonafonte** 44:26 Just validate it works, it builds.
And, and, yeah, and I, so, probably on Monday.
We will make this official.
version. We will make it the latest version official, and so everyone can use that.
**Ben Joseph** 44:46 I will update our test bills today itself, and if I know.
**Nacho Bonafonte** 44:49 Okay, yeah, Chris, yeah, I mean, you know, if you put them… number version explicitly, it will find it. You just put generic open telemetry shift, it will just Download the latest official one, which is still 2.5.
**Ben Joseph** 45:04 No, no, I think we have the version spin.
Okay.
**Nacho Bonafonte** 45:07 Yeah, great, great, great.
**Ben Joseph** 45:09 Yeah.
**Nacho Bonafonte** 45:10 Thank you.
**Ben Joseph** 45:11 Alright, see you next week.
**Nacho Bonafonte** 45:13 to you.
