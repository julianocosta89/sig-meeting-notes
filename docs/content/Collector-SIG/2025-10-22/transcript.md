SIG: Collector SIG
Date: 2025-10-22
Duration: 42 minutes
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 01:54 Hey.
I think we can get started, if you want to go, Marilla.
**MG Marylia Gutierrez** 03:29 Yeah, it's all good.
So, hi everyone, for those who don't know me, my name is Marilla. So, I work in a couple of different SIGs, but one of them is that I'm a maintainer for the Contribute experience. I don't know if any of you noticed, but sometimes when a new person merged a PR that… and they are not yet, like, a member of a hotel, it shows, like, a message, like, hey, want to fill out the service? It's just for us to get a sense of how people are being able to, like, contribute to Hotel, if they're having, like, some issues.
So I check this, the answers, every week, and then once I get a good amount, I'm going to the actual SIG, just to provide the feedback that we receive. So, this is what I'm sharing here today. So, we got… so for this, it's both, like, the main one and the contrib one, and… The average, like, for the 13 answer is 4.6 out of 5, so you guys are getting a lot of 5, and a couple of twos and 3, a couple of complaints, so those are the ones that I want to bring it up. In general, people are happy with the process, a lot of comments, like, all good, people very, like.
people being very helpful, and things like that. And a few points of improvement is, is… a common comment is pretty much saying that we, like, oh, I got, like, my PR approved, but it's not actually getting merged. So, can take sometimes, like, several days or a week to actually get merged.
So people are confused with why it's not getting merged? Do I need to ping another person? Do I need to ping a specific maintainer? So I think that is a part of the process that maybe, like, keep an eye, have a little more frequent just checking, like, approve the ones that are already approved to get it merged. One tip that I can give that is something we… that we are doing on the JavaScript SIG is that we noticed we were having, again, like, a lot of PRs open that were just forgotten. So, as part of our, like, the meeting that we have.
We dedicate a few time at the end, just to go over PR, and we go by Otis Chinuis. Just make sure that somebody is at least assigned to review, people are, like, paying attention, or, like, doesn't make sense anymore, we can just close.
And with this, in a couple of months, we went for, like, I don't know, several pages of PR, and we are now down to, like, one page of open PRs.
Just by making sure that people are looking at it. So yeah.
That's the feedback that I have for this group.
**Jade Guiton** 06:06 Do you know what kind of approvals we're talking about here? Are we talking about, like, code owner approvals on contribib, or…
**MG Marylia Gutierrez** 06:14 So… I got two different types of comments, so I had a few that were saying, like, I got from the co-owner, but… I don't know if I still need from, like, a maintainer, and there was… that process was not clear, and some were already seeing, like, already got one from, like, the maintainer, and it was still not merged. So we had, like, both cases.
**Jade Guiton** 06:38 I see, yeah.
In the first case, it sounds like the main thing to do would be to clarify that, yes, you need an approval.
from Contrib Maintainers.
and for the… for the latter, it might be the… the problem might be that on the core repo, there are approvers that are not maintainers, so even if they approve the PR, they can't merge it. So yeah, it might be good to have a process in place to make sure that peers that are ready to be merged get the attention they need.
**MG Marylia Gutierrez** 07:12 Yeah. Oh, and there was also one comment, there was, like, a single one, and I don't have more info, they were just complaining that a broken pipeline. He was like, was not caused by my PR, but I had to keep trying to fix the pipeline, so I don't have more info on that one.
**Pablo Baeyens** 07:35 Maybe it would be interesting to have issues for these? Like, for the… Process for getting… PRs… Reviewed or, well, not forgotten about. Could be… could be useful, just to… to have a place to discuss things and, yeah, eventually pick it up.
**MG Marylia Gutierrez** 07:56 Yeah, well, other things that I can give a suggestion… so we did something this on the JavaScript, and now we are adding to the communication sig, is that for the cases that they're, like, the code owner that needs to approve.
After that gets approved, we are adding the label already, like, automatically saying, like, has owner approval. So this way, like, maintainers can just, like.
From time to time, just check the ones that already have approval from code owner, and just do, like, a double check, and then get a merge.
**Edmo Vamerlatti** 08:30 Yeah, for the cool…
**Pablo Baeyens** 08:31 I mean… Sorry, go ahead.
**Edmo Vamerlatti** 08:34 Yeah, for the REPL, the PR review process is defined on the README file. Maybe you should move that to the contributing as well, because it's hard to find how the process works.
**Pablo Baeyens** 08:51 I think that would make sense.
And I was going to mention we have the ready-to-merge label, dot.
Usually… helps getting PRs merged faster.
**Christos Markou** 09:09 The problem with this might be that it is manual work that needs to be done, like an approver or a code owner, if they are… if they have the rights to add labels, they need to explicitly add this, so as a maintainer can get this… find this and get this merge. Probably if we could automate this and have an automation that could As it was mentioned, to automatically add the label if co-donors have approved, and at least one or two approvers have approved.
then it would be smoother, I guess.
**Pablo Baeyens** 09:55 Trying to capture the list of things on the meeting notes. So automatically add label if code owners have approved, and probably have done so as well.
Approval, process, description to… Contribute something empty on… Versus… meetings to… Go ahead.
**MG Marylia Gutierrez** 10:30 I'm gonna add here the link of the… the PR that we did on the JavaScript. Put it both on the chat and on the things that the… has owner approval, so that is the script that we have been using there.
Maybe it's a… it's a helpful… at least as a starting point.
**Pablo Baeyens** 10:51 Cool. Yeah. So… Yeah, we can open issues for this, later. I mean, yeah, if somebody wants to volunteer now, Feel free to say so, if not.
Maybe I'll Pick it at some point.
Unopened issues.
Okay, so I think we can move to the next one.
From… I believe it's Danio?
**Dhanya R Mathews** 11:27 Hello, hi.
So we've had a PR that was opened a couple of months back.
We got a review few… again, that was also a couple of months, one or two months back, but we still are not able to, you know.
proceed with the PR. This PR is about, I'm audible, right?
**Pablo Baeyens** 11:51 Sort of scared.
**KALMANMETH** 11:51 Yeah, we hear you.
**Dhanya R Mathews** 11:52 Go ahead. Yeah, we can hear you. Thank you. So, this PR is about adding a new sampling policy to the tail sampling processor. So, in our experimentation, we have noticed that tail sampling processor is not, you know, the sampling policy doesn't account for the different use cases that this application service is being subjected to. So we have raised this PR to account for the use case as well, given that the tail sampling process already groups that raised Groups expans by traces, and then, you know, we have the scope of, analyzing which use case a particular trace belongs to, and giving.
giving some portion of the sampling budget to that particular use case as well. So this PR was, kind of raised in August, but we… the activity is, like, really very slow here. So the last comment that we've had from the reviewer was in September 13.
We have, you know.
responded… the last comment from the reviewer was on 9th of September. We have responded for that on 13th of September, but still, you know, we're not hearing back from them, so we would like to seek your advice on how we can proceed on this PR.
**Pablo Baeyens** 13:06 Right, so thank you for… for bringing it up here. I think you… you did the right thing.
We can… so, the reviewer is not here, because this meeting happens a bit early for, for him.
I am wondering if it would be a good idea for you to go to the sampling SIG, so you could either… Go to this, CNCF Slack channel that I, put on the Zoom chat, or… There is a meeting tomorrow, Happens at 8 Pacific time, it's… I sent you the link as well.
**Dhanya R Mathews** 13:49 And, there you can find the… the experts for…
**Pablo Baeyens** 13:54 sampling, including, the reviewer here, Joshua McDonald, and they can probably help you move this forward. There's been some… Changes and some, like.
development regarding sampling, the samplingSeq level, and I think it… it's probably the best place to get feedback on… on this, unless somebody else in in the call right now wants to.
Say something?
**Dhanya R Mathews** 14:23 Thank you, we shall follow up, using that, you know, SIG meeting. Thank you.
**Pablo Baeyens** 14:37 Okay, feel free to, I mean, ping me or come back to the collector's seat if you, don't get open on the PR.
**Dhanya R Mathews** 14:46 Sure, sure.
**Pablo Baeyens** 14:51 Okay, so I think we can go to the edgeless Lambda receiver.
component proposal?
**Michalis Katsoulis** 15:00 Yes, hello?
So, yeah, probably most of you don't know me, except from the people working at Elastic. So, my name is Michalis.
So, I believe that this is the right place. I'd like to, bring to your attention a proposal we have for a new component, in, OpenTelemetry contrib. So the component's called AWS Lambda Receiver.
And this receiver is designed to run an OpenTelemetry collector as an AWS Lambda function, implementing the Lambda handler to receive AWS invocations and decode messages using existing encoding extensions.
So… yeah.
the motivation behind this, is that AWS Lambda functions, are a very popular serverless service for event-driven architectures.
Because, like, many AWS services, like S3, Cloudwards, SNS, S2S, can trigger Lambda functions, and we think that this is an ideal entry point for, collecting data from AWS services.
So, in the AWS ecosystem, services like, virtual private networks, Elastic Load Balancers, CloudTrail, can store their logs in S3 buckets or in CloudWatch.
And when new files or events are created, this can trigger Lambda function. So, this Lambda function runs an OpenTelemetry collector using this proposed receiver.
what the receiver does is, it is identifying the trigger type, whether it's coming from S3 or from CloudWatch.
And if it's coming from the streets, it's gonna go and download the S3 file. If it's from CloudGo, it's just gonna read the event. And then it will leverage existing encoding extensions, like AWS logs encoding extension, to decode the service logs.
And then this past OpenTelemetry logs are sent down the pipeline to exporter, processor, whatever you want.
In general.
I believe that using an AWS Lambda as a collector is an excellent approach, because you can leverage the auto-scaling mechanism of Lambda, which can scale up to 1,000 concurrent executions.
During high load. Also, it's cost-effective, as customers are charged only for the actual processing time, and not for the idle time. And, also, this event-driven, model.
Leads to lower latencies, compared to polling, based, approaches.
So, at Elastic, we have been working on this for the last, 6 months or so, and, we have built a product, which is currently, like, in TechPreview, which uses this component.
So we have tested this with high volumes, we have tested it with real-world scenarios, and I think we're confident that this is, like, a way forward for collecting telemetry from AWS services. And if you see, like, currently, there are, vendor-specific solutions for such serverless forwarders. There is one by Elastic, there is one by Datadog, and some other companies.
So, I would like… what we want to offer is, like, a solution by only using upstream OpenTelemetry components.
So that we can leverage the event-driven architecture of AWS services.
Yeah, so… We are offering, on our side, a well-tested component that currently supports triggers.
from S3 and CloudWatch, only for logs for now, but can be expanded to support metrics. Also can be expanded to get, to receive triggers from, SNS, SQS as well. And we're looking for a sponsor, to help us upstream this component.
About ownership, we are open. We can take the ownership ourselves, or if anyone else wants to share it, to share the ownership with other contributors, would be great.
Yeah, so… I guess that, there's the issue linked, so if anyone wants to take a look and… Asking a question here on the issue, I'm glad to… To… to respond.
**Pablo Baeyens** 20:07 Thank you.
I personally don't have the bandwidth to sponsor a component right now. I agree with the comments on the issue about clarifying… the relationship or differences with the OpenSummetry Lambda extension, I mean, I think it's also fine if Elastic ends up being… like, if an Elastic approver ends up being the one sponsoring this, would be… good if we find somebody else, but, like, yeah, that's not a requirement, is what I want to say.
**Michalis Katsoulis** 20:41 Yeah, yeah.
Like, by the way, about this, question about existing OpenTelemetry Lambda receiver, it's… it's different, they serve different purposes. This, existing, Lambda… OpenTelemetry Lambda receiver is about, getting telemetry of your existing AWS Lambda.
So, our… our proposal here is a receiver that is the Lambda running as a collector, so the Lambda is the collector.
And you get telemetry from your AWS services, so it's not… For your Lambda.
If that makes sense.
**Pablo Baeyens** 21:26 Yep, that makes sense.
**Michalis Katsoulis** 21:29 Okay, thank you, just, I wanted to raise awareness, that's all, yeah. I mean, it would be great if it was, a sponsor outside Elastic, but, yeah, in any case.
**Pablo Baeyens** 21:40 Alright, thank you for doing it. I don't know if somebody in the room would be willing to… to sponsor it. If not, we can continue the conversation on the issue.
**Michalis Katsoulis** 21:52 Yeah, thank you.
**Pablo Baeyens** 22:01 Yay, so… Then, I am next.
So, as you may have seen, if you are a maintainer on NEC, or have been following the graduation process, well, let me first step back. So, OpenTelemetry is a CNCF project. CNCF projects have different stages that they can go through. Right now, OpenTelemetry is in the incubating stage, and… We applied, some time ago, for the foundation to consider promoting the project to be graduated. That means, We get access to certain resources, marketing, things related to CNCF events that we don't have right now as a project.
And, so, that's one of the things that the Open Technology Governance Committee has been working on.
There's several stages where there's a particular committee within the CNCF called the Technical Oversight Committee. We'll look at, different areas of the project and different aspects of it, such as security, governance, So the last step that the TOC, the Technical Resite Committee, has been doing is adopter interviews. These are interviews with companies or organizations that use OpenTelemetry And they interview them to get their, their feedback and their opinion on the project, so that, well, They can give us, particular recommendations, and, like, make sure that… That we are ready for graduation.
So on… over the past few weeks, the governance committee has met with the TOC, and we've gotten some recommendations. You can see the… the doc I linked on the… Meeting notes, this is… approximately what we got. We got some names from the adopters, but otherwise this is the feedback that we got in written form. We then discussed it, and you can see the meeting notes on… on one of the tabs on that document.
And so there's four recommendations, then there's… or four key outcomes, then there's, on the bullet point level, specific ways to achieve these, these key outcomes.
The TOC was clear that they don't want us to specifically, do those things listed there, so, like, it's not a requirement for graduation to have long-term support, for example, it's just a way to achieve that key outcome.
And so… The… the governance committee, and then, earlier this week, the collector maintainers and approvers, have been… Talking about this, seeing how we can… Interpret these recommendations and apply them both at a project-wide level, but also at the specific, collector-stake level.
In general, we feel like this is not a particular critique on, like, the quality of the things that we're releasing, more about… communicating, what the different stability level on components on second trip is. As you know, that varies. There are some components that are really, unstable, and some that are, you know, widely used and more stable.
And so, Yeah, I just wanted to share this for awareness on, like, the situation. I will share the collector-specific things that the approvers and maintainers group talked about, hopefully later this week, if I have time. And, you know, this is not, like, a decision that the collector approvers and maintainers have made, but more, like, we wanted to get some rough consensus before we… expose it to the wider community and, like, got feedback from everybody. So we'll go through the usual process of, like, discussing things in issues, RFCs, and you should also expect to see some OTEPs, at a project-wide level for discussing some other More general project aspects.
I invite you to, see the recording from the specifications sequence yesterday, where Austin, also from the governance committee.
talk more about this at a more generic level. Yep, I'm… Happy to answer any questions you may have. I'm sorry that I don't have the collector-specific items yet. I hoped I could make it for this meeting, but I… I haven't had the time.
And if there are no questions, we can go to Roger.
**Roger Coll** 27:28 Bablo.
I guess that you can hear me now, and… Basically, I wanted to ask about the default logger structure.
use at the moment in the core collector and in the contrib. So, as I guess many of you might know, in the core collector and in the contrib.
the default telemetry logger for all the components is a ZAP instance, that's a library made by Are you aware?
And I don't know if this has been discussed, lately, or at least I couldn't find any open issue about changing that into another, maybe a more actively maintained or more standard, library, like, for example, the Golang's… Nowadays, the standard, structuring logging library that is S-Log.
And… Basically, I wanted to bring this because we noticed this issue in the eBPF profiler. So, basically, this… in the eBPF profiler.
did not follow, let's say, the standard way of developing components, at least it went the other way around. So, first of all, we developed, like, a sample binary, and now we are transitioning to make it a receiver.
what happened there is that all the codebase used another logging library, that is a logRuse, and we want to change that, and… From all the, basically, all the maintainers.
would like to use the Golang Standard Library that's called S-Log instead of, another one, like ZAP, or any other one, and this is because this is… looks like it's the way to go in the Go community, because in… a few years ago, there was no standard Go longing library.
And if we go that way, or basically if you run nowadays the eBPF profiler with the collector, you will see, let's say, a different formatting for the internal logs, as the link that I have shared is an example of this mixed format between Logros and ZAP.
And also, one of the reasons to change it is because ZAP, it looks like it's not actively maintained, at least there hasn't been any release.
since more than one years ago, and actually, for example, some of the PRs that, the AVPF Profiler maintainers made into the ZAP logger. They haven't been released yet in more than one year.
So, it looks like it's not very actively maintained. And I just wanted to… to ask if… Give a little bit of context on if there is any issue or discussion on… maybe there was a decision that, that won't happen.
And just wanted to ask if someone has the context for that.
Or if not, I can maybe open an issue in the core collector with all this.
**Pablo Baeyens** 30:42 I can give you my opinion, I don't know, like, somebody else wants to talk. So, I… don't particularly agree that SAP is unmaintained. I think they are pretty conservative in, like, merging changes, and, like, yeah, they go slow, but I don't think it's unmaintained.
We… made the decision to go with SAP for the component telemetry settings truck, and that is already Mark 1.0, so… we should support log, sorry, ZAP, Going forward, we can deprecate it, but, like, we cannot outright remove support.
I think the way to go here, in my opinion, is… Just to use the… the subhandler, so there's… this package I sent on the Zoom chat, that creates a handler that can be used with the log S log, and that way you can Sort of.
use S-Log, but, plug into our, existing SAP framework.
And, I mean, if that… proves popular enough, we could, think about replacing everything, but, like, that would be the very first step, in my opinion, like, just… you…
**Roger Coll** 32:08 Okay.
**Pablo Baeyens** 32:09 use S-Log through the handler, and we see if there are particular benefits from that, or…
**Roger Coll** 32:20 Okay.
Yeah, makes sense, and I think, actually, that was… what you shared, it's what was the initial idea for the UPS Profiler, to just wrap it with this… with this library, so… Yeah, I agree that maybe you kind of start with that, and… and see if, for example… well, let's see how the maintenance of the upstream goes, because, yeah.
**Pablo Baeyens** 32:46 probably some PRs are nerds, but .
**Roger Coll** 32:50 At least there hasn't been any release near anything planned, on the last month.
**Pablo Baeyens** 32:56 But definitely, it moves slowly, yeah.
**Roger Coll** 32:58 Okay.
**Pablo Baeyens** 33:00 I'd also be curious on understanding what the changes that the EBPF SIG has tried to…
**Roger Coll** 33:06 It was something… Yeah, I can… I can look for them, but it was something about the war… a warning level of… not being parsed correctly of some… instead of warning being warning, the whole, let's say, the whole word, or something like that. Nothing that it's super crucial, but it was, like, a back in a logging provider that it hasn't been released. That's why, let's say, the maintainers out of it.
yeah, concerned about, using ZAP, and… Thinking that maybe that was the way to go before having SLOC in the Golan community.
Mmm.
But… Yeah, probably we can research more about what's the… what's the corona state there, and… and airplanes.
But, yeah, thanks for sharing all of that, and knowing that That it's already on stable, sorry.
**Pablo Baeyens** 34:09 Yeah, I mean, the fact that it's stable doesn't mean that we cannot, move away from it at some point, just means that we will need to.
**Roger Coll** 34:16 Saints.
**Pablo Baeyens** 34:17 work for it.
**Roger Coll** 34:18 Okay.
Makes sense.
**Pablo Baeyens** 34:20 And, Jad, I think you… you want to say something?
**Jade Guiton** 34:23 Yeah, I guess one question would be, in, version 2, would it not be possible to drop support? Like… For V1, obviously, we can't, but…
**Pablo Baeyens** 34:36 Sure, yeah, I mean, yeah, I… I think a component V2 is something that we probably want to avoid, given that it's, like, a fundamental… Module, but, Like, yeah, if we… if we end up doing it, we can drop support, but .
**Jade Guiton** 34:54 Right.
**Pablo Baeyens** 34:55 In my opinion, we should… First… See if this is actually what we want to do, and, like, use the… The bridge, the handler.
**Jade Guiton** 35:06 Yeah, yeah, definitely. I was just thinking, like, hypothetically, in the far future, I guess, I guess it could be done. My two cents about this is that if we decide to move away from ZAP, I don't think… S-Log would be the way to go. I think we should use the OTel SDK's blogger directly.
Because it's… Well, it has… it offers more possibility, and it would be… Unfortunate if we are unable to dogfood our own.
API, I suppose.
In the same way we're doing with the tracer and the metric meter provider.
**Roger Coll** 35:50 Yeah, makes sense.
Alright, and… Thank you for the… for the feedback, I… I will share it with the… Profiling post and see… How we got there. Good.
So, maybe, Nikolai, your turn?
**Mikołaj Świątek** 36:18 Alright, this is just a short PSA. So recently we've had, some… pretty nasty bugs, one related to Prometheus, to the Prometheus dependency and the Prometheus receiver and Contrib, and then later one related to AutelGo.
And… and it, changes it kind of slightly unwittingly made to how again, Prometheus metrics were emitted by the auto collector, and these actually were both caught when we tried to use a new collector version in Autel Operator to release a new version.
And… Unfortunately, it was nice that we caught them, but it was also much less nice that we didn't catch them before the collector actually released those. So, now we're running these end-to-end tests of the operator with the contribcker image nightly.
And nobody needs to do anything about this, I'm just saying, if you ever get pinged into an issue.
That… about this, then… that's the reason.
Thank you.
And I think we're done, unless, unless anyone else is an unplumped topic that's not engaging.
**Pablo Baeyens** 37:57 Yep, looks like we're done. Thank you, Rhodey.
**Roger Coll** 38:01 Okay.
**Evan Bradley** 38:03 Bye everyone.
**Christos Markou** 38:04 You have one, bud?
**Michalis Katsoulis** 38:06 Bye.
**KALMANMETH** 38:07 Bye.
