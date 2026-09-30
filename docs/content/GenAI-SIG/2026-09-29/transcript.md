SIG: GenAI SIG
Date: 2026-09-29
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Aaron Abbott (Google LLC) 00:02:22 Everyone's the one.
Trask Stalnaker (Microsoft Corporation) 00:02:25 Hey.
Tammy Baylis 00:02:27 Hi, everyone.
Trask Stalnaker (Microsoft Corporation) 00:03:25 We'll get started in just a second. Go ahead, and if you've got any topics to add… All right, well, let's get started. I think, Ludmilla was in the earlier meeting, so I… Expect she will join, but… Not sure if she's also just got back and jet-lagged.
So, let's see.
First, Steve Rao had requested… For the review, it looks like we have the required reviews here, though.
So… I will take just a brief look and plan to merge, Let's say… If you're interested in that, though, please take a look and leave any thoughts. It's fine to go through, you know, another review cycle. If there's… if anybody has… ideas.
Next.
Ankit is not here, but just wanted to raise… Awareness for the voice… Model PR… I think… Rob Ludmilla, you have… The… you were engaged on this.
I'm sure it will take you a couple days to… Catch up some… Backlog and whatnot, so.
Liudmila Molkova 00:06:04 Very optimistic about a couple of days.
If, if, Ankit would watch the recording, the… Steven Allen, who commented, it's the person at Google who's also interested, so… I'll also ping him, and I would like to get his gray checkmark.
Trask Stalnaker (Microsoft Corporation) 00:06:25 Great, yeah, awesome.
Did I get that right?
Liudmila Molkova 00:06:49 I think so.
Trask Stalnaker (Microsoft Corporation) 00:06:57 Okay, yeah, Aaron, So… I had left… yes. So let's… Just quickly, I can explain what I meant here. I didn't mean the naming, I meant the semantics.
of them.
basically saying that Main agent.
Semantic, like, the semantics for agent… Main agent ID, and main agent… Name.
I'm wondering if there's a reason for them to differ semantically from agent ID and agent name.
Yeah. Other than it being the main agent.
Aaron Abbott (Google LLC) 00:07:50 Yes.
I think.
I see what you're saying. I think it kind of started out similar, and then the text diverged a little bit as things went on, and then there was also the PR from Ludmilla that changed the.
agent ID description, so it's, yeah, it's possible I can align them a little bit more, and it just kind of drifted with the review process and everything, but… like, yeah, I think they're they're slightly Semantically different, but, Which I think makes sense to you, but maybe just the… Descriptions could be a lot more, yeah.
Trask Stalnaker (Microsoft Corporation) 00:08:34 Okay.
Yeah, I mean, just the… Certainly, they differ in the idea that one is a main agent or not, but given that within that.
Yeah, and if there are reasons, then that's fine. I was just… wanted to call out that they seemed… in my head, they seemed like the same thing, so I was expecting to see essentially the same description.
Aaron Abbott (Google LLC) 00:09:02 Mmm.
Liudmila Molkova 00:09:04 Is there any… oh, sorry, go ahead.
Aaron Abbott (Google LLC) 00:09:07 No, no, please, please.
Liudmila Molkova 00:09:09 What is the difference today? Like, is there anything substantial?
Trask Stalnaker (Microsoft Corporation) 00:09:15 I don't know if you would call these substantial, but these are the differences today.
Felix Becker 00:09:30 Does this, touch… GenAI.conversation ID at all.
That was something I was wondering with regards to, like, multi-agents.
Aaron Abbott (Google LLC) 00:09:44 No.
This one is, like, sorry.
Felix Becker 00:09:51 Like, in a multi-agents… System, if you have, like, a multi-agent session.
the conversation ID… you kind of have to make the decision. Do you set it to, like, the overall session ID, or do you set it to just, like, one… Thread of that multi-agent session.
And if you put it to the session ID, it's, You're mixing multiple, like, threads into one, if you put it to one thread.
That there is no standard way to, like, associate the whole session together.
But this is not, this does not touch that.
Aaron Abbott (Google LLC) 00:10:32 Yeah, I think… I do know what you're saying. I think it's a bit different. This is more like identifying attributes about the host or the process.
like the the logical thing that people are like, oh, my agent, I deployed my agent,
Felix Becker 00:10:49 Hmm.
Aaron Abbott (Google LLC) 00:10:50 Not, not like instance level conversation and such, but…
Felix Becker 00:10:53 Yeah.
Aaron Abbott (Google LLC) 00:10:55 Yeah, maybe the terminology makes sense, though. I think Ludmila left a comment in chat.
Felix Becker 00:11:00 No, I agree, though, with, like, like, that matches Anthropic language, though, where, like, agent is the… The static resource, and then session is, like, the instance of the agent.
Liudmila Molkova 00:11:17 Session is the instance of the agent.
Can you see why?
Felix Becker 00:11:24 At least in our API, that's… that's how we treat it, yeah. Like… Like, agent is the thing where you one time say.
This is the agent I want. It has this name, it has this system prompt, it has these tools, but it won't do anything yet.
And then you can spawn that agent.
And you can spawn it repeatedly, you can spawn multiple times, you can spawn it once per, like… For different users, you can, you know, spawn it once for different tasks.
And those are sessions.
Aaron, that does… matches this too, right? Like, this is the… the main agent is, like, the static configuration here.
Liudmila Molkova 00:12:07 Yeah, this one identifies the agent itself.
Aaron Abbott (Google LLC) 00:12:12 Yeah, yeah, I think the session thing is is a little bit different. It's like a I guess I see what you're saying, though. It's not like instances in the sense it's instances of like a conversation. And basically a made agent has many sessions. Right?
Felix Becker 00:12:28 Yeah, or, like, in GenAI, it's, like, create agent versus invoke agent.
Aaron Abbott (Google LLC) 00:12:45 The only other thing I wanted to call out here, we talked a couple times about, like, this URN. I think a couple providers, including Google, have this URN and, like, registry thing.
So in a sense, the ID on the resource here is kind of like a service discovery key. It's the thing that People used to talk to it.
which I think the semantics are a little bit different than the agent.id.
Alright.
At like the sub-agent level in that case.
Liudmila Molkova 00:13:19 Why though if subagent is also in the registry?
Aaron Abbott (Google LLC) 00:13:24 Yeah, if SubAgent's in the registry, it would have its own.
The.
GenAI dot main agent, right?
I think we had this whole discussion about the entities for thing, which isn't really available yet. I think it's just a… OTEP at this point.
Liudmila Molkova 00:13:41 On the client side, When you call the hosted agent, the agent ID on the client side matches the main agent ID on the server side, ideally, right?
And then they're… The client.
Side.
the agent ID on the client side should at least include everything that's on the server side, and might be more.
Aaron Abbott (Google LLC) 00:14:10 What did you mean by include?
Liudmila Molkova 00:14:14 I mean everything that can be in the main agent can also be in the agent ID on the client side.
But the Agent ID on the client side can be a little bit more permissive.
Aaron Abbott (Google LLC) 00:14:25 I got you. Do we have agent ID on the client side right now?
Liudmila Molkova 00:14:30 Yes.
Aaron Abbott (Google LLC) 00:14:32 Okay.
Let me take another look at that. That's a good point.
But yeah, I think that's kind of all I had. I can… Follow up offline.
Trask Stalnaker (Microsoft Corporation) 00:14:41 I was rereading, though, I think.
I don't think these are actually think these are reasonable.
differences.
I was gonna resolve this.
I think it's good.
Felix Becker 00:14:55 Can I ask one more question? If… so, if I create an agent, and that's… it's like a multi… Agent.
There's also genai.agent.name, right?
I… would I set… GenAI.agent.name and GenAI.mainagent.name to the same string, and, like, the IDs, too.
Trask Stalnaker (Microsoft Corporation) 00:15:19 So, right now, and correct me if I'm wrong, the… this is… Only for hosted agents today.
Is that correct?
Aaron Abbott (Google LLC) 00:15:34 Yeah, I think… The answer is like not probably not necessarily so.
I don't know how it works in the Anthropic AI. I could totally see it being possible that they end up being the same.
But the, like, the… main agent is… Just to be clear, it's like a resource identifier, right? So it would be static for The life of the agent, effectively.
And… So it could be the same, or it could be like you redeploy.
a new version of your agent, the identifier for Made Agent stays the same, but say you tweaked, like, the… the name of the… The actual agent that's… Like the… the log… like, the agent inside, if that makes sense.
Felix Becker 00:16:23 So in in Google's world, there's like.
there is an agent inside the agent. Does that make sense?
Aaron Abbott (Google LLC) 00:16:31 Yeah, I mean, I think most frameworks I know for the managed agents, like, for… sorry, for the Claude, I think it's called Claude Managed Agents, it's a little bit…
Felix Becker 00:16:41 Yeah.
Aaron Abbott (Google LLC) 00:16:42 same.
Felix Becker 00:16:42 like, the coordinator agent, that's just, like, the top-level agent. So, I guess maybe what would be useful to specify is just, like, in those cases, like, should we just double report the attribute, or should we, like.
omit one of them? Like, should we just not report the main agent attributes, or should we, like, you know, set them both to the same values?
Liudmila Molkova 00:17:04 In the tree, the interesting part, it's the entity or resource. It's something you stamp on the process level.
So, like, it… I think it's not… it can apply to harnesses as well, it's not necessarily for hosted agents. So, harness could… Say, okay, my main agent is this.
And it's not that this is stamped on each metric or span.
It just appears as the resource.
Attribute on those.
And then you would have to… And I think that's the point that you have to… But maybe we can spell it out more clearly.
somewhere.
Trask Stalnaker (Microsoft Corporation) 00:17:51 And just a different… just to… because we might… I'm not sure if… We're… Felix, you're asking sort of more about this PR here is extending this into the SPAN world.
Harm.
This PR itself is… they're resource attributes, so they're not things you would stamp on the span.
Felix Becker 00:18:15 Oh, I see.
Trask Stalnaker (Microsoft Corporation) 00:18:17 It's a global process SDK configured resource.
Felix Becker 00:18:22 Got it.
Okay, so like a hosted product, this PR, actually, you can't really set this.
Because we have spawned, like, one process per agent.
Liudmila Molkova 00:18:39 So for the hosted thing, if you span one agent per process, you can… you would set it.
Felix Becker 00:18:47 Right, but if I don't…
Trask Stalnaker (Microsoft Corporation) 00:18:50 Well, if you… you would need a separate SDK instance per… Not process, but you can have lots of multiple SDKs in one process.
Felix Becker 00:19:03 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:19:04 But today, the resource is global to the process to the SDK.
Right.
In the… with entities…
Felix Becker 00:19:21 So if I don't actually, like, spawn multiple SDK instances, I just have, like, a service that handles many requests, and… It wouldn't, like, it wouldn't make sense to set these at all.
Trask Stalnaker (Microsoft Corporation) 00:19:43 I think that's where, potentially, it gets… I mean… Possibly. Possibly, and there might… I don't really understand. Does anyone understand the entity future of where you can scope entities? Because… I know, like, the browser SIG wants to use… has this idea of using entities to represent sessions.
And so that's obviously a more fine-grained scope.
That is not a reality today in the SDKs yet.
Felix Becker 00:20:19 Yeah, well, in the browser, I can see it, because, like, every tab, you spawn a new SDK instance, right? So if it's set globally, that would work.
yeah, for, like, hosted agent products, it's basically, like, an implementation detail, right? Whether they, like, literally… spawn a sandbox and put an SDK inside of it and start that SDK up, or if they implement it… I think we've published a blog post on this of, like, do you separate the hands from the, from the brains?
Where, like, the brains is actually, like, a multi-tenant service, and then only the hands run, like, inside of the sandbox, and so you couldn't give the brains A different, process level attribute for each… for each agent or each session.
Trask Stalnaker (Microsoft Corporation) 00:21:11 And that's where this PR… I mean, I'm… I'm interested to… Once, basically, we merge this and kind of move on to discussing this… Yeah. Extending it to the span world, I think, is… Very interesting.
Felix Becker 00:21:28 Yeah, happy to move on.
Liudmila Molkova 00:21:31 Yeah, would you mind taking… Sorry, go ahead, Darren.
Aaron Abbott (Google LLC) 00:21:34 No, I was gonna say the same thing, I think, as well.
Liudmila Molkova 00:21:38 Let's say it to make sure.
Aaron Abbott (Google LLC) 00:21:40 Yeah, can you… Felix, do you mind, like, taking a pass at 270?
Do you have thoughts?
Felix Becker 00:21:48 Yeah, I can, I mean, I can just leave, basically, what I just said.
as commons.
Aaron Abbott (Google LLC) 00:21:56 Yeah, I mean, even if, like, the description looks good to you.
Felix Becker 00:21:59 Yeah.
Liudmila Molkova 00:22:02 I was going to say that, let's… let's focus on this one, but I would be interested to hear, Felix, your feedback on the… the other one, the… the SPAN 1385, I think? Trask, you've been showing it. Yeah. Yeah, this one.
Trask Stalnaker (Microsoft Corporation) 00:22:26 Yeah, and let's, let's say that for this one… Same thing… Let's… I'll plan to merge by end of day, unless there's… anything substantial that… We want to address.
Alright, Let's go on, Nikhil. Hey.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:23:05 Hello. Yeah.
Umm.
Yeah, so I think I've… addressed all the comments, and I think a few folks, like Girish and Neil have also commented, so thanks for taking a look at the PR. So, I just wanted to check if there's any other suggestions, or… Umm.
Like, are we good on this PR?
Trask Stalnaker (Microsoft Corporation) 00:23:36 Let's see, so in… Need, Neil, is this use… Is this an approval?
Well, you know…
Neil Yashinsky 00:23:49 Hi, yeah, I only had a… I mean, it's a pretty big… it's a… it's a pretty big poll, so I only had a chance to review a portion of it, and so I… I… I wanted to approve, or if you will, what I reviewed so far, and I'm happy to finish that up. I should have time to finish up today, but I, you know, so… I think I answered your question.
It's a partial, I guess, from what I reviewed.
Trask Stalnaker (Microsoft Corporation) 00:24:11 Yeah, so, yeah, if you can… yeah, that would be awesome if you can.
Finish that up and, you know, leave comments or leave an approval.
And then… Yeah, I will… let's… definitely something I can… look at. Also… Cool, and I forget, does, you are in… okay, we will need one more green… Check mark.
But we'll get… we'll get there. So, Nikhil, the… the technical merge requirement is two green check marks.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:24:57 I see.
Trask Stalnaker (Microsoft Corporation) 00:24:58 So… But basically, other people's approvals help us to, then the… folks with the approval… formal approval rights, take those into account when we're reviewing it. So that's a great step that we've got a few people reviewing it and approving it already.
Liudmila Molkova 00:25:23 And I'm also quite interested, thanks for working on this, I'll take a look.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:25:29 Thanks, Ludmila. Yeah, I know, I didn't… I know you were out, so I didn't wanna, just back, so I didn't wanna, like, bother you with it.
Liudmila Molkova 00:25:38 No, no worries, was bothering me, but yeah, it might take me a few days before I get to it. Thank you.
Nikhil Chitlur Navakiran (Microsoft Corporation) 00:25:45 Sounds good, sounds good.
Trask Stalnaker (Microsoft Corporation) 00:25:50 All right.
Surya, moving on.
Surya Teja 00:25:56 Yeah, so I just wanted to carry forward the yesterday's discussion.
For agent duration, I think we are counting when… when we have nested agents, between each other. So, did I understand that correctly, or, Are we working on, figuring out what is the correct way to measure the end-to-end duration, when agents spawn subagents and stuff?
Liudmila Molkova 00:26:32 Yeah, I think that the thing we discussed before, the 385, it's one of the attempts to solve this.
And there are a couple of other.
Proposals that are similar, but essentially the goal is to mark The outer.
Agent execution, or workflow execution, or whatever, author.
Surya Teja 00:26:56 Yeah.
Liudmila Molkova 00:26:57 In some way, so that we know it's the author.
Surya Teja 00:27:01 Yeah.
Yeah, sorry if I'm cutting you, but I saw the Tern PR Ludmila.
Liudmila Molkova 00:27:11 meet.
Surya Teja 00:27:12 a lot of sense because when you see the whole operation, I, as a consumer, would love to understand how many tokens it has taken to complete the work that I asked it to do, and then what is the duration for that. And it made a lot of sense from that perspective.
And, when I was trying to understand if I can merge both the workflow and agent spans.
The agent duration was sticking as a sore thumb, because I was not sure how to individually differentiate between the workflow duration and agent duration.
And When I was researching, I thought that this is not correctly representing it. So now, say if you… Represent the turn duration.
You give the whole duration it took for completing the set of work that the user asked.
The agent or workflow.
Oh.
Yeah, that's the question. I'll stop here.
Liudmila Molkova 00:28:17 Is there PR for TURN? I think there was an issue, and there were some discussions.
Surya Teja 00:28:23 Yeah, there was no PR actually. I guess you prototyped it, right? I took a look at that. Hmm. Not this.
Liudmila Molkova 00:28:31 Yeah.
Surya Teja 00:28:31 On the…
Liudmila Molkova 00:28:33 is.
Surya Teja 00:28:34 Workflow and agent merge issue.
Liudmila Molkova 00:28:39 7s… 7?
This one.
Surya Teja 00:28:45 Yeah, 477, yeah.
I don't remember the person's name, RK something.
If you just go down, you just… Yeah, below has you prototype something once, turn and.
This thing, right?
Liudmila Molkova 00:29:08 Yeah, there is… there is a prototype. I… I think I've… I need to refresh my memories on this one. But let's imagine we did this. So maybe we can… it's two related problems, but they are also not… not… have different solutions, so there is a problem of, okay, invoke agent and work… and invoke workflow are the same thing, maybe we should call them in some way and still have some means to understand, like, like, what it is.
And then there is a second question. Agents can be nested, you can have workflows nested under agents, workflows nested under workflows, agents nested under agents, any combination of nesting.
Bye.
And.
For this, we probably need some attribute with some naming that identifies one of them as the main.
And the others as sub.
And what would it be? This is the… The other problem.
And it's… it sounds like, currently.
Or… what should we focus on first?
Surya Teja 00:30:24 Yeah. I… When I was giving it a thought, I feel that Aaron's main agent, that makes sense. We can first push that.
And mostly, if I speak from coding perspective, I spawn sub-agents to do some tasks and get send the results back to the main agent. So having that clear demonstration around main agent, demarcation between main agent and sub-agents is going to make our life easier. And individually, when I see How much time each agent took.
It gives sense to me to see each sub-agent took this much amount of time, and this is not rep… the main agent time is not represent… is representative of all the sub-agents, so that makes sense to me.
Yeah. So, I'm leaning towards pushing main agent that Aaron was working on, and then… Looking how the attributes are going to work.
On the histogram, when we plug in this, main agent as the dimension, and the agent names as the dimension.
Liudmila Molkova 00:31:38 Then you're probably interested, the Aaron's PR does not solve that problem. It would stamp main agent under a source.
But.
It would be the same everywhere, like it would not be a distinguishing factor between sub-agent versus the main agent.
This from the 385.
is, and there are a couple of other… oh, there is an alternative 355.
And I think Redeemer created this show at some point.
So it would be cool if you looked into this one and share your thoughts. And it's in draft.
Surya Teja 00:32:19 Yeah.
Liudmila Molkova 00:32:19 The first reason is because I I wanted, us to first focus on the the entity and the naming for the main agent, but also because there are, like, two or three alternatives.
And if people have opinions or preferences, it would be awesome to know.
Surya Teja 00:32:39 Yeah, sure, I'll take a look at this, yeah.
Liudmila Molkova 00:32:43 Yeah, thank you.
Trask Stalnaker (Microsoft Corporation) 00:32:50 All right.
Next up, Felix.
Felix Becker 00:32:57 Alright, yeah, I brought this up, on our last Thursday, A stabilization meeting, too.
But, something that we've run into as we wanted to add more support for OpenTelemetry, on our server side, is that there's currently a bit of an impedance match between What we call the inference span in the spec.
And what is also, determined to be, like, the operation… the chat operation, and what is assigned in all the instrumentations to, like.
One call of the… Anthropic Messages API, or the, like, OpenAI Responses API, or Text Completions API.
And the… Kind of… The crux here is that.
While the conventions are all written with kind of this client-side lens of only instrumenting an SDK, and from a client-side perspective.
one call to the messages API and… or responses API or text completions is, like.
One call, and so, it treats it as one call to inference.
Those calls actually involve multiple calls to inference.
Because all the major providers I'm aware of support, like, have a server-side tool loop. in, like, the responses API and the messages API. So, things like web search, web fetch, direct connections to MCP servers are all implemented on the server side.
And so what actually happens is you call responses or V1 messages.
there's an inference call that might issue a tool call, then we run the web search on our server, then there's another inference call that could issue another tool call, or an MCP call, or something, then we do another inference call.
And we would like to represent those inference calls truthfully, but we don't really… Like, the spec doesn't tell us which span type to use for each. And the problem is similar with the invoke agent spans, too, which… There also are multiple sub-inference calls, but… Those are not actually, like, you know, because they already have their own tool loop, they don't… they actually go straight to the model, they don't necessarily go through the same, like.
B1 messages that then runs the server-side Tolu again.
And so… It's currently not really clear, like, which of these spans should be And inference spans, which of these should be the… the chat operation.
And you're kind of forced to… Set it inconsistently, or leave some span not, annotated.
Curious.
Liudmila Molkova 00:36:17 The… Or is the goal.
For the clients to show what happened on the server better, because server returned it in the response through the server tool call information.
Or to emit it from the server side itself.
Because depending on this, the answer is very different.
Felix Becker 00:36:46 The intent is submitted from the server, if that's what you're asking. And they're like.
The obvious, like, thing here is, like.
If, let's say, a user defined, like, a dashboard that ranked their, like, kind of median or, like, distribution of how long inference takes, right?
And they want to compare that across providers, or they want to just, like, track reliability and compare to SLAs or whatever, like.
this actually gives them… if we… this actually gives them the impression that inference actually takes way, way longer than it really does, because some calls to, like, the Messages API could take three times as long, because there was actually 3 inference calls with tool calls in between, and they're all just, like, one span. So that's the motivation for, like, wanting to… Have its own span that actually represents the inference.
And then also because, you know, you want to track the, like, tool execution time separately.
Aaron.
Aaron Abbott (Google LLC) 00:37:55 Yeah, I shared an issue in the chat and in the docs. It's number 231. I think it's pretty much like the… Maybe it's a sub-issue of what you've described here, but… It's for the inference engine conventions.
Felix Becker 00:38:09 Yeah. I think…
Aaron Abbott (Google LLC) 00:38:10 Maybe we discussed it partially in the context of like open source serving ones like VLM and such.
But yeah, like, I think… I think layer 2 is the proposal here. Yeah. Inference server.
Felix Becker 00:38:25 Hmm.
Aaron Abbott (Google LLC) 00:38:27 I don't know, I feel like if we had… Sorry, go ahead.
Felix Becker 00:38:32 So we put different attributes… For the server.
Aaron Abbott (Google LLC) 00:38:40 Yeah, and I think, so also there's this concept of internal, this fan kind, I don't know if you've seen it, but.
We don't have internal or server right now for any space. Yeah.
Felix Becker 00:38:52 That's, such a… Okay, so this would be… So this would… this would be a new span kind, genai.inference.server.
Liudmila Molkova 00:39:05 Spend type, yeah.
Felix Becker 00:39:07 Okay, and then what is the GenAI.operation.name for that spam kind?
Aaron Abbott (Google LLC) 00:39:16 Good question.
Liudmila Molkova 00:39:18 I think it's… it's more of a… Do we… we have a lot of people who are interested in this, and I am aware of two different groups. The first one is Alibaba folks.
There is another issue from them for aid I posted in the chat.
And there is a interest from Llmd.
To… Define the server side.
Metrics and traces, and I think that people… somebody on this issue for a rate is act… it has some document shared, Google Doc, and they are very interested in finding Kalais.
So, like, we can define these conventions, we can discuss the details, but I think we need a group of people who would kinda work together to build the first Draft, approve, and… Alright. Then it can move forward, and… The what the operation name would be is whatever you'll decide.
Felix Becker 00:40:27 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:40:30 So, I have a question, so, inference.
For one is, like, is this really, This doesn't seem so much like an inference server span, like, this is still a client.
call the inference server span to me, I would think would be on the other side of that.
potentially… And, I mean, I… Kind of, this made sense to me, of.
Essentially renaming what we call inference to chat.
To reserve, then, inference for… The actual inference call.
Felix Becker 00:41:21 Yeah, yeah, I basically, I think, like.
the current… we call the chat span the inference span, but it's not actually the inference span, and that's… that name is only internal right now in the schema. It might become public soon.
But, it would be nice to maybe rename The span, so that we can… not, like… Not, encode this misnomer forever of, like, inference span not actually mapping to… The real inference being done.
Aaron Abbott (Google LLC) 00:42:00 Any alternatives you had in mind, Felix?
like it's like Api inference or something. I don't know.
Felix Becker 00:42:08 Yeah, I mean.
honestly, for all I care, we could just use, like, the operation name, it could be chat, you know? I'm gonna tell you I want messages, but, you know, I don't… I'm not dying on that hill.
Trask Stalnaker (Microsoft Corporation) 00:42:31 What? Yeah, I mean…
Aaron Abbott (Google LLC) 00:42:32 result.
Trask Stalnaker (Microsoft Corporation) 00:42:33 The most common… term for… the, like, when you talk about that, the open, open API, or.
the different clients.
What do they… Call it. Do they call it inference, or do they call it chat, or do they call it something else?
Felix Becker 00:42:55 I don't think any API I'm aware of calls the public like.
API that users interact with in Friends.
Like, you know, OpenAI has responses, Anthropic has messages, What was Gemini's or for?
Aaron Abbott (Google LLC) 00:43:14 Generate content.
Felix Becker 00:43:15 generate content.
Liudmila Molkova 00:43:17 And now interactions, and every… each of them has a couple of, maybe not Anthropic, a couple of versions of different names. But also, it's the… the namespace, right? So it's Create Message, or… Create interaction, or generate content.
Aaron Abbott (Google LLC) 00:43:37 Yeah, I mean I feel like call model call or something like that is pretty agnostic, and probably everybody. I I also just asked AI what it thought because it's yeah.
It's good, this kind of thing.
Felix Becker 00:43:48 Ha ha ha.
Aaron Abbott (Google LLC) 00:43:49 the.
Felix Becker 00:43:53 What did it say?
Aaron Abbott (Google LLC) 00:43:54 Yeah, it's a bottle.
Invocation or something like that.
Call him mom.
Liudmila Molkova 00:44:00 model.
Felix Becker 00:44:01 Well, it's… it's not a model invocation, like, that's the whole point, I think. Like, it's… it's actually the invocation of an API that provides a server-side tool loop, and then calls the model.
Like, in a way, it's almost an invoke agents ban, but I think there's maybe still a clear distinction between He is like.
simpler, more low-level APIs, like text completion, messages, and, like, Invoke Agent, which is, like, you know, hosted agent products.
Aaron Abbott (Google LLC) 00:44:37 Yeah.
I mean, I don't want to get too pedantic, but, like, when, say, you talk to, like, a database, right? You use, like, a database client driver, like, say, it's just, like, the JDBC or whatever, like, it… It's gonna go through several hops, it's gonna, you know, resolve to a shard or something like that, like… You might not be doing the query exactly, but from the client's perspective.
it doesn't, it doesn't know any different, I guess, like maybe in the case of most of these models, but for example, like VLM or, or Olam or whatever you use, open it, you can use the OpenAI client and it doesn't know the difference, right?
Felix Becker 00:45:14 Yeah, I mean, if you are only using SDK, instrumentation, but we do want to emit these from the server now, so I guess that's, like, what's…
Aaron Abbott (Google LLC) 00:45:23 Yeah.
Felix Becker 00:45:24 What's making it observable?
I honestly, I feel like the most, also, like, you know, backwards compatible thing to do here would be to just… Like.
keep the chat span, like, keep the chat operation name attached to what is the, like, call to text completions, chat completions, or responses, or messages API, or generate content.
And maybe just also name the internal type that, and, like, just say, this is the chat span.
And.
Liudmila Molkova 00:45:58 I think we will… we cannot do this, because we need to find the operation name, there's 3.
Defined, and we also need a metric name.
We would… And I think that I made a joke that the chat is so 2023, but it is.
It's like, not the…
Neil Yashinsky 00:46:20 people did today.
No.
Felix Becker 00:46:24 Yeah.
Neil Yashinsky 00:46:25 Yeah.
Felix Becker 00:46:25 I agree with that.
I.
I mean, I also, honestly, I was never quite sure what the other, like, operation names were for, because it's like, what was it, like, generate text? and chat, but, like, chat also generates text. Like, they all generate text, it's an LLM, right?
Liudmila Molkova 00:46:48 Is there a problem? Sorry, Ankit. Is there a problem in having client in French?
Maybe server inference and internal inference?
Felix Becker 00:46:59 I think that could work too.
Trask Stalnaker (Microsoft Corporation) 00:47:01 what's.
Felix Becker 00:47:01 There are a lot of hands up, please just go.
Liudmila Molkova 00:47:06 The real inference.
Trask Stalnaker (Microsoft Corporation) 00:47:09 Oh, okay.
Liudmila Molkova 00:47:10 Yeah.
Trask Stalnaker (Microsoft Corporation) 00:47:12 So not internal kind spam kind internal.
Liudmila Molkova 00:47:16 It's been quite internal.
So there will be 3 spend types.
Server, client, internal.
Trask Stalnaker (Microsoft Corporation) 00:47:26 this would be server, but that… I mean, I'm assuming that this is making a call to a… Oh, that's actually… maybe I… Is this making a call to another service?
To do the inference, or that's running locally?
Felix Becker 00:47:41 I think that's, like, an implementation detail off The, like, model provider, which… it's, like, up to the model provider whether they want to expose that or not. Like, the… the implementation of this OpenTelemetry emission doesn't necessarily reveal, like, every, you know, internal detail of the architecture of the model provider. It's… it's a little more… You know… Just… Choosing what to expose and how to represent it to the user, so I think… I think that difference doesn't matter as much. What matters more is, like, separating inference from the tool calls.
Trask Stalnaker (Microsoft Corporation) 00:48:24 All right, Ankit, let's go to hands.
Ankit Singhal 00:48:27 Hey, one quick question here, so… Are we trying to… So the chat span, at least on the client side, it's defined as… either like modeling responses or chat completion, right? Or interactions in case of Gemini, right?
Are we trying to break that down into… Into more granular operations on the server side?
Felix Becker 00:48:53 Yes.
Ankit Singhal 00:48:53 Been your client for.
Got it, okay.
And, like, would the chat server span not… Cover that in the sense from like on the server side.
Okay, so we are trying to get that into more granular.
Good galaxy.
Felix Becker 00:49:14 Yeah, like.
Ankit Singhal 00:49:14 Hmm.
Felix Becker 00:49:15 Client side, the chat span is already just the, like, the entire call.
Ankit Singhal 00:49:21 Yeah.
Felix Becker 00:49:21 And then there's a, you know, mirror equivalent for the server that maps the entire call.
Ankit Singhal 00:49:28 But this is.
Felix Becker 00:49:29 Then you have to sub-inference, like, the actual inference calls.
A subspans of that.
Trask Stalnaker (Microsoft Corporation) 00:49:41 Aaron.
Aaron Abbott (Google LLC) 00:49:43 Surya, were you before me?
No, okay. No, I was just gonna say, like, yeah, I think… Curating the spans that you show customers is something we're struggling with right now. Like, traditionally in OTEL, it's… very much like… I'm looking at the infrastructure and the the structure of the trace is kind of like the reality. It's not something that that we necessarily design. So I say, there's like 4 levels of load balancers.
under the inference span. Like, I think that or what we see in this picture here, like, they're both really clear to me.
I I think.
like just having the internal or or server side inference spin.
And then, looking like the example traces it, it seems fine to me like a It'll be pretty clear.
Liudmila Molkova 00:50:36 And we want to record, like, the more details that what happened on the server side.
I think Dylan has a good issue about how to represent the steps.
Model took… Or.
on that span. For metrics, we could have additional information that it… I don't know, this is something more complicated. But it pretends to be an inference, right? It wants to look like an inference. It's behind the API that Could be just in France.
You probably don't even know from the client side how complex would it be.
Felix Becker 00:51:21 I think that depends. I just think these APIs have evolved, like, they used to just be inference, but now they're, like, pretty clear about… exposing a lot of, like, more high-level features, like MCP and, web search, and, like, that are very clearly not.
inference. So, like, yeah, if you don't… if you don't enable any server-side tools.
it maps one-to-one to just one inference, which you can still show, right? You can have… the higher level… I don't know what to call it anymore, but, like, the chat's bad, and then you have just one inference call underneath.
I also don't like Chad, by the way. I hate the name.
Liudmila Molkova 00:52:08 If we can find a name that's, like, generic.
And not tied to a specific KPI.
But more expressive than an inference.
It would be an excellent moment to make the change, because we… Bye.
We are… For the stabilization, right? Whatever we pick would stay for quite a bit.
Felix Becker 00:52:32 And, Trask showed this PR to, like, their core OpenTelemetry spec, where, like, the type of the span is gonna, like, become an official attribute, and so that would… that would really… you know, tell every user out there that, like, now this is what the inference span is. Right now, you know, there is still an opportunity to kind of just change it, and it wouldn't even be observable.
Liudmila Molkova 00:53:00 Right.
Felix Becker 00:53:02 I have a question.
Aaron, for, like, the proposal that you linked. I saw… that was also the reason why I opened a new issue. I saw this proposal was mostly focused on, like, like.
like, LLM engines, which I'm not sure I understand correctly what that is, but is that more like a kind of proxy, or what,
Aaron Abbott (Google LLC) 00:53:28 You're talking about, for… 2, 3.
Felix Becker 00:53:33 one.
Aaron Abbott (Google LLC) 00:53:34 2, 3, 1.
This was from Alibaba, I think, and my… my understanding is they're talking about VLM, TGI, like, that's just the examples they gave there, TensorRTLM, so I think it's supposed to be the actual, like, inference engine, the thing that executes the inference for… Okay. Kind of self-managed infra.
Surya Teja 00:53:58 Yeah, that was my question too, because if, say, Anthropic is emitting those spans, they have something similar to VLLM. Are you going to instrument them and emit them as your own spans, was my question actually.
Felix Becker 00:54:22 I'm not familiar with BLM, to be honest.
Like.
All the implementation that I'm working on is on the API layer.
So I just, I just want to like emit, Separate child span.
That actually represents to, like, the internal inference call.
Aaron Abbott (Google LLC) 00:54:44 Yeah, I think it's okay if you don't have the internal span, like just you'd have client and server.
Felix Becker 00:54:51 Yeah, like, what I see in the example trace here with, like, engine prefill, engine decode, I don't think that's something, like, At least I hadn't had any customer, you know, ask for that.
But the, like, customer case for us is, like, separating the tool calls from actual inference, so you can… you can properly track how long do inference calls actually take, and how long do tool executions take.
Liudmila Molkova 00:55:22 It's turtles all the way down, so you're interested in the layer of inference that's The server processing this.
client.
Chat call, whatever. Then there is the portion of real inference, and there are people who want to break this real inference down into smaller pieces.
Felix Becker 00:55:43 Yeah.
It's true, it's kind of true.
Trask Stalnaker (Microsoft Corporation) 00:55:48 I feel… yeah, I feel like we… What makes sense in my brain, at least, is two different names. I mean, like, we need a name for this thing.
Had a name for this thing.
This thing feels to me like… I guess it could be a client or internal span, depending on the implementation.
And I don't know, like…
Felix Becker 00:56:13 The proposal from this issue kind of makes sense.
So I think, as I understand it now, it proposes all three layers to be added.
And then I really only care about adding up to layer 2.
I don't care about layer three.
But just having Layer 1 and Layer 2 separated, I would be happy.
The… the one thing that you mentioned is maybe, yeah, that's a little fuzzy, because what is a client and what is a server?
changes depending on the context, right? You can say, oh, client is only, like, the SDK, and everything past that is server, or you could say, no, and we actually do represent, like, the internal architecture of our, like, platform. For us, we made the design decision on basically the the entire Cloud platform is just one monolith to our customers, and we don't expose our, like, internal architecture, and so… For us, everything that happens past our edge is just an internal span kind.
And we don't go into, like, that amount of detail, and we only expose what you can already get through the API, because you know, I also don't want my security team to be mad at me for, like, exposing some, like, internal architecture details.
Trask Stalnaker (Microsoft Corporation) 00:57:41 Ankit.
Ankit Singhal 00:57:42 Hey, I'd like to add one… one detail.
So, for example, if I'm using an Llm. Right where I don't use any server side tools, assuming that I'm just using a plain Llm. Right?
And then I use tools which are defined on my side as a client, right? And when I orchestrate this, where Adam says, hey, I want to execute a tool, right? And I execute a tool.
Right now, when we model that, it shows up as It's a chat spam, an execute tool.
And probably in another chat span, right?
And if there are multiple tools, then this goes on, right?
And so, for example, if I take the same code and execute it behind a service, right, and similar kind of an API, like a chat completion or interactions.
I personally wouldn't expect the behavior to be, like, the places to be very different, right?
But here, I think we're talking about these two behaviors is going to be very different, because in one case.
On the server side, I'm going to have a new spanned type that we are mentioning out here, the inference. But if I probably run the same thing on the client side, the same logic, then I'm going to see a very different trace structure.
Felix Becker 00:59:02 So I'm not sure I'm following.
Ankit Singhal 00:59:04 So, for example, whatever logic is happening behind the service, right? If I run that same logic on the client side, right, just on my machine.
Perfect.
And I'm calling an LLM that's right now is modeled as a chat spam, right? And then LLM tells me, hey, you need to call that tool.
And that's captured as an execute tool span.
and then your code executes that tool, get the result, and you pass it on back to the Llm. And Llm. Say, okay, this is your final result. Right? The hierarchy that you see is a chat span.
An execute tool, a chat span, which are all syntax, right?
I know.
Liudmila Molkova 00:59:41 Imagine if you run it locally or if you use somebody else's infrastructure, you should probably see slightly different pictures.
Not, not like… Completely different, but relatively different. The dashboards, if you run it locally, and if you run it If you're… if somebody else runs it for you, it would also be probably Slightly different. I kind of like the separation for real inference and not real inference, because, like, things like the server tool results or the tool definitions would be different. And attributes on the spans would be slightly different.
Ankit Singhal 01:00:22 Yeah, but then here, I think we're talking about, like, a span, which… I never see right an inference span when I'm running the same code locally. Right?
That's what, like, I'm… Trying to understand, like, why would there be such a difference when it runs behind, like, if I run the same logic behind some infrastructure, right, which a cloud provider provides.
Trask Stalnaker (Microsoft Corporation) 01:00:46 Sorry to jump in here, but we are…
Ankit Singhal 01:00:48 Yeah, and I'll be almost at that.
Trask Stalnaker (Microsoft Corporation) 01:00:50 We're overtime officially.
Yeah, good discussion, obviously.
A lot of interest in this topic, so… sounds like something we can… Keep making progress on.
Neil Yashinsky 01:01:06 Thanks, Trask. Thanks, everyone.
Liudmila Molkova 01:01:07 Thank you.
Trask Stalnaker (Microsoft Corporation) 01:01:09 I…
Ankit Singhal 01:01:09 Bye.
Nikhil Chitlur Navakiran (Microsoft Corporation) 01:01:11 Thanks. Bye.
