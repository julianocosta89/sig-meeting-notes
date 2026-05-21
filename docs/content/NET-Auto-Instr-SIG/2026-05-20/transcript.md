SIG: .NET Auto-Instr SIG
Date: 2026-05-20
Duration: 39 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 04:58 Hey, guys.
**Zach Montoya** 05:07 Hello.
**Piotr Kiełkowicz** 05:15 Do you want to drive a meeting today, or should I do it?
**Zach Montoya** 05:22 No, no strong interest for me.
**Piotr Kiełkowicz** 05:28 I can grab this, in this case.
I hope you can see my screen. Do you know if Rash will be able to join, or… Breeze?
**Zach Montoya** 05:50 No idea.
Also, looks like we got a Zoom chat from the notetaker, if we want to pause or stop the recording.
I don't know who… I guess it does say who invited the notetaker into healing.
**Piotr Kiełkowicz** 06:21 I think there is a possibility, too.
It's to draw.
I'm not… do not remember, And it's gone.
I think I need to switch to the filter result peers, because we have a lot of non-dependables.
So, from the top, the Panda boards will be immigrated to renovate. It will allow us to Auto-update other dependencies, because for now it is kind of not very well working.
with… with current structure, and I hope Renovate will be… will be better.
infrastructure stuff.
We have also requests from Martin to include GitHub Actions work for… CodeQL for the GitHub Actions.
I think it will be fine to include it. It just needs to pass.
the branch… And a lot of in-progress stuff.
And I will open tomorrow.
It is already revealed. Igor, any comments here?
You're on mute, Igor.
**Igor Kiselev** 08:45 So I'm trying to understand.
All right.
It's, I believe it is… I believe it's really… Milch?
Was there a.
**Piotr Kiełkowicz** 09:00 Okay.
**Igor Kiselev** 09:00 Anything else we're thinking?
**Piotr Kiełkowicz** 09:02 it is kind of hardening the… our GitHub configuration, yes?
**Igor Kiselev** 09:08 Yes, it's almost hard to move, we have configuration.
So the difference, there was a re… It was a follow-up for my previous pull request, where, it was advised instead of using, string, substitution, interpolated string, or use an environment variable, because it would be properly escaped by shell.
And… Less chance that if we use some environment variable that, derived from pull request name or something like that, some malicious activity would be able to do something bad.
So I updated it in, in most places where my pull request used it. I updated it in some places where it was already existing pattern in repository also, but I have not updated it everywhere in repository, where update would require full rewrite and increase the size of, of, code that would be required.
That describes the same thing, and at the same time, we use a state environment variable that Clearly not derived from any pool requested data.
**Piotr Kiełkowicz** 10:23 Cool.
Matt prepared the request to stop promoting resource attributes from app settings to NVARS. I'm not sure if you were able to discuss it last week.
**Zach Montoya** 10:47 No, we didn't, discuss this one.
**Piotr Kiełkowicz** 10:55 I think it is the most important about… the documentation itself.
**Zach Montoya** 11:17 Yeah, so it seems like we… This was… this promotion happened so that we could just, have the SDK inherit that more easily, right?
**Igor Kiselev** 11:29 When we do it without a major version, it's background.
Compatibility change for a setting that Applied through.
Webcam… so webcam, I think, may be a way for delivery of some of our customers.
**Piotr Kiełkowicz** 12:00 Okay, I need to read it, to be honest.
I don't have time to verify this.
And… F sticker… Is it still in progress, or do you want us to… to review it right now?
**efshaikh** 12:22 No, it's still in progress, because the review feedback said that we can refactor it, and I agree with that.
So… That part will be done, and then I'll add some integration tests.
Before we actually remove it.
**Piotr Kiełkowicz** 12:38 So, I'm converting to draft for now, please.
**efshaikh** 12:42 Yes.
**Piotr Kiełkowicz** 12:42 Just reopen when you are ready to… to the final review.
**efshaikh** 12:46 Sure.
I can rewrite the… I can undo the draft status, right, once I publish, or do I…
**Piotr Kiełkowicz** 12:59 Yes, sure, you should have permission to click it, ready to review, or something like this.
**efshaikh** 13:06 Alright.
**Piotr Kiełkowicz** 13:07 I'm not sure where… yes, here, on the bottom of the page.
Another… PRs you would like to discuss?
**Igor Kiselev** 13:21 There are two MyDraft pull requests, instrumentation is trampline, and the same about NuGet, about a NuGet, we already discussed, a NuGet Split. A NuGet split we already discussed some time back, but have not, come to any conclusion if we… it should be delayed until next measure, if it should not be implemented at all, and lastly, I reviewed all existing issues. I found some issues that expresses or tell that we should… that at some point in in the past, we plan to do explicitly what that pull request is doing, so… Once again, we need some decision from SIG, on both original issue and pull request, if it should be closed as not required, or if it should be, hold until next, measure, or it should be merged as… Continue, and in that case, go out of draft and make it.
workable.
**Piotr Kiełkowicz** 14:31 I think the major bump is required.
Because otherwise, the Nugget end users will need to kind of switch the configuration, and SPNet Core is kind of… Main part where the end users are using auto-instrumentation, in my opinion.
**Igor Kiselev** 14:52 not configuration, but a list of reference NuGet packages. They would need to add additional NuGet packages, and without it, they would see a build error.
**Piotr Kiełkowicz** 15:02 Yes, exactly. So… Yep.
In this term, it is kind of breaking chase, in my opinion.
**Igor Kiselev** 15:14 And the question, if we did it, or not. And it's better to answer not even in that pull request, but in an issue that I linked.
Below.
**Piotr Kiełkowicz** 15:28 I would say we can put create200 milestone release, and revisitings.
I'm not sure.
**Igor Kiselev** 15:41 which means… in that case, it means that I still should move it out of draft and complete a work.
And we are targeting it to be done in 2.0, because we may need 2.0 at any point in time, we will get something that is critical enough to do a 2.0, and at the same time, we should have ever since that we target to retrady. So, that's why I'm asking it right now, are we… planning it for 2.0, in that case, yeah, we… I would update it, and I would maintain it in a ready… lead, or… Not now.
**Piotr Kiełkowicz** 16:23 I think we need to check with at least Java team how they are making the major releases.
For the auto-instrumentation. I'm not sure what are the expectations of maintaining two versions.
Similar thing, it's…
**Chris Ventura** 16:45 I'm also not sure.
**Piotr Kiełkowicz** 16:46 there were…
**Chris Ventura** 16:47 If, if there's enough… Critical features to push for a 2.0 release as well.
If this is the only thing for a 2.0 release.
I don't know if that alone justifies it.
**Igor Kiselev** 17:03 I'm not suggesting to do a 2.0 release, what I'm trying to say is that we may have multiple features that could not be merged in a current release, but could be done in a master. So, it means that all… in 2.0, it means that all that features that we target to include in 2.0 should be always in a already in a reviewed state, so that as soon as we decide that it's now a time to do 2.0 release, we merge all set of that.
**Chris Ventura** 17:37 Yeah, so that's the argument that I'm making. I don't know how many features we have for a 2.0 release to have any sort of estimate on when we would do such a release, which would mean we'd have a very long-running branch that we'd have to keep synced up and updated.
Which can be a big maintenance cost.
**Piotr Kiełkowicz** 18:02 Agree with this.
Maybe you could make an exercise and create milestone 2.0.
Or, kind of, needs major bump.
label, whatever.
You want, and put all potential features we need.
**Igor Kiselev** 18:23 Because what we just discussed about a config change, removing it from web config, it's a feature that potentially would be even more devastating for our end users, because it have no way to break the they built So… they update, and nothing… and nothing works after an update. And… That feature is important because it is a sec… Up to some level, it's a fix of security issues, that one application may leak a secret in another application.
in IIS.
That's why I'm talking about 2.0, that it may be sooner rather than later.
**Piotr Kiełkowicz** 19:14 Very cute.
**Zach Montoya** 19:15 that security angle?
**Igor Kiselev** 19:19 Yeah, I think it's, it was made… it mentioned, at least as I understand why we are, working on it, it's because of a security angle, that once we use web config for one application, so one application step in WebConfig, a keys, some keys.
And we read that case in a common open telemetry scope, and then another application can read it.
Maybe I'm wrong.
But my, my main… my main reason… as I read the ticket, it's about a cross-pollination between, different IS applications.
Including cross-pollination of a secret.
**Zach Montoya** 20:12 Hmm, I'm not familiar with this.
**Piotr Kiełkowicz** 20:16 Even if I can agree, our recommendation is to execute I'm gonna be… One application per pool.
If I remember correctly.
our documentation.
**Igor Kiselev** 20:32 our recommendation. If it's, if we would prevent a usage of it, we don't need that feature at all, because we already… Have one application per.
So, in that case, everything works even with web config. But in IA… but with, out-of-process instrumentation, or with, okay, out-of-process may not be an issue, but with .NET Framework.
It was… Pretty often a configuration when multiple applications sits in the same.
**Chris Ventura** 21:13 But at this point, we're talking about a separate issue from this one here.
**Igor Kiselev** 21:19 Yes, we are talking about them together, because most of them may require a 2.0 release.
And another one, it's potentially a security… implication.
**Piotr Kiełkowicz** 21:35 Do you mean this one? Yes. Yes.
**Igor Kiselev** 21:38 I mean, this one.
**Chris Ventura** 21:54 So the argument here is that… Because we're loaded into the shared domain.
If we're reading from these app settings, it can leak.
App Settings.
Between app domains?
**Igor Kiselev** 22:11 Between… yes, between all domains, yep.
I have not looked in detail if it's really required to play 0, but…
**Chris Ventura** 22:41 Yeah, I guess we need to answer the question of.
Will… will a 2.0 release be required? And then that'll…
**Igor Kiselev** 22:49 Yes.
**Chris Ventura** 22:52 That'll determine how we approach it. Approach the other ticket, whether we want to have a branch ready for it or not.
**Piotr Kiełkowicz** 23:02 I agree. If we do not have plan to make a major bump soon, I would just close your PR, to be honest, and… Mark has, to owe my stone without, kind of, due date.
**Igor Kiselev** 23:17 And then we will mark it on an issue itself, and that's why we will have a list of issues that you plan to do in 2.0. Great.
**Piotr Kiełkowicz** 23:26 Yes, exactly.
**Igor Kiselev** 23:37 And instrumentation is tramplain is just another… again, a reminder that I need a feedback despite it's a draft. Not on a… I need, not a review, but I need a feedback if it's something that could be Workable for us, and could be mergable or not.
Cool.
I haven't done a lot of whiteboard things, and I have not done a full review, because it would require a lot of efforts, even for me, and I don't want to spend too much effort if we not have any plans to do some, feature like that.
**Chris Ventura** 24:17 And just to repeat the concerns from the last time we discussed it, with this trampoline feature, it causes enough of a deviation between the upstream native code that it'll become more difficult to sync those changes in the future.
**Igor Kiselev** 24:37 It's probably the main reason. And it's just a pretty complex, pretty… Big, fisher soul.
if it's worth effort or not, so it… but it may improve a memory layout, for some .NET framework. But again, you just mentioned that we do not recommend to have more than one, application per application pool.
If we said that we customer should never use more than one application per, or perdomain, per, per podium. If we said that we should, they should never need, have more than one application per subdomain, it would be very, very edge case, and that we should probably not needed.
If we would like to still support multiple applications per pool, that feature, trade-off Memory usage into a little bit higher, cost of, instrumentation call.
So, in that case, it… Pretty useful.
**Piotr Kiełkowicz** 25:42 I'm not saying that it is a wrong idea, but I would go with the upstream sync first.
And then try to implement anything kind of breaking.
Or making this upstream sync harder.
**Igor Kiselev** 26:02 So, is our suggestion that we should suggest that feature for Datadoc and implement it there first?
And it would be… depends on Datadoc, Wish, or…
**Piotr Kiełkowicz** 26:12 I… I'm not… I'm not telling this that Datadoc should implement this stuff, but Datadoc has already tons of features or fixes in the last, kind of, 3 or 4 years.
And we should take it if Datadoc agrees on this, and then implement this kind of big breaking feature.
And stop making the data dock sync in the future.
**Zach Montoya** 26:43 Yeah, I'm happy to try and, pull down some of the changes and bring them to the profiler here.
But yeah, I think that would be the best way to go if we do decide to do the trampoline.
I know that there are some fixes for sure.
an upstream Datadog, but… I don't know how much it actually gets, changed?
Like, in… mostly, a lot of the changes that go and Datadog are now just in the managed side.
Cause the underlying part is very stable.
So… There may not be, like, if we do a final, like, update.
For, like, what we have today.
Maybe we won't have to track too many upstream changes afterwards.
**Chris Ventura** 27:40 Yeah, it just makes me wonder if, Your customers are running into the same type of problem with the… Multiple applications in the same app pool.
Situation that this is trying to deal with, because… The way things get loaded, they're similar… But…
**Zach Montoya** 28:08 Sir… The… I mean, the main design decision over, like, in the Datadog repo is to not have any external, assembly references outside of what's shipped in the framework, which is very limiting, which means even for, like.NET Framework, it means not referencing SystemNet HTTP.
Since there can be different versions loaded there of, either inbox or out of box. But with that constraint, it means that, the different Datadog assemblies can be loaded, domain neutral, and there's no… Sort of… It can be shared, basically, if it, whenever it's used.
So there's not a lot of issues there. Even, like, with the system diagnostic source, there's no hard assembly reference out of there, so this, like, trampoline approach isn't exactly needed.
So that may not be something that Datadog would take, but, like, we haven't really needed it, like, advanced, like, mechanisms for trying to… Resolve with some of the references.
So that's why that's kind of stayed the same.
**Igor Kiselev** 29:24 It's about a designer V.
That if you don't have a reference to external assemblies, that is not needed every single work, perfect, even with much simpler approach.
And it's not needed on .NET, it's needed only on .NET Framework, also.
**Zach Montoya** 29:50 Yeah, for .NET, it's… for .NET Framework, it's extremely important, especially for the IIS. Yeah, the only… thing, like, we still implement that for .NET and .NET Core-based apps, simply for, like, managing dependencies, Theoretically, we could do that and rely on, like, activity and whatnot and bring our own, but we then don't even, bring our own, like.
diagnostic source, DLL. We just rely on what the user has, so it's all through, like, the, reflection-based, like, duct typing mechanisms in there.
**Piotr Kiełkowicz** 30:50 Any other comments today for this one?
Nope.
**Igor Kiselev** 31:18 That is, we didn't… we talked about it in a previous sequence, the… I have some concerns that our assembly load may not work correctly with single file deployment. I don't think that anybody have validated it. We talked about it with Alexei already, and Alexi plans to look and trade Soon enough, let's say, unless he would, of some time.
**Piotr Kiełkowicz** 31:44 So, 116 for now.
**Igor Kiselev** 31:49 I'm not sure if… depends on when 1.16 would be, but, it… Probably before end of summer, we would… Solve it, if we have any issues.
**Piotr Kiełkowicz** 32:02 So, I'm putting it there, but I would not treat it as a blocker for the release.
Alexei.
Hmm.
Got her, yeah, later.
**Igor Kiselev** 32:24 I don't think that Alexei is, OpenTelemetry member, and to have it in here, we need to have two sponsors for him, and not affiliated through a company.
**Piotr Kiełkowicz** 32:40 I can be in one of them, but…
**Chris Ventura** 32:43 Yeah, I can be a sponsor, too.
**Zach Montoya** 32:47 Yep.
**Piotr Kiełkowicz** 32:48 Thank you.
So, Alexei, you know how to proceed with, with the request?
**Alexey Pukhov** 32:59 Oh, yeah. Yeah, I know.
**Piotr Kiełkowicz** 33:01 On the community side, great.
And we have kind of good candidates for the two-hour version.
Igor, I will put it… I will keep it, unsigned. I hope you put everything into Tua version.
**Igor Kiselev** 33:33 Okay.
**Piotr Kiełkowicz** 33:35 Thanks.
And stock exchange thread is 3.6.
It is working on .NET, but during the batteries, I find out that .NET Framework is not supported.
We have had exactly the same problem with MongoDB, and decided to follow the bytecode instrumentation.
If you want to support both versions here, I do not see any better options, to be honest.
**Igor Kiselev** 34:09 V… Okay, so it's… so there are potential other options. If we… okay.
First question. If instrumentation is the same, instrumentation library is the same for 2.0 and 3.0, I'm not sure about it. But if, instrumentation libraries still target 2.0, And it can work with 3.0. In that case, first customer already could use it if he provides proper assembly binding. Second thing, we could extend our, assembly loader and assembly version patcher, to, to resolve that conflict on, to substitute that assembly binding for a customer if there is, not any. So, this current infrastructure that I implemented in .NET framework, it's possible, so… The main… the main questionnaire would be if… we could use, if instrumentation library would still continue to reference version 2.0, and that 2.0 could work with both 2 and 3. If it's not possible, then assembly patching approach would not work, and would require probably… Bytecodes instrumentation to dynamically load proper instrumentation library.
of flows.
**Piotr Kiełkowicz** 35:44 For now, it is working both for 2 and 3.
**Igor Kiselev** 35:48 In that case, it's possible to do it without bytecode… without bytecode instrumentation, but with our… assemble a partial, but it would require a lot of thoughts and a lot of planning how properly to do it. But even now, in that case.
Customer provides assembly binder, everything works.
**Piotr Kiełkowicz** 36:21 Is it true, Igor, what I thought?
Rod? Great.
**Igor Kiselev** 36:25 Okay, I have not tested it myself, but everything… what I know said that, yes, if customer would provide assembly button, it will work. I could… what we can do, we could, create a test case parade.
And in test case, create an assembly binding and make sure that it works with assembler binding.
**Piotr Kiełkowicz** 36:47 I'm putting to 116.
Because we should handle it.
if, Redis 3 or will be in the saved version. Otherwise, we can postpone.
And I think that's all precious.
**Igor Kiselev** 37:10 If we should… if we should do something more than provide a background, then bytecode instrumentation would be a faster approach.
It may be not the only thing, and we could, in parallel, start looking into how we could use, assembly binding redirection to solve both MongoDB and Redis, but we would not be able to deliver a bigger solution through assembly binding soon enough to make it in 116.
**Piotr Kiełkowicz** 37:46 Okay.
We do not have any open discussions. Milestone 6… Ding… It's also correctly coming by the project board.
And I'm not sure if you want to… Update the project voice itself.
Do you have any other topics?
Nope.
Thank you.
**efshaikh** 38:58 Thank you.
**Zach Montoya** 39:00 Nice.
**Igor Kiselev** 39:00 Okay.
**Zach Montoya** 39:00 See you guys.
**Alexey Pukhov** 39:02 Thank you.
