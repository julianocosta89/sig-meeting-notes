SIG: Community Demo App SIG
Date: 2026-07-08
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Matt Wimpelberg** 02:26 Hey, Juliana, how's it.
**Juliano Costa | Datadog** 02:29 Hello there!
Okay.
**Matt Wimpelberg** 02:31 Nice to finally meet you.
Good, good.
**Juliano Costa | Datadog** 02:33 Likewise.
**Matt Wimpelberg** 02:37 Sorry about, sorry about earlier in the week, the, the back and forth we had. I know it was a little frustrating.
**Juliano Costa | Datadog** 02:43 No worries, I was just, on a bad day, but
**Matt Wimpelberg** 02:47 No, I know. But also the use of the AI coding agents, they really help. But there are definitely times where we rely too much on them. So I'm learning that balance for sure. And it's been a great help in this whole process for this PR.
**Juliano Costa | Datadog** 03:03 Yeah, I I feel the same. I started seeing a couple of prs with like Two lines of code.
where 2 lines of code that actually changed.
But then there is, like, 10 lines of comments added to the.
**Matt Wimpelberg** 03:21 Oh, yeah, yeah.
**Juliano Costa | Datadog** 03:22 And I'm like, why? Then I tried to add something to the agents MD. Let's see if that changes, but yeah, it's,
**Matt Wimpelberg** 03:31 Oh, yeah, I saw that. That actually came up from my Docker file. I think there were too many comments, so I took them out.
I changed it.
**Juliano Costa | Datadog** 03:41 Yeah, like, yeah, in your case, I… In your PR, I wasn't reviewing the code yet.
I was reviewing the… I was reviewing it worked.
So I don't think I… Oh, no, I actually reviewed the code. That was my initial review, where I asked you, like, what was that actually doing? Yeah, yeah, yeah, I did that.
The,
**Matt Wimpelberg** 04:09 I was so frustrated because I had everything working, and I was running… so I use a Mac for work, but I have a Linux laptop that I use on my own, which is x86. So everything worked, and the next day, I saw that your build… you had K6 errors.
And then I started digging in deeper and I saw that it was an ARM issue. But I was like, oh, I got everything working. I went through everything. And then the first thing when he builds it, it fails. But it was a good finding because we can use the Grafana K6 image as the base instead of Debian.
**Juliano Costa | Datadog** 04:38 I was trying to.
**Matt Wimpelberg** 04:39 We were trying to build it like more vanilla so that it was Debbie in with everything installed on top of it. But the Grafana K6 image is fine. And then we do everything from there as in the new.
You know, the new commits.
**Juliano Costa | Datadog** 04:51 Mmhm.
Yeah, but, I mean, K6 is open source, right? And it's…
**Matt Wimpelberg** 04:56 Yeah.
**Juliano Costa | Datadog** 04:57 Yeah, I don't mind adding that to the demo, and I think… It also shows another tool that is supporting OTEL natively, so… Yep. I like that.
**Matt Wimpelberg** 05:10 So.
**Juliano Costa | Datadog** 05:11 One thing that I, that I noticed while, reviewing today was that… You are not adding metrics.
So I think K6 exports metrics via OTOP. This was on your pitch on the issue.
**Matt Wimpelberg** 05:32 Yep.
**Juliano Costa | Datadog** 05:32 But we could… sorry.
We do not have any Go metrics from the Go part of the project, like this hotel.go file.
**Matt Wimpelberg** 05:44 Okay.
**Juliano Costa | Datadog** 05:44 I'm not sure how that interacts with the K6 itself.
So yeah, I was just wondering.
**Matt Wimpelberg** 05:55 Yeah, I'll find out, how we can get to the metrics, and I think it's sending traces, but.
**Juliano Costa | Datadog** 06:00 Yeah, so, in… in the… in the hotel.go, you have traces and logs.
And…
**Matt Wimpelberg** 06:07 Oh, yeah, yeah.
**Juliano Costa | Datadog** 06:09 But we could add metrics. And for Go, we have the runtime metrics as well. So that would also be something that we could add. And the resource detector.
to… if you take a look at, I think it's Recommendation Service.
We have a couple of resource detectors in there, so… That would be something. But I think we can maybe we can add as a follow-up on this PR. Let's discuss this, get this one merged, and then we follow up on that.
**Matt Wimpelberg** 06:45 But let's.
**Juliano Costa | Datadog** 06:46 Patient life.
**Matt Wimpelberg** 06:49 Metrics would be a priority.
**Juliano Costa | Datadog** 06:51 Mmm… at… So this is what… let me… let me bring the things that I have here on my screen real quick, and we can discuss.
Sorry about the workaround on the way that I will share this.
can I share just part of my screen?
portion of the screen share.
Which portion am I sharing?
Okay.
So, if I'm sharing correctly, On the top, you… off.
Zone is on my way. Okay. On the top, we have the load generator running now, the one that we have deployed with the demo.
So, in average, we have, like, one dot something giga here.
For memory, and… 2 chorus?
As CPU usage.
On the PR from Matt.
We have reduced that to, like, 300-something.
For memory, and… Yeah, I would say, like… 400 something for, cores as well, like, mini cores.
So, I think that would be a great… Addition to the demo?
**Pierre Tessier** 08:29 That almost feels fake. What are we missing in terms of capabilities here?
I'm not gonna say 6.
**Juliano Costa | Datadog** 08:35 That's a thing that I wondered as well. But then when we take a look at Jaeger, let me share my screen now. So I haven't accessed the the UI. So I just have like the The traffic that the load generator is sending.
we can see basically everything that we we have in the Logen today.
So… Well, I haven't seen this 134 spans before.
I don't know what happened here.
But it's like a checkout moti, so this is,
**Pierre Tessier** 09:18 That seems right. Although we didn't have this before. Before, this would have came off as multiple traces.
From local.
**Juliano Costa | Datadog** 09:24 Yeah.
**Pierre Tessier** 09:25 it would have been… it would have been one trace for each action. This one here seems to combine them all as a single trace. I don't know if that's… that is what we want, though.
**Juliano Costa | Datadog** 09:35 Mmhm.
**Pierre Tessier** 09:36 Because the transaction, like, even on the multi… on the multi-checkout thing, you'd end up with multiple traces on the standard back end, since he, you know… It's not a session, it's.
**Juliano Costa | Datadog** 09:48 Yeah, I…
**Pierre Tessier** 09:49 Thanks, Dad.
**Juliano Costa | Datadog** 09:50 Yeah, I think… I think configuration-wise, it's fixable.
I already had a couple of back-and-forths with Matt before, and I saw one trace that was getting, like, 200 spans or something like that, and he fixed it.
So I think… On the behavior side, we can reproduce. One thing that we…
**Pierre Tessier** 10:13 Is there a UI for cases?
**Juliano Costa | Datadog** 10:14 Wait a second. I'm not running the… Jesus Christ, sorry. I'm not running the new one. This is actually the one that we have.
Live now. Yeah. So this is ours.
**Pierre Tessier** 10:32 We need this.
**Juliano Costa | Datadog** 10:33 Okay.
**Pierre Tessier** 10:34 It…
**Juliano Costa | Datadog** 10:35 Good on them.
**Pierre Tessier** 10:35 No.
**Juliano Costa | Datadog** 10:36 120 spends, it's already…
**Pierre Tessier** 10:39 We need to fix that.
Yeah.
My next question, I guess, is, does K6 have a UI?
**Matt Wimpelberg** 10:48 No, so it'll be done in JavaScript.
**Pierre Tessier** 10:51 So there is… that's… that's the… that's probably the part that we're missing then, because with Locust, you have a UI, you can see what the load generator is doing. Does that UI provide value beyond being able to stop the load generator? I don't think so.
Right.
**Matt Wimpelberg** 11:06 I mean, I.
**Juliano Costa | Datadog** 11:08 Go ahead, Matt, sorry.
**Matt Wimpelberg** 11:09 No, I was gonna say, I don't know what you guys are getting value out of Locust in that sense now.
**Pierre Tessier** 11:16 Thank you.
Being able to stop the load generator and restart the load generator is, like, the only value I see with that UI.
Do we have a way to do this with K6?
**Juliano Costa | Datadog** 11:28 Yes, Dr. Kirk Hill.
**Matt Wimpelberg** 11:30 Yeah, I was gonna say, like…
**Pierre Tessier** 11:31 Wow. You.
**Matt Wimpelberg** 11:33 Maybe you have like, I mean, when you install it, you could add a flag to Helm or to Docker perhaps. But yeah, while it's running, like you would just kill the container. That wouldn't work in Kubernetes though, because you have another pod.
**Pierre Tessier** 11:46 Come on.
**Matt Wimpelberg** 11:47 If you killed the pod.
That's a valid point, though, because turning it off… like, if you want to generate organic traffic and turn off the load generator.
You wouldn't be able to as easily.
**Juliano Costa | Datadog** 12:00 On Helm or Kubernetes, we can scale down the deployment. I don't think, or even if we go with the Helm values that we have, we disable the logen, which is also easy to do with the setup that you and Tyler created here.
**Pierre Tessier** 12:18 Yeah, yeah.
**Juliano Costa | Datadog** 12:19 Okay.
**Pierre Tessier** 12:20 I'd disable it, I'm just… it requires a redeploy, that.
**Juliano Costa | Datadog** 12:23 You know, I honestly, I don't know how others use, but I rarely access locals.
**Pierre Tessier** 12:31 Yeah, this is probably a Pierre Tessier problem, because sometimes when I'm developing stuff, I'm like, get rid of all the noise, I just want my clicks only.
So, this is… yeah, I'm just…
**Juliano Costa | Datadog** 12:47 No, I agree with that.
**Pierre Tessier** 12:48 My own problems, you know?
**Juliano Costa | Datadog** 12:50 But I do that as well. The thing is that I never go to the UI to stop.
**Pierre Tessier** 12:54 You just.
**Juliano Costa | Datadog** 12:55 Just kill the guy.
**Pierre Tessier** 12:56 Yeah, I go to UI and hit stop, then start again.
**Shenoy Pratik Gurudatt** 13:00 I use the UI tool. I never hit start.
**Pierre Tessier** 13:02 I always only hit stop. It seems to be the only thing I do, but that's fine. Like, if my workflow now needs to be kill the damn container, that's probably easy. You can do that.
You know, I'm trying to think, is there a way we could do in Kubernetes Where, through a config option of some kind.
So instead of having to do a redeploy, we just… Change the config, and then kick the container, or kick the pod.
And when the pod restarts, it loads up its new config, and it knows not to do anything.
**Juliano Costa | Datadog** 13:34 I have an idea.
Matt, so if I got, I'm not a K6 expert at all, so, but if I got it right, we have this goal file.
That controls the cost to the JavaScript load, right?
**Matt Wimpelberg** 13:56 Yep.
**Juliano Costa | Datadog** 13:57 K6 is actually configuring the JavaScript code, but the controller is Go.
**Matt Wimpelberg** 14:05 Correct.
**Juliano Costa | Datadog** 14:06 Cool, so if the controller is go, we could add, open feature there with a feature flag that we enable or disable the load, and then we control everything in the flag DUI.
**Pierre Tessier** 14:20 Does this controller actively monitor K6 as well, or is it just it kicks it off and then it doesn't care about it?
**Matt Wimpelberg** 14:29 It's constantly reporting status on the runs that it's doing to generate the load, so it's constantly monitoring it. If you look at the log.
**Pierre Tessier** 14:35 But is it constantly controlling it? Can it say, hey, stop running?
**Matt Wimpelberg** 14:41 That's a good question. I'll find out.
**Pierre Tessier** 14:44 Because if it is, like, yeah, this is a feature flag now. This is super easy to do.
And we just have a feature flag that controls load generation.
**Matt Wimpelberg** 14:53 Oh.
**Pierre Tessier** 14:55 Yeah, that'd be fucking awesome.
**Juliano Costa | Datadog** 14:56 Awesome. Yeah, yeah, yeah. Awesome. And we, we already have.
We already have a feature flag for, Flooding the…
**Pierre Tessier** 15:08 Thank you.
**Juliano Costa | Datadog** 15:08 content.
So maybe we could, either Integrate both of them together, or have, like, I don't know, like.
**Pierre Tessier** 15:19 Yeah, maybe the flood could just be a slider, number of users.
**Juliano Costa | Datadog** 15:22 Yeah, exactly.
**Pierre Tessier** 15:23 You know what I mean? And then we default to 10, or whatever it is. If you want to flood it, make it.
**Matt Wimpelberg** 15:28 He's 5.
**Pierre Tessier** 15:29 or whatever 5. Sure. But that's yes. And if you set the 0, then that means we just do nothing.
**Juliano Costa | Datadog** 15:38 Mmhm.
**Pierre Tessier** 15:39 And then we have code in the Go controller to know how to work with that feature flag.
And as long as that Go controller does more than just monitoring, if it can truly control.
Yeah, that's the solution. That's… and the savings are significant, man. I love to save 2 gigs, or a gig and a half of memory.
Damn. Yeah.
**Juliano Costa | Datadog** 15:59 One thing that I that I also think why I think that would work is because Usually, when you run a K6 script, you call it, it runs the test, and then it stops.
So I think the Go service is actually re-triggering this test over and over again.
**Pierre Tessier** 16:21 Oh, amazing.
**Juliano Costa | Datadog** 16:22 So I think if we have like a feature flag right before this recalling, then we can control.
**Pierre Tessier** 16:32 I think we have a solution. Let's go ahead and get that done then, I think.
**Juliano Costa | Datadog** 16:36 So, so we wait on that to get the 3.0.
**Pierre Tessier** 16:40 And the only and the only downside is when you when you flip the feature flag, it's the current existing test needs to finish running.
And that's about it, which is fine, because not all feature flags are immediate anyways.
**Matt Wimpelberg** 16:52 And if it's really, like, super critical, you could restart the… reinstall it with, you know.
**Pierre Tessier** 16:56 Okay.
Again, I'm just looking for a way to… get rid of all the load in Jaeger, so I know that when I click a button, whatever trace shows up in Jaeger, whatever happens, it was me clicking on it, and not a load generator.
**Matt Wimpelberg** 17:12 Yep.
**Pierre Tessier** 17:13 That's really, and again, this is the Pierre Tessier.
**Juliano Costa | Datadog** 17:17 Mmhm.
**Pierre Tessier** 17:18 Although I'm sure Giuliano runs into it every once in a while, like, when we're doing dev work, you know, like, get the load gener.
**Juliano Costa | Datadog** 17:26 Yeah, no, I killed the Logen constantly, but I killed the container.
Oh, so.
**Matt Wimpelberg** 17:33 It's actually, it'.
**Juliano Costa | Datadog** 17:34 open an issue like, hey, Login is not accessible. And I was like, why are you using the Login? Why?
**Pierre Tessier** 17:42 I do!
**Juliano Costa | Datadog** 17:45 But.
**Shenoy Pratik Gurudatt** 17:47 By the way, don't get me wrong, I also use the UI, but I used to increase the load at times if I'm not seeing all the spans. I can change the number of users, I can increase the number of requests per user that is coming in via the Locust UI today.
**Pierre Tessier** 18:00 There.
So this feature flag thing that we're talking about would provide you with that same capability.
You'd be able to control load with a slider.
**Juliano Costa | Datadog** 18:09 Oh man, that's actually awesome.
**Matt Wimpelberg** 18:11 What if we put the, like, a button in the flag DUI?
To trigger that feature flag, so it turns off.
**Pierre Tessier** 18:18 We have a UI for feature flags already.
**Matt Wimpelberg** 18:22 Oh, oh, so we… it would be there, then.
**Pierre Tessier** 18:24 Yeah, yeah, we have a UI.
**Matt Wimpelberg** 18:25 So it's all…
**Pierre Tessier** 18:26 As soon as we add the feature flag, we have a UI to control it. That's why I'm like, oh my god, this is a solution.
**Matt Wimpelberg** 18:32 Yeah, yeah, so.
**Juliano Costa | Datadog** 18:33 Is that… No, go ahead, Matt. Sorry.
**Matt Wimpelberg** 18:36 No, I was gonna say, I'm proposing a big change to the project, but I'm still, like, learning the codebase, so I appreciate, like, those little nuances, they're helpful. Because I'm like, oh wait, we can do this, and you're like, yeah, that'.
**Pierre Tessier** 18:48 Yeah, we're super excited about this, because we could use an existing Ui.
It plugs into all the other stuff we have. People will be able to control this through Helm.
Config, you know, config run.
Oh.
It plugs in very well to our world.
**Matt Wimpelberg** 19:04 Mmhm.
**Juliano Costa | Datadog** 19:05 Okay.
**Matt Wimpelberg** 19:08 And then the, you know, the actual test is in JavaScript. So it's, you know, easy for people to change and stuff.
**Pierre Tessier** 19:14 Excuse me.
**Juliano Costa | Datadog** 19:19 It is a fire hose.
**Pierre Tessier** 19:20 Python, Python, Javascript, I don't know.
**Matt Wimpelberg** 19:25 Everybody knows JavaScript, no.
**Pierre Tessier** 19:27 Yeah, does everybody know Python, though?
**Juliano Costa | Datadog** 19:30 Oh, wow.
**Pierre Tessier** 19:32 I think we should write it in Rust, and just… and just be done.
**Juliano Costa | Datadog** 19:36 Oh, God.
**Matt Wimpelberg** 19:36 Everything else.
**Pierre Tessier** 19:38 Mmh.
**Matt Wimpelberg** 19:38 Everything's going to rust.
**Pierre Tessier** 19:39 It'll consume just 1.4 megabytes of memory, and it'll You know.
**Matt Wimpelberg** 19:47 Oh.
**Juliano Costa | Datadog** 19:48 So I have added another thing here to the agenda. I have a draft for the 3.0 blog post.
Which is actually in a tab in ZoomMeeting notes.
Let me just add Pierre here to the agenda… It's a pretty, long block.
And, I wanted to do a couple of things on that. So, first is to, thank everyone that contributed each of those big chunks of feature. So if you follow, you'll see, like Felix Chenoy, like Donal with the and Florian with the profiling. So like, I try to add that.
One thing that landed now that is not here is… Open. So that would be Cedro. Now we have OpenServer as well to see the collector config.
And I also mentioned Weaver, so thanking Martin Twitz here.
And also the work from Florian on the rename.
And then I also try to link that with the Bloomberg.
thing. So kind of showing that the demo is connected with the whole project. And then, yeah.
And also, of course, presenting everything that we have done and why we broke stuff.
So.
**Pierre Tessier** 21:35 Do you have a draft of this thing you could share with us?
**Juliano Costa | Datadog** 21:38 Yeah, yeah, yeah, it is on the… so… up.
If you go to the… I'm sharing the link here, but it's on our, on the, on the, Jesus, on the ZoomMate emails. It's just a different tab.
**Pierre Tessier** 21:55 I have to open and see meeting notes. Sorry. That's my my fault.
Dun dun dun dun…
**Juliano Costa | Datadog** 22:06 But I think the reading and reviewing, we can do async.
**Pierre Tessier** 22:17 Not that long.
**Juliano Costa | Datadog** 22:17 Yep.
Yeah.
I mean, with the attention span that we have nowadays, maybe it is…
**Pierre Tessier** 22:26 Well, no, everybody's got a TLDR skill now in Claude, Oops.
DLDR, you feed it URL, and it gives you what you need? No? Perfect.
**Juliano Costa | Datadog** 22:35 Okay.
Awesome. I love AI.
Oh, that's the thing that I.
**Pierre Tessier** 22:42 You may have got that.
**Juliano Costa | Datadog** 22:43 Or I don't know if you all saw, but we started getting a couple of PRs where the changes is like, hey, I'm changing two lines of code.
This looks great, but then above the two lines of code, there is 10 lines of comments.
I'm like, please, AI, stop.
So I added a note on our agents.md. Let's see if that helps.
But, hopefully… Hopefully.
**Pierre Tessier** 23:18 Can we tell them to stop using M-Dash?
**Juliano Costa | Datadog** 23:21 Yeah, we can also do that.
**Pierre Tessier** 23:23 No, no, I'm joking. I'm so joking. That's just my number one gripe of AIs. It's the em dash usage.
I promise you, anything that my AIs create will not use MDash.
**Juliano Costa | Datadog** 23:37 The first thing that I do after getting the result is like remove the em dashes when it's not going through my already script because I already have a flow where em dashes are forbidden.
Okay.
**Matt Wimpelberg** 23:56 So for the… I'm working on adding that feature, or… it's gonna be basically adding the metrics, and then… the feature flag. Do you want me to let you know? Because I'm committing to the branch, but I'm… I'll let you know when it's ready for review.
**Juliano Costa | Datadog** 24:12 Yeah, if you can, if you can ping us, yeah,
**Matt Wimpelberg** 24:16 Yeah, I don't want… I just don't want you to start reviewing it if it's… like, I've made commits.
**Pierre Tessier** 24:22 No, just to listen, it just, you know, at Giuliano, IPA, right? Puck, buck, whatever. And they get…
**Matt Wimpelberg** 24:31 Oh, yeah, yeah. Got it. Perfect.
**Pierre Tessier** 24:34 Or in Slack, if you want to do that, that's fine too.
**Matt Wimpelberg** 24:38 Cool. Yeah, no, I'm fairly new to contributing, so this is good stuff. I'm enjoying it Appreciate you guys.
**Pierre Tessier** 24:50 Alright, Juliana, I'm gonna read this blog post.
And, I'll I'll put comments in line on it.
**Juliano Costa | Datadog** 24:59 Thank you.
I will add here, like, amp… However… And the… I'll add the new login.
So we wait on that. I mean, we already waited.
Even above.
A year, but it's another couple of weeks.
**Matt Wimpelberg** 25:31 Yeah, so… so what do you guys think, like, timeline-wise? Like, I am on vacation this week, so I'm not really gonna be doing too much, but… I mean, I'll try to check in here and there, hopefully by the end of the week.
**Juliano Costa | Datadog** 25:45 Yeah, I don't think the the blog post will be released soon. I don't think helm charts will be updated soon. So yeah, let's But not now.
let's try to do it. But I I don't. I don't. I don't see like as a pressure or anything.
**Matt Wimpelberg** 26:05 I think, like, end of next week would be very realistic.
**Juliano Costa | Datadog** 26:08 Okay.
**Matt Wimpelberg** 26:09 Not… like, to have it… to have it done, because I think I can have something to you guys to review by the end of this week, and then… Obviously, next week, you know, we can go through and refine it.
**Juliano Costa | Datadog** 26:21 Sounds like a good idea to me.
**Matt Wimpelberg** 26:26 So, this'll be part of 2.0.
**Juliano Costa | Datadog** 26:29 3.0. 3.0, yes.
**Matt Wimpelberg** 26:31 Oh, 3.0. Nice. That's awesome.
**Juliano Costa | Datadog** 26:34 Yep.
**Pierre Tessier** 26:37 Yeah, it's the, probably the thing with the most advanced version number in all of OpenTelemetry.
**Matt Wimpelberg** 26:43 Nice.
**Juliano Costa | Datadog** 26:46 Oh, but come on, we are enough.
Yeah, we are the project, the the the repo with more forks. Right?
**Pierre Tessier** 26:55 We had the most forks of anything in OpenTelemetry, and number 2 is not even close.
It's not even close. Number 2 is a collector, and it's like… it's like we are magnitudes above. I forgot what it was, but it's… it's not even close.
**Juliano Costa | Datadog** 27:11 I'll open the collector here, because by number of contributions, collector is more.
**Pierre Tessier** 27:17 Yes, we have 6,800 forks.
**Juliano Costa | Datadog** 27:21 And the collector has 3.7 K.
**Pierre Tessier** 27:24 Yeah, so we're twice as many force as a collector.
**Juliano Costa | Datadog** 27:29 Awesome.
**Matt Wimpelberg** 27:29 Number one.
**Pierre Tessier** 27:31 Yeah, yeah, it's like, that's what I said, it So, it's important we have a blog post that says, we broke the demo, because we broke every fucking fork.
**Juliano Costa | Datadog** 27:43 Yes.
**Matt Wimpelberg** 27:44 Oh, yeah, yeah.
**Pierre Tessier** 27:45 Pardon, I do have my French in there, but yeah, this is a big deal. And this is like, it's not even close to backward, like, we broke a lot of things in this one. We broke how you launch it, we changed the config files, we renamed them.
There's a lot of things in this demo that are changed, so the full version bump is important.
**Juliano Costa | Datadog** 28:07 Yep But I I think, like overall, I'm super happy with all the changes. I think we are in a Really nice state.
**Pierre Tessier** 28:20 I can't wait for this K6 thing to land, then we could change the memory requirements, drop it down by a gig.
**Matt Wimpelberg** 28:26 Yep.
**Pierre Tessier** 28:28 Cannot express how happy I am, but no need.
**Matt Wimpelberg** 28:31 Alright.
**Pierre Tessier** 28:32 Takes a memory just to run a demo feels wasteful. Really does.
**Matt Wimpelberg** 28:35 Yeah, especially on a laptop. I mean, some laptop, most people should be running 16 now, but there might be some people with old laptops and they can't even run it.
**Pierre Tessier** 28:43 Yeah, we run into those every once in a while. People are like, I can't run the demo, I don't have.
**Matt Wimpelberg** 28:49 Yeah, I'm on a raspberry.
**Pierre Tessier** 28:51 It's it.
**Matt Wimpelberg** 28:53 Cool, well, I appreciate you guys, your.
**Pierre Tessier** 28:56 Yeah, let us know what else you need. We're here and appreciate you kind of looking at this while you're on vacation.
**Matt Wimpelberg** 29:03 Yeah, I mean, it's… We're just, entertaining the kids at home, so it's nothing too crazy. I have some time.
**Juliano Costa | Datadog** 29:09 Okay.
**Matt Wimpelberg** 29:09 Bye by.
**Juliano Costa | Datadog** 29:09 This is harder than working.
**Matt Wimpelberg** 29:12 It is, it is. You're not kidding, you're not kid.
**Pierre Tessier** 29:15 Every parent will tell you the same thing, yeah.
**Matt Wimpelberg** 29:18 Where are you based out of, Pier.
**Pierre Tessier** 29:20 I'm right, you know, I'm Canada, south of Detroit.
**Matt Wimpelberg** 29:25 Oh, okay. Is that where you have a lion.
**Pierre Tessier** 29:28 Yeah, I'm a big Lions fan.
**Matt Wimpelberg** 29:30 I'm a I'm a big I'm a big.
**Pierre Tessier** 29:33 You know what, man? We are cousins. We are Lake Erie cousins there, man. That's right.
**Matt Wimpelberg** 29:38 Use your stadium when it snows.
**Pierre Tessier** 29:40 Yes. Well, not anymore. Now you have a much better stadium.
**Matt Wimpelberg** 29:44 No, but it's not a zone. It's.
**Pierre Tessier** 29:46 I love it though. And for what it's worth, the Lions are gonna open up the stadium with y'all.
This year.
**Matt Wimpelberg** 29:52 Oh, you.
**Pierre Tessier** 29:53 Your week two game, your week two game at home is against the Lions.
And I considered going… I actually considered going to the game, but, you know… Ticket pricing for NFL games, for teams that are in high demand, like the Lions and the Bills, for whatever reason.
I'm not spending $800 for a nosebleed seat.
**Matt Wimpelberg** 30:13 I spent 400 and I'm going to see Bill's Patriots because I want to see Dra.
**Pierre Tessier** 30:17 Oh, hey, for what it's worth, I'm a season ticket holder for the Lions, so I go to all.
**Matt Wimpelberg** 30:22 Oh, w.
**Pierre Tessier** 30:23 I go to one road game a year as well with my son.
**Matt Wimpelberg** 30:26 I'm actually closer to New York City, so I'm on Long Island, so I'm, like, 8 hour drive.
**Pierre Tessier** 30:31 Yeah, fair.
**Matt Wimpelberg** 30:32 We're, We're getting off topic.
**Pierre Tessier** 30:35 Yeah, yeah, yeah, yeah. No, no. Football's great. I love football.
**Juliano Costa | Datadog** 30:42 Football.
**Pierre Tessier** 30:43 Another kind of football, Giuliana.
**Juliano Costa | Datadog** 30:46 Wow.
**Pierre Tessier** 30:47 Oval handball.
**Juliano Costa | Datadog** 30:48 Be careful.
**Pierre Tessier** 30:49 Okay.
**Juliano Costa | Datadog** 30:49 American handball. Okay, yeah.
**Pierre Tessier** 30:54 Hey, look, there's no more North America team in the World Cup. We've all been eliminated. It's clearly all European, like, one South America team.
We're good.
**Juliano Costa | Datadog** 31:05 Yeah, I'm gonna root for this South American team like.
**Pierre Tessier** 31:09 There you go. Go messy, man. Go messy.
**Juliano Costa | Datadog** 31:11 Okay.
**Pierre Tessier** 31:12 Right? What a game he had yesterday.
**Juliano Costa | Datadog** 31:14 Oh.
**Matt Wimpelberg** 31:14 That was awesome. I'm actually… I'm behind Argentina, that was, like, the.
**Juliano Costa | Datadog** 31:19 Good. I'm Brazilian, I'm not allowed to…
**Matt Wimpelberg** 31:23 Beautiful.
**Juliano Costa | Datadog** 31:24 For Argentina, like, we are, like, life rivals, so, like.
**Shenoy Pratik Gurudatt** 31:29 Okay.
**Juliano Costa | Datadog** 31:29 Okay.
Okay.
**Matt Wimpelberg** 31:31 Oh well.
**Juliano Costa | Datadog** 31:32 But yeah, it is what it is.
Well, I need to jump to another one. Thanks, everyone.
**Matt Wimpelberg** 31:38 seeing you guys. Yeah. Yeah.
**Shenoy Pratik Gurudatt** 31:40 Sure.
**Juliano Costa | Datadog** 31:41 Chris.
