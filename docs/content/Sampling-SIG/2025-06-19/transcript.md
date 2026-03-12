SIG: Sampling SIG
Date: 2025-06-19
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/2vn3h8kVFR3L-Vw0UqDQ4_rR8qrIfIv41Z8gAtgYN7HHUGTAS5Ejf2_DA6AFDNHC.fW3J77_pZ8cXvKuU
============================================================

## Zoom Recording Transcript

**jmacdonald** 01:33 Yeah. Can I hear myself?
Hi, Peter! Hi, John! Here we are.
Good to see you.
I think you had a vacation last time. So welcome back
**Peter Findeisen** 01:47 Thank you.
**jmacdonald** 01:49 Oh, good! We have Carlos. I had a fun idea for today. But I also I think it's worth discussing, like the future of the Sig. Because.
and Carlos might have an input here. There's a feeling that hotel has more cigs in it than it can actually sort of provide energy for. And I have a sense that that this meeting is taking up valuable space. And so I wanted to talk about how we can keep seeing each other.
While pausing the Sig effectively. And I have.
And I had a fun idea for what to do today. In it here. So And let me know if you're here, Carlos, and I'm glad to hear if you have anything to add to that.
**Carlos Alberto Cortez** 02:45 I am here. I don't know how's my audio I am here.
**jmacdonald** 02:48 Hear you.
**Carlos Alberto Cortez** 02:48 Space.
**Peter Findeisen** 02:48 I can't hear you.
**Carlos Alberto Cortez** 02:51 Sweet.
**jmacdonald** 02:52 Yeah. I was just saying how I as much as I enjoy this meeting. It's but it's become. There's not much on the agenda and it's not that we don't have ideas or wish lists, but it's more about like who's paying us and staffing us and so on you know we and and I had one item on the agenda which is just this administrative thing that apparently Austin's doing, and I I haven't checked it out yet, but I was asked to look at it for the Sig. What I was hoping to say today here is, you know. I think the the otap that we have pending should merge. It has. I've seen, approvals enough to merge, and I was there's still a few comments left last week.
As we discussed last time in the sig. You can see the notes from it.
When I say what's next, you know, the 1st thing comes to mind is Jaeger remote sampling? And I think for you, Peter, you've mentioned how you know the the follow on that you once wrote up, but haven't completed is configurable sampling.
So in some ways the the work of this group.
If if it were to pause, I would say it moves really to towards the the configuration working group. In a sense, however.
there's something that I'm interested in still, and it does come down to that that Jaeger remote sampling.
So here's my fun idea.
My! My position is that these AI coding assistants are getting pretty powerful, and I would be glad to entertain myself by starting a side conversation in my daily life with an AI coding assistant to do some work on sampling. What I'm trying to say is, I think if we wrote clear document of what we wanted here and now, like I would I would start it in this document right now, what are the requirements for a minimum viable hotel sampling solution that includes something in the collector.
plus what we've built for the current Oteps, you know. Current. Just assume what we we get, what we want from the sdks at this point. It's a. It's a few steps more when we talk about configuration. But to for me to motivate the like work, the the work order here is like what the reason that we want configurable sampling is because we're going to tell hotel users that they can deploy hotel sdks and turn on this feature in a collector, maybe, and then magic happens, which is the magic being. Their traces are dropped down to a a reasonable rate, and they are happy. That's sort of the the idea.
does that sound? And so other. The only thing I have to bring to this meeting here today is the idea that if we're if we're out of ideas, what we could do is write down plan, or a community owned sampler component for the collector and sort of start listing requirements. And then you know, at the end of my workday I can tell the AI assistant. Okay, you got 12 h here. Go for it, and I'm I'm I'm sort of learning here. It's it's a it sounds fun. It sounds funny. But there's a sense in which this could be possible. We just have to tell it what we want, and that's the hard part.
So that's my only idea. Right now. Peter, what do you think.
**Peter Findeisen** 06:37 So I have to admit that I'm very cautious as far as AI coding goes. My, I know that you have. You had some positive experience with that my experience. I had only one. Basically, it was pretty negative. So.
**jmacdonald** 06:58 Yeah.
**Peter Findeisen** 06:58 The the code looks good, but it was using non-existing libraries which.
**jmacdonald** 07:02 Yeah, yeah, no. That happens. You gotta learn. You gotta work with it.
**Peter Findeisen** 07:06 Yeah.
**jmacdonald** 07:08 So so yeah, that my my optimism can can work through that part. And I and I also kind of feel like, Being a realist that this is the direction our industry is going, and I want to learn how to use these tools anyway. So so that was my idea. Because I don't. What I'm trying to say is.
I don't expect to be assigned myself to personally write this code. I don't expect you to.
but if but but I'm confident that I can assign an AI assistant to do much of it. So what if literally here and now we open. We started writing in this document. What are the requirements? What would you hope for.
**Peter Findeisen** 07:57 For the collector, you mean for the collector. Okay?
Well, so I I believe there are 2 major samplers which need to be implemented one is with the fixed probability. There is already a sampler with or a fixed probability, but it needs to be consistent with our approach, with with consistent probability sampling. So it needs to handle the th value correctly.
**jmacdonald** 08:35 You're saying fixed probability, and I'm So so a fixed probability sampler, we have one called probabilistic Sampling Processor. It's been around for a long time, and it.
**Peter Findeisen** 08:45 Yes.
**jmacdonald** 08:46 Has been upgraded with the Otep 2, 35 stuff by me quite a while ago.
but it seems it's still like not a totally useful tool. And I I think that's what we're here to talk about. Partly so.
So the reason I'm saying that is that it has no configurability beyond simply fix the problem.
Yeah, it is. Yes, has no rule. Base.
**Peter Findeisen** 09:14 Right? Right? Well rule-based is already implemented in the collector. Right? So you have your your configuration, which you can specify different conditions and apply different sampling policies.
This is equivalent to to conditional sampling that we have in in head samplers.
What.
**jmacdonald** 09:39 How.
**Peter Findeisen** 09:39 Definitely missing from the collector is the rate limiting sampling which would be consistent with the th values. And we would say, Let's say we have. We want to have that many traces, or that many spans depending on what's doable per the time unit, and it would adjust the sampling probability. Accordingly.
using the same kind of algorithm that we have in in head samplers.
**jmacdonald** 10:11 And is it but the the question I wanted to. So so I wanna record the previous thing you said, which is effectively the idea that we know collectors can be configured. And the I think the idea you're you're aiming at is that this sampler tool that we have literally knows how to do one thing which is, do that sampling logic. And I've actually showed this as a prototype once before. If you combine the features of the filter processor and the transform processor.
You can apply your rules in the other components. Your rules are, I want to choose, based on attribute and and the way it's implemented that I showed once was to take the rule, modify a sampling priority field, which was to say, Here's what I want my probability to be and then it would pass into a sampler which says, I see what the probability is meant to be. I'll just do the thing it said to do that was a somewhat a somewhat awkward construction. Hello, in which the the filter and the transform processors were doing the rule base. And then it's the process. The probabilistic sampler just does something simple.
Is that is that the vision that you were sort of looking at too.
**Peter Findeisen** 11:33 May maybe not the final shape. But I I think it's workable 1st step, or it. It would be useful. I believe.
**jmacdonald** 11:47 And do you agree with that sampling priority mechanism which is to say, the rules will just set the effective probability, and then the sampler will do it.
**Peter Findeisen** 11:59 Well, I would have to have a closer look. I I still believe we have this.
We we miss this rate, limiting, sampling.
**jmacdonald** 12:12 Yeah, I was gonna come to that. So and the thing I want was gonna come to. Then we need, we know we need rate sampling like you said it should be basically modeled on the work we've done for the for the SDK, is it based on?
So this is where I was hoping to to answer some questions in your from the group.
Would you say that it?
that it is based on root spans? Or is it based on any span, or is it based on tail sampling? I think those are the the sort of 3 directions I've seen? Maybe this this job.
**Peter Findeisen** 12:55 Believe it would be tail sampling, because well, we the goal. There were 2 major goals with consistent probability sampling. One was to have these a spantometric pipeline. And second, was, we wanted to keep as many complete traces as possible.
That's why I think that tail sampling is the right place, because here you have complete traces, and you drop complete traces or pass complete traces
**jmacdonald** 13:32 Okay.
I was hoping you'd say that. Maybe. Okay, so definitely, so this puts the tail sampling processor in my sites. Now.
I have. Let's suppose that.
So I'm gonna say, I'm gonna say.
so I I was like, Step one, maybe upgrade the tail sampling processor as it exists today, so that it knows about 2, 35 can.
This may require modification.
I'm saying, I'm saying that because, as we've seen with all, all legacy samples, you might have a rate limited thing that's not probabilistic or not.
**Peter Findeisen** 14:26 Right.
**jmacdonald** 14:27 Cent.
Yeah, So then let's suppose that in one little step forward we we just whacked the tail sampling processor and made it start using our our Otep. Now, there's still something left. That's kind of what I wanted to get to what's left, that the idea is that this tail sampling processor will using its local stream.
derive statistics about the stream of all traces and spans.
**Peter Findeisen** 15:16 Yes.
**jmacdonald** 15:20 I say traces and spans because I'm leaving the question open.
obviously, we make root head sampling decisions, and that affects trace completeness.
I want this to be like version 0, whatever the dumbest, simplest possible thing is. So we're we're probably not looking at intermediate nodes in a trace like it can be a version. 2 problem when we have a problem where like traces are too large because one noisy child has too many children, and so on. That's a solution that we could look at later.
so we're just looking at just looking at root spans and then over a let's say a window of time, let's say, over 30 seconds. We calculate.
okay, what do we calculate? And what do we use for feedback. What I'm what I'm getting to is that we're gonna co-opt or adapt the Jaeger remote sampler.
May essentially providing a a path to connect to that same collector, ask it for configuration and have it spit back. Configuration.
So that the tail sampler this sort of combined sampler we're talking about component will both be a sampler and a configuration server for sampling. That's is that. Does that match your idea?
**Peter Findeisen** 16:56 Well, well, that's definitely one way of of evolving this. But I wouldn't be talking really about this in our step one, right? So it's definitely something.
Oh, God!
**jmacdonald** 17:11 you're you're you're not looking for the adaptive step yet.
**Peter Findeisen** 17:14 No, no? Well, all right, correct. And and I I understand that there are some examples of this feedback loop from the collector to the sampler, and like Jaeger sampler also. I believe honeycomp has something like that.
But the standard or open telemetry is probably becoming opamp, right? So we we should, we should not invent, reinvent the wheel. Here we should wait until OP. Is implemented for for sdks.
and we should use opump at this point to configure the samplers if we want to.
So I wouldn't, because it it feels like duplication of of work. I know that our pump is evolving relatively.
**jmacdonald** 18:09 I, I.
**Peter Findeisen** 18:09 My own name.
**jmacdonald** 18:13 I agree.
**Peter Findeisen** 18:14 Is an accepted standard.
**jmacdonald** 18:18 That was my version. 2 idea. Maybe we skipped version one version. One idea is what I was hearing you say is, there's no feedback loop in version one. There's just a tail sampling configuration that that works and can be configured for rate limited sampling of traces.
**Peter Findeisen** 18:37 Yes.
**jmacdonald** 18:38 That's that's it. Okay.
**Peter Findeisen** 18:39 Yes, that, and this would give the our customers a lot to work with.
They would have to manually configure the rate. But then, again in my experience, which is not my.
I think that customers do not change this these rates too often, so they know more or less what they want to pay for the back end to, for the processing of the traces.
They know more or less what kind of volume is satisfactory for them to derive quality metrics.
and they set it once and keep it forever. They don't want to change that. So if it's let's say 1,000 traces per minute it remains 1,000 traces per minute, and it does not require a lot of changes.
**jmacdonald** 19:33 Right cause. The okay. So then, the idea is that all of our fancy SDK, configuration story lets you lower the cost on the SDK, and wouldn't really change the output.
The scene at the back end.
It's just.
**Peter Findeisen** 19:47 It's a matter of moving a ticket.
**jmacdonald** 19:49 Sampling, forward.
**Peter Findeisen** 19:50 Yeah. So so the sampling rate is like like a controlling knob. If you if you want less costly solution, you decrease the rate. But if you are hitting some qua issues with the quality of your metrics, you cannot go any lower. You need to back off and increase the volume, but there is for many customers. There will be a sweet spot where they will be happy with the metrics, and also the cost will be lower.
**jmacdonald** 20:25 Got it.
**Peter Findeisen** 20:25 Yeah, right of rate limiting, sampling.
**jmacdonald** 20:29 Well, let let me let me lead you to the conclusion at this point. All we need is to take the sample tail sampling processor and make it compatible with Otep. 2, 35. Is that right? 2, 2, 35, ish.
**Peter Findeisen** 20:40 Yes, but we need, we need to modify the rate sampling algorithm which is there. You already mentioned this in one of the bullets.
**jmacdonald** 20:55 I'm I'm trying to to convince myself that all I need to do is go into that code, the the existing tail sampling processor, and like make it make it compatible with the new thing one way or another.
**Peter Findeisen** 21:09 Well, so the the missing step is which already put there is is measuring the incoming rate of traces which basically right now, it's not really measured.
That's the part which is missing. And this is different than for for the head sampler. There is a natural timing between spans because we are sampling exactly the same moment that the span is created.
So it doesn't. The algorithm does not require anything.
any memory, any any storage. It. It just measures the time between between 2 consecutive spans.
This is not doable for tail sampling, because you are receiving your traces and spans in batches.
so you have to apply something more refined. This is the challenge.
**jmacdonald** 22:06 Okay.
Let me ask, then, without asking you to spill any secrets, do you have any sort of rough ideas about this?
The dispatch, this algorithm.
**Peter Findeisen** 22:20 Well, we have. We have implemented something like that in our proprietary. Sampler for the collector in Cisco. I.
This this product, unfortunately, was obsolete. Once we merged with splunk.
I don't know if if it was based on the old
**jmacdonald** 22:47 This game.
**Peter Findeisen** 22:48 For sampling, using the powers of 2 sampling probabilities. But we had something in this area. Yes.
**jmacdonald** 22:58 I remember Otmar has at least once posted an algorithm about in the in the power of 2 way doing this.
**Peter Findeisen** 23:09 Okay.
**jmacdonald** 23:10 Let's see, is it.
**Peter Findeisen** 23:11 Yes, but it was. It was looking at spans, and it was processor for the for the Sd. Some span processor for SDK right. This was not tail sampling.
**jmacdonald** 23:28 Yes, it was right correct. It was just exporting spans and and intermediate sampling them to to maintain a reservoir. I think.
**Peter Findeisen** 23:39 Yes. Yes. Right?
**jmacdonald** 23:44 Is the is there any like high level description you would give here? Or have you already done that?
**Peter Findeisen** 23:58 I can. I can try to work on this. Yes.
**jmacdonald** 24:04 I'm not asking again. I'm not asking you to spill, like, you know, again secrets and I and I wouldn't ask you to give away. Something that you feel is like.
**Peter Findeisen** 24:11 I mean the requirements the requirements are not. I don't think they are secret.
**jmacdonald** 24:17 Yeah.
**Peter Findeisen** 24:17 So, yeah.
**jmacdonald** 24:19 As a as a matter of like pseudo code.
The!
How would you? Could you? Could you describe it as something like each rule.
for each rule you're gonna calculate, like, how many matches there were over a period.
**Peter Findeisen** 24:41 So the way the the way we did it. I don't think this is. I think it was. It was reported to our customers. So I don't think it's a secret anymore. We implemented a 2 step sampling in in in the collector.
The 1st step was rule based. It was we were applying different policies, depending on on some conditions. This is not new. This is, this is an already existing functionality. In the collector. However, our samplers that were applied were handling the the P. And R. Values correctly, because this was still based on the old schema.
Then there was the next step which was rate limiting.
So the customer had control in 2 steps. 1, st 1 1st was to to categorize the traces depending on on the some conditions.
typical cases where, with well, customers wanted to have.
as they say, all all traces with errors. Right? This is a very typical statement from from our customer.
They also want to have a lot of traces with high latency where? Where the the transactions were slow.
So that was that was done in the 1st step, the categorization, and assigning probabilities.
And then there was the next step which was taking managing the streams of traces from the 1st step and applying some rate rate sampling. So the rate was on average statistically meaning well, not not exceeded.
I don't.
No, if this is strictly I wouldn't impose this structure on the collector. I don't think it's mandatory, but this is how we were doing it, and definitely the new part which is not existing in the collector today is a step 2, which is sampling according to required rate of traces.
**jmacdonald** 27:15 So the first, st the 1st step was to let the customer sort of shape the the data, but basically on rules without thinking about rates.
and the second was like, basically bring all those, all the rules outputs back in line with the intended rates.
**Peter Findeisen** 27:33 Yes, so it was. It was a proportional sampling step. It it did not.
It's try to preserve the priorities that were given in the 1st step.
**jmacdonald** 27:48 What do you mean? Priorities.
**Peter Findeisen** 27:50 Well priorities, I mean. So if if a customer say said I want to sample all traces with errors, that was probability, one which which is the highest priority, that so I'm using the priority very informally here.
**jmacdonald** 28:10 Thank you. Thank you. That's why that's what I wondered.
interesting! I at this point.
well, I got what I what I wanted for out of this and I feel like I don't. I feel like we don't have any much more on that at the moment.
This is great. What I learned is that 1st thing we really need is to kind of basically repair the make. The tail sampling processor do do, Otep. 2, 35.
Change its rule engine to to use consistent probability. Sampling.
Step.
The second step is is You've it sounds like you've decomposed it in such a way that step one is just rules and step 2 is just probability or rate limiting, and so there's no feedback in that loop. It keeps it pretty simple.
**Peter Findeisen** 29:16 Yes, there's no feedback. These are relatively independent steps.
**jmacdonald** 29:21 Cool, awesome.
**Peter Findeisen** 29:21 So the step 2 measures, the incoming crate from from the 1st step.
**jmacdonald** 29:32 And I suppose it uses adjusted count rates.
**Peter Findeisen** 29:36 So it of course it keeps adjusted so no.
**jmacdonald** 29:41 No, it doesn't.
**Peter Findeisen** 29:42 It it modifies, adjusted count accordingly. But it's not looking at at the original volume of transactions. In looking at a volume of traces.
**jmacdonald** 29:55 And is it? I see.
**Peter Findeisen** 29:57 Ignores adjusted Count for the purpose of the volume.
**jmacdonald** 30:04 And then do you apply a second adjusted count to each trace.
**Peter Findeisen** 30:09 Yes, adjusted count needs to be modified accordingly.
**jmacdonald** 30:12 On every span? Or is there forever level.
**Peter Findeisen** 30:15 For every spend. Unfortunately, because these are kept for individual spends.
**jmacdonald** 30:20 Okay, I understood all that didn't take notes on that. Okay, well, this is what I wanted to do, and I think we've done it.
I know that the that the very, the. It seems to me like the most important thing to move this forward would be to take control of the tail sampling processor. We sort of knew that.
But now we know it even better.
well, Carlos, you're still listening. Here's what I want to say. I I would like to say we've reached a good end of a meeting. Maybe this meeting could be 30 min from now on, but I also don't want to lose this meeting, because I enjoy speaking with Peter and Otmar every other week, and so on, and I have enough of an itch here that I am kind of curious what I can do with tail sampling processor in 2 weeks and an AI assistant.
so I might just try that and as far as hotel governance, you know, we can say this Sig is paused or not.
I think the goal is to not detract energy from other parts of the community which I don't think we're doing, because this is such a scenario, a narrow interest area. I'll let Carlos, take that point away here and suggest that well, we can keep going. I want to see you again in 2 weeks, Peter, even if there's no Sig, I will be here, and we and I will let you know what I discovered in 2 weeks of fiddling around with the tail sampling processor.
**Peter Findeisen** 31:58 Okay, that's.
**jmacdonald** 31:58 Sound. Yeah, cool.
all right. Well, I'll see you in 2 weeks. Thank you, Carlos. I think we should place a blog post. By the way, Peter, you and you and I could co-author it. We could all co-author it. Everybody in the room here the entire sampling state could co-author just to point out that hotel still doing stuff, and we've got a new spec on sampling that is ready to go and we're excited about. I will also.
I will not forget what I just said. I will come back to this group saying, Blog post at least once.
soon. How's that?
Update the notes with that particular key item.
**Carlos Alberto Cortez** 32:33 That sounds good. I think that there's also great value keeping the group alive. Because in my mind I think it would be great. To also get the consistent and the possible samplers is to a level of stability. No.
that is like not development.
**jmacdonald** 32:56 Great. Well, I actually am gonna fiddle around with the tail sampling processor this just because I say I will.
Thank you all. Let's keep going here. And we'll be on slack, Carlos. We can chat.
**Peter Findeisen** 33:10 Correct.
**jmacdonald** 33:11 Thanks all.
Thank you. Bye, bye.
**Carlos Alberto Cortez** 33:13 Nope.
