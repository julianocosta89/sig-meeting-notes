SIG: OpenTelemetry C/C++ SIG
Date: 2025-08-11
Duration: 17 minutes
Zoom Recording URL: https://zoom.us/rec/share/JPt0v1vPV_lsxWV-sF-J55x8qnrXoXCEyawW-i1jGCY0U5-v0i98cKEkedOmCQH4.BHJjZWvmjG9di5VS
============================================================

## Zoom Recording Transcript

**Tom Tan** 04:28 Hello, Nikhail.
**Nikhil Bhatia** 04:33 Oh, really hot.
**Tom Tan** 04:35 Yeah, same scenario, there are no other maintainers will join today's meeting, so I think if… is there any topic from your side, or…?
**Nikhil Bhatia** 04:46 Yeah, actually, so I was, starting to implement, process resource detector, so I had a few questions.
**Tom Tan** 04:56 Okay, so do you have a PR issue open? Maybe we can… put their questions there to give more visibility, yeah, as today, I think no… not so many maintainers joined at the meeting.
**Nikhil Bhatia** 05:10 Okay, so… I was implementing, or I will implement it, More, and then I'll raise a P arrow.
**Tom Tan** 05:19 Okay.
For the current implementation you are doing, I assume there's an issue, right, for it, for tracking?
Right.
**Nikhil Bhatia** 05:32 Awesome.
Can you come back for?
**Tom Tan** 05:39 Or, I mean, for the, for the current, like, what is it, like… Something in the resource, detector, something? Or is there an issue which tracks that feature, or…?
In our repo.
**Nikhil Bhatia** 05:55 No, so there was an issue?
And, also… there was a document which links to that issue.
**Tom Tan** 06:06 Okay.
**Nikhil Bhatia** 06:07 I'll share both.
**Tom Tan** 06:14 Yeah, could you please share the link to the chat?
**Nikhil Bhatia** 06:18 Yeah.
**Tom Tan** 06:19 Yeah, thanks.
Yes, Anne?
**Nikhil Bhatia** 06:34 So, this is the… document which was linked in the picture.
**Tom Tan** 06:53 Okay, I'm opening the link.
Okay.
Process and the process runtime resource.
So, do you mean you are implementing the attributes in this doc?
Yeah. And currently, C++ is not there, right?
process runtimes, and then, yeah, and the selected process attributes. I think C++, we don't have a runtime.
**Nikhil Bhatia** 07:23 Yeah, we don't have one.
**Tom Tan** 07:25 Yeah.
**Nikhil Bhatia** 07:26 The other attributes, that's upset, to… In the previous meeting, they said that we… … The below one is the issue.
Who's hidden.
**Tom Tan** 07:45 Okay, the second one?
Issue… okay, Mark opened the issue.
Resources, LucasVac… People….
**Lalit** 08:00 Are you hearing something?
**Tom Tan** 08:02 I'm not here, I mean….
**Lalit** 08:04 Okay, okay, great.
Hey, hi, Nikhil. Hi, Ahsan.
**Nikhil Bhatia** 08:10 Hi, Lou.
**Ehsan** 08:16 Hi.
**Tom Tan** 08:20 Okay, let me… Share my screen, then, on this issue.
Hmm… Okay, let me know if you can see my screen.
**Nikhil Bhatia** 08:42 Yep.
I can see.
**Tom Tan** 08:45 Okay, or… Nope.
Resource detector, this one is completely red, or the second link is shared?
**Nikhil Bhatia** 08:57 Actually, … Some more is left, because only the pass… it is only intermittent fast, maybe, like.
Only the container part is implemented.
Okay.
**Tom Tan** 09:11 So is that some part missing in the PR, like….
**Nikhil Bhatia** 09:16 Actually, I broke down the PR, I was thinking, like, … I will implement it in parts.
**Tom Tan** 09:24 Or implemented in part 2, you mean? The remaining one, remaining attributes?
Okay, or any comments on Lalit or Yohsan on this?
**Lalit** 09:41 No, I think we've… this looks good, right? I mean, the container resource… … Detector has already been merged, and… The other ones, Nickel, you'll be raising a PR for that, and we'll be reviewing it.
**Nikhil Bhatia** 09:57 Yep.
So, I was having some questions related to.
**Lalit** 10:01 Yeah, please go ahead.
**Nikhil Bhatia** 10:03 Yeah, yeah. So, … The process, this was detected,
**Lalit** 10:09 Nikki, your voice is not very audible to me, at least. I'm not sure for others, but….
**Tom Tan** 10:15 Yeah, same.
**Lalit** 10:17 Clear.
**Nikhil Bhatia** 10:18 Oh… Let me just increase… Can you hear me now?
**Lalit** 10:24 Yeah, slightly better, yeah, let's see.
**Nikhil Bhatia** 10:26 Yeah, so, … In the… in the document, Which is that… I shared it in the chat, actually, the first one.
So, in that, the process detectors, yeah, this one.
So, it's only said that we need to only implement it for, … Windows and, limits-based operating systems. So, there is nowhere mentioned of Darwin-based operating systems.
So, I think I'm good to continue with Only these two implementations, right?
**Lalit** 11:04 So, where is it written? Like, it should be only for Windows, and… Linux, ….
**Nikhil Bhatia** 11:12 Can you go a little more?
Yep.
Oh, dear.
**Tom Tan** 11:22 Should also work on Windows, right?
**Nikhil Bhatia** 11:26 We have Windows and Linux.
**Lalit** 11:32 Yeah, so then we need to implement only for these two.
It should be okay, I mean, afterwards, if the specs changes to include… Darwin or, you know, I mean, Mac or something, like, then probably we can always extend it further.
**Nikhil Bhatia** 11:51 Yeah.
**Tom Tan** 11:53 So, right now, if this is built for non-Windows and non-Linux, maybe we… we can emit an error, right? Compilation error, and see, not implemented for now.
**Lalit** 12:08 Yeah, we'll, we'll… just skip the build… I mean, right now, for container also, you'll be doing the similar thing, like, you want… it would be only being built for… Oh, in container… in case of container, we are calling it from inside the Docker container, right? All these APIs.
**Nikhil Bhatia** 12:24 Yep.
**Lalit** 12:25 Okay, yeah, so there, there, this scenario is not valid, yeah. So then we should not be… yeah, if it is not Windows and Lane, then probably we should not be… Or the CMake file should just ignore, I mean, conditional, it should be conditional compilation in the CMake.
**Nikhil Bhatia** 12:45 Actually, I was also thinking on this, that How can we compare it for various targets? Target machines?
**Lalit** 12:55 Okay, I mean….
**Nikhil Bhatia** 12:57 So, now, I have implemented it a little bit. So, for Windows, what I'll be doing… is I will include Windows-specific directories, like, for example.
there is an attribute of process.pa.
So, what I'll be doing is, I will include process.hedge, like, for example.
I'll try, I'll share my screen.
Yeah, so I was… Implementing it, something like this, like.
If I have a Microsoft version defined, then I'll include… include this process, and to, … so, Get PID is different for, Microsoft version and Linux.
So, in Linux, it's just get PID, but in Microsoft version, it is, like.
underscore git period, so I'm also defining it here, and… then I'm trying to do something.
**Lalit** 14:01 Yeah, this should be okay. I think we are doing a similar thing, I think, in lots of other places also, using iftiff.
MSS… MSC version, so… I think just… just follow that pattern, which we are doing in other places for cross-com… cross-platform builds.
**Nikhil Bhatia** 14:18 Yeah, sure.
**Lalit** 14:20 Yeah.
**Nikhil Bhatia** 14:23 And also, just another small… No, I think? So… PID, we usually write it as PID underscore T, but here, I have written it in 32T because, like, If you see the… Resource and the source attributes.
How do you have to do that?
**Lalit** 14:46 Yeah, it should be okay. I got your point here. It should be fine here.
**Nikhil Bhatia** 14:52 That's it.
Pretty much.
**Lalit** 15:00 Yeah, that should be okay, I think. More of these things, I think we can… we can do it, do once the PR is there, we can review it there.
**Tom Tan** 15:17 Okay, any more questions on this, this issue?
**Nikhil Bhatia** 15:21 Oh, God.
I'm done with my question.
**Tom Tan** 15:27 Okay, thank you, Mikhil and Led.
Okay, any other topics?
**Lalit** 15:41 No, Ahsan and Tom, I just… … I mean, I created one group on Slack for the maintainers, and I just posted some, some, some, … Some points there. I mean, just reply if you have any concerns on that.
**Tom Tan** 16:00 Okay, alright, we'll take a look.
**Lalit** 16:02 That's on Slack, yeah.
**Tom Tan** 16:08 Okay, if no other topics, I think we can end today's meeting early, and we'll have our next meeting the next Wednesday.
**Lalit** 16:16 Nikhil, you're from India, right? I mean, it would be very late at this time.
**Nikhil Bhatia** 16:20 Yo.
**Lalit** 16:23 You can, I mean, I think you can always post on, on the discussion channel on GitHub. I mean, need not… need not join this meeting that late.
I mean, up to you, but I'm just… just saying that if you have to really… Keep awake for that long.
**Nikhil Bhatia** 16:39 Yeah Actually, I was just doing my college project myself.
**Lalit** 16:44 Okay, yeah, mate.
Yeah, thanks, Tom. If nothing else, probably we're good too.
End the meeting.
**Tom Tan** 16:51 Yeah.
**Lalit** 16:52 Thank you.
**Tom Tan** 16:53 Bye.
**Lalit** 16:53 Thank you.
**Nikhil Bhatia** 16:57 Thank you, everyone. Bye.
**Ehsan** 17:00 Thank you, bye.
