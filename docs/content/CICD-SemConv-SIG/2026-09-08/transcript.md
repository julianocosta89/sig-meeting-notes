SIG: CI/CD SemConv SIG
Date: 2026-09-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:07 Hello?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:12 Hey, how's it going?
**Christophe Kamphaus** 00:14 Why not you?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:18 Alright.
I don't know how long I'll be on here today.
My house got hit by lightning, so I'm waiting for an insurance adjuster to come out here.
I don't know if he'll call or not.
But I should be on at least for a few minutes.
**Christophe Kamphaus** 00:48 Yeah, I think also with the last calls, we're always… Relatively quick.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 00:54 Yeah, I agree.
You.
**Christophe Kamphaus** 01:04 Hello.
**Alan Clucas (Pipekit Inc)** 01:07 Hello.
**Robert Pająk (Splunk Inc.)** 01:08 Hello.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:11 Hey.
**Christophe Kamphaus** 01:34 Who wants to start?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 01:47 I mean, I can, I don't really have any other updates other than what I mentioned last time, which was getting the infrastructure, updated.
I'm writing some automations for that. Next things I'm going to be working on are… Actually adding environment variable context propagation, the shared workflows we have for the dashboard stuff, that's in the hotel space. And then.
Also, I have some PRs to review on the… on the GAB receiver, so those are the two main things I'm going to be working on for the next little bit.
**Christophe Kamphaus** 02:26 And so, from my side, I will review Robert's blog post.
And I will also take a look at Jenkins, how it's using the environment variable propagation.
It makes sense to, use the SDK there.
So that's it from my side.
**Robert Pająk (Splunk Inc.)** 02:51 So Christophe, as you mentioned, the PR for the RC of context and carriers is ready for review. So thanks Christophe. I know Adriel also said that he will look at it. I don't know Alan if you have time.
But if you even just take a look and be aware, it would be great.
**Alan Clucas (Pipekit Inc)** 03:12 I will try and have a look, yes. Thank you for writing it.
**Robert Pająk (Splunk Inc.)** 03:16 Thanks.
**Christophe Kamphaus** 03:16 Yeah, thank you.
Anything else?
**Robert Pająk (Splunk Inc.)** 03:31 Maybe just because we are all here.
I was thinking because I have forgotten.
Do you think that we should also mention the GitHub receiver in the blog post or not really?
From the collector.
**Christophe Kamphaus** 03:52 I would have to read through it at least once to… I have no idea if it makes sense to us.
**Robert Pająk (Splunk Inc.)** 03:58 I think right now, no, because as Adriel told, I think it doesn't support the… propagation yet. Am I right, Israel?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 04:09 Well, I mean, it really… It enables it, it enables the propagation, but it's not the prop… propagation mechanism, if that makes sense. Like, none of these really are the propagation mechanisms, because they have to, like, what has to be done is, like, for GitHub, unless you're instrumenting at the runner, which would honestly be, like, the end-all solution, which would be amazing if they just, like, instrumented their stuff, but… I've tried to talk to them about this, and it's Bonhomme.
I'm deaf ears for now, they, the… all of these solutions require that there is some type of deterministic ID that can be set in the… or inferred in the environment to be able to propagate through environment variable context.
The only one that actually creates a term in S6 IDs.
is the GitHub receiver. The other ones are, like, you're either just gonna make up an ID at the time that you want to make it up at, but there's no guarantee that it's actually gonna map to any type of, thing in the system.
Unless they… they change that, right? So, the only one that actually… well… from the GitHub side, anyway. The only one that really enables that environment variable context propagation because of the context ID, or because of the trace ID, determinism is the GitHub receiver. But I don't know that I'd mention it until… unless we, like, actually show the environment variable context propagation. But, like, the run with telemetry one, for example, requires that… Like, if you want the traces that it emits to show up.
You need the GitHub receiver.
Does that make sense?
**Christophe Kamphaus** 06:02 So, if I understood it right… It would be more run with OpenTelemetry, but one that would implement environment variable propagation.
And you are saying that… You should only mention it if it really matches with the GitHub receiver. Did I get that right?
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 06:26 I would only mention the GitHub receiver if we have some type of instrumentation.
propagating, or using ENV context propagation.
in GitHub.
tying it to the GitHub receiver.
Like… Yeah.
I think I said it right the second time. Does that make sense? Does that clarify it?
**Christophe Kamphaus** 06:50 Yep.
**Robert Pająk (Splunk Inc.)** 06:56 So I think that it would be also best if you just double check the doppels if I'm not lying anyways to what you said.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:03 Yeah.
That works.
**Robert Pająk (Splunk Inc.)** 07:05 And make any false, you know, false statements there.
Better not to tell anything than tell something which is not true.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:15 Yep.
**Christophe Kamphaus** 07:16 I will review it this evening.
**Robert Pająk (Splunk Inc.)** 07:18 Thank you.
**Carlos Alberto Cortez** 07:20 Yeah, likewise, I will review that, after the spec call.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 07:28 I don't know that I will get to it today, but I will definitely get to it in a day or two.
**Christophe Kamphaus** 07:46 Anyone have any other topics?
**Carlos Alberto Cortez** 07:55 Robert, I saw your comment about, like, testing environment propagation, in a few different components, including the dash zero.
GitHub Action, I think it released back, but I will double-check on that part.
**Robert Pająk (Splunk Inc.)** 08:10 Okay, thank you.
**Christophe Kamphaus** 08:28 If there's nothing else, I'm going once, going twice.
See you next time.
**Robert Pająk (Splunk Inc.)** 08:36 See you, bye.
**Christophe Kamphaus** 08:37 what.
**Adriel Quinn Perkins (W.W. Grainger, Inc.)** 08:38 Take care, everybody.
**Carlos Alberto Cortez** 08:39 So.
