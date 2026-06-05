SIG: Sampling SIG
Date: 2026-06-04
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Chris Marchbanks** 05:07 Hello?
**Otmar Ertl (Dynatrace)** 05:15 What?
**Yuanyuan Zhao** 06:21 No, how are you guys doing?
**Peter Findeisen** 06:24 Aye.
**Chris Marchbanks** 06:26 Hello?
**Otmar Ertl (Dynatrace)** 06:48 Josh just wrote that he can't make this meeting.
**Chris Marchbanks** 06:57 Alright.
I guess we can get started then.
First on the list was just Probability Sampler, where all does it exist? So Java Go is almost there.
**Yuanyuan Zhao** 07:39 Yeah, it has gathered… The required number of approvals.
So, but I can… I don't have the rights to merge. I don't think Josh has either. I pinned those guys to merge, and then, Robert. You guys probably know him, Robert.
Payac, P-A-J-A-K, I don't know how to say his last name. He made some comments, and he's, I follow up with him separately, he's on, he's out of the office, so… I don't know whether someone else is gonna merge it before he comes back in, or… We'll have to wait for him. Okay. Basically, a bunch of, like, a waiting game.
**Chris Marchbanks** 08:28 Okay, sounds good. Yeah, I'm planning to, regardless of if it gets merged or not, I'm hoping to experiment with the Go version in the next couple weeks on some workloads here, so…
**Yuanyuan Zhao** 08:38 That metrics, Connector has been ready for a long time.
I'm actually eager to have people try that out, to see how, it works. Hopefully, We… I hope we did a good job there.
It's an interesting little piece of work.
**Chris Marchbanks** 09:00 Cool.
I guess what other… so it's also in Java, what other languages are we most interested in having it in? I don't know.
Question I have.
**Yuanyuan Zhao** 09:16 What are the typical languages that, right. Anecdotals might…
**Peter Findeisen** 09:22 I remember Josh was saying that he's trying to involve some of his colleagues to do something for C-sharp.
But I'm not sure how it went.
**Chris Marchbanks** 09:35 Okay.
Okay.
Yeah, it says, I think he wrote in the notes, it was requested.
**Yuanyuan Zhao** 09:46 Had there been past interest in Python?
**Chris Marchbanks** 09:57 Probably there? I mean, I would imagine once it's there, there would be interest.
Okay.
And then, yeah.
The other, I guess, agenda item I have is I've been starting on a… I have a very early draft PR open, but working on tail sampling Respecting trace state and tail sampling processor, so both propagating it along.
And, making decisions based on the trace state, rather than, right now, we do the FN… the hash of the trace ID.
So, I'll mark that as ready for review soon, and… would love some opinions on the initial steps. It's behind a feature gate to begin with, because there's still some unknowns there, for sure.
Huh.
Anyone else have agenda items or things that they are working on?
Lecture.
**Yuanyuan Zhao** 11:33 Out of curiosity, in the tail sampling processor, are you planning, like, use cases that potentially may change trace state?
**Chris Marchbanks** 11:45 potentially changing the threshold, similar to, like, probability samplers. Effectively, it's… probability and rate limit sample… and rate limiting, those would be the only things that would change the trace state. Otherwise, it should generally just pass it through. There's a little bit of a question mark of, like.
The tail sampling processor, in some modes, has a buffer that, when it's full, will start dropping traces.
We might have to do something in that case as well, as it's effectively a rate limit.
**Yuanyuan Zhao** 12:16 How much is… yeah.
**Chris Marchbanks** 12:17 I'm gonna start by ignoring that, and there's also a mode that you can block.
And just go, well, it's correct for blocking, and we'll see where we go.
Otherwise, it's just a lot of changes up front.
**Yuanyuan Zhao** 12:33 And there's, this multi-stage sampling nature.
Mmm, right?
**Chris Marchbanks** 12:40 Yeah.
**Yuanyuan Zhao** 12:41 sampling, because you already got sampled.
**Chris Marchbanks** 12:44 Yeah, and that… and that should work by, like, as long as you're… like, if you've gotten to the tail sampling, like, you'll have some threshold value, and… As long as we keep propagating that along.
Hopefully it'll work well.
**Yuanyuan Zhao** 13:00 Are we going to propagate both? Are we going to propagate the… like… Some cumulative number, like a product of those, or…
**Chris Marchbanks** 13:13 It should…
**Yuanyuan Zhao** 13:14 The inverse of the… Product of the sampling.
Probability.
**Chris Marchbanks** 13:20 It's just the computed new threshold, right? Unless somebody… correct me if I'm wrong there, but I believe that's how it works.
Similar to what probability does today, or probabilistic does today.
Okay, I don't think we need two numbers.
**Yuanyuan Zhao** 13:45 Awww.
**Chris Marchbanks** 13:46 Like, we just kind of… like, if something was rejected more…
**Yuanyuan Zhao** 13:52 Yeah, like, if the SDK samples 10%.
And then, the tail sampler.
Decides to sample.
Another 10%.
But if it's based on trace ID, then it's consistent, or if one sample's.
**Chris Marchbanks** 14:16 present the other.
**Yuanyuan Zhao** 14:16 it's 5%, if its trace ID is consistent sampling, then it's actually the minimum of both, but if it's orthogonal attributes is the product, there is a little bit of, like, complexity there.
**Chris Marchbanks** 14:30 Yes, yes. I was going to only do it for, effectively… I think that's… no, it's like equalizing mode in the probabilistic sample. I was only going to support equalizing mode to begin with. So if trace state's not there, we're just not going to… do anything.
We'll just… like, there's just not really any… yeah, we can't really do anything. And then if trace date, and then if it's there, we'll do effectively the equalizing, so we'll take the minimum.
And I believe that is correct, but yeah.
Definitely let me know if that's… if my understanding of that is wrong.
But yeah, I was trying to be a little bit opinionated so we don't end up with a bunch of different scenarios in tail sampling process error, because then it becomes especially complicated when it's like, oh yes, I had multiple policies match at different… levels.
Well, what else?
**Yuanyuan Zhao** 15:59 Do we know anyone… Make use of the SPAM metrics connector.
Because Java has been there.
Peter wrote Java, right?
**Peter Findeisen** 16:11 Yes.
**Yuanyuan Zhao** 16:12 So, theoretically, if they use Java, if they use the spam matrix connector, This ends your end. Pass.
**Peter Findeisen** 16:24 Yeah, I don't have any experience with that part.
**Chris Marchbanks** 16:43 Guess not.
**Yuanyuan Zhao** 17:15 More topics, or I'll eat them.
Going once… Going twice.
Company?
**Chris Marchbanks** 17:31 Well… Good to see all of you, have a great day.
**Yuanyuan Zhao** 17:35 Thank you.
**Peter Findeisen** 17:35 Thank you, bye.
**Yuanyuan Zhao** 17:36 Bye, guys.
