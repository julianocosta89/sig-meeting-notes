SIG: Go SIG
Date: 2026-06-18
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**Tyler** 00:39 Hey, Brian.
**Bryan Boreham** 00:40 Hi there, how you doing?
**Tyler** 00:42 How you doing?
**Bryan Boreham** 00:45 Good, good.
I can do a little…
**Tyler** 01:31 Yeah, so it looks like Robert's not gonna make it today.
Let's see… Try to find other messages in Slack.
Yeah, no news from David. I know Damien's out. I don't know if Sam's gonna join, but I'm also not seeing anything on the agenda.
So, maybe we can wait a little bit and see if folks… join enough topics, but yeah, I mean, there's a lot going on, but… Nothing… nothing specific here.
Brian, do you submit talks to, kubeCon?
**Bryan Boreham** 02:56 I did not. I, yeah, I'm gonna… steer clear of USA, immigration through as much as I can.
**Tyler** 03:09 Yeah, can't blame you. Fair enough.
What's the nec- the next EU wins in Barcelona, right?
**Bryan Boreham** 03:16 That sounds about right, yeah.
**Tyler** 03:19 Yeah, that sounds like worth going to.
Yeah.
Yeah, I think that's, like, because it's, like, in March, usually, timeframes, too, so Barcelona in March sounds pretty good to me.
**Bryan Boreham** 03:31 Yeah.
**Tyler** 03:34 Yeah.
Because you're south of England, too, right? Like, it's not too bad, but yeah, it's still pretty rainy down there.
**Bryan Boreham** 03:43 Right, right. Yeah, it's quite likely to be nicer in Barcelona, yep.
**Tyler** 03:50 Yeah, sounds good.
Yeah, you also said you had some, like, travel plans in October, right? Oh no, it was your wife's wife's birthday, that's what it was, yeah. Yeah, you couldn't travel.
**Bryan Boreham** 04:04 It was last year, maybe?
**Tyler** 04:08 Hmm, yeah, I think it was just last meeting we were talking about it, but yeah. Oh.
**Bryan Boreham** 04:12 Interesting. Oh, I see what you mean, yes. No, it's… because… There's a very… there's a very small gap between my wife's birthday and.
**Tyler** 04:21 The conference calls we were talking about? Yeah, yeah.
**Bryan Boreham** 04:23 PromCon is in Munich, which I am planning to go to, but I couldn't add the hotel one before that, because that would then… Look bad.
**Tyler** 04:34 Yeah, no, fair enough. Yeah, that sounds good. Are you talking to Munich, or is it just, attending?
**Bryan Boreham** 04:39 I think we haven't done the RFP yet for that.
**Tyler** 04:43 Oh, really? Oh.
**Bryan Boreham** 04:45 PromCon, yeah, it's kind of… I don't know, I… well, I… yeah.
I… The organization has kind of… Veered around wildly.
I think we have announced the date.
**Tyler** 05:07 Yeah, yeah, just not a RFP, yeah.
**Bryan Boreham** 05:10 Right.
**Tyler** 05:11 Oh, okay.
**Bryan Boreham** 05:13 Right now, we're trying to have an election for the Prometheus Steering Committee. I think that's occupying everyone's attention.
**Tyler** 05:21 That's going on right now, is what you're saying? Yeah.
Oh, okay, cool.
Yeah.
That's interesting. I do think we need something similar to that in OTEL, but yeah.
**Bryan Boreham** 05:33 That's hilarious.
**Tyler** 05:33 That's a whole other… that's a whole other thing. Like the GC?
No… No.
I don't think so. But yeah, that's another… that's another reading.
Hey David, how's it going? .
**David Ashpole** 05:52 Come on.
**Tyler** 05:54 Waiting for you here. I don't think we have any agenda items going on.
So I wanted to check in, see… I know Robert's not making it today.
see if any topics, are top of mind for you. I didn't have anything particular to talk about, but… Yeah.
**David Ashpole** 06:12 I don't think I have much… usually bring up…
**Tyler** 06:18 Okay, no burning PRs that need review or anything like that?
**David Ashpole** 06:22 I don't think there's anything burning.
Okay. I've got a couple out.
None of them are, like… I think most of them are pretty big.
**Tyler** 06:33 Okay.
Yeah, I think the only thing… That I saw, it was kind of like… Coming down the pipeline was that, like, a lot of the detector resource stuff that we had agreed to from the, collector stuff was coming, and the only thing that I saw, I just kept seeing, was, like, this context propagation thing, but, we got that addressed in 1PR, so, otherwise, like, those other ones look fine, I just, like, that was my only nitpick against all the other ones, so, yeah.
I did see your, like, I think there was, like, a sync, optimization PR?
As well, I haven't taken a full look at yet, but… let me see…
**David Ashpole** 07:17 Oh, the sync top map? Yep. That one's out.
And the lazy… the filter.
**Tyler** 07:26 brought us up. I'm…
**David Ashpole** 07:27 So, I think the… That one, the biggest question in my mind is still, like, like, the attributes API for it. If you remember, we ripped out, like… or we decided not to do the really big Self-contained, filtered set concept, right?
**Tyler** 07:49 Yeah. Yeah.
**David Ashpole** 07:51 we… I realized we still need something in the attributes package, because it would obviously not be okay for… the, I don't think it's acceptable if it's possible for… the hash implementation to differ between the metrics SDK Right. And…
**Tyler** 08:10 the… Right.
**David Ashpole** 08:11 And the attributes package, so we need to still have some entry point in the attributes package for this.
Now it's down to a single function.
**Tyler** 08:22 This new distinct filter thing here?
**David Ashpole** 08:24 Yeah, new distinct filtered.
And the weird part about it is mostly that it has to… like, we have to return some way to replay the filter function, and so this does it by returning a bit set, but that's, like, a very weird… It's a weird… Yeah, it's right.
**Tyler** 08:42 I was kind of wondering what this was. Yeah, okay.
**David Ashpole** 08:47 So… so that's still the crux of the issue, is like… If we want to implement this, we need a way to replay a filter against a set.
Consistently.
And so… This seemed like… Not the worst API. This seemed like the least bad one.
Yeah.
But I'm still… it's still not, like… It still feels weird.
And, like, we're leaking something.
**Tyler** 09:20 Yeah, I… the only thing the suggestion I might have is, like, I'd turn this into a distinct type.
In that way, like, it gives you, like, that abstraction allows you to, like, like, evolve.
If you needed to, like, use a different… underlying data representation, or you needed, like, an API around this, Locking this in by just returning this unit 64, like, kind of locks you in, but.
**David Ashpole** 09:49 Yeah.
**Tyler** 09:49 I haven't locked… I haven't looked… yeah, it's been a while since I looked at this, so, like… this may make the most sense. I just… yeah. That's, like, my first reaction. But, like, I mean, this doesn't seem horrible, this just seems weird here, so, like you're saying, But I think, yeah, but I think, like, if you make, like, an API around it, that it may just make it clear, right? Like, even if you call it just, like, I don't know, like, filter bitmask or something, I don't know, Bitmask, I don't know, whatever you want to call it, but, like, it helps to clarify what it is, and then, like, if you… if you do have some sort of, like, API you want to, like, start providing for it, that might be helpful, but yeah.
I don't know.
**David Ashpole** 10:27 We can provide, like, a… we can provide a function that allows you to take a set And apply the bitmask to it, and get…
**Tyler** 10:34 Yeah.
**David Ashpole** 10:35 Right, and, like, get the… Dropped and filtered ones.
**Tyler** 10:40 Right, right.
**David Ashpole** 10:41 The weird part is, like, Like, eventually this grows… To be about the same.
API size is just the, like, filtered set concept.
And so it's mostly me trying to figure out what the right balance is, because, like, this is minimal-ish.
But, yeah.
Yeah, so… I can write out a couple options and bring them to the next SIG meeting or something, if that's helpful, and we can… Can make a call.
**Tyler** 11:08 Yeah, I… I'd probably… I need to review it, honestly, like, I haven't done it.
**David Ashpole** 11:12 Yep.
**Tyler** 11:12 Yeah, I haven't done a full review, so, Yeah, I mean, in a while, at least. So, yeah, I can take a look.
But yeah, okay. I mean, I like the idea, so let's… let's keep… Moving on that one, for sure.
I'll be honest.
**David Ashpole** 11:30 Not much from me. I haven't… haven't, been super active in this SIG last week.
**Tyler** 11:37 Yeah, I did see you had, like, a work in progress for the compliant bound instrument stuff as well.
Is that…
**David Ashpole** 11:43 Still working, yeah.
**Tyler** 11:44 Yeah, cool.
**David Ashpole** 11:47 I just, yeah, I need to dig into that more.
**Tyler** 11:53 Were you able to get something that's compliant with the specification, or is it still, like, open questions there?
**David Ashpole** 12:00 I… I think it's compliant with the specification. It does a lot of things that like, to… To get it performant.
there's a lot of weird things that… like, obviously, I'm working with, like, whatever coding agents to prototype this out right now.
**Tyler** 12:22 Sure. Yeah.
**David Ashpole** 12:23 you know, it's doing a lot of stuff where I'm like, is that really necessary? That looks awful. And so most of it's, like.
trying to figure out if there's a way for us to get good performance and come up with the right, like, internal abstractions or whatever to make it not just be a ton of extra code with a bunch of, like, NEs sprinkled everywhere.
**Tyler** 12:46 So… Hmm.
**David Ashpole** 12:47 That's part of it. I did go and look at the Rust implementation and the Java implementation, and they're doing… A lot of this is less complicated, because they don't have the… They didn't… they never implemented, like, a lockless version of anything.
So, like…
**Tyler** 13:09 Right, right, yeah, because it's all, like, thread local for Rust and stuff, yeah, okay, yeah, right.
**David Ashpole** 13:13 So we…
**Tyler** 13:14 Yeah.
**David Ashpole** 13:14 You know, we have, like, this hot swapping, and all that makes implementing bound instruments way more complex, so…
**Tyler** 13:21 Hmm.
**David Ashpole** 13:22 It's possible the answer is, like, hey, bound instruments are good enough.
That, like… we don't need nearly as much… we don't need… I should say, we could keep The atomic sum, and the atomic histogram, and the atomic exponential histogram.
But ditch the… but potentially ditch the sync.map usage and the hot swapping. So…
**Tyler** 13:50 Hmm.
**David Ashpole** 13:51 like… It is… it is a nice thing that during Collect.
Right? Even if there's a collect ongoing and it takes a while.
Like, the writers aren't blocked.
Right. So you can get, like, latency spikes there.
But that's… that's the big part of the complexity that is making this harder to implement for us than it is for… for Rust and for Java, because they just have, like.
A map and a rewrite lock.
And no… and, like, they lock it while they do collection, right?
**Tyler** 14:29 Okay, I didn't realize Russ did a… That way, I thought, huh.
Huh.
Okay. Yeah, I mean, that's… that's interesting.
**David Ashpole** 14:41 Nobody else does the, like… The swap.
**Tyler** 14:44 Hot swapping? Really? Huh.
**David Ashpole** 14:46 I didn't think so.
Maybe…
**Tyler** 14:50 For some reason, I thought Java did, because they had, like, the concept of, like, this, like, storage mechanism, and so I thought that during collection, they swapped out their storage mechanisms, like, in that hot-swapping pattern, but… That's coming from, like, 2, maybe 3 years ago, me looking at it, so, like, they may have also just completely refactored that.
**David Ashpole** 15:08 I didn't actually look at… I didn't look at Java in detail. I was looking mostly at Rust.
**Tyler** 15:13 Cedar's okay.
**David Ashpole** 15:13 Who responded to my question?
**Tyler** 15:16 Yeah.
Yeah, and that's another one… I've only, yeah, only through conversations with CJO, I've never actually looked at the code for Rust, in much detail, at least, and, like.
Yeah, the way he was describing it was, like, it's completely lockless because it, like, there's no synchronization protocols there, because, like, it's all, like, thread local, so, like, you can only upgrade one map at a time. And that, like, I thought that then, like, it's during the collection.
Yeah, I guess I didn't ask about the collection. Maybe it is, like, a stop and read everything and then go back, but… I'd be, That's really interesting, because he was so, so hyper-performant on, like, the measurement time, being, you know.
**David Ashpole** 15:57 Yeah.
**Tyler** 15:58 Literally, like, 2 nanoseconds. Yeah. Like, insane numbers, that I was like, huh, like, okay, like, you're talking milliseconds at that point, but yeah, okay, like, yeah, so…
**David Ashpole** 16:08 The prototype is 3.2 nanoseconds, which…
**Tyler** 16:12 Yes.
**David Ashpole** 16:12 Like… Which is…
**Tyler** 16:14 Still not good enough for Rust, but yeah.
**David Ashpole** 16:16 Yep.
**Tyler** 16:17 But yeah, I mean, like, okay, that… that sounds great, right? Like, that… I… yeah.
Hmm. Okay.
Well, I might… I don't know, like, I'm also on board for just saying that, like.
Yeah, I guess there's, like, the correctness factor that we were worried about, but, like, if we can get something also, like, baked into the specification saying that, like, hey, like, this is how we're doing it as well, and, like, seeing if we can get some language around, like, alternate implementations, it might be helpful, but, yeah.
**David Ashpole** 16:45 Yeah, I… I'm not gonna give up just yet. I didn't spend enough time on it this week, so…
**Tyler** 16:54 Yeah, okay.
**David Ashpole** 16:56 I'll probably have something next week.
**Tyler** 16:59 Yeah, yeah, no worries. Cool.
Well, cool.
I guess if that's the case, then we could probably just end the meeting early here. I don't think there's any other topics to talk about, so yeah. Good seeing y'all. I will see you all in a week's time.
