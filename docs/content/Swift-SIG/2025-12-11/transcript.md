SIG: Swift SIG
Date: 2025-12-11
Duration: 12 minutes
============================================================

## Zoom Recording Transcript

**Bryce Buchanan** 01:42 Hi, Natural.
**nacho** 01:49 Hello, Bryce, how are you?
**Bryce Buchanan** 01:51 Oh, I'm okay, I've got a little bit of a cold.
**nacho** 01:55 Yeah, you sound like that. Yeah.
Excellent.
**Bryce Buchanan** 02:53 Okay, let me share my screen.
**nacho** 04:02 Excellent.
**Bryce Buchanan** 04:25 I think it's gonna be a light day today, so we can… we can get started.
**nacho** 04:31 Yep.
**Bryce Buchanan** 04:33 Alright, so, let's see, topics from last week. So, found a solution for this… what is this?
Ari, okay, I think Ari is working on this right now, It looks like there's still some… Oh, but yeah, he's… yeah, he's working on that, okay.
But he's not gonna be able to make it today. I think he said he'll have a PR out for that soon.
Okay, then Swift 6 updates… Okay, that's good to know.
Cool.
Okay, so that looks like that might be ready to merge.
I can take a closer look at that after the meeting.
**nacho** 05:53 Yeah.
Yeah, I reviewed that.
Last week, I asked for some changes.
Because it… some of the tests were not testing what we wanted, but yeah, for the rest, it looks good for me, and I think… I'm not sure, I think Ari said he was gonna try to build with that. Did you try that in your… I have no.
I mean, I have no products now.
**Bryce Buchanan** 06:19 I haven't had a chance to look at it, so I'll give that a try.
**nacho** 06:22 Yeah, it will be… Just to see if you can build, normally, your standard flow with it.
Yeah. So… so we don't break our users, but…
**Bryce Buchanan** 06:33 Yeah, I don't have…
**nacho** 06:35 reaper now. I mean, I… I don't use OpenDeremity for my daily tasks anymore.
**Bryce Buchanan** 06:45 Right, right. Okay.
Cool. Alright, so B, you have a monotonic clock issue here. It can go backwards.
Unacceptable.
**Bee Klimt** 07:00 Yeah, there… it turns out there's two problems. So, we've been noticing timestamps or durations that are basically Uint64 max, or close to it.
And I found two problems here. One is… so originally… it looks like originally the code for the monotonic clock was copied from Android's anchored clock and used in 64s and kept track of nanos, which would have been fine.
**Bryce Buchanan** 07:24 At some point, there was a big change to change everything to use the date type.
**Bee Klimt** 07:28 And I think that was a mistake for this particular monotonic clock, because the date can go backwards and is also.
**Bryce Buchanan** 07:36 Right.
**Bee Klimt** 07:36 high precision. And so I'd like to change that.
I also found that… there's a helper function that's used a lot that's timeinterval.to nanoseconds, and it converts to UNT64, and if… if anything would overflow or underflow, it converts it to int max, so if you pass in a small negative duration, you get Uint64 max, and I think, like, it would be safe and more correct to change that to int64, the sign type.
But I, you know, I wanted to ask for feedback before I did that, because this means a lot of little changes throughout the codebase.
**nacho** 08:20 Yeah, I can't say I'm guilty, probably, for that.
For, yeah, for the initial implementation and the change to date, because it was, like, Yeah, something easy for the users to use, but… Yeah, that's totally true.
I, I have been reading, yeah, they, they… the issue I changed… I… I am probably guilty of everything in… in… in your issue, so yeah, It was done because… using date… Was a natural way.
or doing things on iOS, if you want to set time, and you want to… so… That was the… the reason for changing to that. So it was easier for the users, but it's true that, yeah, as you… Proof there, it has several issues with that So, I agree with the change totally. The only thing is… Yeah, how… To make that easy for users to set dates when they have to.
**Bee Klimt** 09:33 I…
**nacho** 09:33 In a… in a safe way. That's my only concern.
**Bee Klimt** 09:37 Yeah, I think I can just change the internals of the monotonic clock. It has a getter for a date type, and it has a getter for nanoseconds as an int64. Are you int64?
This… changing the internals will make the nano time more correct, but we can still convert to date and lose a little precision if they call the getter for a date. I think that's fine.
**nacho** 09:59 Okay, yeah, then, then, then that's perfect. I mean, yeah, Yeah, if it was done bad, it was for… being more comfortable for the users, of the library.
**Bee Klimt** 10:11 I looked at your change, and, like, it was reasonable change. In most places, it was, like, changing places where people would call it, and it totally made sense. It was just the internals of this one class, and that totally makes, you know, it's a totally reasonable change to make, but, like, it just kind of messed up the accuracy.
**nacho** 10:30 Yeah, yeah, totally.
**Bryce Buchanan** 10:31 reservation I really have is about, The time interval 2 nanos returning a assigned value.
I understand that there's a… there's an issue where it, is calculating as a negative number, but, can we prevent that from happening so that… because the… the idea that… that this should always be a… like, an interval should always be positive, right?
**Bee Klimt** 10:59 Wow.
**Bryce Buchanan** 11:00 Boom.
**Bee Klimt** 11:01 No, I mean, you can imagine, like, durations of span should always be positive, but, like, a time interval is what you get if you subtract, like, now from the reference date, or vice versa. So when you're doing time math, negative time intervals are perfectly fine. Like, negative one day from now just means one day ago.
**Bryce Buchanan** 11:18 Okay, that's fair.
And that's just a, okay, so that's a feature of the time interval, itself, not the… okay, yeah, sorry. I was, thinking that we were talking about, like, the time interval coming out of the clock, but… Okay.
**Bee Klimt** 11:35 That, yeah, okay, okay, okay, okay. I see, I see what's happening. Yeah, and by making the monotonic clock actually monotonic, we won't get negative time intervals.
**Bryce Buchanan** 11:43 So, the two nanosecion, sec… or the 2 nanoseconds is a, is an extension that we added to time interval.
**Bee Klimt** 11:51 Yeah.
**Bryce Buchanan** 11:52 Oh, okay, okay, okay, okay, I see, I see.
Alright, yeah, that's fine then.
**Bee Klimt** 11:58 Cool, I will make that change and send the PR before the next meeting.
**Bryce Buchanan** 12:03 Grooving. That's awesome. Thank you.
**nacho** 12:05 Yep.
**Bryce Buchanan** 12:09 All right. I just rolled a release for all the changes that have been coming through, so, it's 2.3.0. It looks like that was approved, so I'll get that merged and set up some release notes for that.
**nacho** 12:26 Okay.
**Bryce Buchanan** 12:28 Alright, any… anything else? I'm not feeling well, so I wanna… Wanna go?
Alright, cool. Short and sweet today. I'll, see you all later, then.
**Bee Klimt** 12:44 Thank you.
**nacho** 12:45 Have a nice weekend.
Yeah, you too.
