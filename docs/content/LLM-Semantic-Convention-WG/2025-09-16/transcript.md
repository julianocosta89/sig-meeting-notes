SIG: LLM Semantic Convention WG
Date: 2025-09-16
Duration: 86 minutes
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 03:20 Hey, folks.
**Bruno Baptista (IBM)** 03:24 Hello.
**Shuwen Pan** 03:26 I don't…
**Sergey Sergeev** 05:58 Yeah, I don't see Lyudmilu yet, maybe… Let's wait a few more minutes, but if Redmiu is not here, probably we can go over the agenda.
liquid from… Say it again?
**Alex Hall** 06:15 She's missing it today. I guess she didn't actually post this.
Publicly.
She posted on a channel, Jenny, I approve this.
Saying she's on a work trip, she has to miss the call.
**Sergey Sergeev** 06:28 Oh.
**Alex Hall** 06:28 The day slash tomorrow.
Right now, basically.
I actually thought that we would see Aaron and that he would take over.
**Sergey Sergeev** 06:44 Thank you.
Can you see my screen?
**Bruno Baptista (IBM)** 07:10 Yes, I can…
**Sergey Sergeev** 07:12 Perfect.
**pratibha moogi** 07:23 Everyone.
**Sergey Sergeev** 07:25 E.
Aaron, do you want to take over the meeting?
**Aaron Abbott** 07:33 Yeah, whatever. I mean, you can share too, that's totally fine.
I'm guessing, Limo's not here yet?
**Sergey Sergeev** 07:44 Yeah, she's missing today.
**Aaron Abbott** 07:47 Oh. Okay.
**Sergey Sergeev** 07:48 I just copied the agenda from… The next topics… And Tim… Yeah, I think there are some standing… Agenda items, like, pull requests to review.
**Aaron Abbott** 08:11 Yeah.
Yeah, we usually start with the board.
Also.
**Sergey Sergeev** 08:16 Okay, I missed the last week, probably you are way more up-to-date, so please, Probably you will be best to drive the meetings.
**Aaron Abbott** 08:29 Okay, no worries.
Yeah. So, also, please add your name, names to the attendees, if you can, and Yeah, please add any topics if you… If you have them.
Okay, cool, let's start with the project board.
We have a couple new issues. I don't know if we covered these last time, let's take a look.
Something was opened last month, I think we… Maybe just added it to the board, Danny, are you here? Do you want to speak to this?
**Dany** 09:25 I'm here, just a sec, I will open my video as well. Hi, hi everyone.
Yeah, so we have submitted this issue. Actually, I'm here with the team, also a few more colleagues from IBM, around the significant gaps that we observe and see around agendic flows.
And observability of aging flows, so this is kind of an umbrella issue for multiple sub-issues, and also follow-up PR requests on adding different capabilities around tasks, actions, agents, artifacts.
memory, and other, you know, key agenda components that are not natively represented.
And we started in small chunks, so we started with tasks.
And specifically for task, we have a set of different attributes that we believe should be added, and, you know, to simplify the adoption and discussion, we split this long list of attributes into categories.
And I think we also already submitted one PR around subset of them that I believe Divya and the team will discuss in more details. And as we go, we will gradually add… you know, there are high-level documents describing these attributes at high level.
and we will provide PRs and address and work with the community to see how to align them. So this is a high-level summary of this convention issue.
**Aaron Abbott** 11:03 Yeah, so we, I think we should discuss this a little more, because we have… I think… A lot of people interested in multi-agents.
And we have some kind of parallel workstreams also with Cisco, Splunk, and Microsoft, so… I'm gonna stick it in the agenda, or you're welcome to add it, and Yeah, we can get everybody's thoughts on that.
**Sergey Sergeev** 11:25 Yeah, I had times trying to find your Slack account, and anyways, how to reach out to you. Are you on… Is this what channel?
**Dany** 11:37 Yeah, so can you please share? I know it was a bit pressure time here, but I'll try to be a bit more involved there and answer more rapidly, and it's not only me, I believe there are several you know, colleagues from our side who will be monitoring and answering questions, and Guangya is also there, part of the work we are doing, so… and again.
Let's have discussion. I think I have answered some of the questions, and colleagues have also answered and provided some of the inputs, but it's just the beginning of the journey. I know it's cross-cutting and very important topic across multiple companies.
And so we are all in the same boat, and we should see how we move this boat into the direction at a proper speed, because this is something really, really highly demanding.
**Sergey Sergeev** 12:36 Okay, it's more how to reach out to you in SWAC. If you are in OpenSilometry Gen AI instrumentation channel, can you just post this pull request so we know how to communicate to you?
**Dany** 12:50 Yeah, yeah, I'm…
**Sergey Sergeev** 12:51 Maybe whether you…
**Dany** 12:52 Yeah, yeah, sure, sure. I will add also, and a few colleagues on our side, so that we can jointly monitor and address this issue. So I will pause also, as they're on this lecture, that you will see.
Okay.
**Aaron Abbott** 13:07 Okay, so if there's… if there's more, we can, we can just add it to the agenda today. Like, I don't know if there's anything else to say on this. It sounds like, Obviously, this is a high-demand thing, but Yeah, should we just… I added it to the agenda, let's see if there's, I guess, more to say.
**Dany** 13:25 Yeah, we can have, again, in some… one of the follow-up sessions, I can, you know, just give a bit more depth or high-level overview of the entire thing, just to share with the relevant people about the idea why we were thinking about this or other attributes.
at high level, and then, as I said, you know, to make it more feasible to consume in there, so we will split it into smaller steps.
And work together to discuss each one of them in more details.
**Aaron Abbott** 13:58 Sounds good.
I think that was everything on the, backlog board, all the new issues at least, so we can get into the regular agenda.
We also, if anybody wants to introduce themselves, anybody new, No pressure, but feel free to, stay hi.
**Harshit Kumar** 14:18 I… yeah.
**Dany** 14:19 words from our side, and maybe other colleagues that will be… I would actually plan to zoom in into the course. So, I'm Dani Moskovich, I'm from IBM Research.
And we are actively working in the area of agent observability analytics and optimization space, trying to help, you know, improve, debug, and maintain agent flows, and specifically, we believe You know, open telemetry is a best, way, you know, best manus for collect relevant information.
And, okay, me and my team is actively involved in this, and together with different.
**Harshit Kumar** 15:00 Different.
**Dany** 15:01 other organization across IBM research.
**Harshit Kumar** 15:05 Mmm…
**Dany** 15:06 And we'll be more and more involved into this thread as well, together with Blangia and other people from our organization.
And… That's all, maybe others who would like to introduce, and I see Harshit right here.
**Harshit Kumar** 15:22 Yeah. Thanks, Jenny. Yeah, am I… am I audible?
**pratibha moogi** 15:25 Yes, that's it.
**Harshit Kumar** 15:26 Great. Yeah, hi, I am Harshit Kumar, and I'm from the India Research Labs, and we work closely as one team with Denny, and I have my other cleave.
I have my other colleagues here with me, Divya and Pratiba, and as Danny mentioned, that we all work in the observability space, especially agent observability, and we believe that, you know, this is a space which is very important given that the wide adoption of agents, AI agents, right? Which is happening around us, so it is something that we should move fast and bring out these capabilities with urgency, yeah.
Thank you.
Pratiba.
**pratibha moogi** 16:09 Hello, everyone. Myself, Pratibha. I've been in this area, observability for a couple of years. I'm part of IBM Research Lab, and we are all working together, Danny and team, to See how, in the observability space, you need different ways to… Surface, different slices and dices of telemetry data, so that The diagnostics, remediation problems can be… done with more effectiveness, yeah.
**Aaron Abbott** 16:46 Awesome. Siddharth, if you have your hand raised, do you want to say hi?
**Siddharth Pareek** 16:51 Hi, good everyone. My name is Sudad Barak. I'm part of the NACA's group, in the central architecture and engineering practice.
What I'm working on is, one, resiliency engineering, so I'm bringing a couple of chaos engineering principles into practice within the bank through AWS, Open… Shift and Java and other tech stacks. That is one stack. Second, what I'm doing is I'm working on, an IA project, and if I have to you know, sum it up in two lines. We're trying… we're building a conversational RAG model, which is sort of an AI assistant for our engineering matrices that lets Our colleagues ask questions in natural language and get insights aligned with our bank-wide engineering, security, and ops OKRs.
That's it, what, from my side, thank you so much.
**Aaron Abbott** 17:57 Okay, awesome, it's great to meet everybody. I think we're a little over the time block, so, yeah, let's get into the agenda, maybe.
I think some of these were copied over from last week, right?
Oh, okay, these are new. Pavan, are you on? Do you want to talk about this?
**Pavan** 18:16 Yeah, I think, Alex had already given some feedback, to this, PR, and thanks, Alex. Sorry I was on, you know, like, sort of, doing some other work, so I couldn't actually reply in time. Apologies. But in… as a highlight, I think one of the key reasons why we wanted a separate attribute to specifically cover the, role.
aspect is, like, our, from our, you know, sort of research and, you know, thinking is that the description is sort of more freeform, not categorical. So, like, for example, in a multi-agent system.
an orchestrator agent would benefit from having a structured role label, for example, like, which role does this agent belong to? You know, for, like, reasoning, you know, filtering, or, like, observability, and the OTEL backend platform as well could significantly benefit from that, especially if we add, like.
agent tick-specific metrics, you know, where it can actually filter by role. Like, in a lot of cases, the description would probably be sufficient, you know, but in many times, you know, given that it's freeform, we probably won't be able to figure out, you know, like.
what exactly is the role, and even though names also could benefit… could sort of indicate the role, given that, you know, it could be arbitrary, there's sort of no guarantee, like, what sort of a participant that particular agent is.
So, at least that has been our thinking in this regard, and, I think Would be interested to see if, If… This resonates with others as well.
**Alex Hall** 20:10 I don't see when we were used outside of, like, a custom application, like, I think semantic conventions are mainly to help with instrumentations.
Libraries being consistent.
And, for example, the thing that's on screen right now, role equals research analyst.
It's called role there, but it sounds like it would fit best with the name, semantic convention.
**Pavan** 20:42 Yeah, in a few sort of frameworks, like, some of the, naming is sort of, you know, interchangeable in that sense.
**Alex Hall** 20:53 Yeah. If we have a thing that's called role, and actually, it's best not… well, if we… if… yeah, if there's a thing called Roll, but you shouldn't use it, for example, for the crew AI role.
That's confusing.
**pratibha moogi** 21:10 So, Alex, generally, in all middleware, the prompt construct, sometimes they have different granularity of their expression, right? So, in case of prew.ai, you have role as a separate field. But generally, from a prompt observability point of view, because it's the most important thing when it comes to monitoring the behavior of agentic system, and it has got different elements, so what you would recommend if we have, you know, a prompt as a… element to support different kinds, right? A lot of research work is happening on different prompt templates, and every element has a role to play when it comes to diagnostics. So, if not in this way, we should have some way to express
**Alex Hall** 22:05 I think that if it's needed, it should be easy to supply an example of when it would be used.
**Dany** 22:11 Yeah, so if I may comment on that, so first of all, I'm glad that the role discussion is raised, because also in our proposal, we do see the value of representing the agendic role.
However, I think this term is a bit abused, and, you know, everyone saying the role of the agent is in context of a single agent.
Well, to me, the agent role is more relevant in concept of multi-agent system, or team, or organization, authentic organization. So, the same agent may… let's say I have a coder agent, yes.
may have different roles in the team, or different teams. And this is important when you try to reflect You know, captures a system that is responsible of delegating the tasks among the agents within the organization or agentic team. So, when… I don't think that, you know, specifically, if you describe the agent role in its sense of goal of the agent, there is no need to edit, and that's why I would argue that adding this as agent.
a role is not necessarily the proper place where I would place it, and what we are suggesting is to add it as an agent role within the team. So, in the context of you defining a team.
And you want to indicate that you have a developer in the team, agent who is developer, or agent who is retriever, or agent who… whoever is it.
And you want to say that this specific agent, regardless of his entire set of capabilities that he can do in this particular team, acts within this particular role, administrator, manager, coder, or whatever, then it makes sense to reflect it and capture it.
And I believe that in multi-agent system, it will be one of the fields, you know, important in the definition of the role that needs to be captured.
My perspective.
**Aaron Abbott** 24:12 If I… I just want to jump in really fast and say, like, It's… it's not super clear to me, like, if these are specific to, like… We're trying to normalize the name, like, some people call it role, some people call it… You know.
Different things and different agent frameworks, like.
It's not clear to me if we're normalizing that, or if we're… Trying to capture a new top-level thing.
like, which problem are we discussing? What to call this thing, or whether it should exist or not?
**Pavan** 24:45 I think if it should exist or not, like, specifically, like, these two examples, where just to sort of show that some of the frameworks actually have the concept of role, but, you know, as what Alex mentioned, it's clear that maybe there's some, you know, like, sort of naming mismatch, where either role here could be description, or it could be name, for example, but in that… in that regard, I think, like.
If you, in a system where you have, like, tens or, you know, or more agents, you know, all doing a specific purpose.
Some, like, the name and description could probably not be sufficient, and so we are probably seeing if there could be an additional role, but the action item is on me to sort of, give some more clear examples here, but… Yeah, that's… that's the idea.
Oh my god.
**Aaron Abbott** 25:38 Yeah, that sounds like a good step, Bruno, do you want to go ahead?
**Bruno Baptista (IBM)** 25:43 Yeah, I want to add something around this.
Role can be also be related with the security framework?
So, in Java, role has a very specific meaning in terms of security.
And usually it's something that is assigned to a person.
I imagine it can be assigned to an agent in the future as well. And, independently of the capabilities of the agent, it's something that you can assign depending on the context. In different parts of the application, some agent might, in theory, have this or that role.
So, just keep that in mind as well.
**Dany** 26:31 Yeah, that's why I'm thinking it's more applicable in the context of a team, where you have to select or specify different roles.
Rather than in context of having a single agent, okay, or only a single organization, which, you know, you just described his capabilities within this application.
**Bruno Baptista (IBM)** 26:59 Yeah, basically, role is different from capability.
**Dany** 27:03 Exactly.
**Aaron Abbott** 27:09 Okay, maybe, Maybe we can take the discussion offline. It sounds like, Pavin, you said you have the action item?
to give some better examples, or maybe update the PR, like, to make the PR more clear.
**Pavan** 27:25 Yeah, sure.
**Aaron Abbott** 27:26 Yeah.
Yep. Okay.
Cool. Let's go to the next one… This is… genai.task.
Divya, are you around? I don't know.
**Divya Pathak** 27:47 Yes, yes, I'm here.
So, yeah, so this PR is a part of the issue that Dani was speaking of few minutes earlier. So, this is a part of introducing semantic conventions for something called as genai.task. So what are tasks? Tasks are fundamental units of work in AI agent workflows. So they basically, essentially capture structure goals, like planning, reasoning, retrieval, etc.
So, this is a part of… this is a… this PR is a part of a smaller… I mean, we are trying to introduce smaller set of attributes as part of this PR, which consists of genai.id, genai.parentid, code.vendor, and, like, task.kind. So, there were a few comments to which we tried to provide some… some of the clarifications to the comments as part of the replies. So yeah.
**Harshit Kumar** 28:41 And there is a… and there's a Google Docs?
**Divya Pathak** 28:44 Yeah, so there's also a Google Doc.
**Harshit Kumar** 28:46 Detailed description with an example.
Why this is important, and how is it applicable?
That's a goal.
**Divya Pathak** 28:55 So we have given an example, So these are some brief descriptions of what each attributes are about, and why, essentially, we need to add them. And an example of, An example which is present below, which showcases how adding these attributes may help us.
**Aaron Abbott** 29:17 Okay. I haven't taken a big look at this, but my, like, immediate reaction is… How is this different from just, like, generic spin?
Especially regarding, like, parent-child relations.
**Harshit Kumar** 29:30 So that is what it is presented as. Exactly, Aaron, that question is answered below as an example, where we show what the spans are and what the tasks are, right? So think of… like, abstracting from multiple tasks a single span, right? So, there could be a scenario where there are 3 or 4 tasks.
3 or 4 spans, and there is a possibility that we can abstract them out into one task. That is exactly what it is doing, right? So it is… spans would still be there, they are still relevant, but this is a mapping from spans to tasks. Denny, you want to add to it?
**Dany** 30:09 Yeah, yeah, I would like to add to it, you know, first of all, to maybe to more clarify this… the concept of tasks. In contrast to spawns, tasks are life elements. They have a life cycle. Tasks can be created Task can be then executed, it can be planned, it can be completed, updated, suspended, and so on.
So, task is an element within agentic systems that may have a life cycle. You may think of a simple task, you know, where, you know, synchronized tasks which are executed as a single step, they are created, executed, and completed, and there's a nicely mapping… you can map them to a single span or reflect them within a single span. But conceptually, they may have… they may have, you know, be more sophisticated in their life cycle, and so that's why it can span over multiple spans and series across multiple traces.
Also, we wouldn't, you know, appreciate that a lot, but that's one point. And the second, like Harshit mentioned, the task Can be an abstraction of the, you know, multiple steps or things that happen within a several, or reflected within the several spans.
So, it's another unit which more aligned with, first of all, also if you see the kinds of types of spines.
They, they, they reflect the different… Agentico on, let's say, non-deterministic steps, usually within your application, that you would like to capture. And another important point is that there are different from another abstraction that we've also to introduce is in Gen AI Action, which task… where task describes actually what needs to be done.
Rather than how it is done. And the action, for example, I'll give you an example. You may have a retrieval task.
Okay, tasked to retrieve some information.
and it may be created at some point of time, and then planned for the execution for a specific agent. The execution of this stuff can be done in multiple ways.
You can retrieve the information by querying the vector database. It's one way to retrieve the information in the agentic flow. You may retrieve the information by applying a tool called… And this would be another, again, retrieval task, but implemented using retrieval action. And finally, you can retrieve the information from the, you know, LLM directly, because it's a common knowledge that LLM can provide an answer, and in this case, it will be represented with the actions that actually reflect the LLM calls. So that's why it's different a bit from SPAN, so SPAN may have a task associated with it or not. It may also have an action that describes how this task is reflected. I hope it answers your questions on the difference between spends And dusks.
**Aaron Abbott** 33:09 Yeah, yeah, a bit. This is… definitely a lot to, to kind of digest, but I… like, I'm really glad we have domain experts here that we can lean into, so what I would say is, I think, is anybody working on the multi-agent stuff from Microsoft and Cisco on the call?
**Sergey Sergeev** 33:30 Yeah, here. Yeah, I think, task, makes sense overall, to me. Action is something new we need to think through, so then again, please, Let's start, Fred, in Swag Channel, so we probably need a deeper dive call, just to review, general IoT use, approach we are doing, where we're trying to define those types, and so on.
We probably need, to add you to that call between Microsoft and Spoonk, where we try to deep dive into multi-agent systems. It's amazing work, by the way, and a very nice, detailed document, so I really appreciate it. So let's sync up and review… Yeah.
Oh, it's…
**Dany** 34:22 I will create a connection on the Slack, and maybe also other colleagues of mine will be on the Slack. And let's, yes, if you have a more detailed technical discussion.
to zoom in on the multi-agent interactions, even single-agent. So we have a broad, both, like you, I believe, in Microsoft, a broad knowledge, both as the developers of the agentic system, but also as those who are developing the system, by the way, all of the instructions that we introduce here, we are trying them by ourselves, so internally, we implement and implement this within the SDK, right? With our agentic developers.
collecting feedback and gradually improving it, and so this is one of the tries. I believe after we work together also with you, we'll further improve it.
to align across, you know, at least several big players on the market, and we'll come with something nice, so let's work together on that.
**Sergey Sergeev** 35:17 Okay, no tools.
**Pradeep Nair** 35:20 for the Genera utility, we were kind of, like, thinking of, like, workflow and tasks, like, where workflow is a collection of tasks, but, like, I also see actions over here, so that's what… so, like Sergey mentioned, we would like to, like, get a little bit more understanding of how…
**Dany** 35:34 Yeah, so let's have a dedicated call. I'll be glad to present at least, you know, the ideas and why we propose this thing. I believe it will resonate well also on your side, actually, on everyone who has developed, you know.
using AutoGen or whatever other framework you are using and experimenting with.
And let's, you know, collectively see how we can enrich it and make it parser. So it's address core things, also, like, memory, And even, you know, artifacts, actions, workflows as well are represented there.
So let's discuss it.
**Aaron Abbott** 36:16 Yeah, that sounds really good.
I think… so you already have a separate call where we kind of go over, like… I think we have, like, 3 design docs now on different conventions for multi-agent systems, so… That seems like the next step to just kind of consolidate the effort and figure out what we all agree on, because there's so many frameworks, there's so many.
**pratibha moogi** 36:35 you know, internal or external, so… Yep.
**Aaron Abbott** 36:39 And then I think Pavan also… oops.
You shared this PR that's kind of… You know, workflow agents, pipelines, like, is this a generic concept?
But I think the discussion still applies to the overall, You know, let's consolidate our effort and all that, so…
**Dany** 37:00 Perfect, perfect.
**Aaron Abbott** 37:04 Okay, cool, yes. Samuel, I don't… I don't know if you're around, Did you want to talk about… the, operation.cost?
**Alex Hall** 37:19 He's not here, but I don't think we need to talk about it. We have talked about it, I'm not even sure why it's been copied here.
**Sergey Sergeev** 37:26 Yeah, it was in the next topics. I cleared the topic by copying it.
To this agenda, so probably we won't be… Getting back to the studio.
**Aaron Abbott** 37:43 And then, so, we have some topics from Mingui, but I don't think they're here, I think it's, maybe from the Asia Pacific call.
Does anybody have any context on these? Or…
**Bruno Baptista (IBM)** 38:01 I wonder if they were copy-pasted from last week.
**Aaron Abbott** 38:05 Yeah, there might be.
Or they might have been from the call, there's, like, a separate time zone call.
Yeah, for this one.
I think we can skip over them then, if, Yeah, I'm not sure. Okay. Maybe… Can jump to this one, then.
This is my PR, I think we talked about it.
maybe a week… yeah, last week, I think? Thank you for the discussion, Alex, I really appreciate it. I think the action items here for me… so just for context, this is the… How to represent multimodal attachments, which could be either, like, inline, or referencing a URI, like… pre-signed URL, or GS colon slash slash S3 colon slash slash kind of thing.
So it sounds like we need file ID. That totally makes sense.
I can add that.
There was this discussion… Marcel left some comments about… Using URI versus file URI.
That's fine, I think we can just work it out on the issue here.
Alex, did you want to say anything about the open topics on this one?
**Alex Hall** 39:37 No, I mean, nothing to say it's not in the comments. We can just use UI for the UI, and… Content for the blob data.
**Aaron Abbott** 39:49 Okay, This one… okay, cool, yeah, you responded. The only other question I had here was, like, on the bytes. Are you okay with that? Are we kind of on the same page there?
**Alex Hall** 40:02 I'm okay with that.
**Aaron Abbott** 40:06 This one…
**Alex Hall** 40:12 Yeah, it shouldn't say Base64 encoded.
**Aaron Abbott** 40:15 Yeah, I need to update that.
To just say, like, the bytes, and then when it's converted to JSON, we get Base64 encoded.
**Alex Hall** 40:23 But something should… yeah, when it's converted to JSON, should get Base64 encoded, but also something should specify what happens when… what the instrumentation captures is a data URL containing Base64, and it sounded like what she wanted was it should actually decode that Base64 back into Bytes.
**Aaron Abbott** 40:42 Yeah, yeah, I mean.
**Alex Hall** 40:43 Or maybe it's fine for it to do either thing.
**Aaron Abbott** 40:49 Yeah, I mean, I think either would be okay.
So, so I was actually curious, like, the OpenAI instrumentations we have, do they… Operate at the level where you might get, just, like, a byte stream before it gets encoded to Base64, or are we doing, like, monkey patching before that happens?
**Alex Hall** 41:07 I don't know how it works, and I don't even know if it captures the images.
**Aaron Abbott** 41:11 Yeah.
Okay, because it just kind of seems, you know, like, if you had something like… I don't know, a framework on top of it that was doing the conversion, it might have access to the byte stream before it gets turned into a data URL, so… I mean.
**pratibha moogi** 41:27 Aaron, quick question, so data could be of any sort, like images and coded images… Any multimedia encoder standards, right?
**Alex Hall** 41:41 That's the idea.
**Aaron Abbott** 41:42 Yep.
**pratibha moogi** 41:45 Okay.
**Aaron Abbott** 41:46 For context, this is just… we're trying to capture, like, what the existing… inference APIs already support.
So, like, I think we've… we talked a lot about Gemini, OpenAI, and I think, Anthropic, they all support something like this.
**pratibha moogi** 42:04 Okay.
**Aaron Abbott** 42:14 So yeah, I'll update this PR with the… to kind of address the comments.
I'll clarify the Bytes comment.
Yeah.
So yeah, I had stuck this one in the agenda, but I think we've talked about it now.
pretty well. It sounds like the… the next step is to kind of take it offline and go through the… Three design docs we have across different people, and come up with, like, a consolidated proposal, so…
**pratibha moogi** 42:49 Yep.
**Aaron Abbott** 42:54 Alright, that's actually the end of the agenda.
I guess we can call it there.
Pavo, you wanna…
**Pavan** 43:06 Yeah, I had another PR, 2594, I think.
**Harshit Kumar** 43:13 like, it was opened a while back, and Ludmila had given some feedback, but I sort of wanted to get some clarity on that.
**Pavan** 43:21 So just as a context, I think, you know, so, we are, you know, working on our OSS library to do, you know, agent tick, multi-agent tick observability, and as a part of this, what we do is we actually, use the attribute session.id to sort of propagate the session context across multiple agents in real time, so that we actually capture, like, a group of traces that belong to a single end-to-end workflow. So, essentially.
you know.
we have been using the OpenTelemetry baggage API under the hood to actually do the session propagation, and we are actually writing a blog that the hotel, you know, baggage authors will sort of reference in some case study. But essentially, the feedback that Ludmila had given was, we wanted to, sort of.
you know, sync with the browser SIG team to figure out what the correlation of the session ID would be.
I sort of fully didn't get the relation between, like, the GenAI namespace and the browser namespace, you know, to sort of, you know, sort of sync up on any, you know, differences there. I don't know if… That's something that we can actually, talk about here, or if, if I should take it offline with, Lord Mela and others.
**Aaron Abbott** 44:59 Well, yeah, I mean, I think the first thing is the GenAI conversation ID, like, there's this thread here. I agree with that. That was my understanding, was this was for exactly what you're describing.
**Pavan** 45:09 And, like.
**Aaron Abbott** 45:10 In particular, it doesn't have to live within a single trace.
If you had, you know, multiple turns of a conversation, each invocation is typically a trace, just by the nature of how much the APIs work.
And then, when you resume that conversation, you generate more traces with the same conversation ID.
And I, I think… Does that kind of make sense? Do you think conversational ID still doesn't work?
**Pavan** 45:35 I mean, in some sense, like, R… understanding and experience has been that if the agents actually are completely distributed and isolated, but they are part of the, let's say, for example, multi-agenting system, the conversation ID sort of tracks the chat, you know.
terms, right? Not, like, the full, like, sort of orchestration. Especially if there's no conversation structure between the agents, and if they operate sort of headless, then like, the, conversation ID probably wouldn't be the right sort of attribute to sort of keep track of the, agentic interaction between one another. The conversation ID is sort of meant to, you know, sort of, get the user interaction. Is that not the case?
like, if some agents actually interact with the users, right? But if some agents are oblivious, and they don't have actually any interaction with the users, but still we want to capture the full end-to-end, you know, interaction of the multi-agented system, then would it still makes sense to use conversation ID, because even if they don't actually have any User interaction, element.
**Aaron Abbott** 46:54 Sergey, do you want to jump in?
**Sergey Sergeev** 46:56 Yeah, I remember the last time we were thinking to look into a workflow ID and some representation of the workflow instead, not necessarily even GenAI, because basically what happens, we are executing some distributed workflow.
And it, don't have to be even, GenAI-specific.
Maybe this is something to look up.
Pabban, do you think that workflow ID will work?
**Pavan** 47:33 Nope.
Yeah, I mean, like, anything that sort of captures the whole end-to-end, you know, interaction, even if it doesn't actually have any user element attached, I think could be useful. The reason why we sort of use session.id is that it's actually a part of the semantic convention registry, and it's actually being used in, like, other namespaces.
within OpenTelemetry, and, you know, there… the session.id is actually also being used by different platforms, like LangFuse.
And, like, a couple of others as well, just to sort of group traces together. If… you know, the conversation ID is probably, hard to sort of keep track, and then, you know, if there is no coordinator agent that sort of, you know, hands off tasks to different age, and then, the, trying to track the, conversation ID, and then, you know, link the different spans to one another sort of becomes a tedious task.
But… That's… that's been, our experience.
**Aaron Abbott** 48:46 Korea, is this the… what you were talking about with workflows, or is there, like, an existing convention?
**Sergey Sergeev** 48:50 I… yeah, I don't have specific, proposal, or maybe we have that workflow ID somewhere. I just, recalled it was probably Lyudmilo's suggestion, if I'm not mistaken, from the last time.
And to me, yeah, I see difference between conversation ID, where it's basically a multi-turn.
chat conversation, and session ID is reserved for, basically.
**Pavan** 49:22 For, browser session.
**Sergey Sergeev** 49:25 So I think, workflow ID may be a better… Help or obscure.
Yeah, if we have already some pull request for workflow ID, probably we need to review it.
**Aaron Abbott** 49:38 No, I was just gonna say if you could drop a comment on the PR.
Either just mentioning.
Harsha, did you wanna…
**Harshit Kumar** 49:47 Yep, so.
**pratibha moogi** 49:49 You know…
**Harshit Kumar** 49:50 In the conversational space, There could be a scenario Where, within a single conversation, because there are multiple turns.
there could be multiple topics or multiple sessions going on simultaneously, if I may say, right? When I say a session, I mean to say that there's one… there's one conversation, but there are conversation boundaries within that one conversation, right? So, Pawan, have you… thought about.
Addressing these kind of scenarios.
**Pavan** 50:29 Yeah, I think not specifically that, but I sort of understand, like, where you're coming from, where within a single end-to-end, like, sort of a… run, there could be, like, different, you know, sort of conversations that have their own sort of context. Right. If… if… yeah, so… but our idea was to, like, sort of keep, like.
a track of the whole end-to-end, you know, session, if you want to call it, and then ensure that, okay, the user sent this prompt, there were, like, you know, six different agents that took part in, you know, like, sort of answering that question. Multiple agents, you know, executed multiple times and things like that. So, in order to keep a track of, like, you know, the Entire execution itself, to…
**Harshit Kumar** 51:21 impressed.
**Pavan** 51:21 of the entire execution context, we needed a different, attribute apart from the conversation ID, which, in some sense, either, like, probably workflow.id or session.id, made more sense. Hence, we were trying to, you know, pitch that in this particular Oh.
the army.
**Harshit Kumar** 51:45 One session is one conversation ID then, right, Cohot?
**Pavan** 51:48 No, no, no, it sort of, has, like, it could have multiple conversations as well. It could be one-to-end, like, relation between that.
**Sergey Sergeev** 52:00 Yeah, I would propose to create a doc with a few examples. I think all three things are different, so session, workflow, and conversation.
And, just to present this document, so it will help to accept those points.
**Pavan** 52:17 I think there's already a doc, but I'll link that in the slide. Thanks.
**Dany** 52:24 Yeah.
**Aaron Abbott** 52:24 I agree, because we're currently not really differentiating those, like, this is what we have for genetic conversation ID.
And it's just kind of a name. So, like, it makes sense to me to propagate this thing in baggage and send it across, and… but maybe the thing, the critique here is, like, hey, we need more granularity, in which case, yeah, definitely some motivating samples would be good.
**Dany** 52:46 Yeah, if I may comment on that, so I do believe that we need definitely a glue that combining and helping to collect, especially we are looking on the analytics side. It's very difficult if you don't have something that glue different pieces together. Sometimes you manage to do it with context propagation within a single trace. Not always it is possible.
So, this kind of glue can be, but as was mentioned here, it's not necessary enough, and maybe more level of granularity is needed. Specifically, when we are introducing the task.
One of the concepts that we're also proposing there is an identification and things around the requester of the task.
So, who actually requests the task external to the system? You know, the task is, you know, is something that agent gets as an input to act on?
But there is a need for binding of this request to some external user outside of the system, and this may be a requester ID that we suggest to have. It can be also, you know, who is this requester? You know, it's a different… situation when you are asked to answer a question by a human, or it's another agent who is asking you to do something. The protocol and the way you react may be different, and specifically, also, the session ID and the request ID, which may be, let's say, even, you know, consider it to be a record in a CRM system externally. Let's say someone opened the ticket, and now agent needs to handle this ticket.
So the binding of the external something to the task of the agent is kind of missing today, and that's why we are proposing also to add the extra information about the requester, and I believe the session IDs or conversation ID sits on the same… on the same area of how we close the gap of understanding that we are operating in concept of the wider application.
It's in the context of the user specific, who is asking us in the context of a session or several steps of the conversation that we are currently working on. So, I think all of these are connected, and let's see how we bring them together with examples.
And different perspectives.
**Aaron Abbott** 55:04 Yep.
Yeah, I would also just say, like, so we have… we also have links in OpenTelemetry, spend links.
Which are more like causal relationship, but not necessarily parent-child. And if I remember right, you can add generic attributes to the link, so… If it's something, you know, something like you said, like this This thing kicks off another task, we want to link them. It might make sense to have the actual, like… how is this thing linked? You can use just the trace ID and SPIN ID to hook them together, but also you can add attributes to say, like, what was the cause of the linkage and stuff like that.
I think that's what we do in messaging, so for just kind of, like, generic PubSub stuff.
We have some conventions here we should probably just look at.
**Dany** 55:54 Okay, great.
**Aaron Abbott** 56:00 Okay.
Is it a good discussion? Does anybody else have, any thoughts on that one?
Okay, cool. So it sounds like we need… Yeah, it sounds like we basically need some more discussion on… or, like, examples to show why we need more granularity, and we can… potentially break apart the conversation ID more, and alright.
**pratibha moogi** 56:38 Okay.
**Aaron Abbott** 56:44 Alright, that's the end of the agenda.
**Sergey Sergeev** 56:45 Yeah, the only thing, so the ABM folks, I started, I posted the message in, this, Hotel Gen AI instrumentation SWAC, So, the Swag channel is linked to the top of this document, because it's basically impossible to find your account and mention you in the swag.
**Dany** 57:08 Actually, currently, I've posted something on the Slack, but I'm not sure that… the one that you shared the link in the chat?
And with the proposal, can you see it? Are we on the same chat? Slack, or…
**Sergey Sergeev** 57:25 Maybe not, probably, Aaron, if you can scroll to the top of this document quickly to show the link to the swipe channel.
**Aaron Abbott** 57:35 Yeah, I'm sharing it, right?
**Dany** 57:37 Okay.
**Sergey Sergeev** 57:37 Yeah, yeah, F.
Okay. So, this is the link, Let me make sure that I'm getting to the same channel.
**Aaron Abbott** 57:48 Yeah. Yeah, I would just say there's, like, we should have some information. There's, like, a community repo also that has links to, like, the Slack channels, all the meeting docs, like, the public calendar and everything, so… Like, folks can edit this meeting doc, you can just add your agenda items for the next week and stuff, and Yeah, also…
**Sergey Sergeev** 58:07 I can quickly share the screen. I will just show this work.
**Aaron Abbott** 58:14 Yes, please.
**Sergey Sergeev** 58:16 So… We will make sure we are on the same page, so this is, the channel. It's Hotel Gen AI Instrumentation Channel, and if you basically click on this link, it should get you over there.
And this is the message, so please show up in this thread just.
say something. And we will add you to this weekly call of Microsoft Franciscos, so we can have deeper discussions about, multi-agent.
**Dany** 58:53 Perfect, okay… Okay. I've posted it on a different channel, so I'll post it there as well. Okay.
**Aaron Abbott** 59:09 Alright, awesome, great to meet all the new people, and see y'all next week.
**Sergey Sergeev** 59:14 Thank you.
**Dany** 59:15 Bye bye.
**Bruno Baptista (IBM)** 59:16 Bye. Bye-bye.
**Harshit Kumar** 59:18 Thank you, bye-bye.
