SIG: Go SIG
Date: 2025-09-25
Duration: 17 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 00:20 Hey, Brian.
**Bryan Boreham** 00:21 Hello there.
**Tyler Yahn** 00:23 How's it going?
**Bryan Boreham** 00:26 Yeah, pretty good. You?
**Tyler Yahn** 00:29 Yeah, good as well. Just another… another busy day. You're going to KubeCon, right?
**Bryan Boreham** 00:36 No, not a…
**Tyler Yahn** 00:38 Oh.
**Bryan Boreham** 00:39 Not in the US.
**Tyler Yahn** 00:41 Oh, okay, yeah, fair enough.
Are you gonna be, at the EU one next year, then?
**Bryan Boreham** 00:46 Probably. I… I just realized I… I forgot to sign up for the program committee.
Sorry.
I'll have to think of a talk, or… Pay for a ticket.
**Tyler Yahn** 01:02 Yeah, still thinking of the talks myself, actually, to sip it there. There's… there's probably a few, but…
**Bryan Boreham** 01:09 Yeah, where is it at? It's in Amsterdam?
**Tyler Yahn** 01:12 Right, next year? Yeah. Yeah. Where are you based out of? Are you… you're in England, right?
Yeah, he said London, that's right, yeah.
Yeah.
**Bryan Boreham** 01:22 I did actually think of one talk, which is entitled, parsing protobuf.
At gigabytes per second.
And other fantasies.
**Tyler Yahn** 01:39 Yeah, I think that's a great talk. I would love to watch that talk.
**Bryan Boreham** 01:44 The title is a… is a riff on, parsing JSON gigabytes per second.
Which is a real talk, and something that really happened.
**Tyler Yahn** 01:58 That's kind of impressive. I… Jason? I thought the whole point of Protobuf was to get rid of that idea that you could… .
**Bryan Boreham** 02:06 It's complicated.
**Tyler Yahn** 02:07 So…
**Bryan Boreham** 02:09 I guess that's why there can be a talk.
**Tyler Yahn** 02:12 Yeah, alright, that's what I'm saying, right? Like, I'm already… I'm already subscribed to this talk.
Well, cool. Alright, we can jump in here just a little bit, just getting myself set up. If you haven't yet, please go ahead and add your name to the attendees list.
If you have agenda items you want to talk about, go ahead and add them there as well. And, Yeah, we can… we can jump in here. So, to start us off, I just wanted to just double check and make sure everyone's aware there was a certificate issue for go.opentelemetry.io this morning, or this evening, depending on where you're at, and so the… Something got messed up with, the certificate issuing that we used for this website. So it was down for a little while. It's been remediated, so if you're on this call and you're still having issues, please open another issue, or… ask in Slack or something like that, so it should, should all work at this point.
There's still gonna be, I think, a post-mortem coming up, to really kind of identify not only the root cause, but the, just, you know, the whole situation. So, stay tuned for that. Otherwise, I don't think there's too much to add at this point, other than, I guess, sorry about that. We'll try to… Make sure it doesn't happen again in the post-mortem.
Okay, cool.
Next up, I wanted to do just another check-in on our milestone. There's quite a lot in progress, so, just wanted to… pull this up, maybe just go down the list. So, first up is, why does cardality limit ad performance overhead to metric measurements? This is something that Robert Hewitt opened. It's still, is something that was looking for an assignee Hmm.
So, looks like we actually just need to do some benchmarking, maybe to see if this has been addressed.
**David Ashpole (dashpole)** 04:14 Yeah, I think that's… You can assign this to me.
It hopefully will be 20 minutes, otherwise maybe I'll unassign myself and remove it from the milestone.
Yeah, perfectly fine.
**Tyler Yahn** 04:26 Yeah, okay, cool. That sounds good.
Next up, we saw this PR for exposed temporality selector functions. This is still something that I don't think has had any follow-up.
Since last week? Yeah.
Yeah, this is one of those things where the default temporality select… or temporality aggregation functions weren't exposed, but then there was an additional thing that's being added here with this temporality select, which is essentially a string to Replace those functions, which was something that we had concerns about.
There hasn't been any action on here, I don't know… I guess there's just nothing to do, other than maybe we'll move it out of the milestone eventually, but, yeah, I think we'll just wait on this one.
Also in here is optimized locking for metric aggregation. This is still a work in progress from David. I don't know if you need to say anything, but we can wait until that's, resolved. There's a bunch of other things related to that.
**David Ashpole (dashpole)** 05:28 Nope, yeah, I just, I think there's one more PR out related to testing.
Before I can actually start.
making the locking improvements themselves. I did, for what it's worth, reach out to Josh McDonald, because he maintains the light step.
Version of this?
And he thought my approach was reasonably good.
**Tyler Yahn** 05:50 He still maintains the light set version of this?
**David Ashpole (dashpole)** 05:53 I don't know if he does anymore. He wrote it, right?
**Tyler Yahn** 05:55 Oh, oh, oh, okay.
**David Ashpole (dashpole)** 05:58 No, no, no, sorry, you may know more.
**Tyler Yahn** 06:01 Well, he switched jobs, he works for Microsoft, last year, so I was a little, like, yeah. Okay.
I was impressed, yeah.
**David Ashpole (dashpole)** 06:08 Yeah.
Once a maintainer, always a maintainer, you know?
**Tyler Yahn** 06:12 That's also true. What, what PR is blocking the… the… this… there's, like, a testing PR you said?
**David Ashpole (dashpole)** 06:18 You've already approved it, it's add concurrent safe tests for metric aggregation. It's about 3 quarters of the way down the page.
**Tyler Yahn** 06:24 Oh, okay, yeah, that's correct. Alright. Yeah, that's a good point. So this is just looking for more reviews at this point. Robert, you've taken a look before, I think the things have been resolved. It was something to do with, yeah, collector, if I'm not mistaken. So, yeah, this is just looking for, more reviews at this point.
**David Ashpole (dashpole)** 06:40 I had a major moment of panic, because I thought time.now was returning Times that were not in order.
**Tyler Yahn** 06:52 It can do that.
**David Ashpole (dashpole)** 06:54 It can't do that.
Yeah. In theory.
in theory, the test I wrote could fail. We'll see if it happens. But the root cause was actually not that. It was that, I was just running the test in a way that wasn't correct.
**Tyler Yahn** 07:11 Okay.
If that does happen, 125… I don't know about 124, but 125 has a way to, like, manipulate the actual time package in the testing framework, but… I guess we can cross that bridge when we get there.
**David Ashpole (dashpole)** 07:27 True, true.
**Tyler Yahn** 07:28 Yeah.
Okay, cool, moving on. Next up is the exporter Prometheus Migrate to New Configuration Options.
**David Ashpole (dashpole)** 07:39 It's still on my list to do. I haven't…
**Tyler Yahn** 07:41 Oh, okay.
**David Ashpole (dashpole)** 07:42 Does this need a Help Wanted tag, or are you looking to try to address this? No, it's like… it's like one line change.
**Tyler Yahn** 07:50 Oh, okay. This is just the default thing, okay, yeah, alright. Cool.
Okay, next, is the improved error handling. This is something that had a PR, I think this is one of those ones that had a draft.
Yeah, I don't know what happened here. I think this looked pretty close, and then I think the author has fallen off.
I'm over.
**David Ashpole (dashpole)** 08:17 Okay, removing it from the milestone.
**Owen Williams (he/she)** 08:20 You've…
**David Ashpole (dashpole)** 08:21 Happy to ping, or we can ping the author on the PR, but I don't think it should block our release.
**Tyler Yahn** 08:28 Yeah, okay.
Yeah, we're not, I think, looking to release anytime soon, but, yeah. I would think this is… this is close enough where I think somebody else could also pick it up as well, but, yeah.
Okay.
Next up, high mutix contention in the metric sums. This is, I think, also something you're actively working on, so… don't know… yeah, this is already assigned to you. Okay.
So I don't know if there's much more to say here.
**David Ashpole (dashpole)** 08:57 Nope, other than I am fixing it, yeah.
**Tyler Yahn** 09:00 Cool. Awesome.
Next up is the observability packages. So, we have all of the observability packages that have, PRs open for them.
Yes, I think this is it. Let's see… I don't think there's anything much more to add other than I think some of these are still just being… reworked. We don't have the release coming up anytime soon, but I think maybe we need to talk about, well, okay, I don't know if we need to… we already talked about it, like, this isn't critical to have in this release, so if these are blocking the release, then I don't think there's… any reason to not move these out of the release.
I guess I can say I'm still actively working on this one, this is the only one I can actually speak to.
I think I've seen movement on a few of these other ones… not this, not this… I think this one. There's definitely movement. I saw this morning, I was just reviewing this, so… I think this is still being actively worked on.
I definitely have not seen anything here.
And then, yeah, this is just a PR. So, yeah, okay, we can keep our eyes on this one. I don't think there's too much to say there.
Okay, and then the last thing is just a PR for optimizing, the return times in the Prometheus exporter. If you're right… if you're working on observability, metrics, this is worth taking a look at. This is something that was already merged for the, standard.trace exporter, so… Yeah, this is, I think, just waiting for, 23 minutes, to meet the time requirement. Otherwise, yeah, cool.
The only other thing is the contribib milestone, which I think has just one issue, up to two issues now. One is the remove the deprecated, inject, and extract. This just needs to get, done.
I got a thumbs up, but I don't know if this is being worked on. So, okay.
We'll have to maybe reassign this, I think, actually.
And then… Sam opened, cannot record error for spans when producing deuce… Momantic conventions.
April 22nd. I don't know why this is not in here.
I added this last week. Oh yeah, this is something that Sam had talked about last week.
If I'm not mistaken, Sam went on vacation, though. I don't know why we added this… Okay, I guess this just needs somebody to actually work on it. It isn't actually assigned to Sam, so this is looking for somebody to jump in here.
Robert, I saw you comment on this. Is there more context that you have?
**Robert Pająk** 12:17 Directly? Sure.
more context, I'm not sure if everything is clear with the semantical version. Right. I think that some agree that my interpretation of the semantic version is clear. I also double-checked with Nudomewa.
But I'm not sure if there's not something also that should also be clarified in somatic convergence. I do not remember the details, because, as you can see, it was August.
**Tyler Yahn** 12:45 Yeah, yeah, gotcha.
**Robert Pająk** 12:48 But it might also need some other work than all.
Or maybe it's nice, or maybe at least it's nice to have. It's not a stable instrumentation, but yeah.
**Tyler Yahn** 12:59 Right. Okay.
Looks like there was an attempt here, but… Okay, yeah, I guess it's just work that needs to find a home and, somebody to contribute to it.
Okay, that is the end of the written agenda. I'm gonna stop sharing my screen here, and ask if anybody else has topics they wanted to discuss.
**Robert Pająk** 13:25 Churches.
**Tyler Yahn** 13:31 Also, any cool projects, or any not-cool projects, that you're working on, that I think are related to this?
Well, okay. If not, then I think we've got a good check-in. So, yeah, I appreciate everyone joining, we can end the meeting early here. Thank you all for joining, appreciate the time and the effort, and I will, see you all next week, or asynchronously.
Bye.
