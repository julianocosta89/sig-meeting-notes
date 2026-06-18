SIG: .NET Auto-Instr SIG
Date: 2026-06-17
Duration: 19 minutes
============================================================

## Zoom Recording Transcript

**efshaikh** 02:47 Yeah, let's see.
**Alexey Pukhov** 02:51 Hey!
I don't think there's anyone here.
**efshaikh** 02:54 Only the two of us.
Meh… It's already 1 minute over.
**Alexey Pukhov** 03:09 Yep, let's wait for…
**efshaikh** 03:11 Yeah, movement for a moment.
**Alexey Pukhov** 03:12 And then we can leave. Yeah, I don't think there was many.
Things to discuss.
**efshaikh** 03:17 Yeah, actually, I wanted to push for the review of that native thing.
So I…
**Alexey Pukhov** 03:22 Well, I mean, if you're on Slack, you can just…
**efshaikh** 03:25 Yeah.
**Alexey Pukhov** 03:26 I'm there.
**efshaikh** 03:26 Wow.
**Alexey Pukhov** 03:27 Boom.
**efshaikh** 04:22 The review for this needs to happen from the Datadog experts. We don't have anyone in-house, apart from Igor.
That's why I was hoping.
**Alexey Pukhov** 04:37 Well, yeah, we'll see if anyone shows up.
**efshaikh** 04:41 Yeah, I have anyways requested it on GitHub, I have explicitly pinged them, so… You know what? This is really interesting. The… we suspend the CLR on time. I mean, this is in public domain, so don't have to worry.
**Alexey Pukhov** 05:02 Oh, yeah.
**efshaikh** 05:03 So our open telemetry, we have opened up our canary mechanism.
Do you know that when we take a snapshot, we actually suspend the CLR runtime for a window where we are walking the stack?
**Alexey Pukhov** 05:19 Yeah, I mean, yeah, of course.
**efshaikh** 05:20 Yeah, and I just had a thought.
So you have a target threat, right? You suspend the target thread.
And then, you suspend the runtime.
So, what happens is, if your target thread is suspended, and if it is at some critical juncture, like NGC collection, or some PEO, in some area where runtime doesn't allow you to suspend itself.
I mean, that is the whole idea why we have to, probe the safety. So now, if runtime suspension fails.
While the target is suspended. That is… the bailout situation, you just… Back off, and you do not proceed with the snapshotting.
The thought was… If the runtime suspension succeeds, currently what we do is we keep the runtime suspended, and we walk the entire stack. And walking stack can take time, depending on how deep the stack is.
So I was just thinking, I want to experiment a bit on this. How about we suspend the target thread, suspend the runtime.
And if it succeeds, we just resume the runtime right away.
Meaning you don't keep the runtime suspended for the window when we are walking the stack, because we already suspended the target thread, and that target thread is not going to run or acquire anything new or go in inconvenient code path. So why keep the runtime suspended for that duration?
So that way, you just shrink the runtime suspension window to just a few microseconds.
I was just thinking about this, and it came to me, so I'm gonna experiment around that. Do you see how… Huge impact it will have if that thing works.
**Piotr Kiełkowicz** 07:20 Hi guys, sorry for being late.
**efshaikh** 07:24 Hey.
**Alexey Pukhov** 07:24 Are you kidding.
**efshaikh** 07:25 Of course.
**Piotr Kiełkowicz** 07:37 17… I will create that.
I will share my screen shortly.
**efshaikh** 07:53 True.
**Piotr Kiełkowicz** 08:02 I think we have kind of… Two unusual guests. Oh, not so usual. So, Mathieu?
Michael, do you have any topics to raise at the beginning?
**Michele Mancioppi** 08:15 I have, some questions about the implementation of declarative configuration.
Sir? Auto-instrumentation, which is relevant for the work on system packages and injector.
**Piotr Kiełkowicz** 08:32 So, in general, we are not following any configuration SDK API.
In general, for .NET, we do not have such things.
As I know… Steve Gordon from Elastic just started the… contribution for this, and starting the scaffolding, I would say that we have kind of file-based configuration for the auto-instrumentation site, and we parse everything here. But the declarative config Yeah, as you see, it is kind of in the very initial state.
**Michele Mancioppi** 09:09 Oh, this is already better than what I had found out reading at Raper, so, good.
**Piotr Kiełkowicz** 09:15 So, in general, Autel design is that this declarative config should be part of the SDK.
And our instrumentation somehow should utilize this. We do not have enough time to properly design, test, and develop this from… for the… all layers, but we have needed the Possibility to configure auto-instrumentation through the file, so we are utilizing More or less the same.
file structure as the declarative config, but it still takes time to be mature enough to set it… to say that it is following all standards needed.
**Michele Mancioppi** 09:56 But do I understand correctly that the target goal is that the 8.9000 instrumentation will use the official format?
**Piotr Kiełkowicz** 10:05 Yes, it is using official format, but it is not… it is kind of… in the auto-instrumentation, we need to parse and understand every configuration for every component we are utilizing.
and configure it manually. With declarative config.
It should be delayed to just… say, hey, use this configure… use this package and configure it based on the YAM file.
So, this is kind of the biggest difference.
**Michele Mancioppi** 10:37 I don't think I understand the big difference, to be honest. Can you give me a more concluded sample, maybe?
**Piotr Kiełkowicz** 10:43 So… For now, Of course, with the declarative config, the component should be responsive for reading and configuring.
**Michele Mancioppi** 10:57 Yes.
**Piotr Kiełkowicz** 10:59 the… The small part of the functionality he is owner, yes?
**Michele Mancioppi** 11:05 And in this case, by component, you mean a single instrumentation, for example?
**Piotr Kiełkowicz** 11:09 Exactly, or SDK on API layer, whatever.
In the current implementation, other components just exposed to, let's say, development API, and we are manually configuring it from the auto-instrumentation site, and we are parsing the YAMP file.
And it is fragile for any changes in the components.
But it is kind of extremely useful for the end users, to be honest.
Even… even if imperfect from the development perspective.
**Michele Mancioppi** 11:49 So, from the point of view of a user adopting the Don Knight Auto instrumentation.
What are the differences between what digital net auto-instrumentation can do based on files, and what the specification for the declarative configuration says it should be possible to do?
**Piotr Kiełkowicz** 12:09 Mmm… No differences, or kind of edge cases. Part of the functionalities for the components are exposed only by environmental variants, and there is no possibility to programmatically Set it up.
So… Technically, all inverse should be ignored.
By auto-instrumentation, but in fact, we are ignoring most of them when we are reading environmental variables.
When we are reading files, but some of them are kind of survivors.
**Michele Mancioppi** 12:46 I see. Okay.
Did you, do you consider implementing… so the, the, something that is, interesting from the perspective of the System Packages Initiative, is whether… We would be able to use one single configuration file across multiple languages.
**Piotr Kiełkowicz** 13:09 I don't think it is possible, and…
**Michele Mancioppi** 13:11 There is actually a part of the specification in experimental configurations to have overrides for specific languages, but only Java has implemented it so far.
As far as I can tell.
**Piotr Kiełkowicz** 13:23 Not supported exception at the moment.
**Michele Mancioppi** 13:29 Is it supported, eventually?
The reason why I'm asking is because the system packages are in the middle of a lot of things, and one interesting question that came up from the OPAMP guys is.
can't you use one single file instead? Because then that is much easier for OpAMP.
to be able to configure the entire Linux host. But that will work only if the implementations in the SDKs allow for language-specific overrides. The schema allows it, but no implementation except what Java does.
**Piotr Kiełkowicz** 14:04 We are not supporting it. We are welcome to the contribution.
**Michele Mancioppi** 14:08 Okay Good.
Thank you.
**Piotr Kiełkowicz** 14:12 I would say that we should not invest a lot of time with current implementation, and if you are interested in this topic.
just look into this PR in the .NET SDK repository, and check with Steve Gordons about his… his plans.
**Michele Mancioppi** 14:31 Sounds good.
**Piotr Kiełkowicz** 14:33 I think in the Splunk, we have also discussed this one versus… Multiple language… multiple files, and for now, we have decided to follow the multiple files.
**Michele Mancioppi** 14:49 I, I understand why you took this position.
**Piotr Kiełkowicz** 14:51 Let's say, per technology.
**Michele Mancioppi** 14:57 Okay.
Thank you. That answers my question.
Well, thank you. Have a nice day. Bye.
**Piotr Kiełkowicz** 15:07 Matteo?
Any important topics for the beginning?
**Matthew Hensley / Grafana Labs** 15:15 Nope, nothing today.
**Piotr Kiełkowicz** 15:20 So… I think we can just quickly go through the… at least issues and PRs.
**efshaikh** 15:37 I was hoping Zach would join in, because I was… planning to request him to review the PR.
**Piotr Kiełkowicz** 15:47 I think you should ping him on the.
**efshaikh** 15:49 Yeah, I think.
**Piotr Kiełkowicz** 15:50 He is green there, but he cannot join, probably. I do not have any message.
**efshaikh** 15:59 Okay.
So I requested review directly on the… GitHub.
**Piotr Kiełkowicz** 16:06 Sure. So, pull request, BMT or PR related to… this one?
stack workflow back for Windows 664, there is one… Pretty important stuff related to SQL Client.NET Framework 3 Context Propagation.
So, if you… if you have time, it would be great to… to review this, I was able to even, kind of.
ChatGPT, kind of diagram flows, which is kind of extremely useful to… for the understanding how the code is working, from… from my perspective.
But the code is kind of pretty… pretty solid, in my opinion.
He's sick, we wouldn't have time.
**efshaikh** 16:55 Yeah, I'll take a look at it.
**Piotr Kiełkowicz** 16:58 And the new issues… the Procreate web config… I think we have started discussion Someday and go, and… varies.
some discussions here.
But no big progress, so I will keep it as it is for now.
New discussions… Yeah, issues are correct, no new discussions… I think we can skip the… Skip this project board check. Also… I will check one more.
I think if we are still using correct calendar, because… There is a chance that we are using the legacy one.
And what was the link in our docs?
Yeah, this is the same, exactly. So, we are good.
If you do not have another topic, we can make the meeting shorter.
**efshaikh** 18:59 Yeah, sure.
**Piotr Kiełkowicz** 19:02 See y'all next week!
**efshaikh** 19:03 See you. Bye.
