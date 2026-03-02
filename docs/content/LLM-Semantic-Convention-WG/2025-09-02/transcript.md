SIG: LLM Semantic Convention WG
Date: 2025-09-02
Duration: 69 minutes
Zoom Recording URL: https://zoom.us/rec/share/yAJGfiQNH8hogvOkEExMbRUNPl-Ok3lUp27vEcnhnKQvXoVFZD376sPoXohWK5Sr.Gp8CAzsYrHesitfn
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:04:57 Oh, I'm sorry, I'm muted. Hi, everyone. How are you?
shiprajain 00:05:01 Hi, everyone. Good morning.
Bruno Baptista (IBM) 00:05:04 Hi, good morning.
Endre Sara 00:05:07 Good morning.
Liudmila Molkova 00:05:10 Hello, old friends and new friends. Let's give people a few more minutes to join and get started. I will start sharing in a sec.
Once I prepare my… screen.
Okay, welcome to our GenAI call. Feel free to add your name to the attendees list. If you want to discuss something, let's add it to the agenda.
Bye.
And let's see, we have a bunch of, pull requests to review and discuss, actually.
And, something to merge…
And there is some status update I want to discuss.
Okay, Shapri, you already added this to the agenda. Yes.
shiprajain 00:06:30 Wonderful.
Liudmila Molkova 00:06:47 So I think out of the pull request to review, the thing I want to discuss is, first.
The, role? This question, role versus gold versus description.
I think there is a PR with… one of them.
Which one?
Okay, there's our dusks.
This is role.
And now… Session ID, I think it's been out there for a while.
And I'd like us to have to…
Come up to some conclusion here.
And then… The last, but not the least…
We probably won't make much progress on it, realistically, but I'm going to list it here, and maybe we'll come back. The task…
slash workflow.
Here.
Okay, so I think people are around, and we can start, so maybe let's do… 10 minutes.
For this… 2015… And… Let's most…
data subdate here, as well. 5 minutes.
Okay.
Wonderful. Let's take a look at the triage board really quick. Let's just spend maybe a few minutes here, check if new issues were created.
Yes, a bunch of them.
Okay, so let's take a quick look… It's an issue.
We need to remove the…
inheritance from invoke agent to inference, because they don't necessarily have the same attributes. I can assign it to myself.
Like, put it in to-do… What else is there?
Argentic systems.
I think this is a huge topic. I think we're discussing it, some individual pieces of it.
We will… Get to some of this… points over time.
And it would be useful to actually link… okay, so there is this issue linked.
Okay.
I think I would like to reply on this issue.
Is Denny here, by the way?
Okay. Would people who work on agents, Shaper, Pavan.
Mind replying and linking your previous pull requests?
Saying that there are quite a few, and the documents we created in the past.
shiprajain 00:10:47 Yeah. Yeah.
Liudmila Molkova 00:10:50 Yeah, that would be wonderful.
So let me put it in the notes.
shiprajain 00:11:01 So, how do you suggest, Ludmila? Because we will have similar topics, around it, right? And we can expedite our work on that area as well in parallel, like, discussing about having a separate hierarchy as task or workflow, and now we are seeing… we are also having that suggestion.
So, do you think, now, you know, us from Microsoft,
Baban and Team from Cisco, and we all collaborate on discussing and concluding only on this topic, because this itself could grow.
Liudmila Molkova 00:11:32 The main goal I have is that everybody who works on badge and tech scenarios know about others who work on it as well.
And stay in touch, and make sure to come up, like, to… when the discussion… when the proposal happens. Everybody should, share their input.
So, my goal is to increase, the awareness and, hopefully build some consensus. My, like, the ask I have is that if you could, review this… there is not much of a proposal, right? There is a suggestion of specific namespaces, but if you could link your prior research.
It would let the person who created this issue know that there is a lot of things in the community that are already going on, and that they can review and share their opinion on.
shiprajain 00:12:21 Okay, okay. And if we have a perspective, should we also create a PR on that?
Because we were thinking to take it step by step, right?
Liudmila Molkova 00:12:31 Yeah, it's, it's like there is…
it's impossible to create a PR on that, right? There's, like, I don't know.
50 people.
shiprajain 00:12:38 Not on this one.
Okay.
Sergey Sergeev 00:12:45 Yeah, I'll, I'll add Danny to the thread, where we discuss the agentic stuff, One swag?
And we'll comment on that GitHub issue as well.
Liudmila Molkova 00:13:03 Wonderful. Thank you.
Shay.
Okay, awesome.
So then, the… I think we are way over time with our triage box.
have some steps identified. The next one is something new we practice. I would love to know, about people who are not coming here
didn't, like, regularly… what brings you here, who you are? If you want to share, please go ahead and share. If you don't want to share, it's totally fine.
Okay, no new intros this time?
Tristan Sloughter 00:14:24 I'm new.
Liudmila Molkova 00:14:26 Hi, Tristan. Hi. Good to see you.
Tristan Sloughter 00:14:29 Yeah, it's good to see you. Yeah, so I'm joining because I just joined Grok, and… My thoughts.
clearly some overlap here. The… I'm on the observability team, and they…
They have their Grok cloud, and doing tracing, and…
metrics and logging on the… in the Grok cloud regarding inference calls, so… thought there would be some…
overlap that I should join in here and see, what's going on, but I haven't actually talked to the inference team to find out what they need and what they're actually tracing yet. I'm doing that this week, so kind of…
Going, the wrong direction, but…
Hopefully, find out more about what they're actually doing, and then can…
Take part more in the… in the SIG.
Liudmila Molkova 00:15:20 Wonderful, great to have you here.
Okay, counting 1… 2… Sri!
Okay, no need.
No need interest.
Okay, so then, let's move on. Shipra, let's see what we have in this pull request.
There was… it's the continuation… sorry, it's the copy from the previous run, right?
And we've had a lot of discussions there.
I want to make sure people, Here,
Recognize it's the copy from the previous time. If you have any comments, please go ahead. I think the PR is now scoped down to the three new things, the two definitions, right, the call arguments and call result.
which essentially… Makes it… Non-controversial, to my opinion.
does anyone have any objections with going forward with this PR?
Does anybody want to take a look? And they didn't take a look yet?
Aaron Abbott 00:16:54 I can take a look, but I also don't want to block it.
So… maybe I'll try to take a look, like, today, we can…
Sujay Solomon 00:17:05 Forge by end of day. Does that seem reasonable?
Liudmila Molkova 00:17:09 Yeah, I can, set myself a reminder to merge it at the end of the day, and also I'll check with you.
That seems it's all good.
Thanks, Shipra, for working on this.
shiprajain 00:17:22 For sure. Yeah, thank you so much, everyone, for all the great inputs, and looking forward for the collaboration, because our journey for multi-agent tracing is still a long way.
So, I really enjoyed working with this group.
Liudmila Molkova 00:17:36 Thank you.
Sergey, you want to talk about…
Agentic attributes and Gen AI metrics.
Sergey Sergeev 00:17:47 Yeah, yeah, it's just, I just noticed that we have, Ian…
Agent plans, we have, all the attributes, agent…
ID, agent name, and so on defined, so if… we look into Gen AAA,
metrics, so it's the same, token usage, or operation duration metrics, which are missing those attributes, which can be optional.
I just wanted to do sanity check before I create a pull request to add those, but basically, we should be able to slice and dice by those attributes, the metrics.
I don't see any reason why it shouldn't be here, but let me know.
If there are any objections before I create his pull request.
Liudmila Molkova 00:18:41 So… when we report talking usage. Let's just… let's imagine we have an agent, the client, the framework agent.
Then, you would have… the LLM call, counting tokens.
Would you also have the agent called counting tokens?
Sergey Sergeev 00:19:04 Yeah, so basically, the goal for this, we need to attribute token usage, to different agents. So when you monitor agentic framework, you will… your agent, orchestrator agent, let's say, will
make OM calls will, basically produce,
We'll consume some tokens, it will be an operation with some duration.
And those metrics are important for customers to understand how many tokens an agent using, and so on. So it will be just additional attributes from…
frameworks like WenChain, WANGRAF.
Liudmila Molkova 00:19:50 So I'm… Maybe I'll do this, sorry?
Hong Kuan?
So, let's imagine we have, a span.
Yeah. For the agent, right?
And let's say it did 3 LLM calls.
Sergey Sergeev 00:20:09 Yes.
Liudmila Molkova 00:20:13 And there… there was…
One, like, 10 input tokens here, 20 output tokens here, and each of them will have some different number.
Sergey Sergeev 00:20:25 Yeah, and, basically, LOM calls will be child spans of the agent invocation, so they will inherit, agent ID, agent name, and so on.
Thank you.
Liudmila Molkova 00:20:39 Yeah, can you wait a sec?
Sergey Sergeev 00:20:41 Yeah, sure.
Liudmila Molkova 00:20:41 So, the token usage we are measuring today would be…
the parallel LM call, right? Yeah. And you can,
Say that the sum of all… all of them, Is your total usage.
Sergey Sergeev 00:21:00 Yes. Basically, every, every,
A woman vacation will produce a metric measurement.
With those values, and attributes
which we defined in the metric. So right now, we can, slice and dice those metrics, by…
If you go back to that methodic, definition in semantic convention.
Liudmila Molkova 00:21:27 Yeah, so what I'm saying is that you would count them twice, you would count them twice now, if you also report this metric on the agent span, on the agent operation.
Sergey Sergeev 00:21:38 No, no.
Liudmila Molkova 00:21:39 twice.
Sergey Sergeev 00:21:40 We don't have to report it from the agent.
Here, we need to report that attribute agent ID from each
So, if you have this attribute, for example, you are using OpenAI,
invocation, but you got, agent ID from the parent's pen.
Liudmila Molkova 00:22:00 You don't know the agent AD when you report this metric.
Sergey Sergeev 00:22:06 So, that's, the thing I, I, I think we are missing. Basically.
If you are writing instrumentation library for OpenAI,
You can check if you have, basically from the parent span, those attributes.
Liudmila Molkova 00:22:24 You, you cannot.
Sergey Sergeev 00:22:25 Again, this…
Liudmila Molkova 00:22:26 possible.
Sergey Sergeev 00:22:27 Maybe I'm missing something, but, yeah, I think I will need to create the pull request, and basically to provide, an idea on how to do it. Otherwise, yeah, we will have… if it's not possible, I don't…
I… I…
I need to double-check, because, Facebook, for example, is doing it, I think. But in general, if it's not possible from,
how to say, inference library, inference client library, we will need to emit this metric from the agent level.
Which will have all those attributes, but…
Then it will be a different metric type.
Liudmila Molkova 00:23:13 Maybe, I think Shipra and Aaron have their hands. Shipra was first, I think.
Sergey Sergeev 00:23:18 Pleased.
shiprajain 00:23:20 So, in traces, we already have, input usage, you know, we have these parameters as usage output tokens and usage input tokens, which is at the LLM span level, which currently captures each
LLM call, how many input and output tokens we have processed, right? Now, as Lutmila said, that, I mean, this can be a derived information, because we would know what all LLM calls have been made, and we can just do the back calculation.
When you talk about, reporting them as separate metric, I still don't understand the benefit of that…
I mean, one thing is we can technically do it or not. Another thing is, why would we want to do it?
Sergey Sergeev 00:24:01 Yeah, I can explain. So, plants usually capture,
Most of the information, you can derive additional metrics on the platform side, but from instrumentation side, it's helpful to report
lower than LHC metrics.
So, you don't need to do it on the platform side.
Hardik Surana 00:24:25 Another use case could be that if the same LLM call, like, you're calling the same provider and the same model, but the calls are coming from different agents.
you would want to know the breakdown of which agent is using more tokens than the other. So, in a multi-agent system, if all of them… if you're… as a user, if you're using only one provider and one model, but multiple agents are using it, you would want to know, like, how your application is getting
Set up in a way that is one agent overusing the context window in a flow?
Sergey Sergeev 00:25:06 Yeah.
shiprajain 00:25:09 Still, still, still not very clear, though, but yeah, I'll think about this thing.
Liudmila Molkova 00:25:14 It's not about the benefit, it's about the feasibility, what we can do, rather than what we… what's best.
Sergey Sergeev 00:25:22 Yeah, we can derive all the metrics from the span.
Liudmila Molkova 00:25:25 Not really. Spans are a sample. We cannot derive metrics from the spans. In the general case, we cannot rely on span attributes or parent span existence.
So, yeah.
Sujay Solomon 00:25:39 Erin, you want to go ahead?
Aaron Abbott 00:25:42 Yeah, I wanted to clarify the multi-agent thing, and clarify if that was in scope, because I think
In that case, it does,
I do see, you know, some value in it. We can't just look at, like, the hotel resource related to this metric. Yeah, I also wanted to plus one the sampling comment, like.
You know, or also if people don't want to capture PII. I mean, I guess that would not be PII. I think we don't require opt-in for the token counts anyway, but yeah, for… definitely for the sampling case. And then, Lumila, like, to your concern was the issue, like, the code doesn't know the agent?
when it's coming from the LLM layer, or was it more like a modeling question?
Liudmila Molkova 00:26:25 It's both. So, I can see how we can have a separate metric for the agent usage.
It would have agent-specific attributes.
And then, when you use one metric, you understand it's LLM, it's nested. When you use agents, you understand it's coming from agents.
the… Could they also add agent… sorry, agent name, not ID, on the… on the current token usage?
We could if we've found a way, but I think there are still two options. Different modeling or the propagation of some sort.
Sergey Sergeev 00:27:09 Yeah, my point would be, we should reuse the same method, if possible, just… if it's just attribute, and we still need to report duration and, token usage.
basically answering the customer's question, how many tokens my agent is using on average, what was the average duration, and so on, percentiles. So, I would propose to reuse the same metric, just,
if possible, just adding optional attributes for agent ID and agent name, so they should be.
Liudmila Molkova 00:27:46 Agent ID is high cardinality, though.
Sergey Sergeev 00:27:49 Is it, I've heard? It is.
Okay, we probably then need to standardize on the name.
Liudmila Molkova 00:27:58 Well, it might not be. Like, well, yeah, that's… that's a good point.
Sergey Sergeev 00:28:02 I can create a pull request, basically, with some example of this metrics, and just showing how to use it, and we can…
Liudmila Molkova 00:28:11 My main concern is that the feasibility, right? So if it doesn't make sense to define semantic conventions for something, that's not possible. So we should figure out how first before we decide what.
Sergey Sergeev 00:28:23 Okay, we'll share a PLC.
Of this telemet in the channel.
Maybe in a few days.
Liudmila Molkova 00:28:33 Awesome, thank you.
Aaron Abbott 00:28:34 Can I just share one more thought? Sorry.
Liudmila Molkova 00:28:36 Chorus.
Aaron Abbott 00:28:37 Yeah, so, like, if you… I'm kind of just digging through some other semantic conventions and trying to find ones that have something like this. I think, Lamil, you're very familiar with the URL.template in HTTP, right? So that one requires some kind of…
cooperation, or for the HTTP client to know something about the template, right? So, like, I think with that one's opt-in, so we'd almost definitely have to do something like that here, in case the agent name is not known, or somebody's not using an agent, right?
Liudmila Molkova 00:29:11 it could… the reason that the URL template opt-in is not because it's not… it's unknown, we could say it's conditionally required if available.
Aaron Abbott 00:29:21 Right.
Liudmila Molkova 00:29:21 Right, so, we can model it, for sure.
Aaron Abbott 00:29:29 Okay.
Sergey Sergeev 00:29:29 Another thing is something like a service name coming from HTTP layer,
To, basically metrics with, token duration and operation duration, so…
It can be an attribute in the metric coming from high-level framework, and we
can use it if it exists, so for agents, I think if agents share, basically, this agent ID, agent name, we can include it optionally to the metric.
And basically, just… it's definitely…
There is a demand for this, for sure.
It's more how we frame it, best.
Liudmila Molkova 00:30:22 Yeah, Shipra?
shiprajain 00:30:24 Not regarding this point, but I'm still stuck on one point that you mentioned, Lytmila, that from span, the attributes that we are maintaining, it is difficult to derive the value, because in our scenarios, usually, we would want to calculate information as performance throughput.
Latency, or, you know, cost-related details, which basically is,
calculated using the tokens, input and output tokens. And, one of the points internally came up that, we should not have any additional attribute to have these values, like throughput latency or cost, because that can be derived from the information that is already getting captured in these pans.
in terms of start and end date or duration, or, the token usage. So,
what can be the challenge in extracting this information that is already available? That was my basic question.
Liudmila Molkova 00:31:20 Yeah, I…
Sergey Sergeev 00:31:21 So if you…
Liudmila Molkova 00:31:21 And provided a good use case that it can be sampled, so you won't see all the…
Sergey Sergeev 00:31:27 All the spans and all the traces on the platform side, but you will see them all on instrumentation side.
alien case, and second,
Maybe they don't want to send the customer. The customer may be avoiding sending telemeting because of PII or something.
shiprajain 00:31:49 Yeah, okay, okay.
Sergey Sergeev 00:31:50 You can, still import instrumentation site metrics.
shiprajain 00:31:54 Hmm.
Okay.
Got it, yeah, thanks.
Liudmila Molkova 00:32:00 And last comment is, it's okay to use parent span information when you query data.
It's impossible to use it when… as you… inside the process when you report something.
It's possible, but it's hockey and unreliable, Shirky.
It's not in this pack.
Sergey Sergeev 00:32:20 Yeah, it's more in Gen AI space, you can expect agents as a thing. So, like, in HTTP, you can expect a service name.
Just it will be a very foundational concept. I think it may… may be worth to expect it.
Liudmila Molkova 00:32:46 Alright, let's move on to, to this, to the next question. Shipra, you have your hand raised, you still have some…
shiprajain 00:32:52 So I'll… no, no, no, I'll… yeah, thank you.
Liudmila Molkova 00:32:56 Yeah, thank you. Okay, so moving on, inference cost… so, sorry, on this one, Sergey, you would try something to prototype something.
Sergey Sergeev 00:33:07 The, action item, Sergei to share POC.
In Swag Channel.
And second, do we need to create a GitHub ticket? We were not really following this process.
And there's a one.
Liudmila Molkova 00:33:29 It's not necessary to have a ticket.
Sergey Sergeev 00:33:32 Okay.
Liudmila Molkova 00:33:34 Unless you want to raise your… contribution cost.
Okay, sorry, let's move on to the next topic.
Sergey Sergeev 00:33:43 Okay. And the inference cost metrics.
Yeah, I… think, that's… that was exactly my question, because I saw somewhere, at least,
Somebody reported an issue, but in general, cost metrics reported from the client side is helpful for some
people, we see it implemented in TraceLoop, so it would be great to define the cost usage… the usage… the cost of, tokens, again, reported from instrumentation site.
Liudmila Molkova 00:34:27 I… I'm not supportive. I… I think it's… it's wider than GenAI space, though. I think we need a… if you… I would suggest first to bring it up to the general semantic conventions, but what would people, I expect to tell you there?
That it's wonderful, it's awesome, we should have it, it needs a project.
It needs a group of people who would work on this from Gen AI, non-GenAI space together, cloud providers, and…
Well… the project proposal, there is a process around it, there are… there's staffing needed, it's…
There is a little bit of coordination, and it would be the… the group like this one.
That would… might meet weekly, might not meet, but would work on the operation costs.
Sergey Sergeev 00:35:22 Yeah,
It will be interesting to figure out how to move it, because it's a working thing for migrating
Today's whoop.
instrumentations to… When you open Telemetic project, they have this metric,
If we reduce the telemetry, it's just not so helpful.
For them, and… I would…
think about GAI operation cost, as a start, I don't know.
Alex.
Have a few authentic.
Alex Hall 00:36:00 Would it be helpful to try and create something that's more scoped, too?
JAI, like, rather than…
trying to capture all the possible costs of GenAI, which is more than just tokens. If there was something like a genai.token usage cost.
Sergey Sergeev 00:36:19 Yeah, yeah, it would be best, I think.
Alex Hall 00:36:22 That would not be something acceptable.
Liudmila Molkova 00:36:25 Yeah, I would argue against that, because if it's a general cost problem.
then it should be a general solution. And if we scroll problem down to GenAI,
It would never get stable.
Alex Hall 00:36:40 I'm just wondering if it's possible to, like, scope it down in a way that makes it less of a project for prototyping, essentially.
Liudmila Molkova 00:36:51 And you don't need a project to prototype, you can definitely experiment, but in order to put something into semantic conventions.
Alex Hall 00:36:59 And, well, I mean prototyping in semantic conventions, if we could, like, sort of…
Get something passed without a whole project.
Yeah, I don't know if that's a sensible way to try and… Move on this.
Liudmila Molkova 00:37:12 I mean, let's… Hawk,
I shared my opinion from semantic convention maintainer perspective, but I'm open to, accept other opinions. I would love to know what other semcon folks think. The great way to make progress would be to bring it up to the
Semantic Conventions, meeting.
Sergey, it's, it's 8 AM, Monday… Pacific time?
So, I… I could bring it up there, but I think it would be best represented if you bring it, or somebody who wants to work on this will bring it.
Sergey Sergeev 00:37:54 outright, or I'll find somebody… yeah, let's put the action item to… Provide, again,
I can create, probably… If you'll see it and share.
So, everybody can see the metric, and I would have to think how… It can be generalist.
And again, I'm thinking about quite important cost.
So, it may reduce…
Liudmila Molkova 00:38:26 the scope,
I think you should also check out this pull request, it's somewhat related.
Sergey Sergeev 00:38:35 Okay.
Liudmila Molkova 00:38:36 Not directly, but there is some intersection.
Sergey Sergeev 00:38:42 Sounds good.
Liudmila Molkova 00:38:48 Cool, moving on to the genie evaluation metrics.
Sergey Sergeev 00:38:53 Oh, who brought this issue? Me again.
Liudmila Molkova 00:38:56 I have no idea.
Sergey Sergeev 00:38:56 Okay, so, evaluation metric is for… again, we report evaluation result as an event, we have this,
pull request merged to semantic convention. Now it's, again, do we want to report instrumentation site evaluation metrics? And it's very similar to token usage and duration.
But we will include all kinds of analogy, things, like evaluation category, it can be an explicit metric name, or it can be an attribute on the same metric, there are pros and cons for it, but in general, you want to…
Answer the questions, customer questions. So, how is my agent doing, or service doing,
do I see some spikes in…
Quality or security reported evaluation metrics.
And this is… I wanted first to get an idea how we can
Approach this problem best, because we know
There is a demand for this.
How can we standardize on this, on it?
Alex Hall 00:40:18 Lilmila, can you zoom out?
Oh, sorry, it's me.
Liudmila Molkova 00:40:23 Domaine? Sure.
Alex Hall 00:40:24 No, no, no, no, no, no, somehow my own Zoom had zoomed. I don't know.
Liudmila Molkova 00:40:31 Okay.
Sergey Sergeev 00:40:39 So, just wanted to share feedback from this group.
Liudmila Molkova 00:40:45 It would be non-controversial if we… if somebody sent a PR and defined evaluation metrics, from… from the, evolution result event that they have, so essentially it's a projection of what we have there into metrics.
Sergey Sergeev 00:41:01 Sounds good.
Okay, oh, somebody… it's either me or somebody from,
Alex Hall 00:41:09 Great.
Sergey Sergeev 00:41:09 What kind of do it?
Alex Hall 00:41:11 What kind of metric is it?
Sergey Sergeev 00:41:13 So the value will be a score.
And, we will have attributes, label, like, positive, negative will be an attribute, and
Evaluation, name, It can be an attribute.
Or it can be metric, something like GenAI, evaluation.
Alex Hall 00:41:37 CCC… Is it a histogram metric?
Sergey Sergeev 00:41:41 Yeah, it can be histogrammetric, so you can see the percentiles, if you… Just monitoring your value.
Then it should be… Pearson there with it.
Liudmila Molkova 00:42:07 It wouldn't work for the metrics that have omni-label, right?
So, if you don't have a numeric score, and you only have label… Okay.
Sergey Sergeev 00:42:20 On a label, you can count, basically, on any, metric.
How many times you've seen one of those labels?
Liudmila Molkova 00:42:33 No, it won't be a histogram.
Sergey Sergeev 00:42:35 Histogram can be… so, histogram measurements report a number of measurements.
So, you can derive count from histogram as well.
Liudmila Molkova 00:42:47 I mean, how would… it's… we don't need to discuss it now, but if somebody would send a PR, they would need to explain how to report
things that don't have a score, right? Either they don't report this metric and report something else, or they report this metric, but then we need to figure out how to do it and document.
Sergey Sergeev 00:43:04 We talk, VR2 language transportability platform named SignalFlow, but I can probably translate to Prometheus.
And go find a queries,
We need a score because, again, different customers, may have different,
thresholds for alerting or for showing what is toxicity. You can imagine that a bank
AI agent, may have different threshold for toxicities and dating chatbot.
Over there, bye.
Okay, I think we have an action item for this. I don't want to take all the meeting time. Sorry for bringing in so many questions, and thank you for feedback. We have a few more items over there.
Liudmila Molkova 00:44:12 Oh, that's great, thank you for bringing it up.
Okay, moving on, Bruno, do you want to talk about auditing events?
Bruno Baptista (IBM) 00:44:23 Hey, Haldmila and everyone. Yes, so we have the opposite problem, so we actually have a prototype for this in Quarkus.
And… we… I was thinking, okay, we need to move these eventually to Langchain 4J.
But what if these events are useful for,
the community in general. So, the idea behind these auditing events is the ability to
Reconstruct the request at a later date, and recompute scores and see if there were any changes.
So we have auditing events for message created, interaction complete. I would say that this is very similar to the,
to the semantic… to the evaluation result that was standardized. So, we have direction failed, response from LLM received might be something else. Tools executed, guardrails executed.
and a few others. So…
What I wanted to ask you guys is if this is interesting, or if this conflicts with some other work that is ongoing.
Liudmila Molkova 00:45:49 Can you help me understand a little bit more? What is it? So, it's not… it's not… it doesn't look like it's similar to the evaluation. It seems like you have a means to describe,
Detailed communication with the model.
Bruno Baptista (IBM) 00:46:06 Correct. Basically, on the moment that we invoke things, we can… we can fire events with the details of the request.
And we can actually reconstruct that request later.
Liudmila Molkova 00:46:19 Yeah, so what we have today, that is kind of similar to what you're describing.
Is… we have…
Let's check, we have Operation Detail Event.
It…
Bruno Baptista (IBM) 00:46:41 Okay.
Liudmila Molkova 00:46:41 covers… it's actually the same as the LLM span.
It covers, known input parameters.
Bruno Baptista (IBM) 00:46:51 None output, the response things, and chat history.
Liudmila Molkova 00:46:56 So it's not… it does not intend to capture absolutely everything, right? It captures some… some things that we consider important from semantic conventions.
Which is not complete today, but there is no goal to capture exactly what happened. And it's one event upon completion.
Bruno Baptista (IBM) 00:47:19 Okay, do you think this could be just a single event with, standard fields that we can, use for everything?
Or… A more rich feature of events would be more appropriate.
Liudmila Molkova 00:47:39 It depends, right? So, like, we discussed in the past that, for example, if there is a streaming response, then maybe, in some cases, we would consider event per chunk.
Right? It's extreme… it could be extremely verbose.
So if, if, like, it's, it's how much granularity Do your needs.
Yeah.
Bruno Baptista (IBM) 00:48:08 Okay, so, like, like in the other cases, probably the best is to propose something and see what happens.
Liudmila Molkova 00:48:19 Probably, but if you want to, like, maybe, come again and give us maybe 10 minutes demo on what you're thinking, how you're thinking to use it.
it would be easier, because then, if you just send something on the GitHub, then very few people tend to look at it, and it tends to.
Bruno Baptista (IBM) 00:48:40 Okay.
Liudmila Molkova 00:48:40 Quite a lot of time to get to any conclusion.
Bruno Baptista (IBM) 00:48:45 Okay, so, we have a colleague that is preparing a demo about this, and it will be ready very soon.
So I… once ready, I'll invite him to come here and show us what he has in mind.
Liudmila Molkova 00:49:04 That would be wonderful.
Bruno Baptista (IBM) 00:49:07 Okay. Thanks very much.
Liudmila Molkova 00:49:10 Thank you.
Thanks. It seems Samuel needed to drop. Samuel, you're not… you're right.
Okay, so… Well, let's put it in the next topics.
And let's move on.
So, someone, from,
CNCF reached out, and they're going to have some presentation on status of AI, in CNCF.
Alex Hall 00:50:01 Can I just check? Oh, go ahead. I mean, I know what Simon was asking about.
Yeah. It was that general cost thing that we were talking about.
Liudmila Molkova 00:50:09 Right, okay.
Alex Hall 00:50:10 Is… is there any guideline
Okay, it's very common practice when you're dealing with money to not just use floats, which have precision problems, but to use, like, the high-precision decimals or something.
Is there any such practice like that in OpenTelemetry?
It just feels like with telemetry, you might want to not be quite so strict, you're not dealing with, like, actual financial transaction logic, you're just trying to monitor how much things cost.
Is there any precedent for either doing or not doing that in OpenTelemetry, of, like, maybe recording the attribute as a string to preserve precision?
Liudmila Molkova 00:50:50 OpenTelemetry doesn't have floats, it only supports doubles.
Alex Hall 00:50:53 Right, but that's what I mean. Either way, you still get these, like… potential weirdness. Does it matter?
Would it make sense to be recording this as a string and let the backend deal with the converting to a number?
Aaron Abbott 00:51:10 Create New York Devil's guide, if possible.
Alex Hall 00:51:12 Sorry.
Aaron Abbott 00:51:13 Sorry, I was gonna say we have int also, right? If I'm remembering correctly.
Liudmila Molkova 00:51:18 Oh, right, yes.
Alex Hall 00:51:18 True.
Aaron Abbott 00:51:21 Let me double check, though.
Liudmila Molkova 00:51:28 So, Alex, you're saying that double precision is not enough?
Alex Hall 00:51:34 I imagine it almost certainly is, except maybe someone will come in and complain and say, hey, this is money, you're gonna end up with, like.
Aaron Abbott 00:51:42 Yeah. 0.30001.
Alex Hall 00:51:46 kind of errors.
You shouldn't be using dollars or floats for this.
Liudmila Molkova 00:51:53 And if it's a metric, it would be very hard not to use numbers, though.
Alex Hall 00:51:57 If it was the span attribute?
Liudmila Molkova 00:52:00 If it's a spend attribute, then it's possible, but it should be translatable to a metric, right? But people would look at this
As a number.
Alex Hall 00:52:12 Yeah, in this context, we were actually thinking about a span attribute.
Aaron Abbott 00:52:18 Yeah, I think we have int onspit for attributes as well, right, Ludmola?
Alex Hall 00:52:23 Yeah, so… But I mean, you know, assuming it's, like, something that is easily factional, especially because
In Gen AI, costs are often less than 1 cent.
Liudmila Molkova 00:52:39 So, since you are aggregating in metrics, the measurement
If you're measuring something, it has to be in double.
Right, it cannot be not enough… it cannot be a string. You cannot aggregate over strings, you cannot sum strings.
Alex Hall 00:53:01 Yeah, so this actually differs a little bit from the previous
version of this topic in this call, and then here we're actually thinking about a span attributes.
Sergey Sergeev 00:53:12 And pardon my ignorance, double is in what, is it protobuf, type, or…
Alex Hall 00:53:21 It's a private bathroom.
Liudmila Molkova 00:53:22 IPSC.
Sergey Sergeev 00:53:23 And, which value it may represent the world's value.
Liudmila Molkova 00:53:29 Think… 10… Power minus, sorry.
Alex Hall 00:53:35 This is a 16th digit rate.
Liudmila Molkova 00:53:37 Or a 15th or 16th digit is the double precision.
Sergey Sergeev 00:53:41 I think it should… it should… it should work for the cost.
Yeah, I think, later on proxy, for example, they report cost, and I didn't see any problem just from the.
Alex Hall 00:53:55 Thanks, like, an hour.
I just wanted to check if, like, anyone feels that, oh, position should be preserved, it should be a string.
If people generally feel like double is good enough.
Aaron Abbott 00:54:08 I mean, if you're…
Alex Hall 00:54:08 doing that.
Aaron Abbott 00:54:10 If you're not doing math, right, then the rounding errors are a separate thing, so if you can represent the number
without losing precision as a double, I guess it would be okay, but…
And you're saying, like, it could be fractional, so cents wouldn't work, you'd have to choose some arbitrary, like, point if you were going to use int?
Alex Hall 00:54:31 Yeah, I think Int would make it hard.
Aaron Abbott 00:54:34 Yeah, I mean, I…
this problem obviously exists in JavaScript a lot if you want 64-bit doubles also, so, like.
Or 64-bit int, so I would maybe check with them. I don't know. I think they use bigInt kind of thing, some bigInt kind of thing in JavaScript for most of the…
that they have that problem, but, you know, traditionally you would do, like, string for an integer in JavaScript to get around this.
Alex Hall 00:55:01 Okay.
It's fine, I don't want to stand this.
Liudmila Molkova 00:55:18 So I… I just keep my hopes up that double precision is enough, or the… whatever the, pricing model people use.
It should work somehow for… for their cloud bills.
But if not, it's actually a big problem. There is no solution for it, not in telemetry, if double precision is not enough. We might scale it up.
So that, it's, it's some weird unit.
Not a cent, not a dollar, right, but something else that would…
Allow us for… to… to make double work.
If it's a string attribute on a span, like, how would you use it? How would you write a query that sums them up?
You would parse it into double, and then you already… I have a problem.
Alex Hall 00:56:12 Some databases support decimals, but…
Tomorrow.
That's all, thank you.
Liudmila Molkova 00:56:24 Yeah, thank you.
Okay, moving on to the status update. I've started sharing that, somebody from CNCF reached out, asking for this. I summarized the
what I think we have and we don't have, and the problems we have here in this document, I wanted to get your folks' eye on this, because if I forgot some company, it's absolutely unintentional if I lied here in some other
place. It's also not intentional, and I probably just mistaken. So if, if you want to take a look, please go ahead. Essentially, what I am saying, that we have LLM calls, the basics.
As something we have.
We have some instrumentation libraries.
Some native instrumentations here and there.
We have conventions and instrumentations for agents and frameworks that are somewhat in progress.
We have two definitions and evaluation results. I list them as in progress. I guess first we didn't merge all of the PRs yet. Second, it's not released.
Third, we're still discussing some aspects of this.
OR.
So we don't have multi-edit orchestration, multimodal content, all this stuff.
We, sometimes hear that people are interested in internals for the model, key-value caches, fine-tuning, GPU, whatnot, none of it is, is here.
And, the vector and databases and semantic convention… sorry, semantic search is not… Here, yet.
And the challenge, Ali, is that there is no convergence, right? So there are tons of different instrumentation libraries with different level of support for semantic conventions, and sometimes open telemetry itself.
And I don't believe we are…
We can say that, there is a standard. We are working on the standard.
the other part that I'm bringing is that, it… the semantic conventions are not a great place to make quick progress on the bleeding edge, right? We are…
Somewhat intentionally, slow, because we want to… we are focused on the long-term stabilization.
And… this paragraph, this sentence, I'm particularly
cautious about. I'm listing some companies that are open to long-term work, and I know there are a lot of you folks here who also work on this.
So, I… I also want to put,
Pidentic AI here, or anybody else who I forgot to put. Again, it's not intentional.
So maybe I'll do this.
So again, please take a look, if you feel I'm, I'm, I'm not being honest, correct me.
Sergey Sergeev 00:59:49 I think TraceHoop's involvement early in this group was really big as well. Probably we can mention Trace Hoop.
I don't know.
Because NEAR is working with different groups in different ways.
Aaron Abbott 01:00:09 Unmal, is the goal to capture here, like, which parties are interested in standardization?
Or are actually, like, adopting the standard, or is it… To just capture the involvement.
Liudmila Molkova 01:00:23 Good question. Maybe we should remove… Pretty specific names at all?
Because the goal is to… provide…
some visibility into the challenges, right? I… From my discussions was the…
this person, you probably have seen this. There were very short
That it seems there are some common challenges across the industry.
And it might be interesting in…
who and which companies are participating, but I think we would be better.
as this.
Aaron Abbott 01:01:08 Yeah, or…
Liudmila Molkova 01:01:09 I don't need this,
Aaron Abbott 01:01:11 Yeah, yeah.
I mean, I think that is the biggest… Challenges like the, you know.
how do we chase all these conventions down? But…
Yeah, this seems fine. I guess the alternative would be people, like, volunteering their companies.
Instead of trying to, guess what their plans are, or something like that, but…
Yeah, we can… we can just leave discussing comments, I guess.
Liudmila Molkova 01:01:40 Yeah, it's a great call-out, thank you.
Okay, and the last point, the opportunities, it's essentially where we would love some help.
That's what I listed,
And I'm definitely interested in what you think.
So, I'm saying we want instrumentations, and especially, not just the instrumentations, but the longer-term ownership for those instrumentations and up in telemetry, or,
If people can upstream this to their libraries themselves, that would also be wonderful.
The other thing is the review in general. I feel we have a lot of, initiatives to…
Work on features, but we actually struggle with the discussions and finding common grounds.
I would love more people to participate in the discussions and provide feedback.
And, then I'm calling out the agentic scenarios. We, I'm, I'm saying that it would be nice to have somebody who is experienced implementing different,
Flows with different technologies, and essentially their feedback on what they have, or maybe, if they see some gaps, and they can share this.
Great.
We are at time.
If you have any comments about this document, Please share them.
It's open for comments, sharing, and everything.
And we didn't get to the PR review.
Let's take it offline. There are 3 APRs that Would love your attention.
Pavan 01:03:49 Just one comment, I think, before we close. So, 2594, due to inactivity, it's been marked as, you know, stale, I think, and it's probably meant for deletion. I'm just thinking if we can keep that open for just a little more
Time, until we can discuss and maybe…
Liudmila Molkova 01:04:10 Sure.
Pavan 01:04:11 Yeah, thank you.
Liudmila Molkova 01:04:12 You can always keep it alive by leaving a comment or something.
Pavan 01:04:17 Okay, okay.
Liudmila Molkova 01:04:18 Yeah, thank you for bringing it up. Yeah, Tristan?
Tristan Sloughter 01:04:21 Yeah, quick question. Is there… there doesn't seem to be a Slack channel specific to Gen AI, LLM stuff?
Is that the case?
Liudmila Molkova 01:04:29 There is one!
Tristan Sloughter 01:04:30 Oh. Yup.
Aaron Abbott 01:04:31 What is it?
Liudmila Molkova 01:04:33 tag you there.
Tristan Sloughter 01:04:34 Okay, thank you.
Aaron Abbott 01:04:35 It's in the dock as well.
Tristan Sloughter 01:04:36 Oh, okay, yeah.
Alex Hall 01:04:38 I have Gen AI in the name.
Liudmila Molkova 01:04:45 Are you unmuted? Anyway, good to see y'all.
Thank you for the great description.
Pavan 01:04:50 Thank you.
Liudmila Molkova 01:04:51 And… goodbye!
Pavan 01:04:54 Bye.
