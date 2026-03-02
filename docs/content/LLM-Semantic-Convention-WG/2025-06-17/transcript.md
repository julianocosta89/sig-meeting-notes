SIG: LLM Semantic Convention WG
Date: 2025-06-17
Duration: 65 minutes
Zoom Recording URL: https://zoom.us/rec/share/gSh6F9z9ffZQ64LaPiC4AZ6qZUS42l-aZMK1i925AFgaUJGFuKFpXvUWl2XyEz_P.jc_Oy8qiKH2DO6Po
============================================================

## Zoom Recording Transcript

Aaron Abbott 00:02:22 Hi, everyone.
Alright.
I think Windmill is going to be a bit late, so probably get started without her. But
if folks could please add your items to the agenda and
add your name to the attendees list. Please.
shiprajain 00:04:13 Could you please share the link to the agenda, Doc?
Aaron Abbott 00:04:17 Oh, yeah, yeah, sure, it's in the calendar. Invite. By the way,
shiprajain 00:04:22 Okay.
Aaron Abbott 00:04:24 I'll share it. Here.
Alright. Let's take a quick look at the Project board. I don't think there's anything new. But
oh, we do. Okay
through.
Yeah. I don't think Drew is gonna be on this call. Does anybody know anything about this? One?
Seems pretty straightforward, like a single dimension with account?
All the metrics.
Okay?
Oh, yeah, there's a Pr, so if somebody, let's take a look
cool.
Looks like we've already got some reviews. So I'm gonna move this one in progress.
It's gonna be
okay. And we have one more.
Does anyone have any context on this?
Looks like pretty much just a kind of Union field for specifying the agent pattern seems pretty reasonable.
there's no Pr. Or anything yet, so let's just leave it in this column, for now.
does anybody want to give any update on things they're working on?
I I reviewed some of Lumilla's Pr, so I think this which one was it
the one with the we were discussing protocol, this one no, not that one.
We were discussing. I think it was Gen. AI dot system
renaming it. And there's some other stuff in there
still waiting for some some feedback from label, I think, on my review comments. But
yeah, and that's all we have for the Project board.
Okay, Sergey, you run. You want to start with your agenda item.
Don't see Sergey.
Alright. I guess we'll come back to this one also, folks. If you can add, I think we usually try to do a
time box, or like a time estimate for each agenda item. So.
Sujay Solomon (Google) 00:07:57 It looks like Sergey just joined.
Aaron Abbott 00:08:00 Oh, okay, perfect.
It's okay. You there.
hey? We're at your agenda item. If you wanted to kick it off.
Sergey Sergeev 00:08:13 Yeah, sorry folks. I go through it a little bit.
So yeah, the problem that we have. And I think everybody starts to hit.
It's around the industry. So we have 2 standards, basically, right now, one.
basically telemetry, we just spend only
which which is coming from Jsoup openly and so on. And basically metrics, events and spans.
So this telemetry I think both
ways will be required by different vendors.
And I was thinking that we probably need some common instrumentation SDK,
which can basically switch the stelemetry under the hood.
So basically, if you prefer to use span only telemetry and put everything on span attributes.
You can do it where it can do by default. But if you want
to switch to spam metrics and events telemetry, probably we set some environment variable, and
that common instrumentation, SDK, can do this thing, Candace Hood.
So this is where it came from. The idea. Second, so let's brainstorm about this problem?
Do we agree as communities that there is this problem.
Aaron Abbott 00:09:58 Yeah, I mean, I'd like to hear more. I've definitely heard the span versus log event thing a lot. I'd like to hear more about the metrics. One.
Sergey Sergeev 00:10:06 Yeah, metics, duration. And basically token, usage is very helpful
for Lm, and vacation for tool usage and so on.
I think it's a useful metric, and
I think, especially for the server side. Be.
Need that metric to be standardized, but for instrumentation to it's very helpful to derive those metrics on instrumentation side.
Aaron Abbott 00:10:41 Great, so are there vendors that only derive them from spins in the back end and don't have any like. They don't accept metrics kind of thing.
Sergey Sergeev 00:10:50 I think a lot of telemetry just emits spans. Correct me if I'm wrong, because that's
maybe open late doing it. Maybe I work.
Aaron Abbott 00:11:02 Okay.
Sergey Sergeev 00:11:07 Yeah, I'll double check and add some details, maybe inside channel, or after the call.
Aaron Abbott 00:11:15 Okay, yeah, I mean, I think
there's kind of this impedance, Mis mismatch, between hotel like
we we recommend, you know, span logs, events and have have them kind of separated, first, st
sticking everything in spans like.
In particular. We talked a lot about how spans are designed to be sampled versus logs and metrics. And then obviously, metrics have different
kind of slos in terms of their pre aggregated and how much memory they're gonna consume.
or what happens if your buffer overflows and stuff like that? So
yeah, I think I think we should definitely talk about that more. You know.
if anybody wants to speak to the span only point of view.
Sujay Solomon (Google) 00:11:59 Aaron, maybe just to sort of
level set on where we are. Can you describe what the the current status is like? If you use instrumentation today
for Gen. AI. Specific things like following our conventions. What does it emit? And then, with Ludmilla's like recent Pr, which I don't know, if that got merged in or not yet like, what does that change it to? And how does that differ from what Sergey is proposing here?
Aaron Abbott 00:12:32 I think Sergey is mostly talking about non hotel semantic convention
Sujay Solomon (Google) 00:12:38 Instrumentation. So like open lit, sorry, Sergey.
Sergey Sergeev 00:12:42 Yeah, there is this problem. So in the perfect ideal world, we have manual instrumentation. Wi-fi is an open telemetry project which.
strictly for semantic convention and amid spinematics and events,
to follow semantic convention. But in the real world I think it's mostly spans and sometimes metrics.
and I think building that common instrumentation Library or SDK somewhere in Python country may help a lot. So basically, you separate instrumentation from the telemetry. It emits. So I think we will have to support both, especially for trace, whoop.
donation, and migration.
So, and there are a lot of frameworks like rank chain or
light alarm, which emit also open telemetry.
It will be helpful to use this common library
to basically to standardize on telemetry
whatever flavor you want, you can tweak it
with some environment variable. But at least you don't have to make a lot of changes
in different ways, and so on.
Aaron Abbott 00:14:12 Yeah, yeah, I think it is a bit more complicated with this Pr from Lugnola.
because we are. We are giving a path for both spends and events.
at least for the completion details. But
yeah, like we, let's talk about it. I mean, I think.
Sergey Sergeev 00:14:29 Yep.
Aaron Abbott 00:14:31 Having some like. We discussed a lot about having these callbacks. So like we, we would have some kind of language like instrumentation, should accept a call back with the signature they should call it at this point.
We have some kind of like injection mechanism, or or we do it kind of reverse where there's a global
saying like, Get get instrumentation callbacks.
So we have something kind of standardized in maybe the contribut repo that all these other folks can use, and then it respects either an environment variable or they they just set the different callbacks. So.
Sergey Sergeev 00:15:04 Yeah. And so just one more thing. So we just, I, I propose we build this library. And if you switch back is it. Let me share.
Yeah. So basically in that. SDK, we can define some gen, a types like Om tools, task workflow agent retrieval embedded.
And basically those types can be separate from telemetry timids. So your instrumentation library can basically create that instrumentation type or gen AI type
and internalizes. SDK, will convert it to the needed telemetry. So we separate from setting all the attributes and everything else on
direct, directly on open telemetry SDK.
And instead using the steps so it will help award also
to do evaluations, which is next item.
But first, st what do you think about types, generic types.
Aaron Abbott 00:16:20 Oh, I mean, I think types is great. Like, right? Now, yeah, yeah, go ahead.
Sergey Sergeev 00:16:27 Yeah, we can reflect semantic conventions directly in those types which will be really helpful.
Aaron Abbott 00:16:37 Yeah. So we have, like, for most most semantic conventions, we kind of take the schema 1st approach where, like people would write the yaml, and then we would generate the types.
I think, in in that Pr. I was sharing from the bill.
I think she used these pydantic models to generate the Json schema.
So I I don't see any reason we shouldn't use these in the util. Besides,
if maybe we could get away with like plain data classes just to
keep the dependencies low, although these are nice because they have obviously validation.
But yeah, I think that would be a good 1st step.
Samuel Colvin (Pydantic) 00:17:16 You don't want pydantic models. You could use data classes and then just use a type adapter to generate the Json schema at the end.
So at least the majority of the code is vanilla python.
Even use triple quoted strings underneath the fields to add the description in the Doc, in the data classes. I think.
Sergey Sergeev 00:17:37 Yeah, the difference which I which I think we want to achieve. We want to create that Gen. A type
without tying it to strictly to telemetry it emits.
So
I was thinking about something like a python object where you define all the required optional parameters. But the instrumentation SDK,
can create different telemetry based on that parameter. Do you want to emit image separately, or you want to put it on a span?
So
Aaron Abbott 00:18:22 Yeah, I think that would be great. And may maybe like
kind of a design for
what? What the interface looks like. What kind of call like? Is there a callback signature that we have? Everybody do, I know with Mill already is a prototype of that
And then I think the other kind of question was.
yeah, like, we, I think we were discussing, not using environment variable, but having the specific callback that you choose be the thing that differentiates, but I think we could discuss it in a design.
Sergey Sergeev 00:18:52 Yeah. And speaking of callbacks, now, we switch into the last point I wanted to discuss. If we can go back that agenda.
So I was thinking how we can do evaluations in Runtime one that telemetre and
again, I think there is an a callback
option in open telemetry instrumentation, where also you potentially can
make a callback for every telemetry you receive
to do, for example, some runtime evaluations. But.
It will be very helpful to
target evaluation. SDK, to those gen a types. So you don't have to parse like span attribute name
to find request and response.
If you have lm, Gen. A type.
so you can expect it has some.
Get their setter for request response, and you don't care about which telemetry it will be turned
under the hood.
Aaron Abbott 00:20:15 Yeah, I think.
Well, I'll I'll anybody else speak first.st But I know we have some kind of data model already in Google. Adk for this, and I'm assuming other agent frameworks do also.
So maybe we could have something like that as a starting point. Anybody else have thoughts.
Sujay Solomon (Google) 00:20:37 Sorry here. Do you have specific evaluation sdks in mind.
Sergey Sergeev 00:20:43 Again, we should support open source vibraries make it blogable. Basically.
evaluation is like open lead, and so on. I have
some Api, so you basically can evaluate request response for bias
correctness and etc, using Lm as a judge or prepare machine learning models.
But basically, yeah, it will yeah, go ahead.
Alex Hall 00:21:21 I'm trying to give an example. We have a package pydantic evals called evaluations SDK, and it has functionality, for, like collecting
all of the spans that happen
during an evaluation run, and then you can look at those bands to specifically like you say, to see what messages were sent to the Llm. Or how did they respond? So you can even judge the
the internals rather than just the results.
Sergey Sergeev 00:21:48 Yeah. And I think the helpful
a part to to try to make it how to say enable
enable out of the box so potentially
just making sure that you can set against something like environment, variable or parameter
to evaluate all your Gen. AI types compatible with evaluator. Let's say, if you have. Lm, Gen. AI type.
you can potentially target to that type different evaluator webinars and produce evaluation metrics.
Sorry I see a lot of hands. I think I'm taking too much time as well.
Aaron, go and go with it.
Aaron Abbott 00:22:40 Oh, no, no! Lamilla was first.st
Sergey Sergeev 00:22:43 Go ahead and place your order. Go ahead
Liudmila Molkova 00:22:46 I wanted to mention that.
we I'd like us to separate problems. The 1st problem is a callback mechanism or injection mechanism that allows you to do stuff. I think the Pr. Aaron was showing suggests to have call back mechanism and suggests to provide types.
For the
prompts and completions. So you can build an relation solution. On top of this, there is a big section with text underneath, like the sculpturing constructions inputs and outputs in this Doc.
and if we start there.
we can expand it. Somebody can build custom solution. We can have a country component that does evaluations and stuff.
So we. So we need to make progress on the 1st steps.
So I wanted to say, Thank you for bringing it up.
Sergey Sergeev 00:23:47 It sounds good. I really like when you come up to some idea and discover that the community is converging in the same space.
I think it's really good for the end, too.
because there are so many benefits of building this SDK and tying it to the standards.
Do you want to move next.
Aaron Abbott 00:24:17 I was gonna say something about the Evals, but I think we have a pretty full agenda, should we?
So we move on if nobody else has any topics on this.
Sergey Sergeev 00:24:28 Yeah, I can propose basic. I will review definitely the Pr and types and maybe add some schemas diagrams, I think, mostly visually.
So. Thank you so much.
Aaron Abbott 00:24:44 Okay. Great.
Liudmila Molkova 00:24:45 You.
Aaron Abbott 00:24:50 Sujay, I think you're next. Do you have any rough time box on this.
Sujay Solomon (Google) 00:24:54 5 min.
So this is just I'm just surfacing, like, I've been talking to the image in Pm, on the Google side. And you know, when you start going into the multimodal side of things, tokens don't work real well as billing units and I think at least on the image inside. They're using image count right now as
the unit. And then on the audio video side, it looks like billing by seconds seems to be common. So I'm bringing this up, not because I I'm necessarily pushing for that to become the the convention here, but I'm curious on where others are seeing this and whether other. It looks like somebody's adding that
Openai has built in tools, and they build differently. But is there some way that we can provide a bit more flexibility in the conventions for how people can include either billing unit and or like account
for that. And I just saw that the I looked at the the issue there, and the suggestion there actually is is quite seems quite good, and it keeps it generic enough.
But overall, it just wanted to surface that that need is bubbling up, at least within Google. And I would love to have some convention I can point them to rather than them doing their own thing.
Liudmila Molkova 00:26:24 Yeah, the problem is cost that you don't know the cost on the producer, right? And the client.
Sujay Solomon (Google) 00:26:31 But it can be an optional one if it's coming from the server side, potentially right like.
if the if the model itself hosted model is generating the telemetry. It could include it.
Liudmila Molkova 00:26:44 Oh, right!
Absolutely.
Samuel Colvin (Pydantic) 00:26:47 Think sorry, Linda. I'll let you go.
Liudmila Molkova 00:26:50 No no no go ahead! Go ahead!
Samuel Colvin (Pydantic) 00:26:51 I was. Gonna say, I think this is this is Adrian from our team asking for this. Our idea is that like customers in our case would
in in cases customers. Some cases customers know the cost, and we don't know their custom costs, and so it would be nice to be able to
define the cost. It's not ideal having to like. Do all the calculation of cost within your application. But
there are, there are scenarios where it might be the best option.
Aaron Abbott 00:27:23 Out of curiosity like the
The use case here is like, I want to know the cost for this trace or the spend. It's not like getting an overall cost estimate.
Don't know.
Samuel Colvin (Pydantic) 00:27:34 It is precisely that people want. Sure they want to see it on an individual span or trace, but they also want to be able to go and do the aggregation
and see how much have we spent in the last week.
etc, etc, how much of my different dev spent on, you know, different projects.
I mean
I. Although Adrian works with me, I slightly disagree with that. This is the best way of doing it, because I think, like going and setting up your cost in your SDK each time is somewhat problematic.
I'm being a bit mean to him as he's not here. But he was like, this is this, Pr is getting lots of traction. So we don't need. He doesn't want to implement it in our database. Basically. So he's trying to find another place to implement it. So which I understand because
there are. Obviously there are a number of different cases. There's obviously the like most commonly used models. That's fine. There's the brand new models when they come out. When people want to be able to see costs. Then there's people with custom pricing.
I also think we don't know where pricing is going. To what extent do I pay a different amount above X tokens per request. Is that stuff going to happen? So it's hard. But
I mean this as a a option would be valuable. But I'm not going to say it's a panacea.
Aaron Abbott 00:28:49 Yeah, yeah, that makes sense. I I would just agree with Alex. Like, I think we already have probably token count counters and stuff like that. So if it was
forgetting the overall roll up, that would be useful.
Samuel Colvin (Pydantic) 00:29:00 Yep.
Liudmila Molkova 00:29:03 Assuming all backends reported, like the older providers reported to some extent.
Would it? Well, it would still be interesting on this pans.
because it gives you per operation cost right?
Samuel Colvin (Pydantic) 00:29:23 Well, there's a secondary issue, and I presume we don't want hotel to solve it, but which is a shared good up to date, public database of what the different models cost in the for the like default case, which is another enormous headache at the moment, I think every provider is sort of doing their own attempt.
We're wondering about building our own. Can we copy it, or can we just piggyback off someone else?
Does hotel want to take, take on the job of having a database of all the costs.
Liudmila Molkova 00:29:49 Oh, no! No! No!
Samuel Colvin (Pydantic) 00:29:50 But I don't. I assume the answer is, no.
Aaron Abbott 00:29:54 Isn't there a separate project for this? I don't know if it's Cncf. But there's like some
cost estimation, big open source project right?
Samuel Colvin (Pydantic) 00:30:02 If you have a link, I'd love to love to see it.
Aaron Abbott 00:30:05 Okay, I'll I'll have to dig it up. I don't remember the name. The top of my head.
Samuel Colvin (Pydantic) 00:30:08 Open router have relatively good costs. They have an Api, but it's not open. It's just they have an Api endpoint that you can get most of it from.
Liudmila Molkova 00:30:19 The the tokens overall is a big problem.
right? So if you I've I've been trying to come up with some good proposal that would at least be extensible and clear to say, Okay, we have now input and output tokens. But then, if you look into, let's say openai Api, they have audio tokens and they can show up, I think, either in either places it's not always clear whether they are included in the input tokens. They also provide
and there's also reasoning tokens and different flavors of of things. So
I definitely think we miss more precise definition for for
something that can be translated to cost.
I also feel that, like.
if customers want to report cost, they can report cost metrics separately on their own.
and then you can derive the cost for your tokens
from the combination of these 2 metrics
like, if we have a metric of cost per token.
Then you can multiply one metric versus another and get the result that you need. So we don't need. I feel like I. I would rather not have.
Aaron Abbott 00:32:07 We lost the vanilla. Right. My!
Where's my audio? Just broke in.
Yes, seem seems so.
Liudmila Molkova 00:32:13 I'm back. My zoom has crashed. Sorry.
Aaron Abbott 00:32:17 Okay, I was waiting for somebody to.
Yeah.
Liudmila Molkova 00:32:20 Yeah, okay, so long story short, I think we have a problem with tokens. I think we can. We? We need to solve it the cost is super interesting. I wonder how we can solve it?
could Suji, do you think we we can make a proposal.
Aaron Abbott 00:32:41 I think so.
To drop.
Liudmila Molkova 00:32:43 Oh, yeah, I'm sorry.
Aaron Abbott 00:32:45 Oh, no, no worries. So I do see. There's some recent discussion on here.
the I don't know about focus, but I think open cost was the one I was thinking of, Samuel. So
I mean, like we said, if if somebody else can solve it, it would be awesome.
ludmill, I think whatever you were saying makes sense like we just have to make sure that the metric dimensions are.
They make sense. They don't have separate units, because then we can't
aggregate them. But it seems like a good.
Liudmila Molkova 00:33:15 I see. So we will figure out what the the the types of tokens that we have.
and we would have the same attributes on the just the token usage.
And then we can
ask vendors and users to report the cost metric per token that has the same dimension. So you can.
Yeah, I can write down this proposal here.
Aaron Abbott 00:33:46 Okay.
Cool. I'll just. I think it's already. Yeah. It's already in the meeting notes. So.
Liudmila Molkova 00:33:53 Oh, wonderful! Thank you!
Aaron Abbott 00:33:58 Alright cool anything else on this one.
Okay, cool ship. Are you around.
shiprajain 00:34:09 Yeah, so shall I share my screen?
Aaron Abbott 00:34:14 Oh, yeah. Please.
shiprajain 00:34:31 Please let me know. Once you can see.
Aaron Abbott 00:34:37 I think it's still, yeah, okay, we can see.
shiprajain 00:34:40 Okay.
so today's discussion is in continuation to the the quick proposal that I presented last week
in the same call, which was to basically propose the standardization for multi agent tracing
of a multi-edged system
the gaps that we observed with respect to tracing that is happening in existing systems. And the proposal on how we can fill it. So I'll keep it short because this was covered last week as well, mainly the couple of feedbacks that to us we have acted upon them. So I prepared this Google Doc,
proposal for everyone to start collaborating and sharing the inputs.
I have also kind of mentioned on the current scope like we discussed last time that this whole discussion can span into multiple, I mean.
starting from multi agent architectures starting from multi agent systems, how we can do the tracing for for you know, single turn, multi agent conversational on conversational. And, you know, taking it ahead to different multi agent architectures, how the tracing should look like.
So in order to keep the Mvp. Small for this particular discussion we are covering particularly about how the initial tracing should look like for a multi-aging system, and we have replicated this on an industry inspired. Use case, which is a travel planner, multi-aging system.
Details capturing in the document below.
So that's and then I mean to mention side by side, me and my team. We're also iterating on these points. But I think these things these topics more complex topics. Maybe in subsequent discussions.
Now, having said so, one of the changes that I did to the proposal that I presented last time
was based on the feedback where earlier we suggested of introducing a new task based span at the root of the hierarchy
and enhance some events under existing span calling agent we got the unanimous feedback that it is better to represent events as spans. So in this particular, Doc, I kind of converted a proposal aligned with that feedback already.
and then talking about few more attributes that we should have in the existing inbox span as well as execute tool. So that is the
the gist of what we are proposing as new.
Here is the trace visualization, I mean, the picture might look might not look clear. So I've also posted a link over here in case anyone it's public right now. So I hope you guys will be able to access it. If not, please let me know I would need your you know, personal email, Id or any email Id which you usually use to access landfuse traces. We will add you to the project.
I could also quickly show the trace itself, and now digging deeper.
so as the initial proposal as per the initial proposal, the idea was that in multi agent system have I mean existing hotel has invoke tool as 2 main spans and couple of attributes. Within these spans, as well as some generic attributes. I've also covered that in my document for glimpse.
for a multi agent system, these spans are not enough to capture the entire workflow at the same time. Now, the notion of in the in multi agent architecture, we kind of approach with the notion of
giving a task to a multi-aging system to solve it, which is further decomposed into subtasks. And then, you know, it is identified. What is the right agent and tool to solve those each tasks. So from the idea. From this idea task, basically,
you know, comes at the root of the hierarchy and controls this whole workflow. So that's what we have tried to depict in this sample trace.
So if we expand it it basically starts from the root span, which is the task span.
We can also visualize how the content within that span looks like.
We are proposing to have an execute task as being done. Some more details like task id description.
You know what constraints are given right in 1st place, by the user. Which is
this? So the constraints having a separate placeholder for that.
What are the giant assigned agents for this particular task, which is nothing but just the orchestrator agent
in this particular implementation and some more details.
you know, which we are capturing as events in form of existing events, basically the user message and stuff like that. So from here we start, which basically passes the control to the orchestrator agent. The information that we captured in this span.
Now at this stage we start off introducing those child spans which we are initially proposing as events. So, for example, the very 1st step that an orchestrator might need to do to identify how this main task should be broken down
and that
depicting in all these different attributes. I'm not going into details. I'm just covering at the high level and also what kind of inputs would be needed for each of those.
And with this.
with this initial planning, we take the segue of getting into the next step, which is calling the next plan. And you know how the agent to agent interaction should start. So basically now based on this planning orchestrator, would identify what is the 1st subtask to be solved. And an agent to agent interaction would enable the
handover. So this one
cover some of the important details like, you know, what is the source agent, target agent? What is the interaction type?
The message type, which is basically a request from request sent from an orchestrated research agent
and other details in form of what will be the data the payload.
Once this is done, at each step. We're also retaining the context
updating the memory. So we have a separate span
call memory update span, which gets called at different steps to keep on keeping the track of the the buildup context.
Now.
if you see here, just to make the description clearer orchestrator agent calls it, which gives back some information. It goes to itinerary agent
and budget agent, and at this step we understand that the data constraint mean constant was breached.
And that step replanning happens, which is nothing but calling the plan task span again.
So this is basically the the quick flow.
And if we expand how each of these individual you know
get triggered. So at the top we talked about, you know, calling the research agent so exactly execute task span is the subtask
span starts which internally calls the invoke agent. So everything basically is guided by the task that has to be performed by that particular agent with the necessary information covered in the metadata. So that's the that's the main idea. And while trying to represent it. We have also covered in details on what kind of attributes we feel should be added. I have also summarized them in the documents.
Liudmila Molkova 00:42:36 Okay, can, can we stop here for a sec?
shiprajain 00:42:40 Yes, please.
Liudmila Molkova 00:42:43 Some questions. Did we instrument some framework, or did we
like, how did we report this data?
shiprajain 00:42:54 Yes, so we started off enhancing the semantic kernel as the framework.
So I mean partially the the traces were generated from those, but until today I could not complete that poc, we are still working on it. So maybe in few days be done. This is the further depiction of the the next step. So basically, this is a simulated trace as of now. But we have promising results from our Poc until now in implementing a similar
example in semantic hurdle.
Liudmila Molkova 00:43:29 Yeah, thanks. So this is simulated. When we execute a task.
Do we
like one thing, I'm worried about that when we simulate. We don't take into account what's actually available
to the let's say, semantic kernel. Does it know when it deals with multi agent system? How easy is it to implement it like, did we take this into consideration?
shiprajain 00:43:59 I mean that we
there, there certainly will be enhancement that has to be done at agentic frameworks. And in order to replicate this task based notion.
Now, how what extent? To what extent those changes
would be needed. We would get to know once we complete our Poc.
so today, I don't have very clear. Yeah. Answer. But but in one more piece of information I want to share that. We also adopted the multi agenting architecture as orchestrator based architecture. I like, I briefly talked in my document. There can be different kind of architectures that a multi agent system can be implemented in. And eventually we would also want to show how the proposal that we are making is unified across different architecture.
And if there are any differences. How do we capture those differences so gradually that information will also come. But I think in this phase, we want to get to one successful Poc using semantic kernel. And we are basically making changes at how sk itself can emit the traces like this.
So okay, is there any other question. Sorry I'm not able to see the chat.
Liudmila Molkova 00:45:20 I think Sam has a question, Sam, do you want to go ahead.
Samuel Colvin (Pydantic) 00:45:24 Yeah, I am. So a few things. One, there seem to be 3 different. I mean multiple. But in particular, 3 new things here. I wonder if it's worth thinking about them individually, or do they need to be implemented together? And then I think my other concern is Lud Miller's point of. So most
most things at the moment are the kind of
delegation workflow, right like where you're effectively calling another agent through a tool.
In that case.
like we already have the tool spanned. My worry is that it's going to be quite hard in the way you call the agent from within a tool to link up all of the correct set all the correct attributes, or to make it easy for that to happen within a framework, especially if you're using something like Mcp, which has its own observability.
Implications, challenges Yada Yada. It's going to be quite hard to set those set the right fields when you run the kind of sub agent. Then you have the a 2, a model of kind of handoff
that seems like without knowing as much about it. That might be slightly easier.
But yeah, I think the 1st thing is, it'd be interesting to to think about doing these separately.
And my concern is basically, how much is it? Is it possible really to set these things in the framework? Because if they're not set in the framework, individual implementers are not going to go and set them.
shiprajain 00:46:53 Yeah, yeah, I agree. I think once you read the documentation also in the Appendix, I have given some details on how this idea of keeping task at the root of the hierarchy, and then deciding what is the agent and tool which I needed to solve. That particular task is stemming from a 2 a documentation, we read, couple of that were built by a 2 a. And in this
documentation, also in in in the trace, you'd also see how we are trying to draw the parlance with Mcp. So that's 1 quick point. I mean, we are not completely there. But we I mean we. We are kind of extending the idea of a 2 way.
The other thing is, I think, one other point that you mentioned, which I felt was not completely correct. Or maybe I misunderstood. So
we are trying to define a task at the root level. And that's the new task or operation type we are suggesting called execute task, which basically
2 series of steps
which is kind of depicting how a multi agent system could think or would proceed, and that's the kind of recapture. It may be delegation it so. Whether it is delegation or not, that completely depends on the kind of multi agent architecture that we are
choosing. Here. It is orchestrator based. And it seems more like, you know, there's 1 central agent which is using some internal mechanism to task plan and then figuring out what is the next agent? And that's the central agent. Which kind of does this? Or you know, multiple times.
We don't call
another agent from a tool, I mean, at least, that is something which we have not thought through and instrumented here. It's mainly a task initiating the planning and agent to agent interaction. And and then one agent calling another agent and agent calling. So it's like that. The the flow, which is also very much aligned with what hotel says, but
just building more on top. So those were come. Some of the
think, you know, point of views that we had in order to build this, our eventual goal was also to come up with the traces which can finally be different monitoring systems and evaluation systems. So that enough information is captured and how the flow actually happened is captured which gives enough details on, say, doing an offline evaluation whether the agent
followed the right path. It made the right decision on the go, and if all the needed information is captured enough in the traces for evaluation systems to make that call. So that was also motivations for us to come up with a proposal like this.
But I'm I'm very happy to hear more thoughts like I said that I've also given references towards the end in the appendix on the a 2 architecture
from which we also sought inspiration. So kindly go through it, and you know, please feel free to add comments.
So taking your feedback now, so we'll try to dissect and see what we can. What bare minimum we 1st in 1st cut.
and how we can incrementally build on top.
Samuel Colvin (Pydantic) 00:50:16 Okay. I don't have anything else, Aaron. Maybe you do.
Aaron Abbott 00:50:21 Yeah, yeah, I was, gonna say, I, I like what you said about doing it incrementally. I think.
it's good to have this as like a starting point, and then add pieces. It. It seems like pieces could be kind of chunked out. I think we addressed the A to a piece. But that was one thing I was gonna ask was, I think, a to a has this. The python SDK has some instrumentation now. I was wondering if we used it here, and we could see what it kind of spits out, how it does propagation, and and write some of that stuff down in the conventions.
shiprajain 00:50:50 yeah. So we we did see that. But it was some time ago, i'll have to refresh that, so maybe I can bring that up? In the next call, or I can continue to enhance this document under feedback section. So what I'm doing is just maintaining a separate feedback section all the feedback that came to us on 10th
of
how we are addressing them. I've briefed it. I can keep adding more sections on each day that we present, so I can enhance here. And then
mark you for review, for offline review.
Aaron Abbott 00:51:25 Yeah. Yeah. And that was my. My other question was, do you think this is ready for? Is this just kind of early feedback, or whenever you're ready, like, we could open it up to comments. And I can share with some Googlers internally, and stuff like that.
shiprajain 00:51:39 So maybe with this initial team, we can circulate it 1st and then take it ahead if maybe by next week. So far I have received like 2 feedback and we are trying to replicate in the sk frameworks. That's only action. Item I have as of now.
But yeah, suggestion from this group. If if you guys think we can start circulating, I'll be okay.
No, that's true from yeah. Okay. So I have my colleague Paul, in the call.
Paul. What do you think.
Paul Shealy 00:52:14 Sorry I shouldn't find the unmute button.
I agree with like one, maybe one week of internal review, and I like a little bit. We'd like to do a little more prototyping, and then yes, maybe in a week. Let's open up for further comments.
Aaron Abbott 00:52:28 Okay, that sounds great.
shiprajain 00:52:32 Awesome. So that's all I.
Aaron Abbott 00:52:37 Cool. Anybody else have thoughts on this, or should we move on to the last one in about 18 min?
Okay, but no, I think it's you.
Samuel Colvin (Pydantic) 00:52:49 I just had one apologies to be kind of damp scrib on this, but I just think
like I think I've said this before in these meetings, like
agents, are pretty new to lots of people into agent communication. While there was an awful lot of talk about it. Everyone says that the little. The use of these things in production is is fairly minimal. So my caution is is as it's been before, that it's very early to define specs for some of these things while they're still evolving so quickly.
I know that's an annoying general piece of feedback, but I think it's worth saying.
shiprajain 00:53:22 Agreed, agreed.
Paul Shealy 00:53:24 Yeah, I'll I'll address that one. So we we do.
There are some areas that we've looked at that are a little more exploratory that we're not pulling into the spec yet. Here. But we're hearing from one of our customers is
the things that we're looking at. Here are a little more firmed, and they're often
wanting to see this level of detail for like further investigations.
So I do agree with the feedback. But I think we're getting aligned with it here.
Liudmila Molkova 00:53:55 I think we all agree that there are key building blocks like the single agent execution.
And we can focus on the the as we prep a prototype.
we'll see that we have to focus on them, because
some things that let's say semantic kernel knows, or another agent framework knows are limited to this agent's task, whatever it is, and it doesn't even know that it's executed in multi agent scenario. Necessarily.
So
if we focus more on the individual building blocks and have means to identify the whole flow across all of them. That should give us
the basic experience.
And, like handover is another unit that we can focus on
but we really cannot control where it appears in the trace, how it happens, and we probably are limited in what we know about it.
shiprajain 00:55:02 Yeah, a little more. So we are on it.
Yeah.
Liudmila Molkova 00:55:07 Wonderful. Thank you.
Cool. I wanted. We have just 5 min, and we definitely cannot go through the planning. So one thing I wanted to bring your attention to
is we? I it's it's my feeling I don't feel we've been. We are focused, and it's a good thing because we are building consensus in the new areas, right?
But it's also we are not making progress on the existing carriers. So I had a doc.
let me find it.
Here we go.
So I've tried to summarize things we are working on across
like we're discussing them every once in a while, and maybe we can work together. Maybe next week we will block. I don't know 30 min to
try to prioritize areas and try to build consensus of what we should be working on.
And I'm going to share this doc with everyone
in the chat and in the meeting notes
feel free to add your comments or suggestions.
If I can, I'll add it to the this as well.
Oh.
there we go.
Okay. So the key areas.
I think we are
that we are doing a bunch of refactorings of the existing conventions with the goal to make conventions
used by and usable by backends like Arise
log fire, and others who would prefer attributes rather than events.
And we are enabling a bunch of scenarios right? The the external storage support. The what else
of them?
Evaluations and things like this? So there are a bunch of pull requests that we have that are contributing to this refactoring.
I'm just going to go through some features, and I'm going to ask you folks to maybe spend some time offline thinking about what you would prioritize and what how would you arrange this list?
The second thing that comes a lot are evaluation metrics.
And everybody's kinda interested, but nobody is trying to unify them. There were some attempts in the past. It seems we we can maybe tackle this.
There is a big work stream of onboarding instrumentation libraries bringing them in. There are people express interest. But yet we don't do this. So maybe we can actually try to assign some work items. If if people are really interested, then they're ready to work on it.
And there are tons of new features that we are discussing like multimodel content that today's discussion about costs is part of this, I feel. But there's way. More than that.
we have somewhat related topics for feature, sorry frameworks and agents and Mcp and multi agents. They are kind of intertwined.
but they're slightly different.
And there is a big part. That's the server side. We we even we didn't really touch upon this.
and it's vaguely how I prioritize them in my head.
But anything in this spaces it's quite a I don't know how to prioritize them.
So again, I would love your feedback on what you think we should be focusing on, and I think we should, we need to start focusing on something.
Aaron Abbott 00:59:55 Cool sounds good. So just basically take a look. And then we can each speak to our priorities on this stuff.
Liudmila Molkova 01:00:02 Yeah. And maybe if you have specific interest in certain area, if you if your company funds this work, if you are ready to work on this. If you can actually contribute in this space, it would be nice to know.
And let's try to spend some time next week to understand what people are interested in and what they are ready to work on.
Aaron Abbott 01:00:24 Yeah, that sounds good. Thank you for putting this together.
Liudmila Molkova 01:00:28 Yeah. Thank you.
Okay, thanks a lot. Everyone. Great discussion.
Aaron Abbott 01:00:35 Yep, alright. So next week.
Liudmila Molkova 01:00:38 See you next week.
