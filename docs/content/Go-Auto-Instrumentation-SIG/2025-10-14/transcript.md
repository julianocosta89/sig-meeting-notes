SIG: Go Auto-Instrumentation SIG
Date: 2025-10-14
Duration: 16 minutes
Zoom Recording URL: https://zoom.us/rec/share/dDH6773r4nJnD4BTulNl2iW_rmJCgedtOjhAXIVMyZIwaBBih15M9JvtR35kdAM9.eMjWSNpj9zAvhDIM
============================================================

## Zoom Recording Transcript

**Mike Dame** 00:29 Hello, Tyler.
**Tyler Yahn** 00:31 Hey, Mike, how's it going?
**Mike Dame** 00:33 Good, how about you?
**Tyler Yahn** 00:34 Doing well. Yeah. Doing well.
What's the… what's the life like over there on the East Coast?
**Mike Dame** 00:44 Cold and rainy.
Not too different for you, right? You're in Seattle.
**Tyler Yahn** 00:50 Portland, but yeah, it's… yeah. I guess today and yesterday were pretty good, though, actually. It's like…
A little cold, but sunny, so, it's definitely fall weather.
**Mike Dame** 01:03 Yeah, it's… it's the, New England falls kicking in with the rain, 50 degrees.
**Tyler Yahn** 01:10 Yep. It goes in.
**Mike Dame** 01:11 Bite up the pellet stove, make some stew.
**Tyler Yahn** 01:16 Nice, yeah, I've actually been looking about getting a pellet stove, it's interesting you have one, yeah. Would you…
**Mike Dame** 01:23 It was built… it's, it was in the house when we moved in. It's, built-in, so it's really nice. It gets the house hot, and it'll… you need a humidifier to run with it. Oh. Just put a humidifier… I mean, you know, knead it, but it's way too dry for me without it, but that's…
If you're looking at them, that's the biggest tip I'd have, is get a good humidifier, put it right next to the pellet stove, and your sinuses will thank you.
**Tyler Yahn** 01:48 Yeah, I do remember that from other houses. I've had fireplaces as well. It's like, you always have, like, put, like, even, like, a pot of water on top, just to, like, have it… but it never, never works the same.
**Mike Dame** 01:58 Yeah, even a fireworks a little bit better, but yeah, we like it. Annoying part is just buying pallets. Every year, you get Home Depot to deliver a pallet of them, and…
**Tyler Yahn** 02:09 Yeah.
**Mike Dame** 02:10 It's pretty warm.
**Tyler Yahn** 02:11 Yeah, I think that's kind of a cool idea. I keep going back and forth on whether that or natural gas, but it just happens.
**Mike Dame** 02:17 Yeah, we're moving in a couple months, and we have a gas fireplace in the new house, and that, if I had the choice, I think I would go with gas, just because it's a pain to kind of work with the pellets, and always having to lug the bags up and down the stairs.
**Tyler Yahn** 02:31 Oh, yeah.
**Mike Dame** 02:33 It's a nice, you know, natural, clean approach, you know, if you want to go pellets versus gas, there's probably about the same.
**Tyler Yahn** 02:41 The thing that, like, stands out is, like, the gas goes out, the pellets don't… I mean, I guess you can run out of pellets, but you can stockpile that, right? Like…
**Mike Dame** 02:50 Yeah, oh, yeah, I guess if you have, like, a gas, tank at your house.
**Tyler Yahn** 02:56 Oh, yeah, you could do that too, right? Yeah.
**Mike Dame** 02:58 But, I guess if you're just hooked up to, like, the city gas line, you should be…
**Tyler Yahn** 03:03 It doesn't run out, right?
Well, yeah, I know, I… it's always, like, I use it as, like, a backup for when the electricity would go out, is what I'm thinking, so… I… you're right, like, I don't think the gas is gonna go out, like, but…
**Mike Dame** 03:17 I didn't know what you meant.
**Tyler Yahn** 03:18 But yeah.
I mean, just, like, I have… I've had gas in the past, and it has, like, been turned off while they're, like, fixing a main or something like that.
**Mike Dame** 03:25 Oh, yeah, yeah.
**Tyler Yahn** 03:27 Usually they're smart about it and do it in, like, the summer, but, like, you know.
**Mike Dame** 03:30 Yeah, that's true, yeah, with the pellets, when you have your supply, you're, you're stocked up.
**Tyler Yahn** 03:35 Self-sufficient, right? Yeah.
**Mike Dame** 03:39 Yeah.
So, it's still holiday season in Israel, so I don't know if Ron is going to be joining. We did have… Barun is another person from our team that he was… he had some stuff that we were thinking about contributing upstream.
just some changes… I mean, we don't have to have the whole meeting right now, but throw it… run it by you. The, we made it so that you can share, maps
across processes, I think it was already something that was in Obi, just not for the Go.
**Tyler Yahn** 04:11 So…
**Mike Dame** 04:11 If it makes sense to contribute that, you know, we have the work
done already, we're doing it now, so, we could… we could contribute that pretty easily, so… I'll see if he's around, otherwise we'll try… it's actually… he's in India, so it might be a little late for him, honestly.
But otherwise.
Michael on that.
**Tyler Yahn** 04:31 Yeah, I mean, if you can, if you can follow up on them…
to try and get that contribution, I think that sounds great. Like, that's really the only thing that's kind of top of mind for me, is, like, starting to work on that migration, or the integration, I guess is a better way to say it, of, like, the probes, with Obi and,
the audience rotation. Still kind of high up top of mind. I don't have the time to be working on it right now, and I know Nicola's also pretty busy, so, like, it's not something I'm actively working on, but, like, that's kind of, like, the next big hurdle.
And what you're describing is definitely something that, lends to that solution, so I think that that'd be great to see,
see a PR for that, I'd definitely be interested, yeah.
**Mike Dame** 05:10 Sending him a message…
But, I mean, it says it's 10 o'clock for him right now, so…
**Tyler Yahn** 05:21 Yeah, I mean, I don't… he doesn't need to join, that's not critical.
**Mike Dame** 05:25 Oh, cool.
pull that. I'd like to, you know, we try to contribute more stuff that we've done, too. We have our own… we basically… our model is we fork the upstream,
And we use that framework, and so we try to pull as much as we can from there. But, you know, we make improvements and stuff, and I like to contribute some of that back, whatever would be helpful, so…
I know I've been… pretty busy with Otago's stuff lately, but…
Love to get more involved in bringing more stuff upstream.
**Tyler Yahn** 05:56 Yeah, I mean, I'd be interested in seeing that as well. I'm happy to review. I've definitely got time to do some reviews, so that makes sense. But yeah, I,
like, I'm also quite busy, this month, at least. Next month, I'm hoping to get back, into committing more… that exact thing I was just talking about, so…
Any sort of, like, fixes we can include here, I think I'd be interested in seeing.
**Mike Dame** 06:21 Cool.
Yeah, okay, Bruin said he's not going to be able to join today. It's… it's late for him, but we'll…
We'll get that PR together, because I think that that would be a good one, and see what else we can… we can bring back. Yeah, I think otherwise, I don't know if we have…
Early quorum of… Talk about more.
**Tyler Yahn** 06:40 We don't really have an agenda either, so it's not, critical. Yeah. I was kind of just waiting to see if people wanted to join. I was gonna, like, there's really nothing to review, actually, so, yeah, like, that's also the other thing. It's just nothing's been going on, so…
Yeah, we can… we can call here. Good seeing you, though. Yeah.
**Mike Dame** 06:57 Yeah, always. We'll see, in two weeks, see if we have anything else by then, or if not, I'm not gonna be able to make… I don't know if I told you, I'm not gonna be able to make the maintainers, thing on… on Sunday. If it was Monday, I would have been able to, but the schedule's gone.
**Tyler Yahn** 07:13 Yeah, I know, it's kind of annoying it's on Sunday, like, a lot of people are having that exact problem, so, yeah.
**Mike Dame** 07:20 Love to, obviously, but… just… I have to leave on Saturday, and then that's just kind of a long week away.
**Tyler Yahn** 07:28 Yeah, I get it. Like, I… there's a lot of commitments from people for that kind of stuff, so… No big deal. You're gonna be at the conference, so we'll see you at the observability booth no matter what, so, yeah, I mean, that sounds good, but yeah.
**Mike Dame** 07:40 Oh, it looks like, David just… I think,
David's joining now, but we were just about to, call it, I think, David, because we don't really have an agenda or quorum.
**David Ashpole (dashpole)** 07:52 Alright, cool. Well, I'm actually just here to say hi, and to say that
Which I think both of you already know, but I'm the TC liaison for…
Go auto transportation now, so…
**Tyler Yahn** 08:04 Oh, cool.
**Mike Dame** 08:05 Good to have you.
**David Ashpole (dashpole)** 08:06 Yeah, I'll show up every once in a while, but…
**Mike Dame** 08:10 Cool. Well, it's good to know who our… who our liaison is. So, yeah, that's, I know it was…
There's a couple different people vetted, I think, were acting as it, kind of, before.
But… yeah.
**David Ashpole (dashpole)** 08:22 You do still have a GC liaison, but…
**Mike Dame** 08:24 Maybe that's who I'm thinking of.
**David Ashpole (dashpole)** 08:26 They're like… honestly, probably more useful, because I don't know if your work is going to touch the spec.
Or, like, TC-related stuff that much, but…
I am here. And I will… I will try and pay attention a little bit.
**Mike Dame** 08:41 Cool. Well, thanks.
I think we're… I think we're good then.
**David Ashpole (dashpole)** 08:46 Cool.
**Tyler Yahn** 08:48 Alright guys, I'll see y'all, in two weeks.
**Mike Dame** 08:51 Yep.
