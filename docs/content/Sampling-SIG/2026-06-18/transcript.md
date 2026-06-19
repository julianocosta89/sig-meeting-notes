SIG: Sampling SIG
Date: 2026-06-18
Duration: 55 minutes
============================================================

## Zoom Recording Transcript

**jmacdonald** 05:41 Hi, everyone. Peter Otmar.
**Otmar Ertl (Dynatrace)** 05:44 Hello.
**jmacdonald** 05:46 I missed a bunch of these meetings, and I feel bad about it, so I'm glad to be here.
And I'm glad to see you both.
I… I'm aware of four PRs that could be discussed. One of them is from you, Peter. The other three I don't think we need to discuss, though I will do the reviews for. The other three are… I'll bring up the notes, but the other three are Trace Pruning Sampler has a big PR.
tail sampling processor has a big PR, and this donation proposal from Honeycomb Which, if you remember, Kent was here for many years. Their product is now being pushed out by a different engineer.
So it's a dynamic sampler for the collector that, they've been using.
Oh, I'm glad Chris is here. Chris can talk with us about the tail sampler.
Hi, Chris. So I was just chatting while I brought up the notes, and And, I know I mentioned that there are 3 collector PRs, yours is one of them.
**Chris Marchbanks** 06:54 Yes.
**jmacdonald** 06:55 Here I come.
And then… Peter's got one. Oh man, how many of these did I miss? Let's just forget about it. But today is the 18th, and some agendas here.
Peter's put his PR up first, so we'll talk about that one, and then… Oh, I'm not… I'm not sharing yet.
I had, like, the craziest month of May that everybody… I'm just gonna say that while I'm fighting this thing. It was intense.
And it's over.
So… Yeah, here we are. Peter's got this, PR to discuss. I was aware of it yesterday, but I haven't looked at it. And then… I'm just gonna say we've got tail, sampling, threshold, we've got trace.
Pruning, next, ER, and then we've got… Any combs sampler.
Open. Cool. So, and then I was thinking about questions that have been on my mind.
I'm gonna roll one of my questions into talking with, Chris about threshold.
and tail sampling that… that I'm… that I'm sitting on. And then, I'll say no more if… at the very end, I have a question for Atmar about exponential histograms, but that's… that's not… that's not on topic. So, Peter, Let's discuss your work.
**Peter Findeisen** 08:27 Right. I don't expect us to do a deep dive during this meeting, just would like to give you some background, so… Apparently, well, the OTEP250 was created last year, and… At some time, it was late 2025, maybe November, some good sold, ported parts of this document into the official specification, documentation.
I miss that part, and I…
**jmacdonald** 09:02 I think that was me.
**Peter Findeisen** 09:03 Oh, okay, thank you.
**jmacdonald** 09:04 Could be.
**Peter Findeisen** 09:06 There were some discrepancies which were discovered quite recently, a couple of weeks ago.
And, I would like to, to, to fix them, because some of them are simply incorrect, and some are, just, well.
it's a naming thing, and it could be argued that one is better than the other, but I think I have a good argument to keep the original terminology that was used by the OTEP. So, this pull request tries to rectify things. By the way.
I noticed there are several things missing.
that, well, missing. Not ported from OTEP 250 to the official specification document. One of those is any of.
sampler that takes a number of delegates and handles them.
accordingly. And there… another thing is we miss the… Oh… rate-limiting sampler, which I think is super important.
**jmacdonald** 10:23 Yeah, I knew that I remember didn't make it, because I was the one Did the work.
**Peter Findeisen** 10:29 Right. That's not mandatory. They don't have to be there, but whatever is in the specs, we would like it to be correct. So I'm asking everyone, to… to have Another look at it.
Because, well, that's the official OpenTelemetry document. Of course, it is right now in development stage. It's not final, not stable, nothing like that.
But whenever there is any issue there, we should be very diligent in fixing those as soon as we can.
**jmacdonald** 11:04 Yeah.
This is hard.
**Peter Findeisen** 11:08 Will.
We… yeah, we are… well, the whole document is just one file for, trace…
**jmacdonald** 11:20 SDK.
**Peter Findeisen** 11:20 K.
And sampling is a small part of it, but… yeah.
**jmacdonald** 11:30 Yeah, that's why I couldn't.
**Peter Findeisen** 11:31 We know that.
**jmacdonald** 11:32 Formatted document here.
Cool, so I see… You know, some naming issues…
**Peter Findeisen** 11:42 Right, and the description of the composite sampler, what it does with the sampling intent, that part was simply missing, but it's a very important part, so I added it here.
**jmacdonald** 12:07 That's this logic, I take it.
**Peter Findeisen** 12:08 Yes, right, yeah.
A number of bullets here.
**jmacdonald** 12:14 All right. Well, I propose that we, since it sounds like you think we can read this offline.
**Peter Findeisen** 12:21 Yeah, of course.
**jmacdonald** 12:22 I'm just gonna queue up PRs for myself to review in the next couple days.
**Chris Marchbanks** 12:27 I will also I literally started, yesterday, started implementing this in Go, so I will take this poll request and.
**jmacdonald** 12:34 Nice.
**Chris Marchbanks** 12:35 folded into my Go implementation.
**jmacdonald** 12:37 Very sweet to hear that. Yeah, this is… things are starting to happen here. I'm really happy to hear that.
I assume that Yuan Yuan's PR merged, the one that was under discussion two weeks ago, sort of as a foundation for Go sampling.
**Chris Marchbanks** 12:55 I… didn't see it merged yet, I was just working on top of it.
**jmacdonald** 12:59 Okay.
**Chris Marchbanks** 13:00 Let me see…
**jmacdonald** 13:03 Each… each repo to its own pace, I don't know.
**Chris Marchbanks** 13:05 Still, still not merged. Yeah, so I just… Branched off of.
**jmacdonald** 13:09 I gave another approval on it about 2 weeks ago.
**Chris Marchbanks** 13:12 Yeah.
**jmacdonald** 13:13 Okay.
Very good. Fyi, Chris is working on OTEP250 support in OTEL Go. Very good. I can write our attendees in here. Josh and Peter as… Thank you. Okay, Is there any more to say, Peter, on the topic? I welcome the updates. It sounds like you are not adding any of, or Back in this PR. Correct.
**Peter Findeisen** 13:49 Correct. I don't want to do everything at one step. We might think about adding them later if we agree to do this, but right now the scope is limited to what I think was wrong.
**jmacdonald** 14:00 Makes sense.
**Peter Findeisen** 14:02 Yep.
**jmacdonald** 14:03 I do very explicitly remember leaving out the rate stuff, because I was trying to find a… just a place to cut it off. It was a large PR at the time. I did not recall explicitly leaving out any of, So that was probably a mistake. I… I remember feeling just kind of, like, a little bit of… Hesitation about rape, because… it was going to require a lot of writing, or convincing people, or proving that the algorithm makes sense, and so on. Like, it was… it was a little bit too… there's not quite enough material in the OTEP to, like, make it… make it easy for me.
**Peter Findeisen** 14:45 Yup.
**jmacdonald** 14:46 At least that's what I remember.
**Peter Findeisen** 14:47 That's, that's true, that's true, yes.
**jmacdonald** 14:49 So, but we… I think we all welcome that. And, I mean, as… More… more of this work begins to take place.
Shall we move on to these other PRs?
That are open, especially since we have Chris here. I, I was, I was gonna try and find the actual PR numbers, but people have been asking me to review Some of these.
Chris, do you have one that's in progress?
**Chris Marchbanks** 15:26 Yeah, so I just have one, it's just starting propagation of trace state, so that's the first one, let me… Shh… There's now a link, So I've got that one, it's just doing it for probabilistic policies to begin with, and is, like, fairly limited in scope, but behind a feature gate.
So, I hope to continue to evolve it, and then turn it on, and fix some of the… it only works in blocking mode correctly as well. So, like, there's lots of caveats today, but I was like, let's get something concrete started.
That isn't thousands of lines.
**jmacdonald** 16:08 Got it. Yeah, I just opened up the collector contribo and typed in sampling, the polls search, and there's, like, 10, 12.
**Chris Marchbanks** 16:15 There's a fair number, yep.
So, anyways, it mostly builds on top of… Making the probabilistic sampler similar to the probabilistic sampler and tail sampling.
And updates… the thresholds when appropriate. Budgets for that.
There are a couple composite samplers that are a bit unknown in their behavior still that I'm still working through that I just left out of this PR.
**jmacdonald** 16:42 Yeah.
And I take it you're sort of… it's interesting that you're working on the OTEP250 stuff at the same time as you're working on, like, almost the same type of logic problem.
**Chris Marchbanks** 16:53 Yeah, that's.
**jmacdonald** 16:54 the connection.
**Chris Marchbanks** 16:54 It is very much all the way through of, like, start an SDK level, there's some sampling decision made, and we need it at all of the levels to eventually be able to pull that correct or extrapolated metrics.
**jmacdonald** 17:09 So, it makes sense to me that you would use the blocking mode, I think.
**Chris Marchbanks** 17:13 Yeah.
**jmacdonald** 17:13 At least just for simplifying the problem.
**Chris Marchbanks** 17:16 Yep.
**jmacdonald** 17:16 And…
**Chris Marchbanks** 17:19 And I plan to address non-sampling mode at some point, I agree that we can just kind of keep track of, I dropped about this percent, I'm going to… Change my thresholds by a little bit.
**jmacdonald** 17:31 Yeah, Cool.
I don't think we should try and review a PR with 27 open files in it, but, I will definitely do that. Are there any, like, math questions that came out of this for you?
**Chris Marchbanks** 17:48 Math-wise, it wasn't too bad, like, most of it's already explored work. It was making sure that… if you have an AND… like, really just make sure the logic of, like, oh, we have an AND… sampler, make sure that I adjusted the threshold the proper direction, which I believe should be the most… limit, the most limiting for AND, because… The most limiting policy is what wins.
Just double-check my logic on those.
**jmacdonald** 18:23 Gotcha.
will do… I was just looking up all the other PRs. There… there's two open for the trace pruning. To me, this… the question that I wanted to ask, that I put the asterisk for is the… I just want to refresh Okay, so if you're… I think the reason why the blocking mode is simple is that you… is that you can just respect the logic that we've defined effectively, like, ANDs and ORs and, threshold adjustments based on, based on the data that's coming in, and what I'm… what I'm… The reason why that logic got hard, in my opinion, or memory, is that there's a rate-limited policy.
And so we're tying this back to where Peter started as well. The rate-limited policy, Left me feeling, that we would… I'm not gonna be able to phrase this very coherently, so I'm gonna try not to, but, We have discussed in the past, reservoir sampling as a topic, and how… There's this… abstractly speaking, in the reservoir sampler, you're gonna make some decision-making about what to keep and what not to keep. We want consistent decisions, so we're gonna rank the… The… the data points by… trace ID, or by 56 bits of trace ID. And, but that… In a rate-oriented sampler, what you're… Trying to do is adjust the threshold To where the right number of data points fall out.
And… The… so then you take your… you take your sorted list of points, or traces, and you look at the… Values that have the… Largest… randomness value first, I guess.
And then, at some point, you say, okay, this is my set, this is the cutoff threshold.
This is the cutoff randomness value. It's my new threshold. My new threshold is 1 less than the new randomness value, or something like that. This was, point of math that I believe was justified by a paper that we looked at by Ting from 2022 that Otmar gave us, or maybe Peter gave us, or both.
Is that… does any of what I just said, like, ring or, like, resonate with anybody?
**Otmar Ertl (Dynatrace)** 21:23 Yes, sis, he'll remember it.
**jmacdonald** 21:25 Okay.
**Chris Marchbanks** 21:27 Yeah.
**jmacdonald** 21:27 I… the reason I ask is partly I think this comes up when you look at rate limiting in the tail sampler, although maybe only when you try to do non-blocking.
**Chris Marchbanks** 21:37 I think it'll happen with blocking, too. I specifically left rate limiting out of this pull request.
**jmacdonald** 21:43 Fair.
**Chris Marchbanks** 21:44 I think we can solve it… I mean, my idea for solving is, like, we already batch things together, so I was thinking of effectively doing the sort and find how many traces are gonna make it through for the rate limiter.
based on the batch, basically. But, like, that's a fairly… it's a larger refactor than I wanted to do in this initial.
**jmacdonald** 22:04 Sure.
**Chris Marchbanks** 22:04 work. Fair. But, like, I think there's a path forward in my mind.
Without having to…
**jmacdonald** 22:15 I'll tell you why I'm…
**Chris Marchbanks** 22:15 Changed everything.
**jmacdonald** 22:17 I'm… we're working on this hotel aero project, so I want… and it's given me a chance to have kind of a clean slate with… observability or what instrumentation we do. I'm not using an OTel SDK because our assertion is that this code will become an SDK effectively, so I don't want to depend on another SDK, And so I'm looking at my own, like, logging code path, like, trying to make it as short and as sort of efficient as possible, and one of the things that concerns me as a telemetry agent is, like, I don't want to fall over, trip over myself from logging too much. So, I want a simple, like, throttler for self-induced logging that just prevents me from excessive logging myself, about myself, while I'm handling other people's telemetry.
And, and I've always enjoyed thinking about reservoir samplers for some reason, And I'm looking at log events that don't necessarily have a trace ID on them. I'm not trying to solve a distributed tracing problem here, I'm just trying to limit the event rate for log events.
And I want them… limited by call sites, so that independent call sites are independent, you know? So, like, if one noisy call site comes up, I want it to be throttled, and the rest of them should keep coming through. And so, I know how to throw a weighted sampling algorithm at this problem, and I'm looking at what I have, and what I have is a bunch of… log events in a buffer, and I finish my time window, and my sampler has chosen The, you know, the top 100 by some measure.
Or the smallest 100 by some measure. But they never had a randomness value.
on them. I was just putting them through a reservoir sampler. So I have a random number that I used for each one of them.
And I compute a threshold.
And I think… what I can do… As… use my weighted sampling result, which will give me an adjusted count.
Turn that adjusted count into a threshold.
Compute the randomness value that's 1 less than that threshold.
put the randomness value on the log statement, and send it out. That's my consistent sampler.
It's not consistent, sorry, that's not my… it's not a consistent sampler, it's just a way to put weighted log events out.
That… that's the topic I had with my asterisk, is that I'm trying to figure out how and when OpenTelemetry has a way to say, here's an event.
I sampled it 1 in 10.
According to a reservoir sampler.
How do I send that information?
In other words, I'm sampling… Using thresholds, but I'm not using randomness values.
And I think I can just make up a randomness value according to the logic that we just said, but I'm… I feel like a… I'm in a vague territory right now.
Does any of that… Have I asked a question yet?
I think I did.
**Chris Marchbanks** 25:46 The one thing I heard that didn't make sense, you said, set the randomness value to 1 less?
Then the threshold for all of them?
**jmacdonald** 25:54 One greater than the threshold.
**Chris Marchbanks** 25:57 Or sorry, what, what, yeah.
**jmacdonald** 25:58 Off by one, somewhere.
**Chris Marchbanks** 26:01 But for all of them.
Like, wouldn't they, like, so, like, every logline in this buffer would get the same randomness value in that case? That was the part that I was, like, a little, like, wait, what?
**jmacdonald** 26:12 Yeah.
**Peter Findeisen** 26:12 Sorry, I heard… initially, I understood that we are setting the threshold, depending on the randomness, not changing the randomness, changing the threshold.
**Chris Marchbanks** 26:25 Yeah.
**Peter Findeisen** 26:25 Or miss… did they miss it?
**Chris Marchbanks** 26:27 That's what I would… that's what I would have expected.
**Peter Findeisen** 26:30 Yeah, yeah, okay.
**jmacdonald** 26:32 Setting the readiness based on a threshold.
**Peter Findeisen** 26:35 No, no, no.
**jmacdonald** 26:37 Setting threshold based on randomness.
**Peter Findeisen** 26:39 Yes, we do not touch the randomness.
**jmacdonald** 26:43 Okay, let me… let me spill out the scenario that I'm trying to… to work through, because I would like to make a no-tel spec eventually here, some… somehow.
So I have these log call sites.
And they trigger in the code when I come to them. And they have just one identifier that says which call site they are.
And so, in the moment of having my call site right there before I evaluate the arguments, I'm trying to skip the logs that are expen… that are not going to be making the sample.
Right then and there, I generate a random number.
Because I don't have context other than what I make up. That's sort of a constraint, but… but I'm really targeting the case where all the logs in the world, you know, don't have tracing yet, like, I don't have trace IDs sorted out here. So… I have my call set identifier, and I have my random number between 0 and 1.
And, I'm looking at the sort of classic priority sampling, or bottom case sampling.
Where you… you are going to invert that number and then sort, and then that's the threshold, effectively. And bottom K adds, like, an exponential and a logarithm, but it's the same algorithm. So that at the end of my period of time, I've chosen my hundred log messages that kept… that were kept. And never mind the wait stuff, because that… it's sort of independent. Each… each item is going to have, a… A rank.
And each item has a adjusted count, like, which I computed, so I can take an adjusted count.
And I could put that on the log event. I could say… I could make an attribute that says, hotel logging adjusted count 100, or 101.
But what I want is a semantic convention that this group agrees to, and we already have some semantic conventions about trace state and threshold and randomness, but the… but that's a consistent story with 56 bits that we know how to find, and I'm saying I've been doing probability sampling, or flipping coins, essentially. And, I have a value that I have determined to have a adjusted count that I… that I believe in, and now I want to turn it into information that is, semantically conventional.
In a sense.
Yeah. And I'm… Alright. And like…
**Chris Marchbanks** 29:11 Gone.
**jmacdonald** 29:12 Okay, I'm trying to figure out if there's a… if there's a translation from, I know my adjusted count, and I had some randomness, but it's not consistent randomness.
I want to output something that somebody will use to count correctly. That's all I want.
And… It's maybe two parts of the question. The first part is, if my adjusted count is not zero.
So, I have an arbitrary adjusted count I want to send. How should I do that? Could be decimal, or it could be floating point numbers, but I don't like that.
Second question is one that we've had in this conversation years ago, which we… it's come and gone, this idea that I've tried to propose myself, and we've rejected it so far. Maybe we're still rejecting it, but the idea that if something doesn't have a sampling probability, meaning we did not select it, and you're still sending it.
how do you say zero? One way to say zero is to leave off your trace state, or leave off your threshold.
But then you're sort of having a convention to say that, well, I assume that things will come in with threshold, and if there's no threshold, I don't know how to count it, so I'm going to count zero.
And the reason I'm saying this is that there are times in a… in this… this reality that I'm trying to envision. So I go through my sampler, I choose… there were… let's say there were 10,000 events in my period. I chose 100 of them.
That means there was 9,900 events that I'm not choosing.
And… In some sense, I… we've… When I choose my 100, and I give them each an adjusted count, those are unbiased.
summaries of the data. If I throw in another value that didn't make the cut, I'm biasing my results, if you count it. And one of the solutions that I'm familiar with, then, is to count zero for all the things that I want to send you that didn't get counted.
So these are… these are values that didn't make the sample, but I might still want to send you.
The… the reason I… I've been describing this as sort of like a FOMO, like, you want to do sampling, but you're afraid, so you're afraid you're going to lose stuff.
Like, I'm… my sampling should be good enough to find everything you want, but if it's not.
Maybe you have a second fallback rule, which is like, oh, and then all the errors, please send me those too.
So now I have a sample that's 100 and it's unbiased, but I also have all my errors.
And I… I'm concerned that I can't count the errors because my 100 covers errors, and I will bias my summaries if I have both a hundred of unbiased events with counts, plus a bunch of straggler events that I had FOMO about, so I kept them. So I'm saying the FOMO events, those are… weight zero. I count them for zero. And you can see them, but you shouldn't count them.
**Chris Marchbanks** 32:11 The.
**jmacdonald** 32:12 Oh my god.
**Chris Marchbanks** 32:13 That is… some of those could have been selected as your 100, so you should have counted.
**Peter Findeisen** 32:17 Right.
**Chris Marchbanks** 32:17 With a… Right.
**Peter Findeisen** 32:18 So… Yes. So my… I have been thinking about similar scenarios, of course, in terms of more… in terms of spans rather than log messages.
But if you reverse the order, if you first look at errors, and… Sample them with probability 1, giving them adjusted count 1, and then you handle the rest, then your results will be correct.
**jmacdonald** 32:48 Yeah, yes.
This also…
**Chris Marchbanks** 32:51 It also comes down to, similarly, it's the same as, like, the Ineof in the original OTEP 250, like, you just have… you have to choose the… The appropriate threshold.
the most permissive, I guess, threshold in this case of whatever policies you have. Tailsamplers in this exact same scenario, where I have a latency policy and I have a probabilistic policy.
And I need to… oh, they both sampled, I need to be sure that I don't modify the threshold in this case, because it came through the latency policy.
So I think it's a similar problem to that.
**jmacdonald** 33:33 Yeah.
And I agree with the construction you just made, is that you can always re-sort or rearrange the sampling policy or the design to choose what you're… what you are worried about missing first, and then put the rest into a sample, and now you've got, sort of, two data sets, or whatever.
my, my… in my particular application, where I'm just trying to make a… I'll call it the automatic sampler. Like, I have… I want this to have as few parameters as possible. It's, like, the dumb, like, fallback safety mechanism.
And also, my concept is to only choose the size of the reservoir and the time period for the reservoir, and that's it.
And so, why I would have FOMO… first of all, I actually don't have FOMO. I'm confident about sampling, and I'm confident that if I get the algorithm right, that I will have what I want and be happy with it. But… I'm… I know that the users that I'm trying to convince to accept this solution have FOMO, let's say. So I'm saying, I'm gonna choose… I have this algorithm that's gonna do a great job of choosing what we want.
And it also can observe the things that we're gonna lose. Like, there… in… in case of emergency, when the sampler bee heart starts to behave bad, I can literally see it falling apart right in front of me, because things are falling out of the sampler that… that are… have zero… no copies. Like, there's… this is a rare species. Like, this… I… I saw a… Creature that I've never seen before, but then I had to let it go because my sample was full, and the randomness didn't support it. So these are the things that I'm genuinely aware that I'm losing.
But my algorithm… it's falling apart, so… so what I want to say is, okay, I saw some rare stuff, it's… the algorithm is breaking at this point. Here are the things that we're going to miss with zero count.
And I don't know how to say zero count, and I don't know how to say Adjusted count was calculated by an algorithm that's not consistent.
That's what I… that was my topic.
**Otmar Ertl (Dynatrace)** 35:45 So what you want to achieve, I think, is something like a weighted sampling approach, where you put some more weight on rare stuff than.
**jmacdonald** 35:55 Yeah.
**Otmar Ertl (Dynatrace)** 35:55 I figured…
**jmacdonald** 35:56 The concept is essentially equal representivity.
It's actually a very simple algorithm, I'm super happy with it right now. It just… just computes inverse frequency weight, and then… I think I've spoken about this here before. I had an idea about using, like, diversity estimates. It doesn't turn out to help.
**Otmar Ertl (Dynatrace)** 36:18 Right.
**jmacdonald** 36:19 the… it actually helps… I mean, it helps something, but it doesn't help what I was looking for. So this is a very simple algorithm that… that… Uses weighted sampling with inverse frequency weight.
And if things are working well, it gives you equal representation, so every call site should have the same… about the same number of examples. That's when it's working well. When it's overloaded, it's just gonna start losing stuff. And that's what I was saying. I would be happy to then, like, pass through with a zero weight annotation.
Let me ask a more direct question, since I think I'm… I'm… often… left field, maybe. If… Peter, I think that you've talked about rules that you believe in, where If we have… A rate-limited sampler, And we… And we… There was a… there's a case where you're gonna use some randomness, but then, never encode it, because you want to hide that randomness to avoid, conflicting correlations.
is… is this… am I looking at the same type of problem here, where I say, I know my adjusted count, I had some randomness here, but I don't have a consistent randomness value. I just have a randomness value.
**Peter Findeisen** 37:56 Sweet.
I'm not sure if it's the same problem or not, but we do have this concept of reliable adjusted count in ODEP 250.
Right? This is… this is for the case where… we… We have the threshold value, which is… which is… and randomness. We… Okay, no. In this case, we have the valid threshold.
We generate new randomness value for this particular case, because we know the probability with which we want to sample, but we do not want to Use the original randomness value, because it will lead to some errors.
Downstream.
I believe I described a use case… a particular use case for this.
In, in the document.
**jmacdonald** 39:00 Yep.
And that's what I think I'm leaning towards. What I'm trying… what I'm… what I'm asking in the most direct way now, I think, is, suppose I've done my weighted sampling, I have a… I have an account that I believe in, according to the math. The count is 2, so it was 50-50 sampling, just to be clear, just to make it easy.
I know that the count of 2 corresponds with a threshold, TH value 8, or hexadecimal 8.
and I know that I don't have a consistent randomness value. Is it okay for me to put TH2… TH8 on that span… on that log record, on that span, to make it simple, and leave off the randomness value?
**Peter Findeisen** 39:51 My gut feeling tells me no.
**jmacdonald** 39:54 No.
**Peter Findeisen** 39:55 Because… When… when you look at… At a span, you are processing a span, well, in a collector, which has… which has the TH value.
And there is always some randomness value, either it's implied or explicit.
Then… In the collector, you know that… the distribution of randomness values across all spans that have the same TH value is uniform, and it's between TH value and max.
And I believe this is an important property that can be used by tail samplers.
To… to adjust… to… to further resample the set of spans. If you violate this principle.
It will be very difficult to… to resample the set of spans. For example, what if you… if you have All randomness value the same.
with different, if you… If you record a TH value, and as you say, there is no randomness, then… This randomness will be implied, or the same for every span?
I'm a little bit lost here.
**Chris Marchbanks** 41:47 Yeah, I think I… like, that's my gut reaction as well, though, is, like, we don't want to… there is a… I see the argument for something that's zero, of just, like, do not count this.
For this case, and, like.
**jmacdonald** 42:00 We certainly can't put that in threshold, that's one of the.
**Chris Marchbanks** 42:02 You can't put that in threshold. Yeah, we talked about this a few weeks ago, a month back or so.
Yeah, because it's also, like, where I'm thinking about this is, like, trace rehydration as well. Like, there are features where we, like… Like, we'll keep all traces around for a while, even without, like, we'll have tailsampled, send them to normal storage, did metrics processing, etc. on them. But we have a thing where, like, oh, this showed up in an exemplar from a log later on, or something like that, and somebody clicked on it, and we'll rehydrate it.
This feels very similar to that, yeah, that FOMO problem of, like, oh, this is actually… somebody thought this was valuable. We rehydrate it, even though it didn't match.
are… it's… It's randomness.
Wasn't, like, didn't match our original policy… our original threshold, therefore, yeah, what do we do with this metric?
What do we do with this in metrics? And that's… So I guess what I'm saying is I'm seeing this in other areas, too. I think that's a similar problem to what you're describing.
**Peter Findeisen** 43:13 Yeah, our old, consistent sampling produced powers of 2. It had a special Encoding that allowed for zero adjusted count.
And we… we…
**jmacdonald** 43:27 I've been asking for this for a long time.
**Peter Findeisen** 43:29 It was coming up in discussions a lot, and, well, you mentioned… Chris, you mentioned exemplars. For exemplars.
The recommended approach is, if you have a choice, you… you select… a span with the highest randomness value, and you do not guarantee that it will get Through all the sampling pipelines.
It's just a best chance.
**Chris Marchbanks** 44:00 Yep.
**Peter Findeisen** 44:01 That, that kind of avoids solving this problem.
We do not have the zero bound… well… And we even…
**Chris Marchbanks** 44:08 Not all libraries support that, because, like, somebody will just throw a trace ID into a log without a care, and…
**Peter Findeisen** 44:16 Yeah. Yeah. Right.
**jmacdonald** 44:21 This is a useful conversation for me.
it's sort of a negative result. I don't… I still don't know what I… what I would like to see, but it might be, for logs.
Without randomness.
That were sampled.
Maybe an attribute named hotel.logging.
Adjustment count. Count.
equals… a hundred… 1001.
Or… Zero. I don't know. I'm, I'm gonna leave it there. We don't have an answer. I don't have a… I don't have an answer.
I don't need an answer, but I want one.
So…
**Chris Marchbanks** 45:07 Yeah.
**jmacdonald** 45:08 So think, I guess, if any of you think, over a coming period of time, that you may know of a reason to have weights or adjusted counts that are not consistent, or not tied to a threshold.
Think about it, or let me know, or come back to this meeting, and we'll talk more.
**Chris Marchbanks** 45:32 Sounds good.
**jmacdonald** 45:33 Okay.
I saw you come off mute, Atmar. Any thoughts?
**Otmar Ertl (Dynatrace)** 45:43 I mean… So, if you wanna, you know, I mean, it's a bot.
Because with standard sampling, you have the free choice of choosing a sampling probability for every individual item.
You know, and you just have to select the probability.
Or, which translates into threshold.
Such that you achieve what you want, right? So, so that you have, for example, for certain items, a higher probability than for others.
Based on… on the… Criteria, yeah, you know.
It's, But in principle, I think, with consistent sampling, it would be possible to do it in a weighted way.
So, this… what I can see.
**jmacdonald** 46:44 Okay.
I'm thinking… I feel like I… you… what you said ties back to stuff that you've said in the past, as I remember, and… and I know that… In part, I know that you have proposed reservoir sampling based on different criteria, effectively, and I'm just following these dumb algorithms that I know from ago, that…
**Otmar Ertl (Dynatrace)** 47:08 Yeah, for unweighted reservoir sampling, yeah, you would choose the same threshold for all of your items in your reservoir, right?
If you want to have weights or give favor some kind of items, you would have to choose the thresholds individually.
But, yeah, you need an algorithm for that, yeah, it's not so easy, you know, to achieve, actually.
Devoids, what you want.
**jmacdonald** 47:36 But are considered.
**Otmar Ertl (Dynatrace)** 47:36 You're YouTube, Sylvia.
**jmacdonald** 47:39 Okay.
I, as I said, don't… don't need a solution for this, but I'm probably gonna do this dumbest thing for now, which is to say I have a count that I'm… that I believe in, and it's not specified anywhere.
And… maybe I'll think some more and come back, and maybe we can talk about it again.
inconclusive. I appreciate your, thoughts.
In that case, so I'm promising to do 4 PR reviews, at least in the next few days.
It's actually 5, because there are 2 of these.
Oops.
PRs.
And with that, I think we could propose to end the call.
**Chris Marchbanks** 48:28 I had one more…
**jmacdonald** 48:29 Thank you all.
**Chris Marchbanks** 48:29 Like, on the trace pruning wall.
**jmacdonald** 48:31 Oh.
**Chris Marchbanks** 48:32 Actually.
**jmacdonald** 48:33 Okay.
**Chris Marchbanks** 48:34 Okay, I didn't…
**jmacdonald** 48:34 mean to talk about it, because we don't have Sean, but you have been speaking to Sean.
**Chris Marchbanks** 48:38 Yes, yes. So another PR… so right now, like, those PRs, yes, just please review them. There's another PR where… so trace pruning right now… effects sampling, by… effectively, we're dropping trees.
And we might keep a couple trees around as outliers.
But there's not really much consistent about this. Something I was planning to… I was thinking about adding to trace pruning is the ability… is… Basically, a way that we keep a set of… example trees around in all cases. Maybe it's 10%, maybe it's log base 2 of the number of trees we'd be pruning away. I don't totally know what the number would be yet, maybe it's something else.
From that, we could… Change the threshold on these spans, such that… You could, again, do math and know that, oh, this… this span actually, in this tree actually would have happened a thousand times, or something like that, approximately this amount.
This is the first time I've kind of done, like, oh, I'm sampling within a single trace, not… At the trace level, where there's randomness.
And I was curious, like, what would be the major concerns about that? Because right now, like, if you're trying to look for a specific span type or something, your metrics are going to be off if you're span pruning, and I don't like that, so I think we need some way to handle it.
But the randomness is tied to a trace right now.
Yeah, so anyway.
Curious if… Anyone had thoughts on that?
**Otmar Ertl (Dynatrace)** 50:24 So you're talking about choosing different thresholds for spans of the same trace?
**Chris Marchbanks** 50:30 Yes.
**Otmar Ertl (Dynatrace)** 50:32 Yeah.
I mean, this is…
**Chris Marchbanks** 50:36 Go on.
**Otmar Ertl (Dynatrace)** 50:37 Also, actually, this is, what I, you know, described in the paper. Many years ago, was published in our head.
**Chris Marchbanks** 50:46 Yeah, so I guess it'd be similar to partial trace sampling, right? Yeah, I guess it'd be similar to partial trace.
**Otmar Ertl (Dynatrace)** 50:50 Yeah.
**Chris Marchbanks** 50:50 Yeah, you'd have… So I guess as long as we keep randomness the same… And we just changed the threshold… Such that outlier traces keep the same threshold, and these randomly sampled… or outlier trees keep the same threshold.
Because they're deterministic in one, and then the randomly chosen ones put… modify the threshold appropriately, there shouldn't be problems.
**jmacdonald** 51:20 I think I'm having a little bit of, distance from this code, making it hard to quite understand your words.
But I… Okay, so I…
**Chris Marchbanks** 51:29 I guess rephrase… let's ignore outlier… outlier trees for now.
if I choose a 10%, if I say I want 10% of… trees to be kept around, not pruned away, if I adjusted the threshold by 10% off… if I adjusted the threshold appropriately for all of those.
That would be the correct approach.
Effectively multiplying… Multiplying all of the example trees by 10.
**Otmar Ertl (Dynatrace)** 52:12 What do you feel?
talking about for equalizing.
**Chris Marchbanks** 52:15 Yeah, me.
**Otmar Ertl (Dynatrace)** 52:18 So are you talking about sub-trace, or, you know, if you have… what would you.
**Chris Marchbanks** 52:26 So let's say we fan out to a hundred different… we fan out an operation to 100 different instances.
Span pruning would collapse that away.
Into, this was just the structure. The new feature would say, let's keep 10 of these.
Therefore, all of those would have to be multiplied by 10.
in the threshold.
**Otmar Ertl (Dynatrace)** 52:54 Yeah, I mean, you… I mean, it's… if you… if you just select a different threshold on this… On all the spans of the suckery.
Then I think everything should be fine, right?
**Chris Marchbanks** 53:11 Okay, great.
**jmacdonald** 53:12 But the… Okay, yeah, yeah. So… you're… Lowering the threshold until you have the right number of exam pars for each subtree.
**Chris Marchbanks** 53:25 Yes.
**jmacdonald** 53:28 Raising the threshold, yeah.
Okay.
I think I followed, and it makes sense.
**Chris Marchbanks** 53:34 Okay, sorry if.
**jmacdonald** 53:36 We're not using the rails.
**Chris Marchbanks** 53:37 Very well.
**jmacdonald** 53:38 We're not using randomness of the… band ID or anything. We're just saying, for this subtree, we're gonna change the threshold for the same trace ID.
**Chris Marchbanks** 53:47 Yes, and I won't mess… yeah, I won't change randomness or anything like that.
Great.
**jmacdonald** 53:57 That's what we think.
I appreciate all this.
This is hard stuff.
**Chris Marchbanks** 54:04 Yeah.
**jmacdonald** 54:05 You got the answer that you wanted, Chris?
**Chris Marchbanks** 54:09 That helps me out. Great, thank you.
**jmacdonald** 54:13 Thanks, Admar, thanks, Peter. I will… and I will do the reviews for you, Chris, and others. Appreciate all of this. Okay. I'm glad we had a normal meeting.
My sense is that… Two weeks from now.
Might work.
Although, it's Thursday before a U.S. holiday.
We'll see. I don't know.
try my best. If I'm not gonna be able to make it for some reason that I can't predict right now, I will let you all know.
**Chris Marchbanks** 54:43 Sounds good. Bye, all.
**jmacdonald** 54:44 Happy holidays, or if you're US in 2 weeks, or whatever, or not. Happy World Day, everybody. See you all next time. Appreciate you.
**Peter Findeisen** 54:53 Bye.
**jmacdonald** 54:54 Right.
**Otmar Ertl (Dynatrace)** 54:55 Beautiful.
