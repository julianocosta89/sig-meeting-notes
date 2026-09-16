SIG: CI/CD SemConv SIG
Date: 2026-09-15
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:28 Good day.
**Christophe Kamphaus** 00:30 Hello?
How are you doing?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:34 Okay, how are you?
**Christophe Kamphaus** 00:36 one.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:39 Good.
Just wanted to say thank you, for holding down the floor as much as you have been lately and I really liked.
Taking the lead.
Know a lot of things. I really appreciate that.
**Christophe Kamphaus** 01:21 Sure, no problem.
I've also gotten more involved in the main semantic conventions.
That's a new exciting project for conformance.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:36 Cool. Like, conformance to SemConf?
**Christophe Kamphaus** 01:38 Yeah,
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:40 Sweet.
**Christophe Kamphaus** 01:40 It's mainly Trask and Ludmilla.
Who were developing that.
So say, now we test.
different instrumentations against the semantic conventions and see which attributes are published with Weaver live check. And it's really exciting.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 02:03 Awesome.
**Christophe Kamphaus** 02:17 Yeah, hi Robert, and thank you very much for the blog post.
**Robert Pająk (Splunk Inc.)** 02:21 Christophe, thanks a lot for your reviews. They were really good.
Thank you. It's hard to read what you're doing yourself, even if your AI is even assisting you, it's still hard to read the same thing a few times.
Yeah, but your comments were very good.
**Christophe Kamphaus** 02:42 Happy to help.
Yeah, from my side, I'm preparing the… prototypes for VCS band conventions.
I still need to test them a bit, so I have some almost ready, and I think I will comment on the PR this evening.
So hopefully we can get that, boom.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:19 Awesome.
**Robert Pająk (Splunk Inc.)** 03:20 From my side, I will be just starting to work on a talk which I will have with Alan.
like in Observability Summit at Prague. So this will be my main focus for upcoming days.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 03:37 Cool.
From my side, I'm going on vacation this week, so… After this, I'm gonna go prep the camper and check out… I'm already checked out, it's really funny, because mentally, my brain is… Fried.
So when I get back, though, I am going to, one, add the ability to send OTLP to the internal infrastructure.
Because right now, it's just the GitHub receiver, which is just a webhook, so I'm gonna add an OTLP endpoint.
And then I'm gonna open a pull request to instrument the dashboard workflow.
Which is mostly Python, which is a perfect candidate to, one, use the SDK for ENV context, and then two, actually take the deterministic IDs that the GitHub receiver generates and pull them in through ENV context propagation.
That's what I'm gonna work on next week.
Which I actually should have time to do, from work.
So…
**Christophe Kamphaus** 04:42 Yeah, nice.
And happy holidays!
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:53 Thank you.
That's all I got. Is there anything we need to talk about, or bring up, or… Any thoughts there?
**Robert Pająk (Splunk Inc.)** 05:14 Carlos spoke about you. Are you alive?
**Carlos Alberto Cortez** 05:17 I'm live, sorry, I was planning for the last two weeks to work again on resurrecting the PR for the Span processor extension, but I have been busy with, Daytime job stuff. I hope to… wrap that up so I can actually spend some cycles, you know? We are trying to, at Dash Zero, to help a lot. I'll tell… As much as we can, but there have been some unexpected things, I need to help here. But yeah, hopefully I can finally, finally, finally start working on that again.
**Robert Pająk (Splunk Inc.)** 05:54 Out of curiosity, because we are within a small group, any one of you is joining the Observability Summit in Europe, which is going to be in Prague?
**Carlos Alberto Cortez** 06:02 That's a good question, yeah, I, I… there's a chance I will be there, yeah. I already asked my boss, so, let's see what happens, but yeah, I think that it would be nice to be there.
**Robert Pająk (Splunk Inc.)** 06:15 If I recall correctly, you like Prague, right?
**Carlos Alberto Cortez** 06:20 Sorry, say that again.
**Robert Pająk (Splunk Inc.)** 06:21 Do I recall correctly that you like, that you, you, you often sometimes visit the Czech Republic or not, not at all, or my mistake?
**Carlos Alberto Cortez** 06:29 Yeah, I'm there most of the time.
**Robert Pająk (Splunk Inc.)** 06:31 Yeah. What?
What about you, Christophe? You don't, you, you're also quite near, I guess.
**Christophe Kamphaus** 06:38 Yeah, I still need to think about it. I'm not sure.
I would like to.
**Robert Pająk (Splunk Inc.)** 06:48 Alan will be there as well.
It motivates you or not. Not sure.
**Christophe Kamphaus** 06:56 Yes, there was one topic I wanted to bring up.
Since we moved the meetings now to the Zoom managed under the Linux Foundation, the old recordings will Be deleted at the end of the year.
I think… I don't use them from my site anymore, it's just if I missed one or two, and I just watch those.
If you don't have any particular ones that you say we really should keep.
I think then it's fine with us to just, Let them be deleted, otherwise we need to save some. Ourselves manually.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:40 Cool, thanks for the call-out. I don't have, any objections with them being deleted as is. Well, if everyone else is good with it.
**Christophe Kamphaus** 07:52 Cool, since there's no action to be taken from us, so… Nice work.
Whiteson.
Nice to have seen you all.
**Robert Pająk (Splunk Inc.)** 08:12 Do as well.
**Christophe Kamphaus** 08:14 See you next time.
**Carlos Alberto Cortez** 08:15 Yep.
**Christophe Kamphaus** 08:16 Bye-bye.
