SIG: .NET Auto-Instr SIG
Date: 2025-11-12
Duration: 14 minutes
============================================================

## Zoom Recording Transcript

**Yevhenii Solomchenko** 00:47 Bye.
**Zach Montoya** 00:53 Hello.
**Piotr Kiełkowicz** 01:10 Hey, guys.
**Zach Montoya** 01:13 Ape.
**Piotr Kiełkowicz** 01:21 Nothing strange happened with my camera.
I think I can start sharing the screen today.
So… I do not see anything special or at the beginning for the agenda.
If you're custom.
Is that letting me know?
I will try to open the most important… Stop.
This is, just bumps, okay.
I've seen some changes from Dan.
Here, from Daniel, but I'm not sure if this is working.
I doubt that you'll have some time this week to look into it, so if you have
capacity, it would be great. Unfortunately, it needs to be executed locally also, because…
Last time, it was kind of… comfortable was looking great, but it was not working as expected.
Startup folk… From Ranier?
I've seen some initial reviews.
Priests, any other comments you have?
**Chris Ventura** 04:17 The changes seemed fine to me. I had only found one minor thing related to a comment.
Just making it match the code.
But… Yeah, I mean, it's unfortunate that it's complicated in the sense that we have to… patch.
A method using, some bytecode changes to make it work.
But… It's not too bad.
**Rhynier** 04:54 Thanks for your review, Chris. I appreciate it.
**Piotr Kiełkowicz** 05:02 So Zach, second power fare is always great.
**Zach Montoya** 05:08 Yep, I'll take a look at that.
**Piotr Kiełkowicz** 05:13 I… we have two file-based configuration…
PRs, both of them also reviewed by Chris. I will check to… I will try to check it tomorrow and match if it's fine.
I doubt that it is kind of anything, that's you.
Understood.
And FDCR created PR…
Allowing us to… execute profile… continuous profiling on the .NET framework.
As I know, he is working on
Documentation, how it is working, and how it is different from .net.
8+.
Because it is kind of,
Significant differences, because we cannot stop all… Whole runtime entry, kind of.
take snapshots thread by thread, if I understand correctly, but you can expect the documentation shortly.
For this. But the code, as I understand, is ready to review if you would like to dig into it.
And I do not think that we have any other important PRs right now.
Nope.
We should send these questions.
Fibers, this one…
I think there is only this one, reported by Sean from Microsoft, and Matayosh…
was able to reproduce it, and as we… and probably the fix needs to be on our side, Chris.
**Chris Ventura** 07:32 Yeah, so I wasn't sure, because… There…
**Piotr Kiełkowicz** 07:38 I know, it should be in the SDK, but we have different… defaults.
**Chris Ventura** 07:45 We do, it's just… what is the expected behavior of the environment variables in general? So…
Is it that if you have one of the metric-specific environment variables set, then you should only look at the metric-specific environment variables?
Or is it that… You should always Look at the fallback.
**Piotr Kiełkowicz** 08:19 I think always look at the full book.
**Chris Ventura** 08:22 Which would be a bug on the SDK, too.
And I can understand making a change on our side.
But… When I looked at the code in the SDK, it never… Looks at the fallbacks.
**Piotr Kiełkowicz** 08:40 Exactly.
But we are always going here.
Because… The way how we configure Options…
We always… we do not know the exact, or specific… signal-specific version, so we are always going to the default environment or variable names. I can agree that there is a bug also on the SDK side.
**Chris Ventura** 09:08 Well, if…
**Piotr Kiełkowicz** 09:08 Yeah, true.
**Chris Ventura** 09:10 Are we sure that we're going down that default path? It seemed like we were going down the metric-specific path, otherwise we would have picked up the…
Correct protocol setting.
**Piotr Kiełkowicz** 09:24 I have… short talk with Matteos today, and he was debugging it.
**Chris Ventura** 09:31 Okay. And he mentioned that it was going into this branch.
**Piotr Kiełkowicz** 09:34 For some reasons.
So…
there are issues probably in two places, as you said, but I think this fix should be done on our side, unfortunately.
**Chris Ventura** 09:51 Yeah, I still think it's a bug on the SDK as well.
Not saying that we shouldn't fix it on our side, too.
**Zach Montoya** 10:02 Is this the bug? With the same environment variables, is this also just reproduce with the SDK and not our…
Auto instrumentation setup?
Do you happen to know?
**Chris Ventura** 10:14 I did not have time to set that up.
But, reading the code, it looks like it.
**Zach Montoya** 10:20 Okay.
**Chris Ventura** 10:25 Because this is where it's interpreting the environment variables, and based on…
The… this branching logic, it only passes a single environment variable name.
Into each of those branches.
**Zach Montoya** 10:42 And it doesn't look at the fallback.
Yeah, yeah, yeah, I would expect there to be some fallback logic, okay.
**Piotr Kiełkowicz** 10:53 I will check it, but for sure it is not blocker, because I don't… I doubt that we have any regression here, so even if we decide to make a releases, it should be fine to make it later.
Lifestone…
We are correct.
currently on this one, I suppose it would be 114.
Momo, and the projects.
No new discussions…
Issues are correctly assigned, and I'm not sure if we…
Funny things to update on our reports. For sure, we need to…
add support for .NET 10 shortly.
But it is, let's say, blocked, or…
by the SDK and the contract, so probably it can be… the job can be started next week.
**Chris Ventura** 12:17 Is the SDK planning on a release in the next 2 weeks or so?
**Piotr Kiełkowicz** 12:22 Today.
**Chris Ventura** 12:23 Oh, okay.
**Piotr Kiełkowicz** 12:24 wooden.
That doesn't see that soon release.
**Zach Montoya** 12:27 First of all… Donna 10 support?
Is it for .NET 10 support? Okay.
**Piotr Kiełkowicz** 12:32 And no other changes, in fact, are kind of very minor.
**Zach Montoya** 12:37 Cool.
**Piotr Kiełkowicz** 12:38 there is, good information for us, there will be less conflicts, because SDKI decided to
downgrade required packages for the .NET 8s. It would be nodes. The only potential conflict throughout your own diagnostic source package, or there will be
equal to the version of the .NET. So, Microsoft extensions, V8 for .NET 8 and V10 for .NET 10.
So… Huge improvement for… for us.
**Zach Montoya** 13:14 So it's only Diagnostic Source that'll be upgraded to the latest .NET version that's, supported, so…
**Piotr Kiełkowicz** 13:21 Exactly. For .NET. For .NET… for .NET framework, it will… all… all packages will be upgraded to the latest.
I think we have kind of… there is kind of a good…
Let me show how it is.
Go ahead and page from this.
I do not have any other topics.
That's the thing.
**Zach Montoya** 14:25 Nothing for myself.
**Piotr Kiełkowicz** 14:31 Thank you all. Have a nice day!
**Zach Montoya** 14:33 Yeah, everyone.
**Rhynier** 14:36 Bye, everyone.
