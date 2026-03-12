SIG: PHP SIG
Date: 2025-08-20
Duration: 21 minutes
Zoom Recording URL: https://zoom.us/rec/share/-Q4LnOR1bIfa-KV0gdr2L0P5xv-rDPk3EguYTkU-HcERqF5W1PM3RN1TzKMlIum1.FVenlBk78CuLkawj
============================================================

## Zoom Recording Transcript

**Brett McBride** 01:44 Hello, Bob.
**Bob Strecansky** 01:46 Fantastic.
Happy Wednesday… well, almost Thursday for you, huh?
**Brett McBride** 01:58 Yeah, yeah, it's getting there, yes. Great to be here, how are you?
**Bob Strecansky** 02:04 You know, another day, another dollar.
**Brett McBride** 02:06 Are you really sitting outside on the porch?
**Bob Strecansky** 02:12 … I'm trying to think of what I could touch to show you that it's for real.
Yeah, it's actually 20 degrees C outside right now, which is really nice.
**Brett McBride** 02:25 Fantastic.
**Bob Strecansky** 02:26 And my cleaning people are in the house, so when that happens, I just like to make sure that I'm out of their way.
**Brett McBride** 02:34 I want interesting-looking Zoom backgrounds, I always need to check whether it's… It's real or not.
**Bob Strecansky** 02:42 Is that just gonna be part of our new normal, is checking if things are AI or not?
**Brett McBride** 02:48 Right, sorry.
**Bob Strecansky** 02:50 the AI janitors.
**Brett McBride** 02:53 Yep.
Hello, Chris.
**Chris Lightfoot-Wild** 02:56 Hey, 14 here now, if you're comparing temps.
**Bob Strecansky** 03:03 That's pretty cool.
**Chris Lightfoot-Wild** 03:06 Yeah, it's really dropped off.
**Brett McBride** 03:08 Yeah, for your summer, yeah.
**Chris Lightfoot-Wild** 03:13 Oh, it's not at the back end of somewhere now for a UK.
Gets… gets wet and cold very shortly.
**Bob Strecansky** 03:21 We had about 5 centimeters of rain last night, so… It cools off.
**Brett McBride** 03:27 Holy man.
**Bob Strecansky** 03:28 Yeah, there's a lot of rain.
**Brett McBride** 03:31 Hello, so again.
**Sergey** 03:32 Hi, guys.
**Chris Lightfoot-Wild** 03:34 Boom.
**Brett McBride** 03:49 And 5cm of rain here would cause flooding.
Do you live in a.
**Bob Strecansky** 03:54 Yeah, it's… It definitely flooded a little bit here yesterday, and I was driving home, and it was, like, one of the worst rainstorms I've ever driven through.
Not fun.
Just to be in the office, to be on Zoom with people.
**Sergey** 04:12 In Australia, do you have, like, clear delineation between seasons? Like, here in Israel, we, like, for almost 9 months, we don't have any rain. Like, there is a clear season when we will have any rain.
**Brett McBride** 04:23 Okay, don't worry. Don't worry.
**Sergey** 04:26 In Australia, it's just spread around, you can have rain any time of year.
**Brett McBride** 04:31 Oh, look, in the north, it's very tropical, and they have wet season and dry season, but down here, I think we have… More like 6.
6 seasons.
Yeah, but even then, yeah, apparently we're… we're in a… we're in a part of the country where it can actually change.
… yeah, I don't know, the saying is we get all of the seasons in a day, and that's… it's almost true on some days.
**Bob Strecansky** 05:07 Do we expect anybody else, or is this our core crew today?
**Brett McBride** 05:12 Expecting, no.
**Sergey** 05:15 Pavila's on vacation, so not, from our team.
**Bob Strecansky** 05:19 Nice.
**Sergey** 05:20 Usually, 3 minutes, people already join, right?
**Bob Strecansky** 05:24 Yep, I think we'll… we'll let it rip.
Alright.
Road to SDK V1… Road to SDK V2 has… one….
**Brett McBride** 05:35 One thing in the queue, but nothing crazy.
**Bob Strecansky** 05:39 The prioritized backlog has a couple things in. Anybody, anything anybody want to talk to you about on this board?
**Sergey** 05:49 So, just last, maybe we already discussed it, what is the main reason for incrementing major version? Is there expected some incompatibilities, so it's just, kind of like signaling?
**Brett McBride** 06:02 The main reason, yeah, because… because we had a bunch of changes to make, which were breaking.
In small ways, but… but… Nevertheless, breaking changes.
… Got it.
Yep, so that's why the SDK, and… And the other part to that is it says in the spec somewhere.
to try to avoid changing major versions on the API.
**Bob Strecansky** 06:32 Or….
**Sergey** 06:32 The guy is gonna try.
So, please go ahead.
**Bob Strecansky** 06:37 Yeah, so we're lumping a bunch of stuff together, and we can make one big change when we deem the time is right, and when people need it.
**Brett McBride** 06:45 Yeah, yeah. Which, I mean, we're probably getting close. I've run out of things to do for… or breaking changes to make, and… There don't seem to be any others in the pipelines. But Sergey, you were just asking me about the API. I'm not sure why… Why it says that in the spec, but it does, and we… we try to find.
**Sergey** 07:05 Is the API changed for version 2 of the PHP SDK?
No, no, just this thing.
So the changes, then, that you say are not backward compatible, they're not in API, some other areas?
**Brett McBride** 07:19 Yeah, just the S, literally just the S.
I think.
**Sergey** 07:22 Hmm.
Okay.
It's interesting, but if those are not exposed by API, do we consider them kind of, like, not backward compatible? Were they committed to be kind of, like, a part of public interface that should stay compatible, if they're not part of API?
**Brett McBride** 07:37 That's a good question. I don't know….
**Sergey** 07:41 I think we've just said….
**Brett McBride** 07:42 Yeah, no, I don'.
**Sergey** 07:43 You know, if other teams already have version 2 of SDK, like, how fast do they… I'm just trying to Trying to understand, like, what is our… you know, like, there are browsers, like, that increment any change, like Chrome, and they just go with just increment major version, don't care.
And then there are approaches that try to stay with the major, kind of, like, keep it, so people can kind of, like, … I guess, it's kind of like, I guess, … It's, … the trade-offs, right? Incoming major, you're kind of, like, signaling that people should be careful upgrading.
But on the other hand, if, like, 99% chances that it will be okay, people don't use those, SDK function.
**Bob Strecansky** 08:24 I know.
**Sergey** 08:25 then.
**Bob Strecansky** 08:27 I know that… I believe it was the Java and the GoSigs both talked about, like, updating to their major version, but I don't know that they've made any progress on that. I think they are sort of in the same boat. They have a couple, like.
theoretical braking changes that I could or could not apply, and they were… I remember that in one of the maintainers' meetings, they were talking about whether or not it was worth it to… I'm not sure of the status. I just know that we are not the only SIG that has considered this.
**Sergey** 08:55 I guess maybe the other way to maybe approach it from a different direction, what are we going to do with the 1X branch? Are we going to continue export into it, or are we gonna completely freeze it and only work on 2X?
**Bob Strecansky** 09:12 That's a good question.
**Sergey** 09:13 The reason I'm asking is I'm trying to see, can we bring in some selfish angle and consider, do we want additional work if we want to continue also maintaining? Maybe that will be motivation not to increment major, right? Then we don't need to.
**Brett McBride** 09:26 It's very good motivation.
yes, we don't… I don't want more work. … No. I mean, look, I would… I would consider… You know, back patching.
bug fixes to it for a while, I suppose, but … I think my preference would be that If you're honest.
**Sergey** 09:47 I understand, but the question is, maybe we can stay with 1X. Do we need to go to version 2? Like, … like you said, if API didn't change… Then maybe the things that change, they're not considered to be breaking anything, like, they have internal details.
**Bob Strecansky** 10:02 Might be a good discussion to bring up in the maintainer's meeting, or in one of, like, or ask the technical committee about it.
**Chris Lightfoot-Wild** 10:10 There are quite a lot of breaking changes, though, aren't there, in terms of, like.
**Brett McBride** 10:13 Yeah, like, people would notice, I think.
**Bob Strecansky** 10:17 Yeah.
**Sergey** 10:17 In terms of what? Sorry, Chris, can you… which one, for example?
**Chris Lightfoot-Wild** 10:21 Well, like, registering… the registry has changed quite a lot towards SPI, I think, from my understanding. So certain things have dropped out that if you've depended on that in an instrumentation package, you'd have to, like, explicitly Handle that, so you can't just… you know, it would break if someone just updated the SDK independently.
**Sergey** 10:43 So the way we will bring up the auto instrumentations, it's not we are composer, it's different, different way, we are composer, but we are SBI.
**Chris Lightfoot-Wild** 10:51 Still, still via Composer, but in the register, like, certain interfaces have just disappeared.
From memory.
**Sergey** 10:59 I see. So in the sense, like, it's not breaking API, like, in the sense, like, API, programmatic API, but it breaks one of the things that users directly have exposed to, and that's the reason, probably.
We want to increment, right?
Okay, I see that.
**Chris Lightfoot-Wild** 11:16 But I imagine, like Brett said, you could probably… Add, like, a glue layer, if we really wanted to stick away from version 2.
But it's probably more work at this point.
**Sergey** 11:30 Yeah, I guess, like, main consideration would be, do we want to continue maintaining two branches, right? Like, is it worth it?
This guy has the trade-off, right?
Especially, like, if you say that if we can introduce this layer, that will… well, I guess it will be additional, kind of, like, thing that will be hanging around.
That will also be, do we want it, right?
**Chris Lightfoot-Wild** 11:49 It does complicate things for your distro a bit, though, doesn't it?
**Sergey** 11:53 No, no, I don't mind, like, for distro, we will just switch and that's it, right? It will not… I guess… We need to consider… No, but we want to shadow the SDK anyway, so we will not even depend on what application is doing. Even if application depends on different major version of SDK.
We didn't do it yet, but we need to do it, like, we need to shade the SDK that we bring with the distro.
So I guess it will be a motivation for us to do it when we switch to 2X.
SDK. But, I don't know, I'm just asking in general. I don't foresee, because the main use case for Distro is, kind of, like, completely hide it from, … From the end users, it's more for DevOps.
then… they probably would not care, like, if it's 2X or whatever, they just want to get latest features.
Yeah, so I guess it's more important for people that are exposed to those changes, right? Like you said, those that directly write those dependencies in Composer and stuff like that.
No, I'm just trying to bring, possible, kind of, like, consequences to this, right? So there are… there will be trade-off, like, to doing this, right? So just trying to understand, … If, … If we 100% kind of, like, … waded in.
All the trade-offs.
Listen for me.
**Bob Strecansky** 13:19 Hmm. Move on… No new stack overflow questions… Okay.
requests… a couple Dependabot.
This… I've noticed this Dependabot, the checkout actions. One breaks a bunch of stuff, so I'm wondering what we should do with these if they break. Like, this could kill actual one is fine, but… I haven't really thought a lot about this yet, I just wanted to say it out loud in case anybody hadn't seen that before.
**Brett McBride** 13:47 Sorry, it has broken other… repositories.
**Bob Strecansky** 13:53 No, not broken repositories, I think, like, the… I've seen this one fail every test a couple times, or fail a good portion of tests a couple times, but I probably need to investigate a little bit more.
**Sergey** 14:05 So this thing is not smart enough, like, if you search, like, for example, this kind of problem, and you will see that people's suggestion walkaround, I guess this depends on… it's not, like, AI-based, that it can apply this walkaround by itself, right? It just… it just does the… the bare minimum, it just upgrades the… the whatever, … Dependencies used, but it's not trying to apply, you know, changes that are necessary to make it compatible.
**Bob Strecansky** 14:29 Right, exactly. So, again, probably more investigation warrant.
**Sergey** 14:33 I guess it's by searching, yeah, I guess it's… if it's something that happens a lot, maybe simple search will show how people work around this.
**Brett McBride** 14:41 Yeah, if that… if that pull request or the associated GitHub action ran to completion, then it's probably okay, because it would have… would have run it with that new version of Checkout Action.
So it's those failures….
**Bob Strecansky** 15:00 I didn't look… I didn't look too….
**Brett McBride** 15:02 Hmm.
Yeah, let's see.
Yeah. Yeah, no, I don't.
**Bob Strecansky** 15:06 are related.
**Brett McBride** 15:07 So I thought this was in, ….
**Bob Strecansky** 15:09 Yeah, this is… oh, yeah, this is what it was. I looked at this earlier. I think one of the… I think the setup PHP, GitHub action may not work effectively with the, new actions yet.
**Brett McBride** 15:22 Right.
Sorry, you're absolutely right, then. ….
**Sergey** 15:27 PHP depends on checkout action.
**Chris Lightfoot-Wild** 15:29 extensions in there as well, can we… can we purge that?
**Bob Strecansky** 15:35 It also looks… yeah, it also looks like it's not consistent, right? Like, PHP 8.3 was fine.
So….
**Brett McBride** 15:42 Was it also just a glitch in… installing.
**Bob Strecansky** 15:46 Never… You never trust GitHub Actions. I'll run this again, just to make sure.
**Chris Lightfoot-Wild** 15:51 Can you… can you clear the cache, though, first? Do you have the permissions to do that?
**Brett McBride** 15:56 I don't think so. It's really hard. I've had to do that once, and it's not… It's not straightforward at all.
**Chris Lightfoot-Wild** 16:03 I'm sure I've seen it in a UI somewhere once, where you can just delete the….
**Brett McBride** 16:07 Really? No.
might depend on the cache, but I, I had to, like, get a token and run API commands to do it, I'll start to write.
**Bob Strecansky** 16:17 Oof.
**Sergey** 16:18 There is some catch that persists between the executions of PR, between the jobs or workflows?
**Brett McBride** 16:25 Yes, we do, we do have cashing.
**Bob Strecansky** 16:29 Yep.
Okay, well… It's like that.
**Brett McBride** 16:32 Composer dependencies, and… ….
I'm not sure what else. Possibly extensions for… installed.
**Sergey** 16:40 worth it, doing it? Maybe it doesn't speed that much, if it can… but I guess it depends how frequently you need to clear it manually.
Versus how much it speeds up, but….
**Bob Strecansky** 16:53 It's also nice to have a faster CRM, but I digress.
Anyway, … Let's see, is there anything else? It doesn't look like we have anything else really pressing in the base repository.
Contrib… Couple more of these bad boys.
I'll see what happens with the main repository one before we deal with the contributor ones.
Instrumentation… same thing. These ones cleared, fine, so I guess I could just approve those and merge them at some point soon.
Oh.
Packages, let's see if anything crazy's going on here… So close to 20 million, we're getting there.
I think that's all of our standing agenda items. Oh, we gotta check the issues, if there's any new fun issues that came up.
Nothing in the last 3 weeks.
Labeled plug. I guess I should also look not labeled bug.
But I had the last one 2 weeks ago, that's good.
That's all… that's it. Does anybody else have agenda topics that they'd like to talk about today?
**Brett McBride** 18:21 No, I don't. Just looking at those issues, or lack of Whoop.
It's gone very quiet the last few weeks, I've noticed.
**Bob Strecansky** 18:30 It has.
**Brett McBride** 18:31 I mean, we're still getting lots of downloads, but, ….
**Sergey** 18:35 Is Australia the time for the… is it also, you have a school vacation for kids?
Or is it the other way around? It's, like, in January, or…?
**Brett McBride** 18:45 our big one is in December and January, but ….
**Sergey** 18:49 Okay. Yeah, so for us, this is kind of like the apex of kids' vacation, right? So, a lot of parents have to take vacation as well.
**Bob Strecansky** 18:59 Same, yeah, we… kids just went back to school for us, which is also, like, that's also, as you know, Brett, as a parent, that is a huge boot, like, a huge crush in productivity when… the kids go back to school. New things, so… But yeah, I wouldn't ex… I don't think that there's anything fishy going on, I think it's just….
**Brett McBride** 19:19 Maybe time of year with vacations and….
**Bob Strecansky** 19:22 Europe is very famous for taking most of August off.
**Brett McBride** 19:26 Yeah, yeah. No, I didn't think it was fishy, I just thought maybe we've solved all of the problems now, and it's… it's all….
**Bob Strecansky** 19:33 What?
**Brett McBride** 19:33 sailing from now.
**Sergey** 19:36 Wow.
**Bob Strecansky** 19:36 Yeah, we've….
**Sergey** 19:37 You're in a good mood today.
**Bob Strecansky** 19:39 You're in, like, a….
**Brett McBride** 19:43 I agree.
**Bob Strecansky** 19:44 cautiously optimistic moves today, Brett.
And you're just like, oh, we're done here, and just, like, sail off into the sunset.
**Brett McBride** 19:52 Yeah, it sounds like the saying, you know, like, when you wake up and nothing hurts, so….
**Sergey** 19:56 You're probably dead.
**Brett McBride** 19:57 Ouch.
**Sergey** 19:59 What?
**Bob Strecansky** 20:00 I haven't heard that before, but that's really funny.
**Brett McBride** 20:03 I like that.
**Sergey** 20:04 Yeah.
**Bob Strecansky** 20:06 Good.
**Chris Lightfoot-Wild** 20:07 Cool, well, no news. Sorry, I did have one question then, sorry. The scale bot stuff… Obviously we've noticed in the past it seems to come to life and then disappears.
**Bob Strecansky** 20:19 You know, I asked….
**Chris Lightfoot-Wild** 20:20 The mechanics thing.
**Bob Strecansky** 20:22 I asked that question in the maintainer's room, but I don't think I ever got a response. Let me check.
**Sergey** 20:27 What does it do stale about? Does it find stale stuff?
**Chris Lightfoot-Wild** 20:30 Yeah, Max issues the sale, and then eventually it should clear rhythm off the list, but it doesn't seem to really be doing that.
**Bob Strecansky** 20:38 I did. Hold on, let me share this, … Alright.
**Chris Lightfoot-Wild** 20:43 Pretty amazing as well. No issues, and then Starbuck takes… the cruft away, then….
**Bob Strecansky** 20:51 Yeah, I did start talking with Trask about it, and then he… Kinda stopped responding.
But… Maybe I can… that's a good question. I will bump that.
**Chris Lightfoot-Wild** 21:11 Sorry, Craig, last minute.
**Bob Strecansky** 21:13 No, nothing visible.
Nothing to be sorry about.
It's a great question, because that is very, very annoying when things are stale and not disappearing from our board.
Alright, Mo?
See y'all on the internet.
**Brett McBride** 21:41 Cool. Thanks a lot, bye-bye.
**Chris Lightfoot-Wild** 21:43 Hello?
