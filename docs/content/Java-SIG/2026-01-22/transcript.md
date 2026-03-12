SIG: Java SIG
Date: 2026-01-22
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 00:00:49 Hello!
John Watson 00:00:52 Good afternoon.
Or morning.
Trask Stalnaker 00:02:05 Hey folks, alright. Oh, we got a crowd, let's go.
Sylvain and Jack.
Sylvain Juge (Elastic) 00:02:15 Yes, so this is about, indie migration.
And so we discussed a bit on our side, so we have it enabled by default in our own distribution.
But we don't have that much adoption so far, because people are a bit slow to update.
But we haven't had any major issue about it. And so, after discussing this a bit internally, we think it could be a good time to switch the default to true by default. So, maybe because it's the easiest option, like, it's one line, easy to revert.
And an alternative that I discussed a bit previously was to say, let's gradually migrate things over time, like, one into cementation at a time. And while this would be the end approach.
And I think it would be really hard to revert.
And so, yeah.
We'd like to gather your thoughts on this, and how much do you trust this choice?
Jack Shirazi 00:03:20 But that is also worth mentioning that, Our old agent, which is in production, has been for many years, uses Invoke Dynamic and has… hundreds of thousands or possibly millions of JVMs running like that, so… We don't think there's any problem with Invoke Dynamic.
Trask Stalnaker 00:03:46 So flipping the default… Has no effect on extensions.
Correct.
Sylvain Juge (Elastic) 00:03:58 Yes.
Trask Stalnaker 00:04:07 And so, okay, and so the thought was… We flipped the default, we… at some point, we could deprecate… Is there anything we want to deprecate?
long-term, like, for… I forget how we've split those APIs up.
Jack Shirazi 00:04:36 I mean, the extensions are going to be runtime mapped into it, so that can be indefinite.
Because that doesn't affect shading of the agent, because they're in a separate class order anyway.
So the reason we want to flip this is so we can get rid of shading in the agent.
And… I don't think that it's… I don't think there's anything else that…
Sylvain Juge (Elastic) 00:05:04 And we now have, like, integration tests that replicate the… what the extensions do, so any, like, advice, transformation that is currently being applied is still effective with extensions.
Trask Stalnaker 00:05:21 And are these… are we still, Mapping these at runtime, to the invoke dynamic, some of the instrumentations.
Sylvain Juge (Elastic) 00:05:35 Yes, so the… so if we flip this by default, it means most instrumentations will, be modified, but we just switch the inline pulse into the annotations of the advice code. And this is the only modification that is being done.
And, we can do this, and… because all internal instrumentation is now, like, indie-ready, so the indie-ready, just disabled the transformation, for example, for a local advice method, or local advice variables.
And other, kind of, transformations that are still available for extensions, so… It doesn't change that. And so, once we flip the default, we have some feedback, maybe in a few months, about if there is any major issue being reported.
And so, once we know and we have feedback on the lack of issue with this, we can start to migrate those instrumentation to make them only run into indie mode. And once all of them have been are running in indie mode, then we can, like, remove shading, at least for internal instrumentation.
Trask Stalnaker 00:06:54 Laurie, any… any concerns?
with… Moving forward with this?
Lauri 00:07:05 Do I understand, right, that you want to flip the switch that starts rewriting the devices automatically?
Sylvain Juge (Elastic) 00:07:17 No, in fact, this… yeah. So, by default, the switch, makes the… so we have an is in the module, method, and, the way this is currently implemented, so unless you have a module that explicitly overwrites, the method, the value of this, Of the scatter. It comes from, configuration. So, this is a ver- oh, we have been testing this for, for months now.
And so, if we flip the default on this, it means, by default, all instrumentations module will run using Indy.
Lauri 00:07:57 But why do you think it doesn't affect extensions?
Sylvain Juge (Elastic) 00:08:02 I think it still affects extensions, but, like, in a transparent way. So, it still applies to extensions.
Lauri 00:08:11 Well, but what if somebody has an extension where the automatic rewriting doesn't work?
Would we… wouldn't we just be breaking their stuff?
Sylvain Juge (Elastic) 00:08:22 In this case, yes.
So, do you think, in this case, we should, like, exclude those extensions explicitly? Maybe by asserting on the class loader?
Lauri 00:08:31 Well, I think whatever we do, we should avoid breaking up user applications.
You know, we kind of have this stability story going on.
Where we kind of try to, like, tell to the users that we don't break their stuff randomly.
Trask Stalnaker 00:08:50 If we could exclude extensions until the major version bump.
Sylvain Juge (Elastic) 00:08:56 Thought would be…
Trask Stalnaker 00:08:57 That would be ideal.
Lauri 00:09:03 I guess there is, like, a possibility that, Users could write an extension that depends on, one of our extensions, something like Nettear.
But perhaps that could be ignored.
Sylvain Juge (Elastic) 00:09:24 So, if we can exclude extensions, do you think it should be safe for internal instrumentation?
Jack Shirazi 00:09:31 We just want to change it so that… because we do know when we're loading an instrumentation that's an extension, so we just want to change it so that in those cases.
Indy is not false.
Lauri 00:09:44 Well, another thing is that, Also, custom distributions might include extensions, like, might include their instrumentations that are not yet converted to India.
And distinguishing those from our instrumentations could be a bit tricky.
Sylvain Juge (Elastic) 00:10:08 Yes.
Lauri 00:10:09 They're not, like…
Sylvain Juge (Elastic) 00:10:10 And in this case, is there any distribution that is not open source, where we could not contribute this?
Lauri 00:10:20 Well, the question is, like, do you want to contribute to, I don't know, some Alibaba custom distribution?
Jack Shirazi 00:10:28 I mean, we just… There you go.
Trask Stalnaker 00:10:32 Go ahead.
I'm a little less… I mean, it's definitely worth considering the distributions, but I… I'm a little… like, the extensions are the more important thing not to break, Until the major.
Jason Plumb 00:10:50 We tell our instrumentations by package, right?
Lauri 00:10:53 Not possible. Well, I think it's possible to turn this on, but, it just… it requires some thought, like, We should be… We shouldn't, like, break too much of the user's things. And if we do accidentally break it, we probably should give them some sort of way back.
Trask Stalnaker 00:11:19 Well, it seems like it's a… the way back is… Easy if we're just flipping the default.
Lauri 00:11:27 Yeah, I think it would be nice if we would, like, finally figure out how we are going to proceed with this, like, how are we going to… Like, are we going to… Give some sort of compatibility with old inline extensions, and… And how are we going to do this?
How are we going to distinguish, like, the extensions that can work with Indy from the others?
Sylvain Juge (Elastic) 00:11:56 Yeah, to me, I think it would be mostly, like, making these… is in the module, like, return either true or false.
Lauri 00:12:05 Well, the eC module is a horrible name for a method, like, yeah. First thing, like, it has to be renamed somehow, or…
Jack Shirazi 00:12:15 But isn't… isn't it just… if it's… if it's in… if it's not using the agent class loader?
If it's using its own class loader, then… It… it can… it can retain faults, and… and then if it's the agent class loader, it's true.
Lauri 00:12:31 Well, but in custom distributions, the instrumentations will also be in agent class loader.
Jack Shirazi 00:12:37 So in custom distributions, we just put it into the release notes what's happening.
Lauri 00:12:47 Well, I think it can be done, but it requires some thought, I think.
Trask Stalnaker 00:12:52 What about, the suggestion to detect by package name and apply it to all I.O, OpenTelemetry, instrumentation.
Java agent packages.
Lauri 00:13:09 I think that's a… that's a valid option, like, that could be considered.
There is also an option to, like, Use some sort of configuration, like, that the… Custom distributions can override.
And opt out from this new behavior.
Sylvain Juge (Elastic) 00:13:34 No.
Lauri 00:13:36 Well, basically, we assume that the custom distribution authors, like, Are capable of testing their own extensions, and and following our release notes.
Sylvain Juge (Elastic) 00:13:49 And so, in this case, do you think a very, like, a very long option of… with a list of, instrumentation names that, Are using this new behavior would be fine.
Jack Shirazi 00:14:05 If we're going by talking…
Lauri 00:14:07 Maybe that's not ideal, because, like, Nobody would want to maintain that list.
Sylvain Juge (Elastic) 00:14:12 Yes.
Jack Shirazi 00:14:14 If we're going by package name, then it's pretty straightforward, right? So that seems like a simple… Yeah. So… and then… and then you've got the… the indie flag that you can just flip back.
So… Customs distributions can do that. Extensions can do that.
That's a really easy… fallback.
Failover.
GZ Gregor Zeitlinger 00:14:40 What about if we delay this switch until 3-0? I mean, this is only 3 months out, according to Trask's planning, and then we would avoid this, Problem altogether.
Lauri 00:15:00 The thing is that, this India extension stuff.
It still requires some work.
for the free O. So if we don't do anything, then the free O isn't going to happen in 3 months, or it's not going to include the indie stuff.
GZ Gregor Zeitlinger 00:15:18 But we have more liberty, to make breaking changes.
Lauri 00:15:25 Well.
Trask Stalnaker 00:15:25 Yeah.
Lauri 00:15:26 Do we want to break everything?
Jack Shirazi 00:15:29 This shouldn't be a breaking change, that's…
Trask Stalnaker 00:15:35 So, I mean, I like the, trying to do what we can, Pre-3-0?
And… I think, additionally, we should probably somehow… officially… Deprecate… Inline, like.
Say that, you know, hey, we have a… because we usually have, like, a deprecation Deprecate first, remove later.
And that would be, like, official notice to distros that, hey, You should… Start migrating to this new thing.
I think it's good… the timing is good for it when we also Migrate, change all of our internal ones to it.
Because that's like, hey, we have this solid migration path, we've done it.
for all of our instrumentations. Now, here's some window of time for you to do it.
And then that would give us… leeway, I think, in 3.0 to, like, if we want to… Force that upon people.
Sylvain Juge (Elastic) 00:16:59 And so, in this case, do you think it's fine to, like, mention something defecated without First, providing a migration pass, and then at 3 total time, provide this.
Jack Shirazi 00:17:13 We have a migration policy, so… It's all, documented.
Trask Stalnaker 00:17:23 Yeah, I thought we had a… I thought the migration path for distros and extensions, they can already… opt-in, or maybe we tell… yeah, I'm not sure, but yeah, we would… when we deprecate, we want to be able to tell people, point people to the new guidance.
Sylvain Juge (Elastic) 00:17:45 Okay. Whatever that is.
Trask Stalnaker 00:18:01 So, Laura… Yeah, go ahead.
Jack Shirazi 00:18:03 Yeah, sorry, Sam is the plan.
We deprecate, which is, just an announcement, right, in the release notes, point to the documentation for that, and then, Change the flag only for, extensions based on, the package name.
Trask Stalnaker 00:18:31 Yeah, could possibly emit a warning, log, For people who are… you… to mention the deprecation, if people are using that… I don't know what other folks… think about… that warning showing up in distros, that can… If users can… Not like that sometimes.
GZ Gregor Zeitlinger 00:19:04 I wouldn't do it. It's probably causing more support issue for distro maintainers.
Trask Stalnaker 00:19:12 So just release notes.
GZ Gregor Zeitlinger 00:19:14 Nope.
Lauri 00:19:17 Well, another option how we could, I guess, possibly do it… Would be to, like, maybe change the muzzle generation somehow.
So that, Or, like, something in the instrumentation module that would say that, like, this module wants to be… wants to use the indie way.
So, if you have, like, modules compiled, like this new model, let's say, that generates it with, like, INDI compatible, then we would, like, immediately know that, okay, these are the Indy modules.
And, for others, we know that these are the non-NDI modules, And, the instrumentations that have been converted would be work as indie modules, and the others would work as they currently work.
Well, it doesn't actually have to be muzzle that's changed, it could be anything, like… For extensions, it could, like, I don't know, be a manifest attribute.
Sylvain Juge (Elastic) 00:20:33 So in this case, it would be, like, relying on the tooling. So, for example, any extension to make it compatible, you would just update, muzzle or tooling dependency, and then rebuild and repackage it.
Lauri 00:20:47 Actually, I don't know, like, whether, like, the muzzle would be the best option, or something else.
Jack Shirazi 00:20:52 Isn't that…
Lauri 00:20:53 That's something that needs to be figured out.
Jack Shirazi 00:20:55 Isn't that just the IsIndy Ready?
Sylvan?
Lauri 00:21:01 Well, it sort of is, but the question is, Do you want to have, Do you want to implement the method to say that this is the indie module?
Like, It would mean that, like, although the old way is deprecated, it would still be, like, the default way.
Because, like, the default value of this would be, like, false.
I hope you get what I meant.
Sylvain Juge (Elastic) 00:21:33 Yeah, or in this case, we would maybe, like, change the default of, like, is in the ready method, so instead of returning false, we make it return to.
Lauri 00:21:44 Well, then you would break all the existing implementations, which.
Trask Stalnaker 00:21:48 Can't blame.
Lauri 00:21:51 Yeah, like, you could, like, instead of, Implementing instrumentation module, you could have, like, a… implement new instrumentation module, or whatever.
Jack Shirazi 00:22:03 There's another option there, because that flag is true or false, but we could… we could make it multi-valued, so it could be true, false, or isIndy Ready, and then set the default to isIndy Ready, which means that anything that's IsIndy Ready would be true.
Something like that.
Lauri 00:22:20 like, by muzzle, I actually meant that, like, What you could do is that, inside those advice, there is, like, this flag. Is it… is it in line, or is it not?
like, Muzzle could use to, like, could, like, collect this information.
And automatically generate something based on that.
Sylvain Juge (Elastic) 00:22:43 Yeah, so for example, if you write a.
Lauri 00:22:45 muzzle to generate, like, this easy and do ready, I don't know.
Sylvain Juge (Elastic) 00:22:49 So, for example, like, the same way we assume that some annotations are being used to return the value from the advice.
we would just say, if you explicitly wrote, like, inline force, it means you… it's an indie-ready one.
I think it could be nice to do that.
Trask Stalnaker 00:23:11 Mmm… That's nice.
Jack Shirazi 00:23:22 Okay, I think we can move this to a PR, and then have feedback on that.
A decision on whether that's valid or invalid.
Trask Stalnaker 00:23:33 Sorry, my network is… Really bad.
Can you hear me now?
Jack Shirazi 00:23:42 Yep.
Trask Stalnaker 00:23:43 Okay, sorry, network lag.
That seemed like a nice way to allow people to… migrate… And opt-in at the same time, if that…
Jack Shirazi 00:24:18 Thank you.
Trask Stalnaker 00:24:28 Sorry, I think I'm still super laggy, so… I may be missing context.
Was there, was that… Enough, Sylvain, to… Work on a… for a path forward to work on. Can chat more next week.
Sylvain Juge (Elastic) 00:24:53 Yes.
Trask Stalnaker 00:24:57 Cool, let's jump, jump the queue here… And go to Jack… for… Shared internal code.
Jack Berg 00:25:14 Yeah, sure. So I'm glad John's here. So I opened this PR in a corresponding issue, maybe a year and change ago, about, like, hey, we should set a goal in the future to eliminate shared internal code.
And, you know, the… for context, shared internal code We have this pattern, it's extremely prevalent throughout OpenTelemetry Java, and the consequence of it is that you have to align your dependencies of OpenTelemetry Java in order to guarantee that you don't get runtime errors.
That's… That's… the consequence in a nutshell. And so, you know, it's hard to justify doing this work, because, you know, how many people don't align their dependencies? And also, there's, like, a lot of shared internal code, but it's still something we ought to do.
And so I… I'm re… sort of resurrecting this PR6978, which I think is the first step in, you know, a long journey of eliminating shared internal code, and it's just, like, tracking the problem.
So, the way that the 6978 works is it just, it, it adds a… what is it? What do we call these? An architecture test.
That, you know, uses these, these reflection API tools to look… to try to detect usages of shared internal code and warn us about them.
And, you know, basically, I think about this in terms of modules, like, how many modules are we publishing, and how many modules still have shared internal code use? And if we can say that, like, a module, for example, like, OpenTelemetry SDK Metrics, no longer uses any shared internal code.
from other packages, other modules, then we're good. And we can check that off. And, you know, we just work through all the artifacts one by one, and maybe there's some sort of prioritization amongst them, and, you know, someday we'll wake up and there won't be any more shared internal code, and this test suite will pass and not warn us anymore.
So, that's what 6978 does. It just, you know, it tells us about the problem. It's, And then we can do something about it. So, what do we do about it? Like, when there is an instance of shared internal code, what are the tactics that we can use to eliminate that? And there's three things that come to mind, and I have got them listed here. So, one of them we do, I call it, like, the copy-paste tactic, and we do this already, so it's basically like, hey, if you use some sort of utility class, and it's in an internal package, just, like, copy that package to all the modules that need it.
So just make a copy of the shared internal code. That's one tactic. And we have an example of this using Gradle tooling right now. We have this, like, you can set this Gradle property at the module level, and if you set it to true, then we'll include this hotel version class in the module, which allows you to programmatically access, like, the version of the module.
You know, at runtime, which is useful in a couple of different places. So, like, you know, if this is… if there's… if this is a recurring pattern, like, we want certain, little utility functions available in a bunch of different places, we could use Gradle tooling to… To make that happen. So that's one strategy. Another strategy, and this is what I'm really interested in feedback on, is to create a new category of packages. Maybe call it util, maybe call it something else, but the idea behind this util category of packages would be, like, hey.
We're gonna guarantee API stability here.
And we're gonna check in the changes to the API via, you know, JAPI CMP, and verify that we don't break, you know, binary or… API compatibility, and… but we're still going to discourage uses of these classes. These classes are for us, and so, like, don't come opening issues, if you use one of these classes directly and there's some sort of issue with it. Like, we're… we're guaranteeing API stability and nothing else.
Maybe… maybe nothing else is too strong a word, but we're just not going to support them.
So that's, like, another tactic we can take.
And then finally, promote APIs to public, which should be public. So, you know, Some APIs we've just been, like, sitting on for a while, and they're in shared internal packages, and, like, you know, someday we envision them being a part of our public API that users interact with, and you know, for those, we just need to make that happen.
We need to be, like, disciplined and say, like, hey, like, are we done soliciting feedback? What information do we need to know to feel comfortable promoting this to the public API?
And yeah, and promote it when it's appropriate to do so. Don't just sort of wait on things indefinitely.
So… I don't know, are there other tactics that I'm not thinking of here? Do folks sort of, like, align, or, you know, do these resonate with people?
John Watson 00:30:34 Is it possible to… not… like, for example, your new util package or whatever. What if we… Rather than doing the copy-paste solution, and rather than having to guarantee any stability on these into util packages, could we just shade it ourselves into those things at build time, rather than having to add this extra maintenance burden of having to maintain API stability on these things?
Jack Berg 00:31:08 Yeah, so that's like, that's sort of a variant of the copy-paste, right?
John Watson 00:31:13 Yeah, but it means we don't have to maintain multiple copies of it. Like, we only have to maintain the one copy of it, and we shade it at build time.
Jack Berg 00:31:21 The copy-paste, what I'm envisioning is basically essentially that.
John Watson 00:31:25 Okay.
Jack Berg 00:31:26 you, you, you have some sort of tooling, Gradle tooling, where you, you, you indicate that something is, that you want to make a copy of it in the module, and, you know, it's not like we're maintaining 10 modules… copies of it, it's like Gradle is doing that for you.
John Watson 00:31:43 Yeah, I… I think we should go… that… so my opinion is we should go that way. I would rather not add additional API surface that is not… things that… like, you say we're not going to support this new util thing, but we kind of have to support it in some way or another.
Jack Shirazi 00:32:04 Is that actually lower maintenance? Because then you have this additional… build thing that people don't understand, and it's a lot of… if you're viewing… if you're, like, viewing the code, then… It… it's… it's not gonna be clear what you're doing.
John Watson 00:32:22 Well, my issue is not on developer… like, the amount of work that developers in the… in the OTEL Java repo have to do. My issue is… people are going… if we publish this thing, people are going to use it. And once it's out of the box, we can't put it back in.
And that means we have… even though these… and we have deliberately not published these things so far, because we don't want to… we don't consider them to be stable, and if we suddenly just say, well, we're gonna make them stable, I mean, there's a reason we didn't make them stable. It's because we don't consider them to be ones that people should be using.
And if we publish them, they will use them. So this is… I'm less concerned about the maintenance… like, the… a little bit of more cognitive overhead for people working in OTEL Java, and more concerned with having to support APIs that are not part of OpenTelemetry, they're just kind of happen to be there because we use them.
So that's… that's kind of where I'm, leaning.
Jason Plumb 00:33:28 With this shading approach, does that imply that, like, every module that depends on another module from the project Gets all of that used code.
shaded in, and then also, is that transitive? Because that's… that interplay between all those modules seems like a lot of bloat if you shade everything.
Jack Berg 00:33:48 Yeah, it could be. I think it would have to be transitive, Jason, and you know.
it's hard to say, off the top of my head, just how much or how little bloat there would be. You know, you'd have to do something interesting, where it's like, you detect the shared internal usage, and you only shade in, for any given package.
the shared internal usage, like, and not anything else from other packages, and, you know…
Jason Plumb 00:34:19 Is that not what shading does already? Like, does it just shade everything, or I thought it was only stuff that was used?
Jack Berg 00:34:24 I mean, there's… there's configuration around it, but generally, you say, like, hey, I want to shade this entire jar, but you can, like, you know, you can include, exclude particular files if you want to.
Jason Plumb 00:34:37 That sounds like a maintenance nightmare. If you wanted to streamline it, like, only bring in the stuff you're using, that sounds like a lot of maintenance.
John Watson 00:34:46 But this is…
Jack Berg 00:34:47 I would hope that we could do it without maintenance, that it could be just automatic, and it's, like, essentially just, like, the build, the Gradle build is doing the tree shaking for us automatically.
John Watson 00:34:56 I would be surprised if this artifact, like, the amount of actual code that gets shaded in, like, when you get down to the bytecode level, like.
what is it gonna be another K per package? Like, it's not gonna be that much… it's not gonna be that much.
And it's already zipped, so… I mean, I would be surprised if that's a real… practical issue.
Trask Stalnaker 00:35:20 I have a… Thought a variant on this proposal.
Which, what about, Dot internal… dot util.
And so, it remains internal, but we make our tooling such that we… our tooling… we do the API diffs, we guarantee Just internally for us, that these things never break.
John Watson 00:35:51 How is… how is… so I'm cons… I'm confused about how this option This is even really different than what we're doing today, except that we aren't guaranteeing API stability. You still have to have things aligned.
Jack Berg 00:36:05 You don't have to have things aligned, because, as soon as you guarantee API stability around, this… this new util, or internal util package, then if you can guarantee API stability, and you can guarantee that across modules.
any module only references stable APIs, then you can confidently say, for example, that the Zipkin module can depend on a different version of Export or Common module without having to worry that APIs aren't available at runtime.
John Watson 00:36:39 You would… that was… that's only if you can guarantee forward… forward compatibility.
Right? Because if you want to add a new… a new function, a new method into this new internal thing that things are going to use, if people are still using the old one, then all their code is going to break if they don't also align the new internal packet… internal module with What the new deployment, new code being released.
Jack Berg 00:37:03 Sure, that's true. But that's, like, a comfortable upgrade path, I guess, is just, like, that we've all sort of gotten used to the idea that we can evolve our APIs by adding new things, you know, in the case of interfaces with, like, default implementations.
John Watson 00:37:21 But I guess I don't see how that solves the user problem. Like, they… now the user still has to basically maintain alignment or risk breakage on forward… on… on adding new functionality in that internal package, or util… util package.
Jack Berg 00:37:37 I suppose that's the best we can do.
Like, there's… because, you know, that sort of… the user has to do some of the alignment work is true even with our stable APIs today.
John Watson 00:37:52 Oh, for sure.
Jack Berg 00:37:55 So, like, this would just be bringing all of our… all of our modules and, like, up to the, sort of, the UX that we offer with our stable APIs.
Which, you know, there's still going to be some edge cases where you have to bring a package Forward inversion.
Sylvain Juge (Elastic) 00:38:23 And regarding this lack of alignment between versions, do you see this as being intentional from the user?
For example, if they inherit some dependencies from something they can't control, or do you see that more happening by accident, and we need to preserve compatibility?
Jack Berg 00:38:41 The thing I saw all the time, Sylvain, was, like, was Spring. The Spring, bomb has a particular version of the of OpenTelemetry that it's, like, pinned to, and, like, let's say you're using the Spring Dependency Management Cradle plugin, then you're getting the OpenTelemetry version from its BOM, which is, like, 1.33.0.
And then you separately add a dependency on OpenTelemetry Java's BOM so that, you know, it's maybe 1.55.0. The interplay between the Spring Dependency Management Gradle plugin and, you know, just adding a dependency, a platform dependency on the OpenTelemetry Java BOM, it's like, it's really bad.
It's like, it's not clear how you… definitively say, like, hey, I want 1.55.0 of OpenTelemetry Java. And so, you, like, frequently come… I came across this, like, a number of times, and you have to do, like, Gradle magic to basically ignore the OpenTelemetry Java version from the Spring Dependency Management Gradle plugin.
GZ Gregor Zeitlinger 00:39:50 It's not magic. We have documented the solution that you should do in the Spring Starter page, but You just cannot read this documentation, and then you are not doing it.
Trask Stalnaker 00:40:01 Yeah.
It is not documented, but it is a magical thing.
Sylvain Juge (Elastic) 00:40:06 Yeah, my question was more, like, should we just try to make sure that when a mismatch happens, the user is aware of it and can fix it? Or should we, like, try to keep things working smoothly, even if there are some complications in the dependencies?
Jack Berg 00:40:24 So that, I think, is, like, a fourth category of things, which is, like, like, something like, continue to accept the problem, but offer the user better detection and mitigation solutions.
Sylvain Juge (Elastic) 00:40:39 Okay, because, for example, like, I was thinking of the hotel version, where you could say, like, every module, when it loads, it checks, like, the modules it depends on, and if there is a mismatch, just issue a warning.
Jack Berg 00:40:52 Right, right.
John Watson 00:41:00 I will… I will 100% agree, though, that this is a real problem, and we have… it can… I think it will continue to happen.
Especially just with the… the… complexity… of the project and its internal dependencies. I agree, it's a bad problem.
I'm just not sure there's a… there's a great solution, unfortunately.
Like, I think we're choosing between maybe the lesser of… The bad, or the uncomfortable solutions.
Jack Berg 00:41:36 The detection solution, actually, like, that's something we can do in the shorter term. Like, even if there's a long tail on resolving this, like, that's kind of interesting. I don't know exactly how that would work, but I don't know, that's interesting to me.
Jason Plumb 00:41:52 So the reason why just hand-waving around, like, silly user use the bomb, like, that doesn't work, right? Because you could have transitives that use different versions? Is that… is that why?
John Watson 00:42:02 Well, I think the spring… the spring case is the bigger one.
Jason Plumb 00:42:05 Yeah, yeah, okay.
John Watson 00:42:05 The way that the spring bomb works with the other bombs in general is just kind of a mess.
Jason Plumb 00:42:10 Yeah.
Jack Berg 00:42:11 It, like, the Spring Dependency Management Gradle plugin, in my head, it just, like, it just puts its finger on the scale and, like, has a higher priority level for the versions that it has under management. So it's, like, overriding what you say in your dependencies.
GZ Gregor Zeitlinger 00:42:27 And that's generally a very good user experience, just to defend Spring a bit, this has, Kept away problems for users most of the time.
Jack Berg 00:42:40 So then, like, Gregor, like, what's the issue then? Because… is it just that… because if Spring always… was able to tip the scales according to its dependencies, like.
How are some dependencies getting to different versions?
Is it, like, it's not… it doesn't bring… it doesn't have enough dependencies under management? It doesn't have all of the OpenTelemetry problems?
GZ Gregor Zeitlinger 00:42:59 cleared. And, in our case, it's specifically the unstable dependencies.
they don't want to have the alpha dependencies, and that's why our hotel bomb picks up the unstable dependencies.
I think that's the main issue, and That's, why they have different versions. If we would.
Jack Berg 00:43:24 I know you're not representing Spring, but I guess, like, it's weird to not want… like, it's not like this Spring dependency management brings in an alpha dependency. It's just saying, like, that this alpha dependency is under management. It's, like, inside of the platform.
So, like, it's still the user's call to bring in that alpha dependency.
GZ Gregor Zeitlinger 00:43:45 You could say that, it would be sensible that Spring would also pin the alpha dependencies. I mean, then we are getting into this religious war again, but I think it would be a practical solution to pin everything and not just some things.
Jack Berg 00:44:09 Okay, we've spent enough time on this issue. I want to get to the other topics. Like, so, tactics aside.
I still think 6978 is a good PR to merge, because it is not opinionated about what the tactics is. It's just about, like, you know, detecting the problem and warning about the modules that use shared internal code.
Every time you run the build.
GZ Gregor Zeitlinger 00:44:36 I just wanted to add one comment before I… Because I did get to it. In Go, this is not such a scary thing, it's called vending. So copying… other code into your codebase. And it's, it's a very, normal thing. You don't have, like, this Gradle magic, you just have a script that copies some other code into your code, branch, and it's under the vendor directory, it's just not common in Java, but it works really well.
Jack Berg 00:45:11 I think that's the shaded solution, the shaded slash copy-paste solution, so…
GZ Gregor Zeitlinger 00:45:16 Yeah, but shading has all sorts of problems, and it's really difficult to understand, even though technically it's very similar.
Jack Berg 00:45:24 Okay.
But, like, categorically, though, so you're kind of giving, like, a thumbs up to the sort of copy-paste family of solutions, whether that's shading or some other variant of it.
GZ Gregor Zeitlinger 00:45:35 Yep, right.
Trask Stalnaker 00:45:42 Alright, let's… Keep going. Sylvain.
Sylvain Juge (Elastic) 00:45:47 Yeah, I tried to be quick. So, we are basically trying to implement something that could be implemented using A rule-based sampler.
But we don't want yet to embrace declarative configuration, and we are wondering in the future.
Over you see, like, distributions interact with, declarative configuration.
Because we want to add some new features that could be, potentially in the future, set by declarative configuration from the user, but we still want, for example, to provide our own implementation. For example, like, to provide, like, runtime configuration, or being able to change assembling rate at runtime.
And so, we wonder how we should deal with these kind of, issues, in the future.
And…
Trask Stalnaker 00:46:42 So, you're asking, generally, like, how to… I mean, you want to do key-value property configuration for a sampler?
Sylvain Juge (Elastic) 00:46:54 Yes. So, two things. First, like, to do something that could be done with a rather verbose configuration of the whole base sampler.
And being able to modify it at runtime.
So the question is, can we in any way, like, get access to the declarative configuration, and just provide our own instance of our custom implementation?
Jack Berg 00:47:22 So…
Jack Shirazi 00:47:23 I was… I was just looking at the, the methods instrumentation, that's effectively what… I think, Gregor, you've now changed it, so what it does is it gets hold of the config provider for the declarative config, and if you're not using declarative config, it'll fall back to the system property. So you just use the same path as you would in declarative config.
But it would use the system property instead. So it looks like that's… that's now supported.
GZ Gregor Zeitlinger 00:47:55 Right.
Jack Berg 00:48:00 So, I guess… I may be misunderstanding the question a little bit, but there's, so… Okay, you've got a distribution of the Java agent, you don't want to necessarily use declarative config, you want to use something like the rule-based sampler, which has sort of complex configuration implicit in it, and you want to use environment variables and system properties to configure it, and then modify it at runtime by connecting to some sort of remote server. So, like.
There's the sampler provider, SPI, Right? So that's the… that's the standard way that you… that you plug into the auto-configure mechanism and provide your own sampler, right? And sampler providers… I think it's configurable sampler provider.
Right? And so, you know, a sampler provider has access to config properties, which allows you to read environment variables and system properties, and I guess, like, there's nothing stopping you from providing your own configurable sampler provider that provides rule-based routing sampler instances, or any other sampler instance, and sort of, you design your own scheme for how that configuration information is represented in environment variables or system properties.
you know, you could do something as, like, you know, you could have a stringified JSON configuration if you wanted to, or you could find some other sort of comma-separated or other delimited sort of way to configure otherwise data, which I would say is, like, better suited for YAML, but not necessarily only YAML, right? There's nothing restricting YAML.
Sylvain Juge (Elastic) 00:49:40 So, in a sense, it would be, like, providing our own configuration bridge, on top of declarative configuration.
Jack Berg 00:49:48 I guess that's the part that I'm probably most likely misunderstanding, is like, are you trying to say, like, I don't want to interact with declarative config at all, I just want my users to use system properties and environment variables. Like.
Sylvain Juge (Elastic) 00:50:04 Yes, at least short term.
Jack Berg 00:50:07 then I don't think you need to interact with declarative config at all.
Like, so, you just need to provide, you know, declarative config as mechanisms for, expressing rule-based routing sampler.
And you need to kind of replicate that functionality with the existing, you know, system property environment mechanism, which is, you know, implement configurable sampler provider.
Jack Shirazi 00:50:37 So, are you also talking about being consistent with declarative config, in case that.
Sylvain Juge (Elastic) 00:50:43 Yes.
Jack Shirazi 00:50:44 Yeah, I think, I think that, that, that, they've done that in the, if you look at the methods instrumentation.
They've effectively done that, so if you… That's implemented such that if you provide a config provider, which there will be, even if you're not using declarative config, it still works. And it works using the… The path you would find.
It's just… Where declarative config would return an array, the… the… The failover returns just the value from the…
Trask Stalnaker 00:51:21 coded string.
Jack Shirazi 00:51:23 Yeah, the encoded string.
Yeah, so I think there's an example there that you can follow.
Trask Stalnaker 00:51:29 One difference, though, if you're specifically asking about samplers, is that, samplers are gonna be SDK, Yeah, the bridge that we have in the Java agent is only for that instrumentation node in declarative Config.
So… I don't know, there's a bunch of pieces, I'm not quite clear on what, where you're stuck.
Sylvain Juge (Elastic) 00:52:01 Yeah, for example, like, see, in this case, it would be, like, overriding the default tracer, and, The default sampler, sorry.
Trask Stalnaker 00:52:11 If you want to put together some code, you know, a draft or anything that, you know, and share it in the Java channel might help us to look at some code.
Jack Shirazi 00:52:22 There was a separate issue, is if declarative config is defined, is there any way to then override in code.
So that's what I was bringing.
Trask Stalnaker 00:52:36 this up for?
Sylvain Juge (Elastic) 00:52:38 Right.
Trask Stalnaker 00:52:38 So this is how you can… a distro can customize if a user is using declarative config.
And you want to augment it with your own, sort of, default values, your own samplers, this is what you would use.
Sylvain Juge (Elastic) 00:52:57 Okay.
Trask Stalnaker 00:52:59 I'll drop that link into…
Sylvain Juge (Elastic) 00:53:04 Thanks, I think we can make progress on this one.
Trask Stalnaker 00:53:09 Cool. Jonathan… Profiling…
Jonathan Halliday (IBM) 00:53:14 Yeah, hopefully this is a quick one. Recall that last year, Ivo dropped by and talked about this proposal to be able to export metadata in a way that other processes can read.
It looks like it's probably got critical mass now.
the TC seemed happy with it. So yeah, last chance to object.
With my profiling hat on, it looks fine. With my Java hat on, mmm… it's gonna require some system programming, you know, we're gonna have to call C code at some point, but… Can't be helped, I think.
Jack Shirazi 00:53:46 Am I writing?
Jonathan Halliday (IBM) 00:53:47 maintainers.
Jack Shirazi 00:53:49 Am I right in thinking that that means that the agent needs to include a… A native, library.
Jonathan Halliday (IBM) 00:53:57 Most likely, yes.
Jason Plumb 00:53:59 Or could it be done with shared memory?
Jonathan Halliday (IBM) 00:54:02 Well, it is being done with shared memory, but setting up the shared memory requires syscalls.
Jason Plumb 00:54:06 Not on… not on newer versions of Java, but yeah, yeah.
Jonathan Halliday (IBM) 00:54:11 Yeah, the specific way it's being set up, I'm not sure Java's API is rich enough. To be honest, I haven't tried it on the latest versions, but… Yeah.
It might depend, you know, which versions we want to support, and exactly which operating system we're running on, and blah.
Jack Shirazi 00:54:25 They've got a pure Java implementation for modern Java, but… Oh, nice. No, we support jobs.
Jonathan Halliday (IBM) 00:54:32 Yes, we support all…
Jason Plumb 00:54:33 8.
Jonathan Halliday (IBM) 00:54:34 Yeah.
Jack Berg 00:54:35 I do think it would be fair to, to not necessarily jump through a million hoops to have this supported all the way back to Java 8.
We have… we have prior art with that, too, right? Like, we have additional features in the Java agent that are unlocked once you have Java 7… Java 11.
John Watson 00:54:55 Yeah, I agree 100%. We should… we should go the expedient path with the Java versioning on this one.
Trask Stalnaker 00:55:05 I would be fine with that as at least an initial implementation, and if we could get a bunch of pushback, then somebody can contribute the more complex thing. We can consider that.
Jack Shirazi 00:55:18 I think the pure Java one requires Java 25, so…
Trask Stalnaker 00:55:23 I was hoping at least down to 21.
Jason Plumb 00:55:28 So the very next thing, like, once this lands and once we build it, the very next thing someone's gonna build, right, is a spam processor that has access to the resource.
Like, that's gonna be the next thing. People… people ask for that all the time, right?
Jack Berg 00:55:41 You can access the resource in a span processor, you just have to call span.2DataGetResource.
Jason Plumb 00:55:47 Oh, you have to convert it.
Jack Berg 00:55:49 It's not that hard. Like, if you're in the SDK space and you want to access the resource, it's pretty easy.
AI space, and you want to access the resource, that's harder.
Jason Plumb 00:55:59 Maybe it's somewhere else, like, maybe it's a sampler, I forget. There's another place where people keep asking for the resource, or it's not easily obtained.
Sampler would make sense.
Trask Stalnaker 00:56:09 Yeah.
Jack Shirazi 00:56:10 just going back to the native library, just to be clear, we're saying, yes, we will include a native library with the… I'm not sure if it's the SDK or the agent.
Jack Berg 00:56:23 It would have to be… it would be modeled as, like, an SDK extension, and then the agent would have to make a decision of whether it would or would not include this SDK extension, and yeah, like, you know, for this to be useful, it has to get the distribution of the OTEL Java agent, so we would probably include it. But, yeah, like, but I thought we were just saying that we think we could do it without native Without, native libraries.
Trask Stalnaker 00:56:54 Depends on the job.
Jack Shirazi 00:56:55 Lovely.
Trask Stalnaker 00:56:55 version, if it's Java 25.
Jack Berg 00:56:58 Right, so, like, that's the starting point, is the… assuming that we don't need anything extra.
Trask Stalnaker 00:57:10 When is Spring gonna bump to Java 25?
That's kind of the driving force right now in the ecosystem.
Jack Berg 00:57:19 what other way could you do this? Like, so if we don't want to use native memory to share this context, like, the only other thing that… another thing that comes to mind is, like, the SDK could… Publish this data on, like, a well-known port or something, or have some sort of discovery mechanism where, you know, it can just, you know, clients can call this over the network?
Jason Plumb 00:57:41 Or it could write a file, or it could open a pipe, yeah, there's…
Jack Shirazi 00:57:45 it can use shared… a shared memory file as well, but I think they've reviewed all of these options, and they've… they've gone with The one that they've gone with.
Jack Berg 00:57:55 So this is just an OTEP, luckily. So, like, if we go and implement this in Java, and we say, like, look, we can only do this in Java 25+, because of these limitations, then maybe that feedback propagates back to these folks and say, look.
We gotta find a different way to share this information, because, you know, we can't limit ourselves to only Java 25+.
I mean, what we can do is we can look at the Java prototype and And, bring our comments back, and say, like.
Unless it's Java 25+, we need to add these dependencies, which seem like toxic dependencies to the Java agent, and we're not that excited about doing that.
Trask Stalnaker 00:58:44 Jonathan, are you planning on working on a Java prototype, once the OTEP merges?
Jonathan Halliday (IBM) 00:58:52 I wasn't, but I potentially can, yeah.
Jason Plumb 00:58:56 Are there prototypes in other languages yet?
Jack Berg 00:59:00 Alright, this OTEP includes links to them.
Jason Plumb 00:59:03 Okay, I haven't read it, sorry.
Jack Berg 00:59:04 Oh, okay, sorry. Josh was just hovering over it. Okay.
Trask Stalnaker 00:59:18 Cool. So… Do you need approval from… The… are you explicitly looking for approval from…
Jonathan Halliday (IBM) 00:59:30 I think it's required, I think it's… It's nice to have.
It's nice that some of the SDKs are saying.
Yeah, this looks okay to us, because obviously they're the ones who have to implement it.
So I guess that will reassure people like the TC, who are the ones who actually have to sign off on it, that it's got critical mass.
Trask Stalnaker 00:59:59 If anybody feels like leaving a comment just about the potential complexity for Java, That might be useful.
But I know it requires some more research.
Alright, we are running out of time.
Jack Berg 01:00:23 This is just an inform. I have two PRs open that are sort of, I like your term, Trask, I saw somewhere. They're pre-factors. I'm trying to… I'm going to do some research… Prefactors.
Trask Stalnaker 01:00:32 Refactor.
Jack Berg 01:00:35 I'm gonna do some refactoring to the metrics SDK to increase performance under contention. Before I do that, I need to get the benchmarks and the testing up to snuff. So that's what these PRs do, so… They're… They're not impactful to the actual public code.
Trask Stalnaker 01:00:53 Alright, and we can talk about 3-0 next week.
Thanks, Haw.
Jack Berg 01:01:00 See ya.
