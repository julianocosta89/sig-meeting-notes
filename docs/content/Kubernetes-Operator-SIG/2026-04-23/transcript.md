SIG: Kubernetes Operator SIG
Date: 2026-04-23
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/MrYFnosFQRy52y615fQPISULA8Zmf7lYSJz9obMwLUAuMmMNrPLXlv4mB3AcYA4w.ZGYjC_9ET9cCAskW
============================================================

## Zoom Recording Transcript

**Benedikt Bongartz** 01:18 Hello?
Yuri!
**yurioliveirasa** 01:23 Hey, man.
**Benedikt Bongartz** 01:25 How are you doing?
**yurioliveirasa** 01:26 I can't hear you.
**Benedikt Bongartz** 01:28 Test 1, 2, 3, 4, 5?
**yurioliveirasa** 01:33 Probably on me? Yes. Promet can hear you now.
**Benedikt Bongartz** 01:44 1, 2, 3, 4, 5? Yeah. Huh.
**yurioliveirasa** 01:48 Bye, guys.
**Ozzy** 02:03 My camera's not working, is it?
I just see a black square, even though it's turned on.
**yurioliveirasa** 02:08 Yeah.
**Ozzy** 02:09 There you go.
**Benedikt Bongartz** 02:11 Maybe you picked the wrong camera?
**yurioliveirasa** 02:13 Yep.
**atoulme** 02:15 Or you have your hand in front of your camera.
Stop doing that, okay? We can see…
**Benedikt Bongartz** 02:22 Just turn the light on.
**yurioliveirasa** 02:25 It's done.
**Ozzy** 02:27 It's dark in here, yes.
**Mikołaj Świątek** 02:29 Go outside into the sun, this is…
**Ozzy** 02:32 necessary.
**Mikołaj Świątek** 02:32 That's great.
**yurioliveirasa** 02:34 Oh, now it looks better, yeah.
**Ozzy** 02:36 Oh, except Google Meet has my background blurred, so now I've got… but I didn't set it turned on in Zoom, so now I've got… Weird things behind me, but…
**atoulme** 02:45 It's fine.
**yurioliveirasa** 02:47 Okay.
**Mikołaj Świątek** 02:51 Hmm, let's see… We don't actually have any, anything in the agenda.
Or do we have something in the agenda that is… that has not been put?
Into the, into the list.
**yurioliveirasa** 03:16 I was, I was doing some, tries today, let me… let me see if I find… So, I'm discussing issues here. This one… one sec.
**Mikołaj Świątek** 03:27 There are… there are… there are six Discuss at Sig issues, which… of which I don't think all of them need to be in Discuss at Sig, and I'm actually removing one right now, because we already discussed it. The one about, And the imports in the API package.
Because that's, like, ongoing.
Anyway… There is one thing I want to discuss at the business issues, is the notion of automatically assigning reviewers to pull requests slash issues.
**yurioliveirasa** 04:05 One of these, I've put this label today to discuss this.
What do you think, guys?
**Mikołaj Świątek** 04:12 I'm… I'm in favor.
I'm cool.
**yurioliveirasa** 04:17 Yeah, for me as well, because, yeah, yeah, if anyone don't mind it, at least I don't mind, but you are more active than I… And the reviewers, but I would vote for this as well.
**Mikołaj Świątek** 04:33 Mmm… For pull requests, I think we're largely, largely not too bad about reviewing them promptly. I don't think we have anything that's, like, waiting for a very long time for any kind of attention. But I also wouldn't mind, like.
assigning two people at random, plus the approver's group, in case anybody actually wants their own volition to participate. Like, that would be my… Proposal… Proposal Zero. Yeah, I would like to do something about issues as well, but for issues, this is unfortunately a bit more… a bit more complicated.
Or at least, or at least, I think it would be nice to have some… Process by which we don't have any issues, that we take care of the issues that actually need triage.
So at least the stuff that comes… the new stuff that comes in is triaged, even if it's not… Otherwise actioned, because it often doesn't really need to be.
or at least I find it, wherever I review new issues, that I often just say, this seems fine, if somebody wants to contribute it, go ahead. And that's basically it.
**yurioliveirasa** 05:58 Yeah, Anton, Pavel.
Aussie, man.
**Mikołaj Świątek** 06:02 Antoine, I bet Antoine has opinions about this, has experiences from the collector.
**yurioliveirasa** 06:08 Yeah.
**Mikołaj Świątek** 06:09 repositories.
**atoulme** 06:11 You were talking about, like, rate of review of PRs?
**Mikołaj Świątek** 06:15 I mean, rate of review of PRs is probably… I don't think PRs are that big of a problem. I think we're worse about issues. I think we sometimes have, like, issues, language with any response. That's, like, I think a bigger problem that we have than reviewing PRs.
**atoulme** 06:31 Yeah, okay, that's fair. Well, I think for… for the collector, we… we were lucky enough that we built a team of triageers, and they have the explicit goal of managing through all the incoming issues.
It's not perfect. We also do a report weekly, where we, compile how many issues are in triage, and that gives us an idea of the trend, because if we start to see that there are too many, it needs to triage, that's a great submitting discussion, and we quickly, redirect the energy of the group towards making sure we get that down to a good level.
I'm noticing that a lot of people jump on issues before they are actually marked as triaged.
And that might be something to kind of push back on a bit more, especially because with AI, people just take an issue and say, look at the issue and make me the patch for this, and then they open a PR. So, we're now seeing a problem where the compounding thing of, like, letting those issues rot is that they also create additional craft for us.
to review at the PR stage, and then it's much harder to push back. So I just want to bring that up. It's a very recent learning for me. I…
**Mikołaj Świątek** 07:42 That's good.
**atoulme** 07:42 spent last night reviewing a bunch of PRs, and I was like, okay, why… hang on, let me read the issue. Well, the issue has not been reviewed. Actually, the issue doesn't make any sense. I actually don't want to do this. And that was very painful, because I was like, there's so much work that went into this that just… No one actually wants this.
Even the originator of the issue was like, that's not what I asked for.
So, we, we should probably do a better job of, at the collector level, in triaging those shoes. And, Yeah, yeah, also making Making a difference between what is a support issue versus what is an actual feature request or a bug.
So, quick triage helps a ton, and We should also be good about closing issues.
I don't think the operator has any edging out of issues.
**Mikołaj Świątek** 08:36 No, it doesn't. And I'm kind of… I kind of don't want to, like… I have… I have, like, this thing sort of coming… that keeps coming back in my head, where I was like, let's configure a style bot.
Right? And then I go, but… then I have to go through all the existing issues, and, like, mark the ones that shouldn't be stale, as you know, never stale, or whatever the label is by default.
So… and that's usually… it usually stops me. I think it might be that… At the very least, I think there's some level of just automation using the GitHub API, or just, like, just, like, a one-shot thing you can do, where you go just… go through the issues. If the last…
**atoulme** 09:22 Excellent.
**Mikołaj Świątek** 09:22 Once is one of the approvers or maintainers asking for more information.
Then add a label about that, and then everything with that label that is older than half a year just gets… Then everything that's… yeah, everything that's left afterwards.
gets the do not stale label, let's say, and then we enable the stale bot. That's, like, a process that might work.
**atoulme** 09:51 I mean… In the past, I've just done it manually, right? And it's actually very good as a sweep, because you find duplicates this way too, or you can refine a bit the issue, or… You can nudge people a bit. So, that's also something we could just… We could, take all the approvals maintainers of the operator, we divide by the number of total issues currently, and then we give everybody some issues to review.
Or something like that.
**Mikołaj Świątek** 10:18 That's an output.
**atoulme** 10:19 Good use of your time.
Okay.
It's very… it's a lot of work if one guy tries to do 300 issues. It's, like, a multi-days amount of work, but if it's 30 issues, you can do this, like, in 2 hours, and be done.
**Mikołaj Świątek** 10:35 That is also true, yeah.
Okay, so, but automatic… automatically assigning reviewers to PRs, is anyone against?
Two reviewers out of the… out of the approvers group would be my, my proposal.
Alright, let's do that then.
I'm gonna…
**yurioliveirasa** 11:09 Let's implement… yeah, let's implement to add 2 reviewers automatically to PRs, right?
**Mikołaj Świątek** 11:14 Yeah. For this to work, I think you have to go to OpenTelemetry Infra, or whatever the repository is, and make the change there in Terraform, but to begin with.
Yuri, since you marked this as discussed, let's say, can you comment under that, the issue that was… that we have opened about this, and say that, yes, yes, we're doing it?
**yurioliveirasa** 11:35 Yeah, okay, I will… I'll do it.
**Mikołaj Świątek** 11:38 Thank you.
**yurioliveirasa** 11:42 I'm sure… Okay.
So, next one.
Do you have another one? .
**Mikołaj Świątek** 11:56 I don't, I'm looking at the same list as you right now.
There is one about go-out instrumentation and Kubernetes jobs and cron jobs, and so on, but honestly, I can't triage that, because I don't really understand how that instrumentation works, and I'm not sure… but it also seems like something that we should triage first before kicking it… kicking that can.
to the, to the goal auto-instrumentation maintainers, right?
So I'm not sure. Maybe, maybe I'll get to it at some point, but could also… Could also ask it as help.
**yurioliveirasa** 12:43 True, do you mean, to the auto instrument, go containers, right?
**Mikołaj Świątek** 12:48 Kind of. I mean, I'm not sure if this is even intended or not, right? Because what happens is… The application… Terminates.
But… the goal, auto-instrumentation doesn't terminate, should it? Like, I feel like it just should, right?
I don't know why it doesn't.
Like, we're… like, we're terminating the pod.
Is it… I haven't even tried to reproduce this.
**yurioliveirasa** 13:19 Yeah, my point of view, when a job, generates a pod, and, you add a sidecar on that pod, if the job, executed their, let's say, its tasks.
This sidecar should be also terminated.
**Mikołaj Świątek** 13:36 That's my understanding of how this works, which is why this is a little bit confusing to me.
Maybe the solution to this is to just try, whether it actually works, the way the issue describes it.
And then we'll see. But also, like, I think Israel's point of… Just deprecate this instrumentation.
It's also valid enough.
**yurioliveirasa** 14:08 Yeah.
Yeah, let me, let me right now to ping the guys about this issue, and then we can decide, either if it's a expected, Kubernetes behavior, I mean, because in our understanding, this sidecar container should be also terminated on the pod.
is terminated.
And… if so, then it's nothing about the Go instrumentation per se, right?
**Mikołaj Świątek** 14:38 Yeah.
I would say so, like, Kubernetes should kill it, right? It shouldn't… it shouldn't get to run forever, because… just because it wants to.
**yurioliveirasa** 14:47 Yeah, I… for that reason, I decided to bring this to seek, because in my point of view, there is nothing about the Go instrumentation in that case specifically, you know? Of course, we can deprecate the Go instrumentation for any reason that you can discuss further.
But… Not in that case. I don't know if anybody has some comments, or a different understanding of Nikolai and I.
No. Okay.
So…
**Mikołaj Świątek** 15:28 All right, the… actually, the least weighted configuration PR, I'm removing it because I just forgot to remove it the previous time we talked about this, but I also have to get back to it.
And… what else do we have?
**yurioliveirasa** 15:48 the support for, CADA outscaling.
**Mikołaj Świątek** 15:55 I don't think I've ever read this issue. What else is about?
I think this might be a bug that we fixed? I recall fixing something about this.
**yurioliveirasa** 16:10 Yeah, it's on the 4401, and I have also, pointed to, to that issue.
On my comment, back last year. But the guy reported that… We have also a different… A different outscaler… for CADA, you know, so basically, if we implement, let's say, the horizontal podot scaler in the CR of the collector.
So, this horizontal pod scaler will work… In a, let's say… in concurrency of, this original KID outscaler, you know? Because KID, it's another operator per C. So, how should we configure this? Should we disable the collector CR? Sorry, the collector HPA?
And are we only cada? How… how should we work on this, you know? Because it depends on the meme replicas in the end of the day.
**Benedikt Bongartz** 17:16 I think there is with… so, I'm not super familiar with KIDA, but I've read that since Kubernetes 136, which I think was released This week? Or… this week?
There is an option for HPA to connect it to KIDA as a metric source, and then support also scale to zero, and so on and so forth. It's alpha, so it needs to be enabled.
But… as far as I understood, this potentially would then resolve this issue at some point.
Because, yeah.
**Mikołaj Świątek** 17:53 Yeah, in 5 years after this is, like, stable, and everybody moved to that… to those versions of Kubernetes.
I don't know, like… Assuming… because the CADA is really just a controller.
Right?
Yeah. It interacts with, with whatever, with the deployment by, by setting the replicas, field, right? Essentially.
So… So is the problem… is the problem that we have a… is that… is the problem that we have this field on our own CR, on the collector CR, and they can't point CADA at that… at RCR? They can only point it at a deployment, or… or stage full set? Is that actually what the problem is?
**yurioliveirasa** 18:55 is, as far as I understood, the problem is, because the reconciliation of the replicas field, you know, because, when we set, like, the open telemetry on desire to have replicas to 1, And then, we point, a SCADA configuration to, I don't know, configuring HPA and to 5 replicas. On SCADA, it starts, scaling this, pod, whatever, this deployment out.
Then the… the OpenTelemetry collectors, Controller will get back to one or two desired replicas.
You know?
**Mikołaj Świątek** 19:42 But I'm reading… because I'm reading the CADA documentation right now, and it says… that… Yee… you can scale… Custom resources with it.
It has to define the scales of resource, so let me, let me, let me give you what I'm reading.
it says here that you should… this should work. Like, you should just be able to use KDA to scale the OpenTelemetry Collector resource. OpenTelemetry Collector resource has the scale sub-resource.
That's how it interacts with the HPA. So, it should just work.
I haven't tested, but… but, like, looking at this documentation, yes.
Should work.
**yurioliveirasa** 20:41 No, we can, I can have a look.
I can have a look, because the two represent a concurrence between, the… what Cato wants to do versus, the reconciliation process of this, collect-a-CR, you know?
**Mikołaj Świątek** 21:01 Yeah, but there's no problem, like, the reconciliation process reconciles the state of the CR with the state of, you know, the deployment slash stateful set, right?
But in this case, you point KDA at the actual CR, and KDAS changes the field on the CR. So then the CR reconciles it where it should. So it should work exactly as you would expect.
**yurioliveirasa** 21:30 Okay, I see it, yeah. So, it should work, yeah.
**Mikołaj Świątek** 21:35 According to this documentation, yes, maybe it doesn't, because we have a bug in there somewhere related to this, but, like, the HPA does work, for example.
So, like, all of this should work the way you would expect.
So, like, it's probably worth… Trying it?
**yurioliveirasa** 22:04 Okay, let me… Okay.
**Mikołaj Świątek** 22:07 It should work the way that you set autoscaler to nil, or the default, like, there's no autoscaler, and then you just point CADA at the OpenTelemetry corrector.
But that's… that's the intended way.
I think… Do we have, do we have anything else?
**yurioliveirasa** 22:47 Nope.
Not from my side.
**Mikołaj Świątek** 22:53 Okay, then. Cool. Thanks, thanks for coming.
The room?
Enjoy the rest of your day.
**yurioliveirasa** 23:00 Thank you, guys. See you.
**Pavol Loffay** 23:02 Goodbye.
