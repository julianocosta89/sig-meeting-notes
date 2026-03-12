SIG: Sampling SIG
Date: 2025-08-14
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/i_v8TpU3SC_i3wohf181iiFdt-WmKefWHHqK0t-epCmRsikP3FnMA3G8spdTMsWa.10mwbyLYw7wD_iYH
============================================================

## Zoom Recording Transcript

**jmacdonald** 00:45 Good morning.
**Peter Findeisen** 00:47 Morning!
**jmacdonald** 00:48 Oh, good, you hear me. That's even better.
I was….
**Otmar Ertl (Dynatrace)** 00:53 Hello.
**jmacdonald** 00:54 A quick thing in the agenda that I have, it's not very much, but I'm glad to see you all. … … let's see… This is, just a procedural one I put in there. There's… there's… we're talk of this… of this, and… and… And, … 3 weeks ago, we said we'd do something, hasn't happened, I don't… So we could talk about this one more time.
Tristan wrote something. I'm gonna read it right now.
This is about the same topic above. This is about how does one migrate samplers, which is a topic I've tried to avoid.
… I think he… so the question is about how do you migrate samplers? One answer is use head sampling, and then your head atomically switches from old to new, I think is what he's roughly saying.
… And that… I believe works when there's only head sampling.
… I… don't really want to dig into this topic right now. If anyone wants to object to that, and wants to talk about this topic, let's talk about this topic.
I see no objections.
**Peter Findeisen** 02:42 My understanding of this comment is, the question is whether the new sampler, the one which replaces the old one.
Will… Set the trace state already, as prescribed by consistent probability samplers.
Or it would just standardize the sampling algorithm.
**jmacdonald** 03:05 I see.
Okay, so you're saying that there's an approach here, which Tristan just said, is that we can migrate samplers by looking at the presence of a trace state entry that we didn't have before.
**Peter Findeisen** 03:24 Oh… No… No, that's….
**jmacdonald** 03:55 … I… okay, I'm rolling… I'm scrolling back up to what I wrote.
I think… I was… I was… there was an implicit assumption here that you're not… that this is a general-purpose approach that we're looking for, that works when you're doing something independent, maybe, or… … Oh, I… so… I don't intend… I don't think we should take a whole lot of time on this. I think one of the past points that I was referring to when I brought half of this memory out here is when you're doing sampling, intermediate sampling, and you have collectors performing some sort of reduction in span traffic.
Those collectors are going to have some sort of sampling configuration, which, if you… if you roll it out in the middle of a trace collection, some of your traces are going to come through with the old… with… with sampling decisions made by You can't update all your collectors atomically, so you're going to have old collectors running with old sampling policies, and new collectors running with new sampling policies, and it's this rollout of new collectors with new policies that stands to break a trace if it's collecting spans that were sampled upstream.
I think is what I was getting to. Does that sound like a reasonable problem statement?
**Peter Findeisen** 05:25 Well, it's sure, but my impression was that this is… phrase ID ratio-based sampler is basically, used as a head sampler, not intermediate sampler.
**jmacdonald** 05:38 Right.
**Peter Findeisen** 05:39 And in my mind, there were two issues with trace ID ratio-based. One was that the algorithm was not specified precisely enough to ensure that different implementations for different platforms would do the same thing. Second thing is that It did not record the sampling probability in the trace state.
We fixed both issues with consistent probability samplers.
But now, when we recommend Deprecating the old one, the question remains whether the replacement will fix both issues, or just one of them.
**jmacdonald** 06:31 And do you… sorry, do you believe that we fixed both of them?
**Peter Findeisen** 06:35 In consistent probability sampling, yes.
**jmacdonald** 06:39 Okay, and so the… So, I'm coming back to my former thinking, which is that the scenario I gave with the collector collecting is not one we're trying to solve for. The scenario that Tristan refers to is… viable, I said we should… we are only interested in the migration story for head sampling. Then I think what happened was a user said, you know, someone in the community said something like, yeah, but what if a user is using non-head sampling, so they've got one of those old legacy trace ID ratio samplers as a child sampler.
And… … And they want, somehow, a strategy to update their samplers that doesn't break something.
… And… I don't want to belabor this anymore. I think there's… … This is a terrible corner case. … Would it be possible for somebody to, … I think this might get back to what Tristan was suggesting. Could I solve the problem I just hypothesized by having a sampler that will be my child sampler, it will be making a sampling decision, either if the new consistent head sampler… the new consistent probability sampler says to sample, or the old trace-80 ratio sampler decides to sample. And I think Tristan is saying that you could potentially do that by looking for trace state. If there's trace date, do the new thing.
If there's not, do the old thing. But… I can only imagine the problems I just created.
And I… and I haven't thought this through.
**Peter Findeisen** 08:35 Oh, God.
**jmacdonald** 08:38 I also don't think it's very important, but it was… it was the… the memory I have is what… that was what was being asked.
… And if there are no more comments, what I will do is offer to follow up on this with at least 5 more minutes of thinking about it before I answer, Tristan, so that the next time I read what I wrote, I can understand myself.
I hope that's good enough. I won't… I won't make you all stare at this any longer. Hi, Carlos, I noticed you joined us since the last moment we were speaking. Welcome. That was the… the… the topic that we, promised to the spec SIG.
what I plan to do, … So… I… I will… … I guess I'm thinking about the next time I speak about this topic in front of the Spec SIG, which could be next Tuesday, I will… Potentially do that.
… there might be even a chance to line up one more topic. I thought I'd mention this, it's following last week's … topic, two weeks ago's topic, and there is something I'd like to probe the audience here for, in this case.
the, tail sampler is still something I'm very interested in. I haven't moved much on it in the last two weeks, but I, as I mentioned in, say, a two-week-ago SpecSIG meeting, there's this problem I've been studying of rate limiting.
My hypothesis is that rate limiters come in many different flavors, but they share a lot of common structure.
And we see, at least two kinds of families of approach for that common structure. One of them is one I'm calling the Envoy approach, and that's where… it's like the terminology and the structures are very detailed, and I don't want to try and summarize it, but it's a particular approach to, Putting the configuration into… routes, and then filter descriptors that have various conditions, and then, like, processing. And then the other approach that I'm aware of now is the tail sampling, which is a little bit more of a tree-based hierarchical representation, and I… I believe they're equivalent at some level. You can, like, translate between… back and forth between them.
And in that sense, … My hypothesis is that there will emerge a standard for, configuring predicates that are sort of conditional and composable, filters, which are drop rules and expressions for dropping.
… decision-making about, dimensionality. So, like, one tenant gets a different rate limit than the other, and so on. So these are all the functions that you put into this, the general side. And then the specific side of this implementation is, am I… am I sampling? Am I filtering out?
Am I, am I blocking?
applying back pressure, and that sort of thing. So those are the, like, the specific behaviors that one configures with this complex tree-based predicate, essentially.
So as I'm looking at that, I'm still trying to… find a rate-limiting algorithm. That's… one thing we've talked about, in the case of the tail sampling processor, I was trying to go, to envision, essentially a fixed state buffer, like a reservoir sampling, essentially, where you have your, you know, your short window of traces that are going to end in a specific time range.
among those traces, you could get more than you anticipated. You could apply some… … some… The number of matching spans could have, like, greatly exceeded your memory budget, and you might have to compress the memory down by sub… by sampling.
to make the effect of a reservoir. So now I'm… I've got, like, a thousand spans, I have… 1,500 have arrived, I'm gonna sample them back down to 1,000, or something along those lines.
And I think I see how to make a basic rate limiter.
from that type of design, having taken all the input from you here. The, piece of it that I wanted to throw out and see if there's any thoughts on, it's gonna take me just a minute to find it, but while I find it.
… let me describe it. So… … There's something of a desire for proportionality, It's a composable sampling rule that has clauses with weights on them.
So, let me find… that, just briefly, so I can show you the configuration, although… hmm… Nothing's easy to read in this case. … So we're here… and I'm looking at config. There's something… and the name is terrible, it's called Composite.
Like, we don't have enough of those. There's a rate-limiting and a composite policy.
These are all the… the sort of node types in this tree… tree-oriented sampler here. And, so… … It's a little hard to follow, but here's the action statement. Composite config holds configurable settings to create a composite sampling policy evaluator. So, it has a total budget, like, this is my rate limiter. I'm trying to get 1,000 spans per second out of this rule.
It has a policy order.
And then… I don't know what the orderer does exactly.
Not sure that we need to replace this exactly.
And then it has, rate allocations and sub-policies. The idea being that you can say, I have these rules, I want 50% to go to this rule, I want 25% to go to that rule, and I want the final 25% to go to the third rule. I can probably find some sort of example in the documentation.
That, that discovers this as well.
So, here's the documentation. … this… a little feature has been kind of rumbling around in my head, and I don't know… I just described earlier that I have an idea about how to do rate-based reservoir sampling, which is to say, allow a buffer to grow and then shrink it whenever I need to using consistent sampling.
by raising thresholds. … this… rule here I haven't thought about. Does anybody have thoughts before I go any further?
you might say, well, this is just a rate-limited thing. Like, if I have $1,000 and 50% goes to the first rule, well, then I just give 500 to the first rule and call it a day.
my… I think I understand this as a more of an opportunistic thing. Well, if you only get this one particular family, well, maybe it's gonna get… it's 100%, so it gets 100%. … Meaning to say that this will give me a thousand spans, and it will try to gauge those ratios somehow, but if there's none of one of the policies, it doesn't count for anything, and so then I guess I could give more to the other rules? I don't know. I just kind of wanted to know if anyone has a feeling here.
**Peter Findeisen** 16:57 Well, my thinking… My thinking is biased by what… what I did for… For sampling in, in, in my company.
But… So… the… with… With rate-limited sampling.
In general, I would like to think about two stages, and we implemented this in two stages.
One… one… the first stage basically talks about the intent. So, we… … it's shaping the stream of spans. We want to have certain proportions, for example, more errors. We want to keep errors around more than the other traces.
Without any consideration for rate limiting?
And rate limiting kicks in, really, as the second stage.
… So… It's similar to what you showed, because Because this composite… rules.
It's really shaping the stream of spends, but… I would like to… make… Rate limiting as second stage, because mixing those two together in one in one step can be really tricky and difficult. I'm not sure if I expressed myself clearly.
**jmacdonald** 18:41 That matches my intuition as well. The rough explanation I gave for a rate-limiting a reservoir sampler earlier was apply the logic of… to shape the spans on the way into the reservoir, if you will, and then only when you run out of space, go apply the rate limit.
And if you don't run out of space, that means apply the rate limit at the end of the interval when you know exactly what you want to do.
… So… … So, in some sense, maybe there's a straightforward answer to what I just described, which is to say, the composite and the rate limit in this configuration that we were just looking at are both sort of, … this is just, like, a terrible example of everything.
That you're just gonna evaluate all of these rules. Anytime you run out of space.
You might go and… change thresholds.
In your… in your pending sample.
… To get down to your rate limit. … And I think the rules that we… we have spelled out rules. You can't adjust the threshold based on… Randomness values.
… But you can… you can adjust thresholds arbitrarily, and then drop out spans according to their… their sampling decision.
I don't know, I'm… I think Atmar is squinting at me like I'm not making sense, … I don't want to continue rambling if I'm not making sense.
**Otmar Ertl (Dynatrace)** 20:24 And I'm myself still thinking about that, but, … Yeah. I mean, the usual way is… That you define weights, right, per spend, and based on the weights, you come to sampling decisions?
Also incorporating the capacity.
Oh… I mean, how does it propose this config? I think it's relatively easy to implement, right? It's an advantage.
**jmacdonald** 20:56 … let's see then, so….
**Otmar Ertl (Dynatrace)** 21:01 I mean… Inc.
not considering, consistent sampling, so I also have to think about it, if this can be realized.
In the context of consistent sampling, but….
**jmacdonald** 21:14 And in some ways, this composite rule is actually just a far more complicated version of the simpler case, which is this rate limiting.
which I think can follow Peter's sort of outline. The idea… but let me… let me give you a… maybe a more real example. So I have a… some sort of policy, and I don't want to literally express it here, but the idea is that I'm going to take one… if it's operation A, I'm going to take rate limit, like, one rate limit, and if it's operation B, I'm going to take a different rate limit. So now the sampling composition is, I will sample either A or B with different rate limits.
So, so now my spans start coming in, and I have a buffer of 1,000.
That's my maximum.
… And now my buffer has filled up.
I've put all the A's and B's that have matched into my buffer, because that's the intent, is to collect A's and B's. And now.
now that I'm out of space, or out of time, and I have a thousand spans that met the criteria of A or B, now I'm going to go back and apply my rate limits. I look at the A policy, it has a rate limit of 10 per bucket. Okay.
Find the 10th highest randomness value, and that's your threshold. That was the algorithm that we roughly spoke about.
It might be the 10th highest sample, threshold… 10th highest randomness value, plus 1.
I did… Atmar, you gave us a paper.
I read it, it made sense.
I think I… … And it was like a… the number space was reversed, so thresholds were falling instead of rising, or whatever, but so, like, that's why the off by 1, the plus one came in, but roughly speaking, that paper argues that you can… Sort your things, and then choose your cutoff wherever you want, and make that the new threshold.
… that matches the bottom K sampler as well. That's, like, my intuition for bottom K sampling is how it works. So then, I look at the A policy, I say, oh, well, I got 500 spans, but I really want 10, so I'm gonna choose the top 10 randomness values. And then I look at my B, and I say, oh, I wanted 300 out of… and I have… and I have… 500 examples, so now I'm gonna rank my 500 and choose 300, and put that threshold on my B-spans.
… I think that kind of makes sense, and probably this composite is just a more complicated version, but not very complicated compared to what I just described.
**Otmar Ertl (Dynatrace)** 23:51 I mean, if the… if the, … Yeah, buckets, or… This joint, so… meaning that a span can only fall into one bucket.
you're satisfying one condition, I think, then it's pretty straightforward, but in how this is defined is you know, there's a… there's a rest bucket, you know, or… I mean, the remaining capacity is used to sample any spans, so, meaning that spans could either can fall in multiple buckets, and I think then it's difficult, probably, to derive the sampling probability or define the threshold rates.
… I still have… To think about it, but… What this proposal, which implications, We follow from this proposal.
**jmacdonald** 24:50 … You were saying that it makes easier if you have separate reservoirs, essentially, for the.
**Otmar Ertl (Dynatrace)** 24:57 No, I mean… I mean, the approach what you described, you know, with setting the threshold is, I mean, if you divide, you know, a stream of… spans into different substrings based on a category, but a new span is… Contained in different substrings, right?
Then, of course, you can easily rate limit each substream with different rate limits.
….
**jmacdonald** 25:23 Is it sequencing important that I choose a rule and then stick to it? Like, I can't be in both A and B categories?
**Otmar Ertl (Dynatrace)** 25:30 Yeah, but here with this proposal, they say, yeah, if there's still capacity left, right, then… then they apply the, always on sampler, right? So, which means that, spans which were already… which were not sampled.
But following in some category 8, for example, which, for example, the test composite Policy 1, right?
We only take 50%.
of those.
… Yeah, you know, it's… you really have to think about it, yes, because it's computational, yeah?
**jmacdonald** 26:14 then I've… I've at least given you the problem statement that is on my mind, because this… I think of composite as being the next step. I still kind of… that the rate-limiting case is far more real in what I've seen.
And, I didn't have any more than the kind of thought experiment there to share with you. However, my last update is that, I've made a meeting for myself to talk to the author of this code, just to, like, pick his brain and see where he is as far as thinking for the future, maintenance, … I can ask him all sorts of questions like this, but I don't think he's gonna have great answers. I think he's sort of put this together, and he's trying to step back from it, and doesn't have opinions about probability sampling the way we do. So… his name is Sean Porter, … So, what I'll do is I'll meet him and share what I learned. I'll take notes. I don't think that it's gonna shed much light on the question I asked earlier, but it could tell us,
**Otmar Ertl (Dynatrace)** 27:19 ….
**jmacdonald** 27:20 things that we don't know. And again, back to my hypothesis, I still kind of feel like it will be good for OpenTelemetry.
In the long run, to have… at least be thinking about, essentially a… The standard or common configuration model for these Composite, predicate, filter.
Rules that we see, again, from… not just in sampling, we see it in rate limiting, we see it in batching, even.
So, that's where I… that's what I will be doing. … ….
**Otmar Ertl (Dynatrace)** 27:53 One thing to add, sorry, I just want to add one thing to this, proposal.
So I'm not sure if it's easy to derive this sampling probability, even if we're not considering consistent sampling, but just the sampling results.
Yeah, it's a traditional sampling, you know.
And I… I'm wondering how the probability is determined, right? I mean, this is the minimum what we want to have, right, to be able to extrapolate the data.
Not talking yet about consistency, but just the probabilities for the… … The probability has to be known in order to be able to extrapolate.
So, but I still have to think about it, how… This can be done with this proposal.
But if this cannot be achieved, then we do not have to talk about consistency, right?
**jmacdonald** 28:56 Yeah, okay, well, how's this? If in the back of your mind you come to any great realizations about consistent sampling and composite rate limits, I'm very curious where you think we can be.
I would say that the reason I'm… I'm just motivated to see this solved, if possible, for the users of the tail sampling processor, and maybe we'll come up with something.
That's all I have for us today. I apologize that it's not too much, … I… We'll follow up on the two things I said I would. I'm gonna meet Sean Porter, and I'm going to, write up something on this migration thread so we can just push forward on… on the replacing trace ID ratio sample project. I don't need any help with that, I think.
… any last items for us?
**Peter Findeisen** 29:53 Yes, so I have a question, so… There's a pull request that changes the specs for composite samplers, and there are some approvals there, but I'm not sure what is still required in order to get it merged.
This was on the agenda for our previous meeting, so there was a link there. Yeah.
….
**jmacdonald** 30:26 We're gonna first remove stale.
… I… I… I'm tired of this, like, we don't update OTEP's thing, because, like, it's hard to get them right, and it's hard to replace them as well.
….
**Peter Findeisen** 30:43 Yeah, we discussed this before, and it looks like there was an agreement that this is kind of an exception here.
**jmacdonald** 30:51 I agree with that.
**Carlos Alberto Cortez** 30:52 Yeah, I can probably, you know, mention something important there. I think that I was only waiting first that we did the specification release, so we don't mess with them, and it's done.
And I would like to just get a note on the header, or somewhere in the tab saying, like, there was an update that happened, so you don't have, you know, to, … Like, so people reading these, they know that, there was a change, you know? But anyway, that can be done even, like, after, as a follow-up. The only thing that I would like to wait, and it's up to you, Peter, whether we… you want to wait for Kent. Kent provided some feedback.
And you apply the feedback, what?
**Peter Findeisen** 31:31 Yes, it was just a typo, ….
**jmacdonald** 31:35 Okay.
**Carlos Alberto Cortez** 31:36 Okay, so that's okay.
**jmacdonald** 31:37 So that's resolved.
I think what you're suggesting, Carlos, is that we want to put, like, a banner somewhere that says, this was modified as of release XYZ, slightly. Just make note.
Great.
**Carlos Alberto Cortez** 31:52 Yeah, correct. And, that can be done even as a follow-up, so we don't, you know, wait even more time. I can just probably merge that and prepare a PR with the banner in the tab, and just mentioning this PR, you know?
**jmacdonald** 32:05 I think we're gonna need more approvals anyway, but… I wouldn't object to just, like, adding a sentence. So you said now the spec release was done, so we're not changing Something that's, like, half… half out the door, in other words.
**Carlos Alberto Cortez** 32:23 Yeah.
**jmacdonald** 32:23 We're just changing the next version that goes out the door.
**Carlos Alberto Cortez** 32:28 Yeah, correct.
**jmacdonald** 32:29 I just approved that, so I think we should be able to….
**Carlos Alberto Cortez** 32:32 Now, to merge.
**jmacdonald** 32:35 I would prefer to just put this one sentence in without another PR, because it's hard to get PRs approved.
**Carlos Alberto Cortez** 32:42 Oh, yeah, good choice.
**jmacdonald** 32:42 That's it.
Does that sound okay to you?
**Carlos Alberto Cortez** 32:45 Yep.
**jmacdonald** 32:47 … I would be willing to add that myself, and push it to your branch, if that works for you, Peter.
**Peter Findeisen** 32:55 Yes, thank you.
**jmacdonald** 32:56 Okay, I will take care of this, and I'll ping you, Carlos, when I'm, … … … I will do that.
**Carlos Alberto Cortez** 33:18 Sweet.
**jmacdonald** 33:19 Alright.
Well, thank you all. … I like to keep it short when we don't have too much, so see you next time. Appreciate it.
**Peter Findeisen** 33:27 Yeah. Thank you.
**jmacdonald** 33:28 Bye. Bye.
