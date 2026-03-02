SIG: .NET Auto-Instr SIG
Date: 2025-10-22
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/Bn0sdYahND2jAy6wIicPeqYRdtXZoxsav71yaETkZIujbfgprLlM5Gw53WIH45gY.UcK1OPxac47PdQig
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 00:52 Hello.
**Zach Montoya** 02:55 Hey, everyone!
**Mateusz Łach** 03:02 Hello?
**Piotr Kiełkowicz** 03:23 Hey, guys.
**Zach Montoya** 03:26 Hey, bye.
**Piotr Kiełkowicz** 03:28 My computer is not working well today, so if you can drive a meeting, it will be great.
**Zach Montoya** 03:37 Sure thing. Alright. Yeah, let me, go ahead and do that.
Alright… Let's get started.
So before we begin, are there any agenda items that people wanted to discuss besides the… Schedules…
The gender that we usually have?
Okay, well, if something comes up, just let me know.
Alright, so we have a…
a bunch of PRs, some of these are Dependabots, we still have… the N-Log one, which…
Hasn't, been completed yet.
Looks like there might be some requested changes.
on here. Is this still… does this still Stan Pietro?
That you had, requesting some tunes for them.
Oh, it looks like they might.
Okay. Yeah, they're just having issues with running the tests, so we need to,
be running those correctly. Okay.
So we'll wait to hear if.
**Piotr Kiełkowicz** 04:55 Sorry, Zach, it is not only about the test, it is only… there is a fundamental problem about the method to choose to instrument.
It covers, let's say, couple of percent of typical usage of Unlock.
**Zach Montoya** 05:12 Oh, okay.
What's…
because I know that I identified, like, the other method that, like, the Datadog one uses, but for this…
Yeah, I'm surprised the… The… the other person, I forgot his name.
Didn't say anything about it yet.
Because, yeah, I think that's probably, like, what, one of the couple of APIs, but it doesn't cover…
We had an internal one that would, like, identify, or that would instrument, like, all of them.
Okay.
Yeah, so let's see. Yeah, so he's… still hasn't had time to revisit this, so…
Okay.
Okay, yeah, I think your review makes that clear, what needs to change, so… yeah, we'll just wait for the review, or wait for, any updates on that.
Let's see… There were a couple of questions, I think,
Steve Gordon finally got back to looking at this.
So I think he had most of the transportation up and running…
But was failing to actually… he was failing to actually get it running recently.
So I think you might need help from one of us to go take a look at this.
**Piotr Kiełkowicz** 06:51 If you have time today, it will be great, otherwise I will try to find some time tomorrow to look into it.
**Zach Montoya** 06:58 Okay, yeah, I think I should have some time today to look at this.
Do you know what this is about, though? I don't recall any… anything about this.
**Piotr Kiełkowicz** 07:08 It was removed, because in the country repository, we have decided to sanitize this method. We've sanitized SQRDB statements.
And it is basically no longer needed.
**Zach Montoya** 07:23 Okay.
Okay
would that affect this? I guess… so, is it… basically, we… the instrumentation sets it by default and sanitizes it by default?
**Piotr Kiełkowicz** 07:40 Yes, it is always sanitized, there is no possibility to, let's say, raw version put into the code, into the attributes.
Yeah, that's it.
**Zach Montoya** 07:56 Okay.
**Piotr Kiełkowicz** 07:57 I'm not sure if we already have this version in… Included in the…
into the build pipeline, but I suppose yes.
**Zach Montoya** 08:09 Okay.
Alright, yeah, I'll, I'll take a look at this to try and unblock him.
So I think, we looked at it, and I think it looks good. The implementation and the test cases looked like they were directionally correct, so…
Just a matter of getting up and running.
Alright, and then we have a couple of file-based configuration ones,
Do we need to dive into these ones right now? Are there any… .
**Piotr Kiełkowicz** 08:38 Tracy provider is the most important. I know about when issue.
Under the batch, you can specify console, which is always simple, let's say, processor.
other parts looks good to me, but I have a plan to review it tomorrow, and if… and fix the mentioned issue also tomorrow.
And if you can, let's say, check its current state, it will be great.
**Zach Montoya** 09:13 Okay.
So, is this the… Is this the reference schema that we should be implementing?
**Piotr Kiełkowicz** 09:20 It is not schema, but it is a good example for.
There are separate schemas in… Sorry. In the same repository.
**Zach Montoya** 09:31 Okay.
Alright, that's good to know then. Okay.
Alright, take a look at that.
Instrumentation configuration, there's some comments on this.
Is there anything else we needed to chat about right now on this?
Okay.
Alright, we'll continue with this review offline.
And, okay, so this one, Igor had, this one. It looks like you recently published this for review, out of draft. Did you want to chat about this one?
**Igor Kiselev** 10:17 Yeah, so I finished, main work for it, so what have been…
changed. I added one additional project to do a publish for .NET Framework, different version, so we still have a compilation for only one .NET Framework 462.
And we have additional projects on top of it that publish using different versions, so it would collect assembly… a different version of assemblies from NuGet packages.
I… yeah, it's…
Probably the main idea on top of it, we get a different list of, assemblies, to do redirected version in C++, so we now need to, push the multiple lists for different supported, .NET frameworks to, Profiler. We need to… the bad thing, I go thing, we now need
to, in runtime, to understand which version of .NET framework currently installed. We do it by register check, as Microsoft device in, both profiler and managed code. It would… and install time also to check which assemblies to push in GOC,
it can… if we are not able to get a .NET framework version, for example, because applications have a restricted permission and they don't have access to, runtime in that case, we, use
062 Road. So to be… to work the same way as it worked before. I have… I honestly think that probably we need to change it, and if we have not detected,
Suppose that we are run on 472, because it would be what most of users would run nowadays. And by the way, 472 and up, have the same binary distribution, so we do not have any difference between 472 and 48, 481.
They all look the same. And, probably last thing, the, so I utilized a feature, of central package management, new feature for pinning,
sensitive dependencies, so I utilized it
Very specifically, only in a project.
that use that collection and publishing of .NET framework assemblies, so it would not affect anything else. And with it, we don't need to mention all transitive dependency in project
So previously we have a duplication, so that we need to mention dependencies and central package management file with a version, and at the same time, in a project, otherwise central…
central defined version would not be used, whereas with that feature, we don't need it anymore, because
relative dependence would be correctly used for my… and I also tried to clean up a little bit how we update a file,
Central Package Management Version file, so that we validate that some
that package that we'd like to add in a version file have not been defined in either that or any upper level, so I utilized MSBuild API checking if, package reference with that, package version with that name already have been defined or not.
This particular framework, so…
Another thing, so how we collect dependency, we do… how we collect dependency, to not have
too much dependencies copied at the same time, so in most files would be same for old version of .NET. Only some assembles, mostly, that was built to support that node standard would be different.
So, now, after I publish an application, I go over through all .NET Framework folders, and if assembly, if the same version of assembly exists in all folders, I move it one level up, so it still would be in that framework folder, NetFX folder.
And it would be in a framework-specific folder as NET72 or NET642, only in case if the assembly is
unique to that version of Framework, on top of it for a future version of Net Framework. So if we, for example, have an assembly that have been used in net 062 and 4.7, but not in 471 and up.
In that case, I couldn't place it in upper level, but I can, I, left it in net
462 folder, and a net, for…
7 folder, I would create a file with a name Named del.link.
with a body that, define which assembly folder I have, which framework-specific folder I need to check to load that assembler, so it makes a little bit harder how we do assembly loading, but it's still pretty simple, I think. Oh, that's all.
**Chris Ventura** 15:43 So, I believe you had some questions that you wrote out in this PR, if we go to the conversation tab.
**Igor Kiselev** 15:50 Yes, so I feel that probably we…
there is a minimum coverage on automated test for it. I have not…
identified what we can automate. If you have any ideas, I would be more than happy to add that… that…
anyone would recommend here. so, questions, what I already mentioned. By default, we fall back for 462 version of Assemblies, but probably nowadays 472 would be a better candidate. So, 462 was
Do not change anything for customers, and it still should work the same way as it worked before.
But 472 probably would be a better option today.
Hmm… Second option was,
I removed one test. I believe that after we switch for transitive dependencies, we don't need it anymore. If
anyone thinks… The note, we can discuss how it will… should be replaced.
Next question was, as I said, previously we checked a dependencies, when we created,
when we updated project file and central package management version file, to match the dependencies, we checked that dependencies is not start with open telemetry or open tracing, because they was governed
already governed by that, central package management. But, as I start using MSBuild API, I don't need the check anymore.
But, at that time, I found that we have not defined a particular version for OpenTelemetry IP provider for three assemblies. So, right now, I defined them in
the project that gathers artifacts for .NET Framework.
But most probably, we should define them one level up, and just always have them as the same way as other OpenTelemetry assemblers.
Last… the next question was, so how we should integrate when I change this dependable bot, and I believe we do not integrate,
central package management assemblies, except off a top level, with 3, I think, assemblies, with dependable.
So, maybe we should, maybe we shouldn't. It would be an extension. We never have it before, but maybe we should do it. And, as I said.
If anyone would have an idea what can be automatically tested more here, I would be more than happy to implement it. Right now, the only test that I added, automated test, is a validation that, 472
is the last version that we need to define, and that all reference packages for upper version still produce the same binaries as 472, so we just validate that the packages do not define any
AFM-specific assets for version higher than 472.
Cool.
So, I would say that neither of those questions are really critical, and we could say that, okay, it's solved in some way already, and we don't want to change anything, but
At the same time, it would be good to…
to just compete on that, yeah. What we decide?
**Zach Montoya** 19:42 Okay, any other questions for Igor at the moment?
Alright, well, thank you for, walking through that.
We'll have to review that offline.
Let's see, so there's a couple more, plugins configuration…
And then update for ASP.NET, did you guys want to jump into any of these?
Particular.
**Piotr Kiełkowicz** 20:12 ISPNet, it
There is one important change. We are loading SPNet instrumentation when a system web is loaded. It is the only critical change, or important change, in this PR.
Yes.
**Zach Montoya** 20:27 Gotcha, okay.
Yeah, I mean, that… that sounds appropriate. I think Chris already commented as such in the conversation, so…
That sounds right. Is there any…
Any concerns about loading too early?
like… An IIS.
**Piotr Kiełkowicz** 20:53 Our test's still passing.
Well, that certainly makes you feel a very artificial, like, artificial scenario.
**Zach Montoya** 21:06 Yeah, that's my only concern, but I don't have… I think our… our testing would blow up if there were some bigger issues. Do we have… maybe, like, if there was some, like, multi, like, app domain… not multi-app domain… multiple sites on an app pool, if we had any automated testing for that.
That could possibly confirm or deny any issues.
**Piotr Kiełkowicz** 21:30 I think we are basically not supporting or not recommending multi-app in the same app domain.
It is the… it is our response, because there is hard to configure everything there. Separate service name, etc.
It is technically possible, but…
**Zach Montoya** 21:55 Yeah, I mean, for one, if our, if our existing testing,
is, is still, like, proving this to be fine, then I think that's a good, like, confidence indicator.
**Chris Ventura** 22:07 I mean, the only problem that I could see is, with loading things too soon, is some dependency not being available.
But I think all the main dependencies… Will still be there.
Because I don't think it requires…
like, Web API and MVC to be available in order for telemetry to come through. I really think that the telemetry mo…
HTTP module just relies on system.web.
And…
**Piotr Kiełkowicz** 22:42 I will double-check it, but I think you are right.
**Zach Montoya** 22:47 Yeah, this is… if this is the HPP module one, then yeah, that sounds like that should be the case.
Where it's only just registering a module and only referencing SystemWeb and maybe other BCL types.
**Chris Ventura** 23:05 Because all of the infrastructure for the HTTP modules are defined in that system.web.
Including, like, the base classes for HTTP modules.
**Zach Montoya** 23:17 So this one's ASP, is this ASPNet, or ASPNet telemetry Chief Module?
**Piotr Kiełkowicz** 23:22 ISPNets is referencing telemetry… HTTP telemetry model, so both of them.
**Zach Montoya** 23:28 Okay.
Hmm…
**Chris Ventura** 23:40 Yeah, and the only assembly reference is system.web.
**Zach Montoya** 23:50 Okay…
Yeah, system up.
API. Okay.
And then I…
**Chris Ventura** 24:05 then I believe all of the other dependencies are things that we, pull in.
**Zach Montoya** 24:11 Yeah, OpenTexture API… As well as… oh, wrong one.
Yeah, I assume we bring these ones in as well.
**Chris Ventura** 24:26 Yep.
**Zach Montoya** 24:27 Okay, yeah.
That seems… yeah, seems fine.
Okay.
Cool. The one question I did have, which I… I had just left a comment very recently on it, but, the…
This module tests… Can you clarify what this module test is asserting, or, like, what this is doing?
**Piotr Kiełkowicz** 24:51 module tests are listing all OpenTelemetry dependencies. I mean, by the prefix… libraries, prefixed by the OpenTelemetry.
And, module… tests… application, for some reasons, is loading system web.
And if you're loading system web, it triggers that a SPNET instrumentation together with telemachine modules should be loaded.
So, it is loading.
And, based on this, we need to adjust this module test.
**Zach Montoya** 25:28 Got it. Okay.
Cool, yeah, sounds good.
Right?
Yeah, I can finish reviewing this in a bit, but…
**Piotr Kiełkowicz** 25:44 And the last one, file, you… you are displaying is the…
It is to ensure that we correctly propagate data on the RWIN and add the test for the metrics, because
it was not tested at all, and it was not working. And it was even malfunctioning on…
Before this… this changes, because we were not loading… we were loading only telemetry modules, which were
Creating activities, and after changes, it is not creating activities, but the instrumentation library is responsible for this, so…
To ensure that both metrics and… Activities are correctly managed, so… We have these tests.
**Zach Montoya** 26:41 Gotcha. Okay.
Sounds good.
Alright, I'll finish reviewing that in a… Bits.
Any other… Any other PRs that we should discuss here?
Alright, let's move on, let's see, new issues…
Let's see… I think these are all… we've already covered this…
Igor, this binary's different, different distributions, is this just the PR that you've been working on, or is this a new issue?
**Igor Kiselev** 27:27 So, yeah, we discussed it on previous, previous time. So, it's…
talk about two different issues at the same time. One of them I would already implement in the current PR, so that, we would have, the same reference for NuGet packages and non-NuGet packages by moving all,
dependencies to a separate project. And on top of it, we need to add a job that would
collect, that would collect managed artifacts before packing zip, or new get packages from one job instead of all jobs, so I would work on it a little bit later, probably once we would merge my initial pull request, otherwise it
could not be extended to NuGet packages yet.
**Zach Montoya** 28:19 Got it, okay.
Cool, thank you for, clarifying.
Okay, so in that case, nothing, anything else that's new, can move on.
Discussions… I… that's nothing, yep.
No issues should be added… Project board…
Looks like there's any changes we need to add here.
Any… any input here?
Things that we should be, moving around on here.
**Chris Ventura** 29:11 There was a issue that we talked about a week or two ago, Zach. I don't know if you had time to look into it, it was trying to reproduce…
A problem that was reported?
**Zach Montoya** 29:25 Yeah, I still… I haven't had time to look at that. Okay. So, I don't have an update on it.
Let's see…
I'll just put that… I think we can put that on the project, though. Just put it as committed, just to make sure we evaluate that.
Oh.
There we go.
Cool.
Alright, anything else on the project board?
Alright.
So I think that wraps up our regular agenda.
I'll make sure to review some of these PRs so that we can…
Keep making progress, especially on the, the… file-based configuration stuff?
But yeah.
Is there anything else you guys wanted to chat about while we're all here?
Alrighty. Cool.
Well, thanks everyone, see you next time.
I…
