SIG: eBPF Instrumentation
Date: 2026-10-14
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Gregor Zeitlinger** 01:00 Hi, Tyler.
**Tyler Yahn (Splunk)** 01:04 Hey, Gregor, how's it going?
**Gregor Zeitlinger** 01:08 Good.
I saw that we also have the pull request dashboard here. That's been such a great help in Java. I love it.
**Tyler Yahn (Splunk)** 01:24 Yeah, I actually, yeah, I'm becoming more and more… it's, like, super, super helpful, like, for maintainers and just trying to figure out what you need to look at, so… We actually just added it to the Go repo yesterday, because it was so helpful.
**Gregor Zeitlinger** 01:40 Nice.
**Tyler Yahn (Splunk)** 01:41 Yeah.
Yeah, there's also, like, there's a bunch of automation that Trask is building out in that shared workflows repo. I don't know if you've been paying attention to it, but.
We also had, this, like, auto review thing?
From Codex. So. Or not Codex.
Copilot.
Where it'll, like, use the CNCF account for the Copilot reviews.
Which is pretty great, because it didn't understand that, like, like, it essentially would just keep doing a review.
Or keep asking for a review until it gets to success.
And so, it's, like, I think pretty helpful, especially for, like, newer, like, PRs from, like, newer members, but, like, it also had, like, this bug where it wouldn't, accept that it had, like, a quota reach, like, message as a success. So, like, we had, like, PRs with, like, over a thousand comments from it saying, like.
I can't… I can't do this review, but then it'd be like, okay, do another review then. So it was just pretty funny, but… Yeah, but yeah, it's also, like, they fixed that bug. It's actually pretty great, for, like, newer, users to have that kind of thing. I don't know if you have that in Java yet, but it's worth, I think, looking into.
**Gregor Zeitlinger** 03:01 I think Trask, was using his own token in Java, and he said that's why he cannot use it anywhere else.
**Tyler Yahn (Splunk)** 03:09 Oh, okay, I see.
Yeah, I, I'm not exactly sure quota-wise, but I do know that, like, it doesn't… like, that's kind of the nice thing, it's supposed to take the CNCF quotas, but yeah, like, we'll see. I don't know how many they have.
There as well.
**Gregor Zeitlinger** 03:30 Are we in the right meeting? I see that people are signing in into the document, but I don't hear anyone else.
**matt** 03:39 Yes?
you.
**Gregor Zeitlinger** 03:41 Okay, so it's me, okay.
**Tyler Yahn (Splunk)** 03:46 Yeah, they're all there. Speaking of that.
why don't we go ahead and jump in? If you guys haven't yet, looks like most of you have already added your name to the attendees list, but if you have agenda items, why don't you go ahead and add them there as well? We currently have an open agenda, so… We'll probably wait just a little bit.
But yeah.
If you had things you wanted to talk about, we can go ahead and Start in just a second.
Cool.
Alright, so… Let's go ahead and jump in here. Nimrod, it looks like you want to talk about.
Keith's peer enrichment updates?
**Nimrod Avni** 04:55 Yeah. Wait, wait, where is it? I just want to put the.
the Pr link.
Yeah, so I was in the, the collector SIG today, and talked about this. Unfortunately, I think not a lot of the… maintainers of the specific component were there, I think only, Christox, and… Basically what they said, I think they're, they're… they want me to split up this issue into kind of two issues. One is, like, the feature of the peer enrichment, and one of them is the thing that will make it work at scale, which is the kind of central component.
I think they also talked about, and I talked with some guy in the thread there about, conventions, like semantic conventions for Kubernetes peer enrichment.
That might be… I don't know if it's a prerequisite, but hope, like, probably something we should push in parallel, because I think us, we have.
I don't know if our naming even is consistent between, let's say, network metrics and all that stuff.
And… and… but I think, like, they had a few, things that they were afraid that it might be kind of too complicated and makes the processor… you know, made more complex, but I'll try to, to… give better reasons for it, and once I have the split issues, I can… send it to you guys if you wanna, you know, endorse it, and I think they told me to be in the next one, which is more US-friendly. I'm not sure what time is it here.
Hoping I can come there and and talk about it as well.
Just wanna, yeah, quick update on that.
**Tyler Yahn (Splunk)** 06:50 Cool, yeah, thanks for the update on that. That all sounds, like, really positive.
progress, so yeah, I'm excited to see how this goes. Please do send the issues when you get them. That sounds like a good idea.
Cool.
Okay, thanks. Alright, next up, Gregor, you wanted to talk about, your… this PR for adding dynamic Instrumentation configuration, if I'm not mistaken?
Gregor, I don't know if you're muted.
**Gregor Zeitlinger** 07:31 Thank you. Yeah. Didn't notice.
Yeah, so this is, the first part of a, series.
That adds the data types, and yeah, just wanted to show you how this is working.
I think this has been discussed before, but I'm not sure, so I wanted to… double-check if this needs more context, or, this is already good. I think the… The PR description already gives you a good overview of what the feature is.
**Tyler Yahn (Splunk)** 08:07 Yeah, I had just seen this right before the meeting, and I was reading through it.
Had some thoughts, but they're not really well formed yet, so I don't want to.
say too much… here, but, I mean, I… so, I definitely think this is a great feature. I definitely, yeah, I think we should move forward on this. I'm interested to hear what Mike, you have to think about this as well, but also, like.
Some of the specifics around naming, I probably want to look into, but again, like, I just haven't thought through it too much yet.
**Gregor Zeitlinger** 08:36 Yeah, I'm not asking for a rubber stamp approval, just wanted to raise awareness and get feedback on, like, the direction, so that we can discuss if this is.
There are other design alternatives that I have not considered, maybe.
**Tyler Yahn (Splunk)** 08:54 Hmm, yeah, absolutely. Yeah, I'm, actively trying to review it, so definitely wait for that, but, Mike, I don't know if you've also seen this?
**Mike Dame (Odigos)** 09:02 Yeah, I've been looking at it. The Custom Instrumentation is kind of an interesting thing for me, because it is one of our… the way that we do it is our enterprise stuff, and some of our paid features, so I do… like, both ways, I want to be careful about, I don't want to influence too much.
into the open source approach, and I also have to kind of be careful about what, you know.
approaches that I… I talk about, but I will give a look into the PR, and try to comment what I can.
**Gregor Zeitlinger** 09:35 Thanks.
**Tyler Yahn (Splunk)** 09:39 Cool.
**Nimrod Avni** 09:40 So this, like, I just wanna… This is like, I think, what Nicola talked about previously with like, it's specifically for Java, I guess, but maybe we can extend it.
Okay, that's cool. Interesting. Yeah, I also have a look at that in some of the.
I think I know probably, I know, Matteo, you, you did, I think something similar-ish. I don't know how the.
**matt** 10:07 Yeah, I think, I think we discussed this with, with Nicola offline. I think it's the… refactoring of the old PLC.
**Nimrod Avni** 10:19 Okay.
**Gregor Zeitlinger** 10:19 Yep, that's correct.
**matt** 10:22 Nice. I will have a look.
**Nimrod Avni** 10:25 I… I think… I think I talked to, Mattia about it, private, but maybe… I don't know if it's a… Probably definitely not like prerequisite to this, but maybe something to think in the future of like.
this kind of configuration is probably something that people want to update live, or update a lot. It's not like…
**matt** 10:49 you.
**Nimrod Avni** 10:50 Yeah, basically, either Opamp support or some other way of, I think you talked about, like, OB operator, like, making those, like, CRDs or something, but… But Opamp is really cool, and then we need to think how it coordinates with… if we're in the collector, and the collector supports Opamp, then how do we do this, like… they need to signal us. I don't know, I'm not super familiar with that protocol, but… It can be, especially with the config V2, which is… kind of more structured and separated so we can, like, hard reload specific components and not restart the whole pipeline?
That sounds something really cool for, you know, OB1 point something.
**matt** 11:39 Yeah, I think I mentioned this in chat to Nicola. I don't know if.
If, if Nicola told you something about, Opamp, Gregor?
**Gregor Zeitlinger** 11:50 I know what OpAmp is, yeah, but I don't know the discussion about OpAmp, regarding this particular issue.
**Nimrod Avni** 12:01 Yeah, I think we can, you know, we can continue with that. It's not like a prerequisite, but I think it'll make it, like, really strong, like, to make those changes, like, dynamically.
You know, just saying, like, okay, I want to monitor this function now, and without needing a full, like, restart or something.
We will go.
**Gregor Zeitlinger** 12:21 That is definitely the idea, yes.
**Nimrod Avni** 12:25 Cool.
Thanks.
**Tyler Yahn (Splunk)** 12:31 Cool.
Yeah, so if folks want to take a look at that, that sounds good.
Otherwise… That's the end of the written agenda. I guess I can ask, if anybody's had a chance to take a look at the 1.0 RC, that was out last week. I know Nicola said that they're already running that, or, like, Grafana folks are already running that, in production, but… Yeah, I didn't know, if other folks have had a moment to take a look.
Still planning on trying to get it out, the 1.0 next week, so, yeah, I just wanted to ask.
Well, okay.
**Mario Macias** 13:14 From the… yeah, sorry, from the Grafana side, we are, we have been struggling in incorporating it into Vela, just for some breaking changes. We… we are just fixing it, so we will… We will test it in in some dev environments during this week.
**Tyler Yahn (Splunk)** 13:37 Okay. Yeah, that sounds good. And so when you say the breaking changes, do you mean like main or do you mean like the tag?
**Mario Macias** 13:42 No, sorry, Yasi, in the library.
When running vendor mode.
We… for example, yesterday I added a feature that was internal, so it was not visible from Baylor, so I had to rewire a few stuff, but nothing that breaks at the level of functionality or configuration.
**Tyler Yahn (Splunk)** 14:11 Okay.
Yeah, I saw… I saw that PR to move that cloud package, public, this morning. So, yeah, like, it sounds like there's still some shuffling needed for code access, but otherwise.
Yeah, yeah, that sounds good. I mean, obviously, it's… Good, good feedback to have, have that, fixed, but yeah.
Cool, alright, well, yeah, please, please let me know how it goes, if there's any, like, big blockers. Otherwise, I'll try to get the PR out, next week before the meeting, and I think it's next Tuesday, is the two-week period, so we'll try to get it out around then, yeah.
Cool. Any other topics folks had?
I guess we have a pretty full house outside of Nicola, Are folks able to make it to KubeCon North America this year?
**Rafael Roquetto** 15:06 I'll be there.
**Tyler Yahn (Splunk)** 15:08 Awesome.
Yeah, you're giving a nice talk, right?
**Rafael Roquetto** 15:11 Yeah, it's supposed to, we'll see how it goes.
**Tyler Yahn (Splunk)** 15:15 Mike's gonna be there.
**Mike Dame (Odigos)** 15:17 Dry runs yesterday of our talks, me and Rafael, so we're… Doing band practice, I call it.
**Rafael Roquetto** 15:25 We gotta practice, yeah.
Who else is gonna be there?
**Tyler Yahn (Splunk)** 15:30 Nicola's gonna be there, I'm gonna be there. Looks like Steven just raised his hand.
I don't see… Yeah, but yeah, so I think it's just us.
I don't know if, Folks also were able to submit the KubeCon EU.
The CFP for the Observability Day, I think, is still open. I think it closes next Sunday, so if you missed the deadline for, the main track, KubeCon, there's still time to get your talks in for Observability Day, if I'm not mistaken. Yeah, it's correct.
**Roy Reshef (Kubex)** 16:12 It's coming Sunday.
**Tyler Yahn (Splunk)** 16:14 Thanks.
Perfect.
So, yeah, the more talks we can get about OB, the better. So, that'd be great.
Well, cool. If there's no other topics… We can end the meeting here.
It's good seeing you all, thanks for the short meeting. We will, I guess, get back to reviewing PRs, yeah.
Okay, everyone, I'll see you in a week's time.
**Nimrod Avni** 16:40 I guess.
