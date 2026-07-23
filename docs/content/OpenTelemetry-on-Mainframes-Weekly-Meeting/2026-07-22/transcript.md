SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-07-22
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 00:19 Hi, Jen. Welcome back.
**Jim Porell** 00:22 Yeah, thanks.
So happy, me and my… my best friend here.
**Ruediger Schulze (IBM)** 00:29 Oh gosh, oh, this doesn't look good.
Did you get rid of this colleague of mine?
**Jim Porell** 00:36 It's gonna be a couple months, so…
**Ruediger Schulze (IBM)** 00:38 A colleague of mine had also kind of, like, a… Accident, and still also on these type of, you know, helpers.
So,
**Jim Porell** 00:50 Did you hear the joke, though? What happened? How I did it?
**Ruediger Schulze (IBM)** 00:53 He fall down and broke this at the hips, you know, there is this at the leg, there is this, you know, which goes.
**Jim Porell** 01:00 Oh, yeah, no.
**Ruediger Schulze (IBM)** 01:00 I don't know the English words for this, but… So…
**Jim Porell** 01:05 joined, but I know what you mean. I, It's kind of a round ball. Both of mine are artificial. No, I was moving a mainframe. I was moving a Z17.
Okay.
**Ruediger Schulze (IBM)** 01:15 How's that?
**Jim Porell** 01:15 a VM workshop in Richmond, and my daughter happens to live in Richmond, so I was staying with her, and… they had boxed it up to send back to Poughkeepsie, or wherever they send these things, and the truck driver came with forks that were this wide, but they need to be that wide for this box, because it was a rack, and so we didn't have another fork, and so they had One fork in it, two guys standing on the other fork, and me pushing this way. And we got it to the door.
And the truck driver moved the truck up to the door, and on the second push out the door.
See you later!
**Ruediger Schulze (IBM)** 01:55 Okay, oh, that's.
**Jim Porell** 01:56 Yeah, not fun, but it's pretty funny that it was on a mainframe moving a mainfr.
**Ruediger Schulze (IBM)** 01:59 Yeah, I was just thinking, that's… that's a story for the mainframe's sake, right?
Don't want to have… of stories.
**Jim Porell** 02:10 So, it was pretty funny, yeah.
Whatever.
**Ruediger Schulze (IBM)** 02:14 wait maybe 2 more minutes. If nobody's joining, I can give you a little bit of update, what's… and I put it already on the… on the notes, but, I can… can walk you through. And I think you discussed a few things last week as well, but, yeah.
Let's give it another minute if somebody is joining.
**Jim Porell** 02:33 And I didn't see anything in Slack that said anybody was getting out.
**Ruediger Schulze (IBM)** 02:37 Actually, I was under the impression that Antoine may actually Be interested to join, because he was asking about the…
**Jim Porell** 02:47 Oh, just Greg says he can't make it.
**Ruediger Schulze (IBM)** 02:49 Oh, okay.
**Jim Porell** 02:53 Sorry, one.
**Ruediger Schulze (IBM)** 02:54 If nobody is joining, let me give you a couple of updates, and I put them already into the.
**Jim Porell** 02:59 Okay.
**Ruediger Schulze (IBM)** 02:59 And, into the meeting summary. Let me just add ourselves here as attendees today.
So the first thing is this… so we have this… this federated repository now, and we also started to… to look at providing first content there. I started specifically to work on semantic conventions for the HMC, And, As we are a federated repository, and as we are also working on our domain, own domain, it's, we actually want to build on the base. And, I just think I really… got a better understanding now of how to do refinements of existing metrics, and also existing definitions, which are already there. Essentially, what the community has been doing is they put forward a version 2 of how you can specify these semantic conventions, so a version 2 schema.
And I'm trying to learn this, so that's why I actually didn't open yet the PR with the content yet, because I'm still working on this, but I hope to do this in the next couple of days. Definitely before I go to some of our occasions, so that there's something that, you know, then can be discussed and reviewed, and name changes be…
**Jim Porell** 04:29 Yeah, okay.
**Ruediger Schulze (IBM)** 04:30 and everything. But I…
**Jim Porell** 04:31 Are you taking off… are you taking August off?
**Ruediger Schulze (IBM)** 04:34 I will be off in August, right? And it will be good if then, you know, feedback comes in.
And at some point, we can, you know, promote this, and this is still a development type of… stability, so this can be still adopted and changed, but then we have kind of like a, you know, clear naming, what's an LPAR, and you know, what metrics attached, how a CPU should be, or a CPU utilization.
**Jim Porell** 05:02 Yes, sir.
**Ruediger Schulze (IBM)** 05:03 You beat… be represented, and so on. So that's work in progress.
dissect?
**Jim Porell** 05:09 Are you doing all that from scratch, or is there any commonality, like, to power, or to any other… Others…
**Ruediger Schulze (IBM)** 05:16 Right?
**Jim Porell** 05:17 time stuff.
**Ruediger Schulze (IBM)** 05:18 Yeah, right now, when I started, it became actually very much, mainframe-specific, I would say, because we, you know, we are now our own domain. But what I said right now, right, I think I got a better understanding now on how to refine the You know, based on existing metrics. So I want to go actually back and make as much as possible use of what is actually in the base.
It's also the right way to do.
Nope.
it's not like, you know… I think what we don't do right now is, you know, an L power, or a power LPOR on a mainframe. I think we are not looking at these commonalities that may come in the review cycle.
the idea right now is just, let's get something out which covers what the HMC is, let's get as much as possible feedback, and then we can adjust it, right, and work from there.
**Jim Porell** 06:16 Okay.
**Ruediger Schulze (IBM)** 06:17 Hey, Antoine, thanks for joining.
I was just recapping, I… I'm still working on the PR for the HMC, I had a couple of learnings, as I just said, right, in terms of how you can do refinements now, also with version 2 of the semantic convention schema that is now there.
Okay. So, I think I'm making progress there, but I need to have a little bit more time to get this to this point, to…
**atoulme** 06:49 Alright.
Sure, let me know how I can help, if you have it, it's fine.
Happy to review whatever you have.
**Ruediger Schulze (IBM)** 06:58 Yeah.
So, the other topic, and I put 4 points on the agenda for today. Okay. And you actually asked this, I just wanted to… actually, unfortunately, I only can't confirm this. To my understanding, and I checked internally here.
There's no progress on the Jitap action runners, From what we hear. We actually don't hear anything, which is an indication that nothing is happening.
**atoulme** 07:27 Alright.
**Ruediger Schulze (IBM)** 07:28 I don't know, maybe we should go to one of these calls, established calls, and maybe put this on the agenda.
**atoulme** 07:37 I'm gonna DM the… I'm gonna go talk to the CTO of CNCF right now.
**Ruediger Schulze (IBM)** 07:44 Okay.
**atoulme** 07:45 Okay.
**Ruediger Schulze (IBM)** 07:46 Yeah, if you have hinges or ways to get this going… This would be good, Because obviously this ties then into the next topics.
**atoulme** 07:58 Okay.
Yeah, I'm just typing something to him when I'm here, but let's go to the next topic for sure.
**Ruediger Schulze (IBM)** 08:05 Yeah, so, Yeah, I've been running some kind of, like, internal, let's call it hackathon, but I used this chance to look at what can we port from OpenTelemetry to Linux on C.
And, it's actually interesting that with… With the AI tooling now, you can do ports of the… the SDKs, or also of the eBBF instrumentation.
With actually not writing any line of code, but just putting the environment there, and… the AI will handle everything for you so that you get actually a working setup.
And, the two examples that we, that we've done is, the… C++ SDK, ported it to Linux on C. This, we knew already, this is work, that this works, we had, you know.
Other activities where this has been ported manually already, but the… for other reasons, it's actually also never made it to the community, so the code that we took from the branch here or from the repo was actually just the existing the existing one with no, Linux and C support, and the other one is OB, obviously, EBF instrumentation. And there is really, you know, there was no support.
And obviously, the way of how the EVF instrumentation works there's certain porting effort required because of the engine, but also then of, you know, certain specifics of the EVF implementation on S390. So, long story short, actually.
What that shows is that there are ways of how things can be ported, obviously AI-assisted or AI-powered.
It's the tooling that is now available for developers.
But that opens, actually, the door to broaden the ecosystem. If we would have Jitap action runners, we could actually, you know, there's a little more care of Lee and WebView, bring these things to the community, integrate this, have them regularly tested, and… Then, you know, bringing things like… OB, but also the profiling, we could actually make progress. We didn't test profiling yet, but it's obviously the next thing to try out if we can get it to working.
**atoulme** 10:36 That's, at the goal… Language level… I mean, when you say profaning, do you mean a pure BPF provider of OpenTelemetry fame, or… Do you mean… something else?
**Ruediger Schulze (IBM)** 10:51 I would just pro- I assume it's one of the repos.
**atoulme** 10:56 Oh, yeah, okay.
**Ruediger Schulze (IBM)** 10:57 So funny, yeah, yeah.
**atoulme** 10:58 Not the PProf, pProf would work on S390X right now, right?
**Ruediger Schulze (IBM)** 11:05 Yeah, that should… yeah, that should work, right?
**atoulme** 11:10 Did you, did you want to open a PR for those changes for Obi?
**Ruediger Schulze (IBM)** 11:15 Not yet, because, I think the first thing is really, let's clarify the GitHub Action topic.
**atoulme** 11:25 Okay.
**Ruediger Schulze (IBM)** 11:26 I would probably want to join the CIC meetings if there is one. I haven't checked yet, actually, but OB definitely has one. There's so much activity.
**atoulme** 11:34 Ohio. Yeah, yeah. Yeah.
**Ruediger Schulze (IBM)** 11:37 I would want to join the CIC meeting before I kind of, like, bring this in, just explaining that this is there and how we can make it work.
**atoulme** 11:45 That's fine by me. Yeah, it's good signaling that you're… If you want me to, but you… you know, it looks like maybe it's better if you go to a SIG Meeting and make the announcement yourself.
I know at least one maintainer on Obi, I can let him know about you coming over.
It's just, I don't have any…
**Ruediger Schulze (IBM)** 12:07 The point is, I mean, bringing in the code really is only reasonable if you somehow have a way to regularly test this, also from a CI point of view.
Okay. And, Obviously, you know, it brings us back to the discussion that we just had, right? If he somehow can get to this agreement… Yep. And, things become much more easy.
Anyway, the good news is, you know, with kind of like this proof point now, we can actually look at other capabilities that somehow would be needed for the platform. And Jim, you obviously, you know this, right? This has also importance for CCX, for instance.
There's a few other things which… where this is reasonable and can be helpful, so…
**Jim Porell** 12:54 I don't.
**Ruediger Schulze (IBM)** 12:57 Yeah, right. That's it from my side, Antoine.
**atoulme** 13:05 Well, I can tell you that, my contact at the CNCF, who works with Jeffrey Sika, I've just let him know that we're not hearing back, and I'm… Asking him for a way to kind of get back in touch with him.
**Ruediger Schulze (IBM)** 13:18 Yeah.
**atoulme** 13:18 Let's see what he says.
So, at least I got… I've got a test balloon up in that direction. I can also work with Morgan McLean on, you know, escalating that properly, but it feels like right now that this is a good avenue to just have a little friendly poke.
In the back, without too much… Pusses.
**Ruediger Schulze (IBM)** 13:39 But we are also waiting, actually, on Jeffrey Sicker, so it's…
**atoulme** 13:43 Yes, we're… yeah.
**Ruediger Schulze (IBM)** 13:45 Correct.
**atoulme** 13:45 I'm talking to a guy on his team.
**Ruediger Schulze (IBM)** 13:47 Yeah, and I have to say this, you know, all our folks internally that would work with the CMCF, they are waiting for them as well.
**atoulme** 13:56 Yeah, so, the guy I'm talking to is Chris Anisik, who… We talked at KipCon, he gave me… He gave me a way to contact him over signal.
And so, he said that's… that's the way… that's the way to talk to him, is to send him messages on signal, which is very… not… corporate. But anyway, I… I was just texting the guy, and he, acknowledged my answer. He's going to look into it, I guess.
And so they seem to be on the same… On some staff level.
Hopefully, we can get some reading to what's going on.
And then… Period.
**Ruediger Schulze (IBM)** 14:35 Yeah, so next step, we get the HMC one going, HMC PMR going, and as I described at the beginning, then really, let's get input here from, you know, the CIC. I would also show it to Lyudmila, definitely, and maybe the semantic convention SICK for a quick review.
I also want to get a couple of other folks to look at this. Certain things about naming that I would be interested to be clarified if it's not on the base, right? If it would be platform-specific.
But yeah, that should be then the next step.
Okay, good.
**Jim Porell** 15:23 I think you doing this with the HMC is a good model to get the other stuff done. Well, like you said, you're figuring out the process, so… Probably be a little bit more expeditious.
**Ruediger Schulze (IBM)** 15:37 There's a few things in flight, I mean, so for instance, Ludwila, she's working, and I think this is really good stuff, she's working on the template, on a common template that can be used across these federated, repositories.
That will be helpful, you know, this is an area where we actually don't want to necessarily be in to have our own formatting of the output.
reusing there what the team is doing there, I think is great. So, This is on the review currently, I think it will still take a couple of… You know, minor or smaller iterations, but then, you know, we can just pull that in as well.
**Jim Porell** 16:22 Alrighty.
**Ruediger Schulze (IBM)** 16:29 Okay, alright.
Okay.
**atoulme** 16:32 Well, yeah, just let us know, I will continue to unblock you on GitHub Actions if I can.
**Ruediger Schulze (IBM)** 16:37 Yeah.
**atoulme** 16:38 No promises, but at least we can try. And then, I will… if you need help on that PR, please let me know, or let everybody know, please.
Yeah. But it looks good.
Thanks for that.
**Ruediger Schulze (IBM)** 16:49 Sure, bye-bye.
**Jim Porell** 16:50 Alright, see you next week. Bye.
**atoulme** 16:51 Next week. Bye.
