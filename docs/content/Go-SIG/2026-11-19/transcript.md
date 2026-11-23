SIG: GO SIG
Date: 2026-11-19
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn (Splunk)** 01:52 Hey.
**Robert Pająk (Splunk Inc.)** 01:54 Hello, what's up?
**Tyler Yahn (Splunk)** 01:55 Not much. How you doing?
**Robert Pająk (Splunk Inc.)** 01:59 Better. I think they're running nose, trying to get the flow, but it's better.
**Tyler Yahn (Splunk)** 02:04 Hmm.
Yeah, I gotcha.
**Robert Pająk (Splunk Inc.)** 02:06 A lot of colleagues, a lot of colleagues, families, and people around are right now sick because it's like the temperatures are here right near freezing. And then it's five plus, five minutes.
It's very easy, you know, to get sick in these circumstances.
**Tyler Yahn (Splunk)** 02:23 Five minus. I haven't seen that in a long time.
Yeah, we were in Salt Lake City, and it was like…
**Robert Pająk (Splunk Inc.)** 02:30 I saw that!
**Tyler Yahn (Splunk)** 02:31 like.
**Robert Pająk (Splunk Inc.)** 02:32 Yeah, he's just…
**Tyler Yahn (Splunk)** 02:33 Yeah.
There's nothing.
**Robert Pająk (Splunk Inc.)** 02:34 Yeah, Yeah, indeed.
**Tyler Yahn (Splunk)** 02:37 Yeah, I like came home and it was colder. : I was just like, oh, this is go back to Salt Lake City. : Yeah.
But yeah, all good.
I don't… I think it might just be us today.
Boom.
**Robert Pająk (Splunk Inc.)** 02:59 Yeah, I'm not sure about David.
And.
**Tyler Yahn (Splunk)** 03:04 Yeah, I saw, Puneet said that he wasn't able to attend, if I remember correctly.
**Robert Pająk (Splunk Inc.)** 03:11 It's very late for him right now.
**Tyler Yahn (Splunk)** 03:13 Yeah, yeah, and I think he's still on, like, leave.
**Robert Pająk (Splunk Inc.)** 03:19 I can ask David because he's online on Slack.
**Tyler Yahn (Splunk)** 03:22 David's out for the first 15 minutes.
**Robert Pająk (Splunk Inc.)** 03:25 Alright.
**Tyler Yahn (Splunk)** 03:26 as well.
**Robert Pająk (Splunk Inc.)** 03:28 Okay.
**Tyler Yahn (Splunk)** 03:32 Well, I mean, I guess we can go over the release prep stuff, and then… See where that takes us, does that sound good?
**Robert Pająk (Splunk Inc.)** 03:41 Yes, sure.
**Tyler Yahn (Splunk)** 03:42 Okay, yeah, I'll start sharing my screen then.
Cool, yeah, I haven't really, Following too much on this, so yeah, it'd be good to go over.
Okay.
**Robert Pająk (Splunk Inc.)** 03:56 You know what?
**Tyler Yahn (Splunk)** 03:57 Oh, just have one PR?
**Robert Pająk (Splunk Inc.)** 04:00 I added this one because I think it's very important, because improper hashing, you know, can cause trouble, especially for metrics.
And yeah, I have reviewed this a few times, and I think it's worth adding.
**Tyler Yahn (Splunk)** 04:14 What about your implementation of the Semcon stuff?
**Robert Pająk (Splunk Inc.)** 04:19 It's merged in GO in the core. It's not merged in the country, yes.
**Tyler Yahn (Splunk)** 04:26 Oh, okay, alright, then I…
**Robert Pająk (Splunk Inc.)** 04:27 the other…
**Tyler Yahn (Splunk)** 04:28 Well, yeah, we'll get there. Okay, that sounds good.
Okay, yeah, that sounds good, so this just needs another review, then.
**Robert Pająk (Splunk Inc.)** 04:36 Yes.
**Tyler Yahn (Splunk)** 04:37 Okay.
**Robert Pająk (Splunk Inc.)** 04:38 I think it will be good if David takes a look. I think I'll ask David because also we need another email.
non-Splunk reviewer, if I remember correctly.
**Tyler Yahn (Splunk)** 04:47 Oh, you've already… oh, I see, yeah. Good idea.
What do you think of this new format for GitHub?
**Robert Pająk (Splunk Inc.)** 05:00 I think I still see the old one.
**Tyler Yahn (Splunk)** 05:03 Yeah, you got to like go up to this. Oh, actually it may not have rolled out to you as well, but like there's like this.
**Robert Pająk (Splunk Inc.)** 05:08 Yeah, I think it has not.
**Tyler Yahn (Splunk)** 05:09 Yeah.
**Robert Pająk (Splunk Inc.)** 05:10 Yeah.
Because there was no obstacle, yes.
**Tyler Yahn (Splunk)** 05:13 I'm.
**Robert Pająk (Splunk Inc.)** 05:14 I have tried the overview page. Yeah.
**Tyler Yahn (Splunk)** 05:17 Oh, you have? Okay.
**Robert Pająk (Splunk Inc.)** 05:18 I have, but I need to opt in. Maybe you, maybe you have you opt in or have you or is it opt in by default? Okay.
**Tyler Yahn (Splunk)** 05:25 Well, no, it's like, you opt in, although I've opted out quite a few times already, because I can't find anything. And then I, like, I keep trying to go back, because I'm like, I'm gonna try to figure this out, but it's like… I like that, like, the comments are reverse-ordered now.
Because otherwise I'm like.
**Robert Pająk (Splunk Inc.)** 05:40 Oh.
**Tyler Yahn (Splunk)** 05:40 Rolling really far, but… It's still, like… like, this is just… it's almost too condensed, and then, like, I can't… like, you gotta, like, hover to do this, and it's, like, it's a little bit off, In my opinion. And then I always get confused when it merges, it, like, puts the name of the merger right here. So I always, like, look in, and I'm like, wait, this is somebody else's PR? Because, like, the name got moved up. So it's like, it's just subtly different, and I just can't quite figure it out, but… Sorry, totally, totally big tangent.
Cool. Alright, moving on to this one, though, you wanted to… so we have this in here.
IMDB request response.
**Robert Pająk (Splunk Inc.)** 06:20 These ones are just nice to have. I have posted them that all except this Helmconf can be just moved out of this milestone. I keep it here, because even today, I merged the AutoMax fix, so maybe there's a little change that… oh, I see, the AutoLich is updated 32 minutes ago, so maybe it also has a chance to be fixed.
Speak so much.
**Tyler Yahn (Splunk)** 06:46 Yeah!
This doesn't look too bad, Links, yeah, okay.
Yeah, I mean, I can take a look at this, after.
I say that, I've got so much to do. I will try to get.
**Robert Pająk (Splunk Inc.)** 07:00 test.
**Tyler Yahn (Splunk)** 07:00 today.
But yeah, okay, cool. Yeah, this looks reasonable. What's the plan for the release? Like, once we get these in, are you trying to get something out, next week, is the goal?
**Robert Pająk (Splunk Inc.)** 07:12 Yeah, I even wanted to… maybe you can try tomorrow, or maybe early next week. I would like to have Damien also, present, helping with also updating merch and some stuff, but I'm not sure if he will be available tomorrow. I know that today he has been on a conference.
So I'm not sure how it works, how it's more working.
**Tyler Yahn (Splunk)** 07:36 I gotcha. Is it AWS re: Invent this week, right?
**Robert Pająk (Splunk Inc.)** 07:40 I have no idea. If AWS is right now, then probably yes.
**Tyler Yahn (Splunk)** 07:44 Yeah, okay.
Yeah, okay. Yeah, actually, I don't know why he'd be there.
Maybe he is, I don't know. Maybe it's a different conference, but… Okay, yeah, that sounds good.
Sounds like a good plan. I know, There's still a bunch of work, I think, for the bound stuff and the finish stuff. David, I don't know if you saw that, like, he started… taking over the Finnish semantic convention, or sorry, the Finnish specification PR, so… There's work moving on that one as well, for experimental features. And the Metric SDK stuff, like, yeah, I think we're… Yeah, moving along. He's also very active on, like, the goals that we set out at the beginning of the year. I see David's been making a lot of movement on those, so, yeah.
But Cool.
Yeah, I mean, I don't know, I guess we could wait another… 7 minutes for David, but I think we might just also call it, Yeah.
**Robert Pająk (Splunk Inc.)** 08:50 I can be here, Tyler, if you want, and then I can just, you know, say to David, I'm not sure how does it work for you.
We can just, you know, or we can just, you know.
Do our stuff and be back in 5 minutes.
**Tyler Yahn (Splunk)** 09:07 Yeah, I mean, I don't know if he really needs to talk about anything.
Yeah, I mean, maybe we can just post in the Slack channel saying, like, we can jump back on if he wanted to talk about that.
**Robert Pająk (Splunk Inc.)** 09:19 That's a good idea.
**Tyler Yahn (Splunk)** 09:20 Yeah, and then we'll go from there. Okay, alright, I will, jump off, and we can… Sync outside of this in a sec.
**Robert Pająk (Splunk Inc.)** 09:28 you.
**Tyler Yahn (Splunk)** 09:29 Alright, bye.
