SIG: Event WG
Date: 2026-01-06
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/8dy1JOTJypWigjlfol1s2OthC30mqkupYkcB92mUQxZgjoe4OUfseNcTll9XIil9.4kyqIWUAHw2-XLyY
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:03:31 Hello!
Sorry for being late.
Trask Stalnaker 00:03:37 The problem… Hello.
Cats. Love your… Cat, window apparatus.
Liudmila Molkova 00:03:48 Yeah.
Even if the day is very bad, I can… Anyways, talk to my cats.
Now, where's Robert? He… I think I've seen him online, but he's not… Around.
he made a stab at the error stuff. I'm not sure if you've seen.
Trask Stalnaker 00:04:17 I saw that there was a PR that did not… Open it.
I'm recording your head back.
That's not what…
Liudmila Molkova 00:06:44 Oh, they wanted to stabilize HTTP, and that depends on it.
And they would rather not…
Trask Stalnaker 00:07:00 do the… yeah, I mean, they could stabilize now, and then… Do the opt-in and major version bump in the future.
Yeah. But I understand.
Liudmila Molkova 00:07:24 I don't mind, yeah.
Trask Stalnaker 00:07:26 Oh, God.
Liudmila Molkova 00:07:28 I don't mind, providing some guidance that we can Provide in this doc and remove span events from it.
What are we going to say?
Trask Stalnaker 00:07:48 I'm trying to think of how this… applies to Java… Agent, Or more like when we would want to… Take that breaking, like… It's still… it feels early to me.
That… because we haven't really… I feel… I'm trying to think of how much work is involved here, what the kind of timeline… Like, is this… Can we push forward with… I mean… Yeah, maybe we should. Maybe we can. Maybe now is… the time… I mean, we do want to deprecate span events, so it… I mean, we do have that kind of clear direction.
Liudmila Molkova 00:08:59 It would mean… Okay, so let's try to compartmentalize. If… Where… Provide the guidance for errors on logs.
vivid.
I really need to pass it through this pack, folks, and this pack, and this is the tab that We are… I'm not… I dropped the ball there.
Span event deprecation would go through it.
Anyway.
The semantic conventions part.
This document is in development. I think we… Could stabilize some sections of it?
Maybe not everything, but most of it.
It's still a pretty long way before It would not… I don't think it's a good path for gold to… to… to block HTTP stabilization on.
But it's probably the next thing we should tackle in the logs, anyway.
Just in general.
Trask Stalnaker 00:10:28 Yeah, cause we're… Done with complex attributes.
What were our other…
Liudmila Molkova 00:10:50 Good question, what are we working on?
Trask Stalnaker 00:10:53 Event name is stable.
Yeah, I mean, I think that complex attributes was… Was our big… the.
Liudmila Molkova 00:11:22 So… Think, duh.
the implementing the ATAPs where… the vision OTAP is the… The big one.
Trask Stalnaker 00:11:36 the span event.
Liudmila Molkova 00:11:39 That you're, you're a vision, not cap.
Whatever it means.
Trask Stalnaker 00:11:43 E…
Liudmila Molkova 00:11:44 The… the span of that deprecation, yeah.
Trask Stalnaker 00:11:51 Okay, so yeah, so that… Makes… Sense that we would do… And that, of course, ties into the exception stuff.
Liudmila Molkova 00:12:08 Right.
Trask Stalnaker 00:12:27 Okay, this is done.
In the proto, serialized emitting exceptions… So, we've stabilized emitting events in the log API.
Question is… Do we want… Record exception…
Liudmila Molkova 00:13:01 And this is the convenience API, and we kinda… done with it, right? We said, okay, go for it, language-specific implementations.
Trask Stalnaker 00:13:19 That's true. We could still have, just on the… Log Record Builder.
We could have a set exception.
Liudmila Molkova 00:13:35 Yeah, and I mean, from the spec perspective, it's the ergonomic API, and we can even list it there.
But essentially, we leave it up to the language seeks to decide what they provide there.
So, like, Rust would not provide said except exception, it would provide something else.
If anything at all.
Trask Stalnaker 00:14:04 So, we're taking a different… because right now, there is the span record exception.
Which is in the spec.
Liudmila Molkova 00:14:18 And it's a convenience.
Right? You don't… Well, we can talk about it in extent, but it's essentially… should provide.
Trask Stalnaker 00:14:47 Okay.
Yeah, I think we would… to me, at least in Java, I… I think I would want to add a set exception On to the Log Record Builder.
Which… Is different than… Is it different than our convenient ergonomic… I don't know what our ergonomic API even is.
Jack has some… thoughts…
Liudmila Molkova 00:15:22 And absolutely, like, I mean, every log API in the world provides some form of it, right? When you provide the exception instance, and… You decide how to format the… It didn't a log record.
So maybe, actually, this is the… Not sure if you want to pick this battle, but… I think… we can think about it as an ergonomic API and set of attributes, but it's much better to think about it as something that's configurable, right? So, if user provides a stack trace, it's not great. We'd rather want them to provide the full exception, and then there is some component that formats the stack trace.
And in the sense, it's not an ergonomic API, it's the very… Specific thing that we want to pass over, maybe all the way to the processors.
Or at least to the, the, some configuration oak.
Trask Stalnaker 00:16:35 Yeah, which is what we ended up doing in Java. Initially we formatted it right away.
But then we ended up passing it across so that People could kind of customize the formatting of it.
Liudmila Molkova 00:16:53 So then let's pick the bottle.
And let's… let's make it, an… Required.
Required for languages with exceptions.
Trask Stalnaker 00:17:03 Yeah.
Liudmila Molkova 00:17:03 Yeah.
With some behavior.
That explains why it's not ergonomic.
Should it create an issue for it?
Trask Stalnaker 00:17:22 Yeah, let's write down… The things that, We… yeah, we should probably… I mean, we could create issues for… the different pieces of this OTAB.
Yes, most everything is remaining.
Log-based exceptions, what… Should the event name… B.
Liudmila Molkova 00:18:31 And this is actually semantic conventions, and much closer to what Robert As… I, I, I, I think… It's separate, right? It's orthogonal. You can add exception to any event.
Exception details.
And maybe if you… all you know that it's an exception, then maybe you should set that… the name to exception.
Trask Stalnaker 00:18:57 Okay.
Liudmila Molkova 00:18:58 error.
Trask Stalnaker 00:18:58 Yeah.
Yeah.
So… Okay, but they should be events. They should have an event name.
Liudmila Molkova 00:19:17 N-no?
So, like, today you can write a log record with exception information using SLF for JRID.
Right. We don't want to limit this ability, do we?
Trask Stalnaker 00:19:32 No.
So, in… But what I… so, for instrument… instrumenting, HTTP instrumentation, you catch an exception, you log an exception.
Liudmila Molkova 00:19:51 Oh… We're back to the… Log versus attributes and span.
Trask Stalnaker 00:20:06 Yeah, we could, yes.
we could… Go back there.
Liudmila Molkova 00:20:19 Imagine, I don't know, let's say there is an instrumentation foo.
And exceptions are part of part of its life, and there is more than one during execution, and you want to log, let's say, not an error, but I don't know, a wording or an info.
With exception details. It's a valid… Case, right.
You're retry… you're retrying, you want to look, why are you retrying?
You probably would want to provide some event name.
and say, I don't know, connection draw… I don't know, connection error, where… Something more specific than just exception.
Anomaly, if you have no other idea. You might want to do exception.
Trask Stalnaker 00:21:25 You're going to have a log level.
It's going to have… the exception… attributes on it.
Liudmila Molkova 00:21:47 Are you thinking it makes no sense to even have event name if it's just an exception?
Trask Stalnaker 00:21:55 I kind of want it to have an event name, so that it's an event, since we're trying to Push people towards… event.
I'm not sure what you would… Do… how you would decide that event name, what… what its sort of relevance is.
I mean, if it's, like, HTTP… if you wanted to filter… I mean, I guess you already have the… With the logger name… Scope, info B would be the HTTP, same as the HTTP Tracer name… So you can… Filter that way already.
There are so many. And then, what about… what happened to our error versus exception?
Liudmila Molkova 00:23:22 Oh, that's… yeah.
I think this is the, the… the core part of the semantic convention story we wanted to tell.
Trask Stalnaker 00:23:37 Yeah… There's so many things, what order?
So, we have… Error versus exception… So what was… what's Robert's PR doing?
Liudmila Molkova 00:24:24 I didn't check the last version. The… We have… So what I want to fix? There is a… This doc talks about how to record errors and spans and metrics. It does not talk.
About how to record them on… logs.
And I think Robert is trying to fix this.
Trask Stalnaker 00:25:00 Oh, I see. Recording errors on spans… So it says it's not recommended to record the error via a span event.
What is it recommended? Recording errors on spans. Oh, I see.
He's just saying, actually, what you stamp on the span itself, and then… There's a separate… Recording errors on logs… I see, and he avoided the stack trace question for now.
But did use error type and error message.
As opposed to exception.
Liudmila Molkova 00:26:54 So this is actually a change in the spec we need to make, because… This is exactly what specification talks about.
I don't think this is the right place to start.
Let me find it.
Can you share?
Trask Stalnaker 00:27:40 Yeah.
Liudmila Molkova 00:27:45 So we have this friend, and I'm pretty sure we… Refer to it.
For, the record exception doc, from the SPAN API.
And this is what we tell here.
And we say that the semantic conventions must provide the following events.
This assumes it's a span event. This assumes it's a… it's a…
Trask Stalnaker 00:28:15 Welcome.
Liudmila Molkova 00:28:22 So I think we… we need to approach it from the spec.
What does the record exceptions say?
Huh.
Trask Stalnaker 00:28:59 So, the deprecation plan… Says… marking the span.
Record exception as deprecated.
Liudmila Molkova 00:29:12 Right.
So this whole section would be deprecated.
Bye.
Trask Stalnaker 00:29:21 Ad event would be deprecated.
Liudmila Molkova 00:29:24 An event would be deprecated.
Trask Stalnaker 00:29:27 Yeah.
Liudmila Molkova 00:29:29 Then, this document should be deprecated.
Trask Stalnaker 00:29:48 Yeah, I mean, so… That gives us a… path to error dot, if we… Want to take that.
Liudmila Molkova 00:30:08 Yes, this so it does so be fully deprecated.
Then it leaves us with… Still… Surrey.
So what do we have? Error?
Right?
Error.
Message.
reception… Right?
Exception.
Message?
Exception.
Backtrace.
So this difference are different.
Right?
Error type is… Or something like this.
Trask Stalnaker 00:31:20 Hey.
So what, I mean, in Java, mostly we just populate it with the… They are a type… What do we do for error type?
Not weird.
Liudmila Molkova 00:31:36 So…
Trask Stalnaker 00:31:37 Yeah.
Liudmila Molkova 00:31:38 Let's say it's the SQL exception.
you would have SQL exception, or whatever the… Override, used versus the error code.
Trask Stalnaker 00:31:56 Right.
Okay. Yeah, yeah, that… I mean, that's… Err…
Liudmila Molkova 00:32:20 This difference… You can… you can find artificial examples where they're different, but probably they are… more same than different, right?
Trask Stalnaker 00:32:51 Yeah… Yes.
Our message, our message.
Liudmila Molkova 00:33:43 It's like… If there is an error.
Explanation or description you got from somewhere.
But the exceptions, do they usually wrap it in something, right? But they… Sometimes preserve, usually preserve the original one.
And to a large extent, It doesn't matter.
Which one you provide?
Trask Stalnaker 00:34:19 Yeah, I'm trying to think, like, most of the time… So, like, with… most of the time, you're catching an exception, and that's kind of all you have, like, it's… A little more… like, that's just… It's a little more rare to be like, okay, this is a database A database exception that we need to extract an error type from.
But, that does exist. So, okay.
I'm with you.
Liudmila Molkova 00:35:07 I don't know where I am yet.
Trask Stalnaker 00:35:08 I don't know where we're going, either. Yeah.
Liudmila Molkova 00:35:11 Yeah.
The stake trace is kind of unique, right?
Error stack trace.
So I've had some requests that has never been merged in the past, and maybe I can find it.
Where I was proposing to talk about errors in general.
And only use exceptions for… first for languages where the exceptions exist.
And on the… Apply when you actually have an exception and you are recording its properties.
I remember it was kind of hard to explain, like, how do you avoid duplication?
But at the same time, being consistent, so you want to populate error type, but when would you also populate exception.type?
And why?
It's confusing.
Trask Stalnaker 00:36:18 Yeah.
If we were trying to consolidate on error… And we catch an exception, and we log exception type and error type.
Error message… But it's not necessarily… exceptions are not necessarily errors.
Would you ever log… Error.
Type… no, error.type is supposed to be… Present when it's an error.
Like, you wouldn't have error.type at levelinfo.
Liudmila Molkova 00:38:03 Huh, good question.
Good point.
Trask Stalnaker 00:38:11 Whereas exception type… Could be info.
And so, like, as something… as an exception bubbles up, like, we were trying to avoid… Logging it multiple times.
By saying that, like, you could log it each time at debug.
But only sort of at the outermost… You would log it at error… So that you could get all of them if you wanted.
Liudmila Molkova 00:39:04 I think we… that the proposal was to avoid logging it, but yeah, if you log it at debug, it doesn't hurt much.
Yeah.
So would we actually implement it in the way that… We would not populate our type.
If it's the severity that's lower than her type?
It sucks.
Trask Stalnaker 00:40:09 So, how bad is it if we have both? We don't… like, I know we were trying to consolidate on error.
Liudmila Molkova 00:40:22 I don't think we're trying to consolidate on there, right? So this already implies we have both.
And the stack trace. I don't want to have error docs.stack trace.
attribute, unless we want to make stack trace typed, and that we would rather remove.
Trask Stalnaker 00:40:42 Hahaha.
like, a complex… stack trace.
Liudmila Molkova 00:40:54 That's placed on a rate.
Trask Stalnaker 00:40:59 Okay.
So… What's… So we have both of these.
We're just trying to decide when to populate Which…
Liudmila Molkova 00:41:19 When to populate which, and how to make it the least.
Confusing to implement and understand.
I think.
And at some point, there, like, yeah, there is a trade-off between technical precision, or what… what makes sense technically, versus how it would actually it be used. And if everybody would just use something simple.
We can… make a… Trade-off in favor of simplicity rather than differentiation.
But anyway, I think we… I'd like to explore the past when we have both, and see how, like, the easiest way we can make it happen.
Trask Stalnaker 00:42:08 Sounds good.
The error, I was just thinking about the error type, is… so, on spans… We have status.
That tells us if it's an error or not.
On logs, we have level that tells us if it's error or not. Metrics is kind of where error type Shines.
And… So… But if it's so… The… the reason to put it on spans and… Logs is for… Span to metrics, pipelines, log to metrics, pipelines.
Liudmila Molkova 00:43:15 Right.
Trask Stalnaker 00:43:41 And so that's kind of why it ends up feeling a little duplicative.
Unless we also say… Wow.
But exception type… Error type.
Liudmila Molkova 00:43:59 Oh, I see what you're saying. So… on… Hands.
Error type is not duplicative, right, because it has a value that's not in the status.
Trask Stalnaker 00:44:16 Oh, and we don't… we're not putting exception type on spans anyways.
Liudmila Molkova 00:44:22 Y… yes.
So… The message, our message is… Probably where it becomes blurry.
It becomes duplicative.
Well, we're not populating either of those on spans, we're saying put it in the spend status description.
I think.
But… I feel our justification for error.message is much weaker than justification for that type.
Trask Stalnaker 00:45:16 Yeah. Yeah, arrow.type is… I agree, is… I mean, the met… because of metrics, it's critical.
Error. I see, so error.message, so what's the point of error.message?
Liudmila Molkova 00:45:40 So we introduced it when, from the feature flags.
Right. And they had cases where, when the… They have an error, but don't have an exception. And it's more terminology than anything.
else.
So if we designed it from scratch.
I would say that exception.message is error.message. They are the same, but we picked But we can have a better terminology with error.message.
Trask Stalnaker 00:46:32 So you're thinking if we… it would be exception type, I see error message…
Liudmila Molkova 00:46:44 So, exception.message is… Error is a generalization of exception, right? So it's a wider term.
Trask Stalnaker 00:47:01 on a log… I think of error message on logs as being the message attribute with a level error.
Liudmila Molkova 00:47:15 I'm gonna pick up.
Okay… I like where you're going.
Is it the case for… Both of them, the message… So, let's say I'm writing, a log today.
what I'm… what I would do is… I would say message, I don't know, connection dropped?
And… I would also have a separate message for what was in the exception.
Not that it has to be done this way, but it's how it's already done.
Trask Stalnaker 00:48:15 Yeah.
Yeah, I mean, I'm thinking of, like, the Java, you know, I log error.
And I have my error message, and then I ask my exception, and it's gonna log my error message, plus my exception to string.
Liudmila Molkova 00:48:32 Right.
What would happen?
If we say… If for a name exception message, terror message, how bad would it be?
And say that, okay, if you want to differentiate log message versus attribute.
This is how you do it. If you don't, just use whatever, log message.
Trask Stalnaker 00:49:23 What is error message… Can we go back to the feature flag?
Error message… So… turn our message. Can… what I'm wondering is, can this be… Message… Does that… that feel… Weird.
Liudmila Molkova 00:50:11 What fatal food word?
Trask Stalnaker 00:50:13 Rename… having this just be, like, response message.
The level… Indicating… being used to indicate that it was an error.
Liudmila Molkova 00:50:30 Oh… Like… let's say in RPC, gRPC would return you Two things, the code and message.
And it's almost like we have RPC response code, there would be RPC response message.
It's not even… A general concept, and more, like, a… Convention-specific thing.
Trask Stalnaker 00:50:58 Yeah…
Liudmila Molkova 00:51:04 I like this.
It essentially means that there is no error message.
At all.
Trask Stalnaker 00:51:12 Yeah, yeah.
And the idea being that backends… Like, when you're displaying it.
Logs, you're gonna use the log level.
To display that it's an error, and filter by errors.
And then the whole content of… Babe.
Event… Is more or less your error message.
Liudmila Molkova 00:52:20 Oh… Yeah.
It's actually… Huh.
Trask Stalnaker 00:52:27 No, go ahead.
Yeah, yeah, all the content of the log is the message, yeah.
Liudmila Molkova 00:52:34 And it's almost like that when it comes to logs, error terminology is confusing because you combine the… like, because it's ambiguous, the severity.
But also the thing that you have attached to the.
Trask Stalnaker 00:52:49 Right.
Right.
And so that would avoid, kind of, the problem of… Do you stamp error.message onto something? Can you stamp it onto something that has level info?
Liudmila Molkova 00:53:06 You probably should stamp it or type on something that has info.
Trask Stalnaker 00:53:12 How about error miss, error. error.type? .
Liudmila Molkova 00:53:18 For the correlation reasons.
Trask Stalnaker 00:53:24 You should or shouldn't?
Liudmila Molkova 00:53:28 I think you should. Like, if, if… Like, imagine you stamped the socket exception, but didn't stamp the… specific error type that caused that socket exception, or you would query By our type, and you wouldn't find your log records about it.
Trask Stalnaker 00:53:51 But shouldn't it then be… Level… error?
Liudmila Molkova 00:54:14 So you… you're going to have… Okay, so for spense.
Trask Stalnaker 00:54:19 Yeah.
Liudmila Molkova 00:54:21 where… We consider them to be an error.
Regardless of the context, right? We're saying, whenever you experience an HTTP 503, it's an error.
For logs, we are seeing something different.
We're saying, Oh, 503! Actually, it's probably retried. Don't… don't log it at error unless you know.
It's not.
And if… I feel like if we don't stamp error type on not errors… then it would… We would break the attribute-based correlation.
Trask Stalnaker 00:55:18 I agree with that, so just trying to think of the… The reason for… Spans and laws… so, because spans and metric… We are aligning their definition of error.
So, what is our justification for having a different definition of error for… Correlated logs…
Liudmila Molkova 00:56:03 That's a great question.
Trask Stalnaker 00:56:10 I mean, I remember the discussion.
That, like… If something is… sporadic… Like, net… like, yeah, like you said, something that was retried… Something sporadic.
Like, the idea that log… Error. Log-level error is more precious.
Trying to be like, oh, when… But I'm wondering if it should be.
Or if that value outweighs… consistent.
Error definition across signals.
Liudmila Molkova 00:56:57 So if we have a consistent third definition across signals.
Where… And presumably, we cannot change it for Spencer metrics.
I'll go suspense.
We would have… Everybody would log errors all the time.
We would need to come up with a new strategy to find The outermost errors, the ones that affected your… Responds back to the caller.
And then we would have… we would need means to filter Ever logs based on something else.
Trask Stalnaker 00:58:00 Oh, I see what… so, if we're catching a… if we're, HTTP client span.
Throws an exception from inside there.
That span is marked as an error.
We… If we recorded a log on that, then… Shit.
Should have error type… for correlation… But it could be… add.
Info… Or debug, even.
Yeah, yeah, I agree.
So, we would have error type, Exception type… So, back to error message… I forget how we got derailed. Oh, it's also… 11.
Liudmila Molkova 00:59:29 Yeah.
Yeah, okay, so I think let's stop here, but I think to summarize, we can entertain the future where there is no error message, right?
And there is then just error type, and then there is exception message and exception stack trace.
Trask Stalnaker 00:59:48 Yeah.
Liudmila Molkova 00:59:49 And they only describe things around runtime exceptions.
Oh, I mean, the except… the runtimes that support exception.
Trask Stalnaker 00:59:59 Yeah.
Do you want to, I mean, I'm up for continuing this discussion later this week, if we want to try to not, to try to… Before we forget… Or trying to make progress, I don't know.
Liudmila Molkova 01:00:21 Yeah,
Trask Stalnaker 01:00:23 There's so many things to unpack here in this whole exception… Thing…
Liudmila Molkova 01:00:31 Yeah, I… I can. It can continue now, or I can continue, pretty much any afternoon is free for me.
Trask Stalnaker 01:00:40 Cool, yeah, let's pick on Slack, but, tomorrow… Yeah, let's meet tomorrow. I'm free from 11… to… 11 to 2.
Liudmila Molkova 01:01:01 11 to tomorrow.
Tomorrow.
Trask Stalnaker 01:01:09 Any time, 11, or if you have preference.
Liudmila Molkova 01:01:13 Anytime.
Trask Stalnaker 01:01:15 Cool, let's do 11.
Liudmila Molkova 01:01:16 Okay.
Trask Stalnaker 01:01:18 Cool, I will, I'll add it to the official.
calendar, and… let other people know in case Robert is able to join.
Liudmila Molkova 01:01:29 Oh, cool, wonderful, thank you.
Trask Stalnaker 01:01:32 Alright.
Good discussion.
Liudmila Molkova 01:01:34 Yeah, good to see you.
