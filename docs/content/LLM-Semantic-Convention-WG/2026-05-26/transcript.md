SIG: LLM Semantic Convention WG
Date: 2026-05-26
Duration: 40 minutes
Zoom Recording URL: https://zoom.us/rec/share/dtfrNZ0GFN1Bzuohdq5aS3PbsoKLaW2WnotWWfHkJ0G97upUYCtY8PyLkkWT3Gka.wvCjMA_I4cmyvMYs
============================================================

## Zoom Recording Transcript

**Steve Rao** 01:13 Yeah, hi, Chaska.
**Trask Stalnaker** 01:18 Hey, folks!
Oh.
My video is not plugged in, that's why.
Give me a sec, I'm gonna rejoin, see if my video works.
**Trask Stalnaker** 02:55 Doesn't look like… Camera wants to… participate today.
Okay, that's okay.
Can you hear me?
**Steve Rao** 03:12 Yes.
**Huxing Zhang** 03:13 Yes.
**Trask Stalnaker** 03:14 Alright.
I will share my screen.
Oh… Wow, these note-takers have become very popular.
**Steve Rao** 04:20 Yeah.
Yeah, you can scroll down.
Yeah, we added some… Agenda?
**Trask Stalnaker** 04:34 Great.
**Steve Rao** 04:35 Ugh.
Score down here, yeah.
**Trask Stalnaker** 04:43 Chang Long.
**changlong** 04:49 Hello.
**Trask Stalnaker** 04:50 Ay.
**changlong** 04:53 Yeah, and since I'm new here, maybe I'm doing a brief introduce… introduction? Sure.
**Trask Stalnaker** 05:00 Oh, yeah.
**changlong** 05:00 Yeah, I work for Alibaba Group, and… I'm a colleague with, Steve and Huxin, and they work in Ali Cloud, so they… they introduced me to join this meeting and join this SIG.
And today, I want to share one proposal about the command line interface, semi-conventions.
There is a scenario, in the… Agent Inflat?
We broadly use the agent to invoke skill, and inside the scale, there are a lot of business command line interface, so… A lot of business units want to instrument those command line interfaces.
I… doing some research before, and I… I know they're already on… and C-L-I-C in the semantic conventions.
But, I think, it's not… working very well with JNI or Scale. So I think, we can… Doing this group, good bridge.
So here is the proposal.
**Trask Stalnaker** 06:26 So, I think the existing semantic conventions are just… for CLI, is just about propagating context.
**changlong** 06:39 Yes.
**Trask Stalnaker** 06:41 And so here, you're…
**changlong** 06:44 And the policemen, and the excursion spent.
And we… we need the metrics as well.
**Liudmila Molkova** 06:56 See, this, this front, this, created for instrumentation.
That spawns subprocesses in Python, and I think they're… it's applicable to… some other, libraries and other ecosystems, but yeah, they probably don't work for, Virginia proper.
**Trask Stalnaker** 07:24 Or, Ludmila, are you saying there… are there semantic conventions spans for command line?
**Liudmila Molkova** 07:30 Yeah, here.
**Trask Stalnaker** 07:32 Oh, no, this is… this is Alan, this is their proposal.
**Liudmila Molkova** 07:36 Oh, yeah, the, the, there is.
**Trask Stalnaker** 07:52 Oh, CLI spins, yes.
Okay, okay, thank you.
Okay, so, maybe you can walk us through what's different here.
**changlong** 08:18 About a spin.
Especially for the CLI spend, there's only one attribute we… we add. It's the process module.
The nice one.
No, in the proposal, yeah.
**Trask Stalnaker** 08:37 in the proposal.
**changlong** 08:38 Yep.
**Trask Stalnaker** 08:39 process module. Oh, okay, okay.
**changlong** 08:42 Because, in… in our scenario, it seems like, many command line interface is, very big.
And for the business, target, like, add to target, add to, cart, or change your address.
And DD will edit this, and… two different, functions into the same, command line interface. So we need a subtype, like module, to distinguish it, or to group by it.
**Trask Stalnaker** 09:25 How would, would this be something that instrumentation could… No.
Or does this require, basically, the user to instrument their own code?
**changlong** 09:41 For command line interface, I think there is no public or open source framework to do this.
Most, scenario is, in-house tools, in-house command line interface.
**Trask Stalnaker** 09:57 So what kind of, is there… What do you want to capture? You want organizational attribution.
Trying to think if there's something that… already… You know, if there's attributes already that you could use, for example… I think there's Proposal…
**Liudmila Molkova** 10:36 service owner?
**Trask Stalnaker** 10:39 Yeah…
**changlong** 10:44 Okay.
**Trask Stalnaker** 10:47 Maybe something like that. Is it a resource attribute?
Let's see, this is on the Kali… Oh, no, wait, wait, wait, I'm on the other, as well.
Yeah, this is on the Kali, so… It's… It could be a resource attribute, right?
**changlong** 11:12 It's… Mmm…
**Trask Stalnaker** 11:13 The thing that owns that process… the people who own that process.
**changlong** 11:19 I don't think so.
I mean… In the, in this agent or another agent, you can invoke the same command line interface, but you, you may use different sub-module of this command line.
I think it's better to put it into the attributes.
**Liudmila Molkova** 11:49 So is it, like, a subcommand?
**changlong** 11:52 Yeah.
Basically, subcommand.
**Trask Stalnaker** 12:00 The… this is on the… your… this would be stamped on the… Inside of the… or… let's see… I guess that's the question. On over here, it's the execution callee.
span… As opposed to the collar span… collar… oh, here, I see, here we do have one for collar. Okay, so you're… you're proposing this as the caller. You want to instrument the skill itself when you're making that call to some other executable.
That makes sense.
**changlong** 12:44 Yeah.
**Liudmila Molkova** 12:46 Is it realistic to expect?
Co-Colese to be instrumented.
I have an Imagine Agent course.
thousands of different tools, most of them are command line tools from OS or GitHub CLI or something.
**changlong** 13:06 Most of them.
**Liudmila Molkova** 13:07 The time, they won't be… Even instrumented.
Well, maybe eventually.
**changlong** 13:14 in… In this proposal, we don't want to instrument, very basic or common tools, or, like, GitHub or browser use.
or, some basic bash. We want to instrument some, higher level.
For, business target, like, add something into your shopping cart.
It's a skill, and it's… it's implemented in command line interface for Agency and invoke.
So… We have hundreds of these, this command line interface, and we… we think it's, useful.
To simplify the agentic.
**Trask Stalnaker** 14:08 So these are, executables that you are authoring, that you are giving customers, sort of, access to call?
**changlong** 14:20 Yes.
**Trask Stalnaker** 14:25 Okay, so you would act… you would instrument… your executables, you implement But, like, to Libilo's point, you wouldn't have… capture anything for… if the skill is calling, like, the GitHub CLI.
**changlong** 14:51 I don't mean, like, as common as GitHub CLI, I think, like, Taobao CLI.
for, so, so for topos AI, the span is, limit. It's not as common as GitHub.
Mmm… And we want to check… Mmm… How many people… how many users will use the… I added two shopping carts, or… order a bill, or, take some orders, or, do some payment, Like this.
**Trask Stalnaker** 15:38 Okay.
**Liudmila Molkova** 15:44 So this is essentially a custom instrumentation that exists inside your tools. It's not something that's… applicable.
Well, it's applicable, but it's not instrumented.
For general purpose.
yours.
**changlong** 16:05 Yes, yes.
**Liudmila Molkova** 16:08 Why do you want it to be in semantic conventions, then?
**changlong** 16:22 That's a good question. I think, I mean, you can…
**Steve Rao** 16:34 I got, I guess, yeah, there is, MCP, semantic convention in JI, semantic, semantic convention, currently, and, I guess, yeah, Tangong, he has, the idea to, provide a proposal, similar to MCP, and to, yeah, collect the, invoke, number from users.
about, CLI.
**Liudmila Molkova** 17:06 Yeah, so for MCP, we have libraries, right? And we can instrument some common layer that people use, and there are a good set of, common libraries. For CLI, there are sometimes libraries, right? For Python, I think this is, the original, conventions were created for a click library, or… Something in Python that spawns the sub-processes.
If we can find a common layer that's, applicable to just skills in general.
Or to some, libraries that would create, quote, like.
skills call it, or executables that skills would call into. It makes sense. What also I think can make sense is Okay, we don't really… we can't really instrument.
the… Kali's side, usually, at least now.
But… the agendic applications can… Amid, color spans.
And it could be a convention that's… less auto-instrumented, and more like a convention for specific Agentic applications, but then we should target all CLI.
things, like GitHub CLI included, and bash commands, all the common ones, so we would say how to capture this.
in a general case, and if the existing CLI conventions are not… if they need to be specific for GenAI, that would make even more sense.
**Steve Rao** 19:10 Yeah, makes sense. Yeah, maybe, Zhang can, yeah, take the comments, back to, think about and, provide more example.
**changlong** 19:21 Okay, maybe we can… Put this into the non-suite, the main convention, for… Our own use, and wait for the… for another moment.
to… To put it to them.
To the open source and to the OpenTelemetry community.
**Liudmila Molkova** 19:48 Yeah, this would make sense. You… do you have a… The proposal, you posted in the… Long suite. Do… did you create an issue in our semantic conventions GenAI?
**changlong** 20:03 Right now, no.
**Liudmila Molkova** 20:06 Could you please create an issue so that, there is a discussion around it?
**changlong** 20:11 Okay.
**Liudmila Molkova** 20:16 Thank you.
**Trask Stalnaker** 20:30 Cool, let's… Go on to, Steve's…
**Steve Rao** 20:39 Yes.
Yeah, yeah, this week, and, our internal, PM provide, a requirement Yeah, they want to collect the reasoning part in output message, and yeah, I want to provide, create an issue, just now, but I found a similar issue.
So I, I just, put the issue, into the agenda.
**Trask Stalnaker** 21:15 So… There's… There is a… I haven't read this, so I might be missing some pieces, but there is a reasoning… dot outputTokens attribute.
**Liudmila Molkova** 21:42 And there is a reasoning part in… In the… Jason schema for messages.
**Steve Rao** 21:50 Yeah.
This, this is, this is a proposal about this, but I, I found, currently in our version, I, semantic, conventions, output JSON, don't contain the reasoning, reasoning part.
Yeah, if I… yeah, remember right.
**Liudmila Molkova** 22:15 There, there is one.
**Trask Stalnaker** 22:19 Here, I'll find what we have today.
**Liudmila Molkova** 22:22 I posted the link to, the… Jupyter Notebook.
If you search for reasoning part.
**Trask Stalnaker** 22:40 Content… Oh, I see, this is asking for not the token count, but the actual.
**Steve Rao** 22:46 Yeah, no, yeah, content of it.
Yeah, it's about the content of output message.
**Trask Stalnaker** 22:53 Oh, and continuity tokens, okay.
Such parts, so… Yeah, looks like we're… As Lamilla says… Looks like reasoning part is there today.
And this is used… this is in the, the attribute for the… output message… Does that cover what you… I mean, obviously.
to give you a chance to check that out, but does that sound like what you were looking for? Were there other parts?
**Steve Rao** 23:58 Continuity.
**Trask Stalnaker** 23:58 tokens.
Oh, sorry, go ahead.
**Steve Rao** 24:04 Yeah, yeah, I'm looking for reasoning part, but I don't find, To the documentation just now, and Yeah, you will doubt you'd, reasoning part, in current, semantic convention. I can check it out later.
**Trask Stalnaker** 24:27 Cool.
**Liudmila Molkova** 24:33 What is continuity tokens, and do you…
**Trask Stalnaker** 24:44 Continuing a reasoning term… So it's tied to… Marius mean.
**Liudmila Molkova** 25:05 Anything that's not captured today can, in theory, be captured as generic part, but… Yeah, we can always add another type of the part.
**Trask Stalnaker** 25:40 Nice.
Cool. Anything else?
You all wanted to chat about today?
**Steve Rao** 25:55 Yeah, no more farming.
**Trask Stalnaker** 26:02 Alright.
**Huxing Zhang** 26:04 Can you hear me? Yeah.
Yeah, I just, have a… Follow-up funding.
And last, last time when we were at the KubeCon, you and, Ludmila has, talked, chatted about the.
demonstration of, our… how… how do we, develop our instrumentations using AI? I think we have a chat with Lumila, and, I want to confirm that Is there any… a chance for us to, like, to demonstrate that… that in some Chennai meeting?
some time off that, and maybe we can make some demonstration about that topic. I'm not sure… how… How do you think about that?
**Liudmila Molkova** 27:02 I remember we chatted about, you folks demonstrating your instrumentation process, or any other parts of what you work on. You're more than welcome to do it here, where if you want bigger audience, we can also figure out, where we can do this. If you're… whenever you're ready.
**Huxing Zhang** 27:21 Okay, so I will talk about my colleagues, and maybe I will invite I had my… one of my colleagues to do the demonstration.
**Liudmila Molkova** 27:34 Which, exactly which topic would you like to present?
**Huxing Zhang** 27:40 I think we can provide something of how do we using AI to developed the… and instrumentation, given that a new version of framework or some framework that we want to instrument, to follow the semantic conventions, we can have the AI agents to develop that instrumentation, according to, like, specification, and do the verification, or… and, yeah, send the PR in some process, like, something like that.
**Liudmila Molkova** 28:23 Yeah, that's awesome. I'm thinking, Trask, what do you think about we try to share it with a bigger audience? I don't know, maybe a spec call, or, maybe some other forum?
And our semantic conventions needing…
**Trask Stalnaker** 28:41 Depends on the timing that works for you all.
If this is kind of the latest that works, then we can… we could do it in this meeting, and this meeting is recorded, and then we could post it.
you know, to various Slack channels with some context.
If you want to… there's also, though, there is the Semantic Convention General SemConv meeting on Mondays, starting at this time now, just after this meeting's time.
And there's the spec meeting.
Which… would… which starts right after this, on Tuesdays.
Which would be another good… chance, especially if you want to kind of generalize it to all kind of… if you think it's generalizable to all instrumentations, not only Gen AI instrumentations, that might be interesting for folks.
In that meeting, we don't have As much time, because there's a lot of other topics, but, you know, like, 20 minutes.
We could probably get…
**Huxing Zhang** 30:01 I think we can do it in this meeting, maybe sometime on this meeting.
First, and then we can… discuss if there's a chance maybe we can share the videos to other channels. That might be good for us, I think.
**Trask Stalnaker** 30:20 Sounds good.
**Liudmila Molkova** 30:20 Sounds good.
Thanks a lot.
**Trask Stalnaker** 30:24 Cool.
**Huxing Zhang** 30:25 Okay.
**Trask Stalnaker** 30:25 Good to see you all.
**Steve Rao** 30:26 Yeah, fine.
**Liudmila Molkova** 30:27 Good to hear.
**Trask Stalnaker** 30:28 Yeah, maybe next week my camera will be working. I need to go reboot my computer.
By all.
**Liudmila Molkova** 30:36 Thank you, bye.
**Steve Rao** 30:37 Hi.
**changlong** 34:24 Okay.
Fuh.
Excuse me.
