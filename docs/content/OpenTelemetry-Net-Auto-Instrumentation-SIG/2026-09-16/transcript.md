SIG: OpenTelemetry .Net Auto Instrumentation SIG
Date: 2026-09-16
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Piotr Kiełkowicz (Splunk Inc.)** 05:19 Hi, guys.
Joyce, is it normal day in US, or kind of holidays, or partial holidays, or whatever?
**Alexey Pukhov** 06:36 No, it just… It's just today.
**eftiquar** 06:42 No partial holiday, it's full working day.
**Piotr Kiełkowicz (Splunk Inc.)** 07:00 Hey, Chris.
Josh, great to see you.
**Rajkumar Rangaraj** 07:06 Virtual.
**Piotr Kiełkowicz (Splunk Inc.)** 07:16 So, it's 556 my time, so I think we can start.
Do you have any important topics for the beginning?
So, let's start with our usual… Agenta?
And we have a couple interesting PRs.
And this one.
So, I've prepared the PR related to native runtime, I think.
But I think we should wait with merging with this, with native sync from the Datadog.
Because there is kind of overlap with modified functions, so… it is more important, in my opinion, to bring the other stuff, but we need Zach approval for this, I'm not sure if he… when he will be fine.
I have to redo this.
And… 12th house… the pre-new update cementing Convention for Kafka.
Technically… Semantic conventions suggest that we should not update.
Because it is still not stable, but it should.
And if we want to allow new attributes, which is defined in 144, and this guy probably needs it, we need to break the cementing… existing semantic conventions and update to 144.
**Chris Ventura (New Relic, Inc.)** 09:25 But if the guidance isn't to update yet, because I thought with the semantic conventions, while it's still being stabilized, the suggestion was for library authors to stay at the older… Stable-ish version of the conventions.
And not make the changes.
Until, instrumentation has stabilized. Or the conventions have stabilized.
**Piotr Kiełkowicz (Splunk Inc.)** 09:58 That's true, there is also option to… Have a kind of environmental variable switch.
To allow use old semantic conventions, new semantic conventions, or both of them together?
It is the… the other options.
**Chris Ventura (New Relic, Inc.)** 10:17 Right, which we haven't done that for any instrumentation yet.
And I don't know if… We even support that for some of the other instrumentation that we pull in.
**Piotr Kiełkowicz (Splunk Inc.)** 10:31 Yes, we support this.
**Chris Ventura (New Relic, Inc.)** 10:33 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 10:34 Or we historically supported this for the… all SQL clients.
Okay. And other stuff like that. There were kind of possibility to switch by environmental variables, but we never documented it.
**Chris Ventura (New Relic, Inc.)** 10:48 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 10:52 But I think the current semantic conventions, together with the schema are finally available. We should be able to Make these breaking changes without any big issues on the customer side.
So… I think we can accept this PR if it's mess or stuff, because I didn't check it yet.
So, it is not hard block from my side.
**Chris Ventura (New Relic, Inc.)** 11:29 So the idea here is that somebody would have to opt in to the newer conventions.
**Piotr Kiełkowicz (Splunk Inc.)** 11:35 No, this… in this PR, we are just switching from the old to the new one.
**Chris Ventura (New Relic, Inc.)** 11:40 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 11:41 But we are posting the schema URL Together with every span, so if the customer needs to roll back, there should be… it should be possible to do this with, kind of, semi-automatic tool, or something like this.
**Chris Ventura (New Relic, Inc.)** 12:00 But you'd need to have a collector in your environment to do it, right?
**Piotr Kiełkowicz (Splunk Inc.)** 12:05 That's true.
But it is kind of a pretty common scenario.
**Chris Ventura (New Relic, Inc.)** 12:14 Yeah, I feel like recently I've run into enough people that aren't running a collector to be able to do that.
Ugh.
I kind of feel like.
**Piotr Kiełkowicz (Splunk Inc.)** 12:31 to this.
**Chris Ventura (New Relic, Inc.)** 12:32 I kind of feel like we should… Follow the pattern that was done before, where there's a switch.
**Piotr Kiełkowicz (Splunk Inc.)** 12:42 The question is when it will be stabilized.
Or if it will be stabilized at all.
**Chris Ventura (New Relic, Inc.)** 12:48 Yeah.
Do you know if there's an active working group for the… Message queuing conventions.
I feel like there isn't for Kafka.
**Piotr Kiełkowicz (Splunk Inc.)** 13:12 I'm pretty sure that this working group is dead.
To be honest.
**Chris Ventura (New Relic, Inc.)** 13:17 That's what I thought.
**Piotr Kiełkowicz (Splunk Inc.)** 13:22 Because when I last seen, kind of, message queue issue, it was automatically closed.
**Chris Ventura (New Relic, Inc.)** 13:28 Right, and I think it was also related to Kafka.
Changes.
**Piotr Kiełkowicz (Splunk Inc.)** 13:38 There you go.
I'm searching.
Nope, it is not. There is kind of someone who is working on this.
I think that's related. Otherwise, it should be auto-closed.
**Chris Ventura (New Relic, Inc.)** 13:58 I think it WAS auto-closed… initially.
Or at least there was one that was auto-closed.
Because this is related to another issue that was… or PR that was opened in our repo, and then the semantic convention.
issue that was open for it was auto-closed, and then a new one got opened.
**Piotr Kiełkowicz (Splunk Inc.)** 14:30 Yeah, you're right, yeah.
It was auto-grossed.
They're accepting issues, not accepting PRs related to this stuff.
**Chris Ventura (New Relic, Inc.)** 14:44 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 14:52 So… I don't see, kind of, any good… good ways what we can decide.
Probably the best options would be to ask to implement this environmental variop switch.
**Chris Ventura (New Relic, Inc.)** 15:07 That's what I think.
**Piotr Kiełkowicz (Splunk Inc.)** 15:09 But the question is how we should handle it in the context of file-based configuration.
**Chris Ventura (New Relic, Inc.)** 15:24 Because this would be the first time we have to access the configuration from Instrumentation, is that it?
**Piotr Kiełkowicz (Splunk Inc.)** 15:32 Yeah, it is fully bytecode Instrumentation, yes, so… It is not the first time, yeah. We can just add the switch, and the question is if we should add the switch, which allows to… You read this environmental wor-up, or ignore in such cases, file-based configuration and read-only Nverse.
**Rajkumar Rangaraj** 16:00 this is another approach we follow, Piotr, these kind of issues. If you go to the conversation and the table, we have an operation and an operation name, right? The older one uses messaging.operation, and the new one uses messaging operation name. So, we just… in the… we just rely on that name to predict whether it's an old one or a new one. And based on that, we… don't throw away the old implementation, keep it for the backward compact, because I don't know how in the SEMCON they decided, like, to break it in the minor version release, but, that's the kind of thing that worked for us, too, but, Thing is that we have to pay the cost for both.
**Piotr Kiełkowicz (Splunk Inc.)** 16:48 It is not a stable semantic convention yet, so they decided to break it.
**Rajkumar Rangaraj** 16:54 Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 16:55 It is… It is why we are discussing keeping the old one, and… versus bringing the new one, or keeping this, Messaging duplicate text.
Switch. Auto stability opt-in.
And, well…
**Rajkumar Rangaraj** 17:15 It's all fine. You need to think from a customer perspective who are using this product, how it's going to impact them. If you want to give a minimal impact, the idea is check that operation and branch it out. If we are fine giving slightly a… little more work to customers, saying, hey, if you… all of a sudden, if you lose the Kafka traces, this is what has happened with your update, and go ahead and redo it.
Yeah, but I don't know. The best approach, if we don't… we should not be breaking customer, because our product is stable, but… Even though semantics is not.
**Chris Ventura (New Relic, Inc.)** 17:54 Yeah, I think we should keep our instrumentation generating the older conventions by default.
And then someone has to opt in to the newer conventions.
So then, I think Piotr's question was, do we only support it from environment variables, or do we need to support it from both environment variables and, declarative configuration?
And I… I, I don't know where this,
**Rajkumar Rangaraj** 18:28 I'm throwing a third idea there. What I'm saying is that let's not even worry about that and support both of them under the hood. We know, based on the… whether it's an… if we have an operation or operation.name, whether it's a new or old semantic.
**Chris Ventura (New Relic, Inc.)** 18:46 Well, this is, bytecode Instrumentation, so we're not subscribing to,
**Rajkumar Rangaraj** 18:53 That makes it…
**Chris Ventura (New Relic, Inc.)** 18:54 Other instrumentation.
**Piotr Kiełkowicz (Splunk Inc.)** 18:56 Yeah, so we are generate… we are responsible fully to generate these semantic conversions.
**Rajkumar Rangaraj** 19:01 Yeah, it's possible.
**Piotr Kiełkowicz (Splunk Inc.)** 19:18 I intend to add kind of temporary switch also on the Kafka level for the… Profiling-based, configuration.
File-based configuration, and… It would be kind of easier for everybody to handle it.
So, what else?
RapidMQ.
cluster named span attributes. I didn't have time to look into it, to be honest.
**Chris Ventura (New Relic, Inc.)** 20:49 Yeah, neither have I. I'm assuming it's gonna be similar to the Kafka… Cluster ID… Resolution.
**Piotr Kiełkowicz (Splunk Inc.)** 20:59 But the Kafka cluster ID was finally accepted, as I remember.
**Chris Ventura (New Relic, Inc.)** 21:03 Yes.
And I don't know where… what the state… Of, this one is.
As far as being accepted.
Because the other thing is… With RapidMQ… Do we still have some bytecode instrumentation for older versions?
Or did we drop support for the older versions and just keep the newer?
**Piotr Kiełkowicz (Splunk Inc.)** 21:54 I think we are supporting.
**Chris Ventura (New Relic, Inc.)** 22:09 Because RapidMQ is natively instrumented.
But only for the newer versions.
**Piotr Kiełkowicz (Splunk Inc.)** 22:20 11.
It needs bytecode Instrumentation for 5 and 6, and everything 7 plus is source instrumentation.
So, if we are touching colony 5 or 6, I would not accept this PR at all, to be honest, and keep it as a… Kind of… legacy existing behavior, and do not include this.
**Chris Ventura (New Relic, Inc.)** 22:43 Right.
So that's… that's where I was going with it. So if… Version 7 Plus are producing those identifiers.
Then we can consider… Backporting, similar functionality, but if it isn't… Then… we should probably leave it, leave it alone.
**Piotr Kiełkowicz (Splunk Inc.)** 23:07 Okay, I will handle it kind of offline, this… this message.
Today or tomorrow?
Don't bounce.
Sorry, I've opened them in the wrong window, and… Azure Container Apps.
I think it is kind of New Relic contributor, Chris.
**Chris Ventura (New Relic, Inc.)** 23:46 Yes, and so I've had a conversation, with this engineer.
I haven't looked closely at the PR, but I tried to talk about the concerns related to, okay, this is making an HTTP call in order to get some metadata.
And if we're not running in that environment, how long will it take for that call to time out? Will it delay?
Getting the resource initialized for the application, the… Does this need to be off by default?
But I do have a question for Raj.
Cause I remember when we added one of the Azure resource detectors.
we had talked about the stability of the various Azure resource detectors, and I wasn't sure what the status of this one in particular is, if it If you think it's ready to be added to auto Instrumentation, with some safeguards, or if it's not quite stable enough.
**Rajkumar Rangaraj** 25:01 It is stable enough, to be honest, like, it is even baked into a part of the Azure Monitor Exporter that we use, the same implementation. The thing is that we did not use as a package, we copied… we rendered in this code.
Just to handle the similar thing what we were speaking about, Kafka. Something changes to provide a support for both, but it's a high time, I think. It's last two years we have been using this one.
With no challenge at all. So… I think recently there was a change which has been done to this, even based on the current the app service attributes that have been specified in the semantic conventions. So it's pretty much stable, this one.
The early thing, what we have been waiting on this one, is the… especially… we want a blessing from someone saying the app services to be a part of the owner in that for that project, saying that App Service owner, VM owner, and everything. In that way, if something changes, they'll have a responsibility to come and fix that.
Yeah, it's more than an observability, it needs a domain knowledge. That's why, from the Microsoft standpoint, we did not take it to this table. That's the thing it's spending on.
Yep.
**Chris Ventura (New Relic, Inc.)** 26:25 Do you think that should block us from making it available by default?
Dinner…
**Rajkumar Rangaraj** 26:32 Can articulate.
**Chris Ventura (New Relic, Inc.)** 26:33 Please?
**Rajkumar Rangaraj** 26:34 It should not.
**Chris Ventura (New Relic, Inc.)** 26:35 Okay.
Sure. And then…
**Piotr Kiełkowicz (Splunk Inc.)** 26:39 It's waiting for a regular review process.
**Chris Ventura (New Relic, Inc.)** 26:42 Okay.
And do we think this is something that we should have off by default?
And require somebody to opt into.
**Rajkumar Rangaraj** 26:52 I would say it can be on by default. It's, like, it's not going to give you a very big, very bad breaking change. The product is not going to change. Whatever the attribute, it is, like, spitting is not… we have the control in the contribo.
So… Okay.
**Chris Ventura (New Relic, Inc.)** 27:10 I just wasn't sure if there's a concern with making that HTTP request to that special Endpoint.
In order to get the information.
**Rajkumar Rangaraj** 27:23 if you're running in the… within the Azure, like, that's the metadata call, which is… Right. Yeah. So, if the workload is in Azure VM, or in the app service does not use that HTTP call, only in VMs it does.
So there is no harm in doing that. That's the recommended way by… I think every RP has a way, the HTTP call to read their metadata, and this is the Microsoft way of doing it.
**Chris Ventura (New Relic, Inc.)** 27:49 Right, but if you're… so… But we have to support more than applications running in the Azure environment.
So, if somebody's running in AWS, will it still attempt to make that HTTP call automatically, and what is the time… and will that cause a delay while we wait for that call to time out?
**Rajkumar Rangaraj** 28:12 It does, I believe, but the thing is that the timeout is… very minimal, I think, like, in this. Maybe we should safeguard that HTTP call with another environment variable, I believe, at this point in time, if that's… we are worried about that. There is a PR also in the contrary repo now, sitting to solve something like that, so I did not take a closer look at that. Probably that should be solved sooner.
There is a complaint customer saying that, hey, I'm running an app service, but I'm seeing a HTTP call failure, and that's logging an exception in my traces. I don't know why it's doing that. So, it does, and there is a… right now, there is a PR in the contract repo to solve that. So, probably solving that should solve your… the questions that you asked as well, Chris.
**Chris Ventura (New Relic, Inc.)** 29:07 Perhaps.
**Piotr Kiełkowicz (Splunk Inc.)** 29:10 And I think more and more.
Users will switch to the file-based configuration, and in this case, it is kind of no issue at all, because they need to explicitly enable… It's research detector.
**Chris Ventura (New Relic, Inc.)** 29:29 Yeah, because if they have to explicitly enable that resource detector, then… I don't think it'll be a big deal, and we can include it.
But if it's something that's automatically going to be on for them and running.
Then, we may need a switch to… Require them to… to opt-in or to turn off that.
That behavior.
**Piotr Kiełkowicz (Splunk Inc.)** 29:59 I think that we provide, kind of, opt… opt-out.
So we can call it specifically. If you are not in the changelog, if you are not using… in the Azure end, please consider setting up this tool to disable, and it should… Kind of cover also this scenario.
Yes.
Here's the pattern.
So, gringo to review and… Potentially managed, okay.
Update native code Instrumentation, it will be kind of… will be only three and a half years.
behind?
the upstream?
But as mentioned at the beginning, we need to approve all from Zach.
**Chris Ventura (New Relic, Inc.)** 31:09 Do you… do we have a target of what tag we're hoping to… Get caught up to.
**Piotr Kiełkowicz (Splunk Inc.)** 31:19 The last one?
**Chris Ventura (New Relic, Inc.)** 31:21 Okay.
I was just curious if there was a bug fix in particular we were trying to make our way towards.
**Piotr Kiełkowicz (Splunk Inc.)** 31:31 I think, historically, we have kind of have some bug fixes which hit at least Splunk customers in some version, and we were working, kind of, couple of days, then we have just made native bug, and customers were happy that we have fixed it, and we did nothing except the this native code update, so… based on this, I would follow.
With AI, it is kind of… Much easier than… than before.
**Chris Ventura (New Relic, Inc.)** 32:05 Yeah, that's fine. I was just curious, because there were a few PRs where, I think, eftikar, you had referenced, oh, we should fix this, and I think Zach had said that, yeah, this was already fixed in the Datadog repo, so we just need to sync it up.
**eftiquar** 32:26 Sure.
Yeah, especially for the longer, paths it was failing, so… It'll be good to see. I can review it once it's fixed.
I'm glad that it's fixed in data logs upstream.
I think any string greater than 512 bytes will be rejected.
That's the bug.
**Piotr Kiełkowicz (Splunk Inc.)** 33:16 I mean, when it will be meshed, we will be kind of here, in the tags, and… The list is pretty wrong.
So, 51 version, and here, kind of, 30, so 80 versions to be.
To be synced.
**Chris Ventura (New Relic, Inc.)** 33:34 We've got a ways to go.
**Piotr Kiełkowicz (Splunk Inc.)** 33:36 Yup.
IBM, we have discussed it kind of a week ago, We have some customers using this in Splunk, or Cisco, whatever.
So, I think we can accept this kind of… Instrumentation, but we need to carefully review it.
I suppose it was… fully AI generated.
**Chris Ventura (New Relic, Inc.)** 34:12 Probably.
**Piotr Kiełkowicz (Splunk Inc.)** 34:13 Probably, but… so, yeah, so manual analysis is needed here.
PR is… Big, let's say.
And… more… let's switch to Kafka first. It is kind of follow-up to 144PR.
Related to Kafka, I ask to first update the semantic conventions, and then… Potentially emerged this one.
And… fticker, and… Yeah, FTR first.
**eftiquar** 35:09 Yes.
So… I have a hardened it, I have… basically tried to eliminate every review feedback from Codex, from Eugenie.
And I'm hoping if someone among you are willing to dive into it, if you have any questions. But this is really important, because this is a bridge to getting the OPAMP dynamic configuration working.
Sorry for a really big PR, but there was no other way to get this through.
**Piotr Kiełkowicz (Splunk Inc.)** 35:58 I'll try to review before next season.
But it is… Challenging, to be honest.
**eftiquar** 36:05 The challenge is, there are too many paths, like, you can dynamically disable the service, and then you can shut down, and while shutting down, you can enable the service, because OPAM can send the config signal anytime, so you have all those concurrency issues. While the service is shutting down, you are enabling it, or you are shutting down the process itself.
And so the CLR callbacks might be in flight, there might be partial captures that are there, so what do we do with the expo? Do we discard them? Do we keep them? Et cetera, et cetera.
It's really less about OPAMP and more about dynamic start and stop and enable, disable of profiling. The original implementation was simple, it was just… a Boolean flag. If profiling is enabled, you start service. If profiling is disabled, you don't start service, unfortunately.
the complexities due to the interaction between a lot of threads that are being profiled, and then you suddenly say, okay, now disable it. Or, okay, change the sampling frequency, or just disable memory location.
And let the thread sampling work, or vice versa.
One big advantage of this change is it put our pre-existing profiling code through really rigorous analysis, because I fixed some of the issues that predated this configuration change. There was a hidden deadlock in our shutdown path.
that was nailed through this, so… The hard work will pay in the long term. But if anyone wants to really take it on, I can have a WebEx or Zoom session, and I can walk them through it.
If that can help. But I really need some pair of eyes to go through it.
**Piotr Kiełkowicz (Splunk Inc.)** 38:07 Boom.
And, Alexey… The second one.
**Alexey Pukhov** 38:18 Yep.
**Piotr Kiełkowicz (Splunk Inc.)** 38:19 Big PR.
**Alexey Pukhov** 38:22 Wow, yeah, so… I mean, it's rather big.
Oh, no, I mean, it contains everything. The fix is not… that vast? But yeah, the code is there. I mean, the code is quite substantial. the quick update, I still need to address the comments left by Igor NFT car.
Dee found a couple of things that I missed.
And… Well, basically, I'll just continue working on this pull request. I'll address the comments and push a new change.
**Igor Kiselev** 39:04 I'd suggest to move it back to draft right now.
**Alexey Pukhov** 39:07 Oh, okay, sure, yeah.
**Igor Kiselev** 39:08 It, it will have a, Pretty serious changes, and the review now probably would not be wise by anybody else.
**Alexey Pukhov** 39:19 Okay, I'll do it right now.
Anyway, so, oh, just for the context, so we need this change to go in before .NET 11, because we're gonna have problems with our assembly redirections.
On lower… on frameworks before .NET 11.
If we don't redirect the assembly references in this attribute.
So this… I mean, we discovered it a long time ago when we first implemented assembly redirection.
Well, not first, but when we refactored the assembly redirection, we discovered that's gonna be a problem in .NET 11, and… Finally, I get some time to work on this.
**Igor Kiselev** 40:11 The good thing, despite there is a lot of code, it is very, very contained, and the changes.
Basically, additional processing on our model loaded and nothing else, so it should be pretty easy review, and we still have plenty of time to resolve it.
**Alexey Pukhov** 40:28 Yeah. See, it's very contained here. There is a lot of code, but it's mostly to find the right attribute.
to parse the… type definition in the attribute to find all the assemblies, and check that the assemblies are of the right version, and if needed, just rewrite the… Type definition on those attributes.
So, some would remind in the assembly ref, redirection, but slightly differently.
I don't see… how do I turn it back to draft?
I'll… I'll do that, anyway.
**eftiquar** 41:10 In fact, Alex.
**Piotr Kiełkowicz (Splunk Inc.)** 41:11 Already done.
**eftiquar** 41:12 review on that metadata machinery, that'll simplify it even further, because your core business logic is just rewriting that narrow portion of assembly version. The bulk of your code is centered around enumerating custom attributes and looking for that unsafe accessor, and that's all just the metadata API handling.
So if we take that apart, your core business logic is really simple.
**Alexey Pukhov** 41:40 It is, it is.
**eftiquar** 41:41 So, that's why…
**Alexey Pukhov** 41:42 There's a lot of…
**eftiquar** 41:43 Feedback is very important.
Because that basically declutters the whole things.
The metadata API is just a lot of noise, but if you take that out.
The review is real easy.
**Alexey Pukhov** 41:57 Yeah, yep, yep. Yeah, the biggest problem is that in C++, you have to do a little bit more work on finding.
**eftiquar** 42:05 Yeah, indeed.
Enumeration, right? That enumeration model and buffering of 32 attributes, just random number, I don't know why 32, but all that advancing through the custom attributes and parsing, that Clouds the core business logic.
**Alexey Pukhov** 42:23 Yep. Yep.
Sure, I'll… I'll take a look at the comments and.
**eftiquar** 42:28 Thank you.
**Alexey Pukhov** 42:30 Sure, thank you.
**Chris Ventura (New Relic, Inc.)** 42:32 And then, based on the PR description, it sounds like there will still need to be some follow-up work to address some of the other gaps before .NET 11. Is that true?
**Alexey Pukhov** 42:45 Yes, there will be, at least from my side, there will be another change. So this, this is gonna fix assembly redirection on .NET 11 for native Profiler, but I also need to implement the fix for the startup hook only.
which would be bringing back the additional dependencies workaround. We're just gonna do it differently this time. But it's gonna be exactly the same workaround, we'll just… We don't have to… Create a project that used to generate, additional dependency structures, because we already have all the assemblies, so it's going to be something… sort of a script that will just reorganize the existing files in a file system to support additional dependencies workaround.
**Chris Ventura (New Relic, Inc.)** 43:40 And then I think there was, unless I'm mixing up the PRs, something about dealing with generics?
Maybe I'm… mistaken PRs.
There was some sort of gap with being able to look up.
the correct…
**Piotr Kiełkowicz (Splunk Inc.)** 44:02 was related to… Here, I think.
**Chris Ventura (New Relic, Inc.)** 44:06 Oh, runtime async, okay, yeah.
**Piotr Kiełkowicz (Splunk Inc.)** 44:08 I'm pretty sure that we are talking about…
**Chris Ventura (New Relic, Inc.)** 44:11 Okay, yeah. I've been trying to look at all of the big PRs, and so I'm probably mixing it up.
**Igor Kiselev** 44:17 Maybe it's not a mix-up, because I have put a command that Alexey has changed right now, skip retargeting over generics, but it's only about how he parse a virtual string. It would be… Very, very well contained, but probably you're talking about something else.
**Chris Ventura (New Relic, Inc.)** 44:35 Yeah.
**Alexey Pukhov** 44:39 Generics are so generic.
**Piotr Kiełkowicz (Splunk Inc.)** 44:46 So, let's go to the issues.
We have 4 of them.
I will close this.
IBM MessageQ, I will tentatively put it on 17, as we have PR already.
I will hand this message… this issue together with PR.
Some new issue related to… serial profiler… And kind of wrong configuration.
**Chris Ventura (New Relic, Inc.)** 46:58 Yeah, this is where you've got a CLR profiler configuration for a different CLR profiler.
But you have the, startup hook configured for auto Instrumentation.
So it triggers a case where… auto Instrumentation believes the CLR profile is available Even though it's a different profiler.
**Piotr Kiełkowicz (Splunk Inc.)** 47:29 I think he should handle it.
**Igor Kiselev** 47:32 Oh, I…
**Piotr Kiełkowicz (Splunk Inc.)** 47:33 I will ask if the reporter would like to provide some fixes.
**Igor Kiselev** 47:38 I think it should be looked by Alexey, because it looks like it is, auto-detection of startup cook mode for assembler direction.
**Piotr Kiełkowicz (Splunk Inc.)** 47:52 Alexey, are you okay to… Take a look on this.
**Igor Kiselev** 47:56 Totally.
**Alexey Pukhov** 47:56 Yeah, of course.
**Igor Kiselev** 47:57 at least, at least to make sure, probably Alexey will fix it, or at least we'll make sure that it is not… Assembler direction, but by method name is StartupHook Only mode, it looks… Like, it will be…
**Alexey Pukhov** 48:13 Yeah, I think what we do in the startup hook, we just basically check if the profiler is enabled or not, but we don't check which profiler is enabled.
From what I remember.
I mean, maybe we should improve it and make sure we only react to our profiler.
**Chris Ventura (New Relic, Inc.)** 48:34 Yeah, that might be the simplest thing.
But with that being said, who knows what's gonna happen if you're using, another profiler?
Auto Instrumentation.
**Igor Kiselev** 48:45 This should work the same way as we would work in startup cook-only mode, let's say that. If… It doesn't mean that it would always work, but at least it should not be much worse of it, or otherwise it would be a fault of other profilers, yeah.
**Chris Ventura (New Relic, Inc.)** 49:03 Yeah.
**Igor Kiselev** 49:13 I have… Okay, we… if we finished it, I have one more comment, on a bug that have not been reported.
Probably yet. Eftikar, So, we have represented, how we do calls gathering may result in deadlock situation in Azure environment, specifically because they also do some hooks, and they hooked our approach of doing stack snapshot, at least for our internal profiler, we know that it is confirmed. I suspect that we have the same issue with our part solution in Hotel.
If the car, do we have it or not? And if we have it, should we create a bug, or should we create a pull request in future?
**eftiquar** 50:06 Yeah, we should. I'll take a look at it.
The issue we should… I haven't explored, but it is likely that it will need same fix as Abdi.
**Igor Kiselev** 50:18 And… I don't say that we are at fault here, I would, so per our internal investigation, it's a hook machinery on Azure, responsible for it more than we are.
But, we have… we can do some workarounds to make it play safely with unknown issues of Azure environment.
Okay.
**Piotr Kiełkowicz (Splunk Inc.)** 51:14 and other topics.
**eftiquar** 51:22 Oh, good.
**Piotr Kiełkowicz (Splunk Inc.)** 51:23 Thank you! See you next week!
**eftiquar** 51:26 Take care.
**Alexey Pukhov** 51:29 Bye.
