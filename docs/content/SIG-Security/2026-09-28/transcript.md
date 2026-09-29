SIG: SIG Security
Date: 2026-09-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Reiley Yang (Microsoft Corporation)** 01:09 Hey, Trask.
Morning.
**Trask Stalnaker (Microsoft Corporation)** 01:15 Good morning, Reilly.
**Reiley Yang (Microsoft Corporation)** 01:23 Let me share my screen.
incident.
**Trask Stalnaker (Microsoft Corporation)** 01:30 Yep.
**Reiley Yang (Microsoft Corporation)** 01:33 Yeah, I saw you also made a lot of, like, improvements on the… AI… Injection, prompt injection, those things.
**Trask Stalnaker (Microsoft Corporation)** 01:44 Oh, yeah, yeah, it'll be interesting to see if that actually catches anything.
**Reiley Yang (Microsoft Corporation)** 01:48 Yeah.
But still, I feel this is not, like.
rocket science. This is, like, more like a best effort thing.
**Trask Stalnaker (Microsoft Corporation)** 01:58 Yeah.
**Reiley Yang (Microsoft Corporation)** 01:59 Hey, Jonathan.
**Jonathon Klobucar** 02:01 Hello!
**Reiley Yang (Microsoft Corporation)** 02:07 Okay, so I have one topic. I'm not sure if Trask wants to talk about his exploration, but let's just jump into the topic here. So this PR, about setting different levels, I think I got a lot of, reviews and feedback.
The problem is, there's always going to be, like, what's the right bar? And I think the two outstanding comments, like, when I look at this, the first one is always about, like, how many days. So, there has two parts. One is… Is that a business day, or is that a day? And I still want to, like, have a strong pushback on business day, because I think business is hard to define. Like, it's totally up to where you're coming from, and I searched some of the CNCS projects when they say business days. I don't see clarity there. Like, it could be the business day in France, or… people are literally gone for 2 months, right? So, I… I'll explain my position. The second part is the number of Base, whether it's business or it's a real… like this. I think people want to negotiate for a reasonable bar. So, for that part, I don't have a strong opinion. I think whatever bar we define, I'm good as long as we have a bar, and based on the situation, we can try to increase the bar. And if the bar is too low, that everyone meets the bar, then it's a good time for us to increase the bar.
I don't feel too passionate about, like, fighting on the numbers. Then, the second major feedback, I think that was from Jack, so basically, about the… the term we use. So instead of using, like, low, medium. Jack mentioned something like this.
I totally understand why he wants to do this, so I kind of, like, like this idea, but before I… before I make the change, I just want to get additional feedback, because I think this is very subjective.
I just don't want to change based on one single feedback, then I got 3 feedbacks saying you should revert that.
And I want to make those changes, before tomorrow morning, so I can bring this back to the maintainers again.
That's it. So I'm, like, more like, this is a subjective thing, I'm waiting for more feedback, I'm trying to find a reasonable balance.
**Trask Stalnaker (Microsoft Corporation)** 04:32 What does low, medium, high today, what's the term… are you saying, like, expectation, or…
**Reiley Yang (Microsoft Corporation)** 04:44 Yeah, so we're… we're just saying… Low expectations.
**Trask Stalnaker (Microsoft Corporation)** 04:47 Oh, yes, yes, low expectations.
**Reiley Yang (Microsoft Corporation)** 04:50 It might be an English thing, so people feel like, no, we don't want to have a low expectation.
**Trask Stalnaker (Microsoft Corporation)** 04:55 I, I…
**Reiley Yang (Microsoft Corporation)** 04:56 month.
Yeah, so this is, like, much nicer English words, I think.
**Trask Stalnaker (Microsoft Corporation)** 05:01 Standard… Transportation…
**Reiley Yang (Microsoft Corporation)** 05:16 Yeah, so if you feel like…
**Jonathon Klobucar** 05:17 I would say instead of elevated, I would call it trusted.
Like, probably, but… I think… I think the words are fine either way.
I get where people are like, I don't like saying low expectation, like, this isn't quite high school, but, like, I get it, like, it sounds maybe derogatory.
undeclared is probably not the correct word. I would say it's like, It's almost experimental, or like… It's, it's, just my last name, which is at Klobucar.
B-U-C-A-R-K-L-O-B-U…
**Reiley Yang (Microsoft Corporation)** 06:03 Anyways, I'll fix that later.
**Jonathon Klobucar** 06:05 Yeah, yeah, yeah.
We'll get it. I can… if you send me… the link's right there, I can go grab it, and I can comment.
I'll do that. I'll do that right after this meeting.
**Trask Stalnaker (Microsoft Corporation)** 06:14 Maybe.
**Jonathon Klobucar** 06:15 Forget.
**Trask Stalnaker (Microsoft Corporation)** 06:16 Maybe expectation is the wrong word.
**Jonathon Klobucar** 06:19 Yeah.
Posture?
**Trask Stalnaker (Microsoft Corporation)** 06:21 Low, medium, high.
**Jonathon Klobucar** 06:23 Like, usually for security programs, I call it, like, you know, like, the data posture, right?
Or, like, something posture, so it's, like, low posture, medium posture, high posture.
**Trask Stalnaker (Microsoft Corporation)** 06:36 Guarantee… Yeah.
Yeah.
That's my… Yeah, posture, or guarantee, or some word.
**Jonathon Klobucar** 06:53 Yeah.
**Reiley Yang (Microsoft Corporation)** 06:57 We're talking about a topic which I'm not good at.
**Trask Stalnaker (Microsoft Corporation)** 07:00 Yeah.
**Reiley Yang (Microsoft Corporation)** 07:01 He's an English speaker.
**Jonathon Klobucar** 07:02 No worries, and also.
**Trask Stalnaker (Microsoft Corporation)** 07:04 I.
**Jonathon Klobucar** 07:05 People have feelings that aren't particular about this kind of stuff. They don't… they'll ascribe a lot of things, like.
My project has low expectations that might even work on it. It's like, that's not what it's declaring, but I understand your, your, you know.
Your feelings on it.
**Trask Stalnaker (Microsoft Corporation)** 07:24 Security… something.
**Jonathon Klobucar** 07:27 there.
**Reiley Yang (Microsoft Corporation)** 07:30 Yeah, so I… I do have a concern about trusted, so if we change this elevated to trusted, it sounds like… Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:38 Other ones aren't trusted.
**Reiley Yang (Microsoft Corporation)** 07:39 Others are not trusted.
**Jonathon Klobucar** 07:41 Yeah.
**Reiley Yang (Microsoft Corporation)** 07:41 Elevated might not be trusted by people who have even higher bar. So I think I'm trying to avoid a booing value.
**Jonathon Klobucar** 07:49 Yeah, I think I think low, medium, high posture probably solves our guarantees, solve like solve some of this. Like Well, we can… I can suggest that in the repo, and be like, hey, I think there's the issue, and write up something kind of nice to be like, I understand.
**Reiley Yang (Microsoft Corporation)** 08:15 Okay.
**Jonathon Klobucar** 08:16 And so then it's like, like things like, you know, JavaScript and probably Java and other major languages should probably like strive for like high posture, right? Because they're, they're used everywhere and like.
**Reiley Yang (Microsoft Corporation)** 08:25 go.
**Jonathon Klobucar** 08:26 There. And then there's just lots of repos that are like a little less.
**Reiley Yang (Microsoft Corporation)** 08:31 And then, I'll make a direct ask. So, do you think if I try to tweak this, and I also step back a little bit on the number of days, I'll try to like, depending on the feedback, I'll… I'll try to add additional, like, one or two days. Then…
**Jonathon Klobucar** 08:49 Yeah, I think… I think… I think you could make it, like.
we will… we will acknowledge receipt of security issues in seven… seven… just seven days is probably, like… it gets rid of weekends, it makes sure, like, if a rotation… I don't know. If people are… if business days isn't working, I just… 72 hours is, like… pretty rough for an open source project that's, like, non-paid, right?
But 7 days should be caught by a rotation, and like, obviously we will, you know, we can say we will try to strive faster for… you know.
Issues that we deem more critical to acknowledge and patch, but like nominally it's a it's a week.
Like, if someone publishes something, for instance, that needs to get taken down, I'm pretty sure that, like, a big flag will get raised, and that'll happen, like, same day, but, like.
what I've discovered whenever I do, like, bug bounty programs or other stuff is that someone will be like, oh yeah, we'll respond within two business days on acknowledgement, and, like, now I'm just, like, doing all this record keeping to, like, make sure a low severity issue is at least, like, acknowledged in, like, a couple of days, and it's definitely not… Lessons learned on that, that one.
**Reiley Yang (Microsoft Corporation)** 10:16 Yeah, so if I make all these changes… Sorry.
Yeah, so if I made all these changes, two of you would be comfortable giving your thumb up.
**Jonathon Klobucar** 10:27 Yeah, yeah, absolutely. But I can do that this, like, this week for sure.
**Reiley Yang (Microsoft Corporation)** 10:32 Okay.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:35 Yeah.
**Reiley Yang (Microsoft Corporation)** 10:35 I think that.
**Trask Stalnaker (Microsoft Corporation)** 10:36 The business days is the… is the one that's clearly content… the most contentious. I think the other one is naming. I think we can… Find something that makes people happy.
**Jonathon Klobucar** 10:49 Yeah.
It's not like it's a hard problem in computer science or anything.
**Trask Stalnaker (Microsoft Corporation)** 11:05 So why… why… So you really don't want business days, because, I mean, it looked… from all the comments, seemed to be people preferring business days and pointing to Kubernetes and other projects using the term business days.
**Reiley Yang (Microsoft Corporation)** 11:21 Yeah, because I feel for… for the attackers, they… they don't care about whether it's vacation or not. And also, business days mean very different things depending on which country you are, so I think it's a source of confusion.
**Jonathon Klobucar** 11:36 Boom.
**Trask Stalnaker (Microsoft Corporation)** 11:37 Except if it's the de facto standard, then… or…
**Reiley Yang (Microsoft Corporation)** 11:43 Back to our confusion, I would feel.
You might say, like, I expect you to fix that, because it has been business days for the past two days, then the other side might say, but it's not my business day.
What do you say? So, I… like, I… I've seen some.
**Trask Stalnaker (Microsoft Corporation)** 12:01 I'm just…
**Reiley Yang (Microsoft Corporation)** 12:02 Yeah.
**Jonathon Klobucar** 12:04 And trust me, security researchers, I love them, but They can get a little persnickety when it's like, it said you would do it in two business days, what's a business day? I want my response, and you're like. I'm trying to work with you to reasonably figure out this disclosure, man, like, it's okay.
**Trask Stalnaker (Microsoft Corporation)** 12:22 What about weekdays?
**Jonathon Klobucar** 12:23 Yeah.
We, we… yeah. Well, so there's, there's a slight… There's a slight wrinkle there, because certain parts of the world, like, their weekend is Friday, Saturday, and they work Sunday.
which, like, if you're getting… if you're getting, like, particular, which I think this… this argument of, what's a business day, if we say just weekdays, someone's gonna… Someone's gonna make that claim, perhaps, in the PR, I would wager. So that's why I'm like, just say 7 days.
**Reiley Yang (Microsoft Corporation)** 12:59 Yeah.
Yeah, I wanted to send this. Wednesdays also have this time.
**Trask Stalnaker (Microsoft Corporation)** 13:03 Okay.
**Reiley Yang (Microsoft Corporation)** 13:04 7.
**Trask Stalnaker (Microsoft Corporation)** 13:05 Yeah, if we're going to 7 days, then yeah, I agree, there's… I got zero problems with 7 days.
So that would be the high?
**Reiley Yang (Microsoft Corporation)** 13:15 Council.
**Jonathon Klobucar** 13:16 Yeah.
And we can put a note that, obviously, like.
If we, you know, we receive something, you know, we will do our best to triage As soon as we can, but, you know, this is the guarantee we're willing to make on triaging of things.
**Reiley Yang (Microsoft Corporation)** 13:36 Yeah.
**Jonathon Klobucar** 13:38 Just because someone will be like, that seems really long, and it's like, well, yeah, that's… that's the SLA. Like, usually, things are triaged in a couple of days, but we don't want to make that guarantee… we can't… we're not going to make a guarantee that we can't always hold, right? Like… Yeah.
**Reiley Yang (Microsoft Corporation)** 14:06 Okay, one other thing I noticed, but I don't see a lot of people too passionate about it. Do you think I should make a clear call out in the doc?
to distinguish the publicly reported CVEs in your dependency versus the security advisories that are secretly reported to you. I think those are very different.
**Jonathon Klobucar** 14:29 Alright, one quick…
**Reiley Yang (Microsoft Corporation)** 14:30 For the security advisor, if people report to you, nobody else would know, only the reporter and yourself would know. Yes. The reporter might say, I'll give you 6 months, if you don't fix that, I'll just make it public to everyone else. Yeah, so we can… You have more room. Even if the security advisory is a critical thing, like, it can destroy your entire system, you technically have more time room.
But for the public CVE, if you depend on something, that thing has a critical CVE, and you take 6 months to fix, that means you're exposed, and everyone will know how to take you down.
So.
**Jonathon Klobucar** 15:01 Yeah, I mean, there's a difference, right? So, like, in order to get a CVE, they kind of have to go through OpenTelemetry to, like.
like, well, like, they can request one, but usually, like, part of responsible disclosure is you know about it. And so, like, what we're… what we're… we… like, wading into is, like, vault management. If we, like, get an advisory and we classify it as critical, there should probably be some SLA on how quick it is for us to get out a patch. Usually, vault-related disclosures are, like.
you know.
report it, like, ask for an update after 90 days, and, like, it ends up being, like, 6 months, like, when you… when you… if they don't move on it, you just can. But we can write that language up in a separate I would say we write that up in a separate draft, but I can take a stab at, like, what that kind of looks like, if you want, as a first pass.
I've had to write this up a couple of times.
Because, like, someone will report an issue, and usually what happens with these is that someone will be like.
Oh my gosh, I found this thing, I think it's a… High and after you look at it and go through the shape you and the other maintainers agree it's like a medium or a low which changes the the clock fix cycle and like.
researchers are generally pretty… especially if you're not paying out a bug bounty, are pretty amenable to whatever you classify it as. It gets a little weird when you have a bug bounty, because the higher the severity, the more money you get, so they like to argue for higher severities, right? Because the incentives are that way. Not maliciously, just like, oh, I think this is, like, a high, like.
And you're incentivized for it to be.
And so I can write up some basic language, and we can just start figuring out what those timetables look like on, like, if we get an advisory that's a low, like.
You know, we have six months or 90 days to try to get a fix for it or something and like, you know, be secret, but like, we'll figure this kind of stuff out.
Does that make sense?
**Reiley Yang (Microsoft Corporation)** 17:03 Yeah.
**Jonathon Klobucar** 17:03 Cool. Yeah.
**Reiley Yang (Microsoft Corporation)** 17:06 Okay, so I think I got everything I need from both of you. Thank you very much.
**Trask Stalnaker (Microsoft Corporation)** 17:10 I'm leaving a comment, about Jack's… related to Jack's comment with the proposal.
I think I like security commitment.
security commitments.
**Jonathon Klobucar** 17:23 I like that. That's a great that like.
**Reiley Yang (Microsoft Corporation)** 17:24 Yeah.
**Jonathon Klobucar** 17:26 That makes it sound like, you know, yeah, very friendly and…
**Reiley Yang (Microsoft Corporation)** 17:34 Okay, thank you very much.
**Jonathon Klobucar** 17:35 Of course.
**Trask Stalnaker (Microsoft Corporation)** 17:36 See ya.
**Jonathon Klobucar** 17:37 Yep, see you.
