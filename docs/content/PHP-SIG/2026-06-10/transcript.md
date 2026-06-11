SIG: PHP SIG
Date: 2026-06-10
Duration: 26 minutes
============================================================

## Zoom Recording Transcript

**Bob Strecansky** 03:39 Whoa…
**Chris Lightfoot-Wild** 03:47 Hello, are you okay?
**Bob Strecansky** 03:49 Doing alright, how about you?
**Chris Lightfoot-Wild** 03:51 Alright, thanks, yeah.
When did the fair ones turn up today?
**Bob Strecansky** 03:55 Maybe not. Traffic was miserable this morning, so I was, I was floundering a little bit, but I'm here now.
**Chris Lightfoot-Wild** 04:05 No tennis today.
**Bob Strecansky** 04:07 Not today, it's a little rainy today.
But… I don't get to play every day, I get to play, like, 3 times a week, probably.
**Chris Lightfoot-Wild** 04:18 I didn't know if it was, like, a Wednesday ritual or something.
**Bob Strecansky** 04:21 Oh, usually… yeah, usually it's whenever… so, we have this facility that's, like, Trying to think.
Non-freedom units for a second.
It's probably, like… 15 kilometers from me, north.
And… It's, They have 4 courts, and when you can book an indoor one, you… 4 indoor courts, and when you can book an indoor one, you do.
**Chris Lightfoot-Wild** 04:52 Okay.
**Bob Strecansky** 04:54 So…
**Chris Lightfoot-Wild** 04:55 We, we don't use, kilometers, bizarrely, in,
**Bob Strecansky** 04:58 Oh, you don't?
**Chris Lightfoot-Wild** 04:59 No.
**Bob Strecansky** 05:01 That's amazing.
**Chris Lightfoot-Wild** 05:01 Miles is more relatable, to a degree, than…
**Bob Strecansky** 05:04 Oh, okay.
**Chris Lightfoot-Wild** 05:05 Yeah, it's weird. We use yards and miles for driving and navigating and… meters for other measurements, and… although height and weight is typically… well, height is typically in, Imperial still, yeah.
**Bob Strecansky** 05:19 Oh, really?
**Chris Lightfoot-Wild** 05:20 Yeah.
**Bob Strecansky** 05:22 Are you… are you tall, or are you short?
**Chris Lightfoot-Wild** 05:24 I'm one of those.
**Bob Strecansky** 05:26 You're one of those.
**Chris Lightfoot-Wild** 05:28 Well, 6'4".
**Bob Strecansky** 05:31 Yeah, you're tall.
I'm… anybody who's… I'm 6'2", anybody who's taller than me is very tall.
Alright, we're 5… we're at 5 after, so I guess we can just… let's get rolling, and if, if anybody else comes in, we can… Continue to talk through whatever we need to, but… Let's see… Telemetry, PHP setting… Sorry, there's too many Zoom things.
**Chris Lightfoot-Wild** 06:04 Notice.
**Bob Strecansky** 06:07 That's us.
Today is the 10th.
Do you have any big, agenda plans over the summer?
**Chris Lightfoot-Wild** 06:30 For here, sorry.
**Bob Strecansky** 06:32 Yeah, I said, do you have anything big going on over the summer?
**Chris Lightfoot-Wild** 06:35 Oh, we're going, we're doing a few weekends away, like… My wife wanted to basically kind of get away every month, at least something.
But even if it's just a few, you know, a few days, going to, like, Tenerife at some point, and… Sorry if we went to Portugal somewhere. Yeah, we went to a handful of places. You can tell that sheep landed, not me.
**Bob Strecansky** 07:03 My wife is an excellent trip planner, and I am not.
**Chris Lightfoot-Wild** 07:06 Yeah, I just carry the bags.
**Bob Strecansky** 07:08 That's right. And pay the bills.
**Chris Lightfoot-Wild** 07:13 Yeah.
**Bob Strecansky** 07:14 Yeah.
**Chris Lightfoot-Wild** 07:15 What yourself, Ethan? Ethan?
**Bob Strecansky** 07:17 Yeah, in, 3 weeks, my brother is getting married.
**Chris Lightfoot-Wild** 07:22 Nice, yep.
You went on a… I forgot to ask, you went on a stagger, didn't you?
**Bob Strecansky** 07:28 Yeah, we did, we went to…
**Chris Lightfoot-Wild** 07:29 Like, South Texas or something.
**Bob Strecansky** 07:31 Yeah, that was… that's it.
We did, and it was amazing. This is where he's getting married, in Highlands, North Carolina.
**Chris Lightfoot-Wild** 07:40 Wow.
**Bob Strecansky** 07:41 Yep.
**Chris Lightfoot-Wild** 07:42 Amazing, that's beautiful.
**Bob Strecansky** 07:43 Yeah, it's in, it's, like, two… a couple hours north of us.
And then, I'm also going to… Buzzards Bay, Massachusetts, for… A week. My wife's family lives here.
**Chris Lightfoot-Wild** 08:00 Okay.
**Bob Strecansky** 08:01 So, we're gonna go visit them.
**Chris Lightfoot-Wild** 08:02 That's nice.
**Bob Strecansky** 08:03 Have you heard of, I don't know why you would have. Have you ever heard of Cape Cod, Massachusetts before?
**Chris Lightfoot-Wild** 08:10 I feel like I've heard Cape Cod, but I don't know about the Massachusetts bit, I don't know if that's the same as Mother Warren, or…
**Bob Strecansky** 08:17 No, Cape Cod is a… like, it's a very famous, a very famous inlet in, peninsula in Massachusetts, and it's, like, where a lot of the… It's where a lot of the Northeastern elite go to vacation, and it's just very fascinating, because it's, like, a lot of… popped collars and pretentiousness and all that stuff. And her family lives in, like.
one of the… there's, like, one bridge that gets onto Cape Cod, and her family lives just before you get onto the island, and it's just, It's nice, because, like, a lot of the lobster and… Good weather in the summer, but not, like, a lot of the elitism.
**Chris Lightfoot-Wild** 09:02 Nice.
**Bob Strecansky** 09:03 Yeah.
**Chris Lightfoot-Wild** 09:04 Hope you have a great time.
**Bob Strecansky** 09:05 Yeah, me too. Alright, so let's walk through these repos real quick. Why did this start failing again? Oh, I guess… I know why, because we haven't had any, any new PRs come in since we made… since I made the fix.
Oh, so this is the CI fix.
And then… some of these have been open since then.
Let's see, why did this fail?
PHP…
**Chris Lightfoot-Wild** 09:40 I mean, it might be this, depends.
I'm not hungover.
**Bob Strecansky** 09:44 I haven't installed… yeah, it looks like, there's some dependencies that are… Broken.
It's just… this is… I think Renovate is more… it's more a hassle than it's worth sometimes.
**Chris Lightfoot-Wild** 09:56 Yeah, it doesn't… especially when it's doing one package at a time, and it doesn't seem to, like… figure out the interdependencies, and I don't know, maybe it's just… I've not seen enough of it.
**Bob Strecansky** 10:07 We probably… well, this one's fine. This one's just a code coverage thing, but… So it must just… that's also frustrating that… It reports failure when everything is good except for the code coverage.
**Chris Lightfoot-Wild** 10:23 Yeah.
**Bob Strecansky** 10:24 Yeah…
**Chris Lightfoot-Wild** 10:25 I could have moved that one, though, sorry, so that's, if you're happy with it, you, fire away.
**Bob Strecansky** 10:30 Hi, Ken.
Alright, but was there anything… more importantly, was there anything else in here that was worth… Talking through… Oh, Sergey was working on this, I don't know what his state is on that, but the rest of this stuff is just… Old.
Bananas.
Should probably go ahead and clean that up at some point.
Looks like there is a Laravel fix?
**Chris Lightfoot-Wild** 11:00 Yeah, I was just looking at it just a minute ago, so, yeah, I'll finish that one up, and hopefully I can just manage that one.
**Bob Strecansky** 11:07 Professor.
**Chris Lightfoot-Wild** 11:08 Looking good pipeline-wise for Laravel. I think there was some issues, though, but I'll give it a test.
No issues with this, sorry, just the… still with the workflows, but…
**Bob Strecansky** 11:18 Got it.
Okay.
What, what else do we… well, and it's interesting that this one passed all CI checks.
**Chris Lightfoot-Wild** 11:27 Well, the only one… I've used to prove the flow, because it was probably only the easy CLA.
**Bob Strecansky** 11:31 Oh, yes, that's true. Sorry.
**Chris Lightfoot-Wild** 11:34 Oh, sorry.
**Bob Strecansky** 11:35 Yeah, you… I know you were work… I'm sorry, I know you were working on the fix for this repo, and we merged that one PR. What… do you know what's left?
**Chris Lightfoot-Wild** 11:45 There's… yeah, there's a handful, because obviously there's, like, the build matrix, so some of the.
**Bob Strecansky** 11:51 Hmm.
**Chris Lightfoot-Wild** 11:52 it looks like there's 40-odd to 50-ish failures, but that's… if you divide that by 4, this is, like, 12, 13, so it's not as terrible, and there's some that are just needing, like, fan slash Psalm, suppression, etc.
**Bob Strecansky** 12:05 Okay.
**Chris Lightfoot-Wild** 12:06 I did actually want to add that to the, agenda, actually, if… I should have thrown that… I'm sorry.
**Bob Strecansky** 12:13 You're good, nope. It's very informal.
**Chris Lightfoot-Wild** 12:18 So do you want me to… I'll stick that on, we can come back to it if.
**Bob Strecansky** 12:22 If you wanna, yeah, if you wanna stick it, and we can come back to it, or we can talk about it now, whichever one you'd rather.
**Chris Lightfoot-Wild** 12:26 Sure, I suppose it with the two of us, it's, like.
**Bob Strecansky** 12:28 Yeah, it's a little, it's a little…
**Chris Lightfoot-Wild** 12:29 It was… I was just looking at, like… and I've had this discussion about, like, static analysis tools and, fixed… linters and fixes and Margo and stuff in the past.
But even looking at, like, you know, Symphony and Laravel, which are some of the bigger frameworks in the PHP ecosystem. They're using PHP Stan, and potentially SAM, but not… neither of them have got fine there.
So I'm wondering if you even just lean it down by reducing just fine completely. Like, do we really need that? Because I fed that into, Get AI's opinion, with ChatGBT, and or Gemini, one of the two, forget now.
And it was saying, PHP Stan sort of evolved quite a bit since maybe the old days of FAN being around, so it's kind of covered everything that Fan was doing, and it's just… The suggestion then was actually some of the things that you're annotating, they step on each other a bit. It's a bit of, like, landmines slash danger ahead.
Yeah, I think…
**Bob Strecansky** 13:33 Yeah, I feel like there's that, like, there's, like, a… definitely a straight line, right? It's like, it started as Peach P… it started as Fan, then you added Peach P-Stan, then you added Psalm, then you added a bunch of other things, then you add Rector for… for, like… upgrades, and then I think Mego is now the next, like, the next iteration in that cycle, but it's like, it's difficult to get yourself to remove the old one when you know it's functioning properly, and it doesn't really have that much impact, but obviously it does have an impact of Colliding with the next thing.
**Chris Lightfoot-Wild** 14:12 Yeah, I wondered if, like… Because it was in… it was in the core repo, the core PHP one, and then contribute.
But it was looking a lot healthier in cost. I thought, obviously, if I'm proposing dropping it.
from at least contrary, it looks like we're out of whack, but I didn't know if, ideally, you were thinking, if Mago is the up-and-comer.
there's a point in the future where we kind of want to just have that, and not all the things, so, like.
**Bob Strecansky** 14:38 Yeah, yeah, that's… Sorry. Yeah, that's… that's my… that's my hope, is that it works… works out fine for the… The root repo, and then we can do it and contribute, too.
**Chris Lightfoot-Wild** 14:52 So, the fact that fans still exists in Contrib, are you against removing that out of the second, or…
**Bob Strecansky** 15:00 I don't really… so, I don't really have, like, strong… I don't really have strong convictions either way.
I think if we think that removing fan from contribib is going to… it's going to not be detrimental and will help with momentum, that's fine with me.
But I also would like to eventually get to the point where we're using… like, I think… Mega is, like, what I envisioned, like, 6 months down the road to be, and I guess we have to, like, determine what we need to do to walk that back so that we can get it rockin'.
**Chris Lightfoot-Wild** 15:34 I think.
**Bob Strecansky** 15:35 First, we have to, like… Hopefully, I didn't get to see if that… person did anything with that, ticket, let me see.
Here it is.
**Chris Lightfoot-Wild** 15:45 But anything in addition?
**Bob Strecansky** 15:48 Not yet.
**Chris Lightfoot-Wild** 15:48 both pass.
**Bob Strecansky** 15:56 Yeah, this one, like, they're all the same. Yeah, of course they are, because it's the same error. I don't know who this person is, but… Looks like they're a new, eager beaver.
But yeah, I would like for that to be our consistent story, but again, I don't know, I have… I have these strong opinions for no particular reason, right? Like, if we find that something else works better for us, then we should use the thing that's gonna work better for us.
**Chris Lightfoot-Wild** 16:26 Well, I mean, I agree with the sentiment, like, we want a good tool, but for the most part, it seems like we've been read in the build pipelines for quite a long time.
**Bob Strecansky** 16:37 For forever.
**Chris Lightfoot-Wild** 16:38 then… with all the, sort of, the way of the land now, with all the, sort of, supply chain attacks, it just makes it way more dangerous to accept anything, not knowing what's, kind of, going wrong. If you… if we're failing at, like, the fan level, and we just accept something, that… it's not even got further down in the dependencies yet, and it…
**Bob Strecansky** 16:57 Right, yes, I agree. I absolutely agree with you, and supply chain attacks are absolutely a real thing. I feel like our industry is going numb to supply chain attacks right now, which is exactly what you don't want to do when you have the gasoline that is AI, but…
**Chris Lightfoot-Wild** 17:14 Absolutely, yeah.
So it was just an… if you're not dead against it, I could potentially look at dropping that… And if not just from everything, you can add it to the build matrix, so we can exclude it on given ones if we wanted to, if you wanted to start out slightly smaller.
**Bob Strecansky** 17:32 Yeah, I think that's… whatever… whatever way you feel like is the easiest to… safely rem… like, safely and slowly remove it, or if it makes more sense to remove it all at once, that's fine too.
**Chris Lightfoot-Wild** 17:44 Because I was just thinking, I'd seen there was someone else, I didn't realize this until… I thought the easiest path was probably going to be reverting what renovated messed up. So, you know, I did that. But then I noticed another contributor, where you'd commented on it, so apologies, I didn't see that. The, fixed depths unblocked composer resolution, that's about 4 from the bottom, if you scroll there, sorry, but… What number?
Have I lost it, sorry, can you scroll… scroll back up?
579, is it?
That's it. That's got a couple of fixes in there that this, Nick had started, and I wanted, obviously, with his findings here, we could… potentially compile a list of the actual instrumentations that are failing, and just, you know, let's just tackle one at once. The AWS one's not green, make that one green, move on to the next one.
And give ourselves, like, a decent chance of actually landing.
one of the fixed PRs, because this has got some fixes in it.
**Bob Strecansky** 18:48 Yeah.
**Chris Lightfoot-Wild** 18:48 It's mangled in, and that other conflicts have come in, and it's just… It's like a burden, then, isn't it, on the person to, like, solve all the merge conflicts, and…
**Bob Strecansky** 18:55 Well, yeah, I think… I also think… And this is even more of a fundamental problem, is like, people will see red CI and they just won't contribute.
**Chris Lightfoot-Wild** 19:04 Yeah, no, no, there's probably some truth to that, isn't there? Because, like…
**Bob Strecansky** 19:08 I know if I was going to contribute to a new open source project and the CI was red, I'd just be like, oh, this is broken.
**Chris Lightfoot-Wild** 19:15 Yeah.
**Bob Strecansky** 19:16 That's it.
So, that's why I've been beating that drum for a little while, but… We probably need to… I don't… yeah, I mean, we need to put more focus in the…
**Chris Lightfoot-Wild** 19:28 Yeah, so are you talking with that? I guess I could potentially, add an issue to say these are the ones that are broken, and then if anyone wants to jump on one, they're happy to, but I can start kind of slowly going through the list as time permits. Yeah, sounds good.
**Bob Strecansky** 19:43 I also…
**Chris Lightfoot-Wild** 19:44 very busy, personally, at the moment, but…
**Bob Strecansky** 19:47 Yeah, I also wonder if, like.
if we can do, like, the quote-unquote hero PR with AI, like, I wonder if that would help.
**Chris Lightfoot-Wild** 19:56 Yeah, I mean, I've seen you've got that additional sort of context, in GitHub that I don't… I don't have, I guess, I don't know if you've paid for that, or it's a work thing, but… Mmm… Yeah, I wonder if even that can be quite, targeted toward which instrumentation it fixes for us, or…
**Bob Strecansky** 20:12 Yeah, probably so.
Let's see… Agent.
I don't know what… looks like you have the ability to create a new agent and do that, but…
**Chris Lightfoot-Wild** 20:26 Is it… this must be because you're, like, the maintainer role, you can see it's done that?
**Bob Strecansky** 20:29 I don't… I don't know.
I don't think I did any… I didn't do anything, like, super special to get… That, but… Let's go back here… it's on your page B… So this is…
**Chris Lightfoot-Wild** 20:45 Although saying that, I thought, I'm a maintainer on that.
**Bob Strecansky** 20:49 Yeah.
**Chris Lightfoot-Wild** 20:49 side, at least now, and I don't have that option, so…
**Bob Strecansky** 20:52 Yeah, I'm doing it.
I'm looking to see if there's, like, a… There doesn't look to be, like, a prompt anywhere, but… Probably need to look into how to… that way, maybe this one.
**Chris Lightfoot-Wild** 21:08 Maybe…
**Bob Strecansky** 21:09 Yeah.
**Chris Lightfoot-Wild** 21:10 Yeah, I guess maybe that could be a future thing for the… for our meetings here, like… assuming we get things into a state of, like, green, you know, the intro to the SIG is like, hey, is everything still green? And if not, there's, like.
Yeah, it's a red flag, isn't it? Well, literally a red flag.
You know, we should sort of try and prioritize keeping it green.
**Bob Strecansky** 21:32 Yep, yeah, I've… I think it's been red for so long that we haven't been able, like, we haven't been able to prioritize that, and we get it green for a second, and then something happens.
**Chris Lightfoot-Wild** 21:41 Yeah.
**Bob Strecansky** 21:42 It's almost like that's a bad pattern for us, right? Like, it's been red for so long, so when it gets green and it goes back to red, you're like, oh, okay, that's expected, but maybe we need to be a little bit more…
**Chris Lightfoot-Wild** 21:53 Yeah.
**Bob Strecansky** 21:53 for lack of a better word, enforcing.
**Chris Lightfoot-Wild** 21:56 Absolutely, yep, yep.
**Bob Strecansky** 21:58 So… And we'll let this rip sip.
**Chris Lightfoot-Wild** 22:00 That was anyway on the fan side. I'll try and see what errors it's sort of picking up, but ideally drop it and hope that PHP stan is going to pick the same ones up, and we don't have to, like, double annotate everything.
**Bob Strecansky** 22:15 Sounds good.
Excuse me.
**Chris Lightfoot-Wild** 22:33 Have we also… the branch is not auto-deleting now, though? Because that one still looks like it's stuck around.
**Bob Strecansky** 22:38 It should… I mean, it does, it just takes a second. I think GitHub's been… Biting.
**Chris Lightfoot-Wild** 22:43 Just, I've had to manually delete a few, recently, but…
**Bob Strecansky** 22:46 Have you?
**Chris Lightfoot-Wild** 22:47 Yeah, maybe it's just GitHub. It's not exactly been the healthiest thing itself, has it, so…
**Bob Strecansky** 22:52 Yeah, I was reading an article about how they said their, like, the commits to GitHub have gone up, like, 800% in the last, like, 3 months or something like that, due to…
**Chris Lightfoot-Wild** 23:03 Yeah.
**Bob Strecansky** 23:04 Absolutely.
**Chris Lightfoot-Wild** 23:04 different buzzword.
**Bob Strecansky** 23:07 Okay, so it looks like… We just start testing PHP 8, too.
Mongoduty update, missing script file… oh.
We don't need that, okay, so… Probably have to go back and fix that. Anyway, open issues… Definitely find out what it is… Complete.
See?
Hang on now. Yeah, the rest of these are under sold.
And then… Let's see, so go to packages, see where we're at… Alright, almost 40 million installs, let's go!
PHP versions.
Looks like…
**Chris Lightfoot-Wild** 24:35 I don't know if you managed to watch any of PHP Verse yesterday, or it would have sucked for your time zone.
**Bob Strecansky** 24:40 No, I didn't even know it was happening.
**Chris Lightfoot-Wild** 24:43 It was a very heavily influenced AI kind of thing.
**Bob Strecansky** 24:46 I feel like that's every conference now.
**Chris Lightfoot-Wild** 24:49 Yeah.
**Bob Strecansky** 24:51 I feel like that's every… everything now.
Good.
Anywho…
**Chris Lightfoot-Wild** 24:57 Well, yeah, just… it would have obviously been nice to talk about any kind of… not me, but I mean, like, if anyone was interested in… OpenTelemetry, getting a mention for all the new stuff they're doing, and I don't know if other SIGs have… Manage to push themselves into their, sort of, ecosystems.
**Bob Strecansky** 25:16 Yeah, I think…
**Chris Lightfoot-Wild** 25:17 We have.
**Bob Strecansky** 25:17 I feel like PHP's ecosystem is just, like, insanely fragmented.
And I don't know if that's intentional, or if that's just how it sort of works, because it's not like… there isn't… there doesn't seem to be a de facto place where people go to talk about PHP stuff, right? Like… go, it's the mailing list Java, they have their own thing. Rust is, like, a couple forums, but there's no, like, oh, this is where… it just seems like people talk about PHP in the PHP.net comments.
But, anyway. Alright, that's all I have on the agenda today. Is there anything else you wanted to walk through?
**Chris Lightfoot-Wild** 25:54 No, I think that was, that was all. Yeah, just, hopefully next week we'll have some more, attendees, and we can divvy up some of the… I was still planning on doing the thing I mentioned in the past, looking at the component owners thing.
So I started looking at how Java's doing that, and how they go, Collector stuff is doing that, because it looks like there's some differences.
**Bob Strecansky** 26:19 Are you talking about co-downers?
**Chris Lightfoot-Wild** 26:22 The component owners that differs from code owners.
**Bob Strecansky** 26:25 Oh, okay.
**Chris Lightfoot-Wild** 26:26 You've got to be, like, a member of the organization, but with this other action that you can include.
there's, like, a separate kind of code owners-esque file, where it then tags that person in the relevant code changes, PR and issues, etc.
**Bob Strecansky** 26:42 Interesting.
**Chris Lightfoot-Wild** 26:43 Yeah, I'll try and… I'll try and look into that a bit more, but that… that was a sort of slow burn, potentially.
**Bob Strecansky** 26:49 I don't look at those.
**Chris Lightfoot-Wild** 26:50 Just a bit of an abit.
**Bob Strecansky** 26:52 Cool. Alright, we'll, we'll see you next week.
**Chris Lightfoot-Wild** 26:55 Cheers, everyone. Bye-bye.
