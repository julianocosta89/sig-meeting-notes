SIG: LLM Semantic Convention WG
Date: 2026-01-27
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Minghui Zhang** 01:45 Hey, Ushian.
**Liudmila Molkova** 05:02 Hello! Hi, everyone.
**Minghui Zhang** 05:04 Hey, hey Lyudmira.
Good afternoon.
**Liudmila Molkova** 05:08 Good morning.
Okay, let me… Yeah, screen… Please add your name to the agenda, and if you have any topics, please add… your topics.
**Minghui Zhang** 05:56 We, we have left that on the top of the agenda, so I will… I will fix the… I will add the, attendees, after this meeting.
Nevermind.
**Liudmila Molkova** 06:15 Okay.
Is that your names?
**Minghui Zhang** 06:21 Okay?
**Liudmila Molkova** 06:33 minghu, I remember you had a PR on the Python trip.
I don't know the status. Do you need any help with it?
**Minghui Zhang** 06:47 I have done it, but it needs more review. Could you please give me an approve?
**Liudmila Molkova** 07:12 This one.
**Minghui Zhang** 07:14 Yes.
**Liudmila Molkova** 07:15 Okay.
And I remember we talked about the configuration.
I will… Review and approve.
**Minghui Zhang** 07:32 So basically, maybe I needed more approval from, Russell and, I don't know, Case? Oh, maybe… Wait, I need a year.
Weirds.
**Liudmila Molkova** 07:52 is approved, dial in, I'll check with him tomorrow on the call.
**Minghui Zhang** 08:00 Thank you.
**Liudmila Molkova** 08:07 Okay… So let's talk about token level attributes and events.
I just skimmed through, I would need to… Spend more time understanding it.
Could you… could you share the, like, the summary?
**Haotong Zhang** 08:33 Okay.
Let me share the screen.
**Liudmila Molkova** 08:37 Yeah, yeah, sure.
**Haotong Zhang** 08:37 Oh, good.
Can you see my screen?
**Minghui Zhang** 08:54 Yeah.
**Chris Yang** 08:54 Yeah, that we can.
**Haotong Zhang** 08:55 Okay, let's get started.
Hello, everyone, I'm Hao Tong from Art Group. Today, I'd like to introduce our proposal.
For token-centered tracing in reference engines, and discuss how we can define new semantic commissions to support it.
Let's see the motivation. Today, mainstream influence engines.
Such as VRM and STLON already support request-level tracing, which means one request typically maps to one span.
But many production issues I am serving do not appear correctly.
At the request level, a single request span can show overall latency, but it often cannot explain why the request is slow.
Yeah, RME for instance, let us say, frequently comes from token-level behavior.
When each token is scheduled, and when it is generated, and how batch size changes over the code iterations, and the queue pressure, and the waiting size of the scheduler. So, we need a rotation system.
That allows users to clearly inspect each token and relate it with internal information, such as scheduling and decoding behavior.
So, let's say this screenshot. The screenshot shows our internal token level analysis tool. In this panel, you can see key metrics like TTFT and TPOT. In the panel below, it visualizes the schedule and generation time for each token.
If you hover over a rectangle, you can view details for the token's, decoding stat.
The one request, one span tracing system follows the semantic conventions defined at this link, and to enable token-level tracing, we need to define additional token-level semantic conventions.
We tried with two approaches for exporting token-related information.
The first one is to use attributes to store token-related information.
In our internal product, we collect token-level metrics as arrays and attach them to the requested span as attributes. Let me explain them one by one. The first is twist level.
The trace of the level, and 0 for no trace, 1 for request trace enabled, and 2 for token level trace enabled.
And the next one is per token generation time. It's an array of time steps when each token is generated.
Relative to request start.
The next one is per token scheduled time.
It's an array of scheduling time steps.
The next two one is…
**Liudmila Molkova** 11:58 Okay, can, can we, stop here for a second? So, like, is it, for, for the… Would you expect the client-side instrumentation to capture those, or… It would be the model itself that captures it.
**Haotong Zhang** 12:21 I think S would be the, the model side.
**Liudmila Molkova** 12:27 I see. So then, it's the conventions you would be introducing is the internal model tracing.
**Haotong Zhang** 12:37 We will insert our codes into the inference engines.
**Liudmila Molkova** 12:44 I see. So then, it sounds like this is a bigger thing. It's the… Engine instrumentation, and we, we have nothing about it, really, to date in, in, in up on telemetry.
**Haotong Zhang** 13:00 now we have implated the basic traces into some influence engines, like VRM and SCLON, and we have come up with some PR Implement our token-level tracing.
**Liudmila Molkova** 13:20 Yeah, it's just… but I'm saying that it's not just the attributes.
It's more. There are…
**Haotong Zhang** 13:27 Oh.
**Liudmila Molkova** 13:28 That the spans need to be defined, it's a huge area of instrumenting the engine.
Itself. And it's, it's cool, it's awesome.
But it's a completely new area for us.
**Haotong Zhang** 13:44 Oh, yes, I know.
So let's, continue. Per token, total tokens.
It indicates the total number of tokens in the request scheduled for this batch.
And these three attributes show the top K candidate tokens returned by the engine, along with their decoded strings, token IDs, and the corresponding log probabilities stored in nested arrays.
And the last one is per token number new tokens.
It shows number of newly generated tokens per iteration, mainly for MTP situation. MTP means a multi-token prediction.
The main benefit is that, this approach is very efficient, in our measurements. It's a single span with a certain number of attributes.
And the arrays are compact. However, we also recognize potential concerns. The first is that the large attributes may not be indexed or queryable in many backends, and it may not align with common semantic conventions or hotel best practice.
And this requires a downstream tool for data visualization.
So, we come up with…
**Liudmila Molkova** 15:16 Yeah, so, yeah, the main concern is that we don't define engine spans today. We don't have… we don't document anything about the engine.
At all. However we want to record this information, And for this, the most important question is probably, How many?
engines are we going to instrument? Is it something unique to Alibaba, or is it a part of ELLM? Like, what is the… Who would report these conventions?
**Haotong Zhang** 15:57 Okay.
**Minghui Zhang** 15:58 Oh, oh, hey, I want to, I want to explain it. So I think this is very, I think it's not, Unicode for Alibaba, it's very generic, semantic conventions for, any, inference engines, like, VRM, like SD-LAN, so we want to, show Common or generic semantic conventions for all of these, All of these inference engines, So that we can… we could have a… have a common, back-end and front end to show the, details.
Rather than we have one for VRM or have another one for STLM, that's our… I think that's our, Yeah.
**Liudmila Molkova** 17:01 Yeah, I'm thinking about the following. So, we are still in process of polishing, the client side.
And there are the problems the SIG mostly tackles, Sergei.
So the problem SIG, currently tackles are, like, client instrumentation, the, Different sources of inference, call agents, multi-agents, more on the client side, on the application side.
And, We can bring it up, but we don't have other representatives of the engines who are interested in this effort.
And it will be a big one.
It's not just defining some attributes.
So, I'm thinking, in the way to make progress, it could be that we would find, we would ask on the sick call, they can spread the word, they can say, you folks are interested, and if there are other people who are interested to participate, they might, they would collaborate on this. The other approach is that you can, like, define these conventions as part of ELLM.
Or you can define them on your own. They initially, at least, don't need to exist in semantic conventions in OpenTelemetry.
Until at least they are… supported by… just a few… common components.
**Minghui Zhang** 18:43 Oh, cool.
**Haotong Zhang** 18:43 Okay.
That, that means, we can explain this in where I am, and I still, in, I still am.
The community… the community of, open telemetry will… Then concern about… Adding it in our semantic conventions.
**Liudmila Molkova** 19:09 I'm more like, why do you even need it to be part of open telemetry semantic conventions? And you… like, first of all, if there is not enough expertise in the community around engine instrumentation, we won't be helpful, we won't be a good authority.
I… like, we need some people who actually represent these engines to review and discuss this in details.
**Haotong Zhang** 19:42 Okay, I understand that.
**neilyashinsky** 19:45 I kind of feel like, I hope this is, this is well… if I'm… if I'm understanding… I'm so sorry, I'm terrible at pronunciation, save me, Ludmila, if I'm close, but I kind of feel like, without… I agree with what… everything you said, and I think, like, the nice thing about these groups is, like.
There are probably people who are lingering on the back walls or whatever, kind of like me today, who have similar, experiences, and… and maybe if I… again, trying to extrapolate a little bit of your instructions is like, hey, great to collaborate on this issue. It might not bubble up to the level of a semantic convention yet, because it's not common enough to, per se, justify a convention in that sense.
But at the same time, like, it's great to… for folks who are… interfacing on these types of conversations to find things that are… I'd say, like, this is an emerging convention, maybe, optimistically, or what have you? Like, it's not… it's not broad enough yet to warrant standardization, but not to say the conve… the conversation is bad or unwanted, which is, again, not that you're saying that, per se, it's just like, hey, like, let's, maybe in trans… Continuing this conversation, less in the context of a convention itself, but, like, a community conversation for people who are involved in similar topics. Am I, like, anywhere close? Bail me out here, please.
**Liudmila Molkova** 21:21 No, thanks a lot for rephrasing it. Okay, sure, sure. It's awesome, yeah.
**neilyashinsky** 21:27 Okay.
I'm turning on the camera so you can see my brow wiping here, because I felt like I was… Not… hopefully not inserting, because I feel like, that's some interesting, conversation, and I don't want to, delay moving on to the next topic, I… oh, like, the one thing that I was wondering here is, like, Do you know how many… values you would expect for per-token candidate token IDs? Like, is that gonna… the one thing that I was wondering is, it looks like that would have extremely high cardinality as a metric?
And perhaps there would be… it'd be better to do that maybe as a log?
If I'm reading it right, I'm super new to what you're trying to do, but… If that's… Yeah, does that make sense?
**Haotong Zhang** 22:21 Yeah, then maybe we can, Continue to discuss, whether our… We have two explanations, but I don't know which explanation is better.
The first one is our, internal product in combination… in combination, and the… Method B is the, The version we, we want to contribute to the community.
**Minghui Zhang** 23:01 Yeah, I, I want to, give some, extra information, so, we do want to, catch, or capture these, high, candidate, identity, informations in, metrics, but, we don't think it's a good idea for, here, because, for the inference engines, each… each request is important for us. We want to mark any, Any requests?
So… Every request may be very different. One request may be fast, and another one may be very slow, and it may be blocked in in any token, and we want to fund the issue. We want to address it. So, I think Chase is more, suitable for these, cases.
Yes, that's why we want to mark… we want to capture this information in trees rather than metrics or logs, yeah.
**neilyashinsky** 24:27 I'd love to hear how that turns out. Again, I wasn't saying it's, like, good. I'm not, like, here to judge, I was just, like, the one thing that I thought about is how valuable Will that be… as a metric, if the cardinality levels are extremely high, versus what you could get from, like, I think… You can keep the request spans?
you know, aggregate attributes, but for, like, the per-token details, the candidate tokens, log probes, maybe scheduling times, that might be useful to structure that as a log or an event itself, rather than a trace, because I think it would just be really hard to… To manage the volume of values that you'd get.
**Minghui Zhang** 25:17 Special thought.
**neilyashinsky** 25:21 I think customers struggle with that.
But maybe you're… I mean, I was gonna say maybe you're smarter than me. I am not a certain 1,000% you're smarter than me. At least in a lot of things. So, maybe on this one as well.
**Minghui Zhang** 25:38 Okay, maybe, maybe we could, we could have a further, discussion about that, but, before that, I think, Hotung, maybe we, maybe we need a more… I think a more detailed, issue about that.
Right?
**Liudmila Molkova** 26:00 God.
I think we need to find a community of people Who are interested in engine instrumentation.
**Minghui Zhang** 26:08 The people who…
**Liudmila Molkova** 26:10 can… Who have experience with engines, and who need to monitor them.
And without having this community, and the feedbacks from… feedback from them.
We would, like, we can continue the discussion, but we would not be able to host the conventions, because we would not have expertise in the community to… to decide what's good and what's bad.
And there are two ways we can take forever. I will advertise it in tomorrow's call, feel free to put it on the agenda or advertise in the chat that you're looking for other people who are interested in server-side tracing.
I can ping, VLM folks, and they might also be interested to collaborate. If we find this community, if we find one or two other people who don't work on Alibaba, maybe work on VLLM, to join the effort, that would be awesome.
If not, then what I'm saying, that you should probably host them yourself, these conventions.
You know what you're doing, you will experiment with this, you will own it.
And then, maybe eventually other people will start following.
But let's try to build that… find the community within the GenAI group. I just don't want to go into the details, because I have no idea how to monitor engines.
**neilyashinsky** 27:41 Yeah, and I'll just say, like, one last note, thanks again for bringing the conversation.
to… and of course, for shepherding us through this, very capably. The last thing I'd say is, like, there's… and there's focus on the client end, if you will, not engine side, but more, like, client side evaluation, performance side.
That's why I've kind of like, oh, that's that, you know, I'm on the other side of the line, if you will, which is why I'm interested.
Separately. But yes, thanks for steering and shepherding the conversation, through the larger group. I think that sounds, like, really helpful.
From what I…
**Liudmila Molkova** 28:16 Yeah, thanks. And…
**Haotong Zhang** 28:17 Thank you.
**Liudmila Molkova** 28:18 We can't, like… wait a sec.
From the client side, there is a similar problem. Much less severe, but a similar one, right? So, how do you record time per each token on a span, on a client span? You don't have any other details, right? But you still have the time between tokens.
And there was an interest in the past, at least from some, some folks, to somehow record this. And I think it's the first attribute that you had.
In this list.
**Haotong Zhang** 28:55 Yes, we have some information that can only be obtained from the engine side.
**Liudmila Molkova** 29:03 Yeah, I mean, we can discuss the approach.
Right? And it will be probably similar on the client and the server, it's just on the client there is One array, and on the server, there is way more.
So, if I understand correctly, your alternative is to use span events, right?
**Haotong Zhang** 29:26 Yes.
We use many, spam events to start the, token-level information.
**Liudmila Molkova** 29:36 Yeah, the span events are… are being deprecated. So they… they won't be span events, there will be just events which are log-based.
But it's effectively, in terms of the volume of data, it's the same, whether you emit a span event or if you emit an attribute.
The attribute is even cheaper, even… less.
**Haotong Zhang** 30:01 Yeah.
**Liudmila Molkova** 30:01 Overhead. Yes.
**Haotong Zhang** 30:03 My concern that their trace will be too event-heavy.
Excellent.
**Liudmila Molkova** 30:11 Yeah.
So, for… for the… I just wanted to discuss, like, the… the couple of approaches I've seen… I've… I've seen people entertaining.
Maybe I'll… I'll just… Take notes in the doc we have.
So one approach is, okay, we can… super verbose, right? We can record every detail. Talking arrives, we remember the timestamp, and we record it.
Okay, token timestamps.
Relative timestamps. The other approach is less verbose, but lossy. What if we record distribution under the attribute, like a histogram under the attribute. We might not need to know The time between each token?
Before each talking, but we might, in more common case, we might want to see if there were Delays.
**Haotong Zhang** 31:22 Yeah.
But we are using the token level tracing to know every latency of the tokens. We don't want to miss anyone.
**Liudmila Molkova** 31:41 Okay, so for your case, you only… you… you want everything.
**Haotong Zhang** 31:48 Yes, yes.
**neilyashinsky** 31:50 I do wonder if that means… if that… if you could still derive your… Tokens per second using a recording rule on the log?
It might perform better.
Because I think you get the same information.
But you won't need as many to keep track of as many spans.
**Haotong Zhang** 32:14 Maybe we will consider that, and… Know that the span event is… will be differentiated.
Maybe using log is a better way.
**neilyashinsky** 32:27 Yeah, for high-frequency data, I think in particular that'll be… from… at performance, I've found… I'm sure Udomil can speak way more about this than I've done, but that could be a, you know… because it is great to, like, have that information, but the moment you need to, like, search through all that information at scale.
then it becomes less accessible if the cardinality is so high that the query takes a really long time, so long to run the query that you, like, by the time you get the data back again… I mean, again, maybe you're super fast about this or what have you, but… That's what I wonder.
**Haotong Zhang** 33:06 Hmm.
**Liudmila Molkova** 33:07 So for spans, we just want people and expect people to query for it, right? It's just if you… you query by something else, by trace ID, and you see, okay, there is some problem, and then on the span, you see a bunch of attributes, and it doesn't affect query experience, it affects the span.
Size.
Recording logs would be fun, because for high-frequency data, instead of recording, let's say, a thousand doubles on attribute, you would record thousand logs. It's much, much, much, much worse for performance and data volume, because there is also envelope size and everything.
**Haotong Zhang** 33:48 Oak.
**Liudmila Molkova** 33:50 But then it would not blow off the… the span payload size. It will be some other signal you can control separately. So, pros and cons. Or you can record it as one log, with all the details, and then, it's still one envelope, but you can control it. So, like, there are trade… trade-offs.
But maybe… okay, there is a world in which you want to record timestamp of each token. But… Another difficult question. Wouldn't you want to record each token, then?
Along with the timestamp.
Like, how do you know?
Which… Oh, you can tokenize again, but let's say Vertex, the Google thing, they… it delivers chunks, not tokens.
And these chunks are much bigger than tokens. So you kind of depend on the… Tokenization mechanism, or chunking mechanism.
**Haotong Zhang** 35:01 Oh, we know, in some situations, we won't, de-tokenize, the token IDs because it's too late, Spend some, some efficient, like, efficient types.
**Liudmila Molkova** 35:25 I'm not sure I've got this. Can we maybe switch to my screen, and I'll try to explain my question.
**Haotong Zhang** 35:34 Okay.
**Liudmila Molkova** 35:41 Oh, thanks.
Okay, so, let's say… I wanted to know… I've been taking some notes, So let's say I'm getting a stream.
And it looks like, I don't know… Oh… I don't know how the technization works, maybe.
Hello, and then world, maybe… like this, I don't know how many tokens there would be. Anyway, so… let's say I'm… I'm receiving this at time stamped 1.
I wonder if you're showing us what you think you should be showing us? What am I showing you?
**neilyashinsky** 36:39 The meeting notes?
**Liudmila Molkova** 36:41 That, that, that, that's what, and I'm typing there.
**neilyashinsky** 36:45 Oh, maybe I just weren't seeing where you were. Oh, you know what? It might have been why. I had… I zoomed in at one point in time, so you were probably doing the totally right thing, and it was just off my screen, so sorry. No, you're right.
**Liudmila Molkova** 36:54 Oh, no worries.
**neilyashinsky** 36:54 You're good, good, good. Thank you.
**Liudmila Molkova** 36:58 Okay, so I'm receiving this token at this timestamp, I'm receiving this token at that timestamp, and finally… Yeah.
So this is what I received, and finally, maybe I received whatever done.
And maybe… I don't even know, maybe there was a retry.
Somewhere here, the connection dropped.
And then it was restored, and after it, I resumed, and this is what happened.
So… Why are we recording just the timestamp?
And not this part.
And it may be more than talking.
**Haotong Zhang** 37:49 Hold coming…
**Liudmila Molkova** 37:54 like… At least from the client side, there is no guarantee that it returns every token.
It's just chunks.
**Haotong Zhang** 38:03 But in engines, the connection problem won't appear…
**Liudmila Molkova** 38:11 Right.
Okay.
**Haotong Zhang** 38:13 I… We just need to, record the time steps and the way We'll surely know the… The rank of the tokens.
**Liudmila Molkova** 38:30 And they are not on the telemetry, or are they?
**Haotong Zhang** 38:38 Oats.
Third… I… I think the engines, meet the tokens locally. They don't need to… Establish a very… Far connect… connection.
**Liudmila Molkova** 39:25 I mean, here, like, the span would also include some information.
about… the… What's… what model has generated, right?
**Haotong Zhang** 39:39 Yes.
**Liudmila Molkova** 39:39 Is it…
**Haotong Zhang** 39:40 model.
Yes, yes.
Another picture?
**Liudmila Molkova** 39:46 So, you don't really care. Like, looking at this span alone, you don't really care About correlating each individual token.
to what it was. You only care about timestamps.
Right.
**Haotong Zhang** 40:08 We also care about the, like, iteration batch size and the rating size, because it can help explain, if the token is Very slow than the other.
It can explain the reason.
**Liudmila Molkova** 40:27 I see, so then essentially what you are recording is a structure of some sort.
So, you're recording the timestamp?
And a bunch of things. So this… We're meaning…
**Chris Yang** 40:42 and record four information. One is, is the scheduled time.
And another one is the generation time.
deceleration time.
And the batch side, iteration batch side. Batch side means total request number.
And another one is the total token number.
Over the batch.
Total token number. Okay.
**Liudmila Molkova** 41:12 Yeah.
**Chris Yang** 41:14 Total, total number.
**Liudmila Molkova** 41:17 Off of the bed.
**Chris Yang** 41:19 Yeah. Yes.
**Liudmila Molkova** 41:20 And then you are recording it as, four separate arrays.
**Chris Yang** 41:27 Yeah.
Because we found that when one's request is slow, we found that some tokens contribute to the slow.
So we, for example, we… maybe we… the request break… break the TDFT, Okay, Authority.
**Haotong Zhang** 41:55 But…
**Liudmila Molkova** 41:56 I mean, the alternative, could be, like, whatever you record, Currently, it's the list of, like, it's multiple arrays that are correlated by index.
Right? So, you take all the arrays, and by… in one position, you would have all those numbers. And if in future you would want to add, let's say, the token itself, or something else, it would come through an additional array.
**Chris Yang** 42:25 Yeah.
**Haotong Zhang** 42:26 Yes.
**Liudmila Molkova** 42:27 The alternative could be, and it's slightly less optimal, but it's a bit more user-friendly, that you record it as a structure.
Right, that's the scheduled time, one generation time, one… Badge size.
to… Total token number… Whatever. Sweet.
This is more readable.
But…
**Chris Yang** 42:59 Yeah.
**Liudmila Molkova** 43:00 minimal.
**Chris Yang** 43:05 Why… why we use the array? Because we can… we consider the… The performance cost, or performance overhead.
Maybe, array is more better when we're considering performance something.
**Minghui Zhang** 43:26 So, let me, like, what do you, what do you mean about this, we should, once we, get a token or a chunk, we send, we emit a log, right?
**Liudmila Molkova** 43:43 I think the most effective way would be the one that you… the two… Documented here.
It's the attribute, and you would have… Timestamps and individual attributes.
Logs would be probably… The least efficient, because you need to create the whole and export the whole log record.
Or… Like, you could have one log record under the span, But it might… Mmm, not be interesting enough.
Like, like, there is not… not a huge difference between one log under the span versus one span attribute.
**Minghui Zhang** 44:38 Yeah, so, so… It's like, it's just like the event with a detailed information, related to the inference span, right?
**Liudmila Molkova** 44:53 Yeah, that's… that's one of the ways to think about it, yeah.
**Minghui Zhang** 44:59 Okay.
**neilyashinsky** 45:08 Well, just one last question. It sounds like the context of this was all, like, within the operations of a single agent.
Are there agent-to-agent considerations in here as well, or is it kind of within the context of a single agent?
Chain of execution.
**Haotong Zhang** 45:26 It's, it's a, Oh, we have implemented in the mainstream engines, like, where I am, STLAN, and Tanzarati RIM.
**neilyashinsky** 45:40 I guess because I was just curious if it spans, like, more than one process, like, if you're… because you're trying to understand, like, end-to-end tracing.
And I was just curious if there's something long happening, is it like there's a sub?
Agent process that's kind of running… That's part of this.
I, I, again, that's more my question. I fully understand what, you know, the context, so maybe I'm mistaken. I was just curious if that's… Part of the operating… ecosystem, or maybe I'm confused?
**Minghui Zhang** 46:13 Yeah.
I know what you mean. I don't think it, it should, or it, it should exist in the common species.
Under the agent, because it's a very large.
very large… Informmissions.
**neilyashinsky** 46:39 Okay, thank you.
**Chris Yang** 46:41 I would follow that.
**Liudmila Molkova** 46:50 Okay, so then, to… the biggest question. I think there are a lot of… Technical details, and they are not important.
To a large extent.
That the most important question is, how do we find The community to help you push it forward.
I'll bring it up on the tomorrow's call.
I mean, what else can we do?
Are you… do you work with VLLM, somebody from VLLM?
**Minghui Zhang** 47:32 Exactly, no, but we, hey, how, how Tong, have, have we, contributed to, VRM or SGLAN before?
**Haotong Zhang** 47:44 Yes, they contribute to where I am at asylum before. The basic trace of where I am is implemented by us.
**Chris Yang** 47:56 Yeah, new concert trace.
**Haotong Zhang** 48:04 And we also work on the finger and the traces of Astila.
**Minghui Zhang** 48:12 Yes, so… so we are the… we are the contributors, right?
**Chris Yang** 48:17 Yeah.
**Haotong Zhang** 48:18 Yes.
**Liudmila Molkova** 48:19 And I see you folks created the issue, the OPP request.
Nice.
**Minghui Zhang** 48:29 Maybe you… Sorry? We could, invited more, maintainers or approvals from VM and SGLM here to discuss this, right?
**Liudmila Molkova** 48:46 I think, like, if, like, if we don't find people in the Autel community who want to collaborate, it is the natural place for this thing to live in VLM.
Like, if you want to document the conventions, they are awesome. So why… why do you want it to be in open telemetry at all? They… you would have much more leverage, or… it would probably go much easier and faster if you make it part of the LLM project.
**Chris Yang** 49:22 Yeah, you can be a fan.
**Minghui Zhang** 49:25 Yeah, but, maybe… asylum, maybe another type of schema.
And it's, we want, we won't get a generic semantic conventions, but, I know it's very, it's very hard for, for us, so, we now could have, specific semantic conventions in, VOM, right?
**Liudmila Molkova** 49:54 And if the LLM project Is open to documenting conventions there.
Like, you send a pull request, if it's merged, they are there, it's just they are not documented.
They could be documented on the side here.
informal way, and informal way, we could, have a link from, from OpenTelemetry, saying, okay, you know what?
We… Also have these external conventions defined in VLLM.
And… it would be… In New York… Control.
Like, if you… if you own the conventions for a VLLM, then probably You cover quite a bit of commonalities, and others would be open to adopting them as well.
Or… am I making sense? Like, is it… Like, is it something that you… would consider?
**Minghui Zhang** 51:05 Yeah, I think, since maybe we could, add some… we could document these behaviors, in VRM, first.
And…
**Haotong Zhang** 51:18 Okay, okay.
**Minghui Zhang** 51:19 I think it's… From, Open Tanometry.
**Liudmila Molkova** 51:25 Yeah.
Okay.
**Minghui Zhang** 51:52 Sorry, go ahead.
**Liudmila Molkova** 51:56 I didn't have anything, And one other thing that, we could consider to, like, help you find the community and, like, bring attention to this. So, imagine, like, this PR is… merged.
And you have conventions documented.
I would be happy to support the blog post in OpenTelemetry.io, saying that this is happening. There are, like, people who are driving engine conventions forward, they're starting with VLLM, And, I don't know, come to OTEL if you want to work on it within OTEL, if you're… or work with them on the VLLM site.
**Haotong Zhang** 53:14 Yes. Okay.
**Chris Yang** 53:15 Okay.
**Haotong Zhang** 53:15 Thank you very much.
**neilyashinsky** 53:20 Definitely appreciate wanting to come and, like, share your insights and your wisdom, and, like, I feel like that's such a great community-supportive endeavor, so, you know.
My camera's off, but, I'm doing the, applause, the American Sign Language for applause, so you'll have to envision me as, like, wavy hands or what have you. But, no, that's great work. Round of applause.
**Liudmila Molkova** 53:43 Thank you, Neil, for being the welcoming host. I sometimes fail with it. It's nothing about you, it's me.
**neilyashinsky** 53:50 Yeah, no, no, it's great, like I said, I thought that was… the conversation shepherded exactly, like, you did a tremendous job as an advocate, you know, trying to, like.
drive as best you understood, I think, if I'm hopefully reflected right, like, how you can achieve the goals as you understood them to be the most productive without being an unnecessary constraint, or what have you.
**Liudmila Molkova** 54:15 Thank you.
**neilyashinsky** 54:16 So, here, a round of applause for you two.
**Liudmila Molkova** 54:18 Thanks. Okay, really appreciate you all coming.
And let me know if I can be helpful.
**neilyashinsky** 54:27 So far, super helpful, none of that, done, no notes. Thanks, everyone. Good chatting with you today.
**Liudmila Molkova** 54:32 Thank you, bye.
**Chris Yang** 54:34 Bye.
**Haotong Zhang** 54:34 Bye.
**Minghui Zhang** 54:36 Thank you.
