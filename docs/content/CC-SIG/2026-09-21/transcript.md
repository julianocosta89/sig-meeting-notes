SIG: C/C++ SIG
Date: 2026-09-21
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Nikhil Bhatia** 01:26 Hi, Doug.
**Doug Barker** 01:28 Hey, Nikhil, how are you?
**Nikhil Bhatia** 01:30 I'm doing good. Our new…
**Doug Barker** 01:33 Pretty good.
**Nikhil Bhatia** 01:37 Yeah, actually, I've provided the overview for that PR.
Totally.
It's the privilege.
**Doug Barker** 01:47 Okay.
You know, We'll take a look, I haven't had a chance to look at it yet.
I appreciate that.
**Nikhil Bhatia** 01:57 Actually, now I understand that It takes a lot of time to review PRs.
**Doug Barker** 02:08 Yeah, and some change more and are more complex than others, for sure.
**Marc Alff [MySQL]** 02:17 Hi, everyone.
**Doug Barker** 02:19 Hey, Mark.
**Nikhil Bhatia** 02:20 Hey, Mark.
**Marc Alff [MySQL]** 02:33 Does anyone know if Tom and Larita are joining tonight?
Or today?
**Doug Barker** 02:41 I don't know.
There's no, I post in Slack, so…
**Marc Alff [MySQL]** 02:48 Okay.
Okay, so, I'm sure you have noticed, but, what's the name of Attula?
Razor tool which is, updating dependencies… which has been enabled in OpenTelemetry CPP.
Oh, oh, renovate, that's it.
So, Renovate is up in CPP, as well as, CPP BuildTools and CPP countries.
And we have been… quite a few, PRs just to keep dependencies up to date.
So I'm not sure if you noticed or not.
**Doug Barker** 04:04 Yeah, it's making, a lot of PRs, I was… And if we, what the cadence is, but maybe we either slow it down, or…
**Marc Alff [MySQL]** 04:13 Well… To tell you the truth, we are starting from way back.
So, this is very few PRs, because we were very out of date.
But I expect this to slow down once we are, accrued again.
**Doug Barker** 04:35 Makes sense.
**Marc Alff [MySQL]** 04:36 So… CPP is almost okay, and Well, CPP Country B is far behind. Still struggling to get the CI working again.
So, this was the… The major news, news from my side.
**Doug Barker** 05:22 So, I can share my screen, unless you want to, Mark.
**Marc Alff [MySQL]** 05:26 Please do.
**Doug Barker** 05:40 So maybe the first thing, talking about versions, do we need to update Weaver or do anything for this one?
**Marc Alff [MySQL]** 05:47 So, not quite. Weaver is the tooling which is used to generate cementing conventions.
So… If reasonable to wither alone, I don't think that will change the output of semantic conventions, unless there is a bug, say, that forgot to generate something.
I guess we take… we need to wait until there's a new release of semantic conventions, and then we can generate the new release of semantic conventions with the new release of Weaver. This is typically how it goes.
**Doug Barker** 06:24 Totally.
**Marc Alff [MySQL]** 06:25 So, no action today.
I did not check the release notes, But on the far-off possibility that there is a bug there that forgot to generate something, we might, but it's… I guess it's safe to just wait for the next release anyway.
Of 70 conventions, I mean.
**Doug Barker** 06:49 That sounds good.
I should have forgotten in Detroit?
**Marc Alff [MySQL]** 06:55 Okay. Yeah. Just a question for you. Have you tried to generate semantic conventions?
**Doug Barker** 07:02 Not for OPTel CPP, but I have for my own applications, trying to, create schemas and use it there, so I'm becoming familiar with the For creating those templates.
**Marc Alff [MySQL]** 07:15 Okay, good.
**Doug Barker** 07:20 Are you using it in your application?
**Marc Alff [MySQL]** 07:23 In mine, no, we don't have… we don't have specific semantic command trains. The only place I'm using it is in CPP to, to keep things up to date.
**Doug Barker** 07:33 Okay.
Yeah, makes sense.
Alright, so we can take a quick look at the ones that are open for discussion. I think some of these are still… over from last time. The one that I added was this one, because a contributor added a PR to Make these the same.
**Marc Alff [MySQL]** 07:56 Yes.
**Doug Barker** 07:57 So my comment on that…
**Marc Alff [MySQL]** 08:05 Well, I saw that it was going mostly backwards.
**Doug Barker** 08:08 Yeah, so it's like downgrading some things, but then also… you know, I don't even… you know, the case I'm trying to make is I don't think, because all of the Bazel dependencies are in BCR and we don't have control over that, that,
**Marc Alff [MySQL]** 08:20 Yes.
**Doug Barker** 08:21 we should allow them to diverge, and that's just gonna have to be what we accept, but the goal would be to always release with the latest that we can, and certainly Renovate would do that for Basil.
But then, in CMake, that's manual now, but we would always try to release with the latest.
Versions of the dependencies, so we get the security fixes.
Silver now.
**Marc Alff [MySQL]** 08:46 Yeah, so… overall, I mean, CMake and Bazel are different beasts, and we depend on packages which are… Shipped and delivered at different times anyway, so… Trying to be exactly in sync is our place, I think.
The best we can do is try to keep up with, with both, flows.
So… If Bazel provides a new package, yes, we should take it, and if CMake has a new package, we should take it.
But expecting it to be on the exact same version, I think is totally okay as, because there is no way to synchronize these, anyway.
If I recall from way back when, The original bug defect.
Was not so much about the versions, which is one thing.
but also on the different libraries, like, sometime, like, how come in CMake we have one library, say, for traces, and in Bazel we have two?
Or things like that. So it makes things a bit odd and more difficult to maintain.
So, for traces, it might be okay, but I think we have some discrepancies around common things.
And, the internal logger, for example, where in CMake you have maybe one library, and in Bazel you have different, different files which are built, one by one, and not put together, so there.
There are small things like this, which are, They're not necessarily wrong, they are just different.
which, makes it harder to maintain.
**Doug Barker** 10:39 I see, so you're saying that the libraries that we deliver are different.
**Marc Alff [MySQL]** 10:43 Yes.
**Doug Barker** 10:43 between CMake and Bazel, so, like, the actual, shared libraries of the targets that are generated.
**Marc Alff [MySQL]** 10:50 Well, technically, Bazel doesn't deliver libraries, but it has dependencies, and the dependencies are not taken on the exact same thing.
But, so, yeah, this is something we may… may want to fix to… Streamline the process, but it's, it's very low priority compared to everything else.
**Doug Barker** 11:14 Okay. Should we have an issue for it? I don't fully, I guess, grasp the issue that's different from this one, but we need a ticket for it.
**Marc Alff [MySQL]** 11:23 I thought we had one, but I don't remember it.
**Doug Barker** 11:27 Okay.
**Marc Alff [MySQL]** 11:27 I think I raised something like that in the past, so if you look at issues raised by me, maybe there is one.
**Doug Barker** 11:35 Okay.
Are you okay, then, with this particular issue, if I close it and the PR?
As, as wanted, as wanted.
**Marc Alff [MySQL]** 11:47 Yeah, totally fine.
**Doug Barker** 11:48 Okay.
Alright, I'll, after the meeting.
Let's see, I think we talked about the… or we did talk about the exception handling last time.
I don't know if there's anything else to follow up here, Owen.
**Marc Alff [MySQL]** 12:15 Yeah, I failed to comment on it and ask, some feedback from Mo, and so I don't know if he… Oh, yeah, I should… I should read that, Fred, but Yeah, nothing… nothing newer from my side. We need to… To decide what to do with it.
**Doug Barker** 12:37 Sounds good.
This one is still discussing it.
Ties to the, PR that you reviewed.
Nikhil?
Do you want to share what you learned on this one, or if you have any additional feedback?
**Nikhil Bhatia** 13:05 No, Doug, that was the only feedback I could provide.
**Doug Barker** 13:12 Okay.
So for this one, from your point of view, I guess, except for the CI failures, do you think it's okay to approve?
**Nikhil Bhatia** 13:32 No, Doug, actually, I felt that, There is, the metrics are being duplicated over here. I feel it can be, efficiently, managed more.
Actually, I was trying out it by myself, but I couldn't do it.
I was planning to do it, but time went by.
I think it needs some more review.
**Doug Barker** 14:08 Okay. Is your concern different from this one that Conserve it as resolved.
**Nikhil Bhatia** 14:15 Yeah, yeah, my concern is different from this.
**Doug Barker** 14:17 Oh, okay.
**Nikhil Bhatia** 14:18 So, metrics are being stored, two times at two different places in this PR.
So, I was looking at that part as well, but I did not put any comment as a…
**Doug Barker** 14:31 Interesting.
Alright.
We'll keep iterating on it. Thanks for the review.
It's very helpful.
**Nikhil Bhatia** 14:40 Thanks for giving me an opportunity to be…
**Doug Barker** 14:46 Well, we have plenty of opportunities. We've got… how many opportunities? We got 50.
**Nikhil Bhatia** 14:53 I mean, it was a very time-consuming process.
**Marc Alff [MySQL]** 14:59 And this was just for one PR. Just imagine, switching from one PR to the next on a totally different subject.
This is very taxing.
**Doug Barker** 15:14 Okay, so as far as discussion goes, I think that's all the ones that So I'll close this one out.
We'll, resolve that one.
We'll probably take a quick look at what needs to be triaged. I think most of these are all from… one contributor on Curl.
**Marc Alff [MySQL]** 15:31 Yes.
**Doug Barker** 15:31 Yeah. So there's…
**Marc Alff [MySQL]** 15:32 So, 20.
**Doug Barker** 15:33 or so from them. I don't really know what to do with these, because I think that there's also a redesign in, you know, in question.
**Marc Alff [MySQL]** 15:40 So… So, yeah, so she has been, begging… begging the girls' school to death.
Which in one way is a good thing, because she found a lot of things which all seem valid.
She also provided some fixes, which have been approved and merged.
But given the number of those, the overall question is, okay.
Basically, we need to step back and assess, is the core code today stable enough and fixable, or should it be rewritten from scratch, basically?
And I'm not sure, so… I didn't look in details in the redesign discussion.
The concern I have is, Even assuming, okay, we do… To do redesign and, And implement that would be any differently.
The question becomes, can we really do it, and what we do in the transition time… in the meantime for the transition?
Because… What we have is, somewhat working.
There might be flows, there might be risk cases, things like this, but at least it's working today, and Maybe not perfectly, but it's, It's working for main use case.
If we start to do a redesign and re-implement that.
My concern is that it will take time to… Pollution get to a stable state.
And… The question becomes, what do we do in the meantime, in the transition?
So… Not quite sure. Obviously, we have a lot of things to fix.
One thing to assess is, is the current code that we have feasible, bug by bug?
So that we are… we feel confident that we can eventually, make it right.
Or is it so bad that, we need to do it again anyway?
And I don't know the answer to that.
**Doug Barker** 17:51 the… Okay, maybe, one small step forward we can take, because I know that there is a… I think it's a PR with a design document. It's just a… I'll ping the contributor and ask if… All of these issues.
One, I think some of these are maybe not specifically related to CURL, but most of them are. I haven't gone through all of them.
**Marc Alff [MySQL]** 18:13 Yeah, I think, I think both of them are.
**Doug Barker** 18:16 Okay.
So I can probably just ask her which of these would be still valid after a redesign, and… Maybe that… then we can focus on… on the ones that, a higher priority, but yeah, it's… It's hard to go through all 20 of them.
Okay.
This one's been up for a little while, I don't Marc if you've had a chance to look at it, it's an interesting, question, so…
**Marc Alff [MySQL]** 18:46 Yeah, so I did, but I think I misunderstood the question at some point.
**Doug Barker** 18:51 Okay.
**Marc Alff [MySQL]** 18:52 So, my first impression was.
okay, we are using OpenTelemetry CPP, and we are using the Prometheus Exporter, and cool scanning for us raised this and that.
And that was my initial understanding.
But… I'm not sure this is the case. I think, the question is more like, okay, we are using OpenTelemetry, we're doing a scan on top of that to see if it's secure or not, which is a good thing and a good practice.
But… I'm not… I don't quite understand if… Which came first? Is it they came first with a decision to pick an exporter in particular, like Prometheus?
And then did the code scanning on that. Or, if they did the code scanning first, and then decided that, oh, no, it's a nightmare, therefore we are not using OpenTelemetry.
Yeah, because it's a bit of a chicken and egg situation, like… Yes, we have different exporters, but say, if you're only using the TLP exporter, for example, any security issues in the… Prometuous exporter doesn't… don't apply to you, and same thing for… Zipkin and whatnot.
So… I don't quite understand the… What was the… The process and the decision tree there.
What we are doing internally… is, in my application, We are only using a few exporters, not all of them.
And what we do is, to be able to build without internalized access anyway, we do import all the code from OpenTelemetry inside our Git branch in a third-party directory.
And this code is trained from… all the exporters we don't use are trained out.
So… we build only with the exporters we need, plus, of course, the core SDK.
But then, every code scanning that happens is only scanning code that we do use in your application, not… it's not scanning code which is there, but not even used.
And that simplifies things.
**Doug Barker** 21:25 That makes sense. Yeah, this sentence says that their tool is flagging the presence of files in the source tree, not the binary. So… it could be that we don't know yet if they're actually using Prometheus, or because Prometheus is a Git submodule, and then CivitWeb is a Git submodule of Prometheus, that it's just being pulled in into their build in source, and then getting scanned as a result.
**Marc Alff [MySQL]** 21:51 I mean, I can see their point of view, I mean… When you depend on a package.
Okay, so you have your code in your source, and you scan it, but… you need to make an extra effort to decide, oh, there are optional features there that I don't need.
Therefore, I can curb them.
Before doing the code scanning.
And if you don't do that, you end up scanning all the dependencies of every single exporter known to be implemented, which is a nightmare.
Because it will go… you will have, OTLP, Zipkin, Prometheus, Jaeger, we had Jaeger in the past, and we had also some Z page and whatnot. I mean, you can have all sorts of zoo.
That will not be part of your application, but which are still flagged by the code scanning tool.
And… on the other end of the spectrum, I don't see what we can do.
Because… We have optional compile flags, so you can take the source code of OpenTelemetry and compile with or without such and such and such exporter.
But the code is still there.
If you scan from source.
And I don't see us delivering packages with only the source code for this, and only the source code for that, and all the combinations. That will be… More complicated as well.
**Doug Barker** 23:33 Makes sense.
One thing, as you were talking, I was thinking about them maybe missing outside of just looking at, like, the CMake file or the Bazel files, I don't think we have documentation that says what What options exist, and how to toggle things on and off.
So, we could… That might be one thing that we can actually do.
**Marc Alff [MySQL]** 23:56 Yeah, we do have that in CMake, but if we are just scanning the source code present on the file system, even if CMake says, well, we are not using that thing, the code scanner will still see the files.
like ATW, I mean, we are not using the ETW exporter, therefore we are just removing that directory. But if it still stay there… Or, suddenly, you have a code scanning, picking up code from platforms, in our case, that we don't even use.
**Doug Barker** 24:35 Yeah, I've got a separate thought on that, which is to get rid of the Git submodules now that we can fetch the source from CMake with fetch content, but that might be one… another avenue to pursue.
So that we no longer have Git submodules, and then this problem would go away entirely, because you would only get that source code if you, Turn on that feature in that case.
**Marc Alff [MySQL]** 25:09 Okay, so… I guess the answer for this, this issue is to explain that they probably should Trim down the code.
To only scan what we are actually using.
**Doug Barker** 25:24 Yeah.
**Marc Alff [MySQL]** 25:25 To get a better picture.
But that, again, this assumes that they know what they are using first.
As opposed to scan everything, and then, based on the scanning, decide what to use.
But yeah, it feels like… especially… it's not so much third party, it's fourth party and more, like, I just saw something like Lua, I don't even know where Lua is coming from in the whole picture.
It's… Yeah, if you don't want Lua in your binary at the end of the day, you need to cut at some point.
**Doug Barker** 26:09 Yep.
Are you, are you generating a software bomb for your project, Mark?
**Marc Alff [MySQL]** 26:21 The, the what?
**Doug Barker** 26:22 The bill of materials, the software bill of materials.
**Marc Alff [MySQL]** 26:29 We are looking at it, but we don't… I don't think we generate that formally, but we're looking close to it in any case, yes.
**Doug Barker** 26:42 Yeah, it's another that we can look at trying to do, too, as a project. It's always difficult because there's so many options, but…
**Marc Alff [MySQL]** 26:49 Nice.
**Doug Barker** 26:49 Okay. I think, this one's clear that, you know, obviously we can't fix Civic… Civet Web, or… You know, even own…
**Marc Alff [MySQL]** 26:58 Reporting on this.
Yeah, we can, by dropping Prometheus.
But it's not something we are going to do, so… But the thing is, so we cannot drop permetus, the user can, if choosing not to use it.
Yeah. And this is the fine line, Bill.
**Doug Barker** 27:22 Okay.
Alright, I'll take a look at that one after the meme and just make a comment.
And we can mark it as, needs more information, waiting on them to…
**Marc Alff [MySQL]** 27:33 So.
**Doug Barker** 27:34 Totally.
**Marc Alff [MySQL]** 27:34 by the way, some disclosure, so, do you… What my application is?
**Doug Barker** 27:43 No.
**Marc Alff [MySQL]** 27:45 Okay. Well, it's public now because we just disclosed the telemetry component, so it happened to be MySQL.
**Doug Barker** 27:54 Oh, it matters.
**Marc Alff [MySQL]** 27:58 Yes.
**Doug Barker** 28:00 Is there a… Repository with that?
**Marc Alff [MySQL]** 28:04 Yes, there is a repo on GitHub, and that contains very open telemetry instrumentation.
**Doug Barker** 28:09 Okay, cool.
**Marc Alff [MySQL]** 28:11 But yes, so because of that, we are very closely looking at dependencies and what can or cannot be in the binary.
**Doug Barker** 28:23 Nice. It's very relevant.
Okay, Yeah, we don't have to go through all these, but here's another relatively recent one that came up.
Are there any PRs that you guys would like to go through?
**Marc Alff [MySQL]** 28:42 Yes, there is one, but it's in the CPP country report.
I forgot his name, but, someone… Yeah, Tomson Tomo.
He did some… a lot of… well, he did a lot of cleanup to… Enable, renovate, first of all.
And also, he's working on fixing, make files so that we can have, CPP Country, building again.
And there is one PR in particular which is doing some cleanup, in, both the Prometheus exporter and the web server, I think?
No.
**Doug Barker** 29:30 I think I'm personally.
**Marc Alff [MySQL]** 29:32 Oh, you merged it already?
**Doug Barker** 29:34 I think so.
I feel…
**Marc Alff [MySQL]** 29:41 No.
You're looking at your closed one, so… Oh, this one, yes, okay.
**Doug Barker** 29:47 Wow.
Yeah, so there were still some failures, but he was able to disable Remaining filling ones, and then, log the tickets so we can track them.
**Marc Alff [MySQL]** 30:00 Okay, so, yeah, that was my main point. So… the state is so bad there in CPP country that The first step is to get the cold building again.
Which achieved.
And… sorry. And the next part is to actually, once we have a good building, to look at CI itself and make sure that the test pass.
But we're… we are coming from so… We are so far behind.
But I think we should, Take smaller steps, as opposed to try to solve everything at once. And in particular, just try to get the call to build.
Especially… so, the reasoning is that the dependencies also are so old that we need also a lot of renovate updates to keep the code up to date with all the dependencies.
So, building is only the first step to get there.
And yes, you also identified a lot of things which are failing today.
**Doug Barker** 31:09 Yeah, I think we're getting… we're getting close, so we still have… probably the most important one, which is this CodeQL job needs to get turned back on, and then the one that didn't get finished from the last one, last Prometheus fix we just looked at was this one for, Linux.
And baseline.
**Marc Alff [MySQL]** 31:25 So… For the first one, for the CodeQL thing, So there is code QL, but there is also scenic format and things like that.
I think I saw a discussion somewhere that, all the formatting code that we have should also format not only CC files, but also CPP files.
Which are currently ignored.
And likewise, not only .h for other files, but also .hpp, So what do we get formatted as well?
So, for that, we will most likely to do some minor change in the CPP build tools.
repo.
Just to adapt the script which is running silent format.
But also, after that, We need to do a new release of the CPP BuildTools repo.
to have a new Docker image that can in turn be used in the CI for both CPP and CPP contribute.
The whole thing with that story is that I think we should have Well, we should use the same Docker image to do all the formatting.
Otherwise, we will end up with, oh, one script in one repo doing formatting one way, another script in another repo, doing formatting another way.
Which is, cruising chaos and, causing some… also some, Some maintenance issues for maintainers, because you have to apply the proper formatic strip for the proper place, and it's, Yeah, I don't think it's worth it. If we can have a single… a single document that knows how to format, period, that would be, Bonsai pour.
**Doug Barker** 33:23 Yeah, I agree.
So, I think it seems like then the next step is to change that script to add these.
**Marc Alff [MySQL]** 33:32 Yeah.
Awesome.
Yes, yes, but…
**Doug Barker** 33:39 And I was looking at this the other day, and I know that the CI for OpenTelemetry CPP and the dev container is using the local script, so there's also a formatting script, which I think is essentially the same as.
**Marc Alff [MySQL]** 33:53 Yeah, well, it's…
**Doug Barker** 33:54 It's.
**Marc Alff [MySQL]** 33:54 It is the same today, but if we change it for those new file extensions, it will diverge, so we need to be careful of that.
And by the way, I saw that also in the dev container, you changed the Dockerfile to use Ubuntu as a base, and install the selling format scripts on top.
Which is good, but we need to be careful also not to diverge from the formatting sweeps in the CPP build tools.
**Doug Barker** 34:26 Yeah, I think what we could do in the future is just copy the Copy the script, or the… build from… format tools image when we create the dev image. The challenge I ran into is that this, CPB format tools Docker was updated to 2604, and then that was causing, CMake to be implicitly upgraded to 4.0, and then that was causing those.
**Marc Alff [MySQL]** 34:50 Oh, boy.
**Doug Barker** 34:51 whole point tracing to, fail, so I switched it back. Yeah.
**Marc Alff [MySQL]** 34:55 Yeah.
Well, this is… Welcome to Dependencies, I mean.
as a recently.
**Doug Barker** 35:05 Yep.
But yeah, I agree. We can standardize on this and just do this simple upgrade.
For these two file types should be fine.
**Marc Alff [MySQL]** 35:18 Yes.
**Doug Barker** 35:22 Okay.
Anything else you wanted to look at in?
CPP contribute.
**Marc Alff [MySQL]** 35:29 In contrib, not particularly, Oh, so just a word on Bezo.
So, well, first of all, the very first time I heard of Bazel was when I joined OpenTelemetry.
And that was a very weird thing to me, and never heard of it before.
And I'm still learning.
This is really a strange beast. So, recently, in CPP, we had a lot of… So, not dependable, but, not really innovate, but before that, dependable, and some updates failing.
Okay, try to update, Absol, it fails. Try to update gRPC, it fails. Try to update PolyPerf, it fails, and so on and so on.
And… while using Renovate, Renovate also suggested that, yes, we should upgrade all of that, upgrade all of that, but also.
On top of that, we should upgrade Bazel itself.
And that was the thing that, unlocked everything, because Bazel did a major change related to packaging.
Especially with the infamous compatibility level flag that was supported earlier and has been abandoned now.
That was causing chaos between packages. So, the fact that we just recently upgraded from Bazel 8.5 to Bazel 8.8, basically unlocked all the upgrade trains from Renovate.
And this is not the kind of things that you… I mean, it's hard to tell. I mean, there's no way to find out. You really need to dig into all the risk notes and whatnot to find that, oh, yes, it's due to this issue, which is fixed in this release, and blah blah blah.
So, now that we are on… we are on Bazel 8.8 in CPP, packages are flowing again, and we recently… upgraded, gRPC, APSOL, autobuff, and maybe a couple of other things, to something very, very recent.
So, this is for CPP, I think we need to do the same thing for CPP contribute as well.
So, there is probably a couple of PRs to come to upgrade all that.
But… We'll probably need some, To do that will permit some changes into the different modules, for Bazel and things like that.
**Doug Barker** 38:21 Yeah, that's interesting, because these might also be on the old-style basil, not Basel mod, I don't know.
**Marc Alff [MySQL]** 38:26 Yeah.
Or maybe they don't…
**Doug Barker** 38:30 Any Bezos support could be tough.
**Marc Alff [MySQL]** 38:35 And also, depending on the version of Bazel you use, it's not looking at the same files. Recent Bazel used a module, older things use something else, so it's a… It's basically a… a maze.
**Doug Barker** 38:53 One thing I was actually thinking about was to, you know, we need a contributing policy here, and we need some… probably some better organization so that, at least in Seamating, you know, everybody's not recreating all the installation and packaging, you know.
Scripts and everything within their own contribution.
But we could also, as part of the contributing guide, just say that it's only CMake, and we don't support Bazel, you know.
For these contrib components.
Looks like a lot of them.
**Marc Alff [MySQL]** 39:27 It depends on who is using it.
**Doug Barker** 39:31 Yeah.
**Marc Alff [MySQL]** 39:35 Nikhil, I don't remember, but are you working for Google?
**Nikhil Bhatia** 39:40 No, no, Marc.
**Marc Alff [MySQL]** 39:42 Okay.
Because, well… from my understanding, Basil… it's a tool which is not widely used in the industry, but it is extremely used by Google internally, so… any… anything related to Google will most likely insist of having not only a CMake build, but also a base of build.
I mean, once it's working, it's okay. It's just… it takes a lot of work just to demangle CMake, and after that, to demangle Bazel.
**Doug Barker** 40:24 Yeah, I'm just kind of poking around here, it looks like.
Most of them are CMake only.
**Marc Alff [MySQL]** 40:30 Yeah.
**Doug Barker** 40:31 Hello.
**Marc Alff [MySQL]** 40:34 Yeah, so on top of that, yes, it may… it may vary between different contributions.
**Doug Barker** 40:40 Like, this is probably the… this web server is the heaviest one, and it's using pure makefiles, too.
**Marc Alff [MySQL]** 40:47 Yeah.
**Doug Barker** 40:51 So… Okay, maybe it's not… was there a particular project that you were concerned about, or file, that we should upgrade?
**Marc Alff [MySQL]** 41:02 No, not really. So, not knowing anything about Renovate, I was pleasantly surprised by the work of, tomorrow.
Because, from a user point of view, I mean, looking at any… so, can you back to the… go back to issues in the CPP configure repo?
There should be an issue, yeah, the dependency dashboard, which is pinned.
Yeah, so… This will list all the action that Renovate wants to take, to upgrade things, and from a user… usability… sorry, usability point of view, it's actually quite nice.
Because you just click on a thing, it just gives you a PR. Of course, the PR will fail, but at least you see what it tried to touch.
And, can work from there.
It's much nicer and much more efficient compared to dependable earlier.
Which did much less than that.
So… For CPP, this weekend I did quite a few PRs just to upgrade things, and it went somewhat okay. The trick was to find the proper upgrade path and find things that we needed to fix to unblock that.
But otherwise, it's, overall, it was working great, so I'm hoping that we can… we can do the same for CPVCon trip.
In this case, in this case, you can tell that the CPP control repo is way old.
I mean, we have a contrib… we have a contribib depending on CPP116, Today we are at 1.29.
So, it tells you that this country has not been updated for ages.
**Doug Barker** 43:06 So how… how, are we managing this? Are you just coming in here and check… I guess as soon as you check… check the box, it will create a PR? Is that how it works?
**Marc Alff [MySQL]** 43:16 Yes.
**Doug Barker** 43:17 Okay.
**Marc Alff [MySQL]** 43:18 It will… it will do what it can, so sometimes the APR is okay, sometimes it needs some work, sometimes it will fail because there is a blocking issue.
So… had two blocking issues recently. One is, what you have seen, and so I did a patch for that, that you reviewed.
That was an issue with, the examples in the configuration, YAML configuration.
For some reason, some examples binary were linked with Google Tests, even though they were not Google Tests.
somehow, magically, this worked with gtest 1.17.
Well… And by upgrading to Google Test 1.18, it broke.
Because the binary somehow, showed true men, when linking.
So, this is the kind of things, I mean.
It's… there's no way you can find this out before then. Either it works or it breaks, but sometimes newer versions of things can expose bugs which have been there forever, or that no one noticed. It's, It's always a bit risky, but once this was fixed, the upgrade to Google Test actually was good.
**Doug Barker** 44:44 Yeah, that sounds helpful. It is nice that it captures all of the upgrades, including the OS and the runners.
**Marc Alff [MySQL]** 44:51 Yes.
So, of course, we should not do everything.
like, things like upgrading, like, Ubuntu… All the recent releases, well.
what if we… we have a case in CPP, what if we want to test with older Ubuntu releases, or older macOS releases? We should still… Use all the things there.
**Doug Barker** 45:22 Is there a way.
That you know of to, tell it that you don't want to do? Like, if we just say we don't want to do this one.
**Marc Alff [MySQL]** 45:30 I'm not sure, but I think I saw that in other repos. Once you have a PR, if you close the PR, the tool will say, okay, you closed it, you denied… I mean, closing it without merging.
So they totally say, okay, you've denied this one, so I will not propose it again unless you change your mind.
Okay. So it will not try again and again.
**Doug Barker** 45:56 And I guess if we just click this one and just upgrade, like, straight to 128, then… These will all disappear once that.
**Marc Alff [MySQL]** 46:02 Oh, yes, these will all disappear, yes.
**Doug Barker** 46:05 Okay.
Yeah, that is helpful.
Do you have thoughts on how best to manage this? It sounds like you're… you're at least going through here and checking off, so I haven't looked at this at all. Should we just… whoever sees it, just come in and check on?
Check these.
Own it.
**Marc Alff [MySQL]** 46:30 I did quite a few upgrades first, the thing is to… Typically take one at a time, otherwise it's, it becomes complicated.
And takes the ones which are less risky, so that it clears, It clears the noise, basically, and… After a while, when doing well at a time, from what I've seen with CPP, it converges.
We should definitely not do everything at once, because some PRs will be conflicting with one another.
Like, if you upgrade to CPP20 or 21 at the same time, well, there will be a conflict between those two PRs, obviously, so we should not do that.
But it's really horrific.
**Doug Barker** 47:32 If the core repo that Dependabot is now disabled, Yeah, great.
**Marc Alff [MySQL]** 47:37 Oh my goodness.
**Doug Barker** 47:37 Okay. Okay.
**Marc Alff [MySQL]** 47:38 Yes.
And as such, I also closed all the pending dependable PRs, because the… Well, the tool being disabled, it was not responding to request to rebase or anything, so the only thing was to close the PL anyway.
And those were duplicated with, Renovate.
**Doug Barker** 48:04 And then this one, I think, is related, so you… you correctly called out that that Ubuntu 22 is being deprecated, so I think we're gonna lose access to it. They start to, like, brown, like, reduce availability for those, so we should get it switched over.
But then, james said that.
Renovate will handle it. I haven't been paying attention.
**Marc Alff [MySQL]** 48:29 Do you know?
**Doug Barker** 48:30 Renovate a salt bed, or maybe it's in a dashboard somewhere?
**Marc Alff [MySQL]** 48:34 Well, so Renovate can fix that. What it will do is find all the… over Ubuntu 22, and propose to upgrade to ever 2426?
But the question is.
It's a choice from us. Do we want to test only the latest, like, always 26, or do we want to test a mix? And in which case, we should keep some workers on 24 and some workers in 26.
And we have the same thing for macOS. I mean, you see that there are two PRs.
to upgrade to macOS 15 or 26, but they're touching the same files.
So… We can do one or the other, but not both at the same time.
So it's up to…
**Doug Barker** 49:21 tell Renovate which ones we want to pin, because I agree, we definitely want to keep testing multiple versions.
**Marc Alff [MySQL]** 49:30 Yes. So, In my understanding, well, so first we should, yes, take a look at CI and decide which worker works on which OS.
But after that, if Renovate proposed to upgrade, if we just let it raise a PR and close the PR, it will just forget about it for a while.
And only, so it will list the PR as denied.
or blocked, or I don't remember the name for that. And later, if you choose to, you can… Trigger… trigger the upgrade again, if you change your mind.
So, let's say if we try to upgrade to 26 and close the PR, it should say, okay, you… Decided not to upgrade to 26, so it's… It will stay there.
So, this is the first time I use the tool, but it's, it looks quite decent, actually.
**Doug Barker** 50:51 Yeah, I agree.
Oh, I see. So you're saying that it just blindly updates?
**Marc Alff [MySQL]** 50:57 Yes, but also on top of… Yeah, but typically, like, VPR, well… maybe we should also upgrade the names as well, so it doesn't say MAC14 and test with MAC15 at the same time.
So the PR may work, but it's, we need to be careful that… Not to blindly accept, because in that case, yes, the… The comments, the name of a target, and so on needs to be addressed.
**Doug Barker** 51:29 Yep.
**Marc Alff [MySQL]** 51:34 But at least the fact that it runs in CI, it tells you what needs to be fixed, and it also tells you if the PI is passing or not, which is very valuable.
**Doug Barker** 51:48 Yeah, I agree.
Let's take a look at please review.
Okay, yeah, we still have this… one from Tom.
**Marc Alff [MySQL]** 52:09 Yes, yes. And also, Lalit recently… Finish some work on metrics.
On neutral pier.
So we should take a look at it as well.
Boom.
I don't remember the name of it, but if you sort by PRs recently updated, you will find it. Or PRs from the ETS.
Yeah, this one.
It's all new thousand lines.
**Doug Barker** 52:55 In there.
Alright, we're almost out of time. Anything else?
**Marc Alff [MySQL]** 53:06 Not for me, just so… In the coming… Week… or weeks, I will mostly try to get Renovate up to speed so that we… We come back from the Dark Ages, and have some recent decent dependencies, so I will be focusing on that mostly.
And after that, I plan to go back to… Cleaning up the no-except warnings that we have.
That, plus all the duplications that we… said we would do after early October.
And so, Basically, in two weeks from now, we'll start to look at deprecation and clean up the code.
**Doug Barker** 54:01 Possibly.
Yep, so only category we have left.
**Marc Alff [MySQL]** 54:06 Yes.
Which is nice, because we come from way back when.
**Doug Barker** 54:14 Many, many hundreds of warnings, if not categories.
**Marc Alff [MySQL]** 54:17 Yes.
And keep in… keep in mind that this is only, Sit and tidy.
A couple of years now, I also… Went on the crusade of fixing, compile… compile warnings.
Which is where the maintainer mode was implemented?
And cleaning up all the maintainer mode's warnings in all the compilers was… also major.
**Doug Barker** 54:54 Okay. Yeah, we can…
**Marc Alff [MySQL]** 54:59 Yes?
**Doug Barker** 55:00 Oh, go ahead.
**Marc Alff [MySQL]** 55:02 Yeah, so, I'm quite surprised that the number of compile warnings actually stayed to exactly zero, so the enforcement is working for the build warnings. I'm hopeful that… So, for build warnings, the enforcement is working. For include what you use, it is also working.
And I'm hopeful that once we get ceiling tidy clean, we can also keep it at zero and enforce that.
So, which will be a… a major milestone, I guess.
**Doug Barker** 55:38 Yeah, that would be nice. And we can turn on some more checks and have more money.
**Marc Alff [MySQL]** 55:43 Perfect.
**Doug Barker** 55:49 Perfect.
Alright, let's check. I don't think there's anything else… through the PRs. Okay.
**Marc Alff [MySQL]** 55:59 I still need to file the issue on community to change the meeting date.
On top of that yet.
I'm trying not to forget it.
**Doug Barker** 56:12 Okay, yeah, no worries.
Once you get it posted, like, if you… Yeah, you tag, tag all of them.
Maintainers, and then we'll get the email.
**Marc Alff [MySQL]** 56:23 Yes.
Nikhil, anything else?
**Nikhil Bhatia** 56:31 Oh, no, Marc.
**Doug Barker** 56:36 Right.
**Marc Alff [MySQL]** 56:37 So, thanks for joining. I know it's mostly Doug and I talking, but at least we get a feel for all what's going on.
**Nikhil Bhatia** 56:46 Yeah, Mark.
**Doug Barker** 56:48 Alright.
Thanks, guys. Have a good evening.
**Marc Alff [MySQL]** 56:53 Yeah, thanks, everyone.
**Nikhil Bhatia** 56:54 Thanks, thanks a lot. Thanks, Doug.
**Marc Alff [MySQL]** 56:58 But…
