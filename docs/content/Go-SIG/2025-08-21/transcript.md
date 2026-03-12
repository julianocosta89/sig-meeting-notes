SIG: Go SIG
Date: 2025-08-21
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:27 Hey, Brian.
**Bryan Boreham** 00:29 Hello?
**Tyler Yahn** 00:30 How are you?
**Bryan Boreham** 00:32 Pretty good.
**Tyler Yahn** 00:35 Yeah, pretty good. Pretty good.
Yeah, chugging along. What time zone are you in?
**Bryan Boreham** 00:43 London, so 5pm.
**Tyler Yahn** 00:46 Oh, okay, yeah.
I had another, collaborator over in southern Italy I was on a call with yesterday, and, he was saying it was also 5PM there. It was an hour earlier, and … I was cracking up, I was like, well, it sounds about, like, dinner time, and he's just like, oh, no, that's not for, like, 5 hours.
**Bryan Boreham** 01:06 Yeah.
**Tyler Yahn** 01:08 Yeah, which, … Definitely a cultural difference there. Apparently, like, yeah, Northern Italy, it's like, yeah, like, they'll eat early, but southern Italy, like, they're just… yeah.
Very late.
**Bryan Boreham** 01:22 Yeah, I think Spain's the worst I've seen you.
**Tyler Yahn** 01:25 You know.
**Bryan Boreham** 01:25 You read on Google Maps, the restaurant opens at 8. You go there, it's like, nope.
**Tyler Yahn** 01:31 Yeah, you go there, and you're, like, the early bird special. Like, you're, like, you're.
**Bryan Boreham** 01:35 Well, they're probably not your milk.
**Tyler Yahn** 01:37 Oh, yeah, oh, right, yeah.
They're probably, they're probably like, who's actually gonna show up at 8? Like, no one's gonna be… so we're not opening, yeah. No, 100%, yeah.
Where, are you in London, or are you just around there?
**Bryan Boreham** 01:52 Yeah, about.
**Tyler Yahn** 01:53 15 miles out from the center. Oh, okay.
**Bryan Boreham** 01:56 Pretty much.
**Tyler Yahn** 01:59 Yeah.
**Bryan Boreham** 01:59 London is kind of… Technically, a series of villages.
**Tyler Yahn** 02:04 Right, right.
Yeah, London itself is, is pretty small in the middle of the city of London, right?
**Bryan Boreham** 02:09 The city of London, yeah.
**Tyler Yahn** 02:10 Yo, I was there for, KubeCon, EU, I guess….
**Bryan Boreham** 02:16 Right.
**Tyler Yahn** 02:17 Sure. Yeah, and … it was the first time, like, I'd passed through London multiple times and, like, spent, like, a day or something, but, like, I spent, like, the full week, plus a little bit extra. That's a really cool city. I really was, like, impressed with it. It's a lot of stuff to do, a lot of, cool places to go see, … Also, the history there is kind of insane. I just, yeah.
**Bryan Boreham** 02:39 Where are you at?
**Tyler Yahn** 02:41 I'm in Portland, Oregon, so I'm in the U.S, so… Yeah, our history, that we know of is only, like, you know, 400 years old, right? So it's like, yeah, like… It's a joke, right? You guys have, like, businesses that are over 400 years old there, like… Yeah.
**Bryan Boreham** 02:59 Chef.
**Tyler Yahn** 02:59 But… Yeah, but I did go to see the City of London to go see, like… I mean, obviously, you can't see the original, like, London wall, that, like, apparently, like, the original, original, like, from the Roman times is, like.
Underground. But, like, the extension of it….
**Bryan Boreham** 03:16 There's bits of it hanging around.
**Tyler Yahn** 03:18 Oh, is it? Okay, yeah. Yeah, I was checking that out. I was like, man, I was just, like, super impressed with that. Yeah, I just couldn't believe how, like, much history was there. Yeah.
That being said, like, I was also in Turkey at one point, and like, yeah, if you want to talk history, like….
**Bryan Boreham** 03:34 Yeah.
**Tyler Yahn** 03:34 It's, it's definitely got a lot more, yeah.
**Bryan Boreham** 03:38 Yeah, I've been to the Cathedral and the bazaar.
**Tyler Yahn** 03:41 Yeah, right?
**Bryan Boreham** 03:42 Like, I….
**Tyler Yahn** 03:43 Like, the, like, all the, like, the blue mosques, right? Like, my favorite part about that is, like, well, okay, so originally it was, like, a, a church, then it was a cathedral, then it was, like, a mosque, then it was a church again, and then it was, it's like, oh my god, like, this just goes all over the place, like, yeah, it's, it's just… it's nuts, the history there. But yeah.
I… I do think, though, that, like, London's actually got, like, a lot going for it, because you can go to, like, the London Museum, and then you can see… I mean, you can see stuff from the Sumerian, like, world, right? I mean, that's… that's kind of cool, like, yeah.
**Bryan Boreham** 04:16 Stuff they plundered from all over the world.
**Tyler Yahn** 04:18 Yeah, I know, it's like, … that was the joke, it was like, well, you know, like, at least I'm benefiting from being able to see it all in one place. Like, I don't have to travel to, like, Iraq or something like that to go find this, yeah, but….
**Bryan Boreham** 04:29 That was mostly the French they took it from.
**Tyler Yahn** 04:31 Right? Yeah, well, yeah, and then the competition with the French made it even worse, right? Yeah, that Napoleon, he really… he really liked that stuff.
… I don't know if anybody else is showing up, actually. I know Robert's out, I know Sam's out, I know Damien's out, and then I think David is also out, so I don't know if he's, like… he's been floating in and out, so it might just be us today.
I've got an agenda, but it doesn't really, … it's… it's not really worth going over, honestly. Right. But I can… if you have topics you wanted to talk about, I know that you have, some PRs, I thought. We could maybe look at those.
**Bryan Boreham** 05:11 Well, yeah, one really, I mean… I… because… So, let me think. Last time was… I was at GopherCon UK, so I missed the last one, but the one before that, somebody was talking about… the PR to optimize the HEX conversion.
… And… I… I thought, well, I'll have a look at that. And then I thought, I can make it go faster.
So that's one of the PRs, but that's marked as draft, because it just totally crashed in unit testing. I haven't even gone back to that one.
**Tyler Yahn** 05:44 Okay.
**Bryan Boreham** 05:45 … But… I did.
think this thing needs more unit tests, so that's… That, that PR must be nearly ready.
**Tyler Yahn** 05:57 Oh, this one, this one, the more trace ID tests?
**Bryan Boreham** 06:00 Yeah, the one that's not marked as draft, yeah.
**Tyler Yahn** 06:02 Yeah, this does look gritty. I haven't looked back at it.
**Bryan Boreham** 06:08 So there's one undismissed comment, which is about fuzz testing. I… I… I started looking… In that repo.
there's….
**Tyler Yahn** 06:21 I… I don't think that should block this. I think, Robert is pretty good at coming up with ideas, that he doesn't particularly mean that you should be addressing in this PR.
**Bryan Boreham** 06:33 Yeah, sure, I just didn't want to kind of dismiss it without doing anything at all.
**Tyler Yahn** 06:38 Yeah, yeah, that's fair. I think, let's track this in an issue, ….
**Bryan Boreham** 06:43 Yeah.
**Tyler Yahn** 06:54 Yeah, I think that's… it's probably… I think it's a great idea.
But I think we'd probably want to do something like this.
**Bryan Boreham** 07:08 I did not know you could do that in GitHub.
**Tyler Yahn** 07:11 It's not the most friendly UI, but yeah.
Yeah, okay, cool, that looks good. And then, it's got two reviews, that are passing. I can… I could take another quick look at this. I think the only thing that I saw was just the naming, and I haven't looked back yet.
Which looks like you've addressed. So, yeah, this looks… this looks great.
Yeah, let's, let's, let's get this merged.
Oh, … okay. Alright, I'll update it. Alright, yeah, I'll plan to… I'll plan to merge it, though, once the CI tests pass. So then the next one is just this, optimize the ID parsing, and this is for this hex parsing. It's a revision… oh, update, okay.
**Bryan Boreham** 08:10 So, yeah, I… so, I don't even know what happened to the original one. I… I thought I could make it go faster, and my one crashed, so I just need to get back to that.
**Tyler Yahn** 08:20 Okay, alright, so this is still just kind of… burgers.
**Bryan Boreham** 08:22 Sorry, I've said that wrong. I… it's not that I made it go faster, … I made it smaller, because the… The original was, like, unrolling absolutely everything.
And, ….
**Tyler Yahn** 08:37 Hmm.
**Bryan Boreham** 08:37 So….
**Tyler Yahn** 08:39 Okay.
**Bryan Boreham** 08:39 mostly what I did, but, it crashed, so I need to figure out… And that was even… even with my extra unit tests. So, in some sense, they're not good enough.
**Tyler Yahn** 08:53 Yeah, okay, no worries. Yeah, I def… obviously, like, just, convert out of a draft once it's ready. I would also say, if you're gonna do this, make sure that you include some benchmarking. I don't know if we have bench… I think we have benchmarks for, oh, you already are, yeah.
Okay.
**Bryan Boreham** 09:11 Well, yeah, that's… that's in the original one, yeah, maybe I didn't post my results. I… I mean, that was kind of literally the ordering that I… I pushed one PR, I pushed another PR saying this needs more tests. I went back to the first one, it crashed in testing, so I marked it as draft, and then… … So yes, I should post the benchmarks, but I should get it to stop crashing before posting the benchmarks.
**Tyler Yahn** 09:38 Yeah, sorry, that's what I meant, just like, when you, when you do convert it, like, obviously, yeah, just keep iterating, locally, but yeah, that sounds good.
We also use, BenchDat, just a heads up on that one. You'll likely be asked to do that one. I don't know if you've seen this before.
… It's just, it helps the statistical noise. Yeah, so, just something, like, pretty much just, yeah, ask for something like that, but otherwise, you got a pretty good start on what we're, what we're seeing here.
So, yeah.
Okay, cool, yeah, I will… I'll definitely keep an eye on this one, I'll merge it.
In just a little bit, and then, yeah, we can keep going on that one.
I don't… yeah, I think that's it. Yeah, that's two PRs I saw, yeah.
**Bryan Boreham** 10:27 Yeah, I mean, I didn't look… is the one… because what happened is somebody else did the first, like I say, unrolled absolutely everything, and… is that one still open? I don't….
**Tyler Yahn** 10:36 I think it is, I know what you're talking about, … Yeah.
Yeah, actually, you have it linked in your PR. Let me share again.
**Bryan Boreham** 10:50 Just left so many windows open.
**Tyler Yahn** 10:53 Right.
I think this is the one that you're talking about.
**Bryan Boreham** 10:59 Yeah, okay, so that one's still open, yeah.
**Tyler Yahn** 11:03 Yes.
I see.
Yeah, so, you were reviewing this and you thought there's a more concise way to do it, is what you came to?
**Bryan Boreham** 11:30 Yeah, … Sorry, I'm trying to page that back in. This is 3 weeks ago now, or something like that. I, … Yeah, I get… well, I guess I was… I was totally unclear what was going on, because there's… there's, like, this auxiliary… Array, which is expressed as a string.
Which is used to decode this, that one.
**Tyler Yahn** 12:04 Yeah.
**Bryan Boreham** 12:06 … And… you know, I sort of squinted at that and thought, what the heck is going on? There has to be a better way to do this. And, … Completely failed.
to… I mean, I do think that thing is better expressed as a byte array than as a string, but that didn't make much difference to anything. So… … Yeah, but along the way, I just kind of… because they're basically… there's the same pattern. There's an 8-byte string and a 16-byte string, and so if you… if you code the 16-byte one as calling the 8-byte one twice.
Then it gets… the whole thing gets a lot shorter.
But, … That wasn't particularly meaningful, … And I don't remember anything else.
But yeah, that was kind of the start of it, is like, what the heck is going on here?
Well, I think that's.
**Tyler Yahn** 13:10 That's kind of like the, … Yeah, that's kind of my feedback for this PR. Like, this comment's, … it's great. It's a lookup table, but, like, how did you come up with this? … Yeah, so I think that… I think having some sort of comment here would have been, my feedback so far on this PR, like… This is pretty inscrutable, like, I don't… Yeah, ….
**Bryan Boreham** 13:36 So it ends up detecting two kinds of errors at the same time. One is where you have a character that's just not hex, and the other error is when every single character is a zero.
Because both of those are illegal, and … … Yeah, so there's kind of a bunch of things that you would… you would sort of never figure out.
… About what's going on in that code.
well, if you're me, without just sort of saying, well, I can do this better, and then three hours later going, well, no, I can't, but maybe I can do it shorter.
**Tyler Yahn** 14:11 Hmm.
**Bryan Boreham** 14:12 … Yeah, I don't know, I, … at the end of the day, it sort of… it depends a little bit exactly how much faster you want it to go, because we're sort of… we're sort of down in nanoseconds.
….
**Tyler Yahn** 14:30 Yeah, I don't… I mean, it's obviously, like, on the fast path for tracing, so, like, optimization is important, but, you know, what kind of results are we seeing? … I mean, that's… That's… I'd have to go look at what these tests are actually measuring, but if this is just a straight conversion of, like, one IDE, like, that's pretty significant. ….
**Bryan Boreham** 14:51 Yeah, but it's now at, like, 16 nanoseconds, so….
**Tyler Yahn** 14:55 Yeah.
**Bryan Boreham** 14:57 You know, a significant percentage difference would be 2 nanoseconds, and… Probably we don't care about 2 nanoseconds.
**Tyler Yahn** 15:08 Yeah, sure, yep.
Yeah, I mean, I do think that you're right, like, there is a point where we're getting diminishing returns on, like, the incomprehensibility of the code versus, like, performance improvements, but… I think this is also one that is kind of standing out as.
**Bryan Boreham** 15:26 Yeah.
**Tyler Yahn** 15:26 Reduction in allocations, which is going to be.
**Bryan Boreham** 15:28 Yeah, no, sure, that's… that's absolutely right. Yeah, I really have no, … No major complaints about that PR. I make the observation when I read it, I couldn't figure out what was going on, and … It's… it's sort of my… typical reaction is… is just to say, well, the, you know, next thing I have to do is try try and do it my own way, and then I'll figure out why they did it that way.
**Tyler Yahn** 15:58 Yeah, okay, see. Yeah, I mean, that's… it's a good approach.
I do think it… It does look like this PR is a little bit of abandoned at this point. I don't see much updates since 3 weeks ago.
**Bryan Boreham** 16:10 Yeah, so that's what I was trying to do, was wake it up and then neaten it up a bit. But obviously, my one has to not crash.
**Tyler Yahn** 16:20 Yeah, yeah, ideally.
**Bryan Boreham** 16:24 Not obviously crack.
**Tyler Yahn** 16:26 Yeah, yeah, even better, yeah.
Well, cool. Yeah, alright, well, I'll keep an eye out on that one. I'll keep an eye out on the other one as well for the tests.
But yeah, anything else you want to talk about? We could probably end it early, otherwise I don't think anybody else is gonna be showing up.
**Bryan Boreham** 16:44 No, that's fine.
**Tyler Yahn** 16:46 Okay.
**Bryan Boreham** 16:46 See you next time.
**Tyler Yahn** 16:47 Yeah. See you later, Brian.
**Bryan Boreham** 16:49 Okay.
**Tyler Yahn** 16:50 Bye.
