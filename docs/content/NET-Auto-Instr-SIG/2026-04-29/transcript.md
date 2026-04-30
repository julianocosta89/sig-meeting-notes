SIG: .NET Auto-Instr SIG
Date: 2026-04-29
Duration: 64 minutes
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 04:55 Hello?
**Alexey Pukhov** 05:03 Bye.
**Zach Montoya** 07:22 Hi, everyone.
**Yevhenii Solomchenko** 07:27 Aye.
**Zach Montoya** 07:32 Would anybody like to drive today?
Alright, I will take that sounds as a no. I can, One second, I'm just setting up today's… Notes… Then I can start leaving the meeting.
Alright… Share screen… Alright, perfect.
Well, we're almost at the end of April. It's pretty crazy.
Let's go through our agenda.
Just preloading everything. Okay, great.
Alright, support requests, we have a bunch of… Dependabot ones.
We have a couple in draft, so… Let me know if there's any of the ones that are in draft that you guys would like to discuss.
**Igor Kiselev** 08:48 Yes, there is one in draft, do not reference OpenTelement Transformation iSpanet Core, I need some feedback on it. So here is… I just… I have not finished it, but I just show what it would be. So, I try to use the same approach with iSpanet Core as we do with Redis, so instead of referencing iSpanet core always, it would be optional reference that we validate at a build time, and if we notice that customer is building iSpanet Core application, and he have not referenced, iSpanet core instrumentation, we would show him an error unless he would suppress it. So it… Will require some Tuning and polishing, if we would like to do it.
especially because I spent Quora is a lot of our customers with Redis, only a small percentage. But that would, solve an issue that, if NuGet package referenced in console application, and that console application later published to, just.net.
We now try to found iSpanet Core SDK, because we… grabbed it from OpenTelemetry Instrumentation I spent before. It's also a little bit better elegant with, idea of NuGet that you get only what you are actually using, and if you would like to use anything additional, you need to reference it.
So… And fails it right now, if you would open any test failure, it would fail exactly with the problems that customer will have. They said that you have an application that references Panet Core, but you have not referenced OpenTelemetry instrumentation ISPANET Core. So… That's why I intentionally have not, changed, end-to-end test right now, so… Just… feedback, if you think it's a proper way, future, or if you say… think that it is, it would create more Burden on our users to add additional reference.
So… We can do it a little bit nicer, but the question is right now about an idea.
**Chris Ventura** 11:08 Does it work with the framework reference that needs to be pulled in for…
**Igor Kiselev** 11:13 Okay, right now, I just make it a little bit dirty, and in our target file, I just manually created from each framework reference that application has. A thing that we validate.
Here is your looking on it. But we could do it as an additional input for our build task, or even as that could work as is.
Yes, it works with some adaptation.
**Chris Ventura** 11:46 Okay, because I think the last time we had looked at doing something like this, it was the framework reference that was required.
That, made things more complicated, and so we kinda… Just left this in the backlog.
So, if we're able to find a way around it.
**Igor Kiselev** 12:08 Yeah? You're, you're right now, you're right now looking at the, at the way… Around this.
At least with my test and with end-to-end tests, we see that it works.
**Zach Montoya** 12:23 So, what would the out-of-the-box behavior be, then, if you just added just the OpenTelemetry auto-instrumentation NuGet? It would just be no instrumentation, and then… Would there be any feedback?
Or any sort of user…
**Igor Kiselev** 12:40 So, okay, if a user have an iSpanet, project.
and he would upgrade to a later version of our NuGet package that do not automatically reference iSpanet Core. He will see a build time error for his project, saying that you need to add, open, open telemetry auto-instrumentation iSpanet Core, or you need to Add it to exclude said properties that that disables an error saying that I don't want action to instrument I spent core.
It will ask Kim to Azer.
Add skip instrumentation, or to add.
the package.
**Zach Montoya** 13:25 So that'd be, like, this property here?
That they would need to update?
**Igor Kiselev** 13:29 Yes, yes.
**Zach Montoya** 13:30 Okay.
**Igor Kiselev** 13:33 In most cases, customer would not like to add deep instrumentation. In most cases, customer should just add additional package reference.
**Zach Montoya** 13:51 Yeah, I'm wondering… I'm trying to think about that. I wonder if… we should… break the compilation? Like, wait, how does this… how does this fail, then? It… does it actually break compilation?
**Igor Kiselev** 14:02 Yeah, it break compilation would show an error, is it?
**Zach Montoya** 14:07 Hmm, okay.
Seems a little strong.
**Igor Kiselev** 14:11 I think we should break a compilation, because after that update, they would get an appla… if they reference our OpenTelemetry auto-instrumentation as a NuGet package, they expect that the application would be instrumented. If, after migration to a new version, the application would not be instrumented.
It's much better to break them at a compilation step and say that, oh, you know.
After that upgrade, you have not completed that upgrade, then allow them to compile as Deploy, and only after it, found that, they lose all instrumentation.
So…
**Zach Montoya** 14:50 Okay, so by default, if they have the OpenSeometry auto-instrumentation, we have two scenarios, one just console, and then one ASP.NET Core, like, as the framework.
Console, this shouldn't run because we haven't detected ASP.NET Core in the build, or sort of the, packages.
So nothing happens.
And then for the ASP.NET Core one, so they set the, like, web, framework equals web, or whatever, they just add… open telemet Transportation, they get this error saying that they should add a spin at core or… or skip it, and then they make the appropriate change, and then they get instrumentation. Does that sound right?
**Igor Kiselev** 15:34 Yes.
**Zach Montoya** 15:34 Okay.
**Igor Kiselev** 15:36 So, I would tweak it a little bit more. So, right now, we check that versions that we added is explicitly defined, so if a customer have a newer version, it would fail. It's not, intention for NuGet packages, it should do a check.
start doing the same range check, so that's why I said that I would require a little bit more work on the pull request. If we intend to go this path, I would polish it. Otherwise.
I don't want to spend my time on that.
**Zach Montoya** 16:10 Yeah, I think that makes sense. So, like, out of the box, like, well, of course, we can include in our documentation as well that they should add both, but if they, you know, just upgraded their current one.
I think… I agree that we should give them some notification, either a build error or a build warning.
That… They need to add this package?
So in general, yeah, I agree with this direction.
**Chris Ventura** 16:42 Yeah, and there's no way for us to automatically pull it in, because… so we can't hide it behind a setting that says.
enable a SpeedNet Core Instrumentation, because that would require us to have an official dependency on that package, which would bring the framework.
survive.
around is for them to manually add it, if they wanted.
**Igor Kiselev** 17:12 Alternatives would be for a fix, would be either to work with OpenTelemetry Instrumentation as Panet Core package, and remove framework reference from it, On one side, it's maybe a correct option, because it should not break anyone, because anyone who would like to instrument I-Spend at Core would have a framework reference already.
So, on other side, if we look at it only from instrumentation point of view, having that framework reference for them is a proper way, otherwise it would be a hack that would not break anybody, but to make it compatible with us.
The… Another thing about what we can do, but it's all, again, a hack. We could, instead of adding it as a normal NuGet metadata that we reference, OpenTelemetry Auto Instrumentation, we could try to reference it from our target.
it would have few bad things. First, we would reference something that is not explicitly visible when you look in the package in NuGet, and it could be… somebody could be not happy about it, especially for somebody who tried to do SBOM, or do a security analysis, or something like that. And second thing, it may result in a build failure on the first build, because First time, restore would restore our files, but on the second run of a build, it would still have a missing package, so… I… Strongly don't like that approach, despite it's also possible.
We could do other…
**Zach Montoya** 19:05 Also strongly dislike that one.
**Igor Kiselev** 19:07 We could do some other hacks. We could try to implement, something that would remove framework reference from… if we added it. We could do, something like if we remove package reference if it was, added by us, if we detected that… so… but all other approaches are much harder, so I think that, we really have only three options. First option, we would close the issue as, for NuGet, not working properly, as we do not plan to fix it. Second option, we go to OpenTelemetry Instrumentation aspect core.
And remove framework reference from it.
throw some hearts. And third option, we use that approach.
I like that approach more than… Any other options, but…
**Chris Ventura** 20:00 Yeah, so I'm just gonna think through the option of, let's say we don't do it.
So, one of the main reasons this ASP.NET Core package still exists is for, proper baggage propagation and, trace context propagation.
And I don't know what the status is of the native support.
for those propagators in .NET.
I'm assuming at some point there'll be native support for it, in which case this package isn't required anymore.
**Piotr Kiełkowicz** 20:43 I think, Chris, you have… to… you touched two things. First one, the native instrumentation in SPNET should come with .NET 11.
So, kind of, couple more years for us with this. Also, propagator was changed in .NET 10 or 11, I do not remember, to the… to support W3C natively.
But I'm not sure if we are working correctly without… without this package.
I mean, if the server side is the SPNET, of course.
And the last thing, if we consider this change.
I'm pretty sure that we should treat this as a breaking change from the user… end-user perspective, and we should consider to, oh.
release, and I'm not so happy with this in… And making the two-hour release right now is kind of problematic in context of the whole security analysis stuff, it's… it will take kind of a couple… Once more.
**Igor Kiselev** 21:57 I'm not suggesting to solve it right now, I just open it to just get… It's about if we like it, or if we don't like it at all.
**Piotr Kiełkowicz** 22:09 I… I'm fine with this solution long-term, but I think it requires bumping to 2.0 version.
And it means that we will have kind of two branches to… to support, and in context of everything codecs or other AI tools are doing, I think it is not the best moment, to be honest.
But I can be convinced to not releasing this as 2.0, but I suppose we will have kind of… Bad comments.
**Zach Montoya** 22:51 Week.
**Piotr Kiełkowicz** 22:52 the community.
**Zach Montoya** 22:54 Let's see. So, part of the change is that we… actually just remove… this package reference.
I mean, the short-term thing is we could… Have an opt-in, like, build property to remove this.
That way we… You know, a user can get their console app working.
If needed.
**Chris Ventura** 23:21 I mean, I guess another alternative is just having a second NuGet package.
That would be opt-in, and yes, it's more… Artifacts for us to have to maintain, more choices, For end users to… To have to choose between, but that would be a non-breaking change that could be done sooner.
**Piotr Kiełkowicz** 23:58 And even if you fork now to two packages.
We can potentially merge them together with… With the major updates.
And just abandon one of them.
**Zach Montoya** 24:18 Would it just be, like, a lightweight… package that's… just has package reference, open source instrumentation, ASP.NET Core.
**Chris Ventura** 24:37 I mean, we could do that for a while, for a migration period.
But I think NuGet has some mechanisms for recommending a replacement package, too.
So that you can get some, warnings in your pipeline.
So… because native support is coming, even though it'll be a while, I'm hesitant to make a change, because I don't know what would happen first.
Us having enough critical mass to have a 2.0 version?
Or, the native support is gonna be done first. I… I don't know which is which.
So I think… It would be nice to go with an option where we don't need to have… are breaking change.
**Igor Kiselev** 25:45 Yes, most probably it would be a second package. The bad thing is that I'd prefer a second package for including Ice Planet, but we could have open instrumentation, or tell out instrumentation minimum, or something like that.
Awww.
It may require a little bit more thought about it. In that case, the proper design would be, yeah, create something like OpenTelemeter Auto Transformation minimum package. That, package would, remove all Instrumentation, resource, so everything for which we could switch to that mechanics.
Witch all packages to that mechanic, so that you pay… that you get only what you want.
And then, after it, our OpenTelementation, our instrumentation package, for now, for compatibility reasons, would still Add all reference that we previously have in lower-level packages.
And, visit… it would be, okay, if you need something that is a minimum, use that package. If you… okay, and after it, we would give you, warning, an error if we detect that you probably missed something.
Otherwise, use a bigger package that includes everything, but yeah, it is not well designed, well worked with, can just console application, and probably we will fix 18 version 2.0, something like that.
So, it's a little bit bigger refactoring how we build our package and how we prepare it, but probably a… Good way that would make it By 2.0 more tested solution, and in 2.0 we may do something different.
**Chris Ventura** 27:49 I don't have a good sense of how often this problem comes up.
It seems like the vast majority of our end users are monitoring It's been a… Core Apps… And there's fewer that are just monitoring more of a console-based application.
Where the… The ASP.NET Core runtime isn't available.
Because I think the main scenario… is either a Dockerized case or a server that doesn't have the ASP.NET Core runtime available.
**Igor Kiselev** 28:33 It's right now a little bit bigger than that, because the question is about, do we really want that all our users get all instrumentation package for a NuGet case all the time? Because each additional DLL, it actually increases the vulnerability scope, for example, for a user. If we have some comes in bed there, now you have a DLL that you could easily load in the process, because we provided it with you. So, it may be good for users if we create some way to install auto-instrumentation.
Where a user would get only what they really need.
**Chris Ventura** 29:12 Isn't that the point of the, declarative configuration?
**Igor Kiselev** 29:20 Not really.
**Zach Montoya** 29:22 We had to ship everything still.
**Chris Ventura** 29:24 Yeah, we ship everything, but it's turned off.
**Igor Kiselev** 29:30 you ship it, so it's easy for assembly loader to load something. It's, again, it is not that we really give you… expose you to vulnerability, but now, it's much easier. So, we already delivered a file with vulnerability to a customer computer, even in a case when that file is not needed for them at all.
from a NuGet package.
There are two approaches, actually, for NuGet packages. One is for normal packages. The advice is always, reference as minimum as possible, and if you have something, create a separate package that would include more.
If you really need it. But at the same time, if we look into Spanit Core, they… started with that approach in iSpanet Core 1.02.0, and then they found that, in most cases for a customer, it is not working, as customer usually needs iSpanet Core as a whole, and then they switched to framework reference, so that they delivered everything. I don't know what's more Applicable to our case.
by some ways.
**Zach Montoya** 30:48 Great, huh?
**Igor Kiselev** 30:49 Sorry, just a note that for a user where we break ice console application, I could come up with a small, must-built script that customer may add to their project.
And, which effectively will remove framework reference, and it would solve a problem.
Specifically for console application, we can document it and say that, okay, we know that there is… we create some problem for console application, please add that must build script in your project to… as a workaround.
But it's also possible.
**Zach Montoya** 31:27 Yeah, I was just thinking, as we were talking about all this, that I feel like just a targeted workaround… would be best without, like, changing our NuGet packages for now. I don't know if… If we simply, like, go to this line, this package reference line, like, if we condition this on a property or something, if that would… Solve… it wouldn't…
**Igor Kiselev** 31:49 Nope.
**Zach Montoya** 31:50 That's all that.
**Igor Kiselev** 31:51 Because, it's a condition not based, so we create… from that package reference, we include it in our metadata. So, and it, right now, our NuGet package have a reference or don't have.
And the only condition on which a NuGet package may have or may not have a reference is a target framework. So there is no way for us, based on a property, to include or not… for a NuGet.
include or not include, dependent packages based on it. So.
**Zach Montoya** 32:27 Does that reference, though, instate the framework, or is it only a build time thing?
Like, I'd be fine if we include this in general, but, like, at build time, as long as we avoid adding, or if we remove the, like, framework, reference.
I think that would be satisfactory.
**Igor Kiselev** 32:46 The problem, there is no easy way for us to understand that the framework reference was added by us. So, I have a prototype code, but it is… very, very complex and error-prone script. So, I don't think it would be possible for us to remove if we added it unintentionally. At the same time, if customer So, it's easy to remove framework reference, but it is not easy to do it automatically. But, yeah, customers may add That small script to remove framework reference by hand, and it would solve workaround.
That specific problem.
**Piotr Kiełkowicz** 33:31 Congratulations.
**Chris Ventura** 33:32 Oh, go ahead.
**Piotr Kiełkowicz** 33:33 Sorry, Chris.
Exact questions bring me one… one idea. As a workaround, of course.
What if we disable manually as PNET core instrumentation? It will be also crashing, so we have the envar.
just disable, SPNET Core both metrics and, traces.
And… how it will be… how it will behave.
This will be crushing on the loading.
**Igor Kiselev** 34:03 No, the problem that… the problem… the current problem for a user is that we added framework reference, and once a user compiled his application, that framework reference would go to their runtime JSON.
**Piotr Kiełkowicz** 34:20 And it is filing on the executing application.
Not later.
**Igor Kiselev** 34:25 Yes, yes, it would be for… checked by .NET host.
So it would not even start.
**Zach Montoya** 34:38 Yeah, so my… my main goal is Can we get a workaround where the user ergonomics are minimal, like setting an MSBuild, property, or setting a… adding a target, or something very small.
**Igor Kiselev** 34:54 Yes.
**Zach Montoya** 34:55 Could then remove the reference.
**Igor Kiselev** 34:56 Yes, Ivika.
**Zach Montoya** 34:58 I want to achieve.
**Igor Kiselev** 34:59 Yes, we can… I could do it, through MSBuild script. I would remove framework reference, through our Augustin script. In… in our existing script, we would also do cleanup of framework reference if user, asked it this… Property or something like that.
Okay, let me try to do it, and… There's a question about, a minimum package.
It's still open, so we could use it.
Pull request to discuss it.
I… So, right now, I'm not intent to proceed anymore with that pull request, unless there would be a voice that… or we probably would like it.
**Chris Ventura** 35:48 Yeah, and I just keep coming back to… I feel like the… It's the ASP.NET Core instrumentation that's really pushing us down this road.
But I believe there's a path forward where that instrumentation package will no longer be necessary.
Even if it's a couple of years out.
So just trying to keep that in mind with the types of major changes that we make to support it.
**Zach Montoya** 36:23 Yeah. Good call out.
**Igor Kiselev** 36:30 I like… I personally like my modular approach, I like the… when a NuGet package, do not bring any additional files if it is not needed, but… At the same time, it's lots of work and probably not too much gain.
**Chris Ventura** 36:47 And, and actually, if… we… Let's talk about this NuGet package a little bit more. So, one of the reasons we created this NuGet package is to get the dependencies in alignment.
When our, what was it? Shared store approach, an additional depths approach, didn't work.
With the new approach for assembly loading?
How much of that is necessary with this NuGet package?
**Igor Kiselev** 37:26 I maybe not fully understand the question.
**Chris Ventura** 37:29 So, originally, we didn't have this NuGet package, we just had the zip.
file that you would download, which contained the additional depths folders and the shared store, folders.
Bye.
Go ahead.
**Igor Kiselev** 37:48 Okay, I got a question. So, I… okay, I still think that a NuGet package, solves a problem of, of dependence resolution in a most native way for .NET framework, and, it is… it has a Minimum price for what we are doing, because we don't need to have an assembly loader, so we not install anything, we limit potential vulnerability exposure for our customers, that we are not loading some files, sitting on this, and only files that are in the manifest, can be loaded. So… So, if, I think that NuGet package may be not very convenient for a user, because it breaks the promise that you have an application, and now, later, you can instrument it.
But it still fits, pretty nice in a picture zone. Okay, I can recompile my application.
I'm not against it. At the same time, I don't want to spend a lot of time on doing manual instrumentation, on doing some manual settings. I'm pretty fine with the features that auto-instrumentation gives me. So, it really sits pretty nice in the middle of the two approaches.
And how many customers will they have with NuGet package once we have a full work in Zip?
I don't know. At the same time, NuGet package is much more convenient, for example, for CI.
If I know that that application would always be instrumented, and I'd like to test it, it's much better that I have all my dependencies in one place and not switch from dependencies that I install through new packages config, through… package props file when I see all versions, and then I need to jump to some other environment specification and change which version of hotel I am using. So… I think… Despite it started as a way to work around an issue in a loader, it becomes bigger than that, and it may probably have some customers that are specifically interested in it.
It's only a guess of my feeling.
**Chris Ventura** 40:09 Right, so if the… if the NuGet package still exists, where my mind's going is how many of these dependencies do we need to have in the NuGet package itself going forward?
Like, is there a future where this NuGet package no longer requires referencing extra dependencies.
**Igor Kiselev** 40:38 The user dependency has to do instrumentation, so… The dependencies are not, should… so, that are dependencies that we… give alongside a zipper hive. So, while they have them in a zipper hive, we probably need them in some ways for NuGet packages, because I…
**Chris Ventura** 41:01 Right.
**Igor Kiselev** 41:02 This bytecode, we activate them, but implementations still need to be delivered.
**Chris Ventura** 41:08 Yeah, so I'm… what I'm saying is, what if the… Zip Archive and the NuGet package were more similar.
Because of the new dependency management that we have.
So that's the scenario that I'm thinking through. So, the NuGet package contains all of the same binaries that the zip Archive Games, comes with in the same structure.
**Igor Kiselev** 41:39 I don't like that approach, honestly, because it's not as a good, NuGet package should behave.
And, having a more modular, dependency, it's probably… Better prompt.
Nugget ecosystem point of view.
it's easier for customers who try to build a SPOM list and found what third-party dependencies and which version are we using. Right now, they install NuGet package, and they explicitly say, okay, I installed better version of that, Z, that, and that package. If we install only one package, and it includes everything, now they have a question, okay, how you get that file? Is that file the same version that we have in NuGet package, or have that file been patched specifically for hotel? Okay, we can compare SSHA and figure it out, but I, and it's still required, and we still pay, some price when we do our custom assembly loader. We do some tweaks, we, start jumping with, different assembly loading context, other things. I'm not saying that it's, It's… too bad, but if a customer in a position that he already installed a NuGet package, and he don't need to pay that price, why are we switching back to a solution when he will pay that price?
**Chris Ventura** 43:20 Yeah, it just… it feels like we're trying to find a solution that's somewhere between our normal auto instrumentation approach.
and the manual SDK approach.
**Igor Kiselev** 43:31 Yes, yes, Nugget… Nuggets currently seats in that.
**Chris Ventura** 43:36 Right, and I think… the… Java ecosystem has… is solving this problem a little bit differently. They have this auto-configure module.
that is used… you can use it with just the SDK-only approach, but you can… but it's also used within the OTel Java agent.
and… you can choose to either install the OTelJava agent.
Or, if you wanted more control, you can… just… instead of referencing the OTel Java agent, you referenced just the auto-configure module.
And then have a little bit more fine-grained control over the dependencies that get brought in.
**Igor Kiselev** 44:36 I probably need to look into it, because I haven't… I don't know how it is implemented in Java.
**Chris Ventura** 44:44 Yeah, I don't know the exact details either, I just know that they're separate things that you can register and use.
Yeah, I guess part of it is, I don't have a good sense for the end user needs here. So, how many end users really Want or need that slimmed-down dependency approach.
And how many end users simply don't care, they just want their auto instrumentation to work.
And I feel like the majority of our users that have gone to the… NuGet package route have done it because of dependency conflicts.
So, I… Yeah, I'm just trying to balance out the needs.
**Zach Montoya** 46:07 Yeah, that's something we can explore more, especially if we're thinking about major version.
So… What was the, what was the immediate outline we got from this?
Were you gonna… was it, adding a build target to try and remove the framework reference? That was, like, our short-term…
**Igor Kiselev** 46:33 Yes, okay, I think, yeah, for now, I would build… I would create an alternative pull request that would remove package, framework reference, based on condition, or if it would be short enough, and it probably would be, I would just command in… Ticket that you could remove framework reference with that code.
And… Add documentation, because, you know, there is not a… We could do… I'll tell… no, we couldn't alternate way up. We couldn't say that if it's installed by us or not. So, I think… So the problem is that, adding property or adding, just an instruction in, what customer need to do, it's pretty the same, because, okay, property, it's one line, removing it's probably three lines, so… Not a big gain.
From Aiden.
Property.
**Zach Montoya** 47:36 Okay.
Cool, yeah, we can do that, for kind of the short-term workaround, and then we can explore later on.
**Igor Kiselev** 47:44 I will try. I will try.
**Zach Montoya** 47:46 Okay. Great.
**Igor Kiselev** 47:50 Sorry, it takes so much time.
**Zach Montoya** 47:52 No, that's good, that's why we're all here, so this is a good time to have these discussions.
Alright, so, going back to this, we talked about that draft PR. Are there any other drafts that people want to discuss, or need, Need review or discussion on?
Alright, and the other two live ones, again, there's, doing assembly redirects for non-default app domains, and then adding a terminal op-amp, not sure if that one's made any progress.
I did look at this one. I'm… So, I'm not sure if other people have as well.
**Igor Kiselev** 48:37 Thank you a lot, Zach, for your review. I will do a pollution, and I will try to add a little bit more documentation. Mostly, it was a question about documentation.
**Zach Montoya** 48:49 Yep.
Alright, so with that, we have a couple new issues.
Alright, so there's one regarding Stack Exchange Redis.
Interesting. And then, some SQL client instrumentation package adjustments.
Let's see what this one…
**Piotr Kiełkowicz** 49:10 It is kind of… I need to test some changes in the… in the country repository with our… with our auto instrumentation, and it reveals that some other changes requires Ugh.
reflection adjustment, so when… when prepared, I just drop it here to not forget about this.
**Zach Montoya** 49:36 Okay.
Sounds good. Stack Exchange Redis, let's see, I'm not sure if anyone's… I've been able to review this.
**Piotr Kiełkowicz** 49:53 I suppose it should go to country repository.
**Zach Montoya** 49:56 Yeah, that's what I'm thinking.
**Chris Ventura** 50:01 Although, I thought there was something in there that referenced something that we were doing.
to get things loaded. They were referencing our lifetime manager?
**Zach Montoya** 50:14 Boop.
**Chris Ventura** 50:15 As one of the problems.
**Zach Montoya** 50:17 Lifetime…
**Chris Ventura** 50:18 Or Lifespan Manager.
**Zach Montoya** 50:20 Oh.
Lifespan.
Okay, it's checked by Lifespan Manager Track.
Yeah, that sounds like that would be… Something in our domain…
**Chris Ventura** 50:33 Right.
**Zach Montoya** 50:34 by Spam Manager… oh, we track it, okay, but, Might be when we register that.
Yeah, so we do track it here.
Mostly for disposing Spilling things, There's no mechanism to dispose it when the underlying connection multiple is closed or garbage collected.
Okay.
Interesting. I mean, this might still be an issue with the contrib… Rather than us, so… When they create this… observer, I guess.
Just seems long-lived.
Oh, it gets disposed, dispose.
Stop, handle, drink, thread… flush.
**Piotr Kiełkowicz** 51:46 There is a test that we wrongly disposed this on the phone.
**Zach Montoya** 51:50 Yeah.
**Piotr Kiełkowicz** 51:51 sites, yeah.
**Zach Montoya** 51:52 Yeah, okay, so that, yeah, that might be us. Okay.
So yeah, this, this is… oh, hey, root cause analysis. So… Yeah, we might… yeah, we'll just take a look at this. I don't know if we need to discuss this right now, but we can each… we can review this and… figure out next steps.
It's looking nice.
**Piotr Kiełkowicz** 52:10 Maybe… maybe we can ask if the… A reporter would like to kind of provide fix also for us.
**Zach Montoya** 52:20 Oh, yeah.
Cool.
Alright, otherwise, this… Milestone… 16, maybe?
Probably. Yeah, let's do that for now. Okay. Cool, cool… Alright.
No discussions… No other issues for this milestone 15.
And I don't think there's really any other changes… On our board.
Do we need…
**Chris Ventura** 53:34 We need to discuss the, change that we rolled back?
**Zach Montoya** 53:39 Oh, that's good.
**Chris Ventura** 53:39 At all.
**Zach Montoya** 53:42 Yes, I did see that one. Okay. Oh, yeah, I think that one… So that was this one.
**Igor Kiselev** 53:49 Yes, sir.
**Zach Montoya** 53:49 When starting up an app domain, so we reverted… Oh, let's just go back. It hurts this.
This one.
**Igor Kiselev** 54:02 Whoa.
Who's, probably I… should… we should not, approve original change at all before a test have been done and demonstrate that it has been done, but here, when I have done a review, I reviewed only that it looks correct, and to check the function, I… despite I feel something uncomfortable, I worked with AI, and it also Says that, yes, it would be cold.
And then we said that, we could do a code coverage in a separate pull request, so… We effectively merge substances at least not Having any issues, but not solving a problem.
**Zach Montoya** 55:02 Yeah, this seems like, yeah, something that might have warranted just a separate regression test.
At the time of Merge.
**Chris Ventura** 55:13 Yeah, at the same time, though, it looks like you've done some further analysis and… Have provided some additional… guidance on… Possible solutions.
**Igor Kiselev** 55:27 Yes, yes. It looks like the original, contributors still would like to continue, so I'm, right now, just… Look at what… what would come from it.
**Zach Montoya** 55:44 Okay, cool, well… Yep, things happen like that. Looks like we have a path forward, though.
Alright, yeah, let's just… yeah, this issue will attract the, you know… Proper resolution, so… Yep, at least, you know, this, this revert, it's very easy for us to revert that, but, you know, we can, try to be a little more stricter on that.
Merging the PRs.
So yeah, this will track the continued resolution of that problem.
Alright, so I don't believe we have anything else to discuss. Is there anything else that you guys wanted to bring up?
**Igor Kiselev** 56:33 Just a small, update, I, as I promised, I put, all my research about iSpanet, core hosting assemblies, and, what I think are the proper way to solve.
But probably we need to wait until Raj would review it. It mostly would be Bon.
It's 44881, 4881.
**Zach Montoya** 57:06 4881… Oh.
**Igor Kiselev** 57:08 Issue. Issue.
**Zach Montoya** 57:09 Bush you.
**Igor Kiselev** 57:11 Ugh.
Issues.
**Zach Montoya** 57:15 Thank you.
**Igor Kiselev** 57:17 Ray.
**Zach Montoya** 57:18 That's what I get for trying to hard-code things. Alright.
I mistaken.
**Igor Kiselev** 57:23 4… 4881.
**Zach Montoya** 57:26 Oh, okay.
**Igor Kiselev** 57:31 Great.
**Zach Montoya** 57:31 Alright, we got there.
**Igor Kiselev** 57:32 Great. So, yep.
My last comment is my detailed analysis and my suggestion, what we can do, and what we should do, or should not do.
So… There's a resource, so… probably it should be now on Raj, as… there is nothing that I can do anymore until it would be confirmed by other parties.
**Zach Montoya** 58:02 Okay.
Alright, yeah, we can follow up on this offline.
Yeah, I don't wanna… I'll take up more time. We're almost at the hour, so that was a pretty… pretty lengthy discussion we had today.
Yeah, is there anything else?
I guess what I'd bring up?
All right, maybe we can just call it here. Yeah, thanks everyone for, for the good discussion.
And, see you next time.
Bye.
**Mateusz Łach** 58:48 YouTube.
