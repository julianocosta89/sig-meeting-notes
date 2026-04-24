SIG: Go SIG
Date: 2026-04-23
Duration: 56 minutes
============================================================

## Zoom Recording Transcript

**Tyler Yahn** 01:05 Hey, Brian.
**Bryan Boreham** 01:06 Hi there.
**Tyler Yahn** 01:09 Hey, David.
How's it going?
**Bryan Boreham** 01:21 Oh, sorry, distracted. Yeah, I'm good. I… About 30 seconds ago, got round to reviewing the PR that you asked me to a week ago.
Okay.
**David Ashpole** 01:33 Awesome.
**Tyler Yahn** 01:34 sorry, the PR…
**Bryan Boreham** 01:36 David's, David.
**Tyler Yahn** 01:37 Whoa.
**Bryan Boreham** 01:39 In the, spec or semantic conventions about Go metrics?
**Tyler Yahn** 01:46 Right.
For the runtime metrics for the opt-in stuff, right?
**Bryan Boreham** 01:49 Yeah, yeah.
**Tyler Yahn** 01:50 Yeah, nice, okay, cool.
**Bryan Boreham** 01:52 I think just the one… sorry, we shouldn't stop the discussion, or even necessarily put this on the agenda.
**Tyler Yahn** 01:58 It's pretty… Pretty open right now, but yeah.
**Bryan Boreham** 02:03 So, I guess.
I… I just… I think the one interesting thing I said is that everything seems to be lumped under other. In memory, everything is lumped under other, apart from stack.
And that surprised me.
**David Ashpole** 02:18 So, the interesting thing, right, there was the discussion in the Go runtime, like, the actual… not us, but the Go like, I think I see you on the agenda every week, so I'm pretty sure you attend.
**Bryan Boreham** 02:32 Yeah, I missed it this time because of the Prometheus meeting, but I'm normally there, yes.
**David Ashpole** 02:37 But the original memory metric actually came from A discussion there around… Like, the basic question from them was, What memory metrics are going to be stable Right. In a long-term way. And they came back with, you should just have stack.
Which… is fair. That is the most useful attribute, probably.
But now, with the CP metric.
**Bryan Boreham** 03:12 I mean, the one that tends to be the biggest is the heap, and… So it's… I just feel that you… the way it's laid there, you just always have to go with the full detail, because… Because you're hardly ever… Like, yeah, when you have a choice between stack and other, you're just always gonna look at the big number in other and go, well, what's that?
And.
**David Ashpole** 03:41 Right.
**Bryan Boreham** 03:46 And it's difficult for me to stand up an argument that you shouldn't just always look at the detail, but, But I think heap.
I mean, I guess there's an argument that the meaning of heap, or what exactly you count as heap, could change over time, and that might.
Disturb people, but… Anyway, that's it. That's my comment.
**David Ashpole** 04:16 Okay, yeah.
It's not actually changing in this PR.
This… this PR is just adding the detailed Version of it.
But it is useful feedback.
And I do feel like if… a typical Go app is run, and More than half of your memory-reported usage falls into the other category that we've done something Not very helpful.
Yeah, so I think that comment resonates. I'll have to… I haven't looked… I think part of the problem is I haven't run a lot of Go apps with these metrics enabled in the detailed mode to see what actually, in practice, is consequential, so maybe I'll do some experiments. I had the same thought for the… CPU metrics, which is… I've grouped them Based on reading the documentation for them thus far.
But it would be helpful, I think, to maybe go through and look at which… which numbers actually are… Meaningful in some way.
In terms of why not just always turn on the detailed ones? That's mostly out of a… a concern that… Like, if Go does decide to change these categories slightly, it would be nice if everybody's dashboards didn't break every version.
**Bryan Boreham** 05:42 Yeah.
**David Ashpole** 05:43 Some aspect of, like.
Can we keep the detailed ones opt-in so that the blast radius of those changes is smaller?
**Bryan Boreham** 05:55 Yeah, so I've… I've never… really looked at the GO stats on the breakdown of CPU. I've just always gone to profiling.
Whereas memory… The thing is that only the heap shows up in the memory profile.
And that's something that we've talked about at the, the go-round time meeting.
So it's… it's far more important that you have some kind of metric breakdown.
But now some other people have turned up, and we're still talking about things that aren't on the agenda, so now I feel bad again.
**David Ashpole** 06:42 I'll put.
**Tyler Yahn** 06:43 They're on…
**David Ashpole** 06:43 agenda. And then… I'll write down a few notes.
**Tyler Yahn** 06:50 Yeah, I did add it to the agenda, but yeah.
I think that this is worth talking about. I think it's a good, relevant topic.
We can move on to David's other question about algorithms, though, if we want, if we're all done with this.
Cool. So, David, you wanted to talk about an open question for exemplar reservoirs? Switching… this… I'm guessing you're talking about the histogram reservoir, right? Not the…
**David Ashpole** 07:32 Fixed. So, let me talk you through… So… so I tried… we'd previously… or I'd previously tried to do a high concurrency implementation of the algorithm L, right? And it turns out that was not correct.
And I explored a bunch of approaches, but I don't think it's… really feasible to implement Algorithm L in a way that's Concurrent and has meaningfully better performance than just locking.
So that's where things stand right now.
The… the alternative to trying to implement algorithm L in a concurrent way is to run multiple copies of the algorithm in parallel, right? So… You could, for example, think, like, oh, well, if there's a lot of contention on this lock for the algorithm. What if we had two instances of it running, and you basically got Like… Put into one or the other, right?
Like, you randomly select one or the other, and it turns out that's statistically correct.
And does reduce lock and tension.
the, like, logical extreme of that is to say that actually we could just run algorithm L on each bucket. So if you have a fixed size reservoir, you've got of size K, you've got K copies of… algorithm L, and so that's what this PR is looking at.
the… I think the weird part comes in.
Here, the… or the… the main downside that I've been able to find is that In order to do this.
It's hard to do the switch.
If you round robin between each of the buckets.
which is what this PR does. There's some bias that's introduced there, so your sample is no longer truly random. Because essentially, if you round robin, it means that It's impossible for… some elements to be in the selection at the same time. So, like.
If you have an exemplary reservoir of size K, then the first element and the K plus 1th element We'll never both be selected, right?
The reason why I did that. So, one… It makes… it does have a performance.
Like, there's a performance reason to do it.
But it also makes it quite simple to implement, because there's just a single global atomic counter, and then that just repeatedly round robins over all the elements.
And inside each bucket.
once it gets collected, it just resets the algorithm L for that one. So the… the logic and, like, reasoning about it concurrently is quite… easy, I would say, compared to other approaches.
But the downside is that there's this, like.
bias that's introduced into the selection process. It's basically… it is fully random, with the exception that There's, like, disallowed combinations, essentially.
If that makes sense.
**Tyler Yahn** 10:59 Yeah, I'm still not following, like, how this is, like, Statistically valid, though.
**David Ashpole** 11:06 How it's statistically valid to run K copies of algorithm L.
So.
**Tyler Yahn** 11:17 Like, I'm still not, like, understanding how, like.
Essentially, what you're doing is you're taking Algorithm L, and you're, like, partitioning whatever that fixed-sized, like, bucketing system you have is to, like, independently have each one of those choose its next insertion point.
Like, there's a global insertion point because, like, that… that's not gonna be the same, then. Like, you choose your next insertion point based on, like.
a statistical, like, understanding of, like, where you're at and where you want to go, but if you're doing that K times, like, you're… you're not… you don't have the same distribution profile.
**David Ashpole** 11:53 So you… If you look at the paragraph, or… I have a paragraph that talks about the runtime of it, but it kind of gives… It, like, it's sort of related.
Which is that… Because the size of each individual Bucket is just one.
The num… the next numbers are not… they're… the next numbers are not as far apart. So, essentially, if you added all the next numbers together.
you would get… roughly what the next number would be for the K-sized one.
**Tyler Yahn** 12:39 Hmm… See, and that… I don't think that's true, though, is what I'm saying. Like, what you just said, like, you're gonna, like, you have a different distribution.
And if you have a different distribution, like, your selection criteria for the next insertion point.
It's going to be sooner if you're doing this algorithm, like, like, the… the width of… Of this distribution is gonna be much, smaller.
Like, I imagine it still peaked on, like, the same average, but, like, your sigmas are off here.
**David Ashpole** 13:08 Say… what do you mean by that?
**Tyler Yahn** 13:11 So, like, if you make the statistical observation of, like, where the next distribution is going to be, like, per… offset, right? So essentially, you have, like, some sort of graph of, like.
This, you know, there'll be 5… Buckets ahead, or this, or 5 measurements ahead, or this'll be 10 measurements ahead, or something like that, plot that as, like, a distribution.
And then you get some sort of, like, histogram count of where that actually is going to apply.
So that comes from, like, this W parameter in algorithm L, if I'm not mistaken. So that W parameter is going to be, like, you know, your average is going to be whatever that statistical average is. So that's going to be, essentially, as this is growing, it's going to be a fixed-sized, like, average that's going to be growing, right?
But as that's growing, like, it's gonna grow at different rates.
Because, like, you're actually choosing over a smaller sample size per bucket.
**David Ashpole** 14:08 So… I can try and work this out. My mental model is that if… Like, if… If we have N-offer calls that are gonna happen in In a collection interval.
and K buckets, right?
if I take… N over… if I take the fraction that gets put in one of the buckets, right, N over K, and I apply algorithm L With a size of 1 to that.
It should correctly distribute those across.
Like, it should give you a time-unbiased sample.
Of those for that bucket.
Right.
**Tyler Yahn** 14:55 Yeah, but the weighting's different, is the problem.
**David Ashpole** 14:58 What… what do you mean by that?
**Tyler Yahn** 15:00 So, you're… I mean, obviously, you're still gonna get a, like, normalized distribution here. Like, that… that's not… I'm not saying that, but I'm saying that, like.
**David Ashpole** 15:07 What do you mean by it?
**Tyler Yahn** 15:09 So your normalized distribution is going to also have, like, a width to it, and that width is going to be defined by, like… the statistical probability that it will actually, like, make it into each bucket. So if you have, like, K different buckets, you're oversampling, essentially.
you're, you're making this W, call K times instead of once per measurement.
**David Ashpole** 15:35 Hmm… I'm… I'm not quite following.
**Tyler Yahn** 15:41 Okay, so, like, if you make a measurement right now, it will determine if it goes into a bucket, right? If it does go into a bucket, it's going to recalculate the next time.
**David Ashpole** 15:52 Yes.
**Tyler Yahn** 15:52 a measurement is going to be put into a bucket, right? That determination of that measurement is like this, this W parameter, right? That's based on the total, like, buckets that can actually be existing, or that can exist, plus the total number of measurements that have already been seen in that particular reservoir.
**David Ashpole** 16:10 Well, yeah, in the whole reservoir, right?
**Tyler Yahn** 16:12 Yeah. That now is not going to be the same calculation if You're not looking at all the measurements that are seen for the whole reservoir, you're looking at all the measurements that are seen Per a one-bucket version of that.
So you're… you start to oversample at that point.
**David Ashpole** 16:36 Oversample, meaning…
**Tyler Yahn** 16:39 Meaning that, like.
**David Ashpole** 16:40 weighted towards the back of the… are you front-weighted or back-weighted?
**Tyler Yahn** 16:44 Replacement weighted.
**David Ashpole** 16:47 Time unbiased. Sorry.
**Tyler Yahn** 16:48 So, you're weighted to the sense that, like, you're going to be choosing more samples for measurements In this new scheme than you would have, for the other scheme. You're going to be, like, replacing.
**David Ashpole** 17:02 So you're saying that you would be… you would be back-weighted, because it would be more likely that something gets replaced.
Then that's something…
**Tyler Yahn** 17:09 Yeah, I guess… I guess I don't know what direction we're talking, but yeah, sure.
**David Ashpole** 17:13 like, basically, in a normal algorithm L1, if you… If you do it properly, then each observation that's passed is equally likely to end up.
**Tyler Yahn** 17:25 Yeah.
**David Ashpole** 17:25 in the final result, right? And so if you're replacing too often, then you'll end up So I… My mental reasoning here is that… If you apply, like, let's say that today.
We have a fixed-sized reservoir of size 1.
Right.
you can apply algorithm L properly.
in a time… Unbiased way to that reservoir of size 1.
And it… it works.
So, what I've done here… is I've… Just taken the exact… a copy of that logic, with K hard-coded to 1.
And applied it to each bucket.
**Tyler Yahn** 18:11 Yeah, you haven't normalized the problem.
**David Ashpole** 18:13 So… What do you mean by normalize?
**Tyler Yahn** 18:16 So, you have a statistical probability per bucket now, but then you have N or K buckets, right? You need a normalization factor there. Like… If you look at the… if you look at the distribution, you are not going to have, like, a normalized distribution of 1 anymore across the time-weighted average for all of these. You're going to have a normalized distribution proportional to K.
**David Ashpole** 18:35 Hmm… I'm… I'm still not following.
Okay, mate… Why… why would I have a normalized distribution proportional to K?
**Tyler Yahn** 18:54 Well, like, you have… okay, like, go back to your example where you can… you can apply this Appropriately to one size bucket.
**David Ashpole** 19:00 Great.
**Tyler Yahn** 19:01 8.
**David Ashpole** 19:01 Yep.
**Tyler Yahn** 19:02 That works great. Now, do it completely independently to another one, right?
**David Ashpole** 19:07 Right, so I have… let's say that I… I'm going from one bucket to two buckets, right? So now I'm giving… And N over 1 of the offer calls go to bucket 1, and N over… or sorry, N over 2 of the offer calls go to bucket 1, which… Whose overall count is… ends up at N over 2, and… another N over 2 go to the second bucket.
**Tyler Yahn** 19:37 Yeah.
So now, take the equivalent if you had a two-sized fixed reservoir.
Each bucket would have seen N measurements, not N over 2.
**David Ashpole** 19:47 and the… Right? And the algorithm for… the algorithm takes K into account, right? So, the algorithm div… divides the… In the calculation of W, it does. Go look at the files changed here.
**Tyler Yahn** 20:04 It's proportional also to N, though, is the problem.
**David Ashpole** 20:13 Okay, I… Proportional to N.
Can you… can you click on the files changed?
**Tyler Yahn** 20:20 Yeah, sure.
**David Ashpole** 20:24 It… it…
**Tyler Yahn** 20:34 Sorry, I don't know where I'm going to.
**David Ashpole** 20:36 Yeah, yeah, so look at the red… the red stuff that's replaced in fixed-size reservoir.
**Tyler Yahn** 20:41 Okay.
**David Ashpole** 20:42 Because this is the current implementation.
**Tyler Yahn** 20:46 Right, okay.
**David Ashpole** 20:48 Keep, keep going down a little bit.
Until we get to wherever, let's look at advance.
**Tyler Yahn** 20:59 This, yeah, right here, right? Is this what you're talking about? Right.
**David Ashpole** 21:03 So, K comes into… Account when we divide the random number by K, right?
Then we do the log, or no?
We're dividing the log by k, and then we're taking the exponent.
And then… When we do next… dot log… then next only takes into account our… W.
And this doesn't… This doesn't take the overall count into… I guess… I'll have to do the math. I still think if you take a time-unbiased algorithm for one bucket.
And give it elements that they wouldn't… It wouldn't suddenly become… time biased.
It… Like, it's hard for me to figure out why that would be the case.
**Tyler Yahn** 22:38 Well, I think that it's… it's… becoming time biased because… You're not proportionally giving each measurement to a statistically, like, random Bucket at that point.
And you're not essentially saying, like, hey, each one of these buckets could assume this measurement, right? You're saying, like, no, only you one can actually assume this measurement, so let's calculate it off of that.
So we aren't looking at any of these other buckets that are actually, like, able to assume that measurement.
And you're skewing… your calculation of W here is the problem.
**David Ashpole** 23:12 But it… in… in my implementation, I remove, like, I say, basically, cap of RDOT measurements is 1.
Right? Because we're… we're applying the algorithm, but we're applying the algorithm as if it's a reservoir of size 1.
**Tyler Yahn** 23:29 Yeah, but that's what I'm saying, like… You… Your calculation for the next insertion point for each one of those is, like, independent, but when you I agree, and then when you, like, multiply those together, like, you should have some unbiased sampling, right?
but it's not weighted correctly at this point, because, like, each one of those actually doesn't have, like, a full set of what the bucketing could be. So, what you've actually done is, like, you've got each independent one, but you aren't getting measurements from a completely random, or from a completely contiguous, like, time sampling at that point.
Like, I think… I think if you offered each measurement to each one of these reservoirs, right, and then, like.
If you offered each one of these measurements to each one of these reservoirs, I think you'd be okay.
But the problem then is that then you're gonna overcount, because you may get it actually to go into multiple places.
But the thing is, is, like, when you only offer N over 2 to… one part of the reservoir and N over 2 to the other part of the reservoir, like, you're partitioning your measurements in time.
**David Ashpole** 24:34 Yeah, well, yes.
So that may be worth saying the same thing.
Like, I don't think… I… I don't think this skews… Like, of the set of measurements.
that go to… because it's round-robining over the buckets, right? At least in the current implementation. Like, of the set that goes to a single bucket, those should be time… Like, properly time-weighted.
Are you just saying that, like.
Like, there is bias that's introduced by round-robining.
Here, right?
**Tyler Yahn** 25:12 Yep.
**David Ashpole** 25:17 But I don't… that shouldn't affect whether or not it's… it's properly time-weighted. That just affects the sets of… Exemplars that you could get on the other side.
**Tyler Yahn** 25:26 I… well… maybe not time-weighted, then maybe I'm not trying to say that, I'm just saying that, like, your scaling factor is not correct. It's not the same.
**David Ashpole** 25:36 Then, I…
**Tyler Yahn** 25:38 How can you have the same scaling factor if you don't have the same size, like.
bucket that's coming into the calculation of that scaling factor, right? Like, each time that you make the scaling factor, you look at, like, a statistical sample of, like, random numbers that are up to K, right?
Now I'm gonna take that away, and I'm gonna look at a statistical sample of N, like, equals 1.
So, I'm not… I'm not making the same calculation for W anymore. And how does that get normalized?
**David Ashpole** 26:08 Random numbers up to K. Can you… sorry, I missed a bunch of those words there, so…
**Tyler Yahn** 26:14 So, so W is calculated here, right? Is, is the max… so you take a statistical, like, random number of… values that are between, you know, 0 and 1, and then for the max of those, that's gonna become your new W, where K is equal to the capacity of the storage.
So, if I'm taking a statistical sample of 10,000 random numbers versus 1.
Like, that's a different weighting.
**David Ashpole** 26:45 But you also are getting… 1 over K thing sent to you, right?
**Tyler Yahn** 26:52 No, you're taking U to the 1 over K.
**David Ashpole** 26:59 U.
Where's you?
**Tyler Yahn** 27:02 Here.
**David Ashpole** 27:12 Oh, that's the random number computed.
So instead… yeah, so instead this just becomes W times U.
**Tyler Yahn** 27:26 Yeah.
**David Ashpole** 27:30 But that's correct when K is 1, no?
**Tyler Yahn** 27:33 100%, but K isn't one. K is… K is now split across all these different partitions, is what I'm saying.
**David Ashpole** 27:39 Okay.
K is 1 in each of the partitions, right?
**Tyler Yahn** 27:43 Yeah, but do you see what I'm saying? Like, it's not equivalent. K is one in each one of the partitions. K is not one when you holistically look at the exemplar reservoir that you were originally calculating it against.
**David Ashpole** 27:55 Right, but I'm.
**Tyler Yahn** 27:56 And it's not, like, and it's not like a linear operation that you're making here.
Like, you can't just say, like, since K is now 1, that that's fine, because, like, we were always dividing by K, so as long as these are multiplied back together, then we're all set. We're actually raising it to the power of 1 over K, so that's not a linear operation, like, that… you need to, like.
You need to bias this in some way where the weighting becomes scaled proportionally.
what I'm saying is, like, I think you can make this work as long as your calculation of the next W in each one of these, like.
Independent, reservoirs Has a different scaling factor.
And that independent scaling factor needs to take into account the full reservoir size.
**David Ashpole** 28:52 I don't think that's correct, but I'll have to… I, I can… I think part of the thing that's important here is that we aren't advancing count as fast, right? So you're not going to be computing advances off. Yeah, I don't know if we're gonna… maybe let's skip this topic, then. I don't know if we need to spend more time here.
I can try and come up with, like, a proof or something.
**Tyler Yahn** 29:22 Yeah, so, I'd like to see this test run.
Yep. With… One, and then the other, and then seeing if you get the same distribution here.
This is… this is what I'm talking about.
**David Ashpole** 29:36 I mean, that passes here.
**Tyler Yahn** 29:38 I imagine it would, because you're biasing it in the same weight as your expectations, but like… what I'm saying is, like, do you get the same numbers if you run this through with The different al- the different algorithms.
Going, like, so if you're… if you're biasing… one way, and, like, you expect that distribution to be, like, the other way? Does that check out?
Is what I'm saying.
**David Ashpole** 30:01 Like, do you want me to… I think the data is… do you want… Maybe I can flip the data?
No bucket.
Mean, so this is just checking the mean, right?
**Tyler Yahn** 30:16 And the intensity is the number I'm using here, but this is related to the, standard deviation, yeah.
**David Ashpole** 30:43 This is…
**Tyler Yahn** 30:43 Basically, this… this part right here.
Sorry, it's not highlighting, but…
**David Ashpole** 31:00 Until you… You think this would pass if the data was weighted towards later observations?
Like, if… If the earlier ones were evicted too often.
Or, sorry, yeah.
**Tyler Yahn** 31:20 Y-yeah, this should fail, if that's the case.
Well, it should fail, it should fail if that's the case. It should also fail if, like… I'm more talking about, like, this intensity factor here, right? This intensity factor is based on, like, the standard deviation that I'm looking for.
And whether, like, the normal distribution actually isn't biased.
In one way or the other.
**David Ashpole** 31:52 Distributed data.
I'll have to look at this test. I mean, it passes on this PR, but that doesn't mean that… I haven't read through this test very closely.
**Tyler Yahn** 32:04 Samples.
This passes on this PR.
Yes. And you're using… okay.
I was looking at a… differently, but this looks like it actually is using directly this new fixed size. Okay, well, then maybe I might be missing something.
**David Ashpole** 32:35 Neither of our brains are big enough, I think.
**Tyler Yahn** 32:39 No, probably not. I'm probably missing something, but, like, I… that… I would be interested to see that. Okay, alright, I can take a look as well.
**David Ashpole** 32:49 I… I think the… So that's… that's one thing that we can verify that… This is actually statistically, time unbiased.
I think the other question I came with was just.
The more basic one of, like, Is round-robining to… these sub-reservoirs.
like… Acceptable, or, do we really want this to be A completely random sample.
**Tyler Yahn** 33:27 Yeah, I mean, I think… I think he… I think looking at… I think looking at that test for particular, like, different values of the sample size, so something on the order of, like.
10, 100, 1,000, and maybe, like, a million, and seeing, like, how the distribution changes based on, like, the round robining versus, like, truly random, could help make that determination.
**David Ashpole** 33:57 The important thing is whether your data has patterns that line up with the reservoir.
**Tyler Yahn** 34:02 Yeah, yeah.
**David Ashpole** 34:03 That's… that's what changes. So if you make every kh element a million, right? Then you'll get something… That's very average, right? So you'll get… you'll always get the 1 million In one particular bucket, with very high confidence, instead of getting it, like, Randomly, sometimes once.
Sometimes, never. Sometimes, 5 times, right?
**Tyler Yahn** 34:28 Yeah, but that's, I think, I think that's pathological data. I don't think we're ever gonna get a good, like, you're never gonna… you can have the same problem here, right? Like, you can put those measurements in the right spots here, and you could always, like, seem to figure that one out.
But…
**David Ashpole** 34:45 the thing with this is that it's always… the bucket assignment is always random. So, you could get, like.
You could still randomly get all of the…
**Tyler Yahn** 34:53 Oh, I see what you're saying.
**David Ashpole** 34:54 Weird cases.
With round robining, if things are spread out by a certain number of places.
they will both get assigned the same bucket, and you could never get both of them at the same time. So it's… it's completely random, with the exception that There's a set of, like, every kh element.
We'll never end up together.
**Tyler Yahn** 35:16 Yeah, right, right.
**David Ashpole** 35:17 Right, so that's the… that's the bias, is that there are some impossible cases. Well, I think it, like…
**Tyler Yahn** 35:24 If that's the case, then, like, you'd have to… if you wanted to, like, recreate the algorithm in, like, that concurrent state, just do the random… Selection instead of the… the round robin, right?
**David Ashpole** 35:34 Right, so we… I think it's possible. It has overhead because we still need to… we still need to do all the other same… same things we were doing, like the atomic counter increments and stuff. It's just an additional call to a random number generator.
And there's some synchronization now that needs to happen between collect… like, right now, the nice thing about Round Robin is that collect is super simple. You're just, like, collect each bucket independently and reset each bucket independently.
And then the next observation to that bucket gets… Like, it's the zeroth one, so it gets populated.
Then there needs to be coordination between the… when do you switch between round-robining, which we do at the beginning, and when do you, switch to the number generator? So you, like, basically have to turn that on after you've received K observations, and make sure it gets turned off.
It… I can… if… Yeah, I can do that if that's, If we think we want to keep that, property.
**Tyler Yahn** 36:47 Yeah, I mean, I think we do.
**David Ashpole** 36:49 Okay.
**Tyler Yahn** 36:50 I feel like there's gotta be some… What is it? Maybe you could try to… I do wonder if you could use, like, an atomic here.
in… In, like, passing in that random value, like… calculate a random value and, like, just do a swap on something that holds that random value. So essentially what you're doing is you're calculating the next bucket for the next You know, insert, and then all you do is you swap with an atomic value, and whatever you get back from that atomic value is what somebody else has already calculated for you, which is also a random number.
Obviously, you need that switch point. I agree there, but, like.
**David Ashpole** 37:33 You could…
**Tyler Yahn** 37:34 You could use that as, like.
**David Ashpole** 37:34 That's fine.
**Tyler Yahn** 37:36 Yeah.
So essentially, you could be continually, like, you know, concurrently calculating random numbers as you needed, but then it's just, like, that actual insertion is managed by some atomic… As long as you don't overrun, and then there's no concurrent access to each bucket again, though, I guess that's a problem, because you can get the same random number twice, and then two Go routines could be trying to update the same bucket.
Which, again, if you're using atomics there, maybe that's fine, I don't know.
**David Ashpole** 38:02 I found that just simple locking around the actual storage was the most performant.
And also the easiest to reason about.
It's… it's more the, like, Filling up the first K after collect.
And then switching to random.
That was kind of tricky.
**Tyler Yahn** 38:23 Yeah, I mean, there was definitely an if statement before, I don't see why maybe you couldn't just, like… Do some sort of promotion algorithm, where, like, it is one, and then as it hits a certain point, it, like, has a synchronization point where the code paths completely change.
**David Ashpole** 38:44 I'll look at it.
**Tyler Yahn** 38:45 I imagine I trust you on that, like, that doesn't seem… Unsolvable, right?
**David Ashpole** 38:51 Yep.
**Tyler Yahn** 38:52 Yeah, okay.
**David Ashpole** 38:53 I can try and figure it out.
Okay.
**Tyler Yahn** 39:00 Okay, okay, anything else you wanted to talk about on that one?
**David Ashpole** 39:07 No, that's it for that one.
**Tyler Yahn** 39:12 Okay.
Cool. Well, if that's the case, there's nothing else on the agenda.
Anything else people wanted to talk about?
Maybe we could check in, Robert, with where we're at on attribute, stuff.
**Pellared** 39:27 I had not been checking myself, like, I know there's one issue regarding… Bite slices?
the PR, I'm not sure what is the status. I haven't looked at it, I think, since yesterday.
That's…
**Tyler Yahn** 39:41 Is that…
**Pellared** 39:42 If I… Go on?
**Tyler Yahn** 39:45 Was that the only thing blocking the next release, is the byte slice limit stuff?
**Pellared** 39:50 Yes, in my opinion, the only stuff blocking the release.
And also, maybe addressing some CVEs, if you… yeah.
I think Sam's, Sam's beer as well. I think if we have those two out… There was also this one regarding OTLP limits.
But still, we didn't get any answer from Felix what is the recommended size.
On… but some… but at the other side, we can also… change it in the future, but I don't… I don't feel also good changing the default limits, given it's a stable, stable package. So, yeah.
So I think there's those 3 PRs. Maybe I'll add it to the milestone.
**Tyler Yahn** 40:35 Yeah.
I think we've got… the… log…
**Pellared** 40:40 No, this is 45. It should be 44.
This is the next one.
**Tyler Yahn** 40:45 Oh, okay.
**Pellared** 40:47 Yeah, there are too many things here.
So map type, you can move it to the next one. It should not be here.
**Tyler Yahn** 40:55 Why does this only show up on some repos? I don't understand.
**Pellared** 41:01 What do you mean?
**Tyler Yahn** 41:01 Oh, I see. You can only do one at a time.
**Pellared** 41:05 Oh, that's annoying. If you want to many of them, then you need to go to other places, you need to go.
**Tyler Yahn** 41:10 Yeah, you gotta go to the issues tab, but it's like, why can't I just do… anyways, sorry, this is just me griping about…
**Pellared** 41:16 Okay.
**Tyler Yahn** 41:19 And then, yeah, it does, like, a bulk update. This is, gosh.
I've been finding a lot of GitHub, errors lately, and it's been bothering me. But, SDK implementation to do deduplication map, this also goes to 45, right? Yeah, yeah. Okay, and then… attribute string method on… to key and key value? Is this… this is blocked on the key value stuff, right? Because we have the value… oh, wait.
**Pellared** 41:45 This one can be closed. This is by, Brian, and I already, like, taken this issue.
So this one, I think, will.
**Tyler Yahn** 41:53 Right, okay, yeah, this is the original one, okay. Did you put in here the superseding PR?
**Pellared** 41:59 Nope.
**Tyler Yahn** 42:06 Okay.
**Pellared** 42:32 Gonna remove from the mice.
**Tyler Yahn** 42:35 Okay.
Apply attribute on this map, that… It goes here, All these observability ones don't block this, but this attribute limit, this is the one that we were talking about.
And I think there's a PR associated.
**Pellared** 42:59 There's the VR.
**David Ashpole** 43:00 Sam's?
No.
**Tyler Yahn** 43:02 Yeah, well, yep, we need to add that as well.
**David Ashpole** 43:06 That seems like the only one that… Has to get in.
**Tyler Yahn** 43:10 Yeah… Yeah, that definitely has to get in. I think this kind of has to get in, given what we've already merged.
**David Ashpole** 43:17 Oh yeah, yeah, true.
**Pellared** 43:19 Would you check, would you go to the bottom? Because maybe if someone has time today.
**Tyler Yahn** 43:26 what else?
**Pellared** 43:28 Not addressed.
**Tyler Yahn** 43:30 Okay, yeah.
**Pellared** 43:31 I wanted to check if my comments were addressed, but were my comments really, like, important, or not really?
Could you scroll… Yeah.
This one is… yeah.
Yeah, this one's… enforcement.
**Tyler Yahn** 43:49 Well, I think this might be a… Person trying to do these things on the weekend?
So, I think maybe if Sam's PR gets merged, we can maybe prioritize this a little bit higher and have somebody else take this on? Does that make sense?
**Pellared** 44:01 Yes, yeah.
Okay.
**Tyler Yahn** 44:13 Okay.
And then what was the other one, Robert, you had?
**Pellared** 44:30 I don't think it… there was this one for the OTLP.
But I'm not sure if it should be blocking or not.
**Tyler Yahn** 44:39 What about this one?
**Pellared** 44:39 I've seen her bike.
I don't think it's blocking.
For sure, I would not look at this PR.
This is David's issue recently about… What possible division by zero, right, David?
**Tyler Yahn** 44:57 Are there two PRs for this?
**David Ashpole** 45:01 That's some…
**Pellared** 45:02 Yeah.
Both.
**David Ashpole** 45:04 KindBot has opened multiple PRs.
**Tyler Yahn** 45:10 Okay.
**David Ashpole** 45:12 with their tokens.
**Tyler Yahn** 45:13 Great. Yeah.
What about your default aggregation? I'm sorry, your, zero with… drop aggregator switch, did that already get merged, David?
**David Ashpole** 45:25 I think that got clicked yesterday.
**Tyler Yahn** 45:28 Okay, yes.
**David Ashpole** 45:28 It would be… I do have a bug fix, actually, which I've been waiting… I have to wait till 2.45.
**Tyler Yahn** 45:37 When… which… I know the feeling. Which PR is it?
**David Ashpole** 45:44 It's already approved and stuff.
We don't have any bugs. Oh, maybe I didn't put bug on it.
**Tyler Yahn** 45:50 Mmm…
**David Ashpole** 45:51 It's just, fixed the counting of… Self-observability.
logs and spans in metrics. Right now, they're still using the length of… the number of.
**Tyler Yahn** 46:03 resources.
Yeah. So that…
**David Ashpole** 46:06 Yeah, there you go.
**Tyler Yahn** 46:07 Yeah, this one. Okay. Yeah, this is…
**David Ashpole** 46:09 Must be nice to get out.
**Tyler Yahn** 46:11 I think that's ready.
Okay.
And then… Robert, sorry, did you… did you know the other… .
**Pellared** 46:23 I know what's my name.
**Tyler Yahn** 46:25 Oh, you… it was your PR? Okay, alright.
**Pellared** 46:27 Yes, one was by… yeah, I just want to discuss if we want to make it blocking or not.
**Tyler Yahn** 46:33 Sure.
**Pellared** 46:36 Yes.
Yep.
So the problem is that we still do not have the information what should be the max maximum request size limit.
For this one.
We still didn't have the information from the profile logistic.
Profiling.
**Tyler Yahn** 46:55 Seems like… Seems like approvers here are in favor of this. What… what's… is, like, is the worry that it may change in the future, and then, like, we'll have to…
**Pellared** 47:07 Yes.
Yep. So the question is the problem for you?
**Tyler Yahn** 47:11 how can it change in the future? Like, it can go down, right?
**Pellared** 47:15 I'll stay too good up.
**Tyler Yahn** 47:18 So if it goes up, then what's the problem?
**Pellared** 47:21 I just want to double-check if it's not a problem for you. If it's not, then, yeah.
Okay.
**David Ashpole** 47:26 You can add it in the first place, then… Seems like we can adjust it.
**Tyler Yahn** 47:31 Yeah.
**David Ashpole** 47:31 Do you want to put it behind a feature gate?
That's the only other option.
**Tyler Yahn** 47:36 Yeah, I mean, that's… yeah.
Nope. And then we go through a cycle of enabling it.
Which, I mean, I'm not opposed to if you want to do that, but… That's up to you.
Okay.
Well, let's add it to the milestone.
**Pellared** 47:53 Yeah, no… Resolve the conflicts after the meeting.
**Tyler Yahn** 47:59 Cool. Okay.
Okay, well, cool, yeah, then it sounds like we've got a few more things before we go with the next release. There's, like, the observability stuff in there as well, but… That's just been bumpin', so… We can keep bumping it.
Awesome. Any other things people want to talk about, or topics?
Have people been thinking about topics for KubeCon North America?
**David Ashpole** 48:31 Yes, but I haven't come up with anything that seems particularly interesting.
**Tyler Yahn** 48:36 Yeah.
it's a good question.
**Bryan Boreham** 48:45 Not quite.
**Tyler Yahn** 48:48 You should do a deep dive into the statistics of, L-based algorithms on… Reservoir sampling.
**David Ashpole** 48:55 Actually, you should just propose it as your own.
**Tyler Yahn** 48:57 Yeah, there you go.
Exactly.
**Bryan Boreham** 49:02 Lightning talk.
**Tyler Yahn** 49:04 No, he needs a full one.
**David Ashpole** 49:05 I'd be the first. Yeah.
**Tyler Yahn** 49:06 the fault here.
No, I… yeah, that's a good question. I do think that there's, like, a lot of great talks in other parts, but I haven't thought too much in the Go space right now.
**Pellared** 49:24 David, to be honest, I'll… I'll be very happy to see a talk about all the improvements that you're doing to the metric stuff. Maybe it's only me, but… Yeah, I was thinking the same.
**Tyler Yahn** 49:36 Same thing, actually.
**Pellared** 49:37 But I remember that there was, like, I remember that CJ was also doing some talk about the performance stuff in metrics, and I heard so many people were saying that it was a great talk, that I wouldn't be surprised that there are, you know, a lot of…
**David Ashpole** 49:50 Truly.
**Pellared** 49:50 That's.
**David Ashpole** 49:52 Yeah.
Oh, okay.
**Tyler Yahn** 49:55 Yeah, I think that… Yeah, I think it's up to you. I'd be interested in that talk as well.
So… but you may have a very small audience, is the problem, so, yeah.
**David Ashpole** 50:08 I will be giving it at the GO SIG meeting.
In May.
**Tyler Yahn** 50:12 Yeah, right?
But, I mean, if you can make it applicable, like, I think at a broader, like… Yeah, it's maybe, like, other hotel maintainers that could be good for the maintainer track, if you can make it more applicable to, like, observability in general? Like, like, what you've looked at, how you've referenced it with, like, the Prometheus world, like, look at, like, across a bunch of different things, like… I think you could increase that applicability. The details, like.
you know, that's for the hardcore fans like Robert and me, but, yeah.
**David Ashpole** 50:46 Just, yep, a deep dive on… How to fight the go escape analysis.
**Pellared** 50:55 Which can…
**Tyler Yahn** 50:55 Also, wrangling complexity. Sdks are super hard, in this sense, so, yeah.
**David Ashpole** 51:03 Yeah, I mean, I've done so much work on it, I feel like I have to put in something for it.
Yeah. We'll see.
**Tyler Yahn** 51:09 Right? You get, 4 talks accepted if you count both KubeCon and, Observability Day, so… So I expect 5.
Good.
No, just joking.
Alright, cool. We've definitely descended into, Ridiculousness at this point, so we could probably end the meeting early. Yeah, awesome. Good seeing y'all. I will check back on that other PR, by the way, David, and then we can touch base on that, too.
**David Ashpole** 51:36 Sure, I've got… I know I've opened a bunch of stuff, so I'll probably try not to do that next week.
**Tyler Yahn** 51:42 No, keep going. Keep that momentum happening. Don't stop.
**David Ashpole** 51:46 Great.
**Tyler Yahn** 51:46 Yep.
Alright, talk to you later.
**David Ashpole** 51:49 Yep. Bye. Bye, guys.
