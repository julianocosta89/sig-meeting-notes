SIG: LLM Semantic Convention WG
Date: 2026-02-23
Duration: 31 minutes
============================================================

## Zoom Recording Transcript

**Sergey Sergeev** 00:45 Here, then.
**Erdenesaikhan Tserendavga** 00:57 Basically, good morning.
**Sergey Sergeev** 01:03 How are you?
**Erdenesaikhan Tserendavga** 01:05 Great. How are you? How's, Mountain Trail.
**Sergey Sergeev** 01:13 Quite good. I will chat more in the Teams.
Now, let's see who joins and how many people.
We'll join if it's just Cisco's pointers, we can probably… Skip, hey, Carl there.
Yeah, maybe we can do a quick intro, let's wait, Couple more minutes for more folks to join.
Please add your names to the attendees, and if you have any agenda topic, please add it here, too, in this… It's the same, OpenTelemat AOM Symantec Convention Working Group, SIG.
Document.
Okay, maybe, everybody who joined for the first time can introduce, yourself. So, a bunch of us here are from Siska Spunk.
Yeah, and so usually this track specifically focuses, on… Agent-specific, multi-agent-specific, conventions, so it's kind of extended time, to… the prime time on Tuesday.
So… Anybody wants to introduce yourself?
**Wolfgang Therrien** 04:19 Sure. Hello, everyone. My name is Wolfgang. I'm a tech lead over at Honeycomb. I'm happy to be here.
**Sergey Sergeev** 04:28 Nice.
Where else?
**Dakota Paasman** 04:34 I can go. Hi, I'm Dakota, I'm a software engineer at BindPlane, and I've been involved in the hotel community, mostly in the op-amp and collector spaces, but, yeah, I was just curious what was going on here and wanted to learn more.
**Sergey Sergeev** 04:54 Nice. Anybody else?
**Ricardo Pesciotta** 05:00 Hi all, this is Ricardo here, can you hear me?
**Sergey Sergeev** 05:02 Yeah, we can hear you.
**Ricardo Pesciotta** 05:04 Okay, so I've been working in the observability space for about 5 years. I started off at Cisco TX, and then I moved to a Cisco partner in the past year and a half.
And I'm currently… Working autonomously.
And I've been involved with, the topic on LLM observability.
For about 6 months.
**Sergey Sergeev** 05:30 Oh, is that school? Exasquian, so Vienus Saskonians here.
Yeah, in general, oh, Nagumar, also joined, from Microsoft, so perfect, now we can start.
Anybody, if you have any topic, please add it to the Google Doc.
Into their agenda.
We have a bunch, in the next topic.
list, so two of them are from Nagumar for a security spec and memory spec.
**nagkumar** 06:13 Yeah, that was supposed to be for tomorrow. I have brought up the spec, here a bunch of times.
Memory and security, so… I think you all are good with it, so we can take it to the call tomorrow.
**Sergey Sergeev** 06:29 Do we have a formal Approvals here.
**nagkumar** 06:34 Oh, we don't. I'm waiting for that.
**Sergey Sergeev** 06:37 I mean, not even formal, but, basically, do we have, somebody… Reviewed, and basically… put an approval here. We probably can… do that, so… for memory… From memory, I think we had somebody from Spawn also who worked, Yeah, I think it was, Josh.
who worked on retrieval, so… Josh, did you get a chance? Can you review today for how memory is different from retrieval?
Spence, and if there are any similarities And if you think that the memory spec is good, maybe you can just approve it, even if you… Don't have a formal… approve your maintainer status, I think it will help to the community.
**Josh Winerman** 07:48 I think I took a look at it a while ago, Sergey, and I think Nakumar did a good job, differentiating between the two. I think it's just more up to Leo Mila and the community at this point in regards to actual semantic convention purposes.
I'm not sure. I don't… I haven't kept very in touch with the PR and what she said, but I could take a look again, I'm just not sure it would… It would do much.
**Sergey Sergeev** 08:15 I think the important part, for memory, as we discussed, what's the difference from retrieval Span, and… If you…
**nagkumar** 08:28 Yeah, I agree with that.
**Sergey Sergeev** 08:29 Yeah, if you can review it and just, approve it, if it makes sense, I think it will help, Lyudmile and the company to… And to Upper Woods.
better.
**Josh Winerman** 08:47 Yeah, I can… I can take a look again, but I think, like I said, I think that the differentiation was pretty… Solid, so…
**nagkumar** 08:57 Awesome. Yeah. Just comment that and hit approve on this PR. That way, you know, other people on the committee who are actual approvers know that other people are taking a look at it, so… That's pretty much everything. Thank you so much, Josh.
Yeah, same thing with security, too, I think.
security, I work with another person on, your team.
**Sergey Sergeev** 09:20 Yeah, I did chase here, I think. Yeah, I did too.
Yeah, Aditya, if you find it good, can you just comment and, proof on this one, too.
**aditya (cisco/splunk)** 09:34 Yeah, sure, Sergey, I'll take a look.
But did we get any… Oh… insights from the security team, like… Or I can take a look from the understanding I have.
I'm good.
Valid.
Dallas, ice bubble!
**Sergey Sergeev** 09:58 I think, from the AI defense team, this is… Cisco AI defense team, they, were going to try and adopt, and I think it, worked high level for them.
But if you can double-check with MIDTA and, provide an update.
I think it was something like security event ID.
**aditya (cisco/splunk)** 10:22 Yeah, because the… like, right now they are… what we have done for them is we are adding a… Custom.
Like, an attribute on the spans.
And how they have done it is… They have pretty much… The pipeline kind of looks for that attribute.
And it triggers some of the flows on the backend, and then Also, how the… the Splunk UI.
parses that attribute, and… Probably they are showing some of the security-related stuff, depending on that.
So, if We change that attribute.
In the upstream, like the open telemetry.
And… So they… everything will have to now… Be updated to the new.
attribute in the downstream systems. Yeah, that's just my…
**Sergey Sergeev** 11:22 Let's double-check that we use this attribute.
It will also be a good support team.
Point.
**aditya (cisco/splunk)** 11:33 Sure. And thanks, Nakumar, for, you know, incorporating some of the comments, even in the draft stage of the PR. Really appreciate it. Thanks a lot.
**nagkumar** 11:41 Yeah.
Happy to.
**Sergey Sergeev** 11:46 What else, did we have?
From… It's a fast, february 9th.
Hmm… Anybody had a chance to look into that, code Agent SDK.
Also, just an open question to this group, So, right now we have, Timothy… focusing more on agents which, run in a mode like AI assistance, but as more and more stuff is being pushed, to something like coat code, and so on.
it may run autonomously for… Tens of minutes. Anybody has an experience monitoring those types of agents?
Nagumar probably, you run this… Yeah. …as part of the foundry.
**nagkumar** 13:07 We still don't have a bunch of things going on for coding agents, but yeah, if we do something for Copilot or anything, I'll let you know. As of now, we have not seen this come up anywhere, but I'll look into it and see if anyone's done anything at Microsoft.
**Sergey Sergeev** 13:35 Yeah, I'm, and, for multi-agent, which protocols, Which protocols do you see people are using? Where everybody is building, basically, same in-process agents first?
and using MCP… tools, basically, using other agents as MCP2. Do you see A2A… Get interaction anywhere.
Beyond, kind of, POC demo examples.
within good, but… yeah.
**nagkumar** 14:30 Yeah, I think we can look into it. I have not seen A2A… Trying to be referenced, The way, like, we treat multi-agents or, you know, multiple agents within one span would be, like, pass the trace parent.
And expect the, you know, child agent to follow that race parent and use that as a parent span, and put child, like, all of its spans as, like, child spans.
But that's just a… way we would do it within our, like, agent framework, I think.
So we would need to think about how to do it with, like, chain, line graph, and other stuff.
But so far, it's just that, like.
Because there is no mechanism to… Extract races from the actual… Protocol which is being used to transfer data between, like, Agent 1 and Agent 2.
If we just pass the trace parent to agent 2, and Agent 2 uses that as, like, a parent, span.
And we can easily get that parent-child relationship.
All of the traces associated with all the sub-agents, or… Other agents, related agents.
**Sergey Sergeev** 15:50 Yeah, Yeah, I'm… I'm also wondering, how can we not, over-engineer prematurely specifically for multi-agents.
In this, track.
And at the same time, To derive that definition for multi-agents, I… I think at some point, it would be great, if you can check with the broader Microsoft team.
What do they do? I don't see anybody from our trip today, from Cisco. We will probably need to double-check with them. Again, I want to find some, excuse… not excuse, sorry, use case, for… For real usage of anything beyond MCPA.
**nagkumar** 17:02 Yeah, I'll look into it. I'm sending a message to the agent's framework person right now.
**Sergey Sergeev** 17:13 anybody else, like, Ricardo… Or anybody new to this group, do you have any topics to discuss? Because if not, probably we can… Take the rest of the time back.
And, to discuss most of this stuff, with the broader group tomorrow.
Okay Yeah, let's, then take some time back.
Again, if you have any… items, topics to discuss, just add it, to that Google Doc, next.
Next topics… And they will be picked up, in… The next meeting.
**nagkumar** 18:53 Thanks for running this, Sergei.
**Sergey Sergeev** 18:55 Oh, and, I see the question, just pop up, popped up, in the chat. Sorry, I missed it when I was sharing. So, Pradeep, you have a question about, pioneer.
**nagkumar** 19:09 Yeah.
**Sergey Sergeev** 19:09 Spec?
**Pradeep Nair** 19:10 Yeah, it's cool.
Nag, offline, and, we can discuss what we,
**nagkumar** 19:18 what we spoke about, in the next meeting. It's just… I'm just curious to know if, like.
**Pradeep Nair** 19:23 There was any thoughts given to planner or planning specs, because we are adding memory, and I remember that.
**nagkumar** 19:29 Yep.
**Pradeep Nair** 19:30 We proposed, the utils, planner and memory were two types that we were trying to… we were trying to visualize or conceptualize, so… I'm just interested in knowing what's the… what's… what's, Nag's take on that, that's all.
**nagkumar** 19:45 Yep.
Yeah, so… A little bit of overview.
Planning is something that is… Very specific to certain types of agents.
Like, not all agents do a plan, or not all models which are powering agents write a plan.
I had this on my, task board at Microsoft, like, come up with a spec for planning, and given I'm do… I did this for memory, like, I was thinking, can we just reuse memory as a plan?
You know, with the memories item being like, hey, this is the plan, and then the memory scope being For within that agent execution.
Versus creating something separate for plants. So… Yeah, happy to… like, if you have a compelling use case where we would benefit from a separate plan type of span or attribute, in hotel, I'd be happy to bring it on, and write down a spec for it.
But yeah, let's chat offline, feel free to do.
**Pradeep Nair** 20:54 I mean, reusing memory also sounds, reasonable, but I didn't look at your current proposal. Is it already… do you already have provisions for that, or would you have to update the memory, spec?
**nagkumar** 21:12 It would just be, like, another memory attribute. So, memory can have, like, a lot of attributes, right? Like, you can save whatever you want into memory.
based on what your agent needs, and it has separate scopes, so go through that PR. The non-normative spec is, like, the easiest one to read. And then, yeah, if you just look in the files, you can see the non-normative spec, and then feel free to hit me up on Slack.
**Pradeep Nair** 21:40 Sure, I'll reach out to you if I have further questions about it, or…
**Sergey Sergeev** 21:44 An interesting use case I saw in some of the customers.
Basically in two of them. Using, basically some deterministic workflows handbooks.
And, basically strain them in a rag.
So, when you need… when your agent needs to do some specific task, you can look it up, in your reg, and fetch the best workflow… Which is deterministic, number of steps you need to perform.
And basically run it. Is it something… similar, or a plan, it's still kind of, dynamic.
Prompt for the model to perform.
**Pradeep Nair** 22:38 Plan is, like, what I understand is, like, some… some internal steps that the agent takes to reach a goal. It could be predeterministic, it could be dynamic as well, but it's in context with memory. That's why I asked, like, if you're… if you're adding memory, do we also have, like.
Any plans to, add, plan or… or planning phase, you know?
**Sergey Sergeev** 22:59 And, and Planner, how is it different from just orchestrator, type of the agent?
**Pradeep Nair** 23:09 Yeah, I mean, that's a good question, I've not, like… Yeah, yeah, no, I just tried to brainstorm here. Yeah, yeah, that's something to think about, but, orchestrator… I don't know, I could be wrong, like, the orchestration… orchestration phase could be, like what you… Described is probably, deterministic and static, or doesn't take memory into context.
Historical memory, into context, but planning is something, that would, like, you know, revolve around memory, is my understanding. I don't know if, like, If, Nog, you have any more inputs on that.
**nagkumar** 23:54 Yeah, the… when I wrote… was writing this memory span, I kind of thought about this, Some agent frameworks bring in, like, a concept of life cycle memory, or… you know, things like what you said, Sergey, around…
**Sergey Sergeev** 24:15 Instructions for an agent to perform a certain task.
**nagkumar** 24:20 And make it more deterministic. And it only exists within the life cycle of that particular agent. It gets picked up dynamically when the agent realizes it needs to perform that task.
So, yeah, I was probably thinking this could be scoped as a memory or life cycle whenever it's updated or retrieved and I can just use that.
Like, or, you know, retrieval. That can go either way. Unless it's being updated, I think retrieval is good enough.
If it's being updated, then we can do the memory one.
**Sergey Sergeev** 24:57 Yeah, basically, I'm trying to put myself into,
**nagkumar** 25:03 DM.
**Sergey Sergeev** 25:04 choose, or put PM HUD here, so, what does it mean? So, let's say we have, that, pointer, or pointing step, or even the memory. So, what do I want to monitor?
As a customer, so… So, if memory has some unique ID.
**nagkumar** 25:31 And, some memories.
**Sergey Sergeev** 25:35 We're more efficient, Yeah, I'm trained to… Think through, so how do you monitor the memory, or for the plan?
What do you monitor for the plan? Do you monitor, bad… do you try to find some bad plans and improve it?
**nagkumar** 26:00 It could just be something, I mean, putting more generic terms.
With… if we are thinking in terms of, like, agent scope, agent created a memory item called plan in the beginning of its execution, and then it edited it multiple times along the way throughout its execution.
You know, that's the sort of insight that customers will probably, benefit from looking at, of like, oh yeah, the initial plan was not good enough, and then it was improved, throughout for further steps or further execution.
**Pradeep Nair** 26:34 Yeah, also something like, you know, planning latency, or the thinking time, So, and, like, how… how well… agent recovers when you replant something, you know? Like, a plan goes wrong, you replant it, how does the agent recover, like, And I think… Just off the top of my mind, something like tool selection could also be… tool selection rate or accuracy could also be something that we can… Monitor out of it.
Not sure yet, though, so again, I'm…
**Sergey Sergeev** 27:10 Yeah.
**Pradeep Nair** 27:12 Yeah, tool selection, I think.
**Sergey Sergeev** 27:14 It's quite important, it's something very, very real, which the teams are struggling with.
Two selections is different, so it's… I took two selections, so one selection.
Maybe… also… Hopeful.
Ugh.
Yeah, anyway, I think, we can, we can work on, on all of those, and just keep, that going. Do we need, something like, Google Doc, where we will have, more… Live discussion, and maybe we will maintain All of the types we are trying to work on.
For reference?
**nagkumar** 28:11 Yeah, we can just use the PR for it. I don't know how much we will, like… Maybe. How much progress we'll do, so… I'll just paste the link to the part where I have, some samples for scope.
So those are the lines in the file. I'll just put it on chat.
Nice. I think, spans.yaml, well, I don't know if it got selected properly.
Right.
Let me bring that up again.
And sponsored Yamilies.
Oh, let him…
**Sergey Sergeev** 29:06 This one, right?
**nagkumar** 29:08 Yeah.
In that, there should be, like, something called memory.scope, and… Mmm… I just hired it. I lost the link again.
**Sergey Sergeev** 29:19 this.
**nagkumar** 29:20 81 to…
**Sergey Sergeev** 29:25 Oh, yeah, hit some big file.
**nagkumar** 29:29 And it was… it gave me a relative link, so I'm having a hard time trying to find that as well.
**Sergey Sergeev** 29:37 hence… Can open the file.
AT… Each way?
**nagkumar** 29:56 Just search for memory.scope.
**Sergey Sergeev** 29:59 Yeah.
See it here.
This one, just the definition of the attribute, right?
**nagkumar** 30:07 Yeah, the reference should show up… somewhere.
Where are your reference?
Yeah, it just… Interesting, yeah. It went away. I'll go find the right link, but… Is it Virginia, I…
**Sergey Sergeev** 30:40 Yeah, what's… Chat about it. Also, and we are at the time for this meeting.
**nagkumar** 30:47 Yeah, thanks for running this, Sergey.
**Sergey Sergeev** 30:49 Oh, thank you. Everybody for joining. Hope to chat with you tomorrow.
**Pradeep Nair** 30:56 Thank you for taking the extra time to discuss this. Bye.
**aditya (cisco/splunk)** 31:00 Anyways…
