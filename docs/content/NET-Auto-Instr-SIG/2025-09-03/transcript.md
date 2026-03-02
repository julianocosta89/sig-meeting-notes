SIG: .NET Auto-Instr SIG
Date: 2025-09-03
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/hxxwdJfoTEMTj3CfxTftXvoUZuJ1jK0Y2ZBb3Ra1bjEDepJdA40aUA5oaNSylT_B.eU8SyugGZIarnK6H
============================================================

## Zoom Recording Transcript

**Mateusz Łach** 01:26 Hello?
**Piotr Kiełkowicz** 02:27 Oh.
**Yevhenii Solomchenko** 02:30 Oh.
**Zach Montoya** 02:31 Hey.
**Piotr Kiełkowicz** 03:08 I think we can start.
Hmm… I don't see any custom.
Points to our agenda, so we can go through for requests, and… Yes, and then issues, and… Transfer the…
for the next work. So, for now…
we have, dependable update and two open and PR related to the underserialization and…
unlock, I think we can check this too.
Zach, I see that you have some…
comment? So, Evgeny, you need to check, and we can probably review it once more time tomorrow, when it is fixed, and…
then merge.
And analog, Zach, also, you have time to review what is the current state of the PR.
**Zach Montoya** 04:19 Yeah, I reviewed it yesterday.
I think, in large part, it looks good. There was one change where the, contributor, had it using, like, only duck typing, and had it inside the library, and then based on some of the comments from SnakeFoot, I don't really know this,
developer, recommended
bringing it out into, like, a separate n-log package, so I added comments to actually say we wanted that to the original form, so I think that that should be fine. It looks like, the original author did that originally, so…
I expect that they'll be able to revert that. But otherwise, the approach looks fine to me.
**Piotr Kiełkowicz** 05:01 I'm not sure if SnakeFoot is not the kind of maintainer, or at least out of unlock right now.
**Zach Montoya** 05:08 Oh, I see.
I didn't look at their, their GitHub profile.
**Piotr Kiełkowicz** 05:14 I was checking a couple weeks ago, so I'm not sure, but…
But it… it can be this case.
**Zach Montoya** 05:23 Yeah. Anyways, I left comments, once those two, like, the… sort of that revert so that structurally it fits into the audio instrumentation and we remove those dependencies, I think it's in a good state.
**Piotr Kiełkowicz** 05:36 Great.
To hear that.
Other parts are kind of blocked and waiting for… for… for this to… to… to move forward.
I hope you have seen that we have released, on Monday, the beta version. Pretty smooth.
No, no issues.
Nourishes.
Well, a lot of them.
Hmm… So…
automate vendoring, it is kind of…
follow-up for what we have done right now. I do not think we need to focus on this right now. I will put it to be next.
And fix it when we need to upgrade the library.
Also, new issue related to macOS. For now, we have support for the Lagasse macOSes, and it is not working, or…
At least, file structure.
Looks like it will be not working on the MacBook Pro.
M1, 2, M4.
From my perspective, it is slow priority if we agree that we can make several releases with
this kind of manual changes done locally and testing on arms.
**Chris Ventura** 07:14 Yeah, we might need to pick this up in a year or so, because I think the Intel Macs are no longer going to be supported, or something along those lines, so that might be something to consider.
**Piotr Kiełkowicz** 07:30 So, not 113, but kind of… one fifth… 14, 15, let's say.
**Chris Ventura** 07:38 Yeah, somewhere in that time… time frame.
Unless, the Mac runner changes in GitHub, and then we need to do something different.
**Piotr Kiełkowicz** 07:53 Sure.
So, it should be fine to fully drop support for x64 and replace it by ARM64.
**Chris Ventura** 08:02 That's my understanding.
**Piotr Kiełkowicz** 08:04 Do you think we can do it right now, or in the future? Because if only replacement, it should be pretty smooth, just switch the…
Runners, and update the… For the tractor?
**Chris Ventura** 08:17 I'm okay with doing a replacement, because I believe the next version of macOS is dropping support for the X64.
**Piotr Kiełkowicz** 09:04 So, I've put it into 1.15. It is early next year, probably.
Or, if needed, earlier.
**Igor Kiselev** 09:15 Oz.
**Piotr Kiełkowicz** 09:18 You go?
**Igor Kiselev** 09:19 I'm just thinking if, is Mark planning to drop a emulator support at all? Because otherwise, it still may be good to support x64 version for some time, as there may be emulated .NET applications that have not been cross-compiled to ARM64.
So…
**Chris Ventura** 09:39 I think the main use case for the macOS support is mostly developer machines. We haven't heard of a production scenario where somebody's running an application that they want instrumented on macOS, other than engineers working on
A Mac Pro.
**Igor Kiselev** 10:02 Inca.
**Chris Ventura** 10:07 And I believe that was the same case for Datadog, if I'm remembering correctly, Zach.
**Zach Montoya** 10:13 Yeah, we don't have any production usage for Mac.
We have, like, yeah, basically limited, like, we have developers using it.
**Piotr Kiełkowicz** 10:23 Same in Splunk, to be honest. I've never heard about any customer running in… On the production side.
Hmm…
It is the issue, the next one. Issue is related to SPNET Core, and we are not replacing controller and action with the values for some cases.
it is issued on the contrip repository, to be honest, but I would like to show you to have an SEO.
And, I don't have time to work on this, as promised last week, but Erasmus will be in touch with Lyudmila to determine if
what to do with… with this case. Still, alan needs to be…
Consultants, what is the plan to…
Or what was the reason for some decisions, especially for conventional routing?
And what we can do to make user experience for our users, but…
So I will open… keep open it for… for one more week.
Mmm… We have a couple related to file-based configuration.
Yes, we have… we already discussed it.
earlier?
Documentation… telemetry…
I think we can add stale label here and close the next week.
Zach, I was discussing it with
The private channel, if you can give some direct recommendation how to start working on this.
It would be great.
Because neither me or him is, kind of, yes.
Ready to pick it up.
**Zach Montoya** 13:08 Yeah, okay, I can, I can add that to the, to the issue.
**Piotr Kiełkowicz** 13:13 Great, thank you.
I think its issue is raised, kind of, 2 months ago, and nobody touched it.
After your comments, Chris.
Would you like to discuss it, or close it, or what is your preference?
In my opinion, the current state is fine.
**Chris Ventura** 13:53 I feel the same way. I'm not sure that we've encountered any scenarios where
We want to test an older version for any particular reason.
**Piotr Kiełkowicz** 14:14 I think we can test it locally with, kind of, vulnerable.
packages.
Is it fine?
I will put the stale label and pink.
Auto.
Yup, I think we have to go through all our new issues.
Discussions… Object.
No… no discussions?
all issues are correctly assigned, and I do not think we need to do anything on the board.
**Chris Ventura** 16:20 So there were some additional feedback provided on the, the… profiling.
let me see if I can find the… the comments.
It happened after we did the release, I believe.
**Mateusz Łach** 16:42 Do you mean the feedback from FTCAR? Related to the shutdown? Yes. Yes, okay, so, yeah, I discussed it briefly with FTCAR, so basically, he mentioned that the current,
Parent solution might not be, like, the most performant, but at the same time, this is, like, fully functional, so…
Yeah, I can look into that before the stable release.
But, yeah, this is more… it is my understanding, this is more of, like, Perf improvement, so…
Unless you think that we… this should have, like, a higher priority?
**Chris Ventura** 17:24 I think it's something to consider before the final release, but if it came in a future release, I think it would make sense, too. I just wanted to ensure that we didn't, lose track of the discussion.
**Mateusz Łach** 17:40 Yeah, so, yeah, sorry, sorry, I discussed it with FTCAR, like, offline, but, didn't, like, update the…
The discussion here.
**Piotr Kiełkowicz** 17:55 I will put 2-1-14, and I sign to you, Matavush.
**Mateusz Łach** 17:59 Okay, thank you.
**Chris Ventura** 18:38 That was the only topic I had to bring up.
I'm gonna drop for another meeting.
**Piotr Kiełkowicz** 18:53 Thank you, I'll see you next week.
**Zach Montoya** 18:55 Alright, see ya, bro.
**Mateusz Łach** 18:58 Thank you, bye-bye.
