SIG: .NET SIG
Date: 2025-10-07
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 02:29 Hello, everyone.
**Matthew Hensley** 02:40 Hello.
**Martin Costello** 03:08 Can you hear me?
**Matthew Hensley** 03:11 Yes.
**Martin Costello** 03:14 Cool, I've… Fixed it.
**Rajkumar Rangaraj** 03:21 Cool, just want to check if any of you want to drive today, like…
**Martin Costello** 03:34 I mean, I could try, but the only things I was gonna suggest was just a rehash of what we talked about last week.
**Rajkumar Rangaraj** 03:42 What was that?
**Martin Costello** 03:44 the… Doing the new releases and the collector issue.
**Rajkumar Rangaraj** 03:51 Okay, I even have an important thing to discuss even before that. The .NET 10 PR, which is yours. That's a very important topic I want to drive.
So even before the .NET gets the…
stable release.net becomes stable, we have to sort this challenge out and have the RC released for the customers to try it out and provide feedback.
**Martin Costello** 04:20 Yeah, I think there's the thing that makes it tricky, is we've also got this issue with the collector, and we've also got changing the dependency versions, which ideally would go out before adding a new version on, because otherwise you'll ship it with the old version's rules, and then change it again.
**Rajkumar Rangaraj** 04:42 Okay.
By any chance you want to drive, Martin, like, you want to share your screen and start driving it, like…
**Martin Costello** 04:50 I can try. I'm very rusty with Zoom.
Can you see GitHub?
**Rajkumar Rangaraj** 05:11 Yeah, I can see the GitHub page, yes.
**Martin Costello** 05:14 Did you want to look at those issues specifically first?
**Rajkumar Rangaraj** 05:17 Yeah, let's go one by one, yes.
**Martin Costello** 05:20 Sorry, I was… I wasn't expecting to do this, so I need to rearrange my monitor so I can see multiple things at the same time.
So, what did you want to discuss specifically about the .NET 10PR? Because…
**Rajkumar Rangaraj** 05:40 You're in the contrary report, probably. I would recommend you to go to the…
**Martin Costello** 05:44 Sorry.
**Rajkumar Rangaraj** 05:53 So the one above that, the comment which I matched the runtime version, is what I was saying.
**Martin Costello** 06:02 You wanna look at that one first?
**Rajkumar Rangaraj** 06:04 Yeah, or the OTLP, anything is fine.
**Martin Costello** 06:10 So, I… let's do the OTLP one last, because I think that's got more conversation relevant to it.
**Rajkumar Rangaraj** 06:17 This one, I see it as a kind of a breaking change. We have done this in the past few times, so I was under the impression when, before reviewing this PR, we are going to do it starting the 9-0, not… we are…
I never felt like that we are changing the existing behavior that was released with the previous versions of the package, because it has, like,
as I called it out, it has a transitive dependency, so even without customer taking any of those packages, dependency injection, abstraction, or something, they might be using the new APIs from it. We're just removing it is going to break their API. This is going to result in breaking change.
**Martin Costello** 07:02 I get that, but that's not what was written in the issue that I wrote up that we all agreed was correct.
**Rajkumar Rangaraj** 07:10 I, I feel like… so, maybe, excuse me for my…
**Martin Costello** 07:17 I…
**Rajkumar Rangaraj** 07:17 like, what I.
**Martin Costello** 07:18 I, I unders…
Yeah, I understand that this is a breaking change, but it's already breaking for the people who want the change to happen, and we can't make them both happy, and the users who are blocked are unblocked by this issue, and anyone affected by that change can upgrade out of the problem.
**Rajkumar Rangaraj** 07:39 I don't know that's the right thing to do, because we have a… we made a promise in the previous issue where the discussion has happened. You know there are two set of users. We said we did this release, and we are not going to switch back. That's a promise we have made to the other set of the users.
And in the next set of the… in the next release, we're going in and saying that, hey, I'm going to break you with the promise, whatever we have made you. That does not make sense to me.
If you go back, you will see in that bigger conversation, there is a lot of conversation on that thread. You will see that this has been released, and we are not going to break the customer once again by changing the behavior.
**Martin Costello** 08:22 But that's not been discussed at any point previously where I've put this…
**Rajkumar Rangaraj** 08:27 Not in your issue. Not in your issue, but your issue points to another issue. It's been discussed in that.
**Martin Costello** 08:33 Now, I understand there's other issues, but I wrote up the plan, and everyone reviewed it and said, this is correct, and this is what we're going to do. So this comment is just throwing all of that out.
**Rajkumar Rangaraj** 08:47 That's what, Martin, like, I did not pay that close attention when I removed it, like, when I looked at it, but the thing is that what I'm saying is, I'm not saying the direction what you're taking on this one is good.
So, my take is, what we do, what we are going to do, do it from 9 and 10 onwards, not… don't apply to the existing… the previous versions that stays there. Don't break the customer.
**Martin Costello** 09:14 I understand that, but that's not what we've already discussed, because otherwise I wouldn't have made the PR do what it does now. I would have done what we'd agreed, and we'd agreed what's in this issue.
**Rajkumar Rangaraj** 09:28 Now I have a disagreement. What do you want me to do?
I'm one of the maintainers here, and I have a disagreement with this plan. I understand we are.
**Martin Costello** 09:36 No, no, no, my issue is that I have done the work in good faith on something you agreed we were going to do, and now at the last minute it's changed. That's my.
**Rajkumar Rangaraj** 09:48 I did a closer review, like, I did not pay… the issue makes very well and everything, but when I did a closer attention and taking a look at how it's going to come and hit the customer, it's going to be a, like, I never realized that this is going to do a breaking change.
So, that I had to figure it out. We never called out also this is going to be a breaking change or anywhere over here, so I had to… when I did a very, very close prayer, and I was about to click on approve and merge, that's when I figured out it's going to break the customers.
**Martin Costello** 10:22 Okay, so…
If that's the way it's gotta be, then that's the way it's gotta be. However, that doesn't actually fix the problem for any of the users who've got an issue. All it does is go, we will very slowly, over the course of years, slowly undo the change, so that in the future, we've completely reversed the decision.
So, I don't think that'll make any of the users
who wanted to check this change actually be happy, because they can't… they can't do anything until they get onto 10. And I imagine a lot of those users aren't going to upgrade to .NET 10 until next year, when 8 goes out of support, because that's just the way users are.
**Rajkumar Rangaraj** 11:04 Let's do this, Martin. I will… let's do this one, actually.
Let's just go back to your peer.
Do you have a change log there?
**Martin Costello** 11:19 I don't think I'd done it yet, because I was avoiding the change conflicts.
And having to constantly update it until we got to the point we're going, right, we're gonna ship it.
**Rajkumar Rangaraj** 11:29 Okay, let's do something, actually. Anyways, we are going to release a beta version, so we have a time to revert back, in case people come and complain about it. I'm ready to take the risk with the beta version here.
So, you could go out and add a changelog with a breaking change, saying that this is a breaking change, and clearly explain what it is. And we will include that also in our release process, and take that to the releasing.md file, too.
Let's see how, we'll collect the feedback from the beta version and see how it goes, and we will take a call based on that.
**Martin Costello** 12:07 Okay.
That seems like a good.
**Rajkumar Rangaraj** 12:08 Once this, changelog, once you update the changelog, I'll go ahead and… I reviewed the other part of this PR. I did review it several times, to be honest, like, earlier and even now. Let's…
Garden Merge and see, how this can impact or benefit customers.
**Martin Costello** 12:30 Yeah, okay, yeah, I'll do… I'll do that tomorrow, because it's, late.
**Rajkumar Rangaraj** 12:33 Yeah, I know, yeah, not in a hurry. And just leave a, like, a sick discussion comment in your… or to my response, so in that way people will know what is the decision that we are taking.
**Martin Costello** 12:45 Okay.
That's fine. Yeah, because, yeah, I think otherwise, if we… if we do nothing and effectively have to take this, what is effectively an announcement, down and retract.
**Rajkumar Rangaraj** 12:55 I agree with you on that point. Like, at a certain point, we need to take some challenge. This is one of the challenges we can take as we are moving in the beta state, instead of directly jumping onto the stable version. So, this is a good one to try it out.
**Martin Costello** 13:09 In that case, regarding the .NET 10 PR,
Those changes will need me to update how all the versions
have been encoded into this PR.
So I'll need to rebaste this one.
So, I would suggest, if there's nothing otherwise wrong with the .NET 10PR, and you want to merge that and do a pre-release with those changes, then we should merge that one after I fix up the other one.
**Rajkumar Rangaraj** 13:40 So which one you want to go first?
**Martin Costello** 13:43 So, for ease, I think it would be easier to merge the… match the versions PR,
And then… because then I'm just adding a if.net 10 block.
And that will update all the versions, because otherwise, if this one goes in first, I have to rework.
the match.
PR.
**Rajkumar Rangaraj** 14:02 I also agree with you on that. So, the morning, once you had the changelog, I'll go ahead and merge that PR.
And then you can work on fixing this one, probably, and then we will work onto merging this one. And before that, we have the OTLP part. Let's see what's the take on that one.
**Martin Costello** 14:19 Yeah, and then, just last thing on the .NET 10PR,
We should be getting RC2 next Tuesday, I believe.
So,
I'll be aiming to update that, but it probably won't be as quick as usual, but if this is already merged by then…
Don't need… to be an update anyway, a separate… in a separate PR.
**Rajkumar Rangaraj** 14:42 Yep.
**Martin Costello** 14:44 So… For the OTLP issue… I've got two PRs open, where… let me just filter it down to me.
So, the first one is… oh, no, sorry, I want PRs, no issues.
That's why I couldn't find it.
So, the first one is, I had to look into the tests.
And it turns out that we do have integration tests that use the collector, But they…
they… before the adoption of Renovate, they just used whatever the latest version was. So…
They could have at any point in time been using the buggy version, but there would be no way to know
Because you would have just got whatever was in use as latest at the time.
So, since Renovate has been used, we've now pinned the collector image.
However, the version now pinned is the latest version, which doesn't contain the incompatibility that caused the origin… that was the original issue I found.
So, I… looked at the integration test, and I downgraded the collector temporarily to 133.
**Rajkumar Rangaraj** 15:58 And…
**Martin Costello** 15:59 They still didn't fail.
So the tests would pass, they didn't detect the issue.
In this PR, I've done a bunch of refactoring, just to the integration tests.
And now they find the issue if the collector is downgraded to 0.133.
So I… that part of the change is reverted, it's back up to 136.
And then while doing that, to get a better error message.
to prove that it was hitting the issue, I included
the changes for the issue I opened a few weeks ago, which was to include the response body.
If, exporting fails, So that change is included in this PR now, so if the…
Collectors downgraded to 133.
It… the upload fails, and you get the error message from the issue that was reported.
So that's all in that issue now, so…
**Rajkumar Rangaraj** 16:58 Okay.
**Martin Costello** 16:58 this should fix the integration test, so if the same problem happened again in a future version of the collector, and then we got to renovate PR to update to that version of the Collector, the test would fail.
**Rajkumar Rangaraj** 17:11 Makes sense, this one.
**Martin Costello** 17:14 So, I think this… this one, as far as I'm concerned, this is ready for review and merge, because then that…
puts Maine on a stable footing with regards to the tests.
**Rajkumar Rangaraj** 17:24 Sure, this is only test changes, right? Can you just switch.
**Martin Costello** 17:27 It's test changes plus a small change to log.
**Rajkumar Rangaraj** 17:32 The response body.
**Martin Costello** 17:34 If the export fails.
Otherwise, it's only test changes, but if necessary, I can split it into two, but I thought it made it easier to show the tests were actually finding the problem with the extended logging.
**Rajkumar Rangaraj** 17:53 Yeah, makes sense.
**Martin Costello** 17:56 And then once I'd done that.
Because in the original issue, it had been discussed the…
there's an incorrect interpretation usage of the Protobuf 3 spec for the histograms, so once I had the tests and I knew that they were working and finding the problem, I've attempted
to fix the problem, but I'm no expert in, protobuff stuff.
But this change builds on top of the PR that updates the tests, so it contains multiple changes at the moment, but I'll rebase it when the tests are merged.
And… Effectively, this changes one file.
And it changes it from using unpacked
to PACT, assuming I have understood the specification correctly.
**Rajkumar Rangaraj** 18:52 I'll take a look into this. I know I wrote this part of the code, so I know the spec.
and.
**Martin Costello** 18:59 I've run the benchmarks, all the results are in the description, and I also
put the packages from the PR into a personal app from mine.
And, through some Grafana load test data, and it looks like the histograms still work.
**Rajkumar Rangaraj** 19:15 Okay.
Like, when you ran it, were there any issues, or, like, the memory allocation increase, or anything that has happened in the benchmark?
**Martin Costello** 19:28 One of the benchmarks… there's an ever-slight regression in… I think it was runtime.
Let me check. But I don't know if it's with… like, if… for just GRPC,
All of the numbers are pretty much the same.
it's slightly more at the start, but then it gets less over time.
But, I do find it strange, though, maybe there's a problem with the benchmarks, that gRPC, it takes 4 seconds, but HTTP is 12 milliseconds to do the same amount of work.
So maybe there's something wrong with the benchmark, and it's failing internally, and it's just loads of exceptions making it go slow or something, but
But then for HTTP, I think it's ever so slightly slower.
I know, it's more… it's like a couple of milliseconds.
Slower.
If what it's doing is not correct, then that might have to be the case.
It could, of course, be that this can… how I've done it can be optimized.
**Rajkumar Rangaraj** 20:41 I'll take a look at it this afternoon, Martin, both the PRs. The other one is for what I looked at, I glanced this PR, but this requires a dedicated time to sit and
Go through it.
**Martin Costello** 20:56 Yeah, it was… because, yeah, this was the only one where I was wondering about
Whether or not the pre-release should happen before this, because…
On the one hand, it's not doing the right thing.
And it would make sense to ship the fix sooner, but on the other hand.
The collector and Grafana and Datadog have all made changes to undo the breakage for customers, so it went from being
Oh, just don't use that version.
To, oh, no, no, we've rolled it back, to, oh no, it's a problem, to, oh no, we've worked around it again.
So it's relative importance seems to keep changing week to week.
**Rajkumar Rangaraj** 21:40 Makes sense. So… Martin, if possible, if the other areas are all fixed, I would say we will just
hold on to this. Maybe we will do… pack this along with the beta version that we are doing, because it's only the one part of the… unless if there is a very huge impact from a business perspective, we don't have any workaround. It makes sense to do the release, because last week only we released it.
So it's a lot of maintenance burden going to add on for a lot many people. We have to need to take anything that we release from here to the Contrape repo, and we need to do all those releases. So it's going to add a lot of complexity, so it's going to be, like, two days of work.
So, unless and until, like, if it is… if it is fine to wait till, like, yeah, exactly for a month.
I would say we could pack it along with the changes that we do for .NET.
**Martin Costello** 22:37 Yeah, that makes sense, it's just, yeah, it just could be unforeseen, because…
it was a collector issue, but then it was a… but then there was a workaround, and there was a newer collector, and then there was an issue in Grafana, and we updated the relevant component, so then it wasn't a problem for Grafana metrics uploads. And then someone reported the problem with Datadog.
And then it was just a problem for about a week, and then eventually someone from Datadog left a…
comment on the issue, went, oh yeah, we've also made a change to roll back the problem, so…
it went from being a problem that affected everyone on Datadog to not being a problem in, like, the space of two days.
So, who knows what extra additional vendor might pop up in two days' time and go, oh yeah, this doesn't work for us either, but someone's only just reported it.
**Rajkumar Rangaraj** 23:29 So, what's your take on it? Like, I just want to take your inputs. How do you want to handle this?
**Martin Costello** 23:36 Well, my unselfish take on it is it's been a problem forever.
So, we've fixed it. Well, hopefully fixed it, and it will not be a problem in the future.
My selfish opinion is, well, we worked around the problem in Grafana, so it can wait.
**Rajkumar Rangaraj** 23:55 Yeah, there… I also feel it could wait. If there is another vendor figures this out, they will have… this is all documented everywhere else, even if they want us to fix.
We have, anyways, we have the previous tagged version. We can… on top of that, we can do a patched version release of this one.
We will have this code also merged, so in this way, like, we are not closing the loop, we will have the loop open for them to, like, to do a patched version for them, if needed.
**Martin Costello** 24:29 Okay, yeah, that's fine. I just thought it was worth the discussion, because on Wednesday, I think it was Wednesday… Wednesday last week, it was an issue affecting users of, like, a big vendor.
And then the day after, it wasn't.
**Rajkumar Rangaraj** 24:43 Yeah. Now, I called out, right, like, if it is last week itself when we discussed this, if .NET is the only one causing an issue, it needs to be definitely fixed. So, I was under the impression that it always needs to be fixed from a .NET, not on the… from the other side. For .NET, like, OTLP exporter, we… the services should not change.
So, it's apt to do a fix in our repo and release it, but as we have a, like, slightly a time, like, one month of time would be good, or even the next version of beta.
would cover this for them to at least test and see whether it works as expected. So in that way, we will give a confidence to the people also that's already been fixed.
**Martin Costello** 25:29 Yeah, okay, that's fine.
Those were the only items I would have put on the agenda had I… had I just copy-pasted, so…
Is there something else you want to talk about before the issues?
**Rajkumar Rangaraj** 25:43 Yeah, I just want to take a look at the other PR, so, like, can you just open the PR view of, like, all the open PR?
The first peer, this is something that you might see, even I…
the issue itself would have been created by me, I believe. I wanted, like, Blanche to review. Blanche…
Had a, like.
I had this, I pushed earlier when I was even not even an approver in this repo, to get this been done for the auto-instrumentation and everything.
So there was a reason why this was not… this… especially this environment variable was not supported in the .NET repo. I don't recall that, what was the reason and everything, and Blanche did a lot… many changes to the DI injection pipe… DI…
related stuff.
That even added more complexity to bring this. So, I looked at the code and everything. I strongly feel we have to reach out to Blanche to get an opinion. I don't see him in here, he's one of the approvers in our repo.
So probably, like, yeah, tagging the Blanche, and I'll also ping him offline to see, if he can take a look at it. Because I don't know the history. Either Alan or Blanche would be the one who knows the history on this one.
So, unless I have an opinion from them, I'll hold on to reviewing or merging this PR.
There is one more… similar way.
**Martin Costello** 27:24 This one?
Because it looks like you've requested changes.
**Rajkumar Rangaraj** 27:28 Yeah, this one is also…
Like, if someone uses a set environment variable in an… or an add environment variable in an…
console application. There are no challenges.
And if someone goes and uses the set environment variable only in the ASP.NET Core web-based application, that's when they will run into challenges. And if we go learn about how we should use an environment variable in a web application, the design…
pattern or the design guidance from the ASPNot Core, they never recommend to use the set environment variable on it. They always recommend to use the i configuration and add things to that and utilize that.
It's something I did the repro and updated in the previous issue that's been quoted here, so I don't feel it's an apt thing to… for us to make this change. I understand what, where the… why customer is creating this one, but…
I have a small recommendation, I don't see the customer is here, but still, I have a small recommendation. It's these kind of issues, this one and the previous one. There is a detailed discussion in the issue that's happening, so it's better, like, the contributors just continue the discussion there, so it will, like.
reduce a lot of their effort before they, convert that as a PR over here.
**Martin Costello** 28:53 Yeah, I think, to be fair on this one, when I reviewed it, it just looked like they were moving code we were already using.
Cause, like, we already do it here.
**Rajkumar Rangaraj** 29:01 Yeah.
**Martin Costello** 29:02 It's just been moved later, so it takes effect at the last possible moment, instead of upfront.
So that's why I didn't think there was any particular issue with it.
I guess, yeah, go back…
You leave a comment and ask them to go back to the issue to discuss it, because otherwise this is just going to sit here stuck indefinitely.
**Rajkumar Rangaraj** 29:29 Here, these are the other two PRs. It's good that we are having a discussion if someone can come and take a look at the recording and everything, that's why I just want to look at it.
Yeah, the… I saw the reset… the scale of exponential histogram, that's another thing I need to pay close attention and do the review. I see you already have your approval button. I'll go and check this one.
Follow.
**Martin Costello** 29:53 Yeah, Peter looked at it as well.
I just looked at the attached issue, and it seemed like
The change was doing what the suggestion in the, in the issue was…
And everything else is basically tests and changelog.
**Rajkumar Rangaraj** 30:11 Yep.
**Martin Costello** 30:17 there's a… there's a PR open from a contributor here that's trying to improve .
**Rajkumar Rangaraj** 30:22 Performance by using spines? Yeah, but…
**Martin Costello** 30:25 But, all the tests are broken.
**Rajkumar Rangaraj** 30:27 Yeah, the initial version which he had it in his repo was, nice, that's why I asked him to go ahead and do the contribution, but it has changed multifolder. So I don't even know… now we need a…
like, benchmark to figure out whatever the change he proposes really adds any value or anything before we change it. But unless, like, Paulo fixes it, I don't think we need to pay any attention to this one.
**Martin Costello** 30:56 Yeah, he did tag me and Peter on it, and he was just like, the tests don't work, what's wrong? And I haven't replied, but the answer is we'll debug it and find out.
**Rajkumar Rangaraj** 31:07 Yeah.
**Martin Costello** 31:11 There's also…
This… this one, I don't… I didn't have enough context on what to do about this one.
**Rajkumar Rangaraj** 31:19 I know, you just added me in the issue, or somewhere you tagged me. I did not get in, like, time to review that.
Today. Don, not sure, is this one or somewhere, like, you related…
**Martin Costello** 31:32 I think I might have tagged you on an issue earlier.
**Rajkumar Rangaraj** 31:35 Yeah.
**Martin Costello** 31:36 But, I know Matt's looked at this one, but this one seemed a bit of a scary change to me.
**Rajkumar Rangaraj** 31:43 She is.
**Martin Costello** 31:43 Stayed out of it.
**Rajkumar Rangaraj** 31:46 This is a… I kind of feel it's a perf issue, is introducing a perf issue within it. That's where we always…
pay close attention to, yeah, let's see how it goes. And there is one other PR which I want to get it merged sooner, that ZZip compression in the OTLP exporter.
That's the one other interesting thing that we need to have it for the exporter.
**Martin Costello** 32:14 I'm not sure what the latest on this is.
**Rajkumar Rangaraj** 32:18 Yeah, probably, like, it's not… it's not good to ask us, the contributor, to…
Fix the conflict, let's, let me… let… the ambulance.
We will review it.
**Martin Costello** 32:32 I just meant more in terms of reviewers, because I've reviewed it, and then there's a few comments from Alan and CJO, but there's otherwise no approval.
**Rajkumar Rangaraj** 32:40 Yeah, Alan and Sijo just taken, like, a very vague look, only from a specification perspective, and they commented saying that instead of, like, a string or something, it should be a enum, as per the spec. That's what they recommended, but nothing more in that. So, I think an in-depth review need to
Happened to ensure that, like, it's good to go and ready to use in the protection.
**Martin Costello** 33:10 Okay, let's go on. That one, is there any other ones?
That you wanted to discuss?
**Rajkumar Rangaraj** 33:15 No, that's all I have it.
**Martin Costello** 33:18 Okay, let's have a quick look at country…
So… there's… Renovate got set up.
Over there today, too. Peter helped me out with that one, because there needed to be some changes in the admin repo.
So it would work properly.
That's… Is Payouter driving the changes to the admin repo, or…
I think, yeah, he merged the PR that was needed. It needed to change the branch protection rules for Renovate.
**Rajkumar Rangaraj** 33:59 Okay.
**Martin Costello** 34:00 for the CLA, and that's been fixed.
**Rajkumar Rangaraj** 34:03 I don't remember seeing the admin peer, that's why I asked. Even Trask is also out.
**Martin Costello** 34:09 No, not sure.
Let me just… Okay, I can find the number for you, but I can't show you the,
the issue, because I don't have access,
Yeah, number 287.
**Rajkumar Rangaraj** 34:33 Okay.
You are not a part of that, or…
**Martin Costello** 34:40 No, I have no visibility on the admin repo.
**Rajkumar Rangaraj** 34:44 Yeah, I just get 4 hours. Like, only maintenance, then.
**Martin Costello** 34:49 Are there any of these PRs
You need to dis- you want to discuss now?
**Rajkumar Rangaraj** 34:54 No, I think, we are good, Duh, I believe.
Just one second, I'm also taking a…
Yeah, that's all… Martin.
Martin, I just want to have a question for you, like, I know you have been contributing for a very long time to both of these reports and everything.
he, like, I'm thinking it's the right time, at least for the contrary repo, you could be, like, moved to be a maintainer. I'll have a word with the other maintenance to check it, but just want to check your interest in that before I just go out and have a discussion with others, with Alan and Piotr.
**Martin Costello** 35:46 Oh, yeah, I'm sure, thanks. I'd be happy to help out with that, if that's something on offer. Sure.
**Rajkumar Rangaraj** 35:52 Yeah, thanks, Martin. I'll go ahead and have the discussion with Piotr and Alan, and I'll probably create a PR for that in this report.
**Martin Costello** 36:02 Okay, cool. Thanks, Rosh.
**Rajkumar Rangaraj** 36:08 Yeah, I think that's all we have with. Just want to go through the… everyone else and see if anyone else has any other questions, so we can…
**Raj Nishtala** 36:18 Hey, hey everyone.
I am, this is my first SIG meeting. It was an interesting discussion. I guess I got a brain dump of all the PRs and…
net app contrib.
So… I had, I put in a link in our document, Or…
is a slightly… it may be a better question in the auto-instrumentation SIG meeting, but I just…
I thought I'd, you know, bring it up.
Yeah, so… so… essentially, I just wanted some pointers on, it looks like, we don't… the…
Lambda layer doesn't support auto instrumentation for the .NET runtime.
if I'm reading this table correctly. I just wanted to understand if there's any work planned around it, or is it something that's even planned at the moment.
Yeah.
If that makes sense.
**Rajkumar Rangaraj** 37:28 Mmm… We may not… I have an answer for you here.
Okay. Because even from an auto-instrumentation perspective, also, I don't know. Like, you can join the SIG there, I'm also mentioning it there, but I don't even know whether…
They will have anything for you there.
**Raj Nishtala** 37:49 Like, if there's anything on the roadmap, or.
**Rajkumar Rangaraj** 37:52 As far as I know, the answer is no, but you can join the SIG to see,
there are certain challenges with that. With Lamb… OpenTelemetry Lambda, I don't know whether… how we can hook in the CLR profiler… we can hook up this startup hook. I don't know how CLR profiler can be hooked in there and everything.
So I don't have a good knowledge about the Lambda part yet to just comment on that. So, in the other SIG, if people, like, have done the basic research, the other maintenance, they may be able to provide you some information there.
**Raj Nishtala** 38:31 Okay, thank you. Yeah, I'll look up a few,
you know, I'll make sure I don't miss any of the issues myself, and I'll take a look at the… I'll take a look at it before the SIG meeting. But yeah, okay.
**Rajkumar Rangaraj** 38:46 But we never, as far as I remember, we never had such discussion in that thing, so it will be good to bring it in.
It's tomorrow at 9am Pacific.
**Raj Nishtala** 38:56 Got it. Okay, I'll plan to join that one. Thank you, thanks.
That's all I had, yeah.
**Rajkumar Rangaraj** 39:07 So, I see Matt is here. Matt, do you have anything?
Pure?
**Matthew Hensley** 39:11 Nothing this week.
**Rajkumar Rangaraj** 39:15 I think, Martin, I think then we could end the meeting.
Thank you for driving it.
**Martin Costello** 39:22 No problem. Good practice.
**Raj Nishtala** 39:27 Thank you, thanks.
**Rajkumar Rangaraj** 39:29 Thank you, guys. Bye.
**Martin Costello** 39:30 See you next time, everyone.
