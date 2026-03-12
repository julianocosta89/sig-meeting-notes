SIG: Android SIG
Date: 2025-07-22
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Jason Plumb** 02:01 Hello!
**GZ Gregor Zeitlinger** 02:06 No.
**Jason Plumb** 02:09 We'll go ahead and get started. I know that Cesar is at an elastic event today or this week, or something, and so will not be joining.
and no one has preloaded any items on the agenda.
and I figure we could go ahead and get started, as people may trickle in.
**GZ Gregor Zeitlinger** 02:31 Has anyone made the joke yet that his agenda is not very elastic.
**Jason Plumb** 02:36 No, I have not heard that joke yet. But now now I have. Yeah.
Okay. Let's go ahead and cruise on over to the open issues. Hi, Hanson.
**Hanson Ho** 02:51 Hey!
**Jason Plumb** 02:54 Who's on over to Android and Android.
and let's see what's out here.
Oh, yes, I think I kicked this off, and I'd expected this just to pass. This seemed like a weird fluke. Yeah, so this is, this is fine.
I'm gonna go ahead and close that.
It said it was cancelled. I don't know if that was a manual thing, but it it looked like it got cancelled.
Alright. There's, you know, the the activity in the repo has been a little slow since we last met, so there hasn't been too much. There are some pull requests. I was messing around with build performance, and this was a change. I was kind of optimistic about that did nothing.
I mean, okay, I it did it. It maybe bought us like on the order of 3 min on a I don't know what was enough.
40 min build or 30 min build. Let's see.
build yeah, 21 min, which I don't love, and if we look at some other builds.
it's a build like pretty consistently still in the thirties.
and it's not the end of the world, and I know that other repos take just as long but it sure does make iterating, especially when doing a release kind of painful, because you do have to kind of wait to stage stuff out. So I'm gonna close this. But I'm open to other ideas. When, if if people have time to think about how to make our build faster. I guess another thing that I I'll just share that I was looking at.
**GZ Gregor Zeitlinger** 04:52 Hi Jason.
**Jason Plumb** 04:53 Yeah.
**GZ Gregor Zeitlinger** 04:54 Did you look into splitting out and doing more in parallel, like we do in the Agent Repository.
**Jason Plumb** 05:02 So how does that work? I don't. Oh, where we have, like the like, the tests, a tests. B thing.
**GZ Gregor Zeitlinger** 05:09 Exactly. It's quite complicated, but at least.
**Jason Plumb** 05:12 I know.
**GZ Gregor Zeitlinger** 05:13 Have to come up with a recipe.
**Jason Plumb** 05:16 It's true. Yeah, yeah, I had not given that in any consideration. So thank you for raising that. I'm gonna make a note of it here.
**Hanson Ho** 05:25 The weird thing about this is that we're not doing very much.
So a lot of it is set up. It's the actual runtime for tests and stuff. I I don't think is is ridiculous.
like, are there better runners we could use? Is it? Is it faster on Linux versus Mac OS, like like, it's just like, I'm by no means an expert in this, but it just feels like we're doing so little and taking so long.
And there's something really weird.
**GZ Gregor Zeitlinger** 06:06 And the agent. I know why it's slow, because it has to like assemble the whole Java agent, and then has to put this instrumentation that you're testing in it, and that just takes long.
I don't know if you have a comparable thing where you have to build a a complete distribution or something before you can test it.
**Jason Plumb** 06:30 At some point.
Go ahead.
**Hanson Ho** 06:32 Some of the tests will require building an app. And I think I don't know how many of these actually require an emulator. So like the app building takes a bit of time. But we're like this, not not this long kind of thing unless we're redoing it. I think we we a few months ago we dug in and then looked into it, and we we couldn't find anything obvious but some some new eyes might might be good to just take a look at, you know.
like the the demo apps, you know. 7 7 min seems excessive, because the SDK should be built already. Unless it's not built unless it's rebuilding it. And the app itself, you know, unless we're running like integration tests in there where we spin up emulators. I don't.
That 7 min is is pretty bad.
**Jason Plumb** 07:26 It's sure there. So in in the main build here there are a couple of those android tests, and I think that those spin up something, don't they.
**Hanson Ho** 07:35 If they're Jv, if they are a roboelectric test, they don't. They just run on the Jvm, so unless they're like like Android test integration tests that, like, you know, spin up an emulator.
**Jason Plumb** 07:50 From from my memory. Let's let's look at the build scan. But from my memory I believe it was like one of the network instrumentation tests was the slowest, like pretty consistently, and when when I looked at it I couldn't exactly remember what was going on. So you can dive into the timeline.
and then you can order by longest, and we can see that test released unit test is the slowest but it only takes 1 min. But then these these minutes start to add up right is the whole thing. So the the double testing is, you know, for the for the release build and the debug build.
you know. That's that's 2 min of that 13.
And then, if we dive into like test performance, I forget how to do that, let's see.
Task execution.
No, maybe see.
I was. Anyway, I was diving through the stuff and trying to get some traction and trying to find some small wins. And that Pr clearly was not one of them.
yeah, this one, maybe. Okay, yeah. So tests, this is sorted by longest. And then these top ones are all network to network right?
**GZ Gregor Zeitlinger** 09:31 Actually, which one is this.
**Jason Plumb** 09:34 Modern sdks. That's kind of a bad test name. But current network provider test. Okay? So if we look at what the current network provider test does the the 1st thing I noted is it do? It does use robo electric.
And there are some different configurations. For because it, the behavior is different, based on which version of the SDK you're using.
**GZ Gregor Zeitlinger** 09:59 That still exists. I used that more than 10 years ago.
**Jason Plumb** 10:03 Robo, electric.
**GZ Gregor Zeitlinger** 10:04 Yep.
**Jason Plumb** 10:05 Yeah. It still exists.
**GZ Gregor Zeitlinger** 10:07 Is it.
**Hanson Ho** 10:08 So.
**GZ Gregor Zeitlinger** 10:08 Outdated, or is it still what you use.
**Hanson Ho** 10:12 It's it's still what you use. But generally you don't use the robotic test. Run. Use the Android 4 test runner, which is a super set of this. It probably doesn't. It probably doesn't improve this. But Robo electric itself spins up pretty fast. So I mean, it's slower than like, you know, just plain old, like J. Unit tests. But 4 seconds. Is not Robo electric? Something is happening here that.
**Jason Plumb** 10:36 41, yeah, 41 seconds. Right? So that seems like this, current. Now, I'm gonna I'm gonna widen my window. I think that's fine with sharing. But just to try to get few more characters there.
White space over here. By the way, if 40, 42 seconds on that one test seems excessive.
**Hanson Ho** 10:58 Yeah, I mean, this is basically what 70% of of of all, all tests.
Well, maybe 60% of all all tests. So if you disable that, you would basically improve this by a minute and a half.
Yeah. Oh, God.
**Jason Plumb** 11:15 So little wins, you know, could add up, but I don't know how to. I don't know how to shrink this like when when looking through that I didn't see anything obvious, so I don't think there's any like weights.
**Hanson Ho** 11:26 It's running. Well, it's running on a whole bunch of different Api that it's not necessary. Because some of them were actually very similar. So like 26 and 27, or wait 2720, anyway. This could be pared down, so I can probably spend like 10 min, and and save us like a minute, if nothing else, just to like trim off the the the excessive ones. So.
**GZ Gregor Zeitlinger** 11:55 That's cool. I mean, I think that helps rather. 1st do the parallelization before you do the the hard work and look at each individual test.
**Hanson Ho** 12:09 Well, this this one is, it takes like 60%. There's 1 test. So the paralyzation, you know, this will still take 41 seconds. If we parallelize this.
**GZ Gregor Zeitlinger** 12:21 Are you talking about? 30 min? Not seconds. What is what's wrong?
**Hanson Ho** 12:26 Oh, I'm just taking. I'm taking a look at the test execution. So I think parallelization would do something. But if a lot of the work is in the SDK setup. Then the parallelization wouldn't really do very much.
**GZ Gregor Zeitlinger** 12:39 Okay.
**Hanson Ho** 12:40 It like. If the test running is is like 50 seconds, then, you know, there's really nothing to paralyze.
**GZ Gregor Zeitlinger** 12:48 Yeah.
**Hanson Ho** 12:51 So that's not going to fix everything. But I think we can start trimming bad stuff. You know, if we could do like a couple of minutes every week
**Jason Plumb** 13:04 Yeah. Okay, yeah. Chipping away at, I think would be awesome. Just for for those who may not have seen this.
I just wanna show people how it's done in the instrumentation repo Yikes. Okay.
so where am I looking? This is not the right place.
Need to just pick up. It's it's like it's part of a Pr build right.
**GZ Gregor Zeitlinger** 13:35 Yeah, you can look at any any bill.
**Jason Plumb** 13:38 Yeah.
And then in it's like these, smoke tests are all run in parallel. Right?
**GZ Gregor Zeitlinger** 13:47 Yeah, but this is not the the standard build.
**Jason Plumb** 13:52 Oh, what's how do I get to the thing you're thinking of, Gregor? I know what you're talking.
**GZ Gregor Zeitlinger** 13:56 It's also here, maybe more down if you scroll down. Yeah, exactly has the the number test and then number, and then also has the the Rava version, and if it's indie or not.
**Jason Plumb** 14:11 Right. So we run all of those in parallel, so that we can be testing 8, 1117 on different at the same time.
**GZ Gregor Zeitlinger** 14:20 Yeah. And then also the the cluster is the test. 1, 2, 3, is it 3 or 4?
So 0. I think it's starting with so 0 to 3. So it it's running.
It's split in 4.
**Jason Plumb** 14:36 And each one is 24 min. So certainly, if these ran serially, it would be a big problem.
**GZ Gregor Zeitlinger** 14:41 Yeah, it is still a pain.
**Jason Plumb** 14:43 I mean, it still takes forever.
does it? It doesn't roll it up here for us. But yeah, okay, so 53 min.
So that's that's just an example of like, I wanna put a screenshot, maybe of that in this.
**Hanson Ho** 15:00 We can do, release and debug in parallel.
**Jason Plumb** 15:04 That would be awesome.
**Hanson Ho** 15:05 Wanna do that?
**Jason Plumb** 15:06 I wish there was some easy way to tell Gradle to do that.
I don't know of one.
**GZ Gregor Zeitlinger** 15:12 You don't need gradle for that. You can do that on the Github Action level.
**Jason Plumb** 15:19 Oh! How do you do that.
Is it in here.
**GZ Gregor Zeitlinger** 15:26 Into. It's easier if you look at the source.
**Jason Plumb** 15:31 That's where I was getting to.
**GZ Gregor Zeitlinger** 15:32 Okay. I didn't know that. You can also navigate that way.
Yeah, look for matrix. But no, this is importing other yaml. It's an fine.
**Jason Plumb** 15:46 Yeah, build common.
**GZ Gregor Zeitlinger** 15:49 And no, this is importing yet another one. It's something with reusable build.
**Jason Plumb** 15:55 Okay.
**GZ Gregor Zeitlinger** 16:01 Reusable.
**Jason Plumb** 16:03 The latest Debs.
**GZ Gregor Zeitlinger** 16:06 Huh!
I thought it was reuse it, but maybe think this does make it. This demonstrates a good point is that there is some complexity in building that parallelization.
Yeah.
**Jason Plumb** 16:20 A lot of moving.
**GZ Gregor Zeitlinger** 16:21 Or matrix. If you want to find the right place no more in
**Jason Plumb** 16:27 The whole Reboom.
**GZ Gregor Zeitlinger** 16:28 Yeah, exactly.
And then, yeah.
**Jason Plumb** 16:35 Yaml
**GZ Gregor Zeitlinger** 16:39 Built common. Okay? It was builtcom, not reusable. Okay, mix that up.
**Jason Plumb** 16:44 Sorry.
Yeah. Here we go.
This find is like, Github, like takes over the ux. Here.
**GZ Gregor Zeitlinger** 16:55 Yeah, this is really annoying. So matrix itself is not complicated. It's more that in this repository it's a little bit over the top. I'm using matrix and other repositories, and it's just fine.
**Jason Plumb** 17:09 Got it. So I wonder how we would use this to parallelize the dev and release tests right.
**GZ Gregor Zeitlinger** 17:18 So usually you would set an environment variable or other argument that you pass. And then you make matrix over that release type. No, I don't know what what the name is. Type.
**Jason Plumb** 17:31 Where's the microphone?
And
**Hanson Ho** 17:35 I mean at Android Android tests is 5 min. So if we split it out, you know, it's 2 and a half minutes.
**GZ Gregor Zeitlinger** 17:46 That's
**Jason Plumb** 17:48 That's not what you want.
But oh, and it looks like, maybe these no. So this one, this one started 1st right, and then it ran for a minute, and then the other one started. So they are serially and so that would that would shave 7 min off the build, wouldn't it?
**Hanson Ho** 18:05 Nuts. This is the start that's that's not duration.
**Jason Plumb** 18:09 I'm sorry it would say 1 min, because they, the.
**Hanson Ho** 18:10 Yeah.
**Jason Plumb** 18:11 1 min. Sorry. Yeah.
**Hanson Ho** 18:12 So I would. I would. So group by type. There's like a bunch of other tests. That's so.
So so the unit test, the the lit analysis took 3 min. I don't know why.
That seems.
**Jason Plumb** 18:27 Yes.
**Hanson Ho** 18:28 Off.
Kotlin, compile being that long also seems off because we don't have that much code the the Cap generate stubs.
I don't know specifically what that does, Jamie. You're on the call, Jamie. You might know what that does.
**GZ Gregor Zeitlinger** 18:47 Cause. That's that's content. Annotation processor.
**Hanson Ho** 18:52 Right. But why? Why does it take 2 min like, what are we generating like the Java compile takes a minute.
So that's probably okay compared to like.
**Jamie Lynch** 19:09 It's also worth mentioning. That capped is getting replaced with ksp, which is much faster.
**Jason Plumb** 19:17 Oh!
**Hanson Ho** 19:19 Yeah, I'm wondering if we could just swap that.
I think there's a bunch of these a minute type saving things. If if paralyzation is easy, we should do that. But if it's like, if it looks at any way hairy, you know may not want to do that.
**Jason Plumb** 19:41 Yeah, there's the trade off. Okay? So we've got some ideas. I don't wanna necessarily spend the entire call scrap Bill. I was just looking at Prs. And I was like, Oh, yeah, this one is still out here.
But I will go ahead and close it, because I don't think that did anything for us.
It was just purely an experiment. So feel free to do those if you have other ideas.
and then what other Prs are out here.
We still haven't decided what to do about this one right?
**Hanson Ho** 20:22 I think we can't upgrade right? Is isn't that what?
What clever? Chuck decided.
**Jason Plumb** 20:30 It's too early for me to remember what the hell that discussion went. But there was.
There was definitely a problem with the upgrade. What was the nature of the failure? Again.
**Hanson Ho** 20:39 I think the new ones hid. Some Api, that clever chuck was depending on because it was basically that's for the click instrumentation
**Jason Plumb** 20:51 Got it. Got it.
**Hanson Ho** 20:53 I guess I think it still works at Runtime, but it it well, actually, I don't remember specifics. But it's it's something to do with stupid Android, or rather, us having to to inspect it at a layer that we shouldn't really be inspecting it, and then.
**Jason Plumb** 21:08 We're instrumentation. We're hacking on stuff. And then they broke broke our ability to hack. So we gotta. I mean, if we want to keep that instrumentation up to date. We should work around it because there will be.
I mean, that's and that's where that issue of running the integration tests came in. Okay.
yeah. Okay, thanks for shaking the cobwebs out for me. I'm remembering this now.
Okay, that's a little bit of a can of worms. But it would be nice to revisit that.
Okay, that's that's basically it on the the interesting prs.
and we've we went over these last time. There's also really not any new issues other than with stuff open this last time. Thanks for doing that.
And what else do people have.
**Hanson Ho** 21:58 Oh, I gotta fix that documentation about desugaring. I was gonna do it last week, but I haven't so you need to sugar. 26 now. I think we got away with only 24, because, whatever the Java SDK required. We didn't use so 24 was, okay. Now it's it's 26. So because of the Java 9 clock implementation that made it into 1.50. So.
**Jason Plumb** 22:26 So previously was 24 lower. Now it's 26, or lower.
**Hanson Ho** 22:29 Yes, so 26. You don't need any sugar for now and then, if it's so, the Delta is really, if it's 24 and 25. You would have to do that.
And you'd also need gradle 8.4 and agp. 8.3 and the workaround. But that's that's all documented already. It's just the the version has to change from 24 to 26. That's all.
**Jason Plumb** 22:59 That's cool. Okay?
And will you take that on.
**Hanson Ho** 23:02 Yeah, yeah, I was gonna do it last week. And and I was gonna like, write comprehensive documentation and go back. And anyway, I didn't go back now. I'll go back today.
**Jason Plumb** 23:10 Sounds good.
Okay, I will. I may try and find cycles this week to open a new Jank, P. Cenk, Pr and simcomf.
and I will try and keep it very brief, and my intention is to have it be, I think 3 things.
Of course, the timestamp, because you get that for free with events. It's gonna be an event name of whatever I had before, like Ui rendering Jank or whatever I had. And then the threshold that was exceeded in in milliseconds, probably.
and then the number of times it was exceeded. And then the period. So there's 3 fields right? It's it's the duration over which is being reported. There's the threshold that was exceeded, and there was the number of times it was exceeded. That's my intention.
Does that sound like a reasonable starting point. Hanson.
**Hanson Ho** 24:08 Yeah, yeah. You basically need to describe what that thing is. And I think those 3 things combined will. And it's it's it's a good start.
**Jason Plumb** 24:19 And maybe I will. Maybe I will spend a little while writing some prose about why.
even though it looks like a metric, we may not want to use a metric for this thing.
especially in the context of real user monitoring.
**Hanson Ho** 24:33 I I think I commented on your closed Pr.
**Jason Plumb** 24:37 You did.
**Hanson Ho** 24:38 Yeah.
**Jason Plumb** 24:39 Yeah.
**Hanson Ho** 24:40 I wasn't sure which. Yeah, I mean.
anyway, feel free to pull from that or, yeah.
**Jason Plumb** 24:46 That's cool.
**Hanson Ho** 24:52 Sometimes walks like a dog and barks like a dog. But is it a dog? It's a person talk.
**Jason Plumb** 24:58 It's true I had someone do that to me a few weeks ago when I was on a bicycle. That's really weird.
**Hanson Ho** 25:07 Well, you're in Portland, so maybe not. Not that weird.
**Jason Plumb** 25:10 It was not in the city. I'll tell you that.
yeah. So this just this is the one I closed, and I didn't see any comments after this, but maybe it's above here in the in the fold.
The big fold, cause I do remember seeing you had commented on this Hanson. Yeah.
**Hanson Ho** 25:31 Oh, there it is. Yeah.
**Jason Plumb** 25:33 Appreciate that.
Okay.
well, I don't have anything else. I'll just make a note that Jason is gonna Cenk.
Pr. In some call sometime this week.
**Hanson Ho** 25:56 I think we have. We have the client Sig at 9 today. So.
**Jason Plumb** 26:02 We do? Yeah. Yeah. So in 30 min we have the clients tickets every other week. It's only half an hour.
My intention is to join that.
**Hanson Ho** 26:11 I saw Josh Post. Something about we'll save it for that one for classic, I guess.
**Jason Plumb** 26:19 Okay.
okay, I mean bringing up this. This topic of metrics, again, might be prudent in that larger, like, non android specific group.
Given that we took up nearly an hour last week with that topic I'm a little hesitant to, but we could at least let them know that we've talked about it, and we've got some ideas formulated, I think. At least it seemed it seemed to me last week, and he's not here to defend himself, but it seemed like we talked Cesar down off that cliff a little bit.
and I think I think he came around to like where we're coming from. I'm not gonna rule out there that there might still be some cases we haven't yet considered that could still be valuable.
But yeah, I don't want to rehash it now.
**Hanson Ho** 27:02 There is, there's a use case. But the use case given where hotel is. Yeah, unless hotel wants to change some things fundamentally about metrics which you know that'd be great. But long road.
**Jason Plumb** 27:18 Alright. Does anyone else have anything that they want want to bring up today, or or talk about?
Cool reviews are always welcome and needed as always. So thanks for showing up. Thanks for being here.
Appreciate it.
See you on the Internet.
**GZ Gregor Zeitlinger** 27:37 See you around.
**Jason Plumb** 27:38 Bye.
**Hanson Ho** 27:39 Bye.
