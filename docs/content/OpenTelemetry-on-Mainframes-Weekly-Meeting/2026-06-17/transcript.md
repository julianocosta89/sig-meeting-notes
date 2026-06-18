SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-06-17
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 01:42 Hey, Craig.
**Greg Shriver** 01:43 Hey, Rudica, how are you?
**Ruediger Schulze (IBM)** 01:45 Good, good. So…
**Greg Shriver** 01:48 Looks like we're really good. We've got, we've got a repo, and man…
**Ruediger Schulze (IBM)** 01:53 Yeah, so I think it's really now time to accelerate.
Not sure if somebody else will join. Jim, will be… And… I… I think it would be out for a couple of… Days or weeks.
From what I heard, so he may not be joining today.
God.
I think Antoine is also on vacation.
Based on what he's sent.
**Greg Shriver** 02:24 Yeah, he's out for, what, 2 weeks, he said.
**Ruediger Schulze (IBM)** 02:26 Yeah, right.
Hi there! .
**Greg Shriver** 02:33 Hello.
**Ruediger Schulze (IBM)** 02:34 I think we haven't seen you yet here, so maybe if you want to briefly introduce yourself, can also say…
**Robert Pająk aka pellared (Splunk)** 02:42 Yeah, sure.
**Ruediger Schulze (IBM)** 02:42 also.
**Robert Pająk aka pellared (Splunk)** 02:44 So, hello, I just wanted to add my name because I, formatted my computer, like, literally on Friday, and I see that my, my, my name is not here. So, my name is Robert Payung, I'm from Splunk, so I'm working with Antoine.
**Ruediger Schulze (IBM)** 02:59 Okay.
**Robert Pająk aka pellared (Splunk)** 03:00 Okay.
Why… Quickly, I will tell you why I am here. So, there are a few reasons.
First of all, I'm working at the OpenTermatry and maintain open specification. I'm also working a lot on the blocks signal in the semantic conventions. I'm also meeting of open theoretically go.
And I know that, mainframes are pretty important for our customers.
I'm in Splunk, and I just thought that maybe I'll be helpful here, and I also had some experience with, with IS400 and a little bit of mainframes back in the studies.
But it's… it was mostly, mostly it was education, not a real… a lot of practical experience, but yeah, I know that AS, like, 40% database, etc.
**Ruediger Schulze (IBM)** 03:57 Okay, Robert, thanks for introducing yourself. So, obviously, you have here a presentation from, from Broadcom, Greg, from, from BMC, Richard.
and myself from IBM, so… Welcome to the SIG. So, we just said, right, so things are progressing, but also it's really that we need now to establish our process about the federated semantic conventions for the mainframe. That's something that I wanted to discuss today. So the repo, and thanks to Antoine, the repo can be available just last week. Things have been a little bit busy. I said I was at things up further from there. Things have been a little bit busy this week, but I will start to focus on this now to get the actions in place that, if you have been following semantic conventions, obviously GenAI, they have been the first to put the federated there, so there's a good example to get this on ours.
And, then… that's what I wanted also to discuss, as we are now kind of like, you know, have our own domain. I think, you know.
once we have these PRs there, as a Craig, Richard, or maybe also Robert, please review them, and then we need to approve them, and we need to essentially get to… get these PRs being, you know, processed through So, the regular mechanisms.
And, you know, as we have certain things already in place which we want to put forward, I'm actually thinking to start with what the, spans for subsystems can be. There are certain implementations there. I think, in the meantime, every vendor has somehow a representation, so let's maybe get from their resource definition or entity definitions, making sure that this works, and then, aligning on what needs to be, you know, span attributes and so on. And, then that could be the first thing. And we discussed previously also about metrics, don't want to go there right now, but… I think the obvious thing is maybe to start with… with these spans, as they are being around already for a while.
And, yeah, I think that's kind of, like, the first thing. And, I think, as maintainers, Antoine also configured you, Greg, so… And, Then I think there's also Morgan and Antoine himself, I believe. But, yeah, we would, you know, then need to go through the review cycle.
Right. And I think that would be the main topic for today, so what might be not a long meeting today, but that's actually where things need to move.
forward with, and that's the.
**Robert Pająk aka pellared (Splunk)** 06:50 Are there…
**Ruediger Schulze (IBM)** 06:51 steps.
**Robert Pająk aka pellared (Splunk)** 06:51 Are there any existing issues regarding this plan semantic ventures that you're mentioning? Are there any… is there any pure art that I can find?
**Ruediger Schulze (IBM)** 06:59 We had a… it's a long-running PR that we had a few… And this is… let me just get this to you.
put it in… I will put it into the, into the meeting notes, there is this PR for the transaction processing system.
And, that actually… we… We said we want to have a generic one.
Boyd, that's not the one.
**Greg Shriver** 07:35 Hey, Rudica, I think… is that 1898?
I think it's listed as, under the open PRs at the top of the…
**Ruediger Schulze (IBM)** 07:44 you're…
**Greg Shriver** 07:44 The meeting notes.
**Ruediger Schulze (IBM)** 07:46 your…
**Greg Shriver** 07:46 Some of that needs to be updated now, because some of that stuff is old now that we have an actual.
**Ruediger Schulze (IBM)** 07:52 Yeah, but if you look at that one, the… Yeah, right here it is the 1898.
If you look at this one… Opening it, also my subs.
So what we did there is, we defined… initially, I think we had a broader scope for this one, to define, really, what needs to go from a spend perspective. In there, we reduced the scope at some point.
And, but on the mainframe, you have transaction processing systems, like KIGS, like IMS, And the idea was to have a common alignment of these attributes across those. Also, eventually, from a community point of view, considering other transaction processing systems, so… I think Oracle has, you know, based on Java, certain implementations.
But, you know, for various reasons, it never really got into a state that it's being approved, and that it made it… Through the whole cycle, from a semantic conventions point of view, And, I think what we need to discuss is then also how to bring it in here, but making it a CUS-specific representation.
And eventually, we would be deprecating what we have been defining for COS and the main semantic conventional repository. There's not much, but a few… definitions are there, like, you know, COS as an operating system. There's a mainframe namespace being defined. I think we would move this all over, over time to… To be part of this.
repo here.
**Greg Shriver** 09:45 We're really good. Do we have a… do we have a link to the GenAI repo that's kind of like the fledgling…
**Ruediger Schulze (IBM)** 09:52 Yeah, I can post… yeah, let me post this to the… to the document.
**Greg Shriver** 10:02 Because that'll be helpful for us, I think, to at least look what they're doing.
Because we'll be following, sort of, similar… I would suspect we'll be following similar… Conventions and processes.
**Ruediger Schulze (IBM)** 10:14 Especially about the processes that we get this right, because they…
**Robert Pająk aka pellared (Splunk)** 10:20 I put the hyperlink in the agenda underneath.
**Ruediger Schulze (IBM)** 10:23 Oh, you have it already at home. Oh, thank you. Okay, great.
Very good. And if you… if you go in there in this… Okay, there's a lot of… This probably will take a little bit of time, but the… you know, there is a lot of actions being, you know, defined and… Obviously, we would be interested in those who perform you know, things like build, Probably need to go through this. I think I was looking at what is on the GenAI repo, just… kind of like… I think I had a better understanding what is on the semantic conventions one, but in the end, we need to have these checks and builds being implemented on our repo to make sure, you know, we… we have Vivo as the open telemetry tool, you know, using the scripts that are… they're being invoked, and so on.
I would take a look at this, I have a little bit more time towards the end of the week for these type of things, and try to put kind of, like, a minimal PR with all these things in there.
testers in my private repo, and then we can… You know, we can go through the review cycle.
Okay, so this is one thing. Anything about that? I have one more question, actually, that I wanted to discuss.
**Robert Pająk aka pellared (Splunk)** 11:59 I have a question.
Do you think that it would be helpful if you create issues, even, like, one sentence long, with the things that we want to do, even, you know, replicating Genet, I think? Because sometimes, you know, I think some things may go concurrently by other people.
Yeah. But, it sometimes also makes easier, you know, to distribute the work, even for yourself. I don't say that we need to do very long description of the issues, but I think that having some kind of portion of, you know.
**Ruediger Schulze (IBM)** 12:33 That's… that's a very good proposal, right?
Yeah.
And just created the first one.
just providing, so I'm not sharing my screen, but just technical.
Quickly erode the first issue.
This is set up with JitHub Actions following the example of the GenAI semantic conventions people.
So, yeah.
Progressive.
**Greg Shriver** 13:25 And you did that in the semantic conventions, retail?
**Ruediger Schulze (IBM)** 13:29 Mainframe repo, yeah, so…
**Greg Shriver** 13:32 Okay, I don't see it yet. I see a dependency dashboard issue. Oh, no, wait, I do see close.
Okay, now I see it. It's there now.
**Ruediger Schulze (IBM)** 13:40 So, okay, so… That, of course, is, is there.
And then, yeah.
Yeah, let's have this done first, and then we can… figures, then, you know, as we progress, I think we want to lay out the other things.
And… I'm just going back… Actually, Greg, I wanted to take the chance, maybe, to also get back to the documentation.
Entry that we have been working on.
Especially you had been working on, and I think I saw you a couple of comments, but… Maybe let's get this also being processed further. This was the doc PR.
**Greg Shriver** 14:38 Yeah.
**Ruediger Schulze (IBM)** 14:38 I am.
**Greg Shriver** 14:39 It's the doc PR, it's up, yeah, it's up there.
Yeah.
**Ruediger Schulze (IBM)** 14:47 Because I think it, you know, we can update this again and say, no, now we're actually working on our own semantic convention, so it's a good coincidence to… To get this document in.
**Greg Shriver** 14:59 Right.
Oh, I agree.
I agree. I still need to mess around with those code spaces, and that's just… that's my own personal issue.
**Ruediger Schulze (IBM)** 15:15 And I still want to get you a couple of updates in there, and… Then there's also the other section on… I'm gonna quickly finalize that.
Little reference to this.
**Greg Shriver** 15:39 That makes sense.
**Ruediger Schulze (IBM)** 15:47 Good.
Yeah.
AM.
I mean, the other issue that we can open on the repo, maybe just doing this… This is Stan.
Take over the mainframe.
I mean, specific definitions.
Wrong… some outdated conventions.
And… They're pretty good.
ones.
Over there.
Over there. Hold on.
sure if this is clear or good English, but I think… what I mean by this is… We actually want to also create a… put a request to deprecate the other ones.
If the… You know, have them defined in our equal here.
I think we just had CUS and mainframe being, defined over there.
And then another new issue is, grades and definitions.
Let's see our system software.
And that probably raises a question if we come to… to messaging. So, how we discussed messaging.
So probably we want to do this separately.
transaction processing, or maybe for the COS transaction processing systems, but then also for messaging.
And, databases, and then that might actually, relate to… to other definitions. I mean, in the messaging space, obviously, certain things exist.
Dang, also, spend definitions.
Cool.
databases for… Good, so this gives us a set of issues we can actually start working on.
So there are no… Whoop.
36, yeah, one, yeah.
6… 6 open issues.
Good.
I think there's nothing else that I would… want to discuss today. Is there, is there any topics, Richard, you have been quiet, anything you want to bring up?
Okay.
Good. Yeah, so Robert, the next steps, obviously, you know, as we described, getting the semantic conventions repo progressed, and then… Getting… getting things done.
And maybe, Craig, feel free to reach out. We can also somehow work on this document together offline, and… I'll hop on a call just to get things done.
**Greg Shriver** 20:24 Which one on the dark PR?
**Ruediger Schulze (IBM)** 20:26 Yeah.
Let's… let's also try to… to solve this. It's a good… good timing.
**Greg Shriver** 20:33 Yeah, I agree.
**Ruediger Schulze (IBM)** 20:36 Okay, then, if there's nothing else, let's meet next week, and then let's look at the first PRs next week.
**Greg Shriver** 20:47 Sounds good.
**Ruediger Schulze (IBM)** 20:49 Okay, thank you.
**Richard Nikula** 20:50 Joki.
**Ruediger Schulze (IBM)** 20:51 Okay, bye.
**Greg Shriver** 20:52 Thank you.
**Robert Pająk aka pellared (Splunk)** 20:52 It was nice to meet you. See you guys. Yeah, thank you.
**Ruediger Schulze (IBM)** 20:55 Terrible. Bye.
**Greg Shriver** 20:56 Thank you.
