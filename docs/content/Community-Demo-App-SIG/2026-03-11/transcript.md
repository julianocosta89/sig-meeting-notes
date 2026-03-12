SIG: Community Demo App SIG
Date: 2026-03-11
Duration: 35 minutes
Zoom Recording URL: https://zoom.us/rec/share/MvvVIous9LTGwHGTpQaI71_LZUyHFJaryQf0oouLiqrooTkGWkT_JMPWKuaBsRLQ.8j0ft7UFWHuYYTbZ
============================================================

## Zoom Recording Transcript

**Cyrille Le Clerc** 02:16 Hello?
**Donal O'Sullivan** 02:24 Hey, Sarah.
**Cyrille Le Clerc** 02:26 How are you today?
**Donal O'Sullivan** 02:28 Where'd yourself?
**Cyrille Le Clerc** 02:30 Good, good, let me choose a vendor-neutral background.
**Donal O'Sullivan** 02:37 I should have one myself, actually.
**Cyrille Le Clerc** 02:40 We have a very nice northern light, so… Hello, everybody.
**FELIX GEORGE** 02:50 Bye.
How you doing?
**Cyrille Le Clerc** 02:54 So, giuliano dropped a message, he will not be able to join.
We have many people on the call. Maybe we can start with a… Small round of introduction.
I can start, so my name is Ciri Leclerc, and I am…
As I am a maintainer of the Hotel Demo, I've recently been promoted as a maintainer.
And then, as you could see, I work for Brafana Labs, but it's not the most important thing of,
this, SQL.
And I like to contribute to…
Making, hotel demo really, production-ready, user-friendly, easy to get started, while being also production-grade.
Maybe we can, move next to, Gerard, or Gerard, I don't know how we pronounce your name, you are the next one on my, Zoom.
**Gerard Vanloo** 03:59 Gerard. Gerard. Hi, I'm Gerard. I'm working at IBM Research. Actually, I posted a couple of PR historical demos to help bump some of the,
the image dependencies, I think sometime last year, in the… around summertime.
And, yeah.
**Cyrille Le Clerc** 04:23 Okay, run.
**Rohan Arora** 04:24 Yep, so, continuing with Gerard, I'm from IBM Research as well. So, we've been actually been using, Hotel Demo as our, front and center application in an effort called as ITBench, which is like a benchmarking effort, particularly targeted around, you know, all these
wave of AI SRE agents, which we have been having. So, yep, that's, that's me.
**Cyrille Le Clerc** 04:51 Yay.
Thank you.
Jonathan?
**Jonathan Munz** 04:56 Hey, yeah, I, work for Embrace,
we're focused on, client SDKs for OTEL, so mobile and web.
For the demo, I've largely been focused on the React Native app, in the demo to get an example of a mobile SDK in the hotel demo.
**Cyrille Le Clerc** 05:21 Thank you. Donald?
**Donal O'Sullivan** 05:25 Hey guys, yeah, so I'm, I work for Elastic, I'm a contributor to OpenTelemetry, and lately been kind of contributing to the demo, just trying to, you know.
get it stable. There's a couple issues, I think, at the moment, just with, like, our own memory issues, that kind of thing. So, for us, we kind of want to have a nice stable demo, just something we can use, you know, to demonstrate our own…
distributions of open telemetry, but yeah.
That's me.
**Cyrille Le Clerc** 05:54 Perfect. Felix?
**FELIX GEORGE** 05:57 Hi. So, I'm Felix George, I'm from IBM Research, part of Rohan and Jara's team. So, I'm first time coming, joining an OpenTelementary meeting. Yeah, been previously worked with, Kubernetes 6 projects.
From, open source perspective, yeah, other than that, I'm pretty new to OpenTelemetry.
Well.
**Cyrille Le Clerc** 06:26 sorry, yup.
**Divya Pathak** 06:33 Yeah.
Hi, so I'm Daveya, I'm also a part of IBM research team here. So, I have been contributing to OpenTelemetry for the Gen AI perspective. This is the first time that I've joined this call for the demo. So, as Felix said, right, so we have been working on AI agents, and on ITBench, we've been using this hotel demo.
And, yeah, so that's all from my end.
**Cyrille Le Clerc** 07:00 Okay, thank you. On Anoushka, I think, and last but not the least…
**Anoushka Nag** 07:04 Hi, I'm Manoushka, I'm also a part of IBM Research, and this is my first call with OTEL, I'm pretty new to it, and I work in the AI for IT automation space.
Yeah, that's on me. Thank you.
**Rohan Arora** 07:19 We also have Muduch here from IBM Research at, yeah, so…
**Mudit (IBM Research)** 07:24 Yeah, he said last, not the least, so maybe…
**Cyrille Le Clerc** 07:27 Oh, sorry, yeah, my, mistake. So many, people.
**Mudit (IBM Research)** 07:31 Yeah.
Okay, so hi everyone. I'm Mudit, again, part of IBM Research.
have been heavily using various kind of demo microservice-based applications over the years, and more recently, in our efforts on ITBench, heavily used Astronomy Shop, the hotel demo.
And also, we have been, from hotel perspective, we have been working on, tail sampling and bringing a new tail sampling processor.
for, trace volume control, last year. And more recently, we are starting to look at, different agentic benchmarking applications, and this is a reason why we all are here, to share and discuss with you guys that
What we have, and any feedback from you guys that we can get.
And also, looking for, adoption, going forward.
**Cyrille Le Clerc** 08:29 Yay.
Thank you very much. So, you dropped in the agenda a proposal, to present your,
Atlantic version of Astronomy Shop, which is very interesting to many of us, I guess. Are there other topics that, people want to bring today?
Oh, Chenoya, you just, joined.
You want to do a quick intro?
**Shenoy Pratik Gurudatt** 08:56 Yeah, hi everyone. I'm Shinoy Prateek from the open search team at AWS. I'm also one of the approvers of the hotel demo.
I'm looking at the proposal, looks pretty good. Surely would like to see the demo. What do you guys have?
**Cyrille Le Clerc** 09:13 Okay.
**Mudit (IBM Research)** 09:14 Okay.
**Cyrille Le Clerc** 09:15 Maybe before you do,
Any other topics before you do your demo? I'm not sure we have… I look at the ongoing PRs, you know, seeing…
I don't know if there is something people want to discuss.
Or are the issues?
People are always welcome to contribute.
maybe… do you have a link to the open source code of your demo, of what you're going to demo today, or not, that you could drop in the Google Doc?
**Mudit (IBM Research)** 09:47 Not yet, but we would like to go in that path, and before we go there, we just wanted to get the feedback from the community.
That, you know, if there are areas we should enhance on, or what should really be the process like, right? We should first open source, and then try to get it incubated in Hotel Rapo, or…
We are just here for the feedback.
But we do have the demo, we do have the code with us, but not out there in public yet.
**Rohan Arora** 10:18 Yeah. Okay. And the objective is to have it out there in the open, right? So, and the way we have been wearing this hat is.
that the current microservice implementation is one implementation, and with the world heading towards agentic applications, this is going… this could be that complementary set, and just like how Hotel Demo is, like, front and center application, which all the APM tools in the world use to showcase their capabilities, they would be using this agentified version of Astronomy Shop to be able to showcase that, right?
So that's… that's the intention, and, yep. So, Mudit, is Felix gonna be driving this, or…
Vivian?
**Mudit (IBM Research)** 10:57 Yeah, I think we have set the context, right? And this is the very purpose we went after this, and given our past experience with Astronomy Shop, which we have heavily used in our other open-sourced work on ITBench.
We thought that it's a very good candidate for identifying it. So, maybe, Felix, why don't you share the architecture once, and then let's dive into the demo.
**FELIX GEORGE** 11:24 So, yeah, so as all of you might be familiar with this architecture of the,
Autel demo application, astronomy show. So, basically, we have identified it just, you know… So, the front end, which invokes all other microservices, they have considered as tools here, and you can chat with the agent here, like, for example, here, instead of the HTTP queries.
From the front end, it will be the natural language request from the chatbot, or we have any version of Asian load generator.
So the queries go into the agent, and the agent will, here, it can be a single agent or a multi-agent application. So we have different flavors of agents, like, we have been experimenting with different flavors of agent as well. And, so here, the agent will, you know,
Use the tools, to… satisfy the user request. Okay, so here, the non-determinism in…
**Mudit (IBM Research)** 12:24 I want to add one thing here, Felix, right?
**FELIX GEORGE** 12:27 the MCP server code.
What?
**Mudit (IBM Research)** 12:31 Yeah, the communication… so all the… the web… the web of Astronomy Shop is there, but we also have an agent, and then rest of the backend microservices becomes the tools for… for the agent.
And, all the communication is happening via MCP. One thing that we have not shown here is the fault injector module. So, we also have a fault injector module currently that supports some basic fault injection mechanisms.
**FELIX GEORGE** 12:58 region.
**Mudit (IBM Research)** 12:59 and non-electric faults.
**FELIX GEORGE** 13:00 Yeah, so this, these are some of the faults that… okay, so basically, we are, we are focusing more on the agent-related faults.
Not, like, not from a microservice-related fault. Like, the agent fails because of the incompetence of the LLM, so we have to inject faults in the LLM, from an agent or from the tool server. This is mostly the microservice-level faults, and these are, like, LLM-related faults and the agent-related faults.
Okay, so this is our, we also have a module of fault injection.
Yeah, but, coming to the agent, so here, this is our basic setup, and the, so the known determinism and the costly, fare here is the, LLMs, LLM usage, right?
mostly people won't have, won't be… it's for benchmarking, they will require a lot of… lot of LLM calls, which might increase the cost. So, right now, we,
We are using a set of… a set of, crafted queries as the agent load generator.
We also have the plans to improve it into a dynamic module, but right now, it's a fixed set of queries. So, our agent will call LLM only for these fixed set of queries, and we are recording these LLM response as they come.
And it can be reused when the second time, the same, exactly same query, comes in.
**Mudit (IBM Research)** 14:23 So, it's a… just to add feelings, right? So, it's a configurable thing that we have, right? If a user wants to always hit an LLM,
they can very well do so, but if not, they can as well use a recorded LLM response so that the cost of running the experiment multiple times is not too high, right? And also, this makes it… the whole idea of this is to get a look and feel and flavor of how an agent works, and given, as Felix said, right, not necessarily
We are working with a very limited set of queries that the Astronomy shop agent is going to handle, so we can use caching or recorded response wherever possible as an optimization step. But again, it's a configurable thing.
**FELIX GEORGE** 15:07 Also, and one other thing is, we are using a trace loop, to get the metrics, LLM and agent-related metrics.
And, which is, you know, so we also use the, propagation, context propagation, and all the traces come, say, connected single trace. For each input query, there will be one trace associated with it. So, I will move to the demo. Here, I'm running the hotel,
telemetry auto demo application. Okay. So, here I have the load generator. Sure.
**Mudit (IBM Research)** 15:43 once.
**FELIX GEORGE** 15:45 Yeah, so we also have created a custom version of the load generator, where we give the input queries as natural language. For example, this is a test query module, okay? So, here, it asks very simple questions, which are, like, mostly related to just one tool.
Okay, for, it's also tagged with which, microservice of the hotel demo application the tool is related to.
So we can just, you know, execute the tool and see what's coming in the traces.
So, it has been successful. Let me check the traces. Okay, so the, agent has executed the query, like, here you can see the input, like, what are the current promotions available on binoculars. So here, and…
like, it executes a whole bunch of tools, in the auto demo application, and you can see the final output. Jeez.
this, okay, binoculation, root, binoculation, sale. Okay, so this is our whole idea, to capture the complete trace, from an agentic perspective, how… how the agent writes the…
Okay, so…
So, here, okay. Now, we also have another set where we have multi-category queries, which is, like, the question is a little bit more complex, which involves the usage of multiple… sequential use of multiple tools.
Maybe the agent will try to get output from one tool, which is used in the following tool call.
Okay, so, the… I can execute this query.
I'll show you So, it's running, okay, I'll go back.
Yeah, it's finished.
Okay.
I think the Jaeger is having some issue.
Okay, while it loads, I will explain, that, you know, The native load generator.
So, the HTTP… we have, you know, generated the questions, natural language questions, regarding to the whatever HTTP load gen… locust load generators have…
native to the OpenTelemetry application. So, it works as it is, like, you can generate a new… you can start a new custom load test, and, you know, you can…
start it, and it will… it will keep on sending the loads, okay? So, yeah.
Coming to the earlier Christian.
Okay, so the load has started, and that's why you can see a lot of traces here. Okay, so just looking at the…
second one. Here, this was the complex query. So here, you can see it is using multiple… so each time, some Astronomy shop application is hit, that is a tool called. Here, it's asking for the list products.
And in the list products, then it gets the recommendation, and…
That's… that was our, that was what we were trying. Display the old categories of products, and recommended… recommend a popular opinion. So, for getting that, it gets all the list of products, and gets all the recommendation. From recommendation, it finally gives you the
Oh.
**Mudit (IBM Research)** 19:35 So maybe, Felix, in the interest of time, you can go to fault injection UI and the Health UI?
**FELIX GEORGE** 19:42 Okay.
One second.
Let's come back.
**Anoushka Nag** 20:01 Felix, it's 8501.
**FELIX GEORGE** 20:03 Oh, okay.
Sorry.
**Mudit (IBM Research)** 20:13 You need to share again, Felix.
**FELIX GEORGE** 20:20 Are you able to see my screen? Okay.
**Rohan Arora** 20:24 You're welcome.
**FELIX GEORGE** 20:25 Okay, thank you for the confirmation. So here, we have, different classes of faults, like reasoning faults, which are related to the LLMs, and again, LLM errors are also related to the LLM-related faults. Tool errors are where we inject, either time or, you know, latency,
error, error rate, or, those kind of faults within the MCP server or the tool construct, then we have system untreachable faults, rate-limited exceeded, agent-related faults, okay? Within reasoning, we have, faults like drift, or cycle.
Which will, drive the agent into, this… this class of faults.
For example, if I'm injecting,
these tool-related faults, sorry, reasoning-related fault, you can see that the LLM gateway is now degraded state, and all other components are, like, MCP Server and the tools, okay, all of them are…
**Mudit (IBM Research)** 21:23 You can also click on Shoot.
**FELIX GEORGE** 21:26 Hello?
**Mudit (IBM Research)** 21:28 Yeah, you can hit on Show Tools also, so basically.
**FELIX GEORGE** 21:30 it's…
**Mudit (IBM Research)** 21:30 the fault injector, as well as
some sort of, health UI as well that, at any given point in time tells you that what is the state of different components in the agent.
And, as Felix said, right, we have a mix of both agentic and non-agentic faults, and at different modules of the agent.
**FELIX GEORGE** 21:56 So…
**Cyrille Le Clerc** 21:56 Okay.
**FELIX GEORGE** 21:57 Let me check if I'm able to…
Load it again and show the faults with some error traces.
Oh.
and my good.
**Rohan Arora** 22:09 Yeah. So, Felix, I think, you know, from the application perspective, right, I know it's more for us that we've gotten into the faults and whatever have you, right, to showcase the broader value, but I think for, from the OpenTelemetry demo perspective, right, the application itself
or the identified version of the application itself here is what, what brings value. So, any initial thoughts, on that, from folks here who are hearing it for the first time?
**Cyrille Le Clerc** 22:41 Yeah, first, so thank you very much, it's extremely interesting, tons of ideas. There, there is a question from Donal on the, chat.
Where is ELLM based?
I think you have… you call OpenAI, or you have the cached version, correct? Or I'm wrong.
Did you see the question on the…
**Rohan Arora** 23:04 Yeah, yeah, so, Felix can comment on this, but yeah, the expectation is that, you know, you're able to reach out to a provider, but there's nothing which is stopping us from having, like, some local model running locally.
**Cyrille Le Clerc** 23:17 And I think we already have this problem with the recommendation service today in the hotel demo, where we have the question, do we use an external provider, or do we do it with something internal that simulates?
**Rohan Arora** 23:30 Yeah.
**Cyrille Le Clerc** 23:33 Okay.
I think… can you come… can you show… share with us some traces, including some attributes of, the…
Sure, ER attribute.
**FELIX GEORGE** 23:46 Tare the trace over email, or do you want.
**Cyrille Le Clerc** 23:49 No, no, they're just on the screen.
**FELIX GEORGE** 23:51 Okay, yeah, yeah, sure. So… Yeah.
**Cyrille Le Clerc** 23:55 What I felt was very interesting here, from an hotel demo standpoint, if you can open any of them, please.
**Mudit (IBM Research)** 24:02 Okay.
**Rohan Arora** 24:05 Edit.
**Cyrille Le Clerc** 24:06 Yeah, I think we are good with this. Can you open maybe one? But here, what I like very much…
It's not exactly an hotel demo, but it's a demo of how to…
Agentify an app where we can see that you seem to reuse exactly the same code of the microservices demo?
And just plug, some AI, capable logic with the agent in front of it, so I felt this was very interesting. And with stress context propagation, we… it works seamlessly, so this…
Looked very compelling to me.
what I felt also was very… you have this… you show this kind of debate or tension, do I put an MCP server between or not?
Or do I just expose… maybe you expose the CLI, or you just expose some skills?
to your, agent to do the job directly, which I felt was
I don't know if I understood it properly, but I felt this was interesting.
**Mudit (IBM Research)** 25:12 And you were looking for context, right? Maybe you can expand on the trace, Felix?
**Cyrille Le Clerc** 25:17 Yes.
**FELIX GEORGE** 25:18 Yeah. So for, these are the attributes that we have. For example, here, what was the input, to the…
**Cyrille Le Clerc** 25:26 loop is not standard hotel, correct? But you have some standard hotel attributes, do you?
**FELIX GEORGE** 25:31 So, yes. So, the problem with… so, we can actually use the OTEL, but the problem is OTL right now doesn't support MCP or the Langraph constructs of tools. So, that was the only reason that prevented us from using Autel.
**Cyrille Le Clerc** 25:46 Okay.
**Mudit (IBM Research)** 25:48 But microservices, all the tool invocations on the microservices that… Yeah, that's from hotel.
**FELIX GEORGE** 25:57 tools.
**Donal O'Sullivan** 25:58 Sorry, just to clarify there, there… there… is that,
specific IBM tracing that you're doing there, it's not like hotel, like, vendor agnostic stuff, right?
**Mudit (IBM Research)** 26:12 No, it's vendor agnostic, right? We are using, langraf?
**FELIX GEORGE** 26:20 So, we are using TraceLobe, it's an open source project, and we are using Langraph to build the agent, so…
**Mudit (IBM Research)** 26:29 Hmm…
**Shenoy Pratik Gurudatt** 26:30 Yeah.
**Mudit (IBM Research)** 26:31 They need to… all the microservices that… from OTEL that we are using as… as backend, those are,
Those are all hotels, and collection is also via our hotel collector here.
**Cyrille Le Clerc** 26:45 Okay.
**Donal O'Sullivan** 26:47 Yeah, there is a hotel collector in the demo already, right? So we shouldn't need to…
Yeah, adding another collector.
**Cyrille Le Clerc** 26:56 Okay.
And I think we would need some people from the AI, Hotel AI, SIG, to…
for them to bring their domain knowledge of AI, but I… it looks very,
Interesting to me to also illustrate this use case.
And it doesn't seem to change that much at demo. It seems to be backward compatible and to just augment without breaking anything.
Yeah, so we also have the default.
**FELIX GEORGE** 27:31 you know, agent, sorry, auto demo application running as it is. We just add one other component which also can use the same components, which the normal, normal flow works.
So, we will add two components. One is the agent, and the other one is the agent-specific load generator.
Yeah, apart from the fault injection and the MCP server things.
**Shenoy Pratik Gurudatt** 27:56 I have a few questions,
First one is, did you guys type GenAI Normalizer? I put it in chat. This is, again, an open-source contribution that, one of my colleagues is doing.
Which normalizes the attributes that are coming in from Traceloop, Langraph, using Phoenix Arise, anything of those external tools, into what OpenTelemetry expects as attributes.
So, this may be a good…
a good tool which can help you normalize your agent span attributes and operation. For example, something like operation name, input, output tokens, even those are not normalized across these tools.
So this is…
**FELIX GEORGE** 28:42 Yup.
**Shenoy Pratik Gurudatt** 28:42 one that can help. The second thing is, I didn't see logs anywhere. Are you guys ingesting any of the agent or MCP logs?
**FELIX GEORGE** 28:54 We are, right now, we are not collecting logs anywhere.
We… we are just focusing on the traces and the, so, metrics, but… So the oxygen.
**Mudit (IBM Research)** 29:05 I mean, logs are emitted, but we are not collecting yet, right? We're not putting them in the pipeline, total pipeline.
**Shenoy Pratik Gurudatt** 29:13 You also mentioned you had a chat interface. I was, also looking if… because that feels like an easy addition to the hotel demo. Currently, if we have agent, that replaces a lot of traditional telemetry, and also the interaction between services.
So, I was just thinking, if you had a chat interface.
That can be added in easily.
And one last thing is, is this all open source? What are your plans to contribute upstream? Is one of my questions as well.
**Mudit (IBM Research)** 29:45 Yeah, so we have the chat UI,
Chinoy, for Hotel, right, where people can interact with the hotel application, Hotel demo application. And for open sourcing, I think that's where we are in this meeting, just to get some early feedback and, you know, try to contribute back.
**Shenoy Pratik Gurudatt** 30:06 Got it. Yeah, I feel the overall, intention is landing. Everything agentic and agentic tracing is on spot, along with the fault-injector dashboard. It's more similar to our feature flag service that we have.
We can also try seeing if we can enhance the existing feature flag with whatever fault-injector dashboard does.
But yes,
I would like to know opinion from others as well, like, Cyril, do you have an opinion on how we can get these things in?
**Cyrille Le Clerc** 30:39 Yeah, so I was… because we just have one minute, so my ideas was, I think we can maybe…
open GitHub issues on the hotel demo repo.
I wonder if we can break down the ideas in sub… domains?
Maybe one is with the MTP server when one other is without the MTP server. A third one would be the chat,
m Experience on, on to be able to
to progress on these, and we would be able to, with GitHub issues, we will be able to loop in some, people from the AI special interest group for them to, bring their domain expertise on AI that we don't have.
Would that make sense?
**FELIX GEORGE** 31:33 Okay, yep.
**Rohan Arora** 31:34 I think I like the idea of breaking it up into phases, right? So one… so… and I think that makes it much more digestible, because, like, things like faults and others are presently, you know, it's all, like, flag-D-based faults in…
In the core application itself, right? So in parallel to that, what makes sense in the agentic world is, is another thing which we all need to come here and define, right? So I like the idea of breaking it up into phases and going…
**FELIX GEORGE** 32:01 I wanted to say one thing, right? So, right now, we are providing the tools, and so everything is configurable, but, like, we provide the tools as a config file, a YAML file. Also, the agent is also provided as a, you know, YAML file. So, you can choose to have a multi, like, hierarchical supervisor kind of agent, or a chain agent, or a single agent, or…
a multi-agentic application, like, however you want to configure, we have… we will accept a config file, and we will create the code for the agent from the config file. So, users can actually, you know, mix and match with different configurations and identify which might be the correct
You know, agent art… Agentic architecture, they…
they will need or, you know, experiment with different flavors of HG applications. So, that customizability is there.
**Cyrille Le Clerc** 32:54 Okay.
Thank you. So please, yeah, create GitHub issues, we will have to wrap up the call.
As small as possible to start with.
So we can, move fast, because if it's too complicated, it will be…
**Mudit (IBM Research)** 33:10 No, point well taken.
**Rohan Arora** 33:13 Nope.
**Mudit (IBM Research)** 33:14 Yeah.
**FELIX GEORGE** 33:15 Thank you.
**Mudit (IBM Research)** 33:15 Thank you very much. We will discuss, yeah.
**Rohan Arora** 33:19 Yep. Thank you, everyone, for your time, and… Thank you.
**Cyrille Le Clerc** 33:23 Thank you. Have a great day, bye.
**Donal O'Sullivan** 33:25 Cool demo. Thank you.
**Shenoy Pratik Gurudatt** 33:28 Cool.
**FELIX GEORGE** 33:29 Thank you.
