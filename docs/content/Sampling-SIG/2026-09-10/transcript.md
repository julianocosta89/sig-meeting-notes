SIG: Sampling SIG
Date: 2026-09-10
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Andreas Gruber (Dynatrace)** 00:33 No, that's a different meeting.
**Otmar Ertl (Dynatrace)** 00:39 It's a different one, but it's still not the one we're coaching.
**Yuanyuan Zhao** 00:44 Siria for a second.
What do I do?
**Otmar Ertl (Dynatrace)** 00:51 I can… Yeah.
Great.
There's a little response time.
**Yuanyuan Zhao** 01:03 myself and, and turn off the video, so I can do some work while I'm waiting.
**Otmar Ertl (Dynatrace)** 01:10 Yeah, sure.
**Yuanyuan Zhao** 01:11 But I'll be here if the meeting is still on.
See ya!
**Otmar Ertl (Dynatrace)** 01:20 Yeah.
**Andreas Gruber (Dynatrace)** 01:21 I will also wait a couple of minutes.
**Otmar Ertl (Dynatrace)** 01:24 That's true.
**Andreas Gruber (Dynatrace)** 01:25 I don't know.
**Otmar Ertl (Dynatrace)** 01:26 I have no idea if this meeting happens today.
Otherwise, I'm 2 weeks again.
Hey, Trish.
**Joshua MacDonald (Microsoft)** 06:01 Can you hear me?
**Otmar Ertl (Dynatrace)** 06:03 Yes.
**Yuanyuan Zhao** 06:03 Yes.
**Joshua MacDonald (Microsoft)** 06:04 Sorry about this, I… there are 3 Zoom meetings. I… I have… I'm very confused. I couldn't find you until you put the link in the Slack.
**Otmar Ertl (Dynatrace)** 06:15 It's no way.
**Joshua MacDonald (Microsoft)** 06:16 Sorry about that. So, Peter and I met in a different room, and I've been using the OpenTelemetry calendar because it's… I don't know, there is a Google Calendar that has these links, and it has changed, and But we can fix this.
I will make sure that by next time, this is… this is fixed. So Peter and I had a short conversation. I just pointed out that Yuanuan's PR has merged.
And I showed Yeah, and I shared a couple links to say that, I have very little news other than, some developments happening in memory profiling that I'm starting to pay attention to, and it brings up sampling algorithms, so I thought it was pretty nice. I put some links to The JE MALIC and the TCMALIC Sampling algorithms, which I've started to digest.
And I just shared briefly with Peter in that other meeting that I was, pleased to learn about this. As you know, I have a past at Google, so the TC Malloc library is very familiar to me. And what I learned, is that, The way they did it, is clever, because it lets you extract four different profiles. It lets you extract the, the byte-weighted profile and the allocation-weighted profile, by its cleverness. And so there's some interest in, adding such support to, Well, Microsoft's malloc library, for one.
Which is me malic. And… so I was looking at that, and I thought it was interesting, and I wanted to share.
Hello, Andreas.
I, feel like I recognize your name. I don't know if we met,
**Andreas Gruber (Dynatrace)** 08:09 Mmm… we never met, I am a colleague of Otmar since a very long time in Dynatrace, and… I'm also dealing with quite a lot of sampling topics here in Dynatrace, especially with our own agent technology, and always discussing how we can interoperate with OpenTelemetry.
As we have also OpenTelemetry customers in our customer base. And recently, I also, looked more into the tail-based samplers from the hotel world, and And then stumbled then across the group again, and then reconnected here with Otmar in that regard.
Also, I'm very interested in, especially when it comes to profiling on the extrapolation of data, be at Dynatrace, and also when you look at open telemetry transformers.
You, you derive metrics from traces, and the metrics always represent what you get.
Or you have to… Extrapolate here. And, especially when you have big customers with our agents, with OpenTelemetry, with agents from other vendors.
It becomes quite interesting to propagate sampling information.
have sampling or extrapolation information on the tail-based samplers, and was also then looking a bit in what… what is currently out there, and what's happening out there, and I think it… It's quite interesting to… to join… join in, and then listen in, and then… Let's see how that evolves, and also quite interesting, you also brought up today profiling. It's another topic I'm working on, the Anatrace.
Also, the whole profiling push from OTEL is quite interesting for us, and…
**Joshua MacDonald (Microsoft)** 10:08 Cool. Yeah, I'm, I'm also excited to see OpenTelemetry grow into profiles. So, Andreas, there's been some work in the collector, the Go Collector, in the last… 3 months, pretty intense, from… coming from the Honeycomb Company, which has added, their own, quite developed, sampling platform, including a bunch of choices for rate-limited, control over tail Sampling.
And it has a little bit more of a… well, there's two now. We have… we have sort of competing tail Sampling processors. They both are moving to support our specifications, and So that's good news.
Do you… I feel like one, it might be time to do an evaluation of where the OpenTelemetry project stands as far as its clients. We just gained one! We got the Go client doing our sampling logic. We have Java.
I can't remember the state of JavaScript, but I think it was partly done, and Python was partly done. That's 4, maybe. I'm still… pestering people about .NET and not making a lot of progress. I also… just don't have a lot of energy behind Rust in OpenTelemetry.
So that, that would be my, my corner, but I don't have, Much momentum.
Is there anything that we should be doing that you think, as a newcomer here, Andreas? As far as.
I… I don't feel like I have a grasp of it, because I come here every two weeks, and we talk about what's new, and very, very little is new, to be honest.
**Andreas Gruber (Dynatrace)** 12:09 Yeah, no, I'm… my thinking was a bit more, just start a bit to listen in and to, to those open telemetry… Groups, and then learn a bit how… Here, is, is, is worked, and then also try to, to, to get a bit familiar, and then see if, if then… Can… how can I contribute to your ideas? I mean, I looked also at some of those pull requests already. I had, of course, agents running, analyzing the whole code, and… verify my… my ideas already, so… of course, but… and then… and that… for me, that the most interesting thing is… how things are actually then implemented in the world with those trace state things to… to put sampling information on the trace state, because that's also something we as Dynatrace on our agent could leverage and then communicate back to the trace state, and then… downstream authors could then leverage of the information we already put.
And on the other hand, this whole tail-based sampling. I did not read yet into the honeycomb mechanisms.
it sounds quite, quite interesting, and I did not also have a look if there's already extrapolation information on the spans. We… and… but I think there is also, from Ertl users, quite some interesting, interest on tail-based sampling.
So I see that also in our customer base, so there's, quite some interest, and also.
on how to deal with metrics, and for a long time, our answer to, to, to hotel and, and, and, to, to customers was, yeah, from hotel side, there is very little… information about the sampling process on the spans that reach your backend. So… cannot basically do anything in terms of extrapolation when we derive metrics on our backend, so… I think from a data consistency perspective.
**Joshua MacDonald (Microsoft)** 14:21 Yeah.
**Andreas Gruber (Dynatrace)** 14:21 The work you're doing is very good.
**Otmar Ertl (Dynatrace)** 14:25 I think there's going to…
**Joshua MacDonald (Microsoft)** 14:27 Go ahead.
**Otmar Ertl (Dynatrace)** 14:28 I think it's general, common goals that we want to extrapolate, you know, data from the collective spans.
And yeah, Andreas is much closer to the product, he's architect with boundaries, so, and by Lyme in research, so I was more… I was ahead of time a little bit, yeah, that's my job.
And, you know, to see if, you know, the definition and specification, you know, are… Good for us, and…
**Yuanyuan Zhao** 15:02 A lot.
**Joshua MacDonald (Microsoft)** 15:03 There's only been… Go ahead, allow me to…
**Yuanyuan Zhao** 15:05 Ask, yeah, I do not have the context, so this is asking for context. Is the tail-based sampling, is it based on the same algorithm that we had, like, the former… Trace IDE ratio-based, now called probabilistic Sampler, or is it a different algorithm?
**Joshua MacDonald (Microsoft)** 15:26 the collector components, and I'm not so close to them that I could, like, recite and verify them without looking again, but they… they both… both the tail Sampling processor, which was the original.
And the new Honeycomb, dynamic… I think we called it Adaptive… anyway, we just renamed it.
Adaptive Tail Sampler. So there's Tail Sampler and Adaptive Tail Sampler, and… I prefer the Honeycomb. It's a little bit more put together, in an organized way. The other one is a little bit like chaos. But they both do have maintainers, and they both have support from a company, and they both, as far as I am aware, have added support for what we called OTEP 235, or the trace state entry for threshold and randomness. And if… I… and I was involved in the code review for the tail sampler processor, and I… I put on my, like, Otmar hat, and I tried to do sampling correctness.
I, basically, I have become a student of the Daniel Ting paper that you shared with us. You know, basically says that you can do this, and you will set your randomness, or your threshold.
accordingly, and you will end up with something correct. So, theoretically, I believe it's correct. I wouldn't… I like to verify things by running real data and seeing that the estimates come out right. So, you know, like, I think we're there.
And that the… And that… At least both authors are trying to be correct, and that's all I know.
Oh, really.
**Yuanyuan Zhao** 17:23 Let me dig a bit deeper. You said that the tail base, the tails, sampler supports, like, the random values and OT, the other OT, tags, keys.
What do you mean by support? Support meaning that they can understand the trade state RV and OT from the SDK, Or that they actually run a similar algorithm.
As the one that actually generated the…
**Joshua MacDonald (Microsoft)** 18:02 I… Believe… that both… okay, so I'm very shaky here. I have to go look more closely, but my understanding is that both have begun to accept the incoming… value from the SDK.
and preserve it well enough to propagate. And then… adjust it… When changing sampling.
So… like with our prototyping, like the equalizing sampler mode and the proportional sampling mode, what I saw in the adaptive sampling mode from Mike was like the equalizing mode.
So they're setting a threshold, and they're letting some of the spans pass, and updating the threshold. That's my understanding.
**Yuanyuan Zhao** 18:57 Yeah, the adaptive part is really, the threshold part that can… that can adaptively change, right? Otherwise, it is just, like, the static, right? I mean, so… It seems like… The adaptive one is more like, let me take a dumb case that, some, operator, manually set a, sampling rate.
And then they bring it down, set another sampling rate, but the adaptive one is just automatically does this at a much faster pace. Is that the right mental model?
**Joshua MacDonald (Microsoft)** 19:38 Yeah, that it is.
**Yuanyuan Zhao** 19:39 Okay.
**Joshua MacDonald (Microsoft)** 19:40 It's using… I… It has several algorithm choices, and I haven't scrutinized them all. It has an exponential weighted moving average, like, for example, and so it's… it's adjusting the threshold to aim for its target rate.
Okay.
And, I know that there are several variations on it, and that's the part I like, is that I know that they have tried and chewed this method for years, that they have been in production selling this code. So, the choices that they make look… or the options that they give you look… tested, essentially. And… and… and… I mean, we could pull it up and look at it right now if you'd like, but, see… If I can find it, hmm…
**Yuanyuan Zhao** 20:30 So it sounds like two kinds of algorithms are involved here.
One is the algorithm that adaptively decides what is the current sampling rate or threshold.
The other is the actual sampling algorithm, which is basically what we've been worked on.
That's the probabilistic sampler, right?
**Joshua MacDonald (Microsoft)** 20:54 That's… that's my understanding, yes.
**Yuanyuan Zhao** 20:56 Okay.
Damn cool with that.
**Joshua MacDonald (Microsoft)** 21:01 Probably worth us getting a little bit more clear, but, so here's an example.
It has a lot of the same… flavors. You have rules, And then you can name your samplers, always sample adaptive percentage, there's also, like.
Adaptive throughput, adaptive percentage, and probabilistic. So, like, those are your basic choices, And… anyway, at least this is trying to be correct, and From our perspective.
And… Again, I like this code better than the other.
Personally.
and this, this, like, this feels like very open telemetry, like, they've got all the support, and… and, you know, here's your OTTL conditions and stuff, so… It's really getting… it's really… it's real, that's what I know.
So that's new, and And as far as I… as far as I have reviewed it, is doing the OTEMP stuff that we… that we have written specs on.
And I'm sure there are corner cases.
That are written up here.
Their… their… their refinery is the commercial product that they are… Still maintaining… So it's like a scalable version of this.
Here are the categories. Important.
Goal throughput. Computes the fingerprints, okay, well… Maybe Mike will come one day, talk with us about it. He's come once or twice to this meeting.
**Yuanyuan Zhao** 23:07 So, about the status of the non-adaptive SDK sampling and spam metrics. Do we have You're sitting on this?
reported.
**Joshua MacDonald (Microsoft)** 23:19 do this?
**Yuanyuan Zhao** 23:21 So, we had the in SDK.
Sampler, right? In several languages.
And we had the spam metrics connector.
That does the extrapolation. Do we have usage about this?
**Joshua MacDonald (Microsoft)** 23:38 I don't know. But what we believe is that you could take that sampler and then send it to a spanimetrics count, and then you'd get counts from your tail sampler, and in theory, you could… you could… you should be able… if you set the tail sampler correctly and, you know, your tail samples extrapolated should re… equal population counts, I think.
Plausible, at least.
I was just pulling that back up. So, yeah.
I was gonna ask Andreas, what's your language of choice?
**Andreas Gruber (Dynatrace)** 24:32 Trava.
**Joshua MacDonald (Microsoft)** 24:33 Java. Okay, so you guys… so you can then, understand that we have… so yeah, unfortunately, it's not one of the languages we're missing for.
**Andreas Gruber (Dynatrace)** 24:41 Yeah.
**Joshua MacDonald (Microsoft)** 24:42 Not surprised. Okay, yeah, I, I've, I guess I… Yeah, I would look for all of you to offer input on, you know.
you know, suppose that we had the rest of the languages. Are we done? Like, what… what's left? I don't… I don't… I don't sense the great deal of adoption, and that's making me feel like we're not done, but I don't have a strong feeling.
**Yuanyuan Zhao** 25:15 Are people aware?
**Joshua MacDonald (Microsoft)** 25:18 Well, there was a blog post about a year ago, I don't know what… I don't care.
See, I… I guess I've always believed that, The, the, the end of the road would be we have some… type of dynamic.
Control that gives us the ability to make a feedback loop between the collector and the SDK. So, I'm shamelessly saying, like, let's do what Datadog H can do, for trace collection, and that means that And basically, users don't have to think about it. You turn on your collector, you turn on your SDK, and the collector sampler starts telling your SDK to turn it down so that we're not wasting so much CPU and memory. That's, in my opinion, where we want to be, and I guess I realize we're not there yet. Mainly for wanting a… I guess, fully implemented end-to-end feedback loop, and it sort of suggests using OpAmp.
to control the SDKs, but it's, it feels a little bit… imaginary, the way I explained it, even though it's, again, just doing what the Datadog agent, or Refinery, well, Datadog Agent can do.
Because that's… that's powerful.
**Yuanyuan Zhao** 26:54 Thank you.
**Joshua MacDonald (Microsoft)** 26:56 So, so yeah, maybe that's my answer, is what's next? I don't think people are aware of it, but I don't think they're quite excited enough yet, either. I would like it for the… like, for example, it would be cool to take the output or the internal state of the adaptive tail sampler we just looked at, and have it, also advertise an op-amp control plane, and then have SDKs connect to the op-amp, and have it… have it control them somehow. I guess that would be cool.
Jimmy might get a dog, basically.
How's that sound?
I'm gonna promise to fix the Zoom room confusion. Is this… I can't even tell what's correct. I'm gonna go to the calendar. See, this is where… Anyway, never mind. I'll fix this later.
**Otmar Ertl (Dynatrace)** 27:53 Yeah, the link and the link name are different, so…
**Joshua MacDonald (Microsoft)** 27:58 Fantastic.
**Otmar Ertl (Dynatrace)** 27:59 That's…
**Joshua MacDonald (Microsoft)** 28:00 That's… that's part of it. You know what I'm gonna do? I'm gonna delete it.
And I'm gonna go to the calendar.
This is how I've been finding meetings lately, is because all the meetings changed, and everything on my Outlook is wrong, and I just know that.
**Otmar Ertl (Dynatrace)** 28:17 Is the calendar the ground rules? I don't know, so…
**Joshua MacDonald (Microsoft)** 28:24 Oh, shoot, that's not what I want.
It's hard to copy a link.
Okay.
No.
Come on, Google.
Okay, well, I don't know that we have much more meaning here.
But I appreciate everyone coming.
And… Really?
There, all the links are now correct, I think.
Any more agenda, you guys?
**Otmar Ertl (Dynatrace)** 29:14 So…
**Joshua MacDonald (Microsoft)** 29:16 Let's make an action item next time. What do we want to see for sampling sake?
Huh.
Feedback.
okay… Andreas, are you familiar with any of these things we're talking about? I'm, the Datadog Agent client… Datadog Agent Mechanism for Sampling traces, or the Jaeger remote mechanism for Sampling traces?
**Andreas Gruber (Dynatrace)** 30:06 I have the impression we at Dynatrice have something similar. I never researched that deep into the Datadog agent.
How, how they control the sampling.
In the end, we have also… I'm familiar with this… we have also our head-based algorithm, we can steer it adaptively.
Where we… Yeah, so, so this, this is, this, this kind of a feedback loop to, to, to, to steer.
We have this… I'm not fully aware how others are doing it, and… I would not now initially see how… how… the use case behind steering a head-based sampler based from the collector, from the… from the tail-based sampler. I think those are a bit of… sometimes distinguished use… separate use cases. So customers that went for tail-based sample.
want to overcome head-based sampled problems, like the error capturing. So this very classic sample. And when you go for tail-based, you have to invest on those kind of memory.
That you can actually do this distill-based sampling, so… I think head-based is a very good, a very cheap, mechanism to really bring the volume down, and… The… and then… Yeah, I really would need also to look a bit what Datadog is doing, and how they are steering it.
**Joshua MacDonald (Microsoft)** 31:56 My, my understanding or recollection is that it's, you know, like, it's put in the synchronous call code path, so, like, you make an export request, you get to… you talk to the agent, and it replies, like, in line with some… some sampling adjustments.
But you're right, that… that… that sometimes people choose tail sampling to overcome problems with head sampling, and you wouldn't always want one or the other. What I see, Inside the company here is a sort of, like.
sort of yes and both are good solution, where you say, I want to do some head sampling just to, like, cut down the volume by a tremendous amount, like 10%.
And then within my 10%, I'm going to go do tail sampling, because I really don't want to collect 10% of samples, either, of chases either, that's way too much. But that way you get some exposure, and anyway, that's the balance I've seen.
**Andreas Gruber (Dynatrace)** 32:52 Yeah, that they understand, and they also see it, with, with those Then, again, with metrics you directly get from the SDKs that have, anyway, the highest precision you can get, and… So…
**Yuanyuan Zhao** 33:05 computed inside the SDK before…
**Andreas Gruber (Dynatrace)** 33:09 Yeah, before Sampling the Like the classic HTTP server request.
**Yuanyuan Zhao** 33:15 Those are two.
**Andreas Gruber (Dynatrace)** 33:17 Those, those are… those are those kind of unsampled, golden signals, so to say. And, yep.
**Yuanyuan Zhao** 33:30 The extrapolation is more interesting for, like, the latency histograms.
that are harder, or more expensive to do inside the SDK. I mean, if simply just the count.
That's cheap.
**Andreas Gruber (Dynatrace)** 33:48 Yeah.
**Yuanyuan Zhao** 33:48 In the SDK, yeah.
**Joshua MacDonald (Microsoft)** 33:57 Well, I look forward to… your input in the future, Andreas, especially if you, would care to join us again. I think there… the more people we have that are actively pushing forward, the more… the more we get, I think.
And I keep saying that I'm interested in things because I want to see them happen for OpenTelemetry. So, at some level, I want to pitch in, and the more energy we have, the more likely it'll get done. I've always wanted this feedback loop, I really have.
**Andreas Gruber (Dynatrace)** 34:34 No, I can't really imagine things where, right.
could make sense. So, also in terms of, especially when you… do the head-based, the tail-based sampling, you always have constraints and, like, memory, and then when you, run out of memory on the collector, you can then throttle on the source with the head-based samplers to actually have still, can maintain your sampling decisions on the collector. So, That's… that's then anyway something where… where a feedback loop always makes sense to my mind, because it's… it's… Yeah, tail-based has its advantages, but you always buy it with memory, and… Yeah, and I…
**Joshua MacDonald (Microsoft)** 35:24 I've seen situations where, again and again, where you have a budget for memory in your collector, let's say, and if too much data arrives, you… you have to break somehow, and I think the way… That we have discussed breaking the way I like the most is to just resample, meaning to adjust the threshold, which means to prefer to keep complete traces and just throw away data that you've collected.
But that means that you are letting data be collected and thrown away. And that's a signal that you maybe should be doing more head sampling.
**Andreas Gruber (Dynatrace)** 36:02 Yep.
**Joshua MacDonald (Microsoft)** 36:03 And so, yeah, there's a… there's a clear signal there.
And that's the sort of, I think, feedback that people would like, is, my tracing costs too much.
I only have this much collector, make sure those SDKs are, you know, somewhere in line with the plan.
**Yuanyuan Zhao** 36:25 With… without looking into honeycombs or adaptive tail Sampler, what does it… What prevents it? The algorithm.
From being used to, adjust.
the in SDK, provided we provide the plumbing, right?
What prevents the algorithm from being used?
**Joshua MacDonald (Microsoft)** 36:53 I don't know exactly what the feedback rule is, I guess. Like, how do you… once you run out of memory on the collector, what do you tell the… How do you decide what to tell the SDKs?
I mean, I guess to say it's not obvious.
**Yuanyuan Zhao** 37:13 Well, what I mean is that So, inside the SDK, it can accept a sampling rate or threshold. So, suppose we have a mechanism that plums The decision inside a collector.
back into the SDK, right? Then the current adaptive Sampling tail sampler implemented by honeycomb, we… what prevents… like, we use the algorithm. I mean, if they're counting memory, etc, they actually don't have to store the things in memory, they just have to collect the stats.
And then make a decision. Of course, there's a bit of a lag, right? But if the production condition persists for a while, it's not like completely erratic, then what you observed, like, a second ago, right, 5 seconds ago, can be applied for the next 5 seconds. So suppose the algorithm of Honeycomb tail Sampler does that, and we have the mechanism.
Is that enough to plumb the things?
**Joshua MacDonald (Microsoft)** 38:28 I…
**Yuanyuan Zhao** 38:28 to have adaptive in SDK Sampling.
**Joshua MacDonald (Microsoft)** 38:33 I think at the high level, yes. Maybe at the, like, detail level, there's some questions still. But at the high level, you're saying, I have a spin that just arrived.
my threshold is up here, its threshold is down here, I have to drop it. You might just tell the SDK to, like, bring its threshold up to match where the collector is. That seems like the rule that would work.
Of course, feedback loops are… are, you know, troublesome. They… they have… Oscillations and noises and things like that to worry about, but…
**Yuanyuan Zhao** 39:06 But it is also a constraint we have to live with, right? If things are completely erratic, there's no way we can do a good job, and we have to make the assumption.
That what you are observed just a short while ago.
is going to apply for that, right? Otherwise, there's no way we can implement adaptive.
**Joshua MacDonald (Microsoft)** 39:28 Yeah, you know, last week I mentioned this.
Little hobby of mine.
Speaking of which, this… this cell… this is a sampler that we are still working on internally, I think you all have heard me talk about my bottom K. This is… this is not my PR, I did a review for it, but basically this is a weighted reservoir algorithm for logs, and… the same idea is being applied. I'm going to say whatever my frequencies were last period, I'm going to assume that that stays the same, and I'm going to adjust my sampling probabilities to match. If the data is the same distribution as last time, then I will get the sample I want. That's basically what we're doing here.
And, I believe that that is a good strategy. I mean, like, within some short time horizon, you should be able to assume that you're getting roughly the same thing. Otherwise, I don't know what else to do.
**Yuanyuan Zhao** 40:25 Yeah, the thing becomes impossible.
**Joshua MacDonald (Microsoft)** 40:30 That was my little hobby.
And that's because logs, it doesn't… doesn't follow any of our consistent sampling rules.
And that is the… that is something that I would love to come back and talk about more. We are… we are still pursuing something along those lines.
Well, we aspire to have a feedback loop in our collection path. I agree.
And I think we have reached the end of a meeting.
**Yuanyuan Zhao** 41:19 I'll see you guys next time!
**Joshua MacDonald (Microsoft)** 41:23 I encourage all of us to, find what it is we want for the future. If it's a feedback loop, we can get more specific.
I'm very excited about it.
I think the plumbing that you're describing, Yuanuan, is not going to be easy. I know some of the SDKs, including Java, have op-amp, so maybe Java is the perfect place to try this out. Like, have your Java SDK connect to your collector.
Twice. Once for export, once for op-amp, and have the sampler control op-amp.
I don't know, I'm sure an agent could write that for us.
**Yuanyuan Zhao** 42:05 Agent, you mean the AI agent?
**Joshua MacDonald (Microsoft)** 42:08 That's the AI agent.
**Yuanyuan Zhao** 42:08 So many agencies.
**Joshua MacDonald (Microsoft)** 42:10 No one will be able to review it, but it's fine.
**Yuanyuan Zhao** 42:14 Yeah, I'm curious what you guys think of the… AI coding.
**Joshua MacDonald (Microsoft)** 42:22 It is, overwhelming me. It's hard to review all the code.
**Yuanyuan Zhao** 42:29 Yeah, definitely.
**Andreas Gruber (Dynatrace)** 42:31 Same here. But it helps to dive into areas you would not go into.
**Joshua MacDonald (Microsoft)** 42:37 Yeah, I can do more math than I ever could.
**Andreas Gruber (Dynatrace)** 42:40 It's, so, and on the alternative…
**Yuanyuan Zhao** 42:43 What degree do you hand off work to it?
**Joshua MacDonald (Microsoft)** 42:49 Varying, depends on where it is. Yeah, so for the main project work I do in Otil Arrow, I feel like I have to review code 5 times for every, like.
Once the agent writes it, so, like.
It can write code, but I still end up doing a lot of… a ton of work just to review it, and that's maybe the normal case now.
Getting a little bit more done, but it's still a tremendous amount of review.
**Yuanyuan Zhao** 43:18 I found from my experience is that I… I'll have to first decide the architecture.
I mean, the best way it works is, actually, I controlled it.
on a quite fine degree, and also, then that way I have confidence on the code as well.
And it also does things in other Bethany, violates the invariant I laid out.
And it also doing things that just mimic what I put in in the production code. Doing the same in the… Test the code, and resulting actually, a flaky test. I'll give you an example. They are, like, I'm using random number generator that I, paralleled several, so I use the XORs with, like, an incremental counter to generate a different seed. But then the test, it actually does exactly the same, completely negate the XOR, because when you are XO-ing the same number, Twice.
So it ended up with a bunch of random numbers generated with the same seed, and then the statistical skew, because it's random, it's pseudo-random, right? The statistic SKU actually completes the WACT.
And it actually doesn't… doesn't agree… so at first, I'd like to find it out. It couldn't.
generate a bunch of, like, this reason, that reason, and never passed the things. I finally gave up and looked into myself, and I found the issue, I fixed it, and I asked them whether that's the cause, because I want to test it. It says, no, it's… that it says very confidently that, that definitely should be fixed, but I don't think it's the reason, it's the cause.
**Joshua MacDonald (Microsoft)** 45:13 It's quite a learning curve.
**Yuanyuan Zhao** 45:15 By the running curve.
Yeah.
**Joshua MacDonald (Microsoft)** 45:18 All right, well, I think we're at the end now. See you in two weeks. Come back with your ideas. Thank you all.
**Otmar Ertl (Dynatrace)** 45:25 But…
