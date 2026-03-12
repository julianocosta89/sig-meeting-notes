SIG: .NET Auto-Instr SIG
Date: 2026-03-04
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 28:35 Hi, Geist.
Sorry for being late.
**Yevhenii Solomchenko** 28:43 Oh.
**Piotr Kiełkowicz** 29:15 Well, I think we can start.
Pretty light, even.
Any other topics except the open-end PRs and… issues?
No.
Can you hear me?
**Igor Kiselev** 29:46 Gospital?
**Piotr Kiełkowicz** 29:48 Right.
So, pull request, hmm… We have, I think, 3 or 4 important PRs.
Two of them are related to no-code. It was already reviewed by Chris, and I'm looking for final review from… Igor, thank you very much for detailed review so far.
Mmm…
**Chris Ventura** 30:29 I, I do have one question about, those PRs. So we're using a domain-specific language based on cell, but how strictly are we wanting to adhere to the cell definition.
**Piotr Kiełkowicz** 30:49 I think pretty strong. It is pretty solid implementation after the review.
**Chris Ventura** 30:57 Okay.
**Piotr Kiełkowicz** 31:00 I think it will be better to be strict there, at least.
From… at the beginning, if there will be kind of negative feedback from the end users, we can kind of… Make some improvements.
**Chris Ventura** 31:14 Okay. Do we have any feeling for how often that, standard changes?
**Igor Kiselev** 31:23 I have, looks like the… the language definitions have not changed in the last 3 years, at least. Okay.
So I could double-check it, but… but I looked into it last time, and the Go repository for anti-alura specification, it was several years.
Bye.
**Chris Ventura** 31:46 Okay. Yeah, since it's not changing frequently, then, I don't think we need anything in place to try to keep us up to date with it.
**Igor Kiselev** 31:56 We can just handle it on an ad hoc basis.
So, with my review, I tried to make sure that we are strictly subset of cells, so yeah, we definitely do not support everything that Cell supports, but we should not allow anything that Cell is not supported, in case if any other language agent would also like to use the same Language, so we would have the same… syntax.
**Chris Ventura** 32:25 Yeah, thanks for looking into that.
**Piotr Kiełkowicz** 32:29 So, pistol… I forgot, to be honest, to review notes related to this. I will try to make… merge it tomorrow.
And Alexi kind of… There's also solid, progress here.
I've requested, kind of, extract some part of to separate PRs, but as we discussed internally in Cisco, it happens in kind of a couple days.
from.
**Alexey Pukhov** 33:03 Sure, yeah, I'll definitely go through those, through your suggestion to do a stack changes. There are some stacks, available. I mean, even though GitHub doesn't support it, but we can still do it manually.
**Piotr Kiełkowicz** 33:17 Please, you have asked me in private channel about this fix. I suppose I find, though, I will have to fix it right now, but I will be sure when the build's finished.
there were a missing built ex… Staff, and it can be installed in this way.
kind of… there is a Docker Gita passion for such functionalities.
**Chris Ventura** 33:48 That's much easier than I thought.
**Piotr Kiełkowicz** 33:52 And just switching to buildings.
But, It is kind of… not fully tested, the CI in progress.
So, the thinking, folks.
Issues.
So, I have 3 follow-up tickets for no code. I think we can skip it this week and back to this topic when… Existing PRs will be merged.
And I'm opening others.
Rash, there is a question to you about… Spnet host Core Hosting.
environmental variable.
**Rajkumar Rangaraj** 35:10 Yeah, I'll, that's something we need to address now, or should I take it off the coupled by?
**Piotr Kiełkowicz** 35:16 I think you can take offline.
**Rajkumar Rangaraj** 35:20 Yeah.
**Piotr Kiełkowicz** 35:39 I think this is the topic discussed Last week?
Or two weeks ago, I don't recall, actually.
And… there is a proposal how to handle it. I think we can still postpone it after the current PR is merged.
So, you can just, review it offline.
MongoDB finally merged native support for OpenTelemetry. It is not released yet.
I think we can put it… For the next release, I mean 1.15, if it will be not available, we can always push to another milestone.
It is not very strict implementation of OpenTelemetry semantic conventions, but it is close enough to include it into our… Distribution.
Chris?
**Chris Ventura** 37:06 I haven't had a chance to, to write up the proposal.
But I'm hoping to get to it this week.
**Igor Kiselev** 37:13 It's a follow-up of what we discussed in the previous week while we looked on Alexi Exchange, so I said that I would create a separate ticket to discuss Right now, it's even not a proposal, it just states what we currently have and what option we have, so we just need to confirm that.
What we have today is what we would like, or if we like, changes in the future.
**Piotr Kiełkowicz** 37:41 Discussions… Tropical bones.
No discussions.
Nice, not typing with the wrong thing.
Not to decide.
**Igor Kiselev** 37:58 Actually, what we just look into my question records versions, it's probably better to be moved to discussions.
Because it's not a bug.
I don't know if.
**Piotr Kiełkowicz** 38:14 We can, but we are… discussions are kind of for external questions, not the… Okay. It's kind of rarely used, to be honest.
**Igor Kiselev** 38:23 Okay.
**Piotr Kiełkowicz** 38:30 I'm not sure if we have… Anything to update you?
This one is in progress.
Oop.
**Chris Ventura** 39:01 So, Igor has been contributing a lot to a lot of the tickets and reviewing many of the PRs, and I want to nominate him to become an approver for our SIG.
**Piotr Kiełkowicz** 39:18 I can support it. Thank you, Chris.
**Igor Kiselev** 39:22 Thank you a lot, Chris and Petra.
**Chris Ventura** 39:28 And Igor, I'll follow up with you once I remember what the process is.
**Igor Kiselev** 39:32 Okay, Sencha.
**Chris Ventura** 39:55 Okay, heck, that's all I have.
See y'all later.
**Piotr Kiełkowicz** 39:58 Thank you all. Have a nice week.
**Alexey Pukhov** 40:01 Thanks, everyone.
