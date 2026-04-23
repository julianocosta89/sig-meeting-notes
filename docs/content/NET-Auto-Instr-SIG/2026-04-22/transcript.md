SIG: .NET Auto-Instr SIG
Date: 2026-04-22
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/1rpgNkVAtqBQ3wDiYjD0BNv7HqN1qCloqPAdSv4YlTMvXuGdEfbdEIEeCAktwERF.QF8S_Lmv32GDyehq
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 02:36 Hi, guys.
**Igor Kiselev** 02:42 Bye.
**Piotr Kiełkowicz** 02:45 He's like, could you please drive? I mean, the… Office today in the open space, so it is… Hardone to have it today.
**Yevhenii Solomchenko** 03:15 Alright, guys.
**Zach Montoya** 03:39 Get started… Cool, so, let's see, so first thing, 115 stable. Let's talk about that. Is everything already, needed, merged in there?
**Piotr Kiełkowicz** 03:56 I think the last PR.
yeasts… Just finishing, it is updating, kind of.
Internal stuff.
BAM production and internal packages, yes.
**Zach Montoya** 04:09 Oh, I see, this one, okay.
**Piotr Kiełkowicz** 04:10 already revealed by… by Robert, so I think it is good to go.
Except this, so we need to just create… release… earliest PR.
But the preparation takes more time than I expected today, so I didn't finish it before the meeting.
**Zach Montoya** 04:34 Cool.
So this one, once that's good to go, we can get ready for the release.
Cool, I guess we can move on to other PRs. There's a bunch of dependency updates.
We have one for… some NetFX entry point, redirection?
I haven't seen this one yet.
Any comments, or anything that we should, Other viewers to know for this one?
**Igor Kiselev** 05:05 We are still working on… on… on the… So, we are not, I mean that, there, it still fails a build, and, require a little bit more work, so it's pretty close, it already looks nice, but… I'll move work and be required, yeah.
**Alexey Pukhov** 05:27 I need to get the pipeline green.
**Igor Kiselev** 05:28 I haven't…
**Zach Montoya** 05:33 Okay.
Alright, I can follow up on that.
Let's see what else, we have a bunch of draft PRs… I think our stability proposal's still here.
And then we have… Can you…
**Igor Kiselev** 05:51 If anybody would have a time, I would be really appreciative feedback for my, PR4728. It's still… In… draft, but it's very, very close, and I will draft it this week.
So…
**Zach Montoya** 06:09 Cool.
I'll add myself.
Alright.
Then we also have OpAmp is… I don't know if Rasmus is here today, Do we know how this was going, Piacher?
For the opium?
**Piotr Kiełkowicz** 06:36 there is kind of still some features needed to be adjusted on the constrip site, and then we can back to this implementation.
I think Steve Gordon is working mostly on the fixes.
**Zach Montoya** 06:52 Hmm, okay.
**Piotr Kiełkowicz** 06:54 It also includes kind of security improvements.
**Zach Montoya** 07:01 Got it. Okay. Cool.
Are there any other APIs you guys want to discuss at the moment?
**Alexey Pukhov** 07:13 Actually, I wanted to talk about one thing. So this is about the startup hook.
and .NET 11… well, actually, not .NET 11, but Diagnostic Source 11. So we get a reply from the Microsoft, looks like we're not gonna have any Solution for the… Startup hook isolation problem.
when we switch to Diagnostic Source 11 on… .NET runtime slower than 11.
And going forward.
So, which means that… We can only accommodate the workarounds in that case.
which is… Basically, two things.
either customer… Update their dependencies inexplicitly.
set the diagnostic source to whatever we need. Or… and the second workaround, we need to bring back the additional dependencies.
for those customers, who can use that, which is… What, portable applications.
So, probably I will work on bringing back the additional dependencies.
So it's gonna be… An option for the customers to use.
In that case. But yeah, nothing else we can do about the startup hook. At this point. That's the best we can do.
So I have a… oh, sorry.
**Zach Montoya** 08:45 I was just gonna clarify, so that's only needed when we're doing, a… not the… not the new deployment, like, that one's fine, it's just the other deployment of, like, the environment variable, or just setting up the… Dropping the zip-on disk, right?
**Alexey Pukhov** 09:03 Yep, that's gonna be the two environment variables, additional dependencies in the store, the work… the workaround that used to be before my change of the assembly redirection.
Then, how are we gonna approach this? We're probably not gonna bring back the original solution that… Assembles the… libraries in the structure and put them in the distribution. We leverage the existing libraries in Tracer Home, because we do ship them. We just restructure that Tracer home. I mean, basically what I'm thinking about is sort of a tool, either a .NET application, executable, or a PowerShell script.
That will just recreate the additional dependencies set up based on the tracer whom.
files. And you can run it before you start your application. So it's, like, one step before you can use the startup hook.
**Piotr Kiełkowicz** 10:05 If it is needed only for this… diagnostic source, we could kind of make additional… Store available by default in the… into the distribution.
**Alexey Pukhov** 10:18 Good point. I mean, right now, it's just diagnostic source. We never know if it's, like, if any other libraries will be… Will be needed, but I see the point.
**Igor Kiselev** 10:30 If we still use, so, okay, let's say my vision on it would be, it, our solution where we catch, items is not, foolproof. There may be a situation when customer application use, some API that would break the sandbox.
So, that's why it may be, in some rare cases, required not only for, single SDSS, but for other cases, for startup cook-only solution.
Visit, If we still provide that solution, it's better to have a script that would create all required dependencies in a proper place than only one. On top of it, in future, we can give additional ability to the same script, to not build that, startup who… to not build that additional, additional depths folder, but also modify an application config file to update it so that it would be future, foolproof, and it would also work in self-contained applications. So, from my point of view, it's better work with a separate tool to do it.
And with a separate tool, we already discussed with Alexi, we need a feedback what… Shape of a tool would be the best, because we could do it Okay, we could do it a PowerShell script, we could do it a .NET tool.
so .NET executable, or it could be even .NET tool, or if we talk about .NET executable, it could be, if it is not a .NET tool, it could be, released.
in the same archive as Zip, or it could be released as a separate archive, because it's required only in some cases, only for some the edge… Yeah, for startup hook. For example, even for startup hook, you would not need that tool if you run it on .NET… if you run version compiled for .NET 11 or .NET 11.
Oh, yeah.
So it's… that's why it's a question about which shape Or we can return back additional zip files, but I don't like additional files right in there, but I don't like it, because it means, again, that we copy the same zip file multiple times on the customer disk. Okay, disk space is cheap, but… the need of 3 copies of the same file, and it would be in not only as the assessment, it would be all the files that we copied in that folder, so that it would be Microsoft Extension, and it would be A64, ARM, so there would be… More than required, actually, much more than required, and for most of customers who is our Profiler customer, it would… it is not required, even one of it was not required, because for Profiler, we solve it.
**Zach Montoya** 13:45 Okay, yeah, keep us posted, Alexi, as you start to work on that, and we can… You know, discuss and see what the proposal is for, how we're gonna package that.
**Alexey Pukhov** 13:56 Sure, yeah, absolutely.
**Igor Kiselev** 13:59 And we already have an issue for it, where we describe the problems about startup hook, so we could.
**Zach Montoya** 14:06 Yeah.
**Igor Kiselev** 14:06 Use that issue to… Get a collective decision what it should be.
**Zach Montoya** 14:12 Yeah, I think it's.
**Igor Kiselev** 14:15 Yes, the last one. The last one.
**Zach Montoya** 14:17 Oh, it's on.
**Alexey Pukhov** 14:18 I put an update there.
Right into description.
Oh, no, this is a different one.
**Zach Montoya** 14:28 Oh. This one?
**Alexey Pukhov** 14:31 Yeah, it shouldn't be this one. Yeah, the last one, yeah.
**Zach Montoya** 14:33 Two different ones, oh.
**Alexey Pukhov** 14:35 One is for native profiler.
**Zach Montoya** 14:37 Oh, I see, I see.
**Alexey Pukhov** 14:38 So, for the native profiler, we're gonna fix that problem.
But it's just for the startup hook, we have to go with workarounds.
**Zach Montoya** 14:46 Yeah, yeah, the default ALC, yep.
Cool?
Alright.
So, let's see… Close these for now. We went through… The PRs, these were all the non-independent bot ones. Seems like we don't have any… Other ones we want to discuss, unless someone wants to bring one up right now.
Let's see, issues… alright, so we've got a couple… Let's see, so we have… Central package, transitive pinning enabled.
Okay.
This seems pretty… pretty clear-cut.
**Igor Kiselev** 15:32 That may a little bit simplify our upgrades.
If I could just simply give one place on this.
**Zach Montoya** 15:39 Yeah.
Yeah, that'd be super helpful.
Okay, I'm just gonna… Let's see, for Milestone for this one… either 116 or VNEXT, not sure this is very critical, it's just kind of a nice to have.
That's… Let's put this under VNEXT, that's… that's fine.
Rights… Build negative packages… oh.
Okay, also another… Another cleanup here.
Alright, yep, this'll be good.
**Piotr Kiełkowicz** 16:19 Igor, I think you have free work for our pipeline. Is it still needed?
**Igor Kiselev** 16:26 That is in… It's on BuiltMigit packages, so that's the job that I have not touched.
**Piotr Kiełkowicz** 16:34 Okay.
**Igor Kiselev** 16:35 Let's deleted.
Where he'll just, you know.
**Piotr Kiełkowicz** 16:41 So, please put for the 116, I think.
**Igor Kiselev** 16:47 I try to not mix in one pull request, something that is not directly related.
**Piotr Kiełkowicz** 16:53 Sure, just checking… double checking if it is stability.
**Zach Montoya** 16:59 Sounds good.
Next one, Stack Exchange Redis. Oh, wow, is this…
**Piotr Kiełkowicz** 17:05 Better version.
Beta version was released, kind of, a couple days ago.
**Zach Montoya** 17:11 Hmm, okay.
Cool.
Alright, so yeah, we'll need to, test this.
Update our version range, test our integration tests.
**Piotr Kiełkowicz** 17:25 Nope.
**Zach Montoya** 17:29 This could be good for the next one.
**Piotr Kiełkowicz** 17:34 I think so.
**Zach Montoya** 17:37 Alright, I'm gonna be reading this letter.
Okay, so those are all the issues of that milestone.
Last things are open discussions, appears there are none. And then we have for our project board… whoops, I did not want to add something.
We have in progress the redirections… Tests, that's still in progress.
And then we have committed the SDK API to 116.
It is today.
**Piotr Kiełkowicz** 18:09 Not yet. We have released hotfix, but it does not include any important changes in terms of blocks, I think.
It was created for almost lost information about the logs changes in the bridge API.
**Zach Montoya** 18:27 Gotcha. Okay.
And then this ASP.NET Core Hosting Startup Assemblies, is this one?
Is this one in progress? Has anything happened with this one?
Okay, okay, we can leave that for now. I'm just committed.
Okay, I don't see any other updates at the moment that we need to add.
Okay. You guys have any updates you guys would like to see to this?
Alright, so yeah, we'll, keep working on the… the test for the NetFX entry points.
get a release out soon with the, Yeah, it'll get out really soon.
So we get that last PR merged, and yeah, that's kind of what's coming up next.
Anything else that you guys would like to discuss?
Cool. Well, I guess we can wrap for today.
Alrighty. Thanks, everyone. See you next time.
**Alexey Pukhov** 20:08 Thanks.
