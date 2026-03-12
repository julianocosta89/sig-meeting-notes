SIG: Sampling SIG
Date: 2026-01-15
Duration: 29 minutes
Zoom Recording URL: https://zoom.us/rec/share/wEk06DojYXLdy064Ng_GQ5v36Jvmo2msw9fwBx9PXKSy-O0IflnR68DCrdLtaoKz.BMtv0LAww4ziMxm1
============================================================

## Zoom Recording Transcript

**jmacdonald** 00:35 Hi, hi, Alf.
**Alf Kenny** 00:37 Hello.
**jmacdonald** 00:38 Hi, Amar.
Happy New Year.
**Alf Kenny** 00:41 Happy New Year!
**jmacdonald** 00:42 Oh… Well, the…
**Otmar Ertl (Dynatrace)** 00:45 Hello, interesting to you.
**jmacdonald** 00:48 Good morning, or good evening. I… Been a while since we did one of these.
So, I'll share, and I know there's an agenda starting, and probably one of the first thing I want to do is ask Alf how his PR… the PR went, because I tried to get help, and then probably forgot to follow through. I think I did something.
**Alf Kenny** 01:12 No, yeah, the… I got a reply from Sean Porter, he didn't provide an actual review, he just sort of, like, made a comment that kind of… echoed the concerns I had, and also accepting… understanding the limitations, and then just kind of… did nothing. And then I… I think there was another guy who was originally specified as being the code reviewer, and he said, I'm not the code owner, you have to talk to this guy, whose name is Patrick something, and I pinged that guy in Slack, and I haven't got a reply from him yet, so I'm kind of… Spinning my tires.
**jmacdonald** 01:44 I see. Well, it sounds like there… we kind of knew this, but I… it sounds like there's a little bit of an ownership issue there. Do you remember the number of your pull request?
**Alf Kenny** 01:55 Let me grab that right now.
**jmacdonald** 01:58 I could find it, but…
**Alf Kenny** 02:00 44378.
**jmacdonald** 02:02 44378.
**Alf Kenny** 02:04 Correct.
**jmacdonald** 02:06 Nobody wants to own this code, is what we've discovered.
So, alright, well, I… oh, here it is, still open.
I have some powers. I can push people, and then say that you've been diligent and patient, and the reviewers aren't reviewing.
It's a signal that we don't have responsive owners, and so we can try and change that.
I don't think you want to become an owner. Nobody wants to become an owner, but I can… I can try and sign myself up, To deflect and, and, And some of the people there know me, so that might work. So I've put this in the notes now.
No response from reviewers.
After many months… Would you say that… that we're… that the… But the current best thing we can do is, push forward, like, I can start asking people to merge this.
I approved.
**Alf Kenny** 03:32 Sure, yeah.
**jmacdonald** 03:33 Yeah, I mean, I think it's just as long as your team feels, or the team that's, the special interest group feels like this isn't.
**Alf Kenny** 03:40 Doesn't have any security concerns, or isn't gonna break anything.
I… it's relatively… it's kind of like a carbon copy of some of the other, processors, or… or, Policies, and then just with a few tweaks, so… From my perspective, it's… I don't… I feel like nothing can go wrong, but then you never know.
**jmacdonald** 04:01 Yeah, okay, so… I… what I can do… this is just… I can try and press forward, approved it again.
I'm… I'm considering taking this to a Slack channel for the collector leads that's a private channel, just to keep noise down.
To ask for help.
Gonna do that.
**Alf Kenny** 04:35 Cool. This morning.
**jmacdonald** 04:36 I wish I could say more, or more helpful, something more helpful.
but what I'm essentially resolving to do is to try and force this in now, since we've waited.
And… I'll ask… essentially right now. I won't follow up on it during the meeting here, though, so I will do my best to push this today. Feel free to Slack me if it feels like it's dropped and I've forgotten. Okay. But what I'll do is start a thread Essentially now.
But not until we're done with this meeting. Asking to, like, essentially say… and if I have to sign up as a code owner, I will. I'm gonna be at least as responsive as those guys at this point, is what we've seen. So, I'll offer myself as a solution, since… I can ignore those PRs just as well as anybody, ultimately speaking. So yeah, okay, that's how I'm gonna handle that. I'm gonna propose that I become a code owner. If there's no… no one else fighting me on that, I'll probably get that settled.
**Alf Kenny** 05:50 I'm gonna jump to another call, and I fully appreciate the help.
**jmacdonald** 05:54 Will do.
This is gonna be even further towards my step to get rid of this thing eventually, so… Cool. Alright, thank you, Alf. I'll… and you can Slack me as well. Thank you.
**Alf Kenny** 06:04 Sure. Yeah.
**jmacdonald** 06:06 Okay, well, for the… for the usual crowd, thank you for being here. I know that there's another item… oh, that's the wrong document. I'm sharing the wrong screen. Okay, here we are.
So we just…
**Yuanyuan Zhao** 06:22 It is the correct one.
**jmacdonald** 06:24 Oh, Yuan Juan. I know that you've been, looking into… both some of the SDKs, like Go, and also spanmetrics, and I see you have two alternatives, let's talk.
**Yuanyuan Zhao** 06:36 So, yeah, I want to round this by you guys.
The current spam metrics, connector, like, supports, like, histograms, only with integral count, right? Like, if you have, like, a value to put into a histogram, it would count that as one.
And there's another option where you can supply a value and say it counts multiple times. But all this multiple has to be integers. The parameter on the functions are of type UINT64, So this is the case on histograms, this is also the case on sums and, counts.
So, with the new… trace state, and in particular, I want to point out that the histogram implementation uses this, this thing from, a package in LightStep.
There's a… right. It is a, it is, it is a, different implementation from the histogram in the, Go SDK, in that it is a more… it's a version that's optimized for, integer types. The, so the… The issue here is that with the new chase state.
That, and the new probabilistic sampling, Now, we're going to have… things that are counted a fractional amount of times, right? Like, the adjusted count, in the implementation, it is actually a float 64, instead of, like, a new int 64, right? If you are sampling something by, like, 3 out of 4 times.
Then, each value you have Should count as 1 and 1 3rd.
time, so it's 1.333, right? That's a load, it's non-integral. And we can't just round each time, because then the loss of precision is very large.
I took some look at the code. There are, this last step implemented… so there are places where it is not hard, like the Samsung count, I can just change it within spam metric connector, the… more nuanced the issue comes in with this use of external packages. Currently, it's like step expansion histogram. The Go SDK also As a experiential histogram, and, this, of course, like, backwards compatibility issue, but putting that aside, right, we definitely have to be backwards compatible, but even putting that aside, I think there are two Approach, approaches that we can move forward, and each has its pros and cons.
The first approach is that we change the counts to just the road 64. The draw… the process that this is clear, this is intuitive.
The, cons is that now, instead of, integer operations, we are looking at the float… floating point, operations, which are more expensive, right? That's a straightforward implementation.
An alternative is, to, wrap a, fractional, scaling factor, right, like the 1.33, of the 3 out of 4 sampling.
wrap that outside of the exponential histograms, so that each operation into the histogram stays the same, still integer, all those things. However, that has the drawback, in that The scaling, factor, this fractional scaling factor.
Should not change very often, which could probably be the case.
Even though with, like, some complex setup, people might, in this case, go into one, sampler with one sampling ratio, and in another case, branch into another sampler with a different sampling ratio, but the number of This kind of different adjusted count.
should be limited, right? That's… but it is… a much more complicated implementation. The pros, of course, is that we preserve the, integer operation. So the performance is slightly better. The histograms in the Go SDK, Josh, let me, Sent you a link so you can show it.
**jmacdonald** 12:13 Okay.
**Yuanyuan Zhao** 12:14 2… the room…
**jmacdonald** 12:20 And by the way, I'm following this debate. I've… this is… this is the first time it's come up in this room, I think, but… Yeah. OCEL does not have a good solution for us when we talk about non-integer multipliers.
**Otmar Ertl (Dynatrace)** 12:33 Actually, there is a third option, it's.
**jmacdonald** 12:37 Let's talk about all the.
**Otmar Ertl (Dynatrace)** 12:37 holistic.
probabilistic rounding, right? So, which would, you know, Would guarantee, that the accounts are unbiased.
And… I mean, this was actually all the original idea, to stick to power of two probabilities, because then the inverse is always an… is always an integer, and we wouldn't have.
Rolo?
But since we decided to allow more sampling probabilities.
Then the solution… what it… I would prefer the solution of probabilistic, Rounding. Roundy.
Because then you do not have to change anything in the histogram, you just have, if, for example, the… them, the trustee count is, like, I know one, one-third.
Then you would, yeah, increment by long.
In two out of those three cases, right?
**Yuanyuan Zhao** 13:40 Depended by another, yeah.
**Otmar Ertl (Dynatrace)** 13:42 Yeah, you're just, Use a random…
**Yuanyuan Zhao** 13:45 Basically, that, if it's, like, 3 out of 4, the sampling, then, 3, so then, two times, right, you, you implemented, you incremented by 1, another time you incremented by 2.
Yes. So you come up total, count the total of 4.
**Otmar Ertl (Dynatrace)** 14:10 Yeah.
**Yuanyuan Zhao** 14:11 with 3 samples. Yeah, that's a good point. I… it actually didn't occur to me. Then this… Probably, sounds like it might be a tough choice now.
Because, it preserves the integer operation.
But on the other hand, you still have to, like.
do this kind of sampling, right? The prospects around the, like, the deciding on when That's… that… that has some overhead.
**Otmar Ertl (Dynatrace)** 14:45 I mean, a random number is relatively cheap.
Of course, you need a random number.
But… I think this overhead is not that big.
**Yuanyuan Zhao** 15:00 Okay, any other, choices that… We might have missed, or these are the top 3.
**jmacdonald** 15:11 I… Thank you for… thank you, Atmar, for the… that option. I've, I've definitely thought of the other two, all of these before. The… the… the idea of a non-integer multiplier, for the record, is an interesting one that, I… I think would require too much, like.
Interpretive… like, too much work for the consumers, essentially.
But my old company was fighting this topic, because they just wanted to take spans and count them in histograms, and they were sampled, and then, like.
You know, being forced to do integers.
So I've seen, and I've also seen… Some code that… that sort of, like.
does approximate integer counting, like Atmar described, so that's… that's… I would… I would lean in that direction.
Now that we've thought about it.
And as you say, for the counters, you can… you can… you can do that. Like, for sums, you can do it correctly, but, as… as a double count.
Even that sort of worries people sometimes. In the Datadog StatsD receiver, not the Datadog, the StatsD receiver, I had to handle this. I don't remember exactly how I did it, but… but we round… Adjusted counts to the nearest integer.
for lack of a better answer, you know, maybe if there's a, improved Probabilistic counting histogram We could use it there as well.
**Yuanyuan Zhao** 16:54 So… then it looks like we have some consensus. Then the next step would be, try one or more of these implementations and try some microbenchmarks.
**jmacdonald** 17:09 I'm just writing up the option that we haven't discussed. Propose a new histogram data type. I've often thought of this. I mean, like… Every time we need a histogram that counts fractional Buckets.
We have this problem, and forcing us to work around it every time is, a nuisance, but there's not enough weight behind needing it, so I like this, approach.
It reminds me that we did similar types of… rounding exercises probabilistically when we were interpolating between non-power of 2 probabilities. So, to sample at 75%, you do the same type of probabilistic snapping to an integer as well. So it's probably the same type of math, I would imagine.
It's straightforward linear math, is what I remember.
**Yuanyuan Zhao** 18:01 Okay, the, the fourth thing, right, the new histogram data type is… it's… it's a thing in a different dimension as the other three. The other three are the implementations.
**jmacdonald** 18:16 Yeah. …office, right?
Yeah.
It's not a realistic alternative at this time. It's just, I think OpenTelemetry has already suffered from having two different histograms.
And having a third would make it worse, not better, even if it's correct and useful.
At least until there's more popularity behind it.
**Yuanyuan Zhao** 18:43 We could probably do this in, do this, new histogram type in, spam matrix Connector first, the contrib, right?
And…
**jmacdonald** 18:57 Well, the problem is that there's no OTLP output format that you can use to represent it, so even if you use the new data structure, you have to output OpenSelemetry data in that setting.
**Yuanyuan Zhao** 19:06 That's, that's actually another thing which I actually forgot, but, to mention, but I probably slacked, Josh a few days ago. It's in this, PData thingy.
That's where, we.
**jmacdonald** 19:25 PData is the abstraction for an object of data in the collector.
**Yuanyuan Zhao** 19:29 Right, right. But, the… the idea, like, for example, the probabilistic rounding, right, can probably… carry over there.
As long as, Like, the interval, we export into, the P data that… those were for, like, exporting things out of the current process, right? And with the rounding… the rounding works, doesn't lose precision only when we have enough data there, right? Some… I mean, another term, statistical significance.
**jmacdonald** 20:12 I see, yep.
**Yuanyuan Zhao** 20:13 Then, if… that's… but it's probably a big if, right? If the, output period is significantly enough Then, we don't need changes.
in, the, wire format.
Because it can preserve the integer, types.
Because of probabilistic wrongdoing.
But it is probably a big if. We don't… we don't know how big that is. I just want to.
**jmacdonald** 20:46 Yeah, I, this is where, with the StatsD, I just kind of waved my hands and ignored it, because there's not much we can do about it.
And do you, let's see, do you con… I forget how… let's see, the span metrics controller connector, does it have an interval that it's in control of?
I think you could probably just sort of, like, keep track of the error and print it out, like, like, warn the user, this is how much error we're having. A longer interval would help.
Yeah, they expected our…
**Yuanyuan Zhao** 21:24 That kind of thing. I mean, it's, like, it is probably a big if, but it doesn't rule out that it can still be used. It's just that anyone who Makes use of that, and…
**jmacdonald** 21:45 Yeah, I don't know, maybe there's some semantic convention we could come up with to warn users that, like, this is rounded data, we couldn't do better, it's just a warning, like, if we want better, we have to change the data model.
**Yuanyuan Zhao** 21:57 Yeah, yeah. So… In that case, actually, I didn't have my, PData format poured out, but in that case.
The change is not as intrusive as changing the integer type to floating point, but instead that it can be a change where we add some new field, which basically says these are extrapolated I… not, like, these are probabilistic extrapolated, and what is the… what the expected error is. That's, like, addition of, to a couple of new fields, which makes the backwards compatibility issue a lot less, right? It's not… not less severe.
**jmacdonald** 22:50 But what I might recommend would be, to try and do that, but without changing any data structure. So, we… as a… there's a couple places that I could imagine, like, one would be just putting another attribute, saying probabilistic true. Like, we did some rounding here. You gotta… you gotta recognize that there's a probabilistic happen… thing happening, and…
**Yuanyuan Zhao** 23:14 Yep.
**jmacdonald** 23:15 It might. You could also… there's, there's places where I doubt users are gonna see the data, like if you added it to the description, or to… if you added it to the metadata field.
most… most of those fields go nowhere, I know. So, putting it in an attribute is the one that's most likely to be seen. So you could just throw in an attribute saying, probabilities happened.
Or it could be, like, a string with a warning, basically saying, the error is maybe… I don't know how you measure error here.
But I, I would… some kind of warning to tell users that they're getting approximate counts, and… Yes.
I feel like there's some sort of mathematical number we could give to, like, tell them the severity, like, the… Variants of some sort.
**Otmar Ertl (Dynatrace)** 24:11 This is, I think, quite difficult, and… General case, especially if the adjusted counts are not constant.
**Yuanyuan Zhao** 24:22 Yeah.
**jmacdonald** 24:26 my… the last time I faced this, it was, like, it was the stats, the environment. So, like, you know that someone can set a sampling rate of 10, and, like, you know that that's gonna really close… be close to 10 when it rounds. My… my… my recommendation, therefore, was, okay.
go ahead, use this connector. It will be rounding. Use probabilities that are close to integer multiples, and it will not be a big problem. So, if your probabilities are close to integer multiples, does this problem go away? Because that's a good recommendation. That's sort of what we recommended for Stats D. And then you just don't even solve the problem.
Yeah, so don't use 3 quarters or one and a half, like, that's the problem, is these, like.
course… like… Rational numbers that are, like, nowhere near an integer reciprocal.
I don't know.
**Yuanyuan Zhao** 25:20 Yeah.
**jmacdonald** 25:22 But…
**Yuanyuan Zhao** 25:23 Right.
**jmacdonald** 25:24 Yeah, so anyway, I would say this is the least of our problem, is to worry about where those little fractional counts go, and if people know about them.
**Yuanyuan Zhao** 25:31 Probably, the first one we can shoot is just, Like, the very basic, attribute of… this is extrapolated.
Because given, like Automat said, given… a estimation, of the expected error can be done very cheaply, right? Unless you do a lot of more operations, and there's also, like, histograms at different buckets, then what do you do over there, right? I think that's, much trickier.
issue. I mean, there.
**Otmar Ertl (Dynatrace)** 26:08 The result… the result is that it would not create, because there's sampling involved anyway, because we get adjusted counts, which are non-impers. And if you do some additionals, yeah.
probabilistic stuff on top. It increases the error a little bit, but I mean, the error is already there before.
And also from the span sampling, we… we… it's also hard to… to estimate the errors.
And so, I wouldn't worry much about it.
**Peter Findeisen** 26:43 So, okay, so they seem…
**Yuanyuan Zhao** 26:46 Seems like we're saying we, do not need to provide an estimation of the expected errors. I mean, it was…
**Otmar Ertl (Dynatrace)** 26:56 I would also recommend…
**Yuanyuan Zhao** 26:58 It's hard, and it's expensive, right? It's, that's the thing. And we recommend they use a sampling rate that is the reciprocal.
Of a, integer.
**jmacdonald** 27:12 Yeah.
**Otmar Ertl (Dynatrace)** 27:13 But still, the histogram is then just, you know, an estimation, right? Because if you have some sample already before, it's still not accurate.
Even if it's a reciprocal of an integer.
**Yuanyuan Zhao** 27:32 Okay.
**jmacdonald** 27:33 Thank you. Well, I've been taking notes…
**Yuanyuan Zhao** 27:35 Well, I feel good, right? Seems like this is a good steak.
That we are arriving at.
**jmacdonald** 27:41 I'm glad we have this talk here. I don't think we've ever spoken about non-integer histogram counting.
Yuan, Yuan, you said you were looking a little bit into the Go SDK sampler support. Any news there?
**Yuanyuan Zhao** 27:53 I haven't, but I will.
**jmacdonald** 27:54 Okay, sure.
**Yuanyuan Zhao** 27:55 I will. I will definitely, look at that. I've had your, pointers. I, I, I was only looking at, this biometrics connector.
**jmacdonald** 28:04 Thank you, that's good.
**Yuanyuan Zhao** 28:05 Yeah.
Next meeting… next meeting, I should, or even before that, I should snag you up about something around the Go SDK.
**jmacdonald** 28:15 Yeah, I don't know. I've… as I mentioned, I have, struggled with the Go SDK and tried to step back, basically, a while back, since I, like, as you see, like, they didn't use my histogram. There's lots of… like, they don't want to do things the way I do things, is what I've found. So that's fine.
There is a SIG meeting for Go today, I… don't plan on going to it. I… I am becoming more and more capable in Rust when we… when… when we… when the time comes, I will be working in the Rust area.
I have no more news on this topic.
For us.
**Yuanyuan Zhao** 28:53 So, the GoSig meeting is today. Do you recommend me to go to chat?
**jmacdonald** 28:57 No, I don't. I don't. I would recommend you continue around span metrics, and then, It's too… it's too… I don't have… I don't know, it's… it's too late today for… for thinking about this. you and I can talk about how to handle the SDKs.
**Yuanyuan Zhao** 29:14 Yeah.
**jmacdonald** 29:15 As time permits.
**Yuanyuan Zhao** 29:16 Sure.
**jmacdonald** 29:19 Thank you all. I think we did it again.
I'm gonna write all 5 of our names here, and then we're done.
**Yuanyuan Zhao** 29:26 Thank you.
**jmacdonald** 29:27 Let's see if you know.
**Yuanyuan Zhao** 29:28 Thank you.
**Peter Findeisen** 29:29 Thank you. Bye.
**Otmar Ertl (Dynatrace)** 29:30 Good, but…
**Yuanyuan Zhao** 29:32 Yep.
