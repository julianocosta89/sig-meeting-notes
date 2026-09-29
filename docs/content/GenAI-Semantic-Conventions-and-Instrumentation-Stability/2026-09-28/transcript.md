SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-09-28
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Surya Teja** 00:15 Hey, hi Trask.
**Trask Stalnaker (Microsoft Corporation)** 00:16 Hey, Surya.
**Surya Teja** 00:18 Also, we can…
**Trask Stalnaker (Microsoft Corporation)** 00:20 Pretty nice here, actually. How about you?
**Surya Teja** 00:24 It was great.
Don't settle, right?
**Trask Stalnaker (Microsoft Corporation)** 00:28 I'm in Portland. So, not far from Seattle, about, like, 180 miles south of Seattle. Slightly better weather, because it's inland in the Willamette Valley.
**Surya Teja** 00:42 Yeah, that's a great place, actually.
**Aaron Abbott (Google LLC)** 01:46 Hello.
**Trask Stalnaker (Microsoft Corporation)** 01:50 Hey!
We'll give one more minute.
It's either, small or late crowd today.
And we don't have… any… topic… listed, but I figure we will… so I figure we can just go to our… Tracking doc… I can… Start, I added… let's see, updates… or… So, for this one.
Just need another review approval on this PR.
So, somebody can… Do that, would be… Great, because this is then… Remember, this is sort of the template, then, for splitting out lots of these, Span types and metric.
Thanks.
**Aaron Abbott (Google LLC)** 04:33 I can take a look. Is it… Did you put it in the notes somewhere, Trask?
**Trask Stalnaker (Microsoft Corporation)** 04:42 Yeah, yeah.
**Aaron Abbott (Google LLC)** 04:49 I see it.
**Trask Stalnaker (Microsoft Corporation)** 04:54 I will actually sit up there.
Why don't we… See, aaron volunteered… Thank you.
Let's see… For the token usage.
So let's go through these in different order. We'll come to this one last.
This one… I think the, this one, I think, is ready for a PR.
Tatsushiko had… Volunteered to take this one.
But I actually… I actually have a different preference, from Ludmilla. So Ludmilla, gave kind of two options, and proposed option two.
And I think I prefer option one. Left a couple of reasons, but probably will. Best to wait on that.
one for Ludmilla's feedback.
**Aaron Abbott (Google LLC)** 06:13 Is there anything ready for review here, this one, 536?
Perfect.
**Trask Stalnaker (Microsoft Corporation)** 06:20 5, 3… oh, so this was the implementing, Ludmilla's.
proposal.
So I guess I should leave a comment here, as well.
**Aaron Abbott (Google LLC)** 06:36 Yeah.
integrate.
**Trask Stalnaker (Microsoft Corporation)** 06:43 Oh, go ahead.
**Aaron Abbott (Google LLC)** 06:44 I was just gonna say, maybe we can talk about this one after updates, if you want. I've thought about it a little bit, too.
**Trask Stalnaker (Microsoft Corporation)** 06:50 Okay.
Yeah, may as well spend a… Couple minutes here while we're… while we're here.
Yeah, what were your thoughts?
**Aaron Abbott (Google LLC)** 07:02 Yeah, I mean, I think the… I haven't read too closely the breakdown Ludmilla gave here, but like, obviously… The percentile calculations are gonna change whether or not we include, like, zeros for certain modalities, and I think Depending which way we do it.
Like, we should think about the use cases in terms of alerting and whatnot.
**Trask Stalnaker (Microsoft Corporation)** 07:27 I think you might be talking about,
**Aaron Abbott (Google LLC)** 07:32 The zeros.
**Trask Stalnaker (Microsoft Corporation)** 07:33 This one… Is this one? No.
This one… You might… I think you might be talking about this one.
**Aaron Abbott (Google LLC)** 07:55 Okay, yeah.
And the other one was for…
**Trask Stalnaker (Microsoft Corporation)** 08:00 The other one was specifically for the operation input token and operation, so the histogram ones.
versus… The… These are the only two histogram token ones that we have.
The modality ones are the counters.
**Aaron Abbott (Google LLC)** 08:22 I see.
**Trask Stalnaker (Microsoft Corporation)** 08:27 So maybe you were thinking of this one, but just without the modality aspect.
**Aaron Abbott (Google LLC)** 08:34 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 08:36 So, Ludmilla, I mean, the question here is… Currently, these histograms don't have error type.
And… So… Ludmilla's point is that Bravo, the most likely thing you might want to… distributions and outliers among failed operations aren't meaningful.
Which I think is probably true.
And… So, she's arguing that, yeah, the histogram, it skews the histogram if you… record… The zero on failed operations.
And so, we've got two options there. One is to add the error type.
Attribute.
Which would then… you'd have essentially separate percentile distributions for successful and not successful.
Do we have a… Yeah, yeah, yeah.
The other option is just don't record them for failed operations.
And I guess my thought, is… if we do want to limit it to successful operations only, maybe we just… maybe, renaming it to successful operations. What I… my concern is that this looks like… Like, I would be surprised that the histogram count here doesn't match the operation count.
And it's not clear that it's filtered by… on.
Yeah, the error by successful. So I guess either of these two options.
**Aaron Abbott (Google LLC)** 10:48 And then, so just to be clear, the partial failures, they can happen like during a stream response when some tokens are returned, right?
And the proposal is to… your proposal is to continue counting those.
Without renaming?
**Trask Stalnaker (Microsoft Corporation)** 11:08 I actually don't care between these two options.
So… if… We think that there's no use case for having that distribution of, tokens on failed attempts.
Then, you know, maybe this is the simpler option.
**Aaron Abbott (Google LLC)** 11:39 Yeah, I kind of agree with you. I don't care too much as long as the Semantics are super clear.
**Trask Stalnaker (Microsoft Corporation)** 11:55 And then this one… oh, yeah, this one… I think this one is pretty straightforward.
I think this is just about the span and event attributes.
not about metrics, and I think it makes sense to not report.
Zeros, and none.
return things.
on those.
This one… keeps coming up. Felix left a comment a few days ago.
I know that… so this is the question of… you've got, oh yeah, I wrote it here.
You've got an invoke agent span, and then you've got chat spans under it.
And you've got your input tokens on the chat spans.
And then you've got this aggregate thing on the invoke agent.
And, it's been reported multiple times that people Just are summing up input tokens across all the spans, instead of limiting it to only the chat spans.
So, it… does feel it's clearly a foot gun, as, Felix said.
At the same time, it's, it's, weird from Semantic Conventions' perspective, like… This is completely different, meaning on chat versus on Invoke Agent.
It's… It feels well-defined as it is, but really, people are making mistakes, so it's probably… It is something we need… should think about.
I don't know if it… I mean, one option is… to re… to have a different name on Invoke Agent.
Kinda sucks, because it's, like, it's very arbitrary, like… Just a different name.
Another option would be just to not report it on Invoke Agent. I don't know if…
**Aaron Abbott (Google LLC)** 14:26 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 14:26 folks find it useful on Invoke Agent.
I…
**Aaron Abbott (Google LLC)** 14:31 I think we… I think we discussed it a couple times, and it's like, it's always this question of denormalizing it to make it easier to read.
And I think there are plenty of people in the camp that it was helpful to have it on Invoke Agent.
**Trask Stalnaker (Microsoft Corporation)** 14:47 Hmm.
**Aaron Abbott (Google LLC)** 14:50 I don't hate the separate name. I think last time we talked about this, I mentioned, like.
It's kind of like in profiling, when you have a node, you can see self.
self tokens versus like cumulative or not, not tokens, but like CPU time or memory, or whatever. So.
**Emil F** 15:12 I think the separate name looks cleaner, because it's… different thing, right? One being an aggregate, the other one being per operation.
And, yeah, looks better, but how… Like, for people who are trying to visualize this, what happens if… if the values don't line up?
Are you showing the sum of those tokens for each operation, or are you showing the aggregate?
**Aaron Abbott (Google LLC)** 15:49 Was it a question if they don't line up? Sorry.
**Trask Stalnaker (Microsoft Corporation)** 15:53 Yeah.
**Emil F** 15:53 Yeah. Oh, sorry.
**Trask Stalnaker (Microsoft Corporation)** 15:54 What should, what should your back end… Display? Is that your question?
**Emil F** 15:59 I mean, yes, like with any denormalization.
You might end up with values that are slightly conflicting, or… conflicting a lot.
So, what should be the guidance there?
**Aaron Abbott (Google LLC)** 16:17 I'll get, you know, go ahead.
**Ankit Singhal** 16:19 I definitely think, like, giving the aggregated token count on the invoke agent.
It's definitely a challenging problem.
Here we are just talking about like chat, chat span, and you can also think about tools which calls or which can use LLMs, which internally can call other agents, right?
getting to a point where you can appropriately say that, yes, these aggregated tokens is for this entire invocation operation.
In my opinion, it's a really hard problem to solve.
**Aaron Abbott (Google LLC)** 16:58 Yeah, Surya.
**Surya Teja** 17:05 Yeah, so for overall, Stuff, aggregating tokens as well as in… on the metric side also.
Say, if you have… if you are having an agent, if you are, doing a histogram of tokens. That also is not reported, correctly, right, if you do this.
**Aaron Abbott (Google LLC)** 17:30 You mean, like, the accounts being different?
**Surya Teja** 17:33 Yeah, yeah.
**Aaron Abbott (Google LLC)** 17:36 Yep.
**Surya Teja** 17:38 Yeah, and…
**Trask Stalnaker (Microsoft Corporation)** 17:39 Histogram?
**Surya Teja** 17:40 Say if we have, tokens on, the agent calls that… Say you have two or three agent calls, and if you aggregate all the tokens For each agent, and you plot it on histogram to report the metrics of how many tokens have been used for each agent.
That… I think that might be wrong, but I'm not sure if we are able to report the right number of tokens for each sub-agent call and agent call, and then finally show what is the total number of tokens Used by this Singleton When you send a prompt, that might be wrong if this thing, like, comes in right.
**Trask Stalnaker (Microsoft Corporation)** 18:39 Yeah, that's, like, you also have subagents, so would aggregate be… the total of… All, like, include subagents.
**Surya Teja** 18:51 Yeah.
**Ankit Singhal** 18:52 Yeah, exactly. And then sub-agents also, you'll report some numbers, right?
And I double counting there.
**Surya Teja** 19:02 Yeah.
I have something totally on the same lines. I have one more question.
Today, with the metrics that we are using for counting or reporting the number of tokens for each agent.
I think we are double counting it, because we are giving the count of all the tokens, one single agent.
took, but there will be sub-agents being spawned by that agent, and we are also counting those tokens, and we might be over-reporting it.
I don't have a good example, but.
We should be targeting for that also, if we see a bug with our metrics reporting on agent… on tokens.
**Trask Stalnaker (Microsoft Corporation)** 19:54 I don't know if we even define what it… whether it should include… The sub-agents are not…
**Surya Teja** 20:04 Yeah, yeah, I'm not sure, Trask.
So, I might be wrong over here, because I might be… Speaking from my memory, which might be stale.
**Aaron Abbott (Google LLC)** 20:17 Yeah, I think it becomes increasingly difficult to instrument as well. So like the query approach is really painful, but it's probably more correct.
Because, like, like, the instrumentation needs to somehow track what the subagents did, and if the, like, agent framework isn't doing that, for example, if it, say it's, like, a subagent call via A2A or something like that. It's gonna be pretty much impossible to do that.
**Ankit Singhal** 20:49 I think my preference would be for accuracy for tokens rather than ease of simplicity.
**Trask Stalnaker (Microsoft Corporation)** 21:00 have.
**Emil F** 21:00 understanding.
**Trask Stalnaker (Microsoft Corporation)** 21:01 gravitating to this option.
Sorry, Emil, go ahead.
**Emil F** 21:07 I'm just trying to understand, when you guys say accuracy, are you, do you see the per span Token count… Being the more accurate option, or the aggregate being the more accurate option?
**Ankit Singhal** 21:23 I think if I understand right, probably just reporting tokens count on the chat spans, where actually the token consumption happens, right? And then using that, which is basically a de-nozzleized form, right? And this is the lowest leaf where you actually consume tokens, right? And then aggregating them based on… That's how you would do, depending on, like.
if you want to do this for entire invoke agent span, and then all its underlying optical. Yes, you can do that. But I think, as Aaron was saying, that would make your queries more complex.
Yeah, okay.
**Emil F** 21:59 bank.
**Ankit Singhal** 22:00 That's my understanding, though. If… There is a different understanding. Please do. Yeah, yeah. Awesome.
**Emil F** 22:08 Yeah, that's actually kind of what I also want to say, that, you know, having the per-span tokens make things more verifiable, because you can pin a particular token Bend, if you will, to a single span.
At a granular level, where I can… where I can see that That makes sense or not. If you get an aggregate over a trace that has, you know, hundreds of spans.
It's… it's hard to figure out if there's an error.
**Trask Stalnaker (Microsoft Corporation)** 22:45 Cool, I think this helps me.
I will think some more about this, and… Try to leave a comment on the issue.
Sort of summarizing… options and concerns.
**Aaron Abbott (Google LLC)** 23:03 One final thought, like, in the context of stabilization.
I feel like removing from invoke agent and then leaving it open to add another, like a new attribute that seems we could address that later if it's controversial.
**Trask Stalnaker (Microsoft Corporation)** 23:22 Yeah.
Makes sense.
Alright, Anything that other folks want to… Raise or discuss?
or report on.
**Samyak Choudhary** 23:44 Yes, am I audible?
**Trask Stalnaker (Microsoft Corporation)** 23:47 Yeah.
**Samyak Choudhary** 23:49 So Traska went through with the PR in the tools one, 525.
I took a look.
Yes?
And it stated that the.
Jen, the tool call ID, was written by two identities for now. Like, the LLM can return it, or either the framework that they're using can return it.
So, it was suggesting that the LLM only should return the tool ID and not the framework, but because that doesn't make much sense.
So the, Suggestion was to change the, the call ID mark span to, from recommended to conditionally required.
Because recommended.
So this is some ambiguity, if the framework has provided it or not, or if the user has selected not to, like, take it. So… I thought, like, conditionally required would be better for the particular use case.
**Trask Stalnaker (Microsoft Corporation)** 25:09 cool, and so that's.
Okay, so it's from recommended to conditionally required. Okay, so that's what the PR is doing today.
So is there anything that you would like to see changed in this PR, or is… do you think this PR is good to go?
**Samyak Choudhary** 25:35 Like, it seemed fine to me, I wanted to know your views, like, what do you think?
**Trask Stalnaker (Microsoft Corporation)** 25:43 Cool, why don't you go ahead and approve it, if it looks good to you?
And that will be a good sort of indicator for other people to take a more detailed look.
**Samyak Choudhary** 25:58 official.
**Trask Stalnaker (Microsoft Corporation)** 26:36 Great.
Anything else?
Thank you, Aaron, for adding…
**Aaron Abbott (Google LLC)** 26:47 Yeah, I just followed up.
**Trask Stalnaker (Microsoft Corporation)** 26:49 share.
**Aaron Abbott (Google LLC)** 26:50 Yeah, I just kind of replied to Felix. Maybe I'll ping him on Slack and see if we can make some progress here.
**Trask Stalnaker (Microsoft Corporation)** 27:05 Cool.
Last… last chance here, anything anyone else wants to discuss or raise?
**Aaron Abbott (Google LLC)** 27:16 I did file one more issue on the inference parts thing.
Oops, sorry, I'm kidding.
It's in here, it's basically… we have a top-level array for the messages, and… It's kind of… Not the greatest thing to work with, so… This is a kind of disruptive change, but… If we want to have something like If you want to add any metadata, for example, it's really difficult right now, because you obviously can't stick that in an array, so… Yep.
**Trask Stalnaker (Microsoft Corporation)** 27:50 All right.
Yeah, okay.
**Ankit Singhal** 27:57 I recently came across PR, I think it was in June.
about like agent id attribute being removed from internal invoke agent span.
So I just want to understand the motivation behind that.
**Trask Stalnaker (Microsoft Corporation)** 28:12 Can you drop a link?
**Ankit Singhal** 28:14 Yeah, let me…
**Aaron Abbott (Google LLC)** 28:25 I think that was from me, right Ankit?
**Ankit Singhal** 28:29 It's okay. Thank you very much for Lumila.
**Trask Stalnaker (Microsoft Corporation)** 28:41 Okay.
**Ankit Singhal** 28:42 Yeah, it's on YouTube.
But yeah, I do see a lot of clue on this, so…
**Trask Stalnaker (Microsoft Corporation)** 28:47 Did you have, yeah, did you have a use case that needed this on… Internal spans?
**Ankit Singhal** 28:55 Yeah, yeah.
**Trask Stalnaker (Microsoft Corporation)** 28:58 Can you explain?
**Ankit Singhal** 28:59 Yeah, so, for example.
When you have a hosted agent, right? Hosted in, like, a remote agent running in cloud.
And you give customer the control to bring their own.
like the framework they want to build. And you provide those infrastructure part right?
So… Yeah, like.
there, like customer registers their agent as a as an entity that they can define right within that platform, whether it's Gcp, Azure, or anywhere. Right?
And then we would like to associate that the agent code that's running, which probably could be running Langchain, or could be running Microsoft Agent Framework, or Strands, right, anything. And it emits invocation internal spans, we can probably associate them, via… getting that invoke agent… agent ID to be the platform provided ID, so that we know, okay, this is for that.
Agent, right.
**Trask Stalnaker (Microsoft Corporation)** 30:00 So two quick thoughts and then get Aaron's.
But one is, can it be a… why a internal span versus a server span?
For your use case?
**Ankit Singhal** 30:21 I.
**Trask Stalnaker (Microsoft Corporation)** 30:21 Other… Is, have you seen Aaron's… entity, this PR?
**Ankit Singhal** 30:36 Oh, no, I've not seen this one. Okay.
**Trask Stalnaker (Microsoft Corporation)** 30:39 Okay, so this is what I think… Sounds maybe like what you would want?
Instead… So yeah, maybe we're out of time, but, yeah, check this, and then, yeah, kind of the answer to whether what you're modeling is really a server span versus an internal span.
But yeah, definitely, yeah, we can discuss more.
**Ankit Singhal** 31:08 Something. Yeah, we'll take a look. Thank you for sharing. Appreciate it.
**Trask Stalnaker (Microsoft Corporation)** 31:11 Alright. Thanks, everyone.
See ya.
**Neil Yashinsky** 31:16 Thanks, Ian.
