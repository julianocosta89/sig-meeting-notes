SIG: C/C++ SIG
Date: 2026-03-18
Duration: 39 minutes
Zoom Recording URL: https://zoom.us/rec/share/M6O6rQkuQ9twHEdwNqnUjvh-dvTJ9y8lhNgvmF2cCqewfn-gS5sqxUU7BBpfz6n5.4-xalhDvyCjNje8b
============================================================

## Zoom Recording Transcript

**Doug Barker** 02:13 Hey, Tom.
And Tom, do you know if Mark or anybody else is gonna join?
**Tom Tan** 05:19 Good morning. I saw some notes from… in the meeting notes. I think Mark added for today, but I'm not sure if he will join or not.
Okay. Yeah.
**Marc Alff [MySQL]** 05:30 Hi, everyone.
**Tom Tan** 05:31 Hi, hi, Mark.
**Doug Barker** 05:32 Hey, Mark.
**Marc Alff [MySQL]** 05:34 Sorry, Zoom was not cooperative, so… Okay, can you see my screen?
**Tom Tan** 06:06 Yep.
**Marc Alff [MySQL]** 06:07 Okay, great.
Hi, Luke.
**Doug Barker** 06:11 It worked.
**Marc Alff [MySQL]** 06:19 I'm not sure if, Severin is joining as well.
We'll see. I think he knows it's now. Just so you know, because of the time zone difference between Europe and the States, this is not the usual time for Severin and me, and for his son as well.
Can you hear me okay?
**Tom Tan** 07:05 Yeah, good. Yeah, okay.
**Marc Alff [MySQL]** 07:06 Okay, so, On the agenda, I just added a few notes, a couple of things to discuss, but I don't know if you have any other topic as well.
**Doug Barker** 07:25 Maybe the release, if you're not gonna cover it. Anything else?
**Marc Alff [MySQL]** 07:28 Yes, it's… yeah, I want to discuss that as well.
Okay, so… I'm… I'm going in order, and just doing… going quickly.
One thing in the last, months, we've been implementing a lot of things in C++, like doing this feature, that feature.
And in the meantime, the spec also has changed, saying, oh, we need this, we need that, there is this new API and whatnot, and this new parameter and whatnot.
So, slowly, I think we are diverging from the spec in ways which are… Sometimes small, sometimes we just forgot to implement some new spec.
So, I'm taking a look at the spec compatibility metrics to see, there are huge areas which are not covered by C++.
So, I think we need to take a look at it to see… to identify them.
And sometimes it's something we have done already, we just forgot to mention it in the spec.
So it's done, there is just a status update to do. And sometimes it's things that have changed in the spec that we have not noticed, so we need to… at least, I think, create a PR for that so that we don't forget.
So… Just… just something to be aware of for the… for the specs.
**Doug Barker** 08:59 I took a quick look, Mark. There were a few things that I implemented that certainly checked off some, some spec requirements. How do you want to, like, track which ones? We can either start, like, an issue, maybe, in our repo?
**Marc Alff [MySQL]** 09:11 So… What I did… So, the spec itself now is in a huge YAML file, which is that one.
And I looked at it, and Created everything which is done only to keep things which are remaining, which is in this list.
And I'm in the process of, like, sometime when there is a question mark, where I'll just say whether if this is really done or really missing.
And to just try to make values smaller.
Just today, I prepared a PR to mention that some, for example, some environment variables are implemented.
This one is implemented, this one is implemented, and so forth, so things that we just need to address.
So yeah, I'm… I'm thinking of just getting that list, shrinking at some point. And as far as, So, typically, either we have something to update in the matrix, in which case it's a PR in the spec repo itself.
Or, if it's something missing, we should just create a niche event.
Does that answer your question?
**Doug Barker** 10:33 I think so. There's a few PRs specifically. I think one is, like, the, uniqueness of registering new instruments, or, meters in… Marc Alff [MySQL] 10:44 Okay.
**Doug Barker** 10:45 these are marked as, like, either question marks or minuses in this spec, so I could either just create a new issue or PR directly to the spec. I think… I think the question is, like, how do you want to manage that? Do you want to, like, create an issue.
**Marc Alff [MySQL]** 10:58 Well, if you… Doug Barker 10:59 With everything that's been finished.
**Marc Alff [MySQL]** 11:02 So, if you know the answer for a given entry, like a PR which is done already, feel free to file a PR in the spec itself.
I can… I can show you an example.
**Doug Barker** 11:16 Yeah, I saw the one that you did, yesterday.
**Marc Alff [MySQL]** 11:19 So, yeah.
Oh.
Just be aware, though, there is a, you have to run a script, because some files are generated automatically in the MDF file, in the spec, so there's a small script to run, but there is a make file for that.
**Doug Barker** 11:33 Grossing.
**Marc Alff [MySQL]** 11:34 And… If it doesn't work, you can always ask me for details.
Okay.
Yeah, so this was this topic. Another thing also which is changing is, OpenTeametry Porto is at version 10 now, and we are still on version 8, so… the thing which is missing is, Bazel Central repository needs to do a packaging for that, so eventually that will come. But the next big question is, OpenTelemetry Portal just defines the profile signal And we are not doing anything about it, so… The question is, should C++ do something about it? And I'm guessing the answer is yes. And then… We probably need to look at the details and decide, okay, what… What does that mean? Do we need some new exporter to a new endpoint, and some SDK code and whatnot, so… to be… to be investigated, I mean… We've been totally ignoring this thing for a long time now.
And, yes, to answer your question on what Nexo is, so, There is a lot of effort, thanks, Doug, on the ceiling tidy cleanup.
So, I'm just waiting for this cleanup to… as long as we have PRs to clean up, I'm waiting a bit.
So that I can include that in the next release. Of course, not everything will be resolved, so… when, I think it's… I'll do a release probably this week, with what we have, and then we can continue the cleanup later, but the good news is that this has been… making good progress. The number of issues was 600 plus, if I recall correctly, and now we are back at 200.
So, thanks. I've done a few myself, and thanks, Duke, for all the others.
And speaking of, pRs, yeah.
Oh.
There are new PRs from today, I also see, I also saw the resource detector thing, so we need to… Obviously, merge that before doing varieties.
talking about Verdis… Google or Tom, if you have anything that you want to include there.
Please make a comment, so that if you… if you depend on the fix, make sure to add a comment so that I will wait on it for it before making the release.
Numero… Question or comments on the release itself?
**Doug Barker** 15:08 I was thinking, of updating the third-party dependencies as well, so we're currently, I think, one version behind on gRPC and, Protobuf.
So I can put my PR to update those.
**Marc Alff [MySQL]** 15:22 Yeah, so, so you know… Joe PC has, well.
So we have two, two different builds. We have the CMEC and the, basel build.
And Bazel has made a lot of progress recently because… with all that.
So, this is basal only.
like this, curl, and so on. Because what happened is, there is now a new workflow with a boat, which is picking up the dependencies and pushing PLs to adjust them.
And this… this workflow is dedicated to Bazel. So Bazel did a lot of, had a lot of upgrades to… to things recent, In the last 2 or 3 weeks.
And for CMake, nothing has changed recently.
So we… Bazel typically… so I think it's okay for Bazel, because Bazel typically works on the latest code anyway.
And for CMake, because we have a dependency on C++14, We need to see if there are things that we can upgrade while still being compatible with C++14, or… Oh, or what's Vista Israel?
But yes, Phil.
There are a few things that, most likely are out of date in CMake.
for dependencies.
Another topic that came today, It has been identified a while ago, but We have a lot of preview flags.
So, someone asked, okay, how do I use this feature? It's a compile time flag, not a run-time flag, blah blah blah, so… I just provided some, some comments.
But overall, the… The thing is, some of those flags, in that case, the OTLP retry itself.
That we have both in gRPC and HTTP.
Those flags have been there for a long time now, and I think it's time to… Make the code mainstream, so the first step is to, change the feature to enable by default, so that more people are exposed to it. And if nothing breaks, and if nobody complains, then just to remove the preview feature so that, The code is part of the normal code base.
So, it's too late to do that for this release.
But for the next one, I think we can also take a look at, a greeting Many preview flags that we have that have been here forever.
Does that make sense?
**Doug Barker** 18:38 Yeah, makes sense.
**Marc Alff [MySQL]** 18:40 No? Okay.
And, last thing… it's a long topic, so there will probably be a lot of discussion about that, but… The ugly child that we never mentioned during the meeting, which is CPPContrib, it's basically, Slowly rotting, so… A lot of the CI processes there are not even working anymore, so CI is broken.
platforms tend to be out of date, and the workflow is not updated to use related platforms.
Prs are not, there are a lot of old PRs which are not looked at, and not reviewed, and not merged, so… The big question there is what to do with it in general, I mean.
Do we… do we try to… to invest some time to at least get CI working and getting back to working state.
Or do we declare some parts unmaintained?
Because at least that will be, More accurate, compared to the… what the real estate of this is.
And of course, because Contributes are just a collection of different things, We need to take that, to look at that contribution by contribution, because some of them might be maintained, some of them might be obsolete.
So it's not for the whole repo, it's country by country.
But I really think that we… it's… we need to do something there.
Even with Makefile, for example, they are not even aligned with the recent OpenTelemetry CPP releases. They are using some old releases.
Which is no good.
**Doug Barker** 20:53 What do you think is the right, path forward with?
OpenTelemetry CBB contribute.
**Marc Alff [MySQL]** 20:58 Not… not sure.
One main issue, I guess, is to actually know if someone is using something or not.
Oh… It… just looking at comments or peers in general, it looks like some parts are used.
And others are just, ignored, so it's hard to tell if they are ignored because it's working, and there is no issue at all.
Or if it's because no one is actually using it.
Whoa.
The only missing part is someone to actually maintain that and look at it.
Vuh.
The list of approvers varies long, because in the past, different people were supposed to look at approved code for different countries.
But truly nothing has happened there, so… I think what we need is approvers or people to actually take care of some areas, but I just don't know how to… To get people to look at it.
And otherwise, well, we… We made it to just declare some of them obsolete.
Or at least unmaintained.
So, no wooden server, I just don't know what to do with it.
**Doug Barker** 22:31 it does seem like there's different categories of code in there. Some are, like, extensions to the SDK, which you would expect, but then some seem to be, like, larger projects, like… Web server module.
**Marc Alff [MySQL]** 22:46 Yeah, there are many different things. There are some exporters, like Lalit and Tom are using, like, all the Geneva stuff, so this is more maintained.
But others, like engine mix and… Web server and things like that, they are just so far behind.
It's, nobody's actually looking at that.
**Doug Barker** 23:11 I was looking at the VC Package repository the other day and saw an issue where somebody was asking for a package in VC Package for OpenTelemetry CBP contribute. Specifically, they wanted to use the, spitty log, Instrumentation.
So I think that there's probably some… at least one person's interested in.
**Marc Alff [MySQL]** 23:34 Alright, so, you know… Doug Barker 23:35 It'd be like a formal package, but I think.
**Marc Alff [MySQL]** 23:39 Yeah, the different… the different loggers, they are fairly… fairly recent and fairly decent.
So that, that can be maintained, I think, because the person who wrote that did a good job, and the code is clean there.
We just need to to update CI and make sure that we have recent libraries for the dependencies.
So we, yeah, these, these parts can be, can be maintained, I think. Others, like NGINX, It just… first of all, we… To maintain that, you just need to… The whole ecosystem that goes with it, and all the dependencies, so it's much bigger.
So those dependencies will need to be maintained by someone who knows this area. It's not something we can do ourselves, I think.
And yeah, some parts, like the different loggers, those can probably be, updated and with a working CI, because we had a working CI before all of that.
So, no need to resolve it now, but just something I want to mention, because at some point, we need to decide what to do there.
Any issue or PRs you want to discuss in, in particular?
The version 10 or… Yeah, of course.
**Doug Barker** 25:43 You had logged an issue saying that the, the header files For the semantic conventions were not being installed.
**Marc Alff [MySQL]** 25:52 Yes, I… so… what I did, I tried to write some code in a demo application to actually use semantic convention and had a build failure.
And so, I need to double-check on that, but I think VEDA file was not there.
Oh… I need to check that again, because I saw your comment that it should be working, so I don't know if it's me, because I used the wrong version, or something like this, or did not uninstall, a proper install, or I need to double-check that.
But the… so, the expected result anyway is that, when someone instruments their own application, like, when they, emit a span or a log record or anything, they may need to attach semantic convention… attributes with semantic conventions in it.
And to do that, we need to see the semantic convention set of files.
And because Rosetta files are generated automatically by a different script, I don't know how well the makefile and CMake takes care of that, and if CMake is actually installing that or not.
So that was the area to check.
**Doug Barker** 27:08 Okay. Yeah, I took a quick look. It looks like on CI, it's installing the header files correctly, and then locally, when I did a test, it was installing them, but if you have a way to reproduce your issue, just… Please add it.
**Marc Alff [MySQL]** 27:20 Okay.
**Doug Barker** 27:20 issued, and I'll take a look.
**Marc Alff [MySQL]** 27:22 Yeah, I will double-check my setup, or… and try to reproduce it then.
**Doug Barker** 27:27 Okay.
**Marc Alff [MySQL]** 27:29 Nice.
On, on issues, so… I'm not even talking about the recent one, because then, we have a review going for that, and that would be resolved quickly.
I'm just more looking at things which are stuck.
This one, so some extension to the… YAML parsing code.
For things which were missing, so someone opened a PR for that, which is actually quite good.
And, there were a couple of review comments, and since then, that person has, Did not come back with, comments or any action, so… Not sure what to do with it. The PR looks good, but it's slowly getting out of sync, because we have so much changes in general in the code base, especially with the same tidy cleanup.
But, I'm afraid that this is going to, To decay, and will take… will… it will take some more work to adjust to it.
And another one which is in the same state, like, this one.
some code moving from header files to CC files, which is good, but in the meantime, because there are so many things changing with CNN format, it causes merge issues.
Because then, of course, the fix that we applied to the editor file needs to be, reapplied again to the… you could move to the CC file, To get the same fix, so… this is an example where the person filing that PI… I mean, the PI is good, but leaving it open for a long time creates issues.
So, hoping that Harish can actually come back to it and resolve it.
And on old PRs, I think there are a couple there that need to be closed. I can, contact the… Oh.
The owner of that to, to let them know.
And the one thing that we'd like to close also, Tom, I don't know if you… if Lalit or you are still working on that, but the… the experiments from Copilot that, are from last summer.
those are still in draft and still, well, the PR is still open, but nothing is happening there, so I wonder… I was wondering if we can… Either finish it, or most likely close it, if we are… No longer playing with that.
The goal being just to… to clean up the PRQ there, because they're… I mean.
20… there are 20 open, but, honestly, we are not doing… we are not reviewing all of them, for all changes all the time.
So it's… because there are so many of them, then it becomes… Easier to just, forget some changes which are important, somewhere.
**Tom Tan** 30:52 I will sync with Lalit after that, this… PRs.
**Marc Alff [MySQL]** 30:59 Sorry, I missed that.
**Tom Tan** 31:02 I'm… I was thinking it's late, and after making these PRs after the date or closing.
**Marc Alff [MySQL]** 31:09 Okay, thanks, Tom.
**Tom Tan** 31:10 Logan.
**Marc Alff [MySQL]** 31:23 And on issues, we don't have that many issues. The copers that we have here.
Are, in fact, things that, I created, just to have something to list in that, But bigger laundry list.
Of things that, people can pick.
And… So, for example, for the, the YAML configuration file. There are 3 open items that need to be resolved, and we have a PR4 one already.
And someone expressed interest to do the others, I think.
So the… the part that seems to be working is just, listing, PRs where we… That are good entry points, and P… I'm pleasantly surprised that people… seem to look at them and find something interesting, and they work on them, instead of just picking a random bug from two or three years ago and try to do… to work on that.
So, this is why I'm creating new items, to just add items there.
And, it seems to be working, because we have all of those that are… have been resolved so far, since… This, VSPR was created.
So, I don't… I don't have any more specific topics, just so a reminder, if you need something part of that, really, is just say so.
And I will try to do that release this week.
Yeah, and if not, it will be early next week.
**Tom Tan** 33:25 Thank you, Mark.
**Doug Barker** 33:30 Thanks, Mark.
**Marc Alff [MySQL]** 33:33 Yup.
So, So, Doug, first of all, we didn't talk for a long time. I've seen you online, but it's nice to see you back, so… Welcome back, and thanks, as usual, for all the work you're doing on, on the… on CMake, on Sealing Tidy, and other things, it's making a real difference.
**Doug Barker** 34:01 Thanks, no, appreciate it, it's good feedback.
**Marc Alff [MySQL]** 34:04 Yep.
**Tom Tan** 34:07 Thank you.
**Marc Alff [MySQL]** 34:10 Unless you have other topics to discuss, I don't have anything more myself.
**Doug Barker** 34:24 Alright, let's go ahead.
**Tom Tan** 34:25 from my side.
**Marc Alff [MySQL]** 34:30 Okay, well, thanks all for joining, Ben.
And, I'll finish the code review that we have, so, do go and merge your PRs, today, then, for those things?
Or, yeah.
Alright, thanks everyone.
**Doug Barker** 34:47 Thanks, guys. See ya.
**Marc Alff [MySQL]** 34:49 Yep, bye now.
**Tom Tan** 34:50 Right?
