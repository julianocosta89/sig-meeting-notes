SIG: LLM Semantic Convention WG
Date: 2025-08-05
Duration: 63 minutes
============================================================

## Zoom Recording Transcript

Aaron Abbott 00:04:57 Everyone. How's it going.
Samuel Colvin (Pydantic) 00:05:01 Hi! There!
Aaron Abbott 00:05:19 Okay.
looks like windmill is gonna be a bit late. So I guess we can get started.
Alright.
Alright. So, looking at the triage board.
I think. Yeah, I think Alex filed these as follow-ups to the 2179 Pr message prototypes. Okay, that makes sense.
And then this one built in server side tool calls.
Yeah, I imagine we could probably discuss these after after that. Pr is merged or they're pretty much just follow ups.
I don't know.
Alex Hall 00:06:42 Well, I specifically opened these now because I wanted to not wait for the Pr. To be merged.
Aaron Abbott 00:06:48 Okay.
Alex Hall 00:06:50 You don't have to block the VR.
Aaron Abbott 00:06:51 Yeah, yeah. Did you add them to the to the agenda?
Alex Hall 00:06:56 No.
Aaron Abbott 00:06:58 Yeah, we could. Yeah, we could just discuss them with 2179, maybe.
See?
Alex Hall 00:07:06 I mean the the server side talk was especially meaningful. I think we 1st need to continue the discussion in 2179, because I told that she should change the example. And now I'm realizing maybe she had a good point. But things are very unclear. Actually okay.
Aaron Abbott 00:07:26 Okay. Cool.
Alex Hall 00:07:27 We have a lot of complication coming from the fact that we're trying to take into account like multiple choices or candidates. And I don't even know if that gets used in practice. But what? Why, I think it does get users. It's very annoying to to take them into account when I feel like it's probably quite rare.
Aaron Abbott 00:07:46 No, okay. Alright. Let me just add it to the under the 2179 discussion.
Alex Hall 00:08:00 What is buggynizer.
Aaron Abbott 00:08:03 Where'd you see that.
Alex Hall 00:08:05 On your one's gone. Is that an extension.
Aaron Abbott 00:08:09 Oh, yeah, it's an extension for Google.
Yeah.
And then the other one was this one, okay?
Alright, yeah. I stuck him in the meeting notes. I think hopefully, hopefully, we can wait till the mill gets here.
Alright! Those are the only 2 new ones looking at to do.
There's a bunch. Yeah, I guess I'll just say, like, I think we've had 2 prs, I think it's from folks from Cisco spunk so we had one for go here, actually, these are the python contribut. So making some progress there. And we're going to do the same versioning thing that we did for the vertex AI instrumentation to kind of share the the packages with open elementary. So okay, did anybody else wanna share anything from this board? Or should we move on to the agenda.
Cool? On, Kit you're on.
I don't think so. Okay, alright, let's come back to that one.
Okay, Samuel, you wanna talk about this one?
Oh, you're muted.
Samuel Colvin (Pydantic) 00:10:05 Apologies. If you could go down to my comment under under Alex's at the bottom of this issue.
Yes, so so basically.
this is not that it has to match this, but this is the having I've gone through. As Alex points out just now. I haven't done images, but I've gone through 15 or so different inference providers and looked at what they return. And basically everyone's response covered is covered by this except for perplexity, who have, like number of requests. But since this only applies for one.
this this allows you to calculate the price of at least reasonably, but for all inference, providers. Sure they have stuff that they don't return like how long they've stored an image for or like, how many like searches they've done. But basically, I would propose that we extend what we currently have, which is input tokens and output tokens to include these.
Alex says this came up in another meeting, which I'm sorry I wasn't wasn't here for so it sounds like the result of that was, okay. Go ahead and propose a propose a change. So maybe this doesn't need to be discussed. But if there is anyone here who has any any thoughts on it would love to hear.
Aaron Abbott 00:11:23 Cool. That's awesome. Thank you for going through all the all the different providers. It's really helpful.
Is this blocked on 2, 1, 7, 9, or this would just be attributes right.
Samuel Colvin (Pydantic) 00:11:36 I understand that this is not blocked.
Alex. You were here for a previous call, so I don't know what they said.
Alex Hall 00:11:41 I mean, basically, I. I created this issue and I brought it up many meetings ago. I can't remember when.
No, it's it's not related to 1, 7, 9, I will say, what one complication I'm thinking of is that ideally, when you add up right? Okay for span attributes. I think this is fairly straightforward, but we would also want to follow a similar pattern for metrics and for metrics. I don't actually know how it would look, because ideally. When you just add up all the values of a metric, and for all the different attribute combinations, you get something meaningful right? And that's going to be complicated if you have, like one metric data point, which is just all the input tokens and another one, which is some subset of that for the cached input tokens.
Samuel Colvin (Pydantic) 00:12:30 Don't think that's the problem. I think the main problem is that Gemini charges more over a certain number of tokens. And so it's like. As far as I know, they're the only model where, like pricing is not linear. But the point is once pricing is not linear. Pricing is not linear, and I'm sure someone else will follow suit with something else.
Alex Hall 00:12:47 I mean, I'll just say it's actually, it's amazing that pricing is usually linear, because the actual computational cost is quadratic.
Aaron Abbott 00:12:55 Yeah.
Samuel Colvin (Pydantic) 00:12:59 But.
Alex Hall 00:12:59 But yeah, I think that for that case you'd have to have something like an attribute on the metric like, was this over 200 k. Or not, or something, but it feels like to do the metrics properly. You might have to have.
You might have to like cache, calculate the the number of uncached input tokens or something to get accurate.
I mean.
Samuel Colvin (Pydantic) 00:13:26 Maybe I'm being dumb here. But, like the point is that this this one, this I mean. There are also reasoning tokens which, for example, Openai return, which may be of interest to someone, but at least until now do not contribute directly to prices. I'm not saying this.
Alex Hall 00:13:41 They contribute, but they're not different.
Samuel Colvin (Pydantic) 00:13:44 Yeah. But as in, I don't think you need to use that number when calculating the price.
Alex Hall 00:13:49 Right? So so maybe the what we should do is is focus purely on span attributes.
because it might be easier to think about the metrics, and also focus on the ones listed here for the sake of what affects pricing.
Samuel Colvin (Pydantic) 00:14:04 I mean, I suppose the the 1st question is, should we create a Pr to like?
Add these to the semantic conventions wait for a more complete set.
Alex Hall 00:14:22 We've already waited, and we should just make the proposal.
Samuel Colvin (Pydantic) 00:14:25 Anyone else have any thoughts on that.
Aaron Abbott 00:14:30 Yeah, I mean, I I think this makes sense to me. I I would I would dig through them a little like, yeah, it definitely seems more complicated for metrics, because it's like input input, total, I guess. And then input audio, etc. So yeah, I I think sending a Pr. Sounds good to me.
Samuel Colvin (Pydantic) 00:14:48 Let's okay.
I think we should have a couple of weeks, and we should check that. Our prices are working properly for them, because it seems unfortunate if the main complexity is cash, read and cash. Write, which I have the the distinction to cover anthropic which splits them. But I need to check that we have all the right logic for for which which one all of the other models just talk about caching. And I, yeah. And then the other thing that's missing, that so that might be wrong. But everything else is the other. The other missing. Other things are just like purely missing, as in these. These are right, there might be more. But okay, I think I'll I'll take away that I or it might be we. But probably I will try to add a Pr. To create a Pr. To propose these additions to semantic conventions, but it's probably a few weeks off.
Aaron Abbott 00:15:39 Okay, yeah, that makes sense.
Sergey Sergeev 00:15:42 I have one question about it. So basically, this is trying to estimate prices on the client side. Not that the prices or token. Usage is coming from the server side, so do we need to separate between what we get from the response. If provider any provider returns token usage. I think we can have it as a server usage.
It's a very reported usage. And here we basically guess on the coin side, right.
Samuel Colvin (Pydantic) 00:16:22 So this the point is, we should be able to populate this in this case data class. But we have the same thing in Javascript entirely from the responses we get from the model to the point is, you make a request. It returns some mixture of different attributes which we think should map to one of these fields.
and from this you can. Then we then have what we do have existing in our repo. Is the logic. To then go from a usage object to a cost in dollars.
As I say, that won't cover every single thing, because things like web searches have a cost, but they're not included in the response, or, like some models, charge per like hour of caching, which isn't included in the response. So we have. No, and it's not per request, so we can't add that. But the point is, this covers all of the this is everything you need to make the most accurate guess at how much that request cost you, based on the response.
Sergey Sergeev 00:17:22 Yeah, okay, thanks. I miss that. It's coming from from the response. So the usage comes from response. And you example it. It. We have some table, and if customers have their own price negotiated with providers again, basically use different values. Yeah.
Samuel Colvin (Pydantic) 00:17:43 Well, not only that, but in our. So we have. We, in addition, are going to record in logfire. There may be a world where that becomes a semantic convention in time, a price field or a cost field. I think we're going to call it logfire cost initially, which is by default. We calculate it using this library. But in theory you can fill in, put that in using your own calculation of whatever else you're pricing. And then there is an open question of whether that should be like genai cost or whether that should be operation dot cost. And you could use it for like a request to Google Maps or something else, if you really wanted. That's a whole nother debate. The 1st thing to do is to get these attributes added to at the moment. I think it's genai dot input tokens extended to cover these ones.
Sergey Sergeev 00:18:28 Thank you for providing this background. I will review it as well.
Samuel Colvin (Pydantic) 00:18:32 Thank you.
Aaron Abbott 00:18:34 Okay. So I think I see what you're saying now. So like, be based on this for a single span, even for like nonlinear pricing like Gemini. You could figure out the cost because you have it split up. But if you did metrics and you aggregated them, it would be impossible to tell, because it's per request right?
Samuel Colvin (Pydantic) 00:18:51 Yep.
Alex Hall 00:18:52 Okay, I got you. Yeah.
Have to include info, like, you know, request that had more than 200 k tokens or something.
Samuel Colvin (Pydantic) 00:19:03 Yeah, you'd have to do something like you'd have to have a different number for number of input tokens above 200 K, and that would then get complicated. But the point is that this, that library that we link to that has all of the logic for going from this usage object to a number in dollars.
Alex Hall 00:19:19 One request.
Samuel Colvin (Pydantic) 00:19:20 For one request.
Aaron Abbott 00:19:23 Okay, cool. Yeah. I think the only I don't think it's blocked on 2179. But we are adding, like all the attributes to to both like the logs and the the spends. But I think it's fine, because it's a shared thing like in the in the Ml, file, I think we call it registry or something like that. So.
okay.
Samuel Colvin (Pydantic) 00:19:44 Well, it'll be a few weeks before I create the Pr. Anyway. Probably so maybe things will have settled.
Aaron Abbott 00:19:50 Okay, awesome.
Make a comment on it.
Yeah.
Anything else on this one.
Samuel Colvin (Pydantic) 00:19:59 No.
Aaron Abbott 00:20:00 No, okay. Ankit. Are you around now?
anksing 00:20:06 Yes, hey? Sorry. I was a bit late.
Aaron Abbott 00:20:10 Oh, no! Worries do you want to talk about about this agenda type? Topic?
anksing 00:20:16 Yeah, certainly, thank you.
so I think it would be nice if you could open one of the document called Journey spans.md. Which shows, like the nice.
Aaron Abbott 00:20:29 Do you want to share.
anksing 00:20:30 Oh, sure I can share.
Aaron Abbott 00:20:32 Yeah.
anksing 00:20:45 Okay, so this is is my chrome or edge window visible.
Aaron Abbott 00:21:01 Yeah, I think I could see the whole screen. But I I'm seeing the Doc right now.
anksing 00:21:06 Oh, I see! Let me like. Do you see some other screens as well.
Aaron Abbott 00:21:12 No, no, I just see Jenny spins dot.
anksing 00:21:14 Okay, awesome. That's good.
Okay? So I think we had some great discussion and feedback around like how we should capture the evaluation results in the last meeting, and one of the major feedback that came out of it was should we have it as a span versus event.
and I think there was a pretty good consensus on it should be a spam, because it's more flexible to capture more information than an event.
So I've updated the Pr to reflect that. And then we had internal discussion as well. And then finally.
after discussing more and looking at both the options. It's definitely felt like span is a better option. And then we can link the evaluation spans like to the to the actual stand which it evaluates and shows the scores for.
So that's a major change that I've done in the Pr. And then I have a I've also added, like a small Poc code, I've linked it in the Pr to show on how you could link that using. Add link like Apis.
so I can go over like all these attributes.
So the 1st attribute is any evaluation name. This is a name that user gives to the evaluation, and it makes more sense to them. The operation name supposed to be evaluation, and then the span name should be evaluation. And whatever evaluation you're doing so. This is following the semantic or the conventions that we have for other spans right now.
Error type in case there's an error, it's captured by this attribute.
and then I have evaluation, label, and a score as well. So evaluation label is more for a purpose of like something which you can easily make sense of when you're reading this evaluation. Scores like relevant or something is not relevant, incorrect pass fail.
and then score could be more like. If you have evaluators where you give in a like. It's like a scale kind of score. And then, if you want to have a label, pass and fail based on your thresholds. You could easily use these 2 attributes to do it.
And the.
Alex Hall 00:23:33 Wait!
anksing 00:23:33 This one.
Alex Hall 00:23:34 Can you just clarify? Maybe you said this and I missed it. What what does the span represent? Is it evaluating a single like Lm. Completion or single performing some tasks that.
anksing 00:23:52 So So this span represents an evaluation score for a span, and you could apply it to possibly any spam you would whether it's a chat completion span, whether it's a tool in work span or whether it's a agent inbox pilot, you are like.
Alex Hall 00:24:09 Yeah, so.
anksing 00:24:10 As a user, calculate the score and then link the evaluations.
Alex Hall 00:24:14 So it's so it's like a low, level, single atomic thing, as in, you know, you're evaluating one thing. This doesn't contain multiple cases, or whatever.
anksing 00:24:29 When you say about like multiple cases whatever like could you help me like with.
Alex Hall 00:24:35 As well. The point is that this is not multiple cases, or whatever this is, you know you're looking at one thing like, you know one request made by an Lm. And you're evaluating that one thing.
and then.
But also is this, this is an evaluation performed by another event.
Some automated process.
anksing 00:25:03 Or yeah or it doesn't have to be Llm. As a judge or evaluation performed by an Llm. But it could be even something like a mathematical calculations like you would do for like FM. Score. If you want to do a rouge score.
Alex Hall 00:25:19 Well, okay. So the last time when when I was saying it was a span is because I was thinking of this in in the way that we do evals and pydantic evals, which is always, you know, there's some some kind of automated process performing the evaluation. It's it's not something where a human looks at it and clicks a button, saying Yes or no?
So is this also. Not something like a human has just given a score that there's there's like a clearly defined process here.
So it's clear what the start and the end would be, and it might be spans inside.
anksing 00:25:57 Yeah, yeah, they can be spans inside, definitely. So this is gonna be a span like, within which you would probably have more child spans. Which shows you how this score was calculated. Right but then, at this evaluation span level, you have a score which you can look at as a user right? And at this point, like, at least, my intention is not to use this, for, like human annotations, kind of a task where user goes and gives a score. But this is more, for you have your Evals, you generate scores or matrix for them, and then you record them along with your traces along with the spans.
I like you, man.
Alex Hall 00:26:41 And technically, you could use these things for things that have no relation to Gen. AI like you. You said it doesn't have to use the evaluation might not be performed using AI, and you're also not necessarily evaluating something that used AI. In the 1st place, although I guess that's the most common use case.
anksing 00:27:03 That's a that's a definitely that's a that's a good question. But then for this Pr, I'm scoping it only for Jenny, because I don't have much context on whether, if I want to apply this to semantic conventions in general, how would like what all things I need to consider so, for now I definitely wanted. My intention is to just scope it for genie. But if this can be applied to a more broader group, I would prefer to go in the direction of let's apply it for genie, and then, if it's applicable for any broader semantic conventions, then we can think of it.
Samuel Colvin (Pydantic) 00:27:38 I agree that it makes sense to scope it to Gen. AI, and if it becomes more generally used, that's a separate thing. My question is kind of on Alex's 1st point. Like.
as I understand it, I mean, I can show you an example from our system. But I mean I was speaking to Pamela Fox from Microsoft, who is like, seems to be one of the experts on emails who was saying that, like you very often have, there were like 4 or 5 different, like groundedness. I forget what the other ones are all called, but like there are loads of different scores you often want to apply. And this mess I'm missing. Something has one.
anksing 00:28:12 School.
Samuel Colvin (Pydantic) 00:28:13 Is the idea that you have multiple different spans for each thing you measure or.
anksing 00:28:18 Yes, that's right.
Samuel Colvin (Pydantic) 00:28:21 Okay, isn't that gonna is that gonna be weird, like as in it's going to make your trace look weird. If you have multiple different spans for each score.
anksing 00:28:37 Oh, okay.
Samuel Colvin (Pydantic) 00:28:37 And each other? Or are they like.
anksing 00:28:41 Oh, okay, so let me actually pull this down. If this helps like one small kind of thing. So I'll just quickly go through this so that it kind of conveys the idea.
So, for example, like, I have this very naive chat completion call, and I'm using instrumental for from open telemetry, one of the contribut extensions called Openai, v. 2.
Once I run this, it generates a trace, and then the way I want to do or attach valuations to this plan is.
I get the trace. Id, I get the span id, and then this is a span where I'm doing my evaluation. So I'm not really doing anything right now. But then assuming there's something happening here, and which gives me a score. So I then use the span which I created earlier, or chat completion. Link it.
yeah, and then add the scores.
So this span is not directly like as a child span of the chat completion, but more like a length span, which gives me the score, and I can look at like this span within the span. You could do like many different things just to get to a score right, and it could be captured by a series of spans or however complex you want to be, but then finally the score, and then you add it as an attribute.
Samuel Colvin (Pydantic) 00:30:13 That makes sense. I think, the biggest issue for us, and if we're alone in this, then fine, because we'll have to fix it at some point, but it's worth checking like we find it hard to. We don't have a currently have a system to backlink from from a span to the spans that link to it as in. Then you need, like an index, both directions, basically. And so it is fundamentally to get all the link spans that might link. You have to like.
scan all time for spans that have this link.
and I don't know what other observability platforms, how well they do like this kind of link.
if like, like, I said, if we're the only ones who don't have that backlink functionality built in, then obviously, we're in the minority. But yeah, I think it's worth checking that, because otherwise very hard to build. This view.
anksing 00:31:00 I see. So actually, this one will expand or add links, or I think there was a way to also add links right here.
that's something that's available in open telemetry. I was reading about it. So I'm hoping this is just more like limitation of the back end which implements us or.
Samuel Colvin (Pydantic) 00:31:18 But I mean well, other people here might know more, but my understanding is pan links are not like that widely used. And then well, anyone who knows better than this like, please apologies if I'm saying something that is not correct. But my understanding is the obvious use of span links is for let's say you kick off a job from within a task. And now I'm like what things started this job. Oh, it's obvious. I've got the link to the span that created it. So I can go from the job back to the context which started it.
I don't know whether or not it is obviously, would you be useful from a given span to say how many different jobs did this start?
But I just don't know how many systems actually have that.
and I think it before we use span links for this. I think it should be. It would be fair to ask, like, I say, we're a minnow in this world, but like of the big hotel platforms, how many of them have backlinking for for span links.
anksing 00:32:10 I see. Okay.
Okay, yeah. Please go.
Aaron Abbott 00:32:15 Yeah.
anksing 00:32:15 Yeah, sorry. I don't see.
Aaron Abbott 00:32:17 I see Audrey.
anksing 00:32:19 Yeah.
Aaron Abbott 00:32:19 I was gonna respond to that, and then I'll I'll let go if that's all right. So so like Sam, I I hear the concern.
To me this does seem exactly like the use case you described, like.
there's an Async job getting kicked off, and we're kind of linking linking back to the spin.
I mean, I don't know if if the client or the agent necessarily kicks it off, but this feels this feels like links to me.
Samuel Colvin (Pydantic) 00:32:45 Yep.
Aaron Abbott 00:32:46 Yeah.
Samuel Colvin (Pydantic) 00:32:47 Actually considered using this for feedback, and we didn't, because it was more work for us to do. But I thought at the time it was mostly because it would have involved us doing this backlinking thing we didn't want to do yet, but I agree it looks it might be a good way of forcing my team to go and implement backlinks.
Aaron Abbott 00:33:06 Okay.
Sergey Sergeev 00:33:07 Yeah. My, my question was about, why can't we use just child span?
It will be a wait arriving span, because most probably it will take tens up to 10 seconds to evaluate using our message edge.
I'm wondering if we can just send a follow up span, which is a child span of that original request response.
And what are the problems with it?
So the.
anksing 00:33:42 Okay, I.
Aaron Abbott 00:33:44 Yeah, I I agree with what you said in chat like it not just the in process instrumentation case. But there might be like an asynchronous job, or something like that.
Sergey Sergeev 00:33:56 Oh, so some some buttons will just spend or.
Samuel Colvin (Pydantic) 00:34:02 And you run your evals 6 weeks later. And this is one of the cases you run it on.
Sergey Sergeev 00:34:07 Got it.
Samuel Colvin (Pydantic) 00:34:08 That is conceptually wrong.
Liudmila Molkova 00:34:13 Sorry I'm late for this discussion.
Why not, child? Span? Because you have 2 contexts. The evaluation happens in one context.
and you need to say that it's related to something to the context in which genie response has happened. Right?
So you inevitably have 2 contexts. You cannot just use parental relationships back to the backlinking problem.
You know what? We have few links in other places and up on telemetry in messaging in connection stuff and backlinks. Yeah, it sucks, implement, it sucks.
but you cannot support upon telemetry fully without supporting back.
Samuel Colvin (Pydantic) 00:35:07 Yep, I think that's a fair answer.
anksing 00:35:12 You.
Sergey Sergeev 00:35:13 Yeah, but one more question about spans with events.
So I believe right now, we support customer data. Request responses in 2 flavors. One is span attributes, and second is basically advance or logs.
Do we need to support 2, 4 h of evaluations? And as events for spend or evaluation spans if we want to support both flavors of telemetry.
So basically, if you send request responses to events, probably it makes sense to send evaluation scores as events as well.
What that shit.
anksing 00:36:06 That's a that's a good question, and I think it came up in the last meeting as well. I think the 1st proposal had, like evaluations, courses, events.
I think, one of the feedback was, events won't fully capture on like information about like how you got to this evaluation score, and that was the reason.
We do that to use spans and link them so that you have the scores, and you could also see how you got to that score.
Sergey Sergeev 00:36:37 So we don't have a way to link an event or log to spend. Okay? So.
anksing 00:36:46 Oh, yeah, you can add an event to the span like that's not a problem. But then I think the reason was if you just have an event, you would not know how you got to the score. If you want to like, trace your values as well right.
If you have an Llm. As a judge, or if you have a workflow which calculates the score.
how that did that workflow come up with that score like what steps it took.
Sergey Sergeev 00:37:13 Yeah.
anksing 00:37:15 That was the reason we pivoted to using spans, and Linkina.
Sergey Sergeev 00:37:21 Yeah, I'll probably ask offhand to better understand it.
Liudmila Molkova 00:37:26 Would it make sense to phase it?
So we kinda feel it.
The span makes sense, right?
Maybe an event makes sense as well.
Can we define a span which we know for sure, that makes sense, and also maybe later on, define an event. But we don't need to boil the ocean and decide everything right now.
anksing 00:38:01 I'm definitely open to it, like, if that option comes back like of having event as well. Maybe we can take it as like a follow up for this spiel, would that be okay?
That makes sense.
Aaron Abbott 00:38:19 Yeah. Sounds good to me.
anksing 00:38:24 Okay, so with that, let me go back quickly, and I can cover like remaining attributes.
So I think we covered label Score model port. I think they're coming from the common one. Reasoning. I think this becomes important for Llm. As a judge, and it's optional, obviously.
And then I have some fields for metadata input output and just metadata. So these are just kind of capturing submitted about inputs outputs and also like for the evaluation as a whole.
And then there are some usage which are existing attributes input token, output tokens which are obviously optional.
so any comments on any of these attributes, and I think I have the link to the Pr as well.
Oh, yeah, I see 2 hands up, Sam and Emila.
Samuel Colvin (Pydantic) 00:39:25 Lube mellow. I think you were first.st
Liudmila Molkova 00:39:29 I'm not sure. So if you want to go first, st go first.st
Samuel Colvin (Pydantic) 00:39:33 Okay, I was talking again. We were talking about cases where you run a single Llm. As a judge, and it returns multiple scores as a structured output rather than running each like the different judges, as separate Llm. Calls. Would the plan be? Then you have 2 different.
anksing 00:39:51 And.
Samuel Colvin (Pydantic) 00:39:51 And then what wraps, what.
anksing 00:39:59 Interesting again.
So in one element, Judge, you're getting multiple scores, multiple metrics.
Samuel Colvin (Pydantic) 00:40:07 Because you can imagine it's basically the same duration. You ask it for a like groundedness score, a politeness, score a like whatever you know whatever it is, knowing this score whatever.
And now I want to attach all of them.
So we use events. Okay, yeah. I mean, that's a good argument for having events as well.
Sergey Sergeev 00:40:43 My 1st year.
Liudmila Molkova 00:40:45 So from from user experience, I mean who I, we can find a way to represent those multiple spans or events under multiple under one span from the user perspective. I would imagine the main use case for relations would be to build a dashboard and show a a metric and have a threshold and alert on this.
If we capture multiple of them in inside one span, it would be much harder to do, especially for this metric like use cases.
We can get away with it by saying, Okay, we will also report the metric.
But I feel like having one telemetry. Item, one measurement per one. Evaluation type is is useful from user experience.
But I agree that having a way to address this case is is important that we in some cases they'll have a batch thing.
Sergey Sergeev 00:42:02 Yeah, I see 2 use cases. First, st you are showing in the trace or conversation view that some of the conversations triggered some of the evaluations.
So let's say you have bias or correctness or politeness whatever. And second, you can monitor services. You can monitor. You can have medics with us evaluations. And then you can basically.
1st identify the problem with a service and then drill down to some particular conversations. So I think in haven't The server elevation, somehow connected to a trace and particular span, is important, but also aggregated. Metrics are important, too. So I think some providers will require spans, and some will require events in the end. I would propose to as optional, maybe a standardizing on spend attributes by default, but make it an event optional.
Aaron Abbott 00:43:22 I think we should probably move on and wrap up this discussion, but if anybody has, like closing thoughts, feel free to go ahead.
Liudmila Molkova 00:43:36 Sounds like the the response of the data model that we have that would address the needs would be the span to represent the process of running evaluations. How many evaluations are there inside?
And then there are child events that are that represent individual violation results having them sometimes spans and sometimes events we could make it work. But like for events, it's it's super clear how you filter them out. You search for specific event, name and word for specific. Well, 1st glance, it would be the specific attribute.
Anyway, that this this is a data model that could address it all.
anksing 00:44:39 Okay, so sounds like, we have a at least close to consensus on the data model. And then we can make a decision on span and spans. First, st events.
Discussion.
Okay, sounds good.
I see some. Thank you.
Aaron Abbott 00:45:03 Cool so we've got about 15 min. Should we go on to the next one?
Thank you.
Okay. There's Noah.
Actually, do you want to share.
Liudmila Molkova 00:45:26 You're already sharing. So if you could keep sharing and you'd have had some problems in the morning, I hope they are resolved. And we can actually see something.
Aaron Abbott 00:45:35 It seems to be worse.
Liudmila Molkova 00:45:37 But now you need to wait until we'll jump to the discussion.
Aaron Abbott 00:45:40 Yep.
Liudmila Molkova 00:45:40 Okay, there are a couple of open discussions that I hope we can close on this one. I feel it's not super important. But just because we are both Alex also here.
so we wanted. We want to make messages in the history extendable. So we should be able to add new type type parts and our Json schema should allow this.
So there are some mechanics of how to express it in the Json Schema and Aaron. Can you scroll down a little bit.
Alex Hall 00:46:27 I mean, I'll I'll say a little bit. I think it's fine to keep it simple.
If if the Json schema isn't actually able to catch like call kinds of mistakes.
That's okay. Because ultimately I don't think that we should be using the Json schema as like this strict, authoritative thing.
I think the more important thing is, you know, the description of what the attributes should look like.
So in any case, this more complicated thing is is essentially a tightening. We could start with the the looser thing which you know has the the simple approach of basically not trying to think about discriminators. And then, if for some reason we feel like we need a strict adjacent schema, we can try and do this later.
Liudmila Molkova 00:47:24 Okay, wonderful. So then let's resolve it, and we can always get back to it later, if you need to.
Aaron Abbott 00:47:36 Okay, go ahead.
Alright. This is the next one.
Liudmila Molkova 00:47:41 Yeah, this one is the more important one.
So we need a way to capture built in tool responses.
I think the the past discussions were that we probably need to discuss more of it. Oh, sorry, Anki, you had your hand raised. Do you wanna go and ask something.
anksing 00:48:02 Yeah. Sorry about the last comment. So like going from, say, a structure to unstructured is like less of a breaking change right? And going from unstructured to structure is a breaking change.
Liudmila Molkova 00:48:18 We are in experimental mode, I think we will inevitably have breaking changes, especially when it comes to tightening things down.
anksing 00:48:28 Okay.
Sounds good.
Liudmila Molkova 00:48:32 But it it's it's a great point that we should resolve all of this and tighten everything we need to before it becomes stable, so that we don't need to do it afterwards.
anksing 00:48:43 That makes sense.
Liudmila Molkova 00:48:50 I'll probably create an issue. And maybe a rule is the things that we want to get tightened so we don't forget it around stability time.
Okay, getting back to this one. So the built-in tools representation in the response messages.
I think we discussed that we will have more development around this, and probably we will need to specify the format for some popular tools.
And we need to have a schema that Has a common part, and H. 2.
Each built-in tool would have would align with it and have some custom properties. So this is the example that was rejected. Right? We don't want to represent to an assistant the built into an assistant. That's 2 separate messages. They aren't.
The the 2 parts will be inside the assistant message.
Alex Hall 00:50:08 That that is what I said initially, and I was having second thoughts which I put in the last comments today as.
Liudmila Molkova 00:50:18 So I feel like we just need to double check.
Alex Hall 00:50:22 Viewing it as multiple messages does match a lot more like the Openai Api shape.
whereas multiple parts matches the Gemini shape. I imagine that what we want is sort of one common vendor, agnostic shape, that, and and sacrifice realisticness, and the actual resemblance to to real Api requests in some cases.
hey? I think doing this with parts will make it like a bit confusing for someone looking at like the open AI requests and responses that we like.
These are messages, aren't they? Not parts?
Okay. Can you help me understand why, like in the example you you have.
Liudmila Molkova 00:51:13 I would say it's the opposite. The annotations are this thing, and they are under role assistant.
Alex Hall 00:51:20 Exactly th. This thing looks like like the whole block. There looks like a message rather than a part.
Liudmila Molkova 00:51:28 But it's both right. The annotations is the built-in tool stuff.
and the text is the actual output.
Samuel Colvin (Pydantic) 00:51:37 Alex, are you talking about chat or responses? The new.
Alex Hall 00:51:40 This is the responses. Api. So it'll return a list of things. This current code block is one item in that list.
And from the open AI perspective. It's a message.
But this means that Openai effectively returns a list of multiple messages which is a weird way of looking at it. But they literally say type message, and they give it a role. And it contains multiple parts potentially.
I don't actually know how you get multiple parts in here, but there's a new way of parts.
Liudmila Molkova 00:52:16 The the parts are the synonym of content here. Right? So it exactly matches the same structure.
Yeah.
Alex Hall 00:52:24 Yes, but but where? The the suggestion that I originally made, which I think you, you changed things to treats this whole message thing as one part.
which means that that content array. If it had multiple things, it would get like flattened out into into the into the higher level array.
which is not necessarily a problem. Actually, where it becomes more of a problem is where you take these output messages and you put them back into the input messages, and then the instrumentation has to reverse that. It has to sort of find out which.
Samuel Colvin (Pydantic) 00:52:59 Which of which of these input messages were generated and actually belong to a single request.
Alex Hall 00:53:07 Assistant Message.
Samuel Colvin (Pydantic) 00:53:08 We may care about that in Pydantic AI, but like hotel doesn't care about reconstructing an Openai request from the observability data just about having a consistent format for the messages which can then be, you know, rendered in observability platforms. Unless I'm.
Alex Hall 00:53:24 I think that we want, like the Gen. AI input messages and Gen. AI output messages, attributes be sort of analogous to you should be able to like. Guess what one would look like based on the other. If the shape changes between the 2 of them.
That's confusing.
Liudmila Molkova 00:53:43 But you are not even supposed to take, built in or outputs and put them back in the chat. History.
Alex Hall 00:53:52 You absolutely can.
In general, you you just take, you know, response output. You add it to the messages you add, like the next user message or whatever. And you just repeat the cycle. You don't. You don't even check what? What exactly, was in there as you're extending? Necessarily, you just.
And I. I tried this, and it just works like these.
I mean, right now, I think we're looking at hotel hypothetical parts. But if you scroll up, I think, to what I where I 1st posted the code code example, and I gave a bunch of open AI things.
Aaron Abbott 00:54:32 No one Alex. Right here.
Alex Hall 00:54:36 The screen sharing is clagging quite a lot for me. No. So we're looking for something that looks like it. It comes from the the open AI Api itself not not meant to be a hotel.
Aaron Abbott 00:54:48 Was it this one.
Alex Hall 00:54:55 So.
Aaron Abbott 00:54:57 So Openai returns this.
Alex Hall 00:55:01 And I was saying that each of these items should be a part.
And now I'm worried that in a sense they work quite well, actually, as a message, because you can take this list of things and put it into the input messages like you wouldn't put all of these as parts of a single message.
So these would live at the same level as like a user message.
No.
I think that's overall. Okay, but it does mean that if if we wanted instrumentation to know that these are parts of a single message, it has to be able to look at the list of messages and see which things are meant to be grouped together.
Aaron Abbott 00:55:46 I see.
anksing 00:55:48 And I just wanted to add, like another angle to it, say, for example, you have built in function like, user defined function tools right? The way that behaves is assistance. Make a assistant message in which it does a tool call right?
And I'm hoping like behind the service like Openai does a very similar thing where it figures out it has to call code interpreter, and it makes a assistant message which tells it.
go call code interpreter and comes back right.
However, that's not exposed to the user. Right? Say, for example, if the telemetry was available on the service side, would we see that kind of structure for messages like right now, the response that we see I'm guessing all of those information is combined into one response and shown to the user like for a local function tool like you would see an assistant calling a tool, and that there's a message for it. And then there is a tool call right and output console.
So that's another aspect like to look on how we can kind of represent these things in hotel, just thinking out loud.
Aaron Abbott 00:57:04 I mean Alex, also, is it a a big deal? If the output from the previous call looks different from the input in the next one, like the whole thing is, is stateless, so you don't need to look back at the previous output right.
Alex Hall 00:57:25 I do think it's confusing if like.
if Gen. AI output dot messages has a different shape from messages, if you like, take, you know if Jenni output dot messages is is just one message, and it has all of these parts.
I expect to then find that same one message. When I look at it. In general, I input the messages. But I okay, I see your point about it's stateless. It's like, why do I need to chain these together.
I think it's just. It's a matter of is it intuitive? Does it work the way people expect? Will will they be able to easily get queries right?
Liudmila Molkova 00:58:12 My take on this is that we are it. We're trying to put built in tools into the same structure as we use for functions, and they just don't fit.
Alex Hall 00:58:30 No, but I think that if, whether or not we, we spit, you know these tool objects into one or 2 parts, so even if we like, treated them separately from local functioning tools. If we just had a a unique semantic convention for them. It's the overall list of things that I'm not sure about the treating it as multiple messages or multiple parts.
Alright.
Liudmila Molkova 00:59:00 Yeah, it's just that the the amount of things we don't know and haven't decided yet is is large around, built in tools.
Samuel Colvin (Pydantic) 00:59:09 Yeah, Sam, you wanted to say something.
Is it worth looking at? Anthropic as well as Gemini? And I don't know what the 4th model is but like a couple more, because at the moment.
Alex Hall 00:59:18 We've we've seen them.
Gemini very clearly returns one message with multiple parts. Gemini very nicely fits the schema that we already have.
Gemini.
Samuel Colvin (Pydantic) 00:59:30 Who and they disagree.
Then you have a 50, 50, if you have 3, then, whatever the answer is, at least you have. You're going to have a majority one way or the other.
Liudmila Molkova 00:59:40 Yeah, so this will. Is this a good point? This will probably add more complexity.
The key question, do we want to block this Pr. On the result of the discussion. It would probably take another month to figure it out.
Alex Hall 00:59:57 I think probably not. But I will say that if if we're going to go forward with the current thing, I do think that the Pr. Needs to make it clear that output dot messages, it being an array. Each item in there represents the choice. I think that isn't really mentioned much or at all.
Liudmila Molkova 01:00:15 Okay, that that's a great point. Then maybe what we should do.
I should take away this example for the built in tools. We have a common there, saying we have no idea how it would look like.
Let's take it away. I'll make it clear that the one message is one choice.
And I like this model, then it's clear to actually parse.
And we, as a next step, we will use your issue to figure out how the built into calls should look like.
Alex Hall 01:00:50 Okay.
Aaron Abbott 01:00:52 Yeah, that sounds good to me, too.
Liudmila Molkova 01:00:55 Thank you. Thanks a lot, and sorry for being late.
Aaron Abbott 01:00:58 No, it's no worries. We are at time any quick thoughts, or should call it there.
Alex Hall 01:01:12 Alright! Thanks.
Aaron Abbott 01:01:13 Alright. See you later.
