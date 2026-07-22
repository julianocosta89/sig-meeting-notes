SIG: Event WG
Date: 2026-07-21
Duration: 25 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 04:01 Hello, Robert. How are you?
**Pellared** 04:06 Hello, hello.
**Liudmila Molkova** 04:09 I don't know.
**Pellared** 04:10 It's been better, I have a headache recently, but it's better now. I hope it's just the weather.
**Liudmila Molkova** 04:17 You still have the heat wave?
**Pellared** 04:19 No, we don't. Actually, we have pretty nice weather, but we have very, like, sometimes we have, like, storms.
And when you get… before the start with Cloudy, I just feel very sleepy.
But at the same time, I have, recently, since, like, 2 weeks, I have a very, I don't know, stiff, you know, neck, like, you know, stiff is… So, it may be also connected with this.
Dude, I'm never sure.
We'll see. How about you?
**Liudmila Molkova** 04:51 I'm doing good.
trying to remember what happened with me in the last few weeks. It was… it's a blur. I don't remember.
**Pellared** 04:59 Yeah, same for me. We have vacations, it should be, you know.
quiet, but it's been so busy for me recently.
**Liudmila Molkova** 05:10 Yeah.
Don't know if Trask is going to join.
you might… I can be grabbing his coffee.
Oh, no way here.
Do you have anything you want to discuss?
**Pellared** 05:32 Not really, I'm just looking at CJPR right now, in the meantime, regarding the… Self-observer… self-observability… Event for shutdown.
Yeah… And I started to think how we will report the shutdown of the logar provider if it's using events.
**Liudmila Molkova** 06:02 Yeah, this is what… Josh, I think, brought up yesterday on the SEMConf call that it's almost like a separate channel.
**Pellared** 06:16 Yep.
But also, I think in the description of the issue, I think, yeah, Citro mentioned that he did it not as a… that he's starting with spends to avoid the locked self-feedback concern. Okay, so he is aware of it.
A log events reporting, log pipelines, roofs.
Oops, failing pipeline.
Okay, but… so how he wants to… how does he… he wants to solve it?
Open questions.
**Liudmila Molkova** 06:51 Yeah.
**Pellared** 06:52 Yep.
**Liudmila Molkova** 06:54 I kind of see how it can be solved with, like, okay, you… you… as a separate channel, logs is the best one, right? Because logs usually do have a separate channel.
**Pellared** 07:10 Yeah.
like, separate channel mean, like, CDL, or something like that, even?
**Liudmila Molkova** 07:17 you can, like, if you use iLogger.net, or whatever, S-Login Go or something, then… and you tell users, okay, there will be some… things written there, so… Oh, so, okay, so our generic guidance then would be that You should configure A second provider for Certain hotel, or hotel.
Which kind of makes sense, right? Because that's what we do, like, at least in .NET, they have this event source in the past, and maybe something… Different today.
internal diagnostics.
**Pellared** 07:55 In Go, we also have something which was… which is, like, pre-logs, you know, pre-logs SDK API. We have, like, internal logger, which we can also configure.
So we already have a separate, you know, logger hook, which is separate from… from Deluxe API and SDK.
**Liudmila Molkova** 08:14 Right, and it can even have a fallback to… or a default to a Studio for… important things.
**Pellared** 08:22 This is what… what it does right now, if I remember correctly. Right now, it defaults to the SDDL. So, when something goes wrong in the SDK, we just, you know, by default, push the SDDL, but if someone wants, he wants to… he can transition, you know, to… to… to null, you know, to dev null, or whatever.
to have anything, or pipe any, anywhere. They want to, I think, even push, set some custom logger there.
Yeah.
**Liudmila Molkova** 08:52 how do you deal with cases that, I don't know, instrumentation library poured something on the hot pass, and you don't really want it in a Studio, whatever?
Or only if they enable something very, very specific.
**Pellared** 09:07 I don't think we have it on the cloud path. Like, people could do it anyway, they can, you know, invoke the logger by itself, I think it's possible, but I think we usually avoid it.
The more problematic is sometimes the who can be… can cause a deadlock.
**Liudmila Molkova** 09:25 Yeah.
And essentially, Josh wanted to leave a comment on this, Pierre, I'm not sure if he did, Ed.
He kind of wants to see the vision.
On how we're… approach it… Cross-Atel, maybe an ATAP.
Because it's a big topic in general.
And, like, Event itself is probably not controversial, but how it's transmitted out is.
**Pellared** 09:53 Yes, I agree.
But that, that Josh wants it for… is he concerned only about Shut down, or about All… everything regarding to self-observability.
**Liudmila Molkova** 10:14 I'm going to guess that everything, but the shutdown is probably the hardest.
**Pellared** 10:19 Yeah, Shutdown is the second channel, for sure.
And yeah, it's also about starting… for starting up, it's the single problem. Once, you know, when the SDK starts, when the application starts, I think we have similar problems.
**Liudmila Molkova** 10:35 It's… it's different, right? Because we didn't finish setting up, maybe.
**Pellared** 10:38 Yeah, yeah, yeah, and it can also fail, you know, crash, or whatever, but you know, just the reverse.
**Liudmila Molkova** 10:45 Right, yeah. So it's like, kind of means that the separate channel is local host, not… Remote.
So I think the idea he… oh, Josh had another idea that… Maybe we should have, It can leave a trace, some persistent stuff, like a file.
And if application restarts in the same… Environment… There should… there is a chance the file remains, and you can report.
the crash you found on the file system, that's what client folks do.
**Pellared** 11:22 Okay, so it's like logs, log file.
**Liudmila Molkova** 11:28 Yeah.
Maybe it's his log or something else, yeah. The log file.
Yeah.
Anyway, we don't have CJRA, since we don't have Trask.
**Pellared** 11:51 Yeah.
Okay, anything else?
Do you want to discuss?
**Liudmila Molkova** 11:59 Not really.
The only big topic that comes up is that Python folks are finishing up Their login API, their ID is enabled.
I didn't look into the PRs yet, but a high chance that it will be done soon, merged, and then login can be declared finally stable in Python. It's still experimental.
**Pellared** 12:23 So, I can share something with you, but I'm not sure if you want to do this. So, Orisa, I'll just share my screen.
So, recently, because we thought… I thought that we are very close to making Go, you know, stable in Go.
I asked… Ai to create Compliance… Audit compliance issues for each section.
Of the specification.
And it has, you know, text like review, some part, you know, for stable statements. I can just, you know, share you later an example.
And then I ask, you know, in a loop, you know, with sub-agents, etc, so that AI will check each of these issues and validate if, you know, try to tackle each of them.
So, and I even asked… let me… So… Here is some audit.
So here is, am I still sharing? Oh, I clicked something.
Motors.
And here's, you know, a summary, you know, how many issues it found, what are the compliance problems, what are the proposed actions, etc. So, what I want to end Most of the things it catched was really legit. It was things which were not spec compliant, or things which were not clear, even from… it also found some problems, in my opinion, with the spec itself.
that some, some things will probably need to be addressed in the spec itself, because it's not, you know, the AI can't understand it than myself, even more. But the AI was very good at, reviewing both the code, you know, and spec compliance. It also found some bugs.
And also inconsistencies, so yeah, it was very good. And it took it, like, I don't know, 3 hours?
to review everything, I just, you know, started it, went for a walk, or something like that, and yeah, it did a lot of things. The one thing which I did, ensuring that I realized it, I also added to the look, created PR with FX, but there are so many of them.
that it didn't make any sense to create it. It would be just better to go, you know, just make a summary, and then go one by one, probably. Prioritize using your… maybe suggesting how to prioritize. Maybe this will be also something worth asking AI.
Because, you know, it felt like, I don't know, 20 issues, so probably asking, you know, to prioritize what to look at.
**Liudmila Molkova** 15:09 Yeah.
You know, it's, it's very interesting, so I've… I had an ask, two years ago as a TC member to review people request… to review Python compliance with LogSpec.
And I did it all by hand, and now they've been fixing these issues in the background, and I've done this review recently again. And I did pretty much what you've done, but less… Diligently, I… He definitely used the, like.
Well, I applied some filter, I ignored a bunch of noise that it gave as irrelevant, but you're much more diligent than me.
But I'm thinking, this pull request… oh, sorry, the… spec compliance review. It's one of the GC responsibilities.
And you pretty much automated it. So, would you be interested in, I don't know, creating a skill and, I don't know, suggesting it to the spec, or… community report, whatever, we would… we could use it. Like, it would be awesome for any maintainer before they ask ZC to review, to run it and see if they are compliant.
**Pellared** 16:33 Yeah, that really makes sense. Yeah, I'll think about it.
The problem with it is that sometimes I feel that, the skills are not very usable. Like, the more I learn AI, and sometimes, you know, sometimes giving too much context, it doesn't work. I'm just… maybe I'm just biased, I'm not sure, but initially, like, a few months ago, I was creating a lot of skills.
And recently, I stopped doing it. I'm not sure if it is the same for you or not. Is it the models are better right now? I'm just… I'm just not sure.
**Liudmila Molkova** 17:06 I do, but, like, I create a skill.
And I ran it multiple times.
And eventually, it… I polish it a lot, based on the feedback, and then I come running it, and I'm saying, okay, you… you had a bunch of issues, like, running through this scale. What would you suggest to be changed in the scale to make it… to avoid these issues? And, like, 50% what gives back is crap.
But 50% is golden.
**Pellared** 17:44 You're always…
**Liudmila Molkova** 17:44 I mean…
**Pellared** 17:45 I think.
These reports were in the community repo?
**Liudmila Molkova** 17:55 Let's see, Josh recently… Advertised.
Try a skill somewhere.
**Pellared** 18:07 I think it's in the Pro Tool.
**Liudmila Molkova** 18:09 Yeah.
So, the asks for the TC API review come through
**Pellared** 18:18 community.
**Liudmila Molkova** 18:19 Community Repo.
but… It could be a low-friction place.
Let me bring this up on the TC call tomorrow, what people think.
This one, I feel it belongs in the spec.
**Pellared** 18:39 Yeah, I also started to think that I can put it in the spec, even moving it, you know, moving it somewhere else would not be a problem. For sure, I… if it lands in community PR, nobody sees it.
As you, I don't know, I think the TC are the maintainers of the community, if I'm not mistaken. Usually, I do not have any notifications, or I just do not watch at them, maybe, on the community report, so probably… Yeah.
**Liudmila Molkova** 19:08 It's about this pack, it belongs to this pack, it… Helps to… like, see if the spec works. I think you would get some support, and I want to bring it up on the TC call to see if there is any strong allergies, too.
This proposal, and maybe deal with them up front.
But I… I think it would be super useful.
**Pellared** 19:34 Okay.
A creating issue.
**Liudmila Molkova** 19:40 Awesome.
**Pellared** 19:41 In a second.
**Liudmila Molkova** 19:43 So you're, you're saying that… You found a lot of problems.
In this pack itself.
**Pellared** 19:51 I'm not sure yet. I'm trying to fix first, you know, make first in the past that I have evident issues, in the… in the cloud.
I have some feelings that some things are… a little bit not correct in the spec, and in some places, I kept feeling that the spec says something, but everyone implemented it in another way.
So, the thing which I… I think the most is how… for Python, it's not a problem, because Python is single-threaded, kind of.
I think, right? But the concurrency model or not, you're using… okay? So the thing is about… but if I remember correctly, I was checking how process or shutdown works. I don't think there's a timeouting context right now in the… in the implementation, if I checked correctly.
You just shut down and wait indefinitely.
Which is…
**Liudmila Molkova** 20:46 Yeah, probably.
**Pellared** 20:47 Which is… which is probably not totally compliant with the spec. Like, I don't think there's a must, but there's a should.
On the other end, yeah, and there are these things which are in the spec that it should be, There shouldn't be a timeout.
That's one requirement, and the second is it should be possible to call it only once.
And now what it means, it means that if you time out the first time, you're not able to shut it down completely.
Because you cannot call it the second time.
**Liudmila Molkova** 21:25 I don't know how to even implement it. You could say…
**Pellared** 21:31 So, it's implemented in different ways. So, for instance, it's nicely implemented in Java.
They are really timing it out, but they do it in a separate thread. So what they do is just that, you know, they ask for shutdown timeout, but it's still running in the background routine, and if they call shutdown the second time, they just, you know, they just get, like, the.
**Liudmila Molkova** 21:52 Wow.
**Pellared** 21:52 focus.
**Liudmila Molkova** 21:53 Just idempotent, right? You can call it multiple times, actually, it's just…
**Pellared** 21:56 Decky.
**Liudmila Molkova** 21:57 Caves, as if it was called once.
**Pellared** 21:59 And it's not defined that way, you know, there's no suggestions, nothing like that in the specs. So, for instance, in… I started implementing it that way in the Go logs SDK, because I like that, but I realized that we have not done it in metrics SDK and Trace SDK, so our users will be super confused if it works differently.
Exactly.
**Liudmila Molkova** 22:22 Yeah.
**Pellared** 22:22 If you're… yeah, it's not something you know, just go back and forth, but there are certain places which… I'm not sure, maybe wrong, etc, also regarding synchronization. I think there's something… there are, like, problems in the, there are places around, which is also nothing for Python, I think, for locking, how it should synchronize, Shutdown, forced flash, and… forced flash, shutdown, and exporting.
And in my opinion, The provider is the… is the… Is the entity which is supposed to synchronize all of the stuff.
And this is not really the way the specification has described it pretty well. It's almost like… it kind of leaks. It kind of leaks, but in my opinion, it's just the way people have written it, not how it's really implemented, and yeah.
But, you know, then the AI sees those things, so it says, like, oh, specification says that this needs to be concurrent safe. It's not needed, but this is what the specification says, so you need to make it concurrent safe, even though.
**Liudmila Molkova** 23:33 Well…
**Pellared** 23:33 old…
**Liudmila Molkova** 23:37 It's another skill that's pretty useful. Take the line of the specification, or, like, a paragraph, and find how it's implemented in all SDKs, and bring some, key findings, code snippets, whatever.
**Pellared** 23:52 Yes, neither.
**Liudmila Molkova** 23:53 for it.
**Pellared** 23:54 That's true. That's true.
Yeah.
**Liudmila Molkova** 24:01 Okay, so then you'll… you'll take a look at the… and filter the… potential issues in the spec, and we'll take a look at them from the log's perspective.
**Pellared** 24:14 Could you repeat, please?
**Liudmila Molkova** 24:16 So, like, you found some issues, you don't know yet if they're real issues or not in the spec.
**Pellared** 24:21 Yeah.
**Liudmila Molkova** 24:22 You would go through them, and you would bring up the… the things that seems… Interesting to fix, possible to fix.
**Pellared** 24:30 Yeah, but probably it will be, like, months from now, because right now we have almost no maintainers, like, right now all the maintainers do not go and approvers are Splunk, and we have a policy that we want at least one other person approver from other company, and right now, David Ashpole is the only one.
**Liudmila Molkova** 24:51 As a vacation.
**Pellared** 24:52 Yes, exactly.
**Liudmila Molkova** 24:54 Okay. Yeah, that's fine. I mean, this is also already stable, so, like, adding 1, 2, 3, 5 more months to it would not really…
**Pellared** 25:04 Exactly, exactly.
**Liudmila Molkova** 25:07 Yeah.
Cool.
And, should we call it?
**Pellared** 25:12 Yep, thanks a lot, nice, nice to see you.
**Liudmila Molkova** 25:15 Good to see ya.
**Pellared** 25:17 Bye!
**Liudmila Molkova** 25:18 Bye bye.
