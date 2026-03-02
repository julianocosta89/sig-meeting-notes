SIG: LLM Semantic Convention WG
Date: 2025-08-12
Duration: 102 minutes
============================================================

## Zoom Recording Transcript

Sergey Sergeev 00:03:01 Hey, folks.
Shuwen Pan 00:03:04 Hey? Hello.
Keith Decker 00:03:08 Good afternoon, good night, wherever you are.
Aaron Abbott 00:04:39 Alright, everyone, please add your name, your name to the attendees list, and add any agenda items if you have them.
Okay, … I don't think Ludmil's gonna be joining, so we could probably…
Get started whenever. Seems like we have pretty good… Attendees know, …
Alright, let me share the project board.
Okay, new issues, I think… I think we talked about these last week. These were kind of follow-ups to 2179.
… I guess we should probably move these to to-do.
Alex, I don't know if you're planning to work on this, or you already started, but… …
Yeah, seems like a reasonable follow-up.
Alex Hall 00:06:58 Too many things, I guess.
Aaron Abbott 00:07:01 Sitian, sorry.
Alex Hall 00:07:02 I haven't started anything, I've just been gathering thoughts.
Aaron Abbott 00:07:07 Okay.
No worries.
… Yeah, and this one's kind of in the same camp.
I'm gonna move it to to-do.
So we don't triage it again.
Okay, does anybody want to say anything?
Is that anything on the board, or we can just go into the agenda.
Alright, … I think this one's for the next APAC meeting.
Does anybody want to say anything about this, or should we just… let's just skip back?
Alex Hall 00:07:46 I'm just thinking, on that board, there was also, like, a category, how to model prompts and completions, maybe those issues…
Should be going there, not to do.
Aaron Abbott 00:07:57 Oh, yeah.
Are these all open PRs, though? Let's see… I guess not.
Alex Hall 00:08:08 For example, this issue.
It's like… To me, underneath that, more message part types.
Aaron Abbott 00:08:18 Okay, yeah, we can move it here, and then, …
This one too, right? Yeah, built in server-side.
Alex Hall 00:08:26 Germany.
Aaron Abbott 00:08:27 Okay.
Yeah, but Milliken… Tell me if we did this wrong, why did this?
Okay, cool.
Ankit, did you wanna… I think you're up next, did you wanna share your screen?
Ankit 00:08:49 Sorry, I'll… I'll just need, like, a couple of minutes, and my laptop restarted, so I joined from my phone. So I'll need, like, a couple of minutes, I'll be….
Aaron Abbott 00:08:58 Okay, so maybe we'll come back to you?
Ankit 00:09:01 Yeah, that'll be… yeah, thank you, appreciate it. Yep.
Aaron Abbott 00:09:04 No worries. Okay. Then… Next on the agenda, Radima.
You're on?
Ridhima Satam 00:09:12 Yes, let me share the screen. I'm asking for review, but I have a question there.
Aaron Abbott 00:09:21 You should be able to share whenever.
Ridhima Satam 00:09:36 Okay, maximum is up, yeah.
So, this is basically the PR for, …
For the telemetry span, to spans for the line chain.
And what I see is,
In this, there was a variable first, the DB, sorry, the attribute GenAI system, and that has been deprecated. So, I earlier, in this PR, I used that, GenAI system, which actually indicated the chat OpenAI line chain,
Langchen's Chat OpenAI. There is one more… instead of system, they introduced the JNI provider name as OpenAI, so actually where your model is serving, that is getting saved in this. So, let me show you the code, actually, here.
what do we want to do, actually? Because if we remove the system right now, then we will… we will not get the context of line chain.
We'll just have, the provider.
So… here… where I'm generating the telemetry.
So…
Yeah, so when the model is starting, I'm fetching some attributes, so one of them was the CNA system. Here, the name was coming chat open AI, and then there is metadata where I'm putting the provider name, setting the provider name. Now, here we just set the OpenAI.
So, what do you think? …
Is it okay to take out the… Langtuning.
Context from here.
Alex Hall 00:11:23 I don't think that we should have a deprecated attribute in there.
Ridhima Satam 00:11:26 Yes, yeah, I'll remove that.
….
Alex Hall 00:11:29 I do think that we had a conversation about this, and we weren't able to resolve it, but we were saying that there should be, essentially, two attributes along these lines, one for the back end and one for the
sort of client library, API protocol.
But we didn't manage to finish that discussion.
Ridhima Satam 00:11:48 Okay, so for that purpose, we were thinking of introducing JNAi.framework, where we can add line chain, and then this
for this… Yeah, of course, I'm going to remove the system.
About then the provider we can keep in, as it is, like, whatever coming from the provider's list.
Alex Hall 00:12:08 Well, framework or land chain or whatever would be…
neither of the two things I was talking about. Why do you want to record the fact that this is a land chain span? How does it help?
consumers.
Ridhima Satam 00:12:23 It's just the… not the span, but about… it gives you information about the framework you're using, right? So… when it's getting at the back end, you know that the framework was used towards LandChain.
Aaron Abbott 00:12:38 So, are you talking about the agent and vacation span, or, like, the, the completion events?
Ridhima Satam 00:12:44 Yeah, these are just the completion, yeah. It's just the LLM invocation, yeah, sorry I missed.
Aaron Abbott 00:12:51 No, no.
Sergey Sergeev 00:12:52 Yes.
Aaron Abbott 00:12:53 Yes.
Sergey Sergeev 00:12:53 Some context that on the backend, we can visualize basically differently if it's one chain or if it's a different framework, so we can basically show some indication, okay, it was done not
… Just even an icon of the framework.
To show that this application is used in the chain.
And second, there are some, …
Framework-specific concepts, which can be also visualized, in comparing to,
So, same type can be converted to… Langchin.
Chat OpenAI.
step.
comparing to the same LM application can be visualized as something else in different frameworks. That's the rationale for doing it.
Alex Hall 00:13:57 Can I ask, why are we building another instrumentation
in the country repo, as opposed to
contributing to the native instrumentation. Like, there's already… within Langsmith.
some OpenTelemetry thing, and I… I think…
like, it mostly does the right work, actually. I don't know if the attributes align, but in particular.
The biggest problem with all of the line chain implementations is the context.
Not propagation, really, but, like, the…
Spans having the correct parents and children.
…
And I think the only way that that problem will ever be solved is some kind of contribution within Langsmith.
Sergey Sergeev 00:14:45 It's… yeah, it's both. So, we are thinking about integration, which can be used, basically for, landsmith, so they have integration with OpenTelematy.
And, this is maybe a better way to do it, but we were thinking about vanilla Python instrumentation as a trace hoop.
library donation right now, because, TraceHoop donates, one-chain instrumentation, and this is how we started,
Contributing to OpenCelemet project?
I think, … integration part, which will be contributed to, Wellesmith.
is second, way to do that. But again, I think we have a little bit more control contributing
to OpenClimate Python can tip.
But, open to any suggestions. I think we should do both, and just see which one sticks.
Anyway, okay.
Alex Hall 00:15:54 Okay.
Aaron Abbott 00:15:56 Yeah, yeah, I mean, I think there's some issues with…
like Alex mentioned with the propagation, …
And obviously, they're not following the semantic conventions, so….
Sergey Sergeev 00:16:06 Yeah, and second thing which I, just remembered, so in Wank Smith, again, when you…
use that integration, you have to deal with, basically figuring out if the global OpenTelematy, context already set up, if you have a tracer, it's a little bit different with,
login provider, for example, you need to check if my application already set up that login.
How do I do it, deal with it if you're using zero-code instrumentation from OpenTelematic and tape?
which a lot of customers want to do. You have a little bit more integration with OpenTelemet SDK, so you can expect that those providers will be set up by zero-quote instrumentation.
Aaron Abbott 00:17:02 Yeah, yeah. I think maybe, yeah, maybe we could treat these separately, like, I definitely think it's worth…
engaging with Langsmith a little. Like, I had a back and forth with them, and they seem open to contributions, but probably unlikely to improve things today.
I think maybe Alex's point was.
is there… does this PR actually have the parent-child relationship working correctly?
Like, is that fixed in your slip? Is it fixed here?
Sergey Sergeev 00:17:29 Yeah, we definitely used it in our demo applications, and it basically connects to the parents' pants, and, …
fully OpenCelematic compatible, so it uses, basically wrapar functions for,
So you need to make sure that… For, link chain, callback concepts, so…
It checks the current span from the global context.
Children's… Yeah, yeah, it's….
Alex Hall 00:18:00 a child.
Awesome.
Sergey Sergeev 00:18:02 It sets the child spends.
Alex Hall 00:18:04 It sets… it sets the current span in the context, and….
Sergey Sergeev 00:18:08 Yeah, I… I think so. Redima, can you provide…? Yes.
Ridhima Satam 00:18:13 We, we do that.
We do it.
Okay, I'm just adding a spam contest.
Aaron Abbott 00:18:23 Yeah. I mean, I definitely… I trust that you tested it, and I don't know if these were edge cases, but I remember one of the issues was that
They have kind of, like, an event loop, and they'll run
callbacks in that event loop, so they're not actually properly represented with the context bars that we use under the hood. So, because they're not running, like, in a stack.
The parent-child relationship didn't propagate right, but… …
Yeah, I mean, I guess we can dig into it on the PR review, too. But do you… does that sound familiar at all?
Ridhima Satam 00:18:53 Yeah, so right now, this PR is just for, LLM invocation, just one simple thing, but we have tested in the POCs, like, when we are testing with tools and other things, so in that, the… we set from where these
Children are coming, like, we set the parent for that, so that we have the proper child-parent relationship set in this code itself.
Aaron Abbott 00:19:20 Okay, so it sounds like there's a lot of topics on this that are kind of independent. I think we should come back to the thing Alex raised about the Langsmith integration.
But, like, for now, I guess my question is, coming back to the original question, which was about the provider thing, right?
…
like, do you think this is blocked? Do you want to propose, like, open a PR to add the framework? Like, what do you want to do here?
Ridhima Satam 00:19:49 Yeah, so what I can do is I'll take out the system right now, because of course, it's deprecated, and then we can just review it for now, if that's okay, and then I'll open a PR for the semantic conventions, and talk about this, how we want to introduce it, and that way we can go. What do you think?
Aaron Abbott 00:20:11 Yeah, I mean, that sounds good to me. …
Yeah, that sounds good to me.
Ridhima Satam 00:20:18 Well, yeah, take out it, or take out the system and then ask for the review on this, then. That's the only blocking thing for this.
Aaron Abbott 00:20:26 Okay.
Can I ask one other question on this PR, just before we move on?
Ridhima Satam 00:20:30 Yeah.
Aaron Abbott 00:20:32 So how are you thinking about
like, the operation spans and duplication between, like, the OpenAI client instrumentation and the link chain level instrumentation.
Ridhima Satam 00:20:46 Hmm… I didn't get that question. Sergey, do you know?
Sergey Sergeev 00:20:52 Yeah, can you repeat that?
Aaron Abbott 00:20:54 Yeah, yeah, so maybe a scenario, like, if I used this lane chain instrumentation, and I also used the, OpenAI V2 instrumentation, right? Say I was using the OpenTelemetry instrument command.
… Unless there's some kind of affordance here, you would get duplicate completion spins, right?
Sergey Sergeev 00:21:13 Yeah, that's right, you will get, basically, child spans, so you will get link chain, chat.
Span?
And you will get OpenAI, … In vacation span, …
The way to differentiate it on the backend,
you can filter by framework, so it probably doesn't make sense to show OpenAI span in …
In the context of Lankchain?
trace, another option is, basically to have, specific documentation how to install… if you install end-chain instrumentation, probably you don't want OpenAI instrumentation.
But I can see, … Different customers wanting,
to instrument part of the application with OpenAI, part of application with LChain. So, same Python application might be using
Different frameworks as well, so….
Aaron Abbott 00:22:17 Yeah, I mean, that's kind of my concern, is I feel like they should work together, …
So, for example, like, the main thing I would want out of the lane chain instrumentation would be the… the, …
like, the framework level stuff, so I think there's, like, conversation ID, you know, agent invocation, tool calls, stuff like that, right? And then the actual completion events could come from the underlying client. So, like, I know our, the OpenAI V2 could be used, or the Vertex one.
And we… we could still have a way to capture in…
Langchain, but it's really hard, because I'm assuming the Langchain chat OpenAI thing is called before, …
The actual client library, so… If the client library has more detailed spins, There's no way to really…
Know if they're gonna be created beforehand or not, so… …
Yeah, I don't want to boil the ocean, though, like… Maybe, maybe we can, …
I don't know. I'll take a look at this PR, and …
And see what we can do. But yeah, that's what I'm thinking.
Sergey Sergeev 00:23:27 Another option, we just, keep it in mind, merge this one, and see what the actual customers
do vivid, and how… They use, and next we can figure out how to avoid duplication.
Aaron Abbott 00:23:48 Okay, cool. Anything else on this one, or should we go back to Ankit?
Ridhima Satam 00:23:53 Yeah, that's… yeah, thank you so much.
Aaron Abbott 00:23:56 Okay, thank you.
I'll get you around.
anksing 00:24:03 Yes, I am.
Aaron Abbott 00:24:05 Great.
Did you want to share?
anksing 00:24:07 Sure. Let me share my screen.
Is my screen visible?
or not.
Aaron Abbott 00:24:19 Yeah, I think it's coming up.
anksing 00:24:20 Open now.
Aaron Abbott 00:24:25 Yep, you're good.
anksing 00:24:27 So, …
I think, there were some good comments on the PR, and then we had some great discussion in the previous meetings as well, so… and, I think thanks to Limila, she has kind of, …
Put down a comment which kind of summarizes various different options that we possibly can have.
And, …
I'll just quickly go over them, and if anybody has any comments or suggestions, please do interrupt me. So, I think she comes, like, I think one great perspective she has put down is
The focus on, like, where this information will be used. And two of the scenarios are one is
showing the eval scores along with the GenA telemetry of your application in some sort of a UX user-friendly way, where customer can go see these things, and then possibly filter out traces and things like those. And the second one is for your monitoring purposes, where you would want to have these scores,
Available for continuous monitoring, and you want to have some alerts.
Right. And then I think she describes about how, having,
Like, events, and filtering them by, by name could actually help with the second one, for sure.
So… The three options that come up here is… one evolves.
Are, like, reported as… …
arrays and spans, and I think this is more about, like, having a complex attribute, if I understand this correctly. …
However, like, one of the drawbacks for this is that once the span is done, you cannot add more.
Metrics or evaluations if you have to in future, and it seems to be… …
Some of the scenarios that a lot of companies support.
And the second one is, …
Report, like, a span for each eval method and score, and one of the drawbacks for this one is, if you have your evaluator kind of spitting out multiple scores, then do you create a span for each one of them?
Which, in a way, feels definitely excessive.
burden. I had to kind of do that.
And the third one is about, …
Results could be reported as… like, evaluation scores could be reported as events, and then you could also have an
eval span, which shows you how these scores were, calculated, traces for those.
However, here you'll be creating two different things. One, events, and the other one is the evaluation spend.
And then Lumina has put down some pros and cons, where, … having events, I think.
So… … And… So…
With this, and I think I did some research over the last week to kind of look at… I wouldn't say research, but it was more like gathering information. So I would try to put together these requirements that came up, and then a comparison of different, like, vendors who provide evaluation,
capabilities, so…
Let me know if these requirements look good, or if there's anything I'm missing. So, one of them was, like, multiple matrix.
I think Alex and Sam has brought this up.
And then evaluator Traces, and then consolidated eval scores at one place.
So it's easier to query them, and then the evaluation scores to be calculated offline.
So, and I put down, like, these three options which, are coming from that comment on the PR. One is having events, the other one is just spans, and then span plus events.
So overall, like….
Alex Hall 00:28:19 Would you use a span if the evaluation score was calculated offline?
anksing 00:28:25 Yeah, so this one would be more like, …
A single span for every evaluation score.
Alex Hall 00:28:31 But for the last row… Evaluation score calculated offline, like, that's like the human annotation, right?
anksing 00:28:39 Oh, so actually, when I mean offline, I mean, like, after your trace has completed, so if you do, like, a couple of days after that, right?
You run your application, you have your traces, and after a couple of days, you kind of run them.
Alex Hall 00:28:52 There is still, like, some automated process with the duration.
anksing 00:28:55 Yeah.
Sergey Sergeev 00:28:56 Human evaluation can fit this, use case as well.
anksing 00:29:01 Oh, that's true.
Alex Hall 00:29:03 So….
Sergey Sergeev 00:29:03 Human feedback.
Alex Hall 00:29:05 That's fine.
Sergey Sergeev 00:29:06 And just to clarify, so the idea is that we send the span and use a span linking to link it back to the trace, so it's not part of the trace, original trace produced by application, so if you evaluate any data.
which is request response to a LAM, for example, in a span, you can link it back using span linking, but it won't be the same trace ID. It will be a separate span.
anksing 00:29:43 Thanks, Sergey, for the… Context, appreciated.
Aaron Abbott 00:29:47 Can I ask a….
anksing 00:29:48 Oh, sure. Yeah, please go ahead.
Aaron Abbott 00:29:51 Yeah, yeah. So, is there anything that you want to actually trace during the offline evaluation?
So, is it… it, like…
It seems kind of weird to emit a SPAN as just a kind of data holder, but if it's, like, you know, a managed
Or self-managed, evaluation platform where, say.
you want to see how the evaluation ran, how long it took, stuff like that, then Trace makes a lot more sense. Which one is kind of the….
anksing 00:30:18 So for, for human feedback, like, at least in my opinion, I don't see any benefit of having a span, because this is just, like, some static data customer's gonna provide, and there's nothing you would probably want to see on how somebody came up. It's just, okay, you provide those annotations, right?
And for that, like, events definitely align in, at least in my brain, pretty seamlessly.
…
However, like, span plus events kind of capture that scenario of, if you want to capture how an evaluator came up with a score, yes, that makes sense. And I was thinking in the terms of, you can always have events, and then you emit a span
And link it if you want to, and that would be an optional thing.
Sergey Sergeev 00:31:03 Right.
anksing 00:31:04 And when I look at, like, a lot of the vendors, like, most of them, I think, except
Or I have, like, 1, 2, 3, 4, 5 of them here.
And if I include Microsoft as well, so 6, then…
We do, like, all of them do show the results, but I think only Pydantic, or majority of them, do not show the traces for the evaluators right now.
I'm not saying that's not useful. It is useful, like, when I'm building it, for sure. Like, Arise also gives you that capability, but only during your development experimentation phase, where customer can manually do that, and it, like… so it's not, like, something which platform provides, in their case.
As an inbuilt functionality.
… What they focus on is…
I have the scores, I want to show them, and then I want to show them alongside the traces.
And it should be kind of easy to query, right?
So, with that regard, like, I think I'm definitely leaning towards
having events to show the scores and associate them with the trace, or span, like, using trace ID span ID, and then…
You can link the spans which generated those evaluation scores, and that could be an optional thing.
So, I wanted to, like… Get feedback and understanding if that seems like a reasonable… Approach to go with.
Sergey Sergeev 00:32:35 Yeah, I… in my… in my opinion, so for different backends and providers, again, different telemetry might fit for evolutionary results, so evaluation result can be a span.
We've just, …
As a data holder, or it can be event, and both of them should be connected to the original span and trace.
Which was used to evaluate, and potentially conversation ID if it's part of the parent attribute. And for evaluation operation, it can be…
Span for sure, because that evaluation… operation span should include tokens usage, and etc.
… So it will be coming maybe even from OpenAI,
instrumentation, if you use OpenAI. Again, we need to think how to avoid duplication of the data.
Or should we put everything on the same evaluation results plan?
How many networkings it used, and etc.
anksing 00:33:44 So, one follow-up question there, Sergey, for, for an evaluator, say, which emits out multiple scores, like, how would you represent that on a span?
like, I was thinking of, like, you could have events for every matrix, but then you could also link that evaluation span, with your actual trace and span.
And the matrix are still limited as events.
Like, just wanted to get your understanding as well on….
Sergey Sergeev 00:34:13 Yeah, first of all, I think OOM as a judge can evaluate… can produce different evaluation results in the same request. Let's say you evaluate request response to AOM,
And you prompt LM as a judge, basically return me a list of different results. If you detected bias, if it looks correct to you, and etc, so…
it will be a structured JSON output, which is a list of evaluation results. And in this case.
We need to put just one evaluation operation, which counts tokens usage.
anksing 00:34:54 Oh, yeah, yeah. But then, like, to the user, you would want to show, like, all the evaluation scores, right? Like, if you… if your evaluator calculates multiple of them, right? So, how would you represent that on that evaluation span?
Sergey Sergeev 00:35:07 Yeah, in general, it's up to the backend, so if you have conversation.
centered view, you can annotate some of the conversation connecting the data. Okay, I detected, this.
…
basically evaluations for this conversation, and I think it's what is happening in the industry, a lot of providers doing it.
…
Yeah, basically, those evaluation results, you can annotate different conversations, and you can connect it to a trace view.
anksing 00:35:42 I see.
Sergey Sergeev 00:35:42 It's coming.
anksing 00:35:43 So… so if I go with this sample, right, are you able to see my screen? I just want to make sure I'm sharing my GitHub sample. So here, say, for example, like, you had some evaluation, right, which you are, putting under a span, say, which is an evaluation span, and this produces multiple scores.
Like, how would you put those scores on a span, right?
Would… are you, like, proposing, like, the attribute to be a complex attribute which can hold more than one score, or…?
Have, like, a span for every score.
Sergey Sergeev 00:36:17 ….
anksing 00:36:18 It'll clarify that part.
Sergey Sergeev 00:36:19 Yeah, I… I think, SPAN per evaluation result is my preference, or event per evaluation result. Sorry, that I'm taking the stage, I think,
Alex, Aaron, and the rest have a word to say on it, too. I see a word in the chat.
anksing 00:36:38 Sure, I'll… sorry, I'm not able to see the chat, but yeah, please go ahead and…
Unmute and ask the question, please.
Alex Hall 00:36:47 No, it's… it's the alternative plan of fusing events. How I think that would go would be.
you… you have events which are… and I've also put this… I also comment on that… that third…
With the document and everything.
You have spans and events. The spans represent the evaluation process. They're optional.
The events represent the scores, and in particular, the events are children of the original evaluated span.
anksing 00:37:24 I see, okay. So, events would go on the span which is being evaluated, right?
Alex Hall 00:37:30 Yes.
anksing 00:37:32 And then you can link the actual evaluation span, which shows you the trace of our evaluation score got.
Alex Hall 00:37:38 Yeah, I don't know. I think that to…
If you're looking at the event and you wanted to see, okay, where's the evaluation span.
…
we just put some, like, custom attributes on the event. I don't think there's a neater way to do it.
anksing 00:37:54 Hmm, I see.
Alex Hall 00:37:55 Events have span links.
But that's okay.
anksing 00:38:00 Oh, wow.
Alex Hall 00:38:00 And vice versa. Okay, not actually vice versa, because for some reason, events don't have….
anksing 00:38:06 Does he vote?
Alex Hall 00:38:07 of their own.
anksing 00:38:09 No, events, I think it's hard to link events back to a span, right?
Let's produce them.
Alex Hall 00:38:14 I'm not sure if that's possible. If that's possible, then that's awesome.
anksing 00:38:17 But I didn't find it.
Alex Hall 00:38:18 ways to identify an event, like… More luck.
They don't have a primary key.
anksing 00:38:27 As far as I can tell.
Aaron Abbott 00:38:32 So you mean linking the event back to the span?
Alex Hall 00:38:36 As in, if you happen to be looking at the evaluation span, it would also be nice, and you could easily go the other way, if there was a way of…
Identifying or describing the events, although in that case, you would need an array.
The
The other option is you just… you have the scores on both, you have the scores on the events.
ends ban.
And the events are a bit cleaner, and they work in all cases where the span may not exist.
Sergey Sergeev 00:39:02 … I dear.
Aaron Abbott 00:39:04 Yep.
anksing 00:39:11 Oh, sorry, I think I heard somebody, but I'm not sure.
Sergey Sergeev 00:39:16 You heard my colleague.
anksing 00:39:18 Oh, I see. Sorry. I see, okay, sorry, okay. No problem. I thought somebody was trying to say something, but I…
So, …
So it seems like, like, we all agree on having events on the actual trace or the span that's being evaluated, right?
And then having a evaluation span and how to link it, that's something we still need more discussion on.
Does that summarize the discussion correctly?
R.
Alex Hall 00:39:53 Yeah, I agree.
Aaron Abbott 00:39:56 So do we have a concrete use case for actually emitting a spend for the evaluation result?
Sergey Sergeev 00:40:03 Mostly, it's, from our side, it's a preference of the backend team. Mostly, I think, some other providers may pay for that data to be sent as a span compared to event, but, …
Again, if we can make the telemetry optional.
span… your span link or event, it might be best.
anksing 00:40:37 So, would it be okay if I start another issue to discuss on, like, span, like, evaluation span, and then for this PR, for this PR, we can move ahead with…
Events?
Like, evaluation scores, images, events, and then… I'll probably, like, work on… Closing on that as well.
Does that sound like a reasonable plan?
Aaron Abbott 00:41:03 Yeah, that sounds great to me.
anksing 00:41:04 Okay.
Awesome. Yeah, I'll… I'll do that, and I'll update the PR and share, make the change in the PR to reflect that, open a new issue, yeah. And, yeah, I'll post it in the…
… channel as well, like, the Slack channel, so… and if I could get some…
Reviews and any other feedback to help, like, move this forward, that would be amazing.
Appreciate it, man.
Okay.
Okay, so it sounds like we all agree with going events for capturing evaluation scores, right? And…
Sounds amazing. Okay, thank you. I think this sounds like good progress to me.
Aaron Abbott 00:41:50 Yeah.
Cool. Anything else on this?
anksing 00:41:57 Actually, just one thing, like, I know, like, there are, like, some of the attributes that are put on there. If there's any feedback around those, please do.
I'll share them as comments, and I'll work on those.
But overall, yeah, thank you for the feedback.
Aaron Abbott 00:42:14 Cool. Thank you for following up.
anksing 00:42:16 Thank you.
Aaron Abbott 00:42:17 Alright, we've got one more topic here. Keith, you run?
Keith Decker 00:42:22 Sure, just looking for some, maintainer's eyes on the Gen AI utils structure PR. We got the approvals needed, just need some maintainers to look at it so we can continue on to the next phase.
Aaron Abbott 00:42:34 Awesome, yeah, that's me. Sorry about that.
… Anything to call out here, or is it mostly just, boilerplate?
Keith Decker 00:42:42 It's boilerplate with a link to the design document.
Aaron Abbott 00:42:45 Obby.
Sergey Sergeev 00:42:47 Why?
Aaron Abbott 00:42:48 Exactly.
Sergey Sergeev 00:42:48 hardest problem solved about naming and location of the package. I think everything else will be smooth.
Aaron Abbott 00:42:58 Okay. Any plans to use this one in, the link chain stuff, or we'll just refactor later on?
Sergey Sergeev 00:43:06 Yeah, we plan to, do both things in parallel, because… Discussions take time.
And it's quite straightforward to convert.
Aaron Abbott 00:43:17 Really? Yeah, that sounds great to me.
anksing 00:43:19 I don't know, yeah. I'm excited about this one. It'll make things, like…
easier to kind of just use this package and instrument Engine AI.
Appreciate for the work.
Aaron Abbott 00:43:33 Absolutely.
Alright, well, that was the end of the agenda.
Nobody else has any topics, we can end a bit early today. Oh, maybe I should just call out, Goodmilla's PR, actually.
So, I don't know… I think there was a few more little back and forths with Alex.
Let me see it, yeah.
anksing 00:43:54 And, I think I also had one comment about that, … Yeah.
And it was about, like, tool calls, so if you can get to that, that'll be good.
Aaron Abbott 00:44:06 Did you leave a comment already?
anksing 00:44:08 Yeah.
So….
Sergey Sergeev 00:44:16 I'm wondering, in general, if in practice, especially Alex, Pydantic, and the rest of providers, do we see that chat history growing infinitively, especially for multi-turn conversations and…
How do we deal with it on the backend? Especially for bigger contexts, like 200K tokens?
Alex Hall 00:44:38 Where we have the separate uploads concept that I think was in this PR, and then we removed it because it's like, we don't know how to specify it.
Sergey Sergeev 00:44:48 So you have… so it's… it can be limited in the spec, right? That the truncate chat history?
Alex Hall 00:44:57 Or is it to use… I don't think you'd rather upload it to separate storage.
Sergey Sergeev 00:45:01 Oh, using Message Refert.
Aaron Abbott 00:45:04 Yes, yes.
Alex Hall 00:45:05 But there is actually mention of truncation in this spec, which is just… Instrumentations may truncate.
Sergey Sergeev 00:45:13 Yeah, I think it's crucial to ensure that if we put the actual context in the chat history, that we truncate it by default.
To some reasonable… Default.
Alex Hall 00:45:27 By default, you don't include anything.
Sergey Sergeev 00:45:30 Say it again?
Alex Hall 00:45:31 I think the default is nothing gets included.
Sergey Sergeev 00:45:34 Oh, okay, that's great.
Alex Hall 00:45:35 Although I don't really know why that's… A topic of the spec.
Sergey Sergeev 00:45:40 Makes sense.
Alex Hall 00:45:41 We're going to ignore that in Pydantic AI, we're going to… if you turn on instrumentation, then by default, it will…
Record content.
Aaron Abbott 00:45:55 Sergey, did you want to, like, drop a comment on here regarding the truncation, or does that….
Sergey Sergeev 00:46:01 Yeah, I need to review this PRS so we won't paint it.
I need to refresh again.
Aaron Abbott 00:46:08 Okay.
Yeah, I would urge, you know, like, if you have some thoughts on this, please take a look. Like, it's been open since, I think, April… yeah, late April.
Sergey Sergeev 00:46:17 I have my comment, I need to check if anything changed.
Aaron Abbott 00:46:22 Okay, yeah, yeah, no worries. It's just, I think this one is blocking a couple different other PRs, so…
That's why I wanted to just bring it up again.
But Ankit, did you want to talk about this one?
anksing 00:46:38 Yeah, so… I think, …
One thing, like, I found challenging here was, there was no way to, like, link this tool back to a tool
This tool called to a specific tool?
The only thing….
Alex Hall 00:46:54 like that. Like, in what way is the name not…
the whole information. What do you mean by specifics?
anksing 00:47:02 So, would name be unique for tools, right? So, for example, like, I was trying out something yesterday with, Assistance API, or even Azure A Agent Service.
Where I could give two different tools, which had the same name, but they were different type of tools.
One was, like, a function tool, I named it as FileSearch, and then I had a file search tool, which is the built-in OpenAI tool, and…
So, if I just go by the name, then… Impossible for me to identify.
Alex Hall 00:47:33 I think that we will… you know, we haven't figured out built-in tools entirely, that's why, like, it essentially got removed from this…
…
PR, as in… there was an example of how to do it, and then we realized, okay, there's some things we're unsure about. So there's an open issue about that, which was mentioned at the beginning of the call. I do think…
If we ended up modeling built-in tools to look the same as function tools, we would probably have, like, at the very least, some Boolean flag built-in true or something.
anksing 00:48:06 I see, okay.
So the other thing I tried was, I used OpenAPI Tool, which is just a risk specification, right? And then…
I named it same as a function tool, and I still ran into that issue, which basically both are not built-in tools, it's just that.
Alex Hall 00:48:24 I have not heard of… open API tools, it sounds.
Intriguing.
Please… Yeah, I think…
This is one of the reasons why I started those follow-up issues, like, more message part types.
We do need to be having these discussions sooner rather than later, because this is, like, the most fundamental stuff.
But also, we want to get this PR merged.
As, like, the foundation.
anksing 00:48:54 Yeah, no, definitely agree.
But I feel like, like, name, will that be unique enough to identify, like, which tool this tool called came from?
It's… Like, the bigger question for me.
Alex Hall 00:49:12 We could also, in the case of function tools, be adding
something like code.function.name, I don't know what the
Thing is, but there is already semantic conventions for, like, Names of actual code.
Functions, like the local… Things seen by the interpreter, rather than whatever's sent to the model.
anksing 00:49:39 I see, so it's some sort of namespacing, in a way.
are… prefixing with the….
Alex Hall 00:49:48 I just mean that if it so happens that you somehow Use a different name.
anksing 00:49:54 input.
Alex Hall 00:49:56 In the code, compared to what you send the model.
There is actually already, like, a logical semantic convention to use there. But that's… this is essentially going off track a bit.
We don't yet have a plan for…
how to model the different kinds of tools. Well, we have a plan, but we're still discussing it.
I would say start by looking at their built-in tools.
Issue.
anksing 00:50:25 Oh yeah, yeah.
Alex Hall 00:50:27 I'll take a look at it. I feel like…
the last issue we were having about built-in tools came down to feeling a bit weird about things related to choices and messages versus parts, and I think we've essentially made a decision that we're going to stick with
One output message equals one choice.
And therefore, everything has to be in a list of message parts.
anksing 00:51:00 Okay.
Aaron Abbott 00:51:01 So, ….
anksing 00:51:06 So for now, like, tool name would be sufficient to identify a tool, right? Would that are…
Just curious on that part.
Alex Hall 00:51:16 I think tooling is pretty clear what it would be for the case of function tools.
And for built-in tools, Might as well just…
Also use whatever built-in tool name you feel like, but…
For gods and tools, there's still something that we might actually change up, like…
If, for example, you call the OpenAI Responses API,
you get back, like, this list of output parts. They fit the current convention fairly well. There's, like, a text part, and there's, for example, with the code interpreter built-in tool, there's a code interpreter part, but it's just one part. It contains both the code that got executed and the results.
And so, if you wanted something that matched that OpenAI structure, you'd have just one part there.
But the Gemini API returns two parts. It separates the code from the results.
And that fits better with the… To request, tool response structure.
And I do think we'd want something unified, and I think… I personally think it would be nice if it… if it looked like the…
Local functioning tool parts.
anksing 00:52:29 Yeah, definitely. I think I agree too. That makes it easier to understand and consistent.
Aaron Abbott 00:52:37 Yeah, I feel like there's always going to be some level of normalization that we're doing.
like, you know, there's… I guess OpenAI has, like, kind of 3 outstanding APIs to call their models, right?
Sorry, OpenAI. So, like, You know, things you might have to squint sometimes, like.
I wonder if it would be reasonable for instrumentations to
You know, enforce that. So if we say name is the identifier, right?
I mean, I guess it's not great, and if it's a common thing, we can make it more clear, but the instrumentations could, you know, like, generate something so you could stitch pieces back together, but….
Alex Hall 00:53:12 It could also be taken further, as in, like, built-in tools… there's a few common ones, there's, like, searching the web, contempting code.
A specialized part for interpreting code would also be kind of nice.
Yep. And that's always displayed in, like, a UI or whatever as, you know, syntax-piloted code, and…
The amount of space logs, or whatever.
Right now, if we went with the built-in tools, look like function tools, the code interpreter outputs, in particular, has a different data shape, depending on whether it's OpenAI or…
Gemini, whatever.
Aaron Abbott 00:53:54 Yeah, so I guess, Ankit, do you have, like.
Maybe, is there, like, a suggestion you could make?
On this comment, like, you know, we could write that down and make it the rule, or we could, you know.
Change something up.
If you have a suggestion, yeah.
anksing 00:54:10 Yeah, definitely. Yeah, I think I'll, dig into how, like, tools are being identified, like, in the Azure Agent service to kind of
come up with a suggestion, yeah. I'll probably spend some time on that, yeah.
Aaron Abbott 00:54:24 Okay.
Yeah, let me see… where's the PR?
Thank you for raising this, by the way, I think, …
It's always good to get more eyes.
anksing 00:54:37 Yeah, like, I ran into this issue because I was trying with the… something with the evaluation, I was like, if I have two tools with the same name, though different types, and then it messed up, I was like, what's happening? And then…
That's how it came up, so it becomes kind of a little important for evaluation as well.
Aaron Abbott 00:54:54 Absolutely.
Sorry.
And Alex, you, you left this comment here about the opt-in thing. I feel like we've gone back and forth on this one a bit.
Alex Hall 00:55:08 It's not specifically on the opt-in thing, it's on… well, it's those four lines, it's about
Are agent spans supposed to have input and output message attributes?
It seemed like she… Partly adjusted in a commit.
Where she changed, like, the descriptions of the…
the attributes within the registry to say, just model instead of model or agent. So I think that the intention was that these aren't supposed to be there.
I mean, I don't know if anyone else has any thoughts on this.
Aaron Abbott 00:55:45 No, I agree.
Alex Hall 00:55:46 It seemed like we… We decided to defer that, and that if we did have these.
They would have a bit of a different meaning.
Aaron Abbott 00:56:07 Yeah, no, I agree.
Alex Hall 00:56:11 One other thing on my mind is that…
I thought that, as a general principle, I'm just gonna link In the chat.
…
it was decided to not use events as a way of recording details, although I don't actually know what this
comment means.
But I think… The idea is that since complex span attributes exist now.
You use those rather than using events.
Aaron Abbott 00:56:50 What was this in reference to on the PR, though? Just using events in general?
Alex Hall 00:56:55 Wha- why… why… why is there this…
Influencer Details event in the GenAI PR.
Aaron Abbott 00:57:02 Yeah.
Alex Hall 00:57:03 Whose existence is apparently entirely
You know, taking things that would have been spam attributes and putting them in a chart event instead.
Like, I don't feel strongly about this, because I don't…
I think we want to use that.
ourselves.
Aaron Abbott 00:57:21 Yeah, I mean, I can speak to that.
Alex Hall 00:57:22 make it work, but, like, I don't know if there were some people in these meetings who pushed for that.
Aaron Abbott 00:57:29 Yep, I mean, I was one of them, so…
The main use case was, like.
There are customers who want to capture 100% of the prompts and responses, even potentially outside of tracing.
So, in order to do that, they can emit them as logs, or as events, right?
And it was also helpful for server-side, where you don't necessarily want to, …
Emit, like, an entire span, or even participate in the same trace as the color, but you can represent these things still following the semantic conventions.
Let me see if I can….
Alex Hall 00:58:08 So the span may be… Is the event meant to be a child of this ban?
Sergey Sergeev 00:58:15 Essentially? I think it's always like a span, span event or spine work, basically you just include fields, trace ID and span ID.
Of, as a brand, spend.
Alex Hall 00:58:30 Which is the parent span? Is it the GenAI span, or the….
Sergey Sergeev 00:58:35 GenAI, spans four different times, like, inference, agent anniversation, etc, whichever produces, input and output from LOM, so you can….
Alex Hall 00:58:49 The intended use case is that
The span itself may actually be…
Like, excluded by something, so this means that…
In the intended use case where people are not recording the spans, they're only recording the events, the events is not gonna have a parent. It's gonna…
Wouldn't it make more?
Aaron Abbott 00:59:11 Right.
Alex Hall 00:59:14 Does it actually say… it doesn't seem to mention anything about the parent or the context of this event. Should that be specified? It seems like it should be.
Aaron Abbott 00:59:23 I mean, I feel like we don't generally do that, like, you know, things are supposed to kind of compose, and it's hard to guarantee the context when you get called, whichever code is doing the recording, unless it's all part of one instrumentation, but…
Like, like you said, in the event that you're not doing tracing, or you've sampled away the spin, then you wouldn't have any kind of guarantee that the parent is there.
Alex Hall 00:59:44 The examples do say, that the… no, I'm… so I'm looking at the wrong thing.
Yes, the examples do show the event having
the GMI span as its parent. Like, the trace ID, the span ID feels the same.
Aaron Abbott 01:00:03 Yeah.
Alex Hall 01:00:04 I think maybe that's missing from the spec, but it does mean that, yeah, you're asking for…
to not be able to actually know the real context of the event. Whereas if the event in the span was sort of siblings, and they…
Both had the same parent, which was… some other span.
then you know where the event belongs. Now, you only know the trace it sits in, but not…
Any more detail on that?
Aaron Abbott 01:00:37 I guess that you're also going to have the opposite problem now.
Alex Hall 01:00:42 If you do have… well, if you have the span and the event.
How do you even know what the point of having both is?
Aaron Abbott 01:00:56 Yeah, I… I think you would… Yeah. There's definitely some cooperation
complexity, like, if you just wanted to record on one or the other. I think, now that I was thinking about the eval conversation as well, it seems difficult to link an event back to another event.
as the eval score for that thing. Like, it still has to have a span ID to link them together, which you can do even if it's sampled, but….
Alex Hall 01:01:24 But I also don't really want to.
delay the PR on this point. I'd rather, if you took this on now, and if you think that there's a problem here, just… the whole thing seems weird to me, but…
I'm not invested enough in the event side of this.
Aaron Abbott 01:01:40 Yep.
Yeah, I mean, I think maybe… we had a lot of conversations, I can try to dig them up, and, you know, we could talk about it next time, too, if this isn't merged. And I think Ludmilla has a lot of context, too, but maybe I'll go through the… all the issues that were linked, and see if I can pull things together.
Alex Hall 01:01:59 Okay.
Aaron Abbott 01:02:01 Okay.
Cool.
Well, we're at time now, …
Thank you, everyone, for joining, I think this was a really productive day, so….
anksing 01:02:12 Awesome. Thank you. Thanks, everyone. Bye.
