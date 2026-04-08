SIG: Event WG
Date: 2026-04-07
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 01:29 Hello, hi Robert.
**Pellared** 01:34 Hello, how are you?
**Liudmila Molkova** 01:36 I am good. How are you?
**Pellared** 01:38 good as well.
**Liudmila Molkova** 01:42 I haven't seen you in the speckles lately, where you're just quiet there.
**Pellared** 01:47 I was today on this tech call. I was even talking in the beginning, maybe you were right.
We will later do stuff in the background.
**Liudmila Molkova** 01:55 Yeah, I would agree.
Pay attention to speckles.
I have not made any progress on logs, it's embarrassing.
**Pellared** 02:21 I made some, and I put everything to the agenda.
I'm just making… Release in the background.
Yeah, I see that you're already on the docs.
**Liudmila Molkova** 02:46 Oh, you made a P… or you made a… Change to this pack, nice!
**Pellared** 02:56 PR, you mean just, not changes yet, right?
**Liudmila Molkova** 03:00 Yeah, yeah, the PR.
**Pellared** 03:00 That's a long way.
Alright.
**Liudmila Molkova** 03:14 I think Trask will be coming. He was just in the call with me a few minutes ago.
**Pellared** 03:18 on the island?
**Liudmila Molkova** 03:19 Probably zip.
Yeah.
Yeah, I'm just reviewing your PR.
**Pellared** 03:36 Okay.
You can ask questions if you want.
You can even share your screen if you want.
**Liudmila Molkova** 03:54 Oh… you would probably hit the… the configuration PR, so… Now that we are going to require Configuration, update for every… PR for a respect change.
**Pellared** 04:10 I added it as the to-do.
I… the prototype also mentions something, so it's just about agreeing for the name. I'm not sure if it's a block or not.
So, yeah, I can draft a PR, I just didn't know if it's, you know… given the prototype already has something. I think it's… I think it's even implemented in Java component, I think Java already did it.
the implemented.
**Liudmila Molkova** 04:32 Yeah.
**Pellared** 04:33 component for configuration.
**Liudmila Molkova** 04:35 I mean, we're going to merge the requirement that spec PRs must come with the config changes, so we'll… yeah.
**Pellared** 04:45 Hello, Krask.
**Trask Stalnaker** 04:47 Ayy!
Robert, you want to drive the meeting?
**Pellared** 05:07 No, please, no! Why? Trask, really? Okay, I could try.
**Trask Stalnaker** 05:13 You got this.
**Liudmila Molkova** 05:15 Yeah.
**Trask Stalnaker** 05:18 Ludmila and I are, like, exhausted now.
**Pellared** 05:21 Oh, absolutely.
**Trask Stalnaker** 05:22 an AI meeting.
**Pellared** 05:27 Let me just do it like that. So, do you want to.
**Trask Stalnaker** 05:32 Plus, you're doing… plus you're… you're pulling all the weight for this SIG right now anyway, so…
**Pellared** 05:38 No, that's not true. That's not true. I think it's true. Anything, anything you wanted to add to the agenda?
I put just mine stuff, I think most of them are follow-ups from the previous one.
I have not created anything for the collector yet.
because we agreed that we are waiting for more feedback, I think, before taking any steps here.
Just pulled it.
S… Yeah, this is waiting for VINX.
Regarding the unwrapping, he, he will, he'll have it on the agenda.
And yeah, that's all.
So maybe let's go one by one.
So, regarding this, this issue… I'm not sure how the same kind of triaging works.
But I remember that last you mentioned that this unwrapping is already the code from the Java instrumentation, right?
And we already have a PR for Go as well, to do kind of the same, just for one type, and it's mostly approved. It's mostly approved, probably, it will be merged tomorrow.
So, even if it will be not merged, we'll do it anyways, because it's a junk that nobody wants. So, I think that… I'm not sure if you want to triage it to the mirror by yourself, or you do it.
**Liudmila Molkova** 07:05 I already did.
The temp contrast process is… Non-existent, pretty much, issue triage.
**Pellared** 07:13 Okay.
Okay, so it means that I can last time myself and try to work on it.
**Liudmila Molkova** 07:19 Absolutely, yes.
**Pellared** 07:20 Okay.
**Trask Stalnaker** 07:21 Yeah, you can remove the need… the label now, also.
**Pellared** 07:25 I… I can? Okay.
**Trask Stalnaker** 07:27 Or accepted, yeah, change it to accepted.
**Pellared** 07:33 Which one?
**Trask Stalnaker** 07:36 Yeah.
**Pellared** 07:39 Alright.
You can put it in progress.
Accept. Okay.
Any hints regarding implementing it? Will it be just, you know, like, asterisk or some comments to the, or do you know your interest think it will be anything more?
Or just, you know, language.
**Liudmila Molkova** 08:06 just a known.
**Trask Stalnaker** 08:07 I was thinking… Yeah, note for error.type, just have a May blah blah blah.
**Pellared** 08:17 Do you want?
**Liudmila Molkova** 08:17 And exception.type.
**Pellared** 08:19 for exception type, okay, so both.
**Trask Stalnaker** 08:21 Oh, right, right.
**Liudmila Molkova** 08:23 This affects… okay, so this affects all the attributes, right? If we unwrap, we also might reduce the trace, and we change the message, because we use the cause as the… option.
**Pellared** 08:37 So, no, we didn't want to change the message. We wanted to keep the message, keep the stack traces, just, unwrap the type.
Because we want the original stack trace with everything, we just want to get rid of this kind of wrapped exception type.
**Trask Stalnaker** 08:57 I think Java does it differently. I think we are unwrapping… And then… Capturing the stack trace message and type.
So, presumably the stack trace should… B… Hmm… I… what you all are suggesting makes a lot of sense, though.
**Liudmila Molkova** 09:38 ecosy.
**Trask Stalnaker** 09:38 Okay.
**Liudmila Molkova** 09:38 Probably not my bossy.
**Trask Stalnaker** 09:44 Yeah, and kind of who cares if the stack trace is extra… Big.
Or, like, in… the only benefit in Java, kind of, of doing this, potentially, is you have a little bit tighter stack trace, but in reality, probably not, really, because you're already removing duplicate frames.
from the caused by… I like… I like what you all are doing in Go. I would just… why don't you include that as the language, and then… Were…
**Pellared** 10:20 Okay.
**Trask Stalnaker** 10:20 kind of… we can debate it on the PR if I come up with any reason not to.
**Pellared** 10:26 Okay.
**Liudmila Molkova** 10:29 Yeah, I'm presumably…
**Trask Stalnaker** 10:30 on a line.
Yeah, potentially we can align with… in Java.
to that.
**Liudmila Molkova** 10:39 Presumably, disrupting exceptions normally don't modify the message, and if they do, well, it's on them.
**Pellared** 10:54 Shall we move to the next one?
Okay.
So this one is… Proposing this processor.
For adding span events based on the events.
from the logs, which already you implemented in Java here.
It's too queer.
And, I also implemented a similar prototype for Go. There are some reasons that we do not want to merge it in Go yet, but it's not because of the bridge design itself, it's only because our logs API is not stable, and it will be just a charm for refactoring it later, and remembering. It will be, yeah, and it's very easy, so it will be more work… it will be the same work that later to refactor it.
But yeah, I have not created… Others, I have forgotten to follow up.
So there was also missing a queen APR for this, for configuration.
And Udemya already, mentioned that probably it will be a must.
Or declarative computers.
**Trask Stalnaker** 12:27 Is that the different from the one above it?
**Pellared** 12:30 I think it will be the same as here. We can also.
**Trask Stalnaker** 12:33 No, no, I mean, your follow-ups, you've got… is follow-up number.
**Pellared** 12:38 Are you alright?
**Trask Stalnaker** 12:39 3 this year.
**Pellared** 12:40 Alright, so, so it was already here. Okay. Okay.
Thank you.
So, I added these as follow-ups, if any of this is required. So, I can create this as a draft, for instance, don't you want, or…
**Trask Stalnaker** 12:57 Yeah.
I would create that.
No. Yeah.
Cause that… that… I feel like that will help us to then review this PR.
**Pellared** 13:08 There have been some discussions.
And it will be helpful if you look into those as well. I think we have time right now, so maybe I'll just… Yeah.
Scroll here… So, Sijo… I'm not sure what is the reason.
that he's very much concerned about exceptions, and I'm not sure if I understand his concerns correctly, because I think he tried to mention him a few things.
And, one is about, which Jack probably pointed out, that it's about dual pumping.
So I added a separate issue for it, I create a separate issue, so it's not a dual… it's not dual emitted through both locks.
and span events.
So that people can configure it, but I will go to it back to it later. But I have a feeling that still CJ has something that he would like to have something for exceptions and other events, which personally, I do not see a reason why, I think that even right now, users of spans also do not have this way to differentiate easily between a span event, which is an error or not an error. I don't… if… and if people didn't ask for something specific for span… for, you know, span events and span events, which are for exceptions, so I don't know what… if we need anything more.
Yeah.
**Trask Stalnaker** 14:42 So, the… I would guess where CJ's coming from, the thing that I could see… is that exceptions, right, were the most common thing for span events, so that's where people want to come back. At the same time, though, now that we have events, we're starting to popularize them, and… emit them for, like, GenAI events.
And so… Somebody may want to…
**Pellared** 15:21 Separate exceptions and others after events.
**Trask Stalnaker** 15:28 Yeah, although, I mean, in the GenAI example, it reminds me that, I mean, those people wanted… Those events on the spans.
S-PAN events, too.
So…
**Pellared** 15:42 Yes, that's my understanding, that if someone does not have logs, you know, backend, which handles events.
**Trask Stalnaker** 15:48 Right.
**Pellared** 15:48 they would like both at the same time. I tried to capture it here. I believe that people who need it will want to have all events, not only exceptions and spans.
And I…
**Trask Stalnaker** 16:00 Yeah.
**Pellared** 16:02 Yeah, and…
**Trask Stalnaker** 16:03 It would be for, like, Jaeger… I mean… Maybe we can… Yeah.
**Liudmila Molkova** 16:13 But, I mean, if people want only some specific events.
They can first configure it, right? Second, which ones they want to be converted through event name.
configuration.
Or they can build their own processor if they want to be as fancy as possible. Like, we are addressing the common needs, if somebody has very special needs, go build them.
**Trask Stalnaker** 16:51 I agree. I mean, I'm in favor of not overcomplicating It, and… We always have the programmatic hatch.
for people.
And if we get feedback, you know, we can get… we can… we can still evolve.
And handle that could be a follow-on thing based on feedback.
**Liudmila Molkova** 17:22 Wouldn't it be the case that if you provide, let's say, an option to say, I only want exception, like, through the name, event name, if the event name equals exception.
then people install this processor and only capture exceptions, and CGO, whatever concern he has, would be… it would be addressed.
**Pellared** 17:45 For the legacy, but, this span, the event name equals exception.
would be true for the old usages of the… of the SPAN API. For newer, which is… because here we are on the other side. Here we are mentioning trans… translating log-based events into… back into spans, so probably it will be, like, an asterisk, something, you know, suffix with exception.
**Liudmila Molkova** 18:18 Yeah.
Then we can go fancier and add instrumentation, scope, name, into the filter, but that's… that's the future.
**Trask Stalnaker** 18:31 Can filtering be… can event filtering be a separate… Processor in the pipeline.
**Pellared** 18:39 Yeah, so this is something which I initially proposed here.
To create something like a branching log record process, or… Which will… could be, like, you know, if-else, if-else, whatever, that could… Because the filter will be probably, you know, if it fits this, then you want to go this pipeline, and I imagine that probably if you need one, it can be just a block.
not just one condition, but then I thought that when we want to build it, we will need to create a language.
for making comparisons, etc, so I figured, no, it's an overkill for right now, let's postpone it. And so I just closed… I just opened it, and after 1 hour of thinking, I decided to close it.
Because implementing it in all languages will be extremely hard and back-prone.
Yeah, maybe I'm just.
**Trask Stalnaker** 19:28 Yeah.
No, no, that's very fair.
**Pellared** 19:34 And then, And then, because of that, I decided to create another proposal, which is just an event routing processor, which is very simple, Work.
Do I have an example? But this is a very simple one. It just creates a branch for eventName equals empty, or event names has something, so people can differentiate between Event log-based events.
And, you know, breached, usually, breached logs from, from logging libraries.
And then… Someone can use it.
To, for instance, make a no-op for a meeting event, log-based event.
on, using event SDK, but then they can still bridge to the span, to the span. So they are not dual, you know, dual bumping, the, the span events, but if they have the… log SDK configured, for instance, to emit to STD out, then you can have still logs to STD out.
Which they may have right now.
Should I rephrase, or describe it a second time?
**Trask Stalnaker** 20:52 No, I…
**Pellared** 20:54 I know.
**Trask Stalnaker** 20:57 Yeah, but I get, I got the, the picture there.
I… like, it sounds like a good thing, I just want to… not… Do more than we have to… For the span at this point, like, Like, this feels like something… Like, a good future thing, once we start getting, you know, more feedback, and Other people asking for it.
I don't know if we need to do it proactively.
**Pellared** 21:40 That's also why I decided to put it as a separate issue, and not try to tackle the same, so we can describe it separately, but at least we have a path forward, if we have a pushback.
**Trask Stalnaker** 21:54 So, in your current PR, The… does it only… it basically takes anything with an event name?
That's the one criteria.
**Pellared** 22:06 it is interrupt.
It's the exact same implementation, we did the exact same implementation goal, and yeah, we feel this is great.
**Trask Stalnaker** 22:16 I would… yeah, I'm in favor of, anything, more complicated being a future issue. Like, not blocking… not blocking it.
Do you want me to leave a comment?
**Pellared** 22:38 Yes, yes, but, what was this one?
yeah, this was… this is also a separate thing.
Here, CJ was concerned about users who use login libraries and just use auto, hotel event name as attribute instead of the, event name field.
And, yeah, and I said that we already kind of discussed it, that it can be a separate processor. So I created a separate issue if someone wants to have a build name event log processor, which takes the auto event name attribute.
And set it as an event name field.
**Liudmila Molkova** 23:22 Isn't it something that even happens in the bridge before it even hits the API?
**Pellared** 23:27 I think, I think, I think we… I think the semantic conversion says that it's not normative, that someone can have it on the bridge, someone can keep on the SDK, In Go, we didn't want to have… in the Egypt Bridge, if I remember correctly, because we do not want to implement it.
for each bleach, and I think that was the main reason.
**Trask Stalnaker** 23:52 I'm… I feel like it should be in the bridge.
**Pellared** 23:57 So here is just defined SDK component.
Because, question, do you want to implement it in English, this kind of translation?
**Trask Stalnaker** 24:05 I do. I do. Because it is… it's a compatibility layer. Hotel.att attributes are… it's a compatibility layer.
**Pellared** 24:20 Let me ask you another way, if the bridge can't do it, why just the SDK cannot do it?
Automatically.
**Trask Stalnaker** 24:31 Oh, that would be okay with me, I guess, if the…
**Pellared** 24:36 What do you think?
**Trask Stalnaker** 24:37 once.
**Pellared** 24:38 The default, like, you know, the default implementation of.
It will be opt-out, but then you decrease the error… and you decrease the probability that some breach author will forget about it.
**Trask Stalnaker** 24:51 I don't have an initial objection to the SDK doing it.
But in either case, you wouldn't need to deal with hotel event name as a Separate attribute in the processors.
**Pellared** 25:07 Okay.
**Liudmila Molkova** 25:09 It would make sense in the collector, because you can read it from somewhere.
**Trask Stalnaker** 25:14 Right.
**Pellared** 25:17 But his concern was, like, maybe not what's in concern, but if it's on the collector.
Then it's too late.
For our log spanned event processor.
**Liudmila Molkova** 25:31 The assumption?
**Trask Stalnaker** 25:32 So, I mean, yeah.
Yep.
**Liudmila Molkova** 25:34 if, if… something in the application use the hotel event name, and application is instrumented with hotel, then whatever the breach or SDK would take care of converting it to event name. So something coming from the SDK, by the moment it hits SDK processor, I should never see this.
**Trask Stalnaker** 25:56 But the collector would still, like, you might be bridging from a non-SDK, you might have a receiver that's, you know, pulling stuff in, or something that's… Different.
**Liudmila Molkova** 26:07 Yeah.
I think this is, like, maybe we should clarify it. So what we say today, that, It can be used to set the event name field by collector SDK components. Maybe we can clarify that if SDK… Preacher SDK can detect A tele event name. It should.
convert it. And then…
**Trask Stalnaker** 26:47 At the earliest possible time.
**Liudmila Molkova** 26:50 Yeah, the earliest possible time, I like it.
I'll create an issue for some kind, or maybe I'll just… I'm not ready to send a PR.
**Pellared** 27:01 I think it can be done here, in this issue.
No, this is the bad one.
Events routing now.
This one I need to delete.
We're avoided.
**Liudmila Molkova** 27:24 Who would know that the most important skill is to find the least words to explain a concept?
**Trask Stalnaker** 27:37 That has always been true.
**Liudmila Molkova** 27:39 That is, yeah.
Yet, not so many people practice the skill. I think lately, they have been very verbose.
**Trask Stalnaker** 27:53 Yeah, it's getting worse.
**Pellared** 27:56 You can… indeed.
**Trask Stalnaker** 27:57 Well, you just have to prompt, AI to, better, like, give me the answer in, 20 words or less.
**Liudmila Molkova** 28:07 Right, so the model providers, the people who teach models, should optimize for this, right? For being concise. It seems they are optimizing.
**Trask Stalnaker** 28:15 Oh my god.
**Liudmila Molkova** 28:16 against it.
**Trask Stalnaker** 28:17 Yes, I agree.
Yeah, like, the default should be be concise, and then you can always ask it for more information.
**Pellared** 28:31 Alright.
Let's move to the next one, okay? Or do you want to discuss something?
So.
**Liudmila Molkova** 28:42 I have a comment on this one. So, you're proposing some SEMConf attributes for the things that don't exist in the span events. Should we just drop them? So, if people are moving from logs to span events, they want to lose some information.
So why do we want to bridge everything?
**Pellared** 29:05 which you're mentioning, I'm lost.
Sorry.
**Liudmila Molkova** 29:09 the span event bridge, I think you're proposing some subconf attributes, the new one for, like, dropped attributes, count, observed timestamp.
I would say maybe later, if somebody wants, really wants it, but as a start, let's just not do this.
**Pellared** 29:25 I… you mean… vis… This one. -H.
**Liudmila Molkova** 29:32 All of them, even severity.
I mean, you want the carrier that doesn't have a notion of severity, you've got it.
**Trask Stalnaker** 29:45 I agree.
**Pellared** 29:46 Make a comment. Make a comment so I can address it.
**Liudmila Molkova** 29:49 Yeah.
**Pellared** 30:38 Okay, here are my comments, and you can do that shortly here.
**Liudmila Molkova** 30:50 I'm also leaving a comment on the PR.
**Pellared** 30:54 Awesome.
I need to turn on the lights, because I'm getting blind.
Okay, switching to the next one.
set status error, so this is a spec thing, and this is not just about logs.
But the locks kind of… This is kind of a little bit related.
we have a lot of things like that in our Go instrumentation.
And instead of doing it, because this is kind of error-prone, we'd like to have something which is, like, set error status. So something similar to what Trust created for the logs.
And this would also make it… easier.
For people to follow the semantic conventions for spans, which we have been working on, which is this thing here, because The SDK could be responsible for setting the error type, setting the span status description based on the message, etc, etc.
We have no prototype yet, because it has not gone through triage, and I first wanted to get any feedback.
If it is something that we want to pursue.
And this is not needed for the deprecation of spanned events, in my opinion, but it is something which would be just nice to have anyway, probably, even right now for us.
**Liudmila Molkova** 32:43 It's a great ergonomic improvement.
**Trask Stalnaker** 32:51 Can I see the example?
Code.
**Pellared** 32:56 This one? Yep.
**Trask Stalnaker** 33:04 So, it's replacing… Okay, error.type… And… Goddess…
**Pellared** 33:16 Yes.
**Trask Stalnaker** 33:17 Right…
**Pellared** 33:18 This is the description.
Status?
**Trask Stalnaker** 33:21 Yeah…
**Pellared** 33:22 attributes.
**Trask Stalnaker** 33:26 So, set error status.
Set error…
**Pellared** 33:40 I thought about as well.
I have no strong opinion here.
I… here I just proposed status, because…
**Trask Stalnaker** 33:54 And so, in Java, for example, this would be… We would pass in the exception object.
So it's…
**Pellared** 34:07 with exceptions.
**Trask Stalnaker** 34:07 not quite set exception, because we're… I mean, it's… Like set exception?
**Liudmila Molkova** 34:20 Just that exception, right?
for Java, because…
**Pellared** 34:24 You have overloads as well.
You can do this, or not stressed.
**Trask Stalnaker** 34:33 I think some exception would be fine in Java. I don't think we would need an overload.
And by default, like, we would not capture the stack trace, but it certainly would be an interesting option for people who wanted And we have had that request before.
To capture the final exception on a span.
**Liudmila Molkova** 35:05 Yeah, the Omni fan…
**Pellared** 35:08 this proposal, I created this issue because we have exactly this ask.
in the Go SDK, to add the configuration to the Tracer SDK, so that this set, which, right now we have this set error record, which creates span events. They want you to have stack traces.
And that was the reason when I created it, because I thought, if you would like to have it, then I would rather want to have first this thing, so first transition to the new types of error recording, and then, if we ever wanted to have the stack traces, then it should be in SDK configuration.
Optin from, possibly.
**Trask Stalnaker** 35:50 I like it. I think just the set exception being the parallel of… I mean, I guess the only thing that's kind of nice about setError here is that it's… Setting it as an error. Like, the status code is error.
so… I think… that is reasonable. It's also sort of like saying, I'm setting this spam as an error, noting it as an error. That's kind of, like, the most important thing I'm doing… So, I like set error.
**Pellared** 36:32 Okay.
**Liudmila Molkova** 36:32 the only small concern I have about it, and it's solvable, but, like, typically, when we report spends, we also report metrics next to them, and error type is shared.
So imagine I pass that error to this pen, and it calculates error type, but I need to calculate it independently for… metrics.
And there is a chance of inconsistencies. The instrumentation API solves it to some extent. Like, if you have a… a higher level that does both traces and metrics. And it's slightly… Inconsistent.
**Trask Stalnaker** 37:20 Yeah, so, for example, we wouldn't use this shortcut in Java, because we already have a higher level API that we would calculate the error type once and stamp it on both.
**Liudmila Molkova** 37:36 But you would… We'll want to use the abstraction so that People can customize stamping exception information on the span… the span ending exception, so…
**Trask Stalnaker** 37:48 Newspad.
**Pellared** 37:51 I remember that in one of the… on the… in the implementation of the bridge, for logging.
enforce that error.
we have… We are doing… No, it's in this… I think it's in this decay, maybe even.
That is the attributes set I think the attributes have, purity.
over-calculating if it's set, you know, on the field. So, if a breach says the attribute error.type. It will not calculate the same attribute again.
From the error.
So we just pass the object, you know, if you want to have this Ludomiya, you know, this optimization that you calculate this error type once, error type only once, you can pass it on attributes or signals, even though you set the error.
But, and the SDK will see, okay, error type is already set, we do not need to calculate it again from the error object. I think we have it implemented.
**Liudmila Molkova** 39:00 Yeah, I'm not… I don't really care about duplicate… oh, sorry, recalculation, it's trivial, right? I mostly care about that, okay, there… there is some logic that sets error type inside that method, but it can be different logic that sets error type for the metrics.
**Trask Stalnaker** 39:22 So it could also have an optional PRAM For error type, to pass to setError, and pass in… Both the exception and optionally error type that you've Already calculated.
**Liudmila Molkova** 39:43 Yeah, the alternative is that… Okay, there are two alternatives. First one…
**Trask Stalnaker** 39:49 That doesn't strip… that doesn't do the unwrapping that we've been… Oh, but that's not at the SDK level anyway, that's an… okay, sorry, go ahead.
**Liudmila Molkova** 39:59 Yeah, so, another alternative is that should have convenience APIs for metrics as well, and they can take exception.
2?
This is a very long… And questionable path.
We can have, Sdk-wide.
Help her.
that populates herotype from exception, but that's the hotel, and… yeah.
**Pellared** 40:39 I think this is something which David Ashpole will be very interested into exploring, because I remember that for the bound instruments.
the most… Problematic things are the error types.
**Liudmila Molkova** 40:53 They are the… the highest… the cardinality, probably. The most dynamic.
**Pellared** 41:00 I mean, not… yeah, they're causing the dynamic that you need to sometimes need to have more attributes, someone's not.
And yeah… And I'm not sure if maybe adding something additional on the… On the instruments, we'll… on the API surface, maybe it will help or not, but I think it may be worth discussing with David, maybe, not sure.
I can try it on my own, but maybe also worth discussing it on the TC.
Cool.
**Liudmila Molkova** 41:34 Yeah.
I'm thinking if we generated code for metrics, we would generate the record overload with exception.
**Pellared** 41:45 Type. Yep.
**Liudmila Molkova** 41:46 And then whatever internally happens, we would call some utility that creates our type from… from error.
I don't like exposing GoodHill APIs and SDKs, because, like, this global static shit.
So maybe we can find some good shape for that one.
**Pellared** 42:09 Okay.
**Liudmila Molkova** 42:16 But, I mean, like, I think these problems are solvable, and I really like that this pen and… does all this logic together. I don't want to take error typesetting away from it.
But maybe, yeah, like, it… it… we should check if our… can we check if error type is already set? We can in the SDK, right? We… we don't… like, if somebody set error type before that, we should not overwrite it.
**Pellared** 42:48 Yeah, I think that's what we were doing in Go SDK already.
**Liudmila Molkova** 42:57 So, like, if you're an instrumentation, you're ready to write some boilerplate, you would do… you would calculate error type, you would set it on span, you would set it on metric, then you would end the span.
And, and if you're a user application, you just want spans, you want things simple, then… It's… it's already perfect.
**Pellared** 43:25 Race. No.
**Trask Stalnaker** 43:32 Yeah, and I could see, again, having that error type as an optional param on set error, since… especially in… Since we're also looking at instrumentations, unwrapping, doing the unwrapping, For… specifically for ArrowType.
**Liudmila Molkova** 43:53 Yeah. Would instrumentations do unwrapping? Well, they would do some, right, specific ones to them.
but also… The SDK would do the unwrapping for common ones.
**Trask Stalnaker** 44:08 Oh, is that where we landed? I forgot.
**Liudmila Molkova** 44:11 I think we'll end at that.
**Trask Stalnaker** 44:14 Is that what you all are doing, Robert and Go?
is unwrapping in the SDK itself.
**Pellared** 44:21 Yes, yes, exactly.
And now I also checked that, yes.
the processor before it goes to the processor. The log records, we are checking if it has any exception attributes.
And if it does not, then we are adding this exception attributes from, you know, calculating based on this.
On this logic here, error type.
So someone…
**Liudmila Molkova** 44:47 Then check for type, though, right? If it exists.
**Pellared** 44:51 We… I think it's exception, I think it's exception type, yeah.
Here.
Where was it? Exception type key, here.
**Liudmila Molkova** 45:09 Okay, anyway, so, like, I think, like, the…
**Pellared** 45:12 dear.
**Liudmila Molkova** 45:13 the… I think we should check if error type is set and not set.
But maybe you only check for the exception.
**Pellared** 45:21 Yes, we don't need protection.
You are right, we do only for exception, but this is for locks. The lock, I think the locks, I think the log semantics only tell you right now about exception type, and exception.
**Liudmila Molkova** 45:36 Yeah.
**Pellared** 45:37 So, if this would be implemented in, you know, Span SDK, this is not a prototype, we're just checking existing code, then we'll change it to error type.
**Liudmila Molkova** 45:46 Yeah.
**Pellared** 45:48 I was just checking if you have some precedence already for it, and we do.
I'll try to make some notes…
**Liudmila Molkova** 46:47 And I like Trask's suggestion to have it as an optional param.
**Pellared** 46:55 Optional parameter to set, to…
**Trask Stalnaker** 47:00 error.
**Pellared** 47:04 advertisement?
**Liudmila Molkova** 47:05 this… Y-yeah.
Not to overwrite. Oh, that's a good question. Not to overwrite ever, but to set it.
To something that's not exception type.
Because there are many cases where you want it not to be exception type.
**Pellared** 47:32 So, the question is, do we need it? Do we need it?
If we already have this one.
Or you still want it for convenience?
**Liudmila Molkova** 47:44 I think it's a good convenience that all the error-related things are said together, but it's, like, not super strong opinion.
So if it sets error types, sometimes.
And it would rather set it In all cases.
Given the user provided.
**Pellared** 48:08 won't always…
**Liudmila Molkova** 48:09 nation.
**Pellared** 48:10 I don't know what it's like… Yes.
Exception.
Runtime.
Have I captured… good enough?
**Liudmila Molkova** 49:02 Yeah, I think so, yeah. Thanks.
**Pellared** 49:04 Okay.
still look at this PR as it may, it may contain some language and stuff, which also may need to be addressed, yeah.
It's longer than this one.
**Liudmila Molkova** 49:25 It's pretty cool, I love it. I miss this method a lot. Nobody does it right. Like, if you look into some random instrumentations out there, nobody does it right consistently with what we recommend, and I understand why it's too hard.
**Pellared** 49:39 Yes.
Okay.
I've stopped sharing my screen then.
Any other things that, we should look at?
Anything from the Gen AI… Gen AI world?
There's no comments.
**Trask Stalnaker** 50:03 I need, I need, I need some… Recovery time, still.
**Liudmila Molkova** 50:09 Robert, would you host Gen AI Instrumentations and GoCon trip?
**Pellared** 50:15 We hope… that, if, if Nikola or other staff in Obi do the semantic… do the instrumentation on the Obi side, then the Obi standard.
**Liudmila Molkova** 50:31 They, they do, they actually have… trust, we have eBPF instrumentation for, for, like, the model calls. Anything that goes on the wire for OpenAI, I think on Tropic, maybe something else, it captures, GenAI conventions.
And I think this is our ultimate answer to everything inference. It would not help with Agentic stuff, because it's essentially not the protocol, right? It's not… Linux kernel doesn't know about anything that happens inside the application, and it… it can forgo, though, right?
For a girl, we can do something.
Yeah.
But, like, there should… Layer in the application.
**Trask Stalnaker** 51:13 There's also the Go CompileTime instrumentation that, Huxing, mentioned last night in the JEMA APAC meeting.
**Liudmila Molkova** 51:23 Oh!
**Trask Stalnaker** 51:23 Because he's involved… he's involved in that project also.
**Liudmila Molkova** 51:27 Oh, nice!
Cool, that's even better.
Cool.
Let's have 7 minutes back.
**Trask Stalnaker** 51:40 Yeah.
Thank you, Robert.
**Pellared** 51:43 Thank you.
Phew.
**Trask Stalnaker** 51:45 by…
