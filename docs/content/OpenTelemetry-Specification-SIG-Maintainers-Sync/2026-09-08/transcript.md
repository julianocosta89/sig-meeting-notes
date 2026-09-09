SIG: OpenTelemetry Specification SIG + Maintainers Sync
Date: 2026-09-08
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:06:53 Hello, hi everybody.
Robert Pająk (Splunk Inc.) 00:06:59 Oh, how are you?
Liudmila Molkova 00:07:01 I am fine, how are you?
Robert Pająk (Splunk Inc.) 00:07:04 Good, good.
Very good.
Liudmila Molkova 00:07:26 Okay, let's give people a few minutes to join.
It's my turn to run this call.
Feel free to add topics to the agenda.
If you're new to this call, not sure if anybody is new, but… You're also welcome to leave your name on the attendees list.
And while we are giving people more time to join, does anybody… would anybody be interested in coming over and giving a project update?
I think we recently onboarded Dart and FlutterSig, it would be interesting to… See people from it, and get to know them, and hear about their plans.
Is anybody from the SIG here?
Okay.
I'll probably ping them.
And we had a long-term… long plan to give an update on this… on the logs, and I… I will consider, Robert, your topic as… As this.
Robert Pająk (Splunk Inc.) 00:09:32 I think it's very reasonable.
Liudmila Molkova 00:09:39 Cool, so then let's go get started. Robert, do you want to present? Do you want me to present?
Robert Pająk (Splunk Inc.) 00:09:47 I prefer you to present, and also, Ludmud and Trask feel free to interrupt me or add any context that I will be… if I will be missing anything.
So, long story short, most of our stuff that we are working on the Lox SIG recently was about, embracing log-based events, and trying to work out on the specification on the logs API SDK to make sure that these are supported and follow the span event API deprecation plan, which the first phase was about, About enhancing the events, the events experience.
And then, once we settle that stable, it's ready, starting deprecating the Span Events API, and also possibly also record error through span, through, tracing API.
And recently, there were vacations, so, holidays, so some summer holidays, so I think it was pretty… more slower than usual.
And also, so it hasn't been a lot of movement since, like, 2 months or so.
But also, recently, we have been, we have been, I think.
We are right now in a place that we probably are starting stabilizing the stuff, so we need more audience and reviews and feedback from broader audience than just LockSIK, so that's why we decided to put this Agentic here anyway.
And one of the things that we need is to stabilize the recording exceptions document, which right now, contains, about, all, like, I think it contains 3 signals, spans, metrics, and logs, how it should be combined. Most of this document, or maybe even all of them, is currently in development status. Most of the prototypes right now are done in Java.
I know that some people saying that they will work on the Python prototypes as well, but I don't know what's the current state of the Python implementation. And this also follows the blog post where, where we say what is the current status, because I remember Daniel was also saying that right now, it's very unclear for the end users what's the current state.
So, the blog post right now, I would say we were still on the… our current state is still like this one, because we are still on, like, stabilizing the event CPI instead… the event CPI, so we are still asking the same for the operators, application developers, observability vendors, our OpenTelemetry Maintainers, I think all of these things which are listed here are still… are still valid.
And yeah, I also created today, just mainly for the tracking purposes, effort issuing somatic conventions to, to stabilize the whole, or maybe parts, how we do, the events, the events document.
Yes, the general infant somatic conventions, because a lot of things there is also, like, developed or stable, but probably a lot of the parts will get stabilized as we are going to use… we'll just create instrumentations with MIT events, then we'll have the lessons learned that are necessary to stabilize the document. There are already a few issues.
that are related to it, that needs to be probably solved, closed, or, you know… right now, they are just… I think some of them are not even have any response.
So, that's it from my site. Ludumiwat Trask, is there anything that I missed, or do you want to wrap up quickly?
Liudmila Molkova 00:13:50 No, thank you for the summary. So, if… if I can… Oh, yeah, Tigran, go ahead.
Tigran Najaryan (Splunk Inc.) 00:13:58 Yeah, just a quick question. Do you guys know how much this is going to impact the existing implementations? Do they already follow what we have in unstable docs, or this means significant rework for the instrumentations?
To match the new… the new wording of the spec.
Liudmila Molkova 00:14:20 I don't believe there are any breaking changes to the instrument… to any instrumentations, but… Some of them will need to… Grow a new feature which reports exceptions as log records.
Tigran Najaryan (Splunk Inc.) 00:14:34 We didn't record these exceptions in the past as spam events, you're saying? This is net new there?
Liudmila Molkova 00:14:41 We did, but then they would probably record them as both, and users would choose which one.
Tigran Najaryan (Splunk Inc.) 00:14:48 Okay.
Liudmila Molkova 00:14:48 And there is an opt-in flag into, logs, so exceptions would… oh, sorry, instrumentations would check if it's enabled.
Tigran Najaryan (Splunk Inc.) 00:14:58 Okay, so it's not going to be, like, a significant volume of work for OpenTelemetry as a result of stabilizing this.
We're already there.
Mostly.
Is that correct?
Liudmila Molkova 00:15:12 It is.
Trask Stalnaker (Microsoft Corporation) 00:15:13 Same thing there, and yeah, we prototyped it in Java, is just, having a flag which moves the exceptions from the span events to log-based events.
And… It was not… it wasn't relative to other semantic conventions. It's very simple.
Tigran Najaryan (Splunk Inc.) 00:15:38 It's, straightforward, I guess, yeah. Okay. Yeah. Alright, thank you.
Liudmila Molkova 00:15:53 So I think…
Trask Stalnaker (Microsoft Corporation) 00:15:54 It's… the… on… on users, I think that's, you know, the bigger… Potential impact that we have to be clear on for people.
Tigran Najaryan (Splunk Inc.) 00:16:09 Yeah, makes sense. Understood, thank you.
Liudmila Molkova 00:16:15 So we've got stuck on the prototypes for the instrumentations that would emit Exception says log records, right?
And if we resolve this, this would, help us stabilize the docu… the documents you mentioned. There are a bunch of issues here that I think are… we probably didn't resolve because we never documented the decision, but I think the decision is made For most of them.
Is it fair?
Robert Pająk (Splunk Inc.) 00:16:49 I guess this is correct. I think that some of these are also, like, mostly rewarding. So, we had some decisions, we had some discussions, but probably we have not worded it precise enough for the… for the readers of the document.
For instance, the display message of the body of the event.
The current documentation says that it is allowed to use it at the display message.
But, nothing says that it's a should, it's a may, yeah, shouldn't, yeah, accept. So, it says that it should not be used, except, but it does not say if it's a good practice to do it or not.
That was… This… what's the issue is about?
And I think we had no answer for this once we were discussing it. That's also why we worded it in this way, because we didn't have any preference. Some people prefer to not having this body, to make these locks smaller, and others wanted to have this, so… I think if anyone has some preference, I think the best way is just to Commented in the issue, and they… we should, find… we should, maybe document decision making.
What should, what is regarding… Should we have this body with display message or not? Is it a good practice or not?
Liudmila Molkova 00:18:25 I think there are two levels. The first one is semantic conventions, and in semantic conventions, we mostly define structured, events that should not have a display message. At least, yet.
But there is a guidance for whoever else who creates their logs.
And they are in a good position to decide, and we don't have a good place to document this guidance.
Right? This is something in the spec, something maybe non-normative.
Like, a best practice, or whatever.
Robert Pająk (Splunk Inc.) 00:19:12 Is it not related to the thing which CJ tried to work, to create some instrumentation guidelines?
Yeah.
Liudmila Molkova 00:19:24 But…
Robert Pająk (Splunk Inc.) 00:19:26 Was there any decision where these guidelines should be put? I remember that last time when I worked, there was a question, should it live in OpenTelemetry I.O, or the Specification? Was there any follow-up on this topic? Sorry for changing the topic, but I think it's very related anyway.
Liudmila Molkova 00:19:46 I don't remember, but I'm thinking, should it be blocking the stability? Because it's… it seems to be additive.
Robert Pająk (Splunk Inc.) 00:19:52 Yeah.
Liudmila Molkova 00:19:53 We have the body in the data model. If you want to use it, go use it. We do not recommend using it in semantic conventions.
Yep. We can.
Add the guidance, saying, okay, you may use display message.
For this and this and this purposes.
Robert Pająk (Splunk Inc.) 00:20:11 That's true, she'll be a blocker.
I agree.
Trask Stalnaker (Microsoft Corporation) 00:20:21 I think it's worth… if we're… if we have a… we're at a… have time, I don't know what's the timing look like, that would be interesting to discuss Jack's comment.
In chat.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:20:39 It seems like a Java-specific thing, possibly.
this was the… this is the whole discussion about, like, you know, I'm just thinking through what it actually means in practice to deprecate the span API… the span event API. You know, you want to say that this API that's existed is now deprecated, and tell users to use something else, the log event API, and I think that implies that the log API is now ergonomic and user-facing.
which, you know, at least in the case of Java, was not a design requirement originally, and so, we don't currently do that. And, You know, one of the key problems in OpenTelemetry Java is like, hey, if you record logs or events via our log API, it's really hard to get them to participate in the other, you know, the rest of the Java logging ecosystem. So, you know, whereas if you record a log in, you know, another logging API, let's call it LogBack or SLF4J, it's really easy to route those into OpenTelemetry. It's not easy to do the opposite.
Like, you know, start…
Trask Stalnaker (Microsoft Corporation) 00:21:46 how… How is that relevant to span events? I mean, span events didn't do that either, so what I'm kind of specifically interested in is why you consider it a blocker.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:01 I don't… I don't know what I consider it. I think it's worth thinking through. I just… like, how… the chain of reasoning is, I… how can we deprecate the span event API without having something to point people towards instead? And how can we have…
Trask Stalnaker (Microsoft Corporation) 00:22:18 Why… why can't we point people toward the existing logs API? Like, in the… in the… All the instrumentations.
I know I'm a power user, but, you know, like, it wasn't… it was pretty simple to switch the span events… logging exceptions from span events to logging exceptions via the log.
API.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:22:42 I would say, and I want to get your thoughts on this, that, like, so, okay, we now have a, like, a log API, which we're formally recommending to use.
And it's… it only partially works. It doesn't work in the way that you would expect, like, a normal log API to work, where, like, you know, it's easy to see those logs in other places besides a network exporter.
That's what we have with our, OTEL log API today. It's really easy to export those over OTLP. It's not easy to see them in the console.
Trask Stalnaker (Microsoft Corporation) 00:23:18 I mean, if somebody wanted… Was cons… wanted that, like, the, I guess it seems okay to me, like, if people want that general purpose, if they want a nice UX logging system, they can still use Log4J, log back.
And… That will, you know, we can bri- we have bridges there to… the… our exporters.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:23:49 Yeah, and I guess it's not a blocker in that sense, but it's like, you know, our guidance would be, you know, use our log API to emit these exception events, and there's, like, sort of an asterisk attached. It's not like use our log API in general.
It's use our log API for this purpose, because if you try to use our log API for a general purpose, you're going to quickly run into these issues.
Trask Stalnaker (Microsoft Corporation) 00:24:13 Okay, but we are, I mean, we are recommending, I hesitate to say we're not recommending using our log API, because we very much are for all the events that we're defining in semantic conventions these days.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:28 Yeah, and I'm saying we never completed the work on that in Java to actually make that a compelling story. It's still a bad story.
Trask Stalnaker (Microsoft Corporation) 00:24:35 Okay, okay, but not necessarily a blocker. Like, I…
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:39 The spec is all there for us to make a good story. We in OTelJava just have to, like, fix it and make it compelling.
to use…
Michele Mancioppi (Dash0 Inc.) 00:24:48 Hi, Aaron.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:24:49 API.
Michele Mancioppi (Dash0 Inc.) 00:24:50 I'm also not sure that languages other than Java have a compelling story in this.
Trask Stalnaker (Microsoft Corporation) 00:24:59 Yeah, I mean, I'm not really… I'm not… I guess I'm not convinced that we need this… I don't know, I think, we need a compelling story for log… like, as a general-purpose logging API. Like, we… want… we need a logs API for omitting events and exceptions for follow… we need a logs API for following semantic conventions, sort of, is the more… is kind of the narrower scope that I see.
the logs API. If we want to go tackle a… better UX-friendly… Java, logging API, that's something we could do, but I see that as separate from emitting semantic conventions.
Michele Mancioppi (Dash0 Inc.) 00:25:46 So, let me, to put on my particular… Focus on automatic interaction.
In a world where the user is using the operator, or is using the system packages.
to automatically inject these SDKs, the SDKs and the instrumentations.
Our expectation would be that they said something in the declarative configuration, or an environment variable.
And automatically, these log records that carry the exceptions will end up in the expected ODLP endpoint.
Right?
Trask Stalnaker (Microsoft Corporation) 00:26:26 That's exactly what happens today via what we've defined, an environment variable in semantic conventions, and Java supports that today.
Michele Mancioppi (Dash0 Inc.) 00:26:36 And, if the user does not configure an OTLP endpoint for logging, what happens?
Trask Stalnaker (Microsoft Corporation) 00:26:45 Big… nothing.
Michele Mancioppi (Dash0 Inc.) 00:26:47 So the data is lost silently.
Liudmila Molkova 00:26:50 Now wait, so users configure opt-in into logs, at least for the time being. Whatever they had, they have a span event. They… if they don't have logs endpoint, they don't opt-in into logs.
Michele Mancioppi (Dash0 Inc.) 00:27:04 Yeah, but that is a dependency that we would need to somehow clarify, that if you set up this obtain, be very sure to actually have a login point, otherwise your exceptions are gone.
That's a point I'm trying to bring across.
Trask Stalnaker (Microsoft Corporation) 00:27:19 Yeah, that was something we discussed, kind of a lot in the, event logging, kind of early, like.
issues, conflicts was backends that don't support lagging. There was some worry about that, and I mean, we… decided at that point that, you know, we really… we do want people to support logs. We do want backends to support logs. We are heavily reliant on logs for events and semantic conventions.
But yes, as Ludmila said, it is opt-in, like, you don't…
Michele Mancioppi (Dash0 Inc.) 00:28:00 Yes. And I unfortunately have not tried the specs on this matter, so if the question's already answered, I apologize in advance. But will the SDK complain loudly if you set up the opt-in without a logging A logging, producer.
Trask Stalnaker (Microsoft Corporation) 00:28:22 No, but there is a, as part of the span, event deprecation stuff, there is a… A new mechanism for routing your span events, or for your logs back to span events?
So we intentionally did not deprecate span events on OTLP, over the wire, and at the SDK level.
Michele Mancioppi (Dash0 Inc.) 00:28:49 Nice.
Trask Stalnaker (Microsoft Corporation) 00:28:50 Specifically for these use cases of backends that don't support logs.
Michele Mancioppi (Dash0 Inc.) 00:28:55 But, don't you think it would be worth to add to the SPAC that if you are going to do the dark magic of ignoring your OpTin because the rest of the configuration is not healthy, then we should tell you that?
Trask Stalnaker (Microsoft Corporation) 00:29:09 Oh, sure, open a… open an issue for that.
Michele Mancioppi (Dash0 Inc.) 00:29:12 Yes, will do.
Robert Pająk (Splunk Inc.) 00:29:16 I think we're running out of time.
Liudmila Molkova 00:29:19 Just wanted to give Matt… Matt Yudo a chance to speak up, sorry, we didn't before.
Matthew Wear (Dash0) 00:29:25 Yeah, yeah, cut me off if this is gonna be too long, but, is kind of an adjacent question, and that is, what if your logs API is not yet stable? So, like, in Ruby, we've been, not using unstable APIs in our instrumentation, because that would require people using our instrumentation to then pull in unstable APIs, and our… our logs API is not yet stable. I wonder if any other SIG is in this boat, or if everybody is actually stable, so it's not a problem.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:29:58 we… Trask can, you know, jump in here if you think I'm misspeaking, but, we accept bringing in unstable APIs as transitive dependencies in our instrumentation.
We've done that in different cases, you know, for example, we have experimental APIs around, like, you know, metric advice, and our instrumentation has needed to use those, and so the instrumentation has a transitive dependency that the user, you know, isn't, I guess, exposed to, unless they add their own direct dependency on that. But, you know, the experimental APIs are present in their application.
Trask Stalnaker (Microsoft Corporation) 00:30:41 Yeah, and it's obviously not… Ideal, but it is pragmatic.
Matthew Wear (Dash0) 00:30:49 Yeah, we've kind of been going the other route, where, like.
The user has to actually have a dependency, and if they do, then we will opt into some things, but that's, like, a pretty big pain to actually, But that's work. There's a lot of, like, special case code, and it would be, yeah, a lot better if… if we could have a transitive dependency on something unstable, but it does… technically, you know, make those APIs available in-app to anybody who finds them, unfortunately.
Michele Mancioppi (Dash0 Inc.) 00:31:20 I'm wondering, as… so, is Ted on the call?
I, I think I remember seeing a note up, maybe from him, maybe from Austin.
About the way we should go around mixing.
Stable and, unstable dependencies.
Or at least I remember one of them talking about it in the scope of Stable by Design.
Matthew Wear (Dash0) 00:31:47 Maybe I can ping Ted, and… Get an answer if he, in fact, was the one who knew about this.
Carlos Alberto Cortez 00:31:54 I mean, his PR in the community repo is still around, but, I don't know, probably he has been busy with other stuff.
Yeah.
Matthew Wear (Dash0) 00:32:04 All right, cool. I don't want to take any more time, but if anybody, yeah, if anybody has more information about this, feel free to reach out to me on Slack or anything else, because I'd like to get a better strategy for us as well, regarding unstable APIs and instrumentation.
Liudmila Molkova 00:32:23 Now, to… to close on this, it's… it's… you… if logs are unstable, probably don't migrate spend events… yet.
Trask Stalnaker (Microsoft Corporation) 00:32:33 Yeah. Prioritize stabilizing logs first.
Liudmila Molkova 00:32:38 Yeah.
Matthew Wear (Dash0) 00:32:39 Yeah, it's… it's on our list.
Liudmila Molkova 00:32:42 Awesome. Yeah.
Trask Stalnaker (Microsoft Corporation) 00:32:43 But yeah, just put this on the list down lower.
Matthew Wear (Dash0) 00:32:46 Alright.
Liudmila Molkova 00:32:50 Cool, moving on to the next topic. Appreciate everybody's thoughts on the logs. Puneet! No meter with matter configurator. Do you want to present?
Puneet Singh 00:33:00 Yeah, I think you can open the link.
Liudmila Molkova 00:33:04 Okay.
Puneet Singh 00:33:08 Right. So configurator as a concept exists across, metrics, logs, and traces, but this is specifically about the, meter configurator. So meter configurator is, experimental function on meter provider.
And it compute… it gets computed On meter creation, and has a single field, which is a Boolean-enabled field, which signifies whether the meter should be enabled or disabled.
The spec is explicit that it's not only a construction time decision, but it also, if the provider supports updating the configurator, it has to be re-invoked for every outstanding meter.
And meters then must change their behavior as per new meter config.
So, it's a kind of dynamic control, where meter can be disabled or enabled, while the application keeps running and holding the references on the same instrument.
So, with respect to the disabled state of the, meter config. It says that when disabled, it should behave like no op.
I've just mentioned them as references, but I see them as, like, coming up in two categories. One is more like a construction time no-op, which talks about that whether you should… you shouldn't validate the arguments, and also you shouldn't maintain any internal aggregator state. The bottom two are more, like, about the, dynamic control, which specifically talks about the recording NOAB behavior, that you shouldn't be recording any, any, Any readings, and storing them in internal state.
Now, the… Construction time behavior of NOAP is not quite compatible with configurator, because it's not reversible. You can enable, and disable, and then enable again, and… but if you satisfy the exact no-op behavior, the question becomes that how you're going to, regain the reference for the internal aggregator state, or in case of Sync Instruments. What about the callbacks, if you are not storing the registration?
So, it's kind of like a bit of conflict between the, the spec expectation, of the reversible behavior, and the construction time no-op, So… when it comes to, you know, like, the actual implementations, the Java implementation currently doesn't have the construction time norm. It specifically gets only the recording part.
Golang version was also converging towards the same path until, I think it was pointed out that there is a tension with the spec, and C++ has implemented the exact NOAP behavior, but they have hit the same tension that it is not quite compatible with this, reversible thing of enable and disable state, actually.
So, overall, we have, like, no SDK implementation which are matching the exact definition of NOAA, and the existing implementations are already kind of converging towards discarding the construction time NOAA behavior, so… That's the…
Liudmila Molkova 00:36:43 Okay, and the ask here is to consider about our guidance and the spec for the dynamic configuration, or… What is the… yeah.
Puneet Singh 00:36:54 Beautiful.
I mean, I would be open to other thoughts. The… I mean, from what I see here is that the construction time knob doesn't seem quite compatible with what spec wants to do. So, yeah, that's the underlying tension here.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:37:13 So, here's my read on this. So, meter configurator is experimental.
dynamic control of any SDK-level configuration is completely underspecified across the board. There's basically no text on it, and so it's the Wild West.
And so, you take something that's the Wild West, and you cross it with something that's experimental, and you're… you're sort of in… And, you're solidly in Wild West territory, and so you're gonna… you're gonna have to expect things that are, like, sort of maybe logically inconsistent or underspecified, and sort of… I think it's your job, if you want to support that thing, to… to find these inconsistencies and to… and to further specify them.
Puneet Singh 00:38:02 Right, I mean, my lean was more towards, dropping the, I mean, the way spec is written, it is meant to support the dynamic control behavior, and to me, Dropping this construction time no-op requirement makes more sense to me.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:38:26 So, construction time, no op. Like, let's elaborate on what that means a little bit here. I think what you're saying is that, you know, right now.
If… let's assume the static config situation. So, you know, you have a meter provider, which is statically configured, and some instruments are enabled, and some are disabled. And, you know, some are selectively disabled via views, or a meter configurator, or whatever.
And, because it's static, you know, when you initialize that instrumentation… that instrument, you can resolve at initialization time that it's disabled, and so you can you can have, like, sort of the code path, like, you know, change and be optimized for that. And if you want to support dynamic configuration of these instruments, then you sort of can't do that, at least in the same way, because you never know if sometime later during the application runtime, if that instrument that was initially disabled will get enabled.
And so, you sort of need to accommodate that and account for, like, hey, at any point later in the application, this instrument could be turned on.
Is that sort of what you're getting at here? Is that the tension?
Puneet Singh 00:39:41 Yes, yes. I mean, I do want to accommodate that, but I see that, you know, trying to also match with this construction time NOAA behavior is… is… unnecessary complexity. It's not like it cannot be done, but it just, doesn't make sense to introduce that kind of complexity just in order to satisfy the complete no-op behavior.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:40:18 Another kind of, angle on this is… You know, the complexity is sort of originating from the desire to have dynamic configuration, and if you drop that requirement, then the collapse… complexity collapses as well.
So, and I think that the whole notion of dynamic config is a may in the specification, and, you know, you may do this, and, you know, as we've talked about, it's sort of underspecified what happens if you do allow dynamic configuration, so… I'm not sure what the problem is. The no-op and the complexity that arise from that, or the optional dynamic config.
Puneet Singh 00:41:12 I think the tension is arising from trying to, support The optional dynamic config.
And, and trying to do it within the exact no-op behavior. Like, I would prefer… Considering it only as a… Noah behavior for the recording side, but… Discarding the construction time no op in order to support the dynamic behavior.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:41:44 Well, that sounds reasonable to me, and so if you implemented something like this in Go, and I would certainly take a look at that and use it to inform the Java implementation. I'm, you know, I'm not under the impression that what we did in Java is, like, the definitive solution. I think it needs work.
Joshua MacDonald (Microsoft) 00:42:05 I just wanted to recommend that we start thinking about disabled state as different than no-op state. So, like, you're pointing out valid observations here. You can't have a no-op with disabled state, so let's talk about, like, separating those two categories.
Thank you.
Liudmila Molkova 00:42:35 Okay.
Thank you.
Puneet Singh 00:42:38 I just wanted to ask one thing as a clarification for the path forward while this gets resolved. Is it… is it, like, okay to concede the… or to the… move the implementation forward, while keeping… keeping a partial view of the NOAP, like Josh said, that we need to separate the, what it means, separate NOAP and the disabled state. So, I take the disabled state as a, The only recording time no op, and try to go forward, or should we, discuss and solidify this as a convention, and then proceed?
Jack Berg (Raintank, Inc. – Grafana Labs) 00:43:18 I think you need to negotiate that with the… I think you're working on this in Go, correct?
Puneet Singh 00:43:22 Yes.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:43:23 So I think you need to negotiate that with the GO Maintainers. You know, whether they, sort of insist on the spec clarifying this currently under-specified area.
before moving the implementation forward. Or, you know, as we sometimes do in Java, you know, if something's underspecified, we go forward with our implementation and use the implementation as sort of guidance or, you know, a reference on how to improve or further specify things. So, Yeah, different… different SIGs have different, postures on this.
Puneet Singh 00:43:58 Got it.
Yeah, I think, yeah, that should be okay.
Liudmila Molkova 00:44:06 Awesome, thank you.
So moving on to the next topic, it's wine.
And it's for this pen type.
I've got some great feedback from Tyler, and also thanks a lot, David, for the prototypes in Go. I think all the points are addressed or replied to. I think, Tyler, maybe I wanted to… Understand better your… Concerns around uniqueness.
And talk it through.
So, for the context, the RTAP… let me know, but maybe it's a little bit too prescriptive, but I still kind of want to keep it that, there is… there is some expectation about the, spend type, format, and, It probably will be in semantic conventions rather than in Specification. Specification will not have any.
But, outside of the span type string, the… There are no… Okay, so spend type is unique within given schema URL.
So, spend types can collide between different schema URLs.
And there is no means to enforce it, and no… I don't think there is a problem because of it. We've been in this world for the last X… Years?
Even starting with OpenCensus and OpenTracing, and we… for metrics and for, for events, and… it's been manageable. Even though there could be collisions across different schema URLs, we tolerate it. It's a soft requirement. As a user, you probably know if you receive your metrics from completely different sources and they collide.
Is there, Tyler, if you can talk, is there anything we want to clarify there? Do you, consider that it's a problem?
Tyler Yahn (Splunk) 00:46:24 Yeah, yeah, no, no, exactly. I mean, I definitely see it's a problem.
Sorry, I haven't taken a look at, like, what you pushed 3 days ago, but I'm guessing, based on what I'm just reading right now, like, that seems, like.
probably okay with what I'm asking for, just, like, some sort of clarification that, like, it actually needs to be considered in the scope of the schema URL for, Matching models, specifically around, like.
remember, like, the sampler is supposed to be able to make a decision off of this, but, like, if it doesn't have access to the schema URL, like, that's gonna be important. But I'd have to double-check, I haven't taken a look at this in a little bit, but yeah, I mean, I think what you just said… Makes sense.
Liudmila Molkova 00:47:04 Yeah, thanks. Yash, take your time.
And this, probably worth mentioning that There is an issue for the instrumentation scope, to appear on the samplers.
And what I'm suggesting here… is that we're… like, whenever.
Daniel Dyla (Dynatrace) 00:47:31 Okay.
Liudmila Molkova 00:47:32 implement this.
And done?
Okay. Whenever the specific language, the SDK implements it.
It would be a good idea to also implement this to friends.
Maybe the instrumentation school, but not resource. And we will specify it, maybe in the spec during stabilization… oh, sorry, during the implementation phase.
there are interesting, like, problems and things again, Tyler, for bringing it up. There is an interesting problem of how to make it backward compatible.
And what I'm suggesting is to, when… if samplers are not designed in the way that you could add more parameters.
Find a way specific to the language that would allow to do this in the future without introducing another method.
But yeah, this friend should come together.
And I can make it more obvious in that app.
Tyler Yahn (Splunk) 00:48:42 Yeah, I mean, that seems like a reasonable approach to me. I don't know if that was specifically targeted at me as a question, but yeah, I mean, that seems… like, the right direction. I'd love to see the implementation side of things, when we get there, but, yeah, from David's prototype, I'm also, like, you know, we don't have as much of a FAD issue there, but yeah.
Liudmila Molkova 00:49:00 Okay.
Awesome, thank you. Dan, I think that's it, unless somebody else has any thoughts on the spend type.
And moving on to Trask.
Trask Stalnaker (Microsoft Corporation) 00:49:15 Yeah, just a quick ask for anyone who is, in, maintainer or approver for one of these, SIGs listed here on just a bunch of PRs. These are the… getting down to the last, ones for this rollout, So, yeah, any approvals or emerging is appreciated, and I will… bug people also via Slack or whatever. Just thought this would be an easy way to reach a bunch of people.
Liudmila Molkova 00:49:54 I see Rust here, by the way. We've had a bunch of issues with it in Weaver because of the… the very Rust-specific and Weaver-specific things, so there might be something interesting going on with Rust, where the ZSmer pipelines over… overrode the generated file.
And… That generates the file is not extensible or configurable enough to, like, set it once and for all in the config, so it won't be regenerated.
Yeah, so, or ask people, pay attention.
Trask Stalnaker (Microsoft Corporation) 00:50:38 Yeah, and if there's anything we can do on the, the shared workflow, to make that work better for REST, happy to.
Liudmila Molkova 00:50:52 Awesome, thank you. Then, Carlos, you are the next one. Oh, Josh?
Carlos Alberto Cortez 00:50:56 Sure, yeah.
Josh Suereth (Google LLC) 00:50:57 Sorry, I had my camera on, I was eating. I was gonna say, for the rest folks, it's cargo releases specifically the issue, and if we both have problems, maybe we work together and make a patch to cargo release itself, because I think it's just missing a feature we need. I think… I don't think it's anything you did, Trask.
Trask Stalnaker (Microsoft Corporation) 00:51:15 Oh, yeah, I mean more like, is there something I can do to help work around it, or make it not a problem for you all?
Josh Suereth (Google LLC) 00:51:23 No, it's literally, like, there's a feature that I think every release workflow needs, and they just don't have it. So, I think that's more the issue.
Liudmila Molkova 00:51:38 Okay.
Carlos, propagators global is not the hard requirement anymore.
Carlos Alberto Cortez 00:51:44 Yeah, this is a small reminder of this, change. As you know, we want to make global propagators an optional thing, the way Tracer provider, meter provider, and Igor provider are these days. So this is currently a high requirement, a must.
But we want to make it, a shoe.
This still would allow people, you know, to offer that if they need that, like, SIGs.
And we talk… Also, a reminder that this couldn't be a breaking thing, because we are actually going from very strict to less strict.
We have enough reviews, but I don't want people to be surprised, you know?
And actually, we are preparing the specification release for this month, So, that's also the question, whether we should include that there, or just hold it, just… You know, in case people want to be sure. As I said before, this is just relaxing.
the, the situation. For most SIGs, this means that they will be able to keep What they are doing, but yeah, this is important for people to know.
Liudmila Molkova 00:52:53 I don't see any problem merging it.
And releasing it, it's, like, even people who's not aware of it, that this is the surprise that doesn't change anything for them if they already implemented it.
Carlos Alberto Cortez 00:53:06 Yeah, exactly. I think it's mostly a thing for new changes, like Kotlin or Dart, for example, you know? And it could offer… Like, some, space, you know, for them to decide what to do.
But yeah, for existing SIGs, it's gonna be the same.
Liudmila Molkova 00:53:26 I'm not surprises.
Only positive ones.
Carlos Alberto Cortez 00:53:29 Yes.
Liudmila Molkova 00:53:34 Let's plan to merge it by the end of the week.
Carlos Alberto Cortez 00:53:37 Yeah, the question is, like, you know, since I think I will send a PR for the Specification release later today, on this, or you can do that yourself. But either way, but yeah, that was also a remaining question, whether we should hold it or just go with it. I think we can go with it. As you said, we are not breaking anything, we are just making things… More relaxed.
Liudmila Molkova 00:54:00 Maybe let's post in the Maintainers channel, or Specification channel, and if nobody objects, let's merge it by the end of the day, and then we will include it into the release.
Carlos Alberto Cortez 00:54:11 Yeah, let's do that. I would say even tomorrow, at the end of the day tomorrow, so in case people are, like, you know, like, it's almost the end of the day for most people in Europe, so yeah, let's say the end of the day tomorrow, but yeah, thank you, I will do that.
Liudmila Molkova 00:54:24 Awesome. Thank you.
Cool, this brings us to the end of the agenda, but I think, Bhaskar, you mentioned that you wanted to share Something?
Do you want to go ahead and talk about it?
Bhaskar Banerjee 00:54:41 Yes, do you think I could share my screen?
Liudmila Molkova 00:54:46 Yeah, sure, I'll give myself.
Bhaskar Banerjee 00:54:48 Thank you so much.
Liudmila Molkova 00:54:50 Go ahead.
Bhaskar Banerjee 00:54:51 So, good afternoon, everyone. My name is Bhaskar, I'm from Capital One, North America.
I'm joined with my colleague, Abiy.
Yeah. And, this is regarding a feature that… We have been working on… Do you guys see my screen? You see my…
Liudmila Molkova 00:55:10 Yep.
Bhaskar Banerjee 00:55:11 Good.
So, our team has been focusing, a lot in terms of lambdas, And, We know Lambda has this… Challenge of gold starts.
And, we have been… Considering… We have played with the OpTeleCollector extension.
the SDK.
Et cetera, et cetera.
And after one of that… We found the route of… loud watch, I mean… to be… And alternate… alternate path for… lambdas, which… have troubles.
Either in… Accepting a cold start with that much latency.
Or not having an allowance for provision concurrency, a way to offset that.
We looked into different languages that… What support they have.
Jabo.
Has some of that support.
Plumb Python and Node do not.
Go and Rust.
can do it.
So, a question was, That… From the exporter's perspective.
We know that the console Explorer is not very much recommended for production.
But would the JSON logging exporter be considered.
could that be considered as an option? And if yes.
One thing that we are trying to do there is… make it… more suitable for CloudWatch, so that People who are leveraging the drought.
Could do it.
Lord ease.
across Java… JavaScript, and Python.
And for that, the ask is, would the community be open To consider that as part of the open source, or do you think they should be kept separate?
So, you guys are seeing here, there's this OTLP JSON exporter that exists.
And we can leverage this.
to export.
all these signals to CloudWatch.
And… Route data from there.
would the community be open for something like this in Python?
and JavaScript.
This doesn't exist there.
And secondly, Would the community be open to some more… Nuances being introduced.
in these exporters.
So that it better suits the… CloudWatch world. There are a few tweaks that could be done here so that things can become… Easier, things can be compressed.
Become… be made more effective.
That's what the question is.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:58:48 Alright, so… the OTLP JSON logging exporters. That's a Java-specific naming convention, and, of a concept that exists at the spec level. I've sent a link to the spec concept, It's called the OTLP File Exporter. It's the same principle. You take the JSON encoding of an OTLP, a payload, and you, you print it out in, you know, what's it called? The JSON lines file format, where it's, like, one JSON payload per line, so that you can deliver.
Bhaskar Banerjee 00:59:24 But I'm.
Jack Berg (Raintank, Inc. – Grafana Labs) 00:59:25 line breaks. And so this already exists in a language-agnostic way. I'm not sure of the implementation status of Python in JavaScript. You can certainly, you know, present this spec as, you know, a rationale for adding an implementation to Python or JavaScript if they don't have this today.
And, you know, in terms of tooling for configuring this across languages, so that's declarative configuration, you know, the YAML file-based configuration format, and so, you know, this OTLP file exporter shows up in the declarative config schema, but again, because this whole OTLP file exporter Specification is in development still, it hasn't reached stability, so, you know, the corresponding types in the declarative config.json schema are experimental as well, so… I would like to see this move forward to stable. I think it's sort of lingered in the development status for too long. There's nothing really that complicated going on here, so if somebody wants to make a push to stabilize this, I would support it.
Bhaskar Banerjee 01:00:33 Sounds good. Thank you. And do you think we should raise an issue on this, a formal issue, and probably show up what we have been doing in space? Is that how we would like it to be presented?
Jack Berg (Raintank, Inc. – Grafana Labs) 01:00:46 Yeah, so that's… that's a typical process for stabilizing, is somebody just has to, like, raise the issue of, like, hey, should we stabilize this and sort of collect the implementation statuses from, the various languages? And, you know, in the process, maybe you come across various unsolved or unresolved issues.
Related to that, that are sort of blockers to stabilization, so that might happen. I won't claim that that's not possible or won't happen. So, yeah, so see if there's a stabilization issue for the OTLP file exporter already. If there's not, open one and, you know, state why you're interested in it, and try to solicit support from others, so…
Bhaskar Banerjee 01:01:29 Sounds good. Thank you. That was the reason we joined the call, to figure out the process.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:01:35 Great.
Liudmila Molkova 01:01:36 Awesome.
Bhaskar Banerjee 01:01:37 Thank you, Jack.
That's all from us.
Liudmila Molkova 01:01:39 If you're interested in the… you mentioned Python and JavaScript, it might be a good idea to either ask in the corresponding Slack channels, or join the SIG call, and see if people would be interested, there in implementation, if there isn't one already. I think you mentioned the run.
Bhaskar Banerjee 01:01:58 Sure, we'll do that.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:02:00 There might be, and it might be called something different. Like, that's… it's worth checking, because, you know, this… this… what you referenced for Java, the OTLP JSON logging exporter, that naming convention existed long before this OTLP file exporter concept was… was… was created, so… Got it, that's all.
Bhaskar Banerjee 01:02:19 We figured out.
Sure, thank you.
It's like a must.
Liudmila Molkova 01:02:26 Thank you. Then it brings us to the end of the agenda.
And thank you all for coming. See you next time.
Jack Berg (Raintank, Inc. – Grafana Labs) 01:02:35 Bye, take care.
Trask Stalnaker (Microsoft Corporation) 01:02:36 I…
Bhaskar Banerjee 01:02:37 Thank you.
