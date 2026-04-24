SIG: Sampling SIG
Date: 2026-04-23
Duration: 50 minutes
Zoom Recording URL: https://zoom.us/rec/share/a17dcDdx8kegB_D-KNji4vwM_VDp8UfRLQXS0hrCaG4viiTi69RDQHOyUYYFiDMG.k5Jz6VMrfxH9h3E3
============================================================

## Zoom Recording Transcript

**jmacdonald** 01:10 Good morning.
**Peter Findeisen** 01:11 Good morning.
**jmacdonald** 01:17 I guess I have an update. Not much.
Switching between Zoom and Teams.
So… good morning.
Maybe it'll be just us, Peter. Oh, here we go. Oh, Carson.
Good morning.
Oh good, we've got people showing, alright, cool.
Hello, folks. One new visitor, I know you are… I know… we know Carson, I do, but maybe I don't remember you coming to this meeting, so welcome, Carson. We can do a little introduction. I believe you work at Elastic.
**Carson Ip** 02:19 Yes, thank you. Great to meet you all. I'm Carson, working at Elastic, and I'm the co-owner of Elasticsearch Exporter, and also, as of today, for the tail sampling processor, so, Please talk to me about how to improve.
tail sampling processor, I'll be happy to work on it.
**jmacdonald** 02:47 Great.
Yeah, I, I gave an update last week in the, Hotel Spec SIG, actually this week in the hotel specsig, kind of quick Actually, I could probably find it. Where is it?
Did I put it in the notes?
You'd think I would put it in the notes.
As soon as I start projecting, I can't… I can't manage… I will share my update, it says a little bit.
Except… ugh, I apologize. I have to switch around between Firefox and Internet and Edge Explorer and stuff, to do things.
And I don't have… And a Google Doc problem.
I know how to find it, though.
Here is the sampling update that I gave this week.
Oh my god. Nothing is easy.
Yeah, there it is.
Hello, everybody, now I found it. So I gave this little brief sort of update on the state of our world here. I named a lot of people who have helped us get here, so thank you, thank you.
This is the timeline, this is the work that we did in this room for 5 years or so.
leading us to this trio, or four major PRs that we put together last year, and, now we're sort of, like.
Toodling our thumbs a little bit, In fact, you guys all know this. This is, like, the new specification work.
Carson, this, like, once in a while in this room, we talk about tail sampling processor and how it, can't really easily be modified to do some of the stuff here, but it's a wish list item. So we talk about, like, how could we, when the tail sampling processor flushes out like, just drops data from memory because it's out of memory. Like, how could we then inflate the counts so that we're… counting something. I gave this sort of, like.
like, you know, summary of the four big components that are around sampling right now, and these are all important, and I say coming soon, it's already here now.
I also, sort of left out… left off with the roadmap.
I… I actually didn't realize how far along we were, and this is a hat tip to Peter. You know, I was saying that we didn't have the declarative configuration model, but I understand now that it's in the 1.0 declarative specification, your work on composable sampler declaration came through, and it's implemented in Java, which I didn't realize.
**Peter Findeisen** 05:56 Yeah, I don't think it's a full implementation, we don't… still don't have predicates, but yeah, it's the step, yeah.
**jmacdonald** 06:05 And I said this… I actually had to refresh my memory on what our plan was, because… and this is the topic that Yuan Yuan may… we should talk about today. As you were working in the Go SDK, we realized that the SDK spec doesn't say something about about, changes about the… clearing of threshold, for example. So there's, like, a little bit of a missing text somewhere.
And as I was reviewing it, I remembered what our plan was, because I didn't until I went to review it. And the middle of this document here sort of says the big, big important piece. We did not change the specification for always on. We did not say you should set TH colon zero for always-on sampling.
Because… Well, we didn't, and I think that's because we would also have to change The parent sampler, and there was no way to do that, and therefore we concluded That we should create… change the default, so that eventually, what we're aiming for to get this stuff on by default, is to change the default sampling rule, which in my pseudocode looks roughly like this, is to build on the composable sampler and the parent-based composable sampler.
Which is this guy.
And this may not read exactly quite the way we want it to read, but that's roughly the idea, is that we're not going to fix always-on, we're gonna change the default.
Yeah.
**Peter Findeisen** 07:33 Yes.
**jmacdonald** 07:34 So, that reminded me where we were.
And… this is the wrong document. And, And that just reminds me that there is so much more work to do on all the SDKs.
And that is all I have, really. I, so, sort of as my review.
Yuan Yuan, should… could we talk about, next, about this missing spec piece? I think that you…
**Yuanyuan Zhao** 08:19 life. Let me give you a link.
**jmacdonald** 08:33 I can also find it, except that you've seen me try to find things in front of you.
**Yuanyuan Zhao** 08:39 So, this is a… PR, and they issue That we discussed in the context of the Go SDK. It's… mainly talk about what Josh just mentioned, that when there isn't a randomness guarantee.
we erase the, TH.
The threshold in the… In the trace context, so that this is basically a signal to, whoever, consumed that trace state that they shouldn't derive Statistical information from it.
I think that's… that's that part.
On the Go SDK, there was an issue with the always-on, because when we have a threshold that is Virtually zero. We turn it on into a always-on sampler in the original implementation.
But we've decided… That it shouldn't be the case that a probabilistic sampler should not turn into a always-on sampler, but a probabilistic sampler with a threshold of zero.
So that was the… Is this different from your understanding, Josh?
**jmacdonald** 10:20 That makes sense. We should not turn into an always-on sampler for the reason I just mentioned earlier, which is we have not said always-on should set the threshold.
**Yuanyuan Zhao** 10:28 Yep.
Yeah, we're not changing the always song. We're just changing basic sampler. You'll never… turning into an always-on sampler, because an always-on sampler, if you are saying it's for properties sampler, then when everything's satisfied, you could also say that the always-on sampler can be for another kind of sampling algorithm when the condition is always satisfied, right? So that's, I think that's a… That loses.
**jmacdonald** 11:02 I… so, that topic, is that… is that contended in the specification? Is there some missing text about that, or is it just a check, or check-in?
**Yuanyuan Zhao** 11:12 The always-on, discussion is not part of the, SPAC revision, and I… This is this?
**jmacdonald** 11:20 thread here, correct?
**Yuanyuan Zhao** 11:22 That's right. Yeah, okay. That was changed.
Right, but this… this is not part of the, spec… revision. I don't think we mentioned… I didn't see we mentioned this in the spec.
Okay. Yeah.
**jmacdonald** 11:39 No, I just…
**Yuanyuan Zhao** 11:40 Back is about… The SPAC is about the treatment of randomness.
**jmacdonald** 11:46 Right, so we did not say somewhere here that if your value is greater than 1, that you should become a probability sampler with.
**Yuanyuan Zhao** 11:54 No, we never say that.
**jmacdonald** 11:55 Yeah, okay.
**Yuanyuan Zhao** 11:56 And this is only about the randomness and the warning, you see the…
**jmacdonald** 12:03 Yeah.
**Yuanyuan Zhao** 12:04 morbidity warning. We're not doing that.
We're basically turning this into… we erase the… Stressholder value.
**jmacdonald** 12:15 I think I understand, and I think we should just fix that. Is that… so I imagine putting.
**Yuanyuan Zhao** 12:21 Yes.
**jmacdonald** 12:22 That's my…
**Yuanyuan Zhao** 12:23 That's my, PR.
Oh, yes.
**jmacdonald** 12:26 Minimum valid ratio is 1.0.
Okay.
**Peter Findeisen** 12:30 I have a question here, just to better understand what is really the case which you consider as not having randomness value?
Hmm, we… When we were talking about adding this trace state flag, which indicates randomness of the trace ID, we understood that this is Fitting a new behavior into old code, and we should probably assume that even if this flag is missing, if this bit is missing.
The trace ID is random.
We are not doing… anymore?
**jmacdonald** 13:16 Yes, no, that's true still. That's still true. That's what I call the presumption of trace ID randomness.
**Peter Findeisen** 13:23 So, what is really the case where we do not have the randomness value?
**Yuanyuan Zhao** 13:30 It's… We can assume it's randomness. We're still making sampling decisions.
as if it's randomness, right? Like, compared to the threshold. What we're not doing is to inject a TH value Regardless.
**jmacdonald** 13:56 I thought… We… Okay. Man, this is a hard conversation.
**Yuanyuan Zhao** 14:03 So, so the, the, yeah, we've added it multiple times already.
**jmacdonald** 14:09 Now I need to read this closely.
**Yuanyuan Zhao** 14:12 So, what TH value, conveys is basically the probability, right, of a span that was chosen. And conversely, That, how many… Singular spans as this one.
represent. That's the adjusted count.
When you don't have a guarantee of randomness, the representativeness is not… There is no guarantee of that.
What Downstream is doing is that If there is a TH value, then we know it is statistically strong that we can use it to extrapolate What, when the TH value is missing.
We basically… the downstream, okay, I see this, I know it represents something, but I… I just don't know how to extrapolate it, because when we do the statistical extrapolation without statistical guarantees, then the skills is enlarged. So what downstream is doing, specifically the SPAN metrics connector, is to treat it just like today, hunt just for itself. And also, for the metrics that it calculates.
From such a spam, Market that, hey, this is just a counted, that it is not statistically extrapolated.
**jmacdonald** 15:53 Hmm.
**Yuanyuan Zhao** 15:55 I think Josh… so, just one last thing, let me finish. So, I was actually derived this independently when I was doing the implementation, but I think Josh mentioned that this was also covered, in some of the discussions and was brought up by Peter.
Aye.
**Peter Findeisen** 16:21 Well, I have a…
**jmacdonald** 16:23 Please, Peter, go ahead.
**Peter Findeisen** 16:26 Okay, everything you said about TH and missing TH is correct. I just wonder if there is really the case where we have to consider that there is no randomness.
Since we assume the presumed… there is presumed randomness of trace ID, even without the Random bit set.
We always have randomness value.
**jmacdonald** 16:53 Yeah, my take on what was said here is that There's a rule about erasing threshold when you don't trust it.
**Peter Findeisen** 17:03 Yes.
**jmacdonald** 17:04 It's not a rule about randomness like that.
And I… what I heard what you said, Yuan Yuan, was more like you… you were aiming to be even sort of stricter in a probabilistic sense than the… presumption of trace ID randomness would give.
**Yuanyuan Zhao** 17:20 I would argue No.
Because when I was… Oh.
doing the implementation, but based on what Joshua, there was actually another thing that I considered, is that when A span does not have the randomness indicator Or should we just discuss… discuss the spend?
If we discard the spam, that is, presume that the trace ID is not random, but instead, actually, the current code, and also Josh's original code, was to still perform sampling.
Using the trace ID as if it is random. So that's the presumption of trace ID randomness.
Otherwise, we wouldn't use… we wouldn't be using it to… perform sampling decisions.
**jmacdonald** 18:26 So…
**Yuanyuan Zhao** 18:27 Is the distinction clear?
we are still treating trace ID as if it's random, even though there's no explicit indicator.
Because we're still using it to perform.
Some… to, make sampling decisions.
that is treating it as random. Otherwise, it is… Otherwise, we should actually just discard it. Like, for example, if trace ID is 0, or trace ID, yeah, trace ID is just some fix, the max… The 56-bit number.
then, the… we are… it's guarantee… it is definitely not random, and using it to perform sampling decisions is just going to skew everything out. You just export… sample too much or sample too little. That's… That's how we should treat something that's not random, but still using it to perform, to make something decisions is a presumption that it is random.
Right? Because Trace ID, only when it's random can we use it to make something decisions. Otherwise, you're just going to… a sample… Too skewed, your samples are too skewed. Is that clear?
Well, that's my end. Yeah, go ahead.
**Peter Findeisen** 20:01 So… when looking at a single span with single trace ID value.
You cannot figure out whether it is random or not.
You can… you can make some analysis of trace IDs if you really see a set of traces and figure out that they are not random, indeed.
But I don't think we are going into that direction at all.
**Yuanyuan Zhao** 20:26 No, we're not. We're just assuming it is.
**Peter Findeisen** 20:29 Right. Right. So… you cannot make any decision in your code based on assumption that a particular trace ID is not random. Whether it's a fixed value.
It can have… The lower 48 bits can be all zeros, yes, it is possible, and the trace ID can still be random.
So you cannot… I don't see how you can… you can…
**Yuanyuan Zhao** 21:02 That's why we are not… We're not treating the missing of the randomness flag as is that it is not random. We are presuming it's… you see, the presuming trace ID random is still here.
the text over here? Well, still, that's… it's just that while you're raising the TH value from the…
**Peter Findeisen** 21:24 Oh, so… so when there is no… random trace ID flag, you want to erase TH, even though we assume that the trace is random?
Right. I, I, I, I… why?
**Yuanyuan Zhao** 21:40 because otherwise, There is no guarantee of, the soundless Of, the extrapolated flag, and there is no way for downstream to know about it.
In the downstream, we're trading it that if… there is a TH value, then we extrapolate it.
If there is not, then we're not extrapolating it, but we mark it as sep… Using an attribute which essentially becomes a different metrics series.
So people can tell whether this is something completely conforming to the new way, or that this is the old way.
Otherwise, there is no way to tell these two.
Your things are part.
**jmacdonald** 22:32 I wonder if we could use the random bit on the consumer instead of what you're proposing, meaning to say, like.
We're going to presume trace ID randomness, we're going to… pretend that their randomness is good, and follow the rules for threshold, and then in the spanimetrics counter, you can say, essentially, I see this threshold, it doesn't have a random bit set, so I think it's somewhat untrustworthy, so I will, use a different attribute To say, Presumed random trustworthiness issues, essentially.
Otherwise, I think the reason we came with presumed randomness was that the W3C spec would re… Level 1 was not going to ever work for us. So, either we wait for everybody in the world to update to level 2, or we… Sort of presume randomness, and then… there might be cases where it's not, but we, as far as we know, every kind of conforming SDK, unless you go out of your way, gives you randomness, and that's good enough.
But I can see how you would… Add a new strictness mode in the spandom metrics counter.
To detect missing random bits.
Which is kind of along the lines of that warning text that we had earlier.
**Peter Findeisen** 24:03 Right, so… It all boils down to how we understand presumed trace ID randomness. I… I imagine that that means exactly that we assume the trace ID… random trace ID bit is set, even if it's not, so… In other words, we don't even test this bit. We just presume that the trace ID is random.
Now, if I understand correctly, what you are trying to do is to split this into into two parts. One is, well, we will use trace, the random… the bits from Trace ID for… making the sampling decision. However, we are not going to put, TH value out.
So, the downstream sampler, if any, will have to rely exclusively on the sampled flag, meaning, well, it's basically the… The legacy sampler behavior.
**Yuanyuan Zhao** 25:12 So basically, to not extrapolate, because we don't know, It is guaranteed to.
**Peter Findeisen** 25:20 Well, you can always assume that some, some… random… some trace ID generators will be broken, and they will set the random trace ID flag, yet the Lower 48 bits will not be uniformly distributed.
And you cannot detect this. This is a bug.
And we will all, pay the consequences for that. There's no way around it.
**Yuanyuan Zhao** 25:53 Right, there's always bugs, but, I don't think that, It is.
**Peter Findeisen** 26:05 Well, so our approach to presumed randomness was based on Unwillingness to, to move to the new, sampling, world… easier and faster, because we cannot wait until all SDKs will support this random trace ID flag.
It's still not supported for many platforms, for many SDKs.
We even use…
**Yuanyuan Zhao** 26:41 I think this is, this is a good argument, right? So that, if, everything is correct about.
the SDK, an old SDK that some customer application uses… Then, even though they have… they are not upgrading… they have not upgraded.
to the, Trace Context Level 2, but simply by Because that's somewhere way upstream.
But by simply using the, new sampler.
Somewhere in the middle of their service network.
They won't be able to get The correct spam metrics for that service.
I… I think that is a argument to go with still putting TH on.
**Peter Findeisen** 27:49 Yes.
**Yuanyuan Zhao** 27:50 Then, in downstream, like Josh said, we can look further into… The transparent, the flags.
And then mark them differently.
**jmacdonald** 28:13 Yeah, that seems like a solution that I would approve, at least. I think we debated this presumed randomness a lot, and I think it was practical… practically a good decision, but… as you point out, there… you know, technically there is a… and Peter said it, you know, those bugs can happen, and we will not be able to detect them quite as easily.
I do think it's appropriate in the spandimetrics counter to Disambiguate or distinguish between perfectly submitted True randomness bit set and all that, versus… probably… Counted correctly, presuming randomness.
**Yuanyuan Zhao** 28:53 Yeah, so I, I want to say that, that I… I don't think that, bugs is the… reason… That, because we cannot prevent bugs, so that, we will have to accept the, the… the long… non-randomness as if it is still random. I think that… What… what software needs to support is that when people make an explicit choice regardless of bugs. Bags always exists, but makes an explicit choice to achieve To obtain some property, then that property should be supported, even though bugs could happen, because bugs shouldn't be the consideration of… supporting or not supporting what? That's… that's what I think. But I think that the… the, supporting Existing applications.
Was partial… upgrade. That's a compounding argument.
So they don't have to, like, upgrade everywhere.
Or at least at the upstream in order to get something.
**Peter Findeisen** 30:23 Yes.
**Yuanyuan Zhao** 30:25 So, then the existing… Spam mattress connector, I think the current… Implementation is still correct, because we are treating the TH value… if there is a TH value extrapolated, if there is no TH value, we count it, because that's the backwards compatible behavior.
With this, right, the TH value, the existence of TH value, Now, has two cases.
One is that there is guaranteed statistical, I mean, bugs aside.
**jmacdonald** 31:08 The, the, the big…
**Yuanyuan Zhao** 31:09 There is guaranteed, yeah, statistical accuracy over there, and then there is another that it is not guaranteed, so we need to… add… a case… In the extrapolated… is… That's what we want.
I think the current is still be… still… is still the same.
The current behavior in spametrix Connector.
It's still, valid, except that we need to further submit They extrapolated the case into two, whether it's accurate or whether it's not accurate.
Or do we want to?
Distinguish it at all.
**jmacdonald** 32:00 I'm trying to enumerate the type, the, the… I'm so tired of spelling corrections, I'm just gonna do that.
So, there are 3 cases.
I'm making up names, and then… H… not present.
Don't care.
**Yuanyuan Zhao** 32:28 It's just counted. Like, what is done exists, prior to… All of our changes.
**jmacdonald** 32:36 What did you call that? Unknown, or…
**Yuanyuan Zhao** 32:39 It's actually counted.
TH not present is actually counted. That's today's case.
**jmacdonald** 32:45 Okay.
**Yuanyuan Zhao** 32:46 It's basically everything counts as one by itself.
**jmacdonald** 32:52 So… Ew.
it sounds okay to me to distinguish these cases, and I feel like that would give you what you're hoping for without I guess what I'm thinking of is a setback to the spec. Like, if we have to wait for Level 2, before this spend and metrics thing's work… thing works, I think we're… we're not gonna… see success.
So… But, but…
**Yuanyuan Zhao** 33:24 Not a necessity, right?
we don't have to wait for… I mean, It can be… incremental.
And that was why we are doing this.
pres… presuming The trace ID is random.
**Peter Findeisen** 33:40 Right, but the second case, when the randomness bit is not set, you will always hit it in case there is at least one Sampler, which is, not level 2 compliant.
Because Level 1 is… has… In Level 1, the sampler is expected to clear all the bits which are not known to Level 1.
And this includes randomness bid.
So, your first case will happen only when all the samplers in your environment are level 2 compliant.
**jmacdonald** 34:23 Or every parent to your root span, essentially.
**Peter Findeisen** 34:27 Yes.
**Yuanyuan Zhao** 34:28 Well, if… If a sampler In the middle of the service network, in the service chain. Chang is… Erasing unknown flags.
then… What's a truly random… trace ID appears unknown.
4… The probabilistic sampler downstream, and we were arriving to the second case, even for something that's truly random, right?
**Peter Findeisen** 35:03 Yes.
**Yuanyuan Zhao** 35:04 The, the… But the second case is still valuable, and doesn't require everybody to upgrade.
At the same time.
Aye.
**jmacdonald** 35:24 Yeah, I think that's why we were aiming for this presumed randomness solution.
Yeah.
I'm gonna say, like, almost… Certainly… And, and… We expect correct count… accounting.
But… I think it's worth distinguishing, so that there are… 3 outcomes, counted.
extrapolated, and… Presume counted, or whatever, like… Probably… probably there's a good word for that, presumed, counted.
But I… I would… I would oppose any… I think I would oppose the effort to… to clamp down on the samplers themselves.
So that they are required to… Erase threshold if the sampling… if the random bit is not set.
that… from their… from their context. I think that would set us back in a way that doesn't benefit us very much.
**Peter Findeisen** 36:29 Yeah.
**Yuanyuan Zhao** 36:30 So we're going to keep the TH value, right? That's what we're saying now. Okay, I think we're on the same page now on this.
**jmacdonald** 36:38 I mean, not taking… this change is not what we want.
**Yuanyuan Zhao** 36:44 Yo, we're gonna just close it.
**jmacdonald** 36:46 Okay.
Thank you.
I will let you… do that.
So I think we… I think this issue is… is we're deciding not to do this as well.
**Yuanyuan Zhao** 37:01 Right.
**jmacdonald** 37:05 And there was… Is that okay with everybody, if we move on from that? I would prefer to see the expanded metrics count three ways than to change the spec.
**Yuanyuan Zhao** 37:19 So we're not going to change the spec. This comes down to, do we actually still care about distinguishing the first two cases?
**jmacdonald** 37:29 Well, I don't, necessarily, but if you did, I wouldn't blame you.
I brought up…
**Yuanyuan Zhao** 37:39 Is there another way?
**jmacdonald** 37:44 Well, I feel like we're just choosing between whether to wait for W3C Level 2 And have it correct in a more… in a stronger sense, versus… Probably having just about the same outcome without waiting.
**Peter Findeisen** 38:03 So, I wonder what would be the impact on end user of OpenTelemetry. So, in first case, when TH is present, random bit is set, we have this true extrapolated case.
The user will see the metrics, perhaps with a warning that they are… these are extrapolations, and can be a little bit inaccurate.
what would the user see in the second case? Well, the values would be the same, the warning would be kind of the same, but would it be stronger?
That something is possibly wrong, or… How do you see that?
**Yuanyuan Zhao** 38:45 We don't have a warning in the first case, right? We won't have one. It's truly extrapolated.
**Peter Findeisen** 38:50 Well, but… well, the warning is probably not the right word. We inform the user that these are not accurate collect-counted values, but they are extrapolated. Maybe it's not with every single value, but somehow the user should be aware of that.
**Yuanyuan Zhao** 39:07 I… we do… we are currently doing… one and two, It's the same case.
And third is another one weeks, we… Separate whether it's counted and extrapolated.
**Peter Findeisen** 39:24 Right, the third case is the legacy case.
It's counted, and the user is… it's fully user responsibility to have it proper, to have the proper count.
If… yes.
But, I wonder what's the difference between a first and second case?
**jmacdonald** 39:45 I think that all it says is not all of your environment is using W3C Level 2.
**Peter Findeisen** 39:49 Right. Well, which means… what does it mean for the values?
**jmacdonald** 39:58 that we are left to doubt the presumption of randomness, I think.
**Yuanyuan Zhao** 40:04 Yeah, that was why I'm asking, too. We actually want to distinguish the 1 and 2 now.
**Peter Findeisen** 40:17 Well, again, this is something that the users will certainly have no impact on, right? They do not really control their trace ID generators in most cases.
**jmacdonald** 40:37 the reason why we wrote those warnings into the spec is kind of to try and put some flag up for somebody about the fact of this, and I think it…
**Yuanyuan Zhao** 40:47 If we… if we don't… so… If we don't distinguish the first two cases.
What's the point of the randomness flag, then?
If I'm… because we're already presuming trace ID is random, so the randomness fact has no use.
Yes.
**jmacdonald** 41:06 Yeah.
**Yuanyuan Zhao** 41:06 That's… it actually comes down to that question.
**jmacdonald** 41:10 That… but that's what… yeah, that's what led us to the presumption anyway, is that W3C kind of made a mistake, and we didn't… we didn't want to wait longer?
We didn't want to wait for Level 1 to be retired.
So, I don't really see a huge value, I'll be honest. Right.
In it.
**Yuanyuan Zhao** 41:33 This also brings the question to the randomness flag.
In… transparent.
**Peter Findeisen** 41:42 So, so, I would hope where…
**Yuanyuan Zhao** 41:44 Policing has no use.
**Peter Findeisen** 41:46 Well, currently, kind of, you are right.
But once… Most, if not all, SDKs will get upgraded to Level 2, we can… Tighten up our implementation and drop the presumed randomness assumption.
Without hurting The customers, without hurting the users.
So this is something for the future, really. But at this point.
Since most of the SDKs are still at level 1, There is no other choice, we have to assume randomness.
**jmacdonald** 42:24 There are 4 cases.
**Peter Findeisen** 42:32 Well, right, RV present is the same as randomness bit set, effectively, right? So, this explicit randomness, you can enhance the first case for that.
**jmacdonald** 42:45 Yeah, okay.
**Yuanyuan Zhao** 42:46 I mean, the RV case… RV case is basically randomness flag set, trace ID is there, so that's… That's not a new case.
So, what Peter just brought up is we change the behavior.
To make it a more strict, Such as… Either discard, The span?
Or… that was actually something I thought before, but then I figured it was, .
**jmacdonald** 43:23 One thing you could do to just make an option out of it for being, I guess, pedantic or something like that would be to make a Boolean flag. You either get to choose presumed extrapolated as true extrapolated if you trust the presumption, or you can count it as counted, which means you don't trust it. Leaving two choices, then.
**Yuanyuan Zhao** 43:42 Yeah, we're currently having only 2 cases.
And, it's… Only that's the, the, absent of randomness, where it forced into. We're actually changing from counted to extrapolated. That's the change.
Today.
**jmacdonald** 44:08 I will support the change. Basically, anything we can do with spam metrics, I support.
But I… can I… can I bring us now to the second topic? Because there were two threads here.
And we've just covered this one about… about… Well, we already covered this one.
This one here… was that the code is described in text. This, if there's randomness.
Or it has the random flag.
we… then update the TH value, but if there was not a randomness flag.
Wait a second… Sorry.
Erase, trace state THC, so… Ugh.
**Yuanyuan Zhao** 45:03 Basically, we are going to remove the condition.
**Peter Findeisen** 45:06 We don't want this behavior. I think this is what we all agreed to.
**Yuanyuan Zhao** 45:12 Right, so it's 71 only. That's what we're gonna do.
**Peter Findeisen** 45:16 Yes.
**jmacdonald** 45:21 Yeah, this doesn't look right anymore, but there was something… But I… I misread it when I… when I responded. This is my confusion now, is that there was a rule And I… I linked to it.
Which is similar, but not the same, which says.
Which says, if sampled incoming threshold is apparently inconsistent, erase it. But that's not the same code that we were just looking at.
And I think this rule is not written in the SDK spec.
**Yuanyuan Zhao** 45:52 It's simple.
**jmacdonald** 45:53 And that's what… and that's what I flagged, because, Tyler is… is, strict about specifications, and he won't let this through without fixing it, basically.
**Yuanyuan Zhao** 46:07 Can you show us the text again? The ones that you said is not there?
**jmacdonald** 46:12 Well… It's this… It's this… it's this here.
Let me make my text bigger. Sampling incoming threshold is apparently inconsistent, erase it.
This is… These two rules.
**Yuanyuan Zhao** 46:34 are important.
**jmacdonald** 46:36 And they are not encoded in this document.
here.
Where they probably should be.
So we don't have anything about erasing incons… If the parent threshold… Is inconsistent, we erase it.
And… If you're doing a probabilistic If you're making a probabilistic decision, You're supposed to erase randomness.
At some level, I'm… ugh, I did not come prepared for this.
Okay.
I feel like I need to study this topic a little bit more, but… but my… I believe I'm still… this… this is still true.
And that we probably need to fix this.
as well.
I was reading this code as being that same rule.
Okay, I have… I have… I feel like I need to do my homework now.
And I don't have anything useful to say.
Yuan Yuan, I think it would be, I think I need to go… Ugh, I'm not able to keep up with this.
**Yuanyuan Zhao** 48:24 What does a sampled incoming threshold mean?
**jmacdonald** 48:30 Do you see a threshold?
And its randomness value is out of range for it being sampled.
Folks, I don't feel like we're being… we're being productive. I can't think while I'm talking to five people either, so I'm afraid that I… Feel that we should postpone this discussion right now.
**Peter Findeisen** 49:05 Okay.
**jmacdonald** 49:05 And take it offline.
**Yuanyuan Zhao** 49:11 Assuming the discussion of probabilistic sampler, not the parent basis threshold thingy.
**jmacdonald** 49:19 I mean, whatever it takes to get this PR finished, but focusing on the sampler, not on the spandimetrics question that we were talking about.
And I… and that means there's some point at which you erase something, and that's what we need to get right in a spec.
**Yuanyuan Zhao** 49:38 Okay, let's take it offline then.
**jmacdonald** 49:40 Yeah, okay. I'm sorry about that. I feel like I… either I have to sit and think while you watch, or something like that, or we all have to sit and think, and we're almost out of time anyway.
Okay, let's, let's, take this to Slack.
And, I'll try and give it some attention over the next couple days.
Best I can say. Sorry, everybody. I think we should end this call, otherwise I just feel kind of like I don't have anything useful to say.
**Yuanyuan Zhao** 50:10 Sounds good.
**jmacdonald** 50:11 Sorry about that.
**Peter Findeisen** 50:13 problem.
**jmacdonald** 50:14 Okay.
See you on Slack, everybody.
**Yuanyuan Zhao** 50:17 Okay.
**Peter Findeisen** 50:17 Yeah, bye.
**Yuanyuan Zhao** 50:18 Yeah, bye.
**Carson Ip** 50:19 Thank you, bye.
