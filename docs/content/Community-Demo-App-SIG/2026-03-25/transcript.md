SIG: Community Demo App SIG
Date: 2026-03-25
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**FELIX GEORGE** 01:14 Hi. Hi, Sarah.
**Cyrille Le Clerc** 01:15 Hello, good morning, good afternoon.
**FELIX GEORGE** 01:19 Good morning.
**Cyrille Le Clerc** 01:21 I'm based in France, so it's an afternoon for me.
**FELIX GEORGE** 01:24 Okay, it's, it's 8.30pm for Indians.
**Cyrille Le Clerc** 01:29 Okay, you're in India. It's quite late as well.
**FELIX GEORGE** 01:46 So, I just wanted to give you a heads up, like, I created an issue, and I have also… based APR.
So… Okay.
**Cyrille Le Clerc** 02:04 That's great. And you're adding an MTP server?
**FELIX GEORGE** 02:08 Yeah, I added two approaches. Like, there is a feature flag, which you can toggle to run it with MCP or with Langraph native tools.
So, there is a feature flag. Sorry, not a feature flag, like an NVMN variable, which you can set to false.
So you can…
**Cyrille Le Clerc** 02:27 So you said, is there a MCP, or the second one is… how is it called?
**FELIX GEORGE** 02:32 Langraph tools, native tools, So, MCD, is… Anthropic-released MCP, right? Just, it lies outside the agent, like, it's an abstraction they created.
**Cyrille Le Clerc** 02:48 Yep.
**FELIX GEORGE** 02:48 But you can either use it as MCP tools or… but the problem with MCP is, right now, because of… it is a two-way communication. So, you send a request from agent to MCP server. It's an HTTP request. You just get the request accepted or not information as the response.
The actual, tool is your tool called, response that comes via a second queue.
So there is a disconnect in the OpenTelemetry context. Because of that, you will get a… there always, whenever there is an MCP, you will get a new span created.
So that's why I kept the Langraph native tools as well, so you get the complete flow under one single Trace, I can… I can also share and show you.
**Cyrille Le Clerc** 03:37 Sorry, why? Because MCP is an asynchronous process?
**FELIX GEORGE** 03:41 Yes, MCP gets an asynchronous process. Also, the request response is also asynchronous. Means, there is one queue which the agent talks to the MCP server, and there is another queue where the response from server is sent to the agent.
**Cyrille Le Clerc** 03:58 Oh, okay, thank you for educating me on this.
I was not aware of this.
**FELIX GEORGE** 04:02 So, I can share my screen and show you. So, this is the user interface. Here I have send a request, like, what are the categories of products available in Astronomy Shop, and what products are there in each category, okay?
So… Yeah, this is the output.
For all different categories. So, if you want to… see the flow of the traces. So there's one trace here.
So, let's open it.
**Cyrille Le Clerc** 04:33 Yep.
**FELIX GEORGE** 04:34 Yeah.
So, there is one tool call associated with… So, it's, API slash products.
Okay, which will get all… which will go to the front end, followed by the product catalog to get all the products, and it will… so there is first LLM call happening here, which selects this particular tool.
List products tool.
And it will carry the list, products, and it will constrict the final response in the second LLM call.
So, all the model.tasks are related to the LLMs, tool.tasks are related to the, AP, the tool functionality calling, like, whether it's MCP or… the Langraph 980 tools. Again, here, tool.task, model.task is the first LLM call.
So here, Yeah, you can… like, I don't wanna explain, everything here. So, I also have added an LLM caching.
So, I also wanted to get your, get your feedback on, like, whatever we have done is, is a right way of doing things. So, here, the chat open AI is the default, you know.
class that I have used for, LLM calling. So I have created a wrapper here. So whenever we call an LLM, Eve,
**Cyrille Le Clerc** 05:55 Yep.
**FELIX GEORGE** 05:55 if they use VCR flag.
Which I'm… again, it's an NVMN variable. If it is set as true, then I will cache the response, LLM request and response, okay?
I can show you how it looks like.
So, it will look like… so, this will be one LLM request response object. So, this particular request came, it is cached. Whenever the same request came… comes again, it doesn't call the LLM.
Second time, it will send the response back. So, this is the idea.
of LLM request response caching. So, we can use it because, here, the set of queries a user can ask to the For example, if you are configuring a load generator, we will create a pre, some queries beforehand, right?
So, I hope that there will be a limited set of queries, and because of this set being small, we can always reuse the cache response again and again when you are running a load generation.
**Cyrille Le Clerc** 07:01 Okay.
**FELIX GEORGE** 07:02 So, yeah, so you don't have to… users can… who doesn't want to spend more on tokens?
They don't wanna… Yeah, that's… Something that I have added here.
Oh, yeah.
**Cyrille Le Clerc** 07:18 Okay, did you see, that there were some, Limited.
**FELIX GEORGE** 07:28 token.
**Cyrille Le Clerc** 07:28 There is a Slack message that was, initiated by, Sorry, let me put it here.
by, Giuliano, but we had very few Ontario.
**FELIX GEORGE** 07:44 Which one?
**Cyrille Le Clerc** 07:45 I just dropped the link, here.
**FELIX GEORGE** 07:48 Okay.
**Cyrille Le Clerc** 08:05 But, yeah… We don't have much, I don't know… can we swap MCP servers, easily, or is it complicated?
**FELIX GEORGE** 08:18 Right now we have… I have, I have created an MCP server with all the APIs that is available in Astronomy Show.
But, but we can make it easily swappable.
It's just a… Hello, you… I cannot hear, you are muted.
**Cyrille Le Clerc** 08:39 Sorry, yeah, I saw that the, Lude Milan, who is, involved in the, Gen AI Instrumentation said that past MCP comes with native instrumentation, so maybe there is some stuff But I, I, I don't have no knowledge of this domain, so I'm…
**FELIX GEORGE** 09:03 Okay, we… right now, I have kept everything, in the same… same container. Like, there are 3 different processes. One is agent, the other one is… chat interface, the chatbot UI, and the third one is the MCP server. If… if you make it MCP is in a different server, you can easily change the image to point out whichever MCP server image you want.
So we can make it that way as well.
**Cyrille Le Clerc** 09:32 I, Yeah, I don't know, I have not… I don't have enough knowledge on MCB Server yet to understand, And there were no content views on this thread, so, I think a challenge we have this week is that it's KubeCon in Europe, and so many people could not, In the past week, they had limited headspace.
So I'm afraid we will struggle to make a big progress this week.
**FELIX GEORGE** 10:01 Okay, I have also pasted the issue along with the PR link in the slide.
**Cyrille Le Clerc** 10:07 Come on, it's great.
**Shenoy Pratik Gurudatt** 10:11 I can take a first jab of reviewing the PR.
**FELIX GEORGE** 10:15 Thanks a lot.
**Shenoy Pratik Gurudatt** 10:15 Get to me first. I have some questions. The MCP, the chat interface, everything, is it part of container name agent in the Docker form?
**FELIX GEORGE** 10:25 Yes.
**Shenoy Pratik Gurudatt** 10:25 Oilty.
**FELIX GEORGE** 10:26 Right now, I haven't made it like that, because… so, the idea behind that was, so the users, use chat interface only along with the agent, right? So, I couldn't find any separate instance where you have to scale them independently. Like, scale just UI, or scale just agent.
I couldn't find a use case where that would happen.
So that's why I kept it together, but if you think it's a good idea to separate them out, I can do that.
**Shenoy Pratik Gurudatt** 10:54 Yeah, I'm just thinking of ways. For example, if I, Want to bring my own agent in my fork, for example.
And then, I just want to use the existing MCP server that you guys have built. That may be one of the… Things that we can do to see…
**FELIX GEORGE** 11:13 Okay.
**Shenoy Pratik Gurudatt** 11:13 pop it out. Also, I would like to know, like, do you know the individual memory consumption of MCP versus agent, and chat together.
**FELIX GEORGE** 11:23 Hmm, no, I haven't tested that out.
**Shenoy Pratik Gurudatt** 11:26 Okay, I see the total memory assigned as fine at MB for agent plus everything, so that… if we keep that, I think that should be good enough for now.
Oh.
Yeah, I don't think that that should be an issue.
**FELIX GEORGE** 11:46 So, I started with 100, it crashed. So, I made it 200, again, it crashed, so I made it 500. I didn't test in between.
I can, I can do a memory, memory, discussion.
**Shenoy Pratik Gurudatt** 11:59 what we do usually to test out memory is, like, for the other services, we have load generator, right? There is a flag for… feature flag for load generator to, bombard all the requests, or increase the number of requests, so that all the services get overloaded.
We check memory consumption of services with that flag, and put that as a limit, usually, at least. That's what we did for the past few things.
But I see you swapped out the load generator, right?
**FELIX GEORGE** 12:30 Yeah, so I didn't use the load… I haven't built the load generator yet, because here the HNDIC load will be the natural language request.
Like, for example, like, it will be the normal queries, right? How many products are there in astronomy Showport? Check out this particular product. So, we have to create a new load generator. So, we were also thinking about it. I have added my thoughts in the issue.
you can, you can take a look, like… And now…
**Shenoy Pratik Gurudatt** 12:58 Increase or extend the capabilities of existing loads and.
**FELIX GEORGE** 13:03 Yeah, yeah, that's what we were, thinking about. So, so, like, for example, whenever you create a new, like, whenever you, hit, like, start a new load, new load test, right? So, there is an option to configure the users and all, right?
You say, so request per second. So, along with that, we can also give a, radio button or slider. Like, by default, it will be zero, like, the complete load will be the, like, system load, like, no, the normal HTTP load.
But if you slide it, towards the right, then, like, for example, if it is 10, then 10% of the load will be the HTT load, and, 90% will be the HTTP load. Like, again, slide it up.
To make it 100% layers and decode. Do you think that's a good idea to start with?
**Shenoy Pratik Gurudatt** 13:52 Yeah, that's one of the ways. What I was thinking is if you have an API for a chat agent.
**FELIX GEORGE** 13:58 Hmm.
**Shenoy Pratik Gurudatt** 13:58 You can just send some, dummy… calls to the chat API directly.
**FELIX GEORGE** 14:05 We have API, we have API, but how do you configure how much load?
**Shenoy Pratik Gurudatt** 14:10 Oh, that is the setting for that in load gen data. We can increase number of users. What you can hard code, or probably keep static is the types of questions. You can have a question bank of 100 questions. Yeah, that's what?
**FELIX GEORGE** 14:24 No.
**Shenoy Pratik Gurudatt** 14:24 will just iterate through all the questions with the load generator, but it'll just use your API.
**FELIX GEORGE** 14:31 Hmm.
**Shenoy Pratik Gurudatt** 14:32 Because currently, there are two ways to enhance load generator. One is to use Playwright, where it goes to the UI, and then does some dummy clicks, writes the actual thing, and then sends some API calls using UI. The other one is to directly use API calls from Load Generator.
**FELIX GEORGE** 14:49 Okay.
**Shenoy Pratik Gurudatt** 14:49 So, you can check which one of them is easier.
**FELIX GEORGE** 14:51 No, I think the second one, we definitely… we have a version of load generator internal, but that doesn't support HTTP1, that just support… we have, you know, swapped it out. Like, it.
**Shenoy Pratik Gurudatt** 15:02 Yeah.
**FELIX GEORGE** 15:03 just, calls the API of the agent, along with the natural language request.
So, but we thought, so Gerard, so Gerard had this idea, right? So this system, like, agent-like astronomy show, it can have, users who use it traditionally with the HTTP request, like on Amazon, where you, you know, buy the stuff with the agent, or there will be traditional usage who just like to click on things and buy So, that's where the idea of the slider came in, like, 10% of the users might be using agent, like, 90% will be using it traditionally, or vice versa, right? So…
**Shenoy Pratik Gurudatt** 15:41 Yeah, Slider also makes sense, like, when you think about it from an actual user's point of view, where things will go, for example, Amazon e-commerce website, people will start using the chatbot more to order, but at the same time, there will be traditional users, so that also makes sense, if you want to keep a balance between regular load and then chat-based load.
**FELIX GEORGE** 16:03 So, yeah, I have added all my thoughts. I have dumped up all my thoughts in the issue. You can…
**Shenoy Pratik Gurudatt** 16:10 Let me, think about it a bit more to see what's the right approach to start with. We can always do the other pieces parallel.
**FELIX GEORGE** 16:19 Yeah, thank you.
**Shenoy Pratik Gurudatt** 16:24 And I think I… we discussed this last time also, did you guys take a look at.
**FELIX GEORGE** 16:29 Yes, I took a look. So, it's an auto collector processor, right?
**Shenoy Pratik Gurudatt** 16:33 Yeah, yeah.
**FELIX GEORGE** 16:36 Yeah. So, yeah, I haven't tried it out yet, but I have taken a look at it, but I'll try to… I'll try to check it out.
**Shenoy Pratik Gurudatt** 16:44 Okay.
Cool.
I think that should be good, Cyril, do we have any questions on the memory limit? Is 500 MB good?
Based on the discussion that we had had.
**Cyrille Le Clerc** 16:59 Under memory-limited profile, you mean?
**Shenoy Pratik Gurudatt** 17:03 Yeah, it's, are we good to add another service in the demo, which is 500MB?
**Cyrille Le Clerc** 17:11 I think we, yeah, we have a PR to leverage profiles in Docker.
**Shenoy Pratik Gurudatt** 17:19 Hmm.
**Cyrille Le Clerc** 17:20 compose, and I think with, Here, we will be able to activate or Disable, enable, or disable this new front end for the existing services, correct?
**Shenoy Pratik Gurudatt** 17:34 Yes, I think so.
**Cyrille Le Clerc** 17:36 And so I think we can protect memory. Does it make sense?
**Shenoy Pratik Gurudatt** 17:41 Yep, I agree to that. That's the case.
Yep.
**Cyrille Le Clerc** 17:49 So I think we would be good.
**FELIX GEORGE** 17:52 So, like, what I understand is that, I should separate out the UI from the agent, UI and MCP server, so there will be.
new additional ports? Is that so?
**Cyrille Le Clerc** 18:05 Sorry, no, I think, Pause, let me show my screen, maybe… We can completely… my understanding with your diagram, Here?
Is that we can completely disable the AI, the agentic front end, composed maybe of an agent on NCP, or maybe just agent on this.
Yeah. Don't keep the traditional.
**FELIX GEORGE** 18:41 Yeah, we can.
**Cyrille Le Clerc** 18:42 As of today's setup.
**FELIX GEORGE** 18:43 Yes, we can disable MCP, or, you know, we can choose the traditional tools.
**Cyrille Le Clerc** 18:50 Yeah, and so MCP plus agent, and we could say there is one profile which consumes a bit more memory, but which also simulates all the adjunctic observability.
And then, there is a smaller profile that excludes this.
To reclaim memory.
**FELIX GEORGE** 19:12 Okay, no, Shinoy was talking about the.
**Shenoy Pratik Gurudatt** 19:14 Oh, dear.
**FELIX GEORGE** 19:15 in the…
**Shenoy Pratik Gurudatt** 19:15 I'll tell, like, I can rephrase what Cyril is also telling, that we had one issue earlier, that hotel demo was taking a lot of memory, because of a lot of services. So what we have in plan is to create Docker profiles, so some of these will be optional.
**FELIX GEORGE** 19:31 Okay, okay.
**Shenoy Pratik Gurudatt** 19:32 Yeah, so that's one part. The other part is to decouple agent and MCP. That's the other part that you're talking about. But with these… with this, profile approach.
We can keep agent as part of Docker Compose only if users want to try everything out. And if they just use minimal Docker profile, then we might not have the agent part, because it will take some extra space.
We're also reviewing a lot of other services as well. It's just not, this part. There are some… Or features also going out, that people use with the feature flags and stuff, so… that's fine, like, that's an expected approach between full and minimal.
**FELIX GEORGE** 20:12 Okay, okay. So, so, yeah, I can, I can have that. So, it, it will be, like, but then, if we are separating it out, out as different components, then we will need separate images as well, right? For UI, for MCP server, and, like, an all-in-one image.
Like.
**Shenoy Pratik Gurudatt** 20:32 Yeah, we can think of what, what are the dependencies. Does, can MCP alone, and can Agent and, chat be one image?
Or something like that.
**FELIX GEORGE** 20:42 We can have one single image and, you know, trigger different components, like the, like, you can use the command to start the container as different, like, you know, like, pass some argument to start just MCP or just agent.
**Cyrille Le Clerc** 20:57 What is the benefit of having one single container?
**FELIX GEORGE** 21:00 Simple… simplicity, I guess, like, just one.
**Cyrille Le Clerc** 21:04 Isn't it common in containers to just have one single process?
**FELIX GEORGE** 21:09 Yeah, so my thought was, so, there is the UI, and there is the agent.
like, there won't be any scenario that… I have created an endpoint specific to agent because it will be easier to send requests directly from the request to the agent, if there is an endpoint.
Just for the agent. Okay, not via UI. UI is just for the users, okay? So I couldn't think of any, and, any, use case where we have to scale just the agent, or just the UI.
If… if we are scaling, both comes together, right? Because… But… Yeah.
**Cyrille Le Clerc** 21:50 I wouldn't be surprised if we… if we… Keep the traditional way of seeing, one container per process.
**FELIX GEORGE** 22:00 Okay, okay, I can do that.
**Shenoy Pratik Gurudatt** 22:02 Yeah.
**Cyrille Le Clerc** 22:02 Because it's, yeah.
**Shenoy Pratik Gurudatt** 22:03 We have seen people who fork the demo, and then try out their own stuff, or also contribute back.
Have, issues when this is single container.
As I mentioned, if you want to just swap the agent out and try different agents that are there in open source, like Homes GPT, for example, so it would be able to connect with your UI and then can talk to MCP as well. So it's easy to decouple as much as possible.
**FELIX GEORGE** 22:30 I can do that, yeah.
**Cyrille Le Clerc** 22:36 Okay.
**Shenoy Pratik Gurudatt** 22:39 Cyril, I saw you had some PRs out for Postgre. Long time we had some updates there.
**Cyrille Le Clerc** 22:46 Yeah, I, .
**FELIX GEORGE** 22:48 Nope.
**Cyrille Le Clerc** 22:49 I have some stuff. I clean up post-gre, because I think we should have a more realistic, setup.
The database should not be called Hotel, but should be called Astronomy Shop.
We should use… we should not use a privileged user to do monitoring. There is a role in Postgre to do it, it's called pgmonitor, and so we should create a user for this.
That's one, yeah, family of stuff I'm doing. I'm doing another family of things, is chasing semantic convention support.
So I am on, Can I share, maybe?
Our, goal… Our Go code is using a library called HotelSQL, do you know it?
**Shenoy Pratik Gurudatt** 23:48 No, I haven't seen this before.
**Cyrille Le Clerc** 23:52 So it does command SQL wrapper on, today, it's bad, oh yeah, we… I can show you how… Our instrumentation is not great today.
I've done a pull request to improve a bit, but not that much, but… Wow.
**Shenoy Pratik Gurudatt** 24:22 moment.
**Cyrille Le Clerc** 24:23 There are so many changes? Yeah.
Did I put a screenshot?
No, shame on me.
Oh.
You have 2 seconds, or you are fed up already?
**Shenoy Pratik Gurudatt** 24:39 No, no, no, no, I want to look at this deeper.
But I'm trying out some parts of DB monitoring as well, so I want to look at this in detail, what enhancement we are doing.
**Cyrille Le Clerc** 24:55 Okay, I will get it here, I think.
Did I close all my previews?
I killed all this, oh, that's a shame.
I'm sure that… Okay, we lack some attributes, like, we had very poor attributes.
Maybe I will stop sharing 2 seconds, and I will get back CPU to, Because my server is… my machine is dying at the moment. Yeah, I am chasing semantic convention support.
Oh yeah, I will be able to do it.
Product catalog, was it… Once again.
Okay.
You see my screen?
**Shenoy Pratik Gurudatt** 26:01 Yep.
**Cyrille Le Clerc** 26:07 So, here, Project Catalog, which is a Golang application using the HotelSQL instrumentation library is doing a database call, select PID blah blah.
I did a PR so that now you have server.address, because in the past you didn't have server.address.
Until all the trade view was broken.
on Weather 4, and also you don't have the database server name.
Database name, sorry.
**Shenoy Pratik Gurudatt** 26:38 Database name is the most important for, dependencies and stuff, if you want to get service dependent.
**Cyrille Le Clerc** 26:44 And so here, what I have to do is to directly do a contribution to the instrumentation library written in Go.
**Shenoy Pratik Gurudatt** 26:51 Hmm.
**Cyrille Le Clerc** 26:53 to fix it.
**Shenoy Pratik Gurudatt** 26:54 I see.
**Cyrille Le Clerc** 26:55 Because you can see in their code.
That, at best, they will capture server address on server port, if you call this helper function that we were not calling, but it's not, providing, database namespace, db.namespace, which is a database name. And so I am, at the moment, doing a pull request on this, project.
To, improve the… To improve.
**Shenoy Pratik Gurudatt** 27:28 database instrumentation cycle. Yeah.
**Cyrille Le Clerc** 27:30 instrumentation.
On the end, I've seen that we have some Python code that access the database.
on, the Python instrumentation library is so limited.
it's not capturing anything, it's a nightmare. But, yeah.
I don't know if I can do it. Golang, I can… do some improvement with Cloud Code, but Python, I've never done it all.
Yeah, is that.
**Shenoy Pratik Gurudatt** 27:55 That's.
**Cyrille Le Clerc** 27:56 I'm doing.
**Shenoy Pratik Gurudatt** 27:57 Let's.
**Cyrille Le Clerc** 27:57 You're interested in better database monitoring.
**Shenoy Pratik Gurudatt** 28:01 Yes.
**Cyrille Le Clerc** 28:02 At the moment.
**Shenoy Pratik Gurudatt** 28:02 I'm doing something with Redis and, Valky.
So, I'm just checking, I'll start checking out next week on what's there today with Valky. Is it similar to what you made improvements for Postgre and add some PRs there?
**Cyrille Le Clerc** 28:20 Oh, yeah, that's great, if you can also contribute and help, that's amazing.
**Shenoy Pratik Gurudatt** 28:24 Yes, yes, yes, yes.
Valky uses some, C-sharp libraries, to connect to, Valky thing. It's like card service talking to Valky database, and Valky has its own instrumentation, but we don't capture a lot here.
And there's a lot of Redis stuff as well from Legacy, so I need to see what all things can be improved.
**Cyrille Le Clerc** 28:52 Okay.
**Shenoy Pratik Gurudatt** 28:58 Are the PRs ready to review? I see they are up and running. I think the namespace thing needs upstream contribution, right?
**Cyrille Le Clerc** 29:06 Namespace needs upstream contribution.
**Shenoy Pratik Gurudatt** 29:09 Yeah, so that is fine. We can… I can also start looking at these.
Probably end of the week, I'll have something.
A lot of… I think Julian is also out for KubeCon, so…
**Cyrille Le Clerc** 29:23 is out for QConf.
**Shenoy Pratik Gurudatt** 29:24 Less hands on deck this week.
**Cyrille Le Clerc** 29:27 Yeah.
**Shenoy Pratik Gurudatt** 29:35 This is awesome.
**Cyrille Le Clerc** 29:37 Okay.
Thank you very much. Anything else?
**Shenoy Pratik Gurudatt** 29:46 I think I'm good.
**Cyrille Le Clerc** 29:53 Okay, so thank you, very much, for the progress on the agantic, observability, contribution.
Sorry, it's not moving that fast, but yeah, we do our best.
**FELIX GEORGE** 30:08 Thank you, thanks a lot for the feedback, and… Yeah, thanks, Fert.
**Shenoy Pratik Gurudatt** 30:15 Thanks, Juan. See you.
**FELIX GEORGE** 30:16 Bye.
**Cyrille Le Clerc** 30:17 Thank you.
**Shenoy Pratik Gurudatt** 30:17 Enjoy.
