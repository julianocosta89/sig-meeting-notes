SIG: Event WG
Date: 2026-02-10
Duration: 57 minutes
Zoom Recording URL: https://zoom.us/rec/share/ofQy5cN3c9t6J04fsFuJ4xgeWYkY1hKS6wSllO0hc3HPdXZddj7kIUC9MdcVYErs.DtQNSbssz8BjZ6Ys
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:57 Hello, hi, Trask.
Long time no see.
I can hear you.
Oh, no, now I can?
**Trask Stalnaker** 01:12 Probably. No.
**Liudmila Molkova** 01:14 Yeah. I was…
**Trask Stalnaker** 01:17 amazed at how many people, I mean, go to the LLM meeting.
**Liudmila Molkova** 01:24 And it's pretty consistent.
It's also not easy.
**Trask Stalnaker** 01:32 Yeah, a lot of, a lot of competing priorities.
**Liudmila Molkova** 01:36 Yeah.
**Trask Stalnaker** 01:37 Sounds.
**Liudmila Molkova** 01:40 That's true.
Okay, is Robert around?
**Trask Stalnaker** 01:50 I… oh, he's got, out sick emoji.
**Liudmila Molkova** 01:57 Oh… I know.
Okay.
**Trask Stalnaker** 02:04 I'll share, give you a break. I know after, I'm always exhausted after the JavaSig meeting.
**Liudmila Molkova** 02:15 Yeah, I need, like, 10 minutes to get back to my head.
**Trask Stalnaker** 02:27 Let's… Let me do a… Job of notes… So, first topic I want to discuss is… Event… what to do with the event body?
**Liudmila Molkova** 03:08 Yeah.
**Trask Stalnaker** 03:12 So… Yeah… I… Yeah, I was having second thoughts about… my suggestion.
And… thinking that… It might be a… a more useful… A more useful story if we say that event, body.
Should… if it is used, it should be a string, it should be a display message.
**Liudmila Molkova** 03:52 Yeah, it would be a better story.
And… Done.
It would mean… That the body itself like, HTTP request body would… be either a stringified version, Or… Like, let's say you record HTTP request.
body. Event.
you would… The body stream is not the display representation of this event, right?
It's an attribute.
**Trask Stalnaker** 04:33 Right.
So, I mean, it… it can be… an attribute is fine. I think the only reason we were thinking in the past about using body for it Was this idea that back-ends might have special Consideration for length of bodies.
**Liudmila Molkova** 04:58 Yeah, so, like, this… Thing.
We are suggesting. We will face Problems from the backends.
And I'm… I think this is the right thing.
To do, to put it as an attribute, even though it's big, because otherwise everything falls apart, right?
No assumptions could be made.
Maybe we should do… More advertising of the thing.
So, I've had a bunch of discussions. It's not strictly related to logs, but I'm curious what you think. I've had a bunch of discussions over time about the The story we've done in GenAI was tons of content and attributes.
**Trask Stalnaker** 06:02 Yeah.
**Liudmila Molkova** 06:04 And we kinda… push through the backends, the backends who want to support GenAI are forced to support these long attributes.
And… there is a big interest, at least I see it in my world, of, like, uploading this content somewhere else.
**Trask Stalnaker** 06:26 Oh, yeah, yeah.
**Liudmila Molkova** 06:28 Google is super interested in it, they are doing some real-life uploading in there.
**Trask Stalnaker** 06:34 Mmm…
**Liudmila Molkova** 06:35 Somewhere in their infrastructure, and they actually get a good feedback from their corporate users, that that's what they want to separate control over this data.
**Trask Stalnaker** 06:48 That's a great… I do think that really ties into this, though, because that… that gives us… basically, we can say, hey, that's the long-term direction.
that attribute.
We would support some kind of attribute ref thing.
And… Cause, yeah, I mean, it doesn't… really matter that much if your enormous thing is in the body versus in the attribute. It's… More about whether you can side-channel it out of your Standard telemetry stream.
**Liudmila Molkova** 07:25 Yeah, and, like, the body only solves the problem for… a little bit better than attributes, right? Not… it's not the…
**Trask Stalnaker** 07:35 It's an indicator that they can use to know what to side-channel.
But if we could have… Some kind of reference attribute.
**Liudmila Molkova** 07:51 Yeah.
**Trask Stalnaker** 07:52 Would that be either cement… I mean, we could probably get away with Just semantic conventioning it, in terms of, like, saying that if it ends with .RAF, and it's, like, this… format, maybe even a complex attribute, I don't know, something that you wouldn't see normally.
If we don't think we can get it into the proto.
**Liudmila Molkova** 08:20 Yeah, so the ref thing turned out to be even more interesting. So there are people who say, oh, I don't want to ref the whole thing, I want to ref some part of the complex attribute, and then semantic conventioning, it becomes a little bit harder, but still possible.
the feedback I've heard from Google folks, that they actually would like to see it more formal and part of the product.
But I don't believe, like, this comes anytime in the next year or two, or I don't know. It's a huge problem.
But it probably should eventually come, because it's also useful for profiles. They need symbols, the crash dumps, thread dumps, memory dumps, all this stuff, wood.
be useful to sense through this, whatever, side channel for large, binary, sensitive, whatever.
But it's just a very huge unknown area. We are nowhere close to start working on it.
**Trask Stalnaker** 09:29 Just sort of to help me complete the picture.
I didn't quite follow the refine-only sub-pieces of a complex attribute.
**Liudmila Molkova** 09:45 like, imagine.
**Trask Stalnaker** 09:46 I mean, I guess I understand the… the request, but, like, what's the… the context there? Like, why.
**Liudmila Molkova** 09:57 Like, you might want to say, okay, I… there is this chat history with my agent, and there are pictures there. I only want pictures to be roughed, but the text can stay.
**Trask Stalnaker** 10:18 Are the pictures… I see… as opposed to, like, in some, like, thinking JSON schema, Base64, a huge Base64 attribute in there?
**Liudmila Molkova** 10:31 Yeah.
**Trask Stalnaker** 10:34 I see.
Okay, that makes sense. Thanks.
**Liudmila Molkova** 10:40 Yeah. And then coming back to it, it sounds like we both… are fine with… Having some heat and explaining the long-term story is separate storage or separate signals for large things, and this way, attributes are kind of acceptable.
Out of bed, yeah.
**Trask Stalnaker** 12:13 Sweet!
**Liudmila Molkova** 12:15 Yeah.
And it's actually somewhat a cheap promise to make, right? It's semantic conventions only.
And there is a way out of it, if it turns out to be… a bad decision.
Yay.
**Trask Stalnaker** 12:38 Alright, oh yes, I think we've… We've, Closed on that. I was very happy with your suggestion.
Let's see… I think the… yes, the open question remaining there, is… attributes.
Stamping other attributes.
Oh, so I did add, I don't know if you saw, I did add severity. I think that's good to… So worth… Reviewing what I said, I'm proposing error.
Since they align with SPAN, Status, error.
**Liudmila Molkova** 13:41 Although…
**Trask Stalnaker** 13:42 There's definitely an argument to be made for Warren.
**Liudmila Molkova** 13:51 So… How would it tie to our discussion of filtering?
Exceptions and stuck traces.
So we wanted to tell your severity As a guiding principle on maybe when to record stack trays.
**Trask Stalnaker** 14:16 Oh… Yeah, and so… For server ones… That's probably more clear. On client ones, yeah, it's… Maybe less clear because of, like, retries and things that… yeah, okay.
**Liudmila Molkova** 14:39 Yeah, I mean… We have a choice, like, we… Would say that… Well, it's really hard to build a processor on logs that would take the parent's mankind into account.
So, like, we could say that depending on the parent's penkind, you could rewrite the severity or derog the stack trace, but…
**Trask Stalnaker** 15:16 Yeah, no, I like… I mean… I think we… I do like… I forgot about the whole… story of not recording… Unless they are… R, like… Not recording them at error level unless they don't have a parent Span that would bubble up.
And possibly get handled.
**Liudmila Molkova** 15:55 So… The client should be warned, or info.
Probably.
Good morning.
**Trask Stalnaker** 16:10 Do we even… or deb- I mean, debug?
**Liudmila Molkova** 16:14 Good question, yeah.
**Trask Stalnaker** 16:19 That's where I thought we were… We… or at least, actually, the head… I think that's where I was leaning in your earlier OTEP.
**Liudmila Molkova** 16:32 There, it was not, I think, not higher than… worn. It allowed… anything on… under… it got… Equal or under 1.
**Trask Stalnaker** 16:46 Okay.
**Liudmila Molkova** 16:48 But… And if this is debug, than… Everything else should not ever be logged at all.
Like, we need some… some range, right?
It's like the fact that HTTP request is made could be a useful event.
It would need to have lower severity than the.
**Trask Stalnaker** 17:17 Gotcha.
**Liudmila Molkova** 17:17 has happened.
**Trask Stalnaker** 17:19 That's fair. I mean, Warren is… The key is not making it an error.
Errors…
**Liudmila Molkova** 17:33 Yeah, and it's not a bad thing to require the exception, especially if… It's… It does not include stack trace. If you could drop the stack trace on it, then… It's not a problem.
**Trask Stalnaker** 17:50 I see. Thinking of it more from the distributed tracing perspective, yeah.
Yeah, it's very interesting from a… My span was sampled in.
And so maybe that is what… People could do on… They could sample Warrens.
at… Trace.
**Liudmila Molkova** 18:17 Hmm…
**Trask Stalnaker** 18:18 trace-based…
**Liudmila Molkova** 18:22 Yeah.
**Trask Stalnaker** 18:24 But errors say I want all my errors.
**Liudmila Molkova** 18:28 Right, yeah, that's another great distinction.
I think that's what we've done.
In Azure SDKs, we've used Warren for exceptions, and… In for a debug for things under.
It's, like, people still complain, because they tend to enable warning above.
**Trask Stalnaker** 18:55 Yeah.
Or even info. We've had complaints, something in Java, we were logging it.
Or at info level.
And, that was… too… verbose.
**Liudmila Molkova** 19:19 So, we can… Put something here.
And we maybe can create an issue to follow up on the feedback, or collect feedback, because if we put something… whatever we put, worn or in.
**Trask Stalnaker** 19:32 Oh, yeah. Yeah, yeah, yeah.
But I, I like… Trying to get some fully solid… That's why I didn't want to postpone some of your comments till after the PR.
Damn.
**Liudmila Molkova** 19:58 And this is server, this is fine, right?
**Trask Stalnaker** 20:01 Thank you.
Do we want to say something?
about… I mean, because you can't have nested service bands, and you could have a client span that doesn't have a parent.
Do we want to say… do we want to make it apparent?
Based Choice…
**Liudmila Molkova** 20:32 Mmm.
If this logic… Makes sense, too.
Record… logs dis… Record exceptions.
on… raw local root spans.
Would it make sense for it to be a separate component?
Rather than doing it in every instrumentation.
Like, you can have a processor.
that… that promotes… All exceptions.
to errors if there is no parent span. If there is no… if the parent is local root.
**Trask Stalnaker** 21:33 Can you… from a… from the log record… Can you traverse? I don't know if you can traverse to the… I don't know if you can get that… Oh, I guess you can get this band contacts, which… okay, I think you can. I think you can.
**Liudmila Molkova** 21:53 If you can get the current span.
**Trask Stalnaker** 21:57 I don't know if you can get the current span.
**Liudmila Molkova** 22:00 I mean, you can, but it's not guaranteed to be there, because you could just stamp the context.
Yeah.
**Trask Stalnaker** 22:17 But I think you can get the full span context in the log.
processor… At which point…
**Liudmila Molkova** 22:29 Do… do you require log records to… Have span context? Can't you just set trace ID, span ID, and flags instead?
**Trask Stalnaker** 22:43 Oh… Probably… I don't know, we probably… Yeah, we probably… Have it reference spam context.
But that may not be for spec, but also, I don't see Para…
**Liudmila Molkova** 23:09 the parent SPAN ID is under SPAN, not on the context, because… You don't need to propagate it.
So you need a span instance to know, yeah.
**Trask Stalnaker** 23:23 Yes.
**Liudmila Molkova** 23:24 So, it's maybe doable, but not per spec, and would not be guaranteed.
**Trask Stalnaker** 23:32 Right.
**Liudmila Molkova** 23:34 Yeah.
So if we don't, like… the… the cons is the complexity of our instrumentations, right? The pros that it's better story for users, if we don't do this.
We set severity to what our info weren't… And on the client's pants.
And then… Users who don't have an outer span, or they're… client operation.
They probably don't get a great experience.
**Trask Stalnaker** 24:24 Anyways. Anyway. Yeah.
And then, so, conversely, on the server side, as far as nest… I mean, nested server spans… Art.
super optimal.
Anyways, so double recording… That as error on both of them is… Probably okay.
**Liudmila Molkova** 25:02 And it's okay for instrumentation to provide a better Story, right?
**Trask Stalnaker** 25:13 Yeah.
Just trying to think forward to if we want to kind of make this a… general… Story… Across all instrumentations.
That… You do some local… Check if you're a local route or not.
Unless, I mean, we could say for, like, internal spans, and we… Or we can lean into the span kind.
So…
**Liudmila Molkova** 26:00 Yeah.
**Trask Stalnaker** 26:01 We can say internal spans. Once we, solve the background job.
Problem, and say that internal spans really should be, like, Internal to a trace.
Yeah, and I've never, never really liked the original decision. We had to kind of work around that anyway, because for Azure Monitor, we wanted that to be displayed as a server.
local route span.
**Liudmila Molkova** 26:38 Yeah. So, like, if it's client.
It's 49 for whatever, if it's… or if… or producer, if it's… server, a consumer, it's an error, and if it's internal, who the fuck knows? Because nobody knows anything about internals.
**Trask Stalnaker** 26:56 Yeah, yeah.
Debug.
**Liudmila Molkova** 27:00 Yeah. Not… just not documented, because eventually, I don't know.
**Trask Stalnaker** 27:06 Yeah… Yeah, I mean, we're not really defining any… internal… So in Java instrumentation, the most common is, like, controller spans, which are opt-in now, thankfully.
Yeah.
**Liudmila Molkova** 27:25 in Gen AI, we… we are defining them, because we… We are having this layered story, and, like, orchestration of agents is.
**Trask Stalnaker** 27:34 Right.
**Liudmila Molkova** 27:34 Internal operation, which has some layers under. And it's not the server or consumer, it's something in between.
But, they… Let's kick down this… this problem down the road.
**Trask Stalnaker** 27:59 I mean, my only thought of tying into this discussion is… If we… like, it's a similar problem to me to the client. I mean, the internal ones are similar to me to the client.
**Liudmila Molkova** 28:18 one.
**Trask Stalnaker** 28:20 But I guess… Yeah, thinking about, like, the Java instrumentation today, we stamp Exceptions on all the internal spans.
And we haven't really gotten pushback.
I know in our distro, we do… Actually, well, we did get pushback in our distro from our customers, and we did, Do some deduplication and do that local parent.
strategy.
But as long as the internal ones and the client ones are worn, That feels like a pretty… clear distinction.
That you could use.
To filter them out.
**Liudmila Molkova** 29:20 It brings an interesting point. So, in Java Agent, you suppress internal spans, right? You have the… Option to suppress them.
**Trask Stalnaker** 29:31 We don't, we don't emit them. We turned off all the internal span-producing telemetry by default in 2.0.
**Liudmila Molkova** 29:43 I see. And this… Would this… Suppress this event as well.
**Trask Stalnaker** 29:51 Yes.
**Liudmila Molkova** 29:53 Yeah, so the whole instrumentation layer is suppressed.
**Trask Stalnaker** 29:58 Yeah.
**Liudmila Molkova** 29:59 Okay, that, that's good.
And then if somebody didn't care about this operation, they would also get the exception log for it.
Should we somehow… Explain it here.
In semantic conventions?
Well, we don't have a concept of suppression defined in semantic conventions.
Or instrumentation as a whole.
**Trask Stalnaker** 30:33 Oh, yeah, but it's coming, right? We have the, now, configuration-based, like, is trace enabled?
Stuff.
So, like, if you're… Trace is if somebody does the configuration thing to disable your named tracer.
**Liudmila Molkova** 31:05 Right, and then they would probably disable also your named meter and blogger, which is the same.
**Trask Stalnaker** 31:13 Okay, the same name. Yeah, yeah, yeah.
**Liudmila Molkova** 31:16 Okay, yeah.
**Trask Stalnaker** 31:17 That works.
**Liudmila Molkova** 31:18 Yeah, and then it kind of gives users the… enough knobs, and… yeah.
Cool, so then let's not think about it. So you're thinking.
Documenting the principle, or at least… Verbalizing it, that the internal spans and client spans would have the same Severity.
For the exception events.
**Trask Stalnaker** 31:46 Yeah, I wouldn't include internal spans at all in here, I just want to make sure that whatever decision we… Put in here aligns with what we want to do.
**Liudmila Molkova** 32:02 I have a PR to… document the… Severity, guidelines, and naming.
And I can reflect it there. I can mention internal or not mention it at all.
I was thinking you remembered by heart.
**Trask Stalnaker** 32:26 I think there's 4 per, and so I'm guessing it's… But, yeah. Yeah.
Again, this was on the… oh, no, I put it in the wrong place again.
Client… Okay.
I'm pretty happy with that, let's a… Throw something against the wall.
**Liudmila Molkova** 33:14 Yeah, I… I would be… I always have this internal debate about exception versus error.
But it sounds like Go and Rust are all leaning into using exception anyway, so probably not a deal.
**Trask Stalnaker** 33:29 Yeah, I was pretty happy to hear that.
That it wasn't, like, a big… as big a problem as I was thinking it was.
**Liudmila Molkova** 33:41 Yeah.
Cool.
**Trask Stalnaker** 33:45 So last question is attributes.
So, I mean… We've got, like… Error.type… And there's all the HTTP, like, http.route, HTTP URL… There's lots of things that… Would be useful to be able to… Slice your exceptions on.
I'm just hesitant… because of… prior art with… Leaned to not duplicating.
When we have… Now, this is across the different signals, so… It would be fair to revisit to have a different Decision or pattern or convention in that case.
It's definitely harder. I'm not really too worried on the back end, because I think that We more or less assume backends need to be able to correlate this stuff.
But pipelines… There's… some… Interesting things that it enables.
Like, exceptions to metrics, pipelines…
**Liudmila Molkova** 35:24 So… on the duplication.
If you… have spans.
If it's sampled in.
You're kinda… Probably prefer not to have duplication, right?
But if it's sampled out, Then maybe you'd rather have more information.
on the event. It's super complicated, right?
To do, in practice.
But I'm thinking, okay, there probably is a lot of information we can add, depending on, like, how it flies in the real world.
And it would be fine, it wouldn't be breaking.
The one thing, like, the, the, the… Contract that we have, that error type is common across signals.
And it indicates… an error.
Should we put it on the server's bench?
And it would capture the… the response code, probably. Or the re… like, the actual reason, not the exception type, but the actual reason why it… Failed.
**Trask Stalnaker** 37:07 On server spans…
**Liudmila Molkova** 37:10 Because it's an error.
Sorry, on the HTTP server request exception.
**Trask Stalnaker** 37:28 Right, I just was writing myself, what error type?
is for… Server spans…
**Liudmila Molkova** 37:46 It could be the same if it's the list, it's all we know.
**Trask Stalnaker** 38:01 Fails with an error before response… Status code was sent.
So, in practical, trying to think of, like, Java instrumentation, it seems like it would usually be the exception?
**Liudmila Molkova** 38:29 Could usually be the… Status code.
Because this is the… More frequent than… Exceptions, right?
During a HTTP request.
**Trask Stalnaker** 38:43 Right, right. On an exception, if an exception happens, and we create an exception record.
Would error type always be the same as exception type?
**Liudmila Molkova** 39:00 Oh… Right.
Yes.
Do it always be the same?
Well… Unless… Unless… I think in .NET, they have this additional information on the exception that tells you, that breaks it down into readable things, but yeah, that's probably an exception case.
**Trask Stalnaker** 39:28 Right.
**Liudmila Molkova** 39:32 Yeah, so it pretty much… for the majority of cases, at least in Java, we would see error type to be the same as exception type. Not so very helpful.
So, if I summarize this, then without, like, if PAN is not recorded, for whatever reason.
This exception is a little bit useless.
**Trask Stalnaker** 40:16 Yeah, I feel like sampling is a big… Is a big deal here.
Especially on… Server spans… Where… Severity level error.
And maybe that could be a determining factor, or if we copy over attributes, is, like, if it is error.
If the severity level is error, then… You should copy over… Span attributes… So that they survive sampling.
**Liudmila Molkova** 41:06 There is another piece.
So… So there… there is this… Common theme that Okay, if Spanish sampled out, and we still want to record something, we record it as a log.
Essentially, record the… the… Pan.
Azure log.
And if we record span as a log, then this event becomes HTTP client request.
With severity, error, and exception.
attributes.
But then it's recorded.
All the time.
**Trask Stalnaker** 42:01 Tell… tell me more about, Because that feels too much like a workaround to not having tail sampling.
This idea of not… like, if you… if a span is sampled out.
But then you want it anyways, recording it as an error. I mean, record it as an event.
**Liudmila Molkova** 42:33 That's a good point.
**Trask Stalnaker** 42:42 And not that that's a reason not to do it, I mean, tail sampling has its problems, for sure, and isn't an option for… A good number of people.
**Liudmila Molkova** 42:54 It's probably more of a… Okay, let… let's have a… Trace to logs exporter.
Than defining this event.
Right, and then we're traced to something where it's shipped to store, or any…
**Trask Stalnaker** 43:14 Right, right.
**Liudmila Molkova** 43:16 Yeah.
okay, let's forget about it.
Yeah, so Don… What you're saying, that the error severity could be… The factor that Adds all the things to the exception event.
We can say that we kindly expect this event to be sampled Along with Spence.
For the time being.
**Trask Stalnaker** 43:53 Yeah, I mean, and if people want their… They… if they want their… Traces for errors. They can do tail sampling.
**Liudmila Molkova** 44:07 Yeah.
I'm kind of excited about solving these problems with the… with the recording things on logs when they're not present on spans, but I think It's just cautious that we are trying to find the replacement for span events, right?
And we haven't yet the feedback in the past that we actually won the SPAN events in absence of SPANs, the exceptions.
Did we?
**Trask Stalnaker** 44:44 I mean… I think that we have… I think that we know that a lot of people, especially coming from classic logs, want… all their errors.
And so this…
**Liudmila Molkova** 45:08 Splitting the signal.
**Trask Stalnaker** 45:10 Recording exceptions as… as events now.
gives, that… It's the common, like, I mean, it's a… like, the common request, right, is I want all my… traces, but only when they're errors. And… So, short of tail sampling.
Okay, well, at least you get your errors now for these things that were sampled out.
**Liudmila Molkova** 45:46 Great. Can I…
**Trask Stalnaker** 45:49 There's the default question, there's also a question of if it… Would make sense just as a configuration knob to… Somehow.
**Liudmila Molkova** 46:01 Yeah, so the configuration knob is… weather… you want… Additional details on the log?
And… Second one, whether it's… A question of… Severity.
kind of Taganel, mostly.
So what is the condition you want your, the extra attributes on your log?
And it could be severity-based, it could be sampling-based, it could be something else.
And then, what if we say… Here.
That… The exception attributes are recommended, required, whatever.
And we could list other Span attributes there as opt-in.
**Trask Stalnaker** 47:15 Yeah, I always struggle with whether we, like, what's the point of adding attrib… Adding attributes explicitly as opt-in, when they're sort of all… opt-in.
**Liudmila Molkova** 47:29 I think the guidance to instrumentations, like, okay, this is the bare minimum, this is the one step extra, and everything is… Party on.
But yeah, we… huh?
**Trask Stalnaker** 47:46 What about, saying, like, instrumentation may… Stamp all of the… Span… captured span attributes.
Onto logs, or may provide an opt-in As opposed to listing all of them.
**Liudmila Molkova** 48:15 Yeah.
Yeah.
**Trask Stalnaker** 48:29 And then there's… I mean, we can also… Go with this.
**Liudmila Molkova** 48:42 Yeah, I think it's the choice between, like, how to document it in the least.
Verbose and confusing manner.
Yeah.
I kind of feel that, like, if we want to go down the road of, okay, let's add span attributes, we probably… wouldn't.
Include all of them.
like… Who cares what was the network local address on an exception log?
Maybe this was a question for Spence as well.
**Trask Stalnaker** 49:23 Do we capture that? Is that, recommended?
Oh, it's opt-in.
Okay, yeah.
**Liudmila Molkova** 49:30 That's good, yeah.
**Trask Stalnaker** 49:33 Yeah, I mean, I feel like our span is… Like, if it's useful on the span, why wouldn't it be useful on… an exception.
If you didn't have the span.
**Liudmila Molkova** 49:52 Yeah.
Yeah, probably.
Okay, so I like the idea of, okay, if, You, you can… your, your instrumentations may… Include… attributes… that are… Defined for the span.
The rule of thumb.
**Trask Stalnaker** 50:51 Okay, cool. Yeah, because, well… Think on that, also. Some more… Hmm. Yeah, yeah, yeah, I'm excited this stuff is kind of… Starting to get… more concrete.
**Liudmila Molkova** 51:17 You were asking if there is, if there are other prototypes.
for…
**Trask Stalnaker** 51:23 Oh, set exception.
**Liudmila Molkova** 51:25 Yeah, there is nothing in Python. If we need it, I can spend some time on doing it.
**Trask Stalnaker** 51:33 Not a priority right now, but… Yeah.
At some point, yeah.
Thought would be… useful. I think we'd… Yeah, I'm just trying to not… I'm trying to stabilize things in Java.
**Liudmila Molkova** 51:49 Yeah.
**Trask Stalnaker** 51:50 And not lose track of those things.
**Liudmila Molkova** 51:52 Yeah.
**Trask Stalnaker** 51:56 While I have you… I was thinking about this some more, and… Take a look at this.
Think… Don't need to give feedback now, but, I am interested in… Trying to… Figure out a… path forward as we… For the declarative configuration scheme that we come up with.
I'm fine with, you know, for… the whole, where did it go? The back compat, basically… Supporting the list thing.
Yeah, this.
That makes… Since I think that's a no-brainer from a portability perspec- back-compat perspective.
But for the, the… new path.
It feels like a nice… chance to… think through… The feedback we've gotten about our simple Stability opt-in, and what we would… I think it kind of ties into… it might tie into the… Stable by default, OTEP, on the…
**Liudmila Molkova** 53:42 Thank you.
**Trask Stalnaker** 53:42 And that, yeah, that there was some, like, how could this be standardized?
I don't know if… Yep.
I'm just thinking about SEMCOMS, but maybe there's… maybe it's broader than SEMCOM, even? Like, as you mentioned, collector components.
**Liudmila Molkova** 54:03 Yeah, I think at least at some point in the top, there was a proposal to, like, have some flag that enables experimental features.
And in a sense, like, the GenAI latest experimental is exactly this.
So could it… would it make sense to decouple?
There's two parts, like the version.
And if you enable experimental things on top, like two flags, not one.
**Trask Stalnaker** 54:33 Oh, yes, yes, I know what you're saying.
Yeah, we have lots of experimental… opt-in-y things in Java.
So what would you… do…
**Liudmila Molkova** 54:49 So, like, The first is… I don't know the version.
And the second one is… The flavor, the… if you…
**Trask Stalnaker** 55:02 Yes.
**Liudmila Molkova** 55:04 say, okay, I want V2, it means I want V2 stable.
And then you can say, actually, I also want to opt in an experimental.
And it means a bit too experimental. The dupe is interesting, yeah.
Okay, yeah.
**Trask Stalnaker** 55:24 Go ahead.
**Liudmila Molkova** 55:26 the dupe… Do we want it to stay?
**Trask Stalnaker** 55:33 That's a… Good question. It was… It was strongly, requested.
for the SEMCOM, the initial SEMCOM stability.
I don't know if it ended up getting used, Heavily, though.
I could circle back with… I think the feedback came from Ted, primarily via… Kubecon… Around that time.
**Liudmila Molkova** 56:19 Yeah.
I, I, I, I'm… Don't think it's a big deal either way, it would be… to know.
**Trask Stalnaker** 56:30 Actually, maybe I'll just throw out just general topic to the community, whether… How people would feel if we dropped that option.
**Liudmila Molkova** 56:43 Yeah.
**Trask Stalnaker** 56:44 the best way to get feedback. Tell them we're getting rid of it, and see what the… see how loud the response is.
**Liudmila Molkova** 56:53 Yeah.
It's also chief to bring it back.
**Trask Stalnaker** 56:58 Cool, thank you for the thoughts.
**Liudmila Molkova** 57:01 Thanks a lot, I have to go. It was great catching up. See you. Bye.
