SIG: C/C++ SIG
Date: 2026-09-30
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nikhil Bhatia** 00:30 Hi, Mark.
**Marc Alff [MySQL]** 01:25 Let's wait a few moments for Duke to come.
Boom.
Do you have any special topic to discuss? Because the… You attended a couple of meetings, but you'd I haven't seen you asking so many questions. So I'm I'm wondering if there is something in particular.
**Nikhil Bhatia** 01:47 Yeah, today there is nothing in particular, but there was a contributor who raised a PR on an issue which was still… which still needed triage.
Okay. So, I think, the… it's… the PR is number 4647.
So that was, removing an enum from the public API.
So, I had added a comment over there. Yeah, yeah.
**Marc Alff [MySQL]** 02:23 4647?
**Nikhil Bhatia** 02:24 Yep.
**Marc Alff [MySQL]** 02:42 Okay.
I haven't looked at it yet, so I don't know the context, but I will.
**Nikhil Bhatia** 03:05 Yeah, so maybe today we can discuss on this issue.
**Marc Alff [MySQL]** 03:07 Sure.
**Nikhil Bhatia** 03:08 Yeah.
**Marc Alff [MySQL]** 03:09 Although the only thing I see is changing some comments, I don't even see a code change.
**Nikhil Bhatia** 03:16 Okay, so I think he had maybe changed the… Code after the comment, so…
**Marc Alff [MySQL]** 03:23 Okay.
Okay, so, could be it's resolved.
Oh, okay.
Hi, Doug.
**Douglas Barker** 03:56 Hey, Mark.
**Nikhil Bhatia** 03:59 had.
**Douglas Barker** 03:59 Hey Nikhil.
**Marc Alff [MySQL]** 04:05 Yeah, we're just discussing with Nikhil.
Just to discuss the PR in particular.
**Douglas Barker** 04:14 Sweet.
**Marc Alff [MySQL]** 04:28 I didn't have time to update the agenda. One thing I noticed Very quickly, that there is a new release of Porto, so we need to adjust, as usual.
And otherwise.
So, there is always the current discussions, but also I wanted to mention that, there is a lot of activity in CPP Contrib.
Which is unusual.
And, that activity is to, fix CI and get it up to date, with Renovate. So the… I want to discuss that also as well, if you have time.
**Douglas Barker** 05:11 Sounds good, yeah.
**Marc Alff [MySQL]** 05:14 Anything on your side?
**Douglas Barker** 05:20 There may be some, some issues Take a double check, but I haven't I haven't prepared anything either for this meeting yet.
**Marc Alff [MySQL]** 05:29 Okay.
Okay, well, I… Yeah, good.
**Douglas Barker** 05:40 Go ahead, Dan, I'll mute.
**Marc Alff [MySQL]** 05:44 Okay, I was about to suggest that we start with the PR that Nikhil mentioned.
and then we can look at everything else.
Why am I uncomfortable again?
Okay, so Nikhil, this… this is about this PR, right? This, timeout in… Yeah. The current code, I guess. Okay.
Just discovering the issue as we… as we go, so… Okay, so It's a bit long to look at all the text there, but in general.
Whether we fix, header files just depends on where it is. So it's in… if it's part of the API, it's, extremely rare, and we try not to.
If it's part of SDK or exporters, we may change things once in a while.
So I don't know… with… What case this is?
Bhutanese in… Seems that the verified change was removed anyway, because this county only contains some code changes for now.
Okay, so yeah, thanks for… For flagging this, I think we'll do that offline, because the… just reading the entire PR and all the… All the issues and all the discussion will take some research time.
**Nikhil Bhatia** 08:36 Yeah.
**Marc Alff [MySQL]** 08:46 So one thing you probably have noticed is that Tom Step down from being a maintainer is only an approver now, so it will continue to provide some valuable feedback on SDK and a lot of things in metrics that he knows very well.
of… But she's, no, no longer maintainer.
And Ehsan, who is a maintainer, took a… No.
was off for a moment, but he's back, actively looking at OpenTelemetry again.
**Nikhil Bhatia** 09:35 Yeah, I had seen that change of Tom.
**Marc Alff [MySQL]** 09:37 stepping.
**Nikhil Bhatia** 09:38 Down as a maintainer to approval.
**Marc Alff [MySQL]** 09:42 Yep.
Do you want to… To look at Cpp first and Cpp contrib after, or any preference.
**Douglas Barker** 09:56 Yeah, I think that makes sense.
**Marc Alff [MySQL]** 09:58 Okay.
So we'll start with Cpp, then.
As usual, the problem is here.
So the number of Prs is getting higher and higher.
There is a couple of cleanup that I can do that I haven't done yet. In particular, for these things, There is a very simple PR.
a while ago that was filed to… if I can find it… It's related to this, no.
So good at this.
Okay, so there is Vspr, which is some code change and cleanup in In the test code that we have for, Socket tools.
So, it's progressing, but… the virtual, So he's a first-time contributor, instead of… Making changes to this PR is instead finding another PR for a related code change.
This one, and this one. So, those two should be closed, in fact, and the fix should be added to the… The main PO.
So… Viva.
Tools that would, would be closed here.
And the main PR, it's some simple change, so it should be approved very soon, I guess.
Apart from that, we also have some, changes related to innovate and Ci.
I haven't looked at the Ubuntu things. The main issue there is to make sure that this builds.
And I think, I think that the failures which which remain here They may be related to CMake Because when using a more recent version of Ubuntu.
Of course, it comes with a more recent version of CMake, and in particular CMake 4 instead of CMake 3 something.
And I don't recall the details, but I've seen that earlier also. There is some… something that break with CMake 4.
So… We might have to do some maintenance in the CMake file themselves to be able to upgrade.
But I don't know the full extent of that.
**Douglas Barker** 12:34 Yeah, one issue I do know about because I ran into it when I updated the dev container when it was bumped to 2604 was the building of open tracing is certainly a problem because it.
**Marc Alff [MySQL]** 12:46 Yeah.
**Douglas Barker** 12:47 doesn't Have a, minimum version compatible with, or will fail automatically and configure for CMake 4.0.
**Marc Alff [MySQL]** 12:57 Oh, that's right. And I remember seeing that for something else. I don't remember the context, but yes, I've seen that.
And… the outcome was that, well, we should upgrade the CMake minimum required there.
Except that the code is in a repo which is read-only and archived.
So, it will never be changed.
So the question is then, how do we do that? Do we apply a patch on top of the repo, or do something special in our… In our code.
Okay. Before taking the code, and it's… yeah, that was something nasty there.
**Douglas Barker** 13:38 Am I remembering correct, Mark, that the open tracing integration is also deprecated by the…
**Marc Alff [MySQL]** 13:44 Yes, yes, I was going there.
No dependencies.
There are a couple of things which are deprecated, so Zikkin, some sampler, and OpenTracing there, and… I don't remember the timeline… But yeah, it so it will be removed from the spec.
Well, still in 6 months.
Okay. What I do not understand is, in terms of policy, whether we can also drop that at the same date.
Or if we still need to wait a bit longer after March.
Hmm.
But yes, given that this is deprecated. Maybe it's not very valuable to fix the make files there and have some Complicated things as record for code, which is going to disappear anyway.
**Douglas Barker** 14:50 Yeah, one idea I had was we can, update our main CI workflows, and then just disable building open tracing on the normal workflows, and only build it on the specific ones, which we could downgrade CMake or use a…
**Marc Alff [MySQL]** 15:06 Yes, yes.
**Douglas Barker** 15:07 CMake3 dot something.
**Marc Alff [MySQL]** 15:10 So, yeah, we can definitely downgrade, I mean… It's not so much downgrade CMake, it's run on a host which is using CMake version 3 something and not 4.
So if we run on an older version of Ubuntu, that should be okay for a while.
The part I haven't checked is that, at the same time, I'm assuming that.
And two workers are being phased out and upgraded in GitHub. So I don't know.
If we will have a worker old enough to have an old enough CMake for a while or not. But it's, yeah, worth… Looking at that, so that we don't… We don't have to fix the CMake minimum required.
**Douglas Barker** 15:56 Okay.
**Marc Alff [MySQL]** 15:59 And yeah, worst case, we can keep the code, but just disable the worker in CI.
This part is never changing anyway, so… I've I don't recall actually seeing some build break in Ci in that code base, because we never touch it, anyway.
**Douglas Barker** 16:19 And I didn't look at the, I don't know if Renovate already had a PR for this, but just curious if it was smart enough to upgrade like the 2204 runners to 2404 and 2404 to 2604.
**Marc Alff [MySQL]** 16:32 No, no, he didn't do that.
**Douglas Barker** 16:35 Okay.
**Marc Alff [MySQL]** 16:37 Which is why I think I've seen that. Where was it?
Come on.
Speaks, you know.
Not there.
So when Renovate does a PR, so at the case for macOS, it did upgrade things to one version, and also to another version, I mean, pick the one you want.
And this thing failed in CI for whatever reason, so I… closed the PR, but Renovate is not enough to remember that, hey, since the PR was closed.
It's not proposing it any longer, and if we want to change our mind, then we have to reopen this again.
So… maybe we can do the same thing also for Ubuntu and see, yeah, there's there's 1 Pr to upgrade to 24. There's another one to upgrade to 26.
I guess we need to decide whether we need to upgrade everything to the same version.
Probably not in terms of coverage.
And otherwise, what we could do is, Upgrade all the 22 to 24, and upgrade all the current 24 to 26.
Something like that.
But we.
**Douglas Barker** 18:06 question.
**Marc Alff [MySQL]** 18:06 Give us some coverage on different platforms.
**Douglas Barker** 18:09 Yep. And I know in CI we also select the specific compiler version and, and I think it's, is a GCC, 15 that comes with 2604, but that, that also would be helpful to make sure that.
**Marc Alff [MySQL]** 18:21 Yes.
**Douglas Barker** 18:22 The new version's covered, I don't know.
But, what version of Clang we can or should test with that we're…
**Marc Alff [MySQL]** 18:29 Yes, Bill.
One thing with OHST. So speaking of compilers.
For the maintenance CI in general.
You know the CI, which is raised to… used to find all the warnings, and make sure that the call is warning-free, and so on. Typically, we use the most up-to-date compilers, so whenever we upgrade.
or whenever we upgrade an OS, we should also check if there's a newer compiler there.
Because typically it can find some… find more things, maybe it will have more warnings detected, things like that.
Boom.
I think I saw some new GCC thing in our codebase recently, so I know that GCC Detect some… detect more things.
**Douglas Barker** 19:19 Yeah.
So maybe this one… does it seem like this PR then needs to be a manual one for now?
**Marc Alff [MySQL]** 19:25 Most very likely because at the minimum, there are some comments in the CI file that say, hey, we are testing on Ubuntu.
22.
So the comment itself, the title needs to be adjusted as well, so to avoid confusion.
So, but, I mean, the change should be trivial, but it will be a manual one.
And also, one thing, so… still looking at Ci. And after that there is also one major major change I would like to to discuss. So still looking at Ci, there is Vspr. To You would check for include what you use?
Which is nice, so, It looks like there is a syntax where you can say, oh, by the way, also look at all the other files which are in this place.
The only problem there is that CI is failing on that, and it's failing with basically an internal bug in the C-Lang format itself.
Where ceiling format is… Quite surprised to see our code and does not know what to do with it.
So… I'm not sure what to do.
Maybe one way also would be to see if there is a newer version of CINAHL format and upgrade, just hoping that this bug has been fixed in CINAHL format.
because in that case that will allow us also to use include what you use on every other file in the Api.
Okay.
**Douglas Barker** 21:10 I'll take a look at that, too. I haven't looked at what the error is, but maybe there's something.
**Marc Alff [MySQL]** 21:14 Yeah, I think someone pasted it.
Yeah, so… Raise your crosshair, and… Yeah, I don't remember the exact message, but it was, you can see it in the logs.
So yeah, I guess the first step would be to upgrade from that.
Because we will do that eventually, so why not do it now, if it can be a workaround?
And one thing that I wanted to discuss, which is major, actually, totally forgot about that.
We have a PR to finally fix the Windows singletons.
If I can find it.
It's a very basic one.
Mmm.
Yes, this one.
So that was a very long time ago, but at some point So you know that every, Every singleton in the API needs to be a really singleton, typically the tracer provider.
So that when you deploy an SDK, you set the tracer provider to something, and then every code compiled with instrumentation suddenly sees that and is instrumented with the SDK. But for this to work.
all the code compiled in using the header files needs to see that singleton. And the problem is.
There's a technical difficulty there, because all our APIs are header-only.
There is not an API library.
So everything is header only, and still having a singleton in C++ with a header file which is header only is not that simple.
And in fact, it took a lot of effort to get that working on Linux first.
That was a couple of years ago, and after that, the problem still remained on Windows. As of today, on Windows, we don't have singletons. So, this PR actually fixes the last part of it.
So it's a fix for the Windows platform only.
And… Oh.
So… There is some trickery involved there. Basically, there is some sort of library which is compiled that contains all the signal toll themselves.
Except that you don't link with that library directly, you have some code in the header files that magically do a get pocket address to find if a symbol exists or not, and and find it.
And, it seems… it seems to be working, boom.
So the code itself, I mean, I'm not getting it with digits now, but it seems to be working.
There is a unit test to test the singleton behavior that we used to fail on windows, and it has been changed.
So it's making good progress. The only problem there is that CI is not totally clean on every read for that.
Oh.
So… It seems that the the patch needs some some rework, especially We've yet, it seems.
But otherwise it seems to be a working working solution for what I've seen from just good review.
**Douglas Barker** 25:27 Yeah, I know.
Owen has experience, I think, working with Windows, and obviously.
**Marc Alff [MySQL]** 25:33 Okay.
**Douglas Barker** 25:34 Lilith and Tom, I think. Tom worked on the previous DLO, right?
**Marc Alff [MySQL]** 25:38 Yes, yes, he did.
I don't recall, are you mostly a Linux user?
**Douglas Barker** 25:45 I'm sorry?
**Marc Alff [MySQL]** 25:46 What platform do you typically use the most?
**Douglas Barker** 25:49 Linux.
**Marc Alff [MySQL]** 25:51 Linux, okay, yeah, same as me.
Okay, so, we need to take a look at this. It's, It's a very promising fix.
And I think there is a good change for this to work, which is a good surprise, because this thing has been there. This issue has been open for at least 3 years now.
With multiple attempts to fix it, and no solution inside, so… So it's some good news.
Just one thing quickly, We have a few reviews which are approved.
Thanks, Nikhil.
So.
**Nikhil Bhatia** 26:52 Yeah.
**Marc Alff [MySQL]** 26:53 for those, the next step is to actually do the merge and.
queue that, and rebase, and wait for the build, and merge again, so I'll try to… To do some of them.
If you… If you see a PR which is approved with.
basically, no remaining questions, or no remaining comments. Feel free to, to merge it as well. Just… it just clears the pipeline.
We've… everything that we have tried.
**Douglas Barker** 27:33 Sounds good. Yeah, I think that 4… the one for me, 4515, So, I was leaving it open to see if anybody else wanted to comment, but it's been open for, Almost a month, so… I think.
Yeah, I'll probably just merge.
**Marc Alff [MySQL]** 27:49 I forgot. Did I prove it yet or not? Oh, I will. I've looked at that code, and I just need to check the box.
**Douglas Barker** 27:59 And then there is one that's been approved for a while, but it's waiting on CLA.
**Marc Alff [MySQL]** 28:06 Yes, well, that we… there's not much we can do about it.
So, I think I've Yeah, some reminders.
So, the… We're waiting on the CLA, so the fix There are 2 parts to that Pr. There's the fix itself, which is trivial, which is to use GETIF instead of GET.
So… That anybody can do.
And on top of that there is. There are a bunch of test case. Well, a bunch test keys are added on that.
I think we can work. We can wait a bit for for Ci to clear, maybe with a reminder once in a while.
No.
But yes, on top of that, it raised the question of what we do for fixing the last SilentID issues related to No exception code.
So this is fixing one, but we have, We have many offers to Alois as well.
**Douglas Barker** 29:19 Yeah, I think there was a draft PR also fixing some, so this is… But then we talked about wanting to get done for the next release, at least for.
**Marc Alff [MySQL]** 29:27 Yes.
**Douglas Barker** 29:28 70.
**Marc Alff [MySQL]** 29:29 Yeah, I think I've seen it. The part I don't like is that it's fixing all of them at once. So it's… It's a lot of code.
It's a lot of code to look at, and We need to make sure that nothing is broken for with us, but It's good that we have that PR.
**Douglas Barker** 29:53 What do you think, Mark? We always get, PRs, if I open up an issue, like a clean, tidy issue, we have 57 or so PRs now, so I haven't been logging new issues, but if we want to focus effort on exceptions, I can open up some new issues, we'll get more PRs, but hopefully fix.
Exceptions.
Oh.
**Marc Alff [MySQL]** 30:14 I would say yes, but given that there is a PR already fixing a lot of issues, we should look at that PR first.
And see if we can… If we can approve it, or if we can ask to break it into smaller pieces, like one for trace, one for metric, things like that.
But I would not ask for more fixes while we have some in review already.
It just creates duplicate work for no reason.
But yes, if we had no PR, yes, that would be a good thing to do, just file a lot of issues and ask for Specific fix, one area at a time.
**Douglas Barker** 31:01 All right, so maybe we prioritize reviewing those 'cause we can, Mark, please review on… The ones that are fixing or catching exceptions.
**Marc Alff [MySQL]** 31:11 Yes. Do you remember the name of it?
**Douglas Barker** 31:14 I'll just… I'll just label them now as I'm looking at them, if you pull up the Please Review.
**Marc Alff [MySQL]** 31:23 Last value aggregation.
**Douglas Barker** 31:27 And then the one in draft is prevent.
stood out of range, escaping, but I'll mark it as please review.
**Marc Alff [MySQL]** 31:37 Okay.
Let's move this one first. Oh, it is.
**Douglas Barker** 31:50 And then somewhat related is maybe the one that you're talking about. That's the one that takes no except off of.
the provider and the tracer logger meter constructors.
**Marc Alff [MySQL]** 32:00 Yes.
Yeah, I think I've called for that also as well.
**Douglas Barker** 32:07 Okay.
So I've I've approved that one and and tagged you to see if you could take a look, but that that is one I think would be.
Hopefully we get in.
**Marc Alff [MySQL]** 32:16 Okay, I'll take another pass at everything to see.
Oh.
which PIs work, because I'm… I'm doing other things as well, and the list is spanning up. If you, yeah, if you see Feel free to add tags also, like, preservative tags, when you see fit, I mean.
So we… we prioritize those.
**Douglas Barker** 32:42 Sounds good.
**Marc Alff [MySQL]** 32:47 So, on… on the Renovate side, I think we are mostly good for CPP. There is only, like, a couple of OS upgrades to do, like, in… Ubuntu or for Windows, but… Except for the CMake surprises, it should not be that bad.
The other thing I wanted to discuss is the state of Cpp contrib.
**Douglas Barker** 33:13 Before we jump over, Mark, should we, I know you wanted to have a release in October. Should we open up that release ticket now?
**Marc Alff [MySQL]** 33:25 Well, I can. I can file the ticket. I mean, the only reason to to enter the ticket is to list all the the fixes we want to put in.
So sure, we can.
Which reminds me, as well, there are some deprecations which were blocked until today, so… I will unblock that and file for the… favor Piers, what goes with it?
Like… Those three things.
**Douglas Barker** 33:55 Yep.
**Marc Alff [MySQL]** 34:01 Sounds good. Yeah, I can create an issue.
Just to list what we need.
So on the Cpp contrib side.
So there is a Pr from Owent, which is massive to implement a Prometheus file exporter.
This is building on all the code that implemented for file exporter itself in in Cpp, which is all coming from moment.
So… VCPI is quite old, because it started a while ago.
There have been a lot of discussions on that, so it's finally getting to a place where everyone agrees.
It's… so it's big because there is some implementation code, but so far, all the… the only point of friction was CI itself.
And the reason this, this cause friction is that, in the meantime.
We also have renovate, which is now activated in the Cpp contract repo.
And Renovate has a lot of things to do.
And, of course, this is touching every… every YAML file used in CI, so everything… every time Renovates wants to do something, there is a potential collision with existing PRs, and on top of that.
Terms, so not the same.
Thomson Tomo.
also did a lot of work to to get Ci up to date.
And every time, There are a lot of changes that also collide on the same file in, and.
In the… in that exporter.
So… It's… it's getting better now?
My plan is to just merge this one because it's First of all, it's… by itself, it's ready to merge.
But also, it will unblock all the changes which have been piling up on the Prometheus exporter.
By the way, I don't know if you noticed, but tomo did also… a label or job in Ci, so that when you have some some code change, it just labels the Pi by area automatically. in this case this this Pi is touching the prometry exporter Sci. So the label is there.
And as you can see, We have… we have, in fact.
6 PRs all touching CI in the same place, which is why we need to get rid of that bottleneck.
So, I will start to merge this work for a moment, because first of all, it's the oldest, and it's stable, and then probably merge, one by one, everything which is piled on top of that.
**Douglas Barker** 37:10 Okay. Yeah, that one with all the labels on it, the big one, 653F approved. It looks like there's just maybe a sporadic, unit test.
**Marc Alff [MySQL]** 37:19 Okay.
**Douglas Barker** 37:25 I was leaving this one open because it does touch, the… extensions that I know Tom has been working on, so I was hoping they would.
**Marc Alff [MySQL]** 37:33 Yes.
Okay, well… Let's see if it's party.
**Douglas Barker** 37:42 How do you… Okay, yeah, you can rerun it from there.
**Marc Alff [MySQL]** 37:46 Yes.
So typically, you need to wait until Ci is done, and then you pick a job and you rerun it.
And, typically what I do is, of course, only rerun the one that failed. No point in rerunning everything.
And if you really, you insist, there's also a way to rerun the debug mode, which is much more verbose and So it's the script. The worker script itself will print some debug info to see. Okay, what is it? If the script itself is failing, you can see what it is doing.
**Douglas Barker** 38:23 Okay.
**Marc Alff [MySQL]** 38:44 Okay, so… Just to… so… The bottom line for Cpp contrib.
merge this to clear the bottleneck, and once this is merged, the next step is to also apply one by one Everything that, What's the name of this thing?
Oh, Renovate, yeah, I was drawing a blank. Yeah, apply everything that Renovates wants to upgrade, and we have quite a few there.
So, of course, not everything will apply. Of course, we are not upgrading to multiple versions at once, we just need to pick the proper one in each case.
But there are quite a few things.
Okay, it's still running, and the last time it failed about, in about 2 minutes, so looks like it was a transient failure.
Oh, fine.
Even post.
Yep.
Okay, I don't have anything else specific.
The main thing is, yeah, as usual, PR bottleneck, renovate bottleneck.
And then the usual suspects, like, Sync ID and exceptions, things like that.
I, I still… I know I still need to do it, to find the issue, to change the meeting time back to always Mondays.
Oh.
I really didn't have a chance to find that yet.
**Douglas Barker** 41:21 Yeah, no worries.
**Marc Alff [MySQL]** 41:31 Nikhil, out of curiosity, in which time zone are you located?
Okay, looks like Nikhil took a break. So, Oh.
**Nikhil Bhatia** 42:15 So yeah, I'm back. Sorry.
**Marc Alff [MySQL]** 42:17 Oh, you're back. Yes. I was just wondering.
**Nikhil Bhatia** 42:21 the.
**Marc Alff [MySQL]** 42:21 In which time zone you are located? Because we are thinking to move the meeting from Wednesdays to always Mondays.
**Nikhil Bhatia** 42:31 Yeah, actually, it gets pretty late, but still, I'm okay to join at any time.
**Marc Alff [MySQL]** 42:38 Okay.
**Nikhil Bhatia** 42:39 So yeah.
Like, mostly that, time zones overlap, So that's not an issue.
**Marc Alff [MySQL]** 42:52 Okay.
**Nikhil Bhatia** 42:53 So yeah.
**Marc Alff [MySQL]** 42:57 Thank you.
**Nikhil Bhatia** 43:00 Thanks, thanks.
**Douglas Barker** 43:00 Mark.
**Nikhil Bhatia** 43:00 Marc.
**Douglas Barker** 43:01 Mark, there was one PR that I missed that I wanted to talk about. It's one that was.
Going to cause the configuration to fail fast on any, any,
**Marc Alff [MySQL]** 43:12 Oh, this one, yes.
**Douglas Barker** 43:14 Support it, yeah. Should we just close this one, or is there any, changes?
**Marc Alff [MySQL]** 43:20 Let's see, CPP, PRs…
**Douglas Barker** 43:23 That's marked do not merge. I think there's only one.
**Marc Alff [MySQL]** 43:27 Yes, this one.
**Douglas Barker** 43:28 Yep.
**Marc Alff [MySQL]** 43:29 Yeah.
Yeah, I will close it.
I typically… so, I did… I didn't want to close it right away, just so that it stays up and people have a chance to look at it and comment.
But yes, the… There is no way we can take that change, so it will be closed.
**Douglas Barker** 43:50 Sounds good.
**Marc Alff [MySQL]** 43:55 It's a I guess it's… When starting on a PR like this, You never know, like, if you don't know a codebase, you don't know all the history, you don't know the specs.
You find something that seems easy, like, yeah, of course it should work like this, you know, I'm finding a PR for it, and yes, it should be a piece of cake, and I know there is something else.
So, this PR just falls into one of those cases, like, no, it's not that simple.
**Douglas Barker** 44:27 Yeah, and I share the concerns that you posted there, because I'm using Python and C++ and reading the same YAML file, so C++.
**Marc Alff [MySQL]** 44:34 Yes.
**Douglas Barker** 44:35 Crashes, and the other one doesn't. That's…
**Marc Alff [MySQL]** 44:37 Yeah.
**Douglas Barker** 44:38 undesirable, so, agreed. Yeah.
**Marc Alff [MySQL]** 44:42 Although, I mean, I guess… There is a point that we should not leave unparsed YAML nodes. Maybe we should parse it and explicitly make a note that we don't use the content of it.
And especially so the instrumentation node, there is some general part and then there is a part for each SDK for each language below it. Maybe we can take a look at the C++ node and complain if something is there because we don't support dynamic.
I don't recall the name, but adding dynamically some instrumentation. Oh, auto-instrumentation, yes. So we don't support that in C++, so if there is a node If there is a C++ node under instrumentation, it's most likely dubious.
Oh.
But, yeah.
**Douglas Barker** 45:38 I would like to support that config provider API and SDK at some point in the future, because even for my own instrumentation, I would like to be able to put the configuration inside this instrumentation block under CTP.
**Marc Alff [MySQL]** 45:52 Yeah, the provider, we should take it, yes. Yeah.
**Douglas Barker** 46:00 So, I think, definitely in the future, we can support it. It's not supported now, obviously.
**Marc Alff [MySQL]** 46:08 Okay.
**Douglas Barker** 46:10 Cool. Okay.
**Marc Alff [MySQL]** 46:15 So given that it is so.
Lalit is also a maintainer, and he has been involved in C++ for a very long time. He's also a maintainer of Rust's repo, so he's also very busy with other things.
So, I guess in terms of meetings, it would be mostly you and me, then.
**Douglas Barker** 46:41 Okay.
**Marc Alff [MySQL]** 46:43 So I'll make sure to show up so that you don't feel alone.
**Douglas Barker** 46:50 Yeah, I'll do my best as well.
**Marc Alff [MySQL]** 46:52 Yeah.
Okay.
Thanks, everyone. Thanks, Duke. Thanks, Nikki.
**Nikhil Bhatia** 46:58 Thanks, Mark.
**Douglas Barker** 46:59 Thanks, Mika.
**Nikhil Bhatia** 47:00 Thanks, Doug.
**Douglas Barker** 47:02 Super.
**Marc Alff [MySQL]** 47:03 But.
**Nikhil Bhatia** 47:03 Bye.
