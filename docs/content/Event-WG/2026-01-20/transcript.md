SIG: Event WG
Date: 2026-01-20
Duration: 28 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:30 Oh…
**Trask Stalnaker** 00:32 Hey!
**Liudmila Molkova** 00:34 The meeting day.
**Trask Stalnaker** 00:37 Yeah…
**Liudmila Molkova** 00:54 Okay, yeah.
I need to drop off a tough… I'm sure to munich.
**Trask Stalnaker** 01:02 Okay.
Do we want to chat about…
Yes, exceptions, errors, and span events.
**Liudmila Molkova** 01:33 So, I've sent this guy… let's see if… no feedback from feature flags.
I dug into the history. It was you who proposed error, that message. Yeah.
**Trask Stalnaker** 01:51 I remember this.
**Liudmila Molkova** 01:55 But, I'll ping Daniel if he doesn't come, in a few days.
**Trask Stalnaker** 02:07 So, I don't, I don't know. And it was, it was featureflag.error.message before.
**Liudmila Molkova** 02:14 It was featureflug. Oh, gosh, give me a sec.
So, it was… Feature… Lag…
Wait, this is the… deprecated.
Oh, here.
So, it was feature file evaluation error message.
They discussed whether it should be evaluation or error.
So the… the… this is where your comment came in, to call a terror message.
from this discussion.
**Trask Stalnaker** 03:08 Okay.
**Liudmila Molkova** 03:09 I'm just proposing to drop.
Both of them, they didn't have consensus.
**Trask Stalnaker** 03:18 Cool. Alright, I have approved that one.
But… Pop the next one, open… may contain… oh yeah, sensitive information.
**Liudmila Molkova** 03:36 So it's just the regular… Blurp.
Oh.
Right.
This whole node.
**Trask Stalnaker** 04:18 Okay, I will… I'll leave a comment.
I have some thoughts, but I need to think through them about,
Options for people… Who have the, like, like, you can disable instrumentation, like, duh…
for some reason, I don't want it to be, like, telemetry… processing in the telemetry pipeline is, like, your only salvation if you have, since, you know, if you have a PII data leak.
**Liudmila Molkova** 05:03 Mmm, I see. So, like, instrumentation may provide additional configuration, too.
Stop recording.
stuff.
**Trask Stalnaker** 05:14 Yeah, or… even…
**Liudmila Molkova** 05:21 Yeah, if you're.
**Trask Stalnaker** 05:22 I don't know.
**Liudmila Molkova** 05:22 And you know that it's common for that specific thing to contain sensitive details, don't record it, even by default.
And maybe I've allowed opting in.
**Trask Stalnaker** 05:35 Yeah, I'm not sure I want to go that far, okay. Like, that's a lot of…
work on instrumentations. I was kind of more thinking just, like,
You can turn the instrumentation off entirely.
If you have a PII data leak.
But maybe, like, it doesn't need sane…
Anyway, it's just something I need to, I'll think through a bit.
**Liudmila Molkova** 06:06 Okay.
**Trask Stalnaker** 06:06 Just wording of, like… I worry anytime we talk about PIA data that people will Little panic mode.
**Liudmila Molkova** 06:16 Right? So leave a comment, I would not merge it until you… Yeah.
**Trask Stalnaker** 06:20 Yeah.
I'll leave a… Actual suggestion, or… or approve it.
**Liudmila Molkova** 06:29 Thank you.
Okay, so… This is the bigger one.
I made it past. So, I think the strategy around this hot tap
is we already are taking it piece by piece, right? We are adding record exception, we are…
Deprecating span events… Well, not deprecating, but anyway, so we are taking… Pieces out of it.
And this example is something Robert is updating.
I just want to try to remember, why did we need a knockup for this?
So, is there… something that should be in OTEP.
**Trask Stalnaker** 07:26 I think…
Or, like, it was, at least in my brain, at the time, there were… there were too many, like, open…
Questions of, like, needing a direction?
To go.
If we think that we have sort of sorted that, Enough to send…
direct PRs, I'm all for it.
**Liudmila Molkova** 07:59 Yeah, and it doesn't seem we're getting any pushback that you need a bigger vision, like OTAP, for the said… said exception. It's… it's…
Straightforward for everybody in the community.
**Trask Stalnaker** 08:12 Yeah, I think the bigger one is this…
I think your PR here, your new PR,
It's… it's the duplication of things, and how to resolve that, and severity levels.
**Liudmila Molkova** 08:30 Okay.
Yeah, so this is not about duplication, right? So I think this covers the gap we identified
for the Roberts PR, that we are replacing SPAN events
That are fully defined, right? There is a name, there is our attributes, with something that's just an attribute group.
Right? And it's not fully defined.
So I want to…
**Trask Stalnaker** 08:55 Yes, event name and severity.
**Liudmila Molkova** 08:58 Yeah, so I just want to update this doc to…
Provide, like, something instrumentations could use.
And it… yeah.
we can build on top of this.
So, Whatapp or SuraSpec PR to add a config option to say at which level the exceptions should be recorded?
But it's, it's like… orthogonal change, right? We don't even need this PR to…
Have some config in the spec for… severity.
**Trask Stalnaker** 09:35 Yeah.
Yeah, I agree, this one is…
straightforward. The one that I think… the one I'm more concerned about getting community buy-in from is…
the… well, I guess… I mean, we've kind of de facto gotten buy-in on span, event, Exception…
Being put now in logs.
With the exception… Eventually. I guess that's what this is.
Yeah, because then… so you have this, and then Robert's…
PR essentially kind of de facto makes semantic conventions recommend using log exception instead of Span recorded exception.
**Liudmila Molkova** 10:37 Yes. Well, not instead of. So now we're saying use one or another, spend event or.
Error in logs?
It removes this pan event option.
**Trask Stalnaker** 10:53 Okay, and so…
Wow, how's that, thinking towards the next, we're getting close to the Java Agent 3.0 major version bump.
I mean, not super close, but a matter of months, hopefully.
That would be… Something for us to consider.
then… changing… our instrumentation from Colleen.
Record exception on spans to… Emmitting them, exceptions as log events.
**Liudmila Molkova** 11:39 Yeah, and maybe it would be… for the typing, it would be a good testing ground for this PR. Like, how would you pick a name?
How would you pick a severity?
**Trask Stalnaker** 11:51 Right, right. Okay.
**Liudmila Molkova** 11:54 It's… it's likely… okay, so there are two possible outcomes for this. First, you would just emit a log record.
was, those attributes. No event name, no nothing.
The other possibility, you would say, okay, HTTP server errors deserve its own event.
And then it should be HTTP server error. It would include all the exception attributes, it might include server address, server port.
Error type, and it's actually… Maybe something else.
**Pellared** 12:34 Hello, sorry for being late.
**Liudmila Molkova** 12:36 Oh, no worries.
**Trask Stalnaker** 12:37 There are…
**Liudmila Molkova** 12:40 We've been going through the PRS and,
We're talking about the proposal for adding… updating the
Log exception… exceptions log with the… Event name and severity.
Stuff.
And,
So the last interesting design decision, let's say we're doing HTTP server instrumentation, if we are emitting a log record instead of span event.
How would we… Would we use a…
an event or a log record for this, and if it's an event, how, like, do we want to document it? Do we want to call it specifically?
**Trask Stalnaker** 13:44 Yeah, my first thought was,
Well, it'd be kind of nice if all, like, HTTP server instrumentation
Stamped the same event name so that you could search for those.
But then I… looking at your example, and like, like…
Could make sense to have more granular event names, like…
why it failed. Like, categorizing them as why they failed.
In which case, that general purpose one doesn't… isn't really… Helpful.
**Liudmila Molkova** 14:30 So, I'm thinking about it from this angle.
So there are things like sentry.
Oh… Or is your monitor who separate exceptions from
Exceptions specifically.
**Trask Stalnaker** 14:49 Yes, yes.
**Liudmila Molkova** 14:51 And in the sense, It's kind of important to have an indication whether
Exception was handled or not. We're back to this escaped thing.
The… hope I have that Okay, if we tell people how to populate severity, properly.
Then, they would use… severity properly.
And we can leverage the severity
To say, okay, if it's an error, then it's an unhandled exception.
This plant has a floor, you see?
Because there are endless amounts of bad logs out there, and our severity is a low fidelity.
indication.
**Trask Stalnaker** 15:41 Right?
**Liudmila Molkova** 15:44 So, we might want to come back to some additional convention for this.
unhandle thing.
**Trask Stalnaker** 15:53 But I… I don't think… I'm not too…
So, I'm not sure we need to over-index on all the existing bad logs that… in it,
Because… I mean, we're kind of…
I think we have a chance to say what we…
think good logs should be, and… people… ha… who are…
aggregating both good logs and bad logs. Like, the good logs at least have more information, like event name and things that, they can…
Filter those down if they need to.
**Liudmila Molkova** 16:40 Okay.
Then, Artel would admit good looks.
It means… does it mean that…
Job, like, when you replace log…
Expand record exception with logger, emit record.
Does it mean you would want to set the event name?
Or we can say, okay, at least for now, it's a… it's a bad log.
at an event.
**Trask Stalnaker** 17:21 Oh.
I mean, but we know it's a good… I mean, when we're catching…
**Pellared** 17:27 Sorry, sorry to interrupt, but I think it may be helpful. What about aerotage?
If we have exceptions, we already…
Are they finding some error types, or not?
**Liudmila Molkova** 17:45 Error type.
**Pellared** 17:51 Is it in not already in the recommendation for exceptions, something about error type?
don't…
**Liudmila Molkova** 17:59 It's in your PR. We don't… Have anything…
**Pellared** 18:02 I think it was… I think it was before my PR.
**Liudmila Molkova** 18:05 Yeah, okay.
**Pellared** 18:06 I think it was before for metrics, yeah, and maybe even for spans.
**Liudmila Molkova** 18:11 Oh, I mean, for metrics and spans, yeah.
**Pellared** 18:15 Yeah, but if we already have the same problem, how do you know?
name the error type for, you know, metric spanse. Is this something different? Do we want to use some different name?
Do we need a new name, then?
**Liudmila Molkova** 18:36 We want event name if we want it to have some special meaning, if it has some additional attributes, let's say, right?
Probably makes no sense to call it…
Exception, or not provide event name at all if it doesn't.
And maybe eventually it will.
So, like, the, the in-place… Like, the equivalent replacement is just a log.
Record or event with bag name exception.
You would get it if, let's say, you want to, I don't know,
switch to log-based events with a spend processor.
But then, if it's a log record now.
Then, in future, it can become better. It can get an event name, it can get extra attributes if it's necessary.
**Trask Stalnaker** 20:03 So, it might help me if we kind of separate these two,
One is instrumentation, logging these exceptions, and one is log bridges.
because instrumentation, when instrumentation is logging the exceptions, I feel like those we have
The… enough information to make good choices?
**Liudmila Molkova** 20:38 Yes?
**Trask Stalnaker** 20:42 So, like, it would be nice… I think it would be nice to have an event name?
To signify, sort of, hey, this is…
Good data, the way that we're sort of the… using the event name To mean… differentiate between
Old… older logs and newer logs.
Log bridging is where We kind of just inherit
Whatever junk is getting emitted already by logs.
Some… we might make different choices there.
**Liudmila Molkova** 21:28 Robert, go ahead, I have a point, but you have your hand raised.
**Pellared** 21:33 Yeah, I know what will help me, some prototype in Java or Python, for sure not in Go, I don't know for HTTP instrumentation or whatever, anywhere that we will have some examples. Because right now, I'm just being lost because I have no, you know, concrete example where you can play with this.
Possible thematic conventions.
What do you think about this?
**Liudmila Molkova** 21:56 No, totally, I'm just, think about what we would discuss, what we would implement in this.
prototype, we're discussing how it would look like.
**Trask Stalnaker** 22:08 And we were discussing that right before you joined, Robert, that, Java is.
**Pellared** 22:14 Well, that's wonderful.
**Trask Stalnaker** 22:15 Java's taking a major version bump in the next few months.
And so I'm kind of motivated to get
any and all big breaking changes in there. So,
I will… either myself or somebody else in Java Instrumentation, I'll ringlead and,
Look at… yeah, it would be nice to get this… Yen.
Stop him using record exception and start emitting them as…
Log record… exceptions as log records.
**Pellared** 22:56 Because what I re… what I remember…
And I also prefer seeing what I remember instead of what is written right now, because this reflects how my current understanding, even, is not written correctly. My understanding could also be also not correct, right? But…
I remember that Ludumio was saying that the error type is something that could be more, like, abstract, more domain-related. That's also why it's often described in the semantic conventions, the event type.
So, the event type is kind of, could be, or should be an, you know.
Kind of what happened, and that's why Metrics are using it.
And I think you also said that the exception type could be also there, which is something, like, more, you know, code level. What is the name of the exception type?
And my understanding for logs, when we have these bridges, we'll just set the exception type, the exception message, exception message.
And I was not sure what about the more, you know, semantic conventions. I think there was an idea, that we want to use the same kind of approach for event name, for, for the
to use the… What we use for metrics, for
Event… sorry, for error type could be useful. Event name.
But then also CJ, I think EuloDumio as well, kind of said that it would be better to use the same attribute.
Yeah, and this is what I remember. And then the question was, do we even need an event name?
**Liudmila Molkova** 24:42 I mean, yeah, so maybe about the event name.
So what event name we would give in HTTP instrumentation? Is it just…
exception, and that what is the value of it? It's not…
Saying anything on top of what's already included in the attributes.
Is it a good, new thing that we want to actually…
**Pellared** 25:12 I thought about telling, because we can have in the error type, you know, what was the error.
If possible, I would rather say.
Kind of name the event name of the operation.
So what we try to do?
**Liudmila Molkova** 25:34 Operation error.
**Pellared** 25:34 folks.
I mean that, for example, yeah, like, connection error, and then you have, I don't know, some DN… the… I don't know, the exception could be an error type, something about DN, I don't know, DNS, or whatever.
I'm just having, you know, thinking about providing more context instead of duplicating the same information in the two, I don't know, multiple attributes and event name.
**Trask Stalnaker** 26:06 Do we want to have… so event name is…
Right, this idea of event name is for categorizing for Either for filtering, grouping,
Do we want to have a category? Like, yes, you can find all exceptions, By looking in the…
Attributes, or the exception.type?
But would you want, like, all exception events to start with, like, exception.something?
And to be able to…
Look at those… Separately.
And I'm not sure you would, like, I… I mean, I like leaning into the severity level.
Right, that that's what matters. You're looking at errors.
**Pellared** 27:16 I also… I also do not have anything
Against using the same information, the same value, even as what we have in error type.
Because I think this is something we also do when naming spans, that we often, for using the span name, we re… we add there some kind of, you know, things that will be already derived from the attributes. And I think we could do something similar here as well.
**Liudmila Molkova** 27:48 So this, this is… analogy is the metric name. It's static.
**Pellared** 27:53 Okay.
**Trask Stalnaker** 27:54 Yeah, I worry about… Making these dynamic…
the… because I think a strong use case is people ingesting, like, they're gonna look for…
events that they care about. And the event name is supposed to really be that identifier of things that you… something that you can filter on.
**Liudmila Molkova** 28:23 It's almost like, and some people do this, they store different events and different database tables.
**Trask Stalnaker** 28:31 schemas, yeah.
**Liudmila Molkova** 28:32 Yeah.
I'm super sorry, I have to drop both. Oh, yeah.
**Trask Stalnaker** 28:37 No problem.
We'll… Pick it up next week.
**Pellared** 28:41 Yep.
**Trask Stalnaker** 28:41 Or on the… I'll look at your… your PRs.
Yeah, yeah.
**Liudmila Molkova** 28:47 See ya. See you later.
**Pellared** 28:49 See you.
