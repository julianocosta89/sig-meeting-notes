SIG: .NET Auto-Instr SIG
Date: 2025-11-19
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 01:07 Hello.
**Piotr Kiełkowicz** 01:19 Hi guys.
**Mateusz Łach** 01:23 Bo.
**Piotr Kiełkowicz** 01:34 I'm not sure if Zach or Chris would like to join.
Raj, do you know anything about… About them? Oh, Chris.
**Rajkumar Rangaraj** 01:43 Nope.
Yeah, I did not see any pinging from them.
Well, Chris is here already.
**Piotr Kiełkowicz** 01:50 Great.
So, I'm trying to show… The screen. Hopefully, you'll see the… our agenda.
And… the first thing I've put on the list is kind of… Cut off new release shortly.
With support for .NET 10 and experimental file-based configuration, and then no-code instrumentation.
I think we first should to verify what stays in current,
milestones, and what I've moved to one 14 version.
So, for sure, we have two leftovers, needs to be implemented… merged, probably. First one is SPNET Core 10 support.
PR is already open up. It would be great if you can Look into it, and…
Verify if you are fine with this.
And Mataush, you have reported kind of memorabic for the group? Yes, yes, yes, I… Continuous profiling.
**Mateusz Łach** 03:10 Yeah, as I was looking into some flaky tests, I realized that there is a problem, basically, possibly memory leak. This is, specific to profiling and, tracking spread-to-span-context correlation.
I have fixed locally, testing it, probably create a PR later, this week, probably tomorrow.
So… Yeah.
**Piotr Kiełkowicz** 03:34 So… so I think there are two… two blockers for… for the upcoming queries, and…
I will show what is in 1.14.
MongoDB, 3.5, he kind of… he's a…
bigger stuff, because the internal implementation was fully reworked by MongoDP team.
And… For now, it is only documented, but it is not supported.
in this version.
issue reported by Sean related that we are wrongly
Handling, metrics, protocol, and couple other things.
draft PR is in place, but…
I do not think it is blocker, it was… We passed forever, so… If there will be no…
Ready before the release, so we can postpone, in my opinion.
**Rajkumar Rangaraj** 04:41 You know, just a question there. By default, we export using HTTP protopref, right? That's the documentation case, right?
**Piotr Kiełkowicz** 04:53 Yes.
**Rajkumar Rangaraj** 04:54 But looking at it, it is doing a GRPC, our implementation. Do we… do we even know that?
Can you repeat the OTLP exporter is doing a by-default GRPC in… from this auto-instrumentation repo. Yeah, so…
**Chris Ventura** 05:13 Raj, what happens is we only set the default to be HTTP protobuf in certain situations, and otherwise we defer to the SDK to deal with all of the environment variables and set things.
But because of the, method that we're using to,
**Rajkumar Rangaraj** 05:39 bootstrap the SDK.
**Chris Ventura** 05:42 In conjunction with the environment variables that that method checks, it results in the Our default not being applied.
So…
**Rajkumar Rangaraj** 05:59 Yeah, that is correct. At this point, I feel, because Sean spent a lot of time on this, the document was slightly misleading in the config, which calls out that by default, it goes over HTTP protobuf.
And there is no way, like, by using this NROM… there is a one without a matrix. Here, if we say exporter VTLP underscore protocol, that works.
But, this does not work, and this is a kind of long, as Peter called, long pending bug in this repo, and I think no one has reported to us it.
I also clearly want to say that instead of doing something here, it's best to get it fixed in the SDK and rely upon that, instead of maintaining in two different places.
**Piotr Kiełkowicz** 06:50 In the SDK, it is not so simple, because the way…
We are utilizing… the way we're registering is, not… Even trying to…
recognize this specific environmental variable. It is just… it's using the more general auto-exporter OTLP endpoint without these metrics or traces infix.
**Rajkumar Rangaraj** 07:17 Yeah, that's why we need to revisit and fix that.
**Piotr Kiełkowicz** 07:21 Sure.
**Rajkumar Rangaraj** 07:22 If I understand and recall correctly, this…
environment variable is somewhere in that. I just went vaguely taken a look at it. Blanche may know more about that implementation. I see this environment variable being present in the SDK. It's being… it's not being applied properly in the configuration. There is a bug in the OTLP configuration which needs a fix in that area.
Yeah, just to give some slight background, this is broken since a long time, but,
With the current bug, there is the only way to do a HTTP broad autograph from the auto-instrumentation, is to use OTLP exporter without that metrics, whatever you highlighted. That's the only way we can switch to HTTP broad autograph from this repo also.
**Chris Ventura** 08:19 Yeah, I do agree that something should be done in the SDK.
I think the argument here was that something could be done sooner.
**Rajkumar Rangaraj** 08:30 Yep.
I'm not going to block anything here if, like, I'd be happy, because it's needed much for us also. If we go on SDK route, it's going to take a very, very longer time than me fixing it here. That's why Sean created an issue here, rather than the SDK.
**Piotr Kiełkowicz** 08:49 So, that's the, I would keep it in 114, if you are fine.
**Rajkumar Rangaraj** 08:54 Unless, like, Sean finds bandwidth and comes here, it's fine, I believe.
**Piotr Kiełkowicz** 08:58 Sure.
what else,
some issues with NPG, SQL and TF Square, probably also with a Squirrel client, it is kind of…
With us for forever.
There is a room of improvements for file-based configuration to be…
To propagate configuration from file-based configuration to the native part.
This kind of… not fits in… directly in…
In the schedule, but hopefully we will be able to
Fix it in the upcoming months.
Kafka and slug fruits, also kind of all tissue.
Nobody is complaining, except us.
The lock bridges, there is an lock, but I think…
PR, but I think it is still not a blocker for the release.
I do not remember this one.
**Mateusz Łach** 10:12 Yeah.
Okay, so this one is a suggestion from FTCAR.
To basically replace the future usage with condition variable.
Yeah, so, let me follow up on that, with FDCar offline. I'll discuss, if,
If there's a swarf…
I, I mean, I don't think… it's… it is my understanding from FTCAR's comment that this is mostly, like,
The… the worry is about performance.
So… Let me follow up.
**efshaikh** 10:53 It should not be worse than the .NET performance. If anything, it could be better than .NET performance, because we do not suspend the runtime.NET Framework cannot be suspended.
So…
It's a narrow slice of performance, narrow thread, right? Just one thread is suspended at a time. So, performance-wise, I don't expect it to be worse than the .NET side.
**Mateusz Łach** 11:18 But we are talking about the .NET side right now.
**efshaikh** 11:24 Say it again? Actually, there is audio side…
**Mateusz Łach** 11:29 Yeah, can you…
**efshaikh** 11:30 dearly.
**Mateusz Łach** 11:30 Can you share the comment, Pietro?
The comment when this was…
Yeah, so some time ago, I was, I was,
Trying to fix the shutdown on our side, because we were… Running into some issues.
And I used the future, which I thought is, like.
**efshaikh** 11:56 Oh, sorry, so you're not referring to the profiler, you're referring to this.
**Mateusz Łach** 12:00 No, no, no. Yeah, to this one, to this one. I'm sorry.
**efshaikh** 12:03 Actually, there is something wrong with my audio. I'm not able to hear clearly. There's something…
Thing going on, but okay, okay.
So, what is the.
**Mateusz Łach** 12:12 Looks.
**efshaikh** 12:13 Question here?
**Mateusz Łach** 12:16 Yeah, so the question is…
**Piotr Kiełkowicz** 12:17 If it should be considered as a blocker for the next release, or it can be postponed, and improvements, or we can just close the issue.
**efshaikh** 12:25 I can fix this now that I'm annually working in that area, if you guys are okay.
**Piotr Kiełkowicz** 12:31 So…
**Mateusz Łach** 12:31 Okay.
**efshaikh** 12:32 I can fix this as part of my ongoing PR, because this kind of is adjacent to what I'm working on, anyways.
**Piotr Kiełkowicz** 12:40 If you can please create… if you can please create separate PR with small changes, your PR is big enough.
**efshaikh** 12:49 You want me to create a separate PR for this?
**Piotr Kiełkowicz** 12:52 Yes, exactly.
**efshaikh** 12:53 Okay, I…
**Piotr Kiełkowicz** 12:54 Olympia.
**efshaikh** 12:54 If you don't mind, Matt.
**Mateusz Łach** 12:56 Cool, sure.
**Piotr Kiełkowicz** 12:57 Right.
**Mateusz Łach** 12:58 Okay, thank you, thank you, FDCar, yeah. So, either way, this is… this shouldn't be a blocker for 1.13, right?
**Piotr Kiełkowicz** 13:06 Right.
My opinion is.
What else?
This is the, also, ancient issue related to the fact that we… include ASP.NET Core.
Instrumentation package directly to… how to instrumentation.
Shin?
And because of this, we have
we cannot execute auto-instrumentation on the runtime, except the SPNET runtime.
I doubt that we have bandwidth to handle it now.
**Igor Kiselev** 13:55 pretty big would be, because some fixes may require changes in SDK,
some features would require changes on how we structure dependencies, and we may need to make sure that iSpanet Core Bootstrapper is not an dependency pass for generic, and it would be really, really big work here.
**Piotr Kiełkowicz** 14:18 Nope.
**Igor Kiselev** 14:19 So…
**Piotr Kiełkowicz** 14:19 True.
**Igor Kiselev** 14:20 Ropolit.
**Piotr Kiełkowicz** 14:21 So, for sure, not for the release, in my opinion, and…
Redirection phase, we have a lot of improvements here, but there are still some…
some places to improve, but I think we are in a better place than the… The previous release.
And I think that's all.
I'm not sure if you think anything should go to 1.14.
Hurting, sir.
Finance?
So, if possible, I would… I would like to cut off.
There is early next week.
So… another perk.
Request, some GitHub stuff. I've seen the shown comments, but I do not have time to…
answer in these two PRs.
A SP.NET Core support.
So, it is kind of pretty important, so please review.
Hmm… Here is one of the attempts of…
fixing issue related to the OTLP environmental variables, but Rasmus is not available this week to move it forward.
But, Rash, if Sean would like to continue work this week, You can take it.
**Rajkumar Rangaraj** 16:28 Yup.
**Piotr Kiełkowicz** 16:36 FTCAR created kind of good, explanation how… Continuous profiling can work.
on the .NET framework, so worth to read it carefully.
The PR itself requires some additional changes, such as including integration tests, which we have for .NET.
But when done, it should be… But the…
Implementation details can be reviewed right now, so description and the review is ready to…
Ready to, to, to, to read it.
And…
Ryanair created this startup hook, I think it is…
Zach and Chris already review it.
I see. Igor, you have some comments?
**Igor Kiselev** 17:35 Yeah.
New minor comments, I think it will be fixed, probably today.
**Piotr Kiełkowicz** 17:40 So…
**Igor Kiselev** 17:42 It's very, very close to…
**Piotr Kiełkowicz** 17:44 Cool. So, when you are ready, I will… I will match it to tomorrow, probably.
just… just ping me on Slack, or WebEx, or what… whatever, that you are fine with this. I'll just approve it to you.
**Igor Kiselev** 17:58 I would approve it. Thank you. Would be all good.
**Piotr Kiełkowicz** 18:04 And the recent walk.
There were some changes, but I think do not have enough time to… to review it.
And execute it. Still on my kind of to-do list.
I don't know what else is here… No issues.
Oh, this is the issue for the next version, for sure.
There is a bug on the .NET side, which prevents us to… Correctly test…
I will show you.
One of the metrics.
Hmm… this identity matrix.
It was already fixed both on the main branch for .NET 11, and therefore hotfix branches for the SPNET core, but there were no release.
So… we have needed… I've needed to add this, kind of…
I'd be called to… to register, so…
Metrics class to generate it correctly.
When the next version of ISPNET Core will be released, we can… Let's remove these testing codes.
It is not affecting the production.
So, putting both of the next version and the project.
Matawus?
**Mateusz Łach** 20:16 Yeah, so… I noticed that some of the tests are failing randomly, so I started looking into them.
I haven't fixed them yet.
I don't think that you're…
they are blocker for the release, I'll try to investigate the source of the failures by the end of this week.
Basically, after I'm done with the… with the mem leak fix, so… Yeah.
**Piotr Kiełkowicz** 20:47 Putting for the next release, then.
I was not able to migrate build project, the new one, to the .NET 10, due to…
Some building issues, still need to…
create kind of small steps to reproduce and find the root cause. There is kind of mismatch between the load dependencies and
code we executed. We… the code we executed in… on the .NET 10.
Not a blocker for the release, it is kind of internal, so…
I think we can ask only for the minimum reproducible example, how to handle it.
I doubt that we have any data.
Dynatrace expert here.
I think other are not new, I will try to review especially the file-based configuration offline, too.
Check what we can do with these issues.
Discussions, and project assignment, and the project report.
No discussions, project assignments…
It is missing the project.
And I do not think we have army.
Oh, this one is in progress, in fact.
I think 10 board is up to date right now.
Do you have any other topics? Questions?
**Chris Ventura** 25:14 Thank you for organizing the stories for the release.
**Piotr Kiełkowicz** 25:20 Sure.
**Chris Ventura** 25:25 And then I just want to call up, I really appreciate the write-up in the PR for the Net Framework, continuous profiling.
**efshaikh** 25:34 Yeah, please take a look at it, and I'll be…
Watching that space for comments and feedback?
**Piotr Kiełkowicz** 25:54 So, thank you, have a nice day.
**efshaikh** 25:57 Thank you, Pierre. Have a good one. Hey, everybody.
**Mateusz Łach** 25:59 Thank you. Bye-bye.
**Rhynier** 26:01 Thank you.
