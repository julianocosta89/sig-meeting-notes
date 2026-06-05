SIG: Swift SIG
Date: 2026-06-04
Duration: 27 minutes
============================================================

## Zoom Recording Transcript

**Vinod Vydier** 01:07 Hey, Nacho.
**Bryce Buchanan** 01:15 Hello.
**nacho** 01:15 Hello?
I was thinking about what's up here.
**Bryce Buchanan** 01:32 Let me pull up the meeting notes.
There we go.
**nacho** 02:30 Yeah, I have updated that content. I just copied and pasted from last week and changed the date.
**Bryce Buchanan** 02:36 Excellent, thank you.
**nacho** 02:38 Yeah, no.
We are the same people.
**Bryce Buchanan** 02:42 Oh yeah, Nacho. So, for, my trip to… Madrid, I'm gonna be there, I think, Sunday?
And I don't have anything going on on Sunday, and… Monday, I think, is pretty open as well, so maybe we could, like.
grab dinner or something Sunday or Monday night.
**nacho** 03:05 Okay.
Yeah, I will… I… yeah, I will send you my phone number, probably. Okay, yeah. You can use WhatsApp or something like that.
**Bryce Buchanan** 03:13 Cool.
**nacho** 03:14 Which will be… Great.
**Bryce Buchanan** 03:18 Grooting. Alright.
Yeah, let's get started then.
**Vinod Vydier** 03:22 we should have Hotel Swift get-together.
**Bryce Buchanan** 03:25 Oh, I don't know if I'll be able to do that, unfortunately. What is the… what time is it right there, or there right now?
**nacho** 03:33 Here.
6PM.
**Bryce Buchanan** 03:35 6 PM. Oh, okay, yeah, maybe we could, I don't know.
**nacho** 03:39 I don't know.
Yeah, they… Y-yeah, you're…
**Bryce Buchanan** 03:44 We have Hotel Swift, cocktails.
**Vinod Vydier** 03:51 I can get, What is that, coconut rum?
I'm actually thinking about that today.
**Bryce Buchanan** 03:59 Alright, I didn't get a chance to do this yet, so that's still to do.
I'm not sure if Ari had a chance to look at this. I messaged him.
**nacho** 04:16 Yeah, yeah, he has… he has created.
**Bryce Buchanan** 04:19 That would be…
**nacho** 04:19 Yes, regarding that.
**Bryce Buchanan** 04:20 Okay.
**nacho** 04:21 I think 3… 3…
**Bryce Buchanan** 04:24 Cool.
**Vinod Vydier** 04:25 You also have a doc, right? That's pretty cool.
**nacho** 04:27 Yep.
**Bryce Buchanan** 04:31 Random build failures, this has been fixed, I believe.
Just had to specify the arc in the architecture and the destination, and that… that resolved it.
I started to release, I'm not sure if this got merged or not.
**nacho** 04:51 Yeah, I remember I approved the PR, but yeah, I don't know if you finally merged it.
**Bryce Buchanan** 05:05 No, it's not been merged yet. I'm just… Do that really quick. Boop, boop, ba-boop.
Okay.
So, any new… or I guess here, I'll pull this… Down here… Yeah, okay, yeah, Will has, taken a son.
**nacho** 05:41 Yep.
**Bryce Buchanan** 05:42 Alright, cool. Will's working on that.
And, no movement yet on this.
Okay.
Any, any new topics we want to discuss?
like I said, I'm gonna go to my company All Hands next week, so I'm gonna not be attending unless I do it with Nacho at a bar, or something like that.
Yeah, should we just jump into, review, or PR review and stuff?
Alright, so here's… Ari's, PR… BlueStep has extracted its own reusable workflow… oh, I thought he already did this, or did he only do that on the main thread, main one?
Triggered both automatically or manually, which is great.
Transient fare without having to re-trigger full release. Good. Excellent. That sounds good to me.
**nacho** 07:02 Definitely is the way to go.
**Bryce Buchanan** 07:08 I just basically moved it into his own thing.
**nacho** 07:19 Yeah, that's right.
**Bryce Buchanan** 07:27 Ai check to lint pod spec. Yeah, okay.
Should lent pods back… Okay, yep, yep, yep. So if it changes, lint it, otherwise it's… you can skip it.
And just do a… Lint, allow warnings, include blah blah blah. This… Okay.
**Vinod Vydier** 08:10 How do we know how many people are using this?
Is there, like, some…
**Bryce Buchanan** 08:14 Apparently nobody, because nobody ever…
**nacho** 08:16 Does anything when it broke.
Yeah, I'm… I think there are some users, but probably they are not updating to the latest version, but yeah, or maybe just dropped, but I remember they… some… some users, more than one, asked for it, in the early days. Probably people also have moved to SPM now, but…
**Bryce Buchanan** 08:42 Yam.
**nacho** 08:43 Yeah, I'm in.
Yeah, you can also merge this, I think.
**Bryce Buchanan** 08:48 will do.
**Vinod Vydier** 08:52 On the Copod site, I don't… is there… they don't keep any track of the… downloads, like, Maven Central and so on has…
**Bryce Buchanan** 09:01 I don't, yeah, I don't think they do.
**Vinod Vydier** 09:02 I don't, okay.
**Bryce Buchanan** 09:09 It's a good question, Alan.
Let's do, I don't know, Alamo Fire.
Yeah, it's just… Yep.
**Vinod Vydier** 09:30 I like that.
**Bryce Buchanan** 09:31 At least they don't publish it.
Okay, let's… alright, so… Bots, bots, bots, bots, here.
Synchronize OpenTelemetry Singleton Resolve Data Races.
**Vinod Vydier** 09:49 It's funny, if you, if you're so…
**Bryce Buchanan** 09:50 bigger room.
**Vinod Vydier** 09:51 Search on the Coco Potts?
**Bryce Buchanan** 09:53 rep, Bill.
**Vinod Vydier** 09:54 to search on CocoPods for OpenTelemetry SDK, it shows a different… Project.
**Bryce Buchanan** 10:01 Yep.
**Vinod Vydier** 10:04 And it's, like, some 0.016…
**Bryce Buchanan** 10:07 Yeah, we tried to contact them and say, like, this is not the official OpenTelemetry thing, and .
**Vinod Vydier** 10:14 They never responded, right?
**Bryce Buchanan** 10:16 Yeah, they never responded. It's, I mean, it's a dead… it's a dead… Yeah.
**nacho** 10:21 Yeah, or they are sniffing data, who knows, right?
**Vinod Vydier** 10:26 And everything is also in Chinese restaurants, all the time.
mission.
That's hard to read.
**Bryce Buchanan** 10:33 Okay, so this is a draft PR, Update destination architecture, and… oh, yeah, so we got this approved, we just need to merge it.
And… okay, so that's draft… And this one was having some problems. What was the problem here?
Here we go, okay, so this should… Well… Hmm… Will it run against the main branch, or will it run against… Oops. Or we'll run against its own version of it.
Let's see… We'll try running it again and see if it fixes it.
Come on now.
That's not what I want.
Is it doing it again?
**nacho** 11:40 Nope.
Yeah, the thing is that… I don't know why we cannot rerun, sometimes, some PRs.
**Bryce Buchanan** 11:49 Is it because it's from somebody else's repository?
**nacho** 11:52 No, because… Everybody creates PRs from a fork, right?
**Bryce Buchanan** 11:59 Damn.
**nacho** 12:00 The thing… I don't know if it's something in the settings of… on the… on the core.
That doesn't allow to… to… to rerun.
I don't know.
We have always rerun an OpenTelemetry Shift. I don't know how many times we have tried that on OpenTelemetry Shift Core without changing code.
**Bryce Buchanan** 12:21 So weird.
**nacho** 12:22 created it, yeah.
**Bryce Buchanan** 12:28 I mean, should we just Well, we can't… I guess we can't maybe enable… here, let's try this.
Hmm… Hmm…
**Vinod Vydier** 13:04 So is there, like, a periodic thing as well? Or just when you have a new.
**Bryce Buchanan** 13:09 Well, did… I swear that we were able to do this earlier… And get it to rerun, but now it won't… won't.
**nacho** 13:18 Yeah, but I don't know if that's because we are not proper admins.
Maybe in this project.
Right. That's my… I don't… I don't know if we have the same rights or something like that.
As it was created later, I don't know.
**Bryce Buchanan** 13:35 Yeah.
Very weird.
**Vinod Vydier** 13:42 It's only failing on core?
Code is a project that is created later, right?
**Bryce Buchanan** 13:56 Here, I'm gonna add a note on here.
**nacho** 14:10 Maybe we can ask Copilot.
**Bryce Buchanan** 14:12 Oh yeah, that's not a bad idea.
Where is that at?
Oh, no, that's not it. Mmm, that's… oh, I see. Interesting.
**nacho** 14:26 Yeah, ChatGPT, or, I mean… Anything that… Yeah, I am not very trustful in Copilot, but…
**Vinod Vydier** 14:34 No, but this is GitHub. GitHub has its own…
**nacho** 14:37 Yeah, in theory.
**Vinod Vydier** 14:39 You know.
**Bryce Buchanan** 14:50 Maybe it'll do it for us.
**nacho** 15:07 Yeah, it's protection rules, or something like that.
**Vinod Vydier** 15:14 Here is in blocked state.
**Bryce Buchanan** 15:16 That's not what I asked it.
**Vinod Vydier** 15:18 I'd already given the answer.
Getting a fix.
No, no…
**Bryce Buchanan** 15:51 Do my job, AI.
**nacho** 15:55 Yeah.
**Bryce Buchanan** 16:02 Useless.
**nacho** 16:04 Yeah, that's… that's useless. It's probably some… some kind of permissions that Or maybe they changed something on their… I don't know.
**Vinod Vydier** 16:41 And, you can also mention that you have, Privileges, right?
**Bryce Buchanan** 16:53 Hmm… hmm…
**nacho** 16:59 Definitely, we were able to make it run once. I don't know why we cannot fully run, that's the key point.
**Bryce Buchanan** 17:15 Am I not one of the repository maintainers, is that why?
**nacho** 17:20 And you are not one of them.
But I am a… I am a maintainer.
I am in that name, right?
And I cannot run it.
**Vinod Vydier** 17:30 Oh, or maybe because you… Ran it, and it has to wait for one of the other folks to approve it?
**nacho** 17:38 The one who ran it the first time?
**Bryce Buchanan** 17:42 Good news! You are a maintainer!
Good news, everybody!
**nacho** 17:56 Yeah, I cannot run it either, so…
**Vinod Vydier** 18:11 Genuinely unavailable.
**Bryce Buchanan** 18:12 Let me try… let me try, doing it through… Maybe I can… Maybe we can try this.
G… H… Rerun… Mute.
Oh, good.
Oh, okay, okay.
Let me try dragging it in.
**nacho** 18:52 Another option is that The branch or committee is not available anymore.
**Bryce Buchanan** 18:58 Oh, yeah, maybe, maybe.
**nacho** 19:01 But we… I can't…
**Bryce Buchanan** 19:04 I mean, we should just re…
**nacho** 19:05 I checked, I checked… I could navigate to that repository.
**Bryce Buchanan** 19:11 Oh, interesting, okay. Unable to retry this workflow run because it was created over a month ago.
That's why.
**nacho** 19:20 But we have been, like.
We have to retry it many times, right? In every meeting, we try to run it again.
**Bryce Buchanan** 19:30 Yeah.
**nacho** 19:31 okay, so the only way is that they have to change the code?
**Bryce Buchanan** 19:36 Yeah, do, yeah, push, do something.
Let's… let me try… I'll ping him again.
**nacho** 20:19 Yep.
**Bryce Buchanan** 20:46 We'll see if we can… If he, responds to that.
Okie dokie. I think that covers everything in Core.
Dependency, I haven't had a chance to look at that.
Okay, alright, let's look at… Domain repo… Same things here from Ari.
That's interesting.
Well, I guess it has to do with all these ones, yeah.
Okay.
What do you think? Merge it?
**nacho** 21:54 Yep.
**Bryce Buchanan** 22:02 Very good… And chores, chores, chores… And then this one also was approved. Ari did that one. Thank you, Ari.
There we go.
And… configurable lifecycle…
**nacho** 22:39 Yeah, this is the one doubling.
Evaluated last week, that we.
**Bryce Buchanan** 22:42 Nope.
**nacho** 22:43 Billy, also.
**Bryce Buchanan** 22:44 Yeah.
**nacho** 22:45 We haven't.
**Bryce Buchanan** 22:46 Had a chance to really look through it yet. I mean, from what I saw, it looks fine. Oh, here, let me approve these runs.
Was it… okay, that was ready for view last week.
Okay. I thought Billy was gonna… was gonna review it, but, Yeah, we can take a look at that.
get your… let's all take a… take a review of that one.
**nacho** 23:19 That, that, yeah, he, it wants to put V-not again in… In… into the, retired, or… or the…
**Vinod Vydier** 23:30 I need to… I need to show more activity, I think.
**nacho** 23:33 Yeah. So, yeah, you can discard that, that pillow.
**Vinod Vydier** 23:38 Maybe I need to add some comment on that?
No, don't.
**Bryce Buchanan** 23:41 I just say, I'm still here.
**Vinod Vydier** 23:46 Hmm.
**Bryce Buchanan** 23:48 There's a draft here, update hotel log handler, that's still in draft. So, waiting on the release. I'll, I'll make a mention.
**nacho** 23:59 Oh, the distributed trust in Britain, also.
**Bryce Buchanan** 24:03 Oh, no, wait, hold on.
What was that one? I'm getting confused now.
Oh, we're just waiting for a resolve on the conflicts here.
**nacho** 24:22 Yep.
You commented on that last month, yeah, that's funny.
**Bryce Buchanan** 24:53 Okay. Here… Swift distributed tracing, waiting for the updates. Okay, yeah.
**Vinod Vydier** 25:10 Is this the one that, apple or some of you.
With no doubt, I appreciate it.
**Bryce Buchanan** 25:23 What's that?
**Vinod Vydier** 25:24 Is it the Apple's distributed tracing bench?
**Bryce Buchanan** 25:28 I believe it is…
**Vinod Vydier** 25:30 Okay.
**Bryce Buchanan** 25:31 Is that what that is?
**nacho** 25:32 Yes, yes, yes, yes, it's the Apple, the Apple… Let's do the tracing bits, yes.
**Bryce Buchanan** 25:38 No, that's a draft, and that's a draft. Okay, so let's take a look at the issues… Yeah.
**nacho** 25:43 Harold wants.
**Bryce Buchanan** 25:44 And those are all old, so no updates here. Alright, cool.
Sorry.
Okay.
Alright.
Okie dokie. Anything else?
Nope. Alright.
**Vinod Vydier** 26:24 I'm gonna… I'm gonna add some maliburum next week in my tea.
**Bryce Buchanan** 26:29 You're gonna add what?
**Vinod Vydier** 26:30 The Maliburum in my tea.
Next week.
**Bryce Buchanan** 26:34 Okay.
Oh, yeah.
All right.
**Vinod Vydier** 26:40 Okay.
**Bryce Buchanan** 26:41 I'll, I'll, see you next time, Nacho. Hopefully, I'll see you next time.
**nacho** 26:48 See you next week. Yeah, I will send you my phone, so… So you can add me to WhatsApp or something like that, so we can.
**Bryce Buchanan** 26:54 Yes.
**nacho** 26:55 better.
**Bryce Buchanan** 26:56 Sounds good. All right. Cool. See ya. Have a good weekend, everybody. Bye.
**nacho** 27:01 Bye.
