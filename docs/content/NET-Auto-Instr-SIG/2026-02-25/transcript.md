SIG: .NET Auto-Instr SIG
Date: 2026-02-25
Duration: 48 minutes
Zoom Recording URL: https://zoom.us/rec/share/FDfLNU74C_Z7zrLTMmrAm5Wv-7IVxr8BQLGi9qSPTNQfVHo034h4FRx1NRE8QicS.VoZaeHcHYif2Kyhf
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 04:27 Hi, guys.
**Chris Ventura** 04:35 Hello.
**Alexey Pukhov** 04:37 Hi again!
**Igor Kiselev** 04:42 Hi.
**Piotr Kiełkowicz** 04:48 Mmm.
I don't think I need to drive anything.
So, let's start with the pull requests.
So, I've just opened the new functionality related to no-code, it is internal requests.
Still, it is not… It does not cover all… Let's say…
unhappy Paths, but Happy Path is ready to… to review.
So, looking for any feedback on this stage.
It is fully manually implemented and does not rely on ANI.
external library, I think it is pretty well described in the documentation.
Basically, what you can do is to… give me a second…
You can manual… you can dynamically set span names, attributes, and the statuses.
Depending on the… Hmm.
Object name, attributes method, and the potential, return value from the methods.
So, looking for… for you. I think, Chris, you have similar… Functionality.
In your agent, or no?
**Chris Ventura** 06:55 Not for dynamically adding the attributes, so I'm interested in how we're declaratively mapping from the config to individual things to extract the attributes from.
**Piotr Kiełkowicz** 07:11 So, there is a proposal kind of working for the happy path, so it would be great if you can take a look into this.
**Chris Ventura** 07:18 Sure, I'll take a look.
**Piotr Kiełkowicz** 07:20 Great, thank you.
Crystals are kind of spying.
I think I need to just check the documentation, and the changelog, and if it is fine, it can be merged.
And Alexei, I think you are also looking for the review, as it is kind of huge PR.
Or you want to fix something before final round of the review?
**Alexey Pukhov** 08:09 Yeah, thank you, yeah, sorry, I was looking for the unmute button.
So… well, yeah, I will need a review. I'm almost code complete for the pull request, I'm just addressing the last, comments that Igor put.
Related to the native… Profiler detection of a standalone deployment.
Looks like we already have similar
logic in other places, so I'm just combining that together.
Well, first of all, both Chris and Igor, thank you for reviewing the change, it's a big one.
I just had two questions, actually, I wanted to bring up loud.
Since we're all here.
But I guess we kind of agreed on that. One of my questions was, we are switching the environment variable for the assembly redirection.
to enable or disable assembly redirection. Since we are switching the environment variable to a new one, it's a good time to make sure we have the right name for the environment variable.
It is… Right now…
Says assembly redirection, but we are planning to use it for the startup hook isolation as well.
Which is, to a certain extent, an assembly redirection, but I just wanted to make sure we're gonna look at that particular place.
To make sure that the name of the variable is… Fits the purpose.
So that was one question. I think, Chris, you already agreed on the name of the environment variable. Igor also agreed, but again, just wanted to use this opportunity to bring it up loud for the whole community in case anyone have any concern against this.
And the second part… oh yeah.
**Piotr Kiełkowicz** 10:04 It was always true, yes, by default, and nothing changed in this way, so we are just changing the name.
**Alexey Pukhov** 10:12 Yeah, we're changing the name because it used to carry the NetFX context. It's now working for both Net and NetFX, so I'm removing NetFX. But then, since we're going to be using it also for the startup hook isolation, that doesn't…
use the native redirection. That's where my question about the name came.
through… But there's a…
**Piotr Kiełkowicz** 10:40 I have one question here, Chris. Do you think then we can just drop old name, or should we have a kind of backlogged
for some period of time.
**Chris Ventura** 10:52 So the… I think we should have some level of backwards compatibility for at least a period of time, and I believe the PR currently has the old name in place for backwards compatibility purposes.
But I believe we're only checking the old name.
for the framework side of it, it's been a little while since I looked at that code.
**Alexey Pukhov** 11:18 Yeah.
No worries, exactly. So we do keep the old environment variable, well, at least for some time. It's a fallback if, only on Windows for .NET Framework, obviously, if the new environment variable is not available.
We… I'm gonna plan to put this in documentation as well, again. Cool. Since it's there, it should be documented.
**Piotr Kiełkowicz** 11:47 short.
**Alexey Pukhov** 11:48 And…
So yeah, anyway, just take a look at the name of the environment variable. Keep in mind that it's also used in the startup hook isolation.
Which is not really redirection. Well, it's not redirection per se, but it's kind of a redirection. We do redirect the assemblies. It's just not in the sense of a native profile redirection.
**Chris Ventura** 12:13 Yeah, it's the same idea, where…
Swapping out the assembly versions.
**Alexey Pukhov** 12:20 Yep.
Cool. Glad I brought this up. And the second question is actually for Pyotr. I do change the… I noticed that from time to time, Pyotr, you're updating the… bumping up the version of the dependencies in the directory props file.
And I'm changing the structure of this file, but not dramatically, I'm adding the .NET Core.
To eat. But I just thought you might… I might need to ask you, to resolve the… Let me check.
**Piotr Kiełkowicz** 13:00 this one.
**Alexey Pukhov** 13:01 Y no de assemblies, directory.
**Piotr Kiełkowicz** 13:06 This one.
**Alexey Pukhov** 13:07 Yep, this one.
So yeah, just thought you… you… I need your opinion on this.
**Igor Kiselev** 13:13 both of those.
**Piotr Kiełkowicz** 13:14 Okay.
**Igor Kiselev** 13:14 will be important, so please take a look that it is still maintainable, and my feeling is that we would need some automation script to help us maintain it, especially with a new approach. Not before hotel selection, when hotel use latest.
**Alexey Pukhov** 13:33 version that is in the same major release for .NET.
**Igor Kiselev** 13:38 For a matching assembly, I mean about Microsoft Extension, login Microsoft Extension, login abstraction, so we use latest version of
assembles 803 for .NET 8, 9 or subset for .NET 9, and it would
be pretty hard to maintain manually, so we most probably would like to have a script to do it. We could create it in a follow-up pull request, but.
**Piotr Kiełkowicz** 14:07 in, in general, SDK from latest release.
Keeps the lowest possible dependency version for the given .NET version. So, for…
NET 8, for most of them, it's just 800. There is no upgrading for old…
801, unless there is kind of security issue.
Such dependencies are kind of big, big issues, so… I'll change that.
**Alexey Pukhov** 14:43 Out of the dog.
**Piotr Kiełkowicz** 14:46 It was changed. I think there is a pin… Issue about this.
**Igor Kiselev** 14:53 And here is… it's in the additional,
things that we'd like to discuss as a group, there is a big difference between our project and, Hotel, typically, because Hotel provides a NuGet package only.
And for NuGet package only, the proper culture would be to depend on the minimum version that is required to… for it to be, installed.
If customer would like to upgrade to a latest version, he always can do it while he manages his own project. So you do not limit what customer… what customer can use as a version of the dependency.
For us, we have two ways of deployment. We have a NuGet deployment, which still should follow the same culture and are controlled by directory packages props on a root level.
And we have a ZIP deployment. For ZIP deployment, it means that we provide not only us, but we also provide all our third-party dependencies as one big package. My personal feeling is that when we provide
us and all our third-party dependencies, and we install it in already existing customer application, and we still upgrade a version of dependencies that customers have, or bring a dependency that customers never have. We should provide a latest, hotfix, for… that bring in dependencies.
And that's why we have a second file in assemblies folder directory packages probe that only guides what we bring in a zipper hive.
So…
**Piotr Kiełkowicz** 16:32 Ngor, one comment here. If you reference, let's say, 800 version.
And it is part of the .NET runtime, and most of these dependencies are part of the .NET runtime. You do not need to ship it at all, because you will rely exact on the .NET runtime folder.
**Igor Kiselev** 16:54 not…
up to some level, and not for most of the dependencies. Because for most of the dependencies, we rely… we compile it for ispanetronTime. Oh, for .NETRANTIME.
And all the dependencies are part of iSPenetronTime. So, unless we plan to have a two different distro for .NET runtime and ISPenetronTime, we still need to bring all that dependencies with us.
Otherwise, it would be not enough for .NET-only runtime. If you would see all Microsoft extension dependencies are that class of dependencies that exist only in ISPNF.
**Piotr Kiełkowicz** 17:34 Yeah, you're right.
An issue about this, yeah, you are right.
**Igor Kiselev** 17:39 And that's why I specifically asked Alexei to sound that concern, that it becomes something that entire SIG should agree on what our strategy is, and make sure that it is in a maintainable state after we would do that merge.
Cool.
**Piotr Kiełkowicz** 18:03 If you are able to redirect to the latest version, we can follow the document framework pattern, in my opinion. Chris, what do you think?
**Chris Ventura** 18:13 Yeah, I think so. I think it would be a lot simpler for us to maintain if we can keep things consistent.
and have fewer of these special cases, so…
I know it's not standard with NuGet to,
depend on the newer versions of things with each release, but I think
I think it would make it a lot easier for us to maintain going forward.
**Igor Kiselev** 18:47 And I heard that, we plan to, continue for NuGet, follow Hotel model, but for Zipper Hive, always use the latest version. So, always use version 10X, even for something that… for Zipper Hive only.
**Piotr Kiełkowicz** 19:06 That's what we… question? It is what we do for .NET Framework, or no?
**Igor Kiselev** 19:11 Yes, we do it for .NET Framework.
Because for .NET framework, there is no, and, why I believe that earlier, why, the change was, in hotel initially. A lot of customers said that we are using our
Our strategy is to use only LTES release.
And a test release is non… every second release. So, and it means that in a time of .NET 11 as the latest release, and .NET 11
as a latest package, we would bring STS, dependency to customers that have a LTS-only policy, and
it's maybe not feel comfortable. At the same time, it may be not a big problem, because Microsoft currently extended a test release to match the previous LTS release, so they would never be in a situation that a new version have less support timeframes than a previous version, but still some facts to discuss. We could create a separate ticket
To discuss specifically that, and what we would like to have in different districts before we would merge them.
**Chris Ventura** 20:26 I thought that that was addressed in the SDK NuGet package, which is ultimately what pushes our dependency strategy.
So, for… Like.NET 9 and 8.
the SDK updated to only depend on the 8 or 9 dependencies when you're targeting that version. But for Framework, I don't… I didn't follow to see which dependency it took.
**Igor Kiselev** 21:08 Okay, yes, so for the framework, it will be the latest, but let me again try to repeat it. It's important. So, right now, we have two files that guide what versions we would use. Who is representing? Could you open again?
the… This one? Yes, that file. So, take a look. There is two directory packages props, one on the root level.
So, on a root level, we only declare what, what
Hotel dependences we bring in with us, and here we fully… it is used for NuGet packages, and here we would fully follow what, hotel, imposed on us.
But at the same time, we have a second directory of packages props, it's inside assemblers folder. So that pile, it's a full transitive closure, a full list of all dependencies down the stack that would be included in the packages.
And for that file, when we built a zip, we have two options. One option, we could always use what OTEL brings to us, and in most cases, it would be the oldest version for that particular framework.
Second option, we could, when we form a ZPR hive, we could auto-upgrade, we could upgrade dependencies only for that ZPR hive.
So, it means that if customers download us and all transitive dependencies, you would get a latest version of what… or latest
There, and here we have our different, strategy. We could have, let's say, that on .NET 8, he would get all latest in 8 family, on .NET 9, he would get all latest in .NET 9 family, or we could say that
always, even on .NET 8, you would get latest dependence. Right now, we implement a strategy here to always use the latest hotfix.
from the same measure. And for .NET Framework, it's always the latest measure. That's why you see in that file a separate section of .NET 8, 9, and 10. If you scroll down, you would see it.
So, you see, for .NET,
8. There is version from 8 family, for .NET 9, there is a latest version on .NET 9 family.
But that file, we are responsible for making it, so by our script automatically would sound which dependencies we include.
through… through hotel, but after it, we can update it, and right now, we are, used.
**Alexey Pukhov** 23:55 Some of those versions were updated, were bumped up, just because they exist.
like, if you just generate this file, I mean, if the file is missing, and you just generate it, it would be 8 zeros, 9 zeros, and 10 zeros.
So I just went ahead and upgraded all those versions to the 8 zeros latest, 9 zeros latest, 10 zeros latest.
**Chris Ventura** 24:24 So, I want to think through what would be the harm if we kept them similar. So…
So right now, with the ZIP deployment, it's using the ones with the latest… Versions.
But if we use the oldest…
without any security issues, so it matches what we're doing for the NuGet.
Will that be problematic?
**Igor Kiselev** 24:54 No? No, it wouldn't.
It wouldn't. The only problematic would be that, you bring, so, the only problematic would be to customers who said that they… we should use the latest hotfix version, for dependencies, that the… you bring in
Not latest hot peaks, version for… for that customer.
**Chris Ventura** 25:20 Right, but with our assembly redirect.
Would we detect that and just load their version, because it's a higher version?
**Igor Kiselev** 25:31 Yes, if they have a higher version, yes, but in a lot of cases, we may bring dependencies that they don't have at all.
So, think about if we are… if they are not on ice penetrant time, but on .netron time, and they installed
latest hotpeaks of .NET runtime, we would still bring, some Microsoft extension packages that… not much in their runtime, but
much la… Non, non-vulnerable latest.
**Chris Ventura** 26:05 Right, which would be the same behavior if they had used a NuGet package to manually manage.
**Igor Kiselev** 26:10 Not really, not really, because if they would use a NuGet package, they would see in Visual Studio a list of packages for which they have a later version released, and they have an opportunity to update them.
Well, I…
**Piotr Kiełkowicz** 26:25 ever.
**Igor Kiselev** 26:26 They would not see a list, a list of dependents that we bring, because that is not the latest one, and they…
Lack an ability to upgrade it easily.
**Chris Ventura** 26:37 Right.
**Piotr Kiełkowicz** 26:37 Increase, and… increase, and one more thing.
the… this approach proposed by Alexier should solve also this… this issue, in my opinion.
Because…
We will be finally bringing the extensions packages, the appropriate version for the .NET and console applications should be able to execute.
**Chris Ventura** 27:06 Yeah, so… I'm just trying to think through this problem, in that… Okay.
So, let's say somebody wasn't using auto-instrumentation, they're just using the SDK.
They add the NuGet package, but they have a policy of always using the latest version of something.
Do those customers always go through and look at transitive dependencies and make sure those transitive dependencies.
**Igor Kiselev** 27:36 Are updated to latest?
I don't know. I would say… I think it, depends on a process for each particular customer. I would say…
Our team, for example, look into what we have and update for transitive dependencies often enough. At the same time.
For example, if we talk about OpenTelemetry.NET Auto Instrumentation package, we have Dependable that do exactly that. It looks for alternative dependencies and creates a pull request, as it seems that new transitive dependencies have been released. So, I believe there would be a lot of customers that have a
process.
That make it auto-validatable, that if there is a new transitive dependence, it would be at least tried.
**Chris Ventura** 28:23 Right, but I think in practice, the majority of people just have something like Dependabot looking at the direct dependencies that they have in their project files, and they're not building out the infrastructure
So, that's where I don't want to solve for a problem that we're not… Sure fully exists.
I mean, it's… it's possible, so… that it could exist, but I'd rather have confirmation before we make things more complicated.
If that makes sense.
**Igor Kiselev** 29:02 It… by the way, if we would say that we always match what we use in NuGet package, we solve another issue right now.
So, if we use a later version.
of dependencies by default in the parHive. It means that, if customer would enable, assembly redirection mode in NuGet.
mold.
and they do not provide that latest version, it would crash the application. That's why we work right now to make, assembly redirection out of… assembly redirection auto-detectable and not activate it for NuGet. Because, by the way, it's not required there. If we would always have the same version that is matching, it would be… that problem would be solved.
So, any option have some benefits and cons.
My suggestion right now would be, let me and Alexi work to create a separate ticket, where we would, again discuss what, what's current state, what option we see.
And after it, there would be 3 or 4 different options. After it, we could collectively select something and discuss it there, and probably get a community option to provide their input to what they think much better for their deployment.
**Chris Ventura** 30:24 Okay, I think that.
**Igor Kiselev** 30:25 And we can, at the same time, change it pretty easily. So right now, we already have a control, and that I said that we only need some automatic scripts that implement that logic, so that it would not be a burden on us when we try to update it to fully follow our…
process. And the only thing that we would need, we need some decision, how currently the packages should look like. And what I hear right now, it is, let's use the oldest version that match, hotel as, hotel as they cannot get package selection.
And it's probably a good start for initial change, so we would
revert the updates to the latest version. So you see in a lot of case 801, 802, it would be reverted to 800.
In most cases.
So… In that case, we would be able to split it, and we found that, yes.
It is our decision for now, but we have a separate discussion about it.
**Alexey Pukhov** 31:38 Okay.
**Piotr Kiełkowicz** 31:39 One comment here, we can always start with the lowest possible version, Hence… If needed.
Upgrade it to the latest hotfixes.
**Igor Kiselev** 31:50 Oops.
**Piotr Kiełkowicz** 31:51 This way, we can go without any breaking changes, in my opinion. The opposite direction is kind of one-way ticket for…
the lifetime of the particular .NET version.
**Igor Kiselev** 32:08 Mmm.
Maybe, maybe, okay, I, I support, I support the decision, let's, like, see.
Probably, in that case, should make sure that the packages looks the same way as it was auto-generated, except of dot
A question, and what's these .NET version dependencies? NET.NET framework version dependencies. Previously, we always used the latest patch.
Should we also continue… should we continue latest patch, or should we downgrade it to the same strategy latest
Late, oldest possible. Non, non-vulnerable.
**Piotr Kiełkowicz** 32:54 Igor, I'm not saying that…
it is a decision that… I'm just putting that one more comment, what will be blocked or possible with that decision, so…
**Igor Kiselev** 33:06 Okay, good.
**Alexey Pukhov** 33:12 Okay, well then I… I'll… I'll change that.
And after that, as I said, DevComplete will be done for me. I just wait until I push the changes to make the pull request green, because there is a native compilation issue, and some formatting issues as well.
And after that, I'll… still have some tasks that I wish to put along with this pull request.
pull request, and there are some optional tests that I can do as a follow-up.
You can review those mandatory tests.
in the description, I think… I think those should go really with the pull request, while I'll move some other tests as…
Those that we can do as a follow-up.
Yeah, thank you so much for the discussion.
**Piotr Kiełkowicz** 34:10 Alex, I think Zach mentioned on the Slack that I would like to review.
this PR, so if you can kind of bring summary of the discussion and share in the GitHub.
Directly, it would be great.
**Alexey Pukhov** 34:25 Sure, yeah, thank you for that. I'll definitely do that.
**Piotr Kiełkowicz** 34:34 Chris, any other top comments for this topic, or…
**Alexey Pukhov** 34:37 I'm done.
**Chris Ventura** 34:39 Nope.
**Piotr Kiełkowicz** 34:48 I… I think that's all. We have, kind of, primal…
depend on both Pierre, but we can depend that offline.
Officials.
**Chris Ventura** 35:20 Yeah, so this one, I think…
Someone was gonna follow up with, Robert internally.
To get a better idea about…
What exactly the ask is?
**Piotr Kiełkowicz** 35:39 No, I didn't check with Robert, to be honest. I can put it on…
I… make a note for myself.
**Chris Ventura** 36:00 Yeah, cause if it's just a nice-to-have…
Given the complexities, it might make sense to put it with VNEXT.
**Piotr Kiełkowicz** 36:09 I agree that for now we can put it in next, and I will check with Robert what he really thinks about this.
And another important topic about the stability of Marking instrumentation as stable.
**Chris Ventura** 36:29 Yes, gosh, I forgot why I created this.
**Piotr Kiełkowicz** 36:36 I think Steve Gordon asked you about this on Slack.
**Chris Ventura** 36:40 Oh, yes, and then we had a discussion about what stable really means, and, what do we need to do in order to declare
Instrumentation is stable within auto instrumentation.
So, is it sufficient to just have… The instrumentation library itself, declared stable.
Or do we need some sort of…
Tests in place to ensure that the instrumentation is backwards compatible as new library versions are released.
So if we think about, let's say, MongoDB, they're working on native instrumentation directly into the MongoDB library itself.
There's not this separate instrumentation library that we can pull in and control which version we ship.
Instead, it's the… customer's MongoDB library itself that they're depending on in their application.
So, do we need tests in place as new versions of the MongoDB library are released to ensure that that instrumentation is following
semantic conventions, appropriately, or do we just need to assume that they're following the semantic conventions? So…
It's about determining what Do we need to have in place to really say that something is stable?
**Piotr Kiełkowicz** 38:27 From our.
**Chris Ventura** 38:27 That's effective.
**Piotr Kiełkowicz** 38:28 I think that in Splunk, we have considered one more parameter.
Yeah, except the stability.
And it is the way how we can control the code.
So, I suppose we potentially could mark the MongoDB in some
Period of time when they declared that it is stable as a state, but…
Mark it, that it is completely out of our control, and it is natively instrumented, and we are just listening on the events.
And… we'll be supporting this as long as the… Library itself is supporting instrumentation.
**Chris Ventura** 39:19 Yeah, that's… that's an interesting approach. So, yeah, this issue is meant as a discussion item.
Where we can decide on what approach we want to take.
In order to… how we want to document the instrumentation.
**Piotr Kiełkowicz** 39:35 So, I know that we have now Weaver or something like this, and we potentially could write some tests and validation.
But I'm not sure if we should do this, because of…
of the scope of the libraries. If the owners of the library decide to break something, it is probably completely up to them.
So… To make it in this way.
**Chris Ventura** 40:08 But is it on us to notify people?
About this.
**Piotr Kiełkowicz** 40:18 That's a good question.
**Chris Ventura** 40:19 That, that we've detected… a difference.
So I think that was part of the discussions.
**Piotr Kiełkowicz** 40:35 So, one more comment here, and one more part. I think MongoDB
is inspired by the OpenTelemetry specification.
Technically, it is still not stale, and… but they decided
And probably we'll merge in this way, that's… they utilize…
Attributes, which are completely not covered by the semantic convention.
And…
In this case, can we mark it as a stable or no? I'm not sure, Chris, to be honest.
**Chris Ventura** 41:16 Right.
And so, if they are following stable semantic conventions… I mean, I don't even know if…
Those conventions have stabilized.
**Piotr Kiełkowicz** 41:31 MongoDB, technically, no. Database part, technically, yes.
**Chris Ventura** 41:38 So, along those lines… I'd lean towards not marking it as stable in that specific case.
**Piotr Kiełkowicz** 41:51 But we have kind of other…
Also, pretty complex example, ISPNet Core.
**Chris Ventura** 41:57 Yeah.
**Piotr Kiełkowicz** 42:00 For… for sure, it is… relies on the state semantic conventions, and… For now.
It is implemented in the instrumentation package.
But… After .NET 11, we probably will be just listening on the SP.NET Core
Diagnostic source and do nothing with… Activities generated by by the .NET itself?
**Chris Ventura** 42:34 But will that cover the baggage changes? Because isn't that still being debated?
**Piotr Kiełkowicz** 42:42 I'm not sure.
Okay. I'm just speaking about the…
**Chris Ventura** 42:47 Oh, no, no, they…
**Piotr Kiełkowicz** 42:48 Activities.
**Chris Ventura** 42:51 Yes. Yeah, on the activity side, Yes, that…
**Piotr Kiełkowicz** 42:56 James merged, kind of.
all activities now provided all attributes mandatory by the semantic conventions.
**Igor Kiselev** 43:08 Really feels for me that…
We… we need to somehow document for each library, that means to… so there is a set of libraries that, we support.
And there is a difference in stability of our auto instrumentation, and stability according to OTEL. And for stability according to hotel, probably we should just share what
What package should provide a guarantee against hotel stability?
And, so it's a question of documentation. If we do, fully in hotel site, if we implement, all activities, paths, and something like that, in that case, we could say if it is, that it is, stable support by open telemetry, including auto-instrumentation, and we can declare it if we have any such libraries. If it is through
instrumentation package, in that case, we should just recommend that, okay, we stable.
auto-instrumentation, but stability of OpenTelemetry itself is defined by that page, and refer to their documentation, what they have. If it is native, once again, we provide that via user native, unless we
plan, in some cases, in future, to say that despite we having support from a native library, we would do some translation, or we would do some adapters to make it improper, non-stat… non…
semantic convention library to talk in the semantic convention on the open telemetry, unless you would plan to do it.
We probably don't need it.
Providing guarantees on our side.
my funeral.
**Chris Ventura** 44:57 So I think to move this issue forward,
we need to at least have some sort of proposal of how we want to approach this. And so, I can try to find the time to…
Write something up in this ticket, and then we can…
Make changes to it, adjust it.
But just to get some opinion out there so that there's something concrete.
I think that'll be easier to move it forward.
**Piotr Kiełkowicz** 45:36 So, I will assign it to you, Chris, right now, yes?
**Chris Ventura** 45:40 Yeah.
**Piotr Kiełkowicz** 45:44 No milestone for now.
I think we can back it to this next week.
Hopefully.
Discussions, especially… That's not like a box.
It's fine.
Sorry, discussions… Our empty…
It was already… sorry, it was already handled, so on the board. I'm not sure if…
I should move on, I think.
**Chris Ventura** 46:34 Was there a specific issue for the no-code changes that you're working on, Pyotr?
**Piotr Kiełkowicz** 46:40 I doubt that there was an issue. It was kind of internal requests.
**Chris Ventura** 46:44 Okay.
**Piotr Kiełkowicz** 46:48 And I think full description is in the…
marked out documents. What… what is it?
**Chris Ventura** 46:56 Yeah.
**Piotr Kiełkowicz** 46:57 It was, right now, implemented.
**Chris Ventura** 46:59 Yeah, I was mostly asking, for the project board.
**Piotr Kiełkowicz** 47:04 Okay.
That's all, I think.
**Chris Ventura** 47:25 Are there any upcoming SDK releases that…
we should be aware of, or changes on the SDK side?
That a Mormon.
**Piotr Kiełkowicz** 47:35 There were one, there were one, issue 6?
Last month… Related to the concurrency issue in logs.
happy, probably, as I remember, but I do not have anything about plans to make the hotfix release for this.
**Chris Ventura** 48:03 Well, that's all I have.
**Piotr Kiełkowicz** 48:07 So, thank you all. See you next week.
**Chris Ventura** 48:09 Let's see how…
**Alexey Pukhov** 48:10 Thank you, see ya.
