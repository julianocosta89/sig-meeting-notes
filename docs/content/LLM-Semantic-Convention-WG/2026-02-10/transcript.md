SIG: LLM Semantic Convention WG
Date: 2026-02-10
Duration: 68 minutes
Zoom Recording URL: https://zoom.us/rec/share/H4KflhBiluBAvDKidtpr3PW0WukMredZ3QaiiiWPZwf6YogAfRcYK3HUmytZQaLr.1mJIN7iwr09TRP1B
============================================================

## Zoom Recording Transcript

neil yashinsky 00:02:16 Hello, everyone.
Good day.
Liudmila Molkova 00:02:38 Hello, hi everyone.
neil yashinsky 00:02:41 Hello, Lumia, how are you?
Josh Bonczkowski 00:02:43 Hello.
Liudmila Molkova 00:02:44 Fine, thank you.
neil yashinsky 00:02:46 Welcome.
Liudmila Molkova 00:02:50 Okay, let's get this started.
Give me a second.
Aaron Abbott 00:03:04 Hey, everyone.
Liudmila Molkova 00:03:07 Hi, Erin!
neil yashinsky 00:03:07 Fair enough.
Liudmila Molkova 00:03:10 Okay, so… I copied this over… yes, I did.
So let's… while people are joining, let's take a look at our board. There were a lot of things that has happened.
Okay, those are still in the pro… is it still in progress?
I think we've merged something?
We've merged the general definition, but…
Should we keep this one open for…
For the specific, built-in tools, like code interpreter.
Okay, I guess I… I'd like to close it, and if people…
anksing 00:04:15 Yeah, hey, hi, sorry, actually my Zoom froze for a moment. So, yeah, I think this one ideally, should be closed. There was another issue that was created for…
like, code interpreter or other tools, so I think we can, link that here, I can.
Liudmila Molkova 00:04:30 Do you know the number of the this year?
anksing 00:04:33 Let me find this here.
Thank you, Bill.
Anirudha Jadhav 00:04:59 Hi, Michael. Good morning.
Liudmila Molkova 00:05:02 Hi.
Anirudha Jadhav 00:05:03 Hi.
anksing 00:05:04 Yes, that's right. Thank you.
Liudmila Molkova 00:05:15 Okay, what else do we have here? New issues.
Talking level attributes and events.
So this are… doo-doo… A2e… this sounds like a good to-do.
Dylan, or Aaron, or anybody from Google's side, would… would you be able to share it with the A2A folks, or review it, and share your thoughts?
Aaron Abbott 00:06:00 Hey, yeah, I… I think I've already shared this with them,
I'm not sure it's something that they would look at right now, but I can reach out again.
One kind of complication is the A2A Python SDK already has some instrumentation.
But I don't think… They're super tied to it, so it is natively instrumented.
But this looks a bit more thought out, to be honest.
Yeah, I can share it with them.
Liudmila Molkova 00:06:28 Yeah, with a caveat, I don't think we're… We should use those names.
We should generally don't think anything here is A2A-specific, to be fair.
Aaron Abbott 00:06:44 Yeah.
Liudmila Molkova 00:06:48 Sure.
Aaron Abbott 00:06:49 I think… I mean, I think those are parts of the protocol specifically, right? Like.
Liudmila Molkova 00:06:55 Yeah, but, like…
Aaron Abbott 00:06:59 Yeah, yeah, not that one.
Liudmila Molkova 00:07:02 the task ID is the…
I think we call it Workflow ID, or we're about to add the workflow ID.
Or that this is…
the 08A protocol version, yeah, and this makes sense. We would just then take away the GenAA prefix, because that's what we…
do lately, and this is… this sounds like a very generalizable thing.
Anyway, so I think this is a… Good thing to…
Do you, in some shape or form.
And… let's take a look at the survey and try to quickly see…
Or maybe not quickly. Oh, we've been here. This is the server-side story.
Okay, I… Done.
General Evaluation Organization.
I think this needs somebody to take a closer look.
Ankit, since you added the evaluation, would you be…
Interested in taking a look at this and sharing your thoughts?
Anirudha Jadhav 00:08:30 Yeah. I'm also here to talk about it if you guys want afterwards, or just let me know whom I can work with on this.
This is Ani, I abroad this, and I've been working on this.
Liudmila Molkova 00:08:41 Yeah, yeah, feel free to add it to the agenda, yes. Just, we might not…
I think I added it to the wrong Word doc, but I'll add it again here.
Okay.
Anirudha Jadhav 00:08:55 But, Ankit, can you help me with this?
I'll reach out to you on Slack also.
anksing 00:09:02 Yeah, yeah, I can…
Anirudha Jadhav 00:09:05 Thanks.
Liudmila Molkova 00:09:09 And this one…
I think this is the duplication of the workflow span?
At least in… in the first…
The first die.
I think somebody needs to read through it and understand the implications.
Let me add a link to the workflow… PR, we have…
Aaron Abbott 00:10:06 Yeah, I feel a bit conflicted about this one.
This is, like, the most basic…
ask the agent if it needs to call a tool over and over again until it gives a response, kind of thing, right? It's like…
I feel like it's kind of implicitly obvious from looking at the The trace, like,
Even in this example, if you didn't have the main reactive step span there.
I don't think it changes the,
The ability to understand this trace.
Liudmila Molkova 00:10:38 Oh, I see. So this is just the wrapper for LLM plus tool, and under the invoke agent.
Aaron Abbott 00:10:49 Yeah, like, I don't know if this would be considered workflow, because it's not, like, a…
Liudmila Molkova 00:10:54 Yeah.
Aaron Abbott 00:10:55 The recipe is just like a… It's almost just like a… Event loop for the agent.
Liudmila Molkova 00:11:02 Yeah, I see.
Okay,
I'll probably comment on this later. My thoughts would be that this is… this should be opt-in, because it's very verbose and not helpful in many cases, but…
Anyway… Let's… Nope.
On, we are way over our triage time. This is… okay, so please add your name to the agenda.
And this is the time where we have some place for new members to…
Talk about themselves, what brings you here, what you want to achieve, get to introduce yourself.
Anirudha Jadhav 00:12:06 Hi, I can go first, if there's nobody here.
Liudmila Molkova 00:12:09 Yeah, go for it.
Anirudha Jadhav 00:12:10 Good. Hi, my name is Ani. My entire name is Anita Chadhaf. I work primarily at AWS, but my team is supporting open search project from the Linux Foundation. Our main goal has been observability, search, and tools around open search.
My purpose of this meeting and a lot of these… we've been in OTAL Demo and a few other meetings regularly, but purpose over here primarily is we are starting to create more agent observability tooling.
And, like, standardizing that in the open source stack.
And for some of the topics involved, we've been consuming telemetry from various sources, and particularly today or going forward, some of the focus is also on evals and experimentation.
Which I feel, talking to other developers, is a very fragmented field. Everybody uses a different eval system and different telemetry, and no standardization in comparison of benchmarks.
And also, that prevents tooling inside an IDE or inside a local dev environment. Like, for example, agent-to-agent traces or multi-agent traces are very difficult to debug, even if you have an agent or an LLM to explain it to you. Sometimes you just need to see things visually.
So, we're trying to create those toolings and standardizations where you can debug multi-agent toolings, and that's where these eval things are important to improve. So, that's a bit about me. As a role, I'm a senior engineering manager, but I do write code.
Yeah, thank you.
Liudmila Molkova 00:13:40 Thank you, Anne.
We have, also your topic on the agenda, so I think we will talk more, I'm curious. Does anybody else want to introduce themselves?
Okay.
Feel free to add anything to the agenda if you want to talk later.
Let's take a look on what we have so far.
Ding…
The JSON schema definition, it got one approval, it needs somebody else's. Dylan, I saw your comments.
Here…
Dylan Russell 00:14:29 Yeah. Paris.
Hmm… Yeah, so one suggestion was to add a name field to this… Function tool definition.
But I think I need to look at this again.
Because I was talking to Aaron, and I think… We…
want to think about how the function… the function definitions are being passed to, like, the Gemini API instead of, like, the…
SDK, which is what I was doing.
So, I'm gonna give this another review, but… I think…
Yeah, I think having a name probably makes sense.
Liudmila Molkova 00:15:24 So you're saying that…
We always have a name and description field. I'm trying to understand, there is a name and description
as well.
Dylan Russell 00:15:38 If you go into the models file.
And… yep.
Liudmila Molkova 00:15:55 This got big!
Dylan Russell 00:15:56 Wow.
Somewhere there's, like, a… yeah, there we go.
So should that have a name field, is what I'm… Asking, I guess.
Liudmila Molkova 00:16:11 Oh, I see.
Yeah. I, I see. Oh, generic tool definition.
It has a name.
Dylan Russell 00:16:21 Oh, okay, I didn't notice that. Okay, it subclasses it.
Liudmila Molkova 00:16:25 Yeah.
But it would be great to get perspective from GCP, please take a look. And I agree with your comment here, I think that we probably want just one opt-in flag.
I… if you think that there is something in this PR that does not allow instrumentations to do this, yeah, that's a great feedback.
Dylan Russell 00:16:51 Okay, cool.
Liudmila Molkova 00:16:54 Thanks.
Okay, and this one, I think it's just FYI. We have the approvals.
On this one.
And if somebody from Python could merge it, that would be wonderful.
I think we wouldn't have,
I… I don't think we… we can do this in this meeting. We didn't have the pack-friendly meeting yesterday, so maybe we will…
Take this offline.
And discuss next time.
Because it's both big, and it's difficult to discuss it without… context.
Okay.
Sorry, I don't want to butcher your name. Anuruda?
You've introduced yourself, but I missed it.
Anirudha Jadhav 00:18:11 You can call me Ani, I go by Ani generally.
Liudmila Molkova 00:18:14 Annie, okay, awesome.
Thank you.
Anirudha Jadhav 00:18:19 Go ahead, sorry.
You're saying something?
Liudmila Molkova 00:18:22 Yeah, so you mentioned that you work on OpenSearch Project, and you're interested in the Agentic scenarios. Are you interested from the, like, SRE agent side, using, telemetry for AI scenarios, or observability into AI?
Anirudha Jadhav 00:18:38 So, currently, we are creating tools for observability, so, like, agent traces, agent evals, and while helping SREs and ML operators and scientists to effectively improve and monitor their agent workflows.
Liudmila Molkova 00:18:58 Mmm, that's cool, yeah. So then you're in the right place.
Anirudha Jadhav 00:19:02 Yeah, today we support, like, log analytics, trace analytics, APM workflows in OpenSearch, Prometheus and Metrics in OpenSearch. Now, this would add a set of features that will help developers to, like, debug production logs, but before we debug production logs, I think the quality of agents is more important as before you start developing on a developer laptop.
And in that persona is where we feel the gaps, and that's where I'm coming from.
For this particular issue.
Liudmila Molkova 00:19:35 Awesome. So yes, for the… using telemetry to, assist people with SRE tasks, this is not the group. We don't discuss this here, but yeah.
Cool. So maybe you want to talk about…
neil yashinsky 00:19:52 I was just gonna say, Ludmila, like, that's one of the reasons I love coming here, is, like, it's like,
I'm trying to find the right analogy, but if you understand what's going on in this group, then it's a lot easier to kind of, like, plan for your observability strategies, because it's, like, the other side of this coin, maybe?
Like, if you want to observe agents, you gotta understand how they're working properly, I think.
Liudmila Molkova 00:20:17 Yeah, thanks.
Appreciate the feedback.
Tiny deal.
Anirudha Jadhav 00:20:24 the motivation a bit, and where we're going with this. Like, today, let me just close my door, sorry.
We don't want to ally somebody.
Okay, so, today.
While we have telemetry being sent from agents, and this telemetry is literally getting standardized into line chain, line graphs, strands, and many other agent frameworks, the telemetry is helping understand traces.
And traces are a good part of debugging things in production.
But they debug when errors happen, but the class of errors today are not similar to services and traces that we are used to in traditional observability, because the class of errors have very much to do with subjective nature of what is correct.
Historically, in services land, there is a static flow. Service A calls B calls C, checkout is a single flow, something breaks, it is true or false.
You know it is red or blue. Today, it is not the case with agents. It is so subjective that we are sampling traces for input, output, and evaluating them online, and the online evals don't have a way to match offline evals, and offline is where a developer is sitting on a laptop. And when a developer is sitting on a laptop, there are eval tools, which are, like.
so many in the industry, and everybody is good. Some things are evaling with an LLM judge, and there are many things… many people who do that, but there are some teams who go deeper into the RAG workflows or the vector engines to get to the next level deeper. The conventions we have kind of support all of them, but they're missing a few things.
And they're not standardized. Not everybody is using evals. Like, even looking at strands, I was going through their codebase, they had some parts of evals, but they removed it later, and they don't know why they removed it. So I think it's just missing that standardization and universal acceptance. But that part is far more important now, to start on a developer laptop as they're evaluating, and to continue the offline eval to online sampling evals to understand
and drift or quality, are these things running at the same quality? So that's, like, the primary motivation. Secondary motivation over here is while you're developing day one, day zero.
on your laptop. You start with single agent, and that's barely enough nowadays. You go very quickly into multi-agent. And multi-agents are, many a times multi-framework, not like one framework nowadays. So with these multi-framework evals, when you're testing things, just testing and debugging is difficult, because on your laptop, even you can't understand what's happening, even if you have all the agents in your environment. And the goal of this would be having the evals standardized in telemetry, where you can
Send it remote.
but also local, like a VS Code plugin, or anti-gravity, or Kiro plugin, where you can, like, visualize the trace. Like, visual part of traces is super important now, because they are so complicated, you can't understand it. You need to visually see it. So that's where this is going.
Liudmila Molkova 00:23:24 That's awesome. Yeah, go ahead.
neil yashinsky 00:23:26 Oh, no, go ahead, please, little meal.
Liudmila Molkova 00:23:28 I, I just, I, I think that there are a lot of common things, between what this group works on and what you bring. I was just,
maybe we can get to some specific proposals, because, like, it's… it's easy to talk about something in particular, and very hard to talk in general. Yeah, but thank you for the intro. Yes, Ankit?
anksing 00:23:51 So, I have one quick question, just to understand, like, the distinction, how is this, like, how would this be different from any experiment tracking platform that's available in the industry, like, be it MLflow, be it, Azure, like, in Foundry, or be it,
Anirudha Jadhav 00:24:09 Assuming they would all use these similar things, so the experiments also get standardized across platforms.
And you can run experiments with multi-agents. Currently, the problem is, you cannot run an experiment if you have two frameworks getting used. Like, if you have a Langraph agent, which is connecting to something else built in a crew agent, and calling something else in strands, you can call them in production. In production, everything will work, but you cannot evaluate anything.
Like, multi-agent evaluations become a big problem, and that is primarily because of standardization in between how people get the output of evaluations to be assessed.
Fair?
anksing 00:24:49 Okay, so I've been… Yeah,
Probably, but I think I might then go into more details on, like, what's the gaps in the local development that prevents anybody to kind of get those details, which you could do it in production, right? Because then, I think that's.
Anirudha Jadhav 00:25:05 Sorry, my headphones just switched. Can you repeat the last part, please?
anksing 00:25:08 Yeah, so I think, then, I would like to dip more into details on,
But other gaps when you're working locally, which prevents you from getting all those details you need for evaluation versus when you're in.
Anirudha Jadhav 00:25:19 Yes. So, locally, what happens is… yeah, yeah, I totally agree. So, locally, what happens is, if you have this agent environment locally, you could kind of debug with logs of all of these things, or traces of all of these things, but you cannot evaluate.
Because if you have a multi-agent framework, the evaluation frameworks that they use are very different. So there is no, like.
end-to-end evaluation that you can do between them. All the evaluations get stuck at single agent, or you have to force your entire organization, like, use only one framework, and that barely happens.
Plus.
If you have this thing even with today's traces, today's traces don't let you connect the traces to the evals.
with multiple runs, because ideally, one run is not going to give you the correct answer to help you make a decision. You need to run multiple runs and multiple inputs, and aggregate and get an aggregate view of correctness, because these are not binary decisions. So the aggregate view is more important for post-analytics, even in a local environment.
So in the local environment, the forcing function today is send your telemeter remote.
I mean, it doesn't need to be your ID, you can have all the telemetry and visualize it right there, and help developers locally.
anksing 00:26:28 Sorry, I think I see a number of under 12, on the profile.
Anirudha Jadhav 00:26:31 Go for it.
Liudmila Molkova 00:26:37 Yeah, I think so.
Anirudha Jadhav 00:26:38 Do you want to go ahead? Yeah.
Sergey Sergeev 00:26:41 Go ahead, Lynn.
Liudmila Molkova 00:26:43 No, I was just trying to be more conscious of time and bring us back to the Earth, but make your final point, Sergey.
Sergey Sergeev 00:26:51 No, my question would be, so, first of all, when you run some experiments or test dataset, you need to put it… to indicate it somehow on telemetry, or you need to set some attribute which should be propagated and set on
the spans with OMs, which are being evaluated. I think we will need to connect… I think I have an idea, basically. You need to specify which attributes you need to stamp on every span, and then when you evaluate which attributes needs to be inherited.
Anirudha Jadhav 00:27:26 From the WEAT.
Sergey Sergeev 00:27:27 Yeah.
Anirudha Jadhav 00:27:28 Yes, I agree. So, in my proposal, I put a sample proposal in draft.
Where, I put the attributes that I would care about. I would definitely like more feedback in which more we can add. I added a sample instrument, sample PR with strands, where I could, like, test it out. So it becomes easy, like, just write Python code, everything just works, and then when you see the output, run a sample OTL collector, and you will see everything as a test case which you can get aggregated view over.
Sergey Sergeev 00:27:54 Yeah, let's start a thread in Swag on it, because I think I have an idea about it. Sorry for…
Anirudha Jadhav 00:28:01 Oh, I didn't even get you ready?
Sergey Sergeev 00:28:03 Maybe we need to move… move…
Anirudha Jadhav 00:28:05 Lord.
Sergey Sergeev 00:28:05 The different topics.
Anirudha Jadhav 00:28:07 But just tell me where to start the thread, I'll work with you accordingly. Just write it on the document or Slack me.
Sergey Sergeev 00:28:12 Sounds good.
Liudmila Molkova 00:28:14 By the way, we have another track for the agent observability on Monday.
Sergey Sergeev 00:28:21 Got it on Monday, too.
Liudmila Molkova 00:28:22 Oh, awesome. Yeah, that's crazy.
Anirudha Jadhav 00:28:26 Yes.
Liudmila Molkova 00:28:27 Yeah, I… my main feedback would be that,
I think you already got it. We tried.
Anirudha Jadhav 00:28:34 I didn't connect your name when I started talking to you, now I connect your name. Yes, I saw your feedback, addressed it, and I changed everything to focus on tests.
Well, namespace.
Liudmila Molkova 00:28:45 Yeah, and I would be curious, I think it's related to Ankit's question, like, the… the experimentation. We have conventions for feature flags, and they…
could be somewhat adopted by the, I think, Azure experimentation platform. Yeah.
Anirudha Jadhav 00:29:04 I think the experiments are a misnomer, almost, in this case, particularly. The reason I say that is, experiments is like a grouping term for tests
which is equal to test suits. So I'm mapping experiments to a test suit right now, and not going in the experiment route with flags. I think the test itself is enough.
Liudmila Molkova 00:29:24 Okay, awesome, thank you.
Anirudha Jadhav 00:29:25 using the run ID to correlate between those things and not keeping anything extra, so it's a very lightweight proposal, that way.
Liudmila Molkova 00:29:32 Okay, nice. Thanks. So, Dan, it's…
Probably not, like, here at least, we wouldn't know if instrumentation runs locally or remotely, doesn't matter, right?
Anirudha Jadhav 00:29:45 Doesn't matter, yes.
Liudmila Molkova 00:29:46 And then we would design this approach from the perspective of how to model telemetry more than.
Anirudha Jadhav 00:29:53 Yes. Where it runs.
Liudmila Molkova 00:29:55 It's a very… it's a very big proposal, and we, we, like, just historically, we cannot observe it in… in one go.
Anirudha Jadhav 00:30:03 I can break it down into smaller proposals, if that's okay, because there are only 3 small pieces. So, if that helps, I can break it down into 3 small proposals.
Liudmila Molkova 00:30:12 Yes, that, that would be great, and maybe we can go one by one, so that we don't, like, yeah, you don't do a lot of work in advance.
Anirudha Jadhav 00:30:22 Makes sense. So I'll start breaking this down, I'll keep the parent one, and the parent one will have no implementation, and the child ones will just link into it.
Makes sense, thank you.
Liudmila Molkova 00:30:32 Thank you. Sergey, you still have your hand raised? Do you wanna, or…
Okay.
Thank you.
I wanted to continue the roadmap exercise we started, last time. Just be…
Trying to be cautious of time.
Let's spend maybe 10 minutes on it, so we have 20 minutes for the rest.
So, I've put things we talked about last time into the Excel. It's the features or the big work items that we
Wanted, that we discussed.
A couple of weeks ago.
Before we start the exercise, do… Do folks want to bring… Other things into this list.
I think what we hear as well is there are a lot of improvements around evaluations.
Aaron Abbott 00:31:52 Let me just, maybe clarify the time scope for this, like, if you're looking at 6 months, full 2026.
Liudmila Molkova 00:32:00 full 2026, I mean, to the next KubeCon.
Aaron Abbott 00:32:03 Okay.
Liudmila Molkova 00:32:05 End of November, because after that, no work is happening.
Pretty much. Well, a lot of work is happening, but nothing gets merged.
I… I don't think the… the… the timeline, like, the, the.
Order would be more important for me than anything else.
It's more of what we are focusing on.
And to just share my thinking, I would consider it as a contract between, within this group, that we collectively decide what we work on, and we deprioritize everything else.
So, because, otherwise we… we can spend every meeting talking about this big and new proposals, but nothing will get merged.
neil yashinsky 00:32:56 I agree. It's better to control.
Anirudha Jadhav 00:32:58 That makes sense.
neil yashinsky 00:32:59 Oh, sorry, go ahead.
Anirudha Jadhav 00:33:01 Sorry, go ahead, I'm just agreeing, yeah.
neil yashinsky 00:33:02 Yeah, yeah, I'd see him.
Liudmila Molkova 00:33:06 Sorry, I just busted something in the chat, I didn't mean to.
Okay, so then, I'm going to send the link here. You have a budget of $100.
You can distribute them however you want.
You can give 100 to one item, you can give, you can sub-spread them equally.
Play, maybe we'll do this. Add your name here.
And add your points.
Here, and we will do the stack ranking. Yeah, Josh?
Josh Winerman 00:33:45 I might have, missed it. I was just wondering, you had brought this up, Lee and Milo, a while ago when we were talking about the roadmap initially, but is, and this is more of a Python thing, too, but is getting…
everything under utils.
Consolidated under one of these.
instrumentations to use, or is that applicable here, even?
Liudmila Molkova 00:34:08 I think the high-quality instrumentations are not possible without UTIOs.
But if you feel it deserves a separate point.
Josh Winerman 00:34:18 No, I think that's… I think that's valid, I was just clarifying.
Liudmila Molkova 00:34:25 Somebody's saying, oh, I'm sorry?
This was not intended, everybody should have access now.
neil yashinsky 00:34:32 Minor details.
Liudmila Molkova 00:34:34 No, major bug.
Cool.
So I'm going to…
turn off screen sharing so we don't… we don't get distracted. And let's… let's spend, I don't know, 5 minutes on this.
neil yashinsky 00:37:13 Did you want to start inserting, maybe a tally, column or something? I bet we could start getting, you know, good consensus on what's already been voted on.
Or are you waiting for me?
Liudmila Molkova 00:37:28 Do you wanna go for it?
neil yashinsky 00:37:30 Sure, yeah, yeah.
Liudmila Molkova 00:37:30 volunteered.
neil yashinsky 00:37:31 Yeah, yeah, I'm big into voting for, believe it or not,
Well, but now I gotta figure out which way to do it. Okay, so I think we could just, like, sum these and average them, yeah.
Liudmila Molkova 00:37:49 And just some would be fine, right?
neil yashinsky 00:37:51 Yeah… wh- well, oh, yeah, that's true.
Liudmila Molkova 00:38:48 Okay, so we're pretty much done.
Let's give it another minute…
Okay, everyone is at 100.
Oh, Keith!
And Kit, are you at 100? Yes, you are.
Somebody left something here. Did you intend to?
Well… Who is modifying the R column? Do you want to modify it?
shuwpan 00:39:39 Yeah, what can I eat, what can I eat.
Liudmila Molkova 00:39:41 Yeah, awesome.
neil yashinsky 00:39:45 Yeah, there's the one school of thought that says, don't show any voting results until all the voting is done, because then you'll, you know, people will just, like, vote for what's popular, and then there's, like, just, you know… because, like, obviously, high-quality instrumentation in Python, clear winner, what do they even call that?
Majority, clear majority, beyond plurality.
And a surprising, strong showing for better evaluation conventions, in my opinion.
Josh Bonczkowski 00:40:18 Honestly, that doesn't surprise me. As many times as I talk to customers about evaluations, that's the number one topic.
neil yashinsky 00:40:25 Yeah, like, I think it's really important, but I was like, but yeah.
Well, look, my vote showed me a liar, though, look at that, I only gave him 5. So, you know, take…
Results may vary.
Liudmila Molkova 00:40:40 Okay.
Interesting. So,
This is also on the fence, and these two… what are those? Those are workflows, orchestration, and server-side observability.
Why?
Let's try to sort them…
Pavan 00:41:08 Oh, one question, sorry, to jump in.
So, in the, area which, says workflow slash orchestration, is that supposed to also cover multi-agent
You know, systems in general.
Like, trying to define, like, conventions for these new types of emergent Systems.
Is that clubbed into that? Or…
Liudmila Molkova 00:41:42 I, I, I, I think so?
But it's a… it's a good question.
At least I think you cannot define multi-agents without this one.
Pavan 00:42:01 If, if I can just update the name of that feature, or if there is a preference to create a new one or something.
I mean, I think the dividing…
Liudmila Molkova 00:42:18 As happened, right? The workflow orchestration.
This is the feature we… are already… working on, and…
In my mind, it would take higher priority than
Any new feature, if it's not part of the workflow orchestration.
Jake, what would be the proposal?
Sure.
Pavan 00:42:50 Okay, okay, I think, I think that's fine.
Liudmila Molkova 00:42:56 Okay.
So, we have, 5 liters.
That are way… Think higher than everything else.
How do you folks feel about it?
Committing to those.
And considering things that are… not…
one of this as a… something that we probably won't get to in 2026. Maybe we'll get to some small things if somebody contributes a trivial
Tools?
We probably would take it, but, we would try to spend our time on this 5.
Things.
neil yashinsky 00:43:52 Makes sense to me.
Liudmila Molkova 00:43:57 And then, it sounds like…
We should spend maybe twice more time on Python than anything else.
neil yashinsky 00:44:07 I guess so.
By the will of the people.
Aaron Abbott 00:44:12 Yeah, I think… I think,
The key, kind of, issue there is…
someone still has to, like, review and maintain the PR, so…
you know, I think I might be… myself and Dylan might be the only…
we've got Keith here from Python, but, like,
I feel like maybe that's not scaling super well, so we can look into ways to improve that, but we should also discuss that in the Python segment, right?
neil yashinsky 00:44:40 And Aaron, you know, I still very much consider myself barely, intern-level, you know.
status, or what have you is not the right word, but, intro… intro… intern-level insights. But, you know, I'd be happy to, like, what do you call that, apprentice with you guys to… or you folks to, you know, begin to be able to help a little bit more on that front?
As I get micey legs under me, so to speak.
Aaron Abbott 00:45:05 Yeah, yeah, sure. I think… I think part of the issue is there's, like, an activation energy to kind of
maybe rework some of the tooling, like, in particular, I think
you have to be a Python approver to get the green check.
neil yashinsky 00:45:19 Amendment.
Aaron Abbott 00:45:20 We're kind of manually merging stuff.
I don't know if this is a big priority for Ricardo, which basically means that I'm…
I'm the person clicking the merge button on all the PRs, in addition to whatever else I'm doing, so…
I don't know, I can… I can discuss that with, you know, the Python sig, or…
I don't know, Woodmill or GC Liaison or something like that.
I feel like it's just a tooling issue to a big extent, but I don't want everybody to be blocked on this, but I hear that it's super, super important, and I agree.
neil yashinsky 00:45:54 Yeah, yeah, I meant not necessarily as an approver, if you will, but just, like, other things I can help with to help relieve your burden, or what have you.
Aaron Abbott 00:46:01 Yeah.
Anirudha Jadhav 00:46:02 I wouldn't be able to commit now, but I'll definitely help out and put a plan in place, because I think regardless of what we implement, if the Python instrumentation is not in place, nothing else works.
I'll start charter reviewing, but I'll make sure we have more capacity on that. I'll try to reach out with a few folks who can regularly work on this.
Surya Teja 00:46:26 So, I can also help over there, on the Python side. I'm not a great Python, I haven't been writing for a long time, but…
You want help, I can help over there.
Liudmila Molkova 00:46:41 Yeah, so… it… No, go ahead.
Aaron Abbott 00:46:44 Please, please, you've been waiting.
Liudmila Molkova 00:46:46 No worries.
There are a lot of people who are interested in reviewing PRs. We are mentioning the Python PRs.
Here.
the… A few of them in the dark.
Let's go for it.
review them.
And I think this would take some burden away from maintainers and other approvers, because you would provide, like, the first
line of defense. Yeah, go ahead, Aaron.
Aaron Abbott 00:47:18 No, please finish your thought.
Liudmila Molkova 00:47:21 yeah, the… the process-wide thing would be…
Interesting. Sergey mentioned there are code owners. The code owners
Can only review, they don't necessarily have a green checkmark.
And they are not super responsive, that's what we see.
Aaron Abbott 00:47:44 Agreed, plus one to all that.
I think the other, kind of, Issue is…
it's a very manual process, reviewing semantic invention PRs, and I think one of the other line items in here, Lyudmila, was about tooling.
So I don't… I don't know if these are, like, a… You know?
Completely orthogonal topics in that sense, because it would make my life massively easier as an approver slash maintainer if there was a test
in the PR that said, you know, had a green status that said everything passes semantic conventions or complies with them, so…
Yeah, to a big extent, I think it's tooling, it's not just, you know, like, this Python code is sound. Somebody has to really know the conventions, and
Yep.
Liudmila Molkova 00:48:31 Yeah, could you add an agenda item for the next week to talk through this more?
Yeah, maybe… I want to join the Python Seague on Thursday. We can talk about it there, but I, like, I don't expect that the group would have a solution that… that… I think Python group would expect us to come up with a
Solution that scales, right, Aaron?
Aaron Abbott 00:48:57 Yeah, yeah, and I know you've been working on this, Lyudmila.
neil yashinsky 00:49:00 I just meant, like, talking through some of the details you just mentioned, Lumila, about, like, the, I looked away for a moment, didn't see where you were saying, like, people… some things that are available right now for people to jump in and help with.
To help relieve the burden of the… some of the other folks.
Liudmila Molkova 00:49:17 Yeah, and speaking of automation, yeah, I think this… this was the thing I selfishly added, because I really wanted.
and… maybe we should just collapse it with Python, I…
I would like to take it as my, at least, personal project, specific to Genia or not, and figure this out.
Anirudha Jadhav 00:49:43 Can I ask a question?
Liudmila Molkova 00:49:45 Yeah.
Anirudha Jadhav 00:49:45 Oh, sorry, Josh, okay, you have a chain thumbs up, okay, how is the…
sort of agentic tooling support, or compliance, or can we add that support on the hotel repos? A lot of the things that we do is we pass first-pass tooling generally by AI right now.
Which does have good sharing files and good things that give you guidance.
they don't commit, but the guidance is super helpful to validate larger repos and work with larger repos, which feed into our PR systems. And I'm not sure how much and how we can add it, but I can easily add a GitHub action to make sure some AI can automatically validate basic things, basic code checks.
And also compliance, and see if any conventions are broken or not.
But that initial pass does help a lot in reviews.
Like, even going forward for the last couple of months.
I'm speaking to our teams and my teams. I think we've been writing more code with AI, and having AI review the first pass, because the reviews become a bottleneck. And then after the first pass or second pass by AI, we do manage to have steering files, but different AI systems review it, so it is a bit different. But the final check is still the reviewer, but it helps the reviewer so much.
Nope.
So if there are GitHub actions or some controls, we can definitely add these things in the workflows of a repost solution.
Liudmila Molkova 00:51:10 I think we… we use Copilot a lot to review. You can… if you have subscription to
Copilot, or maybe quote, you can ask, you can request a pilot to review.
We don't have skills or agent instructions across the repos, and it would probably be something that, Python folks would need to agree and review. It should be aware of the
a lot of.
Anirudha Jadhav 00:51:40 Yeah.
Liudmila Molkova 00:51:41 But the compliance with semantic conventions, we can do it deterministically.
Anirudha Jadhav 00:51:46 Okay.
I'll propose something, and it'll need more conversation. I'll propose something. And it'll be better if you just add it on the repo as GitHub Actions, which will need some external model keys over there. I'm happy to add some keys over there, but I need to make sure if it's okay with everybody first. So I'll propose something, and we can go.
Aaron Abbott 00:52:06 Well, yeah, I think that was the thing I was gonna ask. I can check, you know, with GC and whatnot, but I think this has to kind of be in the open telemetry, you know.
Like, we probably have keys, or we have some subscription through CNCF, I don't know.
Anirudha Jadhav 00:52:19 So, I've been working with LF on a similar thing, so I know the process with LF. CNCF should be similar, so let me propose it and we can talk through it.
Aaron Abbott 00:52:28 Okay, sounds good.
Liudmila Molkova 00:52:30 I can see Trask is on the call. Do you think it's a project-wide, or the.
Trask Stalnaker 00:52:36 Yeah, so we did, recently get
GitHub licenses through CNCF, through GitHub, and they just… GitHub rolled out a feature recently where now
Even if you don't… even if PR authors don't have Copilot license, they should be able to request, Copilot reviews.
And we've enabled that on one repo in OpenTelemetry. We've enabled auto, reviewing of PRs on one of the OpenTelemetry repos, and we can definitely set that up. Some people don't want it, some people do.
But I…
Liudmila Molkova 00:53:23 Thank you.
Trask Stalnaker 00:53:24 I think the big deal is that it shouldn't be limited to
PR authors who have Copilot licenses already anymore.
Anirudha Jadhav 00:53:34 Yeah, yeah.
If that works, that's awesome then.
Aaron Abbott 00:53:39 Okay, let's discuss it at Python Sig 2. I don't know if you can make any, but I want to check with other maintainers also.
Anirudha Jadhav 00:53:45 Makes sense.
Liudmila Molkova 00:53:48 Oh, we have…
Trask Stalnaker 00:53:48 me up on Slack, I can help you set up anything.
Or verify any of that.
Aaron Abbott 00:53:55 Yeah, thank you, Trask.
Liudmila Molkova 00:53:59 Thank you. We have 10 minutes left. I think we had a good discussion. I think we should continue, this discussion on…
Next time… Road map.
I'll probably try to prepare
either an issue, or I'll update our…
Triage board to align with the… Priorities.
Okay, there are a bunch of pull requests to review, and people who volunteered, please go ahead.
We talked about… This one… The workflow.
We have a couple of…
Great checkmark approvals, that's great.
I am withholding my approval because I think it's important to resolve the ADK question.
Other than that, I don't have any concerns.
Ridhima Satam 00:55:27 Yes, so I have replied there with, yeah, workflow agents for ADK. They have the sequential agent…
Parallel and loop agents, so there we can directly map the workflow.
Aaron, if you want to talk about it, like, offline or long, it's fine.
Other than that, the other way, to put a workflow, or start a workflow.
in case we don't have these agents, not just for talking about ADK, but otherwise also, would be, like, would it be a great idea to,
explicitly invoke a workflow, like having an API from the application to invoke a workflow to start and end the workflow. So that could be also one thing we can do. The other approach also could be
say, we observed in the OpenAI agents that you start a trace in…
And then you… in that trace, you have a bunch of…
and it's in the documentation for the OpenAI agents that if you want to club the agents, you can start a trace, and that we can term it as a workflow. If, in case, we don't have that trace, we can also think about
when a span is starting for that particular framework OpenAI agent, and if it doesn't have a root, we can also start a workflow there. So those are other couple of ideas, not just restricting to ADK, but in general, yeah, just wanted to put there.
Liudmila Molkova 00:57:16 Cool, so then let's… let's take it offline. Let's see, where we end up with?
Another small PR.
I think it's pretty useful. We have the approvals, but, Dylan, you also brought it up as a separate
item.
Right.
Dylan Russell 00:57:42 I had a separate question about cached tokens.
Which is just… If other models have this kind of cash token thing.
Liudmila Molkova 00:57:55 Yes, and somebody just added another… attribute forward.
I think we probably should rework this, but, but,
Sorry.
Yeah, the creation and read.
We might need to rework the whole concept of how we track those also for metrics, but the first step is there.
Dylan Russell 00:58:39 Number of input tokens served from a provider-managed cache. Okay.
Yeah, that sounds exactly like what I want.
provider-managed, meaning, like, Google or…
Liudmila Molkova 00:58:53 Yeah, yeah, like, so the… when you get the response, you get the breakdown of…
How your input tokens were distributed, and…
This is the server side.
caching.
Dylan Russell 00:59:07 Okay, cool.
Nice.
Liudmila Molkova 00:59:11 Yeah.
This is a similar one, but for reasoning, right?
And I think the… in the case of, GCP, they're called thinking.
I personally… I don't remember how many of other models have reasoning
I don't have a preference on… of which one to use, so if you think we should consider thinking
Bring it up.
Dylan Russell 00:59:43 Yeah, I think either one is fine, I don't know.
Like… Yeah, I guess their… different models will have different… Terminology.
Liudmila Molkova 00:59:57 Yeah, I think what would be important, and it's not about this PR, but it would be great to have Google a specific page where we talk about this terminology differences and say, oh, okay, reasoning tokens are actually thinking tokens.
Dylan Russell 01:00:14 I see.
Yeah, that makes sense.
Liudmila Molkova 01:00:21 Yeah, another thing I wanted to bring your attention to is we've been discussing it for a bit, and I think this is a good thing to
Add is the metrics for time to first chunk and time per output chunk.
It should work for any, provider.
And, it's a trivial PR, that would be… Interesting to add.
Makes sense.
Yeah, we have one minute left. Those are all the Python
PRs that want your approvals, and there were a lot of
interest. So go ahead, review them, please.
Anirudha Jadhav 01:01:10 Yes.
Liudmila Molkova 01:01:12 Yeah, Ankit?
anksing 01:01:13 So, I actually just wanted to mention the PR I have, so I'll add responsive operation value, so this one is not a Python care, it's a…
Just a schematic originally.
Liudmila Molkova 01:01:24 Okay.
Surya Teja 01:01:25 So, the last 3 PRs are from me. So, the first one deals with adding…
First… first one deals with instrumentation for OpenAI Response's API, so I broke it up into two parts. One… the first part is adding for sync.
Once this is merged, I'll work on adding the async one.
I saw we were missing few attributes over here. I wrote them down in the PR description.
And also, I observed that,
these are not instrumented in chat or embeddings. So, wanted to clarify if I should instrument these or not, and the second thing that I had a doubt was
I added a retrieval operation. There is a retrieve functionality that's in the API, so I added instrumentation around it. Is it right or wrong, is the next question.
So, I'll pause here.
If someone can take a look at it and, you know, clarify these things, it will be helpful for me to instrument stuff.
Liudmila Molkova 01:02:38 Do you use GenAI tools in this PR?
Surya Teja 01:02:44 Yeah.
Liudmila Molkova 01:02:46 Okay.
This is the most important one.
And I'll take a look. I cannot comment right now, and we are out of time. I'm sorry, it ran longer.
Surya Teja 01:02:59 Yeah, sure. Also, wanted to bring your attention to Anthropic's sync instrumentation, because I was not using the correct conventions, and I was…
Using the wrong one. You come and… you gave me a link, right? I changed that, if you remember. So, if you could take one more look at it, and say if the instrumentation conventions are looking good.
That will help, solve things on…
what do you call it? In the async one also. Async one also has been transformed.
Liudmila Molkova 01:03:32 Okay, I'll, I'll do my best, sorry, the OpenAI Sync?
Surya Teja 01:03:40 Yeah, I'll reach out to you via chat with all the questions that I have. You can feel free to respond to me whenever you get time, it's not super urgent.
Liudmila Molkova 01:03:49 Oh, okay, yeah, thank you.
Cool, sorry for running late. See you all around. Let's chat more on the patency. Thanks.
neil yashinsky 01:03:58 Thanks, Julio. Thanks, everyone.
Dylan Russell 01:04:00 Cheers.
