SIG: Android SIG
Date: 2025-11-25
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/YK75e_A7LTKIV6uwno19fVc0lIHx2p3UBqapYZkxsvVqUssbTlpZ2lbVS130Do2l.yDQSIsU6HcKvRVzx
============================================================

## Zoom Recording Transcript

**Mustafa Haddara** 00:32 Good morning.
**JP Jason Plumb** 00:33 Good morning.
Just pulling up the dock.
Dirty.
Alright, I… let me check my messages to see if folks are gonna be here or not. Sometimes I get a DM.
Go ahead and start adding any agenda items that you might have interest in.
Sounds like Handsome will not be here, and Cesar's off until next year, so we'll see if Jamie or anybody else shows up, but we should probably just jump into it.
And the more interesting thing, rather than that lines of code situation, is that I'm starting this.
**Bee Klimt** 01:54 Yay!
**JP Jason Plumb** 01:55 Yay! So…
**Mustafa Haddara** 01:57 Nice.
**JP Jason Plumb** 01:59 It could be a little tricky without an approver in my time zone if stuff goes south, if it doesn't, like, work on the first…
Try, but we're gonna give it our best right before the holiday.
Are there any questions or last-minute concerns about doing the RC1?
We've probably talked that to death.
Okay, so with that out of the way, let's talk about contributing MD.
So I added… Whoa.
It's weird that that's a link, that's not what I meant.
Right, so I made some changes yesterday, already got some feedback, looks like it's good to merge.
They're… As part of this new update to contributing.
There's an encouragement here to keep PR small. This is a problem that we see across OpenTelemetry repos, is, like, especially with new contributors sometimes.
a magical, like, 5,000 line PR will just appear out of nowhere, and the intent here is to at least set some expectation that,
Larger PRs are going to be more difficult to get merged.
Because they're more difficult to review.
There's also, they might have closed it by now, but let's see, I think…
I think it's this one… Yeah, so this person is a new contributor.
And, you know, this… this is, like, 4,000 lines, and then there's another one that they submitted… not this one, this one's good. I think there's a… I think there's another one…
That they might have closed.
Let's see… Yeah, this one.
So, you know, 6,200 lines, plus another 142, so that's a big PR. 97 files, really a bear to ever think about.
Reviewing this one. So they took the feedback, very lovingly, and, like, are gonna break it down. The question… the open question to the community here is, like, should we have a lines of code guideline? So, as part of that discussion,
they straight up asked, like, well, is there, like, a number that I need to adhere to? And, like, there isn't.
I thought there was a comment about that. Maybe it's… there's 3 PRs floating around, and I'm scatterbrained, but
I think Jamie floated, like, an idea of, like, in his brain, like, 500 seems like a good number. I've heard 1,000 elsewhere. I don't have a great number. I'm curious what other people think.
**Mustafa Haddara** 04:59 I was gonna say 500.
**JP Jason Plumb** 05:02 Right.
**Mustafa Haddara** 05:03 As a… just as, like, like, not a hard limit.
**JP Jason Plumb** 05:09 I don't think we should…
**Mustafa Haddara** 05:10 build tooling that, like, you know, closes your PR if it's 505 lines of code. But,
I think that's a good recommendation as, like, a upper bound. Like, if you get above 500, you should think about how digestible is this?
**JP Jason Plumb** 05:26 Yeah.
Okay. Other… okay, Tyro's in agreement. B or Cleverchuck, what… like, is 500… like, does it make sense to put a number in there at all, and if so, is 500 a good number for you?
**Bee Klimt** 05:39 I don't… I don't know a number off the top of my head. 500 seems fine. I agree it's, like, not a hard limit, because something that's just, like, a big rename or something might be more lines, but is easy to…
**JP Jason Plumb** 05:50 Yeah.
**Bee Klimt** 05:50 So…
**JP Jason Plumb** 05:51 Yeah, it's definitely not… it wouldn't not be a hard… Hardline.
**cleverchuk** 05:58 Yeah, I don't know about putting a number to it, but .
**JP Jason Plumb** 06:02 I know.
It's kind of where I was like,
You kind of take it case by case, but yeah, yeah. Okay. Well, let's think about that. I'll get that merged after the… I'll get this one merged after I attempt the release.
And we'll go from there.
Okay, any other topics that folks have?
Okay, well, I would expect stuff to generally be slow across OpenTelemetry and probably all of North America if, you know, this, this week.
people are traveling, there's holidays, so I'm gonna try and get this… I'm gonna try and get the release out, but just know that, you know, PRs are gonna be a little bit slower, and… yeah.
Your help's always appreciated.
**Bee Klimt** 06:59 Thank you.
**JP Jason Plumb** 07:01 Yeah, I won't belabor it. If people are good to drop off, we'll call it at that. Please feel free to review. There's a lot of stuff stacking up, so reviews are definitely helpful.
Alright.
**Mustafa Haddara** 07:16 Thanks.
**JP Jason Plumb** 07:17 Yeah, thanks, everyone.
Happy Holidays!
**Mustafa Haddara** 07:20 See ya. Happy holidays.
