SIG: .NET Auto-Instr SIG
Date: 2025-10-01
Duration: 24 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 02:22 Hello, guys.
**Yevhenii Solomchenko** 02:27 Hello.
**Piotr Kiełkowicz** 02:35 My kids are a bit noisy today, so, like, could you drive today?
**Zach Montoya** 02:43 Yeah, yeah, I can trust.
Let's get that up here… Alright. Yeah, let's go ahead and get started.
Let's see… So nothing, in particular I want to discuss, so I'll just go straight through our typical agenda.
Alright, we got… a good number of PRs open.
So we've got a couple of file-based configuration work… Couple of non-dependabot ones.
I think this N-Log one… This one's been open for a while.
I looked at this myself, and this… Looks like it was close to being completed.
Piasa, do you have any… .
**Piotr Kiełkowicz** 03:47 I've spent, kind of, couple hours for the review and fixing issue. Not hours today fixed, pests.
Just, fixing assertions, because additional spaces, so no big deal.
**Zach Montoya** 04:03 I think I can…
**Piotr Kiełkowicz** 04:05 Finally, look into it tomorrow and merge.
**Zach Montoya** 04:09 Okay.
Sounds good. Did you want to wait on… There was one snake foot. Did you want to wait on there?
The review at all?
**Piotr Kiełkowicz** 04:20 I think this guy is completely unhappy with current bytecode solution.
To be honest.
**Zach Montoya** 04:28 Yeah, probably. That makes sense.
**Piotr Kiełkowicz** 04:31 So, I understand why, because he would like to have a library ready to utilize also outside this auto-instrumentation package.
But it's kind of counterproductive for us.
**Zach Montoya** 04:47 Yeah.
Okay, yeah, I haven't seen… I don't think I've seen their review anytime recently since I waited and, steered, the author to use automatic, so…
**Piotr Kiełkowicz** 05:01 Maybe you can ping him, and we can wait for one more day, or until Monday, and then merge.
If you think it is worth.
**Zach Montoya** 05:16 I'm not sure, yeah, I'm not sure it will be. I think there was some good conversations about trying to optimize it, slightly, like, optimizing the usage.
But I think all his… all the suggestions were taken into account already.
**Piotr Kiełkowicz** 05:31 Okay.
**Zach Montoya** 05:32 Yeah, it's gonna be fine.
**Chris Ventura** 05:33 The part I don't understand, if they're requesting a library.
That can be used outside of auto instrumentation.
My assumption is n-log already has, integration with iLogger, and that's all that's needed.
So, that's the part that I'm not understanding.
**Piotr Kiełkowicz** 05:56 Maybe I… say it wrong, there were kind of interim implementation in this PR, Where there were created and lock specific, our library, which allows to put layouts, I think?
Okay. Into the file configuration.
If I unders… if I remember correctly.
But it was highly dependent on analog and his nightmare.
library dependencies.
**Zach Montoya** 06:35 Yeah, and they're also opting for just, code configuration, which for us wasn't… yeah, was also gonna introduce those dependencies.
Okay, so yeah, this is looking, like, in good shape. Hopefully the… Various, fixes here will… Start passing, and then we can merge that.
Let's see, so… Steve Gordon was working on this, bytecode rewriting. I think he… we've left some comments, so I think he's going to go address those. I'll follow up on that.
Various file-based ones. I didn't have any chance to look at any of these last week. I might have time to look at… I should have time to look at them this week, at least, one or two of them.
Is there an order in which these need to.
**Piotr Kiełkowicz** 07:29 the…
**Zach Montoya** 07:29 Or are they independent?
**Yevhenii Solomchenko** 07:31 No, I don't… No, no.
**Zach Montoya** 07:35 Okay.
Any…
**Piotr Kiełkowicz** 07:38 It will be great if you can review also the last one. PR, you or Chris?
**Zach Montoya** 07:44 This one, the instrumentation configuration?
**Piotr Kiełkowicz** 07:47 The… the last one, base functionalities for configuration-based instrumentation, yes.
It is more or less ready, in my opinion, for the kind of…
**Zach Montoya** 07:59 Oh.
**Piotr Kiełkowicz** 07:59 I don't.
Yes.
**Zach Montoya** 08:03 Okay.
Oh, okay, I think I remember this from a long time ago.
**Piotr Kiełkowicz** 08:07 Yes, there is a lot of… Places to improvements, and lacks of, kind of, basic functionalities, but it is big enough to review.
Okay.
**Zach Montoya** 08:22 Yes, I can take a look at that.
**Chris Ventura** 08:24 Yeah, I think I finally have time either today or tomorrow.
**Piotr Kiełkowicz** 08:28 Yep, that'd be great.
**Zach Montoya** 08:31 Boom?
Alright, we'll follow up there.
And then we have one small, installation detection So we can take a look at that offline.
**Piotr Kiełkowicz** 08:45 Oh, okay. But he's complaining that he do not want to send easy CLI for… small fixes.
**Zach Montoya** 09:02 Okay, well, I guess we can, We can reauthor this. That's so small.
Okay.
Alright.
Okay, so that's all the PRs. Are there any… any topics, well, any high-level topics we should discuss on the PRs?
Over here.
Alrighty, so let's continue on… Yeah, we kind of covered all the non-dependent bot ones. New issues… We have one new one about making .NET startup hooks optional. That's actually interesting. With any responses yet? Oh, okay.
I see. Okay, so this user is… wants the ability to choose to do CLR-based… Rather than a startup hook.
Interesting.
**Igor Kiselev** 10:06 Yes, so it's, we are from OpDynamics' main requested for it, and we are willing to, do it and, make the change, so now we are… we'd like to discuss if the suggestion is acceptable, if it would… if… any… problems you see anyone else see with that option, so our idea is to either use the same way as we do in .NET framework and Instrument, some early methods, or just, probably instrument, some methods in Core Seller itself that, loads startup hook, and if customers have not set startup hook.
Instrumented and inject OpenTelemetry, hook all… only in that cases. So… In that case, we would not require customers to set both startup hook and, Profiler environment variables.
That helps help in some areas.
bundling scenarios when we would like to bundle OpenTelemetry with other existing tools, and don't want customers to modify the existing They have ways they configure it.
**Chris Ventura** 11:24 Yeah, so the… Oh, go ahead. Yeah, so the one gotcha that we ran into that pushed us to, always using the startup hook, at least on the .NET side of things, was, we originally had this implemented so that we did the same injection and startup that we had for .NET Framework.
But there was a timing issue with the selection of which method was, Being injected into early on in order to get everything bootstrapped.
And that led to certain types that we needed from the runtime not being available.
And so, switching to the startup hook.
seemed to work. Now, with the proposal in this description about, injecting into some of those startup hook-specific methods.
That might work around some of those limitations or issues that we ran into, but it'll be something to keep an eye on if this approach is experimented with.
**Zach Montoya** 12:40 Yeah, I think… I think it… well, from my recollection, it might not be completely accurate, but I thought it had to do with the, like, async, async program methods. Or maybe it was the… Infrastructure for, Was the… what's the mode where you just do, like, one file?
I'm missing terminology at the moment.
But where you only had one file, and you just said, like, a file, you didn't even have a program, it was auto-generated. I think it was, like, that infrastructure.
**Chris Ventura** 13:16 So, so it's more than just a startup hook, and so, if I remember right, the crashes that we were seeing were before we even supported?
Some of those, what is it? Not the single file scenario, but where you publish the runtime with your application.
I'm forgetting the name.
**Rhynier Myburgh** 13:42 container?
self-const.
**Chris Ventura** 13:44 Yeah, the self-contained.
And so… because initially, we didn't support the self-contained scenario, because we couldn't bring the set of dependencies with it. But then we added support for the runtime store environment variables.
And I believe, and Raj, correct me if I'm wrong, that was what brought us some improved support for the self-contained, deployment scenarios.
**Rajkumar Rangaraj** 14:15 Yeah, that's correct, Chris. Like, this covers the… all the areas of the support. Earlier, we did not have the support for self-contained enlar.
**Chris Ventura** 14:31 So it's a little bit more than just the startup hook environment variable that's… necessary in order to make things… things work.
**Igor Kiselev** 14:40 We know about it, we have some ideas how we may change assembly loading in future to make a customer not required to set that additional environment variables.
It would be a little bit later, so we started with startup hooks, because it's easy fruit.
Easy hanging fruit, so… We understand that it would be more than such.
**Rajkumar Rangaraj** 15:13 Yeah, probably, like, I don't know why you are exploring why .NET startup hook is an issue. Probably we should not… it should not be questioned, like, to make the startup hook as an optional layer, rather than that we need to understand the issue, what you are running into it. Maybe someone else…
**Igor Kiselev** 15:30 You know, The issue is we try to bundle Hotel into existing product.
And for it, we don't want our customers to make any additional new configuration.
**Rajkumar Rangaraj** 15:43 Okay.
**Igor Kiselev** 15:43 So, that's specifically our problem.
And we can solve it without changing anything in OTEL, because we can bundle that additional logic inside our product.
And have it do all patches on our side, but we just think that it would be useful for every hotel customer, so that, visit one less environment variable to configure.
**Rajkumar Rangaraj** 16:10 Just wondering, why are you using auto-instrumentation? If it's your product, why are you using auto-instrumentation instead of the SDK there?
**Igor Kiselev** 16:18 Because our product is an APM product, and our goal is to give a customer Oh, wait till.
**Rajkumar Rangaraj** 16:27 Okay, I understand that. Now, with a pure smile, it's all I understood what's it, yeah.
Yeah. Yeah.
**Piotr Kiełkowicz** 16:36 Abdi has proprietary agent, let's say.
**Rajkumar Rangaraj** 16:38 Yeah.
**Piotr Kiełkowicz** 16:39 And now we need to… and it is part of Cisco, like Splunk, and so…
**Rajkumar Rangaraj** 16:44 Yeah. I got that part, yeah.
**Piotr Kiełkowicz** 16:46 Okay, done. Cool.
**Igor Kiselev** 16:51 That's why… that's why we are looking for guidance. So we… we can start with implementation in hotel, if it looks feasible, and discuss it later. If it would not be feasible, we would move it to our preparatory part, if it would be feasible, we would… if anybody have some concerns that we should not even start, we would start with… inside our perpetry code from… from beginning.
**Rajkumar Rangaraj** 17:15 Sure. So, here's one thing I recommend you, like, as you have your own product and everything, if there is a customization done, I did the, like, startup hook a long time back. I would recommend you to go and read the startup hook.
documentation, again, there is a way, without environment variable, we can get this hooked up. You might need to have your custom startup hook written and wire up this, that, and everything. That is something you can do to customize it.
**Igor Kiselev** 17:49 we know about it, but it's… we have a lot of different ways how our users can install us, and we don't have a control over… so… I don't believe there is any other ways for us to satisfy a requirement that customers should not modify anything on their environment, and the installation process should not be changed at the same time.
Be able to load, Hotel art instrumentation.
**Rajkumar Rangaraj** 18:21 Got it.
**Chris Ventura** 18:22 The other thing you might be able to do is… The… from the… native code side of things, you might… it might be started early enough that you could set some environment variables for that.
**Igor Kiselev** 18:42 No, it's not possible, because that environment variable are loaded and cached by a seller even before the profiler is installed. So, by that time, we could not modify environment variables. We already investigated that.
**Chris Ventura** 18:59 Yeah, I know it works for some things, but not all, so good to know.
**Igor Kiselev** 19:04 For both that and, share it, and share it entirely, so for a list of, platform-trusted assemblers, it's too late to modify it inside the profiler.
**Piotr Kiełkowicz** 19:19 Igor, so I think you can try to bring Pierre here, but it would be great if you can add self-containing application to the coverage. I don't remember if we have anything like this in our pipeline, and… verify it is working with your notifications. If not.
**Igor Kiselev** 19:43 We would verify that it at least would not make life worse, so we would, validate that it… As a, either not work and not work the same way as not setting an environment variable at all, or fully work. So, we would verify that we would not add any additional customer application crash or something like that.
So that we definitely would check.
So, I'm not saying that, our solution would make all possible, customer… types of customer application, fully working and fully supportable without the startup hook, but it would mean that, okay, for some customer, it would be optional, for some customers, it may be still not optional and still required.
**Zach Montoya** 20:45 Alright, so I'll just, I'll just document here, like, from here, like, no, no objections, but we want to make sure to… Let's cover scenarios that… We had difficulty… with… and… and pause us to… Views.
Sort of.
Next by default… Right? What's up?
**Igor Kiselev** 21:22 Okay, good luck.
**Rhynier Myburgh** 21:24 Yep. Okay.
**Zach Montoya** 21:25 Thank you.
Alrighty, so that's… we have, some of these existing ones, but unless there's any requests, we can just, like, leave these here. These, for the majority of them, seem to cover the file-based configuration work.
So, let's move along… Discussions… probably nothing? Yep, nothing.
Let's see… Issues that should be assigned a project, Nope, nothing. And then project board… This one, I think the only recent changes were… we added the SQL client by transportation last time from committed to in progress.
And then we added the support for Mac OS R64. I haven't taken a look at that yet.
But yeah, other than that.
**Piotr Kiełkowicz** 22:27 I think you can include… changes from the script we have discussed today into your PR.
**Zach Montoya** 22:35 Oh, yes. Probably it will be needed.
Yes, good call. Okay, let me… Okay, goods.
Alright, any updates?
It looks like, I don't think there's any updates we need to make, but… Alright, so I guess this looks good, and so that concludes our regular agenda.
Are there any other topics you guys would like to discuss?
Alrighty.
Well, I'll try to get to some of those PR reviews to move up… move along some of those work, but otherwise, yeah, thanks everyone, and catch you next time.
Bye.
