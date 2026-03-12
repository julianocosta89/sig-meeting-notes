SIG: PHP SIG
Date: 2026-02-04
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Chris Lightfoot-Wild 00:00:17 Hello?
Sergey 00:00:19 Hi, Chris, I don't.
Chris Lightfoot-Wild 00:00:20 Okay.
Sergey 00:00:22 Can you hear me okay?
Chris Lightfoot-Wild 00:00:24 Yeah, can you hear me?
Sergey 00:00:25 Here.
Yep, okay.
How you doing?
Chris Lightfoot-Wild 00:00:30 Jonathan, yeah, how are you?
Sergey 00:00:32 Good well, good well. It's the better time of the year.
Chris Lightfoot-Wild 00:00:36 What's going on?
Sergey 00:00:39 So despite the part of the words, yeah, so… Is it… is it below zero for you now?
Chris Lightfoot-Wild 00:00:47 Not today, it wasn't…
Sergey 00:00:49 Although I assume… it's interesting, I never… Yeah, I never thought about it. England, it's not, it's not that extreme, right?
Chris Lightfoot-Wild 00:00:56 Is it because of gold?
Sergey 00:00:57 stream, do you have any, like, warm currents around it, or…
Chris Lightfoot-Wild 00:01:01 I don't think it affects us that much. Parts of Scotland, get, like, some palm trees and stuff on their shoreline, because coconuts, like, drift across on the Gulf Stream. But yeah, I don't think we're… it's not too drastic, it's just very wet here.
Sergey 00:01:17 Yes, exactly, wetness, but you don't have anything like what they have now in states, right? Like, you know, you don't have drops, like, suddenly it will.
Chris Lightfoot-Wild 00:01:25 No, we don't get.
Sergey 00:01:26 Minus 1520.
Chris Lightfoot-Wild 00:01:29 No, not, not rare, no, it's very rare.
Sergey 00:01:32 Right.
Chris Lightfoot-Wild 00:01:33 Yeah, usually the rest of Europe is suffering before we get cold as well.
Sergey 00:01:39 Yeah, yeah, really, it moves through Europe to you, because usually it moves from Arctic, right? Although you're probably right, usually it will move from Russia, like, from Siberia, I guess. I'm not that, yeah, I know that the United States usually comes from Canada, but that's, That makes sense.
Chris Lightfoot-Wild 00:01:57 They usually call it… whenever the weather gets bad, the newspapers start calling it, like, the Beast from the East.
So it's moving from Siberia across to us. It gets cold, so…
Sergey 00:02:08 That's interesting. Hmm.
Yeah, when we have sandstorms here, it also usually comes from the east.
Chris Lightfoot-Wild 00:02:14 So.
Sergey 00:02:15 This is because all the big deserts, like in Saudi Arabia, deserts, are to the east of us, so it makes sense.
Chris Lightfoot-Wild 00:02:21 We definitely don't get that.
Sergey 00:02:23 Yeah.
Yeah, I looked at the issue that… just want to make sure, to think up with you. So I wanted to look at the issue that you… you mentioned. That is the issue with the config resolver with SPI, right? This is what you were interested in.
Oh, okay, I see that.
Chris Lightfoot-Wild 00:02:43 centralizing how that is logged.
Sergey 00:02:47 Your goal, essentially, is just to make sure that we have one source for configuration, and that source is used everywhere? Is that…
Chris Lightfoot-Wild 00:02:56 Yeah, well, one centralized place to… yeah, so it depends on… wherever you're using it within any SDK or whatever instrumentation packages, they're all… Pulling from the same place.
Sergey 00:03:10 Right, right, right. Yeah, so I wonder, so you opened an issue just for a particular theme, but I think there is at least, currently, if I remember correctly, there are at least 3 sources right now.
There is a PI source, and then there is one for the SDK, and then a separate one for instrumentations, no? Maybe I'm… maybe I'm miscounting? I wonder, like, if you want to Handle them one by one, but maybe it makes sense to create some kind of, like, umbrella issue and say, okay, this is our end goal, to kind of, like, coalesce all of them, and this is kind of going to be the first step.
Chris Lightfoot-Wild 00:03:45 I'd be happy, if you've got any time at the end of this meeting, to stick around a bit.
Sergey 00:03:49 Okay, yeah, sure, sure, yeah.
Chris Lightfoot-Wild 00:03:51 We can do that. Okay. That's alright.
Sergey 00:03:53 Yeah, sure. I remember when I was looking at it, I was kind of like, I was seeing that, instrumentations, they were kind of, like, using a different source a bit. Maybe at the end, it will come to the same place, which is good, but, yeah, let's take a look after the meeting.
Chris Lightfoot-Wild 00:04:09 Cool.
Sergey 00:04:10 Hi, Bob. How you doing?
Bob Strecansky 00:04:11 Hi, I'm doing well, how are y'all?
Sergey 00:04:13 Right, yeah. Is it still, is it still bad, by the wise, or it passed that, spell?
Bob Strecansky 00:04:20 It has been all over the place. It has been everywhere from, like, negative 10C to, like, on Friday it was 17?
So, like, big 30 degree swings are no fun.
Chris Lightfoot-Wild 00:04:32 Celsius, you're in… wow.
Bob Strecansky 00:04:36 Yeah.
Chris Lightfoot-Wild 00:04:36 Sorry, my wife keeps showing me, things on a phone of, like, doing, like, a Facebook feed or whatever, where people are putting pictures of frozen things at Orlando theme parks.
Bob Strecansky 00:04:48 Yeah.
Chris Lightfoot-Wild 00:04:49 We're warmer here than it is there.
Bob Strecansky 00:04:52 They definitely had… I know they had some ice in the fountains, because my wife showed me a picture, too. My brother lives in Charlotte, which is, like, 3 hours, like, due north of here, and they got… They got 11 inches of snow. I'm trying to think what that is in centimeters, but I think they're, like, 25 centimeters of snow.
Which is a lot.
So…
Sergey 00:05:15 Yeah, so people are reviewing all kinds of robots that can continuously plow.
Bob Strecansky 00:05:20 So, I will tell you from experience, I grew up in a climate that was very snow-ridden, and That will be one of the last things that gets perfectly automated, is snow removal, because it's just… it's, like, such a ridiculous proposition, because there's always something, right? Like, there's a chunk in the driveway, or there's, you know, a pole where there's not supposed to be one, or whatever. It's just impossible to get it all.
Chris Lightfoot-Wild 00:05:47 I mean, global warming might beat us to solving that problem, so…
Bob Strecansky 00:05:52 That's very true, it might. We'll see. Well, we're supposed to call it climate change now, Chris, because it's not just war.
Chris Lightfoot-Wild 00:05:58 Oh, okay.
Sergey 00:06:01 Yeah, they rebranded it from that.
Bob Strecansky 00:06:02 Okay. The rebrand. That's fun.
Alright, so let's get rockin'. Did anybody have any agenda topics for today?
Chris Lightfoot-Wild 00:06:15 No, we were just saying that we were gonna have a chat at the end about the config stuff, so feel free to not stick around for that, but we're just… Okay. Sergey are gonna go through some stuff.
Bob Strecansky 00:06:26 Alright, sounds good. We'll pull these up just to see if there's anything exciting, and then I'll let you all talk. I have a hard stop at 8… at 30 past the hour today, so… I'll definitely hang around until then, but… Let's see if anybody thinks that, and he should be alright.
These are… shouldn't be pretty close to all RenovateBot. I need to merge all of these RenovateBot PRs, I'll do that this week.
Chris Lightfoot-Wild 00:06:48 Yeah, it's keeping you busy, like, there's a… I see a constant stream of renovate stuff in, notifications on GitHub.
Sergey 00:06:54 tries to tire you down. I think it's inevitable, they want to force people to automate, so nobody will review it, like, to eliminate the human from the chain of command.
Bob Strecansky 00:07:05 Agreed. And I think that that's probably a… I mean, that will eventually be a good thing. These… these ones, some of these ones have been around for, you know, 2 months. I just haven't merged them and reviewed them, just following your pattern, it's okay, but, yeah, I agree, eventually we'll probably want to automate this, but for now… We ain't.
Sergey 00:07:26 But, like, I think we touched it, like, you think you're adding any value by you spending time and looking at it? You think.
Bob Strecansky 00:07:33 No, I really don't. I think…
Sergey 00:07:35 I think the… well, I think the pro… so…
Bob Strecansky 00:07:38 here's the opportunity that I find. We have unit integration tests, but they're all… like, they all have some sort of varying levels of broken, right? Like, look at all these PRs that are red, and they're not all red because… these changes introduce red. There's… there are other things we need to fix. So there's that cognitive overhead, and then there's also like, you can… I can merge all these right now, it makes no difference, because we're not doing a release. It's like, when you do the release, then you have to worry about that causing problems. So, eventually we need to come up with a good solution for that, because… and there… I don't think there is one that's the problem. It's like.
you can do the… like, you can be diligent and review each of these PRs, and then do a release, and then something can go wrong, and it's like… It would be very difficult to catch, because your unit and integration tests don't have it, and then you get… stuck, right? Like, then you have a broken release, and you either release it again with the broken one out in the wild, or you roll back, or you delete the version, or whatever.
Sergey 00:08:38 Would you say it's a lot of effort to bring all these integration tests back to the… To success? So they agree?
Is that, something that… or will they become red again really quickly? Like… What are you guys' experiences with this?
Bob Strecansky 00:08:54 I don't know. I think that it's definitely something somebody needs to take some time and effort to do.
Sergey 00:09:00 But, I think…
Bob Strecansky 00:09:02 I don't know, I…
Sergey 00:09:04 Maybe, yeah, maybe we'll put ourselves, like, but you guys see this as kind of, like, important stuff to deal with? Like, would it be helpful if we had these tests, something that we can rely on? Because we, technically, like, in Elastic, we do rely on that, like, we… like integration tests, but I wonder if you see… if you see if it's something worth investing effort in, and later maintaining, right? Keeping…
Bob Strecansky 00:09:27 Yeah, it's like, would it be valuable? 1,000% valuable. Like, there's no question. It's just who's going to do it and who's going to maintain it. I think that's where everybody just goes.
Yeah, that'd be great, but I don't want to do it. And if y'all want to do it.
Sergey 00:09:42 We can start with evaluating why… why they're red, and maybe we can, yeah, maybe we can do some kind of, like, 80-20, maybe we can keep some core stuff that must be green. We can…
Bob Strecansky 00:09:54 I have a…
Sergey 00:09:55 We can discuss.
Bob Strecansky 00:09:56 Yeah, I have a strong feeling that these are read probably because of some innocuous linting, or fan, or, you know, some sort of static analysis thing, but I haven't had a chance to dive really deep into it yet.
Yeah, I think that that's definitely something we should do, but… Let's see, is there anything exciting in here?
A Brett, a Brett PR. Very exciting.
Alright, cool.
Then, nothing crazy here… Almost to 30 million, very exciting.
Alright, so y'all wanted to talk about, SPI configuration?
Sergey 00:10:37 Wow, we're already done with the… with the regular agenda? Oh, okay.
Bob Strecansky 00:10:41 Yeah, yeah, we're definitely done with the regular agenda, we're good.
Sergey 00:10:44 Yes, yeah, so we started to talk about, so, Let me see, if I can share so we'll look at the same thing.
you're sharing. Would you mind if I…
Bob Strecansky 00:10:58 Oh, sure.
Sergey 00:10:59 No problem. Okay.
So… We talked about this issue. Please let me know when you can see my screen. Let me make it bigger.
Chris Lightfoot-Wild 00:11:09 We see it.
Sergey 00:11:10 Right. We're talking about this issue, right?
Chris Lightfoot-Wild 00:11:13 Yeah, that's it?
Sergey 00:11:14 Right? Yeah. So, we started to discuss with Chris that the eventual goal is to coalesce all the configuration sources into one, so we have one configuration source, right? Right, Chris? Did I convey it correctly?
Chris Lightfoot-Wild 00:11:30 Yeah, that's it.
Sergey 00:11:32 Okay, so… and this issue is, essentially wants to, to deal with this, right? So it essentially… this is additional configuration that currently is not in line with SPI, right?
Chris Lightfoot-Wild 00:11:46 Yeah, I think it explicitly looks in the environment of Server Super Global itself.
which the other SPI-based stuff may populate.
But equally may not. So… He's trying to unify.
Sergey 00:12:01 You're saying that this by itself is not the… it still relies on something that you can plug via SPI, but you would prefer… but this kind of sounds like a necessary additional layer that we can just defer, because we already have this kind of source or similar interface at SPI, we can just remove this one and use that one, right?
Chris Lightfoot-Wild 00:12:22 Yeah, well, I kind of imagine that there'd be an interface here for the… and it would be promoted from the SDK into the API for loading configuration.
And then, because if you scroll down a bit in this file, the getVariable function.
Just reaching into the server, or…
Sergey 00:12:41 Oh, okay, so you cannot, you cannot control it via the SPI, because it will go directly… Okay.
Chris Lightfoot-Wild 00:12:48 We can obviously have the default implementation do this, but then the SPI stuff can take over.
So that, yeah, in my head, that was the loose kind of idea, that there's one way of doing it, and then, obviously, if you want to, with a distro, like, cut in line and provide your config, you're able to do so.
Sergey 00:13:07 Yes, that definitely would be the best, like, if we could, in some way, yeah, we can discuss how, like, I do agree with you, but, what I remember, let me see if I can, I don't have it working now, but I remember, like, I can, I can bring more, kind of, like, sure that I have it together. Maybe I can find it now. But I remember when I was trying to trace how configuration is being read, I remember I was seeing that it's being read at least, Two different ways, by instrumentations and, and by, SDK itself. So, for example, this configuration, class, I think… Yeah, I need to maybe invest some time to prepare But I remember I was read… I was seeing that, what is passed into the… when instrumentations are created, the stuff that is passed there, like, for example, this… this kind of, like, classes, are they… they are different from the one that we just saw, right? They are additional… let's go back to the one that we saw.
Oops, this one, right? Yeah, so this is the configuration resolver.
And this is, implemented as the configuration resolver interface.
And then we have these kind of, like, classes that also seem to be reading… I don't know, can I jump to this?
This is also the source… Please go ahead.
Chris Lightfoot-Wild 00:14:35 I think there's something called Composite Resolver, somewhere as well, that utilizes this SPI one.
Under the hood.
Sergey 00:14:42 You think this one is SPI, you can replace it with SPI? This one?
Chris Lightfoot-Wild 00:14:47 Excellent.
Sergey 00:14:48 source?
Chris Lightfoot-Wild 00:14:48 Yeah, if you look for the, composite resolver in there, I mean, I could try and…
Sergey 00:14:53 Okay, I see, so you're thinking.
Chris Lightfoot-Wild 00:14:55 Eventually.
Sergey 00:14:56 Actually, so these are okay.
Okay.
I guess it will be… I can prepare, like, I can find myself, like, what are the sources that I saw, and then next meeting we can, we can just summarize, and maybe we can… Essentially, describe how this… what is the state now? Like, how many different ways to read configuration we have now? And then, What we… what we want to be the eventual state, and what are the steps that we need to take to get there.
But, I remember I was not sure, like, if it's, if it eventually… but maybe there were already changes done. Maybe it's the way it is now, is, by the way, Are we… what we are discussing now, is that something that we're planning for V2, or for the current, for V1?
Chris Lightfoot-Wild 00:15:55 Well, I think it would work in V1.
Sergey 00:15:58 Right, right.
Chris Lightfoot-Wild 00:15:59 Has anything backwards incompatible with it?
Sergey 00:16:01 Okay, you think this area is the same in V2 anyway, so there's not going to be much of a difference?
Chris Lightfoot-Wild 00:16:07 Yeah, I don't think so.
Sergey 00:16:08 Okay, that's good. I just want to make sure, I'm not familiar with what are the changes in VIT2 that, That, if there are changes in this area. So, yeah, so… I remember I saw a couple of, of sources, but assuming that maybe there are, maybe there aren't, what, what do you think are the next steps that needs to be taken to move it forward? How can I help?
Chris Lightfoot-Wild 00:16:36 I guess… It would be good to know how you use it in the distro, or would want to… would want to hook into it yourself.
Right.
Sergey 00:16:45 Right.
The way we use it now, the way we use it now, I think, let me quickly see… The way we use configuration now is we plug via… Let me see, quickly… We plug via the… Let me quickly see… so we have this remote configuration handler.
And I think… no, maybe it… yeah, this one is attribute?
So I need to remember how does it do it with the configuration.
Chris Lightfoot-Wild 00:17:18 You just inject it into globals, presumably.
Sergey 00:17:21 Yeah, some of it, it just goes and injects it via the globals, but some of it, maybe all of it, yeah, maybe you're right. For now, we decided to do it sim… Yes, I assume you're probably right, So, for example, when I want to set, like, log level, then it will just go and set log level, right? I guess we can even see this is the configuration option, so they assume it goes and just sets it, Directly, let me see… Yeah. So it just goes and sets the environment variable directly.
So, yeah, if we can do it in a more modular way, so we don't do it via environment variables, that probably will be better.
I remember I also tried to inject, but I think this is for the… yeah, this is for this, I remember I was using SPI for something, but I think, yeah, this one, for example. This is in order to inject attributes, but not for configuration. So, if you could do it for… Also, for configuration, that would be better, more module, yeah.
If we can inject the configuration source. But the… remember we discussed… I think the additional challenge for the way we want to do it is, How do we control, like, what is the priority for this additional source, right?
Chris Lightfoot-Wild 00:18:46 Missouri.
Sergey 00:18:46 if we do it directly from SPI, I remember we discussed it, like, if it can be cleanly done just by SPI, but we don't necessarily need Noon?
the… yeah, I guess, if there is already… the way the current state of SPI allows that, like, if you can inject additional source and say, this is the top level, right? So, essentially, it's the first one that needs to be queried, and only if it responds negatively, then it should proceed to the next one, but I'm not sure if SPI doesn't have this concept of kind of, like, you know, chain of, of, implementing inter… interface implementers, and you query them. I guess it needs to be done, maybe, in code. I'm not sure if.
Chris Lightfoot-Wild 00:19:29 Yeah, the V2 branch, Brett's got something where it programmatically looks through, and there's, like, a weighting aspect to it, so it…
Sergey 00:19:37 Salts the array first, and then, you know, picks a…
Chris Lightfoot-Wild 00:19:40 Heaviest weight, so… So we could replicate that.
Sergey 00:19:45 Waiting, I'm not sure, like, waiting, if I assume correctly, waiting will just, just only query the top-level one, like, I'm not sure if there's a concept of… can you say… but I will take a look at it in V2, you say, right?
Chris Lightfoot-Wild 00:19:59 But if you want…
Sergey 00:19:59 have it work in V1.
Chris Lightfoot-Wild 00:20:02 I was gonna say, sorry, it iterates through them until it gets a result back, so if the first one is greedy and just says, yeah, here's the result, then it would stop at the first one.
Sergey 00:20:12 Okay, so it understands that you can tell it that you don't have the result, so it understands the concept of negative response.
Chris Lightfoot-Wild 00:20:19 Yep.
Sergey 00:20:20 I see.
Okay, yeah, that will work, if we can, if we can do it cleanly this way, because otherwise, we essentially need to understand what are the current configuration sources, kind of like local, if you call them, and then we essentially need to wrap them, and, something similar to what I thought that you did, but I don't know if you already changed that.
What you did with, with the .env reader, right? So, essentially.
you had to rub the other sources and essentially use them in case there is no . Doesn't contain that, right?
Don't remember, is it in provider?
Do you remember where the .env implementation that you implemented?
Chris Lightfoot-Wild 00:21:06 Is it just in the SDK, potentially?
Oh, in the config… what's in the configuration that you just had?
Sergey 00:21:14 It's inside the SDK configuration.
Chris Lightfoot-Wild 00:21:19 I can't remember off the top of… off the top of my head, unfortunately.
Sergey 00:21:23 We in Maine, right? Yeah.
So…
Chris Lightfoot-Wild 00:21:29 But if you search in the… so go to File on the left-hand side there, just the composite Resolver, if you type that in there, because that's the thing that I've seen a lot of instrumentation packages.
Sergey 00:21:38 Was it resolved?
Chris Lightfoot-Wild 00:21:39 The larval instrumentation is using that in places. Yes, if you love that one.
Sergey 00:21:43 This one, right? Composites only? Yeah.
Chris Lightfoot-Wild 00:21:45 And then that is loading, so things typically call a static to get the instance of this, and then it… loads from, SPI with that Resolver interface.
And then falls back to those two built-in ones that are in the SDK.
But then that functionality is also duplicated in the original one in the API, And then, obviously, you've got this thing where you're injecting it into the environment at some point.
I don't know how early you inject into the environment, but do you happen to do it before this runs, and do any of these.
Sergey 00:22:17 Yes, we do it before we load SDK.
Chris Lightfoot-Wild 00:22:20 And do any of these things then clobber your config?
Which, you know, is probably not desired.
Sergey 00:22:27 So my concern with this is, so this approach is fine if this is what we want, like, essentially, you know, to me, to see that it being hard-coded is kind of, like, means that, okay, so it's kind of, like, pluggable, but not 100%, right? So… But that's fine, like, if we decided that… for me, this piece is probably the problematic one, because essentially, if somebody wants .env to be active, I don't want to remove it, right, by registering remote. I want remote to be queried first.
But then, if it doesn't have the result, then it should go to the other ones that are also being registered via the SPI, right? I don't want to replace the… all the rest of the SPI, I only want to have the first chance of refusal.
So this is what you described with weights.
But again, if we… if we just want to solve the problem, that's why I'm not necessarily tying together, like, your goal to just unifying all the sources and bringing them all on the SPI. I think it will be… it's a good goal, even if, though.
without, like, what you said, implemented on V2, it will not be, like, easily possible to register remote additional handler, but that's not the problem, we can just easily take this and, wrap it, and just, you know, in some way, It will take maybe some thinking, how can we easily do it, but, yeah, maybe… I will have to think about it, like, again, we don't want to duplicate if it already exists with V2, and if V2 will come soon, maybe.
We can…
Chris Lightfoot-Wild 00:24:01 The way your distro works is you've vendor… you have your own vendor directory, don't you?
Sergey 00:24:07 Yes, yep,
Chris Lightfoot-Wild 00:24:08 And then the way the SPI works, there's, outside of the runtime, there's a composer script.
Generates the, service?
Service provider's file, and that ends up living in the applications vendor directory.
Sergey 00:24:22 But we also run Composer install on our distro, right? So, when we register SPI, we can register… yes, so there are gonna be two competitive, Composer you can say Composer installations, let's call them this way. So this file that you said, plugin is generated, essentially will have two copies of this file, they will be different. One was generated during the Composer install on application code.
And one that comes with our distro, and it will leave it… so essentially, the first step when distro loads, it will load that file, so all the SPI will be executed based on the composer install on distro.
And then, when application will load, right, later, then it will also will have a chance to execute its own SPI, but But it will be too late for that SDK that we will load, right? So we will already load SDK before even application loads.
Chris Lightfoot-Wild 00:25:17 Yeah, so you've, you've, like, grabbed and inserted your own vendored… Generate some…
Sergey 00:25:23 and so… So, but, what we are working on now, I mentioned a couple of times in the past, and we're almost done working on that, there will be.
Chris Lightfoot-Wild 00:25:32 10 specimen.
Sergey 00:25:33 SDK. They're gonna be shaded, copied, different namespace?
Chris Lightfoot-Wild 00:25:37 And it will…
Sergey 00:25:37 keep it in our distro, so it will not… like, second step after we'll have the shaded, we will maybe install some bridge via the instrumentation, and essentially we will Miro, all the… requests on the application SDK.
If it's compatible with our SDK, we will just intercept all those calls and mirror them They will be executed on application, but they will also mirror them on our copy of SDK. So essentially, how it will be from SPI point of view, it's an interesting question.
That might be challenging, we'll have to see.
If we will have a way to kind of, like, do whatever SPI does on that copy, also do it on our copy, even though it will be after SDK is already loaded, so it might be challenging, I don't know if it will be even possible.
Because, like I said, the application loads later, after the distro. Distro loads first, and then application loads.
And then it loads its own, if it has its own copy. But, I'm not sure if we want to put that use case as the most important one, right? Because if we consider, like, what are the chances that people also bring… also use distro, and they have their own SDK, kind of, like, less… we only want to make sure that we don't crash the application first, to make sure that they are completely, kind of, have, you know, 100%, great experience, like, whatever they do with their own Open SDK, we also, you know, create the same spans, and they're all integrated beautifully in the same trays, all that stuff. Of course, it's gonna be, you know.
It would have been great if we can achieve that, but I wouldn't… like, our main goal currently to shadow… why we're shadowing is mostly because we don't want to… what you had, the problems that you have in Composer, right? We don't want to cause the problems to the application itself, right? We don't want to cause clashes because we are loading the same classes.
That might not be compatible. So, that's why we shade on, just to make sure that application can function as before, even if it has its own Hotel SDK.
But.
Chris Lightfoot-Wild 00:27:46 I suppose in that, in the example on the screen, the environment resolver there, the second, the line below that you've highlighted.
if that was… say that class did… was provided by the, the SDK, or it's part of the API's default loading mechanism, I guess that is something you could… intercepting your distro, isn't it? To say, actually, no, use our version of this, and you load it first.
Sergey 00:28:10 Well, but it will happen too late for us, so this line, yes, we can intercept it technically, but this, on our copying SDK, this method already long passed.
So, for us to go back and reapply it on the SDK that already passed this stage.
Might be… challenging.
Right? Because we're loading our SDK first.
we… possibly that we already may be doing something with it, and then only later application loads, and if it starts to do stuff on its own copy of SDK, to go and apply the same steps that application applying on its own SDK, to also apply them on our SDK is gonna… it might be challenging. Like, creating spans, so that's why this might be the most challenging, all this configuration stuff. First, we only want to make sure, like, for example, that's why I think, maybe API, we even… like, we're more interested in API, maybe, first, so make sure, like, if application creates manual spawns via the API, we want to make sure that those spawns are integrated with spawns that we will create.
With the instrumentations that are packaged with the distro, right?
Chris Lightfoot-Wild 00:29:17 So, but…
Sergey 00:29:18 this is… I assume this is kind of like the, you know, the pinnacle of this, to make sure the configuration is also applied. That's going to be challenging, because of the, like I said, the differences in time when it's done, right? When an application is loaded, it's much later, and Maybe we can do some trickery, and maybe we can keep our SDK kind of, like, you know, half incubated, and only apply, you know, like… but there is a chicken and egg problem here, right? So, we need the SDK to be ready, creating spuns when application invokes any of the technologies that we have instrumentations for.
So… if we would want to keep this kind of, like, not finished state, but needs to be finished the moment we need it to be finished, right? So, it's challenging, we need to think how to do it, but I wouldn't concentrate now. Like, I would probably say, if your goal currently with this issue is, let's… Let's unify configuration source. I think it's a good goal, we need to do it anyway, right? We don't need, you know, to, you know, stop just because we had some issues in much more advanced use cases.
Chris Lightfoot-Wild 00:30:27 Yeah.
I've got a rough idea in my head of how to influence, so maybe I could, like, do a proof-of-concept PR or something, and then… Because I understand your distro, you use the, preload… PHP in the option, don't you, to, like, load your script first?
Sergey 00:30:44 Well, we'll load it directly from native. We have extensions.
Chris Lightfoot-Wild 00:30:47 Oh, okay.
Sergey 00:30:48 that loads it directly by… when request init is called, invoked on extension. Extension goes and loads directly the PHP part of the distro.
Chris Lightfoot-Wild 00:30:58 So you wanted to beat the vendor autoload part, you're… you run ahead of that, don't you? You intercept… like, the first instruction of the PHP script is you doing.
Sergey 00:31:09 Yeah, it's long before, it's done long before… we don't even know, like, for us, it sometimes would be challenging, because we don't always know even when the application is located. Like, if you wanted to implement what you implemented, like, find .en file.
We will not even… we might not even be sure 100% where it is.
Because sometimes we start really early, and we don't have any reference, like, what is the… where is the location of the… I guess we can try to do it, like, if we go and integrate with Apache, like… because obviously we have URL, right? And Apache or FPM, they know how to map URL, Back to the file system location and find what is the initial script that they need to invoke to bootstrap.
But technically, we're even before that stage, right? So we invoked from the native. But again, all this can be changed if we need to. The goal is to, you know, have ability to do stuff. If we have, at the end, like you mentioned, this preload option.
If it will achieve what we need, we can even use that.
Chris Lightfoot-Wild 00:32:10 The version of the OpenTelemetry SDK at the moment, then.
Is that something that you expect the application to have a copy of as well, or do you just provide it in the distro and say the application doesn't need to have it at all?
Sergey 00:32:24 Yeah, for us, it would be preferable if it doesn't have a copy of SDK, right? Because we need to work hard, like I said, with the shadowing, just to handle this use case. Yes, for us, the best application is… so, our approach is for DevOps, right? So, essentially, they have applications, PHP applications that they want to monitor.
They don't need any cooperation from development team, and so assuming the development team doesn't even know anything about OpenTelemetry, and they definitely didn't put anything in Compose or JSON, you know, to have… even API, not to mention SDK, so they don't have anything, we bring everything from outside.
Chris Lightfoot-Wild 00:33:00 So there's no easy way of then knowing, after you've, like, bootstrapped your part of the system, before the application code loads.
What vendored versions of things it's gonna pull in.
Sergey 00:33:14 I mean, there is a way, right? Because we can even instrument composer methods. We can intercept when we see a composer is loading something for the application, right? We can intercept that stuff.
But the issue will be there, like I said, the time, right? The time. Because if we will bootstrap the SDK ourselves, then SDK already will be past the stage where it can be configured, right?
Chris Lightfoot-Wild 00:33:36 So…
Sergey 00:33:37 when the application will start to configure its own SDK, that might be too late for us. We can obviously recreate that instance, we can do all kinds of trickery if we want, right?
Chris Lightfoot-Wild 00:33:47 Yeah.
Sergey 00:33:48 like, it's all the question, what is the best technical way to do it. But, the question at the end, what is the end result, right?
like, I'm trying to think, like, if you say, yeah, but I want to be able to use this .env file, right, for example, right? And .env will be, we need, in order for us to find it, like.
I'm just trying to find real use cases, where would we need to… Because, It's all the question, essentially… what are the chances that, like, if there will be so little amount of applications that will have this, you know, integration with the hotel SDK, it's worth thinking about, like, what is the percentage of those, and what are the features that will be missing that we… like, even .env file that you implemented, I think it will even work without… let's assume that we want to be able to load configuration from .env.
I think it will work, like, if we, will have this, being loaded from when we bootstrap, it's all based on the current directory. Assuming that we are… when we are being run, Apache or FPM already changed the current directory to the root of the application.
then .en file will be read correctly, even though it was read just because we bootstrapped our copy of SDK, But it will find it, right? So, from that point of view, I mean, obviously more advanced use cases, like if somebody will implement their own configuration resolver for us, right, and it will be packaged with application, then yes, we will not invoke it, obviously, because then it will be too late, and.
Chris Lightfoot-Wild 00:35:31 And then…
Sergey 00:35:31 will be only invoked on the copy of the SDK that came with the application.
Right? So… At the end, by the way, it will work from the application point of view, like, application has its own configuration, it will send… maybe it will send to the same backend, like, to the same collector.
the biggest problem with that, it will be two separate traces, right? They will not be integrated between them.
But it's not, like, end of the world, right? So the goal… it will… let's say it this way, it will be partially integrated. The results might be kind of, like, unexpected, in the sense that if we get to the second stage that I mentioned, where we will intercept the calls to the API, Right? Let's say we don't do the configuration, but we do intercept the calls to the API, and we will mirror them on our copy of SDK. Then, those spans will be created in our trace as well.
It's just they might be different, because we didn't apply that configuration that was applied on that copy, right? So the results can be interesting. We can create some kind of Frankenstein here.
Because we will apply the span calls, but they will be based on different configuration.
But, if we… if we really look at how really… what can really happen, you know.
You know, theoretically.
all kinds of things can happen, but really, like, what people do put in their configuration, they might be put sampling rate, or they are putting, like, what is the IP of the collector, stuff like that, right?
How… what is the probability that we'll put something that affects the way spans are created?
I guess sampling rate, it might be interesting if they will have different sampling rate.
in their configuration, and the way Distro will be… will decide what is the sampling rate. That might be interesting to see. The results definitely will be interesting… different, and might be confusing. That's, that's something that we'll need to think how to, you know, how to handle, I agree. But, yeah, so, So, maybe, like, what you suggested, it's interesting, maybe we can… the way we can maybe solve the… since we already have, kind of, like, the concept of, In some way, like, essentially, kind of, like, dynamic configuration.
Maybe if we intercept this kind of thing, what is being done by application.
And we also use it as additional configuration source.
If we can do it in a way that can be re-read, but I don't think SDK is capable of that, so… Currently, I don't see… if it was possible for it to reconfigure itself even after it's initialized, right? After it's constructed.
then we could have just used it as additional configuration source. Like, for example, Java does have this ability, because they create an instance once, and then they need to reconfigure themselves.
every time remote configuration changes. For PHP, we didn't need that, because on each request, we recreate the SDK instance from zero, from scratch. So we can just give it new configuration, we don't need to… To think how we, you know, apply… reconfigure the SDK after it's already initialized, right?
But, yes, because that ability is really hard to implement. You… you need to essentially consider that everything that you created, all the classes, they need to be capable suddenly to reconfigure themselves. After they already created, it's a technical challenge.
Especially if you already have certain, like, traces in flight, right?
But again, for PHP, it's all irrelevant, because, like, if you take classical model.
When you have one request, one trace, and it doesn't, like… and it's usually not that long, then why would you need to change configuration in the middle of it?
It's not supposed to, you know, be minutes of trace. But if you take these new module… models, like React PHP or Swooly, when they are running long, running, like, CLI PHP, And they process many requests, maybe even multiple requests at the same time.
Then you can say, okay, but I do want to reconfigure that thing.
Chris Lightfoot-Wild 00:39:43 Yeah. That's is more challenging, how do you do that, right? So…
Sergey 00:39:47 That's, so currently, we don't even handle that, that model. We only kind of, like… so this change in environment variables, it will only work for the classical model of PHP. It will not work for the model of React PHP or Swoolly when you start it, and then it runs maybe 10, 15 minutes, and… or maybe hours.
And processes many requests, maybe multiple. Because if you have multiple requests at the same time.
you might even say, okay, when I change configuration, I'm not supposed to change it for all of them, let… because you want the request to be consistent, right? If you set sampling rate, you probably want that sampling rate to be used for this whole request until it ends, right? You don't want to change sampling rate in the middle of the request, so essentially you're saying the way… if you want to really implement it cleanly, probably you need to take the snapshot of configuration.
that was at the start of the request, you need to attach that snapshot to the request itself, and use that as a source of configuration for every decision that you make about that request, right? For all the spawns. But if Second request starts, let's say, a couple of seconds later, and configuration is already different, different sampling rate, for example.
Then you attach a different configuration snapshot to that second request, right? So, essentially, configuration should not be kept in classes like SDK and stuff. It should be kind of, like, read from outside, like, from requests.
And, it should be acted upon what this request wants to do, right? Not, It's not like one global configuration per component. Like, sampler should not have its own configuration. Sampler should take the configuration from the… from the request and apply its decisions based on the… and then the second request will give a different configuration, right? So, it's a little bit different model. It might require, like, quite a big change in some classes, where… Yeah, so… This needs to be taken into account, because when I saw how Java did it, Java did it, they didn't account for that. They essentially dope keep configuration per component, not per request. So when they dynamically change that configuration, it can introduce inconsistencies in the middle of the request.
Suddenly, you see that your half of the request was sampled out, because sampling rate was zero, but then suddenly you switched it to 100, and then you have half of the requests sampled in, right? So it will look really inconsistent.
So, but this is the decision they made, because it probably would have required much bigger refactoring to support this kind of, like.
configuration pull request thing, snapshot, yeah. But… Okay.
I remember we discussed it in the past, like, how do you even support this kind of module in the, you know, when you want to be compatible with models like React, PHP, and Swule?
That, that's what I was thinking. This is how we did it, like, in .NET and Classical, in the previous implementation. How to do it now in OpenTelemetry? Like, again, it's possible, just a question, if it's something that is, that bigger, like, obviously, you can go and over-engineer it, but, I wonder, like, how important, like, how many people run… you know, locations that are based on React PHP on Suvoli, and want to change configuration in the middle of, like… maybe people want remote configuration only because they just want to set it up, but they don't change it that frequently, so they are okay with the… Configuration being read only at the start, right, of the process, and then it's just being used, and you have to just restart your… People sometimes are really apprehensive. I know in Java world, they really don't want to have to restart applications just to comply configuration, so that might be an issue, but maybe in PHP it can be done. I know that, for example, in .NET, you can tell .NET server that, okay, just from now on.
stop using the… it will essentially, for all the new requests, it will spawn a new kind of, like, demon, and use new configuration, and all the old requests will just, until they die, they will stay with the old process.
But they will be drained out with time, and all the new ones will already have new configurations. It's kind of like gradual draining from the old to new, but this needs… I don't know if Apache is capable of that.
Like, I… So… Yeah, so what I'm trying to say here is that, Sorry if I can, like, confuse the more than necessary, but I think, If we concentrate just on what you want to achieve, there's to, you know, unifying everything into one, and if this is gonna be the… so you're saying this is gonna be the source of truth, right? This is gonna be the class?
And it's gonna be used everywhere, and this is how it's gonna look… so this is… will stay… this is how it will be, at least, for version 1, right?
I think we can live with it, like, because, Yeah, it's a little bit hard-coded, like, it's definitely not super nice in the sense that But obviously, in our, in distro, we can intercept whatever is, returned from here, and we can just wrap an hour class on top of it, right? So essentially, we will just, whatever this self wraps itself, we will wrap it.
or we will take its guts, like, this sequence, and wrap it in our… we can, you know, do some technical trickery, and just, yeah. But, to tell you the truth, like, now that you said that… now that we… after we discussed, now I really understand that whatever application does here, it will not get to our copy of SDK anyway, so this trickery is not that useful, so there is no reason to do it. So we can just completely, kind of, like, just register via SPI our remote configuration source here.
And that's it. So… So what I'm trying to say is that we will still 100% benefit from the work that you want to do, and I would really like to help, is to unify it, because this way we will make sure that everywhere is remote configuration is being used.
And, yeah, but we don't… so it will work out of the box for us as well. We will just register our remote configuration here via SPI, and it will just work, and it will read from it, and it will… and if it doesn't have a particular configuration of it, then it will fall back on the… this too.
So… Yeah, the part that will be missing is that if application registers its own, so, like, for example, if we want to support Well, I guess we will need to think, like, if we want to support .env and have remote configuration on top of it.
then, yeah, I think we'll still have to think how to do it. So, so let me ask you, maybe I'm missing something. So, if we will, let's say, we will unify and everything will pass through here, so the way it works now in version 1, if somebody registers .envreader that you implemented.
Chris Lightfoot-Wild 00:46:51 And then register something else?
Sergey 00:46:54 then that something else will override the remote read… the dot end, right? So that dot end will not function anymore, right?
But I… no, no, it will, because it's a sequence, right?
Chris Lightfoot-Wild 00:47:04 Yeah, so it's just… there's, I guess, non-deterministic order at the moment of how they are pulled in.
Sergey 00:47:10 Oh, yeah. So, the problem with the order, okay, yeah.
Chris Lightfoot-Wild 00:47:14 I could put something together in a proof of concept PR, and then.
Sergey 00:47:18 But how does it know that it needs to go down the sequence? Is there a way for it to understand that that class return that it doesn't have stuff? Like, when it's been asked to retrieve.
Okay, so there is a… null … null is considered to be a negative answer.
Chris Lightfoot-Wild 00:47:36 Yes?
Sergey 00:47:37 No, it has HES. Okay, I see.
Chris Lightfoot-Wild 00:47:39 There's something that calls this and iterates on them.
Sergey 00:47:43 This has, right?
Chris Lightfoot-Wild 00:47:44 Yes. So it will ask the has, and if… until it gets to the source that says.
Sergey 00:47:50 I have it, and then it will ask eat, right?
Chris Lightfoot-Wild 00:47:52 But I think this is a separate… the SDK configuration resolver that's a bit further down in that list on your left.
Sergey 00:47:59 But it comes through here, isn't it?
Chris Lightfoot-Wild 00:48:03 Yes, if you look at the SDK configuration.
Sergey 00:48:06 This one?
Chris Lightfoot-Wild 00:48:06 Yeah, that should implement the resolver interface, I think.
Yeah, and then that… that is what… so that is calling, on line 29, it iterates the MV source provider.
And then…
Sergey 00:48:19 But here, it's still hardcore.
The same one that was there?
Chris Lightfoot-Wild 00:48:25 This would have to change, but this is what I was suggesting. So if you scroll down in that, the read… it's got this reader read.
So the reader itself, which is that Msourcereader, so if you look at msourcereader, that… that literates… Yeah.
Sergey 00:48:42 So, end source reader, so it's a bit confusing. Env, it's not in the sense that it's only environment variable. It will also read from any file, right?
Chris Lightfoot-Wild 00:48:52 Yeah, it gets… but that was duplicating the existing behavior, which, you know, has been copied over. If you look at msource reader, that obviously takes, like, an iterable Of sources to read from.
Right. And then it retrieves.
Sergey 00:49:07 It gets this, array. So array is essentially… So, it… But this is something that maybe I'm missing. So this one is the default one that it should be used. So, essentially, I remember we already discussed it. So these two lines, they never will be actually involved, because the default one here… Okay, so I now understand… so the default one will always, will always have, will always fall back on these two anyway, right?
Chris Lightfoot-Wild 00:49:38 Yeah, which is why I think… I'd like to, part of the unification, get rid of the other ones, and then have the one that is part of the API as the default to load from those two places.
And then that is, like, the fallback one, and then you can intercept ahead of it, if you need to.
But I can put it together in a.
Sergey 00:49:56 Yeah, yeah, let's discuss it, yeah, I guess, yes. Let's say if you will… it would be great if you could, create something that we can discuss upon, yeah, it would be great, and I… I will send you the other places that I… if I will find other places, and we can handle them in separate step, or in the same step, we can decide later. Maybe you're right, maybe this is the two places that I meant, like, I sorted here and here.
But I think I also saw different interfaces, not just this resolver, because I remember I also saw interface… so this has two separate methods, that one asks if it has this configuration name, and then it relieves it, but I think I also saw interface where it goes in one step, and I think if it returns empty or null , then it's considered to be as negative. I remember I saw a different interface, and I think that interface is passed to the instrumentations, and not to the SDK itself. But I will send you, I will find it, I will send it to you. And then we can see if, if it's something that we can handle in the same step, or separate.
But, so I guess what I am not sure… I guess, yeah, it would be great if we can, if we can discuss a concrete code, because maybe it will answer my questions, because at this point, I'm kind of, like, not 100% sure, like, so is… so you're saying you will not need these two? Because, I guess my concern will be… it means that SPI will always have whatever… SPI will always traverse all the… right, so whatever SDK has by default in its composer JSON, that will always be available for SPI, but you're saying the problem is that order is not deterministic. We don't have…
Chris Lightfoot-Wild 00:51:37 At the moment, yeah, it's not… it's not accounted for, but we could obviously change it to do that.
Sergey 00:51:43 Okay.
do it in V1, we can adapt the SPI plugin to somehow control the order, but how do we configure the order for it? I wonder, it didn't come before, like, in SPI discussions, that order isn't portable. Usually, SPI is used only for one, and there's no issue of order anyway, so…
Chris Lightfoot-Wild 00:52:02 There's something on the V2 branch.
Sergey 00:52:04 Yeah, that's…
Chris Lightfoot-Wild 00:52:05 being accounted for for some internal, like, you know, as we're replacing the registry, some of the components there are weighted differently.
Sergey 00:52:14 Got it. Okay, so, yeah, if, I would be glad to cooperate with you on that. So, if you, if you can, create some kind of, like, so we can discuss upon, and look at it, and say, okay, this answers this and these questions. And from my side, I will send you, I will look for where I saw other sources, and We can either do it in this step, or we can create, like I said, umbrella issue, and defer it, and create this, you know…
Chris Lightfoot-Wild 00:52:43 As part of the distro, are you currently building a Docker image?
But, you know.
Sergey 00:52:49 Distro, or this one?
Chris Lightfoot-Wild 00:52:52 So…
Sergey 00:52:53 You asking how you can try it out?
Chris Lightfoot-Wild 00:52:56 Well, obviously I could just install the code on some, like…
Sergey 00:53:00 No, you can do it in Dockery, so if you look at the…
Chris Lightfoot-Wild 00:53:02 Anyway, but…
Sergey 00:53:03 So, yeah, it's installable, you can install it in Docker. I mean, like, for example, we have this concept of, of component tests, so essentially, we create a Docker environment, and then we install the agent, and we also… there is a mock collector, and it's kind of like end-to-end test that tests the… We call it agent, but essentially this is the part that is being run inside the application, so SDK, essentially.
Chris Lightfoot-Wild 00:53:27 If you just go into the… under prod and PHP, because I think in there you've got an OpenTelemetry namespace, isn't here.
Sergey 00:53:34 Yeah, so this is the… we only have it to substitute the, Certain classes that we needed to substitute in order to…
Chris Lightfoot-Wild 00:53:43 Yeah, so that same kind of mechanism could obviously be used for… if the API had a default way of loading config as its, the implementation of a resolver interface.
You could… you could intercept that here, couldn't you? Just say, download mine, and then you can… Do whatever you do with your remote config handler in there instead.
Sergey 00:54:05 Yeah, yeah, we can… but like you said, we don't even… like, if it can be done with the SPI, we don't even need to do that. So the only reason we.
Chris Lightfoot-Wild 00:54:13 Did it…
Sergey 00:54:14 here, we substituted these classes, preloaded them, so they will shade all the classes that came with our copy SDK.
Chris Lightfoot-Wild 00:54:22 But the only problem with the service, the SPI service loader thing is if you are… as I understand it, sorry, if you were to run… When you're creating your package, and you run and generate that file.
Are you suggesting that would be shadowed as well, or just the hotel SDK?
Sergey 00:54:44 I mean, everything will be shadowed, yeah, we don't want to clash with anything that this application wants to load, so everything in Vendor will be shadowed to beings in a different, kind of, like, random namespace.
Chris Lightfoot-Wild 00:54:55 I don't know what we can call it. The application that has… composed in various other dependencies using SPI, as I understand, then wouldn't you… wouldn't load yours…
Sergey 00:55:09 No, application will not be capable of loading anything from us, because it will be too late for it to do it, because we will load ours first anyway.
And, and… Yes, on purpose, we will do it on purpose, because we don't want, like, you remember this issue that you had with the composer when the different, it might even happen with the transitive dependency, not even direct dependency, right? We might be using a version of SDK that loads some third-party dependency that's not compatible with the version that is being brought by application in its vendor folder, right? So we don't want to get there.
So that's why we will just completely globally shadow the whole vendor folder that we have in our distro, so nothing in the vendor folder, so including these classes. Obviously, this class will also not live in the… in the… this namespace anymore, right? So we will also shadow them. So there will be… we want to get to the situation where we absolutely don't have any… Yeah. Sorry, I have a hard stop in 5 minutes, but it's good for now.
So… yeah, so what I was saying is that, That's the main purpose of shadoin is, Do… To avoid any kind of clash with whatever application might bring, right?
We don't want to, in any way, to load something that application might also bring, and then it will clash, because the versions of incompatible. But, these classes here, they were introduced for different reasons. I'm not even sure that this was a good decision for us to do it. Maybe we will revert it, because obviously we are opening ourselves here to nightmares of of, you know, merging it all the time if something changes upstream, right? The main reason this was brought here is that we implemented our own transport.
That is runs in the background, because we wanted to achieve the… we wanted not to have the delay of both gRPC, or essentially proto-serialization, and we wanted all this to be done in the background.
And especially sending, so it currently happens in the background send. I guess the proto-Cerilization still must happen on the main thread, because we need the… HP objects, right? We cannot allow them to die, so we have to first serialize them into some binary format that are copyable between threads.
And then we will copy. But we'll still do it on the… on the native side, because we wanted to optimize that part. We saw that, by default, this proto-ser serialization was really slow when it's implemented with PHP.
So… so essentially, this is what happens here, is that this class exists, but it… I think it's different from, Yeah, this converts funds, I think it comes from the… Yeah, you can see here, yeah. This comes from the native side. This, convert spuns, it's not, it's not part of the PHP part of the distro, it's implemented.
Chris Lightfoot-Wild 00:58:13 And then.
Sergey 00:58:13 by native part of the distro, and it uses native code to quickly serialize, and then I think what will happen is that there is this transport here.
That is being implemented, yeah, here. So it's eventually… so this class, I remember we made the decision to copy it, and just essentially… just to replace this line that will call our convert, and not the convert that is done by But I think.
Chris Lightfoot-Wild 00:58:45 So in the transport on the left there, the send method is deferring it, isn't it, to, like, C code?
Sergey 00:58:52 So, yeah, this send, yes, I assume it will, yes, this transport here will probably will be this class?
Chris Lightfoot-Wild 00:59:00 This will be injected.
Sergey 00:59:02 And this class, when it does send, it will… it will call this NQ, and this NQ comes also from native, you can see it here.
Chris Lightfoot-Wild 00:59:10 Yeah.
Sergey 00:59:11 So.
Chris Lightfoot-Wild 00:59:12 It's an async syndrome.
Sergey 00:59:13 Yeah, this one will essentially be async, yeah. But, I mean, the decision to copy that class, I think it's just… it's a headache, because every time we update a version of, of our dependency on upstream, we compare… I think we compare… I think we even currently cannot even update, because essentially, we need to keep this class in sync, right? So whatever changed upstream.
we need to take that code, and again, only apply this change on it. I think we just opened ourselves. I don't know if maybe we could have found a better solution, I'm not sure.
why we did it this way, but yeah. But it's definitely not, not ideal, and we… yeah. We don't want… because having this kind of approach of copying the class.
And then keeping it, and just loading it first. It's an interesting trick, but it just, it's a nightmare.
Chris Lightfoot-Wild 01:00:06 Maybe in future with SPI, maybe that's where we could… if we try and crack.
Sergey 01:00:10 Yeah, if we can also do it via ADSPI, you can avoid, yeah, that would be great, but we just need to replace this part, and not the whole code, so we'll need to… yeah, if we can inject this converter, yeah, definitely, if we could find a way just to plug this part.
and not then to drag in the, you know, this nightmare of maintenance, of copying this class, that would be great. But, yeah, yeah, that's an interesting point. We can maybe inject it via the SPI.
Chris Lightfoot-Wild 01:00:35 Well, I'll have a play it good.
Sergey 01:00:36 Okay, but yeah, please let me know, and I will have an action item on my side to send you all the sources of configuration that I will find, and please let me know when, if you want me to take a look at some initial POC, and I would be glad to do that, yeah.
Chris Lightfoot-Wild 01:00:53 Well, yeah, just ping me on Slack, and that'd be…
Sergey 01:00:55 Okay, I will do that, I will do that. Thank you, thank you. Have a nice day.
Chris Lightfoot-Wild 01:00:59 Thank you, thank you, boy.
Sergey 01:01:00 Aye.
