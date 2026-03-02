SIG: System Sem Conv Stability WG
Date: 2025-09-04
Duration: 31 minutes
Zoom Recording URL: https://zoom.us/rec/share/Rgk_Fh50_4HSVMmMo4xTtPwtZzABwCYo_8hfOxwJ0MEzEghXshipfe_HfmqKoEuH.n5gVSsZpfmlwFCq9
============================================================

## Zoom Recording Transcript

**Pablo Baeyens** 00:18 Hey!
**Dmitrii Anoshin** 00:22 Hi, Pablo.
**Christos Markou** 00:31 Hey, folks.
**Dmitrii Anoshin** 00:35 Hi, Christos.
Crystal, do you want to start with your item?
**Christos Markou** 02:18 Yeah, we can start discussing this. Yeah, let's discuss this first, and then, we can have the rest of the time discussing the stability topic that Pablo mentioned.
Yeah, I just wanted to, raise this issue as well, because it also affects the, Kubernetes Working Group. So…
We have already been using this modeling to introduce some Kubernetes-related metrics.
And, yeah, right now we're trying to add some extra ones, and we're blocked because I would like to first ensure that we are, aligned with the guidelines.
So… yeah, I don't know how we can beta… how we can proceed with this one.
I know that Bridon commented on the… on the PR that, he's gonna work on this again, soon. My question is mainly, because the…
The suggestion of this, guidance is that,
We… we should use, status, for example,
status for the metric name, and .state for the attribute, but for some use cases, like in Kubernetes, where… where you have extra… extra things like phases or whatever,
We should have… an attribute called KH.phase.
This is what I see in the PR. So, the attribute is k.phase, and the metric name is k.face.current.
So, my first question is, is this allowed in some ad conventions, to have a metric called kh.phase.current with an attribute kH.phase?
**Josh Suereth** 04:23 So, the metric would be named kates.phase.current, and the attribute would be kits.phase?
**Christos Markou** 04:29 Yeah, that's what the PR suggests.
**Josh Suereth** 04:33 Yeah, we're inconsistent with our attribute versus metric naming thing right now.
In that we haven't, like, finished out our, guidance.
So, technically, you're not violating anything in SEMCOM yet.
Whether or not somebody feels like that's a bad design… how do I want to phrase it? There's a door that we haven't opened to allow it.
But we're not explicitly saying no.
We're just not sure if we want to open the door or not.
So, I think you're, like, the 12th person that wants to open this door for a variety of reasons. So we might just open it up and say, you know what, what we're trying to do with metric namespacing is out. Like, we're done.
but right now, we don't explicitly disallow it.
That's all… that's all I can say. If you want the rationale behind, attributes and metrics, the rationale is, if I have an attribute.
And, that attribute is used in a log, like a log event.
And I want, like, a collector processor.
That just generically says, cool, take events with this name.
take this attribute and give me a metric with it. We want to make sure that that's possible and easy to do in OpenTelemetry.
Whether or not we enforce that it's never broken or never violates SEMCOMF is the door we're not sure if we're going to open or not. Does that make sense?
I don't think that applies to you here at all.
You're actually reporting a state metric.
**Christos Markou** 06:13 Yep.
**Josh Suereth** 06:14 Of the current phase. So, I… If you want, if you want to make that change, I'd be happy to kind of talk through that and…
On the, on the PR and approve it if I, I need to look through the details more in depth, sorry. But yeah, I'd be… I'd be happy to move forward with that, because I don't think you'd be violating that
part of SEMCOF, right? The… this thing where… anyway.
**Christos Markou** 06:42 Yeah, so the option… what we have been using so far is, most of the cases, we were defining those using the same name, both for the attribute, but also for the metric name.
But this might be… some people have raised concerns about this, yeah, and specifically Tyler, because in OTTL, you have this concept of flattening fields, so this might be problematic.
So one option is this, the second option is what Brydon suggests, if it is allowed, and then probably third option is to just find different names, but in Kubernetes metrics specifically, we have already long metrics, like kh.pod.phase.
So, you would need an extra suffix to say current, and then dot something else for the attribute. So, it would become ugly, I guess.
**Dmitrii Anoshin** 07:38 By the way, why do we have something else? Can we have the same metric as the attribute name? I believe we already have it in different places.
In comparison, specifically.
**Christos Markou** 07:51 I mean, that's…
**Josh Suereth** 07:52 In my opinion, that's as designed. Like, we should allow an attribute to become a metric name.
That's… that's by design. That's this whole, I have a bunch of events with attributes on them, and I want to turn them into a metric.
why am I changing the name of the attribute that I'm turning into a metric, you know?
**Braydon Kains** 08:09 Well, I think this is about, like, whether a metric can have an attribute with the same name on it.
I think that's what we're talking about.
**Josh Suereth** 08:17 Oh, like, the metric name and the attribute are the same.
**Dmitrii Anoshin** 08:21 Yeah.
**Josh Suereth** 08:22 Gotcha.
**Braydon Kains** 08:25 that… that was one of the things blocking the status guidance. I also need to, like, rewrite it a little bit, because, like, the way I wrote it sort of made it seem like I was trying to enforce the specific words that we used to describe it, and that was… it was just an attempt to
like, suggestion to remove that conflict of the attribute name being the same as the metric name, because I thought that was, like, a hard restriction, and then it turns out it wasn't, but, like, it… there's reasons it's not good, and so…
we need to, like, decide that, so I can do the rest of this.
**Christos Markou** 08:58 Where do we use it already, Dmitry? I mean, Do you mean the…
Already defined semantic conventions, or somewhere in the implementation?
**Dmitrii Anoshin** 09:07 Yeah, I sold.
**Braydon Kains** 09:08 There's a few examples. I think they're posted in some comment in the status guidance PR.
**Christos Markou** 09:15 Yeah, but those are fresh, I mean, those are new, it's not something that…
**Dmitrii Anoshin** 09:20 from you.
**Christos Markou** 09:21 Yeah, we would need to change them anyways, I mean…
**Braydon Kains** 09:24 Oh, you mean, like, are there any implemented?
I didn't think there were any implemented, because, like, the… this the…
**Christos Markou** 09:30 They are only.
**Braydon Kains** 09:31 Shimplement.
**Christos Markou** 09:31 The container status was defined recently, like, months ago, 4 months, 3 months ago, and then it was also implemented in the collector.
**Braydon Kains** 09:39 Oh, okay.
**Dmitrii Anoshin** 09:40 But why we have to change that? That's what I'm asking. Which problems are we running into?
**Christos Markou** 09:47 I'm not saying… I mean…
I'm not advocating for changing them, but it seems that people want… want them to change. That's…
So, I'm trying to find consensus here.
**Dmitrii Anoshin** 10:01 I can…
**Braydon Kains** 10:03 I can find the issue where Tyler explains the problem that he has with it.
**Dmitrii Anoshin** 10:07 Oh, okay. I see.
So you're referring to Tyler's comments, right, essentially?
**Christos Markou** 10:14 Yep.
**Dmitrii Anoshin** 10:14 Okay.
That's what you mean.
**Christos Markou** 10:17 It's actually on the PR, on Brighton's PR, what Tyler…
Yeah. Describes. So, some of the guidance PR.
**Braydon Kains** 10:26 I have an issue open specifically about the,
The metric being the same name as the attribute, or whatever you want to call it.
I think that's an issue comment link, but I wasn't trying to link to that one, I was just trying to link to the issue.
**Christos Markou** 10:53 Yeah, sharing. Okay, okay.
**Dmitrii Anoshin** 10:56 Yeah, we, like, we introduce some guidance, and then we run into issues with some guidance. If we never had this requirement for attributes to be, like, uniformly unique, long attributes within a metric name, it wouldn't be a problem.
**Christos Markou** 11:20 Yeah. I, I agree.
Okay, let's,
comment back on the issue, anyone that has something to add there. It would be nice to have this, like, moved forward, because it will unblock. And also, if we decide, like, changing the…
the modeling that we used so far, we will also need to go back and change the metrics that we have introduced already. Most of them are not implemented yet, but I think there are two container-related metrics that are implemented.
Wow. So, yeah.
**Dmitrii Anoshin** 11:56 Brighton, you posted a link to a comment from Thompson Tomo, is that what you wanted?
**Braydon Kains** 12:02 No, that… I… I included that in the link by accident. I only meant to link to the… to the issue.
**Dmitrii Anoshin** 12:08 They should sell, okay.
**Josh Suereth** 12:10 So, okay, I'm rereading Tyler's concerns here, and I honestly think it's tied to how Honeycomb works. So, that doesn't make me super happy, but, like.
If you want a flat no TLP,
And give the metric a dot value or something. Like, the value of these metrics is gonna be frickin' 1 all the time. The value's meaningless, the name of the attribute's important.
I…
I would push back. I think it's okay for you to push back a little, Christos. Like, I understand what he's saying about flattening, but we can say, look.
you can still flatten, there's other ways to flatten that isn't just naively saying metric name equals this value. You could say metric name dot value or something, or metric name.metric value, if you want to flatten it into, like, a pure JSON structure. But more importantly.
Is that open telemetry?
Right? We have an open telemetry data model, that's what we're enforcing here.
Do I want the OpenTelemetry data model to be something you can flatten? Absolutely.
But…
like, it doesn't mean we have to be naive with how we do it. So I think there are ways to solve some of those concerns, if you wanted to keep metric name and metric attribute the same.
Because…
The metric name and metric attribute being the same, are you getting pushback from semantic convention approvers on that?
**Dmitrii Anoshin** 13:34 I mean, it would be good if we can get pushback from GC or TC as well, in that case, because, yeah, I agree, it's, like, we are… we cannot…
Please, any, any vendors with, the decision we can make.
**Josh Suereth** 13:50 Yeah, I guess what I'm saying is the… I understand his concern, and I think we should be flattenable.
But…
the… like, saying we have to be naively flattenable is different than saying, hey, maybe we should have a proposal around how to flatten data in OTLP, right?
**Dmitrii Anoshin** 14:07 Makes sense.
**Josh Suereth** 14:08 Yeah.
**Christos Markou** 14:08 So the argument here is that if we only need to do this to cover the flatten, use case, probably that's not a strong argument for having this, right?
**Josh Suereth** 14:19 That's my opinion, unless the… is the flatten actually something that OTTL does to a metric data point?
**Christos Markou** 14:29 Yeah, not sure, to be honest.
**Josh Suereth** 14:36 The last time I worked on the Flatten in O2L, at least a year ago, when I re-implemented it, Flatten only did, it only does attributes, it doesn't actually flatten metric names back then. So I don't know if it's changed, but…
The one that I'm familiar with was, just, just grabs attributes and the key-value pairs within attributes.
**Christos Markou** 15:02 Okay, Brydon, since you originally proposed this guideline, and you went for having different, names, how… any… anything to add here? I'm just trying to collect all opinions and try to, summarize this.
**Braydon Kains** 15:19 most of what I wrote basically assumed that this wasn't allowed, and, like, it wasn't… it wasn't assumed because of anything anyone told me. It was just, like, a…
It seemed logical to me that you wouldn't want it.
Because it just feels weird for usability, but it is not based on anything anyone has ever said before, and I didn't know there existed already things that did this metric name being the same as an attribute.
So, like, if… if we… if it turns out that that's not the case, like, I'm not… I don't actually care that much.
I think it's weird, because, like, if I was in, like, a query scenario, like, on a query UI, and an attribute had the same name as the metric itself, I would be very confused. But that is my only opinion.
It's very loosely held.
Especially for something like Status, where, like.
The value is going to be 1, which is a bit awkward, and then…
the status attribute has a string. So, like, if I… if I don't really know what I'm looking at in a, like, time series data query scenario, and I have, like, the attribute and the metric name being the same, like, in a PromQL query, I think it would be weird.
**Dmitrii Anoshin** 16:38 I think in general, those metrics are weird, and they are not… shouldn't be something that we recommend by default. They should be just a replacement for…
know, like, Cube, or KubeStack, whatever, and for those backends that don't support the entities, because that data is supposed to be sent to the entities, I believe.
**Josh Suereth** 17:01 Yeah, do you… the other thing I was thinking about, do you normally join on those labels in the metrics? Because I don't, like, to your point, Braden, about does it show up in a query, I don't think it does. I think it shows up in the results, so you get a time series back with a state, right? And you'll see, like…
this label equals this value, but I don't know… I don't know if people are going to be joining on it, generally.
**Braydon Kains** 17:22 Process, in process, you might.
**Josh Suereth** 17:26 Process might be different, that's fair, yeah.
**Braydon Kains** 17:28 Yeah, because on one system, you might want to know all of your processes and
An active state, or zombie state, or whatever.
That's… that's… that's the… that's the… that's the… where my brain goes when I think of the… because that's… that was the initial target for the guidance, was… was process status.
And the idea of, like, you want to count how many zombie processes you have on your system, I think it would show up in the query that way.
**Dmitrii Anoshin** 17:56 And what's the problem if we use the same attribute with that?
**Braydon Kains** 18:00 The query, I mean, I'm not a PromQL expert, but the query would look something like process status, where process.status equals zombie, or something like that. Like, the process.status would appear twice in the query.
**Dmitrii Anoshin** 18:12 Yeah, yeah, yeah.
**Braydon Kains** 18:13 If you don't understand what you're looking at, then it would be… it might be confusing.
**Dmitrii Anoshin** 18:18 I mean… I understand the confusion, and maybe ergonomics not being the best.
But there are no, like, significant blockers from the user perspective, right?
**Braydon Kains** 18:32 It's not a blocker, no, no. Like, the reason why… I'm sort of just justifying why that was what I thought. That's the way I thought it worked.
**Dmitrii Anoshin** 18:42 But if you have it, like, if you would need to change the attribute name, to make it…
like, artificially different? Wouldn't that be easy?
I… I'm not sure about that.
**Braydon Kains** 18:56 I think in the specific process status case, having process.status, and then state being the name of the state itself is pretty logical.
And regardless of where we land on this, I probably will end up suggesting that for the process status one specifically. But when it comes to Cates, where the verbiage is different, then it might not make sense.
**Dmitrii Anoshin** 19:20 You mean process status would be the metric and process state would be the attribute?
**Braydon Kains** 19:25 Yes.
**Dmitrii Anoshin** 19:26 Okay.
Which is still… kind of…
**Braydon Kains** 19:32 It's still… it's still weird. It's just the fact that the name's not identical.
**Dmitrii Anoshin** 19:38 Yeah, it still feels, like, artificially different for the reason of being different.
**Christos Markou** 19:45 Yep.
**Braydon Kains** 19:46 Yeah, there's still, like, there is an English language justification for it, and it's in the PR, where I sort of…
Go over, like, what… the difference in definition or usage between status and state, in terms of, like…
Past tense, present, whatever, but…
But yes, it's true, it is a matter of, like, de-conflicting for the sake of deconflicting.
**Christos Markou** 20:08 Yeah, and also we need to keep in mind that, probably for status and state might be more straightforward, but then we have phase, we have other things, like status region, so.
**Braydon Kains** 20:19 For Cates, it probably is not quite as easy as the process version.
**Dmitrii Anoshin** 20:23 Yeah, and in that case, like, when you work with those metrics, you have different of them, you would need to figure out what was this test… what this… that particular attribute name is.
**Braydon Kains** 20:36 But if we keep it the same.
**Dmitrii Anoshin** 20:38 Even if from ergonomics it's not very convenient, but it'll be probably easier to understand and easier to work with, having people
Like, know that it's gonna… it's gonna be the same, so they would always, like, for the new state-like metric, they would just use the same attribute and assume that that's gonna work.
**Braydon Kains** 21:00 Yeah.
I do have more I want to talk about this with, but while we have Josh, I feel like we should move on to the stability topic.
**Christos Markou** 21:08 Yeah, yeah, let's take it offline. Thanks, folks.
**Pablo Baeyens** 21:16 Right, so… I guess… To get your shot to speed.
What we talked about last time was,
We could focus on stabilizing the process namespace first, since that seems to be the one that has the fewest pending issues, and you can see the ones that we consider
Depending on that, project view.
Mmm…
And so, yeah, I think… Christus, you wanted to talk about also, like, about what…
What we are missing, or what we have… we could do different, compared to what we've been doing so far to make sure that we can… we can achieve, stability.
I don't know if you have concrete thoughts about that?
**Christos Markou** 22:20 Yeah, I'm not sure if I have anything concrete to suggest, but, the reason I, reached out to Pablo once more, talking about stability, is that,
it's been quite long that we have been discussing about this, and I have seen, both internally, but also from users, that delaying
Not necessarily for a bad reason, but in general, delaying stability, brings some mistrust, for the project.
And I was wondering,
yeah, how we can move towards this, but yeah, actually committing to this and trying to actually achieve this.
I know it's not that easy, there are reasons for delaying, but on the other side, I was wondering how… if we can find a way, or what we could change, actually, or suggestions from maintainers, or any, I don't know.
different approach that we should take, or if it is just, like, that we're missing
people working on this. Yeah, we can also state this, and that's fine.
**Pablo Baeyens** 23:38 Okay.
I can… I can give my thoughts, and then I guess I'm interested in Josh's take. I think we do…
we would have benefited from more people, or from people that could commit more time, like, I… I don't know, speaking for myself, I haven't been able to commit that much time for
for this sig, and I think if I had, we probably would have been able to
to move faster. But then the other main thing I see, maybe it's…
It's difficult to go for stability while also… Responding to…
You know, enhancements, or new namespaces, or new features that,
you know, people proposed, and that fell under the scope of RC. And I don't know if there's something we could do there on, like, yeah, just… we want
answer to those until we have stability or what, but yeah, that does seem to me like one of the…
The things that is slowing us down.
That we have this dual role.
Dimitri?
**Dmitrii Anoshin** 24:55 Yeah, I want to add something. I completely agree with you, Pablo, but I'm wondering if there can be, like, some solution in a way that people that are coming to OpenTelemetry with issues of adding something new.
Instead of just committing to whatever they ask by ourselves, we try to have them engaged.
And get more contributors by that. So instead of, like, trying to resolve the area issue, we say, hey, go and join the SICK meetings from system, and help us with stabilization. And this can be one of your priorities.
Well, what do you feel about that? It can be just, like.
Like, the way we try to respond
to those people in general, not, like, something, like, concrete, but, like.
**Braydon Kains** 25:52 Moving towards that kind of responses.
**Pablo Baeyens** 25:57 Hmm.
I mean, that makes sense to me.
I guess, do you agree, Bradon, about the, like…
Scope Creek, for the lack of a better name.
**Braydon Kains** 26:09 Yeah, I think…
I think the scope creep is one thing. I… I think a lot of my… a lot of my issues with, like.
how we move towards stabilization are, like, personal hang-ups, where I… I don't feel… confident making…
Like, a lot of, like, technical decisions about stabilization, because what tends to happen is
like, we'll come up with something, we'll put it together, and then someone who knows, like, a lot about some specific niche will come barreling in about, like, why it's a terrible idea to do it that way. And now, just the fear of that happening all the time has made me just not want to work on semantic conventions at all.
And I… I know that has probably been part of
hindering the progress, because initially, when the SIG formed, I did a… I was doing a lot of work at first, and then that started to slow down, and it…
Partially it's a personal thing, partially it's just things…
increasing at work itself, but I think that's… my biggest problem is not really with specifically the way we're doing anything, but just the way that semantic conventions work has, like, shaken out.
I know we only have a minute left, but Josh, if you have anything to add.
**Josh Suereth** 27:23 Yeah, so…
there's two things to think about here. One is, I would encourage, I think we are,
When it comes to stabilization in OpenTelemetry, we have a lot of FOMO.
A new thing comes in, and we want to support it, and we already committed to something, what are we going to do? We have to get past that and find a way, because we're never going to be perfect.
So, we have to find a way to stabilize what we have and say, this provides a good level of observability and adaptive feature requests as we go, which means we will have to find ways to do that compatibly. The entire effort that, like, we started around semantic convention tooling is to give you all the capability to evolve.
and do so safely, and bring the ecosystem with it. That tooling is… I mean, it's still nascent. We're still, like…
we have the ability to diff between versions, right? We don't have the ability to automatically migrate users between versions, but we're trying to get there and give you the capabilities to have more aggressive evolution. But in the meantime, just do what you would do anyway for users, right?
With metrics, make a new metric that's the version 2, when you need it.
Right?
With spans and events, just add new attributes freely, but never remove the old ones that people might depend on.
That kind of stuff we're trying to allow, so that you can pick a scope of, this provides good observability, and we can commit to it and stabilize it, right? If you have a core that you feel is at that state, where it's stable enough that we can build on it for the next 5 years.
let's commit to that if possible. So, my thinking is, if you want to stabilize process.
Get your baseline entity Sort it out. So, the identifying attributes. Descriptive attributes you can add later.
You're not sure if you want command line args? Great. Leave that unstable.
But stabilize the core identity piece, right? Take the metrics you care about and process. We need to figure out how to do, open file descriptors. Great, don't stabilize that metric yet. Stabilize the ones that you can. But you can go incremental here. That's the goal, is that we need incremental, and we need evolution.
And if you don't have the capabilities from semantic convention tooling for that.
bring that to the SIG. Like, we… I don't want you to feel like you have to lock down and you're stuck. That is absolutely not gonna be… that's not gonna work. That's gonna be the failure of the whole semantic invention process, right? So, my recommendation would be pick a tight scope.
stabilize it, and it's okay to then add on metrics and logs and spans later. So if you wanted to pick, like, the key set of process metrics you think absolutely need to be stabilized for the host metric receiver.
Great, put those there. Put everything else behind flags, or if they're… if they have to enable a feature to turn it on.
Great, you can do that without having it be in Simcov, right? But the key set of features that you want to give people is, like, here's a process experience for observability.
let's try to stabilize that as quickly as we can, and let's take some of the shenanigans and, like, extraneous stuff, and figure out how to adapt it into that core experience as, like, an add-on, or something we can provide later. That would be my recommendation.
Our ability to give you the capability to do that, that's on me, and I don't feel like we've given you great tools, but we're working on it as fast as we can. We also only have about 3 or 4 of us active, so that's also part of the problem.
Anyway, that's my thoughts. I gotta jump over to the entities group, but, happy to help, and I think I can attend next week,
No, you guys meet every other week, don't you?
**Braydon Kains** 31:12 We mail it every week.
**Josh Suereth** 31:14 Yeah, it looks like I'm free, so I'll join next week if we want to continue the discussion, too, or I can follow up offline, too, like, on chat, so…
**Christos Markou** 31:22 Cool. Sounds good.
**Braydon Kains** 31:24 Thanks.
**Christos Markou** 31:25 See ya, folks. Bye.
**Pablo Baeyens** 31:27 Yep.
