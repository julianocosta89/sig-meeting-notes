SIG: Go SIG
Date: 2026-01-29
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/UUQ-ZpURlPKz-16ZM2pAKDhX0dVyL4nVNg2GAFGIkEVyOmzSCrp35hh44wjM4jGU.ABETw_gENdnpqnMs
============================================================

## Zoom Recording Transcript

Sonal Gaud 00:00:32 Hello.
Pellared 00:00:37 Joe, how are you?
Sonal Gaud 00:00:40 I'm good, how are you doing?
Pellared 00:00:43 I'm fine.
Where are you located? What's your time right now?
Sonal Gaud 00:00:49 11.30 at night.
Pellared 00:00:52 Nice, yeah. That's what I thought that.
Let's prefer the event.
Not earlier, but later than for mine, because for me, just 7.
Sonal Gaud 00:01:05 Okay.
Tyler 00:01:23 Hey.
Pellared 00:01:27 Hello there.
Tyler 00:01:31 How's it going?
Thumbs up.
David Ashpole (dashpole) 00:01:37 Did you guys get any snow up in Seattle?
Tyler 00:01:41 This is just the…
I'm in Portland, but we got no snow. Well, we got, like, a few flurries. I heard you guys got, like, 2 feet.
David Ashpole (dashpole) 00:01:51 Yep.
I… my back hurts.
Mostly from all the PR reviews, but, you know, also the snow.
Tyler 00:01:58 Yeah, right, yeah.
No, no snowblower for you?
David Ashpole (dashpole) 00:02:04 No, no, I…
Tyler 00:02:05 No.
David Ashpole (dashpole) 00:02:07 I really wanted to get an electric one, and then I heard that they were not very good, so I was like, I'll just get a really nice shovel.
Tyler 00:02:12 Yeah.
David Ashpole (dashpole) 00:02:13 And that's what I have. A really nice shovel.
Tyler 00:02:17 Yeah, I think the nice shovel works out here in Oregon, where you get, like, one or two snowstorms, and snowstorms are, like, at most 6 inches. Yeah, I don't know how I would do…
Two feet all the time, you know, that'd be horrible.
David Ashpole (dashpole) 00:02:32 it's… I don't think it's all the time. I feel like this is the worst it's been in, like…
At least 4 or 5 years.
That's true. Yeah, that's definitely true.
Tyler 00:02:40 Is it still pretty cold there, or is it starting to melt?
David Ashpole (dashpole) 00:02:43 When I biked in this morning, it was, I think, 8 degrees out.
That's funny right now.
Tyler 00:02:51 Yeah, so that's gonna stick around for a while.
David Ashpole (dashpole) 00:02:54 Yep.
Tyler 00:02:56 Oh, dude, that's rough.
I'm actually, yeah, I'm impressed you were able to make it into the office, though. That's… like, on a bike, too? That's kind of, like, crazy.
David Ashpole (dashpole) 00:03:06 It was a little scary on Tuesday, right after the snow, but…
Tyler 00:03:09 Yeah.
David Ashpole (dashpole) 00:03:10 A little bit better, though.
Tyler 00:03:12 Do you have, like, studded tires, or you just, take the spills when they happen?
Oh, okay, alright, yeah.
David Ashpole (dashpole) 00:03:18 don't help when there's big piles of snow, just when there's ice.
Tyler 00:03:23 Yeah, right, yeah.
I used to… I went to college in, Colorado, and, like, yeah, I remember, like, riding home on… in the snow. It was just, like… you'd be going around a corner, and you'd be like, oh, this is, like, fine, and all of a sudden, just, like, ice would just hit, and you'd just be, like, just sliding. Like, there's just nothing you can do, like, at all. Like, you just… yeah, it's just what it was, yeah.
David Ashpole (dashpole) 00:03:45 Yep, but, yep, no.
I haven't fallen yet, which is good.
Tyler 00:03:49 Wow.
David Ashpole (dashpole) 00:03:49 In parts where it's, like, pretty…
You know, like, you can feel the snow, stuff slipping.
I'm sure it'll.
Tyler 00:03:57 eat out a little bit, like, yeah.
David Ashpole (dashpole) 00:04:00 Yep, yep.
Tyler 00:04:01 Yeah.
Well, cool. Let's see, we're at 3 minutes. I see, Sam, good to see ya. We got David, Roberts, Sanal… I don't think Damien's coming today, so we could probably jump in here. Yeah, I'll start sharing my screen. If you haven't yet, please go ahead and add your name to the attendees list.
If you have agenda items you want to talk about, go ahead and add them there as well, and yeah, let's… let's jump in here.
David Ashpole (dashpole) 00:04:29 I'm also happy to move mine to the end, because I don't know how long.
It'll take, but… Doesn't look like there's too much else, so we can… yeah.
Tyler 00:04:38 Yeah… I think…
It might be… I think, I think we got plenty of time. So yeah, let's, let's talk, let's go through. So yeah, let's jump in. So, yeah, David, you want to talk about API and SDK performance? And I'm guessing this is the…
David Ashpole (dashpole) 00:04:59 Yep, so this is the issue. There's two topics I thought would be, like, maybe interesting to introduce to the broader group.
And then, I know we haven't discussed anything since Friday, so, we can also continue, like, if there's anything else, but…
the… The high level is…
I started working on this issue because…
I found that if you followed our contributing guide,
And in the case when you don't know the attributes ahead of time.
you end up having to call attribute new set a bunch, and, this is a little bit… or it's, like, slow, at least compared to the existing metrics SDK, right? So, this is what I started out trying to figure out, is, like, is there a way for us to…
either eliminate having to call attribute.new set entirely, or a way for us to make this faster. And I've investigated a bunch of different things, but I think the most helpful place to maybe start out
Or actually, I'll…
put the question to you, Tyler. Do you think it would be helpful to discuss the benchmarks themselves first, or would you rather discuss, the topic of
Caching in the instrumentation layer.
Because I think those are two…
two sticking points, and I'm not sure which would be helpful for us to resolve first. So what I've done, right, is I have a PR with benchmarks where I've essentially copied what we have in our contributing guide and pasted them in a benchmark, and that's what I've been using to try and evaluate all of the
the various prototypes I've made, right? So, there's that one,
And we haven't… I think we've been having some arguments
Tyler and I, back and forth, I guess, about whether the benchmarks really reflect the, like, correct usage of our APIs, or whether they
Are, like, a suboptimal usage of it, right?
And one topic that has come up here, in the discussion is, like, well, what about caching the attribute sets in instrumentation libraries?
And so, yeah, so that leads us to, like,
the question of, like, can or should we use caches when we're writing our instrumentation? Like, should OpenTelemetry's HTTP instrumentation have an attribute set cache in it? Like, is that okay? Is that something we would actually do? Or is that, like, does that not really reflect
the real usage of our APIs. So I think those are the kind of the questions before the group, and I'll…
I've left my thoughts on caching. I…
I'm not a big fan. I think there are use cases, but mostly…
not for, like, generic instrumentation libraries. I think it's most useful if, like, you're writing instrumentation for your own application.
and know, you know, that you're not going to be… or that you're using the SDK, and that you're not going to be using certain features, or you don't value those features highly.
Tyler 00:08:09 Yeah, I mean, I can jump in here if no one else wants to say anything. I was hoping…
There'd be some other thoughts, but maybe people are still digesting this.
David Ashpole (dashpole) 00:08:17 Yeah, I don't know if one… was that hard to follow? Sam, or… Robert.
Pellared 00:08:24 Maybe that was too much ground. I think… no, I think it was just an introduction. I'm not sure if you want to have any answers here, because, you know,
My thoughts are, like, I don't know, are we exploring to have some, I don't know, API for some convenient pool on the SDK side? That, for instance, instead of people, you know, just writing their own caching.
Which will be very, like, you know, instrumentation, providing something which will just be easier, and people will just use the pooling and caching, like, opt-in the way they want to do it, because anyway, it will be on the… whenever it is, whatever package, it will be the same memory, right?
So, it's… I think it's just more about convenience, but I have not seen any PR proposal, and I'm sure if I… Okay. If I'm…
My faults are, you know, in the correct way.
David Ashpole (dashpole) 00:09:13 So I, I think…
Tyler, do you think it's worth introducing the… I think the two proposals that we're really considering are the bound
Instrument proposal and… Like, something where someone would use a cache. Is that…
Do you think that's correct, Tyler?
Or do nothing.
Tyler 00:09:37 That's been my…
David Ashpole (dashpole) 00:09:38 Do you feel like that's accurate, or…
Tyler 00:09:43 So, I definitely think… so, yeah, like, I do think the…
So I definitely think that the Bound Instrument API has value. I don't think that, as it's proposed here, as, like, with a method, is… is gonna work in the long haul.
But I do think that, like, having a bound instrument API is gonna work, and so I guess… I don't know if I'm, like, misunderstanding, like, the discussion, but, like, I think that, like, it's worth discussing this API edition, like, the functional element, like, the feature element of this API edition, like, I think is…
is definitely worth investigating and pursuing, right? I definitely think there's value here. The,
The thing, though, is that, like, I think that…
I do, I do think… so, yeah, the caching thing is a little bit amorphous, right? Because, like, it's kind of a, a windmill, almost. We're tilting it, because, like, there's not really a good example here. But I do think that, like.
even if we have this API, like, even with this, like, particular method, we need some sort of, like, additional extension to, like, prevent allocations on certain code paths, right?
And I think that… I think whatever…
that says to me that, like, there is… there is a need for something external to whatever the metrics API is to help users write performant instrumentation. So whether that is, like, some sort of additional caching layer that we hold outside, whether that is some sort of, like, sync pool that, like, we help users manage.
For a whole host of other things, like…
I think there is an… there's, like, an abstract other layer to write imperformant instrumentation that it sits on top, like…
if you take a look at our instrumentation for what we've done internal to the Go SDK, like, every single one of them has pools.
They don't have any maps, but, like, yeah, maybe that's also, like, I think that's the question is, like, you know, there's the windmill part, like, what does that actually include, that additional, like, abstract layer? And, like, is there a way to, like, make that more…
you know, easy to use and approachable, I think is a good, good question.
So, like, I think that there's… yeah.
I, I do, so… Yeah, maybe just to back up, like, I, like…
I also don't want us to get lost in the… in the… in the trees here, because I think your point around, like.
the performance of the metrics API, like, just kind of a backstory, the performance of the metrics API was always one of those things where, like, we knew there was going to be trade-offs here, especially in the initial design, like,
A lot of discussion went into this, right? Like, a lot of discussion went into our option type, and, like, these benchmarks, and that kind of thing, right? And, like, we definitely had this discussion multiple times before, where people are saying, like, if you use these options very naively, they can be very inefficient, right? And the thing was is that, like, we've always looked at it like, yeah, that's true.
but you can also use these extremely performantly, and it's… it's pretty… pretty performant if you use them performantly. Like, if you try to do some sort of, like, memory management on your own.
Yeah, like, that'll work. The question and the criticism there is, like, that's not… that's not native, like, and that's not, like…
the API doesn't lend itself to use those things in that performant way, obviously, right? And so, like, you have a lot of users that come into that situation where they're not, maybe, super performance-minded, they use it naively.
And they throw up their hands, saying, like, well, this thing sucks. So… yeah, that's completely valid criticism. It was something that we looked at initially and said, like, let's take a V2 on this and take a look, another look at this. So, like, we're… we're there, right? We're taking another look at this API at this point.
I do think, though, that, like, we need to… constrain the…
I mean, not constrained. Maybe we need to direct the conversation around, like, trying to support the API as it's designed, and trying to see if we can find performance improvements in ways that are, like.
idiomatic of Go and useful for users, I think is kind of my goal here. So, I'm happy to look at the benchmarks.
Benchmarks, I think, are great.
But I think that we also want to, like, I think…
I think it's helpful to look at the naive approach. I'm not saying it isn't. But I also think it's helpful to look at the performant use approach of the API and evaluate that with, like, whatever we come up with, right? Like, because…
that's what I've done in the past, like, I have a few other, like, wrapping prototypes around this, around, you know, all these other things, and I've evaluated them, and, like, it's kind of like apples and oranges eventually, because you start to look at, like, well, you can use this optimally, but, like, you could always do the same thing, like, on your own, right? It's just, how easy is it to do it on your own? And so I think…
you know, long way… long story short, I think, looking at this.
functional element is going to be something we should do. I think we should also look at the functional element. I think it's a yes-and. Like, we need to look at a functional element on top of this for how you would store this.
We talked last time about potentially deprecating the attribute set in the attribute package, and looking at a reimplementation here.
I'm not opposed to that.
David Ashpole (dashpole) 00:14:48 I actually think we could do that,
Regardless of what happens here for ergonomics?
There is no performance benefit to using attributes set, in… if you're doing things optimally. But I think that's maybe a separate… but a smaller topic that we can agree on.
Tyler 00:15:09 Yeah, I… I… I think you're right. I think it could be… I think it could get tied into that caching layer, though, that we're talking about, because if…
Yeah, go ahead.
David Ashpole (dashpole) 00:15:21 Maybe. Is it okay if I bring up caching and some of my,
my issues with it, because I think that's our point of disagreement. Is that okay now? Or do you have anything else you want to say on, like, the general
Framing of this.
Tyler 00:15:38 No, I mean, I… Yeah, go ahead, I have…
David Ashpole (dashpole) 00:15:42 If you can help me with caching either, but go ahead.
if you can jump to the improved performance, it's more than I'm just not happy with it. If you can go to the improved performance issue.
Tyler 00:15:54 Oh, okay.
David Ashpole (dashpole) 00:15:55 And just go to the latest comment.
So I've… I've tried to write down, like, what I think The flavors of caching that…
we could try and apply R, and why I think
at least for the general case, why I consider this much different than using sync pools, right? So a sync pool is, like.
I ask for an item from the pool, I give it back when I'm done, and if the Go Runtime wants to, it can reclaim that, right? So…
Tyler 00:16:23 There's no, like.
David Ashpole (dashpole) 00:16:25 There's no permanently stored thing that exists there. I think having a map with keys that are based on
Sort of the, like, say, the cardinality of your telemetry.
is a very different thing to me. So… Like, for example.
That, the specification explicitly forbids us from…
keeping state in the API, right? And we don't keep state anywhere in the API.
Right? Because the whole idea is that if someone doesn't use your SDK or uses a different SDK, that they shouldn't end up with a bunch of states stored, right? So…
like, from my point of view, if we start telling our users that they should use a cache in their instrumentation, then even if they have a different SDK, or if they use attribute filtering, or cardinality limiting, or anything, like.
we could, like, maybe weirdly reimplement those features in the API, but…
Or in the instrumentation, but it seems like we're…
we're not at least going by the spirit of, like, your instrumentation is meant to be stateless, right? That's my issue with the caching approach. I think if you're the person who has written the application.
and you don't… and you know exactly what SDK you're using, like, this is maybe a very useful trick today, but I don't… I don't consider this the same class of solution as pooling.
Tyler 00:17:54 Gotcha.
David Ashpole (dashpole) 00:17:55 Okay, so I, I think…
from my perspective, that's maybe, like, where our disagreement comes from, and that's why I've written the benchmarks the way I have in
And stuff like that. I don't know if that…
Helps clarify, or if you want to think about it, that's also fine.
Tyler 00:18:12 Yeah, I…
Yeah, I mean, like, I think you're… like, I think it's fair to say, like, providing this, like, the sync map, like, some sort of wrapper around the sync map in, like, the metrics API,
Yeah, like, that's fair criticism of not… and reasons why to not do that.
Having, like, a helper package that did that for you.
David Ashpole (dashpole) 00:18:43 Like, telling our users to do the thing that we're not allowed to do, Like, also feels like…
Kind of funky to me.
For example, you would never do this with OpenTelemetry HTTP, right?
Or would we?
Tyler 00:19:02 I mean, I think we would.
Pellared 00:19:05 I would agree as well, I would use it as well.
Is it stable.
It's stable.
Dr.
David Ashpole (dashpole) 00:19:12 I mean, but…
Pellared 00:19:13 What's the… what's… What's the difference between having, you know, the caching
in package A versus package B, if both of them have stable API for the user perspective.
David Ashpole (dashpole) 00:19:25 It just means that if I use your instrumentation library.
and I, for example, use a different SDK,
That doesn't keep any state at all, like, let's say it writes to…
Josh, or it's eBPF ring buff, or, like, shared memory ring buffer, or… it does something wacky, like…
Pellared 00:19:42 If you're.
David Ashpole (dashpole) 00:19:43 Sure, Vice President.
Pellared 00:19:44 You're now, like, storing a bunch of state.
We can always.
David Ashpole (dashpole) 00:19:47 I mean, perfect.
Pellared 00:19:48 later.
I mean, if… right now, we are already having the state in the autoHTTP So it doesn't make…
David Ashpole (dashpole) 00:19:57 not winning.
Pellared 00:19:57 worse.
David Ashpole (dashpole) 00:19:59 We don't have the.
Pellared 00:19:59 Stop, okay.
I'm listening.
David Ashpole (dashpole) 00:20:02 We don't… If you have… If you have, for example, a…
And, like, let's say that you've turned on HTTP path somehow.
You've, like, written a wrapper, shoved it in a labeler.
you've got an HTTP path back on your metric?
And you use…
Pellared 00:20:21 Hey, love.
David Ashpole (dashpole) 00:20:21 like…
If you use a no-op, we can check enabled, right? So, if you're using a no-op, but let's say you're using the SDK with attribute filtering, right? Your cache will blow up.
But your SDK will be fine, because it has features to deal with cardinality.
So that's, that's my criticism, is like, We…
From my point of view, we're not…
We're trying not to keep state.
in the instrumentation layer, and that's why the API is stateless.
Okay, that's… that's my point of view, at least.
Tyler 00:21:11 Yeah, I don't know if it's waiting on me, but I mean, I think that there's… Okay.
I think that there are still ways you can write instrumentation to handle this.
In the ways that you're talking about, like, all these edge cases, like you're saying, like, you would recreate them in this additional package for state handling.
Whether we want to use them or not, I guess, is…
I don't… like, I think that that's… I don't know if it's… I don't know if I'd say it's completely off my radar of something that we would want to provide.
Whether it's configurable, whether you want to, like, make the hotel HTTP stateless, whether, like, I think that there's ways that we could look at that.
If it's gonna optimize things.
But for the sake of this conversation, let's just go in that direction, saying that, like, we don't want to have state in the API. Like, I don't think you've reached your conclusion here, David, so let's continue on.
David Ashpole (dashpole) 00:22:05 Mike, my… I guess, like… To take a step back, like, my…
my, like, meta-read on this has been that we disagree about the benchmarks that accurately represent, like, performant usage of the API and SDK together, right?
This whole discussion about whether, like, is caching a valid strategy for…
the metrics API SDK, and my… my current opinion is that it's not, like…
There are niche use cases where it is acceptable, but, like, for the general case.
that I've been interested in. It's not a solution.
And… which is why I've written the benchmarks the way I have. And why, like.
You're right that… a lot of the PRs, the prototypes I've written.
end up using some caching inside the SDK, right, as a way to achieve better performance.
And from my point of view, that's actually the correct place to put the caches, if there are going to be any, because the SDK is, like, the thing that's supposed to deal with state. So, like.
My hope, my goal, is to first agree on the set of benchmarks.
And then we can go propose things, and we can argue over, like…
What the right ergonomics are, and if the decision at the end of the day is, like, we don't want to do this because…
like, we don't think the trade-offs are worth it, then that's fine. It's just…
from my point of view, it's been hard to get past, like, settling on the benchmarks. That's it.
Tyler 00:23:36 Hmm.
David Ashpole (dashpole) 00:23:36 Does that make sense?
Tyler 00:23:38 Mmm, yeah, I think it does. Okay. Yeah, sure. So, if we go, if we go back to…
Yeah, that helps.
Are these… the benchmarks, like, do these need to get changed in any way? Like, these, like, I think these are what you're saying, like, what we want to agree on is,
What you have here, like, the current usage here, right?
David Ashpole (dashpole) 00:23:58 Right, so this is based on… Can I just…
Pellared 00:24:01 I would just give one… one feedback, which I hope will support you, David. So, when I was working on Log's SDK performance, for me as well.
My main motivation was the end-to-end benchmarks.
are the ones that show the, you know, the most optimal things, because sometimes the microbenchmarks can hide away this caching, which users will need to do in order to have, you know, the highest performance, but I also try to
Make the calls in a way that represents 90% of the, you know, of the ways that people would instrument the code.
So, yeah.
It's just worth making sure that these benchmarks
are really, you know, are not very HKC, or if they're HKC, just to mark them as well, you know, just to make sure that there are some benchmarks which just show, you know, that something is lower, but we do not need to
Maybe we do not care about, you know, this kind of few benchmarks, because there are edge cases, and you need to know that there are, you know, a lot of people locations in this, but it might not be a problem.
David Ashpole (dashpole) 00:25:05 Yeah, so…
Tyler 00:25:06 I think he's done that, though, here, so I think that that's… Good to say, but… yeah.
They're all integrations throughout the entire system of, like, the API through the SDK, right? So… Yeah.
David Ashpole (dashpole) 00:25:20 I think the only open question was, like, or other than the thread that we have, the only open question is where to put it. It's in its own internal
thing, because it's meant to be end-to-end.
It could be in the SDK, but… It… It really, like…
It's mostly trying to answer, like, the, like, attribute plus…
metrics API plus SDK, what does that look like, in terms of performance? Or, like, when they're used together, right?
In various ways.
So I… yeah.
I don't know if.
Pellared 00:25:56 Yeah, that.
Tyler 00:25:58 Oh, it's in its own module?
David Ashpole (dashpole) 00:26:00 Oh, I don't care. So I… Tyler, I recall you having objected to putting this type of benchmark in the SDK before the Metrics SDK, which is why I stuck it here. If you'd rather put it in the SDK, that's totally fine by me, but…
Pellared 00:26:15 I will put it in the SDK.
Tyler 00:26:18 Okay. I think I was more…
Pellared 00:26:20 Maybe also.
Yup.
Maybe just some end-to-end, just to have, you know, the separation between the…
David Ashpole (dashpole) 00:26:26 Yeah, okay.
Pellared 00:26:27 these end-to-end benchmarks, just because most of them are really micro-benchmarks, and maybe I… I'm not sure… Dave, you can take a look if I have something in the logs already, but I have a gut feeling that I have removed, and it was only my prototype, that I was scared because of the opinions.
What's your position?
Now try again!
Tyler 00:26:49 Yeah, I don't remember the exact conversation, so I may be missing, but I think I was more…
In those conversations.
David Ashpole (dashpole) 00:26:55 all the way back when Josh McDonald was contributing, so I don't think…
Tyler 00:26:59 Yeah, I… that's what I'm thinking of as well, but I don't think it… those benchmarks included things like this, was my problem.
David Ashpole (dashpole) 00:27:05 And so… Okay, yeah.
Tyler 00:27:06 This was, this was more, like, I wanted to see these things, and…
That was the point of contention. But the location, I don't…
Yeah, sounds great. Put them there.
David Ashpole (dashpole) 00:27:17 Okay.
Tyler 00:27:18 Yep.
David Ashpole (dashpole) 00:27:20 Alright, that's it for my topic then, and I'll wait… I'll wait to argue for other things, or unless you want to.
Tyler 00:27:27 I do want to talk about that API decision, but let's… let's maybe… how about… yeah, can we…
I do want to also make sure we get to this, because there's a security issue that needs to get released, so maybe we can talk about this and then come back, David?
David Ashpole (dashpole) 00:27:43 Yeah, that's fine.
Tyler 00:27:44 Okay.
Yeah, because I'm also worried it might take a half hour.
Okay, so, I'm guessing, Robert, you put this here for the next release, right? This is around our, we just had a security issue that needs to get released, and there's things that we may want to,
try to block this on, I guess. I think there are things we want to block this on, so maybe we want to, like, go through this. I don't think anything in this list actually is blocking it, so maybe let's just start updating.
By creating a new…
Okay.
So, this also probably needs to get closed, I haven't come back to it, I'm probably not going to. But let's just do this. So, SK observability, definitely not blocking this.
The Prometheus migration, why?
Ugh, you can't… I don't…
I don't know what's up with this repo. You can't, like… it used to be that you could filter and move things, but anyways,
God.
Okay, the W3C new random flag, also not blocking on this release. Metrics SDK observability, this is a part of the SDK observability, not blocking. Not blocking. The logs SDK observability, also not blocking. So none of these things are actually,
blocking… let me… I think this is the only other one.
So I'm gonna put these in, the next milestone.
Pellared 00:29:19 I'm moving this in the background.
Okay.
Tyler 00:29:23 The thing is, is though, there is the SimConf, new package that was released, so…
the new 139 package is out, so we've done this before, we don't want to release without this migration, and I think this is the thing that is blocking us.
I don't know what's going on here, but this needs to get added to the… this milestone.
Pellared 00:29:47 My election.
Tyler 00:29:54 This is… in this milestone.
Pellared 00:29:57 The other…
Tyler 00:30:08 This was definitely something in this milestone. I guess I'll get it later, but it looks like this already got merged.
Okay, this is already there. So, yeah, it looks like, I think, this PR…
And this issue needed to get resolved,
I don't know what's going on here.
Pellared 00:30:38 Thank you, Jessica!
Yeah, well, thank you.
This PR does not…
Tyler 00:30:48 It does… yeah, this is a little odd.
Pellared 00:30:52 And this is something which you agreed that we do not want to do.
Tyler 00:30:56 Yeah, I don't think this is actually what we want to do either, but, okay. But this, this issue needs to get resolved, I think before we can get a release out.
Pellared 00:31:05 There was a question by, by Damien, if we heard about Zidgame.
Which we are deprecating. Do we need to…
bump sample there as well. I'm not sure how much work is to bump the sample there. It's not more… it doesn't take more time just to, you know.
It's actually noise.
But it's only because I have not checked the RPC versus thematic conversions.
Oh my gosh, look for.
Tyler 00:31:39 Zipkin uses the RPC semantic conventions.
Pellared 00:31:48 It says so here by Damien that he's using some…
Not sure which ones, but yeah.
Tyler 00:31:59 Okay.
Yeah, you're saying that all of this is coming back to the fact that this is just coming from our…
Self-observability telemetry, it's not actually coming from anything In the system.
Pellared 00:32:13 Yep.
Yep.
Tyler 00:32:15 I don't know why… why we're… like, that's all experimental. Like, do we need any of this some kind of stability opt-in stuff?
Pellared 00:32:22 That's what I said, that, in my opinion, none.
Damien agreed.
I can't hear you.
Tyler 00:32:29 Oh, okay. If that's the case, then yeah, I think we should just upgrade it and make the braking changes to the Zenithrooper… yeah.
I saw David shake his head. Sam shaking his head. Yeah, okay.
Pellared 00:32:40 For Zipkin as well, right?
David Ashpole (dashpole) 00:32:42 I think we never have to do one of those opt-in, opt-out things again.
Tyler 00:33:17 Okay. Yeah, I agree. Let's just… let's just do… go through the upgrade.
Okay, then going back to the contribib milestone, I'm guessing there's a similar issue here for tracking, yeah, bump SIMCOM139.
Yeah. That needs to get done. Robert's open that one. I'm gonna go… Yep.
Pellared 00:33:38 this bump, there was already a PR,
And basically, the one who worked on it just got it replaced, so Damien thought that maybe we'll just wait for the release of the go.
and just update the PR, you know, when it's up, and we bump, also go to the newest version, then we will be able to merge this PR.
Tyler 00:34:01 Okay, so this is also blocked on the, the hotel one, is what you're saying?
Pellared 00:34:05 Yes, because it's not… it's just not using, you know, it's just not, updating the…
Tyler 00:34:12 Yo!
Pellared 00:34:13 You know, A digest version?
Yeah.
Tyler 00:34:24 I think I see what you're saying.
Oh yeah, wait, how is this working?
Is this… passing?
I think I'm… I think I'm seeing what you're saying, but…
Pellared 00:34:44 Lean up?
It was not passing.
Tyler 00:34:50 Right, okay. Yeah, I was like, there's no way this can pass without upgrading to some sort of commit, so yeah, that makes sense. I mean, there's nothing stopping us from actually just working off of main, though, because the packages already exist in main.
Pellared 00:35:09 Whoa!
So what I cannot go back.
Sorry, it's hot.
Mr.
Tyler 00:35:32 Okay.
I think we even have, like, a…
A make target for this, right?
Pellared 00:35:39 I think you're right.
Fix them.
Tyler 00:35:55 Maybe it's just at the bottom.
Update allotel.
Okay.
Okay, cool, and then, looking back here, anything else here? This is support the environment variable, propagator. I don't think this is required, right?
No, okay, gonna move this.
Hotel HTTP deprecate the labeler in favor of the withmetrics attribute function. I don't think this needs to get done before the release.
Deprecate read bytes, again, similar. I don't think this has to get done before the release. So I think we're just waiting on the SEMCOM stuff, so that's all it looks like.
I'm a little concerned about the…
ownership of some of these things, like, these are blocking issues for these milestones that we're trying to get out at a little bit faster rate.
Is this not?
Why not change to the right one.
No, I did. Okay, I just was updating.
what are people's thoughts on this one? Like, this PR is not, I guess, as important as this other one for,
bumping the, SIMCOM in the main repo here.
I don't think anybody's actually working on this, based on what I just saw.
David Ashpole (dashpole) 00:37:47 If it doesn't get included in the release, is there something that…
Like, bad that will happen, or is it just that we'll be a little bit behind?
Tyler 00:37:59 I guess our users…
David Ashpole (dashpole) 00:38:00 Until a month or so from now.
Tyler 00:38:04 Yeah, it can be the,
what happens is the users will upgrade the OTel package, they'll use the new SEMCOM package, and then they'll have a conflict with the schema URL, and then, like, there's that whole, like.
It's not the end of the world, but it is the end of the world for some people. But, yeah, like, I don't know.
I do think that, like.
I can try to focus on getting this one done today. It doesn't look like there's any ownership of it, and it's just gonna be an update.
And then the Trib1…
I guess we can wait till tomorrow, and maybe I can take this one on as well, if I don't get any movement here, and then just open up a PR for it.
I guess the goal should be we should try to get a release out before next week's SIG meeting, maybe? Is that reasonable?
David Ashpole (dashpole) 00:38:52 I think that would be… very, yeah, I think that's reasonable.
Tyler 00:39:25 Cool.
That seems like a plan. Let's do that.
Goal for next week, let's maybe coordinate on this. I'll try to get the release out if I have time, but otherwise, I'll ping in Slack channel to see if other folks have time once we get the PRs, merged, or maybe I'll just do it if I have time, but, yeah.
Cool. Anything else people want to talk about with this next release? I think we've got a plan. Seems reasonable, right?
Cool.
We got 20 minutes left. Awesome. Let's go back to… this…
issue here, David, and we can talk more about,
I think the… the next… so the other side was, so we get the performance metrics, and then the other side was, is you wanted to talk about, this… this API, right?
David Ashpole (dashpole) 00:40:19 Yeah, I'm happy to discuss this API. I think, and I'm happy to discuss any of the alternatives.
Okay. Just…
maybe the most helpful thing is, like, I can talk about why some things are more performant than other things, or, like, what the… what the variables are, so that we know, like.
how different.
Because, like, there's a few… there's, I think, two main issues.
So… or, there's a few. Let's… let's go through the benchmark cases. So… For the pre-computed case.
The benefits… In this case.
occur because we don't do a map lookup anymore, right? We… we've done, like, counter.with attributes somehow.
And instead of
And then when you do add, instead of having to look up an attribute set, you can just increment the atomic counter, right? So that's why that case gets better.
For the dynamic case.
This actually has nothing to do with… this gets better not because of the fact that the instrument can be bound or not, but just because
we're not using the options pattern anymore, right? So because this is not wrapped in an option.
we lose the allocations, right? So I think…
Robert, this might be similar to why the logs API ended up not doing the options pattern, right? Is you get some performance improvements by not doing the options pattern.
And then, the other reason why this gets better is the switch from
Sorry, I lost my train of thought.
There's an optimization you can make.
if you… Get the raw attributes and not the fully computed attributes set in the dynamic case.
Because you can just do a hash and a lookup.
Rather than computing the full set.
and then using the hash from that to do your lookup, right? So, in most cases, you never need to actually store the attributes that you're given. You can just do the hash
And that tells you which counter to increment, right? So, those are the two reasons why the dynamic case gets better.
And then the naive case gets better, basically just… As a result of…
the same things as the dynamic case.
just with, like, fewer optimizations applied. There is still an allocation because you're passing in a slice, and so if you don't…
Use a pool with a slice, you still get your allocation.
The filtered… Cases here, all
Apply the same optimizations that we applied for the
No filter cases, right, so everything I discussed.
But the one thing that they end up
Also doing better is that
When we filter today, we take in an attribute set.
Then we end up basically computing a slice from it.
Filtering the slice.
and then computing a new attribute set. So…
The filtered cases basically all have an extra new attribute set.
Or no?
In the filtered pre-computed, I only compute the hash, so I… I made a small optimization there, on top of the existing SDK.
Or maybe…
Tyler 00:43:40 How do you do that? How do you compute the hash?
David Ashpole (dashpole) 00:43:43 So… So you get an attribute set.
you want to do a lookup based on it, right? But there's a filter applied. So you get the slice of attributes.
You filter the slice.
And then you compute the attribute… and then you just compute the hash of those attributes to do your lookup.
And you throw away the set unless you need it. So it's… it's…
Anyways, there's some additional performance penalties we have today, because we're accepting attribute sets and not attributes, that I think… I think some of these could be separately addressed. So…
for the Bound Instruments API in particular, I don't think they're relevant. It's just…
That's more to show that when you get a slice of attributes from the API instead of an attribute set, the filtered case will get a lot better.
But that, I think, is separate from this discussion. So, hopefully that's helpful for, like, the flavor of
Optimizations that are all packed in here.
Tyler 00:44:46 So for this dynamic one, you said that there's an optimization, not from the, the bound method, but just, like, the API differences, but was that computed
With a pool for the option?
David Ashpole (dashpole) 00:44:58 Yes.
So, the issue seems to be that the slice…
When you pass it to, with attributes, the option.
always escapes. And then, when the SDK calls new config.
And the slices, or in the… No, no.
So, sorry, I'm mixing up some of the optimizations I tried. No matter what I tried, I always got two optimizations.
The slice always escaped twice.
when it's passed to with attributes. I… I tried to note them in each PR.
For the other attempts.
Tyler 00:45:38 Yeah, but, but that's why we don't recommend using, like, the with attributes option.
David Ashpole (dashpole) 00:45:46 Or, sorry, with attributes.
Tyler 00:45:49 Let me see if I can…
I've only got… I've got this down to one allocation, though, so I'm… You have?
David Ashpole (dashpole) 00:45:55 Okay.
Tyler 00:45:57 Yeah.
David Ashpole (dashpole) 00:45:58 I couldn't… if you can show me how to do that, then we can improve the benchmark.
So that it's a better… I couldn't figure out how to get
Rid of the second allocation.
Tyler 00:46:09 So there'd be.
David Ashpole (dashpole) 00:46:11 It's… this is, dynamic.
With attributes or with attributes set.
Tyler 00:46:17 Yeah.
David Ashpole (dashpole) 00:46:18 Let me make sure I didn't just copy it wrong from the… Description as well.
Tyler 00:46:24 Okay.
Yeah, this…
Yeah, there's no pooling on the option being used here.
David Ashpole (dashpole) 00:46:45 The ad opt?
Tyler 00:46:46 Yeah, you're passing a new option directly, even though the ad opts up here Is…
David Ashpole (dashpole) 00:46:54 Oh, I see, I see, okay.
Tyler 00:46:56 Yeah.
David Ashpole (dashpole) 00:46:57 Okay, perfect.
Great, I can fix that.
Tyler 00:47:01 Yeah.
David Ashpole (dashpole) 00:47:01 That's awesome. I couldn't figure out… that's also not in our contributor guide, so I can also…
Put that in.
Tyler 00:47:08 Yeah, okay, that makes sense. I think that's… because you're… yeah, this looks… this looks right here, like, this is what we would expect, yeah, but just… yeah, okay.
So that's… that's probably where that's… anyways.
David Ashpole (dashpole) 00:47:20 then I would expect, if you look at, The allocations for… No filter.
dynamic with attribute set. I still see two allocations, but I can't… Beautiful.
Tyler 00:47:34 So, two allocations here, yeah.
David Ashpole (dashpole) 00:47:37 On the main, yeah.
Tyler 00:47:47 I treat slice.
David Ashpole (dashpole) 00:47:49 Can you leave a… Just a comment telling me what to do, and I can…
Get to the bottom of it, unless you think you can figure it out on the call.
Tyler 00:47:57 Mmm, yeah, it might be something I have to look at. This… I… I don't… This might be where…
It's losing it, but, oh, this probably is where it's losing it, actually.
Yeah…
This is probably getting allocated to the heap here, but, I can take a look later. Okay.
That being said, Going back up here, so…
Okay, cool, that's a good breakdown. Looks like…
From all this perspective, like, that makes…
some performance improvements, and mostly the pre-allocate… one of the things also that, like, just to point out that, like, the pre-allocated, like.
I don't think you can do much better with the SDK optimizations that David's put in. Like, even if, we were willing to look at caching external, like, the internal caching means that, like, you don't have to do these, like, additional lookups, so, like, we're talking nanoseconds at that point, or tens of nanoseconds at that point, but, like, it's still, like,
It may be pointed out that, like, that's a very important thing.
Okay, so I think that, like, this motivates…
again, like, the idea of the API, I just want to ask the question about, like, why can't we do,
This idea of using an option being passed to the meter when the instrument's created to bind the instrument?
David Ashpole (dashpole) 00:49:26 So, that will give you, if you look at the benchmark cases.
that will give you… or I think I said that in the comment there, but basically.
If you use this in the pre-computed case, you get to your… you're nice.
You know, 10-ish nanoseconds.
Super fast counter increment, because it's all pre-bound.
If you tried to use the…
new instrument API in the dynamic case.
it wouldn't be any better, right? Because it's the same options parameter, it's presumably the same way of
Like, it's just taking our… Our option and passing it in in a different function.
We can't do any additional… it, like…
Any optimizations we could make to that case, we can simply make to our existing add function, right?
If it's all dynamic, if it's, like.
counter, or, like, new counter with attributes.add versus… you see what I'm saying? Like, moving it around…
When it's dynamic, like that, when we don't know the attribute set ahead of time.
it doesn't help you. And the naive case is just a variation of the dynamic case, right? So… and not that it's that important either.
So that's… it will give you the better pre-computed.
Performance, but it won't give you the better, dynamic performance.
Tyler 00:50:53 Yeah, I, okay.
I don't know if I agree on the… that it won't give you the better dynamic performance.
I'm not following that part.
Because, in my mind, like, I'm seeing as, like, you could pool the options pattern, and you can pull the slice.
the only difference with this API is that you don't have to pool the options pattern. Like, you'd still need to pull the splice to get this optimization here.
So, if, like, if you're pooling both, like, the amateurization of that options pattern seems like it should be… like, I'm also assuming that you're gonna pass the slice directly to whatever function you create here, right? So, like, you're not doing an attribute set in this translation.
And I think that's…
David Ashpole (dashpole) 00:51:38 So, but it would be a with attributes option, right? It wouldn't be, like, a new…
Tyler 00:51:42 Yeah.
David Ashpole (dashpole) 00:51:43 So I think that's where you would still get your allocation.
you…
Tyler 00:51:48 So, but that's… so, what if… what if the with attributes option doesn't allocate a, A set, though.
David Ashpole (dashpole) 00:51:57 In the…
Tyler 00:52:00 Like, if we have the attributes option.
pattern that we talked about, where, like, the config would then be able to return to you, like, hey, it gave me a set, or it gave me the, you know, slice. Here's the slice it gave me.
And you can pass that down through.
David Ashpole (dashpole) 00:52:16 we can look… so this… this may be an area where I tried to do something and failed, so I… there's another prototype that is essentially this, because…
Tyler 00:52:25 Right.
David Ashpole (dashpole) 00:52:26 I think the high level is moving the option from add to the instrument creation in the dynamic case shouldn't change the math.
I think that's correct, but I think the, can we do better by getting attributes from the API?
is, like, maybe an open question. So, this is the… Oh, goodness.
I think it might be the somewhat performant one, E…
Tyler 00:52:55 with it.
David Ashpole (dashpole) 00:52:55 Yeah.
Tyler 00:52:56 Yeah, this might be it, yeah.
David Ashpole (dashpole) 00:52:59 I left comments where I found allocations that I couldn't get rid of.
I think.
So I thought it was strictly better.
And then… Yeah, I implemented it in a very confusing way, don't…
Okay, yes.
Tyler 00:53:25 the adder option…
David Ashpole (dashpole) 00:53:27 So this is the option itself.
Seems to always escape to the heap. This is what I was talking about.
Like… If you just call metric.withattributes, you get an allocation.
And I think I have another comment where the other allocation comes from.
Tyler 00:53:46 Yeah.
Oh, God.
David Ashpole (dashpole) 00:53:54 But it ended up being no better, which… It's like…
Or I think the runtime got slightly better, so I think we could get some small wins, potentially, by going in this sort of direction.
Because you can… you can just compute the hash, then, and not compute the… Full set.
Tyler 00:54:14 There's.
David Ashpole (dashpole) 00:54:14 one… Let's escape through the heap.
destroys the performance of some other stuff, which is why I was like, oops.
Maybe not, but… Oh, really? Huh.
Yeah, all the users of with attributes set will be really sad.
Maybe we can do some tricks to keep their performance. Well, I mean, so that's the other thing, is like, it doesn't have to… mmm…
Tyler 00:54:39 you can split these up as well. Like, this is not an exported type as well. Maybe I could take a look at this, but I do… I do wonder about this, because, like, I see…
I see why this is escaping to the heat, because right now, like, this is a… this is definitely,
inside this function, it's on the stack, given, like, it's like a… it's not a pointer type, it's not a reference type, it's a… you know, and it's very easy to… let's see where this is going. But then it gets cast as this interface, and that's where you're losing that, right? But if you have,
If you have a…
a pool using a pool of measurement options, right, and then you're assigning something that was already referenced, like, say this is a pointer type instead, right? I could see that that then using that pool memory for that storage in the optimization. So I do think that there is still a way to get rid of this, escape, or, I'm sorry, this allocation.
Sorry, that's not the right thing. I think there's a way to amortize this allocation. I don't… like, I think it needs to get allocated to the heap, always. It's just that, like, if you pre-assume that it's going to get allocated to the heap, then I think you could actually make those optimization, but I'd have to… I'd have to verify that, though.
David Ashpole (dashpole) 00:55:49 Okay, yeah, I think this is maybe a…
Tyler 00:55:53 Yeah, I see your point, like, if this can't ever go away.
That is… it is still always going to… yeah, and that… that's gonna always be there if you can't… if you can't make that optimization.
I think that that's… Something to explore.
I do want to say, though, that I'm still, like, really hesitant to try to add this
this method for attributes, though. I think this is, like…
I think, like you're saying, like, you can get this from alternate ways to do this bound instrument, which I think is actually worth doing on its own. The other ones, I'm…
So the other ones I'm a little bit hesitant on, because for one, I do think that, like, our contributor guidelines right now are pretty… well, I guess when you say contributor guidelines, do you mean, like, the contributor guidelines in our repository for, like, our developers, or do you mean, like, on OpenTelemetry.io?
David Ashpole (dashpole) 00:56:47 So, all I meant was that I was trying to… I…
I was trying not to bias the results of all of these by just looking at what we had told… what we had said that we should do for our self-observability metrics.
Tyler 00:57:02 Yeah, okay.
David Ashpole (dashpole) 00:57:02 So that was… that was why I was trying to choose a neutral starting point.
Tyler 00:57:06 Yeah, that seems…
David Ashpole (dashpole) 00:57:07 We can obviously change those and whatever, but that's all.
I don't… it's not on OpenTelemetry I.O. or anything like that.
Tyler 00:57:16 Oh, okay, alright. Then, yeah, I just want to make sure we're talking about the same thing. So yeah, I think that, like…
So every single time that, like, we have dynamic attributes, it's an error situation for us right now, right? Like, all the other times we have…
Sorry, go ahead.
David Ashpole (dashpole) 00:57:30 LHD stuff, it…
Tyler 00:57:32 So, yeah, OTEL HTTP's not taking into account any of these, like, patterns that we've defined. It should be, like, yeah, like, we definitely should look into OTL HTTP, and there are a lot of optimizations from what we already talked about in our contributing guidelines that we could make.
there. We just haven't done that yet. And that comes back to a lot of, like, these pre-commuted, like, strategies that we came up with.
But, that being said, like, it'd be nice if, like, those pre-computers, like.
So, what I'm thinking about is things like, OTEL, like, the response code stuff, right? Like, that's definitely one where you know all the response codes, at least the majority of them. Like, obviously, there may be some outliers, because…
David Ashpole (dashpole) 00:58:13 Right. Anyways…
Tyler 00:58:14 But, like, in the… that would be an error case if you don't match, like, what you already know. And so if you already have, like, these, like, combinations of attributes that you know are going to be returned, like, you can consider them pre-computed and go about your special way of doing that, right? But, like.
I think that that's kind of the case, is, like, we could always try to recommend to do as much pre… pre-compion as, like, as you can possibly do, and I think that, like, even with this API change, like, if we had some way to do a bind instrument, like, we've done this before in some of the optimizations, where, like, you actually create, like, kind of like a…
I don't want to use the word view, but kind of a view of the instrument. It's just an instrument, right? And it's essentially, like, these pre-compiled, like, things where all you're doing is doing these, like, addition of, you know, some sort of, atomic operations.
if you can get, like, just a map of that in your instrumentation, I think, like, you're… like, that kind of pre-compution, like, makes things very optimal. Not even, like, pre-computing, options. You could pre-compute, like, the instruments is a very optimal way, yeah. And so, like, I think it, like…
Yeah, exactly, right? And I think that we've done this in a few places, I'm trying to remember, like, I definitely think I saw this once, where we tried to do this.
And so, like, I think that that's, like, the best you can do. The times where we always are having these dynamic attributes is where, like, we have these error cases and…
Technically, I don't think they're unbounded, but they are kind of unbounded, where literally, like, you get a response and you need to include the error message, and, like, the error message should be, like, a gRPC error code, but, like, it's not always guaranteed to be that.
So it's kind of the same thing as, like, the status message, but yeah.
David Ashpole (dashpole) 00:59:50 It's like maintainability, too, right? It's like, oh, a new error code came along, and…
Yeah. Like, we have to, you know, we can't assume that it's… some of these things are static forever.
Yeah. Unless we detect them, right? Exactly.
Tyler 01:00:03 And, well, that was actually… yeah, and that's actually what we said we wanted to do, was eventually define our full set of errors that we would ever accept. But, like.
Yeah, so, like, I think that, like, this optimization for the pre-computer, again, this is why I think this is a very motivated feature set, is, like, this is, like, the case where we'll want to be pushing users to write instrumentation for this. The dynamic one…
I think that we could look into the optimizations here, but, like, I'm more concerned about, like.
I think the 80% case, where we can try to get users to use these pre-computed attributes, I guess. And the optimizations in the dynamic case.
are important.
But… Personally, and this is, like, this is not,
I don't… this is, like, not a good reason to have a different option pattern for me, is it doesn't motivate that, that change for me, or that inclusion.
David Ashpole (dashpole) 01:00:55 Okay.
I think that's fair. I… I originally came to this trying to…
In my mind, fix the dynamic path.
But, yeah, so I think… I think Mason.
Tyler 01:01:08 I still think.
David Ashpole (dashpole) 01:01:08 different views of, like, the 80% cases.
Yeah.
I don't have anything else.
Tyler 01:01:19 The thing is, is though, like, I do think… I still want to look into this other PR you have, because…
If you have people writing ignorant instrumentation that don't take into account, like, all these contributing guidelines that we have around pre-compution.
It would be nice if it would still just dynamically apply that.
David Ashpole (dashpole) 01:01:38 So maybe they don't get the optimization of, like, pooling their slices or pooling their options, but, like.
Tyler 01:01:45 if you, you know, can still compute the hash and say, like, hey, actually, I've already found this, like, I'm not going to do any more allocations beyond that, I think that we can look into that. So I still want to look into this other…
Prototype that you had,
Yeah, this somewhat performs, so I… I did so many…
David Ashpole (dashpole) 01:02:02 I even tried changing the API to accept, like, pointers to slices, and… It's just…
Tyler 01:02:09 Hmm.
David Ashpole (dashpole) 01:02:09 I couldn't figure out…
Tyler 01:02:11 Okay. Yeah, I…
David Ashpole (dashpole) 01:02:13 I, maybe…
Tyler 01:02:15 Well, yeah, I'll take a look.
David Ashpole (dashpole) 01:02:18 That's… that's fine.
Tyler 01:02:18 We are… Over time, also, so I just want to call that out.
Okay, cool. Robert, you had a comment for adding something to the agenda?
David Ashpole (dashpole) 01:02:32 But we're over time.
Pellared 01:02:33 Oh, yeah, sorry, we're over time, yeah. Oh, I see.
Tyler 01:02:37 We can talk about that next time. Okay, sorry for overextending, but this is a good conversation. Thanks, everyone, for talking. See you all next week.
Pellared 01:02:45 Sue.
