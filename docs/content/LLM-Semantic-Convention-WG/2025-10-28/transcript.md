SIG: LLM Semantic Convention WG
Date: 2025-10-28
Duration: 62 minutes
Zoom Recording URL: https://zoom.us/rec/share/IJiyzsu_14uufAteEM9bL8GhTymtuZyWTnQc3JNDB5fxZXUHoNWVg-KArR4lRH0H.-Qacsd2NQFGYi62N
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:12 Hi, everyone.
Josh Winerman 00:01:17 Hi, Leon Miller.
Liudmila Molkova 00:01:22 Okay, let's give people some time to join, and…
If you have any topics, please add them to the agenda. I will… Go ahead with some triaging.
So let's see what we have in the new issues.
Okay, we talked about it last time. There was a pull request. Oh, Josh, you're here. I left another…
comment on… Your pull request.
I do think it's…
it's super valid to have retrieval span, it's just it's not… it does not need to be… it should not be in the GenAI
Space, because it's… just… generic search.
And I'm happy to discuss it further, and kinda help you make progress on this. I'm also curious, like, what is the… is there a specific problem you're trying to solve for? It's, like, just instrument log chain?
Kind of concern.
Josh Winerman 00:02:34 Oh yeah, yeah, sounds good. I hadn't seen your comment yet, thank you again, though. But let me, yeah, let me look at this, and then, Sergey and I, are really driving this together, so it's… it's hard for me to have the full vision as well, being honest. But thank you, though.
Liudmila Molkova 00:02:51 Yeah, of course, thank you.
Okay, so I am going to… Move it to…
To-do, maybe?
There's a caveat that, Let me,
Rephrase it slightly.
And I think it's more a general… And, vector databases… So I'm actually going to…
Maybe merge this one.
Into this issue.
Or maybe… maybe vector databases are… Special beast.
Okay, I still haven't made any progress on the workflow agent tasks. I didn't create the meeting, I'm sorry, let's keep it here so I don't forget.
Keith Decker 00:04:18 Sounds good.
Liudmila Molkova 00:04:20 Is this a new issue?
For EI client82EI Server Metric Semantic Conventions.
R.
I think agent ID has high cardinality, as well as AI Client ID.
So, I don't… Fully understand.
What's being asked here?
Okay, let's wait for the…
For more information, too.
Comp.
Okay, let's… Take a look at.
Couple of other issues, and move on to the main agenda.
When request fails…
Spends for LM, cash, write, and rate tokens. Okay, let's take a look at this, too.
Dylan, are you here?
Okay, I think he's asking a fair question of what to do when the request fails, and I think it's…
Maybe we need to document something, but it's pretty trivial.
In most cases.
So, if we downstream, So it's all or nothing, right? So if there is…
If request fails, there is no output, and there is error.
If we're streaming, then… There could be partial output, and we should record it. It's probably truncated.
And we will have… information,
We would populate finish reason with an error, and we would have error type to say what's failed.
Alex Hall 00:07:54 Was he not also asking about the input?
Liudmila Molkova 00:08:00 I think, why would it affect…
Alex Hall 00:08:02 Okay, first one is the…
Liudmila Molkova 00:08:08 And then, I think he's asking what the hook should do.
And I think the hook for the upload hook, we should call it all the time, but the combination of
Attributes would tell if there is an error, and if the finished reason is not success.
And record what we have.
So I think it's pretty straightforward, and it seems it's a good thing to document.
So I'm going to move it to to-do.
I don't know what I should do here.
I think we need to add label.
Accept the Trinity they seek.
Okay. If there are volunteers?
Go ahead.
Okay, and the last issue, the triage, spends for LM cache, write and read tokens.
Oh, I haven't seen this one. How come?
Yeah, I think we… we need to find a way to document,
Samuel Colvin (Pydantic) 00:09:43 Should this not be spanned attributes for LLM? Not spanned?
Liudmila Molkova 00:09:49 Yeah…
I agree, this is great to share. I think it's more nuanced, though.
Samuel Colvin (Pydantic) 00:10:07 we have… Alex might remember, but we have
I forget, 4 different types in Gen AI prices, but they roughly match that.
Liudmila Molkova 00:10:20 Yeah, so we have input tokens, output tokens. We need to decide what to do with input tokens.
Right? And then…
Alex Hall 00:10:30 I mean, there's, you know, there's cache read, there's cache write, there's audio, there's cached audio.
And, like, for example, Anthopic actually has, I think, two kinds of cache.
Something either read or write, or maybe both, and…
But there is another issue about this anyway.
I'm just gonna stick in the chat.
Liudmila Molkova 00:10:56 Oh, thanks.
Oh, wonderful.
So let's… Close this one…
Alex Hall 00:11:12 We said that we would get to this, but I don't actually see that happening soon.
So…
People, please feel free to propose.
Liudmila Molkova 00:11:36 And you shared what you have here in this issue, right? So you had your priorities.
Samuel Colvin (Pydantic) 00:11:41 We have go down a bit more, and we have a bit more…
Liudmila Molkova 00:11:45 Oh, nice.
Samuel Colvin (Pydantic) 00:11:49 If you, if you look in the, the, the comment above, I think…
Liudmila Molkova 00:11:52 Oh, sorry.
Samuel Colvin (Pydantic) 00:11:54 Yeah, that's what we have at the moment as our definition of usage.
Alex Hall 00:12:00 So from that definition of usage, we can calculate prices in most cases.
Samuel Colvin (Pydantic) 00:12:05 We also… we need to add…
We need to work out how we do built-in tool calls.
Soon, because we're about to start losing money when people use tool calls and we don't charge them, so…
It's gonna become important fairly soon.
Liudmila Molkova 00:12:24 So the reason I was, I think it's not super straightforward. So the, let's say, input audio, audio tokens are also part of total input tokens, right?
Alex Hall 00:12:37 Yes.
Liudmila Molkova 00:12:38 And cash write tokens are also part of input tokens.
Alex Hall 00:12:43 Yes, right now it says text, but that's incorrect.
Liudmila Molkova 00:12:50 So…
Yeah, whatever we come up with would probably be imperfect, right? It would involve some level of, some learning curve.
Whoa, whoa.
Alex Hall 00:13:01 Some are subsets of others, and pricing calculation has to, like, subtract things to make it work.
Samuel Colvin (Pydantic) 00:13:07 Yeah, because different models count them different ways, as in some of them, it's input excluding cache, sometimes it's total input. We try and get to the, you know.
You know, a correct representation, but…
I don't think it's, flawless.
Liudmila Molkova 00:13:23 Right, yeah. So, like, it's the problem of choosing the least confusing option out of all of them and documenting it then.
Samuel Colvin (Pydantic) 00:13:32 Yep. I think this is probably close to the least confusing option right now, assuming that they don't change how they do it.
Liudmila Molkova 00:13:41 Okay. So… I… Do you…
Do you want to make a stab on it, or you're… I've heard, Alex, you don't.
Alex Hall 00:13:54 I don't want to promise being able to do this soon.
Liudmila Molkova 00:13:59 Okay.
Let me try, let me make a stab on this, and let's see.
Samuel Colvin (Pydantic) 00:14:09 Thank you.
Liudmila Molkova 00:14:19 Okay, so we spent 15 minutes on the triage.
Is there any new member who would want to introduce themselves?
You don't have to, but if you're here, wish…
And you want to share what brings you here?
Come on.
The stage is yours.
Okay, if you change your mind, go ahead and add your, add a topic to the agenda, just say hi, it's okay.
Moving on to the main agenda, I wanted to make a couple of small announcements. First of all, the KubeCon is coming in 2 weeks?
If you are there.
We will have Open Telemetry Observatory somewhere in the project pavilion or something. We will have a GenAI SIG office hours. It just signed us up. I don't know if anybody shows up, but it's on Wednesday at 3pm.
I will be there. I hope other OpenTelemetry contributors will be there as well. Come say hi.
And… Is anybody coming to KubeCon?
Oh, so Jay.
O'Keefe, nice.
Okay, so this observatory thing, it will be there for all 3 days, so if you are bored, or if you want to just come and talk to people, this is a great place to just hang out.
So don't hesitate to come during KI office hours or at any other time.
Okay, and last announcement, this week, is the GC election week, up on telemetry GC.
I think many of you are eligible to vote, and please go ahead and vote. GC are the people who decide open telemetry roadmap, and
they usually have a lot, of interest and, control over the project. So if you,
I don't know, if you have a preference, or if you don't have a preference, go take a look at the people's biographies and what they would like to do in OpenTelemetry.
Okay.
Moving on… Let me close… stinks…
So, I, made another pass on MCP semantic conventions.
I would appreciate some reviews. I lost, my,
I don't know, enthusiasm on it, because I didn't have any approvals, but it seems people are consistently asking about it. I've seen Python instrumentation that's being added, or being proposed.
And I consistently get requests from people to
go ahead and figure it out. So, if you…
Could please take a look?
I…
would like to get a couple of approvals from the SEEK before I bring it to the general semantic conventions.
And… the action item from the last time, I think, was that
you folks asked me to change if anything has clarified from the MCP side on the context propagation, and no, it's not.
the… MCP… Discussion, I should link it somewhere.
But essentially, MCP discussion is at the point where, okay, we use
We have placed the propagate context, A room?
It's Meta.
Param's meta. And, that they don't care what we propagate there.
Samuel Colvin (Pydantic) 00:19:03 Would it help if I sent this to some of the MCP, governing people and got them to review it? Because they might have opinions on it.
Liudmila Molkova 00:19:13 That would be wonderful, yeah.
But at the same time, it's been out there for, like, 6 plus months, and
It's already implemented in some places, and it…
just makes sense to document it, and if…
there is an official MCP position on this, we can always accommodate this position in the future versions.
Samuel Colvin (Pydantic) 00:19:36 I'm pretty sure David's take will be, thank you someone else for having thought about this, great, but I will ping him and try to get him to… look at it.
Liudmila Molkova 00:19:45 Yeah, thank you.
Okay, so then let's keep it open for another week and come back to this.
Samuel Colvin (Pydantic) 00:19:54 Alex, do you know if this matches how we do it in LogFire Instrument MCP?
Alex Hall 00:20:01 what, the conventions? I haven't actually looked at them.
Samuel Colvin (Pydantic) 00:20:04 Okay, maybe you could have a look, Alex.
Alex Hall 00:20:06 Yeah.
Aaron Abbott 00:20:10 Yeah, I'll take a look as well. Thanks for putting this out.
Liudmila Molkova 00:20:16 Thank you.
Awesome. Avan.
Samuel Colvin (Pydantic) 00:20:34 I'm actually seeing David Pereira today, so I will make sure to bring it up with him.
Liudmila Molkova 00:20:39 Oh, thanks a lot, appreciate it.
Have fun, let's talk about session ID.
I'm sorry I didn't see your update.
Pavan 00:20:54 Yeah, yeah, no worries. I think, last, like, you know, two weeks back when we discussed, we wanted a bit more clarity on the definition between, like, a session, a workflow, and a task, and to see, like, where they are actually being used, and some references to it. I tried to…
you know, like, sort of document. Again, there are, like, probably more examples that we may, we may find. Another question that I had was if this probably makes sense to bring it up in the new, like, hotel, you know, like, agent's call,
That we may set up sometime.
Or, you know, if this probably makes sense to discuss here, because, like, me, Keith, and a couple of others are sort of working towards, like, you know, working on similar things. So…
Liudmila Molkova 00:21:51 Yeah, so I think the session would be something that's generic for all Gen AI, it's not, like, edging.
well, maybe it's multi-agent specific thing. Let's talk through it. So the trace loop… oh, sorry, no, MCP has a concept of sessions. It has really nothing to do with.
Pavan 00:22:11 The…
Liudmila Molkova 00:22:11 any… Conversation thread, or… Other things we're discussing.
The MCP session is essentially when the client says, okay, hi, server, I want to talk to you, let's talk for a little bit, and let's end it.
And it's, it's…
I feel like this is not the session that we are talking about here, is it a fair statement?
Pavan 00:22:39 Yeah, I think, you know, when me and Sergey were sort of discussing internally, we tried to, you know, find a few, examples, and I believe, you know, like, the…
trace loop, implement… implementation of the, MCP sort of did, use that, but again, as you say, maybe not in the exact, sort of.
You know, like.
thing that we are looking at in general for, like, multi-agentic systems, but yeah, we try to, you know, sort of gather roughly, and again, like, sort of put together a doc for that, which will essentially try to, you know, help
identify, like, a unique, a user interaction session within a particular application that groups all related telemetry, you know, like spams, traces, until the session is terminated. So…
Liudmila Molkova 00:23:37 So this session…
Pavan 00:23:38 Conversation ID, there is session as well.
Again, has some interesting use cases.
Liudmila Molkova 00:23:47 Yeah, so can we… I'm not sure, I might have missed it. Is there…
Unique identifier representing user interaction session with application.
Pavan 00:24:04 So this is me coming to interact with, maybe, a conversation.
Liudmila Molkova 00:24:10 And then disconnecting from it.
Pavan 00:24:13 Yeah, it could be, like, let's say, you know, again, I'm just trying to take a multi-agent example here. An agent that is probably meant to interact with a user, you know, a user submits a query, and then that agent internally
hands it off to, like, n number of different agents under the scenes, which…
doesn't necessarily, you know, have any interaction with the user. It goes off, does its own thing, it interacts with, like, a bunch of tools, and then, you know, like, sort of, in an async manner, comes back with a particular response.
And these agents themselves could be, like, not co-located, meaning they could be distributed, but the attribute that sort of tries to group together that entire end-to-end, you know, interaction
would be our session ID.
in…
Liudmila Molkova 00:25:09 Wouldn't it be the trace ID? In this scenario you provided, the trace ID would serve the same purpose? It's not always the case, but in this scenario, it would be.
Pavan 00:25:22 It may not always be the case, yeah.
But we essentially, have…
you know, some examples where different agents have, like, different, you know, like, trace IDs that they spin up in an async manner, and trying to essentially have, like, a closed tie-in with, like, the trace ID that is actually originating the entire
flow of sorts could be, like, sort of, problematic. And we sort of assume that there could be different races as well that
overall works towards, like, you know, serving the, user. so…
You know, like, essentially, then, you could group together a number of different races for that particular,
Yeah.
interaction.
Liudmila Molkova 00:26:17 Right, so… the… thing we discussed last time, right? So there are scenarios where the trace ID would work.
There are scenarios where the conversation AD would work.
Pavan 00:26:32 the…
Liudmila Molkova 00:26:34 session idea, or workflow idea. It's something that
Regularly understandable, but it's… it feels…
we really need that, like, how badly do you want to solve this problem? Why do you want to solve it so badly? What is the scenario that you try to address? Or is it, like, you just want to address the most generic case?
Pavan 00:26:56 No, actually, I mean, not necessarily trying to
you know, go behind this problem for eternity, obviously, but something that, you know, has already been implemented by a few providers, you know, like Langfuse and, like, a couple of others as well.
But it doesn't necessarily have, like, a representation in the semantic convention, and we also have, like, a concept of session ID within our SDK, so we just thought that, you know, having this,
accepted in the convention could mean, like, general acceptability for the, terminology as well, within, like, the GenAI systems, because
When these agents work together in an incoherent manner, then they would need to somehow
be grouped together by a single attribute. So, again, like, just trying to see if this would make sense, or if, like, trace ID or, like, the conversation ID would, like.
most sense, .
Liudmila Molkova 00:28:10 So, if I recall our discussion last time on this, that It sounds like…
we would like to explore as far as we can get without introducing new notions, and this is what we do generically in semantic conventions. We try to avoid introducing new things until we
know why, right? And we have a clear understanding of what they are.
We've done some…
bad things in the past, where we introduced something, and then it's impossible to use it, it doesn't fit anywhere, or it's too vague, and people abuse it. So we are a bit more conservative.
So, if…
Pavan 00:28:56 Understood, yeah.
Liudmila Molkova 00:28:57 Yeah, and obviously, if there is a real problem, and there is a real need to introduce it.
Let's… let's bring it. So far, it sounds like there are, like, there is a long way we can go before we have to do it.
Pavan 00:29:16 Okay.
Liudmila Molkova 00:29:26 Yeah, thank you.
And you can definitely bring it in the intelligence colleague, it's… yeah, if you folks there would have a strong need to introduce something.
Please bring it, and we will figure it out.
Okay, we are at the bottom of our agenda, but I think there are plenty of pull requests that we need to review.
I've seen quite a few asks in the chat. Does anybody want to,
Bring their pull requests, and we will take a look.
No? Okay, no.
Keith Decker 00:30:15 I've got a minor one for additional attributes in GenAI, utils that I can throw on the board, if you just want to look at it.
Here, I'll throw it in the dock.
So, when we first did, GenAI Utils, adding the inference, spam calls, we…
kind of omitted a lot of the SEMCOM attributes just to keep the PR as small as possible.
So this one is just adding additional attributes. Looks like we got a review 20 minutes to go.
Work on, but other than that, it's just…
Cleaning up some of the tests and adding… Or attribute.
Aaron Abbott 00:31:09 Yeah, I'm taking a look at this one right now. Apologize for the kind of delay here.
Yeah, makes sense to me, I don't foresee any problems.
Keith Decker 00:31:21 Okay, and then I'll add the second PR up there, too, after Aaron House.
Liudmila Molkova 00:31:30 Oh, we are switch… sorry, we are… oh, we've defined LLM and vacation, right, and this allows us to all do these things.
Keith Decker 00:31:38 Right.
Liudmila Molkova 00:31:57 These are… this only covers spans, right, not metrics yet.
Keith Decker 00:32:04 Correct. There is another PR that I just added on the doc that is adding metrics.
Liudmila Molkova 00:32:13 Okay.
Yeah, this looks good, it's just I wanted to compare it side by side, and maybe…
Take it offline, I'll promise to take a look.
Okay.
Yeah.
Aaron Abbott 00:32:33 I added this one again,
I don't think there's probably a ton to discuss. I think, Lamilla, looks like you replied.
And your change, your suggestion looks good to me.
There was just another reply from, Lingui.
And… I was reading it and didn't completely understand.
I know he's probably not here, but I'll send a reply.
Yeah, just, I guess, bumping this one, but other than…
the suggestion, Lavelle, does it look good to you now?
Liudmila Molkova 00:33:10 Mmm… Other than this suggestion, it looks great. I think I approved, no?
Oh.
Aaron Abbott 00:33:24 Honey?
Liudmila Molkova 00:33:28 Got it.
So I think we already have the… Prototype for this pre-upload hook.
Aaron Abbott 00:33:45 Yeah, I think so. Or, I don't understand why the existing hook couldn't already cover this.
Liudmila Molkova 00:33:52 Yeah, maybe he's just not aware of the hook.
Aaron Abbott 00:33:57 Okay, yeah, I'll, I'll apply the change and then just continue this discussion, but… okay, thanks for… thanks for the review.
Liudmila Molkova 00:34:07 I don't think he disagrees with anything, right? So…
In our case, we're saying it's bytes, but the moment it's realized, it's B64, and this is what he's also saying.
Aaron Abbott 00:34:23 Yeah, it seems like the concern is basically just allowing you to upload and stick a… use the URI part
Or the, or the,
basically to remove blobs, which I think we've heard from Alex, this is something that Pydantic is interested in too, so…
And I'm definitely interested in playing around with that as well, so I think the current structure wouldn't…
With the uploading hook and everything would not change this, but… For really small bite fields.
We should definitely keep the inline one, I think.
Liudmila Molkova 00:34:57 And we cannot make a plot hook required.
Aaron Abbott 00:35:01 Yeah, not too.
Liudmila Molkova 00:35:03 Yeah.
Cool, so then, I think,
I'll approve.
Oh, I approved already, so feel free to resolve this discussion and…
Once all the discussions are resolved, I'm happy to hit merge.
Aaron Abbott 00:35:26 Alright, great, I'll, update it today, hopefully.
Liudmila Molkova 00:35:31 Thank you.
Oh.
Do you want to talk about tool orchestration span?
Tao Chen 00:35:44 Yeah, so I created this issue this morning. So,
It's just adding another spend for… for spend type for agent. So right now, we have…
I would say 2 or 3, I guess, create agent, invoke agent, and the SEQ tool is kind of shared between
agent and, The motto.
And, you know, for agents, So, so I outlined in the issue, with the towel, so…
You know, sometimes an agent may or may not use tools, so when it uses tools, it may use one or more before it
Gets back a response to the… to the user.
So, within… between the… between the invoke agent and…
you know, the user query and the response, there's… there may be another loop that's inside the agent that's orchestrating the tools. So, we currently don't have a span to represent that, and
I'm just…
I just wanted to put this out and see how people like the idea of creating another spend type for agents. And the benefits of this spend would be, you know, we can attach some attributes that
That would make more sense on this span instead of in the invoke agent span.
If that makes sense.
Aaron Abbott 00:37:23 And, which, which attributes would those be? Like, the.
Tao Chen 00:37:27 Yeah, so I outlined two, so besides these two, we'll maybe have more. So, in some of the frameworks, when we have max iteration, like, you know, an agent may only be allowed to, invoke
you know, because sometimes you invoke a tool, and then the tool somehow throws an exception, that the agent is allowed to do a retry, right? And… and we can always set a,
Some frameworks allow people, developers, to set up a limits on the number of retries. So, I…
It could be a max iteration parameter, and you could set it,
You could record that in a spend so that, you know, people knows what's going on. And, you know, in the,
OpenAI Agent SDK, there's also this tool called Behavior,
Which I think makes more sense on this kind of… on this new span.
Yeah, yeah, Luke Mila is showing it on the screen.
Basically, what it says is, after the two use, does it return back to the OM to generate a response, or does it return the tool results back to the user?
Liudmila Molkova 00:38:49 This one, it makes sense on the Invoke Agent, right? It's essentially Invoke Agent.
Parameter.
Tao Chen 00:38:58 Yes and no, because if the agent doesn't use tools, right, if you just ask it a…
a question that doesn't require a tool, then it doesn't make sense.
to record this attribute, I think.
Liudmila Molkova 00:39:16 Oh, if user provided it, we would record it.
If… if it's available as an input parameter.
Even if it's invalid, right? It's not tough for us to decide what's valid and what's not in the instrumentation.
Tao Chen 00:39:31 Yes, yes, I think that's a valid argument, though.
Yeah, I think you're right, but,
Well, maybe we can record these attributes on the invoke agent, too, but then the max iteration, I think.
Maybe more… Appropriate to be in the new spend.
Liudmila Molkova 00:39:57 So, can you help me understand the scope of the spend? So, like, I have Invoke Agent, right? And let's say it's the client-side agent.
It would do some LLM call that would result in tools, And, so the orchestration…
You're suggesting… oh, sorry, the tool orchestration.
Tao Chen 00:40:24 Is that…
Liudmila Molkova 00:40:24 comparison.
Tao Chen 00:40:25 we… Invoke agent, and then if there is tools, Right?
you know, if there's tools, then it will do tool orchestration, and then LOM,
Let me actually share my screen, so that I can actually show you guys.
Yeah, so, can you all see my screen?
Yeah, so Invoke Agent, so if there's tool.
tools, right? Then you will have… to orchestration.
Great.
And then, of LM.
And then SEQ… Tool, and then…
Liudmila Molkova 00:41:15 Awesome.
Tao Chen 00:41:15 L. M?
And then, SAQ… Right?
And then it goes on.
So this is kind of the loop that the agent does internally, right? I also… That's just how.
Liudmila Molkova 00:41:34 then the tool orchestration span is… has the same scope as Invoke Agent. I mean, the same duration, the same outcome.
Pretty much everything the same, except the name.
Tao Chen 00:41:47 Mmm… Well, in some frameworks, I think there is something that's between invoke Higgin and tool orchestration.
Sergey Sergeev 00:42:00 So, maybe you can, share some, what example where the agent is doing it.
I don't think I've ever seen an agent which decides if
Some tools need to be used or not. They'll be really curious.
We see an example.
Tao Chen 00:42:20 Yeah, let me update the issue, and then I will provide some examples.
N.
Yeah, that's a great idea.
Okay, alright, so yeah, so this is a proposal, and I just want to see if people…
like it, and if not, I will… You know, it's okay.
Liudmila Molkova 00:42:45 I, I think that the… New attributes you're suggesting make sense.
the spend, though, I'm… like, if it's the same scope as Invoke Agent, or pretty much the same scope.
I would be cautious about editing it, because, like, the more nesting, the harder it's… like, it's more expensive, right? It's harder for users to understand what's going on. It's like, if we can express
What happens without this pen? We probably shouldn't introduce it.
Tao Chen 00:43:18 Yeah, that makes sense.
Aaron Abbott 00:43:21 Yeah, I was gonna say something similar, like,
I think I could see cases where the scope would be different. So, for example, like, if you had sub-agent invocation.
you might have, like, a set of toolset runs before the agent decides to invoke a sub-agent. So the scope could be slightly different.
It could also be kind of handy, excuse me, with, like, parallel tool calls, so if the LLM requests and the agent supports running them in parallel.
But I agree on the nesting concern, so, like, in the worst case, if you just run one tool, it just introduces kind of unnecessary nesting.
and I don't… I think you could still gather the same information.
By looking at all the tool calls that were done in parallel.
To see how long the toll call section took, or something like that, so… Yeah.
Tao Chen 00:44:14 Yeah, I'll, I will, I will gather some samples and, and,
You know, try to build up an argument on… on, on, on, on…
on the spend. If I cannot find any, I think it's fine, too.
Because I also share the nesting concern.
Keith Decker 00:46:15 But I think you're on mute, Ludmila.
Liudmila Molkova 00:46:19 Oh, I'm sorry, yeah.
Thank you.
So this, this one mimics the… This… this band's part.
Keith Decker 00:46:28 Correct, and adds metrics for inferences.
Liudmila Molkova 00:46:33 Craig.
Nice. So, Dan, oh, by the way, I think you could… Use the metrics helper here.
Keith Decker 00:46:49 Oh, okay.
Look at that.
Liudmila Molkova 00:46:52 There is a…
It's a selfish ask, but if you could try, and if you have any heart feelings about it, or ideas how it can be better, I would be interested in hearing.
Keith Decker 00:47:12 Sure thing.
Liudmila Molkova 00:47:13 Yeah, definitely go check it.
Keith Decker 00:47:14 Setup.
Liudmila Molkova 00:47:17 This… oh, this is the stable one.
Occupating.
Here we go.
So, there is this helper that allows you to create the… metric.
And it populates the description and units.
Keith Decker 00:47:46 Oh, okay.
Sergey Sergeev 00:47:48 Yeah, I think we internally discussed it and realized that it's missing a default bucket.
allocation.
Liudmila Molkova 00:47:57 Oh, and do you…
Sergey Sergeev 00:47:59 here.
Liudmila Molkova 00:48:00 Oh, okay.
Great.
Point.
This one, and yeah, so it makes it impossible for you to use the helper.
Sergey Sergeev 00:48:12 Right. Yeah.
Liudmila Molkova 00:48:13 Okay, yeah.
Okay, I'll…
Aaron Abbott 00:48:19 Would you mind filing a bug for that, Sergey or Keith?
Keith Decker 00:48:23 Yeah, sure, can do it.
Liudmila Molkova 00:48:25 I, I can, I can file it.
Aaron Abbott 00:48:28 Oops.
Sergey Sergeev 00:48:29 I will.
Aaron Abbott 00:48:30 I also want to see…
Sergey Sergeev 00:48:30 I appreciate it, because it will take me time to figure it even out.
Liudmila Molkova 00:48:37 Okay, I'll do it, offline.
Is there something… I mean, this looks good in general, it's just something that I would probably need to review.
Offline…
Sergey Sergeev 00:48:55 Yay, yeah.
Liudmila Molkova 00:48:55 Yeah, they're…
Sergey Sergeev 00:48:57 it overlaps with your pull request for OpenAI instruments.
Liudmila Molkova 00:49:04 Yeah, actually, let's.
Sergey Sergeev 00:49:06 A lot of the same stuff.
Liudmila Molkova 00:49:10 Yeah, so maybe let's take a look at that one as well,
So, I'll try my absolute best to get back to this PR this week.
the reason it's in draft, because it needs to take in all the goodness we've done, and Jenny, our tools was the helpers for
There's friends.
So Sergey, I think you've left some comments, and this is now part of the… Genio Tools.
Sergey Sergeev 00:49:59 Yeah, I think it supported,
But not the spend where it went. I think we are missing it, so…
In some ways, this is ahead of We'll see which MEA.
I think Jesus was,
Yeah, we have a development branch where we go way ahead of what's currently emerged.
So we will need to merge at least, those two kits, requests?
To… to be able to use,
OpenTelemator with huge NEA, for this, change.
Liudmila Molkova 00:50:39 Oh, no, I mean, I mean, the, the config.
The config should be already part of Gen AI too, so I think Dylan merged it.
Sergey Sergeev 00:50:50 Yeah.
Liudmila Molkova 00:50:52 I have a question about GenAI Tools. Did we release it?
Like, if we start using it, we will…
You need to release it first.
Aaron Abbott 00:51:05 Yeah, it's been released, at least 2 times, I think. We can…
Liudmila Molkova 00:51:10 Oh, nice.
Aaron Abbott 00:51:11 Yeah.
We can release whenever, though.
Liudmila Molkova 00:51:14 Okay, cool.
Cool, so I'll take what's already emerged, and we can always update this thing later to, leverage the…
Goodness, engineer, Tils.
Yeah, I think it's extremely valuable if you merge this one even before January 2, so we will have some test coverage.
Sergey Sergeev 00:51:39 So when we migrate to general tools, we can at least have some confidence that it works.
Liudmila Molkova 00:51:47 Oh, we should have tests for it. I should have updated tests, and we can just keep them in place without
they will still validate whatever is in the Gen AI tools.
Okay.
Anything else we need to talk about here?
Josh Winerman 00:52:20 Ludmila, could we have a small follow-up on the retrievals, now that Sergey's here, if you wouldn't mind?
Liudmila Molkova 00:52:26 Yeah, sure.
So that's fine. Go ahead.
Josh Winerman 00:52:30 Oh yeah, no, you go ahead. I was just gonna update Sergey on what we sort of chatted about briefly earlier.
Liudmila Molkova 00:52:41 I'm looking for the… or request.
So, I've, took a look at the Langchain Lama Index haystack. They all seem to provide some obstruction over retrieval, right? And it's a gen, like.
this…
This is pretty much the same as if I was calling, let's say, Elasticsearch client or, Vector Database Client, with the caveat that the abstraction, this part of step abstraction, lives in the GenAI-related library.
Would we instrument them differently, like the Elasticsearch client?
whether it was called from this abstraction or plainly. I think they are the same. The semantics should be pretty much the same. There could be some details here and there that we're missing, but the semantics should be the same.
And my point is that we should probably not put this attributes in GenA namespace, because there is…
not much Gen AI-specific about, let's say, top K.
Oy, the search type.
So if you look, let's say, into Azure AI Search, it has vector search, it has,
Whatever, semantic search, it has hybrid search, and it's…
specific to search, rather than GenAI.
This is the database name, the…
or the database system, and it does not need to be GenAI.
Same here, this is the number of similar documents you would want to retrieve.
This, again, is not Gen AI, this is the result of the query. You retrieved certain things from the search, and you've got some documents.
With this, I think all of this makes sense, and this pan makes sense, it's just not a GenAI span.
And I think it should be maybe in the search namespace.
And, some of this. And it should combine maybe some attributes from the database.
And we can define the span.
we can say, okay, this is heavily used in GenAI, so the GenAI people would have, I don't know, ownership over this spend.
Maybe along with database people.
But… It's just the… I'm asking to reshape the… The naming of this attributes.
Sergey Sergeev 00:55:24 So this plan makes sense, but the naming should be more generic, right?
Liudmila Molkova 00:55:30 Yeah, and if you take a look at the comment, there are some past discussions on this.
I'm not sure if I have more, I might have some, prototype of the search semantic convention, so I'll find a look. I'll take a look.
So there are some, services that are… that… that…
are pretty much the same. There are some considerations. If you look into…
Let me link another pull request.
So there is the PR, it got styled, and there were a few attributes that been introduced there.
Ehh… Similarity, metric, oh, it's a very old pull request. The db query top key.
for example, was introduced there, but take this PR with a grain of salt, because it's a very old one, and most of the things there are…
Somewhat out of date.
I…
Sergey Sergeev 00:57:14 Yeah, again, the whole idea for the Retails plan is to, measure duration for…
Both embeddin and, Fuer.
the vector DB search for DB search.
So, we can see the whole operation duration. And, again, it will be…
An estein for embodying call, and for search call,
the question is, do… do you want, to set some of the attributes, like embedding a provider on the span, and, vector IDB provider?
So, we can, have cosmetics
And be able to split by those attributes and by those dimensions.
Liudmila Molkova 00:58:14 Oh, well, I think this… this is… Interesting. So if, like… The abstractions here.
They don't consider retrieving as embedding plus database call. They consider it as a retrieval, so Google search is also a retrieval.
So what the span shows, you don't know.
Sergey Sergeev 00:58:37 So Retail is just DB search, right?
Liudmila Molkova 00:58:43 So the abstractions here are not, like, any search. DB search, Google search, Any kind of retrieval.
And under it, you could have embedding call.
But it's a child's pen. You don't know whether it's the… like…
You don't necessarily know if there is embedding under, or if it's a…
semantic search, and it doesn't need embedding. If it's keyword search, it doesn't need embedding.
Sergey Sergeev 00:59:17 Yeah, and that's the difference, I think, between ZDB search and retrieval, that retrieval is specifically an embedded call, and then followed up by,
DB search.
And basically, to group those two operations to provide that logical unit for retrieval.
I… I think we're still missing, probably some examples,
what exactly it means in terms of telemetry for those frameworks, and maybe even some code samples which show this is one chain retrieval, this is one index retrieval, maybe I missed it,
Josh, but… Probably it will help to show if it's the Fink at all.
Liudmila Molkova 01:00:19 Yeah, we are at time. I was just looking here, and I… essentially, what they say, it's just any kind of retrieval. I'm not sure if you… if you… at this level of obstruction, you would know
Whether it includes embedding or anything like this.
Anyway, happy to continue the discussion,
Let me know if I can help.
Sergey Sergeev 01:00:42 Yep.
Thank you. I think the action item is basically to provide those examples and to clarify.
Aaron Abbott 01:00:54 Thanks, everyone.
Liudmila Molkova 01:00:55 Thanks.
Aaron Abbott 01:00:56 Talk to you later. Later.
