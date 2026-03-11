SIG: .NET SIG
Date: 2026-03-10
Duration: 22 minutes
Zoom Recording URL: https://zoom.us/rec/share/svlvFb6ODqy8f2XmJo8Jsaeh0iUoroG8K7M2ktDfuN0TGUivHaqD9-MDcwiMtbJu.E15a4zdgdPkmZJoB
============================================================

## Zoom Recording Transcript

**Martin Costello** 00:12 Hey.
**Matthew Hensley / Grafana Labs** 00:14 Hello.
And thanks for that reminder on the gRPC instrumentation.
I'd, totally forgotten it after figuring out what was gonna happen with Stabilization around that, so…
**Martin Costello** 01:04 That's right, I was just… I was just a messenger.
**Matthew Hensley / Grafana Labs** 01:08 Oz.
It's, it's unfortunate, but it looks like RPC and semantic ventions are going to be stable.
Minus gRPC.
So…
**Martin Costello** 01:21 Alright, Roy.
But how come… is there, like, a specific reason, or is it just, like, time?
**Matthew Hensley / Grafana Labs** 01:29 both… Strangely enough, the…
Some folks at Google have went to weigh in, but don't have the time to, and have their own spec for metrics and trace
Stuff as it is.
So…
**Martin Costello** 01:54 Fair enough.
Hey, Raj. Hey, Zach.
**Zach Montoya** 02:01 Hello.
**Rajkumar Rangaraj** 03:13 I shattered my best up.
People. You don't see it.
Martin, I see that you have a topic, do you want to… Go through this.
**Martin Costello** 03:26 Did you read the issue, Raj?
**Rajkumar Rangaraj** 03:30 Mmm, sorry, I was super busy and did not get time for it at all.
**Martin Costello** 03:38 Right, okay. Well, the TLDR is… there's… the declarative configuration specification is now stable.
And it's reached 1.0.
And there's this existing issue that is the, like, the feature request to implement it in .NET.
And…
we've all just sort of been sat on it, not implementing it, and now it's reached stable. I figure we should probably come up with a plan.
To actually implement it.
So the action… the… my action discussion item is just, so what should we do, and how should we go about this?
Because now it's stable, there's probably going to be more demand to actually support it, and I believe there's a partial implementation in the auto-instrumentation at the moment for .NET, but…
Ideally, it means for the SDK.
**Rajkumar Rangaraj** 04:37 Yeah, I don't think that follows the spec,
I think I'm supportive if we need to do it. Do you know, by any chance, any other languages as this completed?
**Martin Costello** 04:50 Exactly.
**Rajkumar Rangaraj** 04:51 way.
**Martin Costello** 04:52 Java does…
There's another one that I've forgotten what it is. There's at least two who've implemented it, and okay.
Matt and I know, Jack.
who's the spec champion for declarative config, and he chases us and goes, when's .NET gonna do it? But I think that's mostly because, just from an implementer point of view, rather than as a user. But I imagine people will start to ask for this.
As it becomes more widely known.
**Rajkumar Rangaraj** 05:23 I think we should do it in .NET. The reason why I consider this, even though, we can build on top of it several things, like op-amp and all might become better with
be having a separated declarative config like this. I think, if we have a bandwidth, I think we should jump on it and
Continued.
**Martin Costello** 05:46 I think it's less bandwidth, because if no one else has got the bandwidth to work on it, it's probably something myself and Matt
would contribute to, but it's more how should we implement it? Because…
declarative config requires you to use YAML. There's no YAML standard library for .NET, so how are we going to go about implementing reading YAML? Are we going to take a dependency on something?
Because there's no de facto standard library for YAML. Do we vendor it in like Autumn Instrumentation is doing? There's lots of open questions like that before starting, but I think it's better to get at least a vague plan of, rather than just picking the spec up and trying something.
**Rajkumar Rangaraj** 06:35 Sure. So, I remember…
a similar discussion happened in the repo, when I was either neither a pro or on a maintainer, but I recall that. Some AML versus JSON discussion happened in this repo. I don't know whether it happened on the peer or…
On… on the issue.
We can go and check that out.
the previous discussion on where we started. I think Alan should be familiar about it, I believe.
Yeah.
someone, I think it's related to the console exporter, and they want to change it to YAML, something like that.
Do you recall any… by any chance, you…
**Martin Costello** 07:20 I think that predates me getting as involved in the project as I am now, so I don't recall that one.
**Rajkumar Rangaraj** 07:26 Yeah, even same here.
I think this is the one, I believe, and they're not… get… merged.
JSON to YAML. Some conversations happen, maybe this may not be the one. A detailed conversation has happened early.
We can, it's better to have the,
Alan also on the, like, on for this discussion, because, some historic information we need, he may know what was a similar discussion happened in the past.
And,
I know, like, I was supposed to be prepared and coming for this. I'll take one more week to be, like, to see… do some more research and come back on this one.
**Martin Costello** 08:25 Okay, that's fine.
**Rajkumar Rangaraj** 08:26 Yeah.
**Martin Costello** 08:26 Yeah, I think for me, the outcome is just, regardless of who is going to implement this eventually, I think we should have a relatively concrete starting point plan.
So that people can start contributing. Because at the moment, it's quite nebulous. It's just, implement this.
**Rajkumar Rangaraj** 08:45 If you also have any proposal bringing that, also could help.
**Martin Costello** 08:52 Yep, sure.
Yeah, because I can't remember…
which one is which out of the, like, the two YAML libraries, but, like, I know I've used both, and I found one more cumbersome than the other, but then… I think one of the two of them also, like, doesn't have native AoT support, but one does.
So there's, like, lots of different aspects to each one, which makes it non-obvious to, like, pick one, like, say you would with, like, Newtonsoft before system text JSON.
Well, let's punt that for further discussion until next week. And I might put some notes in it in the meantime, but otherwise, that's all I wanted to talk about.
**Rajkumar Rangaraj** 09:53 There is one other topic I wanted to bring, as people are here.
It's called as combined.
So I see, most of the,
GenAI SDKs, for example, like, Copilot SDK, OpenAI SDK, and a lot of them, the people are struggling to understand what instrumentation needs to be added and how to capture the data and everything.
So I'm thinking we should have a, like, a plan to have a combined…
DNA instrumentation library, which can capture on the
telemetry for all of these SDKs.
So, want to see, like, like, I'll do a detailed write-up on the issue to see, like.
If we are interested to do this in the contrib repo.
**Martin Costello** 11:02 Sounds… sounds sensible to me, at a high level.
Because, yeah, otherwise, presumably, every… .NET, GenIA, library, or CLI is gonna reinvent the wheel.
**Rajkumar Rangaraj** 11:16 Yep.
We can create many, the only thing is that I said combined, because there are many things that's coming out, so the maintenance will become very, very difficult. So having a combined one
Seems a reasonable thing here. We say that we support everything, maybe Cloudy, or Gemini, or Copilot, or whatever it is. We support everything to a single desktop. That was the idea I'm thinking about here.
**Martin Costello** 11:48 Okay, yeah, that sounds reasonable on paper, before we get into the nitty-gritty.
**Rajkumar Rangaraj** 11:53 Yep.
jack or Matt, do you have any, suggestions or…
Like, learnings that we could apply on this one.
**Zach Montoya** 12:08 I don't really have anything on this one.
**Rajkumar Rangaraj** 12:10 Okay.
**Matthew Hensley / Grafana Labs** 12:11 I've done a… A little bit with the GenAI conventions,
Yeah, this'll definitely be an interesting one. I…
I agree, coming up with something that they can share will be good, I just… Wonder,
Yeah, if, like, if there's enough extension points.
and these SDKs to wire something up, or if they're gonna have to adopt a library.
how much effort that might be, because I assume, you know, they have different architectures under the hood, so…
Figuring out how to satisfy those is gonna be interesting.
**Rajkumar Rangaraj** 12:51 Yeah, and probably there is a little of work needed from our end. For example, I'll give an example. Someone reached me out yesterday saying that I'm going to come and add a co-pilot instrumentation library here in the contract.
I said that if every library is going to… everyone is going to come and say that I'm going to add something like that, it becomes unmanageable.
So that's when I thought about it. We should have some combined one, and if any instrumentation is needed, probably we should push them,
to their… most of these repos are open source, so we can push them to have the instrumentation natively as a part of that. So the one goal of this brochure be, like, it should not take reference of any of the SDKs, without taking the reference, if we can build something, that would be great.
That's the initial thought,
But I'll write up an issue with all the details in it.
**Matthew Hensley / Grafana Labs** 13:51 I think that's an interesting approach, especially as we hope that other libraries will adopt native instrumentation.
So, like, up next for stabilization will probably be messaging.
I wonder if it would be valuable to offer Yeah, the messaging… library that they could…
Take a minimal dependency and not have to figure out…
How to handle all these attributes.
**Rajkumar Rangaraj** 14:18 gift.
Making anything easier for customers is something we should care more about after this point.
**Matthew Hensley / Grafana Labs** 14:25 Definitely.
**Rajkumar Rangaraj** 14:32 Are there any other topics apart from this?
Good. Let me go to the… I don't know.
That's the one special PR which I want to speak about. I think,
I was wondering, I did the changes to the pull request, I'm thinking, what am I seeing there? Okay, now I have a clear idea. So this one, I think,
pierre… blocked this PR and just provided a comment? I didn't know.
I still need to go through this and provide a response to PR. I think if we have to do this one, it's going to be a breaking change, and at this point, the log record design does not allow us to
do this.
I think we should iteratively consider unblocking the scenario for now, instead of keeping the customers blocked forever, and
In an iterative fashion, we can think at a later point if we… it should take a breaking change and do a 2.0 and everything to support these things.
**Martin Costello** 15:59 Okay. Yeah, I didn't, I haven't actually followed up fully on what, Piotr said at the time, because, yeah, because that comment predates me
joining the project, so I didn't know about that when we discussed it last week.
**Rajkumar Rangaraj** 16:15 So, I'll, this, this one also is pending, like, I did all the research, but did not, because it reads a proper write-up, on what is needed. Probably this one, I'll be…
adding my notes to see if Piotr is convinced to unblock this. If not, we may need to just put this work back on hold.
There is nothing much we could do at this point.
Is the spelling on me, I wasn't here.
I think this is pending on me to merge. I'll try and cover this today, Jack.
Martin, do you know what's going on on this? I know there recently.
**Martin Costello** 17:03 Oh, so I asked them to give us some benchmarks, and then they just invented a benchmark that benchmarked spin once.
so I suggested that they benchmark the code that we're doing, but then I think they still have sort of…
Invented a benchmark.
That just tests the change in, like, the extreme case, rather than…
Seeing the change in the code itself.
Because it could… it could be that… it's like a…
Helps the 1% case, and in the 99% case, you can't tell the difference, which would still be fine, but they've still not given, like, a re… like, a real benchmark of the real code yet.
**Rajkumar Rangaraj** 17:54 Okay.
I don't know, but what…
spending our energy in these kinds of PRs. Like, if you're fine with it, it's fine. If not, we can just pay… block this one. You cannot spend.
**Martin Costello** 18:11 Tomorrow, I'll leave another comment tomorrow and going, like, even if the difference is zero, can you run… can you show us the numbers from, like, real, normal usage, rather than contrived?
benchmark, and then if it's… if it doesn't make much of a difference, or, sorry, if it's basically nothing, then we might as well just take the change anyway. I don't think…
It's, big in terms of co-change, it's just there's no evidence.
Really, either way, that it's better, apart from in the extreme case.
of using the API itself.
**Rajkumar Rangaraj** 18:46 I'm fine with it.
So, I think these two PRs, I think the… the…
customers address the feedback on the last one, I believe. I need to just take a re-look at it. It almost looks… everything is… looks good. Only a few of the world, comments were not addressed when I had taken a look at it last time. So, I just need to take a look at it, re-look at it, and see if it is good.
Martin, I know you've already taken a look, you should be fine with this getting merged.
**Martin Costello** 19:22 Yeah, I don't… I think the only things that's changed since I approved it was it's, like, been rebased, or it's been tweaked for comments from other people, but there's nothing that's been changed on it since that I don't agree with.
**Rajkumar Rangaraj** 19:36 Okay, cool.
This one…
I'm not sure, like, whatever we are doing is, right, just left a… I think you cached that, Martin, like, it changes what's needed here, so…
**Martin Costello** 19:52 Yeah, I… yeah, I put a thumbs up on…
what the con… see, you replied, they replied to you, I thumbs up that what they've said they might do makes sense, but then they've not done anything, and I'm slightly suspicious that it's an LLM.
**Rajkumar Rangaraj** 20:09 Yeah.
**Martin Costello** 20:11 So, if it's an LLM, I'm not gonna… I'm not gonna actively chase it. The person responsible for it can.
**Rajkumar Rangaraj** 20:18 Yep. Makes sense.
That's all from the PR perspective. Let's move on to the issues. Don't think there were any new issues.
That got created.
You spoke about that, the smaller release, patched version of the release. Martin, I think it's time for us to get that done. All the small fixes have been merged.
So if you think, that we should do it, go ahead and release it, I think this is the right time, I believe.
**Martin Costello** 20:55 Okay, I'll revisit that tomorrow morning when I remember.
I know there's at least one bug fix in there.
**Rajkumar Rangaraj** 21:07 There are many, if I recall correctly.
This is one of them, and in the OTLP exporter also, we have something like that.
Oh.
some breaking change, or some… I recall something we did there, or no.
**Martin Costello** 21:38 There's some… actually, there's possibly one more pending change we need before we do a release, but I'll, ping you about that on Slack.
**Rajkumar Rangaraj** 21:48 Sure, that makes sense.
I think that's all we have then, I believe. Nothing much…
There are no other questions, I think we could end the meeting now.
**Martin Costello** 22:04 Thanks, Jimmy.
**Rajkumar Rangaraj** 22:06 Nope.
**Martin Costello** 22:07 Bye.
**Zach Montoya** 22:08 Alright, thanks.
**Matthew Hensley / Grafana Labs** 22:17 Thanks.
