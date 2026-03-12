SIG: .NET Auto-Instr SIG
Date: 2026-01-07
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Zach Montoya** 05:28 Hey, everyone.
**Igor Kiselev** 05:36 Oh…
**Alexey Pukhov** 05:38 Hi, Happy New Year to everyone!
**Zach Montoya** 05:41 Yeah, Happy New Year.
**efshaikh** 05:42 Hello, buddy!
**Zach Montoya** 05:49 Let's give it another minute, then, we can… Go ahead with our usual agenda.
**Yevhenii Solomchenko** 05:59 Hey, guys.
**Zach Montoya** 06:09 Alright, yeah, I can, let's see… Cool.
Alright, yeah, I can, go ahead and get started on the agenda.
Alright, so… first, I suppose we can look at the pull requests.
We have a couple open pull requests… let's see… I have some drafts. We have this file-based config one.
For this one… What is the status of this? Is this.
**Yevhenii Solomchenko** 06:47 It's, ready for review.
**Zach Montoya** 06:49 Okay.
Alright, yeah, if this was done 3 weeks ago, I'm sure a lot of us were… were out, so, give some attention to that. Any… anything else that we should know before reviewing?
**Yevhenii Solomchenko** 07:04 Perfect, Bob.
**Zach Montoya** 07:05 Okay. Alright, sounds good.
A couple other ones, document MTLS environment variables, and then enable Rosalind analysis. Yeah, these are all opened in the, Past 3 weeks, so… This one is already approved by a couple of approvers, maintainers.
So, this one should be good to go. And then the other one with Rosal analysis, Piachio's been doing a lot of These good improvements, so… We'll take a look at that, it doesn't seem too complicated.
Alright.
So next, new issues… just close these.
Let's see, so a couple of these we've had for a bit. We have a load exception, another loading diagnostic source.
I don't know if these have any recent activity… Okay, this one's been assigned.
Let's take a look at the diagnostic source one.
Okay we don't have… A minimal reproducible example yet on this one.
Okay.
I'd probably still would recommend that we follow up with this later. I know we have some other work going on right now with… It's loading. .net environment variable conflicts, was this the exporter?
Yes, okay.
So we have some, conflict with the OTLP exporter endpoints.
Did we have a PR that was supposed to address this?
**Chris Ventura** 09:19 So I believe it was retested after those changes, and the problems still persist.
But… we just need somebody to take the time to debug into it, to see what's going on.
**Zach Montoya** 09:31 Gotcha, okay.
Okay, I mean, it looks like we have some good reproduction stats. Anybody have time to… Take a look at this.
Yeah, I'm not sure I'm gonna have time.
Alright, so for now, this will… this will sit here for, until we're able to review this.
So if anyone has an opportunity to take a look, that'd be… that'd be great. I just don't think I'm gonna have time either.
Let's see… addressing some of the conflict challenges, I actually haven't seen this one before.
Looks like this contributor's talking about using assembly load context.
And then Igor also commented.
**Alexey Pukhov** 10:46 Yeah, that's basically… that's me. I file it, so it's basically extending the… thing that we use for .NET Framework, where we do redirection of assembly references, and then since that alone is not gonna work for .NET Core.
Also use of the assembly law context that we also have, but we just don't use it to the full.
extent. So those two things, I believe, will improve the resolution of the conflicts.
Of those assemblies that we do have in hotel, and the customers may have in their own applications.
**Igor Kiselev** 11:28 So, it's a little bit different.
different, it would be… pretty big change to how we currently load, assemblies in .NET… in .NET, because it would not require additional store, but we hope that it would, solve, assembly loading for side-loading us in standalone application, and we also hope that it would help in cases of previous issue when an incorrect version of system diagnostic source has been used.
It's still not absolutely universal solutions. There will be still some cases where.
**Alexey Pukhov** 12:10 limitations.
**Igor Kiselev** 12:11 Yeah, limitations, but it probably would work better and for more customers than the current solution works.
**Zach Montoya** 12:22 I see, so what was the, sorry, I haven't had a chance to read through this. The proposed solution would… Would we be just loading in a separate assembly load context for, for our dependencies?
**Alexey Pukhov** 12:39 This is for the, like, for the profiler solution, so if the profiler is involved, we can use the assembly reference redirection. So, just like for the .NET Framework, where we change the assembly reference redirection. That alone is not going to work for .NET Core, unlike .NET Framework.
So that's why we'll have to… on top of that, we'll have to use the custom SMBLOT context.
To actually load those assemblies, too.
When resolving them.
But the non-profiler solution, when there is only a startup hook involved, that's not gonna work, since there's no profiler. So there, we are thinking about loading the customer application into a separate assembly load context, because by default.
The customer application loads in the default context, and there is no way we can… interfere in how the dependencies of the customer applications are resolved. But if we load it to the custom context, we have more control over how to resolve the dependencies of the customer application if they are conflicting with our dependency… with hotel dependencies.
**Zach Montoya** 13:50 Got it.
**Alexey Pukhov** 13:51 So again, this is not a foolproof solution, there will be limitations, but we believe it's gonna work better than the current one.
**Zach Montoya** 14:01 I see, yeah, it seems like a pretty big change. Yep. Is there, any… And, like, I would suppose the next step would be to… try and POC this with… An example.
**Alexey Pukhov** 14:17 We did a quick prototype for the profiler solution, just for the, actually, system diagnostic source.
assembly. That worked well, so what we want to do is actually extend it to all assemblies and see how it works. Chris also mentioned that there was another attempt, and there was problems with the tests, so that's something we also want to look at.
And for the startup, solution, also kind of get a… I only had a check for the sandbox application, not with the hotel project, but just to try out how it works.
I did a quick sandbox application. I mean, it worked.
But you never know when you try to apply it to the hotel project. So again, we'll have to make a proper POC and then see how it's gonna work.
**Igor Kiselev** 15:06 And there would be a lot of discussion of what specific… check we should do, what types of applications we should validate, probably some discussion about what current solution… what issues current solution tried to solve, and do a specific check for that issue, and so on. It would be a lot of work here.
**Alexey Pukhov** 15:29 See, just to start that thing, it… Maybe it's not gonna fly.
But at least trying.
**Zach Montoya** 15:41 Okay, so, for this case… Yeah, there's… potentially a good amount of work that we can do on this.
I think that the proving out… so the profiler, like, proving out the system diagnostic source.
Example is good.
and then extending that to all the assemblies, would be a good next step. And then after that, I think we could probably come back to this issue and, we can try to document the different cases that we need to cover, with this solution, or what… What existing ones we are seeing, and if this can address those or not.
**Alexey Pukhov** 16:28 Sounds good. Yeah, by the next week, I'll have some… something for the profiler.
**Zach Montoya** 16:34 Okay.
**Alexey Pukhov** 16:38 Thank you!
**Zach Montoya** 16:42 Damn… Bing… Dean.
So let's do that.
Cool, thank you.
And then the last one is immediately releases, I'm not sure… I haven't seen this one, pietro, do you have… I guess this is just a different way to publish a release.
certainly seems fine to make these immunables, just like our NuGet releases are.
**Piotr Kiełkowicz** 17:51 So, the only difference that's… When the release is published, there is no possibility to add or modify or remove anything from artifacts.
So, it is kind of… GitHub.
Ensure us that when it already was published, it will be there forever.
**Zach Montoya** 18:14 Yeah, I mean, I don't know that we've updated Contents in the past.
I guess the only concern would be if we had a bad… a pretty bad bug where we had to do a patch release, and then just… Mark, like, tell users, like, don't download this.
**Piotr Kiełkowicz** 18:35 There is a possibility to modify the description, always.
**Zach Montoya** 18:38 Oh, okay.
Okay.
**Piotr Kiełkowicz** 18:42 Yeah, in that case, then…
**Zach Montoya** 18:44 I'm not terribly worried as long as we're able to, yeah, do a prompt like patch fix, and then just update a release if we have a catastrophic bug to warn users to just update to latest instead of a particular immutable release.
Are there any… Any other… any objections or any other thoughts on… Trying to enable immutable releases.
Okay.
Well, well.
**Piotr Kiełkowicz** 19:22 ask… I will ask Trask to enable it, because it is kind of manual.
action needed. There is no possibility to have it by Terraform yet.
**Zach Montoya** 19:45 Do you think I'll mind if I, tag him on this?
**Piotr Kiełkowicz** 19:48 Yeah, it's fine.
**Zach Montoya** 19:51 Okay.
Okay… Okay, so that's all of our open issues.
Let's see… discussions… I don't anticipate there's anything… yep.
I think we're on 14 now.
Okay, nothing… Oh, sorry, let me actually just create a new, Oh, you've already done that, thank you.
Okay… Oh, yeah.
Second… Alright, and then the last one is reviewing the project board.
So… for this next release, are there any… Things that we're trying to… Any work we're trying to complete, in order to get out the next release?
**Igor Kiselev** 21:10 So, I created a, currently draft pull request, that we see. So, first, I believe that, NetFix Dependency redirection already fails in pretty few cases, especially when we have, With a previous fix to load, assembly optimization with single domain.
It still may, in some… pretty exotic cases. Fail, I believe.
And, I prepared an alternative solution for it. It may work better in some cases and worse in other cases. So instead of using a single domain flag, we use, we generate, assembly… web config or app config building redirection, on the fly when updomain is created. So, pull request is finished in terms that I do not plan to do anything in… change any structure, or do any additional features in current pull request.
But I'd like to add a few units there, and that's why it have not yet been marked as ready for review. But…
**Zach Montoya** 22:29 I see, okay.
**Igor Kiselev** 22:30 Implement assembly redirection, yes.
It probably would.
With that, we probably would be able to close that issue and say that we hope that in most cases, asunder redirection is not failed.
**Zach Montoya** 22:51 Got it, okay .
**Piotr Kiełkowicz** 22:55 And before the next release, we probably need to wait for the SDK release.
There is a security issue related to certificate validation.
Rash, I think you were reviewing the fix already?
**Rajkumar Rangaraj** 23:18 Which one, Pierlo?
**Piotr Kiełkowicz** 23:20 The security issue related to certificate validation on the OTRP exporter.
**Rajkumar Rangaraj** 23:27 Yeah, there is a small… bug I figured out in that, so I'm still reviewing that part.
**Piotr Kiełkowicz** 23:35 Okay.
**Zach Montoya** 23:39 So is the plan, so when that, when that release is made, as soon as that's made, we'll publish a release with the updated SDK, and then… Basically, this, NetFX, like, assembly redirect isn't gonna block the release.
Or do we want to combine those changes into one release?
**Piotr Kiełkowicz** 24:01 If possible, combine. If not, I think… It is not… there is no new issue on, this .NET redirections, so we can still… Shift the release now, and then move follow-ups if needed, or when needed.
**Zach Montoya** 24:21 Okay.
Alright, any other items, in progress we should, document here.
**Piotr Kiełkowicz** 24:35 I think that we need to… the Splunk, or Cisco, whatever, needs to implement, core WCF instrumentation. Technically, it is… Technically, the latest version is supporting Activity sources, and we need to listen on.
on the activities, but I'm not sure if the propagation is working there correctly.
**Zach Montoya** 25:02 Mmm, okay.
**Piotr Kiełkowicz** 25:03 So, it may not be so trivial.
**Zach Montoya** 25:09 Gotcha, okay. Do we have any, So right now, I'm assuming our only instrumentation for WCF is the Net Framework.
Version, and nothing else.
**Piotr Kiełkowicz** 25:20 We are supporting, WCF Client both on… Oh, right.
M.NET Framework, and… server-side only on the .NET framework.
**Zach Montoya** 25:33 Right, so it's… so Core WCF is the new… NET server implementation.
Okay.
Any other updates?
Alright, see nothing? Let's close that.
Alright, I don't see any other topics here.
So, unless we have, any last-minute discussion topics, looks like we're done for today.
**Piotr Kiełkowicz** 26:16 Thank you.
**Zach Montoya** 26:16 Alright, thanks everyone.
**Alexey Pukhov** 26:20 Thanks, bye!
**Rhynier** 26:21 Bye, guys.
**Mateusz Łach** 26:26 Thank you, bye.
