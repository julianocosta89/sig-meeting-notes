SIG: Event WG
Date: 2026-01-07
Duration: 68 minutes
Zoom Recording URL: https://zoom.us/rec/share/KlG7416RJQeC79aWMvMwKGDsk1JxJhR7ygwKX0QMQVSbKPH0vFDeulTsqv0Q21NC.47ryBOpMUnpEbjyQ
============================================================

## Zoom Recording Transcript

Trask Stalnaker 00:00:43 Hey, you made it!
Pellared 00:00:49 Hello, hello, I'm doing good, better than I suspected.
Trask Stalnaker 00:00:52 Alright.
Pellared 00:00:55 Yeah, like, 2 hours ago, it was hard for me to talk about anything, because I was a little bit swollen, but right now, it's looking great.
Trask Stalnaker 00:01:05 Glad to hear.
Hey, Alex!
Pellared 00:01:09 Hello, Lex.
Trask Stalnaker 00:01:10 Alan.
Alex Hall 00:01:11 Hello.
Liudmila Molkova 00:01:17 A lot of people on our…
Trask Stalnaker 00:01:19 Yeah, our special meeting.
Alan West 00:01:20 Hey!
Liudmila Molkova 00:01:21 Yeah. Exceptional meeting.
Alan West 00:01:28 This is a new meeting? I just saw it on the calendar, and I was… I was intrigued.
Liudmila Molkova 00:01:33 So we want to… yeah, go ahead, Tress.
Trask Stalnaker 00:01:35 Please, no.
Liudmila Molkova 00:01:37 So we, we have a… somewhat, large decisions to make around, how we record Errors, or exceptions, or both.
on… Primarily logs here.
Why… is there a difference between an error and exception?
And how do we minimize the confusion here? Because we cannot… Have a good explanation, even to ourselves so far.
Trask Stalnaker 00:02:12 And there's a lot of, There's a lot of moving parts, and… So, we've kind of been struggling on how to make… how to Move forward with it?
We've got… A few different… in-flight pieces. Let me just add links. So we've got… This was sort of the… Original… Work.
We've also got, it also ties into… Span event deprecation.
Alan West 00:03:19 Yeah, I followed that a little bit.
Ultimately, though, the plan there was not to necessarily deprecate, but to… maintain span events, but prefer logs or something, right?
Trask Stalnaker 00:03:40 Maintain it over OTLP.
but deprecate it at the API level.
Liudmila Molkova 00:03:50 And still maintain for as long as API.
Exist at least 3 years.
Trask Stalnaker 00:03:58 Yeah.
Pellared 00:03:59 major versions.
Trask Stalnaker 00:04:01 Yep.
But we want to deprecate it at the API level to signal to… mainly to signal to people the preferred… route.
Not to have multiple ways.
Pellared 00:04:18 Also, I think it should be also, said that the fact that something is deprecated, even the specification.
It does not mean that, you know, the languages need to deprecated on the API. If it caused, for example, a lot of warnings, etc, I think it wouldn't be a language decision, if they wanted to mark it as deprecated in the API or not.
Trask Stalnaker 00:04:41 I think that's fair. I don't… I, I think in… Java, we would probably… I mean, I would prefer to deprecate it, but I understand the… that there can be good reasons not to.
Okay, good, and somebody added Roberts.
PR… So, yeah, so kind of what, I was hoping to do with, We kind of started yesterday, is… like, your PR here, Robert.
I'm having a hard time reviewing it.
Because… I want to see… I think… It would help us to lay out the big picture, and what are the parts steps.
Before we… start. I know you're trying to, like, chip away at it, and that's also a good strategy in a lot of cases. In this particular case, I feel like there's… too many… Balls in the air that are making it hard for me to commit to any Like, to just one chip away at it.
If that.
Makes sense.
Pellared 00:06:24 Can I quickly comment? What is my proposal?
Yeah, so, my main focus in this PR was just to, you know, first of all, kind of focus on the deprecation of the span events, and add something that will basically be instead on the locks.
So that when we remove something, we add something new, basically.
And I also try to avoid, for instance, changing the thermology from errors to events, etc, because I find it too… I don't know. We'll need to settle if we want to have exception types, error types, etc, but I don't think it needs to be addressed in the same PR.
Also, I… I think I… I do not remember the structure right now.
how it's different than before, but I just decided that it would be better to have a separate section for each signal, so we can basically stabilize each signal separately. I think there were some little parts before which was for all the signals, so I moved all these kind of things, even kind of replicated for each signal.
So, this is a… yeah.
too long, don't read. And I tried to also give you the description, what are the proposed next steps.
Trask Stalnaker 00:07:51 Yeah, so some of the things that came up when… come up when looking at this, One is for, recording errors on spans… How does this, right, we've got… So you're… you're saying the… the standard, which is calling record exception, stamping… oh, no, but you're saying error to error message… So we have… this brings… this is the… right? Today, the status quo for recording errors on spans… Is, well, recording exceptions on spans.
And maybe part of the confusion is that this document itself was an attempt at Moving us forward.
Towards, kind of, Errors versus exceptions.
But I… I think that… We haven't completely… Resolved that.
Alex Hall 00:09:11 You can see in the diff that there already was a distinction between errors and exceptions.
Liudmila Molkova 00:09:16 There was one. That's right.
But it said that, an exception should be recorded as a span event or a log record.
And I think this is something that we need to address.
In which order? It's a separate question.
Alex Hall 00:09:38 Yes, but I'm just saying, it's not true that… the… the way to record an error was as an exception. There was already, for example, error.type.
As a common way.
Or is the common recommendation, like… The GenAI instrumentations mention error.type.
Liudmila Molkova 00:10:00 Yeah, pretty much any instrument, any conventions that creates pants or corresponding metrics use error type today.
It's a good ques… we… This document currently doesn't have a section on how to record it on logs.
Really, it only talks about the exceptions.
And we don't have a consistency across signals here.
Pellared 00:10:29 I also wanted to make this… Document as much language and implementation as possible.
Because for, at least I know, like, even for .NET, even for Go, there are a lot of ways to record, and, you know, an error, an exception, not always an exception is really an error.
And the same is, you know, not each error is the exception, etc. It depends on the context and the semantics. Basically, you know.
the way the app is structured, it's just, you know, an API design, it doesn't mean that it follows the semantics of an error. So, yeah.
And I think regarding… I think we should… Put more emphasis here on the, semantics here.
Liudmila Molkova 00:11:16 But by the way, your motivation for pushing for it now, is HTTP instrumentation, right?
Pellared 00:11:26 Yeah, spans, basically stabilizing, how to record on spans, exactly.
Liudmila Molkova 00:11:32 Do you actually… So, like, to do it right, we need to go through the spec, because the spec tells how to record exceptions.
And you actually don't ha- F2.
Record exceptions, I think.
Trask Stalnaker 00:11:53 Yeah, but…
Pellared 00:11:54 The thing is that currently, the spec says that it should be recorded using the API to record, the record exception, basically, I would say.
Liudmila Molkova 00:12:06 Which you don't have to call at all.
Trask Stalnaker 00:12:10 Right, but it does rely on span events.
Pellared 00:12:13 Yeah, exactly.
Liudmila Molkova 00:12:15 But you don't have to call it.
Especially…
Pellared 00:12:19 Because… but because of this ambiguity, the thing is that we treat exception the same as an error in Go, because this is how most languages see error handling, and Tyler said, said to me that he remembers that it was some decision, like, 5 years ago, or something like that.
Love ya, goodbye.
Trask Stalnaker 00:12:43 So, the reason why, like, I'm not… sure this, like, I don't… from the Java HCV instrumentation.
Pellared 00:12:52 Christmas.
Trask Stalnaker 00:12:53 perspective, I don't see what you have here for span errors.
Pellared 00:13:03 as…
Trask Stalnaker 00:13:04 Solving the stability?
Pellared 00:13:07 Prop 6.
Trask Stalnaker 00:13:08 blah, like, the… This is the… this is what the span should look like.
It's already documented here. It's already stable. The open question is where to… what to do with the exception or error, like stack trace, and should that… And I think… The way that we've been leaning has been that that should be log.
I think that's what we said in this… in our span event API deprecation.
Pellared 00:13:50 Yeah, but at the same time, nothing, like Alex created his issue, nothing is against, recording, it's also on the span as attributes regarding error type.
Liudmila Molkova 00:14:04 Oh, error type should be recorded regardless, right?
Trask Stalnaker 00:14:08 Erotite, yes.
Pellared 00:14:10 It's already…
Trask Stalnaker 00:14:11 already here.
Liudmila Molkova 00:14:13 If the message, exception message, you would record a dispense status description.
And stack traces are not what you care about in Goa at all, do you?
Pellared 00:14:27 Not here, not for this HTTP instrument. We could do it, but we don't have to.
There are errors in Go that are capturing sex races, but… It's not idiomatic.
Alex Hall 00:14:39 Sorry, we're already in this meeting, why are we discussing the motivation for the meeting?
Liudmila Molkova 00:14:46 I think we… I'd like us to figure out two parts. First, how we can unblock Robert.
For what he's trying to achieve, which is important, stabilizing HTTP.
And second part, how we tackle this problem without the pressure of immediate stabilization.
is… regardless of what we write in this doc, it's in the development, and what we write will still be in the development. It would make it even… Would need even longer time to stabilize.
But I really… I really want to talk about the right way to approach exceptions versus errors.
Alex Hall 00:15:25 So what's missing in the short term? Is it just the stack trace?
Liudmila Molkova 00:15:32 per god, I think, I think.
Alex Hall 00:15:38 like, you said we want to unblock Robert. In what sense do you feel blocked?
Pellared 00:15:46 So, I will feel blocked because we are not sure what is the way forward for capturing events, especially on metrics, errors, especially on spans.
and metrics, because these are the only stable signals right now for Go… in the Go API. And we… right now, there is a recommendation on the specification to record them as span events.
And we just wanted to make sure that not… first of all, that we're not doing it is okay.
Because if we decided, I think it later, some people might not be happy, this is one thing. But secondly, most importantly, I remember, Alex, your proposals adding additional attributes to this fund itself.
And if those will be added, I'll prefer to add it before the stabilization.
Bring out your… So I just wanted to make sure all the proposals regarding, reporting errors on spans Are basically, kind of, kind of solved, or at least agreed, how we go forward. Have I.
Alex Hall 00:16:58 For recording errors on screens, for errors, not exceptions, there's already a standard place to put the type, the type and the message.
Pellared 00:17:08 There's no clear… there's no clear definition was an error or what was an exception.
Alex Hall 00:17:16 Is that distinction a problem for you at the moment?
Pellared 00:17:20 I think it is.
Alex Hall 00:17:22 Okay.
Trask Stalnaker 00:17:25 I mean, there's definitely, like.
Pellared 00:17:26 and then…
Trask Stalnaker 00:17:27 For Java, for example, we call record exception. We do, like, if there's an exception, bubbles up to a span… to a HTTP server span, we call record exception on it. It gets recorded as a span event.
And so, we… will, you know, we need to execute on this OTEP, Which lays out how to… move forward, as, you know, in an opt-in. I think… I forget how we exactly did it, but, You know, we would… yeah, so… In… you know, it would require a major version bump, of course, in the instrumentation to switch that over to log-based exceptions.
But, we have a major version bump coming up in the next few months. You know, technically that… we could use that as a chance to do this, but it's… this is still stuck in, you know, this has only been OTEP'd, there's no… It still needs to be implemented in the spec, and then prototyped and stabilized.
Pellared 00:18:44 So, I guess, I mean.
Trask Stalnaker 00:18:47 two motivations for this meeting is this is just the continuing work of the LogSig.
And that I want to move forward. I think… Lyudmila… basically, Lyudmila's OTEP here has a lot of good, things in it that we need to work through.
And the span event deprecation Has a lot of things that we need to actually Add to the start.
speccing beyond just the OTEP.
And then there's Robert's piece that is… I think, I'm open to… I… I was struggling to pull that in, and that's where… so… but I'll leave that on the table for Robert. We do want to unblock, if needed, for… If there is a way to unblock sooner. I don't personally see it.
But I can be convinced. I personally think that, Robert, you're gonna need a combination of both of these two things in order to… if you don't want to take in another breaking change to how you record exceptions. Unless you just don't record exceptions at all.
Pellared 00:20:11 So… I think it's acceptable for us to just, basically use undespan, not use the record exception API, Because we are not in hotel HTTP, we do not do any retries, etc. No, it's just a layer on top of HTTP library.
So, all our, kind of, exceptions errors are the ones which are ending the operation.
So, using the existing attributes, and just not calling it, and not adding logs is probably our way to go.
Trask Stalnaker 00:20:44 That's… I mean, I'm not opposed to that proposal, but I think that needs some… Specification semantic convention work to… Right, like, now we're gonna… now you're adding yet another way… place to put exceptions.
Liudmila Molkova 00:21:03 Wait, there is… this is exactly what we have documented for spense, right? We should put exception type, or the error type, and spend status description.
Trask Stalnaker 00:21:15 Oh, I thought…
Liudmila Molkova 00:21:16 Oh!
Trask Stalnaker 00:21:16 Robert, Robert was saying…
Pellared 00:21:17 That's what we are doing.
Trask Stalnaker 00:21:18 message.
Pellared 00:21:20 No, no, no, no, no, we are doing exactly what the spec says. We are just setting status to error, but not always. For example, for, you know, 400, for if it's HP kind, we do not do it. It just sets the description.
Yeah.
And just…
Trask Stalnaker 00:21:36 Okay.
Pellared 00:21:37 setting zero type.
Liudmila Molkova 00:21:39 And I used to have a PR, I think I'm holding it back until the OTAP gets worked on, where I'm suggesting the exception to describe the actual exception for the languages that support exceptions.
And this would be probably definitely good to run it by Go and Rust folks, and C++, because I feel it's weird that we use exceptions in languages that don't have them.
And, like, the long-term idea would be that you don't even… Record them.
Ungora Rusty.
Trask Stalnaker 00:22:33 So, Robert.
Pellared 00:22:34 So… Oh, in gold.
Trask Stalnaker 00:22:36 Are you just going to…
Pellared 00:22:39 We have something which is kind of a little bit like an exception, which is a panic.
But, the mechanism of handling The panic is a little bit different.
Then, catching an exception.
Because, it's possible when, when we, when we end a span, It's possible to catch An unhandled exception inside this span.
So… yeah.
So we can… we are able to, you know, basically catch a handle… if I remember correctly, we are able to, yeah, basically catch an exception which was never handled when the span is ending.
And we can, for instance, you know, Yeah.
Which is totally different than the other languages, I think.
Trask Stalnaker 00:23:39 Wait, why is that different? That sounds exactly the same.
Pellared 00:23:44 How would you… are you able, in the SDK, To know that a span omitted an exception.
And for a trace, and it has not been handled without adding a try-catch everything, everywhere.
Trask Stalnaker 00:24:03 No, but how is that different semantically? That's just… you can do it automatically, we can't do it automatically, but semantically, the semantic.
Pellared 00:24:12 Telemetry is…
Trask Stalnaker 00:24:14 the same.
Pellared 00:24:16 Yes, exactly. That's why, in my opinion, the fact that we added record error, which stands for record exception, was a mistake in Go.
But it's already there.
Oh, I see. And it's on the SDK level.
It doesn't require user, you know, user reaction.
Trask Stalnaker 00:24:38 But that's… are you making the… I didn't understand if you're making the argument that that's not an accept… like… Is that not… Exception dot? Would you not use exception?
Pellared 00:24:48 I know, I think it's an exception. I think it's acceptable, therefore, go is an exception.
Trask Stalnaker 00:24:54 Okay, cool.
So, for this PR, is, is… are you… then… are you going to close this PR, then, now that you see that everything's already stabilized that you need on the span?
Pellared 00:25:16 I will need to sleep about it and read again the open issues, because I have a feeling that it addresses some little other concerns, maybe split it to other issues. Maybe, Alex, do you have some comments from your side? Is it solving any of your issues, or not at all?
Alex Hall 00:25:34 Well, I think it's making progress towards what we want long-term. We want to Be able to record Right, I think that we should be reporting Things on spans that we don't currently have a plan for, given that span events are going to be… deprecated. There was plenty of discussion on that.
issue I created a while back about why.
I just… Yeah, if… if you don't… desperately needed for your current, HTTP thing, that's great, but… I was glad to see.
Pellared 00:26:13 I agree, I think.
Alex Hall 00:26:14 Moving forward anyway.
Pellared 00:26:15 It's still good to be open, does not need to be a blocker for my… for our auto HTTP instrumentation library, but I think it's a step… it should be a step forward for deprecating span events and proposing something for logs.
Maybe I'm just over-documenting things there.
Trask Stalnaker 00:26:34 So, as far as moving forward with deprecating span events… I mean, maybe we can follow the OTEP… I mean, I'd like to follow the OTEP, Given that we worked hard and got lots of approvals on it.
So, if that's the goal, I would suggest that we…
Pellared 00:27:02 So, in my opinion… In my opinion.
because I was reading it. In my opinion, it needs to first start with semantic conventions. In my opinion, just… the fact that you will change the specification and the semantic conventions will still say, you know, to use this, I… I think it's just easier to start there in the semantic conventions, in my opinion, than going straight to the specification, and just, you know, mark these are deprecated.
And just clean up the recommendations.
Trask Stalnaker 00:27:32 So let's try to break out that work, then. So we… We want to… This is… Deprecate spam event.
Because I think that's… part of the problem is there's a lot of different pieces, and so it's not clear what we're… yeah, so let's try to break it down. So, what's the piece that you're… Saying… explaining Robert?
Pellared 00:28:06 So, I tried to print the semantics regarding, the semantic conventions for errors, which right now says that, you know, span events should be used. So, we cannot… we should not deprecate something which is right now used by the semantic conventions.
Trask Stalnaker 00:28:31 So…
Pellared 00:28:33 Lydi are talking to us? I'm sorry.
Liudmila Molkova 00:28:36 Sorry, we have a doc and semantic conventions, for exceptions and spends.
I think we should start by deprecating it.
This doc, is linked… There's reference on the specification?
Pellared 00:28:58 Yes, yes.
Liudmila Molkova 00:29:00 What's your focus?
Pellared 00:29:00 Yeah. Support PRs.
It's an APR description.
Yep.
Trask Stalnaker 00:29:15 for exceptions on…
Pellared 00:29:18 Another one, okay, because there's another one specification, which is very similar.
Liudmila Molkova 00:29:24 Yeah. So, I think it's… It's reasonable to start in semantic conventions, but the specification changes would need to follow.
Right away.
Trask Stalnaker 00:29:38 Let's not worry about ordering so much, we'll come back to ordering, because I think there's… that's a whole other complication.
Pellared 00:29:48 Even as the raft opened straight away.
Trask Stalnaker 00:29:50 Because for this one, like, for dep… to deprecate this, I think we need… generally, we don't deprecate something until there's a stable recommendation.
That replaces it.
Liudmila Molkova 00:30:06 It's the file next to it, exceptions, the dash logs.
Which we also have.
Trask Stalnaker 00:30:17 Okay, hard exceptions…
Liudmila Molkova 00:30:21 I don't think we even agree with what's written here, actually.
Trask Stalnaker 00:30:38 Well, that comes back to what we were discussing yesterday, right?
what we don't…
Pellared 00:30:44 necessarily agree with.
Liudmila Molkova 00:30:46 Yeah, yes.
and tear… How the… this story should look like.
Trask Stalnaker 00:30:59 Okay, so deprecate this… And our new thoughts are… Exception.type… Error, type…
Liudmila Molkova 00:31:36 Now, wait, exception.type stays, right?
the…
Trask Stalnaker 00:31:47 dot message…
Liudmila Molkova 00:31:51 this, I think what we discussed yesterday, that maybe exception.message stays, but error.message goes away.
Trask Stalnaker 00:32:01 Mmm…
Pellared 00:32:08 I do not.
Trask Stalnaker 00:32:09 Yeah.
Pellared 00:32:09 I do not see error.message.
Trask Stalnaker 00:32:13 It's not stable yet.
Liudmila Molkova 00:32:16 It's useless.
Pellared 00:32:16 Yeah, because I see… it's in different ways, it's a different place, I see.
Liudmila Molkova 00:32:21 Yeah.
Trask Stalnaker 00:32:24 Okay, so… Maybe we do agree with?
Liudmila Molkova 00:32:29 So, I think what we… I don't, necessarily agree with is that the event name… Oh, we don't document event needs.
So this document semantic conventions for logs, this one here you have open, is just not complete. It does not include thoughts about severity, it does not include thoughts about event name.
But other than that, it seems reasonable.
Pellared 00:32:57 Have a problem.
Do I understand correctly, Udemyo, that basically, instead of my PR, I should change my PR to include the bits which I added to the section, just put it to this document?
Liudmila Molkova 00:33:09 I don't know yet. Let's list things we want in general.
Trask Stalnaker 00:33:18 Severity, and what was the other?
Liudmila Molkova 00:33:21 Event name.
Pellared 00:33:22 event's name.
Liudmila Molkova 00:33:30 So the other thing we've been discussing… Ms. Trask yesterday, that… Today, the recorded exception is a convenience, is documented as a convenience. That's essentially optional.
And we'd rather have it as… the recommendation that the exception object or error object would be passed around, maybe all the way to the predecessor. It's not semantic convention's concern, but it's this back concern.
Trask Stalnaker 00:34:06 And that would be on log.recordException. So we need… we would want to introduce log.recordException.
Or maybe log record builder, set, except exception.
Liudmila Molkova 00:34:21 Or some.
Love some of a… some version of it.
And that maybe that document, the semantic conventions for exceptions in logs, should say… Maybe it's even fine saying that. It's just a branch of attributes you're… a touch.
To whatever event you produce.
And then we don't even need to document all the other considerations, though they still should exist somewhere.
Trask Stalnaker 00:35:05 Sorry, I missed that last thing that you were saying.
Liudmila Molkova 00:35:09 So… Perhaps the document we have in semantic conventions should say that it's not a specific event definition, it's whatever event you have, you can attach the exception details to that event in this way.
Trask Stalnaker 00:35:43 Yeah, I… I think we need some kind of recommendation for generic stuff, like… when a HTTP server span records an exception, what… like, do you just pick any arbitrary event name? Or do we use… exception, or do we use HTTP, something span, exception?
Liudmila Molkova 00:36:19 Or have I attached them to spend?
Pellared 00:36:23 So… I think there were good reasons.
To have two names, one which is basically the type name, like, for instance, exception type, a second which will say… which will be similar to, basically, spell name on the metric name, with some suffix failed, which will say what was the context when it was executed.
For instance, you can get an, I don't know, socket exception when you're trying to connect to a database.
So, then you have two pieces. What operation, you know, what's the event about? What is the context, which would be kind of the event name, like, you know, for example, database connection fail, failure or failed, and the exception name will be socket exception.
Liudmila Molkova 00:37:18 Yeah, and that's why we keep both server type and exception.
Type.
And it's… it would be great to get your perspective from the GO side, where we're… It's kinda…
Pellared 00:37:31 Difficult But isn't error type right now not the same?
Liudmila Molkova 00:37:39 No, that's exactly what you mentioned, so it can be a connection reset by peer for exception type, and… sorry.
Connection reset by peer in the error type, and socket exception in the exception type.
So it's the distinction within.
Pellared 00:37:59 But right now, in the error type, I see, for instance, JavaNet and no cost exception, certificate invalid.
Let me check the HTTP semantic conventions, see if they say anything about it.
Liudmila Molkova 00:38:11 So, okay, so the HTTP semantic conventions would say The status code could be there, if it's an… indicates an error, like 503.
Or, whatever.
Alex Hall 00:38:27 Is that actually recommended, that if the status code is 500, you record the status code in both?
error.type and HTTP response status code.
Liudmila Molkova 00:38:38 Yep.
Pellared 00:38:40 Yeah, we are using a type because we think that, you know, that we have a type, and additionally, it is the status quo, as Alex said.
Liudmila Molkova 00:38:49 So, error type is across all signals.
And if you.
Alex Hall 00:38:53 You're already recording the status code.
In a dedicated attribute.
Pellared 00:39:00 So much, Peter.
Liudmila Molkova 00:39:01 Yes, but it does not explain that there's an error. Let's say I want to show the duration of my HTTP call.
successful HTTP call.
I… the status quoad and success are orthogonal.
To a large extent.
So for… you… you would care, okay, if status code is 200, or 21 or 302, it could all be a success, and 404.
Alex Hall 00:39:34 Okay.
Trask Stalnaker 00:39:35 What we wanted primarily, this is on metrics.
And we wanted to have… Some dimension that you can split on to know what your error rate is, basically to do your, you know, your error rate calculation?
And so we needed something, and we don't have status code from spans.
To make that, determination.
And so then, because we want it on metrics, and we want correlation with spans, and a lot of the instrumentations.
Push everything to spans, and then how… use metric views to filter those down to the metrics.
That was a further reason that ArrowType ended up on Span as well.
Liudmila Molkova 00:40:23 Yeah, and it's somewhat duplicative, but that's the trade-off.
Trask Stalnaker 00:40:28 Yeah.
Alan West 00:40:31 And it might not always be the same either, right? I mean, like, just because… it's not mandated that it be 500 when the status code is 500. You could have a span where you have status code 500, but you have error type.
of… some exception type, right? That's… that's allowed by the…
Alex Hall 00:40:49 Well, it sounds like it shouldn't be the type of the exception, because… That goes under exception.type.
Trask Stalnaker 00:40:57 I forget, we'll have to look at the, errorotype…
Alex Hall 00:41:06 I mean, I don't think that exception.type is currently… expected to be a span attribute, but I do think that that is the plan.
Liudmila Molkova 00:41:15 If we do this… Yeah.
the way I try to approach it, and in one of the PR I mentioned it's not merged, that I'm trying to say, oh, okay, if your exception type is the same, then, as error type, only record error type, and don't record exception type.
it's… it's a way to do this? Is it a great way? I think it's very confusing and not consistent.
Alex Hall 00:41:41 Can I ask what's going on in what you've currently got in the dock there? This connection reset by pair, where does that come from?
Liudmila Molkova 00:41:49 So let's say you're, an actual example, I think .NET, allows you… let's say socket exception has, additional enum inside it, which says what actually happened, and TLS, or connection reset by peer, and stuff like that.
So this is a distinction within the same exception type.
was the error?
Additional error code than what happened.
Alex Hall 00:42:17 So ideally something a bit more granular than the error type, but less granular than the message.
Liudmila Molkova 00:42:22 Yes.
Low cardinality, but as granular as possible.
Trask Stalnaker 00:42:33 did this end up being… is this, like, for, say, SQL Server… Is this where we… But… No, the status code. Yes, status code… Should match.
Yeah, so in databases, for example, you often have, like.
a whole list of, like, SQL Server has a whole list of error codes.
And so that error code would be what goes in error type.
While it would probably be something like SQL Server exception would be the exception type.
Alex Hall 00:43:20 Okay, but, I mean, we were asking about what happens if you just have… the exception type, I mean, there's no clear way to get any other kind of type.
And Lyudmur said something about, oh, in that case, only record the error type, or I don't know. It does feel like if we're going to, say, record 500 in both the status code.
And the error type, then we might as well store all.
My exception in both error type and exception type.
Liudmila Molkova 00:43:53 So, this… becomes… so, for Spence.
Things are even worse. We have spend status description.
Which is frequently… oh, wait, this is the error message.
Okay, yeah, so that's fine, yeah, exception message, yeah.
So, yeah. So if an exception happens… We could always record both her type, whatever it is, the best candidate available, which might match exception type.
And also exception type. It could also be a way. If exception happens, it's an exceptional situation and some redundancy here.
It's not awful.
Pellared 00:44:40 There's also a question of.
Trask Stalnaker 00:44:42 like, error type might be on… I mean, is on spans.
And we might decide for exception type.
I mean, at least currently, I think the… the way this OTEP went was that it would be a log-based event, and exception.type would be on that.
As opposed to being on the span.
Alex Hall 00:45:10 So I don't think that we… that it's in the OTEP, but at least in the conversation between You trust Lyudmila, and I.
What we settled on was… except the type and the message, in some way, I personally, I think attributes, ideally, but I don't know if we've done that part, but the type and the message would be directly on the span, and the only thing that would not necessarily be directly on the span would be the stack trace.
Trask Stalnaker 00:45:39 So, this was the span terminating exception idea.
And I liked that idea, but when we circled it around with folks, there were concerns that, now these… these most important exceptions, the ones that are causing your server HTV requests to fail.
are now in a different place than your… all your other errors. Like, there was… there was a desire to have exceptions, logs.
All be in the same place on logs.
Alex Hall 00:46:19 Well, the same attributes exception type and message can still also be in logs.
Trask Stalnaker 00:46:26 Yeah, yeah, I mean, that can be an option to, to duplicate them on spans. I think that could be, like, a span processory, or some… some option, but I think I… Yeah.
Alex Hall 00:46:42 I think the important thing is that… Querying on the exception type and the exception message is very common.
And you want it to be easy and efficient, and not require joining between spans and logs. Whereas you don't really query the stack trace much.
You don't… it's fine to not duplicate that, it's big.
and… Chances are you can have a way for the backend to, like, automatically pick up the associated log and use that to display the stack trace.
Trask Stalnaker 00:47:17 Okay, so then you're talking about exception.type and exception.message.
Alex Hall 00:47:23 Yeah.
Trask Stalnaker 00:47:25 So, exception.message is… Could be in span status description.
I know that some…
Pellared 00:47:36 In this case, there's this case when there was something ended with an error exception, but it doesn't result in error status code. For instance, you know, 400.
for HTTP server.
That was the core reason of Alec's issue.
So that we do not miss this information, because right now, you can, as you know, when there's an error, like, 500, you get the exception message.
In a span description, but if it's on 400, you miss this information right now.
So I think the proposal was to.
Alex Hall 00:48:14 Well, I think you don't miss this information right now, you get it in the span of.
Pellared 00:48:18 Yes.
Alex Hall 00:48:18 Fair.
Pellared 00:48:19 Yes, but if we lose, but if we deprecate and not put in the span events, and someone is not using clocks, then it's lost.
Trask Stalnaker 00:48:29 That's why we have, I mean, I think this OTEP covers all of this.
Right, so… Stabilized emitting exceptions, and events. So, emitting exceptions via the logs API. I think that was clearly part of the OTEP.
It doesn't prohibit other options, but this is… I think the immediate one we should… Go forward with.
And then, if you want.
to get those on as spanned events, there's still… we're still supporting that via the SDK, log processor to be able to stamp them onto spans as span events for people who need that.
Whose back end needs that, tight correlation.
Alex Hall 00:49:23 Well, sorry, are we saying that we're going to focus entirely on what's already in this OTAP?
Before we get around to… Something like, you know, exception.message attributes on spans, And in the meantime.
Point people towards this more complicated way to use span events.
Trask Stalnaker 00:49:51 This is what I want to focus on, because we spent a long time getting agreement on it in the community, and it outlines a concrete path forward, unless we run into blockers.
Alex Hall 00:50:09 I mean, I thought we were trying to move away from spam events As much as possible, and even if we're not, like, forcing people off them, we're not… Saying, okay, well, if you want to record exceptions directly on spans, you still have to use span events somehow.
Trask Stalnaker 00:50:27 So, I mean, if you… you're welcome to, you know, send a… a propo… make a proposal and, you know, bring it to… the log sig, the spec sig…
Alex Hall 00:50:39 But I made a proposal, we had a lot of discussion, and that's what that issue that I created was, and then Robert opened a PR, starting that process of… Saying, you know, let's put these attributes on His parents, like, that's already happening.
Pellared 00:50:54 Yeah, we got, in the go, I think we got similar feedback that people would welcome.
this kind of little… just these attributes in the spans. Even if this information is duplicated then in logs, adding just this one kind of attribute, Exception, exception message.
It's seen as a good trade-off.
Trask Stalnaker 00:51:18 And maybe send a PR just with that, so we can discuss that.
Right now, this… PR does a lot.
Right?
It's not clear to me that that's what this PR is about, Robert's PR.
Pellared 00:51:39 But if that's important to you.
Trask Stalnaker 00:51:41 Go, Sig, and Alex for your use cases.
Then, you know, by all means, let's… get a PR out there, and we can discuss the details.
Pellared 00:52:02 Still, I think that the more with a couple, and you know, tackle things in baby steps, the better it will be, because a lot of things you are tackling are not, like, blockers, because they are workarounds. So, for instance, you know, you could make you could find from the logs API transformed into, you know, into SPAN attributes, etc. So, yeah, probably we just need to focus on deprecation, having any proposal, have some common agreement, and then probably before going stable, just making sure all We have some consensus, or at least compromise.
Also, I think that Maybe even getting rid of this documentation, this document, and just pointing, for instance, cementing conventions to exceptions or spans, etc, may be more efficient than playing too much on this single document.
Because it looks like there's already… The document recording errors.
I think it kind of, instead of Yeah, basically the one which I created the PR for.
Trask Stalnaker 00:53:15 Oh, oh,
Pellared 00:53:16 I think instead of… I think it's this place which you're open right now is maybe a better place to put this kind of information, which is in my current PR.
Maybe, I'm not sure, I'm just asking you to be honest, because you're the cement-conditioned maintainers.
Liudmila Molkova 00:53:34 And… We created this doc because we needed a way to have guidance for different… consistent guidance across semantic conventions.
And this is also the way to correlate things, right? I think this is the point, that the way you Classify something as an error as signal agnostic.
Pellared 00:53:56 Okay.
Liudmila Molkova 00:53:57 And… I don't mind breaking this document down and sharing it, but we still need a single… Place.
Her signal and some common…
Pellared 00:54:08 So what we say is that probably we still need this document, but maybe some parts maybe could be better fitted in the separate, you know, in these documents, maybe, just to not duplicate things.
Liudmila Molkova 00:54:21 Yeah, and however… I have this document is…
Trask Stalnaker 00:54:24 I think this document is great, like, we just need to, add, you know, we identified, you know, this is… It's missing some important pieces.
That will, that are difficult, you know, challenging. Like, this whole severity question.
we need to document, and that really does tie into Lyudmila's earlier OTEP.
Pellared 00:54:53 Yep.
Trask Stalnaker 00:54:53 And then the event name consideration is important and tricky also. Like, you know, we have these things, like, well, what… what is… should event name be one of these? Should it be just exception? What… what kind of… What recommendations can we make for exception, for event name to avoid people just… Same XYZ.
Alex Hall 00:55:31 One possible event name is, or at least in the generic case of span ending exception.
Where we're recording the stack trace and whatever, could just be original span name plus exception.
Liudmila Molkova 00:55:49 Yeah, this is a good idea. I somehow think that the span… we are too span-centric.
The only reason we want this as a separate thing is because we assume that somebody cares about it regardless of tracing?
And…
Alex Hall 00:56:10 come up with a generic recommendation in the case where there's no span involved? Like, surely then it's context-dependent?
Liudmila Molkova 00:56:20 You might have context, you just don't have a spend for it.
If you sample it out.
But even without context, getting all the exceptions is kind of popular.
But, yeah, something around, not the spending, but the HTTP client exception. HTTP server exception.
But… might be useful, but then they should be defined, right? So, okay, so, okay.
If you don't know anything, if you don't have a convention, maybe it's just an exception, or no event name at all.
If we say that we meet a log record like that from HTTP server instrumentation, we should define the event fully.
Trask Stalnaker 00:57:28 It's a good option.
We're almost out of time here.
Soon… We've identified This… let's go back to… okay, on this… What else in your OTEP.
Will it Milla… maybe this is an async question.
I know the severity stuff is very… relevant.
Liudmila Molkova 00:58:14 But, yeah, the severity… Nuh…
Trask Stalnaker 00:58:28 Yeah, the duplicate exceptions, I feel like.
Liudmila Molkova 00:58:31 Application route, yeah.
So, I think we can, Declare partial success if we clarify severity.
And if we clarify the setException API.
And based on this too, we can evolve it further.
duplication.
Trask Stalnaker 00:59:08 Yeah, where did I… and I wrote that down somewhere, set exception in… Here, to-do.
Liudmila Molkova 00:59:23 And then, based on what we discussed today, The said exception.
It's essentially the set of exception attributes.
We don't tackle anything.
Alice.
Trask Stalnaker 00:59:40 Yeah, we just keep them…
Liudmila Molkova 00:59:47 With a caveat that it's not the API.
only thing, it goes all the way to SDK.
Trask Stalnaker 00:59:56 Right, as the object.
Liudmila Molkova 00:59:58 As the object, yes, and there is some default format there that creates attributes from exception. That's replaceable.
Trask Stalnaker 01:00:14 Cool.
I can take this… Anybody have anything that they… want to… Robert, you're gonna follow up on your PR and see if there's anything that you want to… Salvage or split out from that.
Liudmila Molkova 01:00:44 M.
I'll… Get back to that happen.
I remember we wanted to clean it up and remove everything that doesn't have to be there, and then we'll keep severity and the event name, maybe something around duplication.
Trask Stalnaker 01:01:01 Yeah, I'm gonna put you on severity, because that's the hardest one, I think. And then, yeah, we can brainstorm more about event name. I think we've got some good ideas there.
Pellared 01:01:15 Alright. If you have any proposals, what should I… do with my PR some concrete proposals, like, for instance, get rid of, you know, for instance, remove severity, just how to scope it out, what to remove, or even just to close it.
Or if you want me to tackle some, you know, part of it, just let me know.
Liudmila Molkova 01:01:38 I have a stupid suggestion.
There is this current dock.
There is the current doc with the one you're modifying, and it says that you should record something as a span event.
Or… Logue record.
What if… what if we just update that section and remove spun event from it?
And there is an example, it's invalid, you would have to remove it.
But… what if I just write this to start with, and then we can expand The section to recording errors and exceptions, if necessary.
Pellared 01:02:24 So, just changing the part about capturing exceptions, that's what you told, to remove span events.
Liudmila Molkova 01:02:33 Yeah, and whatever we can actually recommend now. It also aligns with Alex's question of Do we actually record it on a log?
And… That we don't… there is nothing on the spend that would contain exception information anymore.
So, I'm… maybe I can share for a sec.
Trask Stalnaker 01:03:11 Yeah.
Alex Hall 01:03:15 I don't like the idea of having… A time where… there is no… Recommendation to record anything on the spam.
Unless it's an error.
Like, rather than just removing this, can we not replace it with a new recommendation involving span attributes?
Liudmila Molkova 01:03:54 So what your proposal would be to record this exception as?
attributes on span.
And a log record.
So maybe what… what we can… how we can evolve this.
we know that we want to record it as a log record. It does not preclude recording it as a… Pen… attributes.
Two, in one way or another.
It's… it becomes an… Does it become an instrumentation concern, then? It's an instrumentation choice?
You could, in theory, build a processor.
That, upon receiving a log record, gets the current span, or span associated with this log record.
And you can stamp exception attributes from a log record on that span. It's not an instrumentation concern.
Trask Stalnaker 01:04:59 Yeah, and maybe we just…
Pellared 01:05:00 Thanks, Bob.
Trask Stalnaker 01:05:01 than the hotel.
Pellared 01:05:02 Not sure. There's one problem. I'm not sure if the processor would know if this is, for instance, you know, the last exception.
like, the last error, maybe not accepting, accepting will be the last.
That's useful.
Trask Stalnaker 01:05:16 No, it's a log… it's a log record processor.
And it has access to the current active span.
Pellared 01:05:24 Yeah, but there can be… There can be multiple logs inside the spam.
Retries, etc.
Trask Stalnaker 01:05:31 Oh… yeah.
Liudmila Molkova 01:05:33 It would overwrite then, or it would need to… I don't know.
Alex Hall 01:05:39 But do you want it to go… Just whatever exceptions happen.
As opposed to specifically span ending exceptions.
Pellared 01:05:50 Yeah, I agree with Alex. Maybe just give an option that instrumentations may additionally record exceptions.
Like, just, you know… This ending error or exception as attributes.
Maybe not as a short, but as a May.
Liudmila Molkova 01:06:18 That if we wanted, well, I kind of would love it to have it as opt-in.
Right? It may be off by default, but it would be nice To have, in some cases, of by default bits, because it's duplicative, right?
It could be, in theory, done for record exception.
and… and span, or surro… the span status.
When you're setting spam status, you can pass an exception there.
Or a span record exception could be smart and also write a log record, but that's… that's cross.
cross-signal stuff. That's difficult.
Pellared 01:07:01 I'm not sure if record exception should ever change its behavior.
Liudmila Molkova 01:07:07 That's right.
Unless somebody opts in.
Trask Stalnaker 01:07:11 We're… we're, over time here, and I think we're drifting, into… I think somebody just needs to make a concrete proposal. This is outside of what we have agreement on from the OTEP, so this is outside of our… Core remit. But there's no reason we can't Make additional proposals and try to get community buy-in.
Liudmila Molkova 01:07:43 Yeah.
Still, I think we… sorry, we're still over time, but we can remove this. We can say that this details is… Like, if we say, should record this as a log record.
It does not mean we cannot add extra features.
On top of it. We know… we all agree that this should go away.
Trask Stalnaker 01:08:07 Yes.
Liudmila Molkova 01:08:08 this.
Trask Stalnaker 01:08:16 Cool.
All right, well, thanks for this, extra meeting, this week for the Log SIG.
lot to work through here, and thanks for joining, Alex and Alan. Feel free to join, we meet every Tuesday at, An hour before… this meeting, so at 10 a.m. Pacific time.
So, see you at the next meeting.
Liudmila Molkova 01:08:45 Thank you.
Alex Hall 01:08:46 of…
Trask Stalnaker 01:08:46 I…
