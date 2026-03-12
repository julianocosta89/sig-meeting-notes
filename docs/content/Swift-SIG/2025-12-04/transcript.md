SIG: Swift SIG
Date: 2025-12-04
Duration: 46 minutes
Zoom Recording URL: https://zoom.us/rec/share/MMiO6TMazqGlUzSRM3EpozG9-uCADWLXmzWumonKdEXDQumo_SmkGF3_KrqNTMPC.ev5fVQtMUtZxga3w
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 01:05 Hey y'all, how's it going?
**Bee Klimt** 01:10 Hello.
Hope you had a good holiday.
**Bryce Buchanan** 01:23 Yeah, it was nice. Saw some family, you know, dodged a cold. It was good.
**Billy Zhou** 01:43 Yeah, hey guys.
**Bryce Buchanan** 01:44 Hey, Billy.
Let me check, see if the other, maintainers are gonna be here or not.
Well, I don't know where they all are, so I suppose we could get started. So, the, KTOR instrumentations… B, I think that you got, your PRs up, and, They've been approved. I was waiting for some other feedback on them, if anybody else wanted to take a look at them. But I think those are ready to merge.
**Bee Klimt** 03:46 Okay, I don't… I don't have permission to do that, so…
**Bryce Buchanan** 03:48 Yeah, that's okay, I can… I can follow up on that. I just wanted to let other people get a chance to look at them.
**Bee Klimt** 03:54 And, I'm not sure that those… there was… there was one issue that I found that they might address, an older one, but I'm not sure if they'll address the KTOR instrumentation or not. I looked at the… source code for that a little bit, but it wasn't obvious to me whether it was hitting that API. It wasn't even obvious to me whether it was doing the thing where it uses the session before the instrumentation gets installed, so I'm just… without playing with a working example, I really don't know.
**Bryce Buchanan** 04:20 Okay.
**Billy Zhou** 04:24 What is KTOR? I only saw a couple of, semantic convention migrations, what's… yeah, what's KTOR?
We lost it.
**Bee Klimt** 04:35 There was an issue that this is a Kotlin framework, and the URL session instrumentation doesn't work with it, and You know, one thought was maybe… this known issue that I was fixing, which was the other… the other PR that I opened, might also fix the KTOR thing, but I don't know.
**Bryce Buchanan** 04:55 Yeah, we'll have to check it. I'm doing some work, on, I have another issue that I've been working on. I'm finally finished with, like, the big project I was working on, so I can spend some time on it. I think it's this one down here, this URL session issue. So I can, while I'm working on that, I could try to, reproduce that… that issue on the other library.
So I'll just assign this to myself for now.
Hey, Nacho. Hey, Vanad.
**Vinod Vydier** 05:26 Yay.
**nacho** 05:28 Nope.
**Bryce Buchanan** 05:29 We were just talking about, B's PRs. If you, I've approved them, I think they look good, but I was letting them settle, like, to give you a chance to look at them, but I'm not sure if you'd like to.
**nacho** 05:42 Okay.
**Bryce Buchanan** 05:43 Okay. The workflow changes are up on… I believe both repos?
So now we no longer have to… Build everything, whenever, There's a change anywhere in the repo.
So that's, that's nice.
Let me double check. I know it's in the main repo, but I'm not sure if it's in core or not, so I might need to bring those over.
Build and test… Does have the sh… I think I need to update this, because this doesn't actually work.
Yeah, so there was a… there was a bug with it.
**nacho** 06:28 And, and so I need to update that one in there, but…
**Bryce Buchanan** 06:31 Now the repos no longer require all the builds to run unless there is a change in the sources DER, and it no longer requires, the branch to be up-to-date, as long as there's no merge conflicts, so… That should speed up development a little bit.
Swift 6 updates? Billy? Have you made any progress there?
**Billy Zhou** 06:59 Yeah, I got the build working in core, and I think I need to do some more, like, end-to-end testing, because, like, I don't know if there's, like, weird stuff that you might have in runtime, To clarify, I just made it build, I didn't, like, fix any of the, like, if there are any concurrency issues, like, it's just building using the new annotations. And then, yeah, I guess there was an issue with the, some of the thread safety in, sessions, so I put out a patch for it, and yeah, so I should have put that patch out a while ago, because I already fixed it in, AWS Hotel, but yeah, so that's going through some revisions right now, and then, I believe, And then I also have a working draft for, the, main repo as well for Swift 6 migration. One thing I need to test is, if… either of these can be, deployed standalone, because we have the separate packages. I think the core can be deployed standalone, but I don't think that the main one can.
Need to double-check that, so… yeah, I need to put together a deployment plan for this, and also get it reviewed, but, yeah, like, feel free to take a look in the meantime.
**Bryce Buchanan** 08:14 Cool, yeah, that's, this one here.
**Billy Zhou** 08:17 I don't… are you sharing your screen? I can't… I can't.
**Bryce Buchanan** 08:21 Yeah, I got to be.
**Bee Klimt** 08:24 Yeah, I see it.
**Billy Zhou** 08:25 Oh, maybe something's wrong with mine.
Hmm.
**Bryce Buchanan** 08:27 The, the, feature upgrade to Swift 6.0 number 988.
Yeah, yeah, I can't see your screen for some reason, but, that's weird.
**nacho** 08:38 Maybe the tops in the top?
It's a suit one, suits someone with a meeting, and another with a… Bryce.
**Bryce Buchanan** 08:53 Is there some… What is it, Nasha?
**nacho** 08:58 Yeah, that… maybe he's in the wrong tab in the Zoom window, maybe?
**Bryce Buchanan** 09:03 Oh, I see, I see.
Oh.
**Billy Zhou** 09:05 That makes… Thanks, Nacho.
**nacho** 09:08 It was that, really?
**Billy Zhou** 09:10 Man.
Yeah, Amazon only recently migrated to Zoom, so I'm still kind of a Zoom noob.
**Bryce Buchanan** 09:18 Well, they… they change stuff, and then… don't… it's just, like, it's just a surprise.
**Vinod Vydier** 09:24 We just got off Zoom.
**Bryce Buchanan** 09:29 That's funny. Okay, cool. Yeah, so there's that one, and then there's the, Swift Core one also, right?
This one here. And that one actually is building. Do we want to do, like, a Swift 6 feature branch for a little bit? Like, let it settle?
Users, try it out, see if it works for them, if there's any issues before just, like, pushing it to main and doing a release on that.
**Billy Zhou** 09:58 Yeah, we could do that, yeah, up to you.
**Bryce Buchanan** 10:03 Alright, Nacho, what do you think about that?
**nacho** 10:10 Yeah, I was, yeah, thinking about the… the tools version that… For the uses, if we… I'm not sure if we might keep two separate packets, maybe? Something like that? I'm not sure.
It's always about supporting the platforms that our users have to support for their apps.
That, that's… That's always my concern. We are supporting now, I think it's iOS 16?
Or what is the… Because we changed that recently.
So if there are tools that support that version and have Swift 6, for me, it's okay, move in there. You have an Xcode version that supports… we are… We are currently iOS 13, right?
**Bryce Buchanan** 11:08 12.
**nacho** 11:09 12.
**Bryce Buchanan** 11:10 Yeah.
**nacho** 11:12 Okay.
**Bryce Buchanan** 11:16 Yeah, so maybe we should take a look at… This is gonna be hard to do, right? To have a package Swift for 6, and a package Swift for 9, or 510, or whatever it is, 5.9?
Yeah. But we'll have to add a bunch of annotations to, like.
**nacho** 11:39 Yeah, that, that's true.
**Bryce Buchanan** 11:40 Compatible, right?
**Ariel Demarco** 11:41 I think we can start with core, creating the… the package… 5.9, or 5… 5.0, I don't remember.
And starting feature branch migration.
And by default, we did Swift 6.
At some point in time, everybody will have to migrate, probably.
happened with Swift 3 at some point in time. Apple said, no more 2.3, and… You are doing…
**nacho** 12:10 Because, for example, now, what is the… version that the App Store forces you to support.
**Ariel Demarco** 12:18 So…
**nacho** 12:19 index code.
**Ariel Demarco** 12:21 The next code?
**nacho** 12:22 Yeah.
**Ariel Demarco** 12:23 Let.
**nacho** 12:24 Because maybe that can give us a clue of what people really… really has to support, right? And what's the minimum version that… iOS version that that Xcode version has.
Because probably we are in Xcode.
**Ariel Demarco** 12:41 16 months.
**nacho** 12:42 something around.
For the application.
**Ariel Demarco** 12:44 Totally.
the compiler, Or… s… Xcode 26, let's say, it's Swift 6.2, but it supports up to 3.4.
**nacho** 12:57 So…
**Ariel Demarco** 12:59 you have 4 languages mode. 4, 4.2, 5, and 3.6.
**nacho** 13:05 Yeah, but yeah, I was not talking about the Swift version itself, but the platform it supports.
**Ariel Demarco** 13:12 Oh.
**nacho** 13:12 You know what I mean.
**Ariel Demarco** 13:13 Yeah, yeah.
**nacho** 13:14 If the minimum Xcode version is Xcode 16.4, for example, I don't know what it is.
It… the minimum iOS version it supports.
that we could… we could really move to that. I don't know why, for example, 16.4, support, and that's 26. It supports 15, right?
**Ariel Demarco** 13:37 Yeah, but I think that those are the ones that you have by default on the dropdown. Like, if you go to Xcode in those versions.
By default, you will have those as the minimum and the maximum.
But you can manually set Until 11 or 12, I think.
Still, Xcode supports them.
**Bryce Buchanan** 13:59 Oh, that's.
**nacho** 13:59 Okay.
**Bryce Buchanan** 14:00 That's interesting.
**Ariel Demarco** 14:01 Yeah, they tend to deprecate it as time goes by in the App Store, and that's the final decision, basically.
Not the ID.
I don't remember the last news around, which was… the latest text code going to support, and which was the iOS version?
**nacho** 14:26 Yeah, because Swift 6 comes with Xcode 16, right?
**Ariel Demarco** 14:31 Yeah.
As far as in your homework.
**nacho** 14:35 But we…
**Bryce Buchanan** 14:37 So our users would need Xcode 16 to build.
**nacho** 14:41 And support here iOS 15, it says, regarding this.
Oh, oh, there is… no, that…
**Bryce Buchanan** 14:50 Those are older.
**nacho** 14:51 is 5.10, yeah.
**Bryce Buchanan** 14:53 Yeah, so… so, since all of the latest supported X codes support Swift 6, then we could potentially… I guess the problem comes in, with, using a Swift 6 library when you're running Swift 5, like, you haven't upgraded your own project.
**Ariel Demarco** 15:13 Yep.
**nacho** 15:14 I mean, you can use that, but you must use a compiler that supports Five sticks.
Oh, you can mix… You can mix libraries with Sweep 5 and Swift 6.
**Bryce Buchanan** 15:24 You can?
**nacho** 15:25 Yeah, you can…
**Bryce Buchanan** 15:26 I thought that was the problem that we have, why we can't upgrade to the latest version of, Oh, I guess, I guess it's because of the APIs that it uses, the latest version of, like, Swift Neo, or whatever.
I can't remember what the… what package it is.
That's… that's out of date that we're using.
**nacho** 15:46 Yeah, could be, yeah. There was some, is some… yeah, they were needing SHIP 6, I think.
And we were not going there because it will force our minimum version to be iOS 15 because of Xcode 16.
Who's this?
Yeah, we are always around the same topics.
But… Yeah, then… I don't know, maybe we can… Mmm… We can try to go there, and see…
**Ariel Demarco** 16:23 out.
**nacho** 16:24 changes are needed. But also, there is a problem supporting Xcode 15, for example, for us as developers.
Because it's not easy to get one of those running in a new laptop.
**Bryce Buchanan** 16:38 Yeah.
I mean, I don't… yeah, I don't even think I can, Yeah, because I'm on… I'm on Sequoia.
So…
**nacho** 16:53 Yeah, you can only install Xcode 26, probably.
**Bryce Buchanan** 16:56 Yeah.
Yeah, yeah.
**Ariel Demarco** 17:03 One, one weekend.
for the App Store, like, not… not for Swift on the backend, but for the App Store, you… for apps to be uploaded to the App Store Connect must be built with Xcode 16.
**Bryce Buchanan** 17:18 Okay.
**Ariel Demarco** 17:19 So, so that minimum supported version is 15, so we can probably bump that now, right?
**nacho** 17:23 Yeah, and that means that everyone will support Shrift 6.0 as a compiler.
So they can mix, even if they are using… if they are up using… Sweet 5, they could… link with us.
**Ariel Demarco** 17:39 Will that be a separate package?
Having two packages, one that is let's say, old, and the other is for Swift 6 support.
That has iOS 15 and all that stuff.
**Bryce Buchanan** 17:51 I think that, since the App Store only supports Swift Xcode 16, and as long as you can still have a project that runs an older version of Swift, but can link with a Swift 6, library, like, if we push our Swift 6 upgrade?
and it still works, linking with a Swift 5 project, then I think it's fine.
**Ariel Demarco** 18:20 Okay, because one doubt I had is at Embrace, we use Xcode 26 and 26.1 to build.
We still support, for some reason, iOS 13, tvOS 13, and all that stuff.
And everything works fine, and there's no rejection on the App Store. So, I think those are the minimum requirements in order to build, not to support.
Like, that's the SDK you have to use to build.
**Bryce Buchanan** 18:52 That's interesting, because this says that the deployment targets on these versions are 15 and above, or iOS 15 and above.
**Ariel Demarco** 19:01 Yeah.
it's basically why I mentioned before that even though you can… if you go and open Xcode.
I can share a sec on my screen to show.
Something… what I'm referring to.
**Bryce Buchanan** 19:17 Sure.
Billy, what… did you have something?
**Billy Zhou** 19:22 Yeah, just a quick question, I don't know if it entirely followed, but if we want to raise the minimum support of, from 12 to 15, at least partially, are there any concerns about dropping… Is that the… is that… wait, first of all, is that part of the, decision being made right now?
**Bryce Buchanan** 19:45 Yeah, it's part of it, I think. Okay. Is there any concern about removing support for, like, 12, 13, 14?
**Billy Zhou** 19:52 like, yeah, we've kind of had this discussion too, like, I don't… haven't really seen many people, like, want to use those versions, and… Yeah, I think the Apple published metrics, it's like 95 plus percent, it's like iOS 16 right now, and… At least for, like, people that are still using the App Store, so… Is there any concern there, or.
**Bryce Buchanan** 20:14 Yeah, I think the issue is not necessarily the adoption of the versions, but it's the developers, what they're targeting, right? And so developers like to have, like, the maximum spread.
And so, basically, we need to make sure that our library supports the maximum available spread of deployment targets. And so, like, I think… Ariel, Ari, I think that, You can put in whatever number you want, but if… like, I don't know what happens when you try to upload something, if, like, Apple will pin it to iOS 15, or what.
**Ariel Demarco** 20:56 At Embrace, we don't… we basically don't bump, because there are customers pushing apps with those versions.
**Bryce Buchanan** 21:02 But are they… are they actually pushing apps with those versions, is what I'm…
**Ariel Demarco** 21:06 Yeah, yeah, yeah. Yeah, because I check the versions on the actual sessions. I can go and gather data.
**nacho** 21:14 So that… that's great news. I mean… You have shown here that… We can definitely… Go with SHIF6.
Because it will build, in Xcode 16 or 26, as you saw, and they can target older versions. The only thing is… If it uses some… previous stuff.
There are some… there are some classes, like, for example, the Mutex.
that's used for concurrency and other staffs that… comes with the iOS version?
Or the… but…
**Ariel Demarco** 21:51 Yes.
**nacho** 21:52 Yeah, so if the target still shows 13 and it I think we can go with that, yeah. I didn't expect that thing you did, to work hard, to be honest.
**Ariel Demarco** 22:06 It's extremely weird, but the thing is… as Apple packages.
allow you to still build whatever version you want. Xcode allows you to build with those versions, but by default, it… for newcomers, it basically recommends using 15 and upwards, which, for me, makes sense. Like, imagine newcomers will start by using SwiftUI, So, you probably want to use SwiftUI 2, that starts on IS15, all that stuff that is understandable.
But yeah, I think we can go with…
**nacho** 22:38 Drip-seek, definitely.
**Bryce Buchanan** 22:40 And we can start with Corey, if that builds, and go… and start from there, yeah.
**Ariel Demarco** 22:46 You did a branch for it, Billy?
**Billy Zhou** 22:51 For Slip 6.
**Ariel Demarco** 22:53 Yeah.
**Billy Zhou** 22:54 It's just on my fork right now, but I can push it to, main as well.
**Ariel Demarco** 22:59 Okay, cool.
**Billy Zhou** 23:01 PR.
**Ariel Demarco** 23:02 in terms of having multiple packages or one, shall we have multiple? Because if at some point, I don't know, we want to bump.
versions of iOS or stuff like that, based on… The Swift version, or stuff that we want to do.
might be worth it? I don't know. That's… that's one of the things that I'm still investigating on the brace.
On my side, if we have to have multiple Swift packages or not.
Or if it's worth.
Really.
**nacho** 23:40 I think the problem is maintenance, right?
**Ariel Demarco** 23:42 Yeah.
**Bryce Buchanan** 23:42 Yeah.
**Ariel Demarco** 23:43 Which is a bummer.
If we can do it all in once, and doesn't affect anybody, that would be awesome, and that's great.
By the way, Billy, if you want, I can test… whenever you have something that you… you feel comfortable, I can test that out on… On the brace.
**Billy Zhou** 24:05 Yeah, they both, build right now, and yeah, so you can use it. Just be careful with the main one. I think there's, an issue if you build it without using Swift Core with Swift 6. I don't know if it works as a standalone, I didn't root cause why. Just, be careful about that. Yeah.
**Ariel Demarco** 24:25 Okay. I'll… yeah, I'll do it just.
To test.
**Billy Zhou** 24:30 Yeah.
**Bryce Buchanan** 24:32 So, I'm, I'm, I'm looking at, like, what I can actually download in terms of, like, targets for… in Xcode, like, which… which SDKs, and it only goes back to… like, I can only access back to, iOS 15.
So, I think… I think that we need to have a conversation about what versions, like, what our… what our plan is in terms of supporting, like, really old versions of iOS. I know that, yeah, you can throw whatever deployment target you want in there, but at some point, we're gonna have to bring these versions up just to get access to modern features.
And, Yeah, I think that we just need to sort that out. If there are people running really old, like, building really old deployment targets, maybe we can just say that they need to target an older version of the, of the SDK or something.
Because this, like, I don't think it's tenable going forward like this, especially when Apple's docs say that they only support back to 15.
So… I don't think that we should be trying to support older versions than what Apple supports.
**nacho** 25:52 So, in your branch, Billy, you have just set, Swift Tools version to 6.0, and no iOS changes, right?
**Billy Zhou** 26:03 And what was the last bit? And I'll try to edit and tear you?
**nacho** 26:05 Alright, you only changed the… the… the…
**Billy Zhou** 26:11 Yeah, it's iOS 12.
**nacho** 26:12 the Swiss Tools version, right?
**Billy Zhou** 26:14 Yeah.
**nacho** 26:14 The platforms, you didn't touch them.
**Billy Zhou** 26:17 No, I didn't touch them, but, I mean, I also obviously only tested on the latest iOS versions, so I'm not sure.
**nacho** 26:24 Okay, but it wins, right?
**Billy Zhou** 26:26 Yeah, it builds in all the test paths. Yeah, what we need is more manual testing.
**nacho** 26:32 Okay, yeah, definitely. I can run the automated tests we have on…
**Ariel Demarco** 26:37 older versions.
Have that repair, so… That may heal.
**nacho** 26:42 Oh, and I see you have… unsafe flags?
In settings… I, I was reviewing now a bit.
In your… in the Swift Core one?
I don't think… Unsafe flags are… Are acceptable for building a numbered version?
Is that still the issue? I remember that, in the past.
That using unsafe flags didn't allow you to create numbered versions.
Because I see you are with… You're testing that with… Oh, but it's in a test target yet, right?
Okay.
**Ariel Demarco** 27:35 Yep. Seems that both… Open Energy ABI and test, and SDK test are the ones… with that…
**nacho** 27:44 Okay.
**Bryce Buchanan** 27:48 Okay.
**Ariel Demarco** 27:51 I know what they are.
**Bryce Buchanan** 28:02 Are we… are we good?
To move on?
Are we looking at something?
**nacho** 28:07 Yeah, yeah, yeah, we are good to go, to move on. Yeah, I will, I will review.
the PR, also.
**Bryce Buchanan** 28:13 Okay, cool.
**nacho** 28:14 Just to… to check.
But yeah, it looks… it looks very good.
Definitely, you have done a lot of work here.
**Bryce Buchanan** 28:23 Yeah, it's really appreciated, Billy, thank you.
**Billy Zhou** 28:27 It wasn't that bad, actually. I think migration work has gotten significantly easier in the last year, yeah.
**Bryce Buchanan** 28:32 Nice.
Well, are you going to 6.2, or are you just doing 6.0?
**Billy Zhou** 28:38 I mean, we can do 6.2 if you want.
**Bryce Buchanan** 28:41 No, I'm just… I'm just teasing, it's okay. Yeah.
**nacho** 28:44 Yeah, no, I… yeah.
In a framework ourselves, I don't think it makes so much difference.
Because of the default, non-insulated stuff, but yeah.
**Bryce Buchanan** 29:01 Okay, who's, who put this on here?
**Ariel Demarco** 29:04 I did.
**Bryce Buchanan** 29:06 Okay, huh.
**Ariel Demarco** 29:07 So…
**Bryce Buchanan** 29:08 I'll pop it down then. Is that… is that… oh, my bad? Yeah. Yeah, it's a new topic, yeah, yeah, my bad.
**Ariel Demarco** 29:14 So this is an old one, Nacho did a PR a long time ago, I think it was kind of a year ago.
we had the same issue, same crash, on our SDK.
And while trying to implement the solution, I found out that it still crashed, and went to the original issue here, and see that the one that reported the issue said it keeps crashing. I found out a way to solve it, just… Just saying, I'm going to basically modify this, but I had a question related to the code, and maybe Nacho or Bryce, do you remember?
**Bryce Buchanan** 29:53 Do you… do you have a… do you have it, do you want to share it, or…
**Ariel Demarco** 29:57 You mean the, the fix?
**Bryce Buchanan** 29:59 No, no, well, I mean, the… I guess the portion of the code that you had a question about, but…
**Ariel Demarco** 30:03 Let me, let me find out.
This is a bunt telemetric here.
Yeah.
Thank you.
Sorry, I'm slow.
**Bryce Buchanan** 30:18 No problem.
**Ariel Demarco** 30:21 Can you see my screen?
**Bryce Buchanan** 30:22 Yep.
**Ariel Demarco** 30:23 Let me stash, the changes.
Per second?
Okay, so if we go to URL… URL session instrumentation.
And we basically tried to find, his background.
We have.
**nacho** 30:49 Okay.
**Ariel Demarco** 30:50 This… this thing that basically gets this background.
And checks for the task-based priority.
Yeah. And in that case, returns. Do you remember why we did that, Nacho?
**nacho** 31:04 Yes. Yes.
Because it was the… Only way I phoned them When it implemented, to know that it was, it was a background task.
**Ariel Demarco** 31:21 Okay.
Cool.
And this one is set here.
what I… what I was, concerned about is why we use this… I'm not… this.
Like, not equal.
Because as far as I remember, when you initialized your session.
You can use background, and that is the one that has My edifier.
So, if the identifier isn't nil, maybe you want to mark that as background.
that session.
Which… which helps in most cases.
But, my crash was on watchOS, and for some reason, watchOS, the URL session is not background, but still crashes, because.
**nacho** 32:16 Okay.
**Ariel Demarco** 32:17 That's our… as our market as background.
Which is completely… Weird.
**nacho** 32:22 Yeah. Yeah, I have seen net… crazy networking with WatchOS. Yeah, that's true. So… oh, so it was comparing with NIL instead of… you, you, you use… Not equal, right? You…
**Ariel Demarco** 32:37 Yeah, I… I changed… I will change this to not equal.
And at the same time, in this… Bart?
Where you check for if it's background.
**nacho** 32:50 Yeah, no, that's… that's… no, that… that… that's if it's… no, that's the background. The background is the… is the… identifier, and that task-based priority, that's for async method.
**Ariel Demarco** 33:03 If it's running asynchronously.
**nacho** 33:06 That's, that's the check for asynchronous.
**Ariel Demarco** 33:08 I see. Okay, cool. So, I will have to create another one that is… I will create an extension that is task is background.
else, returns, something like that.
**nacho** 33:22 But you already… I mean, so you already know its background because it has the associated object, right?
**Ariel Demarco** 33:29 Yeah, so maybe here.
for the watchOS cases, other…
**nacho** 33:38 And, and… Yeah, but thinking about the watchOS case, it's crashing because…
**Ariel Demarco** 33:44 It's crushing because you are trying to set… the crash is exactly the same message. It's, task delegate is not supported on background session task. You go and check the URL session.
it's a normal Euro session, like, I'm using your session shared in a simple test, and boom, crashes.
**nacho** 34:03 So is that… is then because it has an identifier in WatchOS?
**Ariel Demarco** 34:09 I really don't know. I understand why it could happen, but it's a bit mysterious.
Because the task, per se, it's marked as… it's marked as a class that is background, and that's basically the fix I'm going to… I'm going to do. I'm going to basically do an extension.
Of your session task?
That is… his background.
his background.
**Bryce Buchanan** 34:39 What version of watchOS are you running into this on?
**Ariel Demarco** 34:43 Good question, let me go and check it out.
It's… it's a…
**nacho** 34:47 Don't we have that in the tests?
**Ariel Demarco** 34:53 For this crash, I couldn't find any. I was doing one to reproduce the crash, and one to fix it.
**nacho** 34:59 Okay.
**Bryce Buchanan** 35:03 I would just check on a couple of different versions of watchOS, just to see if it's, like, like, the fact that it's making all URL sessions background tasks is kind of weird.
**Ariel Demarco** 35:17 Yeah.
**Bryce Buchanan** 35:18 I don't know if there's anything in the documentation around session delegates and watchOS stuff, so, I mean, maybe there might be something in there.
**Ariel Demarco** 35:27 like, if you go now and create a new, a new application, Apple Watch.
and you implement, in our case, our SDK, or OpenTelemetry, and you add the URL to the session implementation, that will crash.
just creating any sort of request, like your session shared, That's going to crash.
That's the way I reproduced it in first.
**Bryce Buchanan** 35:55 I'm just surprised that we haven't seen this before, if it's, like, an inherent… you know, feature of WatchOS.
**Ariel Demarco** 36:05 I don't know how much people is using OpenTelemetry on WatchOS.
**Bryce Buchanan** 36:09 That's fair.
**nacho** 36:10 Yeah, but we… we ran testing watchOS, right? But now… but it was not set in delegates then.
**Ariel Demarco** 36:19 I'm… And probably, I don't know the… if the tests are checking for a sync, but basically, background tasks don't allow… be a sync, nor have completion handlers.
Because of the way background tasks work under the hood.
**nacho** 36:38 Then why are we checking for a sync?
When it's a background.
**Ariel Demarco** 36:44 That's… that's the doubt I had.
**nacho** 36:47 So maybe that's the issue?
**Ariel Demarco** 36:49 That is not a sync.
**nacho** 36:51 In what choice?
And that's why we are not returning?
**Ariel Demarco** 36:59 I really don't know.
**nacho** 37:02 I mean, that return is only… I mean, base priority, that's for catching async URL session methods.
But you say it cannot be a sync if it's a background.
**Ariel Demarco** 37:16 Yeah, it will crash previously to… to reach this point. If you try to initialize our URL session, Let me see, I think I had the crash message.
Somewhere.
Yeah, here.
Speed.
**Bryce Buchanan** 37:34 I think you're only sharing the, Xcode.
**Ariel Demarco** 37:36 Yeah, yeah, yeah, I'm changing.
**Bryce Buchanan** 37:38 Oh, there it is, oh, okay.
**Ariel Demarco** 37:40 This is a crash, you'll find out.
If you try to use a single weight.
You will have all of this and say.
NSG, recent completion handler blocks are not supported in background sessions, and basically what I was doing is not using a background… a background… a completion handler API. I was using a sync await, and went to understand what happened, and basically found out that… Neither a single weight tasks and completion handler are supported in… in background tasks.
Which is also weird So, it's… it's kind of a… kind of complicated bug, but just wanted to give a heads up that I'll probably do a fix for this.
**nacho** 38:30 Okay.
**Ariel Demarco** 38:31 Because it's… it's kind of weird. I'll try to use… to add unit tests using the URL session background, so we can actually check this on every platform.
**Bryce Buchanan** 38:43 Cool.
**nacho** 38:44 Yeah. Yeah, great. Thanks.
Yeah, that's social. The same issue once and again.
**Ariel Demarco** 38:54 That's… Whenever you have to deal with those background stuff, that's not easy.
Everything, like, everything, it's weird.
Apple manages its… You know, really.
**nacho** 39:08 Yeah. Yeah, an Apple Watch has always… been a problem.
With network stuff. They have a very sim… probably they simplified network stack a lot… a lot.
To avoid, memory consumption, and, and yeah, it's… Extremely, extremely… Yeah.
Limited.
**Ariel Demarco** 39:33 I think the main reason is to have identifiers, and they reused all the background system. That's, for me, the reason why everything by default is background, because you can check on Apple Watch extensions, you can check for those identifiers when finished and all that stuff. So I think that's… that's the under-the-hood reason that Generates these kind of weird issues.
**Bryce Buchanan** 40:02 Yeah, that makes sense.
Okie dokie.
Thanks for that, Ari.
Are there any other topics that, we'd like to discuss today?
Huh?
Huh?
Cool.
I think that we can, wrap it up here then.
Alright, everybody, have a great rest of your week. See you next week.
**nacho** 40:28 Nope.
**Ariel Demarco** 40:29 The odds.
**Bryce Buchanan** 40:30 But…
**nacho** 40:30 Right?
