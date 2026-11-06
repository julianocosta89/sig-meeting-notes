SIG: Sampling SIG
Date: 2026-11-05
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Peter Findeisen** 01:30 Hello?
**Joshua MacDonald (Microsoft)** 01:33 in the morning.
Good thing.
I have news from… I have… I have sampling news. I'm so excited.
I mean, at least in the way of progress.
I'm going to share with you that some progress was made in Rust. That's not a great deal of news, but it's news.
October 22nd didn't happen. Yep, I remember that. I was there. Haha.
So, I only have that kind of news, and… There are 3 of us today.
And, but that's not… that's not nothing. Let's go see.
Where did I find that? It was posted in the… Sampling.
No? Yes. No. In Rust.
Yeah… Well, here we go. I found it.
I'll… I'll put it on the screen.
I'll put it on the screen. Wait, are you seeing my screen right now?
**Peter Findeisen** 02:55 Yes.
**Joshua MacDonald (Microsoft)** 02:56 Good, okay, good, okay, good.
Over a year ago, I filed this issue in Rust, asking for an implementation of the consistent Sampling probability Sampling stuff.
And put a bunch of links, and then a year later, someone picked it up. Almost coincidentally, I said I was going to push on Rust two weeks ago, or 4 weeks ago, and here it was. Someone else was doing it. It was, like, very well-timed. So, So that got done and then merged, and I haven't seen another one yet, but I feel like I maybe wouldn't have seen it.
So I don't see any more references to this.
But, it was, A complete implementation of… probability, and… parent-based.
for new probability samplers, and I pointed them directly at the work that Yuan Yuan did, and Chris followed with. So, my guess is there's a work… this person will also work on adding Jaeger Remote Sampling support, exactly like Chris did in the Go Contrib.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 04:06 Excellent.
**Joshua MacDonald (Microsoft)** 04:07 That's my… that's the… that's the news that I have for us.
That's a great gift.
**Peter Findeisen** 04:15 Yep.
**Joshua MacDonald (Microsoft)** 04:16 There's that.
And… I was hoping, I'll say briefly mentioned… Oh, someone else is typing.
Chris might have something to add.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 04:36 adding agenda item.
**Joshua MacDonald (Microsoft)** 04:37 Okay, great. And we have, a new visitor, that we might want to say hello to as well.
Let's see… I was going to make a remark, which I can put on the agenda after Chris's, and then I'll say hello to Juan. This is usually a pretty small meeting, so I wouldn't mind saying hello to you. You are here, and I am here as well. But welcome to Sampling SIG.
**Juan Vega** 05:05 Hello, thank you.
**Joshua MacDonald (Microsoft)** 05:07 And, okay, Chris, let's talk about your… your topic.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 05:11 Yeah, so this touches on, we've talked a little bit about, invalid or invalid, how can we mark traces as, I don't want to include this as metrics?
Kind of the last time I brought this up, we were like, I was pretty well convinced that, like, oh yeah, we don't need this, like, you'll just mark everything as 1.
I ended up with another, talking to some other customers who have brought this up again, and for a slightly new use case, which is, we have built a feature Where we allow customers to restore traces. So, effectively, other companies, other products have this too, where, like, you keep an on-disk or an in-memory cache for X amount of time, and if someone has a trace ID, you can pull it out of that.
Otherwise, it just… it gets removed after a while.
that, if I was to, like, represent that as, say, a tail sampling policy, the tail Sampling policy would look something like… This trace will happen to be clicked on, or something like that, if you could magically do that.
And at which point, we would restore it.
And then it can get included in TraceQL metrics, or any, like, anything looking… creating… trying to create metrics out of loading traces.
It'll suddenly start being included with a default of multiplier of 1.
Or whatever was in the trace state, but, like, it defaults to zero.
That doesn't seem accurate to me anymore, because you can't, like… That policy of somebody might click it, or somebody will click it, is not… is not real, like… somebody might click something that also was multiplied by 20, or something like that. And we already saved multiplied by 20 on a different one, so the same logic we used last time, where we just always take the highest… Or, I guess the lowest multiple doesn't really hold up here, and I was curious, yeah, what others' thoughts are. Did I explain that problem well enough, I guess, and what thoughts there are here? Right now, the workaround is, like.
stick an attribute on this, and then filter away the attribute… filter away any traces that match the attributes of restored, but I don't love that.
**Joshua MacDonald (Microsoft)** 07:41 I'm not sure I followed, and I want a little bit more explanation.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 07:44 Okay.
Yeah, so… okay, so yeah, so we have a… so we have a feature that… Effectively, like, if somebody puts in a… if somebody has an exemplar, or something like that, that isn't sampled by a tail sampling policy.
For whatever reason.
But then they go and they click on that in the next 24 hours, and they actually open up, we will… Pull it out of… we will go, we will pull it out, and we will send it to our long-term storage so that people can reference it, say, during an incident or something like that.
The problem is now that trace that previously was not sampled and should not have been sampled will now count towards… Any sort of metrics.
A lot of the time, doesn't really matter, it'll be overwhelmed by all the other traces, but we've had some heavy users of… This feature where it's enough traces that it will affect the metrics.
That they then try to analyze later on.
**Peter Findeisen** 08:48 So, if I understand correctly, you plan to… Calculate some metrics.
on… Exemplars?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 09:03 It's not just exemplars.
**Peter Findeisen** 09:05 It's on any channel.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 09:06 races, though.
**Peter Findeisen** 09:06 I understand, I understand, but… so… so… My assumption would be that all the metrics are calculated immediately as soon as you are finished with your tail Sampling. It… I don't expect anyone to calculate metrics based on long-term storage, because the metrics should be calculated sooner And calculating metrics, on… on a smaller set of traces, because I agree, these… This selection can be random, can be logical completely from the sampling perspective.
It makes little sense, in general.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 09:53 So, the… the use case here is commonly, like, you will, yeah, you will create your metrics right away, but those are very hard-coded. You have… I use these attributes to create my metrics, that's all I have.
Suddenly, somebody wants to create metrics that was, oh, for this specific tenant, or some sort of attribute that was not part of their metrics generation… original metrics generation pipeline.
They want to… Go and… they want to, yeah, effectively run metrics, still get extrapolated values of… Approximately how many requests did this tenant send?
Something like that, where they did not have that information on the metrics they already created. Does that make sense?
**Peter Findeisen** 10:43 Yes. So, basically, new metrics which did not have a definition sooner, it's a… ad hoc metric created later. Yes. Okay. Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 10:57 Juan, it looks like you have your hand up.
**Juan Vega** 11:00 Can I contribute, or… I mean, I don't know if…
**Joshua MacDonald (Microsoft)** 11:03 Please.
**Juan Vega** 11:03 Okay, yeah, we have a similar feature where every span… Where, or everyday generates metrics.
And if I understand in you, you want to propose, like, a standard way of filtering out, traces that shouldn't count towards the metric, no?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 11:22 Yes, yes, that they would skew the extrapolated results if we counted them.
**Juan Vega** 11:28 That is nice. What we do right now is using an attribute, as you said.
But yeah, it's… more common than I expected, that customers realize that a span that shouldn't… Count over symmetric is counting.
Yeah.
It would be interesting to have, like, a way of filtering them.
on… Yeah, tracer State, or… Yeah, delicious tag would be great. Nice, I guess, I guess.
**Joshua MacDonald (Microsoft)** 12:00 I have… I feel like we've discussed variations on this problem in the past, and the way I have tried to phrase this is that I… always have felt that I wish we had a way to express that zero The zero count.
And we… and it's been proposed and sort of shuffled a few times, never got there, right? And so, what we have instead is saying that if you leave off the… Parent threshold, or the threshold, sampling threshold.
Then it's unknown, and if you are disciplined, you can treat unknown as 0, but most… mostly people treat unknown as 1, count of 1, and therefore, when you send a span to storage that was not sampled, and doesn't have a valid threshold, you're likely to count it for 1, not 0, and there's nothing explicit In our semantic convention that lets us count zero.
And, and we could imagine it being a trace state entry.
I want to add that I actually put this next topic here because someone came to the specifications SIG earlier this week and presented this idea, and Mostly got pushback from the, from the, the group.
But I was… and I wasn't able to make the meeting, so I listened to it after the fact, and, you know, I kind of wanted to say, hey, but we have this whole bunch of work on sampling that's basically designed so that you can have span-derived metrics be correct, and and the… the thing I wanted to emphasize for that particular topic, which I think bleeds into this one, is that, it should be possible, in my opinion, to just write your sampled spans into storage, and then query them dynamically and generate metrics. And that's like a dynamic filter that you might apply. And that's where we hope that the sampling is unbiased, because then you can go.
find every span with user X, and then make some metrics from it, and that says metrics for user X.
metric.
And, so I endorsed the idea, and I still think we don't have a good way to say zero.
And… I don't… I've always kind of wanted it, so I guess I support the idea, but I don't know… what, what are the thoughts and implications on it? Like… as a straw man, I've imagined putting into the OT trace state entry, like, another Two letters to say.
zero. Something. Like, an intentional zero marker, but I don't know what to call it, so that's all I have.
**Peter Findeisen** 14:46 Yeah. The problem, the way Chris defined it, is really a storage issue, backend issue, and I don't think that we have any specification in OpenTelemetry that would Guide, not even control, but guide back-end how to deal with that kind of issues.
So, in our product, we have… we have a similar feature, so to speak. If someone clicks on a trace views it, it will be preserved longer than those traces that were never seen. Those traces which are not viewed are gone within one week. The traces that were looked at Are preserved for a longer period of time.
So, I… I understand where this problem can come from, but again, it's… it's a back-end problem.
It would help to have something that indicates the zero adjusted count, yes, but this use case is a little bit outside of our scope, I think.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 16:06 Yeah, I guess, yeah, I guess the question is, is it, like, if it's a backend issue, and, like, we can each implement it our own way?
That seems fine. Like, is this a feature that we would want to, say, be able to support in the tail sampler?
In the collector, where it has some level of, like, we have on… we have the on-disk storage now.
Would we want to be able to support pulling things out of that storage? And now we are in that, like, it would be in that collector level.
And at that point, I would say it is somewhat in the purview. That said, if we want to say, no, we're just not gonna support that.
I'll keep using an attribute, or, hardcode something. Figure something out for just our product, that's fine.
**Joshua MacDonald (Microsoft)** 16:54 What's the name of the attribute? Like, just for imaginary purposes? Like, don't count me?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 16:59 Yeah, we could do Don't Count Me, we could do, like, I think ours is rehydrated, but yeah, let's call it Don't Count Me, yeah.
**Joshua MacDonald (Microsoft)** 17:06 Which means, approximately… No threshold is known.
And… and I think the way I would turn this into… Something that we care about specifying is to be… If you are a tail sampler who is sending spans, and you… Are… Well, I guess what I mean is, I think we need a policy towards accepting spans that have unknown thresholds, since If we're rigorous about the missing threshold means unknown means zero, then everything's fine.
So, if the tail sampler can Be very loud or reject when it doesn't get thresholds, then… It can be rigorous and only pass thresholds that are non-zero, and when you… when it wants to send something that is zero, it… Puts that zero?
Or it omits the threshold, and it… by agreement, you mean that's a zero, because there's no threshold.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 18:19 Yeah, but the problem with that is it falls down, like, if an SDK has an issue, you're supposed to strip out the threshold.
And then, like, you just… Like, oh, a service was misconfigured, now you just have nothing, is… I don't know. It's not… it's not a graceful fallback, I would say.
**Joshua MacDonald (Microsoft)** 18:38 Yeah… The other, there's, in one of the… There's, Sampling priority equals… 1… Like, there's a sampling priority mechanism that some of the legacies have, and There's a way to force a trace through the probability sampler, for example.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 19:04 Yes.
**Joshua MacDonald (Microsoft)** 19:04 Using something like this, and… It's just another attribute.
approach.
In logs, it's… or 100. But… That's a disagreement in that code.
What would you do if you could, Chris?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 19:35 I would love to add, yeah, some sort of signal to trace date. Part of that is just, I don't want to really be pulling an attribute to filter stuff out, like, that's just more work on the storage systems and… Like, yes, it's missing most of the time, so it's not too bad.
we already have to pull trace date, so I would love there to be some sort of trace date if we want it to be part of… the OT equals part, that would be great. I could also add a… like, for us, I could add a tempo specifically, I could add a, I don't know, GF or something for Grafana ones, and have it be a… be a custom piece of trace state.
Yeah, like, you could do…
**Joshua MacDonald (Microsoft)** 20:18 Zero count.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 20:18 zero count, or something like that. Like, thresholds missing, zero count. Something like that I would be happy with.
But yeah, mostly I wanted to know if this was something we wanted to support, or if I should go the custom route.
**Joshua MacDonald (Microsoft)** 20:40 I would suggest that this is, like, there's a sense that this might be useful beyond just your backend.
But there's also some skepticism. Maybe what we do is put, Experimental feature into their tail sampling, saying, And the only problem is that, you know, like, it would… this might… You know, you could imagine adding to the trace state handling document that says what those characters mean, and you could add a placeholder saying, we're gonna… Reserve an experimental code that says zero count.
And we're gonna use it, and… It's… You're safe… you're free to ignore that if you… if you didn't know about it, or you don't want this new thing, and at least it gives the tail sampler a way to… Convey what, what you're interested in.
And I… and I would go back to the other sampling components, like probabilistic Sampler, which does have a way to pass through data as well, and doesn't do anything special other than this sampling priority, like, flag, which is not standard in any way, or is not written down as a standard.
**Peter Findeisen** 22:00 Do we want to allow this zero count to be present together with a threshold?
Or it would be much more exclusive.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 22:14 If we move it out of experimental, I would probably want it to be mutually exclusive.
Like, we would still have a randomness.
But exclusive with threshold.
**Joshua MacDonald (Microsoft)** 22:30 So you could also have it be, like… this would be breaking the pass, but you could do TH equals, like.
Something that doesn't parse.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 22:41 Yes, but…
**Otmar Ertl (Dynatrace)** 22:44 What would be the use case to have this… the randomness on it?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 22:53 Would you repeat that?
**Otmar Ertl (Dynatrace)** 22:55 Whoops.
So, so you would like to have the randomness still on the… on the span, and…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 23:03 I think… I think so? I'd have to give that a little bit more thought, like, I think it could still be useful, but it might not be needed at all.
**Peter Findeisen** 23:12 If we have randomness derived from trace ID, there is no way to remove it.
**Otmar Ertl (Dynatrace)** 23:18 Yes, you're right.
But if there is explicit randomness, I'm not sure if this is useful in this case.
You gotta be autistic.
**Peter Findeisen** 23:28 It could be dropped, it could be dropped. Well, with… Otmar… Overriding TH with this extra value will complicate a little bit parsing, I guess, and… ParsingTH is an operation that will be performed extremely frequently, so I would be a little bit cautious about how we proceed with details.
**Joshua MacDonald (Microsoft)** 23:53 Yeah.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 23:54 Yeah, I prefer the separate, I prefer the separate, like, let's reserve something separate that we can just quickly check.
**Otmar Ertl (Dynatrace)** 24:06 One question. So, it's basically that the key problem is that you potentially send spans twice, right, to the back end.
Or… to storage. So, because it could be sampled, right?
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 24:19 Yep.
**Otmar Ertl (Dynatrace)** 24:19 And then you store, send it again to the storage.
So Vincent, you had…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 24:29 It probably depends on the storage. We don't have that problem too much, like, we only go through this path if we know something wasn't sampled.
So I think that would depend on the implementation, but, like, it's definitely possible.
**Joshua MacDonald (Microsoft)** 24:53 I would… that, for me, is a separate issue, like, whether the storage system can deduplicate or miscount when you send the same span twice.
Especially if you send it twice with different.
**Otmar Ertl (Dynatrace)** 25:04 Nice.
**Joshua MacDonald (Microsoft)** 25:04 These states.
**Otmar Ertl (Dynatrace)** 25:06 Now I am wondering, for this use case, because as it is written here, that the spam is not sampled, but what does not sample mean that it's generally not sampled, or it was just by chance not sampled?
But it's going through a sampling process, but it was not chosen to be sent to the storage.
So, I mean, this is, because if it's… it's the case that, you know, it's… Going through a sampling process, but it was not picked.
And then you send later again the spam, you know, then you have… it has basically two chances to end up in the storage.
And therefore, you have to set one of these spans to zero.
or the weight of those spans to zero to not overcome this span, right? This is… this is the problem.
If you can deduplicate on the storage side, then you could say, okay, first I have Sampled my spam with, let's say, 10% probability, right? But later, I decide to, Sampled the spend with 100% probability, then you could just override the span, which you've already struck before, with the new With the new, Wheat, you know, to…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 26:31 I think a nice part is if we… if we have this zero count.
and the storage doesn't deduplicate, then at least we wouldn't be double-counting it anymore, correct?
**Otmar Ertl (Dynatrace)** 26:43 Yep.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 26:44 So that… so… I think… This at least helps.
**Joshua MacDonald (Microsoft)** 26:49 That sounds right.
Interesting.
Well… Maybe we should think about this.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 26:59 Okay.
This gives me a good… I can at least experiment with this for our system.
And, like, open up something that… Yeah, tries to reserve.
zero count of ZC.
**Joshua MacDonald (Microsoft)** 27:14 Well, that's…
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 27:16 Good direction for me.
**Joshua MacDonald (Microsoft)** 27:17 It's worth, like, thinking about it, yeah. I think I would support that, but, but I'd love to hear what the others think, too.
**Otmar Ertl (Dynatrace)** 27:28 I mean, during the execution process, you… and you see, I mean.
the same spam twice, yeah, you could deduplicate on demand, right, and then just take the… The… the highest threshold, right?
And… That's it.
Yeah, so if… I mean, it's… it's basically… Yeah.
After your implementation, how to deal with that.
But, not choices.
We need to define zero.
Yeah, in the standard.
**Juan Vega** 28:11 But this could be also used by customers that have two storage, you know? Like, because in your use case, you own the two storage.
We have seen customers actually using two different storage, one internally and another from the vendor.
So, they could maybe want to… What I have seen is that sometimes they want to send traces that… They… they maybe haven't been sampled on their storage, but they want to To have it, upstream for some reason.
So you don't always, like, as a back-end or as a vendor, you don't always have knowledge Of the full use case, like, this was previously saved and then recovered.
**Joshua MacDonald (Microsoft)** 29:04 Trying to think, does that mean we're… you're thinking that we might have a scenario where a tail sampler sees the span, and then… sends… 100% of the data to the customer, But… 1% of the data to a vendor.
And… Yeah, I guess I haven't… I don't see how to… I don't see exactly how the… the sampler is going to be involved in both of those paths to the… to the custom… to the vendor and the customer's own store.
**Juan Vega** 29:47 Well, I mean, this is theoretical, because maybe Chris has another use case in mind, but I don't know if this could be used for that use case. Like, a customer is sending 100% two traces to their own storage, and then they notice during a period of time, or… Whatever they need to recover some traces?
And those cases were sampled on the vendor, or even were sampled on their own Sampling collector?
And they decide to resend them to, to the vendor, but they don't want them to count for Medic, they don't want to count anything. And sometimes even the… The trace state is not used at all.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 30:26 Yeah. Yeah, we've heard this, like, as, like, archive… Like, they have some sort of trace archive or something that they might want to restore data from.
**Joshua MacDonald (Microsoft)** 30:38 It sounds like that what they want to do is store some data and not pay for it, and then, oh, there was an incident, I'm gonna send all that data to the vendor so I can use their system to analyze what happened.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 30:50 Yep.
**Joshua MacDonald (Microsoft)** 30:51 Interesting.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 30:51 Like, yeah, they wanna, yeah, they wanna store it really cheaply, and then restore it only if something bad happened.
So yes, I think it would be a similar process there of, like, we probably… because some of those traces will probably be deduplicated and things like that when sent to said vendor.
So yeah, we'd probably want a similar zero count there to avoid… Double counting or misrepresenting all of the things that weren't sampled originally.
**Joshua MacDonald (Microsoft)** 31:24 I think if we make this a hypothetical exclusive with threshold, it won't bother people very much that don't care.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 31:34 Cool.
**Joshua MacDonald (Microsoft)** 31:37 The reason I put this, next item sort of in our agenda, there's no… I actually invited the author to come talk to us, not… I think the author didn't understand why I was inviting them, and didn't see the connection, so there doesn't have to be a connection here.
But this was a proposal that, comes from AWS. They have a lot of span instrumentation and don't have as much metrics. That's the way I understood it, basically. And I've seen that type of codebase.
That has a heavy span instrumentation and not… A tremendous amount of metrics.
Or they prefer their span coverage, and would like to see metrics derived from spans.
But sometimes you hear this request, and it's mainly asking for SDK support, so I would like to not send spans from this SDK, I would like to turn them straight into metrics, and then send them. And shouldn't we have a semantic convention for that?
Because today, the only semantic convention that exists that we have is in the spandimetrics connector in the collector. And the question is, is that a semantic convention, or is that just the behavior of one component in the collector?
because this is asking for SDK support that does the same thing, and it would make sense to me to… follow the same conventions, and the reason why I'm talking about it here is that the whole point ofandom metrics, or the whole point of sampling, in my opinion, is so that we can draw metrics from spans, and if we're going to do that, we should have conventions, that both work on the SDK or in the collector, and work with sampling, whether it's on the collector or the SDK. So, I think these are connected, even if the original poster didn't seem to agree with me, and I wanted to just mention it here. That I think it is worth us having semantic conventions so that users who want metrics can take them from their spans correctly.
And that was basically just an FYI that that's sort of stirring, and at least one person asking for it.
if that interests you, I guess, follow the issue, or… I have a thread with this person on Slack, and anyway, it's something in discussion.
**Peter Findeisen** 33:53 So, in this use case, they are not… they do not want to pass any traces to the collector, or a backend, or anything. They are just… they just want to see metrics based on spends.
Do I read it correctly?
**Joshua MacDonald (Microsoft)** 34:11 Yes.
**Juan Vega** 34:14 But do they use sampling? Or, I mean, all the spans in the SDK generates metrics, or do they have some kind of sampling.
**Joshua MacDonald (Microsoft)** 34:21 That's the rub here, is that the way they're thinking about it, there's no sampling. The reason that they're doing it in the SDK is so that they can get unsampled metrics from…
**Peter Findeisen** 34:33 Yeah, it's.
**Joshua MacDonald (Microsoft)** 34:33 Oh my gosh.
**Peter Findeisen** 34:34 ZK, you'll see all spans, regardless of whether they were sampled or not.
**Juan Vega** 34:38 Hmm.
**Peter Findeisen** 34:39 So… Sampling cases are… Different color.
**Joshua MacDonald (Microsoft)** 34:43 If you're doing this, it doesn't make sense to sample, but I'm trying to say that you could have… an arrangement where you send the spans to a collector, who then samples them, who then turns them back into metrics, and you should get the same expected values for all your metrics, and you should get the same semantic conventions for your metrics. That's what I'm… that's what I'm envisioning.
So it's really just a call for consistency across, spans… or metrics derived from spans in the SDK, and metrics derived from spans in the… in the collector, is all I'm… is all I'm proposing.
But it was mostly just an FYI.
I… while I have seen a codebase that was heavily span-oriented, the way that it was done, they also had metrics, so I've never seen this actually happening.
But I… it's… hypothetically, I've seen it in the… in the sense that I've seen… Codebases that are very trace-heavy and not very metric-heavy.
Mainly at my old company, where we did a lot of tracing, so… Anyway, there you have it.
And thank you all. I think we've reached the end of an agenda.
Next week is KubeCon, but we don't have a meeting next week, so… nothing to cancel.
If you're at KubeCon, I'll be there for two and a half days.
In case anybody… I don't know if anybody is, but… So, thank you all.
**Chris Marchbanks (Raintank, Inc. – Grafana Labs)** 36:23 Moon.
**Juan Vega** 36:23 Okay, thank you. Thank you.
**Joshua MacDonald (Microsoft)** 36:26 Alright.
