SIG: .NET SIG
Date: 2025-09-30
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Rajkumar Rangaraj** 02:48 Hello, everybody.
**Martin Costello** 02:51 Hey.
**Rajkumar Rangaraj** 03:03 Helen pinged me, he will not be joining today's meeting.
I think we can get started. Already, I just came from another meeting slightly late here.
Let me share mine.
Need.
Are you able to see my screen now?
**Martin Costello** 03:29 Yep.
**Rajkumar Rangaraj** 03:31 So, I had the same topic to add, Martin, and thanks for bringing that, the first one, and the second one, we will go through it.
Before every, stable release, what we do is we just take a look at the, the API file to see, there are any unshipped API, and if it's in the proper way, and review change logs to go through it. So, we will do… that as a part of this week SIG.
And I'll also, as Piotr is a new maintainer, we, got him. I'll check with him if he wants to, go through the release process. I'll give him a chance to see, like, if he's interested to run this release also.
But what we can do is, in this plastic, as a first thing, we can go and see, any public API changes to any of the projects here, and based on that, we can have a green flag to do the release today.
on a other track, like the .NET team, the ASPNET team engaged me, saying that, when are we going to release the, at least the preview version of the ASP.NET Core library, because they've added a lot of 10… Enhancement to the, metrics, and they incorporated… they came and contributed all that to the, contribo.
So they wanted to see some release for the .NET even before the .NET 10 RTM, the stable release. So, once this is done, Martin, we could merge your PRs on the .NET, whatever you have as a proposal, And then we could do another… beta or RC release from that.
**Martin Costello** 05:26 Yeah, because it was… because I thought… I thought we sort of, like, we needed to do 3 releases.
Because the first issue I've linked to is, like, a one… I know you need to check that nothing else has gone in, but the first issue is a one-line Bug, so that could just be a patch.
**Rajkumar Rangaraj** 05:48 Yep.
**Martin Costello** 05:49 Then, there's the middle one, which is the… 8… .NET 8 uses 8.NET 9 uses 9.
Yeah.
**Rajkumar Rangaraj** 05:57 That's correct.
**Martin Costello** 05:58 And then once those two are done, then we could do the pre-release with Don at 10. Because, yeah, it just… because… Because we haven't done any releases yet, it's, like, getting to the point where there isn't… it feels like there's starting to not be enough time to have three distinct releases.
**Rajkumar Rangaraj** 06:20 Performed.
**Martin Costello** 06:20 NET 10 itself ships, because that's, like, about 6 weeks away now.
**Rajkumar Rangaraj** 06:24 Yeah, that's true, Martin. And I'm… I already reviewed this, and I'm completely in line with your proposal. So probably once we push out the current release as what we plan for today, we will work on this and merge it.
So, even before we jump and, get in there, I just want to, like, we will take a quick look and everything, as you called out. The thing is that whenever we do release things, we don't release a single component. All of the components from here goes through the release process.
So, so we have been, like, behind the open telemetry protocol, and what like, we know what's been added there, but we need to go through all the packages and look at the public API and everything here. Blanche, you have a lot of experience with the, repo, like, if I miss anything, please call that out.
So, these things you already called out, like, Martin, and it's already there, and at least we have a two important bug that's being fixed here.
Like, this is a… I can… even though it's a performance improvement, I can kind of see kind of the issue, what it… performance issue, what it brings, I think it's good to get fixed, and this is a very, very big one, for which I feel that we should do the release immediately, instead of holding back.
So this looks good, like, let's take a look at the… Unshipped.
So no… nothing changes to this one.
So, let's take a look at the API also. Do we have in… did we make any public API changes or anything? Sorry.
Here… So these are the two… Unshipped ones, which will… be gone. I don't think we have any problem with this. They are adding a… Link To the telemetry span, the… shim in there. So, I don't see any issues with this one.
Let's take a look at… The other ones also.
Nothing here…
**Mike "Blanch" Blanchard** 09:12 just… A tip, Raj.
**Rajkumar Rangaraj** 09:15 Typically, when we do this, like, public API review.
**Mike "Blanch" Blanchard** 09:19 If you just kick off… the release process, it opens that PR, and it gives you the diff where you can kind of see everything.
**Rajkumar Rangaraj** 09:28 Yeah, I completely missed that part, like, yeah, long time ago.
**Mike "Blanch" Blanchard** 09:32 What you're doing is fine, it's just a little bit easier to have the diff. Now, I don't know if the release process will still work. I saw… We did some changes to use the app, so I don't know if you've tested this.
It might all be broken.
**Rajkumar Rangaraj** 09:53 Let's take it and figure it out, Blanche. What am I doing? .
**Martin Costello** 10:01 Yeah, I was about to suggest myself that for the time after this, we could probably write a GitHub Actions workflow that just hoovers up all the changes from the files.
displays them.
**Rajkumar Rangaraj** 10:16 It's go.
**Mike "Blanch" Blanchard** 10:16 to build, Raj?
**Rajkumar Rangaraj** 10:18 Yeah, yeah, like…
**Mike "Blanch" Blanchard** 10:19 Should be in there, that's, like, at least…
**Rajkumar Rangaraj** 10:21 Yeah.
**Mike "Blanch" Blanchard** 10:27 There basically is one, Martin… in the nature of, like, what this release process will do is it will open a PR that… takes the… unshipped files and merges them into shipped, so you get a PR that has the diff, and you can see everything that's essentially, like, becoming public.
If it still works.
**Rajkumar Rangaraj** 11:18 I ran it mostly… Yeah, I think this is easier to go through. I should have done it in the… Before the meeting, a few minutes before.
**Mike "Blanch" Blanchard** 11:36 There's probably… if you go back to the releasing doc… There's, like, the release notes file… That usually is done, but you can kind of interact with the.
**Martin Costello** 11:55 The PR's been opened, that… it's just that one… those two APIs are the only changes.
**Rajkumar Rangaraj** 12:06 Yeah, this is a very safe one to go through.
And as far as apart from the… this is nice. Thanks a lot, Blanche, here.
And, the thing is that it's also good, like, we know we have the confidence here now, like, the kind of this running, this workflow running itself gives a confidence things should work and not give major challenges to us. Let's wait and see how it goes, touch one.
I think we should proceed with the release. I don't see any concerns with the public API, or any changes that we wanted to release.
**Mike "Blanch" Blanchard** 12:51 It looks pretty… They are very… yeah.
**Rajkumar Rangaraj** 12:55 Sorry, Blanche, you said something?
**Mike "Blanch" Blanchard** 12:58 I was just saying, it looks pretty small, seems reasonable.
**Rajkumar Rangaraj** 13:02 Yep.
there are some PRs still in the OTLP, exporter, for consideration. I think these things could wait.
Not a major thing, and we could get that covered in the next one.
Next changes also for OTLP is also going to be heavy. I see the… the compression is already kind of ready, and this one, we're trying… we need to try and incorporate all of this for the next changes. So I think we are good to kick.
this off.
So, as I said, like, I'll approve that, and then I'll see, like.
if, I'll give Pyotr a chance to see if he can drive, so he understands the… he's always been contributing and takes care, provides feedback, so in this way, he also knows how the entire workflow runs.
Martin, you got the second topic, even. I had, like… Wanted to get the discussion on this one, too.
**Martin Costello** 14:20 Yeah, it just… the… OpenTelem… so the OpenTelemetry Collector made a change.
that broke the .NET SDK.
So, we, Grafana, have now created two issues. There's one that's in the .NET SDK repo, which is, we should have better integration tests, and then there's another one that's been open against the OpenTelemetry collector itself, which is also, we should have better integration tests.
Or end-to-end tests, or whatever name you'd like to give them.
And, but what keeps going round in circles is the… OpenTelemetry collector maintainers keep asserting that it is not a bug on their end, it is a non-compliance with protobuf in the .NET SDK. My understanding, based on what I was told By some other people, and me reading the spec, it seemed to make sense to me.
That it wasn't… it's not an incompatibility.
it's… the SDK does something that the spec allows.
But isn't, like, the obvious default way to do it. But the hotel collector is still insisting it is a bug.
So it's just… what do we do about it, and what do we… what do we fix?
Sorry, bunch.
**Mike "Blanch" Blanchard** 15:50 Just curious, what's the… What's the break?
**Martin Costello** 15:54 So, the OpenTelemetry Collector refactored their protobuf implementation to use a custom implementation, a bit like the one .NET has, in that it has a custom implementation, it's not the same implementation.
And… It did… I don't understand all of the details for the Protobuff stuff, because I've never really written much code against Protobuff.
Is it… they made a change so that it no longer accepted Packed.
values of a certain kind that histograms use, and the net effect was, anyone using the .NET SDK sending, metrics using Protobuf.
to a hotel collector, all of their metric requests were rejected with a HTTP400.
So, basically, broke metrics.
But it's only affected the .NET SDK.
And… I found the issue… semi-coincidentally, by just using a Grafana project we have for doing acceptance tests for OpenTelemetry in a personal project of mine. I was just using something we've made in a personal project, and it stopped working when the new collector shipped.
And… I reported the bug with the collector.
And they insisted it wasn't an issue with Plector, but then they changed it to make the change they'd done work again anyway, and that shipped as 0.134.
And then… Subsequently, both Grafana and, I believe, Datadog have both shipped the OpenTelemetry Collector 133 with the bug in it to their prospective hosted backends, and they've broken a load of customers who use .NET.
And had to roll that back slash forwards.
To fix the brake.
So… We're trying to, like, say, like, yeah, it's not good that… Effectively, customers are finding these issues, because… We can argue about who needs to change what and who broke what. Well, not argue. Debate. We can debate that, but ultimately, all of these issues were found by end users. OpenTelemetry as an organization shipped broken changes to customers.
And we should not do that, as… well, we should try to not do that as much as we can. And that's where these issues have come from.
This specific issue is effectively a Datadog user reporting that they can't push .NET metrics to Datadog anymore.
And that's a duplicate of… another issue we already had that got linked to another issue, which is in a Grafana repo reporting the same bug.
**Mike "Blanch" Blanchard** 18:58 Yeah, makes sense.
**Rajkumar Rangaraj** 19:04 So, Martina, as you called out, the only way, right, we have seen this issue earlier also. You might have seen a minor version released from the .NET area.
So, the… integration test or the end-to-end test gap here is causing an issue. So, if we need to invest something in the OpenTelemetry .NET repo, I would say the investment should be on… what's your first priority? I would say that the priority is to have the integration test for this one, because every, one who uses… most of the people who uses the OpenTelemetry, would be using the OpenTelemetry protocol, so it's very important for us to ensure whatever the release, we do, we do it very confidently. So, only those kind of, like, building that infrastructure with the test is one going to give that confidence.
So… I, I, earlier also, I bought this topic, I, I, because we have some good integration tests in the auto-instrumentation repo.
So… but that need… if we need to bring that over here, we need to build a test framework like what we have in auto-instrumentation, but… But that can be done in a very simpler way, maybe we can flick…
**Martin Costello** 20:22 No rush.
**Rajkumar Rangaraj** 20:22 Leonard.
**Martin Costello** 20:25 Oh, it was me. Sorry, Raj, my internet connection just went unstable and I didn't hear the last 30 seconds of what you said.
**Rajkumar Rangaraj** 20:31 Oh, no worries. What I'm saying is we could take a part of the tests from the, like, auto-instrumentation repos. We do do validation and everything in that area.
So probably that way we can do a fast track on this, but I completely agree with you, Martin. Like, this is one of the very important things we need to… like, after the .NET time, like, if we all have bandwidth, like, we need to get together and see how we can Build the end-to-end test or the integration tests in this repo.
**Martin Costello** 21:05 Yeah, I think the unresolved bit of the question, which was what made me put it on the agenda today, is… So… If we were to add the test suite right now.
**Rajkumar Rangaraj** 21:18 With the latest version of everything, it would pass.
**Martin Costello** 21:22 Because the collector has made a change.
That has effectively reverted the brake.
That broke .NET metrics.
But the discussion with the OpenTelemetry collector repo suggests that we need to do something in the .NET SDK that isn't just an optimization, but is an actual fix.
But then, how urgent is that fix?
And what do we need in place to do it? Because… when I… on the understanding I thought this was an optimization, and they fixed the underlying problem, then it's not urgent, but if it's actually not respecting the protocol, then that seems to make it slightly more important and urgent.
**Rajkumar Rangaraj** 22:13 Yeah. If that is the case, like, we cannot wait for the, like, integration test. If it's going to break everything, we need to just go ahead and fix it. There is a different conversation. Piotr yesterday pinged me, and I asked him, so he… I think he is much engaged from the OpenTelemetry collector also, and he provided some information. I did not go through that, so I had to go through that and figure out whether it's causing the issue now or not.
I don't have that.
Visibility at this point.
**Martin Costello** 22:44 Cause, cause, yeah, I think… If it is definitely a bug in the .NET, SDK.
I feel that we still need the test, because it's quite a fundamental change.
**Rajkumar Rangaraj** 22:58 Yeah, yeah, the test is needed, but if you know that kind of test will take a lot of time to get that added, it's not going to be that super simple.
**Martin Costello** 23:11 I would say it depends in typical software fashion, because for argument's sake, if we were to copy The test suite that found the bug in the first place straight into the repo.
It would be minimal effort.
**Rajkumar Rangaraj** 23:28 That's true.
**Martin Costello** 23:29 But… It does have… it does look a bit… there's… there's a perception issue to it, because it looks like Grafana is forcing something that uses its products into upstream.
Which is not the cat… which is not what we're trying to do, but it… it does… it could look that way, because it is a Grafana… set of stuff.
**Rajkumar Rangaraj** 23:53 So, Martin, if you are going to cover the test, I'm super supportive and will help you and ensure the Proper review happens, and we can move that faster.
**Martin Costello** 24:05 Yeah, cause also, like, we're not… we're not tied to the fact that everyone should use the test product we made, which is called Oats. We're perfectly happy with the community coming up with an alternative solution, and that being, like, the way we want to go.
**Rajkumar Rangaraj** 24:24 Yeah. But it might be that…
**Martin Costello** 24:26 Copy-pasting what we've already come up with.
is a good V0.1.
safety nets.
**Rajkumar Rangaraj** 24:35 Yep.
And I also have another thought. If… NET is the only one which is breaking, and every other language works.
That also is a concern, that's something that we need to fix. We cannot deny saying that there is no issue from our side. So definitely, we can take a look at it, and Try and see how we can… like, fix that out.
**Martin Costello** 25:04 Yeah, it, like, it wouldn't surprise me if it might be that the other SDKs work, inverted commas, by accident.
Because another thing that's discussions that's been had on this issue in the collector is like, oh, why would we add tests for a non-compliant SDK? I was like, you wouldn't.
Why would you test for something that someone shouldn't do? You wouldn't do that. However, if you treat everything as a black box, and you just have Things you ship talk to each other.
That's what's important.
Like, if it… if they're doing weird things, but they work to each other, that's fine, because the end users aren't broken. And then if someone makes an optimization in the pursuit of correctness, or performance, or whatever, and it raises a problem.
Then you can have that discussion before it gets in the hands of end users.
**Rajkumar Rangaraj** 26:12 I, I agree, too.
Do you have a plan, Martin, to just start with the test coverage here?
**Martin Costello** 26:26 I hadn't yet, but I can, because… I've been… Because I didn't want to just be, hey, we should write some tests and go, boom, here's a Grafana thing.
I was… and before today's developments on the issue, where it's Potentially, possibly, it is a bug.
then it was like, well, we've got plenty of time, the problem's been fixed, it's not… it's not urgent.
So I was just sort of waiting for… Discussion to happen on what the tests should be.
But if it's now more urgent, and we should just be adding something… Then, that puts more weight to… we can just take something for now, and then improve on it later.
**Rajkumar Rangaraj** 27:12 True.
That makes sense.
Well, I think we have… Only two double X, and we covered it, and I don't think anything else is pending.
Apart from that?
Martin or Blanche, do you have any other things for discussion? If not, I think we can end the meeting.
**Martin Costello** 27:45 So, I'll assign the tests issue to myself.
**Rajkumar Rangaraj** 27:50 And I'll try and start that sometime in the next week.
**Martin Costello** 27:54 And… I've recent… recently, as in just before the meeting, I rebased the… one of the PR for the major versions change, and one of the tests is failing, so tomorrow I need to investigate that and fix the PR. It's probably something trivial, but something in the merge rebase is broken, so… That… I need to fix that tomorrow before it can be merged.
**Rajkumar Rangaraj** 28:27 Okay, then, I think we can end the meeting, then.
And follow up with the release today.
**Martin Costello** 28:34 Didn't it fate?
**Rajkumar Rangaraj** 28:35 Yeah, thank you, Martin. Thank you, Blanche. See you.
**Mike "Blanch" Blanchard** 28:38 Bye, guys.
