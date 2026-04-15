SIG: Specification SIG
Date: 2026-04-14
Duration: 73 minutes
============================================================

## Zoom Recording Transcript

Jack Berg 00:04:05 Alright, we're 3 minutes over.
Bogdan is supposed to be running this meeting today, but I don't see him in attendance, so… I can pick it up.
I'm gonna start sharing my screen. Please, Adam, add your items to the agenda.
And your name to the attendees list, and we'll get started in just one minute.
All right, Josh McDonald, you got the first topic.
Oh, we're doing a sampling SIG update, that's great. Our, is Josh here?
I don't see him here, so I'm going to bump that to a later part of the agenda, and if we get back to it and he arrives, we can do that then.
Florian, you have the next topic.
Florian Lehner 00:05:18 Yeah, yeah, thank you. Hi. This is more like a quick request.
The OTIP4CM19 was accepted and is merged.
And one part of it is… has a proto, proto file, and there's now a corresponding proto, PR, basically just a copy from the original, OTEP, and the ask is to have a few on the, proto file, and We want to ask if this can get merged.
At some point.
Jack Berg 00:05:57 What does Chidren have to say?
Florian Lehner 00:06:00 Okay, I didn't see Tigran's response yet.
Jack Berg 00:06:10 Right. Is this the right home for this? Is the question. And if not, where? If yes, why?
Florian Lehner 00:06:18 I would say, yes, it's the right place. The reasoning is it should be used by multiple sources, sources like SDKs, sources like OBI, sources like EBPath Profiler.
At the moment, we have a proofing concept in the eBPF profiler, but I think not every SDK should include eBPF profiler as a dependency.
That's why I think, the proto-repository is the right place.
Sure.
Josh Suereth 00:06:50 Yeah, I think you're running into a more interesting discussion. So, Let me… let me ask a related question, because I'm with… I'm with Tigrin here, of we need to make a decision first.
Okay. OTAP.
right, is a protocol for Apache Arrow.
should we have all protocols for which OpenTelemetry will interact with in the same repository? Or should each get its own repository spec standard kind of release cycle, right? So… Do you want to tie the life cycle of that proto that you're going to be recording, that is shared across everything, to the same lifecycle and release management as OTLP itself.
And if OTLP changes, should that change? Like, are they… are they related, or is this really a new protocol that deserves its own thing and attention and release cycle?
Right?
So, from my perspective, there's a piece of me that's like, honestly, it might be better if we had, like.
OTLP and… other protocols together, managed as one thing, where we, like, have a bundle and a big release, there's a piece of me that says maybe this is a separate repo. But that's how I'm viewing this, is like, what would I do for OTAP?
And then what do I do for this? Because I agree there's a lot of similarities between OTLP, and you want it to depend on those protos directly.
But kind of you're your own protocol. You might have your own versioning, right?
Is it gonna be tied one-to-one with OTLP? I don't… that I don't think so.
So that… I'm thinking while I talk, so apologies for the word vomit, but you get… you get my point.
Florian Lehner 00:08:32 Yeah, yeah, I get the point. I see it's tightly closed with, the parts in Proto already, because of the use of the common parts for resources in particular.
But I also don't see the blocker to have it now in Proto, and move it later onto our own repository. To get now the ball rolling, having it in SDKs, eBPI Profiler, OBI, use it there, it's already marked as development, so, it will not break any promises, so I would say yes, use it now in Proto, and we still can move it on to a dedicated repository or whatever at some point.
Jack Berg 00:09:20 Yeah, just a question of naming for this repository. So, it's called, OpenTelemetry Proto, not OpenTelemetry OTLP.
Right? So the name suggests that protobuf definitions, not OTLP, is the bounds for inclusion in here.
Ivo Anjo 00:09:39 Yeah, I guess I… since I opened the PR, maybe I got a bit… maybe let's call it confused on that topic as well, because, like, oh yeah, it's no TLP, it, like, looks like the right repo for it. And I think, to Florian's point, I think right now we have a bit of a problem with, let's call it distribution of this proto, because A, it depends on some of the other protos for the common stuff, and B, we have this, like, right now, we've been copy-pasting this everywhere. It's like, okay, we need this proto, copy-paste, copy, paste, copy, paste. And, we were kind of going, okay, is there, like, a nice centralized location where we can put this? And there's a bunch of mechanisms throughout the ecosystem that are already pulling from this centralized place, so this looks like a nice centralized place where we can put it, and everyone can kind of pull in and stop, like, copy-pasting the proto everywhere, yeah.
Jack Berg 00:10:39 So… Are there additional comments?
I have been doing things on the side, so I haven't been able to take notes. It would be good if somebody could Represent this conversation on a comment on that.
on this PR.
If anybody has, like, a little bit of extra capacity asynchronously, if… while we move on to the next topic.
Reiley 00:11:04 I can do it, Jack.
Jack Berg 00:11:08 Alright, thank you, Riley.
Moving on to the next topic, Robert.
Pellared 00:11:18 Hello, hello?
So, this is just asking for reviews, and I don't… it's kind of, I think, straightforward, but someone may also say if anything is wrong, regarding languages. If there are more languages, for instance, that implement implement context propagation courier, they may call it out. I made only Java and Go, because I think they are the only two implementations that are right now complying to the current state of the specification, because there are also more languages.
And I may even consider doing later, creating issues, or maybe even creating pairs for other languages. This is just creating… changing the status from alpha to beta, which kind of changes the material, just to know that In my opinion, the document is probably good enough for making this label, and then we can work on having more implementations.
Any comments?
Jack Berg 00:12:17 So, I know we have, different stability levels, development, alpha, beta, stable.
In practice, in the spec.
RC as well. In practice in the spec, I mostly see development and stable. Can you remind me what, what, you know, the distinction is between alpha and beta? Like, what additional guarantees we're making?
Pellared 00:12:37 I think it's kind of… you can start using it for production. I think Alpha is, like, pre-production… you, you know, danger, and then beta is, like.
It's not stable, but you can try testing it, if I remember correctly, according to our docs.
Jack Berg 00:12:54 Well, I have no issue with this. I just don't think that we have, you know, really used the full extent of our, you know, our status designations in other places.
approval from me. Yeah, okay.
Please go check that out, especially if you're one of the folks that has been helping to implement prototypes of this.
And then, you know, as Robert mentioned, there are some recent changes that happened to the spec here, and so Go and Java, I think, are up to date, but, you know, please check out your implementation and cross-check it against the latest spec.
And, and update it if it needs to be.
Updated.
Any other comments on this?
Pellared 00:13:41 No, we can go further.
Jack Berg 00:13:44 Alright, you have the next two topics as well, so, we'll just keep going.
Pellared 00:13:50 essentially just a reminder, like, kind of a bump, just for information. Here, we are still waiting for information from the profilerSeek, mainly from Felix, who said that he's going to check what are the, the amount, the payloads that they got in production, as far as I remember.
And yeah, that's, that's just it.
And I'm curious, I thought… I… I… okay, it's strange.
But apart from the sizes, apart from the sizes, I think, people could review this, and we may block it.
someone, I don't know, Tigran or you, Jack, can just block it, that, you know, doesn't get accidentally merged before, before we agree on the limits.
Tigran Najaryan 00:14:43 Yeah, I'm gonna block it, because I think the question we need to answer there is whether having One limit is good enough, or just the limit is good enough, or we need to have a way to also ask the senders to split the message if it is above the limit. I think that part is unclear to me, whether we want to do that or no.
Pellared 00:15:07 I was thinking about it, when I was making the fix in AutoGo, and the issue is that it's kind of mixing the responsibility of the bashing processor.
Because internally, you want the batch processor to have this, you know, batching, and then what? You're… you have some batches, and then you have the exporter, which kind of… batches it again, I'm just not… I just felt that… Yeah, maybe just… Dropping, or… yeah.
Tigran Najaryan 00:15:35 Yeah, I think, yes, I agree with you, it's on… it's a complication.
I don't… I would prefer not to have that. I'm with you, if possible.
But I don't know if we can… if it's going to work well, especially with profiling, right? Can we… Can we find a reasonable limit there that works in the vast majority? I think so.
Pellared 00:15:59 Yes, I would also prefer to have bigger limits. Like, it can be even 100MB, in my opinion.
I think it will be better, then… And also, I think that, the last resort is having this kind of splitting in the exporter as non-default implement, like, non-default behaviors and protect opt-in.
if someone wants to have, I don't know, the profiling exporter, so it may have different behavior. Also, the profiling exporters, the behavior, non-SDKs, it's not defined.
how data would be for profiling should be exported, as far as I remember.
Tigran Najaryan 00:16:37 Okay, so I guess I suggest we wait for the data from the profiling SIG, and then we'll decide how we move forward.
Jack Berg 00:16:46 Just on the splitting piece, so, I mean, I would… I would like it if, you know, we could encode more complexity in the protocol and more smarts in the OTLP clients, such that they, like, you know, intelligently split their payloads based on what the server responds with, but we haven't had anything like that up to this point.
And we've had these OTLP clients for a long time, and so, like, while it's not ideal, you know, we… it's been working, at least somewhat. Like, it sort of implies that you need to do, out-of-band configuration, and, you know, react to running into your collector's limits, which… which, again, is not ideal, but, you know, we've been getting by in some way.
Yeah, you know, just one other thought. I see two people with their hands out.
Pellared 00:17:39 I will just add one personal note. The reason also why I didn't want to add the splitting is that then you have kind of… you can go, like, almost unbounded.
So I think this is also a resistance that, you know, you can, for instance, put 2GB, and it can, you know, split, please, please, please, and you can still go, like, you can still do those just in another way, instead of big payloads, just, you know, spam with a big amount of payloads, so I was not sure if it will be, you know, a robust mechanism.
Jack Berg 00:18:09 Right.
And we've had this topic elsewhere, but, you know, you're talking about the overlapping responsibilities of the batch processor and the exporter, and so, like.
In other contexts, we've talked about how it can be tricky to know how to break up your batches from an OTLP client standpoint, because you don't necessarily know the size of your fully encoded payload before you're writing it.
And so that's… that throws, like, a wrench in this as well. Like, you know.
Pellared 00:18:39 Yes.
Jack Berg 00:18:39 In Java, I could… I could maybe, you know.
like, through the addition of complexity and, you know, overhead, you know, determine the length ahead of time and split accordingly. But it would not be trivial, and… yeah, like, I don't know. It would be a lot of work.
Tigran Najaryan 00:19:02 And it's even more complicated for profiles which use dictionary encoding. For traces and profiles, you could split on the boundary of the resource traces or resource metrics.
reasonably easily. For profiles, it's not so easy to do, because the dictionaries are shared there.
Josh T. Bagdi?
jmacdonald 00:19:28 Yeah, thank you. Just a quick note that, like, we're basically having the same discussion in the collector SIG. It's been ongoing for years, it's not easy. Splitting is hard. I'd like to bring the two together. I've been asked, or I've volunteered to write an RFC on the batch processor situation in the collector.
And it sounds like we're having this… literally the same discussion. It's really hard.
I kind of agree with Jack that, like, we've been getting by. I also sort of think that we've talked about protocol negotiation, and that's how we would solve the, like, bigger problem of, like.
Telling you the limit.
Also got a request in the collector sig for multiple limits, in effect, like, you want to have a limit on bytes and on items, which just makes it more complicated, and I don't know what to do with that, except to say it's hard, and we do need a way to split requests. In the hotel aerostig, we've got a very fancy splitter that deals with dictionaries and so on. It's a complicated algorithm, so there's no escaping. This is a really hard problem, that's all I wanted to say.
Josh Suereth 00:20:31 I'm gonna add that just from our own internal, like, performance testing, the lack of control in the SDK is a huge problem, in my opinion, like, but also from what the data shows. Tuning the collector, and I know that there's problems with the batch processor, but we… you can find It's like an art form to find the right level of batching versus segmenting, but when you find that, you can actually get really decent performance, and it's something you have to tune.
And the fact that our SDK gives you no control over that means you have one edge that's actually somewhat problematic and you cannot tune. And so, yes, we've been kind of getting by.
But, I think there's… yeah. Anyway, I think that tuning batch size versus throughput is something that we need to make sure users can do, especially at high scale.
Tigran Najaryan 00:21:25 I'm getting by, Josh, but for profiling, it may become a real problem. There, the expectation is that the payloads are going to be much larger.
Typically.
So… We've been getting by, we may not anymore, so we'll probably need to do something about it.
I cut you off.
jmacdonald 00:21:45 I just want to add that what Josh said right now is totally true. It's impossible to tune the SDK, and it's because we don't have enough knobs. The user says, oh, I'm… something's wrong with my SDK reporting, I'm going to change the batch size. But because there's no concurrency control, all you do is make large requests.
or you stall the pipeline and cause dropping. There's really no way to raise the throughput above a certain level unless you have concurrency, and that's missing from the SDKs, and that's part of the reason it's so hard to tune what Josh was just saying.
Jack Berg 00:22:21 Okay.
Let's engage on that PR.
We have to keep moving with the schedule.
The next topic, Robert?
This is the… Span Event Bridge.
Pellared 00:22:43 Exactly. So, this is a follow-up from the OTEP regarding migrating from span events to events. So, for people… so, there are already people who are asking that they have some backends, or they want to still use span events, even if the instrumentation would start using log events. So this is just a bridge, which will transform the events into the span events. So, people that, for instance, just utilize Jaeger, do not have any log backend, etc, may… may leave that, may kind of use this… use this configuration.
And this is, this is using, The pure art was mainly the Java implementation.
Based on the feedback, it has been a little bit simplified, because Java added some additional attributes, which were not systematic conventions, to put more data.
But after some discussions, we agreed that we do not need to evolve the span events, so let's just keep the semantics of the span events, so we are not, for instance, we are not, we are not setting the severity level, which is only on events.
This may help encouraging also people to start using, log-based events instead of span events. But this is also development, so based on the feedback, we may just adjust as well.
Thank you.
Jack Berg 00:24:24 Yeah, I'm just giving a little example usage here, so we can understand how, this looks from a UX standpoint.
Pellared 00:24:33 I think I also created, I think I also created a PR for configuration, if I remember correctly, but it was, like, a week ago.
Jack Berg 00:24:41 Okay.
I'm on the configuration PR.
Pellared 00:24:47 Okay. Yeah.
Jack Berg 00:24:55 Carlos, you're muted.
Carlos Alberto Cortez 00:24:57 Yeah, no, no, no, sorry for that. Yeah, I have a small question, because in that PR, not the configuration one, but the spec one.
It is, mentioned that this component would be living either in the SDK or country. I wonder if that's a good idea to keep it that open, you know?
Jack Berg 00:25:18 What, yeah, what is the motivation by, allowing this to be kept in the contrib package? I, I personally, you know, I… we have these built-in processors, built-in exporters, and I've been disappointed that there is so few. Like, I've wanted to see things like a baggage processor, for a while, that would extract data from baggage and put it onto your spans and logs. And so, like, I envision a richer ecosystem of built-in processors to do tasks.
that we expect users to commonly want to do, and this is one of them. So, I would just have this built in directly to the SDK.
What was your thought?
Pellared 00:25:57 My thought is just giving, this is development, let's, let's see what people want to prove, you know, how it goes, and just a lot of flexibility here. For instance, in Go, we often just ask staff to contribute, because everything is just almost standalone, but yeah, we can also add it to the SDK.
The problem is that if it's in the SDK, We can still emit as experimental.
Module? Yeah.
Not a deal-breaker from my perspective.
Jack Berg 00:26:29 Okay.
Bogdan, you have your hand up?
Bogdan Drutu 00:26:32 Yeah, the only question I have, to put it somewhere else, would be if we envision to have a V2, where span events will no longer be a thing.
then, you don't want to have this around in that place, correct? So that's the only reason I can think of having it in a separate report.
Jack Berg 00:26:52 The counterpoint to that is that, can you really fully get rid of span events, given the API's there? I'm under the impression that we can deprecate them.
But that the API.
Pellared 00:27:04 bogged down.
Jack Berg 00:27:04 Fantastic.
Pellared 00:27:05 to…
Jack Berg 00:27:06 Bye.
Bogdan Drutu 00:27:06 I said in a… in a future V2, so you will deprecate them right now, and then in a future V2, you… you… you may possibly remove them completely, correct? Like, then… then this play… this thing will not have a place into that world. I'm not saying that this is necessarily a strong argument, I'm saying, like, that's why… where I can… I can think of why I would put this in a… in a different level.
Jack Berg 00:27:32 I see, but in such a V2 case, you'd also have the ability to delete processors as well, because you're allowing yourself, breaking changes.
Bogdan Drutu 00:27:42 That is true. Okay, no, I'm… I'm fine both ways. I was just giving you some… some of my thinking.
Pellared 00:27:51 Thank you.
Jack Berg 00:27:54 If anybody wants to leave that comment on this PR, maybe Carlos, asynchronously, so we can continue with the agenda.
Pellared 00:28:05 I will just address it right now.
Carlos Alberto Cortez 00:28:07 Okay, thank you. I was going to, thank you.
Jack Berg 00:28:11 Alright, next, Jacob, policies OTEP.
jea 00:28:16 Hello, yes, thank you. Mostly just here to give a quick summary of the OTEP. I know it's decently long, but looking for more reviews on it, there's a few open reviews I've gone through and answered any open questions.
It is maybe too in-depth, but, let me… I'm, you know, interested to, hear any feedback, and answer any questions. To give a quick summary of it, essentially what policies are aiming to do is define a configuration for Rules that can be, worked on independently, and distributed across, not just… collectors, but also SDKs. You could imagine vendors could also run this, but really it's anyone that is in the… that wants to implement this spec, so not just within… like the OTEL ecosystem, but I've also been having conversations with some colleagues at Gravana about getting this into Prometheus and other parts of the telemetry ecosystem as well.
the… Real goal of it is to enable users to define, independent sets of configuration to… run across their environment. So, one use case that we talked about a lot in KubeCon is doing something like semantic invention, translation, where you could say.
I'm going to define a list of policies that specify how you go from version X to X plus 1 of a semantic convention, or how you go from OTel semantic convention for Kubernetes to the Prometheus naming convention, for example.
Users can then deploy this, anywhere they want, not just in the collector layer, but you could do it at the actual time of, telemetry creation as well. And it's not just for metrics, it's for logs and traces and profiles as well, though I don't have the profile, like, proto in here. Profiles would be part of this as well, obviously.
The configuration itself is what's shown on screen today, but definitely open to feedback on it. You know, the goal of the OTEP is not to define exactly what that configuration will look like. In my early implementations and proofs of concept, this is what I've been basing it off of, but definitely subject to change.
Yeah, Josh.
Josh Suereth 00:30:49 I just want to call out one of… in case you didn't see some of the performance numbers that Jacob got with this, one of the cool things about this structure, the reason why it's different than config, it's meant to be complementary.
The… the really cool thing is, because of the way policy is structured, and because of the way that this is fashioned, we can actually take a set of N policies and compress them down and kind of run them in parallel.
And that's what Jacob's prototype is doing. And so, he has really impressive performance numbers of, like, doing, you know, 10,000 policies Versus 10,000 OTTL expressions. And because they're designed to be compressed, because they're designed to be highly limited, and because they're designed to, like, for that use case, this… this has a really, really nice transformation scalability story.
And so for those of you who are running, like, a collector with 10,000 OTTL expressions, like we are, this, this is kind of a big deal.
jea 00:31:51 Yeah, thanks for calling that out, Josh.
Ted, I saw you had your hand up before, if you wanted to…
Ted Young 00:31:57 I was just gonna suggest it sounds like something that's already there is, like, concrete, you know, examples of, like, here's an example of, like, a realistic set of stuff that's grinding, you know, and here's how that… here's all the things it solves, just so it's not theoretical, but it sounds like that's already in there.
jea 00:32:15 Yeah, a lot of it is within, in order to make it a little bit easier to review, it's a lot in, like, dropdowns, so that it's not just, like, big blocks of JSON, but…
Ted Young 00:32:26 Yeah, more like, like a, yeah, like a runnable example.
jea 00:32:29 You know. Huh.
Ted Young 00:32:30 Yeah. Somewhere. But… That's fine.
jea 00:32:36 And for the trace samples in my, like, proofs of concept, I've done my best to also work off of the existing, like, hotel, conventions for… trace sampling as well, so propagating trace context and things like that as well.
Just calling that out.
Jack Berg 00:32:57 This is embedded in the details of the OTEP.
art… Is the application of these policies variant or dependent on signal? You know, like, because we have different sort of tools based on signal of where we can do filtering.
You know, traces, you can do it at the sampler level, or you can have, like, a wrapped exporter that, like, takes, like, fully, you know, ready-to-export batches and applies the different filters.
Logs, it's not easy to do at the processor level, unless you implement the filtering processor. But, you know, you can also do it at the exporter level, and… and metrics, you can do sort of with views, and, also at the exporter level, so how… I guess, like, is there a section we can focus on that defines, like, how you take this sort of, like, more general-purpose definition of, like, what you want, and how that translates to what an SDK should do about these?
jea 00:33:57 Yeah, I didn't include a bunch about that. I mean, there are sections in here that do relate to that, but the actual implementations of these things currently are… their own, sort of, components. So the goal is there… right now, there exists, like, libraries that I've developed for running these policies with the optimizations that Josh mentioned earlier.
And then the idea is that these are basically zero external dependency packages that you can just pull in to wherever in the ecosystem you need them.
So… That's really the goal of them. There is one dependency for Go that I need to work through, which is, like, a CGo dependency. But it's… that's… does that answer the question? Maybe not.
Jack Berg 00:34:45 I mean, sort of. It doesn't actually make me feel that comfortable, because, like, that's what I would be trying to evaluate as an SDK maintainer, is, like, what is the burden going to be on me to be, like, translate this abstract representation of a policy to, you know, what do I actually do about this in the SDK? Because you talked about how this can be dropped into any part of the ecosystem. Well, SDKs are part of the ecosystem.
Josh Suereth 00:35:06 Yeah, I can answer this, Jack, because I, like, I wrote that portion of the proposal. So, like, the idea here would be in the SDK, right, there's this… The policy proposal describes what the policy is and how to distribute it. In the SDK, you'd actually have a component that's policy aware. So I could say, I have a trace sampler that actually reads policies and does sampling based on the policy component. When I install that sampler in the SDK, then suddenly it tells the policy ecosystem, I can get trace sample policies and enforce them.
And then they will… then I will start enforcing them and doing them. So, like, if I have a system that doesn't want to engage with trace sampling, I don't install that policy-based sampler, and then I don't get those policies pushed down to me, is, like, the idea how this works. So basically, inside of the SDK, all our existing capabilities of sampling, of, processors, right? You would have a policy-aware version that can actually get its configuration from the policy store, and it not just gets it from there, it tells the policy store, I support this policy type, and I can enforce it.
And then that component runs. So, we can actually implement these in piecemeal, we can implement them as they're needed, we can optimize them, kind of, like, in the existing hooks we have.
But… and it interacts with configuration, right? Because in the configuration, say, you gotta have static config that says, cool, I want a policy-based, a remote policy-based span processor, I want a policy-based log processor, policy-based, you know, metric pro… measurement processor, whenever we have that kind of a thing. We have to figure out metrics a little bit here, in terms of the right hooks, but, you know, let's assume we have policy-based stuff there.
Then, I can also say, and for the policy component, I want it to connect to, like, this op-amp server, or whatever, or I want it to connect to this to get my policies from.
And so, now we have configuration, we have this dynamic policy thing with, like, high compression rates and efficiency, where I can serve, you know, thousands of these.
That's the idea behind how this all hangs together. Oh, and policies don't have to be served at any one part, like some of the log processing policies. Maybe I do them in the SDK, maybe I do them in the collector. User doesn't have to care. They just have to care that I want to do a transformation, and I want something in my pipeline to do it.
Jack Berg 00:37:33 Bogged in?
Bogdan Drutu 00:37:37 Josh?
Since you seem very familiar with this.
And you mentioned also that, config is different than this.
Can you extrapolate a bit more on that? Besides the fact that, yes, I can see that they are way more compressed.
But what else is different compared with the config that changes at runtime?
Josh Suereth 00:38:06 There's a lot of similarities, so a lot of the difference is actually in tension and purpose. So, I'll give you an example. A policy would not let you pick a pipeline. You can't do pipelining with policies. I can say I want logs to be transformed in this way.
And I would register a policy-based thing in every pipeline where I want that enforcement to happen.
But in the config, I would set up my pipelines and ecosystem and decide where policies are enforced. Policies don't care at all about the pipeline capability that configuration does care about, right? And it could be that.
Bogdan Drutu 00:38:41 Okay, okay, so…
Josh Suereth 00:38:42 Does that… does that make sense?
Bogdan Drutu 00:38:45 Yeah, yeah, makes sense, but then views should be policies.
Josh Suereth 00:38:50 Yes, actually, I… I… that's… yes. I don't think practically we can do that with how SDKs are implemented, which is why I said we need to have a discussion around that, but yeah, I do think views would effectively be policies. They're aggregation policies for metrics.
Bogdan Drutu 00:39:04 Yeah, no, no, no, I'm trying to understand… okay.
And in terms of how this would, would work with OPAM, Are we envisioning this to be a subset of what the OPAMP can do, or are we having a standalone protocol for this?
Josh Suereth 00:39:25 This would be a… oh, go ahead, Jacob, sorry.
jea 00:39:28 Yeah, so this is basically, this was born out of the fact that currently, like, op-amp doesn't have an opinion about the config that it transfers, so the design of this is such that OpAMP is just a transport mechanism for policies, where policies are the configuration.
So, if you scroll down, Jack, if you look for, policy provider, yeah, the architecture diagram.
Jack Berg 00:39:53 Oh, right here. I see it.
jea 00:39:54 Yeah. You'll see that we have, like, a lot of different… methods of providing these policies to implementations, so you could just have a file that you load with policies, or you could have an op-amp connection, which is then doing the transfer of these things. The idea here is that we actually require no modifications to the op-amp ecosystem, because everything that we really need is already supported.
Jack Berg 00:40:30 I'm gonna have to call time on us soon, so if anybody has any comments that want to take us home.
Please make them now.
Bogdan Drutu 00:40:35 Last one… Last… last one, Jack. Last one, how… we should call out… that I believe we shouldn't use these for security things. Like, we shouldn't… use this way of, for example, sending certificates and other things. I think we should keep ourselves away from that part.
jea 00:41:04 Yeah, I don't think we'll be using this for, like, certificate signing or anything like that.
Bogdan Drutu 00:41:11 Not signing, but, like, changing certificates, or things like that. Like, if you want to rotate your certificates, you shouldn't use this mechanism. I just want to call out that this is out of scope of this project, just that people are not starting using this for that.
jea 00:41:30 Yeah, definitely. In the OTEP, it's pretty constrained to just, like, the actual transformation and filtering that we care about.
Jack Berg 00:41:49 Alright.
Got to move on here.
Todd, you have the next topic.
Somehow, 5 minutes doesn't seem like it's adequate for this.
Ted Young 00:41:59 I know, I don't think we have time to really dig in on this call, given all the other things we want to talk about, but, I've run into just a pretty big bugbear here. We're… have a goal in the project of being stable by default, and this is being driven by the fact that some users, and I think a growing portion of users over time.
are going to have more and more requirements, looking at supply chain attacks and things like that, around only wanting things that have been marked post-1.0 stable, etc.
running on their machines. One question I have, that I don't have an answer for, is this just running software, or does this also include downloading the bits onto the machine and then promising not to run them?
Whether that would be bad. Seems like that would probably be bad for some people. And I want to have a better understanding about… How we can go about cleaning this up language by language.
You know, there's, like, package management in every language, but because OpenTelemetry's, you know, big cross-cutting concern. We usually have our own way of bringing with us a big bundle of software, and identifying what it is the user wants to… needs, and then matching them up.
So we already have, in every language, some way of bundling this stuff.
But it tends to bundle everything together. So trying to understand how we would split that out into a bundle of things that are stable versus a bundle of things that are unstable.
Both for that language-level package management, but also for, more system-wide package management solutions that we're looking at, like the operator and, Like regular old Linux system packages.
we would need to have a way for those to have them only, ship the stable stuff. So that's one question, is like, how do we actually split that up, given that we haven't really done it before. And I'm just looking for feedback, from maintainers about how they currently do it, and what would make sense in their language.
The other issue is that, most of the stuff we have today is what I would call de facto stable, where it's actually still marked as beta or unstable, because the semantic conventions either haven't been stabilized, or they were stabilized, and the package wasn't updated, yet, and that's due to just… we don't have a lot of people available in most languages to… to work on contribib.
But we did change our policy on that front to say it is okay to just go ahead and mark these de facto stable packages as stable. They don't have to be updated to the latest semantic convention in order to do that.
But someone would still need to go through and do that work.
So, I think probably what I need to do is just go from, like, SIG to SIG to SIG and talk to maintainers, but I'm just curious if anyone on this call has thoughts about it, or things they could point me at on, like, other examples of… Like, software regimes where they're dividing stable and unstable into two buckets.
Pellared 00:45:40 Can I jump for you?
rehearsed?
Okay, so, first of all, I think that, first of all, I think that it's great that you're… I agree that it's depending on language and com… on language and ecosystem, because I personally have different… depending on the ecosystem, I personally have, I have heard totally different points of view regarding the stability.
For instance, in .NET, I think, like, 3 years ago, before we went stable 1.0, I was very worried that we were making experimental instrumentation and marking them in… and shipping together a stable package.
And there was nobody except me.
who was against it. And personally, I have not heard about a single user that was complaining that some of the instrumentation, like semantics for the automatic instrumentation.
is changing from some time to time, that it only is in the docs. There are… we have the information docs, which instrumentation libraries are not stable.
And, so yeah, we had even a proposal that this can be controlled by environment variable if someone wants to just opt in to only stable telemetry and stable features, and nobody even upvoted this issue. And it has been, like, 3 years since it was open.
And so, this is, like, one part of the story. On the other side, we have some Autel Go users, which are very crazy in the fact that we have HTTP instrumentation, which is still experimental, and they're even… and they're even angry when we are changing The telemetry, because the semantic convection is not stable, and even though it's not stable, even though our instrumentation package is marked as not stable, they are still… they're still not happy when we are changing the telemetry.
So, and the fourth, the third, the third, like, bucket of users which I'm aware of are the collector users, and I think that these are the most ones that are, the most impact of the changes in the configuration.
And from what I see, this is the biggest, like, bucket of unhappy users, which are unhappy when they need to tackle with the changes of the auto-configure… of the configuration.
Yeah, that's everything from my side. I don't know, Ted, do you want to comment? Maybe you want… you can also say if you have other, you know, also, I do not have any numbers. Everything is just for my experience. I would love to have… I would like to have some, you know, surveys, anything like that, but I have none.
Ted Young 00:48:22 So I would say, like, you know, let's put the collector aside for now, and just focus on the language ecosystems, because… you know, I think they… we manage them a little bit separately. In terms of… you know, people who are concerned about the telemetry changing, we're definitely not saying that, it wouldn't be a major version bump to an instrumentation package if it changed its telemetry. I think it's fine to say, like.
You know, you shouldn't automatically consume a new package and have the telemetry change out from under you.
It's more about going from, you know, 0.something to 1 dot something to indicate that What we're saying is this software is safe to run.
We're not saying that the telemetry might change, but we're saying this is an experimental software that, you know, we don't security scan, or we think might blow up on your system, or, you know, we're working on it right now, and there might be bugs. We have a whole bunch of stuff that's, like, stable from that perspective.
In terms of, like, the user motivation, we're seeing this more and more in, like, just big organizations, because they tend to be the ones that are setting, kind of, like, larger-scale system-wide policies around this kind of a thing.
So I definitely would say, like, maybe your average end user working at a smaller company doesn't have a policy, you know, they're making these decisions as individuals.
But we're seeing more and more our company… people coming back and being like, we can't install OpenTelemetry because it violates this security policy that we have.
I would like to understand those policies a bit more, but that's part of why the CNCF came to us and say, as part of graduating, you know, you need to stabilize this stuff.
Logged in.
Jack Berg 00:50:14 We're well over our 5-minute limit. You know, I think we should either continue this topic and just accept that the 5 minutes was never gonna happen, and push the other topics to next week, or, you know, cut the conversation now.
Ted Young 00:50:33 I'm fine with either, don't think we can get through it all today. Bogdan, you wanna…
Bogdan Drutu 00:50:37 I'd prefer to continue this discussion, because otherwise we're gonna start again next week. You're gonna have the same topic next week, and we're gonna start from a fresh start.
Jack Berg 00:50:46 Alright, let's do that then. I'll move the remaining topics to next week's agenda. Please continue, Boggin.
Bogdan Drutu 00:50:51 Thank you, Jack. So, by the way, Ted.
One feature that I've discovered in Snowflake, which I haven't seen in other companies.
is, they call this, so they have two different, ways of graduating something. They… there is a graduation where they say the software is, GA, general available, which means it's not gonna crash, it's gonna do what it's expecting to do, and everything like that.
But then there is another way of changing some of the behaviors.
Which is a bit of a, I think it's a bit of a different process, where we say, okay, and time to time, we have this once every three months, we have a release that is a bit special, which we say it may include behavior changes, which are protected by an opt-in flag.
And then, what we do is we say, hey, we give you one release to opt-in, and then we… you have to opt out if you want, and in four… in four releases, we… you… you are forced to opt-in, essentially.
we have a very well-defined process for this, so I think what we can do here is maybe what we can do is be more aggressive on GA-ing or stabilizing this, but introduce this process of behavioral changes, where we allow people to opt in and opt out of these changes for a period of time, and we have a very, very robust Definition of that.
Ted Young 00:52:24 Yeah.
I think something I struggle with is just the fact that every language kind of does this stuff differently. So I think one action item I'm gonna take is just, like, to kind of audit how the heck we currently do this. So maybe one piece of feedback for me, like, including what you just said, Bogdan, is, like, to write down, when I'm asking people things, what… what are we… information are we trying to collect? If we were to make, kind of, a spreadsheet Like, what are the different columns in the spreadsheet that we want to understand from each… from each ecosystem?
Daniel?
Daniel Dyla (Dynatrace) 00:53:05 Yeah, I think, For one thing, I want to just answer the question you had for JS. We bundle contrib and non-contrib. We don't bundle stable and non-stable.
Right. That's just to answer that question real quick. I do think there is some tension between the idea of Contrib and the idea of stability.
The whole reason we have Contrib is because maintainers did not want to make guarantees about the packages in that repo.
About, like, maintaining, you know, time and effort.
maintenance burden and stuff like that. When those go to 1.0, that comes with an implicit promise that this is going to be maintained long-term at some level of quality, and the question is, like, who does that promise fall on?
So, things would have to be, in my opinion.
Like, that question needs to be answered. And it's fine if the answer is, this does not come with that promise.
But that needs to be very clearly communicated to both the community, for obvious reasons, and the maintainers, because right now, the maintainers, including myself, feel some, like.
hesitance and reluctance to promote things to 1.0.
in the contribib rep repository that they know they don't have time for. Like, I… if I promote the Fastify instrumentation to 1.0, And there's a bug, and that bug sits for a month and a half.
like, where does the… how does that get resolved? Because it's in Contrib because nobody had time for it. And I can tell you, at least in JS, and I think the answer is that this is probably the case.
For most of the languages, the contrib repos have tons of packages which are de facto unmaintained.
Like, they're… they were contributed 2 years ago, they may or may not work just fine.
Nobody opens issues or PRs against them, but, like, also nobody ever looks at them.
Ted Young 00:55:18 Yeah.
Yeah, it's definitely a question, but it's also, like, I feel like we're in a spot where if we just said.
hey, don't run any of the things SDK maintainers don't have time to be expedient about, that then OpenTelemetry actually isn't, like, useful, right? Like, if we today said, only run the stable stuff in OpenTelemetry.
Bogdan Drutu 00:55:42 Mr.
Ted Young 00:55:42 It would be, like.
Daniel Dyla (Dynatrace) 00:55:43 Yeah, of course, I just think it needs a very.
Bogdan Drutu 00:55:46 One more.
Daniel Dyla (Dynatrace) 00:55:46 clear distinction, like a contribib namespace in the releasing, or something like that.
Ted Young 00:55:51 Yeah.
And one thing I'm trying to figure out how to do is how to set up, you know, this stable-unstable… there's kind of a chicken or an egg. We could go back through and mark everything as stable, and then fork stuff off into an unstable package, or even delete things. But that sounds like, like, almost like a forever task.
So, I'm hoping there's a way we can come up with, like, a structure that we can create first, and then start migrating things into the stable part over time, rather than having this, like, gate all the other work that we want to do.
Bogdan, you've got your hand up.
Bogdan Drutu 00:56:32 Yeah, I think… I think, by the way, this same problem applies to our protector country, where we have tons of packages that are not stable, and we try to do a best effort. You can look at the model. We have some external maintainers, or something like that, that they are not fully maintainers of the whole thing, but they are maintainers of that, and we have a process there if something If there is an issue, and the issue is not responded within X amount of months, we mark this as unmaintained, and then we remove it eventually.
Now, this is very unfriendly for the final user.
Ted Young 00:57:16 Yep.
Boop, we lost you.
Were you done?
Jack Berg 00:57:23 Yeah, just to kind of continue where I think Bogdan was going, because he dropped off the call, it looks like, you know, you said a comment, Ted, like, if we… if we only published open telemetry with things that were stable, it wouldn't be useful. Like, so… but, like.
maybe that is hinting at just a fundamental resourcing issue with the scope that OpenTelemetry wants, and the resources that vendors and other contributors are willing to to provide through their time. And so, like, you know, you can try to patch over the problem by trying to make guarantees about things that ought not to get those guarantees, because we don't have the staffing requirements to do them, or you can let the system break And encourage vendors to allocate more resources to the project.
Ted Young 00:58:16 So I… I totally agree with those, and what I'm trying, I think, to do is find a third path, which is not to just let it all break, or demand that we pretend like we have more resources that we have, but it's more like, if we can come up with a framework for describing this, I think… And then when you combine that also with the new system-wide installers that we're doing, and saying they will only install stable things, my hope is, if we have a framework for, like, how you move things to stable, and some cheese at, you know, at the end of the rainbow for, like, motivating people to move it. We could create more visibility around this, and, like, more motivation.
To move it. I think part of the issue is, like, we've gotten by with everything just being kind of unstable, so it's like, if we don't… if we don't change that aspect of it, like, why would anybody change their behavior?
So I think that's… that's one of the things, and what's kind of, like, forcing us is, one, on one hand, graduation, and on the other hand, like, it would be very beneficial to have these system-wide installers, but I don't think We want to roll those out installing things that are unstable. Maybe we're gating that stuff a little too hard.
Daniel Dyla (Dynatrace) 00:59:36 I want to reply to that real quick, because I think it's, it is not… the carrot that you think it is. It's a stick.
Because as a maintainer, if I am hesitating to promote something to 1.0 already, and you come and say, if you promote this to 1.0, I'll include it in the auto installer, and it'll go out to everyone. I'm for sure gonna not go to 1.0.
That's… that's a reason for me to not do that, because now I was already worried about maintaining it, and now it's automatically installed to everybody, and, you know, I'm responsible for it if I mark it as 1.0. That's… that is a reason for me to not go to 1.0.
I… I see Alex in the chat mention something I was already thinking about. Like, this is… to me, this is symptomatic of… like.
we never wanted to maintain all of the instrumentation in the first place, and the… the more we make promises about our own instrumentations, the more that upstream libraries are… they're not motivated to build in first-party solutions. If there's a 1.0 officially maintained MySQL instrumentation package, why would the MySQL instrument, like, authors ever build support into their… you know, that's just taking on burden that they don't want to, that they feel like is already… well… established.
I would… severely limit scope to, like, HTTP and a couple of, like, major database instrumentations, and say, these are the ones that provide 80% of the value, and everything else is contribib, and if the MySQL authors want there to be a stable instrumentation for that, then they should make one.
Jack Berg 01:01:30 All right, time police. Sorry, we're a minute over. We want to have good time hygiene, so please pick this up at next week's meeting. I've allocated 20 minutes on a recurring basis to this topic, indefinitely, until we solve these problems, so let's continue this conversation next week. Thanks for your time, everyone.
Ted Young 01:01:48 Great, thank you all.
Reiley 01:01:51 Thank you.
David Ashpole 01:01:53 Hi, everyone.
