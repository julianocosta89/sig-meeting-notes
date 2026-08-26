SIG: .NET SDK SIG
Date: 2026-08-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:07 Hey.
**Matthew Hensley** 01:16 Hey, can you hear me?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:19 Yep.
**Matthew Hensley** 01:21 Oh, cool.
She works.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:25 They'll be even reworking your tech or something.
**Matthew Hensley** 01:28 Yeah, I… Unplugged some things, plugged it back in.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:34 Oh, that's nearly always a mistake.
**Matthew Hensley** 01:38 Well, you know.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 01:46 Hey, Raj.
**Rajkumar Rangaraj** 01:52 Hello, Martin. Hello, Martin.
**Matthew Hensley** 01:54 Nope.
**Rajkumar Rangaraj** 02:07 Marin, I just want to let you know, next week, Converse, I have a scheduled challenge with this time.
for the next one month, I would be able to join every other week.
Today itself, I had a conflict, but I had to cancel the other one.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:24 Next week, Matt and I won't be here either, because we've got a Grafana event.
**Rajkumar Rangaraj** 02:30 Okay, so probably then we may need to skip, I think. If Alan is there, he could drive. If not, I think, The week after that. But any offline conversation, we can keep it going in the Slack.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 02:44 Sure.
**Rajkumar Rangaraj** 03:02 Let me share my screen now.
You have a few things, Whenever I share using the Slack, I lose my cursor, not sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:30 Yeah, so they're not necessarily all my items specifically, but I've put them on there.
Because I figured there was stuff that we don't necessarily have to fully discuss now, but…
**Rajkumar Rangaraj** 03:41 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:42 they will require conversation in the PR slash issue at some point.
**Rajkumar Rangaraj** 03:46 Okay.
I think we can… this is a very simple one, right? This is spec acid, so we get it. That's all, right? Like, or do you think there's any complexity in this one?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 03:59 So, I… the complexity, I think, is… The… the entity… entities themselves are stable, or at least those two are, but the associated infrastructure to actually, like, read them and populate them is still in development.
So I asked Claude Code to, like, do a quick… What would we have to do?
Which is what's broken down into the items there. But the main reason I thought I'd bring this up is… Is this something that we want to be proactively doing, but doing as.
**Rajkumar Rangaraj** 04:36 I'm there.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 04:36 mental.
**Rajkumar Rangaraj** 04:37 I would say we wait for the customer ask. I think if this is getting done in the other languages, there may be asks around the customers.
We don't even need, know at this point what's the shape, and they wanted it. I would say let's hold on for, A few weeks, at least, to see if we have any asks here.
And how… what's the customer feel about it? How do they want it to that?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:02 Okay. Yeah, I wasn't, like, in an immediate rush to start working on it, but we didn't have anything in the repo tracking doing it at all.
**Rajkumar Rangaraj** 05:12 Yep.
This is a good one, too.
Yeah, this one… yeah, I know this is a gap.
In the hosting package, we had it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 05:24 Yeah, so, I don't see a problem with it, but because it's a non-trivial new public API, I figured I'd bring it up for other people to weigh in on it.
**Rajkumar Rangaraj** 05:37 I would say it's… It's one of the important things. Even I ran into the challenge when writing a distro for… we have a Microsoft distro. I ran into the same issue, because… the iOS application builder entry does not have an entry point for us.
But I think that is a workaround to get into the service collection and getting it done.
It's not a bad idea to get it, and this is making life easier, I feel.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:11 Yeah, I figured this one didn't… we didn't need to care about CEMCOM or anything like that, because it's the hosting package, and it's all .NET-specific stuff anyway.
**Rajkumar Rangaraj** 06:20 Yeah.
I'm fine with it, I'm supportive on this one if this has to be that.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:27 Okay, cool, I'll leave… unless you want to do it, I'll leave a comment on it tomorrow, and give Steve the go-ahead to, like, at least open a draft.
**Rajkumar Rangaraj** 06:35 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:39 This one, this is a very large PR. I've gone through it. I'm happy with it, but because it's quite big, I think we need at least one other person.
**Rajkumar Rangaraj** 06:50 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 06:50 Look at this, even if it's… As a black box, and what it's doing, rather than how it's doing it.
**Rajkumar Rangaraj** 06:58 I did look at it. This pier is slightly big and had a kind of a blocking comment. Just hold on in merging this one.
I did review my… take a look at my first stab on this one. So, I need to go through, in depth, as it changes many aspects over here. Just keep it, leave it open for me on this one.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:20 Oh, yeah, yeah, that's… that's why it hasn't been merged.
**Rajkumar Rangaraj** 07:23 Yes.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 07:24 I was waiting for the people to weigh in on it. But, I did suggest to Steve, I think he's gonna do it in, like, a PR immediately after this one, is… So that if you're using the old settings, You will still get output.
It's just the format is gonna change.
So, and then at a later… and in a future point, we could remove that… the old way of turning it on.
Yeah. So it shouldn't be breaking.
Or at least, it's not breaking unless you were parsing the output.
**Rajkumar Rangaraj** 08:02 So, what I want to ensure is that, like, there is a lot of time spent behind this, like, especially this self-diagnostic is done in a way that we don't need to start the process. We use a concept called as memory mapped.
And we also pull the config change every few seconds and see if there is an update to it and do it. So I want to ensure that with all the changes we introduced, none of that breaks over here.
So, keeping the, the production systems in mind, it was developed, but the changes, whatever it brings now, I want to ensure that the Current behavior stays, and it's built on top of it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:44 Yeah, yeah, I… it… I don't think it's in this PR, but the… Because Steve didn't want to make it even bigger again.
**Rajkumar Rangaraj** 08:52 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 08:53 the next change would be to make sure that the JSON configuration still works, but if there's other scenarios that aren't covered.
That are not where you're using, then yeah, that's fine to check on in those too.
**Rajkumar Rangaraj** 09:06 Yep.
I'll… I'm going to spend some more time this week to take a look into it. But I did pretty much covered more than half of the PR already, so I'll take some more time on this one.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:23 And then this one, I haven't done much feedback on the PR associated with this, other than say it needed more test coverage. But, I think you got tagged onto the PR anyway. I think this is a Microsoft person proposing this?
**Rajkumar Rangaraj** 09:37 Yeah. She was doing the… earlier, she was contributing to our repo as well.
Boom.
Let me check with her, like, what is needed on this one, or do we need to prioritize or not?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 09:52 Okay, yeah, because I think the PL went up first, and then for me… for my time zone, at least, this got opened overnight, and there's some questions in it about how the implementation should be. So I figured there was maybe some context behind this that you knew that I didn't.
**Rajkumar Rangaraj** 10:11 No, I don't have any context on this one. I know I'm being tagged, but I don't have any… Context here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:17 Right, okay.
**Rajkumar Rangaraj** 10:18 So, just want to understand if that… it's not in the spec, we need to just question… I never heard of this one, bottom floor, I don't know whether I miss it.
I'm missing anything here.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 10:30 It's not something I've heard of before either, but I kind of get the gist of what it's doing from reading it, but yeah, there is something in the comments somewhere that calls out, should this be a SEMCOM thing? And it probably should.
**Rajkumar Rangaraj** 10:48 Oh, this is, I remember of a conversation driving with the… the .NET logging folks, there was customers, there were customers.
who raised a sampling, request with the .NET team itself directly. It could be a result of that. I can bring more information in the, coming weeks, like, what is this all about?
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:14 Okay.
And…
**Rajkumar Rangaraj** 11:16 Looks like it's based on the request from the .NET team itself.
So, I think this issue does not capture Y and all that, like, let me ask her to add that as well.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:30 Okay, and I've just realized there was another issue I wanted to… bring up, I'm just check… finding it.
**Rajkumar Rangaraj** 11:37 Yep.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 11:39 Because I left a comment on it.
This week, I'm just trying to find it. It was to do with the Logs Bridge.
If you want to move on, I'll find it, and then we can talk about it at the end.
**Rajkumar Rangaraj** 12:01 Okay.
Hmm… I think I… these could be new ones, which I need to take a look. The… there were yesterday, you did many of the buff improvement PR method to catch up on those stuff. So…
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:23 So I think the… I think the one… I haven't put a tag on it. I think the one that would be good to look at first is the… the fixed CA certificate loading. Someone reported an issue yesterday.
to fix for it. But all the others are just random performance tweaks.
**Rajkumar Rangaraj** 12:41 Okay, cool. I'll try remaining to cover before the end of this week. I'll try to make sure all the PR gets covered.
I think… I did.
I don't know, the first one you… did you take a look at the first one? Like,
**Martin Costello (Raintank, Inc. – Grafana Labs)** 12:56 I think I looked at it at some point, but…
**Rajkumar Rangaraj** 13:01 Okay.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:01 and wait, because CJO had lots of comments on it, I've sort of deferred to him.
**Rajkumar Rangaraj** 13:08 Okay.
Okay, I think pretty much we are in control in this one. As we just released it, I think we don't need to hurry on any of these, I believe.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:28 Oh, that reminds me, actually, Rajk, did you want a staple release of Geneva?
**Rajkumar Rangaraj** 13:32 Oh, no. Let's just hold on it. I thought I'll… there is a PR that comes on it. There is a feature, customer has requested for something, we want to add that and then release the stable version.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 13:44 Okay, cool.
**Rajkumar Rangaraj** 13:51 I think pretty much you are keeping this under control. I don't think any new ones that needs Immediate attention in this contrapor.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:03 Let's see what we've got… Yeah, it's just some minor bug fixes and, you know.
**Rajkumar Rangaraj** 14:12 Yeah.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:12 the same conf attributes.
**Rajkumar Rangaraj** 14:15 Yep.
Cool, you, you wanted to, you were searching for something.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 14:24 Yes, issue 6992.
In the main repo.
I'd love to comment at the bottom of this one yesterday. I was updating the spec compatibility matrix yesterday.
with the OTLP exporter limit changes. And I noticed that we don't export the schema URL in the logs, but we do for traces and metrics. So I had a look into what we would need to do to, like, fix that disparity.
**Rajkumar Rangaraj** 15:06 Got it.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:07 And this is a proposal to add some new public API to, like, fill that gap.
So, we don't necessarily have to talk about it now, but it'd be good to get some feedback.
on if we want to do that, and then… and there's, there's a link to a commit where I've got Claude Code to put something together, and if… that seems to make sense, then I'll open a PR.
**Rajkumar Rangaraj** 15:29 Sure, I'll take a look at this aspect when I review the PRs.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:33 Cool. Thanks, Rosh.
**Rajkumar Rangaraj** 15:37 I'll keep you and me in the assignee list, so it will be easier for me to… Figure out. Sure.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:44 That's fine.
**Rajkumar Rangaraj** 15:44 moment later.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 15:51 I'll just edit the agenda.
**Rajkumar Rangaraj** 16:02 That's all we have it. Are there any other questions?
Yeah, I think if there are no other questions, we could end it.
Thanks, everyone.
**Martin Costello (Raintank, Inc. – Grafana Labs)** 16:25 Thanks, Simon.
**Rajkumar Rangaraj** 16:27 T.
