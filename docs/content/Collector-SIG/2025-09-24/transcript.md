SIG: Collector SIG
Date: 2025-09-24
Duration: 40 minutes
============================================================

## Zoom Recording Transcript

**Alf Kenny** 01:53 Hello.
**GZ Gregor Zeitlinger** 02:20 Hello!
**Dmitrii Anoshin** 05:38 Hi, everyone.
**Evan Bradley** 05:41 Hello.
Jad and Young, do you know if Pablo will be here?
**Jade Guiton** 05:48 I think he intended to come, at least.
**Evan Bradley** 05:53 Okay, we can wait a minute.
How about this? I'll move his agenda item down for now, and Joao, you can go first.
**Dmitrii Anoshin** 06:48 Sounds good.
**João Duarte** 06:50 Thank you.
Okay, yeah, so, this is a follow-up to a conversation, that happened two months ago, July 23rd, about having enrichment capabilities in the collector. At the time, I presented, like, a doc that Try to justify the collector having these capabilities, and the follow-up to that discussion was having a a proposal.
And the proposal exists, so it's, it's there, linked.
And I've had some feedback, and thanks, especially to Sam for the feedback on the proposal.
The, the idea is to, to have a… a processor that can do enrichment. The enrichment sources can be multiple, and that can be ideally defined as extensions, so anyone can build their own as they want, and includes whichever sources they need in their distributions.
The… so the proposal has been updated for that… that requirement. It… Down, there's a comment that tries to provide a skeleton, some interfaces and structures.
That could be used as a base to implement this.
And yeah, so what I'm asking is just, yeah, if anyone is interested in looking at this and providing feedback, I'm still learning the insights and working with the collector code, so bear with anything that doesn't make sense, but any feedback is appreciated, and as well as any interest in sponsoring.
Did this proposal, so… Yeah, open to answer any questions or any discussions.
Or just move to the next topic.
**Evan Bradley** 09:09 I'm gonna move.
Pablo to the… And, if he wants to… if he… if he comes, then he can present it. Otherwise, I can… I can cover the announcement as well.
But, Israel, I think you're next.
**Israel Blancas** 09:24 Wait, hi? So… Well, so, during the last call that would have been the… during the North America time.
I came to this call because we want to introduce some… It's a new feature, right, to the redaction processor, and where there were some concerns related to the size of the resulting binary, and also things like performance and other stuff, right?
Well, I tried to address the whole thing on the… in the PR, right? So if you access the link, you will see that I provide how much the size was, when enabling or not, the feature, and things like that, right?
So, yeah, after that, I didn't receive any feedback, so please, if you can take a look, it would be pretty appreciated, because it's something that we need. I… we have been also, doing some… improvements.
to the code, because it would have been running it different things, right, with different, different systems, and so, right? We found some stuff to improve.
So… yeah.
That's all.
you have any questions or something, I will be happy to answer, or later in Slack or whatever.
**Dmitrii Anoshin** 10:45 Is there also… yeah, I'll… so sorry for, delaying… delay from my side on this one. I'll take a look, today, tomorrow I was on PTO.
And, you mentioned improvements?
Are they… those improvements not related to this capability, but in general to the reduction processor? Is that correct?
**Israel Blancas** 11:04 To this feature, right? Because, when we were running, I mean, if you check the PR, right, you will see that there are multiple, pushes, right? Some of them were related to rebases, and others were to the… to the stability of the feature itself, right? Like, trying to… also, we have been, like, trying to ensure that under, different load and things like that, right? The thing behaves properly. So if you don't enable it, right, you will not have any of those improvements, right? Because, I mean, you will not notice the thing is there.
But these young.
things like that. We, also we have been… Jorge has been working on the… Jorge is the guy from Grafana who is maintaining the library that, is doing the magic, let's say, right, under the hood. He has been also doing some improvements, because he found some things that could be… Much better there, but yeah.
**Dmitrii Anoshin** 12:01 Alright, thank you.
**Israel Blancas** 12:13 Yeah, so I think we're gonna go with the next.
Topic.
**GZ Gregor Zeitlinger** 12:20 I guess that's, me.
Should I just… Share my screen… Working?
Yeah, I have noticed, that, we had a bug in the hotel collector, Because, if I understand correctly, we did not have sufficient tests.
And I wanted to find out That's really the case.
And I'm talking here about this, protobuf wrong wire type, has been filed by a team member in my team.
And if I'm understanding this correctly, it was a weird setup where, there was no test, and… It was even difficult.
To come up with a test case.
So why am I telling that? I'm telling that because… I'm the maintainer of a tool where there is a test.
So, If we would use that tool, or a similar tool, we would be able to prevent, This type of failure in the future.
But I'm not sure, that I'm, getting the picture correctly, because I'm not working on Hotel Collector from day to day. I've just made a couple of PRs.
Yeah, that's it so far. Am I on the right track so far?
**Jade Guiton** 14:18 So, for the first issue, it was particular to a very specific kind of behavior… client behavior. So, I guess the question is, Does your… like, does… do you propose tests include that kind of client? In this case, I guess, I think the .NET client was affected?
**GZ Gregor Zeitlinger** 14:40 Right, yeah, yeah. You're getting that exactly right. So, in this project that I'm maintaining, we have tests for a couple of clients. Not all languages, but .NET is one of them.
And, how it works is that, we pull in the latest version of both.net and the collector, and then we test them both together. And in one such instance, we updated the collector, and it failed, and then we were even able to pinpoint the exact error message that's, how we created this, issue. So we did not try out manually, this was the result of an automated regression test.
**Jade Guiton** 15:23 I see.
Yeah, that would be interesting to have integration tests for all, well, at least a lot of known clients, like, at least official clients.
Because… while this is a bit of a… this was a bit of a weird… Behavior on the client side, like… We want to know if one of the official clients is not… Does not, integrate well.
But the collector.
**GZ Gregor Zeitlinger** 15:56 Cool, yup, that's Cool, yeah, like it.
**Jade Guiton** 16:02 So the other issue, related to profiles, Is it known if it's a similar issue with the newer Poodle buff?
deserialization, or is it, like, a breaking change in the profiles? Because my understanding of… is that the profile's OTLP data model is constantly changing.
So I don't know if it's the same kind of issue, or…
**GZ Gregor Zeitlinger** 16:27 That's totally possible. I have not, investigated this further.
And we do have tests for, For profiling, and in the past, I have had to update both the client and the hotel collector, because they are not expected to be backwards compatible.
Yeah, so maybe the second one is not a good pitch for what I'm trying to say after all.
**Jade Guiton** 16:58 I see, but yeah, it would definitely be interesting, I would be in favor.
**GZ Gregor Zeitlinger** 17:06 Do we want to know more about how this tool works, or should we discuss this offline? I don't want to take too much time off the meeting.
**Jade Guiton** 17:17 If you have a link, maybe posting it in the meeting notes.
Could be a good jumping-off point.
**GZ Gregor Zeitlinger** 17:25 Okay, cool, yeah, then let's do that.
Yeah, you can continue. I'll put the link there right away.
**Roger Coll** 17:41 I think that the next one, it's me. Maybe I can share the screen as well.
So, I wanted to bring this topic about the… Pipeline component telemetry, and the metrics that Basically, they were proposed in this RFC.
That are described down below, and ask a little bit about the current state of it.
If it would make sense, also to start adding them, in semantic conventions.
And… Yeah, basically that, and I guess also we need a future guide that if… also, If you think that would be part of… P1, or if it should be… yeah, tackled, before that, because at the moment, I think that the only internal metrics that we are, generating use the underscore notation, that it's not, very open telemetry, native.
That would be great to start having that, and not have breaking changes, soon.
I don't know if anyone has some… some… To date, or some news regarding this topic.
**Jade Guiton** 19:09 So, the metrics defined here are implemented in the collector right now, but they're under a feature gate.
**Roger Coll** 19:18 Alright.
**Jade Guiton** 19:19 So… Yeah, I'm not sure… For the… relating to SEMCOMF, My understanding of the goal of some semantic conventions is that it's to standardize the metrics emitted by various software So As we want to generalize this to hypothetical different collector implementations.
What do you think would be the… It's the main reason to… put those in semconv.
As opposed to treating them as this application's unique metrics, I suppose.
**Roger Coll** 20:00 That's a good question, and I think we already have some… Definitions that are, let's say.
for only Autel-native applications, define it in semantic conventions, so those, I guess, should be part of it, in my opinion.
Same way as, for example, we treat the ones for, that are generated by SDKs.
So… That's literally my plan.
And also because, for example, some of the metrics, maybe not the ones produced here, but there's an internal metric called processor, CPU time, or something like that.
And that, for example, it does not exist in semantic conventions, but we have another one that, it's called process.cpu.usage, so it's… It's kind of the… The source of truth that we get for these metric definition descriptions, and that we can reuse, right, between components.
So, the idea would be a little bit too aligned these two areas. One would be the collector, and reuse the ones that are already defined in semantic conventions.
And then, obviously, add the ones that we are defining here, and already using in the collector, as you mentioned.
**Jade Guiton** 21:28 For things for, like, CPU usage, it makes sense to align with semantic conventions, because many applications We'll emit that and same thing for SDKs. Many different applications will use these SDKs.
But for these specific metrics, they're highly specific to having… A collector pipeline.
So… while I'm not opposed to standardizing them, I'm not sure if there is If there's enough benefit, especially if it means we would have a harder time changing those metrics, considering they're all still in alpha.
For now.
That would be my concern, is, like, that they would lock us into…
**Dmitrii Anoshin** 22:17 specific version.
**Jade Guiton** 22:19 Despite them being very experimental, and only used in the collector.
**Dmitrii Anoshin** 22:27 They are now experimental, but later on, we want to have them.
Available, and to replace whatever we have currently with underscores.
I believe, even if it's only for the collector, it makes sense to bring them to the semantic convention for the purpose of consistency with other definitions.
Because, as Roger said, we have SDK metrics, right? And if we don't even look at them and define our own collector metrics and stabilize them.
going forward, they might end up being, like, some inconsistency between how things named, how, like, the attributes and metrics structured, comparing to SDKs.
And, bringing those to semantic convention early in the experimental phrase would help with that, I believe.
**Jade Guiton** 23:23 I see if that makes sense.
**jmacdonald** 23:29 Yeah, also there's a trail of OCHEPs that have tried to do this, and every time we got to this sort of point of understanding what we were writing about, it became more complicated. So this has evolved quite a bit since the last time someone tried to write a semantic convention.
But definitely, between the SDK and the collector, there's a will, at least an interest, in trying to do that. And then, some of you know we're working on another pipeline in Rust right now that we would like to bolt into the Go Collector, so we'd like to have a definition that we can target in Rust or other collector pipelines, yes.
**Jade Guiton** 24:04 I see, that would make sense.
**Roger Coll** 24:08 That's a great point.
Okay, then, thank you. I guess we will work on, yeah, adding those on SEMCOM soonish.
And yeah, thanks also about the update of the feature gate, I don't know it.
Thank you.
**Jade Guiton** 24:25 You had a question about V1, I'm not sure if that was V1 of the collector, or…
**Roger Coll** 24:31 Yeah, exactly. Yeah, no, be one of the collectors, but…
**Jade Guiton** 24:37 Yes, if it's…
**Roger Coll** 24:37 Under feature gate, it will be… Or enough, or a stable, before we won, right?
**Jade Guiton** 24:45 I'm not sure what the… I don't think we've added that as a requirement for V1, stabilizing those metrics.
I'd have to check.
The long-term plan for replacing the existing metrics with underscores By the new pipeline metrics is not defined.
So I doubt this will be ready by 1.0.
**Roger Coll** 25:16 Okay, yeah, and I guess it will depend on the same comp sterilization as well, if we… if we link it to that, to that.
**Jade Guiton** 25:25 Yeah.
**Roger Coll** 25:27 Okay, yeah, I can, I can follow up on that.
So…
**Evan Bradley** 25:48 I thought I saw Pablo in here for a minute.
**Kells** 25:52 Apologies, just as the question I was asking in the chat, what is the best way to interact with the semantic convention team? Is it… Is there an email address, or a Discord channel, or a Slack?
just ask, like, newbie questions about how does the actual model interact, why are some of the model names different, and what was, like, the point of some of the relationships? Like, some of the design doc information?
Is anyone… Can point me in the right direction?
**GZ Gregor Zeitlinger** 26:27 I would start with the Slack channel. I can, can look it up. Sometimes it's easier to go on the SIG call if you don't know exactly what to ask. Sometimes it can be difficult to ask the right question, and in the SIG call.
You will get an answer. They can point you into the right direction.
**Kells** 26:50 Okay, thank you.
**GZ Gregor Zeitlinger** 26:53 I'll put the channel name in the document as soon as I find it.
**Kells** 26:58 Awesome. Thank you so much.
**Pablo Baeyens** 27:25 Oh.
Jason, I see you have your… Honda's…
**Yaten Dhingra** 27:31 Yeah. Hi folks, I just, wanted to ask one, quick question.
Actually, in the public cloud channel, I, Andrew mentioned that, the AWS CloudWatch log exporter is, does not have any, code owner as of now, and it will get unsupported in, in a week or two or something.
So, I just wanted to ask that, I had a word with Andre about this, and I have been, contributing to, OpenTelemetry for quite some time.
So, is this any way that I can, volunteer for becoming a co-owner for… the CloudWatch log reporter component.
And I have a PR, raised in, for that. There was an issue which was, I think, raised by the IBM software group.
So it was blocking their progress, and So… Yeah, sorry.
**Dmitrii Anoshin** 28:35 I don't think we have strict requirements for the code owner. It should be at least some contributions to the component, and you have to be an OpenTelemetry member.
OpenTelemetry project member.
If… These points are… checked, we can… you can create a PR, and I'm happy to help you with merging it.
It's always great to have more contributors available to maintain confidence.
**Yaten Dhingra** 29:06 Okay, so I should open a PR for this? Like, do we need any sponsors for this also? Because… In the document.
**Dmitrii Anoshin** 29:13 So, if it's unmaintained, if there are no current maintainers, there is no other code owner to approve UPR other than, like, other OpenTelemetry collector maintainers and approvers, and I'm happy to help.
From the standpoint of maintain.
**Yaten Dhingra** 29:35 Yeah, sure, I think I'll raise a PR about this, and I will share this on Slack with you, if you wish.
**Dmitrii Anoshin** 29:42 Sounds good, thank you.
**Yaten Dhingra** 29:43 Yeah, sure, thank you.
**Pablo Baeyens** 29:54 Okay, it seems like I arrived just in time.
So, I want to stabilize config optional, as in marking us.
1.x. I have a PR for that, I guess… yeah, well, first, if you have anything that you would like to see on config optional, make sure to say it now, so that we… Or, like, say it on the issue, so that we, Consider whether breaking changes would be needed to support your use case.
And then, second, we already know there are a couple of things that are not supported by config optional right now, so it doesn't mean that Config Optional is feature complete, just that we won't make breaky changes.
Specifically.
supporting scalar values is something that, well, Evan and Jad have worked on, and it's not there yet. And also.
optional fields that are enabled by default is not something that we support right now.
So, yeah, if you have any… Anything that you would like to see, feel free to leave it on the issue. If you think config option is ready, feel free to… not ready, feel free to review the PR.
Thanks.
**Evan Bradley** 31:36 I think that's it.
Going once, going twice.
**Alf Kenny** 31:40 Is the floor open to just general… Requests and discussions?
**Evan Bradley** 31:47 Please?
**Alf Kenny** 31:48 Sure.
I was hoping that, I think his name's Sean Porter was gonna be here. He seems to be the code owner for the tail sampling processor, but in his absence, I think my proposal or request is relatively straightforward.
I've been… share that screen. So, I've been working with tracing quite a bit. In my company, I'm one of the primary maintainers of tracing, and… One of the issues I sometimes have found myself having is the inability to, sort of, revert or put a knot on one of the policies within the tail sampling processors. So there is this idea of, like, an inverted logic, but that's going away, and it's not really helpful in my case.
But what I would really… would be really appreciated and helpful is if I could just take a sampling policy and say, whatever that decision is, invert that such that it's sampled instead of not sampled, or not sampled instead of sampled.
And, from what I can tell, it should be relatively straightforward. There could be just, like, some sort of… switching logic based off of what was… what the sampling policy was, and then just decisions made off of sample 2. I'll make this a bit bigger. Sampled to not sampled, or vice versa, or something like, if there's an error, the user can define what that should result in, in terms of this NOT gate. But essentially, it's just a NOT policy that can wrap around other policies within the tail sampling processor.
We already have something like a NOT as well as a drop, but in both those cases… sorry, we already have an AND and a drop, but as described… is described in this issue, neither of those really handle the situation.
And, one example, just to give us some, some, some color to this idea, is that what I'm… Currently, particularly looking for is the ability to sniff out, sections of a distributed trace. So if a trace is being sent, you know, is being generated by multiple applications, one of whom is going through an open… sending its telemetry through an open telemetry collector, I want to be able to determine if this is, if there's no root span in this trace. So, if all of the spans that have been sent from this trace have a parent span ID, and none of them have a nil or a zero.
I would like to be able to make a distinction and switch on that situation by saying, I only want to sample the spans that… or the traces that do not have a… a… a root span. And… Currently, there's, as far as I can tell, and I've tried many different ways, there's no real way to do that with the available policies, but if we just had something that said, look for a span with, with a root, or look for a root span, and the moment you find it, we'll call that a true, and then we'll apply a not to that, and we'll call that a false.
That would allow me to do what I need to do.
**jmacdonald** 34:42 Hey, Alf. I'll speak not for Sean, but I've spoken with him about the component, and I've begun to make sort of ownership claims, so I will review your work, and I do understand that codebase pretty well. Tomorrow, there's a sampling sig every other week, and it's tomorrow morning. If you'd like to speak more about this topic.
I started to imagine some changes in that code, and… Sean's advice was maybe we should start on a new component, like, rather than starting to get too involved with this one, which was a little bit of a warning sign.
So… but I'm definitely interested in talking about the feature. The reason I was in there, is that, the OTEL specification has gained some, work on probability sampling recently.
And those ideas should be applied in the tail sampling processor. It's just a ton of work that needs to be done, kind of, to get all the pieces in place. So, anyway, I'd be glad to talk about that tomorrow at the sampling SIG. It's 8 a.m, or an hour earlier than this meeting. Otherwise, please put me on your code review on JMACD. Thanks.
**Alf Kenny** 35:47 Perfect, thank you very much. Is that in the Google Calendar for hotel?
**jmacdonald** 35:51 Should be able to find it tomorrow.
**Alf Kenny** 35:53 Very much.
**jmacdonald** 35:59 Anyone else with a, item for the floor while we're here?
Well, alright then. Thank you all for joining us. I'll see you next time.
**Pablo Baeyens** 36:15 Yup.
