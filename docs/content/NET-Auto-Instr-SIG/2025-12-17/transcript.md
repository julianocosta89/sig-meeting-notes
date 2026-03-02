SIG: .NET Auto-Instr SIG
Date: 2025-12-17
Duration: 20 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 02:24 I think that we can wait one more minute.
For other guys, if nobody occurs, I think we can cancel.
Hey, Chris.
**Chris Ventura** 02:52 Hello.
**Piotr Kiełkowicz** 02:55 Can you drive to this meeting, or…
**Yevhenii Solomchenko** 02:57 Well…
**Chris Ventura** 02:58 Yeah, just… just give me some time.
**Piotr Kiełkowicz** 03:02 So, thank you.
**Chris Ventura** 03:44 Yeah, let's see… Okay, can you all see my screen?
Okay.
So, let's look at the open pull requests…
So, looks like we just have a few things in draft… So…
Let's see here…
**Yevhenii Solomchenko** 04:22 Do we have some background information on this one?
It's a gap in the file-based config.
**Chris Ventura** 04:31 Okay…
**Yevhenii Solomchenko** 04:33 We have an environment variable, In the native part of code.
From now on.
**Chris Ventura** 04:38 Okay. Transferring.
**Yevhenii Solomchenko** 04:40 that environment variable from the file-based to the nature part.
**Chris Ventura** 04:44 Okay, yeah, this is the… the change done for .NET Frame… for…
the old SQL client library to capture the, the full SQL statement.
Okay.
I remember.
So, the ability to turn this on, or control that from file-based configuration.
**Yevhenii Solomchenko** 05:12 It's,
pretty ready to review. I think it's only… I have one question about, when native parties start off using. Can I just,
Transfer that, configuration, like,
When it's already started, or it should be before Before I start the mandate.
Application.
**Piotr Kiełkowicz** 05:41 True.
**Yevhenii Solomchenko** 05:41 Thank you so much.
**Piotr Kiełkowicz** 05:43 Combining the… I think you should…
Informative part before pushing information about the bytecode instrumentation.
From the managed codes.
If you do this in this way, it should be fine.
**Yevhenii Solomchenko** 06:09 Okay, I'll double-check tomorrow.
**Piotr Kiełkowicz** 06:13 There's kind of…
There is the… there are methods sending the bytecode instrumentations from managed code to the native part, and if you do this before this stuff, it should be okay.
**Chris Ventura** 06:38 And then, it looks like we're trying to…
Pull in some updates to the native side.
Pardon.
**Piotr Kiełkowicz** 06:53 I think it will be not possible, because,
There is no Visual Studio, 2026 on,
The runtime and the agents on the GitHub Actions.
there is an issue, but it was opened in October, and still no progress there. Or there are kind of discussions why it takes so long.
The comments, you can scroll down a bit and you will see this.
**Chris Ventura** 07:25 Okay.
So we're blocked on… Being able to have… The updated build tooling.
**Piotr Kiełkowicz** 07:35 Exactly.
Locally, it is working fine, so… Whatever.
It is problematic only when you check out our…
clean your repository and freshly open in the Visual Studio. Otherwise, it's… Whatever.
**Chris Ventura** 08:04 K.
And then… I assume this project is still on hold.
For the experimental op-amp.
Implementation.
**Piotr Kiełkowicz** 08:20 I think now the most of work is done on the contribute repository. Steve Gordon from the Elastic is adding a lot of functionalities.
Martin Costello from Grafana is mainly reviewing us, Rasmosis on PTO until the next of the… until the January.
So, there will be no progress in the next, let's say, 2 or 3 weeks.
**Chris Ventura** 08:48 Okay.
**Piotr Kiełkowicz** 08:49 And still, we have the problem with loading different versions of the libraries. It is the main blocker.
Because we have dependency on the Google Protobar.
**Chris Ventura** 09:17 Okay, for new issues…
So… Alexi's mentioning what I think are some, interesting approaches.
That I think are probably worth trying out.
to see if they improve things.
For the dependency management scenario.
I did mention… some of the work that Rasmus already investigated with the assembly load context.
Just to have some additional context for this work…
**Alexey Pukhov** 10:06 Yeah, definitely. Thank you, Chris, for that.
Igor already replied to your, like, some details.
Regarding the new suggestion.
What I also want to do with the… with the… and by the way, thank you for the link, I missed it.
What I really want to do is to basically check what was done by Rasmus, what was his investigation, and also check the test.
Because in that ticket.
It is mentioned that there were some failures with the test, that the approach didn't work. I mean, there were some problems caught by the test. I just want to double-check what were the problems of… in the test, to make sure we are addressing them as well.
**Igor Kiselev** 10:49 I'd like to add that we already talked with Rasmus, and I also looked into his branch, and that idea comes up after looking what was issues with Rasmus branch, and
We really… yes, both of that approach, use assembly load and context. It's… by the way, it is possible to implement both of strategies at the same time through a different configuration of luck.
I still believe that, full separation of dependency would be much more work.
the unification of assemblers, and, it's right now mostly, idea about, let's work around restrictions that there would… that APA is
could not be modified, because assembly load and context allow us to load different versions of assemblers. And, most questions would be here, how
how much we okay to use that approach. So, for example, right now we create a store folder, and we create additional depths folder.
So that approach could either be done on top of it, and say that, okay, we have now another way to do the same thing, and the assembly loader would still correctly have found an assembly version from a store.
Or we could say that with that approach, we don't need a store at all, we don't need additional depths at all, we would resolve everything by our assembly resolver, by making it show that it would load each asset. It would still have the only one version of each assembly, but would load it in a prop assembly loading context.
I think that's better, it would result in a cleaner code, it would result in less duplication, we would be able to mostly reuse what we already have in .NET Framework to deliver what, need to be done in .NET.
And on top of it, it would allow us some more interesting things to solve. For example.
this latest hotel release, we provide, .NET 8 assemblies, okay.NET for Microsoft Extension, even for higher version of .NET,
of .NET. So even… so customers who, for example, use console application on .NET 10,
and don't have a reference to Microsoft Extension Thompson assemblers, would get Microsoft Extension assembles of virtual aid.
We already have a multi… multi… multi-targeting pack on .NET Framework.
That is easily to be extended on .NET.
family, and with it, we would still build .NET 8 assemblies for…
us, but we would have a dependency on .NET 10 or .NET 8 assemblies for OTEL itself, and would provide a different version of assemblies, depending on customer runtime. So, that's why my thought
Eve… We would not…
come to any blocker issues with it. It should be our go-to approach. It still has some risk with, that customer application that uses their own.
assembler resolver, and that tried to load the version of assembler that is not in TPAC, maybe broken with it. I think they are broken already with it, but, we have an issue already opened, when
customer's application get, system diagnostic, diagnostic source 8 instead, or 9 instead of 10, and the customer responded that he have, plug-in architecture. It would be really interesting to understand a little bit more, and to better understand… so to better see
How wide it would be that
There would be some separate resolver, in user applications.
Cool.
**Alexey Pukhov** 15:12 Well, we'll keep you all updated.
**Chris Ventura** 15:16 Yeah.
Okay.
So, no code configuration… Of parameterized generic methods.
**Piotr Kiełkowicz** 15:36 You can assign it to me, I will double check, but we have kind of… Okay. Some… some…
tests related to… generic methods?
And I think this… this… User already have some issues with…
Even simpler scenarios, so maybe it's… Okay. Probably also here.
**Chris Ventura** 16:08 I'll leave it off of the project for now until you get a chance to take a look.
And, we got an update on this .NET environment variable conflict.
And… They're still running into the issue with the latest version, so it's probably worth having somebody
See if we can reproduce this.
Locally.
**Piotr Kiełkowicz** 16:48 In this year, I'm out of time, to be honest.
**Chris Ventura** 16:51 Same here.
**Piotr Kiełkowicz** 16:57 So, maybe… I'm not sure if the minimal reproducible example is delivered. If no, we can ask about this.
And tell the customer that we can… Look into it.
next year.
**Chris Ventura** 17:16 Yeah.
I mean, hopefully the reproduction steps are enough.
**Piotr Kiełkowicz** 17:25 Hopefully.
**Chris Ventura** 17:26 Yep.
And… This one, so, upgrading auto instrumentation versions…
Okay, yeah, so we're waiting for the minimal reproducible example here.
**Piotr Kiełkowicz** 18:06 Support.
**Chris Ventura** 18:19 This one… I think was all… oh… Yeah, let's see…
Okay, and we've already assigned this to Steve.
So I think we're just waiting for him to have some time, too.
Okay… Discussions… No new discussions.
Okay… Nothing to add.
There…
**Piotr Kiełkowicz** 19:19 And if you're speaking about the milestones, I think that we will need to make a release in January.
There is kind of a lot of good stuff.
new good stuff, including analog, support for
continuous profiling on the .NET framework, and… Kind of other things.
Hopefully, there will be also… there will be also some release on the SDK, because we have…
Also, some improvements there, including… memory optimization for the OTLP related to histograms.
probably new semantic conventions for the SQL clients, and so on, so…
I suppose if you're doing good.
**Chris Ventura** 20:15 Okay.
Any other topics?
**Piotr Kiełkowicz** 20:23 I'll just make a note that next two meetings are canceled.
Due to holiday season.
I'll see you next year!
**Chris Ventura** 20:39 Yep.
**Alexey Pukhov** 20:39 Thanks, happy holidays, guys!
**Yevhenii Solomchenko** 20:42 You too, bye, see you.
**Alexey Pukhov** 20:45 Bye.
