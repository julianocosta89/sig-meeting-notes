SIG: LLM Semantic Convention WG
Date: 2026-06-30
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:24 Wonderful. Two AI bots and me.
Hi, Huxing, good to see you, another human in this world of AI bots.
**Steve Rao** 01:26 Yeah, hello, Ludimila.
**Liudmila Molkova** 01:30 Hi, Steve.
I joined, and there were two, Not taking bots. And then the third one joined, but then one of them left. I'm happy to see humans here.
**Steve Rao** 01:41 Okay.
**Huxing Zhang** 01:44 Hello.
**Liudmila Molkova** 01:47 Hello.
Do you folks want to discuss anything in particular?
**Steve Rao** 02:28 Yeah, I have a question, but I don't, prepare an issue. It's okay.
Yeah, that is a scenario. We want to, recode a task ID.
in… In reference span, or something like that.
I'm not sure, is there any discussion in community before?
Because, in, multi-agent scenarios, yeah, we want to, correlate… correlate the task to, related, trace, and we want to, calculate, How much token this task will spend, something like that.
**Liudmila Molkova** 03:25 And the task car is a special agent.
Where it's the deterministic process of breaking things down.
**Steve Rao** 03:34 It's a tasker. It's a tasker. Yeah, maybe the tasker sent by human to the multi-agent system.
And, there is a, agent, something like, managing, and there are some agents, like, worker, and, Human, submit a tasker, and the managing will assign the tasker to, some worker's agent to, finish the task.
**Liudmila Molkova** 04:07 Yeah, I think there weren't, several… Maybe related things in some conf… In the past.
And, there were some attempts to define things. The… Yeah.
So, I think that… Part that's missing is what is task?
Where would we… Given the current set of instrumentations.
What would be reported as a task? Or… In which scenarios would it be reported? Maybe you can share some thoughts on this?
**Steve Rao** 04:49 Hmm… okay.
**Liudmila Molkova** 04:59 So here you see there are a bunch of things, but what is a task?
**Steve Rao** 05:06 Okay, yeah, I, you, you, you, you, you mean, yeah, maybe, from the perspective of, committee, we want to get more some specific, scenarios, like, how to, define the task, something like that.
**Liudmila Molkova** 05:24 So, you see, what we're… are focusing on… In the community is… the… libraries… well, the scenarios here, and the set of libraries is completely imaginary. Like, we can add things here.
But none of the… Well, some of these things have a concept of task, I think QueryEye does, right?
Maybe that's the only thing that does in this list?
So, like, if you're… if it's the application concept, Then… It would be hard to define, because every application thinks about tasks as something special.
If, it's the coating agent concept, right? Like, blood or anything else.
This is interesting, but then we would need to look in, like, coating agents, or, like, those harnesses, in general.
And we haven't started yet.
So, if you have some mental model of how it should work altogether.
**Steve Rao** 06:41 Hmm.
**Liudmila Molkova** 06:42 Maybe you folks can prepare a demo, or you can walk us through how you're, how you're thinking about it.
And it would be really interesting for everybody to learn, and then we can start, like, designing this whole approach altogether.
**Steve Rao** 07:02 Okay, okay, makes sense.
Hmm.
**Liudmila Molkova** 07:07 Yeah. Where does the task come up for you? What do you consider to be a task?
**Steve Rao** 07:13 because, yeah, in our, Yeah, company, yeah, we are going to, launch, a product, help, a user to managing their task in multi-agent scenarios.
And And for users, they can, submit some task in the system, and the system will, use an agent to finish the task, or something like that, and there is a concept of Tasker, and they want to, do some related observability.
So, so I get this requirement.
**Liudmila Molkova** 08:03 Okay.
Cool. So then, The main ask would be to see where it appears in other cases, and try to outline what it is.
**Steve Rao** 08:22 Okay, okay, I will check it out of the issue, and, yeah, yeah, if I have some, thoughts on that, I will, leave my comment.
**Liudmila Molkova** 08:35 Yeah.
**Steve Rao** 08:36 issue.
**Liudmila Molkova** 08:39 Yeah, and as you can see, if you watch… search for task in this report, there are… Maybe not.
Yeah, there are a lot of long-tail things, but there are… A few different issues that… Seem to be related.
**Huxing Zhang** 09:08 Yeah, I can… I think I can give an example of how we think that… Task is, for example, imagine we are… Having a group of agents, like.
a couple of open claw. Each of the agents is an open call, and we assign a task for them. They form a team, a team of agents, and, to, like, to develop a system of framework or instrumentations, for example, for hotel, like, added something… add a new instrumentation for… for a framework. And the way to give this… assign this task to a group of agents, so each of them are open call instance, the, the… The task will be spread across multiple agents, and we want to Find out the… for the whole task, how much of the… Token has been… consumed, for example, and this, this is, multi-round. Multi-round, collaborations. Each of… they may have multiple trace ID or spans, a lot of spans, but we want to correlate them.
So we need, definition of how we define this, for example, task ID, and how do we… Propagated it across different agents.
**Liudmila Molkova** 10:47 Yeah, I see. Ugh. So… there is a similar concept, and it's not completely the same, but I'm just talking, trying to understand why it doesn't work. So we have a workflows pen.
So when, let's say, user starts an interaction, the… Encompassing processing would be a workflow.
And inside the workflow, there could be first nested workflows.
So for example, this could be, the first would be Invoke Agent.
that's, triage, and then it would delegate to Maybe one of the screws, the, the… One of the open core instances.
This would be another workflow.
**Steve Rao** 11:46 Hmm…
**Liudmila Molkova** 11:47 And so on.
And… Each of them can have nested structure.
**Steve Rao** 11:55 Hmm.
**Liudmila Molkova** 11:58 and this is the process of executing the high-level task. If this workflow involves multiple turns.
There will be multiple… Turns inside, right?
the… what's… What's missing is some task idea, but… There is, corresponding trace… trace ID and span ID. That is a unique identifier of the thing.
So, if, if task… comes from somewhere else, and there is a task ID that Is attached to this task already.
this makes sense. Or… Where else's task comes up is… sorry, I'm going… I wanted to… Okay, so I did… I had a session with Wood.
Right, and it broke things down into tasks, but that's a different thing, right? It's not the overlapping… do everything, this is more like sub… task.
**Huxing Zhang** 13:31 Yeah, I think there's, some difference between, we are, asking… when we are doing a task in, like, clock code, they, they fork sub-agent, I think, I believe they do so, and we actually have The ability to, to, to trace these, kind of, scenarios, but for agents that are running different instances across multiple agents, and maybe nesting the task, maybe come from outside of this observability system, they have some… like, business meetings of this task. They are being created in, Outside of this system and passed to the contacts, so we want to propagate them.
across different agents. I think this is one of our scenarios.
**Liudmila Molkova** 14:26 So, it's your case that task comes… From an external world.
was the existing ID. Imagine I'm a user, and I… I don't know, this is… I'm doing something about some order ID.
Why is it important for you to have a specific attribute name for it? Because for every user, for every business system, this would be Something different.
You can't… it's possible to propagate it through baggage, right? There is no other way to propagate arbitrary ADs.
And it can be… you can propagate wherever you put in the baggage.
**Steve Rao** 15:17 Hmm.
**Huxing Zhang** 15:18 Yeah, yes, but, I think this may be a common issue, maybe it's not happening right now, but I think… It may be a common issue, and maybe we can… Do something.
On the semantic commission.
**Steve Rao** 15:40 Hmm…
**Liudmila Molkova** 15:42 Yeah, like, we… like, if there are two different independent examples of this.
Let's explore it. Let's see how we would… model the system as a whole. Please explore the workflow span, because the… the naming would be the tough part, because as you've seen my attempt to show you the claud, was that there is already a concept of task, and it's something maybe different.
And there is a crew concept of task. Let's find the naming that's… that would work and would not be conflicting.
**Steve Rao** 16:32 Oh, is… is that unimpossible? We, We abstract, attribute, and to, represent the concept if users want to record related, information, something like a task ID or project ID, and maybe they can, Use this attribute to a storage-related concept.
something like, JNI, conservation ID.
**Liudmila Molkova** 17:09 Like, GenA ConversationD?
**Steve Rao** 17:11 Yeah, and yeah, according to my knowledge, this is a, yeah, this is an abstract concept, yeah, in some con… in some, content, in some scenarios, yeah, maybe, we can use this attribute to, storage session ID.
And, under… something, yeah, maybe, yeah…
**Liudmila Molkova** 18:04 Sorry. Hey, I'm sorry. Sorry for interrupting you. Go ahead, sorry.
**Steve Rao** 18:08 Okay. Yeah, as you mentioned, yeah, maybe, for some different, scenarios, yeah, maybe, people will use different, concepts to, to, to represent this, attribute, something like a project ID or task ID, and, Yeah, my, my concern is, is there any possible? We, from, our community, we model, attribute something like a geni task ID, or something like that. And we… we can tell, user, yeah, maybe if they, need to rec… Capture related, attribute, maybe they can use this, Attribute to a storage-related, field.
Fancy.
**Liudmila Molkova** 19:05 Yeah.
We can, we just need to define what it is, right? So what is the task? When would we use it? When would we tell users to… set this attribute, and what does it actually mean? Because if we don't, everybody will use it in different ways, and there will be no point in having the same attribute.
**Steve Rao** 19:30 Hmm.
Yeah, okay, yeah, you mean, yeah, maybe we need to, clarify the scenarios.
And, G… Add more… some specific example or something, and then we start to model these attributes.
**Liudmila Molkova** 19:56 Right.
Cool.
Anything else on this one?
**Steve Rao** 20:11 Yeah, besides this point, I have another small question.
Yeah, in our JNI, semantic convention, there is an attribute called, JNI, conservation ID.
**Liudmila Molkova** 20:27 Okay.
**Steve Rao** 20:28 But, in a lot of scenarios, something like, for coding agent, there is a concept called session.
**Liudmila Molkova** 20:42 Okay.
**Steve Rao** 20:45 So, I'm not sure, if, whether I, understand correctly. Yeah, maybe in some coding agent scenarios, the, we can… storage, it's a CASA ID, by, by, Conversation IT.
**Liudmila Molkova** 21:06 Oh, that's a great question. So, there isn't… the place, like, the… there isn't conversation ID was added, is… It exists as a concept in… Okay, gentlemen.
**Steve Rao** 21:23 Yeah, I… yeah.
**Liudmila Molkova** 21:25 in, yeah, it's like the Llama Chat story, WS Bedrock, but essentially it was added because of OpenAI Assistance, which had this concept, And it means that… Oh, engine sessions. Interesting. Yeah, so when you store the conversation somewhere else, this is the ID that's used.
2… Query it, or to give it to your model provider, agent provider to pull it up, so instead of carrying, like, the whole conversation around, you just use the conversation ID.
I think the session… the conversation ID is just one thread, at least how it's designed today.
It's like the… the snapshot of a chat… sorry, it's the pointer to the chat history.
**Steve Rao** 22:28 Hmm.
**Liudmila Molkova** 22:29 But then, in case of the coding agent, or complex… like, multi-agent thing, there could be multiple conversations within one session, right?
**Steve Rao** 22:41 Yeah.
**Liudmila Molkova** 22:44 And then the conversation AD is a bad candidate for this.
Session is… We… it has the same problem as… as, task. We… we cannot define it.
redefine session, we will have even more trouble defining task. But, like, for session, it seems At least… We can… There's more clarity, and it seems the session is… everything that Happened during this specific execution.
Right? Where, even then, I… I'm not sure it's… clear. So, for example.
if I return back, is this a session? Can I come back to it all the time?
**Steve Rao** 23:46 Y-yeah.
Encoding agent, yeah, that is a session, and, maybe, one hour ago, we, I can ask some questions, and, it, replied, and, one hour later, I, invite to ask a follow, a following question, and,
**Liudmila Molkova** 24:11 Yeah, so… let's… let's assume… This is a session, Okay, so, yeah, we… Yes.
The next steps for… So, can you remind me what the original question was? Was it about the… just the session? Did you want to model the session? Oh, you asked about conversation, right?
**Steve Rao** 24:39 Yeah.
**Liudmila Molkova** 24:41 Yeah.
So, there were several attempts to define session ID in the past.
For Gen AI.
And they all got stuck on the question of there is a session ID.
Here… And it means something completely different. It's the… user… like, a browser session, like, what I have right now is my… in my Chrome is the… User… end-user session, and it… It's not the same as what we consider to be a session in Gen AI, it's unrelated.
Yeah. So… We can probably define it.
Then, there is a question of… Doing some research, what… others consider to be a session, so the thing I'm… I was looking, like, into yesterday, maybe you're familiar with the trajectories?
And there is this thing for trajectories.
R.
My interruptsies.
And this is… a popular… Benchmarking framework that's also adopted by some of the… vendors, and it has a notion of session ID.
And… it means… It's not something. And there are probably other different interpretations of what session is.
And can we do some research?
On what different providers… different, I don't know, Popular.
Frameworks… vendors… considered to be a GenAI.
Pushing.
I think it's inevitable that at some point we'll define something like this, and I would support adding it, but I think at this point, it's clear that it's not the user provided, like, not the user session, not the browser session, but something GenAI-specific.
Yeah.
**Steve Rao** 27:59 Yeah, and I, I, I thought, yeah, Aaron also, left a comment, on chat.
**Aaron Abbott** 28:08 Yeah, I didn't, I didn't understand how that was different than the conversation we already have, especially, like, the coding agent, that you showed.
**Liudmila Molkova** 28:19 So, if we… Get back here. So, I imagine there are quite a few sub-agents that work on this thing.
Where was the list of to-dos? And potentially, there are multiple conversations in terms of This is my conversation with my agent.
Sorry, I can't find it.
anymore.
**Aaron Abbott** 28:47 I see, so you mean for the sub-agents, they… they would have separate conversations, but it would need to dive back to the root one?
**Liudmila Molkova** 28:55 Right. Yeah.
**Aaron Abbott** 28:58 I see.
**Liudmila Molkova** 29:00 I… I think I'm… I kind of want to maybe even rename the conversation ID to be something.
Different, or at least… Explain that it's just… just the one… One-shot history, not everything, right?
**Steve Rao** 29:23 Okay.
**Aaron Abbott** 29:26 Yeah, I think… I think what you said, Lyudmila, the next step to look at the different concrete implementations would be helpful, because I'm not too familiar with how all of them represent this, like, if they… Internally track the parent conversation.
Any of that stuff.
**Liudmila Molkova** 29:50 We are almost out of time. Pushing, you created an issue. Oh, nice!
what… What… how can we do this? What can we do together?
**Huxing Zhang** 30:04 I think a quick, quick introduction to this issue that we… initially, we have done a conformance tests based on trust, the… conformance OTA waiver task report, conformance report. We add the conformance results of the long suite instrumentations, and there's a PDF attached in the issue that you can And we, we, we are, we are, going to, like, to send PR to Trask's project, for adding this conformance test result, and then we go.
Through, in some order, we need… we will plan… we're planning to, contribute these instrumentations, but maybe not all of them, because some of them are Let's maybe inter… have some, same instrumentations with the open inference ones, so we will… Kind of discuss with the… With you, and to maybe… which one is… we will do first, and then we will get the rest of them down, yeah.
**Liudmila Molkova** 31:22 Awesome, sounds great.
Okay.
Dan, let me know if I can help with anything.
**Huxing Zhang** 31:31 Okay.
**Liudmila Molkova** 31:32 Yeah?
Thank you. Have a good day.
**Steve Rao** 31:35 Yeah, thank you.
**Aaron Abbott** 31:37 Thanks, later.
