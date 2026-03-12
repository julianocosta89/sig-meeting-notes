SIG: Configuration WG
Date: 2026-01-19
Duration: 484 minutes
============================================================

## Zoom Recording Transcript

GZ Gregor Zeitlinger 04:17:07 Hello?
Jack Berg 04:17:08 Hello.
GZ Gregor Zeitlinger 04:17:18 this, the… First meeting in the year!
Jack Berg 04:17:23 For this, no, we had one on January 5th.
GZ Gregor Zeitlinger 04:17:34 Oh, so, already 2 weeks passed. That was quite fast.
Jack Berg 04:17:41 January is flying by.
Well, I think we're gonna have a light agenda today, because it's a, And probably light attendance as well, because it's a public holiday in the United States.
GZ Gregor Zeitlinger 04:18:33 Oh, okay.
Jack Berg 04:18:35 Yeah, if you have, if you do have any topics, let's add them to the board.
Add yourself to the attendees list as well, and… Yeah.
I… if I had to guess, I think this meeting will end quite a bit early.
GZ Gregor Zeitlinger 04:19:05 Oh yeah, I had one thing… That is, Java-specific.
Or maybe not.
It is related to the config provider and the Extended open telemetry.
I think I have an issue for that.
About stabilizing config provider… oh yeah, now I found it.
Jack Berg 04:19:50 Are you gonna add the link to the agenda?
GZ Gregor Zeitlinger 04:19:52 Yes.
Done.
Yeah, I think it is actually not Java-specific, now that I think about it.
Jack Berg 04:20:22 Which, so this… So the title of this is Stabilized Declarative Config.
But then you're talking about some kind of… what to do, some behavior things with, like, what… Config provider behavior should be.
GZ Gregor Zeitlinger 04:20:39 Yeah, you're right. I was struggling to find a good title, what, what I was thinking about is how the usage of git config provider in Java, but probably also in other languages.
Will, behave, once, It is moved from the experimental part into the main OpenTelemetry object. Maybe it's Java-specific, because no one.
Jack Berg 04:21:11 else has such an object as Java has.
I mean, you know, an object like OpenTelemetry, which collects meter provider, tracer provider, logger provider.
GZ Gregor Zeitlinger 04:21:22 Right.
Jack Berg 04:21:24 Well, so, I think we can probably take inspiration from the other signals, because you can have an open telemetry instance that has, like, a meter provider and logger provider set up, but not a tracer provider, or, you know, any other combination of that.
And, so that suggests that, you know, there's a… what happens in those cases is that we have, like, a no-op instance. It's not like, you know, if you ask for the tracer provider, you'd get null back, you just get a no-op instance.
And so it just sort of shifts the problem, right? Because you have to decide what the behavior is of the no-op instance, but, at least it's not null .
GZ Gregor Zeitlinger 04:22:03 Yeah, that's a good answer. For config provider, we have a no-op instance, so we could just… that. I think it just always returns empty objects, but let me double check.
Jack Berg 04:22:22 I think that's not defined in the spec, actually. And so what I… I guess what I'm saying is that that would be an area for improvement.
If we go over to the Tracer metric SDK, or metric specifications, you know, there's an explicit document for NOAP, That describes the behavior for all the different… APIs in here.
And.
GZ Gregor Zeitlinger 04:22:47 Right.
Jack Berg 04:22:47 I don't think we have that for declarative config yet, so… underspecified.
GZ Gregor Zeitlinger 04:22:56 Yeah, at least I checked that in Java, the noop.
Jack Berg 04:22:59 is the one that returns the empty…
GZ Gregor Zeitlinger 04:23:03 declarative config properties.
Jack Berg 04:23:47 Okay, so that's, that's kind of a to-do for us.
Some parts we know.
I don't even think we have a NOAP in OpenTelemetry Java, do we?
GZ Gregor Zeitlinger 04:24:01 For a config provider.
Jack Berg 04:24:03 Yeah.
GZ Gregor Zeitlinger 04:24:04 Yeah, we do. That's what I just checked.
Jack Berg 04:24:06 Oh, you did? Okay.
GZ Gregor Zeitlinger 04:24:09 It's in the interface directly.
Jack Berg 04:24:14 Oh, here we go. Okay.
Okay, so that's what you were following up on, to see what we do.
I see.
GZ Gregor Zeitlinger 04:24:23 Empty.
Jack Berg 04:24:25 Oh, I see how this works, because, technically config provider is just a functional interface, because there's only one method on it, and so this is just saying… it's not like we define a noop instance. There's not, like, a class called, like, noop config provider, but, you know, we just have this sort of this, this lambda.
GZ Gregor Zeitlinger 04:24:44 Yep.
Jack Berg 04:24:45 the functional way.
Yep.
So, I think we're probably going out on a limb there.
Should probably… Describe this behavior in the spec.
I can take a note for that. I don't think it's, related to our stabilization effort, because unfortunately, I don't think config provider is, Is part of the prototypes in other languages.
And, so it's gonna be a little bit longer before that part of the spec stabilizes.
GZ Gregor Zeitlinger 04:25:19 And that means we also have to stick with extended open telemetry for a little bit longer than…
Jack Berg 04:25:25 It seems like it.
Okay. Any other thoughts on this topic?
GZ Gregor Zeitlinger 04:25:40 Yeah, so then, I have created a… point request that allows you to given your own config provider when building an OpenTelemetry instance.
That is also linked to it.
Jack Berg 04:26:04 Okay.
So I'll take a look at that pull request then.
Where… is this the POC, 7960?
GZ Gregor Zeitlinger 04:26:18 Exactly.
Jack Berg 04:26:20 Okay, I'll take a look at that. Sorry, it's been 2 weeks, jeez.
GZ Gregor Zeitlinger 04:26:24 No worries.
Jack Berg 04:26:25 Oh my gosh.
GZ Gregor Zeitlinger 04:26:29 Oh, it's still in draft mode. I think I wanted to discuss this first. Okay, so I'll need to get it out of draft first, then.
Jack Berg 04:26:36 Okay.
The only item I added to the agenda was, and I've been sort of beating this drum for a while, was to, just try to discover any issues that we might conf… confront with a stabilizing declarative config ahead of time, and so… If… for the folks on the call, and anybody that happens to watch this recording, please do review the specification. In particular, the parts of the specification that we're proposing to stabilize, and if you see any issues in those, raise them now.
I don't want to be in the… I don't want to be in the business of uncovering stones, uncovering issues, you know, late.
That would disrupt… disrupt this, this effort.
That's all the items on the agenda.
Anything else before we go?
Alex, thanks for jumping on. I know it's early your time.
Alex Boten 04:27:57 All good. I, I missed my notification, so that's why I was a few minutes late, but… No… no issues on… on my side. I… I did start… some of the work around the implementation in Python, so I'm… Looking forward to doing more of that, hopefully, and maybe on… if there's anything left to uncover, hopefully we'll uncover it.
Jack Berg 04:28:21 Have you talked to the Python approvers or maintainers about that?
Alex Boten 04:28:24 Yep.
Yeah, I talked to them back in December, and they were… they were supportive of me picking up some of the work there, so…
Jack Berg 04:28:33 Oh, I forgot, you used to be a maintainer of Python.
That helps.
Alex Boten 04:28:37 Yeah, that's, like, ancient history.
Jack Berg 04:28:44 Before Python became the center of gravity with AI.
Alex Boten 04:28:51 Yes. In the before days.
Jack Berg 04:28:58 Alright, well, if there's no other topics, we'll let Alex get back to sleep.
Alex Boten 04:29:04 I wish.
Alright, see you later.
Jack Berg 04:29:09 Take care. Bye.
