SIG: GenAI SIG (APAC)
Date: 2026-08-04
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 00:32 Yeah.
Hi, Traska.
**Trask Stalnaker (Microsoft Corporation)** 00:35 Hey, Steve. Hey, Liu.
**Liu Ziming (Abalia)** 00:39 Hey, Trask.
**Trask Stalnaker (Microsoft Corporation)** 00:39 Good evening to you.
Let's see what we have here… oh yes, yes, let's move… We'll make a break here… I'm not sure the way we're managing these I'm… Same… Day, but different meeting notes as… Quite right, but we will continue.
Alright, zooming… do… I… Yeah.
**Liu Ziming (Abalia)** 01:57 I have to laugh, issue on the GitHub, and previously, I think Steve had raised a similar issue. It is about the server-side semantic conventions, and, Previously, our work probably focus mainly on the client-side agent observability, but recently we have noticed that the influence engine side observability is gaining increasing attention from our users. The framework-like VLM and SGLAN have actually already… integrated open telemetry tracing capabilities, but, I think there… there are no, semantic conventions in our community, and some, some attributes in VRM and SJLAN are just, the de facto, de facto semantic conventions in the, inference engine, I think. Something like, the GenAI, GenAI… Oh, I can't sh… We'll have a look.
**Trask Stalnaker (Microsoft Corporation)** 03:30 Oh, these ones.
**Liu Ziming (Abalia)** 03:33 Yeah, the GenA latency, yeah, the GenA latency…
**Trask Stalnaker (Microsoft Corporation)** 03:35 Aha.
**Liu Ziming (Abalia)** 03:37 related attributes. We have not defined the… But actually, they are… they are the de facto semantic conventions in the server-side influence engine, and they use the same… common attributes.
To show the important latency, latency, attributes in the engine. So, maybe we can consider to start with the latency attributes in the… inference server.
**Trask Stalnaker (Microsoft Corporation)** 04:21 Cool, yeah, a couple questions. Are… These, emitting span data, or metrics, or both?
**Liu Ziming (Abalia)** 04:37 Currently, they do not use open telemetry metrics in their code. They use promos, and these attributes are only recorded, I think, in the span, in span.
**Trask Stalnaker (Microsoft Corporation)** 04:57 Okay, so they are… they are emitting both spans and metrics, but the metrics are going… out over Prometheus.
**Liu Ziming (Abalia)** 05:06 I don't think… oh, yeah, yeah, yeah, yeah, yeah.
But, the merchant name may be different.
Metric's name may be different.
Okay, no, I'm…
**Trask Stalnaker (Microsoft Corporation)** 05:20 I'm just trying to understand big picture first, since I'm not familiar with these.
Are these… Are these services?
Or are they things that people run themselves?
I'm wondering, because… services… It's… can be challenging, like, how do… where do they export the data… how do they export the data to the users?
**Liu Ziming (Abalia)** 05:53 They are actually… users may deploy this, inference service themselves, or they will use the service provided by the cloud providers.
both… Possible. And, usually they configure an OTLP endpoint and send the span to the endpoint to… To check the spin.
**Trask Stalnaker (Microsoft Corporation)** 06:30 Do you all at Alibaba… does Alibaba, have a managed service for these?
**Liu Ziming (Abalia)** 06:42 Yes, yes, we have managed service.
And the user can also buy some, by something, like.
Elastic Compute Service and deploy the VLM or SGLAN code by themselves.
It is, it is open-sourced, and I think so many users may deploy this service themselves, deploy their models on this inference service.
**Trask Stalnaker (Microsoft Corporation)** 07:17 Cool, yeah, I know that, I mean, server-side… Telemetry has come up.
Before, and we've sort of just said at… Focused priority on client side.
But… It was… probably, you know, I think it's good to revisit that, see if… There are more folks… Interested, you know, and ready to start Working on server side… telemetry. Yeah.
**Liu Ziming (Abalia)** 08:01 Yeah.
I think VLM and SGLAN framework have… have so many contributors, and it's the most popular inference framework in the GenAI field.
And, we think if we make some semantic conventions for, the influence server, I think there will be so many contributors, Follow our semantic commissions and to make most of the attributes the same, and our users can easily understood what they are recording.
**Liudmila Molkova** 08:48 I have maybe, controversial thoughts on this.
that… Vlm.
De facto created semantic conventions for themselves, and they're following them.
And they're in absolutely best position to evolve those further. It's kind of unfortunate that they are not based on ours, and we don't collaborate enough.
But I think the natural place to evolve this.
is VLLM, but we probably need somebody in between who would maybe bring things VLLM has, and… we would work together. We're… like, they probably don't even need formal semantic conventions to start following a better scheme. So if you just come and contribute to VLLM, they might be… They might just take it, and it becomes de facto standard.
**Liu Ziming (Abalia)** 09:46 I think there are… the GenAI latency-related attributes is the de facto standard, but we have not defined the semantic conventions in our repo.
So, I think we can start with this de facto… de facto semantic conventions. And, once we have the server-side semantic conventions, they will be, I think there will be more and more VRM contributors to, contribute to our Semitic conventions.
And, mmm… yeah.
make the VM, follow our semantic conventions.
**Liudmila Molkova** 10:38 I… when I say, I don't think we have to define conventions in this repo. It would be nice if it was a natural… Like, place of gravity for server people to work in, but… We currently aren't.
And if VLLM what… Come and say, okay, we're donating this.
I'm looking at these metrics, and we would probably name them differently. We would do a lot of things differently.
We… I would feel very conflicted about taking it as is.
Like, without… Immediate desire to change it.
**Liu Ziming (Abalia)** 11:26 we just want the other, influencer, like Estron, to follow the VRM. If we do not do… do something like that, the… the SLAN and VM may be very different in their, open telemetry span, I think.
**Trask Stalnaker (Microsoft Corporation)** 11:54 Yeah, so… I… I definitely agree, that, you know, I don't think it's… What I… what I would see as the first step to us going into server-side telemetry Would be just the very basics.
That would apply, you know, that would be, like, a server span and a server duration metric.
and… you know, more… Detailed things, you know, we would… Need to understand If they are… Broad across all of these servers, or if it's something that's, you know, server-dependent.
You know, I mean, most of these look fairly reasonable as far as probably would apply to other inference servers, but… you know, I think we would… we need to phase it out, and I think the first step, if we are going to go into server telemetry, would be just defining the span and the duration metric, you know, start simple there.
And we… I don't think that we would… You know, give… we don't generally give much weight to, Well, we give the most weight to being… Following our conventional naming.
So, you know, it is, you know.
This doesn't look like something… these names don't look like something we would do, so, you know, just from an expectation perspective, if we do go down this path, I would expect these to change.
But I think that's okay, right? Like, that's kind of the point of, you know, hey, BLLM did a great job of, you know, putting something out, and we can learn from their experience, and then, conform it to our conventions.
And then, you know, when they are ready, they can pick up those changes.
**Liu Ziming (Abalia)** 14:33 Okay, okay.
So…
**Liudmila Molkova** 14:35 We do, by the way, have the server latency, which is don't have a server span.
Somebody who works on Kubernetes, who works on VLLM, contributed the server latency, like, a couple of years ago. We always forget about it, because it's… yeah.
**Liu Ziming (Abalia)** 14:57 Okay, maybe we should contribute to VM first.
**Liudmila Molkova** 15:06 I think what Trask is suggesting to define a span.
And to review if the server metrics align with what you want them to be.
could… are reasonable. I think we… we are already in the spot where we have some server side.
And I, I would review the, the inference server Span the basic one, happily.
But, like, I think, yeah, I would… love to do this project if people from VLLM are interested, and if they would… follow the conventions we define with whatever timeline. They don't have to follow them in the near term with a lot of, like, churn that will be happening.
But, like, if VLLM people are interested in contributing to open telemetry, evolving it, and eventually using Open Telemetry, that would be amazing.
And if they want to work on their own thing, it would be amazing to have somebody who can, like.
Unify and maybe suggest some naming patterns that we have for shared things, for them to use.
**Liu Ziming (Abalia)** 16:29 Okay, I understood.
Cool.
And…
**Liudmila Molkova** 16:42 I think there is even an SDK, like the Hugging Fate Transformers, is it for the inference servers?
**Liu Ziming (Abalia)** 16:52 Yes.
**Liudmila Molkova** 16:53 can, like…
**Liu Ziming (Abalia)** 16:55 the inference server-like VM used the Hugging Face Transformer as its transformer implementation.
And it is part of the reference server, I think.
**Liudmila Molkova** 17:09 It just allows us to relatively easily create reference scenarios, right? You know, we have reference scenarios here.
And since there is the… one of the implementations of the… server-side serving SDK, we could, just use it as the example of how you would instrument. It's not that we actually need to instrument it, it's more like we have a reference scenario.
**Liu Ziming (Abalia)** 17:43 Yeah, okay.
**Trask Stalnaker (Microsoft Corporation)** 17:55 Cool. Anything else you wanted to discuss about this proposal?
**Liu Ziming (Abalia)** 18:02 No, no, no, not yet.
Cool.
**Trask Stalnaker (Microsoft Corporation)** 18:12 Alright, Steve.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:19 Yeah, I create an issue.
And yeah, maybe, yeah, Liu are familiar with this context, and I create a PR.
And, I saw some comments from you.
**Liudmila Molkova** 18:41 Yeah, let me see, I… probably something minor.
I don't remember. Oh, you addressed everything.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:48 Yeah.
**Liudmila Molkova** 18:48 Okay.
Then it should be… let me take a look.
**Trask Stalnaker (Microsoft Corporation)** 19:08 Yeah, I can look at it also for a second.
Approval.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:15 Thank you.
**Trask Stalnaker (Microsoft Corporation)** 19:24 Cool, anything else?
We should chat about?
While we're here?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:32 Nope.
**Trask Stalnaker (Microsoft Corporation)** 19:33 In case you'd… Didn't see, we are… moving forward with the… that conformance testing repo, I think Huxin had asked about that, Related to the blog post.
So I think I'm going to actually get the, I think I've got maintainers and everything lined up now, and so going to get the repo, created.
today or tomorrow, and, figure out how we're… if we want to bootstrap it with everything, or how we want to discuss it with the maintainers, but, I would expect to see us move Forward, hopefully quickly on this now, that we've got kind of a… Plan.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:29 Okay, thank you. Yeah, Hu Xing, he has something he can join us today, yeah.
**Liudmila Molkova** 20:39 Yeah, Trask, I'm curious, do we need a meeting for this? Can we… use one of the existing ones, maybe semantic conventions, or tooling, or Ecosystem Explorer.
**Trask Stalnaker (Microsoft Corporation)** 20:54 Yeah, yeah, I don't want to create a new SIG for it, and a new meeting. I think that, yeah, I was thinking we would use the semantic convention meeting.
Since most of us are there anyways, if there's topics.
**Liudmila Molkova** 21:15 Yeah.
Yeah, that's great, yeah.
**Trask Stalnaker (Microsoft Corporation)** 21:19 And then, yeah, we can do a lot of, a lot of that async and or… Yeah.
**Liu Ziming (Abalia)** 21:29 Yeah, and the last scene, that's, That the other people know that we have changed the meeting room address?
I have… Noticed that today, until today.
**Trask Stalnaker (Microsoft Corporation)** 21:48 Oh…
**Liu Ziming (Abalia)** 21:49 Because I have went to the old meeting.
**Trask Stalnaker (Microsoft Corporation)** 21:52 Yeah!
Okay, I'm glad you found it, found us, yeah, I… I think… Ted had… migrated this meeting, and I think he posted in the… Slack channel about it.
But I know it's easy to, miss… things.
**Liu Ziming (Abalia)** 22:23 Okay, okay.
**Trask Stalnaker (Microsoft Corporation)** 22:25 Yeah, if you see anybody else who missed it, put them this way. Thanks.
**Liu Ziming (Abalia)** 22:32 Okay.
Yeah, thanks.
**Liudmila Molkova** 22:34 So what happens to me, I have duplicated this meeting to one of my calendars, and there, it got… I have the old link, so I need to… Update all of my duplicates to apply into the new place, so maybe it's the same problem for other people.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:51 Hmm, there you go.
**Trask Stalnaker (Microsoft Corporation)** 22:53 Yeah… Cool. Well, good to see you.
**Liu Ziming (Abalia)** 22:59 Yeah, good stuff.
**Liudmila Molkova** 23:00 To see y'all.
**Trask Stalnaker (Microsoft Corporation)** 23:02 Bye.
**Liu Ziming (Abalia)** 23:02 Bye.
