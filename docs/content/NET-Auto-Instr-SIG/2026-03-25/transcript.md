SIG: .NET Auto-Instr SIG
Date: 2026-03-25
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/wejdb4m9GE1JcgpGDLXXm2VliS7BBBC0YF5h48iXcnorIyaSDTLi79YKwjvP3kA8.6Z6fxutaohsPmYrR
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 01:50 Hi, guys.
**Igor Kiselev** 01:56 Right?
**Alexey Pukhov** 01:57 I…
**Zach Montoya** 02:00 Hello.
**Piotr Kiełkowicz** 02:09 Zach, can you drive meeting today? I have some issues with computer, and it freezes from time to time.
Yep.
**Zach Montoya** 02:16 Can do.
**Yevhenii Solomchenko** 02:18 Nice.
**Zach Montoya** 02:33 Alright, so… Alright, I'll just get started.
So, going through our normal agenda, we have a… handful of PRs, Looks like, Piacho just opened up some bico instrumentation.
Anything we need to discuss there, just… Take a look.
I'm sorry, I can't hear you.
**Piotr Kiełkowicz** 03:30 Yeah, I admitted, sorry.
One important information, I don't is kind of fallback instrumentation, and I've disabled it for all known types covered by other instrumentation, so Oracle… MDA will be… will be not covered by this. The same for SQL clients, etc.
So, it is kind of last chance instrumentation, in my opinion, for… 444… for database, abnormet.
Stop.
**Zach Montoya** 04:15 Okay, sounds good.
Alright, I can give that a review offline.
Allocation sampling.
**Yevhenii Solomchenko** 04:27 Issue for the location sampling could start, it offers overflow of the buffer, So…
**Zach Montoya** 04:35 Okay.
**Piotr Kiełkowicz** 04:37 So, historically, we were trying to take all first, I think.
200 allocations, very first allocations in the first seconds, and… Then it kind of is more or less even.
In the time, so we just try to avoid the peak in the startup.
**Zach Montoya** 05:04 Got it. Okay.
Sounds good.
Let's see, so we have a couple of drafts. I'll skip over those unless, anyone wants to call them out.
we have the release attestation.
work. This one, I actually haven't reviewed this yet.
And then NetFX native stack, XS export, okay. Yeah, that'll be important.
For the stack I'm winning.
So, for this one, we just have… we have files that, trying to attest that their… their origin, so I suppose that's… We could take a look offline.
**Piotr Kiełkowicz** 05:52 I think you can… you can omit this until the contributor fix the… issue.
**Zach Montoya** 06:01 Okay.
**Piotr Kiełkowicz** 06:02 Because it is kind of… It is… it should do what… what I expected, but it seems they agree.
Great. Done.
**Zach Montoya** 06:13 Alright, sounds good. And then for the native, I'd say 6, supports… this one, I know that this was a little quite involved in terms of looking up the, doing the stack and winding and whatnot, so, This one we'll just need to review.
Of the native profiler. So I can… I can try to review this as well.
Oh, and then we have the instrumentation Stability Proposal. Is Chris here? Yes, Any updates on this, or how this work is going?
**Chris Ventura** 06:57 No updates, it's there, it's ready for review.
It looks like in the, spec PR related to this, There's some notes in there about auto-instrumentation, and instrumentation stability, and so I think that this is in alignment with that current PR.
So, feel free to take a look.
**Zach Montoya** 07:27 I think I saw a, a blog post, I don't know if it was a spec or a blog post, maybe, like, 2 or 3 weeks ago, that was talking about stability, and that for instrumentations, there's sort of a separation between instrumentation stability and semantic stability, so… For us, it seems like we align with the instrumentation one, where the bits are there.
Production-ready, but the semantics of the signals we generate, that one kind of operates on a different sort of.
**Chris Ventura** 07:57 Yeah.
**Zach Montoya** 07:57 for your support.
**Chris Ventura** 07:58 So, so that blog post kicks off the ideas that they're using?
**Zach Montoya** 08:02 Yep.
**Chris Ventura** 08:03 And then the spec PR's trying to put that… In more specific terms for all of the different SIGs.
**Zach Montoya** 08:11 I see.
**Chris Ventura** 08:12 And so there's a lot more details, there's a lot more things that they're looking at, including nuances like performance and all of that.
So it's kind of blowing up into a much bigger thing.
So, it's just something to keep an eye on.
**Zach Montoya** 08:32 Would you mind adding a link to that particular spec PR in here?
**Chris Ventura** 08:36 It's in the related issue, if I remember right.
**Zach Montoya** 08:41 Related issue… wait, what am I?
**Chris Ventura** 08:43 So, if you go to the Resolves link.
**Zach Montoya** 08:46 Oh, okay, from the original one…
**Chris Ventura** 08:50 And then they were posted.
**Zach Montoya** 08:52 Oh, this one right here. Okay, I see, I see.
Wait, that's not it. Oh, no, no.
**Chris Ventura** 08:57 igor, shared it.
**Zach Montoya** 09:05 Okay, so the stability proposal, okay.
I see.
**Piotr Kiełkowicz** 09:12 It is blog post, but it is one more thing.
this book.
There is one more thing.
**Chris Ventura** 09:25 the second line.
Oh, one more line.
Oh, no.
**Zach Montoya** 09:29 Oh, sorry, sorry. I'll scroll all the way back up.
**Chris Ventura** 09:34 In the comment… there were two links, if I remember right.
**Zach Montoya** 09:40 Oh, thanks. I thought they were one link.
Okay.
And so.
**Chris Ventura** 09:47 This is part of it, and… Maybe we don't have the direct link to the, did the spec change?
**Zach Montoya** 09:58 Yeah, I'm assuming it's a PR on… on the spec repo.
**Chris Ventura** 10:02 Yeah, it is a PR in the spec repo.
Yeah, I'll get the link added.
**Piotr Kiełkowicz** 10:14 Post it to the chat.
**Zach Montoya** 10:16 Oh, okay.
Alright, okay.
Oh, yeah, stale by default, okay.
Yeah, I have seen this, okay.
Yeah, if we could just… if we could just link it directly…
**Chris Ventura** 10:34 Yeah.
**Zach Montoya** 10:34 help.
**Chris Ventura** 10:35 Yeah, I'll get that changed after this.
**Zach Montoya** 10:37 Okay, perfect.
And then these last three all have to do with, work starting from the Assembly conflict resolution.
For this one, for the, .NET store assembly version conflicts.
How is that going? Are there any blockers, or…
**Alexey Pukhov** 11:02 Wow, huh?
With a great pleasure, I can say that it's finally working!
**Zach Montoya** 11:09 Awesome.
**Alexey Pukhov** 11:10 It's been a journey. So yeah, the last thing that I did to make it finally work is more aggressive isolation for the startup hook only.
that way we could contain the set of assemblies that will be in default context, and the discrepancy between Mac OS and other platforms we were able to fix.
So at this point, I just need to finish two manual checks, that I have.
On my pull request. And… there are some comments from Copilot, mostly typos.
And one false positive, so that I'll address too.
And… That should be it.
**Zach Montoya** 11:54 Great, yeah, I'll take a look. I've been following… I think I'm up to date as of maybe… since… like, last week? So…
**Alexey Pukhov** 12:07 Dance.
**Zach Montoya** 12:07 Like, the diff should be smaller.
**Alexey Pukhov** 12:09 Yeah, since the refactor of isolation. Yeah, if you have anything, guys, for the refactor of isolation, let me know. I mean, it was… a bit of a work in progress, I'll be still polishing some of the things there.
So… Yeah.
**Zach Montoya** 12:26 Right?
Yeah, we'll keep a… please, take a look at this, guys, when you can. Hopefully we can get this merged soon.
**Alexey Pukhov** 12:36 Oh yeah, and one thing, the documentation failing for me, I don't understand why. Like, the error is a little cryptic.
**Zach Montoya** 12:46 Markdown, link check… Is this not a…
**Alexey Pukhov** 12:54 I'm not even touching this.
**Piotr Kiełkowicz** 12:56 So, physically.
**Zach Montoya** 12:58 Go on a date.
**Piotr Kiełkowicz** 13:00 We have kind of cache used in the documentation validation, and… If some pages is failing, it is kind of keeping this cache issue for some time, I'm not sure how long.
**Alexey Pukhov** 13:17 Does that mean that this page actually exists, and that's what's failing the cache?
**Piotr Kiełkowicz** 13:22 Yes, and just ignore this issue.
**Alexey Pukhov** 13:27 Okay.
I'll do.
Thanks, and yeah, the other, thanks. I actually moved the… fix in the application to draft, because I'm not actually actively working on it. I'll be working on it after I finish the main pull request. That's a simple change, but I just haven't had time to contribute, so I just moved it to draft.
**Zach Montoya** 13:55 Sounds good.
Alright, any other, PRs that you guys want to discuss right now?
Alright, let's continue on.
Let's see. So, issues… That have been open recently. Let's see, so… You've opened issues to check each of these work, and then updating the SDK API to 1.16.
Oh, when… did that get released yet, or is that.
**Piotr Kiełkowicz** 14:30 It is kind of placeholder just to do not forget about this issue, because there is ongoing activity to… Huh.
fix or extend LOC's bridge API, and we have kind of Dark magic used.
This scope, so we need to adjust to this changes.
**Zach Montoya** 14:53 Okay.
Great. Let me just actually… let's add this to our projects.
Nobody gets reflected there.
Wood.
**Chris Ventura** 15:05 Probably need it also on the milestone.
I assumed that it would be probably the next release?
**Piotr Kiełkowicz** 15:14 16… I dabbed, to be honest.
**Chris Ventura** 15:18 Okay.
**Piotr Kiełkowicz** 15:19 I would create 1.16. I can do it just after the meeting for tomorrow.
**Zach Montoya** 15:25 Okay.
We can…
**Piotr Kiełkowicz** 15:27 Expect to our patch release.
**Zach Montoya** 15:32 Maybe not.
**Piotr Kiełkowicz** 15:32 That's really nice.
**Zach Montoya** 15:35 Oh, sorry.
I'll scratch this.
**Piotr Kiełkowicz** 15:38 So, some requests, but not the minor one.
**Zach Montoya** 15:47 Sounds good.
Alright… That is… okay, that's that one.
Okay. Oh, we actually have a discussion. Looks like Pyatra responded… Transportation fails, done at 8… Likely assembly version conflict… Because it cannot load file or assembly.
Has to do with diagnostic source, okay.
So, this'll be a known issue.
And we'll just keep tabs on this.
I guess it would be good, If, once we merge, the assembly redirects, we could see if this user's setup, is supported. But for now, there's not really a repro or anything for us to just work off of, so…
**Alexey Pukhov** 16:49 Yeah, I think that should be fixed.
**Piotr Kiełkowicz** 16:54 It looks like a typical scenario where they are directly on indirectly referencing diagnostic source in the lower version.10OL.
**Zach Montoya** 17:10 Yeah.
**Igor Kiselev** 17:10 If they use zip for Hive, and after it sees change, such issue should be automatically resolved. If they use NuGet.
In that case, it's still their responsibility to make it, but it should show a var and message in the compilation time.
**Zach Montoya** 17:34 Do they use… wait, wait… I'm guessing that they're relying on NuGet… 10.0.
**Igor Kiselev** 17:42 It's not specified in issue, so I don't know. Maybe it is Nugget, and maybe it is zip archive.
**Zach Montoya** 17:48 Yeah.
**Igor Kiselev** 17:48 Oh.
**Alexey Pukhov** 17:54 Yeah, there we should take care in our new assembly resolution.
**Zach Montoya** 18:00 Okay, we'll slow this as is for now.
Not sure there's much more for us to add at the moment.
Okay. I think this seems to be updated to 15… Okay, nothing on this milestone.
Let me just go update this… And then, lastly, we have our project board.
So in progress, we have the… net effects, redirections, spycode instrumentation for DB command, committed logging libraries for popular logging.
**Piotr Kiełkowicz** 18:48 I think it is no longer committed, to be honest. We have two implementations, and… Nobody's working on the… Lost one.
**Zach Montoya** 18:57 Okay.
Let's add the SDK updates, just to committed.
Is this not the same? Assembly conflicts?
**Alexey Pukhov** 19:13 Yeah, this is the ticket I created for the pull request.
I don't know, do we need to put it in Committed, or…
**Zach Montoya** 19:22 I'll put this… I'll put this in progress.
Does that make sense?
**Alexey Pukhov** 19:25 Thank you.
**Zach Montoya** 19:31 I think this issue over here has to do with ASP.NET Core.
Okay, we haven't really resolved this. Okay.
Alright, so this looks up-to-date.
So yeah, I think that's… I think I sucker for now.
Any other changes?
Alright.
Well, that is our regular agenda. Are there any other topics, anything you guys want to discuss while we're all here?
**Piotr Kiełkowicz** 20:21 Jas, maybe comments when… kind of instrumentation and Alexis PR land, it would be great to make a… Release.
**Zach Montoya** 20:35 Sounds good to me.
**Piotr Kiełkowicz** 20:35 I suppose a lot of customers will be happier, at least on the Splunk side.
**Zach Montoya** 20:41 For sure, for sure.
Yeah, let's do that.
Alright, well, I guess we can wrap early today.
Alright, thanks everyone for your time.
**Piotr Kiełkowicz** 20:54 Sue.
**Zach Montoya** 20:54 Tennesaw?
**Yevhenii Solomchenko** 20:56 Yeah.
**Alexey Pukhov** 20:59 Bye.
