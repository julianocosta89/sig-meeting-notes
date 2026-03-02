SIG: LLM Semantic Convention WG
Date: 2025-10-14
Duration: 69 minutes
Zoom Recording URL: https://zoom.us/rec/share/2Z4hH97M352kHgbINrBSI3COgt6vu2C39QDwDxj3ieSLv7BWSQCjsGZ0YTe-JQ5r.smwgxWbB0TEZh8tG
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:11:56 Hi, everyone.
Josh Bonczkowski 00:12:00 Hello.
Dat Ngo 00:12:02 Hello!
Liudmila Molkova 00:12:07 Good to see you! Please, if you have anything to discuss, please add it to the agenda.
Surya Teja 00:12:16 Hey, hi, guys.
Liudmila Molkova 00:12:19 Hello.
Surya Teja 00:12:21 Yeah, I'm coming here for the first time, so I don't know what is going on, but glad to be part of this.
Liudmila Molkova 00:12:27 Yeah, great to have you. So, how we usually run it, we have some, time, like, the agenda is open to everybody. You can find the link in the notes, and I'll send it in the chat in a second.
Surya Teja 00:12:43 Thanks.
Liudmila Molkova 00:12:44 You can add your topics if you want to,
And, we will spend a few minutes going through the project board. We'll…
usually reserve a little bit of time for folks to introduce themselves, so if you want to have a quick presentation, I don't know, a few words while you're here, what brings you, what… what's interesting.
It would be a good time to introduce yourself, and then we'll go through the discussions, which normally includes reviewing some parts of, some changes, or maybe having discussions on some hairy topics.
So, while people are joining and filling the agenda, let's spend a few minutes on the project board. I have quite a few things in new issues.
Let's see what we have…
So I… I think there are… Some discussions here.
Perhaps we should move it to… to do?
It's not something…
I don't believe anybody's working on it, on any actual PRs.
Sergey Sergeev 00:14:13 We could not reach out to Danny or anybody from the ABM from that group, unfortunately.
Liudmila Molkova 00:14:20 Oh, okay.
Sergey Sergeev 00:14:20 Anybody owns a coal can… Can figure out how to reach out to that group, so we can…
Basically break down those big tickets.
Into smaller pieces.
Until it will be realigned with what Roan ID presents.
It would be great.
Liudmila Molkova 00:14:43 Thank you.
Yeah, so we are…
Essentially, Sergey, do you, do you know about the combined efforts between Microsoft and, Cisco? Is there any progress on this? And, what… like, do you still have the call between you?
Sergey Sergeev 00:15:09 Yeah, we still, haven't, calls, sometimes.
During the week, and, it was iterative.
Progress on different stuff which was proposed, but which was not… Yet implemented, so…
Evaluation results, was one of the items, which was…
Part of that discussion, but, overall, I don't… E…
If you have anybody from Microsoft on this call.
But we discussed last week that we will be filing GitHub issues for each
Item which was proposed, so it will be easier to track.
I… don't see…
At this moment, anybody from the… oh, I see Nagumar, but it's… I think it's a different group.
In Microsoft.
Yeah, so… The conversation's still going.
Liudmila Molkova 00:16:17 Yeah, I wonder if we should have this call public, so we can give it a link to Danny.
So… I can, set up another,
time on the calendar, up in tele calendar, and we can have a Zoom
And meeting minutes and whatnot would probably be… meeting minutes would probably be in the same dock as this one.
Sergey Sergeev 00:16:45 It would be great. It would be great. If… yeah, I think public call at this point is…
Probably the best, because we…
have, way more people trying to contribute, like Michael here, from AWS, and… So on.
Liudmila Molkova 00:17:04 Wonderful. So, let's do this.
Sergey Sergeev 00:17:08 Especially if you can reach out to Danny and get any feedback.
Liudmila Molkova 00:17:14 Yeah, so I… what I can do, I can make sure the information is public, and then he has a chance to see it and, join the call, right? But, or anybody from the IBM,
And I can ping folks from the ABM.
What is the time that you have your call scheduled?
Is it the regular one?
Sergey Sergeev 00:17:40 It's, Monday and Thursday,
In the morning. I think, find something which works for you. I think you…
And we will try to join, or somebody from the team will try to join.
Liudmila Molkova 00:17:56 Let's just start with the time you have, and we can evolve it if people start joining.
Sergey Sergeev 00:18:01 Yeah, it's Monday 9am, and it's,
Firstly, 9AM, which conflicts with Python.
Sick. So we need a different day anyway.
Liudmila Molkova 00:18:13 Okay, so let me start with Monday, 1AM, Pacific time, and .
Sergey Sergeev 00:18:20 Sorry, it was 9am Monday, but, 1AM works too.
Liudmila Molkova 00:18:27 1PM, sorry.
Sergey Sergeev 00:18:29 Yeah, right now it's 9am to 9.30.
Liudmila Molkova 00:18:35 Yeah, where did you see? 1PM?
So now it's not Monday, 9am, To 9.30 a.m. Pacific.
Okay.
Pavan 00:18:57 I think me and Shipra have been trying to reach out to Danny separately and to give them links on what we have been discussing so far, and I believe…
We have, done that, but, like, it's been, like, no response from them.
So, even though they mentioned they would want to Get in touch with us.
We haven't seen that so far.
Liudmila Molkova 00:19:26 Yeah, that's fine, right? So we need to make sure they have the opportunity to join. If they don't join, that's… that's not up to us. We've done our best.
Okay, so I'll follow up, I'll create,
meeting, and I'll share the invite on the… sorry, I'll share the information in the chat.
Okay, so I'm going to put it to to-do. We know it's important, we're going to work on it, but it's still not active.
And I think this is the same…
And… This is the same.
I think we exhausted our… small, trash time frame.
And we have plenty of people here, so if anybody wants to introduce themselves, say what brings you here, anything else, please go ahead.
Surya Teja 00:20:45 I can go first. So, hi, I'm Surya. I have been working on adding some span linking and span strategy, span tracing for OpenAI in, Java,
instrumentation, so I was curious to see what is going on here, so that, if I can…
reach out to anyone when I'm having doubts, when I'm adding the tracing or span, stuff for OpenAPI, so that brought me here. And also, I saw the board, and I saw that there are a few Python tickets that need some help, so I thought, being no…
Here, I can help on few things which are…
small, because I'm not well-versed with the semantic conventions, but I can help with the coding part. So that was the reason for me to join this call, just to be a part of this community.
Liudmila Molkova 00:21:38 Nice! Thanks for coming here.
We have some folks, from Alibaba Cloud who contribute to Java instrumentation. They usually come on Mondays every other week.
I don't think there was a call yesterday, there will be one another week. But other than that, if you have questions, feel free to reach out. The first part… the first… the place to find
Support would be the Slack channel. I think it's linked here.
So if you have questions or doubts, feel free to pause there, or send, and I know you can always reach out to me, I'll try to help. If not, I'll try to find somebody else who can.
Surya Teja 00:22:27 Thanks for that.
Dat Ngo 00:22:28 Yeah, I think I'll do a quick intro, too. Lumila, I don't know if you know, like, me and… me and Xander are almost always on these calls, but we also wanted to just say hi, just so you have a face to the name, and but my name is Dat, and also Xander is also from Arise. Just wanted to do a quick intro, because I don't know if you've ever seen my face, Lumila, but…
We work on Arise. Arise is, obviously we're in the AI observability eval space, kind of the largest player here, but we know how important this space is, but we also just wanted to do a quick intro. So me and Xander are always here, Ludmila, so just know that we're…
We're always here, and you know, I just want to do an introduction, so you're not like, who are these two guys who are always here but never say anything? So, just know that we know this space is important, and, thanks for everything that you do for this group. So, just wanted to do a quick intro.
Liudmila Molkova 00:23:12 Thank you, and thanks everybody who also contributes a lot to this group, and great to… I know your face!
Now and before, thanks for coming, and it's always great to hear your perspective on anything.
Dat Ngo 00:23:25 Perfect.
Liudmila Molkova 00:23:30 Cool. Anyone else?
Nagkumar Arkalgud (Microsoft) 00:23:33 Hey, Radmilla, nice to see you again. Nakumar here. I work for Microsoft, and the reason I'm here is because I'm working on the Python, repos to update based on the latest, Gen AI hotel spec.
And we had a question that probably needed more discussion with this forum, and that was around, the…
Workflow span for a multi-agent.
kind of a sample. So the idea being…
Whenever there is a complex agent with multiple agents involved, with a handoff-like pattern, when the original agent does not
Get the control back.
And it just hands off to another agent. We need a way to group those traces and spans into a common parent.
I think it's easier with, like, server-side tracing, but then if the agents are only using SDKs and we don't have any server-side tracing, building this
parent, It's fine.
which I guess is called Workflow Span. That's what I heard in the Thursday meeting, and I'm here to talk about that if anyone wants to.
had an opinion, or if we are still in, like, the spec stage of things, I just wanted to know more about it.
Liudmila Molkova 00:25:00 Yeah, that's a great topic. I… let me add it to the agenda.
And I think maybe 15 minutes would be a good time frame for it.
Nagkumar Arkalgud (Microsoft) 00:25:10 Yeah, I mean, I don't have much to show other than, like, old PR. I'll link it in the chat. This is for OpenAI agents in Python.
So we… the plan there is to create a new repo.
And I think this still needs a lot more changes, because we decided to name it as V2.
But… Yeah, the idea is having an overarching workflow
as a parent, multiple… multi-agent. The handoff sample, for example, when you run that handoff sample.
it creates, if without a parent span, it creates, like, multiple, like, hey, you know, one assistant, Spanish assistant, concierge, and different blocks without a single parent. And having that parent would probably help us.
Group them all together as one run.
Liudmila Molkova 00:26:09 Yeah, so let's just dedicate some time to this, right after we, and let… I've just added to the agenda, let's… let's take a closer look.
That's how we usually roll, right? So, if you want to bring anything up, feel free to. You can come here to brainstorm how to do this. I can help from general open telemetry perspective.
Or.
Nagkumar Arkalgud (Microsoft) 00:26:32 Absolutely.
Liudmila Molkova 00:26:33 Yeah, so feel free to just add things and reserve some time.
Cool! Anyone else want any introductions?
Cool.
So then, let's move on to the open PRs.
Embedding constermentation.
I'm not sure what's the state of it?
Okay, there are a bunch of people who started reviewing, and nobody approved yet.
And… it seems Ricardo is still reviewing, and it's… I also need to take another look. It's just mechanically…
The trivial change that adds embedding.
span, to OpenAI instrumentation.
There are a lot of changes, but they're trivial.
I don't think I… I… I… if we should…
Discuss anything in particular, and it's just up to… us to review.
Okay?
So let's take a tough line.
Is Aaron here yet?
Okay, let's postpone this until Aaron comes.
What else do we have? Invoke agents, pan, documentation beyond remote agents.
Okay, this PR… we have Invoke Agent Span that records invocation for
We're the agent, and we wanted to clarify that if it's the framework.
Then the spend kind should be internal rather than client.
And I approve? Oh, sorry, I commented, I think it looks pretty good with some minor suggestions.
so, if you want to take a look, go ahead. Other than that, it seems pretty… to reveal.
Okay…
new attributes to track Gen AI session. Ivan, do you want to talk about it?
Pavan 00:29:22 Yeah. I think we have been sort of discussing a little bit, like, back and forth on that. So, the idea was that the current genaiiconversation.id doesn't necessarily track, like, multiple traces that
Relates to, like, our multi-agentic,
Session, that you may call it, like, you know, from start to end, which sort of, tracks, like, not just conversation flows, but
a multi… multi-turn, you know, agentic, you know, communication as well. And one of the things that we wanted to actually do is that, given the session.id is actually within the,
you know, registry, the open telemetry registry. We were wondering if that would be, like, a good semantic match, because, you know, a session could contain multiple conversations, and, it basically, you know,
would be, you know, the right approach to sort of do better correlation and, you know, ensure that we are able to also track cross-agent coordination as well. And when me and, you know, sort of the Splunk team were discussing
there was a case to sort of rename it to workflow.id, which
You know, if it sort of helps to ensure it doesn't overlap with the
you know, some of the work that the browser-Sig team or, you know, other groups are doing, happy to do that, but we just wanted, you know, something to essentially be, like, a separate,
field that would track, like, multiple conversation… sorry, multiple traces, you know, that…
belongs to, or rather, you know, that would be a session in some sense. Like, you know, what a session is, I think different people have different perspective on that, but yeah. I don't know if, I…
sort of explained it in the right manner, but I tried to answer any questions that folks had in that PR, but happy to do that
you know, Nova as well.
Liudmila Molkova 00:31:46 Yeah, so I think we need to answer the question what the session is. And if it's a workflow, it's one thing, right? If it's the
Okay, so what current session ID is? So, let's imagine you have, some conversation.
And maybe there is another conversation.
So, currently, the session ID is something that exists in your browser. So, for example, you… I opened some…
R.
Oh.
That's not what I was going to do. For example, I opened, my browser, went to ChatGPT,
And then… Sorry, aye.
That's amazing.
Pavan 00:32:48 Fox.
Liudmila Molkova 00:32:49 Parent, yeah.
Pavan 00:32:50 Yeah, sorry. I mean, one thing that we wanted… I wanted to sort of understand is that, isn't sessions, like, sort of persistent across, like, all contexts, computing contexts, not just browsers, or is this, like, sort of field only strictly limited to the browsers itself?
Like, session, we use it, you know, in various different
scenarios, right? So, like, a full end-to-end flow could also be, like, a session. I mean, even though
I understand that this term would be more applicable to, like, a browser-based session, but… You know,
it may not necessarily be limited to it, I think.
Liudmila Molkova 00:33:36 Yes, Sergey, go ahead.
Sergey Sergeev 00:33:38 Yeah, I just wanted to reiterate on some of the thoughts we had in the past. So, session ID is used by end-user monitoring, for example, when you have,
A session on, in a browser, or in…
For an application, basically, and it may be multiple interactions with the server, remote server.
And, conversation ID, or thread ID, I think, another term, is something, to glue together multiple… multitrone, interactions with…
AI agent. So, for example, you can have one question asked from the browser, then you can ask another question in the same session, in the same chat.
from your mobile device, so session ID will be different.
Yeah, and, I think we, we roll into,
Nakumar's question about workflow, because workflow is something we are considering to connect multi-agent interactions, which may start from one agent.
And, not necessarily the response will be from the same agent, or it may be no response.
I think you have 3 different things here.
Pavan 00:35:11 I think the concept of session is actually sort of, you know, accepted by multiple providers, like Arise, you know, Langfuse, and a couple of others, where they use that to sort of track
or rather, keep a track of multiple traces, even though, you know, workflow in line train or land graph perspective is sort of used for something else. So I just wonder if there is some ambiguity there.
Which could cause some issues, but…
Sergey Sergeev 00:35:47 Yeah, and another challenge. So, the examples I saw were where you basically said some,
Header, for example, in your request.
session ID, and then you manually extract it. So, I saw those examples, I don't know if there is a…
Any protocol, multi-agenic protocol, which automatically propagates.
that attribute.
Probably there are some, so it will be very helpful to hear from people on call and from Aries themselves.
If, there is a standard in any protocol, I don't think that MCP
propagate something across the ERPC boundaries.
So, I think… Yep, go.
Liudmila Molkova 00:36:40 The context propagation, maybe we can separate for now? There are means… I don't believe there is anything default in the MCP, but the semantic conventions for MCP, have PR for… have an example for baggage, using baggage, too.
propagate this kind of stuff. But maybe we can focus on, workflow via sessions? It sounds like Arise has a notion of session, maybe that, or Xander, can you shed some light? What is it?
Dat Ngo 00:37:12 Yeah, we can… or go ahead, Xander, I saw you go off mute, go ahead.
Xander Song 00:37:16 Or I can… Yeah, it really just is a conversation, is all. So it's just,
a user makes multiple invocations of an LLM, they're intended to be part of a single conversation, or a single
interaction, and we capture them every session. They all share a session ID attribute.
And the point of that is just to create a grouping that is higher than a trace. So there… you can think of them as groups of traces that are all
Related to the single interaction back and forth, a single conversation, and being the…
Or the typical example, but not being, like, being kind of a somewhat more general notion than that.
Liudmila Molkova 00:37:55 You're right, so if I come back 2 months after to some past conversation, it would…
be the same as my old interactions with that rate.
Xander Song 00:38:04 Yeah, I assume so.
you could certainly build the system that way, right? In terms of, like, if you've saved a chat message history for a long time, kind of thing, yeah, I think that would probably be the way that the behavior would work.
Liudmila Molkova 00:38:18 And do you have some other thing for the workflow? Like, for the multiple interactions?
Xander Song 00:38:25 A global task that multiple agents are solving, or something similar?
Not… I'm not really sure what y'all have in mind there. In terms of, like, sessions, I think we really just think of the session as just, like, an interaction between
An assistant, and the user.
Dat Ngo 00:38:48 Yeah, like, a session is maybe a collection of traces, and the purpose of that is sometimes people want to run evals.
across multiple traces, right? So, like, people want to ask, like, at any point, was…
the customer frustrated in this conversation, right? And so the idea is you actually need to collect up a set of traces, those input-outputs. Maybe it's human AI, human AI. Sometimes it's in agentic workflows, it's human…
AI, AI, AI, AI, AI, and then it finally comes back to a human, but the reality of it is, yeah, a session is a collection of traces, and the reason why you need that
kind of logical organization is because a lot of people in the industry see the value of zooming out and being able to run evals across many, many collections of data, if that makes sense.
Sergey Sergeev 00:39:36 they would be acceptable to use workflow naming for single turn, basically when something starts multi-agentic workflow, and just to call it workflow, and have a conversation ID… have a conversation naming for
What you just described as session, basically.
When you have, multiple trees, basically, interaction.
with AI agent, which may happen from different, devices. So, one starts from browser, continues on mobile phone.
And so on.
And do you guys set this, session ID, manually in instrumentation?
Xander Song 00:40:30 So there's a… there's a session ID attribute that we have.
And in terms of, like, the workflow stuff, yeah, I don't think we really have any, like, workflow-specific conventions. We have…
Yeah, not to say that we couldn't, but I'm not sure that we've…
yeah, we haven't really explored that too much. You know, we have… what we have are the notion of, like.
Different kinds of spans that are… different kinds of, like, open inference spans in particular, that…
For different kinds of operations.
And then what might be called a workflow would just be composed of many different kinds of these.
Sergey Sergeev 00:41:09 Yeah, for example, how users consume it, do they have to annotate something with specific SDK from…
Promise from Open Inference, How does…
Xander Song 00:41:23 So we provide…
Sergey Sergeev 00:41:24 session.
Xander Song 00:41:25 Yeah, yeah, yeah. We provide,
So it is a span attribute, and we do provide context managers that will
just in Python, for example, that will…
Add this… add that particular attribute to any…
Span is created within the context.
Does that kind of address the question?
Sergey Sergeev 00:41:50 Yeah, yeah, yeah, it makes sense, so, but…
Again, so it means that, let's say you have a user who uses a LendChain application, a LANGraph application, so they will need
To make some code changes, basically, to annotate some,
Let's say, agent invocation with that session ID, right?
Using the U.S.
Xander Song 00:42:17 of… yeah, so Langchain is, like, quite…
quite difficult as an instrumentation package. I think maybe many people here on the call are familiar with it, just because they don't natively use OpenTelemetry, so there are a lot of challenges inherent in language change, and in particular, like, the context manager that we offer just won't
interact nicely with Langchain. Langchain happens to have their own set of things that they basically call
there are, like, 3 names for it, and I forget what the 3 names are, but they're, like, they have 3 names that they basically allow you to pass in as arguments to their SDK. So the names are things like conversation ID, session ID,
group ID or something like that, don't quote me on that.
And what we do under the hood inside of our auto instrumentation is we basically convert those…
those applica- those conventions, which are basically the same concept that we have for session ID, and we just convert it into our particular openness attribute.
So basically, like, when someone's doing Langchain, we just ask them to
pass in the langchain-specific session ID argument as you would if you were using
just blank chain with… with Blanksmith.
And we'll pick it up and convert it to what is needed for open inference.
Liudmila Molkova 00:43:39 Erin, go ahead.
Aaron Abbott 00:43:42 Hey Al, sorry I was a little late to the call today. I've been listening for a few minutes, and
I… I hear us talking a lot about instrumentation here.
But I think some agent frameworks have, like, you know, a first-class idea of what session is, right? So, like.
At least 80K, Google ADK, which I'm pretty familiar with.
It has this kind of built-in idea of session, and there's different session managers you can plug in, which would be, like, SQLite Database, or…
you know, like a Google Vertex-managed, Session storage, so…
I don't know about all the other frameworks, but it's, you know, just something we can model pretty naturally, I think, from ADK.
Sergey Sergeev 00:44:31 Does it make sense to have just separation between a general session and GAEI session?
Liudmila Molkova 00:44:41 So currently, as Pavan noticed, it's not limited to browsers, but it's limited to end users, right? So these are all activities and actions executed by the end users.
If, like, in the current definition.
if I go to the chatgypt.com, if I open 5 conversations, they will be along to the same session, because this is the unit
rail use and monitoring relies upon, right? So, when I'm working in my browser and I interact with a specific website, here is my flow.
And it… I would imagine it would be hard to change.
And it sounds uncontroversial to stamp session.
ID on the GenAI spans, if it's available, but it doesn't seem to be helpful for GenAI scenarios. It's something orthogonal.
Xander Song 00:45:44 I could maybe hop in here, too. I think when we were considering the session ID, like, we actually looked at this, and we thought that it is exactly the same concept that we think of for session ID. The reason that we created a new session ID attribute was really that this one
we thought that it was likely that we might want to have… to kind of have additional session… session attributes in addition to IDs, such as, like, session.user or something.
And that was, like, kind of the only reason. But when we looked at that, like, experimental hotel.
session ID, which I'm not sure the status of it, if this is still experimental, but we basically thought this is exactly what we kind of want.
Yeah.
Appreciate it.
Liudmila Molkova 00:46:27 Okay, go ahead.
Aaron Abbott 00:46:29 Yeah, like, the reason I brought up the 80K thing is, like, it seems like that would conflict, potentially, when you have multiple, when the agent framework has the concept of session itself, right? Like.
The browser session, as far as I understand, would necessarily be tied to, like, one tab.
or sorry, it would be tied to, like, one tab, or certainly not to multiple, like, browsers, but you could, in theory, have multiple people talking to the same agent, like, if you share a conversation with somebody else, right?
Liudmila Molkova 00:47:03 Right, there are multiple agents that… it's unrelated to end users at all, and have the same session.
Aaron Abbott 00:47:09 Yeah, potentially. I mean, I think there's definitely some overlap, but I don't think it's necessarily the same thing.
Pavan 00:47:16 If the, if the agents also operate sort of headlessly, where there are no message threads or, you know, conversation structure in some sense, then, like.
either session ID or, like, you know, workflow ID, if ever it would need to be renamed, would sort of help to keep track of all of that. So, it wouldn't necessarily be tied to just the system-to-user interaction, but rather what happens
Behind the scenes, in order to get the appropriate answer to… back to the user.
Liudmila Molkova 00:47:54 Yeah, it sounds like we are…
Blowing into the workflow discussions as well.
So we can probably merge those two topics.
so… maybe we can talk about session various workflow? Because it sounds…
Like, we need a notion of some block of interaction between AIs, multiple AIs, and human, maybe?
And…
This block is… we can call it workflow, we can maybe call it session, maybe we can call it something else, but we need to define the granularity of this block and, like, describe it somehow.
Sergey Sergeev 00:48:39 Yeah. And we can abstract from the names for a little, and just step back, and let's say there is no, some practices which happen right now among providers like RISE. Can we define characteristics of
Thus.
three different things, I think. It's still… session is something which is set by browser, It's an important characteristic.
And conversation ID is something which is maintained, either by the client or by the server, different implementations.
And workflow is some unique characteristic that is set and propagated by multi-agentic systems.
As a unique… characteristic of… That single unit of, work.
Maybe it will be worth to, just, to not discuss the names, but to discuss
What exactly are the unique… characteristics COVID.
Liudmila Molkova 00:50:10 Can we answer a simple question to start with? Is workflow different than the conversation?
Could there be more than one conversation in workflow, or could there be, Workflows that are…
Multiple workflows in a conversation, or multiple units.
Sergey Sergeev 00:50:37 So, again, I was thinking about, conversation is, specifically multi-turn interaction with an agent.
And, basically maintaining, the same conversation history, chat history.
And etc. Maybe happening between end user and an agent.
Liudmila Molkova 00:51:02 Yeah, is it different than the workflow?
Sergey Sergeev 00:51:05 And workflow is, specifically the distributed execution
And interaction across multiple agents, including human agents, or,
basically for AI agents, and which…
is one turn, basically, from a user. So, user executes a request, so some process starts, an AI workflow.
And it basically runs for… Long period of time.
And, is not connected, to conversation, so it may be part of single turn.
Interaction within a conversation, but… Not necessarily limited to it.
Liudmila Molkova 00:52:04 So what you're saying, that workflow is a span, and conversation ID is an attribute.
But they… do we need a separate Identifier for a workflow.
Sergey Sergeev 00:52:15 I was thinking about workflow, as a way, to basically to connect, multiple, systems in one, execution.
So it's not only a span, but it's something like trace ID, which can be propagated across RPC boundaries by protocols.
by multi-agentic protocols. The question is if we have an example, in existing, multi-agentic, protocols, like ADK,
Which will require This attribute to be propagated.
across the bundles.
Aaron Abbott 00:53:02 I'm not super sure on the propagation thing.
I think… like, I feel like it'd be helpful if we could anchor on
what, like, some concrete examples of agent frameworks and what they provide.
Because I feel like if we have concepts in the telemetry that don't exist in the application, it would be kind of…
Confusing for the user, so…
Like, I know we also don't want to, like, bike-shed the names right now, which is hard.
Sergey Sergeev 00:53:32 Yeah, I think session, ID, which is set by…
instrumentation from Arise is the closest thing which I know.
exist.
We can call it the session, but,
Xander, can you, so, Rice, folks, can you…
post some example in, the Slack channel.
Where… where we can see how, basically.
your session ID is being propagated.
Xander Song 00:54:14 Across context boundaries? Across…
Sergey Sergeev 00:54:17 Yeah, yeah. Service Founders? Yeah.
Xander Song 00:54:20 Yeah, I don't know that… I mean, I can certainly look. I'm not sure that… I have…
I can look in the docs. I don't… I don't know that it's any different from how…
other attributes would get propagated, though. I don't know if that makes sense, but, like,
I think you would just stick it in baggage, and it would just… and it would just carry over, right? I think that'd be the idea.
In terms of, like…
I mean, there's the question around, like, should… should session ID be allowed to do this, or…
To propagate across context mappers.
Short responders.
Pavan 00:54:57 We have some examples in our SPK as well, which sort of does this exact thing that you mentioned, Xander. We can also sort of link that as well.
Xander Song 00:55:08 Yeah, I don't… I don't see any reason why I couldn't.
I think it's probably fine to do so.
Liudmila Molkova 00:55:18 But I think…
Xander Song 00:55:18 would mainly just be with, like, vanilla OTEL APIs, Sergey, if that makes sense.
Like, I don't know that we have, like, special affordances to make that, like, automatic, if that's the… if that's what you're after.
Sergey Sergeev 00:55:36 Yeah, I mean, my understanding was that you need to have something on the recipient part, extracting that from the baggage and setting it.
Xander Song 00:55:46 Yeah, yeah, yeah.
Sergey Sergeev 00:55:47 So…
Xander Song 00:55:48 That would be it. I don't know that we have affordances that make that automatic, if that's what the question is. And maybe we should, I just… I'm not sure that we've actually…
Encountered a lot of…
I have not… I could be wrong, but I have not heard of, like, concrete asks for
that specific feature. That being said, I'm not sure exactly
how deeply used sessions are sometimes. I think it's a part of the product that people
Kind of discovered later.
but, I mean, I could see it being… needed.
I could see it being needed if you have, like, more complex systems.
And you want to be able to just, like, get insight across service boundaries.
Liudmila Molkova 00:56:34 Assuming the session and conversation are the same.
The conversation will be propagated in one way or another by the user.
Anyway…
Xander Song 00:56:45 Yeah.
Sergey Sergeev 00:56:46 Session and conversation.
Liudmila Molkova 00:56:51 Or a rice case, because for them, it seems they are the same.
Sergey Sergeev 00:56:55 April.
Xander Song 00:56:55 They are the same. Like, we don't have anything called conversation ID, we just call it a session ID, but, like, the canonical
Case for sessions or conversations.
But yeah, I agree, like, yeah. I think we… yeah.
It would just be via, like…
So you have baggage and stuff, so you have hotel APIs that someone would have to set that up.
Liudmila Molkova 00:57:23 say that users in multi… in distributed agents' case, they propagate conversation across agents somehow, and we don't need to do, essentially.
anything, as long as conversation ID is available to instrumentation through, I don't know, the specific SDK.
Xander Song 00:57:44 APIs.
Yeah, I think that's my thought as well. I'm not sure that there… I'm not sure I see offhand what would need to be specifically done for sessions with respect to context propagation.
If that's your point overall, that's what I think what you're saying?
Liudmila Molkova 00:58:00 Yeah, yeah, I'm trying to understand what… what does the, like, unique part of the workflow that's not the conversation ID, and I see… now, Kumar, you turned your camera on, and you are the author of this topic, so maybe you'll share some thoughts?
Nagkumar Arkalgud (Microsoft) 00:58:17 Yes. So, a conversation ID, when I think of it, it would be, like, an interaction between an LLM
And maybe the user, right? Like, one interaction has one conversation ID.
Now, Aaron posted a link about Google's workflow agents, and there is… parallel agents.
Where I assume each parallel agent will have its own conversation ID.
Now, when you have a workflow of con… or will it have the same conversation ID? Aaron, correct me if I'm wrong, I'm not sure.
Aaron Abbott 00:58:50 Yeah, you would have the same session ID. So, my understanding of this thing is it's basically like a flow control in the agent instead of letting the LLM decide, it's kind of just like a hard-coded, you know, you will take this sequence of steps.
And then each… each part of the… like, each step is bottled as a separate agent, but they're all working together on the same,
conversation ID.
Nagkumar Arkalgud (Microsoft) 00:59:13 Okay, yeah, I mean, if conversation ID is the parent, then I'm okay with that, like, I'm just…
concerned about other frameworks, but I don't know of any others. One that I have used mostly is the handoff pattern.
And that is where…
that's the problem when the whole problem started of, like, oh, how do I group everything under one span?
But if everything uses the same conversation ID, then it should probably be pretty straightforward. Or a session ID, like, one ID, which is…
The same amongst the complete execution.
Aaron Abbott 00:59:56 I think I would dig…
Pavan 00:59:57 I…
Aaron Abbott 00:59:58 Oh, sorry.
Pavan 00:59:58 I'd try.
Aaron Abbott 00:59:59 Sorry, I was just gonna say to that, I would… I can dig in a little more, in, like, the multi-agent use case. This was all kind of, like, in process,
single… Single process, multiple agents, but yeah.
Sergey Sergeev 01:00:11 Yeah, and in general, so again, if you execute within some server boundaries where OpenTelematy instrumentation is available, trace ID will be that unique
Identifier.
Liudmila Molkova 01:00:26 I don't think so.
Like… Yeah, it's… Probably… Very soon, that we will start dealing with async flows in agents, because it's inevitable.
Sergey Sergeev 01:00:42 And human in the loop is async flow.
Liudmila Molkova 01:00:44 And the moment, like, when I go in to check, let's say, status of something.
I'm starting a new trace.
Because I'm initiating it from my site, right? I cannot inherit trace from something stored in a database or anything.
Sergey Sergeev 01:00:58 Yeah, but then the challenge is, back to what Nagumar mentioned, it may be a different conversation ID. So again, conversation ID is some identifier on an agent.
So you have that conversation ID, because it's conversation between, something, like, end user and an agent.
If the agent hands off to another agent.
It becomes a client of that agent, remote agent, where it maintains its own conversation ideas.
So, it may be,
I see only this contradiction in general.
With fusing, just first agent conversation ID.
Liudmila Molkova 01:01:48 I wonder, like… we are 10 minutes away from, Dent. So, I wonder…
If we can approach it from this angle.
Like, we have a conversa… the conversation is pretty clear, what is it?
Maybe there is some wiggle room, but we know what it is. We have an attribute for this. How far can we go without defining new things?
what I've heard so far, it sounds like
We can imagine some edge cases where it will be necessary.
But those… Or kinda advanced.
And we definitely need something there, some unique ID to…
group this thing. We don't clearly know what is this.
Maybe we can try our best.
without it, and then once we identify, I don't know, once we identify the framework that needs it, we would have some…
more… Context to decide.
Aaron Abbott 01:03:07 Lumil, you're specifically talking about which one? Because we already have, like, a conversation ID, right?
Liudmila Molkova 01:03:12 Yeah, I'm saying how far we can go without defining workflow ID.
Aaron Abbott 01:03:16 Like, if we try, how…
Liudmila Molkova 01:03:18 How reasonable would it be?
Aaron Abbott 01:03:21 Yeah, plus one.
Pavan 01:03:25 I mean, are you looking for some examples of, like, implementations, or rather case studies, or something like that?
That need the new attribute.
Liudmila Molkova 01:03:42 Yeah, now, Kumar, go ahead.
Nagkumar Arkalgud (Microsoft) 01:03:43 Yeah, other than the ID, in terms of, like, creating a parent span for it.
I mean, and I guess the ID would be the content of the span, but just having a parent
Span for a multi-agent workflow, or are there any more thoughts on that?
Liudmila Molkova 01:04:04 Yeah, and I think, yeah, we should define one. The only question would be whether it's the, like, the…
invoke agent span and arbitrary span? Does it… what is it? So, I think we should have a span. It may be defined in semantic conventions, if it makes sense.
Nagkumar Arkalgud (Microsoft) 01:04:22 Yeah, I like Keith's PR. Let's open.
The Keats issue, I would say.
So we can probably take that and… Well, Connor.
Liudmila Molkova 01:04:35 Okay, sounds good.
So let me write down… So, essentially, what we're saying that we definitely…
We need a pen for the… .
Keith Decker 01:05:06 My PR talks about having a span for multi-agent stuff, but I intentionally left off this whole conversation about an ID for async operations, too.
delegate that over to, like, Pavin's PR.
Or issue.
Liudmila Molkova 01:05:22 Yeah, and we… we can define a span, we can add the notion later, and the attribute on the span.
Cool. Does it sound reasonable to everybody?
Cuo.
We have 5 minutes left to walk through Aaron's PR.
I think, Aaron, do you want to talk about it? Do you want to… is there anything specific we can help with?
Aaron Abbott 01:06:26 I think it's pretty, pretty much good to go. I don't know if floating around,
Yeah, I don't think Marcela's here.
So basically, I addressed, you know, Alex's comments and stuff. It's a little different from what you approved of Mila, if you want to take another look, but…
Basically, we have 3 parts. There's blob, there's URI, and then there's File, which would be something like referencing pre-uploaded file from OpenAI files to PI.
Huh?
And there's… there's a couple discussions around, like, null ability, and optional… optional types, which I… I made a follow-up issue to discuss.
But other than that, we added,
a modality enum, which captures, kind of… we left out document for now, but it captures, you know, image, video, or…
Audio.
And… Yeah, that's pretty much all there is to this one, I think.
Marcel mentioned that he might be, working on, like, a proof of concept, so we could hold off.
I'll merging, for a few days until he has something, but…
That's pretty much all there is.
Liudmila Molkova 01:07:37 I think Alex wanted, somebody to approve it?
Aaron Abbott 01:07:43 Yeah, that was Marcella.
Liudmila Molkova 01:07:45 Oh, Marcel, okay, wonderful. So,
Aaron Abbott 01:07:48 Yeah.
Liudmila Molkova 01:07:49 Okay.
nice, so then, I'll… re-woke…
my approval, and hold it back until, Marcel approves.
And I'll also take another look, so just nobody would accidentally merge it, because it formerly has all the, means to merge.
And… Does… does he know?
Aaron Abbott 01:08:19 Yeah, yeah, yeah.
We're chatting on Slack, so I can ping you once Marcelo is done, too.
Liudmila Molkova 01:08:28 Okay.
Sounds great.
Aaron Abbott 01:08:33 Yep.
Yeah, I don't know if we triaged the issue about using, like, missing, like, differentiating null from not required in the JSON schemas.
We can chat about it next week. I… I don't have a super, super strong opinion on it, but I filed, like, a follow-up issue so we can… people can share their thoughts.
Liudmila Molkova 01:08:56 Okay, is it in the semantic conventions?
Aaron Abbott 01:08:59 Yes, semantic invention should be GenAI.
It's like the fifth one down there.
Liudmila Molkova 01:09:13 Oops.
Aaron Abbott 01:09:15 Yep.
Liudmila Molkova 01:09:17 Oh, okay, we didn't get it,
I'll take a look, I'll try to share my thoughts on the issue.
Aaron Abbott 01:09:30 Okay. Cool.
Liudmila Molkova 01:09:33 Then, thank you all for the great discussion, and see you next week.
Aaron Abbott 01:09:38 Yep. Till.
