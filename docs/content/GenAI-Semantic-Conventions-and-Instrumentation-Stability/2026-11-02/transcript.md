SIG: GenAI Semantic Conventions and Instrumentation Stability
Date: 2026-11-02
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Max Ind** 00:15 Hello.
**Trask Stalnaker (Microsoft Corporation)** 00:25 Hey, Max.
**Max Ind** 00:27 I'm sorry, I'm sorry. I'm deafened. Oh.
Now I can hear you.
**Trask Stalnaker (Microsoft Corporation)** 00:32 Hey.
**Max Ind** 00:33 Hey, thanks for the review and the… On 571.
**Trask Stalnaker (Microsoft Corporation)** 00:38 Yeah, thanks for getting that, Almost to the finish line there.
**Max Ind** 00:44 Yes.
**Liudmila Molkova** 01:42 Good after… Noon. At least it's afternoon for everybody.
**Trask Stalnaker (Microsoft Corporation)** 01:48 Yes.
**Max Ind** 01:51 Hey, it's… it's, it's… it's afternoon, yeah.
**Liudmila Molkova** 01:56 Late.
**Trask Stalnaker (Microsoft Corporation)** 01:59 Fair.
**Liudmila Molkova** 02:05 Okay.
Still… We have a quorum.
Trask and Google.
Oh, Emil as well.
Okay.
So, it seems we have quite a few… Renaming PRs… Oh.
You want more renames.
**Trask Stalnaker (Microsoft Corporation)** 02:49 You were, you had hinted on the… about this a couple of times recently.
So I thought about it some more and agreed.
**Liudmila Molkova** 03:01 I… don't feel like we have to do this. So, like, if we don't do, I will be fine, but, like, if we… if there are… if you think that it's something Better to do now. Let's do it.
**Trask Stalnaker (Microsoft Corporation)** 03:22 I would. Seems, brings consistency across… the GenAI, especially metric names.
**Liudmila Molkova** 03:37 Yeah.
That's kinda happy that we didn't touch envelopes So, I am going to sum that up.
And, I'll update the PRs that they have happened for, I think, a few of those, a couple of those.
**Trask Stalnaker (Microsoft Corporation)** 04:13 Okay.
I… I was… yeah, we've got so many things in flight, we just, I think it's okay to do either, add… update them in the PR, or merge the PR, and… Follow up.
**Liudmila Molkova** 04:36 Oh, okay.
This one… Awesome, you summarized it all. That's great.
**Trask Stalnaker (Microsoft Corporation)** 04:51 Yeah… well… Me.
But yeah, so maybe we can go through… I mean, prioritizing, I think, getting the open PRs reviewed and merged, just since we do have a lot.
**Liudmila Molkova** 05:13 Yeah.
So this one can go lost, and it doesn't have any controversy, it's just a tool link update.
**Trask Stalnaker (Microsoft Corporation)** 05:20 Cool.
**Liudmila Molkova** 05:21 For, for everybody.
not familiar, there is this more formal way to define, like, the fallback list of Span names based on the attribute values.
**Trask Stalnaker (Microsoft Corporation)** 05:36 Oh, nice.
**Liudmila Molkova** 05:39 Yeah.
So this one… Best friend is super important.
And… We approved it. There's some feedback still.
Right.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 05:59 But it looks really close.
**Liudmila Molkova** 06:01 Yeah, I think there is one discussion that we probably should have.
around, like, the operation name?
And… Max, can you remind me, you have the closed list now, right, of operation names?
**Max Ind** 06:17 Oh, I don't.
Yeah, I was… there's, like, one more… one comment from… Yeah, from Christian.
On the… operation name, and I wondered, do we want, because, I wonder if, what the gap is gonna be between now and when the… span type is part of OTLP, because right now the only two entry points are… that are not agent and workflow are ADK and OpenAI SDK, and both are coincidentally named Runner, so I wonder if this gap is, you know, in the short term, if it's okay?
And then if it's not okay, then I wonder what the invoke entry point… To have the closed, set.
How… how would that sound to everyone here?
Instead of, invoke and Framework Entry Point.
**Liudmila Molkova** 07:28 I have some thoughts, I'll just finish typing notes and, I'm sure.
**Trask Stalnaker (Microsoft Corporation)** 07:39 I mean, we don't normally do closed enums, But listing the possibilities is still helpful to keep people sort of contained.
**Felix Becker (Anthropic)** 07:53 Is there a timeline for when… the spend type will be available in OTLP?
**Liudmila Molkova** 08:01 So, I really hope to merge the spec changes maybe this week, if the world cooperates, I don't, like, I think it's possible.
Then, the key question is when it becomes stable for instrumentations to actually rely on it.
And I think it will take a few months.
And I personally am very invested in this, and there is a lot of interest from Google's side, organizationally, to make it happen. But it's not just in my power, but I, like, think optimistically it will take a few months.
**Felix Becker (Anthropic)** 08:42 a few months.
**Liudmila Molkova** 08:43 Yeah, to stabilize, because it's landing in development, and it needs some time to, like, be supported.
Broadly, and we're talking about end of year, so I don't think this year would happen.
**Felix Becker (Anthropic)** 08:58 Okay.
So we should not really rely or count on it, then.
**Liudmila Molkova** 09:04 I'm… I mean, we… It will become real.
Soon enough.
So we should design for it. I was thinking that… The short term would be that we just document every operation named that Like, a relationship that these operation names are expected with the spend type.
But… and this is what I mean by the closed set, so we… we're not saying yet use whatever operation name you want.
We're saying you should use these operation names.
I don't know how do we work around, like, the should and spend type.
That didn't land fully.
**Trask Stalnaker (Microsoft Corporation)** 09:54 Oh, I see, so the problem is being able to aggregate them together.
without span type. I see.
**Liudmila Molkova** 10:03 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 10:06 Yeah, we… it still needs… like, it still needs to get into pro… the proto… Otlp.
**Max Ind** 10:17 Yeah, so…
**Liudmila Molkova** 10:18 Go ahead.
**Max Ind** 10:19 Yeah, so… for operation name, I think that, like, the two… options are, like, go with, invoke entry point, or, like, maybe go with, like, a third name that I don't know, or just have, like, a non-parsimonious, just invoke Runner, just because it just so happens that ADK and OpenAI agree on the term here, so it can be, like, a carve-out.
And then if… but this runs into an issue that if, like, a third framework appears that we didn't know of, then… we may have to extend it, but I'm fine with, like, a shared name.
If everyone is… Here is fine with, like, a more abstract, like, invoke entry point.
**Liudmila Molkova** 11:14 I… I was thinking that, we would… we already have this, And this makes sense for… ADK and OpenAI, and if somebody else appears, for example, somebody very motivated from Langraph, like Emil, would come and say, okay, we want invoke Gruff.
we would just add it to the list of operation names, and then if somebody wants, like, query, I would want to say executeTask, we would add ExecuteTask.
**Max Ind** 11:47 That's fine.
So I'm sleeping.
I can change the wording so that it's like, you know, part of a list. I think there is, like, an enum somewhere, yeah, so I can modify that.
**Trask Stalnaker (Microsoft Corporation)** 12:02 Would it be an enum?
I mean, modeled from… Semantic Conventions.
**Liudmila Molkova** 12:10 It's already in a num, right? But it's just we… it's a subset, it's a list of values within a num.
**Trask Stalnaker (Microsoft Corporation)** 12:19 Operate… are we talking about operation name?
**Liudmila Molkova** 12:21 Huh.
**Trask Stalnaker (Microsoft Corporation)** 12:22 Oh, okay.
I didn't realize.
Then that's easy.
**Liudmila Molkova** 12:36 Okay, so we can document more.
And this is the source for consumers to discover supported.
Constance.
**Emil Filipov** 12:51 I… I'd only ask here that we have Some kind of reasonable guidance on when to use which type.
Because some of those are, kind of, Overlapping or vague concepts.
And ideally, people should know which Which time they should, they should emit.
Or, I don't know.
Or which kind of workflow.
**Liudmila Molkova** 13:16 So ideally in the… yeah, go ahead.
**Trask Stalnaker (Microsoft Corporation)** 13:19 I was just gonna say, ultimately, I… there shouldn't be… it shouldn't matter that much, once there is a… because they all are gonna share that span type.
Unless I… you were thinking of maybe, Liudmila having refine… span refinements for… Okay, in which case it would.
**Liudmila Molkova** 13:44 Right.
Yeah.
**Trask Stalnaker (Microsoft Corporation)** 13:54 But once we have the span refinements, that also helps it to become clearer.
Presumably because you have attribute sets that may apply or not apply.
**Liudmila Molkova** 14:09 Yeah, so, like, if we had, let's say, graph… Attributes.
I would say, okay, apply that refinement.
And put graph attributes there.
Only on… and then it's kind of natural that you would use invoeGraph, but also… To a large extent, it doesn't matter what operation name you give. It can also be even language-specific.
So, because it's not something you query by, it's just a display name, useful display name for users to, like.
Connect the traces they see with the code they wrote.
**Emil Filipov** 15:02 Yeah, if… Yeah, I'd really like some guidance there. A lot of those will be… Kind of can get conflicting between… between the different emitter libraries.
and then you would have, at some point, some kind of refinement. You said, like.
Something based on the type that you need to interpret differently.
Or that you expect or do not expect because of the type.
**Liudmila Molkova** 15:32 Yeah, and I think currently, Max, you have some guidance, right?
**Max Ind** 15:35 Yeah, I have some, some guidance. It's, like, the terms agent and workflow, they have a lot of commonalities, so I tried to… Mostly, like, have a short… One sentence description, and then just give a lot of examples.
Anchor.
people, yeah.
**Emil Filipov** 15:58 Okay, yeah, sounds good.
**Liudmila Molkova** 16:03 Maybe for something like, let's say.
line graph, or ADK, or anything, we would… Half.
one or more refinement of the span, ideally, right? We would have something specific to 80 key, saying… How to populate all the things, and which spans are emitted, and which operation names are emitted per as decay.
And we would, yeah, we would need guidance for the… To create these conventions, but then, for the end users, it's kind of documented.
So, Emil, maybe, can you take a look at this and see if it provides enough guidance so far, and what else would you like to see?
**Emil Filipov** 16:56 Yeah, okay, which, PR was that?
**Liudmila Molkova** 17:00 5… 7… 1…
**Emil Filipov** 17:03 Okay.
**Liudmila Molkova** 17:04 Yeah.
**Emil Filipov** 17:04 Okay, cool.
**Liudmila Molkova** 17:05 Post the one in the chat.
Sorry, desktop sharing?
**Trask Stalnaker (Microsoft Corporation)** 17:15 Yeah.
**Liudmila Molkova** 17:17 Sorry, I don't know how it happens.
Okay.
So we… Other than that… It seems we are… We talked through things… One thing I wanted to, just FYI, the… oh.
how do we want to do… work with the boundaries? Because, Trask are proposing to change, and we're… it seems we're going to give… get a new guidance, and here we want to go up to 24 hours.
**Trask Stalnaker (Microsoft Corporation)** 17:58 Yeah, I was not going to try to interfere with existing PRs, and just let the… let the bucket boundaries go in and then fix everything up in 655, or whatever that is, yeah, because it overlaps with… I think I listed, like, at least 4 or 5 PRs have overlaps with that right now.
**Liudmila Molkova** 18:20 Oh, okay. So you'd like to… for this one to wait.
**Trask Stalnaker (Microsoft Corporation)** 18:24 Yeah.
**Liudmila Molkova** 18:26 Okay.
**Trask Stalnaker (Microsoft Corporation)** 18:27 I can mark it as… or you can mark it… I'll mark it as draft, just to… so we don't accidentally merge it.
**Liudmila Molkova** 18:35 I can never…
**Trask Stalnaker (Microsoft Corporation)** 18:36 I can't block my own PR, unfortunately.
**Liudmila Molkova** 18:45 Cool. Then, Max, if you work on the feedback, it should be ready to go soonish?
Thanks a lot for pushing.
**Max Ind** 18:55 Thanks, Pictito, for reviews.
Thanks a lot of people who are obvious.
**Liudmila Molkova** 19:05 Okay.
So, what, else do we have here?
Remote versus internal…
**Trask Stalnaker (Microsoft Corporation)** 19:20 That one, I think, is ready. I have a couple of comments, but if they're not addressed, I can just push and merge it.
**Liudmila Molkova** 19:28 Okay.
**Trask Stalnaker (Microsoft Corporation)** 19:30 Next one, we can probably close with Max's PR, because it's about the yeah.
I'll, I'll… Check on that, but I think we can.
**Liudmila Molkova** 19:54 Hmm, let's just write a comment.
A long.
Nested… oh, the… the isNested thing.
**Trask Stalnaker (Microsoft Corporation)** 20:42 Yeah.
Do we… Is that something we still… Field that we need.
**Liudmila Molkova** 20:58 I think so, because without it, these metrics are… like, you cannot even… You have to have advanced knowledge. Oh.
about your agents to make anything meaningful out of the invoke agent metric.
**Trask Stalnaker (Microsoft Corporation)** 21:18 Yeah, I'm just trying to think how this is different than, say, like, HTTP client instrumentation.
Right, we have a nested HTTP client, And those… We don't really say anything special about nesting But they suffer the same problem if you do capture them both. Like, it's kind of… we've kind of left it up to instrumentations so far to deal with that and to suppress nested… Not saying it's not a good idea, I just… maybe it's a more general… or maybe we should take it on as a more general.
Topic.
**Liudmila Molkova** 21:59 I mean, we solve it by having a dashboard per Service?
For HTTP, right, you only have one HTTP server.
Span per service. And here you can have…
**Trask Stalnaker (Microsoft Corporation)** 22:13 I've talked about HVVP client spans, which can be nested easily.
**Liudmila Molkova** 22:22 Not within one service. It's invalid.
**Trask Stalnaker (Microsoft Corporation)** 22:25 Why… why is it invalid?
**Liudmila Molkova** 22:29 I mean, it's very rare to call your service over HTTP.
**Trask Stalnaker (Microsoft Corporation)** 22:37 Maybe I'm not clear on what we're talking about here. I thought we were talking about, like, say, like, we have an HTTP client that wraps another HTTP client, and so you end up with nested… spans.
**Liudmila Molkova** 22:52 I mean, we suppress them, usually.
**Trask Stalnaker (Microsoft Corporation)** 22:55 Yeah, so how is this one… is this different?
Info.
**Liudmila Molkova** 23:01 There's different… if I'm trying to build a dashboard, Not for inference, for agents.
that if I build that dashboard.
**Trask Stalnaker (Microsoft Corporation)** 23:11 Oh, perfect.
our link here is about inference.
Oh, I'm sorry, I'm looking. I… oh, sorry, I had jumped ahead. I was on 475. This is why we're… I'm talking past you, sorry.
**Liudmila Molkova** 23:27 Yeah, Max?
**Max Ind** 23:29 Oh, no, no, no, no, I think you arrived at the… At the disagreement, yeah.
**Liudmila Molkova** 23:36 Okay.
**Trask Stalnaker (Microsoft Corporation)** 23:40 Yes, I agree with the… the… I think I agree with the… invocation, the agent stuff is… Different.
**Liudmila Molkova** 23:53 Okay, yes, yes.
**Trask Stalnaker (Microsoft Corporation)** 23:54 We faced that problem, because we don't really have any… we don't have much internal span stuff.
**Liudmila Molkova** 24:04 Yeah, so for… for this one, I think it's… the issue Felix brought up, and… Pa… oh, this is different.
So, this is the… in the same process.
And I think Dylan has a solution in… pretty awesome solution in Python.
And we don't need any semantic convention changed to trade.
**Dylan Russell** 24:42 Yeah, I think we were gonna wait for that… So, like, be around for a little bit.
Before we… went with… like a semantic invention change. So maybe we can just close this for now and wait.
**Liudmila Molkova** 25:03 Maybe we can create an issue and document there that the proposal is to suppress Like, the ones that are truly nested, like, two different Libraries doing Instrumentation for the same thing.
And then, We would keep the issue open to track if anything needs to happen in semantic conventions, and that anyone who tries to find the solution would find the issue.
This proposal and comment if they disagree.
**Dylan Russell** 25:36 Okay, that works.
I could also reach out to some… like, I reached out to Max already about updating ADK with what we did.
But there's a few other with, like, native instrumentation where we could… Tell them what we're doing.
**Max Ind** 25:57 Yeah, and I'm in the middle of, of, using, like, trying to, because right now we're doing a lot of Basically refract… reflection on, like, the check if the… Instrumenter is, is installed in the user's code, and I'm trying to rewrite that to use the proposal.
Dylan merged into… into Python, yeah.
**Liudmila Molkova** 26:32 A.
Maybe we should blog about this, because I think it's a new approach in open telemetry to actually enrich in the inner layers.
Would be cool to get the word out.
Yeah.
Okay, so this one is a Terreville… thing that… just documents that these are the logical inference operations, because there were some PRs in Python.
That assumed that we wanna report all the… HTTP request to the model, or, like, protocol requests to the models, including retries.
And, this document, that is, the number of logical calls don't go deeper than the inference operation.
Okay, so it sounds like we're… We're… there is no… not much to do, just, close and merge some stuff.
**Trask Stalnaker (Microsoft Corporation)** 27:47 Yeah, I am.
**Liudmila Molkova** 27:52 Metric names and buckets… Yeah, there are…
**Felix Becker (Anthropic)** 27:58 It's case for the count of inference calls.
As a metric.
**Liudmila Molkova** 28:05 Sorry?
**Felix Becker (Anthropic)** 28:06 What is the use case of the count of inference calls as a metric?
**Liudmila Molkova** 28:15 Max, do you want to talk.
**Max Ind** 28:16 Yeah, yeah, the… so that's mostly to measure the efficiency of an agent, so, like, if… The agent makes fewer inference calls and tool calls, then you can say that it's, like, more efficient.
And, like, I believe that, like, at least, like, the Google… flash models. I don't know the latest, like, argon and carbon numbers, but, like, at Google, we had, like.
Issues where we, like, We're, like, advancing, but we're advancing at the cost of the model doing… more, Yeah, more inference and tool calls, so that's kind of, like, a way to measure.
this… Yeah.
**Felix Becker (Anthropic)** 29:01 And what… what dimensions do you expect to, like, be used with that metric?
**Max Ind** 29:09 What dimensions? I think just the agent name.
**Felix Becker (Anthropic)** 29:15 Okay.
So, it would be, like… Total number of inference crawls across all sessions for that agent.
Because wouldn't that be biased to… like, you would have to divide that by number of sessions, right? For it to be…
**Max Ind** 29:30 I think it's per… yeah, I think it's per… Single end-to-end invocation right now.
So… Is that what?
**Felix Becker (Anthropic)** 29:41 Maybe a very, very high cardinality, no?
**Max Ind** 29:45 Wh-white?
**Felix Becker (Anthropic)** 29:47 If you do it per session, and not per agent.
**Aaron Abbott (Google LLC)** 29:52 It's not a dimension, it's just, the granularity of the histogram.
**Liudmila Molkova** 30:00 Yeah, so it's the distribution for a single agent across all sessions.
**Felix Becker (Anthropic)** 30:07 Oh, I see.
Okay.
So, you can't actually tie it back to a session, it just gives you, like, a overall histogram.
**Liudmila Molkova** 30:19 Well, you kind of can for outliers, because there are… on metrics, there are exemplars. You can take a look at the outlier and see, like, an example of a trace where.
**Felix Becker (Anthropic)** 30:29 Right, right.
**Liudmila Molkova** 30:30 Shows it.
**Felix Becker (Anthropic)** 30:31 Okay, makes sense.
**Trask Stalnaker (Microsoft Corporation)** 30:34 And should we just… Because, it wasn't clear to me if that… those two metrics, the… Inference calls and tool calls for invocation.
We're part of our stability.
I guess I was… I was assuming the… I guess I was assuming they weren't originally… Let's see if I listed them… yeah, I didn't list them on the initial… List of metrics to stabilize.
Oh, let's see, yeah.
how widely, I guess, Ha… Are they widely used?
too many… Instrumentation supported.
**Liudmila Molkova** 31:31 Some instrumentation… sorry, I didn't support for this, ADK supports them.
I kinda see it both ways, so… just because they are… relatively straightforward, we can try stabilizing them, but also, I think if we, let's say, if we get into a habit of, like, stabilizing something every month, like, I can see that we can stabilize them as the next step.
So either way would work for me, but I… I'm looking at Max, and who's interested the most in them to say if… if you want us to try stabilize sooner.
**Max Ind** 32:13 Yeah, I wonder, because, yeah, I think if the stabilization would be, like.
every month, or every two months. I don't think there's, like, a pressing need to stabilize it right now, but maybe… but I'll ask, also internally, because Miko, I pushed this forward, so I'll ask… I'll ask him.
So that we can have, like, you know, a short stance on this, yeah.
**Liudmila Molkova** 32:41 Awesome, thank you.
We are at time, if… That's… finish the… what do we have in this section, and then call it?
**Trask Stalnaker (Microsoft Corporation)** 32:56 Sounds good.
**Liudmila Molkova** 32:59 Okay,
**Trask Stalnaker (Microsoft Corporation)** 33:02 Inc.
The first two are your PRs, we just need another approval on both of them.
**Liudmila Molkova** 33:12 Yeah, and these are just the continued renaming story.
I can try to update to the new name proposal, and now, ping… Aaron or Dylan to approve?
Those are a tree, though, nothing special.
So we talked a little bit about this one.
So the proposal that is going… already landed, or is going to land in Semantic Conventions is some guidance, right, and the idea that we use 1, 2, 1, 5, and in between.
So it's, it's no longer… Oh…
**Trask Stalnaker (Microsoft Corporation)** 34:06 Please.
Because I… I carried the one 2.55 into minutes, and those… the minutes ones look weird, because then you get, like, 60, 150, 300, 900, instead of, like… What, like, more… Eye abolish.
**Liudmila Molkova** 34:27 Yeah, and essentially the guidance is that, this should be friendly in minutes, and other than that, it's the… dissimilar-friendly, so… not like… Like, when you see it on dashboard, the boundaries look nice.
**Trask Stalnaker (Microsoft Corporation)** 34:48 And I like the 125 on the decimal part also. The only reason I went with 12.55 there is because it matches our existing HTTP bucket boundaries.
**Liudmila Molkova** 35:06 Yeah.
**Aaron Abbott (Google LLC)** 35:09 Could someone summarize the 4280? I'm a little out of the loop there. Is it… the goal is to make it align with, like, human units for time?
**Trask Stalnaker (Microsoft Corporation)** 35:20 The goal is that to provide some guidance for Semantic Convention authors on how to choose bucket boundaries so that we don't… everybody doesn't just Tick bucket boundaries out of the hat.
You're always free to pick other things, but this at least gives people And I narrowed it to only duration histograms.
I think, like, token count and other things, you know, like, I think the GenAI ones make sense to me, that just… Base 2 or base 4 exponential, or whatever.
But for duration, I think it's nice to be a little bit more uniform in OpenTelemetry.
**Aaron Abbott (Google LLC)** 36:10 Okay. Maybe I'll, review 4280, because I had… Some concerns with, like, exponential… matching exponential buckets.
as, like, a default, but yeah, I can take a look offline.
**Liudmila Molkova** 36:32 So it sounds like… We'll see what progress we make by… Wednesday, and we'll go through… The rest of things.
on Wednesday.
Yep.
Sounds good. Thank you. See you all.
**Max Ind** 36:53 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 36:53 I…
