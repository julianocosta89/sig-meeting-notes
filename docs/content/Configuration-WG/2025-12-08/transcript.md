SIG: Configuration WG
Date: 2025-12-08
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/WxdvCaDGNwQj-C73y-rfJjppdQLIHoHcJWERKGP_B7V9hHVlAOY0eaJDVoHiD59Y.qg05AwNRtP0hR3GS
============================================================

## Zoom Recording Transcript

**Tyler** 00:49 Hey.
**Alex Boten** 00:55 Boom.
**Tyler** 00:56 How's it going?
**Alex Boten** 01:00 It is going.
How are you doing?
**Tyler** 01:05 Just getting started with the day.
Hmm.
**Alex Boten** 01:25 You know, it's early, when all I can manage to type in the agenda is my name in the wrong place, and in fact, it was only my first name.
I did not make it to the second name, yeah, there we go, I just copied and pasted it down, that was easier.
**Tyler** 01:39 I didn't want to say anything, but I saw that, I was laughing, yeah.
**Alex Boten** 01:44 I got past the first four letters, and I just paused. I knew there was something else coming after, but…
**Marylia Gutierrez** 01:52 And I just got back from vacation, and my flight got very delayed, so I actually got home, like, close to 4am, so I'm just like, hi!
**Alex Boten** 02:00 Wow.
**Marylia Gutierrez** 02:01 Where am I?
Wow. Did you even… did you even sleep at that point, or did you just… just power through, you know? Yeah.
I just, like, when I saw that, I was like, it's gonna be very late, so I just sent a message on my team channel, like, I'm taking the morning off, and I'm just starting now.
**Tyler** 02:20 What time is it there for you, Perlio?
**Marylia Gutierrez** 02:22 11. I'm in Toronto.
**Tyler** 02:24 Oh, okay, alright, yeah Yeah, I would have taken the whole day off, but that's just me.
**Marylia Gutierrez** 02:31 Yeah, my last… I have, like, the last two weeks also as vacation, so I was like,
**Tyler** 02:37 Yeah, that's a smart thing to do.
Yeah.
It looks like… is Jack able to make it? I'm sorry, I'm looking at…
**Alex Boten** 02:49 I don't know.
I only have one… actually, two issues to talk about.
And… I think… I think both… well, one issue leads to another, so I'm happy to… start whenever. I guess we can get another…
**Tyler** 03:04 Start us off, then? Go ahead.
**Alex Boten** 03:06 Sure.
Yeah, so I just wanted to call attention to the… 1.0-RC3ReleaseCandidate, Poll request. It's currently in draft that, Jack has created.
There are a couple of outstanding issues on it.
And I think… I think the main one… So there's an issue. Maybe I can… I'll just share screen one second.
Figure out my tap situation.
I'll figure this out.
There we go. Alright, I managed to spell my name, and I'm hoping that my screen sharing will work, so this will be.
**Tyler** 03:50 It's asking a lot.
**Alex Boten** 03:52 It's asking a lot, you know, I'm depending on external systems as well, so, you know, it's not just me, but… Okay, so this is the issue that I wanted to call attention to. Specifically, this is trying to get us to… a new release, and the two issues that I wanted to quickly highlight, if folks have not seen it.
There's, this one that was opened a little while ago. This might be the most discussed issue we've ever had in this repo with 32 comments.
is… the idea that we're going to add a top-level section called Distrib… Buchan… there's a little more comments to kind of resolve in here, I think.
But, by and large, this is not… Looking too controversial.
I was following up on this issue where Mark had… Added some comments.
And… If I go all the way to… Bottom, it looks like… Looks like Mark has also come around.
So maybe we'll give it another… day or so to try and see if there'll be any additional comments or reactions on this particular PR, but if not, then we can move this along.
The other one's a little bit… The other one needs a decision. I've made my decision on this, but this is whether we decide to support Upper snake case… upper snake case, or lower snake case.
I… I voted lower snake case, but that's just because… I really don't like… One second.
I find the upper… upper snake case in the config very jarring, so I voted for a lower snake case, but… Feel free to chime in, or… or whatever. If people have comments here, we can also… talk about it now.
**Tyler** 06:02 Yeah, I don't have, I don't have strong preferences here, I just… Wonder… the… so the specification right now has things, I think, defined… With, like, the uppercase is my only concern.
**Alex Boten** 06:19 Or severity level, yeah.
**Tyler** 06:22 Okay.
Yeah.
**Alex Boten** 06:24 like… These guys.
**Tyler** 06:28 Yeah.
But, like… but I don't think that's, like, also… I'm not too sure if that's configuration, as much as it is, like, it was, like, I think the severity text or something like that, right?
**Alex Boten** 06:39 Right.
So…
**Tyler** 06:42 Yeah.
So that's why I'm, like, not… I don't think it's, like, super critical, and I also think that our enum… our definitions of environment variables are explicitly case-insensitive, so this is, like.
not gonna take precedence from that, I guess, is… so, like, we are really making a novel choice here, so I think it's, like, up to us.
how we want to define it.
**Alex Boten** 07:07 Yeah, I mean, the… we already introduced novelty when we brought in, like, Camel casing for… For options?
So, I think this is just trying to provide consistency, because right now we have camel casing, we have some uppercase, we have some lowercase in some other places.
**Tyler** 07:25 Yeah, yeah.
**Alex Boten** 07:26 And… I think you're right in that… Like, the spec for hotel log level, which is what this variable represents, just… Just says the default is lowercase info, and…
**Tyler** 07:42 That's about the only guidance that the spec provides.
**Alex Boten** 07:45 So…
**Tyler** 07:46 That might be my longest open issue, is we need to define log levels, but yeah.
Yeah.
**Alex Boten** 07:52 I mean… I… yeah, I won't… I won't speak to how I feel about these log levels, on a recorded call, but I don't feel very… positively about him. Anyways…
**Tyler** 08:06 Do you mean, like, the uppercase ones, or do you just mean, like, the names of, like, debug 3 or something like that?
**Alex Boten** 08:11 I… Sure, yes.
**Tyler** 08:14 Okay.
**Alex Boten** 08:16 Yeah.
**Tyler** 08:16 Yeah, can't help you with the debug 3 part, but the uppercase can maybe help you out with.
**Alex Boten** 08:21 Yeah. Well, this is what I'm hoping to get out of this, at least addressing some of my concerns about this.
**Tyler** 08:28 Okay.
**Alex Boten** 08:29 Alright, so… If you have a preference, please go and vote with your approvals, I guess, on either upper snake case or lower snake case. That's, I think, all I'm… Really after here.
**Tyler** 08:46 Yeah, I'll probably put my, approval on both, so we can… There we go. Like, I really don't care, yeah.
**Alex Boten** 08:51 Hedging your bets.
**Tyler** 08:52 Yeah, I'll hedge my bet, yeah.
**Alex Boten** 08:54 I like it. Either way, as you can say, I voted for the other one.
**Tyler** 08:59 I like it.
**Alex Boten** 09:02 Yeah. Okay. That's… that's all I had.
Folks have other topics they want to cover.
**Tyler** 09:13 No, that was actually kind of what I was hoping to talk about as well, just that next release, but… account of… I guess… I guess I was thinking Jack would have more to say, but he's already put it into PR, so those are really all he cares about, so yeah.
Well, cool. I mean, I guess we could probably end it early if there's no other topics.
**Alex Boten** 09:38 Sure, yeah, I can go to my other competing meetings.
**Tyler** 09:41 Yeah, right, exactly.
**Alex Boten** 09:42 Alright, see you later.
**Tyler** 09:43 Bye, Rob.
