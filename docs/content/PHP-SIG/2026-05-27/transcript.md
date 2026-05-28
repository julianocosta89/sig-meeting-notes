SIG: PHP SIG
Date: 2026-05-27
Duration: 18 minutes
Zoom Recording URL: https://zoom.us/rec/share/L8FVVoJugPSODh5K0st-wgSTZZdAv2Rb5NeqIQXMDAw-qdxkGOtsMU3G4B0yAfPn.aVzQ_7k4ACEZ3ODp
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:12 Booker.
**Bob Strecansky** 01:13 back.
How are you?
**Chris Lightfoot-Wild** 01:16 How's it going?
**Bob Strecansky** 01:17 Pretty good, how was your vacation?
**Chris Lightfoot-Wild** 01:20 Yeah, it was really good, thanks, yeah.
**Bob Strecansky** 01:22 Nice.
**Chris Lightfoot-Wild** 01:22 Got back on, what was it on Monday.
**Bob Strecansky** 01:27 Nice.
**Chris Lightfoot-Wild** 01:28 Body clock's a bit messed up.
**Bob Strecansky** 01:30 Yeah, that's what happens.
**Chris Lightfoot-Wild** 01:33 Yeah, we were, for the most part, obviously 11 hours behind UK time. And then, on the way back, we had, like, 3 nights in Vegas.
So we're 8 hours behind.
And unbeknownst to us, until we got there, it was Memorial Day weekend.
**Bob Strecansky** 01:50 Yeah, that's a busy time in Las Vegas.
**Chris Lightfoot-Wild** 01:52 Crazy.
**Bob Strecansky** 01:54 I haven't… I haven't gone there in a couple of years. I went there… many years ago for my bachelor party, and then I've gone a couple times since then, and it is… It's hard to explain to people that haven't been there.
**Chris Lightfoot-Wild** 02:08 Yeah.
Yeah, I've been a couple of times now as well, just went, when we… on our honeymoon, so that was, like, 8 years ago?
And then, that was just, like, some random weekend, so it was fine. But this time, we were, like, you know, weaving in and out of people in corridors and walkways and everything, just… crazy.
**Bob Strecansky** 02:28 A lot… a lot going on, huh?
**Chris Lightfoot-Wild** 02:30 Yeah, I mean, we had a good time, so… yeah.
With some shows, so Penn & Teller again.
Some guy called Shim Lin, like a magician?
**Bob Strecansky** 02:41 I don't know.
**Chris Lightfoot-Wild** 02:43 No, we didn't either, so we, we just, you know, sort of look and see what last-minute tickets we could get, so…
**Bob Strecansky** 02:50 Nice.
**Chris Lightfoot-Wild** 02:51 Yeah, good for now.
**Bob Strecansky** 02:54 That's good, glad you got some R&R.
**Chris Lightfoot-Wild** 02:57 Yeah, thank you. How's, stuff going?
descend.
I'm missing much fun.
**Bob Strecansky** 03:03 You didn't miss a whole lot of fun here.
It's just, I think Sergey and Hal are just working on the distro still. I actually got the main CI green, which is kind of exciting.
**Chris Lightfoot-Wild** 03:19 Awesome.
**Bob Strecansky** 03:20 Yeah, there's a pull request open that I need you to review, and then I'll merge it, and then it'll be in good shape. It's just two simple things I put in the agenda.
But… Besides that, not a whole lot, just… Black and through. We had, there was a big… layoff at Intuit. I wasn't affected, but a lot of my coworkers are gone now, so it's been a very strange week for me.
**Chris Lightfoot-Wild** 03:45 Well, I'm sorry too.
**Bob Strecansky** 03:48 Yep, me too.
Me too. Is it just the two of us today?
**Chris Lightfoot-Wild** 03:56 Goodbye.
**Bob Strecansky** 04:01 Chris, did I lose you?
**Andrii Androshchuk** 04:12 Right.
**Bob Strecansky** 04:14 Hello.
**Genivaldo Silva** 04:41 Hello.
**Bob Strecansky** 04:43 Whoa.
Can y'all hear me okay?
**Genivaldo Silva** 04:54 I don't. I can hear you.
**Bob Strecansky** 04:56 I think… I think Chris froze, but we'll wait for him for a minute to get back.
I'll turn off my camera and see if that helps.
Yeah, Chris said he… his laptop was having a moment, so he'll be back in a minute, and then we can get started.
Andra, Jenna, all the hell y'all doing today?
**Andrii Androshchuk** 06:52 Been good.
**Genivaldo Silva** 06:56 And the boot.
**Andrii Androshchuk** 07:00 And you…
**Bob Strecansky** 07:02 Yeah, Chris said, get rolling, he'll be right back, so, we can do that.
Did you all have, specific agenda topics that you wanted to discuss today?
**Andrii Androshchuk** 07:15 Not particular, just came to listen and participate.
**Bob Strecansky** 07:19 Cool, thanks. Glad you're here.
Alright, we'll walk through the boards really quick and see.
What's up?
Looks like there is… New PR for W3C baggage size and entry count caps, so… View that later today… Renovate, renovate, renovate, renovate, renovate.
**Chris Lightfoot-Wild** 07:49 Hello.
**Bob Strecansky** 07:49 Hey Chris, welcome back.
**Chris Lightfoot-Wild** 07:52 Sorry about that, I just, how do the plans, I had to reboot it.
**Bob Strecansky** 07:55 I'm good.
So, this was the PR that I was talking about earlier, Chris. I just added, Psalm fix and a, PHP support error fix, and now this one has all green for CI, which is really exciting, so we're gonna, once you're able to review that, we'll merge it in, and that should, reduce a lot of friction, I'm hoping.
**Chris Lightfoot-Wild** 08:19 Yeah, cool, I'll, take a look at that one.
**Bob Strecansky** 08:22 And I'll have to get back to this OTLPHCP response body one, I just haven't had a chance to get back to that yet.
And…
**Chris Lightfoot-Wild** 08:37 Hi, hi to Andre and, Jenny Valdo as well. I'm not sure if you've met, yourself, Jenny Valdo, but, Good to see it.
**Bob Strecansky** 08:49 Piercer Suguzzle…
**Genivaldo Silva** 08:54 Oh, huh.
**Bob Strecansky** 08:55 I think.
**Genivaldo Silva** 08:55 Are you speaking on mute?
Hello, Chris.
**Bob Strecansky** 09:02 Andre, thank you for reviewing this, peer service attribute to God's all thing, that's really helpful.
**Andrii Androshchuk** 09:10 True.
**Bob Strecansky** 09:13 What's what we got going on here?
Looks like I needed to read that one, too. Oh, that's right, we talked about that being… oh, no. GitHub!
That's not good.
Yeah, I think that's… those are all the main ones.
And then these are probably… I'll just renovate. Yep.
So I'll have to do that. I did, add PHPT tests, Chris. You could probably review this one, too.
**Chris Lightfoot-Wild** 09:45 Yeah, yeah, take a look.
**Bob Strecansky** 09:47 Yeah, those are just AI-generated tests, but I think it will be helpful for test coverage in this repo.
Alright, so that's all that, and then let's check out the project board, see if there's anybody that has anything that's… Right, I'm waiting on the response body size limitation. I need to work on that. And then, we had a volunteer volunteer for the MAGO, review. As you may or may not remember, Chris, we put the… that new CI test.
Into place, and we'll see if they're gonna compare how, some PHP stand versus MegaWorks, so that will be cool to see.
**Chris Lightfoot-Wild** 10:28 Yeah, exciting.
**Bob Strecansky** 10:29 Yeah, that is… we live in exciting times.
And then, let's take a look at packages really quick.
We are almost at 40 million installed, that's exciting. It looks like we're still making really good progress. It feels like people are starting to use this library more, which is also good.
**Chris Lightfoot-Wild** 10:46 How's the… the… oh, sorry, is it just about the 8.5 adoption looking? Obviously, that's…
**Bob Strecansky** 10:51 Oh, you know what?
Let's see, 8.5… Where… oh, that's… How do you do not…
**Chris Lightfoot-Wild** 11:02 I have very close shades of blue.
**Bob Strecansky** 11:04 Well, I'm saying that you click on one of them, and it disappears, but it's… they start all selected, so… I don't know.
Looks like 5-4 usage has… Or, sorry, 8.5 usage has… oh, that's a really bad UI.
Let's see where it is here.
What color are you? You're this one?
Looks like… Wonderful.
**Chris Lightfoot-Wild** 11:32 The bottom ones, I guess, maybe.
**Bob Strecansky** 11:34 Yeah, 1… 1%, 2%, 8%. Wow, it's gone up from… In the last, like, 5 months, it's gone from… Zero… 0 in, you know, October to 10%. I guess that's about what I would expect.
**Chris Lightfoot-Wild** 11:53 I'm only asking because I remember there was some, like, pipeline work where it was failing on 8.5, I think, wasn't there?
**Bob Strecansky** 11:58 Yeah, I think…
**Chris Lightfoot-Wild** 12:00 I need to fix that.
**Bob Strecansky** 12:01 I think that that is resolved with that PR that I… Gave you.
**Chris Lightfoot-Wild** 12:06 No, sorry, so yeah, I'll take a look.
**Bob Strecansky** 12:08 No sweat.
No sweat at all.
Okay.
Alright, that's… that's all that I have for today. Does anybody else have anything they'd like to discuss?
**Chris Lightfoot-Wild** 12:30 Well, I wouldn't have minded, I had a quick look at Andre's, review of my PR, I wouldn't mind just quickly… Flashing some of that out, if that was alright.
**Bob Strecansky** 12:40 Yeah, sure.
**Chris Lightfoot-Wild** 12:41 Maybe just in the open, because the… I wanted to kind of explain my understanding.
**Bob Strecansky** 12:45 Yeah, you wanna, you wanna drive, Chris?
**Chris Lightfoot-Wild** 12:49 Sure? When I… yeah, one second.
See if my laptop doesn't melt into the… Dusk again?
It's just really hot here, sorry, for UK, so… All the devices are getting mega, mega hot.
**Bob Strecansky** 13:07 Oh, no.
How hot is it now?
**Chris Lightfoot-Wild** 13:14 So, in the office at the moment now, well, like, I guess from where I'm at, 27 Celsius, which is…
**Bob Strecansky** 13:21 Oh, wow.
**Chris Lightfoot-Wild** 13:22 8 to 4 Fahrenheit-ish, roughly, is that?
**Bob Strecansky** 13:25 It's a warm day.
**Chris Lightfoot-Wild** 13:27 Yesterday, it was 96 in here. I've got no icons, so it was just horrible.
**Bob Strecansky** 13:31 Oof.
**Chris Lightfoot-Wild** 13:33 Sorry, I'm just gonna buy some time, I'll look for the PR.
**Bob Strecansky** 13:39 Also, you're used to… you… we're in America, where air conditioning is everywhere, so…
**Chris Lightfoot-Wild** 13:44 Yeah, you know, in Vegas in the middle of a hot desert, and yeah, all the air coming felt nice.
When you're indoors, at least.
**Bob Strecansky** 13:52 Yeah.
**Chris Lightfoot-Wild** 13:59 Oh, I've just got the… Oops page as well on GitHub. Come on.
**Bob Strecansky** 14:03 Oh…
**Chris Lightfoot-Wild** 14:06 Alright, nice. There we go.
I'll transition the screen… Cool, so yeah. Thanks, firstly for taking a look at this, Andre.
one I wanted to sort of check about… Or maybe explain my… thinking was… on this? He was talking about… The bit in particular, define it once for the entire library.
I could be wrong in this, but my understanding was to try and… Have the, sort of, traces The specific version that they're emitting telemetry for.
So, like, if obviously you've got messaging components, like, in the queue parts of Laravel.
We might have only instrumented that.
to the SEMConv of, you know, 138 or something at the time.
But there might be some other changes.
In another component, that we can say, oh, we've just omitted telemetry at 1.45.
Without having to go back and change them all at once.
So it allows you to independently update the various components to the new… to the specific version that you're emitting telemetry for.
Rather than just say, all of Laravel has to be at one specific version, and then it's more of a maintenance burden.
to go through and update everything, every time we bump the SEMCOM package.
But that's my current understanding, and Bob, I don't know if that sounds about right from your understanding, or… I might not have provided much context there, sorry, but…
**Bob Strecansky** 15:57 Yeah, I think you're right, Chris.
**Chris Lightfoot-Wild** 16:01 So, yeah, it was roughly trying to break apart from what we've currently got now to the centralized cached instrumentation, where it's, like, one version.
To allow us to… Maybe more easily stay on top of it in future, and bump specific bits of it as and when we can.
So, does that sound, like, roughly like it makes sense? Are you happy with that as a…
**Andrii Androshchuk** 16:25 Yeah, that makes sense, I was just curious whether there was a particular reason behind that.
**Chris Lightfoot-Wild** 16:32 Yeah, I'm not against updating the SEMCOM version, but obviously, I was trying to keep it lower, and then maybe… Because this has been a very long-running PR now, and I apologize for that, because I've got a bunch of conflicts to fix, and I'm, you know, still not quite there with it.
And some of the comments that Nevey has seen as well, sorry, made separately, on some of the PRs about, spam suppression.
I think was something I wanted to try and incorporate into this, so still… Still got some work to do, but I'll, I'll try and look a bit further through this when I've got some time. I'm just… Back from holiday slash vacation, so I'm just trying to catch up on a few bits and pieces, But yeah, I appreciate you, taking a look at that, and, like, it… with, like, someone with… such as yourself with, like, more exposure to Laravel, it's good to get a second opinion on, like, the proposed changes, And if we should be doing it that way at all, because it was obviously the sort of split from how other… some of the other instrumentation is currently set up.
But… Again, totally open to suggestion if you've got, you know, changes and whatnot to make to it, then… Yeah, I'd love to incorporate that stuff, but… Thank you very much for taking the time to…
**Andrii Androshchuk** 17:56 Sure.
**Chris Lightfoot-Wild** 18:00 Cool. That was a MeBo, I'm sorry.
**Bob Strecansky** 18:03 Excellent. Well, I guess we can adjourn. Thanks, y'all.
**Chris Lightfoot-Wild** 18:08 Cheers, sir. Speak to you later.
Boom.
