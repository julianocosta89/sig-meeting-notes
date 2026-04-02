SIG: .NET Auto-Instr SIG
Date: 2026-04-01
Duration: 51 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 01:54 Hi guys, I think we can start.
Can you hear me?
**Yevhenii Solomchenko** 02:06 Yes.
**Alexey Pukhov** 02:07 Yep.
**Piotr Kiełkowicz** 02:25 So… Let's start with PRs. There are two related from the PandaBot, nothing fancy there.
I will open… Ready to review only.
Alexi, the first one is related to executing native tests also on Linux.
**Alexey Pukhov** 02:55 Yeah, must…
**Piotr Kiełkowicz** 02:56 Chris.
**Alexey Pukhov** 02:57 Yeah, and that is… there is one test that I missed during the original PR.
**Piotr Kiełkowicz** 03:03 If you're feeling that it is fine, we can merge it as is, but in fact, it will be not executed.
**Alexey Pukhov** 03:11 Oh.
**Piotr Kiełkowicz** 03:12 In the city.
**Alexey Pukhov** 03:12 Whoa.
Sad.
You know, anyway, I mean, it's nice not to have any unnecessary restrictions on the test that can be potentially executed, but… you know, I honestly don't mind.
Thank you for the comment, yeah, this is a bummer.
**Piotr Kiełkowicz** 03:35 Yep. We have a task for it to… to… To fix it, kind of created, 3 years ago? Or something like that?
**Alexey Pukhov** 03:44 Better late than never.
**Piotr Kiełkowicz** 03:48 Yup, and this one… I think you have some discussion with Igor.
**Alexey Pukhov** 03:54 Yeah, this one, actually, it's an interesting question. Like, this is something I didn't notice, when I did this change initially.
Is that… And basically, there are two things I can do. I can just literally do, remove the side effect that I introduced in the original PR, or we can think about if we want the assembly resolver for the NuGet deployment.
it's effectively no op there. I don't see any way the assembly resolver can really contribute.
In the NuGet deployment. However, I don't know if… if there's… anything, like, I mean, if there's… any potentially use of the assembly resolver on the NuGet deployment, where the customer just used the net and netfix folder to put Some libraries there, and they will be picked up.
That's the only… M… thing that is possible for the assembly resolver to work on the NuGet deployment.
I mean, it's a stretch.
Kind of. But, I mean, this is something that Igor brought up, and I agree with him. This is potentially a change of behavior, if we go with an option 2 as well.
So, just wanted to point that out.
Before I proceed with option 2.
But option one, we should definitely do.
**Piotr Kiełkowicz** 05:42 I do not have a clear answer here.
**Alexey Pukhov** 05:46 No worries.
**Piotr Kiełkowicz** 05:46 No.
**Alexey Pukhov** 05:48 So, I mean, in that case, you also asked if we need anything before we are ready to release. This one… overall is not really required. I mean, it's still optional to do, so… I don't want to hold the release just because of this.
Pull request.
But again, if you feel like it should get in.
At least with an option 1, then… We can make it.
**Piotr Kiełkowicz** 06:18 Zach Rash, any comments here, or you would like to kind of look into it later, and… Discuss offline?
**Zach Montoya** 06:28 I will need to follow up. I'm not sure I understand right now the.
**Piotr Kiełkowicz** 06:35 The same on my side, so…
**Alexey Pukhov** 06:39 So, let… I mean, if you guys have time, I can try to…
**Piotr Kiełkowicz** 06:43 Yeah.
**Alexey Pukhov** 06:44 it a little. So, what we currently have with Assembly Resolver… so, I mean, Assembly Resolver is searching the libraries in the specific folder structure, which starts from NAT or NATFX on NET Framework.
So, essentially, right now, it is not doing anything for the NuGet deployment, just because On the Nugget, the folder structure is different. All the files are either in the root of the… test of the application out, put all they are in the runtime folders. So, effectively, even if we hit assembly resolver, it's not doing anything.
And, since this is a NuGet deployment, all our assemblies and all our dependencies are already in the TPA, So, we effectively never called, handler that would resolve anything, because there is nothing… I mean, nothing that .NET doesn't know.
About us. So, That's why originally I just disabled… I mean, like, okay, you don't need assembly resolver for the NUGI deployment, let me just disable it, because that will also disable the switch of the contextual reflection that is really producing the side effect.
But then Igor brought up a valid concern that, hold on, but if a someone use the zip archive.
Which has the right structure, but decided to disable the redirection using the environment variable.
Right now, the assembly resolver will still be working, and the way it will be working, even if the folder structure is correct, you're on zip deployment.
but you disabled the native redirection, the assembly resolver will still be able to locate our libraries. Like, all the OpenTelemetry libraries, all the dependencies that are not referenced in the customer application, but are in our folders, it'd still be able to find them.
While if I do what I'm doing, I'm actually breaking this use case completely.
That's that?
Yikes.
Since, again, we don't know why would customer disable the environment variable in this case, but it's still a valid situation. If the customer thinks that with the zip archive deployment, they don't need native redirection, they kind of handled all the conflicts on their own.
the assembly resolver will… will be finding our proprietary assemblies, like OpenTelemetry DLL, and OpenTelemetry Auto Instrumentation, all those things.
**Piotr Kiełkowicz** 09:39 All these things which are in the root folder of zip files, yes?
**Alexey Pukhov** 09:43 They are in the net folder.
**Piotr Kiełkowicz** 09:46 Okay.
**Alexey Pukhov** 09:48 It's… it's the… when I said Zee Archive, it's like when you install OpenTelemetry not through the NuGet package.
**Piotr Kiełkowicz** 09:56 And why do you think it is a breaking change?
**Alexey Pukhov** 10:00 Oh, I mean, it's a break-in change only if you disable the environment variable.
**Piotr Kiełkowicz** 10:08 Okay, so…
**Alexey Pukhov** 10:09 Because that's what I did in this pull request. If I detect a NuGet deployment, or the environment variable is disabled.
I disabled the assembly resolver, and this is a breaking part.
**Piotr Kiełkowicz** 10:22 No problem.
**Alexey Pukhov** 10:28 We just… I mean… Which is true, I mean, this is a valid use case, if you decide to handle conflicts on your own.
So you don't need native redirection, you still need assembly resolver to find our assemblies.
**Piotr Kiełkowicz** 10:45 That's true.
**Zach Montoya** 10:46 So if you disable it, then we won't even look up our dependencies like we would before?
**Alexey Pukhov** 10:51 Yep.
So yeah, that we definitely should not do.
But the question, do we still want to disable Assembly resolver if it's pure NuGet deployment?
So we don't look… so, basically, we only, we don't look at the environment variable, we just look at whether it's NuGet or not.
**Zach Montoya** 11:20 If we're already in the, like, trusted… the TPA list, I don't see why we need to keep running the assembly resolver.
**Alexey Pukhov** 11:29 Except, if there is undocumented feature that the customer decided to put some plugin for, libraries into the… net folder.
And we just fined them and load them.
I don't see us ever documenting this.
What if someone did use this?
Dad was… I mean, which, this is very exotic.
**Zach Montoya** 11:56 Wouldn't that be… I mean, unless they… developed and deployed it separately from the app, wouldn't that also be inside the app folder and within the TPA?
**Alexey Pukhov** 12:08 I mean, if they reference it in their project, it's gonna be in the output folder.
It's only if they really went with something exotic and decided to drop some files into the NAT folder.
Not a fix, just because they noticed we use them.
**Piotr Kiełkowicz** 12:26 Do you know… do you mean plugins? You mean auto-instrumentation plugins?
**Alexey Pukhov** 12:32 No, like anything else, literally. You can…
**Piotr Kiełkowicz** 12:35 So, I would not consider this as a breaking change, to be honest.
**Igor Kiselev** 12:40 about our instrumentation plugins, so I don't know who and how use different plugins, so I believe For some, we would install a plugin through a NuGet package, but if some people use it as a hack to drop a plugin…
**Piotr Kiełkowicz** 12:57 No. It is… it should not be considered as a breaking stage, for sure.
Packs are not breaking changes.
**Chris Ventura** 13:07 Yeah, I agree, it's too much of, undocumented behavior.
For us to… to say that we need to support it.
**Alexey Pukhov** 13:22 Well, yeah, I do agree, we never claim that We will support this.
Then, you know what, guys? I'll let you look at the change.
And the comment lets you to sit with it, and, you know, feel free to comment, and I'll, proceed.
With whatever we decide to do.
**Piotr Kiełkowicz** 13:54 Yeah, in general, if it is something fully undocumented, it is not kind of common behavior and expectations. We cannot… We cannot treat it as a… Kind of official contract between us and the end users.
**Igor Kiselev** 14:13 It's an interesting thing, because.
**Alexey Pukhov** 14:15 I don't.
**Igor Kiselev** 14:15 think anything about plugin, how you need to deploy them, how you need to use them, we don't have any documentation for it.
So it's a wild bird.
I believe.
Do we?
When we get…
**Piotr Kiełkowicz** 14:28 There is a plug… there is a plugin.
marked out, I think, documentation, but yeah.
**Chris Ventura** 14:38 Yeah, I don't think we specify how to deploy the plugin with your application. We just give an example.
**Piotr Kiełkowicz** 14:49 But keep in… keep in mind that plugins are still in the Hmm.
**Chris Ventura** 14:55 Experimental.
**Piotr Kiełkowicz** 14:56 Experimental mode, and there is a clear statement that you need to verify your plugin with exact, Auto-instrumentation version.
And you can expect that it will be working between versions, even with minor or parched changes.
**Rajkumar Rangaraj** 15:17 Yeah, that… I… I also agree. Like, I'll give a story about how we use it, the plugin. Like, we use the plugin, to hook up the Azure Monitor Exporter and do some modification to it.
And, the contract is same as what Piotr says, like, even a minor version, if we need to change something to the plugin, like.
we could make it and… the plugin is tied up to the… each and every version that we release, the minor version or something. It should not be, like, be tied up to the… the major version. That's going to cause a lot of issue. We won't be able to help tweak the hook at all, if we do that.
**Igor Kiselev** 16:05 For plugins, in your case, your users get it through a Zplug installation, so you just drop everything in a folder, so it's not a NuGet installation.
Because the whole discussion right now, it's about, how users install plugins in NuGet installation.
If they use it through a NuGet package, also great, they don't have any problems. If they have some different approach.
It may be a problem.
**Rajkumar Rangaraj** 16:34 So this is how the package, we expect, the design, what we have it.
So we've taken up, like, a dependency on this NuGet package, and that's how the plugin is built, and the zip file is recreated again, like, with whatever the content we have.
That's what it uses, to make it easier and all that.
Yeah, for, like, if the NuGet reference is providing the indirect reference to the OpenTelemetry package, I think SDK, I think we are covered here. I don't think there is nothing much about that.
**Igor Kiselev** 17:19 Thank you.
**Piotr Kiełkowicz** 17:29 And the instrumentation stability proposal. To be honest, I was able to look only into the OTAP.
And I've commented there.
I think we should wait for the final decision, what is… what is done in the OTAP, because there's kind of hard discussions.
**Chris Ventura** 17:52 And I think that's fine.
So if we want to close this in the meantime, that's fine with me, put it to draft.
I don't have a strong opinion.
**Piotr Kiełkowicz** 18:15 What else? No issues?
Sorry, my computer is still not working as I would like.
Helpool.
Initials, first one.
I would put to 116.
Priest to do not look into it every meeting.
I think here is the… Time where… where we… when we should decide about the… Future of this.
We have now the oldest possible version, as I understand, and we… it is different than for the .NET framework, where we have always the newest possible version at the time of the release, yes?
**Igor Kiselev** 19:36 Yes, it is a current state, as I understand.
**Piotr Kiełkowicz** 19:41 So, again, guys, we need kind of broader… discussions about this. I'm not sure if you would like to make it now, or… Orita about this… Once again, and comment later.
**Igor Kiselev** 20:02 I seize it.
I personally prefer to have the same strategy for both .NET and .NET Core, so at least if we use, let's say, we could use for .NET Framework the strategy latest match, the… Is that… s… latest measure with the same version that is used for latest measure in .NET, but I really don't like situations that we have, 10.08 in .NET Framework and 10.00 in .NET.
So, I don't have a strong opinion versus, if we have… if we should have a latest hotfix, or, HCK to, oldest known, non-vulnerable, Minor.
It have benefits in both directions, but… I don't like that we have a different version. It makes… It makes, specifically for me, a harder process of, validation which third-party dependency we includes, because now we include a different version of the same package, and I need to disclose all versions that we include.
So… and probably it's not… I'm… I'm not the only one who is affected by that.
**Chris Ventura** 21:24 Yeah, it gets complicated, though, because with… .net, apps… They're likely going to get the latest version if they're keeping their systems patched.
Just because it'll be in the, part of the runtime.
**Igor Kiselev** 21:47 Maybe, maybe we'll be part of runtime, but we again talk about that libraries will be part of runtime for ISPANET. They would not be part of runtime for console application.
**Chris Ventura** 22:01 I mean, depending on their deployment model, right? If it's self-contained versus…
**Igor Kiselev** 22:06 No, I'm not alone.
**Chris Ventura** 22:07 And then…
**Igor Kiselev** 22:08 not only on the runtime, if they use, .NET, base image, and if they are platform, dependent, the library that we use included. So, all that Microsoft extension, they are included in ISPANET, deployment, but they are not included in console application. In .NET, they are part of extensions, so that's why if they use Microsoft.NET .NET image, it would not automatically include latest version of the libraries.
**Chris Ventura** 22:41 Yeah, I was thinking more of diagnostic source.
**Igor Kiselev** 22:44 Diagnostic source, yeah, but for diagnostic source, it's a little bit different. Right.
**Chris Ventura** 22:50 Yeah, whereas with .NET Framework, for all of the dependencies, they just… they're not there.
So, yeah, that's where it gets complicated, but yes, I keep forgetting about the Microsoft Extensions packages.
**Igor Kiselev** 23:09 That's what I'm much more worried, and we already have a different model from Microsoft System Diagnostic source, and everything else. So… I less care about, in that specific case, about Microsoft Diagnostic source, but I much more care about other dependencies.
**Chris Ventura** 23:32 Yeah, so… so maybe I… I… I can agree with you about oldest, non-vulnerable patch.
Just to get them, aligned.
**Alexey Pukhov** 23:52 And when we say oldest patch, does it mean that it's oldest across?
**Chris Ventura** 23:59 Whoa.
**Alexey Pukhov** 23:59 Or it's a base… oldest baseline, for Node.
**Igor Kiselev** 24:04 B means that we still use the C. It's an interesting question. So, I'd say that we follow the model that, for .NET, we use, C major, oldest, non-vulnerable.
**Alexey Pukhov** 24:18 848949…
**Igor Kiselev** 24:21 Yes. And for DOT… Net framework, we use latest, measure, oldest, not vulnerable.
**Alexey Pukhov** 24:32 Just major… so it's… The latest 4.8.
**Igor Kiselev** 24:39 So, okay, for .NET Framework, it would be most probably 10.00.
**Alexey Pukhov** 24:45 10 variables, okay.
**Igor Kiselev** 24:46 In that case, for .NET Framework. For everything else, for 8, it would be 80049900 for 10-10. But at least we would not have a situation that we have 1000 and 10.07 at the same archive.
And, because it would also surprise our users that they don't understand what they are actually using.
**Alexey Pukhov** 25:16 Nope.
It sounds…
**Chris Ventura** 25:30 Yeah.
**Igor Kiselev** 25:31 I would add… I would add the suggestion in the ticket after the call, and then we will work on creating a pull request that would allocate everything to that suggestion. We will still have a chance to look and trade and discuss and think a little bit more about system diagnostic source, offline Let's… let's just start looking what we will have.
And how the land trust builds the work.
**Piotr Kiełkowicz** 25:59 4 tick to 1.15 right now.
And looking for comments with some Argo.
Another comment here, Chris?
**Chris Ventura** 26:18 Nope.
**Piotr Kiełkowicz** 26:30 Ryan, Ryan, what is… joined… not yet. I think he's still some kind of… Extended 40 days? Whatever.
**Igor Kiselev** 26:40 So, but here is, we already get confirmation that it is not needed, so…
**Piotr Kiełkowicz** 26:48 Okay.
**Igor Kiselev** 26:48 We could, then, we could, Discuss if we could remove using of it, because otherwise we use substance that is not needed, or if it is, we would still use it, because there is no harm from it.
And we could either discuss it in the same ticket, or close it, because it was a question, and discuss it in a separate ticket. I think it's better to, take a decision here, if we…
**Piotr Kiełkowicz** 27:16 Great.
**Igor Kiselev** 27:17 Can I remove it or not.
I personally prefer to not have Any setting that is not needed.
If it have no harm right now, who knows what it would be in future, but… If, yeah, if anybody thinks it's risky, we get left at least.
**Chris Ventura** 27:42 Yeah, Raj, I'm assuming that you're still relying on the startup hook only and ASPNET Core hosting startup.
stuff for the Azure use cases.
**Rajkumar Rangaraj** 27:57 That's true.
**Chris Ventura** 27:58 Is that correct?
**Rajkumar Rangaraj** 27:59 Yep.
**Chris Ventura** 28:01 So that's a scenario where there's no profiler, so we still rely on those two settings to make auto-instrumentation work there.
**Igor Kiselev** 28:08 pie.
I understand that it's not about that if startup hook here, there, we still would have it injected by startup hook.
So that setting is actually required only in case if no profiler and no startup cook at all.
My personal understanding, I may be incorrect right here.
But that's why I suggest to remove it, because when we have a startup hook, that's still not needed.
**Chris Ventura** 28:39 Okay, so with the startup hook, it's early enough in the lifecycle that it can still set up that environment variable and have it take effect?
Is that what you're saying?
**Igor Kiselev** 28:51 Hmm.
I may be incorrect, but I understand that we don't need even… that startup hook is still enough As we already load our instru- our, Instrumentation, and it, so our installation would inject, that in any key.
So maybe I'm wrong. I may look into it a little bit deeper.
**Chris Ventura** 29:19 Yeah.
**Igor Kiselev** 29:19 Even right now, with the current state, if we remove that environment variable and use startup hook only, nothing should change for end customers.
**Chris Ventura** 29:31 I didn't think the startup hook was able to… Wire up the… the logger.
**Rajkumar Rangaraj** 29:38 Yeah, I can give her details related to it. In the startup hook, we don't have access to the service collection.
So… we introduced this ASPNET Core Bootstrapper, where we have the access to the service collection. That's how the, iLogger… we have the control to the iLogger when we inject the, the OpenTelemetry hooks to it.
The startup hook in our case is purely an assembly resolver than anything else. We don't have any… like, logic to do, any other tweaks, or, like, it just says that how to load the, entry point. That's what the startup hook does in this case.
So, and the next thing is that, people may feel like I can just add this ASP.NET core directly in this environment.set, environment variable in this data book.
That's not going to work. The runtime needs this earlier than the startup hook. So, only then, I'm targeting all those terms. The loader will be loading all this library needed for that. That happens even before the… It's the startup hook part.
**Igor Kiselev** 30:59 interests.
It's interesting, I believe that Sataphook is the first one.
Because it gets controlled before the…
**Rajkumar Rangaraj** 31:06 You know, even a lot many things happened before the startup hook. That's why we could not control… if that is the case, we don't even need an assembly, depth, or whatever we have as a dependence, additional dependencies, or run things to.
**Igor Kiselev** 31:21 There are additional dependencies we need, because the power list is built before, but I don't think that any additional variables would affect the power list, so I don't believe… so, right now, my feeling is that that setting is actually, the… current startup process would be first.NET runtime will build up a list, then we get a control in our startup hook. After it, application entry point would get a control. Application entry point in ISPNet case would look… would check for the environment variable, and would load, it if it is defined. So.
**Rajkumar Rangaraj** 32:03 So, I don't know what we, like… it's a bigger topic or something like that, if you are just trying to avoid one environment variable is… used, and we try to avoid that. I don't think the effort that we put in for that is worth here.
This can just live there, and we have a core logic built into it to ensure that if it is, like, if the logger is integrated already in Core Profiler, the bootstrap knows it need to ignore and moves it off. It just packs off. It does not do anything in that.
So, just want to understand the idea behind it. If it's just to, like, remove the one environment variable in case of, like, we set it through CLR, I don't think even it's worth a thing to battle around this one.
**Igor Kiselev** 32:52 Is there a lot of things that I don'.
**Rajkumar Rangaraj** 32:53 to this one.
**Igor Kiselev** 32:54 I don't have any strong opinion about that. From my point of view, it was about supportability and understanding the process, how our applications start up, and where we can expect any hard issues. That was found mostly while we discussed about how to implement assembly Resolver, if we need to think about it.
And at that point, we realized that we do not fully understand how it works.
Then, once we started the discussion, we end up, even now, even today, that nobody fully understands how it works, and it creates some additional risks That's why my suggestion was, like, if it is creating some additional risks, and nobody understands how it works, and we have a suspicion that it may be enough to remove it. Probably it's safer to remove and enable it only in particular configuration when it is required.
If right now, we deem that it is safer to stay it as is, let's just say that, okay, we believe that in many configurations it's not needed, but we are not… we don't want to spend time validating all of that right now, so let's just left it as is. It was a ticket mostly open as a discussion point, and share a discussion about it.
**Rajkumar Rangaraj** 34:13 Yeah, I understand, Igora, but I have two concerns here with what you called out. You called about a supportability issue. You removing this is what is going to cause a supportability issue, because according to us, we have wired up all of this environment variable.
You go ahead and removing it, we need to just go on and handle this situation. This is what is going to invite us the customer problem and the supportability issues instead of removing, that part. The second thing is that, it's, it's surprising to hear that, like, no one knows what's happening.
So, just wondering why that's coming here. I think all the maintainers over here should be aware of the complete design and the architecture of the project, what's been here since a long time. Just want to hear from your… from you, if there is a gap, so that we can, figure out and fill in for you, if some part… parts are missing there.
**Igor Kiselev** 35:14 Okay, maybe I used a bad word, sorry if I was up. That's… as I said that we open an issue to understand a little bit better how that environment variable is used. So, I… right now, after the discussion, I have some concerns, because we… have a little bit different opinion, how… how a startup process works, but it's better to discuss probably in Slack, in their communication between us, and I, as I said that I agree that it's not worth, it was an open topic to discuss what is the safest and… most useful approach, and as I hear, that it's better to left it as is. I don't have any objections around tablets. Let's just comment that we don't think that it deserves change right now.
I just… from my point of view, I was a little bit worried that I'm not sure that we covered All the settings in all tests.
That's why… it may result in some problems, because we have not full picture when we've done some other changes on it, so it was mostly, as I said.
as a safeguard opens the ticket that let's discuss, and let's see if… if we are missing something. If we are not missing anything, great.
**Rajkumar Rangaraj** 36:45 Sure, sure. So I understand now. So the thing is that this auto-instrumentation repo has two kinds of enablement, one using the CLR profiler, and another using the startup hook.
And most of the cloud providers use the startup hook way of enabling the auto-instrumentation. The only one reason for that is the CLR profiler here is not multiplex. So the moment we use the CLR profiler from the auto-instrumentation, no other profiler can get injected into the process.
So that's the drawback that needs to be solved here completely, before the cloud providers can take a dependency on the, it by enabling it using the CLR profiler way. So that's why we have a, like, two set of things available here. But if you look at it, I know that recently there are a lot many things changed from the the profiler way of hookup. The earlier when we did it, the design, what we did is.
We had the startup hookup way. The CLR also… CLR… the profiler way also, what it does is it used to relay upon the startup hook and does the enablement. That's how it had been kept earlier. So I know we have removed… the recent times we have removed that dependency and everything, but At this point, I believe until we solve that other issue, these two parts need to coexist and shouldn't be changing. If it changes.
It's a big… I would consider it as a big breaking change for whoever uses… who does not want to take a dependency on the profiler.
**Igor Kiselev** 38:22 I don't suggest to remove a startup hook.
I, I, I even tried to do, to, make our best to still support it, and the ticket was very, very small, only about that additional ISPANET thing. But okay, let's, move the discussion outside of that meeting to not, spend time once, I would understand a little bit better, or I… or… we would understand each other a little bit better, we could return back and continue the discussion if needed, or we could just close the ticket already, so…
**Rajkumar Rangaraj** 39:00 Sure, sure. Pietro, you may know both the sides of the things, like, let us know, like, if anything is there, so that we can have a discussion to see, Like, something needs to be removed, or added, or without any…
**Igor Kiselev** 39:17 Sure.
**Rajkumar Rangaraj** 39:18 D.
**Piotr Kiełkowicz** 39:22 In general, we are going only about, About this call, one call you are discussing, yes?
Rash?
**Rajkumar Rangaraj** 39:43 What did you say? Like, I thought you were…
**Piotr Kiełkowicz** 39:44 That's the… there is… just to sum up the reason for the startup hook, this, this bootstrapper functionality, it is the only meaningful thing we are doing in this… in this code. It is just ingesting OpenTelemetry rocks from startup.
**Rajkumar Rangaraj** 40:02 Yeah, yeah.
And that also, if you look at it, the top one, right, like, those are the guards to ensure that… we ensure that CLR profiler touches it, we don't do anything here. It just returns it from there, yeah.
**Piotr Kiełkowicz** 40:24 Igor, I suppose that you will be reading the documentation carefully about this in the… short term. If you find any kind of… missing parts of what we have discussed, that it will be great to put even short notes with, kind of, references to the code.
**Igor Kiselev** 40:45 Yes, yes. I suggest to left a ticket open for a little bit more. I would use that just to confirm what I have found and what… how it works, I probably would confirm that it's already recommended. I would put a link to the documentation where we discuss about that.
**Piotr Kiełkowicz** 41:07 Cool. So, I will keep it as it is for this week.
**Igor Kiselev** 41:14 Thank you.
**Piotr Kiełkowicz** 41:16 Just discussed. We have two… Issues related to unsafe access or type.
**Alexey Pukhov** 41:26 Yep!
So, the native profiler might be a little easier to… Discuss, basically there is a draft pull request.
With a suggestion to extend the… IL rewriting for the unsafe accessor type.
I mean, it works, we just need to finalize it. That's gonna be actually one of the items on my plate.
sooner than later.
But I… again, we… it's gonna be a problem when we switch to DS Diagnostic sources version 11, so we still have time.
**Piotr Kiełkowicz** 42:10 So, it is not necessarily needed for the 1.15 release, but… For the follow-up, for sure we need.
**Alexey Pukhov** 42:18 future, yeah, whenever…
**Igor Kiselev** 42:20 It would be required… it would be required for the first release that would be after OpenTelemetry as we switch to System Diagnostic Source 11.
**Alexey Pukhov** 42:31 When is the timeframe for the .NET 11 to be released?
**Igor Kiselev** 42:35 member.
**Alexey Pukhov** 42:36 November, so we have a lot of time.
**Piotr Kiełkowicz** 42:39 Yep.
Putting for the next… next milestone. And what's about this?
**Alexey Pukhov** 42:44 Oh, dear, this is… this is a hard one.
**Igor Kiselev** 42:51 So, that's okay. It's both the same, but for startup hook.
And, current state, if we would not found any… if we would not do anything, then after we will switch to System Diagnostic Source 11, startup cook on .NET 10 would not work.
So, possible, solution right now first, everything. We could, deploy a script that will build, additional depths and, folder, the same way as it was before our change, and I would recommend to use it up to the day. It would not solve questions for… solve problems for everyone, but it will solve a problem for everyone for which it worked before our change. It is what we plan to do once again, before .NET 11 timeframe be… Promised.
develop it. And, if, And in parallel, as I said, I will open a ticket with .NET runtime, I would describe what we have, I would get an opinion what can be done on a .NET runtime side.
maybe we would get some great ideas. It would be a little bit easier for me now, because right now I could not say that we are planning to do something that will be breaking in .NET 11, but I could say that, okay, OpenTelemetry used that hacks, or approach to get an ability for users to load it from a separate folder from a ZIP deployment. But that approach worked with 8, 9, 10, but will be broken once .NET 11 will be released.
If nothing would be changed and, would limit… NET customers who are trying to use, OpenTelemetry Auto Instrumentation as drop-in, so probably we can found some solutions. So, version of the ticket, it was the main reason why I have not, Opened external ticket yet.
**Piotr Kiełkowicz** 45:18 Still, we have some time.
And… It is still… needs to be fixed before .NET 11.
**Alexey Pukhov** 45:27 Yep.
**Piotr Kiełkowicz** 45:28 Ritz.
**Igor Kiselev** 45:29 even probably a little bit later if, OpenTelemetry would not switch, on the first day.
Oh.
**Piotr Kiełkowicz** 45:37 It will switch.
We… I… we expect changes needed for… for… in SDK to… to support new required flag by the… W3C propagator.
**Igor Kiselev** 45:56 Okay, so is that this means…
**Alexey Pukhov** 45:58 November.
**Igor Kiselev** 45:59 November, December.
**Alexey Pukhov** 46:01 Yeah.
**Piotr Kiełkowicz** 46:02 Yep.
**Alexey Pukhov** 46:03 But yeah, the additional dependencies will be… will be back, probably. Well, most likely.
**Piotr Kiełkowicz** 46:12 Can we kind of just back the additional Dependencies only for… let's say.NET tenants.
Is it only for diagnostic source, or it's… Or which… it will affect all of packages, because if it can be targeted only for one library, I do not consider it a big problem, to be honest.
**Igor Kiselev** 46:38 It's a good question. We need to run our… we implemented, some tools to validate a set of assemblies. We would need to rerun the tools to get particular transfers for it, so maybe a huge chance that it, we could do it all around, system diagnostic source, and once again, it would be required only in, .NET 10 customers. Okay, in future it would be, for any customers that…
**Alexey Pukhov** 47:12 11 with…
**Igor Kiselev** 47:13 version of .NET than SDS that we use.
**Piotr Kiełkowicz** 47:20 So, I would consider short-term, I would consider checking this.
And if needed, creating… Even empty… additional… store.
even in… Time frame from 1.15 to… Kind of bring back the… usage of environmental variup to the North's border.
**Igor Kiselev** 47:49 Rosers.
**Piotr Kiełkowicz** 47:50 To switch from one to another.
**Igor Kiselev** 47:52 Right now, how it was designed, nobody required to remove the environment variables. They would not harm, so, even if it would not.
**Piotr Kiełkowicz** 48:04 We have removed it from the scripts and documentation.
**Igor Kiselev** 48:09 Yes, they have removed from scripts and documentation. So, for every customer that use our script, it… nothing would change at all. For customers that use it, probably we should command that We expect that that environment variable may be needed, and because there is no harm, we advise to not remove them from the scripts.
Absolutely, is that?
I suggest to solve it as a documentation, take it right now, but… but before next release.
**Piotr Kiełkowicz** 48:41 Nope.
So, putting this one to 115, partially.
And we need to tell a document this.
And I think that's all.
This one, last week. I keep open this discussion because there is no response from the… Outer… And the last one… Should I update the board, or we are fine?
For now?
I think it can be… it can be fine, and here is everything fine.
15 alts.
And… I would like to make a kind of cutoff for the beta version, if you don't mind.
I'm not sure this week or the… or the next one, probably after… We decide what to do.
Oh… Oof, whiffe… with this one.
Objections? Are we okay with this plan?
**Chris Ventura** 51:13 I think that makes sense.
**Piotr Kiełkowicz** 51:28 Do you have any other topics, or… We are fine for today.
See you. Next week, in this case. Thank you!
**Alexey Pukhov** 51:42 Bye, thank you.
