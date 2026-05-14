SIG: Community Demo App SIG
Date: 2026-05-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Juliano Costa | Datadog** 02:36 Hello there.
**Donal O'Sullivan** 02:38 Hey, Juliano, how are ya?
**Juliano Costa | Datadog** 02:41 Good. How are you?
**Donal O'Sullivan** 02:43 Good, good.
**Juliano Costa | Datadog** 02:47 Nice. Yeah, I thought we would skip this one.
It's a long word.
I joined the main authority, and I was like, yeah.
**Donal O'Sullivan** 03:02 Yeah, yeah, no one's here. I'm happy to skip if you'd like. I don't really have anything to talk about. I… yeah, it's just mainly the profile, and I guess it's probably good to go. Just waiting on… I guess we need Pierre to review, and… And, order value's right.
**Juliano Costa | Datadog** 03:19 Yeah, I think we need someone… extra to… to review, like, I'm too biased now to review it.
**Donal O'Sullivan** 03:29 Yeah, that's fair. Cool.
**Juliano Costa | Datadog** 03:32 There, there, there is one… open PR from the PandaBot that is crashing on the build, because… One of the dependencies on Rust. So, Rust has two repos.
as many of our, SDKs in OTAL, the country, and, and Core. Core had a dependency bump to 0.32.
But some dependencies that we use from Contrip are still relying on 0.31.
So when we try to build the service, it crashes because it has two versions of the SDK.
I raised to the folks on Rust, and I think they will release soon, so yeah, that's it.
But that's the… I think the only thing that I had on my… on my list… As Chanoy just, joined, I wanna say that I haven't looked at his PR, so… There is this.
**Shenoy Pratik Gurudatt** 04:44 No, I just wanted to make sure that we are aligned, that Weaver does the attributes check, and then the telemetry test is only doing the sanity test.
**Juliano Costa | Datadog** 04:55 Yeah, telemetry should do… Telemetry should take care of, experience connected?
And, I think metrics and logs emitted.
I don't think we need to actually validate, anything on the… On the metrics and logs.
Just that they are… Coming out of the service.
**Shenoy Pratik Gurudatt** 05:24 I… I think my PR doesn't do the spans connected check yet, it just.
an existence for services. Same for logs and metrics.
Okay. Let me check what to do first fans connected part. It's just… different Jaeger queries that I need to make. I think that should be feasible.
**Juliano Costa | Datadog** 05:44 Yeah, I feel that this is important. This was way more important when we started the project, 3 years ago or so, because… I think when we started Traces, where GA, like, really… like, it was close to GA traces. Metrics were not… Implemented at all, and logs were not even on the map.
So, what we had a couple of times was, bumping dependencies on, On… well, dependencies bump, and context propagation breaking.
So then we… we started thinking about, and then trace tests came into play. So that… that was, I would say, vital to the project.
at the beginning. Nowadays, we do not see broken context propagation as much.
like, I don't think we had any in the last 2 years or so, so… If you take a look at, we have one PR from Peter on Tuesday, 3194.
What he did was that he kind of added to… to services.
Oh, no, he didn't.
Wait.
Where did I see that?
I thought that he did.
Let me just check if it is on the history here.
I think what he… It… Beginning was… adding some… Health checks.
So what… This is also cool, because we can… test the services in an isolated scenario. Like, it builds, It generates spends.
metrics and logs, but, like, the spend that we'll generate would be, like, hello, or, like, ping, whatever, like, help.
And, like, yeah, this is working, we are good to go.
I like that approach as well, so the problem of this approach is that we cannot have all of that in one PR, so we would need to add health checks into all services, and then kind of open the PR to validate that.
Bishop.
I think this would be cool.
Because, let's say that we change the ad service.
Or I don't know, checkout service.
As of today, check out… It's kind of in the middle of the demo, so everything goes through it.
We cannot just test checkout. We need to spin up the whole demo, and then test all the spins.
But if we are changing just checkout, and we have a health check that emits the spend… spends.
Then we could just run this container, send a request, get this pin, Done, done, and move on.
**Shenoy Pratik Gurudatt** 09:24 Word.
**Juliano Costa | Datadog** 09:25 What do you… what do you both think? I don't know, like, open to discussions here.
**Shenoy Pratik Gurudatt** 09:35 What is the intention of the health check? Is it to just check if service is alive?
**Juliano Costa | Datadog** 09:41 Yeah, but in our case, we would use the how check to emit.
telemetry, and then validate if the spins are being exported. So it would be a trace with one spin, but, Unless it's a node, because one, get, get, like, a bunch of spans in one single trace, but anyways, the point of the health check in here would be to validate that. And then, when we think about deploying on Kubernetes, we could implement the… the help checks on the pods, so then the Kubernetes live check and help check checks these endpoints, and we could even implement some feature… I think we have one service that does that. Let me… one second.
I think we have one… one scenario that crashes.
on Kubernetes, with the… It's a health check stuff. Failed readiness probe implemented on cart.
It forces the redness probe to fail with unhealthy.
And, the pod… the pod status changes to not ready.
And then Kubernetes will… would redeploy the container.
Oh, redeploy the plot.
**Shenoy Pratik Gurudatt** 11:21 You see, that's the regular readiness check, right?
**Juliano Costa | Datadog** 11:25 Thank you, go to the mic.
**Shenoy Pratik Gurudatt** 11:26 Current implementation, I'm using the load gen.
So once the demo starts, the load generator starts sending requests, and then that is used to check if all services are alive.
Rather than checking individual containers, so we check the connection. Like, that makes easier for me to check the connections, because load generator is trying everything. But with health check, it's just one service that will generate a span.
**Juliano Costa | Datadog** 11:52 Again, this was just an idea that came a while we were talking. I think going through the whole demo is… more reliable, and we can confidently merge the PR, because we know that everything is running, everything is connected. Done, done. Auto-merge.
Like, we can even, make the dependable bot auto-merge itself, With the help check approach, we would be confident that the service is running and a meeting is passed, but we wouldn't be 100% sure that the context propagation is properly working. So, there is this.
I think if we stick to the initial plan, it's better.
Because… because with that, we can enable the auto-merge, and then the GitHub itself, like, the action itself would validate Everything is connected, done, done.
Go for it.
**Shenoy Pratik Gurudatt** 12:57 Yeah.
I did, add the same script into Make and into CI, so that's not much of a difference. The CI tests are already there.
You bet.
I'm just thinking, is there any other place where health check can be better?
To be used.
**Juliano Costa | Datadog** 13:20 Mmm… I think for the Flight DUI, for the profiling new UI that, will, come in.
Those, they do not have load.
**Shenoy Pratik Gurudatt** 13:34 Yes, yes, yes, yes. Flag Day is one that is not there in the… In the checks that I am doing, because there's nothing coming in there, yeah.
**Juliano Costa | Datadog** 13:43 Yep.
**Shenoy Pratik Gurudatt** 13:44 That's a good point. So, probably for them, we should use health check.
Or you can keep help check for everything, and then… the side of… We want to do both.
Yeah.
**Juliano Costa | Datadog** 14:00 Honestly, I don't think we should, do both now that we are discussing, because if you're gonna run the whole demo, what's the point of having, like, a… I mean, we could… have… Things like… If it builds an… because we have one… We have one test that just builds the service.
So we validate if the service builds. This was, again, also another problem that we had a lot at the beginning. Sometimes, dependable PRs came in, we merged, but the service not even built.
**Shenoy Pratik Gurudatt** 14:41 Hmm.
**Juliano Costa | Datadog** 14:41 and this is good and useful, like, I was, just, sharing with Donald here, the… the Rust, the Pentabot PR that we got today, it's bumping SDK version to 0.032.
But we have a contrib, dependency as well, that is for the, resource detectors.
And for the contrib trip, there was no bump, so that still relies on SDK 031. So when we try to build the service, it crashes, so… good. We are… We are safe to say that we won't merge this, because it's crushing the service.
**Shenoy Pratik Gurudatt** 15:27 Yep.
**Juliano Costa | Datadog** 15:29 So then we could, thinking about, on the same With this same approach, we could have the hot check as, pre… pre-step. Okay, the how chat's working, great. So now let's run the whole demo to… Because that consumes more resources and stuff.
I…
**Donal O'Sullivan** 15:56 Yeah. You also want to fail faster, as well, to give feedback sooner. Do you know, like, if you're taking 15 minutes for a PR to build and tell the author, this is broken, whereas if you can do it in a few minutes… Can help that feedback loop, you know?
**Juliano Costa | Datadog** 16:13 Perfect, yep.
And I…
**Shenoy Pratik Gurudatt** 16:15 Currently, when I was writing the CI test, I saw the images that we were building in the build test.
They cannot be used in another worker.
So I had to, write a step to rebuild all the images, again, for the telemetry SCI worker, because it's just cache that can be shared, I guess, but not the exact images.
And the other part is, if we do health checks, will it be just running one container, or will it be running the demo again fully, and then checking the health checks?
**Juliano Costa | Datadog** 16:48 No, for the… for the health check, that… I think that's the main point. I would run just the service.
**Shenoy Pratik Gurudatt** 16:55 I see, that makes sense.
**Juliano Costa | Datadog** 16:56 Yeah, we need to make sure that the service Actually, runs individually, because there are some services that do not do that.
And if… because… oh god, that's a whole new world. If we run with the Docker Compose, let's say Docker Compose start add.
it will get all the dependencies from add and start together. We would need to run, like, docker run add, or something like that, and then… Expose 8080, or whatever port ad has, and then just send a ping on the health standpoint.
So, it's simple, but it has a couple of steps till we get there.
Yeah.
I… as we are using MergeQ, is there… is there a way of, Let's say, adding everything to the merge queue, and then… all those PRs are merged into one PR, And then the… the… the action runs.
like, the full test runs on this single PR, and if it's successful, then merge to main. That would be great, because If we have 15 PRs bumping dependencies, as we have every, every day.
This would be 15 times running the full demo, but… If we build the 15 services, Once.
Run once the full demo, okay, validated, then we merge all together.
Any… this is just me thinking, I…
**Shenoy Pratik Gurudatt** 18:52 You want that feature, I don't know if that exists.
**Donal O'Sullivan** 18:55 Yeah.
It sounds like you want to squash them all into one commit.
And then merge that as a… as a PR.
are… yeah, I don't know how you do that from multiple PRs, and you… I don't think, yeah.
I'm not sure.
**Juliano Costa | Datadog** 19:15 I… I… well, Peter is… he has a lot of experience with, CI and stuff.
I will ping him and, and… ask if that's possible, and if not, I'll raise a feature request on GitHub.
And they can't vibecode that in two days and deliver.
**Shenoy Pratik Gurudatt** 19:38 Christmas.
**Juliano Costa | Datadog** 19:44 Isn't that how things work nowadays?
**Shenoy Pratik Gurudatt** 19:49 There are a lot of builders, but there are very less reviewers.
everywhere.
**Juliano Costa | Datadog** 19:55 Yeah, but you can use GitHub Copilot to reveal the PR.
Fair enough.
**Donal O'Sullivan** 20:01 Just… just look at all the outages that have been happening lately.
**Juliano Costa | Datadog** 20:08 Okay.
Cool.
Yeah, so maybe, you know, let's start with what you already have, and then we build on top of that.
**Shenoy Pratik Gurudatt** 20:22 Yeah. Do you want me to just add the span connection check first, before we merge that in?
**Juliano Costa | Datadog** 20:28 If you say that you are working on that, I would love to wait, and then we get that.
**Shenoy Pratik Gurudatt** 20:36 Yeah.
I think we can… Cut anywhere.
**Juliano Costa | Datadog** 20:40 If you say no, let's start with this, and then I'll send a follow-up PR, also fine.
I haven't checked, and we have a public holiday tomorrow, so here in Austria, and off Friday, so I'll be back just on Monday, just so you know.
**Shenoy Pratik Gurudatt** 21:00 then I can probably add them.
**Juliano Costa | Datadog** 21:03 But we have other reviewers and other.
**Shenoy Pratik Gurudatt** 21:06 Yeah, yeah, unless, Donald, you can also take a look.
**Donal O'Sullivan** 21:10 Sure, yeah, yeah, no problem, Shanoy. I, I will… I won't get to it today, but I'll get to it tomorrow for sure.
**Shenoy Pratik Gurudatt** 21:16 Okay.
then I think if you're good for tomorrow, we can merge that in, and I'll have a follow-up.
**Juliano Costa | Datadog** 21:24 But Donald, do you know if we could configure Dependabot to… merge all PRs automatically to this.
**Donal O'Sullivan** 21:35 So…
**Juliano Costa | Datadog** 21:36 French?
**Donal O'Sullivan** 21:37 Yeah, so I… I don't know, but I would think so. I think you just have to specify a different branch, so, like, you create a feature branch, and then all dependable PRs would open on… that feature branch. Well, they'd all open to merge into that feature branch, and once that happens, you could open another PR on that feature branch to merge to main, and then that could be your bulk… Dependency update, if that makes sense.
Like, you can do that in CI, it's just that it's a bit, like… You have to write all the scripts for it, like, you know, but I have done some stuff like that. It can be a bit hacky, but you can definitely do it.
**Juliano Costa | Datadog** 22:20 Bye.
I like that, yeah.
That would be cool.
**Donal O'Sullivan** 22:26 Like, the Dependabot we use is just, like, a setting, right? It's just like a… there's a dependabot file, so… I think you should be able to specify. Anyway, look, I'm kind of hijacking the conversation again, but, just an idea.
**Juliano Costa | Datadog** 22:38 No, I think we are here to discuss.
**Shenoy Pratik Gurudatt** 22:42 Yeah, totally relevant. Reduce ops, or the less number of reviewers.
**Juliano Costa | Datadog** 22:48 Well, reduce ops. That's a nice, talk title.
**Donal O'Sullivan** 22:55 Reduce, obviously, yeah.
Could… could create an issue for… I can have a look at the… at the Dependabot.
config and just, like, see if, like, I mean, I might… yeah. And then if… maybe open an issue for it or something, or…
**Juliano Costa | Datadog** 23:13 Yep.
I think we would need to play a little bit with hashes or regex to say, hey, independent bot, create this PR here.
or create the PRs, and then when all PRs, workflows succeed, Auto-merge into this new PR.
Or into this new branch.
And then once all the PRs for the day are merged into this branch, run the… the full test.
And if the full test succeeds, then, merge to me.
**Donal O'Sullivan** 23:54 Yeah.
**Juliano Costa | Datadog** 23:55 Yeah, no, this is… this is fun.
**Donal O'Sullivan** 23:59 The only thing is where it could get painful is, like, it might… they might all work individually, and when you merge into one, something breaks, then you have to, like, trawl through… Where did it actually break, you know, versus… when you do test it 15 times, you're testing it just for that change, I suppose, so there is a bit of a… Yeah.
**Juliano Costa | Datadog** 24:20 Yeah, that's true, but hopefully Shanoi scripts will say, hey, this broke.
**Donal O'Sullivan** 24:27 Yeah, yeah, yeah, yeah, yeah.
**Juliano Costa | Datadog** 24:29 And not, like…
**Shenoy Pratik Gurudatt** 24:32 It is a month.
**Juliano Costa | Datadog** 24:33 I'm working.
**Donal O'Sullivan** 24:34 Hmm, hmm.
**Juliano Costa | Datadog** 24:35 Yeah.
And then we can investigate why that service broke. Because, yeah.
If we think about, like… If we merge individually into main, and everything is working, then we would still have the same problem.
**Donal O'Sullivan** 24:54 Yeah, yeah, yeah.
**Juliano Costa | Datadog** 24:56 The only thing is that we wouldn't know which one was the one that… yeah, okay, yeah.
Ugh.
I don't… I don't know.
Life should be simpler.
**Donal O'Sullivan** 25:14 Yeah.
I have… I have seen the auto-merge.
configured, like, in my previous… employer, I know, like, one of the teams, they had, like, they… they had dependable setup that were, like, it would open a PR, and then it would… if everything passed, it would… all the CI checks would pass, it would just auto-merge. So, like, there was no… No human reviewers needed. I think maybe… I think for the most part, it works fine.
I guess it depends what you're… If it's just, like, Go versions, it's probably fine, but if it's something a bit more… Tricky, maybe, but, yeah.
**Juliano Costa | Datadog** 25:54 Yo.
**Shenoy Pratik Gurudatt** 25:59 I would be happy if we get there with our CI tests.
**Donal O'Sullivan** 26:03 Hmm.
**Shenoy Pratik Gurudatt** 26:04 Because anyways, if there is something that is not caught in CI, it might be difficult even for us to actually, during the sanity test, validate a specific case that can go wrong.
We usually get to know if someone faces an issue, or we are self-test it out later, once the PRs are merged in.
**Donal O'Sullivan** 26:20 Hmm. Hmm.
That makes sense.
Yeah.
I think you can. Anyway, yeah.
Okay.
**Juliano Costa | Datadog** 26:38 Okay, yeah, that was… I didn't add anything to the meeting notes. Great, good job.
I will do that.
**Donal O'Sullivan** 27:14 Seems the Pinderbot does have a setting target branch.
You can specify what branch to open the PR, and… Anyway…
**Juliano Costa | Datadog** 27:24 Yeah, my main concern there is that We would need to… make sure the Pentabot creates the PR, and this… or this branch, and then this branch needs to be unique.
and, like, every day it would be a different branch name, so I know that we can say, hey.
If the break.
**Donal O'Sullivan** 27:51 Mr. Space.
**Juliano Costa | Datadog** 27:51 with whatever, but, like, how the other How the other… or?
Yeah, we could add the date on the branch, because then it's easy to pass to the other ones, like, just get the date, and that's the name. Okay, yeah, it's doable, yeah, yeah, okay.
I'll just add here, like, mainly discussions on… on, Boop.
As we are here, tonight.
Donna opened up PR to add profiling to the demo?
I've reviewed it and, changed a couple things in there, so… It looks good to me, but, I've done the changes together with him, so it would be nice to have someone else taking a look. Would you be able to… to take a look? You will need to… you will need to reboot your front-end proxy.
Just so you know, because that, was an issue for me and Donal.
**Shenoy Pratik Gurudatt** 29:50 Okay.
**Juliano Costa | Datadog** 29:51 We are introduced.
**Shenoy Pratik Gurudatt** 29:53 We've seen the…
**Juliano Costa | Datadog** 29:53 FirePit, we are introducing FirePit and, and changing the way that we… We've… And introducing a new endpoint to the… to the front-end proxy, so… then you can access through the proxy, fire pit, yeah.
**Shenoy Pratik Gurudatt** 30:15 No.
Okay, I think I have some bandwidth tomorrow. I can get it done tomorrow.
Awesome. Also, when I'm thinking through my PR, I think it's better if we get this in, in case there are review comments, and then I do one more iteration. This is fine for now. I'll create a follow-up issue, and link it to the PR for the connection of the scans.
**Juliano Costa | Datadog** 30:38 Cool.
Then, see you all… Well, I won't be here next week, so see you all in two weeks.
**Donal O'Sullivan** 30:47 Cool.
See you guys.
**Juliano Costa | Datadog** 30:50 Cheers.
**Shenoy Pratik Gurudatt** 30:51 Bye.
**Donal O'Sullivan** 30:53 Take care.
