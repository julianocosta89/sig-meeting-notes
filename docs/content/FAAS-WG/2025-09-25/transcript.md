SIG: FAAS WG
Date: 2025-09-25
Duration: 7 minutes
============================================================

## Zoom Recording Transcript

**Warre Pessers** 02:10 Hello?
**Maxime David** 02:14 And hello?
**Warre Pessers** 02:16 Serkin and Tyler let me know that they can't be here. Serkin has some issues at work, and Tyler also has conflicting meetings for this one and the next, SIG meeting.
Okay.
Do you have anything specific you wanted to discuss today?
**Maxime David** 02:36 I don't have anything specific, no. I was just, catching up, lately, and see if someone is, having some… some topics to discuss today.
**Warre Pessers** 02:48 Yeah, there's not that much currently ongoing, I think. I don't know if you remember, but there was this, big thing around the SQS context propagation.
Yeah. That is something that is now a little bit stuck in the JavaScript SIG. They still need to make a decision, and I'm trying to get that pushed through, but it's, it's a little bit difficult at the moment, but we'll get there.
Okay.
**Maxime David** 03:19 Do you need help? Do you need the help to get there, or it's just taking time because they're not too sure that it's the right decision to do?
**Warre Pessers** 03:28 Yeah, indeed, the second one, they're not really entirely sure they want to do it this way, because the spec, the messaging spec for Lambda has deviated from the general spec for messaging.
Tracing, so they want to evaluate if we maybe need to also,
change this in the semantic conventions so that both lambda and the general,
implementation are aligned, and then… Okay. Yeah, also we'll have to update the PR, but, that shouldn't be too difficult.
**Maxime David** 04:10 Okay. I actually have one, one, one topic that I want to discuss is for, Node 24.
we might think about removing the callback handler, or the callback signature handler. You know, in Node.js, when you create an Lambda function, there is two options to create a handler. It's either callback-based or async await.
And we are… Asking the community if it would make sense to remove the callback-based.
And it seemed that we are leaning towards to do that. It's not a…
decision yet, but I think we are going to move toward that, and I think I would need to assess
if we need to make some change to the LambdaTelementary repo to support that, or if it's going to be no-op. So I think I want to have a look at that.
**Warre Pessers** 05:03 Yes, that is indeed an interesting one, because I've seen the warning in my lambdas at work, and I've also seen the issue, I think it's a good decision, by the way.
**Maxime David** 05:13 Exactly.
**Warre Pessers** 05:14 And then, I think I pinged you about this a while ago, that I already noticed that the JavaScript instrumentation, for example, seems to by default, wrap
lambda handlers and, turn them into a callback-style lambda, regardless of whether you, wrote a callback-style lambda yourself or not, so we will definitely have to…
To, to, open a PR for that as well.
**Maxime David** 05:44 Yeah, the good news is that we just released last week the preview image for Node 24 without support for the callback.
So, I would be able to make some tests, like, pretty easily with, using OCI Image. So, yeah, I will definitely look at that, because we want to make sure that when we release it, the, OpenTelemetry tooling is still working, of course.
**Warre Pessers** 06:11 Okay, yeah, cool. That's, that's an interesting one, for sure.
**Maxime David** 06:16 Okay, so let me take an action item on this, then.
**Warre Pessers** 06:19 Yeah, okay, nice.
I'm thinking if there's anything else worth mentioning, but it's been pretty quiet the last couple of weeks.
**Maxime David** 06:31 No.
**Warre Pessers** 06:33 So I don't think there's anything urgent right now. I was going to look into some stuff for the Python instrumentation. There was, someone who requested, support for more instrumentation in the Lambda layer, so we'll have to do some checks,
how this impacts the layer size and all that, to avoid lengthy cold starts, but I will get to that in the next week, probably, to also.
**Maxime David** 07:04 Okay.
**Warre Pessers** 07:04 See if we can help him out there.
And then, other than that, yeah, there's some dependables PRs open that I will be going through tonight,
But I think that's it for now.
**Maxime David** 07:21 Okay, cool.
**Warre Pessers** 07:24 Also, happy to see you joining, again.
**Maxime David** 07:28 Yeah, yeah, so yeah, so it was… it has been a crazy, crazy couple of, months at work, but yeah, I'm definitely back.
**Warre Pessers** 07:36 Yeah, that's nice.
Okay, if there's nothing else, then I think we can, finish up.
**Maxime David** 07:42 Okay, that was a quick one, but, yeah, nice, nice to meet you again, and yeah, let's see what's going to happen for the action item over the next week.
**Warre Pessers** 07:52 Thank you.
Okay, thank you, bye-bye.
