SIG: OpenTelemetry C/C++ SIG
Date: 2026-04-20
Duration: 13 minutes
============================================================

## Zoom Recording Transcript

**Marc Alff [MySQL]** 03:56 Hi, Tom.
**Tom Tan** 03:57 Hi, Mark.
Good evening.
**Marc Alff [MySQL]** 04:01 I was just about to cancel a meeting, so thanks for joining.
**Tom Tan** 04:06 Okay.
**Marc Alff [MySQL]** 04:14 cannot attend. He's looking at… he will take a look at PRs and issues.
**Tom Tan** 04:19 Okay.
**Marc Alff [MySQL]** 04:20 You cannot, you cannot join the meeting.
**Tom Tan** 04:22 Yeah, I think Nalid will also not joined today's meeting.
**Marc Alff [MySQL]** 04:26 Okay, great.
Do you see my screen?
**Tom Tan** 04:35 Yeah, I can see your screen.
**Marc Alff [MySQL]** 04:36 Okay, I prepared a couple of notes for… for this week, and also I copy and pasted the… the open questions, open items from last week, as well.
**Tom Tan** 04:48 I see.
Oh, do we plan for a new release?
**Marc Alff [MySQL]** 04:56 I think so, because the next one, the last one was a month ago.
**Tom Tan** 05:00 I figured out.
**Marc Alff [MySQL]** 05:02 And… So, I will be off next week, so I can start to plan it, but, Very likely it will be on the first week of May, I guess.
**Tom Tan** 05:14 Okay.
**Marc Alff [MySQL]** 05:14 I'm on vacation next week.
**Tom Tan** 05:17 Okay, no problem. I think I'm not aware of any fixes need to be released very soon, so… Good from my side.
**Marc Alff [MySQL]** 05:33 One thing we need to… Prefixes this one.
It's the security issue that was found in Go as well.
I agree.
We don't have a fix yet anyway, so we need…
**Tom Tan** 05:47 Yeah, the issue, I may be, I've… What is it?
**Marc Alff [MySQL]** 05:50 Let's see… This one?
When we send to an endpoint, we get an answer, a reply.
**Tom Tan** 06:15 I see.
**Marc Alff [MySQL]** 06:16 P, auto memory.
**Tom Tan** 06:18 Goodbye.
**Marc Alff [MySQL]** 06:19 Yes, and… If we are talking to a corrupted endpoint, the endpoint may reply with a huge reply.
And in that case, we just try to allocate memory to represent it without question, so, It may, it may cause an out-of-memory allocation on the server itself.
**Tom Tan** 06:43 Yeah, makes sense. I think I read this issue.
**Marc Alff [MySQL]** 06:48 And so, the… the security issue for Go is public, so, Everyone knows about it, so I guess we need to fix it as well.
**Tom Tan** 06:57 Yeah, I think so.
Are you this one? Like, maybe we can ask for help, or… doesn't it sound…
**Marc Alff [MySQL]** 07:05 So that…
**Tom Tan** 07:06 a big issue. Yeah.
**Marc Alff [MySQL]** 07:08 So, I don't think it's a big issue, because For a problem to… To show up, you need to talk to a compromised system in the first place, so… It's… there is another issue to get there.
But for our business, we should do it.
Yeah. And someone expressed interest of, in fixing that, and Nadit replied as well already, so…
**Tom Tan** 07:31 I see, okay.
I think I missed the updates there. Yeah, thanks.
**Marc Alff [MySQL]** 07:36 Yeah, we just… basically, we need to… To truncate very apply to a given size.
**Tom Tan** 07:42 Yes. Definitely.
Okay, looks good.
**Marc Alff [MySQL]** 07:49 Okay.
So, yeah, otherwise, I have a question, you may know, because the… the story of this thing, there is something called plugin.
In OpenTelemetry.
**Tom Tan** 08:08 Inc.
I think I don't have full context on this one. It was there, I think, from the very beginning.
**Marc Alff [MySQL]** 08:17 Oh, it's very old, and I haven't.
**Tom Tan** 08:19 Yeah.
**Marc Alff [MySQL]** 08:20 it's used anywhere. So, yeah, this thing… In my understanding, it's, it is very old code that was there.
**Tom Tan** 08:31 Yeah, I'm not aware of anyone is using that to…
**Marc Alff [MySQL]** 08:37 Yeah, it's also… go ahead. Yeah, it's not doing anything by itself, so it's, I think it was meant as a framework to later load, exporter DLL, things like that, or exporter shared memory.
The shed library, sorry.
**Tom Tan** 08:54 Okay, well, I think.
**Marc Alff [MySQL]** 08:55 I've never used.
**Tom Tan** 08:57 This is even… came before the DLL thing, and and when I added the DL thing, I think I… Didn't consider using these, so… yeah.
**Marc Alff [MySQL]** 09:08 Yeah, it's very old.
**Tom Tan** 09:10 Yeah.
**Marc Alff [MySQL]** 09:12 So, I know.
**Tom Tan** 09:13 Yeah, this doesn't conform to the… or not specified in the spec, right, also.
**Marc Alff [MySQL]** 09:18 No, it's massive.
**Tom Tan** 09:19 That's only.
**Marc Alff [MySQL]** 09:20 It's totally outside of spec. It's something that was added, So, it is not used at all, so I think we can just remove it.
Once or twice.
**Tom Tan** 09:33 So, yeah.
**Marc Alff [MySQL]** 09:34 of opinions on that. Okay.
**Tom Tan** 09:37 Yeah.
Yeah, feel free to reach PR, I'm not sure.
maybe Lalita could have more… more context on this, but I think it should be fine to remove it.
**Marc Alff [MySQL]** 09:52 Okay.
Yeah, so I will OPR, and we can… we can have some comments there if need be.
**Tom Tan** 09:59 Thanks.
**Marc Alff [MySQL]** 10:03 Do get a question on… so, OpenTelemetro Porto has a version 10?
And we are not using it yet.
And there was a question on When we can agree to that.
Sorry. And we are missing… for this thing to be available in Bazel, we are missing… something on… a module on Bazel Central Repository, so…
**Tom Tan** 10:31 Okay.
I saw… It's updating that Bazel?
like, Bazel tools, is that for this?
**Marc Alff [MySQL]** 10:41 no, it's, for… it's something different. But, Keith was, updating Bazel Central Repository earlier, so I guess I can ask him to have, a module for ProTool, and then we can upgrade to that.
**Tom Tan** 10:59 Okay.
Sounds good.
**Marc Alff [MySQL]** 11:08 Okay, I don't have anything else.
I don't… have you noticed the ceiling tidy is really… Getting better and better?
**Tom Tan** 11:18 Yeah, so a lot of PRs on fixing that part.
**Marc Alff [MySQL]** 11:22 Yes. And for you?
**Tom Tan** 11:24 the dark, and yeah.
**Marc Alff [MySQL]** 11:25 Thanks. We started at… yeah, we… so Doug worked a lot on this, and I did some parts as well. We started with more than 600 warnings, so we are from 600 down to 33 now.
**Tom Tan** 11:40 No.
**Marc Alff [MySQL]** 11:40 There's a few, a few left, so…
**Tom Tan** 11:43 Okay.
And from my part, I think I heard there could be a fix on the ETW exporter about the data type issue, but that's… If we… Do we plan to release on May? I think that's… that's good. We will catch that again.
**Marc Alff [MySQL]** 12:04 Okay, sounds good. Yeah, it will be… I think I'll be ready to do that in the first week of May, but not before, anyway.
**Tom Tan** 12:15 Okay.
**Marc Alff [MySQL]** 12:19 Okay, I saw you did a couple of code reviews also for Duke and other PR, so thanks for that.
A lot of them are ready to work, so I will go ahead with… and do that.
Just so you know, I will be off next week, so I will miss the next, the meeting next week, but otherwise, I will be back afterwards.
**Tom Tan** 12:40 Okay, next Wednesday? That's… okay, let's see.
**Marc Alff [MySQL]** 12:43 Yes.
I will send a note on Slack anyway.
**Tom Tan** 12:50 Yeah, okay, that would be great, maybe also put a note here, so… In the calendar.
**Marc Alff [MySQL]** 12:57 Yep.
**Tom Tan** 13:01 Okay.
**Marc Alff [MySQL]** 13:02 Okay, I don't have anything else, I don't know if you have some topics.
**Tom Tan** 13:06 No more topics from my side?
**Marc Alff [MySQL]** 13:08 Okay.
Sounds good, Van. Thanks for joining.
**Tom Tan** 13:13 Enjoy your vacation.
**Marc Alff [MySQL]** 13:15 Yeah, thank you.
Bye now.
**Tom Tan** 13:18 Bye, talk to you later.
**Marc Alff [MySQL]** 13:20 NATO, yes.
**Tom Tan** 13:21 make a lot of sense.
