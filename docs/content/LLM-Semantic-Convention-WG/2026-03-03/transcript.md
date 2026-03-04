SIG: LLM Semantic Convention WG
Date: 2026-03-03
Duration: 71 minutes
============================================================

## Zoom Recording Transcript

**neil yashinsky** 00:37 Hi, everyone. Oh, look, un… expected bot! Recording an already recorded meeting.
I guess it's not quite recording yet, but it's attempting to record an already recorded meeting.
**Liudmila Molkova** 01:14 Hello. Hi, everyone.
**neil yashinsky** 01:19 Hello?
**Sergey Sergeev** 01:21 A…
**Liudmila Molkova** 01:23 There is this funny… Both, James Fellow, not Baker.
I'm sorry, James, we're not giving you permissions, but I don't know how to tell you that.
**neil yashinsky** 01:34 Sadly, I'm pretty sure I could be wrong, but I feel like there's a better than 60% chance that we've attempted to tell James's note-taking bot this before in other SIG calls.
**Liudmila Molkova** 01:46 Absolutely, that's why.
**neil yashinsky** 01:48 Oh, I think it'll disappear.
Oh, like an auto-reject or something?
**Liudmila Molkova** 01:52 I don't… I don't… I can't kick him out for it.
it out, but yeah. Sorry, James, can you please just watch the recording? It's recorded.
Okay, let's do…
usual… Triage while we are waiting for people to come.
Oh, pretty back to agenda on Mondays.
It's nice.
I just want to make sure, you folks, how are you doing there? Maybe we can… I can add a topic, and we can just chat how things are going there, what you folks are working on.
Anything we need to know here?
And feel free to add your name to the agenda, please add topics, and let's go to the project board.
So I want to put this one on the agenda.
Hey, what else do we have here?
They're not showing traces. This is… 5, 10… Bug?
Who owes the code owner for this thing?
Nakumar, are you here?
**nagkumar** 04:09 Yes.
**Liudmila Molkova** 04:11 G… Did you see this one?
You're the component owner on the agents. Do you know by heart if we are supported yet at all?
**nagkumar** 04:23 I don't think we would do the system prompt
But yeah, I'll take a look at it.
**Liudmila Molkova** 04:32 Thank you.
Are you the member of Attorg?
I don't know.
**nagkumar** 04:39 Honestly, I don't know how this works, but this, package, I created it, along with, other folks on the…
team,
Because there was no tracing library. Lighton helped me create this. There was no tracing library for, OpenAI agents, so we created it.
**Liudmila Molkova** 05:02 So I'm pretty sure you can, your… meet the OpenTelemetry org member
requirements, and I just cannot even assign the issue to you.
Could you follow up, and maybe request a membership? It's actually super easy.
Kuna.
**nagkumar** 05:23 I'll do that.
**Liudmila Molkova** 05:24 And everybody else, if you have a few contributions to ATEL, code, comments, issues, discussions.
PRs, you are eligible.
And I… can support you, you need two people to support you who are existing org members.
So you go to the community repo.
you do organization membership request, and you just fill out some links, and you need to find two sponsors. Ping me, I will probably be able to sponsor you.
Oh, sorry?
I'll just put it in the chat here.
**Trask Stalnaker** 06:18 So you need, two sponsors who are approvers or maintainers of Repos.
**Liudmila Molkova** 06:25 Oh, thanks, yeah.
**Trask Stalnaker** 06:26 So, Aaron or myself could be a second sponsor.
**Liudmila Molkova** 06:35 Thank you, Trask, for the clarification.
Okay, what else do we have on the project board? Oh, and it's listed in progress, interesting.
let's… And… Couple of minutes on the no status ones.
Agent version and agent role.
I think we already have version.
And we could not agree on what role is, if I remember correctly. It's just a name.
I think we can probably close this one.
Okay, so I'm going to,
close this one.
Trask, you send too many peers. Not that they might.
Okay, we are out of the box in our agenda, we still have a full board, but let's move forward to
our topics.
This is the time to introduce yourself if you want to. If you're new to this group, we would love to know about you.
Okay.
If you change your mind, go ahead and add your name to the agenda, and we will be happy to talk.
Ankit and Trask.
Do you want to talk about… Edge and Servers Pen.
Is Enkid here?
**Trask Stalnaker** 09:39 I don't see him, but I just pinged him.
In case he's able to join… He had…
**Liudmila Molkova** 09:50 She had a… Should we… oh.
**Trask Stalnaker** 09:51 Yeah, we can move, we can, go on in case he's able to join.
Otherwise, I can talk through.
**Liudmila Molkova** 09:59 Let's give him a chance to join, and yeah, let's move on to…
Let's put some other topics first.
So… we have this pie, the span. This PR that's, seems it's… Lowe's?
I… So, Sam, this question, I saw, Aaron, you approved, and I saw your comment.
But I wanted to see if there is anything… that… that you… Wanted to bring.
**Tao** 10:42 I also just left a comment, but it's… it's…
Kind of similar to what, what's been discussed.
**Liudmila Molkova** 11:00 I see.
So, what… how… how… what made me…
why I approved it.
So there is an API that's not Invoke Agent, right?
like, this is a specific API, it's a structurally different span than Invoke Agent.
It could contain just one agent underneath.
Like, it's an edge case, probably. You probably wouldn't…
Have one, but there is no way to guarantee that you are not orchestrating one agent.
Does it make sense, though?
**Tao** 11:47 Yeah, I think it makes sense. You know, if you have a workflow, and that workflow only has one agent, that's totally valid, but I think in our definition.
in our main definition, which we could say something like, represent a workflow that orchestrates agents, right?
maybe that would be less confusing, because the first time I read this, it was saying, you know, a workflow is a sequence of operations, including LM calls and tool calls.
The first thing that came to my mind was, that's an agent.
Right?
So, maybe… You know, a workflow is… a sequence of…
agent invocations, right? It could be one or many.
But… We shouldn't mention… I don't know, because this seems to be a complete overlap of invoke agent.
**Sergey Sergeev** 12:55 Yeah, I can provide some, justification for separate types and the thinking here. So, workflow is more of a grouping of operations, and specifically in one chain, it may be…
So is it… Because everything is a chain, basically, in a blank chain. So, workflow provides…
an option to define that top level with input and output, and the difference from the agent that it…
it may be reused, so sometimes you want to monitor the workflow Which agents can invoke.
And the workflow is basically,
a grouping of DNA operations, each agent
can call. You can use sub-agents and etc, but…
Workflow is more, predefined.
Predefined flow of, different GenA,
operations, I would say, this way.
And, again, in some frameworks, like WankChain, this is just a helpful, abstraction.
In general, it's,
yeah, we can make everything an agent, and agent can be a tool, so we can simplify. In the end, everything can be simplified to just two calls, if we keep,
**Tao** 14:44 Generally, isn't it?
Yeah, not generalizing it. I think it's just… Whoa.
Say a user is reading this document, and it is trying to… the user is trying to decide if it should… if the user should use invoke agent or invoke workflow.
Right? It seems like both would be appropriate.
Right.
So I think this is the discussion that I… that that's similar to the one you just closed?
**Liudmila Molkova** 15:16 Yeah.
**Tao** 15:16 Yeah, I think… I think he raised the same point as I did.
like… in Invote Agent, it's kind of like a specialization of Invote Workflow.
But it… We don't… we don't provide the guidance on which one we should use, depending on the situation.
**Liudmila Molkova** 15:38 I see, so we are saying that if you… Cannot.
**Tao** 15:48 I'm just…
**Liudmila Molkova** 15:48 distinguish Invoke Agent from Invoke Workflow.
You… should not report in workflow… in Vogue Workflow. You should only report in Vogue Agent.
But maybe if it would be helpful to spend more time describing what in-work work… what in-work workflow is, or can you suggest maybe some… some version of this?
Tax, that would be… That would provide clarity.
**Tao** 16:22 Yeah, I, I can, I can think, think,
think about something. Maybe it's just the distinction between invoke workflow and Invote Agent, right?
But right now, it's… I think it's not super clear.
**Liudmila Molkova** 16:42 Yeah, so will you make a stab and try to suggest something?
**Tao** 16:48 Yeah, I would do that.
**Liudmila Molkova** 16:50 Thank you.
Cool.
Anything else on this?
**Sergey Sergeev** 17:24 Just, just one, wanna ask if you can,
Do it in a timely manner, because this pull request stays open for a while, so… Yeah.
**Tao** 17:35 I'll do it right after this meeting.
**Sergey Sergeev** 17:39 Thank you so much. No, this is helpful.
**Liudmila Molkova** 17:48 Cool, thank you. So then, moving on to Ankit Tantrusks. Ankit, I've seen you, you're here. Awesome. Do you want to present? Do you want me to present?
**Trask Stalnaker** 18:00 I think we have now, Ankit, listed this diagram.
So we can talk through…
There are cut… so there are three questions we have. One about the async modeling, so let's…
Kinda talk… About that first.
I think we got good input last week, and so kind of wanted to confirm this view.
that… If the invoke agent… if the server invoke agent span was async, then we would use…
Span Kind Consumer.
If it was not async, we would use Span Kind Server.
And in both cases, we would parent… do natural parenting, not use links.
Do you think… oh yeah, go ahead.
**Liudmila Molkova** 19:06 It sounds… Yeah, the… to… to things. We might…
It's probably the first example of something being conditional, either consumer or server.
**Trask Stalnaker** 19:20 Yeah.
I was worried about that.
**Liudmila Molkova** 19:29 Into the problem, though.
**Sergey Sergeev** 19:32 I have a question for this use case. So, when you send something, I think, so what is the common pattern? Do we still maintain the same trace?
Or they would be… When you purchase something asynchronously,
do you… so specifically for multi-agent, now, if you have a question, if you send the response,
to the agent. Does it know the trace context? Does it maintain somewhere the trace context, or it will be processed as a new request?
**Trask Stalnaker** 20:18 So in this picture, at least, the trace ID would flow all the way through, and you would parent everything.
So they would all be part of the same trace.
As opposed to… Messaging, for example.
We're messaging consumers because we have that batch consumer concept, and you have multiple traces flowing into one batch consumer.
We'd… Use links instead of… So it gets a new trace at that point.
**Sergey Sergeev** 21:04 Yeah, I'm… I'm, I'm really wondering, how it,
Yeah, if you have an… if you have an example of something like that working, especially when the server boundary is belonging to a different company, if you… if your client makes a call to a server, let's say the server is,
something like, ChatGPT… So, your client, makes a call, and,
**Trask Stalnaker** 21:38 Do we even have, a clear…
**Sergey Sergeev** 21:41 Boundary of trees away.
Because asynchronous communication between the server and the client, for example, the server can do the thinking and processing.
On the backend, but you can send a correction message.
Which will be applied, so I'm really wondering where we have that trace boundary.
In this use case.
**Trask Stalnaker** 22:11 So, we're… the… It's a really good question. I guess…
we're not… I… I think that's a, orthogonal question. We do have that, that has come up in the spec.
A bunch lately of, like, trace boundary as distributed traces flow to other organizations, and when to start a new trace or not.
So I suspect… I want to say this is the same situation.
Let me dig up a spec link, though.
And I can add it here.
Because this is a… a very… this is a good example. This particular use case is a good example, since a lot of times the server is…
Run by another org.
**Sergey Sergeev** 23:11 Yeah, in this example, the server is Microsoft, the client is abitary application, so on the server, you probably don't want to accept the trace ID or other OpenTelemet attributes sent in the header, so I think you
Want to sanitize it, for security reasons.
And if so, maybe it's the protocol Level… something.
Which can be the uniting.
attributes.
**Liudmila Molkova** 23:48 So if… if we don't trust the trace context from the upstream.
we would still link it. I now trust you don't want to use links, but we would still have means to correlate.
And on the server side, it would still be… hopefully, the server should the best effort to keep it one.
trace, right? It cannot even report the span if the server side
Span, if it's not the single thing.
**Trask Stalnaker** 24:19 Well… You have to know where to…
Yeah, to send it if it's going to the same,
For one person to be able to see the full trace.
**Liudmila Molkova** 24:32 Yeah, Erin?
**Aaron Abbott** 24:35 Yeah, I was… I was kind of wondering, like, do we need to have a convention here? Like, what happens if we don't do anything? So, for example, like, say these go in a message queue. We already have messaging semantic conventions.
And then from the… from the part where the agent runs in some compute environment, like, within the server.
It would just do the normal, you know, invoke agent stuff.
But the parent would be, like, instead of being an HTTP span, it might be a message span, which would have type consumer, right?
So I guess I'm wondering, like.
What if we do nothing, and we kind of just let the implementation details show up in the trace?
Yep.
**Trask Stalnaker** 25:20 Yeah, that's a good question, and ties to, the third topic that, third question that we had, sort of, of, Lydmila had asked about whether client address, client port should be on…
the… Invoke… agent server span, since it would be captured by this HTTP server span on the diagram.
And So, I guess the, it's… Still…
can be nice for the… like, that can add a lot of noise, right, to your traces to capture all the HTTP spans and the messaging spans all in the middle.
If you know that
you know, it's really what you care about is kind of the logical layer of the GenAI operations.
**Aaron Abbott** 26:23 Okay. So, so, like, is this from the perspective of IO and everything?
and there's, like, an org boundary, maybe? Or is it, like, a SaaS is serving a… or, say, something like OpenAI Remote Agents, right? Like, is,
Is the goal to surface a specific
Trace tree that looks a certain way to people, or is it to kind of show the…
Like, operational internal details.
**Trask Stalnaker** 26:52 Yeah, it's a good, I think within this, on the green… Part, the server boundary,
Right, if you modeled all of that the… from the server, because probably there is a message queue in between that server queue and the,
the invoke agent server span.
And so, certainly that could all be modeled.
I'm not sure what… And yeah, to… to…
question of whether… I mean, I think…
What we would like is to not…
muddy the… the user's trace. Like, this is more for use… end users, view of the traces, I guess, to answer your question, as opposed to operationally, where
You would care more about those internal details.
**Aaron Abbott** 27:52 Okay, Ankit, I think.
**anksing** 27:55 Yeah, and I think I want to bring up, like, a couple of points. One was about the first question about having, like, whether you want to have, like, have HTTP span as a parent, and I think Tras already covered that about
it might be there, it might not be there, depending upon what role you want to have in your public-facing, you know, customer-facing traces, right? And the second one I think I want to bring up is, even for the client spans right now, like, we do show a certain structure of the spans to kind of make user understand how your agent came up with the response, right?
like, there's a possibility you could make those spans even more verbose in the sense of capturing every HTTP interaction it might do, right, under the hood, or any kind of loop that it runs through, right? That's possible, but then we still try to keep it at a
place where it's more easily, like, understandable, right? And I know that's a very hard line to define where it is.
But at the same time, on the service, it becomes a little more complex on that front, right? And having that complexity of how
services are kind of managing that. Like, it depends on, like, how much service wants to expose that at the same point, right?
**Aaron Abbott** 29:13 Yeah, I don't… I don't think I have the answers, but,
I guess, if the goal is to, like,
Expose a view to the client, like…
Is… are we answering the question from the perspective of client and the server being, like, completely…
You know, like,
like, it… I think it sounds like we are doing that, we just want to see what the client…
wants to see, and then I'm kind of confused why the async is even, something that we're discussing versus
Just kind of showing the nice view.
**anksing** 29:47 I see.
So…
I think we also want to show, like, yeah, you can capture this on the client side, but we also want to show, like, how service came up… service came up with those response rates, and then, there's not always a case where client might not be instrumented. That's possible, like, highly possible.
And then, in those cases, you don't get really, like… So, what we want to achieve is…
having observability on how agent works, like, if it's working behind a service, right? To some extent. So, which you obviously, like, hard to rely on just the client instrumenting everything and being able to give you that, right?
Which is not foolproof, in a way, right?
**Trask Stalnaker** 30:29 Aaron, if I can rephrase, I think what you're asking was why… why it matters, then, if it's async or not, from the, like, the customer's perspective there.
**Aaron Abbott** 30:44 Yeah.
**Trask Stalnaker** 30:45 And I think I'm… I mostly agree. I think the only thing that we're talking about that changing between the two would be the span kind.
And that's… Only because of the definitions in open telemetry around spankind, and whether
I have to always go back and read those, because they're… they're confusing, but I…
thing. The server one means that there's, like, a client waiting for the
Like, in the way that they're nested, the server one should be basically nested under the client one, whereas a consumer would then say, hey, this is…
Async, and now it's offset there.
But… we haven't… I… Can't say we've really tackled this in OpenTelemetry.
Ludmila, do you… do we… do you know of any… existing…
I mean, this is kind of different.
**Liudmila Molkova** 31:59 We do have consumers in messaging, but this is messaging.
And I'm… I'm thinking in the background, like, what… what is… What?
Who would it hurt if we always called that server?
Like, yeah, it's… it… it's… It smells a little bit, but in practice, does it… it's probably better.
Shake, the answer is probably doesn't… it doesn't matter on the server. The async nature does not matter on the server. It only matters on the client.
**Trask Stalnaker** 32:50 I see what you're saying.
**anksing** 32:57 Curious about, like, when you say it doesn't matter on the server, like, there's some details which changes with that, right? Like, for example.
your HTTP server, span, if you have, like, that kind of
finishes even before your age. Probably your… Invocating server span starts, right?
Or, I know, not much of a big deal.
**Liudmila Molkova** 33:19 And, I mean, the GenAI span looks exactly the same, regardless how client calls.
**anksing** 33:27 Yes.
Oh, shit.
**Trask Stalnaker** 33:37 Oh, go ahead.
**Liudmila Molkova** 33:42 We are a little bit in the bike shedding detail.
**Trask Stalnaker** 33:45 Yeah, let me, we'll do some more thinking. I think that's a good question that we have to answer.
What would be the harm in… Making that a server-side, so…
I will… will take that action item.
**Liudmila Molkova** 34:09 Thank you.
**Aaron Abbott** 34:11 Cool.
**Liudmila Molkova** 34:13 I'll keep this.
**Trask Stalnaker** 34:15 Yeah, sorry, more. So this one,
What I wanted to ask here is…
What the… if there's a preference for how to…
tackle this in, in this PR, in… So one option is for this PR to just…
stay as is, extending inference client, which is two weird things. A, it's extending inference, and B, the server span is extending client.
But the… Attributes are pretty much the same. I think Anko was… Providing some feedback on that.
Or we could do a separate PR first, basically, to kind of rearrange that hierarchy.
in the YAML, and then come back to this PR.
Totally fine either way, just kind of wanted, To hear a preference.
**Liudmila Molkova** 35:24 It's a long-standing issue that we… we don't even want to invoke agent client to extend this.
**Trask Stalnaker** 35:32 Right.
**Liudmila Molkova** 35:33 And, I think, Aaron, you raised it before, and I totally agree, it's kind of weird.
So…
if you folks are ready to do the refactoring, it would be awesome. I tried to do this, and there are some hairy questions I didn't want too often, but then maybe if there is a demand, let's just do it together.
**Aaron Abbott** 35:58 Yeah, I think the only thing that I kind of came around to, I put a comment at the very bottom of this one, but, like.
or… I've talked to a lot of people, and invoking an agent
And kind of the workflow as well that we were discussing, but it does kind of inherently…
You know, it has an input and an output.
And then that thing probably encapsulates the system instructions, so we might want to leave input-output, but
Some of the other stuff, like model, doesn't really make any sense to me.
**Trask Stalnaker** 36:31 So, that's a good question. So, I mean, model could apply as, like, your… it's your default model for your Invoke agent.
Right? Like, even when I run Copilot locally, CLI, like, I… I can specify You know, my…
My default model, my… all these other aspects that…
Sort of our defaults for the inference call.
**Aaron Abbott** 37:05 Yeah. I guess the question is if that would… if it should be kind of on the…
this invoke agent outer span, or… like, we do… we do put it in the inference calls, of course,
But, like, What am I trying to say?
**Trask Stalnaker** 37:21 Is it duplicative? The question has been… it's basically duplicative.
**Aaron Abbott** 37:26 Yeah, I mean, I think it is a little duplicative. That's not really my concern, though. It's mostly just, like.
if you have Workflow, for example, or in ADK, it's like, you can have Workflow Agent, which doesn't have model.
So there's definitely cases where you cannot have it.
But it's kind of like,
not the input to the component, it's more just, like, a static property of it. So maybe we, maybe we leave it, but…
That's what I'm trying to say. Angate, did you want to…
**anksing** 38:00 Y-yeah, I just wanted to,
Understand, like, is the point of view, like,
Like, in case of an agent, you kind of already define these things and then use them, rather than a reference call where you kind of can go say, I want to pick this model. Is it more about that, or…
Like, if there is an agent framework which can let you pick which model to use, or entry-invocation, would that change?
Just curious to understand.
**Aaron Abbott** 38:30 Yeah, I mean, I think… maybe I haven't thought that hard about it. You're raising good points.
Yeah, I don't know, I think, we can maybe chat about it on the issue. I could probably…
**anksing** 38:47 Yeah, definitely. Yeah, definitely. Because what I'm thinking is, like, when I use GitHub Copilot or another, like, I can switch the agent, like, as I'm doing my conversation, I can switch it in between, right? That's possible. Yeah. And I do that quite a lot, sometimes when…
So…
Yeah, just curious, like, that's what I was thinking of, but yeah, good to chat on the issue, yeah.
**Trask Stalnaker** 39:12 Maybe what we… can do to answer is kind of go back to what we're,
looking at the API, take the span, and what are the different APIs for different,
agents.
And whether they take these parameters or not, and kind of map… map those out to know if they should… if they… if there's even data to be captured on the… that invoke agent call.
**Liudmila Molkova** 39:45 Maybe we can split? I would be excited to solve this problem for clients. And it does not directly affect your first server, and if you can, in the server PR,
Separate the server, and we can have a clean story for the server then.
Just don't inherit from… common stuff. Like, why would changes on client automatically affect Server, right?
**Trask Stalnaker** 40:15 Yeah, so, we would need to… Extract out a common… Attribute group.
use that in both the client and the server.
**Liudmila Molkova** 40:33 We don't have to. You can model the server.
**Trask Stalnaker** 40:38 Oh, not Creative Commons.
**Liudmila Molkova** 40:40 with, first, from client.
And we can just… from that, we can see what's in there.
And maybe we will merge them, because it's just the sugar and the definition, it does not change any conventions at all.
**Trask Stalnaker** 40:59 Got it. Okay, that makes a lot of sense. So, not… not… don't try to extract a common thing
But just create a clean copy for the server, invoke agent server.
**Liudmila Molkova** 41:14 Yeah, and I would encourage us still to solve the original problem. We have a bug, the structural bug.
It's just… Slightly unrelated to what you're trying to do.
**Trask Stalnaker** 41:27 Perfect.
Thank you.
And the last one kind of ties back to our earlier discussion. Lamila, you had left a comment about client address and client port on the invoke agent server span.
And… It makes sense, like, I can definitely see it both ways.
The… But I think the…
And we could also just have it opt-in, as, you know, hey, if you know that you aren't… if you're choosing not to capture the HTTP server span.
Then you can opt in and capture that directly on the Invoke Agent server span.
But they, they are… Important…
Attributes, with all of the security concerns around invoking… Invoking agents.
**Liudmila Molkova** 42:34 aren't… they're… GDPR concerns. I would… I think Microsoft cannot capture user IP addresses, or probably any provider cannot.
Like, opt-in makes sense?
But then, it's always opt-in. You could never capture that.
In practice.
**Trask Stalnaker** 43:02 I defer to Ankit. My understanding is that we… the security folks required that field.
**anksing** 43:10 Yeah, and I think, that, like, the discussion about that thing is still going through Kenosila, but they want to have that information, possibly available once they go through that.
And this is mostly for, like, security purposes.
**Liudmila Molkova** 43:39 Okay, I see…
**Trask Stalnaker** 43:40 We do… we do capture it by default on HTTP server spans.
**Liudmila Molkova** 43:48 Assuming… like, my impression that the main use case for it is that you capture this telemetry for somebody else, and it's an external system.
And you…
**Trask Stalnaker** 43:57 Oh, I see what you're saying. Right, right.
**Liudmila Molkova** 44:03 And you don't have the collector or processing in the SDK on the… in the process.
To actually strip this data.
But anyway, yeah.
So it sounds like you kind of need it. And let's, let's start with Upton.
Would it be a good story?
**anksing** 44:27 I can't defer it to you. Yeah, that sounds good. Yeah, opt-in is good. I think we got all this, yeah.
Some, like, legal sealer requirements that has to come to us about, like, asking customers for how to opt in, but yeah, that sounds good.
**Liudmila Molkova** 44:43 Okay, move on.
**Trask Stalnaker** 44:45 Opt-in Anka means that, I mean, you… it doesn't mean that
It means that the person instrumenting can…
**anksing** 44:54 Yeah.
**Trask Stalnaker** 44:54 Choose to opt-in and capture that.
**anksing** 44:57 Yeah, yeah, exactly, yeah.
Yeah, and actually, what I was referring to was more about, like, in the Microsoft ecosystem than, like, having Sila, like, on the server side, allowing us to kind of capture this information right then, which requires some customer concept, yeah.
**Liudmila Molkova** 45:17 I love it when security collides with privacy.
**Trask Stalnaker** 45:21 Excuse me.
**Liudmila Molkova** 45:22 It was awesome.
Both top…
**Trask Stalnaker** 45:25 priorities.
**Liudmila Molkova** 45:27 Yes.
Should we move on to orange?
**Trask Stalnaker** 45:32 Thank you for all the discussions.
**Liudmila Molkova** 45:35 Thank you.
This friend.
**Aaron Abbott** 45:40 Yes. I don't think, we can probably make progress right here.
But I just wanted to… I don't know if Mingle looks at these meetings, but…
We have a couple comments here, and some PRs implementing this.
in, Google Gen AI, so… just wanted to drop it here and see if we could…
you know, maybe move it forward. I think we're pretty close, it's just, A couple small questions about…
Things that were missing.
**Liudmila Molkova** 46:10 Can you ping meaningfully? I think he's been on the,
Lunar New Year, holiday, and baby, he's back now, keeping him.
**Aaron Abbott** 46:22 Yeah. I guess it's just, I think it's just some cosmetic stuff. Do we need to discuss something?
No, no, I don't think we need to discuss,
It was… it was pretty minor.
Yeah, just kind of wanted to… Shout it out again.
**Liudmila Molkova** 46:38 If it's minor, could you maybe create the follow-up issue and approve it, and then we can merge it and follow up, or is it something that would be…
Important.
**Aaron Abbott** 46:49 Yeah, so basically, like, my question here was, is there anyone who doesn't use JSON schema? Because we left it kind of loose?
So we… we could address it in a follow-up, but it would make the… it would make it more strict, which I guess is okay as well.
But it might be quicker to just answer on this PR, so I'll ping him, and if we can't resolve it quickly, then yeah, follow up works for me.
**Liudmila Molkova** 47:13 Or maybe if it's something trivial, if you leave a suggestion, and he is not coming soon to update it, we can just commit it and merge it.
**Aaron Abbott** 47:24 Yep. Okay.
**Liudmila Molkova** 47:28 Thank you.
**Aaron Abbott** 47:29 Yeah, it's been a while for this PR.
**anksing** 47:34 We'll also take a look at this, I think it's gonna probably affect a few of the other telemetry that we do, so…
**Liudmila Molkova** 47:40 Awesome, thank you.
**anksing** 47:41 Different fillet, I should say.
Thank you.
**Liudmila Molkova** 47:45 We are at the bottom of our agenda, but only because I didn't do a good job updating it.
Though anyone has a topic to discuss, otherwise I want to spend some time on, reviewing peers.
Okay, cool.
**Aaron Abbott** 48:07 Sounds good.
**Liudmila Molkova** 48:07 Dad.
Let's see, we have a couple of trivial PRs that I hope we can just go ahead and…
Merge.
Okay.
So, there is one we're doing here for… the exceptions?
It's across semantic conventions. The… Span events are being deprecated.
And, we want to provide an alternative as log-based event.
So the only thing this PR introduces is saying that if you
instrumenting the client, whatever genre client operation, and it throws Record this event.
Where's the… Traditional exception attributes.
And it should be warning.
And that's it.
Instead of span.recordException.
**Aaron Abbott** 49:25 I think I might be a little out of the loop, but is there a reason that we have to have
An AI-specific event for it.
**Liudmila Molkova** 49:34 It's just the… the… Practice we came up with that every convention would have a
The reserved attribute name.
And…
you could still treat them as one thing by grouping it as just the ends of this exception, but also, we could add AI-specific attributes here.
And what it's saying that, you can also provide configuration option to populate exception events with the attributes captured on the corresponding span.
So, the structure of this event
Will depend on the instrumentation, and then the name should be specific.
Charles, did you want to touch something?
**Trask Stalnaker** 50:23 No, no, just that, that, I mean, that was…
I mean, that's a good question, something we kind of went back and forth on. The primary reason is to have an event name.
For it, and not just…
Use exception, or kind of have a generic exception event name for everything.
**Aaron Abbott** 50:51 Okay, yeah, I… I… maybe I'll… I don't wanna…
get too in the weeds on this one. Is there… is there, like, a, root issue I can look at?
**Liudmila Molkova** 51:06 Yeah, it's time.
**Trask Stalnaker** 51:08 VR.
Yeah, we would love feedback on this.
**Aaron Abbott** 51:15 Okay.
**Trask Stalnaker** 51:16 Because, yeah, I mean, related, as I've been implementing in Java, like, it's…
Not, like, it would be easier to have just, say, event name as exception everywhere, like, from a generic codebase.
And…
So what I ended up doing, most recently was just taking instrumentation names, since we have that already.
I'm doing instrumentationName.exception.
As the event name.
**Liudmila Molkova** 52:04 Cool. So it might be, not as…
trivial as I hoped, but it's great that we have the discussion for this.
What else is trivial that we can bite? This is super trivial. I noticed that we don't have, the response model and embedding spans.
And if somebody can give it a second review… It would be.
Awesome.
**anksing** 52:36 Sir, and one quick question on the other, the exceptions.
**Liudmila Molkova** 52:39 Oh, sorry, yeah, yeah, yeah, go ahead.
**anksing** 52:40 So, I know right now, like, for capturing, errors on the spans, we use error.
Type and error.message, so this is replacing error.message, or is it replacing the entire thing?
**Liudmila Molkova** 52:54 No, the… it does not replace anything, so error.type stays, it's on the spans and metrics to capture the… if error has happened. But sometimes you also want to record the… the…
Exception details, like the stack trace, and the message, and exception type is not the same as error type, actually?
At least.
Usually.
And… than… It's the extra log you can report.
Yeah, actually, Don, I don't… should… we are saying should, right, so we should report. Jenny Instrumentation should report it.
**anksing** 53:36 I see.
**Liudmila Molkova** 53:36 Absolutely.
**anksing** 53:37 I was looking at the documentation where it talks about the error, so it says error.message attribute is deprecated.
CSM.
New, or maybe I'm coming back to this after a long time.
**Liudmila Molkova** 53:49 Our message is deprecated, but it's not used on GenA conventions at all.
**anksing** 53:55 So… yeah, it's not… okay, yeah, that's true.
Okay, so then just the error.type has to be unexplored, okay.
So for any more information, you have to record this via this event, right?
Like, this is a log-based event, right? For exception messages?
**Liudmila Molkova** 54:17 Yeah.
**anksing** 54:17 Okay, got it.
**Liudmila Molkova** 54:19 The… the exception type, message, and stack trace, or… Record it as exception event.
**anksing** 54:28 Just like a subset setting, this will be a new change as well, so…
Probably have to capture this and make sure we are following this.
Cool. Okay, that's good.
Thank you.
**Liudmila Molkova** 54:42 Thank you. Cool. So this one is to review all the embeddings, and… we have another…
thing… oh, it's actually pretty, pretty much ready. Aaron, you had some comments… About the thinking spans.
**Aaron Abbott** 55:11 Yeah, I haven't kept up on this one.
**Liudmila Molkova** 55:14 Oh, I think… Where we ended up with, is that
Multiple systems have the concept of Thinking and reasoning.
But Claude Antropic does not expose… this on the…
usage in response, it has some separate endpoint report details. So, essentially, it's not applicable to Anthropic, but applicable to everything else.
And the ask here is to…
Put this attribute on inference span.
For everybody, with a caveat that it might not be reported for some systems.
Yeah, I think it's just waiting for a follow-up from the author.
**Aaron Abbott** 56:06 Okay.
**Liudmila Molkova** 56:10 Okay, there are a bunch of other…
4 requests here. We went through this.
I also wanted to ask Karin…
About this one, somebody's taking over adult PR from Michael.
Is this… does it align with you? Does the person… does… does the work.
**Aaron Abbott** 56:33 Yeah, the cocoa?
Yeah, yeah, they're a Googler. They don't work with me, this is kind of just, something they're doing in their free time.
So I can… I can take a look, I think one… Yeah.
I'll take another look at this one.
**Liudmila Molkova** 56:55 Okay, thanks. Yeah, I will be waiting for… for your, or Dylan's feedback before I… I…
For my opinion. But yeah, you approved it in the past, so I hope that… It's… Let's see.
**Aaron Abbott** 57:11 Thank you.
**Liudmila Molkova** 57:13 Thank you.
So, we have 3 minutes left, and I don't think we'll be able to achieve anything meaningful.
In the 3 minutes, any parking thoughts?
Cool, then thank you. See you around.
**anksing** 57:34 Thank you. Thanks, everyone.
Good day.
**Trask Stalnaker** 57:38 I…
**neil yashinsky** 57:39 Absolutely. Thanks, everyone.
