SIG: .NET Auto-Instr SIG
Date: 2026-04-08
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**efshaikh** 01:36 I see.
**Alexey Pukhov** 01:39 Hey, FD car, how are you?
**efshaikh** 01:42 All good, all good. How are you?
**Alexey Pukhov** 01:45 I'm good.
**efshaikh** 01:47 Looks like that snapshot is keeping you too busy.
But…
**Alexey Pukhov** 01:51 Oh.
**efshaikh** 01:52 Yeah, don't worry about it, profiler side, I will handle.
**Alexey Pukhov** 01:56 Hold on, FTCR, I don't think we should discuss that in this meeting.
**efshaikh** 02:03 There's nobody joined yet.
**Alexey Pukhov** 02:05 Oh, I mean, it's still recorded.
**efshaikh** 02:07 Dope!
Yeah.
Thank you for.
**Alexey Pukhov** 02:15 No worries.
**Zach Montoya** 03:29 Hey, everyone!
**Igor Kiselev** 03:32 Bye.
**Alexey Pukhov** 03:33 Bye.
Good morning.
**Zach Montoya** 03:48 Alright, I'll just go ahead and get started, and people can catch up as we, as they come in.
So I'll drive this and share my screen… Alright, so you should be able to see it. Do you let me know if you have any… other, sort of, things you want to talk about on the agenda today, besides our regular, schedule. Let me just check up on this issue that we had last time really quick, because we were waiting for this to be merged. Okay, yep.
It's all merged. So, with that, it looks like we are probably in a position now to… Release the beta.
But let's go through the rest of these first.
Alright, so, pull requests… Looks like there's one fix here.
That's ready for review.
**Igor Kiselev** 04:48 I would do a review, so my worry was, that, So, per my knowledge in our internal product, starting up very early, may affect iSpanet application, so I would like to look at So that, it's, as I suggested, move a startup, from, application entry point to assembly load event.
I'm not sure if the save assembly load event happens or not on iOS, because there is a little bit different how first up domain and secondary updomain are loaded. If it would happen on iOS, it may be not the proper way. If it will not.
great, it's, probably will solve all issues, but what also confused me a little bit, we was not able to start, IIS tests.
And it was the most interesting part here, and it looks like we have not, was not able to start it due to some, end-to-end, infrastructure issues, like Dockers, Kubernetes says that it is a deprecated way to run it, or something like that, so that's why it's a little bit on hold, but I would look and trade.
**Zach Montoya** 06:08 Okay.
Let's see, when was this original issue reported? This was a while ago, right? Yeah.
**Igor Kiselev** 06:16 Sure.
**Zach Montoya** 06:16 Okay, haha.
Do you think that this blocks us from doing an RC release?
**Igor Kiselev** 06:23 No, no, that was an issue that was… With us for years, so if nobody except us complained about it, it… Probably not too critical.
**Zach Montoya** 06:36 Okay. Yeah, I just want to make sure that, none of the work that we just did to do the redirection caused, like, a regression of any sort, so…
**Igor Kiselev** 06:43 No, that's… that's unrelated to… that's in the same field, but it is in .NET Framework and not .NET Core, so it's a completely different path.
**Zach Montoya** 06:55 Okay, great. So, yeah, we can continue to take a look at this offline. I'll also take a look as well, and yeah, we'll just, we'll continue on that.
Outside this call.
There's other ones in draft. I'm not sure if you guys have any ones that you want to discuss or share right now.
**Alexey Pukhov** 07:18 I mean, none of my drafts are ready, so.
**Zach Montoya** 07:20 From…
**Alexey Pukhov** 07:21 me.
You can skip them.
**Zach Montoya** 07:25 Alright.
Sounds good, we can skip over that for now.
Issue, ASP.NET Core Hosting Startup Assembly… I'm not sure, did we make any progress on this?
**Igor Kiselev** 07:39 once again, it's on me. I said that I would do some more investigation, I would comment on it, and so the decision right now, it's not a real issue, it's mostly a discussion point, if we can do it better, because it is not hurting anybody, and that And with making it better, the main reason… the main goal is to not make it worse.
**Zach Montoya** 08:02 Got it. Okay.
Alright, we'll just keep that one open as is.
Let's see, there was a discussion open several weeks ago, No progress on that. That's okay.
**Igor Kiselev** 08:20 By the way, is that the type of issue that may be solved in a better release with Alex Exchange?
**Zach Montoya** 08:26 Yeah, yeah, that makes sense, yeah, because this one's on .NET 8.
**Igor Kiselev** 08:29 If it is a ZIP installation, if it is NuGet installation, we probably would not change necessarily should be solved later.
**Zach Montoya** 08:36 Mmm, so… Okay.
**Igor Kiselev** 08:38 Loris.
**Zach Montoya** 08:39 Okay.
Sounds good.
No other issues. I see… Alright, well, I guess we're now on the project board part part of this discussion.
**Igor Kiselev** 08:49 by the way, by the way, can we… we probably should update a template for issue, for quiz and other things, the asking customer to report on which installation they are, on Zip or on NuGet, because the types of issue would be Similar, but different, and the solution would also be different.
Cool.
**Zach Montoya** 09:14 Okay.
Yeah, we have runtime environment, but yeah, we could easily describe if they're deploying with the NuGet installation or Zip or MSA. Okay, good idea.
I will create an issue so that I can update the bug report.
**Igor Kiselev** 09:32 Okay, thank you, thank you a lot!
It would simplify a lot of investigation of such things, and it would result in much less asking for, okay, can you describe on which particular installation you are, or trying to… or even for guesswork?
**Zach Montoya** 09:49 Yeah, actually, you know, this seems like overkill, I'll just, I'll just do PR.
**Igor Kiselev** 09:53 Okay, thank you, thank you, awesome.
**Zach Montoya** 09:54 Great. Okay, yeah, I mean, the last thing on our regular agenda, is going through the project board.
Let's see, we have NetFX, that one… It's like, for the NetFX one, there's the approach for dealing with that, so we can leave this one open.
I still…
**Igor Kiselev** 10:23 I really like to understand, I would talk with people who, you know, take it separately. I'd really like to understand what's really left Because my belief, we solved most of problems already, but… maybe I'm missing something, so…
**Zach Montoya** 10:42 Yeah, I think, I mean, if we get to the bottom of that other PR, understanding the setup and… Checking if that's, maybe there's some misconfiguration, but if we can confirm that we have solved, that issue, like, maybe we can be able to resolve this, because, yeah, the NetFX and the core runtimes, now we have the redirections in place.
Minus the, what.NET 11 issues we're gonna have, but…
**Igor Kiselev** 11:07 It's not a fix, it means that it is about .NET Framework, so… and on .NET Framework, that was my previous change, I believe the most of problems was secondary domains, and that I probably already fitted, so I… I will try to reproduce it again, I'm not yet sure, and validate if we already fixed it.
**Zach Montoya** 11:30 Okay.
**Igor Kiselev** 11:30 Maybe next.
Not next week, but next few weeks.
**Zach Montoya** 11:36 Yeah, it'd be pretty cool if we were able to confirm and kind of resolve this.
Yes. Some of the conflict for .NET.
**Igor Kiselev** 11:51 Now we probably solved it, because Alexis changed merch, so we… It varies…
**Alexey Pukhov** 11:59 Yeah, I have a lot of follow-ups. I don't know, should I create separate tickets for the follow-ups? I keep just… Mentioning the same ticket there.
**Zach Montoya** 12:09 Yeah, I mean, if you have an idea right now of what, like, the concrete things that you need to do, you could just, like.
List them as, like, small sub-issues, and then once we… once all of those ones are merged, then we can close this out.
**Alexey Pukhov** 12:24 Yeah, sure, yeah. I'm still kind of walking through the list of unfinished things from the main PR. I'm kind of halfway through.
Then I'll just pause the whole summary of things.
**Igor Kiselev** 12:36 Could you, in that case, probably post here that there is… Resolved through that commit, and then.
**Alexey Pukhov** 12:46 Okay.
**Igor Kiselev** 12:46 But we can… left it open for freaking…
**Alexey Pukhov** 12:50 follow-ups. Got it.
**Igor Kiselev** 12:52 Make easier for everybody else to understand which state it is.
**Alexey Pukhov** 12:58 Yep, yep, yep, good point. I'll do that.
**Zach Montoya** 13:02 Perfect, thank you.
A ClassDK update, I'm not sure they have updated yet.
I suppose they haven't, so this is open. Okay.
Yeah, that's still open, and we'll address that when it gets there. Okay.
I don't see any other updates we need to make at the moment.
For this release.
So I guess we're… I guess we're good here.
Alright. So, do you guys have any other topics you wanted to discuss right now?
Alright, well, thanks everyone, yeah, I'll catch you guys next time.
**Igor Kiselev** 14:00 Goodbye.
**Alexey Pukhov** 14:01 Thank you.
**Zach Montoya** 14:02 Thanks, everyone.
**Alexey Pukhov** 14:03 Aye.
