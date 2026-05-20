SIG: CI/CD SemConv SIG
Date: 2026-05-19
Duration: 23 minutes
============================================================

## Zoom Recording Transcript

**Alan Clucas** 05:15 Hi, Al.
**Pellared** 05:18 Hello, Alan, how are you?
**Alan Clucas** 05:19 I'm alright, how are you?
**Pellared** 05:22 It's fine.
**Alan Clucas** 05:23 Good.
**Pellared** 05:25 Are you outside?
**Alan Clucas** 05:27 No, no, it's kind of light, it's very light. It's… that's the back of.
**Pellared** 05:32 Dad.
**Alan Clucas** 05:33 And there's, like, a lean-to on the back of the house that's.
**Pellared** 05:38 Awesome, that's a very nice setup.
**Alan Clucas** 05:41 Yeah, I can see the garden just there, so… Thanks for putting in all the legwork on those, talks.
**Pellared** 05:57 Yeah, thank you as well.
Do you want me to add you to the attendees list?
**Alan Clucas** 06:47 Sorry?
**Pellared** 06:48 Do you want me to add you to the attendees list?
**Alan Clucas** 06:52 Oh, yes, please, if you're there. Yeah, thank you. Yeah, you sound good.
I wasn't sure I was going to make it today.
Had a customer saying they needed me on a call, and then… and then they've changed it for… Two hours' time, which I can't make, so… Haven't told them that yet.
**Pellared** 07:16 I think that also, I don't know how many people joined, I saw only Carlos has… has… written that he'll be late, like, 5 minutes?
**Alan Clucas** 07:26 Wow.
**Pellared** 07:29 And Adriel, and Christoph, Are not joining.
**Alan Clucas** 07:37 I don't have anything to report, anyway.
We give up.
**Pellared** 13:43 After Carlos, is he able to join or not?
Give me a sec.
**Alan Clucas** 13:46 Yeah.
**Pellared** 14:31 I have sent him a private message, I think we can just wait, you know, 3 or 5 minutes, and drop.
**Alan Clucas** 14:37 Yeah.
It's fine.
**Pellared** 14:42 Oh, Carlos is… 20… Hello, hello!
**Carlos Alberto Cortez** 15:01 Hey, hey!
**Alan Clucas** 15:02 Yeah.
**Pellared** 15:04 How are you?
**Carlos Alberto Cortez** 15:06 Good, good. Sorry for joining late. It was… Doing some local stuff here, yeah.
So I'm guessing we didn't get Adriel?
**Alan Clucas** 15:20 No, I trailed No, no cost of… Good.
**Carlos Alberto Cortez** 15:28 By the way, since I have you here, I can probably mention that I opened a spec PR. Oh, by the way, I saw your PR, Robert, I need to review it.
I saw that only yesterday, There's a…
**Pellared** 15:45 Right.
**Carlos Alberto Cortez** 15:49 But yeah, this is, let me put it that, in the agenda here.
But it's, for… it's based on the… what you mentioned some weeks ago, and finally had time last week to work on the prototype around, because I was… I was having a prototype, but it was very incomplete, for reasons. Let me put, here we are.
Perfect.
So, there's a PR I just put there in the agenda.
This is for adding these new operations to spam processor. There will be 3 of them.
And I went with your… with your path that you suggest, Robert, that having them as separate methods Rather than having a single one, they could be reporting the different changes.
The important part, I guess, the important things to mention there is that, besides being three metals, the first one is that, We will be passing readable spans, which means that we cannot modify a span there.
And I think that's good, because, you know, otherwise we don't want to have, like, you know, recursive things, especially if we don't need to.
And this could be more… mostly for reporting, you know, externally what's happening with the span, rather than actually mutating the span itself. So readable span for the way, in this way… sorry, in this, in this case. The second one is that we will not be reporting these events, in case cardinality… Or general limits are impacting, you know, are, sorry, are preventing links from being added, or attributes from being set.
attributes being updated, still discover, for example, but other than that, you will not get the events. So that means that you will be getting events only for stuff that actually will be appearing in the final span, you know?
And that's it, yes. I will probably work on the prototype, on the previous one.
Yes.
**Pellared** 17:49 I just have… One question.
I… probably there was something, it's obvious for me. I'm just thinking on why we do have… Span context on add link.
And we do not have span context in other methods, and either why it is needed for on add link.
Out of the links, man.
Yep. Okay.
I see.
**Carlos Alberto Cortez** 18:33 Yeah, besides that, I will be also probably working on the previous prototype, which was the one with a single method, just for Jack to see how it could look.
But I think that this is… this way is what's something you could prefer as a good maintainer, correct?
**Pellared** 18:49 I agree.
I think regard… I think it may be good, as others may ask, you know, the same question, why it's not a separate method. I don't know if you can capture my feedback that I added to you, and just add it to the PR description, or somewhere.
Because I imagine that JavaScript folks will ask for it, maybe Python folks as well, because, yeah.
and maybe if they'll be unhappy with this decision, maybe there should be some… we can consider adding some note in the specification that represent, you know, implement it as a one method, and some, I don't know, billing or different payloads.
maybe also specification compliant, if the… I don't know TC, other TC members think this is a good decision.
**Carlos Alberto Cortez** 20:01 Yeah.
Although, for me, it would be kind of weird to say, like, Because, you know, yeah.
**Pellared** 20:08 Then you look at our languages, and each of them is different.
**Carlos Alberto Cortez** 20:12 Yeah, also, I can imagine now, from now on, that people would start taking this as a way to Have a very relaxed specification in the bad side, in the bad sense.
I don't know. Anyway, they're… yeah.
Okay, yeah, let's just close that. But honestly.
It's only three methods, and they are very simple, so I couldn't expect big problems, honestly. I know that having one instead of three is simpler.
But at the same time, I don't think… if we have, like, for example, 8 methods instead of 3, probably, yes, you know, that's something to… You know, to consider. Especially, for example, if events… if spun events hadn't been, deprecated.
It's like, okay, you have 4, but now it's like, we don't even have to worry about that.
**Pellared** 21:03 I think you can also call out in the PR why it's not added to the… why we are not adding for the events. I think some readers may forget that it's been… it's… the plan is to deprecate this.
**Carlos Alberto Cortez** 21:16 Yeah, we can do that, just in case, just to be on the safe side.
**Pellared** 21:20 So, long story short, I think the PR is good. I think that's just making it easier for others, you know, to review.
**Carlos Alberto Cortez** 21:28 Yeah, yeah, yeah. And just in case, I will probably, I was planning to wrap these things up, these prototype that Jack wanted, but I was busy reviewing other stuff that was in my queue, that have been in my queue, but yeah, I will do that, just in case. But hopefully we make progress on this one, yeah.
Okay, that's all from my side for 2AM.
**Pellared** 21:59 Yeah, my questions were probably mostly to others. I was just thinking about, you know, stabilizing the carriers, what we need, and I just thought, you know, I have this one PR, which I added, because I think adding some information for the implementations, which are not obvious, is a good call out.
Based on other reviews, and I thought also about working… adding this informative variable carrier, maybe to Node.js and Rust, because a lot of modern tools are using these technologies. I don't think it's box stabilization, but I think it will be useful And yeah, that's my plan for the following weeks.
**Carlos Alberto Cortez** 22:38 Yeah, that could be nice. And it could be nice that, yeah, we try to stabilize stuff. I do have the impression that sometimes it has happened… That different languages have prototypes, but then people forget that this is not stable yet.
And somebody needs to come and, you know, try to drive this.
And just say, hey, we have an opportunity…
**Pellared** 23:00 Is that an impression?
**Carlos Alberto Cortez** 23:04 You are, you are, yes.
**Pellared** 23:08 Yeah, that's also why I decided, you know, to just, kind of.
Try to manage it, and be the one who tries to drive it end-to-end.
**Carlos Alberto Cortez** 23:19 Yeah.
Sweet.
**Pellared** 23:23 Still the first time.
Okay, then I think we can end here.
**Carlos Alberto Cortez** 23:31 Perfect. Yeah, thank you so much for the help, and talk to you flying. Or later today, actually.
**Pellared** 23:35 Thank you.
Yes!
So…
**Alan Clucas** 23:39 I…
