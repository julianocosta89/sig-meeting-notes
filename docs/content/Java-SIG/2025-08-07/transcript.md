SIG: Java SIG
Date: 2025-08-07
Duration: 49 minutes
============================================================

## Zoom Recording Transcript

**GZ Gregor Zeitlinger** 00:47 Hello!
**John Watson** 00:56 Good evening, morning, day.
**GZ Gregor Zeitlinger** 01:02 Evening for me. Yeah, the last meeting on declarative configuration we were only 2. So let's see how how many we can get for this one.
**John Watson** 01:19 Crass is out right and job out.
**Jason Plumb** 01:22 Watson. I'm I'm prepared to drive unless you want to.
**John Watson** 01:26 No, do it!
**Jason Plumb** 01:27 Okay.
It'll be my my gift.
**John Watson** 01:31 Thank you, sir, appreciate it.
**Jason Plumb** 01:34 Worth gift ever.
Yeah, I was. I was. I was talking with Robert earlier. And I was like, Yeah, might be a little slow. Today we'll see.
**John Watson** 01:55 Yeah. My team here at Cloudera is only 2 of us in today also. So it's a slow day.
**Jason Plumb** 02:01 Yeah.
**John Watson** 02:03 I don't know why, but it's my birthday. Everyone's celebrating my birthday. That's why.
**Jason Plumb** 02:07 Woo, happy birthday.
**GZ Gregor Zeitlinger** 02:09 Happy birthday.
**Jason Plumb** 02:15 Alright! Give another 30 seconds.
is Jay's background the same background Nikita used to always have, or am I confusing it.
**John Watson** 02:32 Do you remember Nikita's background?
I think, probably. Yeah, I don't see. It looks similar, at least.
**Jay DeLuca** 02:39 The iss!
**Jason Plumb** 02:41 Bye.
Well, in Trask's absence I will be driving today's meeting, which is currently a pretty light agenda. If anyone has topics they would like to discuss.
Please add them to the agenda, or just feel free to jump in and yell stuff at any any point. I am going to be doing the release for core, or at least kind of driving it as a non maintainer. I can't merge so, Watson, you'll be around tomorrow to help with this cool
**John Watson** 03:18 A Shelby.
**Jason Plumb** 03:19 Cool either, either late tonight. Later, today or tomorrow, I will take this out of draft and we can proceed. But it's very light, which maybe I'm I hope I think I'm not missing anything, but I think it's also just been pretty slow with Jack out, so.
**GZ Gregor Zeitlinger** 03:35 Yeah, I have some Prs open, but they need review. So they.
**Jason Plumb** 03:40 Yeah. Yeah. So that's the next thing to talk about, then is like, which of these Prs, do we really want to to try for open open to suggestions here. If people have cycles to review.
**John Watson** 04:00 I definitely will not.
**Jason Plumb** 04:03 Okay.
**John Watson** 04:05 Although I may go through and like check some of the update, like just the the simple dependency updates. But.
**Jason Plumb** 04:14 Yeah. Yeah. The gradle 9. The gradle stuff is failing across a bunch of the repos. I got the android one working. That was kind of exciting. I can show you that one.
**John Watson** 04:26 Yeah, what were the? So what do you have? A Tldr, and like, what has changed? That's breaking everything.
**Jason Plumb** 04:32 In our case it was really strange. We had looks like he probably already merged it.
We had one configuration that was being declared that was being added to the configuration container unnecessarily is what it seems like. So our our breakage was around this. So we have some configuration that's created. And then we're adding into configurations. But, like the Java Doc on create, says it creates and adds it to the configurations. So this was unnecessary, and this is a compilation error in Gradle 9. So that was that was the change I made to support this and then this variable didn't need to be declared. So it was failing the whatever Grail val validator stuff.
and this is unrelated.
But that was that was it on ours. But over here it's pretty interesting. Let's see.
**John Watson** 05:31 Well, our great old setup.
The repo is pretty non trivial, so.
**Jason Plumb** 05:37 Yeah, exactly. So this one says it can't get invention for project.
So we can look in here. It's like, line one.
**John Watson** 05:50 That's.
**Jason Plumb** 05:51 Yeah, anyway.
**John Watson** 05:52 It was fast, I guess.
Oops.
**Jason Plumb** 05:56 I haven't had any time to look at this at all.
**John Watson** 05:58 We need a call onurag.
He he wrote all this stuff originally.
**Jason Plumb** 06:03 I think the I think the instrumentation one is also failing. See if it's failing for the same reason. That's not the right one.
This one also failing?
And is that the same?
None of the oh, that's muzzle.
Is that? Why, it's failing, anyway, it's very broken.
**John Watson** 06:38 But that one looks like it might be similar to what you did in Android.
**Jason Plumb** 06:43 I? No, I think it was pretty clear. The error I got on the android one was like.
Configurations cannot be directly added. Use a factory method. And I'm like, all right.
anyway, that's that's happening across everything. I think it's also happening contrib.
**GZ Gregor Zeitlinger** 07:03 I also have an error in my distro for the shadow. Gradle 9.
**Jason Plumb** 07:09 Oh, interesting!
**GZ Gregor Zeitlinger** 07:15 Did. Did we have any problems? That you encountered that I might be able to to check.
**Jason Plumb** 07:24 So this one is lumping them together, which is interesting right?
**John Watson** 07:29 Oh, is it no longer? We're no longer have to use the John Wrangelman shadow. There.
**Jason Plumb** 07:33 I don't know. I mean, this is this is in contrib so renovate as part of the gradle v. 9, also updated this which that's unexpected for me. Did anybody else commit this?
That's why. Okay, that's why.
**GZ Gregor Zeitlinger** 07:51 Oh, yeah.
**Jason Plumb** 07:52 But it's.
**GZ Gregor Zeitlinger** 07:53 That one.
**Jason Plumb** 07:54 Yeah, it's contrib. Thanks. Yeah, but still broken.
But it looks like just tests. So maybe maybe not. Let's see.
Hmm.
**John Watson** 08:08 And when windows, and maybe rewrite.
**Jason Plumb** 08:12 Weird smattering. So I'm gonna just do this.
**John Watson** 08:16 Looks like. Maybe all the windows ones were failing, though.
Oh, no, no windows. 11 or Java 11 was working.
**Jason Plumb** 08:23 Yeah, it was a weird smattering. So I'm just gonna pretend that everything's fine over there. And I haven't seen what it's done in our distro just to compare notes with you, Gregor.
This 1 0, ours is passing.
**GZ Gregor Zeitlinger** 08:43 There is this for me as well. It was only the shadow that is failing.
**Jason Plumb** 08:47 I mean we we also shadow.
**GZ Gregor Zeitlinger** 08:50 Everyone is shadowing.
**Jason Plumb** 08:52 Oh, sorry. Sorry. You mean you mean the dependency to shadow? V. 9. Got it? It's this one. Yeah, that's broken for us, too.
**GZ Gregor Zeitlinger** 08:59 Maybe this is the same problem.
**Jason Plumb** 09:01 It. It probably is.
Yeah. So this is probably the change that we need. The the one that Trask made is probably just what we need to make here as well is changing which Plugin we're using.
It may no longer be the wrangle man. Jingle man, whatever that is.
**John Watson** 09:20 Jay Engelman.
**GZ Gregor Zeitlinger** 09:23 Yeah, let me pull up my my error so that we can compare.
**Jason Plumb** 09:34 Is it in here somewhere.
**GZ Gregor Zeitlinger** 09:40 Yeah, I can actually send you the link.
**Jason Plumb** 09:42 Okay.
**GZ Gregor Zeitlinger** 09:48 You like.
Here it is.
**Jason Plumb** 09:53 Okay.
**GZ Gregor Zeitlinger** 09:58 It's shadow gradle plug. And now it's already gradled up. So it it looks like this is already the upgraded updated one.
**Jason Plumb** 10:07 Yeah.
**GZ Gregor Zeitlinger** 10:09 And the error is really strange. It says that it's missing a dependency, so that an exporter cannot be found.
If you look for Otlp. This is what it's missing.
but it could be a red herring.
Now you have to look there.
**Jason Plumb** 10:29 Oh, yeah.
**GZ Gregor Zeitlinger** 10:30 This is exactly the message.
**Jason Plumb** 10:33 And that's the failure.
Huh?
**GZ Gregor Zeitlinger** 10:36 Yep, I I pretty sure that this is a failure.
I think it might be a problem that the metadata file is not shadowed correctly.
**Jason Plumb** 10:50 Hmm.
**GZ Gregor Zeitlinger** 10:54 I looked at the change log, but I couldn't find anything that explains it.
**Jason Plumb** 11:03 Okay.
Well, Trask's description of what he did in contrib was pretty brief.
but it seemed like he was on to something. Probably.
I mean it was in this one right?
**GZ Gregor Zeitlinger** 11:21 Yep.
**Jason Plumb** 11:29 But you were already on Gradle. Up.
**GZ Gregor Zeitlinger** 11:32 Yep, that's right. Is anything else you changed.
**Jason Plumb** 11:36 Let's look at the commit.
Maybe I already was.
No.
**GZ Gregor Zeitlinger** 11:45 No, that's all. Okay.
**Jason Plumb** 11:47 Oh, rc, 3. That's interesting.
Okay.
**GZ Gregor Zeitlinger** 11:54 The version is different.
**Jason Plumb** 11:57 I mean, it's it's rc, yeah, I mean, it's Rc, 3, and not 9 point. Oh, so I don't know if.
**GZ Gregor Zeitlinger** 12:02 I can try that.
**Jason Plumb** 12:03 Yeah, I don't know if that's synced with gradle now.
No sure like version wise.
But it yeah. I wish he was here to explain why or how he, how he found this.
but it seems like it didn't actually fix everything.
**GZ Gregor Zeitlinger** 12:23 Does he have the same error that I have now?
This is also with Otlp.
**Jason Plumb** 12:29 Well, there's a bunch more stuff in here. Okay?
Well, I guess we gotta wait for these tests to finish or the build to finish since I re-clicked it.
Okay, we have a question from Jay.
Oh, yeah. Yeah.
This person also has an issue in Android. I just, I recognize that name.
**Jay DeLuca** 13:13 Okay.
**Jason Plumb** 13:14 Cause. It's like, I kind of want it to be 50 cent.
**John Watson** 13:18 50 50 cent.
**Jason Plumb** 13:20 Yeah, I'm not allowed to say it that way.
No, it's like, that's just a cool name. Yeah, we can. I think we can move this one.
Yeah, they're using disk buffering. And this is definitely an android thing. Right?
Yeah.
But the I guess because the crash was in the exporter. They wanted to open it. Here. Is that what? What's is that? What's happening.
**Jay DeLuca** 13:50 Maybe they just don't know about gallery part or not.
**Jason Plumb** 13:55 They definitely know about android because they've filed issues. There.
**John Watson** 13:58 I mean, this definitely looks 100% like an android thing. Not a.
**Jason Plumb** 14:02 Let's just move it. Can I move it?
Transfer something I've done, maybe once in my life. Oh, how did it know.
**John Watson** 14:13 Would you have access?
No, it's the 1st one in the list.
**Jason Plumb** 14:18 Yeah, I think it's actually correct. Yeah, I think that is why.
**Jay DeLuca** 14:23 It's just that obvious that it needs to go there.
**Jason Plumb** 14:25 Yeah, okay.
And there's a record of this. Right? Yeah, okay, cool. Thanks for bringing that up.
Yeah. They they filed another one. Just only I'm I'm just getting distracted here, cause we have time, and our agenda is pretty light. But yeah, they filed this one about time drift, and there was another one about being able to change the exporter. Yeah, we've we've been. We've been speaking with this person.
So cool.
Okay, issue triage.
We've reached that point.
**Jay DeLuca** 15:20 I think the one of note here is the spring, 4 0 0. It's gotten some attention today.
**Jason Plumb** 15:30 Spring.
Yeah, that's 1. Yep.
**Jay DeLuca** 15:34 It looks like in the the new version of spring. They moved a bunch of classes around. So now the spring starter doesn't work. I don't know if other things are broken as well, but.
**Jason Plumb** 15:44 Gregor, have you had a chance to look at this yet? Have you tried spring? 4.
**GZ Gregor Zeitlinger** 15:49 I have not even heard about it, but it looks like a milestone, not the final version. Is that right?
**John Watson** 15:56 Yeah. I wonder if it's worth waiting until it's out of like a further milestone before messing with it, because maybe they'll move stuff around again.
**GZ Gregor Zeitlinger** 16:03 Yeah.
**Jason Plumb** 16:05 Yeah.
**GZ Gregor Zeitlinger** 16:06 We just exclude.
I think we can exclude the milestone releases for a latest.
Where has this come up?
Oh, it's it's not a test.
It's a user report.
**Jason Plumb** 16:24 Yeah, yeah.
**Jay DeLuca** 16:24 Yeah. Yeah. And a couple of people commented on it today, I think.
**Jason Plumb** 16:31 Lori!
**GZ Gregor Zeitlinger** 16:36 I mean, okay, no, it's actually a good point to to consider how we should support this at all.
**John Watson** 16:48 Yeah, it's gonna be interesting. If it's a spring boot starter. Like, do we gonna need multiple version? Do we already have multiple versions? So we have like one for spring, 2 and one for spring. 3.
No, it's even more magic. We have one starter, but it has different source. Trees.
**GZ Gregor Zeitlinger** 17:07 That targets different versions. That was one of Laurie's idea.
**John Watson** 17:14 And it's working fine. So I think we should just.
**GZ Gregor Zeitlinger** 17:18 Do that at some point, but maybe it's really too early to support it now.
But we definitely say that we're welcome for for contributions. So if someone is interested in that, we can just point to how the source tree for Spring 3 is working and then having contributions that would greatly help.
**Jason Plumb** 17:42 Yep.
alright. I'm not gonna leave a comment on this right now, but I did remove it from triage, and I added, Spring boot starter. If anyone wants to comment, that'd be helpful.
**GZ Gregor Zeitlinger** 17:53 Can you? Put it in the chat? Then I can.
**Jason Plumb** 17:56 I can. Yeah, I'll put it in the doc. How about that?
**GZ Gregor Zeitlinger** 17:59 Yeah, that's great.
Thanks.
**Jason Plumb** 18:20 I didn't see this one yet. Has anyone looked at this.
**Jay DeLuca** 18:23 Yeah, the the open AI tests are really flaky. So they've been failing pretty consistently for the past week or so. Honorog has another pr. Open for extending the same instrumentation, and he makes some changes to the test that will hopefully resolve it.
**Jason Plumb** 18:42 Okay, it was just on J, 9.
**Jay DeLuca** 18:47 No, it happens.
Okay, like, it'll on random ones. Sometimes it's test. Latest dev, sometimes it's it's happening on Prs, too. Occasionally.
**Jason Plumb** 18:57 Okay. Okay.
**GZ Gregor Zeitlinger** 19:04 We have a report on flaky tests.
**Jay DeLuca** 19:07 Yeah. So if you click, if you open that flaky open AI test issue that I opened down at the bottom, there.
**Jason Plumb** 19:15 Oh, it's already on here.
**Jay DeLuca** 19:18 Yeah, right there.
Lori wrote a there's like a a module within. The repo that reports on these. So if you scroll up and click on that very flaky. Yeah.
**Jason Plumb** 19:34 Hmm.
**Jay DeLuca** 19:35 There's this spreadsheet that's up updated every night. So if you scroll all the way down to the bottom.
**Jason Plumb** 19:41 Whoa, I've never seen this.
Wow, yeah, okay.
**Jay DeLuca** 19:46 This is this is some Laurie magic here.
**Jason Plumb** 19:50 I've never seen this.
Okay. So if we go to like newer stuff is at the bottom.
**Jay DeLuca** 19:57 Yeah, if you just scroll all the way down, you'll see like starting on like the 27th or something of of last month. It's just like 99% open. AI, yeah.
**Jason Plumb** 20:09 Yeah. So you're looking at the package name here.
a little random touch base. This is super cool, because it's so, it's catching flaky. So is this, because anytime we, we end up rerunning a test or something like, how do you know how he's sourcing this.
**Jay DeLuca** 20:24 Yeah, I I think he. He has this this module that runs an analysis after the tests run, and it checks to see if, like they failed on a previous run.
I forget the exact logic, but I remember when I reviewed it. It's pretty cool stuff.
**Jason Plumb** 20:40 Cool, cool.
**Jay DeLuca** 20:40 But yeah.
**Jason Plumb** 20:42 Okay.
**GZ Gregor Zeitlinger** 20:43 Is this something that we could also use in the SDK, because I currently have a Pr. Where I'm not sure if it's really flaky or not.
**Jay DeLuca** 20:52 Probably.
**John Watson** 20:53 I mean, we don't really end up with many flaky tests in the SDK, but it I mean, if we wanted to put that in there it would be fine. The SDK. Seems test wise, pretty stable.
**Jason Plumb** 21:04 I mean, even just even just running like the same tests over and over on Github. If you do it long enough.
it you're gonna encounter some flakiness just just the nature of ephemeral cloud deployments and stuff. You're gonna hit these weird edge cases from time to time. So this is cool, because, like, if you know, this pops up and is only in here like one time, you can sort of write it off, you know I don't. I don't know what we do when this is no longer 14,000, when it's like a hundred 44,000 or a million.
But it's cool. I didn't know this was here. And then what are these links? These are Bill.
**Jay DeLuca** 21:42 The right to the the build scans and the Github actions. Yeah.
**Jason Plumb** 21:47 So this is the double failure just to pick one that's not open. AI.
Okay. So it drops you in.
dropped into Grpc. For some reason. Is that correct, anyway?
**Jay DeLuca** 22:01 No, I think, yeah, just the the the path that it runs all the. It just jams them all together.
**Jason Plumb** 22:09 Cool, and this is also determined to be flaky. Okay, that's cool. And then I guess it would take a person to go, analyze and try and figure out why it was determined to be flaky. But again.
**Jay DeLuca** 22:20 I think, with the previous version of velocity, or whatever we were using. It, had historical reports, and so I think it works on like individual basis. But we don't have like the longer term analysis. So I think that's why Lori.
**Jason Plumb** 22:35 Okay, that's why.
**Jay DeLuca** 22:36 Discussed.
**Jason Plumb** 22:37 Okay, cool.
Yeah, I learned a thing today. And it's not even 9, 30 yet.
Kind of just trying to focus on the newer stuff.
Well, this is odd that should work. Everyone loves this feature.
**Jay DeLuca** 23:06 Yeah, it's not obvious to me that this person is doing anything wrong. But I wasn't sure if it was like a that maybe the operator wasn't injecting the them correctly or something. But I started looking into this, and I didn't see anything obvious.
**Jason Plumb** 23:20 Yeah, it'd be cool if they could do a repro.
So is this about the operator?
**Jay DeLuca** 23:27 No, this is just for the environment variables. But I think what they're you, the operators, what they're using here in the the Yaml manifest.
**Jason Plumb** 23:42 This is spelled right.
**Jay DeLuca** 23:44 Yeah. I checked that. The the variables all look correct.
**Jason Plumb** 23:48 Yeah, and we support splitting on comma, probably. Yeah, okay.
**GZ Gregor Zeitlinger** 23:54 Yeah, looks, correct.
**Jason Plumb** 23:57 And I wonder, though like, because this is Yaml, can it support a list like, should this be 2 things on 2 separate lines? I don't know.
**GZ Gregor Zeitlinger** 24:06 So environment variables must be strings.
**Jason Plumb** 24:09 Oh, and then this is environment. Yeah, yeah, ignore me. Correct. Yeah.
All right. Weird, alright triaged.
I can't get the correct trace. Id?
Hmm!
That's cool. There's a little repro.
Do we have a label for? I think we have a label for that, don't we?
**Jay DeLuca** 24:52 Yeah, repro-provided.
**Jason Plumb** 24:58 Okay, we have instrumentation.
**Jay DeLuca** 25:05 Yeah, we do have instrumentation. And we we instrument a lot of the other Rx Java, like observable dot.
**Jason Plumb** 25:15 15.
**Jay DeLuca** 25:15 The ones. I looked into this briefly this morning. So I don't know if we're just missing a particular type of the observable
**Jason Plumb** 25:30 2, 5.
What version of it?
**GZ Gregor Zeitlinger** 25:36 Old.
**Jason Plumb** 25:37 Yeah, I was gonna say, what?
Yeah, that's a few versions old.
Has Rx had any updates to it?
**Jay DeLuca** 25:49 I don't think so. He's on Rx 2 as well.
**Jason Plumb** 25:53 So old Rx. And old instrumentation.
And when do you suppose 2 2 was released like 13 months ago? If we just, if we were consistent on months, so that would be all the way back in like last summer.
So there's been a few things. But I don't. This seems like a problem I don't know.
**GZ Gregor Zeitlinger** 26:21 Yeah, this looks like one like a fix.
**Jason Plumb** 26:24 You know. Maybe sorry for just doing this on the call. Y'all.
**Jay DeLuca** 26:42 That's fine!
**Jason Plumb** 26:49 Right?
It's a trio. Okay, cool.
**Jay DeLuca** 26:54 I think we're close to like 400 issues. So we should.
**Jason Plumb** 26:58 I know. I think I think Core is worse, isn't it?
No core is way better. Okay, yeah, this is, this is a lot of issues. Yeah.
well, that one needs to be looked at.
**John Watson** 27:16 We should at some point go through the core repo and see if there's a bunch of old stuff we can close, though.
**Jason Plumb** 27:23 Yeah. And that can be a separate meeting, or just like a divide and conquer kind of effort.
**John Watson** 27:27 Get it.
**Jason Plumb** 27:28 Doesn't have to be on the Sig call.
**John Watson** 27:30 Very true.
**Jason Plumb** 27:31 But in midsummer. Why not? Why not? What else are we doing?
Certainly not.
**Jay DeLuca** 27:37 Okay.
**Jason Plumb** 27:37 Certainly the 6 of us are not taking vacation.
**Jay DeLuca** 27:41 Similar to that is like. I wonder if if there would be some benefit to putting in some rules around Prs being open for like over a year, and just like automatically close them.
**Jason Plumb** 27:54 Yeah, does the stale check? Take that into consideration.
**Jay DeLuca** 28:00 I don't know that I've ever seen a Pr. Closed.
**Jason Plumb** 28:03 Like we have that stale label right? Like we have.
**Jay DeLuca** 28:06 I think if you put needs customer or yeah, if there's automation that if you put needs author feedback, it. Stat, it slaps it with the the stale.
**Jason Plumb** 28:15 Let me get this one out of here.
So none of these are Prs, though.
**Jay DeLuca** 28:21 Right.
**Jason Plumb** 28:23 And yeah, needs. Author. Feedback is like one of my favorite things of all time. And the automation around that is like so helpful.
is there a way to limit this to? Can you look at the labels for? Prs, yeah, let's do this.
None are marked stale.
any closed? Oh, interest. Oh, but they were all needs author feedback. So I think the workflow includes a stale like I think it needs author. Feedback sits there for one or 2 weeks, or whatever, and then it gets marked stale, and then it gets closed for being stale too long.
**Jay DeLuca** 29:00 Yeah. So we do have a workflow. We just got us tag them.
**Jason Plumb** 29:04 Yeah.
yeah, it has to be manually tagged. There's no automation around like this has been out there for 2 years, because there certainly are some that have been.
but that's also just the nature of like big, long living projects or long lived projects. I think.
**Jay DeLuca** 29:22 Yeah.
**Jason Plumb** 29:22 Yeah.
Okay, so this one is new.
No such method. Error. Patch logger in the boot drop tried to add a custom instrumentation and build into a new custom distro, and it won't run.
Oh, is this is this one of the Apac folks? Maybe I don't. I don't know any of them unfortunately relocate. Hmm!
It's odd.
**John Watson** 30:16 They said, what version of Jdk. 21 did there were there new things added to the jewel logger in Jdk. 21, that we're somehow missing.
**Jason Plumb** 30:31 That is a good question. I don't know how to look that up easily.
**John Watson** 30:36 Yeah. Well, I mean, you could look at the source, and there should be a sense in the if you look at the source of of you know, of the jewel logger.
**Jason Plumb** 30:45 Well, what do you think is the easiest way to get there?
**John Watson** 30:48 Idea.
**Jason Plumb** 30:51 Yeah, I'm not sharing that right now.
So this is 8. Can I just substitute that?
That'd be too easy.
Here's 6.
Yeah, no, I mean, it's a good question. I think that's the right question to be asking. It's a good question to be asking.
You could comment on that capturing application. Logs does not work. Yes, it does and then you see these words, and you get scared.
**Jay DeLuca** 31:31 Yeah, it's been a lot of web logic stuff popping up recently. Lori's been going back and forth with this guy.
**Jason Plumb** 31:38 Oh, okay.
I think we can take this off.
Floury's been working with him.
Yeah, that would just take someone to look into that propagator error for azure azure function.
I'm not quite following this. Okay, so calling from parent to child.
presumably these are 2 separate functions is always creating 2 spans under parent trace, id.
**GZ Gregor Zeitlinger** 32:59 Or cream to.
**Jason Plumb** 33:02 Expected one parent.
I'm not following this.
**GZ Gregor Zeitlinger** 33:07 I also don't get it. If it's 1 function or multiple.
**Jason Plumb** 33:11 Yeah, I'll just ask.
**GZ Gregor Zeitlinger** 33:15 Like? How do we reproduce it?
**Jason Plumb** 33:18 Who is this? Avb.
That's pretty generic. Sorry, but I am. Gonna do that alright declarative config support, Robert, your favorite topic. Oh, this is from Gregor Gregor's favorite topic as well.
**GZ Gregor Zeitlinger** 34:12 I want to have more people whose favorite topic that's.
**Jason Plumb** 34:15 Well, I mean, it's Jack's favorite topic as well. But yeah, okay.
I think we can just remove this one like that's.
**GZ Gregor Zeitlinger** 34:26 Yeah, right? It does not need that labors.
**Jason Plumb** 34:30 Yep.
another one from Gregory.
Oh, yeah. So the yeah, this is all this, specifically, is one of Robert's favorite topics.
**GZ Gregor Zeitlinger** 34:46 Yeah, we just discussed it in the previous meeting.
**Jason Plumb** 34:49 And.
**GZ Gregor Zeitlinger** 34:53 We basically have to convince Jack that this is a valid use case, or he convinces us that it can be done in a different way.
**Jason Plumb** 35:02 Yeah.
Okay, well, I just remove. I remove that label and we can move on from that. It's a that's a bigger discussion.
Great old commands fail with Sonotype. That's not true. Is that true?
That is not true? No way.
These lines, what lines?
It's Elvis. Oh, and it throws.
I don't have those set, do I?
**John Watson** 35:34 Yeah, but nobody should be running upload. Release, bundle.
**Jason Plumb** 35:38 Well, apparently upload release bundle is part of running tasks, or that gets evaluated. When.
oh, is this? Because yeah, this needs to be moved into the do first.st I think that's the problem.
I'm a gradle. I'm a gradle expert. I know lots about Gradle, and I love it so much. So I'm gonna speak confidently about this and say that I think that these should be moved into the do first, st because otherwise they get evaluated at configuration time, and not at Runtime, or whatever these other magical phases that Gradle has is yeah.
**Jay DeLuca** 36:13 Not able to repro, though.
**Jason Plumb** 36:15 Can you? Have you tried it just now.
**Jay DeLuca** 36:18 I just did a great old task. Right? That's.
**Jason Plumb** 36:21 Yeah. Did you do a clean checkout?
I mean, that shouldn't affect anything. Never mind. Yeah. Gradle tasks is the claim.
**Jay DeLuca** 36:34 It all worked for me.
**Jason Plumb** 36:39 Okay, I'm gonna try and reproduce it.
Has this person been around before.
**Jay DeLuca** 37:03 Actually well, he he actually just submitted a Pr in instrumentation repo to add Grpc metrics.
he! He picked up a Pr from someone else who may or may not have abandoned it, and he's.
**Jason Plumb** 37:20 Okay.
**Jay DeLuca** 37:20 Like.
Finished it up.
**Jason Plumb** 37:23 I reproduce this problem locally.
**Jay DeLuca** 37:26 Really.
**Jason Plumb** 37:26 Yeah, yeah, I get, could not create task upload resource bundle.
Sona type user, not set. It's exactly those lines. So I can. I will just assign that to myself.
just because I'm a glutton for punishment.
**John Watson** 37:43 You know that this is funny. I you know I haven't worked in the instrumentation repo for several years.
but I think this issue has been out there for actually, for a very, very long time.
**Jason Plumb** 37:55 This one.
**John Watson** 37:55 Yeah, I mean not the issue. But I think that this has been happening. I remember checking out the station repo. I don't know. 3 years ago, and trying to Bootstrap stuff and running into something almost exactly identical to this.
**Jason Plumb** 38:10 Yeah.
**John Watson** 38:11 Like, yeah, I'm not gonna worry about it. And I stepped away and didn't do anything about it.
I think I think my hack was. I just like, set an empty environment, set the environment variable to garbage locally.
to get around it.
**Jason Plumb** 38:27 That that's sounding familiar to me as well like maybe I had that in my granel properties, like my global Greenle properties.
**John Watson** 38:32 Yeah, yeah, something along those lines.
**Jason Plumb** 38:35 I have to set a reminder for myself, otherwise I will never get come back to this.
**GZ Gregor Zeitlinger** 38:44 Okay.
**Jason Plumb** 38:46 Cool.
Yeah, I mean, that's a bad experience for someone, right? If they just checked it out and it fails on even like you're new to the project you're like, I I just want to even know what tasks are available for this massive project, and if it blows up in your face like that's that's bad. But I'm wondering why it didn't fail, for Jay.
**John Watson** 39:09 But if iron barrel's probably set somewhere secret, hidden.
**Jason Plumb** 39:13 I mean, I'm on Java 17 right now. I don't think that's gonna affect that at all.
Now, that's interesting.
Okay, we haven't looked at. This is a little bit old.
but there's no traction on it yet.
Support for custom created message, listener, container in spring cloud aws.
**John Watson** 40:01 I love. How message listener can. It's spelled differently every time.
**Jason Plumb** 40:06 It's a tough one we don't do, do we? Do. Propagation by default does not use this, which makes it unknown to the job agent custom container does not use this one.
I don't know what this means in the context of spring cloud. Aws, we've never used that like I'm I'm confused of what this seems like an Sqs instrumentation problem. But then it's like specific to spring cloud somehow.
Does anybody does anyone else understand this?
**Jay DeLuca** 41:04 I think the our spring cloud.
I think our spring cloud stuff is just Sqs instrumentation.
**Jason Plumb** 41:12 Okay.
Okay.
**Jay DeLuca** 41:16 Looks like we instrument the Sqs. Template.
**Jason Plumb** 41:29 Dang! There's no help wanted.
Do we have spring? It's not spring boot starter. It's just spring cloud. Okay.
Oh, I didn't even need to refresh. This is like, I think it was pulling this off as we were getting to them.
Here's another spring cloud thing.
I have this really petty like ultra petty pet peeve. When people like put like articles in front of stuff like this.
I don't know.
It's petty, I mean. I guess I'm sorry this one's correct, because.
**John Watson** 42:25 That looks pretty good.
**Jason Plumb** 42:27 The agent in this case. Okay, I just I see it so much where people are like. I turned on the open telemetry, and then I had a problem like, where is that coming from?
That's a Netty thing. Huh?
**John Watson** 42:53 What version of the agent are they using.
**Jason Plumb** 42:57 Let's see 2, 18 current 1, 8.
**John Watson** 43:04 Oof.
**Jason Plumb** 43:05 Yeah, like, yeah.
Oh, hmm!
Have you tried it without Spring Cloud sleuth?
I'm gonna ask that question.
**John Watson** 43:25 So they're using the agent and sleuth.
**Jason Plumb** 43:28 They are.
**John Watson** 43:29 That hmm.
**Jay DeLuca** 43:32 I was looking into this a little bit, and so it led me down a rabbit hole of really old issues from years ago, and one of the comments was from John Watson, saying that you shouldn't use the 2 competing.
**Jason Plumb** 43:45 Yeah.
**John Watson** 43:45 Yeah, and depending on what version of sleuth I know there's there's issues with the way context is propagated which I can definitely imagine causing something along these lines, but I haven't looked at any of this for years, so.
**Jason Plumb** 44:02 I mean, this is, this is totally the kind of thing that would happen to.
**John Watson** 44:06 Yeah.
**Jason Plumb** 44:07 Yeah, alright. We'll see if they respond.
That's that's most of these like needs triage.
**Jay DeLuca** 44:21 I I submitted a Pr. For this one.
**Jason Plumb** 44:24 Oh, you did. Okay, we can remove that. Then seems like it's been triaged. If you fixed it.
**Jay DeLuca** 44:31 Yeah, I should. You can assign it to me, too, if you want.
Not that we really do that.
**Jason Plumb** 44:37 This one, yeah.
**John Watson** 44:41 Still at Splunk.
**Jason Plumb** 44:43 He is. Yeah, he's still. I think he's still over on.
**John Watson** 44:46 Not on vacation. As far as I know, it's pretty much on vacation going to some crazy Spa all the time.
**Jason Plumb** 44:52 I can neither confirm nor deny. If that constantly happens.
I know he's on the developer productivity team. It's an internal team.
Yeah, he's been he's been using the SDK a lot lately, and he comes up with weird questions about trying to configure different temporalities like simultaneous multiple temporalities, which is not something we're good at.
Yeah.
**Jay DeLuca** 45:27 And one thing about this is I ran into some issues with keeping it on Java 11. So I just updated the containers to 21, which it all seemed to work locally. But I also touched the windows container, which I'm not able to test, so I'm just hoping that it.
It looked like it was pinned to a very specific version before, and I'm hoping that wasn't.
**Jason Plumb** 45:53 Yeah.
**Jay DeLuca** 45:53 Intentional.
I'd be able to test it, though, actually might be able to take the published version from my fork and try and run the smoke tests in Ci.
**Jason Plumb** 46:14 I forget the complete reason why we were doing these Shaws, but I think it was. I think it's a different approach to putting versions in here. And it's like more specific right? Because this, this, I think, allows whoever controls eclipse Tamarin to like push another like Docker doesn't prevent you from pushing same version multiple times. And so what is secure one time is maybe not secure, or it could if it could be tampered with. And I think the Shah is what prevents. That is why we I think it's why we were using those.
**John Watson** 46:45 Well, it's not a version. It's just a tag. And that's why that's why it can be pushed to multiple times.
**Jason Plumb** 46:51 Right? Yes, yes, yeah.
But everyone I mean, I mentally treat it like a like a version, even because it it often looks like semver, even though it's just a tag.
**John Watson** 47:02 Looks like a version.
**Jason Plumb** 47:03 No, but.
**John Watson** 47:04 Really just.
**Jason Plumb** 47:04 That is, that is a vector for supply chain attack. And so that's why. So it might be worth looking at, Jay to see if you can find the shop for that, for whatever this version, latest version for 21 is, and just stick it in there.
**Jay DeLuca** 47:18 Yeah.
**Jason Plumb** 47:18 And then renovate, should come along and update those as needed.
Like, I think it will look at these.
**GZ Gregor Zeitlinger** 47:25 But renovate, will also add the Shah.
**Jason Plumb** 47:29 Yeah, that's what I mean. Like, once you get the Shawn in here, and this is fine to validate that it works. But we should get that sean there.
cause I think that's more consistent. But and it's passing right?
Yeah.
**Jay DeLuca** 47:42 It is passing, but I think that just means that they were able to build the containers. I don't. I think the actual smoke test reference like a really old tag. So after this, this finishes, I was gonna go and update those to point to something newer. But.
**Jason Plumb** 47:59 Okay, okay, I'm just gonna put a comment asking for the Shaw again.
**Jay DeLuca** 48:05 Yep.
**Jason Plumb** 48:06 If that's reasonable.
**Jay DeLuca** 48:07 Yeah, yeah, I'll do that.
**Jason Plumb** 48:15 How about Asha?
And I don't mind being a little obtuse there, because we talked about it all right. Well, we did the Lord's work. There's also this one.
Is that the same one we were looking at? I thought we were looking at needs triage.
Well, whatever these are, the ones that are like hanging out there.
Okay, cool. Well, Does anybody else have anything they want to do or talk about?
We don't have to take up the full hour.
Okay.
**John Watson** 49:16 Thanks for driving Jason.
**Jason Plumb** 49:17 Yeah, yeah, no worries and, Watson, I'll reach out to you later today, probably just to get a head start on that.
**John Watson** 49:23 Yeah, just ping me if you need need. When when you need to review.
**Jason Plumb** 49:27 Cool.
**Jay DeLuca** 49:28 How about?
**John Watson** 49:29 I'll need a merge is what I'll need.
Yeah, yeah, no, I understand.
**Jason Plumb** 49:32 Okay. Cool. Cool. Thanks. Everyone.
**Peter Findeisen** 49:35 Thanks.
**Jason Plumb** 49:36 Take care and have a good weekend.
**Robert Niedziela** 49:39 Hi.
**GZ Gregor Zeitlinger** 49:39 Hi.
