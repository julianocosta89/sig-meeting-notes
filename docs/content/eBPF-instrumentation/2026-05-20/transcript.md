SIG: eBPF instrumentation
Date: 2026-05-20
Duration: 48 minutes
============================================================

## Zoom Recording Transcript

**Mattia Meleleo** 01:38 Hello.
**Rafael Roquetto** 01:40 Hey guys, how's it going?
**Mattia Meleleo** 01:43 Pretty good. How about you?
**Rafael Roquetto** 01:46 You're getting started for the day, first meeting of the day, so…
**Florian Lehner** 01:56 Here's the other way around, last meeting of today.
**Rafael Roquetto** 01:59 Lucky you.
**Mattia Meleleo** 02:01 Yep, one hour left.
**Nikola Grcevski @ Grafana / OpenTelemetry** 03:01 Hey, everyone.
Everything's going?
**Mario Macias** 03:08 Oh… Nikola Grcevski @ Grafana / OpenTelemetry 03:09 Alright, there's Google it popping in… Okay… B.
Bye.
Oh, let me hear it.
Do you have any agenda items, please add them to the meeting?
Otherwise, we could just go through open issues.
Figuring it out… Also, add your name in the attendees list, if you haven't done.
**Rafael Roquetto** 04:37 You're the anonymous beaver. That's very… Canadian.
**Mattia Meleleo** 04:48 Not so anonymous.
**Nikola Grcevski @ Grafana / OpenTelemetry** 05:20 All three questions.
**Rafael Roquetto** 05:24 Hmm… Nikola Grcevski @ Grafana / OpenTelemetry 05:38 Okay, very unique.
Okay. Sounds like we have a quorum.
Let's get going.
I wanted to actually, specifically, since we have Floria here, somebody asked me this, recently, and I was wondering if… what you think, Florian, about this. But in Obi, we have a tiny agent.
And that sits in a Java process. We auto-inject it.
Does it make sense for us to write the, the things you need for Java agent to work, or is the existing trace profile correlation sufficient?
I know initially Elastic had a prototype, and we went to donation that had that thread information written, that thread local storage.
Just ask it.
**Florian Lehner** 06:37 Yeah, there are two approaches. I don't know if the OBI Java agent populates the context-sharing eBPF map.
If so, then it already works, then nothing needs to be done.
And there's a second approach, currently pushed by Datadog, or Datadoc people.
To share, or bring more… more process contacts from SDKs into cases like OBI and profiling. So, I think I have an open proof of concept, but there's a conflict with the… With, dependencies and, the Proto file that is used in this context is not yet merged in, in Proto. So, this is a little bit in move, the specification is merged, but it's not there yet.
There are proof-of-concept implementation for some SDKs, but not all SDKs, so we… this needs to be also done.
But, yeah, takeaway is, if the OBI Java agent populates the context map in OBI, EBF, then it works, and for the rest, we are… We are working on it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:00 Okay, got it. Okay, so it seems like Mattia, yeah, already added it. I just… yeah, I thought I'd bring it up because somebody asked me, and I said, I don't know, I guess… But… Or you don't need to…
**Mattia Meleleo** 08:12 I think it's, it's, it's what you are referring to, but yeah, anything should be tested.
Accordingly. This one is tested, but for the login reacher, for Trace Profile, maybe, I don't know.
Okay. The state's separate.
**Nikola Grcevski @ Grafana / OpenTelemetry** 08:30 I think it should be, that's pretty much it, like, if you, Yeah, I think I see what you did. Yeah, I think that should matter.
That should be fine.
The only thing is that… Yeah, this information… Yeah.
I don't know, I have to think about this, because I think this information I only… No, this is written because it's the thread info, not just on sending and receiving, so… It should be updated every time.
There's a… so we updated this information.
In the Java, from the Java agent, when… one thread.
Forks and other, and that means even with the… It schedules a new executor to be picked up through the interface of What is it, callable, runnable, any of those?
It's not necessarily every thread, it just helps us kind of relate who's done… who's the parent of… Who?
For the purpose of context propagation, so… I have to think about that. There might be… I think it might be sufficient.
I mean, we know exactly at what time the Java thread is the real Java thread. We won't know virtual threads, but that's… that's fine.
I think it should be sufficient.
Yeah.
Cool.
Alright, we need to test it. Thanks.
Well, I'm not sharing the agenda, I guess.
Share the internet.
Hmm.
Too many things open on my screen.
Okay, well, next on the list. I don't know how to share with Zoom, usually.
Maybe I can do a window.
Bacteria.
One second… Alright, my desktop is not cooperating.
Alright, well… We're here.
**Mario Macias** 11:08 I can… I carry it if you want.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:11 Okay, yeah, why don't you share it?
**Mario Macias** 11:23 Inter… interesting that my screen is not also… Nikola Grcevski @ Grafana / OpenTelemetry 11:28 Nate, they're just part…
**Mario Macias** 11:30 cooperating with you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:33 Zoom…
**Mario Macias** 11:35 Let me see… allow Zoom… oh, okay, I need to allow.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:41 Don't worry about it, I think I'm just gonna open a new… window…
**Mario Macias** 11:46 Oh, God.
**Nikola Grcevski @ Grafana / OpenTelemetry** 11:47 I think that should do it for me.
Dang.
And I should be able to share this with me right now.
Oh, and Mario did it, okay.
**Mario Macias** 12:10 Okay, any… anyhow, I… I share my screen, I guess you could.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:13 Correct.
Yep.
Okay, cool.
**Mario Macias** 12:21 Yeah, they met.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:23 Yeah.
**Mario Macias** 12:23 Here.
Rafael, these… AI policy from Chelum.
**Rafael Roquetto** 12:28 Which is actually from you, because you're the one who discovered it. I don't know if you want to talk about it, otherwise I can.
**Mario Macias** 12:35 Yeah, but basically this morning, I… I saw this… they announced.
**Nikola Grcevski @ Grafana / OpenTelemetry** 12:41 in…
**Mario Macias** 12:41 I don't remember which social network they… they shared it, and I found it very interesting. Maybe we can… we can take it as a reference.
And… and try to implement some… some similar AI… AI policy with our inter… for our interactions.
With the community, or even internal to us.
**Nikola Grcevski @ Grafana / OpenTelemetry** 13:08 Okay.
**Rafael Roquetto** 13:09 Yeah, the… Nikola Grcevski @ Grafana / OpenTelemetry 13:10 I like it.
**Rafael Roquetto** 13:11 The part that I found, like, useful was the unacceptable use. I mean, obviously everything.
**But, when they say it's not acceptable to use generative AI tools to communicate in any silly or community space with content that is substantially written using generative AI tools. I find that that if we somehow could enforce that, I don't know if you guys agree with this to begin with, right? We don't have to agree? This would… I'm hoping this would help a lot with, you know, issues being reported and PRs being raised, because… Nikola Grcevski @ Grafana / OpenTelemetry** 13:52 Probacco.
**Rafael Roquetto** 13:53 I still see that a lot of those just, like, a wall of text that is, like, a code plan or something like this, and it makes it really hard as a reviewer to… you know, extract the actual juice of it, and the fundamentals, okay, what's happening there. So, at least it forces the person to actually reason by themselves and write something more, I guess, meaningful. I don't know. I particularly like that part, but… It's just a thought.
**Mario Macias** 14:28 Yeah, I also… I also liked it.
maybe we can do a PR with this… with this AI policy, add some modification. You might consider, credit, Silium team as, inspiration, and maybe we can take the discussion offline via GitHub pull request, and then we can discuss each.
each point, and people can… can give their opinion for each of the different bullets. I don't know, what do you think?
**Rafael Roquetto** 15:06 Yeah, that works. Actually, it's in my, like, the whole AI stuff's still on my work plate, because I feel like, Copilot is not working as well as we want it.
**Mario Macias** 15:19 Yeah.
**Rafael Roquetto** 15:19 some of the policies, so I have an item on my list that I want to go back and see if there is anything that can be done. I talked a little bit.
to Steven about it, maybe either using Copilot, or see if we can actually have, like, some sort of bot that will flag.
**Mario Macias** 15:38 Yeah.
**Rafael Roquetto** 15:39 these teams, so I will… I might not be able to do this this week, but yes, I will do that if… I mean, unless anyone… someone wants to take it over, it's fine with me, but otherwise, I will… I'll get to it and incorporate that as well.
**Mario Macias** 15:52 You've been creating… creating the pull request, or with a… with this file, or… or…
**Rafael Roquetto** 15:58 Yes, yes, I can do that. Okay.
**Mario Macias** 16:00 Okay, yeah, if you are busy with other things, I can do it at the end, it's… copying and doing the PRM and stuff in the…
**Rafael Roquetto** 16:08 Well, if you want to do discussion… Cause I won't… I don't think I'll do it today, or tomorrow, but, up to you.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:15 like.
**Rafael Roquetto** 16:15 Can you do it? If you don't do it, then I'll ping you and say, hey, I'm about to do it, and then that's it.
**Mario Macias** 16:21 Okay, okay, I'll do it later, yeah.
**Rafael Roquetto** 16:24 Okay. Alright.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:26 Yeah, if we're gonna take the silly one, please reference it that it was taken from.
**Mario Macias** 16:30 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:31 And the other thing is, one thing I would suggest doing is enumerating this thing, so it should be, like, one… Acceptable use to unacceptable use. And once we have it, even if it's not enforced, if we see, bad behavior, we can just point them to the policy and say, according to rule… 2… 5?
**Mario Macias** 16:54 Okay, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 16:55 acceptable use, please resubmit after you understand the code, and then otherwise people may complain. You're closing my PR for no reason, I, you know, and so on. As long as there's a policy, and we…
**Mario Macias** 17:10 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:11 stated.
Okay. It's easy to point to the policy and say, this is against our policies, please resubmit.
**Mario Macias** 17:16 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 17:18 And we'll close the PR.
Alright.
Cool.
Okay.
What's the next one? Do you want to switch to… Maybe I can share, I think it's lovely to share now.
Okay.
Okay, okay. I guess we'll wait for Mario. So the next one on the agenda, I just wanted to point out I'm out next week, so I need somebody else. As bad as a job I'm doing today, we need someone else to do it next week, because I'm back on Thursday, whatnot.
**Mario Macias** 18:01 Happy… happy to do it.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:04 Okay.
Then, Mario… Okay, so KubeCon.
I just wanted to get a poll of hands for people here. I know Tyler was interested. I'm interested. If I can get a show of hands of who also wants to go, for KubeCon North America.
In Soul Play City in November.
then maybe we can create a list of… unless you're submitting on your own, I just want to see if you need help.
**Mattia Meleleo** 18:37 We will probably try to recycle the talk we had with Florian.
**Nikola Grcevski @ Grafana / OpenTelemetry** 18:42 Okay.
I had thoughts about that one, that's great, so I guess, Mattia… San Foreign.
If, we… could we spin, like, a real-world example that we've… optimized, or something like that, that would go better. They like those real-world use cases.
of, you know, we… there was this open source… whatever service we found with OB, some transactions were slow, we used the profiler, and we found why the… there was, like, a latency, so it's like a case study of how to use the two tools. People love that stuff. So, that will go much well. So you're presenting both tools.
How they, work together, but also… a real-world use case, that might actually help. I don't know what applications we pick, but I'm sure there's one that we can… we can use.
Michaela, I see you here. You're interested in any sort of… I know we haven't done much work, or be an injector together, but I was just wondering, maybe that might be another one, if you're interested in participating.
**Michele Mancioppi** 19:57 I have… with Antoine, we have been talking about submitting, Nikola Grcevski @ Grafana / OpenTelemetry 20:03 Pretty important.
**Michele Mancioppi** 20:04 A, talk about system packages.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:08 Dang.
**Michele Mancioppi** 20:09 We dearly, dearly, dearly hope that by then.
OBI is part of the cheery, happy family of the language system.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:16 Okay.
**Michele Mancioppi** 20:16 So I see potential synergies.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:19 Okay.
I mean, that's… it's also called, like, KubeCon-based software development. So you say you're going to talk about it as a KubeCon, and then it forces you to do it by then, at least in some form or another.
**Michele Mancioppi** 20:32 That, that strategy already twice with InJactor.
**Nikola Grcevski @ Grafana / OpenTelemetry** 20:35 There you go.
Yeah, so maybe that's another avenue. Otherwise, we have, people want to put their name, then we can come up. There's Gen AI Talk, I mean, I don't know if, Haibin has done a lot of work here.
I don't know how to engage with him, but maybe I'll reach out to him on the CNC of Slack if he's around, and see if he wants to… Participate, if he's willing, or he can go.
**Mario Macias** 21:10 Yeah, I'm adding myself as a backup. I mean, KubeCon NA is not my priority, because it's in the other side of… Of the sea, but if you are missing some co-speaker, just to give more heterogeneity and so on.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:29 I have.
**Mario Macias** 21:30 Also, to… to be there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:33 Okay, cool.
**Rafael Roquetto** 21:36 Do you think people would be interested in some OB internal talks, or would that be too… to…
**Michele Mancioppi** 21:41 Technical, like, you know… Like, catnip.
Kind of mega-nerd topics, that's what KubeCon is about.
**Rafael Roquetto** 21:50 Okay, maybe I'll submit something on that.
as well.
**Nikola Grcevski @ Grafana / OpenTelemetry** 21:58 Yeah?
**Michele Mancioppi** 21:59 I had tried, like, I think at least once, to submit a talk about the injector.
And I actually got it through when I started, when I called it the art and craft of no-data instrumentation. And it became so nerdy that people accepted it, finally. Same concept even with other talks.
**Rafael Roquetto** 22:19 Alright, good, good, that's encouraging, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:25 Alright.
**Mario Macias** 22:26 Oh, you aren't added as an attendee, Michele, do you want me to add you?
**Michele Mancioppi** 22:33 Yes, gladly. The.
**Mario Macias** 22:40 That's O, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 22:41 Zero, there's zero, yeah.
**Michele Mancioppi** 22:43 Yep.
**I mean, I was mostly intending to lurk, but then… Nikola Grcevski @ Grafana / OpenTelemetry** 22:48 That's okay. I called you up.
Okay, cool. I'll propose some ideas on the channel, and… See… see if anybody wants to… partner, and then… Antonio already… I know Tony… Antonio already submitted something about that we're gonna have to implement or attempt to POC, mixing up.
The, network instrumentation, network monitoring, and application monitoring.
Definitely interesting.
Okay.
Cool.
Alright, so open PRs? Do you want to switch to that link?
**Mario Macias** 23:37 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:37 That's what else we've, Usually…
**Mario Macias** 23:44 Okay, shall we?
**Nikola Grcevski @ Grafana / OpenTelemetry** 23:46 Bottom up, yeah.
**Mario Macias** 23:47 Yeah, bottom-up So, dependencies, dependencies, this is an experiment, very old.
update Docker, maybe most of those renovate.
**Pull requests are already updated, or, in… Nikola Grcevski @ Grafana / OpenTelemetry** 24:06 I was born March 31st, yeah.
**Mario Macias** 24:09 Maybe we can close them, and renovate will re-trigger.
Sure. So, because probably some of those have been already… Superseded by… by newer ones.
Okay, super link expands, connected, there we go. This is a draft. This is from Tyler.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:32 Yeah.
**Mario Macias** 24:33 Yeah. New socket Tracer from Rafael with the direct review, so I guess unless you… 1, 2, okay.
**Rafael Roquetto** 24:41 Yeah, about that one real quickly, now that Mattia's gRPC stuff is in, I hope to pick it up sometime.
**Mario Macias** 24:48 Sweet.
**Rafael Roquetto** 24:48 the base, yeah, we'll see.
**Mario Macias** 24:50 Okay.
Denny's, another from Portugal.
**Nikola Grcevski @ Grafana / OpenTelemetry** 24:56 Profile.
**Mario Macias** 24:57 concept from Florida. This is a proof of concept, so we can… Nikola Grcevski @ Grafana / OpenTelemetry 25:01 Do you want to talk about it for me, or do you want to skip it?
**Florian Lehner** 25:03 I'mma skip it for a moment.
**Mario Macias** 25:06 Okay, another from Steven, it's a whip. Okay, we maybe can go to this, first. Go Jess on gRPC.
by Span Name. This is from a first-time contributor.
We have an approval, some comments, changes requested from Rafael.
**Okay… Nikola Grcevski @ Grafana / OpenTelemetry** 25:34 world.
**Mario Macias** 25:35 Okay, an additional rule, and also, should we find… Okay, do you have some comments?
But I don't see any later comment addressing your comments.
**Rafael Roquetto** 25:50 Yeah, no, so… Yeah, I haven't heard again. Maybe we should, ping him, or wait a bit? What do you guys think?
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:01 Yeah, I can wait a little bit. I mean, this is important to fix, but yeah, let's see if this goes anywhere. Somebody also picked up on a similar item, maybe you can see the next one.
**Mario Macias** 26:13 Okay, actually, actually, this has been mentioned somewhere else, okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:22 Or even if it's a new issue.
**Mario Macias** 26:23 Okay, one hour ago, Okay, this issue has been already addressed.
Okay, let's… let's… let's go later to this… To this PR… open PR. Okay, so at the moment, let's keep it as… as is.
Okay?
these… Attunkeptical Co.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:51 Yeah, these are the LLM-generated ones that we're gonna have to be, okay. Go through them.
**Mario Macias** 26:57 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 26:58 Rafael.
**Mario Macias** 26:58 This is still, yeah, it's still in draft status.
We had some comments from Raphael, from Mark.
Also, we have this in draft status from the same author.
So I guess… I guess it's similar. We have some changes requested from Rafael.
**Many, many conflicts. Okay, we can't… We have this from Mong… this… two weeks ago from Mongo. I will mark it also for… Nikola Grcevski @ Grafana / OpenTelemetry** 27:32 Clause.
**Mario Macias** 27:32 To… to… for closing it, and re-triggering, They integrate config, the two… Nikola Grcevski @ Grafana / OpenTelemetry 27:39 It's a POC, yeah.
**Mario Macias** 27:41 Tyler, yes, he's still in POC, Well, it's long, it has some… Some conflicts? Okay.
This is also from Renovate. Update Go. I don't know what is this updating, if it is updating the Go version?
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:03 What?
**Mario Macias** 28:04 Yeah, it's… Nikola Grcevski @ Grafana / OpenTelemetry 28:05 Maybe this is… this probably… Tyler's been pushing changes? Can you.
**Mario Macias** 28:10 Maybe, yes. I think he's working on this.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:14 Yeah, because it's… it's…
**Mario Macias** 28:15 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:16 Because it's exchanging the eBPF code. So, I mean, I guess Tyler's working on upgrading.
**Mario Macias** 28:21 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:22 all the gold… Versions.
**Mario Macias** 28:26 Okay, we'll see.
Introducing Weekly Flaggy Test Report. This has been approved.
by me, and Matthia.
Yeah, I think we can merge it. There are some… there were some comments from Copilot that have been addressed.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:46 Huh?
**Mario Macias** 28:47 It looked okay to me.
**Nikola Grcevski @ Grafana / OpenTelemetry** 28:49 Correct.
**Mario Macias** 28:50 Okay, let's… Nikola Grcevski @ Grafana / OpenTelemetry 28:51 Let's go.
**Mario Macias** 28:58 Okay, This is… Restaurante… yeah, this is… From this person that is contributing a lot.
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:11 Yeah, I think.
**Mario Macias** 29:13 411?
**Nikola Grcevski @ Grafana / OpenTelemetry** 29:16 So, I looked at this one. I don't know what you guys think. This was one of the security issues reported that Tyler opened up.
as… And if you look at the related issue, If you see that fix, the first in the summary fix, 2032, if you look at the issue.
It's… Saying that… when we do TTL0, it disables the expiry map.
The metrics can grow Overflow the heap.
I guess that's also possible if you have TTL of 1,000 years.
I think you can achieve the same thing. We have a time to live.
value, so… This fix is addressing the zero, so he's saying in the fix.
That he's proposing. He's saying, oh, if it's zero, Expirated right away.
I don't know, I mean, we could accept it, but I just don't know if it does anything, to be honest.
That was my comment.
**Mattia Meleleo** 30:33 Wouldn't it?
**Mario Macias** 30:34 speed.
**Mattia Meleleo** 30:34 breaking change.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:36 It would, yeah.
And… and that's my concern, because it would be a braking change, but it actually… And Dawson doesn't fix.
**Mattia Meleleo** 30:47 Anything, because users can still shoot themselves in the foot.
**Nikola Grcevski @ Grafana / OpenTelemetry** 30:53 Yeah, the default is not zero, so by default, there's no behavior, and if people And I think the doc say, if you set it to zero, you disable the expire, so… I mean… If you do.
**Mario Macias** 31:06 So this is… this is Konshu's foot gun.
**Nikola Grcevski @ Grafana / OpenTelemetry** 31:10 Yeah, so maybe the comment… maybe what we should do is change the docs to say, if you say this, if you set this to zero, expect that you're going to get a memory leak, and don't do this, essentially.
Just warn people in the docs, because if you set it to 100 years, you will also get a memory leak.
Yeah. So…
**Rafael Roquetto** 31:31 Yeah, I think that's very predictable, easy to reason about, leaving, like, not having this PR just setting to zero as they get a memory leak, because I feel like if the problem is, like, the growing map.
Then there shouldn't be… it should be fixed as, okay, add a limit to the map, and the map starts printing errors, but outside of this, you know, like, another… something that, you know.
you put the map behind an API that doesn't matter to you, despite of any configuration, overflow that map, which is a much bigger change, and I'm not proposing we do that.
**Mario Macias** 32:08 That'.
**Rafael Roquetto** 32:09 That's, I think, how, if we were to fix this, how… that's how I would personally go about it, because, you know, otherwise, where else don't we have something like this? So I think… Nikola Grcevski @ Grafana / OpenTelemetry 32:19 Yeah.
**Rafael Roquetto** 32:20 Letting zero overflow the map is a very… you know, you're doing that, it goes up well.
**You did it. So… Nikola Grcevski @ Grafana / OpenTelemetry** 32:28 Yeah, and every time you add a constant, like, 10,000 elements, or no more than that, you're gonna have to add a config option to configure it, because, sure enough, somebody's gonna hit it, and they're gonna start losing… metrics. Yeah. Yeah, I… we can actually suggest Probably, an update to the docs to say, if you set this to zero, expect that you're gonna get memory leaks.
**Mario Macias** 32:56 Okay.
**Shall I comment it here, or in the… on the… in the… Nikola Grcevski @ Grafana / OpenTelemetry** 33:02 VR, yeah, yeah.
**Mario Macias** 33:04 Okay, then… Put gun as a verb is correct.
**Nikola Grcevski @ Grafana / OpenTelemetry** 33:31 Yeah, that's good.
**Mario Macias** 33:56 Morning Oh, God.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:12 That's exactly it.
**Mario Macias** 34:14 Shall I close it, or leave by… leave it open by now?
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:20 Yeah, I mean, let's see what he says, and then…
**Mario Macias** 34:24 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 34:25 We can close on the next.
**Mario Macias** 34:28 Okay.
Yeah, so, there are… another PR, open PR, is… From Mattia… all these workflows, refactor VM integration.
**I see, a request for splitting a… Nikola Grcevski @ Grafana / OpenTelemetry** 34:51 Matthias split the commits? Okay.
**Rafael Roquetto** 34:53 Yeah. I already started looking into it this morning again.
**Mattia Meleleo** 34:57 Yeah, I started by adding some more kernel coverage, and then it took my hand, and there were some bugs in kernel 5.10.
So yeah, I… I did everything in here, and I split it by comments, so it's easier to… to review it by comment.
**Mario Macias** 35:16 Okay.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:18 Amazing. Okay. Thank you.
**Mattia Meleleo** 35:20 One thing I'm not, sure about is the… so, right now, we are pulling the kernel images from, from one catalog, from, Celium.
I'm not sure.
**Mario Macias** 35:30 We should…
**Mattia Meleleo** 35:31 to mention it somewhere for license attribution or… or something like that. It's Apache 2.0 licenses, so… It's pretty open, but I'm not sure if we should, mention it somewhere.
**Rafael Roquetto** 35:44 I can double-check, and… sorry, Nicola, yeah, go ahead.
**Nikola Grcevski @ Grafana / OpenTelemetry** 35:49 No, I mean, if we've taken the code from them, then we should definitely mention it, but if we're just using their image, I think it's fine.
**Mario Macias** 35:57 Yeah, I think…
**Mattia Meleleo** 35:58 I think it's just the images, yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:01 Yeah, that is Klein.
**Rafael Roquetto** 36:02 I gotta say, I think this is a really good change. Like, we don't have to maintain our kernels anymore, compile stuff, and now we have so much more coverage. So, yeah, thanks for doing that.
**Nikola Grcevski @ Grafana / OpenTelemetry** 36:14 Cool, alright. Do I need some reviews?
**Mattia Meleleo** 36:18 Oh, also, there is one other thing I wanted to ask. So, if we wanted to run… all of our integration suite on all these kernels, it would take a lot of time, so I added one command, which is slash all VMTests.
which is, which is basically another workflow that, that is run on demand, on, some, like, BPF… BPF-heavy.
PRs, for example.
yeah, I don't know if that's the best way to go.
Around it, or if we want to just trigger it manually from the UI.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:00 So, would that be possible to just add a label, and that triggers the workload, or…
**Mattia Meleleo** 37:05 Also, we can do it labeled, yeah. I can change it.
**Mario Macias** 37:08 If we detect… if we detect that a BPF file has changed, run them automatically, maybe, and…
**Mattia Meleleo** 37:15 I wouldn't do that, because maybe some BPF changes are trivial, and this workflow takes really a lot of time, like.
**Mario Macias** 37:24 Okay.
**Mattia Meleleo** 37:24 50 minutes, or something like that, because it has a lot of kernels, and it has to run all the tests on all the kernels.
**Mario Macias** 37:32 Okay.
**Mattia Meleleo** 37:36 So right now, it's with that command over there, which is slash all VMTests, but I can do it labeled as well.
**Mario Macias** 37:43 Yeah, we can… so anyone can add a label if they want to get the result or suspect something might be broken. Yeah, it's fine.
**Mattia Meleleo** 37:52 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 37:54 Yeah, I mean, I guess, maintainers, we can just add the label.
When we see a PR with a lot of eBPF changes, and…
**Mario Macias** 38:02 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:03 For now, and see how it goes.
Cool. Good work.
**Mario Macias** 38:08 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:14 And there's only one left, which is mine.
**Mario Macias** 38:16 Thank you.
Improving TCP and match parsing performance.
**Nikola Grcevski @ Grafana / OpenTelemetry** 38:23 Yeah, so we had a customer complain about… missing… Events.
So… So this is, essentially, this customer is running high throughput, I think.
maybe… I forget, 1,000 requests per second.
And so they provided us with the BPF logs and everything, so, I was trying to tally up what's happening, and I saw a lot of… in the BPF logs, unable to reserve, on the ring buffer.
So… That primarily hit… I think the TCP events are disproportionate compared to the HTTP events, because I think they're using multiple databases, memcache, there's, like.
So they're comparing with an earlier version, which didn't have all these protocols, I think maybe it had only SQL for their use case, and that one is producing all the events, and then.
**Mario Macias** 39:24 I serve.
**Nikola Grcevski @ Grafana / OpenTelemetry** 39:25 Realizing that by adding all these protocol parsers, it's becoming, And we've actually added a lot of overhead.
But the silliest thing is most of the overhead is actually allocation of… of errors. And Yeah, so there's a lot of changes, but and I have some comments from Rafael and Matthias, so I will address them today, hopefully. But essentially, every time we do anything such as return an error, if it's a formatted error, that's really bad, but it's also, like, returning an error New, it allocates a new object, so if you look at the before picture, Most of the time.
**Mario Macias** 40:10 Oh, huh.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:11 garbage collection.
**Mario Macias** 40:12 Wow.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:13 Absolutely.
Yeah.
**Mario Macias** 40:14 That's a very good improvement. Only forever? Oh, wow.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:20 Yeah, it's mostly errors, and I did find this one thing with the HTTP2 parser.
Because we try to, when it's garbage bites.
**Mario Macias** 40:31 I didn't know.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:31 it's maybe HTTP2, so we've missed the initial preamble of the communication, so we want to…
**Mario Macias** 40:38 True.
**Nikola Grcevski @ Grafana / OpenTelemetry** 40:38 Detective from now on, onwards.
And, what's… what's happening is that… Every time we create a new framer, that just allocates this massive array.
duplicates it.
Unfortunately, most of them are private.
But I added, some extra sanity checks for the frames.
for is HTTP2 to work around it, but other than that, most of the improvements came from Early detection that it's really not the protocol that we're parsing, and removing the error.
formatting.
So yeah, it's like 6 times faster now.
I'm hoping that actually puts a large dent. That actually dawned on me something else, is that we… we should pay close attention to these protocols, and how expensive they are.
To run. So, I'm planning on doing… Around maybe looking at How expensive is to parse meant cache if it was really man-cached?
**Mario Macias** 41:52 Yeah.
**Nikola Grcevski @ Grafana / OpenTelemetry** 41:52 One is to kind of skip over protocols you don't know, which is testing the worst-case scenario, but it's also Once you detect the protocol, how expensive it is to do.
The actual parsing, so… We should probably look into that.
**Mario Macias** 42:10 Okay.
Okay.
**Mattia Meleleo** 42:11 Just wanted to add one short thing. In the future, maybe it would… I know Rafael doesn't like this, maybe…
**Mario Macias** 42:18 Hmm, which…
**Mattia Meleleo** 42:19 defer to eBPF more.
Categorization of these protocols. Classification.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:26 Yeah, maybe. Yeah, maybe.
**Mattia Meleleo** 42:28 So we have zero overhead user space?
**Rafael Roquetto** 42:32 Yeah, no, I think that's a good idea.
**Nikola Grcevski @ Grafana / OpenTelemetry** 42:35 Now, yeah, now it's… I mean, it's obvious because we're… like, in eBPF, we're paying more attention, and it's, like, we have… we can't have loops, we can't have all this nicer space.
that we have in the Go user space, so we've been spoiled, and I just kept on adding stuff. And eventually, it just, Yeah, there's quite a bit of overhead. When I first ran it, I even… my test, I had enabled, heuristic SQL detection. That's actually really expensive.
Because the SQL heuristic, if we don't recognize this MySQL postgres of Microsoft SQL, we try to look for a SQL statement in the payload.
It's not on by default, fortunately, so it's not… It's not related, but it does. That actually is very expensive.
Yeah.
**Mattia Meleleo** 43:37 Yeah, if I'm not wrong, we loop over the whole buffer for SQL.
**Nikola Grcevski @ Grafana / OpenTelemetry** 43:41 And for each one, and I remember that, We look for each one of the commands, because we want to find the first one.
Because it could be, like, a select wrapped in an insert or something, or an update with a select, and so you want to find that it's update, not a select. But if you search first for select, you find the select, you're going to find the inner statement, and it's not great.
Yeah.
Yeah.
So, and you have to do case insensitive, because otherwise, People, right? Uppercase, lowercase.
But it's not on by default, so that one is… people turn it on, they can get slow, but we should look into it, I guess, is what I'm saying, is these protocol detectors are very performance sensitive, so we should probably spend time optimizing them.
**Michele Mancioppi** 44:33 And, this is something that we're doing so that… You can see the… Which grid is run from the client, from the server, on which side?
**Nikola Grcevski @ Grafana / OpenTelemetry** 44:44 Yeah, both, both.
Yeah.
So we collect, bits of information I mean, for some protocols, we collect a lot of information in the eBPF side, but for some protocols, we just take the TCP buffers, and then we parse them in user space.
On the… in the GO side, because that's much easier to work with.
than implementing it at, the protocol level on the eBPS side.
But… Having said that, you know, parsing Mongo brackets.
it's not trivial, so we'd rather use the Mongo library to parse them, rather than implement our own version of the Mongo… parser.
**Michele Mancioppi** 45:28 But, I mean, this is probably something that has been litigated a lot, but… You don't want to get the query in the client.
From the library?
I mean, that is what normal instrumentationers do, right?
**Nikola Grcevski @ Grafana / OpenTelemetry** 45:44 Yeah, but then you have to implement every library independently.
So, for Go, we do that.
But it's a long tail, and we constantly have to kind of implement the same things that the SDKs implement.
It's a lot of work and a lot of maintenance, and things break quite frequently. They change their stuff, so we don't want to be in that business. As much as we want, we can.
So I'd like to capture only what's required, and then like, when you think about it, Kafka and Go alone, there's, like, Go Kafka, there's the Segment I.O. Kafka, there's…
**Michele Mancioppi** 46:21 I had to support 40 different HTTP clients in Java.
**Nikola Grcevski @ Grafana / OpenTelemetry** 46:26 Exactly, right, when you think about it, right. And then… but they all speak HTTP at the end of the day, so if you can parse the protocol, you'll get them all with a single blow, right?
**Michele Mancioppi** 46:35 And in the moment you start talking about speedy and some of the really weird stuff, but let's say more… Nikola Grcevski @ Grafana / OpenTelemetry 46:41 Yeah, more or less.
Yeah, so… So we've done… we've taken that approach at… It's, But as we've added more protocol support, which was one of the goals since the beginning of this quarter, of this year, sorry.
That has also pulled pressure on here, because now there's AMQP, MQTT, there's all sorts of protocols that are being detected by OBI.
Well, before it was just SQL, maybe Kafka, and… I don't know what else? Redis.
**Michele Mancioppi** 47:11 I have seen something like this before in, Linkerd.
They are actually doing something similar.
For, proxying over… Over the side course.
So maybe there is a trick or zoo that you can look up there.
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:27 Yeah, okay, good point. Thanks.
See what else they do, maybe they.
**Mario Macias** 47:38 Boop?
**Nikola Grcevski @ Grafana / OpenTelemetry** 47:39 Face?
**Mario Macias** 47:42 Yeah, so… I think… that's… that's it.
So, any last time topic to talk about?
Otherwise… Have a nice day.
**an afternoon… Nikola Grcevski @ Grafana / OpenTelemetry** 48:05 I'll see you soon.
**Mario Macias** 48:06 So, see you soon. Bye-bye.
**Mattia Meleleo** 48:08 combined.
