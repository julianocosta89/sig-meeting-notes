SIG: Swift SIG
Date: 2026-05-21
Duration: 59 minutes
============================================================

## Zoom Recording Transcript

**Vinod Vydier** 05:13 Hey, Bryce, good morning.
**Bryce Buchanan** 05:20 Oh, no, I'm muted. How are you?
**Vinod Vydier** 05:28 Please.
I'll be… I'll be right back.
Should we wait for one more minute, maybe? Yeah.
**Bryce Buchanan** 07:27 Yeah, I'm not sure if, Billy's here, that's good. I'm not sure if Nacho's coming or not, he didn't say he wouldn't be here.
**nacho** 08:42 Sorry, a bit late.
**Bryce Buchanan** 08:44 Oh, there you are. Pretty good. I just shared.
Okay, Billy needs to drop early.
I guess let's just jump right in, and we'll talk about the Swift 6 PR. I think I merged it yesterday? Did I merge it? Did it get merged? I proved it. I know I did that, at least.
**Billy Zhou** 09:06 Yeah, I think he merged it.
**nacho** 09:08 Yeah, you want to, yeah.
**Bryce Buchanan** 09:09 Right.
Cool, yeah, so that's finally done, and now we need to talk about the long list of, Dependencies that need to get updated, and how to handle that.
I don't know if you saw this, but in, in the Slack, or no, not the Slack, the, the, issues for updating GRPC to 2.0.
The, the… poster of that, or no, I guess not, but somebody… Immediately posted, like, it's like, oh, it looks like you guys just, migrated to Switch 6. Like, let's, let's, let's upgrade GRPC now.
**Vinod Vydier** 09:58 Was it the bot, or was it a real person?
**Bryce Buchanan** 10:04 I don't know why.
**nacho** 10:05 It was very fast, yeah.
**Bryce Buchanan** 10:07 It was… it was today, it wasn't, like, right after I merged the PR, but… Bo, so I was thinking about this, and I'm wondering, you know, like, you can build against Swift 6-compatible libraries using Swift 5.10, but… but if you're using gRPC on an older version, you haven't upgraded to Swift 6 yourself.
How… how would, us upgrading to gRPC 2.0 affect those sorts of users? That's what I'm a little concerned about.
Should we… Split the… should we do a split, package, and have one for, like, older versions of Swift, and one for newer, or will that even work?
I don't know, I was just thinking about this, a little concerned.
**Vinod Vydier** 11:02 Do they have to use the older version of the… Thank you.
**Billy Zhou** 11:06 Wait, could you say that again, Bryce?
**Bryce Buchanan** 11:08 Well, so, we were blocked by, by not supporting Swift 6.
we were blocked, from upgrading gRPC 2.0 because we didn't support Swift 6. We couldn't use the gRPC 2.0.
But, it is possible to link with… well, I guess maybe, is it not possible to link with libraries built with Swift 6, with older versions of Swift, or…
**nacho** 11:38 Yes, it… I mean, the new versions of Xcode should be able to link libraries of different with street 5, street 6, or whatever.
This would be a book.
**Billy Zhou** 11:51 Yeah, like, before, we were literally on Swift 5 minimum on the main package, but we were using 6 on the core. So it's, like, normal, I think what was weird was that, like, Yeah, there's some strange behavior. Let me think about… let me find my notes on something.
**Bryce Buchanan** 12:13 I don't… I don't remember why we couldn't upgrade to GRPC2. There's something weird going on with it.
But anyway, it boils down to, like, what if other… what if our users are on an older version of gRPC, can't upgrade because they haven't gone through the process, but then we upgrade to gRPC2, and that causes downstream problems for them?
**Billy Zhou** 12:40 Oh, that might cause issues, because if they're literally on a different major version of the package, For example, like, AWS Hotel Swift, like, I think we had this issue, too, with, like, some of this MIDI modules, like, a bunch of our internal users just couldn't build, because there's no way to resolve major dependency conflicts, I think.
**nacho** 13:03 Yeah, I think it also was related to minimum iOS.
versions or Marcos versions that gRPC2 supported, I think, also. I don't remember exactly, but I think to remember, it was also related to that, that the minimum target version.
Was, very new.
And that was limiting. I don't think it was 5.6 versus 5.5, because I think almost since the beginning.
it was related. I mean, it was possible to mix.
three, five, and fixed libraries while you… Didn't use sweep 6 things, right?
But… I think it was more related to that. So now that we are… have updated Xcode, and our minimum target also, I think, with PIP6, because we'll have to move to something like Xcode, 16? I don't know.
Probably also the minimum target person.
can also be now supported for eRPC 2.0.
Also, gRPC is the library that brings more third-party dependencies into the mix.
I don't know if it will bring even more, or it will bring some transient things that could be a problem.
**Billy Zhou** 14:25 Oh, I remember the strange behavior as well that might be relevant, maybe someone can look into this.
I remember, like, when I was doing the migration, and I was using Swiftly to change the actual version on my machine.
I noticed… I think that when I went down to Swift 5 with Swiftly, I literally couldn't build our package, even though our, the, hard-coded minimum version said Swift 5.9 or whatever. So, maybe there was, like, some, like.
lack of support in the first place, that, like, I mean, this might be really relevant to the situation, actually. I would double-check that, Because I remember I had it upgraded Swiftly 6.0 anyways, just to build.
So, maybe we never supported 5 anyways, actually. That would be a good thing to double-check, actually. That was the strange behavior for my notes, yeah, I remembered.
**Bryce Buchanan** 15:23 Okay, well… Just based off of these comments in this issue, it does seem like it had something to do with Swift 6.
But I guess we'll need to revisit it. But I'm wondering, like, Can we… I guess… We probably couldn't, because it's a totally different, like, interface, we probably couldn't, like, have a…
**nacho** 15:47 Oh, yeah.
**Bryce Buchanan** 15:48 Report for it.
**nacho** 15:49 him.
if it had some sweep 6 interface that was forced in the new API of eRPC, yeah, probably that was the reason then, because it's clearly, as you say, I mean, what you say there is clearly pointing to Swift 6, so maybe I just… I was just wrong, and it's because it has some… maybe a synchronous thing, or some Main actor or actors-related stuff that… You need to support?
But, yeah, probably… yeah, I… It has been… version 2.0 has been out for a long time now.
So, probably, probably we, we… We could try to move there, also.
**Bryce Buchanan** 16:38 okay. I think we should definitely revisit this. I'm just a little concerned about all of the moving parts in the dependency chain, and how that's gonna affect stuff.
You know, we'll see. We'll see.
**nacho** 16:54 Probably we'll need some API changes, for sure, every place where we are using it, but yeah.
**Bryce Buchanan** 17:00 Hinder.
Alright.
Billy, did you have anything else you wanted to talk about since you have to go soon?
**Billy Zhou** 17:08 No, no, that was it. Yeah, I'm just, yeah, if there's, anything, just let me know. I'm available on Slack.
**Bryce Buchanan** 17:16 Cool, right on. Alright, have a good one.
**Billy Zhou** 17:18 Thanks, guys.
**Bryce Buchanan** 17:26 Okay, let's… so, Ari had a chance to look at the SPM traits to see if we can reduce our download size. It looks like that's a no-go, unfortunately, at least for that solution.
But he posted a big thing in the Slack, and I'm not really sure… I haven't had a chance to read it all.
Let's see… That's that one.
**Vinod Vydier** 17:54 I think his suggestion is to have some sort of a XC framework, right? Which would be like a… It would be, like, binary with all… everything… Packaged up together.
So then you don't have to download dependencies.
But that is… that has its own challenges, too.
Because then you start drifting away.
To download the latest.
But yeah, we can… we can wait for Ari to come back for, next week.
**Bryce Buchanan** 18:36 Okay, it does look like we have the release merged, it just hasn't… It's really easy to get cleaned up. And then marked as released, so… 2.4.1 release… I'm joking.
**nacho** 19:02 Yeah, my main concern here, creating the final release, was if it has been Tested somewhere, like, that… At least build some links with Users of the previous one.
what's wrong.
**Bryce Buchanan** 19:17 2.1, or 2.4.1?
**nacho** 19:19 Yeah.
For example, in your project, did you try just 2-4-1, linking?
**Bryce Buchanan** 19:27 I haven't, I haven't yet. What is the concern? This isn't the Swift 6 one yet, though.
**nacho** 19:33 This is… this isn't the Swift one, no. This is a previous one, yeah, just fixing bugs. Yeah. But yeah, just… just thinking if… if it just…
**Bryce Buchanan** 19:42 Just to double-check to make sure it's still… yeah.
**nacho** 19:45 just to check it, it builds, right? And it doesn't cross and start, something like that.
Because we… we… that's something that we… Don't have in our releases.
something that validates, that I were built on… You know, we validate that core links in the main library, but we don't validate that main library just links with A user of that.
**Bryce Buchanan** 20:13 Right.
Alright, well, I can, I can do that after the meeting, and oops.
And, I'll clean this up and set it to available once it's… once that's done.
**nacho** 20:32 Yeah, do you want me to clean that?
And we are just testing.
**Bryce Buchanan** 20:36 That's fine too, yeah.
**nacho** 20:37 And it's just to take some work from you.
Not making you just link.
And, and, and, and adults are those.
**Bryce Buchanan** 20:51 Yeah, I would appreciate that, thank you.
Let's see, so… Is there anything else from last week to talk about? It doesn't look like it, I think we covered everything.
**nacho** 21:04 Yeah, it was… the only topic was the one that, Ari has mentioned in the… about the trade.
Yeah, we talked about The two repositories being a nightmare.
And adding more work than we really wanted to have, and just talked about the possibility that with a new feature that comes with SPM, which is SPM Trades, if we could avoid that dependency hell that happens, but it looks like it… we cannot, because Ari checked out.
He said that it happens after the… After the library… other dependencies have been downloaded, so… Doesn't change much.
But I don't know if he has.
But he offered all other options, right?
**Vinod Vydier** 22:02 Yeah, is it a suggestion to go towards XC Framework? Because I thought we had some requests like that, and we didn't… We didn't decide the binary releases, right?
Let's see previous leaders.
**Bryce Buchanan** 22:16 Yeah, I mean, I think we provide one via CocoaPods.
**Vinod Vydier** 22:21 Okay.
**Bryce Buchanan** 22:23 Which, I don't know if… Cocopause has been updated. Maybe it has.
Can't keep track of all this.
I thought we had a Cocoa Pods job in here.
**Vinod Vydier** 22:40 Yeah, we do, I think CocoaPod itself is gonna go away, so… That was another… Thing that we discussed last week.
**Bryce Buchanan** 22:50 Is it in this one?
I don't get here.
I think that maybe we have to manually push it, maybe that's the thing.
Yeah, cause I don't see a… Maybe. Or this one, maybe?
Oh, that failed. Good. Oh, of course it's Cocopods having problems.
Oh, good.
Good stuff, good stuff.
Alright, well… I'm glad that we decided to add Cocoa Pots. It's been nothing but a pain in the butt.
Alright, well, let's see, what should we do next? Let's look at our pull requests.
So, we have a couple of drafts here that haven't been updated, I don't think…
**nacho** 24:15 Yeah, I think, Billy… added some changes to that case, but it's still, yeah.
It's still on undraft, yeah, maybe he can tell us next week.
**Bryce Buchanan** 24:30 Yeah.
**nacho** 24:31 The tracing bridge, I think it has not changed. That's the other library.
**Bryce Buchanan** 24:44 Oh, 4 days ago.
**nacho** 24:47 Yeah, but he didn't change to… maybe we can ask him if… Because… but it still has some conflicts, it says, but… So, yeah, we, we… he added… He, he used this, this new… I think that he also wrote for the Corps, but it's still a work in progress, so yeah.
**Bryce Buchanan** 25:11 Yeah, alright.
**nacho** 25:12 I don't know if we… We'll continue.
**Bryce Buchanan** 25:17 Yeah, maybe I'm just… And then a bunch of dependencies, there's this one as well.
**nacho** 25:41 Yeah, you approved that, or something like that, right?
**Bryce Buchanan** 25:44 Oh yeah, I thought it looked good, but it's… I realized it was still in draft.
Yep.
Yeah, oh yeah, that's right, okay, Yeah, this does look like it was… am I thinking of the right thing?
Vanessage… Oh, okay, yeah, okay, that's the lock handler, yep, yep, okay.
That's good, that's good, that's good. Spans… this just has issues on it.
**nacho** 26:12 I approve it, yeah, but it didn't.
Yeah, it's failing… Some test.
**Bryce Buchanan** 26:25 Oh yeah, so I saw this, and I wasn't… this is kind of weird. Asynchronous wait fail, exceeded timeout. This, I think… That this has to do with the runner that it's on.
**nacho** 26:40 Yeah, I think I re- I rerun that… Yo.
Yesterday, Or the day before, yeah.
Not sure, because I did that with my phone. I don't know if the app works well or not.
Yeah, let's…
**Bryce Buchanan** 27:02 Because I think there's… I remember, like, when they introduced the, the ARM hardware.
the, the iOS simulator like, was really poor performance on the ARM hardware.
And so I think that this might… Might have something to do with that.
**nacho** 27:28 Okay, yeah, I mean, the failure in the test is not related to this code.
**Bryce Buchanan** 27:33 Yeah.
**nacho** 27:33 which is only for WattsOS, to be honest. The final changes were only… Added to WatSource.
So yeah, it should, it should merit. I mean, it should, it should… Eventually… Work.
Yeah, it was our watch source only, change at the end.
So, yeah.
**Vinod Vydier** 28:28 The watch voices seems, like, green.
**nacho** 28:32 Yeah, so that's why there is no reason for iOS.
builder to fail. I don't know. Maybe it's just a flaky test, because it has to access the disk, something like that.
**Bryce Buchanan** 28:44 Yeah, yeah, I mean, it's like a timer thing, and yeah, and I've noticed with these, at least on GitHub, like, the… those timing… those performance tests can be just, like, wildly… inaccurate.
like, yeah, like, it'll be seconds outside of the expectation for some reason, but it has nothing to do with the actual… yeah, it's like, here we go. Here's the problem. Okay, so we're running on ARM hardware.
And it's gonna randomly choose one of these ones.
And… I think that… If it chooses the wrong one, it's gonna be really poor performance.
**nacho** 29:26 Okay.
**Bryce Buchanan** 29:27 If it chooses… I think if… I'm not sure… yeah, I think if it chooses the x8664 architecture, it has to emulate, you know, the hardware, and it just, like, is super slow.
So, I think we might need to revisit…
**nacho** 29:45 Yeah, the…
**Bryce Buchanan** 29:45 That the test target.
**nacho** 29:48 Yeah, the destination, right?
**Bryce Buchanan** 29:49 Yep, yeah.
So probably… Probably, Yeah, because this runs in the make, right?
**nacho** 30:07 Yep.
**Bryce Buchanan** 30:11 So I probably need to… I think I've tried this before, and it gets mad.
About this, but it probably needs to be something like… Something like that.
**Vinod Vydier** 30:24 Let's put the hardware.
**Bryce Buchanan** 30:27 But, yeah, I'm not sure if that'll actually work or not, because it's like, oh, you don't need to say what architecture it is.
But, anyway…
**nacho** 30:36 But that could probably happen with all the simulators, right?
Because all the simulators have the Intel version of…
**Bryce Buchanan** 30:44 I'm not sure, actually.
**nacho** 30:48 I mean, yeah, because they had to run on Intel.
on Intel hardware with Xcode.
**Bryce Buchanan** 30:56 Oops.
**nacho** 30:56 So all of them should have I mean, simulators existed for both platforms, always.
**Bryce Buchanan** 31:03 Yeah.
That's right, that is true.
**nacho** 31:08 So yeah, so maybe they failed randomly, but only… I think we are only making iOS depending one.
And macOS, I think. We are not… doing others, like… I mean… mandatory that all of them validates just iOS and MacOS, I think, just to avoid, yeah, flaky tests.
**Bryce Buchanan** 31:33 Okay, so let's see, so…
**nacho** 31:38 Yeah, it looks like it was running now with the arm.
a, ARM architecture. It said it was the first that much.
**Bryce Buchanan** 31:50 Oh yeah, oh yeah, you're right. Yeah, so TVOS has one… Yeah, so maybe they just randomly picked the right one.
**nacho** 32:01 Yeah. And if they fail, we don't notice, right? Because they are not mandatory to pass.
**Bryce Buchanan** 32:07 Yeah, yeah, fair enough. Alright.
So that's… That's something, Let me add… here we go.
Yeah, random.
I'm guessing it's ARM64, since we're running on the ARM64… hardware, but I'm not entirely sure.
**nacho** 33:30 Yeah, it must be that. I mean, in the… in its native architectures.
It must be.
It must be faster always.
**Bryce Buchanan** 33:48 Okay.
Alright, so that's all PRs for the main repo.
It looks like there's no big… Okay.
I'm gonna close that one.
Changes to the fabric to incorporate this change in spec.
Miss Ari's on that one.
No updates.
**nacho** 34:49 Yeah, that, that… Yes, that's right. Yeah, I messed that code that… I, I reviewed and messed up, yeah.
**Bryce Buchanan** 35:01 Pretty good.
**nacho** 35:03 So yeah, we could close that.
**Bryce Buchanan** 35:11 True.
There's actually a… Hmm, interesting. I didn't see that this was updated.
Hello?
It's really slow.
**nacho** 36:25 Yeah.
**Bryce Buchanan** 36:35 Alright, enough of that.
I guess we kind of need to do a little bit of cleanup in here. Looks like there's quite a few updates that have been made.
**nacho** 36:51 Yeah, they are very old market, don't they?
**Bryce Buchanan** 36:54 You know, let's go take a look at the switch core issue.
Our pull request, okay, I got that one, and then we got apply default view. Oh yeah, okay. So, I finally did take a look at this.
And, what he's saying appears to be correct.
I think that, yeah, it was just a, implementation mistake that I made when I, when I added this, but yeah, it should be using a, a fallback when… Okay.
So, I was thinking that the implementation was supposed to be such that, unless it was explicitly, like, set.
It would just…
**nacho** 37:42 Yeah, it should…
**Bryce Buchanan** 37:42 stuff, but it actually shouldn't, necessarily. And if, users want to ignore a specific metric, they need to specifically set up, like, a drop aggregator for that.
**nacho** 37:54 Okay.
**Bryce Buchanan** 37:54 Yeah, so this all looks fine. I think the issue is that there are some build problems again. Oops, not that one.
Oh, actually, this was a weird one. This was, like, Homebrew was pooping out for some reason, and I think it's because… Of some, dependency… Issues, like our… our… I wonder which one it was.
**nacho** 38:32 Oh, some of the… of the updates.
**Bryce Buchanan** 38:36 Yeah, there was, like, an update or something to the… I thought there was, at least. So we have our… Checkout action? No. Swiftland… Which job is it? It's the… Hmm… This one.
So maybe, maybe we actually… oh, is it this problem? Set it? No.
That's probably not it.
Yeah, there's something… For some reason, like, Yeah, I'm not… Hmm, hmm, hmm… I can't remember exactly what the issue is, but I thought that maybe updating… The dependencies might fix it.
At least that's what my investigation led me to believe, but yeah, so… Yeah, it's like… What?
Oops, that's not what I wanted to search.
Hmm… Yeah, so I'm not entirely sure what the cause of this is or why it's happening, but it seems like it only is happening for this PR for some reason.
And, why can't I… I can't rerun it.
**Vinod Vydier** 40:41 The opt home brew is in the… on the sound.
**Bryce Buchanan** 40:46 Bye.
**Vinod Vydier** 40:47 Simulate, or the test machine, right?
**Bryce Buchanan** 40:50 Yeah.
**Vinod Vydier** 40:52 It's not found, how… so how's that… how other tests are working, then, if it's not… so you're just trying to install…
**Bryce Buchanan** 41:00 I'm wondering if it was just… oh, maybe it might have just been an errant issue.
But for some reason, I can't restart it, and I don't know why. I guess, but…
**nacho** 41:10 That happened in the past with some other PRs, that you cannot rerun the checks. I don't know why.
**Bryce Buchanan** 41:17 Oh, interesting.
**nacho** 41:19 It's not the first time I see a PR that you cannot rerun, and you have to commit something. Maybe it's some policy in this project?
comes ahead in.
I don't know.
**Vinod Vydier** 41:31 So the Opt Homebrew, I also looked up, that could be the… Apple Silicon versus the Intel Mac, because Intel Mac's homebrew defaults to user local, as opposed to… Apple Silicon, which does Opt Homebrew, so if the script is using Opt Homebrew, and it's taking a…
**Bryce Buchanan** 41:53 Oh, is that? Okay.
**Vinod Vydier** 41:54 I mean, that is… Intel-based, and it…
**nacho** 41:58 Oh, okay.
**Vinod Vydier** 41:59 Yeah.
**Bryce Buchanan** 42:02 Interesting, okay.
All right.
**nacho** 42:05 Yeah, but this… this video about the tech not working, it has happened in the past.
And maybe it's also in 5th core.
I don't remember.
But… Yeah, not being able to rerun is…
**Bryce Buchanan** 42:25 Yeah, I don't know what that is. That's… yeah, that's weird and annoying. Okay, so you're saying that… like, there's… wait, so there's something wrong with… our test doesn't specifically call out the, that location in the brew, so… I'm not sure.
That's weird.
Are you saying, Vinod, that it was fixed in, like, GitHub? Like, it was a GitHub runner issue?
**Vinod Vydier** 43:04 Yeah, so if it runs on the… Intel.
Until the homebrew was… Intel-based Macs used to… Installed on the slash user slash local.
Whereas the… Apple Silicon ones use Optium Blue.
So the default location of Homebrew has changed.
**Bryce Buchanan** 43:34 I see.
**Vinod Vydier** 43:35 So, you know, our script is only using right?
So it's not able to find brew.
And, somehow it's… Thinking it should go to Opt Home Brew, and… There's some pictures.
**Bryce Buchanan** 44:01 It works fine on the other…
**Vinod Vydier** 44:04 So the fix is to reinstall homebrew.
**Bryce Buchanan** 44:07 Yeah.
**Vinod Vydier** 44:08 cold, yeah, yeah.
**Bryce Buchanan** 44:09 Yeah, that's… yeah, so I'm guessing it was, like, an issue on the runner, and so maybe it's been fixed since then, but we can't rerun this job, I don't know why, so that's really weird.
**nacho** 44:19 Could this… yeah, could be something in the settings, or something like that?
**Bryce Buchanan** 44:24 Because…
**nacho** 44:25 It has happened in the past, so… It must be something… that… Maybe we are doing with Open MSG… Coral? I don't know.
**Vinod Vydier** 44:41 Oh, so it's only on core.
**nacho** 44:43 Yeah, only… I mean, it doesn't happen in all PRs, just in… just in some of them, but maybe they are only in core.
That's my…
**Bryce Buchanan** 44:53 Oh, you know what it might be? I think I know what it might be.
Is it because… is it because it's a different repo? Is that why? We don't have the ability to rerun them?
**nacho** 45:08 But… You always create PS from another repo, right?
**Bryce Buchanan** 45:12 Yeah, that's true.
But maybe it's because it's not one of our repoots.
Maybe it's because… Yeah.
**nacho** 45:21 No, because I run, for example, I think I… you have been able to run the watch… the watchOS fix with URL session.
And it was not your repo, either.
**Bryce Buchanan** 45:33 Is it… is it because you had to approve the job, and maybe you own the jobs now? Is that why? Like… tubes.
to, you know, like, when somebody else has a PR, and it's like, you know, is it okay to run the tests with this PR?
**nacho** 45:52 I don't know, maybe I approve that. I'm gonna check.
**Bryce Buchanan** 45:55 Can you rerun it? Because it looks like you rerun it last time.
**nacho** 45:59 Okay, let me check then.
**Bryce Buchanan** 46:04 Maybe because you approved it initially?
**nacho** 46:09 the default view.
**Bryce Buchanan** 46:13 Yeah.
**nacho** 46:18 And checks were not successful.
No.
I don't… Let's see, I, They cannot return it either.
**Bryce Buchanan** 46:44 See, I can do this one.
**nacho** 46:46 It should be… Where it should be? Yeah, that's right. All jobs, I don't have that either.
I only have the latest builder.
**Bryce Buchanan** 47:03 Let's see, how about this one?
Weird. Alright, well, I'll do some offline digging as to why this is.
**nacho** 47:31 Yeah, maybe we have something in the repository with that, I don't know.
**Bryce Buchanan** 47:35 Yeah, I might have to… I'll… that's one of the places I need to… I need to figure out… I can't remember where all, like, the permissions and stuff are managed, what repository that is, so I have to go…
**nacho** 47:45 Yeah, they change it into town.
Wow.
**Bryce Buchanan** 47:57 Yeah, I don't.
**Vinod Vydier** 47:57 A lot of, lot of repositories, yeah.
**Bryce Buchanan** 48:00 Rich winning.
Oh, okay.
Well…
**Vinod Vydier** 48:08 Oh, it's crossed 100, huh?
**Bryce Buchanan** 48:13 Okay. I don't think there's anything else to look at in Swift Core. Dependency Dashboard, abandoned dependencies.
Detective… Okay.
is unmutained.
Well then.
We might need to take a look at this.
Hasn't been updated since 2020. I don't know, like, we use this, right? This is, a valuable…
**Vinod Vydier** 49:09 Damn, we do.
**Bryce Buchanan** 49:11 So I'm not sure if there's a replacement for this, so we might… might just ignore that.
**nacho** 49:18 Yeah.
**Vinod Vydier** 49:19 There is no official equivalent.
**Bryce Buchanan** 49:22 Damn.
Anyhow, I think we've looked at this one before, right? But… Yeah, yeah, so I think… What, what were… what were we saying about this one? That, I guess we probably should reply and just let them know that, you know, it's a process, and we're just getting on to Swift 6, and we're gonna be… making things… Actually, properly sendable, rather than unsafe sendable.
**nacho** 50:20 Yep.
Yeah, we'd be… also, we had… several constructions that… are not easy to move, like a static instance and singletons and things like that. Yeah.
**Bryce Buchanan** 50:37 Yep. Yep, yep, yep, yep, yep.
**nacho** 50:40 Yeah, trying to make that… Sendable, everything sendable properly is not gonna be… easy at all.
We provide uncheck and double salty.
They know when things are really sendable or not, but yeah. Making everything sendable is not… It doesn't make sense either.
Yeah. Because… I mean, you don't want to always move everything into dependent threads, right?
**Bryce Buchanan** 51:07 Yeah, that's true, yeah.
**nacho** 51:09 not always here. Also, at the beginning of the… strip sticks and double things. It was like… you thought that everything had to be an extract and be sendable, right? But… You know, where do you store the states?
Only with ACTOS and asynchronous access?
That doesn't work. Always. I mean, it's nice if you can do that, but yeah.
with medium-complex projects, that's not a solution, so yeah.
**Bryce Buchanan** 51:40 Hmm.
**nacho** 51:41 and he wanted to make everything And we'll send our con… Compliance.
Or confirm it.
**Bryce Buchanan** 51:52 Nacho, do you think you could reply to this and just let, like, kind of make the case why it's not gonna be possible to do everything like that?
**nacho** 52:03 Okay, yeah, I, I can, I can, I can, I can address that, yeah.
**Bryce Buchanan** 52:07 Thank you, thank you, Nashan.
There you are.
Internet's slow today. Maybe GitHub's slow, I don't know.
**Vinod Vydier** 52:19 GitHub as slow, I think, huh?
**Bryce Buchanan** 52:40 I guess I'll close this issue, because this is regarding the old, metric kit implementation, and now we have a new one, so… I'll just close that.
Alright, I think that's everything.
**Vinod Vydier** 52:58 Alright, so we have a… we have a Firefly's AI note-taker.
**Bryce Buchanan** 53:04 Yeah.
**Vinod Vydier** 53:05 Whoa.
**Bryce Buchanan** 53:05 That's been around for a little bit.
**Vinod Vydier** 53:07 Oh, is it? Okay, I didn't notice that.
**nacho** 53:09 So take care what you say, because someone is, yes, writing it down.
**Bryce Buchanan** 53:14 So…
**Vinod Vydier** 53:15 Okay.
**nacho** 53:16 You cannot talk about what you know, you… I'm gonna say keywords.
**Bryce Buchanan** 53:21 topic of safety, yeah.
**nacho** 53:23 Yeah.
Take care.
**Vinod Vydier** 53:25 Dude.
**Bryce Buchanan** 53:26 Have a good weekend, everybody.
**Vinod Vydier** 53:27 Yeah, have a good long weekend, okay?
**nacho** 53:29 I will finish the release notes after.
**Bryce Buchanan** 53:32 Okay, thank you. I'll double-check that it actually builds. Yeah.
**nacho** 53:37 That's right. Bye.
**Vinod Vydier** 53:40 Right.
