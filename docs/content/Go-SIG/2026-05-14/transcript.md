SIG: Go SIG
Date: 2026-05-14
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/ezHJnRiYKqD9s1HJ9i2Nk3iK8GctL-NgOBf2stpdG75zZ_OrwoeyLD_aayalI4A_.kS7m_5i-ylpq2Dz5
============================================================

## Zoom Recording Transcript

**Tyler** 01:09 Hey, Brian.
**Bryan Boreham** 01:10 And there…
**Tyler** 01:12 How's it going?
**Bryan Boreham** 01:15 Not bad. Not bad.
**Tyler** 01:18 Yeah.
**Bryan Boreham** 01:23 I'm going on vacation on Saturday, so… Kind of mostly… mostly there, in my head.
**Tyler** 01:32 Yeah, yeah, I leave, for mine tomorrow, so, technically, this afternoon, I'm already packing up, so, yeah.
I'm with you, one step out the door already, yeah.
Where are you going? Anywhere fun?
**Bryan Boreham** 01:46 Anguilla.
**Tyler** 01:47 Wow! Okay, that's way further than where I'm going. Yeah.
Are you just visiting, or do you have, other objectives in mind?
**Bryan Boreham** 01:58 Oh, this is, this is a Grafana event.
**Tyler** 02:05 Oh, really?
Cool.
**Bryan Boreham** 02:09 You know, I guess it's a… What we would call a jolly, perk.
But also, I mean, that's the place where the .ai domain lives.
**Tyler** 02:24 Oh, is it really? Oh, I didn't know that. Okay, yeah, yeah, that makes sense.
Where it's, like, one of those countries where it's, like, the regions where it's, like, that's, like, the main source of income, essentially. It's, like, just domain registration.
**Bryan Boreham** 02:38 It's gonna be after tourism. Yeah, I think, I think .
Is more like that, but yeah, it's.
**Tyler** 02:46 Yeah, that's right, yeah.
No, that's cool.
**Bryan Boreham** 02:51 Leaning into that.
**Tyler** 02:53 So you each get your own domain, as just a party favor?
**Bryan Boreham** 02:59 I don't know, we've registered Grafana.ai.
**Tyler** 03:02 Yeah.
What about brian.ai?
**Bryan Boreham** 03:04 Yeah, I'll check if it's available.
**Tyler** 03:08 Yeah, I would imagine it's long gone, but yeah.
That's cool. How long are you there for? Just a whole week, or…
**Bryan Boreham** 03:17 Yeah.
**Tyler** 03:18 Nice. Oh, cool. Yeah.
Yeah, that should be a lot of fun.
Do you have other, how many other Grafanistas are headed over there?
I wonder if Steven, who's also in, I think, England.
**Bryan Boreham** 03:34 It's, there's about 100 or so, but it, whether it's… Sorry, which… which Stephen are you referring to?
**Tyler** 03:45 Yeah, Lang, Stephen Lang, sorry, I'm trying to remember if he caught me.
**Bryan Boreham** 03:51 Let me check. No.
**Tyler** 03:54 Oh, okay, alright.
**Bryan Boreham** 03:56 Not this time.
**Tyler** 03:57 Yeah.
Yeah, I was wondering… he's working… he does a lot of stuff in Obi, he's really great at, like, CI, work and… and EPPF stuff as well, but, like.
Yeah, I thought he was over there. I think he's in England, but maybe just the British.
**Bryan Boreham** 04:13 Yeah, no, I, I, I, I know who you mean, yeah, I, Just, yeah, it's the… Somewhat restricted event.
Huh.
**Tyler** 04:27 Oh, yeah, yeah, I mean, I'm sure…
**Bryan Boreham** 04:30 We do have absolutely everyone going to Vienna in August, the end of August.
**Tyler** 04:35 Oh, really? Oh, cool.
That's awesome.
That's another place I've always wanted to go. In 2019, I can't remember, it was either KubeCon was supposed to be there, or, the W3C meeting was supposed to go there, but I was supposed to go.
And of course, COVID happened, and so then… yeah, I guess it was 2020. So then, yeah, it just was like, never, never went. It's always been kind of sitting in the back of my mind of wanting to go there, yeah. It looks beautiful, so I've always wanted to check it out.
**Bryan Boreham** 05:09 Yeah, yeah, it's palaces and stuff, yeah.
**Tyler** 05:16 Yeah.
Yeah.
Classic Europe.
Hey, David.
**David Ashpole** 05:26 Hey, Tyler.
**Tyler** 05:28 How's it going?
**David Ashpole** 05:30 Doing alright.
**Tyler** 05:31 Nice.
**David Ashpole** 05:31 Sorry, I haven't done nearly as much this week as in past weeks, but… I guess that's okay, feels like it's kind of been a quiet week.
**Tyler** 05:39 Yeah, a lot of people out. I think, I think, as we were just talking, most of Europe is going on vacation, starting now and probably ending in 3 months.
Okay.
Yeah, but yeah, a lot of my colleagues are also out.
So, yeah, it's been pretty slow here, too.
Yeah, I haven't done too much, I guess, to report other than the fact that I'm leaving for 2 weeks after this, so, yeah.
**David Ashpole** 06:07 Yeah.
Is there anything we want to get in before you… like, is there anything you have in flight that you want to make sure gets in before you head out?
Nope. Not in the ghost space.
**Tyler** 06:16 Not in the…
**David Ashpole** 06:16 Semantic Conventions PR merged, right?
the…
**Tyler** 06:20 Regeneration.
**David Ashpole** 06:21 for 41…
**Tyler** 06:23 Yeah. Did it?
Oh, that's a good question.
I…
**David Ashpole** 06:30 It's not like someone else can't rerun it, but…
**Tyler** 06:32 Yeah, yeah, yeah, I've got so many… things in flight, to be honest, I totally forgot about that one. Yeah, that's a good question, let me pull that up.
**David Ashpole** 06:45 Do we have any agenda topics for today?
**Tyler** 06:48 Nope.
**David Ashpole** 06:49 Okay.
**Tyler** 06:50 Not yet, at least.
It has not merged.
**David Ashpole** 06:55 I think it… Reviews.
**Tyler** 06:58 It got 2 reviews… Oh, yeah, oh, I think the only reason I didn't merge it was because I lost the tab. Yeah, I was planning to merge it, like, the day after. I think you got 2 reviews immediately, and I was just waiting on the 24 hours.
So yeah, I guess I just kind of blanked on it.
But yeah, so I guess that's a question. I'd like to get this in in the next release, just because it needs to be, but, like, as you pointed out in that, is that there's, like, a bunch of follow-up stuff that we wanted to also do.
So, since I'm leaving, I think it's more a question for you, and then Robert, who's also not here, he's on sick leave this week, if, like, you guys are okay with addressing that? I mean, I'm happy to do that when I get back, but that's gonna be in 3 weeks, you know, so, like, that's probably a little too long.
**David Ashpole** 07:47 We have too many CBEs open. Yeah. At least for 3 weeks.
**Tyler** 07:51 Yeah. Oh.
**David Ashpole** 07:53 I don't think any of them are must-haves.
Sure.
Sure, it doesn't sound like… This is my top priority right now.
**Tyler** 08:06 No, that's fine. I mean, I get it. Yeah, so what did we have?
I think we had regeneration of… Yeah, there were other changes. I think that they were, like… Oh yeah, you did, Adam.
update all metrics in the process comp to be observable. That was also, like, kind of already ready to go, it just needed to, like, get incorporated.
**David Ashpole** 08:28 Yep.
**Tyler** 08:29 And then…
**David Ashpole** 08:30 I think those can get in, let's see. I would just merge your PR, and we'll get them in. Because the main… yeah, we have… we have one… I know this is a public call.
So we had the one from Sam, right, that needs to go in.
I don't remember any of the other ones.
**Tyler** 08:56 I don't know if those are gonna get addressed in this… in this release. Yeah, that's…
**David Ashpole** 09:00 That was my thinking as well, like, so if we can get Sam's, and then get the release out.
And maybe get some of these small things cleaned up. What else is in the milestone here?
**Tyler** 09:09 I think it's just… I think it's just those… that Sam's PR and then this, semantic convention stuff. There is one thing in Contrib that's, like, kind of… Always been there, so that can get bumped, but, like… .
Yeah, those are really the two top priorities.
**David Ashpole** 09:25 Cannot find milestones.
**Tyler** 09:28 Oh, I can start sharing. Maybe?
There we go.
**David Ashpole** 09:47 We have 1, 2… 3… Poor.
5…
**Tyler** 09:58 Yeah.
Fixed cash…
**David Ashpole** 10:01 Just Sam's.
Yeah. I don't feel like this has to get in, this cache one.
**Tyler** 10:07 I don't either. I thought that it was, like, close, but… yeah.
**David Ashpole** 10:10 It's been approved.
I'm Robert and I.
Like, it makes sense what it's doing, and the… I guess what the benchmarks even show? They should show, right, any additional costs.
**Tyler** 10:27 Yeah. Well, yeah.
**David Ashpole** 10:28 Excellent.
**Tyler** 10:30 Exactly. It's, it's… I would imagine… yeah, this looks ready to go, honestly.
**David Ashpole** 10:35 Okay.
**Tyler** 10:36 Just… yeah.
**David Ashpole** 10:38 Cool. I'll hit the merge buttons on both of those, so you can go.
Relax on… you're not a beach person, though, right? So relax in a mountain or something.
**Tyler** 10:50 Yeah.
**David Ashpole** 10:51 At the very top.
Okay, cool.
Oh.
**Tyler** 10:55 I think, I didn't check at the baggage one as well, but I know Robert's been syncing back and forth on that one as well, and it looks close, if not ready last time, but, Yeah…
**David Ashpole** 11:07 Robert and I can make sure that that gets in, I think, while you're gone.
**Tyler** 11:10 Right, that's kind of what I figured. Okay.
Yeah, okay, cool, then… oh, yeah, there's no reviews on it, or no approvals. I'll need a review.
But yeah, okay, cool, yeah, I don't think there's anything… I didn't want to, like, throw that on your plate and then also be like.
Yeah, you need to get these other things done, yeah. So, cool, but if you guys are okay with that, I think it should be pretty straightforward, yeah.
**David Ashpole** 11:36 Cool. Alright, then, let's just call the meeting then.
**Tyler** 11:40 Sounds good.
Alright, everyone.
**David Ashpole** 11:42 Bye.
