SIG: .NET Auto-Instr SIG
Date: 2025-10-15
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**efshaikh** 00:49 Hello there.
**Yevhenii Solomchenko** 00:55 Okay.
**Piotr Kiełkowicz** 02:36 Hey, guys.
**Yevhenii Solomchenko** 02:40 Hey.
**Zach Montoya** 02:52 Hello.
**Yevhenii Solomchenko** 02:55 Hello.
**Piotr Kiełkowicz** 03:15 I hope you can see my screen.
There is no specific topic to agenda.
Or you have something important to start with?
So, let's go for our typical, stuff.
All the requests, there is a couple related to…
Also, I produced today as PNET instrumentation and WCF.
But it's failing for some reasons.
I'll need to investigate why.
**Yevhenii Solomchenko** 03:59 Perfect.
**Piotr Kiełkowicz** 04:00 Come on.
**Yevhenii Solomchenko** 04:01 Hi, IS.
**Piotr Kiełkowicz** 04:04 That's about.
Anywhere you bet.
So, we need to understand why, and…
If needed, we need to fix it on the transcript repository.
We have couple PRs related to file-based configuration.
Evgeny, is there anyone you would like to start with?
I think it was last time Tracy Provider.
**Yevhenii Solomchenko** 04:36 Yeah, now I'm trying to…
I built for a lot of processors.
Instead of one…
**Piotr Kiełkowicz** 04:44 Okay.
So, which one other we should focus on?
**Yevhenii Solomchenko** 04:52 I think, important is, trace a provider and the instrumentation configuration.
**Piotr Kiełkowicz** 04:58 So, guys, if you have some time, it would be great if you review instrumentation configuration, this one, 4492.
**Yevhenii Solomchenko** 05:08 For plugins, I… Trying to, throughout, that's where we should place.
That, configuration causes out of… specification.
**Piotr Kiełkowicz** 05:19 Okay.
Zach, I see that you have started working on macOS.
**Zach Montoya** 05:28 Yep, just started on it. I have some failures that I need to look at.
But it just, updates from Mac OS 13 to 14.
**Piotr Kiełkowicz** 05:42 Okay, so I will fix the title. At least.
**Zach Montoya** 05:45 Oh, yeah, yeah, I started with 15 and then figured I should probably just go incremental and just do the next version up to 14, so… Thank you, Pat.
**Piotr Kiełkowicz** 05:58 Okay, so you need to double-check what's going concrete.
**Zach Montoya** 06:02 Yeah, it's not… yeah, it's not ready for review yet.
**Piotr Kiełkowicz** 06:07 Okay, and what else is,
Threekotel.net, I think it will be part of this one.
**Zach Montoya** 06:17 Yeah, that one's… I've included that in my change, so I can…
if there isn't any other comments on that, I can just close it and say it's included in that one.
**Piotr Kiełkowicz** 06:28 Okay.
Now, you reported this information.
Sorry, go nuts.
Okay.
OpenClient. The Rasmus, as I remember, is working on the…
Possibility to load the protobath in there.
Safe way to avoid some conflict, potential conflicts.
Otherwise, it's ready to… to review.
Unlock, there is no progress, and SQL comments…
I'm not sure what is the progress. I think we need to ping stiff in some private channel.
Zach, do you have any conversation with Steve?
**Zach Montoya** 08:14 No, I don't have any other updates since, he said he was going to…
Update the feedback?
**Piotr Kiełkowicz** 08:46 And I think that's all.
Or, Igor, do you have any new things to discuss here, or you are fine with current solution?
Recurrent state.
**Igor Kiselev** 09:02 Mmm… eats…
pretty close, to go out of draft. I still need to solve, a few issues with, transitive dependency generators that I found not work properly. At the same time, I try to, solve, issues… to solve
Oh.
something that looks for me as a problem that we compile it differently for Zip, Archive, and NuGet without any reason for it, so I try to solve that, and…
hope this week, I would… Make it out of…
Draft, and it will be ready for review for everyone.
**Piotr Kiełkowicz** 09:46 Okay.
**Igor Kiselev** 09:49 It's mostly working now already, so it… nothing… it would not change too much after it, at least idea, but it would still change… would have some changes how exactly we apply transitive dependency, where we define transitive dependency under 6.
**Piotr Kiełkowicz** 10:09 Okay.
And I think we have discussed others already.
So, Igor, you are referring to this issue, right?
**Igor Kiselev** 10:48 Yes, yes, I refer to that issue. That issue actually covers two points at the same time. First, we have, for no reason, differ in all official artifacts,
Each, different types of distribution have different, compilation of absolute same open telemetry auto-instrumentation.
I'm not…
Suggest and change anything in the development process, or how we build it, how we test it, except of a…
production build that we publish as a nerdy pack. For that build, we probably need to identify which, which job should be a primary for patching, managed assemblers.
and just collect the managed assemblies the same way as we do now in NuGetBuild, when we collect all profiler assemblies from different builds.
It would make it a little bit easier to understand what is official artifact of OpenTelem channel instrumentation, and
Second problem, first one, it's even not a problem, it's just minor inconvenience for someone who tried to analyze what libraries is in their output folder, and if they are valid or non-valid.
Second is a little bit, worse, because, we…
have, how we define dependency currently results that, we've been to different versions of system diagnostic, diagnostic source in, for .NET Framework, in, Zip Archive.
and NuGet package. In NuGet package, we build to all the support at 1, 9.00. In Zipper Hive, we've been to, 9.09.
It would be not noticed.
By customer, usually, because we do,
bend in redirection… we apply bind in redirection to the same version. But it actually should be two different processes. We can apply bind in redirection and redirect to a latest one, when we do, but we still, it still should be enough for us to bend, internally to an oldest one.
And…
it can be pretty easily done, and I would try to achieve it in my workload that I set that.
some of the…
**Piotr Kiełkowicz** 13:17 So, if I should choose… as we build NuGet packages probably on Windows machines.
I would say that should be our, let's say, primary build for managed roads.
**Igor Kiselev** 13:30 Right?
After it, I… I don't know yet how OCI and build, works, I have not looked into it yet, but probably after I would finish with the original PR, I could take a look here and also do it.
**Piotr Kiełkowicz** 13:52 I agree with Chris' comments that,
It… we need to have working…
At least locally, without spinning multiple builds. So, it is kind of mandatory for me as a developer.
**Igor Kiselev** 14:10 I fully agree with it, and I would even add that the only way to make sure that it is working is to still have CI legs that do it. So that's why I do… I suggest to still continue to use the same CI legs that we have. The only difference would be how we create a final.
**Piotr Kiełkowicz** 14:29 Or at least Becky.
If you take the, let's say, build pipeline, I would… Create the build.
the ZP builds, let's say, on this level.
Here, somewhere, and we have here the integration test. And the integration test should rely on the, let's say, final artifacts you would like to ship here.
Okay?
**Igor Kiselev** 15:01 Okay, sure.
**Piotr Kiełkowicz** 15:02 Make sense?
**Igor Kiselev** 15:03 Yes. Sinker? Yep.
**Piotr Kiełkowicz** 15:05 Right.
We have discussed this… I'm thinking terrible. I think we have discussed this last time, and Matayosh agreed that we can document it, just…
Somehow.
No progress here, no.
Mmm… I do not see Ranier today, so probably no progress here.
I will check internally what is the… Priority for this.
**Igor Kiselev** 15:50 We are working on it, there should be some progress this week, so… It's…
**Piotr Kiełkowicz** 15:57 Okay, so next year. Probably next.
Sorry, I'm not mistaken.
And… download…
Cruise… Yep.
**Zach Montoya** 16:14 So we.
**Piotr Kiełkowicz** 16:15 If he wants to close it or no.
**Zach Montoya** 16:18 We closed it, and then we reopened just to make sure, like, since they gave us a repro that they were able to run, that we make sure to give it a try. So, I'm assigned on it, and I just didn't get to it last week.
**Piotr Kiełkowicz** 16:33 Okay, great.
**Chris Ventura** 16:34 I closed it because of the stale label, so it might make sense to remove that label if I didn't remove it already.
**Piotr Kiełkowicz** 16:44 Let's see if mine as well.
Checking out quick.
Am I correct, yes?
**Zach Montoya** 16:55 Yep.
**Piotr Kiełkowicz** 16:56 Great, thank you.
Other are related to… file-based configuration. I think I can…
Let's say, clean up it offline.
No, we do not have any new discussions… everything is correctly assigned, and…
I doubt that we need to update anything on the… Our board.
Rash,
if you do not have any other important topic, there were the release of .NET 9 RC2, and
all OpenTelemetry.NET Ripple suffering when we're trying to upgrade to the.
**Rajkumar Rangaraj** 18:07 Yeah. Latest RC2. Yeah, I was just looking at that. Don't know, apart from me following up on that issue, to see if they released the…
Update for us.
It all points to the same issue where you pointed out from those, the PIs.
**Piotr Kiełkowicz** 18:26 Yeah, exactly. If you can make .NET guys aware about this internally in Microsoft.
**Rajkumar Rangaraj** 18:32 I, I…
**Piotr Kiełkowicz** 18:33 Right.
**Rajkumar Rangaraj** 18:33 just know as this meeting was going on, I took that and pinged one of the PM about this one.
**Piotr Kiełkowicz** 18:39 Cool, thank you very much.
And other topics, guys?
**Chris Ventura** 19:00 So, what build problem are you seeing with RC2 in the SDKs, just out of curiosity?
**Piotr Kiełkowicz** 19:08 I will share the screen once again, and share the link with you.
**Chris Ventura** 19:13 Because I'm seeing some weird things with the .NET SDK and older versions of Visual Studio.
**Piotr Kiełkowicz** 19:23 And what we're suffering, and… is here.
When you have system value type.
used somehow, it is failing. I will build on .NET Framework 462.
**Chris Ventura** 19:41 Yes, okay.
**Igor Kiselev** 19:49 I would bet it's because of, how to clean up
for NuGet, for not required NuGet, if .NET 10 is inside, a build. I'm pretty sure there was some flags to disable that mechanics, in mass builds that can be used as a temporary workaround.
**Chris Ventura** 20:10 Yes, that's what I'm running into on my local machine.
as well.
**Piotr Kiełkowicz** 20:17 But I think it is so important that it will be shortly fixed.
And we'll be notating next month.
**Chris Ventura** 20:28 Okay, so there is an issue. Oh, this is the issue in the SDK repo, okay.
**Piotr Kiełkowicz** 20:32 Yes, exactly.
**Chris Ventura** 20:34 Perfect.
Cuz… yeah, I'm seeing all sorts of weird behavior.
With, yeah, ValueTuple, and even Diagnostic Source.
with multi-targeted builds.
**Rajkumar Rangaraj** 20:51 I think in .NET 10, if I recall correctly, when I looked at the changes that's coming, there is a big change in the system value tuple.
They have done. Looks like, as they called out, it's a regression, than, anything else, so…
Hopefully this gets fixed sooner, based on what my observation is. Like, if we go and figure out, like, what's new in .NET, we will see some changes related to the value tuple there.
**Piotr Kiełkowicz** 21:23 there were not this compilation issue… issue in RC1, I can confirm, for sure.
**Rajkumar Rangaraj** 21:28 Yeah, that's why it looks like a regression than anything else. They are breaking the existing thing, yeah.
**Chris Ventura** 21:38 But yeah, the other big issue is the nougat pruning.
Which… has some weird behavior, depending on what version of Visual Studio and MS Build you're using.
**Piotr Kiełkowicz** 21:51 I have a separate branch for the upgrading auto-instrumentation. I think I commented out or blocked this pruning.
Or warming related to this pruning.
But when executed locally with RC1, it's working fine, more or less.
**Chris Ventura** 22:55 Well, I don't have any topics, so I'm gonna drop out.
See y'all later.
**Zach Montoya** 23:03 Sounds good. See ya.
Alright, baby.
