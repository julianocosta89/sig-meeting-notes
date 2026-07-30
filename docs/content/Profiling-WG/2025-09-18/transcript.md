SIG: Profiling WG
Date: 2025-09-18
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Frederic Branczyk 00:01:46 Hello, hello.
Fabrizio Ferri Benedetti 00:01:51 Good day, everyone.
Felix Geisendörfer 00:05:14 Volunteers, or somebody wants to do the moderation?
If not, I just lost the game of chicken, I guess.
Alright.
Hello, and welcome, everybody!
to our bi-weekly Profiling Sikh meeting. As usual, everybody probably already has some meeting notes open.
And we will go through the agenda, and I think the first one is to always go through the active action items.
So… Guess I can share my screen.
Let's close some other stuff real quick.
Here we go.
So, previous action items.
Alex say, write a profiling signal protoconsistency check tool. Any updates on that?
Alexey A 00:06:33 No updates over the last… two weeks, but this is in progress. I will try to send a pull request before the next meeting.
I have kind of, like, the scaffolding done, but just need to… Need to add all checks, and… yeah.
Felix Geisendörfer 00:06:54 Okay.
Frederic Branczyk 00:06:54 By the way, I did, I did just update, the validation code in Parker as well, As of, like, what's it, one dot date.
Alexey A 00:07:06 Okay. Yeah, I've been using that, I've… One of my… one of my windows had the broadcast code, so I'm… I'm definitely peeking into that.
Frederic Branczyk 00:07:16 Okay, I'm just saying, I think yesterday I updated it to the latest version.
Alexey A 00:07:21 Okay.
Felix Geisendörfer 00:07:23 Cool.
Awesome, then… We can go to the next one, PProf Hotel Converter, is that… The discussion we had last time…
Alexey A 00:07:39 Yes, yes, I added it to myself. I haven't started working on it, but it's on my list.
Felix Geisendörfer 00:07:47 Well, thanks for taking that, but I think the… on the… there was a GitHub issue, let me see if I find it… Do we have it in the meeting notes?
Was it this one?
Yes, I think this one, I'll carry that over.
Alexey A 00:08:09 I think the…
Felix Geisendörfer 00:08:11 The last comment there was basically that we have to wait for the collector upgrade to 1.8, and I don't know if that has happened already.
Christos Kalkanis 00:08:19 Yeah, that, that took place.
Felix Geisendörfer 00:08:22 Okay, so this is unblocked now.
Christos Kalkanis 00:08:25 over here.
Alexey A 00:08:26 Why is collector a prerequisite? Like, this is supposed to be a part of Collector, or.
Felix Geisendörfer 00:08:33 So this, is a pull request to do that in the collector as part of a receiver for PProf, so I think the idea is that you can send… you can send PPROFs to it, and I guess part of the testing is to just convert PProf to hotel and backs to make sure that the code transformation from PPROF to hotel is sound.
Alexey A 00:08:53 Okay, I should take a look at that. Can you add a link?
Felix Geisendörfer 00:08:58 Yeah, yeah, yeah, link.
Alexey A 00:09:01 Oh, okay.
Felix Geisendörfer 00:09:01 Link to…
Florian Lehner 00:09:02 As I already looked into this, I can also help out on this one.
Okay, so, but let's firstly, Florian, you said, the 1.8 upgrade, or who said it, was Geocrystals?
Christos Kalkanis 00:09:19 Yeah, yeah. Yeah, so that took place.
Alexey A 00:09:25 Yeah, this whole PData thing, I'm not super familiar with it, it's… If it's a part of a collector, that means that… it's not… it's not going to be easy to have, like, a command line tool or something to convert, or… is it still… it's just, like, this P data versus just the proto? These are just, like, kind of, like, two different worlds.
Christos Kalkanis 00:09:49 Yeah, you will need to import some collector libraries in order to get access to pit data. Not the entire collector, but yeah.
Okay. It is, yeah, it's an extra layer of indirection. Ideally, we just use the proton, unfortunately.
Florian Lehner 00:10:03 Yeah, I think if we go with an independent tool, then really, like, using Proto would be easier.
For the linked PR that is part of Autel Collector Contracts, so this will completely build on the P data, not the protocol.
Alexey A 00:10:23 Okay. But having a receiver is probably more important, because that kind of, like, makes it a part of ecosystem, so…
Florian Lehner 00:10:32 Yeah, I don't think that's… yeah, yeah, yeah, makes sense.
Felix Geisendörfer 00:10:39 Yeah, so I… I think that… having both, there's nothing against having a standalone tool. I guess it has different use cases, right? The standalone tool would be for somebody who has, like, an hotel profile and wants a P-Prof, or vice versa, and that might make sense, but I think for the collector, the needs are people want to… basically write these receivers that can receive profiling data in non-OTEL formats, and make sure that they can convert those to the OTel P data in particular format properly, and as part of making sure that such a component works, they want to write, I guess, supposed round-trip tests where they convert from what they have into OTEL, and then back to what they initially had, and make sure that they didn't lose anything in the process.
Well, cheerful is actually a better example, that's not expected to round trip.
So I guess the question is, Alexi, given… so I think the urgent need that we had was to unblock this, because this is a collector contributor who basically wants to… use the signal for something, load-bearing that people might end up using. I think that is, to me, like, a little bit more urgent than the standalone tool, so… I arguably, like, if you still want to do the standalone tool, I think you can do it completely independently and not worry about this issue at all. But if you… you already have a bunch of action items here, if you want to prioritize something, I guess this could be lower priority for you then, if that makes sense.
Alexey A 00:12:46 Yeah, yeah, that sounds good. And also, like, writing another converter, I will take a look first at the collector work, and I think… Just, like, as someone who is familiar with PPROF format, I think if someone is already working on the converter, then spending my time on reviewing that work, and just… just, like, from the PROF point of view, I think this is probably more important.
then… Writing a standalone converter.
If that makes sense.
Christos Kalkanis 00:13:16 I think that the main question we're trying to answer here is whether it's possible to take people off, convert it into hotel profiling and back without the loss of information. Now, there are multiple ways to answering that question, and the one with the shortest time may be what makes the most sense to go, but it's really the question that's, Most important, because it implies that if it's not possible to convert paper of a profiling and back without loss of information, then we need to take a step back And possibly delay the alpha release candidate.
But… Yeah, so far, I mean, I'm running ahead now, because we actually have a point in the agenda, we can talk about it. So, yeah, I'll stop for now, and then circle back.
Felix Geisendörfer 00:14:13 Okay.
I guess if we… which item is set? Is it this one?
No, that's separate. Where?
Which one did you have in mind?
Christos Kalkanis 00:14:26 Felix, it's the first point, it's yours, you have it tagged. Discuss, profile sequence optimization.
Felix Geisendörfer 00:14:31 Oh, I think that, to me, is a separate issue.
Christos Kalkanis 00:14:34 Okay, yeah, maybe I can't…
Felix Geisendörfer 00:14:35 round tripping.
Christos Kalkanis 00:14:36 Right, I got confused. I think Antoine was the one who brought both issues up, so maybe that's why. Okay.
Felix Geisendörfer 00:14:43 This is not from Bockton, this is not from Antwin.
Christos Kalkanis 00:14:46 Okay.
Yeah, so Antoine opened the paper of compatibility in the Collector PR, and he ran into some trouble there.
I think part… I looked at that myself as well, and I left a comment, I think, to that. So part of the trouble to me seems like he got confused because of the… some of the documentation that we have in the profiling proto is very vague. So, for example, we're talking about the specification.
But there is no profiling specification right now. So, Antoine translated this to the frame types that we have.
And, you know, so essentially he was using… Our instructions, and reaching the wrong conclusions, and then when he tried to implement it, he did things that he shouldn't have done, so, you know, he got breakheads.
But what we can take from that is.
One, yes, we should absolutely try to help him to to make this happen, because that answers the question, proves the point that we can convert to PPROF.
We can convert from papers.
I think, Felix, in the previous meeting, you mentioned that in Datadog, you actually do the reverse. You're converting to PBrov, from motor profiling, so you were kind of confident that at least that works.
Felix Geisendörfer 00:16:06 We haven't upgraded to 1.8 yet, I think. Neyev, correct me if I'm wrong, but we're planning to do it soon.
Nayef Ghattas 00:16:12 Yeah, we are doing it for 1.7 right now, but planning to do it for 1.8 soon.
Christos Kalkanis 00:16:19 So, yeah, so we should help Antoine with SPR, but also we should, yeah, do a final pass on the proton and all the documentation strings that we have in the file, because some of those may no longer make sense and need to be changed, and also others are vague, and they refer to bits that don't exist yet, for example, the profiling specification.
We make a reference to it in the product, but we haven't actually written it.
Felix Geisendörfer 00:16:43 Yep.
I guess going forward, I think there's a group of people who are motivated to help Antoine, which is Florian, and I also said last meeting I'd help as well, if needed, so I think we have that covered, and we just need to basically Yeah, I don't know what the best step would be, is to basically ask him to upgrade his PR against 1.8, and… or one of us could try to come in and do some coding, I don't know what's easier, but we'll, I think, do that async in the PR, or in the Slack.
And then, Alexi, yeah, you'll… if you want to still do a standalone tool, and you think you can do it really fast, great, but it might just be a duplicate effort if that all the work comes together quicker.
Alexey A 00:17:29 Yeah, sounds good, I'll take a look at that work and decide.
Felix Geisendörfer 00:17:33 Okay.
Okay, let's move on to the next item here.
all review context propagation documents, has somebody had a chance? Was there more comments there? Do we still need people's… We fuse… what's the state?
Nayef Ghattas 00:18:32 I think I can give, an update on the resource definition in the OpenTyama VPF Profiler one, and maybe Ivo has, wants to… has any thoughts on the other two, but for this one, I think, Christos, you left a comment asking, sort of, what is the worst case scenario of the number of resources we could have. And after looking at the SDKs, essentially in the SDKs, resource attributes can be configured on a per-process level.
So in the absolute worst case scenario, we would have a single resource per process.
But then if we want to match the… what the SDK is doing and have the same resource attributes for profiles, then for the traces that are emitted and the metrics that are emitted in the SDK, it doesn't seem like… There might be options other than… with what they're doing. Sort of the trade-off would be either, do that split per resource, and so have repetition in resource attributes, because they don't use the dictionary right now in the hotel format, and the dictionary is only used, for example, attributes.
Or, sort of, keep the resource attributes split more high level.
But in that case, the sample attributes will be able to reuse the dictionary, but we'll have the dictionary link repeated in each, in each of the sample.
So, it's unclear what… would be the best path forward there. I'm planning to sort of update the document to indicate all that and weigh the trade-offs, but I'm curious to know if anyone had any early thoughts on this.
Felix Geisendörfer 00:20:23 Can you just say the last thing again, so we can accept the cardinality issue of the resource attribute duplication, or the alternative is to… how do we avoid… Dad?
Nayef Ghattas 00:20:33 put, put different higher-level resource attributes, and the per-process fields, per-process ID fields would stay in sample attributes.
But then that would make us different from what the… Hotel SDKs, I'll do one.
Felix Geisendörfer 00:20:54 Okay, if somebody has thoughts, go for it.
And maybe, Nate, if you can wordsmith this a little bit in the doc. I don't think I captured this as well.
Nayef Ghattas 00:21:04 Makes sense.
Alexey A 00:21:08 Can we… can we link to that, to that comment thread?
Or to which document it is.
Nayef Ghattas 00:21:19 It's the first document, the only comment in it.
Alexey A 00:21:23 Okay.
Felix Geisendörfer 00:21:33 It's linked nope.
Christos Kalkanis 00:21:35 Okay, thanks, by the way, yeah, if you can update the document, that would be great, because then I can share it with other people, and then all the context is in the document, we don't have to…
Nayef Ghattas 00:21:43 Yep. That makes sense.
Florian Lehner 00:21:54 One request for the document.
Could you also extend by… a subsequent processor, like a resource detection and Kubernetes, or, like, Kubernetes attributes that are usually attached in the OTA collector after a receiver are not sufficient for your use case, and that's why these changes are required.
Nayef Ghattas 00:22:24 I'm not completely sure I got the… Question?
Florian Lehner 00:22:28 So, when you see the service pipelines in an auto collector, you have usually the receiver and an exporter, and in between, you can put multiple processors.
And, one of, common-use processor is, for example, the resource detection, that, enriches, that enriches, attributes and resource attributes.
I think it would be benefit if we… can… say, or if there would be a statement in the document why these… Processors, are not sufficient for the use case.
And, this points also out that, we have these, processors all in OTEL, like, resource detection, Kubernetes attributes, and you name it, and all these are working on the Kubernetes, on the hotel, resource, resource types. So, if we… decide as a group to change the resource profile's type, to, to handle the high cardinality, as pointed out earlier, then we will break everything in OTEL there, because it will not be compliant anymore. That's a concern I have.
Nayef Ghattas 00:23:46 I'm not sure I fully understand, because my belief is that right now, it's not compliant with what all the other SDKs are doing. So, I believe that the current state is that if all those processors are expecting the resource attributes to be split in the similar way that the SDKs are doing for metrics, traces, etc.
This would not work for profiles right now, because the resource represents a container and not a process.
Florian Lehner 00:24:14 We have experimented with this, and it works quite well. So, we are using the Kubernetes attribute processor and resource detection.
to enrich… Exactly this information.
Nayef Ghattas 00:24:25 So, the Kubernetes Attributes Processor is special because it only requires the container ID on the resource to be able to do the enrichment, and the resource detection processor, my belief is that the last time we discussed this, it only adds host-specific attributes to the… to the… to the payload, and not process-specific attributes, and those are the attributes we care about, and that would be set by the different SDKs on the SDK level.
Florian Lehner 00:24:58 If they settle.
Felix Geisendörfer 00:25:00 Maybe, make…
Florian Lehner 00:25:01 I suppose.
Nayef Ghattas 00:25:03 yeah, maybe I could add that to the document.
And we can discuss.
Felix Geisendörfer 00:25:08 I think having an example of where that, yeah, the enrichment that Florian mentions doesn't work, like a use case and example, would be, I think, sufficient.
Nayef Ghattas 00:25:15 Yep.
Christos Kalkanis 00:25:22 Now I just went back to the document. So, I had a follow-up question, which is, okay, so the worst case could be one resulted process, but if that's mostly theoretical, in that, you know, that depends on whether the developer has, you know, marked up processes, and… That's fine, I don't have a big problem with that. But if you look at my follow-up question in the document, there's… it's somewhere in the optical telemetry SDK documentations, there's a recommendation where if the service name is not present.
they tell you to make it up, and you make the service name up by combining the executable name. So essentially, that will force us to have one resource per process in every scenario. So then the worst case becomes the actual normal.
It shouldn't.
Nayef Ghattas 00:26:11 paper process, to be per process Right. So, for example, in the case of Python that is triggering a lot of forks, instead of having one per PID, we would have one for all the PIDs that are using the same executable name.
Christos Kalkanis 00:26:26 Right.
But I'm guessing… Yeah, so there is no point of contention there. Do we need to further clarify that with hotel, or is it something we have to abide by? That's kind of my question. Do we have to abide by that? Because if we have to abide by that, yeah, it kind of changes the equation a little bit.
Nayef Ghattas 00:26:45 I think some of it is up to us to decide if we want to have the same resource attributes as all the other signals, and be able to easily provide users with ways to correlate between signals using these attributes. We'll have to I think we'll have to abide with the same rules that the SDKs are doing.
the risk is, if we don't, is that the SDKs are going to emit data that are going to have certain resource attributes, and that the profiles will not have the same resource attributes. So if someone is a user and is searching for traces using service, I don't know, web server, then they would… Not be able to look for profiles that are using service web server.
Or something like that.
Christos Kalkanis 00:27:35 Okay.
Felix Geisendörfer 00:27:38 Sounds to me. Any follow-up, or if not, Alex, you can go next.
Alexey A 00:27:45 Actually, on this topic, I think for the document, it would be nice, and I wonder if it's possible to… list all the possible alternatives, and probably as text rather than pictures, and also add pros and cons for each of them, because I think, especially if we want to involve any other OpenTelemetry folks into the discussion, I think it's good to have kind of, like, complete picture for each alternative, and… Maybe motivation and pros and cons?
and this one specific question I had is, is the… with, resource per process, is the biggest problem, is the biggest problem is having a resource per process that are outside of containers, just because there's, like, so many of them?
because I would expect that the difference between a resource for just containerized things for, like, the run in Kubernetes.
The difference between resource per process and resource per cgroup, or per container, should not be that big, because I think in most cases there's one process inside of container anyway, but maybe I'm missing something.
And I think these other things would be nice to capture.
Nayef Ghattas 00:28:55 Yeah, I'll definitely add more details on that. The thing is, for languages that fork a lot, like PHP or Python, one container will… could map to, like, 10, 15, 20, 100 processes, depending on the configuration.
Alexey A 00:29:11 I see. I see. Okay.
Felix Geisendörfer 00:29:22 Okay, then I think next steps is, Neyev making the updates you mentioned, together with some examples of… Yeah, where the enrichment is… would be different with what you're proposing versus what can be done with these processors.
And everybody else who has thoughts, please continue commenting on the document. It keeps the discussion going there.
Let's see where… Sort of… Could speed up a little bit to get to the main agenda items. Owner wanted to create document values timestamp shape.
Does anybody have updates on that, or should we just continue carrying that forward?
Alexey A 00:30:02 I think we could cover this as part of the, of the pull request we have for this discussion of timestamps and values.
Christos Kalkanis 00:30:13 Yeah, but I have… I have an item in the agenda for that, which is Clarify714. I think that's… that's the pulley request for this.
Felix Geisendörfer 00:30:22 Okay, then… this one… Okay, so that basically is the same issue you're saying?
Christos Kalkanis 00:30:34 Yeah, I think we can discuss this when we, yeah, discuss this point.
Felix Geisendörfer 00:30:40 Okay, then… Boom.
Okay, so then I'll skip over this. Tipper of…
Alexey A 00:31:01 This is not…
Felix Geisendörfer 00:31:02 This is done. Nice. Thank you.
Mmm.
We have done top or bottom from this?
That's, like, bottom.
Okay, Jonathan sent PR for adjusting field order. Do we have Jonathan here today?
Christos Kalkanis 00:31:26 Yeah, this is…
Alexey A 00:31:28 the.
Christos Kalkanis 00:31:28 This is done. I'm not gonna open the patch.
Felix Geisendörfer 00:31:30 Oh, that's the same one, okay, okay.
Christos Kalkanis 00:31:31 Got it.
Felix Geisendörfer 00:31:32 on the agend 8… Zoom, and… This one was also completely.
Alexey A 00:31:47 Yeah, this is also done.
Felix Geisendörfer 00:31:50 Sweet, thank you.
Okay, then… I guess we can start with the full agenda. So, I want to bring up… This discussion around… Premature optimization, So this is from Bogdan, who I believe is a maintainer of the collector, maybe has some other OpenTelemetry positions. I think he's a pretty recognized figure in the community.
And he's opened a fairly vague issue initially, claiming that we're doing it wrong. And, I think we're slowly starting to get to more concrete examples, and I think, Turns out that Bogdan is thinking about… profiles being produced by SDKs rather than the eBPF profiler, and he doesn't find our… the format we designed very… targeted for that use case, which, yes, it's not. We built it for the eBPF profiler, primarily, and made sure that it could also work for the SDKs, but I think it's not… primarily SDK-focused, I guess my question here is, I think we still have discussions to do with Bogdan. My question was mostly around how the SIC fields on whether or not that should be a blocker for taking the signal to the next level or not. I personally feel… No, until Bogdan gets a little bit more specific on what his problem is and what his use case is, but I'm curious to hear all those thoughts.
Frederic Branczyk 00:33:27 I feel like an explicit goal of this was to make it also good for a system-wide profiler.
Felix Geisendörfer 00:33:37 Yes.
Frederic Branczyk 00:33:38 And that's just how it has looked then.
Felix Geisendörfer 00:33:42 Yeah, so basically, he says in the majority of the worlds that I'm a part of, I happen to know he's at Snowflake right now, so maybe they're building something themselves, or using some existing profilers. We're collecting profiling data from one process at a time.
So, yeah, of course, our format is going to look a little weird to you if that's your use case, but…
Christos Kalkanis 00:34:04 So, my impression is that we asked, I think it was either Bogdan, yeah, or maybe Antoine, I think, if I remember correctly. He was also partly involved in the discussion, maybe in the beginning, I think it was Antoine who brought this up first, and then Bogdan joined, or something like that, but anyway, so we've asked them to be more concrete, right? To bring us technical arguments. So, what exactly do they find confusing? What exactly do they find hard to do?
And, yeah, so far, I don't see… any of that. And Alexi, I think, mentioned in the previous meeting that if we don't have those technical arguments, then it's hard for us to even address the points here, if there are any points. Yeah, so from my point of view, I don't think this would be a blocker. Not at all. Actually, we should proceed with the alpha as soon as we can, in order, like, that's the point of the alpha, to actually have something that will attract more attention, so that we get more eyes to look at what we do, and then, you know, obviously, if this issue comes up again.
or other issues that maybe we've completely missed, yeah, that's partly the point of the alpha. And also, as we found out recently with Antoine going through the proto and getting confused by the documentation that we have.
Like, the more fresh eyes we have, looking at the proto.
the better product we're going to end up with, because all of us are conditioned, in a way, with profiling, and also we've been working on this a long time, and then we look at it, and we know it's parts to ignore or skip, or not pay any attention to how to resolve them subconsciously. But, you know, most new people coming at this and looking at this with fresh eyes.
We'll probably end up running into issues that we haven't even thought about.
So from that point of view, speeding up the alpha and not blocking it right now for something that's not substantial enough, I think makes sense.
Alexey A 00:35:44 Yeah, plus… plus one for me, I would also like to… it would be nice to just… because I think there was an argument, like, oh, merging this is difficult, and I was not clear, like, okay, like, how merging is more difficult when it's a global dictionary as opposed to… as opposed to per resource or per profile dictionary. I think it, yeah, like, more tech… more details would be nice, and I think just…
Felix Geisendörfer 00:36:09 I think I can explain that. It is more difficult, because you'll have to re… index all the reference in the dictionary you have from the stuff you merge in, because they will get new index numbers into the dictionary, but…
Alexey A 00:36:22 But if you merge two profiles, you also need to do the same, no?
Felix Geisendörfer 00:36:26 No, if they have their own dictionary, then you wouldn't need to merge any dictionaries.
Alexey A 00:36:30 No, I mean, like, if you merge… if I merge to this top-level protos, and then I recursively merge profiles that are within… within those.
If I do the aggregation, I still need to do the same thing, right? Because maybe I'm…
Felix Geisendörfer 00:36:43 If you merge two top-level profiles into one profile, yes, but if you just basically take two OTLP payloads that are two profiles, and then you make it an OTLP payload that's two profiles, if they each have their own dictionaries, it's much simpler to do the merging.
Alexey A 00:36:56 But I probably wouldn't want to just concatenate them, I would want to combine the dictionaries so that I minimize the space used.
Felix Geisendörfer 00:37:04 I mean, that makes sense to all of us, but apparently, to some people, the simplicity of implementation outweighs the potential benefits of actual compression you can achieve from a more complex implementation, which is what we're after here. I think it's just people looking at it from different angles.
Alexey A 00:37:20 Okay.
Florian Lehner 00:37:23 To some degree, I see the concern they have.
But I think the benefits we bring to the ecosystem are overwhelming for this purpose.
For example, if you look in OTLP and OTTL that, is using profiles, at the moment there's, I would say, non-documented gentleman agreement, that, fields in the OTL profile are read-only. They… if you change it, you will break the protocol. And, if you apply a filter processor, or any changes to the protocol, then you break something. So, yeah, I think what we can do is really improve on documentation.
And, if you look into Hotel Proto, there are also issues, that say, hey, we should introduce such, such dictionaries, also for other, other use cases, like logs, traces, and metrics. So, I think we can find both cases, depending on who's writing it.
And, with… other hotel approaches, like the, OB, the hotel EVPF-based instrumentation, they will greatly benefit for the approach that we are just, introducing. And, yeah, they're killing With logs and traces at the moment, the collector, because they don't have this optimization that we do.
Alexey A 00:39:07 One thought is that if you merge these top-level profiles.
Technically, nothing prevents you from just concatenating the top-level dictionaries and adjusting the indices.
like.
Felix Geisendörfer 00:39:21 Because that's already… Complexity, like entrusting all the indexes.
Alexey A 00:39:24 But, but then, like, yeah, adjusting, so… It seems like the implicit, or maybe explicit, requirement here… which I didn't see. I don't have a good… intuition about is… that… Some code should be able to merge.
Or concatenate payloads with minimal knowledge about the actual, like, payload internals? Is there… is this, like, collector requirement or something? I… it seems that this is where Bogdan's concern is coming from. Like, he wants to be… he wants to write some code somewhere that may be able to… to merge payloads without knowing anything about them.
Felix Geisendörfer 00:40:01 I mean, maybe I need to reread the issue, but everything I've seen so far, he's been too wake for me to really know what he is trying to do, and why he doesn't like what we're doing, and until he gets more specific, I don't think we should engage in the business of guessing what he wants to tell us, like, he should actually write it down. That would be my reference.
Alexey A 00:40:20 Then it seems, it seems, yeah, plus one to proceed, and as we proceed.
people have a chance to be more specific. One thing I also wanted to mention, that I think the discussion about resources and, the document that we discussed before, I think it's related to this, because if we make some changes there, then it may change our view on… on this… For example, if we make resources even more granular, I think we will become even more opinionated that they should be shared.
Felix Geisendörfer 00:40:56 Yep.
I mean, I don't see us moving away from the design with a global dictionary right now, I think it makes a ton of sense, but… It's not the sweet spot for everybody, but that's okay, because… We are, I think, okay with making it a little bit hotter for the… hotel components to process the signal in exchange of getting smaller sizes on the wire. This is… was a goal from the beginning in the OTEP that we had about the vision for the signal. We wanted to be… very small as we can be within the constraints of hotel.
Okay, I think we covered this, if anybody feels… Need to do more? Please speak up in 1, 2, 3… And if not, then we can go to the next item, Alexi Original Payload Format.
Alexey A 00:41:49 Sorry, just a quick note on the previous item, and I don't know what the right answer is, like, do we want to close that issue to signal that we don't plan to address it?
Felix Geisendörfer 00:41:58 No, I think that would be perceived as kind of aggressive. I don't think we have a conclusion yet, right?
Bogdan still feels like we are not understanding him, which is true, we don't, but I think he's also not put a lot of effort into understanding what we've designed and why we've done it, so I think we can just reply to him and ask for more details, point him to stuff that we have written down, and see if we can get it aligned. I wouldn't close yet.
Alexey A 00:42:20 Sounds good. Okay.
On the next one, to… yeah, I think someone asked me about this, maybe it was in the… In the hotel chat?
Yeah, we say if the original payload is in PPRO format.
It should not be included in this field.
But it was not clear… Like, it just seemed that this… document… sorry, this comment is from the very old times, and I was not sure… whether it's still applicable. I don't even remember well why we wanted the… Original payload…
Florian Lehner 00:43:04 I think at some point we had the discussion that, if the… If PPROF is fully convertible to the OTAP profiling, then there should be no need to have it as original payload in… as… in addition.
But… I think this is… Some warm months back?
And we can revisit this anyway.
Alexey A 00:43:32 Is this more about, like, lossy versus lossless? Like…
Florian Lehner 00:43:36 Would it make…
Alexey A 00:43:37 Would it make more sense to say… to say in this comment something more like, if the original payload has been converted losslessly, then we don't need to provide the original payload, or…
Florian Lehner 00:43:48 Yeah, work makes sense from my point.
Alexey A 00:43:52 Felix, do you remember? Because I've… maybe I'm thinking this out, but I have vague memory that you were one of the… one of people who wanted this field, but maybe I.
Felix Geisendörfer 00:44:03 Yes, I… yeah, I definitely think we want this field for data formats that we can only convert by losing data, and those two formats that I have in mind are execution traces from Go, as well as JFRs.
Where, like, for example, if I have an execution trace, I can extract the CPU profile out of that and put that in the hotel stuff, but I don't think I can do the… convert all the events that are in a Go execution trace into OTEL in any way that's useful. So that's the use case for putting the original payload in, and JFR also has more data than we can intelligently map to, yeah, new format. For PPROF, I guess discouraging putting original PPROFs in is probably a good idea, because we think that's gonna round trip, so I think we want to discourage that, but I think…
Alexey A 00:45:02 Is this optional overall? Like, if, like, maybe someone converted something, like, loss… in a lossy way.
But… they… they don't have good reasons to keep the… the higher fidelity by load. In that case, they don't have to, right?
Christos Kalkanis 00:45:21 Yeah, I don't think we've ever made this mandatory. It's up to the discretion of the producer, and in some, yeah, contexts, it would make sense. In others, no.
Alexey A 00:45:31 Okay.
Christos Kalkanis 00:45:33 And also, Antoine was also confused by this. It's also in his collector pull request.
Alexey A 00:45:41 Maybe I'll take a stab at improving the comment for this field, just to capture things, like, that this is kind of, like, optional, this gives a chance to the backend to keep the original higher fidelity payload, and there are some specific formats where we think this… this is not needed, such as, for example, P-Pro, because we know that they can be converted round-trip without loss. I think we're just, like, putting a bit more…
Felix Geisendörfer 00:46:08 Yeah. The reasoning… a reasoning narrative would help.
So, you could, in theory, convert PPROF in a lossy way, Like, to give one specific example, at Datadoc right now, we put timestamps in PPROFs using labels, and it's kind of messy, and… you know, OTEL supports timestamps, so we could map that one-to-one, but we could also do a receiver that Would, drop the timestamps, and just create a profile with our time information.
I don't know why we would do that, but just as an example. And then maybe retaining the original could be useful to some use cases. There might be edge cases where even the PPROF, but I think the most important thing we should tell people, if there was data loss in the conversion, then it's acceptable for producers to put the data in there. I don't think we need to go into more detail than that. We can hint at the fact that this will typically not be the case with PPROF.
Alexey A 00:47:03 Unless you do something exotic.
Okay.
Felix Geisendörfer 00:47:06 Yeah, yeah, I don't think the people we're targeting with the documentation will do exotic things of that kind. It's more like insight-based.
Alexey A 00:47:14 In many… in many cases, just having, like, a short note on the res… on, like, on the… on the motivation behind something, let's… let's people decode the rest, so I'll… I'll… I'll take a step at that.
Frederic Branczyk 00:47:27 My expectation is that probably, in reality, what's gonna happen is that For formats that have more fidelity, they're gonna be included, but it's probably… we'll probably want some functionality in the collector to be able to drop this, so that people can choose whether it goes actually over the wire and, you know, pay egress costs for this kind of stuff.
Felix Geisendörfer 00:47:55 Yeah, and I mean, even on the producer side, I think it should be configurable, like, for producers. I do agree that this is optional.
Frederic Branczyk 00:48:04 Yep.
Agreed.
Felix Geisendörfer 00:48:16 Yeah, but I would like the default to be to propagate when it's there in the collector.
If somebody's against that, let me know.
Okay, then are we done here, or somebody wants to speak up again? Alexis, your hand is up? Is that still up to date?
Alexey A 00:48:36 Sorry, this is stale.
Felix Geisendörfer 00:48:38 Still, flooring?
Florian Lehner 00:48:39 Yeah, related to this, we… in the protocol… in the protocol comment, we say, or general payload format, the expected values are defined in semantic conventions, but, we don't have that.
And, some time back, we had a discussion how this looks… could look like.
For example, you want to hint the reader of the original payload, hey, it's JFR version 123, or PPROF version 456, I don't know, just an example, but we never spoke about how this should look like.
Yeah, I think it was Jonathan who came up in the discussion with some kind of format.
Do we want to make this, or push this into semantic conventions?
So, I would say it comes down to, hey, an identifier for some kind of company or protocol.
Divided by a slash, and then followed by a numeric version.
Russian identifier.
Alexey A 00:50:04 People format, for example, doesn't really have a version.
Version component could be optional.
In general, no objection… oh, sorry, go ahead, Felix.
Felix Geisendörfer 00:50:19 Yeah, I would… I would actually be against version, just because it is a little bit more complicated, to keep that in there.
in some cases, the producer might not even know it's a version. Like, if the Go runtime, for example, gives me an execution trace, it doesn't tell me what's version is. I know the details, I can figure it out, but, like, it's… It's not, like, something that's in there. And on the other hand, the readers that I'm familiar with, I think a reader that would read JFR or Go Execution Traces is typically designed to read the latest version and older versions than that.
So I think the reader doesn't really care, it's just you need to know which reader to invoke.
Alexey A 00:50:52 Or maybe they use… or maybe they use some API, which is… and so, like, the version is transparent to them anyway.
Felix Geisendörfer 00:51:00 Sure, but what I'm saying is, I think the only reason to put version in the protocol and make it a first-class thing would be if somebody wants to filter based on that, like, in the collector, if somebody wants to drop payloads based on the version of the original payload.
And to me, I don't know a use case for that, but if we think there is one, then I would be for including it. If we don't think we have a use case for it, I would keep simple and not do that.
Jonathan Halliday (IBM) 00:51:25 I think my original intent here, from what I remember, was something similar to the way that, language or content type headers work in HTTP, in that you can specify as much detail as you like. So you can say.
language is English, or you can say language is American English, and it's kind of hierarchic, so the version could be like that. You can tack it on if you want to be specific.
Or you can just say, this is pre-prof.
Felix Geisendörfer 00:51:53 But what would be the use case for being more specific?
Jonathan Halliday (IBM) 00:52:02 The receiving end is able to choose deposits.
more fine-grained way, I guess, if it has more metadata.
It's relying on… Two versions of the thing being… compatible enough that you can… pass it, and… you know, there's file formats where they have magic bags at the beginning, they give you the version information. If you had something like that, you wouldn't need Metadata for it, because the… The metadata's inside the file format.
But if you can't even attempt to pass it unless you know what it is.
You have to have a full… Metadata to be able to choose your parser.
Alexey A 00:52:48 Yeah, I'm not familiar with any profiling format or any, like, serious format that wouldn't include such information, because…
Jonathan Halliday (IBM) 00:52:55 I hope so, yeah.
Felix Geisendörfer 00:52:58 it seems pretty useful to have that. Well, PProf is maybe the exception, but it's… I guess PProf is pretty stable at this point, and not expected to change anymore from what we heard, so… So, anyway, would the idea be to, like, basically have, like, a concatenated string, or should we, like, if we think it's useful enough to have, like, shouldn't it be a separate field? Wouldn't that make more sense than having it as a concatenated string?
Jonathan Halliday (IBM) 00:53:48 I think at this point, if we don't have a use case for it, I'd say we… Chop it from the… I'm not going to say drop it from the semantic conventions, because we haven't got semantic conventions either. I wouldn't… I wouldn't add it as a… Atlantic convention, I would just add, the semantic convention We'll just be, here are some well-known strings for the common formats, and if… If you've got one that isn't on this list, here's a suggestion of how you… Construct a volume for it.
Felix Geisendörfer 00:54:20 I think I like that, and I think that… well, no, I think that basically if people want to register new formats, they should come to the semantic conventions and add the formats there.
And… I think for formats where maybe the version is going to be needed in the future, we could also make a semantic convention for that, what the version could look like. We can do that.
Jonathan Halliday (IBM) 00:54:40 Yeah, I mean, if we don't want it to be user extensible, we can do the same thing that, you know, Ayanna or someone does with port assignments, where they just say, you know, email this person or raise a PR here to… Reserve a new value in this enum.
And we'll just start out with the semantic conventions, we'll just define Pprof and JFR, and that should be enough to get started with.
Felix Geisendörfer 00:55:04 That would make sense to me.
Okay, then I guess the, to-do that is emerging here is updating the semantic conventions, making a change for that.
Florian Lehner 00:55:36 Yeah, I can take this away. I'm just thinking about that, as we just provide, examples, like PROF, JFR, I think it would better fit into specifications rather than semantic conventions.
Because semantic conventions defines values that are used, and specification just, tells you how something can be used and gives you examples.
Felix Geisendörfer 00:56:03 Hmm.
Florian Lehner 00:56:04 I think we might end up in the specification, but, I can figure this out, and, yeah, I can do this.
Felix Geisendörfer 00:56:16 Okay, and if you need help with this, I would also be up for it, because I was asking for this. But should I put it on the to-do list under your name for now?
Florian Lehner 00:56:28 I will do it.
Felix Geisendörfer 00:56:30 Oh, you'll add one? Thank you. Okay, that's great. Then we can move on. Do we have Faprizio here asking about hotel profiling documentation?
Fabrizio Ferri Benedetti 00:56:39 Yeah, hey, hello everybody. I believe someone introduced me, at the previous meeting. I'm here, because Christian, Chris just invited me. I'm a maintainer of the OpenTermity.io documentation, and, I was wondering, like.
At which point would we be comfortable with, or at which point we feel like we'll need to have user-facing documentation on the doc site. That will be the first question, because from then on, we can decide then how to do it, which means Probably, like, opening an initial task in the OpenLimited.io repository.
To plan the scope and the content of the documentation.
Profiling is a bit special in that Currently, we don't have anything, we just have blog posts from last year announcing this initiative. There are links to the in-progress specifications and conventions, but for example, we don't have concept documentation on profiling yet.
We don't have, of course, instructions on how to use it in the collector. As far as I know, there's a feature gate, so it's not really ready for prime time.
And I guess we don't want to document the use of the binary on its own, although we could, so that's also something that we need to decide.
But yeah, so perhaps first would be more the question of the timing, like, when do we want this to happen, in the documentation? And then, it would be great to put one of you to open an issue.
in the OpenTranity.io repo, so that we can start conversations around, planning for the docs.
Felix Geisendörfer 00:58:24 Yeah, I would… guess that the answer is we should start thinking about this soon. Essentially, as we go to alpha, I think we should start thinking about documentation and start writing it.
I don't know if somebody feels we should delay after alpha significantly, but…
Christos Kalkanis 00:58:43 No, I agree. I think the sooner we start, you know, adding the documentation, thinking about the implementation, the better off we're gonna be. I introduced Fabricio, by the way, in the last meeting, but Fabricio couldn't make it then, so he joined us today. Thank you, Fabricio, for attending. The goal here is for us to Maybe have a stable version of the protocol out by end of the year, stabilize it.
you know, obviously, this is a rolling date. We're not sure if that's… we're gonna make it, but the alpha, we're hoping to get it out ASAP by end of September. Originally, it was supposed to be end of August. It got pushed back a little bit.
So, Fabricio, do you think for an alpha-vention or risk candidate, do… what sort of documentation do you think is absolutely needs to be there, if any?
Fabrizio Ferri Benedetti 00:59:31 Yeah, so it depends on, on the kind of, happy path. So, I think… We would probably need concept documentation on profiling itself.
I don't want… I don't know if… if we want to add something to the hotel demo for this, probably not in scope initially.
And then, of course, I'm thinking more of a dedicated section just on profiling, because There's a side that touches on the collector configuration. There are aspects that may be more related with language SDKs or the languages themselves, the instrumenting. So, I think it's probably best to work on a new section in the docs.
But that's… that's a conversation we can have in that initial issue, I think.
Felix Geisendörfer 01:00:18 Hey, can you drop a link here for the repo where we should open an issue to get this… get the ball rolling?
Laprizio?
Fabrizio Ferri Benedetti 01:00:31 Yeah, yeah, I think it's… it's probably better if… if it can come from some of you.
Felix Geisendörfer 01:00:36 Yeah, yeah, we're happy to do it, which is neat.
Christos Kalkanis 01:00:38 Yeah, literally.
Felix Geisendörfer 01:00:38 Where do…
Fabrizio Ferri Benedetti 01:00:40 Yeah, I'd be happy to be, like, the, you know, taking care of the next steps.
Christos Kalkanis 01:00:48 Can you add the link to the repository where we should.
Fabrizio Ferri Benedetti 01:00:50 Oh, yeah, sure.
Is our open telemetry… Are you a reaper? One second.
Paste it here in the chat. That's, that's the, that's the one.
Christos Kalkanis 01:01:03 Okay, I got a lot of the limits. Thanks.
Felix Geisendörfer 01:01:05 Okay, cool. Yes, any takers for that action item?
We're opening an issue.
Christos Kalkanis 01:01:13 Yeah, I can take it, I cannot commission.
Felix Geisendörfer 01:01:16 Okay, cool, then… I think we're basically out of time, so… but we have, I think, an answer for you. Thank you, Fabricio, for joining and bringing this up.
Fabrizio Ferri Benedetti 01:01:24 Thank you.
Felix Geisendörfer 01:01:25 And, yep.
Yes, we will… the next agenda items will have to wait till next time. But thank you, everybody, for…
Alexey A 01:01:35 For joining, and I wish you all a good local time.
Frederic Branczyk 01:01:38 Thanks, everyone. Bye.
Felix Geisendörfer 01:01:40 Take care.
