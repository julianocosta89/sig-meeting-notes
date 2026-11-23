SIG: GenAI SIG (APAC)
Date: 2026-11-17
Duration: 30 minutes
============================================================

## Zoom Recording Transcript

**Trask Stalnaker (Microsoft Corporation)** 03:45 Hello!
Can you hear me?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 03:52 Yes, right, cross.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 03:56 Yes.
**Trask Stalnaker (Microsoft Corporation)** 04:14 Hello!
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 04:17 Alright, Traska.
**Trask Stalnaker (Microsoft Corporation)** 04:19 Yeah, I can hear it.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 04:24 was the KubeCon North American going.
**Trask Stalnaker (Microsoft Corporation)** 04:35 Yes.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 04:37 Haha, only, okay.
Hello?
Hello, Traska? Can you…
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:14 Just thinking he's leaving, and then we'll be right back.
**Trask Stalnaker (Microsoft Corporation)** 05:36 Okay, I think I got it working.
Hello.
Hey, Steve. Hey, Huxing.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 05:44 I asked, how has the group come North America going?
**Trask Stalnaker (Microsoft Corporation)** 05:50 Good, good. I just got back this afternoon, well.
I went, not from… directly from KubeCon, but direct… from KubeCon, I went to, California for, a wedding this weekend, and just got back this afternoon, so… Yeah, I have not been home for a while.
Good. But it was good, it was good. hopefully the… videos… They tend to do a good job of getting the videos out.
for those.
So you all can check stuff out that you might find interesting.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 06:37 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 06:40 How about you? How are things going?
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 06:46 Yeah, we… we are doing good. We… we actually… actually, we have a lot of, staff.
To work with our customers, so we're trying to keep the… effort into open source while we are, helping, supporting our customer requirements, yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:11 Let's see what you got on the list today. Roles and boundaries between hotel evaluation result events.
And the evaluation results within an evaluation system.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 07:28 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 07:33 Okay, help me understand…
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 07:38 Yeah, I, I found, yeah, there is a semantic convention event for, evaluation result. And, I also found in some, evaluation, system, they will, produce the evaluation result.
For each, evaluators.
Such as they will, evaluate its traits and produce a result, and the result will store it in their evaluation system.
Yeah, I'm curious, yeah, and in OTEL, yeah, there is an event called, evaluation result, and, what is, different between the, hotel evaluation result with, With, evaluation system. Yeah, maybe, I guess, in their system, maybe they don't use this event to, capture their evaluation result.
**Trask Stalnaker (Microsoft Corporation)** 08:53 Yeah, I'm… I guess… That's a good question, because I'm trying to think of, the libraries that we've… Instrumented to have evaluation That do evaluations.
Hmm. And… I don't think they're tied to a particular system. I could certainly see systems… So, my guess is that it's duplicative, right, like, that… That's kind of a similar thing, where… We're… you know, this is for observability purposes of your… Evaluation result, capturing it somewhere that you can see it.
But… I mean, generally, when you're doing an evaluation, you're gonna want to… Store it.
Somewhere…
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 10:08 Yeah, for example, yeah, in some evaluation system, they will, they will achieve, correlate the evaluation result to the trace.
In these scenarios, yeah, which, are… which result I should use… Original evaluation result produced by system or, evaluation, result event.
Designed by Hotel.
**Trask Stalnaker (Microsoft Corporation)** 10:44 I mean, so this… Event will be tied to your trace, so in your observability system, you'll be able to see that, and it'll be, linked together.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:03 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 11:04 So, I guess that's sort of… Maybe the extent of what we can say as open telemetry but certainly.
You know, if there are… if you're storing, you know, certain things In other systems, you don't have to… capture them here. It just, you know, it wouldn't be sort of… I guess, open telemetry… Blessed, or whatever, if that makes sense.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 11:55 It might help if, like.
**Trask Stalnaker (Microsoft Corporation)** 11:57 Do you have a kind of more practical, Because, I mean, I can ask for other people's… Thoughts tomorrow on the call, if other people have… You know, run into this same kind of issue.
With external evaluation systems.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:20 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 12:20 But maybe if you have a more specific Like, is this an evaluation system that you all, have at Alibaba that you… Like, is integrated into your platform?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 12:36 Yeah, in our, plan for, we, correlate the, evaluation result to the trace.
But, we, designed the evaluation, result structure.
We, we don't use this, event.
So, we, I care also, yeah, I guess in a lot of evaluation systems, or planful, they have their own evaluation result, structure. They want to, They can be used to, provide the, Special, feature for their users.
And, So I… I'm just curious, yeah, in these scenarios, do we need to, capture the, evaluation result event, provided by OTEL or not, or there is any motivation, for hotel evaluation result? Why, why we decide this event?
And, is there… I named, Father, Motivation, we can use that in the future, if we capture this event.
**Trask Stalnaker (Microsoft Corporation)** 14:02 I mean… So, having all of that data in, sort of, a standard hotel format all together has some advantages, potentially. I don't know, like, there was a lot of discussion at the, at KubeCon about trajectories.
And… Producing trajectories from traces.
And… I don't know if… I don't know if evaluations are part of… Trajectories or not.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 14:44 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 14:45 But if they were, you know, that could come over.
I guess I don't know, ed.
Would be… you know, there's nothing that says you… Absolutely have to… record this, so I guess, you know, if your customers don't find this useful, None.
You don't need to… Emit it.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 15:16 Okay, and, yeah, you can, go back to the, yeah, Google Doc, and you can scroll down, and also, see some note, yeah, maybe, written by you or Ludemil, scroll down.
Yeah, scroll down, and, this… yeah, yeah, here, yeah. And, yeah, you can scroll down.
There are some, note about, yeah.
Evaluation… Here.
**Trask Stalnaker (Microsoft Corporation)** 15:51 Yeah, so the open search folk… We're interested in this.
So OpenSearch is, like, a observability backend.
Right, so again, like, if people… for users who are sending all their telemetry to open search.
It's nice to send your evaluation events there, also, because then they can… Correlate stuff for you.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 16:22 Hmm.
Okay, yeah, okay, okay, open source just, observability, backend, instead of, it doesn't include, evaluation, feature.
I, I found that…
**Trask Stalnaker (Microsoft Corporation)** 16:42 Yeah, go ahead.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 16:44 Yeah, I found in some, plan for, like, Lawn Smith or, Dad.org, they also, they both provide, observability, GenAI observability, feature for users and, evaluation feature for users.
so, I… I think maybe in their system, they don't need, yeah, this, evaluation result even. They, they just, correlate the trace to their own evaluation result.
They can provide the, a correlation, of… For sure, sure.
And, yeah, yeah, and also I can, I see there are some notes about, yeah, Copaca North America, and, Yeah, so I'm curious about this point.
And, I also found, yeah, there are some, issues, it's related to evaluation.
event in, in, GenAI, hotel GenAI repository.
**Trask Stalnaker (Microsoft Corporation)** 18:10 Yeah, I mean, so this is for… Right, if you're writing evaluators outside of your observability, like, so you're saying Datadog or, you know, somebody, they will run evaluations for you?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:26 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 18:27 Right, so they don't need a standard format to get it into their backend.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 18:33 Yeah.
**Trask Stalnaker (Microsoft Corporation)** 18:34 So that's different than… Customers writing evaluations, or, Third-party platform that's different from your observability platform.
writing evaluations.
And… At that point, then… the evaluation event.
it has… use case there.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:01 Okay, yeah, you mean, maybe, this, this event is used by customer. They, they, write this event and send it to some, observability backend.
**Trask Stalnaker (Microsoft Corporation)** 19:17 Right, or they use an evaluation library that we emit… that we instrument and emit for them.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:26 Okay, yeah, you… okay, I… I see. Yeah, maybe the users, they can, create some evaluator.
in, offline, produce the evaluation result. Right, or online.
**Trask Stalnaker (Microsoft Corporation)** 19:42 Yeah.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 19:44 Okay, makes sense. Thank you.
**Trask Stalnaker (Microsoft Corporation)** 19:56 Cool. Anything else you wanted to… Check in about?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 20:09 Yeah, and, yeah, Traskar, and, yeah, can you explain more about, different, about, hotel, GenAIsmatic Convention, and, ATIF? And I also, see the note, and, somebody discard this pointer, yeah, with maintainer in, North America. And, I think…
**Trask Stalnaker (Microsoft Corporation)** 20:35 Yeah, I mean, so I don't have a good grasp on this, so I probably wouldn't be able to.
Do any more justice than… Just looking at these issues, I… the plan right now is someone from… at Google is… has proposed Version 2 for these trajectories.
And they're just trying to figure out how we can collaborate between OpenTelemetry and the Trajectories format.
If it's something that… Yeah, basically, how does it… how do they fit together? How do we align them? That sort of thing.
Nothing… has been decided at all. I think the next step is For them to… potentially open an issue. I don't think… I mean, somebody needs to do, sort of, the analysis of Where the gaps are, and… Whether it's something that… We… Want to… Whether the trajectories can be derived just from semantic invention data, or if that's going to be, like, having to emit a whole separate, like, trajectory event with the trajectory data as a special, semantic invention event.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:24 Okay.
**Trask Stalnaker (Microsoft Corporation)** 22:27 Yeah, I would say very early discussion, but at the same time, the person from Google wanted to move pretty quickly, So, we'll see, but not… not a lot to say.
Yet.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 22:44 Okay.
That makes sense.
And, yeah, next question is about, yeah, release of, hotel gene, repository.
And, yeah, if I remember right, and, Ludamine, a long time ago, yeah, I mean, Ludomimila said, the community hoped to release, the RC version.
Before, before the Kuvka. And, yeah, and
**Trask Stalnaker (Microsoft Corporation)** 23:29 Yeah, so obviously we didn't make that date.
Our new… what we shared with people at KubeCon was that… We… I want to be… we want to stabilize it.
by, the KubeCon EU, What Lemil and I have talked about is we were hoping to RC by the end of the year.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 24:00 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 24:01 So… it's kind of… I'm not really sure what to do as far as making a release. I know we have… it's been a long time since we've made a release.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 24:13 Nothing.
**Trask Stalnaker (Microsoft Corporation)** 24:13 At the same time, we have a lot of breaking changes, so, like, we kind of don't want people to be, like.
incrementally taking all these breaking changes, but I… I think we're kind of doing that anyways.
In the Python repo, at least. I… I'm not sure, I… I think some of the stuff we are updating to the latest already.
So, I'm not sure. Are you all, did you have a particular… Use case, or you're just kind of trying to track what the progress is?
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 24:51 Yeah, yeah, in our… In our, in our, instrumentation, all kind of narrow instrumentation, and, yeah, we want to, update the semantic convention version, and I also found that, yeah, there are a lot of updates in, hotel gene repository, and, yeah, if the community can.
yeah, release a new version, and we can, follow the new version, hotel gene isomantic convention. Yeah, this is our initial… Concert.
**Trask Stalnaker (Microsoft Corporation)** 25:35 Yeah, let me, I will add that for a topic for tomorrow.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 25:57 Yeah, maybe, yeah, if a community can release the RC version, or… Something like that, and yeah.
**Trask Stalnaker (Microsoft Corporation)** 26:06 Well, it wouldn't be a, RC, like.
we wouldn't be ready for an RC. That's the… that's kind of the problem, is we're kind of still in a middle state here.
but… I guess it depends on instrumentations.
Our advice for people is to not… is to… not… Make lots of braking changes.
Into the instrumentations, like, kind of wait until things are more stabilized.
Or stabilized.
But…
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 26:42 Hmm.
**Trask Stalnaker (Microsoft Corporation)** 26:42 You all know your users best, so instrumentation would definitely have the… Ability to do whatever they think is best for themselves.
Like, in the Java instrumentation repo, for example.
Right, we have a commitment to not break telemetry.
Outside of a major version bump.
So, we couldn't, sort of, adopt new… we have to flat… put it behind a flag.
to update to the latest semantic conventions, GenAI semantic conventions.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 27:20 Okay.
**Trask Stalnaker (Microsoft Corporation)** 27:25 But I will ask, I'll bring that up as a topic tomorrow.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 27:28 Okay, thank you.
**Trask Stalnaker (Microsoft Corporation)** 27:30 Yeah.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 27:37 Yeah, let's call it early, if we don't have more cars.
Thank you.
**Trask Stalnaker (Microsoft Corporation)** 27:43 Sounds good. Alright.
**Steve Rao (Alibaba Cloud (Singapore) Private LTD)** 27:45 list.
**Trask Stalnaker (Microsoft Corporation)** 27:46 Talk to you.
Bye.
**Huxing Zhang (Alibaba Cloud (Singapore) Private LTD)** 27:48 Bye-bye.
