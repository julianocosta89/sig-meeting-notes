SIG: K8s Semantic Convention SIG
Date: 2026-10-13
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Stephen Lang (Raintank, Inc. – Grafana Labs)** 02:51 Hey, we can leave it another minute, see if anyone turns up.
Anybody's got anything for the agenda?
Feel free to add it.
Put the link in the chat.
Alright, alright.
I guess I'll share in case this joins.
Feel free to add your name to the attendees list.
There's a couple from Chris. Is there any… anything from anyone here? Pilot Serena, Abby?
**Abhimanyu Bajaj (Splunk)** 04:51 Hello, everyone. I just joined in. I had that pull request open, the 4158. So I thought it will be discussed today. And I just wanted to hear you guys out, how you guys discuss, you know, just learn and see how things flow along.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:08 Sure, okay. It's mostly async.
But if you… if you've got, like, anything specific that you want to discuss, you know, we can, we can do that here as well. There's the, have you seen the Slack channel?
**Abhimanyu Bajaj (Splunk)** 05:23 Yep, I am.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:24 Yeah, so Slack and GitHub is mostly where the stuff happens.
And then, Is there anything specific that you wanted to sort of bring up and discuss about the PR?
**Abhimanyu Bajaj (Splunk)** 05:39 No.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 05:44 So we can take a look. So this is So these… Are these new metrics? So it's for the memory limit and requests, so this is for the new feature in Kubernetes that allows the pod level limits, is that right?
**Abhimanyu Bajaj (Splunk)** 06:01 Correct. So Chris Mark had that 4133 PR open, where he was requesting changes to be confirmed that if these metrics can be added.
Okay.
And if some of the similar metrics can be grouped together, so this PR basically tells or confirms what all can be done and what all can't be.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:23 Cool, okay.
**Abhimanyu Bajaj (Splunk)** 06:26 You already approved. Yes, please. Sorry. Go ahead.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 06:29 I was sorry, I was just gonna say, I haven't looked into the PR.
I guess one… one thing I'd be interested in, I don't know if… if you know, is how the, how Kubernetes deals with having multiple limits set. You know, if it's set at the container level, does that take precedence over the pod level?
Or is it the other way around?
**Abhimanyu Bajaj (Splunk)** 06:52 Limit is set on the container level. I can quickly check by replicating. I think pod level will take precedence, but I can quickly check once I have the infrastructure ready for it.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:02 Okay.
**Abhimanyu Bajaj (Splunk)** 07:03 Yep.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:04 I.
**Abhimanyu Bajaj (Splunk)** 07:05 the.
**Tyler Helmuth** 07:05 I didn't even think Kubernetes let you set a limit on a pod. I thought it was only on containers. And then at the pod level, it was just.
Some of all the containers.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:14 Previously, that was correct, but in some new version of Kubernetes, they also added the pod level limitation.
**Tyler Helmuth** 07:21 Yes.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:22 very.
**Tyler Helmuth** 07:22 so.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 07:23 Yeah.
So this is… these would be the metrics to kind of expose that… the fact that that is a… now a feature in Kubernetes. So, obviously, one thing I'm thinking, which is probably the same thing as you, Tyler, is if you see metrics at both the pod level and the container level.
What you know, what are you going to do with that information? How are you going to act on it?
And what if you only have The pod level limits, but not the container, and vice versa, and what if you have both?
I'm just not too familiar with the actual Kubernetes logic and the feature here. So I'm just Kind of interested.
I don't know if it would affect the… the metrics in any way, because I guess the metrics just have to represent whatever is in the Kubernetes API.
And it's probably… I don't know if it would be correct to document the Kubernetes behavior.
In the, you know, hotel metrics… themselves.
But that's probably best, you know, being left upstream.
But I guess… Maybe it's important to know how these kind of interact with each other, if you have multiple limits set.
That's just a general comment.
Kind of thinking aloud.
All right, well, thanks for this, Bjarne. If anybody wants to take a look, feel free to do so.
And that is 4158 on the SemCol repo.
**Dmitrii Anoshin (Splunk Inc.)** 08:53 Don't we already have a utilization metric for the pod?
**Tyler Helmuth** 09:00 I think, one of the utilization metrics.
for CPU and memory, not for the limit.
I think it's getting deprecated or got removed already. I can't remember.
Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 09:16 annoyed.
**Tyler Helmuth** 09:17 It was desktop OMIPS. But last I checked, it was wrong or something like that.
**Dmitrii Anoshin (Splunk Inc.)** 09:23 And this utilization will be about against current limit.
Because…
**Tyler Helmuth** 09:30 believe.
**Dmitrii Anoshin (Splunk Inc.)** 09:31 organization.
**Tyler Helmuth** 09:32 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 09:33 Do we want to edit? Because it brings some confusion if we decided to remove those.
And it's unclear, like, against… Which particular… Utilization, it'll be… compared against So why don't we have usage instead? That's my point.
**Tyler Helmuth** 09:57 What's that?
**Dmitrii Anoshin (Splunk Inc.)** 09:58 Usage. Why don't we use? Why don't we have usage or like working set.
**Tyler Helmuth** 10:04 Let me look at what the receiver's doing right now.
**Dmitrii Anoshin (Splunk Inc.)** 10:07 Yeah. Yeah. My point is just like if you, I'm not sure if we need utilization, that's I guess might be confusing.
**Tyler Helmuth** 10:15 Hmm.
**Dmitrii Anoshin (Splunk Inc.)** 10:16 So, if we have user.
**Tyler Helmuth** 10:17 Because it could be calculated, you mean?
**Dmitrii Anoshin (Splunk Inc.)** 10:19 Yeah, yeah, we have, we'll get desired current.
That should be enough.
It's basic metrics, and Yeah. But if you include include utilization, it will be always like.
Unclear to the end users, what do we… What does it mean?
**Tyler Helmuth** 10:42 In this PR, is utilization defined as desired over current, or is it the… Remember.
Working set, if I were working set, okay.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:56 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 10:57 So.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 10:58 Not sure what this means.
**Dmitrii Anoshin (Splunk Inc.)** 11:00 Yeah, this… this is wrong. Utilization… we've been having utilization as a… Metric bounded like from 0 to one.
And here it says that is… Yeah, it's actually like, it's confusing like, why, why, what memory working set divided by container memory working set. This is doesn't seem right.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 11:29 It would also be difficult to calculate in the case of having, you know, mixed Limits.
Between container and… And pod.
Because, do you… You know, if you… if you just have So, if you've got a pod with multiple Containers. And only one of those containers.
Has a limit set, but then you also have a pod limit set, then what do you choose for the.
you know, the total available when you're calculating utilization. It gets even more confusing now, because you are using the container level or the pod level.
**Dmitrii Anoshin (Splunk Inc.)** 12:07 Yeah, I would suggest we exclude visualization from this PR.
Does that make sense?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 12:14 Yep.
And drop a comment on him.
**Dmitrii Anoshin (Splunk Inc.)** 12:20 Thank you.
**Tyler Helmuth** 12:44 Here's a recent… This was the context I was thinking of.
There's a PR, a recent PR, where some utilization metrics have dropped.
Well.
For context.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 13:06 Sorry, Tyler, say that again.
**Tyler Helmuth** 13:08 I was just thinking about utilization as a hard topic in open telemetry.
talking about it now. Here's another PR where We… it looks like we deprecated some utilization stats.
utilization metrics.
So… In this PR.
following a similar… Approach to just stick with.
Stick with the values and not calculate a utilization for the customer, seems fine.
That was the discussion, and this PR was like… The number that we were emitting was either wrong or could be calculated, and so we didn't want to emit it anymore.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 13:56 Let me, let me link that.
Does that make sense, Abby?
Yeah.
**Abhimanyu Bajaj (Splunk)** 14:19 Yes, yes, yes, completely. Thank you.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 14:25 Alright, we have another one here.
4156.
One's from Chris.
Okay, it's pod volume.
**Tyler Helmuth** 14:42 Yeah, it looks like this is a request to start investigating these metrics in depth. See if they're ready for RC.
Chris's initial investigation is that they're probably not.
It seems like the metrics that these represent are more specific to PVCs.
Okay.
Maybe we should change these metrics to be… more specific to that, I think, is what Chris is suggesting.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:06 Okay.
Is there a suggestion that there would be volumes within a pod that are not backed by PVCs?
So, this would be… What, like, host path volume amounts, that kind of thing?
**Tyler Helmuth** 15:40 I don't know. That's a good question to bring up. I only read it really fast this morning, right before the meeting.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 15:45 Yeah.
I don't know if Empty Durr Is that classed as a PVC or not?
If it's just a volume without…
**David Ashpole (Google LLC)** 15:58 DDers are not. No, they're not PBCs.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:00 Okay.
**David Ashpole (Google LLC)** 16:01 Sorry I'm late, by the way.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 16:02 Hi, David.
So yeah, if anybody's got, Any more detail that they can add to this 4156 on Semconf?
They're looking for more comments.
As to whether this should be more specific to PVC volume data.
Thank you.
We got one from Stuart.
**Stuart Buckingham** 16:28 Yes.
Thanks.
So we're trying to replace, cube state metrics with, the hotel collector, Kate's objects. And one thing that's missing is having an owner reference.
For pods, there's already daemon set name and deployment name and stateful set name in the, the spec.
But there's not a generic owner reference, and when you have pods that are, like, like, certificate challenges.
are things that don't belong to a staple set, daemon set, or deployment that shows up as missing. And so there's no way to do that attribution. The Kubernetes The data model does have owner reference, and I linked that on the PR and in the meeting notes.
And that defines the API version, controller, kind, name, and UID.
And so I've… I made a PR to add that to the… hotel definition, but I saw in the contribution guide that you do need to have an issue approved first. So, this is just the issue that sort of lays out that, it would have the attributes kates.owner.apiversion.kind.name and populate.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 17:54 So I actually have an issue for almost the same thing. Maybe we should team up on this.
**Stuart Buckingham** 18:00 Yeah, I did a bit of a research. I found this 1693 issue, so I don't know if yours was… Quite new.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:08 3778?
**Stuart Buckingham** 18:12 Must miss.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 18:13 So this… so this may be because it doesn't have an ID, but… so when I actually looked at raising this as a PR. So, stepping back a bit, I have exactly the same issue as you. Okay. But I looked at this from the workload name and workload kind perspective, and then when I went to This got approved.
So it's been triaged already.
And it looks like it's all good.
But when I came to actually PR this, I found that it was a bit more complicated than I expected, and I came across the fact that we might need this unique identifier at the workload level, and also tracking the API version as well.
So I think potentially the PRs that we both have might be, sort of quite similar and overlapping.
So I wonder if we should team up on this.
**Stuart Buckingham** 18:59 Yeah, sure. Do you want to, have you got… you've got, something in the works already?
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 19:05 Yeah, yeah. So, I have something locally, I haven't pushed it up to a branch yet, but, I mean, we could.
You know, I could create a branch, or if you've got one, we could work on that together.
**Stuart Buckingham** 19:17 Yeah, mine is just to add that, the owner reference with the spec that I put in there.
I'm just reading through yours. Yeah, that PromQL query is sort of the same thing we end up doing, which is horrible.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 19:33 Yeah.
Okay, I'd say, let's are you on slack? Cncf slack.
**Stuart Buckingham** 19:41 Yep. Yeah, I can…
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 19:44 So, let's catch up on mine.
**Stuart Buckingham** 19:54 Just.
**Dmitrii Anoshin (Splunk Inc.)** 19:56 I also would like to mention that And all this complex… Data.
additional data for that we can be associated with Kubernetes objects.
is a… Typically would go as an entity.
Yeah. Data. And we have HTMLs being, reported by… Kubernetes cluster receiver, and it's been kind of… Defined the spec as well, there is some work.
towards that.
So… In the entity world, the ownership would be relationship between the entities.
And it's currently emitted as, Hmm.
log events, like, each entity, like, reported periodically. But also, we are thinking that that potentially can be part of the resource, because in the resource, we already specify which resource attributes Construct… which entities they construct.
Whether it's both, like, deployment namespace.
And we are thinking about… This kind of ownership, basic ownership, basic.
relationship definition there as well. I can maybe share one of my PRs. It's been a while since I've done them.
And it's, like, still… I don't know.
**Stuart Buckingham** 21:29 Oh, really?
**Dmitrii Anoshin (Splunk Inc.)** 21:31 Not really approved. Okay, go ahead.
**Stuart Buckingham** 21:33 Does that mean that the role would need to be able to… get… Because if you've got all of these custom resources and operators and things, then the cluster role can receive, like, watch on all of those objects is going to need quite a lot of scope.
**Dmitrii Anoshin (Splunk Inc.)** 21:55 I'm not sure I follow. Typically, on the resource, you put all of the entities in the chain, like, you would put… you would put pod.
And deployment as well, right?
**Stuart Buckingham** 22:07 Mmm.
**Dmitrii Anoshin (Splunk Inc.)** 22:09 And you need to have some kind of association between them.
**Stuart Buckingham** 22:14 I.
**Dmitrii Anoshin (Splunk Inc.)** 22:14 Association is what we want to put as in data model as well. Actually, let me let me share my.
product VR. It's been abandoned, but we just yesterday talked about it on NTTSIC, and we definitely want to bring it back and have a solution for this. So maybe, potentially, it'll help you.
So here's the PR to the proto.
So, essentially, what it does, it just defines a context ID of an entity where this one is unique.
So, for example, if it's sport, it would be unique within Kubernetes cluster or like namespace or something. So it might be.
Not necessarily.
would help you to define the ownership. Because.
Maybe… Context identity will not be necessarily correspond to the owner in Kubernetes. We need to define that in the Semantic Conventions, but the idea is pretty much the same.
**Stuart Buckingham** 23:24 The service account doesn't need to watch for that if you're using like the CAKES attribute receiver or something like that, a processor or something.
**Dmitrii Anoshin (Splunk Inc.)** 23:34 Can you come again?
So…
**Stuart Buckingham** 23:38 If the entity is not like a fundamental type, say it's like a custom resource or something.
**Dmitrii Anoshin (Splunk Inc.)** 23:45 Oh, I see.
**Stuart Buckingham** 23:46 It belongs to a controller. Do you then need to give… permission to the service account to be able to watch for those objects as well.
**Dmitrii Anoshin (Splunk Inc.)** 23:55 But it's implementation details, but you would need to have access to get to get those objects right and add them to.
**Stuart Buckingham** 24:04 Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 24:05 resource.
So, it has to be done anyway.
**Stuart Buckingham** 24:09 Well, if… so the… the Go K8s API machinery has the function getControllerOf, which just returns a reference.
The…
**Dmitrii Anoshin (Splunk Inc.)** 24:21 Oh, I see. I see.
**Stuart Buckingham** 24:23 You don't need to actually and same thing, you know, you do QPUB and get pods, you don't need to actually be able to.
**Dmitrii Anoshin (Splunk Inc.)** 24:29 I see.
**Stuart Buckingham** 24:30 Access to, like, the underlying custom, Controller and the custom resources and things.
And we want to avoid having to give unlimited scope to the collectors to be able to… and also the overhead of watching all of these other… Yeah.
**Dmitrii Anoshin (Splunk Inc.)** 24:45 Makes sense. Makes sense. You just want to put a reference, but the reference would not provide you any information. I mean, information would be just a name of the object, but the object itself will not be available on the resource. That's what you're saying, right?
**Stuart Buckingham** 24:59 Exactly, it's just, it's a permissions thing for us.
**Dmitrii Anoshin (Splunk Inc.)** 25:02 Okay, so yeah, so in that case, this will not work, because this entity relationship is strictly between both entities being in the resource.
And the resource… baggage. So okay.
Yeah, we can have it added as an optional attributes.
optional resource attributes, I guess.
Okay.
Thank you.
**Stuart Buckingham** 25:26 Matches on UID, does it?
Or you haven't got to that implementation part.
**Dmitrii Anoshin (Splunk Inc.)** 25:31 Yeah, much as… actually, like, reference context ID would be… would be identifying set of attributes for a particular entity, which typically UID of an object in Kubernetes use case.
**Stuart Buckingham** 25:48 Definitely useful, yeah.
Yeah, I think we can take this offline, Stephen.
**Stephen Lang (Raintank, Inc. – Grafana Labs)** 26:03 Yeah, I'll create a new thread in the Slack channel for this SIG, so anyone else can jump in as well.
Is there anything else from anyone you'd like to discuss?
All right, I think that's a wrap. Thanks all.
