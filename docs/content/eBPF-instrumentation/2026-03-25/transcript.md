SIG: eBPF instrumentation
Date: 2026-03-25
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/WTmiG8tJi-uZl1TMerFwSr6EIVaQ4ASGxCr4f62U_w0bb992haWjJTWpLbhnqAxf.4C_0mUlNtkf6qY5P
============================================================

## Zoom Recording Transcript

**Giuseppe Ognibene | Coralogix** 00:19 Hi, everyone.
**Nimrod Avni** 00:21 Hello.
**Stephen Lang** 00:23 Hey.
**Nimrod Avni** 00:24 Fair enough.
No.
**Stephen Lang** 00:46 So I know Nicola's out, but Mario's here today, so he might join.
**Nimrod Avni** 01:01 I don't know who else has, I guess, Tyler and… Nicolor But… Be a small one.
**Stephen Lang** 01:16 Yeah, Raphael's not very well.
As well.
**Nimrod Avni** 01:18 Huh.
**Mike Dame** 01:36 Yes.
**Stephen Lang** 01:38 Fair enough.
**Nimrod Avni** 01:39 Hey, Mike.
**Stephen Lang** 02:02 Did anyone volunteer to drive the call today?
**Nimrod Avni** 02:06 Yeah, it'll be me.
I think it's gonna probably be a quick one, I guess I'll wait. Like, we'll wait a minute if someone else joins, I don't know.
I'm, like, Grafana for waiting for anyone, I guess it's only you.
**Stephen Lang** 02:20 Maybe not.
**Nimrod Avni** 02:21 Maybe Mark, and you said maybe, Mario, as well.
**Stephen Lang** 02:26 Yeah.
**Nimrod Avni** 02:27 I'll wait, like, a minute or something.
If you have any, like, agenda items you want to talk about?
Feel free to add them.
I guess I'll share my screen.
Yeah, cool, so I think we can start, probably be, quick one. I have a couple stuff I want to talk about, The first one, I think there was someone in the OB… Slack channel, and add, like, another… Colleague, came up, who came over and… kind of asked me how to get into Obi, and how to… start contributing?
So… at least for the guy on Slack, I told him, hey, a good place to look is good for issues.
And before that, we had, like, a lot of… a lot of those weren't tagged, with good first issue.
And I also told him, Like, also, like, doing, like, looking for some to-dos, or looking for some, like, fix-me's in the code, and also some, I'll try to, like, run Cloud or something and let him, give suggestions on, some minor stuff to do, like, I don't know, fix Explicit panics with, correct error handling and so on.
I just want to bring it up, so if… I think if anyone… Either, has an issue that, like.
Can be, something that's kind of small.
I think it's a good thing to, like, label it, as well as, like, if you see an issue.
someone else opens, and you think it would be kind of easy to solve, I think we can tag it.
And maybe add something in the… contributing MD file to, like, point out to these types of issues.
Yeah, I don't know. That was, like, something… I had in mind, unless you have anything else regarding how to get into the project, maybe updating, like, I don't know, Spell checks and, like, you know, misspells in documentation, or… Stuff like that will probably be the easy, easy stuff.
But yeah, I just wanted to bring it up if anyone has any ideas. If not, I can… Add a small note in the contributing MD file pointing to… These types of issues.
No?
**Stephen Lang** 05:25 Yeah, the other one I can think of is the… the test refactoring over to docker test.
I know that… And I think we reached consensus on that, I don't know.
But at least when… that is definitely what we're doing. There's probably going to be quite a lot of work to go and take the existing test suite and Move it over to the… you know, DockerTest package instead.
Maybe it's worth… Creating at least some issues.
So that somebody could, you know, pick it up, and we could maybe help distribute that.
Because it's effectively, like, the spec is already there, which is you just have to take the existing test.
refund, too, right?
**Mattia Meleleo** 06:09 I think, I have, something regarding that one. So, there was an issue with, the… how the Docker… containers were being initialized, and it was a bug in, I think, already Docker test.
Okay. Where staff couldn't, get initialized concurrently, because there was a race.
So I'm not sure, I think we should check how long does it take to boot up, big Docker Compose files.
Plus, that might be a performance issue.
Or, yeah.
Well, I know that, that, One second, I don't remember the name… I know that this issue is being worked on in Docker test.
So once a patch comes out for that, I think we can… We can proceed.
**Stephen Lang** 07:13 So I guess more generally, it's just if we have any large-scale refactorings, it'd be good to kind of make it clear and break it down as to, you know, what needs to be done and have Maybe, you know, one issue per package, or, like, have it such that it's Leo, for somebody else, if they were going to pick it up, what subtasks they might need to create, and how they could scope it if they were going to do some sort of refactoring.
And I don't know of any other refactorings that we have other than this Test 1.
Unless anybody else can think of any, that's… You know, clean up or a rework of stuff that we already have.
**Nimrod Avni** 07:56 I don't think, like, anything… maybe when we get to, like, the new config V2 stuff that Tyler's working on, I guess we'll need to kind of refactor stuff a bit, but until then, I don't know.
But I like your idea, maybe create some, like, epic slash, like, umbrella issue over all of that, and, like, split it up to subtasks for… Package per test.
And labeling all of them was like, okay, that's a good thing to start off with.
I… I like that.
**Stephen Lang** 08:29 Do we have an easy way for checking if we're… Compliant with the semantic conventions.
**Nimrod Avni** 08:37 I did last KubeCon, I remember, trying to integrate with, Weaver. There's, like, say, other… like, a Rust-based project that checks, semantic conventions. I did it in, like, a more… Integration-testy way, with, like, basically… Setting up OB, exporting.
data, I think it was, like, a Weaver daemon set, basically, that acts as a receiver.
And then, like, kind of compares it to the, auto schema.
But I think there's probably a way to embed it as, like, either in our integration test or, like, in unit tests or something.
And that might be a good thing to, like… because I think it supplies some, like, CLI to do it, but I think we can add it.
Once we get some, like, infrastructure in of, like, how to check it.
Like, we need to check… I guess… I guess we need to check, like, all of our integration tests, everything that we export.
We kind of need to hook it up as well to Weaver to make sure that we follow the semantic conventions.
Or in the, like, the traces gen, integration test, and the metrics one, and all that.
But yeah, once we… and I saw, like, a couple of… there's some, like.
Warn… you have, like, warnings, which is stuff that are, No, I don't remember. There was, like, specific errors of, like, keys that don't exist in the semantic convention, or that have been deprecated.
You also have some warnings of, like, you know, the pipe doesn't fit, you expect a string, you give it an end, some stuff like that.
Yeah. I think once we get some infrastructure in, might be also a good thing. I'll try to… maybe work it, and I'll open an issue for it at least, and then we can kind of fix it.
Step by step.
**Stephen Lang** 10:42 Awesome, thank you.
**Nimrod Avni** 10:45 Yeah, cool.
Yeah.
Mattia? Yeah, you want to talk about the kernel version coverage?
**Mattia Meleleo** 10:55 Yeah, we have, discussed this a little bit internally, just to tell others. I think we should, think of, Of a list of kernels we want to test on, because right now we are… testing, I think, on 5.15 and 6. And, and whatever GitHub decides the runner version is.
So, for example, today we, we had, login HR tests failing because there was a bug in, core relocation.
And it would have been nice to get that before GitHub updated the kernel in the runners.
So I think… I think we should start some kind of, issue or document.
Where… where we agree on a set of kernels we should, test on?
I was thinking, maybe we need the… the minimum version that we support, like 5.8.
We also need the latest mainline, or recent mainline, like 6.19, or I don't know what's the latest one right now.
And, maybe some, someone in… some kernel in between which, which is used in the LTS versions of Ubuntu, or the most, used, distros.
They can't be too many, of course, because, LCI would take, A year to run, but something.
**Stephen Lang** 12:36 Hold out.
**Mattia Meleleo** 12:36 Makes sense.
**Stephen Lang** 12:37 They'll all run in parallel, wouldn't they? Because we do one, One runner, one parallel runner per kernel at the moment.
So I don't think it'll take any longer, it's just that we'll be using lots more runners.
Yeah.
what was I going to say? So this could be… there's two things here. It could be an opportunity to move away from Alpine.
Because we still have this issue with the insecure proc effects.
we're, like, pinned to an older version of Alpine for these VM tests, because of this, like, nested virtualization.
Issue.
Which, if we're going to introduce, like, a bunch more kernels, maybe we shouldn't scale up the approach that we have at the moment, which is pinned an old version.
And that could be… that we could switch away from Alpine so that we could use, like, the latest And more secure.
**Mattia Meleleo** 13:34 Where exactly do we use Alpine? Is it in the Docker image of the testing image of Obi?
**Stephen Lang** 13:41 It's… I think it's on the file system of the kernel that we use, when we're deploying the QEMU VM.
So, like, we… there's two… the reason that we have those two specific kernel versions is because Raphael built those kernels manually and stored them into Git.
And then we… we run those kernels on top of the, like, same, like, alpine layer, because I think it depends on the… Alpine root FS layout.
**Mattia Meleleo** 14:13 Oh yeah, I wanted to add, maybe we need some kind of a kernel builder, like a bash script which fetches the kernel.
**Stephen Lang** 14:21 Yeah.
**Mattia Meleleo** 14:21 Source from.
**Stephen Lang** 14:24 That's a good idea.
**Mattia Meleleo** 14:26 Yeah, and with a config, it builds the kernels that we specify Somewhere, you know, at least.
**Stephen Lang** 14:34 Yeah.
Yeah, that would be good, because at the moment, I think they're… they just have been manually built. The configure file is in there, but you'd have to, you know, create it yourself.
**Mattia Meleleo** 14:44 Yeah, no.
**Stephen Lang** 14:46 So that's one thing. The other thing I was going to say is… For the issue that you picked up, where… the GitHub runners move to a new version. Like, if we have a specific list of kernel versions, we would still miss new kernels, unless we did something like, try and pick a kernel next, or something. We'd have to, like, rebuild kernel next.
every, I don't know, week, or something like that.
So that we're effectively using…
**Mattia Meleleo** 15:17 I don't think we should be that fast with updating. Maybe we can pick the latest major, for example.
**Stephen Lang** 15:26 Okay, but we need some ways for that.
**Mattia Meleleo** 15:28 Every month or two months, I think it's fine.
**Stephen Lang** 15:31 Yeah.
But it'd be nice if there's a way to at least list what that version is, and automatically update it. Like, we update the offsets automatically.
**Mattia Meleleo** 15:39 Oh, yeah, yeah.
**Stephen Lang** 15:40 Good to have the versions updated automatically as well.
**Mattia Meleleo** 15:47 Good point.
**Nimrod Avni** 15:53 Okay, yeah, I think it makes sense as well, like, to… I think, Pino, that's something… I don't know if it already emerged, or… You, we added it internally the, like, the, verifier.
Ci, I guess that's part of that.
**Giuseppe Ognibene | Coralogix** 16:09 No, no, it's not magic. Actually, I didn't open on Hobby, because there are 25… Failing…
**Mattia Meleleo** 16:17 Cheers.
**Giuseppe Ognibene | Coralogix** 16:19 So there are some combinations of constants that are not working.
No. So I need to fix this issue. I hope to solve it.
**Nimrod Avni** 16:31 Okay.
I guess we can, add it in addition to these, version coverage, kernels.
But yeah, that's a good point.
**Mattia Meleleo** 16:40 Also, I would build the kernels for both arches.
AMD64 and ARM.
**Nimrod Avni** 16:49 Yeah.
Makes sense.
**Giuseppe Ognibene | Coralogix** 16:51 Actually, I had a question.
why we don't extend, like, the number of kernel versions that we use only to load the BBBF programs? I mean, like, to run the integration test, we can use, like Mattia said, like, the minimum version, the latest stable version, and so on. But to load the program, we can… Increment the number, like a 10 or 20 version.
**Nimrod Avni** 17:26 We can, it's just, like, a question of… I think having both the verifier and… integration test running on the kernel is, like, a kind of big guarantee that it… we, Like, we say that it works on this, kernel version, and if you only run verifier.
I guess that's… that gives some indication, but I guess we… this can also miss stuff.
**Giuseppe Ognibene | Coralogix** 17:56 Yeah, but, I mean, in the opposite way, if, if we have a problem on a kernel version that is not in the integration test, at least we can, Find that there is a problem that can abression.
Using the verifier. If it's not in both, neither in the verifier test and in the integration test.
We… we are missing the… the girl.
**Nimrod Avni** 18:22 Yeah, I don't have a…
**Giuseppe Ognibene | Coralogix** 18:28 This is really, really fast. I mean, it's… just… Try to…
**Mattia Meleleo** 18:33 Yeah, I think we can do that. The thing is, We have to check, If we have to rebuild the full list, of kernels.
Every once in a while.
that if we have, like, 50 kernels, that will take a long time, but I think once we compile them once.
I think we are good to go. I don't know where to… where we should store them.
Do we use… 10FS, or…
**Nimrod Avni** 19:08 Where are the current, kernel… kernel store, and it's also.
**Mattia Meleleo** 19:12 They are in the repository, but we only have two.
**Nimrod Avni** 19:16 Hmm.
**Giuseppe Ognibene | Coralogix** 19:19 Can we use another repo?
**Stephen Lang** 19:21 Well, I was wondering, is… are there some pre-built kernels we can use? Is there, like, a… does somebody provide these somewhere? Like, an OCI?
repository, or… Has, has this already been done, maybe?
Because if we had something where the actions are quite lightweight and we're not storing the kernels in the repo, we could just download them from some trusted source, verify them with a checksum or something.
And then run them, instead of having to compile themselves.
kind of feel like this should have been done by someone else, I don't know if it has.
**Nimrod Avni** 19:58 Yeah, makes… makes sense. Maybe we can say, like, search for, there's gonna creep.
kernels.
Like, yeah, we can… I don't know if… I guess we can probably all, like, move all of this to, issue. I'll try to open one as well, from that.
Yeah, that sounds like a good idea.
Yeah, cool.
So, I think the last part we can, go over open PRs, I guess. I'll skip all the… the PandaBot stuff, Because we're kinda sick of it.
Yeah, I guess I'll go from the bottom.
I don't know, let me check if Tyler… Need any more review on this?
I guess, yeah.
I guess they gave him some comments a couple of days ago, probably in KubeCon.
Yeah, I… I talked to the guy that, opened this PR, and I think he's gonna probably You said that you should, like, respond this week with… Submitting, like, some of the fixes that we suggested?
So, this one, we should continue with it?
Or this, I don't know if Tyler… Anything, Mattia, I see you approved. I think we can just, merge this?
**Mattia Meleleo** 21:44 Yeah, I think, I think we can merge it. Maybe we should wait for Tyler's… Last words, otherwise this is complete, or…
**Nimrod Avni** 21:56 I can just tag him, maybe.
**Mattia Meleleo** 22:01 Yup.
**Nimrod Avni** 22:03 If he says yes, we'll do it.
Yeah, this is Tyler as well.
This is, Mike's… I don't know, I think we talked about it last week, I don't know if… Anything has changed since then.
I actually had some stuff from, yesterday as well.
**Mike Dame** 22:21 Yeah, Mario left some comments, some feedback, so I'm working on that. I also saw, Nicola had pinged me on, looks like there's a flaky test right now with the dynamic bid selector, so I'm gonna… I think I might have a fix for that, and I'm trying to, add that into this PR, but I'm gonna… Basically, Mario was pointing out, and I agree with him too, that, the dynamic selector, I was really trying to, like, wire it through, like, existing criteria matcher, and trying to, line it up with everything that's there already, but It kind of, like, the more and more that we look at it, it kind of seems like it's sort of its own thing, so he was telling me that we can, I don't understand… I have to try to understand the swarm stuff that we have first, but it, seems like we can kind of run two mutually exclusive swarms. So basically, if the dynamic selector, which is the pids matcher, is set up, then use that one instead of the static config, because the whole point of using this is that it's not going to conflict with static config like it's meant to be used by code.
And I think that makes sense, too, because I'm honestly seeing this as something that kind of grows into more than just a dynamic PID selector, but more of, like, a dynamic selector on its own that code can use to interact with Obi. So I'm gonna be… Looking at that refactor, he opened up a, like, a sample test to show that it's possible, so that, I think, should clean up the code path for where Dynamic Selector is being used a lot.
So, I'll try to get that soon, because I know that we're trying to do, the release probably next week, right? So… I'll get back to him, probably today or, maybe tomorrow on that.
**Nimrod Avni** 24:14 Great. That sounds good. That's right.
Yeah, Pino, you have this… check OS support, I don't know if we have anything else to do with it.
**Giuseppe Ognibene | Coralogix** 24:31 No, no, I need… I need to… to implement the… the comment review. It was as simple to do, but then it got a lot of comments.
So I need some time to… To update it.
**Nimrod Avni** 24:45 That was not a good first issue.
**Giuseppe Ognibene | Coralogix** 24:48 No, indeed, we need to select the good first tissue show.
In a good way.
I end up to do two reflectors, very simple to do.
**Nimrod Avni** 25:00 Need to be careful.
**Giuseppe Ognibene | Coralogix** 25:02 Okay. Yep.
**Nimrod Avni** 25:04 Okay, we have some more stuff, yeah, we have another one, oh, huh?
Extracting some attributes to a common, the common attributes field.
**Giuseppe Ognibene | Coralogix** 25:17 Yeah, Mario, that good comment. I just updated, because he didn't reply, but I implemented it. If it's good, we can use it, otherwise I will revert it.
Basically, there was… there was, some fields in common with… with Netflix, solely, I need to, like, merge it.
That's all.
Just.
I fucked it.
**Nimrod Avni** 25:48 Okay.
Cool.
Yeah, I'm Mario, okay, Mario had one of… Testing, mutually exclusive nodes, Between two parallel nodes, the execution is mutually exclusive.
I think that's… Like, when he means no… yeah, okay, like, swarm node, okay.
And relating to, what you did, Mike.
Yeah, yeah. I guess that's, like, a prerequisite to… Your PR?
**Mike Dame** 26:20 I don't think it's a prerequisite, but this is, like, kind of the example test that he put together.
**Nimrod Avni** 26:26 Oh my god.
**Mike Dame** 26:27 What he's doing, what he was saying should be possible, so…
**Nimrod Avni** 26:30 Oh, you just edited the test.
Okay.
Cool, makes sense.
Nice. Okay, that looks good.
Yeah, and then just… A bunch more, renovate stuff.
It'll be, probably need to look at. I think… I don't know if that's, the same check. Some of them probably failed.
Because, Mattia, what you just fixed, the… The issue with the… True.
**Mattia Meleleo** 27:01 I rebased something. I'm not sure if this one is related to my stuff.
If you open the test, I don't think it's related, because there were a lot of tests failing.
**Nimrod Avni** 27:16 Yeah, the thing may… probably may be… Maybe some, but not all. I think that… Yeah, that's login.
**Mattia Meleleo** 27:25 We can… we can try to restart this one.
**Nimrod Avni** 27:28 But I think this one might be… I think that's also that stuff, leaky toast, so I think that's probably good, but… I'll try to run them both.
Not again.
Yeah, cool, I think that's it, for… I think the agenda here, kind of a… Small, quick.
Sig.
Yeah, definitely. Unless anyone has, anything they want to add that we want to discuss?
Cool, so, have a…
**Giuseppe Ognibene | Coralogix** 28:13 I had a question for Mario, but he's not here.
Next time.
**Nimrod Avni** 28:19 I already… I already know the question.
Yeah, cool, guys. So, be back probably next week with a bigger team, bigger SIG.
Well, I guess I'll see you guys next week.
**Stephen Lang** 28:35 Ping Mario on Slack if you… if you want. He's pretty busy, but he may be able to get back to it at some point.
**Giuseppe Ognibene | Coralogix** 28:40 No, no, Steven, the question is very, very, very stupid.
**Stephen Lang** 28:47 I'm sure there's no stupid questions, just, just ping you.
**Giuseppe Ognibene | Coralogix** 28:49 Oh, no, this one is very… I can, I can…
**Nimrod Avni** 28:55 When you know it.
**Giuseppe Ognibene | Coralogix** 28:57 There is a line of code that I don't understand. Maybe… maybe you know.
But then I need to find it. I don't remember where it is.
**Stephen Lang** 29:07 I'd say there's no stupid questions, just, just post it on… on the Slack… in the leads channel, if you don't want to.
**Giuseppe Ognibene | Coralogix** 29:14 Okay, yeah, well, yeah, maybe it's better, maybe it's better.
**Stephen Lang** 29:19 All right, thanks all. Thanks, Nimrod, for leading us.
**Nimrod Avni** 29:22 Yeah, sure. Have a good day, guys.
Beautiful.
**Giuseppe Ognibene | Coralogix** 29:25 You know, how about you?
**Mattia Meleleo** 29:26 Goodbye.
**Nimrod Avni** 29:28 Bye-bye.
