SIG: .NET Auto-Instr SIG
Date: 2026-03-18
Duration: 54 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz** 02:38 Hi, guys.
**Matthew Hensley / Grafana Labs** 02:43 Hello.
**Alexey Pukhov** 02:45 Hi.
**Piotr Kiełkowicz** 02:53 Hey, guys.
Give me a second… I think that we can start.
We can start as usual from new issues.
Go one by one.
increase already opened NPR to define this stability. I do not see any comments last week.
I'll try to look into it.
This… in the upcoming one.
We'll click on the comments here.
**Yevhenii Solomchenko** 04:13 I write one comment in the PR, it's about, no-code instrumentation, I'm not sure it should be in that… stability proposal.
**Piotr Kiełkowicz** 04:36 I think he already… this one is still waiting for mergers from Alexi, and then we can decide, yes?
**Igor Kiselev** 04:48 Which one… which one of it is a drawer?
**Piotr Kiełkowicz** 04:51 Version management strategy.
**Igor Kiselev** 04:54 Oh, yeah You can decide at any time, really.
**Piotr Kiełkowicz** 05:00 Sure.
**That's… Igor Kiselev** 05:07 We get a response here, so I believe that it is a confirmation that we can remove dependencies straight from default NuGet package. It means that if anybody needs it, they probably should install that specific package.
**Rajkumar Rangaraj** 05:25 Just a question on this.
Is it causing any issues? Because the way we have developed this is it should not conflict with each other. I know it's an additional enrollment variable, we could remove it. Has this caused any issues or anything?
**Igor Kiselev** 05:42 So, it is not causing any issues directly, but indirectly, it is one of a step, to solve, a NuGet, installation for SDK pack… For, Microsoft Net SDK packages, because it brings, NetFrame, net, ISPANET As the key dependency.
**Rajkumar Rangaraj** 06:04 Yeah.
**Igor Kiselev** 06:05 So we break, applications, but it's not only one, so… Rajkumar Rangaraj 06:11 Yeah, as far as we have the ASP.NET Core Instrumentation library, that is also going to bring the same dependency. That's why this was not solved, and we were fine during that time to have it.
**Igor Kiselev** 06:25 The separate sink itself would be… harder to understand what's the purpose of it, so we can just get some files that is never used, but we depend on, so… Rajkumar Rangaraj 06:37 Yeah, so if it's always a CLR profiler-based onboarding, yes, this can be removed, but if someone does not want to do anything with CLR profiler, the… This is needed, this is mandatory.
**Igor Kiselev** 06:51 But it's the same… but the script that, enable it is the same script that enables, ISPANET, that enables a profiler. So if they use instrument as such.
**In that case, both profilers and that will be enabled. But there is not using instrument as such. Nobody would enable, environment, variable unless they would do it manually, but if they would do it it's manually why we bring it by default with our NuGet packages, so… Rajkumar Rangaraj** 07:22 Okay, got it.
As far as we are not removing for, like, the startup hook approach, I'm fine with this.
Removing it from the profiler-based integration.
**Piotr Kiełkowicz** 07:35 I have a question if you're speaking about this. Do you have any End users, Relying solely on… Startup Hook without, filer.
**Rajkumar Rangaraj** 07:52 So, ours is, like, if you look at the implementation that we do within the Azure Monitor, it's a button click enablement or something like that. We don't provide or ask customer to take dependency on NuGet package or anything.
So, the way it is done is completely based on the startup hookers. So, right now, this feature is in private preview in AKS. It's completely based on the startup hook based. We don't use profoiler at all in that case. So, if removing something like this is a breaking change in those areas.
**Piotr Kiełkowicz** 08:28 Understandable.
I'm asking because, guys, from Abdi are mostly from Abdi, but also Instang, in general are looking to to… To improve the serving Assembly version conflicts, and the startup hook-only solution is kind of the most problematic.
Yeah. And I'm not sure if we'll be to… To mitigate all of cases.
**Rajkumar Rangaraj** 09:02 Yeah, but for a lot of reasons, like, the profiler-based hook is not the, one that we need to take it by default, because it might… we have a… it's not a multiplexer-based profiler, what we have it. So at the moment, we had this.
no other profiler can get attached to the process. So, we don't want… Yeah, unless that is solved, we don't want to take a profiler-based approach in enabling the auto-instrumentation. That's the reason why the Azure Monitor is not dependent on that.
**Piotr Kiełkowicz** 09:40 So, if we implement this multiplexer.
known from Microsoft stuff, it should be fine to drop it, yes?
**Rajkumar Rangaraj** 09:50 Yeah, if we have a multiplexer, I think it would be… but I think it's a… I think we did some initial investigation, I believe, a long time back, a very long time back, maybe 3 years before? I think that's a… a lot of effort from our side, I believe. That's why we just passed that and left it as it is. And we did not have a profoiler experts also around that time.
So I don't know how much it has changed with… I know, Pietro, you and Splunk is also driving a profiler-based effort. I don't know how much that has changed the equation here.
**Piotr Kiełkowicz** 10:27 Yup. So, a lot of change as we are working to get there with historically updated email, and they… Igor, Alexei, and other guys are kind of outers of providers' proprietary ways, so… Yeah, a lot of expertise there right now.
**Rajkumar Rangaraj** 10:51 Yeah, and… yeah, sorry, go ahead.
**Igor Kiselev** 10:54 We will probably create an issue, separate issue, where we will describe current state of a startup hook, and what problems we will see with it, and we will use that issue to collect opinion why a startup-only hook is used. I already get about a profiler, but let's get a full picture, if anybody uses it for some other purpose, and it will help us to make a proper decision how we.
**Rajkumar Rangaraj** 11:23 Yeah.
**Igor Kiselev** 11:23 Most of that in the future.
**Rajkumar Rangaraj** 11:24 So, the most of the cloud… it's going to be a challenge for most of the cloud providers, not only for Microsoft, any of the cloud providers, vendors. The issue that they're going to run into it is They may have their… right now, in this state, the only thing I see as a drawback in this one is, we cannot attach any of their native profiles once we do it with this approach to collect data.
So, that's where it is acting as a blocker, and we had to rely only upon this data pool. The moment we have that resolved, we have a profiler from the auto-instrumentation. It attaches and does only that job, and allows every other profiler to run along with that. That's the time I think we can… remove the startup hook and completely rely upon the other approach.
And I don't know whether you know about it, Igor, I'm also working upon the out-of-process-based instrumentation.
I had to de-prioritize because something high priority has come and hit my list internally. That's why I passed that effort for, like, the past 3 months. I'll be soon jumping into it and driving that. That's another branch in this one. So, that is supposed to solve many of the problems we see it over here.
So, that's how high, how I'm trying to solve the thing, and I have a complete support from the .NET team on it. I don't know whether you have taken a look, like, probably there is a demo also pending on me, or to do it in this SIG since a long time. So, I'll come back and, try and do that.
2.
NextGen is a folder name, Piotr, it's in the, nextGen.
**Piotr Kiełkowicz** 13:16 Okay, it was merged to me?
**Rajkumar Rangaraj** 13:18 Yeah, the next-gen folder is in the main, it will have some dock, but the… most of the work is in the out-of-process auto-instrumentation, so… Piotr Kiełkowicz 13:27 True.
Sure, sure, I… I thought that it was in the separate browser, but I.
**Rajkumar Rangaraj** 13:33 It's in a separate branch. It's still in a separate branch. This is the initial document we had put. In the out-of-process branch, we have it in the next-gen folder, all the implementation.
**Piotr Kiełkowicz** 13:44 Okay. Out of process collection, yeah.
**Rajkumar Rangaraj** 13:47 Yeah.
**Piotr Kiełkowicz** 13:47 Sure.
**Igor Kiselev** 13:52 Right now, I think it's not visible, but we will discuss it when we'll work on Alexis change.
**Rajkumar Rangaraj** 14:00 Yep.
**Piotr Kiełkowicz** 14:06 Hmm… unsafe accessor type. I think it is follow-up task for… Procurrent PR, do you… would you like to discuss something, Alexei, today?
**Alexey Pukhov** 14:23 Sure, definitely. I mean, this is related to.
**Piotr Kiełkowicz** 14:26 Like, this one, or… Sorry, this… this one or this one?
I was there.
**Alexey Pukhov** 14:32 There, there are two, well… Good question, which one to discuss first? Well, I mean, both of them are related to… to the PR that I'm doing, and both are related to the same new reflection that .NET 10 introduced, which is this unsafe accessor type.
which is a JIT-level reflection, which means that in the managed code, we cannot do anything if anyone decides to reflect Types from our dependencies.
From our conflicting dependencies.
Yeah, so, it will just bypass any managed things, like a switch of the contextual reflection context, and it will just load the dependency into default context.
And if it's a dependency that we would load otherwise into a custom context, then we have a problem. There are two dependencies loaded at the same time.
And the issue started in .NET 10 when .NET 10 started to load types from diagnostic source, which is just bad, bad, bad, bad, because this is a dependency that should have been loaded only once.
So, there are two issues, because they… this affects a little differently the native profiler deployment and the startup hook-only isolation… Sorry, startup hook-only deployment. So, with the native profiler, there is still a chance… well.
Not a chance. We can't fix it in the native profiler by extending our redirection. So, so far we only do the assembly reference redirection, but we can also extend native profiler to do redirection in those Attributes as well.
I have a draft PR to show that it's actually working.
That we can really do that. And probably this is the issue, is this the… Yeah, this is the issue about the native profiler. So, the reason why it's separated from the startup hook only deployment, because we don't have this issue right now.
But we will have this issue once, the .NET 11 will be released, and OTEL will switch to the diagnostic source version 11.
So why it is not reproduced right now? Because right now, everything is on 10.
And on .NET 10, we'll be loaded in diagnostic Source 10, and it will eventually be loaded in the default ILC, no matter what, for the native profiler. So that's why it's not an issue right now. Whatever is automatically loaded by this reflection to default ILC satisfies our approach.
But once hotel switches to 11, that's where the problem will happen, because .NET runtime will load version 10 into default ILC, and we would want to load 11 into a custom ILC. That's where the drift will happen. But the native redirection.
Can help us, we can redirect, we can change those references in the attribute to our version, and then we'll take care of it by the managed handler.
So, that's why it's a separate issue, because we don't have to fix it right now, we can fix it, later.
Well, the startup hook escalation, and thank you for bringing up a topic about the need of the startup hook escalation, because that's becoming more and more critical. So, for the startup hook isolation, it's an issue right now.
Because, Because it just loads the… this reflection will load diagnostic source into a default ILC, while for the startup hook isolation in the PR that I'm working on, we are trying to move as much things into isolated context.
Right now, we're gonna be having, an issue that we load two same versions of the diagnostic source in two contexts.
And this is bad.
So, the only thing we can really do right now is to just let Diagnostic source to be loaded into default ILC, including all the dependencies that Diagnostic source will bring in. This is the only thing for the startup hook that we can do right now.
Which will be working It's fine.
And it's actually working fine. I've already did the change.
Except when .NET 11 will be released, and we're gonna be switching diagnostic source to 11 version.
Same problem. The 11 will be loaded to… well, the 10 will be loaded to default ILC. We cannot load 11 into default ILC, and we just don't have any option.
And at that point, the only thing we can really suggest to the customers on a startup hook-only solution is to force synchronization of the diagnostic source to the version that can satisfy open telemetry, which means you either reference a diagnostic source 11 in your projects directly.
Or you go with the additional dependencies workflow. Alex?
**Piotr Kiełkowicz** 19:59 Alexi, sorry for the… Alexey Pukhov 20:01 Sure.
**Piotr Kiełkowicz** 20:02 It is not a regression against current state, not after your changes.
**Alexey Pukhov** 20:07 Yep, this is… I didn't check what's happening right now. I filed that issue on top of the change that I'm.
**Igor Kiselev** 20:14 So, it's a very tricky question. So, technically, it is a regression, but we would be affected by that regression only after, somebody would upgrade to… after hotel will upgrade to system diagnostics, source.
**Piotr Kiełkowicz** 20:34 No, no, no.
**Igor Kiselev** 20:35 11.
**Alexey Pukhov** 20:36 No, what?
**Piotr Kiełkowicz** 20:36 Against current state before merging it to… Before merging galaxy, it changes to domain.
**if… Alexey Pukhov** 20:47 The answer, I didn't look, so I don't know what's gonna happen with this, given we are not making the change.
So, with the current state of.
**Piotr Kiełkowicz** 21:00 Current state, auto-instrumentation is failing, for sure.
If you require higher version, then… than previous… then it's loaded by .NET runtime itself.
**Igor Kiselev** 21:14 But V… Alexey Pukhov 21:15 It's still a problem, no matter what.
**Piotr Kiełkowicz** 21:18 Yes.
**Alexey Pukhov** 21:19 Alright.
**Igor Kiselev** 21:19 Aren't our additional depth solves it?
sync.
**Piotr Kiełkowicz** 21:24 Nope.
Nope, it is not solving.
**Alexey Pukhov** 21:27 Why?
**Oh, oh, hold on, why? Because there is no direct dependency in the customer application to the diagnostic source, so… Piotr Kiełkowicz** 21:37 Yes.
**Alexey Pukhov** 21:38 Should additional… I mean, again, I didn't check it, but from my understanding, additional dependencies should affect the permission of the TPA list.
I actually don't know.
**Igor Kiselev** 21:50 I believe in a current state, it would be a problem if a customer have a direct dependency to SDM.
**Piotr Kiełkowicz** 21:57 Yes, exactly.
**Igor Kiselev** 21:58 will not have a problem if customers have no dependency to SDAS at all. In that.
**Piotr Kiełkowicz** 22:04 That's true.
**Igor Kiselev** 22:04 additional depth, boot up, downgrade. So, it's a current state. That's why. After, so if commercial axis change.
And will not do any additional workarounds on top of it. After OTEL would be releasing version… after .NET will release version 11, and OpenTelemetry will switch to System Diagnostic Diagnostic source version 11, then on for customers on .NET 10, it will be a problem, because additional devs dependence are deprecated, and there is no them anymore, unless we would provide some analog for it. But we are not able to correctly redirect an assembly, even for customers that currently have it. So we still have a some time frame to solve it, and solution, we discussed, first solution, we discussed that we could create a script that would, bring back additional depth solution, but not on our side, we would create a script that will restore it right at the client side.
So as installation time. Or… so, it would work the same way as it worked today, and would not be a breaking change for existing Customs accept installation step would be a little bit different. And, second.
I think that I have some hopes, I will create a ticket in .NET itself, talking about what happened and why it breaks us, and probably .NET would suggest some options there, because it's easily, solvable on .
NetSight.
But not solvable on our side, unfortunately.
Ugh.
**Alexey Pukhov** 23:53 Yeah, the problem is how they decided to introduce this new reflection that just have no con… I mean, there is no way to control it, so maybe they can provide something.
**Igor Kiselev** 24:05 It still would be a problem for .NET 10 customers, but most probably it would not be… if the solution would be found, it may not be a problem for .NET 11 customers when .NET 12 will be released, or something like that.
**Chris Ventura** 24:22 So, I'm interested in hearing what the .NET Runtime team has to say about it, because there were two main solutions that Noah Falk brought up.
When we were trying to figure out… how to manage all of our dependencies. And so, the first solution was about trying to be the first one to load that dependency, because the first one to load it wins for modern .NET apps.
The second approach was to use, a separate assembly load context, and ensure that everything's using that separate assembly load context. So, if that… approach isn't viable, then I think it's a gap in the design of this feature.
**Rajkumar Rangaraj** 25:14 The only challenge is, like, we cannot load in the separate assembly context. The reason is, diagnostic source has to be in the context running with the application.
**Only then… Alexey Pukhov** 25:24 swan.
**Rajkumar Rangaraj** 25:25 When we… yeah.
**Alexey Pukhov** 25:27 And you cannot load diagnostic source of a higher version if the lower version is in TPA.
You will just figure out.
**Rajkumar Rangaraj** 25:36 We rented.
Yeah, and also, we went to the .NET team. I'm hearing that we need to go to .NET team. We went back to .NET team several times, and at one point in time, they said this is going to cause a breaking change for them, and they are not going to help us further. We have to stay away from doing hacking techniques like this.
That's when I started the outoff process with their help. I asked them and continued that.
So… We said… I asked them to enhance the additional depth so that, at least for the observability vendors, we can do some hooks and upgrade the library to the latest one, when we have the confidence. So they said the product has been since a long time, that's going to be a very bad-breaking change from their, the Tortman side.
So, we did not get help from there, and they said stay away from the additional depths also, because they said at some point in time, additional depths concept may go out of .NET, but don't know when and what it is. So, these are all, like, a one-year whole conversation that we had with them.
**Alexey Pukhov** 26:43 Yeah, interesting insight. Given that additional dependencies only work for the framework-specific apps, they don't work for the self-contained.
**Chris Ventura** 26:52 Yeah.
**Alexey Pukhov** 26:53 The only option we really have is just to force customers to directly reference a… Good version of diagnostic source.
**Rajkumar Rangaraj** 27:04 That's the only production as of today, yes.
**Igor Kiselev** 27:08 So, in… so, let's reiterate. So, we don't have any problem in current, in .NET 10.908 with current state of solutions that LET have done.
Once .NET 11 will be released, We can revert to… it would still solve all problems for a profiler base.
It would not solve a problem for assembly hook-only based, but we could, re-implement a solution.
**Alexey Pukhov** 27:47 We are currently using.
**Igor Kiselev** 27:48 that we have today, and making it not worse than it was… it is today. These are all the problems.
**Rajkumar Rangaraj** 27:55 Tony!
Yeah, the story, what you are explaining.
is what we have been going through in this repo for every .NET release. You are saying if we release .NET 11, it may not work. This is… this was the last year conversation around this time. Hey.NET1 is getting released. It will come up with a new diagnostic source. And we always have been going through this challenge in this repo and updating, and at least we have a path how to solve that part. It's not something new to this repo. Theatrasmus may have a lot of, like.
**Alexey Pukhov** 28:31 You keep solving this over and over again, yeah.
**Rajkumar Rangaraj** 28:34 Yeah.
**Alexey Pukhov** 28:35 You know, at this point, I really, at some point, I said, like, I mean, this is kind of a fundamental tension. I understand that the diagnostic source is coming from OpenTelemetry, it's not the auto-instrumentation dependency, it's coming from OpenTelemetry, but maybe we should top reference in the latest version of the diagnostic source, even in OpenTelemetry, and it's like.
**I mean, I don't… Piotr Kiełkowicz** 29:00 Alexey, it is not possible, to be honest.
I know. System diagnostic source.
is… for .NET equivalent for OpenTelemetry API.
I mean, all trace… Traces and metrics are handled by this packet, and… more or less, new.net brings new features. We expect new… I think, randomness flag related to Context propagation support.
**Igor Kiselev** 29:39 Why?
**Piotr Kiełkowicz** 29:40 directly in diagnostic source.
**Alexey Pukhov** 29:44 Yeah, but then diagnostic source is a .NET runtime, so the reason why OpenTelemetry customers don't have problems, they just reference OpenTelemetry in their projects, and that brings the latest diagnostic source, yet it's still kind of… I mean, isn't it bizarre that diagnostic source is so integral to .NET runtime, and then even OpenTelemetry, to be able to support latest features, have to bring in the latest diagnostic source, basically ignoring the version that is in .NET runtime.
**Rajkumar Rangaraj** 30:18 I can take that caution, actually.
So, in the OpenTelemetry, normally in OpenTelemetry, there is a vision. We wanted to make all the OpenTelemetry API as a part of the the language runtime itself. So.NET is the first language where we could get the OpenTelemetry APIs back, baked into the .NET language itself, but the… when we added everything, it all went into the diagnostic source. That's their story.
If you look at it, even in OpenTelemetry today, I think the technical committee, I know, like, 3 or 4 weeks back, they were discussing how can we take the same approach for Node.js and the other languages, where they can natively have the API as a part of the language itself, not a separate library.
So, that's the vision where OpenTelemetry is diving towards, and .NET is one of the first adapters of that, and because, whom, when we went to the .NET team, they were super supportive and taking the OpenTelemetry spec as it is, and implementing the API layer in their languages. That's why we have everything in the diagnostic source, to give you the background information.
**Alexey Pukhov** 31:29 Oh yeah, sure, but then why don't we use the version that is provided in runtime, since it's really a part.
**Piotr Kiełkowicz** 31:36 the runtime.
Because new features… because new features comes with new reviews.
It is hard to explain customers that if you want new features, you need to upgrade your dependencies, your .NET, to If you are upgrading OpenTelemetry.
**Alexey Pukhov** 31:55 Yeah, I mean, that's exactly what I'm suggesting. Like, if you want to use new features, don't go to .NET 8. Switch to .NET 10. Well, I know.
This is a problematic topic, I know, I know. Well, I mean, that's kind of attention that I'm trying to bring in, that diagnostic source, which is a source of open telemetry, is .NET runtime, and that kind of… creates all the issues. Well, I mean, it's not… it doesn't create issues, it just brings the architecture.
**Igor Kiselev** 32:26 So, oh, I… Rajkumar Rangaraj 32:28 I does recommend you to take a look at the other proposal. I don't know whether you had a time to look at it. At least the diagnostic source, whenever it creates a span, or logs, or a meter, logs it does not do. The span over a meter, it emits the signal that we can capture out of… from the out-of process, and we can observe that. So, I wrote up, like, a proof of concept, and we moved the proof of concept to a NuGet package and have it in the other branch. There are docs or issues also around that in this repo.
I'll definitely ask you to take a look at it. I think that's the recommendation when I went through the .NET, don't inject anything inside the customer process. We cannot survive through that approach for a very long time. That's why they asked me to stay out of it.
**And that, and they gave… and the recommendation has come from them. This is an… Another approach, they are ready to support us, Alexey Pukhov** 33:27 Going forward.
**Rajkumar Rangaraj** 33:28 Yeah, in the going forward, they can provide that kind of support, adding it in the runtime for us.
**Piotr Kiełkowicz** 33:37 One comment… sorry, one comment here to you guys. It will not solve all cases, because this approach supports only natively instrumented libraries, so no bytecode approach.
Yeah.
**Rajkumar Rangaraj** 33:56 We need to have a fusion at this point, and probably, Like, that's… that's an easier thing to cover, I believe, by using some, like, whatever we discussed. It's not only the standalone approach of.
that can solve the problem immediately. But if you're looking at the long way, along with the profiler, also take looking at the other approach, which is not proposed by me, it is proposed we work with the .NET and come up with a proposal. I would also ask you guys to take a look into that, and if that fits, or any modification we… Do that to make a greater win there.
**Igor Kiselev** 34:37 Oof.
**Alexey Pukhov** 34:39 Sure, yeah, I mean, I don't have, actually, a problem with native profiler.
there is a solution on Native Profiler. And also, just to channel whatever Igor said, with the whole change that I'm doing, I'm not introducing more problems, it's just whatever we always had a problem with, we still Have them.
**Igor Kiselev** 35:00 And on top of it, I would say that, we… I have some hopes for .NET issue, because in any case, we are not asking them to change something principle here. We can!
They can change, give them much more RP, but I heard that it's not the case that the .NET team would like to do.
But we only need… to solve the problem, we only need, in one particular place, in Mascara lip library, stop loading diagnostic source through new reflection API, and use old Reflection API that gives us ability to catch it and render a proper.
**Alexey Pukhov** 35:39 That will help.
**Igor Kiselev** 35:40 It would be one small change to revert in one particular case, not using a fancy new API, but use an old API for compatibility without instrumentation.
**Chris Ventura** 35:50 Well, at the same time, they could also just make it so that this new API doesn't bypass the assembly load notification.
**Igor Kiselev** 35:59 So… Chris Ventura 35:59 And allow a change there.
**Igor Kiselev** 36:00 It's a little bit bigger thing, because probably it would require some new design, because on some level, it's logical. So why is that, system, contextual?
**was created, because in a contextual reflection, you are not always capable to track which assembly tries to load, a new assembly. That's why, you know, so it all comes from a score leap, so you lose information which assembly, comes, coming from. And that's why they created that reflect, contextual reflection API to give away for, an assembly that try to use a reflection say, okay, I'm currently the assembler on top of stack, so use my, my, assembly loading context. Right, I just… Chris Ventura** 36:50 I'm just saying that there are, there is precedence for changes like this. For example, tiered compilation.
There are flags that can be passed that disables tiered compilation.
To allow other things, Yep. Other things to work more smoothly. So… so it has been done before, So they do have more than one option.
**Igor Kiselev** 37:16 Yeah, yeah, there are multiple options, that's why I will create an issue. I really hope that something would… will happen, but we need to understand that even if something will happen, it will help .NET 11 customers in .NET 12 timeframe, or .NET 12 customers in .NET 13 timeframe, but most probably for .NET 10 customers, it would be that use assembly hook only scenario.
It would be a problem on, on .NET 11.
**Rajkumar Rangaraj** 37:45 Yeah. The one thing which you need to also consider is Diagnostic Source is not a one single library.
It has its dependencies. Whenever we think about solving anything with that, we need to take a look at the whole.
**Igor Kiselev** 37:58 The reduction.
**We already done… we already implemented a tool that do a static, scan of assembly and, fetch all the dependencies, so we already, looked into full graphs and, Alexey Pukhov** 38:13 Yeah, if we leak diagnostic source, we leak all other… all its dependencies, too.
**Rajkumar Rangaraj** 38:20 Yeah. I also have a question, like, the logging extensions also should have an issue. I'm wondering why that was not a topic. It's not only diagnostic source.
Even a logger is an issue. Logging API is in the.
**Alexey Pukhov** 38:34 Okay.
**Rajkumar Rangaraj** 38:35 metric.
**Alexey Pukhov** 38:37 Yeah, Microsoft… Rajkumar Rangaraj 38:38 Extension Library.
**Alexey Pukhov** 38:39 Microsoft extension, we don't use the latest, latest. We stick to the… Okay. On .NET 8, we stick to 8, 9, 9, 10, 10.
**Rajkumar Rangaraj** 38:50 Got it, got it.
That's a big change we did.
**Piotr Kiełkowicz** 38:54 Indeed.
**Igor Kiselev** 38:54 And the problem right now, not because of, so we used an approach with unification to the latest version in that pool recognized. That's why we not have a problem with any particular assembly. We have a problem when we could not catch and redirect an assembly to a newer version, so… With all the… with all the problems that unification also introduced, because with unification, you can trash customer application if the new version is not compatible with the application. We even done that check, we know that, which, starting from which version, they are not compatible, and, for it, Rasmus already asked if we are able to, make, OpenTelemetry, fully OpenTelemetry Microsoft Extension Dependency Private.
And it looks like… We can, in some cases, if a customer application have no dependency, direct dependency to OpenTelemetry. If they have dependency to OpenTelemetry, it will leak, and we could only use the unification.
**Piotr Kiełkowicz** 40:04 Igor… One topic here, when you report this issue to .NET Runtime, please share on the Slack channel.
**Igor Kiselev** 40:13 True.
Sure, I would, as soon as I would create an issue, I would share in, like, Chinland.
And I would, in any case, back-reference it to original issues and some previous history that I know.
I probably would talk about, first in an issue, I will talk about how it particularly affects us, and what we need for us, but I would also talk there about, more general issues, so what if a profiler or TPE or assemblyHook would like to bring a new dependency in generic.
And that problem could be either solved locally for us for OpenTelemetry, or we could discuss if there is some generalized solution possible.
**Piotr Kiełkowicz** 41:06 So, I think… We can switch to pull requests.
The first one, proof of concept, is related to the topic we have discussed. Yeah. And it is built on top of On the other one.
**Alexey Pukhov** 41:23 Actually, this one, I just created… I just… I didn't put it on top, I just put it on top of main master.
main branch. But basically, just to show what the code can be used to redirect the… Unsafe accessor type attribute, and what application I use to check that it's working.
But it should go on top… oh, yep, sorry, Potter, yeah, it should go on top. I mean, it's only needed on… Told both.
My pull request.
**Piotr Kiełkowicz** 41:58 Right.
Next one, attestation files. In general, should work fine, but it is kind of… Developed, or probably co-piloted.
In some strange way, looking for… Some improvements there.
Mmm… FT carries on PTO, I think, this week, and another.
But you can check it, we have discussed internally, there are two features included, also native stack.
Resolution, so not unknown natives.
Stack, but we have agreed that it should be splitted, so… this native resolution for native code will be extracted to separate PR, but you can check the currents.
PR.
If you're interested.
Sorry, Chris, I did not look into it yet, but if you would like to comment, feel free.
**Chris Ventura** 43:14 Yeah, the main thing I have here is I felt that creating a PR to a doc was just gonna make it easier for us to comment and suggest changes.
So, this didn't have to be a PR, we could have done it as this discussion in the original issue, but I just felt that it was going to be a lot easier in this form.
I do have a question out on the… spec change related to this, where I think there's some… Language in there that… Makes it harder for… or puts some expectations on auto instrumentation.
that doesn't feel quite right, so I'm hoping that they can clarify what they mean by the phrasing on the specification side.
And so, this is also going to be subject to how that discussion goes.
**Piotr Kiełkowicz** 44:15 Oop.
I will try to look into it in the upcoming week.
It is also follow-up.
So, we'll close… This one, Alexier… We are looking for any changes here, or what?
Because I've seen a lot of discussion, Igor.
**Alexey Pukhov** 44:47 I just… Yeah, I have a better proposal… I mean, since we extracted this to a separate pull request, I have a better proposal how we should handle the console buffers.
**Piotr Kiełkowicz** 44:58 Interesting.
**Alexey Pukhov** 44:59 doing anything right now, because I'm trying to finish the main pull request.
**Okay, so… Piotr Kiełkowicz** 45:04 So, it is still waiting for some improvements on your side.
**Alexey Pukhov** 45:09 Still waiting here.
**Piotr Kiełkowicz** 45:12 And this one is still waiting for final changes.
our sites.
**Alexey Pukhov** 45:16 everything we have discussed, I have basically implemented in this full request, so both, like, the dependency chain of diagnostic source and default ILC for the startup hookah isolation. And, well, just wanted to quickly, bring a status. So, I mean, all the changes seem to work really well. The pipeline is… well, I wish I say green, but it's almost green. There are… two jobs on Mac OS for 9 and 8.
that shows a failure, and one failure in particularly makes me uncomfortable, this is the .NET 9. If you look at the test, this is the assembly redirection that claims that The diagnostic source has been loaded twice.
So… This is for isolation, by the way.
So that I have to look. I think I missed something. So I have to investigate that one particular failure, but everything else, with all those changes that we did, looks solid.
**So yeah, I'll keep you all posted. So hopefully it's something minor, but I'll have to… Igor Kiselev** 46:34 I'd like to… I'd like to ask an opinion here. So that is, we still need to understand why the issue happened.
But if we will see some other blocker, that issue, that would require some move work to solve it. The issue happens only on macOS, and if we would prove that only Mac OS is affected by it. And the issue is on Mac OS specifically, affects only, startup hook-only solution.
Canvy, in that case, just declare that startup cook-only solution on macOS, is not supported for now, and it would be a follow-up, solution, and… not increase work right now, because I believe we… previously, we have not, done the same, level of compatibility for Mac OS. For example, we, switched from x64… x64-bit ARMOS to ARM64, so we introduced some breaking change in macOS build.
Previously. So maybe it would be also the case that, the feature that most probably would not be used a lot.
Would be broken for some time.
**Piotr Kiełkowicz** 47:58 That's a question.
**Alexey Pukhov** 48:00 the Mac off.
**Igor Kiselev** 48:01 So, yeah, the question is, if we validate that an issue is only for macOS, And, no other would be affected by it, and we will get information about it. And the fix for macOS is difficult. Can we do a fix for macOS?
For startup hook only solution, after the pull request will be merged.
as a follow-up, and not put even more work in the same pull request, which is already very, very big and very hard to… validate.
Let's the review.
**Piotr Kiełkowicz** 48:40 I think we need to… when we understand, we can make that final decision. I would not commit to any directions right now.
**Alexey Pukhov** 48:51 Fair.
**Piotr Kiełkowicz** 48:58 But yes, in general, support for macOS is typically for development purposes.
And I doubt that anybody is using it on the production side.
**Alexey Pukhov** 49:12 Well, by the way, thank you for those who created this pipeline.
Ye.
It shows… Really interesting issues.
**Piotr Kiełkowicz** 49:36 No… There is one… Question… Chris Ventura 49:55 I was wondering if this is something that needs to be forwarded to the, SDK SIG. It wasn't clear if this was… And.
**Piotr Kiełkowicz** 50:08 And… I agree that it is completely unrelated to all the instrumentation part, but in general, yes, it is working because we are deploying everything to GAG.
**Igor Kiselev** 50:24 And right now, even without Docket.
probably would also work, because I tried to fix all situations, and at least an hour end-to-end test, it proves that it works even without GOC.
**Piotr Kiełkowicz** 50:41 I will make a note just after the… the meeting.
**Chris Ventura** 50:49 Yeah, I just don't know how we can recommend them to manage those assemblies on the SDK side.
as far as getting it registered in the GAC and updated, Accordingly.
**Piotr Kiełkowicz** 51:16 I do not think that win.
We need to update anything.
Almighty.
I can update it, but also outside the… Hmm… outside the meeting, I'm working on other nets, biotech instrumentation.
At least for part of the… Part of the… Library, so we can expect something upcoming week, probably.
Matthew, sorry, I've missed your topic.
Are you still with us? Yes, you are.
**Matthew Hensley / Grafana Labs** 52:24 Yeah, it's no problem. So, open PR… Recently, we had a user notice about setting resource attributes.
Them getting copied to environment variables, so if you have multiple services in one app pool.
Yep. Just some unintuitive behavior. So, I was looking at fixing it, but I know there's been a lot of, work going on around declarative config also, so I just wanted to… Make sure there wasn't gonna be any conflicts, or something around configuration is already Going to be reworked?
Before I, did that.
**Piotr Kiełkowicz** 53:04 So, for now, configuration is as is.
And it is fully written on .NET Auto instrumentation, but I… I've seen notes on the SDK.
Yesterday, that you are discussing, moving into OpenTelemetry SDK level.
So… Yes, you can expect some changes to what needs to happen.
But for now, I doubt that anybody is working on any improvements.
In its part.
**Matthew Hensley / Grafana Labs** 53:39 Okay. Well then, I will have a PR shortly.
**It's hopefully safe. Definitely running into some flaky tests that I'm gonna have to fix first, so… Piotr Kiełkowicz** 53:51 Slacky test, do you mean in our pipeline, or new tests you have created?
**Matthew Hensley / Grafana Labs** 53:57 Existing ones, when running locally, there's environment variable leakage, It seems.
**Piotr Kiełkowicz** 54:06 Oh, strange, because I told you that we already handle it on these cases, but yeah.
We're looking for any improvements.
You can share.
**Matthew Hensley / Grafana Labs** 54:16 Awesome.
Thanks.
**Piotr Kiełkowicz** 54:33 Any other topics?
So, thank you! See you next week.
**Alexey Pukhov** 54:46 Thanks to everyone!
**Yevhenii Solomchenko** 54:47 Thank you.
