SIG: C/C++ SIG
Date: 2025-10-29
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Doug Barker** 01:18 Hey, Nico, how are you?
**Nikhil Bhatia** 01:23 Hi, Doug, I'm fine, how are you?
**Doug Barker** 01:25 Oh, pretty good.
**Nikhil Bhatia** 01:27 Oh, that's great.
Doug, I wanted to ask, one thing,
On my PR, there was… there were some comments by, someone else, other than our reviewers, so.
**Doug Barker** 01:44 Huh.
**Nikhil Bhatia** 01:45 Like, are they valid? I wanted to ask.
**Doug Barker** 01:50 Yeah, I think, you know, it's a public, open project, so anybody is free to comment. I think it's also your judgment, you know, to review it and see if it's worth,
you know, or ask for clarifying questions, but I think anything that people post, you know, is something that can be considered.
And there's also, like, the, co-pilot post, too, you know, and those are worth considering.
But ultimately, for the PR to be merged, one of the approvers or maintainers will have to approve it and then merge it.
**Nikhil Bhatia** 02:25 Oh, okay, got it, got it, Doug. Thanks, Doug.
**Doug Barker** 02:28 Yep.
Yeah, so I think the short of it is, yeah, just consider it, you know, reply if you feel appropriate, and then, ultimately, though, one of the approvers or maintainers will have to approve.
**Nikhil Bhatia** 02:40 Yeah, yeah, sure.
**Marc Alff [MySQL]** 02:40 Hi, everyone.
**Doug Barker** 02:43 Hey, Mark.
**Nikhil Bhatia** 02:45 Mark.
**Marc Alff [MySQL]** 03:04 Sorry I'm a tiny late today.
So, Doug and Nikhil, do you have any items to discuss? I don't… I just quoted the conversation in the middle, so I don't know,
If you are… if something needed attention or not.
**Nikhil Bhatia** 03:48 Everything was clarified, Mark, bytuck.
**Marc Alff [MySQL]** 03:52 Okay, great.
I wanted to discuss some things specific to the runtime context storage with Valid. He mentioned that it will be a bit late. In the meantime.
I don't have a lot of things. One thing I noticed is that,
OpenTelemetry Porto did a release a while ago, and… We're waiting for…
Bazel to upgrade that, so it's,
Bazel took that in Bazel Central Repository, so we can now adopt it, so I think I will probably soon.
And another question I have for everyone is, the last release was, I think, earlier.
Yeah, the last release was a month ago, I was wondering if,
Anyone needs a release soon or not, and we…
I think we can start to plan for another one.
**Doug Barker** 05:32 That sounds good. I think this'll be… will this be the first release with the configuration… declarative configuration feature?
**Marc Alff [MySQL]** 05:39 Yes. So, things were merged in part earlier, but I think only this release will have the meg files. So, in effect, it's only working starting off this release.
**Doug Barker** 05:57 I guess starting there, are there any other PRs that you're, need to get in, then, for this release?
for the configuration.
**Marc Alff [MySQL]** 06:03 Probably, yes, so the…
So, the spec for the model itself in configuration is still moving a bit. They are preparing already 3 now. Lately, there were some changes in the way the TLS parameters are represented, so we need to adjust for that.
So, yes, I will most likely do a PR, just for that. And…
But I think it should be… that should be all for now.
And in any case, the… The language… the model itself is still evolving slowly and with minor tweaks, so…
We can declare that the feature is complete according to the RC3 spec, but if there are some changes later, then of course we will need to adjust as well.
**Doug Barker** 07:07 Good.
**Marc Alff [MySQL]** 07:17 Yeah, so I think Porto has done some…
So we need to upgrade to that. I haven't checked CMT conventions.
Can do that quickly now.
Yeah, well, that release was a while ago, so I don't know if…
Anything is coming quickly, or not.
Okay.
Not yet, I guess.
Any specific issues or PR you want to look at?
Nikki, I don't know if you have,
work in the pipeline or not, I don't remember.
Maybe I should look into popular reports.
**Nikhil Bhatia** 08:41 Lalit said that he would, review it this week. From starting, I didn't get any review till now on that, and my peer, so…
**Marc Alff [MySQL]** 08:49 Okay.
Oh, I don't know if you noticed, but there's a new user, this guy, who is making a lot of comments in a lot of places, so he seems to be very motivated to get into the code and in the details.
**Nikhil Bhatia** 09:16 Yeah, actually, he, he reviewed my pull request too, and he provided me some comments.
**Marc Alff [MySQL]** 09:22 Okay.
Sounds good.
Duke, anything you want to look at in particular?
**Doug Barker** 09:46 Yeah, I just had that, one that says Docker. I think it's, 3718?
So, this is kind of like a final…
wrap-up of the third-party dependency cleanup, so finally, in order to get rid of that setup gRPC script, I had to go in and fix the, the Docker, so at least it's building with all the right dependencies, so…
It builds locally. I don't know… I don't know who's using it, but if anybody wants to use this now, it'll at least pull in the dependencies.
**Marc Alff [MySQL]** 10:17 Yeah, it's, I would be surprised if a lot of people are using it. I think, historically, it was mostly used internally by maintainers to do some development on this or that.
But, personally, I have not even used it, I think, ever myself.
**Doug Barker** 10:38 Yeah, the dependencies were out of date, and it was pointing to an old version of OpenTelemetry CPP, but at least it will point to main and build all the dependencies, so if anybody…
**Marc Alff [MySQL]** 10:49 Yeah.
**Doug Barker** 10:49 at least wanted to get some inspiration on how to, build a Docker container with all the dependencies. Cool.
Now, a good spot.
**Marc Alff [MySQL]** 10:57 Okay.
Well, in any case, this is only affecting CI, or…
tooling if someone is using Docker, but it's not affecting the library itself.
So, Vitworth.
**Doug Barker** 11:08 Yeah.
**Marc Alff [MySQL]** 11:09 low risk.
**Doug Barker** 11:11 Right. It doesn't affect the library, and I don't think even any tooling in CI uses this, so I think this is probably just, like, offline, you know, like you're saying, maintainer use cases, but I figured in order to get rid of the
set up gRPC script, I had to fix everything else, so… I did so.
**Marc Alff [MySQL]** 11:28 Yeah, good code.
Okay.
Asan, I think, has some knowledge of Docker, so maybe he can review that.
And I can take a look as well, and do the review.
**Doug Barker** 11:42 Okay.
Sounds good.
**Marc Alff [MySQL]** 12:13 By the way, I don't know if you… if you noticed, but
I think this year, again, Europe and the states are not changing to wintertime at the same time.
So, we are already in wintertime, and for typically 2 or 3 weeks, I think the meeting
For you, it's the same, because you are in the States, and the meeting is, in fact,
in Pacific time.
But for me, the meeting is earlier than an hour.
So, this, this could affect also his son, who is in Germany.
**Doug Barker** 13:01 Yeah, I'm on, East Coast time now in Boston, so…
**Marc Alff [MySQL]** 13:06 So, that's right to move this.
**Doug Barker** 13:08 Well, this one's actually a good time for me now, because it's lunchtime, so I can easily find time to…
to join.
**Marc Alff [MySQL]** 13:15 Just so you know, I also created a new label.
For… because,
I'm getting tired of looking at every single item in PRs and issues, so there is a new label now, so whenever you need to discuss something explicitly, just feel free to tag an issue with it.
And if you… if you don't have the permissions to tag something, just add a comment that it needs to be discussed.
**Doug Barker** 13:48 Perfect. Sounds good.
**Marc Alff [MySQL]** 13:57 Duke, a question for you. So, recently, I've seen in CI2…
test failures that I've never seen, Never seen before.
And, for example, this one,
So, we had… we had another test case that fails once… once in a while, and it's known, but this one, this is a test case that fails.
And what happened is, so, the test case is defining two traces and doing an export.
And it's expecting the two traces to be part of the same payload, expecting the exporter to actually work on it once.
And in this case, it did… the exporter was called two times, which is still legal and legit.
But I'm wondering if this is somehow related to a recent upgrade of the g-test library.
Because I know that we have done that in some places, and I'm… because it's a timing issue, I'm wondering if there is anything that changed in GTest itself that makes it more…
More likely for that timing issue to appear.
**Doug Barker** 15:13 Yeah, we upgraded all the dependencies, so even pro… this would be impacted by Protobuff as well, because it's OTLP, I'm guessing.
**Marc Alff [MySQL]** 15:22 Yes. Yes, it is OTRP, yes.
**Doug Barker** 15:26 So yeah, it potentially could be. Do you think,
Do you think there's an issue with the dependencies, or do you think the issue's exposed… Oh, no, no, it… I think it exposed an existing flow in the test.
**Marc Alff [MySQL]** 15:41 Okay. So the test was,
I mean, it's a very edge case. I was just surprised that it happened twice in a row, which is unlikely. But very edge cases, it can happen, and when that happened, the test case was not robust enough to account for that.
**Doug Barker** 15:59 But it's a purely a test issue, there's no issue…
**Marc Alff [MySQL]** 16:03 I haven't seen anything wrong with the dependencies or with the production code itself.
**Doug Barker** 16:08 Hmm.
Yeah.
Well, I could definitely see the case of, like, upgrading the dependencies has changed the timing of the test in some way that exposes the issue then. But I think, like you said, the concern would be, like, is this a production code issue, or is it a test issue? And it sounds like you think it's a test issue.
**Marc Alff [MySQL]** 16:28 No, it's a… it's a test.
**Doug Barker** 16:31 Okay.
**Marc Alff [MySQL]** 16:31 Okay.
Also another question for you, which is related to CMake, because you seem to be good at it.
For whatever reason, we use this old policy, and…
By definition, every time we use an old policy, CMA complains that, hey, this is duplicated, and it will go away at some point, so you should do something about it, basically.
And I'm wondering if anything needs to be done for this one. From what I could tell, this specific policy is about…
the… setting the warning flags in C flag for Visual Studio.
**Doug Barker** 17:22 Sure. And…
**Marc Alff [MySQL]** 17:23 I don't… I don't recall the reason why we did that.
But in any case, because of the maintainer's build, all the warnings should be cleaned at that point. So even if the warning flags are changed, I don't see why it would affect the build.
So I'm guessing we can get rid of that.
**Doug Barker** 17:43 Okay.
Yeah, I can put up a PR to get rid of it. I think there was a comment in the top of the CMake file where this is set, and why we kept it, but I agree with you. By the nature of it being set to old, like, at some point it will go away, we would be forced to address it, so we might as well try to remove it now.
**Marc Alff [MySQL]** 18:00 Yes.
Yeah, because, like,
In the application I'm using, and instrumenting, we build from source, and this is selling to show up as well.
Okay. You know, build.
Usually, this is a good… yeah, those kind of things, this is a good driver for…
For me to actually look at a bug and fix it.
When you depend on it, you tend to fix it faster.
**Doug Barker** 18:29 Right, yep. And those CMake warnings can be annoying.
**Marc Alff [MySQL]** 18:33 Nope.
**Doug Barker** 18:35 Okay. You can, you can assign this to me. I'll just try to remove it and see if anything in the build, complains.
**Marc Alff [MySQL]** 18:42 Yeah, so I was… This is exactly what I was planning to do anyway.
See, brilliance. Brilliancy.
And we…
**Doug Barker** 18:51 Okay.
**Marc Alff [MySQL]** 18:53 I think Tom might know about the story, because according to Vid Blame, he's the one who actually said that.
But we'll see during the review, or if anything shows up.
But again, this is just a warning, and we should be warning free, so I don't see why it would break.
**Doug Barker** 19:11 Yep.
**Marc Alff [MySQL]** 19:25 And also, another thing which is related to CMake, if you have some knowledge about that, So…
Someone is complaining that we have two slashes in some path.
So… In my understanding, this actually changes nothing, because…
Two paths, two slashes, is exactly the same as one, so…
It doesn't change which file is installed where, it's purely cosmetic.
But I'm curious why things like this can happen.
I was hoping to find a place in CMake where we, say, append exporters slash.
to a directory somewhere, as opposed to just exporters, but I haven't even seen it.
So I don't understand why we have things like this and this.
**Doug Barker** 20:15 Yeah, and I took a quick look in CI, and I don't think that jobs in CI show this, and I don't think I see this locally, so I don't know if this is reproducible everywhere, but…
What you guys see when you, pro Sermic.
**Marc Alff [MySQL]** 20:36 Because in the install test, I guess we already make install at some point, so we should see that.
**Doug Barker** 20:42 Exactly, yeah. I took a quick look, and I didn't see it in CI, so… I don't know.
**Marc Alff [MySQL]** 20:46 Focus.
**Doug Barker** 20:50 I can comment, if you want, with a link.
CI logs. I don't know if this user will be able to see the CI logs, will they? Maybe.
**Marc Alff [MySQL]** 20:59 They should… well… You need to know where to dig into.
Because people typically, I mean.
**Doug Barker** 21:09 But they are public if you're logged into GitHub.
**Marc Alff [MySQL]** 21:11 Yeah.
**Doug Barker** 21:12 Anybody can see it.
**Marc Alff [MySQL]** 21:14 I think anybody can see it, yes. Typically, you would go there to see the build, and…
Let's see…
**Doug Barker** 21:26 It's like any of the season.
**Marc Alff [MySQL]** 21:27 toy tests.
CMIC installed blah blah blah…
So it would be somewhere down the…
**Doug Barker** 21:41 Yeah.
**Marc Alff [MySQL]** 21:42 down the rabbit hole, but, I mean, you only have to…
We're looking to find it, so… I doubt people.
**Doug Barker** 21:51 That's true, I don't think… you probably can't get a link to a specific line in the…
**Marc Alff [MySQL]** 21:56 Log output.
Or just copy and paste the log output, because it tends to go away at some point.
**Doug Barker** 22:02 Yep, fair enough.
Do we need a label,
For issues like this that may be, like, not an issue.
If we can determine that it's not an issue that we need to address, because we only have, like, needs triage.
**Marc Alff [MySQL]** 22:26 It needs more info.
Yeah, maybe we have one, one label like this, otherwise we can just comment and close it.
**Doug Barker** 22:35 Okay.
**Marc Alff [MySQL]** 22:36 I don't remember, I mean, I'm used to the…
the GitHub UI as you see it now, which is with a maintainer's privilege, so I don't even remember, if you have different privileges, what you see and what you can or cannot do.
I think you should have…
You should be able to set labels, even to create ones, new ones, if you want to.
I don't remember if you can close an issue or not, things like that, but
Otherwise, just put a comment and I will close it.
**Doug Barker** 23:13 Okay. I think I can. I think I've been, not closing user issues and letting them close it after, after I make a comment, but, if you…
I think we should close issues after we make a comment, we can do…
**Marc Alff [MySQL]** 23:26 Whoa.
I mean, it's,
You're right, it's a better practice to just comment and let the user close if I agree, and…
After some time, if there is no reaction at all, then we can close it ourselves.
**Doug Barker** 23:39 Okay, that sounds… sounds good.
**Marc Alff [MySQL]** 23:43 Thanks.
**Doug Barker** 23:44 Nope.
**Marc Alff [MySQL]** 23:59 Oh yeah, so I guess we can think of…
Can think of the next release to come.
**Doug Barker** 24:21 Did anything, come of the…
the contribution and the discussion about the OpenTelemetry CPP Contrib, are we gonna put that
I forget what that contribution was.
**Marc Alff [MySQL]** 24:32 It was automatic instrumentation in PHP.
So…
I think I saw either a community or a blog post or something, saying that the contribution was accepted.
by the governance committee in general, which is good. And I… so I don't know what are the next steps for that, if we need to create some… some repos to receive the code and start to set up reviewers or maintainers and things like that.
But yes, the contribution itself was accepted.
**Doug Barker** 25:11 Nice.
Because one thing I've been thinking about, and I can probably do within the next year or so, is, like, start to work on CMake infrastructure for OpenTelemetry, CPP, Contrib, if we wanted to get to a point
Where we create a single pro… single project, you know, that people can easily contribute to, because right now, it's kind of a free-for-all.
**Marc Alff [MySQL]** 25:36 It's, yeah, right now it's free for all, and… Well, first of all, the…
CPP contrib itself is not that well maintained, to say the least. It just depends on which… some contribs are maintained, some others are not.
And even beyond that, if you have too many cooks in the kitchen, I mean, you see one style of
script for CMake in one place, another style with a different design in another place, and it starts to be very difficult to sort out.
So, yeah, if… and you want to dive into CMake there, feel free.
I would be more than happy to, approve peers as they… as you can provide them.
**Doug Barker** 26:23 I think I lost the audio for a little while, Mark, I didn't…
**Marc Alff [MySQL]** 26:26 your, oh, sorry.
Yeah, I was just, I was saying.
When too many people, maintain CME scripts in different places, it's not uniform, so it's much harder to maintain.
So if you have the same style of CMake all over the place, it will… it will make…
It will help a lot, first of all, to have some consistency, and if you can file some PRs, then just let me know, and I will review them and approve them.
**Doug Barker** 26:57 Okay.
Because one thing we could do is to make it a single project structure, like we have in the main repository, and then have components for each of the…
Kind of like what are currently sub-projects, you know, like a new extension, or a new, exporter, or a new resource detector, or something like that could be its own.
CMake component within that overall project, and then that would allow us to build, you know, build and install just OpenTelemetry CPP Contrib as one project.
**Marc Alff [MySQL]** 27:31 And that's…
**Doug Barker** 27:33 that might be, a goal, so if that sounds interesting, that could be something I work on, you know, later this year.
**Marc Alff [MySQL]** 27:39 And I think we need to do that, and I don't know how well CI works, but
In CPP, we do CI on… when a PR is merged.
So, whenever a PR is merged, we have a new breed, and because we have
a lot of changes. We keep up to date, and we notice when the platform has changed, or things like that.
In CPP contrib.
The setup is pretty much the same, except that there are no merges. So, a contribib may go without a merge for a long time, and CI is never executed for a while.
So, if, say, if GitHub retires some OS, saying, oh, Ubuntu, this version is removed, and then you need to upgrade to that version, for example.
We don't even notice.
So, if we have something to build everything, I think we… maybe there is a way to not trigger CI on pushes, but also, say, do a full build once a week, for example, to make sure that everything is still fine, and that will be…
That will help a lot, because then we will detect anything that breaks when it happens, and not 6 months after that.
**Doug Barker** 29:04 Yeah, that sounds doable.
**Marc Alff [MySQL]** 29:06 Yeah. And speaking of the YAML project.
for the contribib, now that we… as you remember, people can contribute their own, plugins to the… to the YAML file, so…
whenever that is done, we will also need to build… well, to adapt the CMEC files to provide builders for the YAML configuration file in Contrib.
**Doug Barker** 29:35 So we need to have a working CMake then.
**Marc Alff [MySQL]** 29:37 to do that.
**Doug Barker** 29:41 Yeah, I'd imagine if we had a unified, like, approach to the build system and contribute, people would probably contribute a lot of stuff there. It's just a lot of overhead now. If you want to contribute, you have to come up with your own CMake project.
**Marc Alff [MySQL]** 29:54 Yeah. By the way, when I reviewed that a long time ago, all your CMake changes, I didn't fully understood how useful all the install tests were, but I just found out what they test and what they cover.
with a YAML project, and it's really…
A good thing to have, so thanks for that.
**Doug Barker** 30:16 Of course.
**Marc Alff [MySQL]** 31:09 Nikhil, anything you want to discuss?
**Nikhil Bhatia** 31:13 No, Mark, nothing from my side.
**Marc Alff [MySQL]** 31:16 Okay.
I'm asking because I'm… after a while, I'm feeling lonely speaking, alone.
I'm not sure if Llit can make it, so maybe we can discuss further thing with, one time.
Runtime context data, because it's,
we need this knowledge to see how this part works. Just so you know, this is about this discussion.
the…
Currently, we have only one type of runtime contact storage, which is implemented, which is using free local storage.
So it works, it's the default one, and everyone is happy with it, mostly. There are some use cases to define a different kind of runtime contact storage. Typically, this happens for people who want to implement, say, their own thread pool, or things like that.
Because with a fad pool, there are some…
Additional complexity, and you need to do special things when…
When your task, goes from one worker to another, and things like that.
So… We need… basically, the issue here is that we need to make sure that the interface we provide
Especially with the token, and the context, and the runtime context in general.
Is enough so that people can implement their own runtime contact storage if they want to.
And because we don't have examples of how to do things differently, we don't know for sure if…
everything is possible or not. So this is the part to discuss.
But, it's a discussion of its own, so it will take some time.
Doug, I don't know if you noticed, but, Owen is also making some changes to, CMake related to Protob.
**Doug Barker** 33:54 Yeah, I haven't, taken a look at this yet. It looks like it's still in draft, so maybe…
When he's done, he'll, change it.
**Marc Alff [MySQL]** 34:02 Yes.
Well, actually, the title is seen draft, but I don't… is in draft, but
The PR might be ready for you, I don't know, unclear.
**Doug Barker** 34:14 Oh, God.
**Marc Alff [MySQL]** 34:15 And, in any way, does his shoes of its own.
And yeah, I didn't fully grasp the problem, but it's… this is related to building the audible buff library, and whether we build the static library, the shared library, both, and the combination that goes with it.
**Doug Barker** 34:38 Yeah, I'd have to look. I think this gets into the challenges with DLLs on Windows, right? I don't know if…
**Marc Alff [MySQL]** 34:44 Oh, yeah.
**Doug Barker** 34:46 supports DLLs on Windows, so this may be… Yeah.
**Marc Alff [MySQL]** 34:52 larger.
**Doug Barker** 34:52 this year, bro.
I can take a look.
**Marc Alff [MySQL]** 34:55 Yeah, well, DLL on Windows are a larger issues… issue, and there is also an issue still on Windows with,
open telemetry.
Basically, we have singletones in the… in the API.
which is working… Yeah, those things. So, we have singletons which are working everywhere, except on Windows.
And we still don't have a working solution for that.
This has been something… Plaguing the code for, like, at least 2 or 3 years now.
But this is a… This is unrelated to the port of buffed itself.
It's a… it's another place.
**Doug Barker** 35:54 Yeah, I haven't personally looked into this, Windows singleton issue.
Cool.
**Marc Alff [MySQL]** 35:58 Oh, it's…
Okay, so yeah, I will… so, Duke, I will probably,
do another PR for the TS changes in the YAML config.
So, when you have a chance, please take a look.
**Doug Barker** 36:28 Okay.
**Marc Alff [MySQL]** 36:29 And, I don't have… I don't have anything else at the moment.
**Doug Barker** 36:37 Sounds good. And Nikkel, I'll… if Lillette doesn't give you feedback by, say this Sunday, I'll take a quick look at your PR, but I probably won't have time until the weekend.
**Nikhil Bhatia** 36:48 Yeah, sure, thanks. Thanks, Doug.
**Doug Barker** 36:51 Yep.
**Marc Alff [MySQL]** 36:52 Okay, and…
I'll try to take a look as well. There are just too many things cooking at the same time, so…
Time is, the resource which is missing the most for me.
**Doug Barker** 37:08 Let's get some time back.
**Marc Alff [MySQL]** 37:10 Yes.
Nikhil, any… anything else you want to discuss? Or do?
**Nikhil Bhatia** 37:17 No, not from my side, Mark.
**Marc Alff [MySQL]** 37:20 Okay.
**Doug Barker** 37:21 Welcome.
**Marc Alff [MySQL]** 37:22 And, so, yeah, so Duke, I hope you're,
You're all settled down on, you said it was Boston on the East Coast, or…
**Doug Barker** 37:29 Yeah, yeah, in, Boston, North Reading. In Boston.
**Marc Alff [MySQL]** 37:34 Okay.
**Doug Barker** 37:37 Yeah?
**Marc Alff [MySQL]** 37:39 Okay, well, nice to see all of you, and
I will close the call now, so thanks for joining, and see you soon, online or at the next call event.
Yeah. See you. Bye now.
**Nikhil Bhatia** 37:57 Thanks, Marge. Thanks, Doug.
