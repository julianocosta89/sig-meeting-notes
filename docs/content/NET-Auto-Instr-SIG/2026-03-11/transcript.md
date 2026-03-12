SIG: .NET Auto-Instr SIG
Date: 2026-03-11
Duration: 24 minutes
Zoom Recording URL: https://zoom.us/rec/share/nBgVbrqa_oZRF6gRZtTUFxY5b4LReglU7uPr0vi2dC0Vp3VIB6NXuCAZ68S0uus.ALXsVPyphDh3InL0
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 02:35 Hey guys, Omni Splanks again.
**Alexey Pukhov** 02:42 We like this meeting.
**Piotr Kiełkowicz** 03:45 Chris will not be able to join.
Isaway also…
So, there is a small chance for… Yes.
Caesar.
Chris, for sure, will be not able to join.
**Zach Montoya** 04:20 Hello…
**Piotr Kiełkowicz** 04:21 So… Hi, I think we can start.
Discussion.
The contact box.
So, let's try our tweeze.
pull request, new ASDK, and it means that, in this case, that we need to upgrade also Alpine with its packages, so waiting for,
Another look to… to be merged.
The second one is related to the knockout functionality and covering more collection types.
By the size method, so if you would like to have… take a look, it would be great.
Chris created this PR related to the stability. To be honest, I didn't have time yet to look into it.
So, I'm not sure if… if you would like to discuss it today, or… Offline. Offline.
**Zach Montoya** 05:48 Yeah, I think we could talk about that offline. Is there comments to that?
**Piotr Kiełkowicz** 05:54 Hmm… Alex, yes, PRs related to… Assembly ver… assembly version conflicts.
**Alexey Pukhov** 06:07 So, I'm at the final stages, so it's all about…
new automation by this point. So we did some Internal testing.
Which showed great results.
So we moved on to those mandatory testing that we had to do, and there we start seeing some issues. So,
Quick thing… starting from .NET 9, during the OpenTelemetry initialization, somewhere in the internals of the .NET,
There was a reflector call… oh, sorry, yeah, there was a reflection call to some of the open, system diagnostic types.
And the reflection was not that supported by the…
native profiler redirection. Well, native profiler redirection doesn't, handle the reflection.
So that led to the load of the system diagnostic source, Ian?
to contact us, which exact… which is exactly what we don't want to do. So, the long story short.
I thought…
I mean, I didn't expect we're gonna hit it that fast, so it's not something unusual, but I just didn't thought we have to do it now, but looks like we have.
So, there will be a small change.
To… specifically to the native.
Bath.
Where we have to handle the reflection calls.
Oh, and the problem there happening before we… well, I mean, it doesn't matter where we set up.
Our direction, it's still reflection.
So we have to handle this. There is a,
Fairly easy solution to do this.
But I think we should do it now.
Even though none of the automation from… existing automation from OpenTelemetry caught this, none of our internal testing hid that.
But the moment I start working on those mandatory tests, that's where we hit this.
So yeah, this is a short, quick…
**Piotr Kiełkowicz** 08:25 That's what?
Would you like to include this fix into existing PRs, or as a follow-up?
**Alexey Pukhov** 08:33 Well, I mean, I discovered this, while working on those tests that we wanted to ship with PR.
So, I would say we should do it now. I mean, I…
**Piotr Kiełkowicz** 08:46 Okay.
**Alexey Pukhov** 08:47 I, I understand that, The car is getting bigger and bigger.
But… that…
I mean, we can do this as a follow-up, but I would say we should do it now, because we just literally hit it on those tests that we decided should…
support the change.
**Piotr Kiełkowicz** 09:07 Okay.
**Alexey Pukhov** 09:10 Cool, Jim?
That's all from me, so I'm still hoping final stage.
**Piotr Kiełkowicz** 09:20 Hmm… there is some PR from Matt related to…
multiple application polls. It is still on my to-do list, to be honest, so… If you have time.
Please review.
And… what else?
Ongoing discussions on file-based configuration.
And how we should behave.
Behave when the file is not existing, and it is enabled.
Should we… Gracefully shut down, continue without this, or whatever.
**Yevhenii Solomchenko** 10:08 Yeah, we can discuss. From my opinion, the best option will be just that sort of the exception.
Even, it's a fail-fast setting, because, we cannot read the file-fast setting without the file.
**Piotr Kiełkowicz** 10:27 So, should we just… Behaved like… like as an operation.
Open telemetry.
In that cases?
**Yevhenii Solomchenko** 10:41 Oh…
**Zach Montoya** 10:42 If we can't get to the fail fast setting, or it's not in the environment, we should probably just…
Assume that it's… we're not failing fast, and we just try to make that a no-op.
**Piotr Kiełkowicz** 10:55 Yep.
**Zach Montoya** 10:56 Is that… was that what your question was?
**Piotr Kiełkowicz** 10:58 Yes.
I think it should be the solution.
So, if you configure… File-based configuration, and file is not existing, we should…
Typically work as an operation, just log error.
In the fight base.
Into the files, sorry.
Does that make sense, Steve Guineau?
**Yevhenii Solomchenko** 11:24 Without the exception, but exception will be thrown from the…
When you try to read the file, instead of manually throw the exception. Anyway… So, you should redirect.
**Piotr Kiełkowicz** 11:42 Silently… you should silently continue and avoid any configuration from the OpenTelemetry instrumentation. You should just disable it and log errors to the file configuration… to the log file.
**Yevhenii Solomchenko** 11:59 Without the exception.
Strongly exception.
**Piotr Kiełkowicz** 12:04 Whatever. If you need to throw exception here, it is fine, but you should not kill the application, you should silently continue.
**Yevhenii Solomchenko** 12:21 Okay.
**Piotr Kiełkowicz** 12:23 If you want to read
file fast setting, you need to read the file. If the file is not existing, And…
File-based configuration is enabled. You cannot read this, so you need to silently continue.
**Yevhenii Solomchenko** 12:41 Great.
Right.
**Piotr Kiełkowicz** 12:47 Is it okay?
**Yevhenii Solomchenko** 12:52 So it's, like, more redirecting to the environment variable configuration instead of…
**Piotr Kiełkowicz** 12:57 Whoa.
you have read configuration that you need to read file-based configuration, but it is… the file is not available, so you are just disabling OpenTelemetry auto-instrumentation.
**Yevhenii Solomchenko** 13:11 Oh, okay.
**Piotr Kiełkowicz** 13:16 So, it should work more or less like empty… file.
And I think that's all what we have.
What else we have? Sorry, I found one.
new issues.
Eagle.
**Igor Kiselev** 14:02 So, it's, while we have done, internal tests of, assembly loading, we've done it also for .NET, redirection, while it's exchange, we've also done it in, for .NET Framework.
And here, we identified interesting issues. So, currently, we suggest, customer to install us on .NET Framework assemblers in GOC.
But, with my changes that I have done before, in a lot of cases, we should work without, installing a semblance in GAC, and in many cases, it's better, because, if customers keep GUCK installation, he is not risking of installing
of killing other .NET Framework applications by just installing . OpenTelemetry.NET agent. And in that case, we install, our assembly resolver on… in a main method.
So, if we need to resolve assembly from a main method, it's too late, for that location. It's possible to fix by moving our,
assembler resolver from customer entry point to some method in .NET Framework that would be called just before the control passed to a customer entry point.
It's up to some of them only to be tricky through different things. We can discuss it later. Right now, it's just a ticket to Trex that we have an issue, and probably we would fix it in the future.
On my, some config switch to enable affix, right?
**Piotr Kiełkowicz** 15:48 Do we need it to, in the next two years.
**Igor Kiselev** 15:50 You saw Justin X. No… Just at some point, I'm not sure how we track it, but…
**Piotr Kiełkowicz** 15:57 To the next extent, when needed, we can just put… Yes, yes.
The other milestones.
**Zach Montoya** 16:04 So, this doesn't cause any crashes or anything in the meantime, right?
**Igor Kiselev** 16:08 If customers use a GAC installation, which is a recommended scenario, it does not, result in any crashes. If customers keep GUC installation on .NET Framework and try to use it in an application that,
that use a s… Z… Were a main method.
use assemblies at VeraDirect, it will result in customer application crash. But right now, it's not official support installation pass.
**Zach Montoya** 16:45 Interesting, even if…
does it still crash in the regular, the default? Like, I forgot what the loader optimization is with the default one, where only MScorelib is installed shared domain, and everything else is in…
Just, like, the one domain, it still fails in that case?
**Igor Kiselev** 17:04 It would fail, for example, if you have a console application, and console application use, some Microsoft extension dependency injection class, or something like, like that, and for a direct,
that Microsoft extension assembly to some new version. And now, in runtime, an application is unable to phone that Microsoft Extension Assembly, and it would crash with a…
or the main method is that NSMD reference is not… was not able to… to be found.
**Zach Montoya** 17:41 Okay.
**Igor Kiselev** 17:42 If it is in GAC, yes, it will be found. If it is in the application folder, so somebody copied it in the application folder, it will be found, but…
**Piotr Kiełkowicz** 17:51 Otherwise, yeah.
**Igor Kiselev** 17:52 It would be crush.
**Piotr Kiełkowicz** 17:54 Nigor, do you have, kind of.
Ready codes to… or steps to reproduce.
**Igor Kiselev** 18:01 I would, we would work to add some steps to briefs here.
**Piotr Kiełkowicz** 18:05 Yeah.
Even if we are not working on now, it will be beneficial to document it, how to make it.
**Igor Kiselev** 18:13 Trust me.
**Piotr Kiełkowicz** 18:14 Hippin'.
Ranier?
I think you are still waiting for a response from Rash.
Ranier, could you please ping Karash on Slack?
Ranier is not saved.
Alright, Pinkross.
This comes…
Hmm…
**Igor Kiselev** 19:10 By the way, by the way, with my previous task, we already have a test, in our OpenTelemetry end-to-end test that exposes behavior if we disable, registering assemblies in GOG.
So, by default, we… before we run end-to-end test, we register assemblies in GAC. Without those steps, the test will fail. I would mention which test it is.
**Alexey Pukhov** 19:35 Oh, I mean, this is a test that I'm extending as part of my pull request. This is the assembly redirection on Net Framework. That will for sure fail if you don't have assemblies in GAG.
**Piotr Kiełkowicz** 19:50 Cool! So, if you can just mention these two steps, and refer to the particular test, it would be great.
**Igor Kiselev** 19:57 Sure.
**Piotr Kiełkowicz** 20:05 I think you can still postpone discussion about this one. One more week, let's… Plant the…
**Igor Kiselev** 20:12 I'll send you a direction.
**Piotr Kiełkowicz** 20:15 On the main.
And it is the issue… We have discussed during the PR, so we are fine here.
Certainly.
It's empty, that's fine. Also empty on the… Hmm…
What do we have? We have the boards to verify, and I think we are…
Who defines things right now.
Nothing to update.
Do you have any other topics to discuss today?
**Igor Kiselev** 21:27 A small question.
With a file-based configuration, right now, file-based configuration, total override, all environment variable. Is it design behavior, or it's something that we can change?
I'm talking about shouldn't merge with environment variable configuration, or it should override them, especially in case of a collections. So my…
My problem with right now, specifically with the plugins, if customers have a file-based configuration, we would rate plugins from file-based configuration and would ignore plugins that have been configured through environment variable.
**Piotr Kiełkowicz** 22:09 true.
**Yevhenii Solomchenko** 22:10 Yeah, that's correct.
**Piotr Kiełkowicz** 22:12 But you can inject environmental variable to the plugin by placeholders.
Anti-tw.
**Igor Kiselev** 22:19 Giveaway.
**Piotr Kiełkowicz** 22:20 that's to DeFi.
**Igor Kiselev** 22:22 If customer configured it in a… in the file, but there is… Pretty tough.
Okay.
Got it.
Excuse me.
**Piotr Kiełkowicz** 22:36 That's expected? Unfortunately or unfortunately?
**Igor Kiselev** 22:40 Okay, in my case, it's unfortunately, I would discuss internally that case what can be done.
So…
**Piotr Kiełkowicz** 22:46 There was a plan to have what you see is what you get in the Firebase configuration. It is not fully true, but let's say almost.
**efshaikh** 22:58 So, on AppDecidegor, there is one place where we merge the environment variables and what is there on the file, right?
Cool.
**Igor Kiselev** 23:09 Unfortunately.
Okay, we will discuss it internally later.
Because it's not a problem for hotel. Okay, unless we are not saying that, unless we would like to give an ability for environment variable, to…
do some changes to, customer config, and give away, for example, install a plugin by multi-level lookup, or something like that, the server install some additional plugins for OTEL Auto Instrumentation. Unless that is not a design… a feature we'd like to design for, we don't have a topic to discuss in OTEL.
If we think that we may need a situation when computer configuration would
force some additional plugins into Hotel Auto Instrumentation, so in case we can Think a little bit more.
About it.
**Piotr Kiełkowicz** 24:16 So, thank you! Have a nice week!
**Alexey Pukhov** 24:23 Thank you!
