SIG: LLM Semantic Convention WG
Date: 2025-07-29
Duration: 85 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:01:57 Hi! Everyone.
Josh Bonczkowski 00:02:01 Hello!
Liudmila Molkova 00:02:10 Let's give people a few minutes to join.
Liudmila Molkova 00:03:21 Okay, so let's get started.
Let's copy over the participants understanding topics.
Let's see what they have.
So quick. Update, we, we actually had a pack meeting today.
and I probably will spend a few minutes
updating you folks on some discussions there.
And do I have plenty of
topic. So this this we discussed.
Go on.
We have one from Ankit.
I would like to reserve some time to
close up the last discussions on
this. Pr.
Do we have other topics? I think we had a couple of prs for
from Microsoft and Cisco and multi agent stuff. Do you folks want to talk about them here.
Pavan 00:05:03 Sure. I think some of the comments that you had,
you know, left in in that Pr. Made total sense. I was trying to take some time to review that. But if we wanted to also bring that up in this meeting, happy to do so.
Liudmila Molkova 00:05:21 I mean, if you, if you feel you don't need to, then let's not. I'm just asking in case you want to edit it to the agenda. But if you feel you're fine, then
oh, let's not.
Yeah.
Pavan 00:05:33 Okay, I could basically take 2 or 3 min if if there is some time.
Liudmila Molkova 00:05:39 Sure.
Pavan 00:05:40 Think my Pr is 2, 5, 5, 1.
Yeah, thank you.
Liudmila Molkova 00:05:52 Of course.
Yeah, that's the right one.
Awesome
And
did I just break?
Yeah, I I think I put it in the wrong place. There I go.
Okay, so let's get started project triage board.
Well, I will hope I hope to clean it up sooner than later.
Because the inputs and outputs Pr, there are a bunch of things that are in progress that are
not quite moving.
Let's close here.
No, I think there are there. We have an utils, hotels, discussion. We still have some Cp.
This one gets told.
Aaron, do you want to close it.
or do you still want to follow up on the Pr.
Aaron Abbott 00:07:14 Hey? Sorry. I just just joined
Liudmila Molkova 00:07:17 Oh, no, no worries, it's it's not super important.
So it seems you're still planning to work on this Pr. At some point.
Aaron Abbott 00:07:26 Yeah.
Liudmila Molkova 00:07:27 Okay.
Okay?
Oh, we have conventions for Mcp and Review. I think Drew is making progress on this one.
And those 2 are related.
Okay, no, nothing new has been created.
So let's move on to the main agenda.
We had in a pack call yesterday with Minghu and other Alibaba folks.
They are just to bring you up to speed on what we discussed. 1st one. They have some
instrumentations that they would ideally like to contribute.
They are super interested in the utils that would help them. They looked in the document. They liked it. They might leave some comments.
With the details.
We talked about them bringing up the instrumentation.
For example, this one.
The challenge is that it might include a lot of things that we don't define in semantic conventions yet.
Such as reasoning and maybe something else.
And they actually would like to bring instrumentation without documented conventions.
I personally think it's not a great idea.
Given that if we bring the link chain and another framework instrumentation, and both have have undocumented conventions. Then we are on the
worse spot than having this instrumentation somewhere else that that's my review on this I
I'm open to changing it. But I would actually like people to at least document the conventions in the draft Pr before they
send them to.
Our repositories.
Alex Hall 00:09:40 Can I ask, what what is the goal when bringing
something into the the contribut repo
like? It's a very big repo in which it's quite hard to develop.
and things move very slowly. Releases are spaced far apart.
Yeah, we I've been thinking about. You know, we said that we would donate certain instrumentations from Pydantic like for the agent Openai agents. SDK,
I'm thinking it would just make things harder when we wanted to maintain that.
Liudmila Molkova 00:10:17 I can tell you why we would do something like this in Microsoft.
Because, let's say, there is a work fire instrumentation, and it's behind some license
you folks can change this license at any moment.
and we, as Microsoft, cannot provide
any support for the packages, so we cannot recommend our users
to use your instrumentation, however good it could be. Right.
So we need the instrumentation to be governed by some reliable entity like Cncf.
That would not disappear or change the licensing, and that we can influence.
So while let's say, Look, fire.
speed is very fast. It's nothing guarantees it to remain the same. And up in telemetry it may be slow, but we know how to influence it, and we know how to.
That it's reliable to a certain extent.
Alex Hall 00:11:26 I'm pasting something in the chat which is a link to a Microsoft blog article recommending using the logfire Openai agents, SDK instrumentation.
Liudmila Molkova 00:11:37 Microsoft is big. But yeah, we would not support it. We can
in the blog post, but we can provide support over it that we would.
Alex Hall 00:11:45 What does provide support, mean? Like.
Liudmila Molkova 00:11:49 I, I think, do we need?
Yeah, I mean, the other reason people bring instrumentations is that they want to share the burden
once it gets pretty much stable it doesn't change much like open AI. The the burden of maintaining it is relatively low.
So you share it. You pay back
to the community. You'd be a good community player, and you
also rely on other people to help you fix it. If things get broken.
Alex Hall 00:12:35 Okay.
Liudmila Molkova 00:12:36 So ideally from open telemetry side, we would lose
libraries to be instrumented natively, so that Openai would instrument their code according to semantic conventions. Would this ever happen? Well, who knows? Azure sdks or
instrument it? And as much as we can we follow semantic connections?
Okay. I
not sure. I convinced you my goal was not to convince you to donate. But I I definitely would like to chat more about if you're interested in the donation, and what would be the the blockers
the release process is one. But we actually release Gen. AI stuff on demand.
So it's per package.
Okay? So the last update from the
a pack call that Minkkoi will investigate the geni operation type.
There is an issue about this. If anybody is working on it. Anybody is interested, please chime in on the discussion.
There are some different thoughts here in priority. If you have some convention that are similar to the
spend kind or operation type. Please. Go ahead. Drop the link here. It would be very useful for me who is doing the investigation.
Okay? Moving on to the next topic. Anki, do you want to talk about evaluations?
anksing 00:14:36 Yes, so I host this one, if I need to dude.
Liudmila Molkova 00:14:41 When I present. Do you want me to present.
anksing 00:14:44 I mean, whichever works, I think what I got for me.
Yeah. And I think, I've also updated the Md file so it might be easier to look at that. Events.
Sujay Solomon 00:15:02 Good morning!
anksing 00:15:03 And for some reason it did not show up in the this one. So if you just scroll up just above the custom events, it's there. I'll update the update.
So talk to kind of restrict like that. Okay, awesome.
So the main idea for this event is to capture the evaluation scores
and see them alongside your traces. And
this could be added at any span level. For example, it could be added as a at a
tool call, or like execute tool span, or it could be added at invoke agent span.
So there are certain fields that are valid in here which kind of
describes and captures some of the things that make sense and are helpful. So 1st one is the gen evaluation name. So this is basically
what you're kind of evaluating. For for example, like relevance or intent resolution.
error type, just to capture, like whatever in case there is an error while calculating the score.
and the 3rd one is Jenny evaluation dot score this is the actual score that you get. It could be
not just an Llm. Case. Llm. Is a judge based call. It could be like even something like f 1 score or score blue score
and then, any kind of evaluation metadata. So the main idea for having that evaluation, hey, Alex.
Alex Hall 00:16:43 Did you say that this would be a child of like an L. And M. Or an agent span.
anksing 00:16:49 Oh, this would be an event. This is defined as an event that you would add to your spam.
Alex Hall 00:16:56 Why, why would this not be a span on its own, which actually is the parent of possibly an Lm.
Related spam like.
anksing 00:17:08 Yeah, I think that's a that's a good point.
so one of the reason like you're thinking about like, why, I propose it as an event rather than a span was
like
a span like you would capture. Not just the score. You would probably want to also capture input and output. But I'm not sure like, how
often would user want to. Also like, look at the traces, for like, how many how you came up with that matrix or score, it's possible the customer wants that. But then
And.
Alex Hall 00:17:47 Library, and you know it's to me it's a well-defined operation, you know. You
well, there's several levels of operation, but it's you know, it's. It's a task that takes some time
and encapsulates any number of things within.
anksing 00:18:06 Yeah, no, definitely, I, I think I'm also looking for like feedback from this group, like.
since there have been like a lot of experts here like who have probably done a similar thing. So and the other reason, like, I also thought, like we could do where this event, probably, if needed, could also point to a span which actually gives you the traces of like, how you came up with that score.
So that's another way I was thinking of, but definitely like looking for feedback on
what would be a better approach.
or what would be the best approach to capture the evaluation score.
Liudmila Molkova 00:18:47 Have some thoughts. The 1st one is, let's say they are. The evaluator
is is essentially a separate infrastructure, right?
Probably a different service.
anksing 00:19:01 Yeah, definitely.
Liudmila Molkova 00:19:03 And the spans that describe evaluator internals and the duration the
I don't know. Status and extra attributes I don't know service, name and stuff like this are
about the different service. You wouldn't.
They are part of the evaluator internal telemetry.
The what's important when you look into your
data and how it was evaluated.
It may be separate. Maybe we can merge this together.
But having an event solves one problem that spans is hard to solve.
how do we identify this specific telemetry
item that describes a violation result?
We can query spans and have a special property on them like a violation. What score relation name?
You can use this as a filter.
and we can say event, name as evaluation result.
So I feel like, even if we have the spend.
it doesn't mean that we shouldn't have an event.
But I'm also curious what other people think.
Alex Hall 00:20:32 Didn't follow what the event contained. In addition to the span.
Liudmila Molkova 00:20:38 It will go to a different place.
like event goes to somebody who requested the evaluation and internal elevation. Telemetry stays within the evalator service.
Sorry. I think Sujay has something to say.
Sujay Solomon 00:20:56 I was just gonna say, maybe we can work backwards from what
we suspect. People will use this information like what, how we will, how they will use it. Right one, I think, when somebody is viewing a span that has to do more with the agent's execution.
it is necessary for them to be able to correlate that span with the results of an evaluation that happens now that evaluation could have happened either online, like
right when the agent was executing, or it could be sort of a batch batch, offline thing that happens. In either case, I think
we have to have some way of correlating that
agent execution span with the evaluation results. Maybe we can work backwards from like that being the user goal to how can we come up with conventions that would support that.
anksing 00:22:04 And I also want to bring up like there have, and like, there are cases where where I've seen like
where you like as a customer. You would probably not never see the evaluator stance like on how evaluator came up with the score, because that's some like kind of secret sauce by some company behind the scenes, and they do not expose that, and only thing that's exposed to the customer is the score that they get, and then some sort of reasoning on why that score was given, but how? It was calculated, like not
be exposed to like the users that are some
secret sauce thing for a company that provides that functionality.
So in that case, like, would it mean that the span the scores holds the scores
and not the actual like the execution of on how you came up with that score.
Hardik Surana 00:23:05 I have a clarifying question the. The intent of
sending these events is the intent to fire off the fact that, hey, you want to conduct an evaluation for a prompt and response pair, or the evaluation has already been conducted. And this is just an event showing you what the results are.
anksing 00:23:25 Yeah. So the the aim of this event is to show the results of the evaluation so that you can see these scores, filter them filter by them, and then kind of look at like what's going on with your
agent or any Gen. AI app.
Hardik Surana 00:23:40 And in that case, like is is there coupling between the library or framework that you use to to have the conversation with the Lm. And the evaluation like, could you give an example of
like? What? How evaluation would be conducted? Because there, for any sort of telemetry to be generated. You would need.
or, like the relevant telemetry to be generated through instrumentation for that library. So, for example, if I'm using the Openai SDK to interact with my Llm. And I want to conduct an evaluation with the result of what I got back. I would also need instrumentation on whatever library I am using to perform the evaluation. Let's say I'm using Dpval as an example.
Wouldn't we need instrumentation conducted on Dpval itself to be able to collect any telemetry, whether that's a span or an event, or a metric.
anksing 00:24:39 I mean, that's a good point. However. Like as you give an example of a Dp, well, right? So. Dp, well is a client side implementation. So yes, it's possible. Say, for example, if you call a service, and which is a 3rd party service which helps you identify whether you have safe content or the response of your Llm. Is safe.
right? And there is some secret sauce behind. The service which takes your response tells you whether it is safe or not, but they don't expose anything about it like how they come like came up with that response. Right? All they give you is a score and a reason why? Right? So in that case.
even if there is instrumentation behind that service, you will, it won't be exposed to the customer.
So so the main.
Hardik Surana 00:25:25 The the, the person or the entity that is generating these scores is the entity that has the conversations as well, and they would be the ones who would consume it.
The consumers and producers of this telemetry are not different. Right.
anksing 00:25:42 They can be
right. So here, like, I have an agent, and I want to like evaluate how good a tool call was right. I can call a service and give all the data about the tool call, and then can tell me right whether that service emits traces which you can look at on how it generated the traces is dependent on the service right? What I care as a user whether my tool call like, do I get a score for the tool call. If yes, then I want to
kind of be able to filter my like traces where my tool calls are low and so that I can take more action. Right?
Okay? So the example that you gave where you want to be able to filter traces by.
Hardik Surana 00:26:26 The evaluation score. Doesn't that
put more weight on the case? That you should actually have evaluation scores as span attributes rather than events.
anksing 00:26:36 So so scores here are being proposed as event attributes.
So
Liudmila Molkova 00:26:43 We actually, maybe we can follow suggestion. And
anksing 00:26:49 Okay.
Liudmila Molkova 00:26:49 Think about user experience. I think it's probably
something we can easily change to say it's a span, or it's a event.
The attributes will be applicable, regardless.
Hardik Surana 00:27:04 Yeah, the attributes definitely make sense. But I would also go ahead to suggest that, irrespective of span or event, I guess.
since it's a score, it should also get generated as a metric as well.
Liudmila Molkova 00:27:21 What? Why.
Hardik Surana 00:27:22 Because I mean, these would. These would be gauges or counters. And you might. There is a use case where you would want to look at aggregates like, Hey, has my tool selection accuracy gone down over time? And you'd want to look that on a chart over a time series, in which case, having that as a metric would be easier.
Liudmila Molkova 00:27:48 As an optimization, right?
But you can still aggregate over events or spans, or whatever.
Hardik Surana 00:27:55 Right.
That's.
Liudmila Molkova 00:27:57 That.
Hardik Surana 00:27:58 Computationally easier from a observability back end perspective, to have it as a metric.
Liudmila Molkova 00:28:04 Yeah, the reason I'm asking is because there, this things are rare
and they are have high cardinality.
They are very expensive to calculate right evaluation. So you have very few of them.
So it might not. Well, it's definitely a better user experience. But it sounds like a very specific
use case where you want to
aggregate them and lose cardinality. But anyway, I think this is something we can always discuss.
Sujay Solomon 00:28:34 Yeah, I wouldn't, plus one ardic suggestion here, though, I think
yes, today, a lot of the the Evalds are very expensive and and not done super often, but
I think the direction that the industry seems to be going in is to make them much more lighter. And there's a class of evals that may potentially happen online continuously versus
you know, only happening occasionally or batched for those having
metrics that could denote something like quality as a golden metric.
Could, you know, could
could happen so I don't know that we should define conventions around that right now. We should probably like allow that to mature a little bit. But I think that the concept does make sense.
and in that case, like I think metrics would be much more usable in observability backends, as Ardik mentioned, than
than necessarily just spans.
Hardik Surana 00:29:41 And the added advantage would also be that if you generate it both as a span attribute and as a metric.
the another improvement to the ux could be. You go from looking at a metric to being able to find spans and traces that match that metric so that could be a filtration criteria that's easier to implement as well.
But events in general, like the stores that you would store them in, the correlations that you would do with traces or metrics.
It's just a different paradigm.
Liudmila Molkova 00:30:18 I I think we would do both. I think there are 2 hands raised. Xander, do you want to? I think you were first.st Do you want to go ahead.
Xander Song 00:30:26 Sure I'll be. Yeah, I just have a quick comment, which is, I think,
So from what I've seen
at arise, I would say, I think most evals are computed. Most evals that we see at least are computed post hoc, like not
during the execution of the span. I I, actually, I really haven't seen that very often.
where someone is like synchronously computing their Evals.
I'd also say, like, we see people computing
a lot of evals. So we we see, like we have some teams who compute evals for every single trace. And and so we do see some users and customers who don't.
who don't compute sparse evals, but like just always compute evals in spite of the cost of it.
Liudmila Molkova 00:31:14 Thank you.
Josh Bonczkowski 00:31:16 So this is Josh from new relic. And you know, similar to Zander with the rise. We've seen kind of similar behavior where lots of evals are always sync. The other part I want to call out is your, you know, discussion around metrics versus spans versus the events.
it's great to have a golden metric to understand overall health. But our customers are also asking for, you know, more specifics of like which of the requests have, which you know, kind of evaluation with it. So I can go search for. Show me the ones that have certain ratings, right? Or you know, for us. We also have the thumbs down thumbs up kind of scenario also.
So they're looking for. Not just this overall request had an evaluation that was X. But this particular request to the Llm. Within it, where there could be 5 or 6, especially when you get to agentic, you know, can identify exactly which one was the offensive one, or whatever whatever thing that was, was called out. And so the metrics won't quite catch that as well. That's where, like the spans, or whether the events, I think, will be much more handy to to utilize.
Liudmila Molkova 00:32:25 Josh, you. You mentioned that similarly to arise, that most devouts are computed
synchronously or asynchronously. I want to make sure I heard you right.
Josh Bonczkowski 00:32:35 They are. Our customers are doing it. Async today. Usually it's 1 of
many times, although they're, you know, sending it off to a 3rd party to be evaluated later. And then we only come back with the like, the span id, that where it came from the original request.
Liudmila Molkova 00:32:54 Yeah, thanks for the clarification.
Alex, do you want to talk about what you do at? Look for your at Pedantic? Or do you want to keep it. I just copied it from the chat. I think it's super useful to know what you do.
Alex Hall 00:33:11 I mean, we're we're also very much figuring out, figuring it all out as we go. But
my point is just that there are many places, many levels.
where you could be creating spans.
0 is a very surprising number to me.
Liudmila Molkova 00:33:34 Okay, cool. So I think it was a great discussion. There are a couple of things I'd like to summarize the 1st one.
We don't have an answer on whether it should be a span or an event.
We'll need to continue this discussion.
and definitely could also be a metric are.
The other thing is how relations are conducted. I feel like it's not important how the result would be
recorded in a similar way, and we can
go from from one definition and expand it if we need to.
Yeah. Nk, do you wanna add something.
anksing 00:34:20 Yeah, like, we just wanted to understand. Like for the 1st one, will it be a span or an events like
like, what's the process, or how can we kind of make progress on that in terms of like getting feedback? And then kind of like weighing out options like, what's the process overall?
Kind of finally get to consensus.
Liudmila Molkova 00:34:48 Sounds.
anksing 00:34:49 So this is like a conversation on the Pr. Which kind of weighs out one against the other kind of look at what makes more sense overall.
Liudmila Molkova 00:35:00 I, personally would be interested in how others are doing it. I'm not sure how far we can go understanding it. So identic uses spans
anksing 00:35:10 I see it.
Liudmila Molkova 00:35:11 What like arise does do we know? I think Xander needed to drop, but maybe he's open in the in the slack to answer this. It might be a little bit of a research.
anksing 00:35:26 Okay.
Liudmila Molkova 00:35:27 But it sounds like span is a
good alternative, and it should work. We should be cautious about the number of details.
I I haven't heard anyone except us 2, and keep defending events.
anksing 00:35:42 No, no, I I think it's more about like
I can understand. Like span can capture. Yeah, like inputs and outputs and kind of what happened to generate that score. But then.
shouldn't
2 details about those when you are actually working with your agents? Right
then it's more like you are tracing and evaluating your evaluators rather than your agents.
But yeah, understandable still, some details. You might be interested in.
Sujay Solomon 00:36:27 Do do span links make sense here at all.
anksing 00:36:33 Yeah, yeah, definitely.
Sujay Solomon 00:36:35 Okay.
Liudmila Molkova 00:36:35 Go ahead!
anksing 00:36:36 Oh, sorry. Please go ahead.
Liudmila Molkova 00:36:40 If we do it as spans, then we would need to decide. If the span is a child of Jenny I span
that we are that contains the actual work being evaluated, or and it it is linked to the context in which evaluator started doing the evaluation.
Or it's the opposite. And the Spanish child of the context evalator had.
And then it's linked to the Gen. AI.
Sujay Solomon 00:37:07 Yeah. But if it's a child, though that's a causal relationship, I don't. I don't. This one. This is, if it's asynchronous, it's likely it could even happen like hours after the execution has has completed. Typically, like
we've, we've told customers to like move away from creating like parent child relationships in those cases, and rather lean more into span links. I don't know if
hotel has a point of view on that typically.
Liudmila Molkova 00:37:41 What what happens. And we are running out of time, I think. Let's spend 3 more minutes and on this topic, and then move on. So what happens when you
have a link?
Let's say you have a link to span, and it represents the whole evaluation infra. You would see the trace about your geni operation
plus, you would see all the internals of the elevator.
and if if it's a child of the span being evaluated itself.
then it's contained. You can say, Okay, don't show me this link. Maybe
the link to evaluator infrastructure. So it's complicated. I think.
Okay, boy.
need to figure out how to do this. And it's it's not some immediate decision we can make right now.
Sujay Solomon 00:38:38 Sounds good.
Liudmila Molkova 00:38:44 Any last thoughts on this one
sounds like there is interest in evaluations. Everybody's doing it. Nobody is willing to share how or some some are
okay.
So then, let's move on to hopefully
resolve the remaining portions on the inputs and outputs.
so one thing I wanted to mention one of the things that we were blocked on this check.
I am going to send a Pr that relaxes this check and allows extended at complex attributes on Spence. We briefly discussed it with semantic conventions group, and I haven't heard any objections.
So we have a high chance of this check getting
green sometime soon. Oh, Aaron, you approved. Thanks.
And I think there are still a few open discussions.
and I wanted to get the rule
it doesn't show me open comments.
Okay, let's move from bottom to top.
The system instructions is a weird one.
So for others, the context is that we have instructions that are part of the chat history
and instructions that are not part of the chat history.
So, for example, when you send a news responses. Api, or you create an agent. You can provide instructions.
They are not structured or they have arbitrary structure, are.
And Erin, if I understand correctly, you're suggesting to support either 4.
Aaron Abbott 00:40:53 Yeah, I just I just don't like any, you know.
I feel like it's a little hard. And
so I'm kind of have 2 proposals here. Oh, actually responded to so yeah, one of them. And I don't know if this is feasible with the current semantic convention tooling, but would be like string or union of chat. Message.
because those seem to be the 2, the 2 possible things that we can't kind of decide
but like any would would leave it open to like, you know, int or double or
random structured thing. So if we could lock it down a little more, I think it would be good. And then the other possible thing is like, Oh, Alex, I see you left a comment to a chat message or a list of chat message, and then for Openai. When it uses a flat string it would just kind of wrap the object in the chat message.
Liudmila Molkova 00:41:46 Yeah on this one. So
the reason I didn't do it and let's talk through it.
if we look into the model.
So if you provide system instructions as a part of chat history.
it would be in site input messages.
So this is the text content or text part.
And it's super weird. Because, let's say, when use responses. Api, you have 2 places for the chat history.
Sorry. 2 places for system instructions.
Scroll down and find it.
Aaron Abbott 00:42:41 Yeah, I saw that, too.
Liudmila Molkova 00:42:47 So alright.
So there is a the instruction here.
There is input messages.
and you can have an arbitrary number of system messages inside your chat history. As far as I,
my experiments go open. A doesn't like it. It will either
ignore the rest. I don't remember exactly, but it's it's kind of wonky. It's not documented what they do. If you provide multiple system messages, especially if you provide them in different parts of your chat history. But you can certainly do this.
And my idea was, okay. The the data is weird.
We cannot change the data. So we need to find some
somewhat reasonable way to record it.
and the closer we are to reality the better. And it means that if it's a chat history, it goes to input.
It's not a chat history. If it's a separate property, it goes to attribute itself.
Aaron Abbott 00:44:04 Yep.
Alex Hall 00:44:06 I mean, Alan is talking about the type.
Aaron Abbott 00:44:09 Yeah, I think the main objection is, can it not be any.
Liudmila Molkova 00:44:14 So if we
Alex Hall 00:44:16 A list of message parts is, is, is quite close to any in the sense that it can still represent pretty much anything, but
in a better defined way.
Liudmila Molkova 00:44:29 The thing is, it wouldn't have a role, the role or the message part. Right? So what do we have in the message part.
So it's export type. Oh, I see.
Oh, okay.
we wouldn't have. We would never have something like this there.
So essentially, you're saying it's a export. The list of text ports, at least, for now.
Alex Hall 00:45:03 If we, if if we, if we mentioned that the only thing it can contain is is text, then I don't think there's much point in going beyond string, but if we're saying it, it might be other things
that it might. The input might not, might might be more than just text.
then I think it makes more sense to go for a list of message parts rather than any.
Liudmila Molkova 00:45:24 We don't have a case for anything by by but string and string array. So maybe if we start with string and array of strings. We can always expand the Union right? It's not the breaking change to start supporting new types. If we need to.
Aaron Abbott 00:45:43 Yeah, I mean, that seems reasonable to me. I think we
Gemini has uses reuses the same content type. And
so there is like the the option of doing nesting. But I don't know if it's semantically valuable to capture that. So I think string or string array would work. But
yeah, that that or chat message. I'm fine with all 3 of those options.
Liudmila Molkova 00:46:08 Okay.
Aaron Abbott 00:46:21 Yeah. And also also in the context, like, I know, we removed from this Pr, but the remote references thing.
I wonder
if it's string. It leads to this kind of confusion. If if it should be like a Json string. So it's a valid Json document
versus just the raw string with the system. Message.
but that was my main thing was also like, if if the remote, when we get to the remote reference part, it's nice if we know the schema of the file beforehand.
Liudmila Molkova 00:46:53 Then it should be a text part or the the message part right.
because it contains the the discriminator.
Aaron Abbott 00:47:02 Yeah, it could be.
I mean, I think also, like Json or Json already, would be feasible, because just just something that you could finally pass to a Json parser right.
Liudmila Molkova 00:47:12 So the any is the Json or Json array right, drink.
Aaron Abbott 00:47:20 That's true. Yeah.
Alex Hall 00:47:23 But it would be a way of
message. Path, not just message, part.
Liudmila Molkova 00:47:29 Right?
Okay.
Alex Hall 00:47:38 Is there a reason to like? Have array of string in there as opposed to array of text parts.
right.
Liudmila Molkova 00:47:47 It's easier to aw, desserialize
and make sense of this data. If you know it's all text or message parts, because there is a discriminator.
You don't need to guess if it's a string.
don't need to check the type. You can ignore a known discriminator values.
So some structure versus absolutely anything.
Okay, I think.
one reasons I wanted to have any is that they wanted to postpone all the discussions. What we are going to have here. But it seems it's not the good reason we still have the discussions.
I'll
probably go ahead with some form of list of message parts. If you folks are fine with it, Aaron, what do you think.
Aaron Abbott 00:48:53 Yeah, that sounds great. And and like you said, like, we can expand the Union. But if you start with any.
then you can't go anywhere from there. So.
Liudmila Molkova 00:49:04 Okay, sounds good. Do we have anything else that's open? I think there was a
there was a discussion. I just wanted to bring your attention, and I'm not sure if there is anything controversial.
So Alex brought up a good point that we need to support arbitrary ports, and, according to my Jason scheme and definition, they were not allowed.
So I'm introducing this guy. It changes how the Json schema looks like. If you, if you know how to use pedantic. Better to
express what you want. Please tell me I I
I'm not sure if it's the perfect way, but it's the best they found.
Other thing I changed
is that I renamed the 2. Call part to 2 Po call, request part to match the response part
and the tool response part.
This is
the trickiest moment. Ankit. I see you, Andres, do you want to chime in right now, or is it something different?
Ankit 00:50:12 I can go at the end.
Liudmila Molkova 00:50:14 Okay, thank you.
So if we look at the tool correspond and examples
we now have an example of built in to call.
And let's do this.
Okay, so this is an example of a response
who is built into. So this is the final message, right?
And this is a a part.
That is a total response.
This is a bit wonky.
So we have this thing defined in the Json Schema, the response.
And it has a type.
This is not defined in the Jason schema. But we need some discriminator again.
This is the 2 call interpreter call, and there is a code code is technically not a response. It's some intermediary step
so I hey? Oh, that we will. And let's say it's a file search. There will be queries.
And we, the queries, are technically an input to the tool.
Alex Hall 00:51:48 Sorry. Isn't there a tool call part somewhere in this situation, like calling the code interpreter? And that's where you would provide the code.
Liudmila Molkova 00:51:59 Yes, they are squashed right. The 2 call, request and response are squashed into one thing.
Alex Hall 00:52:06 That says.
Liudmila Molkova 00:52:09 So you would rather capture it as 2 parts.
Alex Hall 00:52:15 I'm not, you're saying, because, like the information comes back that way.
like from the responses Api, or something.
Liudmila Molkova 00:52:25 It's a lot of org with somewhat unclear transformation.
So like, let's say, it's a code interpreter. Then this is a total correspondence. There will be a tool.
and to call what request and it will be, have the same id, and until we have the
but then there is no response per se.
It does not produce a response. It's essentially this is the response.
Alex Hall 00:53:19 And this seems to be adapted from the example I gave you in slack that had.
You put a sort of a response and output. It was like the thing that got printed
or returned, or whatever.
Liudmila Molkova 00:53:31 So this is the what I get from.
For the interpreter, it has no output. It might have.
Alex Hall 00:53:43 It might have.
If it doesn't, then I would say that that the
part is sort of empty, but
especially in the general case. You sort of expect
that there's a call and a response.
Ankit 00:54:00 Yeah, actually, I've seen, like, usually in some cases, I've seen the outputs available, and those usually refer to as like
files. And the log files like any kind of artifacts it produces, and also the log files of
code execution. That's what I've seen for code interference.
Liudmila Molkova 00:54:25 Yeah.
Hi, so what I hear is, we need to spend a little bit more time designing
how this looks like the current example is somewhat controversial.
One quick chat before we move on to the next topic.
Can we create an action item and do it as a follow up.
Aaron Abbott 00:54:55 So I
I thought that what we had was kind of what Alex was describing. So I'll take another look at the Pr.
I guess I'm okay. Either way.
like the follow up would be before a release. I assume right.
Liudmila Molkova 00:55:11 E.
Well, you never know. So if we want it to be in the same release, then we would rather hold it back
and do it along with work.
I don't know. Once we have an agreement on the second Pr, we'll we'll merge this one.
Okay, we still have a couple of topics left. I'll try to make as much progress as I can. And, Aaron, if you can take a look.
let's try to close on this sooner, and
let's take a look. What else do we have lost our notes?
Avan, do you wanna go through any anything here.
Pavan 00:55:58 Oh, yeah. So
basically, we had proposed a slightly more complex Pr, initially. But we have sort of narrowed it down to like just, you know, helping.
at least, you know, add some new span attributes and a couple of metrics to the agentic ecosystem that we thought could be useful. And we basically have like full proof of concepts and like trace links for some of our recommendations which we would be happy to sort of talk through that. But initially, what we found out was that in the Llm. Spans
the log probability for each output token was sort of missing, which is being used heavily by Openai and Azure Openai models in general. So, and we sort of use that in some of our applications as well. So we were wondering if
you know if that could be sort of an optional field, where, if they specify this value to be true, then the log probability would be sort of emitted by the would be returned by the model. So
this was one of one of those
spans. The the other one that we basically did was the agentic role. So typically within like a workflow context, an agent would have some specific function or responsibility. So what we were thinking was that the agentic framework or the SDK that the developer will use? Would either, you know, through an annotation approach, or
through some other means, would have that as an optional parameter that the user could set just to specify. You know what role this agent was would play and it would typically help to sort of categorize like use, resource usages, latency patterns.
error rates, you know, like, so on and so forth. So we thought that, having that explicitly mentioned in the invoke agent span like for the agent, dot role would also be useful. So our sort of proposal was around that these 2 different span attributes. There were like couple of other metrics as well, which
you know, happy to sort of take some feedback. But in in general, you know, we wanted to sort of ensure that, you know, within a react pattern, let's say, depending on how the developer would set up their agent system. And each agent would have like multiple turns looping and things like that which
the atomic, you know, operation dot duration wouldn't necessarily capture. In a in a let's say session context. So we wanted to see if for the entire task completion
the end to end completion, duration would accurately capture, like how exactly within a given prompt what was the actual duration of that particular agent from from the task initialization to the task completion? Which could involve multiple operations.
So one of one of that metric recommendation was that.
And yeah, the active underscore agents just to sort of capture. How many agents are act, you know, currently being active in the system, and that was like sort of trying to take some inspiration from the existing like different areas in open elementary that already has, like, you know, some
means of capturing, like how many different connections are active, whether be it a database or like, you know, a message, queue, so on and so forth. So we feel that, given that there has been like a lot of discussions just in general from evolving from a single agent system to like a multi platform.
These initial proposals could be sort of useful, but not just in multi agent context, but in a single agent context as well.
so happy to get any feedback and thoughts on the team.
Liudmila Molkova 01:00:34 So one thing we we are almost out of time. One thing I want to call out, we actually a lot of questions I have are related to the implementation details. And could you please provide links to the prototypes? And
it would help answer them. And maybe we should answer some of these questions, and how is it collected? When would you actually record
that agent becomes active, and so on in the conventions themselves?
Pavan 01:01:07 Of course I'll do that. Thank you.
Liudmila Molkova 01:01:10 Thank you. I'm sorry we didn't. We don't have a time for the last
poor request. Is it the call for review, or is there any active discussions we need to have on this key.
Keith Decker 01:01:25 I think I was bringing it here to resolve the namespace conflict between trace loops. Vva client and open telemetry.
not sure if this right place for that, or or what's going on here.
Liudmila Molkova 01:01:39 Have you got any response from key from you?
Keith Decker 01:01:42 Yeah. New said, yes. So
I I yeah, I'm not sure where to go from. Here.
Liudmila Molkova 01:01:49 So I think they need to share the ownership. I'm sorry we we are out of time.
Keith Decker 01:01:56 Okay.
Liudmila Molkova 01:01:56 But I'll check if if they did, you know. Do you know, if they've actually shared, the ownership is open to monetary.
Keith Decker 01:02:03 Don't know.
Aaron Abbott 01:02:03 Not not yet. Keith, you can ping me on slack. Since you have slack, we can try.
Keith Decker 01:02:07 Okay. Sounds good.
Aaron Abbott 01:02:09 Okay.
Liudmila Molkova 01:02:10 Be wonderful. Thanks a lot. Everyone
have a great rest of your week and see you around.
Aaron Abbott 01:02:16 Thank you. Everyone.
Pavan 01:02:17 Bye, everyone.
