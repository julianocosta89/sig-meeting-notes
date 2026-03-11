SIG: LLM Semantic Convention WG
Date: 2026-03-10
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

Sergey Sergeev 00:01:28 Hey, everybody.
Liudmila Molkova 00:01:46 Well, hello. Hi, everyone.
How are you today?
Surya Teja 00:01:55 Hello folks, I'm doing great. How are you? How is everyone?
Liudmila Molkova 00:02:00 Oh, I'm doing good.
Thanks for asking.
Somebody is modifying the agenda. Thank you.
I am going to start sharing. Does anybody else want us to drive the call? I wouldn't mind somebody else driving?
Sergey Sergeev 00:02:18 No, no, no, sorry, I just started to copy it, yeah, please, take over.
Liudmila Molkova 00:02:25 No worries at all, I appreciate it.
And if somebody is interested in driving the call, this would also be much appreciated.
Okay, so let's see what we have. There was some topics yesterday in the Gentic track.
Would it be interesting to… if… if we,
if you folks summarized what happened, there, maybe just a few minutes, a few things that you discussed, would it be helpful? Like, if not, it's okay.
Sergey Sergeev 00:03:03 Yeah, in general, just a few questions, were brought up, by Victor. I don't see if he's joining today or not. Sometimes it feels that, some folks just join in on Monday.
We have general topics, we try to… I'm trying to collect…
the questions, and just to redirect to Tuesday, so one question was about OCSF, and…
OpenClemmetry convergence, so, the request to Victor was to summarize and to show some examples, basically.
How it can be…
how it can be, expressed in OpenCLEM at the… schema, and…
just shared, not commerce, security… Proposal.
for guardrails, so, no immediate outcome, and second was a proposal which I'm yet,
by, by Wolf Gunn, so there is an issue.
And, so, he will review the existing GenAI semantics, and will circle back if anything is actionable.
From this pull request.
And I had, basically an open question about,
agent interrupts and commands. I'm still cleaning up the proposal, so… Not actionable.
Liudmila Molkova 00:04:46 Awesome, thank you.
Sergey Sergeev 00:04:47 If we will have, some…
some time left today, I may be about to just…
to ask physical questions I have.
related to hygienic… Interrupt and, commands to resume.
Liudmila Molkova 00:05:07 Awesome.
Well, let's try. Thanks for the update.
So, people are still joining, like, let's take a look at the board.
New issues… This is the old one, we're still…
Not clear what to do with it… How to capture user information.
Oh, okay, we're… Talked about this.
Okay, Aaron was asking… yes.
It is allowed. I…
I hope we can build something that would support both some combination of user and session.
It would not be specific to… Either… of them.
And… I think there were some prototypes in Python.
But, M… I'm blanking now.
But yeah, so we need to solve this in one way or another, so I'm going to put it to…
Kidoo?
That is probably Python.
Tested with monarch dependencies.
Aaron, can you talk a bit about this?
Aaron Abbott 00:06:59 yeah, I can… I can mention it. So, so basically we have, like,
You know, we have this monorepo.
But we have independent releases.
And that kind of creates some friction, because there's…
There's, like, dependencies within the model repo that need to be released in order.
Which means that if you, like, update UtiligenAI and you want to use it in an instrumentation right away.
It means that the tests need to pull from the model repo instead of, like, the max deployed version.
So, so basically, it's just calling out that friction and saying a couple ways we could work on it.
And one option is to just deploy all the GenAI packages
Like, in lockstep at the same time, and not worry about the independent release stuff so much.
Liudmila Molkova 00:07:49 Yeah, I think this would be easier for everyone, right? Because, like, deploying them one by one rarely happens, and if I deploy them on a regular basis.
Together, it would make sense.
Aaron Abbott 00:08:03 Yeah, I mean, we have been deploying
them separately, actually, a little bit. If you look at the… we don't have to look, but if you look at the release history, you can see it.
But say we… say we published it, like, once a week.
With some automation, then we probably wouldn't need that.
Could probably just release them all at once.
Liudmila Molkova 00:08:23 Did we actually publish them frequently enough? Like, more frequently than the whole report?
Aaron Abbott 00:08:30 Yeah, I don't remember if they show up in these releases.
Excuse me.
You keep going, yeah.
Is that one…
Liudmila Molkova 00:08:43 Yeah.
Aaron Abbott 00:08:45 So, I think if we did release them all, like, once a week, it would probably be a faster overall cadence, but it's not…
Oh.
Liudmila Molkova 00:08:54 Do we need to, though? Like, can we just release… like, can we do this? Can we release them on monthly cadence?
But have an ability, if you absolutely need, to release independent package as well.
Like, if we release them together with the rest of the world, why wouldn't we?
Aaron Abbott 00:09:14 Well, I mean, I think we could do that, but if we keep the independent option, then we still have this, like, dependency order issue.
Liudmila Molkova 00:09:22 Yeah, but then it's an ad hoc process that you need to rarely need to do at all.
Aaron Abbott 00:09:29 Yeah, I mean, I think I'm open to it. We can,
Maybe trouble coming in the issue, Luna?
Liudmila Molkova 00:09:36 Yeah.
Okay, but that's, that's a good… Oh, I'm…
So we talked about… The need to define and document Configuration options.
We have a great opportunity to do it formally in the configuration repo.
If anybody is interested in looking into this and, like, taking what we have, and creating a formal
configuration here. Like, it already contains Genia Instrumentation config, and it currently only supports this opt-in into latest experimental conventions. So we could evolve it.
And we could then document it.
Before or after. We can document it informally in Markdown.
At Trusk?
So you turned your camera on?
Trask Stalnaker 00:11:47 Just here, I'm here.
Liudmila Molkova 00:11:50 Hi.
Trask Stalnaker 00:11:52 No comment.
Liudmila Molkova 00:11:54 Okay.
So, I will… Well, what to do? We talked about it before, it would be important,
Would anybody be interested? Would anybody volunteer?
neil yashinsky 00:12:15 Hi, Ludimila, I just got here, I, so it's classic me for, like, oh, I'll volunteer for a task I haven't even heard any more of, but I'm happy to look at this one, it sounds like,
it was… it's open, no one's looking at it right now. I can at least take a first shot at it. I think there's one or two other things I've, kind of been,
What's the word I'm looking for? Yeah, N-E-I-L dash…
N? Probably find me. Neil… oh, I'm sorry, Neil the.
Yeah.
Liudmila Molkova 00:12:48 Neil?
neil yashinsky 00:12:51 Yeah, we need a dash, sorry. Dash. T-H-E?
Hmm.
I might not be in your preview. I'll send you a quick message, you'll have it.
Liudmila Molkova 00:13:03 Sure.
Awesome.
neil yashinsky 00:13:05 Thanks.
Liudmila Molkova 00:13:05 Thank you.
Okay, let's move on. Does anybody… is anybody new to this group, and you want to introduce yourself?
Eugene 00:13:23 I guess I'll introduce myself. My name's Eugene. This is my first time here. I'm an independent researcher, and I'm just getting interested in, kind of, LLM observability.
Liudmila Molkova 00:13:33 Awesome. Great to have you here.
neil yashinsky 00:13:37 Yeah, welcome over.
I'm sure we'll be better off with your contributions.
Liudmila Molkova 00:13:46 Anybody else?
Erdenesaikhan Tserendavga 00:13:49 Yeah, I couldn't introduce myself.
My name is Erton, I'm working for by Cisco Splunk with,
All of the teammates in this meeting with Sergey, Josh K, Chuning, and Ritima.
It's my first meeting here. Thank you.
Liudmila Molkova 00:14:09 Great to have you.
neil yashinsky 00:14:11 Yeah, hello and welcome.
Liudmila Molkova 00:14:17 Okay, so then… Moving on to the agenda.
Ankit and Trask.
How to document… R.
severity and error message in Gen AI evaluation, and then, oh, I love it.
Troscoric.
Anki, do you want to talk about it?
Trask Stalnaker 00:14:49 Yeah, sorry, it helps to be mute off.
The… yeah, so this came up, we're trying to implement the evaluation result event, and so there was just some…
Questions that arose around… Specifically around how to capture errors.
From when an evaluation Fails.
And…
I know kind of the answer, because I'm in the event SIG that's trying to answer those questions.
But I was wondering… And definitely we can talk about this in the event, so you also…
But how… whether we should include some language in the events themselves.
For people reading those, kind of, some generic stuff, pointers… To help answer that question.
Since people won't really know to… where to go in these semantic conventions to… Get those answers.
Liudmila Molkova 00:16:14 I'm thinking maybe…
we made a mistake adding error type here. Maybe this event should always be the result of successful evaluation.
It means that the revelation has happened.
And then the exception is just a separate thing, it does not report the result of evaluation.
Trask Stalnaker 00:16:47 I agree, but still…
it's still… I mean, I… nice from an event, like, I'm thinking, like, you want to generate metrics for that, you want to gen… you want to…
Like, it is… Why… why wouldn't we capture errors?
Liudmila Molkova 00:17:11 There are two parts of evaluation, the process of evaluation, right, and the result.
And let's say, Company A runs the evaluations, but reports evaluation results to the original caller. So you use SAS to do evaluations.
And then the evaluation result belongs to you. The process of evaluation is essentially.
Trask Stalnaker 00:17:35 Oh…
Liudmila Molkova 00:17:36 the, the wood… And then you don't care if they failed, you only care about the result.
Like, you cannot build metric from this, because…
It wouldn't show you the result.
Trask Stalnaker 00:17:55 Got it, and that's why it's an event and not a span, because it's not actually representing the evaluation process.
Liudmila Molkova 00:18:02 Yeah, we've been, like, bike-shedding on it, and we decided to go with event because it makes sense regardless, but we've also been thinking, like, it could, like, if you own this infrastructure, you could potentially put the evaluation result as an attribute on spends as well, we just didn't…
capture the… But it's a possibility.
Sergey Sergeev 00:18:27 Yeah, the challenge with it, so, when you have application telemetry, let's say you have LOM span, and you sample it for evaluation somehow.
So, typically, you don't want to stop that span from being processed.
In your pipeline, because evaluations are asynchronous and take time.
So, if you sample that span for evaluation,
And again, you don't want to create an evaluation span on the same trace of your application, because this way you kind of add in telemet
to the application trace, somehow you will see a new span which doesn't belong to the application.
So this is why, WOG went, with, that span ID and trace ID, for correlation.
Was decided as a better approach,
what you can indicate on the span, and this is what we do on the Splunk side, so we put an attribute that this span was sampled
for evaluation.
This way, you can see, from the span side, okay, the span was,
In queue for evaluation or whatever, but, probably…
Something failed, you never… you can never see it, evolutionary result. Great.
Yeah, it can… probably DM you on Swark if you're interested in more details about it.
Trask Stalnaker 00:20:15 Yeah, so then you…
When do you capture the… where… so you mark the span that it was in queued for evaluation,
When do you… when and where do you capture the event?
Sergey Sergeev 00:20:34 Yeah, so the event is produced by evaluator, and if it's instrumentation site evaluations, basically, when you evaluate something in application or in instrumentation.
What we do. Then you can…
You basically eventually should produce that evolutionary result with either success or fail.
But, there is a potential that it can be dropped, and etc.
If it's platform-side, so this is internal implementation of your platform, how you monitor it, and so on.
Trask Stalnaker 00:21:15 I see, so potentially this is…
Similar to where we may have a split of client and server… instrumentations where… If you are…
Instrumenting the platform, the evaluation itself, then you might want to capture that as a span.
Okay, that gives me more stuff to think about. Thank you for all the context.
Liudmila Molkova 00:21:47 Yeah, I think the beauty of the event is that regardless of how you
do the process of ovulation, you can have the same event.
Sergey Sergeev 00:22:01 Yeah, and one use case, so application developers, some application developers will insist on doing application-side evaluation. Basically, they will, run their own LLM calls on their own… with their own business logic, so…
And then the question, if they're using some monitoring solution, how can they communicate
You… basically, there's evolutionary result, so you can turn it into metic, or whatever, or correlate with the trace.
So this is, also a helpful concept.
Bismo.
Trask Stalnaker 00:22:42 And, are you able to tie that to the, like, the agent span, the agent trace?
Sergey Sergeev 00:22:53 Yeah, if you switch back to that definition, I think it should capture the context, the trace and span context.
Liudmila Molkova 00:23:03 Yeah, so the idea is to parent it, but again, there's, like… I think in the discussion before, we thought that maybe it should be linked
well, we cannot link an event. But essentially, there should be some way to establish correlation. Maybe the evaluation process should link to the original thing it is evaluating, if it knows the context. But I think it's not always possible.
So we are correlating with the response ID.
But I think if we talk about agent, it's not applicable, but then the
either the conversation AD is applicable, or something else about that specific A run.
Sergey Sergeev 00:23:46 Yeah, interior is just including,
trace ID and span ID as an optional.
Tables here may solve the problem.
Liudmila Molkova 00:24:01 It's included, right? It's just… they are not… as a parent, it's just not always available, because you… if you run an application, right, you… you already… the span has already finished, you don't know its context.
Sergey Sergeev 00:24:15 Yeah, yeah, yeah.
Trask Stalnaker 00:24:21 Cool, thank you. I think that gives me enough to follow up on, and I'll, potentially make…
Proposal about, like, what you were mentioning about that it's not errors, it's only successes.
Something like that.
Liudmila Molkova 00:24:45 Cool, thank you. Thanks for bringing it up.
And you're both still on stage for the Invoke Agent Span?
Trask Stalnaker 00:24:53 Yeah.
Yeah, if you scroll down, just wanted confirmation about one…
request there. I was interpreting what you were asking, and if you can just confirm this is what you meant.
Liudmila Molkova 00:25:21 I meant… that I think last time we discussed that we don't need to
Extend client attributes on the server span.
even if it's the invoke agent client, right? We don't extend HTTP client on HTTP server, because they
inherently, they have something in common, but not much. So I was thinking that we can just…
Have a full list of urgent server attributes, and not extend any group at all.
Trask Stalnaker 00:25:57 Isn't that what, this is doing, though? Extend attributes, gen AI common… oh, it still says .client.
Right.
Okay.
Do we… and we don't have a… common… Without the dot client.
Liudmila Molkova 00:26:19 I don't think… yeah, we don't have common with that. It's the first…
Well, maybe second server thing that we have.
Trask Stalnaker 00:26:29 Okay, okay.
Liudmila Molkova 00:26:32 Did Ankit… it's, maybe Ankit already did it?
Trask Stalnaker 00:26:37 He did what I recommended, what I thought you were suggesting.
Liudmila Molkova 00:26:41 Sorry.
Trask Stalnaker 00:26:42 Yeah, yeah. So, to…
Extend the common, basically to break it from inference.
So, it does one of those two things. It breaks it from inference, but not from client.
Liudmila Molkova 00:27:02 Yeah.
Trask Stalnaker 00:27:04 And I have my other… the other PR. I mean, I'm happy to continue making progress on splitting those things out, I just need another approval to merge my PR
Here, and then I can follow. Then, once we have this, then we can… Split out.
Invoke agent client. I guess, though, this still extends… the common.client, I think.
and common.client, yeah.
Which is…
Liudmila Molkova 00:27:47 English.
Trask Stalnaker 00:27:47 Okay, for this… PR, because there's no server
Invoke Agent Server, but… yeah, we'll…
Liudmila Molkova 00:27:58 And this makes… it even makes sense between embeddings and inference, so, like…
That seems fine, but it's not fine for server, because it has server address and server port.
Trask Stalnaker 00:28:12 Right.
Okay, I understand now.
Liudmila Molkova 00:28:17 Sorry for the confusion.
Trask Stalnaker 00:28:18 worries.
Liudmila Molkova 00:28:23 Cool.
Anything else on the server? I'm sorry, I didn't see your comments yesterday.
Trask Stalnaker 00:28:33 No, no. I think that… That was the only… Question I had.
Liudmila Molkova 00:28:44 Okay, thing can't get addressed my comments. I'll take another look, thanks. And,
Aaron, I think you raised this issue about separating agent and inference.
Would you be interested in reviewing the PR that does it?
Trask Stalnaker 00:29:04 I already think…
Liudmila Molkova 00:29:05 Yeah, yeah.
Trask Stalnaker 00:29:06 about it.
Aaron Abbott 00:29:07 Yeah, I just haven't had a look yet, but I'm interested.
Trask Stalnaker 00:29:10 Thank you.
Liudmila Molkova 00:29:12 I think so, like… Cool. Then moving on to the next topic?
Now Kumar, do you want to talk about memory?
Sergey Sergeev 00:29:23 Do you mind if I quickly ask one more question?
Liudmila Molkova 00:29:27 No, no, of course, go ahead.
Sergey Sergeev 00:29:28 the Invoke agent server site, so…
Is the change mostly to highlight that,
Invoke agent on the server side can provide richer telemetry than the coin side.
And hide the complexity of all the inference and etc, and basically to return
Something like token usage, and etc.
It is so that… .
Trask Stalnaker 00:29:57 The server span can still have nested spans…
itself of further inference and other things, and so it gives it a parent. It allows the context to sort of propagate
From client to server, and then down to… further…
Inference and agent… client invoke agent calls.
I don't feel like I didn't answer your question.
Sergey Sergeev 00:30:28 No. Yeah, I mean, it's,
Yeah, maybe I will take a 2.3.
Trask Stalnaker 00:30:37 No, no, it's…
Sergey Sergeev 00:30:38 If you have…
Trask Stalnaker 00:30:40 I would love to understand your… I…
I'm sure you probably know a lot more about it than I do, so it will help me to understand.
Liudmila Molkova 00:30:52 To my understanding that the client, in this case, just invokes the agent, and the whole agent invocation happens on the server.
And then all of the logic that happens on the server, like.
doing specific conference calls, tool calls, and everything. Unless server is instrumented, the client has no idea how
The server came up with the SouthClam.
Sergey Sergeev 00:31:16 Yeah, and this plan will capture some… those details, and this will be the difference from the coins, right?
Because as a client invoke agent… oh, go ahead, Taryn.
Aaron Abbott 00:31:31 Sorry, yeah, I was just gonna say something about the tokens, but I can wait until you're done.
Trask Stalnaker 00:31:40 Kind of relates, I think, to what you were saying about the, the evaluation
Pieces where if you do… if you are instrumenting the platform.
Then you can capture more pieces, and…
If you are… You can… Then capture the end-to-end
Trace with a lot more details of what's happening.
Or, or if you're running the agent.
Like, a user's agent is deployed in… Platform.
And this making agent-to-agent calls, then you can capture that full Trace.
Sergey Sergeev 00:32:39 Unfortunately.
Trask Stalnaker 00:32:40 I can't.
Sergey Sergeev 00:32:41 What about tokens?
Trask Stalnaker 00:32:45 So in the… In the…
Split out, let's see, what did… Invoke… agent… didn't…
I think it was on my PR, Ludmila… .
Liudmila Molkova 00:33:15 Dawkins?
Trask Stalnaker 00:33:18 Yeah, the invoke… when… oh, when I split the invoke agent… From the inference attribute hierarchy
Yeah, you had left, Comment.
If you just go to the discussion at the main page on the PR.
Yeah, that… It would be the sum of all the tokens.
If you do capture it.
at the invoke. So the invoke agent, when it's an internal… so it's kind of similar, the invoke agent…
Spans can be either client spans or internal spans, when they represent the, like, frameworks that run locally.
And I… the server invoke agent spans, to me, feel basically the same as the internal.
Invoke agent spans, because they represent something that's running and has nested pieces.
If you go to the issue, maybe you can… let me share the research that I had done on the issue there.
Liudmila Molkova 00:34:57 Oh, yeah.
Trask Stalnaker 00:35:09 So, I had split it into… there's two comments here. Part one is internal spans.
When I was looking at the invoke agent spans, the… there were very different, sort of,
frameworks, implementations, APIs for them, whether it was internal or client, so I split that out, and then kind of mapped what the different attributes
Map to for those.
So, if you scroll up to the internal spans is probably the more interesting here, related to the server spans.
Where… Like, OpenAI, agent does expose the input tokens and output tokens.
It internally sums them up and gives you that back, so you can capture that.
Aaron Abbott 00:36:18 Yeah, so I… I, I…
I'm a little nervous about, sorry. I'm a little nervous about summarizing these counts, and I don't…
know if there's, like, a good way around it, but, at least what we do in some of our UIs that we built on semantic conventions at GCP is we…
We basically just sum across these kind of stupidly.
And we can calculate, like, the entire invocation token usage. So it's kind of like in metrics, like, you know, it's nice if doing a sum
Is correct and doesn't have any double counting, but…
I can see how these would be useful from, like, a UI perspective.
Liudmila Molkova 00:37:01 I wonder if we should, like, our UIs, I think every UI does it, and I think Alex raised it in the past, that it's kind of hard to separate
on the aggregated from the LLM, so maybe we can
The UI should understand if it's reported on an LLM call, on the, like, leave call.
Aaron Abbott 00:37:21 Done.
Liudmila Molkova 00:37:22 you should count it. On the agent, if agent call agent, Then, like, you…
You cannot separate, you don't know if you are aggregated or aggregated, aggregated, and how many turtles are down there.
Sergey Sergeev 00:37:40 Yeah, to me, it makes sense when we make a call to an agent, which is server-side, and which hides the complexity, so basically, you will see just one invoke agent spend, so it hides all the complexity of the internal
calls and et cetera, but it will produce you some aggregated view on token usage, on the cost, how many tools were called, was it successful or not, then we can use
The server side,
Span, but if you provide more detailed spans, child spans, then you should not probably do the segregates.
And… Probably we can, document it clearly, so if you…
provide all the way to LM invocation, or to invocation spends.
Then I will use aggregated fields on the agent. If you hide that complexity as a provider, you don't want to expose how it worked, you just…
Received a request, you did something, you responded, then you can provide those optional aggregate, counters.
Maybe we can document it, here's a guidance.
Liudmila Molkova 00:39:05 I'm just kidding.
Aaron Abbott 00:39:06 stay through your study.
You wanna jump in?
Surya Teja 00:39:12 Hey, hi. I just have a small doubt. So this is for local agent-to-agent, tracing scenario, right?
And not just for remote Agent to agent?
Liudmila Molkova 00:39:27 So I think this section is for local trust, correct me. This section is for
remote, so for both. And it kind of makes sense.
To talk about both.
Trask Stalnaker 00:39:43 I think local to local would…
Probably be just nest these internal spans, invoke agent internal spans, that would then just get nested under each other.
Surya Teja 00:39:57 Eat.
Trask Stalnaker 00:39:59 Whereas the server span is designed to be the remote end of a… paired with a client invoke agent span, if you are also instrumenting the server
itself.
Surya Teja 00:40:16 Yeah, one thing that I want to add is, this is completely later on, but the local agent-to-agent, this scenario might be quite helpful for Claude Agent SDK, because that is summoning agents locally, and it is running in parallel, so this kind of spans
can be used over there. I'm just providing a use case. I'm not commenting on the broader, how and why's, but just adding more, case for this one.
Trask Stalnaker 00:40:48 Cool, thanks.
Sergey Sergeev 00:40:50 Yeah, I think if we clearly, define, basically.
some rules or guidance. Basically, if you provide more detailed child spans, with token usage, as an example.
on the span attribute, so do not set it, one's agent span were…
Maybe just produce just one agent span and do not show your internal complexity here.
If you provide the segregated… counters.
Maybe there are some, hybrid… use cases.
Trask Stalnaker 00:41:37 Yeah, it sounds like, so, the proposal would be to,
Not capture… basically, don't capture tokens on… Invoke agent… internal spans… Or server spans… in general unless…
You know, you're trying to optimize telemetry cost.
Like, and you're not capturing nested…
The actual nested spans for some reason, but that would maybe… not be recommended.
Liudmila Molkova 00:42:23 You don't know.
Right? Your Invoke Agent Instrument.
Trask Stalnaker 00:42:27 You would have to…
Liudmila Molkova 00:42:28 orthogonal.
Trask Stalnaker 00:42:30 Unless you control the platform.
Liudmila Molkova 00:42:35 Yeah. But…
Trask Stalnaker 00:42:36 I'm not sure that needs to… yeah,
Let me start with, Sergey's proposal.
And unfortunately, we don't have… Ankit couldn't make it today, so our… the real domain expert isn't here on my side, and I'm…
Swimming. I'm trying.
Sergey Sergeev 00:43:00 Also, one follow-up question, how do you capture that server-side, span?
Do you provide some tracer, or… and how you… and how you join it with your application-level tracer, so…
If you can show that, example, It will be helpful.
Trask Stalnaker 00:43:24 So, the… I mean, the basic idea would be that, so, right, we get a… you get a HTTP request.
from the client span, your HTTP server, like, you may have an HTTP server span here, which then puts the…
Span context in scope.
And that's how it flows down to now your generic, say, Python invoke agent instrumentation is going to automatically pick that up.
Sergey Sergeev 00:44:04 Yeah, I don't know how ADK is doing it, for OpenAI, you can,
You can basically start it easier.
When you run, openAI. Application.
And it basically captures… That telemet, but,
Yeah, yeah, I'm trying to understand how… if it's even a use case when you have application-side telemetry and server-side telemetry, and you will get both server-side traces and coin-side traces in one
In one kilometer tool, it will be some server-side observability.
Is it your platform specific, or is it General Wizenable?
Monero.
Trask Stalnaker 00:45:03 I mean, I guess what I would… yeah, I mean, it's…
it's… if you have a platform, and I think this probably applies to,
The… most of these agent platforms where you can run your agent.
And your agent can make client calls to other agents.
And so… I mean, when you talk about client, it's not like it's…
client running on, you know, your local machine, it's…
Client span that's still running on the platform.
And so… The trace, you know, you can instrument that .
Sergey Sergeev 00:45:52 So, Aaron, can… Yeah, I see you.
Aaron Abbott 00:45:58 I was gonna say we should maybe call time on this,
But I did have one other comment to kind of be a hypocrite here, but, like, I think another proposal, and I haven't thought this one out, is to have a different attribute name, so that
If you do a flat sum, It's always, like.
you know, easier to reason about, versus having to look at the actual structure of the spans. I don't know about this in particular, but maybe we can, like… I think other… some platforms have already probably handled this.
We can look at what other people have done, like,
Yeah, yeah, like you said, Alex has a handle on this. I don't know if anybody knows how Lingsmith does this, or other platforms, or anybody else on the call.
But yeah, we should… and I was gonna say, I'll probably get somebody from, like, our UI side to take a look at it, so that they don't… I don't have to try to explain this to them later. See if they can leave a comment.
Sergey Sergeev 00:47:00 Thank you.
Trask Stalnaker 00:47:01 Yeah, overall, I like Sergey's proposal, though, of, I'm gonna see if that works, for Ankit.
Of just not capturing tokens on the internal and server Invoke agent spans.
Liudmila Molkova 00:47:25 Yeah, I… I'm…
Let's move on, but I have some thoughts. I think these cases should look similar, like, whatever we come up with. I don't feel like why they are different at all.
Like, the client… the internal and client.
Trask Stalnaker 00:47:42 internal and server?
Liudmila Molkova 00:47:45 Internal and server, yeah. So if it happens in one process, or if it happens in two different processes, why does it matter?
Trask Stalnaker 00:47:53 I totally agree. I don't think that… Proposed anything different.
Liudmila Molkova 00:48:00 Okay, then maybe I misunderstood.
Aye.
Trask Stalnaker 00:48:04 Only that the span kind… would be different.
Liudmila Molkova 00:48:10 the level of control is different. You cannot control anything that happens here.
You don't know. It's client application.
Trask Stalnaker 00:48:24 Let's take it to the PR.
Liudmila Molkova 00:48:26 Yeah.
Yeah, Nakamarlich.
Trask Stalnaker 00:48:29 Thank you all for all the input, though.
Liudmila Molkova 00:48:33 dear.
nagkumar 00:48:34 So, memory spec, we spoke over this a while ago, we've had,
Around 50 comments. There have been a few updates, so genai.memory.type has been removed.
Because only Azure AI Foundry had this natively, and no other framework exposes it. So if we decided that if we need it on Azure site, we'll just add it as a vendor-specific attribute. And we also found that
We did a little more research on the GenAI memory scope across 6 different frameworks on
Who supports what, user, agent, conversation, team are the four things in the enum that we have come up with.
And yeah, we have updated the artifacts with the VR description and other things, so…
One more reviews, that is… I guess, Trask and Redmill are the only ones who've…
commented on it, so we would love to have more people look at it and give me more feedback so we can get this.
Merged, or take it to a state where it's good enough to be merged.
Trask Stalnaker 00:49:48 Nagmar, I left a comment, at…
I think maybe you missed it, the… at the bottom, the… the tables. I was trying to, validate
this yesterday, and the, like, if you can add links to the PR description table cells to basically, right, everywhere where it says yes.
If it can link to the API,
So that we can basically verify… validate.
nagkumar 00:50:28 Yeah, for the scope one, right?
Trask Stalnaker 00:50:31 For all of… for all of them. If you look at the… the original, like, I had left a comment,
nagkumar 00:50:42 I might have marked them as a result of.
you would pay.
Trask Stalnaker 00:50:46 You look at this.
nagkumar 00:50:46 fainted.
Trask Stalnaker 00:50:47 comment where, I kind of… First attempted to build that.
I had links in all of the… Cells… to the APIs, something like that really helped.
Because it's really… it's very time-consuming to go through and to verify that all of these things, whether they… whether it's truly generalizable or not.
nagkumar 00:51:17 Okay.
Trask Stalnaker 00:51:17 You really have to, as a reviewer, you really have to understand the individual or API calls.
Especially for those of us who aren't deeply Ingrained in this space.
Already.
nagkumar 00:51:32 Sounds good. I'll update the description to have links for each of the cells.
Trask Stalnaker 00:51:36 Cool. Thank you.
Liudmila Molkova 00:51:39 Thanks. A quick comment while we're still here. Is memory…
Always remote? Can it be local? It can be, right?
nagkumar 00:51:48 Yep.
Can't be locally.
Liudmila Molkova 00:51:51 Okay.
Okay, I'll take another look, and maybe I'll,
Share some thoughts based on this.
Thank you.
nagkumar 00:52:03 Phew.
Liudmila Molkova 00:52:05 Moving on, Aaron, MCP ecosystem Updates, nice.
Aaron Abbott 00:52:10 Yes,
So this is pretty cool. I don't know how I missed this, because I've been working on, instrumenting, like, the Python MCP SDK, but, Fast MCP, which I guess.
for the most part, it wraps the MCP client library, like, the actual MCP SDK.
They've got native OTEL API instrumentation for
the MCP semantic dimensions, I think it's even, yeah, it's even linked in here.
Liudmila Molkova 00:52:37 Follow them.
Aaron Abbott 00:52:38 Yeah.
Liudmila Molkova 00:52:39 Wow!
Aaron Abbott 00:52:42 Yeah, so I figured I'd share this, I'm playing around with it now, but
It's… it's pretty exciting to see, and
Yeah, you know, hopefully more stuff to follow.
If you go back to the notes, or we can look at this for a while, I don't know.
Liudmila Molkova 00:53:00 Acquire it.
Aaron Abbott 00:53:01 Yeah, yeah. So I linked, kind of, what I'm doing in the core MCPSDK here. I have pretty much everything, like, diffed out.
there's this… Tricky question of… Fixing the context propagations that the transports
kind of communicate with the MCP logical layer.
Had a PR out for this for a while, but…
Yeah, I'm just trying… I will coordinate between, like, FastMCP and this work as I kind of get it done, but I just want to let people know I'm working on this, so…
That would be, like…
Liudmila Molkova 00:53:35 up.
Support. Encouragement, review.
Aaron Abbott 00:53:40 Yeah, if you want to review…
That would be… that'd be cool.
Sergey Sergeev 00:53:45 Yeah, it will be super happy to review, because I had to implement it in SDOT Expoenix history.
for a customer urgent request, and I think I see the same conclusions, basically, meta for context propagation. However, I play it with a transport level
Propagation using, the baggage.
So, and, in general, gRPC and HTTP should support it, I think, out of the box.
Liudmila Molkova 00:54:16 Not for streaming, though.
Sergey Sergeev 00:54:18 Say it again?
Liudmila Molkova 00:54:19 Not for streaming. The moment you start streaming, you cannot support… you cannot use transport context.
Sergey Sergeev 00:54:27 Then meta, yes. I think I will be able to review it quickly.
Aaron Abbott 00:54:35 I think… I think Meta's actually pretty uncontroversial, so if you go back to the notes… .
Sergey Sergeev 00:54:40 Yeah, Leon.
Yes, so this was actually…
Aaron Abbott 00:54:44 it's pretty much, like, copy-pasted from what we wrote. I think Adrian took it over and put it into,
the SEP there. So this is merged into…
You know, model context protocol for now.
Liudmila Molkova 00:54:56 Nice!
Aaron Abbott 00:54:58 Yeah.
Sergey Sergeev 00:54:59 This has exceeded.
Aaron Abbott 00:55:01 Yes.
Agree.
Sergey Sergeev 00:55:02 Yeah, I will come over to you with conversation ID.
And security settings, basically client and server side, so we need to clearly define when
How to control, which attributes are propagated, from the coin side, and same on the server side, when and what attributes should be accepted.
Aaron Abbott 00:55:29 Would this… would baggage not… Kind of be sufficient there?
I think the spec says that you should… sorry, it says you should use whichever propagators are configured. At least in Python, we include baggage and trace parent, which includes trace state also, by default, so…
what were you thinking to promote, like, a conversation ID?
More specifically.
Sergey Sergeev 00:55:55 Egm specifically is a use case when you want to stamp it on every span.
propagate down to the child's pens, but do not want, to send something like ChatGPT Conversation ID over to the remote server.
Yeah, other correlation attributes may be…
the same, so maybe you want to send something like conversation ID or session, but not the user ID, or…
Aaron Abbott 00:56:29 Yeah.
I mean, I kind of feel like baggage is the right tool, but we don't have really great guidance in OTEL on how to use it. We don't have any, like.
For lack of a better word, baggage filters or baggage samplers.
But, like, obviously the, you know, user can set it in their code before they make the call, so… I think,
My preference would be to solve it with baggage, if possible. I don't know what other people think.
Sergey Sergeev 00:56:55 And baggage will travel using that method by default, right?
Aaron Abbott 00:57:00 Yes, correct.
Sergey Sergeev 00:57:02 okay.
Liudmila Molkova 00:57:09 Moving on, notification semantics are fuzzy.
Aaron Abbott 00:57:14 Yes. So this was kind of while I was implementing it, I'll be really quick here.
One thing I noticed was notifications are…
inherently, like, responseless in the JSON RPC spec.
I linked the… the JSON RPC spec in the notes here. There's kind of an interesting…
The link.
Liudmila Molkova 00:57:36 It's not a problem, though, because at least in
from the .NET SDK, you send an actual
Data over the network, and it's hand out on the server.
And the server does not, like, does not process it, it doesn't return anything, but it's, like, from the tracing perspective.
Or duration, it's still a network operation.
Aaron Abbott 00:58:03 Yeah, I hear you. I think, unfortunately, the way the Python one is made, it's very fire and forget. It basically just goes in a queue, and there's no callback mechanism for when the notification happens.
Liudmila Molkova 00:58:15 But it's still… there is still something on the client that awaits for their request to complete, or nothing at all.
Aaron Abbott 00:58:22 No, no, no.
Liudmila Molkova 00:58:23 Not even in the framework.
Aaron Abbott 00:58:25 Correct, yeah.
if you click on… on… I mean, it waits for the… in queuing, but it doesn't wait for anything to consume the queue, necessarily. It could be a.
Liudmila Molkova 00:58:34 I see. Yeah. Yeah.
Aaron Abbott 00:58:36 If you click on that one right there, I think…
it's a little bit fuzzy, but it says… you know, I think this is mostly referring to the client-server model, but it says
You know, they're not confirmable, so you don't… you don't necessarily know… you might know it was written to the network, but you don't know that it was received by the server.
Liudmila Molkova 00:58:54 Right, it's still… if network fails, at least sometimes it would also… Fail.
Aaron Abbott 00:59:00 Yeah.
Liudmila Molkova 00:59:01 If I forget the HTTP call, then it would…
Fail, some were just not on the… The caller wouldn't know.
Aaron Abbott 00:59:12 Yeah, so it might just be an implementation detail for Python here.
Which is fine. And then the other thing that I think was a little fuzzy was if the notification… there's, like, a notification on the server, so there would be a client… sorry, a server span on the client for the notification.
And, it's not super clear if those ones should be parented by…
like, if the whole thing should cascade such that the notifications that were emitted from an original MCP call should all kind of appear in the same parent-child relationship.
Liudmila Molkova 00:59:47 Hmm, so this, this longer running, the, the, the, the polling for the… Yes. Yeah.
Aaron Abbott 00:59:53 Yeah.
Liudmila Molkova 00:59:54 Yeah, that's a good… It shows the important part, the notifications are delivered, or not.
Aaron Abbott 01:00:03 Yeah, I think for Python, it's an implementation detail that we can't see that.
Liudmila Molkova 01:00:09 But, yeah.
That's a tricky place.
Like, do you want us to do something about it, or it's just something that's not ideal, but…
She'll be…
Aaron Abbott 01:00:19 No, I don't think we need to do anything, I just kind of wanted to call it out.
Liudmila Molkova 01:00:24 And maybe documented better.
Aaron Abbott 01:00:27 Yeah.
Liudmila Molkova 01:00:30 Oh, sorry, we didn't get to it. Anything really quick you want to mention?
Aaron Abbott 01:00:36 Well, maybe, I think, since we have Sergey on the call, Sergey, do you know anything about the status of this one? The…
contrib langchain instrumentation we've been working on from Splunk.
Sergey Sergeev 01:00:47 He does it, is it somewhere on the wrong namespace? Is it, doesn't need to be…
Have they somehow, got into wrong namespace, or, not sure, Eve.
Aaron Abbott 01:01:06 Yeah, I think there's the Pi Pi question. I don't know if we've reached out and kind of got agreement from.
Sergey Sergeev 01:01:11 Yo.
How I view it, as unconsciously?
Aaron Abbott 01:01:17 Y'all reach out on Slack.
Sergey Sergeev 01:01:19 x.
Liudmila Molkova 01:01:20 Awesome, thank you all.
Aaron Abbott 01:01:22 Thank y'all.
Liudmila Molkova 01:01:23 See you around.
Aaron Abbott 01:01:24 Later.
neil yashinsky 01:01:27 Alright, everyone, thanks.
