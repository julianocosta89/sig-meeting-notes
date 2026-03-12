SIG: Security Governance SIG
Date: 2025-12-08
Duration: 11 minutes
============================================================

## Zoom Recording Transcript

**Jeremy Corley (Microsoft)** 00:11 Hey, Jeremy.
Hey, hello!
**Trask Stalnaker** 00:17 our things.
**Jeremy Corley (Microsoft)** 00:20 Doing alright… How's your December looking? A little busy.
Yes.
My, My, my, my furnace is acting up, so we're dealing with that one, so… Oh, no. Always good timing, yes. That'll be fine.
Well, it looks like my camera's not gonna work today. No, that's alright.
Excuse me.
Are you getting an echo from my microphone, or is it okay?
**Trask Stalnaker** 01:04 I am.
I am.
**Jeremy Corley (Microsoft)** 01:07 Yeah. Yeah.
Okay, we'll try this.
**Trask Stalnaker** 01:38 testing…
**Jeremy Corley (Microsoft)** 01:39 Okay, is that… is that better?
**Trask Stalnaker** 01:41 Yeah.
**Jeremy Corley (Microsoft)** 01:43 Okay.
**Trask Stalnaker** 01:49 Cool, so, I thought we could chat about, James is…
**Jeremy Corley (Microsoft)** 01:57 Interested in…
**Trask Stalnaker** 01:59 Like, trying to help out with, some of this… Stuff… And… Let's see… I was… pinging, so Eddie Knight, who we worked with, like, a year ago, a bit, he's in the part of the CNCF, Security and Compliance Tag.
And there was sort of some…
**Jeremy Corley (Microsoft)** 02:45 Different direction that seemed like…
**Trask Stalnaker** 02:48 they were taking or recommending. So I was checking in with him this morning, about CLO monitor.
He said that… so they were planning to sunset CLO Monitor, but then… They changed their mind about it.
So I think they're not sunsetting it, but… I'm not sure that's… he said, this is what the CNCF leadership is really… kind of invested in… is this LFX Insights… .
**Jeremy Corley (Microsoft)** 03:34 So…
**Trask Stalnaker** 03:35 I think it makes sense to sort of… Shift… not necessarily invest in CLO monitor… .
**Jeremy Corley (Microsoft)** 03:51 Legal quality…
**Trask Stalnaker** 03:55 But try to understand, and I can provide some guidance to James, basically, to… Try to understand what, oh, including archived repos…
**Jeremy Corley (Microsoft)** 04:10 Interesting.
Why…
**Trask Stalnaker** 04:15 are… oh, excluded from health score and security best practices, okay.
**Jeremy Corley (Microsoft)** 04:21 Oh, excellent.
**Trask Stalnaker** 04:24 Report issues… okay, that's about the LFX Insights.
I'll delete. So this is… Okay, across all repos, I see, so if we wanted to look at a single one, like, let's look at… Java… Ha ha ha ha ha ha.
Cora, okay… Popularity, development… First time… okay, these are… oh, I see, there's a whole tab for security, got it. Yes, so this is what we want… care about.
And what does this… Breakdown… Wallet… Okay, this is… Whoa… They, okay, okay, so… Contained generated executable artifacts, yes.
probably the Gradle wrapper…
**Jeremy Corley (Microsoft)** 05:53 Hi… If we look at…
**Trask Stalnaker** 05:56 Others… quality… Okay, kind of same. So they don't have very much… Here, it does not… Insights does not contain a list of repositories.
Makefile… binary. Make files aren't binary. What are they talking about?
I suspect this is a fairly new, undertaking from… the CNCF, the sort of LFX Insights, and I have seen that they are pushing this a lot, like, this is supposed to replace the, the dev stats? I don't know if you've seen the dev stats is…
**Jeremy Corley (Microsoft)** 06:57 They're… That's… that's…
**Trask Stalnaker** 07:01 a bunch of…
**Jeremy Corley (Microsoft)** 07:01 dashboards.
**Trask Stalnaker** 07:03 About contribution stats, and how long.
**Jeremy Corley (Microsoft)** 07:08 PRs take, take…
**Trask Stalnaker** 07:10 Land, and all kinds of stuff like that.
So, it's… Beautiful.
**Jeremy Corley (Microsoft)** 07:16 They're…
**Trask Stalnaker** 07:18 Kind of trying to move away from that and towards… Putting everything in this.
**Jeremy Corley (Microsoft)** 07:26 LFX Insights.
Is… is that…
**Trask Stalnaker** 07:36 What's the visibility on this? Is there…
**Jeremy Corley (Microsoft)** 07:40 Is it just open?
**Trask Stalnaker** 07:42 Yeah.
**Jeremy Corley (Microsoft)** 07:42 Like, everybody.
Oh, okay.
Interesting.
Here, I'll put a link, a specific…
**Trask Stalnaker** 07:53 We… Oh, there's a time range… Anyway, I will… let's see… Security… Oh, that's too bad, it doesn't update the link, they're not deep links.
Yeah.
**Jeremy Corley (Microsoft)** 08:23 They've kind of.
**Trask Stalnaker** 08:23 a lot of work. They've got a lot of work to do to make this good, but, Yellow monitor… Has been screwed.
Alright.
**Jeremy Corley (Microsoft)** 09:17 Yeah.
**Trask Stalnaker** 09:18 How old… just point… James, to that.
**Jeremy Corley (Microsoft)** 09:27 Yeah, that sounds, sounds reasonable.
**Trask Stalnaker** 09:33 There's the FASA stuff, the license check stuff… I don't know if that's really… not exactly security.
So, maybe… I might actually…
**Jeremy Corley (Microsoft)** 09:51 Split.
**Trask Stalnaker** 09:52 that over into… Community repo…
**Jeremy Corley (Microsoft)** 10:10 I don't think.
**Trask Stalnaker** 10:10 We have really…
**Jeremy Corley (Microsoft)** 10:15 Much.
**Trask Stalnaker** 10:16 Oh.
**Jeremy Corley (Microsoft)** 10:16 Oh, yeah, yeah.
Yeah, I'm not seeing much else to talk about. I'll take care of that.
Renovate.
PR…
**Trask Stalnaker** 10:41 Cool, shall we, so, OpenTelemetry, all the meetings are canceled the last two weeks?
Which… Oh, would be the next meeting, Arna.
**Jeremy Corley (Microsoft)** 10:55 Okay.
**Trask Stalnaker** 10:56 So we're already off the books.
**Jeremy Corley (Microsoft)** 10:58 This is the last…
**Trask Stalnaker** 11:01 Meeting… security meeting for…
**Jeremy Corley (Microsoft)** 11:05 the year.
Oh, excellent.
**Trask Stalnaker** 11:10 Alright.
**Jeremy Corley (Microsoft)** 11:12 Yeah, yeah.
**Trask Stalnaker** 11:13 Maybe we'll.
**Jeremy Corley (Microsoft)** 11:15 Brainstorm what…
**Trask Stalnaker** 11:17 What our goals are, New Year's resolutions when we come back.
**Jeremy Corley (Microsoft)** 11:23 Yeah, yeah, that's a good one. I like it. Yes. Alright. Okay.
Alright, thanks so much, Travis.
Bye. Bye-bye.
