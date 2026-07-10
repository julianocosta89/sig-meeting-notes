SIG: Go SIG
Date: 2026-07-09
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:30 Hey, Brian.
**Bryan Boreham** 00:32 There.
**Tyler** 00:34 How's it going.
**Bryan Boreham** 00:37 Oh.
Okay, it's a little hot here. Well, like, you know, for the… we're not used to it.
**Tyler** 00:46 Right? Yeah.
That's what Robert was saying as well for polling.
**Bryan Boreham** 01:00 Nobody has air conditioning. So I'm out in the garden right now trying to, which is still pretty hot.
**Tyler** 01:06 Hahaha.
Yeah, that doesn't sound great. I… yeah, I can't stand that. And you guys, I'm guessing, don't have, AC, right?
**Bryan Boreham** 01:18 Right, yeah.
**Tyler** 01:19 Yeah, yeah.
**Bryan Boreham** 01:20 I mean, the offices do, but I'm working from home, so…
**Tyler** 01:24 Yeah, yeah, yeah.
Is there any… Hope that the weather's gonna break there, or is it just, like, the next few weeks gonna be like this?
**Pellared** 02:04 Hello?
**Bryan Boreham** 02:07 Hello.
**Tyler** 02:13 I think it broke for Robert, right? What's your weather, Robert?
**Pellared** 02:19 Sunny, sometimes rainy, like normal.
**Tyler** 02:22 Not 100 degrees, or 40 degrees, yeah.
**Pellared** 02:26 No, no, it's very good, it's normal.
**Tyler** 02:29 Oh, okay.
**Pellared** 02:30 Two degrees.
Brian was just.
**Tyler** 02:33 Brian was saying it was quite hot there still.
**Pellared** 02:36 Still?
**Bryan Boreham** 02:37 supposed to be…
**Pellared** 02:38 Okay.
**Bryan Boreham** 02:38 Yeah.
Yeah, until, like, Monday. Supposed to get a little cooler on Monday.
**Pellared** 02:45 I think I saw some forecasts that right now Poland is one of the coolest places in Europe.
Okay.
**Tyler** 03:04 Cool. I'm looking at the meeting notes. Doesn't look like there's too much there. If you haven't yet, go ahead and add your name to it, and Yeah, I mean, I guess we can just get started here. Robert, it looks like you were looking for review requests?
**Pellared** 03:19 Yep, that's basically it.
**Tyler** 03:22 Okay.
**Pellared** 03:35 So I saw, Tyler, that you reviewed the one that I created, I think, today.
All of them. Some of them, I think.
were the 1st one from the bottom. No, I think the 2 ones from the bottom were probably approved by David Ashpole, and I think the one in the and the 1st from the bottom, I think, was not approved by anyone.
And you can see even the statuses, review required, et cetera. But all of them, if they're approved, they're all only approved by one person, by you or David. So it's a little bit different.
**Tyler** 04:10 Yeah, I.
**Pellared** 04:10 Oh, indeed.
**Tyler** 04:13 Umm.
Yeah, this, yeah, it's looking.
**Pellared** 04:19 Taylor, that you wanted to discuss, or not really.
**Tyler** 04:24 No.
Okay.
Yeah, just haven't got to look at these. Some of these, some of these are the ones I did, yeah.
But yeah, I mean, I'll try to try to finish up here.
Looking at these.
**Pellared** 04:38 The first from the bottom?
It's quite big, but I… the 3rd one, and… or maybe even this one is not that bad.
I think this one has, like.
Yeah, this one is not that bad. I remember that the third one from the bottom is… I think it was larger.
Yeah, this one, because I was like finding issues, issues and issues. And I just decided that all of them are kind of connected to each other. And I just decided to have it in one Pr. Even if you later decide to split it up, I think it's better to at least have a look.
At all of these things together, how… how… how… Like, the whole proposed changes, because it basically changes, kind of, the whole pipeline of shutting down.
**Tyler** 05:32 It changes the pipeline for shutting down?
**Pellared** 05:34 I will say that right now, after these changes, if shutdown is called.
then any further processors, it will call the processors shutdown, and it will not allow calling any other methods on the processors after the shutdown is called on the provider. So if one… everything will just go to no operation.
any forced flashes, any emits, etc. I think in the current implementation, if you shut down the provider, you can still emit, call emit, etc.
which.
**Tyler** 06:04 Oh…
**Pellared** 06:05 So this one, this one kind of… changes in multiple levels. First, on the provider, I think also some changes on the processor level also updates the comments to clarify that shutdown will not be called more than once.
Et cetera.
**Tyler** 06:21 Mmh Yeah, yeah, I'd have to look at it. But yeah.
**Pellared** 06:27 Yes.
**Tyler** 06:28 Okay, sounds good. Yeah.
Well, cool, yeah, That sounds, yeah, I'll try to prioritize that afterwards. Looks like, Puneet, you're also looking for reviews?
**Puneet Singh** 06:46 These are the continuation from the last week. I think, some of them you left some comments regarding some final touches, which are addressed, so would appreciate one more look.
**Tyler** 06:58 Yes.
Still.
**Puneet Singh** 07:07 These are the detector.
PS later to detector migration.
**Tyler** 07:11 Okay.
What's going on here?
links. Yeah, okay.
**Puneet Singh** 07:19 I think this has to do with the absence of the GoDoc link, which is not yet created, because the detector, is new, or, or, you know, that, that link didn't exist before, actually.
**Tyler** 07:36 Yeah. Yeah, I it looks like they all have approvals. Is it just waiting on me?
**Puneet Singh** 07:44 I think so.
Or Robert, maybe.
**Tyler** 07:48 Oh, oh, okay, it's just another, yeah, another, owner or maintainer, okay.
**Puneet Singh** 07:53 Yep.
**Tyler** 07:54 I gotcha.
This looks like it's actually ready.
**Puneet Singh** 08:02 Job.
**Tyler** 08:03 Yeah, this one, let's merge this.
Oh.
Yeah.
**Pellared** 08:10 Yes, we can mer.
**Tyler** 08:11 Oh, wait a minute. Oh, no, we're in contrib. Okay.
**Pellared** 08:15 Okay.
**Tyler** 08:16 Yes.
Okay.
And then, yeah, this one as well.
Okay, yeah, just needs more reviews at this point, it looks like, so, okay.
Yep.
add it to the list.
Hopefully, after the end of the meeting, yeah.
Cool, alright, yep.
Awesome. Yeah, any other… Things people had that aren't on the agenda I see David's also just joined.
**David Ashpole** 08:50 Yep, hey. I don't think I have anything for the agenda, though.
**Tyler** 08:55 Cool. Alright. Do you have any Prs? We need to review.
**David Ashpole** 09:00 I was just looking yesterday.
I think the main one is the… SyncMap exponential histogram one still.
And there was one for runtime.
metrics.
The histogram bucket one.
**Tyler** 09:23 Yeah, let's see.
**David Ashpole** 09:26 Use per bucket count for histogram sum.
Oh, and there's a flaky test fix.
**Tyler** 09:34 They're all in Go.
And.
**David Ashpole** 09:36 So there's 2 in GoContrib, and then just the useSync.map, for exponential histogram aggregations.
**Tyler** 09:45 Okay.
**David Ashpole** 09:48 And then use time unbiased algorithm for histogram reservoir is the other one in OpenTelemetry Go.
**Tyler** 09:56 Okay.
Okay, cool. Yeah, yeah, these don't have any reviews, so other folks on the call as well, please take a look. Looks like these have had reviews already.
I'm guessing you're just looking for a.
**David Ashpole** 10:16 Yeah, I think most of them need a second.
Yeah, the contrib ones aren't that crazy, they're just…
**Tyler** 10:30 This actually looks…
**David Ashpole** 10:32 Yes.
**Tyler** 10:32 Good, right? Alex is a code owner here, right?
**David Ashpole** 10:36 Or does that count? Okay.
**Tyler** 10:38 Yeah, yeah.
**David Ashpole** 10:39 If it counts, I will… Not bother anyone else, then. Yeah, you can hit it.
**Tyler** 10:44 Yeah, alright, sure, I'll hit This one.
I don't think. Yeah, okay, I think this one needs another.
Same here.
Okay.
Well, cool, yeah, alright It looks like there's just… more review work needed.
Actually, I think this is me. Yeah, I guess unless Sam jumps on.
But, okay, cool, yeah, we'll… That's the rest of my day.
I got a bunch of stuff for OB2 to review. So yeah. Well, cool. All right. Yeah, that sounds good.
I mean, if that's the case, we could probably end early then, and we can… Get back to reviewing.
Awesome. Alright, everybody.
I've seen you. All right, bye.
**Pellared** 11:36 Thank you.
