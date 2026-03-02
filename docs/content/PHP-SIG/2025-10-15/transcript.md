SIG: PHP SIG
Date: 2025-10-15
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 02:59 Interesting.
**Nick Schuch** 03:00 Hey, how you going?
**Chris Lightfoot-Wild** 03:02 Yeah, Martha, how are you?
**Nick Schuch** 03:04 Not too bad. I… just created a pull request for something internal, but the pull request ID is 666.
**Chris Lightfoot-Wild** 03:16 Fingers crossed a bit.
**Nick Schuch** 03:18 Yeah… It's a big pull request, though, so…
**Chris Lightfoot-Wild** 03:24 I've just seen as well, Bob might not make it today, so…
**Nick Schuch** 03:28 Okay.
**Chris Lightfoot-Wild** 03:29 I was curious who was gonna rock up.
I might have been on my own for a bit, but hopefully you joined.
**Nick Schuch** 03:37 And I thought, I'm try… I'm trying to make it… I'm trying to be consi… a little bit consistent.
Ugh, it's, yeah, usually… 10 o'clock my time at night, so it's… yeah, so…
**Chris Lightfoot-Wild** 03:53 Yeah, I think you have roughly the similar position in the world to, Brett, aren't you? I think he's…
**Nick Schuch** 03:59 Yeah.
**Chris Lightfoot-Wild** 03:59 Near Perth, was it?
**Nick Schuch** 04:01 Yep, and they all just clicked over to Daylight Savings, so… yeah, it's even later for him now, so…
**Sergey** 04:12 Alright, guys.
**Chris Lightfoot-Wild** 04:13 Hey, it's okay.
Okay.
I did wonder that as well, because actually, our clocks go forward in the UK in a couple of weeks as well, so…
I've missed one in the past where I'd forgotten the…
The US time this is based on hasn't changed, so… I guess so.
Dual-check the card and make sure I don't miss it.
**Pawel Filipczak** 04:37 Yeah, that's central.
**Chris Lightfoot-Wild** 04:41 Do you think we expected anyone else?
I could, I could do the screen share if we've… if we're happy to.
Go as the four of us.
fuel.
**Nick Schuch** 04:58 Nope.
Yeah, sounds good.
**Chris Lightfoot-Wild** 05:04 Bear with the story.
**Nick Schuch** 05:05 It's, brett not making it.
**Chris Lightfoot-Wild** 05:10 Not sure, he's on, he's on, sort of, leave at the moment. Oh, okay. Yeah, yeah. So, I mentioned he may or may not be able to pop up.
Okay, yep.
**Nick Schuch** 05:23 Oh, nice.
**Chris Lightfoot-Wild** 05:28 I think he had something like 10… 10 months of…
Paternity leave or something like that, so…
**Nick Schuch** 05:34 Oh, great.
**Chris Lightfoot-Wild** 05:35 For a little while.
**Nick Schuch** 05:38 Oh, that's…
**Chris Lightfoot-Wild** 05:38 Right, I've just found the document, I'll share the screen.
I always, have to look for the button, just because we use, like, Slack for huddles at work, and then Google Meet sometimes as well, and it's just… they're all in slightly different positions.
I'm gonna shut the window.
Show the full thing in.
**Nick Schuch** 06:11 Oh, goodness.
**Chris Lightfoot-Wild** 06:13 Can everyone see that okay?
Nice.
Something…
Let's get the template to actually work.
Sorry about that, wait a second, I'm sorry. I lost it.
Who have typed it by this time, but…
There we go. Cool. Did anyone have anything they wanted to add to the agenda while it's,
Before we get going on?
**Nick Schuch** 07:51 Probably be a quick one.
**Chris Lightfoot-Wild** 07:55 Yeah.
I was gonna ask about early PR as well, but I'm trying to catch… Bro.
I'll be into it.
Oh, I've clicked on the wrong thing, there we go.
I don't know, that's just because I've… sorry, apologies, I've copied the template, which I…
The wrong link on it.
**Nick Schuch** 08:35 We have got our own project Baltimore, haven't we?
**Chris Lightfoot-Wild** 08:38 Pub likes to open, so…
**Nick Schuch** 08:42 Start with that as well.
**Chris Lightfoot-Wild** 08:45 SDKv2, still nothing on that, is there? So I think that was,
Just waiting for Brett to sink in with us at some point and see what his plans were.
**Sergey** 08:56 Are you sharing, are you sharing the same screen that you…
**Chris Lightfoot-Wild** 09:01 Possibly not, have I… why not?
**Nick Schuch** 09:03 Oh.
**Sergey** 09:05 Have I sharing anything, or is it just one window? You're sharing one screen, but it seems that you're doing something on another screen.
What's the one you were referring to?
**Chris Lightfoot-Wild** 09:15 Can you, can you see…
**Sergey** 09:17 We still see the document, at least what I… this is what I see. I see the… the agenda document.
**Chris Lightfoot-Wild** 09:22 Oh, sorry. I obviously clicked the wrong thing to stop, and only shared one window.
Yeah.
**Sergey** 09:29 You opened other tabs, but it seems that maybe you… maybe it's just frozen, but… No, no, the cursor was blinking.
It's hard to say.
**Chris Lightfoot-Wild** 09:39 What about that, can you say fast?
**Sergey** 09:40 Now we see the… the backlog, yeah.
**Chris Lightfoot-Wild** 09:44 Right, sorry, so you can imagine I was on the V2 board, and it looks the same as last week. I won't go back to it. And then on this one, I don't think there's anything necessarily to discuss here, nothing seems to be, like, actively in progress.
This is in the same state, I've not gone back to it yet.
Nothing on… Here that anyone's aware of, that… People were looking at… discussion.
Maybe as well move this. Can you still see? It's okay, if I'm switching… switching…
**Sergey** 10:22 Yeah, now we see the…
**Chris Lightfoot-Wild** 10:23 Each… the main repo.
Cool, let's see if there's any new issues, which, there's none there, which is great.
Pull requests.
Nevada opened one.
Which… I guess it's waiting for some reviews.
If anyone's interested in having a look at that, I'll try to have a look at it myself as well.
It needs Bob or Brett to ultimately review stuff, but I guess we can give it, like, a first pass and see, so they can merge it.
And then just all the usual clutter with the, Dependabot.
Bump in packages and stuff, it doesn't realize anything.
New to discussing that.
**Sergey** 11:20 I guess I can kick off a small item. Do you know if there are any decisions made, like, how to proceed with version 2, or…
about the plan, I remember Bob mentioned,
that Brett said Tamadia's, but I was just wondering…
**Chris Lightfoot-Wild** 11:35 I don't think… we've not seen,
Brett since, of where I think we discussed last time that we probably needed to run it by him and see what his thoughts were on it. But I guess you guys have probably got some thoughts on it equally, haven't you? Maybe to… is it worth flushing those out, just…
We can make note of them, and then maybe discuss it in the future.
one, so it might give Brett time to, like…
You know, mull it over, or…
Did you just want to say we'll try and commit to discuss it in future, and…
So hopefully Brett's around.
**Sergey** 12:11 Oh, okay,
So, there's a meeting with Brad, or do you mean, like, offline? Just, see, let him mull over it, and then maybe he'll, like…
**Chris Lightfoot-Wild** 12:23 I wonder if…
**Sergey** 12:24 I guess so.
**Chris Lightfoot-Wild** 12:24 Any particular questions or concerns, thoughts around…
like, the whole thing, because I think Brett said he was going to have a think about it, so I'm… I guess I'm in the same boat as you, really, wanting to see what that, what happens there.
But if we do have any…
collective thoughts. We could maybe jot them down, just because we don't know if Brett, you know, he might not be able to make it for a little bit.
**Sergey** 12:45 You mean, like, here, in this document, in the agenda?
**Chris Lightfoot-Wild** 12:49 We can… just as a… if you've got anything off the top of your head…
**Sergey** 12:52 It's not less of a thought, just mostly the question is, essentially.
because I remember, Bob mentioned that maybe we would want to have some kind of trial period for version 2 before making it main, so I'm just wondering, like, is that what we… is that… I'm sure we want to go that way? Sounds, like, reasonable, just want to see, like, what is our approach,
To version 2 will be, like, do we want to switch to it, or do we want to let users reuse it in some way?
And then… so, essentially, maybe there will be some time period where we'll have both.
Version 2 and version 1, like.
It's more of a question, less of a, you know, suggestion, considering, like, what are people thinking about it? Like, how this feature will go.
**Pawel Filipczak** 13:37 So I think we should at least create something
Some kind of dock with the braking changes, because if there is no braking changes, then we can try to go.
But if there are any breaking changes, then it can, you know, that's so many production environments. If someone is using code error in the production, then it might be a difficult issue. There might be any issues, right? If they're using SDK and something is not, you know.
compatible, then… We should, you know, take into consideration, too.
Create some immigration doc, or if there's a need for that, something like that.
**Sergey** 14:18 If I understood correctly, the breaking chain is not regarding the data, so data is still produced, although, in light of what was said in the previous meeting.
there are the issues with this data attribute, so putting that aside, maybe not related to version 2. Yeah, so, if I'm sorry, from user point of view, it might not be, but maybe, like, from… from people that compose the applications, which exten… which instrumentation is available to use, with which,
Yeah, that's… that's probably correct, what you're saying, is that, like, what is the… so if they will exist at the same time, version 2 and version 1, then what does it… what does it mean regarding the instrumentations, right? So now you need to also… certain versions of instrumentations that will be compatible.
With the… will we bump all the instrumentations also to some major version?
I guess that will, probably will be something that will be exposed to users, they need to be aware of it, right?
Well, let's say, depending on whom we call users, like, let's say, application developers, or…
Whoever deploys it,
I think in classic model, it's mostly application developers themselves will introduce dependency, and they will package the application.
We do tell… As part of it, right? Assuming that's the…
That's the way people do it, then…
And then… but I guess for the end, like, DevOps that get the data and analyze it, that probably… they don't care about that, right? Assuming the data is fully compatible.
**Chris Lightfoot-Wild** 15:53 Yeah, I think there was some other bits that had just dropped off in terms of, like, the braking changes. You were mentioning, Powell, with, some of the transports and the way you register
Exporters and things like that.
Which, obviously, all the packages will need to update to reflect V2 as well.
And then, I guess, I think one of the…
considerations was about how we have, like, the, you know, the monorepo split, and how we maintain various branches, and…
And that affects both contraum and… Man, does that…
I don't know, I think… I remember Bob saying about,
There was, you know, back in the day, these were all split, and then they kind of merged together, but…
Seems… I don't know, like, complicated now to try and… Bye.
Keeping it as well.
**Sergey** 16:58 Did you guys ever see any benefit of having those separate packages from monorepo? Like, instead of having just one SDK and, okay, let's say API,
Although… okay, for dependency's sake, maybe it makes sense to separate API and SDK, but is there any advantage of having, like, multiple pieces that the SDK is composed of? Like, if I understand correctly, there's only one API, but then there are multiple…
Implementation pieces, right? Like, exporters and all that stuff.
**Chris Lightfoot-Wild** 17:25 Yeah, I'm not sure what… I think that predated me being around as well, so I joined in that state, and .
**Sergey** 17:32 Do you see any benefit in that? Like, are there use cases where it makes sense to have this split? Like, do people use different packages for the same implementation, or is there a rationale not to use maybe some packages, or kind of, like, reduce the amount of dependencies that you pull in?
And so the one is the key.
You give us more sophisticated…
**Chris Lightfoot-Wild** 17:52 So, you could build your own SDK if you wanted.
I think, and I've seen… I think maybe Neve's got an implementation, I don't know if it, you know…
Is a full one or not?
Yeah, I'm not… I'm not entirely sure on that. I mean, is that potentially something we could jot down for…
Bob, do you think? If he's got context of.
**Sergey** 18:14 Because then it will simplify, right? If we had only one. Maybe we can, maybe Verchant 2 will also allow us to drop that, right? If there is no benefit. If you want to use alternative SDK, then that's fine, as long as it's compatible with the API, right?
It makes sense to have at least API and SDK separate, I agree, but…
Do we also split SDK into multiple pieces? Is that… because that's the issue with… if I understand correctly, the version 2, it will not affect the API. API will still be version 1, right?
**Chris Lightfoot-Wild** 18:42 Yes.
That's it.
**Sergey** 18:44 So it'll only affect… and then what you raise is that the issue, okay, so what about the other pieces, like exporters and other pieces that are released as separate packages?
how that will affect them, this version 2. Will they also be incremented?
To a new major version or not. So, like, additional questions that the question is.
if we didn't have those separate packages, that would not have been the question, right? So, is that additional complexity justified by some use cases?
**Chris Lightfoot-Wild** 19:12 Yeah.
**Sergey** 19:18 By the way, how many… do you know how many packages we build from monorepo in addition to SDK? I know that there is SDK, there is exporters.
I know there is a protobuf, but I think.
**Chris Lightfoot-Wild** 19:31 Brother Buffett's.
**Sergey** 19:32 from different repo, right? Protobiles.
**Chris Lightfoot-Wild** 19:34 Yeah, yeah, I think we've got context and semantic conventions split as well.
Hmm.
**Sergey** 19:43 It's also built from the monorepo? From Big Rippo?
**Chris Lightfoot-Wild** 19:48 Super cool.
**Sergey** 19:49 Interesting. So, maybe some people won't take dependency on… only on semantic conventions?
**Chris Lightfoot-Wild** 19:56 So, yeah, API… this configuration part of the SDK is still separate, and I think…
I thought… my understanding of that was it was kind of semi-experimental, and eventually it'd be
merged into the SDK proper.
But as it stands, that's a separate package.
And context is… These three, exports as a…
Again, another 3 of the packages there. And then SDK and semantic conventions.
So, so then that goes and splits out, and it's.
**Sergey** 20:34 I wonder, like, if some of the splits were for historical reasons, right? Maybe version 2 can eliminate that, if it's worth it?
And, yeah, maybe, you know, to use this opportunity.
To, to reevaluate if it's even worth, having,
those… all the separate packages, maybe we can… if you already introduced a new major version.
Maybe we can, do that change as well.
**Chris Lightfoot-Wild** 21:00 Yeah, perhaps it'd be good to pause that and see if Bob or Brett also know off the top of their head, or if not, we'll have to go and do a bit more digging, because I don't know how much of the…
You know, hotel specification is being, you know, followed here, that these components should be separate, and, you can…
play around with the versions, etc. But then I know…
So in our V1 of the API, there's already been some backwards incompatible changes that kind of break semantic convention, but we are…
sorry, break semantic versioning in the terms that you'd use it with Composer, but we're kind of… Quote.
hardlining, sticking to V1, because it matches the spec.
I don't know, that's just…
might confuse some people. Obviously, we're talking about it, and we're… we're here most weeks, and if you'd…
**Sergey** 21:52 spec changed even after the release of the version 1, not like the 0 or something, it changed even after version 1 was already released of the API?
**Chris Lightfoot-Wild** 22:00 I believe the OpenAPI spec itself is… sorry, not OpenAPI… OpenTelemetry spec itself has been, you know, having changes that at times have been backwards incompatible.
Well, until I think the market is stable, it's,
Permitted to do so, is my understanding?
But it is obviously just a point of frustration for a user, if you're in a PHP ecosystem.
And you expect the packages to not…
break all the time, I guess.
Again, there's probably some good reasons as it is now, or at least we can discuss it, and if there's not good reasons, maybe we could change it.
**Sergey** 22:43 Yeah, definitely agree. It would be nice if somebody could remember what are the reasons, then at least we can all evaluate and see if it's…
But, yeah, but maybe interesting opportunity, since we already incremented in my version.
If some unnecessary complexity was accumulated, For historical reasons, right?
**Chris Lightfoot-Wild** 23:05 Yeah.
And I think this document goes back quite far, doesn't it? So, it might be a bit of a graveyard of information further down, but,
It was…
**Sergey** 23:15 You mean, you mean maybe worth, searching later on? Okay.
**Chris Lightfoot-Wild** 23:18 Yeah, I've never been all the way… 156 pages of, notes back from 2019, so…
**Sergey** 23:27 Hmm.
**Chris Lightfoot-Wild** 23:29 There might be something in there that might not, I guess, but yeah. Pause that one for Bob, see if he knows.
Oops.
**Sergey** 23:39 Yeah, so then it, like you said, it will reduce this question, yeah, but now, as it stands right now, if it will continue, yeah, we also need to make a decision.
What's gonna be the versions of other pieces that build from monorepo?
**Chris Lightfoot-Wild** 23:53 I mean…
**Sergey** 23:53 Technically, if they don't depend on SDK, they add just, like, API, they might not even care, right?
If you didn't change them, you don't even need to increment diversions.
**Chris Lightfoot-Wild** 24:03 Nope.
**Sergey** 24:04 Technically.
**Chris Lightfoot-Wild** 24:05 Have you had an opportunity to test V2 in your distro at all?
**Sergey** 24:10 No, not… not yet. That probably should be, we should do soon. Is it stable enough? Is it ready for it to be tested? It's a stable thing?
**Chris Lightfoot-Wild** 24:18 From what I've seen, the changes are fairly minimal, but I think maybe the document you suggested, Powell, would be useful to know which bits explicitly have, you know, backwards incompatible changes.
**Sergey** 24:31 Do you know what was the main reason? What are the incompatible changes? Is it change to the API towards the instrumentations? Like, the way instrumentations have been registered, or…
**Chris Lightfoot-Wild** 24:40 quite a bit of cleanup with the SPI usage, and the way the, sort of, global factories and whatnot were instantiated previously, whereas some of those have been just removed, so if you wanted to register a transport factory, it needs SPI now, versus
the old way of doing it. So that… that leans into what you were suggesting, you know, with the…
The other packages that may be in Contrib have to update as well.
To support that newer behavior, so…
**Sergey** 25:10 Yeah, then we'll have a challenge of maintaining, like, if we… Depending on the…
the period, how long is this period gonna be, if we will need to continue maintaining both the branch for the one, like, this is compatible with the SDK in version 1, version 2, gonna be…
A little bit more work if you want to go with this route of, of this experimental stage for version 2, right?
**Chris Lightfoot-Wild** 25:34 Yep.
There's quite a few questions there, I guess, we can pose to Bob, and unless there's anything else, we could maybe leave it at that initial list and see, you know, if Bob's placed to answer that, or if maybe Brett wants to, chip in if he's got some thoughts around it.
Yeah, and just see… I guess generally, it would just be interesting to see what the rough timeline was. You know, is it going to be in the new year? Are we just sort of…
a state now where it's kind of frozen to a degree, and then if so, I guess…
We'd kind of want some people to test it, at least, or else we don't know that there's problems, do we?
**Sergey** 26:13 But, so when you say test it with version to the distro, what about the instrumentations? So, instrumentations, the way they register now with SDK, will it be compatible the way they do it, or essentially…
I wonder, like, if we encounter issues, even if we want to contribute change so it will be compatible with version 2, or do you know, maybe it's already in works? Do you know if, Brad or anybody else is already working on it? Like, for example, Laravel, did you have some work on the… making it compatible version 2?
**Chris Lightfoot-Wild** 26:44 I've got some changes that were relying on SPI functionality, but… I…
as far as I'm aware, in the live instrumentation, there was nothing that had changed that we're breaking for it, but it wasn't registering custom transports or anything.
But I can certainly try and give that a go as well. I guess that would just be easier if there was a beta tagged.
V2 somewhere to get, you know, Hands-on too, so…
Yeah, I could try and have a look at that.
**Sergey** 27:15 Yeah, maybe worth releasing some kind of, like, dev version of version 2, like, as a package, you mean?
**Chris Lightfoot-Wild** 27:21 Yeah, I know you can sort of compose the, you know, the entire project in, but…
**Sergey** 27:25 Trust.
**Chris Lightfoot-Wild** 27:26 that's not how it's used in the real world, is it? It's, like, split into the various component pieces, so…
Because the API is going to stick as V1, and then the rest of the…
The repo's gonna be vetoed, isn't it? So it's…
**Sergey** 27:40 But I wonder, like, the whole thing… did it have to be, like, break and change? Was it possible to keep the old way and just introduce a new way of registering, or was it, like, too hard to keep both, like.
**Chris Lightfoot-Wild** 27:56 I'd probably be inclined to say it's not that it's impossible to have done, but just the amount of,
Ongoing maintenance costs is probably the…
**Sergey** 28:08 No, because the way it sounds, like, we will have to pay it one way or the other, like, unless we say, okay, we test it internally, and we will release version 2, and that's it, all the new versions of instrumentations, they will only be compatible with version 2, right?
**Chris Lightfoot-Wild** 28:21 No.
It might be worth, potentially, if you've got thoughts on that, eyeball in the V2 branch that's up there, comparing it to Maine and seeing…
**Sergey** 28:32 Currently, the only difference is there version 2 compared to the base is only about this change. There was no new features contributed to version 2, so all the changes are related to this braking change.
**Chris Lightfoot-Wild** 28:44 I'm not…
I'm not 100% sure on that, to be honest. I thought it was just some, you know…
rejigging of existing stuff. I don't think there's anything major that's new in there, but…
Yeah, I wouldn't be… I don't think I'll… bet myself on that, 100%.
**Sergey** 29:01 Yeah, because it sounds like if we had a way to make it kind of, like, compatible, then…
We'll maybe avoid a lot of,
A lot of painful decisions, or…
Time that needs to be spent on…
All these alternative branches and all that stuff.
But, okay, let's talk a little bit.
**Chris Lightfoot-Wild** 29:19 Sorry?
**Sergey** 29:20 Please go ahead, yeah.
**Chris Lightfoot-Wild** 29:21 I was gonna say, already there's a slight overhead, isn't there, of… you know, most PIs are opened against Maine, and there is a V2 that, you know, Brett's been working on, but…
There's already, some differences that, yeah.
**Sergey** 29:35 But if this new mechanism, if there was a way to merge it back to main, and keep it as an optimized way, and then we can, with time, switch instrumentations to use it.
I wonder, like, how much of an issue it's gonna be to still maintain in this old way.
But I guess I'm talking quite abstractly about it. I need to see what is… what is the mechanism that was changed in this way. So, if it's so core that it will be too hard to maintain, kind of like, all the new together, then…
Maybe it's not… Not a technically relevant question.
**Chris Lightfoot-Wild** 30:12 Yeah, I did have… because I'd have some thoughts at one point as well about that, because obviously you can just switch based… you can check… I think what you're doing in your distro, but in C, but…
With the Composer installed versions checks and things like that, you could switch the code path to obviously use the old behavior or the new one, but…
**Sergey** 30:30 Hmm.
**Chris Lightfoot-Wild** 30:31 And I've seen, you know, a few agents that do that in their instrumentation.
But I guess it's just the difference between… Open source, and like…
Low number of maintainers versus,
you know, paid organizations doing that as a, you know, full-time job. So there's a balance between that somewhere, isn't there, I guess? But if you… I guess it would be useful if you've got more eyes on the branch, and if you think there's an obvious thing we've overlooked.
Mmm.
**Sergey** 31:00 Yeah, I agree, yeah, for me it's a bit abstract, so maybe I'm, yeah, making suggestions that are
Not… not that technically feasible. So yeah, I will take a look, and then we can… we can get back to this discussion.
Maybe we'll have additional input from Brad and Bob, Yeah, we're getting that evaluated.
**Chris Lightfoot-Wild** 31:19 I've got a question, I guess, as well, but maybe more toward, Powell. I guess we've not heard any updates so far on the, donation piece. Is that still just ongoing?
**Pawel Filipczak** 31:30 So, it's still ongoing, but there is some… there is a bit of progress, so…
Let's say we are waiting for the confirmation from the C++.
Team, and then, yeah.
then it… I guess it will be voted, so, yeah, we are very close to agreement… agreement.
And that's it. So, I'm not sure about any other steps. So, of course, there's… it should be somewhere…
There are some questions asked to the legal teams and so on.
But I'm not aware what kind of questions, what kind of feedback we'll get from them.
So, there is a dedicated Slack channel.
For the, for the, contribution.
And of donation, so it's otel-domination-elastic-outl dash phpchannel, so I'll maybe… Ulta.
Put a channel name on the… on the chart so you can paste it.
**Chris Lightfoot-Wild** 32:35 Yeah, that's probably easier, sorry, I might have probably caught that up.
**Pawel Filipczak** 32:39 This is the donation-related channel.
**Chris Lightfoot-Wild** 32:42 And.
**Pawel Filipczak** 32:45 After votes, I guess we…
**Sergey** 32:47 Second hotel, after the elastic, there is a second hotel, so I can paste it in the chat.
Are you ready a patient, Paul?
**Pawel Filipczak** 32:54 This is the channel, this is the channel name on the Slack, so… No, no, huh?
**Sergey** 33:01 I can paste it in the slack off there, if people want to.
**Pawel Filipczak** 33:05 If I paste it like this, will it work?
And I see.
This is the channel name. Auto Donation.
Elastic Autel PHP.
**Chris Lightfoot-Wild** 33:15 Yeah, acute.
I missed one of the hotels, but…
**Pawel Filipczak** 33:19 Mostly.
**Chris Lightfoot-Wild** 33:19 It was, right?
**Sergey** 33:21 There are never too few hotels, yeah.
**Pawel Filipczak** 33:23 Yeah.
**Sergey** 33:24 Too many.
**Pawel Filipczak** 33:25 So, so yeah, the conclusion is that…
it will… it will be voted on the GC level, and after that, I guess we can… we are ready to go, and we can start to work around that.
**Chris Lightfoot-Wild** 33:38 Yeah, amazing. Because I think… I might be a bit vague on the memory here, but…
I'd asked, potentially, about metrics in the past, and that was something.
**Pawel Filipczak** 33:48 Maybe we're considering…
**Sergey** 33:50 Yeah, we're definitely considered to have out-of-the-box metrics, and this is something that other SDKs have. Other, yeah, so I was just wondering, like, from what angle do you approach, like, what metrics do you thought.
**Chris Lightfoot-Wild** 34:06 What's…
**Sergey** 34:07 Do you use it.
**Chris Lightfoot-Wild** 34:07 Basic stuff that currently,
having to, like, maintain, you know, in a different data store, like Redis, and just push request counts and things like that to increment externally, and scrape it separately.
Just because of the whole, you know, everything resets per request. Yeah.
of PHP, we're not able to utilize the metrics that other languages kind of get for free.
**Pawel Filipczak** 34:32 So currently, the workaround that is in progress, so I'm working on this process thing.
Which will… which will collect the data from the workers, and then we can implement some kind of policy.
Or choose why… which kinds of policies we can…
We can implement around the metrics, some kind of different aggregation models, whatever.
But first, we need… we have to finish the collecting of the data, sending all of the data, even through this process, so I'm on that right now.
And the next step will be to get the OpAMP config distributed to all of the workers from the other side, communication from the other side.
And then I think we can focus on metrics, because they are very useful. I mean, the process metrics, the memory consumption metrics, the…
Someone also called me, I saw the contributor the GC metrics, but they can be also done from using that method, the additional process, so…
A lot of things we can achieve by this process, so, yeah.
**Sergey** 35:46 Yeah, I think we have a little bit different, meanings when we say metrics, so you, Chris, meant more like, maybe some mechanism, but although I'm not 100% sure, so currently, it's harder with PHP because we don't keep any state per process, so essentially.
If we… because I'm trying to understand, because there is still an issue if you have multiple hosts.
and they all send metrics, they… it needs to be accumulated somehow, but if I correctly, the metrics, when it's sent, it does have some kind of, like, host ID, so this way they don't mix, and they can be correctly kind of, like, combined? Is that why it's not a problem with other… for other agents, like Java?
**Pawel Filipczak** 36:25 So there is a problem, because if you have Apache, for example, and you have hundreds of workers.
And they are working in parallel, and you want to know which is the request count per… processed request per minute, for example, right? Or how many workers you have. Then it… you can
send this message, because from the current OpenTel method, you can send it from the worker, I mean, from the instance of the worker and the current script, then it's been trusted, so…
We have to, let's say, add something. You can send some… your value from a worker to this, let's say, supporting process.
Then you can aggregate it there, right?
**Sergey** 37:07 But it somehow works, like, let's say, for example, this is what I'm trying to understand, like, what's the difference between PHP and other languages, because other languages don't have this problem. They can send metrics directly from the workers.
So, for example, let's say Node.js or Java.
When they want to send metrics, they send it directly from each worker.
Now, what is the… why it works for them and not for PHP? Is it because PHP doesn't keep memory even per PID?
So, metrics do have this PID attribute, and that's why for Java and O.JS it works, and they're correctly combined from different hosts from different PIDs. They don't override each other, but instead they are being summed together. Is that why it works for other languages, but not for PHP?
**Pawel Filipczak** 37:53 how it works for the languages, so if you have the multi-proof…
**Sergey** 37:58 Essentially, the question for you, Chris, like, why… why for PHP you need this Redis, and Node.js doesn't need any Redis, it just works for it?
**Chris Lightfoot-Wild** 38:06 Well, as I understand, I guess, there is some mechanism where it's kept in memory at the counter, and then it is incrementing.
**Sergey** 38:13 Yeah, but it can only be kept memory per process, right? So, let's say if Node.js, you run multiple… let's say you have 8 cores, then you will probably run 8, 8 workers on a host, because Node.js is also not multi-threaded, right? So if you want to use all your cores, you will run 8 workers.
So, I don't know how people do it in Node.js, but let's assume they will do it. Or maybe they never do it, maybe only they run only one per host.
I'm just trying to understand why it works, but we definitely know that in languages like Java or Node, you will run at least one worker per host, right? You will have multiple hosts, they will all send the same metric, let's say request count.
And it will be correctly summed together, it will not be overriding each other, right? So metrics at least have differentiation per host.
Right? So at least metrics for different hosts, they don't mix together, they don't override each other, they… they're just being kept as different documents, and then you can sum them, right?
**Chris Lightfoot-Wild** 39:09 Yep.
**Sergey** 39:10 So, the question is now, is it the same, like, per PID? Is it the PID is also attached? So, when you will send from different, like, worker processes.
So, it sounds to me like what Pravel suggested is, if doing it, like, pure PID works for Node.js, then we just need to overcome… the only limitation that PHP has relative, let's say, to Node.js, is that in PHP, you lose memory even for the same PID, right? Each request, the memory is reset.
And it's not the case in Node.js. Node.js keeps the memory per PID,
And it can, kind of, like, increment the count internally.
**Pawel Filipczak** 39:45 You know, Sergei, Node.js is not working like that, that you have one process per thread in your… per thread in your CPU, right? The Node.js is using the lip UV underneath, so…
**Sergey** 40:01 Yeah, but technically, you cannot, like… like, if you want to use all your cores, there is no way to do it in Node.js, because at any moment, you can only run on one core, right? Again, I don't know if it's even a problem for Node.js, if you're I.O. bound, maybe you don't even care how.
**Pawel Filipczak** 40:14 Oh my god.
**Sergey** 40:14 as you use?
**Pawel Filipczak** 40:15 you have the… the Libuv is using internally the thread pool, so it's using many threads. So if you… you have this pool, and there are events, right, so there are event loops, so…
it… those events are processed in many threads, so it doesn't mean that if you have one process, then you have to create 8 processes to handle the 8 CPU cores, or 8 CPU threads. So, it's using computer analysis on my hands to…
to… to use more than one thread at the time, so…
**Sergey** 40:49 Okay, okay, let's put Node.js, maybe you're right, I'm not familiar with Node.js Mobile, it's possible that they never run multiple workers on the same host. It's, like Java, they will usually run only one worker. But, so, but…
let's say for… but at least per host, so if we will introduce this model that you suggested, Pavel, that we have this central process that will accumulate everything.
**Pawel Filipczak** 41:12 And we don't even need radius, right? That will solve the problem. Radius?
**Sergey** 41:16 Because if we will send the same metrics, let's say request count, from different hosts, it will work, because those metrics will not override each other, because they will have a special tag with some kind of, like, host ID, or host name, or whatever. They will be kept as separate things, right?
Okay.
So…
**Pawel Filipczak** 41:35 Yeah, but it depends how you split the data. It's always about splitting the data and additional…
additional data you are sending. So, of course, if you resend the thread ID, for example, or PIT ID, right? Process ID, then…
We can do everything, but if you want to get some results from the application, let's say, point of view.
Then this process… Might help to aggregate that, right?
Yeah.
**Sergey** 42:07 Right. But on the other hand, if we will add process ID now, we can even solve this problem even now, without this aggregating process, right? Except for the overhead of sending. I guess sending after each request still will have its own overhead of just sending.
**Pawel Filipczak** 42:21 Yeah. But…
But if… but if you want to, you know, sum some data between the requests from the PID, PA, and…
split it by the PID, Then, maybe, in the collector?
**Sergey** 42:36 But I don't know if it's technically possible. Chris, did you consider this? Like, adding attributes that will support this summation even without radius?
**Chris Lightfoot-Wild** 42:45 And to be honest, not looked into it for a little while, because I was kind of.
**Sergey** 42:49 What do you use for the backend? Where do you send your data? Like, is it Yagi or Jaeger, or what do you use for the backend?
**Chris Lightfoot-Wild** 42:55 No, currently we've not got, we're moving toward using a proper APM, but we're just using stuff like CloudWatch at the moment, and aggregating that way, without OTEL.
And then the team I'm on is pushing toward Hotel, and obviously wanting
Metrics as part of that to replace all the other…
Yeah, janky stuff you've got to do just to get some basic metrics.
**Sergey** 43:20 Right.
**Chris Lightfoot-Wild** 43:20 So, as…
**Sergey** 43:21 metrics, it's tricky. When you say replace metrics, do you mean, like, system metrics, CPU, memory, and stuff like that?
**Chris Lightfoot-Wild** 43:26 Just simple things like how many jobs are running, and request count, these, like, various basic stuff from us, not necessarily host metrics that we can get from collectors, but stuff about the application level counts of things that happen.
**Sergey** 43:43 Okay, so you're… so depending on your business logic, something that you count internally and you want to expose?
**Chris Lightfoot-Wild** 43:48 Yeah, yeah, that's right, yeah. And at the moment, it's like, you know, we have to push it into a Redis, stack, and then something pulls it periodically, and…
just because of the whole thing, and I tried it last with,
hotel metrics, you know, I got from 0 to 1, and then the graph just stays as 1, because every request is reset in the counter, and it… I couldn't, you know, that's kind of where it was stuck.
So…
**Sergey** 44:13 Yeah, it's very interesting, that's why I asked, like, what kind of backend, because it sounds like backend that draws that graph… it's… first of all, it's strange, because at least it should have maybe put some timestamp, and then…
kept different documents with different timestamps, because if it shows graph, it implies that it's aware of the time series, so how come it doesn't understand? Maybe it doesn't understand the fact that it's plus 1 and not just 1, so maybe that's the issue.
Neurology or something?
**Chris Lightfoot-Wild** 44:39 Yeah, I've seen there was a split between, delta and cumulative temporality that you could set in the collector, or somewhere, that maybe I could…
Maybe I can pick it up again, but I've just not… I've not seen anyone say, hey, I've got PHP hotel metrics working, and here's the… the example, so…
**Sergey** 44:57 Yeah, maybe we can…
**Chris Lightfoot-Wild** 44:58 I'm just keen on seeing what that is, and if it's already there, I'm missing it, but.
**Sergey** 45:04 Yeah, that would be interesting, maybe the request count. Well, we, as our first goal, didn't see necessarily this, because as you mentioned, it's not something that we can automatically expose with our distribution, because it depends on the application, right? So it's more, maybe.
**Chris Lightfoot-Wild** 45:18 Yeah, so it is, I just thought if there was… if you're keeping, like, a single processor, running, you know, then that is…
able to mask the export of metrics, I guess you would aggregate it in memory, and you've got one
one place, then, with that count, Avenue, where you're not…
It's not ephemeral and just resetting between requests.
**Sergey** 45:39 Yeah, I mean… but we still will need to understand the temporality, right? Because what you said, the accumulating, it's only relevant to delta temporality, right? If you do want to override, it will still override, even if it's accumulating, right? If it's not delta, if it's accumulating, then it will override. So it also depends on that.
But currently, we don't have, like what Pavel mentioned, it's something that is work in progress. Currently, we have background sending, but it's done on the second thread, in the same process, so it's still not shared between all the workers.
So, yeah, but in the future, yeah, we want to do that. Yeah, so that would be possible, like, again, if we… if we will assume that it will be only one, kind of, like, this central per…
World Host.
Because it still might be an issue if we want to have these multiple things per host, but I guess we can deal with it later.
**Chris Lightfoot-Wild** 46:30 If you have… if you… if it's ultimately some work that is planned in, it'd be cool, I guess, that…
if you've got a link to an issue or something, I could just kind of track it, just out of personal interest.
**Sergey** 46:41 Yeah, sure. We can send an issue for the… yeah, we have an issue of entry.
**Chris Lightfoot-Wild** 46:46 Well, I'm kind of… I'm interested in, you know, giving it a go at some point, so if you're, you know, I'd be… I'll be a willing volunteer.
**Sergey** 46:54 Yeah, sure, sure. I mean, I don't know what will arrive first. I guess we'll implement it first before even we will… a contribution will be accepted, but never know, maybe they will surprise it. So I guess we will first implement it.
**Chris Lightfoot-Wild** 47:06 It's part of Elastic, excuse me? I'm not trying to put any kind of pressure on it, you know, whenever, whenever.
**Sergey** 47:11 I don't know, it's not related, we're working on it. I'm just wondering if it will be first become available already as part of the hotel, after the contribution is accepted, but
if I'm being realistic, I think we'll probably… we'll have it as elastic first, and then we'll probably contribute it again. We'll add it to contribution.
That will be accepted, yeah.
**Pawel Filipczak** 47:33 I'm planning to finish it in November, so at least the semantic events, and we'll see what… about that. Maybe also the op-amp, spreading the remote configuration, but we will see.
**Chris Lightfoot-Wild** 47:46 Nice. Exciting.
**Sergey** 47:48 Yeah, but, you know, it's a bit different view on the metrics, like, when we thought about introducing the metrics as part of this distribution, we mostly were thinking about the collecting what you called host metrics.
Even though it's kind of, like, sounds like there are better mechanisms, maybe, to do it, just external probes that will just probe,
But maybe some of them is harder, like getting GC, something PHP-specific, but a lot of people just want to have it out of the box. They just install the agent, and just want to have, also the system metrics, host metrics, so… other SDKs have it out of the box, even though, you know.
there might be a point of view that it should not be part of the hotel, it's a different mechanism of probing CPU and memory, but this is what other agents already do, other SDKs.
**Chris Lightfoot-Wild** 48:35 I guess there's… because I understand some of it is other languages that, you know, support multi-threading are a lot more able to, you know, maintain these counts and…
Export asynchronously to the main thread.
**Sergey** 48:48 Yeah, definitely, technically, there are technical difficulties in PHP, pure PHP. If you want to do it as part of the… without relying on the native code, yeah, that's… that's an issue for PHP to have it. But,
I assume other agents did it, like, the decision itself to do it, even. Some might argue that it's not part of the hotel, like SDK, right? There are other mechanisms that you can do that will collect this, you can deploy.
**Chris Lightfoot-Wild** 49:13 Yeah, I mean, typically, from what I've seen, it's, you know, it's recommended you, you know, go with a sidecar or something, run the hotel collector, and that's got a host metrics module of its own, so you don't have to build it in each and every language.
**Sergey** 49:25 The collector can actively go and probe all kinds of APIs, read the CPU reading, memory reading.
**Chris Lightfoot-Wild** 49:32 You know, like, actively.
**Sergey** 49:33 Rob?
**Chris Lightfoot-Wild** 49:34 Yeah, you can mount proc into it, and then it just does whatever it does there to get some metrics out of the system.
**Sergey** 49:41 Wow, and it's the same collector that you will send spawns to? It's a part of the same thing that can run… so it's kind of like multi-purpose knife. You just run it as a demon, and you can tell it to do different things, like accept spawns, and also go and probe system metrics.
**Chris Lightfoot-Wild** 49:56 Yeah, it's got… there's loads of extensions, to it, but I think, you know, the sort of PHP documentation suggests, obviously, running that close
as close as you can to PHP, because of the limitations of.
**Sergey** 50:08 Yeah, yeah, that's… that makes sense. Well, I guess your distro is probably encompassing that, and you don't necessarily…
**Chris Lightfoot-Wild** 50:13 No, no, we don't distribute collector with,
You just… he's got a little…
**Sergey** 50:18 It's an interesting suggestion. I guess, I guess the fact that, you know, if the main reason you want to run it close is to alleviate this network issue, right, both latency and instability of the network when you're sending data.
Then, yes, the fact that we will accumulate data and send it the background, we'll remove that, so we don't need, technically, to have collector.
But, yeah, you know what? It's an interesting suggestion that you make. The package collector with that distro that we're distributing.
We didn't think about it, it's an interesting point, but I don't know, maybe we'll think about it. But no, currently we don't do it. We only package, like, some native code, and mostly SDK and instrumentations. We don't package collector with it.
So, yeah, you still need to, like, if you want… again, since we do it in the background, if the main reason you want to install collector is, to… to deal with the sending issue, right, network latency, and… yeah, so you don't need to do it, because background sending takes care of that, but…
But the other functionality that you mentioned for the collector, there's extensions that can read the system metrics.
Yeah, it makes you think, do we want to re-implement it, or just rely on Collector?
I don't know, it's an interesting point. I wonder why other SDKs then did it differently. Maybe we should investigate how they did it.
Interesting point, yeah.
**Chris Lightfoot-Wild** 51:40 Yeah, I'm not too sure of that, but I guess, let us know what you find. Sorry for asking a bunch of questions there at the end, but.
**Sergey** 51:48 No, those are very good questions. Go ahead, like, if you ever have more, definitely… that was a very interesting point about the package and the collector, and why…
if I… I just need to find out how the other SDK is implemented. Maybe just implement it really small set, so that they don't care if it's done differently than…
They just call some API, read the CPU and memory, and that's it.
**Chris Lightfoot-Wild** 52:08 I think a lot of the suggestion has just been, rather than every language duplicate every feature, you know, as long as your specific SDK can export to the collector via OTLP,
All that, you know, you can deduplicate all that effort.
Just leave it to the collector to worry about it, and get on with your application.
**Sergey** 52:30 And technically, if you implement it as a C library, a lot of this functionality, like what Brett did with Trust, right? If you can implement it and expose it as C, and then per language, you just do a really small bridge that just, you know, somehow bridges it to it.
But especially this metrics, if there was, like, a C that we could all incorporate, you know, for other agents, like, especially Java, those the managed environments, maybe harder for them. But if there was a C SDK, and it was part of the instrumentations extension.
then that one could have collected all this and have threads and whatever, right? That could have been done just in shared C, or C++, for that matter, doesn't matter.
I guess it was maybe more requirements for the environment, but, yeah.
So…
But it was not a decision. I know that some companies do it, right, Pavel? Any older company… some companies do do it, take the common code and try to… to do as much as possible in shared code, and just package which language, but…
**Pawel Filipczak** 53:34 Yeah.
**Sergey** 53:35 It's not always, you know, you need somebody to maintain that shared, finn.
But yeah, currently, It would be interesting, maybe Sipath, we can share with them.
SuperPass SDK, yeah.
In the future, or whatever.
**Chris Lightfoot-Wild** 53:54 I guess it would be interesting if there's already some dialogue, see if there's overlap there. I think that's the thing that's been discussed.
**Sergey** 54:00 I would assume that C++ probably has much less traction, because it doesn't have all this, it's not a managed language, so for you to instrument anything, it probably would require code changes, or really some kind of, like, a lot of manual…
Right, probably? I'm not aware of any…
You can maybe… you can intercept some APIs if they're using shared library, but again, you need to know which APIs, you need to somehow… but they're very hard to… to extract arguments and analyze them. Like, low-level languages like CC+, in that sense, after they're compiled.
It's really hard, because you don't have any… they optimize, so you don't have any meta-information to try at runtime to…
**Pawel Filipczak** 54:43 Huh.
**Sergey** 54:43 To do anything after it's already compiled, so you need to… to inject the code, maybe in compilation stage, and compile it in.
**Pawel Filipczak** 54:51 Yes, you have to include the library.
**Sergey** 54:55 Yeah, so… so in that sense, then, the traction for the… for C++ from the OpenTelemetry might not be as, you know, definitely not as Java, but maybe not even as PHP.
So, from that point of view…
We might, you know, even if we implement part of our design in C++, we might get much more useful than C++ itself.
**Chris Lightfoot-Wild** 55:16 Cool. Yeah.
Well, thanks for the background, I find that. I guess it's probably a good time to wrap this, and send these questions over to Bob slash Brett, see if the,
**Pawel Filipczak** 55:27 What are your thoughts on that?
**Chris Lightfoot-Wild** 55:29 yeah, thanks very much for everyone's time.
**Pawel Filipczak** 55:33 Thank you, guys. Have a nice day.
**Chris Lightfoot-Wild** 55:34 Cheers, see you later. Bye-bye.
**Sergey** 55:36 Bye.
