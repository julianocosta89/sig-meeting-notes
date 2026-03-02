SIG: .NET Auto-Instr SIG
Date: 2025-09-17
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/KLFPoNWGeinRuSvWs8R0N_1cWqCXpQTIo3SU3TW7mGNcMeC_1c7LPzOMxy5BCIXW.9-DlJp44kLl7TQ4c
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 00:53 Hey Zach, how are you?
**Zach Montoya** 00:56 Doing well, how are ya?
**Piotr Kiełkowicz** 00:57 I'm fine, thanks.
Hello, Corin, today.
**Zach Montoya** 01:04 Yeah? Is anyone else from Swank coming?
**Piotr Kiełkowicz** 01:07 Rasmus should be FAA today, but Mateusz and Evgeny are on PTO still.
**Zach Montoya** 01:17 Well, we'll see.
How are things going from the, the SDK side?
**Piotr Kiełkowicz** 01:33 I've heard that Rush is planning some hotfix release to fix up some gRPC issues.
**Zach Montoya** 01:43 Hmm.
If I…
**Piotr Kiełkowicz** 01:46 Understand correctly yesterday's meeting.
**Zach Montoya** 01:52 Huh.
**Piotr Kiełkowicz** 01:53 Yes, or no?
**Zach Montoya** 01:55 I don't remember…
hearing about the gRPC talk, I remember hearing about the, the versioning policy for everything else. Oh, yeah.
**Piotr Kiełkowicz** 02:08 telemetry gRPC exporter, and there is kind of missing header.
**Zach Montoya** 02:12 Oh, okay. Yeah, I didn't hear about that.
**Piotr Kiełkowicz** 02:16 Okay.
**Zach Montoya** 02:17 Yeah.
But the main one was, I think Martin had a PR, about matching the runtime versions.
Which I think is a good change.
**Piotr Kiełkowicz** 02:28 Yes, exactly.
Also, it is the second grade change, but on the Microsoft side.NET 9 will be longer supported.
**Zach Montoya** 02:37 Yes, yes, I heard that.
That's a good… that's a good change.
**Piotr Kiełkowicz** 02:50 I think we can briefly check what we have.
On the agenda…
Questions? Would you like to share screen, or should I do it?
**Zach Montoya** 03:15 Yeah, I can share screen.
**Piotr Kiełkowicz** 03:17 Right.
**Zach Montoya** 03:22 Yeah, so… we have two in progress.
PRs. The N-Log one, I actually reviewed it yesterday, and I think it's, looked good from our side. There's… there's a couple of small changes, so I haven't approved it yet, but there's a couple small changes, I think.
But after reverting it so that it's just… it's all inside of the instrumentation project now. So if you look at the files now.
It is all just inside our regular audience rotation, which is good. But there's some, like, really small cleanup of things, like, the… this comment with the directory packages.
And then also, the… The author had updated the assembly info.
But that's no longer needed, because we have it all in one package, or one assembly, so some really small things, but design-wise, it looks good, so that's a good thing.
And then we have the file-based configuration. I have not looked at this yet.
**Piotr Kiełkowicz** 04:29 It should be great if you can check.
Yeah.
Your increase or rush.
And it is first step to this fair-based configuration, working step.
**Zach Montoya** 04:41 Okay.
**Piotr Kiełkowicz** 04:43 there is a couple to-dos, but I would like to keep it for follow-ups, because it is not crucial.
And… this PAR attack.
It's still big enough, or too big even.
**Zach Montoya** 04:59 Okay, yeah, I can take a look, but I won't be able to get to it till next week, so if someone beats me to it, then great, otherwise I can take a look sometime next week.
Okay… Issues, so just some more tasks to track for file-based configuration.
Nothing else, though.
I also don't know if there's…
Hold on one sec, let's go to regular issues. Any other comments on things? I haven't seen…
Oh, we have one update on this.
Update 7 hours ago, maybe another follow-up question? Oh, okay.
Okay, I will respond to this,
Igor, had added some new…
a new, like, API for, like, building signatures, which is really, really handy, but, this is probably the first time someone's actually using it besides Igor, so we need to…
Help with this.
So, I'll… I'll provide some feedback on that.
Okay, yeah, those seem to be the only updates, just the new… new issue and then that question, so I'll go back to that later.
What is next?
Zero discussions.
Kind of expected… No issues for this milestone that we need to add to the project.
And then the project board.
So this one… I suppose we can…
We could add the SQL client stuff on here if we want, but,
That's not necessary for 1.13.
Yeah, I don't think… is there anything else you guys wanted to track for this?
This next release.
Okay.
Cool. Does that wrap everything up?
Yeah, that wraps up our regular agenda. Are there any other topics you guys wanted to discuss while we're all here?
**Chris Ventura** 07:37 One thing I'm curious about, Raj, is, how things are looking with the next-gen,
What is it? Out of process, prototyping.
**Rajkumar Rangaraj** 07:53 So Chris, like, we have everything working, as of now with the .NET monitor. The code is in my branch, so, I did not get bandwidth further to take it forward. I was supposed to prepare a presentation for RSIG also here.
So probably that would be the first thing, and then I'll move, in contributing that code to the…
NET monitor space.
**Chris Ventura** 08:21 Yeah, because I remember you saying you had things working, and so I wasn't sure if it had made its way to the .NET Monitor team yet.
**Rajkumar Rangaraj** 08:28 Not yet. I wanted to drive it here before taking it to them.
**Chris Ventura** 08:32 Okay.
**Rajkumar Rangaraj** 08:33 I want to do a small presentation here on what is… how that package being used and everything, and then take it to them.
Yeah, at some point in time, the way we have done this, it's a plug-and-play. It no need to be. Even if we wanted to have our own out-of-process-based executable, I descend it in that way, so it can be easily unpluggable from anywhere.
**Chris Ventura** 09:04 Yeah, and then another thing I was curious about, I think it was, like, a month or two ago, there was some issue reported with the collector not being able to decode
some OTLP payloads from .NET services, and I don't know if the root cause was ever discovered for that.
**Rajkumar Rangaraj** 09:29 Sorry, go ahead.
**Piotr Kiełkowicz** 09:31 fixed in the latest collector release. 133 is affected, 134 is fixed.
But probably there is a space for improvement on .NET Exporter.
To work also on 133, but it is not crucial, in my opinion.
**Rajkumar Rangaraj** 09:51 I think we fixed that. It was that the header, the trialing headers which was missing caused that issue.
that's already, fixed, and we did not release it yet. That's where the discussion is going on, like.
Right now, we want to take a .NET 10 update and do another RC release in that space, like SDK space, but before that, we are still discussing, as this is a critical fix, should we do a hotfix and release it from the
Current one and, move forward.
**Piotr Kiełkowicz** 10:23 I'm pretty sure that there are two separate issues. One is related to GRPC, the second one is for the
Not perfect, or suboptimal… arguments, passing from .NET to the collector.
**Rajkumar Rangaraj** 10:47 there is no issues of such… it's filed in the .NET repo, Pyotr. Like, if you have a knowledge, just grab and create an issue. If there is some gap, we should be covering that up. Anything in the OTLP is a very important thing for every one of us.
So we should have it fixed, like, today, if collector is imported, tomorrow some other service may be impacted because of that.
**Piotr Kiełkowicz** 11:11 Sure, I will double-check with Juan Fre-free tomorrow.
**Rajkumar Rangaraj** 11:15 Yeah.
**Chris Ventura** 11:17 Okay, and then my assumption is.
If changes are made to the .NET exporter, we'll likely have to port those similar changes to our out-of-process next-gen branch.
To, to have similar changes.
At least that's my assumption.
**Rajkumar Rangaraj** 11:37 That's correct.
So right now, like, we are in a very early beta state, like, as peril dashboard, something like that is what we are targeting now. So moment, if it is to the better shape, I think,
We should ensure that all of these known issues, whatever happened after the code copy, we need to track and bring it to the OTLP exporter space.
And that's a good call-out, Chris. Like, we need to keep a tab on what's changing in that space.
**Chris Ventura** 12:18 Yeah, it makes me wonder if there's…
Some sort of abstraction that should be shared between the repos?
Like, is there some sort of shared library that we want to use? I don't know if that's realistic, but it's just a thought.
**Rajkumar Rangaraj** 12:37 From the SDK, if I look as an… if I need to speak as an SDK maintainer, I would say,
it's not the right thing to provide anything apart from the OTLP exporter, because that's what the spec says. Anything apart from that customization, if we need to do something like that, that needs to go and live in the country repo. So, such kind of customization, so…
Nothing…
that should impact the SDK, because it's very stable, and you shouldn't be doing such shareable components from there, based on the principle and the philosophy that's been followed there. Yeah, this is going to be a gap that we are going to have for, like.
**Chris Ventura** 13:16 Between these two repos.
**Zach Montoya** 13:36 Alright, I guess… Anything else, worth discussing at the moment?
Okay, well, say nothing. Seems like, we're good to go.
Yeah, thank you all, and I'll see you next week.
**Rajkumar Rangaraj** 13:56 Sure.
**Piotr Kiełkowicz** 13:56 Thank you, bye.
**Zach Montoya** 13:57 But…
