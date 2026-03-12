SIG: PHP SIG
Date: 2025-11-26
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Sergey** 00:25 Alright, Chris?
**Chris Lightfoot-Wild** 00:30 Hello. Okay.
**Sergey** 00:33 How you doing?
**Chris Lightfoot-Wild** 00:35 Oh, that's…
**Sergey** 00:35 Bro, if, if I… If I connected to the right meeting.
Is Bob already preparing for… For the Thanksgiving?
**Chris Lightfoot-Wild** 00:46 Yeah, I think Bob's off, enjoying some turkey, and yeah, I was…
**Sergey** 00:52 the American thing? You don't have anything, I wonder… If, England, there was something that, gave, kind of, like, Go.
Kind of, like, became eventual Thanksgiving? No? Nothing, like, signal to that?
**Chris Lightfoot-Wild** 01:07 I'm aware of. No, we've got… the next holiday for us is just Christmas break, so…
**Sergey** 01:15 Interesting.
Well, they have mythology behind it, it's… sounds like purely American, right? They have all this, all the Spaca Hontas, or who was the chief there? Native American chief that, kind of like, there was this Mayflower, right? All these, legends that they have.
pilgrims.
that tried to survive. So… So that's, it, all three of us.
**Chris Lightfoot-Wild** 01:46 I guess it'll be a quick one. I didn't know if… Anyone else is gonna rock up on it, but, I suppose Sean, who was here last week, is American as well, isn't he? So he'll be… Arranging some time off?
I don't mind doing a screen share.
**Sergey** 02:03 Yeah, it seems to be the role of the… Responsible adult.
**Chris Lightfoot-Wild** 02:08 That's a good thing.
I don't mind if you want to step in, you can, to the reins on it as well.
**Sergey** 02:16 Yeah, let's try it next time.
**Chris Lightfoot-Wild** 02:17 It's not… Love it.
Oop.
**Sergey** 02:25 Are you communicating with Brett from time to time? Because I see that he's active, just, Was his time being saved on the meetings, or he just on his time zone, like… I think he's just as active as before, you know? I was wondering, like, what was the… the difference in his, like, what was the… shifting down.
**Chris Lightfoot-Wild** 02:45 Yeah, I've not… I've not heard from him, personally, but I guess, yeah, he's just checking in asynchronously when he's got… Somerville.
**Sergey** 02:53 I guess it's, shifting down was based on just a synchrony, that he can, better manage his own time, like, decide when he's gonna work on… I mean, that's…
**Chris Lightfoot-Wild** 03:03 Yeah, I guess, so he's off looking after the baby, isn't he? So I guess whenever the baby's asleep, he perhaps has a few spare moments.
Yeah.
I'm sure he's very busy, and catching up on sleep himself.
It isn't on the agenda this week.
Nothing's browsers?
**Sergey** 03:33 Let me just exc…
**Chris Lightfoot-Wild** 03:35 I don't think this template thing ever works, is it?
**Sergey** 03:39 Oh. Would you like me to cook it? Yeah.
**Chris Lightfoot-Wild** 03:42 I'll try and, nope.
Sorry, Paul, I was trying to spell your name out there, apologies.
Awesome.
Hopefully I got that right. Welcome.
**Sergey** 04:03 Have, bought for that?
We need to find a bot for that as well.
**Chris Lightfoot-Wild** 04:08 Yeah, maybe.
**Sergey** 04:09 I mean, there are definitely bots that summarize the meeting and that, right? Maybe they can generate the agenda.
**Chris Lightfoot-Wild** 04:16 Yeah?
A lot of the AI listening to us?
Firefly or something. Cool, so… Did you have anything you wanted to add to the agenda? I'm not sure there's…
**Sergey** 04:29 The only thing that I wanted to ask, maybe you're familiar with it, I was wondering, small item is… are you familiar with how the split between repos happen? Like, essentially… what I need to achieve is that I want to run the tests, so I was working on this, you remember we discussed this feature of Shade doing the dependencies, so they don't clash if they are loaded into the application context that has similar dependency on the same packages, but with different version?
So… So… in order to have higher confidence that whatever packages we shadowed like that, that they are not broken, we wanted to run the tests that belong to that package, right? So, for example, SDK, to run OpenTelemetry SDK tests on that shaded version of SDK.
But unfortunately, the way we split these repos is that only the production code is being split, there are no tests in that repo.
So, that means that we need to go back to the monorepo and run those tests in monorepo.
**Chris Lightfoot-Wild** 05:29 But it was wild.
**Sergey** 05:30 I'm wondering, like, what is the mapping? How to go back?
How, like, for example, if I have a tag on the… on the repo which was used to release on the packages, let's say it's SDK 1.9.
And this is the one that I want to test.
how do I go back to the monorepo and find the commit that corresponds to the same?
State of the repo.
**Chris Lightfoot-Wild** 05:54 Well, because the commits change, don't they, when you split the repo?
Do you think that…
**Sergey** 06:00 These of the commits are the same, like, hashes are the same?
**Chris Lightfoot-Wild** 06:02 No, because it's a subtree split, so it just generates a new commit ID, isn't it? So is that where you're trying to track the specific one?
**Sergey** 06:09 No, I'm asking, like, how is it possible to track? Like, is it possible to go back and find the commit Based on the… like, is there some kind of mapping somewhere? Like, if I have a tag on the… on the repo with the SDK, on the read-only repo.
Okay, from the tag, I can find the hash commit, commit hash, right?
but still in that read-only repo, how do I go back to the monorepo and find the corresponding hash there.
**Chris Lightfoot-Wild** 06:40 So, when you're looking at, like, a tag like this, you want to see what the actual ID is back in source.
**Sergey** 06:46 Yeah, exactly.
**Chris Lightfoot-Wild** 06:48 That is a great question. I'm not sure how possible or not that is.
**Sergey** 06:53 I searched how… what utility they use, and then I asked Google how to do it, and the recommendation was… to do kind of, like, pattern matching to… so you have a sequence of commits here, and just find… so in this read-only repo, they're obviously the mirror of the commits in the actual repo, right? So just find them, like, take the… I don't know, top 10, and just find them in the… in the log of the commits on that directory, and if you find them, assuming that that, that sequence of commits is unique based on the, I guess, on the comments, or whatever. Like, you just map them… well, if you want to automate it, then you… this is what the… I don't know, I guess that algorithm was proposed to somebody to do it manually, but I guess you can also automate it. But I was wondering if there is a better way to do it, just than, you know, selecting some group of commits and finding the… The origins in the… in the monorepo.
**Chris Lightfoot-Wild** 07:45 I guess it would be… even just looking at this page ahead of us now, it would be useful if… the release notes here said, split from, and then, you know, the tree, and the source, so at least you can jump back into it and see what's what. Otherwise…
**Sergey** 07:59 Do you think this is how it works? Like, this utility… because I was just even wondering, like, how this utility works? Is this done on continuous? Like, is this continuous thing? Like, on each change of the monorepo, it goes and pushes them to the read-only, or is it done on demand when you release, like.
**Chris Lightfoot-Wild** 08:14 I think Brett's been typically running the release script.
**Sergey** 08:22 If it's based on the release, that means that it's on demand, right? So this read-only repo is not constantly kept in sync on each commit to the monorepo.
It's only done on demand when you want to release from the triple, right? So you push… Everything that you want up to this particular commit, and then you say, okay, let's put tag on the commit in that read-only repo.
And then release it from there.
So it sounds like it's done on demand, not constantly. And if it's done on demand, then it's possible to do what you suggested, like, technically, it can track and remember what was the original commit hash that, was kind of, like, used as a, you know.
Essentially, the instruction was push everything up to that commit, right? Then it will mirror all the commits into that read-only thing.
So technically… so maybe I will reach out to Brett and ask him if it's possible, maybe he can… maybe he can…
**Chris Lightfoot-Wild** 09:18 Yeah, I think it… I think it's this package that is used to do this natural split, and…
**Sergey** 09:24 It's called Shell something sh… How is this called? This is for just… no, I think they refer to it, it's kind of like, they refer to it even on the page of this read-on repo.
They say that this is the utility that was used to split it, it's called the… It says that it's a replacement software. So if you go to the… if you go to the root of the read-only repo, like, for example, OpenTelemetry SDK, It will say… Which, which utility was used?
For its generation, or… Or something. But, but you don't have experience with that. I don't want to take your time, I thought, in case you were involved in that.
**Chris Lightfoot-Wild** 10:12 No.
**Sergey** 10:12 If you go.
**Chris Lightfoot-Wild** 10:12 to the road.
**Sergey** 10:13 of this, it will reference to that tool, so if you go look at the comments, it says which tool was used to Does it say here?
Maybe I found it somewhere else.
Maybe I swear somewhere. So there is some kind of tool that's related to Git, Git Split3, or something like that, I don't remember what was the name of the tool.
But, maybe I will start with this DevTools situation.
Yeah.
**Chris Lightfoot-Wild** 10:39 Some of the rounding tooling that makes it a bit easier, but it's probably best question posed for Bob and or Brett.
**Sergey** 10:47 Okay, okay.
**Chris Lightfoot-Wild** 10:48 But my understanding is they just manually kind of kick it off.
So, I don't know if that necessarily helps you, with your current.
**Sergey** 10:56 No, it helps in the sense that maybe they can do what you suggested, like, maybe they can record the original commit somewhere in the release notes, then it will definitely help to, to just go to that commit to the original repo, yeah.
**Chris Lightfoot-Wild** 11:09 So… maybe this won't… Marco Split, Greatest. Some trees… Is that roughly… Buh.
**Sergey** 11:35 Yeah, well, I will follow with maybe Bob and Brett, see if we can make it easier.
**Chris Lightfoot-Wild** 11:46 Nope.
Yeah, I guess that, from my knowledge, that's been around for quite a number of years. I think it was even Nibe or something that had done that bit, so, But I guess they, actively use it, so they should hopefully know the answer to that.
Cool, right, I guess we can just fly through the bottom, more likely.
Nothing, more likely than not, nothing for us to do, but we'll see.
**Sergey** 12:14 So is it growing the amount of requests from the bots?
**Chris Lightfoot-Wild** 12:17 Yes.
**Sergey** 12:18 They're growing?
**Chris Lightfoot-Wild** 12:20 It's a very long list. I've had… I've got to go back to this PR of mine, and you've got some comments from Neva on that.
Brett's got one here.
**Sergey** 12:36 So, what did you decide to do with that PSR log?
**Chris Lightfoot-Wild** 12:39 We decided to…
**Sergey** 12:42 To just pin it to some version, or… pinned into the…
**Chris Lightfoot-Wild** 12:46 I think Nina's preference was to go with, like, the first attempt, which was to just disable the… the SDK.
**Sergey** 12:54 Oh, okay.
**Chris Lightfoot-Wild** 12:56 So, I'll address the comments in that, and probably just close that one down, and then go and… Tweaked the other one.
I mean, it seems risky, doesn't it? Like, even though I've done a couple of tests and it seems to work.
I guess when you push it out to a broad range of users, don't want to be the responsible person for cocking it up.
**Sergey** 13:16 I mean, it sounds like, yeah, it sounds like it's… I mean, is there really a use case that you want to run, OpenTelemetry inside Composer or some short script? It should be short and… So until you have a valid use case, it's probably not worth introducing potential complications just for that.
**Chris Lightfoot-Wild** 13:33 Theater.
**Sergey** 13:33 Yeah, absolutely.
**Chris Lightfoot-Wild** 13:35 So this is waiting on someone from, someone to eyeball, so… Try and get around to that at some point.
**Sergey** 13:45 In the clearance.
**Chris Lightfoot-Wild** 13:48 I think that was it, wasn't it? Sorry, on the relevant PRs that weren't automatically generated?
I did find…
**Sergey** 14:02 Hmm.
**Chris Lightfoot-Wild** 14:04 Bye-bye.
Yeah, so nothing… nothing new in there for a while.
**Sergey** 14:09 I saw that he referenced, in this update, declarative config, he referenced service loader.
Is it used in any way? Like, can you… In this, PR update declarative config from Brent.
**Chris Lightfoot-Wild** 14:24 Is it pointing at B…
**Sergey** 14:25 Anyway, a service detector.
Is that, he means SPI, right?
**Chris Lightfoot-Wild** 14:35 What was it? Is there a comment on that? Sorry, I missed. Add service detector.
**Sergey** 14:39 Hmm. Well, I'll take a look at it.
Are you familiar with this, this change?
**Chris Lightfoot-Wild** 14:45 I've not… I've not really looked at this in depth, because there was, you know, Nive was on it, and but, you know, really looked to a greater mind, so… Yeah, I guess I could take a look separately as well and try and figure out…
**Sergey** 14:56 I was just wondering, because I remember this declarative config was kind of a completely alternative way, and then it was… my assumption it was not even compatible.
with all the SPI, like, you cannot use, like… if you use declarative, then all the configuration sources that you have… you can load via the SPI, they will not work anymore, right? I thought it's completely, like, too, you need to choose first the pass Either you go with declarative, then it will read a particular file.
or you go with the normal configuration, and then all the SPI, you can register, kind of, like.
**Chris Lightfoot-Wild** 15:26 The SDI still allows you to load configuration from declarative.
**Sergey** 15:31 Okay, so there is a combination, you can use the clarity, but in… with this PI.
Yeah, I've got a very, very stale, contribute…
**Chris Lightfoot-Wild** 15:40 thing for Lyra, where I started doing that, but It's, like, more than a year old, I think, now, so I need to kind of update it. But yeah, I was trying to… trying to use the config from declarative, so it looks… looks fairly flexible, but I guess it's still, like, under active development in the spec, so… Yeah, I didn't have much urgency, I guess, to try and fix it.
**Sergey** 16:02 Okay.
**Chris Lightfoot-Wild** 16:06 This, monologue, I think Sean had mentioned this as well last week, the login context, so he's got a PR open for that.
He did ping me about it as well as a sort of heads up, because I said I was interested last week, so I'll try and have a look at that.
Jared, it's so much nice, isn't it?
some of the… Login-related one.
**Sergey** 16:39 Alright, so not from Sean?
Also, in the same area?
**Chris Lightfoot-Wild** 16:45 Yeah, I should open that.
old.
**Sergey** 16:53 15 automated ones, so I'll leave that for Bob.
**Chris Lightfoot-Wild** 16:57 Close off…
**Sergey** 16:59 I wonder, like, is this like a Tetris, when you just do one and then they all collapse into one? Like, are they on the same dependency, just one on top of the other?
**Chris Lightfoot-Wild** 17:11 They're renovating Dependabot Competence.
**Sergey** 17:13 No, he said that, yes, he said that one of them is smart enough to close the previous one.
Random floor.
**Chris Lightfoot-Wild** 17:22 So, there is a new, a new question in here.
Half-spunk has bought a new random flag.
I don't know anything about…
**Sergey** 17:29 Yeah, it has… it has some flag that kind of, like, tells you if the generation of ID was truly random or not truly random. Yeah, I remember, something like that. But I didn't know that it's new, I thought it existed from the very beginning, but… Okay, worth taking a look.
No.
**Chris Lightfoot-Wild** 17:48 I guess, level in that? Is there, like, a feature… is there a feature request label?
**Sergey** 17:53 What… was it just a comment if we supported? Like, what was the… what was the question?
Do we want to support it or not?
**Chris Lightfoot-Wild** 18:04 Well, I guess it's more that we should support it, based on that, but… I think I've seen this person's name pop up before, I guess they're in potentially a different SIG.
**Sergey** 18:14 Hmm.
**Chris Lightfoot-Wild** 18:14 Excuse me.
Well, and it's a member of the technical committee as well, so… Seemingly relevant.
**Sergey** 18:22 I wonder, like, Okay, I mean, how much confidence this requires for you to know, like, if you use this PHP library to generate random Like, how do you know if it's truly random or not? I mean, how… how much randomness do you need to distinguish here, right? Because essentially, using a library.
You don't know what level of randomness it actually provides, but okay.
**Chris Lightfoot-Wild** 18:47 Well, I guess, for now, at least, maybe Brett might weigh in on this, if… this is a fairly recent issue, so we might not have had time to eyeball it yet, but…
**Sergey** 18:57 It's interesting, I think I saw this kind of thing about randomness a long time ago, so I didn't know it was anew, but maybe.
I remember I saw this issue, but I never took it seriously, because I thought, okay, I guess, Like, if you're in an isolated environment, how do you actually know, like, you're just using some library, level of randomness can be really relative, right? So many layers of obstruction between you and any kind of source of real randomness.
It's hard for you to… from… after those yellow layers, to actually make a call and say, okay, this is the level of randomness, and I will record it like that.
But, okay, maybe it's, still doable in PHP as well.
Awesome.
**Chris Lightfoot-Wild** 19:42 Nice.
There was nothing else.
I think you bought that, what's the… Did we look at this one already last week?
**Sergey** 19:53 Which one?
the randomness, I still see the… Screen with the randomness.
**Pawel Filipczak** 19:58 you've.
**Chris Lightfoot-Wild** 19:59 Oh, sorry, it says it's… I still don't want to do that. Apologies, I didn't mean to do that.
Is there a bullet? Is it possible? It looks like it's frozen, mouse doesn't even move.
**Sergey** 20:12 I don't know, maybe if you switch screens, you know?
If it's.
**Chris Lightfoot-Wild** 20:16 It seems to have… I'm just sharing and reshare it.
Apologies.
Can you see that now?
**Sergey** 20:25 Auto Symphony, it's a console default response.
**Chris Lightfoot-Wild** 20:29 Yeah, I don't remember eyeballing this one last week either, but.
**Sergey** 20:33 Is it the same guy that was asking questions on Slack about Symphony? I remember somebody was asking something.
It was not working for them, but maybe it was unrelated.
Hmm.
**Chris Lightfoot-Wild** 20:45 I'm not sure.
**Sergey** 20:46 Are you familiar with this package? I also worked on Symphony, not just another one.
**Chris Lightfoot-Wild** 20:50 I've only looked at it, I've not, I've not actually used it myself, so… but I could try and have a read, and see if there's anything in there.
**Sergey** 21:00 We haven't temptation for doctrine.
Okay, interesting.
Are you familiar with Doctrine?
**Chris Lightfoot-Wild** 21:07 Again, I've not… I've not actively used it, so I can't… can't openly comment on that one, unfortunately.
I wondered if… I've seen her in the… Just in kind of a similar vein to people asking questions around, like, distinct packages that… on the hotel collector, repo, like, some of the components there sort of have… you know, allocated maintainers, and then they can kind of go stale and into an unmaintained state, and eventually they get dropped. I'm not suggesting that that is the case here, but I wonder, you know, it's hard to drum up, I guess it's best efforts on people coming along and contributing, but… when…
**Sergey** 21:52 I mean, in this case, it's pretty popular technologies, right?
understand this approach with dropping it, if it was some proprietary or, you know, like, rarely used thing, yeah, I would agree with you. But doctrine and symphony are pretty popular things, right?
**Chris Lightfoot-Wild** 22:07 Yeah, absolutely, and I don't obviously intend for them to be dropped, I just wondered, like, how do you draw up more interest in people coming along and, you know, actively participating? I mean, it's not…
**Sergey** 22:17 In this sense.
**Chris Lightfoot-Wild** 22:19 For the collector, it seems like, you know, it's quite a popular… Piece of the… the puzzle, but… PHP.
**Sergey** 22:26 for that.
**Chris Lightfoot-Wild** 22:27 Like, there's only a handful of us, isn't there? And a few people, like, passively…
**Sergey** 22:32 Yeah, yeah, I don't… to tell the truth, I don't know, like, I guess it's.
**Chris Lightfoot-Wild** 22:38 I'm not familiar enough with organizing communities and, you know…
**Sergey** 22:42 Motivating people to do something, just, out of the largestness of their heart.
Are you… so if you…
**Chris Lightfoot-Wild** 22:51 10 minutes.
**Sergey** 22:52 suggestions, how to motivate them. Like, technically, open source allows people, like, you know, like… but I remember Bob was kind of, like, saying that it's not nice, just telling people, please go ahead and contribute. Maybe I didn't understand exactly what, when he described, that, okay, let's market as, Help wanted, right? This is the label.
**Chris Lightfoot-Wild** 23:15 Good.
**Sergey** 23:16 I don't know why it's considered to be… sounds to me like a completely… completely valid suggestion. Like, if you come up with a question and… Maybe you didn't even think about it, that you can just go and contribute. Maybe just knowing that and letting somebody know that's an option, maybe motivate them to do that.
I don't think it's impolite, but maybe I'm looking at it from the wrong angle.
**Chris Lightfoot-Wild** 23:39 I just… I wonder if it's worth, adding it for, like, maybe if Bob's around next week, as a discussion point then, because… maybe you could ask the, you know, the technical committee, or some of the other SIG groups, you know, how they drum up more interest.
I mean, maybe this is as good as it gets, and, you know, it's always a bit quiet with et cetera, but if there's some other way of getting more eyes on it, then… But…
**Sergey** 24:08 I think it'll be good, like, if we can, Yeah, I mean, obviously there will be probably some technology languages, like Java, maybe they… they just feel it less, because so many people use them, and they will just, you know, on a relative basis will have much more interest in Absolute, right, because they… the initial set of people are so much larger. So, but if we can have the similar discussions with those that had those challenges, and they somehow improved, and we can use the approaches.
It would be nice to discuss… I don't know who is the closest to PHP in that sense.
I don't know, Python? I guess Python is on the… On the rise now, so maybe.
**Chris Lightfoot-Wild** 24:49 We have Severin, don't we, as our, like, tech committee representative? I don't know if…
**Sergey** 24:55 Yeah, let's bring it up next time with Bob and see how can we… what… maybe we can do some kind of, like, knowledge sharing with others, maybe we can organize meetings with others.
SIG groups and ask them questions like that.
Maybe they will have some interesting advice.
**Chris Lightfoot-Wild** 25:19 I guess, membership.
**Sergey** 25:28 Meaning.
**Chris Lightfoot-Wild** 25:31 Oh, I don't know if it's harsh, but it feels like there's kind of, like, a semi-unment end.
**Sergey** 25:52 Yeah, I guess, It doesn't matter, like, as long as we will remember to describe it the right way, I don't think it needs to be perfectly politically correct.
**Chris Lightfoot-Wild** 26:01 Yeah, I'm not trying to offend anyone, because I'm sure people will jump on it, and… but it's, you know…
**Sergey** 26:06 Yeah, yeah, I think it's fine. Obviously, yeah.
**Chris Lightfoot-Wild** 26:13 Absolutely.
**Sergey** 26:14 Like, like, you know, you're not, you're not, publishing on… On Twitch, something like that.
For our internal consumption, it's good enough.
But yeah, I agree with you, it's an interesting… it's an interesting question. How can we motivate people to… yeah. Let's see what Bob will have to… maybe he will have some ideas.
**Chris Lightfoot-Wild** 26:35 Well, well, we've been through the bolds there, did you guys have anything… That you want to?
Pull me up, maybe.
**Sergey** 26:45 That's when we're starting into the contribution process, so we'll have a… We will update next, and like I said, I was working on this shade doing. I want to see if I can run tests on that.
To have higher confidence, and Like I promised, I will send you the link to see that after it will be stable.
But, yeah, so… We just… our plan, like, near term, is to finish the contribution, and then hopefully we will participate much more to this day-to-day tasks of maintaining the packages and all that stuff.
**Pawel Filipczak** 27:23 I was working on this coordinator process, and so now we have the off-pump configuration distribution to the workers, and we have the Signals sending only from this coordinator, so the workers are passing the data to the coordinator, and then there we have only one connection to the endpoint.
It's been cut, the things, consuming less resources, but we didn't release it yet.
So it's, we… I guess we will release the… the both features, I mean, the shadowing and the coordinator.
In the, in the water release, so… I think soon we'll release the next version, and… now I'm switching to the, to the, contribution, so, yeah.
A lot of fork.
Behind. In front of us, so… Take some time.
**Sergey** 28:23 Yeah, but the big advantage will be that it will be directly available upstream, and It'll be easier for us to just work directly on upstream instead of having something internal, then… thinking how to convert it to be acceptable upstream. So, yeah, hopefully we'll… Shorten the… minimize the overhead. Yeah. Keeping it in our repo, and then… Trying to contribute later, so… Hopefully, it will give us the ability to work directly. So, essentially, the goal is to work as little as possible on something that is… will be kept in our repo, but try to have it upstream directly.
But yes, at the beginning it will be in this distro, but I hope we will be participating much more in… already working directly on SDKs, or whatever doesn't need to be… especially for distro, but can be done exactly… directly in country, or in SDK, or repos, that would be better to do it there.
**Pawel Filipczak** 29:16 No.
**Sergey** 29:17 Yeah.
**Chris Lightfoot-Wild** 29:19 And is it possible, then, to potentially replace the existing instrumentation? I think… is there some back and forth between.
**Sergey** 29:28 Did you approach that.
We'll have to see how we converge between them. That's quite a challenge, how we… Because, yeah, if we can minimize duplication of code.
That would be better, but the question is, is it something that, If the bows will be stable enough and not changing, then maybe minimizing duplication will not be the first, you know, high priority.
Because, this, in distro, we implemented much more than just instrumentation on the native side.
So, we will still need to keep the native part of the code there anyway.
So, if this small part just related to the instrumentation.
just trying to share it and use exactly the same code that's done. The advantage of current instrumentation, obviously, is that it's much simpler, it's smaller, it's only instrumentation that is implemented in that extension.
And, so maybe in some cases it might be proof, be enough, but we'll have to, you know, try to use… yeah, please go ahead.
**Pawel Filipczak** 30:31 I think, I think that the… More… the most important difference between both is the build system. So, we are in the .php elastic, I mean.
We are relying on some packages from the… from the outside of the compiler, and the pure OpenTelemetry extension is relying only on the C feature, so it's not fetching any dependencies. It depends only on the PHP, Pedro, so it's using the PHP-style PHPs to build the extension, so you can build it.
if you can build a PHP on your environment, then it will most probably build also the extension, right, for you.
And if… and we are relying on the pre-built binaries in our distro, right? So we are providing the APK, dev, and TPM packages.
So, in that case, if Sarron is trying to use the open telemetry on some exotic.
system, then it will be difficult For him to build it, right?
**Chris Lightfoot-Wild** 31:46 And.
**Pawel Filipczak** 31:48 With the car…
**Sergey** 31:49 our distro, like, it will be easier for them.
**Pawel Filipczak** 31:51 through your seats.
**Sergey** 31:52 Build the simpler instrumentation, the current one.
**Pawel Filipczak** 31:54 It's much simpler.
**Sergey** 31:55 But we need to better understand all these use cases, like, so, I would not say, to tell the truth, I would not say that it's the most pressuring thing. I think it would be much more important to explain to users when to use what.
The fact that they don't share the code, I don't think users care that much. Like, even if we'll share the code, there still will be the same question, there still will be a simple extension, which can build anywhere, like on IEX, you can probably build it anywhere a PHP Engine builds, right?
And then there is more advanced distro, which we will distribute as a package is preferable. So I think the use cases are different, like, we thought about the distro mostly concentrating on DevOps.
So DevOps, they might even not know much about PHP, especially they don't want to build any kind of, like, Peckle stuff.
They just want to have a package, you install it, and it works. Like I said, the approach is completely different. They install it per site, they don't even know how many applications, so they obviously cannot go and add dependencies to applications.
So approach is a little bit different from who is your, kind of, like, target audience. But if we can converge it, and if we can detect use cases that can be, you know.
bows, and share as much as possible when it's necessary, like, especially in the areas that are hot, right, that change, and we don't want to duplicate them, those. Instrumentation, I think I'm less worried about, because those areas, they almost don't change, so even if we have this code duplicated.
Nobody cares, we don't change, like, it's not that we fix it here now, we need to remember, fix it there as well, right? So…
**Pawel Filipczak** 33:32 And I think, you know, I think that it will self-clarify in the future.
**Sergey** 33:37 Yeah, yeah. So I will probably be less, but I would say, mostly, I think we'll first need to have better messaging, like, what is the use cases we want to start with, who wants… who can use what for what use cases, and yeah. So… From there, I think we will see… what are the, you know, what code needs to be shared. I think we will have maybe even more motivation to share something with maybe even a C++ SDK, or maybe, I don't know, maybe Rust SDK, like any native, other native SDK, maybe there will be motivation to share something with them.
not necessarily… so, this is also something to consider, that maybe the amount of code that will not be PHP-specific, like what Pavel mentioned, like OPAM, all that stuff that can just as easily be applied to other, right, other native, SDKs that can be shared.
That might be also one area that somebody would want to work on, yeah.
But, mostly what we… in our mind, exactly what you just wrote in this agenda for next time meeting, is try to see how we bring in, like, PHP-specific business value as soon as possible. So, I myself less, kind of, like, worried about code duplicated, I want to get to get to kind of, like, have features that are, you know, useful for PHP.
with HP users sooner, like, maintaining better, you know, like, these use cases of Symphony, whatever, Doctrine, all those use cases that provide more value business-wise, less about, you know, like, whether we have duplicated code or not, as long as it's not something that, you know, a huge technical depth for us.
Yeah.
**Chris Lightfoot-Wild** 35:24 Awesome. And it's the coordinator piece, isn't it, that's gonna, if I'm right, eventually allow us to more easily use metrics, and actually.
**Sergey** 35:33 Yeah, we're open, like, if it's something that we can improve the story around metrics. So we want to implement metrics eventually, but system metrics out of the box, to have system metrics, maybe out of the box, but it's still… but you're talking about the metrics API that is used directly by.
**Chris Lightfoot-Wild** 35:53 Yeah, just by the metric signal, because I guess, I feel like more… from a user perspective, it feels like the logs and the traces kind of works.
**Sergey** 36:01 To tell you the truth, I still… I would love to sit down on that and better understand the problem space, because I'm still 100% not sure why it's even a problem, like, considering that there is this temporality thing, the delta, right? It should technically even work even with the PHP application model being this kind of, like, the fact that it's been reset on each, I'm still not 100% sure why it doesn't work even with that, right? Let's say if you want to count requests.
If you're saying that counter will send, like, increments of any frequent count, why doesn't it work at the end? Like, why is it… like, HP doesn't work when, like, Node.js does work, and… What's the difference there, right?
**Chris Lightfoot-Wild** 36:43 You see what I'm saying?
**Sergey** 36:45 Like, what is so special about BHP?
This is…
**Pawel Filipczak** 36:49 Because if you are running the web server, right, and you are, let's say, in each worker, you have some value, and you want to report it. So, in one worker, you have the value 10, in the second worker, you have value 20.
And in the third worker, you have the value 40, and what you want to report. So, if you report it from the each worker, what you will get as a result.
**Sergey** 37:14 Why is it, but why is it a problem only for PHP? How other languages don't have this problem?
**Pawel Filipczak** 37:19 But the other languages, they are running the self-applic… let's say, self… containing applications, so they can share the state, and then can aggregate the values. So if, for example.
**Sergey** 37:31 But it's only per host, so you're saying… you're saying other languages, they have only one process on each host?
**Pawel Filipczak** 37:36 Sergei, let's assume you have Node.js, and you can share the values between the requests. So you have the local storage for the… for those values, and you can aggregate, so you can… you can calculate the metric you want to say… to send per host, let's say that, right?
**Sergey** 37:53 Okay.
**Pawel Filipczak** 37:54 And in the PHP, you override it. You cannot share the state between the requests. You cannot calculate.
**Sergey** 38:01 Yeah, I understand, I understand the limitation with the memory being wiped out between requests. I'm just trying to better understand why it's not an issue, like, because you have the same issue when you have multiple hosts, right? If your service is distributed.
And you want all the… because at the end, like, if you look at all these metrics, you will probably want to see them, not your host…
**Pawel Filipczak** 38:22 You know, I'm not thinking about host, I'm thinking about the application level. It's not about the host. Exactly, but this is because…
**Sergey** 38:30 If we're thinking about application, even in Node.js, it can be distributed over multiple hosts. You can have multiple nodes belonging to the same application, right?
**Pawel Filipczak** 38:38 Yes, yes.
**Sergey** 38:39 but still, somehow it works out, they're not overriding each other, they're somehow being combined. So that's why it brings to me the question, okay, so then in PHP, it's true, in PHP, you have an even finer grain of split. It's not even per host, but even inside the host, you have split per request, right? Each request is kind of like a separate instance of application.
But still, you can handle that, right? Why is it… like, other than the overhead, I can understand the overhead of sending the metrics after each request, but this is the same issue with the trace. So, so Chris, like, just a small question, like, what is the problem? Like, why PHP cannot do what other languages do? Why PHP's specific problem?
**Chris Lightfoot-Wild** 39:20 is a good question. I guess my understanding is perhaps lacking to explain it definitively, so I probably need to go away as well and re-test it, but…
**Sergey** 39:30 Yeah, so I guess we need to… so, from my point of view, if we will better understand the problem domain, and if the solution will be to… to provide some kind of service on top of the coordinator, so it'll be kind of like, let's say, some kind of, like, you know, simple storage per host that will aggregate stuff and then combine them correctly from all the requests? Yeah, we can do it, if that's the best solution.
**Pawel Filipczak** 39:52 Per web server, or per process. Coordinator is not working per host.
**Sergey** 39:59 Yeah, whatever, whatever we… as long as it solves the problem that we want to solve, right? Like, if it will solve it, then, fine, let's, But exactly what you said, with all these limitations. So, if I'm hearing you correctly, let's say if you have a coordinator that was assigned to Apache, but then you're also running command line scripts, right? Then it will not go to the same coordinator if it's command line, right?
**Pawel Filipczak** 40:23 Yes.
**Sergey** 40:24 So then you will still have an issue, so people need to be aware of it.
So they need to be aware that whatever metrics are coming from the… from whatever application is running on top of Apache, it's not the same if they are running now some Laravel artisan scripts, right? Of course. So they need to understand whatever artisan produced, that will be different, unless we want to somehow handle both, so we need to be just aware of that.
So… but, Chris, the best thing, like, if you have some use case in mind that you know that you want to do, and it doesn't work currently, then please let us know, and we'll investigate it in time and see if the best solution will be to use this coordinator, and then, yeah, sounds like additional things that we can do with it, definitely.
**Pawel Filipczak** 41:07 Yes, I think that we should create some, let's say, document with the use cases, and how to solve that, and maybe it's easier to sort that in the collector, and just do some metric processing there.
Or maybe we can do that in our coordinator process.
Because technically.
**Sergey** 41:26 Technically, I understand that this temporality thing.
**Pawel Filipczak** 41:29 Yes.
**Sergey** 41:29 The fact that, are you sending deltas, or are you sending absolute values?
In some way, it should directly handle this issue with the nodes being distributed, like, the sources of this matrix. If they're distributed and they cannot coordinate with each other, then maybe what they need to send are deltas. They should not send absolute values. But maybe it doesn't work in all the cases. Maybe in some cases, there's no, like.
A meaningful delta that you can send, so you have to send absolute, then you need to find a way to deal with it.
So, yeah, it would be best to compile a list of cases and understand what's the problem there.
**Chris Lightfoot-Wild** 42:02 Yeah.
**Pawel Filipczak** 42:03 I have to learn more about the metrics in OpenTelematic, how they are being processed by the backends, so that's… I don't have much experience with the metrics in the OpenTelematic, frankly speaking, so…
**Sergey** 42:17 Yeah, we can only, like, we can look at our backend, like, in case of Elastic, we have Elasticsearch and Kibana.
And we can see how they handle. But obviously, it will be kind of, like, proprietary a little bit in the sense that, okay, maybe that's not even the right way. Obviously, there are a lot of languages already do it this way.
But if we need to do it differently for PHP, we can adapt.
But, yeah, so it's best to understand the use cases, understand the current issues. And if you can guys bring a different perspective, you guys use a different backend. Like, Chris, for example, what do you use for the backend? Are you using kind of, like, Zipkin, or… how is that?
**Chris Lightfoot-Wild** 42:54 I'm ruled.
At the moment, we've only got, local, open telemetry, and in production, we're just AWS CloudWatch, but the metrics for that are coming from… we're pushing into Redis, as I like, data store, and then periodically a script aggregates them and pushes it into CloudWatch, so it's kind of a bit…
**Sergey** 43:15 CloudWatch, you can also push it in OpenTelemetry format, or is it proprietary, CloudWatch?
**Chris Lightfoot-Wild** 43:19 It's just, like, our own… it's just a JSON file that we, you know, space…
**Sergey** 43:24 So it's not… so, when you translate from Radius, you already translate to specific format for CloudWatch, it's not OpenTelemetry anymore, it's just…
**Chris Lightfoot-Wild** 43:30 At the moment, there's no open telemetry, so… but then I'm obviously trying to push… I'm kind of, like, advocating at work, I guess, for Rotel, and obviously.
**Sergey** 43:41 But what I'm trying to advocate? You can use CloudWatch to push… you can push OpenTelemetry into it, or you will need to use a different backend, too, if you want to push OpenTelemetry into it?
**Chris Lightfoot-Wild** 43:52 We could… we'd be pushing… if we were to use CloudWatch, we'd be using the hotel collector to… export it that way, but… Currently, obviously, we're not… we're not doing any of that. We've just got our own, like, in-house thing, but it's…
**Sergey** 44:06 Okay. But it's possible you can… you can push OpenTelemetry into the CloudWatch as well?
**Chris Lightfoot-Wild** 44:11 Yeah, you can export metrics into that, I believe.
Okay, I see. That's not the plan, like, you know, down the…
**Sergey** 44:19 So you say, you say you can use, maybe, collector instead of ready, so there will be collector. Each local collector will be kind of, like, aggregating per host, and then collectors, each collector will push to CloudWatch? Is that what you want to do?
**Chris Lightfoot-Wild** 44:32 Yeah, so I guess all our sidecar collectors will just, like, you know, retrieve all the signals out of the… Each worker process, and then they aggregate them into, like, a gateway that exports Or does whatever other processing we want.
But yeah, just in my head, the metrics thing never seemed to work, so maybe I need to revisit it and see… if it's tweaking this temporality thing, or… my understanding was just off, But, like, currently we do even just, like, a simple count, you know, we've got a request come in, and we'll increment that count by one.
**Sergey** 45:09 I mean, just on top of my hands, it sounds like delta is perfect for that, right? So temporality delta should work So then, you need to switch to temporality delta, but again, I'm not… I'm not 100% sure, I don't exactly have a good knowledge about how MeteX… like, obviously, it will then… how do you aggregate them? Like, does Metax have attributes like host or public service? Can you aggregate them based on those attributes? I assume so? Should be like that, right?
**Chris Lightfoot-Wild** 45:33 Yeah, I guess we should at least host, but I don't know if… I don't know if there's enough information there, but I guess I can try it, and then… report back. Maybe it's just me being an idiot, but I don't know.
**Sergey** 45:46 How do you aggregate your traces? Do you have a concept of, kind of like, service or something? Like, that, kind of, like, application thing, and then you can look at the traces all belong in a particular application?
**Chris Lightfoot-Wild** 45:57 Yeah, the, sort of service name.
**Sergey** 45:59 Service name, okay. So, the question is, so would you prefer to also those business metrics also to be per service? Like, to try to attach the same service name attributes to the metrics as well?
And then aggregate them also in the context of service?
**Chris Lightfoot-Wild** 46:13 We probably would, I guess, because currently it's like, and our public APIs, you know, we just count requests on that, etc, and that is just using the non-will-tell kind of way. It'd be nice to say, oh, we just… we do this, and then we can do away with all that complexity.
But… .
Yeah, I guess I need to retest that and see.
just hoping that, you know, somehow magically, I can configure the SDK to export to the collector, and then the metrics just line up for us magically without us having to do any… Yeah, for those.
**Sergey** 46:47 Well, I mean, it sounds like metrics you will have to do manually. Like, you will need to implement a code in your application that creates those metrics, right? The metrics themselves will not appear magically.
**Chris Lightfoot-Wild** 46:57 I mean, yeah, we… okay, we increment an account, but then we don't have to… do any aggregation ourselves and, you know, write custom scripts that passes JSON objects, etc.
**Sergey** 47:10 I mean, I'm not familiar with the backend like this CloudWatch. If eventually you want to piece… to push all your pieces into that, it obviously depends if CloudWatch is capable of aggregating, like that, right?
So, I don't know that in Elastic, they can, like, you can limit it on different dimensions, like, you can limit it by time, by service, by this, by that. So, and then it will aggregate based on the, you know, on your limits that you put on all these dimensions.
And then there are more advanced things that you can do, like you can do histograms and stuff like that.
So, that obviously depends on the backend, if it's, if it's, advanced enough that it can run… like, it gets raw data, right? And now… how it can aggregate them, or do whatever, processing after that.
If it does it on the ingest time, or on, you know, on query time, it's all optimizations that all depend on this backend.
**Chris Lightfoot-Wild** 48:06 Yeah, I'll… I guess I'll give it a go, and then I'll see.
Yeah, please let us know, that definitely will be very valuable.
**Sergey** 48:14 To get. So you're essentially the… kind of like, trying to… you… you, in the sense, the end customer that we… needs to get feedback from, right? You are the application developer that want to get value out of the OpenTelemetry, so your feedback… please stay on the line, your feedback is very valuable to us, yeah.
**Chris Lightfoot-Wild** 48:31 Yeah, and it's been very easy to, like, just instrument and get traces and logs out, because you've got to do very little.
Or it feels like you've got to do very little, but then with the metric side, it just… seem…
**Sergey** 48:44 Well, obviously, like, you cannot do much about the business, right? If you have proprietary business metrics that you need to want to collect, obviously you will need to do it. But if we can… I don't know if the… if we can do metrics for already… so we're mostly concentrating on traces when we haven't contributed all the… all the kind of, like, support for technologies.
But I think we can do metics as well, right, out of the box for those technologies, like, Because we don't… it doesn't need to be limited to traces, like, for example, we can count in doctrine or whatever, we can count queries, we can count, like… I think that might be the next step, right? Get metrics out of the already… out of instrumentations that we have there.
Not just traces.
For example. But, we need to think, sometimes metrics made more, you know, sometimes it might be more effective, even, like, overhead-wise, right? We might, Collect metrics even if we don't collect traces, so… maybe there are even some place for optimizations there.
**Chris Lightfoot-Wild** 49:41 Yeah, I'll have a play around with the API and then see, you know, what comes out of it, if it's easy enough that I've just overlooked something, or… I'll set up the collector quite right, or something like that, but… Yeah.
I'll report at some point in the future. Sorry for just, touching on the subject again. It's, yeah.
**Sergey** 50:02 Okay.
**Chris Lightfoot-Wild** 50:03 Okay, thank you guys. Yeah, have a good week. I'll see you later.
**Sergey** 50:07 Bye.
