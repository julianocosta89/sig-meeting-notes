SIG: Sampling SIG
Date: 2025-07-03
Duration: 51 minutes
Zoom Recording URL: https://zoom.us/rec/share/A9lkX0oIAwedJv0hevjGGAl_BLFkWFWIheW3-fwm9HBmcnPrVmDGum-5-RlKs4fu.3Jp5hV3BNEKDBRpJ
============================================================

## Zoom Recording Transcript

**jmacdonald** 02:34 Hello!
**Peter Findeisen** 02:36 Hello!
**jmacdonald** 02:39 Okay.
**Otmar Ertl (Dynatrace)** 02:40 Hello!
**jmacdonald** 02:42 I have a few things I want to talk about, and I know what one of them or 2 of them will be. Let me find the notes.
and I'll share So I think it's probably 2 things. One is the clarification for Otep, 2 50 that is already in the agenda, and we can start there.
And the second thing is we'll say random question, oh, I'm in bold.
random questions about tail sampling processor. This is going to be a fun one. I'm glad you're here, Kent Kent. So I saw the Pr. In the spec Sig specification repo yesterday. So I have a feeling what this is about, Peter, but I'd love you to to put it in your own words and tell us what we're looking at.
and I will share.
**Peter Findeisen** 03:36 So we briefly discuss this thing before, so it boils down to assumptions about about the state of of the span which we there is no t value when there is no t value.
We don't know anything about the sampling probability, but I wasn't sure whether we can assume that the spans that we see still have the randomness value distributed also, provided the sampling flag is set is on that We can say anything about the randomness value about how it is distributed, and initially it looks like we can assume that if the threshold is not set, nobody touched the randomness flag, so we sorry the random value. So we can assume that it is distributed uniformly across across the the whole spectrum of possible values. However, if we use this to make any sampling decision, and still do not record the threshold. And this is the case where we want to have this compatibility with legacy some parent samplers.
then this is no longer true.
because if we use the randomness value and compare it with a threshold to set the sampling flag. We will not report the threshold, but, of course, the randomness value which will be the associated with spans that have the sampling flag set will no longer be distributed across the whole spectrum of of possible values. So in the next phase.
I'm avoiding to use the word downstream because it it's post something else. But in descendant spans wants to make sampling decision based on parent.
and they want to change. And in combination, let's say, with rate limiting, sampling. They want to change the probability they want to decrease the sampling probability.
We don't know what the sampling probability was.
We only can provide the new sampling probability which hopefully will set the stream of sample spans to the appropriate level.
But we cannot use the randomness value anymore because it's not distributed as we assumed it would be I I know it's a very complicated explanation. I'm not sure if you followed.
But actually, I ran some tests just to make sure. And yeah, it's it is broken. If we use the randomness, original randomness, randomness, value in this combination. So we have to generate simply a new value for each case. This is a corner case, because this works only when we combine the legacy samplers with the consistent probability samplers for us. It is a corner case, but in real life I am afraid it will be quite an office encountered by our our customers, who who would.
or users of open telemetry who would not be able to set the to switch to consistent probability samplers all at once.
May I ask.
**Yuanyuan Zhao** 07:54 Some questions. Pardon me, this is a something that you already covered. Is this case?
Is this is the concern about, or the potential crash between a upstream and downstream sampler.
In that If a upstream sampler I mean the the reason we mentioned legacy is because but like in legacy. We actually don't know what happened in upstream.
So in the in the upstream sampler.
they might have already made use of the randomness value and applied the same consistent probabilistic sampling at let's say, a probability of p. 1.
And then in the downstream sampler.
We want to apply. We want to further sample right? By the probability of p. 2.
Then the data coming out of both stages.
it should have a probability of p. 1 times. P. 2. Of being sampled.
**Peter Findeisen** 09:26 No!
Well, we could.
**Yuanyuan Zhao** 09:30 Look! How do you.
**Peter Findeisen** 09:31 Not not necessarily right. So it depends on what we want. Yes, this is a possible scenario. However, this is not what I'm talking about. I'm talking about the sin scenario when there is no threshold recorded.
Therefore your p. 1 would be unknown.
**Yuanyuan Zhao** 09:49 Yeah.
**Peter Findeisen** 09:49 And it's simply impossible to to have the second stage of sampling work in such a way that it, the effective probability, will be p. 1 times, p. 2.
**Yuanyuan Zhao** 10:02 Okay, okay? And that apply. So because not knowing what upstream is doing right, whether it is using the same consistent property sampling what even ratio it used made the downstream impossible to deal with it in any way.
So the case you described is even worse than what I was trying to say the p. 1 times, p. 2. Outcome which could actually potentially be dealt with if the information was recorded, but because the information wasn't recorded. There's no way we we can deal with it.
**Peter Findeisen** 10:40 What?
So? Okay? Oh, it's the problem is only when we looked at the sampled flag. So if you have stage one of sampling again. I'm consciously not using terms upstream and downstream because we wanted it to be use in a in a different meaning.
If stage one of sampling records the threshold. We know what happened. We know exactly what the state is, if there is no threshold, but we want to, and the sampled flag is set.
Then we simply cannot use the randomness value. That's that's the thing that that my tonight change.
**jmacdonald** 11:27 Can I insert my understanding of this right now, just to make sure. The reason a simple example would be, you start with the legacy hotel sampler, which was called trace id ratio based, but was not specified. So any old algorithm will do. You presumably took the 128 bits or 64 bits of randomness from that trace Id in a random way, or sorry, not in an arbitrary way, and created a decision. And now that decision is contingent on the randomness, you don't want to use the randomness again.
we're assuming that randomness was used. If we don't see a threshold and apparent sample decision.
**Peter Findeisen** 12:04 Right.
**jmacdonald** 12:05 And therefore you're creating a new randomness.
**Peter Findeisen** 12:08 Yes.
**Yuanyuan Zhao** 12:08 Yeah.
**jmacdonald** 12:09 And it means that the child, the span that gets that new randomness.
**Peter Findeisen** 12:14 It's a it's a temporary randomness. We generate it once we do not record it anywhere. It is just used to make the with the correct probability.
**Yuanyuan Zhao** 12:26 Yeah. Cause. If we make use of that, there's a potential clash, and we have no way of knowing whether it is donna right.
**Peter Findeisen** 12:38 Right. So let's assume that we have a setup which is using parent based sampling combined with with rate limiting, sampling. I believe this will be a frequent scenario if the incoming, if the parent span has a sampled flag, but no threshold.
We still want to trim the stream of spans to satisfy the conditions imposed by this rightly meeting sampler.
We do this by suggesting a threshold, and this suggestion suggested threshold is such that it assumes that the randomness value is uniformly distributed from 0 to to to power of 56 minus one.
But if the parent somewhere made a sampling decision based on a similar setup.
The randomness value with a sample flag will not have the same distribution.
It will be only from the past threshold up to to the power of 56, minus one.
**Yuanyuan Zhao** 14:03 Yeah, because when the upstream, even though initially, was random, the stream was random, but the earlier stage already applied sampling that created the buyers that certain randomness value will survive after that. So what we are seeing there is not a statistically random distribution anymore.
right? Right?
**Peter Findeisen** 14:30 Right.
So now, the technic technicality. So I I have this pull request to make this clarification. And, by the way, of course, doing some some explanations about what we mean by certain things.
and there is some resistance from that which, frankly, I'm not sure. I understand, because we are not trying to create a new auto tip, and we are not even trying to extend the Otep. We are trying just to clarify and fix certain things.
**jmacdonald** 15:09 Yeah, I saw that I I I would like to not burden you with that topic.
let's take that particular topic offline. I'll talk to Carlos about it. And I think it's okay, especially like it's so recent. And you're not.
I. I think we should just make the change in the Otep. But but perhaps what I'm gonna propose is that we is that we clearly put a like change log at the bottom of it. I don't wanna spend the time in this meeting right now to talk about that procedural problem. But I've understood the the high level. So you're saying that we we synthesize a randomness value and then make a decision and then don't record it.
**Peter Findeisen** 15:51 Right? No? Well, we will not record it, because if we record it as a T value.
we have much higher assumptions about.
**jmacdonald** 16:01 Right. We've made.
**Peter Findeisen** 16:02 Cannot do this. Yeah, so I will. Of course, I will modify the prototype in Java to follow this new clarification or change if you will. And I'll have a pull request hopefully next week.
So yeah, I believe.
**Yuanyuan Zhao** 16:26 In this case we also cannot put in a threshold right? The threshold stays unset. It would be wrong if we put anything there.
**Peter Findeisen** 16:34 Right.
**jmacdonald** 16:40 So I get it. I think so. We can pass through the sampling. We can do the rate limiting, probabilistically speaking, but we just can't set a randomness value or change a threshold.
I like it.
**Peter Findeisen** 16:50 Yes, yes.
**jmacdonald** 16:52 Thanks for the verbal clarification. I think it really helped.
Since I well, I'd like to just respect everyone's time and move quickly. I wanted to talk about this tail sampling processor. It was sort of a like a fun idea. 2 weeks ago. I put into this channel that I was thinking about the tail sampling processor. I actually asked what next to this group, and Peter was more or less saying, I think the 1st thing a user might want would be a tail sampling processor. And we have this thing, and it's sort of lacking ownership. And it's not necessarily as structured the way we like it maybe doesn't do what refinery does, but it is existing. And so I thought I'd pick it up and take a look at it.
As you know, I also did this on the side with a coding agent. So I was talking to a coding agent for 2 weeks about this code base.
Interesting experiment. It definitely didn't quite succeed. I definitely got halfway through and like was having trouble telling which way was forward and which way was backward. It was very, very big mess. I did get something through it. I did get through it, I think. At least I have a rough draft. I don't even want to look at it. It's this Pr, here it's it's a mess. But I I reached a point of understanding what the scope of the change was going to be where the problems are going to be. etc. I kind of know the code base a little bit now.
And you, you basically are able to follow the Otep sort of structures that we have for for some of it. I got through. Put sort of putting all the Otep 2 35 decision making in based on, you know, there's already package in the Go collector code base for that that and so sort of structurally inserting the the Otep 235 stuff took a while. Then there was there's all this sort of like rule engine existing, and I tried to put those structures from Otep 250 into place there.
I eventually got to needing to implement, to to look at how it did rate limiting. Essentially, it has us a memory limiting function as well as a rate limiting function, and I tried to kind of like muddle through it a little bit, and I ended up wanting sort of framing myself a question, what do I want, really? And and this is what I was hoping to to maybe pick your brains here. If there's any secrets you don't want to give away, don't give them away, but in the end what I what I sort of sketched out for myself was.
Now, there's this, you know, this sort of pool of spans that all are gonna in the same moment of time are going to be decided. So there's a buffer. Let's say it can be a second long. During that second you're just letting the the spans build up until they become too many. Or you get to the end of your window and you're gonna tick happens. And you want to sort of flush some some traces out During this period of accumulation these spans have been arriving and placed into a trace kind of data structure. And now we're at the point of decision making. It's a configuration parameter. How long we wait. So now you've waited 30 seconds or something. You've got all the spans you're gonna get. It may not be complete. You know there could be stragglers. But and and the problem is that I mean not a problem, but one of the challenges right away is that you have this trace which has different weights on different spans, potentially. So how do I? How do I give it the trace a weight. I don't think I can, but I I kind of like faked it for a second. I'm just gonna use the 1st trace that 1st spans that arrives or the root span. I'm gonna find a problem like I'm gonna find an adjusted count for this trace. And then I did. I wanted to do some sort of rate limiting. So I did the only thing I know. And that's like, apply a weighted sampling algorithm, not a consistent sampling algorithm. Just like I've got 500 traces. I need to reduce it to 300 traces. I'm going to do some sampling and weighted, weighted, weighted sampling. I used some weight coming in computed an output weight called that a multiplier, and I put it on a different attribute, saying, for this trace, due to sampling, I selected 60% of the traces I saw. Therefore the adjusted count is the inverse of 0 point 6 or whatever.
**Kent Quirk (he/him)** 21:07 Quick question.
**jmacdonald** 21:08 Yeah.
**Kent Quirk (he/him)** 21:09 On when you talk about weight on the spans coming in, you're talking about the fact that those you're you're using the sampling probability of those spans that were head sampled by some percentage. That's what you mean by weight.
**jmacdonald** 21:26 And I'm very muddled right now. I think you can see the problems I'm getting to. I wanted to make the outputs be countable in the sense that you can make span to metrics. The incoming spans have effect adjusted counts according to all the sampling logic that we've talked about. And now I'm saying, well, I have too many traces. So I'm going to randomly select among my traces. Apply another multiplier based on my selection process.
It means that the traces come out with a tail sampling multiplier plus their original Otep 235. State whatever it was that in theory you would multiply.
**Kent Quirk (he/him)** 22:06 Yes.
**jmacdonald** 22:07 Get span counts from, and just like success. But I don't know that I'm doing it correctly, and I wondered if there were any thoughts in this room about how do you rate limit traces in a tail sampling environment?
Given that the individual spans are all different late arriving, have their own weights, and so on.
And I know, Peter, you you had some ideas. You've you've talked about it. I'm not asking you to tell me everything, but I think you were saying the idea to. Originally I thought we were going to select traces based on threshold, and I realized that that doesn't necessarily work
**Peter Findeisen** 22:44 So.
**Yuanyuan Zhao** 22:45 Oh! Oh! Oh! Why.
**Peter Findeisen** 22:47 Yeah.
**Yuanyuan Zhao** 22:47 Why doesn't it work.
**jmacdonald** 22:49 Oh, yeah, let me let me say what I was thinking. So I was thinking, Okay, well, I have a hundred traces, and they have randomness values, and I want to output 25 traces.
Do I?
This is where I couldn't figure out the math, and I didn't know what to do. So I did something different. I you know, like I can look at my 100 randomness values. I can say that. Well, the 25th value. The maximum value, I think, is here. So if I choose a threshold between these 2 points, I will have 25 traces output.
But I don't know that that makes any sense. Probabilistically speaking, there's still quite a free variable there.
and I don't know how to solve this.
Don't.
**Yuanyuan Zhao** 23:39 So I think there are 2 cases.
One is we have a conforming earlier stage samplers. So the randomness value are tagged, the threshold are tagged, although the threshold for different spans might be different.
right?
And we want to select again after this in this. Let's say, the second stage 25% of that. Your question is, how do we select it? My what I?
What I'm wondering is that so? We just can look at the current population and define the this second stage selection as randomly select among this current population right. And then this comes down to the sampling function what we use.
And in the case where we know the randomness value, we know the threshold, even though it is different, but because of the nature of consistent probabilistic sampling. That's it's it is like it is basically not longer a. p. 1 times, p. 2, but a main kind of thingy, then what we needed to apply in this case is the probability the probability existed on the span right the universe of threshold times my, the my current threshold. So if previously was selected by 50%, now, we want to have 25%. So this is like 12.5%, right.
We apply that.
So in the case of what Peter described that, we don't know the threshold value, we don't even know whether the randomness value was used or not touched. Then we simply have to use some other function, because we don't know whether that would clash. And in this case, I think certain level of clash is unavoidable, and with that, just because whatever we use in the the theoretically.
some upstream were happening to be used the same consistent sampling algorithm we ended up selecting.
But that's a limitation. I don't think there's any way we can get away with it.
You see what I mean.
**jmacdonald** 26:30 I think I do.
**Yuanyuan Zhao** 26:31 Yeah, right? We we could pick whatever new readiness value. But that probabilities is, there's a non 0 probability of clash. And we're selecting incorrectly, but in reality is that the probability, that kind of clash? We were wrong?
That happens. It's very long.
**jmacdonald** 26:54 It's.
**Peter Findeisen** 26:54 So the the solution that we had we had it implemented with the old style of consistent probability sampling, using the R and P values.
But the the behavior was basically independent on that. It was just technicality. So if you have, let's say you see that you have a set of 100 spans, and you want to arrive at the set of about 25 spans how to arrive to these values. It's a separate concern, but you need to to calculate this. Prob, this factor which you want to decrease the value volume of spans by.
And if it's 20, let's say you want to keep only 25% of what it's incoming.
Then for each span you take the threshold of this span and modify, convert it to probability, and you multiply this probability by 25% and convert it back to a threshold. And this is a new threshold that you apply for this span. If this threshold is still lower than the round the randomness value you, you keep it. If not, you discard it. That's the algorithm.
Yeah, that's what what it does it if if this, if all the spans in a trace have the same threshold, then we will not break any traces, all traces will either either be discarded or sampled if there are different threshold values within within a trace trace might get broken. But the customer are aware of that right. They know that if they configured their sampling in such a way there will be no guarantee of of completeness.
**Yuanyuan Zhao** 28:56 I don't know what.
I don't know whether I would call that broken when the are having different threshold or probability.
That's we need to clearly define what is the semantics in this second stage of sampling? Right it?
is it?
Is it like just a randomly select on the population you receive.
then applying like one span is 50% selected, the other is 80% selected. And now we want to select the 25% then applying the the, the multiplication part, the product.
50%, 25% and 80% and 25%. I think it's the same statistic of probability.
It's just the combined effect of both stages.
**Peter Findeisen** 29:53 Right? So so I I miss 1. 1 thing which is also very important with this algorithm is that it of course, preserves the sanity of span to metrics, pipelines, right? Everything is still. Cal will be calculated correctly.
**Yuanyuan Zhao** 30:12 Yep.
**Peter Findeisen** 30:14 Now, with with respect to when I when I use the term broken, I didn't mean that. It's something which is not working correctly.
It's just breaking traces. But if the customers users want to set different probability sampling thresholds for different parts of their traces for different services. For example, this is something that they expect.
**Yuanyuan Zhao** 30:48 So I would also call that, even if we don't do anything, even if we don't have the second stage of sampling. If customers are applying different probability to different parts of the same trace.
They already have broken traces.
What? We added, yeah, we are actually not.
Increase the probability of brokenness where preserving that we are preserving that. So it's not something that this second stage is introducing.
**Peter Findeisen** 31:27 Correct. Yes.
**Kent Quirk (he/him)** 31:30 So just to express like a different strategy, refinery considers it's it's making decisions on at the trace level, not at the span level.
And so it's going to preserve either all of the spans in a trace that it received, or none of them is the decision that it's making, and then, as part of its processing, it will multiply the probability of that trace having been chosen by the incoming probability level. So if you sent broken traces, you would still have broken traces. It would be broken in exactly the way it was broken the way it arrived at.
**Yuanyuan Zhao** 32:21 That's right.
**Kent Quirk (he/him)** 32:21 The sample.
**Yuanyuan Zhao** 32:22 The relative brokenness is saying.
**Kent Quirk (he/him)** 32:24 Yes, but if we don't we would not drop.
It would not selectively drop new spans from a trace that had arrived with the traces sampled. That's the difference between these things. In other words.
if you chose to sample, like all of your database spans at 10% and everything else at 50%.
It would not. Then if refineries decision is another 10% or something like that, you wouldn't get 1% of your database. You'd still get that 10% on that trace. In other words, the trace would traverse refinery intact or not, or just get dropped entirely. So that's a difference. And the cost of that is that now refinery needs to remember for each trace what its decision was. So that late arriving spans get the same decision.
That's where we refinery keeps effectively a bloom filter of dropped traces, and a, you know, actual cache of kept traces along with the sampling percentage chosen so that it can correctly attribute that data as it moves through refinery, even if it arrives late, and then that cache, of course, expires over time. And so when somebody sends us a giga trace that has a million spans, and it lasts 12 h that might fall out of the cache. But.
**jmacdonald** 33:45 The tail sampling processor has something similar, but not as developed and actually like. I can't tell how it expires. It's like 1 1 hash table.
**Kent Quirk (he/him)** 33:54 Oh, yeah.
**jmacdonald** 33:55 How's that?
**Kent Quirk (he/him)** 33:56 Binary. I had to do 2 nested hash tables that overlap that kind of that makes more sense.
**jmacdonald** 34:02 Yeah, this is not what's not as sophisticated. I think it might be fairly broken. And and it was originally storing a map of Boolean values decision values. And I was gonna change it to be a a multiplier or a threshold. So Peter.
**Kent Quirk (he/him)** 34:17 Well, so I wanted to ask you that about that real quick before you go further. Did your change compose the decisions in a way that preserves this probability because one of the problems that I had when I looked at the tail sampler like a year and a half ago, was that it was just handing to each decision process would return either a yay or na, yes or no decision which had no information about probability. Yeah.
**jmacdonald** 34:46 I I tore it apart and added that, and it made a huge change, and I would start over again if I was to to do this because based on what I learned. But so major changes are needed. And but if if I may come back to to the we've all described a little bit now but, Peter, that I what you described, might work. But I I sort of turned away from something right there, and I want to ask a question. So we've got all traces came in. There were a hundred. I want 25.
The mental model I had stated was, I'm going to look at all my randomness values, and I can see where to cut them off to get 25 traces. But I don't know how to randomly choose a value, you were saying instead, don't, don't look at the randomness values, look at the thresholds.
turn them all into probabilities, multiply them, turn them back into thresholds and then filter some out. Now, that's a probabilistic algorithm that I think what you're saying should get me 25 traces.
**Peter Findeisen** 35:47 Yes.
**jmacdonald** 35:48 If the randomness is random.
**Yuanyuan Zhao** 35:50 Yeah.
**Peter Findeisen** 35:50 Yes.
**Yuanyuan Zhao** 35:51 Well, well, that's that's what I said as well. Right the in. In that case.
**jmacdonald** 35:56 Challenging that I just hadn't thought about it.
**Yuanyuan Zhao** 35:58 Yeah. Yeah.
And then there. So with everything that's a conforming that's that's sampled by conforming sampler. We could apply this like the multiples with some legacy. Where things are not marked.
there is, it's impossible to always do it correctly, but in practice the clash would be very low. You can just choose some like random things. The mechanism would be outside of this. It would be outside of algorithm, outside of mechanism to make sure that nobody else was accidentally using a randomness value chosen this way. And the algorithm done that way right? So to avoid a a crash, so that if you just apply 25% in an unknown case.
Then you got the same result.
What I don't get was Kent said something to record the decision.
Why do we need to do that in our refinery?
Was it like not using some consistent sampling algorithm or some other? There was some other.
**Kent Quirk (he/him)** 37:25 Refinery can make non-consistent decisions because it has a rule based sampler. So what happens is depending on which sampler people are using that can be based on evaluation of the contents of the trace. And so you can say, keep all the errors and 10% of the 400 s. And you know, 1% of everything else. You can make those sorts of rules. And it can also do like dynamic sampling based on the data that's coming in so that you'll you'll be sure that you'll get like a sampling of every endpoint your system uses, even if some of them are rare. So the point is that it. It makes trace level decisions without taking into it's not. It's not making consistent decisions based on any upstream sampling. It is making trace level decisions, and then it composes the rules by basically asking the sampler, tell me what probability this this rule is effectively so. In other words, if you say sample this at 10%, then you know, it will give you back the 10% and so we can then multiply that probability.
So the sampler says, sample this at 10%. And then at the end, when we're actually making the decision, that's when we apply that probability. But that's not based on doing a consistent sample. Refinery is is not trying to be consistent. It's trying to preserve traces. That's its that's its primary goal is to either pass on an entire trace or none of it, and it cares less about statistical coherence than it does about achieving a certain rate.
**Peter Findeisen** 39:21 So, if I'm not mistaken, the difference with refinery is that it assumes that the sampling probability is recorded only in the root span. Is this correct.
**Kent Quirk (he/him)** 39:33 No actually, refinery does decorate every child span with the appropriate probability, and, in fact, it will multiply it through if the different spans have probability decorating those, as well.
**jmacdonald** 39:46 And do you see? Keep this so my question right now is, do we keep this adjustment separate like I've I put it in a an attribute because it's not Otep. 235. It's not part of the consistent sampling decision. It's just another decision. I can't. That you're saying is somehow probabilistic, and therefore there's still math we can do. If you, if you take one in 10 traces, I can, randomly speaking, I can multiply by 10, and then and then my final count would be the Otep 2, 35 accounting times the adjustment factor that was tail trace based.
And I was just thinking of that as like a simple, multiplier
**Kent Quirk (he/him)** 40:28 That's the way refinery does it. It does it as a simple multiplier.
**jmacdonald** 40:31 There again. We have that problem that we've seen in the past, which is like, if you have a stage multiple stages of sampling. And you think they're independent, but they're actually performing the same function. You end up inflating your account.
**Yuanyuan Zhao** 40:43 Esh.
**jmacdonald** 40:44 Yeah.
**Yuanyuan Zhao** 40:45 That's why you apply the the multiple, the product instead of just applying what's configured for your stage.
**jmacdonald** 40:53 So there's some warnings here. But I but nevertheless I saw Otmar not shaking his head like yes, that sounds right good.
**Otmar Ertl (Dynatrace)** 41:03 Maybe I can, also, because maybe let's go back to consistent sampling, because this is where we started from. And Peter described the way how to do the consistent sampling by just, you know, keeping the probabilities proportional right.
But I mean, this is just one way to do it consistently. It depends what you actually want to achieve in the second sampling stage. If you wanna keep the proportions. I mean, this is, of course, a valid use case, but it's also valid that you would like to try to balance out the probabilities in the second stage. So that means, here you keep spans which have gone through the 1st sampling stage. Yeah, with the lowest sampling probability, so meaning that they have a higher adjusted count. You would like to keep them with a higher probability than those which you know, were sampled with 100% probability in the 1st stage. So just to so at the end of the second stage, ideally, all the spans have the same sampling probability, even though they had a different probability.
1st stage. Of course this is not always achievable, but the second stage can at least try to do its best there, and this can also be done consistently. And we actually had that in the prototype for the 1st approach where we have to. We had the Pndr value, and where we had just propelled this of 2 I demonstrate that this, of course, would also work out for the new approach. And actually, this is exactly what what Josh described to that. You keep basically the the spans with the highest star values and and find a threshold such that the the number of remaining spans is exactly what you want.
and this is another way of consistent sampling. But this way tries to balance out the probabilities.
So it really depends. What's your goal? And there's, of course, something in between those 2 solutions.
Yeah, it really depends. What is your goal of your second sample stage.
**jmacdonald** 43:37 I I understand. There's so many goals we could have, and and all these in some way do work.
maybe help me with a little math question, then. So let's suppose I had a hundred traces, and they had a uniformly distributed randomness values.
and I have a hundred, and I want to choose 50. So, randomly speaking, probably my threshold is going to be about 50.
That's not really. That's not quite right.
**Peter Findeisen** 44:06 Okay. Okay. No. Sorry. No.
**jmacdonald** 44:08 Is it? 49, 49, and a half, or 50.
**Peter Findeisen** 44:10 The problem. The problem with the second stage sampling is that your our randomness values are not uniformly distributed anymore.
because you see only a subset of all spans that were ever created.
and the random randomness value are random only in the interval between the threshold and the Max.
**Yuanyuan Zhao** 44:36 That's right.
That's why we have to apply the product of both stages.
Probability of both stages.
That's I think that's the same thing that we covered in the previous question that
**jmacdonald** 44:57 Yeah, okay.
**Yuanyuan Zhao** 44:58 4, 5, 6, 9, right.
**jmacdonald** 45:02 Oh, yeah.
**Yuanyuan Zhao** 45:02 Yes, we can't make use of the random, so we cannot set the threshold.
**Peter Findeisen** 45:06 If there is no threshold, we cannot. Yeah.
**jmacdonald** 45:09 But but I think Otmar's algorithm was choosing from the higher end of the scale. So as long as you're only raising threshold, which we agree is logical. Then you're only reducing the raising the threshold into the area where it's random.
It didn't sound right.
**Peter Findeisen** 45:26 Well. So what I described was, we discussed this before we had this 2 different styles of behavior. One was proportional. This is what I described.
and the other is balancing, which is what Otmar described and balancing creates the similar distribution of of the sample traces as they were in the original population of traces. And there there are possible combination of of that. And I describe the principle of of our algorithm here. But it is important to understand that the user still had control over selecting groups of traces with specific conditions. For example.
often heard, I want to keep all my traces with errors. Right? So we did. We hear that our customers say that. But we actually don't allow them to to do this, because with every category we want to have rate limit. So instead, they have to say, I want to keep all my traces with errors up to 1,000 per minute.
This is a mandatory part that we enforced to save the money, of course, because what what will happen if all of their traces have errors and and protect the system from crashing as well.
**jmacdonald** 47:01 I get. I think I understand. I was just looking at the mathematics of it. I felt like, Okay, I've sorted my randomness values. I want to choose a threshold, and there's some freedom between my 25th randomness value and my 26th randomness value. There's a whole bunch of thresholds that fit in there, and any one of those thresholds gives me the right number, but they don't feel random to me or equal to me, and I don't understand how I can just make up a threshold when I have a to to choose my output count based on because there's a a gap between them somewhere in the middle of the gap, somewhere at the edge of the gap. What's going on here?
**Otmar Ertl (Dynatrace)** 47:39 Yeah, there is a there's a paper it's I think it's all called threshold sampling, and I think whether to be unbiased.
If I remember correctly. If you, for example, keep 100 spans, then you have to take the threshold of the 101st span.
Okay.
**jmacdonald** 48:01 One.
**Otmar Ertl (Dynatrace)** 48:01 Like that.
**jmacdonald** 48:02 Okay.
**Otmar Ertl (Dynatrace)** 48:03 That's actually what I was thinking.
**jmacdonald** 48:04 James.
**Otmar Ertl (Dynatrace)** 48:06 It's can you find a link to that?
Not 100. Yeah, I will look it up. But I'm not 100% sure. But I think it's like that.
But of course they assume yeah, continuous random values, I mean, could be tricky because we have this great random values for the, and it's not so unlikely that we have multiple spans with the same random value if they come from the same place. So it.
This would need some additional research, I guess. So.
**jmacdonald** 48:44 Okay. Well, we've covered the the rough topic that I wanted to, and I had. My questions have been said. So now now I'm happy.
It sounds like a number of these approaches are actually fine. They have different goals and different outcomes.
I appreciate the conversation. My goal was to get to where I could suggest reasonable things for this code base tail sampling processor which I'm sort of trying to adopt.
And I would say that I've had my questions answered And I'd like to see that paper out more because I was thinking about exactly what you just said. The plus one is that like, choose my next threshold, plus one, or whatever it would be great to see that. And I also remembered you had an algorithm that did something like that with Rnp values. So appreciate the input.
have have we reached a good place to Move on. I think that that was a useful conversation. Thank you.
I my goal with this tail sampling processor, by the way, is to take ownership. I was thinking, I'm going to reach out to the owner of the code. He's been looking for new owner, new code owners as well, so that'll be my next step, and I'll report back what I find.
**Kent Quirk (he/him)** 50:06 This is Jirazi.
**jmacdonald** 50:07 This is someone named Porter tech is. Seems to have stepped away from it, but it's the other person who has a care who has an interest here. And they come in slack and they ask for help. So so I'm gonna be giving them that help
**Kent Quirk (he/him)** 50:22 Okay.
yeah, this has been one of those things I've been wanting to do and never found time to do so.
**jmacdonald** 50:28 Well, I didn't have time either, but the agent made it. I don't know. So ken I'm gonna send you something. I might start including you on my, on my ramblings on this topic, just to kind of, you know. Have someone to approve it? So thank you all.
**Kent Quirk (he/him)** 50:41 I think I am still an approver on that particular repo.
**jmacdonald** 50:45 Excellent we'll we'll it's it's going to live. I'm I'm sure of it. Thank you all. I think we've we've done a good job. Peter, I'll go back to your your spec here, now that I understand it, and and give concrete guidance that I can, and and Carlos and I will help you.
**Peter Findeisen** 51:02 Thank you.
**jmacdonald** 51:03 Get this through.
Thank you all. I think this is it I I there's more to talk about, but I don't have anything else to say. So see you in 2 weeks.
**Kent Quirk (he/him)** 51:15 Sounds great. See you.
**jmacdonald** 51:17 Bye, cheers bye!
One.
