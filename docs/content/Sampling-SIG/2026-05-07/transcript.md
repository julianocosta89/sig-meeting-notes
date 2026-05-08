SIG: Sampling SIG
Date: 2026-05-07
Duration: 26 minutes
Zoom Recording URL: https://zoom.us/rec/share/jtSN7g4zE_zMWF5mmUtdrFizHli8ouhxZu35S7jSd7E3J9wD4wq-Cy9S8u183Q6a.K4lQm2aJ2dYljuCa
============================================================

## Zoom Recording Transcript

**jmacdonald** 05:16 Hello, everybody.
We have a recording happening. Hi, recording.
And… Will show us some notes.
Cool.
Well, let's see, has it been exactly 2 weeks? Yes.
And, let's see who's here. Hi, Chris. Hi, Peter. Hi, Atmar.
Nope.
So… I… Showed you guys my update last week. I'm just looking at last… last time, because I… I don't have much new to say.
I followed up with Yuan Yuan's issue that we talked about last time.
In order to refresh my memory.
And… Was able to give feedback. I think… The… what we realized was that Yuan Yuan was looking for a little more firmness than we have for the random bit.
And we're not gonna get it, and that's okay. Meaning to say, we have to trust the presumption of randomness.
I… went and refreshed my memory, because if you… if you don't keep your memory fresh about our sampling spec, what happens is you forget. So, the, The confusion I had crept into my head was, about treating always-on sampler, which… We have not specified should begin emitting Trace state.
Meaning, we're not gonna say, TH0 for… Always on, and that's because as I wrote in my slides.
We plan to change the default sampler.
Which was to say, to create… this default.
Which gives us a composition of composable samplers. I had sort of forgotten that detail, but the spec says it, that's fine. So, I didn't find any spec bugs.
I refreshed my memory. The only thing I found was… This one sentence says that that Always On will do what I just said it wouldn't, and I think that's not true.
I had said something about how the SDK spec maybe was missing something about randomness.
sorry, erasing invalid thresholds, and then I just had to re-read it all. So all I'm saying is I had to re-read it all, and it made sense again.
And there is supplemental guidance on how to… on when to conceal, The randomness, if you're making random decisions not based on on the randomness in the trace ID, or the explicit randomness value. That's just a summary of what I learned by following up.
last week.
And I'm sort of just narrating. I don't have much agenda today.
I would invite Chris to see if he's got any updates on sampling collector stuff.
And the only other news I have before I pass it off is that I'm going to visit my headquarters in Seattle next week, and I'm going to press for a .NET sampler implementation when I'm there.
So that will be my… my promise to talk about… actually, second promise is I don't want… I can't make this meeting in two weeks, because there's a summit, observability Day, and I'm going to be talking, so I won't be here.
So that's my news. Will… Press for .NET SDK work next week.
And make it to the… May… 21, meeting.
That's my update.
Anything, Chris?
**Chris Marchbanks** 10:02 I don't have too much, I'm mostly hoping to… I'm hoping to get some of the trace, or… Basically the changes that went into probabilistic sampling into the tail sampler as well, so that, like, so that if you're using a probabilistic… Tail sampling, you will also appropriately set threshold and… But I need time to be able to do that, so we'll see when it actually happens.
**jmacdonald** 10:30 Let's talk about it a little bit. Yeah.
I… I've spent at least, like, one kind of week of free time, sort of, over the last year and a half, maybe, picking at that code.
Doing, like, hackathons on it and so on.
I remember feeling that it was… going to be a major project to do.
And it was requiring several, like, design steps, so I kind of remember, like.
There being… there's a 30-second… like, let's say there's a 30-second window And… If you run out of trace Trace capacity during that time, you begin ejecting data kind of arbitrarily.
And my, my attempt, the way I phrased it, or focused on it, was to, make another parameter, which was, like, a slice, a number of slices, to divide up the future.
into fixed, shorter segments of time. And then… and then each time.
Would re… would re… would… each time window would keep us separate.
threshold calculation, which is… Which is… which is to say, like.
and we've talked about adaptive sampling, or, you know, in general here, so, you could make it a reservoir. There's lots of ways to do this, I think, anyway, but the structural challenge was that there's a lot of code there, and it's.
**Chris Marchbanks** 12:11 There's a lot of code there, yeah.
**jmacdonald** 12:13 And I think when I… when I first spoke to Sean Porter about it, he was sort of like, maybe we should start a new codebase. I mean… That's also not so… sounding very appealing either, but…
**Chris Marchbanks** 12:25 Yeah, and I think, like, that ship's probably sailed, like, there are enough people using the tail sampler as is that I… It would be a very challenging migration.
**jmacdonald** 12:36 Yeah, I agree.
**Chris Marchbanks** 12:38 Yeah… I think it's… I think we could make… I'm hoping that we could make incremental changes, and like, maybe it will work only in some scenarios.
We actually… we don't run with the dropping traces, like, there's two options, like, you can drop or you can block.
**jmacdonald** 12:59 Mmm.
**Chris Marchbanks** 13:00 And we almost always run with blocking instead.
Which is like, okay, we'll provide some back pressure, it allows us to scale things up.
As we need to, but we… so we don't run into the randomly dropping traces issue in that case.
**jmacdonald** 13:18 Not know that.
That's interesting.
**Chris Marchbanks** 13:21 Yeah, I think there's some improvements for what we could do with the dropping traces as well, or the blocking… the blocking traces of workflow.
Yeah, so, like, that helps a lot with the, oh, we're just randomly dropping.
Recent changes, we actually do… we effectively have one-second batches of traces at this point, or of the decisions.
So we could definitely track, like, oh, I've dropped this many out of this batch, and incorporate that. It's hard to say, like.
Would those have been sampled or not? Because if they're dropped, we just don't know.
**jmacdonald** 13:58 Yeah.
**Chris Marchbanks** 13:59 I'd have to think about how the math works out on that.
**jmacdonald** 14:02 And then there's a few other hand-wavy things going on, which I'm okay with, like, you put the trace into a bucket for finishing when it expires.
but you start the timer on the first arrival, and you don't even know if you have the route yet, or something along… like, I'm waving my hands right now, but that stuff is, like, secondary to me, but also sort of, like, another reason why you have this fog of confusion, when you're… when you're looking at that code.
Yeah.
**Chris Marchbanks** 14:33 Fair. So I think we could probably make progress. It might not work perfectly for all cases. I'm most… Like, it would be a pretty big change to, like, rate limiting, and those sorts of things, and then sub-policies is the other area.
That… like, in my… yes, I've also spent a few days looking at this and trying to figure out where all the sharp edges are. Like, there's some, like, the sub-policies get a little… I haven't figured out if the math works correctly for those or not, either.
**jmacdonald** 15:05 I remember thinking through it a bit, and there's a feature flag that needs to be taken out. Like, like, old code needs to go away, and maybe it hasn't yet.
But the feature flag was, Making it, like, a very strange interaction with drops and inversion.
**Chris Marchbanks** 15:26 Yeah…
**jmacdonald** 15:27 This is one of the features that makes that code impossible to understand, basically.
**Chris Marchbanks** 15:31 Yeah, I deprecated it and swapped the default for that a while ago, so I think I could remove it at this point.
**jmacdonald** 15:36 Oh, good.
**Chris Marchbanks** 15:37 I think it's been long enough that I could remove those. And yeah, that'll be a really nice cleanup.
**jmacdonald** 15:43 Cool.
**Chris Marchbanks** 15:43 So, maybe I'll just start.
**jmacdonald** 15:44 Cause then… Because then I think the question comes down to, if we just have the kind of classic AND and OR, and probability, and attribute filters, which is sort of the stuff of OTEP 250.
which is the composable sampler logically, then we're almost in the same place as an SDK, and we can follow all the rules that Peter, you know, wrote down and stuff, but it's not quite the same.
why is it not quite the same? It's not quite the same, because I can't even say why it's not quite the same.
Well, for all the complicated factors I've just described.
**Chris Marchbanks** 16:27 Yeah, there are some complicating factors, but, like, I think, like, I think it's possible, because, like, the patterns are similar enough that I think it will be possible.
And Peter convinced me that it's definitely fine just to… For things like latency policies, just… Keep the same threshold it came in with.
And all of that'll work properly.
**jmacdonald** 16:49 Cool. And so then you have this, like, short slice of time where you're saying, I want 50 traces per second, or whatever. Yep. And, when the 51st one arrives, if you block, that sounds good.
If you don't want to block, then… I think there's a couple of technical questions here about how you adjust threshold, and I… I would have to go back to my old notes and think about it for a minute to say anything more intelligent.
**Chris Marchbanks** 17:21 Yeah. I will give that some investigation slash thought as well, because, yeah, I was very much looking at our blocking use case so far.
**jmacdonald** 17:29 D, Chris, are you familiar with this paper that Atmar shared for us? It's called Adaptive Sampling, it's published in the last few years. Adaptive Threshold Sampling, I think.
**Chris Marchbanks** 17:42 I would have to look.
**jmacdonald** 17:43 I feel like that was trying to give us an answer, and I had to… I keep… I had to read it again a couple times, but it was, anyway.
I feel that I have some confusion over well, choice of… What exactly you do.
in that bucket, with threshold as… You need to… you know, drop something. And I think the answer we have is you drop the thing with the lowest Highest randomness value.
And you eventually get to the point where you have 50, and that threshold is your new threshold.
and the math behind that is, like, really cool and also confusing.
But I feel like there's still some uncertainty in my head. That's all I got.
**Chris Marchbanks** 18:34 Cool. Do you have a… another… is that linked to this paper in the notes somewhere?
**jmacdonald** 18:38 it. You can also, yeah, I'm sure it's in the notes somewhere down, and, I'm sure we can Slack… find it in Slack, too. It's been discussed.
**Chris Marchbanks** 18:45 cool. It's like, Google found me something from 2017, which is definitely possibly what it is.
**jmacdonald** 18:50 No, I feel like it was a 2024-ish type of paper, but we can find it. Anyway, I thought it was quite enlightening. I would have to go read it again.
But it was connected with the same topic.
**Chris Marchbanks** 19:03 Okay, great. Yeah, I will go read through that. Oh yeah, this looks… This looks similar.
I'll go find it slash read through it.
**jmacdonald** 19:14 Very cool.
Anybody else want to say anything?
No need to.
I… I appreciate you all. I like having short meetings. I sometimes feel nervous having this meeting without, like, a great deal of agenda. So, what I propose is we're done. I can't make it. We'll meet again in a month.
If… would be good for me.
Hopefully I have some news on .NET, hopefully Chris has some great stuff to share, and thank you all. Be on Slack.
**Chris Marchbanks** 19:49 Cool.
**Peter Findeisen** 19:49 Thank you all, bye.
**Otmar Ertl (Dynatrace)** 19:51 Thank you, bye.
