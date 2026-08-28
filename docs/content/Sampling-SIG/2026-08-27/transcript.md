SIG: Sampling SIG
Date: 2026-08-27
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Joshua MacDonald (Microsoft)** 01:53 Hello.
Oh, wow.
**Peter Findeisen** 01:57 Hello?
**Joshua MacDonald (Microsoft)** 01:59 Good to see you all, it's been… It's been too long, looks like. Summer.
And… I see Chris.
I see Peter.
Wait a second, Chris, weren't you at Grafana a minute ago?
**Chris Marchbanks** 02:19 Oh, whoa, what the heck?
I used to be at Splunk.
**Joshua MacDonald (Microsoft)** 02:24 Okay.
**Chris Marchbanks** 02:25 years ago.
**Joshua MacDonald (Microsoft)** 02:26 How funny.
I didn't know that either.
**Chris Marchbanks** 02:28 What?
**Joshua MacDonald (Microsoft)** 02:32 Peter is also at Splunk, although I think you might still say Cisco.
**Peter Findeisen** 02:36 I entered the back door, and kind of.
**Joshua MacDonald (Microsoft)** 02:41 That's funny. Well, it could be a short one today. I do have a couple things to share, If nothing else.
So I take it you're still at Grafonicus.
**Chris Marchbanks** 02:52 I am still at Grafana, nothing has changed, except apparently I actually… it was whatever the new, like, Linux foundation, like, it made me log in, and apparently it added that. I should probably change my affiliation.
**Joshua MacDonald (Microsoft)** 03:07 I thought I'd show you, yeah. Well, I said I had at least one thing to share. I've been promising for a while that I would get some, not .NET.
And work underway, and it's not exactly what maybe we were hoping, but it's a start, and I have been involved in this, I put up a PR here. Anyone who's listened to me long enough in this forum knows I am excited about reservoir sampling and weighted sampling, and my favorite reservoir weighted sampling algorithm is Bottom K.
And, it doesn't necessarily fit together with consistent probability Sampling, but it is a viable method for fixed size samples, and I just wanted to show a little bit that we… we have this, major, like, logs capacity issue, so this has been developed for some teams that use a lot of .NET logs, and Yeah, it's a… I've described it in the past here. It's an inverse frequency weight.
That gets adjusted so that you are aiming for equal numbers or equal representivity. And… We came up with a rule about the least, sorry, the unseen weight, so what do you… what do you give the weight for something you've never seen before? Found a good answer to that, anyway. This is a logs SDK sampler that will… keep a limit on logging, and I'm happy with it, but it also means I'm developing both myself and one other coworker named Yun Ting, As .NET Sampling people, and we… we have a plan underway to start developing consistent probability Sampling as spec'd. So that's… that's coming. This is sort of our first deliverable.
That's… I didn't… I actually have… Done a bunch of… investigation into this, and it's internal work that isn't very academic. I wouldn't necessarily publish it or anything, but we do have quite a lot of evidence that this works pretty well.
So, I thought I'd share that.
No agenda required. The other, I mean, updates I might share. Updates. Mike Gold's… Smith.
Has made a ton of progress.
On the… the honeycomb adaptive Sampling logic.
We're calling it Adaptive Tail Sampler.
this point.
I am conscious that we have effectively competing codebases. I think this is healthy, actually.
And I think the… the fact is that we can use the owners of all of these to bring together ourselves, so I think… you reviewing Mike's work, Mike reviewing your work, Chris, is a good example of the community going.
And… Anyway, so I don't see conflicts.
And the honeycomb sampler has been established for so long that just seeing them share it is also very, I think, great.
**Chris Marchbanks** 06:32 Yeah, I think that part's really good. Yeah, like, it has different trade-offs, but…
**Joshua MacDonald (Microsoft)** 06:38 Right.
**Chris Marchbanks** 06:39 Seems reasonable.
**Joshua MacDonald (Microsoft)** 06:41 The other thing that I felt like catching up on is that I feel like, Yuan Yuan maybe went on a long summer vacation, Because we are somewhat stalled, and I want… to… I can rescue this. In fact, that's my pledge today, is I will pick up this PR.
The… Alright, well, that was that.
I had… That's about all I can come up with to talk about for sampling today.
Chris, got any agenda, or questions, or help I can do, or any questions we can share with Peter?
**Chris Marchbanks** 07:58 You had reviewed a PR of mine, had one comment on it. I think I addressed it.
If you could take another look at that, I can find it.
**Joshua MacDonald (Microsoft)** 08:07 Yeah, I'm… my goal has been to, like, rapidly unblock everyone who wants help with collector sampling work, and I've been… Mike has been, like, every other day, like, here's another one. I'm like, yep. And I do review them a little bit. But I've also developed quite a lot of trust for you and for Mike, so, for example, so, they're easy. Just send me them.
**Chris Marchbanks** 08:31 Cool, I will send that to you once I find it again.
Yes, it is this one.
Yeah, and that was just… where the threshold should be is now aligned in a little bit of research there. There is an interesting, and actually, there's an interesting trade-off on it that I want to make sure you're okay with.
Which is…
**Joshua MacDonald (Microsoft)** 09:07 Why don't you give me and Peter a brief rundown?
**Chris Marchbanks** 09:09 Yeah, so this is… so the idea here is limiting policies, rate limiting, like, so span limiting, bytes limiting policies.
We are trying to, report appropriate threshold values for that. The way we're doing that is… Effectively taking the bucket, which is our one second of traces that we're processing, finding how many fit in the rate… in… fit in the rate limit, and just creating the cut point there. You brought up the paper that said I should do it at the first excluded one instead of the last included one, so I switched to that.
It does work for this scenario, and I found, like, there's multiple versions of this paper, and they have this as the exact scenario.
**Joshua MacDonald (Microsoft)** 10:00 There is a ACM somewhere, SIGMOD paper as well. I noticed it yesterday.
**Chris Marchbanks** 10:08 Yeah… The problem that… The one time it breaks down is if… if the bucket size on your rate limiter is less… is smaller than the size of… or smaller than two times the size of your largest trace.
The value can be incorrect.
So this would be only really hit… Hit users who are sending very large traces that are fairly rate-limited.
And I'm wondering, like, that seems like an okay trade-off for this approach to me.
But I was wondering if there was significant concerns.
**Joshua MacDonald (Microsoft)** 10:51 So you were saying… Wait, I couldn't… wait, something's larger than… than half. Wait, say that again?
**Chris Marchbanks** 10:58 So, if there is a single trace in the batch, That is larger than… I believe it is… Half of the entire… However much is left in the rate-limiting bucket.
For this second.
Then our calculated threshold can be incorrect.
**Joshua MacDonald (Microsoft)** 11:24 Because we don't have the first excluded.
**Chris Marchbanks** 11:28 Yeah, like, you might just use up most of the budget on the very first trace, and then, like, the second one is like, oh, I'm done now, and I don't… yeah, and then you move to your first excluded trace, and, like, who knows what… if that value's actually useful or not.
like, practicat- like, pragmatically, I'm like, that seems like an okay trade-off. Users can tweak the configs if they really care.
**Joshua MacDonald (Microsoft)** 11:56 Yeah, it's just…
**Chris Marchbanks** 11:57 it, but…
**Joshua MacDonald (Microsoft)** 11:57 I wonder… this is just a thought, and the same thing happens in this PR, there's, like, it's the same algorithm, roughly, like,
**Chris Marchbanks** 12:05 Yeah…
**Joshua MacDonald (Microsoft)** 12:06 Of choosing the next plus one.
And so in this, in this code, we keep an array of plus one, essentially, so that, like, you can track something that you're not storing, it's just, like, that next value, the next randomness value above you.
so if you keep N slots and N1 just randomness value, it works, I think, although that complicates, like, the explanation, essentially.
So I… so I… so that's my only thought, is can you store a threshold that you're not… that, like, takes less space than the trace?
**Chris Marchbanks** 12:46 Where would that next plus one… I guess, where does that come from? I could take a look at your…
**Joshua MacDonald (Microsoft)** 12:51 Well…
**Chris Marchbanks** 12:51 are as well.
**Joshua MacDonald (Microsoft)** 12:53 I mean, I'm just saying, like, there's a… there's a reservoir that's got size… S, and then it's actually an S plus 1 array, or heap.
So that you're always storing the… Well, I, I see, I see how, the situation's different, because you've got these, like, variable-sized objects of traces and so on, and you're trying to fit a budget.
it's interesting how this connects with all kinds of other work I'm seeing right now. So, aside from the fact that I've just reviewed a PR that does a plus one and keeps The next element on purpose.
slightly wasting a tiny little bit of space in that case. The batch processor across OpenTelemetry is under… always under review, as the SDKs do it one way, and that collector has moved a lot on that.
And then we always find ourselves in this situation of, what do you do when one indivisible request exceeds your batch size, which sounds like what you're having, and I might just punt At that point. Cool. And, like, emit one trace, and, like… I'm not sure you have a valid… threshold, but I guess the only thinking I have there is that you can store a threshold without storing the whole trace, and then maybe your next threshold is… is there, or I… sorry, you store a randomness value without storing a trace, and then your next threshold is… your threshold is the next value that you didn't consume, or…
**Chris Marchbanks** 14:25 Okay. Yeah, I'll think about that. That's effectively what I'm doing.
And, like, it has to be, like, if there's a trace that's larger than, like, our entire bucket size, we just… or larger than our max bucket size, we throw that out right away, so we're just like, that's never gonna make it through this, we're just going to sample that at zero. So you only end up in this, like, midpoint of, like, big traces… with a small rate limit, and it's like, it's very edge-casey, but yeah, I'm happy to punt it.
**Joshua MacDonald (Microsoft)** 14:53 Yeah, I think you can just… I feel like the solution might be just to store one additional randomness value, but discard the trace associated with it.
**Chris Marchbanks** 15:00 Yeah… okay, I'll take a look at that. I think that's kind of what we're doing, because we already have that value, like, we know what our next one is.
And that's what we're using as the threshold, so I think we're doing that?
**Joshua MacDonald (Microsoft)** 15:13 Cool.
**Chris Marchbanks** 15:13 Today,
**Joshua MacDonald (Microsoft)** 15:15 then it sounds okay. Also, I think it's totally fine to just, like, when the configuration is such that you have, like, one item.
actually, the same thing happened here. I'm like, if you have one, this algorithm completely degenerates and it's not useful, so, like… you know.
**Chris Marchbanks** 15:31 Right, like, it, it, yeah.
**Joshua MacDonald (Microsoft)** 15:32 reconstruction.
**Chris Marchbanks** 15:33 Because in that scenario, like, sorry, like, we're doing our best.
Yeah. Cool.
**Joshua MacDonald (Microsoft)** 15:40 Just trying to put a link. Okay.
That sounds good to me.
**Chris Marchbanks** 15:45 Alright, that's what was on my mind, so thank you.
**Joshua MacDonald (Microsoft)** 15:50 Any last words?
Appreciate seeing you all this morning.
I think we'll… I'll be here 2 weeks from now.
The summer's over, everybody.
**Chris Marchbanks** 16:01 It is not. I am going on vacation, so…
**Joshua MacDonald (Microsoft)** 16:04 Okay, well, maybe we won't see you two weeks from now, Chris.
**Chris Marchbanks** 16:07 I will, yeah, I will be biking somewhere between Vienna and Budapest in two weeks.
**Joshua MacDonald (Microsoft)** 16:10 Nice. Very cool. Should be fun.
Well, thank you all, see you next time.
**Chris Marchbanks** 16:15 y'all.
